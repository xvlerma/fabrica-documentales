# -*- coding: utf-8 -*-
# «Bankia» · parte 3: la factura, el juicio y el final
from lib import *

# ---------------- VI · LA FACTURA ----------------
M('tension', 6)
T('La factura', '2012 · 2013', num='VI', secs=6.0, sting='tema')
B('drama')
NEW("Para entender quién pagó, hay que hablar de un producto con nombre amable: las participaciones preferentes. Durante años, las cajas que formaron Bankia las vendieron en sus oficinas como si fueran depósitos a plazo. Pero no lo eran.",
    ai('preferentes_mesa', 'an elderly woman at a savings bank desk being handed a contract, the employee pointing where to sign, warm deceptive light, seen from the side, faces turned away', at='las participaciones preferentes'),
    cd(dict(type='kw', word='PREFERENTES', sub='un producto complejo y perpetuo vendido como si fuera un depósito'), at='como si fueran depósitos a plazo'))
DAT("Las preferentes eran deuda perpetua de la entidad. Sin fecha de devolución y sin garantía. Los afectados por las preferentes y la deuda subordinada de las cajas de Bankia rondaban los trescientos mil.",
    cd(dict(type='counter', **{'from': 0}, to=300000, label='afectados por preferentes y deuda subordinada de las cajas de Bankia'), at='rondaban los trescientos mil'))
NEW("Pongamos un ejemplo. Una jubilada con veinte mil euros ahorrados va a su oficina de siempre. Le ofrecen un producto que paga más que un depósito. Firma. Lo que no le explican es que, si la entidad se hunde, ese dinero puede quedar atrapado sin fecha de salida. Eso es lo que descubrieron, de golpe, cientos de miles de familias.",
    AIR('preferentes_mesa', at='Pongamos un ejemplo'),
    ai('cocina_noche', 'an elderly woman sitting alone at her kitchen table late at night with a pile of bank letters and a calculator, a single lamp, her face hidden in her hands, seen from the side in shadow', at='cientos de miles de familias'))
NAR("En los juzgados aparecieron historias difíciles de creer. Clientes que no sabían leer ni escribir y que habían firmado igualmente. Personas de más de ochenta años con un producto perpetuo. Ahorros de toda una vida, atrapados en un papel que no se podía vender.",
    ai('firma_temblorosa', 'an elderly wrinkled hand signing a long contract with a trembling pen at a bank desk, face out of frame, warm lamp light', at='Clientes que no'),
    ai('papel_atrapado', 'a savings passbook locked inside a small glass case with chains around it, dust, single beam of light', at='Ahorros de toda'))
NAR("Como condición del rescate europeo, Bruselas impone en dos mil trece que esos inversores asuman pérdidas. Sus preferentes se convierten a la fuerza en acciones de Bankia, con una quita. Y por las calles de media España empieza a verse algo que no se había visto nunca: jubilados manifestándose frente a los bancos.",
    ph('Berlaymont building European Commission Brussels', at='Bruselas impone', lt=['Comisión Europea', 'Bruselas'], lugar='berlaymont'),
    ph('manifestación preferentes', at='jubilados manifestándose', lt=['Protesta de afectados por las preferentes', 'España, 2013'], lugar='preferentes'),
    ai('pancarta_jubilados', 'elderly protesters with raised fists and whistles marching in front of a bank branch in a Spanish city on a cold morning, seen from behind and in profile, banners blank, determined', at='frente a los bancos'))
NEW("Se abre un arbitraje para quienes demuestren que se les vendió un producto que no entendían. Se presentan más de ciento ochenta mil solicitudes. Unas ciento treinta y siete mil son aceptadas. El resto, a los tribunales.",
    ai('cola_arbitraje', 'a long line of elderly people holding folders of documents waiting in a bank branch corridor, seen from behind, patient and weary, cold light', at='Se abre un arbitraje'),
    cd(dict(type='split', left=dict(title='Solicitudes de arbitraje', lines=['182.951']), right=dict(title='Aceptadas', lines=['137.359'])), at='Unas ciento treinta y siete mil'))
