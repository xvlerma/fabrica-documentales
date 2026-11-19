# -*- coding: utf-8 -*-
"""Ayudas para escribir el guion de «Vivir al límite» como código: cada llamada añade una unidad a U."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # narrador
    'CON': '8gK5gnQBZnJWm1ta8R8X',   # co-narradora: Carmen
    'DOC': 'BXtvkfRgOYGPQKVRgufE',   # documentos, estudios, prensa, carteles
    'T1': 'v2UIb6nJm38uahTHNpTv',    # testimonios masculinos (1)
    'T2': 'nMvZRihyU408YNgNXHuX',    # testimonios masculinos maduros (2)
    'T3': 'T9kg8O6bvv6gT3lruF5p',    # testimonios masculinos (3)
    'T4': 't9LRTh3y1ioN00e9wsNh',    # científico / experto citado (Aaron Abad)
    'TF': 'OvG3ld31AQ6IRXW4ojTa',    # testimonios femeninos: Lulú
}
_p = os.path.join(HERE, 'recursos.json')
R_ = json.load(open(_p)) if os.path.exists(_p) else {}

def _clean(d): return {k: v for k, v in d.items() if v is not None}
def N(text, *shots, voice='NAR'): U.append(_clean(dict(k='N', text=text, voice=voice, shots=list(shots))))
def C(text, *shots): N(text, *shots, voice='CON')
def R(voice, text, *shots): U.append(_clean(dict(k='R', text=text, voice=voice, shots=list(shots))))
def T(title, sub, secs=5.0, sting='tema', text=None, chapter=True):
    U.append(_clean(dict(k='T', secs=secs, sting=sting, chapter=chapter, text=text, voice='NAR' if text else None,
                         card=dict(type='title', title=title, sub=sub))))
def B(track): U.append(dict(k='B', track=track))
def M(track, secs, end=False): U.append(_clean(dict(k='M', track=track, secs=secs, end=end or None)))

SRC = 'openverse,commons'
def ph(q, at=None, lt=None, tr=None, src=SRC, **kw): return _clean(dict(photo=q, src=src, at=at, lt=lt, tr=tr, **kw))
def vd(q, at=None, lt=None, tr=None, **kw): return _clean(dict(video=q, free=True, at=at, lt=lt, tr=tr, **kw))
def cd(card, at=None, tr=None, lt=None): return _clean(dict(card=card, at=at, tr=tr, lt=lt))
def K(word, q, at=None, video=False):
    d = dict(video=q, free=True) if video else dict(photo=q, src=SRC)
    d.update(kw=word, at=at, kw_at=0.4, kw_dur=2.2); return _clean(d)
def Q(text, attrib, at=None): return cd(dict(type='quote', text=text, attrib=attrib), at=at)
def MAPA(title, lon, lat, name, span=60, at=None):
    """Mapa que vuela del mundo al lugar."""
    keys = [[-170, -58, 190, 75], [lon - span, max(-80, lat - span * .55), lon + span, min(82, lat + span * .55)], [lon - 6, lat - 3.3, lon + 6, lat + 3.3]]
    return cd(dict(type='mapfly', title=title, keys=keys, points=[dict(name=name, lon=lon, lat=lat, at=0.55, big=1, pulse=True)]), at=at)
