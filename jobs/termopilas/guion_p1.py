# -*- coding: utf-8 -*-
# Guion de «La batalla de las Termópilas» · parte 1: apertura, contexto, capítulos 1 y 2
from lib import *

# ---------------- APERTURA ----------------
B('tension')
N("[serious] Seguro que la has visto. Trescientos espartanos de capa roja, solos, frenando a un imperio entero. Es la imagen de la película «Trescientos». [short pause] Pero lo que pasó de verdad fue más extraño. Más duro. Y mucho más interesante.",
  ph('Leonidas Thermopylae Jacques-Louis David', src='commons', at='Seguro'),
  ph('Greek hoplite red-figure kylix', src='met,cleveland', at='Trescientos espartanos'),
  ph('Achaemenid Persian soldiers relief Persepolis', src='commons,met', at='un imperio entero'),
  ph('Greek warrior helmet bronze Corinthian', src='met,cleveland', at='Pero lo que pasó'))
N("Agosto del año cuatrocientos ochenta antes de Cristo. Un camino entre la montaña y el mar, tan estrecho que en algunos tramos solo cabía un carro. [short pause] De un lado, el ejército más grande que el mundo había visto. Del otro, unos siete mil griegos.",
  ph('Thermopylae pass landscape', src='commons', at='Agosto', lt=['Las Termópilas', 'Grecia central · 480 a. C.']),
  cd(dict(type='versus', title='Agosto de 480 a. C.', left=dict(name='Los griegos', color=GR, lines=['unos 7.000 hombres', 'de una treintena de ciudades']),
          right=dict(name='El Imperio persa', color=PE, lines=['entre 120.000 y 300.000', 'según los cálculos modernos'])), at='De un lado'))
N("Y al frente de los griegos, un rey de Esparta que ya sabía, porque se lo había dicho un oráculo, que de allí no iba a volver.",
  ph('Spartan hoplite statue Leonidas Sparta museum', src='commons', at='un rey de Esparta', lt=['Leónidas', 'Rey de Esparta', 'griegos']),
  ph('Delphi Temple of Apollo ruins', src='commons', at='un oráculo', lt=['Delfos', 'Santuario de Apolo · hoy']))
N("[serious] ¿Por qué Esparta mandó solo a trescientos de los suyos? ¿Quién enseñó a los persas el camino que nadie vigilaba? [pause] Y la pregunta que lleva veinticinco siglos sin una respuesta sencilla: ¿por qué, la última mañana, un puñado de hombres decidió quedarse a morir?",
  ph('Spartan warrior bronze figurine', src='met,cleveland,commons', at='Por qué Esparta'),
  ph('Kallidromo mountain Thermopylae', src='commons', at='Quién enseñó'),
  ph('dying warrior Greek sculpture Aegina pediment', src='commons,met', at='la última mañana'))
T('La batalla de las Termópilas', 'Tres días que cambiaron la historia', secs=5.5, sting='tema', text='[dramatically] La batalla de las Termópilas.', chapter=False)

# ---------------- CONTEXTO DE ENTRADA ----------------
B('tema')
N("Para entender lo que pasó en aquel desfiladero hay que conocer a dos mundos que estaban a punto de chocar.",
  ph('ancient map Greece Persia Aegean', src='commons', at='dos mundos'))
N("De un lado, Persia: un imperio que iba desde el río Indo, en el actual Pakistán, hasta el mar Egeo, con Egipto, Babilonia y media Asia dentro. Lo gobernaba un solo hombre, el Gran Rey, y en el año cuatrocientos ochenta ese hombre era Jerjes.",
  cd(dict(type='mapfly', title='El Imperio persa', keys=[[20, 20, 75, 45], [20, 24, 70, 44]], points=[
      dict(name='Persépolis', lon=52.89, lat=29.93, at=0.25, pulse=1, big=1), dict(name='Babilonia', lon=44.42, lat=32.54, at=0.45),
      dict(name='Sardes', lon=28.04, lat=38.48, at=0.6), dict(name='Egipto', lon=31.2, lat=30.0, at=0.5)]), at='De un lado, Persia'),
  ph('Xerxes relief Persepolis', src='commons', at='era Jerjes', lt=['Jerjes I', 'Gran Rey de Persia · 486-465 a. C.', 'persas']))
