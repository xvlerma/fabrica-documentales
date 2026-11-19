# -*- coding: utf-8 -*-
# «El oro de Moscú» · parte 3: capítulos 5, 6 y 7 y cierre
from lib import *

# ---------------- CAPÍTULO 5 ----------------
T('Del oro a las armas', 'Capítulo 5', secs=5.0, text='[serious] Capítulo cinco. [short pause] Del oro a las armas.')
B('tension')
IZQ("Valencia, dieciséis de febrero de mil novecientos treinta y siete. Once días después del acta de Moscú, Largo Caballero y Negrín firman la primera orden de venta. Y lo que dice explica muchas cosas.",
    ph('Valencia 1937', at='Valencia, dieciséis', lt=['Valencia', '16 de febrero de 1937']),
    ph('Francisco Largo Caballero 1937', at='Largo Caballero'))
V('DOC', "«Entregue el equivalente de este oro al delegado del Comisariado para el Comercio Exterior, agente comercial de la URSS en España, como pago de las mercancías libradas por él al Gobierno de la República Española, por la suma de cincuenta y un millones ciento sesenta mil ochocientos ochenta y ocho dólares.»",
  DOCC('Orden de venta · Valencia, 16 de febrero de 1937', 'como pago de las mercancías libradas por él al Gobierno de la República Española, por la suma de 51.160.888 dólares', 'Orden firmada por Largo Caballero y Negrín', at='Entregue el equivalente'))
IZQ("[serious] Mercancías ya entregadas. Es decir: la Unión Soviética llevaba meses mandando armas a crédito, antes de vender un solo gramo del oro. Los tanques y los cazas que defendieron Madrid en noviembre se pagaron después de haber combatido.",
    K('YA ENTREGADAS', 'T-26 tank Madrid 1936', at='Mercancías ya entregadas'),
    ph('Polikarpov I-16 Spain Republican', at='los cazas'))
DER("Cierto. Y también es cierto que, a partir de ahí, cada venta funcionó igual. El Gobierno español ordenaba vender una partida. El Banco del Estado soviético la compraba, y el dinero se transfería a un banco de París.",
    ph('Gosbank USSR building Moscow', at='El Banco del Estado soviético'),
    ph('Paris boulevard Haussmann 1930s', at='un banco de París'))
DER("Sobre el papel, el precio era justo: las órdenes pedían vender a la cotización del oro en la Bolsa de Londres de ese día. Pero quien ejecutaba la venta, cobraba las comisiones y llevaba las cuentas era siempre Moscú. La República, con su embajador como único testigo, solo podía firmar y esperar.",
    ph('Kremlin 1937 winter', at='pasar por Moscú'))
DER("Ese banco de París tenía un nombre muy discreto: Banca Comercial para la Europa del Norte. Pero no era un banco francés cualquiera. Era propiedad de la Unión Soviética. [short pause] El oro salía de un bolsillo soviético y entraba en otro.",
    ph('Banque Commerciale pour l Europe du Nord Paris', at='Banca Comercial', lt=['Banque Commerciale pour l\'Europe du Nord', 'banco soviético en París', 'urss'], gloss=['Eurobank', 'banco de propiedad soviética en París', 'urss']),
    K('UN BANCO SOVIÉTICO', 'Paris 1930s bank', at='propiedad de la Unión Soviética'))
IZQ("Y desde ese banco, la República pagaba. No solo armas soviéticas: también compras en Checoslovaquia, en Polonia, en Bélgica, en Estados Unidos, petróleo, alimentos, materias primas. El oro de Moscú financió buena parte de la economía de guerra republicana, no solo los tanques rusos.",
    cd(dict(type='list', header='Qué se pagó con el oro', items=[['Armas', 'soviéticas y de otros países'], ['Combustible', 'petróleo y carburantes'], ['Comida', 'trigo y alimentos'], ['Materias primas', 'para la industria de guerra']]), at='No solo armas'))
