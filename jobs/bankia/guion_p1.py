# -*- coding: utf-8 -*-
# «Bankia» · parte 1: apertura in medias res, siete cajas y el inspector
from lib import *

# ---------------- APERTURA: VIERNES 25 DE MAYO DE 2012 ----------------
B('tension')
NAR("[serious] Madrid. Viernes, veinticinco de mayo de dos mil doce. Cuatro y media de la tarde. En la sede de Bankia, el consejo de administración se encierra en una sala.",
    ph('Puerta de Europa towers Madrid', at='Madrid', lt=['Torres Puerta de Europa', 'Madrid'], lugar='kio'),
    ai('consejo_noche', 'a long boardroom table seen from the far end, a dozen men in dark suits seated in silhouette against tall windows over a city at dusk, one empty chair at the head, tense stillness', at='el consejo de administración'),
    ai('reloj_sala', 'close-up of a wristwatch on the wrist of a man in a dark suit resting on a polished boardroom table, papers and a fountain pen beside it, low golden light', at='se encierra en una sala'))
NAR("Al frente de la mesa hay un hombre que lleva solo dieciséis días en el cargo. Tiene una cifra apuntada. Y cuando la dice en voz alta, nadie en la sala habla.",
    ph('José Ignacio Goirigolzarri', at='un hombre que lleva solo', lt=['José Ignacio Goirigolzarri', 'Presidente de Bankia desde mayo de 2012', 'banca'], lugar='goiri'),
    ai('papel_cifra', 'a single sheet of paper slid across a dark boardroom table by a hand, other hands frozen around it, dramatic overhead light, the paper blank and glowing', at='Tiene una cifra apuntada'),
    ai('silencio_mesa', 'men in suits around a boardroom table frozen in silence, seen from behind and in shadow, one man covering his mouth with his hand, cold window light', at='nadie en la sala habla'))
DAT("Diecinueve mil millones de euros. Es lo que el banco tiene que pedir al Estado para no hundirse. El mayor rescate de la historia de España.",
    cd(dict(type='counter', **{'from': 0}, to=19000, label='millones de euros que pide Bankia al Estado', suffix=' M€'), at='Diecinueve mil millones'),
    ai('oro_derrumbe', 'a tall stack of gold coins collapsing in slow motion on a dark marble floor, coins scattering toward the viewer, emerald green rim light, cinematic', at='para no hundirse'))
NEW("Esa misma tarde, el banco rehace sus cuentas del año anterior. Donde decía que había ganado trescientos nueve millones, ahora reconoce que perdió casi tres mil. Y el consejo entero, salvo el presidente y el consejero delegado, dimite.",
    cd(dict(type='split', left=dict(name='Cuentas de 2011 · febrero', lines=['+309 millones', 'de beneficio']), right=dict(name='Cuentas de 2011 · 25 de mayo', lines=['−2.979 millones', 'de pérdidas'])), at='Donde decía'),
    ai('sillas_vacias', 'a boardroom after everyone has left, chairs pushed back at odd angles, coffee cups and scattered papers, the city lights glowing outside, deep green shadows', at='dimite'))
NAR("Pero lo más increíble no es la cifra. Es la fecha. Porque apenas diez meses antes, este mismo banco había tocado la campana en la Bolsa de Madrid. Y trescientas cuarenta y siete mil personas le habían confiado sus ahorros.",
    ai('campana_bolsa', 'a polished bronze ceremonial bell being struck inside an ornate nineteenth-century stock exchange hall, confetti-like light, crowd of silhouettes applauding, golden glow', at='había tocado la campana'),
    ph('Palacio de la Bolsa de Madrid', at='la Bolsa de Madrid', lt=['Palacio de la Bolsa', 'Madrid'], lugar='bolsa'),
    ai('cola_oficina', 'ordinary people, retirees and young couples, waiting in line inside a busy bank branch in Spain, seen from behind, warm afternoon light through the glass, hopeful atmosphere', at='trescientas cuarenta y siete mil personas'))
