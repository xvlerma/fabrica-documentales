# -*- coding: utf-8 -*-
# «Vivir al límite» · parte 1: apertura, mapa, Coober Pedy, Oimiakón, Yakutsk
from lib import *

# ---------------- APERTURA FRÍA ----------------
B('tension')
N("[serious] Son las cinco de la mañana a cinco mil cien metros de altura. Aquí arriba, cada bocanada de aire trae la mitad de oxígeno que en la playa. No hay árboles. No hay alcantarillas. Y aun así, miles de personas se levantan cada día para entrar en una montaña.",
  vd('La Rinconada Peru', at='Son las cinco', lt=['La Rinconada', 'Andes del Perú · 5.100 m']),
  ph('La Rinconada Peru town', at='No hay árboles'),
  ph('La Rinconada mine Ananea', at='entrar en una montaña'))
C("Durante treinta días trabajan sin cobrar. Al día treinta y uno, lo que logren sacar de la roca es suyo. Puede ser nada. Puede ser oro.",
  ph('La Rinconada miners', at='Durante treinta días'),
  K('ORO', 'gold nugget', at='Puede ser oro'))
N("[short pause] La Rinconada, en Perú, es el pueblo más alto del mundo. Pero no es el único sitio donde vivir parece imposible. [pause] Hay un pueblo que se refugia bajo tierra para no morir de calor. Otro donde el termómetro bajó a casi setenta grados bajo cero. Una ciudad sobre hielo que se está derritiendo. Un pueblo entero dentro de un solo edificio. Y una isla tan lejos de todo que, para llegar, hay que navegar una semana.",
  ph('La Rinconada Peru glacier', at='La Rinconada, en Perú', lt=['La Rinconada', 'Puno, Perú']),
  ph('Coober Pedy dugout', at='bajo tierra'),
  ph('Oymyakon winter', at='setenta grados bajo cero'),
  ph('Yakutsk buildings piles permafrost', at='Una ciudad sobre hielo'),
  ph('Begich Towers Whittier', at='un solo edificio'),
  ph('Tristan da Cunha island aerial', at='Y una isla'))
C("Esta es la historia de nueve lugares donde la gente vive, trabaja, se enamora y cría a sus hijos en condiciones que a la mayoría nos parecerían insoportables. Nada de lo que vas a ver es ficción. Y algunas cosas, te lo aseguramos, te van a costar creerlas.",
  ph('Longyearbyen children snow', at='Esta es la historia'),
  ph('Coober Pedy underground church interior', at='Nada de lo que vas a ver'))
N("[serious] ¿Cómo se vive allí? ¿Quién elige vivir allí? [pause] Y la pregunta que de verdad importa: cuando todo te dice que te vayas… ¿por qué se quedan?",
  ph('Edinburgh of the Seven Seas', at='Cómo se vive'),
  ph('Longyearbyen polar night', at='Quién elige'),
  vd('mountain fog dawn', at='por qué se quedan'))
T('Vivir al límite', 'Los lugares más extremos donde vive gente', secs=5.5, sting='tema', text='[dramatically] Vivir al límite.', chapter=False)

# ---------------- EL VIAJE ----------------
B('tema')
C("Vamos a dar la vuelta al planeta. Nueve lugares y una misma regla: en cada uno, la naturaleza ha puesto un límite. Y alguien ha decidido vivir justo al otro lado.",
  cd(dict(type='mapfly', title='Nueve lugares al límite', keys=[[-170, -58, 190, 75]], points=[
      dict(name='La Rinconada', lon=-69.4, lat=-14.6, at=.15), dict(name='Coober Pedy', lon=134.8, lat=-29.0, at=.22),
      dict(name='Oimiakón', lon=142.8, lat=63.5, at=.29), dict(name='Yakutsk', lon=129.7, lat=62.0, at=.36),
      dict(name='Norilsk', lon=88.2, lat=69.3, at=.43), dict(name='Longyearbyen', lon=15.6, lat=78.2, at=.50),
      dict(name='Whittier', lon=-148.7, lat=60.8, at=.57), dict(name='Aogashima', lon=139.8, lat=32.5, at=.64),
      dict(name='Tristán de Acuña', lon=-12.3, lat=-37.1, at=.71)]), at='Vamos a dar la vuelta'))
