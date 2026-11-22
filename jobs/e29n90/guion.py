# -*- coding: utf-8 -*-
"""PEDRO SÁNCHEZ · LA ENTREVISTA QUE NADIE LE HIZO
DocuVox · Especial Elecciones 29N · guion nuevo (22-11-2026), escrito desde cero.

Formato: diez preguntas. Las preguntas son de DocuVox; las respuestas, cortes reales de Pedro Sánchez con su fecha.
Después de cada respuesta, los hechos (con su fuente en pantalla) y la defensa del aludido.
Voces: TOP (Narrador Top) y NEW (Narrador New) se alternan por bloques; ENT (entrevistadora) solo pregunta; DOC lee documentos.
Ningún político con voz sintética: todo lo que dicen los protagonistas es su voz real de archivo.
"""
V = dict(TOP='EtnizbrIk2nKCZCt0zqW', NEW='gcDsmGjWArnZhxIfcR7d', ENT='BXtvkfRgOYGPQKVRgufE', DOC='nMvZRihyU408YNgNXHuX')
CO = 'media/e29n90/cortes/'; DE = 'media/e29n90/decl/'; BR = 'media/e29n90/broll/'; CA = 'media/e29n90/capturas/'
U = []

def N(v, text, shots=None, **kw): U.append(dict(k='N', voice=v, text=text, shots=shots or [], **kw))
def R(v, text, shots=None, **kw): U.append(dict(k='R', voice=v, text=text, shots=shots or [], **kw))
def C(clip, who, src, a=None, b=None, audio_only=False, quote='', base=CO, **kw):
    u = dict(k='C', src=base + clip, lt=[who, src], fuente='cita', **kw)
    u['in'] = a if a is not None else 0
    if b is not None: u['out'] = b
    if audio_only: u.update(audio_only=True, quote=quote)
    U.append(u)
def Q(n, text, say=None):
    U.append(dict(k='T', voice='ENT', text=say or text, secs=6.5, voice_at=0.6, sting='golpe', chapter=True,
                  card=dict(type='pregunta', n=f'PREGUNTA {n:02d} / 10', text=text, foot='LA ENTREVISTA QUE NADIE LE HIZO'), title=f'{n}. {text}'))
def M(track, secs, shots=None): U.append(dict(k='M', track=track, secs=secs, shots=shots or []))
def B(track): U.append(dict(k='B', track=track))
def card(**c): return dict(card=c)
def dijo(ld, lt, rd, rt, src='', red=True, at=None):
    s = dict(card=dict(type='dijo', left=dict(date=ld, text=lt), right=dict(date=rd, text=rt, source=src), red=red))
    if at: s['at'] = at
    return s
def doc(img, title, lines, source, at=None, focus=None):
    c = dict(type='doc', image=CA + img, title=title, lines=lines, source=source)
    if focus: c['focus'] = focus
    s = dict(card=c)
    if at: s['at'] = at
    return s
def vid(f, start, at=None, lt=None):
    s = dict(file=BR + f, start=start)
    if at: s['at'] = at
    if lt: s['lt'] = lt
    return s
def ai(key, at=None):
    s = dict(ai_key=key)
    if at: s['at'] = at
    return s
AVISO = card(type='aviso', head=True, lines=['Pedro Sánchez no ha participado en este documental.',
        'Sus respuestas son declaraciones públicas de archivo, con su fecha y su contexto original.',
        'Pedro Sánchez no está imputado en ninguna causa. Investigado no significa culpable.'])

# =====================================================================================
# APERTURA · LA NOCHE DEL PERDÓN  (in medias res)
# =====================================================================================
B('tension')
C('clip_39b_usted_no_lo_es.mp4', 'Pedro Sánchez a Mariano Rajoy', 'Cara a cara · 14/12/2015', 0, 5.6)
C('clip_39c_feijoo_decente.mp4', 'Alberto Núñez Feijóo a Pedro Sánchez', 'Cara a cara · 19/11/2026', 0, 7.0)
N('TOP', "[serious] La misma palabra. [pause] Once años después. [short pause] Con los papeles cambiados.",
  [card(type='aviso', lines=['14/12/2015', '19/11/2026'], size=60)])
N('NEW', "Jueves, diecinueve de noviembre de dos mil veintiséis. Madrid. Faltan diez días para las elecciones generales. "
         "Es el único cara a cara de la campaña. Y en el bloque dedicado a la corrupción, el presidente del Gobierno hace algo que no había hecho nunca en un debate.",
  [ai('plato_debate'), ai('atriles', at='cara a cara')])
C('clip_01b_pido_perdon_corrupcion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · RTVE · Cara a cara · 19/11/2026', 0, 15.8)
N('TOP', "[serious] Pide perdón. [short pause] Y en la misma frase se declara limpio. [pause] "
         "Las dos cosas a la vez. Así ha gobernado ocho años: pidiendo comprensión por lo que pasó a su alrededor, y defendiendo que nada de eso le toca a él.",
  [ai('congreso_noche'), ai('pasillo_vacio', at='ocho años')])
N('NEW', "Sus defensores dicen que ha sacado adelante el país en la década más difícil que se recuerda: una pandemia, un volcán, una riada, una guerra en Europa. "
         "Sus críticos dicen que ha sobrevivido a costa de casi todo lo que prometió. [short pause] Este documental no le va a pedir que elija. Le va a poner delante sus propias palabras.",
  [vid('ar_dana_coches__03.mp4', 40, at='riada'), vid('ar_ceuta_espigon__02.mp4', 12, at='críticos'), ai('urnas', at='propias palabras')])
N('TOP', "[softly] Hay preguntas que nadie le hizo así, una detrás de otra. [pause] Se las vamos a hacer. [short pause] "
         "Y le vamos a dejar contestar a él. Con sus respuestas reales. Con su fecha. Y con lo que pasó después.",
  [AVISO])
U.append(dict(k='T', voice='TOP', text="Pedro Sánchez. [pause] La entrevista que nadie le hizo.", secs=6.0, voice_at=0.8, sting='golpe',
              card=dict(type='title', title='Pedro Sánchez', sub='La entrevista que nadie le hizo')))
M('tema', 4, [card(type='aviso', lines=['Todas sus respuestas son reales.'], size=54)])

# =====================================================================================
# PREGUNTA 1 · ¿POR QUÉ TENDRÍAMOS QUE CREERLE?
# =====================================================================================
Q(1, '¿Por qué tendríamos que creerle?', 'Presidente, ¿por qué tendríamos que creerle?')
B('pulso')
N('NEW', "Pamplona, abril de dos mil quince. Pedro Sánchez lleva diez meses al frente del Partido Socialista. En un plató de la televisión navarra, le preguntan si su partido pactaría con EH Bildu para gobernar en Navarra.",
  [ai('pamplona_noche'), card(type='aviso', lines=['NAVARRA TV · ABRIL DE 2015'], size=46)])
C('clip_35_bildu_no_vamos_a_pactar.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Navarra TV · 2015', 1.4, 5.5)
N('TOP', "[serious] Cinco veces, si hacía falta. [pause] El veinte de mayo de dos mil veinte, en plena pandemia, el PSOE firmó con Unidas Podemos y con EH Bildu un acuerdo para derogar la reforma laboral. Bildu se convirtió después en uno de los apoyos estables de su Gobierno en el Congreso.",
  [dijo('2015 · NAVARRA TV', '«Con Bildu no vamos a pactar»', '20/05/2020', 'Acuerdo firmado por PSOE, Unidas Podemos y EH Bildu para derogar la reforma laboral', 'Fuente: El País · Maldita.es')])
N('NEW', "Septiembre de dos mil diecinueve. España va camino de su cuarta repetición electoral en cuatro años. Sánchez explica en laSexta por qué no quiere un Gobierno de coalición con Pablo Iglesias.",
  [ai('urnas_repeticion'), card(type='aviso', lines=['LASEXTA · 19/09/2019'], size=46)])
C('clip_31_no_dormiria.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · laSexta · 19/09/2019', 0, 10.5)
N('TOP', "Siete semanas después, el diez de noviembre, se celebran las elecciones. [short pause] Cuarenta y ocho horas más tarde, el doce de noviembre, Sánchez e Iglesias firman un preacuerdo de Gobierno. Y se abrazan.",
  [dijo('19/09/2019', '«No dormiría por la noche»', '12/11/2019', 'Preacuerdo de Gobierno de coalición con Unidas Podemos, 48 horas después de las elecciones', 'Fuente: RTVE')])
N('NEW', "En aquella misma campaña, Cataluña era el gran tema. Un mes antes, el catorce de octubre, el Tribunal Supremo había condenado a los líderes del proceso independentista. Sánchez, en funciones, compareció para fijar la posición del Gobierno.",
  [ai('supremo_fachada'), card(type='aviso', lines=['14/10/2019 · SENTENCIA DEL PROCÉS'], size=46)])
