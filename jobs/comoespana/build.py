# -*- coding: utf-8 -*-
"""Construye el job de «Cómo funciona REALMENTE España»: planos anclados, animaciones Manim con cues
sincronizados a la palabra, y jobs/comoespana/job.json.

    python build.py cues      → escribe anim/cues/*.json (tiempos por palabra de voz_words.json)
    python build.py job       → escribe job.json (necesita las animaciones renderizadas en media/comoespana/anim)
"""
import sys, os, json, re, unicodedata, difflib, copy
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import guion as G
from num2words import num2words

TEMPO = 0.9           # atempo lineal del motor (sin estirar pausas: los cues siguen valiendo)
LEAD = 0.1            # el plano empieza 0,1 s antes de su palabra (anchor_lead)
HOLD = 4.0            # segundos de cola en cada animación (por si el plano se alarga)
MEDIA = 'media/comoespana'
WORDS = json.load(open(os.path.join(HERE, 'voz_words.json')))

def norm_tokens(s):
    s = re.sub(r'(\d+)[.,](\d{3})', lambda m: m.group(1) + m.group(2), s)
    s = re.sub(r'(\d+)\s*%', lambda m: m.group(1) + ' por ciento', s)
    s = s.replace('XIX', 'diecinueve')
    s = re.sub(r'\d+', lambda m: ' ' + num2words(int(m.group()), lang='es') + ' ', s)
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-zñ0-9]+', s)

def wseq(key):
    """[(t, token)] de la unidad, expandiendo cifras de whisper a palabras."""
    out = []
    for a, b, w in WORDS[key]:
        toks = norm_tokens(w)
        for j, tk in enumerate(toks): out.append((a + (b - a) * j / max(1, len(toks)), tk))
    return out

def find_t(key, phrase, after=0.0):
    seq = wseq(key); q = norm_tokens(phrase); L = len(q)
    toks = [t for _, t in seq]
    for j in range(len(toks) - L + 1):
        if seq[j][0] >= after - 0.05 and toks[j:j + L] == q: return seq[j][0]
    best, bj = 0, None
    for j in range(len(toks)):
        if seq[j][0] < after - 0.05: continue
        r = difflib.SequenceMatcher(None, ' '.join(q), ' '.join(toks[j:j + L])).ratio()
        if r > best: best, bj = r, j
    if bj is None or best < 0.6: raise SystemExit(f'cue no encontrado en {key}: «{phrase}» ({best:.2f})')
    return seq[bj][0]

def unit_dur(key): return WORDS[key][-1][1] + 0.15 if WORDS[key] else 3

# ------------------------------------------------------------------ planos
# P = foto/vídeo de archivo (casting en Commons); A = animación Manim; C = tarjeta del motor
def P(q, at=None, lt=None, video=False, **kw):
    d = dict(video=q, old=False) if video else dict(photo=q, src='commons')
    if at: d['at'] = at
    if lt: d['lt'] = lt
    d.update(kw); return d
def A(scene, at=None, cues=None, p=None, name=None):
    return dict(_anim=scene, _name=name or scene, at=at, _cues=cues or {}, _p=p or {})
def C(card, at=None): return dict(card=card, **({'at': at} if at else {}))

