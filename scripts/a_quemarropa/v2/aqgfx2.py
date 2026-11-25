"""Grafismo v2 de «A quemarropa» (DocuVox): tipografía editorial (Inter Display / Inter / Crimson Text),
márgenes amplios, amarillo DocuVox solo como acento, rótulos arriba a la izquierda para no tapar subtítulos nativos."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import re, json, os
W, H = 1920, 1080
YEL = (0xF2, 0xFF, 0x00); WHITE = (255, 255, 255); BLACK = (0, 0, 0)
INK = (14, 15, 17); GREY = (160, 164, 170); LIGHT = (225, 227, 230)
MX = 150
FD = '/usr/share/fonts/opentype/inter/'; CR = '/usr/share/fonts/truetype/google-fonts/ofl/crimsontext/'
FILES = {'disp_b': FD + 'InterDisplay-Bold.otf', 'disp_sb': FD + 'InterDisplay-SemiBold.otf', 'disp_xb': FD + 'InterDisplay-ExtraBold.otf',
         'disp_m': FD + 'InterDisplay-Medium.otf', 'body': FD + 'Inter-Regular.otf', 'body_m': FD + 'Inter-Medium.otf', 'body_sb': FD + 'Inter-SemiBold.otf',
         'quote': CR + 'CrimsonText-Italic.ttf', 'quote_sb': CR + 'CrimsonText-SemiBoldItalic.ttf'}
def SAN(t):
    if not isinstance(t, str): return t
    t = t.replace('✕', '×').replace('✓', '✔')
    t = re.sub(r'\bSEÑAL:\s*', '', t)
    return t
_otext = ImageDraw.ImageDraw.text; _olen = ImageDraw.ImageDraw.textlength
ImageDraw.ImageDraw.text = lambda self, xy, text, *a, **k: _otext(self, xy, SAN(text), *a, **k)
ImageDraw.ImageDraw.textlength = lambda self, text, *a, **k: _olen(self, SAN(text), *a, **k)
_F = {}
def F(w, s):
    if (w, s) not in _F: _F[(w, s)] = ImageFont.truetype(FILES[w], s)
    return _F[(w, s)]
def canvas(bg=None): return Image.new('RGBA', (W, H), (0, 0, 0, 0) if bg is None else tuple(bg) + (255,))
def bgcard():
    """fondo de tarjeta: negro tinta con viñeta suave"""
    im = Image.new('RGBA', (W, H), INK + (255,))
    g = Image.new('L', (W, H), 0); d = ImageDraw.Draw(g)
    for i in range(30):
        a = int(70 * (i / 30) ** 2); d.rectangle((i * 22, i * 12, W - i * 22, H - i * 12), outline=None, fill=a)
    glow = Image.new('RGBA', (W, H), (28, 30, 34, 255)); im = Image.composite(glow, im, g.filter(ImageFilter.GaussianBlur(120)))
    return im
def wrap(d, text, f, maxw):
    out = []
    for para in SAN(text).split('\n'):
        cur = ''
        for w in para.split():
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=f) <= maxw or not cur: cur = t
            else: out.append(cur); cur = w
        if cur: out.append(cur)
    return out
def fit(d, text, w, sizes, maxw, maxlines):
    for s in sizes:
        L = wrap(d, text, F(w, s), maxw)
        if len(L) <= maxlines: return s, L
    s = sizes[-1]; return s, wrap(d, text, F(w, s), maxw)
def spaced(d, xy, text, f, fill, track=3):
    x, y = xy
    for ch in SAN(text):
        d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track
    return x
def spaced_len(d, text, f, track=3): return sum(d.textlength(c, font=f) + track for c in SAN(text))
def kicker(d, x, y, text, col=YEL, size=30):
    f = F('body_sb', size); spaced(d, (x, y), text.upper(), f, col, 4); return y + int(size * 1.6)
def rule(d, x, y, w=120, col=YEL, th=4): d.rectangle((x, y, x + w, y + th), fill=col)

# ------------------------------------------------------------------ rótulos sobre imagen (arriba a la izquierda)
def r1(line1, line2='', tag=None):
    """Rótulo de persona / fuente: arriba a la izquierda, sobre degradado. tag = DIJO / HIZO."""
    im = canvas(); d = ImageDraw.Draw(im)
    grad = Image.new('L', (W, 330), 0); gd = ImageDraw.Draw(grad)
    for y in range(330): gd.line((0, y, W, y), fill=int(170 * (1 - y / 330) ** 1.6))
    im.paste(Image.new('RGBA', (W, 330), (0, 0, 0, 255)), (0, 0), grad)
    x, y = 96, 70
    if tag:
        f = F('disp_xb', 40); tw = spaced_len(d, tag, f, 5) + 40
        col = YEL if tag == 'HIZO' else WHITE
        d.rectangle((x, y, x + tw, y + 62), fill=col); spaced(d, (x + 20, y + 8), tag, f, BLACK, 5); x2 = x + tw + 24
    else: x2 = x
    s1, L1 = fit(d, line1.upper(), 'disp_b', [56, 50, 46], W - x2 - 200, 2)
    yy = y
    for l in L1: d.text((x2, yy), l, font=F('disp_b', s1), fill=WHITE); yy += int(s1 * 1.12)
    if line2:
        L2 = wrap(d, line2, F('body_m', 38), W - x2 - 200)[:2]
        rule(d, x2, yy + 10, 60, YEL, 3); yy += 24
        for l in L2: d.text((x2, yy), l, font=F('body_m', 38), fill=LIGHT); yy += 48
    return im
def pie(text):
    """Fuente de captura o de plano: etiqueta arriba a la izquierda."""
    return r1(text.split(' · ')[0], ' · '.join(text.split(' · ')[1:])) if ' · ' in text else r1(text, '')
def subt(text):
    """Subtítulo: Inter SemiBold 50, caja negra 75 %, abajo centrado (sobre la franja si la hay)."""
    im = canvas(); d = ImageDraw.Draw(im); f = F('body_sb', 50)
    L = wrap(d, text, f, 1500)[:3]; lh = 64; y0 = H - 70 - lh * len(L)
    for i, l in enumerate(L):
        tw = d.textlength(l, font=f); x = (W - tw) / 2; y = y0 + i * lh
        d.rectangle((x - 18, y - 4, x + tw + 18, y + lh - 4), fill=(0, 0, 0, 190))
        d.text((x, y), l, font=f, fill=WHITE)
    return im
def cover(box):
    im = canvas(); ImageDraw.Draw(im).rectangle(box, fill=(0, 0, 0, 255)); return im

# ------------------------------------------------------------------ tarjetas a pantalla completa
LABEL_COL = {'CONDENAD': ((0xC6, 0x28, 0x28), WHITE), 'INVESTIGAD': ((0xE8, 0xA3, 0x17), BLACK), 'SIN PRUEBA': ((0x6B, 0x6F, 0x76), WHITE),
             'ACUSACIÓN': ((0x8E, 0x44, 0xAD), WHITE), 'INDICIO': ((0x2E, 0x86, 0xC1), WHITE), 'PUBLICADO': ((0x5D, 0x6D, 0x7E), WHITE), 'DATO': (YEL, BLACK)}
def label_colors(label):
    u = label.upper()
    for k, v in LABEL_COL.items():
        if k in u: return v
    return (WHITE, BLACK)
def _body_block(d, x, y, text, maxw, sizes=(64, 58, 52, 46, 42), lines=6, font='disp_sb', col=WHITE, lh=1.22):
    s, L = fit(d, text, font, list(sizes), maxw, lines)
    for l in L: d.text((x, y), l, font=F(font, s), fill=col); y += int(s * lh)
    return y
def t1(label, text):
    """Tarjeta con etiqueta de estado (CONDENADO, INVESTIGADO, SIN PRUEBA…)."""
    im = bgcard(); d = ImageDraw.Draw(im); bg, fg = label_colors(label)
    f = F('disp_xb', 44 if text else 64); tw = spaced_len(d, label.upper(), f, 5) + 56; hh = 80 if text else 110
    y0 = 300 if text else (H - hh) // 2
    d.rectangle((MX, y0, MX + tw, y0 + hh), fill=bg); spaced(d, (MX + 28, y0 + (hh - f.size) // 2 - 6), label.upper(), f, fg, 5)
    if text: _body_block(d, MX, y0 + hh + 60, text, W - 2 * MX - 100)
    return im
def t2(text, bg=None, kick=None):
    """Tarjeta de dato o aviso: kicker opcional, texto editorial, fuente separada si viene tras «\\n»."""
    im = bgcard(); d = ImageDraw.Draw(im)
    parts = text.split('\n'); main = parts[0]; src = ' '.join(parts[1:])
    m = re.match(r'^([A-ZÁÉÍÓÚÑ0-9/ ]{3,24}) · (.*)$', main)
    if m and not kick: kick, main = m.group(1), m.group(2)
    tmp = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    s, L = fit(tmp, main, 'disp_sb', [66, 60, 54, 48, 44], W - 2 * MX - 120, 6)
    hblock = (60 if kick else 0) + len(L) * int(s * 1.22) + (80 if src else 0)
    y = max(140, (H - hblock) // 2)
    if kick: y = kicker(d, MX, y, kick)
    for l in L: d.text((MX, y), l, font=F('disp_sb', s), fill=WHITE); y += int(s * 1.22)
    if src:
        rule(d, MX, y + 24, 80, YEL, 3); d.text((MX, y + 44), src, font=F('body_m', 32), fill=GREY)
    return im
def q1(quote, source='', bg=None, kick=None):
    """Cita literal: Crimson Text cursiva, comilla amarilla grande, fuente debajo; fondo = fotograma del protagonista oscurecido."""
    if bg is not None:
        im = bg.convert('RGBA').resize((W, H)).filter(ImageFilter.GaussianBlur(14))
        im = Image.alpha_composite(im, Image.new('RGBA', (W, H), INK + (205,)))
    else: im = bgcard()
    d = ImageDraw.Draw(im)
    q = quote.strip()
    q = re.sub(r'^[«"]\s*', '', q); q = re.sub(r'\s*[»"]$', '', q)
    s, L = fit(d, q, 'quote', [76, 70, 64, 58, 52, 46, 42], W - 2 * MX - 160, 9)
    lh = int(s * 1.25); hblock = len(L) * lh + (100 if source else 0) + (60 if kick else 0)
    y = max(120, (H - hblock) // 2)
    if kick: y = kicker(d, MX + 120, y, kick)
    d.text((MX, y - 40), '«', font=F('quote_sb', 190), fill=YEL)
    for i, l in enumerate(L):
        d.text((MX + 120, y), l + ('»' if i == len(L) - 1 else ''), font=F('quote', s), fill=WHITE); y += lh
    if source:
        rule(d, MX + 120, y + 26, 80, YEL, 3); d.text((MX + 120, y + 46), source, font=F('body_m', 32), fill=LIGHT)
    return im
def d1(big, label=''):
    """Cifra grande."""
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, big, 'disp_xb', [240, 200, 170, 140, 120, 100], W - 2 * MX, 2)
    hb = len(L) * int(s * 1.0) + (130 if label else 0); y = (H - hb) // 2 - 20
    for l in L: d.text((MX, y), l, font=F('disp_xb', s), fill=YEL); y += int(s * 1.0)
    if label: rule(d, MX, y + 30, 120, WHITE, 3); _body_block(d, MX, y + 60, label, W - 2 * MX, (52, 46, 42), 2, 'disp_m', LIGHT)
    return im
def n1(word, yellow=False):
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, word, 'disp_b', [120, 104, 92, 80, 70], W - 2 * MX, 3)
    y = (H - len(L) * int(s * 1.1)) // 2
    for l in L:
        tw = d.textlength(l, font=F('disp_b', s)); d.text(((W - tw) / 2, y), l, font=F('disp_b', s), fill=YEL if yellow else WHITE); y += int(s * 1.1)
    return im
def x1(num, title, sub=''):
    """Cabecera de expediente."""
    im = bgcard(); d = ImageDraw.Draw(im)
    y = 360; kicker(d, MX, y, f'EXPEDIENTE {int(num):02d}' if str(num).isdigit() else str(num), YEL, 34)
    s, L = fit(d, title.upper(), 'disp_xb', [118, 104, 92, 80], W - 2 * MX, 2); y += 70
    for l in L: d.text((MX, y), l, font=F('disp_xb', s), fill=WHITE); y += int(s * 1.05)
    if sub: rule(d, MX, y + 30, 120, YEL, 4); d.text((MX, y + 60), sub, font=F('disp_m', 44), fill=LIGHT)
    return im
def x0(title):
    return n1(title)
def p1(q):
    im = bgcard(); d = ImageDraw.Draw(im); y = 330; y = kicker(d, MX, y, 'LA PREGUNTA')
    _body_block(d, MX, y + 20, q, W - 2 * MX - 100, (84, 76, 68, 60), 4, 'disp_b'); return im
def k1(num, rest):
    im = bgcard(); d = ImageDraw.Draw(im); y = 330
    kicker(d, MX, y, 'PERDÓN'); d.text((MX, y + 50), f'N.º {num}', font=F('disp_xb', 150), fill=YEL)
    if rest: _body_block(d, MX, y + 240, rest, W - 2 * MX - 100, (52, 46, 42), 4, 'disp_m', LIGHT)
    return im
def z1(text):
    im = bgcard(); d = ImageDraw.Draw(im); _body_block(d, MX, 380, text, W - 2 * MX, (54, 48, 44), 6, 'disp_m', LIGHT); return im
def r2(names, dim=()):
    """Lista de personas con su estado procesal."""
    im = bgcard(); d = ImageDraw.Draw(im); n = len(names)
    lh = min(150, 760 // max(n, 1)); y = (H - lh * n) // 2
    for i, (nm, st) in enumerate(names):
        col = (110, 110, 110) if i in dim else WHITE
        d.text((MX, y), nm.upper(), font=F('disp_b', min(64, lh - 40)), fill=col)
        if st:
            bg, fg = label_colors(st); f = F('body_sb', 28); tw = spaced_len(d, st.upper(), f, 3) + 30
            d.rectangle((MX, y + min(64, lh - 40) + 14, MX + tw, y + min(64, lh - 40) + 56), fill=bg); spaced(d, (MX + 15, y + min(64, lh - 40) + 18), st.upper(), f, fg, 3)
        y += lh
    return im
def l1(items, upto=None):
    """Cronología horizontal; upto = cuántos hitos se ven (para animarla por pasos)."""
    im = bgcard(); d = ImageDraw.Draw(im); n = max(1, len(items)); upto = n if upto is None else upto
    x0_, x1_ = MX, W - MX; y0 = 520; cw = (x1_ - x0_) / n
    d.line((x0_, y0, x1_, y0), fill=(70, 74, 80), width=4)
    for i, (fe, hi) in enumerate(items):
        x = x0_ + cw * (i + 0.5); on = i < upto
        if on: d.line((x0_ if i == 0 else x0_ + cw * (i - 0.5), y0, x, y0), fill=YEL, width=4)
        d.ellipse((x - 14, y0 - 14, x + 14, y0 + 14), fill=YEL if on else (70, 74, 80))
        if not on: continue
        f = F('disp_b', 52 if n <= 4 else 44); fw = d.textlength(fe, font=f)
        d.text((x - fw / 2, y0 - 100), fe, font=f, fill=YEL)
        fb = F('body_m', 36 if n <= 4 else 32); L = wrap(d, hi, fb, cw - 36)[:4]; yy = y0 + 46
        for l in L:
            lw = d.textlength(l, font=fb); d.text((x - lw / 2, yy), l, font=fb, fill=WHITE); yy += int(fb.size * 1.3)
    return im
# --- mapa real (Natural Earth)
GEO = '/home/claude/w/aq/geo/countries.geojson'
import math
PLACES = {'MELILLA': ((-2.94, 35.29), (-3.6, 36.3), 4.4), 'CEUTA': ((-5.32, 35.89), (-4.6, 36.4), 4.4),
          'ADAMUZ': ((-4.52, 38.03), (-3.7, 39.9), 10.5), 'URDA': ((-3.72, 39.41), (-3.7, 39.9), 10.5)}
def m1(place, sub='', lonlat=None, center=None, span=None):
    key = place.upper().split()[0]
    if key in PLACES and lonlat is None: lonlat, center, span = PLACES[key]
    center = center or (-3.7, 39.9); span = span or 10.5
    k = math.cos(math.radians(center[1])); lon_span = span * (W / H) / k
    box = (center[0] - lon_span / 2, center[1] - span / 2, center[0] + lon_span / 2, center[1] + span / 2)
    def P(lo, la): return ((lo - box[0]) / (box[2] - box[0]) * W, (box[3] - la) / (box[3] - box[1]) * H)
    im = Image.new('RGBA', (W, H), (16, 24, 32, 255)); d = ImageDraw.Draw(im)
    try:
        G = json.load(open(GEO))
        for ft in G['features']:
            name = ft['properties'].get('ADMIN', ''); geom = ft['geometry']
            polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
            fill = (78, 84, 92, 255) if name == 'Spain' else (48, 52, 58, 255)
            for poly in polys:
                pts = [P(lo, la) for lo, la in poly[0]]
                if len(pts) > 2: d.polygon(pts, fill=fill, outline=(100, 105, 112, 255))
    except Exception as e: print('mapa sin geojson', e)
    if lonlat:
        x, y = P(*lonlat)
        for r, a in ((46, 50), (28, 110), (13, 255)): d.ellipse((x - r, y - r, x + r, y + r), fill=YEL + (a,))
        f = F('disp_xb', 92); fs = F('disp_m', 46)
        tw = max(d.textlength(place.upper(), font=f), d.textlength(sub, font=fs) if sub else 0)
        tx = x + 70 if x + 70 + tw < W - 80 else x - 70 - tw
        ty = y - 130 if y > 260 else y + 50
        pad = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(pad).rectangle((tx - 30, ty - 20, tx + tw + 30, ty + (170 if sub else 110)), fill=(10, 12, 15, 170))
        im.alpha_composite(pad); d = ImageDraw.Draw(im)
        d.text((tx, ty), place.upper(), font=f, fill=WHITE)
        if sub: d.text((tx, ty + 104), sub, font=fs, fill=YEL)
    return im
def s1_text(cols):
    im = bgcard(); d = ImageDraw.Draw(im); n = len(cols); cw = (W - 2 * MX) / n
    for i, c in enumerate(cols):
        x = MX + cw * i
        if i: d.line((x, 300, x, 780), fill=(70, 74, 80), width=3)
        L = c.split('\n'); y = 420
        for j, l in enumerate(L):
            f = F('disp_b', 70 if j == 0 else (110 if len(l) <= 4 else 48)); col = WHITE if j == 0 else (YEL if l.strip() in ('SÍ', '✔') else (230, 80, 70) if l.strip() in ('NO', '×') else WHITE)
            lw = d.textlength(l, font=f); d.text((x + (cw - lw) / 2, y), l, font=f, fill=col); y += int(f.size * 1.3)
    return im
def s1_split(imgA, imgB, labA='', labB=''):
    im = Image.new('RGBA', (W, H), INK + (255,)); w = W // 2 - 6
    for i, (img, lab) in enumerate(((imgA, labA), (imgB, labB))):
        t = img.convert('RGB'); r = max(w / t.width, H / t.height); t = t.resize((int(t.width * r) + 1, int(t.height * r) + 1))
        ox = (t.width - w) // 2; t = t.crop((ox, 0, ox + w, H)); im.paste(t, (i * (W // 2 + 6), 0))
        if lab:
            d = ImageDraw.Draw(im); f = F('disp_b', 46); x = i * (W // 2 + 6) + 60
            d.rectangle((x - 20, 60, x + d.textlength(lab, font=f) + 20, 130), fill=(0, 0, 0, 200)); d.text((x, 68), lab, font=f, fill=WHITE)
    ImageDraw.Draw(im).rectangle((W // 2 - 6, 0, W // 2 + 6, H), fill=YEL)
    return im
def capture_frame(path, maxw=0.88, crop=None):
    """Captura o recorte de prensa: centrado sobre fondo de la propia captura desenfocada."""
    src = Image.open(path).convert('RGB')
    if crop: src = src.crop(crop)
    bg = src.resize((W, H)).filter(ImageFilter.GaussianBlur(40)); bg = Image.alpha_composite(bg.convert('RGBA'), Image.new('RGBA', (W, H), INK + (200,)))
    r = min(W * maxw / src.width, H * 0.74 / src.height); t = src.resize((int(src.width * r), int(src.height * r)), Image.LANCZOS)
    x = (W - t.width) // 2; y = (H - t.height) // 2 + 70
    sh = Image.new('RGBA', (t.width + 60, t.height + 60), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((30, 30, t.width + 30, t.height + 30), fill=(0, 0, 0, 160))
    bg.paste(sh.filter(ImageFilter.GaussianBlur(18)), (x - 30, y - 20), sh.filter(ImageFilter.GaussianBlur(18))); bg.paste(t, (x, y))
    return bg
def credits(lines, title='FUENTES'):
    im = bgcard(); d = ImageDraw.Draw(im); y = 110; y = kicker(d, MX, y, title, YEL, 34)
    cols = 2 if len(lines) > 14 else 1; per = (len(lines) + cols - 1) // cols; cw = (W - 2 * MX) / cols
    for c in range(cols):
        yy = y + 20
        for l in lines[c * per:(c + 1) * per]:
            d.text((MX + c * cw, yy), l, font=F('body_m', 30), fill=LIGHT); yy += 44
    return im
def disclaimer(text):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
    s, L = fit(d, text, 'body', [44, 40, 36], 1300, 8); y = (H - len(L) * int(s * 1.45)) // 2
    for l in L:
        tw = d.textlength(l, font=F('body', s)); d.text(((W - tw) / 2, y), l, font=F('body', s), fill=LIGHT); y += int(s * 1.45)
    return im
def presenta():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
    f = F('body_sb', 40); t = 'DOCUVOX PRESENTA'; tw = spaced_len(d, t, f, 14); spaced(d, ((W - tw) / 2, H / 2 - 30), t, f, WHITE, 14)
    return im
def titulo(t1_, t2_=''):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
    f = F('disp_xb', 150); tw = d.textlength(t1_, font=f); d.text(((W - tw) / 2, H / 2 - 140), t1_, font=f, fill=WHITE)
    if t2_: f2 = F('body_sb', 44); tw = spaced_len(d, t2_, f2, 10); spaced(d, ((W - tw) / 2, H / 2 + 60), t2_, f2, YEL, 10)
    return im

def nota(text):
    """Cartel sobre la imagen, centrado en la parte baja (por encima de los subtítulos)."""
    im = canvas(); d = ImageDraw.Draw(im); f = F('disp_sb', 46)
    L = wrap(d, text, f, 1400)[:2]; lh = 58; y0 = 640
    w = max(d.textlength(l, font=f) for l in L) + 60
    d.rectangle(((W - w) / 2, y0 - 16, (W + w) / 2, y0 + lh * len(L) + 10), fill=(0, 0, 0, 200))
    d.rectangle(((W - w) / 2, y0 - 16, (W - w) / 2 + 6, y0 + lh * len(L) + 10), fill=YEL)
    for i, l in enumerate(L):
        tw = d.textlength(l, font=f); d.text(((W - tw) / 2, y0 + i * lh), l, font=f, fill=WHITE)
    return im