N("Calor, frío, suelo helado, aire tóxico, oscuridad, aislamiento, volcanes y falta de oxígeno. Empezamos por el calor. [short pause] Y por un agujero en el suelo.",
  cd(dict(type='list', header='Los ocho límites', items=['Calor', 'Frío', 'Suelo helado', 'Aire tóxico', 'Oscuridad', 'Aislamiento', 'Volcanes', 'Falta de oxígeno']), at='Calor, frío'),
  ph('Coober Pedy mine shaft', at='Y por un agujero'))

# ---------------- 1 · COOBER PEDY ----------------
C("Antes de salir, una idea para entender todo lo que vamos a ver. El cuerpo humano es una máquina muy exigente. Funciona bien con el centro del cuerpo a unos treinta y siete grados, con agua cerca y con aire suficiente. Si te alejas mucho de esas condiciones, empieza a fallar.",
  vd('human silhouette sunrise mountain', at='Antes de salir'),
  K('37 °C', 'thermometer body temperature', at='treinta y siete grados'))
N("Por eso casi toda la humanidad vive en una franja estrecha del planeta: ni muy alta, ni muy fría, ni muy seca. Los lugares de este viaje están fuera de esa franja. Y en cada uno, la gente ha encontrado un truco para sobrevivir: cavar, calentar, aislar, compartir… o simplemente aguantar.",
  vd('earth from space night lights', at='Por eso casi toda la humanidad'),
  cd(dict(type='list', header='Cinco trucos para sobrevivir', items=['Cavar', 'Calentar', 'Aislar', 'Compartir', 'Aguantar']), at='un truco para sobrevivir'))
T('Bajo tierra', 'Coober Pedy, Australia', secs=4.5, sting='tension')
B('desierto')
N("Desierto de Australia Meridional, a unos ochocientos cincuenta kilómetros de Adelaida. En verano, el aire puede pasar de los cuarenta y cinco grados. A primera vista, Coober Pedy parece un pueblo casi vacío: tierra rojiza, montones de escombros y unas chimeneas blancas que salen directamente del suelo.",
  MAPA('Coober Pedy', 134.75, -29.01, 'Coober Pedy', span=25, at='Desierto de Australia'),
  vd('Coober Pedy', at='En verano', lt=['Coober Pedy', 'Australia Meridional · hoy']),
  ph('Coober Pedy landscape mullock heaps', at='montones de escombros'),
  ph('Coober Pedy ventilation shafts dugouts', at='unas chimeneas blancas'))
C("Esas chimeneas son la pista. Debajo hay salones, cocinas, dormitorios y hasta iglesias. Según el consejo del distrito, viven aquí unas dos mil quinientas personas. Y se calcula que la mitad vive bajo tierra.",
  ph('Coober Pedy underground home interior', at='Debajo hay salones'),
  ph('Serbian Orthodox Church Coober Pedy', at='hasta iglesias', lt=['Iglesia ortodoxa serbia de San Elías', 'Coober Pedy · excavada en 1993']),
  cd(dict(type='counter', to=50, prefix='', label='por ciento de los vecinos vive bajo tierra'), at='la mitad'))
N("Todo empezó el uno de febrero de mil novecientos quince. Un chico de catorce años, Willie Hutchison, buscaba agua con la expedición de su padre. No encontró agua. Encontró ópalos, tirados en la superficie.",
  cd(dict(type='timeline', header='Coober Pedy', events=[['1915', 'Willie Hutchison encuentra ópalo'], ['1920', 'el pueblo recibe su nombre'], ['1985', 'se rueda Mad Max 3'], ['1993', 'iglesia serbia excavada']]), at='Todo empezó'),
  ph('Coober Pedy opal', at='Encontró ópalos', lt=['Ópalo de Coober Pedy', 'la piedra que fundó el pueblo']))
N("Llegaron los buscadores. Se cuenta que, después de la Primera Guerra Mundial, muchos eran soldados que volvían de las trincheras y sabían cavar. Y descubrieron algo que cambiaría el pueblo para siempre: unos metros por debajo de la superficie, la roca mantiene una temperatura casi constante.",
  ph('Coober Pedy opal fields', at='Llegaron los buscadores'),
  ph('Coober Pedy old dugout historic', at='unos metros por debajo'))
