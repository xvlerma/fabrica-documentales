# -*- coding: utf-8 -*-
# «Las estafas más grandes de la historia» · parte 1: apertura, la pirámide y el país que no existía
from lib import *

# ---------------- APERTURA ----------------
B('tension')
NAR("[serious] Nueva York, diez de diciembre de dos mil ocho. Wall Street se hunde en la peor crisis desde mil novecientos veintinueve. Y en una oficina del centro de Manhattan, uno de los financieros más respetados del mundo llama a sus dos hijos a su despacho.",
    ph('Lipstick Building New York', at='Nueva York', lt=['El edificio Lipstick', 'Tercera Avenida, Nueva York · sede de la firma Madoff']),
    ai('wall_street_2008', 'traders on a New York stock exchange floor in 2008 holding their heads in despair under red screens, seen from behind, motion blur', at='Wall Street se hunde'),
    ai('despacho_noche', 'an executive office high in a Manhattan skyscraper at night, city lights through the window, an empty leather chair behind a large desk', at='llama a sus dos hijos'))
NAR("Les dice que ya no puede más. Que no le queda nada. Y les dice una frase que ellos repetirán ante las autoridades al día siguiente.",
    ai('manos_mesa', 'close-up of an old man\'s hands resting on a polished desk, a fountain pen and an unopened envelope, night, lamplight', at='ya no puede más'),
    ai('dos_hijos', 'two men in suits standing frozen in a dark office doorway, backlit silhouettes, a third older man seated in shadow before them', at='les dice una frase'))
MAD("[softly] Todo es una gran mentira.",
    cd(dict(type='quote', text='Todo es una gran mentira.', attrib='Bernard Madoff a sus hijos · 10 de diciembre de 2008, según la denuncia de la SEC'), at='Todo es'))
INV("[serious] Ese hombre se llamaba Bernard Madoff. Había presidido el Nasdaq, la bolsa tecnológica de Nueva York. Y durante décadas había dirigido la mayor estafa piramidal de la historia: sesenta y cinco mil millones de dólares en cuentas que, sobre el papel, existían. Y que en realidad no existían.",
    ph('Bernard Madoff mugshot 2009', at='Bernard Madoff', lt=['Bernard Madoff', 'Financiero · expresidente del Nasdaq', 'estafa']),
    ph('Nasdaq MarketSite Times Square', at='el Nasdaq'),
    cd(dict(type='counter', to=65000, label='millones de dólares en cuentas que no existían', prefix='$'), at='sesenta y cinco mil millones'))
NAR("Apenas un año antes, en un debate público sobre los mercados, ese mismo hombre había dicho esto.",
    ai('panel_debate', 'a small conference stage with a panel table and microphones under spotlights, an audience in the dark, 2007', at='en un debate público'))
MAD("En el entorno regulatorio actual, es prácticamente imposible violar las normas. Es imposible que una infracción pase desapercibida. Y desde luego, no durante mucho tiempo.",
    cd(dict(type='quote', text='Es imposible que una infracción pase desapercibida. Y desde luego, no durante mucho tiempo.', attrib='Bernard Madoff · debate público, octubre de 2007'), at='En el entorno regulatorio'))
NAR("Pero Madoff no inventó nada. Casi dos siglos antes, un escocés ya había vendido un país entero que no existía. Un inmigrante italiano dio su nombre a la estafa. Un conde falso vendió la Torre Eiffel. Dos veces. Y el hombre más poderoso de Suecia apareció muerto en París cuando su imperio de papel empezó a arder.",
    ph('Gregor MacGregor portrait', at='un escocés'),
    ph('Charles Ponzi 1920', at='Un inmigrante italiano'),
    ph('Eiffel Tower 1920s', at='la Torre Eiffel'),
    ph('Ivar Kreuger', at='Suecia'))
NAR("[pause] Y en España, casi medio millón de familias metieron sus ahorros en algo tan inocente como un álbum de sellos.",
    ai('album_sellos', 'an open stamp collection album on a kitchen table in a modest Spanish home, reading glasses beside it, afternoon window light', at='un álbum de sellos'))
