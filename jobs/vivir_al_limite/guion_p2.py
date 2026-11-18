# -*- coding: utf-8 -*-
# «Vivir al límite» · parte 2: Norilsk, recapitulación, Longyearbyen, Whittier, Aogashima
from lib import *

# ---------------- 4 · NORILSK ----------------
T('La ciudad cerrada', 'Norilsk, Rusia', secs=4.5, sting='tension')
B('industria')
N("Siberia, por encima del círculo polar ártico. Norilsk tiene unos ciento setenta y cinco mil habitantes y es la ciudad de más de cien mil habitantes más al norte del planeta. No hay carretera que la una con el resto de Rusia. Se llega en avión, o por el río Yeniséi en verano. [short pause] Y, si eres extranjero, solo con un permiso especial.",
  MAPA('Norilsk', 88.2, 69.35, 'Norilsk', span=30, at='Siberia, por encima'),
  ph('Norilsk panorama', at='Norilsk tiene', lt=['Norilsk', 'Krai de Krasnoyarsk, Rusia']),
  ph('Norilsk airport Alykel', at='Se llega en avión'),
  K('CIUDAD CERRADA', 'Norilsk winter street', at='un permiso especial'))
C("Norilsk es una ciudad cerrada desde dos mil uno. Pero su historia empezó mucho antes, y de la peor manera. En mil novecientos treinta y cinco, la Unión Soviética abrió aquí un campo de trabajos forzados del Gulag: el Norillag.",
  ph('Norillag Gulag memorial Norilsk', at='un campo de trabajos forzados', lt=['Memorial del Norillag', 'Norilsk']),
  cd(dict(type='timeline', header='Norilsk', events=[['1935', 'se abre el campo del Norillag'], ['1951', 'unos 72.500 presos'], ['1956', 'cierra el campo'], ['2001', 'ciudad cerrada a extranjeros'], ['2020', 'vertido de gasóleo']]), at='En mil novecientos treinta y cinco'))
N("Los presos construyeron las minas, las fundiciones y la propia ciudad, sobre el permafrost y a temperaturas de cuarenta bajo cero. En mil novecientos cincuenta y uno llegó a haber unos setenta y dos mil quinientos. El campo se cerró en mil novecientos cincuenta y seis. Muchos supervivientes se quedaron a vivir aquí el resto de su vida.",
  ph('Norilsk Gulag prisoners history', at='Los presos construyeron'),
  cd(dict(type='counter', to=72500, label='presos en el Norillag en 1951'), at='setenta y dos mil quinientos'),
  ph('Norilsk old town Leninsky prospekt', at='Muchos supervivientes'))
C("¿Por qué aquí? Por lo que hay bajo tierra. Los yacimientos de Norilsk y Talnaj son los mayores conocidos del mundo de níquel, cobre y paladio. Ese paladio acaba en los catalizadores de los coches de medio planeta.",
  ph('Norilsk Nickel plant', at='Por lo que hay bajo tierra'),
  ph('palladium metal', at='Ese paladio'))
R('DOC', "La luz en la ventana de Rusia.",
  Q('La luz en la ventana de Rusia', 'Himno de la compañía Norilsk Nickel, citado por The Moscow Times', at='La luz'))
N("Así llama el himno de la empresa minera a sus fundiciones. [pause] Pero durante décadas, esa luz salía de unas chimeneas que convirtieron Norilsk en uno de los lugares más contaminados de la Tierra. Los satélites detectaban el dióxido de azufre desde el espacio. Ninguna otra instalación humana emitía tanto.",
  ph('Norilsk smoke stacks', at='esa luz salía'),
  ph('Norilsk sulfur dioxide satellite NASA', at='Los satélites'),
  K('DIÓXIDO DE AZUFRE', 'Norilsk smelter pollution', at='Ninguna otra'))
C("Alrededor de la ciudad, kilómetros y kilómetros de bosque muerto. Lluvia ácida. Ríos teñidos de rojo. Y en mayo de dos mil veinte, el permafrost cedió bajo un depósito de combustible de una central eléctrica. Se derramaron más de veinte mil toneladas de gasóleo: el mayor vertido de la historia del Ártico.",
  ph('Norilsk dead forest', at='bosque muerto'),
  ph('Norilsk 2020 diesel spill Ambarnaya river', at='en mayo de dos mil veinte', lt=['Río Ambárnaya', 'vertido de 2020']),
  cd(dict(type='counter', to=21000, label='toneladas de gasóleo vertidas · 2020'), at='veinte mil toneladas'))