R('DOC', "Las viviendas subterráneas mantienen una temperatura cómoda y estable, entre veintitrés y veinticinco grados, de día y de noche, durante todo el año.",
  Q('Entre 23 °C y 25 °C, de día y de noche, todo el año', 'Asociación de Turismo de Coober Pedy', at='Las viviendas'))
C("Fuera, el desierto quema. Dentro, ni calefacción ni aire acondicionado. Una casa excavada en la arenisca de una ladera puede tener varias habitaciones. Algunas llegan a los cuatrocientos cincuenta metros cuadrados.",
  vd('desert heat haze', at='Fuera, el desierto'),
  ph('Coober Pedy dugout bedroom', at='Dentro'),
  ph('Faye\'s Underground Home Coober Pedy', at='Algunas llegan', lt=['Casa subterránea de Faye', 'Coober Pedy']))
N("[short pause] Bob Del Tedesco lleva décadas en Coober Pedy. Su casa también está excavada en la colina. Y su calle es el mejor resumen del pueblo.",
  ph('Coober Pedy street dugout entrance', at='Bob Del Tedesco'))
R('T2', "En mi calle hay unas tres casas. Todo lo demás siguen siendo casas cueva.",
  cd(dict(type='quote', text='En mi calle hay unas tres casas. Todo lo demás siguen siendo casas cueva.', attrib='Bob Del Tedesco, vecino · Il Globo · traducción'), at='En mi calle'))
N("El nombre del pueblo viene de una expresión aborigen, kupa piti. Se suele traducir como «el agujero del hombre blanco». Otros prefieren «el pozo de agua de los muchachos». Desde mil novecientos setenta y cinco, la comunidad aborigen local lo llama también Umoona: «larga vida».",
  cd(dict(type='split', left=dict(title='Kupa piti', lines=['«el agujero del hombre blanco»', 'la traducción popular']), right=dict(title='Otras lecturas', lines=['«el pozo de los muchachos»', 'Umoona: «larga vida», desde 1975']), strike=False), at='El nombre del pueblo'))
C("Con un paisaje así, no es raro que el cine lo eligiera para imaginar otros planetas. Aquí se rodaron escenas de «Mad Max, más allá de la cúpula del trueno» y de «Pitch Black». Pero lo que de verdad brilla está bajo los pies.",
  ph('Moon Plain Coober Pedy', at='otros planetas', lt=['Moon Plain', 'cerca de Coober Pedy · hoy']),
  ph('Pitch Black spaceship prop Coober Pedy', at='Pitch Black'),
  K('BAJO TIERRA', 'Coober Pedy underground', at='bajo los pies'))
N("Coober Pedy ha dado durante décadas buena parte de los ópalos de calidad del planeta. Todavía hoy, buscadores independientes trabajan sus concesiones con taladros y aspiradoras gigantes. [pause] Y los carteles avisan: no camines hacia atrás. Hay miles de pozos abiertos.",
  ph('Coober Pedy opal mining machine blower', at='Todavía hoy'),
  ph('Coober Pedy warning sign shafts', at='Y los carteles avisan'),
  ph('Coober Pedy mine shafts aerial', at='miles de pozos'))
C("Vivir aquí tiene otros retos. Casi no llueve y no hay ríos. El agua sale de un acuífero subterráneo, salada, y se potabiliza en el propio pueblo. Durante años fue uno de los grandes quebraderos de cabeza de la comunidad. Ahora la empresa pública de aguas del estado va a hacerse cargo de la red antes de dos mil veintisiete.",
  ph('Coober Pedy water tank', at='Casi no llueve'),
  ph('Coober Pedy town aerial', at='Ahora la empresa pública'))
N("Y hay detalles que solo existen en Coober Pedy. Un campo de golf sin una sola brizna de hierba, donde cada jugador lleva su trocito de césped artificial para golpear la bola. Un árbol en lo alto de una colina, hecho de chatarra soldada, porque durante años no hubo ningún árbol de verdad. [short pause] Y una población de lo más variada: según la web oficial del pueblo, alrededor del sesenta por ciento de los vecinos tiene raíces europeas, de los emigrantes que llegaron tras la Segunda Guerra Mundial.",
  ph('Coober Pedy golf course', at='Un campo de golf', lt=['Campo de golf de Coober Pedy', 'sin hierba']),
  ph('Coober Pedy metal tree', at='Un árbol en lo alto', lt=['El árbol de chatarra', 'Coober Pedy']),
  ph('Coober Pedy main street Hutchison Street', at='Y una población'))