DAT("Bankia nunca emitió preferentes: las heredó de las cajas. Pero fue Bankia quien tuvo que pagar. Entre arbitrajes y sentencias, acabó devolviendo unos dos mil ochocientos millones de euros a sus titulares.",
    cd(dict(type='counter', **{'from': 0}, to=2800, label='millones devueltos a titulares de preferentes y subordinadas', suffix=' M€'), at='unos dos mil ochocientos millones'))
DAT("Y los accionistas de la salida a bolsa lo ven desde la primera fila. En abril de dos mil trece, el FROB reduce el valor nominal de cada acción a un céntimo y agrupa cien acciones antiguas en una nueva. Justo antes, en marzo, la acción comprada a tres con setenta y cinco rondaba los quince céntimos. Una pérdida del noventa y seis por ciento.",
    BOLSA(0.15, 'cotización de Bankia · marzo de 2013', at='rondaba los quince céntimos', frm=3.75),
    cd(dict(type='kw', word='−96 %', sub='lo que perdió una acción comprada en la salida a bolsa'), at='Una pérdida del noventa y seis por ciento'))
NAR("Mil euros invertidos aquel veinte de julio se habían convertido en unos cuarenta. Para muchas familias no era dinero para especular. Eran los ahorros de una vida.",
    ai('billete_quema', 'a single banknote slowly burning at the edges on a dark wooden table, embers floating up, close-up, no readable denomination', at='en unos cuarenta'),
    ai('foto_familia', 'an old framed family photograph standing on a sideboard next to a pile of opened bank letters, dim evening light in a modest Spanish home, faces not visible', at='Eran los ahorros de una vida'))
DAT("Mientras tanto, el banco se transforma por dentro. En dos mil doce el grupo pierde unos diecinueve mil millones de euros. Traspasa a la Sareb, el llamado banco malo, diecinueve mil trescientos cuarenta y siete millones en pisos, suelo y préstamos. Y su plan anuncia más de seis mil despidos, el veintiocho por ciento de la plantilla, y el cierre de unas mil cien oficinas.",
    ai('carpetas_camion', 'workers loading hundreds of document boxes onto a truck at night from the back door of a bank building, harsh work lights, rain', at='la Sareb'),
    ai('persiana_baja', 'the metal shutter of a small bank branch being pulled down for the last time on a quiet Spanish street at dusk, a hand on the shutter, melancholic', at='el cierre de unas mil cien oficinas'))
NEW("Goirigolzarri tiene un encargo: que Bankia sobreviva para que el Estado pueda recuperar algo algún día. Muchos analistas de la época no le daban ninguna posibilidad.",
    ai('timon_tormenta', 'a lone figure at the helm of an old ship in a violent storm at night, waves crashing over the deck, a faint gold light on the horizon, oil painting, epic', at='que Bankia sobreviva'))
NEW("Pero la pregunta de fondo seguía en el aire. Si las cuentas con las que Bankia salió a bolsa no reflejaban la realidad, ¿alguien lo sabía? ¿Alguien iba a responder por ello?",
    ai('balanza_justicia', 'a bronze statue of blind Justice holding scales in a dark courthouse hall, a beam of cold light falling on the scales, dust in the air', at='Alguien iba a responder por ello'))

NAR("Antes de seguir, una pregunta para ti. ¿Quién crees que debería haber respondido ante la justicia? Déjalo en los comentarios. Porque lo que decidieron los tribunales sorprendió a casi todo el mundo.",
    ai('balanza_niebla', 'golden scales of justice standing alone in thick fog inside an empty courtroom, dramatic backlight', at='Antes de seguir'))
# ---------------- VII · EL JUICIO ----------------
M('tension', 6)
T('El juicio', '2012 · 2022', num='VII', secs=6.0, sting='tema')
B('juicio')
NAR("Junio de dos mil doce. Un partido político, UPyD, presenta una querella ante la Audiencia Nacional por la salida a bolsa. Poco después se suma una iniciativa ciudadana financiada con pequeñas donaciones, el grupo conocido como Quince eme pa Rato. El juez Fernando Andreu imputa a Rato y a una treintena de antiguos consejeros.",
    ph('Audiencia Nacional Madrid', at='la Audiencia Nacional', lt=['Audiencia Nacional', 'Madrid'], lugar='audiencia'),
    ai('querella_mesa', 'a thick legal complaint document stamped and placed on a counter of a court registry by a hand, an official in shadow behind the glass, cold light, no readable text', at='presenta una querella'),
    ai('donaciones', 'many hands of different ages each dropping a coin into a large glass jar on a table at a neighborhood assembly, warm light, solidarity', at='financiada con pequeñas donaciones'))
