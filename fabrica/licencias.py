"""Control de licencias y créditos de DocuVox (lista master: docs/RECURSOS.md).

Un único máster sale en YouTube e iVoox. Música, efectos y audio de archivo deben valer para los dos destinos;
la imagen solo para YouTube, salvo la miniatura (también va a iVoox en versión cuadrada).
Si un recurso necesita crédito y no lo tiene, el episodio NO se publica (out/licencias_estado.txt).

Salida en out/: licencias.json (ficha de cada recurso), creditos_publicos.txt (texto para la descripción de YouTube
e iVoox), licencias_estado.txt (PUBLICAR: SÍ / NO, bloqueos y avisos) y, si hace falta, locucion_cierre.txt.
"""
import json, re, datetime

# credito: plantilla del crédito público ({title}, {author}, {license}); None = no exige crédito.
# multi: vale para YouTube + iVoox. solo_yt: solo YouTube (prohibido en el audio del máster).
FUENTES = {
    # 0 · v7 (especial elecciones): fuentes institucionales y cita audiovisual
    'moncloa':      dict(nombre='La Moncloa', dominios=('lamoncloa.gob.es',), licencia='Reutilización con cita de la fuente (aviso legal de La Moncloa)',
                         credito='Imágenes y declaraciones: La Moncloa ({title})', multi=True),
    'congreso':     dict(nombre='Congreso de los Diputados', dominios=('congreso.es',), licencia='Reutilización con cita de la fuente (Ley 37/2007)',
                         credito='Archivo audiovisual del Congreso de los Diputados ({title})', multi=True),
    'senado':       dict(nombre='Senado de España', dominios=('senado.es',), licencia='Reutilización con cita de la fuente (Ley 37/2007)',
                         credito='Archivo audiovisual del Senado ({title})', multi=True),
    'poder_judicial': dict(nombre='Poder Judicial', dominios=('poderjudicial.es',), licencia='Reutilización con cita de la fuente (CENDOJ / CGPJ)',
                         credito='Fuente: Poder Judicial ({title})', multi=True),
    'boe':          dict(nombre='BOE', dominios=('boe.es',), licencia='Reutilización con cita de la fuente', credito='Fuente: BOE ({title})', multi=True),
    'cita':         dict(nombre='Cita audiovisual (art. 32 LPI)', dominios=(), licencia='Cita con fin de análisis y crítica (art. 32 LPI)',
                         credito='Fragmento citado con fin de análisis: {title}', multi=True,
                         nota='fragmento breve, con fuente en pantalla y en la descripción; no es una licencia: puede recibir reclamaciones de Content ID'),
    # 1-2 · lugar o hecho real y archivo español
    'wikimedia':    dict(nombre='Wikimedia Commons', dominios=('wikimedia.org', 'wikipedia.org'), licencia='', credito='por_licencia'),
    'bne':          dict(nombre='Biblioteca Nacional de España', dominios=('bne.es',), licencia='CC BY 4.0',
                         credito='Imágenes procedentes de los fondos de la Biblioteca Nacional de España', fijo=True),
    'cnig':         dict(nombre='CNIG', dominios=('cnig.es', 'ign.es'), licencia='CC BY 4.0 (ign.es)', credito='{title} © Instituto Geográfico Nacional / CNIG'),
    # 3 · cine y archivo histórico
    'archive':      dict(nombre='Internet Archive / Prelinger', dominios=('archive.org',), licencia='', credito='por_licencia',
                         aviso='archivo de cine sin dominio público explícito: confirma derechos de la película y de su banda sonora'),
    'loc':          dict(nombre='Library of Congress', dominios=('loc.gov',), licencia='No known restrictions (LoC)', credito=None),
    'nara':         dict(nombre='US National Archives', dominios=('archives.gov',), licencia='Dominio público (NARA)', credito=None),
    # 4 · arte y foto de época
    'europeana':    dict(nombre='Europeana', dominios=('europeana.eu',), licencia='', credito='por_licencia'),
    'met':          dict(nombre='The Met', dominios=('metmuseum.org',), licencia='CC0', credito=None),
    'cleveland':    dict(nombre='Cleveland Museum of Art', dominios=('clevelandart.org',), licencia='CC0', credito=None),
    'smithsonian':  dict(nombre='Smithsonian Open Access', dominios=('si.edu',), licencia='CC0', credito=None),
    'rijksmuseum':  dict(nombre='Rijksmuseum', dominios=('rijksmuseum.nl',), licencia='CC0', credito=None),
    # 5-6 · mapas, satélite y ciencia
    'naturalearth': dict(nombre='Natural Earth', dominios=('naturalearthdata.com', 'nvkelso/natural-earth'), licencia='Dominio público', credito=None),
    'landsat':      dict(nombre='Landsat (USGS)', dominios=('usgs.gov',), licencia='Dominio público', credito=None),
    'copernicus':   dict(nombre='Copernicus', dominios=('copernicus.eu',), licencia='Copernicus Sentinel data',
                         credito='Contiene datos Copernicus Sentinel modificados ({title})'),
    'nasa':         dict(nombre='NASA', dominios=('nasa.gov',), licencia='NASA (dominio público)', credito=None,
                         aviso='NASA: revisa en la ficha que no sea material de terceros'),
    'eso':          dict(nombre='ESO', dominios=('eso.org',), licencia='CC BY 4.0', credito='{title} — ESO'),
    'esahubble':    dict(nombre='ESA/Hubble', dominios=('esahubble.org', 'spacetelescope.org'), licencia='CC BY 4.0', credito='{title} — ESA/Hubble'),
    'noaa':         dict(nombre='NOAA', dominios=('noaa.gov',), licencia='Dominio público', credito=None),
    # 7 · stock de apoyo
    'pexels':       dict(nombre='Pexels', dominios=('pexels.com',), licencia='Pexels License', credito=None),
    'coverr':       dict(nombre='Coverr', dominios=('coverr.co',), licencia='Coverr License', credito=None,
                         aviso='Coverr: confirma que el clip no es premium, patrocinado ni generado por IA'),
    'mixkit_video': dict(nombre='Mixkit', dominios=('mixkit.co/free-stock-video',), licencia='Mixkit Stock Video Free License', credito=None),
    'pixabay':      dict(nombre='Pixabay', dominios=('pixabay.com',), licencia='Pixabay Content License', credito=None),
    'dareful':      dict(nombre='Dareful', dominios=('dareful.com',), licencia='CC BY 4.0', credito='Vídeo: {title} — Dareful (CC BY 4.0)'),
    'unsplash':     dict(nombre='Unsplash', dominios=('unsplash.com',), licencia='Unsplash License', credito=None),
    # 8 · música (se elige antes del montaje)
    'mixkit_music': dict(nombre='Mixkit Music', dominios=('mixkit.co/free-stock-music', 'assets.mixkit.co/music'), licencia='Mixkit Stock Music Free License',
                         credito=None, multi=True, nota='no registrar en Content ID; no usar en pistas solo musicales ni en TV/radio'),
    'buckley':      dict(nombre='Scott Buckley', dominios=('scottbuckley.com.au',), licencia='CC BY 4.0', multi=True,
                         credito='Música: {title} by Scott Buckley – released under CC-BY 4.0. www.scottbuckley.com.au'),
    'incompetech':  dict(nombre='Incompetech', dominios=('incompetech.com', 'incompetech.filmmusic.io'), licencia='CC BY 4.0', multi=True,
                         credito='Música: {title} Kevin MacLeod (incompetech.com) – Licensed under Creative Commons: By Attribution 4.0',
                         locucion='Música de Kevin MacLeod, incompetech punto com, con licencia Creative Commons Atribución 4.0.'),
    'youtube_cc':   dict(nombre='Biblioteca de audio de YouTube (CC)', dominios=(), licencia='CC BY 4.0', multi=True, credito='{author}'),
    'youtube_std':  dict(nombre='Biblioteca de audio de YouTube (licencia estándar)', dominios=(), licencia='YouTube Audio Library License',
                         credito=None, solo_yt=True),
    'pixabay_music': dict(nombre='Pixabay Music', dominios=('pixabay.com/music', 'cdn.pixabay.com/audio'), licencia='Pixabay Content License', credito=None,
                          aviso='Pixabay Music es último recurso: riesgo de reclamaciones de terceros en YouTube'),
    'openverse':    dict(nombre='Openverse / ccMixter', dominios=('ccmixter.org', 'openverse.org'), licencia='', credito='por_licencia'),
    # 9 · efectos y ambientes
    'sonniss':      dict(nombre='Sonniss GDC Bundle', dominios=('sonniss.com',), licencia='Sonniss #GameAudioGDC License', credito=None, multi=True,
                         nota='guardar el texto de la licencia junto al lote; no entrenar IA; no redistribuir suelto'),
    'freesound':    dict(nombre='Freesound', dominios=('freesound.org',), licencia='', credito='por_licencia', multi=True),
    'mixkit_sfx':   dict(nombre='Mixkit SFX', dominios=('mixkit.co/free-sound-effects', 'assets.mixkit.co/active_storage/sfx'), licencia='Mixkit Sound Effects Free License', credito=None, multi=True),
    '99sounds':     dict(nombre='99Sounds', dominios=('99sounds.org',), licencia='99Sounds License', credito=None, multi=True),
    'zapsplat':     dict(nombre='ZapSplat', dominios=('zapsplat.com',), licencia='ZapSplat Standard License (Basic)', multi=True,
                         credito='Sound effects obtained from https://www.zapsplat.com', fijo=True),
}
AUDIO_KINDS = ('música', 'sonido')
# Modo seguro (por defecto; "seguro": false en job.json lo desactiva): solo fuentes con licencia comercial explícita.
# Fuera siempre: Coverr Pixabay Music y Openverse/ccMixter (riesgo de terceros), Biblioteca de YouTube estándar.
# Cualquier aviso bloquea, salvo recursos manuales marcados "revisado": true tras comprobar su ficha.
VETADAS_SEGURO = ('pexels', 'coverr', 'pixabay_music', 'openverse', 'youtube_std')
PROPIOS = ('ia', 'elevenlabs', 'docuvox', 'narrador')  # material propio: no va a los créditos públicos ni se revisa


