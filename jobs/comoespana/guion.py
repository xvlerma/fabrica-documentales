# -*- coding: utf-8 -*-
"""CÓMO FUNCIONA REALMENTE ESPAÑA — guion (locución). Voces: TOP = España, NEW = el mundo, DOC = textos legales.
Cada entrada: (clave, voz, texto). Las unidades T son títulos de capítulo (pausa propia, sin voz salvo el título general).
Modelo de voz: eleven_multilingual_v2 (sin etiquetas entre corchetes)."""
VOICES = {'TOP': 'EtnizbrIk2nKCZCt0zqW', 'NEW': 'gcDsmGjWArnZhxIfcR7d', 'DOC': 'BXtvkfRgOYGPQKVRgufE'}
S = []
def N(key, voice, text): S.append(dict(k='N' if voice != 'DOC' else 'R', key=key, voice=voice, text=' '.join(text.split())))
def T(key, num, title, secs=4.0, voiced=None): S.append(dict(k='T', key=key, num=num, title=title, secs=secs, text=voiced))

# ---------------------------------------------------------------- 0 · GANCHO
N('g1', 'TOP', """Este domingo votan millones de españoles. Imagina que ganas. Eres el más votado de todo el país... y aun así,
podrías no gobernar jamás. Suena raro, pero es perfectamente legal. Y no es teoría: ya ha pasado en España.""")
N('g2', 'NEW', """Y si eso te parece extraño, espera. En Suiza no manda un presidente: gobiernan siete personas a la vez, y la
presidencia cambia de manos cada año. En Andorra hay dos jefes de Estado. Uno es el obispo de Urgell. El otro... es el presidente de Francia.""")
N('g3', 'TOP', """¿Quién manda de verdad en España? ¿Para qué sirve el rey? ¿Adónde van tus impuestos? ¿Y cuánto se decide en Bruselas?
Para entender cómo funciona tu país... hay que dar la vuelta al mundo.""")
T('t0', None, 'CÓMO FUNCIONA REALMENTE ESPAÑA', secs=4.5, voiced='Cómo funciona realmente España.')

# ---------------------------------------------------------------- 1 · GANAR Y NO GOBERNAR
T('t1', 1, 'GANAS Y NO GOBIERNAS')
N('a1', 'TOP', """Empecemos por algo que casi nadie sabe. El domingo no vas a votar al presidente del Gobierno. Su nombre ni siquiera
aparece en tu papeleta. Lo que eliges es una lista de diputados de tu provincia. Trescientos cincuenta en total, que se sientan en el Congreso.""")
N('a2', 'TOP', """Y son ellos quienes eligen al presidente. Para ganar a la primera, el candidato necesita la mayoría absoluta: ciento setenta
y seis votos, la mitad más uno. Si no la consigue, dos días después hay una segunda votación, y entonces le basta con tener más síes que noes.""")
N('a3', 'DOC', """Artículo noventa y nueve de la Constitución: «El candidato propuesto expondrá ante el Congreso de los Diputados el programa
político del Gobierno que pretenda formar y solicitará la confianza de la Cámara».""")
N('a4', 'TOP', """Por eso el más votado puede quedarse fuera: si otros partidos suman más escaños y se ponen de acuerdo, el Gobierno es suyo. Y si
pasan dos meses sin que nadie lo consiga, se repiten las elecciones. Ocurrió en dos mil dieciséis... y otra vez en dos mil diecinueve.""")
N('a5', 'TOP', """Pero, ¿cómo se convierten tus votos en escaños? Aquí entra en escena un jurista belga del siglo diecinueve: Victor D'Hondt.""")
N('a6', 'TOP', """Imagina una provincia con cinco escaños y cinco partidos. El partido A saca cuarenta mil votos; el B, treinta mil; el C, dieciocho mil;
el D, nueve mil; y el E, dos mil quinientos. Primera regla: quien no llega al tres por ciento de los votos de la provincia, se queda fuera. Adiós, partido E.""")
N('a7', 'TOP', """Ahora, los votos de cada partido se dividen entre uno, entre dos, entre tres... y los cinco números más altos se llevan los escaños.
Cuarenta mil: escaño para A. Treinta mil: para B. Veinte mil, que es A entre dos: segundo escaño para A. Dieciocho mil: para C. Y quince mil:
segundo para B. Resultado: dos, dos y uno. ¿Y el partido D, con casi uno de cada diez votos? Cero.""")
N('a8', 'TOP', """Y aquí viene lo sorprendente. Cada provincia tiene al menos dos diputados, sea grande o pequeña, y el resto se reparte por población.
Soria, con unos noventa mil habitantes, elige dos: uno por cada cuarenta y cinco mil personas. Madrid, con más de siete millones, elige treinta y ocho:
uno por cada ciento ochenta y ocho mil. Un escaño de Soria representa a cuatro veces menos gente que uno de Madrid.""")
N('a9', 'NEW', """Ahora, otro país. En el Reino Unido no hay listas. El país se divide en seiscientos cincuenta distritos, y en cada uno gana un solo
diputado: el que tenga más votos, aunque sea por uno. Los demás votos de ese distrito no se traducen en nada. En dos mil veinticuatro, los laboristas
lograron casi dos de cada tres escaños con apenas un tercio de los votos.""")
N('a10', 'NEW', """Francia lo hace en dos vueltas. Si nadie arrasa en la primera, una semana después se vota otra vez, solo entre los candidatos
más votados, y los partidos negocian quién se retira. Puedes quedar segundo el primer domingo... y ganar el siguiente.""")
N('a11', 'NEW', """Mira lo que ocurre con exactamente los mismos votos en los tres sistemas. El reparto de escaños cambia por completo. El sistema
electoral no es un detalle técnico: puede decidir quién gobierna.""")
N('a12', 'NEW', """Y luego está Estados Unidos. Allí, al presidente no lo eligen directamente los ciudadanos, sino quinientos treinta y ocho
electores. Cada estado tiene los suyos y, en casi todos, quien gana el estado se los lleva todos. Hacen falta doscientos setenta. En dos mil dieciséis,
Hillary Clinton sacó casi tres millones de votos más que Donald Trump... y perdió. Ha pasado cinco veces en su historia.""")
N('a13', 'TOP', """Así que tu voto no elige directamente a quien manda. Pero entonces, en España... ¿quién manda de verdad? ¿El presidente... o el rey?""")

