# -*- coding: utf-8 -*-
# «Las estafas más grandes de la historia» · parte 3: España, Madoff y cierre
from lib import *

# ---------------- V · LOS SELLOS QUE NO VALÍAN NADA ----------------
T('Los sellos que no valían nada', 'España, 2006', num='V', sting='drama')
DOC("Expediente número cinco. Sospechosos: los directivos de Fórum Filatélico y de Afinsa. Delito: estafa piramidal disfrazada de inversión en sellos. Víctimas: unos cuatrocientos sesenta mil clientes en toda España.",
    cd(dict(type='ficha', name='Fórum y Afinsa', role='Las dos mayores filatélicas de España', group='Expediente V · inversión en sellos', color=[196, 38, 34]), at='Expediente'),
    ai('hoja_sellos', 'a full sheet of colourful vintage postage stamps with ornate borders, generic landscapes and flowers, close-up, soft lamplight, no portraits', at='Sospechoso'))
B('drama')
NAR("España también tiene su propia galería de estafas. En junio de dos mil uno, la Comisión Nacional del Mercado de Valores intervino una agencia de valores de Madrid llamada Gescartera. Faltaban cerca de noventa millones de euros de sus clientes, entre ellos instituciones como el arzobispado de Valladolid. Su dueño, Antonio Camacho, fue condenado a once años de cárcel.",
    ph('CNMV sede Madrid', at='la Comisión Nacional del Mercado de Valores', lt=['CNMV', 'Comisión Nacional del Mercado de Valores · Madrid']),
    cd(dict(type='counter', to=88, label='millones de euros desaparecidos en Gescartera (2001)'), at='noventa millones'),
    ph('Audiencia Nacional Madrid', at='condenado a once años'))
INV("Pero lo de Gescartera, con ser grave, fue solo un aviso. Cinco años después estalló algo mucho más grande. Algo que no afectaba a grandes inversores, sino a la gente normal. A tus vecinos. Quizá a tus abuelos.",
    ai('abuelos_cocina', 'an elderly couple\'s hands holding a folder of contracts at a kitchen table in a Spanish apartment, a coffee cup, soft window light, faces not visible', at='a tus abuelos'))
NAR("[serious] Madrid, nueve de mayo de dos mil seis. Todavía no son las nueve de la mañana. La policía entra a la vez en las sedes de las dos mayores empresas filatélicas del país: Fórum Filatélico y Afinsa. Detienen a sus principales directivos. Precintan las oficinas. Bloquean las cuentas.",
    ai('policia_amanecer', 'Spanish police officers seen from behind entering a modern office building lobby at dawn, blue light reflections on glass, 2006', at='La policía entra'),
    cd(dict(type='split', left=dict(title='Fórum Filatélico', lines=['Sociedad filatélica', 'Inversión en sellos · Madrid']), right=dict(title='Afinsa', lines=['Afinsa Bienes Tangibles', 'Inversión en sellos · Madrid']), strike=False), at='Fórum Filatélico'))
INV("La operación la dirigía la Audiencia Nacional, a partir de una investigación de la Agencia Tributaria y de una querella de la Fiscalía Anticorrupción. Y la cifra de afectados dejó al país sin aliento: unos cuatrocientos sesenta mil clientes, con casi seis mil doscientos millones de euros invertidos.",
    ph('Audiencia Nacional Madrid', at='la Audiencia Nacional', lt=['Audiencia Nacional', 'Madrid']),
    cd(dict(type='counter', to=460000, label='clientes de Fórum Filatélico y Afinsa'), at='cuatrocientos sesenta mil'),
    cd(dict(type='counter', to=6200, label='millones de euros invertidos, según la Agencia EFE'), at='seis mil doscientos millones'))