N("Del otro lado, Grecia. Que no era un país, sino cientos de ciudades independientes, las polis, cada una con sus leyes, su ejército y sus rencillas con la vecina. Las dos más poderosas eran Atenas, una democracia con flota, y Esparta, una ciudad que vivía para la guerra.",
  ph('Acropolis Athens Parthenon', src='commons', at='Del otro lado, Grecia', lt=['Atenas', 'hoy']),
  ph('Greek hoplites black-figure amphora', src='met,cleveland', at='cada una con sus leyes'),
  ph('Sparta Taygetus mountains', src='commons', at='Esparta, una ciudad', lt=['Esparta', 'Laconia · hoy']))
N("[serious] Persia ya había intentado conquistar Grecia una vez. En el cuatrocientos noventa, el padre de Jerjes, Darío, envió una expedición que acabó derrotada en Maratón. Diez años después, el hijo volvía para terminar el trabajo. Y esta vez no venía con una expedición: venía con todo el imperio.",
  ph('Darius I Behistun relief', src='commons', at='Darío', lt=['Darío I', 'Gran Rey de Persia · padre de Jerjes', 'persas']),
  ph('Marathon plain Greece', src='commons', at='Maratón', lt=['Maratón', '490 a. C.']),
  ph('Persian archers frieze Susa', src='commons', at='con todo el imperio'))
N("¿Por qué tanto empeño en Grecia? Todo había empezado en la costa de la actual Turquía, en Jonia, donde vivían ciudades griegas sometidas a Persia. En el cuatrocientos noventa y nueve se rebelaron. Atenas les mandó veinte barcos, y en la revuelta los rebeldes quemaron Sardes, una de las capitales del imperio. Heródoto cuenta que Darío ordenó a un sirviente que le repitiera tres veces cada día, antes de comer: «Señor, acuérdate de los atenienses».",
  cd(dict(type='mapfly', title='Jonia', keys=[[20, 35, 32, 42], [25.5, 37.0, 29.5, 39.5]], points=[dict(name='Sardes', lon=28.04, lat=38.48, at=0.4, pulse=1, big=1), dict(name='Mileto', lon=27.28, lat=37.53, at=0.55), dict(name='Atenas', lon=23.73, lat=37.98, at=0.7)]), at='en Jonia'),
  ph('Sardis ruins temple Artemis', src='commons', at='quemaron Sardes', lt=['Sardes', 'capital de Lidia · hoy']),
  K('ACUÉRDATE DE LOS ATENIENSES', 'Darius relief Persepolis', at='Señor, acuérdate'))
N("Estos son los protagonistas de esta historia. Merece la pena retenerlos, porque van a volver una y otra vez.",
  cd(dict(type='cast', title='Los protagonistas', groups=[
      dict(name='Griegos', color=GR, people=[dict(name='Leónidas', role='Rey de Esparta', commons=IMG['leonidas']),
           dict(name='Temístocles', role='General de Atenas', commons=IMG['temistocles']), dict(name='Los tespios', role='Los 700 de Demófilo', commons=IMG['tespios'])]),
      dict(name='Persas', color=PE, people=[dict(name='Jerjes', role='Gran Rey de Persia', commons=IMG['jerjes']),
           dict(name='Los Inmortales', role='Guardia de Hidarnes', commons=IMG['inmortales'])])]), at='Estos son'))
N("[softly] Y hay uno más, el más importante de todos, aunque no luchó. Casi todo lo que sabemos de las Termópilas lo escribió un hombre que nació más o menos el año de la batalla, en Halicarnaso, la actual Bodrum. Se llamaba Heródoto.",
  ph('Herodotus bust', src='commons,met', at='Se llamaba Heródoto', lt=['Heródoto de Halicarnaso', 'Historiador · h. 484-425 a. C.']),
  ph('Bodrum castle Halicarnassus', src='commons', at='Halicarnaso', lt=['Halicarnaso', 'hoy Bodrum, Turquía']))
N("Cuarenta años después de la batalla, Heródoto recorrió Grecia preguntando. Habló con los descendientes, visitó el desfiladero y leyó las inscripciones. A aquel trabajo lo llamó «historia», que en griego significa algo muy sencillo: investigación. [short pause] Y nos dejó una frase que resume este documental.",
  ph('Herodotus Histories manuscript', src='commons', at='recorrió Grecia'),
  K('HISTORIA = INVESTIGACIÓN', 'Herodotus Histories manuscript page', at='investigación'))
R('HER', "«De todos ellos he averiguado los nombres, porque fueron hombres dignos de memoria. Y he averiguado también los nombres de los trescientos.»",
  cd(dict(type='quote', text='He averiguado los nombres de los trescientos.', attrib='Heródoto, Historia VII, 224 · lectura', commons=IMG['herodoto']), at='De todos'))
