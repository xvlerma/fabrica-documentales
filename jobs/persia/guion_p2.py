# -*- coding: utf-8 -*-
# «El Imperio Persa: la historia que 300 no te contó» · parte 2: capítulos III, IV y V
from lib import *

# ---------------- III · LA MÁQUINA DE DARÍO ----------------
T('La máquina de Darío', '522 – 490 a. C.', num='III', sting='tema')
B('maravilla')
NEW("Kermanshah, en el oeste de Irán, año mil ochocientos treinta y cinco. Un oficial británico, Henry Rawlinson, se cuelga de una cuerda en la pared de Behistún para copiar, letra a letra, la inscripción de Darío. [short pause] Le llevará más de diez años.",
    ph('Behistun cliff Kermanshah', at='Kermanshah'),
    ph('Henry Rawlinson portrait', at='Henry Rawlinson', lt=['Henry Rawlinson', 'Oficial y orientalista británico · 1810 – 1895', 'otros']),
    ai('rawlinson_cuerda', 'a nineteenth-century explorer hanging from ropes on a sheer limestone cliff copying ancient carved script into a notebook, a ladder below, vast Iranian plain behind', at='se cuelga de una cuerda'))
NAR("[serious] Gracias a esa copia se descifró la escritura cuneiforme, con la que se escribió durante tres mil años en Mesopotamia. Behistún hizo con ella lo que la piedra de Rosetta con los jeroglíficos. [short pause] El mentiroso de Behistún, si lo era, nos dejó la llave de toda una civilización.",
    ph('Behistun inscription Old Persian cuneiform', at='la escritura cuneiforme'),
    ph('Rosetta Stone British Museum', at='la piedra de Rosetta'))
DAR("[serious] Dice Darío el rey: tú que seas rey en adelante, guárdate mucho de la mentira. Al hombre que sea seguidor de la mentira, castígalo bien.",
    PAP('Tú que seas rey en adelante, guárdate mucho de la mentira.', 'Darío I', 'Inscripción de Behistún', at='guárdate mucho de la mentira'))
DAR("Dice Darío el gran rey: este es el reino que tengo. Desde los escitas que viven más allá de Sogdiana, hasta Kush. Desde la India, hasta Sardes. Me lo concedió Ahuramazda, el más grande de los dioses.",
    cd(dict(type='imperio', title='El imperio de Darío, hacia 500 a. C.', bbox=[18, 12, 80, 48], stages=[
        dict(year='Oeste', label='De Libia y Tracia al Egeo', zona=['EGY', 'TUR', 'LBY', 'CYP', {'c': 'BGR', 'box': [25.0, 41.2, 28.6, 42.6]}]),
        dict(year='Centro', label='Mesopotamia, Levante e Irán', zona=['EGY', 'TUR', 'LBY', 'CYP', 'IRQ', 'SYR', 'LBN', 'ISR', 'JOR', 'PSE', 'IRN', 'ARM', 'AZE']),
        dict(year='Este', label='Hasta Asia Central y el Indo', zona=['EGY', 'TUR', 'LBY', 'CYP', 'IRQ', 'SYR', 'LBN', 'ISR', 'JOR', 'PSE', 'IRN', 'ARM', 'AZE', 'TKM', 'UZB', 'TJK', 'AFG', 'PAK'])]), at='este es el reino que tengo'))
NEW("Y es que Darío, usurpador o no, resultó un genio de la organización. Dividió el imperio en unas veinte provincias, las satrapías. Al frente de cada una puso a un sátrapa, un gobernador. Pero al lado le dejó un secretario y un jefe militar que respondían directamente ante el rey.",
    cd(dict(type='list', header='Cómo se gobernaba una satrapía', items=['El sátrapa: gobierna y recauda', 'El secretario real: escribe al rey', 'El jefe de la guarnición: responde ante el rey', 'Los «ojos y oídos del rey»: inspectores por sorpresa']), at='las satrapías'),
    ph('Apadana staircase delegations Persepolis', at='unas veinte provincias'))
HER("Los indios, el pueblo más numeroso de todos los que conocemos, pagaban el tributo más alto: trescientos sesenta talentos de oro en polvo. Babilonia y el resto de Asiria, mil talentos de plata y quinientos niños eunucos.",
    PAP('Los indios pagaban el tributo más alto: trescientos sesenta talentos de oro en polvo.', 'Heródoto, sobre los tributos de Darío', 'Historias, III, 92 – 94', at='oro en polvo'),
    ph('Persepolis Apadana relief Indian delegation gold', at='trescientos sesenta talentos'))
NAR("Y por encima de todos, unos inspectores que los griegos llamaban los ojos y los oídos del rey. Llegaban sin avisar. [short pause] Un sátrapa podía ser el hombre más poderoso de su provincia, pero nunca sabía quién estaba escribiendo sobre él.",
    ai('ojos_oidos', 'a cloaked royal inspector arriving unannounced at a governor palace at dusk, guards stepping aside, the governor freezing at the top of the stairs', at='los ojos y los oídos del rey'))
