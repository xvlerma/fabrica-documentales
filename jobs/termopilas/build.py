# -*- coding: utf-8 -*-
"""Construye job.json y guion.md a partir de guion_p1..p3 y recursos.json. Uso: python3 build.py [stage]"""
import json, os, re, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import lib
for p in ('guion_p1', 'guion_p2', 'guion_p3'): importlib.import_module(p)
U = lib.U; RES = lib.R_
stage = sys.argv[1] if len(sys.argv) > 1 else 'cast'

def words(t): return len(re.sub(r'\[[^\]]*\]', ' ', t).split())
def chars(t): return len(t)
tot = {}; ch = 0
for u in U:
    if u.get('text'):
        v = u.get('voice', 'NAR'); tot[v] = tot.get(v, 0) + words(u['text']); ch += chars(u['text'])
W = sum(tot.values())
# voz: todas las unidades empaquetadas en un archivo; cada una es un tramo [inicio, duración]
VOZ = json.load(open(os.path.join(HERE, 'voz.json'))); GEN = json.load(open(os.path.join(HERE, 'gens.json')))
for i, u in enumerate(U):
    if str(i) in VOZ and RES.get('voz_url'): u['url'] = RES['voz_url']; u['clip'] = VOZ[str(i)]; u['gen'] = GEN[str(i)]
# estimación de duración y respiraciones musicales hasta ~59,5 min
TEMPO = 0.9
def est(U):
    t = 6.8 + 15
    for j, u in enumerate(U):
        if u['k'] in ('N', 'R'):
            nxt = U[j + 1]['k'] if j + 1 < len(U) else None
            t += u['clip'][1] / TEMPO * 1.03 - 0.25 + (0.9 if nxt in ('R', 'P') else (1.5 if u['k'] == 'N' else 1.0))
        elif u['k'] == 'T': t += max(u.get('secs', 4.5), 0.7 + (u['clip'][1] / TEMPO + 1.0 if u.get('clip') else 0))
        elif u['k'] == 'M': t += u['secs']
    return t

CLV = lambda a: {'image': f'https://openaccess-cdn.clevelandart.org/{a}/{a}_print.jpg'}
POOL = {
 'paisaje': ['Thermopylae-Air-View.jpg', 'Foloi oak forest.JPG', 'View of Mount Taygetus from the Menelaion) on 15 May 2019.jpg',
   'Ivan Konstantinovich Aivazovsky - Gathering Storm, 1899.jpg', 'Grèce. Vue de Sparte Avec le Taygete LCCN2017658135.jpg',
   'ISS067-E-153797 - View of Greece - Lamia - river Spercheios (Sperchios) - Maliac Gulf (Maliakos Gulf) - Thermopylae - Kamena Vourla (cropped).jpg',
   'The River Eurotas in Sparta on 15 May 2019.jpg', 'Effet du tonnerre.jpg', 'Messene 01.jpg', 'Plain of Marathon with Pine Forest and Wetlands, May 2015 - panoramio.jpg',
   'View of modern Sparta, Mount Taygetus and the Eurotas from the Menelaion on 15 May 2019.jpg', 'Heinrich Leutemann - The Oracle at Delphi (1885).jpg',
   'Ruins of Thespiae, from a Sketch by Daniel - Wordsworth Christopher - 1882.jpg', 'Full Moon (6043616882).jpg', 'Battle of Thermopylae - pass.jpg'],
 'persia': ['Persepolis, Apadana, Central Relief, Pharnaces.jpg', 'Right Section of the Treasury Reliefs (4735541667).jpg', 'Persepolis theasury.jpg',
   'Ionian Tribute Bearers on the Apadana Staircase (Best Viewed Size "Large") (4688057305).jpg', CLV('1960.175'), 'Behistun inscription reliefs.jpg',
   'SC 337334 - Persepolis. Palace of Xerxes. (52256758190).jpg', CLV('1943.279')],
 'griego': [CLV('1923.645'), CLV('1929.134'), CLV('1965.78'), CLV('1926.241'), CLV('1929.135'), CLV('1970.82'), CLV('1927.6'), CLV('1928.859'),
   CLV('2024.63'), 'Red-figure kylix nude hoplite (Boston MFA 89.270).jpg', CLV('1970.16'), CLV('1926.54')],
}
BED_POOL = {'persia': 'persia', 'batalla': 'griego', 'tema': 'paisaje', 'tension': 'paisaje', 'noche': 'paisaje'}
_bi = {}
def breath_shot(bed):
    k = BED_POOL.get(bed, 'paisaje'); i = _bi.get(k, 0); _bi[k] = i + 1
    v = POOL[k][i % len(POOL[k])]
    return dict(v) if isinstance(v, dict) else {'commons': v}

