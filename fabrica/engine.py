"""Fábrica de documentales: del manifiesto (job.json) al MP4 final.
Uso: python fabrica/engine.py jobs/<id>"""
import os, sys, json, glob, math, random, re, subprocess, shutil, traceback
from concurrent.futures import ThreadPoolExecutor
import numpy as np, librosa, soundfile as sf
from PIL import Image, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as SRC, cards as CARDS, parallax as PX

SR, FPS, W, H = 44100, 25, 1920, 1080
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LOG.append(s)

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: raise RuntimeError(' '.join(cmd[:6]) + ' :: ' + r.stderr[-600:])
    return r.stdout

def fetch(path_or_url, ext=None):
    if path_or_url.startswith('http'): return SRC.download(path_or_url, ext)
    p = path_or_url if os.path.isabs(path_or_url) else os.path.join(ROOT, path_or_url)
    return p

# ================= AUDIO =================
def load(path):
    y, _ = librosa.load(path, sr=SR, mono=False)
    if y.ndim == 1: y = np.stack([y, y])
    return y.astype(np.float32)
def rms_db(y): return 20 * np.log10(np.sqrt(np.mean(y ** 2)) + 1e-9)
def gain_to(y, db): return y * 10 ** ((db - rms_db(y)) / 20)
def fade(y, fi, fo):
    y = y.copy(); n = y.shape[1]; a = min(n, int(fi * SR)); b = min(n, int(fo * SR))
    if a: y[:, :a] *= np.linspace(0, 1, a)
    if b: y[:, n - b:] *= np.linspace(1, 0, b)
    return y
def trimv(y):
    _, (s, e) = librosa.effects.trim(y.mean(0), top_db=42)
    return y[:, max(0, s - int(.08 * SR)):min(y.shape[1], e + int(.15 * SR))]
def stretch_pauses(y):
    iv = librosa.effects.split(y.mean(0), top_db=38, frame_length=2048, hop_length=256); parts = []; prev = 0
    for a, b in iv:
        g = (a - prev) / SR; parts.append(y[:, prev:a])
        if prev > 0 and g >= 0.22: parts.append(np.zeros((2, int(min(0.75, g * 0.65) * SR)), y.dtype))
        parts.append(y[:, a:b]); prev = b
    parts.append(y[:, prev:]); return np.concatenate(parts, 1)
def loop_to(y, n, xf=2.0):
    out = y.copy(); x = int(xf * SR)
    while out.shape[1] < n:
        out = np.concatenate([out[:, :-x], out[:, -x:] * np.linspace(1, 0, x) + y[:, :x] * np.linspace(0, 1, x), y[:, x:]], 1)
    return out[:, :n]
def tempo(path, factor):
    if abs(factor - 1) < 1e-3: return path
    out = path + f'.t{factor}.wav'
    if not os.path.exists(out): sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', path, '-af', f'atempo={factor}', '-ar', str(SR), out])
    return out

def sfx_file(q, credits):
    if q.startswith('http') or q.startswith('assets/'): return fetch(q)
    c = SRC.freesound(q)
    if not c: raise RuntimeError(f'sin efecto para "{q}"')
    c = c[0]; credits.append(('sonido', c)); return SRC.download(c['url'], '.mp3')