NAR("¿Cómo se llega ahí? Con una idea que sonaba a sentido común. Durante unos veinticinco años, Fórum y Afinsa vendieron lotes de sellos como inversión. El argumento era sencillo: un sello antiguo vale más cada año que pasa. Tú comprabas el lote, la empresa lo guardaba, y al cabo del plazo te lo recompraba con una rentabilidad fija, más alta que la de un depósito del banco.",
    ai('archivo_sellos', 'stacks of investment folders and plastic sleeves filled with sheets of vintage postage stamps on shelves in a 2000s office archive, fluorescent light, no people', at='lotes de sellos'),
    ai('lupa_sellos', 'a magnifying glass over a page of an old stamp album with rows of colourful vintage postage stamps, desk lamp, close-up, no readable text', at='un sello antiguo'),
    cd(dict(type='list', header='El contrato filatélico', items=[('Compras un lote de sellos', 'la empresa los guarda por ti'), ('Pasa el plazo pactado', 'el sello «se revaloriza»'), ('Te lo recompran', 'con una rentabilidad fija')]), at='Tú comprabas'))
INV("El problema es que el precio de esos sellos lo fijaban ellos mismos. La investigación concluyó que muchos se habían comprado baratos y se valoraban entre cinco y diez veces más tras pasar por sociedades en el extranjero. Afinsa llegó a guardar ciento cincuenta millones de sellos en sus almacenes. Fuera de ese circuito, valían muy poco.",
    cd(dict(type='split', left=dict(title='Precio en el contrato', lines=['Fijado por la propia empresa', 'Sube cada año']), right=dict(title='Precio real de mercado', lines=['Entre cinco y diez veces menos', 'según la investigación']), strike=True), at='lo fijaban ellos mismos'),
    cd(dict(type='counter', to=150000000, label='sellos en los almacenes de Afinsa'), at='ciento cincuenta millones'))
DOC("Fórum Filatélico había construido un mercado cerrado, ajeno al del coleccionismo de sellos. Solo podía mantener su actividad reteniendo a sus inversores y captando otros nuevos. Es el paradigma de las estafas piramidales.",
    cd(dict(type='doc', title='Sentencia de la Audiencia Nacional · julio de 2018', lines=['«Un mercado cerrado, ajeno al del coleccionismo»', '«Captando nuevos inversores»', '«El paradigma de las estafas piramidales»'], source='Audiencia Nacional, Sala de lo Penal · caso Fórum Filatélico'), at='mercado cerrado'))
DOC("Fórum Filatélico ofrecía al público la venta de lotes de sellos, asegurándole que, transcurrido el plazo fijado en el contrato, se encargaría de venderlos en el mercado a un precio superior.",
    cd(dict(type='doc', title='Tribunal Supremo · sentencia del caso Fórum', lines=['«Ofrecía al público la venta de lotes de sellos»', '«Se encargaría de venderlos en el mercado a un precio superior»'], source='Sala Segunda del Tribunal Supremo · confirma la estafa piramidal'), at='ofrecía al público'))
NAR("Es decir: Ponzi, ochenta años después, con sellos españoles. Y muchos de sus clientes no eran especuladores. Eran jubilados, autónomos, familias. Muchos habían metido más de cincuenta mil euros, los ahorros de toda una vida, porque los sellos parecían algo sólido. Algo que se podía tocar.",
    KA('PONZI CON SELLOS', 'jubilados_sello', 'elderly retired couple hands holding a single vintage postage stamp in a plastic sleeve at a kitchen table, window light', at='Ponzi, ochenta años después'),
    ai('manos_sello', 'an old person\'s hands holding a single postage stamp with tweezers under a desk lamp, shallow depth of field', at='Algo que se podía tocar'))
INV("Los juicios tardaron más de una década. En dos mil dieciséis, once directivos de Afinsa fueron condenados a penas de hasta doce años. En dos mil dieciocho llegó la sentencia de Fórum: doce años y cuatro meses para su expresidente, Francisco Briones, que el Tribunal Supremo rebajó después a once años y diez meses.",
    cd(dict(type='timeline', header='El caso Fórum-Afinsa', events=[['2006', 'Intervención judicial'], ['2016', 'Condenados 11 directivos de Afinsa'], ['2018', 'Sentencia de Fórum'], ['Después', 'El Supremo confirma la estafa']]), at='Los juicios'),
    ai('sala_vistas', 'a modern Spanish courtroom with wooden benches full of elderly spectators seen from behind, judges\' bench in the distance, cold light', at='doce años y cuatro meses'))
