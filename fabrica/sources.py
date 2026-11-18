"""Búsqueda y descarga de material libre para uso comercial (YouTube monetizado).
Cada función devuelve candidatos: dict(kind, url, w, h, dur, credit, license, page, id)."""
import os, json, time, hashlib, urllib.parse, urllib.request

UA = 'fabrica-documentales/1.0 (https://github.com/xvlerma/fabrica-documentales)'
CACHE = os.environ.get('FABRICA_CACHE', '/tmp/fabrica_cache')
os.makedirs(CACHE, exist_ok=True)
def lic_ok(lic):
    """Solo dominio público, CC0 y CC BY: nada NC, ND ni SA (documento maestro)."""
    import re as _r
    l = (lic or '').lower()
    if _r.search(r'(^|[\s\-_/])(sa|nc|nd)($|[\s\-_/\d.])', l) or 'sharealike' in l or 'share alike' in l or 'noncommercial' in l or 'noderiv' in l or 'gfdl' in l: return False
    return any(x in l for x in OK_LIC)
OK_LIC = ('cc0', 'pdm', 'public domain', 'cc by', 'cc-by', 'by', 'pixabay', 'no restrictions', 'attribution')

_last = {}
def _get(url, headers=None, tries=7):
    host = urllib.parse.urlparse(url).netloc
    for i in range(tries):
        if 'wiki' in host:  # Wikimedia limita a los bots: ritmo pausado
            w = 0.6 - (time.time() - _last.get(host, 0))
            if w > 0: time.sleep(w)
            _last[host] = time.time()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=60) as r: return r.read()
        except Exception as e:
            if i == tries - 1: raise
            code = getattr(e, 'code', 0)
            time.sleep((15 * (i + 1)) if code == 429 else (2 + 3 * i))

def _json(url, headers=None): return json.loads(_get(url, headers))

def download(url, ext=None, headers=None):
    import re as _re
    m = _re.search(r'elevenlabsusercontent\.com/.*/content_generation/[A-Za-z0-9]+/([A-Za-z0-9]+)/', url)
    h = ('el_' + m.group(1)) if m else hashlib.sha1(url.split('?')[0].encode() if 'figma.com' in url else url.encode()).hexdigest()[:16]
    ext = ext or os.path.splitext(urllib.parse.urlparse(url).path)[1] or '.bin'
    out = f'{CACHE}/{h}{ext}'
    if not os.path.exists(out) or os.path.getsize(out) < 1000:
        data = _get(url, headers)
        open(out + '.part', 'wb').write(data); os.rename(out + '.part', out)
    return out

# ---------- vídeo ----------
def pixabay_videos(q, n=30):
    key = os.environ.get('PIXABAY_API_KEY')
    if not key: return []
    j = _json(f'https://pixabay.com/api/videos/?key={key}&q={urllib.parse.quote(q)}&per_page={n}&safesearch=true')
    out = []
    for h in j.get('hits', []):
        V = h['videos']; v = V.get('large') or {}
        if not v.get('url') or v.get('width', 0) < 1280: v = V.get('medium') or {}
        if not v.get('url'): continue
        thumb = next((V[k].get('thumbnail') for k in ('medium', 'large', 'small', 'tiny') if (V.get(k) or {}).get('thumbnail')), None)
        if not thumb and h.get('picture_id'): thumb = f"https://i.vimeocdn.com/video/{h['picture_id']}_640x360.jpg"
        out.append(dict(kind='video', url=v['url'], w=v.get('width', 0), h=v.get('height', 0), dur=h.get('duration', 0), thumb=thumb,
                        credit=f"{h.get('user','')} / Pixabay", license='Pixabay Content License', page=h.get('pageURL'), id=f"pxb{h['id']}", tags=h.get('tags', '')))
    return out

def relevant(c, must):
    """True si el candidato menciona alguno de los términos obligatorios (etiquetas, título o página)."""
    if any(x in str(c.get('tags', '')).lower() for x in ('ai generated', 'ai-generated', 'generative', 'midjourney', 'render', '3d', 'animation', 'cartoon')): return False
    if not must: return True
    txt = ' '.join(str(c.get(k, '')) for k in ('tags', 'title', 'page', 'credit')).lower()
    return any(m.lower() in txt for m in must)