N("[short pause] Igor Klyushin llegó a Norilsk con siete años, en mil novecientos setenta y siete. Hoy es activista medioambiental. En dos mil dieciséis vio el río Daldikán teñido de rojo. Se lo contó a la periodista Marianne Lavelle, de la revista Undark:",
  ph('Daldykan river red Norilsk 2016', at='el río Daldikán', lt=['Río Daldikán', 'Norilsk · 2016']))
R('T3', "Cuando fui aquella noche a ver el Daldikán, se me cayó el alma a los pies. Se me rompió el corazón.",
  Q('Cuando fui aquella noche a ver el Daldikán, se me rompió el corazón.', 'Igor Klyushin, activista · Undark, 2021 · traducción', at='Cuando fui aquella noche'))
C("Valeriya Bolgova es líder de los nganasanos, uno de los pueblos indígenas de la península de Taimyr. Vive en una aldea cercana. Después de una visita a Norilsk, lo resumió así:",
  ph('Nganasan people Taymyr', at='los nganasanos', lt=['Pueblo nganasán', 'península de Taimyr']))
R('TF', "Allí no se puede respirar. Fui tosiendo todo el camino de vuelta a casa.",
  Q('Allí no se puede respirar. Fui tosiendo todo el camino de vuelta a casa.', 'Valeriya Bolgova, líder nganasana · Undark, 2021 · traducción', at='Allí no se puede respirar'))
N("Vasily Ryabinin fue subdirector de la oficina de Norilsk de la agencia rusa de protección del medio ambiente. Creció en el barrio vecino de Talnaj. En esa misma revista, lo resumió con un dicho:",
  ph('Talnakh Norilsk district', at='Talnaj', lt=['Talnaj', 'Norilsk']))
R('T2', "En ruso tenemos un dicho: es como tirar guisantes secos contra la pared.",
  Q('Es como tirar guisantes secos contra la pared.', 'Vasily Ryabinin, exinspector ambiental · Undark, 2021 · traducción', at='En ruso tenemos un dicho'))
N("Según la prensa rusa, la situación ha mejorado: en dos mil dieciséis cerró la fundición más antigua, y en dos mil veintitrés Norilsk salió por primera vez de la lista oficial de ciudades con contaminación muy alta. Hay que tomarlo con cautela: casi todo lo que sabemos de Norilsk lo cuentan las autoridades o la propia empresa.",
  cd(dict(type='split', left=dict(title='Lo que dicen', lines=['cierre de la fundición más antigua (2016)', 'fuera de la lista de contaminación muy alta (2023)']), right=dict(title='La cautela', lines=['ciudad cerrada', 'pocas fuentes independientes']), strike=False), at='Según la prensa rusa'))
N("El clima no ayuda. Norilsk pasa más de doscientos días al año bajo la nieve. Las ventiscas pueden paralizar la ciudad durante días. Por eso muchos barrios se diseñaron como manzanas cerradas, con los edificios formando un muro alrededor de un patio, para frenar el viento.",
  ph('Norilsk blizzard winter', at='Las ventiscas'),
  ph('Norilsk courtyard apartment blocks aerial', at='manzanas cerradas'))
C("Y, como en Yakutsk, todo se levanta sobre pilotes clavados en el permafrost. Con el deshielo, muchos edificios se han agrietado. Desde principios de este siglo apenas se ha construido vivienda nueva, y hay bloques enteros abandonados.",
  ph('Norilsk abandoned building', at='bloques enteros abandonados'),
  ph('Norilsk building piles', at='sobre pilotes'))
C("¿Y por qué se vive aquí? Por los sueldos, mucho más altos que en el resto del país. Y porque, para muchas familias, Norilsk es simplemente su casa. [short pause] Edificios de colores para alegrar el invierno, una de las mezquitas más septentrionales del mundo y semanas enteras sin que salga el sol.",
  ph('Norilsk colorful buildings', at='Edificios de colores'),
  ph('Norilsk mosque Nurd Kamal', at='una de las mezquitas', lt=['Mezquita Nurd Kamal', 'Norilsk']),
  vd('arctic city winter night lights', at='semanas enteras'))