SHOTS = {
 'g1': [P('Palacio de las Cortes Madrid fachada', lt=['Congreso de los Diputados', 'Madrid']), P('urna electoral España elecciones', at='Imagina que ganas'),
        P('Hemiciclo del Congreso de los Diputados', at='Eres el más votado', kw='GANAS… Y NO GOBIERNAS'), P('Congreso de los Diputados leones', at='Y no es teoría')],
 'g2': [P('Bundeshaus Bern', at='En Suiza', lt=['Palacio Federal', 'Berna (Suiza)']), P('Bundeshaus Bern Bundesratszimmer', at='gobiernan siete'),
        P('Casa de la Vall Andorra', at='En Andorra', lt=['Casa de la Vall', 'Andorra la Vella']), P('Catedral de la Seu d\'Urgell', at='Uno es el obispo', lt=['Catedral de Santa María', 'La Seu d\'Urgell']),
        P('Palais de l\'Élysée', at='El otro', lt=['Palacio del Elíseo', 'París'])],
 'g3': [P('Congreso de los Diputados interior pleno', at='Quién manda'), P('Palacio Real de Madrid', at='Para qué sirve'), P('Agencia Tributaria edificio Madrid', at='Adónde van'),
        P('Berlaymont building Brussels', at='Y cuánto se decide', lt=['Comisión Europea', 'Bruselas']), P('The Blue Marble NASA Apollo 17', at='hay que dar la vuelta')],
 'a1': [P('Palacio de la Moncloa', at='El domingo no vas', lt=['Palacio de la Moncloa', 'Madrid']), P('papeletas elecciones generales España sobre', at='Su nombre ni siquiera'),
        P('colegio electoral España votación', at='Lo que eliges'), P('Hemiciclo Congreso Diputados vista general', at='Trescientos cincuenta')],
 'a2': [A('Hemiciclo', at='Y son ellos', cues=dict(mayoria='ciento setenta y seis', mitad='la mitad más uno', segunda='segunda votación', sies='le basta'))],
 'a3': [C(dict(type='quote', text='El candidato propuesto expondrá ante el Congreso de los Diputados el programa político del Gobierno que pretenda formar y solicitará la confianza de la Cámara', attrib='Constitución española · artículo 99.2'))],
 'a4': [A('Suma', at='Por eso el más votado', cues=dict(suma='si otros partidos', acuerdo='se ponen de acuerdo', suyo='el Gobierno es suyo')),
        A('Repeticion', at='Y si pasan', cues=dict(dos='dos meses', r2016='dieciséis', r2019='diecinueve'))],
 'a56': [P('Victor D\'Hondt', at='un jurista belga', lt=['Victor D\'Hondt', 'jurista belga (1841-1901)']),
         A('DhondtVotos', at='Imagina una provincia', cues=dict(A='El partido A', B='el B', C='el C', D='el D', E='y el E', barrera='Primera regla', fuera='Adiós'))],
 'a7': [A('DhondtTabla', at='Ahora', cues=dict(divide='se dividen', s1='cuarenta mil', s2='treinta mil', s3='veinte mil', s4='dieciocho mil', s5='quince mil', resultado='Resultado', cero='Cero'))],
 'a8': [A('SoriaMadrid', at='Y aquí viene', cues=dict(minimo='al menos dos', soria='Soria', madrid='Madrid', veces='Un escaño de Soria'))],
 'a9': [P('Palace of Westminster', at='Ahora, otro país', lt=['Palacio de Westminster', 'Londres']),
        A('Mayoritario', at='El país se divide', cues=dict(distritos='seiscientos cincuenta', uno='en cada uno', resto='Los demás votos', dato='En dos mil veinticuatro'))],
 'a10': [P('Palais Bourbon Assemblée nationale', at='Francia', lt=['Asamblea Nacional', 'París']), P('bureau de vote France élections urne', at='una semana después'),
         P('Assemblée nationale hémicycle', at='Puedes quedar segundo')],
 'a11': [A('TresSistemas', at='Mira lo que ocurre', cues=dict(votos='Mira', h1='exactamente', h2='tres sistemas', h3='El reparto'))],
 'a12': [P('United States Capitol west front', at='Y luego está', lt=['Capitolio', 'Washington D. C.']),
         A('ColegioElectoral', at='Allí, al presidente', cues=dict(electores='quinientos treinta y ocho', estados='Cada estado', n270='Hacen falta', votos='En dos mil dieciséis', perdio='y perdió'))],
 'a13': [P('Urna electoral', at='Así que tu voto'), P('Palacio Real de Madrid fachada sur', at='o el rey', lt=['Palacio Real', 'Madrid'])],
 'b1': [C(dict(type='quote', text='La forma política del Estado español es la Monarquía parlamentaria', attrib='Constitución española · artículo 1.3'))],
 'b2': [A('OrganigramaEspana', at='Traducido', cues=dict(rey='El jefe del Estado', sanciona='sanciona', propone='propone', gobierno='Y el jefe del Gobierno', refrendo='Sus actos'))],
 'b3': [A('Comparativa', at='En otros países', cues=dict(usa='En Estados Unidos', fra='En Francia', ale='En Alemania', sui='Y en Suiza'))],
 'b4': [A('Monarquias', at='Las monarquías', cues=dict(reinan='Hay reyes que reinan', ESP='España', SWE='Suecia', GBR='Reino Unido', gobiernan='Y hay reyes', SAU='Arabia'))],
 'b5': [A('Reinos', at='Y aquí va', cues=dict(canada='Canadá', australia='Australia', nz='Nueva Zelanda', jamaica='Jamaica', quince='quince'))],
 'b6': [P('Constitución española 1978 ejemplar original', at='Ahora bien')],
 'c1': [A('Reformas', at='Las reglas', cues=dict(ref='referéndum', art='ciento sesenta', cuatro='solo cuatro', ultima='Formentera'))],
 'c2': [P('Houses of Parliament London Thames', at='El Reino Unido', lt=['Parlamento británico', 'Londres']), P('Magna Carta British Library', at='Sus reglas', lt=['Carta Magna (1215)', 'British Library']),
        P('Parliament Buildings Wellington Beehive', at='Nueva Zelanda', lt=['Parlamento', 'Wellington (Nueva Zelanda)'])],
 'c3': [P('Tribunal Supremo Madrid', at='Y quién vigila', lt=['Tribunal Supremo', 'Madrid']),
        A('Tribunales', at='En España hay dos', cues=dict(supremo='El Tribunal Supremo', constitucional='El Tribunal Constitucional', doce='Tiene doce'))],
 'c4': [P('Wisconsin Supreme Court chamber', at='Y en Estados Unidos', lt=['Tribunal Supremo de Wisconsin', 'EE. UU.']), P('judicial election campaign sign', at='Hacen campaña')],
 'c5': [P('Congreso de los Diputados votación pleno', at='Pero')],
 'd1': [A('Mocion', at='Se puede', cues=dict(otro='proponer a otro', n176='ciento setenta y seis', ya='Si lo logra', seis='En democracia', una='Solo una'))],
 'd2': [A('Impeachment', at='En Estados Unidos', cues=dict(camara='La Cámara', senado='el Senado juzga', tercios='dos tercios', cuatro='Cuatro veces', ninguno='Ninguno'))],
 'd3': [P('Constitutional Court of Korea', at='En Corea del Sur', lt=['Tribunal Constitucional', 'Seúl (Corea del Sur)']),
        P('2016 South Korean protests candlelight Gwanghwamun', at='destituyó a Park', lt=['Protestas de 2016-2017', 'Seúl']), P('2024 South Korean martial law National Assembly', at='y a Yoon')],
 'd4': [P('Cortes de Castilla y León edificio Valladolid', at='Hasta aquí')],
 'e1': [A('Autonomias', at='Diecisiete', cues=dict(diecisiete='Diecisiete', servicios='hospitales', foral='Y el País Vasco'))],
 'e2': [A('Federales', at='En la Constitución', cues=dict(esp='En la Constitución', ale='Alemania', usa='Estados Unidos', sui='Y Suiza')), P('Landsgemeinde Glarus', at='y sus ciudadanos votan', lt=['Landsgemeinde', 'Glaris (Suiza)'])],
 'e3': [P('euro banknotes coins', at='Y todo eso')],
 'f1': [A('Cien', at='Imagina', cues=dict(cien='Imagina', ps='cuarenta y uno', san='Catorce', serv='Trece', eco='Once', edu='Nueve', seg='Cuatro', resto='Y el resto'))],
 'f2': [A('Intereses', at='Fíjate', cues=dict(intereses='solo en intereses', mas='Más que'))],
 'f3': [A('Deuda', at='Porque las administraciones', cues=dict(billon='alrededor de', pib='más o menos', quien='A quién', ext='Casi la mitad', euro='El segundo', resto='Y el resto'))],
 'f4': [A('PresionFiscal', at='Pagamos', cues=dict(esp='En España', dk='En Dinamarca', golfo='Y en países')), P('Dubai skyline Burj Khalifa', at='el Estado vive', lt=['Dubái', 'Emiratos Árabes Unidos'])],
 'f5': [P('Berlaymont Brussels European Commission', at='Pero hay decisiones', lt=['Comisión Europea', 'Bruselas'])],
 'h1': [A('UnionEuropea', at='En la Unión', cues=dict(ue='Unión Europea', regl='los reglamentos', dir='las directivas', prima='Y si una ley'))],
 'h2': [A('Euro', at='El euro', cues=dict(veintiuno='veintiún', bulgaria='Bulgaria', bce='Fráncfort')), P('European Central Bank Frankfurt Seat', at='en el Banco Central', lt=['Banco Central Europeo', 'Fráncfort'])],
 'h3': [A('BrexitONU', at='Salir es posible', cues=dict(brexit='El Brexit', onu='Y por encima', cinco='cinco países', esp='España, no'))],
 'h4': [P('United Nations General Assembly hall', at='Hasta ahora')],
 'i1': [P('Guaita San Marino', at='San Marino', lt=['Guaita', 'San Marino']),
        A('Ficha', at='Y los cambia', name='FichaSanMarino', cues=dict(dato='el uno de abril'), p=dict(iso='SMR', ll=[12.45, 43.94], nombre='San Marino', sub='dos jefes de Estado a la vez', num='6', numsub='MESES DE MANDATO', lines=['Capitanes regentes', 'relevo: 1 de abril y 1 de octubre', 'tradición documentada desde 1243']))],
 'i2': [P('Istana Negara Kuala Lumpur', at='En Malasia', lt=['Istana Negara', 'Kuala Lumpur']),
        A('Ficha', at='Nueve sultanes', name='FichaMalasia', cues=dict(dato='para cinco años'), p=dict(iso='MYS', ll=[102.0, 3.5], nombre='Malasia', sub='un rey elegido', num='9', numsub='SULTANES ELIGEN AL REY', lines=['mandato de 5 años', 'el trono va rotando']))],
 'i3': [P('Piazza San Pietro Vaticano', at='El Vaticano', lt=['Plaza de San Pedro', 'Ciudad del Vaticano']), P('Cappella Sistina interno', at='elegido por los cardenales', lt=['Capilla Sixtina', 'lugar del cónclave'])],
 'i4': [P('Schloss Vaduz', at='En Liechtenstein', lt=['Castillo de Vaduz', 'Liechtenstein']),
        A('Ficha', at='Y lo más curioso', name='FichaLiechtenstein', cues=dict(dato='en dos mil tres'), p=dict(iso='LIE', ll=[9.55, 47.14], nombre='Liechtenstein', sub='el príncipe puede vetar leyes', num='2003', numsub='REFERÉNDUM QUE AMPLIÓ SUS PODERES', lines=['2003: sí con un 64 %', '2012: el 76 % rechaza recortarlos']))],
 'i5': [P('Punakha Dzong Bhutan', at='Y en Bután', lt=['Punakha Dzong', 'Bután']),
        A('Ficha', at='Su Constitución', name='FichaButan', cues=dict(dato='Y el país'), p=dict(iso='BTN', ll=[90.4, 27.5], nombre='Bután', sub='Constitución de 2008', num='65', numsub='AÑOS: EDAD DE RETIRO DEL REY', lines=['Felicidad Nacional Bruta', 'como meta del Estado']))],
 'i6': [P('Ballot box Spain election', at='Ahora vuelve'),
        A('Recap', at='Tu voto se suma', cues=dict(provincia='Tu voto se suma', dhondt='La ley', diputados='Los diputados', rey='El rey', tc='El Constitucional', comunidad='Tu comunidad', bruselas='Y una parte'))],
 'i7': [P('Congreso de los Diputados fachada noche', at='Ningún sistema'), P('Puerta del Sol Madrid kilómetro cero', at='Ahora ya sabes')],
}
# respiraciones de música sola (6-7 s) tras los ganchos fuertes, con su plano
BREATH = {'a8': ('Soria', ['Soria', 'Castilla y León']), 'c3': ('Tribunal Constitucional de España', ['Tribunal Constitucional', 'Madrid']), 'h1': ('European Parliament Strasbourg hemicycle', ['Parlamento Europeo', 'Estrasburgo']), 'a12': ('Lincoln Memorial reflecting pool', ['Washington D. C.', 'EE. UU.']),
          'b5': ('Parliament Hill Ottawa', ['Parlamento de Canadá', 'Ottawa']), 'c4': ('United States Supreme Court building', ['Tribunal Supremo', 'Washington D. C.']),
          'd3': ('Gwanghwamun Square Seoul', ['Plaza de Gwanghwamun', 'Seúl']), 'e2': ('Bern old town Aare', ['Berna', 'Suiza']),
          'f4': ('Nyhavn Copenhagen', ['Copenhague', 'Dinamarca']), 'h3': ('United Nations Security Council chamber', ['Consejo de Seguridad', 'Nueva York']),
          'i5': ('Paro Taktsang Tiger\'s Nest', ['Paro Taktsang', 'Bután'])}

