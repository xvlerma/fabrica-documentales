# -*- coding: utf-8 -*-
# «El corralito argentino» · parte 3: cinco presidentes, el corralón, ¿podría pasar en España? y cierre
from lib import *

# ---------------- VI · CINCO PRESIDENTES ----------------
T('Cinco presidentes', '20 de diciembre de 2001 · 1 de enero de 2002', num='VI', secs=6.0, sting='accion')
B('tension')
NEW("Como no había vicepresidente, que había dimitido un año antes, el poder pasa al presidente del Senado. Ramón Puerta, peronista. Gobierna dos días, solo para convocar al Congreso.",
    ph('Ramón Puerta', at='Ramón Puerta', lt=['Ramón Puerta', 'Presidente provisional · 20-23 de diciembre', 'gobierno'], lugar='puerta'),
    cd(dict(type='timeline', header='Cinco presidentes en once días', events=[('20 dic.', 'De la Rúa renuncia'), ('21 dic.', 'Ramón Puerta'), ('23 dic.', 'Rodríguez Saá'), ('30 dic.', 'Eduardo Camaño'), ('1 ene.', 'Eduardo Duhalde')]), at='Gobierna dos días'))
NAR("El domingo veintitrés, el Congreso elige presidente interino al gobernador de San Luis, Adolfo Rodríguez Saá. Y en su discurso de investidura, ante diputados y senadores, hace un anuncio que nadie se atrevía a pronunciar.",
    ph('Adolfo Rodríguez Saá', at='Adolfo Rodríguez Saá', lt=['Adolfo Rodríguez Saá', 'Presidente interino · 23-30 de diciembre', 'gobierno'], lugar='rsaa'),
    ph('Congreso de la Nación Argentina edificio', at='el Congreso elige', lt=['Congreso de la Nación', 'Buenos Aires'], lugar='congreso'))
NEW("Por cierto, cuentan las crónicas de aquellos días que el primer jefe de Gobierno extranjero en llamar a Rodríguez Saá, antes incluso de que el Congreso lo eligiera, fue el presidente del Gobierno español, José María Aznar. España tenía mucho dinero en juego en Argentina.",
    ph('José María Aznar', at='José María Aznar', lt=['José María Aznar', 'Presidente del Gobierno de España', 'europa'], lugar='aznar'),
    ai('telefono_oceano', 'an old telephone cord stretching across a dark ocean between two continents seen from space, glowing faintly, symbolic', at='antes incluso de que'))
RSA("Anuncio que el Estado argentino suspenderá el pago de la deuda.",
    cd(dict(type='quote', text='Anuncio que el Estado argentino suspenderá el pago de la deuda.', attrib='Adolfo Rodríguez Saá · Asamblea Legislativa, 23 de diciembre de 2001'), at='Anuncio que el Estado'))
CRO("La mayoría de los legisladores se pone en pie y empieza a gritar: ¡Argentina! ¡Argentina! Es el mayor impago de deuda soberana de la historia hasta ese momento. Más de sesenta mil millones de dólares en bonos dejan de pagarse.",
    ai('hemiciclo_pie', 'a crowded parliament chamber with legislators on their feet applauding and shouting, papers thrown in the air, seen from the gallery', at='se pone en pie'),
    cd(dict(type='counter', **{'from': 0}, to=61803, label='millones de dólares en bonos en impago', suffix=' M$'), at='Más de sesenta mil millones'))
NEW("Rodríguez Saá promete un millón de puestos de trabajo y mantener el uno a uno. Pero los cacerolazos no paran, los gobernadores de su propio partido le retiran el apoyo y, a los siete días, también dimite.",
    ai('cacerolazo_congreso', 'a night crowd banging pots in front of a domed parliament building, a few small fires on the street, defiant', at='los cacerolazos no paran'),
    ai('silla_vacia2', 'a second empty chair at the head of a long table with a microphone, a resignation letter lying on it, cold light, repetition motif', at='también dimite'))
NAR("El final de Rodríguez Saá es casi una escena de película. Convoca a los gobernadores a una cumbre en la residencia de Chapadmalal, junto al mar. Casi ninguno aparece. Entiende el mensaje, vuela a su provincia, San Luis, y desde allí anuncia su renuncia por televisión.",
    ai('mesa_costa', 'a long conference table set for many guests in a seaside residence, almost all chairs empty, waves visible through the window, one figure standing alone', at='Casi ninguno aparece'))
CRO("Durante tres días ocupa el cargo el presidente de la Cámara de Diputados, Eduardo Camaño. Y el uno de enero de dos mil dos, el Congreso elige a un quinto presidente, el que debía terminar el mandato. El peronista Eduardo Duhalde.",
    ph('Eduardo Camaño', at='Eduardo Camaño', lt=['Eduardo Camaño', 'Presidente provisional · 30 dic.-1 ene.', 'gobierno'], lugar='camano'),
    ph('Eduardo Duhalde', at='Eduardo Duhalde', lt=['Eduardo Duhalde', 'Presidente de Argentina · 2002-2003', 'gobierno'], lugar='duhalde'))