def detecta(c):
    """Nombre de la fuente de un recurso (campo 'fuente' o dominio de la página / URL)."""
    if c.get('fuente') in FUENTES: return c['fuente']
    txt = f"{c.get('page', '')} {c.get('url', '')}".lower()
    best = None
    for k, f in FUENTES.items():  # el dominio más específico gana (mixkit.co/free-stock-music antes que mixkit.co)
        for d in f['dominios']:
            if d in txt and (best is None or len(d) > best[1]): best = (k, len(d))
    if best: return best[0]
    cr = str(c.get('credit', '')).lower()
    if 'incompetech' in cr: return 'incompetech'
    if 'freesound' in cr: return 'freesound'
    return None


def _lic(c, f):
    return (c.get('license') or (f or {}).get('licencia') or '').strip()

def _es_by(lic):
    l = lic.lower()
    return bool(re.search(r'(^|[^a-z])(cc[ -]?)?by([ -]|/|$)', l)) or '/licenses/by' in l or 'attribution' in l

def _es_libre(lic):
    l = lic.lower()
    return any(x in l for x in ('cc0', 'publicdomain', 'public domain', 'dominio público', 'pdm', 'zero', 'no known restrictions', 'no restrictions'))

def _nc(lic): l = lic.lower(); return 'noncommercial' in l or bool(re.search(r'(^|[^a-z])nc([^a-z]|$)', l)) or '-nc' in l
def _nd(lic): l = lic.lower(); return 'noderiv' in l or bool(re.search(r'(^|[^a-z])nd([^a-z]|$)', l)) or '-nd' in l
def _sa(lic): l = lic.lower(); return 'sharealike' in l or bool(re.search(r'(^|[^a-z])sa([^a-z]|$)', l)) or '-sa' in l