IZQ("¿Y qué llegó? Solo entre octubre de mil novecientos treinta y seis y julio de mil novecientos treinta y siete, la Unión Soviética envió seiscientos cuarenta y ocho aviones y trescientos cuarenta y siete tanques. Sin ellos, Madrid habría caído en el primer invierno.",
    cd(dict(type='versus', title='Envíos soviéticos, octubre 1936 - julio 1937', left=dict(name='Aviones', color=SO, lines=['648']), right=dict(name='Tanques', color=SO, lines=['347'])), at='seiscientos cuarenta y ocho'),
    ph('Madrid defense November 1936', at='Madrid habría caído'))
IZQ("[serious] Y aquí hay que mirar al otro lado del frente. Porque Franco también necesitaba armas, y no tenía el oro del Banco de España. ¿Cómo las pagó? A crédito. Alemania e Italia le mandaron aviones, tanques y decenas de miles de soldados, y le dejaron pagar después de la guerra.",
    ph('Italian CTV troops Spain 1937', at='decenas de miles de soldados'),
    ph('Condor Legion aircraft Spain', at='Alemania e Italia'))
IZQ("Y no solo las dictaduras. Una gran petrolera estadounidense, Texaco, le suministró a Franco combustible a crédito durante toda la guerra. A la República, el mundo le cobraba al contado y por adelantado. A Franco, le fiaban. [short pause] Esa diferencia explica por qué el oro tuvo que salir de España.",
    ph('Texaco oil tanker 1930s', at='Texaco', lt=['Texaco', 'petrolera estadounidense']),
    K('AL CONTADO / A CRÉDITO', 'oil barrels 1930s port', at='le fiaban'))
DER("Es un argumento sólido. Aunque tiene otra lectura: a Franco le fiaban porque sus proveedores confiaban en que ganaría. A la República nadie le fiaba a largo plazo. Ni siquiera Stalin: le adelantó armas unos meses, pero con el oro ya guardado en Moscú.",
    ph('Francisco Franco 1937 Burgos', at='a Franco le fiaban'))
IZQ("Además, no todo lo que llegó de la Unión Soviética se pagó con oro. Miles de voluntarios de medio mundo vinieron a luchar en las Brigadas Internacionales, organizadas por la Internacional Comunista. Y cientos de pilotos republicanos se formaron en escuelas de vuelo soviéticas, como la de Kirovabad.",
    ph('International Brigades 1937', at='Brigadas Internacionales', gloss=['Brigadas Internacionales', 'voluntarios extranjeros que lucharon por la República', 'izquierda']),
    ph('Spanish Republican pilots 1937', at='cientos de pilotos'))
M('tension', 9)
DER("[serious] Ahora, el precio. En mil novecientos noventa y ocho, el investigador británico Gerald Howson publicó un libro, Armas para España, basado en los archivos militares rusos abiertos tras la caída de la Unión Soviética. Y sus conclusiones fueron un terremoto.",
    ph('Russian State Military Archive Moscow', at='archivos militares rusos'),
    ph('fall of Soviet Union 1991 Moscow', at='la caída de la Unión Soviética'))
DER("Según Howson, los soviéticos cobraron a la República precios inflados, jugando con el tipo de cambio entre el rublo y el dólar. Y una parte del material eran restos: fusiles de la Primera Guerra Mundial, cañones de varios países, piezas que no casaban con su munición.",
    cd(dict(type='split', left=dict(title='Lo que se pagó', lines=['precios en dólares', 'cambio fijado por Moscú']), right=dict(title='Lo que llegó', lines=['material moderno', 'y también chatarra de 1914'])), at='precios inflados'),
    ph('World War I rifles old', at='fusiles de la Primera Guerra Mundial'))
