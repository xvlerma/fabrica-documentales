# -*- coding: utf-8 -*-
# «Crisis de 2008» · parte 3: el rescate, la vivienda hoy y la respuesta final
from lib import *

# ---------------- CAPÍTULO 6 · EL RESCATE ----------------
T('El rescate', '2009 · 2012', num='VI', secs=4.5, sting='tema')
B('tension')
NAR("[serious] Madrid, veinte de julio de dos mil once. Palacio de la Bolsa. Rodrigo Rato, exvicepresidente del Gobierno y exdirector gerente del Fondo Monetario Internacional, toca la campana. Bankia empieza a cotizar.",
    ph('Bolsa de Madrid Palacio de la Bolsa', at='Palacio de la Bolsa', lt=['Palacio de la Bolsa', 'Madrid · 20 de julio de 2011']),
    ph('Rodrigo Rato', at='Rodrigo Rato', lt=['Rodrigo Rato', 'Presidente de Bankia', 'banca']),
    ai('campana_bolsa', 'a hand ringing a large brass bell on a stock exchange balcony above a crowd of applauding people in suits, confetti light, celebratory, motion', at='toca la campana'))
NEW("Para entender cómo se llegó hasta ahí hay que volver a las cajas. Cuando estalló la burbuja, eran ellas las que más ladrillo tenían. Una tras otra empezaron a caer. La primera, Caja Castilla-La Mancha, intervenida por el Banco de España en marzo de dos mil nueve. Después, CajaSur. Después, la Caja de Ahorros del Mediterráneo, vendida al Banco Sabadell por un euro.",
    ph('Caja Castilla La Mancha', at='Caja Castilla-La Mancha'),
    cd(dict(type='timeline', header='La caída de las cajas', events=[('2009', 'Caja Castilla-La Mancha'), ('2010', 'CajaSur'), ('2011', 'CAM, vendida por un euro'), ('2012', 'Bankia')]), at='Una tras otra empezaron a caer'))
DAT("En dos mil nueve había cuarenta y cinco cajas de ahorros en España. Hoy quedan dos pequeñas cajas que siguen siéndolo. Todas las demás desaparecieron, se fusionaron o se convirtieron en bancos.",
    cd(dict(type='split', left=dict(title='2009', lines=['45 cajas de ahorros']), right=dict(title='Hoy', lines=['2 cajas', 'el resto, fusionadas o convertidas en bancos']), strike=False), at='cuarenta y cinco cajas'))
NEW("La solución que se eligió fue juntarlas. Siete cajas, con Caja Madrid y Bancaja a la cabeza, se unieron para formar un gigante: Bankia. Y para conseguir capital, el gigante salió a bolsa.",
    ph('Torre Caja Madrid Bankia', at='Bankia'),
    ai('siete_llaves', 'seven heavy old vault keys being joined on a single iron ring by two hands, dramatic spotlight, dark background, symbolic close-up', at='Siete cajas'))
DOC("Para ordenar aquel proceso nació en junio de dos mil nueve el FROB, el Fondo de Reestructuración Ordenada Bancaria. Su misión: dar dinero público a las cajas que se fusionaran y tomar el control de las que no pudieran sobrevivir.",
    cd(dict(type='doc', title='Real Decreto-ley 9/2009 · creación del FROB', lines=['Fondo de Reestructuración Ordenada Bancaria', 'ayudas a las entidades que se integren'], source='Boletín Oficial del Estado · 27 de junio de 2009'), at='el FROB'))
PRE("Muchas fusiones se hicieron entre cajas de la misma comunidad, con sus mismos consejos y sus mismos problemas. Los analistas las llamaron fusiones frías. Juntar dos enfermos, decían algunos, no da un sano.",
    ai('dos_edificios', 'two old bank headquarters buildings in a Spanish city connected by a fragile rope bridge in a storm, symbolic editorial composition, dramatic sky', at='fusiones frías'))
RAT("La salida a Bolsa de Bankia es una decisión estratégica para hacer más fuerte la entidad y consolidar su papel de liderazgo.",
    cd(dict(type='quote', text='La salida a Bolsa de Bankia es una decisión estratégica para hacer más fuerte la entidad.', attrib='Rodrigo Rato · 20 de julio de 2011'), at='La salida a Bolsa'))
