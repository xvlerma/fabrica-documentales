#!/usr/bin/env python3
"""Coherencia imagen-locución: elige, para cada búsqueda del job, SOLO candidatos que muestran
lo que dice la locución, y lista los planos que se quedan sin material para que se cubran con
imagen IA (escenas) o con mapa/tarjeta (datos), nunca con relleno genérico.

Uso (después del casting, antes del render):
    python3 fabrica/coherencia.py jobs/<id>/job.json <carpeta_out> > jobs/<id>/qpicks.json

En el job:
    "lugares":    {"oymyakon": ["oymyakon", "oimiakon", "tomtor"], ...}   # palabras que identifican cada sitio
    "prohibidas": ["putin", "airbus", "stamp", ...]                     # temas que nunca deben salir
    "permitidas": ["stamp", "portrait"]                                 # quita prohibidas genéricas cuando son el tema
    "permitir_sa": true                                                  # CC BY-SA permitido en imagen y vídeo (decisión del creador, 19-11-2026)
    plano:  {"photo": "Oymyakon winter", "lugar": "oymyakon"}           # opcional: fija el sitio del plano
            {"video": "snow storm", "generico": true}                   # solo si la frase NO habla de un sitio concreto (sin rótulo de lugar)

Salida: qpicks (JSON) por stdout e informe por stderr:
    FALTA <clave> → <n> planos sin material coherente: cambia esos planos a {"ai": ...} o a una tarjeta/mapa.
"""
import json
import re
import sys

PROHIBIDAS_BASE = ['stamp', 'sello postal', 'flag of', 'bandera', 'coat of arms', 'escudo', 'logo', 'map of', 'locator map',
                   'putin', 'president', 'minister', 'portrait', 'selfie', 'airbus', 'boeing', 'aeroflot', 'airlines', 'airport',
                   'diagram', 'chart', 'graph', 'srtm', 'banner of', 'erasmus', 'wedding', 'concert']


def lic_ok(lic, permitir_sa):
    l = (lic or '').lower()
    if re.search(r'(^|[^a-z])nc([^a-z]|$)', l) or 'noncommercial' in l: return False
    if re.search(r'(^|[^a-z])nd([^a-z]|$)', l) or 'noderiv' in l: return False
    sa = 'sharealike' in l or bool(re.search(r'(^|[^a-z])sa([^a-z]|$)', l.replace('usa', '').replace('nasa', '')))
    return permitir_sa or not sa


def texto(c):
    return ' '.join(str(c.get(k) or '') for k in ('title', 'tags', 'page', 'credit')).lower()


def lugar_de(t, lugares):
    t = t.lower()
    for lid, ws in lugares.items():
        if any(w.lower() in t for w in ws): return lid
    return None


def main(job_path, out):
    job = json.load(open(job_path))
    lugares = job.get('lugares', {})
    perm = {p.lower() for p in job.get('permitidas', [])}   # genéricas que en este tema SÍ son el asunto (p. ej. sellos)
    prohib = [p for p in PROHIBIDAS_BASE if p not in perm] + [p.lower() for p in job.get('prohibidas', [])]
    permitir_sa = job.get('permitir_sa', True)
    castq = json.load(open(f'{out}/castq.json'))
    edl = json.load(open(f'{out}/edl.json'))
    planos = {}
    for s in edl:
        sp = s.get('spec', {})
        for kind in ('photo', 'video'):
            if kind in sp:
                k = f'{kind}:{sp[kind]}'
                d = planos.setdefault(k, dict(n=0, lugar=sp.get('lugar'), generico=sp.get('generico', False)))
                d['n'] += 1
    qp, faltan = {}, []
    for k, d in planos.items():
        lid = d['lugar'] or lugar_de(k, lugares)
        buenos = []
        for c in castq.get(k, []):
            t = texto(c)
            if not lic_ok(c.get('license'), permitir_sa) or any(p in t for p in prohib): continue
            if lid and lugar_de(t, {lid: lugares.get(lid, [lid])}) != lid: continue   # tiene que ser ESE sitio
            if not lid and not d['generico']: continue                                 # sin sitio ni marca de genérico: no se adivina
            buenos.append(c)
        if buenos: qp[k] = buenos
        necesarios = max(1, (d['n'] + 1) // 2)   # cada candidato puede repetirse como mucho 2 veces
        if len(buenos) < necesarios:
            faltan.append((k, d['n'], len(buenos)))
    for k, n, b in faltan:
        print(f'FALTA {k} → {n} planos, {b} candidatos coherentes: pasa los que falten a imagen IA (escena) o a mapa/tarjeta (dato)', file=sys.stderr)
    print(f'{len(qp)} de {len(planos)} búsquedas con material coherente', file=sys.stderr)
    json.dump(qp, sys.stdout, ensure_ascii=False)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