C("Bajo tierra hay hasta un hotel, con habitaciones excavadas en la roca, y varias iglesias: la católica de San Pedro y San Pablo, una anglicana conocida como la iglesia de las catacumbas y la ortodoxa serbia, con sus santos tallados a mano en las paredes de arenisca.",
  ph('Coober Pedy underground hotel room', at='hasta un hotel'),
  ph('Catacomb Church Coober Pedy', at='la iglesia de las catacumbas', lt=['Iglesia de las catacumbas', 'Coober Pedy']))
N("Esos pozos son un peligro real. Alrededor del pueblo hay campos de minas abandonadas, agujeros verticales de un metro de ancho y hasta treinta de profundidad, sin vallas. Más de un visitante distraído ha caído en uno. Por eso, en Coober Pedy, mirar al suelo al caminar no es timidez. Es supervivencia.",
  ph('Coober Pedy open mine shaft danger', at='Esos pozos son un peligro'),
  K('MIRA AL SUELO', 'Coober Pedy opal field shafts', at='mirar al suelo'))
C("Aquí, para escapar del calor, se excava hacia abajo. [short pause] Ahora vamos a un lugar donde el problema es exactamente el contrario. Donde salir a la calle sin protección puede congelarte la piel en minutos.",
  ph('Coober Pedy sunset', at='Aquí, para escapar'),
  vd('Siberia winter frost', at='Ahora vamos'))
M('desierto', 8)

# ---------------- 2 · OIMIAKÓN ----------------
T('El polo del frío', 'Oimiakón, Rusia', secs=4.5, sting='tension')
B('frio')
N("Siberia oriental, república de Sajá, también llamada Yakutia. A orillas del río Indiguirka hay un pueblo de unos quinientos habitantes. El seis de febrero de mil novecientos treinta y tres, su estación meteorológica marcó sesenta y siete grados y siete décimas bajo cero.",
  MAPA('Oimiakón', 142.8, 63.46, 'Oimiakón', span=30, at='Siberia oriental'),
  ph('Oymyakon village', at='un pueblo de unos quinientos', lt=['Oimiakón', 'Yakutia, Rusia']),
  cd(dict(type='counter', to=-67.7, prefix='', label='grados · 6 de febrero de 1933'), at='sesenta y siete grados'))
R('DOC', "La temperatura más baja del hemisferio norte: sesenta y siete grados y siete décimas bajo cero, registrada en Oimiakón el seis de febrero de mil novecientos treinta y tres. Es también la más baja medida fuera de la Antártida.",
  cd(dict(type='doc', title='Guinness World Records', lines=['La temperatura más baja del hemisferio norte: −67,7 °C, Oimiakón, 6 de febrero de 1933.'], source='Guinness World Records · traducción'), at='La temperatura más baja'))
C("Hay que decirlo todo: algunos climatólogos discuten esa medida, porque el termómetro de alcohol de la época necesitaba una corrección. Pero el título de lugar habitado más frío del planeta no se lo quita nadie. En enero, la media diaria ronda los cuarenta y seis bajo cero.",
  cd(dict(type='split', left=dict(title='El récord', lines=['−67,7 °C en 1933', 'termómetro de alcohol corregido']), right=dict(title='Lo que nadie discute', lines=['media de enero: −46 °C', 'el lugar habitado más frío']), strike=False), at='algunos climatólogos'),
  ph('Oymyakon thermometer', at='En enero'))
N("¿Cómo es un día normal a cincuenta bajo cero? Empieza por el coche. Muchos vecinos lo guardan en garajes con calefacción. Y si se queda fuera, se deja con el motor encendido. Toda la noche.",
  K('−50 °C', 'Oymyakon winter road', at='Cómo es un día normal'),
  ph('Oymyakon car frost', at='Empieza por el coche'),
  ph('Yakutia winter car exhaust', at='con el motor encendido'))
N("[short pause] El fotógrafo neozelandés Amos Chapple pasó varios días aquí. Lo que vio una mañana se lo contó a la revista Smithsonian.",
  ph('Oymyakon road Kolyma highway winter', at='El fotógrafo neozelandés'))
