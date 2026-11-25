# -*- coding: utf-8 -*-
# «El corralito argentino» · parte 2: la caldera, el estado de sitio y el helicóptero
from lib import *

# ---------------- III · LA CALDERA ----------------
T('La caldera', '6 · 18 de diciembre de 2001', num='III', secs=6.0, sting='accion')
B('calle')
NEW("Mientras tanto, en las provincias, la crisis llevaba tiempo hirviendo. Muchas no tenían con qué pagar a sus funcionarios y les pagaban con bonos, papelitos que valían como dinero solo dentro de la provincia. Los llamaban patacones, lecops, quebrachos.",
    ai('bonos_mano', 'a fan of colourful provincial bond notes held in a worried hand, compared against a single crisp banknote in the other hand, close-up', at='les pagaban con bonos'),
    cd(dict(type='list', header='Las cuasimonedas', items=[('Patacones', 'provincia de Buenos Aires'), ('Lecop', 'emitidos por la Nación'), ('Quebrachos', 'Chaco'), ('y una docena más', 'en otras provincias')]), at='patacones'))
CRO("Día doce. Miércoles. Grupos de desocupados cortan rutas en el conurbano de Buenos Aires: La Matanza, Florencio Varela, San Martín. Les llaman piqueteros.",
    DIA(12, 'del corralito · miércoles 12 de diciembre', at='Día doce', frm=5),
    ai('piquete_ruta', 'unemployed protesters blocking a highway with burning tires and wooden pallets, thick black smoke, a line of stopped trucks behind', at='cortan rutas'))
CRO("Día trece. Jueves. Huelga general, la séptima contra este Gobierno. Y por la noche, en los barrios de clase media de la capital, empieza a oírse un ruido nuevo. Metal contra metal. Desde los balcones.",
    DIA(13, 'del corralito · jueves 13 de diciembre', at='Día trece', frm=12),
    ai('balcon_cacerola', 'people on the balconies of a tall apartment building at night banging pots and pans, dozens of lit windows, the sound almost visible as lines', at='Desde los balcones'))
NAR("Ese mismo día, en Mendoza, más de cien personas entran a la fuerza en un supermercado y se llevan lo que pueden. Es el primero. Los saqueos saltan a Rosario, a Córdoba, a Entre Ríos.",
    ph('Mendoza Argentina ciudad', at='en Mendoza', lt=['Mendoza', 'Argentina'], lugar='mendoza'),
    ai('saqueo_super', 'a crowd forcing open the shutter of a supermarket, people running out with bags of flour, rice and cooking oil, chaotic motion, harsh daylight', at='se llevan lo que pueden'),
    cd(dict(type='map', title='La ola de saqueos · diciembre de 2001', bbox=[-71.5, -38.5, -56.5, -26.0], points=[dict(name='Mendoza', lon=-68.84, lat=-32.89, big=1), dict(name='Rosario', lon=-60.64, lat=-32.95, big=1), dict(name='Córdoba', lon=-64.18, lat=-31.42), dict(name='Paraná', lon=-60.52, lat=-31.73), dict(name='Buenos Aires', lon=-58.38, lat=-34.60, big=1)]), at='Los saqueos saltan'))
NEW("Lo que se llevaban no eran televisores. Eran harina, arroz, fideos, aceite. En algunos sitios, los propios supermercados empezaron a repartir comida en la puerta para que no les rompieran la persiana.",
    cd(dict(type='list', header='Lo que se llevaban', items=[('Harina', ''), ('Arroz', ''), ('Fideos', ''), ('Aceite', '')]), at='Eran harina, arroz'),
    ai('reparto_puerta', 'supermarket employees handing out bags of food through a half-open shutter to a crowd of reaching hands, tense but orderly', at='repartir comida en la puerta'))
NEW("Esos mismos días, organizaciones sociales y sindicatos montan una consulta popular por un seguro de desempleo. Votan millones de personas. Y las cacerolas de los balcones empiezan a sonar cada noche un poco más fuerte.",
    ai('urnas_calle', 'ballot boxes set up on folding tables on a busy sidewalk, long lines of working people waiting to vote, a sense of urgency', at='una consulta popular'))
