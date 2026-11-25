# -*- coding: utf-8 -*-
# «El corralito argentino» · parte 1: apertura en el helicóptero, un peso un dólar y el sábado del decreto
from lib import *

# ---------------- APERTURA: JUEVES 20 DE DICIEMBRE DE 2001 ----------------
B('accion')
NAR("[serious] Buenos Aires. Jueves, veinte de diciembre de dos mil uno. Pasadas las siete y media de la tarde. Sobre la azotea de la Casa Rosada, un helicóptero blanco enciende los motores.",
    ph('Casa Rosada Buenos Aires', at='Buenos Aires', lt=['Casa Rosada', 'Sede del Gobierno · Buenos Aires'], lugar='rosada'),
    ai('heli_azotea', 'a white presidential helicopter with spinning rotors on the flat rooftop of a grand neoclassical palace at dusk, smoke and tear gas drifting below, wind whipping', at='un helicóptero blanco'))
NAR("Abajo, en la Plaza de Mayo, huele a gas lacrimógeno. Hay caballos de la policía, piedras, cristales rotos. Y miles de personas golpeando cacerolas.",
    ai('plaza_gas', 'a vast city square filled with tear gas clouds, mounted police charging on horses, protesters running and throwing stones, palm trees and an obelisk-like monument in silhouette', at='huele a gas lacrimógeno'),
    ai('caballos_carga', 'police horses rearing and charging through a crowd, riders with batons raised, people scattering, dramatic low angle, motion lines', at='caballos de la policía'),
    ai('cacerolas_mil', 'a dense crowd of ordinary people of all ages banging pots and pans with spoons above their heads at night, open mouths shouting, raw energy', at='golpeando cacerolas'))
NEW("Dentro del helicóptero va un hombre que hasta hace unos minutos era el presidente de la República Argentina. Acaba de firmar su renuncia. Y se marcha volando, porque por tierra ya no puede salir.",
    ph('Fernando de la Rúa', at='un hombre que hasta hace', lt=['Fernando de la Rúa', 'Presidente de Argentina · 1999-2001', 'gobierno'], lugar='delarua'),
    ai('heli_despega', 'a white helicopter lifting off from a palace roof into an orange smoky sky, a crowd far below raising fists and pots, seen from street level', at='se marcha volando'))
CRO("Treinta y nueve muertos en dos días, según los recuentos más citados. Cientos de heridos. Miles de detenidos. Y en las puertas de los bancos, persianas de acero con abolladuras de martillo.",
    cd(dict(type='counter', **{'from': 0}, to=39, label='muertos el 19 y 20 de diciembre de 2001'), at='Treinta y nueve muertos'),
    ai('persiana_martillo', 'close-up of a dented steel shutter of a bank branch, hands holding hammers striking it, sparks and dents, angry motion', at='persianas de acero'))
NAR("¿Cómo se llega a esto? Pues todo había empezado diecinueve días antes. Un sábado. Con un ministro en televisión y una cifra: doscientos cincuenta. Doscientos cincuenta pesos a la semana. Era todo lo que podías sacar de tu propio dinero.",
    ph('Domingo Cavallo', at='un ministro en televisión', lt=['Domingo Cavallo', 'Ministro de Economía', 'gobierno'], lugar='cavallo'),
    cd(dict(type='kw', word='250', sub='pesos por semana · ni uno más'), at='doscientos cincuenta pesos'))
NEW("Los argentinos lo bautizaron enseguida. Con un diminutivo, como quien encierra a un niño pequeño para que no se escape. El corralito.",
    ai('corral_banco', 'a small wooden playpen fence built around the steel doors of a bank, tiny figures of savers trapped inside reaching through the bars, surreal symbolic image', at='El corralito'))
