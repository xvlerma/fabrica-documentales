# -*- coding: utf-8 -*-
# «Las estafas más grandes de la historia» · parte 2: Ponzi, Lustig y Kreuger
from lib import *

# ---------------- II · EL HOMBRE QUE DIO NOMBRE A LA ESTAFA ----------------
T('El hombre que dio nombre a la estafa', 'Boston, 1920', num='II', sting='tema')
DOC("Expediente número dos. Sospechoso: Carlo Ponzi, también llamado Charles. Inmigrante italiano, antecedentes por falsificación. Delito: prometer un cincuenta por ciento en cuarenta y cinco días. Víctimas: decenas de miles.",
    cd(dict(type='ficha', name='Charles Ponzi', role='Inmigrante italiano · antecedentes por falsificación', group='Expediente II · 50 % en 45 días', color=[196, 38, 34]), at='Expediente'),
    ph('Charles Ponzi 1920', at='Sospechoso'))
B('tema')
NAR("Boston, agosto de mil novecientos diecinueve. Un inmigrante italiano de poco más de metro y medio, elegante, sin un dólar en el bolsillo, abre una carta que le ha llegado desde España. Dentro hay un pequeño cupón de correos.",
    ph('Boston 1920 street', at='Boston', lt=['Boston', 'Estados Unidos · hacia 1920']),
    ph('Charles Ponzi 1920', at='Un inmigrante italiano', lt=['Charles Ponzi', 'Inmigrante italiano · 1882-1949', 'estafa']),
    ph('International reply coupon', at='un pequeño cupón'))
INV("Se llamaba Carlo Ponzi, aunque en América todos le conocían como Charles. Allí había fregado platos, trabajado de camarero y pasado por la cárcel en Canadá por falsificar un cheque. [short pause] Y aquel cupón le dio una idea.",
    ph('Charles Ponzi portrait', at='Carlo Ponzi'),
    ai('cocina_platos', 'a young immigrant seen from behind washing a mountain of dishes in a steaming 1910s restaurant kitchen sink, warm tungsten light', at='fregado platos'))
PON("Llegué a este país con dos dólares y cincuenta centavos en efectivo y un millón de dólares en esperanzas. Y esas esperanzas nunca me abandonaron.",
    cd(dict(type='quote', text='Llegué a este país con 2,50 dólares en efectivo y un millón de dólares en esperanzas. Y esas esperanzas nunca me abandonaron.', attrib='Charles Ponzi a The New York Times'), at='Llegué a este país'),
    ai('barco_inmigrantes', 'immigrants with suitcases crowding the deck of a steamship arriving in Boston harbour in 1903, seen from behind, morning fog', at='dos dólares'))
NAR("Era un cupón de respuesta internacional. Se compraba en un país y se canjeaba en otro por sellos. Pero tras la Primera Guerra Mundial, las monedas europeas se habían hundido. Un cupón comprado barato en Italia o en España se canjeaba en Estados Unidos por sellos que valían bastante más.",
    ph('International reply coupon Universal Postal Union', at='cupón de respuesta internacional', lt=['Cupón de respuesta internacional', 'Unión Postal Universal']),
    cd(dict(type='split', left=dict(title='Se compra en Europa', lines=['Moneda hundida tras la guerra', 'El cupón sale muy barato']), right=dict(title='Se canjea en EE. UU.', lines=['Sellos en dólares', 'Valen varias veces más']), strike=False), at='las monedas europeas'))
INV("Sobre el papel, era un negocio legal. En la práctica, era imposible a gran escala: había que comprar, transportar y canjear millones de cupones, y el beneficio de cada uno se medía en céntimos. [pause] Ponzi nunca lo hizo de verdad.",
    K('IMPOSIBLE', 'International reply coupon', at='imposible a gran escala'))