CRO("Día dieciséis. Domingo. El presidente insiste en público: ni devaluación, ni dolarización. El uno a uno se mantiene.",
    DIA(16, 'del corralito · domingo 16 de diciembre', at='Día dieciséis', frm=13),
    ph('Fernando de la Rúa', at='El presidente insiste', lt=['Fernando de la Rúa', 'Presidente de Argentina', 'gobierno'], lugar='delarua'))
CRO("El efecto en la economía es inmediato. Las ventas se hunden. Las fábricas de coches, de ropa, de materiales de construcción echan el cierre por falta de pedidos. Diciembre, que debería ser el mes de las compras de Navidad, se convierte en el peor mes del año.",
    ai('escaparate_vacio', 'an empty department store decorated for Christmas with no customers, mannequins in the window, a salesperson waiting alone, cold light', at='el mes de las compras de Navidad'))
NEW("Y el ministro, lejos de aflojar, presenta un presupuesto para dos mil dos con nuevos recortes, la condición del FMI para volver a prestar.",
    ph('Domingo Cavallo', at='Y el ministro', lt=['Domingo Cavallo', 'Ministro de Economía', 'gobierno'], lugar='cavallo'),
    ai('presupuesto_tijera', 'a thick budget document on a desk with a pair of scissors resting on top, red pencil marks everywhere, cold office light', at='nuevos recortes'))
NEW("Hasta los senadores de su propio partido, con el expresidente Raúl Alfonsín a la cabeza, piden públicamente que Cavallo se vaya. El presidente lo sostiene. Es la única carta que le queda.",
    ph('Raúl Alfonsín', at='Raúl Alfonsín', lt=['Raúl Alfonsín', 'Expresidente · senador de la UCR', 'gobierno'], lugar='alfonsin'),
    ai('ultima_carta', 'a single playing card held between two fingers over a table where all other cards have been swept away, tense close-up', at='la única carta'))
CRO("Día dieciocho. Martes. Los saqueos llegan al Gran Buenos Aires. En cada barrio corre el rumor de que mañana vienen a por el siguiente súper. Los comerciantes duermen dentro de sus tiendas.",
    DIA(18, 'del corralito · martes 18 de diciembre', at='Día dieciocho', frm=16),
    ai('tendero_noche', 'a shopkeeper sitting on a chair inside his dark shop at night behind a lowered metal shutter, a baseball bat across his knees, sleepless', at='duermen dentro de sus tiendas'))
NAR("[pause] Y llega el miércoles diecinueve. El día en que el Gobierno decide que la respuesta no es dar marcha atrás. Es apretar más fuerte.",
    ai('puno_cierra', 'a giant fist slowly closing around a small model of a city, cracks spreading, dramatic contrast of black and red', at='apretar más fuerte'))

# ---------------- IV · ESTADO DE SITIO ----------------
T('Estado de sitio', 'Miércoles 19 de diciembre de 2001', num='IV', secs=6.0, sting='accion')
B('accion')
CRO("Día diecinueve. Desde primera hora, los saqueos se extienden por el conurbano, por Santa Fe, por Entre Ríos, por Corrientes. Hay muertos en Rosario. Policías disparando. Comerciantes disparando.",
    DIA(19, 'del corralito · miércoles 19 de diciembre', at='Día diecinueve', frm=18),
    ai('humo_conurbano', 'columns of black smoke rising over low-rise suburban rooftops, a police car with lights spinning, people running across an avenue, aerial view', at='se extienden por el conurbano'))
NEW("En la Casa Rosada, el presidente intenta un gesto de última hora: ofrece al peronismo, que controla el Congreso, entrar en un gobierno de unidad. La respuesta tarda. Y la tarde avanza.",
    ph('Casa Rosada Buenos Aires', at='En la Casa Rosada', lt=['Casa Rosada', 'Buenos Aires'], lugar='rosada'),
    ai('telefono_espera', 'a heavy old telephone on a presidential desk not ringing, an ashtray full, a man in a dark suit pacing behind it in shadow', at='La respuesta tarda'))