IZQ("Esa tesis también tiene respuesta. Viñas y otros historiadores que han trabajado con los mismos archivos rusos discuten esos cálculos. Sostienen que el material moderno, los cazas, los bombarderos, los tanques T-veintiséis, era de lo mejor que había en Europa. Y que los contratos fueron legales, firmados entre dos Estados soberanos.",
    ph('Tupolev SB bomber Spain Katiuska', at='los bombarderos'),
    ph('T-26 tank Spanish Civil War', at='T-veintiséis', gloss=['T-26', 'carro de combate soviético, el mejor del principio de la guerra', 'urss']))
IZQ("[softly] Y hay un dato que rara vez se cuenta. Donde la República sufrió más estafas no fue en Moscú. Fue en los mercados de media Europa, comprando a traficantes. El historiador Miguel Campos documenta casos de intermediarios, e incluso de cargos republicanos, que supuestamente se quedaron con millones por el camino.",
    ph('arms dealer 1930s Europe port', at='traficantes'),
    ph('Spanish Republic money francs 1937', at='se quedaron con millones'))
DER("Eso es verdad, y dice mucho del desorden con que se gestionó el dinero. Pero no quita lo esencial. Con el oro en Moscú, el que ejecutaba las ventas, aplicaba el tipo de cambio y marcaba el ritmo de los envíos era siempre la misma parte. [short pause] La República ponía el dinero. Stalin ponía las condiciones.",
    K('STALIN PONÍA LAS CONDICIONES', 'Stalin Kremlin 1937', at='Stalin ponía las condiciones'))

IZQ("Con las armas llegaron también los asesores. Unos dos mil militares y técnicos soviéticos pasaron por España durante la guerra: pilotos, tanquistas, instructores, intérpretes. Muchos combatieron y murieron en los cielos de Madrid y en el frente de Aragón.",
    ph('Soviet advisers Spain 1937', at='los asesores'),
    ph('Soviet pilots Spain 1937', at='pilotos, tanquistas'))
DER("Y con los asesores militares llegaron otros, menos visibles. Los hombres de la NKVD, como Orlov, que no estaban allí para pilotar aviones, sino para vigilar, informar y, llegado el caso, eliminar a quien estorbara a Stalin.",
    ph('NKVD agents 1930s', at='menos visibles'))

# ---------------- RECAPITULACIÓN 2 ----------------
B('tema')
DER("Recapitulemos otra vez. Desde febrero de mil novecientos treinta y siete, la República va vendiendo el oro depositado en Moscú. El dinero pasa por un banco soviético en París y con él se pagan armas soviéticas y compras en medio mundo.",
    cd(dict(type='recap', title='Hasta aquí', items=[['Febrero de 1937', 'primera orden de venta: 51 millones de dólares'], ['El circuito', 'Gosbank, banco soviético en París y pagos'], ['Lo que llegó', '648 aviones y 347 tanques hasta julio de 1937'], ['El debate', 'precios inflados o precios de mercado']]), at='Recapitulemos'))
IZQ("Las armas llegan y salvan Madrid. Pero el precio y la calidad de lo que se compró siguen discutidos, y el control de las cuentas lo tiene Moscú. [short pause] Y en mayo de mil novecientos treinta y siete, todo cambia en el Gobierno de la República.",
    K('MAYO DE 1937', 'Barcelona 1937', at='todo cambia'))

# ---------------- CAPÍTULO 6 ----------------
T('Se acabó el oro', 'Capítulo 6', secs=5.0, text='[serious] Capítulo seis. [short pause] Se acabó el oro.')
B('rusia')
DER("Barcelona, mayo de mil novecientos treinta y siete. En plena guerra, anarquistas y trotskistas se enfrentan a tiros con comunistas y fuerzas del Gobierno. Mueren cientos de personas. Son los llamados hechos de mayo.",
    ph('Barcelona May Days 1937 barricades', at='Barcelona, mayo', lt=['Barcelona', 'mayo de 1937']),
    ph('Barcelona 1937 street fighting', at='hechos de mayo', gloss=['Hechos de mayo', 'choques armados entre izquierdas en Barcelona, mayo de 1937']))