DAT("Tres con setenta y cinco euros. A ese precio se vendió cada acción aquel verano. El jueves veinticuatro de mayo, la víspera del rescate, la acción cerró a uno con cincuenta y siete. Ya había perdido más de la mitad. Y lo peor aún no había llegado.",
    BOLSA(1.57, 'cierre de Bankia · 24 de mayo de 2012', at='uno con cincuenta y siete', frm=3.75))
NEW("[pause] ¿Cómo puede un banco que sale a bolsa como una cuestión de Estado necesitar el mayor rescate de la historia en menos de un año? ¿Quién sabía lo que había dentro? Y la pregunta que todavía hoy no tiene una respuesta cómoda: ¿quién pagó la factura?",
    ai('pasillo_sombra', 'a man in a suit walking away down a long dark marble corridor of a bank headquarters, his long shadow cast toward the viewer, emerald light at the end', at='Quién sabía'),
    ai('cartera_vacia', 'an old leather wallet lying open and empty on a kitchen table beside a bank statement and reading glasses, early morning light, Spain', at='quién pagó la factura'))
NAR("Esta es la historia de los diez meses que hundieron a Bankia. Contada día a día, desde la campana hasta el rescate. Y de lo que vino después: los tribunales, la cárcel y una sentencia que nadie esperaba.",
    DIA(310, 310, 'del toque de campana al rescate', at='los diez meses'),
    ai('mazo_sombra', 'the shadow of iron prison bars falling across a marble courthouse floor, a single beam of light, dust in the air, cinematic', at='la cárcel'))
T('Bankia', 'Salió a bolsa. Diez meses después pidió el rescate', secs=5.5, sting='tema', text='[dramatically] Bankia. Diez meses.', chapter=False)

# ---------------- I · SIETE CAJAS Y UNA TORRE ----------------
T('Siete cajas y una torre', '2010', num='I', secs=6.0, sting='tema')
B('fondo')
NEW("Para entender cómo se llegó a esa sala, hay que retroceder dos años. Dos mil diez. La burbuja inmobiliaria ha reventado y las cajas de ahorros, las entidades que durante un siglo guardaron el dinero de los españoles, están llenas de pisos que nadie compra y de préstamos a promotores que ya no pueden pagar.",
    ai('grua_parada', 'abandoned tower cranes over a half-built housing development on the outskirts of a Spanish city at dusk, empty concrete skeletons, long shadows, melancholic', at='La burbuja inmobiliaria ha reventado'),
    ai('libreta_caja', 'an old-fashioned savings passbook and a few coins on a wooden counter of a traditional Spanish savings bank, warm nostalgic light, hands of an elderly customer', at='las cajas de ahorros'),
    ai('bloques_vacios', 'rows of brand new empty apartment blocks with no lights on at night, a single streetlight, unfinished landscaping, ghost town atmosphere', at='llenas de pisos que nadie compra'))
DAT("Para medir la burbuja basta un dato. En dos mil seis se empezaron a construir en España más viviendas que en Alemania, Francia e Italia juntas. Y una parte enorme de ese ladrillo se pagó con crédito de las cajas.",
    ai('obra_europa', 'endless rows of identical half-built apartment blocks stretching to the horizon under a stormy sky, tower cranes, bare concrete skeletons, aerial view, cinematic', at='Para medir'),
    cd(dict(type='kw', word='MÁS VIVIENDAS', sub='que Alemania, Francia e Italia juntas · 2006'), at='más viviendas'))
