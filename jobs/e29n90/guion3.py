# -*- coding: utf-8 -*-
"""PEDRO SÁNCHEZ · LA ENTREVISTA QUE NADIE LE HIZO — montaje v3: «versión crítica» (Auditoría 360, sección 7).

- Las 10 preguntas en su orden. La locución es la misma de v1: solo se recorta (fuera el argumentario y las
  defensas, tabla 7.2) y se reordena (4 movimientos). No se graba nada nuevo.
- Entran todos los cortes, con su fuente real en el rótulo, sin marcas ajenas (recortes) y de 25 s como máximo.
- Moción de 2018: la frase de la decencia es de ÁBALOS y va rotulada como suya. El espejo final usa la frase
  verificada de Sánchez («¿Está dispuesto a dimitir hoy, aquí, ahora? Dimita, señor Rajoy…»).
- Suelo legal: estado procesal de cada persona, la advertencia sobre Aldama, «ningún tribunal…», la ironía de
  Podemos, avisos de apertura y cierre. Ninguna imagen de IA de personas reales; todas llevan «RECREACIÓN».
- Sistema visual: sin negros, tarjetas siempre sobre imagen, sellos de estado procesal, audiogramas para los
  cortes de solo audio, barra «Pregunta X / 10», subtítulos karaoke (locución y cortes) y flash antes de cada pregunta.
"""
import sys, os, copy, hashlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guion as OLD, guion2 as V2
# tramos exactos fijados con la transcripción de los cortes (stt v3)
ABALOS_DECENCIA = (23.4, 27.6); DIMITA = (23.9, 26.7)
O = OLD.U
CO = 'media/e29n90/cortes/'; DE = 'media/e29n90/decl/'; BR = 'media/e29n90/broll/'; CA = 'media/e29n90/capturas/'; HL = 'media/e29n90/hls/'; EX = 'media/e29n90/ext/'
NQ = 10
AV = EX + 'abalos_mocion_vertical.mp4'; AV_CROP = [0.34, 0.05, 0.32, 0.70]
U = []; CUTS = []
md5 = lambda t: hashlib.md5(t.encode()).hexdigest()[:10]

# ---------------------------------------------------------------- utilidades
DEF_HEADS = ('LA DEFENSA', 'LO QUE DICE EL PSOE', 'TAMBIÉN')
def clean(shots):
    """Fuera las tarjetas de argumentario (versión crítica)."""
    out = []
    for s in shots or []:
        c = s.get('card') or {}
        ls = c.get('lines') or []
        if ls and str(ls[0]).upper().startswith(DEF_HEADS): continue
        out.append(s)
    return out
bgc, ai, at, cap, dijo, aviso, vid = V2.bgc, V2.ai, V2.at, V2.cap, V2.dijo, V2.aviso, V2.vid
F_CONGRESO, F_MONCLOA19, F_DEBATE26, F_WILD, F_ZP, F_DANA, F_CEUTA = V2.F_CONGRESO, V2.F_MONCLOA19, V2.F_DEBATE26, V2.F_WILD, V2.F_ZP, V2.F_DANA, V2.F_CEUTA

# planos ya corregidos en v2, por texto de la locución
V2SH = {}
for u in V2.U:
    if u['k'] in 'NRT' and u.get('text'): V2SH[u['text']] = u.get('shots')

def unit(i, shots=None, **kw):
    """Unidad de locución de v1 tal cual (mismo audio). Planos: los indicados, o los corregidos en v2, o los de v1."""
    u = copy.deepcopy(O[i]); u.pop('chapter', None)
    if shots is None: shots = V2SH.get(u['text'], u.get('shots'))
    u['shots'] = clean(shots); u.update(kw); u['_old'] = i; U.append(u); return u

def piece(i, parts, shots=None, **kw):
    """Recorte de una locución de v1 (sin gastar créditos): parts = [(desde, hasta), ...] por frases del texto.
    desde=None: desde el principio; hasta=None: hasta el final. Se recorta el audio con marcas de whisper (voz/cut.py)."""
    t = O[i]['text']; frag = []
    for a, b in parts:
        ia = t.index(a) if a else 0
        ib = t.index(b, ia + 1) if b else len(t)
        frag.append(t[ia:ib].strip())
    text = ' '.join(frag)
    text = re.sub(r'\s*\[(pause|short pause)\]\s*$', '', text)
    text = text[0].upper() + text[1:]
    if md5(text) == md5(t): return unit(i, shots, **kw)
    CUTS.append(dict(src=md5(t), parts=[[a, b] for a, b in parts], text=text, key=md5(text), voice=O[i]['voice'], old=i))
    u = dict(k=O[i]['k'], voice=O[i]['voice'], text=text, shots=clean(shots if shots is not None else V2SH.get(t, O[i].get('shots'))), _old=i)
    u.update(kw); U.append(u); return u

def C(src, who, where, a, b, **kw):
    u = dict(k='C', src=src, lt=[who, where], fuente='cita', **kw); u['in'] = a; u['out'] = b; U.append(u); return u

def AUD(src, who, where, a, b, quote, bg, t=None, **kw):
    """Corte de solo audio: audiograma (onda, frase en grande, fuente) sobre imagen real."""
    card = dict(type='audiograma', text=quote, attrib=f'{who} · {where}', audio=src, ss=a)
    return C(src, who, where, a, b, audio_only=True, quote=quote, shots=[bgc(card, bg, t)], **kw)

def M(secs, shots, track='pulso'): U.append(dict(k='M', track=track, secs=secs, shots=shots))
def B(track): U.append(dict(k='B', track=track))
def Q(n, i_old, text, bg, t=None):
    u = copy.deepcopy(O[i_old]); u['secs'] = 4.2
    c = dict(type='pregunta', n=f'PREGUNTA {n:02d} / {NQ:02d}', text=text, foot='PEDRO SÁNCHEZ · LA ENTREVISTA QUE NADIE LE HIZO', bgimg=bg)
    if t is not None: c['bgt'] = t
    u['card'] = c; u['title'] = f'{n}. {text}'; u['chapter'] = True; u['shots'] = []; U.append(u)
def FLASH(src, a, b, who, where, **kw):
    """3–5 s del mejor corte del capítulo justo antes de su pregunta."""
    return C(src, who, where, a, b, flash=True, gap=0.25, **kw)
def stamp(text, color='red', sub='', at_=0.8): return dict(stamp=[text, color, sub], stamp_at=at_)