def units_seq():
    """Secuencia final de unidades (a5 y a6 van fusionadas en a56)."""
    out = []
    for u in G.S:
        if u['key'] == 'a6': continue
        u = dict(u)
        if u['key'] == 'a5':
            a6 = next(x for x in G.S if x['key'] == 'a6'); u['key'] = 'a56'; u['text'] = u['text'] + ' ' + a6['text']
        out.append(u)
    return out

def cues():
    os.makedirs(os.path.join(HERE, 'anim', 'cues'), exist_ok=True); plan = []
    for u in units_seq():
        key = u['key']; sh = SHOTS.get(key, [])
        anchors = []
        for s in sh:
            anchors.append(find_t(key, s['at']) if s.get('at') else 0.0)
        for j, s in enumerate(sh):
            if '_anim' not in s: continue
            t0 = anchors[j]; t1 = anchors[j + 1] if j + 1 < len(sh) else unit_dur(key) + 1.6 * TEMPO
            dur = (t1 - t0) / TEMPO + LEAD + HOLD
            tt = {}
            last = t0
            for name, phrase in s['_cues'].items():
                ta = find_t(key, phrase, last); last = ta + 0.05
                tt[name] = round((ta - t0) / TEMPO + LEAD, 2)
            js = dict(dur=round(dur, 2), t=tt, p=s['_p'], unit=key, scene=s['_anim'], shot=round((t1 - t0) / TEMPO, 2))
            json.dump(js, open(os.path.join(HERE, 'anim', 'cues', s['_name'] + '.json'), 'w'), ensure_ascii=False, indent=1)
            plan.append((s['_name'], s['_anim'], js['dur'], tt))
    for p in plan: print(p[0], p[1], p[2], p[3])
    json.dump([dict(name=n, scene=sc) for n, sc, _, _ in plan], open(os.path.join(HERE, 'anim', 'plan.json'), 'w'), indent=1)