N("[serious] Vamos a seguir sus pasos. Lo que contó, lo que se le escapó, y lo que la arqueología ha descubierto después.", ph('Thermopylae Leonidas monument', src='commons', at='Vamos a seguir'))
M('tema', 12)

# ---------------- CAPÍTULO 1 · EL IMPERIO QUE CONTABA HOMBRES POR CERCADOS ----------------
T('El imperio que contaba por cercados', 'Capítulo 1', sting='tema', chapter=True)
B('persia')
N("Susa, en el corazón de Persia. Hacia el cuatrocientos ochenta y uno antes de Cristo. Un rey espartano vive aquí, en el palacio de su enemigo. Se llama Demarato. Años antes lo echaron del trono de Esparta con una trampa y huyó a la corte persa. Y ahora se entera de algo que nadie en Grecia sabe todavía.",
  ph('Susa palace Achaemenid', src='commons,met', at='Susa', lt=['Susa', 'capital persa · h. 481 a. C.']),
  ph('Achaemenid palace relief guards', src='commons', at='Se llama Demarato', lt=['Demarato', 'Rey de Esparta en el exilio', 'persas']),
  ph('Persepolis Apadana staircase relief', src='commons', at='Y ahora se entera'))
N("Jerjes ha decidido invadir Grecia. Demarato quiere avisar a su antigua ciudad, pero los caminos están vigilados. Así que coge una tablilla de escribir, de las que se cubrían con cera, le quita la cera, graba el mensaje en la madera y la vuelve a cubrir. A simple vista, es una tablilla en blanco.",
  ph('ancient Greek wax writing tablet', src='met,cleveland,commons', at='coge una tablilla'),
  ai('wax tablet', at='graba el mensaje'))
N("Cuando llega a Esparta, nadie entiende para qué alguien enviaría una tablilla vacía. Nadie, salvo una mujer: Gorgo, la esposa del rey Leónidas. Ella intuye el truco y manda raspar la cera. Debajo está el aviso. Gracias a ella, Esparta supo antes que nadie lo que venía.",
  ph('Spartan woman bronze figurine running girl', src='commons,met', at='una mujer: Gorgo', lt=['Gorgo', 'Reina de Esparta · hija de Cleómenes', 'griegos']),
  D('La tablilla de Demarato', 'tablilla', text='Gorgo descubrió el truco: mandó raspar la cera y encontraron el mensaje escrito en la madera.', source='Heródoto, Historia VII, 239', at='manda raspar'))
N("[serious] ¿Y qué era exactamente «lo que venía»? Para Jerjes, aquella guerra no era una campaña más. Era una deuda familiar. Su padre había perdido en Maratón ante un ejército de ciudadanos atenienses. Para el rey de reyes, eso era una humillación que había que borrar.",
  ph('Persian king relief royal audience', src='commons', at='Para Jerjes'),
  ph('Greek hoplite vase Marathon battle', src='met,cleveland', at='en Maratón'))
N("No todos en la corte estaban de acuerdo. Heródoto cuenta que, cuando Jerjes reunió a los grandes del imperio para anunciar la guerra, solo uno se atrevió a llevarle la contraria: su tío Artábano, hermano de Darío. Le recordó que su padre ya había estado a punto de perder un ejército entero en otra campaña lejana, contra los escitas. Y le advirtió de que los dioses suelen castigar a los que se hacen demasiado grandes.",
  ph('Persepolis nobles relief procession', src='commons', at='su tío Artábano', lt=['Artábano', 'Tío de Jerjes y consejero', 'persas']),
  ph('Scythian warriors gold comb', src='met,commons', at='contra los escitas'))
R('JER', "«Agradece que eres hermano de mi padre. Eso te libra de recibir el pago que merecen tus palabras sin sentido. Y como eres un cobarde, te quedarás aquí, con las mujeres, mientras yo marcho contra Grecia.»",
  cd(dict(type='quote', text='Te quedarás aquí, con las mujeres, mientras yo marcho contra Grecia.', attrib='Jerjes a Artábano, según Heródoto, Historia VII, 11 · lectura', commons=IMG['jerjes']), at='Agradece'))
N("[short pause] Heródoto añade que después Jerjes dudó. Que tuvo un sueño que le ordenaba ir a la guerra, que obligó a su tío a dormir en su cama para ver si el sueño se le aparecía también a él, y que se le apareció. Para Heródoto, aquella guerra estaba escrita. Era el castigo que los dioses preparaban para el orgullo de un rey.",
  ph('Achaemenid royal bed throne relief', src='commons', at='tuvo un sueño'),
  ph('Greek gods Nemesis relief', src='met,cleveland,commons', at='el castigo que los dioses'))
