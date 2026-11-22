"""Grafismo animado del canal: título, cita, ficha, lista, cronología y mapa con flechas.
Cada tarjeta se dibuja fotograma a fotograma (PIL) y se codifica con ffmpeg."""
import os, json, math, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1920, 1080, 25
HERE = os.path.dirname(os.path.abspath(__file__))
GOLD = (214, 178, 112); CREAM = (236, 224, 200); DIM = (170, 150, 120); RED = (178, 60, 40)
BG0 = (18, 14, 10); BG1 = (58, 44, 28); SEA = (14, 20, 26); LAND = (58, 46, 32); COAST = (150, 120, 80); RIVER = (70, 110, 130)
PAPER = (222, 208, 178); INK = (40, 28, 18); STRING = (170, 30, 25)
BRAND_DOT = (242, 255, 0)  # amarillo DocuVox: solo como punto mínimo en los rótulos
THEME = {}
_bgcache = {}
_fcache = {}
ROLE = {'cinzel600': 'display', 'cinzel400': 'display_light', 'corm500': 'body', 'corm500i': 'italic', 'corm600': 'body_bold'}

def set_theme(spec):
    """Aplica la piel del episodio: preset de themes.json o dict con 'base' + cambios."""
    global GOLD, CREAM, DIM, RED, BG0, BG1, SEA, LAND, COAST, RIVER, PAPER, INK, STRING
    presets = json.load(open(f'{HERE}/themes.json', encoding='utf-8'))
    if isinstance(spec, str): spec = {'base': spec}
    spec = spec or {}
    t = dict(presets.get(spec.get('base', 'antiguo'), presets['antiguo']))
    for k, v in spec.items():
        if k == 'fonts': t['fonts'] = {**t['fonts'], **v}
        elif k != 'base': t[k] = v
    THEME.clear(); THEME.update(t); _bgcache.clear(); _fcache.clear()
    c = lambda k: tuple(int(x) for x in t[k])
    GOLD, CREAM, DIM, RED = c('accent'), c('text'), c('dim'), c('alert')
    BG0, BG1, SEA, LAND, COAST, RIVER = c('bg0'), c('bg1'), c('sea'), c('land'), c('coast'), c('river')
    PAPER, INK, STRING = c('paper'), c('ink'), c('string')
    return THEME

def _font_file(ref):
    if not ref.startswith('gf:'): return f'{HERE}/fonts/{ref}.ttf', None
    path, _, w = ref[3:].partition('@')
    from sources import download
    import urllib.parse
    f = download('https://raw.githubusercontent.com/google/fonts/main/' + urllib.parse.quote(path), '.ttf')
    return f, (int(w) if w else None)

def font(name, size):
    ref = (THEME.get('fonts') or {}).get(ROLE.get(name, name), name)
    key = (ref, size)
    if key in _fcache: return _fcache[key]
    try:
        path, wght = _font_file(ref); f = ImageFont.truetype(path, size)
        try:
            axes = f.get_variation_axes(); vals = []
            for a in axes:
                nm = (a.get('name') or b'')
                nm = nm.decode() if isinstance(nm, bytes) else str(nm)
                if 'eight' in nm and wght: vals.append(max(a['minimum'], min(a['maximum'], wght)))
                elif 'ptical' in nm: vals.append(max(a['minimum'], min(a['maximum'], size * 0.5)))
                else: vals.append(a.get('default', a['minimum']))
            if vals: f.set_variation_by_axes(vals)
        except Exception: pass
    except Exception as e:
        print('aviso fuente', ref, e, flush=True); f = ImageFont.truetype(f'{HERE}/fonts/{name if name in ROLE else "corm500"}.ttf', size)
    _fcache[key] = f; return f

def CASE(s):
    m = THEME.get('case', 'upper'); return s.upper() if m == 'upper' else s

def TR(x): return x * THEME.get('tracking', 1.0)

def bg(seed=1):
    if seed in _bgcache: return _bgcache[seed].copy()
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, (H // 8, W // 8))
    img = Image.fromarray(((n - n.min()) / (n.max() - n.min()) * 255).astype('uint8')).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18))
    a = np.asarray(img, dtype=np.float32) / 255
    base = np.array(BG0, np.float32); hi = np.array(BG1, np.float32)
    rgb = base + (hi - base) * a[..., None] ** 1.6
    rgb += rng.normal(0, 3.2, (H, W, 1)).astype(np.float32)  # grano fino de película
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