C('co_cumplimiento_integro__02.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 14/10/2019', 0, 12, base=DE)
N('TOP', "Y tres semanas después, en el debate electoral de Televisión Española, fue más lejos. Habló de Carles Puigdemont, que había huido a Bélgica.",
  [ai('plato_debate_2019')])
C('clip_32_traerlo_de_vuelta.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate electoral · RTVE · 04/11/2019', 0, 3.2)
C('co_referendum_ilegal__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Debate electoral · 04/11/2019', 0, 9, base=DE)
N('NEW', "[serious] Íntegro cumplimiento. Traerlo de vuelta. Un nuevo delito para los referéndums ilegales. [pause] "
         "Lo que vino después está en el Boletín Oficial del Estado. En junio de dos mil veintiuno, el Gobierno indultó a los nueve líderes del procés condenados a prisión. "
         "En diciembre de dos mil veintidós, las Cortes suprimieron el delito de sedición. El delito para los referéndums ilegales nunca llegó.",
  [dijo('14/10/2019', '«El acatamiento significa su íntegro cumplimiento»', 'JUNIO DE 2021', 'El Gobierno indulta a los nueve condenados a prisión por el procés', 'Fuente: BOE · El País'),
   dijo('04/11/2019', '«Un nuevo delito para prohibir los referéndums ilegales»', 'DICIEMBRE DE 2022', 'Se suprime el delito de sedición. El nuevo delito nunca se aprobó', 'Fuente: BOE', at='sedición')])
N('TOP', "Cuando le preguntaron por los indultos, el veintiocho de junio de dos mil veintiuno, dio esta respuesta.")
C('clip_36_indultos_nunca_cambie.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · 28/06/2021', 5.8, 19.4)
N('NEW', "Faltaba la amnistía. [short pause] En noviembre de dos mil veintidós, en Al Rojo Vivo, le preguntaron qué pedía el independentismo. Esta fue su respuesta, según la transcripción oficial de La Moncloa.",
  [card(type='aviso', lines=['LASEXTA · AL ROJO VIVO · 10/11/2022'], size=46)])
C('clip_33_no_entra_constitucion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · laSexta · 10/11/2022 (audio)', 0, 11.4, audio_only=True,
  quote='Algo que desde luego este gobierno no va a aceptar y que desde luego no entra en la legislación ni en la Constitución española.')
N('TOP', "[serious] Ocho meses después, el veintitrés de julio de dos mil veintitrés, Sánchez pierde las elecciones frente al Partido Popular. Pero puede seguir gobernando. "
         "Le faltan siete votos: los de Junts, el partido de Puigdemont. [pause] El veintiocho de octubre, ante el Comité Federal del PSOE, anuncia la amnistía con una frase que él mismo recordaría tres años después.",
  [ai('hemiciclo_vacio'), card(type='seats', title='Investidura · noviembre de 2023', total=350, groups=[['PSOE y socios', 172], ['Junts', 7], ['Resto', 171]]) ])