INV("Seis expedientes. Seis disfraces del mismo engaño. ¿Cómo se convence a miles de personas a la vez? ¿Por qué nadie lo vio venir, ni los bancos, ni los gobiernos, ni los expertos? [pause] ¿Y podría volver a pasarte a ti?",
    ai('archivador', 'a row of six worn cardboard case files tied with red string on a detective desk under a green banker\'s lamp, no readable text', at='Seis expedientes'),
    ai('fila_oficina', 'a long queue of people in winter coats waiting outside a closed office door at dawn, seen from behind, wet pavement', at='podría volver'))
T('Las estafas más grandes de la historia', 'De Ponzi a Madoff', secs=5.5, sting='tema', text='[dramatically] Las estafas más grandes de la historia. De Ponzi a Madoff.', chapter=False)

# ---------------- ANTES DE EMPEZAR: LA PIRÁMIDE ----------------
B('fondo')
NAR("Antes de abrir el primer expediente, hay que entender el truco. Porque casi todas estas historias usan el mismo, con distinto disfraz.",
    ai('trile_mesa', 'a street hustler\'s hands moving three cups on a small folding table, a coin half hidden, night street, close-up', at='el truco'))
INV("Funciona así. Alguien te promete una rentabilidad alta y, sobre todo, segura. Le das tu dinero. Al cabo de unos meses, te paga lo prometido. Puntual. [short pause] Lo que no sabes es que ese dinero no sale de ningún negocio. Sale del bolsillo del siguiente que ha llegado.",
    cd(dict(type='list', header='Cómo funciona una pirámide', items=[('La promesa', 'una rentabilidad alta y segura'), ('El pago puntual', 'con el dinero del que llega después'), ('El boca a boca', 'los primeros traen a otros'), ('El derrumbe', 'cuando dejan de entrar nuevos')]), at='Funciona así'))
NAR("Mientras entre dinero nuevo, la rueda gira. Los primeros cobran, les cuentan a sus amigos que funciona, y los amigos traen a más amigos. Pero cada promesa exige más dinero que la anterior. Y el día que dejan de llegar nuevos inversores, o que muchos piden su dinero a la vez, la pirámide se derrumba en cuestión de días.",
    ai('billetes_mano', 'hands passing a thick envelope of banknotes across a table to other hands, dim lamplight, close-up', at='la rueda gira'),
    ai('cena_amigos', 'friends around a dinner table raising glasses in a warm 1950s-style living room, one man leaning in to whisper a tip, faces in soft shadow', at='los amigos traen'),
    ai('fichas_domino', 'a long line of falling dominoes on a dark wooden table, motion blur, low angle, dramatic side light', at='se derrumba'))
INV("Hoy lo llamamos esquema Ponzi. Pero el primer gran maestro del engaño financiero moderno no fue Ponzi. Fue un soldado escocés que, un siglo antes, se coronó príncipe de un país imaginario.",
    ph('Gregor MacGregor portrait', at='soldado escocés'))

# ---------------- I · EL PAÍS QUE NO EXISTÍA ----------------
T('El país que no existía', 'Londres, 1822', num='I', sting='tema')
DOC("Expediente número uno. Sospechoso: Gregor MacGregor, militar escocés. Se hace llamar príncipe. Delito: vender bonos, tierras y cargos de un país que no existe. Víctimas: cientos de inversores y unos doscientos cincuenta colonos.",
    cd(dict(type='ficha', name='Gregor MacGregor', role='Se hace llamar cacique de Poyais', group='Expediente I · un país inventado', color=[196, 38, 34]), at='Expediente'),
    ph('Gregor MacGregor portrait', at='Sospechoso'))
B('ironia')
NAR("Londres, mil ochocientos veintiuno. Llega a la ciudad un hombre de uniforme, con medallas, una historia de película y un título que nadie había oído jamás: cacique de Poyais.",
    ph('London 1820s engraving', at='Londres', lt=['Londres', 'Grabado de la época']),
    ph('Gregor MacGregor portrait', at='un hombre de uniforme', lt=['Gregor MacGregor', 'Militar y aventurero escocés · 1786-1845', 'estafa']),
    ai('salon_londres', 'a candlelit Regency-era London drawing room full of gentlemen in tailcoats gathered around a uniformed officer telling a story, faces turned away', at='una historia de película'))