def propio(c):
    cr = str(c.get('credit', '')).strip().lower()
    return cr in PROPIOS or str(c.get('id', '')).startswith('ai') or 'elevenlabs' in f"{c.get('url', '')} {cr}"


def credito_publico(kind, c, fuente):
    """Línea de crédito exacta para la descripción, o None si la fuente no exige crédito."""
    f = FUENTES.get(fuente) or {}
    lic = _lic(c, f); title = c.get('title') or c.get('name') or ''
    title = re.sub(r'^(File|Archivo):', '', str(title)); title = re.sub(r'\.(ogg|mp3|wav|flac|jpe?g|png|tiff?|webm|mp4)$', '', title, flags=re.I).strip()
    tpl = f.get('credito')
    if tpl == 'por_licencia' or (tpl is None and fuente is None):
        if not _es_by(lic): return None
        autor = str(c.get('credit', '')).strip()
        return f"{kind.capitalize()}: {title + ' — ' if title else ''}{autor} · {lic} · {c.get('page', '')}".strip(' ·')
    if tpl is None: return None
    if tpl == '{author}': return str(c.get('credit', '')).strip() or None
    return tpl.format(title=title or 'pista', author=c.get('credit', ''), license=lic)


def revisa(credits, job=None):
    """Devuelve (fichas, bloqueos, avisos) para la lista [(tipo, recurso), ...] del motor."""
    job = job or {}; fichas, bloq, avis = [], [], []; seen = set(); hoy = datetime.date.today().isoformat()
    seguro = job.get('seguro', True)
    for kind, c in credits:
        cid = c.get('id') or c.get('url')
        if cid in seen or propio(c): continue
        seen.add(cid)
        fu = detecta(c); f = FUENTES.get(fu) or {}; lic = _lic(c, f); audio = kind in AUDIO_KINDS
        cr = credito_publico(kind, c, fu)
        ref = f"[{kind}] {c.get('title') or c.get('credit') or cid} ({f.get('nombre', fu or 'fuente desconocida')})"
        necesita = bool(f.get('credito')) and f.get('credito') != 'por_licencia' or _es_by(lic)
        if not lic: bloq.append(f'{ref}: sin licencia registrada')
        elif _nc(lic): bloq.append(f'{ref}: licencia no comercial ({lic})')
        elif audio and _nd(lic): bloq.append(f'{ref}: licencia sin obras derivadas ({lic}); el audio se corta y se mezcla')
        elif not fu and not (_es_libre(lic) or _es_by(lic)): bloq.append(f'{ref}: fuente desconocida y licencia no reconocida ({lic})')
        if audio and f.get('solo_yt'): bloq.append(f'{ref}: solo vale para YouTube y el audio del máster también va a iVoox')
        if necesita and not cr: bloq.append(f'{ref}: necesita crédito y no lo tiene')
        if necesita and cr and fu in ('youtube_cc',) and len(cr) < 20: bloq.append(f'{ref}: copia el texto completo del icono CC de YouTube Studio')
        if _sa(lic):
            permitir = (job or {}).get('permitir_sa', True) and not audio   # imagen y vídeo: sí, con crédito (19-11-2026); música: no
            if seguro and not permitir: bloq.append(f'{ref}: licencia CompartirIgual ({lic}) vetada en modo seguro')
            elif not seguro: avis.append(f'{ref}: licencia CompartirIgual ({lic}); acredita y no la uses en la miniatura')
        aviso = f.get('aviso')
        if fu == 'archive' and _es_libre(lic) and not audio: aviso = None          # dominio público explícito en la ficha
        if fu == 'nasa' and not c.get('fuente'): aviso = None                      # búsqueda NASA: ya descarta material de terceros
        if c.get('revisado'): aviso = None
        if aviso: (bloq if seguro else avis).append(f'{ref}: {aviso}' + (' (marca "revisado": true tras comprobar la ficha)' if seguro and c.get('fuente') else ''))
        if seguro and fu in VETADAS_SEGURO: bloq.append(f'{ref}: fuente vetada en modo seguro')
        if seguro and audio and fu == 'archive': bloq.append(f'{ref}: música/sonido de Internet Archive vetado en modo seguro (licencia puesta por quien lo sube)')
        fichas.append(dict(tipo=kind, fuente=fu or 'desconocida', nombre_fuente=f.get('nombre', ''), titulo=c.get('title') or c.get('name') or '',
                           autor=c.get('credit', ''), licencia=lic, pagina=c.get('page', ''), url=c.get('url', ''), fecha_descarga=hoy,
                           credito=cr or '', destinos=['youtube', 'ivoox'] if audio else ['youtube'], nota=f.get('nota', '')))
    # Incompetech en pódcast: crédito locutado al cierre de iVoox (pauta prudente)
    if any(x['fuente'] == 'incompetech' for x in fichas):
        texto = ' '.join(str(u.get('text', '')) for u in (job.get('units') or [])[-6:]).lower()
        if 'macleod' not in texto: (bloq if seguro else avis).append('Incompetech: añade al cierre la línea de locucion_cierre.txt (versión iVoox)')
    return fichas, bloq, avis