M('industria', 8)

# ---------------- RECAPITULACIÓN 1 ----------------
B('tema')
N("Llevamos cuatro lugares. Para no perdernos: en Coober Pedy se excava para huir del calor. En Oimiakón, el frío decide si hay clase. En Yakutsk, la ciudad entera depende de que el suelo siga helado. Y en Norilsk, la riqueza del subsuelo levantó una ciudad que durante años nadie podía visitar.",
  cd(dict(type='recap', title='Hasta aquí', items=[['Coober Pedy', 'bajo tierra contra el calor'], ['Oimiakón', '−67,7 °C, el polo del frío'], ['Yakutsk', 'una ciudad sobre hielo'], ['Norilsk', 'níquel, Gulag y ciudad cerrada']]), at='Llevamos cuatro lugares'))
C("Ahora subimos todavía más al norte. A un lugar donde no hace tanto frío como en Siberia. Pero donde, durante casi cuatro meses al año, el sol no sale.",
  vd('polar night arctic', at='Ahora subimos'))

# ---------------- 5 · LONGYEARBYEN ----------------
T('La noche polar', 'Longyearbyen, Noruega', secs=4.5, sting='tension')
B('noche')
N("Archipiélago de Svalbard, a mitad de camino entre Noruega y el Polo Norte. Longyearbyen tiene unos dos mil quinientos habitantes y presume de tenerlo todo «más al norte del mundo»: la escuela, el hospital, la universidad.",
  MAPA('Longyearbyen', 15.63, 78.22, 'Longyearbyen', span=25, at='Archipiélago de Svalbard'),
  vd('Longyearbyen Svalbard', at='Longyearbyen tiene', lt=['Longyearbyen', 'Svalbard, Noruega · hoy']),
  ph('Longyearbyen houses colorful', at='presume de tenerlo todo'))
C("A finales de octubre, el sol se esconde tras el horizonte. Y no vuelve a asomar hasta mediados de febrero. Durante las semanas centrales, ni siquiera hay claridad a mediodía. Es la noche polar.",
  ph('Longyearbyen polar night town', at='A finales de octubre'),
  cd(dict(type='timeline', header='El año en Longyearbyen', events=[['finales de octubre', 'último sol'], ['noviembre-enero', 'noche polar'], ['mediados de febrero', 'vuelve el sol'], ['8 de marzo', 'el sol toca la escalera del viejo hospital'], ['abril-agosto', 'sol de medianoche']]), at='Y no vuelve'))
N("Cuando por fin vuelve, el pueblo lo celebra. Hay una fecha marcada: el ocho de marzo, cuando el sol llega a iluminar los escalones del antiguo hospital. [short pause] Y en verano ocurre lo contrario: de abril a agosto, el sol no se pone nunca.",
  ph('Longyearbyen old hospital steps', at='el ocho de marzo'),
  vd('midnight sun arctic', at='en verano'))
C("Pero el peligro aquí no es la oscuridad. Es el oso polar. En las afueras del pueblo, unas señales con fondo negro marcan el límite. Más allá, nadie sensato camina sin un rifle y una pistola de bengalas.",
  ph('polar bear Svalbard', at='Es el oso polar'),
  ph('Longyearbyen polar bear warning sign', at='unas señales', lt=['Señal de peligro de oso polar', 'Longyearbyen']),
  K('RIFLE', 'Svalbard rifle polar bear protection', at='sin un rifle'))
N("Dentro del pueblo, las armas no se pueden llevar cargadas ni entrar en los edificios. Pero los osos no leen las normas. En Navidad de dos mil diecinueve, uno bajó tranquilamente por la calle principal hasta que la policía lo espantó.",
  ph('Longyearbyen main street winter', at='la calle principal'))
C("Y luego está la leyenda más famosa de Longyearbyen. La repiten guías, periódicos y viajeros. La guía Hella Liira se la explicaba así a un periodista:",
  ph('Longyearbyen cemetery', at='la leyenda más famosa'))
R('TF', "El gobierno, sencillamente, no lo permite.",
  Q('Aquí está prohibido morir. El gobierno, sencillamente, no lo permite.', 'Hella Liira, guía · Traveller · traducción', at='El gobierno'))