NEW("Más de trescientos cuarenta mil pequeños ahorradores compraron acciones a tres euros con setenta y cinco céntimos. Muchos eran clientes de toda la vida de su caja, que la habían visto anunciar en las sucursales.",
    cd(dict(type='counter', to=347000, label='pequeños accionistas en la salida a bolsa de Bankia'), at='Más de trescientos cuarenta mil'),
    ai('sucursal_cola', 'elderly customers queuing inside a bank branch office in Spain, posters on the walls without readable text, a teller window, warm interior light, seen from behind', at='clientes de toda la vida'))
NAR("[pause] Diez meses después, todo saltó por los aires. Siete de mayo de dos mil doce: Rato dimite. Dos días después, el Estado se queda con el banco. Y el veinticinco de mayo, Bankia pide diecinueve mil millones de euros más. Ese mismo día se suspende su cotización.",
    cd(dict(type='timeline', header='Bankia · diez meses', events=[('20 jul 2011', 'sale a bolsa a 3,75 €'), ('7 may 2012', 'dimite Rato'), ('9 may 2012', 'el Estado toma el control'), ('25 may 2012', 'pide 19.000 millones')]), at='Diez meses después'),
    cd(dict(type='counter', to=19000, label='millones de euros pedidos por Bankia · 25 de mayo de 2012'), at='diecinueve mil millones'))
DAT("Bankia había salido a bolsa valorada en unos seis mil setecientos millones de euros. Cuando se suspendió su cotización, sus acciones ya habían perdido más de un tercio de su valor. Y lo peor estaba por llegar: en dos mil doce, ya nacionalizada, declaró pérdidas de más de diecinueve mil millones. Las mayores de la historia de una empresa española.",
    cd(dict(type='counter', to=19000, label='millones de euros de pérdidas de Bankia en 2012 · más de'), at='declaró pérdidas'))
B('accion')
NAR("[dramatically] Y entonces España entró en pánico. Los inversores huyen de la deuda española. La prima de riesgo, lo que España paga de más por pedir prestado respecto a Alemania, se dispara. Y en Bruselas, Berlín y Washington empiezan a hablar en voz alta de algo que parecía impensable: el rescate de España.",
    ai('sala_crisis', 'a crowded government crisis room at night with officials around a table covered with papers and phones, screens with red charts, seen from behind, tense action', at='España entró en pánico'),
    ph('European Commission Berlaymont Brussels', at='Bruselas'))
NEW("Sábado nueve de junio de dos mil doce. Tras una videoconferencia con sus socios del euro, el ministro de Economía, Luis de Guindos, anuncia que España pedirá ayuda europea para sus bancos. Hasta cien mil millones de euros. Y lo explica así.",
    ph('Luis de Guindos 2012', at='Luis de Guindos', lt=['Luis de Guindos', 'Ministro de Economía', 'gobierno']),
    cd(dict(type='counter', to=100000, label='millones de euros · línea de ayuda europea para la banca'), at='Hasta cien mil millones'))
GUI("No tiene que ver con un rescate en absoluto. No hay el más mínimo rescate.",
    cd(dict(type='quote', text='No tiene que ver con un rescate en absoluto. No hay el más mínimo rescate.', attrib='Luis de Guindos · 9 de junio de 2012'), at='No tiene que ver'))
GUI("Es un préstamo en condiciones extremadamente favorables.",
    cd(dict(type='quote', text='Es un préstamo en condiciones extremadamente favorables.', attrib='Luis de Guindos · 9 de junio de 2012'), at='Es un préstamo'))
NAR("Un detalle que hoy parece de guion: antes de ser ministro, Luis de Guindos había dirigido en España y Portugal el banco cuya caída lo empezó todo. Lehman Brothers.",
    ph('Lehman Brothers logo building', at='Lehman Brothers'))
NEW("Al día siguiente, el presidente Mariano Rajoy compareció en la Moncloa antes de viajar a Polonia para ver a la selección en la Eurocopa. Habló de una línea de crédito. Y defendió así lo que había hecho su Gobierno.",
    ph('Palacio de la Moncloa', at='la Moncloa'))