NEW("Para pagar todo eso hacía falta dinero. Darío acuñó una moneda de oro casi puro, el dárico, con el rey arrodillado tirando con arco. Los griegos la llamaban «los arqueros». [short pause] Con ella, como veremos, Persia compraría más ciudades griegas que con todos sus ejércitos.",
    ph('Daric gold coin Achaemenid', at='el dárico', lt=['Dárico de oro', 'Hacia 500 a. C.']),
    ai('monedas_oro', 'a heap of ancient gold coins spilling from a leather bag onto a wooden table, an oil lamp, a hand counting them in the shadows', at='compraría más ciudades'))
B('tema')
NAR("[serious] Y para que las órdenes llegaran a tiempo, construyó carreteras. La más famosa, el Camino Real, unía Susa, en Irán, con Sardes, junto al mar Egeo. Dos mil quinientos kilómetros, con una posta cada jornada de camino.",
    cd(dict(type='mapfly', title='El Camino Real de Darío', keys=[[24, 26, 56, 42], [26, 28, 54, 41]],
        points=[dict(name='Sardes', lon=28.04, lat=38.49, at=0.1), dict(name='Puertas Cilicias', lon=34.77, lat=37.3, at=0.35), dict(name='Nínive', lon=43.15, lat=36.36, at=0.6), dict(name='Susa', lon=48.25, lat=32.19, at=0.85), dict(name='Persépolis', lon=52.89, lat=29.93, at=0.95)],
        arrows=[dict(path=[[28.04, 38.49], [32.0, 39.6], [35.5, 39.0], [34.77, 37.3], [38.3, 37.1], [43.15, 36.36], [45.4, 34.3], [48.25, 32.19]], color=PE, at=0.2, dur=3.0)]), at='el Camino Real'),
    ai('posta_relevo', 'a royal courier galloping into a stone relay station at night, a fresh horse and rider already waiting with torches, the message passed hand to hand', at='una posta cada jornada'))
HER("No hay nada mortal que viaje más rápido que estos mensajeros. Ni la nieve, ni la lluvia, ni el calor, ni la noche les impiden cumplir a toda velocidad la etapa que tienen asignada.",
    PAP('Ni la nieve, ni la lluvia, ni el calor, ni la noche les impiden cumplir a toda velocidad la etapa que tienen asignada.', 'Heródoto, sobre los correos persas', 'Historias, VIII, 98', at='Ni la nieve'),
    ai('correo_nieve', 'a Persian horseman riding hard through a blizzard on a mountain road, cloak flying, a sealed leather pouch at his belt', at='Ni la nieve'))
NEW("Lo que a pie costaba unos noventa días, el correo del rey lo hacía en una semana o poco más. [short pause] Veinticuatro siglos después, esa frase de Heródoto se grabó en la fachada de la gran oficina de correos de Nueva York. Allí sigue.",
    cd(dict(type='counter', to=90, label='días a pie de Sardes a Susa · el correo real: una semana o poco más'), at='unos noventa días'),
    ph('James Farley Post Office New York inscription', at='la gran oficina de correos de Nueva York', lt=['Oficina de correos James A. Farley', 'Nueva York · hoy']))
DAR("Dice Darío el rey: soy persa. Desde Persia conquisté Egipto. Ordené cavar este canal, desde el río llamado Nilo, que corre en Egipto, hasta el mar que viene de Persia.",
    ph('Darius Suez canal stele Chalouf', at='Ordené cavar este canal'),
    cd(dict(type='map', title='El canal de Darío', bbox=[28, 26, 36, 33], points=[dict(name='Nilo', lon=31.25, lat=30.05), dict(name='Mar Rojo', lon=32.55, lat=29.95, big=1), dict(name='Lagos Amargos', lon=32.4, lat=30.35)]), at='hasta el mar'))
NAR("[serious] Un canal del Nilo al mar Rojo. Casi dos mil cuatrocientos años antes que el de Suez. Y en los desiertos de Irán, los persas perfeccionaron los qanats: túneles subterráneos de kilómetros que llevan el agua de las montañas a los campos sin que el sol la evapore. Algunos todavía funcionan.",
    ph('Qanat Iran underground channel', at='los qanats', lt=['Qanat', 'Irán · hoy']),
    ai('qanat_construccion', 'ancient diggers lowering baskets into a deep vertical shaft in the Iranian desert, a line of shafts stretching toward distant mountains, sunrise', at='túneles subterráneos'))
B('maravilla')
NEW("Y luego estaba la capital. Hacia el año quinientos dieciocho, Darío empezó a levantar Persépolis: una terraza artificial del tamaño de diecisiete campos de fútbol, palacios con columnas de veinte metros y escaleras de peldaños tan bajos que, según se dice, se podían subir a caballo.",
    ph('Persepolis ruins aerial view', at='levantar Persépolis'),
    ph('Persepolis Apadana columns', at='columnas de veinte metros'),
    ph('Persepolis grand staircase', at='escaleras de peldaños'),
    ai('persepolis_esplendor', 'the full splendor of Persepolis at its height, painted palaces with colored reliefs and cedar roofs, crowds of delegations climbing the great staircase, golden afternoon', at='palacios con columnas'))