NEW("Para la acusación, la idea era sencilla. Si las cuentas de dos mil once tuvieron que rehacerse con casi tres mil millones de pérdidas pocas semanas después, esas pérdidas ya estaban ahí cuando se vendieron las acciones. Para las defensas, todo lo contrario: las cuentas cumplían las normas, estaban supervisadas, y lo que hundió al banco fue la crisis y las nuevas exigencias del Gobierno.",
    cd(dict(type='versus', left=dict(name='Acusación', lines=['las pérdidas ya existían', 'cuando se vendieron las acciones']), right=dict(name='Defensas', lines=['cuentas supervisadas y legales', 'lo hundieron la crisis y los decretos'])), at='Para la acusación, la idea era sencilla'))
DOC("Diciembre de dos mil catorce. Dos inspectores del Banco de España, nombrados peritos por el juez, entregan su informe. Concluyen que las cuentas de dos mil once no reflejaban la imagen fiel de la entidad y que parte de los deterioros eran anteriores a la reformulación.",
    cd(dict(type='doc', title='Informe pericial', lines=['Las cuentas de 2011 no expresaban', 'la imagen fiel de BFA y Bankia'], source='Peritos del Banco de España · Audiencia Nacional, diciembre de 2014'), at='entregan su informe'),
    ai('perito_papeles', 'two men in shirtsleeves at a long table covered with spreadsheets and binders in a windowless room, one pointing at a page, harsh overhead lamp, seen from behind', at='Dos inspectores del Banco de España'))
NEW("Mientras la vía penal avanza despacio, miles de pequeños accionistas eligen otro camino: la vía civil. Demandan a Bankia para que se anule la compra de sus acciones. Y en enero de dos mil dieciséis llega el golpe definitivo.",
    ph('Tribunal Supremo Madrid', at='en enero de dos mil dieciséis', lt=['Tribunal Supremo', 'Madrid'], lugar='supremo'),
    ai('abogado_maletin', 'a lawyer in a dark coat carrying a thick briefcase climbing the steps of a neoclassical courthouse in Madrid on a winter morning, seen from behind', at='la vía civil'))
DOC("El Pleno de la Sala de lo Civil del Tribunal Supremo confirma que el folleto contenía graves inexactitudes. Según el alto tribunal, los pequeños inversores compraron valores de una entidad al borde de la insolvencia, con pérdidas multimillonarias no confesadas.",
    cd(dict(type='quote', text='Compraron valores de una entidad al borde de la insolvencia y pérdidas multimillonarias no confesadas.', attrib='Tribunal Supremo, Sala de lo Civil · sentencias de 3 de febrero de 2016'), at='al borde de la insolvencia'))
DOC("Y añade algo que apunta más arriba. Los pequeños inversores no tenían medios para conocer la verdadera situación del banco. Y el folleto había sido autorizado por un organismo público, lo que contribuyó a generar confianza en ellos.",
    AIR('lupa_juez', at='Los pequeños inversores no tenían medios'))
DAT("Bankia decide devolver a todos los minoristas de la salida a bolsa su inversión íntegra, más un uno por ciento de interés anual. En pocos meses ya ha devuelto unos mil doscientos millones de euros a más de ciento noventa mil personas.",
    cd(dict(type='counter', **{'from': 0}, to=190000, label='pequeños accionistas que recuperan su dinero · 2016', prefix='+'), at='más de ciento noventa mil personas'),
    ai('carta_buzon', 'an elderly man opening a letter by his mailbox in the hallway of a Spanish apartment building, relief in his posture, warm morning light, seen from behind', at='su inversión íntegra'))
