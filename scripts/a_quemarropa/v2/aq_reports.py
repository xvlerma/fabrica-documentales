"""Informes 1, 2, 3 y 5 de la ETAPA 1 (markdown)."""
import json, os, re, datetime
AQ = '/home/claude/w/aq'; OUT = AQ + '/entrega'; FPS = 25
P = {s['n']: s for s in json.load(open(AQ + '/plan.json'))}; ROWS = {int(r['#']): r for r in json.load(open(AQ + '/edl.json'))}
import collections as _c
ROWS = _c.defaultdict(lambda: {'Bloque': 'APERTURA', 'Duración': '—', 'Contenido literal (voz o texto)': '', 'Texto en pantalla (+ # verificación)': '', 'Nota para el montador': '', 'Visual en pantalla (archivo de recurso)': '', 'Música / sonido': '', 'Tipo': 'apertura'}, ROWS)
L = json.load(open(AQ + '/plan_log.json')); TL = {x['n']: x for x in json.load(open(AQ + '/timeline.json'))}
QC = json.load(open(AQ + '/qc.json')) if os.path.exists(AQ + '/qc.json') else {}
CHK = json.load(open(AQ + '/check.json')) if os.path.exists(AQ + '/check.json') else {}
NR = {d[0]: d for d in json.load(open(AQ + '/nar_rep.json'))}
def tc(t):
    f = int(round(t * FPS)); h, f = divmod(f, 3600 * FPS); m, f = divmod(f, 60 * FPS); s, f = divmod(f, FPS); return f'{h}:{m:02d}:{s:02d}:{f:02d}'
def mmss(t): return f'{int(t // 60)}:{t % 60:04.1f}'
tot = sum(round(s['D'] * FPS) / FPS for s in P.values())
# ---------------- 1 incidencias
o = ['# Informe 1 · Incidencias del montaje v2', '', f'«A quemarropa · Pedro Sánchez» · DocuVox · ETAPA 1 · {datetime.date.today():%d/%m/%Y}', '',
     f'**Duración real:** {tc(tot)} ({tot:.1f} s) · objetivo 1:02:58 (3778 s) ±3 % · desviación {((tot - 3778) / 3778 * 100):+.2f} %.', '']
o += ['## Tratamientos legales aplicados', '',
      '| Fila | Tratamiento |', '|---|---|',
      '| 142 | Audio de las mujeres: forma de onda sin imagen de personas, nombres con pitido (fuente ya tapada), tope legal de 14 s, sin música. |',
      '| 185, 186 | Testigos sin nombre: imagen difuminada a pantalla completa (desenfoque fuerte) y rótulo sin identidad. |',
      '| 282 | Menores en Ceuta: planos generales difuminados a pantalla completa. |',
      '| 402 | Audio atribuido (Argentina): voz distorsionada (tono −22 %) y sin imagen de OKDiario (forma de onda); foto, nombre y cargo fuera. |',
      '| 137, 188, 288 | Faldones de otros medios tapados con reencuadre al 125 % (se pierde la franja inferior). |',
      '| Todo el b-roll de `archivo/` y `cortes_externos/` | Reencuadre al 125 % para sacar faldones y moscas de cadena. |', '']
o += ['## Filas 🔴', '', '| Fila | Decisión |', '|---|---|',
      '| 94 | Corte de Atresmedia ≤20 s, cortado antes del tramo de Wild 2026. |',
      '| 95, 180, 388 | Ya son tarjetas Q1 en el EDL (vídeo de atresplayer fuera). |',
      '| 149, 165, 393 | Imagen de agencia con licencia: sustituida por tarjeta Q1 con el literal y su fuente, sin el audio de agencia. |',
      '| 409 | Tarjeta «COMPRUÉBALO TÚ» sobre negro, sin fondo de agencia. |', '']
o += ['## Incidencias por fila', '', '| Fila | TC programa | Incidencia |', '|---|---|---|']
for n, m in sorted(set(map(tuple, L['inc']))):
    o.append(f"| {n} | {tc(TL[n]['tin']) if n in TL else ''} | {m} |")