NAR("En enero de mil novecientos veinte fundó una empresa con un nombre imponente: Securities Exchange Company. Y lanzó una promesa que nadie había oído: un cincuenta por ciento de beneficio en cuarenta y cinco días.",
    ph('Charles Ponzi office Boston', at='fundó una empresa'),
    K('50 % EN 45 DÍAS', 'Boston 1920 bank', at='un cincuenta por ciento'))
INV("Para que te hagas una idea: los bancos pagaban entonces en torno a un cinco por ciento al año. Ponzi ofrecía diez veces más en seis semanas. Y lo más importante: los primeros clientes cobraron. Puntualmente.",
    cd(dict(type='split', left=dict(title='Un banco de 1920', lines=['Cerca de un 5 % al año']), right=dict(title='Charles Ponzi', lines=['50 % en 45 días', 'Pagado puntualmente… al principio']), strike=False), at='los bancos pagaban'))
NAR("Cobraron con el dinero de los que llegaban detrás. Pero eso nadie lo sabía. Lo que se sabía en Boston era que el italiano pagaba. Y el rumor corrió como la pólvora. En primavera entraban miles de dólares a la semana. En verano, cientos de miles al día.",
    ai('billetes_cajones', 'a 1920s office desk drawer overflowing with crumpled dollar banknotes, wastebaskets stuffed with money, dramatic side light', at='cientos de miles al día'))
INV("Las colas daban la vuelta a la manzana en Hanover Street. Según la revista Time, en los días de más jaleo hacían falta seis policías a caballo para ordenar a la multitud en la calle. En siete meses, unas treinta mil personas le confiaron más de diez millones de dólares. Se dijo incluso que buena parte de la policía de Boston había invertido con él.",
    ai('cola_ponzi', 'a long queue of men in 1920 hats and overcoats stretching along a Boston street to the door of a small office, seen from behind, morning light', at='Las colas'),
    ai('policia_caballo', 'mounted policemen on horses in 1920 uniforms keeping order beside a crowded Boston street, seen from behind', at='seis policías a caballo'),
    cd(dict(type='counter', to=10000000, label='dólares de unas 30.000 personas en siete meses (1920)', prefix='$'), at='diez millones'))
NAR("Ponzi se compró una mansión con piscina climatizada, se hizo con una parte de un banco y paseaba en limusina. Los periódicos le llamaban mago de las finanzas.",
    ai('mansion_1920', 'a large white colonial mansion with columns and a wide lawn in 1920 New England, a shiny black limousine in the driveway, golden afternoon light, no people', at='una mansión'),
    ai('limusina_1920', 'a chauffeur-driven black 1920 limousine gliding along a Boston street, passersby turning to look, seen from the side, no visible faces', at='paseaba en limusina'))
PON("Cuanto más compraba, más quería comprar. Era una manía.",
    ai('joyas_mesa', 'a velvet jewellery box overflowing with diamond necklaces and gold watches on a 1920s vanity table, mirror reflections', at='Era una manía'))
PON("Cuando gane mi primer millón, todo lo que pase de ese millón lo gastaré en intentar hacer el bien en el mundo.",
    cd(dict(type='quote', text='Todo lo que pase de mi primer millón lo gastaré en intentar hacer el bien en el mundo.', attrib='Charles Ponzi a The New York Times · 1920'), at='hacer el bien'))
INV("No todo el mundo se lo tragaba. Un veterano del oficio, William Miller, que en mil ochocientos noventa y nueve había estafado más de un millón de dólares en Brooklyn con un truco parecido, le dijo a un periodista de Nueva York una frase deliciosa.",
    ai('celda_lectura', 'an older man in a 1920s suit reading a newspaper by a barred window, raised eyebrow implied by posture, seen from the side in shadow', at='William Miller'))
JUE("Puede que yo sea algo torpe, pero no entiendo cómo Ponzi ha ganado tanto dinero en tan poco tiempo.",
    cd(dict(type='quote', text='Puede que yo sea algo torpe, pero no entiendo cómo Ponzi ha ganado tanto dinero en tan poco tiempo.', attrib='William «520 %» Miller, estafador, al New York Evening World · 1920'), at='Puede que'))
