# -*- coding: utf-8 -*-
"""Guion de «El oro de Moscú» como código: cada llamada añade una unidad a U."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = []
IZ = [190, 58, 48]     # República / izquierda
DE = [64, 104, 168]    # sublevados / derecha
SO = [150, 150, 150]   # URSS
VOICES = {
    'DER': 'EtnizbrIk2nKCZCt0zqW',   # narrador A · lectura crítica (voz de la casa: abre y cierra)
    'IZQ': 'y3QZXBVdGkWBnlHwEtgG',   # narrador B · lectura de la izquierda (Néstor, grave y sereno)
    'DOC': 'BXtvkfRgOYGPQKVRgufE',   # documentos y prensa
    'ORL': 'T9kg8O6bvv6gT3lruF5p',   # Alexander Orlov (lectura de su relato)
    'HIS': 'nMvZRihyU408YNgNXHuX',   # lecturas de historiadores
}
_p = os.path.join(HERE, 'recursos.json')
R_ = json.load(open(_p)) if os.path.exists(_p) else {}
class _D(dict):
    def __missing__(self, k): return None
IMG = _D(R_.get('img', {}))
AI = _D(R_.get('ai', {}))
SRC = 'commons,europeana,loc'
def _c(d): return {k: v for k, v in d.items() if v is not None}
def V(voice, text, *shots):
    k = 'N' if voice in ('DER', 'IZQ') else 'R'
    U.append(_c(dict(k=k, text=text, voice=voice, shots=list(shots))))
def DER(text, *s): V('DER', text, *s)
def IZQ(text, *s): V('IZQ', text, *s)
def T(title, sub, secs=5.0, sting='tema', text=None, chapter=True, voice='DER'):
    U.append(_c(dict(k='T', secs=secs, sting=sting, chapter=chapter, text=text, voice=voice if text else None,
                     card=dict(type='title', title=title, sub=sub))))
def B(track): U.append(dict(k='B', track=track))
def M(track, secs): U.append(dict(k='M', track=track, secs=secs))
def ph(q, src=SRC, at=None, lt=None, tr=None, **kw):
    if IMG.get(q): return _c(dict(commons=IMG[q], at=at, lt=lt, tr=tr, **kw))
    return _c(dict(photo=q, src=src, at=at, lt=lt, tr=tr, **kw))
def vid(q, at=None, lt=None, **kw): return _c(dict(video=q, old=True, at=at, lt=lt, **kw))
def cd(card, at=None, tr=None, lt=None): return _c(dict(card=card, at=at, tr=tr, lt=lt))
def K(word, q, at=None, src=SRC):
    d = ph(q, src=src, at=at); d.update(kw=word, kw_at=0.4, kw_dur=2.2); return d
def Q(text, attrib, at=None, img=None):
    c = dict(type='quote', text=text, attrib=attrib)
    if img and IMG.get(img): c['commons'] = IMG[img]
    return cd(c, at=at)
def DOCC(title, text, source, at=None, img=None):
    c = dict(type='doc', title=title, lines=[text], source=source)
    if img and IMG.get(img): c['commons'] = IMG[img]
    return cd(c, at=at)
def ai(key, q, at=None):
    """Recreación: si hay imagen IA generada, se usa con rótulo; si no, plano de archivo equivalente."""
    if AI.get(key): return _c(dict(ai=AI[key], at=at, lt=['Recreación', '']))
    return ph(q, at=at)
