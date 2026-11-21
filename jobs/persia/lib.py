# -*- coding: utf-8 -*-
"""Guion de «El Imperio Persa: la historia que 300 no te contó» como código: cada llamada añade una unidad a U."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
PE = [196, 150, 60]    # Persia (oro aqueménida)
GR = [64, 112, 168]    # griegos
OT = [150, 144, 136]   # otros pueblos (medos, lidios, babilonios, egipcios, escitas)
MA = [176, 26, 32]     # Macedonia
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # Narrador Top · abre, cierra, clímax y ganchos
    'NEW': 'gcDsmGjWArnZhxIfcR7d',   # Narrador New · contexto, transiciones, «mientras tanto»
    'HER': 'nMvZRihyU408YNgNXHuX',   # Heródoto y fuentes griegas y romanas leídas (misma voz que en Termópilas)
    'PIE': 'BXtvkfRgOYGPQKVRgufE',   # lo que dicen las piedras: tablillas, cilindros e inscripciones persas
    'CIR': 'E2QlXxgvzGjoBViEdH8g',   # Ciro el Grande (cilindro, Heródoto)
    'DAR': 'Yqxik8v3XlyYOTWnDIVu',   # Darío I (Behistún, Naqsh-e Rostam)
    'JER': 'v2UIb6nJm38uahTHNpTv',   # Jerjes (misma voz que en Termópilas)
    'GRI': 'T9kg8O6bvv6gT3lruF5p',   # voces griegas: Esquilo, Jenofonte, Demarato, Temístocles
    'ESP': '78CWyCi7BhMrI529XJKv',   # voz épica para las gestas (Leónidas, batallas)
    'ALE': 'bMIdItbZXoHowF85mbi4',   # Alejandro Magno
}
NARR = ('NAR', 'NEW')
_p = os.path.join(HERE, 'recursos.json')
R_ = json.load(open(_p)) if os.path.exists(_p) else {}
class _D(dict):
    def __missing__(self, k): return None
IMG = _D(R_.get('img', {}))
AI = _D(R_.get('ai', {}))
SRC = 'commons,met,cleveland,europeana'
def _c(d): return {k: v for k, v in d.items() if v is not None}
def V(voice, text, *shots):
    k = 'N' if voice in NARR else 'R'
    U.append(_c(dict(k=k, text=text, voice=voice, shots=list(shots))))
def NAR(text, *s): V('NAR', text, *s)
def NEW(text, *s): V('NEW', text, *s)
def HER(text, *s): V('HER', text, *s)
def PIE(text, *s): V('PIE', text, *s)
def CIR(text, *s): V('CIR', text, *s)
def DAR(text, *s): V('DAR', text, *s)
def JER(text, *s): V('JER', text, *s)
def GRI(text, *s): V('GRI', text, *s)
def ESP(text, *s): V('ESP', text, *s)
def ALE(text, *s): V('ALE', text, *s)
def T(title, sub, num=None, secs=5.0, sting='tema', text=None, chapter=True, voice='NAR'):
    U.append(_c(dict(k='T', secs=secs, sting=sting, chapter=chapter, text=text, voice=voice if text else None,
                     card=_c(dict(type='title', title=title, sub=sub, num=num)))))
def B(track): U.append(dict(k='B', track=track))
def M(track, secs): U.append(dict(k='M', track=track, secs=secs))
def ph(q, src=SRC, at=None, lt=None, **kw):
    if IMG.get(q): return _c(dict(commons=IMG[q], at=at, lt=lt, **kw))
    return _c(dict(photo=q, src=src, at=at, lt=lt, **kw))
def cd(card, at=None, lt=None): return _c(dict(card=card, at=at, lt=lt))
def K(word, q, at=None, src=SRC):
    d = ph(q, src=src, at=at); d.update(kw=word, kw_at=0.4, kw_dur=2.2); return d
def KA(word, key, prompt, at=None):
    d = ai(key, prompt, at=at); d.update(kw=word, kw_at=0.4, kw_dur=2.2); return d
def PAP(text, autor, obra, at=None): return cd(dict(type='papiro', text=text, autor=autor, obra=obra), at=at)
def Q(text, attrib, at=None): return cd(dict(type='quote', text=text, attrib=attrib), at=at)
def OTRA(grecia, piedras, at=None):
    """Recurso propio del episodio: «la otra versión». Izquierda, lo que contaron los griegos; derecha, lo que dicen las fuentes persas."""
    return cd(dict(type='split', left=dict(title='Lo que contó Grecia', lines=grecia), right=dict(title='Lo que dicen las piedras', lines=piedras), strike=False), at=at)
AIP = {}
STYLE = ('epic oil painting in the style of 19th-century academic history painting, dramatic chiaroscuro, warm golden light, '
         'lapis blue and burnished gold palette, visible brushstrokes, cinematic composition, dynamic action, '
         'faces turned away or in shadow, no recognizable faces, no text, no letters, no inscriptions, no logos')
def ai(key, prompt, at=None, move=None):
    """Escena IA al óleo (sin caras reconocibles ni letras). Si aún no está generada, queda pendiente."""
    AIP[key] = prompt + ', ' + STYLE
    if AI.get(key): return _c(dict(ai=AI[key], at=at, move=move))
    return _c(dict(ai_pending=key, photo=prompt[:60], src=SRC, at=at))
