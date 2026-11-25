"""Descarga fotos de Commons (títulos en fotos/lista.txt, o 'buscar: consulta') a /tmp/fo con su ficha (licencia, autor)."""
import sys, os, json, urllib.request, urllib.parse
sys.path.insert(0, 'fabrica'); import sources as S
out = sys.argv[1]; os.makedirs(out, exist_ok=True); fichas = []
def get(t, i):
    c = S.commons_file(t); u = c['url']
    req = urllib.request.Request(u, headers={'User-Agent': 'DocuVox/1.0 (fabrica)'}); d = urllib.request.urlopen(req, timeout=60).read()
    fn = f'f{i:02d}.jpg'; open(f'{out}/{fn}', 'wb').write(d); c['file'] = fn; c['title'] = t; fichas.append(c); print(fn, t, c['license'])
i = 0
for line in open('fotos/lista.txt', encoding='utf-8'):
    line = line.strip()
    if not line: continue
    if line.startswith('buscar:'):
        q = line[7:].strip()
        u = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&list=search&srnamespace=6&srlimit=12&srsearch=' + urllib.parse.quote(q)
        for r in S._json(u)['query']['search']:
            try: get(r['title'], i); i += 1
            except Exception as e: print('error', r['title'], e)
    else:
        try: get(line, i); i += 1
        except Exception as e: print('error', line, e)
json.dump(fichas, open(f'{out}/fichas.json', 'w'), ensure_ascii=False, indent=1)
