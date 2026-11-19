# -*- coding: utf-8 -*-
"""Construye job.json y guion.md. Uso: python3 build.py [stage]"""
import json, os, re, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import lib
for p in ('guion_p1', 'guion_p2', 'guion_p3'): importlib.import_module(p)
U = lib.U; RES = lib.R_
stage = sys.argv[1] if len(sys.argv) > 1 else 'cast'
def words(t): return len(re.sub(r'\[[^\]]*\]', ' ', t).split())
tot = {}; ch = 0
for u in U:
    if u.get('text'):
        v = u.get('voice', 'DER'); tot[v] = tot.get(v, 0) + words(u['text']); ch += len(u['text'])
W = sum(tot.values())
GEN = RES.get('gens', {})
for i, u in enumerate(U):
    g = GEN.get(str(i))
    if g: u['gen'] = g['gen']; u['url'] = g.get('url')
job = {
    'id': 'orodemoscu', 'title': 'El oro de Moscú', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 2, 'gap': 600}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 9, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'izquierda': lib.IZ, 'derecha': lib.DE, 'urss': lib.SO, 'centro': [150, 150, 150]},
    'glossary': [
        dict(term='NKVD', on='la NKVD', def_='policía política de Stalin', bando='urss'),
        dict(term='Frente Popular', on='Frente Popular', def_='coalición de izquierdas que gobernaba desde febrero de 1936', bando='izquierda'),
        dict(term='No Intervención', on='No Intervención', def_='pacto para no vender armas a ningún bando (1936)'),
        dict(term='claveros', on='los llamados claveros', def_='empleados del Banco que custodiaban las llaves del oro'),
        dict(term='Gojrán', on='el Gojrán', def_='depósito de metales preciosos del Estado soviético', bando='urss'),
        dict(term='POUM', on='POUM', def_='partido marxista enemigo de Stalin', bando='izquierda'),
        dict(term='Pravda', on='Pravda', def_='diario oficial del Partido Comunista soviético', bando='urss'),
    ],
    'theme': {'base': 'guerra_moderna', 'grade': 'frio'},
    'music': RES.get('music', {
        'tema': {'mixkit': 'https://assets.mixkit.co/music/614/614.mp3', 'title': 'Silent Descent'},
        'tension': {'mixkit': 'https://assets.mixkit.co/music/188/188.mp3', 'title': 'Echoes'},
        'noche': {'mixkit': 'https://assets.mixkit.co/music/594/594.mp3', 'title': 'River Flow'},
        'rusia': {'mixkit': 'https://assets.mixkit.co/music/168/168.mp3', 'title': 'Staring at the Night Sky'},
    }),
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'tension': -37, 'noche': -37, 'rusia': -36}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.9, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 1936,
    'qpicks': RES.get('qpicks', {}), 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
NAMES = dict(DER='NARRADOR A (lectura crítica)', IZQ='NARRADOR B (lectura de la izquierda)', DOC='DOCUMENTO', ORL='ALEXANDER ORLOV (lectura)', HIS='LECTURA')
L = ['# El oro de Moscú · guion', '', f'Palabras habladas: **{W}** (objetivo 6.960 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v}' for k, v in tot.items()), '']
for i, u in enumerate(U):
    if u['k'] == 'T': L += ['', f"## {u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · por voz {tot}')
print('objetivo 6752-7169:', 'OK' if 6752 <= W <= 7169 else 'FUERA')
