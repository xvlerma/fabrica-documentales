"""Fábrica de documentales: del manifiesto (job.json) al MP4 final.
Uso: python fabrica/engine.py jobs/<id>"""
import os, sys, json, glob, math, random, re, subprocess, shutil, traceback
from concurrent.futures import ThreadPoolExecutor
import numpy as np, librosa, soundfile as sf
from PIL import Image, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as SRC, cards as CARDS, parallax as PX, align as AL

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
PAUSE = dict(k=0.65, cap=0.75)
def stretch_pauses(y):
    if PAUSE['k'] <= 0: return y
    iv = librosa.effects.split(y.mean(0), top_db=38, frame_length=2048, hop_length=256); parts = []; prev = 0
    for a, b in iv:
        g = (a - prev) / SR; parts.append(y[:, prev:a])
        if prev > 0 and g >= 0.22: parts.append(np.zeros((2, int(min(PAUSE['cap'], g * PAUSE['k']) * SR)), y.dtype))
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

MUSIC_PATHS = {}
def music_file(v, credits, name=''):
    """Pista de música: URL o ruta, {"url", "credit", "license", "page"}, {"incompetech": "Título"}
    o {"search": "...", "src": "archive,commons,openverse,freesound", "pick": n}."""
    if isinstance(v, str): p = fetch(v, '.mp3')
    elif 'incompetech' in v: c = SRC.incompetech(v['incompetech']); credits.append(('música', c)); p = SRC.download(c['url'], '.mp3')
    elif 'search' in v:
        cs = SRC.music_search(v['search'], v.get('src', 'archive,commons,openverse,freesound'), n=8)
        cs = [c for c in cs if not c.get('dur') or c['dur'] >= v.get('min_secs', 50)] or cs
        if not cs: raise LookupError(f'sin música libre para "{v["search"]}"')
        c = cs[min(v.get('pick', 0), len(cs) - 1)]; credits.append(('música', c)); p = SRC.download(c['url'], os.path.splitext(c['url'].split('?')[0])[1] or '.mp3')
    else:
        p = fetch(v['url'], '.mp3')
        if v.get('credit'): credits.append(('música', dict(id=v['url'], credit=v['credit'], license=v.get('license', ''), page=v.get('page', v['url']))))
    if v.__class__ is dict and v.get('start'):  # recorte de una pieza larga (segundos)
        q = p + f'.{v["start"]}_{v.get("secs", 0)}.wav'
        if not os.path.exists(q): sh(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(v['start']), *(['-t', str(v['secs'])] if v.get('secs') else []), '-i', p, '-ar', str(SR), q])
        p = q
    MUSIC_PATHS[name] = p; return p