INV("Se llamaba Gregor MacGregor. Era escocés y había luchado de verdad en las guerras de independencia de Sudamérica, a las órdenes de Simón Bolívar. Eso no era mentira. Lo que vino después, sí.",
    ph('Simon Bolivar portrait', at='Simón Bolívar', lt=['Simón Bolívar', 'Libertador sudamericano']),
    ai('batalla_independencia', 'a 19th-century South American independence war cavalry charge across a dusty plain, flags and smoke, painterly grain', at='guerras de independencia'))
NAR("MacGregor contaba que el rey de la costa de los Mosquitos, en la actual Honduras, le había regalado un territorio enorme. Un país con su capital, su catedral, su teatro, su banco y ríos donde el oro se recogía casi con la mano. Un paraíso esperando a colonos británicos.",
    cd(dict(type='map', title='La costa de los Mosquitos · 1820', bbox=[-88.5, 13.0, -82.5, 17.5], points=[dict(name='«Poyais»', lon=-84.9, lat=15.9, big=1), dict(name='Belice', lon=-88.2, lat=17.25), dict(name='Golfo de Honduras', lon=-87.5, lat=16.2)]), at='costa de los Mosquitos'),
    ai('ciudad_sonada', 'an idealised 19th-century view of a colonial tropical capital with a cathedral, a theatre and wide avenues by a river, golden light, painterly', at='su capital'),
    ai('oro_rio', 'a hand scooping gold nuggets from a crystal clear jungle river, sunbeams, dreamlike', at='el oro se recogía'))
DOC("Esbozo de la costa de los Mosquitos y del territorio de Poyais. Por el capitán Thomas Strangeways. Londres, mil ochocientos veintidós.",
    cd(dict(type='doc', title='Sketch of the Mosquito Shore', lines=['Guía del territorio de Poyais', 'Atribuida al «capitán Thomas Strangeways»', 'Londres, 1822'], source='El autor no existía: el libro se atribuye al propio MacGregor'), at='Esbozo'))
INV("Ese libro de más de trescientas páginas describía el clima, los cultivos, las costumbres de los nativos. Su autor, el capitán Strangeways, no existía. Los historiadores lo atribuyen al propio MacGregor. [short pause] Era, quizá, la primera gran campaña de marketing de una estafa.",
    ai('libro_poyais', 'an old 1822 leather-bound guidebook lying open on a Regency writing desk, an engraved landscape illustration on the page, candlelight, no readable text', at='Ese libro'),
    ai('pluma_libro', 'a quill pen writing in a thick leather-bound manuscript by candlelight, ink pot, wax seal, Regency era desk', at='no existía'),
    KA('MARKETING', 'certificado_tierras', 'an ornate 19th-century land grant certificate with an engraved border and a red wax seal on a desk next to a quill, no readable text', at='campaña de marketing'))
NAR("Y funcionó. En octubre de mil ochocientos veintidós, la City de Londres le concedió un préstamo a nombre del gobierno de Poyais: doscientas mil libras. Vendía bonos del Estado, tierras a precio de saldo y hasta cargos de oficial en su ejército. Imprimió incluso billetes de su propio banco.",
    ph('Royal Exchange London 19th century', at='la City de Londres', lt=['La Bolsa de Londres', 'Royal Exchange · siglo XIX']),
    cd(dict(type='counter', to=200000, label='libras en bonos de un país inventado (1822)', prefix='£'), at='doscientas mil libras'),
    ph('Poyais dollar banknote', at='billetes de su propio banco', lt=['Billete de Poyais', 'Dólar del «Banco de Poyais»']))
INV("[softly] Había para todos los gustos. Cargos en el banco de Poyais, grados de capitán en su guardia. Y un zapatero de Edimburgo fue nombrado, ni más ni menos, zapatero oficial de la corte del príncipe.",
    ai('zapatero_taller', 'a Scottish cobbler\'s workshop in 1822, leather boots on a bench, tools hanging, a framed official-looking appointment certificate on the wall, warm window light', at='zapatero oficial'),
    KA('ZAPATERO REAL', 'botas_reales', 'a pair of polished leather riding boots on a velvet cushion beside a parchment with a crown-shaped wax seal, Regency era, lamplight', at='ni más ni menos'))
NAR("Muchos compradores eran escoceses de clase media. Gente que vendió lo que tenía para empezar de cero en el Nuevo Mundo. Cambiaron sus libras por dólares de Poyais, convencidos de que allí valdrían más.",
    ai('maletas_muelle', 'a family\'s wooden trunks and a child\'s small suitcase on a foggy 19th-century harbour quay, ship rigging behind, seen from behind', at='empezar de cero'),
    ai('cambio_billetes', 'a bank counter in 1822 Edinburgh, a hand pushing gold sovereigns under a brass grille and receiving colourful foreign banknotes, close-up', at='Cambiaron sus libras'))