# =====================================================================================
# ARRANQUE (0:00–2:00)
# =====================================================================================
B('tension')
C(CO + 'clip_39b_usted_no_lo_es.mp4', 'Pedro Sánchez a Mariano Rajoy', 'Cara a cara · 14/12/2015 · Academia de TV', 0, 5.6, crop=[0.02, 0.02, 0.86, 0.86], gap=0.2)
C(CO + 'clip_39c_feijoo_decente.mp4', 'Alberto Núñez Feijóo a Pedro Sánchez', 'Cara a cara · RTVE · 19/11/2026', 0, 7.0, crop=[0.05, 0.12, 0.88, 0.88])
unit(3, [aviso(['14/12/2015', '19/11/2026'], *F_DEBATE26, size=60)])
B('pulso')
# tráiler (~35 s): cortes que ya existen, corte seco
C(CO + 'clip_35_bildu_no_vamos_a_pactar.mp4', 'Pedro Sánchez', 'Navarra Televisión · 2015', 1.4, 5.5, crop=[0.0, 0.1, 0.9, 0.9], gap=0.15, trailer=True)
C(CO + 'clip_31_no_dormiria.mp4', 'Pedro Sánchez', 'laSexta · 19/09/2019', 4.7, 10.5, gap=0.15, trailer=True)
C(CO + 'clip_32_traerlo_de_vuelta.mp4', 'Pedro Sánchez', 'Debate electoral · RTVE · 04/11/2019', 0, 3.2, crop=[0.06, 0.0, 0.84, 0.84], gap=0.15, trailer=True)
AUD(CO + 'clip_22_pues_ya_esta.mp4', 'Pedro Sánchez', 'RNE · 06/11/2019', 0, 8.3, '«¿La Fiscalía de quién depende?… Pues ya está»', *F_MONCLOA19, gap=0.15, trailer=True)
C(AV, 'José Luis Ábalos (PSOE) a Mariano Rajoy', 'Moción de censura · Congreso · 31/05/2018', *ABALOS_DECENCIA, crop=AV_CROP, fit=True, gap=0.15, trailer=True)
C(CO + 'clip_14_mano_en_el_fuego.mp4', 'Pedro Sánchez', 'The Wild Project · 13/11/2026', 3.7, 8.2, gap=0.15, trailer=True)
C(CO + 'clip_06_ire_al_hormiguero.mp4', 'Pedro Sánchez', 'La Revuelta · RTVE · 22/10/2026', 0, 3.9, crop=[0.1, 0.14, 0.8, 0.58], trailer=True)
B('tension')
unit(4, [ai('plato_debate'), ai('atriles', at='cara a cara')])
C(CO + 'clip_01b_pido_perdon_corrupcion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0, 15.8)
unit(6, [bgc(dict(type='dijo', left=dict(date='19/11/2026', text='«Pido perdón»'), right=dict(label='Y EN LA MISMA FRASE', date='19/11/2026', text='«Somos gente limpia»', source='Cara a cara · RTVE'), red=True), *F_DEBATE26), ai('pasillo_vacio', at='ocho años')])
unit(8, [bgc(OLD.AVISO['card'], *F_CONGRESO)])
U.append(dict(k='T', voice='TOP', text=O[16]['text'], secs=3.2, voice_at=0.4, sting='golpe',
              card=dict(type='title', title='Pedro Sánchez', sub='La entrevista que nadie le hizo'), shots=[]))

# =====================================================================================
# 1 · ¿POR QUÉ TENDRÍAMOS QUE CREERLE?
# =====================================================================================
Q(1, 18, 'Presidente, ¿por qué tendríamos que creerle?', *F_MONCLOA19)
B('pulso')
unit(20)
C(CO + 'clip_35_bildu_no_vamos_a_pactar.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Navarra Televisión · 2015 · vía El Debate', 1.4, 5.5, lt_at=1.3, crop=[0.0, 0.1, 0.9, 0.9])
unit(22, [dijo('2015 · NAVARRA TV', '«Con Bildu no vamos a pactar»', '20/05/2020', 'Acuerdo de PSOE, Unidas Podemos y EH Bildu para derogar la reforma laboral', 'Fuente: El País · Maldita.es', *F_CONGRESO),
          at(dijo('2015', '«Se lo repito cinco veces o veinte»', 'DICIEMBRE DE 2023', 'EH Bildu logra la alcaldía de Pamplona con el voto del PSOE', 'Fuente: El País', *F_CONGRESO), 'Pamplona')])
unit(23)
C(CO + 'clip_31_no_dormiria.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · laSexta · 19/09/2019 · vía La Razón', 0, 10.5)
unit(25)
unit(26)
C(DE + 'co_cumplimiento_integro__02.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 14/10/2019', 0, 12, crop=[0.09, 0.0, 0.82, 0.82], lt_at=5.0)
unit(29, [aviso(['DEBATE ELECTORAL · RTVE · 04/11/2019'], CO + 'clip_32_traerlo_de_vuelta.mp4', 1.5), ai('belgica_carretera', at='Bélgica')])
C(CO + 'clip_32_traerlo_de_vuelta.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate electoral · RTVE · 04/11/2019', 0, 3.2, crop=[0.06, 0.0, 0.84, 0.84])
C(DE + 'co_referendum_ilegal__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate electoral · RTVE · 04/11/2019 · vía Cadena SER', 0, 11.9, crop=[0.15, 0.0, 0.62, 0.62])
unit(32)
C(DE + 'co_rebelion_2018__01.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · Espejo Público · Antena 3 · 17/05/2018', 15.4, 35.1)
unit(34)
unit(36)
C(CO + 'clip_36_indultos_nunca_cambie.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cadena SER · 28/06/2021', 5.8, 19.4)
unit(39)
AUD(CO + 'clip_33_no_entra_constitucion.mp4', 'Pedro Sánchez', 'Al Rojo Vivo · laSexta · 10/11/2022 · audio', 0, 11.4,
    '«Este Gobierno no va a aceptar (…) No entra en la legislación ni en la Constitución española»', *F_MONCLOA19)
unit(41)
C(CO + 'clip_34b_necesidad_virtud_wild.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 0, 11.0)
# movido (7.2): la investidura de 2023 después del Comité Federal, antes del BOE: la cronología ya no va hacia atrás
AUD(CO + 'clip_33b_acorde_constitucion.mp4', 'Pedro Sánchez', 'Debate de investidura · Congreso · 15/11/2023 · audio', 0, 5.9,
    '«La amnistía que planteamos es perfectamente legal. Es acorde con la Constitución»', *F_CONGRESO)
piece(43, [(None, 'Y aquí está')], [cap('doc_33_BOE_STC_137-2025_amnistia_31-07-2025.jpg', 'LEY DE AMNISTÍA', ['BOE · 11/06/2024'], 'BOE')])
unit(44, [ai('congreso_escalinata'), at(aviso(['CONGRESO · 12/11/2025'], CO + 'clip_36b_nogueras_bloqueado.mp4', 4), 'Nogueras')])
C(CO + 'clip_36b_nogueras_bloqueado.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados · 2025', 0, 12.0, crop=[0.11, 0.0, 0.78, 0.78])
C(DE + 'ul_puigdemont_perpinan__02.mp4', 'Carles Puigdemont (Junts)', 'Perpiñán · 27/10/2025 · vía Cadena SER', 88.3, 112.3)
unit(46, [bgc(dict(type='quote', text='«Nos hemos aprovechado de la ambición de Sánchez para derrotar a España»', attrib='Carles Puigdemont · según El Mundo · noviembre de 2026'), DE + 'ul_puigdemont_perpinan__02.mp4', 100)])
C(DE + 'co_feijoo_decente__01.mp4', 'Alberto Núñez Feijóo', 'Cara a cara · RTVE · 19/11/2026', 4.3, 19.9, crop=[0.15, 0.05, 0.75, 0.75])
unit(49)
C(CO + 'clip_35c_derecho_a_cambiar_de_opinion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 26.6, 36.0)
C(CO + 'clip_35d_horizonte_coherencia.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · Informativos Telecinco · 16/11/2026', 0, 23.6, crop=[0.0, 0.17, 0.69, 0.69], hflip=True)
unit(52, [aviso(['EL HORMIGUERO · ANTENA 3 · JULIO DE 2023'], DE + 'ul_cambiado_opinion__01.mp4', 30)])
C(DE + 'ul_cambiado_opinion__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · El Hormiguero · Antena 3 · 06/07/2023', 24.5, 36.2)
C(DE + 'ul_cambiado_opinion__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · El Hormiguero · Antena 3 · 06/07/2023', 57.5, 72.2)
unit(55, [aviso(['EL HORMIGUERO · 06/07/2023', 'Sobre Cataluña'], DE + 'ul_cambiado_opinion__01.mp4', 180)])
C(DE + 'ul_cambiado_opinion__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · El Hormiguero · Antena 3 · 06/07/2023', 176.2, 191.9)
unit(57, [dijo('06/07/2023', '«Decisiones diferentes a las que dije antes de las elecciones»', '2023-2026', 'Amnistía, Junts y la investidura', 'Fuente: BOE', *F_CONGRESO)])
unit(58)
C(CO + 'clip_36c_nogueras_cinico.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados · 12/11/2025 · vía OKDiario', 0, 18.3, crop=[0.12, 0.0, 0.76, 0.76])
unit(61)

# =====================================================================================
# 2 · ¿QUIÉN ELIGIÓ A JOSÉ LUIS ÁBALOS?
# =====================================================================================
FLASH(AV, *ABALOS_DECENCIA, 'José Luis Ábalos (PSOE) a Mariano Rajoy', 'Congreso · 31/05/2018', crop=AV_CROP, fit=True)
Q(2, 63, 'Presidente, ¿quién eligió a José Luis Ábalos?', *F_CONGRESO)
B('tension')
unit(65, [cap('doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', 'NOTA DEL TRIBUNAL SUPREMO', ['Ábalos · 24 años y 3 meses', 'Koldo García · 19 años y 8 meses'], 'CGPJ · 22/06/2026'),
          at(bgc(dict(type='ficha', name='José Luis Ábalos', role='Exministro de Transportes · exsecretario de Organización del PSOE'), CA + 'doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', **{}), 'Ábalos')])
U[-1]['shots'][-1].update(stamp('CONDENADO', 'red', '24 años y 3 meses'))
unit(66)
piece(67, [('Pedro Sánchez no está', None)], [bgc(dict(type='aviso', lines=['Pedro Sánchez no está imputado', 'en esta causa ni en ninguna otra.'], head=True), *F_CONGRESO)])
unit(68)
piece(69, [('Sin cargo', None)], [ai('carretera_noche'), ai('coche_tarjetas', at='Peugeot'),
           at(bgc(dict(type='board', title='El Peugeot · 2016', nodes=[['Pedro Sánchez', 'candidato'], ['José Luis Ábalos', 'condenado'], ['Santos Cerdán', 'investigado'], ['Koldo García', 'condenado']], links=[[0, 1], [0, 2], [0, 3], [1, 3]], center=True), *F_CONGRESO), 'cuatro')])
unit(70)
unit(71, [vid('mocion2018_sanchez_dimita.mp4', 1, base=EX), aviso(['MOCIÓN DE CENSURA · CONGRESO · 31/05/2018'], EX + 'mocion2018_sanchez_dimita.mp4', 12, at_='moción')])
C(EX + 'mocion2018_sanchez_dimita.mp4', 'Pedro Sánchez', 'Moción de censura · Congreso · 31/05/2018 · señal del Congreso vía Cuarto Poder', 5.8, 30.3, lt_at=6.0, crop=[0.0, 0.08, 0.9, 0.9])
piece(75, [(None, 'Según recuerda')], [aviso(['JOSÉ LUIS ÁBALOS', 'Secretario de Organización del PSOE · 2018'], EX + 'mocion2018_abalos_decencia.mp4', 6)])
# recuperado (7.3): Ábalos en la moción, con su rótulo. Es su frase, no la de Sánchez.
C(AV, 'José Luis Ábalos (PSOE) a Mariano Rajoy', 'Moción de censura · Congreso · 31/05/2018 · vía El Debate', 18.2, 27.6, crop=AV_CROP, fit=True, lt_at=0.9)
C(EX + 'mocion2018_abalos_decencia.mp4', 'José Luis Ábalos (PSOE)', 'Moción de censura · Congreso · 31/05/2018 · vía El Debate', 2.6, 13.6, crop=[0.0, 0.1, 0.9, 0.9], **stamp('CONDENADO', 'red', '2026 · 24 años y 3 meses', 4.0))
piece(75, [('Según recuerda', None)], [aviso(['MARIANO RAJOY'], EX + 'mocion2018_sanchez_dimita.mp4', 17)])
C(CO + 'clip_39_rajoy_lecciones.mp4', 'Mariano Rajoy', 'Moción de censura · Congreso · 31/05/2018 · vía El Debate', 0, 8.0, crop=[0.0, 0.1, 0.9, 0.9])
_u = unit(77); _u['shots'] = [ai('despacho_sello')] + _u['shots']
unit(78)
unit(79, [aviso(['VÍDEO DEL PSOE · MARZO DE 2020'], DE + 'ul_abalos_feminista__01.mp4', 3)])
C(DE + 'ul_abalos_feminista__01.mp4', 'José Luis Ábalos', 'Vídeo del PSOE · #SoyFeministaPorque · marzo de 2020', 0, 9.0, crop=[0.1, 0.0, 0.7, 0.7], **stamp('CONDENADO', 'red', '', 4.0))
unit(81, [ai('expediente_mesa'), at(aviso(['CONGRESO · 09/07/2025'], CO + 'clip_18_feijoo_prostibulos.mp4', 6), 'Feijóo')])
C(CO + 'clip_18_feijoo_prostibulos.mp4', 'Alberto Núñez Feijóo', 'Congreso · 09/07/2025 · vía Libertad Digital', 4.6, 18.4, crop=[0.12, 0.1, 0.65, 0.65])
unit(83, [bgc(dict(type='aviso', lines=['Ningún tribunal ha juzgado al presidente por ello.'], head=True), CO + 'clip_18_feijoo_prostibulos.mp4', 8)])
unit(84)
piece(85, [('El nueve de julio', None)], [aviso(['CONGRESO · 09/07/2025'], HL + 'h16_me_equivoque.mp4', 10)])
C(HL + 'h16_me_equivoque.mp4', 'Habla Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/07/2025 · La Moncloa', 16.3, 20.95)
C(HL + 'h17_politico_limpio.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/07/2025 · La Moncloa', 9.0, 29.5)
unit(89, [ai('ferraz_noche_generica'), at(bgc(dict(type='ficha', name='Santos Cerdán', role='Sucesor de Ábalos en Organización'), *F_CONGRESO), 'Santos Cerdán')])
U[-1]['shots'][-1].update(stamp('INVESTIGADO', 'amber'))

# =====================================================================================
# 3 · ¿SABÍA LO QUE PASABA EN FERRAZ?
# =====================================================================================
AUD(CO + 'clip_15_necesito_a_balas.mp4', 'Leire Díez (grabación)', 'Publicada por El Confidencial · febrero de 2025', 0, 4.0, '«Necesito a Balas»', CA + 'doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', flash=True, gap=0.25)
Q(3, 91, 'Presidente, ¿sabía usted lo que pasaba en Ferraz?', V2.BR + 'ar_dana_coches__03.mp4' if False else CO + 'clip_15g_caso_flagrante.mp4', 2)
B('pulso')
piece(93, [(None, 'El PSOE insiste')], [ai('ferraz_fachada_dia'), ai('oficinas_furgonetas', at='Agentes'), at(aviso(['27/05/2026 · FERRAZ, 70', 'Requerimiento de la UCO · 12 horas'], CO + 'clip_15g_caso_flagrante.mp4', 2), 'doce horas')])
unit(94, [ai('mascarillas_hangar'), at(aviso(['FEBRERO DE 2024', 'Detención de Koldo García · contratos de mascarillas'], *F_CONGRESO), 'Koldo García')])
unit(95)
piece(96, [(None, 'Sánchez lo niega')], [aviso(['VÍCTOR DE ALDAMA', 'Empresario · confesó · condenado'], *F_CONGRESO),
           at(aviso(['LA FOTO · FEBRERO DE 2019', 'Publicada por El Mundo · octubre de 2024'], *F_CONGRESO), 'El Mundo'),
           at(bgc(dict(type='quote', text='Uno no elige con quién se hace una foto.', attrib='Pedro Sánchez · 27/10/2024 · según The Objective'), *F_CONGRESO), 'uno no elige'),
           at(aviso(['Es la palabra de un acusado', 'que buscaba rebajar su condena.'], *F_CONGRESO), 'palabra de un acusado')])
piece(97, [(None, 'Cerdán niega')], [bgc(dict(type='counter', **{'from': 2}, to=39, label='reuniones localizadas por los investigadores, según Voz Pópuli'), *F_CONGRESO)])
unit(98)
AUD(CO + 'clip_15_necesito_a_balas.mp4', 'Leire Díez (grabación)', 'Publicada por El Confidencial · febrero de 2025', 0, 4.0, '«Necesito a Balas»', CA + 'doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg')
piece(100, [(None, 'El PSOE dice'), ('Está investigada', None)], [bgc(dict(type='ficha', name='Leire Díez', role='Militante del PSOE'), *F_CONGRESO, **{})])
U[-1]['shots'][-1].update(stamp('INVESTIGADA', 'amber', 'no condenada'))
unit(101, [aviso(['FEBRERO DE 2024', 'Estalla el caso Koldo'], *F_CONGRESO), at(aviso(['CONGRESO · 28/02/2024'], CO + 'clip_41b_no_tapa.mp4', 2), 'Febrero')])
C(CO + 'clip_41b_no_tapa.mp4', 'Habla Pedro Sánchez', 'RESPUESTA REAL · Congreso · 28/02/2024', 0.8, 3.6)
unit(104)
C(CO + 'clip_15e_corrupcion_cero.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 18/06/2025', 0, 7.7, lt_at=5.4)
unit(106)
C(CO + 'clip_15g_caso_flagrante.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 24/06/2026', 0, 5.0)
C(HL + 'h15f_no_financiado.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 24/06/2026 · La Moncloa', 43.3, 55.2)
unit(109, [aviso(['MAÑANEROS 360 · TVE · 09/09/2026'], DE + 'ul_manyaneros_chantaje__01.mp4', 150)])
C(DE + 'ul_manyaneros_chantaje__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Mañaneros 360 · TVE · 09/09/2026 · vía El País', 147.7, 171.6, crop=[0.0, 0.1, 0.9, 0.72])
unit(111, [dijo('09/09/2026', '«El Partido Socialista no se ha financiado irregularmente»', 'OCTUBRE DE 2026', 'Anticorrupción ve indicios, aunque considera «prematuro» imputar al partido', 'Fuente: Ara', *F_CONGRESO)])
unit(112, [aviso(['CARA A CARA · RTVE · 19/11/2026'], CO + 'clip_20b_sumarios.mp4', 5)])
C(CO + 'clip_20b_sumarios.mp4', 'Alberto Núñez Feijóo', 'Cara a cara · RTVE · 19/11/2026', 3.8, 13.1)
unit(115, [ai('ventana_noche_moncloa_generica')])

# =====================================================================================
# 4 · ¿POR QUÉ SU FAMILIA ESTÁ EN LOS TRIBUNALES?
# =====================================================================================
M(3.2, [bgc(dict(type='quote', text='«Aquí no hay caso, hay fango»', attrib='Pedro Sánchez · laSexta · 17/05/2024'), CO + 'clip_19a_senoras_de.mp4', 3)], track='tension')
Q(4, 117, 'Presidente, ¿por qué su familia está en los tribunales?', CO + 'clip_19a_senoras_de.mp4', 3)
B('tension')
unit(119)
unit(120)
unit(121)
piece(122, [(None, 'Ella niega cualquier')], [ai('aula_vacia'), at(bgc(dict(type='list', header='Lo investigado', items=['Tráfico de influencias', 'Corrupción en los negocios', 'Apropiación indebida', 'Intrusismo']), CO + 'clip_19c_derecho_no_responder.mp4', 4), 'investigado')])
unit(123)
C(CO + 'clip_19d_1_vinculacion.mp4', 'Mercedes Zarzalejo (PP)', 'Asamblea de Madrid · 13/11/2024 · vía Vozpópuli', 3.0, 14.7, crop=[0.0, 0.1, 0.88, 0.88])
C(CO + 'clip_19d_3_software.mp4', 'Mercedes Zarzalejo (PP)', 'Asamblea de Madrid · 13/11/2024 · vía Vozpópuli', 0, 2.8, crop=[0.0, 0.1, 0.88, 0.88])
C(CO + 'clip_19c_derecho_no_responder.mp4', 'Begoña Gómez', 'Asamblea de Madrid · 13/11/2024 · vía Vozpópuli', 0, 14.3, crop=[0.0, 0.1, 0.88, 0.88], **stamp('PROCESADA', 'amber', 'juicio con jurado', 6.0))
piece(128, [(None, 'Y aquí está su defensa'), ('la Fiscalía pide', 'Ella sostiene')],
      [bgc(dict(type='ficha', name='Begoña Gómez', role='Esposa del presidente · juicio con jurado previsto en 2027'), CO + 'clip_19c_derecho_no_responder.mp4', 6)])
U[-1]['shots'][-1].update(stamp('PROCESADA', 'amber'))
unit(129, [aviso(['MITIN DEL PSOE · SEVILLA · 12/11/2026'], CO + 'clip_19a_senoras_de.mp4', 3)])
C(CO + 'clip_19a_senoras_de.mp4', 'Begoña Gómez', 'Mitin del PSOE · Sevilla · 12/11/2026 · vía El País', 0, 6.9, crop=[0.0, 0.08, 0.9, 0.9])
C(CO + 'clip_04_baile_sevilla_completo.mp4', 'Pedro Sánchez y Begoña Gómez', 'Mitin del PSOE · Sevilla · 12/11/2026 · vía OKDiario', 21.0, 26.0, crop=[0.0, 0.12, 0.8, 0.6])
unit(132)
unit(133, [bgc(dict(type='ficha', name='David Sánchez', role='Hermano del presidente'), *F_MONCLOA19)])
U[-1]['shots'][-1].update(stamp('CONDENADO', 'red', 'sentencia recurrida'))
unit(134)
piece(135, [(None, 'El Gobierno lo defendió')])
unit(136, [aviso(['TVE · 01/09/2025'], CO + 'clip_23_jueces_minoria.mp4', 12)])
C(CO + 'clip_23_jueces_minoria.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · TVE · 01/09/2025', 0, 19.3, lt_at=1.2)
piece(139, [(None, 'El Gobierno la defendía'), ('Y hay otra frase', None)], [aviso(['TRES ASOCIACIONES DE JUECES RESPONDEN'], CO + 'clip_23_jueces_minoria.mp4', 12),
            at(aviso(['RNE · 06/11/2019'], *F_MONCLOA19, size=50), 'Radio Nacional')])
AUD(CO + 'clip_22_pues_ya_esta.mp4', 'Pedro Sánchez', 'RNE · 06/11/2019 · audio', 0, 9.8, '«¿La Fiscalía de quién depende?… Pues ya está»', *F_MONCLOA19)
# movido (7.2): el que rectifica es Sánchez, justo después de su audio
piece(142, [('Al día siguiente', 'Seis años')], [aviso(['07/11/2019', 'Sánchez rectifica: «no fui preciso»'], *F_MONCLOA19)])
piece(141, [(None, 'El fiscal general defendió')], [ai('supremo_fachada')])
piece(142, [('Seis años', 'Hubo votos'), ('Y el tribunal', None)],
      [aviso(['TRIBUNAL SUPREMO · 20/11/2025', 'Fiscal general del Estado: dos años de inhabilitación y multa'], *F_CONGRESO),
       at(aviso(['El tribunal no dio por acreditada', 'ninguna orden del presidente'], *F_CONGRESO), 'Y el tribunal')])
unit(143, [aviso(['G20 · JOHANNESBURGO · 23/11/2025'], CO + 'clip_21_creo_inocencia_fiscal.mp4', 2)])
C(CO + 'clip_21_creo_inocencia_fiscal.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · G20 Johannesburgo · 23/11/2025 · vía ABC', 0.4, 5.4, crop=[0.0, 0.1, 0.9, 0.9])
unit(145, [ai('playa_noche_generica')])
piece(147, [(None, 'Su fiscal general'), ('Él, sin', None)],
      [bgc(dict(type='recap', title='Hasta aquí', items=['Bildu, Podemos, Puigdemont: hizo lo contrario', 'José Luis Ábalos · condenado', 'Santos Cerdán · investigado', 'Begoña Gómez · procesada', 'David Sánchez · condenado (no firme)', 'Pedro Sánchez · sin imputación']), *F_CONGRESO)])

# =====================================================================================
# 5 · ¿DÓNDE ESTABA USTED?
# =====================================================================================
M(3.4, [cap('doc_26_ceuta_whatsapp_CNI_Moncloa_29-07-2026.jpg', 'CNI · 29/07/2026 · 13:52', ['«asalto por valla y mar»'], 'La Moncloa')], track='noche')
Q(5, 149, 'Presidente, ¿dónde estaba usted?', BR + 'ar_ceuta_espigon__02.mp4', 12)
B('noche')
unit(151)
unit(152, [ai('espigon_noche'), vid('ar_ceuta_espigon__02.mp4', 40, at='espigón', blur=18),
           at(bgc(dict(type='counter', to=72000, label='entradas en Ceuta, según Maldita.es y elDiario.es'), BR + 'ar_ceuta_espigon__02.mp4', 20), 'setenta y dos mil'),
           at(bgc(dict(type='counter', to=72, label='muertos como mínimo, según la Delegación del Gobierno'), BR + 'ar_ceuta_espigon__02.mp4', 30), 'setenta y dos muertos')])
unit(153)
unit(154, [vid('ar_mareta_llegada__02.mp4', 4), aviso(['LA MARETA · LANZAROTE · AGOSTO DE 2026'], BR + 'ar_mareta_llegada__02.mp4', 4, at_='La Mareta')])
C(CO + 'clip_24a_playlist.mp4', 'Pedro Sánchez', 'Vídeo publicado en sus redes sociales · 01/08/2026 · vía ESdiario', 0, 6.0, crop=[0.335, 0.0, 0.33, 1.0], fit=True)
C(CO + 'clip_24b_feliz_verano.mp4', 'Pedro Sánchez', 'Vídeo publicado en sus redes sociales · 01/08/2026 · vía ESdiario', 0, 4.8, crop=[0.335, 0.0, 0.33, 1.0], fit=True)
unit(157, [ai('sala_calendario'), at(bgc(dict(type='counter', to=25, label='días hasta la reunión del Consejo de Seguridad Nacional'), *F_CEUTA), 'veinticinco'),
           at(aviso(['CONGRESO · 03/09/2026'], CO + 'clip_26_aviso_rutinario.mp4', 2), 'tres de septiembre')])
C(CO + 'clip_26_aviso_rutinario.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 03/09/2026', 0, 5.4)
unit(160)
piece(161, [('Ese mismo día', None)], [aviso(['MAÑANEROS 360 · TVE · 09/09/2026'], DE + 'ul_manyaneros_chantaje__01.mp4', 10)])
C(DE + 'ul_manyaneros_chantaje__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Mañaneros 360 · TVE · 09/09/2026 · vía El País', 0, 13.7, crop=[0.0, 0.1, 0.9, 0.72])
C(CO + 'clip_25_no_estaba_de_vacaciones.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 3.5, 15.7, lt_at=1.2)
unit(164, [aviso(['CONGRESO · 16/09/2026'], CO + 'clip_25c_eso_a_vivas.mp4', 3)])
C(CO + 'clip_25c_eso_a_vivas.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · Congreso · 16/09/2026 · vía Europa Press', 0.6, 5.8)
piece(166, [(None, 'El Gobierno lo defiende')], [ai('valla_frontera_niebla'), at(bgc(dict(type='aviso', lines=['ABRIL DE 2026', 'El Congreso aprueba una resolución contra el giro sobre el Sáhara. Solo vota en contra el PSOE.'], head=True), *F_CEUTA), 'En abril')])
unit(167, [aviso(['JUAN JESÚS VIVAS', 'Presidente de la ciudad autónoma de Ceuta (PP)'], *F_CEUTA),
           at(aviso(['CASA REAL', 'El Rey sigue la situación «con preocupación e indignación»'], *F_CEUTA), 'Casa Real'),
           at(aviso(['CADENA SER · 31/08/2026'], CO + 'clip_28b_rey_ceuta_melilla.mp4', 5), 'anunció')])
C(CO + 'clip_28b_rey_ceuta_melilla.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Hoy por Hoy · Cadena SER · 31/08/2026', 0, 20.8, crop=[0.1, 0.05, 0.8, 0.78])
unit(170, [vid('ar_dana_coches__03.mp4', 40), ai('calle_barro', at='Veintinueve'), vid('ar_dana_poyo__02.mp4', 6, at='Doscientos treinta'),
           at(bgc(dict(type='counter', to=230, label='muertos en tres comunidades · balance de La Moncloa'), *F_DANA), 'muertos')])
unit(171)
piece(172, [('Pero la ley', 'Su defensa')], [at(aviso(['LEY 17/2015', 'Emergencia de interés nacional: a iniciativa propia del Gobierno.', 'No se declaró.'], *F_DANA), 'la ley')])
piece(173, [('Un año después', None)], [vid('ar_dana_poyo__02.mp4', 20), at(aviso(['03/11/2025', 'Dimite Carlos Mazón, presidente de la Generalitat'], *F_DANA), 'Mazón')])
unit(174)
piece(175, [('Y tres años antes', None)], [aviso(['LA PALMA · 20/09/2021'], CO + 'clip_28bx_la_palma_recursos.mp4', 2)])
C(CO + 'clip_28bx_la_palma_recursos.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Palma · 20/09/2021 · vía Público', 0, 6.7, crop=[0.0, 0.1, 0.6, 0.6])
unit(177, [ai('valla_frontera_niebla'), at(aviso(['BRUSELAS · 24/06/2022'], CO + 'clip_30b_bien_resuelto.mp4', 2), 'Bruselas')])
C(CO + 'clip_30b_bien_resuelto.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Bruselas · 24/06/2022 · La Moncloa', 0, 3.6)
piece(180, [(None, 'Interior defendió'), ('El ministro Fernando', None)], [ai('puerto_lancha'), at(aviso(['BARBATE · 09/02/2024', 'Dos guardias civiles muertos'], *F_DANA), 'Mueren')])
unit(181, [aviso(['LA MONCLOA · 29/04/2025'], CO + 'clip_29_operadores_privados.mp4', 3)])
C(CO + 'clip_29_operadores_privados.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 29/04/2025', 0, 6.5)
unit(183, [ai('vias_alta_velocidad_niebla'), ai('vias_recta_amanecer', at='raíles')])

# =====================================================================================
# 6 · ¿QUIÉN RESPONDE POR LAS VÍAS?
# =====================================================================================
M(3.2, [bgc(dict(type='quote', text='«Si hay algo cercano a la infalibilidad, es la alta velocidad española»', attrib='Óscar Puente · 20/01/2026'), CO + 'clip_10b2_bajisima.mp4', 4)], track='noche')
Q(6, 185, 'Presidente, ¿quién responde por las vías?', CO + 'clip_10d2_renuncio_listas.mp4', 8)
B('tension')
unit(187)
C(CO + 'clip_08_tremendamente_extrano.mp4', 'Óscar Puente', 'Ministro de Transportes · 18/01/2026 · vía El Debate', 0, 4.9, crop=[0.0, 0.1, 0.9, 0.9])
C(CO + 'clip_10b2_bajisima.mp4', 'Óscar Puente', 'Ministro de Transportes · enero de 2026', 0, 9.9)
unit(190)
unit(191, [ai('estacion_noche_vacia'), at(bgc(dict(type='counter', to=69, label='muertos en Urda · 28/10/2026'), HL + 'h10_urda.mp4', 220), 'Sesenta y nueve')])
C(HL + 'h10_urda.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Urda (Toledo) · 28/10/2026 · La Moncloa', 211.0, 233.2)
unit(193)
C(CO + 'clip_10d2_renuncio_listas.mp4', 'Óscar Puente', 'Congreso · Diputación Permanente · 03/11/2026 · vía AS TV', 6.7, 15.9, crop=[0.0, 0.0, 0.86, 0.86])
C(CO + 'clip_10d_no_todos_iguales.mp4', 'Óscar Puente', 'Congreso · Diputación Permanente · 03/11/2026 · vía AS TV', 0, 5.7, crop=[0.1, 0.0, 0.8, 0.8])
unit(197)
unit(198, [ai('catedral_banco_vela'), at(aviso(['FUENTES DE LA MONCLOA', 'No acostumbra a asistir a ceremonias religiosas.'], *F_MONCLOA19), 'Fuentes')])
unit(199)
C(CO + 'clip_04z_1_caballe_2018.mp4', 'Funeral de Montserrat Caballé', 'Barcelona · 08/10/2018 · Antena 3', 0, 1.6, crop=[0.1, 0.0, 0.82, 0.82])
C(CO + 'clip_04z_2_sassoli_2022.mp4', 'Funeral de Estado de David Sassoli', 'Roma · 14/01/2022 · La Moncloa', 0, 1.6)
C(CO + 'clip_04z_3_vara_2025.mp4', 'Funeral de Guillermo Fernández Vara', 'Olivenza · 06/10/2025 · El Mundo', 0, 1.6, crop=[0.15, 0.0, 0.82, 0.82])
C(CO + 'clip_04z_4_papa_2026.mp4', 'Misa de León XIV', 'Sagrada Familia · 10/06/2026 · La Moncloa', 0, 1.6)
unit(204)
C(CO + 'clip_04c_te_quiero_mitin.mp4', 'Mitin del PSOE', 'Sevilla · 12/11/2026 · vía El País', 0, 3.0, crop=[0.0, 0.1, 0.9, 0.9])
C(CO + 'clip_04b_baile_montero_completo.mp4', 'María Jesús Montero y Begoña Gómez', 'Mitin del PSOE · Sevilla · 12/11/2026 · vía OKDiario', 0, 6.0, crop=[0.0, 0.08, 0.85, 0.7])
unit(208)
C(CO + 'clip_01c_feijoo_perdon_toledo.mp4', 'Alberto Núñez Feijóo', 'Cara a cara · RTVE · 19/11/2026', 0, 12.3)
piece(210, [('La siguiente pregunta', None)], [ai('congreso_noche')])

# =====================================================================================
# 7 · ¿POR QUÉ SIGUE DEFENDIENDO A ZAPATERO?
# =====================================================================================
FLASH(CO + 'clip_14_mano_en_el_fuego.mp4', 3.7, 8.2, 'Pedro Sánchez', 'The Wild Project · 13/11/2026')
Q(7, 212, 'Presidente, ¿por qué sigue defendiendo a José Luis Rodríguez Zapatero?', *F_ZP)
B('pulso')
unit(214, [ai('caja_fuerte'), cap('doc_14_joyas_Zapatero_TheObjective_11-06-2026.jpg', 'LAS JOYAS', ['Fotos de las joyas, en las bolsas de la Policía'], 'The Objective · 11/06/2026', at_='The Objective')])
piece(215, [(None, 'Zapatero defiende'), ('Pidió la nulidad', None)], [bgc(dict(type='ficha', name='José Luis Rodríguez Zapatero', role='Expresidente del Gobierno · presunción de inocencia'), *F_ZP),
           vid('ar_zapatero_audiencia__01.mp4', 6, at='nulidad')])
U[-1]['shots'][0].update(stamp('INVESTIGADO', 'amber'))
unit(216, [aviso(['MITIN DEL PSOE'], DE + 'ul_zapatero_tener_poco__02.mp4', 4)])
C(DE + 'ul_zapatero_tener_poco__02.mp4', 'José Luis Rodríguez Zapatero', 'Mitin del PSOE · vía Vozpópuli', 1.0, 9.9, crop=[0.0, 0.08, 0.88, 0.88], **stamp('INVESTIGADO', 'amber', '', 3.0))
unit(218, [ai('avion_hangar'), cap('doc_08_plusultra_moncloa_09-03-2021_cabecera.jpg', 'CONSEJO DE MINISTROS · 09/03/2021', ['Rescate de 53 millones a Plus Ultra'], 'La Moncloa', at_='Consejo'),
           at(bgc(dict(type='counter', to=53, label='millones de euros para Plus Ultra · 09/03/2021'), *F_ZP), 'cincuenta y tres')])
unit(219, [aviso(['MAÑANEROS 360 · TVE · 23/07/2026'], CO + 'clip_14b_no_hable_con_nadie.mp4', 4)])
C(CO + 'clip_14b_no_hable_con_nadie.mp4', 'José Luis Rodríguez Zapatero', 'Entrevista · Mañaneros 360 · TVE · 23/07/2026', 0, 12.8, crop=[0.2, 0.0, 0.62, 0.62])
unit(221, [aviso(['LA MONCLOA · JULIO DE 2026'], CO + 'clip_14c_perifrastica.mp4', 3)])
C(CO + 'clip_14c_perifrastica.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · julio de 2026 · vía elDiario.es', 0, 7.8, crop=[0.0, 0.1, 0.85, 0.85])
unit(224, [vid('ar_zapatero_audiencia__01.mp4', 12), at(aviso(['BRUSELAS · 18/06/2026'], DE + 'ar_sanchez_apoyo_zp__01.mp4', 30), 'fijó')])
C(DE + 'ar_sanchez_apoyo_zp__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Bruselas · 18/06/2026 · vía Libertad Digital', 25.2, 45.3, crop=[0.08, 0.06, 0.88, 0.88])
C(DE + 'ar_sanchez_perifrastica__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · julio de 2026 · vía elDiario.es', 73.4, 89.8, crop=[0.0, 0.1, 0.85, 0.85])
unit(228, [aviso(['TVE · 09/09/2026'], CO + 'clip_14a_contar_con_jose_luis.mp4', 3)])
C(CO + 'clip_14a_contar_con_jose_luis.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · TVE · 09/09/2026', 0, 7.9)
unit(230, [aviso(['THE WILD PROJECT · 13/11/2026'], *F_WILD)])
C(CO + 'clip_14_mano_en_el_fuego.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 3.7, 12.8, lt_at=0.8)
unit(232, [bgc(dict(type='recap', title='La mano en el fuego', items=['José Luis Ábalos · condenado', 'Ángel Víctor Torres', 'José Luis Rodríguez Zapatero · investigado']), *F_WILD),
           at(aviso(['CONGRESO DEL PSOE DE CANARIAS · 26/01/2025'], CO + 'clip_12b_admirador_torres.mp4', 3), 'Tenerife')])
C(CO + 'clip_12b_admirador_torres.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso del PSOE de Canarias · 26/01/2025 · Antena 3', 0, 13.6, lt_at=4.0)
unit(234, [bgc(dict(type='aviso', lines=['Ángel Víctor Torres', 'no ha sido condenado por ningún delito.'], head=True), CO + 'clip_12b_admirador_torres.mp4', 12)])
# movido (7.2): la respuesta de La Moncloa, pegada a González y antes de García-Page
piece(235, [(None, 'Y el presidente de Castilla')], [bgc(dict(type='quote', text='«Si alguien tiene que dejarlo, que lo deje el que lo destroza»', attrib='Felipe González · Ateneo de Madrid · febrero de 2026'), *F_CONGRESO)])
piece(238, [(None, 'Pero había otras')], [aviso(['LA MONCLOA', 'González es «una voz más»'], *F_MONCLOA19)])
piece(235, [('Y el presidente de Castilla', None)], [aviso(['EL HORMIGUERO · ANTENA 3 · FEBRERO DE 2026'], CO + 'clip_20f_page_felipe.mp4', 3)])
C(CO + 'clip_20f_page_felipe.mp4', 'Emiliano García-Page (PSOE)', 'Presidente de Castilla-La Mancha · El Hormiguero · Antena 3 · febrero de 2026', 0, 8.1, crop=[0.05, 0.05, 0.9, 0.9])
piece(238, [('Pero había otras', None)], [ai('hemiciclo_vacio')])
unit(240, [bgc(dict(type='recap', title='Hasta aquí', items=['Ceuta: un aviso del CNI «rutinario»', 'La DANA: 230 muertos', 'Adamuz y Urda: un ministro dimitido', 'Zapatero: investigado, la mano en el fuego']), *F_DANA)])

# =====================================================================================
# 8 · ¿SE PUEDE GOBERNAR SIN EL PARLAMENTO?
# =====================================================================================
M(3.2, [bgc(dict(type='quote', text='«con o sin un concurso de un poder legislativo»', attrib='Pedro Sánchez · Comité Federal del PSOE · septiembre de 2024'), *F_CONGRESO)], track='tension')
Q(8, 242, 'Presidente, ¿se puede gobernar sin el Parlamento?', *F_CONGRESO)
B('pulso')
unit(244, [ai('tomo_presupuestos'), at(bgc(dict(type='timeline', header='Presupuestos', events=[['2023', 'Últimos aprobados'], ['2024', 'Prorrogados'], ['2025', 'Prorrogados'], ['2026', 'Prorrogados']]), *F_CONGRESO), 'prorrogados')])
piece(245, [('Y en septiembre', None)], [at(bgc(dict(type='quote', text='«con o sin un concurso de un poder legislativo»', attrib='Pedro Sánchez · Comité Federal del PSOE · septiembre de 2024 · según The Objective'), *F_CONGRESO), 'Comité Federal')])
unit(246, [ai('constitucion_libro'), at(aviso(['LA MONCLOA · 23/05/2020'], DE + 'co_vencido_virus__02.mp4', 8), 'pandemia')])
C(DE + 'co_vencido_virus__02.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 23/05/2020', 5.1, 14.3)
piece(248, [(None, 'El Gobierno sostiene')], [ai('constitucion_libro'), at(bgc(dict(type='dijo', left=dict(date='2020', text='Estados de alarma'), right=dict(date='2021', text='El Tribunal Constitucional anula el primero y la prórroga de seis meses del segundo', source='Fuente: BOE · STC 148/2021 y 183/2021'), red=True), *F_CONGRESO), 'Tribunal')])
unit(249, [aviso(['CONGRESO · 18/12/2024'], CO + 'clip_36bx_bulo_boe.mp4', 5)])
C(CO + 'clip_36bx_bulo_boe.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 18/12/2024 · vía La Vanguardia', 3.45, 9.6, crop=[0.08, 0.06, 0.88, 0.88])
piece(251, [(None, 'El Gobierno la defendió')], [bgc(dict(type='counter', to=17104, label='millones de euros de deuda de Cataluña condonados (pacto con ERC)'), *F_CONGRESO)])
unit(252, [aviso(['CONGRESO DE LOS DIPUTADOS'], DE + 'ul_nogueras_bloqueada__02.mp4', 10)])
C(DE + 'ul_nogueras_bloqueada__02.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados', 2.8, 21.9, crop=[0.11, 0.0, 0.78, 0.78])
unit(255, [ai('hemiciclo_luz'), at(aviso(['MOCIÓN APROBADA', 'Pedía al presidente una cuestión de confianza. No era vinculante.'], *F_CONGRESO), 'No era vinculante')])
unit(256)
unit(257, [aviso(['06/10/2026'], CO + 'clip_37b_contra_la_oposicion.mp4', 2)])
C(CO + 'clip_37b_contra_la_oposicion.mp4', 'María Jesús Montero (PSOE)', '06/10/2026 · vía Libertad Digital', 0, 5.0, crop=[0.15, 0.1, 0.7, 0.7])
unit(259, [aviso(['LASEXTA · 20/02/2024'], CO + 'clip_37f_fachosfera_existe.mp4', 3)])
C(CO + 'clip_37f_fachosfera_existe.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · Al Rojo Vivo · laSexta · 20/02/2024', 0, 21.6, crop=[0.1, 0.05, 0.8, 0.68])
unit(261, [ai('congreso_escaño_vacio'), at(aviso(['CONGRESO · 09/09/2026'], CO + 'clip_26f_perro_sin_amo.mp4', 3), 'Abascal')])
C(CO + 'clip_26f_perro_sin_amo.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/09/2026 · vía elDiario.es', 1.5, 11.8, crop=[0.0, 0.1, 0.88, 0.88], lt_at=0.3)
C(CO + 'clip_26c_ningun_chantaje.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Mañaneros 360 · TVE · 09/09/2026', 0, 9.2, crop=[0.12, 0.0, 0.7, 0.7])
unit(265, [aviso(['CUMBRE DE LA OTAN · ANKARA · 08/07/2026'], CO + 'clip_26e_con_creces.mp4', 3)])
C(CO + 'clip_26d_trump_espana.mp4', 'Donald Trump', 'Cumbre de la OTAN · Ankara · 08/07/2026', 0, 11.7, crop=[0.1, 0.05, 0.8, 0.72])
C(CO + 'clip_26e_con_creces.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cumbre de la OTAN · Ankara · 08/07/2026', 0, 9.1, crop=[0.0, 0.18, 0.8, 0.8])
unit(268, [aviso(['MITIN DE PODEMOS · ZARAGOZA · 31/01/2026'], CO + 'clip_18c_que_voten.mp4', 0.5)])
C(CO + 'clip_18c_que_voten.mp4', 'Irene Montero (Podemos)', 'Mitin de Podemos · Zaragoza · 31/01/2026 · vía AS TV', 0, 11.0, crop=[0.1, 0.0, 0.75, 0.75])
C(CO + 'clip_18bx_barrer_fachas.mp4', 'Irene Montero (Podemos)', 'Mitin de Podemos · Zaragoza · 31/01/2026 · vía AS TV', 0, 12.1, crop=[0.1, 0.0, 0.75, 0.75], lt_at=2.0)
unit(271, [bgc(dict(type='aviso', lines=['Podemos explicó después', 'que aquellas palabras eran irónicas.'], head=True), CO + 'clip_18bx_barrer_fachas.mp4', 6)])
unit(272, [aviso(['ABRIL DE 2023', 'Ley del «solo sí es sí»'], DE + 'co_si_es_si_perdon__01.mp4', 10)])
C(DE + 'co_si_es_si_perdon__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Entrevista en los diarios de Vocento · TVE · abril de 2023', 7.4, 15.6, crop=[0.05, 0.08, 0.7, 0.7])
unit(275, [ai('edificio_obra_parada')])

# =====================================================================================
# 9 · ¿VA LA ECONOMÍA COMO UN COHETE?
# =====================================================================================
FLASH(CO + 'clip_02_millon_viviendas.mp4', 0.8, 3.5, 'Pedro Sánchez', 'Cara a cara · RTVE · 19/11/2026')
Q(9, 277, 'Presidente, ¿va la economía como un cohete para todos?', CO + 'clip_37c_cohete.mp4', 4)
B('pulso')
unit(279, [aviso(['FORO DE FONDOS EUROPEOS · 16/05/2024'], CO + 'clip_37c_cohete.mp4', 4)])
C(CO + 'clip_37c_cohete.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Foro de fondos europeos · 16/05/2024 · vía Libertad Digital', 1.9, 7.1, crop=[0.12, 0.1, 0.85, 0.85])
unit(282)
unit(283, [aviso(['CARA A CARA · RTVE · 19/11/2026'], CO + 'clip_02_millon_viviendas.mp4', 4)])
C(CO + 'clip_02_millon_viviendas.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0.5, 10.5)
unit(285, [dijo('19/11/2026', '«Hemos construido un millón de viviendas»', 'DATOS', 'Unas 705.000 viviendas terminadas (752.000 contando 2018)', 'Fuente: Idealista vía Artículo14 · Maldita.es', CO + 'clip_02_millon_viviendas.mp4', 4),
           at(bgc(dict(type='counter', to=705000, label='viviendas terminadas, frente a 1.000.000'), CO + 'clip_02_millon_viviendas.mp4', 4), 'setecientas cinco')])
unit(287, [ai('portal_madrid_desahucio_generico'), at(aviso(['SEPTIEMBRE DE 2026'], CO + 'clip_37g_maricarmen.mp4', 2), 'Una cámara')])
C(CO + 'clip_37g_maricarmen.mp4', 'Maricarmen, vecina desahuciada (rostro difuminado)', 'Imágenes difundidas por ESdiario · septiembre de 2026', 0, 6.7, crop=[0.0, 0.1, 0.85, 0.75], blur=22)
piece(290, [('En el debate', None)], [aviso(['CARA A CARA · RTVE · 19/11/2026', 'La carta sin respuesta'], *F_DEBATE26)])
unit(291, [aviso(['LA REVUELTA · RTVE · 22/10/2026'], CO + 'clip_06_ire_al_hormiguero.mp4', 2)])
C(CO + 'clip_06_ire_al_hormiguero.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · La Revuelta · RTVE · 22/10/2026', 0, 3.9, crop=[0.1, 0.14, 0.8, 0.58])
unit(293, [aviso(['NO FUE.'], CO + 'clip_06_ire_al_hormiguero.mp4', 2, size=72)])
AUD(CO + 'clip_07_motos_cobardia.mp4', 'Pablo Motos', 'El Hormiguero · Antena 3 · 11/11/2026', 0, 5.7, '«Por un lado es una torpeza política (…) y por otro, a lo mejor es cobardía»', DE + 'ul_cambiado_opinion__01.mp4', 60)
unit(295, [aviso(['THE WILD PROJECT · 13/11/2026'], *F_WILD), at(aviso(['FUERA DE CONTROL · LA SÉPTIMA · 15/11/2026'], CO + 'clip_05_chulazo.mp4', 1.6), 'La Séptima')])
C(CO + 'clip_05_chulazo.mp4', 'Alba Carrillo (pregunta)', 'Fuera de control · La Séptima · 15/11/2026', 0, 5.5, crop=[0.05, 0.05, 0.9, 0.66], lt_at=1.5)
unit(297, [aviso(['INFORMATIVOS TELECINCO · 16/11/2026'], CO + 'clip_35d_horizonte_coherencia.mp4', 12)])
AUD(CO + 'clip_05b_mal_informado.mp4', 'Pedro Sánchez a Carlos Franganillo', 'Informativos Telecinco · 16/11/2026', 0, 2.0, '«A lo mejor usted está mal informado, Carlos»', CO + 'clip_35d_horizonte_coherencia.mp4', 12)
unit(300, [ai('congreso_tribuna_vacia_luz')])

# =====================================================================================
# 10 · ¿QUÉ LE DIRÍA HOY EL PEDRO SÁNCHEZ DE 2018?
# =====================================================================================
FLASH(EX + 'mocion2018_sanchez_dimita.mp4', *DIMITA, 'Pedro Sánchez', 'Moción de censura · Congreso · 31/05/2018', crop=[0.0, 0.08, 0.9, 0.9], tag='dimita')
Q(10, 302, 'Presidente, ¿qué le diría hoy el Pedro Sánchez de 2018?', *F_CONGRESO)
B('tema')
piece(304, [(None, 'Así lo recuerda')],
      [vid('ar_dana_coches__03.mp4', 60), vid('ar_ceuta_espigon__02.mp4', 50, at='Ceuta', blur=18),
       at(bgc(dict(type='recap', title='Ocho años', items=['Ábalos y Koldo García · condenados', 'Santos Cerdán · investigado', 'Zapatero · investigado', 'Begoña Gómez · procesada', 'David Sánchez · condenado (no firme)', 'Fiscal general del Estado · condenado', 'Pedro Sánchez · sin imputación']), *F_CONGRESO), 'exministro')])
piece(305, [(None, 'Quienes le defienden'), ('Quienes le critican', None)], [ai('congreso_tribuna_vacia_luz')])
unit(306, [vid('mocion2018_sanchez_dimita.mp4', 1, base=EX)])
C(EX + 'mocion2018_sanchez_dimita.mp4', 'Pedro Sánchez', 'Moción de censura · Congreso · 31/05/2018 · señal del Congreso vía Cuarto Poder', 16.3, 30.3, lt_at=5.4, crop=[0.0, 0.08, 0.9, 0.9])
unit(308, [ai('congreso_noche')])
C(CO + 'clip_01b_pido_perdon_corrupcion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0, 11.0)
M(4.5, [bgc(dict(type='dijo', left=dict(label='2018', date='31/05/2018', text='«Dimita, señor Rajoy, y todo terminará»'), right=dict(label='2026', date='19/11/2026', text='«Pido perdón… somos gente limpia»', source='Señal del Congreso · RTVE'), red=True), *F_CONGRESO)], track='tema')
unit(311, [bgc(OLD.AVISO['card'], *F_CONGRESO)])
U.append(dict(k='M', track='tema', secs=10, end=True, shots=[bgc(dict(type='list', header='Fuentes principales', items=[
    'Señal del Congreso · RTVE · laSexta · Antena 3 · Telecinco · Cadena SER · La Moncloa',
    'BOE · CGPJ · Tribunal Supremo · Tribunal Constitucional · INE',
    'Maldita.es · El País · El Mundo · elDiario.es · Ara · Voz Pópuli · The Objective · Europa Press',
    'Cortes con su medio y fecha en pantalla · lista completa con enlaces en la descripción']), *F_CONGRESO)]))

# =====================================================================================
# pasada final: ninguna tarjeta sin imagen de fondo; ninguna locución sin plano
# =====================================================================================
def _bg_of(u):
    if u['k'] == 'C' and not u.get('audio_only'):
        return u['src'], float(u['in']) + (float(u.get('out') or u['in'] + 4) - float(u['in'])) * 0.5
    return None
last = F_CONGRESO
for j, u in enumerate(U):
    b = _bg_of(u)
    if b: last = b
    if u['k'] in 'NR' and not u.get('shots'):
        nxt = next((x for x in U[j + 1:j + 3] if x['k'] == 'C'), None)
        if nxt and not nxt.get('audio_only'):
            u['shots'] = [aviso([nxt['lt'][1].replace('RESPUESTA REAL · ', '').split(' · vía')[0].upper()], nxt['src'], float(nxt['in']) + 1.0)]
        else: u['shots'] = [vid(os.path.basename(last[0]), last[1], blur=24, base=os.path.dirname(last[0]) + '/')]
    for s in u.get('shots', []) or []:
        c = s.get('card')
        if c and c.get('type') not in ('doc', 'audiograma', 'pregunta') and not c.get('bgimg'):
            c['bgimg'], c['bgt'] = last

# =====================================================================================
# subtítulos de los cortes: correcciones a la transcripción automática (nombres, cifras, palabras mal oídas)
# =====================================================================================
FIX = {
    'clip_31_no_dormiria.mp4': [['el 95 de', 'el 95 % de']],
    'clip_14_mano_en_el_fuego.mp4': [['mano del fuego', 'mano en el fuego']],
    'clip_06_ire_al_hormiguero.mp4': [['¿Tú vas a ir al hormiguero? ¿Tan invitado, no? Te oiré al hormiguero y a un vega falto.', '¿Tú vas a ir a El Hormiguero, que estás invitado, no? —Iré a El Hormiguero (…)']],
    'co_feijoo_decente__01.mp4': [['Pus de Món', 'Puigdemont']],
    'clip_36c_nogueras_cinico.mp4': [['sínico', 'cínico']],
    'abalos_mocion_vertical.mp4': [['la serie que', 'la sede que']],
    'mocion2018_abalos_decencia.mp4': [['algo inhibida', 'algo inevitable']],
    'clip_18_feijoo_prostibulos.mp4': [['prostímulos', 'prostíbulos']],
    'h16_me_equivoque.mp4': [['Ávalos', 'Ábalos']],
    'clip_15g_caso_flagrante.mp4': [['pertenencias', 'personas']],
    'clip_19d_3_software.mp4': [['sofá', 'software']],
    'clip_25_no_estaba_de_vacaciones.mp4': [['full -time', 'full time']],
    'clip_28b_rey_ceuta_melilla.mp4': [['Zeus y Melilla', 'Ceuta y Melilla']],
    'ul_zapatero_tener_poco__02.mp4': [['darmo', 'dar mucho']],
    'clip_14b_no_hable_con_nadie.mp4': [['Plussul', 'Plus Ultra'], ['No hable', 'No hablé'], ['no hable', 'no hablé']],
    'clip_14c_perifrastica.mp4': [['perifrástrica', 'perifrástica']],
    'ul_nogueras_bloqueada__02.mp4': [['Junz', 'Junts'], ['Feijo', 'Feijóo']],
    'clip_02_millon_viviendas.mp4': [['el 13 son', 'el 13 % son']],
    'clip_05b_mal_informado.mp4': [['Carl.', 'Carlos.']],
    'clip_26d_trump_espana.mp4': [['Spain es un patrón terrible en Nato. No participan, no pagan. No quiero nada hacer con Spain. Cut off all trade with Spain.',
                                   '(Traducción) España es un socio terrible en la OTAN. No participan, no pagan. No quiero tener nada que ver con España. Cortad todo el comercio con España.']],
}
NOSUBS = {'clip_04_baile_sevilla_completo.mp4', 'clip_04b_baile_montero_completo.mp4', 'clip_04z_1_caballe_2018.mp4', 'clip_04z_2_sassoli_2022.mp4',
          'clip_04z_3_vara_2025.mp4', 'clip_04z_4_papa_2026.mp4', 'clip_04c_te_quiero_mitin.mp4'}
for u in U:
    if u['k'] != 'C': continue
    b = os.path.basename(u['src'])
    if b in FIX: u['subs_fix'] = FIX[b]
    if b in NOSUBS: u['subs'] = []
    if b == 'clip_26_aviso_rutinario.mp4': u['out'] = 6.3
    if b == 'clip_22_pues_ya_esta.mp4': u['out'] = 8.4
