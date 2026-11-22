# -*- coding: utf-8 -*-
# «Bankia» · parte 2: la campana, el castillo de naipes y la semana que cayó Rato
from lib import *

# ---------------- III · LA CAMPANA ----------------
T('La campana', 'Junio y julio de 2011', num='III', secs=4.5, sting='tema')
B('fiesta')
NEW("Junio de dos mil once. Bankia lanza una de las mayores campañas publicitarias que ha visto la banca española. Anuncios en televisión, en la radio, en las marquesinas. El mensaje invita a hacerse accionista. A ser, como decían los propios anuncios, bankero.",
    ai('marquesina', 'a glowing advertising billboard at a bus stop on a busy Madrid avenue at night, pedestrians walking past with umbrellas, the billboard showing only an abstract emerald green glow, no text', at='en las marquesinas'),
    ai('tele_salon', 'an elderly couple watching television in a modest Spanish living room at night, the green light of the screen on their faces seen from behind the sofa, cozy and trusting', at='Anuncios en televisión'),
    KA('«BANKEROS»', 'cartel_gigante', 'a huge advertising banner unfurling down the facade of a glass office tower in Madrid at sunset, workers on a platform, abstract green design, no text', at='bankero'))
NAR("Pero la campaña más eficaz no estaba en la televisión. Estaba en las miles de oficinas del grupo. Allí, empleados que conocían a sus clientes de toda la vida les ofrecían las acciones. Jubilados, familias, pequeños ahorradores que nunca habían comprado una acción en su vida.",
    ai('oficina_mesa', 'a bank employee across a desk sliding a brochure toward an elderly woman with a handbag on her lap in a small Spanish bank branch, warm light, trust, seen from the side with faces turned away', at='les ofrecían las acciones'),
    ai('jubilado_firma', 'the wrinkled hands of an elderly man signing a form with a cheap ballpoint pen at a bank counter, his reading glasses beside the paper, close-up, golden light', at='Jubilados, familias'),
    ai('pareja_joven', 'a young couple sitting at a bank branch desk holding hands, seen from behind, an employee pointing at a screen, afternoon sun through blinds', at='pequeños ahorradores'))
DAT("Mientras tanto, los grandes inversores internacionales no se fían. La demanda no llega. Y el diecinueve de julio, la víspera del estreno, Bankia tiene que rebajar el precio. La horquilla inicial iba de cuatro con cuarenta y uno a cinco con cero cinco euros por acción. El precio final se queda en tres con setenta y cinco.",
    ai('traders_dudan', 'foreign fund managers in a glass office in London at night looking at screens and shaking their heads, seen from behind, cold blue light, rain on the windows', at='los grandes inversores internacionales no se fían'),
    cd(dict(type='split', left=dict(title='Horquilla inicial', lines=['4,41 € — 5,05 €', 'por acción']), right=dict(title='Precio final · 19 de julio', lines=['3,75 €', 'por acción'])), at='tiene que rebajar el precio'),
    BOLSA(3.75, 'precio de salida de cada acción de Bankia', at='tres con setenta y cinco', frm=5.05))
DOC("Folleto de la oferta. Cuenta de resultados del primer trimestre de dos mil once: beneficio pro forma, no auditado, de noventa y un millones de euros. Las advertencias sobre riesgos ocupan decenas de páginas.",
    cd(dict(type='doc', title='Folleto de la oferta pública de Bankia', lines=['Primer trimestre de 2011', 'Beneficio pro forma no auditado: 91 millones'], source='Registrado en la CNMV · 29 de junio de 2011'), at='Folleto de la oferta'))
NEW("Aun así, la operación se cierra. Bankia capta tres mil noventa y dos millones de euros. Y la mayor parte de ese dinero no viene de fondos ni de bancos de inversión. Viene de la gente de a pie.",
    cd(dict(type='counter', **{'from': 0}, to=3092, label='millones captados en la salida a bolsa', suffix=' M€'), at='tres mil noventa y dos millones'),
    ai('hucha_rota', 'a ceramic piggy bank on a kitchen table, its coins being poured into a canvas bank bag by an old hand, warm window light, intimate', at='Viene de la gente de a pie'))
NAR("Piensa en lo que significaba para muchos de ellos. No eran inversores profesionales. Eran personas que confiaban en la caja de su barrio, la misma de la libreta de ahorros y la hipoteca. Si el empleado de toda la vida decía que era buena idea, ¿por qué iban a dudar?",
    AIR('jubilado_firma', at='No eran inversores profesionales'),
    ai('barrio_caja', 'a neighborhood savings bank branch on a quiet Spanish street corner in the early evening, warm light inside, an elderly couple walking in arm in arm, seen from behind, nostalgic', at='la caja de su barrio'))