RAJ("Si no hubiésemos hecho los deberes, nos habrían intervenido.",
    cd(dict(type='quote', text='Si no hubiésemos hecho los deberes, nos habrían intervenido.', attrib='Mariano Rajoy · 10 de junio de 2012'), at='Si no hubiésemos'))
PRE("La prensa internacional no tuvo dudas. Para casi todos los periódicos del mundo, aquel préstamo tenía un nombre: el rescate de la banca española.",
    ai('kiosco', 'a newspaper kiosk in a European street with dozens of front pages stacked, headlines blurred and unreadable, people grabbing copies, morning rush, motion', at='La prensa internacional'))
B('tension')
DAT("Veinticuatro de julio de dos mil doce. La prima de riesgo española llega a seiscientos treinta y ocho puntos básicos. El bono a diez años supera el siete por ciento. Es el nivel al que Grecia, Irlanda y Portugal habían tenido que pedir el rescate completo.",
    cd(dict(type='counter', to=638, label='puntos básicos de prima de riesgo · 24 de julio de 2012'), at='seiscientos treinta y ocho'))
NAR("Y entonces, dos días después, en Londres, un italiano pronunció una frase que lo cambió todo. Mario Draghi, presidente del Banco Central Europeo.",
    ph('Mario Draghi 2012', at='Mario Draghi', lt=['Mario Draghi', 'Presidente del Banco Central Europeo']))
USA("Dentro de nuestro mandato, el Banco Central Europeo está dispuesto a hacer lo que sea necesario para preservar el euro. Y créanme: será suficiente.",
    cd(dict(type='quote', text='El BCE está dispuesto a hacer lo que sea necesario para preservar el euro. Y créanme: será suficiente.', attrib='Mario Draghi · Londres, 26 de julio de 2012 (traducción)'), at='Dentro de nuestro mandato'))
NEW("Los mercados se lo creyeron. La prima empezó a bajar. España recibió algo más de cuarenta y un mil millones del préstamo europeo, se creó un banco malo, la Sareb, para quedarse con los pisos y los créditos tóxicos de las cajas, y el sistema no se hundió.",
    ph('Sareb', at='la Sareb'),
    ai('almacen_llaves', 'a vast warehouse wall covered with thousands of hanging apartment keys with tags, a single worker on a ladder, cold industrial light, wide', at='un banco malo'))
DAT("La Sareb recibió casi doscientos mil inmuebles y préstamos de las entidades rescatadas, pagados a unos cincuenta mil millones de euros. Pisos sin terminar, solares, urbanizaciones a medias. Buena parte de los restos de la burbuja acabaron en un solo cajón.",
    cd(dict(type='counter', to=200000, label='activos traspasados a la Sareb · casi'), at='casi doscientos mil inmuebles'))
DAT("Pero tuvo un precio. Según el Banco de España, entre dos mil nueve y dos mil dieciocho se inyectaron más de sesenta y cuatro mil millones de euros públicos en la banca. De ellos, solo se esperaban recuperar unos catorce mil ochocientos. Más de cincuenta mil millones no volverán.",
    cd(dict(type='split', left=dict(title='Inyectado en la banca', lines=['64.098 millones de euros', '2009-2018']), right=dict(title='Recuperable', lines=['Unos 14.785 millones', 'más de 50.000 millones, perdidos']), strike=False), at='Según el Banco de España'),
    cd(dict(type='counter', to=50000, label='millones de euros de dinero público que no se recuperarán · más de'), at='Más de cincuenta mil millones'))
DOC("El préstamo europeo llegó con un documento de condiciones, el memorando de entendimiento firmado en julio de dos mil doce. Obligaba a los bancos rescatados a reducir su tamaño, a cerrar oficinas y a traspasar sus activos inmobiliarios al banco malo. Y obligaba a quienes tenían preferentes y deuda de esos bancos a asumir pérdidas.",
    cd(dict(type='doc', title='Memorando de entendimiento · julio de 2012', lines=['Recapitalizar y reestructurar las entidades débiles', 'Traspasar los activos inmobiliarios a una sociedad de gestión', 'Reparto de pérdidas con preferentistas'], source='Eurogrupo y Gobierno de España · 20 de julio de 2012'), at='el memorando de entendimiento'))
