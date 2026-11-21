# -*- coding: utf-8 -*-
# «Crisis de 2008» · parte 1: apertura, la fiesta del ladrillo y los que lo vieron venir
from lib import *

# ---------------- APERTURA ----------------
B('tension')
NAR("[serious] La crisis de dos mil ocho dejó en España seis millones de parados, cientos de miles de familias sin casa y un rescate bancario de decenas de miles de millones de euros. Y empezó con algo que parecía imposible que saliera mal: un piso.",
    ph('Residencial Francisco Hernando Seseña', at='La crisis de dos mil ocho', lt=['Seseña, Toledo', 'La urbanización de El Pocero']),
    ai('cola_paro', 'a long queue of unemployed people in winter coats outside a Spanish employment office at dawn, seen from behind, wet pavement, dramatic low sun', at='seis millones de parados'),
    ai('desahucio_puerta', 'a family carrying boxes and a child\'s bicycle down the stairs of an apartment block while police officers wait at the door, seen from behind, tense', at='familias sin casa'),
    ai('grua_atardecer', 'a single tower crane over an unfinished brick apartment block at sunset, a lone worker climbing, strong backlight', at='un piso'))
DAT("Ahora mira este dato. En dos mil siete, en lo más alto de la burbuja, el metro cuadrado de vivienda libre en España llegó a dos mil ochenta y cinco euros. A finales de dos mil veinticinco ha llegado a dos mil doscientos treinta. Nunca había costado tanto.",
    HOY(['2007 · máximo de la burbuja', '2.085 €/m²', 'vivienda libre tasada'], ['2025 · último dato', '2.230 €/m²', 'un 7 % por encima'], at='Ahora mira este dato'),
    cd(dict(type='counter', **{'from': 2085}, to=2230, label='euros por metro cuadrado · vivienda libre, 2025', suffix=' €'), at='dos mil doscientos treinta'))
NEW("Y entonces, como ahora, las familias se preguntaban lo mismo: si comprar ya, antes de que subiera más, o esperar. En dos mil siete, casi nadie esperó.",
    ai('pareja_escaparate', 'a young couple looking at apartment listings in the window of a real estate agency at night, their reflections in the glass, warm light from inside', at='si comprar ya'),
    ai('firma_notaria', 'hands signing a thick mortgage contract at a notary desk, a pen, a set of new keys on the table, close-up, golden light', at='casi nadie esperó'))
NAR("[pause] Para entender si estamos otra vez en el mismo punto, hay que volver al principio. A la década en la que España se convenció de que el ladrillo nunca baja. Al día en que un banco de Nueva York cayó y arrastró a medio mundo. Y a los años en los que este país aprendió, a golpes, palabras como desahucio, prima de riesgo o rescate.",
    ph('Lehman Brothers headquarters 2008', at='un banco de Nueva York', lt=['Sede de Lehman Brothers', 'Nueva York · septiembre de 2008']),
    ai('multitud_sol', 'a huge crowd filling a Madrid square at night, thousands of people with raised hands and handmade banners without readable words, aerial view, epic', at='aprendió, a golpes'))
NEW("¿Cómo llegó un país entero a construir más casas que nadie en Europa? ¿Quién lo vio venir y por qué nadie lo paró? [pause] Y la pregunta grande, la que responderemos al final: ¿se está repitiendo?",
    ai('mapa_gruas', 'a Spanish coastline seen from a plane covered with dozens of tower cranes and half-built apartment blocks, epic wide aerial', at='más casas que nadie'),
    ai('reloj_oficina', 'a dark office of a central bank at night, a single desk lamp, piles of reports, a silhouette at the window looking at the city', at='Quién lo vio venir'),
    ai('cruce_hoy', 'a modern Spanish city street today with apartment blocks and a rent sign on a balcony, evening, people walking with phones, seen from behind', at='se está repitiendo'))
T('Crisis de 2008', 'Así se arruinó España (y puede repetirse)', secs=5.5, sting='tema', text='[dramatically] Crisis de dos mil ocho. Así se arruinó España.', chapter=False)

