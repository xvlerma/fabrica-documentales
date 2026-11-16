"""Movimiento de cámara 2,5D sobre una foto: mapa de profundidad + desplazamiento por capas.
Si no hay modelo de profundidad disponible, devuelve None y el motor usa el zoom plano."""
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
    with _lock:  # el modelo no es seguro entre hilos
        d = np.asarray(m(Image.fromarray(img_rgb))['predicted_depth'].squeeze().cpu().numpy(), np.float32)
    d = cv2.resize(d, (img_rgb.shape[1], img_rgb.shape[0]), interpolation=cv2.INTER_CUBIC)
    lo, hi = np.percentile(d, 2), np.percentile(d, 98)
    d = np.clip((d - lo) / max(1e-6, hi - lo), 0, 1)
    d = cv2.GaussianBlur(d, (0, 0), sigmaX=img_rgb.shape[1] / 300)  # bordes suaves: menos desgarros
    return d

# movimientos: (zoom inicio, zoom fin, paneo x, paneo y, dolly de profundidad, órbita lateral)
MOVES25 = [(1.04, 1.10, 0.00, 0.00, 0.10, 0.000), (1.10, 1.04, 0.00, 0.00, -0.08, 0.000),
           (1.08, 1.08, 0.04, 0.00, 0.03, 0.022), (1.08, 1.08, -0.04, 0.00, 0.03, -0.022),
           (1.06, 1.10, 0.02, -0.02, 0.07, 0.012), (1.10, 1.06, -0.02, 0.02, -0.05, -0.012)]

def frames(canvas_rgb, W, H, N, move):
    """Genera N fotogramas BGR WxH. canvas_rgb: imagen preparada (más grande que la salida)."""
    import cv2
    D = depth(canvas_rgb)
    if D is None: return None
    ch, cw = canvas_rgb.shape[:2]; src = cv2.cvtColor(canvas_rgb, cv2.COLOR_RGB2BGR)
    z0, z1, px, py, dz, orb = MOVES25[move % len(MOVES25)]
    base = min(cw / W, ch / H)  # píxeles de lienzo por píxel de salida con zoom 1
    u, v = np.meshgrid(np.arange(W, dtype=np.float32) - W / 2, np.arange(H, dtype=np.float32) - H / 2)
    def gen():
        for f in range(N):
            e = 0.5 - 0.5 * math.cos(math.pi * f / max(1, N - 1))
            z = z0 + (z1 - z0) * e; s = base / z
            cx = cw / 2 + px * cw * (e - .5); cy = ch / 2 + py * ch * (e - .5)
            X = cx + u * s; Y = cy + v * s
            d = cv2.remap(D, X, Y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
            k = 1 + dz * e * d  # lo cercano crece más en el dolly
            orbx = orb * cw * (e - .5) * (d - .35)  # lo cercano se desplaza más en la órbita
            Xs = cx + (X - cx) / k - orbx; Ys = cy + (Y - cy) / k
            yield cv2.remap(src, Xs.astype(np.float32), Ys.astype(np.float32), cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    return gen()