R('T1', "Un hombre con el que me alojaba dejó el coche en marcha toda la noche. Aun así, por la mañana, el eje de transmisión estaba completamente congelado.",
  Q('Dejó el coche en marcha toda la noche. Aun así, por la mañana, el eje estaba completamente congelado.', 'Amos Chapple, fotógrafo · Smithsonian · traducción', at='Un hombre con el que'))
C("Las pestañas se escarchan al respirar. El vaho se congela en el aire y se queda flotando como una niebla. Los cultivos son imposibles, así que la dieta de invierno es casi toda carne y pescado: reno, potro, pescado del río. Muchas veces se come congelado, cortado en virutas finas.",
  ph('Oymyakon frozen eyelashes', at='Las pestañas'),
  vd('frozen breath winter cold', at='El vaho'),
  ph('stroganina frozen fish Yakutia', at='cortado en virutas', lt=['Stroganina', 'pescado congelado en virutas · Yakutia']))
R('T1', "El vaho era tan espeso como el humo de un puro. Tenía que aguantar la respiración para hacer cada foto.",
  Q('El vaho era tan espeso como el humo de un puro. Tenía que aguantar la respiración para hacer cada foto.', 'Amos Chapple, fotógrafo · traducción', at='El vaho era tan espeso'))
N("[short pause] Bolot Bochkarev, vecino de la zona, se lo explicaba así al canal estadounidense The Weather Channel:",
  ph('Yakutia people traditional', at='Bolot Bochkarev'))
R('T3', "A los yakutos nos encanta la comida fría: el pescado ártico crudo y congelado, el hígado de caballo crudo y congelado. Pero eso se considera un manjar. En el día a día, lo que nos gusta es la sopa con carne.",
  Q('Nos encanta la comida fría. Pero eso es un manjar. En el día a día, lo que nos gusta es la sopa con carne.', 'Bolot Bochkarev, vecino de Yakutia · The Weather Channel · traducción', at='A los yakutos'))
N("Y luego está la escuela. La única del pueblo solo cierra a los más pequeños cuando el termómetro baja de cincuenta y dos bajo cero. Los mayores siguen yendo a clase hasta los cincuenta y seis.",
  ph('Oymyakon school', at='Y luego está la escuela'),
  cd(dict(type='list', header='¿Hay clase hoy?', items=['Hasta −52 °C: todos a clase', 'Menos de −52 °C: los pequeños en casa', 'Menos de −56 °C: se queda en casa todo el mundo']), at='solo cierra'))
C("En enero de dos mil dieciocho, el termómetro digital que se había instalado en el pueblo para los turistas marcó sesenta y dos bajo cero. Y se rompió. [short pause] Ese día, sí, se cerraron las escuelas de toda la región.",
  ph('Oymyakon digital thermometer', at='el termómetro digital'),
  K('SE ROMPIÓ', 'Oymyakon monument pole of cold', at='Y se rompió'))
C("La vida diaria tiene sus propias reglas. Las tuberías de agua se congelarían bajo tierra, así que en muchas casas el baño está fuera, en una caseta del patio. Y hasta enterrar a un muerto es un trabajo de días: el suelo está tan duro que hay que ablandarlo antes con fuego.",
  ph('Oymyakon wooden house winter', at='La vida diaria'),
  ph('Yakutia outhouse winter', at='el baño está fuera'),
  ph('Oymyakon cemetery', at='hasta enterrar a un muerto'))
N("Y, sin embargo, Oimiakón no es un lugar helado todo el año. En verano, el termómetro puede superar los treinta grados. Entre el día más frío y el más caluroso hay casi cien grados de diferencia. Pocos lugares habitados del planeta tienen un contraste así.",
  ph('Oymyakon summer', at='En verano'),
  cd(dict(type='versus', title='Un año en Oimiakón', left=dict(name='Invierno', lines=['récord: −67,7 °C', 'tres horas de luz en diciembre']), right=dict(name='Verano', lines=['más de 30 °C', 'veintiuna horas de luz en junio'])), at='casi cien grados'))
C("Y el frío extremo también está cambiando. En dos mil dieciocho, Alexander Arzhakov le decía a la agencia rusa RIA Novosti:",
  ph('Oymyakon landscape winter valley', at='también está cambiando'))
R('T2', "Llevamos observando el cambio climático todos los años desde los años ochenta. Cada año hace más calor.",
  Q('Cada año hace más calor.', 'Alexander Arzhakov · RIA Novosti, 2018 · traducción', at='Llevamos observando'))
