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
        if g: u['gen'] = g; u['url'] = URLS.get(g)
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
    'permitir_sa': True, 'lugares': LUG, 'permitidas': PERM,
    'id': 'persia', 'title': 'El Imperio Persa: la historia que 300 no te contó', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 1, 'gap': 99999}, 'auto_sfx': {}, 'sfx_max': 5,
    'max_shot': 7, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'bando': {'persia': lib.PE, 'griegos': lib.GR, 'otros': lib.OT, 'macedonia': lib.MA},
    'glossary': [
        dict(term='Aqueménidas', on='Imperio Aqueménida', def_='la dinastía de Ciro y Darío, 550 – 330 a. C.'),
        dict(term='Sátrapa', on='un sátrapa', def_='gobernador de una provincia del imperio persa'),
        dict(term='Ahuramazda', on='adoraban a Ahuramazda', def_='el dios sabio de la luz y la verdad de los reyes persas'),
        dict(term='Cuneiforme', on='la escritura cuneiforme', def_='escritura en forma de cuñas sobre barro o piedra'),
        dict(term='Elamita', on='Escritas en elamita', def_='la lengua de la administración persa en Persépolis'),
    ],
    'theme': {'base': 'antiguo', 'grade': 'calido', 'accent': [214, 170, 70], 'alert': [40, 80, 150]},
    'music': RES.get('music') or {
        'tema': {'mixkit': 'https://assets.mixkit.co/music/578/578.mp3', 'title': 'Gold Virginia'},
        'batalla': {'mixkit': 'https://assets.mixkit.co/music/679/679.mp3', 'title': 'Epical Drums 04'},
        'tension': {'mixkit': 'https://assets.mixkit.co/music/538/538.mp3', 'title': 'Nield Grohm Hanging 1'},
        'maravilla': {'mixkit': 'https://assets.mixkit.co/music/586/586.mp3', 'title': 'Charlotte'},
        'drama': {'mixkit': 'https://assets.mixkit.co/music/614/614.mp3', 'title': 'Silent Descent'}},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -36, 'batalla': -34, 'tension': -37, 'maravilla': -36, 'drama': -37}, 'inter_db': -22,
              'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.5, 'gap_q': 1.0},
    'tempo': 0.9, 'parts': 4, 'codec': 'hevc', 'max_kbps': 750, 'audio_kbps': '112k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 539,
    'qpicks': json.load(open(os.path.join(HERE, 'qpicks_curado.json'))), 'split_still': 6.5,
    'thumbs': [{'name': 'A', 'url': 'https://s3-alpha-sig.figma.com/img/0964/a10d/cc36f38b02bd325dbbf87eb0d80f2799.png?Expires=1795996800&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=IWp3WY1pmSajxeo1qpkMfnVjc-6Otw8cc8xv1niL5vICLHE6MA2CXqvI4wYJDc0B7ZXgfoJnUaaL8HSS7fjLHLz~~aOaTYuJT8WyFCDPrO4BNsRcRJdRTBrW17TTzIFgADDxbYQDZDZCrErvfjvI-K3hkOsLRTMahPIAcxmqgtxVXoKbVCuTbCTQKCCDybMo7Hvnc673-Gm6tunWQE3Q360w8y~z8r3UYR9flcx6Wc85V9ei1GrThShXSDBmmQVIjcy4t~83QdC72DCdwB3GaaQmUZtMgI65r3EDRTg3uRjIwaZxkSVU5XWBuCYriwkYB69w0RcCjmEsp~VAqhSucw__', 'credit': 'Ilustración IA (recreación)', 'license': 'propia', 'grande': 'JERJES', 'caja': 'NO ERA ASÍ', 'sub': 'LA HISTORIA QUE 300 NO TE CONTÓ'},
               {'name': 'B', 'commons': 'File:Left Section of the Treasury Reliefs (4735523887).jpg', 'grande': 'JERJES', 'caja': 'NO ERA ASÍ', 'sub': 'LA VERDAD DEL IMPERIO PERSA'},
               {'name': 'C', 'commons': 'File:Xerxes Enthroned (4736067680).jpg', 'grande': 'JERJES', 'caja': 'NO ERA ASÍ', 'sub': 'LA HISTORIA QUE 300 NO TE CONTÓ'}], 'picks': RES.get('picks', {}), 'rev': RES.get('rev', 1),
    'units': U,
}
for g in job['glossary']: g['def'] = g.pop('def_')
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(lib.AIP, open(os.path.join(HERE, 'ai_prompts.json'), 'w'), ensure_ascii=False, indent=1)
NAMES = dict(NAR='NARRADOR TOP', NEW='NARRADOR NEW', HER='HERÓDOTO Y FUENTES CLÁSICAS', PIE='LO QUE DICEN LAS PIEDRAS', CIR='CIRO', DAR='DARÍO', JER='JERJES', GRI='VOCES GRIEGAS', ESP='VOZ ÉPICA', ALE='ALEJANDRO')
L = ['# El Imperio Persa · guion', '', f'Palabras: **{W}** (objetivo 6.960 ±3 %) · caracteres: {ch} · por voz: ' + ', '.join(f'{k} {v} ({100*v/W:.0f} %)' for k, v in tot.items()), '']
for u in U:
    if u['k'] == 'T': L += ['', f"## {u['card'].get('num', '') + ' · ' if u['card'].get('num') else ''}{u['card']['title']}" + (f"  ·  _{u['card']['sub']}_" if u['card'].get('sub') else ''), '']
    if u['k'] == 'M': L += [f"_[música sola · {u['secs']} s]_", '']
    if u.get('text') and u['k'] != 'T':
        L += [f"**{NAMES.get(u.get('voice'), u.get('voice'))}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}", '']
open(os.path.join(HERE, 'guion.md'), 'w').write('\n'.join(L))
print(f'unidades {len(U)} · palabras {W} · caracteres {ch} · min≈{W/116:.1f}')
for k, v in sorted(tot.items(), key=lambda x: -x[1]): print(f'  {k}: {v} ({100*v/W:.1f} %)')
print('IA:', len(lib.AIP), '· con voz:', sum(1 for u in U if u.get('url')))