# ---------------- CAPÍTULO 1 · LA FIESTA DEL LADRILLO ----------------
T('La fiesta del ladrillo', '1997 · 2006', num='I', secs=4.5, sting='tema')
B('fiesta')
NAR("[serious] Seseña, provincia de Toledo, dos mil tres. A cuarenta kilómetros de la Puerta del Sol, en mitad de un campo de cereal, un constructor hecho a sí mismo anuncia la mayor urbanización de España. Trece mil quinientos pisos. En un pueblo que entonces tenía unos diez mil habitantes.",
    ph('Seseña Toledo', at='Seseña', lt=['Seseña', 'Toledo · La Sagra']),
    ai('campo_cereal', 'a vast wheat field on the plains south of Madrid with the first excavators arriving, dust clouds, wide shot, early morning', at='en mitad de un campo de cereal'),
    cd(dict(type='counter', to=13500, label='pisos proyectados en El Quiñón, Seseña'), at='Trece mil quinientos pisos'))
NEW("Se llamaba Francisco Hernando, aunque toda España lo conocía por su apodo: El Pocero. Había empezado limpiando pozos negros en Madrid. Ahora levantaba una ciudad entera con su nombre.",
    ph('Francisco Hernando Contreras', at='Francisco Hernando', lt=['Francisco Hernando, «El Pocero»', 'Promotor · Onde 2000', 'banca']),
    ai('pocero_obra', 'a powerful man in a suit seen from behind standing on a mound of earth overlooking hundreds of foundations and cranes, arms spread, epic', at='levantaba una ciudad'))
NAR("No era una locura aislada. Era el espíritu de una época. Y para entenderla hay que conocer las tres piezas que encendieron la fiesta.",
    ai('tres_piezas', 'three huge glowing objects on a dark table: a euro coin, a stack of bricks and a bank key, dramatic spotlight, still life', at='las tres piezas'))
NEW("La primera, el dinero barato. En mil novecientos noventa y nueve llega el euro y, con él, los tipos de interés de Alemania. De repente, una hipoteca en España cuesta la mitad que pocos años antes.",
    ph('Euro coins 2002', at='llega el euro'),
    ai('cambio_pesetas', 'hands exchanging old Spanish peseta banknotes for brand new euro notes at a bank counter, 2002, close-up, festive light', at='los tipos de interés de Alemania'),
    cd(dict(type='kw', word='DINERO BARATO'), at='La primera'))
DAT("En junio de dos mil tres, el euríbor, el índice al que van atadas casi todas las hipotecas españolas, cae hasta el dos coma cero uno por ciento. El mínimo de su historia hasta entonces.",
    cd(dict(type='counter', to=2.01, dec=2, suffix=' %', label='euríbor · junio de 2003, mínimo de entonces'), at='cae hasta el dos coma cero uno'))
NEW("La segunda pieza, el suelo. En mil novecientos noventa y ocho se aprueba una nueva ley que convierte en urbanizable casi todo lo que no esté protegido. La idea era sencilla: si hay más suelo para construir, las casas bajarán. Pasó justo lo contrario.",
    ai('topografo', 'a surveyor with a tripod measuring an empty dry hillside dotted with olive trees, red and white stakes in the ground, long shadows', at='convierte en urbanizable'),
    cd(dict(type='doc', title='Ley 6/1998 sobre régimen del suelo y valoraciones', lines=['Todo el suelo que no esté protegido', 'podrá considerarse urbanizable'], source='Boletín Oficial del Estado · 13 de abril de 1998'), at='se aprueba una nueva ley'))
DOC("Exposición de motivos de la ley: la reforma pretende facilitar el aumento de la oferta de suelo, haciendo posible que todo el suelo que todavía no ha sido incorporado al proceso urbano, en el que no concurran razones para su preservación, pueda considerarse susceptible de ser urbanizado.",
    cd(dict(type='doc', title='Ley 6/1998 · exposición de motivos', lines=['Facilitar el aumento de la oferta de suelo', 'Todo el suelo no protegido, susceptible de ser urbanizado'], source='Boletín Oficial del Estado · 1998'), at='Exposición de motivos'))
