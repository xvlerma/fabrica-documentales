# -*- coding: utf-8 -*-
"""Guion de «El corralito argentino» como código."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
GOB = [116, 172, 223]   # gobiernos y ministros (celeste)
CAL = [214, 48, 49]     # la calle: ahorristas, manifestantes (rojo)
FIN = [236, 196, 90]    # FMI, bancos, acreedores (ámbar)
EUR = [170, 180, 200]   # Europa y España (gris azulado)
VOICES = {
    'NAR': 'EtnizbrIk2nKCZCt0zqW',   # Narrador Top · abre, cierra, clímax y ganchos
    'NEW': 'gcDsmGjWArnZhxIfcR7d',   # Narrador New · contexto, transiciones, «mientras tanto»
    'CRO': '8gK5gnQBZnJWm1ta8R8X',   # Carmen · la cronista: el reloj, las cifras y Europa
    'DOC': 'T9kg8O6bvv6gT3lruF5p',   # documentos: decretos, leyes, comunicados
    'CAV': 'v2UIb6nJm38uahTHNpTv',   # palabras reales de Domingo Cavallo
    'DLR': 'nMvZRihyU408YNgNXHuX',   # palabras reales de Fernando de la Rúa
    'DUH': 'E2QlXxgvzGjoBViEdH8g',   # palabras reales de Eduardo Duhalde
    'RSA': 'y3QZXBVdGkWBnlHwEtgG',   # palabras reales de Adolfo Rodríguez Saá
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
def CRO(text, *s): V('CRO', text, *s)
def DOC(text, *s): V('DOC', text, *s)
def CAV(text, *s): V('CAV', text, *s)
def DLR(text, *s): V('DLR', text, *s)
def DUH(text, *s): V('DUH', text, *s)
def RSA(text, *s): V('RSA', text, *s)
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
def DIA(n, label, at, frm=None):
    """Reloj de la crisis: día n desde el decreto del corralito (1 de diciembre de 2001 = día 1)."""
    return cd(dict(type='counter', **{'from': frm if frm is not None else max(0, n - 6)}, to=n, label=label, prefix='DÍA '), at=at)
def USD(v, label, at, frm=1.0):
    """Cotización del dólar en pesos."""
    return cd(dict(type='counter', **{'from': frm}, to=v, label=label, prefix='$ ', dec=2), at=at)
AIP = {}
STYLE = ('bold linocut relief print illustration, hand-carved texture with visible gouge marks, limited three-ink palette of sky blue, '
         'deep black and blood red on warm off-white paper, strong diagonal composition full of motion and tension, Argentina around 2001, '
         'no readable text, no letters, no numbers, no logos, no flags with emblems, no recognizable faces, faces in shadow, turned away or simplified')
def ai(key, prompt, at=None, move=None):
    """Escena IA (grabado en linóleo celeste, negro y rojo; sin caras ni letras). Si aún no está generada, queda pendiente."""
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