NAR("[pause] Veinticinco años después, esa palabra se ha quedado a vivir en español. La oímos en Chipre. La oímos en Grecia. Y cada vez que un banco español se tambalea, alguien la susurra.",
    ai('cajero_cola_europa', 'a long queue of people in winter coats in front of an ATM on a European street at dawn, seen from behind, a closed bank door, tense silence', at='La oímos en Chipre'),
    ai('susurro', 'two silhouettes leaning close together whispering in front of a bank facade at night, a single streetlight, secretive mood', at='alguien la susurra'))
NEW("¿Cómo puede un Gobierno quedarse con el dinero de sus ciudadanos de un día para otro? ¿Quién se llevó los dólares que había en los bancos? Y la pregunta que te vamos a responder al final, con datos: ¿podría pasar en España?",
    ai('caja_fuerte_vacia', 'a huge round bank vault door swung open revealing completely empty shelves, a single sheet of paper drifting on the floor, dramatic light', at='Quién se llevó los dólares'),
    ai('mapa_puente', 'a symbolic bridge of light stretching across a dark ocean from South America to the Iberian peninsula, seen from above, dramatic', at='podría pasar en España'))
T('El corralito', 'El día que los bancos se quedaron tu dinero', secs=5.5, sting='tema', text='[dramatically] El corralito.', chapter=False)

# ---------------- I · UN PESO, UN DÓLAR ----------------
T('Un peso, un dólar', '1991 · 2001', num='I', secs=6.0, sting='tema')
B('fiesta')
NEW("Para entender el corralito hay que retroceder diez años. A una Argentina que acaba de salir de una pesadilla. En mil novecientos ochenta y nueve los precios se multiplicaron por más de treinta en un solo año. Hiperinflación.",
    ai('hiper_precios', 'a shopkeeper frantically re-labelling prices on supermarket shelves with a pricing gun while shoppers rush past with carts, chaos, motion blur', at='Hiperinflación'),
    cd(dict(type='counter', **{'from': 0}, to=3000, label='inflación en Argentina · 1989 (más del)', suffix=' %'), at='más de treinta'))
NEW("Los sueldos se cobraban por la mañana y se gastaban por la tarde, antes de que el billete valiera menos. Había supermercados que remarcaban los precios varias veces al día.",
    ai('sueldo_corre', 'a worker running down a city street clutching a thick wad of banknotes, people chasing a bus, frantic energy, early 1990s Buenos Aires', at='Los sueldos se cobraban'),
    ai('billetes_viento', 'banknotes blowing in the wind through an empty street like dead leaves, a child chasing them, melancholy', at='valiera menos'))
NAR("[serious] Y antes del milagro, hubo un aviso. Uno que casi nadie recuerda fuera de Argentina.",
    AIR('billetes_lado', at='hubo un aviso'))
CRO("Veintiocho de diciembre de mil novecientos ochenta y nueve. En la Casa Rosada, el ministro de Economía de Menem, Antonio Erman González, anuncia que los plazos fijos se van a canjear a la fuerza por bonos del Estado. Los Bonex ochenta y nueve. En dólares, sí. Pero a cobrar en diez años.",
    ph('Casa Rosada Buenos Aires', at='En la Casa Rosada', lt=['Casa Rosada', 'Buenos Aires'], lugar='rosada'),
    cd(dict(type='doc', title='Plan Bonex · Decreto 36/1990', lines=['Plazos fijos canjeados por Bonex 89', 'Bonos en dólares a 10 años', 'Vencimiento: 1999'], source='Boletín Oficial · 3 de enero de 1990'), at='Los Bonex ochenta y nueve'))
DOC("Decreto treinta y seis de mil novecientos noventa. Para que la moneda nacional recupere su valor adquisitivo, resulta imprescindible limitar la circulación en australes a lo estrictamente necesario.",
    cd(dict(type='quote', text='Resulta imprescindible limitar la circulación en australes a lo estrictamente necesario.', attrib='Decreto 36/1990 · Poder Ejecutivo Nacional'), at='Decreto treinta y seis'))