NAR("En su discurso de toma de posesión, Duhalde mira a los ahorradores a los ojos. Y les hace una promesa que todavía hoy recuerda cualquier argentino que tuviera una cuenta en el banco.",
    ai('ahorrista_escucha', 'an elderly couple sitting very close to a small radio on a kitchen table, holding hands, listening intently, warm lamp', at='mira a los ahorradores'))
DUH("[serious] El que depositó dólares recibirá dólares.",
    cd(dict(type='quote', text='El que depositó dólares recibirá dólares.', attrib='Eduardo Duhalde · discurso de asunción, 1 de enero de 2002'), at='El que depositó dólares'))
NAR("[pause] Cinco días después, esa promesa ya no existía.",
    cd(dict(type='kw', word='5 DÍAS', sub='lo que duró la promesa'), at='Cinco días después'))

NAR("¿Qué pasó en esos cinco días? Que alguien hizo las cuentas. En los bancos no había dólares suficientes para devolver todos los depósitos en dólares. Muchos ya se habían ido del país. Y los que quedaban estaban prestados. Para cumplir la promesa, habría que inventarlos.",
    ai('cajon_vacio', 'a bank teller pulling open drawer after drawer in a vault, every one empty, a single coin rolling on the floor, flashlight beam', at='Que alguien hizo las cuentas'))
# ---------------- VII · EL CORRALÓN ----------------
NEW("[pause] Recapitulemos. En diciembre de dos mil uno, Argentina congeló los depósitos, perdió a su presidente, dejó de pagar su deuda y tuvo cinco jefes de Estado en once días. Pero lo peor para los ahorradores todavía no había llegado.",
    cd(dict(type='recap', header='Hasta aquí', items=['1 dic. · el corralito: 250 $ por semana', '19 dic. · estado de sitio y cacerolazo', '20 dic. · De la Rúa se va en helicóptero', '23 dic. · default de la deuda', '1 ene. · Duhalde promete dólares']), at='Recapitulemos'))
NAR("Si estás disfrutando de esta historia, suscríbete a DocuVox: es gratis y nos ayuda a hacer más documentales como este. Ahora sí. Vamos a ver qué pasó con el dinero.",
    ai('suscribe_campana', 'a single brass bell hanging in a dark doorway catching a ray of light, dust in the air, inviting mood', at='suscríbete a DocuVox'))
T('El corralón', '2002', num='VII', secs=6.0, sting='accion')
B('drama')
CRO("Seis de enero de dos mil dos. El Congreso aprueba la Ley de Emergencia Pública. La convertibilidad, el uno a uno que había durado casi once años, muere oficialmente. El peso se devalúa.",
    cd(dict(type='doc', title='Ley 25.561 de Emergencia Pública', lines=['y de reforma del régimen cambiario', 'Fin de la convertibilidad', 'Nuevo dólar oficial: 1,40 pesos'], source='Congreso de la Nación · 6 de enero de 2002'), at='la Ley de Emergencia Pública'),
    USD(1.40, 'pesos por dólar · dólar oficial, enero de 2002', at='El peso se devalúa'))
NEW("Pero el dinero sigue encerrado. Y se encierra todavía más. Los plazos fijos quedan reprogramados: te los devolverán, sí, pero dentro de años. Al corralito le sale un hermano mayor. El corralón.",
    ai('corral_grande', 'an enormous iron fence enclosing a crowd of tiny people and their suitcases, the small wooden playpen from before visible inside it, surreal escalation', at='El corralón'))
NAR("Y en febrero llega el golpe definitivo. La pesificación. Todos los depósitos en dólares se convierten a la fuerza en pesos. A uno con cuarenta pesos por cada dólar.",
    cd(dict(type='doc', title='Decreto 214/2002', lines=['Pesificación de depósitos y deudas', 'Depósitos: 1,40 pesos por dólar + ajuste', 'Deudas: 1 peso por dólar'], source='Poder Ejecutivo Nacional · febrero de 2002'), at='La pesificación'),
    ai('dolar_derrite', 'a green dollar bill melting like wax into a puddle of pale blue paper money on a bank counter, surreal, high contrast', at='se convierten a la fuerza'))
CRO("Uno con cuarenta parecía razonable. El problema es que el dólar, ya libre, no se quedó ahí. En pocos meses llegó a rozar los cuatro pesos.",
    USD(3.90, 'pesos por dólar · máximo de 2002 (aprox.)', at='rozar los cuatro pesos', frm=1.40))