NAR("Por la noche, De la Rúa aparece en cadena nacional. Todas las televisiones del país. Y anuncia la medida más grave que puede tomar un presidente en democracia.",
    ai('tele_escaparate', 'a crowd gathered in front of a shop window full of televisions all showing the same faceless figure at a desk, night, glowing screens', at='aparece en cadena nacional'))
DLR("[serious] Han ocurrido en el país hechos de violencia que ponen en peligro a personas y a bienes, y crean un cuadro de conmoción interior. Quiero informarles que he decretado el estado de sitio en todo el territorio nacional.",
    ph('Fernando de la Rúa', at='Han ocurrido en el país', lt=['Fernando de la Rúa', 'Cadena nacional · 19 de diciembre de 2001', 'gobierno'], lugar='delarua'),
    cd(dict(type='quote', text='Quiero informarles que he decretado el estado de sitio en todo el territorio nacional.', attrib='Fernando de la Rúa · cadena nacional, 19 de diciembre de 2001'), at='Quiero informarles'))
CRO("El estado de sitio suspende garantías constitucionales. En Argentina, esas palabras se oían por primera vez desde los años de la dictadura. Y el efecto fue exactamente el contrario del que buscaba el presidente.",
    cd(dict(type='kw', word='ESTADO DE SITIO', sub='garantías constitucionales suspendidas · 30 días'), at='El estado de sitio'),
    ai('botas_calle', 'military-style boots marching in a row on wet cobblestones at night, reflected streetlights, menacing', at='la dictadura'))
NEW("Años después, De la Rúa diría que aquel estado de sitio había sido una medida simbólica. Esa noche, nadie lo entendió así.",
    ai('sombra_decreto', 'the shadow of a hand holding a decree stretching across a dark city full of tiny lit windows, ominous symbolic composition', at='una medida simbólica'))
B('calle')
NEW("Minutos después de que termine el discurso, en Buenos Aires empieza a sonar algo que nadie había convocado. Primero una ventana. Luego un edificio entero. Luego toda la calle.",
    ai('ventana_sola', 'a single lit window in a dark apartment block at night, a silhouette leaning out banging a pot with a ladle', at='Primero una ventana'),
    ai('calle_entera', 'an entire street at night filled with people pouring out of apartment doors in pyjamas and slippers banging pots, motion and noise', at='toda la calle'))
NAR("[dramatically] Las cacerolas. Miles de vecinos bajan en zapatillas, en camiseta, con la sartén de la cena en la mano. Nadie los ha llamado. Caminan solos hacia la Plaza de Mayo y hacia el Congreso.",
    ai('marcha_cacerolas', 'a huge spontaneous crowd marching down a wide avenue at midnight banging pots and pans, families, elderly people and teenagers together, streetlights', at='Miles de vecinos'),
    ph('Plaza de Mayo Buenos Aires', at='la Plaza de Mayo', lt=['Plaza de Mayo', 'Buenos Aires'], lugar='plazamayo'),
    ph('Congreso de la Nación Argentina edificio', at='el Congreso', lt=['Congreso de la Nación', 'Buenos Aires'], lugar='congreso'))
NAR("No hay pancartas. No hay partidos. No hay líderes. Solo el ruido. Un ruido metálico, ensordecedor, que se oye desde los barrios de Palermo, de Belgrano, de Caballito, y que avanza por las avenidas hacia el centro como una marea.",
    ai('marea_ruido', 'a river of people flowing down a wide boulevard at night between tall apartment buildings, pots raised like torches, viewed from a high balcony, overwhelming scale', at='como una marea'))
CRO("Es la clase media. La que votó a la Alianza. La que tenía los ahorros en el banco. Y ahora grita una frase que se convertirá en el lema de toda una época.",
    ai('clase_media', 'a middle-aged couple in office clothes banging pots side by side in a crowd at night, the woman with her glasses on her head, determined', at='Es la clase media'))
NAR("Que se vayan todos.",
    cd(dict(type='kw', word='¡QUE SE VAYAN TODOS!', sub='el grito de diciembre de 2001'), at='Que se vayan todos'))