def escribe(out_dir, credits, job=None):
    """Escribe licencias.json, creditos_publicos.txt, licencias_estado.txt y locucion_cierre.txt. Devuelve True si se puede publicar."""
    fichas, bloq, avis = revisa(credits, job)
    json.dump(fichas, open(f'{out_dir}/licencias.json', 'w'), ensure_ascii=False, indent=1)
    orden = {'música': 0, 'vídeo': 1, 'archivo': 2, 'sonido': 3}
    lines = []
    for x in sorted(fichas, key=lambda x: orden.get(x['tipo'], 9)):
        if x['credito'] and x['credito'] not in lines: lines.append(x['credito'])
    open(f'{out_dir}/creditos_publicos.txt', 'w').write(
        ('Créditos\n' + '\n'.join(lines) + '\n') if lines else 'Créditos\nMaterial de archivo y stock con licencias abiertas que no exigen atribución.\n')
    loc = [FUENTES[k]['locucion'] for k in {x['fuente'] for x in fichas} if FUENTES.get(k, {}).get('locucion')]
    if loc: open(f'{out_dir}/locucion_cierre.txt', 'w').write('\n'.join(loc) + '\n')
    ok = not bloq
    est = [f"PUBLICAR: {'SÍ' if ok else 'NO'}", f"modo: {'seguro' if (job or {}).get('seguro', True) else 'normal'} · recursos revisados: {len(fichas)} · créditos públicos: {len(lines)}", '']
    if bloq: est += ['BLOQUEOS (corregir antes de publicar):'] + [f'- {b}' for b in bloq] + ['']
    if avis: est += ['AVISOS (revisar):'] + [f'- {a}' for a in avis] + ['']
    est += ['Si llega una reclamación de Content ID: disputa con la ficha del recurso en licencias.json (página, licencia y fecha).',
            'Antes de publicar: pega creditos_publicos.txt en la descripción de YouTube y de iVoox, sube en privado y revisa las comprobaciones de Studio.']
    open(f'{out_dir}/licencias_estado.txt', 'w').write('\n'.join(est) + '\n')
    return ok, bloq, avis
