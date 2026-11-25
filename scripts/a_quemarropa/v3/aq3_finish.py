"""v3: concat de seg3 + mezcla con music3 + normalización a −14,5 LUFS (dos pasadas, pico real ≤ −1 dBTP)
-> entrega3/montaje_v3.mp4; EDL v3 con TC reales y tabla TC v2 → TC v3."""
import json, subprocess, os, csv, re
AQ = '/home/claude/w/aq'; FPS = 25; OUT = AQ + '/entrega3'; os.makedirs(OUT, exist_ok=True)
P = json.load(open(AQ + '/plan3.json')); ROWS = {int(r['#']): r for r in json.load(open(AQ + '/edl.json')) if str(r['#']).isdigit()}
TL2 = {x['n']: x for x in json.load(open(AQ + '/timeline_v2.json'))}
def tc(t):
    f = int(round(t * FPS)); h, f = divmod(f, 3600 * FPS); m, f = divmod(f, 60 * FPS); s, f = divmod(f, FPS)
    return f'{h:02d}:{m:02d}:{s:02d}:{f:02d}'
SR = 48000; raw = AQ + '/dialog3.raw'; lst = AQ + '/concat3.txt'
open(lst, 'w').write(''.join(f"file '{AQ}/seg3/s{s['n']:03d}.mov'\n" for s in P))
with open(raw, 'wb') as fo:
    for s in P:
        N = int(round(round(s['D'] * FPS) / FPS * SR))
        b = subprocess.run(['ffmpeg', '-v', 'error', '-i', f"{AQ}/seg3/s{s['n']:03d}.mov", '-vn', '-f', 's16le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
        b = b[:N * 4] + b'\x00' * max(0, N * 4 - len(b)); fo.write(b)
mixwav = AQ + '/mix3.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', '48000', '-ac', '2', '-i', raw, '-i', AQ + '/music3.wav',
                '-filter_complex', '[0:a][1:a]amix=inputs=2:normalize=0:duration=first[a]', '-map', '[a]', '-c:a', 'pcm_f32le', mixwav], check=True)
os.remove(raw)
# primera pasada de medida
r = subprocess.run(['ffmpeg', '-v', 'info', '-i', mixwav, '-af', 'loudnorm=I=-14.5:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
af = (f"loudnorm=I=-14.5:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
      f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true:print_format=json,aresample=48000")
r2 = subprocess.run(['ffmpeg', '-v', 'info', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-i', mixwav, '-map', '0:v', '-map', '1:a', '-af', af,
                     '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-movflags', '+faststart', OUT + '/montaje_v3.mp4'], capture_output=True, text=True)
if r2.returncode: print(r2.stderr[-2000:]); raise SystemExit(1)
o = r2.stderr; m2 = json.loads(o[o.rindex('{'):o.rindex('}') + 1])
os.remove(mixwav)
json.dump(dict(pass1=m, pass2=m2), open(AQ + '/loud3.json', 'w'), indent=1)
# EDL v3 + TC v2 → v3
t = 0.0; rows = []
for s in P:
    D = round(s['D'] * FPS) / FPS; n = s['n']; r_ = ROWS.get(n, {})
    v2 = TL2.get(n)
    src = '; '.join(f"{os.path.basename(p)} {a:.2f}-{b:.2f}" for p, a, b in s.get('src', [])) if s.get('src') else ''
    rows.append([n, r_.get('Bloque', 'APERTURA'), tc(t), tc(t + D), f'{D:.2f}', tc(v2['tin']) if v2 else '—', f"{v2['D']:.2f}" if v2 else '—',
                 f"{t - v2['tin']:+.2f}" if v2 else '—', s['tipo'], src, (r_.get('Contenido literal (voz o texto)', '') or s.get('kind', ''))[:200]])
    s['_in'] = t; t += D
with open(OUT + '/EDL_A_QUEMARROPA_v3_TC_reales.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['#', 'Bloque', 'TC entrada v3', 'TC salida v3', 'Duración v3', 'TC entrada v2', 'Duración v2', 'Desplazamiento acumulado (s)', 'Tipo', 'Fuente (archivo entrada-salida, s)', 'Contenido'])
    w.writerows(rows)
json.dump([dict(n=s['n'], tin=s['_in'], D=round(s['D'] * FPS) / FPS, tipo=s['tipo']) for s in P], open(AQ + '/timeline3.json', 'w'))
print('total', tc(t), t, 'loud', m2.get('output_i'), m2.get('output_tp'))
