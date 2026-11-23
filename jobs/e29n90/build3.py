# -*- coding: utf-8 -*-
"""job.json del montaje v3 (versión crítica, auditoría 360 §7). Uso: python3 build2.py [cast|final]"""
import json, os, re, sys, hashlib, copy
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE)); sys.path.insert(0, HERE)
import guion3 as G
stage = sys.argv[1] if len(sys.argv) > 1 else 'cast'
U = copy.deepcopy(G.U); AI = json.load(open(os.path.join(HERE, 'ai_urls.json')))
H = lambda t: hashlib.md5(t.encode()).hexdigest()[:10]
COLS = {'PSOE y socios': [178, 58, 46], 'Junts': [237, 234, 228], 'Resto': [70, 70, 72]}
falta = []
def fix_card(c):
    if c.get('type') == 'timeline' and 'events' not in c: c['events'] = c.pop('items'); c['header'] = c.pop('title', '')
    if c.get('type') == 'seats' and 'parties' not in c:
        c['parties'] = [{'name': n, 'seats': k, 'color': COLS.get(n, [120, 120, 120])} for n, k in c.pop('groups')]
    if c.get('bgimg') and str(c['bgimg']).startswith('ai:'): c['bgimg'] = AI[c['bgimg'][3:]]
for i, u in enumerate(U):
    for k_ in [k for k in u if k.startswith('_')]: u.pop(k_)
    for s in u.get('shots', []):
        if 'ai_key' in s: s['ai'] = AI[s.pop('ai_key')]
        if 'card' in s: fix_card(s['card'])
    if u.get('card'): fix_card(u['card'])
    if u.get('text') and u['k'] in ('N', 'R', 'T'):
        p = f"media/e29n90/voz/{H(u['text'])}.mp3"
        if os.path.exists(os.path.join(ROOT, p)): u['url'] = p
        else: falta.append((i, u['text'][:60]))
    if u['k'] == 'C':
        if stage == 'final': assert u['out'] - u['in'] <= 25.0, (i, u['src'])
        assert os.path.exists(os.path.join(ROOT, u['src'])), u['src']
if falta: print('SIN VOZ:', len(falta), falta)
MK = lambda n, t: {'mixkit': f'https://assets.mixkit.co/music/{n}/{n}.mp3', 'title': t, 'page': 'https://mixkit.co/free-stock-music/'}
job = {
    'id': 'e29n90', 'title': 'Pedro Sánchez, la entrevista que nadie le hizo', 'channel': 'DocuVox', 'stage': stage,
    'align': True, 'align_model': 'small', 'no_pad': True, 'reuse': {'max': 3, 'gap': 300}, 'auto_sfx': {}, 'sfx_max': 0,
    'max_shot': 10, 'min_shot': 1.6, 'anchor_lead': 0.1,
    'theme': {'base': 'plataforma', 'grade': 'neutro'},
    'music': {'tema': MK(565, 'Fallen (Asper)'), 'tension': MK(188, 'Echoes'), 'pulso': MK(538, 'Nield Grohm Hanging 1'),
              'noche': MK(605, 'Delirium'), 'nada': MK(22, 'Piano Reflections'), 'golpe': MK(676, 'Epical Drums 01')},
    'audio': {'voice_db': -20, 'bed_db': {'tema': -35, 'tension': -36, 'pulso': -36, 'noche': -37, 'nada': -36, 'golpe': -31},
              'inter_db': -22, 'pause_stretch': 0.45, 'pause_cap': 0.6, 'gap_n': 1.0, 'gap_q': 0.8},
    'tempo': 0.94, 'parts': 6, 'codec': 'hevc', 'max_kbps': 1100, 'audio_kbps': '128k',
    'intro': ['assets/intro/docuvox.mp4'], 'seed': 2911, 'rev': 11,
    'clip_subs': True, 'kara_subs': False, 'clip_model': 'small', 'karaoke': True, 'max_still': 6, 'kara_chars': 40,
    'units': U,
}
json.dump(job, open(os.path.join(HERE, 'job.json'), 'w'), ensure_ascii=False, indent=1)
print('unidades', len(U), '· cortes', sum(1 for u in U if u['k'] == 'C'), '· stage', stage)