NAR("Pero hay un detalle que muchos pasaron por alto. El dinero para devolver esas acciones salió de un banco que ya era, en su mayoría, del Estado. Es decir, en buena parte, de todos los contribuyentes.",
    ai('monedas_mano', 'hands of many different people pouring coins into one large pile on a dark marble floor, the pile glowing gold, symbolic, top-down view', at='de todos los contribuyentes'))
B('ironia')
NEW("Y en medio de todo esto, estalla otro escándalo. Otoño de dos mil catorce. Se descubre que durante años decenas de consejeros y directivos de Caja Madrid y Bankia usaron tarjetas de crédito que no aparecían en la contabilidad oficial. Las llamarán tarjetas black.",
    ai('tarjeta_mantel', 'a matte black credit card lying on a white tablecloth in a luxury restaurant next to a glass of wine, candlelight, close-up, no readable text or logos', at='tarjetas black'),
    ai('compras_lujo', 'a hand in a dark suit sleeve sliding a black card across the glass counter of a jewelry shop, gold watches under the glass, warm seductive light, no readable text', at='usaron tarjetas de crédito'))
DAT("Sesenta y cinco condenados en dos mil diecisiete. Unos doce millones de euros gastados entre dos mil tres y dos mil doce. Joyas, viajes, restaurantes, ropa. Había usuarios propuestos por el Partido Popular, por el PSOE, por Izquierda Unida, por los sindicatos y por la patronal.",
    cd(dict(type='counter', **{'from': 0}, to=12, label='millones de euros gastados con las tarjetas black · 2003-2012', suffix=' M€'), at='Unos doce millones de euros'),
    cd(dict(type='list', header='Tarjetas black · sentencia de 2017', items=[('Condenados', '65'), ('Miguel Blesa', '6 años de prisión'), ('Rodrigo Rato', '4 años y medio')]), at='Sesenta y cinco condenados'))
DAT("Según la sentencia, los consejeros propuestos por el PP gastaron más de dos coma nueve millones. Los propuestos por el PSOE, uno coma tres. Los de Izquierda Unida, más de ochocientos mil euros. El resto, directivos y representantes de otras organizaciones.",
    cd(dict(type='list', header='Gasto con las tarjetas black por origen del consejero', items=[('Propuestos por el PP', 'más de 2,9 millones'), ('Propuestos por el PSOE', '1,34 millones'), ('Propuestos por IU', 'más de 818.000 euros')]), at='Según la sentencia, los consejeros'))
NAR("Miguel Blesa, el antecesor de Rato en Caja Madrid, es condenado a seis años. Fallecerá en dos mil diecisiete, antes de que su condena sea firme. Rato, a cuatro años y medio. El Supremo lo confirma en octubre de dos mil dieciocho.",
    ph('Miguel Blesa', at='Miguel Blesa', lt=['Miguel Blesa', 'Presidente de Caja Madrid (1996-2010)', 'banca'], lugar='blesa'),
    ai('pasillo_tribunal', 'a long corridor of a modern courthouse with frosted glass doors, a man in a dark suit walking away with his lawyer, shadows, cold light', at='El Supremo lo confirma'))
DAT("De los doce millones, nueve coma tres se gastaron en la etapa de Blesa. Dos coma seis, cuando el presidente era Rato. Él mismo, según la sentencia, gastó con su tarjeta casi cien mil euros.",
    AIR('tarjeta_negra', at='De los doce millones'))
B('drama')
NAR("[pause] Veinticinco de octubre de dos mil dieciocho. Prisión de Soto del Real, Madrid. El hombre que había dirigido el Fondo Monetario Internacional se para ante las cámaras antes de entrar.",
    ph('Centro penitenciario Soto del Real', at='Prisión de Soto del Real', lt=['Centro penitenciario Madrid V', 'Soto del Real'], lugar='soto'),
    ai('puerta_prision', 'the heavy grey gate of a modern prison complex under an overcast sky, a crowd of photographers with cameras raised in the foreground seen from behind, tension', at='se para ante las cámaras'))
