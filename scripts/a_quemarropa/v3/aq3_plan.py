"""Plan de segmentos: cada fila del EDL -> dict(n, D, pieces, ov, audio, kind, src_tc...)."""
from aq3_build import *

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
    57: lambda: G.t2('El PSOE y Unidas Podemos firman por escrito con EH Bildu derogar la reforma laboral del PP a cambio de su abstención.', kick='HIZO · 20/05/2020'),
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


# ======================================================================================================
# V3 · MONTAJE FINAL (encargo «PROMPT_MONTAJE_FINAL_v3», 25/11/2026). No se toca narrativa, locución ni orden.
# ======================================================================================================
E3 = {int(r['#']): r for r in ROWS if str(r['#']).isdigit()}
C110 = 'iw*0.91:ih*0.91:iw*0.045:ih*0.045'          # recorte máximo 110 %
C110TR = 'iw*0.91:ih*0.91:0:ih*0.09'                 # deja fuera la mosca de arriba a la derecha
C110TL = 'iw*0.91:ih*0.91:iw*0.09:ih*0.09'           # deja fuera la mosca de arriba a la izquierda
ZB = [0, int(H * 0.74), W, H]                        # faldón inferior (desenfoque localizado)
ZCORN = [[0, 0, int(W * 0.17), int(H * 0.16)], [int(W * 0.83), 0, W, int(H * 0.16)]]
REMOVE3 = set(REMOVE) | {8, 152, 402, 404, 344}
LOG3 = []      # (n, id, problema, acción, estado)
def log3(n, iid, prob, acc, est='corregido'): LOG3.append((n, iid, prob, acc, est))
CUR = {'bottom': 980}
_r1, _nota = G.r1, G.nota
def _r1w(*a, **k):
    k.setdefault('bottom', CUR['bottom']); return _r1(*a, **k)
def _notaw(text, bottom=None): return _nota(text, bottom or CUR['bottom'])
G.r1 = _r1w; G.nota = _notaw
# filas cuyo corte trae subtítulos/rótulos quemados abajo que se quedan visibles: el rótulo A sube 24 px por encima
SUBBOT = {59: 800, 285: 980, 286: 980, 13: 980, 18: 980}
WAVEROWS = {76, 79, 81, 91, 142, 161, 196, 197, 243, 248, 391, 406, 10, 229, 222, 186, 146, 44, 300}
for _n in WAVEROWS: SUBBOT[_n] = 800

def ovname(o): return os.path.basename(o[0])
def is_rot(b): return b.startswith(('r1_', 'pie', 'v2_r', 'v2_p', 'cart', 'd1o', 'v2_o', 'r3_'))
def drop_rot(seg): seg['ov'] = [o for o in seg['ov'] if not is_rot(ovname(o))]
def add_r1(seg, name, line2='', tag=None, a=0.3, key=None, bottom=None):
    CUR['bottom'] = bottom or SUBBOT.get(seg['n'], 980)
    D = seg['D']; need = G.r1_need(name, line2, tag)
    b = min(D - 0.08, max(a + need, min(D - 0.08, a + 5.0)))
    seg['ov'].append((png(G.r1(name, line2, tag), key or f'r3_{seg["n"]}'), a, b, 'A'))
    CUR['bottom'] = 980
def add_nota(seg, text, a, b, key):
    seg['ov'].append((png(G.nota(text), key), a, b, 'A'))
def own_bg(p, t, key, crop=None): return frame_at(p, t, 'wbg_' + key, sat=0.85, dark=0.32, blur=40, crop=crop)
def to_wave(seg, bg=None):
    """corte → forma de onda + subtítulo (Inter 40, caja 65 %, 82 % de la altura) sobre fondo del hablante desenfocado"""
    n = seg['n']; t0 = 0.0; pcs = []
    seg['ov'] = [o for o in seg['ov'] if not ovname(o).startswith(('cv', 'band', 'sb'))]
    for k, (p, ss, to) in enumerate(seg['src']):
        d = round((to - ss) * FPS) / FPS
        w = P_wave(p, ss, d); w['bgimg'] = bg or own_bg(p, ss + d / 2, f'{n}_{k}'); pcs.append(w)
        for i, (a, b, txt) in enumerate(subs_for(n, k, ss, to, t0)):
            if n == 142: txt = re.sub(r'(?i)¿?ariana\??|la colombiana', '[pitido]', txt)
            seg['ov'].append((png(G.subt(txt), f'sb3_{n}_{k}_{i}'), a, b, False))
        for a_ in seg['audio']:
            if a_.get('t') == 'clip' and a_['path'] == p: a_['wave'] = True
        t0 += d
    tot = sum(x['dur'] for x in pcs)
    if abs(tot - seg['D']) > 0.02: pcs[-1]['dur'] = round(pcs[-1]['dur'] + seg['D'] - tot, 3)
    seg['pieces'] = pcs
def set_audio_tc(seg, k, ss=None, to=None, fade=None):
    """recorte del corte k (audio e imagen a la vez); devuelve la variación de duración"""
    p, ss0, to0 = seg['src'][k]; ss = ss0 if ss is None else ss; to = to0 if to is None else to
    d0 = round((to0 - ss0) * FPS) / FPS; d = round((to - ss) * FPS) / FPS
    seg['src'][k] = (p, ss, to)
    ai = [a for a in seg['audio'] if a.get('t') == 'clip'][k]
    ai['ss'] = ss; ai['dur'] = d
    if fade: ai['fade_out'] = fade
    vi = [x for x in seg['pieces'] if x['t'] in ('clip', 'wave')][k]
    vi['ss'] = ss; vi['dur'] = round(vi['dur'] + d - d0, 3); vi['len'] = d
    # los audios siguientes se desplazan
    sh_ = d - d0; after = False
    for a in seg['audio']:
        if a is ai: after = True; continue
        if after and a.get('t') == 'clip': a['at'] = round(a.get('at', 0) + sh_, 3)
    seg['ov'] = [(o[0], o[1], o[2] if o[2] < seg['D'] - 0.2 else o[2] + sh_, o[3]) for o in seg['ov']]
    seg['D'] = round(seg['D'] + sh_, 3)
    TCLOG.append((seg['n'], os.path.basename(p), ss0, to0, ss, to, 'v3: ' + ('entrada' if ss != ss0 else 'salida') + ' corregida', False))
    return sh_