DAT("Trescientos cuarenta y siete mil trescientos treinta y ocho accionistas individuales. Frente a solo doscientos ochenta inversores institucionales. Más de la mitad del dinero, unos mil ochocientos millones, lo pusieron pequeños ahorradores.",
    cd(dict(type='versus', left=dict(title='Accionistas individuales', lines=['347.338']), right=dict(title='Inversores institucionales', lines=['280'])), at='Trescientos cuarenta y siete mil'))
B('accion')
NAR("[dramatically] Veinte de julio de dos mil once. Nueve de la mañana. Palacio de la Bolsa de Madrid. Banqueros, empresarios y políticos llenan el parqué. Y Rodrigo Rato sube a tocar la campana.",
    DIA(1, 310, 'Bankia empieza a cotizar · 20 de julio de 2011', at='Veinte de julio de dos mil once'),
    ph('Palacio de la Bolsa de Madrid interior', at='Palacio de la Bolsa de Madrid', lt=['Palacio de la Bolsa', 'Madrid · 20 de julio de 2011'], lugar='bolsa'),
    ai('parque_lleno', 'an ornate nineteenth-century stock exchange trading floor packed with men in suits and a few women, cameras flashing, a raised podium, golden chandelier light, excitement', at='llenan el parqué'),
    ai('mano_campana', 'a hand in a dark suit sleeve gripping the rope of a polished bronze bell, motion blur as it swings, flashes from photographers, golden light', at='sube a tocar la campana'))
RAT("Es una satisfacción compartir con más de trescientos cuarenta y siete mil accionistas este momento histórico.",
    cd(dict(type='quote', text='Es una satisfacción compartir con más de 347.000 accionistas este momento histórico.', attrib='Rodrigo Rato · Bolsa de Madrid, 20 de julio de 2011'), at='Es una satisfacción'))
NEW("La primera hora es un mal presagio. La acción llega a caer más de un cinco por ciento. Rato habla de una auténtica tormenta financiera en Europa. Y al cierre, la cotización termina exactamente donde empezó: tres con setenta y cinco. La prensa señala que los bancos que colocaron la oferta compraron para sostener el precio.",
    ai('pantalla_roja', 'a large stock ticker display board in a historic exchange hall flashing red light across the faces of a crowd seen from behind, tension, no readable numbers', at='La acción llega a caer'),
    ai('tormenta_madrid', 'dark storm clouds gathering over the Madrid skyline with a lightning bolt over the business district, dramatic oil painting, emerald and gold light', at='una auténtica tormenta financiera'),
    BOLSA(3.75, 'cierre del primer día · 20 de julio de 2011', at='termina exactamente donde empezó', frm=3.55))
PRE("Las crónicas de ese día se llenan con la imagen de la campana. Bankia ya es el cuarto banco del país por tamaño. En octubre entrará en el Ibex treinta y cinco, el club de las mayores empresas de la bolsa española.",
    ai('telediario', 'a television set glowing in a dark Spanish bar at night, a few customers at the counter turned toward it, the screen showing an abstract golden bell shape, no text', at='Las crónicas de ese día'),
    KA('IBEX 35', 'ibex_club', 'the grand doors of an ornate stock exchange building opening onto a golden lit hall, silhouettes of men in suits walking in, triumphant', at='el Ibex treinta y cinco'))
NAR("Trescientas cuarenta y siete mil personas creían haber comprado un trozo de un banco sólido. Lo que no sabían es que el reloj ya había empezado a correr.",
    ai('reloj_arena', 'a large antique clock face on the wall of a dark bank hall, its hands moving, a sliver of green light across it, ominous', at='el reloj ya había empezado a correr'))

# ---------------- IV · EL CASTILLO DE NAIPES ----------------
T('El castillo de naipes', 'Agosto de 2011 · abril de 2012', num='IV', secs=4.5, sting='tema')
B('tension')
PRE("El verano de dos mil once es el de la crisis de la deuda europea. Grecia se tambalea. Italia y España pagan cada vez más por pedir prestado. Y la acción de Bankia empieza a bajar. Despacio. Sin pausa.",
    ai('europa_tormenta', 'a stormy sea crashing against a lighthouse on a rocky European coast at night, the light beam struggling through the rain, oil painting, epic', at='la crisis de la deuda europea'),
    ai('escalera_baja', 'a man in a suit descending a long spiral staircase into darkness, seen from above, his figure getting smaller, green light fading', at='Despacio. Sin pausa'))

