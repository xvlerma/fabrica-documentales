import sys, os, json, subprocess
"""Corta ventanas de vídeos HLS oficiales (Moncloa) y las deja en out/ para transcribirlas y verificarlas."""
jobs = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
for j in jobs:
    o = f"{out}/{j['name']}.mp4"
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-reconnect', '1', '-reconnect_streamed', '1', '-reconnect_delay_max', '10',
           '-ss', str(j.get('ss', 0)), '-i', j['src'], '-t', str(j.get('dur', 60)),
           '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=25',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', o]
    r = subprocess.run(cmd, capture_output=True, text=True); print(j['name'], r.returncode, r.stderr[-300:], flush=True)