NEW("Pasada la medianoche, la Plaza de Mayo está llena. La policía carga y tira gases. Y en el Ministerio de Economía, Domingo Cavallo presenta su dimisión. El padre del uno a uno se va. Pero la gente no.",
    ai('plaza_medianoche', 'a city square packed with protesters at midnight, a grand pink palace facade lit behind them, tear gas canisters smoking, people covering their mouths', at='la Plaza de Mayo está llena'),
    ph('Domingo Cavallo', at='Domingo Cavallo presenta su dimisión', lt=['Domingo Cavallo', 'Dimite en la madrugada del 20 de diciembre', 'gobierno'], lugar='cavallo'))
NAR("[pause] Al amanecer del jueves, el presidente sigue en su despacho. Sin ministro de Economía. Sin apoyo en el Congreso. Con un país en llamas. Le quedan doce horas en el cargo. Y van a ser las más sangrientas.",
    ai('amanecer_rosada', 'dawn over a grand palace with smoke still rising from the square in front, debris and abandoned pots on the ground, eerie silence', at='Al amanecer del jueves'),
    cd(dict(type='kw', word='12 HORAS', sub='le quedan en el cargo'), at='doce horas'))

# ---------------- V · EL HELICÓPTERO ----------------
T('El helicóptero', 'Jueves 20 de diciembre de 2001', num='V', secs=6.0, sting='accion')
B('accion')
CRO("Día veinte. Por la mañana, las Madres de Plaza de Mayo hacen su ronda de los jueves, como cada semana desde mil novecientos setenta y siete. Y la policía montada carga contra ellas.",
    DIA(20, 'del corralito · jueves 20 de diciembre', at='Día veinte', frm=19),
    ai('madres_panuelos', 'a circle of elderly women wearing white headscarves walking together in a square, a mounted policeman rushing toward them, shocking contrast', at='las Madres de Plaza de Mayo'),
    ai('montada_carga', 'mounted police charging at full gallop across a square, hooves on pavement, scarves and placards flying, extreme motion', at='la policía montada carga'))
NEW("Las imágenes de los caballos contra mujeres de setenta años con pañuelos blancos dan la vuelta al país en minutos. Y desde el mediodía, la Plaza de Mayo se convierte en un campo de batalla.",
    ai('panuelo_suelo', 'a white headscarf lying on the ground under the hoof prints of a horse, a dropped placard nearby, close-up, heavy symbolism', at='pañuelos blancos'))
NAR("Jóvenes, motoqueros, empleados, estudiantes. Se enfrentan a la policía en la avenida de Mayo, en la diagonal, en las calles que rodean la plaza. Piedras contra balas de goma. Y no solo de goma.",
    ph('Avenida de Mayo Buenos Aires', at='la avenida de Mayo', lt=['Avenida de Mayo', 'Buenos Aires'], lugar='avmayo'),
    ai('motos_humo', 'young people on motorcycles riding through tear gas toward a police line, others throwing stones, burning barricade, chaos', at='motoqueros'),
    ai('piedras_balas', 'protesters crouched behind an overturned bus shelter throwing stones while rubber bullets ricochet, smoke everywhere, bold diagonal', at='Piedras contra balas'))
CRO("Ese jueves, en el centro de Buenos Aires, mueren cinco personas. Varias por disparos de armas de fuego. En todo el país, entre el diecinueve y el veinte, la cifra más citada es de treinta y nueve muertos.",
    cd(dict(type='counter', **{'from': 0}, to=5, label='muertos en el centro de Buenos Aires · 20 de diciembre'), at='mueren cinco personas'),
    ai('flores_acera', 'a small pile of flowers and a lit candle on a city sidewalk next to a dark stain, people\'s legs passing by, mourning', at='armas de fuego'))
NEW("Mientras tanto, dentro de la Casa Rosada, De la Rúa sigue buscando un acuerdo. A media tarde habla al país y vuelve a ofrecer al peronismo compartir el Gobierno. La respuesta llega enseguida. Es un no.",
    ph('Casa Rosada Buenos Aires', at='dentro de la Casa Rosada', lt=['Casa Rosada', 'Buenos Aires'], lugar='rosada'),
    ai('puerta_cierra', 'a tall carved wooden palace door slowly closing on a long corridor, a single figure left alone inside, cold light', at='Es un no'))