NAR("De vicepresidente del Gobierno a director del Fondo Monetario Internacional. De ahí, a presidente del cuarto banco de España. Y ahora, a una celda. Pocas caídas en la historia reciente de España han sido tan largas.",
    ai('celda_luz', 'an empty prison cell with a narrow barred window, a single shaft of daylight falling on a neatly made bed, stark, silent, oil painting', at='a una celda'))
RAT("Pido perdón a la sociedad y a las personas que se hayan podido sentir decepcionadas o afectadas.",
    cd(dict(type='quote', text='Pido perdón a la sociedad y a las personas que se hayan podido sentir decepcionadas o afectadas.', attrib='Rodrigo Rato · Soto del Real, 25 de octubre de 2018'), at='Pido perdón'))
NEW("Ese perdón era por las tarjetas. Por la salida a bolsa, Rato siempre defendió su inocencia. Y ese juicio, el gran juicio de Bankia, empieza en noviembre de dos mil dieciocho, en la sede de la Audiencia Nacional en San Fernando de Henares. Treinta y cuatro acusados. La Fiscalía Anticorrupción pide para Rato ocho años y medio de cárcel.",
    ph('Audiencia Nacional San Fernando de Henares', at='San Fernando de Henares', lt=['Audiencia Nacional', 'San Fernando de Henares'], lugar='audiencia'),
    ai('sala_juicio', 'a large modern courtroom with dozens of defendants in dark suits seated in rows seen from behind, three judges on a raised bench in the distance, cold institutional light', at='Treinta y cuatro acusados'))
B('juicio')
NEW("Por la sala desfilan supervisores, auditores e inspectores. Celma, el auditor, repite ante el tribunal aquella frase: presidente, no va. Y Casaus, el inspector de los correos, describe la salida a bolsa con una imagen muy gráfica.",
    AIR('auditor_noche', at='Celma, el auditor'),
    ai('testigo_estrado', 'a witness seated alone at a small table facing a raised bench of judges in a modern courtroom, seen from behind, microphone, single beam of light', at='Casaus, el inspector de los correos'))

CAS("Metes el chute, parece que cumples el capital, pero es un banco que destruía valor cada día.",
    cd(dict(type='quote', text='Metes el chute, parece que cumples el capital, pero es un banco que destruía valor cada día.', attrib='José Antonio Casaus · declaración como testigo, abril de 2019'), at='destruía valor cada día'))
PRE("El exgobernador del Banco de España Miguel Ángel Fernández Ordóñez niega haber recibido aquellos correos. Y Javier Aríztegui, que había sido subgobernador, defiende ante el tribunal que Bankia era un banco importante, con negocio en toda España, que tenía futuro.",
    ph('Miguel Ángel Fernández Ordóñez', at='Miguel Ángel Fernández Ordóñez', lt=['Miguel Ángel Fernández Ordóñez', 'Gobernador del Banco de España (2006-2012)', 'gobierno'], lugar='mafo'),
    cd(dict(type='kw', word='JAVIER ARÍZTEGUI', sub='subgobernador del Banco de España (2006-2012)'), at='Y Javier Aríztegui'),
    AIR('testigo_estrado', at='defiende ante el tribunal'))
NAR("[dramatically] El juicio termina en octubre de dos mil diecinueve. La sentencia tarda casi un año en llegar. Veintinueve de septiembre de dos mil veinte. La Audiencia Nacional dicta sentencia. Cuatrocientas cuarenta y dos páginas. Y un fallo que sorprende a casi todo el país.",
    ai('juez_lee', 'three judges in black robes seated at a raised bench in a modern courtroom, the central one reading from a thick document, everyone else frozen, dramatic cold light', at='La Audiencia Nacional dicta sentencia'),
    ai('folios_sentencia', 'a very thick stack of bound court papers landing on a table, a cloud of dust rising in a beam of light, slow motion, no readable text', at='Cuatrocientas cuarenta y dos páginas'))
M('juicio', 2)
DAT("Absueltos. Los treinta y cuatro. Rato, Olivas, el auditor Celma y todos los consejeros.",
    cd(dict(type='kw', word='ABSUELTOS', sub='los 34 acusados por la salida a bolsa · 29 de septiembre de 2020'), at='Absueltos'))