DER("Largo Caballero cae. Y el diecisiete de mayo, el nuevo presidente del Gobierno es Juan Negrín. El hombre que había enviado el oro a Moscú pasa a dirigir la República hasta el final de la guerra.",
    ph('Juan Negrín 1938', at='Juan Negrín', lt=['Juan Negrín', 'Presidente del Gobierno, 1937-1939', 'izquierda']))
DER("Unas semanas después, el líder del POUM, un partido marxista contrario a Stalin, Andreu Nin, es detenido y desaparece. Lo asesinaron agentes soviéticos. La operación la dirigió el mismo hombre que había cargado el oro en Cartagena: Alexander Orlov.",
    ph('Andreu Nin', at='Andreu Nin', lt=['Andreu Nin', 'Dirigente del POUM', 'izquierda'], gloss=['POUM', 'partido marxista revolucionario, enemigo de Stalin', 'izquierda']),
    ph('Alexander Orlov', at='Alexander Orlov'))
DER("[serious] Para los críticos, esta es la consecuencia política del oro. Sin oro en España, sin otra fuente de armas, la República dependía de Moscú para seguir luchando. Y esa dependencia daba a Stalin una influencia enorme sobre quién mandaba, a quién se perseguía y cuándo se negociaba.",
    K('DEPENDENCIA', 'Soviet flag 1937', at='dependía de Moscú'),
    ph('Communist Party Spain 1937 poster', at='una influencia enorme'))
DER("Hay un ejemplo que los críticos citan siempre. En abril de mil novecientos treinta y ocho, Indalecio Prieto, ministro de Defensa y el socialista más reacio a los comunistas, sale del Gobierno. Él mismo culpó después a las presiones comunistas y soviéticas.",
    ph('Indalecio Prieto 1938', at='Indalecio Prieto', lt=['Indalecio Prieto', 'Ministro de Defensa Nacional hasta abril de 1938', 'izquierda']))
IZQ("Los defensores de Negrín no niegan la influencia soviética. Pero recuerdan que Negrín no era comunista, que chocó varias veces con los asesores de Moscú y que su objetivo era otro: resistir hasta que estallara la guerra en Europa y las democracias tuvieran que ayudar a la República. Su biógrafo, Enrique Moradiellos, lo llamó la figura más difamada de la España del siglo veinte.",
    ph('Juan Negrín speech 1938', at='Negrín no era comunista'),
    K('RESISTIR', 'Spanish Republic poster resistir 1938', at='resistir'),
    ph('Juan Negrín portrait 1930s', at='la figura más difamada'))
M('rusia', 9)
IZQ("Mientras tanto, el oro se iba vendiendo. Partida tras partida, durante todo mil novecientos treinta y siete. Una guerra moderna devoraba el dinero a una velocidad que nadie había previsto.",
    ph('Spanish Civil War artillery 1937', at='devoraba el dinero'))
DER("Y en mil novecientos treinta y ocho, según las cuentas soviéticas, el depósito estaba prácticamente vacío. A finales de ese año, Negrín y Méndez Aspe tuvieron que pedir a Moscú nuevos suministros a crédito. [pause] La cuarta reserva de oro del mundo se había evaporado en menos de dos años.",
    ph('empty bank vault', at='prácticamente vacío'),
    cd(dict(type='counter', to=0, label='toneladas de oro español que quedaban en Moscú en 1939, según la URSS'), at='se había evaporado'))
IZQ("[serious] Julio de mil novecientos treinta y ocho. El Ejército Popular cruza el río Ebro en la mayor ofensiva republicana de la guerra. Es la apuesta final de Negrín: aguantar, demostrar que la República seguía viva, y esperar a que Francia y Gran Bretaña entraran en guerra con Hitler.",
    ph('Battle of the Ebro 1938', at='el río Ebro', lt=['Batalla del Ebro', 'julio-noviembre de 1938']),
    ph('Republican soldiers Ebro crossing 1938', at='la mayor ofensiva'))