N("[pause] Prohibido morir. Suena a broma, pero tiene una base real. El pequeño cementerio dejó de recibir entierros a mediados del siglo veinte, porque el permafrost no deja que los cuerpos se descompongan. En mil novecientos noventa y ocho, unos científicos llegaron a exhumar víctimas de la gripe de mil novecientos dieciocho para estudiar el virus.",
  K('PROHIBIDO MORIR', 'Longyearbyen cemetery crosses', at='Prohibido morir'),
  ph('Longyearbyen cemetery crosses', at='El pequeño cementerio', lt=['Cementerio de Longyearbyen', 'Svalbard']),
  cd(dict(type='timeline', header='El cementerio helado', events=[['1918', 'víctimas de la gripe española'], ['mediados del s. XX', 'se dejan de hacer entierros'], ['1998', 'exhumación científica']]), at='En mil novecientos noventa y ocho'))
R('DOC', "Si tiene la desgracia de enfermar de gravedad, cuente con que lo enviarán en avión o en barco a otra parte de Noruega para terminar allí sus días.",
  cd(dict(type='doc', title='BBC News, 2008', lines=['«Lo enviarán en avión o en barco a otra parte de Noruega para terminar allí sus días.»'], source='Duncan Bartlett, BBC · traducción'), at='Si tiene la desgracia'))
C("Pero no hay ninguna ley que lo prohíba. Lo que ocurre es más prosaico: quien enferma de gravedad es trasladado al continente. Y las embarazadas suelen viajar semanas antes del parto para dar a luz en Noruega.",
  cd(dict(type='split', left=dict(title='La leyenda', lines=['«está prohibido morir»']), right=dict(title='La realidad', lines=['no hay ninguna ley', 'los enfermos graves y los partos van al continente'])), at='no hay ninguna ley'))
C("La misma crónica de la BBC contaba otro detalle: cuando los niños de la guardería salen de excursión fuera del pueblo, la maestra lleva un arma. Y en la universidad, el primer día de clase de cada estudiante se dedica a aprender a disparar.",
  ph('Longyearbyen kindergarten', at='los niños de la guardería'),
  ph('University Centre in Svalbard UNIS', at='en la universidad', lt=['Centro Universitario de Svalbard', 'Longyearbyen']))
N("Longyearbyen nació como pueblo minero del carbón, a principios del siglo veinte. Hoy vive de la ciencia y del turismo. Y guarda un tesoro bajo una montaña: la Bóveda Global de Semillas, abierta en dos mil ocho, con copias de seguridad de los cultivos del mundo entero.",
  ph('Longyearbyen coal mine historic', at='pueblo minero del carbón'),
  ph('Svalbard Global Seed Vault', at='la Bóveda Global de Semillas', lt=['Bóveda Global de Semillas de Svalbard', 'abierta en 2008']))
N("El cambio climático también se nota aquí. Svalbard es una de las regiones del planeta que más rápido se calientan. En diciembre de dos mil quince, un alud cayó sobre varias casas de Longyearbyen y mató a dos personas. Y en dos mil diecisiete, el agua del deshielo llegó a meterse en el túnel de entrada de la Bóveda de Semillas.",
  ph('Longyearbyen avalanche 2015', at='un alud', lt=['Longyearbyen', 'alud de diciembre de 2015']),
  ph('Svalbard Global Seed Vault entrance', at='el túnel de entrada'))
C("Y aun así, la gente llega. Hay vecinos de más de cincuenta países. Muchos vienen unos años, por trabajo o por aventura, y se van. Otros se quedan. Dicen que la noche polar no es negra: es azul, con auroras boreales que bailan sobre el fiordo.",
  vd('northern lights aurora Svalbard', at='es azul'),
  ph('Longyearbyen aurora', at='auroras boreales'))
N("Y hay un detalle legal que hace de Longyearbyen un lugar único. Por el Tratado de Svalbard, firmado en mil novecientos veinte, los ciudadanos de los países firmantes pueden vivir y trabajar en el archipiélago sin visado. Eso sí: tienen que demostrar que pueden mantenerse. Aquí no hay red de ayudas sociales para quien se queda sin trabajo.",
  cd(dict(type='doc', title='Tratado de Svalbard · 1920', lines=['Los ciudadanos de los países firmantes pueden vivir y trabajar en el archipiélago.'], source='Tratado de Svalbard, 9 de febrero de 1920'), at='Por el Tratado de Svalbard'),
  ph('Longyearbyen town summer', at='tienen que demostrar'))