DAR("Dice Darío el rey: los materiales de este palacio vinieron de lejos. La madera de cedro la trajeron de un monte llamado Líbano. El oro, de Sardes y de Bactria. El lapislázuli, de Sogdiana. El marfil, de Etiopía, de la India y de Aracosia. Los canteros que labraron la piedra eran jonios y sardianos. Los orfebres, medos y egipcios. Los que cocieron los ladrillos, babilonios.",
    cd(dict(type='list', header='Quién construyó el palacio de Darío', items=['Cedro: del Líbano', 'Oro: de Sardes y Bactria', 'Canteros: jonios y sardianos', 'Orfebres: medos y egipcios', 'Ladrillos: babilonios']), at='vinieron de lejos'),
    ph('Darius Susa foundation charter tablet Louvre', at='Los canteros'))
NAR("[dramatically] ¿Quién la construyó? Durante siglos se dio por hecho la respuesta: esclavos. Como en las películas. [pause] Hasta que en mil novecientos treinta y tres los arqueólogos de la Universidad de Chicago abrieron un cuarto de la muralla. Y encontraron decenas de miles de tablillas de barro.",
    ai('esclavos_latigo', 'a stereotypical Hollywood-like vision of slaves dragging huge stones under whips, deliberately theatrical and false, red dramatic light, blurred', at='esclavos'),
    ph('Persepolis Fortification tablet Elamite', at='decenas de miles de tablillas'),
    ph('Persepolis excavation Herzfeld 1930s', at='abrieron un cuarto de la muralla'))
PIE("Son el archivo de la Fortificación de Persépolis. Escritas en elamita, entre los años quinientos nueve y cuatrocientos noventa y cuatro antes de Cristo. Cebada, vino, cerveza, ovejas. Quién las recibe, cuánto, en qué mes. Y quién lo firma con su sello.",
    cd(dict(type='doc', title='Archivo de la Fortificación de Persépolis', lines=['Tablillas de barro en elamita', '509 – 494 a. C.', 'Raciones de cebada, vino, cerveza y ganado'], source='Instituto de Estudios Antiguos · Universidad de Chicago', hl='Raciones'), at='Son el archivo'),
    ph('Persepolis Fortification tablet seal impression', at='firma con su sello'))
PIE("[serious] Y lo que cuentan no es una obra de esclavos. Miles de trabajadores, llegados de todo el imperio, cobran cada mes una paga en especie, según su oficio. Los más cualificados, hombres o mujeres, cobran lo mismo. [short pause] Hay mujeres al frente de equipos de trabajo, con el título de jefa.",
    ai('taller_mujeres', 'women artisans weaving and dyeing textiles in a large workshop at Persepolis, a woman supervisor holding a clay tablet directing them, sunlight through columns', at='mujeres al frente'),
    OTRA(['Una capital levantada a latigazos', 'Esclavos sin nombre'], ['Trabajadores con nombre y paga', 'Mujeres jefas de equipo', 'Raciones extra por maternidad'], at='no es una obra de esclavos'))
PIE("Y hay raciones especiales para las madres. Las que acaban de dar a luz reciben cereal y vino o cerveza de más durante un tiempo. [short pause] Aunque no todo es moderno: si el bebé es un niño, la ración extra es el doble que si es una niña.",
    ai('madre_registro', 'a storehouse scribe pressing a seal on a clay tablet while several mothers with infants wait in line holding baskets, grain sacks and wine jars, soft morning light', at='raciones especiales para las madres'),
    ph('Persepolis Fortification tablet Elamite', at='si el bebé es un niño'))
PIE("Las tablillas tienen también a las reinas. Irdabama, una gran dama de la corte, gestiona sus propias tierras, con cientos de trabajadores a su cargo y su propio sello. Artistona, la esposa favorita de Darío, recibe vino y ovejas para sus banquetes. [short pause] Nada que ver con las mujeres encerradas de un harén de película.",
    ph('Achaemenid cylinder seal impression', at='su propio sello'),
    ai('reina_hacienda', 'an elegant Persian noblewoman in fine robes inspecting vineyards and storehouses on horseback with scribes and stewards, her face turned away, golden hour', at='gestiona sus propias tierras'))
DAR("[serious] Dice Darío el rey: no es mi deseo que el débil sufra injusticia por culpa del fuerte. Ni que el fuerte sufra injusticia por culpa del débil. Lo que es justo, eso es lo que deseo. No soy amigo del hombre que sigue la mentira.",
    ph('Naqsh-e Rostam tomb of Darius', at='Dice Darío el rey', lt=['Tumba de Darío', 'Naqsh-e Rostam, Irán']),
    PAP('No es mi deseo que el débil sufra injusticia por culpa del fuerte. Lo que es justo, eso es lo que deseo.', 'Darío I', 'Inscripción de su tumba en Naqsh-e Rostam', at='no es mi deseo'))