NEW("Y la tercera pieza, la más española de todas: las cajas de ahorros. Medio sistema financiero del país en manos de entidades sin accionistas, cuyos consejos repartían los partidos, los sindicatos y las administraciones. Ellas pusieron buena parte del dinero.",
    ph('Caja Madrid sede', at='las cajas de ahorros'),
    ai('consejo_caja', 'a long boardroom table with many empty leather chairs and name plates without readable text, crystal water glasses, chandelier, top view', at='cuyos consejos repartían'))
B('tension')
NAR("Con el dinero barato, el suelo abierto y las cajas prestando, la máquina arrancó. Y ya no paró.",
    ai('hormigonera', 'a line of concrete mixer trucks driving at speed on a dusty road into a giant construction site, motion blur, action, sunset', at='la máquina arrancó'))
NEW("Y hubo una cuarta pieza que nadie había previsto: la gente. En pocos años llegaron a España millones de personas de Ecuador, de Rumanía, de Marruecos, de Colombia, atraídas por el trabajo que daba la propia construcción. Y todas necesitaban un techo.",
    ai('llegada_inmigrantes', 'newly arrived immigrant workers with backpacks walking out of a Madrid bus station into the morning sun, seen from behind, hopeful, busy street', at='la gente'))
DAT("Los datos del padrón lo dejan claro. En dos mil uno, España tenía unos cuarenta y un millones de habitantes. En dos mil ocho, más de cuarenta y seis. Cinco millones más en siete años. Casi tanto como toda la población de la Comunidad Valenciana.",
    cd(dict(type='counter', **{'from': 41000000}, to=46000000, label='habitantes de España · de 2001 a 2008'), at='Los datos del padrón'))
DAT("Mil novecientos noventa y siete: el precio de la vivienda empieza a subir. En los nueve años siguientes sube más de un ciento ochenta por ciento. Los sueldos, en ese mismo tiempo, apenas se mueven en comparación.",
    cd(dict(type='timeline', header='Precio de la vivienda', events=[('1997', 'empieza la subida'), ('2002', 'llega el euro en monedas'), ('2006', '+183 % desde 1998'), ('2007', 'máximo de la burbuja')]), at='Mil novecientos noventa y siete'))
NEW("Y España empezó a construir como nadie. En dos mil seis se iniciaron más de ochocientas mil viviendas en un solo año.",
    cd(dict(type='counter', to=800000, label='viviendas iniciadas en 2006 · más de'), at='más de ochocientas mil viviendas'),
    ai('obra_noche', 'a gigantic construction site lit by floodlights at night, dozens of workers, cranes swinging steel beams, sparks from welding, epic action', at='a construir como nadie'))
NAR("[pause] Algunos años de la burbuja, España empezó más viviendas que Alemania, Francia e Italia juntas. Tres países que sumaban más de cuatro veces su población.",
    cd(dict(type='versus', title='Viviendas nuevas en un año de la burbuja', left=dict(name='España', lines=['Más de 800.000', '44 millones de habitantes'], color=BAN), right=dict(name='Alemania + Francia + Italia', lines=['Menos, entre los tres', 'Más de 200 millones de habitantes'], color=POL)), at='más viviendas que Alemania'))
NEW("La construcción llegó a pesar más del doble que en la media de los grandes países europeos. Uno de cada ocho trabajadores españoles vivía del ladrillo. Y miles de chavales dejaban el instituto a los dieciséis años para subirse a un andamio. Algunos ganaban más que sus profesores.",
    ai('chaval_andamio', 'a teenage construction worker in a hard hat on scaffolding high above a new neighbourhood, seen from behind, wind, sunny, a crane in the background', at='para subirse a un andamio'),
    ai('aula_vacia', 'an empty high school classroom in Spain with half the chairs on the desks, afternoon light through the windows, a forgotten backpack', at='dejaban el instituto'))