N("Jerjes tardó años en prepararla. Reunió soldados de casi cincuenta pueblos: persas y medos, egipcios, indios, árabes, etíopes. Heródoto los describe uno a uno, con sus armas y sus ropas, como si estuviera viendo un desfile. Y esa variedad la vemos todavía hoy en los relieves de los palacios persas, donde cada pueblo aparece llevando tributo al Gran Rey.",
  ph('Persepolis tribute bearers relief Apadana', src='commons', at='Reunió soldados'),
  ph('Persepolis delegations relief', src='commons', at='Heródoto los describe'),
  ph('Persepolis Apadana relief nations', src='commons', at='en los relieves'))
N("¿Cuántos eran? Heródoto da una cifra precisa: un millón setecientos mil soldados de a pie. Y cuenta cómo los contaron. En una llanura metieron a diez mil hombres apretados, trazaron un círculo a su alrededor y levantaron un cercado de piedra a la altura del ombligo. Después hicieron pasar al ejército entero por el cercado, diez mil cada vez.",
  cd(dict(type='counter', to=1700000, label='soldados de a pie según Heródoto'), at='un millón'),
  ai('enclosure', at='En una llanura'),
  D('Cómo se contó el ejército', 'herodoto_ms', text='Metieron a diez mil hombres, trazaron un círculo y levantaron un muro a la altura del ombligo. Luego llenaron el cercado una y otra vez.', source='Heródoto, Historia VII, 60', at='levantaron un cercado'))
N("[serious] Es una imagen impresionante. Pero ningún historiador de hoy se la cree. Un ejército así no podría haber bebido ni comido en la Grecia de entonces. Los cálculos modernos hablan de entre ciento veinte mil y trescientos mil hombres. Siguen siendo muchísimos: probablemente el ejército más grande reunido hasta entonces.",
  cd(dict(type='split', left=dict(title='Heródoto', lines=['1.700.000 infantes', '80.000 jinetes', 'más de 500.000 marinos']),
          right=dict(title='Historiadores de hoy', lines=['120.000 – 300.000 soldados', 'unas 600 naves de guerra', 'límite: agua y comida']), strike=True), at='Pero ningún historiador'),
  ph('Persian Immortals glazed brick Susa Louvre', src='commons', at='Siguen siendo muchísimos'))
N("Para mover a toda esa gente de Asia a Europa había que cruzar el Helesponto, el estrecho que hoy llamamos de los Dardanelos. Mide algo más de un kilómetro en su parte más estrecha. Jerjes mandó tender dos puentes hechos con cientos de barcos atados unos a otros, con cables de lino y de papiro.",
  cd(dict(type='mapfly', title='El Helesponto', keys=[[20, 35, 32, 43], [25.5, 39.6, 27.4, 40.9]], points=[dict(name='Abidos', lon=26.4, lat=40.2, at=0.4, pulse=1, big=1), dict(name='Sestos', lon=26.38, lat=40.23, at=0.55)]), at='el Helesponto'),
  ph('Dardanelles strait', src='commons', at='los Dardanelos', lt=['Estrecho de los Dardanelos', 'el antiguo Helesponto · hoy']),
  ph('Xerxes bridge of boats Hellespont engraving', src='commons', at='dos puentes'))
N("Pero llegó una tormenta y los destrozó. Y aquí Heródoto cuenta una de las escenas más famosas de la Antigüedad.",
  ph('stormy sea engraving 19th century', src='commons', at='llegó una tormenta'))
R('HER', "«Cuando Jerjes se enteró, montó en cólera y mandó dar al Helesponto trescientos latigazos y arrojar al mar un par de grilletes. Y mandó cortar la cabeza a los encargados de los puentes.»",
  ph('Xerxes lashing the sea illustration', src='commons', at='trescientos latigazos'),
  cd(dict(type='quote', text='Mandó dar al Helesponto trescientos latigazos.', attrib='Heródoto, Historia VII, 35 · lectura', commons=IMG['herodoto']), at='Y mandó cortar'))
N("[short pause] Azotar al mar. Para los griegos que leyeron aquello, era el retrato perfecto de un tirano que se creía por encima de los dioses. Puede que Heródoto exagerara. Pero los puentes se reconstruyeron, más fuertes, y según él el ejército tardó siete días y siete noches en cruzar.",
  ph('Xerxes army crossing Hellespont engraving', src='commons', at='los puentes se reconstruyeron'))
