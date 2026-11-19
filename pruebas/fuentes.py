"""Prueba real de fuentes en el runner (con internet). Ronda 2: conexiones definitivas + catálogo Mixkit."""
import sys, os, json, traceback
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fabrica'))
import sources as S
def probar(nombre, fn, bajar=True):
    print(f'\n=== {nombre}')
    try:
        r = fn(); print(f'  {"OK" if r else "VACÍO"} {len(r)} resultados')
        for c in r[:3]: print('   ', json.dumps({k: c.get(k) for k in ('url', 'page', 'credit', 'license', 'title', 'dur')}, ensure_ascii=False)[:330])
        if r and bajar:
            try: p = S.download(r[0]['url'], '.bin'); print(f'  DESCARGA OK {os.path.getsize(p)} bytes')
            except Exception as e: print('  DESCARGA ERROR', e)
        return r
    except Exception: print('  ERROR'); traceback.print_exc(limit=3)
print('=== Mixkit: construyendo catálogo')
cat = S.mixkit_catalog_build()
json.dump(cat, open(os.path.join(S.CACHE, 'mixkit_catalogo.json'), 'w'), ensure_ascii=False, indent=0)
print(f'  pistas verificadas (Free License): {len(cat)}')
from collections import Counter
print('  grupos:', Counter(g for e in cat for g in e['grupos']).most_common(40))
S.MIXKIT_CAT = os.path.join(S.CACHE, 'mixkit_catalogo.json')
probar('Mixkit búsqueda "dramatic suspense"', lambda: S.mixkit_search('dramatic suspense'))
probar('Mixkit búsqueda "epic cinematic"', lambda: S.mixkit_search('epic cinematic'), bajar=False)
probar('NASA vídeo', lambda: S.nasa('earth from space', video=True, n=3))
probar('Library of Congress "spain 1936"', lambda: S.loc_photos('spain 1936'))
probar('Library of Congress "steam locomotive"', lambda: S.loc_photos('steam locomotive'), bajar=False)
probar('Smithsonian "steam locomotive"', lambda: S.smithsonian('steam locomotive'))
probar('Smithsonian "ancient egypt"', lambda: S.smithsonian('ancient egypt'), bajar=False)
probar('Rijksmuseum "Nachtwacht"', lambda: S.rijksmuseum('Nachtwacht', n=3))
probar('Rijksmuseum "ship"', lambda: S.rijksmuseum('ship', n=3), bajar=False)
