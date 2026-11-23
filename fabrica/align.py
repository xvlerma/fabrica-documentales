"""Alineación palabra a palabra de la locución con el guion (gratis, en el runner).

faster-whisper transcribe cada unidad de voz ya procesada (tempo y pausas aplicados) con marcas de tiempo
por palabra; después se casan con las palabras del guion para que cada token del texto tenga su instante.
Así las imágenes, rótulos y tarjetas se anclan a la palabra que los justifica ("at" en el plano)."""
import os, re, json, hashlib, unicodedata, difflib
import numpy as np

_MODEL = {}

def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9ñ]', '', w)

def tokens(text):
    """Palabras del guion sin etiquetas de voz: [(original, normalizada)]."""
    clean = re.sub(r'\[[^\]]*\]', ' ', text or '')
    return [(w, norm(w)) for w in clean.split() if norm(w)]

def _whisper(y, sr, model_name):
    from faster_whisper import WhisperModel
    import librosa
    if model_name not in _MODEL:
        _MODEL[model_name] = WhisperModel(model_name, device='cpu', compute_type='int8', cpu_threads=os.cpu_count() or 2)
    a = y.mean(0) if y.ndim == 2 else y
    a = librosa.resample(a.astype(np.float32), orig_sr=sr, target_sr=16000)
    segs, _ = _MODEL[model_name].transcribe(a, language='es', word_timestamps=True, beam_size=1,
                                            condition_on_previous_text=False, vad_filter=False)
    return [(w.word, float(w.start), float(w.end)) for s in segs for w in (s.words or [])]

def transcribe(y, sr, model_name='small', cache_dir='/tmp'):
    """e29n90: transcripción palabra a palabra de un corte real (para subtítulos de los cortes)."""
    key = hashlib.sha1(('c1' + str(y.shape) + str(float(np.abs(y).sum()))[:12] + model_name).encode()).hexdigest()[:16]
    cp = f'{cache_dir}/clipw_{key}.json'
    if os.path.exists(cp): return json.load(open(cp))
    from faster_whisper import WhisperModel
    import librosa
    if model_name not in _MODEL:
        _MODEL[model_name] = WhisperModel(model_name, device='cpu', compute_type='int8', cpu_threads=os.cpu_count() or 2)
    a = y.mean(0) if y.ndim == 2 else y
    a = librosa.resample(a.astype(np.float32), orig_sr=sr, target_sr=16000)
    segs, _ = _MODEL[model_name].transcribe(a, language='es', word_timestamps=True, beam_size=5, condition_on_previous_text=False)
    out = [dict(w=w.word.strip(), n=norm(w.word), t=round(float(w.start), 3), e=round(float(w.end), 3)) for s_ in segs for w in (s_.words or []) if norm(w.word)]
    json.dump(out, open(cp, 'w'), ensure_ascii=False)
    return out

def remap(text, ws):
    """Corrige el texto de un corte (nombres, cifras) conservando los tiempos de whisper palabra a palabra."""
    tk = tokens(text)
    if not ws or not tk: return []
    hn = [w['n'] for w in ws]; sn = [n for _, n in tk]; times = [None] * len(tk); ends = [None] * len(tk)
    sm = difflib.SequenceMatcher(None, sn, hn, autojunk=False)
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == 'equal':
            for k in range(a1 - a0): times[a0 + k] = ws[b0 + k]['t']; ends[a0 + k] = ws[b0 + k].get('e')
        elif op == 'replace' or (op == 'insert' and b1 > b0):
            t0 = ws[b0]['t'] if b0 < len(ws) else ws[-1]['t']; t1 = ws[b1 - 1].get('e') or ws[b1 - 1]['t'] + 0.3
            for k in range(a1 - a0): times[a0 + k] = t0 + (t1 - t0) * k / max(1, a1 - a0)
    last = ws[0]['t']
    for i in range(len(times)):
        if times[i] is None: times[i] = last + 0.15
        last = times[i] = max(times[i], last)
    return [dict(w=o, n=n, t=round(t, 3), **({'e': e} if e else {})) for (o, n), t, e in zip(tk, times, ends)]

def proportional(text, d):
    """Sin voz real (casting) o si falla whisper: reparto por caracteres."""
    tk = tokens(text); tot = sum(len(o) + 1 for o, _ in tk) or 1; acc = 0; out = []
    for o, n in tk:
        out.append(dict(w=o, n=n, t=round(d * acc / tot, 3))); acc += len(o) + 1
    return out

def align_unit(text, y, sr, model_name='base', cache_dir='/tmp'):
    tk = tokens(text)
    if not tk: return []
    key = hashlib.sha1(('v2' + text + str(y.shape) + str(float(np.abs(y).sum()))[:12] + model_name).encode()).hexdigest()[:16]
    cp = f'{cache_dir}/align_{key}.json'
    if os.path.exists(cp): return json.load(open(cp))
    d = y.shape[-1] / sr
    try: hyp = _whisper(y, sr, model_name)
    except Exception as e:
        print('aviso alineación (reparto proporcional):', e, flush=True); return proportional(text, d)
    hn = [norm(w) for w, _, _ in hyp]; sn = [n for _, n in tk]
    times = [None] * len(tk)
    sm = difflib.SequenceMatcher(None, sn, hn, autojunk=False)
    for a, b, size in sm.get_matching_blocks():
        for k in range(size): times[a + k] = hyp[b + k][1]
    # reemplazos 1 a 1 (números, nombres mal transcritos): toma el inicio de la palabra transcrita
    # reemplazos (cifras dichas en letra y transcritas en número, nombres mal oídos): reparte el tramo transcrito
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == 'replace':
            t0, t1 = hyp[b0][1], hyp[b1 - 1][2]; L = sum(len(tk[a0 + k][1]) + 1 for k in range(a1 - a0)); acc = 0
            for k in range(a1 - a0):
                if times[a0 + k] is None: times[a0 + k] = t0 + (t1 - t0) * acc / max(1, L)
                acc += len(tk[a0 + k][1]) + 1
    # huecos: interpolación lineal por posición
    known = [i for i, t in enumerate(times) if t is not None]
    if not known: return proportional(text, d)
    for i in range(len(times)):
        if times[i] is not None: continue
        L = max([k for k in known if k < i], default=None); R = min([k for k in known if k > i], default=None)
        if L is None: times[i] = max(0.0, times[R] - 0.3 * (R - i))
        elif R is None: times[i] = min(d, times[L] + 0.3 * (i - L))
        else: times[i] = times[L] + (times[R] - times[L]) * (i - L) / (R - L)
    for i in range(1, len(times)): times[i] = max(times[i], times[i - 1])
    out = [dict(w=o, n=n, t=round(t, 3)) for (o, n), t in zip(tk, times)]
    json.dump(out, open(cp, 'w'), ensure_ascii=False)
    return out

def find(words, phrase, start=0):
    """Índice de la primera palabra de `phrase` en `words` desde `start` (exacto y, si no, aproximado)."""
    q = [n for _, n in tokens(phrase)]
    if not q or not words: return None
    seq = [w['n'] for w in words]; L = len(q)
    for rng in (range(start, len(seq) - L + 1), range(0, len(seq) - L + 1)):
        for j in rng:
            if seq[j:j + L] == q: return j
    best, bj = 0.0, None; s = ' '.join(q)
    for j in range(0, max(1, len(seq) - L + 1)):
        r = difflib.SequenceMatcher(None, s, ' '.join(seq[j:j + L])).ratio()
        if r > best + (0.02 if j < start else 0): best, bj = r, j
    return bj if best >= 0.72 else None