def build_audio(job, U):
    """Coloca voces, interludios, camas y efectos. Devuelve timeline de unidades y lista de eventos de audio."""
    A = job.get('audio', {}); credits = []
    VOICE = A.get('voice_db', -20); BED = A.get('bed_db', {'tension': -35, 'batalla': -31, 'noche': -37}); INTER = A.get('inter_db', -23)
    music = {k: load(fetch(v)) for k, v in job['music'].items()}
    beds = {k: load(fetch(v)) for k, v in job.get('beds', {}).items()}; beds.update({k: v for k, v in music.items() if k not in beds})
    events, tl, bedspans = [], [], []
    t = 0.0; bed = None; bedstart = 0; used = {}; words = 0; vsec = 0
    for i, u in enumerate(U):
        k = u['k']
        if k in ('N', 'P', 'R'):
            y = gain_to(stretch_pauses(trimv(load(tempo(fetch(u['url'], '.mp3'), u.get('tempo', job.get('tempo', 0.96)))))), VOICE - (0 if k == 'N' else 1))
            events.append((int(t * SR), y)); d = y.shape[1] / SR; vsec += d
            tl.append(dict(i=i, k=k, t=round(t, 3), d=round(d, 3)))
            if k == 'N': words += len(re.sub(r'\[[^\]]*\]', '', u.get('text', '')).split())
            nxt = U[i + 1]['k'] if i + 1 < len(U) else None
            gap = 1.6 if k == 'N' else 1.1
            if nxt in ('R', 'P'): gap = 0.9
            t += d + gap
        elif k == 'B':
            if bed is not None: bedspans.append((bed, bedstart, t + 0.8))
            bed = u.get('track'); bedstart = max(0, t - 0.6)
        elif k == 'M':
            tr, secs = u['track'], u['secs']; src = music[tr]; L = src.shape[1] / SR
            if u.get('end'): o = max(0, L - secs)
            else:
                o = u.get('offset', (used.get(tr, 0) * 13.7) % max(1, L - secs - 1)); used[tr] = used.get(tr, 0) + 1
            seg = src[:, int(o * SR):int((o + secs + 1.5) * SR)]
            seg = fade(gain_to(seg, INTER), 0.05 if t == 0 else 0.8, 2.5 if u.get('end') else 1.5)
            events.append((int(max(0, t - 0.5) * SR), seg)); tl.append(dict(i=i, k='M', t=round(t, 3), d=secs)); t += secs
        elif k == 'S':
            y = fade(gain_to(load(sfx_file(u['sfx'], credits)), u.get('db', -29)), 0.3, 1.0)
            events.append((int(t * SR), y)); tl.append(dict(i=i, k='S', t=round(t, 3), d=1.2)); t += 1.2
    if bed is not None: bedspans.append((bed, bedstart, t))
    log(f'voz: {vsec/60:.1f} min, {words} palabras narrador, total {t/60:.1f} min')
    return dict(events=events, bedspans=bedspans, beds=beds, BED=BED, end=t, tl=tl, credits=credits)

def mix_audio(A, extra, out):
    N = int((A['end'] + 3) * SR); mix = np.zeros((2, N), np.float32)
    for s, y in A['events'] + extra:
        e = min(N, s + y.shape[1]);
        if e > s: mix[:, s:e] += y[:, :e - s]
    for b, s, e in A['bedspans']:
        if not b: continue
        src = A['beds'][b]; n = int((e - s) * SR)
        off = np.random.RandomState(int(s)).randint(0, max(1, src.shape[1] - SR * 5))
        src = np.concatenate([src[:, off:], src[:, :off]], 1)
        y = fade(gain_to(loop_to(src, n), A['BED'].get(b, -35)), 1.5, 2.0); a = int(s * SR); m = min(n, N - a)
        mix[:, a:a + m] += y[:, :m]
    mix /= max(1, np.abs(mix).max() / 0.95)
    sf.write(out + '.raw.wav', mix.T, SR, subtype='PCM_16')
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', out + '.raw.wav', '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '48000', '-ac', '2', out])