NAR("Cuando empezaron las dudas, cientos de clientes asustados se agolparon a la vez para pedir su dinero. Y Ponzi hizo algo genial: pagó a todos. Según las crónicas, devolvió unos dos millones de dólares en tres días. Y mientras la gente esperaba en la cola, mandó repartir café y rosquillas. Muchos, tranquilizados, volvieron a dejar su dinero.",
    ai('cafe_cola', 'a 1920s Boston street queue of men in flat caps and coats, a clerk handing out coffee cups and doughnuts, morning steam, seen from behind', at='café y rosquillas'),
    cd(dict(type='counter', to=2000000, label='dólares devueltos en tres días para calmar el pánico', prefix='$'), at='dos millones de dólares'))
DOC("[serious] Duplica el dinero en tres meses. Cincuenta por ciento de interés pagado en cuarenta y cinco días por Ponzi. Tiene miles de inversores.",
    cd(dict(type='doc', title='The Boston Post · 24 de julio de 1920', lines=['«Duplica el dinero en tres meses»', '«50 % de interés pagado en 45 días por Ponzi»', '«Tiene miles de inversores»'], source='Titular de portada · The Boston Post'), at='Duplica'))
INV("Ese titular de portada fue el principio del fin. Al Boston Post le olió raro. Encargó a expertos financieros que hicieran las cuentas, y las cuentas no salían: para cubrir lo prometido, Ponzi habría necesitado muchísimos más cupones de los que había en circulación en todo el mundo.",
    ph('Boston Post 1920 newspaper', at='Boston Post'),
    cd(dict(type='split', left=dict(title='Lo que prometía', lines=['Comprar cupones a millones', 'en toda Europa']), right=dict(title='Lo que había', lines=['Muchos menos cupones', 'en circulación en todo el mundo']), strike=True), at='las cuentas no salían'))
NAR("Y entonces llegó la traición que Ponzi no esperaba. Su propio jefe de prensa, William McMasters, el hombre que le había ayudado a fabricar su imagen, se pasó al bando contrario. A principios de agosto publicó en el Boston Post su veredicto: Ponzi estaba en quiebra sin remedio.",
    ph('newspaper city room 1920s', at='jefe de prensa'),
    K('EN QUIEBRA', 'Boston Post 1920 newspaper', at='en quiebra'))
NAR("[serious] En agosto de mil novecientos veinte, los auditores entraron en su empresa. Al final, cuando se contó todo, encontraron cupones por valor de sesenta y un dólares. Sesenta y uno. Por los millones que habían pasado por sus manos.",
    ai('auditores_libros', 'accountants in 1920s suits bent over large ledgers under green desk lamps in a dark office, seen from behind', at='los auditores'),
    cd(dict(type='counter', to=61, label='dólares en cupones encontrados por los auditores', prefix='$'), at='sesenta y un dólares'))
NAR("La noticia corrió por Boston en horas. Esta vez, la multitud que rodeó su oficina no traía dinero. Según la revista Time, gritaba otra cosa: ¡Matadlo!",
    ai('multitud_furiosa', 'an angry 1920 crowd pressing against the glass door of a Boston office, fists raised, police helmets visible, seen from inside the dark office', at='la multitud'),
    KA('¡MATADLO!', 'punos_multitud', 'raised fists and hats of an angry 1920 street crowd against a grey sky, low angle, motion blur', at='Matadlo'))
INV("Ponzi fue detenido ese mismo mes. Varios bancos cayeron con él. El Boston Post ganó el premio Pulitzer por destaparlo. Ponzi pasó más de una década entre cárceles y juicios, volvió a estafar en Florida vendiendo terrenos que eran pantano, y en mil novecientos treinta y cuatro fue deportado a Italia.",
    ph('Charles Ponzi 1920', at='fue detenido'),
    ph('Florida swamp 1920s', at='terrenos que eran pantano'))
