# -*- coding: utf-8 -*-
"""job.json de «Pedro Sánchez, la entrevista que nadie le hizo». Uso: python3 build.py [stage]"""
import json, os, re, sys, hashlib, copy
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE)); sys.path.insert(0, HERE)
import guion as G
stage = sys.argv[1] if len(sys.argv) > 1 else 'cast'
U = copy.deepcopy(G.U); AI = json.load(open(os.path.join(HERE, 'ai_urls.json')))
H = lambda t: hashlib.md5(t.encode()).hexdigest()[:10]
EXTRA = {57: ['«Rectificar»', 'Decisiones diferentes a las que dijo antes de las elecciones'],
         226: ['Plus Ultra · 53 millones de euros', 'Préstamo del Fondo de apoyo a la solvencia (SEPI)', 'Defensa del Gobierno: «salvó 60.000 empleos»']}
# cortes del inventario que faltaban (todos verificados por transcripción)
def after(pred, new):
    j = next(k for k, u in enumerate(U) if pred(u)); U[j + 1:j + 1] = new
isC = lambda name: (lambda u: u['k'] == 'C' and u['src'].endswith(name))
after(lambda u: u['k'] == 'C' and u['src'].endswith('clip_35_bildu_no_vamos_a_pactar.mp4') and u.get('out') == 5.5,
      [dict(k='C', src='media/e29n90/cortes/clip_35b_bildu_navarratv.mp4', lt=['Pedro Sánchez', 'RESPUESTA REAL · Navarra TV · 2015'], fuente='cita', **{'in': 2.3, 'out': 7.3})])
after(isC('clip_33_no_entra_constitucion.mp4'),
      [dict(k='M', track='tension', secs=3, shots=[{'card': {'type': 'aviso', 'lines': ['Un año después', '15/11/2023 · Debate de investidura'], 'head': True, 'size': 52}}]),
       dict(k='C', src='media/e29n90/cortes/clip_33b_acorde_constitucion.mp4', audio_only=True, quote='La amnistía que planteamos es perfectamente legal. Es acorde con la Constitución.',
            lt=['Pedro Sánchez', 'RESPUESTA REAL · Debate de investidura · Congreso · 15/11/2023 (audio)'], fuente='cita', **{'in': 0.0, 'out': 5.9})])
after(isC('clip_36b_nogueras_bloqueado.mp4'),
      [dict(k='C', src='media/e29n90/decl/ul_puigdemont_perpinan__02.mp4', lt=['Carles Puigdemont (Junts)', 'Perpiñán · octubre de 2025 · anuncia la ruptura con el PSOE'], fuente='cita', **{'in': 88.3, 'out': 123.7}),
       dict(k='M', track='tension', secs=4.5, shots=[{'card': {'type': 'quote', 'text': '«Romper el apoyo al Partido Socialista. Ejercer la oposición.»', 'attrib': 'Carles Puigdemont · Perpiñán · octubre de 2025 · traducido del catalán'}}])])
after(isC('clip_19d_1_vinculacion.mp4'),
      [dict(k='C', src='media/e29n90/cortes/clip_19d_2_aldama.mp4', lt=['Mercedes Zarzalejo (PP)', 'Asamblea de Madrid · 13/11/2024 · pregunta'], fuente='cita', **{'in': 0.4, 'out': 16.2})])
for u in U:
    if u['k'] in ('N', 'R') and 'registra la oficina' in u.get('text', ''):
        u['shots'].insert(1, {'file': 'media/e29n90/broll/ul_zapatero_registro__01.mp4', 'start': 3, 'at': 'registra'})
HLS_CUT = json.load(open(os.path.join(HERE, 'hls_cuts.json'))) if os.path.exists(os.path.join(HERE, 'hls_cuts.json')) else {}
for u in U:
    if u['k'] == 'C' and '/hls/' in u['src']:
        n = os.path.basename(u['src'])[:-4]
        if n in HLS_CUT: u.update(HLS_CUT[n])
        else: u['in'], u['out'] = 0, 8.0  # provisional para el casting