C("[short pause] En Yakutia cuentan una leyenda: cuando Dios estaba creando la Tierra y repartía el hielo por el mundo, se le quedaron las manos tan frías que lo dejó caer todo aquí. En Oimiakón.",
  ph('Oymyakon winter landscape snow', at='En Yakutia cuentan una leyenda'),
  K('LO DEJÓ CAER AQUÍ', 'Oymyakon frost trees', at='lo dejó caer todo aquí'))
N("Lo curioso es el nombre. Oimiakón vendría de una palabra del pueblo even que significa «agua que no se congela»: un manantial donde los peces pasan el invierno. [pause] El lugar más frío del mundo se llama, literalmente, como un agua que nunca se hiela.",
  ph('Indigirka river winter', at='Lo curioso es el nombre'),
  ph('Oymyakon pole of cold monument', at='El lugar más frío', lt=['Monumento al Polo del Frío', 'Oimiakón']))
C("A unos novecientos kilómetros por carretera está la capital de Yakutia. Allí el frío se queda bajo los cimientos. Y una ciudad entera depende de que el suelo siga congelado.",
  ph('Kolyma highway road of bones winter', at='A unos novecientos', lt=['Carretera de Kolimá', 'Yakutia · hoy']),
  ph('Yakutsk city winter fog', at='una ciudad entera'))
N("Esa carretera tiene un nombre terrible: la llaman la carretera de los huesos. La construyeron, en tiempos de Stalin, presos de los campos de trabajo del Gulag. Muchos murieron durante las obras. Hoy sigue siendo la única vía terrestre que une esta parte de Siberia con el resto del país.",
  ph('Kolyma highway', at='la carretera de los huesos', lt=['Carretera de Kolimá', 'la «carretera de los huesos»']),
  ph('Kolyma highway Gulag history', at='presos de los campos'))
M('frio', 8)

# ---------------- 3 · YAKUTSK ----------------
T('Sobre hielo', 'Yakutsk, Rusia', secs=4.5, sting='tension')
N("Yakutsk tiene unos trescientos mil habitantes. Está considerada la ciudad grande más fría del planeta. Y es la mayor construida sobre permafrost.",
  MAPA('Yakutsk', 129.73, 62.03, 'Yakutsk', span=30, at='Yakutsk tiene'),
  ph('Yakutsk panorama', at='unos trescientos mil', lt=['Yakutsk', 'capital de Yakutia']),
  ph('Yakutsk winter street', at='la ciudad grande más fría'))
C("El récord de la ciudad está en sesenta y cuatro grados bajo cero. En enero, la máxima del día muchas veces no pasa de los treinta y cinco bajo cero. Y aun así, la vida sigue: autobuses, colegios, tiendas, universidades. Una ciudad normal… en un congelador.",
  ph('Yakutsk winter bus stop', at='la vida sigue'),
  K('UN CONGELADOR', 'Yakutsk frost street', at='en un congelador'))
R('DOC', "Permafrost: suelo que permanece congelado durante al menos dos años seguidos. En Yakutia puede tener cientos de metros de espesor.",
  cd(dict(type='doc', title='Permafrost', lines=['Suelo que permanece congelado al menos dos años seguidos.'], source='Definición geológica'), at='Permafrost'))
C("Ese hielo es la roca sobre la que se apoya la ciudad. Mientras esté duro, aguanta lo que le eches. Pero un edificio normal calienta el suelo que tiene debajo. El hielo se funde, la tierra se convierte en barro, y los cimientos se agrietan.",
  ph('permafrost ice layer', at='Ese hielo'),
  ph('Yakutsk cracked building', at='los cimientos se agrietan'))
N("Por eso, en Yakutsk, los bloques de viviendas de la época soviética no tocan el suelo. Se levantan sobre pilotes de hormigón clavados en el permafrost, con un hueco por debajo para que corra el aire helado.",
  ph('Yakutsk apartment building on stilts', at='no tocan el suelo'),
  ph('Yakutsk piles foundation building', at='Se levantan sobre pilotes', lt=['Edificio sobre pilotes', 'Yakutsk']))
