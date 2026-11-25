"""QC_informe_v3.md + contactsheet_v3.jpg (antes v2 / después v3 de cada punto corregido)."""
import json, subprocess, os, collections
from PIL import Image, ImageDraw, ImageFont
AQ = '/home/claude/w/aq'; OUT = AQ + '/entrega3'
L = json.load(open(AQ + '/plan3_log.json')); LOG = L['log3']
T2 = {x['n']: x for x in json.load(open(AQ + '/timeline_v2.json'))}; T3 = {x['n']: x for x in json.load(open(AQ + '/timeline3.json'))}
QC = json.load(open(AQ + '/qc3.json')); LO = json.load(open(AQ + '/loud3.json'))
EXTRA = json.load(open(AQ + '/qc3_extra.json')) if os.path.exists(AQ + '/qc3_extra.json') else []
def tc(t):
    if t is None: return '—'
    t = max(0, t); h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{int(h)}:{int(m):02d}:{s:05.2f}' if h else f'{int(m)}:{s:05.2f}'
GRAV = lambda i: 'P0 legal' if i in ('L-01', 'L-02', 'L-03', 'L-04', 'L-05') else ('P1 legal' if i.startswith('L-') else ('P2 texto' if i.startswith('T-') else 'estética'))
rows = []; seen = set()
for n, iid, prob, acc, est in LOG + EXTRA:
    k = (n, iid, prob)
    if k in seen: continue
    seen.add(k)
    a = T2.get(n); b = T3.get(n)
    rows.append((a['tin'] if a else 9e9, tc(a['tin']) if a else '—', tc(b['tin']) if b else 'eliminada', n, iid, prob, GRAV(iid), acc, est))
rows.sort()
md = ['# QC · montaje v3 · «Pedro Sánchez, a quemarropa» · DocuVox', '',
      f"- **Archivo:** `montaje_v3.mp4` · 1920×1080 · 25 fps · H.264 High CRF 18 · AAC 320 kbps 48 kHz · +faststart",
      f"- **Duración:** {tc(QC['total'])} (v2: 1:04:09.88; diferencia {QC['total'] - 3849.88:+.1f} s)",
      f"- **Sonoridad:** {LO['pass2'].get('output_i')} LUFS integrados · pico real {LO['pass2'].get('output_tp')} dBTP (objetivo −14,5 ±0,5 LUFS, ≤ −1 dBTP; dos pasadas)",
      f"- **Negros detectados:** {len(QC['blacks'])} · **congelados:** {len(QC['freezes'])} · **no previstos:** {len(QC['unplanned'])}", '',
      '## Tabla de correcciones', '', '| TC v2 | TC v3 | Fila | ID | Problema | Gravedad | Acción | Estado |', '|---|---|---|---|---|---|---|---|']
for _, a, b, n, iid, prob, g, acc, est in rows:
    md.append(f'| {a} | {b} | {n} | {iid} | {prob} | {g} | {acc} | {est} |')
pend = [r for r in rows if r[8] in ('pendiente', 'parcial')]
md += ['', '## Pendiente / no corregido del todo', '']
for _, a, b, n, iid, prob, g, acc, est in pend: md.append(f'- **{iid} · fila {n} ({a} → {b}):** {prob}. {acc}.')
md += ['', '## Hallazgos del QC automático sobre el v3', '']
for x in QC['unplanned']: md.append(f'- {x[0]}: {tc(x[1])}–{tc(x[2])} · filas {x[3]}')
if not QC['unplanned']: md.append('- Ninguno sin motivo.')
md += ['', '## Tabla TC v2 → TC v3', '', 'Completa, fila a fila, en `EDL_A_QUEMARROPA_v3_TC_reales.csv` (columna «Desplazamiento acumulado»).']
open(OUT + '/QC_informe_v3.md', 'w').write('\n'.join(md) + '\n')
# hoja de contactos: antes / después
fnt = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf', 18)
pts = []; done = set()
for r in rows:
    n = r[3]
    if n in done or n not in T2: continue
    done.add(n); pts.append((n, r[4]))
tiles = []
for n, iid in pts:
    a = T2[n]; b = T3.get(n)
    pair = Image.new('RGB', (960, 270), (20, 20, 20))
    for j, (mp, t) in enumerate(((AQ + '/entrega/montaje_v2.mp4', a['tin'] + min(2.0, a['D'] / 2)), (OUT + '/montaje_v3.mp4', b['tin'] + min(2.0, b['D'] / 2) if b else None))):
        if t is None: continue
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', mp, '-frames:v', '1', '-vf', 'scale=480:270', '/tmp/_cs.jpg'])
        try: pair.paste(Image.open('/tmp/_cs.jpg'), (480 * j, 0))
        except Exception: pass
    d = ImageDraw.Draw(pair); d.rectangle((0, 0, 959, 26), fill=(0, 0, 0)); d.text((6, 3), f'fila {n} · {iid} · antes {tc(a["tin"])}  |  después {tc(b["tin"]) if b else "eliminada"}', fill=(242, 255, 0), font=fnt)
    tiles.append(pair)
c = 2; rr = (len(tiles) + c - 1) // c; S = Image.new('RGB', (960 * c, 270 * rr), (0, 0, 0))
for i, t in enumerate(tiles): S.paste(t, ((i % c) * 960, (i // c) * 270))
S.save(OUT + '/contactsheet_v3.jpg', quality=72, optimize=True)
print('ok', len(rows), 'filas;', len(tiles), 'pares;', os.path.getsize(OUT + '/contactsheet_v3.jpg') // 1024, 'KB')
