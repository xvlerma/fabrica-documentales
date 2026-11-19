#!/usr/bin/env python3
"""Publica un documental terminado en YouTube (API de datos v3).

Uso: python3 fabrica/publish.py jobs/<id>
Lee jobs/<id>/youtube.json y los archivos de jobs/<id>/out/.
Secrets necesarios (entorno): YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN.

youtube.json:
{
  "title": "...", "description": "...", "tags": ["..."],
  "category": "27", "lang": "es-ES",
  "thumb": "miniatura_B",            # sufijo del archivo de out/
  "publish_at": "2026-11-20T17:00:00Z",   # opcional; si falta, se programa en la próxima hora punta
  "synthetic": false                  # «Uso de IA» (decisión del creador)
}
Escribe out/youtube_publicado.json con el id y el enlace.
"""
import datetime as dt
import glob
import json
import os
import sys
import time

import requests

API = 'https://www.googleapis.com'


def token():
    r = requests.post('https://oauth2.googleapis.com/token', data={
        'client_id': os.environ['YT_CLIENT_ID'], 'client_secret': os.environ['YT_CLIENT_SECRET'],
        'refresh_token': os.environ['YT_REFRESH_TOKEN'], 'grant_type': 'refresh_token'}, timeout=60)
    r.raise_for_status()
    return r.json()['access_token']


def proxima_hora_punta(min_espera_h=2, hora_local=18):
    """Próxima 18:00 de Madrid con al menos 2 h de margen (comprobación de derechos y procesado HD)."""
    ahora = dt.datetime.now(dt.timezone.utc)
    off = 2 if 3 < ahora.month < 11 else 1  # aproximación CET/CEST
    d = ahora.replace(minute=0, second=0, microsecond=0)
    d = d.replace(hour=(hora_local - off) % 24)
    while d < ahora + dt.timedelta(hours=min_espera_h):
        d += dt.timedelta(days=1)
    return d.strftime('%Y-%m-%dT%H:%M:%SZ')


def subir_video(tk, path, meta):
    status = {'privacyStatus': 'private', 'publishAt': meta['publish_at'],
              'selfDeclaredMadeForKids': False, 'containsSyntheticMedia': bool(meta.get('synthetic', False)),
              'license': 'youtube', 'embeddable': True}
    body = {'snippet': {'title': meta['title'][:100], 'description': meta['description'][:5000],
                        'tags': meta.get('tags', []), 'categoryId': meta.get('category', '27'),
                        'defaultLanguage': meta.get('lang', 'es-ES'), 'defaultAudioLanguage': meta.get('lang', 'es-ES')},
            'status': status}
    size = os.path.getsize(path)
    r = requests.post(f'{API}/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status',
                      headers={'Authorization': f'Bearer {tk}', 'Content-Type': 'application/json; charset=UTF-8',
                               'X-Upload-Content-Type': 'video/mp4', 'X-Upload-Content-Length': str(size)},
                      data=json.dumps(body), timeout=120)
    r.raise_for_status()
    url = r.headers['Location']
    chunk = 64 * 1024 * 1024
    pos = 0
    with open(path, 'rb') as f:
        while pos < size:
            f.seek(pos)
            data = f.read(chunk)
            end = pos + len(data) - 1
            for intento in range(5):
                try:
                    rr = requests.put(url, data=data, timeout=600, headers={
                        'Authorization': f'Bearer {tk}', 'Content-Range': f'bytes {pos}-{end}/{size}'})
                    break
                except requests.RequestException:
                    time.sleep(10 * (intento + 1))
            else:
                raise SystemExit('subida interrumpida')
            if rr.status_code in (200, 201):
                return rr.json()
            if rr.status_code == 308:
                rng = rr.headers.get('Range')
                pos = int(rng.split('-')[1]) + 1 if rng else 0
                print(f'   subido {pos * 100 // size} %', flush=True)
                continue
            raise SystemExit(f'error de subida {rr.status_code}: {rr.text[:300]}')
    raise SystemExit('la subida terminó sin respuesta final')


def main(jobdir):
    meta = json.load(open(os.path.join(jobdir, 'youtube.json')))
    out = os.path.join(jobdir, 'out')
    mp4 = sorted(glob.glob(os.path.join(out, '*.mp4')))[0]
    base = mp4[:-4]
    meta.setdefault('publish_at', proxima_hora_punta())
    tk = token()
    print('== publicando en YouTube:', meta['title'], '· sale el', meta['publish_at'])
    v = subir_video(tk, mp4, meta)
    vid = v['id']
    res = {'id': vid, 'url': f'https://youtu.be/{vid}', 'publish_at': meta['publish_at'],
           'privacy': v.get('status', {}).get('privacyStatus'), 'avisos': []}
    th = f"{base}_{meta.get('thumb', 'miniatura_A')}.jpg"
    if os.path.exists(th):
        r = requests.post(f'{API}/upload/youtube/v3/thumbnails/set?videoId={vid}',
                          headers={'Authorization': f'Bearer {tk}', 'Content-Type': 'image/jpeg'},
                          data=open(th, 'rb').read(), timeout=120)
        if r.status_code != 200:
            res['avisos'].append(f'miniatura no aplicada ({r.status_code}): {r.text[:200]}')
    srt = base + '.srt'
    if os.path.exists(srt):
        meta_c = {'snippet': {'videoId': vid, 'language': meta.get('lang', 'es-ES')[:2], 'name': 'Español'}}
        r = requests.post(f'{API}/upload/youtube/v3/captions?uploadType=multipart&part=snippet',
                          headers={'Authorization': f'Bearer {tk}'},
                          files={'snippet': (None, json.dumps(meta_c), 'application/json'),
                                 'file': ('subs.srt', open(srt, 'rb'), 'application/octet-stream')}, timeout=120)
        if r.status_code not in (200, 201):
            res['avisos'].append(f'subtítulos no aplicados ({r.status_code}): {r.text[:200]}')
    # comprobación: si YouTube bloquea el vídeo en privado (proyecto sin auditar), avisarlo claramente
    time.sleep(20)
    r = requests.get(f'{API}/youtube/v3/videos?part=status&id={vid}',
                     headers={'Authorization': f'Bearer {tk}'}, timeout=60).json()
    st = (r.get('items') or [{}])[0].get('status', {})
    res['estado'] = st
    if st.get('publishAt') is None and st.get('privacyStatus') == 'private':
        res['avisos'].append('YouTube ha quitado la fecha de publicación: el proyecto de la API está bloqueado en privado. '
                             'Hay que publicarlo a mano en YouTube Studio o pedir la auditoría de la API.')
    json.dump(res, open(os.path.join(out, 'youtube_publicado.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main(sys.argv[1])