NEW("El canje afectaba a todo lo que pasara de un millón de australes, unos quinientos cincuenta dólares de la época. Y quien necesitaba el dinero ya, tenía que vender esos bonos en la calle. Según Javier González Fraga, que presidió después el Banco Central, llegaron a cotizar al treinta por ciento de su valor.",
    cd(dict(type='counter', **{'from': 100}, to=30, label='por ciento de su valor · lo que llegaron a cotizar los Bonex (según González Fraga)', suffix=' %'), at='al treinta por ciento'),
    AIR('billetes_viento', at='vender esos bonos'))
NAR("La Corte Suprema dio por bueno el decreto. Y los argentinos aprendieron una primera lección: un plazo fijo podía convertirse, de la noche a la mañana, en un papel a diez años. [pause] Doce años después, esa lección volvería. Multiplicada.",
    ph('Palacio de Justicia de la Nación Buenos Aires', at='La Corte Suprema', lt=['Palacio de Justicia', 'Corte Suprema · Buenos Aires'], lugar='tribunales'),
    AIR('reloj_lunes', at='Multiplicada'))
NAR("Y entonces llega un economista de Córdoba con un plan que parece magia. Domingo Cavallo, ministro de Economía de Carlos Menem. Marzo de mil novecientos noventa y uno. La Ley de Convertibilidad.",
    ph('Domingo Cavallo 1990s', at='Domingo Cavallo', lt=['Domingo Cavallo', 'Ministro de Economía de Menem · 1991-1996', 'gobierno'], lugar='cavallo'),
    ph('Carlos Menem', at='Carlos Menem', lt=['Carlos Menem', 'Presidente de Argentina · 1989-1999', 'gobierno'], lugar='menem'),
    cd(dict(type='doc', title='Ley 23.928 de Convertibilidad', lines=['27 de marzo de 1991', 'Tipo de cambio fijo por ley', 'Respaldo en divisas del Banco Central'], source='Boletín Oficial de la República Argentina'), at='La Ley de Convertibilidad'))
CRO("La regla era sencilla. Un peso vale un dólar. Siempre. Por ley. Y por cada peso que circulara, el Banco Central tendría que guardar un dólar de respaldo en sus reservas.",
    cd(dict(type='versus', left=dict(name='1 PESO', lines=['moneda argentina', 'desde 1992']), right=dict(name='1 DÓLAR', lines=['respaldo en reservas', 'por cada peso'])), at='Un peso vale un dólar'),
    ph('Banco Central de la República Argentina edificio', at='el Banco Central', lt=['Banco Central de la República Argentina', 'Buenos Aires'], lugar='bcra'))
NAR("Cavallo se hizo famoso por un gesto. Puso, uno al lado del otro, un billete de un peso y uno de un dólar. Mismo valor. Para un país que llevaba décadas viendo cómo su moneda se evaporaba, aquella imagen era casi una religión.",
    ai('billetes_lado', 'two banknotes laid side by side on a dark table under a single spotlight, one pale blue and one green, perfectly aligned, almost sacred mood', at='un billete de un peso'),
    ai('altar_moneda', 'a crowd of people looking up with reverence at a giant coin standing upright like a monument in a city square, sun rays behind it', at='casi una religión'))
NEW("Funcionó. La inflación se desplomó en pocos meses. Volvió el crédito. Los argentinos podían comprar un coche a plazos, viajar a Miami, pagar el alquiler en dólares. Fue la fiesta del uno a uno.",
    ai('fiesta_uno', 'a joyful 1990s middle-class family loading suitcases into a car under bright sun, a shiny new car, palm trees, optimistic mood', at='la fiesta del uno a uno'),
    ai('aeropuerto_miami', 'travellers with shopping bags crowding an airport departure hall in the 1990s, big windows with airplanes, festive', at='viajar a Miami'))