# ================= MATERIAL VISUAL =================
USED = set()
MUST = []
def candidates(spec, n=8, use_used=True):
    """Candidatos para un plano de vídeo o foto, filtrados por relevancia (job['must'])."""
    out = []
    def add(lst):
        for c in lst:
            if (use_used and c['id'] in USED) or any(c['id'] == x['id'] for x in out): continue
            if SRC.relevant(c, MUST if ('video' in spec and not spec.get('free')) else []): out.append(c)
    if 'video' in spec:
        q = spec['video']
        for fn in (lambda: SRC.pixabay_videos(q), lambda: SRC.pixabay_videos(q.split()[0] + ' egypt') if MUST and not spec.get('free') else [],
                   lambda: SRC.commons_search(q, video=True), lambda: SRC.archive_videos(q) if spec.get('old') else []):
            try: add(fn())
            except Exception as e: log('  aviso fuente:', q, e)
            if len(out) >= n: break
    elif 'photo' in spec:
        q = spec['photo']; order = spec.get('src', 'cleveland,met,commons,europeana').split(',')
        F = dict(cleveland=lambda: SRC.cleveland(q), met=lambda: SRC.met(q), commons=lambda: SRC.commons_search(q), europeana=lambda: SRC.europeana(q))
        for s_ in order:
            try: add(F[s_.strip()]())
            except Exception as e: log('  aviso fuente:', s_, q, e)
            if len(out) >= n: break
    return out[:n]

def use(c, credits, spec=None):
    USED.add(c['id']); credits.append(('vídeo' if c['kind'] == 'video' else 'archivo', c))
    if c['kind'] == 'video': return dict(kind='video', path=SRC.download(c['url'], '.mp4'), dur=c.get('dur', 0), old=(spec or {}).get('old'))
    return dict(kind='image', path=SRC.download(c['url'], '.jpg'), move=(spec or {}).get('move'))

def resolve(spec, need, credits, pick=None):
    """Convierte una especificación de plano en un recurso local: dict(kind, path, credit...)"""
    if pick:
        if 'spec' in pick: spec = pick['spec']
        else: return use(pick, credits, spec)
    if 'card' in spec: return dict(kind='card', card=spec['card'])
    if 'ai' in spec: return dict(kind='image', path=fetch(spec['ai'], '.jpg'), ai=True, move=spec.get('move'))
    if 'image' in spec: return dict(kind='image', path=fetch(spec['image'], '.jpg'), move=spec.get('move'))
    if 'file' in spec: p = fetch(spec['file']); return dict(kind='video' if p.endswith(('.mp4', '.webm', '.mov')) else 'image', path=p)
    if 'commons' in spec:
        c = SRC.commons_file(spec['commons']); credits.append(('archivo', c))
        return dict(kind=c['kind'], path=SRC.download(c['url']), dur=c['dur'], move=spec.get('move'))
    if 'video' in spec or 'photo' in spec:
        cands = candidates(spec, n=4)
        if not cands: raise LookupError(f'sin material relevante para "{spec.get("video") or spec.get("photo")}"')
        if 'video' in spec: cands.sort(key=lambda c: (c['dur'] < need, -min(c['w'], 1920), -c['dur']))
        return use(cands[0], credits, spec)
    raise ValueError(f'plano no reconocido: {spec}')