N("Antes de cruzar, en Abidos, junto al estrecho, Jerjes quiso ver a su ejército entero. Le prepararon en una colina un trono de mármol blanco. Desde allí vio el Helesponto cubierto de barcos y las playas y las llanuras llenas de hombres. Primero se sintió dichoso. Y después se echó a llorar.",
  ph('Abydos Dardanelles hill view', src='commons', at='en Abidos', lt=['Abidos', 'orilla asiática del Helesponto']),
  ph('Persian fleet ships ancient engraving', src='commons', at='cubierto de barcos'))
N("Artábano, el tío que se había opuesto a la guerra, le preguntó por qué lloraba un hombre que acababa de llamarse feliz. Y Jerjes le dio una respuesta que no esperaríamos de un tirano.",
  ph('Persepolis Xerxes relief', src='commons', at='le preguntó por qué lloraba'))
R('JER', "«Me he puesto a pensar en lo breve que es la vida humana. De toda esta multitud, dentro de cien años no quedará nadie vivo.»",
  cd(dict(type='quote', text='De toda esta multitud, dentro de cien años no quedará nadie vivo.', attrib='Jerjes en Abidos, según Heródoto, Historia VII, 46 · lectura', commons=IMG['jerjes']), at='Me he puesto'))
N("[pause] Es una de las escenas más extrañas del libro. El hombre que va a azotar al mar es también el que llora pensando en la muerte de sus soldados. Heródoto no escribe sobre monstruos. Escribe sobre personas.",
  ph('Herodotus bust', src='commons,met', at='Heródoto no escribe'))
N("Jerjes hizo algo más, todavía más ambicioso. Doce años antes, una flota persa se había estrellado contra los acantilados del monte Atos, en el norte de Grecia. Para que no volviera a pasar, mandó excavar un canal a través de la península. Dos kilómetros de largo, treinta metros de ancho.",
  ph('Mount Athos peninsula', src='commons', at='monte Atos', lt=['Monte Atos', 'Calcídica, norte de Grecia · hoy']),
  cd(dict(type='mapfly', title='El canal de Jerjes', keys=[[21, 38.5, 26, 41.5], [23.6, 40.2, 24.4, 40.6]], points=[dict(name='Canal de Jerjes', lon=23.93, lat=40.39, at=0.5, pulse=1, big=1)]), at='mandó excavar un canal'))
N("[serious] Durante siglos, muchos pensaron que el canal era otra exageración de Heródoto. Hasta que en los años noventa un equipo británico y griego estudió el subsuelo con sondeos sísmicos y radar. El canal estaba allí, enterrado. Heródoto, esta vez, decía la verdad.",
  cd(dict(type='split', left=dict(title='Lo que contó Heródoto', lines=['un canal a través del Atos', 'para que pasaran dos trirremes']),
          right=dict(title='Lo que encontró la geofísica', lines=['un canal de unos 2 km', 'hoy enterrado bajo los campos']), strike=False), at='Hasta que en los años noventa'),
  ph('Xerxes canal Athos Nea Roda', src='commons', at='estaba allí, enterrado'))
N("En la primavera del cuatrocientos ochenta, el ejército echó a andar. Atravesó Tracia y Macedonia, y las ciudades del norte se fueron rindiendo sin luchar. Jerjes había enviado mensajeros a toda Grecia con una petición que era, en realidad, una orden: tierra y agua.",
  cd(dict(type='mapfly', title='La marcha de Jerjes', keys=[[19, 35, 30, 43], [21, 37.5, 27, 42]], points=[dict(name='Abidos', lon=26.4, lat=40.2, at=0.15), dict(name='Tracia', lon=25.5, lat=41.1, at=0.3), dict(name='Macedonia', lon=22.5, lat=40.8, at=0.5), dict(name='Termópilas', lon=22.56, lat=38.8, at=0.8, pulse=1, big=1)]), at='el ejército echó a andar'),
  K('TIERRA Y AGUA', 'Greek terracotta hydria water jar', at='tierra y agua'))
N("Entregar tierra y agua significaba aceptar al rey persa como señor. Muchas ciudades lo hicieron. Tebas, entre ellas, se inclinó hacia Persia. Los griegos tenían una palabra para eso, «medizar»: ponerse del lado de los medos, como llamaban a los persas.",
  ph('Greek terracotta vessel water jug hydria', src='met,cleveland', at='Entregar tierra y agua'),
  ph('Thebes Greece Cadmea', src='commons', at='Tebas', lt=['Tebas', 'Beocia']))