NAR("Haz la cuenta. Si tenías diez mil dólares en el banco, te devolvían catorce mil pesos. Y con catorce mil pesos, en la calle, podías comprar unos tres mil quinientos dólares. Si aceptabas los pesos, habías perdido casi dos tercios de tus ahorros. Sin hacer nada. Sin tocar nada.",
    cd(dict(type='split', left=dict(title='Lo que depositaste', lines=['10.000 dólares', 'antes del corralito']), right=dict(title='Lo que podías recuperar', lines=['14.000 pesos', '≈ 3.500 dólares a mediados de 2002'])), at='Haz la cuenta'),
    ai('ahorros_humo', 'a pair of hands holding a wad of banknotes that turns into smoke and drifts away, a disbelieving silhouette behind, slow motion', at='casi dos tercios'))
NEW("Y había una segunda trampa. La pesificación fue asimétrica. Los depósitos se cambiaban a uno con cuarenta. Pero las deudas en dólares, a uno por uno.",
    cd(dict(type='versus', left=dict(name='Ahorradores', lines=['depósitos en dólares', 'pesificados a 1,40']), right=dict(name='Deudores', lines=['deudas en dólares', 'pesificadas a 1,00'])), at='La pesificación fue asimétrica'))
CRO("Quien debía cien mil dólares, de repente debía cien mil pesos. Un regalo para los grandes endeudados, entre ellos muchas empresas. La diferencia la pagó el Estado, con nuevos bonos, y la pagaron los ahorradores. El propio Duhalde reconocería años después que su frase había sido un error.",
    ai('balanza_rota', 'an old brass scale tipped violently to one side, a heavy sack of coins crushing one pan while the other flies up empty, dramatic shadow', at='Un regalo para los grandes endeudados'))
DUH("Decir que el que depositó dólares recibiría dólares fue un error.",
    cd(dict(type='quote', text='Decir que el que depositó dólares recibiría dólares fue un error.', attrib='Eduardo Duhalde · entrevista en Radio Cooperativa, años después'), at='fue un error'))
B('calle')
NAR("Imagina por un momento que eres tú. Que tienes los ahorros de toda una vida en un plazo fijo en dólares. La entrada de un piso. La jubilación. Y que un día, por decreto, alguien decide que ya no son dólares. Y que lo que te queda vale un tercio.",
    ai('ahorro_vida', 'an elderly couple sitting at a kitchen table staring at a bank statement in silence, a framed wedding photo on the wall behind, dim afternoon light', at='los ahorros de toda una vida'))
NAR("La reacción fue furiosa. Durante todo dos mil dos, miles de ahorradores se plantan cada semana frente a los bancos. Golpean las persianas con martillos. Pintan las fachadas. Y los bancos responden blindando las puertas con planchas de metal.",
    ai('martillos_banco', 'a crowd of middle-aged savers striking the metal-plated front of a bank with hammers and pots, sparks flying, rage in motion', at='Golpean las persianas con martillos'),
    ai('fachada_chapas', 'a grand bank facade completely covered with welded steel plates and graffiti scrawls without readable letters, an empty street, eerie', at='planchas de metal'))
CRO("En el centro de Buenos Aires, el grito se repetía cada semana frente a los bancos: chorros, chorros, chorros, devuelvan los ahorros. Ladrones. Devuelvan los ahorros. En noviembre de dos mil dos, en Mar del Plata, la tensión llegó a tal punto que la mayoría de los bancos de la ciudad no abrieron.",
    cd(dict(type='quote', text='Chorros, chorros, chorros, devuelvan los ahorros.', attrib='Consigna de los ahorristas · Buenos Aires, 2002'), at='chorros, chorros'),
    ph('Mar del Plata ciudad', at='en Mar del Plata', lt=['Mar del Plata', 'Argentina'], lugar='mardelplata'))
CRO("Los tribunales se llenan de recursos de amparo. El uno de febrero, la Corte Suprema declara inconstitucional el corralito en el caso de un ahorrador. Quien tenía abogado y paciencia, a veces, recuperaba algo más. Quien no, se quedaba con lo que le dieran.",
    ph('Palacio de Justicia de la Nación Buenos Aires', at='la Corte Suprema', lt=['Palacio de Justicia', 'Corte Suprema · Buenos Aires'], lugar='tribunales'),
    ai('expedientes_torre', 'towering stacks of legal files in a courthouse corridor, lawyers squeezing past, a clerk buried behind them, overwhelming', at='recursos de amparo'))