def commons_search(q, video=False, n=10):
    filt = ' filetype:video' if video else ' filetype:bitmap'
    u = ('https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6'
         f'&gsrlimit={n}&gsrsearch={urllib.parse.quote(q + filt)}&prop=imageinfo&iiprop=url|size|extmetadata|mime|mediatype&iiurlwidth=1920')
    j = _json(u); out = []
    for p in (j.get('query', {}).get('pages', {}) or {}).values():
        ii = (p.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
        lic = (m.get('LicenseShortName', {}) or {}).get('value', '')
        if not lic_ok(lic): continue
        art = (m.get('Artist', {}) or {}).get('value', '')
        import re; art = re.sub('<[^>]+>', '', art).strip()[:80] or 'Wikimedia Commons'
        if video:
            if not ii.get('mime', '').startswith('video'): continue
            url = ii.get('url'); dur = float(ii.get('duration') or 0)
        else:
            url = ii.get('thumburl') or ii.get('url'); dur = 0
        out.append(dict(kind='video' if video else 'image', url=url, w=ii.get('width', 0), h=ii.get('height', 0), dur=dur, title=p.get('title', ''),
                        thumb=None if video else ii.get('thumburl'), credit=art, license=lic, page=ii.get('descriptionurl'), id='wm' + str(p.get('pageid'))))
    return out

def commons_file(title):
    t = title if title.startswith('File:') else 'File:' + title
    u = ('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|size|extmetadata|mime'
         f'&iiurlwidth=1920&titles={urllib.parse.quote(t)}')
    j = _json(u)
    for p in j['query']['pages'].values():
        ii = (p.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
        import re
        art = re.sub('<[^>]+>', '', (m.get('Artist', {}) or {}).get('value', '')).strip()[:80] or 'Wikimedia Commons'
        vid = ii.get('mime', '').startswith('video')
        lic = (m.get('LicenseShortName', {}) or {}).get('value', '')
        if not lic_ok(lic): raise LookupError(f'licencia no permitida ({lic}) en {t}')
        return dict(kind='video' if vid else 'image', url=ii.get('url') if vid else (ii.get('thumburl') or ii.get('url')),
                    w=ii.get('width', 0), h=ii.get('height', 0), dur=float(ii.get('duration') or 0), credit=art,
                    license=(m.get('LicenseShortName', {}) or {}).get('value', ''), page=ii.get('descriptionurl'), id='wm' + str(p.get('pageid')))

def archive_videos(q, n=8):
    u = ('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(f'({q}) AND mediatype:movies AND (licenseurl:*publicdomain* OR collection:prelinger)')
         + f'&fl[]=identifier&fl[]=title&rows={n}&output=json')
    try: docs = _json(u)['response']['docs']
    except Exception: return []
    out = []
    for d in docs:
        try:
            md = _json(f"https://archive.org/metadata/{d['identifier']}")
            files = [f for f in md.get('files', []) if f.get('name', '').lower().endswith('.mp4')]
            if not files: continue
            f = sorted(files, key=lambda f: -int(f.get('size', 0) or 0))[0]
            out.append(dict(kind='video', url=f"https://archive.org/download/{d['identifier']}/{urllib.parse.quote(f['name'])}", w=0, h=0,
                            dur=float(f.get('length', 0) or 0) if str(f.get('length', '')).replace('.', '').isdigit() else 0,
                            credit=f"{d.get('title','')} / Internet Archive", license='Public Domain', page=f"https://archive.org/details/{d['identifier']}", id='ia' + d['identifier']))
        except Exception: continue
    return out

def europeana(q, video=False, n=10):
    key = os.environ.get('EUROPEANA_API_KEY')
    if not key: return []
    t = 'VIDEO' if video else 'IMAGE'
    u = (f'https://api.europeana.eu/record/v2/search.json?wskey={key}&query={urllib.parse.quote(q)}&qf=TYPE:{t}&reusability=open'
         f'&media=true&rows={n}&profile=rich')
    out = []
    for it in _json(u).get('items', []):
        url = (it.get('edmIsShownBy') or [None])[0]
        if not url: continue
        rights = (it.get('rights') or [''])[0]
        if 'nc' in rights.lower(): continue
        out.append(dict(kind='video' if video else 'image', url=url, w=0, h=0, dur=0, credit=(it.get('dataProvider') or ['Europeana'])[0],
                        license=rights, page=it.get('guid'), id='eu' + it.get('id', '').replace('/', '_')))
    return out

def cleveland(q, n=10):
    u = f'https://openaccess-api.clevelandart.org/api/artworks/?q={urllib.parse.quote(q)}&cc0=1&has_image=1&limit={n}'
    out = []
    for a in _json(u).get('data', []):
        im = ((a.get('images') or {}).get('web') or {})
        if not im.get('url'): continue
        out.append(dict(kind='image', url=im['url'], w=int(im.get('width') or 0), h=int(im.get('height') or 0), dur=0,
                        credit='Cleveland Museum of Art', license='CC0', page=a.get('url'), id=f"cma{a['id']}", title=(a.get('title') or '') + ' ' + (a.get('culture') or [''])[0] if isinstance(a.get('culture'), list) else a.get('title'), thumb=im['url']))
    return out

def met(q, n=8):
    try:
        ids = (_json(f'https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q={urllib.parse.quote(q)}').get('objectIDs') or [])[:n * 2]
    except Exception: return []
    out = []
    for i in ids:
        try:
            o = _json(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}')
            if o.get('isPublicDomain') and o.get('primaryImage'):
                out.append(dict(kind='image', url=o['primaryImage'], w=0, h=0, dur=0, credit='The Metropolitan Museum of Art', license='CC0',
                                page=o.get('objectURL'), id=f'met{i}', title=f"{o.get('title','')} {o.get('culture','')} {o.get('department','')}", thumb=o.get('primaryImageSmall') or o['primaryImage']))
        except Exception: pass
        if len(out) >= n: break
    return out

# ---------- audio ----------
def freesound(q, min_d=1, max_d=30, n=8):
    key = os.environ.get('FREESOUND_API_KEY')
    if not key: return []
    f = urllib.parse.quote(f'duration:[{min_d} TO {max_d}] license:("Creative Commons 0" OR "Attribution")')
    u = (f'https://freesound.org/apiv2/search/text/?query={urllib.parse.quote(q)}&filter={f}&sort=rating_desc'
         f'&fields=id,name,username,license,previews,duration,url&page_size={n}&token={key}')
    out = []
    for s in _json(u).get('results', []):
        out.append(dict(kind='audio', url=s['previews']['preview-hq-mp3'], dur=s.get('duration', 0), credit=f"{s['username']} / Freesound",
                        license=s.get('license', ''), page=s.get('url'), id=f"fs{s['id']}", name=s.get('name')))
    return out

# ---------- música gratuita con licencia comercial ----------
# Solo dominio público, CC0 y CC BY (sin NC, ND ni SA: la pista se corta, se repite y se mezcla).
MUSIC_OK = ('publicdomain', 'public domain', 'pdm', 'cc0', '/by/', 'cc by ', 'cc-by ', 'cc by-4', 'attribution')
def _music_ok(lic):
    l = (lic or '').lower() + ' '
    if any(x in l for x in ('nc', '-nd', ' nd', 'sa', 'noderiv', 'sharealike', 'noncommercial')): return False
    return any(x in l for x in MUSIC_OK) or l.strip() in ('by', 'cc by')

def openverse_music(q, n=10):
    """Openverse (Wikimedia, Freesound, ccMixter). Jamendo excluido a propósito."""
    u = (f'https://api.openverse.org/v1/audio/?q={urllib.parse.quote(q)}&license=cc0,pdm,by&category=music'
         f'&source=wikimedia_audio,freesound,ccmixter&page_size={n}&length=medium,long')
    out = []
    try: res = _json(u).get('results', [])
    except Exception: return []
    for r in res:
        if not r.get('url') or r.get('source') == 'jamendo': continue
        out.append(dict(kind='audio', url=r['url'], dur=(r.get('duration') or 0) / 1000, title=r.get('title', ''), credit=f"{r.get('creator','')} / {r.get('source','')}",
                        license=f"CC {r.get('license','').upper()} {r.get('license_version','')}".strip(), page=r.get('foreign_landing_url'), id='ov' + r['id'],
                        tags=' '.join(t.get('name', '') for t in (r.get('tags') or [])[:12])))
    return out

def archive_music(q, n=10):
    """Internet Archive: grabaciones de dominio público / CC0 / CC BY (Musopen, bandas militares, gramófono, sinfónica)."""
    lic = '(licenseurl:*publicdomain* OR licenseurl:*zero* OR licenseurl:*licenses/by/*)'
    u = ('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(f'({q}) AND mediatype:audio AND {lic}')
         + f'&fl[]=identifier&fl[]=title&fl[]=creator&fl[]=licenseurl&sort[]=downloads+desc&rows={n}&output=json')
    try: docs = _json(u)['response']['docs']
    except Exception: return []
    out = []
    for d in docs:
        if not _music_ok(d.get('licenseurl', '')): continue
        try:
            md = _json(f"https://archive.org/metadata/{d['identifier']}")
            fs = [f for f in md.get('files', []) if f.get('name', '').lower().endswith('.mp3')]
            def L(f):
                try: return float(f.get('length', 0))
                except Exception:
                    try: m_, s_ = str(f.get('length', '0:0')).split(':')[-2:]; return int(m_) * 60 + float(s_)
                    except Exception: return 0
            fs = [f for f in fs if 50 < L(f) < 900] or fs
            for f in fs[:3]:
                out.append(dict(kind='audio', url=f"https://archive.org/download/{d['identifier']}/{urllib.parse.quote(f['name'])}", dur=L(f),
                                title=f"{d.get('title','')} · {f.get('title') or f['name']}", credit=f"{d.get('creator','') if isinstance(d.get('creator'), str) else ', '.join(d.get('creator') or [])} / Internet Archive",
                                license='Dominio público' if 'publicdomain' in d.get('licenseurl', '') or 'zero' in d.get('licenseurl', '') else 'CC BY',
                                page=f"https://archive.org/details/{d['identifier']}", id='iam' + d['identifier'] + str(hash(f['name']) % 10000)))
        except Exception: continue
        if len(out) >= n: break
    return out

def commons_music(q, n=10):
    """Wikimedia Commons: grabaciones libres (muchas de dominio público: orquestas, bandas militares, música antigua)."""
    u = ('https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6'
         f'&gsrlimit={n * 2}&gsrsearch={urllib.parse.quote(q + " filetype:audio")}&prop=imageinfo&iiprop=url|extmetadata|mime')
    try: j = _json(u)
    except Exception: return []
    out = []
    import re
    for p in (j.get('query', {}).get('pages', {}) or {}).values():
        ii = (p.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
        lic = (m.get('LicenseShortName', {}) or {}).get('value', '')
        if not _music_ok(lic): continue
        dur = float(ii.get('duration') or 0)
        art = re.sub('<[^>]+>', '', (m.get('Artist', {}) or {}).get('value', '')).strip()[:80] or 'Wikimedia Commons'
        url = ii.get('url')
        if not url: continue
        out.append(dict(kind='audio', url=url, dur=dur, title=p.get('title', ''), credit=art, license=lic, page=ii.get('descriptionurl'), id='wma' + str(p.get('pageid'))))
    return out[:n]

def freesound_music(q, n=10):
    """Freesound: atmósferas, drones y piezas largas (CC0 / CC BY)."""
    return [dict(c, title=c.get('name', '')) for c in freesound(q, min_d=45, max_d=900, n=n)]

def incompetech(title):
    """Kevin MacLeod (incompetech.com), CC BY 4.0: título exacto de la pista."""
    return dict(kind='audio', url='https://incompetech.com/music/royalty-free/mp3-royaltyfree/' + urllib.parse.quote(title) + '.mp3', dur=0, title=title,
                credit='Kevin MacLeod (incompetech.com)', license='CC BY 4.0', page='https://incompetech.com/music/royalty-free/', id='inc' + title.replace(' ', '_'))

MUSIC_SRC = dict(archive=archive_music, commons=commons_music, openverse=openverse_music, freesound=freesound_music)
def music_search(q, src='archive,commons,openverse,freesound', n=8):
    out = []
    for s_ in src.split(','):
        fn = MUSIC_SRC.get(s_.strip())
        if not fn: continue
        try: out += [c for c in fn(q, n) if c['id'] not in {x['id'] for x in out}]
        except Exception as e: print('aviso música', s_, e, flush=True)
    return out