DER("Pero en septiembre, en Múnich, Francia y Gran Bretaña entregan a Hitler una parte de Checoslovaquia para evitar la guerra. La esperanza de Negrín se hunde. Y Stalin, que ve cómo las democracias pactan con Hitler, empieza a perder interés en España.",
    ph('Munich Agreement 1938 Chamberlain Hitler', at='en Múnich', lt=['Acuerdos de Múnich', 'septiembre de 1938']),
    K('MÚNICH', 'Munich 1938 conference', at='La esperanza de Negrín se hunde'))
IZQ("En octubre, las Brigadas Internacionales desfilan por última vez en Barcelona antes de marcharse. Y en noviembre, la batalla del Ebro termina con la retirada republicana. La guerra está perdida, aunque durará cuatro meses más.",
    ph('International Brigades farewell Barcelona 1938', at='desfilan por última vez'),
    ph('Ebro retreat 1938', at='la retirada republicana'))
IZQ("En esos últimos meses, el dinero que quedaba no solo pagaba armas. Pagaba también trigo y alimentos para una zona republicana desbordada de refugiados, donde en ciudades como Barcelona o Madrid se pasaba hambre de verdad.",
    ph('Barcelona 1938 food queue', at='se pasaba hambre'),
    ph('Spanish Civil War refugees 1938', at='refugiados'))
IZQ("Hay que decirlo con claridad: aunque el oro se hubiera quedado en España, se habría gastado igual. Es lo que pasa con las reservas de cualquier país en guerra. Gran Bretaña vació las suyas pocos años después para pagar la guerra contra Hitler.",
    ph('Bank of England gold World War II', at='Gran Bretaña vació las suyas'))
DER("La diferencia es quién lleva las cuentas. Gran Bretaña podía comprobar cada libra que gastaba. La República, en cambio, tuvo que fiarse de las cuentas que le presentaba el Gobierno soviético. [short pause] Y en marzo de mil novecientos treinta y nueve, la guerra se perdió.",
    ph('London 1940', at='Gran Bretaña podía comprobar'),
    ph('end of Spanish Civil War 1939 Madrid', at='la guerra se perdió', lt=['Madrid', 'marzo de 1939']))

DER("Y aún queda un último cargamento. En marzo de mil novecientos treinta y nueve, en las últimas semanas de la guerra, el yate Vita llega a México. A bordo, cajas con joyas, oro y objetos de valor reunidos por el Gobierno republicano, para mantener a los exiliados.",
    ph('yacht Vita 1939', at='el yate Vita', lt=['Yate Vita', 'Veracruz, marzo de 1939']),
    ph('Veracruz port 1939', at='llega a México'))
DER("Ese tesoro acabó controlado por Indalecio Prieto, ya enfrentado a muerte con Negrín. Y los dos dirigentes socialistas se pasaron el exilio acusándose mutuamente de cómo se había gestionado el dinero de la República. [short pause] La guerra por el oro siguió mucho después de que terminara la otra.",
    ph('Indalecio Prieto Mexico exile', at='Indalecio Prieto'),
    K('LA OTRA GUERRA', 'Mexico City 1939', at='La guerra por el oro'))

# ---------------- CAPÍTULO 7 ----------------
T('El recibo', 'Capítulo 7', secs=5.0, text='[serious] Capítulo siete. [short pause] El recibo.')
B('tema')
DER("Para la España de Franco, el oro de Moscú se convirtió enseguida en un arma de propaganda. Era la prueba de que la República había vendido el país a los soviéticos. Y una explicación cómoda para el hambre de la posguerra: no hay pan porque los rojos se llevaron el oro.",
    ph('Francoist propaganda poster 1940', at='arma de propaganda'),
    ph('Spain 1940s ration queue', at='el hambre de la posguerra'))