DOC("El tribunal destaca que la salida a bolsa contó con la aprobación de todos los supervisores: el Banco de España, la Comisión Nacional del Mercado de Valores, el FROB y la Autoridad Bancaria Europea. Y sobre Rato escribe que la descripción de hechos concretos y suficientemente acreditados contra él brilla por su ausencia.",
    cd(dict(type='list', header='La salida a bolsa contó con el visto bueno de', items=[('Banco de España', 'supervisor bancario'), ('CNMV', 'supervisor de los mercados'), ('FROB', 'fondo de rescate'), ('Autoridad Bancaria Europea', 'EBA')]), at='la aprobación de todos los supervisores'),
    cd(dict(type='quote', text='La descripción de hechos concretos y suficientemente acreditados (…) brilla por su ausencia.', attrib='Sentencia de la Audiencia Nacional · 29 de septiembre de 2020'), at='brilla por su ausencia'))
NEW("Dos años después, en octubre de dos mil veintidós, el Tribunal Supremo confirma las absoluciones. Ya es firme. Nadie ha sido condenado penalmente por la salida a bolsa de Bankia.",
    AIR('balanza_justicia', at='el Tribunal Supremo confirma las absoluciones'),
    cd(dict(type='kw', word='FIRME', sub='el Supremo confirma las absoluciones · octubre de 2022'), at='Ya es firme'))
DOC("El Supremo escribe que no advierte error palmario alguno en el razonamiento de la Audiencia. Aunque admite que son posibles otras valoraciones de los mismos hechos.",
    cd(dict(type='quote', text='No se advierte error palmario alguno.', attrib='Tribunal Supremo, Sala de lo Penal · octubre de 2022'), at='no advierte error palmario alguno'))
PRE("Ya en dos mil veinte, al conocer la absolución, la plataforma ciudadana que había impulsado la causa reaccionó con un comunicado que pedía un cambio en las leyes y resumía el sentimiento de muchos afectados en una frase: nunca más un caso Bankia.",
    ai('asamblea_vecinal', 'a packed neighborhood assembly hall at night, people of all ages standing and listening to a speaker at the front, seen from the back of the room, warm light, determination', at='nunca más un caso Bankia'))
NAR("[softly] Y así queda una paradoja difícil de explicar. La justicia civil dijo que el folleto engañó a los pequeños inversores y obligó a devolverles el dinero. La justicia penal dijo que no se probó que nadie cometiera un delito. Las dos sentencias son firmes. Y las dos conviven.",
    cd(dict(type='split', left=dict(title='Vía civil · 2016', lines=['El folleto indujo a error', 'Hay que devolver el dinero']), right=dict(title='Vía penal · 2020-2022', lines=['No se prueba ningún delito', 'Los 34, absueltos']), strike=False), at='una paradoja difícil de explicar'),
    ai('dos_puertas', 'two identical heavy wooden courtroom doors side by side in a marble hall, one lit warm gold, the other cold blue, a lone figure standing between them seen from behind', at='Y las dos conviven'))

NEW("[pause] Y la historia de Rato con Bankia todavía guardaba un capítulo más. ¿Recuerdas la gran campaña publicitaria de la salida a bolsa?",
    AIR('marquesina', at='la gran campaña publicitaria'))
DOC("Diciembre de dos mil veinticuatro. La Audiencia Provincial de Madrid condena a Rodrigo Rato a cuatro años, nueve meses y un día de prisión por tres delitos fiscales, blanqueo de capitales y corrupción entre particulares. Entre los hechos que da por probados: que impuso que Bankia contratara a dos agencias de publicidad, Publicis y Zenith, a cambio de comisiones.",
    cd(dict(type='doc', title='Sentencia de la Audiencia Provincial de Madrid', lines=['4 años, 9 meses y 1 día de prisión', 'Delitos fiscales, blanqueo y corrupción entre particulares'], source='20 de diciembre de 2024 · recurrida ante el Tribunal Supremo'), at='Diciembre de dos mil veinticuatro'),
    ai('agencia_contrato', 'two men in dark suits shaking hands over a signed contract in a sleek advertising agency office at night, glass walls, city lights, faces in shadow, oil painting', at='a cambio de comisiones'))
