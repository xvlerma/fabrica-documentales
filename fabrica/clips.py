"""v7 · etapa "clips": busca, localiza al segundo y recorta cortes reales de archivo oficial.

Para cada página oficial (La Moncloa, RTVE...) lista sus vídeos HLS y sus subtítulos .vtt; busca en los
subtítulos las frases pedidas (búsqueda difusa) y recorta el vídeo con margen. Si un vídeo no tiene
subtítulos, lo transcribe con faster-whisper y busca ahí. Todo sale plano en out/:
  clip_<nombre>.mp4 · clip_<nombre>.jpg · clips.json (dónde se encontró cada frase y con qué confianza)
  txt_<video>.txt (transcripción con tiempos, para buscar más frases después)
  discover.json (lo que respondieron las búsquedas de RTVE)
"""
import os, re, json, html, difflib, subprocess, unicodedata, urllib.request, urllib.parse

UA = {'User-Agent': 'Mozilla/5.0 (DocuVox clips)'}
LOG = []

def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LOG.append(s)

def get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()

def norm(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9ñ ]+', ' ', t)

def ts(s):
    p = s.replace(',', '.').split(':'); p = [float(x) for x in p]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]

def parse_vtt(txt):
    cues = []
    for m in re.finditer(r'(\d[\d:.,]+)\s*-->\s*(\d[\d:.,]+)[^\n]*\n(.*?)(?:\n\s*\n|\Z)', txt, re.S):
        t = re.sub(r'<[^>]+>', '', m.group(3)).replace('\n', ' ').strip()
        if t: cues.append((ts(m.group(1)), ts(m.group(2)), t))
    return cues

def words_from_cues(cues):
    """reparte cada cue en palabras con tiempo proporcional (suficiente para cortar con margen)"""
    W = []
    for a, b, t in cues:
        ws = norm(t).split()
        for k, w in enumerate(ws): W.append((w, a + (b - a) * k / max(1, len(ws)), a + (b - a) * (k + 1) / max(1, len(ws))))
    return W

def find_phrase(W, phrase):
    """mejor ventana de palabras para la frase: (score, t0, t1)"""
    P = norm(phrase).split()
    if not P or not W: return (0, 0, 0)
    n = len(P); best = (0, 0, 0); toks = [w for w, _, _ in W]
    for i in range(0, max(1, len(W) - n + 1)):
        win = toks[i:i + n + 2]
        r = difflib.SequenceMatcher(None, P, win[:n]).ratio()
        if r > best[0]: best = (r, W[i][1], W[min(len(W) - 1, i + n - 1)][2])
    return best

def whisper_words(src, model='small'):
    from faster_whisper import WhisperModel
    wav = '/tmp/clips_audio.wav'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-vn', '-ac', '1', '-ar', '16000', wav], check=True, timeout=5400)
    import soundfile as sf, numpy as np
    y, _ = sf.read(wav, dtype='float32')
    m = WhisperModel(model, device='cpu', compute_type='int8', cpu_threads=os.cpu_count() or 2)
    segs, _ = m.transcribe(y, language='es', word_timestamps=True, beam_size=1, vad_filter=True)
    W = []
    for s in segs:
        for w in (s.words or []):
            for t in norm(w.word).split(): W.append((t, float(w.start), float(w.end)))
    return W

def cut(src, t0, t1, out_mp4, pad=(1.2, 1.5)):
    a = max(0, t0 - pad[0]); d = (t1 + pad[1]) - a
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{a:.2f}', '-i', src, '-t', f'{d:.2f}',
                    '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out_mp4],
                   check=True, timeout=1200)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{min(d, pad[0] + 0.6):.2f}', '-i', out_mp4, '-frames:v', '1', '-vf', 'scale=640:-2',
                    out_mp4[:-4] + '.jpg'], timeout=120)
    return a, d

def page_media(pg):
    txt = html.unescape(get(pg).decode('utf-8', 'ignore'))
    links = set(re.findall(r'''(https?:[^"'\s<>]+?\.(?:m3u8|mp4|vtt)(?:\?[^"'\s<>]*)?)''', txt))
    for r in re.findall(r'''["'](/[^"'\s<>]+?\.(?:vtt|mp4|m3u8))["']''', txt):
        links.add('https:' + r if r.startswith('//') else 'https://www.lamoncloa.gob.es' + r)
    links = {re.sub(r'^https?://www\.lamoncloa\.gob\.es//', 'https://', l) for l in links}
    vids = {}
    for l in sorted(links):
        if l.endswith('.m3u8'):
            b = re.search(r'[:/]([^:/]+?)(?:__300)?\.(?:smil|mp4)/playlist', l)
            if b: vids.setdefault(b.group(1).lower(), l)
    vtts = {re.sub(r'\.vtt$', '', l.rsplit('/', 1)[-1]).lower(): l for l in links if l.endswith('.vtt')}
    return vids, vtts