NAR("Murió en mil novecientos cuarenta y nueve en un hospital de caridad de Río de Janeiro, casi ciego y sin dinero. [pause] Su nombre, eso sí, sigue vivo. Cada vez que un juez describe una pirámide de inversores, dice la misma palabra: Ponzi.",
    ph('Rio de Janeiro 1940s', at='Río de Janeiro'),
    K('PONZI', 'Charles Ponzi portrait', at='la misma palabra'))

# ---------------- III · EL HOMBRE QUE VENDIÓ LA TORRE EIFFEL ----------------
T('El hombre que vendió la Torre Eiffel', 'París, 1925', num='III', sting='ironia')
DOC("Expediente número tres. Sospechoso: Victor Lustig, alias el conde. Al menos veinte nombres falsos, cinco idiomas. Delito: vender un monumento nacional. Dos veces.",
    cd(dict(type='ficha', name='Victor Lustig', role='Alias «el conde» · cinco idiomas', group='Expediente III · la Torre Eiffel', color=[196, 38, 34]), at='Expediente'),
    ph('Victor Lustig mugshot', at='Sospechoso'))
B('ironia')
NAR("Hay estafas que se hacen con miles de víctimas. Y hay estafas que solo necesitan una. Pero esa víctima tiene que comprar algo muy grande.",
    ph('Eiffel Tower 1920s', at='algo muy grande'))
INV("París, mil novecientos veinticinco. La Torre Eiffel tiene treinta y seis años y no todos la quieren. Se construyó para una exposición universal y nunca se pensó que fuera eterna. Mantenerla cuesta una fortuna, y algún periódico se pregunta si no habría que desmontarla.",
    ph('Paris 1925 street', at='París', lt=['París', 'Francia · hacia 1925']),
    ph('Eiffel Tower Exposition Universelle 1889', at='una exposición universal'),
    ph('Eiffel Tower Citroen illumination 1925', at='Mantenerla'))
NAR("Victor Lustig lee esa noticia en un café. Lustig había nacido en el Imperio austrohúngaro, hablaba cinco idiomas y se hacía llamar conde. Llevaba años estafando a millonarios en los grandes transatlánticos. Y aquella noticia le pareció una invitación.",
    ph('Victor Lustig', at='Victor Lustig', lt=['Victor Lustig', 'El «conde» Lustig · 1890-1947', 'estafa']),
    ph('ocean liner 1920s', at='transatlánticos'))
INV("Encarga papel con membrete oficial del Ministerio de Correos y Telégrafos. Escribe a seis de los mayores chatarreros de París. Y los cita, con la máxima discreción, en uno de los hoteles más lujosos de la ciudad: el Hôtel de Crillon, en la plaza de la Concordia.",
    ai('membrete_carta', 'a forged official French government letter with a wax seal and a fountain pen on a hotel writing desk, 1920s, no readable text', at='papel con membrete'),
    ph('Hotel de Crillon Paris', at='Hôtel de Crillon', lt=['Hôtel de Crillon', 'Plaza de la Concordia, París · hoy']))
NAR("[softly] Allí les cuenta un secreto de Estado. El Gobierno ha decidido desmontar la torre y vender sus siete mil toneladas de hierro. Como el asunto puede escandalizar a los parisinos, se hará en silencio. Les lleva en limusina a visitarla. Y les pide ofertas en sobre cerrado.",
    ai('salon_hotel', 'six men in 1920s overcoats seated around a table in an opulent Paris hotel salon, cigar smoke, chandeliers, faces in shadow', at='un secreto de Estado'),
    cd(dict(type='counter', to=7000, label='toneladas de hierro «a la venta»'), at='siete mil toneladas'),
    ph('Eiffel Tower 1920s', at='a visitarla'))
