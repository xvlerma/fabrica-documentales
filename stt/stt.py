import sys, os, json, glob, subprocess
import numpy as np
def pcm(f):
    b = subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-vn','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b, np.float32)
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
m = WhisperModel(os.environ.get('STT_MODEL', 'small'), device='cpu', compute_type='int8')
res = {}
FL = [l.strip() for l in open(src) if l.strip()] if src.endswith('.txt') else sorted(glob.glob(f'{src}/*.mp4'))
for f in FL:
    n = os.path.basename(f)
    try:
        segs, info = m.transcribe(pcm(f), language=('eu' if n.endswith('_eu.mp4') else 'es'), word_timestamps=True, vad_filter=False, beam_size=5)
        S = [dict(s=round(s.start, 2), e=round(s.end, 2), t=s.text.strip(), w=[[round(w.start, 2), round(w.end, 2), w.word] for w in (s.words or [])]) for s in segs]
        res[n] = dict(dur=info.duration, segs=S)
        print(n, round(info.duration, 1), ' '.join(s['t'] for s in S)[:200], flush=True)
    except Exception as e: res[n] = dict(error=str(e)); print(n, 'ERROR', e, flush=True)
json.dump(res, open(f'{out}/stt.json', 'w'), ensure_ascii=False, indent=0)
with open(f'{out}/stt.txt', 'w') as fh:
    for n, r in res.items(): fh.write(f"## {n} ({r.get('dur', 0):.1f} s)\n" + '\n'.join(f"[{s['s']:.1f}-{s['e']:.1f}] {s['t']}" for s in r.get('segs', [])) + '\n\n')