C("Hay más rarezas. Las calles no tienen nombre, tienen número. Y los gatos están prohibidos, para proteger a las aves. [short pause] De la oscuridad total pasamos ahora a un pueblo de Alaska con un problema muy distinto: casi todos sus vecinos duermen bajo el mismo techo.",
  ph('Longyearbyen street road number', at='Las calles no tienen nombre'),
  ph('Svalbard birds Arctic tern', at='para proteger a las aves'),
  ph('Begich Towers Whittier Alaska', at='bajo el mismo techo'))
M('noche', 8)

# ---------------- 6 · WHITTIER ----------------
T('Un pueblo en un edificio', 'Whittier, Alaska', secs=4.5, sting='tension')
B('frio')
N("Alaska, a un centenar de kilómetros de Anchorage. Whittier está encajado entre montañas y un fiordo del estrecho del Príncipe Guillermo. En el censo de dos mil veinte tenía doscientos setenta y dos habitantes. Y casi todos viven en un mismo edificio de catorce plantas: las Begich Towers.",
  MAPA('Whittier', -148.68, 60.77, 'Whittier', span=20, at='Alaska, a un centenar'),
  vd('Whittier Alaska', at='Whittier está encajado', lt=['Whittier', 'Alaska · hoy']),
  ph('Begich Towers', at='las Begich Towers', lt=['Begich Towers', '14 plantas · terminadas en 1957']))
C("El edificio lo levantó el ejército de Estados Unidos durante la Guerra Fría y se terminó en mil novecientos cincuenta y siete. Era cuartel y vivienda para las familias de los militares. Cuando el ejército se fue, el edificio se convirtió en un bloque de pisos.",
  ph('Whittier Alaska army base history', at='el ejército de Estados Unidos'),
  ph('Buckner Building Whittier abandoned', at='Cuando el ejército se fue', lt=['Edificio Buckner', 'abandonado · Whittier']))
C("Muy cerca sigue en pie, abandonado, el otro gigante del pueblo: el edificio Buckner, terminado en mil novecientos cincuenta y tres. En su día lo llamaron «la ciudad bajo un mismo techo». Hoy es una mole de hormigón vacía, con las ventanas rotas, mirando al fiordo.",
  ph('Buckner Building Whittier', at='el edificio Buckner', lt=['Edificio Buckner', 'abandonado desde los años sesenta']))
N("Hoy, dentro de las Begich Towers hay casi todo lo que necesita un pueblo: viviendas, oficinas municipales, una pequeña tienda, la oficina de correos. Y un túnel subterráneo que lleva directamente a la escuela, para que los niños no tengan que salir a la calle en invierno.",
  ph('Begich Towers interior hallway', at='dentro de las Begich Towers'),
  ph('Whittier school tunnel', at='un túnel subterráneo'))
C("Porque fuera, el clima es feroz. Whittier recibe de media unos cinco mil litros de precipitación por metro cuadrado al año, una de las cifras más altas de Estados Unidos. Las ráfagas de viento pueden superar los ciento veinte kilómetros por hora.",
  vd('Alaska rain storm fjord', at='el clima es feroz'),
  cd(dict(type='counter', to=5000, label='litros por metro cuadrado al año · Whittier'), at='cinco mil litros'))
N("[short pause] La periodista Jen Kinney pasó una temporada aquí. Su conclusión fue sencilla: con ese viento y hasta diecisiete metros de nieve en un año, es muy fácil no salir de las Begich Towers durante días. O semanas.",
  ph('Whittier Alaska snow deep', at='hasta diecisiete metros de nieve'))
N("Y para entrar o salir por tierra solo hay un camino: el túnel Anton Anderson. Cuatro kilómetros de un solo carril, por el que pasan, por turnos, coches y trenes. Cambia de sentido cada media hora. [short pause] Y por la noche, se cierra.",
  ph('Anton Anderson Memorial Tunnel', at='el túnel Anton Anderson', lt=['Túnel Anton Anderson', 'único acceso por carretera']),
  vd('Whittier tunnel', at='Cuatro kilómetros'),
  K('SE CIERRA', 'Whittier tunnel entrance night', at='se cierra'))