PRE("[softly] Y así se anunciaban los pisos en dos mil seis. Hipotecas a cuarenta años. Algunas cajas ya ofrecían hasta cincuenta, para menores de treinta y cinco, con el cien por cien del precio financiado y cinco años pagando solo intereses.",
    cd(dict(type='list', header='Así se vendía una hipoteca en 2006', items=[('Hasta 50 años', 'para menores de 35'), ('100 % financiado', 'sin entrada'), ('5 años de carencia', 'pagando solo intereses'), ('Interés variable', 'atado al euríbor')]), at='así se anunciaban'),
    ai('folleto_banco', 'a glossy bank brochure with a smiling family drawn as abstract shapes and a house key, on a bank counter, no readable text, warm light', at='Hipotecas a cuarenta años'))
NEW("Los bancos y las cajas competían por darte el préstamo. Las tasadoras valoraban el piso por encima de lo que costaba, para que la hipoteca cubriera también los muebles, el coche y, a veces, las vacaciones.",
    ai('tasador', 'a man with a clipboard and a measuring tape in an empty brand new apartment, sunlight through big windows, plastic still on the floor', at='Las tasadoras valoraban'))
DAT("Hoy esto suena a otro planeta. En dos mil ocho, el noventa y siete por ciento de las hipotecas nuevas eran a tipo variable. A finales de dos mil veinticinco, solo cuatro de cada diez lo son. La mayoría de las familias que compran hoy pagan una cuota fija.",
    HOY(['2008', '97 % de hipotecas variables', 'atadas al euríbor'], ['2025', '6 de cada 10 a tipo fijo', 'cuota que no cambia'], at='Hoy esto suena a otro planeta'))
B('fiesta')
NAR("Y mientras tanto, la fiesta se extendía por todo el país. En la costa mediterránea, en los alrededores de Madrid, en pueblos de interior que nunca habían visto una grúa.",
    cd(dict(type='map', title='La burbuja en el mapa · 2006', bbox=[-9.5, 36.0, 3.5, 43.8], points=[dict(name='Seseña', lon=-3.70, lat=40.10, big=1), dict(name='Madrid', lon=-3.70, lat=40.42), dict(name='Valencia', lon=-0.38, lat=39.47), dict(name='Castellón', lon=-0.04, lat=39.99), dict(name='Ciudad Real', lon=-3.93, lat=38.99), dict(name='Marbella', lon=-4.88, lat=36.51), dict(name='Murcia', lon=-1.13, lat=37.99)]), at='se extendía por todo el país'),
    ph('Benidorm skyline', at='la costa mediterránea'),
    ai('pueblo_grua', 'a small whitewashed village on a dry Spanish plain with three tower cranes rising over new beige apartment blocks behind the church, wide shot', at='pueblos de interior'))
NEW("Ayuntamientos que firmaban recalificaciones a cambio de dinero para fiestas, polideportivos o rotondas. Rotondas con esculturas gigantes. Aeropuertos. Parques temáticos. Palacios de congresos.",
    ai('rotonda', 'a huge abstract metal sculpture in the middle of a brand new roundabout surrounded by empty plots and streetlights, sunset, slightly absurd', at='Rotondas con esculturas gigantes'),
    ph('Ciudad de las Artes y las Ciencias Valencia', at='Palacios de congresos'))
PRE("Valencia tuvo la Copa América de vela y un circuito urbano de Fórmula Uno. Madrid, cuatro rascacielos nuevos en la Castellana. Y casi cada capital de provincia quiso su gran proyecto. Las obras se inauguraban con banda de música. Lo que costaban no se pagaría ya. Se pagaría después.",
    ph('Cuatro Torres Business Area Madrid', at='cuatro rascacielos nuevos'),
    ai('inauguracion_banda', 'a municipal brass band playing at the ribbon cutting of a huge empty new convention center, officials in suits and a small crowd with flags, sunny, festive, absurd scale', at='con banda de música'))