NAR("Mientras tanto, los afectados se organizaron. Se manifestaron en Madrid y en decenas de ciudades, año tras año, cada nueve de mayo. Reclamaron al Estado que respondiera por no haber vigilado a tiempo. En dos mil diez, el Tribunal Supremo le eximió de pagar: no había, dijo, responsabilidad patrimonial.",
    ai('manifestacion', 'a crowd of elderly protesters holding blank placards and umbrellas in a Madrid street in the rain, seen from behind, 2008', at='Se manifestaron'),
    ph('Tribunal Supremo Madrid', at='el Tribunal Supremo', lt=['Tribunal Supremo', 'Madrid']))
JUE("Ha sido el mayor fraude de la historia de España.",
    cd(dict(type='quote', text='El mayor fraude de la historia de España.', attrib='El fiscal del caso Fórum Filatélico, según la prensa'), at='el mayor fraude'))
JUE("Un hecho insólito, incapaz de repetirse.",
    cd(dict(type='quote', text='Un hecho insólito, incapaz de repetirse.', attrib='El fiscal del caso Fórum Filatélico, según la prensa'), at='Un hecho insólito'))
NAR("[softly] Según las asociaciones de afectados, los clientes de Fórum han recuperado en torno a una quinta parte de lo invertido. Los de Afinsa, alrededor de un diez por ciento. Miles de ellos murieron esperando que acabaran los juicios.",
    cd(dict(type='split', left=dict(title='Fórum Filatélico', lines=['En torno al 20 % recuperado']), right=dict(title='Afinsa', lines=['Alrededor del 10 % recuperado']), strike=False), at='una quinta parte'),
    ai('carta_banco', 'a stack of unopened official letters on a hallway table in an empty Spanish apartment, late afternoon light, dust in the air', at='murieron esperando'))
INV("[pause] Expediente cinco, caso cerrado. Pero la herida no se ha cerrado. Cada nueve de mayo, todavía hoy, hay quien vuelve a recordar aquella mañana de dos mil seis.",
    KA('CASO CERRADO', 'expedientes_juzgado', 'stacks of thick court case files tied with red string on shelves in a Spanish courthouse archive, fluorescent light, dust, no people', at='caso cerrado'))
INV("Y aquí aparece la pregunta que se repite en todos los expedientes. Si tantos lo sabían, si había inspecciones, si había avisos, ¿por qué nadie lo paró antes? [pause] Para responderla, hay que volver al principio. A Nueva York.",
    ph('Lipstick Building New York', at='A Nueva York'))

# ---------------- VI · LA GRAN MENTIRA ----------------
T('La gran mentira', 'Nueva York, 2008', num='VI', sting='tema')
DOC("Expediente número seis. Sospechoso: Bernard Lawrence Madoff, expresidente del Nasdaq. Delito: la mayor estafa piramidal conocida. Duración: décadas. Víctimas: miles, en todo el mundo.",
    cd(dict(type='ficha', name='Bernard Madoff', role='Financiero · expresidente del Nasdaq', group='Expediente VI · la mayor de la historia', color=[196, 38, 34]), at='Expediente'),
    ph('Bernard Madoff mugshot 2009', at='Sospechoso'))