CHAPTER_YT = {'t1': 'Ganas y no gobiernas', 't2': 'Rey o presidente: formas de gobierno', 't3': 'Constitución y Tribunal Constitucional',
              't4': 'Moción de censura e impeachment', 't5': 'Comunidades autónomas y federalismo', 't6': 'Impuestos y deuda pública',
              't7': 'Cuánto manda la UE', 't8': 'Los gobiernos más raros del mundo'}
BEDS = {'g1': 'tema', 't1': 'pulso', 't2': 'mundo', 't3': 'calma', 't4': 'pulso', 't5': 'mundo', 't6': 'calma', 't7': 'pulso', 't8': 'mundo', 'i6': 'tema'}
MIX = lambda n, t: {'mixkit': f'https://assets.mixkit.co/music/{n}/{n}.mp3', 'title': t, 'page': 'https://mixkit.co/free-stock-music/'}

PICK = {'Palacio de las Cortes Madrid fachada': 6, 'Hemiciclo del Congreso de los Diputados': 1, 'Congreso de los Diputados leones': 6, 'Bundeshaus Bern': 6,
        'Bundeshaus Bern Bundesratszimmer': 0, 'Casa de la Vall Andorra': 4, "Catedral de la Seu d'Urgell": 0, "Palais de l'Élysée": 6, 'Palacio Real de Madrid': 1,
        'Berlaymont building Brussels': 0, 'The Blue Marble NASA Apollo 17': 1, 'Palacio de la Moncloa': 4, 'papeletas elecciones generales España sobre': 0,
        "Victor D'Hondt": 7, 'Palace of Westminster': 0, 'Palais Bourbon Assemblée nationale': 6, 'bureau de vote France élections urne': 1,
        'Assemblée nationale hémicycle': 1, 'United States Capitol west front': 6, 'Lincoln Memorial reflecting pool': 7, 'Palacio Real de Madrid fachada sur': 6,
        'Parliament Hill Ottawa': 6, 'Constitución española 1978 ejemplar original': 0, 'Houses of Parliament London Thames': 5, 'Magna Carta British Library': 0,
        'Parliament Buildings Wellington Beehive': 3, 'Wisconsin Supreme Court chamber': 7, 'judicial election campaign sign': 7, 'United States Supreme Court building': 3,
        '2016 South Korean protests candlelight Gwanghwamun': 0, '2024 South Korean martial law National Assembly': 4, 'Gwanghwamun Square Seoul': 3,
        'Cortes de Castilla y León edificio Valladolid': 6, 'Landsgemeinde Glarus': 3, 'Bern old town Aare': 0, 'euro banknotes coins': 5, 'Dubai skyline Burj Khalifa': 6,
        'Nyhavn Copenhagen': 6, 'Berlaymont Brussels European Commission': 6, 'European Central Bank Frankfurt Seat': 3, 'United Nations Security Council chamber': 6,
        'United Nations General Assembly hall': 5, 'Guaita San Marino': 0, 'Istana Negara Kuala Lumpur': 7, 'Piazza San Pietro Vaticano': 7, 'Cappella Sistina interno': 4,
        'Schloss Vaduz': 2, 'Punakha Dzong Bhutan': 0, "Paro Taktsang Tiger's Nest": 1, 'Congreso de los Diputados fachada noche': 0, 'Puerta del Sol Madrid kilómetro cero': 2}