INV("Lustig ya había elegido a su víctima: André Poisson, un empresario de provincias que soñaba con codearse con la alta sociedad de París. Poisson dudó un momento. Entonces Lustig hizo su jugada maestra.",
    ai('hombre_sombrero', 'a nervous provincial businessman in a bowler hat seen from behind, looking up at the Eiffel Tower ironwork, overcast sky', at='André Poisson'))
NAR("Le confesó, bajando la voz, que un alto funcionario cobra poco para la vida que se le exige. Y le pidió un soborno. [short pause] Poisson respiró tranquilo. Si el funcionario pedía una mordida, es que era un funcionario de verdad.",
    ai('sobre_mesa', 'a thick envelope slid across a white tablecloth between two gloved hands, 1920s restaurant, candlelight', at='le pidió un soborno'),
    K('LA MORDIDA', 'Hotel de Crillon Paris', at='una mordida'))
INV("Pagó la torre y pagó el soborno. Lustig cogió el dinero y se subió al primer tren a Viena. ¿Y Poisson? Le dio tanta vergüenza que nunca lo denunció.",
    ph('Gare de l\'Est Paris 1920s', at='primer tren a Viena'),
    ai('tren_viena', 'a 1925 steam train departing a Paris station at night, clouds of steam under the glass roof, passengers boarding, seen from behind', at='Poisson'))
NAR("Medio año después, Lustig volvió a París. Y vendió la torre otra vez, a otro grupo de chatarreros. Esta vez el elegido sí fue a la policía, y Lustig tuvo que huir a Estados Unidos. [short pause] Allí acabó metido en el negocio de los billetes falsos, y en mil novecientos treinta y cinco cayó por fin.",
    K('DOS VECES', 'Eiffel Tower 1920s', at='otra vez'),
    ai('imprenta_falsos', 'a clandestine 1930s counterfeiting workshop at night, an old printing press with sheets of freshly printed banknotes hanging to dry, a single bulb, no people', at='cayó por fin'))
INV("Ni siquiera la cárcel le detuvo del todo. En septiembre de mil novecientos treinta y cinco, esperando juicio en Nueva York, se escapó de la prisión federal descolgándose por una ventana con una cuerda de sábanas. Mientras bajaba, según se cuenta, fingía limpiar los cristales ante los curiosos. Lo atraparon unas semanas después en Pittsburgh. Terminó en Alcatraz, y murió preso en mil novecientos cuarenta y siete.",
    ai('cuerda_sabanas', 'a rope of knotted bedsheets hanging down the brick facade of a 1930s New York jail, pedestrians far below on the street, high angle', at='cuerda de sábanas'),
    KA('FUGA', 'carcel_federal', 'the stone facade of a 1930s New York federal detention building at night, barred windows, a police car outside, wet street', at='se escapó'),
    ph('Alcatraz Island', at='Alcatraz', lt=['Alcatraz', 'Bahía de San Francisco · hoy']))
NAR("[softly] Su truco más rentable, sin embargo, fue otro: la caja rumana. Una caja de madera con rodillos que, según él, imprimía billetes de cien dólares auténticos. Delante del comprador, la máquina soltaba uno, muy despacio. Lustig la vendía por miles de dólares. Cuando la caja empezaba a escupir papel en blanco, él ya estaba muy lejos.",
    ai('caja_rumana', 'a polished mahogany box with brass rollers and cranks on a hotel table, a crisp banknote slowly emerging from a slot, dramatic lamplight, close-up', at='la caja rumana'),
    KA('PAPEL EN BLANCO', 'caja_blanco', 'an open polished wooden box with brass rollers revealing only stacks of blank white paper slips inside, lamplight, close-up', at='papel en blanco'))