DAT("Desde entonces, España ha cerrado más de la mitad de sus oficinas bancarias. Había más de cuarenta y cinco mil en dos mil ocho. Hoy son menos de dieciocho mil.",
    cd(dict(type='split', left=dict(title='Oficinas bancarias · 2008', lines=['Más de 45.000']), right=dict(title='Hoy', lines=['Menos de 18.000', 'pueblos enteros sin banco']), strike=False), at='más de la mitad de sus oficinas'))
NEW("[short pause] ¿Y los responsables? Rato acabó en prisión, pero no por la salida a bolsa de Bankia, de la que fue absuelto junto a toda la cúpula: por las tarjetas opacas de Caja Madrid. Y cinco años después del rescate, en dos mil diecisiete, otro banco, el Popular, se hundió en una noche y fue vendido al Santander por un euro.",
    ai('celda_puerta', 'a heavy prison corridor door closing, seen from inside, a man\'s shadow on the floor, cold light, symbolic close-up', at='Rato acabó en prisión'),
    ph('Banco Popular sede Madrid', at='el Popular'))
NAR("Y el propio Banco de España acabó haciendo examen de conciencia. En dos mil diecisiete publicó un largo informe sobre la crisis. Al presentarlo, su gobernador, Luis María Linde, reconoció lo que diez años antes casi nadie quería decir en voz alta.",
    ph('Luis María Linde', at='Luis María Linde', lt=['Luis María Linde', 'Gobernador del Banco de España · 2012-2018', 'gobierno']))
DOC("Este proceso se ajustó a una dinámica consistente con lo que puede considerarse una burbuja especulativa en el sector inmobiliario.",
    cd(dict(type='quote', text='Una dinámica consistente con lo que puede considerarse una burbuja especulativa.', attrib='Luis María Linde, gobernador del Banco de España · presentación del Informe sobre la crisis, 2017'), at='Este proceso se ajustó'))
NAR("[pause] España salió de aquello. La economía volvió a crecer a partir de dos mil catorce. El paro empezó a bajar. Los precios de los pisos tocaron fondo ese mismo año, un treinta por ciento por debajo del máximo. Y durante unos años pareció que la lección estaba aprendida. [dramatically] Hasta que los precios volvieron a subir.",
    cd(dict(type='timeline', header='Precio de la vivienda libre', events=[('2007', '2.085 €/m²'), ('2014', '1.463 €/m² · el fondo'), ('2019', 'recuperación'), ('2025', '2.230 €/m² · récord')]), at='Los precios de los pisos tocaron fondo'))

NEW("Y llegó una década de dinero casi gratis. Entre dos mil dieciséis y dos mil veintiuno, el euríbor pasó meses enteros por debajo de cero. Nunca había sido tan barato pedir una hipoteca. [short pause] Y la historia empezó a rimar.",
    cd(dict(type='kw', word='EURÍBOR NEGATIVO', sub='2016 · 2021'), at='por debajo de cero'))
# ---------------- CAPÍTULO 7 · LA VIVIENDA HOY ----------------
T('La vivienda hoy', '¿Se está repitiendo?', num='VII', secs=5.0, sting='tema')
B('fondo')
NAR("[serious] Seseña, hoy. Las mismas calles que la prensa extranjera fotografiaba vacías están hoy llenas de coches aparcados. Hay colegios, supermercados, parques infantiles. Cerca de cuatro mil pisos habitados.",
    ph('El Quiñón Seseña 2024', at='Las mismas calles', lt=['El Quiñón, Seseña', 'Hoy']),
    ai('quinon_hoy', 'the same red brick apartment blocks now with children playing in a park, cars parked along the street, laundry on balconies, families walking, sunny afternoon', at='llenas de coches aparcados'))
NEW("¿Quién vive allí? En buena parte, familias jóvenes que no pueden pagar un piso en Madrid. La ciudad fantasma de la burbuja ha revivido gracias a lo contrario de una burbuja: a que faltan casas.",
    ai('mudanza', 'a young couple carrying moving boxes into an apartment building entrance, a toddler holding a small plant, a rental van, morning light, hopeful', at='familias jóvenes'))
