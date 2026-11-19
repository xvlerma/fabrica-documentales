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
VOZ = json.load(open(os.path.join(HERE, 'voz.json'))) if os.path.exists(os.path.join(HERE, 'voz.json')) else {}
GEN = json.load(open(os.path.join(HERE, 'gens.json'))) if os.path.exists(os.path.join(HERE, 'gens.json')) else {}
URLS = RES.get('urls', {})
for i, u in enumerate(U):
    if str(i) in URLS: u['url'] = URLS[str(i)]; u['gen'] = GEN.get(str(i))
    if str(i) in VOZ and RES.get('voz_url'): u['url'] = RES['voz_url']; u['clip'] = VOZ[str(i)]; u['gen'] = GEN.get(str(i))
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


# ---------- v3.2: material por capítulo, respiraciones con imagen y alineación conservada ----------
CHQ = {
 'intro': dict(p=['La Rinconada in Perú, the highest city on earth', 'Begich Towers', 'Longyearbyen polar night', 'Coober Pedy underground'], v=['earth from space night lights', 'mountain fog dawn', 'aerial mountains clouds sunrise']),
 'coober': dict(p=['Coober Pedy', 'Coober Pedy opal fields', 'Coober Pedy underground', 'Coober Pedy opal', 'Coober Pedy South Australia'], v=['australia outback desert', 'desert heat haze', 'opal stone']),
 'oimiakon': dict(p=['Oymyakon', 'Yakutia winter', 'Kolyma highway', 'Sakha Republic winter', 'Oymyakon winter'], v=['siberia winter village', 'Siberia winter frost', 'frozen breath winter cold', 'snow forest winter frost']),
 'yakutsk': dict(p=['Yakutsk', 'Yakutsk winter street', 'Lena river Yakutsk', 'Yakutsk Mammoth Museum', 'Yakutsk panorama'], v=['yakutsk', 'siberia city winter', 'frozen river winter']),
 'norilsk': dict(p=['Norilsk', 'Norilsk winter street', 'Talnakh Norilsk district', 'Norilsk Nickel plant', 'Norilsk building piles', 'Norilsk abandoned building'], v=['arctic city winter night lights', 'industrial smoke chimney winter', 'tundra winter']),
 'longyear': dict(p=['Longyearbyen', 'Longyearbyen polar night', 'Svalbard Global Seed Vault', 'polar bear Svalbard', 'Longyearbyen cemetery'], v=['svalbard', 'polar night arctic', 'northern lights aurora Svalbard', 'midnight sun arctic']),
 'whittier': dict(p=['Begich Towers', 'Whittier, Alaska', 'Buckner Building Whittier', 'Anton Anderson Memorial Tunnel', 'Begich Towers Whittier Alaska'], v=['Whittier Alaska', 'Alaska rain storm fjord', 'alaska fjord glacier', 'Whittier tunnel']),
 'aogashima': dict(p=['Aogashima', 'Aogashima island', 'Aogashima aerial', 'Hachijojima island'], v=['japan volcanic island aerial', 'volcano island ocean aerial', 'steam volcanic vent', 'japan island sea cliffs']),
 'tristan': dict(p=['Tristan da Cunha', 'Edinburgh of the Seven Seas', 'Tristan da Cunha island', 'Nightingale Island Tristan', 'Tristan da Cunha Potato Patches'], v=['atlantic ocean waves island', 'remote island ocean aerial', 'ocean storm waves']),
 'rinconada': dict(p=['La Rinconada, Puno', 'La Rinconada houses', 'La Rinconada street', 'La Rinconada Peru people', 'Lake Titicaca', 'La Rinconada in Perú, the highest city on earth'], v=['high altitude Andes mountains snow', 'peru andes mountains', 'mountain dawn snow peaks', 'andes peru altiplano']),
 'final': dict(p=['Begich Towers', 'Tristan da Cunha island', 'La Rinconada houses'], v=['aerial mountains clouds sunrise', 'earth from space night lights']),
}
T2C = {'Bajo tierra':'coober','El polo del frío':'oimiakon','Sobre hielo':'yakutsk','La ciudad cerrada':'norilsk','La noche polar':'longyear','Un pueblo en un edificio':'whittier','Dentro del volcán':'aogashima','El fin del mundo':'tristan','El techo del mundo':'rinconada','¿Por qué se quedan?':'final'}
BAD = json.load(open(os.path.join(HERE, 'bad_keys.json'))) if os.path.exists(os.path.join(HERE, 'bad_keys.json')) else {}
for i, u in enumerate(U): u['oi'] = i
cur = 'intro'; rot = {}; nrep = 0
for u in U:
    if u['k'] == 'T' and u['card']['title'] in T2C: cur = T2C[u['card']['title']]
    u['ch'] = cur
    for s in u.get('shots', []):
        key = ('video:' + s['video']) if 'video' in s else (('photo:' + s['photo']) if 'photo' in s else None)
        if key and key in BAD:
            r = rot.get(cur, 0); rot[cur] = r + 1; L = CHQ[cur]
            if r % 3 == 2: s.pop('photo', None); s.pop('src', None); s['video'] = L['v'][(r // 3) % len(L['v'])]; s['free'] = True
            else: s.pop('video', None); s.pop('free', None); s['photo'] = L['p'][r % len(L['p'])]; s['src'] = 'openverse,commons'
            if s.get('lt') and s['lt'][-1:] and s['lt'][0] in ('Oimiakón', 'Yakutsk', 'Norilsk', 'Coober Pedy', 'Longyearbyen', 'Whittier', 'Aogashima', 'Tristán de Acuña', 'La Rinconada') and 'video' in s: s.pop('lt')
            nrep += 1
print('planos con consulta sustituida:', nrep)
# respiraciones de música con imagen del lugar: cada ~165 palabras, entre dos unidades de narración
BED = 'tema'; out = []; acc = 0; vrot = {}; nb = 0
def breath(ch, secs=10):
    r = vrot.get(ch, 0); vrot[ch] = r + 1; L = CHQ[ch]
    return dict(k='M', track=BED, secs=secs, ch=ch, shots=[dict(video=L['v'][(r + 1) % len(L['v'])], free=True)])
for j, u in enumerate(U):
    if u['k'] == 'B': BED = u['track']
    if u['k'] == 'M' and not u.get('shots'):
        r = vrot.get(u['ch'], 0); vrot[u['ch']] = r + 1; L = CHQ[u['ch']]
        u['shots'] = [dict(video=L['v'][r % len(L['v'])], free=True)]
    out.append(u)
    if u.get('text') and u['k'] in ('N', 'R'): acc += words(u['text'])
    nxt = U[j + 1] if j + 1 < len(U) else None
    if acc >= 165 and u['k'] == 'N' and nxt and nxt['k'] == 'N':
        out.append(breath(u['ch'])); acc = 0; nb += 1
U[:] = out; lib.U[:] = out
print('respiraciones añadidas:', nb)
# alineación previa: reindexa align.json al nuevo orden de unidades (evita volver a transcribir)
AP = os.path.join(HERE, 'align_cast1.json')
if os.path.exists(AP):
    pre = json.load(open(AP)); new = {}
    for i, u in enumerate(U):
        o = u.get('oi')
        if o is not None and str(o) in pre and u.get('url'):
            new[str(i)] = dict(key=f"{i}:{u['url'][-40:]}", words=pre[str(o)]['words'])
    json.dump(new, open(os.path.join(HERE, 'align.json'), 'w'), ensure_ascii=False)
    print('alineación reindexada:', len(new))
for u in U: u.pop('oi', None); u.pop('ch', None)

job = {
    'id': 'vivir_al_limite', 'title': 'Vivir al límite', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 2, 'gap': 600}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 9, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'glossary': [
        dict(term='permafrost', on='sobre permafrost', def_='suelo que sigue congelado al menos dos años seguidos'),
        dict(term='Gulag', on='del Gulag', def_='red de campos de trabajos forzados de la Unión Soviética'),
        dict(term='ciudad cerrada', on='es una ciudad cerrada', def_='solo se entra con un permiso especial'),
        dict(term='noche polar', on='Es la noche polar', def_='época del año en que el sol no sale'),
        dict(term='caldera', on='una gran caldera', def_='hundimiento enorme que deja un volcán tras una erupción'),
        dict(term='hingya', on='lo llaman hingya', def_='vapor geotérmico que sale de las grietas de la caldera'),
        dict(term='cachorreo', on='llamado cachorreo', def_='30 días de trabajo sin sueldo a cambio de 1 o 2 días de mineral propio'),
        dict(term='pallaqueras', on='las pallaqueras', def_='mujeres que buscan oro entre las rocas desechadas'),
        dict(term='mal de montaña crónico', on='Es el mal de montaña crónico', def_='enfermedad por vivir años con poco oxígeno'),
    ],
    'theme': {'base': 'ciencia', 'grade': 'neutro'},
    'music': RES.get('music', {
        'tema': {'search': 'cinematic documentary piano strings', 'src': 'archive,commons,openverse,freesound', 'min_secs': 90},
        'tension': {'search': 'dark cinematic tension drone', 'src': 'openverse,freesound,archive', 'min_secs': 60},
        'desierto': {'search': 'didgeridoo ambient desert', 'src': 'archive,openverse,freesound,commons', 'min_secs': 60},
        'frio': {'search': 'arctic ambient cold wind music', 'src': 'openverse,archive,freesound', 'min_secs': 60},
        'industria': {'search': 'industrial dark ambient', 'src': 'openverse,freesound,archive', 'min_secs': 60},
        'noche': {'search': 'dark ambient night calm', 'src': 'openverse,freesound,archive', 'min_secs': 60},
        'isla': {'search': 'ocean ambient piano calm', 'src': 'openverse,archive,freesound', 'min_secs': 60},
        'andes': {'search': 'andean flute quena music', 'src': 'archive,commons,openverse,freesound', 'min_secs': 60},
    }),
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'tension': -37, 'desierto': -36, 'frio': -36, 'industria': -37, 'noche': -37, 'isla': -36, 'andes': -36}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.9, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 5100,
    'qpicks': RES.get('qpicks', {}), 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)

# guion legible
L = ['# Vivir al límite · guion', '', f'Palabras habladas: **{W}** (objetivo 6.960 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v}' for k, v in tot.items()), '']
NAMES = dict(NAR='NARRADOR', CON='CO-NARRADORA', DOC='DOCUMENTO', T1='TESTIMONIO', T2='TESTIMONIO', T3='TESTIMONIO', T4='TESTIMONIO', TF='TESTIMONIO')
for i, u in enumerate(U):
    if u['k'] == 'T': L += ['', f"## {u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · por voz {tot}')
print('objetivo 6752-7169:', 'OK' if 6752 <= W <= 7169 else 'FUERA')
