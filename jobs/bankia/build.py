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
            u['url'] = f'jobs/bankia/voz/{g}.mp3' if os.path.exists(loc) else URLS.get(g)
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
    'thumbs': [dict(name='A', commons=RES.get('thumb_commons', 'Bolsa de Madrid edited.jpg'), grande='BANKIA', caja='10 MESES', sub='SALIÓ A BOLSA Y PIDIÓ EL RESCATE')], 'lugares': LUG, 'permitidas': PERM,
    'id': 'bankia', 'title': 'Bankia: salió a bolsa y 10 meses después pidió el rescate', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 1, 'gap': 99999}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 6, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'gobierno': lib.POL, 'banca': lib.BAN, 'ciudadanos': lib.CIU, 'justicia': lib.JUS},
    'glossary': [
        dict(term='Caja de ahorros', on='Una caja de ahorros no tenía', def_='entidad sin accionistas, con consejos repartidos entre gobiernos, partidos y sindicatos'),
        dict(term='BFA', on='por sus siglas, BFA', def_='Banco Financiero y de Ahorros: la matriz que unió a las siete cajas'),
        dict(term='FROB', on='el FROB', def_='Fondo de Reestructuración Ordenada Bancaria: el fondo público de rescate'),
        dict(term='CNMV', on='Comisión Nacional del Mercado de Valores registra', def_='el supervisor de la bolsa: registra los folletos de las ofertas'),
        dict(term='Preferentes', on='las participaciones preferentes', def_='deuda perpetua y sin garantía, vendida en oficinas como si fuera un depósito'),
        dict(term='Prima de riesgo', on='La prima de riesgo de España', def_='lo que España paga de más que Alemania por pedir prestado'),
    ],
    'theme': {'base': 'bolsa', 'grade': 'frio'},
    'music': RES.get('music') or {
        'tema': {'mixkit': 'https://assets.mixkit.co/music/605/605.mp3', 'title': 'Delirium'},
        'tension': {'mixkit': 'https://assets.mixkit.co/music/188/188.mp3', 'title': 'Echoes'},
        'fiesta': {'mixkit': 'https://assets.mixkit.co/music/322/322.mp3', 'title': "Life's a Movie"},
        'accion': {'mixkit': 'https://assets.mixkit.co/music/678/678.mp3', 'title': 'Epical Drums 03'},
        'drama': {'mixkit': 'https://assets.mixkit.co/music/614/614.mp3', 'title': 'Silent Descent'},
        'ironia': {'mixkit': 'https://assets.mixkit.co/music/1136/1136.mp3', 'title': 'Daylight Robbery'},
        'juicio': {'mixkit': 'https://assets.mixkit.co/music/591/591.mp3', 'title': 'Kroks'},
        'fondo': {'mixkit': 'https://assets.mixkit.co/music/540/540.mp3', 'title': 'Nield Grohm Hanging 3'}},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'tension': -36, 'fiesta': -37, 'accion': -35, 'drama': -37, 'ironia': -37, 'juicio': -36, 'fondo': -37}, 'inter_db': -22,
              'pause_stretch': 0.55, 'pause_cap': 0.7, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.92, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 2012,
    'qpicks': json.load(open(os.path.join(HERE, 'qpicks_curado.json'))) if os.path.exists(os.path.join(HERE, 'qpicks_curado.json')) else {}, 'split_still': 5.0, 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(lib.AIP, open(os.path.join(HERE, 'ai_prompts.json'), 'w'), ensure_ascii=False, indent=1)
NAMES = dict(NAR='NARRADOR (TOP)', NEW='NARRADOR (NEW)', DAT='EL MARCADOR', DOC='DOCUMENTOS', PRE='PRENSA', RAT='RODRIGO RATO',
             RAJ='MARIANO RAJOY', CAS='JOSÉ ANTONIO CASAUS', CEL='FRANCISCO CELMA')
L = ['# Bankia · guion', '', f'Palabras: **{W}** (objetivo 5.220 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v} ({100*v/W:.0f} %)' for k, v in tot.items()), '']
for u in U:
    if u['k'] == 'T': L += ['', f"## {u['card'].get('num', '') + ' · ' if u['card'].get('num') else ''}{u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · min≈{W/116:.1f}')
for k, v in sorted(tot.items(), key=lambda x: -x[1]): print(f'  {k}: {v} ({100*v/W:.1f} %)')
print('IA:', len(lib.AIP), '· con voz:', sum(1 for u in U if u.get('url')))
