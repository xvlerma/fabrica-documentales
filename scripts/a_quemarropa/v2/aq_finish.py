"""Concat de segmentos + mezcla con la música provisional -> montaje_v1.mp4; EDL y FCPXML con TC reales."""
import json, subprocess, os, csv, html
AQ = '/home/claude/w/aq'; FPS = 25; OUT = AQ + '/entrega'; os.makedirs(OUT, exist_ok=True)
P = json.load(open(AQ + '/plan.json')); ROWS = {int(r['#']): r for r in json.load(open(AQ + '/edl.json'))}
import collections as _c
ROWS = _c.defaultdict(lambda: {'Bloque': 'APERTURA', 'Duración': '—', 'Contenido literal (voz o texto)': '', 'Texto en pantalla (+ # verificación)': '', 'Nota para el montador': '', 'Visual en pantalla (archivo de recurso)': '', 'Música / sonido': '', 'Tipo': 'apertura'}, ROWS)
def tc(t):
    f = int(round(t * FPS)); h, f = divmod(f, 3600 * FPS); m, f = divmod(f, 60 * FPS); s, f = divmod(f, FPS)
    return f'{h:02d}:{m:02d}:{s:02d}:{f:02d}'
lst = AQ + '/concat.txt'
open(lst, 'w').write(''.join(f"file '{AQ}/seg/s{s['n']:03d}.mov'\n" for s in P))
# audio: cada segmento ajustado a su duración exacta en muestras (sin deriva acumulada)
SR = 48000; raw = AQ + '/dialog.raw'
with open(raw, 'wb') as fo:
    for s in P:
        N = int(round(round(s['D'] * FPS) / FPS * SR))
        b = subprocess.run(['ffmpeg', '-v', 'error', '-i', f"{AQ}/seg/s{s['n']:03d}.mov", '-vn', '-f', 's16le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
        b = b[:N * 4] + b'\x00' * max(0, N * 4 - len(b)); fo.write(b)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-f', 's16le', '-ar', '48000', '-ac', '2', '-i', raw, '-i', AQ + '/music.wav',
                '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.89:level=false[a]',
                '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-movflags', '+faststart', OUT + '/montaje_v1.mp4'], check=True)
# EDL con TC reales
t = 0.0; rows = []
for s in P:
    D = round(s['D'] * FPS) / FPS; r = ROWS[s['n']]
    src = '; '.join(f"{os.path.basename(p)} {a:.2f}-{b:.2f}" for p, a, b in s.get('src', [])) if s.get('src') else ''
    rows.append([s['n'], r['Bloque'], tc(t), tc(t + D), f'{D:.2f}', r['Duración'], s['tipo'], src, r['Contenido literal (voz o texto)'][:200]])
    s['_in'] = t; t += D
with open(OUT + '/EDL_A_QUEMARROPA_v1_TC_reales.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';'); w.writerow(['#', 'Bloque', 'TC entrada programa', 'TC salida programa', 'Duración real', 'Duración EDL', 'Tipo', 'Fuente (archivo entrada-salida, s)', 'Contenido']); w.writerows(rows)
# FCPXML 1.9: el montaje v1 como un solo medio, troceado por filas del EDL (cada clip = una fila, con su nombre y TC reales)
fr = f'1/{FPS}s'
def rt(x): return f'{int(round(x * FPS))}/{FPS}s'
spine = []
for s in P:
    D = round(s['D'] * FPS) / FPS
    nm = html.escape(f"fila {s['n']} · {s['tipo']} · " + ROWS[s['n']]['Contenido literal (voz o texto)'][:60])
    spine.append(f'<asset-clip ref="r2" name="{nm}" offset="{rt(s["_in"])}" start="{rt(s["_in"])}" duration="{rt(D)}"/>')
x = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.9"><resources><format id="r1" name="FFVideoFormat1080p25" frameDuration="{fr}" width="1920" height="1080"/>
<asset id="r2" name="montaje_v1" start="0s" duration="{rt(t)}" hasVideo="1" hasAudio="1" format="r1" audioSources="1" audioChannels="2" audioRate="48000"><media-rep kind="original-media" src="file:./montaje_v1.mp4"/></asset></resources>
<library><event name="A quemarropa v1"><project name="A quemarropa · montaje v1 (por filas del EDL)"><sequence format="r1" duration="{rt(t)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k"><spine>
{chr(10).join(spine)}
</spine></sequence></project></event></library></fcpxml>'''
open(OUT + '/A_QUEMARROPA_v1.fcpxml', 'w').write(x)
json.dump([dict(n=s['n'], tin=s['_in'], D=round(s['D'] * FPS) / FPS, tipo=s['tipo']) for s in P], open(AQ + '/timeline.json', 'w'))
print('total', tc(t), t)