# ---------------------------------------------------------------- 2 · REY O PRESIDENTE
T('t2', 2, '¿QUIÉN MANDA: EL REY O EL PRESIDENTE?')
N('b1', 'DOC', """Artículo uno, apartado tres: «La forma política del Estado español es la Monarquía parlamentaria».""")
N('b2', 'TOP', """Traducido: en España hay dos cargos distintos. El jefe del Estado, que es el rey: representa al país, sanciona las leyes y, tras
hablar con los partidos, propone un candidato a presidente. Y el jefe del Gobierno, que es quien gobierna. El rey reina, pero no gobierna. Sus actos
necesitan la firma de otro, del presidente o de un ministro, que es quien responde por ellos. Se llama refrendo.""")
N('b3', 'NEW', """En otros países, estos papeles se reparten de otra forma. En Estados Unidos, el presidente es a la vez jefe del Estado y jefe del
Gobierno. En Francia, el poder se comparte entre un presidente elegido por los ciudadanos, con mucho poder, y un primer ministro. En Alemania, el
presidente tiene un papel casi ceremonial y quien gobierna es el canciller. Y en Suiza, el jefe del Estado no es una persona: son los siete miembros del
Consejo Federal, juntos.""")
N('b4', 'NEW', """Las monarquías tampoco son todas iguales. Hay reyes que reinan, como los de España, Suecia o el Reino Unido. Y hay reyes que
gobiernan: en Arabia Saudí, el rey concentra todo el poder del Estado, y no existe un parlamento elegido por los ciudadanos.""")
N('b5', 'NEW', """Y aquí va una curiosidad. El rey del Reino Unido no es solo rey del Reino Unido. También es rey de Canadá, de Australia, de Nueva
Zelanda, de Jamaica... En total, de quince países independientes, cada uno con su propio gobierno.""")
N('b6', 'TOP', """Ahora bien: si el rey no gobierna y el presidente sí... ¿quién le pone límites a quien gobierna?""")