C("En invierno, el túnel abre a las siete de la mañana y la última pasada es antes de las once de la noche. Si la pierdes, te quedas al otro lado de la montaña hasta el día siguiente. Antes de que el túnel se abriera a los coches, en el año dos mil, a Whittier solo se llegaba en tren, en barco o en avioneta.",
  cd(dict(type='list', header='Túnel de Whittier · invierno', items=['Abre a las 7:00', 'Un sentido cada media hora', 'Coches y trenes por turnos', 'Última pasada antes de las 23:00']), at='En invierno'),
  ph('Whittier harbor boats', at='en barco'))
N("No todo el mundo aguanta. Arnie vivió en las Begich Towers y se mudó. Cuando la periodista Jen Kinney le preguntó por el edificio, contestó esto:",
  ph('Whittier Alaska town view', at='No todo el mundo aguanta'))
R('T2', "Yo lo llamo la cueva de los murciélagos. Porque hay que estar más chiflado que una cabra para vivir ahí.",
  Q('Yo lo llamo la cueva de los murciélagos. Hay que estar más chiflado que una cabra para vivir ahí.', 'Arnie, antiguo vecino · Jen Kinney, Business Insider · traducción', at='Yo lo llamo'))
C("Whittier también sabe lo que es una catástrofe. El veintisiete de marzo de mil novecientos sesenta y cuatro, el gran terremoto de Alaska, de magnitud nueve coma dos, provocó olas que arrasaron el puerto. En Whittier murieron trece personas.",
  ph('1964 Alaska earthquake Whittier damage', at='el gran terremoto de Alaska', lt=['Terremoto de Alaska', '27 de marzo de 1964']),
  cd(dict(type='counter', to=9.2, label='magnitud · terremoto de Alaska de 1964'), at='magnitud nueve coma dos'))
N("Por eso hoy el túnel peatonal que sube del puerto a las torres está señalizado como ruta de evacuación en caso de tsunami. En un pueblo así, el edificio no es solo una casa. Es también el refugio.",
  ph('Whittier tsunami evacuation route sign', at='ruta de evacuación', lt=['Ruta de evacuación', 'Whittier']),
  ph('Begich Towers Whittier mountains', at='Es también el refugio'))
C("Pero otros lo ven al revés: un pueblo donde todo el mundo se conoce y donde el vecino está a un ascensor de distancia. En verano llegan los cruceros y la población se multiplica. En invierno, vuelve a ser una comunidad de unos pocos cientos de personas dentro de una torre. [short pause] Y ahora nos vamos al otro lado del Pacífico. A una isla que, literalmente, vive dentro de un volcán.",
  ph('Whittier cruise ship harbor', at='En verano llegan los cruceros'),
  ph('Begich Towers winter', at='dentro de una torre'),
  ph('Aogashima aerial', at='dentro de un volcán'))
M('frio', 8)

# ---------------- 7 · AOGASHIMA ----------------
T('Dentro del volcán', 'Aogashima, Japón', secs=4.5, sting='tension')
B('isla')
N("Mar de Filipinas, a unos trescientos cincuenta kilómetros al sur de Tokio. Aogashima es la isla habitada más meridional y más aislada del archipiélago de Izu. Y, aunque parezca increíble, administrativamente pertenece a la ciudad de Tokio.",
  MAPA('Aogashima', 139.76, 32.46, 'Aogashima', span=10, at='Mar de Filipinas'),
  ph('Aogashima island', at='Aogashima es la isla', lt=['Aogashima', 'islas Izu, Tokio']),
  ph('Aogashima cliffs sea', at='administrativamente'))
C("Desde el aire se entiende todo. Es un volcán que sale del mar, con acantilados por todos lados. Dentro tiene una gran caldera, la de Ikenosawa. Y en el centro de esa caldera, otro volcán más pequeño: el Maruyama.",
  ph('Aogashima double caldera aerial', at='Desde el aire'),
  ph('Ikenosawa caldera Aogashima', at='la de Ikenosawa', lt=['Caldera de Ikenosawa', 'Aogashima']),
  ph('Maruyama Aogashima cone', at='el Maruyama', lt=['Monte Maruyama', 'cono dentro de la caldera']))