if all(u.get('clip') for u in U if u['k'] in ('N', 'R')):
    t0 = est(U); deficit = 59.5 * 60 - t0; BR = 9
    nb = max(0, int(deficit // BR)); print(f'estimado sin respiraciones: {t0/60:.1f} min · se añaden {nb} respiraciones de {BR} s')
    if nb:
        voice_t = sum(u['clip'][1] / TEMPO for u in U if u.get('clip')); step = voice_t / (nb * 1.45); acc = 0; bed = 'tema'; out = []; added = 0
        for j, u in enumerate(U):
            out.append(u)
            if u['k'] == 'B': bed = u['track']
            if u.get('clip') and u['k'] == 'N': acc += u['clip'][1] / TEMPO
            nxt = U[j + 1] if j + 1 < len(U) else None
            if added < nb and acc >= step and u['k'] == 'N' and nxt and nxt['k'] == 'N':
                out.append(dict(k='M', track=bed, secs=BR, shots=[breath_shot(bed)])); added += 1; acc = 0
        U[:] = out; lib.U[:] = out
    print(f'estimado final: {est(U)/60:.1f} min')

for u in U:  # pausas musicales del guion: imagen de archivo en vez de la tarjeta de marca
    if u['k'] == 'M' and not u.get('shots') and not u.get('end'):
        u['shots'] = [breath_shot(u['track']) for _ in range(2 if u['secs'] >= 12 else 1)]

OV = RES.get('ov', {}); nov = 0
for i, u in enumerate(U):
    sh = u.get('shots')
    if not sh: continue
    new = []
    for k, s_ in enumerate(sh):
        o = OV.get(f'{i}:{k}')
        if not o: new.append(s_); continue
        nov += 1
        if o.get('drop'): continue
        if 'image' in o or 'commons' in o: s_ = {x: y for x, y in o.items() if x not in ('lt_set', 'drop')}
        else: s_ = dict(s_)
        if 'lt_set' in o:
            if o['lt_set'] is False: s_.pop('lt', None)
            else: s_['lt'] = o['lt_set']
        new.append(s_)
    u['shots'] = new
print('overrides aplicados', nov, 'de', len(OV))

job = {
    'id': 'termopilas', 'title': 'La batalla de las Termópilas', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 2, 'gap': 600}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 9, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'griegos': lib.GR, 'persas': lib.PE},
    'glossary': [
        dict(term='polis', on='las polis', def_='ciudad-Estado griega independiente'),
        dict(term='medizar', on='medizar', def_='pasarse al bando persa', bando='persas'),
        dict(term='agogé', on='agogé', def_='la educación militar de los niños espartanos', bando='griegos'),
        dict(term='ilotas', on='Los ilotas', def_='siervos del Estado espartano', bando='griegos'),
        dict(term='éforos', on='los éforos', def_='cinco magistrados que vigilaban a los reyes', bando='griegos'),
        dict(term='Carneas', on='las Carneas', def_='fiesta sagrada de Apolo: prohibía salir a la guerra'),
        dict(term='hoplita', on='Hoplitas', def_='soldado de infantería pesada griego', bando='griegos'),
        dict(term='falange', on='en falange', def_='formación cerrada de hoplitas, hombro con hombro', bando='griegos'),
        dict(term='Inmortales', on='los Inmortales', def_='los 10.000 de la guardia del Gran Rey', bando='persas'),
        dict(term='Anfictionía', on='la Anfictionía', def_='liga de pueblos griegos que custodiaba santuarios'),
    ],
    'theme': {'base': 'antiguo', 'grade': 'calido'},
    'music': RES.get('music', {
        'tema': {'search': 'ancient Greek lyre music', 'src': 'archive,commons,openverse', 'min_secs': 90},
        'tension': {'search': 'dark cinematic drone', 'src': 'openverse,freesound,archive', 'min_secs': 60},
        'persia': {'search': 'oud duduk ancient Persia', 'src': 'archive,openverse,commons', 'min_secs': 60},
        'batalla': {'search': 'epic war drums percussion', 'src': 'openverse,freesound,archive', 'min_secs': 60},
        'noche': {'search': 'dark ambient night tension', 'src': 'openverse,freesound,archive', 'min_secs': 60},
    }),
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'tension': -37, 'persia': -36, 'batalla': -34, 'noche': -37}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.9, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 480,
    'qpicks': RES.get('qpicks', {}), 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'thumbs': [
        dict(name='A', commons='Jacques-Louis David - Leonidas at Thermopylae (detail) - WGA6096.jpg', grande='TERMÓPILAS', caja='NO ERAN 300', sub='La historia real'),
        dict(name='B', commons='Archers frieze Louvre AOD488.jpg', grande='LEÓNIDAS', caja='LA ÚLTIMA MAÑANA', sub='Termópilas · 480 a. C.'),
    ],
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)

# guion legible
L = ['# La batalla de las Termópilas · guion', '', f'Palabras habladas: **{W}** (objetivo 6.960 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v}' for k, v in tot.items()), '']
NAMES = dict(NAR='NARRADOR', HER='HERÓDOTO (lectura)', LEO='LEÓNIDAS', JER='JERJES', DEM='DEMARATO', DOC='DOCUMENTO / ORÁCULO', DIE='DIENECES')
for i, u in enumerate(U):
    if u['k'] == 'T': L += ['', f"## {u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · por voz {tot}')
print('objetivo 6752-7169:', 'OK' if 6752 <= W <= 7169 else 'FUERA')
