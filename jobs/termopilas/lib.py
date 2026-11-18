# -*- coding: utf-8 -*-
"""Ayudas para escribir el guion de Termópilas como código: cada llamada añade una unidad a U."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
GR = [242, 255, 0]      # griegos: amarillo DocuVox
PE = [176, 64, 48]      # persas: rojo teja
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # narrador
    'HER': 'nMvZRihyU408YNgNXHuX',   # lectura de Heródoto (masculina madura)
    'LEO': '78CWyCi7BhMrI529XJKv',   # Leónidas: «Espartano»
    'JER': 'v2UIb6nJm38uahTHNpTv',   # Jerjes
    'DEM': 'T9kg8O6bvv6gT3lruF5p',   # Demarato
    'DOC': 'BXtvkfRgOYGPQKVRgufE',   # oráculo, inscripciones y documentos
    'DIE': 't9LRTh3y1ioN00e9wsNh',   # Dieneces: Aaron Abad, castellano
}
_p = os.path.join(HERE, 'recursos.json')
R_ = json.load(open(_p)) if os.path.exists(_p) else {}
IMG = R_.get('img', {})          # claves -> título exacto de Commons
AI = R_.get('ai', {})            # claves -> URL de recreación generada
AIQ = {  # mientras no haya recreación, plano de archivo equivalente
    'wax tablet': 'ancient Greek writing tablet wax stylus', 'enclosure': 'Persian army relief soldiers rows',
    'boys': 'Greek boys wrestling vase', 'wall': 'ancient Greek fortification wall stones', 'feigned': 'hoplites turning charge vase',
    'shepherd': 'Greek shepherd terracotta figurine', 'night march': 'Persian spearmen relief night', 'oak leaves': 'oak forest Greece mountain',
    'descent': 'Kallidromo mountain slope forest', 'fire camp': 'Greek sacrifice altar vase', 'battle dust': 'Greeks fighting Persians vase',
    'immortals arrive': 'Immortals archers frieze Susa', 'hill silence': 'Kolonos hill Thermopylae', 'field': 'fallen warriors vase',
    'trenches': 'ancient battlefield burial', }

def _clean(d): return {k: v for k, v in d.items() if v is not None}
def N(text, *shots, voice='NAR'): U.append(_clean(dict(k='N', text=text, voice=voice, shots=list(shots))))
def R(voice, text, *shots):
    U.append(_clean(dict(k='N' if voice == 'NAR' else 'R', text=text, voice=voice, shots=list(shots))))
def T(title, sub, secs=5.0, sting='tema', text=None, chapter=True):
    U.append(_clean(dict(k='T', secs=secs, sting=sting, chapter=chapter, text=text, voice='NAR' if text else None,
                         card=dict(type='title', title=title, sub=sub))))
def B(track): U.append(dict(k='B', track=track))
def M(track, secs, end=False): U.append(_clean(dict(k='M', track=track, secs=secs, end=end or None)))

def ph(q, src='commons,met,cleveland', at=None, lt=None, tr=None, **kw):
    return _clean(dict(photo=q, src=src, at=at, lt=lt, tr=tr, **kw))
def cd(card, at=None, tr=None, lt=None):
    def fix(o):  # claves de imagen -> commons
        if isinstance(o, dict):
            if 'commons' in o and (o['commons'] is None or o['commons'] == ''): o.pop('commons')
            for v in o.values(): fix(v)
        elif isinstance(o, list):
            for v in o: fix(v)
    fix(card); return _clean(dict(card=card, at=at, tr=tr, lt=lt))
def K(word, q, at=None, src='commons,met,cleveland'): return _clean(dict(photo=q, src=src, kw=word, at=at, kw_at=0.4, kw_dur=2.2))
def D(title, imgkey, text, source, at=None):
    c = dict(type='doc', title=title, lines=[text], source=source)
    if IMG.get(imgkey): c['commons'] = IMG[imgkey]
    else: c = dict(type='quote', text=text, attrib=source)
    return _clean(dict(card=c, at=at))
def ai(key, at=None, lt=None, tr=None):
    if AI.get(key): return _clean(dict(ai=AI[key], at=at, lt=lt or None, tr=tr))
    return _clean(dict(photo=AIQ.get(key, key), src='met,cleveland,commons', at=at, lt=lt if lt and lt[1] != 'Recreación' else None, tr=tr))

class _ImgDict(dict):
    def __missing__(self, k): return None
IMG = _ImgDict(IMG)
