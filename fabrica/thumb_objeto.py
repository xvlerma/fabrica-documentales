"""Miniatura DocuVox de OBJETO: pieza de museo recortada, iluminada sobre negro.

Formatos: 'yt' 1280×720 (objeto a la derecha, texto a la izquierda) y 'cuadrada' 3000×3000 (iVoox/podcast:
objeto arriba, texto abajo). Mantiene el color real de la pieza (bronce), con luz cálida desde arriba.
Texto: palabra grande blanca (Barlow Condensed Black) y caja amarilla #F2FF00 con letra negra, logo DocuVox."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.join(os.path.dirname(HERE), 'assets', 'brand')
Y = (242, 255, 0)
B = lambda n, s: ImageFont.truetype(f'{KIT}/BarlowCondensed-{n}.ttf', s)


def recortar(foto):
    """Devuelve RGBA con el fondo del museo quitado (rembg; si no, umbral sobre fondo claro)."""
    im = Image.open(foto).convert('RGB')
    try:
        from rembg import remove
        cut = remove(im)
    except Exception as e:
        print('  rembg no disponible, uso umbral:', e)
        g = ImageOps.grayscale(im)
        bgv = sorted(g.getpixel((x, y)) for x, y in [(2, 2), (g.width - 3, 2), (2, g.height - 3), (g.width - 3, g.height - 3)])[1]
        diff = ImageChops.difference(g, Image.new('L', g.size, bgv)).point(lambda v: 255 if v > 28 else 0)
        diff = diff.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.5))
        cut = im.convert('RGBA'); cut.putalpha(diff)
    bb = cut.getchannel('A').point(lambda v: 255 if v > 20 else 0).getbbox()
    return cut.crop(bb) if bb else cut


def fondo(w, h, cx, cy, r):
    bg = Image.new('RGB', (w, h), (6, 5, 4))
    luz = Image.new('L', (w, h), 0); ImageDraw.Draw(luz).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    luz = luz.filter(ImageFilter.GaussianBlur(r * 0.55))
    calido = Image.new('RGB', (w, h), (70, 46, 20))
    return Image.composite(calido, bg, luz.point(lambda v: int(v * 0.85)))


def pegar(im, obj, x, y, alto):
    o = obj.resize((int(obj.width * alto / obj.height), alto), Image.LANCZOS)
    rgb = ImageEnhance.Contrast(o.convert('RGB')).enhance(1.15)
    rgb = ImageEnhance.Brightness(rgb).enhance(1.05); a = o.getchannel('A')
    # luz cenital: oscurece la parte baja de la pieza
    grad = Image.new('L', o.size); gd = ImageDraw.Draw(grad)
    for yy in range(o.height): gd.line([(0, yy), (o.width, yy)], fill=int(255 - 120 * yy / o.height))
    rgb = Image.composite(rgb, Image.new('RGB', o.size), grad)
    # sombra/halo
    halo = Image.new('L', im.size, 0); halo.paste(a.point(lambda v: int(v * 0.6)), (x, y + int(alto * 0.03)))
    im.paste(Image.new('RGB', im.size, (0, 0, 0)), (0, 0), halo.filter(ImageFilter.GaussianBlur(alto * 0.04)))
    im.paste(rgb, (x, y), a)
    return o.width


def textos(d, x0, ytop, ancho, grande, caja, sub, k=1.0, centro=False):
    size = int(250 * k)
    while d.textlength(grande, font=B('Black', size)) > ancho and size > 60: size -= 4
    f1 = B('Black', size); tw = d.textlength(grande, font=f1); x = x0 + (ancho - tw) / 2 if centro else x0
    bb = d.textbbox((0, 0), grande, font=f1)
    d.text((x + 6 * k, ytop - bb[1] + 6 * k), grande, font=f1, fill=(0, 0, 0)); d.text((x, ytop - bb[1]), grande, font=f1, fill=(255, 255, 255))
    y2 = ytop + (bb[3] - bb[1]) + int(34 * k)
    size2 = int(96 * k)
    while d.textlength(caja, font=B('Black', size2)) > ancho - 40 * k and size2 > 30: size2 -= 4
    f2 = B('Black', size2); b2 = d.textbbox((0, 0), caja, font=f2); w2, h2 = b2[2] - b2[0], b2[3] - b2[1]
    xb = x0 + (ancho - w2 - 40 * k) / 2 if centro else x0 - 6 * k
    d.rectangle([xb, y2, xb + w2 + 40 * k, y2 + h2 + 40 * k], fill=Y)
    d.text((xb + 20 * k - b2[0], y2 + 20 * k - b2[1]), caja, font=f2, fill=(10, 10, 10))
    y3 = y2 + h2 + int(70 * k)
    if sub:
        f3 = B('SemiBold', int(40 * k)); t = sub.upper(); w3 = d.textlength(t, font=f3)
        xs = x0 + (ancho - w3) / 2 if centro else x0
        d.text((xs, y3), t, font=f3, fill=(200, 200, 200))


def logo(im, x, y, lw):
    lg = Image.open(f'{KIT}/DocuVox_Logo_Horizontal_Amarillo-Blanco.png').convert('RGBA')
    lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS); im.paste(lg, (int(x), int(y)), lg)


def make(out, foto, grande, caja, sub='', formato='yt'):
    obj = recortar(foto)
    if formato == 'cuadrada':
        S = 3000; im = fondo(S, S, S // 2, int(S * 0.36), int(S * 0.42))
        alto = int(S * 0.50); ow = int(obj.width * alto / obj.height)
        if ow > S * 0.72: alto = int(alto * S * 0.72 / ow); ow = int(obj.width * alto / obj.height)
        pegar(im, obj, (S - ow) // 2, int(S * 0.12) + (int(S * 0.50) - alto) // 2, alto)
        d = ImageDraw.Draw(im); textos(d, 200, int(S * 0.635), S - 400, grande, caja, sub, k=2.6, centro=True)
        logo(im, (S - 560) / 2, 120, 560)
    else:
        W, H = 1280, 720; im = fondo(W, H, 930, 300, 430)
        alto = 640; ow = int(obj.width * alto / obj.height)
        if ow > 640: alto = int(alto * 640 / ow); ow = int(obj.width * alto / obj.height)
        pegar(im, obj, 960 - ow // 2, 40 + (640 - alto) // 2, alto)
        d = ImageDraw.Draw(im); textos(d, 58, 190, 560, grande, caja, sub, k=1.0)
        logo(im, 58, 52, 210)
    im.save(out, quality=94)
    if formato != 'cuadrada': im.resize((320, 180), Image.LANCZOS).save(os.path.splitext(out)[0] + '_mini.jpg', quality=90)
    return out
