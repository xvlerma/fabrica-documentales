import sys, os, json, subprocess, numpy as np
"""Un corte HLS de Moncloa con tiempo máximo por intento, y su transcripción con marcas por palabra."""
name = sys.argv[1]; out = sys.argv[2]; os.makedirs(out, exist_ok=True)
j = next(x for x in json.load(open('stt/hls.json')) if x['name'] == name)
o = f"{out}/{name}.mp4"
for k in range(5):
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-rw_timeout', '20000000', '-ss', str(j.get('ss', 0)), '-i', j['src'], '-t', str(j.get('dur', 60)),
           '-vf', 'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps=25',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', o]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=420); print(name, k, r.returncode, r.stderr[-200:], flush=True)
        if r.returncode == 0 and os.path.getsize(o) > 100000: break
    except subprocess.TimeoutExpired: print(name, k, 'timeout', flush=True)
from faster_whisper import WhisperModel
b = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', o, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
m = WhisperModel('small', device='cpu', compute_type='int8')
segs, _ = m.transcribe(np.frombuffer(b, np.float32), language='es', word_timestamps=True, beam_size=5)
S = [dict(s=round(s.start, 2), e=round(s.end, 2), t=s.text.strip(), w=[[round(w.start, 2), round(w.end, 2), w.word] for w in (s.words or [])]) for s in segs]
json.dump(S, open(f'{out}/{name}.json', 'w'), ensure_ascii=False)
for s in S: print(f"[{s['s']:.1f}-{s['e']:.1f}] {s['t']}")
