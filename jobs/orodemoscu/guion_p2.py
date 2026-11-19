# -*- coding: utf-8 -*-
# «El oro de Moscú» · parte 2: capítulos 3 y 4 y recapitulación
from lib import *

# ---------------- CAPÍTULO 3 ----------------
T('Tres noches en La Algameca', 'Capítulo 3', secs=5.0, text='[serious] Capítulo tres. [short pause] Tres noches en La Algameca.')
B('noche')
DER("Cartagena, veintidós de octubre de mil novecientos treinta y seis. Anochece. Por la carretera de la costa avanza una columna de veinte camiones de cinco toneladas. Delante, en un coche, va Alexander Orlov. A su lado, un alto funcionario del Tesoro español que, según Orlov, no podía disimular los nervios.",
    ph('Cartagena coast road 1930s', at='Cartagena, veintidós', lt=['Cartagena', '22 de octubre de 1936']),
    ai('convoy', 'trucks convoy night 1930s', at='veinte camiones'),
    ph('Alexander Orlov 1930s', at='Alexander Orlov'))
DER("Ese funcionario era, casi con seguridad, Francisco Méndez Aspe, director general del Tesoro y hombre de total confianza de Negrín. Él sería el responsable español de la entrega.",
    ph('Spanish Ministry of Finance 1936', at='Francisco Méndez Aspe', lt=['Francisco Méndez Aspe', 'Director general del Tesoro', 'izquierda']))
IZQ("Cartagena era entonces el corazón de la Armada republicana. La mayor parte de la flota se había quedado con el Gobierno, y la base estaba llena de marinos, obreros del arsenal y, desde hacía pocos días, de técnicos soviéticos que descargaban los primeros envíos de armas.",
    ph('Spanish Republican Navy fleet Cartagena 1936', at='el corazón de la Armada'),
    ph('Cartagena arsenal workers 1930s', at='obreros del arsenal'))
IZQ("¿Y quién conducía los camiones? Aquí está uno de los detalles más llamativos. Según el propio Orlov, eran tanquistas soviéticos recién llegados a España. Hombres que no hablaban español, que no conocían a nadie en Cartagena y que no podían contar nada.",
    ai('drivers', 'Soviet tank crew 1936 Spain', at='tanquistas soviéticos'),
    ph('T-26 tank crew Spain 1936', at='no hablaban español'))
DER("Llegan a los polvorines excavados en la montaña. Dentro esperan sesenta marineros españoles. Y apiladas contra las paredes, miles de cajas de madera, todas iguales. Cada una pesa unos sesenta y cinco kilos. Dentro hay monedas, lingotes, hasta virutas de oro.",
    ph('La Algameca polvorines Cartagena', at='polvorines excavados', lt=['La Algameca', 'polvorines de la Armada']),
    ai('crates', 'wooden crates stacked tunnel', at='miles de cajas'),
    ph('gold coins sack', at='monedas, lingotes'))
IZQ("[softly] Los marineros cargan las cajas a mano, una a una, hasta los camiones. Los camiones bajan al muelle. Y en el muelle, las cajas pasan a las bodegas de los barcos soviéticos. Así, durante tres noches seguidas. Sin luces. Con el miedo constante a un bombardeo.",
    ai('loading', 'sailors loading crates night port', at='cargan las cajas'),
    ph('Cartagena dock 1930s', at='al muelle'),
    ph('Spanish Civil War air raid night', at='un bombardeo'))
DER("Orlov contó después que, durante una de esas noches, sonó una alarma aérea en Cartagena. Y que lo que le obsesionaba era que una bomba alcanzara un camión cargado de oro, en mitad de la carretera, a la vista de todos.",
    ph('Cartagena air raid 1936', at='alarma aérea'),
    ai('coins road', 'gold coins scattered', at='a la vista de todos'))
M('noche', 9)
DER("[serious] El veinticinco de octubre todo está a bordo. Cuatro buques soviéticos: el Kim, el Kursk, el Neva y el Volgolés. En total, siete mil ochocientas cajas.",
    ph('Soviet cargo ship 1930s', at='Cuatro buques soviéticos'),
    cd(dict(type='list', header='El reparto del oro, 25 de octubre de 1936', items=[['Neva', '2.697 cajas'], ['Kim', '2.100 cajas'], ['Kursk', '2.020 cajas'], ['Volgolés', '983 cajas']]), at='el Kim'))
DER("Siete mil ochocientas. Esa es la cifra española. Pero Orlov, en su relato, da otra: siete mil novecientas. Cien cajas más. [pause] Cien cajas son seis toneladas y media de oro.",
    cd(dict(type='split', left=dict(title='Cifra española', lines=['7.800 cajas']), right=dict(title='Cifra de Orlov', lines=['7.900 cajas'])), at='Pero Orlov'),
    cd(dict(type='counter', to=6500, label='kilos: lo que pesan 100 cajas'), at='seis toneladas y media'))