NAR("Y en esa fiesta, España tenía sitio en primera fila. Telefónica se quedó con los teléfonos. Iberia, con Aerolíneas Argentinas. Repsol compró YPF, la petrolera nacional. Y el Santander y el BBV entraron en la banca argentina comprando dos de sus grandes bancos.",
    cd(dict(type='list', header='España desembarca en Argentina · años noventa', items=[('Telefónica', 'telefonía'), ('Iberia', 'Aerolíneas Argentinas'), ('Repsol', 'YPF'), ('Santander · BBV', 'banca')]), at='España tenía sitio'),
    ai('barcos_llegan', 'a fleet of ships with billowing sails crossing the ocean toward a modern skyline, symbolic image of investment arriving, bold diagonal', at='Repsol compró YPF'))
CRO("Hubo un detalle que entonces parecía un lujo y luego sería una trampa. Millones de argentinos podían tener la cuenta del banco directamente en dólares. A finales de dos mil, la mayor parte de los depósitos del país estaban en dólares, no en pesos.",
    ai('libreta_dolares', 'close-up of hands opening a bank passbook stamped with dollar signs on a counter, warm light, sense of security that will soon break', at='directamente en dólares'),
    cd(dict(type='split', left=dict(title='Depósitos en pesos', lines=['22.118 millones', '30 de noviembre de 2001']), right=dict(title='Depósitos en dólares', lines=['47.476 millones', '30 de noviembre de 2001'])), at='la mayor parte'))
NEW("Para financiar la fiesta, el Estado también vendió casi todo lo que tenía: teléfonos, petróleo, trenes, agua, electricidad. Privatizaciones a un ritmo que pocos países han visto. Era dinero que entraba una sola vez.",
    ai('subasta_pais', 'an auctioneer hammer coming down over a table covered with tiny models of trains, oil derricks, power lines and telephone poles, bidders in shadow', at='vendió casi todo'))
NAR("Pero un peso solo puede valer un dólar si entran dólares de verdad. Exportando. O pidiendo prestado. Y Argentina, cada vez más, pedía prestado.",
    ai('grifo_dolares', 'a giant tap pouring a thin stream of coins into a leaking barrel, water spilling from cracks at the bottom, symbolic', at='pidiendo prestado'))
CRO("Y la deuda no paraba de crecer. Cada año había que pedir más para pagar lo anterior. Los mercados lo medían con un termómetro que en Argentina se volvió tan popular como el resultado del fútbol: el riesgo país. Cuanto más alto, más caro le salía al país pedir prestado.",
    ai('termometro_pais', 'a giant mercury thermometer rising above a city skyline at dusk, people in the streets looking up at it like at a scoreboard', at='el riesgo país'))
B('tension')
NEW("En mil novecientos noventa y nueve Brasil, el gran vecino y principal cliente, devalúa su moneda. De golpe, los productos argentinos son carísimos. Las fábricas cierran. El paro sube. Y el país entra en una recesión de la que ya no saldrá.",
    ai('fabrica_cierra', 'factory workers walking out through iron gates at dusk as the gate is chained shut behind them, smokestacks without smoke, long shadows', at='Las fábricas cierran'),
    cd(dict(type='timeline', header='La cuesta abajo', events=[('1999', 'Brasil devalúa'), ('2000', 'Blindaje del FMI'), ('jun. 2001', 'Megacanje de deuda'), ('jul. 2001', 'Ley de déficit cero'), ('nov. 2001', 'Fuga de depósitos')]), at='entra en una recesión'))
NAR("Ese mismo año gana las elecciones Fernando de la Rúa, al frente de la Alianza, una coalición de radicales y centroizquierda. Promete limpiar la política. Y mantener el uno a uno.",
    ph('Fernando de la Rúa presidente', at='Fernando de la Rúa', lt=['Fernando de la Rúa', 'Presidente · la Alianza (UCR y Frepaso)', 'gobierno'], lugar='delarua'),
    ai('urna_votos', 'hands dropping ballots into a wooden ballot box, a line of voters waiting behind, hopeful morning light', at='gana las elecciones'))