DLR("Yo no me aferro a un cargo.",
    cd(dict(type='quote', text='Yo no me aferro a un cargo.', attrib='Fernando de la Rúa · 20 de diciembre de 2001'), at='Yo no me aferro'))
NAR("Poco después, el presidente escribe su renuncia a mano. Una carta breve dirigida al Congreso. La firma. Y pregunta cómo puede salir del edificio.",
    ai('carta_renuncia', 'an elderly hand writing a short letter on official letterhead with a fountain pen, a lamp, a window with smoke outside, the paper blank of readable words', at='escribe su renuncia a mano'))
CRO("La plaza está tomada. Las calles de alrededor, también. Salir en coche es imposible. Solo queda un camino. Hacia arriba.",
    AIR('heli_azotea', at='Hacia arriba'))
B('tema')
NAR("[serious] Pasadas las siete y media de la tarde, Fernando de la Rúa sube a la azotea. El helicóptero presidencial, un Sikorsky blanco, despega de la Casa Rosada rumbo a la residencia de Olivos. Abajo, en la plaza, la gente lo ve alejarse. Y aplaude. Con rabia.",
    ai('heli_ve_plaza', 'from a crowded square, people looking up at a white helicopter rising above a pink palace into an orange dusk sky, some clapping, some shouting', at='la gente lo ve alejarse'),
    ph('Fernando de la Rúa', at='Fernando de la Rúa sube', lt=['Fernando de la Rúa', 'Renuncia · 20 de diciembre de 2001', 'gobierno'], lugar='delarua'),
    ai('heli_ciudad', 'a small white helicopter flying low over a vast city at dusk with columns of smoke rising from several streets, wide cinematic shot', at='rumbo a la residencia de Olivos'))
NAR("En la plaza, alguien levanta una cacerola hacia el cielo. Otros silban. Otros lloran. Hay quien jura que nunca olvidará el sonido de aquellas aspas mezclado con el de miles de cacerolas. El poder, literalmente, se iba volando.",
    ai('cacerola_cielo', 'a single raised pot silhouetted against a red sky, a helicopter tiny in the distance above it, crowd around in shadow, iconic', at='alguien levanta una cacerola'))
NEW("Es la imagen que resume la crisis de dos mil uno. Un presidente que llega a la Casa Rosada en coche oficial y se va por los aires, porque por tierra ya no hay país que lo deje pasar.",
    ai('heli_silueta', 'the silhouette of a helicopter against a huge setting sun over a city skyline, bold red and black, iconic poster composition', at='Es la imagen que resume'))
CRO("Y hay un epílogo que casi nadie recuerda. A la mañana siguiente, viernes veintiuno, De la Rúa, ya sin cargo, vuelve a la Casa Rosada poco antes de las nueve. Tiene una última firma pendiente: deroga el estado de sitio que él mismo había decretado. Luego se marcha. Esta vez, por la puerta.",
    DIA(21, 'del corralito · viernes 21 de diciembre', at='A la mañana siguiente', frm=20),
    ai('puerta_salida', 'a lone man in a dark suit walking out through tall palace doors into pale morning light, an empty square ahead, quiet after the storm', at='Esta vez, por la puerta'))
NAR("[pause] Pero cuando el ruido del helicóptero se apaga, queda la pregunta de verdad. Argentina no tiene presidente. No tiene ministro de Economía. No puede pagar su deuda. Y los ahorros de millones de personas siguen dentro de los bancos.",
    ai('sillon_vacio', 'an empty presidential armchair in a grand office, a sash draped over it, papers scattered, smoke-stained window behind, silence after chaos', at='Argentina no tiene presidente'),
    ai('boveda_cerrada', 'a massive closed bank vault door with a giant padlock and chains, a single shaft of light, people\'s shadows on the wall', at='siguen dentro de los bancos'))
NAR("¿Quién los iba a sacar de ahí? La respuesta llegaría en once días. Y de la mano de cinco presidentes distintos.",
    cd(dict(type='kw', word='5 PRESIDENTES', sub='en once días'), at='cinco presidentes distintos'))