NEW("La verdad contra la mentira. Es el corazón de la religión de los reyes persas, que adoraban a Ahuramazda, el dios sabio de la luz, frente a las fuerzas del engaño. [short pause] El propio Heródoto, que no era su amigo, lo vio así.",
    ph('Faravahar Persepolis relief', at='Ahuramazda', lt=['Faravahar', 'Símbolo alado · Persépolis']))
HER("A sus hijos, desde los cinco hasta los veinte años, solo les enseñan tres cosas: a montar a caballo, a tirar con arco y a decir la verdad. Lo más vergonzoso para ellos es mentir. Y lo segundo, tener deudas.",
    PAP('Solo les enseñan tres cosas: a montar a caballo, a tirar con arco y a decir la verdad.', 'Heródoto, sobre los persas', 'Historias, I, 136', at='solo les enseñan tres cosas'),
    ai('ninos_arco', 'Persian boys learning to shoot bows from galloping horses on an open plain under an instructor, dust and sunlight, ancient Iran', at='tirar con arco'))
HER("Darío reunió a unos griegos de su corte y les preguntó por cuánto dinero estarían dispuestos a comerse a sus padres muertos. Dijeron que por nada del mundo. Entonces llamó a unos indios, los calatias, que sí se comen a sus padres, y les preguntó por cuánto aceptarían quemarlos. Se pusieron a gritar horrorizados. Así es la costumbre: la reina de todas las cosas.",
    PAP('Así es la costumbre: la reina de todas las cosas.', 'Heródoto, sobre Darío y las costumbres de los pueblos', 'Historias, III, 38', at='la reina de todas las cosas'),
    ai('dario_costumbres', 'a Persian king on a throne questioning two groups of foreigners, Greeks in himations recoiling in horror on one side and Indian men in white on the other, a court interpreter between them', at='Darío reunió a unos griegos'))
NAR("[serious] Un imperio que respeta a sus pueblos, paga a sus obreros y presume de no mentir. Pero también un imperio que no perdona una rebelión. [pause] Y en el año cuatrocientos noventa y nueve, al otro extremo del mapa, las ciudades griegas de la costa de Asia se rebelaron.",
    cd(dict(type='map', title='499 a. C.: la revuelta jonia', bbox=[20, 34, 32, 42], points=[dict(name='Mileto', lon=27.28, lat=37.53, big=1), dict(name='Sardes', lon=28.04, lat=38.49), dict(name='Atenas', lon=23.73, lat=37.98), dict(name='Éfeso', lon=27.34, lat=37.94)]), at='se rebelaron'))
NEW("Pidieron ayuda a Grecia. Atenas mandó veinte barcos. Y en el año cuatrocientos noventa y ocho, jonios y atenienses entraron en Sardes, la gran capital persa del oeste, y la incendiaron. Ardieron las casas, el mercado y el templo de la diosa Cibeles.",
    ai('sardes_arde', 'a city of mud-brick and reed houses burning at night, Greek hoplites running through smoke-filled streets, a temple engulfed in flames, people fleeing', at='la incendiaron'))
HER("Cuando Darío se enteró, pidió un arco y disparó una flecha al cielo. Y ordenó a uno de sus criados que, cada vez que le sirvieran la cena, le repitiera tres veces: «Señor, acuérdate de los atenienses».",
    ai('flecha_cielo', 'a king in royal robes on a palace terrace shooting an arrow straight up into a stormy sky, courtiers watching in silence', at='disparó una flecha al cielo'),
    PAP('Señor, acuérdate de los atenienses.', 'Lo que un criado repetía a Darío en cada cena, según Heródoto', 'Historias, V, 105', at='acuérdate de los atenienses'))
NAR("[dramatically] Darío no lo olvidó. [pause] Ocho años después, una flota persa cruzó el Egeo con una misión: castigar a Atenas. Y desembarcó en una playa a cuarenta kilómetros de la ciudad. Una playa llamada Maratón.",
    ai('flota_egeo', 'a vast Persian fleet of hundreds of warships with dark sails crossing the Aegean sea at dawn, horses on transport ships, islands on the horizon', at='una flota persa'),
    ph('Marathon bay beach Greece', at='Maratón', lt=['Bahía de Maratón', 'Ática, Grecia · hoy']))

# ---------------- IV · MARATÓN, VISTA DESDE PERSIA ----------------
T('Maratón, vista desde Persia', '490 a. C.', num='IV', sting='batalla')
B('batalla')
ESP("[dramatically] Septiembre del año cuatrocientos noventa antes de Cristo. Durante días, los dos ejércitos se miran sin moverse. Y de pronto, los atenienses cargan. Corriendo. Con treinta kilos de bronce encima, a través de la llanura, directos contra los arqueros persas.",
    ai('carga_maraton', 'Greek hoplites charging at a run across a coastal plain under a rain of Persian arrows, bronze shields raised, spears forward, dust clouds, wide dramatic view', at='los atenienses cargan'),
    ai('arqueros_persas', 'ranks of Persian archers behind wicker shields loosing volleys of arrows at an incoming charge, seen from behind their line, the sky dark with arrows', at='los arqueros persas'))