CRO("En diciembre de dos mil, el FMI y otros acreedores arman un rescate de casi cuarenta mil millones de dólares. Lo llaman el blindaje. Seis meses después llega el megacanje, para alargar los plazos de la deuda a cambio de intereses todavía más altos.",
    ph('International Monetary Fund headquarters Washington', at='el FMI', lt=['Fondo Monetario Internacional', 'Washington'], lugar='fmi'),
    cd(dict(type='counter', **{'from': 0}, to=40000, label='millones de dólares del blindaje · diciembre de 2000 (casi)', suffix=' M$'), at='casi cuarenta mil millones'),
    ai('escudo_grietas', 'a huge iron shield held up by many hands, deep cracks spreading across its surface, debris falling, dramatic', at='Lo llaman el blindaje'))
CRO("Marzo de dos mil uno. Dimite el ministro de Economía, José Luis Machinea. Le sustituye Ricardo López Murphy, que anuncia un recorte de unos dos mil millones de pesos, con tijera para provincias y universidades. Estallan las protestas. Su propia coalición le da la espalda. Dura diecisiete días.",
    cd(dict(type='counter', **{'from': 0}, to=17, label='días de Ricardo López Murphy como ministro de Economía'), at='Dura diecisiete días'),
    ai('universidad_protesta', 'university students occupying the steps of a neoclassical faculty building with banners without letters, raised fists, a teacher among them, bright day', at='Estallan las protestas'))
NEW("Y ese mismo marzo, con el país al borde del abismo, De la Rúa llama al hombre que inventó el uno a uno. Domingo Cavallo vuelve al Ministerio de Economía. Esta vez, para salvar su propia criatura.",
    ph('Domingo Cavallo', at='vuelve al Ministerio', lt=['Domingo Cavallo', 'Ministro de Economía · desde marzo de 2001', 'gobierno'], lugar='cavallo'),
    ph('Palacio de Hacienda Buenos Aires Ministerio de Economía', at='Ministerio de Economía', lt=['Ministerio de Economía', 'Buenos Aires'], lugar='hacienda'))
NAR("Lo intenta todo. En julio, una ley de déficit cero: el Estado no gastará ni un peso más de lo que ingresa, aunque haya que recortar sueldos públicos y pensiones. Y en agosto, otra ley con un nombre que hoy suena a broma macabra.",
    ai('tijeras_nomina', 'giant scissors cutting through a long paper payroll held by many anxious hands, pensioners watching, stark contrast', at='recortar sueldos públicos y pensiones'))
DOC("Ley veinticinco mil cuatrocientos sesenta y seis. De intangibilidad de los depósitos. El Estado nacional en ningún caso podrá alterar las condiciones pactadas entre los depositantes y la entidad financiera.",
    cd(dict(type='doc', title='Ley 25.466 · Intangibilidad de los depósitos', lines=['«El Estado nacional en ningún caso', 'podrá alterar las condiciones pactadas', 'entre los depositantes y la entidad financiera»'], source='Congreso de la Nación · agosto de 2001'), at='Ley veinticinco mil'))
NAR("[pause] Una ley para prometer, por escrito, que nadie tocaría tus ahorros. Tres meses y medio después, esa promesa iba a durar exactamente un fin de semana.",
    ai('papel_arde', 'a single official document with a wax seal catching fire at one corner, curling and burning on a dark desk, embers rising', at='un fin de semana'))
CRO("Porque la gente no se fiaba. Entre enero y noviembre de dos mil uno, de los bancos argentinos salió el equivalente a unos veinte mil millones de dólares. Solo en octubre y noviembre, cerca de dieciocho mil.",
    cd(dict(type='counter', **{'from': 85308}, to=65380, label='millones de dólares en depósitos · de enero a diciembre de 2001', suffix=' M$'), at='unos veinte mil millones'),
    ai('cola_ventanilla', 'a long anxious queue snaking out of a bank branch onto the sidewalk, people clutching documents and bags, a guard at the door, morning', at='salió el equivalente'))