def card3(img, key, D, kind='card'):
    p = P_img(card(img, 'v3_' + key), D, z=0); p['v3'] = kind; return p
def SANCHEZ_BG(key): return own_bg(F_('cortes_externos/00a3_mocion_cuartopoder__(ext)s.mp4'), 36.0, key)

# ------------------------------------------------------------------ correcciones fila a fila
def fx_7(seg):    # L-08: la ráfaga pasa de 7 a 9 con corte limpio
    for a in seg['audio']: a['fade_out'] = 0.01
def fx_10(seg):   # L-16: declaración judicial con la mosca de OKDiario → forma de onda
    to_wave(seg, SANCHEZ_BG('s10')); drop_rot(seg)
    add_r1(seg, 'Pedro Sánchez ante el juez', 'Grabación difundida por OKDiario · 24/09/2024')
    log3(10, 'L-16', 'Mosca grande de OKDiario en la grabación judicial', 'Forma de onda con subtítulo y rótulo «Grabación difundida por OKDiario»')
def fx_11(seg):   # T-04
    drop_rot(seg); add_r1(seg, 'David Sánchez', 'Badajoz · 09/01/2025', 'CONDENA NO FIRME')
    log3(11, 'T-04', 'Rótulo de David Sánchez', 'Rótulo «DAVID SÁNCHEZ · CONDENA NO FIRME»')
