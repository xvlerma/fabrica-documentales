# -*- coding: utf-8 -*-
"""Guion de «La Antigua Roma (Historia Completa)» como código: cada llamada añade una unidad a U."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
RO = [176, 26, 32]     # Roma
CA = [64, 112, 168]    # Cartago
BA = [118, 140, 76]    # galos, germanos y otros pueblos «bárbaros»
OR = [196, 150, 60]    # Oriente: griegos, Egipto, Partia, Persia
VOICES = {
    'NAR': 'gcDsmGjWArnZhxIfcR7d',   # Narrador New · guía (máx. 60 %)
    'ESP': '78CWyCi7BhMrI529XJKv',   # Espartano · co-narrador épico (batallas, clímax)
    'MUR': 'BXtvkfRgOYGPQKVRgufE',   # voz femenina · la Roma de la calle: grafitos, epitafios, vida cotidiana
    'FUE': 'nMvZRihyU408YNgNXHuX',   # fuentes antiguas leídas (Polibio, Livio, Plutarco, Suetonio, Tácito, Plinio, Jerónimo…)
    'HIS': 'y3QZXBVdGkWBnlHwEtgG',   # lectura de historiador moderno (Gibbon)
    'CES': '9VIVvGo8sgpRzsz9ndfa',   # Julio César
    'CIC': 'v2UIb6nJm38uahTHNpTv',   # Cicerón
    'AUG': 'E2QlXxgvzGjoBViEdH8g',   # Augusto
    'CAT': 'Yqxik8v3XlyYOTWnDIVu',   # Catón el Viejo y Marco Aurelio
    'GRA': 'bMIdItbZXoHowF85mbi4',   # Tiberio Graco
    'VES': 'OMWmRY8slGlr6mHJSqwy',   # Vespasiano y Diocleciano (los del humor)
    'ENE': 'T9kg8O6bvv6gT3lruF5p',   # enemigos de Roma: Breno, Maharbal, Pirro
}
NARR = ('NAR', 'ESP', 'MUR')
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
def ESP(text, *s): V('ESP', text, *s)
def MUR(text, *s): V('MUR', text, *s)
def FUE(text, *s): V('FUE', text, *s)
def T(title, sub, num=None, secs=5.0, sting='tema', text=None, chapter=True, voice='NAR'):
    U.append(_c(dict(k='T', secs=secs, sting=sting, chapter=chapter, text=text, voice=voice if text else None,
                     card=_c(dict(type='title', title=title, sub=sub, num=num)))))
def B(track): U.append(dict(k='B', track=track))
def M(track, secs): U.append(dict(k='M', track=track, secs=secs))
try:
    import fix as _fix
except Exception:
    _fix = None
def ph(q, src=SRC, at=None, lt=None, tr=None, **kw):
    r = _fix.resolve(q, AI) if _fix else None
    if r: return _c(dict(r, at=at, lt=lt, tr=tr, **kw))
    if IMG.get(q): return _c(dict(commons=IMG[q], at=at, lt=lt, tr=tr, **kw))
    return _c(dict(photo=q, src=src, at=at, lt=lt, tr=tr, **kw))
def cd(card, at=None, tr=None, lt=None): return _c(dict(card=card, at=at, tr=tr, lt=lt))
def K(word, q, at=None, src=SRC):
    d = ph(q, src=src, at=at); d.update(kw=word, kw_at=0.4, kw_dur=2.2); return d
def PAP(text, autor, obra, at=None): return cd(dict(type='papiro', text=text, autor=autor, obra=obra), at=at)
def MITO(leyenda, real, at=None, fuente=None, img=None):
    c = _c(dict(type='mito', leyenda=leyenda, real=real, fuente=fuente))
    if img and IMG.get(img): c['commons'] = IMG[img]
    return cd(c, at=at)
AIP = {}  # clave -> prompt de la ilustración (se genera con Figma, estilo novela gráfica fijo)
def ai(key, prompt, at=None, move=None):
    """Ilustración IA estilo novela gráfica. Si aún no está generada, queda como búsqueda de archivo equivalente."""
    AIP[key] = prompt
    if AI.get(key): return _c(dict(ai=AI[key], at=at, move=move))
    return _c(dict(ai_pending=key, photo=prompt[:60], src=SRC, at=at))