NEW("Hasta que en septiembre de dos mil ocho quiebra Lehman Brothers en Nueva York. El grifo del dinero internacional se cierra de golpe. Y las cajas, que pedían prestado en esos mercados para prestar a los promotores, se quedan con dos cosas: pisos sin vender y deudas que pagar.",
    ph('Lehman Brothers headquarters New York 2008', at='Lehman Brothers', lt=['Sede de Lehman Brothers', 'Nueva York'], lugar='lehman'),
    ai('grifo_cerrado', 'a heavy brass tap on a marble bank wall turned shut, the last drop of liquid gold falling into an empty basin, dramatic close-up', at='El grifo'),
    ai('pisos_vacios', 'a brand-new empty apartment building at dusk with every window dark, unsold, weeds growing at the entrance, lonely streetlight', at='pisos sin vender'))
DAT("Una caja de ahorros no tenía dueños ni accionistas. Sus consejos se repartían entre gobiernos autonómicos, ayuntamientos, partidos y sindicatos. Y en dos mil diez, el Banco de España las empuja a fusionarse para sobrevivir.",
    ai('consejo_caja', 'a crowded old-fashioned boardroom of a savings bank with wood panelling, men of different ages arguing across the table, seen from behind, cigarette smoke and warm lamplight', at='Sus consejos se repartían'),
    ph('Banco de España Madrid edificio', at='el Banco de España', lt=['Banco de España', 'Madrid'], lugar='bde'))
DAT("La más grande de todas tenía casi tres siglos de historia. Caja Madrid nació del Monte de Piedad que fundó el sacerdote Francisco Piquer en mil setecientos dos, para prestar a los pobres sin usura. En dos mil nueve manejaba unos ciento ochenta mil millones de euros.",
    ph('Monte de Piedad Madrid Descalzas', at='Monte de Piedad', lt=['Antiguo Monte de Piedad', 'Madrid'], lugar='cajamadrid'),
    ai('monte_piedad', 'an eighteenth-century Madrid pawn office interior, poor families in period clothes handing over bundles to a clerk behind a wooden counter by candlelight, oil painting, faces in shadow', at='para prestar a los pobres'))
NAR("La mayor de todas esas uniones nace el treinta de julio de dos mil diez. Siete cajas firman un contrato de integración. Dos gigantes, Caja Madrid y Bancaja. Y cinco pequeñas: la Caja Insular de Canarias, Caja de Ávila, Caixa Laietana, Caja Segovia y Caja Rioja.",
    ai('firma_siete', 'seven fountain pens laid side by side on a long contract on a polished table, hands reaching for them, dramatic overhead light, emerald and gold tones', at='Siete cajas firman'),
    cd(dict(type='kw', word='CAJA MADRID', sub='nacida del Monte de Piedad de 1702'), at='Caja Madrid'),
    ph('Bancaja sede Valencia', at='Bancaja', lt=['Bancaja', 'Valencia'], lugar='bancaja'),
    cd(dict(type='list', header='Las siete cajas de Bankia', items=[('Caja Madrid', 'Madrid'), ('Bancaja', 'Valencia'), ('Caja Insular de Canarias', 'Las Palmas'), ('Caja de Ávila · Caja Segovia', 'Castilla y León'), ('Caixa Laietana · Caja Rioja', 'Mataró · Logroño')]), at='cinco pequeñas'))
NEW("Lo llaman fusión fría. Cada caja sigue existiendo, pero el negocio pasa a una sociedad central: el Banco Financiero y de Ahorros, que todo el mundo conocerá por sus siglas, BFA. Para arrancar, el Estado le presta cuatro mil cuatrocientos sesenta y cinco millones de euros del fondo de rescate bancario, el FROB.",
    ai('engranajes', 'seven old bronze gears of different sizes locking together into one large machine in a dark vault, sparks and dust, green light, cinematic', at='Lo llaman fusión fría'),
    cd(dict(type='counter', **{'from': 0}, to=4465, label='millones prestados por el FROB a BFA · diciembre de 2010', suffix=' M€'), at='cuatro mil cuatrocientos sesenta y cinco millones'))
