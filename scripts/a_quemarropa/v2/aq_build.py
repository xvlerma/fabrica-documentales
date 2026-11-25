"""Motor de montaje v1 de «A quemarropa · Pedro Sánchez» (ETAPA 1).
Fila del EDL -> plan de segmento -> render (H.264 CRF 18 veryfast + PCM) -> concat -> mezcla con música provisional."""
import json, re, os, sys, subprocess, glob, math, hashlib
sys.path.insert(0, '/home/claude/w'); sys.path.insert(0, '/home/claude/w/aq')
import wt
import aqgfx2 as G
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

AQ = '/home/claude/w/aq'; B = '/mnt/user-data/uploads/Pedro Sánchez, a fondo/'
SEG = AQ + '/seg'; PNG = AQ + '/png'; os.makedirs(SEG, exist_ok=True); os.makedirs(PNG, exist_ok=True)
FPS = 25; W, H = 1920, 1080
ROWS = json.load(open(AQ + '/edl.json'))
RES = {d['n']: d for d in json.load(open(AQ + '/resolved.json'))}
NAR = {d[0]: d for d in json.load(open(AQ + '/nar_rep.json'))}
FX = json.load(open(AQ + '/clipfx.json'))
STT = {}
for f in glob.glob(AQ + '/stt_out/*.json') + glob.glob(AQ + '/stt_out2/*.json'):
    STT[os.path.basename(f).replace('.mp3.json', '')] = json.load(open(f))
def full_words(path):
    b = os.path.basename(path); k = 'F_' + b.rsplit('.', 1)[0]
    if k in STT: return [(a, bb, w.strip()) for s_ in STT[k] for a, bb, w in s_['w']]
    return wt.words(b)
def lit_tokens(lit):
    t = re.sub(r'\b[A-ZÁÉÍÓÚÑ]{3,}:\s*', ' ', lit); t = re.sub(r'\[[^\]]*\]|\(.*?\)', ' ', t)
    return [wt.nz(x) for x in t.split() if wt.nz(x)]
def align(words, lit, lo=0, hi=1e9):
    tk = lit_tokens(lit)
    if len(tk) < 1 or not words: return None
    Wn = [(a, b, wt.nz(w)) for a, b, w in words if lo <= a <= hi]
    head = tk[:4]; tail = tk[-4:]
    def eq(a, b): return a == b or (len(a) >= 5 and len(b) >= 5 and a[:5] == b[:5])
    def score(i, pat):
        seg = [x[2] for x in Wn[i:i + len(pat) + 2]]
        return sum(1 for p in pat if any(eq(p, q) for q in seg))
    best = max(range(len(Wn)), key=lambda i: (score(i, head), -i), default=None)
    if best is None or score(best, head) < min(2, len(head)): return None
    i0 = best
    while i0 + 1 < len(Wn) and Wn[i0][2] != head[0] and Wn[i0 + 1][2] in head[:2]: i0 += 1
    if Wn[i0][2] != head[0]:
        for j in range(best, min(best + 3, len(Wn))):
            if Wn[j][2] == head[0]: i0 = j; break
    span = len(tk); cands = []
    for back, lastw in enumerate(reversed(tail)):
        cands = [j for j in range(i0, min(len(Wn), i0 + int(span * 1.6) + 6)) if eq(Wn[j][2], lastw)]
        if cands: span -= back; break
    if not cands: return None
    j = min(cands, key=lambda j: abs((j - i0 + 1) - span))
    return Wn[i0][0], Wn[j][1]
INC = []   # incidencias
TCLOG = [] # recortes / TC corregidos
def inc(n, msg): INC.append((n, msg))

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: raise RuntimeError(' '.join(map(str, cmd))[-600:] + '\n' + r.stderr[-1500:])
    return r.stdout