NAR("En noviembre, España vota. Mariano Rajoy gana con mayoría absoluta. Su ministro de Economía, Luis de Guindos, llega con una prioridad: limpiar los balances de los bancos.",
    ph('Mariano Rajoy 2011', at='Mariano Rajoy', lt=['Mariano Rajoy', 'Presidente del Gobierno desde diciembre de 2011', 'gobierno'], lugar='rajoy'),
    ph('Luis de Guindos', at='Luis de Guindos', lt=['Luis de Guindos', 'Ministro de Economía (2011-2018)', 'gobierno'], lugar='guindos'),
    ai('escoba_balance', 'a giant broom sweeping a cascade of scattered documents and miniature houses off a dark marble floor of a bank vault, dramatic, symbolic, oil painting', at='limpiar los balances'))
DAT("Y el veintiuno de noviembre, el día siguiente a las elecciones, el Banco de España interviene el Banco de Valencia. Su mayor accionista era Bancaja, una de las siete cajas de Bankia. Es la primera grieta visible dentro del grupo.",
    ph('Banco de Valencia sede', at='el Banco de Valencia', lt=['Banco de Valencia', 'Valencia'], lugar='bancovalencia'),
    ai('grieta_marmol', 'a crack spreading across the polished marble floor of a grand bank hall, a beam of cold light following it, dust rising, cinematic', at='la primera grieta visible'))
DOC("Real Decreto-ley de febrero de dos mil doce. Las entidades deberán provisionar sus créditos al ladrillo, es decir, apartar dinero para cubrir lo que probablemente nunca cobrarán. En mayo llegará un segundo decreto que exigirá todavía más.",
    cd(dict(type='doc', title='Real Decreto-ley 2/2012', lines=['de saneamiento del sector financiero', 'Provisiones por los activos inmobiliarios'], source='Boletín Oficial del Estado · 4 de febrero de 2012'), at='Real Decreto-ley de febrero'),
    ai('caja_monedas', 'hands placing stacks of coins into a deep metal drawer of a vault, the drawer seemingly bottomless, green light from below, symbolic', at='apartar dinero para cubrir'))
NEW("Y sin embargo, ese mismo febrero, Bankia presenta resultados. Asegura que en dos mil once ganó trescientos nueve millones de euros. Sobre el papel, todo va bien.",
    cd(dict(type='counter', **{'from': 0}, to=309, label='millones de beneficio que Bankia anuncia para 2011 · febrero de 2012', suffix=' M€', prefix='+'), at='trescientos nueve millones'),
    ai('papel_sonrisa', 'a glossy annual report lying on a polished table under bright light, a hand placing a gold pen on top, everything gleaming, hollow luxury, no readable text', at='Sobre el papel, todo va bien'))
DAT("En la bolsa, el mercado piensa otra cosa. En marzo, la acción ya ronda los tres euros. Más de un veinte por ciento por debajo del precio de salida.",
    BOLSA(3.0, 'cotización de Bankia · marzo de 2012', at='ronda los tres euros', frm=3.75))
NAR("Y entonces aparece el hombre que cambia la historia. No es un juez ni un político. Es el socio de la auditora Deloitte responsable de las cuentas de Bankia: Francisco Celma. Tiene que firmar las cuentas de dos mil once. Y no lo ve claro.",
    ai('auditor_noche', 'a man in shirtsleeves alone in a glass office at night surrounded by binders, rubbing his temples, seen from behind, the city lights below, emerald desk lamp', at='Francisco Celma'),
    ai('firma_suspendida', 'a fountain pen hovering above the signature line of a thick bound document, the hand hesitating, extreme close-up, dramatic chiaroscuro', at='Y no lo ve claro'))
NEW("El problema está en BFA, la matriz. Según contaría Celma en el juicio, el valor al que BFA tenía apuntada su participación en Bankia era muy superior a lo que de verdad valía en bolsa. Reconocerlo suponía pérdidas multimillonarias.",
    ai('balanza', 'an old brass weighing scale on a dark desk, one side heavy with a stack of documents, the other side with a few gold coins rising, dramatic light, symbolic', at='era muy superior'))