IZQ("Los historiadores que han revisado la documentación del depósito en Moscú no encuentran esas cien cajas. Lo más probable es que Orlov se equivocara al recordar, treinta años después. El acta soviética coincide con la española.",
    ph('Spanish Civil War archive documents', at='la documentación del depósito'),
    K('7.800', 'archive ledger page', at='coincide con la española'))
DER("Es lo más probable. Pero fíjate en el problema: para saber cuánto oro salió de verdad, dependemos de dos fuentes. El acta que firmaron los soviéticos, y el recuerdo de un agente de la NKVD. [short pause] El recibo que habría permitido comprobarlo en Cartagena no existe. Se negaron a darlo.",
    ph('Soviet official document stamp', at='El acta que firmaron'),
    K('SIN RECIBO EN CARTAGENA', 'Cartagena port night', at='no existe'))
DER("Y hay otro detalle del relato de Orlov que retrata la operación entera. Para los españoles, él no era un agente de la NKVD. Se presentó con un nombre falso, Blackstone, como si fuera un representante de la banca extranjera. Los marineros que cargaban las cajas no sabían quién era el hombre que daba las órdenes.",
    ai('blackstone', 'man in coat silhouette night 1930s', at='un nombre falso'),
    K('«MR. BLACKSTONE»', 'Cartagena night 1936', at='Blackstone'))
IZQ("Tampoco sabían adónde iba el oro. Y eso, en plena guerra y con espías de los dos bandos en todos los puertos, era exactamente lo que se pretendía. Si los sublevados se hubieran enterado del día y de la ruta, habrían intentado interceptar los barcos.",
    ph('Spanish Civil War spy 1936', at='espías de los dos bandos'),
    ph('Nationalist cruiser Canarias 1936', at='interceptar los barcos'))
IZQ("Con el oro viajaron cuatro empleados del Banco de España, los llamados claveros, los responsables de las llaves de la cámara. Su misión era vigilar el cargamento hasta el final. [short pause] Su viaje iba a durar mucho más de lo que imaginaban.",
    ph('Banco de España employees 1930s', at='cuatro empleados', gloss=['claveros', 'empleados del Banco que custodiaban las llaves del oro']),
    ph('ship deck 1930s sea', at='Su viaje'))
DER("Los barcos zarpan hacia el este. Atraviesan el Mediterráneo, pasan los Dardanelos y el Bósforo, y entran en el mar Negro. Navegan con todas las precauciones, porque el Mediterráneo está lleno de buques de guerra italianos.",
    cd(dict(type='mapfly', title='Cartagena → Odesa', points=[dict(name='Cartagena', lon=-0.98, lat=37.60, at=0.1, big=1), dict(name='Estambul', lon=28.98, lat=41.01, at=0.6), dict(name='Odesa', lon=30.73, lat=46.48, at=0.85, pulse=1, big=1)]), at='hacia el este'),
    ph('Bosphorus 1930s ship', at='el Bósforo'),
    ph('Italian navy cruiser 1930s', at='buque de guerra italiano'))
IZQ("El miedo no era exagerado. La Italia de Mussolini tenía buques y submarinos en la zona, y muy pronto empezaría a atacar a los barcos que llevaban suministros a la República. Si el oro caía en manos italianas, acababa en las de Franco.",
    ph('Italian submarine 1930s', at='con submarinos'),
    ph('Mussolini 1936', at='La Italia de Mussolini'))

# ---------------- CAPÍTULO 4 ----------------
T('Odesa', 'Capítulo 4', secs=5.0, text='[serious] Capítulo cuatro. [short pause] Odesa.')
B('rusia')
DER("Odesa, puerto soviético del mar Negro. Entre el dos y el seis de noviembre de mil novecientos treinta y seis van llegando los barcos. El Kursk se retrasa unos días por una avería. Nadie en España lo sabe todavía, pero el Gobierno de la República se está marchando de Madrid a Valencia esa misma semana.",
    ph('Odessa port 1930s', at='Odesa, puerto', lt=['Odesa', 'noviembre de 1936']),
    ph('Odessa harbour ships 1930s', at='van llegando los barcos'),
    ph('Valencia 1936 government', at='a Valencia'))
IZQ("En el puerto espera un despliegue enorme. Soldados de la NKVD acordonan el muelle. Los propios agentes descargan las cajas y las suben a un tren especial. Destino: Moscú.",
    ph('Odessa port Potemkin stairs 1930s', at='En el puerto espera'),
    ai('train', 'Soviet train 1930s steam', at='un tren especial'))
