# -*- coding: utf-8 -*-
"""PEDRO SÁNCHEZ · LA ENTREVISTA QUE NADIE LE HIZO — montaje v2 (rehecho según la Auditoría 360 del 23-11-2026).

Cambios de fondo respecto a v1:
- Fuera la cita de la moción de 2018 que no era de Sánchez (clip_38 es Ábalos). El espejo final usa solo la frase
  verificada de Sánchez: «¿Está dispuesto a dimitir hoy, aquí, ahora? Dimita, señor Rajoy, y todo terminará» (señal del Congreso, 31/05/2018).
- 7 preguntas, cronología dentro de cada capítulo, cortes de 25 s como máximo, imagen bajo cada audio, nada de negros:
  las tarjetas van sobre imagen (bgimg). Las imágenes de IA llevan «RECREACIÓN».
- Fuera las frases editoriales del narrador, las digresiones (Montero, Trump, Hormiguero, Alba Carrillo, etc.),
  los cortes de youtubers y los particulares (Maricarmen, contrato del ático).
"""
import sys, os, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guion as OLD
O = OLD.U
CO = 'media/e29n90/cortes/'; DE = 'media/e29n90/decl/'; BR = 'media/e29n90/broll/'; CA = 'media/e29n90/capturas/'; HL = 'media/e29n90/hls/'; EX = 'media/e29n90/ext/'
U = []
NQ = 7

def bgc(card, img, t=None):
    """Tarjeta sobre imagen: img puede ser captura, archivo de vídeo (t = segundo) o URL de IA."""
    card = dict(card); card['bgimg'] = img
    if t is not None: card['bgt'] = t
    return dict(card=card)
def reuse(i, shots=None, **kw):
    """Reutiliza la locución ya grabada de la unidad i del guion v1 (mismo texto = mismo audio)."""
    u = copy.deepcopy(O[i]); u.pop('chapter', None)
    if shots is not None: u['shots'] = shots
    u.update(kw); U.append(u)
def N(v, text, shots, **kw): U.append(dict(k='N', voice=v, text=text, shots=shots, **kw))
def R(v, text, shots, **kw): U.append(dict(k='R', voice=v, text=text, shots=shots, **kw))
def C(src, who, where, a, b, **kw):
    u = dict(k='C', src=src, lt=[who, where], fuente='cita', **kw); u['in'] = a; u['out'] = b; U.append(u)
def Q(n, i_old, text, bg, t=None):
    """Pregunta: misma locución de v1 (unidad i_old), tarjeta de máquina de escribir sobre imagen, 4 s."""
    u = copy.deepcopy(O[i_old]); u['secs'] = 4.2
    c = dict(type='pregunta', n=f'PREGUNTA {n:02d} / {NQ:02d}', text=text, foot='PEDRO SÁNCHEZ · LA ENTREVISTA QUE NADIE LE HIZO', bgimg=bg)
    if t is not None: c['bgt'] = t
    u['card'] = c; u['title'] = f'{n}. {text}'; u['chapter'] = True; U.append(u)
def B(track): U.append(dict(k='B', track=track))
def ai(key, at=None):
    s = dict(ai_key=key)
    if at: s['at'] = at
    return s
def vid(f, start, at=None, blur=None, base=BR):
    s = dict(file=base + f, start=start)
    if at: s['at'] = at
    if blur: s['blur'] = blur
    return s
def at(shot, a): s = dict(shot); s['at'] = a; return s
def cap(img, title, lines, source, at_=None, focus=None):
    c = dict(type='doc', image=CA + img, title=title, lines=lines, source=source)
    if focus: c['focus'] = focus
    s = dict(card=c)
    if at_: s['at'] = at_
    return s
def dijo(ld, lt, rd, rt, src, bg, t=None, at_=None):
    s = bgc(dict(type='dijo', left=dict(date=ld, text=lt), right=dict(date=rd, text=rt, source=src), red=True), bg, t)
    if at_: s['at'] = at_
    return s
def aviso(lines, bg, t=None, at_=None, size=46):
    s = bgc(dict(type='aviso', lines=lines, head=True, size=size), bg, t)
    if at_: s['at'] = at_
    return s

# fondos reales que se repiten (fotogramas de los propios cortes)
F_CONGRESO = (EX + 'mocion2018_sanchez_dimita.mp4', 12.0)
F_MONCLOA19 = (DE + 'co_cumplimiento_integro__02.mp4', 4.0)
F_DEBATE26 = (CO + 'clip_01b_pido_perdon_corrupcion.mp4', 3.0)
F_WILD = (CO + 'clip_25_no_estaba_de_vacaciones.mp4', 8.0)
F_ZP = (BR + 'ar_zapatero_audiencia__01.mp4', 6.0)
F_DANA = (BR + 'ar_dana_coches__03.mp4', 40.0)
F_CEUTA = (BR + 'ar_ceuta_visita_pitos__01.mp4', 3.0)

# =====================================================================================
# GANCHO (0:00–0:45): la misma palabra, once años después → pregunta 1
# =====================================================================================
B('tension')
C(CO + 'clip_39b_usted_no_lo_es.mp4', 'Pedro Sánchez a Mariano Rajoy', 'Cara a cara · 14/12/2015 · Academia de TV', 0, 5.6, crop=[0.02, 0.02, 0.86, 0.86])
C(CO + 'clip_39c_feijoo_decente.mp4', 'Alberto Núñez Feijóo a Pedro Sánchez', 'Cara a cara · RTVE · 19/11/2026', 0, 7.0, crop=[0.05, 0.12, 0.88, 0.88])
reuse(3, [aviso(['14/12/2015', '19/11/2026'], *F_DEBATE26, size=60)])
reuse(7, [vid('ar_dana_coches__03.mp4', 40), vid('ar_ceuta_visita_pitos__02.mp4', 6, at='críticos'), at(bgc(dict(type='aviso', lines=['Sus propias palabras.', 'Con su fecha.'], head=True, size=56), *F_DEBATE26), 'propias palabras')])
reuse(8, [bgc(OLD.AVISO['card'], *F_CONGRESO)])
Q(1, 18, 'Presidente, ¿por qué tendríamos que creerle?', *F_MONCLOA19)