INV("Una advertencia de investigadora: casi todo lo que sabemos de la venta de la torre procede de los agentes que le persiguieron y de la prensa de la época. Las cifras varían según la fuente. Pero la lección es nítida: el estafador no vende un objeto. Vende la sensación de estar entre los elegidos.",
    cd(dict(type='quote', text='El estafador no vende un objeto. Vende la sensación de estar entre los elegidos.', attrib='Lección del expediente Lustig'), at='la lección'))
NAR("A Lustig se le atribuyen incluso unos mandamientos del buen estafador. Nadie sabe si los escribió él. Pero suenan exactamente a él.",
    ai('cuaderno_reglas', 'an elegant 1930s leather notebook open on a hotel desk next to a silk tie and a fountain pen, handwriting blurred and unreadable', at='mandamientos'))
LUS("[softly] Primero: sé un oyente paciente. Es eso, y no hablar deprisa, lo que le da sus golpes al estafador. Segundo: nunca parezcas aburrido. Espera a que el otro te diga sus ideas políticas, y dale la razón. Nunca presumas: deja que tu importancia se note sola. Nunca vayas desaliñado. [short pause] Y nunca te emborraches.",
    cd(dict(type='list', header='Los mandamientos del estafador', items=[('Sé un oyente paciente', 'no hables deprisa'), ('Nunca parezcas aburrido', ''), ('Dale la razón', 'en política y en religión'), ('Nunca presumas', 'que tu importancia se note sola'), ('Nunca te emborraches', '')]), at='Primero'),
    ai('gemelos_traje', 'an elegant 1930s gentleman in a tailored suit adjusting a gold cufflink in a hotel bar, face out of frame, crystal glasses, close-up on hands', at='Nunca presumas'))
INV("Y hay otra historia que se cuenta de él, quizá la más audaz. Lustig le pidió a Al Capone cincuenta mil dólares para doblarlos en dos meses. Los guardó en una caja fuerte sin tocarlos. Pasado el plazo, se los devolvió enteros, avergonzado, diciendo que el negocio había fallado. Capone, impresionado por su honradez, le regaló cinco mil dólares. [pause] Que era exactamente lo que Lustig buscaba desde el principio.",
    ph('Al Capone', at='Al Capone', lt=['Al Capone', 'Gánster de Chicago']),
    ai('caja_fuerte', 'a heavy steel safe in a dim 1920s office with its door ajar showing neat stacks of banknotes, single desk lamp', at='caja fuerte'),
    cd(dict(type='split', left=dict(title='Lo que pidió', lines=['50.000 dólares de Capone']), right=dict(title='Lo que se llevó', lines=['5.000 dólares «de regalo»', 'sin arriesgar nada']), strike=False), at='Que era exactamente'))

# ---------------- IV · EL REY DE LAS CERILLAS ----------------
T('El rey de las cerillas', 'Estocolmo, 1932', num='IV', sting='tema')
DOC("Expediente número cuatro. Sospechoso: Ivar Kreuger, ingeniero y financiero sueco. Uno de los hombres más ricos del mundo. Delito: balances falsos, bonos falsificados y una pirámide de escala mundial.",
    cd(dict(type='ficha', name='Ivar Kreuger', role='Financiero sueco · «el rey de las cerillas»', group='Expediente IV · una pirámide mundial', color=[196, 38, 34]), at='Expediente'),
    ph('Ivar Kreuger portrait', at='Sospechoso'))
B('tension')
NAR("Ahora cambiamos de escala. Porque el siguiente estafador no era un pícaro con un traje elegante. Era uno de los hombres más poderosos del planeta.",
    ph('Ivar Kreuger', at='los hombres más poderosos'))
