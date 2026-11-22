# Corta cada chunk de ElevenLabs en una pista por unidad (alineación whisper + silencios)
import sys, os, json, re, subprocess, unicodedata, difflib, urllib.request, time
import numpy as np
from faster_whisper import WhisperModel
chunks = json.load(open('jobs/e29n90/voz_chunks.json')); urls = json.load(open('voz_urls.json'))
OUT = sys.argv[1]; os.makedirs(f'{OUT}/media/e29n90/voz', exist_ok=True); os.makedirs('/tmp/vz', exist_ok=True)
from num2words import num2words
def norm(t):
    t = re.sub(r'\[[^\]]*\]', ' ', t)
    t = re.sub(r'(\d+)[.,](\d+)', lambda m: m.group(1) + ' coma ' + m.group(2), t)
    t = re.sub(r'\d+', lambda m: ' ' + num2words(int(m.group()), lang='es') + ' ', t)
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z0-9]+', t)
def pcm(f):
    b = subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b, np.float32)
def silences(f):
    r = subprocess.run(['ffmpeg','-i',f,'-af','silencedetect=noise=-40dB:d=0.35','-f','null','-'],capture_output=True,text=True).stderr
    s = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; e = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    return list(zip(s, e))
m = WhisperModel('small', device='cpu', compute_type='int8')
rep = {}
for c in chunks:
    cid = c['id']; u = urls.get(cid)
    if not u: rep[cid] = 'sin url'; print(cid, 'SIN URL'); continue
    f = f'/tmp/vz/{cid}.mp3'
    for i in range(4):
        try: urllib.request.urlretrieve(u, f); break
        except Exception as e: print(cid, 'retry', e); time.sleep(5)
    dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    segs, _ = m.transcribe(pcm(f), language='es', word_timestamps=True, beam_size=5)
    W = [(w.start, w.end, w.word) for s in segs for w in (s.words or [])]
    tw = []; ti = []
    for k, (a, b, w) in enumerate(W):
        for t in norm(w): tw.append(t); ti.append(k)
    sw = []; starts = []
    for un in c['units']:
        starts.append(len(sw)); sw += norm(un['text'])
    sm = difflib.SequenceMatcher(None, sw, tw, autojunk=False); mp = {}
    for bl in sm.get_matching_blocks():
        for j in range(bl.size): mp[bl.a + j] = bl.b + j
    def tpos(i, fwd=True):
        rng = range(i, len(sw)) if fwd else range(i, -1, -1)
        for x in rng:
            if x in mp: return mp[x]
        return None
    S = silences(f); cuts = [0.0]
    for n in range(1, len(c['units'])):
        a = tpos(starts[n] - 1, False); b = tpos(starts[n], True)
        ea = W[ti[a]][1] if a is not None else cuts[-1]; sb = W[ti[b]][0] if b is not None else dur
        est = (ea + sb) / 2
        cand = sorted([(e - s, s, e) for s, e in S if e > ea - 0.05 and s < sb + 0.05 and (s + e) / 2 > cuts[-1] + 0.5], reverse=True)
        if cand: s_, e_ = max(cand[0][1], ea - 0.05), min(cand[0][2], sb + 0.05); cut = (s_ + e_) / 2
        else: cut = est
        if a is None or b is None: print(cid, 'aviso: sin anclas en unidad', n, flush=True)
        cuts.append(cut)
    cuts.append(dur); r = []
    for n, un in enumerate(c['units']):
        a, b = cuts[n], cuts[n + 1]
        o = f"{OUT}/media/e29n90/voz/{un['key']}.mp3"
        subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',f'{a:.3f}','-to',f'{b:.3f}','-i',f,
            '-af','silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.12',
            '-c:a','libmp3lame','-b:a','160k',o])
        heard = ' '.join(w for (x, y, w) in W if x >= a and y <= b + 0.05).strip()
        r.append(dict(key=un['key'], a=round(a, 2), b=round(b, 2), ratio=round(difflib.SequenceMatcher(None, norm(un['text']), norm(heard)).ratio(), 2), oye=heard[:300], txt=un['text'][:300]))
        print(cid, un['key'], round(b - a, 1), r[-1]['ratio'], flush=True)
    rep[cid] = dict(dur=dur, units=r)
json.dump(rep, open(f'{OUT}/voz_report.json', 'w'), ensure_ascii=False, indent=1)
