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
from lugares import L as LUG
from qcur import Q as QCUR
_AI = RES['ai']
FIX = {  # coherencia: planos sin material coherente -> otra búsqueda coherente o imagen IA
 'Hollywood film set Rome 1950s': {'ai': _AI['hollywood_set']},
 'Forum Romanum ruins sunset': {'photo': 'Forum Romanum panorama'},
 'Titus Livius statue Padua': {'ai': _AI['livio_escribe']},
 'Hut of Romulus Palatine postholes': {'photo': 'Palatine Hill Rome view'},
 'Iron Age hut urn Latium': {'ai': _AI['cabanas_palatino']},
 'Capitoline geese painting': {'ai': _AI['ocas_capitolio']},
 'Last Day of Numantia Alejo Vera': {'photo': 'Numantia ruins Soria'},
 'Gracchi brothers statue Guillaume': {'ai': _AI['tiberio_foro']},
 'Fasti calendar Roman marble': {'ai': _AI['cesar_calendario']},
 'Julius Caesar denarius dictator perpetuo': {'photo': 'Julius Caesar Tusculum bust'},
 'Julius Caesar laurel wreath coin': {'photo': 'Julius Caesar Chiaramonti bust'},
 'Augustus young bust Ara Pacis': {'photo': 'Augustus Via Labicana'},
 'Pompeii electoral programmata': {'photo': 'Pompeii electoral inscription'},
 'Pompeii Basilica graffiti': {'photo': 'Pompeii graffiti wall'},
 'Colosseum vomitorium entrance': {'photo': 'Colosseum Rome exterior'},
 'Forum Romanum sunset': {'photo': 'Roman Forum view from Capitoline'},
 'Scipio Aemilianus': {'ai': _AI['escipion_cartago']},
 'Antoninus Pius bust': {'photo': 'Marcus Aurelius equestrian statue Capitoline'},
 'Pharsalus battle': {'ai': _AI['farsalia']},
}
GT = json.load(open(os.path.join(HERE, 'gens_text.json'))) if os.path.exists(os.path.join(HERE, 'gens_text.json')) else {}
URLS = json.load(open(os.path.join(HERE, 'urls.json'))) if os.path.exists(os.path.join(HERE, 'urls.json')) else {}
for i, u in enumerate(U):
    g = GT.get(u.get('text'))
    if g: u['gen'] = g; u['url'] = URLS.get(g)
    elif u.get('text'): print('SIN VOZ', i, u['text'][:50])
    for sh in u.get('shots', []):
        sh.pop('ai_pending', None)
        if sh.get('photo') in FIX:
            r = FIX[sh.pop('photo')]; sh.update(r)
            if 'ai' in r: sh.pop('src', None)
        if 'photo' in sh and sh['photo'] in LUG: sh['lugar'] = sh['photo']
# --- montaje: orden por ancla, sin rótulo en IA, y planos largos partidos (duraciones del casting) ---
import unicodedata
def _n(x): return ' '.join(re.sub(r'[^a-z0-9ñ ]', ' ', ''.join(c for c in unicodedata.normalize('NFD', re.sub(r'\[[^\]]*\]', ' ', x or '').lower()) if unicodedata.category(c) != 'Mn')).split())
for i, u in enumerate(U):
    sh = u.get('shots') or []
    if u.get('text') and len(sh) > 1:
        txt = _n(u['text']); keys = []; last = -1
        for s in sh:
            p = txt.find(_n(s['at'])) if s.get('at') else -1
            last = p if p >= 0 else last + 0.01; keys.append(last)
        u['shots'] = [s for _, s in sorted(zip(keys, sh), key=lambda z: z[0])]
    for s in u.get('shots') or []:
        if 'ai' in s: s.pop('lt', None)
    if i == 179:
        for s in u['shots']: s.pop('lt', None) if s.get('photo') == 'Marcus Aurelius equestrian statue Capitoline' else None
EDL = os.path.join(HERE, 'edl_cast.json')
if os.path.exists(EDL):
    from collections import Counter
    uses = Counter(s['photo'] for u in U for s in u.get('shots') or [] if 'photo' in s)
    long_ = {}
    for e in json.load(open(EDL)):
        sp = e['spec']
        if e['d'] > 9.5 and ('photo' in sp or 'ai' in sp) and sp.get('at'): long_[(e['unit'], sp['at'])] = e['d']
    extra = 0
    for i, u in enumerate(U):
        out = []
        for s in u.get('shots') or []:
            out.append(s); d = long_.get((i, s.get('at')))
            if not d: continue
            ph_ = s.get('photo'); add = []
            if ph_ and ph_ in QCUR:
                n = min(2, int(d // 7), 2 * len(QCUR[ph_]) - uses[ph_])
                add = [dict({k: v for k, v in s.items() if k in ('photo', 'src', 'lugar')}) for _ in range(max(0, n))]
                uses[ph_] += len(add)
            out += add; extra += len(add)
        if u.get('shots'): u['shots'] = out
    print('planos añadidos en tramos largos:', extra)
# --- sin imágenes repetidas: cada búsqueda, como mucho tantas veces como fotos distintas aprobadas;
#     objetos, bustos y cuadros, una sola vez por unidad (fotos distintas del mismo objeto también cuentan como repetición)
LUGAR_VARIADO = {'Sagunto castle', 'Colosseum Rome exterior', 'Insula Ara Coeli Rome', 'Theodosian Walls Istanbul', 'Lake Trasimeno',
                 'Diocletian Palace Split', 'Hadrian Wall Housesteads', 'Italica Santiponce amphitheatre', 'Carthage Punic ports', 'Pompeii plaster casts'}
from collections import Counter as _C
tot = _C(); drop = 0; ai_seen = set()
for i, u in enumerate(U):
    if not u.get('shots'): continue
    out = []; per = _C()
    for s in u['shots']:
        q = s.get('photo')
        if q:
            cap = len(QCUR.get(q, [1]))
            if tot[q] >= cap or (per[q] >= 1 and q not in LUGAR_VARIADO): drop += 1; continue
            tot[q] += 1; per[q] += 1
        if 'ai' in s and 'card' not in s:
            if s['ai'] in ai_seen and len(u['shots']) > 1: drop += 1; continue
            ai_seen.add(s['ai'])
        out.append(s)
    u['shots'] = out or u['shots'][:1]
print('planos repetidos quitados:', drop)
job = {
    'lugares': LUG, 'permitir_sa': True,
    'id': 'roma', 'title': 'La Antigua Roma (Historia Completa)', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 1, 'gap': 99999}, 'auto_sfx': {}, 'sfx_max': 5,
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
    'qpicks': {'photo:' + k: v for k, v in QCUR.items()}, 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
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