def build_audio(job, U):
    """Coloca voces, interludios, camas y efectos. Devuelve timeline de unidades y lista de eventos de audio."""
    A = job.get('audio', {}); credits = []
    PAUSE.update(k=A.get('pause_stretch', 0.65), cap=A.get('pause_cap', 0.75)); GAP_N = A.get('gap_n', 1.6); GAP_Q = A.get('gap_q', 1.1)
    VOICE = A.get('voice_db', -20); BED = A.get('bed_db', {'tension': -35, 'batalla': -31, 'noche': -37}); INTER = A.get('inter_db', -23)
    def ld(k, v):
        try: return load(music_file(v, credits, k))
        except Exception as e:
            if job.get('stage') != 'cast': raise
            log(f'  aviso música {k}: {e} (silencio en el casting)'); return np.zeros((2, SR * 90), np.float32)
    music = {k: ld(k, v) for k, v in job['music'].items()}
    beds = {k: ld(k, v) for k, v in job.get('beds', {}).items()}; beds.update({k: v for k, v in music.items() if k not in beds})
    events, tl, bedspans = [], [], []; VY = {}
    def voice(u):
        if not u.get('url'):  # casting sin voz todavía: silencio estimado por longitud del texto
            return np.zeros((2, int(SR * max(2, len(re.sub(r'\[[^\]]*\]', '', u.get('text', ''))) / 14.5))), np.float32) + 1e-6, False
        src = fetch(u['url'], '.mp3')
        if u.get('clip'):  # v3.1: voz empaquetada en un solo archivo; cada unidad es un tramo [inicio, duración]
            a_, d_ = u['clip']; cp = f"{src}.c{a_:.3f}_{d_:.3f}.wav"
            if not os.path.exists(cp): sh(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{a_:.3f}', '-t', f'{d_:.3f}', '-i', src, '-ar', str(SR), cp])
            src = cp
        return gain_to(stretch_pauses(trimv(load(tempo(src, u.get('tempo', job.get('tempo', 0.96)))))), VOICE - (0 if u['k'] in ('N', 'T') else 1)), True
    t = 0.0; bed = None; bedstart = 0; used = {}; words = 0; vsec = 0
    for i, u in enumerate(U):
        k = u['k']
        if k in ('N', 'P', 'R'):
            y, real = voice(u); VY[i] = (y, real)
            events.append((int(t * SR), y)); d = y.shape[1] / SR; vsec += d
            tl.append(dict(i=i, k=k, t=round(t, 3), d=round(d, 3)))
            if k == 'N': words += len(re.sub(r'\[[^\]]*\]', '', u.get('text', '')).split())
            nxt = U[i + 1]['k'] if i + 1 < len(U) else None
            gap = u.get('gap', GAP_N if k == 'N' else GAP_Q)
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
        elif k == 'T':  # título o capítulo con pausa propia: golpe de música, tarjeta y (opcional) el narrador diciéndolo
            secs = u.get('secs', 4.5); va = u.get('voice_at', 0.7)
            if u.get('url') or u.get('text'):
                y, real = voice(u); VY[i] = (y, real); events.append((int((t + va) * SR), y)); secs = max(secs, va + y.shape[1] / SR + 1.0)
            if u.get('sting') and u['sting'] in music:
                src = music[u['sting']]; o = u.get('offset', 0); seg = src[:, int(o * SR):int((o + secs + 1.5) * SR)]
                events.append((int(t * SR), fade(gain_to(seg, INTER + u.get('sting_db', 0)), 0.05, 1.6)))
            tl.append(dict(i=i, k='T', t=round(t, 3), d=secs, va=va)); t += secs
        elif k == 'S':
            y = fade(gain_to(load(sfx_file(u['sfx'], credits)), u.get('db', -29)), 0.3, 1.0)
            events.append((int(t * SR), y)); tl.append(dict(i=i, k='S', t=round(t, 3), d=1.2)); t += 1.2
    if bed is not None: bedspans.append((bed, bedstart, t))
    log(f'voz: {vsec/60:.1f} min, {words} palabras narrador, total {t/60:.1f} min')
    return dict(events=events, bedspans=bedspans, beds=beds, BED=BED, end=t, tl=tl, credits=credits, VY=VY)

def align_audio(job, U, A, job_dir, out_dir):
    """Marca de tiempo de cada palabra del guion (absoluta en la línea de tiempo). Se guarda en align.json."""
    pre = {}
    if os.path.exists(f'{job_dir}/align.json'): pre = json.load(open(f'{job_dir}/align.json'))
    words = {}; model = job.get('align_model', 'base'); n_wh = 0
    for e in A['tl']:
        i = e['i']; u = U[i]
        if i not in A['VY'] or not u.get('text'): continue
        y, real = A['VY'][i]; off = e['t'] + (e.get('va', 0) if e['k'] == 'T' else 0)
        key = f"{i}:{u.get('url', '')[-40:]}"
        if str(i) in pre and pre[str(i)].get('key') == key: ws = pre[str(i)]['words']
        elif real and job.get('align', False): ws = AL.align_unit(u['text'], y, SR, model, SRC.CACHE); n_wh += 1
        else: ws = AL.proportional(u['text'], y.shape[1] / SR)
        words[i] = dict(key=key, off=off, words=ws)
    json.dump({str(k): dict(key=v['key'], words=v['words']) for k, v in words.items()}, open(f'{out_dir}/align.json', 'w'), ensure_ascii=False)
    log(f'   alineación: {len(words)} unidades ({n_wh} con whisper, resto en caché o proporcional)')
    A['words'] = words
    A['allw'] = [x[1:] for x in sorted([((v['off'] + w['t'], q), v['off'] + w['t'], w['w'], w['n']) for v in words.values() for q, w in enumerate(v['words'])])]

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
        for fn in (lambda: SRC.pixabay_videos(q), lambda: SRC.pixabay_videos(q.split()[0] + ' ' + MUST[0]) if MUST and not spec.get('free') else [],
                   lambda: SRC.commons_search(q, video=True), lambda: SRC.archive_videos(q) if spec.get('old') else []):
            try: add(fn())
            except Exception as e: log('  aviso fuente:', q, e)
            if len(out) >= n: break
    elif 'photo' in spec:
        q = spec['photo']; order = spec.get('src', 'cleveland,met,commons,europeana').split(',')
        F = dict(cleveland=lambda: SRC.cleveland(q), met=lambda: SRC.met(q), commons=lambda: SRC.commons_search(q), europeana=lambda: SRC.europeana(q), openverse=lambda: SRC.openverse_images(q))
        for s_ in order:
            try: add(F[s_.strip()]())
            except Exception as e: log('  aviso fuente:', s_, q, e)
            if len(out) >= n: break
    return out[:n]

def qkey(spec): return ('video:' + spec['video']) if 'video' in spec else ('photo:' + spec['photo'])

def use(c, credits, spec=None):
    USED.add(c['id']); credits.append(('vídeo' if c['kind'] == 'video' else 'archivo', c))
    if c['kind'] == 'video': return dict(kind='video', path=SRC.download(c['url'], '.mp4'), dur=c.get('dur', 0), old=(spec or {}).get('old'))
    return dict(kind='image', path=SRC.download(c['url'], '.jpg'), move=(spec or {}).get('move'))

USES = {}; REUSE = dict(max=2, gap=600)
def resolve(spec, need, credits, pick=None, t=0.0):
    """Convierte una especificación de plano en un recurso local: dict(kind, path, credit...)"""
    if pick:
        if 'spec' in pick: spec = pick['spec']
        else: return use(pick, credits, spec)
    if 'card' in spec:
        c = json.loads(json.dumps(spec['card']))
        def walk(o):
            if isinstance(o, dict):
                if o.get('commons'):
                    m = SRC.commons_file(o['commons']); credits.append(('archivo', m)); o['_path'] = SRC.download(m['url'], '.jpg')
                elif o.get('image'): o['_path'] = fetch(o['image'], '.jpg')
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(c)
        return dict(kind='card', card=c)
    if 'ai' in spec: return dict(kind='image', path=fetch(spec['ai'], '.jpg'), ai=True, move=spec.get('move'))
    if 'image' in spec: return dict(kind='image', path=fetch(spec['image'], '.jpg'), move=spec.get('move'))
    if 'file' in spec: p = fetch(spec['file']); return dict(kind='video' if p.endswith(('.mp4', '.webm', '.mov')) else 'image', path=p)
    if 'commons' in spec:
        c = SRC.commons_file(spec['commons']); credits.append(('archivo', c))
        return dict(kind=c['kind'], path=SRC.download(c['url']), dur=c['dur'], move=spec.get('move'))
    if 'video' in spec or 'photo' in spec:
        key = qkey(spec)
        if QPICKS.get(key):
            lst = QPICKS[key]; i = QPOS.get(key, 0); QPOS[key] = i + 1
            order = [lst[(i + o) % len(lst)] for o in range(len(lst))]
            ok = [c for c in order if len(USES.get(c.get('id'), [])) < REUSE['max'] and all(abs(t - x) >= REUSE['gap'] for x in USES.get(c.get('id'), []))]
            c = ok[0] if ok else min(order, key=lambda c: len(USES.get(c.get('id'), [])))
            if not ok: log(f'  aviso repetición: "{key}" en t={t:.0f}s reutiliza un recurso ({len(USES.get(c.get("id"), [])) + 1}.ª vez); añade candidatos')
            USES.setdefault(c.get('id'), []).append(t)
            return use(c, credits, spec)
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
        while not job.get('no_pad') and d / n > (3.4 if t < job.get('cold_secs', 60) else 6.0) and rep: specs = specs + [dict(x, lt=None) for x in rep[:max(1, len(rep) // 2)]]; n = len(specs)
        while n > 1 and d / n < (1.6 if t < job.get('cold_secs', 60) else 2.6): specs = specs[:-1]; n -= 1
        # reparto: tarjetas y vídeo algo más largos que las imágenes IA
        wts = [1.25 if ('card' in s or 'video' in s) else (0.8 if 'ai' in s else 1.0) for s in specs]; ws = sum(wts); acc = t
        for m, (s, w) in enumerate(zip(specs, wts)):
            dd = d * w / ws
            shots.append(dict(spec=s, t=acc, d=dd, unit=i, k=e['k'], lt=s.get('lt'), tr_in=s.get('tr'),
                              fadein=.8 if (e['k'] == 'M' and m == 0) else 0, fadeout=1.2 if (e['k'] == 'M' and m == n - 1) else 0))
            acc += dd
    shots[-1]['fadeout'] = 3.0
    for a_, b_ in zip(shots, shots[1:]):
        if b_.get('tr_in'): a_['tr_out'] = b_['tr_in']
    for s in shots:
        if s['t'] < job.get('cold_secs', 60) and not ('video' in s['spec'] or 'commons' in s['spec']):
            log(f'  aviso: plano no real en el primer minuto (t={s["t"]:.0f}s): {list(s["spec"])[0]}')
    # control de la regla "nunca más de 2 IA seguidas"
    run = 0
    for s in shots:
        run = run + 1 if 'ai' in s['spec'] else 0
        if run > 2: log(f'  aviso: 3 imágenes IA seguidas en t={s["t"]:.0f}s')
    return shots

def build_edl_sync(job, U, A):
    """Montaje anclado a la palabra: cada plano con "at" empieza 0,3 s antes de esa palabra; los demás se reparten
    entre anclas. Sin relleno por repetición (no_pad). Los títulos van en unidades T con pausa propia."""
    tl = A['tl']; W_ = A.get('words', {}); lead = job.get('anchor_lead', 0.1); items = []; pend = None
    for j, e in enumerate(tl):
        nxt = tl[j + 1]['t'] if j + 1 < len(tl) else A['end'] + 3
        t, d, i = e['t'], nxt - e['t'], e['i']
        if e['k'] == 'S': pend = (t, d); continue
        if pend: t, d = pend[0], d + pend[1]; pend = None
        u = U[i]
        if e['k'] == 'T': specs = u.get('shots') or [dict(card=u.get('card') or {'type': 'title', 'title': job.get('title', '')}, tr=u.get('tr'))]
        else: specs = u.get('shots') or [{'card': {'type': 'title', 'title': job.get('channel', ''), 'sub': job.get('title', '')}}]
        wu = W_.get(i); pos = 0
        for m, s in enumerate(specs):
            at = None
            if s.get('at') and wu:
                k_ = AL.find(wu['words'], s['at'], pos)
                if k_ is None: log(f'  aviso ancla no encontrada (unidad {i}): "{s["at"]}"')
                else: pos = k_ + 1; at = max(t, wu['off'] + wu['words'][k_]['t'] - lead)
            if m == 0 and at is None: at = t
            items.append(dict(spec=s, t=at, unit=i, k=e['k'], ustart=t, uend=t + d, m=m, n_in=len(specs)))
    if items: items[0]['t'] = 0.0
    # reparte los planos sin ancla entre las anclas conocidas
    known = [k for k, it in enumerate(items) if it['t'] is not None] + [len(items)]
    for a_, b_ in zip(known, known[1:]):
        ta = items[a_]['t']; tb = items[b_]['t'] if b_ < len(items) else A['end'] + 3
        free = list(range(a_ + 1, b_))
        if not free: continue
        # los planos sin ancla no cruzan su unidad: reparte dentro de [ta, min(tb, fin de unidad)]
        for q, k in enumerate(free):
            items[k]['t'] = ta + (min(tb, items[k]['uend']) - ta) * (q + 1) / (len(free) + 1) if items[k]['m'] > 0 else items[k]['ustart']
    MIN = job.get('min_shot', 1.2)
    for k in range(1, len(items)):
        if items[k]['t'] < items[k - 1]['t'] + MIN:
            if items[k]['spec'].get('at'): log(f'  aviso anclas muy juntas en t={items[k]["t"]:.1f}s: se retrasa "{items[k]["spec"]["at"]}"')
            items[k]['t'] = items[k - 1]['t'] + MIN
    shots = []
    for k, it in enumerate(items):
        end = items[k + 1]['t'] if k + 1 < len(items) else A['end'] + 3
        s = it['spec']; d = end - it['t']
        if d <= 0.2: log(f'  aviso plano descartado por falta de hueco: {list(s)[0]}'); continue
        shots.append(dict(spec=s, t=it['t'], d=d, unit=it['unit'], k=it['k'], lt=s.get('lt'), tr_in=s.get('tr'),
                          fadein=.8 if (it['k'] == 'M' and it['m'] == 0) else 0, fadeout=1.2 if (it['k'] == 'M' and it['m'] == it['n_in'] - 1) else 0))
    shots[-1]['fadeout'] = 3.0
    for a_, b_ in zip(shots, shots[1:]):
        if b_.get('tr_in'): a_['tr_out'] = b_['tr_in']
    allw = A.get('allw', [])
    for s in shots:
        g = s['spec'].get('gloss_on')
        if g:
            q = [n for _, n in AL.tokens(g)]
            hit = next((tw for k_, (tw, _, n_) in enumerate(allw) if s['t'] - 0.3 <= tw < s['t'] + s['d'] and [x[2] for x in allw[k_:k_ + len(q)]] == q), None)
            if hit is not None: s['spec'] = dict(s['spec'], gloss_at=round(max(0.2, hit - s['t'] - 0.1), 2))
    # glosario del episodio: la primera vez que se nombra cada término, su chip aparece en el plano que está en pantalla
    for gl in job.get('glossary', []):
        q = [n for _, n in AL.tokens(gl.get('on', gl['term']))]
        hit = next((allw[k_][0] for k_ in range(len(allw)) if [x[2] for x in allw[k_:k_ + len(q)]] == q), None)
        if hit is None: log(f'  aviso glosario: no se nombra "{gl["term"]}"'); continue
        k_ = next((k for k, s in enumerate(shots) if s['t'] <= hit < s['t'] + s['d']), None)
        if k_ is None: continue
        if shots[k_]['t'] + shots[k_]['d'] - hit < 2.2 and k_ + 1 < len(shots): k_ += 1; at = 0.2
        else: at = max(0.2, hit - shots[k_]['t'] - 0.1)
        if shots[k_]['spec'].get('gloss') or 'card' in shots[k_]['spec']: log(f'  aviso glosario: "{gl["term"]}" cae en una tarjeta u otro glosario'); continue
        shots[k_]['spec'] = dict(shots[k_]['spec'], gloss=[gl['term'], gl['def']] + ([gl['bando']] if gl.get('bando') else []), gloss_at=round(at, 2),
                                 gloss_dur=min(4.5, shots[k_]['d'] - at - 0.3))
    for s in shots:
        s['heard'] = ' '.join(w for (tw, w, _) in allw if s['t'] - 0.2 <= tw < s['t'] + s['d'])
    sync_report(job, shots, allw)
    return shots

SYNC = []
def sync_report(job, shots, allw):
    """Avisos de sincronía: persona o lugar sin mención cerca, títulos con voz debajo, planos demasiado largos."""
    SYNC.clear(); maxd = job.get('max_shot', 8.0)
    for n, s in enumerate(shots):
        sp = s['spec']; near = {nn for (tw, _, nn) in allw if s['t'] - 2 <= tw <= s['t'] + s['d'] + 2}
        if s.get('lt'):
            toks = [AL.norm(x) for x in re.split(r'[\s\-]+', s['lt'][0]) if len(AL.norm(x)) > 3]
            if toks and not any(tk in near for tk in toks): SYNC.append(f'plano {n} t={s["t"]:.1f}s: rótulo "{s["lt"][0]}" sin mención en ±2 s')
        if 'card' in sp and sp['card'].get('type') == 'title' and s['k'] not in ('T', 'M') and not sp.get('at'):
            SYNC.append(f'plano {n} t={s["t"]:.1f}s: título dentro de una unidad de voz (usa una unidad T)')
        if s['d'] > maxd and 'card' not in sp: SYNC.append(f'plano {n} t={s["t"]:.1f}s: dura {s["d"]:.1f} s; añade un plano o una tarjeta')
    for x in SYNC: log('  sincronía:', x)

MOVES = [(1.00, 1.12, .5, .5, .5, .5), (1.12, 1.00, .5, .5, .5, .5), (1.10, 1.10, 0., 1., .5, .5), (1.10, 1.10, 1., 0., .5, .5),
         (1.04, 1.14, .2, .7, .7, .3), (1.14, 1.04, .8, .3, .3, .6), (1.0, 1.03, .5, .5, .5, .5), (1.06, 1.06, .5, .5, .9, .1)]
GRADES = dict(
    calido='eq=contrast=1.06:saturation=0.88:gamma=0.97,colorbalance=rs=.04:gs=.01:bs=-.04:rh=.03:bh=-.03,vignette=PI/4.4',
    frio='eq=contrast=1.08:saturation=0.78:gamma=0.97,colorbalance=rs=-.03:gs=0:bs=.04:rh=-.01:bh=.02,vignette=PI/4.4',
    neutro='eq=contrast=1.05:saturation=0.86:gamma=0.98,vignette=PI/4.6',
    bn='hue=s=0,eq=contrast=1.14:gamma=0.96,vignette=PI/4.2',
    sepia='hue=s=0,eq=contrast=1.08:gamma=0.97,colorchannelmixer=.95:.05:0:0:.85:.1:0:0:.7:.1:.05:0,vignette=PI/4.4')
GRADE = GRADES['calido']
BRAND = {}
BANDO = {}
ENC_H264 = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-maxrate', '1.6M', '-bufsize', '3.2M', '-g', '50', '-pix_fmt', 'yuv420p', '-an']
def enc_hevc(kbps): return ['-c:v', 'libx265', '-preset', 'fast', '-crf', '25', '-x265-params', f'vbv-maxrate={kbps}:vbv-bufsize={kbps * 2}:keyint=50:log-level=error', '-tag:v', 'hvc1', '-pix_fmt', 'yuv420p', '-an']
ENC = list(ENC_H264); ABR = '128k'
QPICKS = {}; QPOS = {}

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

OVERLAYS = {}
def render_shot(sh_, out, workdir):
    if os.path.exists(out): return out
    f0 = round(sh_['t'] * FPS); f1 = round((sh_['t'] + sh_['d']) * FPS); N = max(1, f1 - f0); dur = N / FPS
    R = sh_['res']; sp = sh_['spec']; fx = []
    # transiciones: destello (salto en el tiempo) o negro (cliffhanger); fundidos de entrada/salida
    if sh_.get('tr_in') == 'flash': fx.append('fade=t=in:st=0:d=0.35:color=white')
    elif sh_.get('tr_in') == 'black': fx.append('fade=t=in:st=0:d=0.3')
    elif sh_.get('fadein'): fx.append(f'fade=t=in:st=0:d={sh_["fadein"]}')
    if sh_.get('tr_out') == 'flash': fx.append(f'fade=t=out:st={dur - .18:.3f}:d=0.18:color=white')
    elif sh_.get('tr_out') == 'black': fx.append(f'fade=t=out:st={dur - .45:.3f}:d=0.45')
    elif sh_.get('fadeout'): fx.append(f'fade=t=out:st={dur - sh_["fadeout"]:.3f}:d={sh_["fadeout"]}')
    gen = None
    if R['kind'] == 'card':
        tmp = out + '.card.mp4'
        if not os.path.exists(tmp): CARDS.render_card(R['card'], dur, tmp, fade_in=0, fade_out=0)
        base = ['-i', tmp]; vf = 'null'
    elif R['kind'] == 'video':
        L = R.get('dur') or float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', R['path']]).strip() or 0)
        slow = min(1.6, max(1.0, dur / max(.5, L - 1.5))) if L else 1.0
        start = max(0, min(L - dur / slow - .2, 1.0 + (L - dur / slow) * random.random() * .5)) if L else 0
        base = ['-ss', f'{start:.2f}', '-stream_loop', '-1', '-i', R['path']]
        crop = sp.get('crop')  # recorte de franjas negras de origen: [x, y, w, h] relativos
        cf = f'crop=iw*{crop[2]}:ih*{crop[3]}:iw*{crop[0]}:ih*{crop[1]},' if crop else 'cropdetect=limit=24:round=2:reset=0,' if False else ''
        vf = f'setpts={slow:.3f}*PTS,{cf}scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS},' + (GRADE if not R.get('old') else 'eq=contrast=1.05')
    else:
        p = f'{workdir}/prep_{os.path.basename(R["path"])}.jpg'
        if not os.path.exists(p): prep_still(R['path'], p)
        rgb = np.asarray(Image.open(p).convert('RGB'))
        if R.get('ai'):
            rgb = PX.film_treatment(rgb, dark=sp.get('dark', .9), soften=.45, seed=sh_['n'])
            pfx = dict(shake=1, flicker=sp.get('fire', 1), focus=sp.get('focus', (.85, .25)), seed=sh_['n'])
        else:
            pfx = dict(shake=sp.get('shake', .35), flicker=sp.get('fire', 0), focus=sp.get('focus'), seed=sh_['n'])
        if R.get('move') != 'flat' and os.environ.get('FABRICA_25D', '1') == '1':
            gen = PX.frames(rgb, W, H, N, sh_['move'], FPS, pfx)
        if gen is not None:
            base = ['-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']; vf = GRADE
        else:
            if R.get('ai'): Image.fromarray(rgb).save(p + '.ai.jpg', quality=94); p = p + '.ai.jpg'
            z0, z1, x0, x1, y0, y1 = MOVES[sh_['move'] % len(MOVES)]
            e = f'(0.5-0.5*cos(PI*(on/{max(1, N - 1)})))'
            base = ['-loop', '1', '-framerate', str(FPS), '-i', p]
            vf = (f"zoompan=z='({z0}+({z1}-{z0})*{e})':x='(iw-iw/zoom)*({x0}+({x1}-{x0})*{e})':y='(ih-ih/zoom)*({y0}+({y1}-{y0})*{e})':d={N}:s={W}x{H}:fps={FPS}," + GRADE)
    # capas superpuestas: humo/polvo real (pantalla), rótulo inferior, palabra clave
    ins = []; chain = f'[0:v]{vf},format=yuv420p[b0]'; last = 'b0'; k = 1
    ov = sp.get('ov', 'dust' if R.get('ai') else None)
    if ov and OVERLAYS.get(ov):
        ins += ['-stream_loop', '-1', '-i', OVERLAYS[ov]]
        chain += f';[{k}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},hue=s=0,curves=all=0/0 0.35/0 1/0.9,format=gbrp[o{k}];[{last}]format=gbrp[g{k}];[g{k}][o{k}]blend=all_mode=screen:all_opacity={sp.get("ov_op", .4)}:shortest=1,format=yuv420p[b{k}]'
        last = f'b{k}'; k += 1
    if sh_.get('lt'):
        lt = f'{workdir}/lt_{abs(hash(tuple(sh_["lt"])))}.png'
        col = BANDO.get(sh_['lt'][2]) if len(sh_['lt']) > 2 else None
        if not os.path.exists(lt): CARDS.lower_third(sh_['lt'][0], sh_['lt'][1] if len(sh_['lt']) > 1 else None, lt, color=col)
        ins += ['-loop', '1', '-framerate', str(FPS), '-i', lt]; la = sp.get('lt_at', 0.35)
        chain += f';[{k}:v]format=rgba,fade=t=in:st={la}:d=0.45:alpha=1,fade=t=out:st={max(la + 1, min(la + 4.8, dur - .6)):.2f}:d=0.5:alpha=1[o{k}];[{last}][o{k}]overlay=0:0:shortest=1[b{k}]'
        last = f'b{k}'; k += 1
    if sp.get('gloss'):  # glosario: chip arriba a la izquierda con la sigla y su traducción a lenguaje de hoy
        g = sp['gloss']; gp = f'{workdir}/gl_{abs(hash(tuple(g)))}.png'
        if not os.path.exists(gp): CARDS.gloss(g[0], g[1] if len(g) > 1 else '', gp, color=BANDO.get(g[2]) if len(g) > 2 else None)
        g0 = sp.get('gloss_at', 0.3); g1 = min(dur - .3, g0 + sp.get('gloss_dur', 4.5))
        ins += ['-loop', '1', '-framerate', str(FPS), '-i', gp]
        chain += f';[{k}:v]format=rgba,fade=t=in:st={g0}:d=0.35:alpha=1,fade=t=out:st={max(g0 + .5, g1 - .4):.2f}:d=0.4:alpha=1[o{k}];[{last}][o{k}]overlay=0:0:shortest=1[b{k}]'
        last = f'b{k}'; k += 1
    if sp.get('kw'):
        kp = f'{workdir}/kw_{abs(hash(sp["kw"]))}.png'
        if not os.path.exists(kp): CARDS.keyword(sp['kw'], kp)
        a0 = sp.get('kw_at', .3); a1 = min(dur - .2, a0 + sp.get('kw_dur', 1.8))
        ins += ['-loop', '1', '-framerate', str(FPS), '-i', kp]
        chain += f';[{k}:v]format=rgba,fade=t=in:st={a0}:d=0.12:alpha=1,fade=t=out:st={a1 - .3:.2f}:d=0.3:alpha=1[o{k}];[{last}][o{k}]overlay=0:0:shortest=1[b{k}]'
        last = f'b{k}'; k += 1
    if BRAND.get('mosca') and R['kind'] != 'card':
        ins += ['-loop', '1', '-framerate', str(FPS), '-i', BRAND['mosca']]
        chain += f';[{last}][{k}:v]overlay=0:0:shortest=1[b{k}]'; last = f'b{k}'; k += 1
    chain += f';[{last}]' + (','.join(fx) if fx else 'null') + '[v]'
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', *base, *ins, '-filter_complex', chain, '-map', '[v]', '-frames:v', str(N), '-r', str(FPS), *ENC, out + '.tmp.mp4']
    if gen is None: sh(cmd)
    else:
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            for fr in gen: pr.stdin.write(fr.tobytes())
        except BrokenPipeError: pass
        pr.stdin.close(); err = pr.stderr.read().decode(errors='ignore')
        if pr.wait(): raise RuntimeError('ffmpeg 2.5D :: ' + err[-600:])
    os.rename(out + '.tmp.mp4', out); return out

def outro(job, shots, wd):
    """Pantalla final DocuVox (fondo para elementos de YouTube) con la cola de la música del episodio."""
    secs = job.get('brand', {}).get('outro_secs', 15)
    bgp = next((s['res']['path'] for s in reversed(shots) if s['res']['kind'] == 'image' and not s['res'].get('ai')), None)
    png = f'{wd}/outro.png'; CARDS.end_screen(png, bgp)
    tr = job.get('brand', {}).get('outro_track') or next(iter(job['music']))
    src = MUSIC_PATHS.get(tr); out = f'{wd}/outro.mp4'
    a = (['-sseof', f'-{secs + 2}', '-i', src] if src else ['-f', 'lavfi', '-t', str(secs), '-i', 'anullsrc=r=48000:cl=stereo'])
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', png, *a, '-t', str(secs),
        '-vf', f'fade=t=in:st=0:d=0.8,fade=t=out:st={secs - 1.2}:d=1.2,format=yuv420p',
        '-af', f'loudnorm=I=-24:TP=-3,afade=t=in:st=0:d=1.5,afade=t=out:st={secs - 3}:d=3', '-map', '0:v', '-map', '1:a',
        *[x for x in ENC if x != '-an'], '-r', str(FPS), '-c:a', 'aac', '-b:a', ABR, '-ar', '48000', '-ac', '2', out])
    return out

def sync_sheets(shots, wd, out_dir):
    """Control de concordancia: cada plano de persona, lugar o documento junto a lo que se oye mientras sale."""
    from PIL import ImageDraw, ImageFont
    F = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'corm600.ttf'), 20)
    sel = [s for s in shots if s['spec'].get('at') or s.get('lt') or 'photo' in s['spec'] or 'commons' in s['spec'] or s['spec'].get('gloss')]
    per = 12
    for k in range(0, len(sel), per):
        ch = sel[k:k + per]; sheet = Image.new('RGB', (3 * 640, ((len(ch) + 2) // 3) * 440), (12, 12, 12)); d = ImageDraw.Draw(sheet)
        for j, s in enumerate(ch):
            x, y = (j % 3) * 640, (j // 3) * 440; p = f'{wd}/shots/{s["n"]:04d}.mp4'; im = f'{wd}/sy_{s["n"]}.jpg'
            try:
                sh(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{min(1.6, s["d"] / 2):.2f}', '-i', p, '-frames:v', '1', '-vf', 'scale=620:-1', im])
                sheet.paste(Image.open(im), (x + 10, y + 10))
            except Exception: d.text((x + 20, y + 120), 'sin fotograma', font=F, fill=(255, 80, 80))
            tag = s['spec'].get('at') or (s.get('lt') or [''])[0] or s['spec'].get('photo') or s['spec'].get('commons') or ''
            d.text((x + 12, y + 360), f'#{s["n"]} {s["t"]:.1f}s · {tag}'[:60], font=F, fill=(240, 200, 120))
            hd = s.get('heard', '')
            d.text((x + 12, y + 386), ('«' + hd[:58]), font=F, fill=(200, 230, 255)); d.text((x + 12, y + 410), (hd[58:116] + '»'), font=F, fill=(200, 230, 255))
        sheet.save(f'{out_dir}/sincronia_{k // per:02d}.jpg', quality=78)
    log(f'   hojas de sincronía: {(len(sel) + per - 1) // per}')

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
    rows = []; table = {}; seenq = {}; qtab = {}
    for n, s in enumerate(shots):
        sp = s['spec']
        if not any(k in sp for k in ('video', 'photo', 'commons', 'ai', 'image')): continue
        if 'commons' in sp:
            try: c = SRC.commons_file(sp['commons']); c['thumb'] = c['url'] if c['kind'] == 'image' else None; cs = [c]
            except Exception as e: cs = []; log('  aviso commons:', e)
        elif 'ai' in sp or 'image' in sp: cs = [dict(kind='image', url=sp.get('ai') or sp.get('image'), id=f'ai{n}', credit='IA')]
        else:
            key = qkey(sp)
            if key in seenq: seenq[key] += 1; continue
            seenq[key] = 1; pre = [dict(c, elegido=True) for c in QPICKS.get(key, [])]
            cs = (pre + [c for c in (candidates(sp, n=8 - len(pre), use_used=False) if len(pre) < 8 else []) if c['id'] not in {x.get('id') for x in pre}])[:8]; qtab[key] = cs
        table[str(n)] = cs
        txt = (s.get('heard') or re.sub(r'\[[^\]]*\]', '', U[s['unit']].get('text', '') or '')).strip()[:120]
        rows.append((n, s, cs, txt))
        log(f'   plano {n} t={s["t"]:.0f}s {list(sp)[0]}="{list(sp.values())[0] if isinstance(list(sp.values())[0], str) else ""}" -> {len(cs)} candidatos')
    per = 6; k = 0
    for i in range(0, len(rows), per):
        chunk = rows[i:i + per]; sheet = Image.new('RGB', (8 * 392 + 8, len(chunk) * 292 + 8), (12, 12, 12)); d = ImageDraw.Draw(sheet)
        for r, (n, s, cs, txt) in enumerate(chunk):
            y = 8 + r * 292; sp = s['spec']; q = sp.get('video') or sp.get('photo') or sp.get('commons') or 'IA'
            kq = qkey(sp) if ('video' in sp or 'photo' in sp) else None
            d.text((10, y), (f'#{n} {s["t"]:.0f}s  {kq}  ·  usado {seenq.get(kq, 1)} veces' if kq else f'#{n}  {s["t"]:.0f}s  [{q}]')[:150], font=F, fill=(240, 200, 120))
            d.text((10, y + 236), ('«' + txt + '»')[:170], font=F, fill=(200, 230, 255))
            for j, c in enumerate(cs[:8]):
                x = 8 + j * 392; sheet.paste(_thumb(c, wd), (x, y + 34))
                d.rectangle([x, y + 34, x + 30, y + 62], fill=(0, 0, 0)); d.text((x + 8, y + 36), str(j), font=F, fill=(255, 255, 255))
                if c.get('elegido'): d.rectangle([x, y + 34, x + 383, y + 249], outline=(242, 255, 0), width=4)
            if not cs: d.text((10, y + 120), 'SIN CANDIDATOS', font=F, fill=(255, 80, 80))
        sheet.save(f'{out_dir}/cast_{k:02d}.jpg', quality=82); k += 1
    json.dump(table, open(f'{out_dir}/cast.json', 'w'), ensure_ascii=False, indent=0)
    json.dump(qtab, open(f'{out_dir}/castq.json', 'w'), ensure_ascii=False, indent=0)
    open(f'{out_dir}/castq_uso.txt', 'w').write('\n'.join(f'{v}x  {k}' for k, v in seenq.items()))
    json.dump([dict(n=s['n'] if 'n' in s else i, t=round(s['t'], 2), d=round(s['d'], 2), unit=s['unit'], heard=s.get('heard', ''), spec=s['spec']) for i, s in enumerate(shots)],
              open(f'{out_dir}/edl.json', 'w'), ensure_ascii=False, indent=0)
    cast_music(job, out_dir, F)
    log(f'FIN CASTING: {k} hojas, {len(rows)} planos con material')
    open(f'{out_dir}/informe.txt', 'w').write('\n'.join(LOG) + '\n')

def cast_music(job, out_dir, F):
    """Candidatos de música libre por pista con búsqueda: espectrograma + energía para elegir "pick" a ojo."""
    from PIL import ImageDraw
    tab = {}; rows = []
    for name, v in list(job.get('music', {}).items()) + list(job.get('beds', {}).items()):
        if not (isinstance(v, dict) and 'search' in v): continue
        cs = SRC.music_search(v['search'], v.get('src', 'archive,commons,openverse,freesound'), n=8)
        cs = [c for c in cs if not c.get('dur') or c['dur'] >= v.get('min_secs', 50)] or cs
        tab[name] = cs[:12]
        for j, c in enumerate(cs[:12]):
            try:
                pth = SRC.download(c['url'], os.path.splitext(c['url'].split('?')[0])[1] or '.mp3')
                y, sr_ = librosa.load(pth, sr=22050, mono=True, duration=150)
                S = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=1024, hop_length=512)), ref=np.max)
                im = Image.fromarray((np.clip((S[:300][::-1] + 80) / 80, 0, 1) * 255).astype('uint8')).resize((900, 110))
                rms = librosa.feature.rms(y=y)[0]; c['dur'] = c.get('dur') or len(y) / sr_
                c['energia'] = [round(float(x), 3) for x in np.interp(np.linspace(0, len(rms) - 1, 30), np.arange(len(rms)), rms)]
                c['tempo'] = float(np.atleast_1d(librosa.beat.beat_track(y=y, sr=sr_)[0])[0])
                rows.append((name, j, c, im))
            except Exception as e: log('  aviso música candidata', c.get('id'), e)
    if not tab: return
    json.dump(tab, open(f'{out_dir}/musica.json', 'w'), ensure_ascii=False, indent=0)
    sheet = Image.new('RGB', (1400, 40 + 150 * len(rows)), (12, 12, 12)); d = ImageDraw.Draw(sheet)
    for i, (name, j, c, im) in enumerate(rows):
        y0 = 20 + i * 150
        d.text((10, y0), f'{name} · pick {j} · {c.get("dur", 0):.0f}s · ~{c.get("tempo", 0):.0f} bpm · {c.get("license","")}', font=F, fill=(240, 200, 120))
        d.text((10, y0 + 26), f'{c.get("title","")[:90]} — {c.get("credit","")[:40]}', font=F, fill=(200, 200, 200))
        sheet.paste(im.convert('RGB'), (10, y0 + 52))
        e = c.get('energia', []); mx = max(e or [1]) or 1
        for q in range(len(e) - 1): d.line([(930 + q * 15, y0 + 150 - 90 * e[q] / mx), (930 + (q + 1) * 15, y0 + 150 - 90 * e[q + 1] / mx)], fill=(120, 220, 235), width=2)
    sheet.save(f'{out_dir}/musica.jpg', quality=82); log(f'   música: {len(rows)} candidatas en musica.jpg / musica.json')

def make_thumbs(job, out_dir):
    """v3.1: miniaturas A/B con fabrica/thumb.py a partir de fotos de Commons ("thumbs" en el job)."""
    import thumb as TH
    for t in job.get('thumbs', []):
        try:
            c = SRC.commons_file(t['commons']); p = SRC.download(c['url'], '.jpg')
            out = f"{out_dir}/{job['id']}_miniatura_{t['name']}.jpg"
            TH.make(out, p, t['grande'], t['caja'], t.get('sub', ''), None, tuple(t['recorte']) if t.get('recorte') else None)
            log(f'   miniatura {t["name"]}: {c.get("credit", "")} · {c.get("license", "")}')
        except Exception as e: log('  aviso miniatura', t.get('name'), e)

# ================= PRINCIPAL =================
def run(job_dir):
    job = json.load(open(f'{job_dir}/job.json')); U = job['units']
    out_dir = f'{job_dir}/out'; wd = '/tmp/fabrica_work'; os.makedirs(out_dir, exist_ok=True); os.makedirs(f'{wd}/shots', exist_ok=True)
    random.seed(job.get('seed', 7)); credits = []; MUST[:] = job.get('must', [])
    global GRADE
    th = CARDS.set_theme(job.get('theme', 'antiguo')); g = th.get('grade', 'calido'); GRADE = GRADES.get(g, g)
    log(f'== piel: {th.get("uso", job.get("theme"))} · etalonaje {g}')
    br = job.get('brand', {}); BRAND.clear()
    if br.get('mosca', True): BRAND['mosca'] = os.path.join(ROOT, 'assets/brand/DocuVox_Mosca_1920x1080_alfa.png')
    log('== 1/5 audio: colocando voces, música y efectos')
    A = build_audio(job, U); credits += A['credits']
    align_audio(job, U, A, job_dir, out_dir)
    BANDO.clear(); BANDO.update({k: tuple(v) for k, v in job.get('bando', {}).items()}); REUSE.update(job.get('reuse', {}))
    log('== 2/5 guion visual'); shots = build_edl_sync(job, U, A) if job.get('align') else build_edl(job, U, A)
    if SYNC: open(f'{out_dir}/sincronia.txt', 'w').write('\n'.join(SYNC) + '\n')
    log(f'   {len(shots)} planos')
    qp = job.get('qpicks', {}); qsrc = {}
    if os.path.exists(f'{job_dir}/castq.json'): qsrc = json.load(open(f'{job_dir}/castq.json'))
    for k_, v_ in qp.items():
        QPICKS[k_] = [qsrc[k_][x] if isinstance(x, int) else x for x in v_ if not isinstance(x, int) or (k_ in qsrc and x < len(qsrc[k_]))]
    if job.get('stage') == 'cast': return cast(job, U, shots, out_dir, wd)
    picks = job.get('picks', {})
    global ENC, ABR
    if job.get('codec') == 'hevc': ENC = enc_hevc(job.get('max_kbps', 750)); ABR = job.get('audio_kbps', '112k')
    PART = os.environ.get('FABRICA_PART')
    log('== 3/5 buscando y descargando material')
    last = -1
    for n, s in enumerate(shots):
        try: s['res'] = resolve(s['spec'], s['d'], credits, picks.get(str(n)), t=s['t'])
        except Exception as e:
            log(f'  ! plano {n} ({s["spec"]}) -> {e}; uso alternativa')
            alt = job.get('fallback') or [{'card': {'type': 'title', 'title': job.get('channel', ''), 'sub': job.get('title', '')}}]
            s['res'] = resolve(alt[n % len(alt)], s['d'], credits)
        mv = random.choice([m for m in range(len(MOVES)) if m != last]); s['move'] = last = mv; s['n'] = n
    for name, q in job.get('overlays', {}).items():
        try:
            c = q if isinstance(q, dict) else candidates({'video': q, 'free': True}, n=1)[0]
            OVERLAYS[name] = use(c, credits)['path']
        except Exception as e: log('  aviso capa', name, e)
    # efectos automáticos: golpe de aire al entrar cada tarjeta, impacto en títulos
    extra = []
    # (por defecto, ninguno: el golpe de aire en cada tarjeta resultó chirriante y repetitivo en el episodio 2)
    auto = job.get('auto_sfx', {}); cap = job.get('sfx_max', 5)
    cache = {}; count = {}
    def sfx(q, db):
        count[q] = count.get(q, 0) + 1
        if count[q] > cap: raise RuntimeError(f'"{q}" ya sonó {cap} veces (sfx_max)')
        if q not in cache: cache[q] = gain_to(load(sfx_file(q, credits)), db)
        return cache[q]
    for s in shots:
        if s['res']['kind'] == 'card' and s['t'] > 1:
            q = auto.get('title') if s['res']['card']['type'] == 'title' else auto.get('card')
            if not q: continue
            try: y = sfx(q, -27 if 'boom' in q else -31); extra.append((int(max(0, s['t'] - 0.25) * SR), fade(y[:, :int(3 * SR)], 0.02, 0.8)))
            except Exception as e: log('  aviso sfx auto:', e)
    trs = job.get('tr_sfx', {'black': 'cinematic hit deep'})
    for s in shots:
        q = s['spec'].get('sfx')
        if q:
            q, db = (q, -30) if isinstance(q, str) else q
            try: y = sfx(q, db); extra.append((int(max(0, s['t'] - s['spec'].get('sfx_pre', .4)) * SR), fade(y[:, :int(s['d'] * SR + SR)], .05, .6)))
            except Exception as e: log('  aviso sfx plano:', e)
        if s.get('tr_in') in trs:
            try:
                y = sfx(trs[s['tr_in']], -28); pre = 0.6 if s['tr_in'] == 'flash' else 0.02
                extra.append((int(max(0, s['t'] - pre) * SR), fade(y[:, :int(2.5 * SR)], .02, .6)))
            except Exception as e: log('  aviso sfx transición:', e)
    if PART:
        k_, N_ = map(int, PART.split('/')); mine = [s for s in shots if s['n'] % N_ == k_]
        log(f'== parte {k_ + 1}/{N_}: {len(mine)} planos')
        with ThreadPoolExecutor(int(os.environ.get('FABRICA_THREADS', '2'))) as ex:
            for i_, f in enumerate([ex.submit(render_shot, s, f'{wd}/shots/{s["n"]:04d}.mp4', wd) for s in mine]):
                f.result()
                if i_ % 20 == 0: log(f'   plano {i_}/{len(mine)}')
        log('FIN PARTE'); open(f'{out_dir}/informe_parte{k_}.txt', 'w').write('\n'.join(LOG) + '\n'); return
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
    pieces = [fetch(p) for p in job.get('intro', ['assets/intro/docuvox.mp4'])]
    for k in range(len(bounds) - 1):
        a, b = bounds[k], bounds[k + 1]; fa, fb = round(a * FPS), round(b * FPS)
        lst = f'{wd}/part{k}.txt'
        open(lst, 'w').write(''.join(f"file '{wd}/shots/{s['n']:04d}.mp4'\n" for s in shots if fa <= round(s['t'] * FPS) < fb))
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{wd}/v{k}.mp4'])
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', f'{wd}/v{k}.mp4', '-ss', f'{fa / FPS:.3f}', '-t', f'{(fb - fa) / FPS:.3f}', '-i', f'{wd}/doc.wav',
            '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', ABR, '-ar', '48000', '-ac', '2', '-shortest', f'{wd}/m{k}.mp4'])
        pieces.append(f'{wd}/m{k}.mp4')
        if k < len(cuts): pieces.append(cuts[k][1])
    if job.get('brand', {}).get('outro', True):
        try: pieces.append(outro(job, shots, wd))
        except Exception as e: log('  aviso pantalla final:', e)
    norm = []
    for k, p in enumerate(pieces):  # piezas externas: mismas características que el doc
        if p.startswith(wd): norm.append(p); continue
        q = f'{wd}/ext{k}.mp4'
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', p, '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p',
            *[x for x in ENC if x != '-an'], '-c:a', 'aac', '-b:a', ABR, '-ar', '48000', '-ac', '2', q]); norm.append(q)
    open(f'{wd}/final.txt', 'w').write(''.join(f"file '{p}'\n" for p in norm))
    final = f'{out_dir}/{job["id"]}.mp4'
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{wd}/final.txt', '-c', 'copy', '-movflags', '+faststart', final])
    # desplazamientos de tiempo por intro e inserciones (para subtítulos y capítulos)
    def dur(p): return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).strip())
    intro_d = sum(dur(fetch(p)) for p in job.get('intro', ['assets/intro/docuvox.mp4'])); ins_d = [dur(c[1]) for c in cuts]
    def T(x): return x + intro_d + sum(d for (c, _), d in zip(cuts, ins_d) if x >= c)
    # subtítulos
    srt = []; n = 1
    for e in A['tl']:
        u = U[e['i']]
        if e['k'] not in ('N', 'P', 'R', 'T') or not u.get('text'): continue
        wu = A.get('words', {}).get(e['i'])
        if wu and wu['words']:  # subtítulos a la palabra: cada frase empieza cuando se dice
            ws = wu['words']; chunks = []; cur = []
            for w in ws:
                cur.append(w)
                if re.search(r'[.!?…:;]$', w['w']) or len(' '.join(x['w'] for x in cur)) > 78: chunks.append(cur); cur = []
            if cur: chunks.append(cur)
            vend = wu['off'] + e['d'] - (e.get('va', 0) if e['k'] == 'T' else 0)
            for c_, ch_ in enumerate(chunks):
                a = wu['off'] + ch_[0]['t']; b = (wu['off'] + chunks[c_ + 1][0]['t'] - 0.05) if c_ + 1 < len(chunks) else min(vend, a + 6)
                srt.append(f"{n}\n{srt_time(T(a))} --> {srt_time(T(max(b, a + 0.8)))}\n{' '.join(x['w'] for x in ch_)}\n"); n += 1
            continue
        txt = re.sub(r'\[[^\]]*\]', '', u['text']); sents = [s.strip() for s in re.split(r'(?<=[.!?…])\s+', txt.replace('\n', ' ')) if s.strip()]
        tot = sum(len(s) for s in sents); a = e['t']
        for s_ in sents:
            b = a + e['d'] * len(s_) / tot
            for chunk in [s_[i:i + 84] for i in range(0, len(s_), 84)] if len(s_) > 84 else [s_]:
                srt.append(f'{n}\n{srt_time(T(a))} --> {srt_time(T(b))}\n{chunk}\n'); n += 1
            a = b
    open(f'{out_dir}/{job["id"]}.srt', 'w').write('\n'.join(srt))
    chs = list(job.get('chapters', [])) + [dict(unit=i, title=(u.get('card') or {}).get('title', '')) for i, u in enumerate(U) if u['k'] == 'T' and u.get('chapter')]
    chs.sort(key=lambda c: c['unit'])
    ch = ['0:00 Introducción'] + [f"{int(T(next(x for x in A['tl'] if x['i'] == c['unit'])['t']) // 60)}:{int(T(next(x for x in A['tl'] if x['i'] == c['unit'])['t']) % 60):02d} {c['title']}" for c in chs]
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
    json.dump([dict(n=s['n'], t=round(s['t'], 2), d=round(s['d'], 2), unit=s['unit'], heard=s.get('heard', ''), spec=s['spec']) for s in shots], open(f'{out_dir}/edl.json', 'w'), ensure_ascii=False, indent=0)
    try: sync_sheets(shots, wd, out_dir)
    except Exception as e: log('  aviso hoja de sincronía:', e)
    make_thumbs(job, out_dir)
    log(f'FIN: {final} · {D/60:.1f} min · {os.path.getsize(final)/1e6:.0f} MB')
    open(f'{out_dir}/informe.txt', 'w').write('\n'.join(LOG) + '\n')

if __name__ == '__main__':
    try: run(sys.argv[1])
    except Exception:
        traceback.print_exc(); os.makedirs(f'{sys.argv[1]}/out', exist_ok=True)
        open(f'{sys.argv[1]}/out/informe.txt', 'w').write('\n'.join(LOG) + '\n\nERROR:\n' + traceback.format_exc()); sys.exit(1)