NEW("La Fiscalía pedía muchos más años. Rato anunció que recurriría la sentencia ante el Tribunal Supremo, por lo que no es firme mientras el alto tribunal no se pronuncie.",
    ai('escalones_supremo', 'an old man in a dark coat walking slowly up the wide stone steps of a neoclassical courthouse alone at dusk, seen from behind, long shadow', at='no es firme'))
# ---------------- VIII · EL FINAL ----------------
M('tension', 6)
T('El final', '2013 · 2021', num='VIII', secs=6.0, sting='tema')
B('tema')
NEW("¿Y Bankia? Contra casi todos los pronósticos, sobrevivió. Con Goirigolzarri al frente volvió a dar beneficios y empezó a devolver dividendos a su principal accionista, el Estado.",
    ph('José Ignacio Goirigolzarri', at='Con Goirigolzarri al frente', lt=['José Ignacio Goirigolzarri', 'Presidente de Bankia (2012-2021)', 'banca'], lugar='goiri'),
    ai('amanecer_torres', 'two leaning glass towers in Madrid at sunrise, the first rays of gold light hitting their facades after a stormy night, puddles reflecting, hopeful, oil painting', at='sobrevivió'))
DAT("En dos mil dieciocho absorbe a otra entidad rescatada, Banco Mare Nostrum. Y en dos mil veinte, en plena pandemia, llega la noticia que cierra el círculo.",
    ai('fusion_puentes', 'two old stone bridges converging into one over a river at dawn in mist, golden light, symbolic, oil painting', at='Banco Mare Nostrum'))
NAR("En septiembre de dos mil veinte se anuncia: CaixaBank absorbe a Bankia. El veintiséis de marzo de dos mil veintiuno, la acción cotiza por última vez. Tres mil quinientos treinta y siete días después de aquella campana.",
    cd(dict(type='kw', word='CAIXABANK', sub='absorbe a Bankia · marzo de 2021'), at='CaixaBank absorbe a Bankia'),
    cd(dict(type='counter', **{'from': 3400}, to=3537, label='días cotizó Bankia en bolsa · 2011-2021'), at='Tres mil quinientos treinta y siete días'))

DAT("El Estado se queda con algo más del dieciséis por ciento del nuevo CaixaBank. Ha cobrado dividendos durante estos años. Pero de los más de veintidós mil millones que puso en Bankia, la mayor parte sigue sin recuperarse. Y el propio Gobierno ha reconocido que se está lejos de recuperarlo. Goirigolzarri, por su parte, pasa a presidir el nuevo gigante.",
    cd(dict(type='kw', word='16 %', sub='participación del Estado en CaixaBank tras la fusión'), at='algo más del dieciséis por ciento'),
    ai('caja_vacia_luz', 'an open empty steel safe in a dark vault with a single coin left inside catching the light, cinematic, melancholic', at='la mayor parte sigue sin recuperarse'))
DAT("La cuenta del rescate, en cambio, nunca se cerró. En dos mil catorce, el FROB vendió un siete y medio por ciento de Bankia por unos mil trescientos millones. En dos mil diecisiete, otro siete por ciento por unos ochocientos dieciocho. Muy lejos de los más de veintidós mil millones que se metieron.",
    cd(dict(type='list', header='Lo que recuperó el FROB vendiendo acciones', items=[('2014 · 7,5 %', '≈ 1.300 M€'), ('2017 · 7 %', '≈ 818 M€'), ('Inyectado', '22.424 M€')]), at='La cuenta del rescate'))
NAR("Y ese mismo año, el Banco de España hizo su propio cálculo para todo el sector. De todo el dinero público que se puso en la banca española durante la crisis, unos sesenta mil millones se daban ya por perdidos. Lo pagaron los contribuyentes.",
    ph('Banco de España Madrid edificio', at='el Banco de España', lugar='bde'),
    cd(dict(type='kw', word='60.000 M€', sub='ayudas públicas a la banca dadas por perdidas · Banco de España, 2017'), at='sesenta mil millones'),
    ai('hucha_suelo', 'a shattered ceramic piggy bank on a dark marble floor, a few coins scattered, spotlight from above', at='Lo pagaron'))