NEW("Pero el agujero de fondo no era contable. Era de ladrillo. Préstamos a promotores que no iban a devolverse, suelo que ya no valía lo que decían los libros, pisos embargados que nadie quería. Cada mes que pasaba, ese agujero se hacía más grande. Y cada nuevo decreto del Gobierno obligaba a mirarlo de frente.",
    AIR('bloques_vacios', at='Era de ladrillo'),
    ai('pozo_oscuro', 'looking down into a deep dark hole that has opened in the middle of a marble bank lobby floor, cracked tiles at the edges, men in suits standing at the rim seen from above, cinematic', at='ese agujero se hacía más grande'))
CEL("Presidente, no va.",
    cd(dict(type='quote', text='Presidente, no va.', attrib='Francisco Celma (Deloitte) a Rodrigo Rato, 13 de abril de 2012 · según su declaración en el juicio'), at='Presidente, no va'))
NAR("Trece de abril de dos mil doce. Eso es lo que Celma recordó haberle dicho a Rato. Cuatro días después, el Banco de España aprueba el plan de saneamiento que presenta Rato. Pero Deloitte sigue sin dar su visto bueno. Y el treinta de abril, último día del plazo, el grupo envía sus cuentas a la Comisión Nacional del Mercado de Valores. Sin la firma del auditor.",
    ai('sello_lacre', 'an official rubber stamp coming down hard on a document on a dark desk, ink spatter, extreme close-up, motion, no readable text', at='el Banco de España aprueba el plan'),
    DIA(285, 310, 'cuentas enviadas sin la firma del auditor · 30 de abril de 2012', at='El treinta de abril'),
    ai('sobre_sin_firma', 'a sealed envelope being dropped into an official mail slot of a government building at night, a lone hand, cold blue light, no readable text', at='Sin la firma del auditor'))
PRE("En el sector financiero, aquello suena a alarma. Presentar las cuentas sin el informe del auditor no es lo normal en un banco que cotiza en el Ibex. Las llamadas entre Bankia, el Banco de España y el Ministerio de Economía se multiplican.",
    ai('telefonos', 'three men in different dark offices on telephones at night, split by shadows, tense faces turned away, cigarette smoke, thriller atmosphere', at='Las llamadas entre Bankia'))
NEW("[softly] Al castillo de naipes le quedaba una semana en pie.",
    ai('naipes', 'a tall house of playing cards on a green felt boardroom table beginning to collapse, cards in mid-air, dramatic light, slow motion, no readable cards', at='Al castillo de naipes'))

NEW("Y si este documental te está atrapando, es buen momento para suscribirte a DocuVox. Porque lo que viene ahora es la semana más vertiginosa de la historia de la banca española.",
    ai('vertigo_torre', 'looking straight down from the top of a leaning glass skyscraper at night, the city lights far below, vertigo, emerald reflections, cinematic', at='la semana más vertiginosa'))
# ---------------- V · DIECINUEVE MIL MILLONES ----------------
T('Diecinueve mil millones', 'Mayo y junio de 2012', num='V', secs=4.5, sting='tema')
B('accion')
NAR("Lunes, siete de mayo de dos mil doce. A media mañana llega un comunicado. Rodrigo Rato dimite como presidente de Bankia y de BFA.",
    DIA(292, 310, 'dimite Rodrigo Rato · 7 de mayo de 2012', at='siete de mayo de dos mil doce'),
    ai('reporteros', 'a crowd of reporters with microphones and cameras pressing against the glass doors of a corporate headquarters in Madrid, flashes, chaos, seen from inside', at='llega un comunicado'),
    ph('Rodrigo Rato 2012', at='Rodrigo Rato dimite', lt=['Rodrigo Rato', 'Dimite el 7 de mayo de 2012', 'banca'], lugar='rato'))
DOC("En su nota, Rato explica que su salida es lo más conveniente para esta entidad. Y propone a su sucesor: José Ignacio Goirigolzarri, el que había sido consejero delegado del BBVA durante años.",
    cd(dict(type='quote', text='Lo más conveniente para esta entidad.', attrib='Comunicado de Rodrigo Rato · 7 de mayo de 2012'), at='lo más conveniente para esta entidad'),
    ph('José Ignacio Goirigolzarri 2012', at='José Ignacio Goirigolzarri', lt=['José Ignacio Goirigolzarri', 'Ex consejero delegado del BBVA', 'banca'], lugar='goiri'))
