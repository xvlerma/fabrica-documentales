import json, os, subprocess, numpy as np
from faster_whisper import WhisperModel
OUT = '/tmp/vo'; os.makedirs(OUT, exist_ok=True)
def pcm(f):
    b = subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b, np.float32)
m = WhisperModel('medium', device='cpu', compute_type='int8'); rep = {}
for k in open('voz/check.txt').read().split():
    segs, _ = m.transcribe(pcm(f'media/e29n90/voz/{k}.mp3'), language='es', beam_size=5)
    rep[k] = ' '.join(s.text.strip() for s in segs); print(k, rep[k], flush=True)
json.dump(rep, open(f'{OUT}/check_report.json', 'w'), ensure_ascii=False, indent=1)
