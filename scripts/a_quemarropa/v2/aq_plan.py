"""Plan de segmentos: cada fila del EDL -> dict(n, D, pieces, ov, audio, kind, src_tc...)."""
from aq_build import *

FILE_RE = re.compile(r'((?:cortes_externos/(?:r\d+|c\d)/|cortes_externos/|cortes_rebajados/|cortes/|archivo/|capturas/)?[\w\-\.\(\)]+?\.(?:mp4|jpg|png))(?:\s*·\s*(\d+:\d+)\s*-\s*(\d+:\d+))?')
CODE_RE = re.compile(r'\[(L1|D1|Q1|N1|R2|S1|M1|C1|T1|K1|T2|X1|X0|Z1|P1)\]')
LASTV = {'p': None}

def refs_of(V):
    out = []
    ms = list(FILE_RE.finditer(V))
    for i, m in enumerate(ms):
        ctx = V[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(V)]
        out.append(dict(ref=m.group(1), a=secs(m.group(2)) if m.group(2) else None, b=secs(m.group(3)) if m.group(3) else None, ctx=ctx, path=findf(m.group(1))))
    return out

def quotes(s): return re.findall(r'«([^»]+)»', s or '')

def q1bg():
    if not LASTV['p']: return None
    p, t, crop = LASTV['p']
    k = 'q1bg_' + hashlib.md5(f'{p}{t}'.encode()).hexdigest()[:8]
    return Image.open(frame_at(p, t, k, sat=0.2, dark=0.6, crop=crop)).convert('RGBA')

def ref_piece(n, rf, dur, blur=0):
    p = rf['path']; ctx = rf['ctx']
    if not p: inc(n, f'recurso no encontrado en disco: {rf["ref"]}'); return None
    if p.lower().endswith(('.jpg', '.png', '.jpeg')):
        z = 0.12 if 'zoom' in ctx else 0.04
        return P_img(capture_png(p, hashlib.md5(p.encode()).hexdigest()[:8] + (f'_b{blur}' if blur else '')), dur, z=z, blur=8 if 'desenfocad' in ctx else 0)
    pr = probe(p); fd = pr['dur'] or 10
    if re.search(r'fotograma|congelad|último plano|se oscurece', ctx) or re.search(r'[Ff]otograma de\s*$', ''):
        t = 0.5 if 'primer' in ctx else (fd - 1.0 if 'último' in ctx else fd * 0.4)
        fx = fx_for(p, t); crop = fx['crop'] if fx else None
        if not crop and re.search(r'/(cortes_externos|archivo)/', p): crop = 'iw*0.76:ih*0.76:iw*0.12:ih*0.10'
        return P_img(frame_at(p, t, 'fr_' + hashlib.md5(f'{p}{t}'.encode()).hexdigest()[:8], crop=crop), dur, z=0.03, fade_dark='oscurece' in ctx)
    if rf['a'] is not None: ss, ln = rf['a'], (rf['b'] - rf['a'])
    else:
        ss = min(8.0, fd * 0.15) if '/archivo/' in p else (0.3 if fd > 3 else 0)
        ln = max(0.5, fd - ss - (10 if fd > 60 else 0.3))
    fx = fx_for(p, ss); crop = fx['crop'] if fx else None
    if not crop and re.search(r'/(cortes_externos|archivo)/', p): crop = 'iw*0.76:ih*0.76:iw*0.12:ih*0.10'
    if ln + 0.05 < dur:
        room = fd - ss - (10 if fd > 60 else 0.3)
        if room >= dur and 'faldón' not in ctx:
            inc(n, f'{os.path.basename(p)}: el tramo indicado ({ln:.1f} s) no llena la locución ({dur:.1f} s); el plano sigue corriendo {dur - ln:.1f} s más (mismo plano, sin audio)'); ln = dur
        else: inc(n, f'{os.path.basename(p)}: tramo de {ln:.1f} s para {dur:.1f} s de plano; se congela el último fotograma {dur - max(ln, room):.1f} s'); ln = max(ln, min(room, dur))
    return P_clip(p, ss, dur, src_len=ln, crop=crop, blur=blur, z=0.06 if ln < dur - 0.3 else 0.0)

def split_even(D, k): return [round(D / k, 3)] * (k - 1) + [round(D - round(D / k, 3) * (k - 1), 3)]

def date_items(text, maxn=5):
    """hitos (fecha, texto) desde una locución: años y fechas escritos en letra"""
    yrs = {'dos mil cuatro': '2004', 'dos mil nueve': '2009', 'dos mil once': '2011', 'dos mil trece': '2013', 'dos mil catorce': '2014', 'dos mil dieciocho': '2018',
           'dos mil veinte': '2020', 'dos mil veintitrés': '2023', 'dos mil veinticuatro': '2024', 'dos mil veinticinco': '2025', 'dos mil veintiséis': '2026'}
    out = []
    for sent in re.split(r'(?<=[.:;])\s+', text):
        for k in sorted(yrs, key=len, reverse=True):
            if k in sent:
                i = sent.find(k); before = re.sub(r'\s+(en|de|el|del)$', '', sent[:i].strip(' ,.:;')).strip(' ,.:;')
                after = sent[i + len(k):].strip(' ,.:;')
                hito = before if len(before.split()) >= 2 else after
                hito = re.sub(r'^(y|en)\s+', '', hito, flags=re.I)
                hito = ' '.join(hito.split()[:5]).rstrip(',;:')
                hito = hito[:1].upper() + hito[1:]
                out.append((yrs[k], hito)); break
    return out[:maxn]

def l1_items(V, narr):
    m = re.search(r'L1 · (.*?)(?:\s*\[L1\]|\s*\+|$)', V)
    body = (m.group(1) if m else '').replace('cronología', '').strip(' :')
    chunks = [c.strip() for c in re.split(r'→', body) if c.strip()]
    if len(chunks) == 1 and ' / ' in chunks[0]: chunks = [c.strip() for c in chunks[0].split(' / ')]
    items = []
    for c in chunks:
        dm = re.search(r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?|\b(?:19|20)\d\d(?:-\d{4})?\b)', c)
        fe = dm.group(1) if dm else ''
        hi = c.replace(fe, '').strip(' ·:()«»') if fe else c.strip('«» ')
        hi = re.sub(r'\(.*?\)', '', hi).strip()
        if hi.count('«') > hi.count('»'): hi += '»'
        hi = hi[:1].upper() + hi[1:]
        items.append((fe, hi))
    if sum(1 for f, h in items if f) < 2 or re.search(r'hitos|fechas', body):
        di = date_items(narr)
        if len(di) >= 2: return di
    return items or [('', body)]

def d1_parts(s):
    s = s.strip(' ·')
    parts = [p.strip() for p in s.split(' · ')]
    big, label = parts[0], ' · '.join(parts[1:])
    m = re.match(r'^([\d.,≈%€M\s→/✕+\-]+?\d[\d.,%€M]*)\s+([A-Za-zÁÉÍÓÚáéíóúñÑ(«].*)$', big)
    if m and not label: big, label = m.group(1), m.group(2)
    return big.strip(), label.strip()