NEW("Los persas no se lo esperaban. Nadie cargaba así contra ellos. El centro persa aguantó, pero las alas griegas lo rodearon. Y la batalla se convirtió en una huida hacia los barcos, entre las marismas.",
    cd(dict(type='map', title='Maratón, 490 a. C.', bbox=[23.88, 38.08, 24.06, 38.2], points=[dict(name='Campamento ateniense', lon=23.94, lat=38.15), dict(name='Playa y flota persa', lon=24.0, lat=38.12, big=1), dict(name='Gran marisma', lon=24.03, lat=38.15)]), at='las alas griegas'),
    ai('huida_barcos', 'Persian soldiers fleeing through marshes toward beached warships, Greeks pursuing, a ship being pushed off the shore, chaos and spray', at='una huida hacia los barcos'))
HER("En esta batalla de Maratón murieron unos seis mil cuatrocientos bárbaros, y de los atenienses, ciento noventa y dos.",
    cd(dict(type='versus', title='Maratón, según Heródoto', left=dict(name='Persas', color=PE, lines=['unos 6.400 muertos', 'la flota escapa casi intacta']), right=dict(name='Atenienses', color=GR, lines=['192 muertos', 'enterrados en un túmulo']), ), at='En esta batalla'),
    ph('Marathon tumulus Soros', at='ciento noventa y dos', lt=['El túmulo de Maratón', 'Tumba de los 192 atenienses · hoy']))
NAR("[serious] Para Atenas fue el nacimiento de una leyenda. El soldado que corrió hasta la ciudad para anunciar la victoria y murió al llegar es el origen de la carrera de maratón, aunque esa historia la cuentan autores muy posteriores. [short pause] Pero ¿y para Persia?",
    ai('corredor_maraton', 'a lone exhausted runner arriving at the gates of an ancient Greek city at sunset, collapsing as citizens rush toward him, dust', at='El soldado que corrió'))
NEW("Para Persia, Maratón fue una expedición de castigo que salió mal en una frontera lejana. Ninguna crónica persa la menciona. El imperio no perdió una sola provincia. Y la flota volvió casi entera a Asia. [short pause] Lo que sí cambió fue algo más difícil de medir: el orgullo del rey.",
    OTRA(['La victoria que salvó a Occidente', 'El fin de la amenaza persa'], ['Una expedición de castigo fallida', 'Ninguna crónica persa la menciona', 'El imperio, intacto'], at='una expedición de castigo'))
NAR("Darío empezó a preparar una invasión mucho mayor. Pero entonces se rebeló Egipto. Y en el año cuatrocientos ochenta y seis, con unos sesenta y cuatro años, el gran organizador murió. [pause] La venganza quedó en herencia. Para su hijo.",
    ph('Naqsh-e Rostam tomb of Darius', at='el gran organizador murió'),
    ph('Xerxes relief Persepolis', at='Para su hijo'))

# ---------------- V · JERJES Y LAS TERMÓPILAS ----------------
T('Jerjes y las Termópilas', '486 – 479 a. C.', num='V', sting='tema')
B('tension')
NEW("Jerjes tenía treinta y dos años cuando subió al trono. No era el primogénito de Darío. Pero era el nieto de Ciro el Grande por parte de madre, la reina Atosa, y eso pesaba más. [short pause] En Trescientos es un gigante de casi tres metros, calvo, cubierto de piercings y cadenas de oro, que se cree un dios.",
    ph('Xerxes relief Persepolis', at='Jerjes', lt=['Jerjes I', 'Rey de Persia · 486 – 465 a. C.', 'persia']),
    K('300', 'Persepolis treasury relief king audience', at='En Trescientos'))
NAR("[serious] Los relieves de Persépolis muestran otra cosa: un hombre con barba larga y rizada, una túnica hasta los pies y una corona. Y los reyes persas nunca dijeron ser dioses. Se presentaban como los elegidos de Ahuramazda. Que no es lo mismo.",
    ph('Persepolis treasury relief king audience', at='Los relieves de Persépolis'),
    OTRA(['Un dios-rey gigante y salvaje', 'Piercings, cadenas y máscaras'], ['Un rey con barba y túnica larga', 'Elegido de Ahuramazda, no dios', 'Como lo esculpieron los persas'], at='nunca dijeron ser dioses'))
JER("Dice Jerjes el rey: por la gracia de Ahuramazda construí esta Puerta de Todos los Países. Mucho más, que es bello, se construyó en Persépolis, y lo construimos yo y mi padre.",
    ph('Gate of All Nations Persepolis', at='esta Puerta de Todos los Países', lt=['Puerta de Todos los Países', 'Persépolis · Jerjes I']),
    ph('Gate of All Nations lamassu Persepolis', at='que es bello'))