NEW("Ese mismo día se sabe que el Gobierno y el Banco de España preparan una inyección de entre siete mil y diez mil millones de euros. La cifra se quedará muy corta.",
    ai('maletin_oro', 'a heavy leather briefcase being opened on a table in a dim government office, golden light spilling out from inside, men leaning over it in shadow', at='preparan una inyección'))
NAR("[dramatically] Miércoles, nueve de mayo. Goirigolzarri toma posesión. Esa misma tarde, el consejo de BFA pide al Estado que convierta en acciones los cuatro mil cuatrocientos sesenta y cinco millones que le había prestado. Traducido: BFA pasa a ser del Estado. Bankia queda nacionalizada de hecho.",
    ai('llave_entrega', 'a large old brass key being handed from one hand to another across a dark marble table, both hands in dark suit sleeves, dramatic spotlight', at='Goirigolzarri toma posesión'),
    cd(dict(type='kw', word='NACIONALIZADA', sub='el Estado se queda con BFA y controla el 45 % de Bankia'), at='Bankia queda nacionalizada'))
DAT("En tres días, la acción pierde un trece por ciento. Y los clientes empiezan a hacer la pregunta que ningún banco quiere oír: ¿está seguro mi dinero?",
    ai('cajero_cola', 'a nervous line of people at night in front of a bank cash machine on a Madrid street, coats and umbrellas, the screen glowing green, seen from behind', at='está seguro mi dinero'))
DAT("El Gobierno responde que los depósitos están garantizados. Y es cierto: quien tenía una cuenta o un depósito no perdió nada. Pero los accionistas y los que tenían preferentes eran otra historia.",
    ai('candado', 'a heavy steel padlock on the door of a bank vault in close-up, emerald light, reassuring and cold at the same time', at='los depósitos están garantizados'))
NAR("Y llegamos a donde empezamos. Viernes, veinticinco de mayo. Por la mañana, la Comisión Nacional del Mercado de Valores suspende la cotización de Bankia. A las cuatro y media se reúne el consejo. Y Goirigolzarri pone la cifra sobre la mesa.",
    DIA(310, 310, 'Bankia pide el rescate · 25 de mayo de 2012', at='Viernes, veinticinco de mayo'),
    ai('pantalla_negra', 'a stock ticker board in a dark exchange hall with one line gone dark, traders in silhouette staring up at it, eerie silence', at='suspende la cotización'),
    AIR('consejo_noche', at='A las cuatro y media'))
DAT("Diecinueve mil millones para BFA y Bankia. Sumados a los préstamos anteriores, las ayudas públicas acabarán en veintidós mil cuatrocientos veinticuatro millones de euros. Y las cuentas de dos mil once, rehechas: pérdidas de dos mil novecientos setenta y nueve millones en Bankia. Tres mil trescientos dieciocho en BFA.",
    cd(dict(type='counter', **{'from': 19000}, to=22424, label='millones de euros en ayudas públicas a BFA-Bankia', suffix=' M€'), at='veintidós mil cuatrocientos veinticuatro millones'),
    cd(dict(type='split', left=dict(title='Bankia · 2011', lines=['−2.979 millones']), right=dict(title='BFA · 2011', lines=['−3.318 millones'])), at='Y las cuentas de dos mil once, rehechas'))
DAT("¿Cómo se pasa de ganar trescientos nueve millones a perder casi tres mil? El nuevo equipo revisa los préstamos y los inmuebles uno por uno. Y decide apartar ocho mil quinientos millones en provisiones, por encima incluso de lo que exigían los dos decretos del Gobierno.",
    cd(dict(type='counter', **{'from': 0}, to=8500, label='millones en provisiones adicionales · mayo de 2012', suffix=' M€'), at='ocho mil quinientos millones'))
NEW("Para hacerse una idea: con veintidós mil millones se podría pagar el sueldo de un año de casi un millón de trabajadores en España. Las pérdidas de BFA fueron las segundas mayores de la historia de la banca española, solo por detrás de las de Banesto en mil novecientos noventa y tres.",
    ai('estadio_gente', 'a vast crowd of ordinary workers filling a huge stadium at dusk seen from high above, tiny figures, overwhelming scale, golden light', at='casi un millón de trabajadores'),
    KA('BANESTO, 1993', 'banesto_eco', 'an old bank headquarters in Madrid in the early nineties under grey sky, police cars in front, photographers, oil painting with muted colors', at='Banesto'))