CRO("A quien no quería pesos, el Gobierno le ofreció otra salida: cambiar su depósito por bonos del Estado en dólares, los Boden, que se irían pagando a lo largo de diez años. Quien aguantó hasta dos mil doce recuperó buena parte de sus dólares. Pero tuvo que esperar una década.",
    cd(dict(type='timeline', header='La salida lenta', events=[('feb. 2002', 'Pesificación'), ('may. 2002', 'Primer canje por Boden 2012'), ('dic. 2002', 'Fin del corralito'), ('2003', 'Boden 2013'), ('ago. 2012', 'Último pago del Boden 2012')]), at='los Boden'),
    ai('reloj_arena_billetes', 'a huge hourglass where the falling sand is made of tiny banknotes, a seated figure waiting beside it as seasons change through the window', at='esperar una década'))
CRO("El corralito, el de los doscientos cincuenta pesos, se levantó oficialmente el dos de diciembre de dos mil dos. Había durado un año. Los plazos fijos del corralón tardaron todavía más.",
    DIA(367, 'del corralito · 2 de diciembre de 2002, se levanta', at='el dos de diciembre de dos mil dos', frm=300))
NEW("Mientras tanto, el país se hunde. El paro supera el veintiuno por ciento. La economía cae a una profundidad que no se veía en generaciones. Y en octubre de dos mil dos, más de la mitad de los argentinos, el cincuenta y siete y medio por ciento, está bajo la línea de la pobreza.",
    cd(dict(type='counter', **{'from': 38.3}, to=57.5, label='de la población bajo la línea de pobreza · octubre de 2002', suffix=' %', dec=1), at='el cincuenta y siete y medio'),
    ai('comedor_popular', 'a long table in a community soup kitchen with families eating from metal bowls, volunteers ladling soup from a huge pot, warm and grim', at='bajo la línea de la pobreza'))
NAR("La gente se las arregla como puede. Se multiplican los clubes del trueque: cambias una tarta por unas zapatillas, unas clases de inglés por una docena de huevos. Y por las noches, miles de cartoneros recorren las calles buscando papel y cartón para vender.",
    ai('trueque_feria', 'a bustling barter market in a school gym, people exchanging homemade bread, shoes and clothes across folding tables, lively', at='los clubes del trueque'),
    ai('cartonero_noche', 'a man pulling a handcart piled with cardboard through a dark city street at night, a child sitting on top, streetlights', at='cartoneros'))
NEW("Una película argentina de dos mil diecinueve con Ricardo Darín, La odisea de los giles, contó esta historia desde el pueblo: unos vecinos que juntan sus ahorros para montar una cooperativa y los pierden en el corralito. Su título lo dice todo. Los giles. Los ingenuos. Los que confiaron.",
    ai('vecinos_cooperativa', 'a group of small-town neighbours around a kitchen table pooling cash into a tin box, hopeful faces in shadow, warm lamp, rural Argentina', at='La odisea de los giles'))
# ---------------- VIII · AL OTRO LADO DEL RÍO ----------------
T('Al otro lado del río', 'Uruguay · 2002', num='VIII', secs=6.0, sting='accion')
B('tension')
NAR("[dramatically] Pero el corralito no se quedó en Argentina. Cruzó el río.",
    cd(dict(type='map', title='Al otro lado del Río de la Plata', bbox=[-59.5, -35.6, -55.5, -33.8], points=[dict(name='Buenos Aires', lon=-58.38, lat=-34.60, big=1), dict(name='Montevideo', lon=-56.16, lat=-34.90, big=1)]), at='Cruzó el río'))
CRO("Montevideo, dos mil dos. Durante años, miles de argentinos habían guardado sus dólares en bancos uruguayos, al otro lado del Río de la Plata. Era su caja fuerte. Cuando estalla el corralito, empiezan a sacarlos. Primero, poco a poco. Luego, en avalancha.",
    ph('Montevideo ciudad', at='Montevideo', lt=['Montevideo', 'Uruguay'], lugar='montevideo'),
    AIR('cajero_noche', at='empiezan a sacarlos'))
NEW("En medio año, el sistema bancario uruguayo devuelve casi la mitad de todos sus depósitos. Un cuarenta y siete por ciento, según los cálculos publicados después en el propio Uruguay. Las reservas del Banco Central se vacían.",
    cd(dict(type='counter', **{'from': 0}, to=47, label='de los depósitos salieron de los bancos uruguayos en medio año · 2002', suffix=' %'), at='Un cuarenta y siete por ciento'),
    AIR('reloj_arena_billetes', at='se vacían'))
CRO("El treinta de julio de dos mil dos, el presidente Jorge Batlle decreta un feriado bancario. Es el primero en veinte años. Los bancos de Uruguay no abren.",
    ph('Jorge Batlle', at='Jorge Batlle', lt=['Jorge Batlle', 'Presidente de Uruguay · 2000-2005', 'gobierno'], lugar='batlle'),
    ph('Banco de la República Oriental del Uruguay sede Montevideo', at='Los bancos de Uruguay no abren', lt=['Banco de la República', 'Montevideo'], lugar='brou'))