NEW("Jerjes pasó cuatro años preparando la invasión de Grecia. Hizo excavar un canal a través de la península del monte Athos, para que sus barcos no tuvieran que rodear un cabo donde una flota persa ya había naufragado. Y mandó tender dos puentes de barcos sobre el estrecho del Helesponto, entre Asia y Europa.",
    ph('Mount Athos peninsula', at='monte Athos'),
    ph('Dardanelles strait Canakkale', at='el estrecho del Helesponto', lt=['El Helesponto', 'Los Dardanelos, Turquía · hoy']),
    ai('puente_barcos', 'two immense pontoon bridges made of hundreds of ships lashed together spanning a strait between two continents, workers laying planks and earth, dawn light', at='dos puentes de barcos'))
HER("Cuando los puentes estuvieron terminados, se levantó una gran tormenta que lo rompió y lo deshizo todo. Al enterarse, Jerjes ordenó que el Helesponto recibiera trescientos azotes y que arrojaran al mar un par de grilletes.",
    ai('tormenta_puentes', 'a violent storm tearing apart a bridge of boats across a strait, ships breaking loose and capsizing, cables snapping, lightning', at='una gran tormenta'),
    ai('mar_azotado', 'soldiers whipping the stormy sea with long lashes from a rocky shore while a broken bridge of boats drifts in the waves, a king on a throne watching from a hill, dark clouds', at='trescientos azotes'))
JER("Agua amarga, tu señor te impone este castigo porque lo ofendiste sin haber recibido de él ofensa alguna. El rey Jerjes te cruzará, quieras o no.",
    PAP('Agua amarga, tu señor te impone este castigo porque lo ofendiste. El rey Jerjes te cruzará, quieras o no.', 'Palabras de los azotadores del mar, según Heródoto', 'Historias, VII, 35', at='Agua amarga'))
NAR("[softly] Es el episodio que todo el mundo recuerda: el rey loco que azota el mar. Pero en el mundo antiguo, castigar a un río o a un mar era un ritual, no una locura. [short pause] Y Heródoto, en el mismo libro, cuenta otra escena de Jerjes que casi nadie recuerda.",
    ph('Herodotus bust Metropolitan Museum', at='Heródoto, en el mismo libro'))
HER("En Abidos, Jerjes quiso ver a todo su ejército. Desde un trono de mármol blanco miró el Helesponto cubierto de barcos y las llanuras llenas de hombres. Primero se sintió feliz. Y después, se echó a llorar.",
    ai('jerjes_llora', 'a king seated on a white marble throne on a hilltop, seen from behind, looking down at an endless army and a strait full of ships, a lonely melancholic figure in golden light', at='se echó a llorar'))
JER("[softly] Me ha venido a la mente la compasión, al pensar qué breve es la vida del hombre. De toda esta multitud, dentro de cien años no quedará ni uno vivo.",
    PAP('De toda esta multitud, dentro de cien años no quedará ni uno vivo.', 'Jerjes en Abidos, según Heródoto', 'Historias, VII, 46', at='Me ha venido a la mente'))
NEW("[serious] ¿Cuántos eran? Heródoto da una cifra imposible: un millón setecientos mil soldados de infantería. Los historiadores modernos la reducen mucho: quizá entre cien mil y trescientos mil hombres, según quién haga la cuenta. [short pause] Aun así, el ejército más grande que había visto Europa.",
    cd(dict(type='split', left=dict(title='Heródoto', lines=['1.700.000 de infantería', 'Ríos bebidos hasta secarse']), right=dict(title='Historiadores de hoy', lines=['Entre 100.000 y 300.000', 'Un ejército enorme, pero posible']), strike=True), at='Cuántos eran'),
    ai('ejercito_naciones', 'a procession of soldiers from dozens of nations of the Persian empire marching past, Ethiopians, Scythians, Indians, Lydians with varied weapons and dress, dust and banners', at='el ejército más grande'))
HER("¿Qué pueblo de Asia no llevó Jerjes contra Grecia? ¿Qué río no se secó al beber su ejército, salvo los más grandes?",
    ai('rio_seco', 'an army of thousands drinking from a river until it runs dry, horses and men crowding the cracked muddy riverbed, heat haze', at='Qué río no se secó'))
NAR("Venían de casi cincuenta pueblos distintos: persas y medos, pero también egipcios, indios, escitas, etíopes, fenicios… y muchos griegos. [short pause] Porque esto casi nunca se cuenta: buena parte de Grecia ya estaba del lado de Persia, o se negó a luchar contra ella.",
    ph('Tomb of Xerxes Naqsh-e Rostam throne bearers', at='casi cincuenta pueblos distintos'),
    ai('griegos_aliados', 'Greek soldiers and Persian officers sharing a campfire in a large camp at night, Greek helmets beside Persian bows, an uneasy alliance', at='muchos griegos'))