NAR("Esa noche, el rescate de un banco dejó de ser un problema de un banco. Pasó a ser un problema de un país. Porque si la cuarta entidad de España necesitaba diecinueve mil millones, ¿cuánto necesitaban las demás? Esa era la pregunta que se hacían en Londres, en Fráncfort y en Washington.",
    ai('mapa_europa_luz', 'a darkened map of Europe on a wall in a war-room style office at night, a single red light glowing over the Iberian peninsula, silhouettes of officials in front, no readable text', at='un problema de un país'),
    ai('fondos_extranjeros', 'bankers in a high-rise office in a foggy northern European city at night watching screens, one picking up a phone urgently, seen from behind, cold blue light', at='en Londres, en Fráncfort y en Washington'))
PRE("El lunes, cuando Bankia vuelve a cotizar, la acción se hunde: llega a caer cerca de un veinticinco por ciento en los primeros minutos. La prima de riesgo de España, lo que el país paga de más que Alemania por pedir prestado, supera los quinientos puntos. Y ese mismo lunes, el presidente del Gobierno comparece ante la prensa.",
    ai('desplome', 'traders on a stock exchange floor with hands on their heads, papers flying, red light flooding the room, chaos, motion blur, cinematic', at='la acción se hunde'),
    cd(dict(type='counter', **{'from': 400}, to=500, label='puntos de prima de riesgo · 28 de mayo de 2012'), at='supera los quinientos puntos'))

RAJ("No va a haber ningún rescate de la banca española.",
    cd(dict(type='quote', text='No va a haber ningún rescate de la banca española.', attrib='Mariano Rajoy · rueda de prensa, 28 de mayo de 2012'), at='No va a haber ningún rescate'))
NEW("[pause] Doce días después, el sábado nueve de junio, el Eurogrupo acuerda prestar a España hasta cien mil millones de euros para sanear sus bancos. El Gobierno lo llama línea de crédito. En toda Europa se le llama rescate.",
    ph('Justus Lipsius building Brussels', at='el Eurogrupo', lt=['Consejo de la UE', 'Bruselas'], lugar='bruselas'),
    cd(dict(type='counter', **{'from': 0}, to=100000, label='millones · préstamo europeo para la banca española · 9 de junio de 2012', suffix=' M€'), at='hasta cien mil millones'),
    ai('bandera_ue_lluvia', 'a row of flags in front of a modern glass government building in Brussels in heavy rain at night, blurred, cold, no symbols readable', at='En toda Europa se le llama rescate'))
RAJ("El crédito es a la banca y lo va a pagar la banca.",
    cd(dict(type='quote', text='El crédito es a la banca y lo va a pagar la banca.', attrib='Mariano Rajoy · Congreso de los Diputados, junio de 2012'), at='lo va a pagar la banca'))
DAT("Antes, el veintiuno de junio, dos consultoras independientes, Oliver Wyman y Roland Berger, habían calculado lo que necesitaba toda la banca española en el peor escenario: hasta sesenta y dos mil millones de euros.",
    cd(dict(type='counter', **{'from': 0}, to=62000, label='millones que necesitaría la banca española en el peor escenario · junio de 2012', suffix=' M€'), at='hasta sesenta y dos mil millones'))
NAR("[dramatically] Y el veinte de julio de dos mil doce, el Eurogrupo aprueba definitivamente el memorando del rescate bancario español. La fecha no es casualidad del guion. Es un año exacto, día por día, después de que sonara la campana de Bankia.",
    ai('calendario', 'an old wall calendar in a dim office with its pages blowing and flipping in a draft of wind, landing on a single page, golden shaft of light, no readable numbers', at='un año exacto, día por día'),
    AIR('mano_campana', at='sonara la campana de Bankia'))
DAT("De ese préstamo europeo, al grupo BFA-Bankia le tocaron casi dieciocho mil millones. El mayor pedazo de todos.",
    cd(dict(type='counter', **{'from': 0}, to=17959, label='millones del rescate europeo para BFA-Bankia', suffix=' M€'), at='casi dieciocho mil millones'))
NAR("[softly] Faltaba saber quién iba a pagar de verdad. Y la respuesta estaba en las oficinas de siempre. En los mismos mostradores donde, un año antes, se habían vendido las acciones.",
    AIR('oficina_mesa', at='quién iba a pagar de verdad'),
    ai('mostrador_vacio', 'an empty bank counter in a small Spanish branch after closing time, a single chair, a forgotten umbrella, cold fluorescent light, melancholy', at='En los mismos mostradores'))
M('drama', 6)