if QC:
    o += ['', '## Control técnico', '', f"- Negros detectados: {len(QC['blacks'])} · congelados: {len(QC['freezes'])} · silencios >1,5 s: {len(QC['silences'])}.",
          f"- No previstos: {len(QC['unplanned'])}."]
    for k, a, b, rs in QC['unplanned']: o.append(f'  - {k}: {mmss(a)}–{mmss(b)} (filas {", ".join(map(str, rs))})')
    o.append(f"- Duplicados de corte no intencionados: {len(QC['dups'])}" + ''.join(f"\n  - filas {a} y {b}: {f} {x}-{y} s" for a, b, f, x, y in QC['dups']))
    o.append(f"- Tarjeta «Consultados por DocuVox, no han respondido»: {'NINGUNA' if not QC['consultados_en_edl'] else QC['consultados_en_edl']} (EDL) · {CHK.get('consultados_audio', 'pendiente')} (retranscripción).")
    o.append(f"- Sincronía A/V: {len(QC['desync'])} segmentos con desfase >45 ms; pista de vídeo {QC['streams'].get('video', 0):.2f} s / audio {QC['streams'].get('audio', 0):.2f} s.")
if CHK:
    o += ['', '## Retranscripción del montaje frente al EDL y el Anexo A', '', f"Concordancia media de los literales: {CHK['media']:.1f} %. Filas por debajo del 80 %:", '']
    for n, sc, exp, got in CHK['bajas']: o.append(f'- **{n}** ({sc:.0f} %): esperado «{exp[:140]}» · oído «{got[:140]}»')
    o += ['', '## Literales comprobados al oído (filas pedidas)', '']
    for n, got in CHK['oido']: o.append(f'- **Fila {n}:** «{got}»')
open(OUT + '/1_INCIDENCIAS.md', 'w').write('\n'.join(o) + '\n')
# ---------------- 2 narración
o = ['# Informe 2 · Narración', '', 'Las 171 locuciones, regeneradas con el texto exacto del Anexo A.', '',
     '| Fila | Narrador | TC programa | Duración estimada (EDL) | Duración real | Diferencia | Incidencias de pronunciación |', '|---|---|---|---|---|---|---|']
te = tr = 0
for n, s in sorted(P.items()):
    if 'ocuci' not in s['tipo'].lower(): continue
    nr = NR.get(n); real = nr[2] if nr else s['D']; est = s['edl_dur']; te += est; tr += real
    pr = CHK.get('pron', {}).get(str(n), '') if CHK else ''
    if nr and not nr[4]: pr = (pr + ' · ' if pr else '') + f'ritmo alto ({nr[3]:.2f} pal./s): revisar a oído'
    o.append(f"| {n} | {'Narrador Top' if 'Top' in s['tipo'] else 'Narrador New'} | {tc(TL[n]['tin'])} | {est:.2f} s | {real:.2f} s | {real - est:+.2f} s | {pr or '—'} |")
o += ['', f'**Total locución:** estimada {te:.1f} s · real {tr:.1f} s ({tr - te:+.1f} s).']
open(OUT + '/2_NARRACION.md', 'w').write('\n'.join(o) + '\n')
# ---------------- 3 recortes y TC
o = ['# Informe 3 · Recortes y TC corregidos', '', 'Entrada y salida de cada corte ajustadas a palabra con STT (faster-whisper, palabra a palabra): la entrada nunca pisa una sílaba; la salida lleva una cola de ≈0,25 s o la «cola corta» indicada en la fila, sin dejar entrar la palabra siguiente.', '',
     '| Fila | Archivo de origen | Entrada EDL (s) | Salida EDL (s) | Entrada real (s) | Salida real (s) | Motivo | «Ajustar a oído» |', '|---|---|---|---|---|---|---|---|']
for n, f, a, b, a2, b2, how, oido in L['tc']:
    o.append(f"| {n} | {f} | {'' if a is None else f'{a:.2f}'} | {'' if b is None else f'{b:.2f}'} | {a2:.2f} | {b2:.2f} | {how} | {'sí' if oido else ''} |")
