# -*- coding: utf-8 -*-
"""Guion de «Bankia» como código."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
POL = [86, 140, 214]    # gobiernos, supervisores y políticos
BAN = [86, 206, 142]    # Bankia, cajas y banqueros
CIU = [236, 170, 70]    # ahorradores, accionistas, ciudadanos
JUS = [200, 200, 210]   # tribunales
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # Narrador Top · abre, cierra, clímax y ganchos
    'NEW': 'gcDsmGjWArnZhxIfcR7d',   # Narrador New · contexto, transiciones, «mientras tanto», recapitulaciones
    'DAT': '8gK5gnQBZnJWm1ta8R8X',   # Carmen · el marcador: cifras, cotización, dinero
    'DOC': 'T9kg8O6bvv6gT3lruF5p',   # documentos, folleto, correos, sentencias
    'PRE': 'BXtvkfRgOYGPQKVRgufE',   # prensa y crónica de calle
    'RAT': 'y3QZXBVdGkWBnlHwEtgG',   # palabras reales de Rodrigo Rato
    'RAJ': 'E2QlXxgvzGjoBViEdH8g',   # palabras reales de Mariano Rajoy
    'CAS': 'nMvZRihyU408YNgNXHuX',   # palabras reales del inspector José Antonio Casaus (correos y testimonio)
    'CEL': 'v2UIb6nJm38uahTHNpTv',   # palabras reales del auditor Francisco Celma (testimonio en el juicio)
}
NARR = ('NAR', 'NEW')
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
def NEW(text, *s): V('NEW', text, *s)
def DAT(text, *s): V('DAT', text, *s)
def DOC(text, *s): V('DOC', text, *s)
def PRE(text, *s): V('PRE', text, *s)
def RAT(text, *s): V('RAT', text, *s)
def RAJ(text, *s): V('RAJ', text, *s)
def CAS(text, *s): V('CAS', text, *s)
def CEL(text, *s): V('CEL', text, *s)
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
def BOLSA(price, label, at, frm=None):
    """Marcador de la acción: cotización de BKIA en ese momento."""
    d = dict(type='counter', to=price, label=label, suffix=' €', dec=2)
    if frm is not None: d['from'] = frm
    return cd(d, at=at)
def DIA(n, total, label, at):
    """Cuenta atrás: día n de los diez meses (310 días entre la campana y el rescate)."""
    return cd(dict(type='counter', **{'from': max(0, n - 12)}, to=n, label=label, prefix='DÍA '), at=at)
AIP = {}
STYLE = ('dramatic cinematic oil painting, Caravaggio chiaroscuro lighting, visible brushstrokes, deep emerald green, black and burnished gold palette, '
         'tense financial-thriller atmosphere, dynamic composition with motion, Madrid in the early 2010s, '
         'no readable text, no letters, no numbers, no logos, no recognizable faces, faces in shadow or turned away')
def ai(key, prompt, at=None, move=None):
    """Escena IA (óleo claroscuro verde esmeralda y oro, sin caras ni letras). Si aún no está generada, queda pendiente."""
    AIP[key] = prompt + ', ' + STYLE
    if AI.get(key): return _c(dict(ai=AI[key], at=at, move=move))
    from sub import SUB
    s = SUB.get(key)
    if s and s[0] == 'ai' and AI.get(s[1]): return _c(dict(ai=AI[s[1]], at=at, move=move))
    if s and s[0] == 'ph': return ph(s[1], at=at)
    if s and s[0] == 'kw': return cd(dict(type='kw', word=s[1], sub=s[2]), at=at)
    return _c(dict(ai_pending=key, card=dict(type='kw', word='·', sub=key), at=at))

def AIR(key, at=None, move=None):
    """Reutiliza una escena IA ya generada."""
    return _c(dict(ai=AI[key], at=at, move=move))
