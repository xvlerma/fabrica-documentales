"""Búsqueda y descarga de material libre para uso comercial (YouTube monetizado).
Cada función devuelve candidatos: dict(kind, url, w, h, dur, credit, license, page, id)."""
import os, json, time, hashlib, urllib.parse, urllib.request

UA = 'fabrica-documentales/1.0 (https://github.com/xvlerma/fabrica-documentales)'
CACHE = os.environ.get('FABRICA_CACHE', '/tmp/fabrica_cache')
os.makedirs(CACHE, exist_ok=True)
OK_LIC = ('cc0', 'pdm', 'public domain', 'cc by', 'cc-by', 'by', 'by-sa', 'cc by-sa', 'pixabay', 'no restrictions', 'attribution')

def _get(url, headers=None, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=60) as r: return r.read()
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(2 + 3 * i)

def _json(url, headers=None): return json.loads(_get(url, headers))

def download(url, ext=None, headers=None):
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
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
        if not any(x in lic.lower() for x in OK_LIC) or 'nc' in lic.lower().replace('nc-', 'nc '): continue
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

def openverse_music(q, n=8):
    u = (f'https://api.openverse.org/v1/audio/?q={urllib.parse.quote(q)}&license_type=commercial&category=music'
         f'&page_size={n}&length=medium,long')
    out = []
    try: res = _json(u).get('results', [])
    except Exception: return []
    for r in res:
        if not r.get('url'): continue
        out.append(dict(kind='audio', url=r['url'], dur=(r.get('duration') or 0) / 1000, credit=f"{r.get('creator','')} / {r.get('source','')}",
                        license=f"CC {r.get('license','').upper()} {r.get('license_version','')}", page=r.get('foreign_landing_url'), id='ov' + r['id']))
    return out