IZQ("[serious] Y hay que decirlo: la propaganda franquista exageró. Contaba la historia como un robo, ocultaba que buena parte del oro se gastó en armas que de verdad llegaron, y no decía nada del oro de París ni de las armas que Alemania e Italia daban a Franco a crédito.",
    K('PROPAGANDA', 'Francoist newspaper 1940', at='exageró'),
    ph('Italian troops Spain 1937 CTV', at='Alemania e Italia'))
DER("Mientras tanto, el único hombre que conocía todas las cuentas guardaba silencio en el exilio. Juan Negrín vivió en Francia y en Inglaterra, defendió hasta el final la legitimidad de su Gobierno, y nunca publicó los papeles del oro.",
    ph('Juan Negrín exile Paris', at='en el exilio'),
    ph('Juan Negrín 1940s', at='nunca publicó'))
DER("Negrín murió en París el doce de noviembre de mil novecientos cincuenta y seis. [pause] Un mes después, el dieciocho de diciembre, su hijo entregó al cónsul de España en París un dosier. Dentro estaba el acta del depósito de Moscú y las órdenes de venta. [short pause] Los papeles acabaron en manos del Gobierno de Franco.",
    ph('Paris 1956 street', at='murió en París', lt=['París', '12 de noviembre de 1956']),
    ph('Spanish consulate Paris', at='cónsul de España en París'),
    DOCC('Dosier Negrín', 'Acta de depósito del oro y órdenes de venta', 'Entregado al consulado de España en París · 18 de diciembre de 1956', at='un dosier'))
IZQ("Por qué lo hizo la familia sigue siendo discutido. La versión más aceptada es que Negrín quería que los papeles volvieran a España, para que constara que el oro no se robó, sino que se gastó por decisión de un Gobierno legítimo. Era su manera de defenderse ante la historia.",
    ph('Juan Negrín family', at='la familia'),
    K('ANTE LA HISTORIA', 'old documents archive', at='ante la historia'))
DER("Con el recibo en la mano, el Gobierno de Franco reclamó oficialmente el oro a la Unión Soviética. Y en abril de mil novecientos cincuenta y siete, antes incluso de que llegara la reclamación formal, Moscú respondió en público por medio del diario Pravda.",
    ph('Spanish Ministry Foreign Affairs 1957', at='reclamó oficialmente'),
    ph('Pravda newspaper 1957', at='diario Pravda', lt=['Pravda', 'diario oficial del Partido Comunista', 'urss']))
V('DOC', "La respuesta, en resumen, era esta: no hay oro. La República lo había gastado entero en las armas y los suministros que recibió durante la guerra.",
  cd(dict(type='doc', title='Respuesta soviética · abril de 1957', lines=['No queda oro: la República lo gastó en armas y suministros.'], source='Resumen de la respuesta publicada por Pravda'), at='no hay oro'))
DER("Fíjate en el orden: primero la respuesta, después la pregunta. Moscú sabía lo que España iba a reclamar, y cerró la puerta antes de que nadie llamara.",
    K('PRIMERO LA RESPUESTA', 'Pravda 1957 front page', at='primero la respuesta'))
DER("Fin de la discusión. Sin auditoría, sin acceso a las cuentas, sin un solo documento soviético a la vista. Durante veinte años, España no tuvo relaciones diplomáticas con la Unión Soviética, y el oro fue siempre la condición. Cuando por fin se restablecieron, en mil novecientos setenta y siete, el asunto se dejó a un lado.",
    K('SIN AUDITORÍA', 'Kremlin 1957', at='Sin auditoría'),
    ph('Spain USSR diplomatic relations 1977', at='mil novecientos setenta y siete'))
IZQ("[softly] Y sin embargo, uno de los mayores apoyos a la versión soviética salió de una institución del propio régimen. En mil novecientos setenta, el economista Joan Sardá publicó una historia del Banco de España. Y concluyó que el oro se había gastado legítimamente para pagar las armas.",
    ph('Banco de España 1970', at='Joan Sardá', lt=['Joan Sardá', 'Economista · Servicio de Estudios del Banco de España', 'centro']),
    K('GASTADO, NO ROBADO', 'old ledger book', at='legítimamente'))
