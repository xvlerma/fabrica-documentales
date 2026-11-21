# -*- coding: utf-8 -*-
"""Construye job.json y guion.md. Uso: python3 build.py [stage]"""
import json, os, re, sys, importlib, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import lib
from lugares import L as LUG, PERMITIDAS as PERM
for p in ('guion_p1', 'guion_p2', 'guion_p3'): importlib.import_module(p)
U = lib.U; RES = lib.R_
stage = sys.argv[1] if len(sys.argv) > 1 else 'cast'
def words(t): return len(re.sub(r'\[[^\]]*\]', ' ', t).split())
tot = {}; ch = 0
for u in U:
    if u.get('text'):
        v = u.get('voice', 'NAR'); tot[v] = tot.get(v, 0) + words(u['text']); ch += len(u['text'])
W = sum(tot.values())
def _n(x): return ' '.join(re.sub(r'[^a-z0-9ñ ]', ' ', ''.join(c for c in unicodedata.normalize('NFD', re.sub(r'\[[^\]]*\]', ' ', x or '').lower()) if unicodedata.category(c) != 'Mn')).split())
bad = []
for i, u in enumerate(U):
    if u.get('text') and u['k'] != 'T':
        txt = _n(u['text'])
        for s in u.get('shots', []):
            if s.get('at') and _n(s['at']) not in txt: bad.append((i, s['at']))
if bad: print('ANCLAS QUE NO ESTÁN EN SU FRASE:', bad)
QCUR = {}
try:
    from qcur import Q as QCUR
except Exception: pass
GT = json.load(open(os.path.join(HERE, 'gens_text.json')))
URLS = json.load(open(os.path.join(HERE, 'urls.json')))
for i, u in enumerate(U):
    if u.get('text'):
        g = GT.get(u['text'])
        if g:
            u['gen'] = g; loc = os.path.join(HERE, 'voz', g + '.mp3')
            u['url'] = f'jobs/crisis2008/voz/{g}.mp3' if os.path.exists(loc) else URLS.get(g)
    for sh in u.get('shots', []):
        sh.pop('ai_pending', None)
        if 'ai' in sh: sh.pop('lt', None)
    sh = u.get('shots') or []
    if u.get('text') and len(sh) > 1:
        txt = _n(u['text']); keys = []; last = -1
        for s in sh:
            p = txt.find(_n(s['at'])) if s.get('at') else -1
            last = p if p >= 0 else last + 0.01; keys.append(last)
        u['shots'] = [s for _, s in sorted(zip(keys, sh), key=lambda z: z[0])]
job = {
    'permitir_sa': True, 'export_voice': True,
    'thumbs': [dict(name='A', commons='Presidente José Luis Rodriguez Zapatero - La Moncloa 2011.jpg', grande='2008', caja='¿SE REPITE?', sub='LA BURBUJA QUE ARRUINÓ A ESPAÑA')], 'lugares': LUG, 'permitidas': PERM,
    'id': 'crisis2008', 'title': 'Crisis de 2008: así se arruinó España (y puede repetirse)', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 1, 'gap': 99999}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 7, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'gobierno': lib.POL, 'banca': lib.BAN, 'ciudadanos': lib.CIU},
    'glossary': [
        dict(term='Euríbor', on='el euríbor, el índice', def_='el tipo de interés al que se ata casi toda hipoteca variable'),
        dict(term='Caja de ahorros', on='las cajas de ahorros', def_='entidad sin accionistas, con consejos repartidos entre partidos, sindicatos y gobiernos'),
        dict(term='Hipotecas subprime', on='hipotecas basura', def_='préstamos a familias con poca capacidad de pago, empaquetados y vendidos por todo el mundo'),
        dict(term='Ejecución hipotecaria', on='ejecuciones hipotecarias', def_='el proceso judicial por el que el banco se queda con la casa si no se paga'),
        dict(term='Prima de riesgo', on='La prima de riesgo, lo que', def_='lo que España paga de más que Alemania por pedir prestado'),
        dict(term='Sareb', on='la Sareb', def_='el «banco malo»: se quedó los pisos y créditos tóxicos de las cajas'),
    ],
    'theme': {'base': 'economia', 'grade': 'neutro'},
    'music': RES.get('music') or {
        'tema': {'mixkit': 'https://assets.mixkit.co/music/168/168.mp3', 'title': 'Staring at the Night Sky'},
        'tension': {'mixkit': 'https://assets.mixkit.co/music/548/548.mp3', 'title': 'A Voice from The Past'},
        'fiesta': {'mixkit': 'https://assets.mixkit.co/music/371/371.mp3', 'title': 'Cat Walk'},
        'accion': {'mixkit': 'https://assets.mixkit.co/music/160/160.mp3', 'title': 'Minimal Emotion'},
        'drama': {'mixkit': 'https://assets.mixkit.co/music/580/580.mp3', 'title': 'Sun and His Daughter'},
        'ironia': {'mixkit': 'https://assets.mixkit.co/music/639/639.mp3', 'title': 'Jazz 1'},
        'fondo': {'mixkit': 'https://assets.mixkit.co/music/570/570.mp3', 'title': 'Sonor #2'}},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'tension': -37, 'fiesta': -37, 'accion': -36, 'drama': -37, 'ironia': -37, 'fondo': -37}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.9, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 2008,
    'qpicks': json.load(open(os.path.join(HERE, 'qpicks_curado.json'))), 'split_still': 6.5, 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(lib.AIP, open(os.path.join(HERE, 'ai_prompts.json'), 'w'), ensure_ascii=False, indent=1)
NAMES = dict(NAR='NARRADOR (TOP)', NEW='NARRADOR (NEW)', DAT='LA MESA DE DATOS', DOC='DOCUMENTOS', PRE='PRENSA Y CALLE', ZAP='J. L. RODRÍGUEZ ZAPATERO',
             SOL='PEDRO SOLBES', FAB='CARLOS FABRA', RAT='RODRIGO RATO', GUI='LUIS DE GUINDOS', RAJ='MARIANO RAJOY', USA='RICHARD FULD / MARIO DRAGHI')
L = ['# Crisis de 2008 · guion', '', f'Palabras: **{W}** (objetivo 6.960 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v} ({100*v/W:.0f} %)' for k, v in tot.items()), '']
for u in U:
    if u['k'] == 'T': L += ['', f"## {u['card'].get('num', '') + ' · ' if u['card'].get('num') else ''}{u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · min≈{W/116:.1f}')
for k, v in sorted(tot.items(), key=lambda x: -x[1]): print(f'  {k}: {v} ({100*v/W:.1f} %)')
print('IA:', len(lib.AIP), '· con voz:', sum(1 for u in U if u.get('url')))
