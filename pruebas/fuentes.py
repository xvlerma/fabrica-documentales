"""Prueba real de fuentes en el runner (con internet). Imprime un informe y muestras crudas."""
import sys, os, json, re, traceback, urllib.request, urllib.parse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fabrica'))
import sources as S
def raw(url, n=1500, headers=None):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': S.UA, **(headers or {})})
        with urllib.request.urlopen(req, timeout=40) as r: b = r.read()
        print(f'  RAW {url} -> {len(b)} bytes\n  ' + b[:n].decode('utf-8', 'replace').replace('\n', ' ')[:n])
        return b
    except Exception as e: print(f'  RAW {url} -> ERROR {e}')
def probar(nombre, fn):
    print(f'\n=== {nombre}')
    try:
        r = fn(); print(f'  OK {len(r)} resultados')
        for c in r[:3]: print('   ', json.dumps({k: c.get(k) for k in ('url', 'page', 'credit', 'license', 'title', 'dur')}, ensure_ascii=False)[:400])
        # comprobar que el primer recurso se descarga
        if r:
            try: p = S.download(r[0]['url'], '.bin'); print(f'  DESCARGA OK {os.path.getsize(p)} bytes')
            except Exception as e: print('  DESCARGA ERROR', e)
    except Exception: print('  ERROR'); traceback.print_exc(limit=2)
probar('NASA imagen', lambda: S.nasa('apollo 11 moon landing'))
probar('NASA vídeo', lambda: S.nasa('earth from space', video=True, n=4))
probar('Library of Congress', lambda: S.loc_photos('spain 1936'))
print('\n=== Smithsonian (crudo)')
k = os.environ.get('SMITHSONIAN_API_KEY') or 'DEMO_KEY'
raw(f'https://api.si.edu/openaccess/api/v1.0/search?q={urllib.parse.quote("steam locomotive")}&rows=2&api_key={k}', 3000)
print('\n=== Rijksmuseum (crudo)')
b = raw('https://data.rijksmuseum.nl/search/collection?title=Nachtwacht&imageAvailable=true', 1200)
try:
    first = json.loads(b)['orderedItems'][0]['id']; print('  primer id', first)
    ob = raw(first, 4000, {'Accept': 'application/ld+json'})
    j = json.loads(ob); vs = j.get('shows') or []
    print('  shows', json.dumps(vs)[:300])
    if vs: v = raw(vs[0]['id'], 2500, {'Accept': 'application/ld+json'})
    try:
        vj = json.loads(v); d = (vj.get('digitally_shown_by') or [{}])[0].get('id')
        if d: raw(d, 2500, {'Accept': 'application/ld+json'})
    except Exception as e: print('  sin digitally_shown_by', e)
except Exception as e: print('  ERROR rijks', e)
print('\n=== Mixkit (crudo)')
for u in ('https://mixkit.co/free-stock-music/mood/dramatic/', 'https://mixkit.co/free-stock-music/tag/cinematic/'):
    b = raw(u, 300)
    if b:
        t = b.decode('utf-8', 'replace')
        mp3 = sorted(set(re.findall(r'https?://assets\.mixkit\.co/[^"\'\s]+?\.mp3', t)))
        print(f'  mp3 encontrados: {len(mp3)}', mp3[:5])
        i = t.find('.mp3'); print('  contexto:', t[max(0, i - 700):i + 200].replace('\n', ' ') if i > 0 else '(sin .mp3)')
        pages = sorted(set(re.findall(r'/free-stock-music/[a-z0-9-]+-\d+/', t))); print(f'  fichas: {len(pages)}', pages[:5])