M('tema', 9)
DER("Para entonces, los protagonistas habían ido desapareciendo. Largo Caballero había muerto en París en mil novecientos cuarenta y seis, tras pasar por un campo de concentración nazi. Prieto murió en México en mil novecientos sesenta y dos. Y Alexander Orlov, el hombre que cargó el oro, murió en Estados Unidos en mil novecientos setenta y tres, llevándose lo que no había contado.",
    ph('Francisco Largo Caballero 1940s', at='Largo Caballero había muerto'),
    ph('Indalecio Prieto 1950s', at='Prieto murió'),
    ph('Alexander Orlov', at='Alexander Orlov, el hombre'))
IZQ("Con la democracia llegaron los historiadores. En mil novecientos setenta y seis, recién muerto Franco, Ángel Viñas publicó su primer estudio sobre el oro. Su título lo decía todo: El oro de Moscú, alfa y omega de un mito franquista. Para Viñas, la cuestión estaba clara: el oro se gastó, no se robó.",
    ph('Madrid 1976 Transition', at='mil novecientos setenta y seis'),
    K('ALFA Y OMEGA DE UN MITO', 'old book cover 1970s', at='alfa y omega'))
IZQ("Viñas había sido economista del Estado y diplomático, y tuvo acceso a la documentación del Banco de España y del Ministerio de Hacienda. Fue el primero en reconstruir, venta a venta, adónde fue el dinero.",
    ph('Ministerio de Hacienda Madrid', at='Ministerio de Hacienda'))
DER("Pero la crítica no vino solo de la derecha. En mil novecientos noventa, el historiador Francisco Olaya Morales, que había militado en el anarquismo, publicó El oro de Negrín. Un libro durísimo contra la gestión del dinero de la República. [short pause] Y es que muchos anarquistas y socialistas nunca perdonaron que el tesoro del país quedara en manos de Moscú.",
    ph('CNT FAI 1936 Barcelona', at='en el anarquismo'),
    K('EL ORO DE NEGRÍN', 'old book 1990', at='El oro de Negrín'))
IZQ("Después llegaron los archivos rusos. Howson en mil novecientos noventa y ocho, Martín Aceña en dos mil uno, Daniel Kowalsky en dos mil tres, y otra vez Viñas, en una trilogía y en un último libro de dos mil veintitrés, de más de quinientas páginas, basado en documentos soviéticos publicados en ruso. [short pause] Cada nueva caja de papeles ha matizado algo. Ninguna ha cerrado la discusión.",
    cd(dict(type='timeline', header='La batalla de los historiadores', events=[['1976', 'Viñas: «alfa y omega de un mito»'], ['1990', 'Olaya: El oro de Negrín'], ['1998', 'Howson: Armas para España'], ['2001', 'Martín Aceña: El oro de Moscú y el oro de Berlín'], ['2023', 'Viñas: Oro, guerra, diplomacia']]), at='Después llegaron'))

# ---------------- CIERRE ----------------
B('tension')
IZQ("Noventa años después, ¿qué sabemos? Sabemos que el oro existió, que salió de Cartagena, que llegó a Moscú y que se firmó un acta. Sabemos que se vendió por orden del Gobierno republicano y que con él llegaron aviones, tanques y alimentos que alargaron la resistencia dos años y medio.",
    ph('Cartagena port today', at='salió de Cartagena', lt=['Cartagena', 'hoy']),
    ph('Spanish Republic soldiers 1938 Ebro', at='alargaron la resistencia'))
IZQ("Para Ángel Viñas, la conclusión es clara: el oro de Moscú no fue un robo, sino el pago de una República abandonada. Y la idea contraria sobrevive por otras razones.",
    ph('Spanish Civil War archive', at='Ángel Viñas'))