INV("Ivar Kreuger, ingeniero sueco, nacido en Kalmar en mil ochocientos ochenta. Empezó construyendo edificios y acabó dominando un producto que había en cada casa del mundo: las cerillas. A finales de los años veinte, sus fábricas producían entre dos tercios y tres cuartas partes de todas las cerillas del planeta.",
    ph('Ivar Kreuger portrait', at='Ivar Kreuger', lt=['Ivar Kreuger', '«El rey de las cerillas» · 1880-1932', 'estafa']),
    ph('Kalmar Sweden old town', at='Kalmar'),
    ph('Swedish Match matchbox', at='las cerillas'),
    cd(dict(type='counter', to=75, label='% de las cerillas del mundo, en su punto más alto', prefix=''), at='tres cuartas partes'))
NAR("Su fórmula era audaz. Después de la Primera Guerra Mundial, muchos gobiernos estaban arruinados. Kreuger les prestaba millones. A cambio, le daban el monopolio de las cerillas en su país. Francia, Alemania, Polonia y más de una docena de países firmaron con él.",
    cd(dict(type='map', title='El imperio de las cerillas · años 20', bbox=[-10, 35, 40, 62], points=[dict(name='Estocolmo', lon=18.07, lat=59.33, big=1), dict(name='París', lon=2.35, lat=48.86), dict(name='Berlín', lon=13.40, lat=52.52), dict(name='Varsovia', lon=21.01, lat=52.23)]), at='muchos gobiernos'))
INV("Era un hombre extraño. Soltero, discreto, obsesionado con el secreto. Tenía casas en Estocolmo, París, Berlín y Nueva York, y en las reuniones casi no hablaba. Sus colaboradores sabían solo la parte del negocio que les tocaba. Nadie, salvo él, veía el cuadro completo.",
    ai('kreuger_despacho', 'a lone silhouetted financier standing at a tall window of a 1920s Stockholm office overlooking the harbour, back turned, cigar smoke', at='obsesionado con el secreto'),
    ai('telefonos_mesa', 'a 1920s executive desk with several black bakelite telephones, ledgers and a world map on the wall, dramatic lamp light', at='la parte del negocio'))
INV("Para conseguir ese dinero vendía acciones y bonos de sus empresas en Wall Street y en Europa. Pagaba dividendos altísimos, año tras año. Pero muchos de esos dividendos salían del dinero de los nuevos inversores. Es decir: una pirámide, con traje de multinacional.",
    ph('Kreuger and Toll share certificate', at='acciones y bonos'),
    K('UNA PIRÁMIDE', 'New York Stock Exchange 1920s', at='una pirámide'))
NAR("En octubre de mil novecientos veintinueve, la revista Time le dedicó su portada. Era el financiero del momento, el hombre que prestaba dinero a los países. Ese mismo mes, Wall Street se desplomó.",
    ph('Time magazine cover Ivar Kreuger 1929', at='la revista Time'),
    ph('Wall Street crash 1929', at='Wall Street se desplomó'))
NAR("[serious] Tras el crac, el dinero dejó de fluir. Kreuger necesitaba cada vez más crédito para tapar los agujeros, y empezó a falsificar balances. Incluso fabricó bonos falsos del Estado italiano para usarlos como garantía.",
    ph('Wall Street crash 1929 crowd', at='Tras el crac'),
    ai('bonos_falsos', 'a stack of ornate engraved bond certificates under a desk lamp, a magnifying glass and a rubber stamp beside them, no readable text', at='bonos falsos'))
INV("París, doce de marzo de mil novecientos treinta y dos. Kreuger tenía una reunión con sus banqueros. No se presentó. Lo encontraron en la cama de su apartamento con un disparo en el pecho y una pistola al lado. [short pause] Hay quien todavía hoy sostiene que lo asesinaron. La versión oficial fue el suicidio.",
    ai('dormitorio_paris', 'an elegant 1930s Paris apartment bedroom in morning light through tall shutters, an empty unmade bed, a revolver silhouette on the nightstand, no person visible', at='No se presentó'))