C('clip_34b_necesidad_virtud_wild.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 0, 11.0)
N('NEW', "La ley de amnistía se publicó en el BOE el diez de junio de dos mil veinticuatro. [short pause] Y aquí está la defensa del Gobierno, con un documento detrás: "
         "en julio de dos mil veinticinco, el Tribunal Constitucional concluyó que la Constitución no prohíbe una amnistía, aunque anuló algunos puntos de la ley. Hubo votos particulares en contra.",
  [doc('doc_33_BOE_STC_137-2025_amnistia_31-07-2025.jpg', 'STC 137/2025', ['La Constitución no prohíbe la amnistía', 'Inconstitucionalidad parcial · votos particulares'], 'BOE · 31/07/2025'),
   card(type='aviso', lines=['LA DEFENSA', 'El Gobierno sostiene que la amnistía es legal y que el Tribunal Constitucional le dio la razón.'], head=True, at='defensa')])
N('TOP', "Junts votó la investidura. Y dos años después, en octubre de dos mil veinticinco, rompió con el Gobierno. Su portavoz en el Congreso, Míriam Nogueras, lo dijo así.",
  [ai('congreso_escalinata')])
C('clip_36b_nogueras_bloqueado.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados', 0, 12.0)
N('NEW', "Este mes, en plena campaña, el propio Puigdemont lo resumió con una frase que publicó El Mundo: «Nos hemos aprovechado de la ambición de Sánchez para derrotar a España».",
  [card(type='quote', text='Nos hemos aprovechado de la ambición de Sánchez para derrotar a España', attrib='Carles Puigdemont · según El Mundo · noviembre de 2026')])
N('TOP', "[serious] El trece de noviembre, en un pódcast con millones de seguidores, le preguntaron por todos estos giros. Por qué un votante debería creer lo que promete ahora.")
C('clip_35c_derecho_a_cambiar_de_opinion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 26.6, 36.0)
C('clip_35d_horizonte_coherencia.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Informativos Telecinco · 16/11/2026', 0, 23.6)
N('NEW', "[softly] Un horizonte que no cambia. Y unas posiciones que sí. [pause] Él lo llama coherencia. Sus socios de investidura, en el Congreso, lo llamaron de otra manera.")
C('clip_36c_nogueras_cinico.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados · 12/11/2025', 0, 18.7)
N('TOP', "[serious] Pero el cambio de opinión que más caro le ha salido no fue sobre una ley. [pause] Fue sobre un hombre. Un hombre al que eligió él. [short pause] Y que hoy está condenado a veinticuatro años de prisión.",
  [doc('doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', 'TRIBUNAL SUPREMO', ['22/06/2026'], 'CGPJ', at='condenado')])
M('tema', 5)

# =====================================================================================
# PREGUNTA 2 · ¿QUIÉN ELIGIÓ A JOSÉ LUIS ÁBALOS?
# =====================================================================================
Q(2, '¿Quién eligió a José Luis Ábalos?', 'Presidente, ¿quién eligió a José Luis Ábalos?')
B('tension')
N('TOP', "[serious] Veintidós de junio de dos mil veintiséis. Tribunal Supremo. Siete magistrados, por unanimidad. "
         "José Luis Ábalos, exministro de Transportes y exsecretario de Organización del PSOE: veinticuatro años y tres meses de prisión. "
         "Koldo García, su asesor: diecinueve años y ocho meses. El empresario Víctor de Aldama, que confesó: cuatro años y medio.",
  [doc('doc_03_sentencia_abalos_CGPJ_22-06-2026.jpg', 'NOTA DEL TRIBUNAL SUPREMO', ['Ábalos · 24 años y 3 meses', 'Koldo García · 19 años y 8 meses'], 'CGPJ · 22/06/2026'),
   card(type='ficha', name='José Luis Ábalos', role='Exministro · CONDENADO por el Tribunal Supremo', at='Ábalos'),
   card(type='ficha', name='Koldo García', role='Exasesor · CONDENADO', at='Koldo')])
R('DOC', "Sentencia del Tribunal Supremo. Al valorar la confesión de Aldama, el tribunal habla de una «corrupción orgánica, organizada y continuada».",
  [card(type='quote', text='corrupción orgánica, organizada y continuada', attrib='STS 418/2026 · al valorar la confesión de Aldama')])
N('NEW', "La defensa de Ábalos ve arbitrariedad en la sentencia y ha anunciado que acudirá a la justicia europea. [short pause] Pedro Sánchez no está imputado en esta causa. Ni en ninguna otra. "
         "Pero la pregunta de este capítulo no es judicial. Es política. ¿Cómo llegó Ábalos hasta ahí? [pause] Para responderla hay que volver a un coche.",
  [card(type='aviso', lines=['LA DEFENSA', 'El abogado de Ábalos recurrirá. Pedro Sánchez no está imputado en ninguna causa.'], head=True)])
N('TOP', "Otoño de dos mil dieciséis. Sánchez acaba de perder la secretaría general del PSOE tras un Comité Federal a gritos. Sin cargo, decide recorrer España en su coche para recuperar el partido, agrupación por agrupación. "
         "Él mismo lo contó en su libro, Manual de resistencia. En ese Peugeot viajaban cuatro hombres. [pause] Pedro Sánchez. José Luis Ábalos. Santos Cerdán. Y Koldo García.",
  [ai('carretera_noche'), ai('coche_lluvia', at='Peugeot'),
   card(type='board', title='El Peugeot · 2016', nodes=[['Pedro Sánchez', 'candidato'], ['José Luis Ábalos', 'condenado'], ['Santos Cerdán', 'investigado'], ['Koldo García', 'condenado']], links=[[0, 1], [0, 2], [0, 3], [1, 3]], center=True, at='cuatro hombres')])
N('NEW', "En mayo de dos mil diecisiete, Sánchez gana las primarias. Un mes después, el dieciocho de junio, elige a su equipo. El secretario de Organización, el número tres del partido, el que controla el aparato, será José Luis Ábalos. Y en su área entra Santos Cerdán.",
  [doc('doc_cierre_Abalos_secretario_Organizacion_EFE_18-06-2017.jpg', 'EFE · 18/06/2017', ['Sánchez elige a Ábalos para Organización'], 'Valencia Plaza (EFE)'),
   doc('doc_cierre_Abalos_Cerdan_area_Organizacion_EFE_18-06-2017.jpg', 'EL ÁREA DE ORGANIZACIÓN', ['Ábalos, con Cerdán dentro'], 'Valencia Plaza (EFE)', at='Santos Cerdán')])
N('TOP', "[serious] Un año después, el treinta y uno de mayo de dos mil dieciocho, Sánchez defiende en el Congreso la moción de censura contra Mariano Rajoy, tras la sentencia del caso Gürtel. Y le exige lo que él llama decencia.",
  [ai('congreso_tribuna')])
C('clip_00a_dimita_rajoy.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Moción de censura · Congreso · 31/05/2018', 0, 11.8)
C('clip_38_abalos_decencia_mocion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Moción de censura · Congreso · 31/05/2018', 5.8, 28.8)
N('NEW', "Quien defendió aquella moción desde la tribuna en nombre del PSOE fue José Luis Ábalos. Según recuerda Maldita.es, dijo que la presentaban para sacar de la política la corrupción. Rajoy le contestó así.",
  [doc('doc_cierre_maldita_mocion_23-06-2026.jpg', 'MALDITA.ES', ['Ábalos defendió la moción «para sacar de la política la corrupción»'], 'Maldita.es · 23/06/2026')])
C('clip_39_rajoy_lecciones.mp4', 'Mariano Rajoy', 'Congreso · Moción de censura · 2018', 0, 8.0)
N('TOP', "Una semana después, el siete de junio, el Boletín Oficial del Estado publica el nombramiento. Ministro de Fomento: José Luis Ábalos Meco. Firma el real decreto el presidente del Gobierno.",
  [doc('doc_03_BOE_nombramiento_Abalos_ministro_07-06-2018.jpg', 'REAL DECRETO 357/2018', ['Ministro de Fomento: don José Luis Ábalos Meco'], 'Extracto · BOE-A-2018-7577', focus=[0.1, 0.35, 0.8, 0.3])])
N('NEW', "Enero de dos mil veinte. Aeropuerto de Barajas, de madrugada. Ábalos se reúne en un avión con Delcy Rodríguez, vicepresidenta de Venezuela, que tenía prohibida la entrada en el espacio Schengen. "
         "Durante semanas, el ministro dio versiones distintas de aquel encuentro. Maldita.es las contó. Y el Gobierno negó, con estas palabras, que el presidente hubiera hablado por teléfono con ella.",
  [ai('pista_aeropuerto_noche'), doc('doc_13_maldita_versiones_Delcy_11-10-2024.jpg', 'LAS VERSIONES DE BARAJAS', ['Las versiones de Ábalos y del Gobierno'], 'Maldita.es · 11/10/2024', at='Maldita'),
   doc('doc_13_Exteriores_desmiente_llamada_Delcy_06-02-2020.jpg', 'COMUNICADO', ['«Es absolutamente falso»'], 'Secretaría de Estado de Comunicación · 06/02/2020', at='negó')])
N('TOP', "En marzo de dos mil veinte, en vísperas del ocho de marzo, el PSOE publicó una campaña en redes. Uno de sus protagonistas era su secretario de Organización.",
  [card(type='aviso', lines=['#SOYFEMINISTAPORQUE · PSOE · MARZO DE 2020'], size=44)])
C('ul_abalos_feminista__01.mp4', 'José Luis Ábalos', 'Vídeo del PSOE · #SoyFeministaPorque · marzo de 2020', 0, 9.0, base=DE)
N('NEW', "[serious] Años después, el sumario del caso Koldo y los audios publicados por la prensa describirían otra cosa. Según las informaciones basadas en los informes de la UCO, la trama pagaba viajes y alojamientos a mujeres de su entorno. Feijóo lo usó en el Congreso como arma contra el presidente.",
  [ai('expediente_mesa')])
C('clip_18_feijoo_prostibulos.mp4', 'Alberto Núñez Feijóo', 'Congreso · 09/07/2025', 4.6, 18.4)
R('DOC', "Es una acusación política, pronunciada en la tribuna del Congreso. Ningún tribunal ha juzgado al presidente por ello.",
  [card(type='aviso', lines=['ACUSACIÓN POLÍTICA', 'Ningún tribunal ha juzgado al presidente por ello.'], head=True)])
N('TOP', "Julio de dos mil veintiuno. Sánchez remodela su Gobierno y saca a Ábalos del Ministerio y de la secretaría de Organización. En aquel momento no explicó en público por qué. "
         "Su sustituto al frente de la Organización del PSOE es Santos Cerdán. [pause] Y dos años después, en las elecciones de dos mil veintitrés, Ábalos vuelve: número dos de la lista del PSOE por Valencia.",
  [doc('doc_cierre_Cerdan_sustituye_Abalos_Mallorcadiario_13-07-2021.jpg', 'JULIO DE 2021', ['Cerdán sustituye a Ábalos'], 'Mallorcadiario · 13/07/2021'),
   card(type='aviso', lines=['23J · 2023', 'Número 2 de la lista del PSOE por Valencia: José Luis Ábalos'], head=True, at='número dos')])
N('NEW', "El PSOE sostiene que lo apartó en cuanto supo. Que lo expulsó. Que colaboró con la justicia. El nueve de julio de dos mil veinticinco, en el Congreso, Sánchez dio su versión.",
  [card(type='aviso', lines=['LA DEFENSA', 'El PSOE dice que apartó y expulsó a Ábalos y que colabora con la justicia.'], head=True)])
C('h16_me_equivoque.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/07/2025', None, None, base='media/e29n90/hls/')
C('h17_politico_limpio.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/07/2025', None, None, base='media/e29n90/hls/')
N('TOP', "[serious] Me equivoqué al confiar en Ábalos. [short pause] Y en Santos Cerdán. [pause] El hombre que vino después. El que estaba en el coche. El que heredó las llaves de Ferraz.",
  [ai('ferraz_noche_generica')])
M('tension', 4)

# =====================================================================================
# PREGUNTA 3 · ¿SABÍA LO QUE PASABA EN FERRAZ?
# =====================================================================================
Q(3, '¿Sabía usted lo que pasaba en Ferraz?', 'Presidente, ¿sabía usted lo que pasaba en Ferraz?')
B('pulso')
N('NEW', "Madrid, calle Ferraz, número setenta. Sede federal del Partido Socialista. Miércoles, veintisiete de mayo de dos mil veintiséis. "
         "Agentes de la Unidad Central Operativa de la Guardia Civil entran en el edificio. Se quedan doce horas. [short pause] El PSOE insiste en que no fue un registro, sino un requerimiento de documentación. Es exacto: fue un requerimiento.",
  [ai('ferraz_fachada_dia'), card(type='aviso', lines=['27/05/2026 · FERRAZ, 70', 'Requerimiento de la UCO · 12 horas'], head=True, at='doce horas')])
N('TOP', "[serious] Para entender por qué la UCO llegó hasta allí, hay que volver a junio de dos mil veinticinco. El juez del Supremo ve «consistentes indicios» contra Santos Cerdán, el número tres del partido. Cerdán dimite de todos sus cargos. Pasará cuatro meses y veinte días en prisión provisional.",
  [doc('doc_03b_cerdan_auto_indicios_CGPJ_12-06-2025.jpg', 'AUTO DEL TRIBUNAL SUPREMO', ['«Consistentes indicios» contra Santos Cerdán'], 'CGPJ · 12/06/2025'),
   card(type='ficha', name='Santos Cerdán', role='Exsecretario de Organización · INVESTIGADO · presunción de inocencia', at='Cerdán dimite')])
N('NEW', "Según publicó Voz Pópuli, Cerdán había declarado dos reuniones con un empresario de la trama. Los investigadores le atribuyen treinta y nueve. Cerdán niega haber cometido ningún delito.",
  [card(type='counter', **{'from': 2, 'to': 39, 'label': 'reuniones localizadas por los investigadores, según Voz Pópuli'})])
N('TOP', "Aquel mismo verano salió a la luz otra figura. Leire Díez, militante del PSOE. El Confidencial publicó la grabación de una reunión de febrero de dos mil veinticinco, en la que hablaba de conseguir información contra mandos de la Guardia Civil que investigaban al partido. Ella reconoció que la voz era suya.",
  [ai('grabadora_mesa')])
C('clip_15_necesito_a_balas.mp4', 'Leire Díez (grabación)', 'Publicada por El Confidencial · reunión de febrero de 2025', 0, 4.0, audio_only=True,
  quote='No necesito a todo el mundo ahora. Necesito a Balas.')
N('NEW', "Balas es el apellido de un teniente coronel de la UCO. Según el juez Santiago Pedraz, Leire Díez formaba parte de una red para obstaculizar causas judiciales. Según el sumario publicado por la prensa, recibía unos cuatro mil euros al mes, y la gerente del PSOE está imputada. [short pause] "
         "El PSOE dice que Leire Díez «nada tiene que ver» con la organización. Ella niega haber actuado en su nombre. Está investigada; no condenada.",
  [card(type='ficha', name='Leire Díez', role='Militante del PSOE · INVESTIGADA · presunción de inocencia'),
   card(type='aviso', lines=['LA DEFENSA', 'El PSOE: Leire Díez «nada tiene que ver» con la organización.'], head=True, at='nada tiene que ver')])
N('TOP', "[serious] Y ahora, las respuestas. Porque el presidente ha hablado mucho de corrupción. [pause] Febrero de dos mil veinticuatro, recién estallado el caso Koldo.",
  [card(type='aviso', lines=['LO QUE DIJO'], size=70)])
C('clip_41b_no_tapa.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 28/02/2024', 0.8, 3.6)
N('NEW', "Junio de dos mil veinticinco, tras el auto contra Cerdán.")
C('clip_15e_corrupcion_cero.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 18/06/2025', 0, 7.7)
N('NEW', "Junio de dos mil veintiséis, dos días después de la sentencia del Supremo.")
C('clip_15g_caso_flagrante.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 24/06/2026', 0, 5.0)
C('h15f_no_financiado.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 24/06/2026', None, None, base='media/e29n90/hls/')
N('TOP', "[serious] El Partido Socialista no se ha financiado irregularmente. [pause] Es lo que sostiene el PSOE. Y aquí está lo que dicen los documentos: "
         "en octubre de dos mil veintiséis, la Fiscalía Anticorrupción vio indicios contra el partido, pero consideró prematuro imputarlo. El PSOE, como organización, no está imputado.",
  [card(type='dijo', left=dict(label='LO QUE DICE EL PSOE', date='24/06/2026', text='«No hay financiación irregular»'),
        right=dict(label='LO QUE DICE LA FISCALÍA', date='OCTUBRE DE 2026', text='Ve indicios contra el partido, pero considera prematuro imputarlo', source='Fuente: Ara · 08/10/2026'), red=False)])
N('NEW', "Y en el debate del diecinueve de noviembre, Feijóo resumió la ofensiva de su partido con una sola frase sobre la política de vivienda.")
C('clip_20b_sumarios.mp4', 'Alberto Núñez Feijóo', 'Cara a cara · RTVE · 19/11/2026', 3.8, 13.1)
N('TOP', "[softly] Pisos en los sumarios. Viviendas prometidas. [pause] De las viviendas hablaremos. [short pause] Pero antes hay otra pregunta. Porque las causas no se quedaron en la sede del partido. [pause] Llegaron a su casa.",
  [ai('ventana_noche_moncloa_generica')])
M('tema', 5)

# =====================================================================================
# PREGUNTA 4 · ¿POR QUÉ SU FAMILIA ESTÁ EN LOS TRIBUNALES?
# =====================================================================================
Q(4, '¿Por qué su familia está en los tribunales?', 'Presidente, ¿por qué su familia está en los tribunales?')
B('tension')
N('TOP', "[serious] Miércoles, veinticuatro de abril de dos mil veinticuatro. Un juzgado de Madrid abre diligencias contra Begoña Gómez, la esposa del presidente, por su actividad profesional. "
         "Esa misma tarde, Sánchez publica una carta a la ciudadanía. Anuncia que se toma cinco días para pensar si sigue. Y escribe: «¿Merece la pena todo esto? Sinceramente, no lo sé».",
  [ai('carta_escritorio'), card(type='quote', text='¿Merece la pena todo esto? Sinceramente, no lo sé.', attrib='Carta a la ciudadanía · 24/04/2024', at='Merece')])
N('NEW', "Cinco días después, se queda. Y tres semanas más tarde, en laSexta, deja la frase que marcaría su defensa.")
C('ul_hay_fango__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · laSexta · 17/05/2024', None, None, base=DE)
N('TOP', "Noviembre de dos mil veinticuatro. Asamblea de Madrid. Begoña Gómez comparece ante una comisión de investigación impulsada por el Partido Popular sobre su relación con la Universidad Complutense. La diputada popular Mercedes Zarzalejo le pregunta durante más de dieciséis minutos.",
  [ai('sala_comision_vacia')])
C('clip_19d_1_vinculacion.mp4', 'Mercedes Zarzalejo (PP)', 'Asamblea de Madrid · 13/11/2024', 3.0, 14.7)
C('clip_19d_3_software.mp4', 'Mercedes Zarzalejo (PP)', 'Asamblea de Madrid · 13/11/2024', 0, 2.8)
C('clip_19c_derecho_no_responder.mp4', 'Begoña Gómez', 'Asamblea de Madrid · 13/11/2024', 0, 14.3)
N('NEW', "Hoy, Begoña Gómez está procesada. Irá a juicio con jurado, previsto para dos mil veintisiete. [short pause] Y aquí está su defensa, que también consta en la causa: la Fiscalía pide su absolución. Ella sostiene que es víctima de una persecución por ser la mujer del presidente.",
  [card(type='ficha', name='Begoña Gómez', role='Esposa del presidente · PROCESADA · juicio con jurado previsto en 2027'),
   card(type='aviso', lines=['LA DEFENSA', 'La Fiscalía pide la absolución. Begoña Gómez denuncia una persecución.'], head=True, at='defensa')])
N('TOP', "[serious] Doce de noviembre de dos mil veintiséis. Mitin de arranque de campaña en Sevilla. Begoña Gómez sube al escenario.",
  [card(type='aviso', lines=['SEVILLA · 12/11/2026'], size=50)])
C('clip_19a_senoras_de.mp4', 'Begoña Gómez', 'Mitin del PSOE · Sevilla · 12/11/2026', 0, 6.9)
C('clip_04_baile_sevilla_completo.mp4', 'Pedro Sánchez y Begoña Gómez', 'Mitin del PSOE · Sevilla · 12/11/2026', 20.0, 26.0, db=-14)
N('NEW', "Seis días después, el presidente era portada de la revista Lecturas. El titular: «No imagino mi vida sin Begoña».",
  [doc('doc_05_portada_Lecturas_18-11-2026.png', 'LECTURAS', ['«No imagino mi vida sin Begoña»'], 'Lecturas · 18/11/2026')])
N('TOP', "En casa de los Sánchez hay otra causa. David Sánchez, hermano del presidente, que trabajaba para la Diputación de Badajoz. "
         "Un tribunal le ha condenado a nueve años de inhabilitación como cooperador necesario de un delito de prevaricación, y le ha absuelto del de tráfico de influencias. La sentencia está recurrida. No es firme.",
  [card(type='ficha', name='David Sánchez', role='Hermano del presidente · CONDENADO en primera instancia · sentencia recurrida')])
N('NEW', "Y hay una tercera historia, más pequeña, publicada por la prensa. Calle San Bernardo, número treinta y ocho, Madrid. El edificio es de Muface, la mutualidad pública de los funcionarios. "
         "Según el contrato que publicó El Debate, la familia de Begoña Gómez alquila allí un ático desde mil novecientos ochenta y seis: entonces, doscientos setenta y dos euros al mes; en dos mil veinticinco, ochocientos ochenta y dos. Cuando el Senado pidió los datos de esos pisos, el Gobierno no los entregó, según The Objective.",
  [doc('doc_18_muface_contrato_atico_1986_pag1_ElDebate_02-09-2025.jpg', 'CONTRATO DEL ÁTICO · 1986', ['San Bernardo, 38 · Madrid'], 'El Debate · 02/09/2025'),
   doc('doc_18_muface_TheObjective_titular_01-10-2025.jpg', 'RESPUESTA AL SENADO', ['El Gobierno no da al Senado los datos de los pisos'], 'The Objective · 01/10/2025', at='Senado')])
N('TOP', "[serious] Para defender a su familia, el presidente ha cargado contra una parte de los jueces. El uno de septiembre de dos mil veinticinco, en Televisión Española, le preguntaron si había jueces en guerra con su Gobierno.")
C('clip_23_jueces_minoria.mp4', 'Pedro Sánchez (incluye la pregunta)', 'RESPUESTA REAL · TVE · 01/09/2025', 0, 19.3)
N('NEW', "Tres asociaciones de jueces le respondieron públicamente. [short pause] Y hay otra frase suya, de hace siete años, que explica por qué la relación del Gobierno con la justicia es una de las preguntas de esta campaña. Seis de noviembre de dos mil diecinueve. Radio Nacional.",
  [card(type='aviso', lines=['RNE · 06/11/2019'], size=50)])
C('clip_22_pues_ya_esta.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · RNE · 06/11/2019 (audio)', 0, 9.8, audio_only=True,
  quote='¿La Fiscalía de quién depende? ¿De quién depende? Del Gobierno. Pues ya está.')
N('TOP', "Al día siguiente rectificó: dijo que no había sido preciso. [pause] Seis años después, el veinte de noviembre de dos mil veinticinco, el Tribunal Supremo condenó al fiscal general del Estado a dos años de inhabilitación y a una multa por revelación de datos reservados. Hubo votos particulares. Y el tribunal no dio por acreditado que el presidente le diera ninguna orden.",
  [card(type='dijo', left=dict(date='06/11/2019 · RNE', text='«¿La Fiscalía de quién depende? (…) Pues ya está»'), right=dict(date='20/11/2025', text='El Supremo condena al fiscal general del Estado a dos años de inhabilitación', source='Fuente: Poder Judicial · RTVE'))])
N('NEW', "Tres días después de esa condena, desde la cumbre del G20 en Johannesburgo, el presidente dijo esto.")
C('clip_21_creo_inocencia_fiscal.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · G20 Johannesburgo · 23/11/2025', 0.4, 5.4)
N('TOP', "[serious] Cree en su inocencia. Y la defiende. [pause] Pero en el verano de dos mil veintiséis la pregunta dejó de ser qué decía el presidente. Pasó a ser dónde estaba.",
  [ai('playa_noche_generica')])
M('tension', 4)

# =====================================================================================
# PREGUNTA 5 · ¿DÓNDE ESTABA USTED?
# =====================================================================================
Q(5, '¿Dónde estaba usted?', 'Presidente, ¿dónde estaba usted?')
B('noche')
R('DOC', "Mensaje del Centro Nacional de Inteligencia. Veintinueve de julio de dos mil veintiséis. Trece horas, cincuenta y dos minutos. «Llamamiento para asalto por valla y mar mañana a las veinte horas».",
  [doc('doc_26_ceuta_whatsapp_CNI_Moncloa_29-07-2026.jpg', 'CNI · 29/07/2026 · 13:52', ['«Llamamiento para asalto por valla y mar mañana a las 20h»'], 'Documento publicado por La Moncloa · 09/09/2026')])
N('TOP', "[serious] Al día siguiente, miles de personas entran en Ceuta a nado y saltando el espigón. Según los datos recogidos por Maldita.es y elDiario.es, unas setenta y dos mil entradas. Y al menos setenta y dos muertos, según la Delegación del Gobierno.",
  [vid('ar_ceuta_espigon__02.mp4', 5), vid('ar_ceuta_espigon__02.mp4', 40, at='espigón'), card(type='counter', **{'to': 72000, 'label': 'entradas en Ceuta, según los datos publicados'}), card(type='counter', **{'to': 72, 'label': 'muertos como mínimo, según la Delegación del Gobierno'}, at='setenta y dos muertos')])
N('NEW', "El treinta de julio, según recogió Maldita.es, el Ministerio del Interior sostiene que no es posible declarar la situación de emergencia nacional. El treinta y uno, el presidente viaja a Ceuta. La visita dura hora y media. Le reciben con pitos.",
  [vid('ar_ceuta_visita_pitos__01.mp4', 3), vid('ar_ceuta_visita_pitos__02.mp4', 6, at='pitos')])
N('TOP', "Y después, se marcha a La Mareta, la residencia oficial de Lanzarote, para sus vacaciones de verano. [pause] El uno de agosto, sus redes sociales publican este vídeo.",
  [vid('ar_mareta_llegada__02.mp4', 4), card(type='aviso', lines=['LA MARETA · LANZAROTE · AGOSTO DE 2026'], size=44, at='La Mareta')])
C('clip_24a_playlist.mp4', 'Pedro Sánchez', 'Vídeo en sus redes sociales · 01/08/2026', 0, 6.0)
C('clip_24b_feliz_verano.mp4', 'Pedro Sánchez', 'Vídeo en sus redes sociales · 01/08/2026', 0, 4.8)
N('NEW', "El Consejo de Seguridad Nacional no se reunió hasta veinticinco días después. [short pause] El tres de septiembre, de vuelta en el Congreso, el presidente explicó qué decían los informes de inteligencia que había recibido.",
  [card(type='counter', **{'to': 25, 'label': 'días hasta la reunión del Consejo de Seguridad Nacional'})])
C('clip_26_aviso_rutinario.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 03/09/2026', 0, 5.4)
N('TOP', "[serious] Un aviso rutinario. [pause] Seis días después, el propio Gobierno publicó todos los informes. Entre ellos, el mensaje del día veintinueve. «Asalto por valla y mar. Mañana. Veinte horas».",
  [doc('doc_26_ceuta_cabecera_Moncloa_09-09-2026.jpg', 'LOS INFORMES DESCLASIFICADOS', ['Publicados por La Moncloa'], 'La Moncloa · 09/09/2026'),
   doc('doc_26_ceuta_whatsapp_CNI_Moncloa_29-07-2026.jpg', 'CNI · 29/07/2026', ['«asalto por valla y mar mañana las 20h»'], 'La Moncloa', at='Asalto')])
C("ul_ceuta_evidencias__01.mp4", "Pedro Sánchez", "RESPUESTA REAL · septiembre de 2026", None, None, base=DE)
N('NEW', "La defensa del Gobierno: que ningún informe previó ni la escala ni la probabilidad de lo que ocurrió, y que el presidente trabajó desde la residencia oficial con el ministro del Interior al frente. Ese mismo día, en Televisión Española, lo explicó así.",
  [card(type='aviso', lines=['LA DEFENSA', 'Ningún informe previó la escala ni la probabilidad de lo ocurrido.'], head=True)])
C('ul_manyaneros_chantaje__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Mañaneros 360 · TVE · 09/09/2026', None, None, base=DE)
C('clip_25_no_estaba_de_vacaciones.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 3.5, 15.7)
N('TOP', "Dieciséis de septiembre. Pasillos del Congreso. Un periodista le pregunta por los menores que siguen en las calles de Ceuta.")
C('clip_25c_eso_a_vivas.mp4', 'Pedro Sánchez (incluye la pregunta)', 'RESPUESTA REAL · Congreso · 16/09/2026', 0.6, 5.8)
N('NEW', "Juan Jesús Vivas es el presidente de Ceuta. [short pause] La Casa Real hizo saber que el Rey seguía la situación con preocupación e indignación. Y el presidente anunció una visita del jefe del Estado.",
  [vid('ar_rey_ceuta_indignacion__02.mp4', 5)])
C('clip_28b_rey_ceuta_melilla.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cadena SER · 31/08/2026', 0, 20.8)
N('TOP', "[serious] No era la primera vez que una catástrofe le preguntaba al presidente dónde estaba. [pause] Veintinueve de octubre de dos mil veinticuatro. Valencia. La DANA. Doscientos treinta muertos en tres comunidades, según el balance oficial de La Moncloa de diciembre.",
  [vid('ar_dana_coches__03.mp4', 20), vid('ar_dana_poyo__02.mp4', 10, at='La DANA'), card(type='counter', **{'to': 230, 'label': 'muertos · balance oficial de La Moncloa · 02/12/2024'}, at='Doscientos treinta')])
R('DOC', "Dos de noviembre de dos mil veinticuatro. Comparecencia del presidente: «El Gobierno central está listo para ayudar. Si necesita más recursos, que los pida».",
  [card(type='quote', text='El Gobierno central está listo para ayudar. Si necesita más recursos, que los pida.', attrib='Pedro Sánchez · La Moncloa · 02/11/2024')])
N('NEW', "En esa misma comparecencia anunció diez mil efectivos más. Y la versión de la frase que circuló después por redes, recortada, era falsa, como comprobó Maldita.es. "
         "Pero la ley permite al Gobierno declarar una emergencia de interés nacional por iniciativa propia. No la declaró. Su defensa: era una facultad, no una obligación, y la gestión correspondía a la Generalitat Valenciana.",
  [card(type='aviso', lines=['LEY 17/2015', 'Emergencia de interés nacional: a iniciativa propia. No se declaró.'], head=True),
   card(type='aviso', lines=['LA DEFENSA', 'Era una facultad, no una obligación. La competencia era de la Generalitat.'], head=True, at='defensa')])
N('TOP', "Al día siguiente, en Paiporta, la comitiva oficial entra en una calle llena de barro. Los vecinos gritan. Lanzan objetos. El coche del presidente es golpeado. Sánchez se va. Los Reyes se quedan.",
  [vid('ar_paiporta_coche__01.mp4', 3), vid('ar_paiporta_salida__01.mp4', 8, at='Sánchez se va'), vid('ar_paiporta_reyes__03.mp4', 6, at='Los Reyes')])
N('NEW', "El Gobierno atribuyó la agresión a grupos ultras organizados, y defendió que la seguridad aconsejaba sacar al presidente. [pause] Y tres años antes, en La Palma, con el volcán en erupción, la promesa había sido esta.",
  [card(type='aviso', lines=['LA DEFENSA', 'Grupos ultras organizados y razones de seguridad.'], head=True)])
C('clip_28bx_la_palma_recursos.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Palma · 20/09/2021', 0, 6.7)
N('TOP', "[serious] Todos los recursos del Estado. [pause] Melilla, junio de dos mil veintidós: al menos veintitrés migrantes mueren en la valla. El presidente, desde Bruselas, valoró así la actuación.",
  [ai('valla_frontera_niebla')])
C('clip_30b_bien_resuelto.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Bruselas · 24/06/2022', 0, 3.6)
N('NEW', "Y tras el gran apagón del veintiocho de abril de dos mil veinticinco, la responsabilidad tenía destinatario.")
C('clip_29_operadores_privados.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 29/04/2025', 0, 6.5)
N('TOP', "[softly] Siempre hay un recurso que pedir. Un informe rutinario. Un operador privado. Un presidente autonómico al que preguntar. [pause] Y en enero de dos mil veintiséis, llegó la tragedia que tocaría a su propio Gobierno. [short pause] Sobre raíles.",
  [ai('vias_alta_velocidad_niebla')])
M('tema', 4)

# =====================================================================================
# PREGUNTA 6 · ¿QUIÉN RESPONDE POR LAS VÍAS?
# =====================================================================================
Q(6, '¿Quién responde por las vías?', 'Presidente, ¿quién responde por las vías?')
B('noche')
N('NEW', "Enero de dos mil veintiséis. Adamuz, Córdoba. Un tren de alta velocidad sufre un accidente. Según el propio ministro, en una recta y en una vía renovada. El ministro de Transportes, Óscar Puente, comparece.",
  [ai('vias_recta_amanecer'), card(type='ficha', name='Óscar Puente', role='Ministro de Transportes (2023-2026)', at='Óscar Puente')])
C('clip_08_tremendamente_extrano.mp4', 'Óscar Puente', 'Ministro de Transportes · 18/01/2026', 0, 4.9)
C('clip_10b2_bajisima.mp4', 'Óscar Puente', 'Onda Cero · enero de 2026', 0, 9.9)
N('TOP', "[serious] Muy baja. Bajísima. [pause] Veintiocho de octubre de dos mil veintiséis. Urda, Toledo. Otro accidente ferroviario. Sesenta y nueve muertos, según la información publicada. "
         "Ese día el presidente viaja a Urda y habla de una confianza quebrada.",
  [ai('estacion_noche_vacia'), card(type='counter', **{'to': 69, 'label': 'muertos en Urda · 28/10/2026'}, at='Sesenta y nueve')])
C('h10_urda.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Urda · 28/10/2026', None, None, base='media/e29n90/hls/')
N('NEW', "El tres de noviembre, ante la Diputación Permanente del Congreso, Óscar Puente anuncia que se va.",
  [card(type='aviso', lines=['DIPUTACIÓN PERMANENTE · 03/11/2026'], size=46)])
C('clip_10d2_renuncio_listas.mp4', 'Óscar Puente', 'Congreso · Diputación Permanente · 03/11/2026', 6.7, 15.9)
C('clip_10d_no_todos_iguales.mp4', 'Óscar Puente', 'Congreso · Diputación Permanente · 03/11/2026', 0, 5.7)
N('TOP', "El BOE del día siguiente publica su cese, «agradeciéndole los servicios prestados».",
  [doc('doc_10d_BOE_cese_Puente_04-11-2026.jpg', 'REAL DECRETO 974/2026', ['Cese de don Óscar Puente Santiago', '«agradeciéndole los servicios prestados»'], 'BOE · 04/11/2026')])
N('NEW', "[serious] Martes, diez de noviembre. Catedral de Toledo. Funeral por las víctimas de Urda. [pause] El presidente del Gobierno no está. "
         "Fuentes de La Moncloa explicaron a la prensa que no acostumbra a asistir a ceremonias religiosas.",
  [ai('catedral_interior_velas'), card(type='aviso', lines=['LA DEFENSA', 'Fuentes de La Moncloa: no acostumbra a asistir a ceremonias religiosas.'], head=True, at='Fuentes')])
N('TOP', "En el archivo hay otras imágenes del presidente. [short pause] En el funeral de Montserrat Caballé, en dos mil dieciocho. En el funeral de Estado de David Sassoli, en Roma, en dos mil veintidós. En el de Guillermo Fernández Vara, en dos mil veinticinco. Y en la misa del papa León catorce en la Sagrada Familia, en junio de este año.",
  [card(type='aviso', lines=['ARCHIVO'], size=60)])
C('clip_04z_1_caballe_2018.mp4', 'Funeral de Montserrat Caballé', 'Barcelona · 08/10/2018', 0, 1.6)
C('clip_04z_2_sassoli_2022.mp4', 'Funeral de Estado de David Sassoli', 'Roma · 14/01/2022 · La Moncloa', 0, 1.6)
C('clip_04z_3_vara_2025.mp4', 'Funeral de Guillermo Fernández Vara', 'Olivenza · 06/10/2025', 0, 1.6)
C('clip_04z_4_papa_2026.mp4', 'Misa de León XIV', 'Sagrada Familia · 10/06/2026 · La Moncloa', 0, 1.6)
N('NEW', "Dos días después del funeral de Toledo, el doce de noviembre, arranca la campaña. Mitin del PSOE en Sevilla.",
  [card(type='aviso', lines=['SEVILLA · 12/11/2026'], size=50)])
C('clip_04c_te_quiero_mitin.mp4', 'Público del mitin', 'Sevilla · 12/11/2026', 0, 3.0)
C('clip_04b_baile_montero_completo.mp4', 'María Jesús Montero y Begoña Gómez', 'Mitin del PSOE · Sevilla · 12/11/2026', 0, 6.0, db=-14)
N('TOP', "[serious] Una semana después, en el cara a cara, Feijóo se lo reprochó.")
C('clip_01c_feijoo_perdon_toledo.mp4', 'Alberto Núñez Feijóo', 'Cara a cara · RTVE · 19/11/2026', 0, 12.3)
N('NEW', "Y el presidente pidió perdón a las familias. Dijo que es un dolor que llevará siempre con él. [pause] Es su respuesta. [short pause] La siguiente pregunta lleva a otro hombre en el que dijo confiar. Su mentor.",
  [card(type='aviso', lines=['LA DEFENSA', 'En el debate, Sánchez pidió perdón a las familias de las víctimas.'], head=True)])
M('tension', 4)

# =====================================================================================
# PREGUNTA 7 · ¿POR QUÉ SIGUE DEFENDIENDO A ZAPATERO?
# =====================================================================================
Q(7, '¿Por qué sigue defendiendo a Zapatero?', 'Presidente, ¿por qué sigue defendiendo a José Luis Rodríguez Zapatero?')
B('pulso')
N('TOP', "[serious] Madrid. Despacho de José Luis Rodríguez Zapatero. Primavera de dos mil veintiséis. La Policía registra la oficina del expresidente del Gobierno. En una caja fuerte aparecen joyas. "
         "The Objective publicó las fotografías, en las bolsas de la Policía.",
  [vid('ar_zapatero_joyas__02.mp4', 4), doc('doc_14_joyas_Zapatero_TheObjective_11-06-2026.jpg', 'LAS JOYAS', ['Fotos de las joyas, en las bolsas de la Policía'], 'The Objective · 11/06/2026', at='The Objective'),
   vid('ar_zapatero_joyas__03.mp4', 6, at='bolsas')])
N('NEW', "El auto del diecinueve de mayo le investiga por tráfico de influencias, organización criminal y falsedad documental, en la causa que examina el rescate público de la aerolínea Plus Ultra. Y hay una pieza separada, por contrabando y delito fiscal, por las joyas. "
         "Zapatero defiende su inocencia. Pidió la nulidad de la causa, y le fue rechazada.",
  [card(type='ficha', name='José Luis Rodríguez Zapatero', role='Expresidente del Gobierno · INVESTIGADO · presunción de inocencia'),
   vid('ar_zapatero_audiencia__01.mp4', 6, at='nulidad')])
N('TOP', "Antes de todo esto, en un mitin, Zapatero había resumido así lo que significa ser socialista.")
C('ul_zapatero_tener_poco__02.mp4', 'José Luis Rodríguez Zapatero', 'Mitin del PSOE', None, None, base=DE)
N('NEW', "[serious] El rescate. Nueve de marzo de dos mil veintiuno. El Consejo de Ministros aprueba cincuenta y tres millones de euros para Plus Ultra, una aerolínea pequeña, con capital venezolano. La Moncloa lo anunció así.",
  [doc('doc_08_plusultra_moncloa_09-03-2021_cabecera.jpg', 'CONSEJO DE MINISTROS · 09/03/2021', ['Rescate de 53 millones a Plus Ultra'], 'La Moncloa'),
   card(type='counter', **{'to': 53, 'label': 'millones de euros para Plus Ultra · 09/03/2021'}, at='cincuenta y tres')])
N('TOP', "Zapatero, en una entrevista en Televisión Española, negó haber intervenido.")
C('clip_14b_no_hable_con_nadie.mp4', 'José Luis Rodríguez Zapatero', 'Entrevista · TVE', 0, 12.8)
N('NEW', "Y el presidente, preguntado por esa entrevista, defendió el expediente.")
C('clip_14c_perifrastica.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 2026', 0, 7.8)
N('TOP', "[serious] Con su mentor ya investigado, el nueve de septiembre, le preguntaron si Zapatero estaría en la campaña.")
C('clip_14a_contar_con_jose_luis.mp4', 'Pedro Sánchez (incluye la pregunta)', 'RESPUESTA REAL · TVE · 09/09/2026', 0, 7.9)
N('NEW', "Y el trece de noviembre, a dieciséis días de las elecciones, en The Wild Project, fue más allá.")
C('clip_14_mano_en_el_fuego.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · The Wild Project · 13/11/2026', 3.7, 12.8)
N('TOP', "[pause] La mano en el fuego. [short pause] Es la misma expresión de confianza que, por otros hombres, ya le había costado cara. En enero de dos mil veinticinco, en Tenerife, dedicó otra a su ministro Ángel Víctor Torres, cuyo nombre aparecía entonces en informaciones de prensa sobre el caso Koldo.",
  [card(type='aviso', lines=['ADEJE · TENERIFE · 26/01/2025'], size=46)])
C('clip_12b_admirador_torres.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso del PSOE de Canarias · 26/01/2025', 0, 13.6)
R('DOC', "Ángel Víctor Torres no ha sido condenado por ningún delito.",
  [card(type='aviso', lines=['Ángel Víctor Torres no ha sido condenado por ningún delito.'])])
N('NEW', "Dentro del partido hubo quien le advirtió. En febrero de este año, en el Ateneo de Madrid, Felipe González dijo que votaría en blanco y que no pensaba irse del PSOE: «Si alguien tiene que dejarlo, que lo deje el que lo destroza». Y el presidente de Castilla-La Mancha, Emiliano García-Page, lo dijo en televisión.",
  [card(type='quote', text='Si alguien tiene que dejarlo, que lo deje el que lo destroza.', attrib='Felipe González · Ateneo de Madrid · 10/02/2026')])
C('clip_20f_page_felipe.mp4', 'Emiliano García-Page', 'El Hormiguero · febrero de 2026', 0, 8.1)
N('TOP', "[serious] La Moncloa respondió que González es solo «una voz más». [pause] Pero había otras voces que el presidente sí escuchaba. Las de sus socios. Y con ellas, la pregunta de si se puede gobernar sin el Parlamento.",
  [card(type='aviso', lines=['LA DEFENSA', 'La Moncloa: Felipe González es «una voz más».'], head=True)])
M('tema', 4)

# =====================================================================================
# PREGUNTA 8 · ¿SE PUEDE GOBERNAR SIN EL PARLAMENTO?
# =====================================================================================
Q(8, '¿Se puede gobernar sin el Parlamento?', 'Presidente, ¿se puede gobernar sin el Parlamento?')
B('pulso')
N('NEW', "La Constitución, en su artículo ciento treinta y cuatro, obliga al Gobierno a presentar cada año los Presupuestos Generales del Estado. "
         "España llega a estas elecciones con los presupuestos de dos mil veintitrés, prorrogados en dos mil veinticuatro, en dos mil veinticinco y en dos mil veintiséis.",
  [ai('constitucion_libro'), card(type='timeline', title='Presupuestos', items=[['2023', 'Últimos aprobados'], ['2024', 'Prorrogados'], ['2025', 'Prorrogados'], ['2026', 'Prorrogados']], at='prorrogados')])
N('TOP', "[serious] Su defensa: la prórroga es legal, también lo dice la Constitución. [pause] Y en septiembre de dos mil veinticuatro, ante el Comité Federal de su partido, el presidente avisó de cómo pensaba gobernar: «con o sin un concurso de un poder legislativo».",
  [card(type='aviso', lines=['LA DEFENSA', 'La prórroga presupuestaria es legal (art. 134.4).'], head=True),
   card(type='quote', text='Vamos a avanzar con determinación, con o sin apoyo de la oposición, con o sin un concurso de un poder legislativo.', attrib='Pedro Sánchez · Comité Federal del PSOE · 07/09/2024', at='septiembre')])
N('NEW', "Diciembre de dos mil veinticuatro. Última sesión de control del año.")
C('clip_36bx_bulo_boe.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 18/12/2024', 0, 9.4)
N('TOP', "El BOE como respuesta. [pause] Para seguir en el poder, el Gobierno necesitaba a sus socios cada semana. Con Esquerra Republicana pactó la condonación de diecisiete mil cien millones de euros de deuda de Cataluña. El Gobierno la defendió como una medida abierta a todas las comunidades.",
  [card(type='counter', **{'to': 17104, 'label': 'millones de euros de deuda condonada pactada con ERC (Cataluña)'}),
   card(type='aviso', lines=['LA DEFENSA', 'El Gobierno: la condonación está abierta a todas las comunidades.'], head=True, at='defendió')])
N('NEW', "Pero Junts ya se había ido. Y desde el Congreso, Míriam Nogueras le recordó al presidente de quién dependía.")
C('ul_nogueras_bloqueada__02.mp4', 'Míriam Nogueras (Junts)', 'Congreso de los Diputados', None, None, base=DE)
N('TOP', "[serious] Con Junts votando junto al Partido Popular y a Vox, el Congreso llegó a aprobar una moción que pedía al presidente someterse a una cuestión de confianza. No era vinculante. No se sometió.",
  [vid('ul_junts_mocion_pp__02.mp4', 4), card(type='aviso', lines=['MOCIÓN APROBADA', 'Pedía al presidente una cuestión de confianza. No era vinculante.'], head=True, at='No era vinculante')])
N('NEW', "El diecinueve de junio de dos mil veintiséis, el presidente aseguró que presentaría presupuestos en dos mil veintiséis y que habría elecciones en dos mil veintisiete. [pause] El cinco de octubre disolvió las Cortes. Elecciones, veintinueve de noviembre.",
  [card(type='dijo', left=dict(date='19/06/2026', text='«Presentaremos los presupuestos y habrá elecciones en 2027»'), right=dict(date='05/10/2026', text='Disolución de las Cortes. Elecciones el 29 de noviembre', source='Fuente: BOE · 06/10/2026')),
   doc('doc_36c_BOE_disolucion_convocatoria_29N_06-10-2026.jpg', 'REAL DECRETO 806/2026', ['Disolución de las Cortes y convocatoria de elecciones'], 'BOE · 06/10/2026', at='disolvió')])
N('TOP', "Al día siguiente, el seis de octubre, la dirigente socialista María Jesús Montero habló de la huelga general convocada para noviembre.")
C('clip_37b_contra_la_oposicion.mp4', 'María Jesús Montero (PSOE)', '06/10/2026', 0, 5.0)
N('NEW', "Una huelga contra la oposición. [short pause] El presidente, en cambio, dijo que no era «una huelga contra nadie». [pause] Pero es un lenguaje que el presidente ya había usado para referirse a una parte de los medios y de las redes. Febrero de dos mil veinticuatro, laSexta.")
C('clip_37f_fachosfera_existe.mp4', 'Pedro Sánchez (incluye la pregunta)', 'RESPUESTA REAL · laSexta · 20/02/2024', 0, 21.6)
N('TOP', "[serious] El nueve de septiembre de dos mil veintiséis, en plena crisis de Ceuta, Santiago Abascal le preguntó en el Congreso si Marruecos le estaba chantajeando. La respuesta del presidente se hizo viral.",
  [ai('congreso_escaño_vacio')])
C('clip_26f_perro_sin_amo.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Congreso · 09/09/2026', 1.5, 11.8)
C('clip_26c_ningun_chantaje.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Mañaneros 360 · TVE · 09/09/2026', 0, 9.2)
N('NEW', "Dos meses antes, en la cumbre de la OTAN en Ankara, Donald Trump había cargado contra España por su gasto militar.")
C('clip_26d_trump_espana.mp4', 'Donald Trump', 'Cumbre de la OTAN · Ankara · 08/07/2026', 0, 11.7)
C('clip_26e_con_creces.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cumbre de la OTAN · Ankara · 08/07/2026', 0, 9.1)
N('TOP', "Horas después, Trump dijo que España se había «redimido por completo». [pause] Y en casa, los socios marcaban su propio rumbo. En enero de este año, en un mitin de Podemos en Zaragoza, Irene Montero celebraba la regularización extraordinaria de inmigrantes.",
  [card(type='aviso', lines=['ZARAGOZA · 31/01/2026'], size=46)])
C('clip_18c_que_voten.mp4', 'Irene Montero (Podemos)', 'Mitin de Podemos · Zaragoza · 31/01/2026', 0, 11.0)
C('clip_18bx_barrer_fachas.mp4', 'Irene Montero (Podemos)', 'Mitin de Podemos · Zaragoza · 31/01/2026', 0, 12.1)
R('DOC', "Días después, dirigentes de Podemos explicaron que aquellas palabras eran irónicas, una burla de la teoría del reemplazo.",
  [card(type='aviso', lines=['LA DEFENSA', 'Podemos: las palabras de Montero eran irónicas.'], head=True)])
N('NEW', "[serious] Gobernar así tiene costes. A veces los paga el propio Gobierno. En abril de dos mil veintitrés, tras cientos de rebajas de condena a agresores sexuales por la ley del solo sí es sí, el presidente pidió perdón a las víctimas.",
  [card(type='aviso', lines=['LEY DEL «SOLO SÍ ES SÍ»'], size=50)])
C('co_si_es_si_perdon__01.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · abril de 2023', None, None, base=DE)
N('TOP', "[softly] Otro perdón. [pause] Y entre perdón y perdón, una promesa que se repitió en todas las campañas. Quizá la que más afecta a la vida diaria. [short pause] La vivienda. Y la economía.",
  [ai('edificio_obra_parada')])
M('tema', 4)

# =====================================================================================
# PREGUNTA 9 · ¿VA LA ECONOMÍA COMO UN COHETE PARA TODOS?
# =====================================================================================
Q(9, '¿Va la economía como un cohete para todos?', 'Presidente, ¿va la economía como un cohete para todos?')
B('pulso')
N('NEW', "Dieciséis de mayo de dos mil veinticuatro. Foro sobre fondos europeos. El presidente presume de datos.")
C('clip_37c_cohete.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · La Moncloa · 16/05/2024', 1.9, 7.1)
N('TOP', "[serious] Los datos que él cita existen. En dos mil veinticinco, el PIB creció un dos coma seis por ciento, según el INE. España superó los veintidós millones de ocupados. Es la defensa de su gestión, y es sólida.",
  [card(type='counter', **{'to': 22460000, 'label': 'ocupados · INE'}), card(type='aviso', lines=['LA DEFENSA', 'PIB +2,6 % en 2025 · más de 22 millones de ocupados (INE)'], head=True, at='defensa')])
N('NEW', "Pero no todos en su propio Gobierno lo vieron igual. Su vicepresidenta segunda, Yolanda Díaz, le contestó en público.")
C('ul_yolanda_cohete__03.mp4', 'Yolanda Díaz', 'Vicepresidenta segunda del Gobierno', None, None, base=DE)
N('TOP', "[serious] Y luego está la vivienda. En el debate del diecinueve de noviembre, el presidente dio esta cifra.")
C('clip_02_millon_viviendas.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0.5, 10.5)
N('NEW', "Un millón de viviendas en ocho años. [pause] Según los datos recopilados por Idealista y publicados por Artículo14, las viviendas terminadas en ese periodo rondan las setecientas cinco mil; unas setecientas cincuenta y dos mil si se cuenta dos mil dieciocho entero. "
         "Y Feijóo le recordó en el debate otra cifra: la vivienda pública estatal entregada frente a la prometida.",
  [card(type='dijo', left=dict(date='19/11/2026', text='«Hemos construido un millón de viviendas»'), right=dict(date='DATOS', text='Unas 705.000 viviendas terminadas (752.000 contando 2018)', source='Fuente: Idealista vía Artículo14 · Maldita.es'), red=True)])
R('DOC', "Feijóo, por su parte, negó haber prometido él mismo un millón de viviendas, aunque la medida ciento cuarenta y cuatro de su programa hablaba de esa cifra.",
  [card(type='aviso', lines=['TAMBIÉN', 'Feijóo negó su propia promesa del millón de viviendas (medida 144 de su programa).'], head=True)])
N('TOP', "Septiembre de dos mil veintiséis. El desahucio de Maricarmen, una vecina de Madrid de ochenta y siete años, abre los informativos. Una cámara le pregunta a quién responsabiliza.",
  [ai('portal_madrid_desahucio_generico')])
C('clip_37g_maricarmen.mp4', 'Maricarmen, vecina desahuciada', 'Imágenes difundidas por ESdiario · septiembre de 2026', 0, 6.7)
N('NEW', "El presidente habló de una tragedia social y pidió apoyo para su decreto de vivienda. En el debate, Feijóo le preguntó si Maricarmen era la persona que le había escrito una carta que no respondió.",
  [card(type='aviso', lines=['LA DEFENSA', 'El presidente pidió apoyo a su decreto de vivienda.'], head=True)])
N('TOP', "[serious] Y para explicar todo esto, en campaña, el presidente eligió sus escenarios. En octubre, en La Revuelta, de Televisión Española, prometió esto.",
  [card(type='aviso', lines=['LA REVUELTA · RTVE · 22/10/2026'], size=46)])
C('clip_06_ire_al_hormiguero.mp4', 'Pedro Sánchez (incluye la pregunta)', 'RESPUESTA REAL · La Revuelta · RTVE · 22/10/2026', 0, 3.9)
N('NEW', "No fue. [short pause] Pablo Motos lo comentó en su programa el once de noviembre.")
C('clip_07_motos_cobardia.mp4', 'Pablo Motos', 'El Hormiguero · 11/11/2026', 0, 5.7)
N('TOP', "En cambio, el presidente sí fue a The Wild Project, y a programas de entretenimiento en otras cadenas. En La Séptima, la colaboradora Alba Carrillo le preguntó por su vida sentimental.",
  [card(type='aviso', lines=['LA DEFENSA', 'Ir a programas de gran audiencia es habitual en campaña.'], head=True, at='entretenimiento')])
C('clip_05_chulazo.mp4', 'Alba Carrillo', 'Fuera de control · La Séptima · 15/11/2026', 0, 5.5)
N('NEW', "Y al día siguiente, en Telecinco, cuando el periodista Carlos Franganillo le apretó con un dato, le respondió así.")
C('clip_05b_mal_informado.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Telecinco · 16/11/2026', 0, 2.0)
N('TOP', "[softly] Mal informado. [pause] Queda una última pregunta. Es la más sencilla de todas. Y él mismo la formuló, palabra por palabra, hace ocho años. [short pause] Solo que entonces se la hizo a otro.",
  [ai('congreso_tribuna_vacia_luz')])
M('tension', 5)

# =====================================================================================
# PREGUNTA 10 · ¿QUÉ DIRÍA EL PEDRO SÁNCHEZ DE 2018?
# =====================================================================================
Q(10, '¿Qué diría el Pedro Sánchez de 2018?', 'Presidente, ¿qué le diría hoy el Pedro Sánchez de dos mil dieciocho?')
B('tema')
N('NEW', "Ocho años. Una pandemia, un volcán, una riada, dos tragedias ferroviarias, una crisis en la frontera de Ceuta. Una amnistía. Tres presupuestos prorrogados. "
         "Un exministro y su asesor, condenados. Su secretario de Organización, investigado. Su mentor, investigado. Su esposa, procesada. Su hermano, condenado en primera instancia. El fiscal general que defendió, condenado. [pause] "
         "Y él, sin imputación alguna. Así lo recuerda siempre. Y es verdad.",
  [card(type='recap', title='Ocho años', items=['Ábalos y Koldo · CONDENADOS', 'Cerdán · INVESTIGADO', 'Zapatero · INVESTIGADO', 'Begoña Gómez · PROCESADA', 'David Sánchez · condena recurrida', 'Fiscal general · CONDENADO', 'Pedro Sánchez · NO IMPUTADO'])])
N('TOP', "[serious] Aquel treinta y uno de mayo de dos mil dieciocho, desde la tribuna del Congreso, Pedro Sánchez le explicó a Mariano Rajoy qué hace un presidente cuando la corrupción llega a su partido.",
  [ai('congreso_tribuna')])
C('clip_38_abalos_decencia_mocion.mp4', 'Pedro Sánchez', 'Moción de censura · Congreso · 31/05/2018', 11.2, 32.7)
N('NEW', "[softly] Aquel día, la moción salió adelante. Rajoy dejó de ser presidente. [pause] Y en el debate de este mes, ocho años y medio después, el presidente que la ganó contestó así a la pregunta de la corrupción.")
C('clip_01b_pido_perdon_corrupcion.mp4', 'Pedro Sánchez', 'RESPUESTA REAL · Cara a cara · RTVE · 19/11/2026', 0, 11.0)
M('nada', 2, [card(type='aviso', lines=[''], size=40)])
N('TOP', "[serious] Pedro Sánchez no ha participado en este documental. Todas sus respuestas son reales, públicas y tienen fecha. Las preguntas eran nuestras. [pause] "
         "Las conclusiones no. [short pause] Esas, el veintinueve de noviembre, son suyas.",
  [AVISO])
U.append(dict(k='T', secs=8.0, sting='golpe', card=dict(type='aviso', head=True, lines=['DOCUVOX', 'Fuentes completas en la descripción.', 'Ninguna encuesta electoral aparece en este documental.'])))
