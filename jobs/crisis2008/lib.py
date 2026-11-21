# -*- coding: utf-8 -*-
"""Guion de «Crisis de 2008: así se arruinó España (y puede repetirse)» como código."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
POL = [86, 140, 214]    # gobiernos y políticos
BAN = [236, 150, 62]    # banca, cajas y promotores
CIU = [130, 186, 110]   # ciudadanos, familias, movimientos
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # Narrador Top · abre, cierra, clímax y ganchos
    'NEW': 'gcDsmGjWArnZhxIfcR7d',   # Narrador New · contexto, transiciones, «mientras tanto», recapitulaciones
    'DAT': '8gK5gnQBZnJWm1ta8R8X',   # Carmen · la mesa de datos: cifras oficiales (INE, Banco de España, CGPJ)
    'DOC': 'T9kg8O6bvv6gT3lruF5p',   # Bernardo · documentos, leyes, informes y titulares
    'PRE': 'BXtvkfRgOYGPQKVRgufE',   # prensa y crónica de calle
    'ZAP': 'v2UIb6nJm38uahTHNpTv',   # palabras reales de José Luis Rodríguez Zapatero
    'SOL': 'nMvZRihyU408YNgNXHuX',   # palabras reales de Pedro Solbes
    'FAB': 'OMWmRY8slGlr6mHJSqwy',   # palabras reales de Carlos Fabra
    'RAT': 'y3QZXBVdGkWBnlHwEtgG',   # palabras reales de Rodrigo Rato
    'GUI': 'Yqxik8v3XlyYOTWnDIVu',   # palabras reales de Luis de Guindos
    'RAJ': 'E2QlXxgvzGjoBViEdH8g',   # palabras reales de Mariano Rajoy
    'USA': 'bMIdItbZXoHowF85mbi4',   # palabras reales de Richard Fuld y Mario Draghi (traducidas)
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
def ZAP(text, *s): V('ZAP', text, *s)
def SOL(text, *s): V('SOL', text, *s)
def FAB(text, *s): V('FAB', text, *s)
def RAT(text, *s): V('RAT', text, *s)
def GUI(text, *s): V('GUI', text, *s)
def RAJ(text, *s): V('RAJ', text, *s)
def USA(text, *s): V('USA', text, *s)
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
def HOY(left, right, at):
    """Tarjeta del paralelismo: lo de entonces frente a lo de hoy (sin tachar)."""
    return cd(dict(type='split', left=dict(title=left[0], lines=left[1:]), right=dict(title=right[0], lines=right[1:]), strike=False), at=at)
AIP = {}
STYLE = ('editorial illustration, gouache and colored pencil on textured paper, warm terracotta, ochre and cobalt blue palette, '
         'bold graphic shapes, dynamic cinematic composition, strong light, documentary scene set in Spain in the 2000s, '
         'no readable text, no letters, no logos, no recognizable faces')
def ai(key, prompt, at=None, move=None):
    """Escena IA (ilustración editorial a gouache, sin caras ni letras). Si aún no está generada, queda pendiente."""
    AIP[key] = prompt + ', ' + STYLE
    if AI.get(key): return _c(dict(ai=AI[key], at=at, move=move))
    from sub import SUB
    s = SUB.get(key)
    if s and s[0] == 'ai' and AI.get(s[1]): return _c(dict(ai=AI[s[1]], at=at, move=move))
    if s and s[0] == 'ph': return ph(s[1], at=at)
    if s and s[0] == 'kw': return cd(dict(type='kw', word=s[1], sub=s[2]), at=at)
    return _c(dict(ai_pending=key, photo=prompt[:60], src=SRC, at=at))

def AIR(key, at=None, move=None):
    """Reutiliza una escena IA ya generada."""
    return _c(dict(ai=AI[key], at=at, move=move))