NAR("Acababa de volver de Estados Unidos en barco, agotado. En el Hotel du Rhin le esperaban banqueros británicos y suecos para una reunión decisiva. Según la revista Time, aquella misma mañana todo París desfilaba ante el féretro de un ministro ilustre, Aristide Briand. Al día siguiente, los titulares ya no hablaban de Briand. Hablaban de él.",
    ai('vestibulo_hotel', 'bankers in 1930s overcoats waiting in an elegant Paris hotel lobby, pocket watches, cigarette smoke, nobody facing camera', at='Hotel du Rhin'),
    ai('quiosco_prensa', 'a 1932 Paris newspaper kiosk on a rainy boulevard with stacks of newspapers and blurred headlines, passersby with umbrellas, no readable text', at='los titulares'))
DOC("El rey de las cerillas, muerto en París. Lo encontraron con un revólver al lado. Curiosamente, no llevaba cerillas encima.",
    cd(dict(type='doc', title='Prensa internacional · 14 de marzo de 1932', lines=['«El rey mundial de las cerillas, muerto en un piso de París»', '«Encontrado con un revólver a su lado»', '«Curiosamente, no llevaba cerillas encima»'], source='Crónicas de agencia publicadas en la prensa de la época'), at='El rey de las cerillas'))
NAR("Once días después, los auditores de Price Waterhouse abrieron sus libros. En pocas semanas lo declararon un estafador. Según la revista Time, había desviado más de mil cien millones de dólares de la época. La bolsa de Estocolmo tuvo que cerrar. Cayó el Gobierno sueco. Y miles de pequeños ahorradores, de Suecia a Estados Unidos, lo perdieron todo.",
    cd(dict(type='counter', to=1168, label='millones de dólares de 1932 desviados, según la revista Time', prefix='$'), at='mil cien millones'),
    ph('Stockholm Stock Exchange building', at='La bolsa de Estocolmo', lt=['La Bolsa de Estocolmo', 'Suecia']),
    ai('ahorradores_banco', 'a crowd of worried small savers in 1932 coats and hats in front of closed bank doors in the snow, seen from behind', at='lo perdieron todo'))
DOC("Uno de los asuntos más feos de la historia de los negocios. Kreuger había sido el mayor estafador del mundo.",
    cd(dict(type='doc', title='Revista Time · 1932', lines=['«Uno de los asuntos más feos de la historia de los negocios»', '«El mayor estafador del mundo»'], source='Así resumió la prensa estadounidense el caso Kreuger'), at='Uno de los asuntos'))
INV("Su caída pesó en la gran reforma financiera de Estados Unidos. En mil novecientos treinta y cuatro nació la SEC, la Comisión de Bolsa y Valores, el organismo que debía vigilar a los mercados para que algo así no volviera a pasar. [pause] Recuerda ese nombre. Volverá a salir.",
    ph('Securities and Exchange Commission headquarters Washington', at='la SEC', lt=['La SEC', 'Comisión de Bolsa y Valores de EE. UU.']),
    K('LA SEC', 'Securities and Exchange Commission seal', at='Recuerda ese nombre'))
INV("[pause] Expediente cuatro, caso cerrado.",
    K('CASO CERRADO', 'Ivar Kreuger', at='caso cerrado'))

# ---------------- RECAPITULACIÓN ----------------
M('fondo', 6)
NAR("Hasta aquí, más de un siglo de engaños y una misma receta.",
    cd(dict(type='recap', title='Hasta aquí', items=[('Poyais · 1822', 'un país inventado y una historia irresistible'), ('Ponzi · 1920', 'pagar a los viejos con el dinero de los nuevos'), ('Lustig · 1925', 'la víctima quiere sentirse elegida'), ('Kreuger · 1932', 'la pirámide con traje de multinacional')]), at='Hasta aquí'))
INV("Ahora vamos a mirar más cerca. Primero, aquí, en España. Y después, al hombre que lo hizo todo a la vez, durante décadas, delante de las narices de todos.",
    ph('Spain flag Madrid', at='en España'))