def gfx(code, V, T, narr, n):
    """gráfico opaco a pantalla completa para la plantilla code"""
    after = re.sub(r'^.*?' + code + r'\s*·\s*', '', V, count=1) if (code + ' ·') in V else V
    after = CODE_RE.sub('', after).strip()
    q = quotes(after)
    if code == 'D1':
        s = q[0] if q else after
        big, label = d1_parts(s)
        return G.d1(big, label)
    if code == 'N1':
        if q: w = q[0]
        elif after.startswith('negro'): w = T or ''
        elif ':' in after: w = after.split(':', 1)[1].strip()
        else: w = re.sub(r'\s*\(.*?\)|\s*sobre negro.*$', '', after)
        return G.n1(w.strip())
    if code == 'L1': return G.l1(l1_items(V, narr))
    if code == 'R2':
        if T and '/' in T: names = [tuple((x.split(' · ', 1) + [''])[:2]) for x in T.split(' / ')]
        elif T: names = [(x, '') for x in T.split(' · ')]
        else:
            nm = re.findall(r'\b[A-ZÁÉÍÓÚÑ]{2,}(?:\s+[A-ZÁÉÍÓÚÑ]{2,})+', after); names = [(x, '') for x in nm] or [('', '')]
        return G.r2([(a.strip(), b.strip()) for a, b in names])
    if code == 'M1':
        m = re.search(r'mapa (?:de )?([A-ZÁÉÍÓÚ][\wáéíóúñ]+)(?:\s*\(([^)]+)\))?', after)
        place = m.group(1).upper() if m else after
        sub = m.group(2) if m and m.group(2) and 'zoom' not in m.group(2) else ''
        if q: sub = (sub + ' · ' if sub else '') + q[-1]
        return G.m1(place, sub)
    if code == 'K1':
        m = re.search(r'«(\d+)»', V); return G.k1(int(m.group(1)) if m else 1, '')
    if code == 'T1':
        lab = T or re.sub(r'^(etiqueta|cabecera fija)\s*', '', after).strip('«» ')
        if q and not T: lab = q[0]
        return G.t1(lab, '')
    if code == 'Q1':
        if n in Q1TXT: return Q1TXT[n]()
        qn = quotes(narr)
        if qn: quote = '«' + max(qn, key=len) + '»'
        elif q: quote = '«' + q[0] + '»'
        else:
            inc(n, 'Q1 sin literal en el EDL: tarjeta de dato con el texto de la locución'); return G.t2(narr)
        return G.q1(quote, T, None)
    if code == 'S1':
        cols = [c.strip(' «»✕✓') for c in re.split(r'\s*\|\s*|\s*/\s*', after.split(':', 1)[-1])]
        cols = [c for c in cols if c and 'sin imagen' not in c and 'con su versión' not in c]
        return G.s1_text([c.replace(' con su versión', '') for c in cols])
    return None

Q1TXT = {
    57: lambda: G.t2('HIZO · 20/05/2020\nEl PSOE y Unidas Podemos firman por escrito con EH Bildu derogar la reforma laboral del PP a cambio de su abstención.'),
    241: lambda: G.t2('Proposición de ley del Grupo Socialista para limitar la acusación popular, aplicable a los procesos abiertos · registrada en enero de 2025 · retirada en noviembre\nEl Debate · 17/11/2025'),
    309: lambda: G.t2('Dirigentes de Podemos: aquellas palabras eran irónicas, una burla de la teoría del reemplazo.'),
    360: lambda: G.q1('«El Gobierno deberá presentar ante el Congreso de los Diputados los Presupuestos Generales del Estado al menos tres meses antes de la expiración de los del año anterior.»', 'Constitución Española · art. 134.3'),
}
def r1_from(T):
    t = clean(T).split(' + ')[0]
    if not t: return None
    parts = [p.strip() for p in t.split(' · ')]
    return G.r1(parts[0], ' · '.join(parts[1:]))

def caps(t): return t and t.upper() == t and len(t) > 3

MED_KEYS = ('VÍA ', 'SEÑAL', 'LA MONCLOA', 'ANTENA 3', 'LASEXTA', 'RTVE', 'TVE', 'ONDA CERO', 'CADENA SER', 'EL MUNDO', 'EL PAÍS', 'RNE',
            'TELECINCO', 'CUATRO', 'EUROPA PRESS', 'OKDIARIO', 'EL CONFIDENCIAL', 'EL INDEPENDIENTE', 'THE WILD PROJECT', 'ACADEMIA', 'ELDIARIO', 'LIBERTAD DIGITAL', 'TIKTOK', 'IMÁGENES', 'PUBLICAD')
R1FIX = {129: 'JORDI WILD LEE UNA PUBLICACIÓN DE PEDRO SÁNCHEZ · THE WILD PROJECT · 13/11/2026'}
def rotulo_corte(n, T, note):
    t = clean(R1FIX.get(n, T)).split(' + ')[0]
    t = re.sub(r'\s*\[[^\]]*\]', '', t).strip(' ·')
    parts = [x.strip() for x in t.split(' · ') if x.strip()]
    tag = None
    if parts and parts[0] in ('DIJO', 'HIZO'): tag = parts.pop(0)
    if parts and parts[0] == 'AUDIO': parts.pop(0)
    if not parts: return None
    name, rest = parts[0], [re.sub(r'^SEÑAL:\s*', '', x) for x in parts[1:]]
    joined = ' · '.join(rest).upper() + ' ' + name.upper()
    if not any(k in joined for k in MED_KEYS):
        m = re.search(r'Origen [^.]*?(vía [^.·;|(]+|señal de[l]? [^.·;|(]+|señal [^.·;|(]+)', note)
        med = m.group(1).strip().upper() if m and 'anotar' not in m.group(1) else None
        if not med:
            if 'CARA A CARA' in joined or 'DEBATE' in joined: med = 'ACADEMIA DE TELEVISIÓN'
            elif 'CONGRESO' in joined or 'SESIÓN DE CONTROL' in joined: med = 'SEÑAL DEL CONGRESO'
            elif 'SENADO' in joined: med = 'SEÑAL DEL SENADO'
        if med: rest.append(med)
    return tag, name, ' · '.join(rest)

# ------------------------------------------------------------------ especiales
ANKARA = next((p for p in ALLF if 'ankara' in os.path.basename(p).lower() and p.endswith('.mp4')), None)
def F_(name): return findf(name)
def lastframe(path): d = probe(path)['dur']; return frame_at(path, d - 0.3, 'lf_' + hashlib.md5(path.encode()).hexdigest()[:8])
def split2(pa, pb, key):
    return card(G.s1_split(Image.open(pa), Image.open(pb)), key)
SIX = ['CONDENADO', 'INVESTIGADO', 'ACUSACIÓN DE UN CONDENADO', 'INDICIO POLICIAL', 'PUBLICADO POR UN MEDIO', 'SIN PRUEBA']
VOZFRAMES = []   # (n, path, t, crop) para el repaso final


# ------------------------------------------------------------------ v2: correcciones fila a fila (notas de revisión del 25/11)
CROP = 'iw*0.76:ih*0.76:iw*0.12:ih*0.10'
def C(img, key, D, z=0.0, dark=False): return P_img(card(img, key), D, z=z, fade_dark=dark)
def CL(path, ss, D, crop=CROP, z=0.0): return P_clip(path, ss, D, src_len=D, crop=crop, z=z)
def SRC(n): s = RES[n]['src'][0]; return s[0], (s[1] or 0), s[2]
def first_sents(t, k=2): return ' '.join(re.split(r'(?<=[.!?])\s+', t)[:k])
def L1anim(items, D, key, z=0.0):
    k = len(items); ds = split_even(D, k)
    return [C(G.l1(items, upto=i + 1), f'{key}_{i}', d) for i, d in enumerate(ds)]
def ov_r1(name, line2, key, a, b, tag=None): return (png(G.r1(name, line2, tag), key), a, b, True)
def o3(n, D, V, T, narr):
    a = frame_at(F_('cortes/clip_39b_usted_no_lo_es.mp4'), probe(F_('cortes/clip_39b_usted_no_lo_es.mp4'))['dur'] * 0.3, 'v2_39b')
    b = frame_at(F_('cortes/clip_39c_feijoo_decente.mp4'), probe(F_('cortes/clip_39c_feijoo_decente.mp4'))['dur'] * 0.5, 'v2_39c')
    la, lb = '2015 · SÁNCHEZ A RAJOY', '2026 · FEIJÓO A SÁNCHEZ'
    img = G.s1_split(Image.open(a), Image.open(b), la, lb) if n == 3 else G.s1_split(Image.open(b), Image.open(a), lb, la)
    return [C(img, f'v2_s1_{n}', D, z=0.02)], []