N("Ese cono interior nació de la última gran erupción, entre mil setecientos ochenta y mil setecientos ochenta y cinco. Fue una tragedia. En mil setecientos ochenta y cinco, de los trescientos veintisiete habitantes de la isla murieron entre ciento treinta y ciento cuarenta. Los demás huyeron.",
  cd(dict(type='timeline', header='Aogashima', events=[['1780', 'empieza la erupción'], ['1783', 'evacuación por la lava'], ['1785', 'gran erupción: unos 130-140 muertos'], ['hoy', 'unos 160 vecinos']]), at='Ese cono interior'),
  cd(dict(type='counter', to=327, label='habitantes en 1785 · murieron entre 130 y 140'), at='de los trescientos veintisiete'))
N("Imagínalo: una isla minúscula, sin puerto natural, rodeada de acantilados. Y de repente, la tierra empieza a escupir fuego por el centro. Los supervivientes huyeron en barcas hacia Hachijojima. Muchos otros no llegaron a tiempo a la costa.",
  ph('Aogashima cliffs coast', at='rodeada de acantilados'),
  K('FUEGO', 'Aogashima volcano crater', at='escupir fuego'))
C("Pasaron décadas antes de que la isla volviera a estar habitada del todo. Hoy viven en Aogashima unas ciento sesenta personas: es el municipio con menos habitantes de todo Japón. Y la Agencia Meteorológica Japonesa sigue considerando el volcán activo.",
  ph('Aogashima village houses', at='Hoy viven en Aogashima', lt=['Aldea de Aogashima', 'el municipio menos poblado de Japón']),
  K('VOLCÁN ACTIVO', 'Aogashima Maruyama steam', at='activo'))
N("¿Y cómo se llega? Primero hay que ir a Hachijojima, otra isla, a unos setenta kilómetros. Desde allí hay un helicóptero de veinte minutos, con pocas plazas y reserva previa. O un barco de unas tres horas que, con el mar bravo, se cancela muy a menudo: algunas guías calculan que solo sale la mitad de los días.",
  ph('Hachijojima island', at='Hachijojima', lt=['Hachijojima', 'escala obligatoria']),
  ph('Aogashima helicopter heliport', at='un helicóptero'),
  ph('Aogashima Sanpo port ferry', at='O un barco', lt=['Puerto de Sanpo', 'Aogashima']))
C("Pero vivir dentro de un volcán también tiene ventajas. Por las grietas de la caldera sale vapor caliente. Los vecinos lo llaman hingya. Antes de que llegara la electricidad se usaba para calentar y cocinar. Hoy alimenta una sauna geotérmica, un horno donde cualquiera puede cocer huevos y boniatos, y una pequeña fábrica de sal.",
  ph('Aogashima geothermal steam hingya', at='Los vecinos lo llaman hingya'),
  ph('Aogashima sauna', at='una sauna geotérmica', lt=['Sauna geotérmica', 'Aogashima']),
  ph('Aogashima salt hingya', at='una pequeña fábrica de sal'))
C("La vida diaria en una isla de ciento sesenta vecinos tiene su propio ritmo. Casi todo llega por mar: comida, combustible, materiales. Cuando el barco no puede atracar durante días, las estanterías de la tienda pueden quedarse vacías. Y los propios vecinos destilan su aguardiente, un shochu que se ha hecho famoso en todo Japón.",
  ph('Aogashima shochu', at='un shochu', lt=['Aochu', 'shochu de Aogashima']),
  ph('Aogashima road village', at='La vida diaria'))
N("Y quien llega se encuentra un paisaje que no parece de este mundo: dentro de la caldera, una selva de helechos gigantes; alrededor, paredes de roca que caen en vertical al océano; y en el centro, el pequeño volcán humeando, cubierto de vegetación. La única carretera atraviesa la pared del cráter por un túnel.",
  ph('Aogashima tree ferns caldera', at='una selva de helechos'),
  ph('Aogashima Maruyama forest', at='el pequeño volcán'),
  ph('Aogashima tunnel road', at='por un túnel'))
N("De noche, sin apenas luz artificial, el cielo de Aogashima es uno de los más limpios de Japón. [pause] Un volcán que mató a casi la mitad de sus vecinos se ha convertido en el corazón de la isla. Pero hay un lugar todavía más solitario. Una isla volcánica en mitad del Atlántico, donde no se puede llegar en avión.",
  ph('Aogashima starry sky night', at='De noche'),
  ph('Tristan da Cunha volcano Queen Mary Peak', at='mitad del Atlántico'))
M('isla', 8)