NAR("Durante varios días, un país entero se queda sin bancos. Y en Washington se negocia contra el reloj.",
    AIR('puerta_cierra', at='se queda sin bancos'))
NEW("La salida llega desde el Tesoro de Estados Unidos: un préstamo puente de mil quinientos millones de dólares. El domingo cuatro de agosto, el Parlamento uruguayo aprueba a toda prisa la ley que lo hace posible. Los plazos fijos en dólares de la banca pública se aplazan. Pero las cuentas corrientes y las cajas de ahorro de los dos bancos públicos quedan garantizadas.",
    cd(dict(type='counter', **{'from': 0}, to=1500, label='millones de dólares · préstamo puente del Tesoro de EE. UU. a Uruguay', suffix=''), at='mil quinientos millones'),
    cd(dict(type='doc', title='Ley 17.523 · Uruguay', lines=['Aprobada el 4 de agosto de 2002', 'Prórroga de los plazos fijos de la banca pública', 'Garantía de cuentas corrientes y cajas de ahorro'], source='Parlamento del Uruguay'), at='la ley que lo hace posible'))
CRO("Los bancos reabren días después, con fuerte vigilancia. Uruguay se libró de un corralito como el argentino. Pero varios bancos privados ya no volvieron a abrir sus puertas.",
    AIR('fachada_chapas', at='ya no volvieron a abrir'))
NAR("Y aquella crisis dejó una frase para la historia. En plena resaca, ante el secretario del Tesoro estadounidense, Batlle soltó en inglés: We are fantastic. [pause] Uruguay acababa de comprobar que el miedo no entiende de fronteras.",
    cd(dict(type='quote', text='We are fantastic.', attrib='Jorge Batlle ante el secretario del Tesoro de EE. UU. · 6 de agosto de 2002'), at='We are fantastic'))
NAR("[pause] Argentina tardó años en levantarse. Y desde entonces, la palabra corralito viaja sola por el mundo. Hasta que, en dos mil trece, aterrizó en Europa.",
    ai('palabra_viaja', 'a paper airplane flying from a smoky South American city across a dark ocean toward a Mediterranean island at dawn, symbolic', at='aterrizó en Europa'))

# ---------------- IX · ¿Y EN ESPAÑA? ----------------
NAR("[dramatically] Y ahí empieza la parte de esta historia que nos toca más de cerca. Porque lo que pasó en Buenos Aires parecía imposible en Europa. Hasta que pasó.",
    ai('sombra_europa', 'the long shadow of a South American palace stretching across the ocean and touching the coast of a European city at dawn, symbolic', at='Hasta que pasó'))
T('¿Y en España?', 'Chipre · Grecia · el Popular', num='IX', secs=6.0, sting='accion')
B('europa')
CRO("Chipre. Marzo de dos mil trece. Un país del euro, con bancos gigantes para su tamaño, pide un rescate a la Unión Europea y al FMI. La condición incluye algo que nunca se había hecho en la eurozona.",
    ph('Bank of Cyprus Nicosia', at='Chipre', lt=['Banco de Chipre', 'Nicosia'], lugar='chipre'),
    cd(dict(type='map', title='Corralitos en Europa', bbox=[-10.0, 33.5, 35.5, 44.5], points=[dict(name='Chipre · 2013', lon=33.38, lat=35.17, big=1), dict(name='Grecia · 2015', lon=23.73, lat=37.98, big=1), dict(name='España', lon=-3.70, lat=40.42)]), at='Un país del euro'))
CRO("El primer plan, pactado un fin de semana en Bruselas, cobraba un impuesto del seis coma setenta y cinco por ciento incluso a los depósitos de menos de cien mil euros, los que se suponía garantizados. Los chipriotas corren a los cajeros. Y el diecinueve de marzo, el Parlamento de Chipre lo tumba: ni un solo voto a favor.",
    cd(dict(type='kw', word='6,75 %', sub='impuesto propuesto a los depósitos de menos de 100.000 € · Chipre, marzo de 2013'), at='seis coma setenta y cinco'),
    ph('Cyprus House of Representatives Nicosia', at='el Parlamento de Chipre', lt=['Parlamento de Chipre', 'Nicosia · 19 de marzo de 2013', 'europa'], lugar='chipre'),
    cd(dict(type='seats', title='Votación en el Parlamento de Chipre · 19 de marzo de 2013', total=55, parties=[dict(name='En contra', seats=36, color=[214, 48, 49]), dict(name='Abstención', seats=19, color=[170, 180, 200]), dict(name='A favor', seats=0, color=[116, 172, 223])]), at='ni un solo voto a favor'))
NAR("La versión final salvó a los pequeños ahorradores. Pero Europa había cruzado una línea: por primera vez, el dinero de los clientes servía para pagar el rescate de un banco.",
    ai('linea_cruzada', 'a foot stepping over a glowing red line painted on the marble floor of a bank hall, crowd watching in shadow, symbolic', at='había cruzado una línea'))