OVR = {
    3: o3, 445: o3,
    31: lambda n, D, V, T, narr: ([CL(SRC(29)[0], SRC(29)[1] + 0.5, D, crop=None)], []),
    24: lambda n, D, V, T, narr: (L1anim([('2004', 'Concejal de rebote'), ('2009', 'Diputado de rebote, por la baja de Pedro Solbes'), ('2011', 'Fuera'), ('2013', 'Dentro otra vez, por la baja de Cristina Narbona'), ('2014', 'Secretario general del PSOE: 49 % frente a 36 %')], round(D - 4, 2), 'v2_l24') + [ref_piece(n, refs_of(V)[0], 4)], []),
    32: lambda n, D, V, T, narr: ([CL(F_('cortes/clip_r7_salvados_2016.mp4'), 20.0, round(D * 0.42, 2), crop=None),
                                    C(G.q1('«Durante los viajes realizados, en la promoción de la candidatura…»', 'Sentencia del Tribunal Supremo 418/2026 · 22/06/2026 · p. 25', None, 'LA SENTENCIA · HECHOS PROBADOS'), 'v2_q32', D - round(D * 0.42, 2))], []),
    61: lambda n, D, V, T, narr: ([CL(F_('archivo/co_cumplimiento_integro__01__0Ir2CrNDq0U.mp4'), 3.0, D)], []),
    75: lambda n, D, V, T, narr: ([P_img(frame_at(SRC(76)[0], SRC(76)[1] + 1.0, 'v2_f75'), D, z=0.04)], []),
    78: lambda n, D, V, T, narr: ([CL(F_('cortes/clip_33b_acorde_constitucion.mp4'), 0.3, round(D * 0.55, 2), crop=None), C(G.d1('179 votos', 'Investidura de Pedro Sánchez · 16/11/2023'), 'v2_d78', D - round(D * 0.55, 2))],
                                   [(png(G.cover((0, 790, W, H)), 'band'), 0, round(D * 0.55, 2), False), ov_r1('Investidura', '16/11/2023 · Congreso de los Diputados', 'v2_r78', 0.3, round(D * 0.55, 2) - 0.1, 'HIZO')]),
    84: lambda n, D, V, T, narr: ([CL(F_('archivo/co_cerdan_waterloo__02__FL0-pEPdqtk.mp4'), 32.0, D)], [ov_r1('Santos Cerdán y Carles Puigdemont', 'Bruselas · imágenes: La Vanguardia', 'v2_r84', 0.3, D - 0.1)]),
    87: lambda n, D, V, T, narr: ([CL(F_('archivo/ul_puigdemont_perpinan__02.mp4') or F_('archivo/ul_puigdemont_perpinan__01__Anj24ocXO4g.mp4'), 2.0, D, crop=None)], []),
    100: lambda n, D, V, T, narr: ([CL(SRC(54)[0], SRC(54)[1], D, crop=None)], [ov_r1('Pedro Sánchez y Pablo Iglesias', 'Firma del acuerdo de coalición · 12/11/2019', 'v2_r100', 0.3, D - 0.1)]),
    101: lambda n, D, V, T, narr: ([C(G.d1('14/03/2020', 'Estado de alarma'), 'v2_d101', D)], []),
    103: lambda n, D, V, T, narr: ([P_img(capture_png(F_('capturas/cap_d17_boe_stc_148_2021-01.png'), 'v2_c103'), D, z=0.04)], [(png(G.pie('BOE · STC 148/2021 y 183/2021'), 'v2_p103'), 0.4, D - 0.1, True)]),
    107: lambda n, D, V, T, narr: ([CL(F_('cortes_externos/28b_la_palma_recursos__r-DyWeC6BY8.mp4'), 5.0, round(D * 0.5, 2)), C(G.d1('Hasta 2028', 'Plazo para pagar las ayudas al campo palmero · Diario de Avisos, 05/12/2025'), 'v2_d107', D - round(D * 0.5, 2))], []),
    112: lambda n, D, V, T, narr: ([C(G.t2(first_sents(narr, 2), kick='LA LEY DEL «SOLO SÍ ES SÍ»'), 'v2_t112', D)], []),
    113: lambda n, D, V, T, narr: ([C(G.d1('1.205 rebajas', '121 excarcelaciones de agresores sexuales · CGPJ, 01/09/2023'), 'v2_d113', D)], []),
    117: lambda n, D, V, T, narr: ([C(G.k1(1, '16/04/2023 · Ley del «solo sí es sí»'), 'v2_k117', D)], []),
    124: lambda n, D, V, T, narr: (L1anim([('2020', 'Contratos de mascarillas en plena pandemia'), ('2023', 'Ábalos vuelve a las listas del PSOE'), ('20/02/2024', 'La Guardia Civil detiene a Koldo García')], round(D * 0.62, 2), 'v2_l124') +
                                    [CL(F_('archivo/ul_foto_aldama__01__IeUah4v6cfg.mp4'), 3.0, D - round(D * 0.62, 2))], []),
    125: lambda n, D, V, T, narr: ([CL(F_('cortes_externos/38_abalos_mocion__(ext)s.mp4'), 5.0, D)], [ov_r1('José Luis Ábalos', 'Congreso de los Diputados', 'v2_r125', 0.3, D - 0.1)]),
    140: lambda n, D, V, T, narr: ([P_img(frame_at(SRC(141)[0], SRC(141)[1] + 1.5, 'v2_f140'), D, z=0.05)], []),
    143: lambda n, D, V, T, narr: ([C(G.t2(narr, kick='INFORMES DE LA UCO'), 'v2_t143', D)], []),
    145: lambda n, D, V, T, narr: ([C(G.s1_text(['INECO\nempresa pública', 'TRAGSATEC\nempresa pública']), 'v2_s145', D)], []),
    148: lambda n, D, V, T, narr: ([C(G.t2('El Mundo publica una foto de Víctor de Aldama con el presidente, tomada en febrero de 2019 en un acto del PSOE en Madrid.', kick='OCTUBRE DE 2024'), 'v2_t148', D)], []),
    176: lambda n, D, V, T, narr: ([C(G.t2('Dimite tras denuncias internas de trabajadoras por presunto acoso. El PSOE tardó cinco meses en darles credibilidad públicamente.', kick='PACO SALAZAR · MONCLOA'), 'v2_t176', D)], []),
    191: lambda n, D, V, T, narr: ([CL(SRC(159)[0], SRC(159)[1] + 0.5, D, crop=None)], [(png(d1ov('27/05/2026 · UCO EN FERRAZ'), 'v2_o191'), 0.5, D - 0.2, True)]),
    192: lambda n, D, V, T, narr: ([P_img(capture_png(F_('capturas/doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg'), 'v2_c192'), D, z=0.03)], [(png(G.pie('Tribunal Supremo · 22/06/2026'), 'v2_p192'), 0.4, D - 0.1, True)]),
    195: lambda n, D, V, T, narr: ([CL(F_('cortes_externos/15_balas__c6Q37Fr03CM.mp4'), 0.3, round(D * 0.55, 2), crop='iw*0.34:ih*0.80:iw*0.64:ih*0.12'), C(G.t1('INVESTIGADA', 'Leire Díez, militante socialista'), 'v2_t195', D - round(D * 0.55, 2))], []),
    202: lambda n, D, V, T, narr: ([C(G.t2(re.sub(r'\s*\((Euronews[^)]*)\)\s*', '', T) + '\nEuronews'), 'v2_t202', D)], []),
    213: lambda n, D, V, T, narr: (L1anim([('24/04/2024', 'Carta a la ciudadanía'), ('25-28/04', 'Cinco días sin agenda'), ('29/04/2024', 'Anuncia que se queda')], D, 'v2_l213'), []),
    214: lambda n, D, V, T, narr: ([C(G.q1('«Aquí no hay caso. Hay fango.»', 'Pedro Sánchez · laSexta · 17/05/2024'), 'v2_q214', D)], []),
    216: lambda n, D, V, T, narr: ([CL(SRC(221)[0], SRC(221)[1] + 0.2, D, crop=None)], [ov_r1('Begoña Gómez', 'Asamblea de Madrid · 13/11/2024', 'v2_r216', 0.3, D - 0.1)]),
    251: lambda n, D, V, T, narr: ([C(G.t2(narr, kick='LA CAUSA DEL FISCAL GENERAL'), 'v2_t251', D)], []),
    269: lambda n, D, V, T, narr: ([CL(F_('archivo/ar_zapatero_audiencia__01__b3nfdmzBoS4.mp4'), 40.0, D)], [ov_r1('José Luis Rodríguez Zapatero', 'Expresidente del Gobierno', 'v2_r269', 0.3, D - 0.1)]),
    271: lambda n, D, V, T, narr: ([CL(F_('archivo/ar_zapatero_audiencia__01__b3nfdmzBoS4.mp4'), 90.0, D)], []),
    280: lambda n, D, V, T, narr: ([ref_piece(n, refs_of(V)[0], round(D / 2, 2)), ref_piece(n, refs_of(V)[1], D - round(D / 2, 2))], [(png(G.pie('CNI · 29/07/2026 · 13:52 · Documento publicado por el Gobierno'), 'v2_p280'), 0.4, D - 0.1, True)]),
    284: lambda n, D, V, T, narr: ([CL(F_('archivo/ar_ceuta_visita_pitos__01__hnL6vOxtYk4.mp4'), 3.0, D)], [ov_r1('Visita a Ceuta', '01/08/2026', 'v2_r284', 0.3, D - 0.1)]),
    289: lambda n, D, V, T, narr: (L1anim([('30/07/2026', 'Crisis en Ceuta'), ('25/08/2026', 'Se reúne el Consejo de Seguridad Nacional, 26 días después'), ('03/09/2026', 'Explicaciones en el Congreso')], D, 'v2_l289'), [(png(G.pie('La Moncloa · 25/08/2026'), 'v2_p289'), 0.4, D - 0.1, True)]),
    299: lambda n, D, V, T, narr: ([C(G.t2('Carta al rey Mohamed VI: el plan de autonomía marroquí pasa a ser, para el Gobierno, «la base más seria, realista y creíble» para el Sáhara Occidental. Sin pasar por el Congreso.', kick='MARZO DE 2022'), 'v2_t299a', round(D * 0.6, 2)),
                                     C(G.t2(first_sents(narr.split('Congreso.', 1)[-1], 3).strip() or 'El Congreso aprueba una resolución contra el giro.', kick='ABRIL DE 2022'), 'v2_t299b', D - round(D * 0.6, 2))], []),
    306: lambda n, D, V, T, narr: ([C(G.t2('Irene Montero celebraba la regularización extraordinaria de inmigrantes.', kick='ENERO DE 2026 · MITIN DE PODEMOS EN ZARAGOZA'), 'v2_t306', D)], []),
    312: lambda n, D, V, T, narr: ([C(G.t2('Los aliados aceptan subir el gasto en defensa hasta el 5 %. España dice que no lo hará.', kick='JUNIO DE 2025 · CUMBRE DE LA OTAN EN LA HAYA'), 'v2_t312', round(D * 0.75, 2)), C(G.n1('Julio de 2026 · Cumbre de Ankara'), 'v2_n312', D - round(D * 0.75, 2))], []),
    313: lambda n, D, V, T, narr: ([C(G.q1('«Socio terrible»', 'Donald Trump, sobre España en la OTAN', None, 'JULIO DE 2026 · CUMBRE DE ANKARA'), 'v2_q313', D)], []),
    319: lambda n, D, V, T, narr: ([C(G.t2('Denuncia ante EFE la «absoluta inferioridad» de los agentes frente al narco.', kick='FISCAL JEFE DE CÁDIZ'), 'v2_t319a', round(D * 0.5, 2)),
                                     C(G.t2('Interior había disuelto en 2022 la unidad especial contra el narcotráfico en el Campo de Gibraltar, el OCON-Sur.\nSegún la prensa', kick='OCON-SUR'), 'v2_t319b', D - round(D * 0.5, 2))], []),
    322: lambda n, D, V, T, narr: ([CL(F_('archivo/ar_dana_riada__02__FXxqigb-9xw.mp4'), 4.0, round(D * 0.5, 2)), C(G.d1('229 muertos', 'DANA de Valencia · 29/10/2024 · La Moncloa, 25/11/2024'), 'v2_d322', D - round(D * 0.5, 2))], []),
    326: lambda n, D, V, T, narr: ([CL(F_('archivo/ar_dana_coches__02__wVkAc0Hv-oU.mp4'), 30.0, round(D * 0.45, 2)), C(G.d1('2009', 'Se encarga el plan para encauzar el barranco del Poyo. No llegó a ejecutarse. · Valencia Plaza'), 'v2_d326', D - round(D * 0.45, 2))], []),
    346: lambda n, D, V, T, narr: ([C(G.t2('Funeral de Estado por las víctimas de Urda, presidido por los Reyes. El presidente no acude.', kick='10/11/2026 · CATEDRAL DE TOLEDO'), 'v2_t346', D)], []),
    358: lambda n, D, V, T, narr: ([C(G.s1_text(['2024\n×', '2025\n×', '2026\n×']), 'v2_s358', round(D * 0.55, 2)), C(G.t2('El Congreso tumbó en enero de 2025 y de 2026 dos decretos ómnibus, con la subida de las pensiones dentro.', kick='SIN PRESUPUESTOS: DECRETO LEY'), 'v2_t358', D - round(D * 0.55, 2))], []),
    361: lambda n, D, V, T, narr: ([C(G.d1('17.100 M€', 'Condonación de deuda de Cataluña pactada con Esquerra Republicana'), 'v2_d361', D)], []),
    363: lambda n, D, V, T, narr: ([P_img(capture_png(F_('capturas/doc_36c_BOE_disolucion_convocatoria_29N_06-10-2026.jpg'), 'v2_c363'), round(D * 0.68, 2), z=0.03),
                                    P_img(frame_at(F_('cortes_externos/38_abalos_mocion__(ext)s.mp4'), 8.0, 'v2_f363', crop=CROP), D - round(D * 0.68, 2), z=0.04)],
                                   [(png(G.pie('BOE · 06/10/2026'), 'v2_p363'), 0.4, round(D * 0.68, 2) - 0.1, True), ov_r1('José Luis Ábalos', 'Antiguo número tres del PSOE · condenado', 'v2_r363', round(D * 0.68, 2) + 0.2, D - 0.1)]),
    180: lambda n, D, V, T, narr: ([C(G.q1('«Rajoy y Aznar han tenido 15 ministros imputados o condenados. Yo he tenido la desgracia de tener uno.»', 'Pedro Sánchez · Salvados (laSexta) · 22/11/2026  —  Newtral (25/06/2026): de los ministros de Aznar, tres fueron condenados y otros investigados; no todos', q1bg(), 'SU CIFRA · NO CONTRASTADA'), 'v2_q180', D)], []),
    385: lambda n, D, V, T, narr: ([C(G.n1('¿Se aceptaría el resultado?'), 'v2_n385', D)], []),
    416: lambda n, D, V, T, narr: ([C(G.n1('22 de junio de 2026 · Tribunal Supremo'), 'v2_n416', D)], []),
    422: lambda n, D, V, T, narr: ([C(G.q1('«…de Pedro Sánchez Pérez-Castejón que se presentaba a dichas elecciones primarias»', 'Sentencia del Tribunal Supremo 418/2026 · p. 25', None, 'LA SENTENCIA · HECHOS PROBADOS'), 'v2_q422', D)], []),
    449: lambda n, D, V, T, narr: ([P_img(frame_at(SRC(447)[0], SRC(447)[1] + 1.0, 'v2_f449', dark=0.55), D, z=0.06)], []),
    450: lambda n, D, V, T, narr: ([P_img(frame_at(SRC(414)[0], SRC(414)[1] + 2.0, 'v2_f450', dark=0.55), D, z=0.06)], []),
}