DAT("Las cuentas de los ayuntamientos se volvieron adictas al ladrillo. Las licencias de obra, el impuesto sobre construcciones y las ventas de suelo llegaron a ser una parte enorme de sus ingresos. Cuando la construcción se paró, muchos se quedaron con polideportivos que no podían mantener y deudas que no podían pagar.",
    ai('polideportivo_cerrado', 'a large modern municipal sports pavilion with a locked gate, weeds in the parking lot and a faded construction sign, overcast, abandoned', at='polideportivos que no podían mantener'))
NAR("[dramatically] Todo el mundo ganaba. O eso parecía. Porque nadie se hacía la pregunta incómoda: ¿quién iba a vivir en todas esas casas?",
    ai('urbanizacion_vacia', 'endless rows of identical new apartment blocks with no lights in any window at night, empty streets, a single streetlight, eerie', at='quién iba a vivir'))
DAT("Un estudio de la época lo calculó así: de las más de ochocientas mil viviendas construidas en un año, unas cuatrocientas cincuenta mil sobraban si se tenía en cuenta cuánta gente necesitaba casa de verdad.",
    cd(dict(type='split', left=dict(title='Construidas en un año', lines=['Más de 800.000']), right=dict(title='Sobraban', lines=['Unas 450.000', 'sin comprador real']), strike=False), at='Un estudio de la época'))
NEW("Muchas no se compraban para vivir. Se compraban para vender. Sobre plano, antes de que existieran. Y se revendían dos y tres veces antes de poner el último ladrillo.",
    ai('maqueta', 'a white architectural scale model of an apartment complex on a table in a sales office, hands pointing at it, a crowd of buyers around, dynamic', at='Sobre plano'))
PRE("[softly] En los telediarios de aquellos años se repetía una frase en bares, oficinas y comidas familiares: el piso nunca baja. Alquilar era tirar el dinero. Y el que no compraba, perdía.",
    ai('bar_tele', 'a crowded Spanish bar at lunchtime with a TV on the wall, men at the counter arguing and gesturing, plates of tapas, warm busy atmosphere, faces turned away', at='en bares, oficinas'))
DAT("Y en parte tenían razón, porque durante una década fue verdad. Entre mil novecientos noventa y ocho y dos mil seis, el precio de la vivienda casi se triplicó. Quien compraba un piso en mil novecientos noventa y ocho y lo vendía en dos mil seis, ganaba casi tres veces lo invertido, sin haber hecho nada.",
    cd(dict(type='split', left=dict(title='Piso comprado en 1998', lines=['100.000 euros']), right=dict(title='El mismo piso en 2006', lines=['Unos 280.000 euros', 'sin tocar un ladrillo']), strike=False), at='casi se triplicó'))
NAR("[pause] Y en Seseña, la ciudad de El Pocero empezaba a tomar forma. Bloques y bloques de ladrillo rojo en mitad de la nada. Sin colegio. Sin centro de salud. Sin agua garantizada. [short pause] Pero eso daba igual. Mientras los precios subieran, todo valía.",
    ph('El Quiñón Seseña', at='la ciudad de El Pocero'),
    ai('bloques_nada', 'dozens of identical red brick apartment blocks standing in the middle of an empty dusty plain, no trees, no people, harsh midday sun, aerial', at='en mitad de la nada'))

# ---------------- CAPÍTULO 2 · LOS QUE LO VIERON VENIR ----------------
T('Los que lo vieron venir', '2006 · 2007', num='II', secs=4.5, sting='tema')
B('tension')
NAR("[serious] Madrid, mayo de dos mil seis. Un grupo de inspectores del Banco de España, los encargados de vigilar a los bancos desde dentro, envía un escrito al Gobierno. No hablan con medias palabras.",
    ph('Banco de España edificio Cibeles', at='Banco de España', lt=['Banco de España', 'Madrid · Plaza de Cibeles']),
    ai('sobre_ministerio', 'an official envelope being placed on a large ministry desk by a hand, a window with Madrid rooftops behind, morning light, no readable text', at='envía un escrito al Gobierno'))