NEW("Los bancos chipriotas cierran casi dos semanas. Cuando reabren, solo se pueden sacar trescientos euros al día. Y los depósitos de más de cien mil euros sufren una quita: en el Banco de Chipre, casi la mitad de lo que superaba esa cifra.",
    ai('nicosia_cola', 'people queuing at a bank in a sunny Mediterranean street, shuttered doors, a police officer at the entrance, worried crowd seen from behind', at='cierran casi dos semanas'),
    cd(dict(type='list', header='El corralito de Chipre · 2013', items=[('≈ 12 días', 'bancos cerrados'), ('300 €', 'al día por persona'), ('> 100.000 €', 'quita sobre lo que superaba'), ('2 años', 'de controles')]), at='trescientos euros al día'))
CRO("Grecia. Lunes, veintinueve de junio de dos mil quince. Los griegos se despiertan con los bancos cerrados y un límite de sesenta euros al día en los cajeros. Los bancos tardan tres semanas en reabrir. Y los últimos controles no se levantan hasta dos mil diecinueve.",
    cd(dict(type='kw', word='GRECIA', sub='29 de junio de 2015 · bancos cerrados'), at='Grecia'),
    cd(dict(type='counter', **{'from': 300}, to=60, label='euros al día en los cajeros griegos · 29 de junio de 2015', suffix=' €'), at='sesenta euros al día'),
    ai('jubilados_atenas', 'elderly pensioners waiting in a long line in the hot sun outside a closed bank in Athens, holding papers, a white marble building behind', at='Los bancos tardan tres semanas'))
CRO("Grecia vota en referéndum el cinco de julio. Gana el no a las condiciones del rescate. Una semana después, su Gobierno acepta un acuerdo todavía más duro. Con los bancos cerrados, el margen para negociar se había esfumado.",
    ai('urna_atenas', 'a polling station in a Greek school with voters dropping ballots, a closed bank visible through the window across the street, tense summer light', at='vota en referéndum'))
NEW("En España, el miedo tuvo fecha. Mayo de dos mil doce, cuando Bankia pidió el rescate. Aquella semana, el Nobel de Economía Paul Krugman llegó a escribir en el New York Times que veía venir el fin del euro y corralitos en España. Los ministros salieron a desmentirlo. Y no pasó. Pero el susto quedó.",
    ph('Paul Krugman', at='Paul Krugman', lt=['Paul Krugman', 'Premio Nobel de Economía · 2008', 'finanzas'], lugar='krugman'),
    ai('cola_bankia', 'worried customers queuing at a Spanish savings bank branch in 2012, an employee at the door trying to calm them, early summer light', at='el miedo tuvo fecha'))
NAR("Pero para cientos de miles de ahorradores españoles, aquellos años sí trajeron su propio corralito. Uno con otro nombre.",
    AIR('ahorro_vida', at='su propio corralito'))
CRO("Las participaciones preferentes. Durante años, bancos y cajas las colocaron a clientes de toda la vida como si fueran casi un depósito. No lo eran. No tenían fecha de vencimiento y no las cubría el Fondo de Garantía. En toda España se vendieron unos treinta mil millones de euros a cerca de setecientos mil clientes, según los cálculos publicados entonces.",
    cd(dict(type='counter', **{'from': 0}, to=30000, label='millones de euros en preferentes vendidos en España (aprox.)', suffix=''), at='unos treinta mil millones'),
    cd(dict(type='versus', left=dict(name='Depósito', lines=['fecha de vencimiento', 'cubierto hasta 100.000 €']), right=dict(name='Preferente', lines=['sin vencimiento', 'sin Fondo de Garantía'])), at='No lo eran'))
NEW("Cuando las cajas se hundieron, ese dinero quedó atrapado. No había quien lo comprara. Y en el rescate, las preferentes de Bankia se convirtieron en acciones con una quita media del treinta y ocho por ciento.",
    cd(dict(type='counter', **{'from': 0}, to=38, label='de quita media en las preferentes de Bankia · 2013', suffix=' %'), at='treinta y ocho por ciento'),
    AIR('expedientes_torre', at='quedó atrapado'))
CRO("Llegaron los arbitrajes y los juicios. Solo en Bankia, según la propia entidad, rondaban los trescientos mil afectados. Alrededor de tres de cada cuatro acabaron recuperando toda su inversión, por arbitraje o en los juzgados. Pero hubo quien tardó años.",
    cd(dict(type='list', header='Bankia · preferentes y subordinadas', items=[('≈ 300.000', 'afectados, según la entidad'), ('≈ 75 %', 'recuperó toda su inversión'), ('años', 'lo que tardaron algunos')]), at='Llegaron los arbitrajes'))