B('batalla')
ESP("[dramatically] Agosto del año cuatrocientos ochenta. Las Termópilas. Un paso entre la montaña y el mar tan estrecho que, en algunos puntos, solo cabía un carro. Allí esperan unos siete mil griegos, con el rey de Esparta, Leónidas, y sus trescientos.",
    ph('Thermopylae pass Leonidas monument', at='Las Termópilas'),
    ph('Leonidas statue Thermopylae', at='Leónidas', lt=['Leónidas I', 'Rey de Esparta', 'griegos']),
    cd(dict(type='counter', to=7000, label='griegos en las Termópilas, según las cifras de Heródoto: no solo trescientos'), at='unos siete mil griegos'))
NEW("Jerjes esperó cuatro días. Pensaba que se retirarían. A su lado estaba un rey espartano en el exilio, Demarato, y el rey persa le preguntó cómo era posible que tan pocos hombres, y libres, se enfrentaran a él.",
    ai('jerjes_demarato', 'a Persian king and an exiled Greek king in a red cloak talking in a royal tent overlooking a mountain pass by the sea, maps on a table, evening', at='Demarato'))
GRI("Son libres, pero no del todo. Tienen un amo, la ley, a la que temen mucho más de lo que tus súbditos te temen a ti. Y la ley les ordena siempre lo mismo: no huir ante ninguna multitud, sino vencer o morir en su puesto.",
    PAP('Tienen un amo, la ley, a la que temen mucho más de lo que tus súbditos te temen a ti.', 'Demarato a Jerjes, según Heródoto', 'Historias, VII, 104', at='Son libres'))
ESP("[dramatically] Al quinto día, Jerjes atacó. Primero, medos. Después, su guardia de élite: los Inmortales. Y en aquel embudo de roca, sus lanzas cortas no podían con las largas de los griegos. Dos días de matanza. [short pause] Heródoto dice que Jerjes saltó tres veces de su trono, temiendo por su ejército.",
    ai('inmortales_atacan', 'Persian elite infantry in colorful robes and wicker shields advancing into a narrow rocky pass against a wall of bronze shields, spears clashing, sea spray, chaos', at='los Inmortales'),
    ai('trono_salto', 'a king leaping up from his throne on a hill above a battle in a mountain pass, courtiers frozen, the battle raging far below in dust', at='saltó tres veces de su trono'))
NAR("[serious] Y entonces, la traición. Un griego de la zona, Efialtes, le vendió a Jerjes un sendero por las montañas. Esa noche, los Inmortales lo cruzaron con antorchas. Al amanecer, los griegos estaban rodeados.",
    ai('sendero_noche', 'a long column of soldiers with torches winding along a narrow mountain path through an oak forest at night, a local guide leading them', at='un sendero por las montañas'))
ESP("[dramatically] Leónidas mandó retirarse a casi todos. Él se quedó con sus trescientos y unos pocos aliados. Cuando se les rompieron las lanzas, lucharon con espadas. Cuando se rompieron las espadas, con las manos y los dientes. [pause] Ninguno sobrevivió.",
    ai('ultima_resistencia', 'the last stand of a few hundred Greek warriors on a small hill surrounded by an overwhelming army, broken spears, a hail of arrows darkening the sun', at='Ninguno sobrevivió'))
NEW("[serious] Es la escena que Trescientos convirtió en mito. Pero visto desde el otro lado, hay algo que la película no cuenta: en ese combate murieron también dos hermanos de Jerjes, Abrocomes e Hiperantes, hijos de Darío. [short pause] Para el rey persa, las Termópilas fueron una victoria. Y una tragedia familiar.",
    OTRA(['Monstruos contra héroes', 'Una derrota moral persa'], ['Una victoria persa en el campo', 'Dos hermanos del rey, muertos', 'El paso abierto hacia Atenas'], at='visto desde el otro lado'))
HER("Jerjes recorrió el campo entre los muertos. Al llegar al cuerpo de Leónidas, ordenó cortarle la cabeza y clavarla en un palo. Es la prueba de que el rey estaba más irritado con Leónidas que con ningún otro hombre: los persas suelen honrar, más que nadie, a los guerreros valientes.",
    ai('campo_muertos', 'a king walking slowly among the fallen after a battle in a mountain pass at dusk, broken shields and spears, crows circling, guards with torches', at='entre los muertos'))
NEW("[short pause] Después, el camino a Atenas quedó abierto. La ciudad estaba vacía: sus habitantes habían huido a las islas.",
    ph('Acropolis of Athens view', at='el camino a Atenas', lt=['La Acrópolis', 'Atenas · hoy']))
ESP("[dramatically] Los persas subieron a la Acrópolis y la quemaron. Templos, estatuas, todo. [short pause] Dieciocho años después de que Atenas incendiara Sardes, el criado de Darío ya podía callarse.",
    ai('acropolis_arde', 'the Acropolis of Athens burning at night, ancient temples engulfed in flames, Persian soldiers silhouetted on the rock, smoke against the stars', at='la quemaron'),
    ph('Kritios Boy Acropolis Museum', at='estatuas'))