NAR("Sobre el papel, la idea tenía lógica: siete entidades débiles juntas pesan más que por separado. Pero dentro de ese gigante convivían siete culturas, siete consejos, siete redes de oficinas solapadas y, sobre todo, siete carteras de préstamos al ladrillo. Juntarlas no las hacía más sanas. Solo las hacía más grandes.",
    ai('siete_barcos', 'seven old wooden ships lashed together with ropes on a dark stormy sea, lanterns swinging, one already listing, epic oil painting, emerald and gold light', at='siete entidades débiles juntas'),
    ai('ladrillos_pila', 'a giant unstable tower of red bricks stacked inside a grand marble bank hall, workers in suits looking up at it, cracks forming, dramatic chiaroscuro', at='Solo las hacía más grandes'))
DAT("El nuevo grupo arranca con más de trescientos mil millones de euros en balance. Es el tercer banco de España. Y tiene un presidente con un currículum que pocos banqueros del mundo pueden igualar.",
    ai('torre_noche', 'two leaning glass office towers facing each other over a busy roundabout in Madrid at night, light trails of cars below, emerald and gold reflections, cinematic wide shot', at='el tercer banco de España'))
NAR("Un gigante, sí. Pero con pies de barro. Y dentro de ese barro había una pregunta que nadie quería hacer en voz alta: cuánto valía de verdad todo el ladrillo que las cajas guardaban en sus balances.",
    ai('pies_barro', 'a colossal golden statue of a banker standing on cracked crumbling clay feet, small figures below looking up, chiaroscuro', at='Un gigante'),
    ai('ladrillo_balanza', 'a stack of red bricks piled on one side of an old brass scale weighing against gold coins, dim vault', at='cuánto valía'))
NAR("Rodrigo Rato. Vicepresidente económico en los gobiernos de José María Aznar. Director gerente del Fondo Monetario Internacional entre dos mil cuatro y dos mil siete. Ahora preside el grupo entero.",
    ph('Rodrigo Rato', at='Rodrigo Rato', lt=['Rodrigo Rato', 'Presidente de Caja Madrid, BFA y Bankia (2010-2012)', 'banca'], lugar='rato'),
    ph('International Monetary Fund headquarters Washington', at='Fondo Monetario Internacional', lt=['Sede del FMI', 'Washington'], lugar='fmi'),
    ai('despacho_rato', 'a powerful executive office high in a glass tower, a lone man in a dark suit standing at the window with his back to the viewer, looking out over Madrid at sunset', at='Ahora preside el grupo entero'))
PRE("Su llegada no fue sencilla. Durante casi un año, el Partido Popular de Madrid libró una guerra interna por el control de la caja. La presidenta de la Comunidad, Esperanza Aguirre, quería a su número dos, Ignacio González. El alcalde, Alberto Ruiz-Gallardón, se oponía. Y el líder nacional del partido lo dijo en televisión.",
    ph('Esperanza Aguirre', at='Esperanza Aguirre', lt=['Esperanza Aguirre', 'Presidenta de la Comunidad de Madrid (2003-2012)', 'gobierno'], lugar='aguirre'),
    ph('Alberto Ruiz-Gallardón', at='Alberto Ruiz-Gallardón', lt=['Alberto Ruiz-Gallardón', 'Alcalde de Madrid (2003-2011)', 'gobierno'], lugar='gallardon'),
    ai('pulso_mesa', 'two hands in dark suit sleeves locked in an arm-wrestle on a polished table under a single hanging lamp, other men watching in shadow, tense, oil painting', at='una guerra interna'))
RAJ("Si yo tuviera que nombrar a un presidente de Caja Madrid, ése sería Rato.",
    cd(dict(type='quote', text='Si yo tuviera que nombrar a un presidente de Caja Madrid, ése sería Rato.', attrib='Mariano Rajoy · entrevista en Antena 3, octubre de 2009'), at='Si yo tuviera que nombrar'))
