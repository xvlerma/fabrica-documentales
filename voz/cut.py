# Recorta locuciones ya grabadas en frases sueltas (sin gastar créditos): marcas por palabra de whisper
import json, os, re, subprocess, unicodedata, numpy as np
from faster_whisper import WhisperModel
OUT = '/tmp/vo'; os.makedirs(f'{OUT}/media/e29n90/voz', exist_ok=True)
def norm(t):
    t = re.sub(r'\[[^\]]*\]', ' ', t); t = unicodedata.normalize('NFD', t.lower())
    return re.findall(r'[a-z0-9]+', ''.join(c for c in t if unicodedata.category(c) != 'Mn'))
def pcm(f):
    return np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout, np.float32)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
m = WhisperModel('medium', device='cpu', compute_type='int8'); rep = []
AF = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.12'
for c in json.load(open('voz/cuts.json')):
    f = f"media/e29n90/voz/{c['src']}.mp3"
    segs, _ = m.transcribe(pcm(f), language='es', word_timestamps=True, beam_size=5)
    W = [(w.start, w.end, norm(w.word)) for s in segs for w in (s.words or [])]
    W = [(a, b, n[0]) for a, b, n in W if n]
    def find(ph):
        q = norm(ph)[:2]
        for k in range(len(W) - len(q) + 1):
            if [W[k + j][2] for j in range(len(q))] == q: return k
        return None
    a, b = 0.0, dur(f)
    if c['start']:
        k = find(c.get('wstart', c['start'])); a = (W[k - 1][1] + W[k][0]) / 2 if k else 0.0
    if c['end']:
        k = find(c.get('wend', c['end'])); b = (W[k - 1][1] + W[k][0]) / 2 if k else b
        if c['end'] == 'y habla de': b = W[k - 1][1] + 0.08
    o = f"{OUT}/media/e29n90/voz/{c['key']}.mp3"
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',f'{a:.3f}','-to',f'{b:.3f}','-i',f,'-af',AF,'-c:a','libmp3lame','-b:a','160k',o])
    s2, _ = m.transcribe(pcm(o), language='es', beam_size=5); heard = ' '.join(s.text.strip() for s in s2)
    rep.append(dict(key=c['key'], a=round(a, 2), b=round(b, 2), found=[c['start'], c['end']], heard=heard, text=c['text']))
    print(c['key'], a, b, '|', heard, flush=True)
json.dump(rep, open(f'{OUT}/cut_report.json', 'w'), ensure_ascii=False, indent=1)