NEW("Recapitulemos. Siete cajas se unieron porque no podían sobrevivir solas. Un banco salió a bolsa con el aval de todos los supervisores. Trescientas cuarenta y siete mil personas compraron. Diez meses después, el Estado tuvo que poner veintidós mil millones. Los tribunales civiles devolvieron el dinero a los pequeños accionistas. Los penales no condenaron a nadie.",
    cd(dict(type='recap', title='Diez meses que costaron 22.424 millones', items=[('Siete cajas, un banco', 'julio de 2010'), ('La campana', '20 de julio de 2011 · 3,75 €'), ('El rescate', '25 de mayo de 2012 · 19.000 millones'), ('Los tribunales', 'devolución en 2016 · absolución en 2020')]), at='Recapitulemos'))
NAR("Quedan las preguntas. ¿Por qué se ignoraron los avisos? ¿Por qué nadie paró una operación que un inspector ya llamaba bombona de oxígeno? ¿Y por qué, cuando todo se vino abajo, la factura acabó repartida entre los ahorradores y los contribuyentes?",
    AIR('inspector_pantalla', at='Por qué se ignoraron los avisos'),
    ai('ahorradores_contribuyentes', 'a crowd of ordinary Spanish people of all ages standing in a large plaza at dusk looking up at a glowing glass tower, seen from behind, silent, monumental', at='entre los ahorradores y los contribuyentes'))
NEW("Hay una lección que sirve para cualquiera que tenga unos ahorros. Que una inversión la venda tu oficina de siempre, que la anuncie la televisión y que la apruebe el supervisor, no la convierte en segura. Leer la letra pequeña, y preguntar por ella, sigue siendo tu mejor protección.",
    ai('lupa_letra', 'an elderly woman holding a magnifying glass over a contract at her kitchen table, reading carefully, warm lamp light, seen over her shoulder, no readable text', at='Leer la letra pequeña'))
NEW("Algunas cosas sí cambiaron. Las cajas de ahorros, tal y como existían, desaparecieron: se convirtieron en bancos o en fundaciones. Y desde noviembre de dos mil catorce, los grandes bancos de la zona euro los supervisa directamente el Banco Central Europeo, desde Fráncfort.",
    ph('European Central Bank headquarters Frankfurt', at='el Banco Central Europeo', lt=['Banco Central Europeo', 'Fráncfort'], lugar='bce'))
NAR("Muchos de aquellos trescientos cuarenta y siete mil accionistas recuperaron su dinero gracias a los tribunales civiles. Otros, los que compraron más tarde en la bolsa, no tuvieron esa suerte. Y todos, como contribuyentes, pagaron una parte del rescate. Sin haber firmado nada.",
    cd(dict(type='kw', word='190.000', sub='accionistas recuperaron su inversión por la vía civil'), at='recuperaron su dinero'),
    AIR('cartera_vacia', at='no tuvieron esa suerte'),
    AIR('cola_oficina', at='como contribuyentes'),
    AIR('ventanas_casas', at='Sin haber firmado nada'))
NAR("[pause] El veinte de julio de dos mil once, una campana sonó en la Bolsa de Madrid. Prometía un banco nuevo, sólido y de todos. En cierto modo, la promesa se cumplió. Bankia acabó siendo de todos. Pero no como nadie había imaginado.",
    AIR('campana_bolsa', at='una campana sonó en la Bolsa de Madrid'),
    ai('campana_silencio', 'a bronze ceremonial bell hanging still and silent in an empty ornate stock exchange hall at night, a single beam of moonlight on it, dust floating', at='Pero no como nadie había imaginado'))
NEW("Si este documental te ha hecho pensar, suscríbete a DocuVox y cuéntanos en los comentarios: ¿tú o alguien de tu familia compró acciones o preferentes de Bankia?",
    ai('salon_noche', 'a family sitting together on a sofa in a Spanish living room at night watching television, seen from behind, warm lamp light, intimate', at='suscríbete a DocuVox'))
