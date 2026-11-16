"""Cámara 2,5D sobre una foto: mapa de profundidad + desplazamiento por capas, cámara al hombro,
cambio de foco, parpadeo de llama y tratamiento de película para recreaciones.
Si no hay modelo de profundidad, devuelve None y el motor usa el zoom plano."""
import threading, math
import numpy as np

_lock = threading.Lock(); _pipe = [None]; _failed = [False]

def _model():
    if _pipe[0] is not None or _failed[0]: return _pipe[0]
    with _lock:
        if _pipe[0] is None and not _failed[0]:
            try:
                from transformers import pipeline
                _pipe[0] = pipeline('depth-estimation', model='depth-anything/Depth-Anything-V2-Small-hf', device=-1)
            except Exception as e:
                print('  aviso: sin modelo de profundidad ->', e, flush=True); _failed[0] = True
    return _pipe[0]

def depth(img_rgb):
    """img_rgb: np.uint8 HxWx3. Devuelve profundidad 0..1 (1 = cerca), suavizada."""
    import cv2
    from PIL import Image
    m = _model()
    if m is None: return None
    with _lock:
        d = np.asarray(m(Image.fromarray(img_rgb))['predicted_depth'].squeeze().cpu().numpy(), np.float32)
    d = cv2.resize(d, (img_rgb.shape[1], img_rgb.shape[0]), interpolation=cv2.INTER_CUBIC)
    lo, hi = np.percentile(d, 2), np.percentile(d, 98)
    d = np.clip((d - lo) / max(1e-6, hi - lo), 0, 1)
    return cv2.GaussianBlur(d, (0, 0), sigmaX=img_rgb.shape[1] / 300)

# (zoom inicio, zoom fin, paneo x, paneo y, dolly de profundidad, órbita lateral)
MOVES25 = [(1.04, 1.10, 0.00, 0.00, 0.10, 0.000), (1.10, 1.04, 0.00, 0.00, -0.08, 0.000),
           (1.08, 1.08, 0.04, 0.00, 0.03, 0.022), (1.08, 1.08, -0.04, 0.00, 0.03, -0.022),
           (1.06, 1.10, 0.02, -0.02, 0.07, 0.012), (1.10, 1.06, -0.02, 0.02, -0.05, -0.012)]

def _noise(N, fps, freqs, seed):
    rng = np.random.default_rng(seed); t = np.arange(N) / fps; out = np.zeros(N)
    for f, a in freqs: out += a * np.sin(2 * math.pi * f * t + rng.uniform(0, 2 * math.pi))
    return out

def film_treatment(rgb, dark=0.82, soften=0.7, seed=0):
    """Recreación IA → 'rodada': menos nitidez plástica, halo en altas luces, negros levantados, más oscura, desaturada."""
    import cv2
    x = rgb.astype(np.float32) / 255
    if soften: x = cv2.GaussianBlur(x, (0, 0), soften)
    lum = x.mean(2, keepdims=True)
    small = cv2.resize(np.clip(lum - 0.62, 0, 1)[..., 0], (x.shape[1] // 8, x.shape[0] // 8), interpolation=cv2.INTER_AREA)
    hl = cv2.resize(cv2.GaussianBlur(small, (0, 0), x.shape[1] / 720), (x.shape[1], x.shape[0]))[..., None] * np.array([1.0, 0.55, 0.3], np.float32)
    x = x + hl * 0.9
    x = lum + (x - lum) * 0.82            # desatura
    x = 0.035 + x * (1 - 0.035) * dark      # negros de película y exposición más baja
    return np.clip(x * 255, 0, 255).astype(np.uint8)

def frames(canvas_rgb, W, H, N, move, fps=25, fx=None):
    """Genera N fotogramas BGR WxH. fx: dict(shake, focus=(a,b), flicker, seed)."""
    import cv2
    fx = fx or {}
    D = depth(canvas_rgb)
    if D is None: return None
    ch, cw = canvas_rgb.shape[:2]; src = cv2.cvtColor(canvas_rgb, cv2.COLOR_RGB2BGR)
    z0, z1, px, py, dz, orb = MOVES25[move % len(MOVES25)]
    base = min(cw / W, ch / H)
    u, v = np.meshgrid(np.arange(W, dtype=np.float32) - W / 2, np.arange(H, dtype=np.float32) - H / 2)
    seed = fx.get('seed', move)
    sx = _noise(N, fps, [(0.31, 1), (0.83, .45), (2.1, .12)], seed) * cw * 0.0035 * fx.get('shake', 0)
    sy = _noise(N, fps, [(0.27, 1), (0.71, .4), (1.9, .12)], seed + 1) * ch * 0.0035 * fx.get('shake', 0)
    fl = 1 + (_noise(N, fps, [(1.3, .5), (3.7, .35), (7.9, .2), (11.3, .1)], seed + 2) * 0.045 * fx.get('flicker', 0))
    focus = fx.get('focus')
    def gen():
        for f in range(N):
            e = 0.5 - 0.5 * math.cos(math.pi * f / max(1, N - 1))
            z = z0 + (z1 - z0) * e; s = base / z
            cx = cw / 2 + px * cw * (e - .5) + sx[f]; cy = ch / 2 + py * ch * (e - .5) + sy[f]
            X = (cx + u * s).astype(np.float32); Y = (cy + v * s).astype(np.float32)
            d = cv2.remap(D, X, Y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
            k = 1 + dz * e * d
            orbx = orb * cw * (e - .5) * (d - .35)
            Xs = (cx + (X - cx) / k - orbx).astype(np.float32); Ys = (cy + (Y - cy) / k).astype(np.float32)
            img = cv2.remap(src, Xs, Ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
            if focus:
                fp = focus[0] + (focus[1] - focus[0]) * (0.5 - 0.5 * math.cos(math.pi * min(1, max(0, (f / max(1, N - 1) - .2) / .5))))
                w = cv2.resize(np.clip(np.abs(d[::4, ::4] - fp) * 2.6 - .15, 0, 1), (W, H))[..., None]
                bl = cv2.resize(cv2.GaussianBlur(cv2.resize(img, (W // 4, H // 4), interpolation=cv2.INTER_AREA), (0, 0), 1.8), (W, H))
                img = cv2.convertScaleAbs(img * (1 - w) + bl * w)
            if fx.get('flicker'): img = cv2.convertScaleAbs(img, alpha=float(fl[f]))
            yield img
    return gen()