_PR = {}
def probe(p):
    if p not in _PR:
        j = json.loads(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,width,height', '-of', 'json', p]))
        v = [s for s in j['streams'] if s['codec_type'] == 'video']
        _PR[p] = dict(dur=float(j['format'].get('duration', 0) or 0), w=v[0].get('width', 0) if v else 0, h=v[0].get('height', 0) if v else 0,
                      audio=any(s['codec_type'] == 'audio' for s in j['streams']))
    return _PR[p]

ALLF = [os.path.join(r, f) for r, ds, fs in os.walk(B) for f in fs if f.lower().endswith(('.mp4', '.png', '.jpg', '.jpeg', '.mkv', '.webm'))]
ALIAS = {'14_25_wild_project__(ext)s.mp4': 'cortes_externos/14b_wild_corto__(ext)s.mp4'}
def findf(ref):
    ref = ref.strip().lstrip('(')
    if os.path.basename(ref) in ALIAS: ref = ALIAS[os.path.basename(ref)]
    if os.path.basename(ref) == 'docuvox.mp4': return '/home/claude/fabrica-documentales/assets/intro/docuvox.mp4'
    b = os.path.basename(ref); stem = b.rsplit('.', 1)[0]
    sub = ref.rsplit('/', 1)[0] if '/' in ref else ''
    for alt in ([b] + ([] if b.startswith('clip_') else ['clip_' + b])):
        c = [p for p in ALLF if os.path.basename(p) == alt]
        if sub: c = sorted(c, key=lambda p: ('/' + sub + '/') not in p)
        if c: return c[0]
    c = [p for p in ALLF if os.path.basename(p).startswith(stem)]
    return c[0] if c else None

def clean(t):
    t = t or ''
    t = re.sub(r'\s*·?\s*verif\..*$', '', t)
    t = re.sub(r'\[#[^\]]*\]', '', t); t = re.sub(r'\[v\d[^\]]*\]', '', t); t = re.sub(r'\(⚠️[^)]*\)|\(❓[^)]*\)|\(✅[^)]*\)|\(🔁[^)]*\)', '', t)
    t = re.sub(r'\s+·\s*v3\b', '', t)
    t = re.sub(r'\s+', ' ', t).strip(' ·')
    return '' if t in ('—', '-', '–') else t

def png(img, key):
    p = f'{PNG}/{key}.png'
    img.save(p); return p

def secs(s):
    s = (s or '').strip().replace(',', '.')
    if s in ('—', '', '-'): return None
    v = 0
    for x in s.split(':'): v = v * 60 + float(x)
    return v

# ---------------------------------------------------------------- STT y ajuste a palabra
def stt_words(n, k):
    key = f'r{n:03d}_{k}'
    if key not in STT:
        src = (RES.get(n) or {}).get('src') or []
        return full_words(src[k][0]) if k < len(src) else None
    meta = json.load(open(f'{AQ}/sttin/{key}.mp3.json'))
    off = meta['a']
    return [(a + off, b + off, w.strip()) for s in STT[key] for a, b, w in s['w']]

def snap(n, k, path, ss, to, note, lit=''):
    """No cortar ninguna palabra: el literal se localiza en el STT del tramo; entrada antes de su primera palabra,
    salida con cola de ≈0,25 s (o la cola corta de la fila) sin dejar entrar la palabra siguiente."""
    tail = 0.25
    m = re.search(r'Cola corta \(([\d.]+) s\)', note)
    if m: tail = max(0.04, float(m.group(1)))
    Wd = stt_words(n, k)
    if not Wd: return ss, to, 'sin STT: TC del EDL'
    tk = lit_tokens(lit)
    if not tk: return ss, to, 'sin literal: TC del EDL'
    Wn = [(a, b, wt.nz(w)) for a, b, w in Wd]
    def eq(a, b): return a == b or (len(a) >= 5 and len(b) >= 5 and a[:5] == b[:5])
    win = [i for i, x in enumerate(Wn) if ss - 1.6 <= x[0] <= to + 1.0]
    if not win: return ss, to, 'STT sin palabras en el tramo: TC del EDL'
    # primera palabra del literal cerca de la entrada
    fi = None
    for h in tk[:3]:
        c = [i for i in win if eq(Wn[i][2], h) and abs(Wn[i][0] - ss) < 1.6]
        if c: fi = min(c, key=lambda i: abs(Wn[i][0] - ss)); break
    li = None
    for t in reversed(tk[-3:]):
        c = [i for i in win if eq(Wn[i][2], t) and abs(Wn[i][1] - to) < 1.6 and (fi is None or i >= fi)]
        if c: li = min(c, key=lambda i: abs(Wn[i][1] - to)); break
    how = []
    if fi is not None:
        a, b, _ = Wn[fi]; ss2 = max(a - 0.08, min(ss, b - 0.25), 0)
        if fi > 0 and Wn[fi - 1][1] > ss2 + 0.05: ss2 = max(ss2, Wn[fi - 1][1] - 0.02)
        ss = round(ss2, 2); how.append('entrada a palabra')
    else: how.append('entrada del EDL (STT no reconoce la primera palabra)')
    if li is not None:
        a, b, _ = Wn[li]; to2 = b + tail
        if li + 1 < len(Wn): to2 = min(to2, max(b + 0.04, Wn[li + 1][0] - 0.04))
        to = round(to2, 2); how.append('salida a palabra + cola')
    else: how.append('salida del EDL (STT no reconoce la última palabra)')
    return ss, to, 'STT: ' + ', '.join(how)

def subs_for(n, k, ss, to, shift):
    Wd = stt_words(n, k)
    if not Wd: return []
    ws = [x for x in Wd if x[0] >= ss - 0.05 and x[1] <= to + 0.1]
    out = []; cur = []
    for x in ws:
        cur.append(x)
        if len(cur) >= 7 or x[2].endswith(('.', '?', '!', '…')):
            out.append(cur); cur = []
    if cur: out.append(cur)
    res = []
    for c in out:
        a = c[0][0] - ss + shift; b = c[-1][1] - ss + shift + 0.25
        res.append((max(0, a), b, ' '.join(w for _, _, w in c)))
    for i in range(len(res) - 1):
        if res[i][1] > res[i + 1][0]: res[i] = (res[i][0], res[i + 1][0], res[i][2])
    return res

# ---------------------------------------------------------------- cobertura de faldones
def fx_for(path, ss):
    b = os.path.basename(path)
    best = None
    for f in FX:
        if f['src'] == b and (f['to'] is None or (ss or 0) < f['to']) and (ss or 0) >= (f['ss'] or 0) - 30: best = f
    return best

LETTERBOX = [(0, 0, W, 132), (0, H - 132, W, H)]

# ---------------------------------------------------------------- piezas
def P_clip(path, ss, dur, src_len=None, crop=None, blur=0, z=0.0, fade_dark=False):
    return dict(t='clip', path=path, ss=ss, dur=dur, len=src_len or dur, crop=crop, blur=blur, z=z, dark=fade_dark)
def P_img(p, dur, z=0.04, blur=0, fade_dark=False): return dict(t='img', path=p, dur=dur, z=z, blur=blur, dark=fade_dark)
def P_black(dur): return dict(t='black', dur=dur)
def P_wave(path, ss, dur): return dict(t='wave', path=path, ss=ss, dur=dur)

def frame_at(path, t, key, sat=1.0, dark=1.0, blur=0, crop=None):
    p = f'{PNG}/{key}.png'
    if not os.path.exists(p):
        if path.lower().endswith(('.jpg', '.png', '.jpeg')): im = Image.open(path).convert('RGB')
        else:
            d = probe(path)['dur']; t = max(0, min(t, d - 0.2))
            tmp = f'{PNG}/{key}_raw.png'
            cf = f'crop={crop},' if crop else ''
            sh(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', path, '-frames:v', '1', '-vf', f'{cf}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', tmp])
            im = Image.open(tmp).convert('RGB')
        if im.size != (W, H):
            r = max(W / im.width, H / im.height); im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1)); ox = (im.width - W) // 2; oy = (im.height - H) // 2
            im = im.crop((ox, oy, ox + W, oy + H))
        if sat != 1.0: im = ImageEnhance.Color(im).enhance(sat)
        if dark != 1.0: im = ImageEnhance.Brightness(im).enhance(dark)
        if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
        im.save(p)
    return p