DOC("Según la información publicada años después, los inspectores describían la situación de la economía como delicada. Y el sector inmobiliario, como frágil.",
    cd(dict(type='doc', title='Escrito de los inspectores del Banco de España · 2006', lines=['La situación económica es «delicada»', 'El sector inmobiliario es «frágil»'], source='Según la información publicada por El Mundo (2011)'), at='los inspectores describían'))
NEW("Advertían de algo que hoy parece evidente: que las cajas y los bancos estaban prestando demasiado, a demasiado plazo y a gente que quizá no podría devolverlo. Aquel escrito no cambió nada.",
    ai('carpeta_archivo', 'a thick folder being filed away in a dusty archive cabinet by a hand, a drawer closing, dim light, close-up', at='no cambió nada'))
PRE("No eran los únicos. La palabra burbuja aparecía en la prensa económica desde dos mil tres. Algunos economistas y algunos libros lo advertían cada año. Y cada año, promotores, tasadoras y buena parte de los bancos respondían lo mismo: en España no hay burbuja, hay demanda. Y mientras la demanda siguiera, tenían razón.",
    ai('hemeroteca', 'a stack of financial newspapers from different years on a desk, the same warning headline repeated but blurred and unreadable, a coffee cup, morning light, editorial still life', at='La palabra burbuja aparecía'))
NAR("Porque en dos mil seis y dos mil siete, el discurso oficial era otro. España crecía más que nadie en Europa. Tenía superávit. Y el paro había bajado del ocho por ciento por primera vez en décadas.",
    ph('José Luis Rodríguez Zapatero 2007', at='el discurso oficial', lt=['José Luis Rodríguez Zapatero', 'Presidente del Gobierno · 2004-2011', 'gobierno']),
    cd(dict(type='list', header='España · 2007', items=[('Crecimiento', 'por encima de la media europea'), ('Superávit', 'en las cuentas públicas'), ('Paro', 'por debajo del 8 %')]), at='España crecía'))
NEW("Al otro lado del Atlántico, sin embargo, algo empezaba a crujir. En Estados Unidos, millones de hipotecas concedidas a familias sin ingresos estables, las llamadas hipotecas basura o subprime, dejan de pagarse.",
    ai('casas_usa', 'a suburban American street with foreclosure signs in front of several identical wooden houses, autumn leaves, overcast sky, no readable text', at='dejan de pagarse'))
PRE("Nueve de agosto de dos mil siete. El banco francés BNP Paribas congela tres de sus fondos. Dice que ya no puede saber cuánto valen. Los bancos de medio mundo dejan de prestarse dinero entre ellos de un día para otro.",
    ph('BNP Paribas siège Paris', at='BNP Paribas'),
    ai('pantallas_rojas', 'traders on a European stock exchange floor watching walls of red screens, phones in hand, frantic movement, motion blur, seen from behind', at='dejan de prestarse dinero'))
PRE("Catorce de septiembre de dos mil siete. Reino Unido. Cientos de clientes hacen cola en la puerta de las oficinas del banco Northern Rock para sacar sus ahorros. Es la primera retirada masiva de depósitos en un banco británico en más de un siglo. Las imágenes dan la vuelta al mundo.",
    ph('Northern Rock queue 2007', at='Northern Rock', lt=['Northern Rock', 'Reino Unido · septiembre de 2007', 'banca']),
    ai('cola_banco_uk', 'a long queue of worried customers in coats outside a British bank branch on a grey morning, police officer at the door, seen from behind, tense', at='hacen cola'))
NAR("En España, la reacción del Gobierno fue de calma. Agosto de dos mil siete. El vicepresidente económico, Pedro Solbes, sobre el efecto que tendría aquella crisis de las hipotecas americanas.",
    ph('Pedro Solbes', at='Pedro Solbes', lt=['Pedro Solbes', 'Vicepresidente y ministro de Economía', 'gobierno']))