N("[serious] Solo una treintena de ciudades se juntaron para resistir, con Esparta al mando y Atenas como gran potencia naval. Diez años antes, Atenas y Esparta habían tratado a los mensajeros de Darío de una forma que no se olvida: en Atenas los arrojaron a un barranco, y en Esparta, a un pozo, para que cogieran allí la tierra y el agua que quisieran.",
  ph('Greek alliance hoplites marching vase', src='met,cleveland', at='Solo una treintena'),
  ph('ancient Greek well', src='commons', at='a un pozo'))
N("Atenas, que sabía que sería el primer objetivo, también consultó a Delfos. La primera respuesta fue aterradora: huid al fin del mundo. La segunda dejó una pista oscura: solo una muralla de madera resistiría. Muchos atenienses pensaron en la vieja empalizada de la Acrópolis. Pero un político, Temístocles, sostuvo que la muralla de madera eran los barcos. Y convenció a Atenas de jugárselo todo en el mar.",
  ph('Delphi Treasury of the Athenians', src='commons', at='también consultó a Delfos', lt=['Tesoro de los atenienses', 'Delfos · hoy']),
  K('MURALLA DE MADERA', 'Greek trireme ship vase', at='una muralla de madera'),
  ph('Themistocles bust', src='commons', at='Temístocles', lt=['Temístocles', 'Político y general ateniense', 'griegos']))
N("Esa decisión, tomada antes de las Termópilas, explica todo lo que vino después. Atenas había construido en pocos años una flota de unos doscientos trirremes, los buques de guerra de la época, con la plata de unas minas recién descubiertas. Sin esa flota, el plan griego no habría sido posible.",
  ph('Laurion silver mines ancient', src='commons', at='con la plata', lt=['Minas de Laurio', 'Ática']),
  ph('Athenian silver tetradrachm owl', src='met,cleveland', at='unos doscientos trirremes'))
N("No había marcha atrás. Y la pregunta era dónde parar a un ejército que nadie había parado nunca.",
  ph('Greek mountain pass Thermopylae aerial', src='commons', at='dónde parar'))
M('tension', 14)

# ---------------- CAPÍTULO 2 · ESPARTA ----------------
T('La ciudad sin murallas', 'Capítulo 2', sting='tema', chapter=True)
B('tema')
N("Esparta, en el sur del Peloponeso. Una ciudad sin murallas. Los espartanos decían que sus murallas eran sus hombres. Y para entender lo que pasó en las Termópilas hay que entender cómo se fabricaba a uno de esos hombres.",
  ph('Sparta ancient theatre ruins Taygetus', src='commons', at='Esparta', lt=['Esparta', 'Peloponeso · hoy']),
  K('SIN MURALLAS', 'Sparta Eurotas valley Taygetus', at='Una ciudad sin murallas'))
N("A los siete años, los niños espartanos dejaban a su familia y entraban en la agogé, la educación del Estado. Vivían en grupos, dormían en lechos de juncos que ellos mismos cortaban, pasaban hambre a propósito y aprendían a robar comida sin que los pillaran. Si los pillaban, el castigo no era por robar: era por dejarse coger.",
  ph('Greek boy athlete vase', src='met,cleveland', at='A los siete años'),
  ph('Eurotas river reeds Sparta', src='commons', at='lechos de juncos'),
  ai('boys', at='aprendían a robar'))
N("A los veinte se convertían en soldados. Y a los treinta, si superaban todo aquello, eran ciudadanos de pleno derecho: los «iguales». Comían juntos cada día en comedores comunes y no tenían otro oficio que la guerra. Ni comerciaban, ni cultivaban la tierra.",
  ph('Spartan hoplite bronze figurine', src='commons,met', at='A los veinte'),
  ph('Greek symposium banquet vase', src='met,cleveland', at='Comían juntos'))
N("En campaña se les reconocía de lejos. Llevaban el pelo largo, que cuidaban como un símbolo de hombres libres, y un manto teñido de rojo. Jenofonte, que los conoció bien unas décadas después, escribió que ese color se eligió porque era el que menos se parecía a la ropa de mujer y el más apropiado para la guerra.",
  ph('Spartan warrior bronze long hair', src='met,commons', at='el pelo largo'),
  ph('Xenophon bust', src='commons', at='Jenofonte', lt=['Jenofonte', 'Historiador ateniense · h. 430-354 a. C.']))