NEW("Ese otoño, el Gobierno había vendido otra idea: la bancarización. Que todo el mundo pagara con tarjeta y cobrara en cuenta, para sacar la economía de la sombra y cobrar más impuestos. Sonaba moderno. Pronto iba a sonar a otra cosa.",
    ai('tarjetas_lluvia', 'a rain of plastic cards falling over a street market where vendors only hold cash, people looking up puzzled, playful but ominous', at='la bancarización'))
CRO("Los bancos se quedan sin efectivo. Para cubrir los agujeros se prestan dinero entre ellos de un día para otro, y en esos días el interés de esos préstamos llegó a dispararse a cifras de cientos por cien al año.",
    ai('termometro_rojo', 'a giant thermometer on the facade of a bank with the red column bursting out of the top, glass cracking, people below shielding their eyes', at='se quedan sin efectivo'))
NEW("En la última semana de noviembre la estampida es imparable. Y el viernes treinta, en el Ministerio de Economía, se trabaja de noche con las persianas bajadas.",
    ai('ministerio_noche', 'a single lit window high on a monumental government building at night, silhouettes of men leaning over a table inside, the city dark around it', at='se trabaja de noche'),
    ai('papeles_decreto', 'tired hands passing typed papers across a table cluttered with coffee cups and ashtrays at 3 a.m., harsh desk lamp, tension', at='con las persianas bajadas'))
NAR("[dramatically] Esa noche se estaba escribiendo el corralito. Y nadie fuera de aquella sala sabía lo que iba a pasar con su dinero el lunes.",
    ai('reloj_lunes', 'a wall clock above a closed bank door ticking toward midnight, long shadow of the hands across the steel, ominous', at='el lunes'))

# ---------------- II · EL SÁBADO DEL DECRETO ----------------
T('El sábado del decreto', '1 de diciembre de 2001', num='II', secs=6.0, sting='accion')
B('tension')
CRO("Día uno. Sábado, uno de diciembre de dos mil uno. El presidente De la Rúa firma el decreto mil quinientos setenta. Lo ha redactado el equipo de Cavallo en los últimos días de noviembre.",
    DIA(1, 'del corralito · sábado 1 de diciembre', at='Día uno', frm=0),
    cd(dict(type='doc', title='Decreto 1570/2001', lines=['Firmado el sábado 1 de diciembre de 2001', 'Límite: 250 pesos o dólares por semana', 'Por titular y por entidad'], source='Boletín Oficial de la República Argentina'), at='firma el decreto'))
NEW("Según la reconstrucción que publicó La Nación, el límite iba a ser de mil pesos por semana. Luego se habló de quinientos. Al final, se quedó en doscientos cincuenta.",
    cd(dict(type='list', header='El límite semanal que se discutió', items=[('1.000 pesos', 'primera idea'), ('500 pesos', 'segunda'), ('250 pesos', 'la definitiva')]), at='mil pesos por semana'),
    ai('cifra_tachada', 'a hand crossing out numbers on a paper with a thick red pen again and again, the paper torn by the pressure, extreme close-up', at='se quedó en doscientos cincuenta'))
DOC("Decreto mil quinientos setenta de dos mil uno. Prohíbense los retiros en efectivo que superen los pesos doscientos cincuenta o dólares estadounidenses doscientos cincuenta por semana, por parte del titular, del total de sus cuentas en cada entidad.",
    cd(dict(type='doc', title='Decreto 1570/2001', lines=['Prohíbense los retiros en efectivo', 'que superen los $250 o U$S 250 por semana', 'del total de sus cuentas en cada entidad'], source='Poder Ejecutivo Nacional · 1 de diciembre de 2001'), at='Decreto mil quinientos setenta'))