def capture_png(path, key, blur=0, maxw=0.85):
    p = f'{PNG}/cap_{key}.png'
    if not os.path.exists(p):
        im = G.capture_frame(path, maxw)
        if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
        im.convert('RGB').save(p)
    return p

def card(img, key):
    p = f'{PNG}/card_{key}.png'
    img.convert('RGB').save(p); return p

# ---------------------------------------------------------------- gráficos transparentes extra
def d1ov(text):
    im = G.canvas(); d = ImageDraw.Draw(im)
    for y in range(H // 2, H):
        a = int(210 * (y - H / 2) / (H / 2)); d.line((0, y, W, y), fill=(0, 0, 0, a))
    s, L = G.fit(d, text, 'disp_xb', [120, 104, 92, 80], W - 2 * G.MX, 2)
    f = G.F('disp_xb', s); y = H - 120 - len(L) * int(s * 1.05)
    for l in L: d.text((G.MX, y), l, font=f, fill=G.YEL); y += int(s * 1.05)
    return im

def wave_bg():
    im = G.canvas((0x0B, 0x0B, 0x0B)); return im

# ---------------------------------------------------------------- render de un segmento
def render(seg):
    n = seg['n']; D = round(seg['D'] * FPS) / FPS
    out = f'{SEG}/s{n:03d}.mov'
    hs = hashlib.md5(json.dumps(seg, sort_keys=True, default=str).encode())
    for p in seg['pieces']:
        if p['t'] == 'img' and os.path.exists(p['path']): hs.update(hashlib.md5(open(p['path'], 'rb').read()).digest())
    for o in seg['ov']:
        if os.path.exists(o[0]): hs.update(hashlib.md5(open(o[0], 'rb').read()).digest())
    sig = hs.hexdigest()[:10]
    if os.path.exists(out) and os.path.exists(out + '.sig') and open(out + '.sig').read() == sig: return out
    inputs = []; ch = []; idx = 0; labs = []
    for k, p in enumerate(seg['pieces']):
        d = p['dur']
        if p['t'] == 'clip':
            pr = probe(p['path']); ss = p['ss'] or 0
            if pr['dur'] and ss > pr['dur'] - 0.4: ss = max(0, pr['dur'] - p['len'] - 0.4)
            L = min(p['len'], d, max(0.2, pr['dur'] - ss)) if pr['dur'] else min(p['len'], d)
            inputs += ['-ss', f'{ss:.3f}', '-t', f'{L + 0.1:.3f}', '-i', p['path']]
            cf = f"crop={p['crop']}," if p.get('crop') else ''
            bl = f",gblur=sigma={p['blur']}" if p.get('blur') else ''
            if pr['w'] and pr['h'] and pr['h'] > pr['w'] * 1.05:
                ch.append(f"[{idx}:v]{cf}fps={FPS},split[ba{k}][fa{k}];[ba{k}]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=30,eq=brightness=-0.2[bb{k}];"
                          f"[fa{k}]scale=-2:{H}{bl}[ff{k}];[bb{k}][ff{k}]overlay=(W-w)/2:0,setsar=1,format=yuv420p,tpad=stop_mode=clone:stop_duration={d + 1:.2f},trim=duration={d:.3f},setpts=PTS-STARTPTS[p{k}]")
            else:
                zz = f",scale=w='{W}*(1+{p['z']}*t/{d:.3f})':h=-2:eval=frame,crop={W}:{H}" if p.get('z') else ''
                dk = f",fade=t=out:st={max(0, d - 1.6):.2f}:d=1.5" if p.get('dark') else ''
                ch.append(f"[{idx}:v]{cf}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}{bl},format=yuv420p,tpad=stop_mode=clone:stop_duration={d + 1:.2f},trim=duration={d:.3f},setpts=PTS-STARTPTS{zz}{dk}[p{k}]")
            idx += 1
        elif p['t'] == 'img':
            inputs += ['-loop', '1', '-framerate', str(FPS), '-t', f'{d + 0.2:.3f}', '-i', p['path']]
            zz = f",scale=w='{W}*(1+{p['z']}*t/{d:.3f})':h=-2:eval=frame,crop={W}:{H}" if p.get('z') else ''
            bl = f",gblur=sigma={p['blur']}" if p.get('blur') else ''
            dk = f",fade=t=out:st={max(0, d - 1.6):.2f}:d=1.5" if p.get('dark') else ''
            ch.append(f"[{idx}:v]scale={W}:{H},setsar=1,fps={FPS},format=yuv420p{zz}{bl}{dk},trim=duration={d:.3f},setpts=PTS-STARTPTS[p{k}]")
            idx += 1
        elif p['t'] == 'black':
            inputs += ['-f', 'lavfi', '-t', f'{d:.3f}', '-i', f'color=c=black:s={W}x{H}:r={FPS}']
            ch.append(f"[{idx}:v]format=yuv420p,setsar=1,trim=duration={d:.3f},setpts=PTS-STARTPTS[p{k}]"); idx += 1
        elif p['t'] == 'wave':
            inputs += ['-ss', f"{p['ss']:.3f}", '-t', f'{d:.3f}', '-i', p['path']]; ia = idx; idx += 1
            inputs += ['-f', 'lavfi', '-t', f'{d:.3f}', '-i', f'color=c=0x0B0B0B:s={W}x{H}:r={FPS}']; ib = idx; idx += 1
            ch.append(f"[{ia}:a]aformat=channel_layouts=mono,showwaves=s=1500x340:mode=cline:rate={FPS}:colors=0xF2FF00:scale=sqrt,format=rgba[wv{k}];"
                      f"[{ib}:v][wv{k}]overlay=(W-w)/2:(H-h)/2-60:shortest=1,format=yuv420p,setsar=1,tpad=stop_mode=clone:stop_duration=1,trim=duration={d:.3f},setpts=PTS-STARTPTS[p{k}]")
        labs.append(f'[p{k}]')
    if len(labs) > 1: ch.append(''.join(labs) + f'concat=n={len(labs)}:v=1:a=0[base]')
    else: ch.append(f'{labs[0]}null[base]')
    cur = 'base'
    for q, (pp, a, b, fade) in enumerate(seg['ov']):
        inputs += ['-loop', '1', '-framerate', str(FPS), '-t', f'{D:.3f}', '-i', pp]
        b = min(b, D)
        if fade: ch.append(f"[{idx}:v]format=rgba,fade=t=in:st={a:.2f}:d=0.32:alpha=1,fade=t=out:st={max(a, b - 0.24):.2f}:d=0.24:alpha=1[o{q}]")
        else: ch.append(f"[{idx}:v]format=rgba[o{q}]")
        en = '' if (a <= 0.01 and b >= D - 0.01) or fade else f":enable='between(t,{a:.2f},{b:.2f})'"
        ch.append(f'[{cur}][o{q}]overlay=0:0:shortest=1{en}[v{q}]'); cur = f'v{q}'; idx += 1
    ch.append(f'[{cur}]format=yuv420p[vout]')
    # audio
    alabs = []; t0 = 0.0
    for k, a in enumerate(seg['audio']):
        if a['t'] == 'clip':
            if not probe(a['path'])['audio']: inc(n, f'sin pista de audio: {os.path.basename(a["path"])}'); continue
            inputs += ['-ss', f"{a['ss']:.3f}", '-t', f"{a['dur']:.3f}", '-i', a['path']]
            dist = ',asetrate=48000*0.78,aresample=48000,atempo=1.282,aecho=0.6:0.5:18:0.3' if a.get('distort') else ''
            for (ba, bb) in a.get('beeps', []): dist += f",volume=enable='between(t,{ba:.2f},{bb:.2f})':volume=0" 
            nr = ',afftdn=nf=-28,highpass=f=110,lowpass=f=7500,acompressor=threshold=-24dB:ratio=3:attack=10:release=200' if a.get('wave') else ''
            ch.append(f"[{idx}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,highpass=f=70{nr}{dist},loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,"
                      f"afade=t=in:d=0.015,afade=t=out:st={max(0, a['dur'] - 0.045):.3f}:d=0.04,adelay={int(a.get('at', t0) * 1000)}:all=1[a{k}]")
            t0 = a.get('at', t0) + a['dur']
        elif a['t'] == 'wav':
            inputs += ['-i', a['path']]
            ch.append(f"[{idx}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,adelay={int(a.get('at', 0) * 1000)}:all=1[a{k}]")
        elif a['t'] == 'raw':
            inputs += ['-i', a['path']]
            ch.append(f"[{idx}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[a{k}]")
        alabs.append(f'[a{k}]'); idx += 1
        for q, (ba, bb) in enumerate(a.get('beeps', []) if a['t'] == 'clip' else []):
            inputs += ['-f', 'lavfi', '-t', f'{bb - ba:.3f}', '-i', 'sine=frequency=1000:sample_rate=48000']
            ch.append(f"[{idx}:a]aformat=sample_fmts=fltp:channel_layouts=stereo,volume=-14dB,afade=t=in:d=0.01,afade=t=out:st={max(0, bb - ba - 0.01):.3f}:d=0.01,adelay={int((a.get('at', 0) + ba) * 1000)}:all=1[bp{k}_{q}]")
            alabs.append(f'[bp{k}_{q}]'); idx += 1
    if alabs:
        mix = ''.join(alabs) + (f'amix=inputs={len(alabs)}:normalize=0:duration=longest,' if len(alabs) > 1 else '')
        ch.append(f"{mix}apad,atrim=0:{D:.3f}[aout]" if len(alabs) > 1 else f"{alabs[0]}apad,atrim=0:{D:.3f}[aout]")
    else:
        inputs += ['-f', 'lavfi', '-t', f'{D:.3f}', '-i', 'anullsrc=r=48000:cl=stereo']; ch.append(f'[{idx}:a]atrim=0:{D:.3f}[aout]'); idx += 1
    cmd = ['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(ch), '-map', '[vout]', '-map', '[aout]',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-g', '50', '-threads', '2',
           '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', '-frames:v', str(int(round(D * FPS))), '-t', f'{D:.3f}', out]
    sh(cmd); open(out + '.sig', 'w').write(sig)
    return out
