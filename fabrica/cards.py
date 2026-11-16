"""Grafismo animado del canal: título, cita, ficha, lista, cronología y mapa con flechas.
Cada tarjeta se dibuja fotograma a fotograma (PIL) y se codifica con ffmpeg."""
import os, json, math, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1920, 1080, 25
HERE = os.path.dirname(os.path.abspath(__file__))
GOLD = (214, 178, 112); CREAM = (236, 224, 200); DIM = (170, 150, 120); RED = (178, 60, 40)
_bgcache = {}

def font(name, size): return ImageFont.truetype(f'{HERE}/fonts/{name}.ttf', size)

def bg(seed=1):
    if seed in _bgcache: return _bgcache[seed].copy()
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, (H // 8, W // 8))
    img = Image.fromarray(((n - n.min()) / (n.max() - n.min()) * 255).astype('uint8')).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18))
    a = np.asarray(img, dtype=np.float32) / 255
    base = np.array([18, 14, 10], np.float32); hi = np.array([58, 44, 28], np.float32)
    rgb = base + (hi - base) * a[..., None] ** 1.6
    yy, xx = np.mgrid[0:H, 0:W]
    v = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    rgb = np.clip(rgb * np.clip(v, 0.25, 1)[..., None], 0, 255)
    _bgcache[seed] = Image.fromarray(rgb.astype('uint8')).convert('RGBA')
    return _bgcache[seed].copy()

def ease(x): x = max(0., min(1., x)); return 0.5 - 0.5 * math.cos(math.pi * x)