NAR("Y ese fin de semana, Domingo Cavallo da la cara en televisión. Con calma. Como quien explica un pequeño cambio de horario.",
    ai('tele_salon', 'a family sitting frozen in front of an old cathode-ray television in a dim living room at night, the screen glow on their backs, cups of mate on the table', at='da la cara en televisión'))
CAV("La única limitación es que podrá extraer en efectivo, en billetes o monedas, hasta doscientos cincuenta pesos por semana.",
    cd(dict(type='quote', text='La única limitación es que podrá extraer en efectivo, en billetes o monedas, hasta 250 pesos por semana.', attrib='Domingo Cavallo · anuncio del corralito, diciembre de 2001'), at='La única limitación'))
CRO("El decreto hacía algo más. Limitaba a mil dólares al mes las transferencias al extranjero. Y prohibía sacar dinero del país en efectivo por encima de esa cifra. La puerta de salida también quedaba cerrada.",
    cd(dict(type='list', header='Lo que prohibía el decreto 1570', items=[('250 $ por semana', 'retiros en efectivo por titular y banco'), ('1.000 U$S al mes', 'transferencias al exterior'), ('salida de efectivo', 'prohibida por encima de ese límite'), ('90 días', 'duración prevista')]), at='mil dólares al mes'),
    ai('aduana_maleta', 'an airport customs officer opening a suitcase stuffed with banknotes on a steel table, a nervous traveller in shadow, harsh fluorescent light', at='La puerta de salida'))
NEW("El argumento oficial era proteger los ahorros. Tu dinero seguía siendo tuyo, decía el ministro. Podías pagar con tarjeta, con cheque, con transferencia. Solo el efectivo quedaba limitado. Y solo durante noventa días.",
    ai('tarjeta_mano', 'a hand holding up a plastic bank card in front of a small neighbourhood shop that only has a cash box, the shopkeeper shaking his head', at='Podías pagar con tarjeta'),
    cd(dict(type='kw', word='90 DÍAS', sub='la duración prometida'), at='noventa días'))
NEW("El ministro reconoció que las medidas causaban molestias. Pero sostuvo que evitaban algo peor: una derrota de todos los argentinos. La palabra derrota se quedó flotando en el aire.",
    ai('palabra_flota', 'smoke rising from a television set in a dark living room forming an abstract shape in the air, a family watching it, uneasy', at='La palabra derrota'))
CAV("Estamos para defender su ahorro, su dinero.",
    cd(dict(type='quote', text='Estamos para defender su ahorro, su dinero.', attrib='Domingo Cavallo · cadena nacional, diciembre de 2001'), at='Estamos para defender'))
CRO("Había un problema. En la Argentina de dos mil uno, se calcula que solo el uno por ciento de las compras se pagaba con tarjeta. El resto, en billetes. Y millones de personas vivían de trabajos en negro, de changas, de lo que cobraban en mano cada día.",
    cd(dict(type='counter', **{'from': 0}, to=1, label='de las transacciones, por vía electrónica (estimación)', suffix=' %'), at='solo el uno por ciento'),
    ai('changa_obrero', 'a day labourer with a tool bag waiting at a street corner at dawn with other men, hoping for a day job, cold light', at='changas'),
    ai('kiosco_caja', 'a tiny street kiosk with an empty cash drawer pulled open, the owner resting his head on his hands, newspapers hanging around', at='en mano cada día'))
NAR("El albañil al que le pagaban en efectivo, de repente, no cobraba. El kiosco no vendía. El jubilado no llegaba a la farmacia. El corralito no solo encerró el dinero de los ahorradores. Encerró la economía entera.",
    ai('albanil_espera', 'a construction worker sitting on a pile of bricks with empty hands, an unfinished wall behind him, dusk, defeated posture', at='El albañil'),
    ai('farmacia_jubilado', 'an elderly man with a cane standing at a pharmacy counter counting a few coins in his palm, the pharmacist waiting, cold fluorescent light', at='El jubilado'),
    ai('economia_jaula', 'a whole miniature city with houses, shops and factories trapped inside a giant birdcage, people pressing against the bars, surreal', at='Encerró la economía entera'))