o += ['', '## Cortes con su duración final', '', '| Fila | TC programa | Duración EDL | Duración real | Fuente (entrada-salida) |', '|---|---|---|---|---|']
for n, s in sorted(P.items()):
    if s['tipo'] != 'voz': continue
    o.append(f"| {n} | {tc(TL[n]['tin'])} | {s['edl_dur']:.2f} s | {round(s['D'] * FPS) / FPS:.2f} s | {'; '.join(f'{os.path.basename(p)} {a:.2f}-{b:.2f}' for p, a, b in s.get('src', [])) or s.get('kind', '')} |")
open(OUT + '/3_RECORTES_Y_TC.md', 'w').write('\n'.join(o) + '\n')
# ---------------- 5 recursos
used = {}
for n, s in P.items():
    for p in s['pieces']:
        if p.get('path') and '/png/' not in p['path']: used.setdefault(os.path.basename(p['path']), set()).add(n)
    for p, a, b in s.get('src', []): used.setdefault(os.path.basename(p), set()).add(n)
mus = json.load(open(AQ + '/music_plan.json')) if os.path.exists(AQ + '/music_plan.json') else []
mu = {}
for n, name, off, g, D in mus:
    if name and g is not None: mu[name] = mu.get(name, 0) + D
MIX = {'epical': ('Epical Drums 03', 'Grigoriy Nuzhny', 678), 'selpan': ('Selpan', 'Eugenio Mininni', 612), 'fallen': ('Fallen (Asper)', 'Eugenio Mininni', 565), 'masking': ('Masking the Masters', 'Eugenio Mininni', 552),
       'moonwalk': ('Moon Walk', 'Eugenio Mininni', 609), 'discover': ('Discover', 'Eugenio Mininni', 587), 'vertigo': ('Vertigo', 'Eugenio Mininni', 597), 'delirium': ('Delirium', 'Eugenio Mininni', 605),
       'bangkok': ('Fragments Of Bangkok', 'Eugenio Mininni', 625), 'feedback': ('Feedback Dreams', 'Eugenio Mininni', 588), 'shame': ('Shame', 'Eugenio Mininni', 553), 'goats': ('Goats', 'Eugenio Mininni', 564),
       'xanthos': ('Xanthos', 'Eugenio Mininni', 633), 'farewell': ('The Farewell', 'Eugenio Mininni', 546), 'river': ('River Flow', 'Eugenio Mininni', 594), 'drawing': ('Drawing the Sky', 'Eugenio Mininni', 606)}
o = ['# Informe 5 · Recursos y créditos consumidos', '', '## Servicios', '',
     '- **ElevenLabs** (Creative, modelo eleven_v4): 171 locuciones en 21 tandas (13 Narrador Top, 8 Narrador New); ≈31.700 créditos de la cuenta Creator (quedan ≈52.000). Una sola toma por tanda.',
     '- **GitHub Actions** (repositorio de la fábrica, rama `aq-media`): descarga de voces y música; transcripción palabra a palabra (faster-whisper medium) de los cortes y del montaje.',
     '- **Figma Weave:** no se ha usado. **Imagen o vídeo generados con IA:** ninguno. **Voces que imiten a personas reales:** ninguna.',
     '- Render y mezcla: ffmpeg en el espacio de trabajo (H.264 CRF 18 preset veryfast, AAC 320 kbps).', '',
     '## Música provisional (Mixkit · Mixkit Stock Music Free License · sin crédito obligatorio)', '', '| Tema | Autor | Mixkit ID | Segundos en el montaje |', '|---|---|---|---|']
for k, v in sorted(mu.items(), key=lambda x: -x[1]): o.append(f'| {MIX[k][0]} | {MIX[k][1]} | {MIX[k][2]} | {v:.0f} s |')
o += ['', '## Material de archivo y capturas usados', '', '| Archivo | Filas |', '|---|---|']
for f, ns in sorted(used.items()): o.append(f"| {f} | {', '.join(map(str, sorted(ns)))} |")
o += ['', '## Créditos públicos', '', 'Sin cambios respecto a `creditos_publicos_CORREGIDO.txt`: firma DocuVox; música de Mixkit (sin crédito obligatorio). No se mencionan voces sintéticas ni herramientas de IA.']
open(OUT + '/5_RECURSOS_Y_CREDITOS.md', 'w').write('\n'.join(o) + '\n')
print('informes ok')