B('tension')
NAR("Bernard Madoff nació en Queens, en Nueva York, en mil novecientos treinta y ocho. En mil novecientos sesenta fundó su propia firma con unos cinco mil dólares que, según contaba, había ahorrado como socorrista y montando aspersores. Y durante décadas fue un pionero de verdad: su empresa ayudó a llevar la compraventa de acciones a la era de los ordenadores.",
    ai('queens_1940', 'a modest working-class street in Queens, New York in the 1940s, brick row houses, a corner shop, a boy with a bicycle seen from behind, autumn afternoon', at='Queens'),
    ph('Bernard Madoff', at='fundó su propia firma'),
    ai('pantallas_bolsa', 'a 1990s trading room with rows of glowing CRT monitors showing blurred green and red figures, empty chairs at night, no readable text', at='la era de los ordenadores'))
INV("Tenía dos negocios. Uno, legal y muy respetado: comprar y vender acciones para otros intermediarios. Lo dirigían sus hijos y su hermano. El otro, en otra planta del mismo edificio, gestionaba el dinero de inversores privados. Ahí no entraba casi nadie.",
    cd(dict(type='split', left=dict(title='Planta de arriba', lines=['Negocio legal', 'compraventa de acciones', 'Hijos y hermano']), right=dict(title='Otra planta', lines=['Gestión de fortunas', 'Muy pocos empleados', 'Nadie preguntaba']), strike=False), at='Tenía dos negocios'),
    ph('Lipstick Building 885 Third Avenue', at='del mismo edificio'))
NAR("Ese segundo negocio ofrecía algo que parecía mágico. No unos beneficios espectaculares, sino constantes. En torno a un diez por ciento al año, con muy pocos meses en negativo, fuera cual fuera la situación de la bolsa. [short pause] Ni Ponzi se había atrevido a tanta calma.",
    cd(dict(type='split', left=dict(title='La bolsa real', lines=['Años de subidas', 'y años de desplomes']), right=dict(title='Madoff, sobre el papel', lines=['En torno al 10 % al año', 'Casi nunca un mes en negativo']), strike=False), at='algo que parecía mágico'))
INV("Él lo llamaba su estrategia de conversión con opciones. Decía que compraba acciones de grandes empresas y se protegía con contratos que limitaban las pérdidas. Sonaba sofisticado. Sonaba imposible de comprobar para un cliente normal. Y precisamente por eso, casi nadie preguntaba.",
    cd(dict(type='split', left=dict(title='Lo que decía hacer', lines=['Comprar acciones de grandes empresas', 'Protegerse con opciones']), right=dict(title='Lo que hacía', lines=['Nada', 'Pagar con el dinero de los nuevos']), strike=True), at='Él lo llamaba'))
INV("Y Madoff no perseguía a los clientes. Los rechazaba. Hacía sentir que entrar en su fondo era un privilegio. Le llegaban por recomendación: clubs de campo, fundaciones benéficas, grandes fondos de inversión que le pasaban el dinero de sus propios clientes. También desde España, a través del fondo Optimal, del Banco Santander.",
    ai('club_campo', 'a private country club lounge with leather armchairs and whisky glasses, men in suits talking quietly, faces in shadow, warm evening light', at='clubs de campo'),
    ai('club_privado', 'a discreet private banking office with a single armchair facing a desk, Madrid skyline at dusk through the window, no people', at='desde España'))
NAR("Un analista que le investigó durante años lo explicaría después ante el Congreso: el mayor talento de Madoff era hacerse el difícil. Ofrecer la falsa seguridad de lo exclusivo. Porque cuando alguien te dice que no puedes entrar, de repente es lo único que quieres.",
    ai('cuerda_terciopelo', 'a velvet rope barrier in front of a closed mahogany door in a luxury building lobby, a doorman\'s gloved hand raised, warm light', at='hacerse el difícil'))
NAR("Pero hubo alguien que hizo las cuentas. Harry Markopolos, un analista de Boston, recibió el encargo de copiar la estrategia de Madoff. Lo intentó. Y llegó a la conclusión de que era matemáticamente imposible. Solo había dos explicaciones: o Madoff usaba información privilegiada, o era un fraude.",
    ph('Harry Markopolos', at='Harry Markopolos', lt=['Harry Markopolos', 'Analista financiero · Boston', 'autoridades']),
    K('IMPOSIBLE', 'Boston Financial District skyline', at='matemáticamente imposible'))