def fit(name, size, text, maxw, spacing=0.0):
    """Reduce el cuerpo hasta que el texto quepa en maxw (títulos largos)."""
    while size > 24:
        f = font(name, size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
        w = d0.textlength(text, font=f) + f.size * spacing * max(0, len(text) - 1)
        if w <= maxw: return f
        size = int(size * 0.94)
    return font(name, size)

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
    im = Image.new('RGBA', (w + 20, 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im); st = THEME.get('rule', 'diamond')
    if st == 'bar': d.rectangle([10, 8, w + 10, 12], fill=GOLD); return im
    d.line([(10, 10), (w + 10, 10)], fill=GOLD, width=2); c = w / 2 + 10
    if st == 'diamond': d.polygon([(c, 3), (c + 7, 10), (c, 17), (c - 7, 10)], fill=GOLD)
    return im

# ---------- tipos ----------
def f_title(spec, t, D):
    fr = bg(spec.get('seed', 11))
    a = ease(t / 1.2); s = 1 + 0.03 * (t / D)
    _t = CASE(spec['title']); L = text_layer(_t, fit('cinzel600', int(116 * s), _t, 1680 * s, TR(0.10)), GOLD, TR(0.10))
    put(fr, L, W / 2, H / 2 - 40, a)
    if spec.get('sub'):
        put(fr, rule_layer(400), W / 2, H / 2 + 45, ease((t - .6) / 1))
        put(fr, text_layer(spec['sub'], font('corm500i', 56), CREAM), W / 2, H / 2 + 110, ease((t - .9) / 1))
    return fr

def f_ficha(spec, t, D):
    fr = bg(spec.get('seed', 13))
    put(fr, text_layer(CASE(spec['name']), fit('cinzel600', 110, CASE(spec['name']), 1680, TR(0.1)), GOLD, TR(0.1)), W / 2, H / 2 - 30, ease(t / .8), dy=int(30 * (1 - ease(t / .8))))
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
    put(fr, text_layer(CASE(spec.get('attrib', '')), font('cinzel400', 30), GOLD, TR(0.15)), W / 2, yb + 55, ease((t - ta - .3) / .8))
    return fr

def f_list(spec, t, D):
    fr = bg(spec.get('seed', 41)); items = spec['items']; n = len(items)
    put(fr, text_layer(CASE(spec['header']), font('cinzel600', 58), GOLD, TR(0.12)), W / 2, 190, ease(t / .8))
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
    if spec.get('header'): put(fr, text_layer(CASE(spec['header']), font('cinzel600', 50), GOLD, TR(0.12)), W / 2, 150, ease(t / .8))
    p = ease((t - .3) / (D * 0.6)); d = ImageDraw.Draw(fr)
    d.line([(x0, y), (x0 + (x1 - x0) * p, y)], fill=GOLD, width=3)
    for i, (yr, txt) in enumerate(ev):
        fx = (i / (n - 1)) if n > 1 else .5; x = x0 + (x1 - x0) * fx
        k = ease((p - fx) * 6 + 1) if p >= fx else 0
        if k <= 0: continue
        r = 11 * k; d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD)
        up = i % 2 == 0
        put(fr, text_layer(yr, font('cinzel600', 44), GOLD), x, y - 70 if up else y + 70, k)
        ls_ = wrap(txt, font('corm500', 38), 380)
        for j, l in enumerate(ls_[::-1] if up else ls_):
            put(fr, text_layer(l, font('corm500', 38), CREAM), x, (y - 135 - j * 46) if up else (y + 130 + j * 46), k)
    return fr

_land = {}
def fit_bbox(bbox):
    """Amplía el encuadre a 16:9 sin deformar (corrección por latitud) y deja aire arriba para el título."""
    lon0, lat0, lon1, lat1 = bbox; lat1 += (lat1 - lat0) * 0.16
    k = math.cos(math.radians((lat0 + lat1) / 2)); cx, cy = (lon0 + lon1) / 2, (lat0 + lat1) / 2
    L, A = lon1 - lon0, lat1 - lat0; need = W * A / (k * H)
    if need > L: L = need
    else: A = L * k * H / W
    return [cx - L / 2, cy - A / 2, cx + L / 2, cy + A / 2]
def _geo(name):
    if name in _land: return _land[name]
    from sources import download
    p = download(f'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/{name}.geojson', '.geojson')
    _land[name] = json.load(open(p)); return _land[name]

def _map_base(bbox, seed):
    key = ('map', tuple(bbox))
    if key in _bgcache: return _bgcache[key].copy()
    lon0, lat0, lon1, lat1 = bbox = fit_bbox(bbox)
    # ajusta el encuadre a 16:9 en proyección equirectangular corregida por latitud
    k = math.cos(math.radians((lat0 + lat1) / 2))
    def P(lon, lat): return ((lon - lon0) / (lon1 - lon0) * W, (lat1 - lat) / (lat1 - lat0) * H)
    im = Image.new('RGBA', (W, H), SEA + (255,)); d = ImageDraw.Draw(im)
    for f in _geo('ne_50m_land')['features']:
        g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
        for poly in polys:
            pts = [P(x, y) for x, y in poly[0]]
            if len(pts) > 2: d.polygon(pts, fill=LAND + (255,), outline=COAST + (255,))
    try:
        for f in _geo('ne_50m_rivers_lake_centerlines')['features']:
            g = f['geometry']; ls = g['coordinates'] if g['type'] == 'MultiLineString' else [g['coordinates']]
            for l in ls: d.line([P(x, y) for x, y in l], fill=RIVER + (255,), width=3)
    except Exception: pass
    im = im.filter(ImageFilter.GaussianBlur(0.6))
    vg = bg(seed); arr = np.asarray(im).astype(np.float32); v = np.asarray(vg).astype(np.float32)
    arr[..., :3] = arr[..., :3] * 0.75 + v[..., :3] * 0.35
    out = Image.fromarray(np.clip(arr, 0, 255).astype('uint8'), 'RGBA'); _bgcache[key] = out
    return out.copy()

def f_map(spec, t, D):
    bbox = spec['bbox']; lon0, lat0, lon1, lat1 = fit_bbox(bbox)
    def P(lon, lat): return ((lon - lon0) / (lon1 - lon0) * W, (lat1 - lat) / (lat1 - lat0) * H)
    fr = _map_base(bbox, spec.get('seed', 61)); d = ImageDraw.Draw(fr)
    if spec.get('title'):
        band = Image.new('RGBA', (W, 170), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
        for yy in range(170): bd.line([(0, yy), (W, yy)], fill=(8, 8, 10, int(200 * (1 - yy / 170) ** 1.2)))
        fr.alpha_composite(band, (0, 0))
        put(fr, text_layer(CASE(spec['title']), font('cinzel600', 46), GOLD, TR(0.12)), W / 2, 72, ease(t / .8))
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

# ================= GRAFISMO v3 =================
CYAN = (120, 220, 235)
def _lerp(a, b, k): return a + (b - a) * k
def _img(spec, key='_path'):
    c = _bgcache.get(('img', spec[key]))
    if c is None: c = Image.open(spec[key]).convert('RGB'); _bgcache[('img', spec[key])] = c
    return c

def _draw_land(d, P, view, scale):
    lon0, lat0, lon1, lat1 = view
    for f in _geo('ne_50m_land')['features']:
        g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
        for poly in polys:
            ring = poly[0]; xs = [q[0] for q in ring]; ys = [q[1] for q in ring]
            if max(xs) < lon0 or min(xs) > lon1 or max(ys) < lat0 or min(ys) > lat1: continue
            step = max(1, int(len(ring) / 4000)) if scale > 40 else 1
            pts = [P(x, y) for x, y in ring[::step]]
            if len(pts) > 2: d.polygon(pts, fill=LAND + (255,), outline=COAST + (255,))
    try:
        for f in _geo('ne_50m_rivers_lake_centerlines')['features']:
            g = f['geometry']; ls = g['coordinates'] if g['type'] == 'MultiLineString' else [g['coordinates']]
            for l in ls:
                if all(not (lon0 <= x <= lon1 and lat0 <= y <= lat1) for x, y in l[::5] + [l[-1]]): continue
                d.line([P(x, y) for x, y in l], fill=RIVER + (255,), width=3 if scale < 60 else 2)
    except Exception: pass

def f_mapfly(spec, t, D):
    """Viaje de cámara sobre el mapa entre varios encuadres (zoom logarítmico), con lugares y rutas."""
    keys = [fit_bbox(b) for b in spec['keys']]; n = len(keys) - 1
    T = D * spec.get('travel', 0.65); u = min(n, max(0., t / T * n)) if n else 0
    i = min(n - 1, int(u)) if n else 0; k = ease(u - i) if n else 0
    a, b = keys[i], keys[min(n, i + 1)]
    sa, sb = a[2] - a[0], b[2] - b[0]; span = sa * (sb / sa) ** k
    cx = _lerp((a[0] + a[2]) / 2, (b[0] + b[2]) / 2, ease(k)); cy = _lerp((a[1] + a[3]) / 2, (b[1] + b[3]) / 2, ease(k))
    ratio = (a[3] - a[1]) / sa; vs = span * ratio
    view = [cx - span / 2, cy - vs / 2, cx + span / 2, cy + vs / 2]
    def P(lon, lat): return ((lon - view[0]) / span * W, (view[3] - lat) / vs * H)
    im = Image.new('RGBA', (W, H), SEA + (255,)); d = ImageDraw.Draw(im)
    _draw_land(d, P, view, span)
    v = np.asarray(bg(spec.get('seed', 61))).astype(np.float32); arr = np.asarray(im).astype(np.float32)
    arr[..., :3] = arr[..., :3] * 0.75 + v[..., :3] * 0.35
    fr = Image.fromarray(np.clip(arr, 0, 255).astype('uint8'), 'RGBA'); d = ImageDraw.Draw(fr)
    # cuadrícula de coordenadas tenue
    gstep = 10 ** math.floor(math.log10(span / 3))
    for g_ in np.arange(math.floor(view[0] / gstep) * gstep, view[2], gstep): x = P(g_, 0)[0]; d.line([(x, 0), (x, H)], fill=(255, 255, 255, 14))
    for g_ in np.arange(math.floor(view[1] / gstep) * gstep, view[3], gstep): y = P(0, g_)[1]; d.line([(0, y), (W, y)], fill=(255, 255, 255, 14))
    for p_ in spec.get('points', []):
        at = p_.get('at', 0) * D; kk = ease((t - at) / .6)
        if kk <= 0: continue
        x, y = P(p_['lon'], p_['lat'])
        if not (-50 < x < W + 50 and -50 < y < H + 50): continue
        r = (8 + 6 * p_.get('big', 0)) * kk
        if p_.get('pulse'):
            rr = r + 18 * ((t * 1.2) % 1); d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=GOLD + (int(200 * (1 - (t * 1.2) % 1)),), width=2)
        d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD, outline=(20, 15, 10))
        put(fr, text_layer(p_['name'], font('corm600', 40 + 8 * p_.get('big', 0)), CREAM), x + 18, y, kk, anchor='lm')
    for j, a_ in enumerate(spec.get('arrows', [])):
        at = a_.get('at', .7) * D; kk = ease((t - at) / a_.get('dur', 1.6))
        if kk <= 0: continue
        path = [P(lon, lat) for lon, lat in a_['path']]
        L = [math.dist(path[q], path[q + 1]) for q in range(len(path) - 1)]; tot = sum(L); goal = tot * kk; acc = 0; seg = [path[0]]
        for q, l in enumerate(L):
            if acc + l >= goal: r_ = (goal - acc) / max(l, 1e-6); seg.append((path[q][0] + (path[q + 1][0] - path[q][0]) * r_, path[q][1] + (path[q + 1][1] - path[q][1]) * r_)); break
            seg.append(path[q + 1]); acc += l
        col = tuple(a_.get('color', RED)); d.line(seg, fill=col, width=7, joint='curve')
        if len(seg) > 1:
            (xa, ya), (xb, yb) = seg[-2], seg[-1]; ang = math.atan2(yb - ya, xb - xa)
            d.polygon([(xb + 22 * math.cos(ang), yb + 22 * math.sin(ang)), (xb + 14 * math.cos(ang + 2.4), yb + 14 * math.sin(ang + 2.4)), (xb + 14 * math.cos(ang - 2.4), yb + 14 * math.sin(ang - 2.4))], fill=col)
        if a_.get('label') and kk > .6:
            mx, my = path[len(path) // 2]; put(fr, text_layer(a_['label'], font('corm500i', 38), CREAM), mx + 20, my, ease((kk - .6) / .4), anchor='lm')
    if spec.get('title'):
        band = Image.new('RGBA', (W, 170), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
        for yy in range(170): bd.line([(0, yy), (W, yy)], fill=(8, 8, 10, int(200 * (1 - yy / 170) ** 1.2)))
        fr.alpha_composite(band, (0, 0)); put(fr, text_layer(CASE(spec['title']), font('cinzel600', 46), GOLD, TR(0.12)), W / 2, 72, ease(t / .8))
    return fr

def _fit(img, bw, bh):
    w, h = img.size; s = min(bw / w, bh / h); return img.resize((int(w * s), int(h * s)), Image.LANCZOS)

def f_scan(spec, t, D):
    """Escáner forense sobre una imagen real: barrido de TAC, rejilla, marca de hallazgo y datos."""
    src = _img(spec); fr = Image.new('RGBA', (W, H), (4, 8, 12, 255))
    im = _fit(src, 1000, 940); g = np.asarray(im.convert('L')).astype(np.float32) / 255
    xr = 1 - g if spec.get('invert', True) else g
    xr = np.clip((xr - .15) * 1.5, 0, 1) ** 1.2
    tint = np.stack([xr * 120, xr * 225, xr * 240], -1); orig = np.stack([g * 210, g * 200, g * 185], -1)
    p = ease(t / (D * .45)); hh = im.height; cut = int(hh * p)
    out = orig.copy(); out[:cut] = tint[:cut]
    if 0 < cut < hh: out[max(0, cut - 4):cut + 2] = [200, 255, 255]
    ox, oy = 180 + (1000 - im.width) // 2, (H - im.height) // 2
    fr.alpha_composite(Image.fromarray(out.astype('uint8')).convert('RGBA'), (ox, oy)); d = ImageDraw.Draw(fr)
    for gx in range(ox, ox + im.width, 64): d.line([(gx, oy), (gx, oy + hh)], fill=CYAN + (22,))
    for gy in range(oy, oy + hh, 64): d.line([(ox, gy), (ox + im.width, gy)], fill=CYAN + (22,))
    d.rectangle([ox, oy, ox + im.width, oy + hh], outline=CYAN + (90,), width=2)
    for i, txt in enumerate(spec.get('hud', ['TC · CORTE AXIAL', 'MOMIA C1 · MUSEO EGIPCIO DEL CAIRO'])):
        put(fr, text_layer(txt, font('cinzel400', 24), CYAN, TR(0.15)), 1290, 90 + i * 36, ease((t - .3) / .6), anchor='lm')
    if spec.get('mark'):
        mx, my, mr = spec['mark']; X, Y, R = ox + mx * im.width, oy + my * hh, mr * im.width
        k = ease((t - D * .5) / .8)
        if k > 0:
            ang = 360 * k; d.arc([X - R, Y - R, X + R, Y + R], -90, -90 + ang, fill=(235, 70, 50, 255), width=5)
            if k >= 1:
                pulse = R + 14 * ((t * 1.5) % 1); d.ellipse([X - pulse, Y - pulse, X + pulse, Y + pulse], outline=(235, 70, 50, int(160 * (1 - (t * 1.5) % 1))), width=2)
            lab = text_layer(CASE(spec.get('label', '')), font('cinzel600', 36), (245, 120, 90), TR(0.1))
            right = ox + im.width + 40 + lab.width + 20 < W; lx = ox + im.width + 40 if right else ox - 40; ka = ease((t - D * .5 - .6) / .6)
            if ka > 0:
                d.line([(X + R * (1 if lx > X else -1), Y), (_lerp(X, lx, ka), Y)], fill=(235, 70, 50, 255), width=3)
                put(fr, lab, lx + (10 if lx > X else -lab.width - 10), Y, ka, anchor='lm')
                if spec.get('sublabel'):
                    sl = text_layer(spec['sublabel'], font('corm500i', 36), CREAM); put(fr, sl, lx + (10 if lx > X else -sl.width - 10), Y + 50, ka, anchor='lm')
    return fr

def f_doc_txt(spec, t, D):
    """Documento sin imagen: título, texto y fuente en tarjeta tipográfica."""
    fr = bg(spec.get('seed', 71)); f = font('corm500i', 60); lh = 80
    put(fr, text_layer(CASE(spec.get('title', '')), fit('cinzel600', 58, CASE(spec.get('title', '')), 1500, TR(0.12)), GOLD, TR(0.12)), W / 2, 230, ease(t / .8))
    put(fr, rule_layer(360), W / 2, 295, ease((t - .3) / .8))
    lines = [l for x in spec.get('lines', []) for l in wrap(x, f, 1400)]
    y0 = H / 2 - len(lines) * lh / 2 + 20; step = min(1.0, (D * 0.45) / max(1, len(lines)))
    for i, l in enumerate(lines):
        put(fr, text_layer(l, f, CREAM), W / 2, y0 + i * lh, ease((t - .6 - i * step) / .9))
    if spec.get('source'):
        put(fr, text_layer(spec['source'], font('corm500', 34), GOLD), W / 2, H - 170, ease((t - 1.2 - len(lines) * step) / .8))
    return fr

def f_doc(spec, t, D):
    """Documento real (papiro, inscripción) con acercamiento al detalle y traducción línea a línea."""
    if not spec.get('_path'): return f_doc_txt(spec, t, D)
    src = _img(spec); fr = bg(spec.get('seed', 71))
    fx, fy, fw, fh = spec.get('focus', [0, 0, 1, 1]); k = ease(t / (D * .5))
    w0, h0 = src.size; vw = _lerp(1, fw, k) * w0; vh = _lerp(1, fh, k) * h0
    cx = _lerp(w0 / 2, (fx + fw / 2) * w0, k); cy = _lerp(h0 / 2, (fy + fh / 2) * h0, k)
    box = [cx - vw / 2, cy - vh / 2, cx + vw / 2, cy + vh / 2]
    view = src.crop(tuple(int(v) for v in box)); view = _fit(view, 1100, 820)
    ox, oy = 110, (H - view.height) // 2 - 20; fr.alpha_composite(view.convert('RGBA'), (ox, oy)); d = ImageDraw.Draw(fr)
    d.rectangle([ox - 2, oy - 2, ox + view.width + 2, oy + view.height + 2], outline=GOLD + (120,), width=2)
    if spec.get('hl'):
        hx, hy, hw, hh = spec['hl']; kk = ease((t - D * .5) / .6)
        if kk > 0:
            X0, Y0 = ox + hx * view.width, oy + hy * view.height; d.rectangle([X0, Y0, X0 + hw * view.width * kk, Y0 + hh * view.height], outline=GOLD + (255,), width=4)
    ty = 170
    for tl_ in wrap(CASE(spec.get('title', '')), font('cinzel600', 38), 520):
        put(fr, text_layer(tl_, font('cinzel600', 38), GOLD, TR(0.06)), 1290, ty, ease(t / .8), anchor='lm'); ty += 52
    put(fr, rule_layer(260), 1290 + 140, ty + 5, ease((t - .3) / .8))
    lines = spec.get('lines', []); step = (D * .7) / max(1, len(lines)); y = ty + 70
    for i, l in enumerate(lines):
        for j, ww in enumerate(wrap(l, font('corm500i', 42), 520)):
            put(fr, text_layer(ww, font('corm500i', 42), CREAM), 1290, y, ease((t - .8 - i * step) / .7), anchor='lm'); y += 54
        y += 26
    if spec.get('source'): put(fr, text_layer(spec['source'], font('corm500', 28), DIM), 1290, H - 120, ease((t - 1) / .8), anchor='lm')
    return fr

def f_board(spec, t, D):
    """Tablero de investigación: fichas de papel unidas por hilo rojo."""
    fr = bg(spec.get('seed', 81)); d = ImageDraw.Draw(fr); nodes = spec['nodes']; n = len(nodes)
    pos = spec.get('pos') or [(W / 2 + 620 * math.cos(2 * math.pi * i / n - math.pi / 2) * (0 if (i == 0 and spec.get('center')) else 1),
                               H / 2 + 50 + 330 * math.sin(2 * math.pi * i / n - math.pi / 2) * (0 if (i == 0 and spec.get('center')) else 1)) for i in range(n)]
    step = (D * .45) / max(1, n)
    for i, j in spec.get('links', []):
        kk = ease((t - .4 - max(i, j) * step - .3) / .7)
        if kk <= 0: continue
        (x0, y0), (x1, y1) = pos[i], pos[j]; d.line([(x0, y0), (_lerp(x0, x1, kk), _lerp(y0, y1, kk))], fill=STRING + (255,), width=4)
    for i, (name, role) in enumerate(nodes):
        kk = ease((t - .4 - i * step) / .5)
        if kk <= 0: continue
        x, y = pos[i]; cw, ch = 300, 150
        card = Image.new('RGBA', (cw + 40, ch + 40), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
        cd.rectangle([24, 24, cw + 24, ch + 24], fill=(0, 0, 0, 90)); card = card.filter(ImageFilter.GaussianBlur(6)); cd = ImageDraw.Draw(card)
        cd.rectangle([16, 16, cw + 16, ch + 16], fill=PAPER + (255,))
        cd.text((cw / 2 + 16, 70), name.upper(), font=font('cinzel600', 34 if len(name) < 14 else 26), fill=INK, anchor='mm')
        cd.text((cw / 2 + 16, 120), role, font=font('corm500i', 28), fill=tuple(int(a * .55 + b * .45) for a, b in zip(INK, PAPER)), anchor='mm')
        cd.ellipse([cw / 2 + 6, 10, cw / 2 + 26, 30], fill=STRING + (255,))
        card = card.rotate(((i * 37) % 9 - 4) * .8, resample=Image.BICUBIC, expand=True)
        put(fr, card, x, y - 25 * (1 - kk), kk)
    if spec.get('title'): put(fr, text_layer(CASE(spec['title']), font('cinzel600', 46), GOLD, TR(0.12)), W / 2, 70, ease(t / .8))
    return fr

def f_counter(spec, t, D):
    fr = bg(spec.get('seed', 91)); k = ease(t / (D * .55)); v = _lerp(spec.get('from', 0), spec['to'], k)
    txt = f"{int(round(v)):,}".replace(',', '.')
    put(fr, text_layer(spec.get('prefix', '') + txt, font('cinzel600', 200), GOLD, TR(0.04)), W / 2, H / 2 - 50, ease(t / .5))
    put(fr, rule_layer(420), W / 2, H / 2 + 80, ease((t - .4) / .8))
    put(fr, text_layer(spec.get('label', ''), font('corm500i', 60), CREAM), W / 2, H / 2 + 150, ease((t - .6) / .8))
    return fr

def f_split(spec, t, D):
    fr = bg(spec.get('seed', 95)); d = ImageDraw.Draw(fr); k = ease((t - .2) / .8)
    d.line([(W / 2, H / 2 - 380 * k), (W / 2, H / 2 + 380 * k)], fill=GOLD, width=2)
    for side, cx, col in (('left', W / 4, DIM), ('right', 3 * W / 4, GOLD)):
        s_ = spec[side]; at = .4 if side == 'left' else D * .4
        put(fr, text_layer(CASE(s_['title']), font('cinzel600', 44), col, TR(0.12)), cx, 260, ease((t - at) / .7))
        y = 360
        for i, l in enumerate(s_.get('lines', [])):
            for ww in wrap(l, font('corm500', 44), 700):
                put(fr, text_layer(ww, font('corm500', 44), CREAM if side == 'right' else DIM), cx, y, ease((t - at - .4 - i * .5) / .6)); y += 58
            y += 24
        if side == 'left' and spec.get('strike', True) and t > D * .4:
            kk = ease((t - D * .4) / .4)
            if kk > 0: d.line([(cx - 330, 330), (cx - 330 + 660 * kk, 330 + (y - 360) * kk)], fill=RED + (200,), width=5)
    return fr

KIND.update(mapfly=f_mapfly, scan=f_scan, doc=f_doc, board=f_board, counter=f_counter, split=f_split)


# ---------- v3: accesibilidad y grafismo explicativo ----------
def _photo(spec, w, h, bw=True):
    """Foto real recortada a w×h (en B/N por defecto), con marco fino; None si no hay."""
    from PIL import ImageOps
    p = spec.get('_path')
    if not p or not os.path.exists(p): return None
    im = ImageOps.fit(Image.open(p).convert('L' if bw else 'RGB'), (w, h), centering=(0.5, 0.3))
    im = im.convert('RGBA'); d = ImageDraw.Draw(im); d.rectangle([0, 0, w - 1, h - 1], outline=GOLD + (160,), width=2)
    return im

def _col(c, default=None): return tuple(int(x) for x in c) if c else (default or GOLD)

def f_ficha_v3(spec, t, D):
    """Ficha con foto real: retrato a la izquierda, nombre, cargo y grupo a la derecha."""
    if not spec.get('_path'): return f_ficha(spec, t, D)
    fr = bg(spec.get('seed', 13)); ph = _photo(spec, 560, 700); k = ease(t / .9)
    put(fr, ph, 540, H / 2 + int(20 * (1 - k)), k)
    col = _col(spec.get('color')); d = ImageDraw.Draw(fr)
    if spec.get('color') and k > .2: d.rectangle([900, H / 2 - 140, 908, H / 2 + 160], fill=col)
    nm = CASE(spec['name']); MAXW = W - 940 - 90
    put(fr, text_layer(nm, fit('cinzel600', 92, nm, MAXW, TR(0.08)), GOLD, TR(0.08)), 940, H / 2 - 80, ease((t - .3) / .8), anchor='lt')
    fr_ = font('corm500i', 50); rl = wrap(spec.get('role', ''), fr_, MAXW)
    if len(rl) > 2: fr_ = font('corm500i', 42); rl = wrap(spec.get('role', ''), fr_, MAXW)[:3]
    y = H / 2 + 30
    for ln in rl: put(fr, text_layer(ln, fit('corm500i', fr_.size, ln, MAXW), CREAM), 942, y, ease((t - .7) / .8), anchor='lt'); y += int(fr_.size * 1.25)
    if spec.get('group'):
        g = CASE(spec['group']); put(fr, text_layer(g, fit('cinzel400', 34, g, MAXW, TR(0.14)), col, TR(0.14)), 942, y + 18, ease((t - 1.0) / .8), anchor='lt')
    return fr

def f_cast(spec, t, D):
    """Tablero de protagonistas agrupados por bando: foto, nombre y papel. Entran escalonados."""
    fr = bg(spec.get('seed', 17)); groups = spec['groups']
    if spec.get('title'): put(fr, text_layer(CASE(spec['title']), font('cinzel600', 54), GOLD, TR(0.12)), W / 2, 92, ease(t / .8))
    tot = sum(len(g['people']) for g in groups); step = min(.55, (D * .55) / max(1, tot)); idx = 0
    gw = (W - 160) / len(groups); d = ImageDraw.Draw(fr)
    def layout(n):
        cols = n if (gw - 40) / max(1, n) - 24 >= 150 else max(1, int((gw - 40) // 174)); return cols, math.ceil(n / cols)
    maxrows = max(layout(len(g['people']))[1] for g in groups)
    for gi, g in enumerate(groups):
        x0 = 80 + gi * gw; col = _col(g.get('color')); kg = ease((t - .2 - gi * .25) / .7)
        if kg > 0:
            d.rectangle([x0 + 20, 170, x0 + 20 + (gw - 40) * kg, 176], fill=col)
            put(fr, text_layer(CASE(g['name']), font('cinzel600', 40), col, TR(0.12)), x0 + gw / 2, 215, kg)
        ppl = g['people']; n = len(ppl); cols, rows = layout(n)
        pw = min(220, (gw - 40) / cols - 24, (H - 420) / maxrows / 1.2 - 100 / 1.2); phh = int(pw * 1.2); rh = phh + 120
        for j, pe in enumerate(ppl):
            r, c = divmod(j, cols); cx = x0 + gw / 2 + (c - (min(cols, n - r * cols) - 1) / 2) * (pw + 34)
            cy = 270 + r * rh + max(0, (H - 300 - maxrows * rh) / 2)
            k = ease((t - .6 - idx * step) / .6); idx += 1
            if k <= 0: continue
            ph = _photo(pe, int(pw), phh)
            if ph is None:
                ph = Image.new('RGBA', (int(pw), phh), (40, 40, 40, 255)); ImageDraw.Draw(ph).rectangle([0, 0, int(pw) - 1, phh - 1], outline=col + (200,), width=2)
            put(fr, ph, cx, cy + phh / 2 + int(16 * (1 - k)), k)
            dd = ImageDraw.Draw(fr); dd.rectangle([cx - pw / 2, cy + phh + 2, cx + pw / 2, cy + phh + 7], fill=col)
            fn = font('cinzel600', 28); nl = wrap(pe['name'], fn, pw + 22)[:3]
            for li, ln in enumerate(nl): put(fr, text_layer(ln, fit('cinzel600', 28, ln, pw + 26), CREAM), cx, cy + phh + 32 + li * 32, k)
            if pe.get('role'):
                for li, ln in enumerate(wrap(pe['role'], font('corm500i', 24), pw + 22)[:2]):
                    put(fr, text_layer(ln, font('corm500i', 24), DIM), cx, cy + phh + 36 + len(nl) * 32 + li * 28, k)
    return fr

def f_seats(spec, t, D):
    """Hemiciclo: los escaños se colorean por grupo, con la cifra que se cuenta y la línea de mayoría."""
    fr = bg(spec.get('seed', 19)); d = ImageDraw.Draw(fr); total = spec['total']; parties = spec['parties']
    if spec.get('title'): put(fr, text_layer(CASE(spec['title']), font('cinzel600', 54), GOLD, TR(0.12)), W / 2, 80, ease(t / .8))
    rows = max(6, int(math.sqrt(total / 3.2))); cx, cy = W / 2, H - 250; R0, R1 = 260, 640
    radii = [R0 + (R1 - R0) * r / (rows - 1) for r in range(rows)]; tot_len = sum(radii)
    per = [max(1, round(total * rr / tot_len)) for rr in radii]; per[-1] += total - sum(per)
    pts = []
    for rr, n in zip(radii, per):
        for j in range(n): a = math.pi * (1 - j / max(1, n - 1)); pts.append((a, cx + rr * math.cos(a), cy - rr * math.sin(a)))
    pts.sort(key=lambda p: -p[0])
    colors = []
    for pa in parties: colors += [_col(pa.get('color'))] * pa['seats']
    colors += [(70, 70, 70)] * (total - len(colors))
    p = ease((t - .5) / (D * .5)); shown = int(total * p); rad = max(4, int((R1 - R0) / (rows - 1) * 0.40))
    for i, (_, x, y) in enumerate(pts):
        c = colors[i] if i < shown else (55, 52, 48)
        d.ellipse([x - rad, y - rad, x + rad, y + rad], fill=c)
    if spec.get('majority'):
        k = ease((t - D * .55) / .6)
        if k > 0:
            d.line([(cx, cy - R1 - 20), (cx, cy - R0 + 20)], fill=CREAM + (int(255 * k),), width=3)
            put(fr, text_layer(f"MAYORÍA: {spec['majority']}", font('cinzel400', 30), CREAM, TR(0.14)), cx, cy - 110, k)
    x = 140
    for i, pa in enumerate(parties):
        k = ease((t - .8 - i * .35) / .6)
        if k <= 0: continue
        v = int(round(pa['seats'] * min(1, p * 1.05)))
        put(fr, text_layer(str(v), font('cinzel600', 96), _col(pa.get('color')), TR(0.04)), x, H - 170, k, anchor='lt')
        put(fr, text_layer(pa['name'], font('corm500i', 40), CREAM), x, H - 70, k, anchor='lt')
        x += 520
    return fr

def f_versus(spec, t, D):
    """Dos bandos frente a frente: foto del líder, nombre del bloque y quiénes lo forman."""
    fr = bg(spec.get('seed', 23)); d = ImageDraw.Draw(fr); k0 = ease((t - .1) / .7)
    d.line([(W / 2, H / 2 - 400 * k0), (W / 2, H / 2 + 400 * k0)], fill=GOLD, width=2)
    if spec.get('title'): put(fr, text_layer(CASE(spec['title']), font('cinzel600', 44), GOLD, TR(0.12)), W / 2, 70, ease(t / .8))
    for side, cx in (('left', W / 4), ('right', 3 * W / 4)):
        s_ = spec[side]; col = _col(s_.get('color')); at = .3 if side == 'left' else .9; k = ease((t - at) / .7)
        ph = _photo(s_, 340, 400)
        if ph is not None: put(fr, ph, cx, 340 + int(20 * (1 - k)), k)
        put(fr, text_layer(CASE(s_['name']), fit('cinzel600', 56, CASE(s_['name']), 760, TR(0.08)), col, TR(0.08)), cx, 590, k)
        if k > 0: d.rectangle([cx - 160 * k, 632, cx + 160 * k, 637], fill=col)
        y = 690
        for i, l in enumerate(s_.get('lines', [])):
            kk = ease((t - at - .5 - i * .35) / .6)
            for ww in wrap(l, font('corm500', 40), 760): put(fr, text_layer(ww, font('corm500', 40), CREAM), cx, y, kk); y += 52
    return fr

def f_recap(spec, t, D):
    """Recapitulación: puntos numerados que entran uno a uno (quién es quién y dónde estamos)."""
    fr = bg(spec.get('seed', 29)); items = spec['items']; n = len(items)
    put(fr, text_layer(CASE(spec.get('title', 'Hasta aquí')), font('cinzel600', 56), GOLD, TR(0.12)), W / 2, 150, ease(t / .8))
    put(fr, rule_layer(320), W / 2, 210, ease((t - .3) / .8))
    step = min(1.2, (D * .65) / max(1, n)); gap = min(150, 700 / n); y0 = 300
    for i, it in enumerate(items):
        a, b = (it if isinstance(it, (list, tuple)) else (it, None)); k = ease((t - .7 - i * step) / .6)
        y = y0 + i * gap
        put(fr, text_layer(f'{i + 1}', font('cinzel600', 70), GOLD), 360, y, k)
        put(fr, text_layer(a, fit('cinzel600', 48, a, W - 560), CREAM), 450, y - (14 if b else 0), k, anchor='lm')
        if b: put(fr, text_layer(b, fit('corm500i', 36, b, W - 560), DIM), 452, y + 34, k, anchor='lm')
    return fr

KIND.update(ficha=f_ficha_v3, cast=f_cast, seats=f_seats, versus=f_versus, recap=f_recap)

def gloss(term, meaning, out, color=None):
    """Chip de glosario arriba a la izquierda: sigla o término y su traducción a lenguaje de hoy."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); MAXW = 1000; f1 = fit('cinzel600', 44, CASE(term), MAXW, TR(0.08)); f2 = font('corm500i', 36)
    ml = wrap(meaning, f2, MAXW)[:2]; d0 = ImageDraw.Draw(im); w1 = d0.textlength(CASE(term), font=f1)
    w2 = max([d0.textlength(l, font=f2) for l in ml] or [0]); bw = int(max(w1, w2) + 90); bh = 150 + 46 * (len(ml) - 1)
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    gd.rectangle([60, 60, 60 + bw, 60 + bh], fill=(0, 0, 0, 170)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(6)))
    d = ImageDraw.Draw(im); d.rectangle([60, 60, 68, 60 + bh], fill=tuple(color) if color else GOLD)
    im.alpha_composite(text_layer(CASE(term), f1, GOLD, TR(0.08)), (96, 74))
    for i, l in enumerate(ml): im.alpha_composite(text_layer(l, f2, CREAM), (98, 140 + i * 46))
    im.save(out)

def keyword(word, out):
    """Palabra clave a pantalla completa (capa transparente) para superponer sobre un plano."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g); gd.rectangle([0, H / 2 - 160, W, H / 2 + 160], fill=(0, 0, 0, 120))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(60)))
    L = text_layer(CASE(word), fit('cinzel600', 150, CASE(word), 1700, TR(0.18)), GOLD, TR(0.18)); im.alpha_composite(L, ((W - L.width) // 2, (H - L.height) // 2))
    im.save(out)

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

def lower_third(a, b, out, color=None):
    """Rótulo inferior. `color`: color del bando o grupo (barra vertical), para reconocerlo en todo el episodio."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
    gd.rectangle([0, H - 260, 1100, H - 90], fill=(0, 0, 0, 150)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))
    d = ImageDraw.Draw(im); d.line([(144, H - 205), (214, H - 205)], fill=GOLD, width=3)
    if color: d.rectangle([104, H - 212, 112, H - 100], fill=tuple(color))
    if THEME.get('brand_dot', True): d.ellipse([122, H - 211, 134, H - 199], fill=BRAND_DOT)  # firma DocuVox: el punto
    im.alpha_composite(text_layer(CASE(a), fit('cinzel600', 52, CASE(a), W - 300, TR(0.10)), GOLD, TR(0.10)), (142, H - 200))
    if b: im.alpha_composite(text_layer(b, fit('corm500i', 40, b, W - 300), CREAM), (144, H - 138))
    im.save(out)

def end_screen(out, bg_path=None, kit=None):
    """Pantalla final DocuVox (fondo para los elementos de YouTube): imagen del propio episodio en B/N, marca y huecos."""
    kit = kit or os.path.join(os.path.dirname(HERE), 'assets', 'brand')
    fr = Image.new('RGB', (W, H), (16, 16, 16))
    if bg_path and os.path.exists(bg_path):
        from PIL import ImageOps, ImageEnhance
        b = ImageOps.fit(Image.open(bg_path).convert('L'), (W, H)).filter(ImageFilter.GaussianBlur(6))
        fr = ImageEnhance.Brightness(b.convert('RGB')).enhance(0.32)
    fr = fr.convert('RGBA'); d = ImageDraw.Draw(fr)
    yy, xx = np.mgrid[0:H, 0:W]; v = np.clip(1 - 0.6 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0.3, 1)
    arr = np.asarray(fr).astype(np.float32); arr[..., :3] *= v[..., None]; fr = Image.fromarray(arr.clip(0, 255).astype('uint8'), 'RGBA'); d = ImageDraw.Draw(fr)
    logo = Image.open(f'{kit}/DocuVox_Logo_Horizontal_Amarillo-Blanco.png').convert('RGBA'); logo = logo.resize((300, int(300 * logo.height / logo.width)), Image.LANCZOS)
    fr.alpha_composite(logo, (96, 64))
    bf = lambda n, s: ImageFont.truetype(f'{kit}/{n}.ttf', s)
    d.line([(96 + 320, 72), (96 + 320, 64 + logo.height - 8)], fill=(139, 139, 133), width=2)
    d.text((96 + 340, 64 + logo.height / 2), 'DOCUMENTALES SONOROS', font=bf('BarlowCondensed-SemiBold', 26), fill=(244, 243, 238), anchor='lm')
    for x, lab in ((96, 'SIGUE ESCUCHANDO'), (1000, 'RECOMENDADO')):
        d.text((x, 262), lab, font=bf('BarlowCondensed-ExtraBold', 30), fill=BRAND_DOT, anchor='ls')
        d.rectangle([x, 280, x + 824, 280 + 463], outline=(139, 139, 133, 140), width=2)
    d.ellipse([760, 850, 900, 990], outline=(139, 139, 133, 160), width=2)
    d.text((930, 905), 'SUSCRÍBETE', font=bf('BarlowCondensed-Black', 54), fill=(244, 243, 238), anchor='lm')
    f2 = bf('BarlowCondensed-Black', 54); x = 930
    for w_, c_ in (('Y ', (244, 243, 238)), ('ESCUCHA', BRAND_DOT), (' MÁS.', (244, 243, 238))):
        d.text((x, 962), w_, font=f2, fill=c_, anchor='lm'); x += d.textlength(w_, font=f2)
    fr.convert('RGB').save(out, quality=95)

# ---------- e29n90: piel de plataforma (la entrevista) ----------
def _flat(seed=5):
    """Negro plano con grano fino: el fondo de la entrevista."""
    k = ('flat', seed)
    if k not in _bgcache:
        rng = np.random.default_rng(seed); base = np.array(BG0, np.float32)
        rgb = np.clip(base + rng.normal(0, 2.4, (H, W, 1)).astype(np.float32), 0, 255)
        _bgcache[k] = Image.fromarray(rgb.astype('uint8')).convert('RGBA')
    return _bgcache[k].copy()

def f_pregunta(spec, t, D):
    """LA PREGUNTA: número arriba en mono, la pregunta se teclea letra a letra con cursor; nada más en pantalla."""
    fr = _flat(spec.get('seed', 5)); q = spec['text']; cps = spec.get('cps', 16)
    hdr = spec.get('n', '')
    if hdr: put(fr, text_layer(hdr, font('display_light', 30), DIM, 0.12), 160, 150, ease(t / .5), anchor='lm')
    f = font('cinzel600', spec.get('size', 84)); lines = wrap(q, f, 1600); n = int(max(0, t - .35) * cps)
    y0 = H / 2 - (len(lines) * 112) / 2; shown = 0; cur = None
    for i, l in enumerate(lines):
        vis = l[:max(0, n - shown)]; shown += len(l) + 1
        if vis: put(fr, text_layer(vis, f, CREAM), 160, y0 + i * 112, 1, anchor='lm')
        if len(vis) < len(l) and cur is None: cur = (i, vis)
    if cur is None: cur = (len(lines) - 1, lines[-1])
    if (int(t * 2.2) % 2 == 0) or n < sum(len(l) + 1 for l in lines):
        d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); cx = 160 + d0.textlength(cur[1], font=f) + 14
        ImageDraw.Draw(fr).rectangle([cx, y0 + cur[0] * 112 - 44, cx + 22, y0 + cur[0] * 112 + 46], fill=CREAM)
    if spec.get('foot'): put(fr, text_layer(spec['foot'], font('display_light', 26), DIM, 0.12), 160, H - 140, ease((t - .3) / .6), anchor='lm')
    return fr

def f_aviso(spec, t, D):
    """Aviso legal sobrio: líneas cortas en mono, centradas, sobre negro."""
    fr = _flat(spec.get('seed', 6)); f = font('display_light', spec.get('size', 38)); lh = int(f.size * 1.6)
    lines = [l for x in spec['lines'] for l in wrap(x, f, 1500)]; y0 = H / 2 - len(lines) * lh / 2
    for i, l in enumerate(lines): put(fr, text_layer(l, f, CREAM if i == 0 and spec.get('head') else DIM), W / 2, y0 + i * lh, ease((t - .2 - i * .15) / .6))
    return fr

def f_dijo(spec, t, D):
    """LO QUE DIJO / LO QUE PASÓ: dos columnas sobre negro, fecha en mono, la segunda entra a mitad."""
    fr = _flat(spec.get('seed', 7)); d = ImageDraw.Draw(fr); k = ease((t - .1) / .6)
    d.line([(W / 2, H / 2 - 360 * k), (W / 2, H / 2 + 360 * k)], fill=CREAM + (255,), width=2)
    for side, x0, at in (('left', 140, .2), ('right', W / 2 + 100, D * .45)):
        s_ = spec[side]; a = ease((t - at) / .6)
        put(fr, text_layer(s_.get('label', 'LO QUE DIJO' if side == 'left' else 'LO QUE PASÓ'), font('display_light', 30), DIM, 0.14), x0, 250, a, anchor='lm')
        put(fr, text_layer(s_.get('date', ''), font('display_light', 34), RED if (side == 'right' and spec.get('red')) else CREAM, 0.06), x0, 305, a, anchor='lm')
        y = 400; fz = font('cinzel600', s_.get('size', 54))
        for ww in wrap(s_['text'], fz, 760): put(fr, text_layer(ww, fz, CREAM), x0, y, a, anchor='lm'); y += int(fz.size * 1.25)
        if s_.get('source'): put(fr, text_layer(s_['source'], font('display_light', 26), DIM, 0.08), x0, H - 200, a, anchor='lm')
    return fr

KIND.update(pregunta=f_pregunta, aviso=f_aviso, dijo=f_dijo)