# ---------------------------------------------------------------- 3 · REGLAS Y QUIÉN VIGILA
T('t3', 3, 'LAS REGLAS DEL JUEGO')
N('c1', 'TOP', """Las reglas están en la Constitución. Se aprobó en referéndum el seis de diciembre de mil novecientos setenta y ocho, y tiene ciento
sesenta y nueve artículos. Lo curioso es lo poco que ha cambiado: en casi cuarenta y ocho años, solo cuatro reformas. La última, este mismo año, para
que Formentera elija su propio senador.""")
N('c2', 'NEW', """El Reino Unido, en cambio, ni siquiera tiene una Constitución escrita en un solo texto. Sus reglas están repartidas en leyes,
sentencias y costumbres de siglos. Nueva Zelanda, tampoco.""")
N('c3', 'TOP', """¿Y quién vigila que nadie se la salte? En España hay dos tribunales que se confunden a menudo. El Tribunal Supremo está en la cima de
los jueces: juzga delitos, pleitos y recursos. El Tribunal Constitucional no juzga a personas: decide si una ley choca con la Constitución y protege los
derechos fundamentales. Tiene doce magistrados, propuestos por el Congreso, el Senado, el Gobierno y el Consejo General del Poder Judicial.""")
N('c4', 'NEW', """Y en Estados Unidos pasa algo que aquí sería impensable: en treinta y ocho estados, los jueces del tribunal supremo estatal pasan
por las urnas. Hacen campaña, recaudan donaciones... y algunos hasta salen en anuncios de televisión.""")
N('c5', 'TOP', """Pero, ¿qué pasa si el Congreso quiere echar al presidente a mitad de mandato? ¿Se puede?""")

# ---------------------------------------------------------------- 4 · ECHAR A UN PRESIDENTE
T('t4', 4, 'CÓMO ECHAR A UN PRESIDENTE')
N('d1', 'TOP', """Se puede. Se llama moción de censura, y tiene un truco: no basta con estar en contra. Hay que proponer a otro candidato, y que
ese candidato consiga la mayoría absoluta, ciento setenta y seis votos. Si lo logra, se convierte en presidente en ese mismo momento. En democracia
ha habido seis mociones de censura. Solo una salió adelante, en dos mil dieciocho.""")
N('d2', 'NEW', """En Estados Unidos, el camino se llama impeachment. La Cámara de Representantes acusa y el Senado juzga, y para destituir hacen
falta dos tercios de los senadores. Cuatro veces se ha juzgado así a un presidente. Ninguno fue destituido.""")
N('d3', 'NEW', """En Corea del Sur, en cambio, la última palabra la tiene el Tribunal Constitucional, y ya lo ha hecho dos veces: destituyó a
Park Geun-hye en dos mil diecisiete y a Yoon Suk Yeol en dos mil veinticinco, después de que declarara la ley marcial.""")
N('d4', 'TOP', """Hasta aquí, el poder central. Pero en España hay muchos más gobiernos de los que crees.""")

# ---------------------------------------------------------------- 5 · UN PAÍS DENTRO DE OTRO
T('t5', 5, 'UN PAÍS DENTRO DE OTRO PAÍS')
N('e1', 'TOP', """Diecisiete comunidades autónomas, más Ceuta y Melilla, cada una con sus propias instituciones. Las comunidades gestionan buena parte
de lo que más usas: hospitales, colegios, servicios sociales. Por eso tu centro de salud no depende del Gobierno central, sino de tu comunidad. Y el
País Vasco y Navarra van más allá: recaudan casi todos sus impuestos y pagan al Estado una cantidad pactada.""")
N('e2', 'NEW', """En la Constitución, España no se define como un Estado federal, aunque en muchas cosas se le parece. Alemania sí lo es: dieciséis
estados, los länder, con tanto peso que participan en buena parte de las leyes federales. Estados Unidos tiene cincuenta estados, que deciden hasta si
aplican la pena de muerte. Y Suiza tiene veintiséis cantones, y sus ciudadanos votan en referéndum varias veces al año.""")
N('e3', 'TOP', """Y todo eso, hospitales, colegios, pensiones, hay que pagarlo. ¿Con qué? Con tu dinero.""")

# ---------------------------------------------------------------- 6 · TUS 100 €
T('t6', 6, '¿ADÓNDE VAN TUS CIEN EUROS?')
N('f1', 'TOP', """Imagina que todo lo que gastan las administraciones públicas fueran cien euros. Con los últimos datos completos de Hacienda, los de
dos mil veinticuatro: cuarenta y uno van a protección social, sobre todo pensiones, pero también desempleo y otras ayudas. Catorce, a sanidad. Trece, a
servicios generales, donde están los intereses de la deuda. Once, a asuntos económicos: carreteras, transporte, apoyo a empresas. Nueve, a educación.
Cuatro, a seguridad y justicia. Y el resto, a cultura, medio ambiente, defensa y vivienda.""")
N('f2', 'TOP', """Fíjate en un detalle: solo en intereses de la deuda se van más de cinco euros de cada cien. Más que en defensa y medio ambiente juntos.""")
N('f3', 'TOP', """Porque las administraciones españolas deben alrededor de un billón setecientos cincuenta mil millones de euros: más o menos todo lo
que produce el país en un año. ¿A quién se lo debemos? Casi la mitad de la deuda del Estado está en manos de inversores extranjeros. El segundo gran
acreedor es el propio sistema del euro, a través del Banco de España. Y el resto, bancos, aseguradoras, fondos... y ciudadanos que compran letras del Tesoro.""")
N('f4', 'NEW', """¿Pagamos mucho o poco? Depende de con quién te compares. En España, impuestos y cotizaciones suman cerca del treinta y siete por
ciento de todo lo que produce el país. En Dinamarca, más del cuarenta y cinco: el récord de la OCDE. Y en países del golfo Pérsico, como Emiratos o
Arabia Saudí, no hay impuesto sobre la renta: el Estado vive, sobre todo, del petróleo y del gas.""")
N('f5', 'TOP', """Pero hay decisiones que ni siquiera se toman en Madrid. Se toman a más de mil trescientos kilómetros.""")