DAT("El veintiocho de enero de dos mil diez, Rato es elegido presidente de Caja Madrid por unanimidad. Sustituye a Miguel Blesa, que llevaba catorce años al frente.",
    ai('votacion_manos', 'a row of raised hands voting around a long wooden boardroom table in an old savings bank headquarters, warm lamplight, seen from behind, unanimous', at='por unanimidad'))
NEW("A su lado, como vicepresidente, el hombre fuerte de Bancaja: José Luis Olivas, que había sido presidente de la Generalitat Valenciana. Y como consejero delegado, Francisco Verdú. Madrid y Valencia, los dos grandes feudos del ladrillo, en una misma mesa.",
    ph('José Luis Olivas', at='José Luis Olivas', lt=['José Luis Olivas', 'Vicepresidente de Bankia · expresidente de Bancaja', 'banca'], lugar='olivas'),
    ai('mapa_feudos', 'an old map of Spain spread on a dark table lit by a desk lamp, two heavy brass paperweights placed on Madrid and Valencia, a hand moving one of them, chiaroscuro', at='Madrid y Valencia'))
PRE("En la prensa económica se repite una frase: nace un gigante. Pero dentro del Banco de España hay quien no lo ve así. Y lo deja por escrito.",
    ai('periodicos', 'a stack of morning newspapers being cut open with a knife on a kiosk counter in Madrid at dawn, steam from a coffee cup, no readable headlines', at='nace un gigante'),
    ai('carta_sobre', 'a sealed manila envelope lying alone on a desk inside a dark government office, a beam of light from a window falling on it, ominous', at='Y lo deja por escrito'))

# ---------------- II · EL INSPECTOR ----------------
M('tension', 6)
T('El inspector', 'Abril y mayo de 2011', num='II', secs=6.0, sting='tema')
DOC("Real Decreto-ley de dieciocho de febrero de dos mil once, para el reforzamiento del sistema financiero. Capital principal mínimo del ocho por ciento. Del diez por ciento para las entidades que dependan de los mercados mayoristas y no tengan al menos un veinte por ciento de su capital en manos privadas. Plazo: treinta de septiembre.",
    cd(dict(type='doc', title='Real Decreto-ley 2/2011', lines=['para el reforzamiento del sistema financiero', 'Capital principal: 8 % · 10 % sin inversores privados'], source='Boletín Oficial del Estado · 19 de febrero de 2011'), at='Real Decreto-ley de dieciocho de febrero'))
DAT("El diez de marzo, el Banco de España comunica a doce entidades que les falta capital. Unos quince mil millones de euros para todo el sector. En la lista está BFA.",
    cd(dict(type='counter', **{'from': 0}, to=12, label='entidades a las que les falta capital · 10 de marzo de 2011'), at='a doce entidades'),
    ai('lista_nombres', 'a hand running a finger down a typed list on official letterhead in a dark office, a red pencil mark on one line, extreme close-up, letters blurred and unreadable', at='En la lista está BFA'))
B('tension')
NAR("Primavera de dos mil once. Para BFA quedan dos caminos. Salir a bolsa y captar dinero de inversores. O ser intervenida.",
    ai('cruce_caminos', 'a man in a suit standing at a fork in a dark rain-soaked road at night, one path lit gold, the other disappearing into darkness, seen from behind, cinematic', at='quedan dos caminos'),
    cd(dict(type='versus', left=dict(name='Salir a bolsa', lines=['captar capital de inversores', 'mantener el control']), right=dict(name='Ser intervenida', lines=['el Estado entra', 'los gestores salen'])), at='Salir a bolsa y captar'))