NAR("[pause] No fue un corralito. Nadie te impedía sacar el dinero de tu cuenta. Pero para quien lo vivió, la sensación se pareció mucho: abrir la carta del banco y descubrir que lo que creías ahorro no lo era.",
    AIR('ahorrista_escucha', at='la carta del banco'))
NAR("Y España. Siete de junio de dos mil diecisiete. El Banco Popular, el sexto banco del país, amanece intervenido. La Junta Única de Resolución europea lo vende al Santander por un euro.",
    ph('Banco Popular Español sede Madrid', at='El Banco Popular', lt=['Banco Popular', 'Madrid · junio de 2017', 'europa'], lugar='popular'),
    cd(dict(type='kw', word='1 EURO', sub='el precio del Banco Popular · 7 de junio de 2017'), at='por un euro'))
DOC("Nota del FROB, siete de junio de dos mil diecisiete. A través de esta decisión se garantiza la seguridad de los depositantes de Banco Popular y la ausencia de impacto para las finanzas públicas.",
    cd(dict(type='doc', title='Nota de prensa del FROB', lines=['«se garantiza la seguridad de los depositantes', 'de Banco Popular y la ausencia de impacto', 'para las finanzas públicas»'], source='Fondo de Reestructuración Ordenada Bancaria · 7 de junio de 2017'), at='Nota del FROB'))
NEW("Los clientes del Popular no perdieron un euro de sus depósitos. Los accionistas y algunos bonistas, en cambio, lo perdieron todo. Y ahí está la primera clave para responder a nuestra pregunta.",
    ai('accion_papel', 'a framed share certificate with no readable text falling and shattering on a marble floor, shards of glass flying, cold light', at='lo perdieron todo'))
NAR("[serious] Entonces, ¿podría pasar en España un corralito como el argentino? Vamos a separar lo que te protege de lo que no.",
    ai('balanza_espana', 'a balanced old scale on a table in a dim room, one pan holding a small shield, the other pan holding a crack of light, contemplative', at='podría pasar en España'))
CRO("Lo que te protege, primero. Argentina guardaba sus ahorros en una moneda que su Banco Central no podía fabricar: el dólar. Cuando se acabaron los dólares, se acabó el juego. España usa el euro, y detrás del euro está el Banco Central Europeo, que puede prestar a los bancos solventes el dinero que necesiten, siempre que aporten garantías.",
    ph('European Central Bank headquarters Frankfurt', at='el Banco Central Europeo', lt=['Banco Central Europeo', 'Fráncfort', 'europa'], lugar='bce'),
    cd(dict(type='versus', left=dict(name='Argentina 2001', lines=['ahorros en dólares', 'que no podía imprimir']), right=dict(name='España hoy', lines=['ahorros en euros', 'con el BCE detrás'])), at='Argentina guardaba sus ahorros'))
CRO("Segundo, el Fondo de Garantía de Depósitos. Si tu banco quiebra, cubre hasta cien mil euros por titular y por entidad. Es una norma europea, igual en los veintisiete países de la Unión.",
    cd(dict(type='kw', word='100.000 €', sub='por titular y por entidad · Fondo de Garantía de Depósitos'), at='el Fondo de Garantía de Depósitos'),
    cd(dict(type='counter', **{'from': 0}, to=100000, label='euros garantizados por titular y por entidad', suffix=' €'), at='hasta cien mil euros'))
NEW("Y hay una tercera diferencia. La deuda argentina estaba en dólares: había que conseguir dólares para pagarla. La deuda pública española es alta, ronda el cien por cien del PIB, pero está en euros, la misma moneda en la que se cobran los impuestos.",
    cd(dict(type='versus', left=dict(name='Argentina 2001', lines=['deuda en dólares', 'moneda ajena']), right=dict(name='España hoy', lines=['deuda en euros', '≈ 100 % del PIB'])), at='La deuda argentina estaba en dólares'))
NEW("Ahora, lo que no te protege del todo. Grecia demostró que, dentro del euro, si el Banco Central Europeo deja de dar liquidez a los bancos de un país, esos bancos cierran. Ocurrió en plena negociación del rescate griego. Y lo que el Fondo de Garantía protege es tu dinero si un banco quiebra, no que puedas sacarlo cuando quieras.",
    ai('grifo_bce', 'a giant tap high on a glass skyscraper slowly being turned off by a gloved hand, the stream of light below thinning to a drop over a small city', at='deja de dar liquidez'))
CRO("Además, desde la reforma de dos mil diecinueve, la normativa bancaria europea permite a las autoridades suspender los pagos de un banco en apuros hasta dos días hábiles, mientras deciden qué hacer con él. Es un corralito pequeño, con nombre técnico: moratoria.",
    cd(dict(type='kw', word='MORATORIA', sub='hasta 2 días hábiles · normativa europea de resolución bancaria'), at='moratoria'))