DER("El tren cruza Ucrania hacia el norte, más de mil trescientos kilómetros, con escolta armada en cada vagón. Es el último tramo del viaje. A partir de aquí, el oro de España ya no estará nunca más al alcance de un español.",
    cd(dict(type='mapfly', title='Odesa → Moscú', points=[dict(name='Odesa', lon=30.73, lat=46.48, at=0.15, big=1), dict(name='Kiev', lon=30.52, lat=50.45, at=0.45), dict(name='Moscú', lon=37.62, lat=55.75, at=0.85, pulse=1, big=1)]), at='cruza Ucrania'),
    ph('Soviet steam train 1930s snow', at='escolta armada'))
DER("Según contaría Orlov, Stalin celebró la llegada del oro con una cena para los jefes de la NKVD. Y allí pronunció una frase que se ha repetido mil veces. Hay que advertirlo: solo la conocemos por Orlov, y no hay ningún documento que la confirme.",
    ph('Stalin 1936', at='Stalin celebró'),
    ph('Kremlin banquet hall', at='una cena'))
V('ORL', "«Los españoles no volverán a ver su oro, igual que no pueden verse sus propias orejas.»",
  Q('Los españoles no volverán a ver su oro, igual que no pueden verse sus propias orejas.', 'Frase atribuida a Stalin por Alexander Orlov · sin confirmación documental', at='Los españoles', img='stalin'))
DER("¿Y quién era Orlov para contar todo esto? En mil novecientos treinta y ocho, cuando las purgas de Stalin empezaron a alcanzar a sus propios compañeros, huyó de España con su familia y desapareció en Estados Unidos. Escribió a Stalin una carta: si le dejaban en paz, callaría. Y calló. No publicó nada hasta que Stalin murió, en mil novecientos cincuenta y tres.",
    ph('Alexander Orlov 1950s', at='huyó de España'),
    ph('Stalin funeral 1953', at='Stalin murió'))
DER("Dos años después declaró ante el Senado de Estados Unidos. Y más tarde contó la operación del oro con todo detalle. [short pause] Es un testigo directo. Pero también es un desertor que vivió de sus secretos. Por eso cada cosa que cuenta hay que contrastarla.",
    ph('United States Senate hearing 1955', at='el Senado de Estados Unidos', lt=['Senado de EE. UU.', 'septiembre de 1955']),
    K('TESTIGO DIRECTO', 'Alexander Orlov portrait', at='testigo directo'))
IZQ("[serious] Es una frase redonda, y por eso conviene desconfiar de ella. La propaganda de Franco la convirtió en la prueba de que Stalin había robado el oro. Pero una frase atribuida en unas memorias no es una prueba.",
    ph('Francoist propaganda poster', at='La propaganda de Franco'),
    K('¿PRUEBA O LEYENDA?', 'Stalin portrait', at='no es una prueba'))
DER("Tienes razón: no es una prueba. Lo que sí es prueba es lo que pasó con los cuatro claveros. No les dejaron volver a España. La Unión Soviética los retuvo durante mucho tiempo, y cuando por fin pudieron salir, fue lejos de España.",
    ph('Moscow 1937 street', at='los cuatro claveros'),
    K('RETENIDOS', 'Moscow winter 1937', at='los retuvo'))
DER("Eran los únicos españoles que habían visto el oro llegar. Y los únicos que podían contar, de primera mano, cómo se trataba.",
    ph('Gokhran Moscow', at='visto el oro llegar'))
M('rusia', 9)
IZQ("En Moscú, el oro se guarda en el Gojrán, el depósito de metales preciosos del Estado soviético. Y empieza el recuento. Caja a caja. Moneda a moneda. Había que separar el oro por países, por épocas, por calidad.",
    ph('Gokhran precious metals depository Moscow', at='el Gojrán', lt=['Gojrán', 'Depósito estatal de metales preciosos · Moscú'], gloss=['Gojrán', 'depósito de metales preciosos del Estado soviético', 'urss']),
    ai('counting', 'counting gold coins hands', at='Moneda a moneda'))
IZQ("El recuento dura tres meses. Y se hace con un cuidado extraordinario. Se pesó y se clasificó cada partida, y todo quedó por escrito. Para Viñas, eso demuestra que la operación fue un depósito bancario en regla, no un saqueo.",
    cd(dict(type='timeline', header='Del puerto al recibo', events=[['25 oct 1936', 'Salen de Cartagena'], ['2-6 nov 1936', 'Llegan a Odesa'], ['nov-ene', 'Recuento en Moscú'], ['5 feb 1937', 'Acta de depósito']]), at='tres meses'),
    ph('gold coins inspection', at='Se pesó'))