faltan = []
for i, u in enumerate(U):
    for s in u.get('shots', []):
        if 'ai_key' in s: s['ai'] = AI[s.pop('ai_key')]
    if u.get('text') and u['k'] in ('N', 'R', 'T'):
        p = f"media/e29n90/voz/{H(u['text'])}.mp3"
        if os.path.exists(os.path.join(ROOT, p)): u['url'] = p
        else: faltan.append(i)
    if u['k'] in ('N', 'R') and not u.get('shots'):
        nx = U[i + 1] if i + 1 < len(U) else {}
        if i in EXTRA: u['shots'] = [{'card': {'type': 'aviso', 'lines': EXTRA[i], 'head': True, 'size': 46}}]
        elif nx.get('k') == 'C' and nx.get('lt'): u['shots'] = [{'card': {'type': 'aviso', 'lines': list(nx['lt']), 'head': True, 'size': 46}}]
        else: u['shots'] = [{'card': {'type': 'aviso', 'lines': ['Pedro Sánchez', 'La entrevista que nadie le hizo'], 'head': True, 'size': 46}}]
if faltan: print('sin voz:', len(faltan), faltan[:20])
MK = lambda n, t: {'mixkit': f'https://assets.mixkit.co/music/{n}/{n}.mp3', 'title': t, 'page': 'https://mixkit.co/free-stock-music/'}
job = {
    'id': 'e29n90', 'title': 'Pedro Sánchez, la entrevista que nadie le hizo', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 3, 'gap': 300}, 'auto_sfx': {}, 'sfx_max': 0,
    'max_shot': 12, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'theme': {'base': 'plataforma', 'grade': 'neutro'},
    'music': {'tema': MK(565, 'Fallen (Asper)'), 'tension': MK(188, 'Echoes'), 'pulso': MK(538, 'Nield Grohm Hanging 1'),
              'noche': MK(605, 'Delirium'), 'nada': MK(22, 'Piano Reflections'), 'golpe': MK(676, 'Epical Drums 01')},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -35, 'tension': -36, 'pulso': -36, 'noche': -37, 'nada': -36, 'golpe': -30},
              'inter_db': -22, 'clip_db': -19, 'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.92, 'parts': 4, 'codec': 'hevc', 'max_kbps': 900, 'audio_kbps': '128k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 2911, 'rev': 1,
    'units': U,
}
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
print('unidades', len(U), '· stage', stage)

# guion legible con fuentes
NAMES = dict(TOP='NARRADOR', NEW='NARRADOR', ENT='PREGUNTA (DocuVox)', DOC='DOCUMENTO')
L = ['# Pedro Sánchez, la entrevista que nadie le hizo', '', 'DocuVox · Especial Elecciones 29N · guion con fuentes', '',
     '> Las respuestas de Pedro Sánchez y del resto de aludidos son cortes reales de archivo, con su fecha y su medio. '
     'Las preguntas y la narración son de DocuVox. Investigado no es condenado: se indica en cada caso el estado procesal.', '']
def srcs(u):
    out = []
    for s in u.get('shots', []):
        c = s.get('card') or {}
        for k in ('attrib', 'source', 'foot'):
            if c.get(k): out.append(c[k])
        for side in ('left', 'right'):
            if isinstance(c.get(side), dict) and c[side].get('source'): out.append(c[side]['source'])
        if s.get('lt'): out.append(' · '.join(s['lt']))
    return out
for u in U:
    if u['k'] == 'T' and u.get('card'):
        L += ['', f"## {u['card'].get('title', '')}" + (f" — {u['card']['sub']}" if u['card'].get('sub') else ''), '']
    if u['k'] in ('N', 'R') and u.get('text'):
        L += [f"**{NAMES.get(u['voice'], u['voice'])}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}"]
        f_ = [x for x in srcs(u) if x]
        if f_: L += ['', '  _Fuente en pantalla: ' + ' / '.join(dict.fromkeys(f_)) + '_']
        L += ['']
    if u['k'] == 'C':
        L += [f"▶ **CORTE REAL** · {' · '.join(u.get('lt') or [])}" + (f" · «{u['quote']}»" if u.get('quote') else ''), '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
