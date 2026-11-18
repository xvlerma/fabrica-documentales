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
                out.append(dict(k='M', track=bed, secs=BR)); added += 1; acc = 0
        U[:] = out; lib.U[:] = out
    print(f'estimado final: {est(U)/60:.1f} min')

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