INV("En el año dos mil lo denunció ante la SEC. Sí, la misma SEC que nació tras la caída del rey de las cerillas. No le hicieron caso. Insistió. Y en dos mil cinco envió un informe con veintinueve señales de alarma y un título que no dejaba lugar a dudas.",
    ph('Securities and Exchange Commission headquarters Washington', at='la SEC'))
DOC("El mayor fondo de inversión del mundo es un fraude.",
    cd(dict(type='doc', title='Informe de Harry Markopolos a la SEC · 2005', lines=['«El mayor fondo de inversión del mundo es un fraude»', 'Decenas de señales de alarma, una por una'], source='The World\'s Largest Hedge Fund is a Fraud · noviembre de 2005'), at='El mayor fondo'))
NAR("La SEC examinó a Madoff varias veces y no encontró nada. Un informe interno del propio organismo reconoció después sus errores: nunca comprobaron con terceros si las operaciones que Madoff decía hacer existían de verdad. [pause] No existían.",
    K('NO EXISTÍAN', 'Securities and Exchange Commission seal', at='No existían'))
INV("Markopolos llegó a temer por su vida y por la de su familia, convencido de que se estaba enfrentando a gente muy poderosa. Y cuando por fin todo estalló, en febrero de dos mil nueve, le dejaron hablar ante el Congreso de Estados Unidos.",
    ai('ventana_noche', 'a man\'s silhouette looking through the blinds of a suburban house window at night, a car\'s headlights outside, tension', at='temer por su vida'),
    ph('United States Capitol', at='el Congreso de Estados Unidos', lt=['Congreso de EE. UU.', 'Washington · 4 de febrero de 2009']))
MKP("[serious] Les entregué en bandeja, envuelta para regalo, la mayor estafa piramidal de la historia. Y, de algún modo, no se molestaron en hacer una investigación a fondo, como es debido, porque estaban demasiado ocupados con asuntos más prioritarios.",
    cd(dict(type='quote', text='Les entregué en bandeja, envuelta para regalo, la mayor estafa piramidal de la historia.', attrib='Harry Markopolos ante el Congreso de EE. UU. · 4 de febrero de 2009'), at='Les entregué'))
MKP("Si una estafa piramidal de cincuenta mil millones de dólares no entra en la lista de prioridades de la SEC, entonces quiero saber quién fija sus prioridades.",
    ai('analista_graficos', 'a financial analyst desk at night in a Boston office, printed performance charts covered in red circles, a calculator and coffee, a man silhouette leaning over them, face hidden', at='quiero saber'))
INV("Durante años, Madoff pagó a los que pedían su dinero con el dinero de los que llegaban. Exactamente lo que hizo Ponzi. Solo que durante mucho más tiempo, y con extractos impecables que se fabricaban en esa otra planta de la oficina.",
    ai('extractos_imprenta', 'stacks of printed financial account statements coming out of an old dot-matrix printer in a dim back office at night, no readable text', at='extractos impecables'))
NAR("Según se supo en los juicios a sus colaboradores, en aquella planta se usaban ordenadores antiguos para imprimir confirmaciones de operaciones que nunca se habían hecho. Se elegían las cotizaciones del pasado que mejor cuadraban, y se inventaban las compras y las ventas a posteriori. Rentabilidades perfectas, fabricadas hacia atrás.",
    ai('ordenador_antiguo', 'an old beige office computer terminal with a green-text screen glowing in a dark back office at night, stacks of paper beside it, no readable text', at='ordenadores antiguos'),
    KA('HACIA ATRÁS', 'sello_fechas', 'a hand pressing an old rubber date stamp onto a printed account statement, a pile of statements beside it, desk lamp, close-up, no readable text', at='fabricadas hacia atrás'))
