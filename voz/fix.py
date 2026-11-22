import json, os, subprocess, urllib.request
from faster_whisper import WhisperModel
urls = json.load(open('voz_urls.json')); OUT = '/tmp/vo'; os.makedirs(f'{OUT}/media/e29n90/voz', exist_ok=True)
f = '/tmp/v10.mp3'; urllib.request.urlretrieve(urls['v10'], f)
AF = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.12'
cuts = {'1e8e7c22eb': (126.92, 140.10), '011803d1b7': (140.10, 168.20), 'f97dce6e89': (168.20, 181.68)}
m = WhisperModel('medium', device='cpu', compute_type='int8'); rep = {}
for k, (a, b) in cuts.items():
    o = f'{OUT}/media/e29n90/voz/{k}.mp3'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(a), '-to', str(b), '-i', f, '-af', AF, '-c:a', 'libmp3lame', '-b:a', '160k', o])
for k, (a, b) in list(cuts.items()) + [('99b6_check', (23.36, 40.63))]:
    w = f'/tmp/{k}.wav'; subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(a), '-to', str(b), '-i', f, '-ac', '1', '-ar', '16000', w])
    segs, _ = m.transcribe(w, language='es', beam_size=5); rep[k] = ' '.join(s.text.strip() for s in segs); print(k, rep[k], flush=True)
json.dump(rep, open(f'{OUT}/fix_report.json', 'w'), ensure_ascii=False, indent=1)