DER("[serious] El cinco de febrero de mil novecientos treinta y siete se firma el acta definitiva. Por España, el embajador Marcelino Pascua. Por la Unión Soviética, el comisario de Finanzas, Grinko, y el vicecomisario de Asuntos Exteriores, Krestinski.",
    ph('Marcelino Pascua', at='Marcelino Pascua', lt=['Marcelino Pascua', 'Embajador de la República en Moscú', 'izquierda']),
    ph('Grigory Grinko', at='Grinko', lt=['Grigori Grinko', 'Comisario del Pueblo de Finanzas', 'urss']),
    ph('Nikolay Krestinsky', at='Krestinski', lt=['Nikolái Krestinski', 'Vicecomisario de Asuntos Exteriores', 'urss']))
V('DOC', "Quinientos diez millones setenta y nueve mil quinientos veintinueve gramos de oro en bruto. Una vez descontada la aleación de las monedas, unas cuatrocientas sesenta toneladas de oro puro.",
  DOCC('Acta de depósito · Moscú, 5 de febrero de 1937', '510.079.529,3 gramos de oro en bruto', 'Acta de recepción del oro español', at='Quinientos diez millones'),
  cd(dict(type='counter', to=460, label='toneladas de oro fino, según Martín Aceña'), at='cuatrocientas sesenta'))
IZQ("Y conviene recordar qué había dentro de esas cajas. Según el documento de entrega, quince mil quinientos setenta y un sacos de monedas de oro de muchos países, sesenta y cuatro lingotes y cuatro paquetes de virutas. Casi todo eran monedas, que había que fundir o vender.",
    cd(dict(type='list', header='Contenido del cargamento', items=[['15.571', 'sacos de monedas de oro'], ['64', 'lingotes'], ['4', 'paquetes de virutas']]), at='quince mil'))
IZQ("Pascua era médico, como Negrín, y socialista. Durante meses fue el único representante español en Moscú, y el encargado de vigilar que cada orden de venta se cumpliera. Su correspondencia es hoy una de las fuentes principales para reconstruir qué se hizo con el oro.",
    ph('Marcelino Pascua portrait', at='Pascua era médico'))
DER("Al precio de entonces, más de quinientos millones de dólares. Hoy, ese oro valdría decenas de miles de millones de euros. [short pause] Fíjate en un detalle: Grinko y Krestinski, los dos hombres que firmaron el recibo por parte soviética, serían fusilados por Stalin al año siguiente, en las purgas.",
    cd(dict(type='counter', to=518, label='millones de dólares de 1936'), at='quinientos millones'),
    ph('Moscow trial 1938 Bukharin', at='serían fusilados', lt=['Tercer proceso de Moscú', 'marzo de 1938']))
IZQ("Es un detalle terrible, pero no cambia el valor del documento. El acta existe, está firmada y reconoce que el oro es de España. Ese papel es la prueba de que la República no regaló nada.",
    K('EL ACTA EXISTE', 'official document signatures 1937', at='El acta existe'))
DER("El acta existe. La pregunta es qué valía un papel firmado por un Estado que fusilaba a quienes lo firmaban. [pause] Y la siguiente pregunta es aún más importante: ¿cómo salió ese oro del Gojrán? ¿Quién decidió cada venta, a qué precio, y adónde fue el dinero?",
    ph('Kremlin night 1930s', at='qué valía un papel'),
    ph('Gokhran vault gold', at='cómo salió ese oro'))

# ---------------- RECAPITULACIÓN ----------------
B('tema')
IZQ("Antes de seguir, recapitulemos. En septiembre del treinta y seis, con Franco camino de Madrid, el Gobierno saca el oro del Banco de España y lo lleva a Cartagena. Una cuarta parte se vende en Francia.",
    cd(dict(type='recap', title='Hasta aquí', items=[['Septiembre 1936', 'el oro sale de Madrid hacia Cartagena'], ['Oro de París', '193 toneladas vendidas en Francia'], ['25 de octubre', '7.800 cajas zarpan hacia Odesa'], ['5 de febrero de 1937', 'acta de depósito en Moscú']]), at='recapitulemos'))
DER("Las otras tres cuartas partes, quinientas diez toneladas, salen en octubre hacia la Unión Soviética, sin recibo, en una operación dirigida por la NKVD. Y en febrero de mil novecientos treinta y siete, Moscú firma un acta de depósito. [short pause] Ahora empieza lo más difícil de explicar: cómo desapareció.",
    ph('Soviet cargo ship sea 1930s', at='quinientas diez toneladas'),
    K('¿CÓMO DESAPARECIÓ?', 'empty bank vault', at='cómo desapareció'))