CRO("Y había otro detalle. Desde ese momento, los sueldos tenían que cobrarse en una cuenta bancaria. Millones de trabajadores que nunca habían pisado un banco tuvieron que abrir una cuenta para que les ingresaran un dinero que luego no podían sacar entero.",
    ai('obrero_banco', 'a construction worker in dusty clothes standing awkwardly in a marble bank lobby holding his helmet, a long counter ahead, out of place', at='nunca habían pisado un banco'))
B('calle')
CRO("Día tres. Lunes. Los bancos abren y las colas dan la vuelta a la manzana. Hay gente que hace noche en la acera. Hay peleas. Hay quien se desmaya del calor, porque en Buenos Aires diciembre es pleno verano.",
    DIA(3, 'del corralito · lunes 3 de diciembre', at='Día tres', frm=1),
    ai('cola_manzana', 'an endless queue of people under a scorching summer sun wrapping around a city block, umbrellas and newspapers as shade, a bank entrance far away', at='las colas dan la vuelta'),
    ai('desmayo_calor', 'a woman fainting in a hot crowded queue, people around catching her and fanning her with newspapers, harsh sunlight', at='quien se desmaya'))
NEW("En los cajeros se forman filas a cualquier hora, para sacar los doscientos cincuenta en cuanto se renueva el cupo. Y los que tienen el dinero en un plazo fijo descubren que ni siquiera pueden tocarlo.",
    ai('cajero_noche', 'people queuing at an ATM in the middle of the night under a flickering light, someone checking a wristwatch, tired faces turned away', at='En los cajeros'))
NAR("Para los grandes, en cambio, el reloj había corrido de otra manera. Porque en las semanas anteriores, quien tenía información y dinero suficiente para moverlo ya lo había sacado del país.",
    ai('maletin_avion', 'a man in an expensive suit walking up the stairs of a private jet with a heavy briefcase, seen from behind, night runway lights', at='ya lo había sacado del país'))
NEW("Entre los bancos atrapados en el corralito estaban también los españoles. El Santander, el BBVA. Sus clientes argentinos hacían la misma cola que los demás. Y en Madrid, las acciones empezaban a notar el golpe.",
    ai('bolsa_madrid_rojo', 'traders silhouetted against a huge board of red falling numbers without readable digits in an old stock exchange hall, tense, Madrid', at='en Madrid'))
CRO("Día cinco. Miércoles. Llega la peor noticia desde Washington. El Fondo Monetario Internacional comunica que no desembolsará el siguiente tramo de su préstamo: mil doscientos sesenta y cuatro millones de dólares que Argentina necesitaba para pagar su deuda.",
    DIA(5, 'del corralito · miércoles 5 de diciembre', at='Día cinco', frm=3),
    ph('International Monetary Fund headquarters Washington', at='Fondo Monetario Internacional', lt=['FMI', 'Washington', 'finanzas'], lugar='fmi'),
    cd(dict(type='counter', **{'from': 0}, to=1264, label='millones de dólares que el FMI retiene', suffix=' M$'), at='mil doscientos sesenta y cuatro'))
NEW("Sin ese dinero, el impago de la deuda es cuestión de semanas. Y en la calle, la paciencia se está acabando todavía más rápido.",
    ai('mecha_encendida', 'a burning fuse sparkling along a dark street pavement toward a stack of crates, glowing embers, extreme tension', at='la paciencia se está acabando'))
NAR("[dramatically] Porque lo que nadie en el Gobierno había calculado es lo que pasa cuando a un país entero le quitas el efectivo. No protesta solo la clase media. Protesta el hambre.",
    ai('estomago_vacio', 'a group of children and mothers standing outside a closed supermarket with metal shutters, empty shopping bags in their hands, harsh light', at='Protesta el hambre'))