NEW("La fórmula que se elige tiene truco. No saldrá a bolsa todo el grupo. Se crea un banco nuevo, Bankia, que se queda con el negocio de las oficinas, los clientes y los depósitos. Y la matriz, BFA, se queda con buena parte de lo más tóxico: el suelo, los préstamos dudosos y las participaciones en otras empresas.",
    ai('dos_cajas_fuertes', 'two steel bank vaults side by side in a dark basement, one gleaming and clean with gold light, the other rusted and leaking dark water, dramatic contrast', at='La fórmula que se elige tiene truco'),
    cd(dict(type='list', header='La estructura de doble banco', items=[('Bankia', 'oficinas, clientes y depósitos · sale a bolsa'), ('BFA, la matriz', 'suelo, préstamos dudosos y participadas · se queda fuera')]), at='Se crea un banco nuevo, Bankia'))
DAT("A esto se le llamó estructura de doble banco. Bankia sería el escaparate. BFA, la trastienda.",
    ai('escaparate', 'a brightly lit luxurious shop window at night on a Madrid street, and behind it through a half-open door a dark cluttered storeroom piled with boxes, chiaroscuro', at='Bankia sería el escaparate'))
NEW("Para que te hagas una idea: es como poner en la calle una tienda reluciente y guardar los muebles rotos en el almacén de atrás. El cliente solo ve el escaparate.",
    ai('tienda_almacen', 'a gleaming lit shop window on a Madrid street at night, and through a half-open back door a dark storeroom full of broken furniture, cinematic', at='Para que te hagas'))
NAR("Y aquí entra en escena un hombre que casi nadie conocía. José Antonio Casaus, jefe del equipo de inspectores del Banco de España que vigila día a día al grupo. Entre abril y mayo de dos mil once envía cuatro correos electrónicos a sus superiores.",
    ai('inspector_pantalla', 'a middle-aged man in shirtsleeves typing at a computer late at night in a dim office, only the glow of the screen on his tired face seen in profile and shadow, stacks of files around', at='José Antonio Casaus'),
    ai('correo_enviar', 'close-up of a finger pressing a key on an old office keyboard in the dark, the cold blue glow of a monitor, tension', at='cuatro correos electrónicos'))
DOC("Correo de dieciséis de mayo de dos mil once. El inspector describe a Bankia con una debilísima y decreciente capacidad para generar resultados. Y añade que el grupo tiene un consejo muy politizado y poco profesional.",
    cd(dict(type='doc', title='Correo interno del Banco de España', lines=['«debilísima y decreciente capacidad', 'para generar resultados»', '«consejo muy politizado y poco profesional»'], source='José Antonio Casaus, inspector · 16 de mayo de 2011'), at='Correo de dieciséis de mayo'))
CAS("La salida a bolsa con la estructura de doble banco, sin hacer cambios estructurales, sólo es una bombona de oxígeno.",
    cd(dict(type='quote', text='La salida a bolsa con la estructura de doble banco (…) sólo es una bombona de oxígeno.', attrib='José Antonio Casaus, inspector del Banco de España · correo de 2011'), at='bombona de oxígeno'))
NAR("Una bombona de oxígeno. Es decir: aire para aguantar unos meses, no una cura. Casaus no estaba diciendo que la salida a bolsa fuera ilegal. Estaba diciendo que no resolvía el problema. Que el enfermo seguía enfermo.",
    ai('bombona', 'a hospital oxygen cylinder standing next to an empty bed in a dark ward, a single lamp, the gauge needle near empty, symbolic, oil painting', at='aire para aguantar unos meses'))
NEW("Casaus propone otra salida: que un gran banco, preferiblemente extranjero, absorba al grupo. Y apunta por qué cree que no ocurrirá. Según escribió, los políticos que gestionan la entidad no querrán perder su herramienta de financiación.",
    ai('banco_extranjero', 'a sleek foreign bank tower of glass in a northern European city under grey sky, reflected in a puddle, cold and distant', at='preferiblemente extranjero'),
    ai('ajedrez', 'a hand in a dark suit sleeve moving a chess piece on a board set on a boardroom table, other pieces fallen, dramatic chiaroscuro, emerald and gold', at='herramienta de financiación'))