DOC("Y en dos mil veintidós, la prensa contaba que en el mismo municipio se planeaban casi catorce mil viviendas nuevas. Más que las que soñó El Pocero.",
    cd(dict(type='doc', title='Seseña · 2022', lines=['Se planean 13.825 viviendas nuevas', '«dejan pequeño el sueño de El Pocero»'], source='El Periódico de España · 16 de enero de 2022'), at='casi catorce mil viviendas nuevas'))
NEW("Y el aeropuerto sin aviones de Castellón tampoco es ya lo que era. Hoy tiene vuelos regulares, un negocio de mantenimiento de aviones y ha batido récords de pasajeros. Los monumentos de la burbuja, uno a uno, han encontrado uso. [short pause] Porque el país que tenía casas de más se ha quedado corto.",
    ph('Castellón Costa Azahar Airport aircraft', at='Hoy tiene vuelos regulares'))
NAR("[pause] Y aquí está la pregunta que nos trajo hasta aquí. Si el piso vuelve a costar más que nunca, ¿estamos otra vez en dos mil siete? Vamos a compararlo dato a dato.",
    cd(dict(type='kw', word='¿2007 OTRA VEZ?', sub='dato a dato'), at='estamos otra vez en dos mil siete'))
DAT("Primero, el precio. A finales de dos mil veinticinco, el metro cuadrado de vivienda libre marcó dos mil doscientos treinta euros, un siete por ciento por encima del máximo de dos mil siete. Pero eso es en euros de cada año. Si se descuenta lo que han subido los precios de todo lo demás desde entonces, la vivienda sigue en torno a un veinticinco por ciento por debajo de aquel máximo.",
    HOY(['Precio nominal', '2007: 2.085 €/m²', '2025: 2.230 €/m²'], ['Descontada la inflación', 'Hoy, en torno a un 25 %', 'por debajo de 2007'], at='Primero, el precio'))
NEW("Segundo, lo que cuesta en sueldos. En dos mil siete, comprar un piso exigía de media nueve años y medio de la renta bruta de un hogar. A finales de dos mil veinticinco, casi ocho. El esfuerzo más alto desde dos mil once.",
    HOY(['2007', '9,5 años de renta', 'máximo histórico'], ['2025', '7,98 años de renta', 'el más alto desde 2011'], at='Segundo, lo que cuesta en sueldos'))
DAT("Tercero, y aquí está la gran diferencia: el crédito. En dos mil siete, lo que los bancos habían prestado a las familias para comprar casa equivalía al sesenta y dos por ciento de la economía española. Y lo prestado a promotores y constructoras, a otro cuarenta y dos. Hoy esas cifras son el treinta y uno y menos del seis por ciento.",
    HOY(['Crédito en 2007', 'Hipotecas: 62 % del PIB', 'Promotores: 42 % del PIB'], ['Crédito en 2025', 'Hipotecas: 31 % del PIB', 'Promotores: menos del 6 %'], at='el crédito'))
DOC("El Banco de España lo resume en su último informe de estabilidad financiera: los criterios para conceder hipotecas se han relajado un poco, pero siguen muy lejos de sus máximos, y los riesgos inmobiliarios para la estabilidad financiera permanecen contenidos.",
    ph('Banco de España Cibeles', at='El Banco de España lo resume'),
    cd(dict(type='doc', title='Informe de Estabilidad Financiera · primavera de 2026', lines=['Los criterios de concesión se mantienen', '«muy por debajo de sus máximos históricos»', 'Los riesgos inmobiliarios «permanecen contenidos»'], source='Banco de España · mayo de 2026'), at='su último informe'))
DAT("Cuarto, las casas que se construyen. En dos mil seis se empezaron más de ochocientas mil viviendas. En dos mil veinticinco se terminaron unas noventa y dos mil. Ese mismo año se crearon en España unos doscientos cuarenta mil hogares nuevos.",
    HOY(['2006', 'Más de 800.000 viviendas', 'empezadas en un año'], ['2025', '92.000 terminadas', 'para 240.000 hogares nuevos'], at='Cuarto, las casas que se construyen'))
