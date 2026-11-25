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
            u['url'] = f'jobs/corralito/voz/{g}.mp3' if os.path.exists(loc) else URLS.get(g)
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
    'thumbs': [dict(name='A', commons=RES.get('thumb_commons', 'Casa Rosada (Buenos Aires).jpg'), grande='CORRALITO', caja='250 $ A LA SEMANA', sub='EL DÍA QUE LOS BANCOS SE QUEDARON TU DINERO')], 'lugares': LUG, 'permitidas': PERM,
    'id': 'corralito', 'title': 'El corralito argentino: el día que los bancos se quedaron tu dinero (¿podría pasar en España?)', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 1, 'gap': 99999}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 5.5, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'gobierno': lib.GOB, 'calle': lib.CAL, 'finanzas': lib.FIN, 'europa': lib.EUR},
    'glossary': [
        dict(term='Convertibilidad', on='La Ley de Convertibilidad', def_='un peso igual a un dólar, fijado por ley (1991-2002)'),
        dict(term='FMI', on='el FMI y otros acreedores', def_='Fondo Monetario Internacional: presta a países en apuros a cambio de condiciones'),
        dict(term='Estado de sitio', on='El estado de sitio suspende', def_='régimen de excepción que suspende garantías constitucionales'),
        dict(term='Default', on='el mayor impago de deuda soberana', def_='suspensión de pagos de la deuda de un Estado'),
        dict(term='Pesificación', on='La pesificación. Todos', def_='conversión forzosa a pesos de depósitos y deudas en dólares'),
        dict(term='FGD', on='el Fondo de Garantía de Depósitos. Si', def_='cubre hasta 100.000 € por titular y entidad si un banco quiebra'),
        dict(term='BCE', on='detrás del euro está el Banco Central Europeo', def_='Banco Central Europeo: presta liquidez a los bancos del euro'),
    ],
    'theme': {'base': 'corralito', 'grade': 'calido'},
    'music': RES.get('music') or {
        'tema': {'mixkit': 'https://assets.mixkit.co/music/846/846.mp3', 'title': "I Won't surrender"},
        'tension': {'mixkit': 'https://assets.mixkit.co/music/735/735.mp3', 'title': 'Percussions 03'},
        'accion': {'mixkit': 'https://assets.mixkit.co/music/677/677.mp3', 'title': 'Epical Drums 02'},
        'calle': {'mixkit': 'https://assets.mixkit.co/music/733/733.mp3', 'title': 'Percussions 01'},
        'fiesta': {'mixkit': 'https://assets.mixkit.co/music/642/642.mp3', 'title': 'Latin Jazz'},
        'drama': {'mixkit': 'https://assets.mixkit.co/music/122/122.mp3', 'title': 'Slow Rain'},
        'europa': {'mixkit': 'https://assets.mixkit.co/music/568/568.mp3', 'title': 'Focus on Yourself'},
        'fondo': {'mixkit': 'https://assets.mixkit.co/music/564/564.mp3', 'title': 'Goats'}},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -35, 'tension': -35, 'accion': -34, 'calle': -35, 'fiesta': -36, 'drama': -37, 'europa': -36, 'fondo': -37}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.2, 'gap_q': 0.9},
    'tempo': 0.94, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 2001,
    'qpicks': json.load(open(os.path.join(HERE, 'qpicks_curado.json'))) if os.path.exists(os.path.join(HERE, 'qpicks_curado.json')) else {}, 'split_still': 5.0, 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(lib.AIP, open(os.path.join(HERE, 'ai_prompts.json'), 'w'), ensure_ascii=False, indent=1)
NAMES = dict(NAR='NARRADOR (TOP)', NEW='NARRADOR (NEW)', CRO='LA CRONISTA', DOC='DOCUMENTOS', CAV='DOMINGO CAVALLO', DLR='FERNANDO DE LA RÚA', DUH='EDUARDO DUHALDE', RSA='ADOLFO RODRÍGUEZ SAÁ')
L = ['# El corralito argentino · guion', '', f'Palabras: **{W}** (objetivo 5.220 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v} ({100*v/W:.0f} %)' for k, v in tot.items()), '']
for u in U:
    if u['k'] == 'T': L += ['', f"## {u['card'].get('num', '') + ' · ' if u['card'].get('num') else ''}{u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · min≈{W/116:.1f}')
for k, v in sorted(tot.items(), key=lambda x: -x[1]): print(f'  {k}: {v} ({100*v/W:.1f} %)')
print('IA:', len(lib.AIP), '· con voz:', sum(1 for u in U if u.get('url')))
