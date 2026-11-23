# Recorta locuciones ya grabadas (sin gastar créditos): marcas por palabra de whisper.
# Cada entrada de voz/cuts.json: src (clave del mp3 original), key (clave del resultado), text, y
#   - start/end (un tramo), o
#   - parts: [[desde, hasta], ...] (varios tramos que se unen con una pausa corta). desde/hasta = frase del texto o null.
import json, os, re, subprocess, unicodedata, numpy as np
from faster_whisper import WhisperModel
try:
    from num2words import num2words
except Exception:
    num2words = None
OUT = '/tmp/vo'; os.makedirs(f'{OUT}/media/e29n90/voz', exist_ok=True)
def norm(t):
    t = re.sub(r'\[[^\]]*\]', ' ', t)
    if num2words: t = re.sub(r'\d+', lambda m: ' ' + num2words(int(m.group()), lang='es') + ' ', t)
    t = unicodedata.normalize('NFD', t.lower())
    return re.findall(r'[a-z0-9ñ]+', ''.join(c for c in t if unicodedata.category(c) != 'Mn'))
def pcm(f):
    return np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout, np.float32)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
m = WhisperModel('medium', device='cpu', compute_type='int8'); rep = []
AF = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.12'
for c in json.load(open('voz/cuts.json')):
    f = f"media/e29n90/voz/{c['src']}.mp3"
    segs, _ = m.transcribe(pcm(f), language='es', word_timestamps=True, beam_size=5)
    W = []
    for s in segs:
        for w in (s.words or []):
            for tok in norm(w.word): W.append((w.start, w.end, tok))
    def find(ph, after=0):
        q = norm(ph)[:4]
        for L in (len(q), 3, 2):
            qq = q[:L]
            for k in range(after, len(W) - len(qq) + 1):
                if [W[k + j][2] for j in range(len(qq))] == qq: return k
        return None
    parts = c.get('parts') or [[c.get('start'), c.get('end')]]
    segs_ = []; pos = 0; ok = True
    for a_ph, b_ph in parts:
        a, b = 0.0, dur(f)
        if a_ph:
            k = find(a_ph, pos)
            if k is None: ok = False; print('  ! no encuentro', a_ph, flush=True)
            else: a = (W[k - 1][1] + W[k][0]) / 2 if k else 0.0; pos = k
        if b_ph:
            k = find(b_ph, pos + 1)
            if k is None: ok = False; print('  ! no encuentro', b_ph, flush=True)
            else: b = W[k - 1][1] + 0.12 if k else b; pos = k
        segs_.append((a, b))
    o = f"{OUT}/media/e29n90/voz/{c['key']}.mp3"; tmp = []
    for q, (a, b) in enumerate(segs_):
        t_ = f'/tmp/cut_{q}.wav'
        subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',f'{a:.3f}','-to',f'{b:.3f}','-i',f,'-af',AF,'-ar','44100','-ac','1',t_]); tmp.append(t_)
    if len(tmp) == 1: subprocess.run(['ffmpeg','-loglevel','error','-y','-i',tmp[0],'-c:a','libmp3lame','-b:a','160k',o])
    else:
        sil = '/tmp/cut_sil.wav'; subprocess.run(['ffmpeg','-loglevel','error','-y','-f','lavfi','-i','anullsrc=r=44100:cl=mono','-t','0.35',sil])
        lst = '/tmp/cut_list.txt'; open(lst, 'w').write(''.join(f"file '{x}'\nfile '{sil}'\n" for x in tmp[:-1]) + f"file '{tmp[-1]}'\n")
        subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',lst,'-c:a','libmp3lame','-b:a','160k',o])
    s2, _ = m.transcribe(pcm(o), language='es', beam_size=5); heard = ' '.join(s.text.strip() for s in s2)
    rep.append(dict(key=c['key'], segs=[[round(a, 2), round(b, 2)] for a, b in segs_], ok=ok, heard=heard, text=c['text']))
    print(c['key'], segs_, 'OK' if ok else 'FALLO', '|', heard, flush=True)
json.dump(rep, open(f'{OUT}/cut_report.json', 'w'), ensure_ascii=False, indent=1)