DAT("Y el tipo de casa que se compra también ha cambiado. En los años de la burbuja, seis de cada diez viviendas vendidas eran nuevas. Hoy, solo algo más de dos de cada diez. Se compra sobre todo vivienda usada, porque no hay nueva.",
    HOY(['Años 2000', '6 de cada 10 ventas', 'vivienda nueva'], ['Hoy', 'Algo más de 2 de cada 10', 'vivienda nueva'], at='el tipo de casa que se compra'))
NAR("[pause] En dos mil siete sobraban casas. Hoy faltan. El Banco de España calcula que solo entre dos mil veintiuno y dos mil veinticinco se ha acumulado un déficit de unas setecientas cincuenta mil viviendas. Concentrado en Madrid, Barcelona, Valencia, Alicante, Málaga y la costa.",
    cd(dict(type='counter', to=750000, label='viviendas que faltan · déficit 2021-2025 según el Banco de España'), at='setecientas cincuenta mil'),
    cd(dict(type='map', title='Donde faltan casas · 2025', bbox=[-9.5, 36.0, 3.5, 43.8], points=[dict(name='Madrid', lon=-3.70, lat=40.42, big=1), dict(name='Barcelona', lon=2.17, lat=41.39, big=1), dict(name='Valencia', lon=-0.38, lat=39.47), dict(name='Alicante', lon=-0.48, lat=38.35), dict(name='Málaga', lon=-4.42, lat=36.72), dict(name='Murcia', lon=-1.13, lat=37.99)]), at='Concentrado en Madrid'))
DAT("Y quinto, las hipotecas. En dos mil ocho, casi todas eran variables y el euríbor estaba por encima del cinco por ciento. Hoy seis de cada diez se firman a tipo fijo. El euríbor está en torno al tres coma tres por ciento, y noviembre de dos mil veintiséis va camino de ser su mes más caro del año.",
    HOY(['2008', '97 % hipotecas variables', 'euríbor por encima del 5 %'], ['2026', '6 de cada 10 a tipo fijo', 'euríbor ≈ 3,3 % y subiendo'], at='Y quinto, las hipotecas'))
NEW("Para entenderlo en euros: una hipoteca variable media, de ciento sesenta y siete mil euros a veinticinco años, que se revise en diciembre de dos mil veintiséis, pagará unos ochenta y siete euros más al mes que hace un año. Molesto, pero muy lejos de los golpes de dos mil ocho. El problema hoy no es la cuota de los que ya tienen hipoteca. Es la entrada que no pueden reunir los que quieren tenerla.",
    cd(dict(type='counter', to=87, prefix='+', suffix=' €', label='al mes · hipoteca variable media que se revisa en diciembre de 2026'), at='ochenta y siete euros más al mes'))
B('tension')
NEW("Entonces, ¿todo tranquilo? No del todo. Porque hay señales que recuerdan demasiado a aquellos años.",
    ai('nubes_ciudad', 'dark storm clouds gathering over a modern Spanish city skyline with tower cranes, a ray of sunlight on one building, dramatic wide', at='señales que recuerdan'))
NAR("[pause] Y hay una lección de dos mil siete que conviene no olvidar: casi nadie vio venir el final de la subida. Ni los compradores, ni los bancos, ni los gobiernos. Las burbujas solo se ven con claridad cuando ya han estallado.",
    ai('pompa_jabon', 'a giant soap bubble reflecting a city of cranes and apartment blocks, about to burst, held above a crowd of tiny people looking up, surreal editorial image', at='Las burbujas solo se ven'))
DAT("Un estudio de la Fundación de las Cajas de Ahorros, Funcas, publicado en dos mil veintiséis, lo resume con una comparación: por número de compraventas y por precio real, el mercado se parece al de dos mil tres o dos mil cuatro, en plena subida. Pero por crédito y por riesgo de los bancos, se parece más al de mil novecientos noventa y nueve. Un ciclo de precios avanzado, con un sistema financiero mucho más sano.",
    cd(dict(type='split', left=dict(title='Por precio y ventas', lines=['Como en 2003-2004', 'en plena subida']), right=dict(title='Por crédito y riesgo', lines=['Como en 1999-2002', 'bancos mucho más sanos']), strike=False), at='Un estudio de la Fundación'))