# ---------------------------------------------------------------- 7 · BRUSELAS
T('t7', 7, '¿CUÁNTO MANDA BRUSELAS?')
N('h1', 'NEW', """En la Unión Europea, España comparte parte de sus decisiones con otros veintiséis países. Algunas normas europeas, los reglamentos,
se aplican directamente en toda la Unión, sin que el Congreso tenga que votarlas. Otras, las directivas, fijan un objetivo y obligan a cada país a
adaptar sus leyes. Y si una ley española choca con el derecho europeo en un asunto que es de la Unión, prevalece el europeo.""")
N('h2', 'NEW', """El euro lo usan ya veintiún países, desde que Bulgaria se sumó en enero. Por eso los tipos de interés, los que encarecen o
abaratan tu hipoteca, no se deciden en Madrid, sino en Fráncfort, en el Banco Central Europeo.""")
N('h3', 'NEW', """Salir es posible: el Reino Unido lo hizo. El Brexit se consumó el treinta y uno de enero de dos mil veinte, más de tres años y
medio después del referéndum. Y por encima de todo está la ONU: en su Consejo de Seguridad, cinco países, Estados Unidos, China, Rusia, Reino Unido y
Francia, pueden tumbar una resolución con un solo voto en contra. España, no.""")
N('h4', 'TOP', """Hasta ahora, sistemas más o menos parecidos. Pero en el mundo hay países con reglas que parecen inventadas.""")

# ---------------------------------------------------------------- 8 · LOS MÁS RAROS Y CIERRE
T('t8', 8, 'LOS GOBIERNOS MÁS RAROS DEL MUNDO')
N('i1', 'NEW', """San Marino tiene dos jefes de Estado a la vez, los capitanes regentes. Y los cambia cada seis meses: el uno de abril y el uno de
octubre. Lo hace desde la Edad Media.""")
N('i2', 'NEW', """En Malasia, el rey se elige. Nueve sultanes, cada uno soberano de su propio estado, eligen entre ellos a uno para cinco años, y el
trono va rotando.""")
N('i3', 'NEW', """El Vaticano es una monarquía absoluta... y electiva: su soberano es el papa, elegido por los cardenales en el cónclave.""")
N('i4', 'NEW', """En Liechtenstein, el príncipe puede vetar leyes y destituir al Gobierno. Y lo más curioso: esos poderes los amplió un referéndum,
en dos mil tres. En dos mil doce, los votantes se negaron a recortárselos.""")
N('i5', 'NEW', """Y en Bután, en el Himalaya, fue la propia monarquía la que llevó al país a la democracia. Su Constitución, de dos mil ocho, obliga
al rey a retirarse a los sesenta y cinco años. Y el país presume de medir su éxito con la Felicidad Nacional Bruta.""")
N('i6', 'TOP', """Ahora vuelve a España. El domingo, cuando metas el sobre en la urna, ya sabes lo que pasa después. Tu voto se suma en tu provincia.
La ley D'Hondt lo convierte en escaños. Los diputados eligen a un presidente... o no. El rey sanciona, pero no decide. El Constitucional vigila. Tu
comunidad gestiona tu hospital. Y una parte de las reglas se escribe en Bruselas.""")
N('i7', 'TOP', """Ningún sistema es perfecto. Cada país ha elegido el suyo, con sus ventajas y sus costes. Ahora ya sabes por qué España funciona
así. Lo que hagas con tu voto... es cosa tuya.""")

if __name__ == '__main__':
    import collections
    ch = sum(len(u['text'] or '') for u in S); w = sum(len((u['text'] or '').split()) for u in S)
    by = collections.Counter()
    for u in S:
        if u.get('text'): by[u.get('voice', 'TOP')] += len(u['text'].split())
    print('caracteres', ch, 'palabras', w, 'min≈', round(w / 125, 1), dict(by), {k: round(v / w * 100) for k, v in by.items()})