C("En los años sesenta, la norma era clavar esos pilotes unos seis metros. Hoy no siempre basta. Según los científicos del Instituto Melnikov del Permafrost, que tiene su sede aquí, la temperatura media de la ciudad ha subido dos grados y medio en una década.",
  ph('Melnikov Permafrost Institute Yakutsk', at='Instituto Melnikov', lt=['Instituto Melnikov del Permafrost', 'Yakutsk']),
  cd(dict(type='counter', to=2.5, prefix='+', label='grados en una década · Yakutsk'), at='dos grados y medio'))
N("[short pause] En dos mil dieciocho, Eduard Romanov le enseñó a la agencia France Presse una viga hundida y agrietada bajo nueve pisos de viviendas. Y le dijo esto:",
  ph('Yakutsk panel apartment block', at='Eduard Romanov'))
R('T3', "Todo Yakutsk está en peligro. Los propietarios pueden perder su vivienda. Y nadie está preparado para esto.",
  Q('Todo Yakutsk está en peligro. Y nadie está preparado para esto.', 'Eduard Romanov · AFP, 2018 · traducción', at='Todo Yakutsk'))
C("Algunos bloques ya se han tenido que derribar. Uno de ellos, el número diecinueve, se inclinó cuarenta y dos centímetros. Irina vive cerca y lo contó al diario The Irish Times.",
  ph('Yakutsk demolished building', at='Algunos bloques'),
  cd(dict(type='counter', to=42, prefix='', label='centímetros de inclinación · bloque 19'), at='cuarenta y dos centímetros'))
R('TF', "Yo no vivo en ese edificio, por suerte, y mi bloque parece que está bien por ahora. Pero a todos nos preocupa lo que pueda pasar aquí.",
  Q('A todos nos preocupa lo que pueda pasar aquí.', 'Irina, vecina de Yakutsk · The Irish Times · traducción', at='Yo no vivo'))
N("Y hay otra cosa que llama la atención en Yakutsk: las tuberías. La calefacción y el agua caliente no van enterradas, porque derretirían el suelo. Van por fuera, forradas, recorriendo las calles a la vista de todos.",
  ph('Yakutsk heating pipes above ground', at='las tuberías'),
  ph('Yakutsk pipes street', at='Van por fuera'))
C("Además, Yakutsk está en la orilla del río Lena, y todavía no hay un puente que lo cruce. En verano se pasa en ferri. En invierno, el río helado se convierte en carretera. [short pause] Entre una cosa y otra, hay semanas en que el río no se puede cruzar.",
  ph('Lena river Yakutsk', at='el río Lena', lt=['Río Lena', 'Yakutsk']),
  ph('Lena river ice road', at='En invierno'),
  ph('Lena river ferry Yakutsk', at='En verano'))
C("En invierno, la ciudad se cubre con una niebla helada que no se levanta: el vapor de los coches, las casas y las personas se congela en el aire y se queda flotando entre los edificios. En los mercados, el pescado se vende al aire libre, tieso como un palo, apilado de pie.",
  ph('Yakutsk ice fog', at='una niebla helada'),
  ph('Yakutsk frozen fish market', at='En los mercados', lt=['Mercado de Yakutsk', 'pescado congelado al aire libre']))
N("Y el permafrost guarda sorpresas. Por toda Yakutia aparecen restos de mamuts lanudos, congelados durante miles de años. Algunos están tan bien conservados que aún tienen piel y pelo. Yakutsk tiene incluso un museo dedicado a ellos.",
  ph('mammoth Yakutia permafrost', at='restos de mamuts'),
  ph('Yakutsk Mammoth Museum', at='un museo dedicado', lt=['Museo del Mamut', 'Yakutsk']))
N("¿Y por qué tanta gente aquí? Primero fueron las pieles, desde el siglo diecisiete. Luego, el oro. Y, sobre todo, los diamantes de Yakutia, descubiertos en los años cincuenta. [pause] Debajo del hielo hay riqueza. Y la riqueza siempre atrae a la gente. Lo vamos a ver todavía más claro en el siguiente lugar. Una ciudad a la que, durante décadas, casi nadie podía entrar.",
  ph('Yakutsk fortress wooden tower', at='Primero fueron las pieles'),
  ph('Mir diamond mine Mirny', at='los diamantes de Yakutia', lt=['Mina de diamantes Mir', 'Yakutia']),
  ph('Norilsk city', at='Una ciudad a la que'))
M('frio', 8)