NAR("[serious] En septiembre de mil ochocientos veintidós zarpó de Londres el primer barco, el Honduras Packet, con unos setenta colonos. En enero le siguió el Kennersley Castle, desde el puerto escocés de Leith, con casi doscientos más. Médicos, abogados, artesanos. Familias enteras.",
    ai('velero_tormenta', 'a 19th-century sailing brig crossing a grey Atlantic sea under storm clouds, small figures on deck from far away', at='el primer barco'),
    ph('Leith harbour 19th century', at='Leith', lt=['Puerto de Leith', 'Edimburgo, Escocia']),
    cd(dict(type='timeline', header='Los barcos de Poyais', events=[['Sep 1822', 'Honduras Packet · unos 70 colonos'], ['Ene 1823', 'Kennersley Castle · casi 200'], ['1823', 'Lluvias, malaria y fiebre amarilla']]), at='Familias enteras'))
INV("Cuando llegaron a la costa, buscaron la capital. No había capital. No había catedral, ni teatro, ni banco. Había selva. Mosquitos. Un puñado de cabañas. Y unos nativos que no sabían nada de ningún príncipe de Poyais.",
    ai('desembarco', 'settlers in 1820s clothes wading ashore from rowing boats onto a desolate jungle beach, looking around in confusion, seen from behind', at='buscaron la capital'),
    ai('selva_costa', 'an untouched tropical jungle coastline with a muddy river mouth, a few makeshift palm-leaf shelters, heavy humid haze', at='Había selva'),
    ai('selva_mosquitia', 'a muddy jungle river lined with mangroves under a heavy grey sky, swarms of insects over the water, untouched wilderness, no people', at='Mosquitos'))
NAR("[pause] Llegaron las lluvias. Y con ellas, la malaria y la fiebre amarilla. De los cerca de doscientos cincuenta colonos que viajaron a Poyais, más de la mitad murieron. El zapatero de la corte, desesperado, se quitó la vida.",
    ai('lluvia_cabana', 'torrential tropical rain on a collapsing palm-leaf shelter at night, a lantern flickering inside, mud everywhere', at='Llegaron las lluvias'),
    cd(dict(type='counter', to=250, label='colonos viajaron a Poyais · más de la mitad murieron'), at='doscientos cincuenta'),
    ai('cruces_playa', 'simple wooden crosses on a rainy tropical beach at dusk, palm trees bending in the wind', at='más de la mitad murieron'))
INV("Los supervivientes fueron rescatados y llevados a la colonia británica de Belice. En octubre de mil ochocientos veintitrés, unos cincuenta volvieron a Londres. Y aquí viene lo más increíble: algunos seguían defendiendo a MacGregor. Pensaban que les habían fallado sus agentes, no él.",
    ai('rescate_barco', 'a rescue ship\'s rowing boat taking exhausted ragged settlers off a jungle beach at dawn, mist, seen from a distance', at='rescatados'),
    ph('London street 1820s engraving', at='volvieron a Londres'),
    K('LO DEFENDÍAN', 'Gregor MacGregor portrait', at='seguían defendiendo'))
NAR("MacGregor ya había huido a Francia, donde intentó el mismo golpe con inversores franceses. Lo juzgaron en París. Y salió absuelto. Volvió a Venezuela, que le reconoció su grado de general y una pensión, y murió en Caracas en mil ochocientos cuarenta y cinco. [short pause] Nunca fue condenado por nada.",
    ph('Palais de Justice Paris engraving', at='Lo juzgaron en París'),
    ph('Caracas 19th century', at='murió en Caracas'),
    K('NUNCA CONDENADO', 'Gregor MacGregor portrait', at='Nunca fue condenado'))
INV("Poyais nos deja la primera lección de este expediente. A la gente no se la engaña con números. Se la engaña con una historia que quiere creer.",
    cd(dict(type='quote', text='A la gente no se la engaña con números. Se la engaña con una historia que quiere creer.', attrib='Expediente I · Poyais · caso cerrado'), at='primera lección'))