NAR("[serious] Hasta que llegó el otoño de dos mil ocho. Quiebra Lehman Brothers. Los mercados se desploman. Y los clientes de Madoff, asustados, piden su dinero a la vez. Unos siete mil millones de dólares. Ese dinero no estaba.",
    ph('Lehman Brothers headquarters 2008', at='Lehman Brothers'),
    ph('New York Stock Exchange 2008', at='Los mercados se desploman'),
    cd(dict(type='counter', to=7000, label='millones de dólares que pidieron los clientes en 2008', prefix='$'), at='siete mil millones'))
INV("El diez de diciembre confesó a sus hijos. Ellos acudieron a sus abogados, y los abogados a las autoridades. A la mañana siguiente, los agentes del FBI se presentaron en su ático del Upper East Side. Según la agencia AP, les abrió un hombre derrotado, en albornoz, que sabía que se había acabado.",
    ph('Upper East Side Manhattan', at='Upper East Side', lt=['Upper East Side', 'Manhattan, Nueva York']),
    ai('albornoz_puerta', 'an apartment door half open in a luxury Manhattan building hallway at dawn, a silhouette in a bathrobe inside, seen from behind the visitors', at='en albornoz'))
INV("Ese mismo día, la directora de Ejecución de la SEC lo resumió así: un fraude masivo, tanto por su alcance como por su duración.",
    cd(dict(type='quote', text='Un fraude masivo, tanto por su alcance como por su duración.', attrib='Linda Chatman Thomsen, directora de Ejecución de la SEC · 11 de diciembre de 2008'), at='un fraude masivo'))
INV("El fraude cruzó el Atlántico. Cuando estalló, el Santander reconoció que sus clientes tenían dos mil trescientos treinta millones de euros expuestos a Madoff. Semanas después, el banco ofreció compensar a sus clientes particulares. Y al otro lado del océano, en México, Chile o Argentina, miles de ahorradores descubrieron que su dinero había acabado en el mismo agujero.",
    cd(dict(type='counter', to=2330, label='millones de euros de clientes del Santander expuestos a Madoff (2008)'), at='el Santander'),
    ai('ahorradores_latam', 'a bank branch waiting area in Latin America in 2008, worried customers seated with folders on their laps, seen from behind, fluorescent light', at='miles de ahorradores'))
NAR("Entre las víctimas había grandes fortunas, pero también fundaciones benéficas, fondos de pensiones y jubilados. La fundación del premio Nobel de la Paz Elie Wiesel, superviviente del Holocausto, perdió casi todo su patrimonio en el fondo de Madoff.",
    ph('Elie Wiesel', at='Elie Wiesel', lt=['Elie Wiesel', 'Premio Nobel de la Paz 1986', 'victimas']),
    ai('fundacion_vacia', 'an empty charity foundation office with framed photographs on the wall and cardboard boxes packed on the floor, late afternoon light', at='perdió casi todo'))
NAR("Tres meses después, el doce de marzo de dos mil nueve, Madoff se declaró culpable de once delitos. Leyó una declaración ante el juez.",
    ph('Daniel Patrick Moynihan United States Courthouse', at='se declaró culpable', lt=['Tribunal federal', 'Manhattan · 12 de marzo de 2009']),
    cd(dict(type='counter', to=11, label='delitos de los que se declaró culpable'), at='once delitos'))
MAD("Señoría, durante muchos años, hasta mi detención el once de diciembre de dos mil ocho, dirigí un esquema Ponzi a través del negocio de asesoría de inversiones de mi firma. No puedo expresar adecuadamente cuánto siento lo que he hecho.",
    ai('sala_federal', 'a federal courtroom in Manhattan seen from the back rows, a grey-haired man in a dark suit standing at the defence table, wood panelling, cold light', at='Señoría'),
    cd(dict(type='doc', title='Declaración de culpabilidad · 12 de marzo de 2009', lines=['«Dirigí un esquema Ponzi»', '«No puedo expresar adecuadamente cuánto siento lo que he hecho»'], source='Tribunal federal del distrito sur de Nueva York'), at='cuánto siento'))