SOL("Tendrá un impacto relativamente pequeño en la economía española.",
    cd(dict(type='quote', text='Tendrá un impacto «relativamente pequeño» en la economía española.', attrib='Pedro Solbes · 17 de agosto de 2007'), at='Tendrá un impacto'))
NEW("Un mes después, el once de septiembre de dos mil siete, el presidente José Luis Rodríguez Zapatero dejó una frase para la historia.",
    ph('Zapatero 2007 discurso', at='el once de septiembre'))
ZAP("Haciendo uso de un símil futbolístico, se podría decir que España ha entrado en la Champions League de la economía mundial.",
    cd(dict(type='quote', text='España ha entrado en la Champions League de la economía mundial.', attrib='José Luis Rodríguez Zapatero · 11 de septiembre de 2007'), at='Haciendo uso'))
NAR("[pause] En ese mismo momento, sin que nadie lo dijera en voz alta, la burbuja ya había tocado techo. Las ventas de pisos empezaban a caer. Los precios se frenaban. Y las grúas, sin que nadie lo notara, empezaban a quedarse quietas.",
    ai('grua_quieta', 'a tower crane frozen above an unfinished concrete skeleton building, its hook hanging still, grey sky, no workers, melancholic wide shot', at='empezaban a quedarse quietas'))
NEW("En febrero de dos mil ocho, en plena campaña electoral, el vicepresidente Solbes y el candidato económico del Partido Popular, Manuel Pizarro, se enfrentaron en un debate televisado. Pizarro hablaba de crisis. Solbes, de un frenazo pasajero. En marzo, el Partido Socialista volvió a ganar las elecciones.",
    ph('Manuel Pizarro', at='Manuel Pizarro', lt=['Manuel Pizarro', 'Candidato del PP · 2008', 'gobierno']),
    ai('plato_debate', 'a television debate studio with two lecterns facing each other under bright lights, cameras in the foreground, audience in darkness, seen from the back of the studio', at='un debate televisado'))
DAT("Las viviendas que se empezaron en dos mil siete fueron casi un veinticinco por ciento menos que el año anterior. Pero se terminaron más que nunca: casi seiscientas mil. Una bolsa enorme de pisos nuevos buscando dueño. Justo cuando los compradores empezaban a desaparecer.",
    cd(dict(type='split', left=dict(title='2007 · empezadas', lines=['Casi un 25 % menos']), right=dict(title='2007 · terminadas', lines=['Casi 600.000', 'más que nunca']), strike=False), at='Las viviendas que se empezaron'))
NEW("Y había un detalle que casi nadie miraba. El euríbor llevaba meses subiendo. Y con él, la cuota de millones de hipotecas variables.",
    cd(dict(type='timeline', header='Euríbor a 12 meses', events=[('2003', '2,01 %'), ('2005', '≈ 2,3 %'), ('2007', '4,56 %'), ('julio 2008', '5,39 %')]), at='El euríbor llevaba meses subiendo'))
DAT("En julio de dos mil siete estaba en el cuatro coma cincuenta y seis por ciento. Un año después, en julio de dos mil ocho, en el cinco coma treinta y nueve: el máximo de su historia. Para una hipoteca media, casi mil euros más al año.",
    cd(dict(type='counter', **{'from': 4.56}, to=5.39, dec=2, suffix=' %', label='euríbor · julio de 2008, máximo histórico'), at='cinco coma treinta y nueve'))
NAR("[serious] Las familias que se habían hipotecado al límite empezaron a hacer cuentas a final de mes. Las promotoras, a no vender. Y los bancos, a mirar con miedo lo que tenían en sus balances. [pause] Pero el verdadero golpe todavía no había llegado. Vendría de Nueva York. Y tenía nombre de banco.",
    ai('cocina_cuentas', 'a couple at a kitchen table at night with bills and a calculator, the woman holding her head, a single hanging lamp, seen from the side, faces in shadow', at='hacer cuentas a final de mes'),
    ph('Lehman Brothers 745 Seventh Avenue', at='Vendría de Nueva York'))