# consultas sin material propio: otro candidato (distinto archivo) de otra búsqueda coherente
ALT = {'urna electoral España elecciones': ('Palacio de las Cortes Madrid fachada', 2), 'Congreso de los Diputados interior pleno': ('Hemiciclo del Congreso de los Diputados', 0),
       'Agencia Tributaria edificio Madrid': ('euro banknotes coins', 7), 'colegio electoral España votación': ('papeletas elecciones generales España sobre', 4),
       'Hemiciclo Congreso Diputados vista general': ('Hemiciclo del Congreso de los Diputados', 4), 'Congreso de los Diputados votación pleno': ('Hemiciclo del Congreso de los Diputados', 5)}
CASTQ = {}
for f in sorted(os.listdir(HERE)):
    if f.startswith('castq_r') and f.endswith('.json'): CASTQ.update(json.load(open(os.path.join(HERE, f))))
PICK2 = {}   # picks del segundo casting (se rellenan tras revisarlo)

def shot_out(s):
    s = dict(s)
    q = s.get('photo')
    if q:
        ref = (q, PICK[q]) if q in PICK else ALT.get(q) or ((q, PICK2[q]) if q in PICK2 else None)
        if ref and ('photo:' + ref[0]) in CASTQ:
            c = CASTQ['photo:' + ref[0]][ref[1]]
            s.pop('photo'); s.pop('src', None); s['commons'] = c['title']
    if '_anim' in s:
        d = dict(file=f"{MEDIA}/anim/{s['_name']}.mp4", start=0, grade=False, fuente='propia')
        if s.get('at'): d['at'] = s['at']
        return d
    return {k: v for k, v in s.items() if not k.startswith('_') and v is not None}