NEW("Pero desde la Acrópolis en llamas, los atenienses podían ver otra cosa. Su flota. Escondida en el estrecho de Salamina, a pocos kilómetros. [pause] Y su jefe, Temístocles, acababa de enviar a Jerjes un mensaje secreto.",
    ph('Salamis strait Greece', at='el estrecho de Salamina', lt=['Estrecho de Salamina', 'Grecia · hoy']),
    ph('Themistocles bust Ostia', at='Temístocles', lt=['Temístocles', 'Estratega ateniense', 'griegos']))
B('tension')
NAR("[serious] El mensaje decía que los griegos iban a huir por la noche, y que era el momento de atacarlos. Era mentira. Jerjes mandó a su flota entrar en el estrecho. [short pause] Y en aquel canal tan estrecho, cientos de barcos persas no podían maniobrar. Uno de los griegos que lucharon aquel día, el poeta Esquilo, recordaría el grito que se oyó al amanecer.",
    ai('mensajero_noche', 'a secret messenger in a small rowing boat crossing a dark bay at night toward a distant fleet, lanterns on the water', at='por la noche'),
    ai('salamina_batalla', 'a massive naval battle in a narrow strait, Greek triremes ramming Persian warships, oars snapping, sailors falling into the sea, a king watching from a hill above', at='no podían maniobrar'))
GRI("[dramatically] ¡Adelante, hijos de los griegos! Liberad la patria, liberad a vuestros hijos y a vuestras mujeres, los templos de los dioses de vuestros padres y las tumbas de vuestros antepasados. ¡Ahora se lucha por todo!",
    PAP('¡Adelante, hijos de los griegos! Liberad la patria. ¡Ahora se lucha por todo!', 'Esquilo, que luchó en Salamina', 'Los persas, 402 – 405', at='Adelante, hijos de los griegos'))
HER("Jerjes contemplaba la batalla sentado al pie del monte Egaleo. Cada vez que veía a uno de los suyos hacer algo notable, preguntaba quién era, y sus escribas anotaban el nombre del capitán y de su ciudad.",
    ai('jerjes_escribas', 'a king seated on a golden throne on a hillside, scribes beside him writing on tablets, watching a naval battle in the strait below, smoke rising', at='sus escribas anotaban'))
NEW("Entre sus capitanes había una mujer: Artemisia, reina de Halicarnaso, la ciudad natal de Heródoto. Había aconsejado a Jerjes no luchar en el mar. En plena batalla, para escapar, embistió a un barco de su propio bando. Jerjes, desde lejos, creyó que había hundido uno griego.",
    ph('Artemisia I of Caria Salamis Kaulbach', at='Artemisia', lt=['Artemisia I', 'Reina de Halicarnaso · aliada de Jerjes', 'persia']))
JER("[serious] Mis hombres se han convertido en mujeres. Y mis mujeres, en hombres.",
    PAP('Mis hombres se han convertido en mujeres, y mis mujeres, en hombres.', 'Jerjes en Salamina, según Heródoto', 'Historias, VIII, 88', at='Mis hombres'))
NAR("[serious] Salamina fue un desastre para Persia. Jerjes volvió a Asia y dejó en Grecia a su mejor general, Mardonio, con un ejército escogido.",
    ph('Battle of Salamis Kaulbach painting', at='Salamina fue un desastre'))
ESP("[dramatically] Platea, verano del año cuatrocientos setenta y nueve. Mardonio lucha en primera fila, sobre un caballo blanco, rodeado de mil persas escogidos. Mientras él sigue vivo, los persas aguantan. Entonces un espartano llamado Arimnesto lo derriba. [pause] Mardonio cae. Y con él, todo el ejército. Persia nunca volvería a invadir Grecia.",
    ai('platea_batalla', 'a great land battle on a wide plain below a mountain, Spartan hoplites breaking through Persian lines, a fallen commander on a white horse, dust', at='Platea'))
NEW("[serious] Pero conviene mirar el mapa. Para los griegos, aquello fue la guerra que salvó su mundo. Para Persia, fue un fracaso en el extremo occidental de un imperio que seguía llegando hasta la India. No perdió Egipto, ni Babilonia, ni Asia Menor. [short pause] Jerjes siguió reinando catorce años más.",
    cd(dict(type='imperio', title='479 a. C.: después de Platea', bbox=[10, 12, 80, 48], stages=[
        dict(year='Grecia', label='Lo que Persia no consiguió', zona=['GRC']),
        dict(year='Persia', label='Lo que Persia conservó', zona=['TUR', 'EGY', 'IRQ', 'SYR', 'IRN', 'AFG', 'PAK', 'LBN', 'ISR', 'JOR', 'ARM', 'AZE', 'TKM', 'UZB', 'CYP', 'PSE'])]), at='conviene mirar el mapa'))
NAR("[dramatically] Hasta una noche de agosto del año cuatrocientos sesenta y cinco. [pause] Jerjes dormía en su palacio. Y el hombre que entró en su habitación no era un enemigo. Era el jefe de su propia guardia.",
    ai('jerjes_asesinado', 'a shadowy armed figure entering a royal bedchamber at night with a dagger, moonlight through curtains, a sleeping king, silent tension', at='entró en su habitación'))