# ================= MONTAJE =================
def build_edl(job, U, A):
    shots = []; tl = A['tl']; pend = None
    for j, e in enumerate(tl):
        nxt = tl[j + 1]['t'] if j + 1 < len(tl) else A['end'] + 3
        t, d, i = e['t'], nxt - e['t'], e['i']
        if e['k'] == 'S': pend = (t, d); continue
        if pend: t, d = pend[0], d + pend[1]; pend = None
        specs = U[i].get('shots') or [{'card': {'type': 'title', 'title': job.get('channel', ''), 'sub': job.get('title', '')}}]
        n = len(specs)
        rep = [x for x in specs if not ('card' in x or 'ai' in x or 'commons' in x or 'image' in x or 'file' in x)]
        while d / n > 11 and rep: specs = specs + [dict(x, lt=None) for x in rep[:max(1, len(rep) // 2)]]; n = len(specs)
        while n > 1 and d / n < 3.2: specs = specs[:-1]; n -= 1
        # reparto: tarjetas y vídeo algo más largos que las imágenes IA
        wts = [1.25 if ('card' in s or 'video' in s) else (0.8 if 'ai' in s else 1.0) for s in specs]; ws = sum(wts); acc = t
        for m, (s, w) in enumerate(zip(specs, wts)):
            dd = d * w / ws
            shots.append(dict(spec=s, t=acc, d=dd, unit=i, k=e['k'], lt=s.get('lt'),
                              fadein=.8 if (e['k'] == 'M' and m == 0) else 0, fadeout=1.2 if (e['k'] == 'M' and m == n - 1) else 0))
            acc += dd
    shots[-1]['fadeout'] = 3.0
    for s in shots:
        if s['t'] < job.get('cold_secs', 60) and not ('video' in s['spec'] or 'commons' in s['spec']):
            log(f'  aviso: plano no real en el primer minuto (t={s["t"]:.0f}s): {list(s["spec"])[0]}')
    # control de la regla "nunca más de 2 IA seguidas"
    run = 0
    for s in shots:
        run = run + 1 if 'ai' in s['spec'] else 0
        if run > 2: log(f'  aviso: 3 imágenes IA seguidas en t={s["t"]:.0f}s')
    return shots

MOVES = [(1.00, 1.12, .5, .5, .5, .5), (1.12, 1.00, .5, .5, .5, .5), (1.10, 1.10, 0., 1., .5, .5), (1.10, 1.10, 1., 0., .5, .5),
         (1.04, 1.14, .2, .7, .7, .3), (1.14, 1.04, .8, .3, .3, .6), (1.0, 1.03, .5, .5, .5, .5), (1.06, 1.06, .5, .5, .9, .1)]
GRADE = 'eq=contrast=1.06:saturation=0.88:gamma=0.97,colorbalance=rs=.04:gs=.01:bs=-.04:rh=.03:bh=-.03,vignette=PI/4.4'
ENC = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-maxrate', '1.6M', '-bufsize', '3.2M', '-g', '50', '-pix_fmt', 'yuv420p', '-an']

def prep_still(path, out, BW=2880, BH=1620):
    im = Image.open(path).convert('RGB'); w, h = im.size; ar = w / h
    if 1.55 <= ar <= 2.0:
        s = max(BW / w, BH / h); im2 = im.resize((math.ceil(w * s), math.ceil(h * s)), Image.LANCZOS)
        x = (im2.width - BW) // 2; y = (im2.height - BH) // 2; c = im2.crop((x, y, x + BW, y + BH))
    else:
        s = max(BW / w, BH / h); b = im.resize((math.ceil(w * s), math.ceil(h * s)), Image.BILINEAR)
        x = (b.width - BW) // 2; y = (b.height - BH) // 2
        c = ImageEnhance.Brightness(b.crop((x, y, x + BW, y + BH)).filter(ImageFilter.GaussianBlur(50))).enhance(0.35)
        s2 = min(BW * .92 / w, BH * .92 / h); fg = im.resize((int(w * s2), int(h * s2)), Image.LANCZOS)
        c.paste(fg, ((BW - fg.width) // 2, (BH - fg.height) // 2))
    c.save(out, quality=94)

def render_shot(sh_, out, workdir):
    if os.path.exists(out): return out
    f0 = round(sh_['t'] * FPS); f1 = round((sh_['t'] + sh_['d']) * FPS); N = max(1, f1 - f0); dur = N / FPS
    R = sh_['res']; fx = []
    if sh_.get('fadein'): fx.append(f'fade=t=in:st=0:d={sh_["fadein"]}')
    if sh_.get('fadeout'): fx.append(f'fade=t=out:st={dur - sh_["fadeout"]:.3f}:d={sh_["fadeout"]}')
    if R['kind'] == 'card':
        CARDS.render_card(R['card'], dur, out, fade_in=sh_.get('fadein') or .25, fade_out=sh_.get('fadeout') or 0); return out
    if R['kind'] == 'video':
        L = R.get('dur') or float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', R['path']]).strip() or 0)
        slow = min(1.6, max(1.0, dur / max(.5, L - 1.5))) if L else 1.0
        start = max(0, min(L - dur / slow - .2, 1.0 + (L - dur / slow) * random.random() * .5)) if L else 0
        vf = f'setpts={slow:.3f}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS},' + (GRADE if not R.get('old') else 'eq=contrast=1.05') + ''.join(',' + x for x in fx)
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{start:.2f}', '-stream_loop', '-1', '-i', R['path'], '-vf', vf]
    else:
        p = f'{workdir}/prep_{os.path.basename(R["path"])}.jpg'
        if not os.path.exists(p): prep_still(R['path'], p)
        if R.get('move') != 'flat' and os.environ.get('FABRICA_25D', '1') == '1':
            gen = PX.frames(np.asarray(Image.open(p).convert('RGB')), W, H, N, sh_['move'])
            if gen is not None:
                cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                       '-vf', GRADE + ''.join(',' + x for x in fx)]
                return _encode_pipe(cmd, sh_, gen, N, out, workdir)
        z0, z1, x0, x1, y0, y1 = MOVES[sh_['move']]
        e = f'(0.5-0.5*cos(PI*(on/{max(1, N - 1)})))'
        vf = (f"zoompan=z='({z0}+({z1}-{z0})*{e})':x='(iw-iw/zoom)*({x0}+({x1}-{x0})*{e})':y='(ih-ih/zoom)*({y0}+({y1}-{y0})*{e})':d={N}:s={W}x{H}:fps={FPS},"
              + GRADE + ''.join(',' + x for x in fx))
        cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', p, '-vf', vf]
    return _encode_pipe(cmd, sh_, None, N, out, workdir)

def _encode_pipe(cmd, sh_, gen, N, out, workdir):
    if sh_.get('lt'):
        lt = f'{workdir}/lt_{abs(hash(tuple(sh_["lt"])))}.png'
        if not os.path.exists(lt): CARDS.lower_third(sh_['lt'][0], sh_['lt'][1] if len(sh_['lt']) > 1 else None, lt)
        i = cmd.index('-vf'); vf = cmd[i + 1]; del cmd[i:i + 2]
        cmd += ['-loop', '1', '-framerate', str(FPS), '-i', lt, '-filter_complex',
                f'[0:v]{vf},format=yuv420p[b];[1:v]format=rgba,fade=t=in:st=0.6:d=0.6:alpha=1,fade=t=out:st=5.2:d=0.6:alpha=1[o];[b][o]overlay=0:0:shortest=1[v]', '-map', '[v]']
    cmd += ['-frames:v', str(N), '-r', str(FPS), *ENC, out + '.tmp.mp4']
    if gen is None: sh(cmd)
    else:
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            for fr in gen: pr.stdin.write(fr.tobytes())
        except BrokenPipeError: pass
        pr.stdin.close(); err = pr.stderr.read().decode(errors='ignore'); 
        if pr.wait(): raise RuntimeError('ffmpeg 2.5D :: ' + err[-600:])
    os.rename(out + '.tmp.mp4', out); return out

def srt_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f'{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}'

# ================= CASTING =================
def _thumb(c, wd):
    from PIL import ImageOps
    try:
        if c.get('thumb'): p = SRC.download(c['thumb'], '.jpg')
        elif c['kind'] == 'image': p = SRC.download(c['url'], '.jpg')
        else:
            p = f"{wd}/th_{c['id']}.jpg"
            if not os.path.exists(p): sh(['ffmpeg', '-loglevel', 'error', '-y', '-ss', '3', '-i', c['url'], '-frames:v', '1', '-vf', 'scale=640:-1', p])
        return ImageOps.fit(Image.open(p).convert('RGB'), (384, 216))
    except Exception as e:
        log('  aviso miniatura:', c.get('id'), e); return Image.new('RGB', (384, 216), (40, 0, 0))

def cast(job, U, shots, out_dir, wd):
    """Primera pasada: candidatos por plano en hojas de miniaturas para elegir antes del render."""
    from PIL import ImageDraw, ImageFont
    log('== casting: buscando candidatos')
    F = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'corm600.ttf'), 22)
    rows = []; table = {}
    for n, s in enumerate(shots):
        sp = s['spec']
        if not any(k in sp for k in ('video', 'photo', 'commons', 'ai', 'image')): continue
        if 'commons' in sp:
            try: c = SRC.commons_file(sp['commons']); c['thumb'] = c['url'] if c['kind'] == 'image' else None; cs = [c]
            except Exception as e: cs = []; log('  aviso commons:', e)
        elif 'ai' in sp or 'image' in sp: cs = [dict(kind='image', url=sp.get('ai') or sp.get('image'), id=f'ai{n}', credit='IA')]
        else: cs = candidates(sp, n=8, use_used=False)
        table[str(n)] = cs
        txt = re.sub(r'\[[^\]]*\]', '', U[s['unit']].get('text', '') or '').strip()[:110]
        rows.append((n, s, cs, txt))
        log(f'   plano {n} t={s["t"]:.0f}s {list(sp)[0]}="{list(sp.values())[0] if isinstance(list(sp.values())[0], str) else ""}" -> {len(cs)} candidatos')
    per = 6; k = 0
    for i in range(0, len(rows), per):
        chunk = rows[i:i + per]; sheet = Image.new('RGB', (8 * 392 + 8, len(chunk) * 262 + 8), (12, 12, 12)); d = ImageDraw.Draw(sheet)
        for r, (n, s, cs, txt) in enumerate(chunk):
            y = 8 + r * 262; sp = s['spec']; q = sp.get('video') or sp.get('photo') or sp.get('commons') or 'IA'
            d.text((10, y), f'#{n}  {s["t"]:.0f}s  [{q}]  {txt}', font=F, fill=(240, 200, 120))
            for j, c in enumerate(cs[:8]):
                x = 8 + j * 392; sheet.paste(_thumb(c, wd), (x, y + 34))
                d.rectangle([x, y + 34, x + 30, y + 62], fill=(0, 0, 0)); d.text((x + 8, y + 36), str(j), font=F, fill=(255, 255, 255))
            if not cs: d.text((10, y + 120), 'SIN CANDIDATOS', font=F, fill=(255, 80, 80))
        sheet.save(f'{out_dir}/cast_{k:02d}.jpg', quality=82); k += 1
    json.dump(table, open(f'{out_dir}/cast.json', 'w'), ensure_ascii=False, indent=0)
    json.dump([dict(n=s['n'] if 'n' in s else i, t=round(s['t'], 2), d=round(s['d'], 2), unit=s['unit'], spec=s['spec']) for i, s in enumerate(shots)],
              open(f'{out_dir}/edl.json', 'w'), ensure_ascii=False, indent=0)
    log(f'FIN CASTING: {k} hojas, {len(rows)} planos con material')
    open(f'{out_dir}/informe.txt', 'w').write('\n'.join(LOG) + '\n')

# ================= PRINCIPAL =================
def run(job_dir):
    job = json.load(open(f'{job_dir}/job.json')); U = job['units']
    out_dir = f'{job_dir}/out'; wd = '/tmp/fabrica_work'; os.makedirs(out_dir, exist_ok=True); os.makedirs(f'{wd}/shots', exist_ok=True)
    random.seed(job.get('seed', 7)); credits = []; MUST[:] = job.get('must', [])
    log('== 1/5 audio: colocando voces, música y efectos')
    A = build_audio(job, U); credits += A['credits']
    log('== 2/5 guion visual'); shots = build_edl(job, U, A)
    log(f'   {len(shots)} planos')
    if job.get('stage') == 'cast': return cast(job, U, shots, out_dir, wd)
    picks = job.get('picks', {})
    log('== 3/5 buscando y descargando material')
    last = -1
    for n, s in enumerate(shots):
        try: s['res'] = resolve(s['spec'], s['d'], credits, picks.get(str(n)))
        except Exception as e:
            log(f'  ! plano {n} ({s["spec"]}) -> {e}; uso alternativa')
            alt = job.get('fallback') or [{'card': {'type': 'title', 'title': job.get('channel', ''), 'sub': job.get('title', '')}}]
            s['res'] = resolve(alt[n % len(alt)], s['d'], credits)
        mv = random.choice([m for m in range(len(MOVES)) if m != last]); s['move'] = last = mv; s['n'] = n
    # efectos automáticos: golpe de aire al entrar cada tarjeta, impacto en títulos
    extra = []
    auto = job.get('auto_sfx', {'card': 'cinematic whoosh', 'title': 'cinematic boom impact'})
    cache = {}
    def sfx(q, db):
        if q not in cache: cache[q] = gain_to(load(sfx_file(q, credits)), db)
        return cache[q]
    for s in shots:
        if s['res']['kind'] == 'card' and s['t'] > 1:
            q = auto['title'] if s['res']['card']['type'] == 'title' else auto['card']
            try: y = sfx(q, -27 if 'boom' in q else -31); extra.append((int(max(0, s['t'] - 0.25) * SR), fade(y[:, :int(3 * SR)], 0.02, 0.8)))
            except Exception as e: log('  aviso sfx auto:', e)
    log('== 4/5 mezcla final de audio'); mix_audio(A, extra, f'{wd}/doc.wav')
    log('== 4/5 renderizando planos')
    with ThreadPoolExecutor(int(os.environ.get('FABRICA_THREADS', '2'))) as ex:
        futs = [ex.submit(render_shot, s, f'{wd}/shots/{s["n"]:04d}.mp4', wd) for s in shots]
        for k, f in enumerate(futs):
            f.result()
            if k % 20 == 0: log(f'   plano {k}/{len(shots)}')
    log('== 5/5 montaje final')
    # trozos: [intro] + doc partido por inserciones
    inserts = sorted(job.get('inserts', []), key=lambda x: x['after_unit'])
    cuts = []
    for ins in inserts:
        e = next(x for x in A['tl'] if x['i'] == ins['after_unit']); cuts.append((e['t'] + e['d'], fetch(ins['file'])))
    bounds = [0] + [c[0] for c in cuts] + [A['end'] + 3]
    pieces = [fetch(p) for p in job.get('intro', [])]
    for k in range(len(bounds) - 1):
        a, b = bounds[k], bounds[k + 1]; fa, fb = round(a * FPS), round(b * FPS)
        lst = f'{wd}/part{k}.txt'
        open(lst, 'w').write(''.join(f"file '{wd}/shots/{s['n']:04d}.mp4'\n" for s in shots if fa <= round(s['t'] * FPS) < fb))
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{wd}/v{k}.mp4'])
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', f'{wd}/v{k}.mp4', '-ss', f'{fa / FPS:.3f}', '-t', f'{(fb - fa) / FPS:.3f}', '-i', f'{wd}/doc.wav',
            '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2', '-shortest', f'{wd}/m{k}.mp4'])
        pieces.append(f'{wd}/m{k}.mp4')
        if k < len(cuts): pieces.append(cuts[k][1])
    norm = []
    for k, p in enumerate(pieces):  # piezas externas: mismas características que el doc
        if p.startswith(wd): norm.append(p); continue
        q = f'{wd}/ext{k}.mp4'
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', p, '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p',
            '-c:v', 'libx264', '-preset', 'medium', '-crf', '22', '-g', '50', '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2', q]); norm.append(q)
    open(f'{wd}/final.txt', 'w').write(''.join(f"file '{p}'\n" for p in norm))
    final = f'{out_dir}/{job["id"]}.mp4'
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{wd}/final.txt', '-c', 'copy', '-movflags', '+faststart', final])
    # desplazamientos de tiempo por intro e inserciones (para subtítulos y capítulos)
    def dur(p): return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).strip())
    intro_d = sum(dur(fetch(p)) for p in job.get('intro', [])); ins_d = [dur(c[1]) for c in cuts]
    def T(x): return x + intro_d + sum(d for (c, _), d in zip(cuts, ins_d) if x >= c)
    # subtítulos
    srt = []; n = 1
    for e in A['tl']:
        u = U[e['i']]
        if e['k'] not in ('N', 'P', 'R') or not u.get('text'): continue
        txt = re.sub(r'\[[^\]]*\]', '', u['text']); sents = [s.strip() for s in re.split(r'(?<=[.!?…])\s+', txt.replace('\n', ' ')) if s.strip()]
        tot = sum(len(s) for s in sents); a = e['t']
        for s_ in sents:
            b = a + e['d'] * len(s_) / tot
            for chunk in [s_[i:i + 84] for i in range(0, len(s_), 84)] if len(s_) > 84 else [s_]:
                srt.append(f'{n}\n{srt_time(T(a))} --> {srt_time(T(b))}\n{chunk}\n'); n += 1
            a = b
    open(f'{out_dir}/{job["id"]}.srt', 'w').write('\n'.join(srt))
    ch = ['0:00 Introducción'] + [f"{int(T(next(x for x in A['tl'] if x['i'] == c['unit'])['t']) // 60)}:{int(T(next(x for x in A['tl'] if x['i'] == c['unit'])['t']) % 60):02d} {c['title']}" for c in job.get('chapters', [])]
    open(f'{out_dir}/capitulos.txt', 'w').write('\n'.join(ch) + '\n')
    seen = set(); cr = []
    for kind, c in credits:
        if c['id'] in seen: continue
        seen.add(c['id']); cr.append(f"- [{kind}] {c.get('credit','')} · {c.get('license','')} · {c.get('page','')}")
    open(f'{out_dir}/creditos.txt', 'w').write('Material de archivo y sonido (licencias abiertas):\n' + '\n'.join(cr) + '\n')
    # hoja de control: un fotograma cada ~25 s
    D = dur(final); k = 0
    for x in np.linspace(3, D - 3, 24):
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{x:.1f}', '-i', final, '-frames:v', '1', '-vf', 'scale=480:-1', f'{wd}/c{k:02d}.jpg']); k += 1
    ims = [Image.open(f'{wd}/c{i:02d}.jpg') for i in range(k)]; w_, h_ = ims[0].size
    sheet = Image.new('RGB', (w_ * 4, h_ * 6))
    for i, im in enumerate(ims): sheet.paste(im, ((i % 4) * w_, (i // 4) * h_))
    sheet.save(f'{out_dir}/control.jpg', quality=80)
    json.dump([dict(n=s['n'], t=round(s['t'], 2), d=round(s['d'], 2), unit=s['unit'], spec=s['spec']) for s in shots], open(f'{out_dir}/edl.json', 'w'), ensure_ascii=False, indent=0)
    log(f'FIN: {final} · {D/60:.1f} min · {os.path.getsize(final)/1e6:.0f} MB')
    open(f'{out_dir}/informe.txt', 'w').write('\n'.join(LOG) + '\n')

if __name__ == '__main__':
    try: run(sys.argv[1])
    except Exception:
        traceback.print_exc(); os.makedirs(f'{sys.argv[1]}/out', exist_ok=True)
        open(f'{sys.argv[1]}/out/informe.txt', 'w').write('\n'.join(LOG) + '\n\nERROR:\n' + traceback.format_exc()); sys.exit(1)