NAR("Y Chipre enseñó la regla que más conviene recordar: por encima de los cien mil euros por persona y por banco, tu dinero no está garantizado. Si el banco cae, puede usarse para rescatarlo.",
    cd(dict(type='split', left=dict(title='Hasta 100.000 €', lines=['garantizados por el FGD', 'por titular y entidad']), right=dict(title='Por encima', lines=['pueden sufrir pérdidas', 'si el banco cae'])), at='por encima de los cien mil euros'))
CRO("Hay algo que sí está en tu mano comprobar. Por ley, el contrato de cualquier depósito en España tiene que informar de qué fondo de garantía lo cubre y hasta qué cantidad. Y el límite de cien mil euros se cuenta por titular y por entidad, no por cuenta: dos cuentas en el mismo banco suman.",
    ai('contrato_lupa', 'hands holding a bank contract under a desk lamp, a pen pointing at a paragraph of blurred unreadable fine print, careful mood', at='el contrato de cualquier depósito'))
NEW("[pause] Así que la respuesta honesta es esta. Un corralito como el argentino, con el dinero atrapado durante años y los ahorros convertidos a la fuerza en otra moneda, necesitaría algo que hoy no se ve en el horizonte: que España saliera del euro de forma desordenada. Un cierre bancario de días, o pérdidas en grandes depósitos de un banco que quiebra, en cambio, ya han pasado en Europa. Y la ley lo permite.",
    ai('horizonte_niebla', 'a lone figure standing on a cliff over a misty sea looking toward a distant lighthouse, dawn, sky blue and black ink, contemplative', at='la respuesta honesta'))

CRO("Un último dato para ponerlo en perspectiva. El Fondo de Garantía de Depósitos español cubre hoy más de novecientos mil millones de euros. Es una cifra enorme. Y, como todos los seguros, está pensado para que quiebre un banco. No para que caigan todos a la vez.",
    cd(dict(type='counter', **{'from': 0}, to=924, label='mil millones de euros en depósitos garantizados por el FGD · diciembre de 2024', suffix=' MM€'), at='más de novecientos mil millones'),
    ai('paraguas_lluvia', 'a single large umbrella sheltering a small crowd from a heavy storm, while the storm grows darker on the horizon, symbolic', at='como todos los seguros'))
# ---------------- CIERRE ----------------
B('tema')
NAR("Veinticinco años después, en Buenos Aires todavía hay quien guarda los dólares debajo del colchón. No es una manía. Es memoria. Porque en diciembre de dos mil uno, los argentinos aprendieron que una ley que promete no tocar tus ahorros dura lo que tarda otro Gobierno en escribir otra.",
    ai('colchon_dolares', 'an old woman lifting the corner of a mattress to check a hidden envelope, a crucifix on the wall, dim bedroom, intimate', at='debajo del colchón'),
    ai('ley_sobre_ley', 'one official document being placed on top of another, the first slowly burning underneath, a pen still in the hand, symbolic', at='en escribir otra'))
NEW("El corralito no empezó con un decreto. Empezó mucho antes, con una moneda atada al dólar, con una deuda que nadie quería mirar y con un sistema que funcionaba mientras todos creyeran en él.",
    ai('castillo_naipes', 'a tall house of cards built from banknotes on a table, one card at the bottom slipping out, the whole structure starting to lean', at='mientras todos creyeran en él'))
NEW("La historia del corralito no es solo argentina. Es la historia de qué pasa cuando un Estado promete algo que no puede cumplir, y lo sostiene hasta el último día. Uno a uno. Intangibilidad. El que depositó dólares recibirá dólares. Tres promesas. Las tres rotas.",
    cd(dict(type='list', header='Tres promesas', items=[('1991', '«Un peso, un dólar»'), ('agosto de 2001', 'Ley de intangibilidad de los depósitos'), ('1 de enero de 2002', '«El que depositó dólares recibirá dólares»')]), at='Tres promesas'))
NAR("[pause] Porque un banco, al final, no es una caja fuerte. Es una promesa. Y el día que la gente deja de creer en ella, ninguna puerta es lo bastante gruesa.",
    ai('puerta_boveda_final', 'a colossal round vault door standing open to an empty room, a single figure silhouetted in the doorway looking in, last light', at='no es una caja fuerte'))
NAR("Si te ha gustado esta historia, suscríbete a DocuVox y cuéntanos en los comentarios: ¿tú sacarías el dinero del banco? En el próximo documental seguimos tirando del hilo del dinero. Nos vemos.",
    ai('heli_final', 'a small white helicopter disappearing into a red sunset over a calm city, the square below now empty with a few abandoned pots, closing image', at='Si te ha gustado'))