MAD("[serious] Cuando empecé el esquema Ponzi, creí que terminaría pronto y que podría sacarnos de él, a mí y a mis clientes. Pero resultó difícil, y al final imposible. Y con los años me di cuenta de que mi detención y este día llegarían inevitablemente.",
    cd(dict(type='quote', text='Con los años me di cuenta de que mi detención y este día llegarían inevitablemente.', attrib='Bernard Madoff ante el juez · 12 de marzo de 2009'), at='Cuando empecé'))
NAR("El día de la sentencia, nueve víctimas hablaron en la sala. Ninguno de sus amigos ni de su familia había enviado una sola carta en su defensa. Madoff se giró hacia ellas.",
    ai('victimas_sala', 'rows of courtroom spectators seen from behind, an older woman standing to speak at a lectern, tissues in hand, solemn light', at='nueve víctimas'))
MAD("[softly] Vivo en un estado de tormento, sabiendo todo el dolor y el sufrimiento que he causado.",
    cd(dict(type='quote', text='Vivo en un estado de tormento, sabiendo todo el dolor y el sufrimiento que he causado.', attrib='Bernard Madoff ante el tribunal · 29 de junio de 2009'), at='Vivo en un estado'))
INV("El veintinueve de junio de dos mil nueve llegó la sentencia. Ciento cincuenta años de prisión, la pena máxima posible para un hombre de setenta y un años. El juez Denny Chin sabía que era simbólico. Y lo explicó así.",
    cd(dict(type='counter', to=150, label='años de prisión · 29 de junio de 2009'), at='Ciento cincuenta años'))
JUE("[serious] El simbolismo es importante. Hay que enviar el mensaje de que los delitos del señor Madoff fueron extraordinariamente malvados. Y de que este tipo de manipulación del sistema no es un delito incruento que ocurre sobre el papel, sino uno que causa un daño humano enorme.",
    cd(dict(type='quote', text='Los delitos del señor Madoff fueron extraordinariamente malvados.', attrib='El juez Denny Chin al dictar sentencia · 29 de junio de 2009'), at='El simbolismo'),
    ai('mazo_sombra', 'the shadow of a judge raising a gavel cast on a wood-panelled courtroom wall, dramatic low light', at='daño humano enorme'))
NAR("Las cuentas de sus clientes sumaban, sobre el papel, unos sesenta y cinco mil millones de dólares. El dinero que de verdad le habían entregado rondaba los dieciocho mil millones. El resto eran beneficios que nunca existieron. [pause] Madoff murió en una prisión de Carolina del Norte en abril de dos mil veintiuno. Tenía ochenta y dos años.",
    cd(dict(type='split', left=dict(title='Sobre el papel', lines=['Unos 65.000 millones de dólares']), right=dict(title='Dinero real entregado', lines=['Unos 18.000 millones', 'según el administrador judicial']), strike=False), at='sobre el papel'),
    ph('Butner Federal Correctional Complex', at='una prisión de Carolina del Norte'))
INV("Desde entonces, el administrador judicial del caso, Irving Picard, ha pasado años persiguiendo el dinero: demandando a bancos, fondos y a clientes que habían cobrado beneficios ficticios. Ha logrado recuperar una parte muy importante del dinero aportado. Pero nada devuelve los años de angustia de quienes lo perdieron todo.",
    ai('archivo_cajas', 'endless rows of archive boxes on metal shelves in a dim legal records room, a single lawyer silhouette walking between them', at='persiguiendo el dinero'))