def job():
    U = []; chapters = []; prev_seq = units_seq()
    for u in prev_seq:
        key = u['key']
        if key in BEDS: U.append(dict(k='B', track=BEDS[key]))
        if u['k'] == 'T':
            if u['key'] == 't0':
                U.append(dict(k='T', key=key, secs=4.5, voice_at=0.5, sting='golpe', text=u['text'], url=f'{MEDIA}/voz/t0.mp3',
                              card=dict(type='title', title='Cómo funciona realmente España', sub='Por qué ganar las elecciones no basta')))
            else:
                U.append(dict(k='T', key=key, secs=u['secs'] + 1.0, sting='golpe', chapter=True, title=CHAPTER_YT[key],
                              card=dict(type='title', title=u['title'].capitalize() if False else u['title'], sub=f"Capítulo {u['num']}", n=str(u['num']))))
            continue
        uu = dict(k=u['k'], key=key, voice=u['voice'], text=u['text'], url=f'{MEDIA}/voz/{"a56" if key == "a56" else key}.mp3',
                  shots=[shot_out(s) for s in SHOTS.get(key, [])])
        U.append(uu)
        if key == 'a56': chapters.append(dict(unit=len(U) - 1, title="Ley D'Hondt explicada"))
        if key in BREATH:
            q, lt = BREATH[key]
            U.append(dict(k='M', track=BEDS.get(key, 'calma') if False else 'tema', secs=7.5, shots=[shot_out(dict(photo=q, src='commons', lt=lt))]))
    ig3 = next(i for i, u in enumerate(U) if u.get('key') == 'g3')
    job = dict(id='comoespana', title='Cómo funciona REALMENTE España', channel='DocuVox', stage='cast', align=True, align_model='small',
               no_pad=True, reuse={'max': 1, 'gap': 600}, auto_sfx={}, sfx_max=5, max_shot=10, min_shot=1.6, anchor_lead=LEAD, max_still=6,
               theme={'base': 'plataforma', 'accent': [242, 193, 78], 'text': [244, 247, 251], 'dim': [143, 163, 191], 'bg0': [10, 20, 36], 'bg1': [19, 33, 58],
                      'fonts': {'display': 'gf:ofl/barlowcondensed/BarlowCondensed-ExtraBold.ttf', 'display_light': 'gf:ofl/barlowcondensed/BarlowCondensed-SemiBold.ttf',
                                'body': 'gf:ofl/barlowcondensed/BarlowCondensed-Medium.ttf', 'italic': 'gf:ofl/barlowcondensed/BarlowCondensed-MediumItalic.ttf',
                                'body_bold': 'gf:ofl/barlowcondensed/BarlowCondensed-Bold.ttf'}, 'tracking': 0.06, 'grade': 'neutro'},
               music={'tema': MIX(153, 'Electron 01'), 'pulso': MIX(161, 'Minimal Techno 02'), 'mundo': MIX(184, 'Vastness'), 'calma': MIX(110, 'Departure'),
                      'golpe': MIX(676, 'Epical Drums 01')},
               audio={'voice_db': -20, 'bed_db': {'tema': -36, 'pulso': -37, 'mundo': -36, 'calma': -36, 'golpe': -31}, 'inter_db': -22,
                      'pause_stretch': 0, 'pause_cap': 0.6, 'gap_n': 2.0, 'gap_q': 1.1},
               tempo=TEMPO, parts=4, codec='hevc', max_kbps=1100, audio_kbps='128k', intro=[], inserts=[dict(after_unit=ig3, file='assets/intro/docuvox.mp4')],
               chapters=chapters, seed=29, rev=1, units=U)
    p = os.path.join(HERE, 'job.json')
    if os.path.exists(p):
        old = json.load(open(p))
        for k in ('picks', 'qpicks', 'rev', 'stage'):
            if k in old: job[k] = old[k]
    json.dump(job, open(p, 'w'), ensure_ascii=False, indent=1)
    print('unidades', len(U), 'planos', sum(len(u.get('shots') or []) for u in U))

if __name__ == '__main__':
    {'cues': cues, 'job': job}.get(sys.argv[1], lambda: print(__doc__))()