def special(n, D, V, T, narr):
    """devuelve (pieces, ov) o None"""
    if n in OVR: return OVR[n](n, D, V, T, narr)
    if n in (3, 445):
        a = lastframe(F_('cortes/clip_39b_usted_no_lo_es.mp4')); b = lastframe(F_('cortes/clip_39c_feijoo_decente.mp4'))
        if n == 445: a, b = b, a
        return [P_img(split2(a, b, f's1_{n}'), D, z=0.02)], []
    if n == 69:
        a = frame_at(F_('cortes_externos/35_bildu_navarratv__(ext)s.mp4'), 0.5, 'fr69a'); b = frame_at(RES[54]['src'][0][0], 2.0, 'fr69b')
        return [P_img(split2(a, b, 's1_69'), D, z=0.02)], []
    if n == 233:
        a = frame_at(F_('cortes/clip_19c_derecho_no_responder.mp4'), 1.0, 'fr233a'); b = frame_at(F_('cortes_externos/04c_mitin_sevilla_elpais__(ext)s.mp4'), 5.0, 'fr233b')
        return [P_img(split2(a, b, 's1_233'), D, z=0.02)], []
    if n == 82: return [P_img(card(G.s1_text(['«NUEVO DELITO»\nNO', '«AMNISTÍA»\nSÍ']), 's1_82'), D, z=0)], []
    if n == 293: return [P_img(card(G.s1_text(['DEFENSA', 'INTERIOR', 'DELEGACIÓN']), 's1_293'), D, z=0)], []
    if n == 331: return [P_img(card(G.s1_text(['GOBIERNO', 'OPERADORES']), 's1_331'), D, z=0)], []
    if n == 20:
        return [P_img(card(G.t1(l, ''), f't1six_{i}'), d, z=0) for i, (l, d) in enumerate(zip(SIX, split_even(D, 6)))], []
    if n == 315:
        fr = [capture_png(F_('capturas/doc_26_ceuta_whatsapp_CNI_Moncloa_29-07-2026.jpg'), 'cni315'),
              frame_at(F_('cortes_rebajados/R4a_tiktok_playlist_LIMPIO.mp4'), 1.0, 'fr315b'),
              frame_at(F_('cortes_externos/25c2_eso_a_vivas__(ext)s.mp4'), 1.0, 'fr315c')]
        if ANKARA: fr.append(frame_at(ANKARA, 2.0, 'fr315d'))
        else: inc(n, 'no hay plano de Ankara en disco: tres congelados en lugar de cuatro')
        return [P_img(f, d, z=0.03) for f, d in zip(fr, split_even(D, len(fr)))], []
    if n == 349:
        fs = [F_(f'cortes/clip_04z_{i}.mp4') or F_(x) for i, x in enumerate(['cortes/clip_04z_1_caballe_2018.mp4', 'cortes/clip_04z_2_sassoli_2022.mp4', 'cortes/clip_04z_3_vara_2025.mp4', 'cortes/clip_04z_4_papa_2026.mp4'], 1)]
        fs = [F_(x) for x in ['cortes/clip_04z_1_caballe_2018.mp4', 'cortes/clip_04z_2_sassoli_2022.mp4', 'cortes/clip_04z_3_vara_2025.mp4', 'cortes/clip_04z_4_papa_2026.mp4']]
        fs = [f for f in fs if f]
        return [P_clip(f, 0.1, d, src_len=probe(f)['dur'] - 0.15, z=0.10) for f, d in zip(fs, split_even(D, len(fs)))], []
    if n == 429:
        a = capture_png(F_('capturas/doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg'), 'c429a', maxw=1.0); b = capture_png(F_('capturas/doc_03b_cerdan_auto_indicios_CGPJ_12-06-2025.jpg'), 'c429b', maxw=1.0)
        return [P_img(split2(a, b, 's1_429'), D, z=0.02)], []
    if n == 448:
        k = max(1, int(D // 1.0)); step = max(1, len(VOZFRAMES) // k); sel = VOZFRAMES[::step][:k]
        ds = split_even(D, len(sel))
        return [P_img(frame_at(p, t, f'rep_{nn}', crop=c), d, z=0) for (nn, p, t, c), d in zip(sel, ds)], []
    if n == 24:
        rf = refs_of(V)[0]
        return [P_img(card(G.l1(l1_items(V, narr)), 'l1_24'), D - 4, z=0), ref_piece(n, rf, 4)], []
    if n == 176:
        inc(n, 'clip_r6_feijoo_salazar_desconocido.mp4 está dañado (no decodifica, también en el PC): la fila va solo con el gráfico L1 de fechas')
        return [P_img(card(gfx('L1', V, '', narr, n), 'g176'), D, z=0.02)], []
    if n in (124, 201):
        rf = refs_of(V)[0]; code = 'R2' if n == 201 else 'L1'
        g = P_img(card(gfx(code, V, T if n == 201 else '', narr, n), f'g{n}'), D / 2, z=0)
        c = ref_piece(n, rf, D / 2)
        return ([g, c] if n == 124 else [c, g]), []
    if n == 32:
        return [P_img(card(G.q1('«Durante los viajes realizados, en la promoción de la candidatura…»', 'Sentencia TS 418/2026 · hechos probados · p. 25'), 'q1_32'), D, z=0.02)], []
    if n == 422:
        return [P_img(card(G.q1('«…de Pedro Sánchez Pérez-Castejón que se presentaba a dichas elecciones primarias»', 'Sentencia TS 418/2026 · p. 25'), 'q1_422'), D, z=0.02)], []
    if n == 347:
        t348 = clean([r for r in ROWS if r['#'] == '348'][0]['Texto en pantalla (+ # verificación)'])
        return [P_black(min(2.0, D / 3)), P_img(card(G.q1(t348, ''), 'q1_347'), D - min(2.0, D / 3), z=0)], []
    if n == 408:
        caps_ = [capture_png(F_(x), f'c408_{i}') for i, x in enumerate(['capturas/cap_v20_newtral_bulos_29n.png', 'capturas/cap_v21_verificat_rumores_fraude.png', 'capturas/cap_v45_maldita_bulos_29n.png'])]
        return [P_img(c, 1.5, z=0.03) for c in caps_] + [P_img(card(G.t2(T), 't2_408'), D - 4.5, z=0)], []
    if n == 409:
        m = re.match(r'\[([^\]]+)\]\s*(.*)', T); return [P_img(card(G.t1(m.group(1), m.group(2)) if m else G.t2(T), 't1_409'), D, z=0)], []
    if n == 381: return [P_img(card(G.q1(T, ''), 'q1_381'), D, z=0)], []
    if n == 334 or n == 337:
        place, sub = ('ADAMUZ', 'Córdoba · 46') if n == 334 else ('URDA', 'Toledo · 69')
        return [P_img(card(G.m1(place, sub), f'm1_{n}'), D, z=0.03)], []
    if n == 280:
        rs = refs_of(V); ds = split_even(D, 2)
        return [ref_piece(n, rs[0], ds[0]), ref_piece(n, rs[1], ds[1])], [(png(G.pie(T), f'pie{n}'), 0.4, ds[0] - 0.1, True)]
    return None

# ------------------------------------------------------------------ planificadores por tipo
def plan_visual(n, D, V, T, narr, tipo):
    sp = special(n, D, V, T, narr)
    if sp: return sp
    codes = CODE_RE.findall(V)
    rs = [r for r in refs_of(V)]
    ov = []
    blur = 12 if n == 282 else 0
    lead = V.split(' ')[0]
    if tipo == 'cartel' or tipo == 'rótulo' or tipo == 'cita en pantalla':
        if not rs:
            m = re.match(r'\[([^\]]+)\]\s*(.*)', T)
            if lead == 'T1' or (m and lead != 'T2' and lead != 'Q1'): img = G.t1(m.group(1), m.group(2)) if m else G.t2(T)
            elif lead == 'T2': img = G.t2(T)
            elif lead == 'Q1': img = G.q1(T, '', q1bg() if tipo == 'cartel' else None)
            elif lead == 'X1':
                ps = [p.strip() for p in T.split(' · ')]; num = re.sub(r'\D', '', ps[0]); img = G.x1(num, ps[1] if len(ps) > 1 else '', ' · '.join(ps[2:]))
            elif lead == 'X0': img = G.x0(T)
            elif lead == 'K1':
                m2 = re.match(r'PERDÓN N\.º (\d+) · (.*)', T); img = G.k1(int(m2.group(1)), m2.group(2)) if m2 else G.t2(T)
            elif lead == 'Z1': img = G.z1(T)
            elif lead == 'P1': img = G.p1(T)
            else: img = G.t2(T); inc(n, f'cartel sin plantilla reconocible («{V[:40]}»): se usa T2')
            return [P_img(card(img, f'c{n}'), D, z=0)], []
        # cartel con capturas
        m = re.match(r'\[([^\]]+)\]\s*(.*)', T)
        if m or len(T) > 90:
            dc = round(D * 0.45, 2)
            pcs = [ref_piece(n, r, d) for r, d in zip(rs, split_even(dc, len(rs)))]
            img = G.t1(m.group(1), m.group(2)) if m else G.t2(T)
            return pcs + [P_img(card(img, f'c{n}'), D - dc, z=0)], []
        pcs = [ref_piece(n, r, d) for r, d in zip(rs, split_even(D, len(rs)))]
        if T: ov.append((png(G.pie(T), f'pie{n}'), 0.3, D - 0.1, True))
        return pcs, ov
    # locución / recurso visual
    graphic = None
    main_codes = [c for c in codes if c not in ('C1',)]
    if not rs and main_codes:
        graphic = gfx(main_codes[0], V, T, narr, n)
        dark = 'oscurece' in V or 'se apagan' in V
        pcs = [P_img(card(graphic, f'g{n}'), D, z=0.02, fade_dark=dark)]
        if T and main_codes[0] in ('D1', 'Q1', 'L1') and clean(T) and not quotes(T) and main_codes[0] != 'Q1':
            ov.append((png(G.pie(T), f'pie{n}'), 0.4, D - 0.1, True))
        return pcs, ov
    if not rs:
        if tipo == 'recurso visual' and RES.get(n, {}).get('src'):
            s = RES[n]['src'][0]; pcs = [P_clip(s[0], s[1] or 0, D, src_len=(s[2] - s[1]) if s[2] else D)]
        elif n == 232:
            pcs = [P_clip(F_('cortes_externos/04c_mitin_sevilla_elpais__(ext)s.mp4'), 5.0, D)]
        else:
            inc(n, f'visual sin recurso localizable («{V[:60]}»): negro provisional'); pcs = [P_black(D)]
        if T: ov.append((png(r1_from(T) if caps(T.split(' · ')[0]) else G.pie(T), f'pie{n}'), 0.4, D - 0.1, True))
        return pcs, ov
    ds = split_even(D, len(rs))
    pcs = [ref_piece(n, r, d, blur=blur) for r, d in zip(rs, ds)]
    pcs = [p for p in pcs if p] or [P_black(D)]
    if len(pcs) < len(rs): pcs = [dict(p, dur=round(D / len(pcs), 3)) for p in pcs]
    m = re.search(r'\+ D1 «([^»]+)»', V)
    if m: ov.append((png(d1ov(m.group(1)), f'd1o{n}'), 0.5, D - 0.2, True))
    if T:
        t = clean(T)
        if t:
            img = r1_from(t) if caps(t.split(' · ')[0]) and 'C1' not in codes else G.pie(t)
            ov.append((png(img, f'pie{n}'), 0.4, D - 0.1, True))
    return pcs, ov

TOFIX = {303: 12.35, 15: 12.4}
NOEXT = {142, 161, 196, 197, 402, 185, 186, 248, 13, 14}
FULL = {88, 91}
def fin_w(w): return w.strip().endswith(('.', '?', '!', '…', '»', '"'))
def extend_sentence(n, k, ss, to, full_start=False):
    Wd = stt_words(n, k)
    if not Wd: return ss, to, None
    W2 = sorted(Wd); how = None
    inside = [i for i, x in enumerate(W2) if x[0] >= ss - 0.1 and x[1] <= to + 0.06]
    if not inside: return ss, to, None
    j = inside[-1]
    if not fin_w(W2[j][2]):
        jj = j
        while jj + 1 < len(W2) and W2[jj + 1][0] - W2[jj][1] < 0.9 and W2[jj + 1][1] - W2[j][1] < 4.0:
            jj += 1
            if fin_w(W2[jj][2]): break
        if jj > j and fin_w(W2[jj][2]):
            end = W2[jj][1] + 0.3
            if jj + 1 < len(W2): end = min(end, max(W2[jj][1] + 0.06, W2[jj + 1][0] - 0.04))
            to = round(end, 2); how = 'salida al final de la frase'
    if full_start:
        i = inside[0]; ii = i
        while ii - 1 >= 0 and not fin_w(W2[ii - 1][2]) and W2[ii][0] - W2[ii - 1][1] < 0.9 and ss - W2[ii - 1][0] < 4.0: ii -= 1
        if ii < i: ss = round(max(0, W2[ii][0] - 0.08), 2); how = (how + '; ' if how else '') + 'entrada al inicio de la frase'
    return ss, to, how
TFIX = {268: '[VERSIÓN DE OTRO INVESTIGADO] El expresidente de Plus Ultra, Julio Martínez, también investigado, sostiene que el 1 % del rescate era para Zapatero.',
        119: 'Pedro Sánchez no está imputado en ninguna de las causas de este expediente. Todas las personas investigadas tienen derecho a la presunción de inocencia.'}
def plan_row(r):
    n = int(r['#']); tipo = r['Tipo']; V = r['Visual en pantalla (archivo de recurso)']; T = clean(TFIX.get(n, r['Texto en pantalla (+ # verificación)']))
    T = re.sub(r'\s*\[AVI[^\]]*\]', '', T)
    note = r['Nota para el montador']; lit = r['Contenido literal (voz o texto)']
    dE = float(r['Duración'].replace(',', '.')) if r['Duración'] not in ('—', '') else 0
    seg = dict(n=n, tipo=tipo, ov=[], audio=[], pieces=[], kind=tipo, src=[], edl_dur=dE)
    if tipo == 'intro':
        p = '/home/claude/fabrica-documentales/assets/intro/docuvox.mp4'; D = round(probe(p)['dur'] * FPS) / FPS
        seg.update(D=D, pieces=[P_clip(p, 0, D, src_len=D)], audio=[dict(t='clip_raw', path=p)])
        seg['audio'] = [dict(t='clip', path=p, ss=0, dur=D)]
        seg['src'] = [(p, 0, D)]; return seg
    if 'ocución' in tipo or 'OCUCIÓN' in tipo:
        wav = f'{AQ}/nar/n{n:03d}.wav' if n != 33 or not os.path.exists(f'{AQ}/nar/n033_v2.wav') else f'{AQ}/nar/n033_v2.wav'
        D = round((probe(wav)['dur'] + 0.32) * FPS) / FPS
        seg.update(D=D, audio=[dict(t='wav', path=wav, at=0)])
        seg['pieces'], seg['ov'] = plan_visual(n, D, V, T, lit, tipo)
        seg['pieces'] = [p for p in seg['pieces'] if p]
        tot = sum(p['dur'] for p in seg['pieces'])
        if abs(tot - D) > 0.02: seg['pieces'][-1]['dur'] = round(seg['pieces'][-1]['dur'] + D - tot, 3)
        seg['nar'] = 'Top' if 'Top' in tipo else 'New'
        if n == 33: seg['audio'] = [dict(t='wav', path=f'{AQ}/nar/n033_v2.wav', at=0)]
        band_broll(seg)
        if n == 208: seg['ov'].append((png(G.pie('IMÁGENES: OKDIARIO · AGOSTO DE 2026'), 'v2_p208'), 0.3, D - 0.1, True))
        return seg
    if tipo == 'voz' and n == 152:
        D = round(max(dE, 4.5) * FPS) / FPS
        seg.update(D=D, pieces=[P_img(card(G.q1(lit, clean(r['Texto en pantalla (+ # verificación)']), q1bg()), 'q152'), D, z=0)], kind='Q1 (corte erróneo)')
        inc(n, 'clip_16_me_equivoque.mp4 no contiene la frase del EDL (dice «…nuestro proyecto. Soy muy consciente de ello…»): tarjeta Q1 con el literal y su fuente hasta localizar el tramo bueno del 09/07/2025')
        return seg
    if tipo == 'voz' and n in (149, 165, 393):
        D = round(max(min(dE, 3.0 + len(lit.split()) / 2.7), 4.0) * FPS) / FPS
        q = re.sub(r'\s*\(literal:.*?\)', '', lit).strip()
        seg.update(D=D, pieces=[P_img(card(G.q1(q, clean(r['Texto en pantalla (+ # verificación)']), q1bg()), f'rojo{n}'), D, z=0)], kind='Q1 (🔴)')
        inc(n, 'origen 🔴 (agencia con licencia): se sustituye el corte por tarjeta Q1 con el literal y su fuente, sin el audio de agencia')
        return seg
    if tipo == 'voz':
        src = [list(x) for x in (RES[n].get('src') or [])]
        if n == 91:
            inc(n, 'se retira el audio añadido en la segunda pasada (era de laSexta 2022, no de esta entrevista): queda el intercambio real con Alsina en Onda Cero, completo')
        if not src: inc(n, 'corte sin fuente resuelta'); seg.update(D=dE, pieces=[P_black(dE)]); return seg
        wave = bool(re.search(r'[Oo]nda', V)) or n == 248; t0 = 0.0
        if n == 248: inc(n, 'el clip alternativo de RNE es audio sobre negro: se monta con forma de onda y subtítulo')
        for k, (p, ss, to, lab) in enumerate(src):
            pr = probe(p)
            if ss is None or (abs((to - ss) - dE) > max(1.5, 0.25 * dE) and len(src) == 1):
                fw = full_words(p)
                al = align(fw, lit, (ss or 0) - 6 if ss is not None else 0, (to + 6) if to else 1e9) if fw else None
                if al:
                    TCLOG.append((n, os.path.basename(p), ss, to, round(al[0] - 0.08, 2), round(al[1], 2), 'localizado por la frase (STT)', False))
                    ss, to = max(0, al[0] - 0.08), al[1]
                elif ss is None: inc(n, 'no se pudo localizar la frase por STT: se usa el clip completo')
            if ss is None:
                ss, to = 0.0, pr['dur']
                if 'finales' in note and pr['dur'] > dE + 0.8: ss = max(0, pr['dur'] - dE - 0.3)
                Wd = stt_words(n, k)
                m = re.search(r'Entrar justo en «([^»]+)»', note)
                if m and Wd:
                    hit = [x for x in Wd if wt.nz(x[2]) == wt.nz(m.group(1))]
                    if hit: ss = max(0, hit[0][0] - 0.06)
            parts = [x for x in re.split(r'\b[A-ZÁÉÍÓÚÑ]{3,}:', lit) if x.strip()]
            litk = lit if len(src) == 1 else (parts[k] if len(parts) == len(src) else '')
            ss2, to2, how = snap(n, k, p, ss, to, note, litk)
            if (abs(ss2 - ss) > 0.02 or abs(to2 - to) > 0.02):
                TCLOG.append((n, os.path.basename(p), ss, to, ss2, to2, how, 'ajustar a oído' in note))
            elif 'ajustar a oído' in note: TCLOG.append((n, os.path.basename(p), ss, to, ss2, to2, how + ' · sin cambio necesario', True))
            ss, to = ss2, to2
            if n not in NOEXT:
                ss3, to3, how3 = extend_sentence(n, k, ss, to, n in FULL)
                if how3:
                    TCLOG.append((n, os.path.basename(p), ss, to, ss3, to3, how3, False)); ss, to = ss3, to3
            if n in TOFIX: TCLOG.append((n, os.path.basename(p), ss, to, ss, TOFIX[n], 'salida alargada para que se oiga entera la última palabra', False)); to = TOFIX[n]
            if n == 142 and to - ss > 14.0: to = ss + 14.0; TCLOG.append((n, os.path.basename(p), ss, to, ss, to, 'tope legal 14 s', False))
            d = round((to - ss) * FPS) / FPS
            fx = fx_for(p, ss); crop = fx['crop'] if fx else None; covers = []
            if fx and fx.get('letterbox'): covers = LETTERBOX
            if fx and fx.get('covers'): covers = covers + [tuple(c) for c in fx['covers']]
            if re.search(r'tapar (el )?faldón', note) and not crop: crop = 'iw*0.76:ih*0.76:iw*0.12:ih*0.10'; inc(n, 'faldón tapado con reencuadre (zoom 130 %, se recorta la franja inferior)')
            elif not crop and not covers and '🟡' in note and not re.search(r'sin faldón|sin faldones', note + r['Archivo']): crop = 'iw*0.76:ih*0.76:iw*0.12:ih*0.10'
            if n == 288: crop = 'iw*0.50:ih*0.50:iw*0.19:ih*0.02'; inc(n, 'rótulo de El País en la imagen: reencuadre cerrado sobre el rostro'); covers = list(covers) + [(0, 880, W, H)]
            elif n in BAND:
                covers = list(covers) + [(0, 600 if n == 137 else 790, W, H)]
                if k == 0: inc(n, 'faldón de otro medio en la imagen: franja negra inferior (27 %)')
            blur = 16 if n in (185, 186) else 0
            if wave or n == 402 or lab == 'AUDIO': seg['pieces'].append(P_wave(p, ss, d))
            else:
                seg['pieces'].append(P_clip(p, ss, d, src_len=d, crop=crop, blur=blur))
                VOZFRAMES.append((n, p, ss + d * 0.5, crop))
                LASTV['p'] = (p, max(ss, to - 0.4), crop)
            beeps = []
            if n == 142:
                for a_, b_, w_ in (stt_words(n, k) or []):
                    if re.search(r'ariana', wt.nz(w_)) and ss <= a_ <= to: beeps.append((round(a_ - ss - 0.08, 2), round(b_ - ss + 0.08, 2)))
                if beeps: inc(n, f'nombre de mujer audible sin pitido en la fuente («Ariana», {", ".join(f"{x:.1f}-{y:.1f} s" for x, y in beeps)} del corte): se añade pitido. «La colombiana» se mantiene (nacionalidad, no profesión, ciudad ni fecha): revisar con criterio legal')
            seg['audio'].append(dict(t='clip', path=p, ss=ss, dur=d, at=t0, distort=(n == 402), beeps=beeps, wave=bool(wave or lab == 'AUDIO' or n == 402)))
            for c in covers: seg['ov'].append((png(G.cover(c), f'cv{n}_{k}_{c[1]}'), t0, t0 + d, False))
            if wave or lab == 'AUDIO' or n == 402:
                for i, (a, b, txt) in enumerate(subs_for(n, k, ss, to, t0)):
                    if n == 142: txt = re.sub(r'(?i)¿?ariana\??', '[pitido]', txt)
                    seg['ov'].append((png(G.subt(txt), f'sb{n}_{k}_{i}'), a, b, False))
            seg['src'].append((p, ss, to)); t0 += d
        D = round(t0, 3); seg['D'] = D
        rc = rotulo_corte(n, r['Texto en pantalla (+ # verificación)'], note)
        if rc:
            tag, name, line2 = rc
            seg['ov'].append((png(G.r1(name, line2, tag), f'r1_{n}'), 0.3 if D > 2 else 0.05, min(D - 0.15, 10.0), True))
            seg['tag'] = tag
        m = re.search(r'\+ cartel: «([^»]+)»', lit)
        if m: seg['ov'].append((png(G.nota(m.group(1)), f'cart{n}'), 0.6, D - 0.2, True))
        if wave and n not in (142,):
            pass
        return seg
    # cartel, silencio, recurso visual, rótulo, cita
    if tipo in ('cartel', 'rótulo', 'cita en pantalla'):
        nw = len(re.findall(r'\w+', T)); need = 1.0 + nw / 3.4
        if need > dE + 0.3: inc(n, f'tarjeta alargada para poder leerla: {dE:.1f} → {min(dE + 2.0, need):.1f} s'); dE = min(dE + 2.0, need)
    D = round(dE * FPS) / FPS
    seg['D'] = D
    if tipo == 'silencio': seg['pieces'] = [P_black(D)]; return seg
    seg['pieces'], seg['ov'] = plan_visual(n, D, V, T, lit, tipo)
    seg['pieces'] = [p for p in seg['pieces'] if p]
    tot = sum(p['dur'] for p in seg['pieces'])
    if abs(tot - D) > 0.02: seg['pieces'][-1]['dur'] = round(seg['pieces'][-1]['dur'] + D - tot, 3)
    band_broll(seg)
    return seg

def band_broll(seg):
    if seg['n'] not in BAND_BROLL or seg['n'] in OVR: return
    t = 0.0
    for p in seg['pieces']:
        if p['t'] == 'clip': seg['ov'].insert(0, (png(G.cover((0, 790, W, H)), 'band'), t, t + p['dur'], False))
        t += p['dur']

BAND = {10, 106, 109, 137, 141, 171, 172, 179, 205, 227, 229, 265, 288, 304, 305, 320, 357, 365, 372, 389, 394, 406, 410, 428}
BAND_BROLL = {39, 42, 74, 78, 125, 218, 271}
PAUSE = {3: 0.8, 101: 1.0, 108: 1.0, 130: 1.0, 283: 2.0, 286: 1.5, 292: 1.5, 322: 2.0, 334: 2.0, 337: 2.0}
def add_pause(seg):
    n = seg['n']
    if n in PAUSE:
        p = PAUSE[n]; seg['pieces'][-1]['dur'] = round(seg['pieces'][-1]['dur'] + p, 3); seg['D'] = round(seg['D'] + p, 3); seg['pause'] = p
        for i, o in enumerate(seg['ov']):
            if o[3] and abs(o[2] - (seg['D'] - p - 0.1)) < 0.5: seg['ov'][i] = (o[0], o[1], seg['D'] - 0.1, o[3])
    if n == 277:
        seg['pieces'][0]['dur'] = round(seg['pieces'][0]['dur'] + 3.0, 3); seg['D'] = round(seg['D'] + 3.0, 3); seg['pause'] = 3.0
        for a in seg['audio']:
            if a['t'] == 'wav': a['path'] = a['path'].replace('n277.wav', 'n277_pad.wav')
            else: a['at'] = a.get('at', 0) + 3.0
    return seg
DISCLAIMER = ('Documental crítico de DocuVox.\n\nLas declaraciones son de archivo, con su medio y su fecha. Pedro Sánchez no ha participado en este documental. '
              'Las personas investigadas sin sentencia firme gozan de la presunción de inocencia.')
def opening():
    return [dict(n=1000, tipo='apertura', ov=[], audio=[], src=[], edl_dur=4.0, D=4.0, kind='apertura',
                 pieces=[P_black(0.6), P_img(card(G.presenta(), 'v2_presenta'), 3.4, z=0.0, fade_dark=True)]),
            dict(n=1001, tipo='apertura', ov=[], audio=[], src=[], edl_dur=8.0, D=8.0, kind='aviso',
                 pieces=[P_img(card(G.disclaimer(DISCLAIMER), 'v2_disclaimer'), 8.0, z=0.0, fade_dark=True)])]
def fuentes_credits():
    import collections
    txt = open(B + 'FUENTES_COMPLETAS.md', encoding='utf-8').read()
    meds = re.findall(r'^### (.+?) \((\d+)\)', txt, re.M)
    names = [m for m, c in meds]
    pages = [names[i:i + 26] for i in range(0, len(names), 26)]
    return pages
def credits_seg():
    pages = fuentes_credits(); pcs = []
    pcs.append(C(G.t2('Fuentes, medios y fechas de cada declaración y documento: en pantalla en cada corte y, enlace por enlace, en la descripción. Rectificaciones de los aludidos: en el plazo legal de tres días.', kick='DOCUVOX'), 'v2_cr0', 6.0))
    for i, pg in enumerate(pages): pcs.append(C(G.credits(pg, 'FUENTES Y MEDIOS CONSULTADOS' + (f' · {i + 1}/{len(pages)}' if len(pages) > 1 else '')), f'v2_cr{i + 1}', 5.0))
    pcs.append(C(G.credits(['Música: Mixkit (Mixkit Stock Music Free License)', 'Mapas: Natural Earth (dominio público)', 'Un documental de DocuVox'], 'CRÉDITOS'), 'v2_crm', 5.0, dark=True))
    D = round(sum(p['dur'] for p in pcs), 2)
    return dict(n=455, tipo='cartel', ov=[], audio=[], src=[], edl_dur=D, D=D, kind='créditos', pieces=pcs)
HIZODIJO_PAUSE = 0.7
REMOVE = {95, 166, 175, 219, 220, 257, 410}
def plan_all():
    segs = opening()
    order = [r for r in ROWS]
    i35 = next(i for i, r in enumerate(order) if r['#'] == '35'); i37 = next(i for i, r in enumerate(order) if r['#'] == '37')
    r37 = order.pop(i37); order.insert(i35, r37)
    order = [r for r in order if int(r['#']) not in REMOVE]
    for r in order:
        try:
            s = plan_row(r) if r['#'] != '455' else credits_seg()
            s = add_pause(s)
            if s.get('tag') in ('HIZO', 'DIJO') and not s.get('pause'):
                s['pieces'][-1]['dur'] = round(s['pieces'][-1]['dur'] + HIZODIJO_PAUSE, 3); s['D'] = round(s['D'] + HIZODIJO_PAUSE, 3); s['pause'] = HIZODIJO_PAUSE
            segs.append(s)
        except Exception as e:
            import traceback; traceback.print_exc(); inc(int(r['#']), f'ERROR de plan: {e}'); raise
    return segs

if __name__ == '__main__':
    S = plan_all()
    json.dump(S, open(AQ + '/plan.json', 'w'), ensure_ascii=False, indent=0, default=str)
    json.dump(dict(inc=INC, tc=TCLOG), open(AQ + '/plan_log.json', 'w'), ensure_ascii=False, indent=0)
    print(len(S), 'segmentos', round(sum(s['D'] for s in S), 1), 's')
    for n, m in INC: print('INC', n, m)
