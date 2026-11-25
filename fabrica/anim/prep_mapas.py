"""Prepara mapas compactos (Natural Earth, dominio público) para el módulo de animaciones.
Uso: python prep_mapas.py <carpeta con ne_50m_admin_0_countries.geojson y ne_10m_admin_1_states_provinces.geojson>"""
import sys, json, os, math
import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon
SRC = sys.argv[1]; OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
def rings(geom, tol, minarea=0):
    g = geom.simplify(tol, preserve_topology=True)
    ps = [g] if isinstance(g, Polygon) else list(getattr(g, 'geoms', []))
    out = []
    for p in ps:
        if p.area < minarea: continue
        out.append([[round(x, 3), round(y, 3)] for x, y in p.exterior.coords])
    return out
def dump(name, feats): json.dump(feats, open(f'{OUT}/{name}.json', 'w'), separators=(',', ':')); print(name, len(feats), os.path.getsize(f'{OUT}/{name}.json') // 1024, 'KB')
w = gpd.read_file(f'{SRC}/ne_50m_admin_0_countries.geojson')
dump('mundo', [dict(iso=r.ADM0_A3, name=r.NAME, cont=r.CONTINENT, rings=rings(r.geometry, 0.12, 0.05)) for r in w.itertuples() if r.ADM0_A3 != 'ATA'])
eu = w[w.CONTINENT == 'Europe']
dump('europa', [dict(iso=r.ADM0_A3, name=r.NAME, rings=rings(r.geometry, 0.03, 0.002)) for r in w.itertuples() if r.CONTINENT in ('Europe', 'Asia', 'Africa')])
a = gpd.read_file(f'{SRC}/ne_10m_admin_1_states_provinces.geojson')
dump('espana_prov', [dict(name=r.name, region=r.region, rings=rings(r.geometry, 0.01, 0.0005)) for r in a[a.adm0_a3 == 'ESP'].itertuples()])
dump('alemania', [dict(name=r.name, rings=rings(r.geometry, 0.02, 0.001)) for r in a[a.adm0_a3 == 'DEU'].itertuples()])
dump('suiza', [dict(name=r.name, rings=rings(r.geometry, 0.005, 0.0002)) for r in a[a.adm0_a3 == 'CHE'].itertuples()])
dump('eeuu', [dict(name=r.name, postal=r.postal, rings=rings(r.geometry, 0.05, 0.01)) for r in a[a.adm0_a3 == 'USA'].itertuples()])