# =====================================================================================
# 1 · ¿POR QUÉ TENDRÍAMOS QUE CREERLE?  (2015 → 2026)
# =====================================================================================
B('pulso')
reuse(20, [ai('pamplona_noche'), aviso(['NAVARRA TELEVISIÓN · ABRIL DE 2015'], CO + 'clip_35_bildu_no_vamos_a_pactar.mp4', 4.5, at_='plató')])
C(CO + 'clip_35_bildu_no_vamos_a_pactar.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Navarra Televisión · 2015 · vía El Debate', 1.4, 5.5, lt_at=1.3, crop=[0.0, 0.1, 0.9, 0.9])
reuse(22, [dijo('2015 · NAVARRA TV', '«Con Bildu no vamos a pactar»', '20/05/2020', 'Acuerdo de PSOE, Unidas Podemos y EH Bildu para derogar la reforma laboral', 'Fuente: El País · Maldita.es', *F_CONGRESO)])
reuse(32, [aviso(['ESPEJO PÚBLICO · ANTENA 3 · 17/05/2018'], DE + 'co_rebelion_2018__01.mp4', 20)])
C(DE + 'co_rebelion_2018__01.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · Espejo Público · Antena 3 · 17/05/2018', 15.4, 35.1)
reuse(23, [ai('urnas_repeticion'), aviso(['LASEXTA · 19/09/2019'], CO + 'clip_31_no_dormiria.mp4', 5, at_='laSexta')])
C(CO + 'clip_31_no_dormiria.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · laSexta · 19/09/2019 · vía La Razón', 0, 10.5)
reuse(25, [dijo('19/09/2019', '«No dormiría por la noche»', '12/11/2019', 'Preacuerdo de Gobierno de coalición con Unidas Podemos, 48 horas después de las elecciones', 'Fuente: RTVE', CO + 'clip_31_no_dormiria.mp4', 5)])
reuse(26, [ai('supremo_fachada'), aviso(['14/10/2019 · SENTENCIA DEL PROCÉS'], *F_MONCLOA19, at_='compareció')])
C(DE + 'co_cumplimiento_integro__02.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 14/10/2019', 0, 12, crop=[0.09, 0.0, 0.82, 0.82], lt_at=5.0)
reuse(29, [aviso(['DEBATE ELECTORAL · RTVE · 04/11/2019'], CO + 'clip_32_traerlo_de_vuelta.mp4', 1.5)])
C(CO + 'clip_32_traerlo_de_vuelta.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate electoral · RTVE · 04/11/2019', 0, 3.2, crop=[0.06, 0.0, 0.84, 0.84])
C(DE + 'co_referendum_ilegal__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate electoral · 04/11/2019 · señal RTVE vía Cadena SER', 0, 11.9, crop=[0.15, 0.0, 0.62, 0.62])
reuse(34, [dijo('14/10/2019', '«El acatamiento significa su íntegro cumplimiento»', '22/06/2021', 'El Gobierno indulta a los nueve condenados a prisión por el procés', 'Fuente: BOE · 23/06/2021', *F_MONCLOA19),
           dijo('04/11/2019', '«Un nuevo delito para prohibir los referéndums ilegales»', 'DICIEMBRE DE 2022', 'Se suprime el delito de sedición. El nuevo delito nunca se aprobó', 'Fuente: BOE', CO + 'clip_32_traerlo_de_vuelta.mp4', 1.5, at_='sedición')])
reuse(36, [aviso(['CADENA SER · 28/06/2021'], CO + 'clip_36_indultos_nunca_cambie.mp4', 8)])
C(CO + 'clip_36_indultos_nunca_cambie.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cadena SER · 28/06/2021', 5.8, 19.4)
reuse(35, [aviso(['LA DEFENSA DEL GOBIERNO', 'Los indultos, una apuesta por la concordia.'], CO + 'clip_36_indultos_nunca_cambie.mp4', 12)])
reuse(39, [aviso(['LASEXTA · AL ROJO VIVO · 10/11/2022'], *F_MONCLOA19)])
C(CO + 'clip_33_no_entra_constitucion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · laSexta · 10/11/2022 (audio)', 0, 11.4, audio_only=True,
  quote='Este Gobierno no va a aceptar (…) No entra en la legislación ni en la Constitución española.',
  shots=[bgc(dict(type='quote', text='«No entra en la legislación ni en la Constitución española»', attrib='Pedro Sánchez · Al Rojo Vivo · laSexta · 10/11/2022 · audio'), *F_MONCLOA19)])