V('HIS', "«Un mito es una creencia inmutable a la que cierta derecha sigue amarrada por razones ideológicas.»",
  Q('Un mito es una creencia inmutable a la que cierta derecha sigue amarrada por razones ideológicas.', 'Ángel Viñas, historiador · entrevista en Diario de León (2026)', at='Un mito'))
DER("[serious] Es una respuesta firme. Pero deja preguntas sin contestar. [short pause] ¿Por qué se envió todo el oro de una vez, y no por partes, según se fuera necesitando? ¿Por qué a la dictadura más opaca de Europa, y no repartido entre varios países?",
    cd(dict(type='list', header='Preguntas abiertas', items=[['1', '¿Por qué todo de una vez?'], ['2', '¿Por qué a un solo país?'], ['3', '¿Por qué sin recibo en Cartagena?'], ['4', '¿Quién auditó las cuentas?']]), at='deja preguntas'))
DER("¿Por qué no se pidió un recibo en Cartagena? ¿Por qué se retuvo a los únicos testigos españoles? ¿Y quién comprobó, gramo a gramo, que las cuentas que Moscú presentó eran ciertas? [pause] La respuesta a esa última pregunta es sencilla: nadie.",
    ph('Cartagena night port', at='un recibo en Cartagena'),
    K('NADIE', 'empty vault dark', at='nadie'))
IZQ("Hay respuestas para algunas. Todo de una vez, porque Madrid podía caer en días y no había tiempo para ir enviándolo por partes. A un solo país, porque era el único que vendía. Y sin auditoría, porque la República perdió la guerra y nunca tuvo ocasión de pedir cuentas.",
    ph('Madrid November 1936 front', at='Madrid podía caer'),
    K('NO HABÍA TIEMPO', 'Madrid 1936 barricade', at='no había tiempo'))
DER("Son respuestas razonables. Pero todas tienen el mismo punto débil: dan por hecho que no había otra forma de hacerlo. Y eso, precisamente, es lo que no se puede demostrar. Porque las demás opciones nunca se discutieron. Las descartaron dos hombres, en secreto, en unos pocos días.",
    ph('Juan Negrín Largo Caballero 1936', at='dos hombres'))
IZQ("[softly] Y conviene no olvidar a quién defendían esas armas. A un Gobierno elegido en las urnas, atacado por un ejército sublevado que tenía detrás a Hitler y a Mussolini. Sin el oro de Moscú, Franco habría ganado en unos meses. Con él, la República resistió casi tres años.",
    ph('Spanish Republic voters 1936', at='elegido en las urnas'),
    ph('Hitler Mussolini 1937', at='Hitler y a Mussolini'))
IZQ("Quizá porque en el otoño de mil novecientos treinta y seis no había tiempo para hacerlo mejor. Madrid estaba a punto de caer. Y cuando una casa arde, nadie negocia el precio del agua.",
    ph('Madrid burning November 1936', at='Madrid estaba a punto de caer'))
DER("Quizá. [short pause] O quizá por eso mismo. Porque quien llega con el agua en el momento del incendio sabe que puede pedir lo que quiera. [pause] El oro de Moscú no fue un robo. Lo entregó un Gobierno, por su propia voluntad, a una dictadura que nunca tuvo que rendir cuentas.",
    ph('Stalin 1937 portrait', at='puede pedir lo que quiera'),
    ph('Soviet cargo ship 1936', at='Lo entregó un Gobierno'))
DER("[softly] Siete mil ochocientas cajas salieron de Cartagena una noche de octubre. Lo que valían de verdad, y lo que costaron, se quedó para siempre en Moscú.",
    ph('Cartagena harbour night', at='Siete mil ochocientas cajas'),
    ph('Kremlin night snow', at='para siempre en Moscú'))
DER("Esto ha sido DocuVox. Si te ha gustado, suscríbete y cuéntanos en los comentarios: ¿la única salida... o la gran entrega?",
    cd(dict(type='title', title='DocuVox', sub='Documentales sonoros'), at='Esto ha sido'))