N("¿Quién la cultivaba, entonces? Los ilotas. Eran los habitantes de las tierras que Esparta había conquistado, convertidos en siervos del Estado. Había muchos más ilotas que espartanos, quizá siete por cada uno. Y ese miedo permanente a una rebelión explica buena parte de la forma de ser de Esparta.",
  ph('Greek farmers plowing black-figure', src='met,cleveland', at='Los ilotas'),
  cd(dict(type='counter', to=7, label='ilotas por cada espartano, según algunos cálculos antiguos'), at='quizá siete'))
N("[serious] Esparta tenía además una rareza: dos reyes a la vez, de dos familias que decían descender de Heracles. Los reyes mandaban el ejército en la guerra, pero en casa vigilaban cinco magistrados elegidos cada año, los éforos.",
  ph('Heracles black-figure amphora', src='met,cleveland', at='Heracles'),
  cd(dict(type='list', header='Cómo se gobernaba Esparta', items=[['Dos reyes', 'mandan el ejército en campaña'], ['Cinco éforos', 'elegidos cada año, vigilan a los reyes'], ['Gerusía', 'consejo de 28 ancianos y los dos reyes'], ['Asamblea', 'los ciudadanos varones aprueban o rechazan']]), at='dos reyes a la vez'))
N("Los espartanos tenían fama de hablar poco y con mucha intención. Su tierra se llamaba Laconia, y de ahí viene nuestra palabra «lacónico». Cuentan que un rey extranjero les mandó una amenaza: si entro en vuestra tierra, os destruiré. Los espartanos contestaron con una sola palabra: «Si». Es decir: si es que llegas a entrar.",
  ph('Laconia landscape Peloponnese', src='commons', at='Laconia', lt=['Laconia', 'Peloponeso · hoy']),
  K('LACÓNICO', 'Spartan bronze hoplite figurine', at='«lacónico»'))
N("Y las mujeres de Esparta eran también distintas de las del resto de Grecia. Hacían ejercicio, heredaban tierras y opinaban en público, algo que escandalizaba a los atenienses. Cuando una mujer de Atenas le preguntó a Gorgo por qué las espartanas eran las únicas que mandaban sobre sus hombres, Gorgo respondió que era porque eran las únicas que parían hombres.",
  ph('Spartan girl running bronze figurine British Museum', src='commons', at='las mujeres de Esparta'),
  cd(dict(type='quote', text='Somos las únicas que parimos hombres.', attrib='Gorgo, según Plutarco, Dichos de mujeres espartanas'), at='Gorgo respondió'))
N("Uno de esos reyes, en el cuatrocientos ochenta, era Leónidas. Y lo era casi por casualidad. Era el tercer hijo del rey Anaxándridas. Su hermano mayor, Cleómenes, murió sin hijos varones. El segundo, Dorieo, había muerto en Sicilia. Así que la corona acabó en Leónidas, que además estaba casado con la hija de Cleómenes: Gorgo, la mujer de la tablilla.",
  ph('Spartan hoplite marble torso Leonidas', src='commons', at='era Leónidas', lt=['Leónidas', 'Rey de Esparta desde h. 489 a. C.', 'griegos']),
  cd(dict(type='list', header='Cómo llegó al trono', items=[['Cleómenes', 'el mayor: muere sin hijos varones'], ['Dorieo', 'el segundo: muere en Sicilia'], ['Leónidas', 'el tercero: rey y yerno de Cleómenes']]), at='Era el tercer hijo'))
N("Cuando estalló la guerra, los espartanos hicieron lo que hacían siempre ante algo grande: preguntar al oráculo de Delfos. Allí, una sacerdotisa, la Pitia, respondía en nombre del dios Apolo. Y la respuesta que trajeron a Esparta fue terrible.",
  ph('Delphi sanctuary Apollo', src='commons', at='oráculo de Delfos', lt=['Delfos', 'Santuario de Apolo']),
  ph('Pythia oracle Delphi kylix Themis Aegeus', src='commons', at='la Pitia'))
R('DOC', "«Para vosotros, habitantes de la espaciosa Esparta: o vuestra gran ciudad será destruida por los persas, o la tierra de Lacedemonia llorará la muerte de un rey del linaje de Heracles.»",
  cd(dict(type='quote', text='O vuestra ciudad será destruida, o Lacedemonia llorará la muerte de un rey.', attrib='Oráculo de Delfos, según Heródoto, Historia VII, 220'), at='Para vosotros'))
N("[serious] O la ciudad, o el rey. Heródoto está convencido de que Leónidas conocía esta profecía. Y de que, cuando llegó el momento, eligió.",
  ph('Leonidas at Thermopylae David detail', src='commons', at='Heródoto está convencido'))