def rtve_discover(queries, out_dir):
    """prueba varios puntos de la API pública de RTVE y guarda lo que conteste (ids, títulos, fechas)"""
    res = {}
    for q in queries:
        qq = urllib.parse.quote(q); res[q] = {}
        for ep in [f'https://api2.rtve.es/api/search/contents?search={qq}&context=tve&type=video&size=40',
                   f'https://api2.rtve.es/api/search/contents?search={qq}&size=40']:
            try:
                b = get(ep, 40).decode('utf-8', 'ignore')
                items = []
                try:
                    j = json.loads(b); its = (j.get('page') or {}).get('items') or j.get('items') or []
                    for it in its:
                        items.append(dict(id=str(it.get('id')), t=it.get('longTitle') or it.get('title'), d=it.get('publicationDate') or it.get('dateOfEmission'),
                                          dur=it.get('duration'), type=str(it.get('contentType') or it.get('type') or '')[:40],
                                          url=it.get('htmlUrl') or it.get('url')))
                except Exception: pass
                res[q][ep] = dict(n=len(b), items=items[:40])
            except Exception as e: res[q][ep] = dict(error=str(e)[:200])
    json.dump(res, open(f'{out_dir}/discover.json', 'w'), ensure_ascii=False, indent=1)

def rtve_subs(vid):
    try:
        j = json.loads(get(f'https://www.rtve.es/api/videos/{vid}/subtitulos.json'))
        for it in j.get('page', {}).get('items', []):
            if it.get('lang', '').startswith('es') and it.get('src'): return get(it['src']).decode('utf-8', 'ignore')
    except Exception as e: log(f'  subtítulos RTVE {vid}: {e}')
    return None

def rtve_meta(vid):
    try:
        it = json.loads(get(f'https://www.rtve.es/api/videos/{vid}.json'))['page']['items'][0]
        return dict(title=it.get('title'), date=it.get('publicationDate'), dur=it.get('duration'), url=it.get('htmlUrl'))
    except Exception as e: return dict(error=str(e)[:200])

def run(job, out_dir):
    os.makedirs(out_dir, exist_ok=True); report = []
    if job.get('discover'): rtve_discover(job['discover'], out_dir)
    for pj in job.get('sources', []):
        # pj: {"page": url}  o  {"rtve": id}  o  {"src": m3u8/mp4}, con "find": [{"name","phrase","pad"}], "transcribe": bool
        try:
            vids, vtts = {}, {}
            if pj.get('page'): vids, vtts = page_media(pj['page'])
            if pj.get('rtve'):
                vids = {f"rtve{pj['rtve']}": f"https://ztnr.rtve.es/ztnr/{pj['rtve']}.m3u8"}
                s = rtve_subs(pj['rtve'])
                if s: vtts = {f"rtve{pj['rtve']}": s}
                report.append(dict(rtve=pj['rtve'], meta=rtve_meta(pj['rtve']), subs=bool(s)))
            if pj.get('src'): vids = {pj.get('key', 'src'): pj['src']}
            log(f"== {pj.get('page') or pj.get('rtve') or pj.get('src')}: {len(vids)} vídeos, {len(vtts)} subtítulos")
            # palabras por vídeo
            WV = {}
            for k, u in vids.items():
                v = vtts.get(k)
                if v is not None:
                    if v.startswith('http'): v = get(v).decode('utf-8', 'ignore')
                    WV[k] = words_from_cues(parse_vtt(v))
                elif pj.get('transcribe') or not vtts:
                    if pj.get('only') and not any(o.lower() in k for o in pj['only']): continue
                    try:
                        log(f'  transcribiendo {k}…'); WV[k] = whisper_words(u, pj.get('model', 'small'))
                    except Exception as e: log(f'  whisper {k}: {e}'); continue
                if k in WV:
                    open(f'{out_dir}/txt_{k[:60]}.txt', 'w').write(
                        '\n'.join(f'{a:8.1f} {w}' for w, a, _ in WV[k]))
            for f in pj.get('find', []):
                best = (0, 0, 0, None)
                for k, W in WV.items():
                    if f.get('video') and f['video'].lower() not in k: continue
                    sc, a, b = find_phrase(W, f['phrase'])
                    if sc > best[0]: best = (sc, a, b, k)
                if f.get('at'): best = (1.0, f['at'][0], f['at'][1], f.get('video') or next(iter(vids)))
                sc, a, b, k = best
                r = dict(name=f['name'], phrase=f['phrase'], video=k, url=vids.get(k), score=round(sc, 3), t0=round(a, 2), t1=round(b, 2),
                         page=pj.get('page'), rtve=pj.get('rtve'))
                if k and sc >= f.get('min', 0.6):
                    try:
                        ss, d = cut(vids[k], a, b, f"{out_dir}/clip_{f['name']}.mp4", tuple(f.get('pad', (1.2, 1.5))))
                        r.update(ok=True, ss=round(ss, 2), dur=round(d, 2))
                    except Exception as e: r.update(ok=False, error=str(e)[:200])
                else: r.update(ok=False, error='frase no encontrada con confianza suficiente')
                log(f"  {f['name']}: {r.get('ok')} {k} {sc:.2f} {a:.1f}-{b:.1f}"); report.append(r)
        except Exception as e:
            log(f'  error fuente {pj}: {e}'); report.append(dict(source=pj, error=str(e)[:300]))
        json.dump(report, open(f'{out_dir}/clips.json', 'w'), ensure_ascii=False, indent=1)
    open(f'{out_dir}/run.log', 'w').write('\n'.join(LOG))
