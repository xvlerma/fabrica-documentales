#!/usr/bin/env python3
"""Shorts verticales 1080x1920 a partir del documental montado, en dos versiones por clip:
  yt  → YouTube Shorts: cierre «DOCUMENTAL COMPLETO EN EL CANAL»
  ig  → Instagram Reels y TikTok: sin logo ni la palabra YouTube; cierre «Documental completo: busca DOCUVOX»
Todo el texto va dentro de la zona segura común (Shorts, Reels y TikTok tapan el 25 % inferior, la franja
derecha de botones y la barra superior): nada importante por debajo de y=1460, ni a la derecha de x=940, ni por encima de y=230.
Uso: python3 shorts.py <mp4> <srt> <carpeta_salida>"""
import json, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

KIT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'brand')
W, H, Y = 1080, 1920, (242, 255, 0)
SAFE_L, SAFE_R = 70, 940            # columna de texto (la derecha queda libre para los botones)
VID_Y = 560                          # vídeo 16:9 (1080x608) entre y=560 y y=1168
SUB_Y = 1200                         # subtítulos justo debajo del vídeo, muy por encima de los títulos de la app
F = lambda n, s: ImageFont.truetype(f'{KIT}/BarlowCondensed-{n}.ttf', s)
SHORTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shorts.json')))


def ts(x):
    h, m, s = x.replace(',', '.').split(':'); return int(h) * 3600 + int(m) * 60 + float(s)


def srt(path):
    out = []
    for b in re.split(r'\n\s*\n', open(path, encoding='utf-8').read().strip()):
        L = b.strip().split('\n')
        if len(L) >= 3 and '-->' in L[1]:
            a, z = L[1].split('-->'); out.append((ts(a.strip()), ts(z.strip()), ' '.join(L[2:])))
    return out


def wrap(d, text, font, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def centered(d, y, line, font, fill, shadow=True):
    cx = (SAFE_L + SAFE_R) / 2; tw = d.textlength(line, font=font)
    if shadow:
        for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3), (4, 4)): d.text((cx - tw / 2 + dx, y + dy), line, font=font, fill=(0, 0, 0))
    d.text((cx - tw / 2, y), line, font=font, fill=fill)
    return tw


def overlay_png(path, hook1, hook2, tag):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    logo = Image.open(f'{KIT}/DocuVox_Logo_Horizontal_Amarillo-Blanco.png').convert('RGBA'); lw = 240
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    im.paste(logo, (int((SAFE_L + SAFE_R) / 2 - lw / 2), 240), logo)
    f1 = F('Black', 96); y = 320
    for ln in wrap(d, hook1.upper(), f1, SAFE_R - SAFE_L)[:2]: centered(d, y, ln, f1, (255, 255, 255)); y += 100
    f2 = F('Black', 84); t2 = hook2.upper(); tw = d.textlength(t2, font=f2); bb = d.textbbox((0, 0), t2, font=f2)
    cx = (SAFE_L + SAFE_R) / 2
    d.rectangle([cx - tw / 2 - 22, y + 8, cx + tw / 2 + 22, y + 8 + bb[3] - bb[1] + 34], fill=Y)
    d.text((cx - tw / 2, y + 25 - bb[1]), t2, font=f2, fill=(10, 10, 10))
    if tag:  # mención fija pequeña, justo encima del vídeo
        f3 = F('SemiBold', 34); centered(d, VID_Y - 46, tag.upper(), f3, (230, 230, 230))
    im.save(path)


def text_png(path, text, size, color, box=None, ypos=SUB_Y, maxlines=2):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F('ExtraBold', size); y = ypos
    for ln in wrap(d, text.upper(), f, SAFE_R - SAFE_L - 20)[:maxlines]:
        if box:
            cx = (SAFE_L + SAFE_R) / 2; tw = d.textlength(ln, font=f)
            d.rectangle([cx - tw / 2 - 18, y - 6, cx + tw / 2 + 18, y + size + 12], fill=box)
            centered(d, y, ln, f, color, shadow=False)
        else: centered(d, y, ln, f, color)
        y += size + 12
    im.save(path)