TOBJ = [[int(W * 0.06), int(H * 0.38), int(W * 0.94), int(H * 0.64)], [0, int(H * 0.84), W, H]]
def _tobj(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['crop'] = 'iw*0.91:ih*0.91:iw*0.045:0'; p['ozones'] = [list(z) for z in TOBJ]; p['zsig'] = 24
def fx_25(seg):
    _tobj(seg)
    log3(25, 'L-16', 'Marca de agua grande de The Objective y franja amarilla con su web (Comité Federal 2016)', 'No hay plano limpio del acto y la marca está en el centro: recorte al 110 % que saca la franja y desenfoque localizado de la marca y de los subtítulos de origen', 'parcial')
def fx_26(seg):
    _tobj(seg); drop_rot(seg); add_r1(seg, 'Pedro Sánchez', 'Comité Federal del PSOE · 01/10/2016 · Imágenes: The Objective', bottom=980)
def fx_27(seg):
    _tobj(seg); drop_rot(seg); add_r1(seg, 'Pedro Sánchez', 'Ferraz · 01/10/2016 · Imágenes: The Objective', bottom=980)
def fx_29(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p.setdefault('ozones', []).extend([[0, 0, int(W * 0.62), int(H * 0.11)], [int(W * 0.80), 0, W, int(H * 0.15)]])
    log3(seg['n'], 'D-04', 'Título quemado de otro medio cortado arriba', 'Desenfoque localizado (fuera del todo)')
fx_31 = fx_29
def fx_39(seg):   # D-01 + plano que corría 10,6 s sin audio
    D = seg['D']; d1 = round(D * 0.45, 2); d2 = round(D * 0.30, 2); d3 = round(D - d1 - d2, 3)
    p1 = F_('cortes_externos/00a3_mocion_cuartopoder__(ext)s.mp4')
    seg['pieces'] = [P_clip(p1, 175.0, d1, crop=C110TR), P_clip(p1, 30.0, d2, crop=C110TR), P_clip(F_('cortes_externos/38b_abalos_decencia__(ext)s.mp4'), 8.0, d3, crop=C110TR)]
    seg['ov'] = []
    add_nota(seg, 'Caso Gürtel: sentencia\n24 de mayo de 2018', 0.3, min(d1 - 0.1, 6.0), 'v3_n39')
    log3(39, 'D-01', '«24/05/2018 · SENTENCIA GÜRTEL» en amarillo sobre franja negra', 'Rótulo del estilo único en dos líneas; fuera la franja')
    log3(39, 'QC', 'Plano de la moción corría 10,6 s sin audio', 'Tres planos del mismo material: Rajoy en el escaño, Sánchez en la tribuna, Ábalos')
def fx_44(seg):   # L-12
    to_wave(seg); drop_rot(seg); add_r1(seg, 'Pedro Sánchez', 'La Moncloa · 17/09/2018')
    log3(44, 'L-12', 'Vídeo de Europa Press con marca de agua', 'No hay vídeo de La Moncloa del acto en disco: forma de onda con subtítulo y rótulo «La Moncloa · 17/09/2018»')
def fx_48(seg):   # V-07
    seg['pieces'] = [P_clip(F_('cortes_externos/38b_abalos_decencia__(ext)s.mp4'), 8.0, seg['D'], crop=C110TR)]
    log3(48, 'V-07', 'Plano de Báñez y Méndez de Vigo', 'Ábalos en la tribuna (31/05/2018, señal del Congreso), sin la mosca')
def fx_52(seg): set_audio_tc(seg, 0, ss=3.28); log3(52, 'S-04', 'Se colaba la cola de la pregunta anterior', 'Entrada en «yo sería…» con fundido de 10 ms')
def fx_67(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['vcut'] = 0.45
    log3(67, 'V-01', 'Miniatura «EL IN…» y logo de LDTV al final', 'Fuera: se mantiene el último fotograma limpio')
def fx_73(seg):   # D-05
    seg['pieces'] = [card3(G.d1('PP 137 · PSOE 121', 'Elecciones generales · 23/07/2023'), 'd73', seg['D'])]
    log3(73, 'D-05', '«137 PP / 121 PSOE» partido en dos líneas', '«PP 137 · PSOE 121» en una línea a 64-72 px con contexto debajo')
def fx_74(seg):   # T-06
    seg['ov'] = [o for o in seg['ov'] if not is_rot(ovname(o))]
    add_r1(seg, 'Carles Puigdemont', 'Hoy amnistiado (TS, 20/11/2026)', a=0.6)
    log3(74, 'T-06', 'Puigdemont sin situación actual', 'Rótulo «Puigdemont · hoy amnistiado (TS, 20/11/2026)»')
def fx_79(seg):   # D-06
    set_audio_tc(seg, 0, to=6.22, fade=0.08); log3(79, 'D-06', 'Corte contradictorio y repetición (11:00:16–11:07:08)', 'Salida tras «…es acorde con la Constitución»; ahorro ≈6 s')
def fx_81(seg): set_audio_tc(seg, 0, to=19.10, fade=0.10); log3(81, 'S-01', 'Acababa en «tenemos que ser…»', 'Salida en la pausa tras «…Cataluña.» con fundido de 100 ms')
def fx_91(seg): set_audio_tc(seg, 0, to=19.12, fade=0.12); log3(91, 'QC', 'Ruido al final de la fila 91', 'Salida tras «larga.» con fundido de 120 ms')
def fx_94(seg): set_audio_tc(seg, 0, to=192.10, fade=0.12); log3(94, 'S-01', 'Acababa en «y que la…»', 'Salida en la pausa tras «…sociedad catalana» con fundido de 120 ms')
def fx_106(seg): set_audio_tc(seg, 0, ss=0.38); log3(106, 'S-04', 'Se comía la primera sílaba', 'Entrada en «garantizar» con fundido de 10 ms')
def fx_109(seg):
    set_audio_tc(seg, 0, fade=0.12)
    log3(109, 'S-03', '«…por parte de los…» acaba a mitad', 'El archivo de origen termina ahí (3,6 s); no hay más frase en disco: fundido de 120 ms', 'pendiente')
def fx_115(seg):
    set_audio_tc(seg, 0, ss=7.99)
    for p in seg['pieces']:
        if p['t'] == 'clip': p['vcut'] = 0.75
    log3(115, 'S-04', 'Se comía la primera sílaba', 'Entrada en «perdón» con fundido de 10 ms')
    log3(115, 'V-02', 'Cortinilla blanca en diagonal al final', 'Fuera')
def fx_142(seg):  # L-07
    a = [x for x in seg['audio'] if x.get('t') == 'clip'][0]; ss = a['ss']
    for a_, b_, w_ in (stt_words(142, 0) or []):
        if re.search(r'colombiana', wt.nz(w_)) and ss <= a_ <= ss + a['dur']:
            a['beeps'].append((round(a_ - ss - 0.42, 2), round(b_ - ss + 0.08, 2)))
    log3(142, 'L-07', '«la colombiana» audible', 'Pitido igual que los nombres')
def fx_146(seg):  # L-09
    p = seg['src'][0][0]
    to_wave(seg, own_bg(p, 8.5, 'sala146')); drop_rot(seg)
    add_r1(seg, 'Testigo', 'Juicio en el TS · 07/04/2026')
    log3(146, 'L-09', 'Primer plano de la testigo y apellido', 'Forma de onda sobre la sala desenfocada; rótulo «TESTIGO · JUICIO EN EL TS · 07/04/2026»')
def fx_151(seg):  # L-01: alarga 3 s el plano de Sánchez, sin audio nuevo, y fundido de 12 fotogramas
    vi = [x for x in seg['pieces'] if x['t'] == 'clip'][-1]
    vi['dur'] = round(vi['dur'] + 3.0, 3); vi['len'] = vi['len'] + 3.0; seg['D'] = round(seg['D'] + 3.0, 3); seg['vfade_out'] = 0.48
    log3(152, 'L-01', 'Tarjeta «Es evidente que me equivoqué…» sin Diario de Sesiones del 09/07/2025 en la carpeta', 'Fuera; el plano anterior de Sánchez se alarga 3 s con fundido de 12 fotogramas')
def fx_177(seg):  # T-08
    seg['pieces'] = [card3(G.t2('Denuncias internas por acoso contra un alto cargo del PSOE: esperaron meses.', kick='FERRAZ · SEDE FEDERAL DEL PSOE'), 't177', seg['D'])]
    log3(177, 'T-08', 'Plano de la presentadora de RTVE (pulseras)', 'No hay plano de fachada de la Moncloa ni de Ferraz en disco: tarjeta con fondo desenfocado', 'parcial')
def fx_180(seg):  # T-03
    seg['pieces'] = [card3(G.q1('«Rajoy y Aznar han tenido 15 ministros imputados o condenados. Yo he tenido la desgracia de tener uno.»',
                                'Pedro Sánchez · Salvados (laSexta) · 22/11/2026\nNewtral (25/06/2026): de los ministros de Aznar, tres fueron condenados; no todos los demás fueron imputados',
                                None, 'SU CIFRA · NEWTRAL LA DESMIENTE EN PARTE'), 'q180', seg['D'])]
    log3(180, 'T-03', 'Etiqueta y línea de Newtral cortadas', 'Etiqueta «SU CIFRA · NEWTRAL LA DESMIENTE EN PARTE»; Newtral en dos líneas dentro del área segura')
def fx_182(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['vcut'] = 0.5
    log3(182, 'QC', 'Destello blanco en 25:01:20', 'Fuera los últimos fotogramas')
def fx_186(seg):
    to_wave(seg, own_bg(seg['src'][0][0], 30.0, 's186')); drop_rot(seg)
    add_r1(seg, 'Trabajadora de Ferraz', 'Testigo · Grabación difundida por El Debate · 13/11/2025')
    log3(186, 'QC', 'Imagen congelada y marca de El Debate (25:47)', 'Forma de onda con subtítulo sobre la sala desenfocada')
def fx_188(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['vcut'] = 0.35
    log3(188, 'V-03', 'Cortinilla azul de TVE', 'Fuera')
def fx_191(seg):  # T-09
    seg['pieces'] = [card3(G.d1('27/05/2026', 'Agentes de la UCO entran en Ferraz, sede federal del PSOE, con un requerimiento del juez'), 'd191', seg['D'])]
    seg['ov'] = []
    log3(191, 'T-09', 'Comparecencia con faldón de TVE bajo «UCO EN FERRAZ»', 'No hay plano de la fachada de Ferraz en disco: tarjeta de dato con fondo desenfocado', 'parcial')
def fx_195(seg):  # L-10 + V-06
    D = seg['D']; d1 = round(D / 2, 2)
    seg['pieces'] = [card3(G.t1('INVESTIGADA', 'Leire Díez, militante socialista. La prensa la bautizó como «la fontanera».'), 't195a', d1),
                     card3(G.q1('«obstaculizar de forma sistemática y continuada» procedimientos judiciales', 'Auto del juez Pedraz · según el auto, formaba parte de una trama', None, 'LEIRE DÍEZ · INVESTIGADA'), 't195b', round(D - d1, 3))]
    seg['ov'] = []
    log3(195, 'L-10', 'Foto de Leire Díez en blanco y negro, primerísimo plano y con grano', 'No hay foto a color en capturas/: sin foto, dos tarjetas con su situación procesal', 'parcial')
    log3(195, 'V-06', 'Cabecera animada de otro medio (27:20)', 'Fuera (la fila ya no usa ese vídeo)')
def fx_203(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['vcut'] = 0.25; p['z'] = 0.05
    log3(203, 'V-04', 'Fotogramas del desfile con el círculo amarillo', 'Fuera')
def fx_208(seg):
    pass
def fx_215(seg): set_audio_tc(seg, 0, to=10.62, fade=0.12); log3(215, 'S-01', 'Acababa en «el caso de José Luis Ábalos…» (el archivo se corta ahí)', 'Salida en la pausa tras «…es así» con fundido de 120 ms')
def fx_222(seg):
    to_wave(seg, own_bg(F_('cortes/clip_19c_derecho_no_responder.mp4'), 5.0, 'beg222')); drop_rot(seg)
    add_r1(seg, 'Juez y Begoña Gómez', 'Grabación difundida por Vozpópuli · 05/07/2024')
    log3(222, 'L-16', 'Marca grande de Vozpópuli en la grabación judicial', 'Forma de onda con subtítulo y rótulo «Grabación difundida por Vozpópuli»')
def fx_229(seg):
    to_wave(seg, SANCHEZ_BG('s229')); drop_rot(seg)
    add_r1(seg, 'Pedro Sánchez ante el juez', 'Grabación difundida por OKDiario · 24/09/2024')
    add_nota(seg, 'Acogerse a la dispensa era su derecho como cónyuge.', 5.0, seg['D'] - 0.2, 'v3_c229')
    log3(229, 'L-16', 'Mosca de OKDiario y congelado (32:01–32:06)', 'Forma de onda con subtítulo y rótulo «Grabación difundida por OKDiario»')
def fx_235(seg):
    seg['pieces'] = [P_clip(F_('cortes/clip_19c_derecho_no_responder.mp4'), 1.0, seg['D'], crop=None, z=0.04)]
    log3(235, 'L-16', 'Fotograma con la marca de Vozpópuli', 'Otro plano del mismo caso: Begoña Gómez en la Asamblea (13/11/2024)')
def fx_242(seg): set_audio_tc(seg, 0, ss=11.45); log3(242, 'S-04', 'Se comía la primera sílaba', 'Entrada en «nada acorde» con fundido de 10 ms')
def fx_252(seg):  # T-05
    seg['pieces'] = [card3(G.d1('20/11/2025', 'Primer fiscal general del Estado condenado · Recurso de amparo pendiente ante el TC'), 'd252', seg['D'])]
    log3(252, 'T-05', 'Falta el recurso pendiente', '«Recurso de amparo pendiente ante el TC»')
def fx_255(seg): set_audio_tc(seg, 0, to=4.34, fade=0.10); log3(255, 'S-01', 'Acababa en «además…»', 'Salida tras «…del Estado» con fundido de 100 ms')
def fx_259(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['ozones'] = [[int(W * 0.62), int(H * 0.66), W, H]]
    log3(259, 'QC', 'Cabeza ajena en la esquina (35:48–36:00)', 'Desenfoque localizado de la esquina')
def fx_272(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['ss'] = 4.5
    log3(272, 'V-05', 'Cabecera de The Wild Project', 'Entrada después de la cabecera')
def fx_284(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['crop'] = C110; p['ozones'] = [[int(W * 0.76), 0, W, int(H * 0.13)]]
    log3(284, 'L-16', 'Mosca de Expansión', 'Recorte al 110 % que la deja fuera')
def fx_287(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['vcut'] = 0.3
def fx_288(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['ss'] = p['ss'] + 0.6; p['crop'] = 'iw*0.91:ih*0.91:iw*0.045:0'; p['ozones'] = [[0, int(H * 0.49), W, H], [int(W * 0.80), 0, W, int(H * 0.14)]]
    seg['ov'] = [o for o in seg['ov'] if not ovname(o).startswith('cv')]
    log3(288, 'QC', 'Línea azul diagonal (40:00) y rótulo de El País', 'Entrada 0,6 s después; desenfoque localizado del faldón con nuestro rótulo encima')
def fx_300(seg):  # L-13
    to_wave(seg); drop_rot(seg); add_r1(seg, 'Félix Bolaños', 'La Moncloa · 02/05/2022')
    log3(300, 'L-13', 'Vídeo de EFE', 'No hay vídeo de La Moncloa en disco: forma de onda con subtítulo y rótulo «La Moncloa · 02/05/2022»')
def fx_305(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p.setdefault('ozones', []).extend([[0, int(H * 0.56), W, H], [0, 0, int(W * 0.16), int(H * 0.15)]])
    set_audio_tc(seg, 0, to=30.45, fade=0.12); log3(305, 'S-01', 'Acababa en «de manera…»', 'Salida tras «…migración regular.» con fundido de 120 ms')
def fx_315(seg):  # L-14
    if len(seg['pieces']) == 4:
        seg['pieces'][3] = card3(G.q1('«Socio terrible»', 'Donald Trump'), 'q315', seg['pieces'][3]['dur'])
    log3(315, 'L-14', 'Imagen de Trump con la marca de ABC', 'Tarjeta «Socio terrible» · Donald Trump, sin foto')
def fx_318(seg):  # L-04
    D = seg['D']; d1 = round(D * 0.5, 2)
    seg['pieces'] = [P_img(card(G.m1('BARBATE', 'Cádiz · 09/02/2024'), 'v3_m318'), d1, z=0.03), card3(G.d1('Barbate · 09/02/2024', 'Dos guardias civiles muertos'), 'd318', round(D - d1, 3))]
    log3(318, 'L-04', 'Vídeo del choque de la narcolancha', 'No hay plano neutro del puerto en archivo/: mapa de Barbate y tarjeta «Barbate · 09/02/2024 · Dos guardias civiles muertos»')
def fx_339(seg):  # T-10
    D = seg['D']; d1 = round(D * 0.5, 2)
    seg['pieces'] = [P_clip(F_('cortes/clip_r6_puente_mejor_momento.mp4'), 3.0, d1, crop=C110TR), P_img(capture_png(F_('capturas/doc_10d_BOE_cese_Puente_04-11-2026.jpg'), 'v3_c339'), round(D - d1, 3), z=0.03)]
    seg['ov'] = []; add_r1(seg, 'Óscar Puente', 'Ministro de Transportes · Senado')
    add_nota(seg, 'BOE · cese de Óscar Puente · 04/11/2026', d1 + 0.3, D - 0.15, 'v3_n339')
    log3(339, 'T-10', 'Collages ilustrados (VALLADOLID, PUENTE DIMITE, sillón rojo)', 'Plano de archivo de Puente y BOE del cese')
def fx_348(seg):
    seg['pieces'] = [card3(G.q1('«Yo siempre he ido a ceremonias aconfesionales, nunca he ido a oficios religiosos, que respeto profundamente.»', 'Pedro Sánchez · La Séptima · 09/11/2026'), 'q348', seg['D'])]
    log3(348, 'QC', 'Comillas dobles y fuente dentro de la cita', 'Cita y fuente separadas')
def fx_347(seg):
    seg['pieces'] = [p if p['t'] != 'black' else dict(P_img(card(G.bgcard(), 'v3_empty'), p['dur'], z=0), v3='card') for p in seg['pieces']]
    for p in seg['pieces']:
        if p['t'] == 'img' and 'q1_347' in p['path']: p['path'] = card(G.q1('«Yo siempre he ido a ceremonias aconfesionales, nunca he ido a oficios religiosos, que respeto profundamente.»', 'Pedro Sánchez · La Séptima · 09/11/2026'), 'v3_q347')
def fx_349(seg):  # L-18
    for p in seg['pieces']:
        if p['t'] == 'clip': p['ozones'] = [[0, int(H * 0.62), int(W * 0.55), H], [int(W * 0.86), 0, W, int(H * 0.16)]]
    log3(349, 'L-18', 'Rótulos quemados de otros medios («Sánchez y Torra coinciden…», «…acude al entierro…»)', 'Desenfoque localizado')
def fx_358(seg): pass
def fx_367(seg):  # L-15: ≤10 s; dos tramos del mismo plano
    p, ss, to = seg['src'][0]
    set_audio_tc(seg, 0, ss=3.48, to=4.50, fade=0.01)
    d2 = round((20.85 - 14.64) * FPS) / FPS
    seg['src'].append((p, 14.64, 20.85))
    seg['audio'].append(dict(t='clip', path=p, ss=14.64, dur=d2, at=seg['D'], beeps=[], wave=False))
    seg['pieces'].append(P_clip(p, 14.64, d2, src_len=d2, crop=[x for x in seg['pieces'] if x['t'] == 'clip'][0].get('crop')))
    seg['D'] = round(seg['D'] + d2, 3)
    drop_rot(seg); add_r1(seg, 'Pedro Sánchez', 'Al Rojo Vivo · laSexta · 20/02/2024', 'DIJO')
    log3(367, 'L-15', 'Corte de televisión privada de 19 s', 'Dos tramos del mismo plano (7,2 s): «…que es la fachosfera» y la pregunta con su respuesta')
def fx_379(seg): set_audio_tc(seg, 0, to=126.45, fade=0.10); log3(379, 'S-02', 'Se comía «no venir»', 'Salida alargada hasta la palabra')
def fx_388(seg):  # L-11
    seg['pieces'] = [card3(G.q1('«Como vamos a ganar y vamos a ser primera fuerza política… esa pregunta no hace falta que me la hagas.»', 'Pedro Sánchez · Salvados · laSexta · 22/11/2026'), 'q388', min(seg['D'], 7.0))]
    seg['D'] = seg['pieces'][0]['dur']
    log3(388, 'L-11', '«Yo tengo mis datos… muy buena pinta»', 'Fuera; la tarjeta se queda con la primera frase')
def fx_395(seg):  # L-17
    for p in seg['pieces']:
        if p['t'] == 'clip': p['ozones'] = [ZB]; p['crop'] = None
    seg['ov'] = [o for o in seg['ov'] if not ovname(o).startswith('cv')]
    log3(395, 'L-17', 'Faldón de OKDiario «AL CAUDILLO SÁNCHEZ…»', 'Desenfoque suave localizado; queda nuestro rótulo')
def fx_401(seg):  # L-06: la tarjeta cubre el hueco del audio retirado (lectura completa)
    T = clean(E3[401]['Texto en pantalla (+ # verificación)']); nw = len(re.findall(r'\w+', T)); need = round(min(10.0, 1.0 + nw / 3.4) * FPS) / FPS
    if need > seg['D']:
        seg['pieces'][-1]['dur'] = round(seg['pieces'][-1]['dur'] + need - seg['D'], 3); seg['D'] = need
    log3(402, 'L-06', 'Audio atribuido (Argentina)', f'Fuera el audio; la tarjeta anterior dura {seg["D"]:.1f} s (lectura completa)')
def fx_403(seg): seg['vfade_out'] = 0.48; log3(404, 'T-07', 'Tarjeta de Mojácar', 'Fuera; 403 y 405 con fundido de 12 fotogramas')
def fx_405(seg): seg['vfade_in'] = 0.48
def fx_420(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p['crop'] = C110TR
    log3(420, 'L-16', 'Mosca de El Debate', 'Recorte al 110 % que la deja fuera')
def fx_40(seg): fx_420(seg)
def fx_5(seg): fx_420(seg)
def fx_443(seg):  # D-07
    seg['pieces'] = [P_clip(F_('cortes/clip_r6_caraacara_04_tolerancia_cero.mp4'), 12.0, seg['D'], crop=None)]
    seg['ov'] = [o for o in seg['ov'] if not ovname(o).startswith('cv')]
    log3(443, 'D-07', 'Plano repetido del cara a cara (1:01:17)', 'Otro plano del cara a cara (Feijóo escuchando)')
def fx_446(seg):
    for p in seg['pieces']:
        if p['t'] == 'img': p['path'] = frame_at(F_('cortes_externos/00a_dimita_elindependiente__(ext)s.mp4'), 3.0, 'v3_f446', crop=C110)
    log3(446, 'V-06', 'Logotipo de otro medio (1:02:29)', 'Fotograma limpio del mismo vídeo')
def fx_454(seg):  # T-02
    T = clean(E3[454]['Texto en pantalla (+ # verificación)']) + ' Situaciones procesales a 25/11/2026.'
    seg['pieces'] = [card3(G.t2(T), 't454', seg['D'])]
    log3(454, 'T-02', 'Aviso final sin fecha de las situaciones procesales', '«Situaciones procesales a 25/11/2026.»')
def fx_285(seg):  # L-03
    q = '«Este verano os he preparado una playlist con algunas de las canciones que más estoy escuchando de este año…»'
    D = round(max(4.0, 1.0 + len(q.split()) / 3.4) * FPS) / FPS
    seg['pieces'] = [card3(G.q1(q, 'TikTok de Pedro Sánchez · 01/08/2026'), 'q285', D)]; seg['audio'] = []; seg['ov'] = []; seg['D'] = D; seg['src'] = []
    log3(285, 'L-03', 'Bajo la voz del TikTok de la «playlist» hay un fondo continuo (≈ −44 dB, sin pausas limpias): probable canción', 'La «playlist» pasa a tarjeta con la cita, sin el audio')
def fx_12(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p.setdefault('ozones', []).append([0, int(H * 0.86), int(W * 0.12), H])
    log3(12, 'QC', 'Mosca de AS TV abajo a la izquierda', 'Desenfoque localizado')
def fx_14(seg):
    for p in seg['pieces']:
        if p['t'] == 'clip': p.setdefault('ozones', []).append([0, 0, int(W * 0.32), int(H * 0.13)])
    log3(14, 'QC', 'Logo de Libertad Digital arriba a la izquierda', 'Desenfoque localizado')
def fx_4(seg): seg['vfade_out'] = 0.32; log3(4, 'V-08', 'Salida seca de la intro', 'Fundido de 8 fotogramas')
FIX3 = {k[3:]: v for k, v in globals().items() if k.startswith('fx_') and callable(v)}
FIX3 = {int(k): v for k, v in FIX3.items() if k.isdigit()}

# ------------------------------------------------------------------ pasada global
XROWS = {n for n, r in E3.items() if r['Visual en pantalla (archivo de recurso)'].startswith('X1')}
KEEPSUB = {59, 26, 27, 13, 18, 285, 286}
NOZB = {7, 15, 16, 28, 41, 52, 61, 66, 67, 84, 90, 93, 94, 105, 107, 124, 127, 151, 156, 158, 182, 207, 221, 239, 254, 255, 267, 269, 271, 272, 290, 294, 303, 324, 326, 335, 336, 356, 379, 396, 407, 424, 447}
NOBG = ('m1', 'cap_', 's1_', 'presenta', 'v2_s1', 'card_v3_m318')
def isrealcard(p):
    if p['t'] != 'img': return False
    if p.get('v3') == 'card': return True
    return is_card(p['path'])
def post3(segs):
    # 1 · faldones: fuera la franja negra; recorte ≤ 110 % + desenfoque localizado con el rótulo encima
    for s in segs:
        keep = []
        for o in s['ov']:
            b = ovname(o); m = re.match(r'cv\d+_\d+_(\d+)\.png$', b)
            if b == 'band.png' or (m and int(m.group(1)) in (600, 790, 880)):
                y = 600 if (m and m.group(1) == '600') else 770
                t = 0.0
                for p in s['pieces']:
                    if p['t'] == 'clip' and t < o[2] and t + p['dur'] > o[1]:
                        p.setdefault('ozones', [])
                        if [0, y, W, H] not in p['ozones']: p['ozones'].append([0, y, W, H])
                    t += p['dur']
                continue
            keep.append(o)
        if len(keep) != len(s['ov']): log3(s['n'], 'C', 'Franja negra opaca sobre faldón ajeno', 'Desenfoque suave localizado; nuestro rótulo A encima')
        s['ov'] = keep
        for p in s['pieces']:
            if p['t'] == 'clip' and p.get('crop') == CROP:
                p['crop'] = C110
                if s['n'] not in KEEPSUB:
                    p.setdefault('ozones', [])
                    for z in ([] if s['n'] in NOZB else [ZB]) + ZCORN:
                        if z not in p['ozones']: p['ozones'].append(z)
        # rótulos y carteles: animación estándar A (8 fotogramas + 6 px) y duración mínima de lectura
        nov = []
        for o in s['ov']:
            pp, a, b, f = o[:4]
            if f is True: f = 'A'
            if f == 'A' and ovname(o).startswith(('r1_', 'v2_r', 'r3_')):
                b = max(b, min(s['D'] - 0.08, a + 3.0))
            nov.append((pp, a, b, f))
        s['ov'] = nov
        rots = [o for o in s['ov'] if ovname(o).startswith(('r1_', 'v2_r', 'r3_'))]
        if rots:
            top = min(Image.open(o[0]).getbbox()[1] for o in rots)
            for i, o in enumerate(s['ov']):
                b = ovname(o)
                if b.startswith(('cart', 'v3_c', 'v3_n')) and any(o[1] < r[2] and o[2] > r[1] for r in rots):
                    im = Image.open(o[0]); bb = im.getbbox()
                    if bb and bb[3] > top - 10:
                        sh_ = top - 16 - bb[3]; im2 = Image.new('RGBA', im.size, (0, 0, 0, 0)); im2.paste(im, (0, sh_))
                        s['ov'][i] = (png(im2, 'stk_' + b[:-4]), o[1], o[2], o[3])
    # 2 · negro plano fuera de los silencios del EDL → fondo desenfocado
    for s in segs:
        if s['tipo'] in ('silencio', 'apertura', 'intro'): continue
        for i, p in enumerate(s['pieces']):
            if p['t'] == 'black':
                s['pieces'][i] = dict(P_img(card(G.bgcard(), 'v3_empty'), p['dur'], z=0), v3='card')
    # 3 · pasos de expediente: fundido a negro de 20 fotogramas, negro ≤ 1 s con cama musical, cartel con fundido de 12
    for i, s in enumerate(segs):
        if s['n'] in XROWS:
            j = i - 1
            if segs[j]['tipo'] == 'silencio':
                segs[j]['D'] = 0.4; segs[j]['pieces'] = [P_black(0.4)]; segs[j]['bed'] = True; j -= 1
            pv = segs[j]; pv['vfade_out'] = 0.8
            for p in pv['pieces']: p['dark'] = False
            s['vfade_in'] = 0.48; s['vfade_out'] = 0.48; s['bed'] = True
            log3(s['n'], 'D-03 / S-05', 'Corte seco a negro con silencio digital', 'Fundido a negro de 20 fotogramas, negro de 0,4 s y cartel sobre cama musical')
    for s in segs:
        if s['tipo'] == 'silencio' and s['D'] > 1.5:
            s['D'] = 1.5; s['pieces'] = [P_black(1.5)]; log3(s['n'], 'QC', 'Silencio en negro de más de 1,5 s', 'Recortado a 1,5 s')
    # 4 · tarjetas B: fondo = plano vecino desenfocado y oscurecido; ninguna tarjeta fija más de 10 s
    last = None; pend = []
    def setbg(p, src, key):
        p['bgimg'] = bg_png(src, key)
    for s in segs:
        newp = []
        for k, p in enumerate(s['pieces']):
            if p['t'] == 'clip' and not p.get('vert'):
                last = (p['path'], (p['ss'] or 0) + min(p['dur'], p.get('len', p['dur'])) / 2, p.get('crop'))
            if isrealcard(p):
                if last: setbg(p, last, f"{s['n']}_{k}")
                else: pend.append(p)
                if p['dur'] > 10.0 and last:
                    D = p['dur']; parts = []; rem = D; flip = True
                    while rem > 0.01:
                        d = min(rem, 7.0 if flip else 4.0)
                        if rem - d < 2.0: d = rem
                        if flip: q = dict(p, dur=round(d, 3))
                        else: q = P_clip(last[0], max(0, last[1] - 2.0), round(d, 3), src_len=round(d, 3), crop=last[2], z=0.04)
                        parts.append(q); rem -= d; flip = not flip
                    log3(s['n'], 'B', f'Tarjeta fija de {D:.1f} s', 'Alterna con el plano relacionado: nunca más de 10 s fija')
                    newp += parts; continue
            newp.append(p)
        s['pieces'] = newp
    first = next(((p['path'], 5.0, p.get('crop')) for s in segs for p in s['pieces'] if p['t'] == 'clip' and '/intro/' not in p['path']), None)
    for p in pend: setbg(p, first, 'first_' + hashlib.md5(p['path'].encode()).hexdigest()[:6])
    # 5 · formas de onda sin fondo: fotograma del propio corte desenfocado
    for s in segs:
        for k, p in enumerate(s['pieces']):
            if p['t'] == 'wave' and not p.get('bgimg'): p['bgimg'] = own_bg(p['path'], p['ss'] + p['dur'] / 2, f"{s['n']}_{k}")
    # 6 · nunca más de dos formas de onda seguidas
    run = 0
    for s in segs:
        hasw = any(p['t'] == 'wave' for p in s['pieces']); hasv = any(p['t'] in ('clip', 'img') for p in s['pieces'])
        run = run + 1 if hasw and not hasv else 0
        if run > 2: log3(s['n'], 'D', 'Tres formas de onda seguidas', 'Revisar', 'pendiente')
    for s in segs:
        tot = round(sum(p['dur'] for p in s['pieces']), 3)
        if abs(tot - s['D']) > 0.02: s['pieces'][-1]['dur'] = round(s['pieces'][-1]['dur'] + s['D'] - tot, 3)
    return segs

# ------------------------------------------------------------------ D-08 · créditos nuevos
SAFE_X = G.SAFE_X
CR_TXT = B + 'CREDITOS_FUENTES_PANTALLA.txt'
def credit_media():
    L = [l.split(' · ') for l in open(CR_TXT, encoding='utf-8') if re.match(r'^\d+ · ', l)]
    seen = {}
    for x in L:
        m = x[1].strip(); k = m.lower()
        if k not in seen: seen[k] = m
    return sorted(seen.values(), key=lambda m: m.lower().lstrip('0123456789'))
BADCR = {10, 229, 222, 186, 25, 26, 27, 44, 300, 146, 395, 349, 142, 402, 8, 152, 177, 288, 203, 195, 67, 115, 188, 182, 272, 446, 48, 59}
def credits3():
    cw = int(W * 0.55) - SAFE_X - 40
    blocks = [('', ['Un documental de DocuVox'], 1), ('Fuentes y medios consultados', credit_media(), 2),
              ('Música', ['Mixkit (Mixkit Stock Music Free License)'], 1), ('Mapas', ['Natural Earth (dominio público)'], 1),
              ('Archivo', ['Congreso de los Diputados, Senado, Tribunal Supremo, La Moncloa, BOE'], 1), ('', ['DocuVox'], 1)]
    roll = G.credits_roll(blocks, cw); rp = png(roll, 'v3_roll'); rh = roll.height
    v = 72.0; Dr = round((rh + H * 0.55) / v * FPS) / FPS
    out = f'{AQ}/v3_credits.mp4'
    # montaje de la ventana 16:9 con planos del propio documental (1,5-2,5 s, fundidos de 8 fotogramas, sin repetir)
    sel = []; seen = set()
    cand = [x for x in VOZFRAMES if x[0] not in BADCR and x[0] < 440]
    k = int(Dr // 2.0) + 1; step = max(1, len(cand) // k)
    for x in cand[::step]:
        if x[1] in seen: continue
        seen.add(x[1]); sel.append(x)
    sel = sel[:k]
    WW, WH = 768, 432
    key = hashlib.md5((json.dumps([(a, b, round(c, 1)) for a, b, c, d in sel]) + str(Dr) + str(rh) + 'c3').encode()).hexdigest()[:8]
    if not os.path.exists(out + key):
        parts = []
        for i, (nn, p, t, c) in enumerate(sel):
            d = 2.0 if i % 3 else (2.4 if i % 2 else 1.6)
            q = f'{PNG}/crm_{i}.mp4'; cf = f'crop={c},' if c else ''
            sh(['ffmpeg', '-v', 'error', '-y', '-ss', f'{max(0, t - 1):.2f}', '-t', f'{d:.2f}', '-i', p, '-an', '-vf',
                f'{cf}crop=iw*0.86:ih*0.80:iw*0.07:ih*0.04,scale={WW}:{WH}:force_original_aspect_ratio=increase,crop={WW}:{WH},setsar=1,fps={FPS},format=yuv420p,'
                f'fade=t=in:d=0.32,fade=t=out:st={d - 0.32:.2f}:d=0.32', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', q])
            parts.append(q)
        lst = f'{PNG}/crm.txt'; open(lst, 'w').write(''.join(f"file '{x}'\n" for x in parts))
        sh(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{PNG}/crm_all.mp4'])
        x0 = int(W * 0.55) + (int(W * 0.45) - WW - SAFE_X) // 2; y0 = (H - WH) // 2
        sh(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-t', f'{Dr:.3f}', '-i', f'color=c=0x0E0F11:s={W}x{H}:r={FPS}',
            '-loop', '1', '-framerate', str(FPS), '-t', f'{Dr:.3f}', '-i', rp, '-stream_loop', '-1', '-i', f'{PNG}/crm_all.mp4',
            '-filter_complex', f"[1:v]format=rgba[r];[0:v][r]overlay=x={SAFE_X}:y='{H}-t*{v}':shortest=1[a];"
                               f"[2:v]setpts=PTS-STARTPTS,format=yuv420p[m];[a][m]overlay=x={x0}:y={y0}:shortest=1,"
                               f"drawbox=x={x0 - 1}:y={y0 - 1}:w={WW + 2}:h={WH + 2}:color=0x3A3D42:t=1,fade=t=in:d=0.5,fade=t=out:st={Dr - 3:.2f}:d=3,format=yuv420p",
            '-t', f'{Dr:.3f}', '-r', str(FPS), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-an', out])
        open(out + key, 'w').write('ok')
    intro = card3(G.t2('Documental crítico de DocuVox. Fuentes, medios y fechas de cada declaración, en la descripción. ¿Le aludimos? Escríbanos: publicaremos su rectificación conforme a la LO 2/1984.', kick='DOCUVOX'), 'cr0', 8.0)
    pcs = [intro, P_clip(out, 0, Dr, src_len=Dr, crop=None)]
    D = round(8.0 + Dr, 2)
    log3(455, 'T-01', 'Cartel final', 'Texto nuevo con la LO 2/1984')
    log3(455, 'D-08', 'Créditos por páginas', f'Rodillo a dos columnas ({len(credit_media())} medios) y ventana 16:9 con {len(sel)} planos del documental; {Dr:.0f} s')
    return dict(n=455, tipo='cartel', ov=[], audio=[], src=[], edl_dur=D, D=D, kind='créditos', pieces=pcs)

def plan_all3():
    segs = opening()
    order = [r for r in ROWS]
    i35 = next(i for i, r in enumerate(order) if r['#'] == '35'); i37 = next(i for i, r in enumerate(order) if r['#'] == '37')
    r37 = order.pop(i37); order.insert(i35, r37)
    order = [r for r in order if int(r['#']) not in REMOVE3]
    for r in order:
        n = int(r['#'])
        CUR['bottom'] = SUBBOT.get(n, 980)
        s = plan_row(r) if n != 455 else credits3()
        CUR['bottom'] = 980
        if n in FIX3: FIX3[n](s)
        s = add_pause(s)
        if s.get('tag') in ('HIZO', 'DIJO') and not s.get('pause'):
            s['pieces'][-1]['dur'] = round(s['pieces'][-1]['dur'] + HIZODIJO_PAUSE, 3); s['D'] = round(s['D'] + HIZODIJO_PAUSE, 3); s['pause'] = HIZODIJO_PAUSE
        segs.append(s)
    for n in (8, 344):
        log3(n, 'L-08' if n == 8 else 'S-09', '«¿De qué prostíbulos ha vivido usted?» en la ráfaga' if n == 8 else 'Pregunta de Feijóo sobre los audios del maquinista sin respuesta ni fuente',
             'Fuera; 7 y 9 con corte limpio y microfundidos de 10 ms' if n == 8 else 'Fuera (opción recomendada)')
    return post3(segs)

if __name__ == '__main__':
    S = plan_all3()
    json.dump(S, open(AQ + '/plan3.json', 'w'), ensure_ascii=False, indent=0, default=str)
    json.dump(dict(inc=INC, tc=TCLOG, log3=LOG3), open(AQ + '/plan3_log.json', 'w'), ensure_ascii=False, indent=0)
    print(len(S), 'segmentos', round(sum(s['D'] for s in S), 1), 's')