NAR("Sus correos llegan a su jefe de grupo. Lo que pasó después lo discutirían durante años los tribunales. Ante el juez, quien los recibió los llamó meras opiniones. El gobernador aseguró que nunca le llegaron. La operación siguió adelante.",
    ai('carpeta_cerrada', 'a hand closing a thick file folder and placing it on top of a tall stack in a dim archive room, dust floating in a shaft of light', at='meras opiniones'),
    ai('pasos_escalera', 'men in suits walking briskly up a grand marble staircase of an official building, seen from below and behind, motion blur, determined', at='La operación siguió adelante'))
PRE("En los despachos de Madrid se decía que la salida a bolsa de Bankia era una cuestión de Estado. Si fracasaba, el mensaje a los mercados sería terrible: que el sistema financiero español no podía sostenerse solo.",
    ph('Palacio de la Moncloa', at='En los despachos de Madrid', lt=['Palacio de la Moncloa', 'Madrid'], lugar='moncloa'),
    ai('mercados_pantallas', 'traders silhouetted against walls of glowing screens in a dark trading room, red light spilling across their shoulders, motion and tension', at='el mensaje a los mercados'))
PRE("Y mientras tanto, en la calle, el país hierve. El quince de mayo de dos mil once, miles de personas acampan en la Puerta del Sol. Una de sus pancartas se repetiría por toda España: no somos mercancía en manos de políticos y banqueros.",
    ph('Acampada Sol 15M Madrid 2011', at='acampan en la Puerta del Sol', lt=['Puerta del Sol, Madrid', 'Mayo de 2011'], lugar='sol15m'),
    ai('plaza_noche', 'a vast crowd of young people camped in a city square at night under tarps and lights, banners without readable text, warm glow, seen from above, oil painting', at='en manos de políticos y banqueros'))
NEW("En las pancartas de Sol hay una frase que se repite. No somos mercancía en manos de políticos y banqueros. Muy cerca de allí, en las oficinas del nuevo banco, se prepara la mayor colocación de acciones del año.",
    ph('Acampada Sol 15M Madrid 2011', at='En las pancartas', lt=['Acampada del 15-M', 'Puerta del Sol, Madrid'], lugar='sol15m'),
    cd(dict(type='quote', text='No somos mercancía en manos de políticos y banqueros', attrib='Lema de Democracia Real Ya · 2011'), at='No somos'),
    ai('oficina_preparativos', 'inside a bank branch after hours, stacks of glossy brochures being unpacked onto desks, green lamps, figures seen from behind', at='Muy cerca'))
NAR("Así que el veintinueve de junio de dos mil once, la Comisión Nacional del Mercado de Valores registra el folleto de la oferta. Cientos de páginas. Cifras, riesgos, cuentas. Un documento que, años después, el Tribunal Supremo examinaría frase a frase.",
    ph('Comisión Nacional del Mercado de Valores sede Madrid', at='la Comisión Nacional del Mercado de Valores', lt=['CNMV', 'Madrid'], lugar='cnmv'),
    ai('folleto_grueso', 'a thick bound prospectus document dropped heavily onto a desk, pages fluttering, dust in a shaft of light, no readable text', at='registra el folleto'),
    ai('lupa_juez', 'a judge in a black robe seen from behind, turning a page of a thick document under a green banker lamp in a dark wood-panelled chamber', at='frase a frase'))
NEW("[softly] En ese folleto había un número. Un beneficio. Y ese número iba a viajar a trescientas cuarenta y siete mil casas.",
    ai('numero_luz', 'a single sheet of paper glowing on a dark desk as if lit from within, light spilling out across the room, mysterious, no readable text', at='En ese folleto había un número'),
    ai('ventanas_casas', 'night view of an ordinary Spanish apartment building with dozens of lit windows, families visible as tiny silhouettes inside, warm and fragile', at='trescientas cuarenta y siete mil casas'))
M('tension', 5)
