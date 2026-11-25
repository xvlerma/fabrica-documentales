"""Grafismo v3 de «A quemarropa» (DocuVox) — estilo único del encargo «MONTAJE FINAL v3».
A · rótulo de tercio inferior con caja negra al 65 %, acento amarillo de 4 px, Inter 44/32.
B · tarjetas con el texto en capa transparente: el fondo (plano vecino desenfocado y oscurecido, con acercamiento
    del 3 %) lo pone el motor de render. Cita Crimson cursiva 42 px; dato Inter Display SemiBold ≤ 72 px; texto Inter 34 px.
C · desenfoque localizado de faldones ajenos (lo aplica el motor; aquí solo la máscara).
D · subtítulos de 40 px en caja negra al 65 %, al 82 % de la altura."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import re, json, os, math
W, H = 1920, 1080
YEL = (0xF2, 0xFF, 0x00); WHITE = (255, 255, 255); BLACK = (0, 0, 0)
INK = (14, 15, 17); GREY = (0xD9, 0xD9, 0xD9); LIGHT = (0xE6, 0xE6, 0xE6); MID = (150, 154, 160)
SAFE_X = 96; SAFE_Y = 54
MX = 150                       # margen izquierdo de las tarjetas (dentro del área segura)
TXT_W = int(W * 0.70)          # ancho máximo de la caja de texto de tarjeta
BOX_A = 166                    # negro al 65 %
FD = '/usr/share/fonts/opentype/inter/'; CR = '/usr/share/fonts/truetype/google-fonts/ofl/crimsontext/'
FILES = {'disp_b': FD + 'InterDisplay-Bold.otf', 'disp_sb': FD + 'InterDisplay-SemiBold.otf', 'disp_xb': FD + 'InterDisplay-ExtraBold.otf',
         'disp_m': FD + 'InterDisplay-Medium.otf', 'body': FD + 'Inter-Regular.otf', 'body_m': FD + 'Inter-Medium.otf', 'body_sb': FD + 'Inter-SemiBold.otf',
         'body_b': FD + 'Inter-Bold.otf', 'quote': CR + 'CrimsonText-Italic.ttf', 'quote_sb': CR + 'CrimsonText-SemiBoldItalic.ttf'}
INTERNAL = re.compile(r'\s*\[legal[^\]]*\]|\s*\[#[^\]]*\]|\s*\[AVI[^\]]*\]|\s*AVI-\S+|\s*\((?:literal|verificar|comprobar)[^)]*\)|\s*comprobar al oído|\s*·?\s*verif\.\s*#?[\d#\s,]*(?:\([^)]*\))?', re.I)
def SAN(t):
    """saneado de todo texto en pantalla: fuera notas internas, «SEÑAL:», «VÍA »"""
    if not isinstance(t, str): return t
    t = t.replace('✕', '×').replace('✓', '✔')
    t = INTERNAL.sub('', t)
    t = re.sub(r'\bSEÑAL:\s*', '', t); t = re.sub(r'\bSeñal:\s*', '', t)
    t = re.sub(r'(^|·\s*)V[ÍI]A\s+', r'\1', t); t = re.sub(r'(^|·\s*)[Vv]ía\s+', r'\1', t)
    t = re.sub(r'\s+(V[ÍI]A|[Vv]ía)\s+', ' · ', t)
    t = re.sub(r'[ \t]+', ' ', t)
    return t.strip()
_otext = ImageDraw.ImageDraw.text; _olen = ImageDraw.ImageDraw.textlength
ImageDraw.ImageDraw.text = lambda self, xy, text, *a, **k: _otext(self, xy, SAN(text) if text not in ('«', '»') else text, *a, **k)
ImageDraw.ImageDraw.textlength = lambda self, text, *a, **k: _olen(self, SAN(text) if text.strip() else text, *a, **k)
_F = {}
def F(w, s):
    if (w, s) not in _F: _F[(w, s)] = ImageFont.truetype(FILES[w], s)
    return _F[(w, s)]
def canvas(bg=None): return Image.new('RGBA', (W, H), (0, 0, 0, 0) if bg is None else tuple(bg) + (255,))
def bgcard():
    """capa de tarjeta: transparente (el fondo desenfocado lo compone el render)"""
    return canvas()
NOBREAK = re.compile(r'\b(el|la|los|las|un|una|de|del|y|e|a|en|por|con|al|su|sus|que|o|u|no|ni|lo|se)$', re.I)
def wrap(d, text, f, maxw):
    """corte por sentido: nunca deja al final de línea un artículo/preposición corta, ni separa número y unidad"""
    out = []
    for para in SAN(text).split('\n'):
        words = para.split(); cur = []
        i = 0
        while i < len(words):
            w = words[i]
            t = ' '.join(cur + [w])
            if d.textlength(t, font=f) <= maxw or not cur: cur.append(w); i += 1; continue
            # mover a la línea siguiente la palabra «débil» final y números con su unidad
            nxt = []
            while len(cur) > 1 and (NOBREAK.search(cur[-1]) or re.fullmatch(r'[\d.,]+', cur[-1])): nxt.insert(0, cur.pop())
            out.append(' '.join(cur)); cur = nxt
        if cur: out.append(' '.join(cur))
    return out
def fit(d, text, w, sizes, maxw, maxlines):
    for s in sizes:
        L = wrap(d, text, F(w, s), maxw)
        if len(L) <= maxlines: return s, L
    s = sizes[-1]; return s, wrap(d, text, F(w, s), maxw)
def spaced(d, xy, text, f, fill, track=3):
    x, y = xy
    for ch in SAN(text) if len(text) > 1 else text:
        _otext(d, (x, y), ch, font=f, fill=fill); x += _olen(d, ch, font=f) + track
    return x
def spaced_len(d, text, f, track=3): return sum(_olen(d, c, font=f) + track for c in (SAN(text) if len(text) > 1 else text))
def rule(d, x, y, w=120, col=YEL, th=4): d.rectangle((x, y, x + w, y + th), fill=col)
_DM = ImageDraw.Draw(Image.new('RGBA', (8, 8)))

# ------------------------------------------------------------------ etiquetas y píldoras
TAG_COL = {'DIJO': (WHITE, BLACK), 'HIZO': (YEL, BLACK), 'CONDENAD': ((0xE5, 0x48, 0x4D), WHITE), 'INVESTIGAD': ((0xF5, 0xA6, 0x23), BLACK),
           'NO IMPUTAD': ((0x8A, 0x8F, 0x96), WHITE), 'PROCESAD': ((0xF5, 0xA6, 0x23), BLACK), 'SIN PRUEBA': ((0x8A, 0x8F, 0x96), WHITE),
           'ACUSACIÓN': ((0x8E, 0x44, 0xAD), WHITE), 'INDICIO': ((0x2E, 0x86, 0xC1), WHITE), 'PUBLICADO': ((0x5D, 0x6D, 0x7E), WHITE),
           'SU CIFRA': ((0xF5, 0xA6, 0x23), BLACK), 'DATO': (YEL, BLACK), 'TESTIGO': ((0x8A, 0x8F, 0x96), WHITE), 'VERSIÓN': ((0x5D, 0x6D, 0x7E), WHITE),
           'AUDIO': ((0x5D, 0x6D, 0x7E), WHITE), 'AVISO': ((0x5D, 0x6D, 0x7E), WHITE)}
def tag_colors(label):
    u = label.upper()
    for k, v in TAG_COL.items():
        if k in u: return v
    return (WHITE, BLACK)
def pill(d, x, y, label, size=24, maxw=None):
    """píldora en versalitas; si no cabe en maxw, en dos líneas. Devuelve (ancho, alto)."""
    f = F('body_b', size); txt = SAN(label).upper(); bg, fg = tag_colors(txt)
    lines = [txt]
    if maxw and spaced_len(d, txt, f, 2) + 2 * int(size * 0.55) > maxw:
        lines = wrap(d, txt, f, maxw - 2 * int(size * 0.55) - 20)
    padx = int(size * 0.55); lh = int(size * 1.35)
    tw = max(spaced_len(d, l, f, 2) for l in lines) + 2 * padx; th = lh * len(lines) + int(size * 0.25)
    d.rectangle((x, y, x + tw, y + th), fill=bg)
    for i, l in enumerate(lines): spaced(d, (x + padx, y + int(size * 0.18) + i * lh), l, f, fg, 2)
    return tw, th

# ------------------------------------------------------------------ A · rótulo de tercio inferior
def shorten2(line2, f, maxw):
    parts = [p.strip() for p in SAN(line2).split(' · ') if p.strip()]
    s = ' · '.join(parts)
    return s
def r1(line1, line2='', tag=None, bottom=980, maxw=1200):
    """Identificador: caja negra 65 % abajo a la izquierda, acento amarillo 4 px, nombre 44 SemiBold, 2.ª línea 32 regular gris claro.
    bottom = borde inferior de la caja (subirlo cuando el corte trae subtítulos quemados)."""
    im = canvas(); d = ImageDraw.Draw(im)
    fn = F('body_sb', 44); f2 = F('body', 32)
    name = SAN(line1).strip()
    sn, Ln = fit(d, name, 'body_sb', [44, 40, 36], maxw, 1)
    fn = F('body_sb', sn)
    l2 = shorten2(line2, f2, maxw) if line2 else ''
    L2 = wrap(d, l2, f2, maxw)[:2] if l2 else []
    padx, pady = 24, 14
    tag_h = 0; tag_w = 0
    if tag: tag_w, tag_h = pill(_DM, 0, 0, tag, 24)
    w = max([d.textlength(l, font=fn) for l in Ln] + [d.textlength(l, font=f2) for l in L2] + [tag_w]) + 2 * padx + 4
    h = pady + (tag_h + 10 if tag else 0) + int(sn * 1.18) * len(Ln) + (8 + 42 * len(L2) if L2 else 0) + pady
    x0 = SAFE_X; y0 = bottom - h
    d.rectangle((x0, y0, x0 + w, bottom), fill=(0, 0, 0, BOX_A))
    d.rectangle((x0, y0, x0 + 3, bottom), fill=YEL + (255,))
    x = x0 + 4 + padx; y = y0 + pady
    if tag: pill(d, x, y, tag, 24); y += tag_h + 10
    for l in Ln: d.text((x, y - 4), l, font=fn, fill=WHITE); y += int(sn * 1.18)
    if L2:
        y += 8
        for l in L2: d.text((x, y - 3), l, font=f2, fill=GREY); y += 42
    im.info['box'] = (x0, y0, x0 + w, bottom); im.info['args'] = ('r1', line1, line2, tag)
    return im
def r1_need(line1, line2='', tag=None):
    """duración mínima de lectura: 3 s o 1 s por cada 15 caracteres"""
    n = len(SAN(line1 or '')) + len(SAN(line2 or '')) + (len(tag) if tag else 0)
    return max(3.0, n / 15.0)
def pie(text, bottom=980):
    t = SAN(text)
    if ' · ' in t:
        a, b = t.split(' · ', 1); return r1(a, b, bottom=bottom)
    return r1(t, '', bottom=bottom)
def subt(text, ycenter=int(H * 0.82)):
    """subtítulo de formas de onda: Inter SemiBold 40 en caja negra 65 %, centrado al 82 % de la altura"""
    im = canvas(); d = ImageDraw.Draw(im); f = F('body_sb', 40)
    text = SAN(text); text = text[:1].upper() + text[1:]
    L = wrap(d, text, f, 1400)[:2]; lh = 54; y0 = ycenter - lh * len(L) // 2
    for i, l in enumerate(L):
        tw = d.textlength(l, font=f); x = (W - tw) / 2; y = y0 + i * lh
        d.rectangle((x - 20, y - 6, x + tw + 20, y + lh - 2), fill=(0, 0, 0, BOX_A))
        d.text((x, y), l, font=f, fill=WHITE)
    return im
def cover(box):
    im = canvas(); ImageDraw.Draw(im).rectangle(box, fill=(0, 0, 0, 255)); return im
def blurmask(boxes, feather=36, size=(W, H)):
    """máscara (L) de las zonas a desenfocar, con bordes difuminados"""
    m = Image.new('L', size, 0); d = ImageDraw.Draw(m)
    for x0, y0, x1, y1 in boxes: d.rectangle((x0, y0, x1, y1), fill=255)
    return m.filter(ImageFilter.GaussianBlur(feather / 2))

# ------------------------------------------------------------------ B · tarjetas (capa transparente)
def _vcenter(hblock): return max(SAFE_Y + 40, (H - hblock) // 2)
def _text(d, x, y, L, f, col, lh):
    for l in L: d.text((x, y), l, font=f, fill=col); y += lh
    return y
def t1(label, text):
    """tarjeta con etiqueta legal (píldora 22 px encima del texto, nunca fuera del cuadro)"""
    im = bgcard(); d = ImageDraw.Draw(im)
    f = F('body', 34)
    L = wrap(d, text, f, TXT_W)[:6] if text else []
    if not text:   # solo etiqueta: dato grande
        s, Lb = fit(d, SAN(label).upper(), 'disp_sb', [72, 64, 56], TXT_W, 2)
        y = _vcenter(len(Lb) * int(s * 1.15)); bg, fg = tag_colors(label)
        rule(d, MX, y - 30, 80, bg if bg != WHITE else YEL, 6)
        _text(d, MX, y, Lb, F('disp_sb', s), WHITE, int(s * 1.15)); return im
    tw, th = pill(_DM, 0, 0, label, 22, TXT_W)
    hb = th + 26 + len(L) * 48; y = _vcenter(hb)
    pill(d, MX, y, label, 22, TXT_W); y += th + 26
    _text(d, MX, y, L, f, WHITE, 48)
    return im
def t2(text, bg=None, kick=None):
    """dato o aviso: texto corrido Inter 34 (máx. 4 líneas de ~50 caracteres; si no cabe, 30 px y 6 líneas), fuente debajo 24 px"""
    im = bgcard(); d = ImageDraw.Draw(im)
    parts = SAN(text).split('\n'); main = parts[0]; src = ' '.join(parts[1:]).strip()
    m = re.match(r'^([A-ZÁÉÍÓÚÑ0-9/ ÜÇ\'«»\-]{3,40}) · (.*)$', main)
    if m and not kick: kick, main = m.group(1), m.group(2)
    s, L = fit(d, main, 'body', [34, 32, 30], 1120, 4)
    if len(L) > 4: s, L = fit(d, main, 'body', [30, 28], TXT_W, 7)
    lh = int(s * 1.42)
    hb = (s and len(L) * lh) + (50 if kick else 0) + (60 if src else 0); y = _vcenter(hb)
    if kick:
        kw, kh = pill(d, MX, y, kick, 22, TXT_W); y += kh + 22
    y = _text(d, MX, y, L, F('body', s), WHITE, lh)
    if src:
        rule(d, MX, y + 16, 60, YEL, 3); d.text((MX, y + 30), src, font=F('body', 24), fill=GREY)
    return im
def q1(quote, source='', bg=None, kick=None):
    """cita literal: Crimson Text cursiva 42 px con comillas «», fuente debajo en Inter 24"""
    im = bgcard(); d = ImageDraw.Draw(im)
    q = SAN(quote).strip(); q = re.sub(r'^[«"“]\s*', '', q); q = re.sub(r'\s*[»"”]$', '', q)
    s, L = fit(d, q, 'quote', [42], TXT_W - 40, 9)
    if len(L) > 9: s, L = fit(d, q, 'quote', [38, 36], TXT_W, 11)
    lh = int(s * 1.32); src = SAN(source or '')
    Ls = wrap(d, src, F('body', 24), TXT_W)[:3] if src else []
    hb = len(L) * lh + (36 + 34 * len(Ls) if Ls else 0) + (52 if kick else 0); y = _vcenter(hb)
    if kick:
        kw, kh = pill(d, MX, y, kick, 22, TXT_W); y += kh + 24
    for i, l in enumerate(L):
        t = ('«' if i == 0 else '') + l + ('»' if i == len(L) - 1 else '')
        _otext(d, (MX if i else MX - _olen(d, '«', font=F('quote', s)), y), t, font=F('quote', s), fill=WHITE); y += lh
    if Ls:
        rule(d, MX, y + 14, 60, YEL, 3); y += 30
        for l in Ls: d.text((MX, y), l, font=F('body', 24), fill=GREY); y += 34
    return im
def d1(big, label=''):
    """dato o número: Inter Display SemiBold ≤ 72 px, una línea de contexto de 28 px debajo"""
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, SAN(big), 'disp_sb', [72, 64, 56, 48], TXT_W, 2)
    Ll = wrap(d, label, F('body', 28), TXT_W)[:3] if label else []
    hb = len(L) * int(s * 1.12) + (24 + 40 * len(Ll) if Ll else 0); y = _vcenter(hb)
    rule(d, MX, y - 26, 80, YEL, 6)
    y = _text(d, MX, y, L, F('disp_sb', s), WHITE, int(s * 1.12))
    if Ll: _text(d, MX, y + 24, Ll, F('body', 28), GREY, 40)
    return im
def n1(word, yellow=False):
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, SAN(word), 'disp_sb', [64, 56, 48, 42], TXT_W, 3)
    y = _vcenter(len(L) * int(s * 1.18))
    _text(d, MX, y, L, F('disp_sb', s), YEL if yellow else WHITE, int(s * 1.18))
    return im
def x1(num, title, sub=''):
    """cartel de expediente"""
    im = bgcard(); d = ImageDraw.Draw(im)
    lab = f'EXPEDIENTE {int(num):02d}' if str(num).isdigit() else str(num)
    s, L = fit(d, SAN(title).upper(), 'disp_sb', [72, 64, 56], TXT_W, 2)
    Ls = wrap(d, sub, F('body', 32), TXT_W)[:3] if sub else []
    hb = 60 + len(L) * int(s * 1.1) + (30 + 46 * len(Ls) if Ls else 0); y = _vcenter(hb)
    f = F('body_sb', 26); spaced(d, (MX, y), lab, f, YEL, 5); y += 60
    y = _text(d, MX, y, L, F('disp_sb', s), WHITE, int(s * 1.1))
    if Ls: rule(d, MX, y + 12, 80, YEL, 4); _text(d, MX, y + 36, Ls, F('body', 32), GREY, 46)
    return im
def x0(title): return n1(title)
def p1(q):
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, q, 'disp_sb', [64, 56, 48], TXT_W, 4); hb = 50 + len(L) * int(s * 1.2); y = _vcenter(hb)
    kw, kh = pill(d, MX, y, 'LA PREGUNTA', 22); y += kh + 24
    _text(d, MX, y, L, F('disp_sb', s), WHITE, int(s * 1.2)); return im
def k1(num, rest):
    im = bgcard(); d = ImageDraw.Draw(im)
    Ll = wrap(d, rest, F('body', 30), TXT_W)[:3] if rest else []
    hb = 50 + 84 + (20 + 42 * len(Ll) if Ll else 0); y = _vcenter(hb)
    kw, kh = pill(d, MX, y, 'PERDÓN', 22); y += kh + 20
    d.text((MX, y), f'N.º {num}', font=F('disp_sb', 72), fill=YEL); y += 90
    if Ll: _text(d, MX, y, Ll, F('body', 30), GREY, 42)
    return im
def z1(text):
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, text, 'body', [34, 32, 30], TXT_W, 5); y = _vcenter(len(L) * int(s * 1.42))
    _text(d, MX, y, L, F('body', s), LIGHT, int(s * 1.42)); return im
def r2(names, dim=()):
    """lista de personas con su estado procesal"""
    im = bgcard(); d = ImageDraw.Draw(im); n = len(names)
    lh = min(110, 820 // max(n, 1)); y = _vcenter(lh * n)
    fs = 44 if lh >= 100 else 36
    for i, (nm, st) in enumerate(names):
        col = (120, 120, 120) if i in dim else WHITE
        d.text((MX, y), SAN(nm).upper(), font=F('body_sb', fs), fill=col)
        if st:
            nw = d.textlength(SAN(nm).upper(), font=F('body_sb', fs))
            pill(d, MX + nw + 28, y + 6, st, 22)
        y += lh
    return im
def l1(items, upto=None):
    """cronología: línea fina, puntos amarillos, textos de 26 px que se leen enteros"""
    im = bgcard(); d = ImageDraw.Draw(im); n = max(1, len(items)); upto = n if upto is None else upto
    x0_, x1_ = MX, W - MX; y0 = 500; cw = (x1_ - x0_) / n
    d.line((x0_, y0, x1_, y0), fill=(120, 124, 130), width=2)
    for i, (fe, hi) in enumerate(items):
        x = x0_ + cw * (i + 0.5); on = i < upto
        if on: d.line((x0_ if i == 0 else x0_ + cw * (i - 0.5), y0, x, y0), fill=YEL, width=2)
        r = 9; d.ellipse((x - r, y0 - r, x + r, y0 + r), fill=YEL if on else (90, 94, 100))
        if not on: continue
        f = F('disp_sb', 34); fw = d.textlength(fe, font=f)
        d.text((x - fw / 2, y0 - 70), fe, font=f, fill=YEL)
        fb = F('body', 26); L = wrap(d, hi, fb, cw - 30)[:5]; yy = y0 + 32
        for l in L:
            lw = d.textlength(l, font=fb); d.text((x - lw / 2, yy), l, font=fb, fill=WHITE); yy += 36
    return im
# --- mapa real (Natural Earth): opaco, con su propio fondo
GEO = '/home/claude/w/aq/geo/countries.geojson'
PLACES = {'MELILLA': ((-2.94, 35.29), (-3.6, 36.3), 4.4), 'CEUTA': ((-5.32, 35.89), (-4.6, 36.4), 4.4),
          'ADAMUZ': ((-4.52, 38.03), (-3.7, 39.9), 10.5), 'URDA': ((-3.72, 39.41), (-3.7, 39.9), 10.5), 'BARBATE': ((-5.92, 36.19), (-5.3, 36.7), 4.4)}
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
        for r, a in ((34, 50), (20, 110), (9, 255)): d.ellipse((x - r, y - r, x + r, y + r), fill=YEL + (a,))
        f = F('disp_sb', 64); fs = F('body', 32)
        tw = max(d.textlength(place.upper(), font=f), d.textlength(sub, font=fs) if sub else 0)
        tx = x + 60 if x + 60 + tw < W - SAFE_X else x - 60 - tw
        ty = y - 110 if y > 260 else y + 50
        pad = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(pad).rectangle((tx - 24, ty - 14, tx + tw + 24, ty + (128 if sub else 84)), fill=(0, 0, 0, BOX_A))
        im.alpha_composite(pad); d = ImageDraw.Draw(im)
        d.rectangle((tx - 24, ty - 14, tx - 21, ty + (128 if sub else 84)), fill=YEL)
        d.text((tx, ty), place.upper(), font=f, fill=WHITE)
        if sub: d.text((tx, ty + 80), sub, font=fs, fill=GREY)
    d.text((W - SAFE_X - 360, H - SAFE_Y - 20), 'Mapa: Natural Earth', font=F('body', 20), fill=(150, 154, 160))
    return im
def s1_text(cols):
    im = bgcard(); d = ImageDraw.Draw(im); n = len(cols); cw = (W - 2 * MX) / n
    for i, c in enumerate(cols):
        x = MX + cw * i
        if i: d.line((x, 360, x, 720), fill=(120, 124, 130), width=2)
        L = c.split('\n'); y = 430
        for j, l in enumerate(L):
            big = j > 0 and len(l.strip()) <= 4
            f = F('disp_sb', 56 if j == 0 else (72 if big else 30))
            col = WHITE if j == 0 else (YEL if l.strip() in ('SÍ', '✔') else (0xE5, 0x48, 0x4D) if l.strip() in ('NO', '×') else GREY)
            lw = d.textlength(l, font=f); d.text((x + (cw - lw) / 2, y), l, font=f, fill=col); y += int(f.size * 1.35)
    return im
def s1_split(imgA, imgB, labA='', labB=''):
    """pantalla partida (dos fotogramas reales): opaca"""
    im = Image.new('RGBA', (W, H), INK + (255,)); w = W // 2 - 3
    for i, (img, lab) in enumerate(((imgA, labA), (imgB, labB))):
        t = img.convert('RGB'); r = max(w / t.width, H / t.height); t = t.resize((int(t.width * r) + 1, int(t.height * r) + 1))
        ox = (t.width - w) // 2; t = t.crop((ox, 0, ox + w, H)); im.paste(t, (i * (W // 2 + 3), 0))
    d = ImageDraw.Draw(im); d.rectangle((W // 2 - 3, 0, W // 2 + 3, H), fill=YEL)
    for i, lab in enumerate((labA, labB)):
        if not lab: continue
        f = F('body_sb', 32); x = i * (W // 2 + 3) + SAFE_X; tw = d.textlength(lab, font=f)
        ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(ov).rectangle((x, 960 - 64, x + tw + 52, 960), fill=(0, 0, 0, BOX_A))
        im.alpha_composite(ov); d = ImageDraw.Draw(im); d.rectangle((x, 896, x + 3, 960), fill=YEL); d.text((x + 28, 908), lab, font=f, fill=WHITE)
    return im
def capture_frame(path, maxw=0.88, crop=None):
    """captura o documento: centrado sobre la propia captura desenfocada (opaco)"""
    src = Image.open(path).convert('RGB')
    if crop: src = src.crop(crop)
    bg = src.resize((W, H)).filter(ImageFilter.GaussianBlur(40)); bg = Image.alpha_composite(bg.convert('RGBA'), Image.new('RGBA', (W, H), INK + (200,)))
    r = min(W * maxw / src.width, H * 0.74 / src.height); t = src.resize((int(src.width * r), int(src.height * r)), Image.LANCZOS)
    x = (W - t.width) // 2; y = (H - t.height) // 2 - 30
    sh = Image.new('RGBA', (t.width + 60, t.height + 60), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((30, 30, t.width + 30, t.height + 30), fill=(0, 0, 0, 160))
    bg.paste(sh.filter(ImageFilter.GaussianBlur(18)), (x - 30, y - 20), sh.filter(ImageFilter.GaussianBlur(18))); bg.paste(t, (x, y))
    return bg
def disclaimer(text):
    im = bgcard(); d = ImageDraw.Draw(im)
    s, L = fit(d, text, 'body', [34, 32], 1100, 10); lh = int(s * 1.5); y = _vcenter(len(L) * lh)
    for l in L:
        tw = d.textlength(l, font=F('body', s)); d.text(((W - tw) / 2, y), l, font=F('body', s), fill=LIGHT); y += lh
    return im
def presenta():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
    f = F('body_sb', 40); t = 'DOCUVOX PRESENTA'; tw = spaced_len(d, t, f, 14); spaced(d, ((W - tw) / 2, H / 2 - 30), t, f, WHITE, 14)
    return im
def nota(text, bottom=None):
    """cartel informativo sobre imagen: estilo A (caja del tercio inferior, sin nombre)"""
    im = canvas(); d = ImageDraw.Draw(im); f = F('body_sb', 40)
    L = wrap(d, text, f, 1300)[:2]; lh = 52
    w = max(d.textlength(l, font=f) for l in L) + 52; h = lh * len(L) + 28
    bottom = bottom or 980; y0 = bottom - h; x0 = SAFE_X
    d.rectangle((x0, y0, x0 + w, bottom), fill=(0, 0, 0, BOX_A)); d.rectangle((x0, y0, x0 + 3, bottom), fill=YEL)
    for i, l in enumerate(L): d.text((x0 + 28, y0 + 12 + i * lh), l, font=f, fill=WHITE)
    im.info['args'] = ('nota', text, '', None)
    return im
# ------------------------------------------------------------------ D-08 · créditos a dos columnas (rodillo)
def credits_roll(blocks, colw=int(W * 0.55) - 2 * SAFE_X):
    """imagen alta (RGBA transparente) con el texto de los créditos; blocks = [(titulo, [lineas], ncols)]"""
    f_t = F('body_sb', 30); f_l = F('body', 26); f_s = F('body_sb', 22)
    rows = []
    y = 0
    out = Image.new('RGBA', (colw, 20000), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    for title, lines, ncols in blocks:
        if title:
            spaced(d, (0, y), title.upper(), f_s, YEL, 4); y += 46
        if ncols == 1:
            for l in lines:
                for ll in wrap(d, l, f_l, colw):
                    d.text((0, y), ll, font=f_l, fill=WHITE); y += 38
        else:
            cw = (colw - 30) // ncols; per = (len(lines) + ncols - 1) // ncols
            for c in range(ncols):
                yy = y
                for l in lines[c * per:(c + 1) * per]:
                    t = l
                    while d.textlength(t, font=f_l) > cw - 10 and len(t) > 4: t = t[:-2]
                    if t != l: t = t.rstrip() + '…'
                    d.text((c * (cw + 30), yy), t, font=f_l, fill=WHITE); yy += 36
            y += per * 36
        y += 64
    return out.crop((0, 0, colw, y))