NEW("Las compraventas superaron las setecientas mil en doce meses, el nivel más alto desde dos mil siete. Los pisos subieron en dos mil veinticinco por encima del siete por ciento. Y en dos mil veintiséis, con la inflación de nuevo en torno al cuatro por ciento, el Banco Central Europeo prepara nuevas subidas de tipos.",
    cd(dict(type='list', header='Las señales de alarma', items=[('Más de 700.000 compraventas', 'en 12 meses · máximo desde 2007'), ('Precios +7 % en 2025', 'por encima de los sueldos'), ('Inflación en torno al 4 % en 2026', 'y el BCE preparando subidas')]), at='Las compraventas superaron'))
DAT("Y un dato pequeño pero significativo: en dos mil veinticinco, las ejecuciones hipotecarias iniciadas volvieron a subir, un doce por ciento, después de tres años bajando.",
    cd(dict(type='counter', to=12.4, dec=1, suffix=' %', label='subida de las ejecuciones hipotecarias iniciadas en 2025 · INE'), at='volvieron a subir'))
NEW("Pero el mayor cambio no está en las hipotecas. Está en el alquiler. Quien hoy no puede comprar, alquila. Y alquilar se come en muchas ciudades más de un tercio del sueldo. El gobernador del Banco de España, José Luis Escrivá, llegó a describir la situación de la vivienda como una emergencia nacional.",
    ph('José Luis Escrivá', at='José Luis Escrivá', lt=['José Luis Escrivá', 'Gobernador del Banco de España']),
    ai('piso_compartido', 'four young adults in their late twenties sharing a small rented apartment kitchen, one counting coins, laptops and dishes, evening, cramped but warm, faces turned away', at='alquilar se come'),
    cd(dict(type='kw', word='EMERGENCIA NACIONAL', sub='José Luis Escrivá, gobernador del Banco de España'), at='una emergencia nacional'))

DAT("Los datos lo confirman. El porcentaje de hogares con casa en propiedad ha bajado al setenta por ciento. Los alquileres llevan más de una década creciendo más deprisa que los sueldos. Y los jóvenes españoles se emancipan, de media, después de los treinta años. De los más tarde de Europa.",
    cd(dict(type='list', header='La crisis de hoy', items=[('70 % de hogares en propiedad', 'y bajando'), ('Alquileres', 'creciendo más que los sueldos'), ('Emancipación', 'después de los 30 años de media')]), at='Los datos lo confirman'))
PRE("[softly] Y la vivienda ha vuelto a la calle. En mayo de dos mil veintiséis, miles de personas se manifestaron en Madrid contra el precio de la vivienda. Quince años después del Quince M, muchos de los que entonces acampaban en Sol vuelven a protestar. Ahora, por el alquiler.",
    ai('protesta_alquiler', 'a large street protest in Madrid with thousands of young people holding house-shaped cardboard signs without readable text, a rent sign silhouette on a balcony above, sunny, aerial, action', at='la vivienda ha vuelto a la calle'))
NEW("Las propuestas para salir de aquí dividen a los partidos. Unos piden liberar suelo, bajar impuestos y facilitar que se construya mucho más y más deprisa. Otros piden limitar los alquileres y levantar un gran parque de vivienda pública, como el que tienen otros países europeos. Y casi todos coinciden en el diagnóstico: faltan casas donde está el trabajo.",
    cd(dict(type='split', left=dict(title='Una receta', lines=['Más suelo y menos trabas', 'construir mucho más']), right=dict(title='Otra receta', lines=['Limitar alquileres', 'más vivienda pública']), strike=False), at='Las propuestas para salir de aquí'))
NEW("[short pause] Antes de la respuesta, recapitulemos cómo está todo, dato a dato.",
    cd(dict(type='recap', title='2007 frente a hoy', items=[('Precio', 'récord nominal · un 25 % menos en términos reales'), ('Esfuerzo', '8 años de renta · 9,5 en 2007'), ('Crédito', 'la mitad que entonces'), ('Casas', 'en 2007 sobraban · hoy faltan 750.000'), ('Hipotecas', 'la mayoría a tipo fijo')]), at='recapitulemos cómo está todo'))
# ---------------- CIERRE · LA RESPUESTA ----------------
B('tema')
NAR("[serious] Así que, ¿se está repitiendo la crisis de dos mil ocho? [pause] La respuesta corta es no. No de la misma manera.",
    cd(dict(type='kw', word='¿SE REPITE?', sub='la respuesta'), at='se está repitiendo la crisis'))