def cta_png(path, plat):
    if plat == 'yt':
        text_png(path, 'Documental completo en el canal', 66, (10, 10, 10), box=Y, ypos=SUB_Y + 10)
        return
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx = (SAFE_L + SAFE_R) / 2
    d.rectangle([SAFE_L, SUB_Y - 10, SAFE_R, SUB_Y + 230], fill=(10, 10, 10, 235))
    centered(d, SUB_Y + 10, 'DOCUMENTAL COMPLETO:', F('ExtraBold', 54), (255, 255, 255), shadow=False)
    f = F('Black', 92); t = 'BUSCA DOCUVOX'; tw = d.textlength(t, font=f); bb = d.textbbox((0, 0), t, font=f)
    d.rectangle([cx - tw / 2 - 20, SUB_Y + 88, cx + tw / 2 + 20, SUB_Y + 88 + bb[3] - bb[1] + 34], fill=Y)
    d.text((cx - tw / 2, SUB_Y + 105 - bb[1]), t, font=f, fill=(10, 10, 10))
    im.save(path)


def make(mp4, subs, out_dir, k, s, plat):
    t0, t1 = s['start'], s['end']; dur = t1 - t0; wd = os.path.join(out_dir, f'tmp{k}{plat}'); os.makedirs(wd, exist_ok=True)
    tail = 4.5 if plat == 'ig' else 6.0
    overlay_png(f'{wd}/ov.png', s['hook1'], s['hook2'], 'DocuVox · ' + s['tag'] if plat == 'ig' else '')
    cta_png(f'{wd}/cta.png', plat)
    cues = [(max(0, a - t0), min(dur, z - t0), tx) for a, z, tx in subs if z > t0 and a < t1]
    inputs = ['-ss', f'{t0:.2f}', '-t', f'{dur:.2f}', '-i', mp4, '-loop', '1', '-i', f'{wd}/ov.png', '-loop', '1', '-i', f'{wd}/cta.png']
    chain = (f'[0:v]split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.3[bg];'
             f'[b]scale={W}:-2[fg];[bg][fg]overlay=0:{VID_Y}[v0];[v0][1:v]overlay=0:0:shortest=1[v1];'
             f"[v1][2:v]overlay=0:0:enable='gte(t,{dur - tail:.2f})':shortest=1[v2]")
    last = 'v2'; n = 3
    for q, (a, z, tx) in enumerate(cues):
        z = min(z, dur - tail)
        if z <= a: continue
        p = f'{wd}/s{q}.png'; text_png(p, tx, 62, (255, 255, 255)); inputs += ['-loop', '1', '-i', p]
        chain += f";[{last}][{n}:v]overlay=0:0:enable='between(t,{a:.2f},{z:.2f})':shortest=1[w{q}]"; last = f'w{q}'; n += 1
    chain += f';[{last}]fade=t=in:st=0:d=0.4,fade=t=out:st={dur - 0.6:.2f}:d=0.6,format=yuv420p[vout];[0:a]afade=t=in:st=0:d=0.3,afade=t=out:st={dur - 0.7:.2f}:d=0.7[aout]'
    out = os.path.join(out_dir, f"roma_short_{k + 1}_{plat}.mp4")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', chain, '-map', '[vout]', '-map', '[aout]', '-t', f'{dur:.2f}',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-r', '30', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out], check=True)
    return out


if __name__ == '__main__':
    mp4, s_, od = sys.argv[1:4]; subs = srt(s_); os.makedirs(od, exist_ok=True)
    only = sys.argv[4] if len(sys.argv) > 4 else None
    for k, s in enumerate(SHORTS):
        if only and str(k + 1) != only: continue
        for plat in ('yt', 'ig'): print(make(mp4, subs, od, k, s, plat))
