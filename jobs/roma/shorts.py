#!/usr/bin/env python3
"""Shorts verticales 1080x1920 a partir del documental montado.
Uso: python3 shorts.py <mp4> <srt> <carpeta_salida>
Cada short: fondo del propio plano desenfocado, vídeo 16:9 centrado, logo, gancho arriba (blanco + caja amarilla),
subtítulos grandes en mayúsculas y «DOCUMENTAL COMPLETO EN EL CANAL» los últimos 6 s."""
import json, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

KIT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'brand')
W, H, Y = 1080, 1920, (242, 255, 0)
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


def overlay_png(path, hook1, hook2):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    logo = Image.open(f'{KIT}/DocuVox_Logo_Horizontal_Amarillo-Blanco.png').convert('RGBA'); lw = 300
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS); im.paste(logo, ((W - lw) // 2, 120), logo)
    f1 = F('Black', 104); y = 300
    for ln in wrap(d, hook1.upper(), f1, 960):
        tw = d.textlength(ln, font=f1); d.text(((W - tw) / 2 + 4, y + 4), ln, font=f1, fill=(0, 0, 0)); d.text(((W - tw) / 2, y), ln, font=f1, fill=(255, 255, 255)); y += 110
    f2 = F('Black', 92); tw = d.textlength(hook2.upper(), font=f2); bb = d.textbbox((0, 0), hook2.upper(), font=f2)
    d.rectangle([(W - tw) / 2 - 24, y + 14, (W + tw) / 2 + 24, y + 14 + bb[3] - bb[1] + 40], fill=Y)
    d.text(((W - tw) / 2, y + 34 - bb[1]), hook2.upper(), font=f2, fill=(10, 10, 10))
    im.save(path)


def text_png(path, text, size, color, box=None, ypos=1420):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F('ExtraBold', size); y = ypos
    for ln in wrap(d, text.upper(), f, 980)[:3]:
        tw = d.textlength(ln, font=f)
        if box: d.rectangle([(W - tw) / 2 - 18, y - 6, (W + tw) / 2 + 18, y + size + 10], fill=box)
        for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3), (3, 3)):
            if not box: d.text(((W - tw) / 2 + dx, y + dy), ln, font=f, fill=(0, 0, 0))
        d.text(((W - tw) / 2, y), ln, font=f, fill=color); y += size + 14
    im.save(path)


def make(mp4, subs, out_dir, k, s):
    t0, t1 = s['start'], s['end']; dur = t1 - t0; wd = os.path.join(out_dir, f'tmp{k}'); os.makedirs(wd, exist_ok=True)
    overlay_png(f'{wd}/ov.png', s['hook1'], s['hook2'])
    text_png(f'{wd}/cta.png', 'Documental completo en el canal', 70, (10, 10, 10), box=Y, ypos=1660)
    cues = [(max(0, a - t0), min(dur, z - t0), tx) for a, z, tx in subs if z > t0 and a < t1]
    inputs = ['-ss', f'{t0:.2f}', '-t', f'{dur:.2f}', '-i', mp4, '-loop', '1', '-i', f'{wd}/ov.png', '-loop', '1', '-i', f'{wd}/cta.png']
    chain = (f'[0:v]split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.25[bg];'
             f'[b]scale={W}:-2[fg];[bg][fg]overlay=0:(H-h)/2-40[v0];[v0][1:v]overlay=0:0:shortest=1[v1];'
             f"[v1][2:v]overlay=0:0:enable='gte(t,{dur - 6:.2f})':shortest=1[v2]")
    last = 'v2'; n = 3
    for q, (a, z, tx) in enumerate(cues):
        p = f'{wd}/s{q}.png'; text_png(p, tx, 64, (255, 255, 255)); inputs += ['-loop', '1', '-i', p]
        chain += f";[{last}][{n}:v]overlay=0:0:enable='between(t,{a:.2f},{z:.2f})':shortest=1[w{q}]"; last = f'w{q}'; n += 1
    chain += f';[{last}]fade=t=in:st=0:d=0.4,fade=t=out:st={dur - 0.6:.2f}:d=0.6,format=yuv420p[vout];[0:a]afade=t=in:st=0:d=0.3,afade=t=out:st={dur - 0.7:.2f}:d=0.7[aout]'
    out = os.path.join(out_dir, f"roma_short_{k + 1}.mp4")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', chain, '-map', '[vout]', '-map', '[aout]', '-t', f'{dur:.2f}',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-r', '30', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out], check=True)
    return out


if __name__ == '__main__':
    mp4, s_, od = sys.argv[1:4]; subs = srt(s_); os.makedirs(od, exist_ok=True)
    for k, s in enumerate(SHORTS):
        print(make(mp4, subs, od, k, s))