reuse(41, [ai('hemiciclo_vacio'), bgc(dict(type='seats', title='Investidura · noviembre de 2023', total=350, groups=[['PSOE y socios', 172], ['Junts', 7], ['Resto', 171]]), *F_CONGRESO)])
C(CO + 'clip_34b_necesidad_virtud_wild.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 0, 11.0)
U.append(dict(k='M', track='pulso', secs=3.2, shots=[aviso(['DIECIOCHO DÍAS DESPUÉS', 'DEBATE DE INVESTIDURA · 15/11/2023'], *F_CONGRESO)]))
C(CO + 'clip_33b_acorde_constitucion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate de investidura · Congreso · 15/11/2023 (audio)', 0, 5.9, audio_only=True,
  quote='La amnistía que planteamos es perfectamente legal. Es acorde con la Constitución.',
  shots=[bgc(dict(type='quote', text='«La amnistía que planteamos es perfectamente legal. Es acorde con la Constitución»', attrib='Pedro Sánchez · Congreso · 15/11/2023 · audio'), *F_CONGRESO)])
reuse(43, [cap('doc_33_BOE_STC_137-2025_amnistia_31-07-2025.jpg', 'STC 137/2025', ['La Constitución no prohíbe la amnistía', 'Inconstitucionalidad parcial · votos particulares'], 'BOE · 31/07/2025')])
N('TOP', 'Junts votó la investidura. Y dos años después, en octubre de dos mil veinticinco, rompió con el Gobierno.',
  [aviso(['PERPIÑÁN · OCTUBRE DE 2025'], DE + 'ul_puigdemont_perpinan__02.mp4', 95)])
C(DE + 'ul_puigdemont_perpinan__02.mp4', 'Carles Puigdemont (Junts)', 'Perpiñán · 27/10/2025 · vía Cadena SER', 88.3, 112.3)
N('NEW', 'Este mes, en plena campaña, el propio Puigdemont lo resumió con una frase que publicó El Mundo: «Nos hemos aprovechado de la ambición de Sánchez para derrotar a España».',
  [bgc(dict(type='quote', text='«Nos hemos aprovechado de la ambición de Sánchez para derrotar a España»', attrib='Carles Puigdemont · según El Mundo · noviembre de 2026'), DE + 'ul_puigdemont_perpinan__02.mp4', 100)])
reuse(49, [aviso(['THE WILD PROJECT · 13/11/2026'], *F_WILD)])
C(CO + 'clip_35c_derecho_a_cambiar_de_opinion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 26.6, 36.0)
reuse(58, [aviso(['CONGRESO DE LOS DIPUTADOS · 12/11/2025'], CO + 'clip_36c_nogueras_cinico.mp4', 6)])
C(CO + 'clip_36c_nogueras_cinico.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados · 12/11/2025 · vía OKDiario', 0, 18.3, crop=[0.12, 0.0, 0.76, 0.76])
reuse(61, [cap('doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', 'TRIBUNAL SUPREMO', ['22/06/2026'], 'CGPJ', at_='condenado')] + [ai('congreso_noche')])

# =====================================================================================
# 2 · ¿QUIÉN ELIGIÓ A JOSÉ LUIS ÁBALOS?  (Ábalos y Ferraz, 2016 → 2026)
# =====================================================================================
Q(2, 63, 'Presidente, ¿quién eligió a José Luis Ábalos?', *F_CONGRESO)
B('noche')
reuse(69, [ai('carretera_noche'), ai('coche_lluvia', at='Peugeot'),
           at(bgc(dict(type='board', title='El Peugeot · 2016', nodes=[['Pedro Sánchez', 'candidato'], ['José Luis Ábalos', 'condenado'], ['Santos Cerdán', 'investigado'], ['Koldo García', 'condenado']], links=[[0, 1], [0, 2], [0, 3], [1, 3]], center=True), *F_CONGRESO), 'cuatro hombres')])
reuse(70, [cap('doc_cierre_Abalos_secretario_Organizacion_EFE_18-06-2017.jpg', 'EFE · 18/06/2017', ['Sánchez elige a Ábalos para Organización'], 'Valencia Plaza (EFE)'),
           cap('doc_cierre_Abalos_Cerdan_area_Organizacion_EFE_18-06-2017.jpg', 'EL ÁREA DE ORGANIZACIÓN', ['Ábalos, con Cerdán dentro'], 'Valencia Plaza (EFE)', at_='Santos Cerdán')])
N('TOP', '[serious] Un año después, el treinta y uno de mayo de dos mil dieciocho, Sánchez defiende en el Congreso la moción de censura contra Mariano Rajoy, tras la sentencia del caso Gürtel.',
  [vid('mocion2018_sanchez_dimita.mp4', 1, base=EX), aviso(['MOCIÓN DE CENSURA · CONGRESO · 31/05/2018'], EX + 'mocion2018_abalos_decencia.mp4', 3, at_='tribuna')])
C(EX + 'mocion2018_abalos_decencia.mp4', 'José Luis Ábalos (PSOE)', 'Moción de censura · Congreso · 31/05/2018 · vía El Debate', 2.6, 23.8, crop=[0.0, 0.1, 0.9, 0.9])
reuse(75, [aviso(['JOSÉ LUIS ÁBALOS', 'Secretario de Organización del PSOE · 2018'], EX + 'mocion2018_abalos_decencia.mp4', 6), at(aviso(['MARIANO RAJOY'], EX + 'mocion2018_sanchez_dimita.mp4', 17), 'Rajoy')])
C(CO + 'clip_39_rajoy_lecciones.mp4', 'Mariano Rajoy', 'Moción de censura · Congreso · 31/05/2018 · vía El Debate', 0, 8.0, crop=[0.0, 0.1, 0.9, 0.9])
U.append(dict(k='M', track='noche', secs=3.4, shots=[aviso(['Y EL CANDIDATO, PEDRO SÁNCHEZ,', 'LE HIZO UNA PREGUNTA'], EX + 'mocion2018_sanchez_dimita.mp4', 12)]))
C(EX + 'mocion2018_sanchez_dimita.mp4', 'Pedro Sánchez', 'Moción de censura · Congreso · 31/05/2018 · señal del Congreso vía Cuarto Poder', 5.8, 30.3, lt_at=6.0, crop=[0.0, 0.08, 0.9, 0.9])
reuse(77)
reuse(78, [ai('pista_aeropuerto_noche'), cap('doc_13_maldita_versiones_Delcy_11-10-2024.jpg', 'LAS VERSIONES DE BARAJAS', ['Las versiones de Ábalos y del Gobierno'], 'Maldita.es · 11/10/2024', at_='Maldita'),
           cap('doc_13_Exteriores_desmiente_llamada_Delcy_06-02-2020.jpg', 'COMUNICADO', ['«Es absolutamente falso»'], 'Secretaría de Estado de Comunicación · 06/02/2020', at_='negó')])
reuse(84, [cap('doc_cierre_Cerdan_sustituye_Abalos_Mallorcadiario_13-07-2021.jpg', 'JULIO DE 2021', ['Cerdán sustituye a Ábalos'], 'Mallorcadiario · 13/07/2021'),
           aviso(['23J · 2023', 'Número 2 de la lista del PSOE por Valencia: José Luis Ábalos'], *F_CONGRESO, at_='número dos')])
reuse(94, [ai('expediente_mesa'), aviso(['FEBRERO DE 2024', 'Detención de Koldo García · contratos de mascarillas'], *F_CONGRESO, at_='Koldo García')])
reuse(101, [aviso(['LO QUE DIJO · CONGRESO · 28/02/2024'], CO + 'clip_41b_no_tapa.mp4', 2)])
C(CO + 'clip_41b_no_tapa.mp4', 'Habla Pedro Sánchez', 'RESPUESTA REAL · Congreso · 28/02/2024', 0.8, 3.6)
reuse(95, [cap('doc_03b_cerdan_auto_indicios_CGPJ_12-06-2025.jpg', 'AUTO DEL TRIBUNAL SUPREMO', ['«Consistentes indicios» contra Santos Cerdán'], 'CGPJ · 12/06/2025'),
           at(bgc(dict(type='ficha', name='Santos Cerdán', role='Exsecretario de Organización · INVESTIGADO · presunción de inocencia'), *F_CONGRESO), 'Cerdán dimite')])
reuse(104, [aviso(['CONGRESO · 18/06/2025'], CO + 'clip_15e_corrupcion_cero.mp4', 3)])
C(CO + 'clip_15e_corrupcion_cero.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 18/06/2025', 0, 7.7, lt_at=5.4)
reuse(85, [aviso(['LA DEFENSA DEL PSOE', 'Apartó y expulsó a Ábalos. Colabora con la justicia.'], HL + 'h16_me_equivoque.mp4', 10)])
C(HL + 'h16_me_equivoque.mp4', 'Habla Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/07/2025 · La Moncloa', 16.3, 20.95)
C(HL + 'h17_politico_limpio.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/07/2025 · La Moncloa', 9.0, 29.5)
reuse(96, [aviso(['VÍCTOR DE ALDAMA', 'Empresario · confesó · condenado'], *F_CONGRESO),
           at(aviso(['LA FOTO · FEBRERO DE 2019', 'Publicada por El Mundo · octubre de 2024'], *F_CONGRESO), 'El Mundo'),
           at(aviso(['LA DEFENSA', 'Sánchez niega haberle pedido la foto.'], *F_CONGRESO), 'Sánchez lo niega')])
reuse(97, [bgc(dict(type='counter', **{'from': 2}, to=39, label='reuniones localizadas por los investigadores, según Voz Pópuli'), *F_CONGRESO)])
reuse(93, [ai('ferraz_fachada_dia'), aviso(['27/05/2026 · FERRAZ, 70', 'Requerimiento de la UCO · 12 horas'], *F_CONGRESO, at_='doce horas')])
reuse(65, [cap('doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', 'NOTA DEL TRIBUNAL SUPREMO', ['Ábalos · 24 años y 3 meses', 'Koldo García · 19 años y 8 meses'], 'CGPJ · 22/06/2026')])
reuse(66, [bgc(dict(type='quote', text='«corrupción orgánica, organizada y continuada»', attrib='STS 418/2026 · al valorar la confesión de Aldama'), CA + 'doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg')])
reuse(67, [aviso(['LA DEFENSA', 'El abogado de Ábalos recurrirá. Pedro Sánchez no está imputado en ninguna causa.'], *F_CONGRESO)])
reuse(106, [aviso(['CONGRESO · 24/06/2026'], CO + 'clip_15g_caso_flagrante.mp4', 2)])
C(CO + 'clip_15g_caso_flagrante.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 24/06/2026', 0, 5.0)
C(HL + 'h15f_no_financiado.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 24/06/2026 · La Moncloa', 43.3, 55.2)
reuse(111,
  [aviso(['LO QUE DICE EL PSOE', '«El PSOE no se ha financiado irregularmente»'], HL + 'h15f_no_financiado.mp4', 48),
   at(aviso(['FISCALÍA ANTICORRUPCIÓN · OCTUBRE DE 2026', 'Indicios, pero «prematuro» imputar al partido · según Ara'], *F_CONGRESO), 'Fiscalía')])
N('TOP', 'Porque las causas no se quedaron en la sede del partido. [pause] Llegaron a su casa.', [ai('pasillo_vacio')])

# =====================================================================================
# 3 · ¿POR QUÉ SU FAMILIA ESTÁ EN LOS TRIBUNALES?  (2019 → 2025 / 2024 → 2026)
# =====================================================================================
Q(3, 117, 'Presidente, ¿por qué su familia está en los tribunales?', CO + 'clip_19a_senoras_de.mp4', 3)
B('tension')
reuse(119, [ai('carta_escritorio'), at(bgc(dict(type='quote', text='¿Merece la pena todo esto? Sinceramente, no lo sé.', attrib='Carta a la ciudadanía · 24/04/2024'), *F_MONCLOA19), 'Merece')])
reuse(120, [ai('atriles')])
reuse(121, [bgc(dict(type='quote', text='«Aquí no hay caso, hay fango.»', attrib='Pedro Sánchez · laSexta · 17/05/2024'), *F_MONCLOA19)])
reuse(122, [ai('expediente_mesa'), bgc(dict(type='list', header='Lo investigado', items=['Tráfico de influencias', 'Corrupción en los negocios', 'Apropiación indebida', 'Intrusismo']), CO + 'clip_19c_derecho_no_responder.mp4', 4)])
reuse(123, [ai('sala_comision_vacia'), aviso(['ASAMBLEA DE MADRID · 13/11/2024'], CO + 'clip_19d_1_vinculacion.mp4', 5, at_='Asamblea')])
C(CO + 'clip_19d_1_vinculacion.mp4', 'Mercedes Zarzalejo (PP)', 'Asamblea de Madrid · 13/11/2024 · vía Vozpópuli', 3.0, 14.7, crop=[0.0, 0.1, 0.88, 0.88])
C(CO + 'clip_19c_derecho_no_responder.mp4', 'Begoña Gómez', 'Asamblea de Madrid · 13/11/2024 · vía Vozpópuli', 0, 14.3, crop=[0.0, 0.1, 0.88, 0.88])
reuse(128, [bgc(dict(type='ficha', name='Begoña Gómez', role='Esposa del presidente · PROCESADA · juicio con jurado previsto en 2027'), CO + 'clip_19c_derecho_no_responder.mp4', 6),
            at(aviso(['LA DEFENSA', 'La Fiscalía pide la absolución. Begoña Gómez denuncia una persecución.'], CO + 'clip_19c_derecho_no_responder.mp4', 6), 'defensa')])
reuse(133, [bgc(dict(type='ficha', name='David Sánchez', role='Hermano del presidente · CONDENADO en primera instancia · recurrida'), *F_MONCLOA19)])
reuse(136, [aviso(['TVE · 01/09/2025'], CO + 'clip_23_jueces_minoria.mp4', 12)])
C(CO + 'clip_23_jueces_minoria.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · TVE · 01/09/2025', 0, 19.3, lt_at=1.2)
reuse(139, [aviso(['TRES ASOCIACIONES DE JUECES RESPONDEN'], CO + 'clip_23_jueces_minoria.mp4', 12),
            at(aviso(['RNE · 06/11/2019'], *F_MONCLOA19, size=50), 'Radio Nacional')])
C(CO + 'clip_22_pues_ya_esta.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · RNE · 06/11/2019 (audio)', 0, 9.8, audio_only=True, quote='¿La Fiscalía de quién depende? (…) Pues ya está.',
  shots=[bgc(dict(type='quote', text='«¿La Fiscalía de quién depende?… Pues ya está»', attrib='Pedro Sánchez · RNE · 06/11/2019 · audio'), *F_MONCLOA19)])
N('TOP', 'Al día siguiente rectificó: dijo que no había sido preciso. [pause]', [aviso(['07/11/2019', '«No fui preciso»'], *F_MONCLOA19)])
reuse(141, [ai('supremo_fachada')])
N('TOP', 'Seis años después, el veinte de noviembre de dos mil veinticinco, el Tribunal Supremo condenó al fiscal general del Estado a dos años de inhabilitación y a una multa por revelación de datos reservados. Hubo votos particulares. Y el tribunal no dio por acreditado que el presidente le diera ninguna orden.',
  [aviso(['TRIBUNAL SUPREMO · 20/11/2025', 'Fiscal general del Estado: dos años de inhabilitación y multa'], *F_CONGRESO),
   at(aviso(['Votos particulares', 'No consta ninguna orden del presidente'], *F_CONGRESO), 'votos particulares')])
reuse(143, [aviso(['G20 · JOHANNESBURGO · 23/11/2025'], CO + 'clip_21_creo_inocencia_fiscal.mp4', 2)])
C(CO + 'clip_21_creo_inocencia_fiscal.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · G20 Johannesburgo · 23/11/2025 · vía ABC', 0.4, 5.4, crop=[0.0, 0.1, 0.9, 0.9])
reuse(145, [ai('playa_noche_generica')])

# =====================================================================================
# 4 · ¿DÓNDE ESTABA USTED?  (DANA 2024 → Ceuta 2026)
# =====================================================================================
Q(4, 149, 'Presidente, ¿dónde estaba usted?', *F_DANA)
B('noche')
N('TOP', 'Veintinueve de octubre de dos mil veinticuatro. Valencia. La DANA. Doscientos treinta muertos en tres comunidades, según el balance oficial de La Moncloa de diciembre.',
  [vid('ar_dana_coches__03.mp4', 40), vid('ar_dana_poyo__02.mp4', 6, at='Doscientos treinta')])
reuse(171, [bgc(dict(type='quote', text='«El Gobierno central está listo para ayudar. Si necesita más recursos, que los pida.»', attrib='Pedro Sánchez · La Moncloa · 02/11/2024'), *F_DANA)])
reuse(172, [aviso(['10.000 EFECTIVOS MÁS', 'Anunciados en la misma comparecencia'], *F_DANA),
            at(aviso(['LEY 17/2015', 'Emergencia de interés nacional: a iniciativa propia. No se declaró.'], *F_DANA), 'la ley'),
            at(aviso(['LA DEFENSA', 'Era una facultad, no una obligación. La competencia era de la Generalitat.'], *F_DANA), 'defensa')])
N('NEW', 'La Generalitat Valenciana, gobernada por el Partido Popular, también tuvo que responder por aquel día. La alerta a los móviles llegó cuando muchos pueblos ya estaban inundados. Un año después, el tres de noviembre de dos mil veinticinco, el presidente valenciano, Carlos Mazón, dimitió reconociendo errores propios.',
  [vid('ar_dana_poyo__02.mp4', 20), at(aviso(['03/11/2025', 'Dimite Carlos Mazón, presidente de la Generalitat'], *F_DANA), 'Mazón')])
reuse(174, [vid('ar_paiporta_coche__01.mp4', 3), vid('ar_paiporta_salida__01.mp4', 8, at='Sánchez se va'), vid('ar_paiporta_reyes__03.mp4', 6, at='Los Reyes')])
N('NEW', 'El Gobierno atribuyó la agresión a grupos ultras organizados, y defendió que la seguridad aconsejaba sacar al presidente. [pause]',
  [aviso(['LA DEFENSA', 'Grupos ultras organizados. La seguridad aconsejaba salir.'], BR + 'ar_paiporta_salida__01.mp4', 8)])
U.append(dict(k='M', track='noche', secs=3.4, shots=[aviso(['VERANO DE 2026', 'CEUTA'], BR + 'ar_ceuta_espigon__02.mp4', 12, size=56)]))
reuse(151, [cap('doc_26_ceuta_whatsapp_CNI_Moncloa_29-07-2026.jpg', 'CNI · 29/07/2026 · 13:52', ['«Llamamiento para asalto por valla y mar mañana a las 20h»'], 'Documento publicado por La Moncloa · 09/09/2026')])
reuse(152, [vid('ar_ceuta_espigon__02.mp4', 5, blur=16), vid('ar_ceuta_espigon__02.mp4', 40, at='espigón', blur=16),
            at(bgc(dict(type='counter', to=72000, label='entradas en Ceuta, según Maldita.es y elDiario.es'), BR + 'ar_ceuta_espigon__02.mp4', 20), 'setenta y dos mil'),
            at(bgc(dict(type='counter', to=72, label='muertos como mínimo, según la Delegación del Gobierno'), BR + 'ar_ceuta_espigon__02.mp4', 30), 'setenta y dos muertos')])
reuse(153, [vid('ar_ceuta_visita_pitos__01.mp4', 3), vid('ar_ceuta_visita_pitos__02.mp4', 6, at='pitos')])
reuse(154, [vid('ar_mareta_llegada__02.mp4', 4), aviso(['LA MARETA · LANZAROTE · AGOSTO DE 2026'], BR + 'ar_mareta_llegada__02.mp4', 4, at_='La Mareta')])
C(CO + 'clip_24a_playlist.mp4', 'Pedro Sánchez', 'Vídeo publicado en sus redes sociales · 01/08/2026 · vía ESdiario', 0, 6.0, crop=[0.335, 0.0, 0.33, 1.0], fit=True)
C(CO + 'clip_24b_feliz_verano.mp4', 'Pedro Sánchez', 'Vídeo publicado en sus redes sociales · 01/08/2026 · vía ESdiario', 0, 4.8, crop=[0.335, 0.0, 0.33, 1.0], fit=True)
reuse(157, [bgc(dict(type='counter', to=25, label='días hasta la reunión del Consejo de Seguridad Nacional'), *F_CEUTA),
            at(aviso(['CONGRESO · 03/09/2026'], CO + 'clip_26_aviso_rutinario.mp4', 2), 'tres de septiembre')])
C(CO + 'clip_26_aviso_rutinario.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 03/09/2026', 0, 5.4)
reuse(160, [cap('doc_26_ceuta_cabecera_Moncloa_09-09-2026.jpg', 'LOS INFORMES DESCLASIFICADOS', ['Publicados por La Moncloa'], 'La Moncloa · 09/09/2026'),
            cap('doc_26_ceuta_whatsapp_CNI_Moncloa_29-07-2026.jpg', 'CNI · 29/07/2026', ['«asalto por valla y mar mañana las 20h»'], 'La Moncloa', at_='Asalto')])
reuse(161, [aviso(['LA DEFENSA DEL GOBIERNO', 'Ningún informe previó la escala ni la probabilidad de lo ocurrido.'], *F_WILD)])
C(DE + 'ul_manyaneros_chantaje__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Mañaneros 360 · TVE · 09/09/2026 · vía El País', 8.4, 13.75)
C(CO + 'clip_25_no_estaba_de_vacaciones.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 3.5, 15.7, lt_at=1.2)
reuse(164, [aviso(['CONGRESO · 16/09/2026'], CO + 'clip_25c_eso_a_vivas.mp4', 3)])
C(CO + 'clip_25c_eso_a_vivas.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · Congreso · 16/09/2026 · vía Europa Press', 0.6, 5.8)
U.append(dict(k='M', track='noche', secs=3.4, shots=[aviso(['JUAN JESÚS VIVAS', 'Presidente de la ciudad autónoma de Ceuta (PP)'], *F_CEUTA)]))
N('TOP', 'Y en enero de dos mil veintiséis, llegó la tragedia que tocaría a su propio Gobierno. [short pause] Sobre raíles.', [ai('carretera_noche')])

# =====================================================================================
# 5 · ¿QUIÉN RESPONDE POR LAS VÍAS?  (enero → noviembre de 2026)
# =====================================================================================
Q(5, 185, 'Presidente, ¿quién responde por las vías?', CO + 'clip_10d2_renuncio_listas.mp4', 8)
B('tension')
reuse(187, [ai('vias_recta_amanecer'), at(bgc(dict(type='ficha', name='Óscar Puente', role='Ministro de Transportes (2023-2026)'), CO + 'clip_10d2_renuncio_listas.mp4', 8), 'Óscar Puente')])
C(CO + 'clip_08_tremendamente_extrano.mp4', 'Óscar Puente', 'Ministro de Transportes · 18/01/2026 · vía El Debate', 0, 4.9, crop=[0.0, 0.1, 0.9, 0.9])
C(CO + 'clip_10b2_bajisima.mp4', 'Óscar Puente', 'Ministro de Transportes · enero de 2026', 0, 9.9)
reuse(190, [bgc(dict(type='quote', text='«Si hay algo cercano a la infalibilidad, es la alta velocidad española.»', attrib='Óscar Puente · 20/01/2026'), CO + 'clip_10b2_bajisima.mp4', 4)])
N('TOP', '[serious] Muy baja. Bajísima. [pause] Veintiocho de octubre de dos mil veintiséis. Urda, Toledo. Otro accidente ferroviario. Sesenta y nueve muertos, según la información publicada. Ese día el presidente viaja a Urda.',
  [ai('vias_recta_amanecer'), at(aviso(['URDA (TOLEDO) · 28/10/2026', '69 muertos, según la información publicada'], HL + 'h10_urda.mp4', 220), 'Urda, Toledo')])
C(HL + 'h10_urda.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Urda (Toledo) · 28/10/2026 · La Moncloa', 211.0, 233.2)
reuse(193, [aviso(['DIPUTACIÓN PERMANENTE · 03/11/2026'], CO + 'clip_10d2_renuncio_listas.mp4', 8)])
C(CO + 'clip_10d2_renuncio_listas.mp4', 'Óscar Puente', 'Congreso · Diputación Permanente · 03/11/2026 · vía AS TV', 6.7, 15.9, crop=[0.0, 0.0, 0.86, 0.86])
reuse(197)
reuse(198, [ai('catedral_interior_velas'), at(aviso(['LA DEFENSA', 'Fuentes de La Moncloa: no acostumbra a asistir a ceremonias religiosas.'], *F_MONCLOA19), 'Fuentes')])
reuse(199, [aviso(['ARCHIVO'], CO + 'clip_04z_2_sassoli_2022.mp4', 1, size=60)])
C(CO + 'clip_04z_1_caballe_2018.mp4', 'Funeral de Montserrat Caballé', 'Barcelona · 08/10/2018 · Antena 3', 0, 1.6, crop=[0.1, 0.0, 0.82, 0.82])
C(CO + 'clip_04z_2_sassoli_2022.mp4', 'Funeral de Estado de David Sassoli', 'Roma · 14/01/2022 · La Moncloa', 0, 1.6)
C(CO + 'clip_04z_3_vara_2025.mp4', 'Funeral de Guillermo Fernández Vara', 'Olivenza · 06/10/2025 · El Mundo', 0, 1.6, crop=[0.15, 0.0, 0.82, 0.82])
C(CO + 'clip_04z_4_papa_2026.mp4', 'Misa de León XIV', 'Sagrada Familia · 10/06/2026 · La Moncloa', 0, 1.6)
reuse(204, [aviso(['SEVILLA · 12/11/2026'], CO + 'clip_04c_te_quiero_mitin.mp4', 1.5, size=50)])
C(CO + 'clip_04c_te_quiero_mitin.mp4', 'Mitin del PSOE', 'Sevilla · 12/11/2026 · vía El País', 0, 3.0, crop=[0.0, 0.1, 0.9, 0.9])
reuse(208, [aviso(['CARA A CARA · RTVE · 19/11/2026'], CO + 'clip_01c_feijoo_perdon_toledo.mp4', 3)])
C(CO + 'clip_01c_feijoo_perdon_toledo.mp4', 'Alberto Núñez Feijóo', 'Cara a cara · RTVE · 19/11/2026', 0, 12.3)
reuse(210, [aviso(['LA DEFENSA', 'En el debate, Sánchez pidió perdón a las familias de las víctimas.'], *F_DEBATE26), at(ai('congreso_noche'), 'Su mentor')])

# =====================================================================================
# 6 · ¿POR QUÉ SIGUE DEFENDIENDO A ZAPATERO?  (2021 → 2026)
# =====================================================================================
Q(6, 212, 'Presidente, ¿por qué sigue defendiendo a José Luis Rodríguez Zapatero?', *F_ZP)
B('pulso')
reuse(218, [cap('doc_08_plusultra_moncloa_09-03-2021_cabecera.jpg', 'CONSEJO DE MINISTROS · 09/03/2021', ['Rescate de 53 millones a Plus Ultra'], 'La Moncloa'), cap('doc_08_plusultra_moncloa_09-03-2021_texto.jpg', 'LA MONCLOA · 09/03/2021', ['Nota del Consejo de Ministros'], 'La Moncloa', at_='anunció')])
reuse(214, [vid('ar_zapatero_joyas__02.mp4', 4), cap('doc_14_joyas_Zapatero_TheObjective_11-06-2026.jpg', 'LAS JOYAS', ['Fotos de las joyas, en las bolsas de la Policía'], 'The Objective · 11/06/2026', at_='The Objective'),
            vid('ar_zapatero_joyas__03.mp4', 6, at='bolsas')])
reuse(215, [bgc(dict(type='ficha', name='José Luis Rodríguez Zapatero', role='Expresidente del Gobierno · INVESTIGADO · presunción de inocencia'), *F_ZP),
            vid('ar_zapatero_audiencia__01.mp4', 6, at='nulidad')])
reuse(224, [vid('ar_zapatero_audiencia__01.mp4', 12)])
C(DE + 'ar_sanchez_apoyo_zp__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Bruselas · 18/06/2026 · vía Libertad Digital', 25.2, 45.3, crop=[0.08, 0.06, 0.88, 0.88])
reuse(226, [cap('doc_08_plusultra_moncloa_09-03-2021_texto.jpg', 'LA DEFENSA', ['Un préstamo, no un rescate', '60.000 empleos salvados, según el Gobierno'], 'La Moncloa')])
reuse(219, [aviso(['MAÑANEROS 360 · TVE · 23/07/2026'], CO + 'clip_14b_no_hable_con_nadie.mp4', 4)])
C(CO + 'clip_14b_no_hable_con_nadie.mp4', 'José Luis Rodríguez Zapatero', 'Entrevista · Mañaneros 360 · TVE · 23/07/2026', 0, 12.8, crop=[0.2, 0.0, 0.62, 0.62])
reuse(228, [aviso(['TVE · 09/09/2026'], CO + 'clip_14a_contar_con_jose_luis.mp4', 3)])
C(CO + 'clip_14a_contar_con_jose_luis.mp4', 'Pedro Sánchez (con la pregunta)', 'RESPUESTA REAL · TVE · 09/09/2026', 0, 7.9)
reuse(230, [aviso(['THE WILD PROJECT · 13/11/2026'], *F_WILD)])
C(CO + 'clip_14_mano_en_el_fuego.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 3.7, 12.8, lt_at=0.8)
U.append(dict(k='M', track='tema', secs=3.4, shots=[bgc(dict(type='aviso', lines=['La última pregunta.', 'Qué se prometió. Y qué se cumplió.'], head=True, size=52), CO + 'clip_02_millon_viviendas.mp4', 4)]))

# =====================================================================================
# 7 · ¿QUÉ LE DIRÍA HOY EL PEDRO SÁNCHEZ DE 2018?
# =====================================================================================
Q(7, 302, 'Presidente, ¿qué le diría hoy el Pedro Sánchez de 2018?', *F_CONGRESO)
B('tema')
reuse(244, [ai('constitucion_libro'), at(bgc(dict(type='timeline', header='Presupuestos', events=[['2023', 'Últimos aprobados'], ['2024', 'Prorrogados'], ['2025', 'Prorrogados'], ['2026', 'Prorrogados']]), *F_CONGRESO), 'prorrogados')])
reuse(245,
  [aviso(['LA DEFENSA', 'Artículo 134.4: la prórroga es constitucional.'], *F_CONGRESO),
   at(bgc(dict(type='quote', text='«con o sin un concurso de un poder legislativo»', attrib='Pedro Sánchez · Comité Federal del PSOE · septiembre de 2024 · según The Objective'), *F_CONGRESO), 'Comité Federal')])
reuse(279, [aviso(['LA MONCLOA · 16/05/2024'], CO + 'clip_37c_cohete.mp4', 4)])
C(CO + 'clip_37c_cohete.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Foro de fondos europeos · 16/05/2024 · vía Libertad Digital', 1.9, 7.1, crop=[0.12, 0.1, 0.85, 0.85])
reuse(281, [bgc(dict(type='counter', to=22460000, label='ocupados · INE · 2025'), CO + 'clip_37c_cohete.mp4', 4),
            at(aviso(['LA DEFENSA', 'PIB +2,6 % en 2025 · más de 22 millones de ocupados (INE)'], CO + 'clip_37c_cohete.mp4', 4), 'defensa')])
reuse(283, [aviso(['CARA A CARA · RTVE · 19/11/2026'], CO + 'clip_02_millon_viviendas.mp4', 4)])
C(CO + 'clip_02_millon_viviendas.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0.5, 10.5)
reuse(285, [dijo('19/11/2026', '«Hemos construido un millón de viviendas»', 'DATOS', 'Unas 705.000 viviendas terminadas (752.000 contando 2018)', 'Fuente: Idealista vía Artículo14 · Maldita.es', CO + 'clip_02_millon_viviendas.mp4', 4)])
reuse(286, [aviso(['TAMBIÉN', 'Feijóo negó su promesa del millón de viviendas (medida 144 de su programa).'], CO + 'clip_39c_feijoo_decente.mp4', 3)])
reuse(304,
  [vid('ar_dana_coches__03.mp4', 60), vid('ar_ceuta_espigon__02.mp4', 50, at='Ceuta', blur=16),
   at(bgc(dict(type='recap', title='Ocho años', items=['Ábalos y Koldo García · condenados', 'Santos Cerdán (sucesor de Ábalos) · investigado', 'Zapatero · investigado', 'Begoña Gómez · procesada', 'David Sánchez · condenado (no firme)', 'Fiscal general del Estado · condenado', 'Pedro Sánchez · sin imputación']), *F_CONGRESO), 'exministro')])
reuse(305, [ai('congreso_tribuna_vacia_luz')])
reuse(306,
  [vid('mocion2018_sanchez_dimita.mp4', 1, base=EX)])
C(EX + 'mocion2018_sanchez_dimita.mp4', 'Pedro Sánchez', 'Moción de censura · Congreso · 31/05/2018 · señal del Congreso vía Cuarto Poder', 16.3, 30.3, lt_at=5.4, crop=[0.0, 0.08, 0.9, 0.9])
reuse(308, [ai('congreso_noche')])
C(CO + 'clip_01b_pido_perdon_corrupcion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0, 11.0)
reuse(311, [bgc(OLD.AVISO['card'], *F_CONGRESO)])
U.append(dict(k='M', track='tema', secs=10, end=True, shots=[bgc(dict(type='list', header='Fuentes principales', items=[
    'Señal del Congreso · RTVE · laSexta · Antena 3 · Cadena SER · La Moncloa',
    'BOE · CGPJ · Tribunal Supremo · Tribunal Constitucional · INE',
    'Maldita.es · El País · El Mundo · elDiario.es · Ara · Voz Pópuli · The Objective · Europa Press',
    'Lista completa, con enlaces, en la descripción']), *F_CONGRESO)]))
