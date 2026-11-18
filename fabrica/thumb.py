"""Miniatura de YouTube con el Design System DocuVox (1280×720).

Uso:
  python fabrica/thumb.py salida.jpg --foto retrato.png --fondo documento.png \
      --grande "PUCHERAZO" --caja "DEL 36" --sub "LAS ELECCIONES DE FEBRERO" [--recorte x0,y0,x1,y1]

Reglas: foto real de archivo en B/N a la derecha; palabra grande blanca (Barlow Condensed Black) y segunda
parte en la caja amarilla #F2FF00 con letra negra; línea secundaria gris con el punto amarillo; logo arriba a la
izquierda; esquina inferior derecha libre (duración de YouTube). Comprueba la lectura a 320×180 (se guarda _mini)."""
import os, sys, argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.join(os.path.dirname(HERE), 'assets', 'brand')
W, H, Y = 1280, 720, (242, 255, 0)

def make(out, foto, grande, caja, sub='', fondo=None, recorte=None, fondo_recorte=None):
    if fondo:
        bg = Image.open(fondo).convert('L')
        if fondo_recorte: bg = bg.crop(fondo_recorte)
        bg = ImageOps.fit(bg, (W, H)); bg = ImageEnhance.Brightness(bg).enhance(0.38).filter(ImageFilter.GaussianBlur(1.2))
    else: bg = Image.new('L', (W, H), 18)
    im = Image.merge('RGB', [bg] * 3)
    p = Image.open(foto).convert('L')
    if recorte: p = p.crop(recorte)
    p = ImageEnhance.Contrast(ImageOps.autocontrast(p, cutoff=1)).enhance(1.25)
    ph = 760; p = p.resize((int(p.width * ph / p.height), ph), Image.LANCZOS)
    m = Image.new('L', p.size, 255); md = ImageDraw.Draw(m)
    for x in range(260): md.line([(x, 0), (x, p.height)], fill=int(255 * x / 260))
    im.paste(Image.merge('RGB', [p] * 3), (W - p.width + 60, -10), m)
    v = Image.new('L', (W, H), 0); ImageDraw.Draw(v).ellipse([-300, -250, W + 300, H + 250], fill=255)
    im = Image.composite(im, Image.new('RGB', (W, H)), v.filter(ImageFilter.GaussianBlur(160)))
    g = Image.new('L', (W, H)); gd = ImageDraw.Draw(g)
    for x in range(W): gd.line([(x, 0), (x, H)], fill=max(0, int(225 - x * 0.30)))
    im = Image.composite(Image.new('RGB', (W, H)), im, g); d = ImageDraw.Draw(im)
    B = lambda n, s: ImageFont.truetype(f'{KIT}/BarlowCondensed-{n}.ttf', s)
    x0 = 58; size = 178
    while d.textlength(grande, font=B('Black', size)) > 720 and size > 90: size -= 6
    f1 = B('Black', size)
    d.text((x0 + 5, 185), grande, font=f1, fill=(0, 0, 0)); d.text((x0, 180), grande, font=f1, fill=(255, 255, 255))
    size2 = 150
    while d.textlength(caja, font=B('Black', size2)) > 700 and size2 > 70: size2 -= 6
    f2 = B('Black', size2); bb = d.textbbox((0, 0), caja, font=f2); tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.rectangle([x0 - 6, 400, x0 + tw + 30, 400 + th + 46], fill=Y); d.text((x0 + 12, 400 + 23 - bb[1]), caja, font=f2, fill=(10, 10, 10))
    if sub:
        f3 = B('SemiBold', 40); d.text((x0 + 2, 600), sub.upper(), font=f3, fill=(205, 205, 205))
        tb = d.textbbox((x0 + 2, 600), sub.upper(), font=f3); d.ellipse([tb[2] + 14, 615, tb[2] + 28, 629], fill=Y)
    logo = Image.open(f'{KIT}/DocuVox_Logo_Horizontal_Amarillo-Blanco.png').convert('RGBA'); lw = 210
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS); im.paste(logo, (x0, 52), logo)
    im.save(out, quality=93); im.resize((320, 180), Image.LANCZOS).save(os.path.splitext(out)[0] + '_mini.jpg', quality=90)
    return out

if __name__ == '__main__':
    a = argparse.ArgumentParser(); a.add_argument('out'); a.add_argument('--foto', required=True); a.add_argument('--grande', required=True)
    a.add_argument('--caja', required=True); a.add_argument('--sub', default=''); a.add_argument('--fondo'); a.add_argument('--recorte'); a.add_argument('--fondo_recorte')
    r = a.parse_args(); tup = lambda s: tuple(int(v) for v in s.split(',')) if s else None
    print(make(r.out, r.foto, r.grande, r.caja, r.sub, r.fondo, tup(r.recorte), tup(r.fondo_recorte)))