def text_layer(text, f, fill, spacing=0.0):
    d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    if spacing:
        ws = [d0.textlength(c, font=f) for c in text]; tw = int(sum(ws) + f.size * spacing * (len(text) - 1)) + 4
    else:
        tw = int(d0.textlength(text, font=f)) + 4
    th = int(f.size * 1.45)
    im = Image.new('RGBA', (max(tw, 1), th), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if spacing:
        x = 2
        for c, w in zip(text, ws): d.text((x, th / 2), c, font=f, fill=fill, anchor='lm'); x += w + f.size * spacing
    else: d.text((2, th / 2), text, font=f, fill=fill, anchor='lm')
    return im

def put(frame, layer, cx, cy, a, anchor='mm', dy=0):
    if a <= 0: return
    x = int(cx - layer.width / 2) if anchor == 'mm' else int(cx); y = int(cy - layer.height / 2 + dy)
    if a < 1:
        r, g, b, al = layer.split(); al = al.point(lambda v: int(v * a)); layer = Image.merge('RGBA', (r, g, b, al))
    frame.alpha_composite(layer, (max(0, x), max(0, y)))

def wrap(text, f, maxw):
    d = ImageDraw.Draw(Image.new('RGB', (1, 1))); words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def rule_layer(w=320):
    im = Image.new('RGBA', (w + 20, 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.line([(10, 10), (w + 10, 10)], fill=GOLD, width=2); c = w / 2 + 10
    d.polygon([(c, 3), (c + 7, 10), (c, 17), (c - 7, 10)], fill=GOLD); return im

# ---------- tipos ----------
def f_title(spec, t, D):
    fr = bg(spec.get('seed', 11))
    a = ease(t / 1.2); s = 1 + 0.03 * (t / D)
    L = text_layer(spec['title'].upper(), font('cinzel600', int(116 * s)), GOLD, 0.10)
    put(fr, L, W / 2, H / 2 - 40, a)
    if spec.get('sub'):
        put(fr, rule_layer(400), W / 2, H / 2 + 45, ease((t - .6) / 1))
        put(fr, text_layer(spec['sub'], font('corm500i', 56), CREAM), W / 2, H / 2 + 110, ease((t - .9) / 1))
    return fr

def f_ficha(spec, t, D):
    fr = bg(spec.get('seed', 13))
    put(fr, text_layer(spec['name'].upper(), font('cinzel600', 110), GOLD, 0.1), W / 2, H / 2 - 30, ease(t / .8), dy=int(30 * (1 - ease(t / .8))))
    put(fr, rule_layer(360), W / 2, H / 2 + 50, ease((t - .5) / .8))
    put(fr, text_layer(spec.get('role', ''), font('corm500i', 54), CREAM), W / 2, H / 2 + 115, ease((t - .8) / .8))
    return fr

def f_quote(spec, t, D):
    fr = bg(spec.get('seed', 21)); f = font('corm500i', 62)
    lines = wrap('«' + spec['text'] + '»', f, 1400); lh = 84; y0 = H / 2 - len(lines) * lh / 2 - 40
    step = min(1.2, (D * 0.5) / max(1, len(lines)))
    for i, l in enumerate(lines):
        put(fr, text_layer(l, f, CREAM), W / 2, y0 + i * lh, ease((t - .3 - i * step) / .9))
    yb = y0 + len(lines) * lh + 30; ta = .3 + len(lines) * step
    put(fr, rule_layer(300), W / 2, yb, ease((t - ta) / .8))
    put(fr, text_layer(spec.get('attrib', '').upper(), font('cinzel400', 30), GOLD, 0.15), W / 2, yb + 55, ease((t - ta - .3) / .8))
    return fr

def f_list(spec, t, D):
    fr = bg(spec.get('seed', 41)); items = spec['items']; n = len(items)
    put(fr, text_layer(spec['header'].upper(), font('cinzel600', 58), GOLD, 0.12), W / 2, 190, ease(t / .8))
    put(fr, rule_layer(360), W / 2, 250, ease((t - .3) / .8))
    step = min(1.4, (D * 0.65) / max(1, n)); gap = min(120, 640 / n)
    for i, it in enumerate(items):
        a, b = (it if isinstance(it, (list, tuple)) else (it, None))
        k = ease((t - .8 - i * step) / .7)
        put(fr, text_layer(a, font('corm500', 52), CREAM), W / 2, 330 + i * gap, k, dy=int(18 * (1 - k)))
        if b: put(fr, text_layer(b, font('corm500i', 40), DIM), W / 2, 374 + i * gap, k)
    return fr

def f_timeline(spec, t, D):
    fr = bg(spec.get('seed', 51)); ev = spec['events']; n = len(ev)
    y = H / 2 + 20; x0, x1 = 220, W - 220
    if spec.get('header'): put(fr, text_layer(spec['header'].upper(), font('cinzel600', 50), GOLD, 0.12), W / 2, 150, ease(t / .8))
    p = ease((t - .3) / (D * 0.6)); d = ImageDraw.Draw(fr)
    d.line([(x0, y), (x0 + (x1 - x0) * p, y)], fill=GOLD, width=3)
    for i, (yr, txt) in enumerate(ev):
        fx = (i / (n - 1)) if n > 1 else .5; x = x0 + (x1 - x0) * fx
        k = ease((p - fx) * 6 + 1) if p >= fx else 0
        if k <= 0: continue
        r = 11 * k; d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD)
        up = i % 2 == 0
        put(fr, text_layer(yr, font('cinzel600', 44), GOLD), x, y - 70 if up else y + 70, k)
        for j, l in enumerate(wrap(txt, font('corm500', 38), 380)):
            put(fr, text_layer(l, font('corm500', 38), CREAM), x, (y - 135 - j * 46) if up else (y + 130 + j * 46), k)
    return fr

_land = {}
def _geo(name):
    if name in _land: return _land[name]
    from sources import download
    p = download(f'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/{name}.geojson', '.geojson')
    _land[name] = json.load(open(p)); return _land[name]

def _map_base(bbox, seed):
    key = ('map', tuple(bbox))
    if key in _bgcache: return _bgcache[key].copy()
    lon0, lat0, lon1, lat1 = bbox
    # ajusta el encuadre a 16:9 en proyección equirectangular corregida por latitud
    k = math.cos(math.radians((lat0 + lat1) / 2))
    def P(lon, lat): return ((lon - lon0) / (lon1 - lon0) * W, (lat1 - lat) / (lat1 - lat0) * H)
    im = Image.new('RGBA', (W, H), (14, 20, 26, 255)); d = ImageDraw.Draw(im)
    for f in _geo('ne_50m_land')['features']:
        g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
        for poly in polys:
            pts = [P(x, y) for x, y in poly[0]]
            if len(pts) > 2: d.polygon(pts, fill=(58, 46, 32, 255), outline=(150, 120, 80, 255))
    try:
        for f in _geo('ne_50m_rivers_lake_centerlines')['features']:
            g = f['geometry']; ls = g['coordinates'] if g['type'] == 'MultiLineString' else [g['coordinates']]
            for l in ls: d.line([P(x, y) for x, y in l], fill=(70, 110, 130, 255), width=3)
    except Exception: pass
    im = im.filter(ImageFilter.GaussianBlur(0.6))
    vg = bg(seed); arr = np.asarray(im).astype(np.float32); v = np.asarray(vg).astype(np.float32)
    arr[..., :3] = arr[..., :3] * 0.75 + v[..., :3] * 0.35
    out = Image.fromarray(np.clip(arr, 0, 255).astype('uint8'), 'RGBA'); _bgcache[key] = out
    return out.copy()

def f_map(spec, t, D):
    bbox = spec['bbox']; lon0, lat0, lon1, lat1 = bbox
    def P(lon, lat): return ((lon - lon0) / (lon1 - lon0) * W, (lat1 - lat) / (lat1 - lat0) * H)
    fr = _map_base(bbox, spec.get('seed', 61)); d = ImageDraw.Draw(fr)
    if spec.get('title'): put(fr, text_layer(spec['title'].upper(), font('cinzel600', 46), GOLD, 0.12), W / 2, 80, ease(t / .8))
    pts = spec.get('points', []); arrows = spec.get('arrows', [])
    for i, p in enumerate(pts):
        k = ease((t - .5 - i * .35) / .6)
        if k <= 0: continue
        x, y = P(p['lon'], p['lat']); r = 9 * k
        d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD, outline=(20, 15, 10))
        put(fr, text_layer(p['name'], font('corm600', 40), CREAM), x + 16, y, k, anchor='lm')
    t0 = .6 + len(pts) * .35
    for i, a in enumerate(arrows):
        path = [P(lon, lat) for lon, lat in a['path']]
        k = ease((t - t0 - i * 1.0) / 1.6)
        if k <= 0 or len(path) < 2: continue
        L = [math.dist(path[j], path[j + 1]) for j in range(len(path) - 1)]; tot = sum(L); goal = tot * k; acc = 0; seg = [path[0]]
        for j, l in enumerate(L):
            if acc + l >= goal:
                r = (goal - acc) / l; seg.append((path[j][0] + (path[j + 1][0] - path[j][0]) * r, path[j][1] + (path[j + 1][1] - path[j][1]) * r)); break
            seg.append(path[j + 1]); acc += l
        col = tuple(a.get('color', RED))
        d.line(seg, fill=col, width=7, joint='curve')
        (xa, ya), (xb, yb) = seg[-2], seg[-1]; ang = math.atan2(yb - ya, xb - xa)
        d.polygon([(xb + 22 * math.cos(ang), yb + 22 * math.sin(ang)), (xb + 14 * math.cos(ang + 2.4), yb + 14 * math.sin(ang + 2.4)),
                   (xb + 14 * math.cos(ang - 2.4), yb + 14 * math.sin(ang - 2.4))], fill=col)
        if a.get('label') and k > .6:
            mx, my = path[len(path) // 2]; put(fr, text_layer(a['label'], font('corm500i', 38), CREAM), mx, my - 36, ease((k - .6) / .4))
    return fr

KIND = dict(title=f_title, ficha=f_ficha, quote=f_quote, list=f_list, timeline=f_timeline, map=f_map)

def render_card(spec, dur, out, fade_in=.25, fade_out=.0):
    N = max(1, round(dur * FPS)); fn = KIND[spec['type']]
    vf = []
    if fade_in: vf.append(f'fade=t=in:st=0:d={fade_in}')
    if fade_out: vf.append(f'fade=t=out:st={N / FPS - fade_out:.3f}:d={fade_out}')
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           *(['-vf', ','.join(vf)] if vf else []), '-frames:v', str(N), '-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-maxrate', '1.6M',
           '-bufsize', '3.2M', '-g', '50', '-pix_fmt', 'yuv420p', out + '.tmp.mp4']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    last = None
    for i in range(N):
        t = i / FPS
        # fotogramas estáticos al final: reutiliza para ir más rápido
        frame = fn(spec, t, dur).convert('RGB').tobytes() if (t < dur * 0.8 + 2 or last is None) else last
        last = frame; p.stdin.write(frame)
    p.stdin.close(); p.wait()
    if p.returncode: raise RuntimeError('card render failed')
    os.rename(out + '.tmp.mp4', out)

def lower_third(a, b, out):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    gd.rectangle([0, H - 260, 1100, H - 90], fill=(0, 0, 0, 150)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))
    d = ImageDraw.Draw(im); d.line([(120, H - 205), (190, H - 205)], fill=GOLD, width=3)
    im.alpha_composite(text_layer(a.upper(), font('cinzel600', 52), GOLD, 0.10), (118, H - 200))
    if b: im.alpha_composite(text_layer(b, font('corm500i', 40), CREAM), (120, H - 138))
    im.save(out)