N("Pero antes faltaba un problema muy espartano. Era verano y se celebraban las Carneas, la gran fiesta en honor de Apolo. Durante la fiesta, la ley prohibía salir a combatir con el ejército completo. Además coincidían los Juegos Olímpicos, con su propia tregua sagrada.",
  ph('Greek festival procession vase Apollo', src='met,cleveland', at='las Carneas'),
  ph('Olympia stadium ancient', src='commons', at='los Juegos Olímpicos', lt=['Olimpia', 'hoy']))
N("[serious] No era la primera vez que pasaba. Diez años antes, cuando Atenas pidió ayuda contra Darío, los espartanos respondieron que no podían salir hasta la luna llena, por motivos religiosos. Llegaron a Maratón al día siguiente de la batalla. Solo pudieron ver los cadáveres de los persas y felicitar a los atenienses. Esta vez no podían permitirse llegar tarde.",
  ph('full moon night sky Greece', src='commons', at='hasta la luna llena'),
  ph('Marathon tumulus Soros', src='commons', at='Llegaron a Maratón', lt=['Túmulo de Maratón', 'tumba de los atenienses caídos · hoy']))
N("Así que Esparta decidió mandar una avanzadilla, para que los aliados vieran que iba en serio y no se pasaran a los persas. El grueso del ejército iría después, al acabar las fiestas. Esa avanzadilla eran los trescientos.",
  ph('Greek hoplites marching black-figure', src='met,cleveland', at='una avanzadilla'),
  K('300', 'Spartan hoplite shield lambda vase', at='Esa avanzadilla eran'))
N("[softly] Y Leónidas los eligió con un criterio que dice mucho. Según Heródoto, escogió a hombres que tuvieran hijos vivos. Si caían, su familia no se extinguiría con ellos.",
  ph('Greek father child farewell vase warrior departure', src='met,cleveland', at='hombres que tuvieran hijos'))
N("De la despedida en Esparta nos ha llegado una frase. No la cuenta Heródoto, sino Plutarco, un autor que escribió casi seis siglos después recogiendo dichos de espartanos famosos. Gorgo le preguntó a su marido qué debía hacer.",
  ph('Plutarch bust Delphi', src='commons', at='Plutarco', lt=['Plutarco', 'Escritor griego · h. 46-120 d. C.']))
R('LEO', "«Casarte con un buen hombre, y tener buenos hijos.»",
  cd(dict(type='quote', text='Cásate con un buen hombre y ten buenos hijos.', attrib='Leónidas a Gorgo, según Plutarco, Moralia 240e'), at='Casarte'))
N("[pause] Es una frase seca, muy espartana. No dice «volveré». Dice lo contrario.",
  ph('Greek warrior departure vase', src='met,cleveland', at='No dice'))
N("Plutarco recoge otra. Cuando los éforos le reprocharon que se llevara tan pocos hombres, Leónidas respondió:",
  ph('Spartan hoplite figurine', src='commons,met', at='los éforos'))
R('LEO', "«Son demasiados para lo que vamos a hacer.»",
  cd(dict(type='quote', text='Son demasiados para lo que vamos a hacer.', attrib='Leónidas, según Plutarco, Dichos de espartanos'), at='Son demasiados'))
N("[serious] Trescientos espartanos. Pero no iban solos. Cada uno iba acompañado de ilotas que cargaban el equipo y que, llegado el momento, también lucharon y murieron. Y por el camino se les fueron uniendo hombres de otras ciudades. Cuando llegaron al desfiladero, eran unos siete mil.",
  cd(dict(type='list', header='Los griegos en las Termópilas', items=[['Esparta', '300 hoplitas y sus ilotas'], ['Arcadia (Tegea, Mantinea…)', '2.120'], ['Corinto', '400'], ['Tespias', '700'], ['Tebas', '400'], ['Fócide y Lócride', '1.000 + el ejército de los locrios'], ['Otras ciudades', 'Fliunte 200, Micenas 80']]), at='no iban solos'),
  cd(dict(type='counter', to=7000, label='griegos en el desfiladero, aproximadamente'), at='unos siete mil'))
N("Ese es el primer mito que hay que matizar. Nunca fueron trescientos contra un millón. Fueron unos siete mil contra un imperio. Que sigue siendo una locura.",
  cd(dict(type='split', left=dict(title='El mito', lines=['300 espartanos', 'contra millones']), right=dict(title='Lo que cuentan las fuentes', lines=['unos 7.000 griegos', 'contra 120.000-300.000']), strike=True), at='el primer mito'))
M('tema', 12)