# ---------------- CIERRE ----------------
T('El mismo truco', 'Doscientos años de estafas', secs=4.5, sting='tema')
B('fondo')
NAR("Un país inventado. Unos cupones de correos. Una torre. Unas cerillas. Unos sellos. Un fondo de inversión. Seis disfraces distintos. Y por debajo, el mismo truco.",
    cd(dict(type='board', title='Seis expedientes, un mismo truco', nodes=[['Poyais', 'MacGregor · 1822'], ['Cupones', 'Ponzi · 1920'], ['Torre Eiffel', 'Lustig · 1925'], ['Cerillas', 'Kreuger · 1932'], ['Sellos', 'Fórum y Afinsa · 2006'], ['Fondo', 'Madoff · 2008']], links=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 5], [1, 4]]), at='Un país inventado'))
INV("Si repasas los expedientes, las señales se repiten. Una rentabilidad alta y, sobre todo, demasiado regular. Un negocio que nadie sabe explicar del todo. La sensación de estar entre unos pocos elegidos. Los primeros que cobran y te lo cuentan. Y alguien, casi siempre, que avisó y no fue escuchado.",
    cd(dict(type='recap', title='Las señales que se repiten', items=[('Rentabilidad demasiado regular', 'alta y sin sobresaltos'), ('Nadie sabe explicarlo', 'el negocio es un misterio'), ('Exclusividad', 'te hacen sentir elegido'), ('Los primeros cobran', 'y traen a los demás'), ('Avisos ignorados', 'alguien lo vio antes')]), at='las señales se repiten'))
NAR("[softly] Ninguna de estas estafas se apoyó solo en la codicia. Se apoyó en algo mucho más humano: la confianza. En un militar con medallas, en un vecino que cobraba puntual, en un banco de prestigio, en unos sellos que se podían tocar.",
    ai('apreton_manos', 'a firm handshake between two men in suits over a desk, warm lamplight, extreme close-up, shallow depth of field', at='la confianza'))
INV("Y fíjate en algo. Los estafados no eran tontos. Había banqueros, abogados, médicos, grandes fondos de inversión, gobiernos enteros. Lo que tenían en común no era la ignorancia. Era que todos querían creer que esta vez sí, que esta vez habían encontrado la excepción.",
    ai('espejo_traje', 'a well-dressed professional adjusting his tie in a mirror in a marble bathroom, reflection only partly visible, cold light', at='no eran tontos'))
INV("Por eso la próxima gran estafa no se parecerá a ninguna de estas. Llegará con otro disfraz, con otra tecnología, con otra palabra de moda. [pause] Pero hará la misma promesa.",
    ai('pantalla_movil', 'a smartphone glowing on a dark table at night, its screen showing an upward green chart line with no numbers or text, reflections', at='otro disfraz'))
NAR("Hoy, la Comisión Nacional del Mercado de Valores publica cada semana advertencias sobre empresas que ofrecen invertir sin estar autorizadas. Los llaman chiringuitos financieros. Cambian de nombre, de web y de producto: criptomonedas, divisas, inmuebles, inteligencia artificial. El guion, en cambio, apenas cambia.",
    ph('CNMV sede Madrid', at='Comisión Nacional del Mercado de Valores'),
    K('CHIRINGUITOS', 'CNMV sede Madrid', at='chiringuitos financieros'),
    ai('anuncio_movil', 'a person on a night train scrolling a smartphone showing a flashy investment advert with a rising chart, screen glow on hands, no readable text', at='criptomonedas'))
NAR("[dramatically] Y alguien, en algún lugar, volverá a decir esa misma frase. [pause] Todo es una gran mentira.",
    K('TODO ES UNA GRAN MENTIRA', 'Lipstick Building New York', at='Todo es una gran mentira'))
INV("Y ahora, te toca a ti. ¿Cuál de estos seis expedientes te ha parecido más increíble? Te leemos en los comentarios.",
    cd(dict(type='board', title='¿Cuál es el más increíble?', nodes=[['Poyais', '1822'], ['Ponzi', '1920'], ['Torre Eiffel', '1925'], ['Kreuger', '1932'], ['Fórum y Afinsa', '2006'], ['Madoff', '2008']], links=[]), at='te toca a ti'))
