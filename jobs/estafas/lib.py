# -*- coding: utf-8 -*-
"""Guion de «Las estafas más grandes de la historia: de Ponzi a Madoff» como código."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
ES = [196, 38, 34]     # estafadores
VI = [80, 120, 168]    # víctimas
AU = [150, 144, 136]   # autoridades, jueces, investigadores
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # Narrador Top · narrador principal
    'INV': '8gK5gnQBZnJWm1ta8R8X',   # Carmen · la investigadora: datos, pruebas, cómo cayó
    'DOC': 'T9kg8O6bvv6gT3lruF5p',   # Bernardo · documentos, prensa, sentencias
    'MAD': 'E2QlXxgvzGjoBViEdH8g',   # Santiago · palabras reales de Bernard Madoff
    'JUE': 'Yqxik8v3XlyYOTWnDIVu',   # Roque · jueces, fiscales, testigos de la época
    'MKP': 'bMIdItbZXoHowF85mbi4',   # Oliver · Harry Markopolos (sus palabras ante el Congreso)
    'PON': 'OMWmRY8slGlr6mHJSqwy',   # Gonzalo · Charles Ponzi (sus palabras a la prensa)
    'LUS': 'y3QZXBVdGkWBnlHwEtgG',   # Néstor · Victor Lustig (mandamientos que se le atribuyen)
}
NARR = ('NAR', 'INV')
_p = os.path.join(HERE, 'recursos.json')
R_ = json.load(open(_p)) if os.path.exists(_p) else {}
class _D(dict):
    def __missing__(self, k): return None
IMG = _D(R_.get('img', {}))
AI = _D(R_.get('ai', {}))
SRC = 'commons,loc,europeana'
def _c(d): return {k: v for k, v in d.items() if v is not None}
def V(voice, text, *shots):
    k = 'N' if voice in NARR else 'R'
    U.append(_c(dict(k=k, text=text, voice=voice, shots=list(shots))))
def NAR(text, *s): V('NAR', text, *s)
def INV(text, *s): V('INV', text, *s)
def DOC(text, *s): V('DOC', text, *s)
def MAD(text, *s): V('MAD', text, *s)
def JUE(text, *s): V('JUE', text, *s)
def MKP(text, *s): V('MKP', text, *s)
def PON(text, *s): V('PON', text, *s)
def LUS(text, *s): V('LUS', text, *s)
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
AIP = {}
STYLE = ('cinematic film still, film noir lighting, deep shadows, single hard key light, 35mm film grain, muted desaturated colors, '
         'documentary realism, no visible faces, no text, no letters, no logos')
def ai(key, prompt, at=None, move=None):
    """Escena IA estilo cine negro (sin caras ni letras). Si aún no está generada, queda pendiente."""
    AIP[key] = prompt + ', ' + STYLE
    if AI.get(key): return _c(dict(ai=AI[key], at=at, move=move))
    return _c(dict(ai_pending=key, photo=prompt[:60], src=SRC, at=at))
