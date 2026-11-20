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
        v = u.get('voice', 'NAR'); tot[v] = tot.get(v, 0) + words(u['text']); ch += len(u['text'])
W = sum(tot.values())
GT = json.load(open(os.path.join(HERE, 'gens_text.json'))) if os.path.exists(os.path.join(HERE, 'gens_text.json')) else {}
URLS = json.load(open(os.path.join(HERE, 'urls.json'))) if os.path.exists(os.path.join(HERE, 'urls.json')) else {}
for i, u in enumerate(U):
    g = GT.get(u.get('text'))
    if g: u['gen'] = g; u['url'] = URLS.get(g)
    elif u.get('text'): print('SIN VOZ', i, u['text'][:50])
    for sh in u.get('shots', []): sh.pop('ai_pending', None)
job = {
    'id': 'roma', 'title': 'La Antigua Roma (Historia Completa)', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 2, 'gap': 300}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 9, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'roma': lib.RO, 'cartago': lib.CA, 'barbaros': lib.BA, 'oriente': lib.OR},
    'glossary': [
        dict(term='Cónsul', on='Dos cónsules', def_='los dos jefes de la República, elegidos cada año', bando='roma'),
        dict(term='Plebe', on='la plebe', def_='los ciudadanos que no eran de familia noble'),
        dict(term='Dictador', on='Le nombran dictador', def_='cargo de emergencia con poder absoluto, como máximo seis meses', bando='roma'),
        dict(term='Tribuno de la plebe', on='tribuno de la plebe', def_='defensor de la plebe, con derecho de veto'),
        dict(term='Proscripciones', on='Las proscripciones', def_='listas de enemigos a los que cualquiera podía matar'),
        dict(term='Guardia pretoriana', on='la guardia pretoriana', def_='la escolta personal del emperador'),
        dict(term='Tetrarquía', on='la tetrarquía', def_='gobierno de cuatro: dos augustos y dos césares'),
    ],
    'theme': {'base': 'roma', 'grade': 'calido'},
    'music': RES.get('music') or {'tema': {'mixkit': 'https://assets.mixkit.co/music/79/79.mp3', 'title': 'The Journey'}, 'tension': {'mixkit': 'https://assets.mixkit.co/music/76/76.mp3', 'title': 'Epic Games'}, 'noche': {'mixkit': 'https://assets.mixkit.co/music/520/520.mp3', 'title': 'Ode to Loneliness'}},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'tension': -37, 'noche': -37}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.9, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 753,
    'qpicks': RES.get('qpicks', {}), 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(lib.AIP, open(os.path.join(HERE, 'ai_prompts.json'), 'w'), ensure_ascii=False, indent=1)
NAMES = dict(NAR='NARRADOR', ESP='ESPARTANO (co-narrador)', MUR='VOZ DE LA CALLE', FUE='FUENTE ANTIGUA', HIS='EDWARD GIBBON (lectura)', CES='JULIO CÉSAR',
             CIC='CICERÓN', AUG='AUGUSTO', CAT='CATÓN / MARCO AURELIO', GRA='TIBERIO GRACO', VES='VESPASIANO / DIOCLECIANO', ENE='ENEMIGOS DE ROMA')
L = ['# La Antigua Roma (Historia Completa) · guion', '', f'Palabras habladas: **{W}** (objetivo 6.960 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v} ({100*v/W:.0f} %)' for k, v in tot.items()), '']
for i, u in enumerate(U):
    if u['k'] == 'T': L += ['', f"## {u['card'].get('num', '') + ' · ' if u['card'].get('num') else ''}{u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch}')
for k, v in sorted(tot.items(), key=lambda x: -x[1]): print(f'  {k}: {v} ({100*v/W:.1f} %)')
print('IA:', len(lib.AIP), '· con voz:', sum(1 for u in U if u.get('url')))