NAR("En dos mil siete, España construyó demasiadas casas con dinero prestado que no existía. Cuando el crédito se cortó, cayeron los bancos y, detrás de ellos, el empleo. Aquella fue una burbuja de crédito.",
    ai('castillo_naipes', 'a tall house of cards built from bank papers and house keys collapsing in slow motion on a wooden table, dramatic light, action', at='Aquella fue una burbuja de crédito'))
NEW("Hoy ocurre casi lo contrario: se construyen muy pocas casas para la gente que las necesita, y los bancos prestan con mucho más cuidado. Lo que hoy se repite no es la burbuja de los bancos. Es el precio.",
    HOY(['2007 · burbuja de crédito', 'Sobraban casas', 'Los bancos prestaban sin freno'], ['Hoy · crisis de acceso', 'Faltan casas', 'El crédito está contenido'], at='Hoy ocurre casi lo contrario'))
NAR("[pause] Y eso tiene otra consecuencia. La crisis de dos mil ocho la sufrieron los que compraron. La de hoy la sufren, sobre todo, los que no pueden comprar. Una generación que tiene trabajo, que tiene estudios, y que a los treinta años sigue compartiendo piso o viviendo con sus padres.",
    ai('joven_ventana', 'a young woman in her thirties looking out of her childhood bedroom window at a city full of apartment blocks and cranes at dusk, seen from behind, posters on the wall without readable text', at='viviendo con sus padres'))
NEW("Para comprar hoy un piso medio hacen falta ahorros que muchas familias jóvenes no tienen: la entrada, los impuestos, el notario. Los bancos ya no financian el cien por cien como en dos mil seis. Y esa es, precisamente, una de las razones por las que hoy hay menos riesgo de otro dos mil ocho. La misma prudencia que protege a los bancos deja fuera a muchos compradores.",
    ai('hucha', 'a young person counting savings from a ceramic piggy bank on a small table next to a real estate listing on a laptop screen without readable text, night, lamp light, faces hidden', at='hacen falta ahorros'))
NAR("¿Puede volver a estallar algo? Nadie lo sabe. Si los tipos suben mucho y el empleo cae, las familias más endeudadas volverán a sufrir. Pero los expertos coinciden en que el riesgo hoy no es que caigan los bancos. Es que la vivienda siga alejándose de los sueldos.",
    ai('balanza_hoy', 'a large balance scale with a small house on one side and a stack of payslips on the other, the house side heavier, symbolic still life, warm light', at='Nadie lo sabe'))
NEW("Y si algo nos dejó dos mil ocho son tres señales para reconocer el peligro: que los precios suban mucho más deprisa que los sueldos durante años; que comprar parezca la única opción posible; y que todo el mundo, desde el banco hasta el vecino, te diga que esta vez es diferente.",
    cd(dict(type='list', header='Tres señales de peligro', items=[('Precios que suben más que los sueldos', 'durante años'), ('Comprar como única opción', '«alquilar es tirar el dinero»'), ('«Esta vez es diferente»', 'la frase de todas las burbujas')]), at='tres señales para reconocer el peligro'))
NAR("[serious] Dos mil ocho nos enseñó que el ladrillo sí puede bajar. Que un país puede quedarse con millones de casas vacías y cientos de miles de familias sin casa a la vez. [short pause] Y que cuando llega la factura, la pagan sobre todo los que menos margen tienen.",
    ph('Residencial Francisco Hernando Seseña', at='el ladrillo sí puede bajar'),
    ai('dos_mundos', 'split composition: on one side an empty dark apartment block, on the other a family with suitcases on the street at dusk, cinematic wide', at='millones de casas vacías'))
NAR("[pause] En el próximo documental de DocuVox: Bankia. El banco que salió a bolsa con trescientos cuarenta mil pequeños ahorradores y pidió el rescate diez meses después. Suscríbete para no perdértelo.",
    ph('Torre Bankia Plaza de Castilla', at='Bankia'),
    cd(dict(type='kw', word='PRÓXIMAMENTE: BANKIA', sub='suscríbete a DocuVox'), at='Suscríbete'))
