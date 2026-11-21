# -*- coding: utf-8 -*-
# «Crisis de 2008» · parte 2: la caída de Lehman, seis millones de parados y las casas vacías
from lib import *

# ---------------- CAPÍTULO 3 · EL DÍA QUE CAYÓ LEHMAN ----------------
T('El día que cayó Lehman', '2008', num='III', secs=4.5, sting='tema')
B('tension')
NAR("[serious] Nueva York, lunes quince de septiembre de dos mil ocho, una y cuarenta y cinco de la madrugada. Lehman Brothers, el cuarto banco de inversión de Estados Unidos, con ciento cincuenta y ocho años de historia, presenta la mayor quiebra de la historia del país.",
    ph('Lehman Brothers headquarters September 2008', at='Lehman Brothers', lt=['Lehman Brothers', 'Nueva York · 15 de septiembre de 2008', 'banca']),
    ai('noche_ny', 'a Manhattan skyscraper at night with only a few lit windows, police cars and TV vans on the street below, rain, dramatic', at='una y cuarenta y cinco de la madrugada'))
DAT("Deudas por más de seiscientos mil millones de dólares. Más que el producto interior bruto de muchos países enteros.",
    cd(dict(type='counter', to=600000, label='millones de dólares en deudas · más de', prefix='$'), at='seiscientos mil millones'))
NEW("Por la mañana, las cámaras de televisión de todo el mundo graban la misma escena: empleados saliendo del edificio con sus cosas en cajas de cartón. Veinticinco mil personas se quedaban sin trabajo de golpe.",
    ph('Lehman Brothers employees leaving boxes 2008', at='cajas de cartón'),
    ai('cajas_carton', 'office workers in suits carrying cardboard boxes out of a glass skyscraper lobby into a crowd of press photographers with flashes, seen from behind, action', at='empleados saliendo del edificio'))
NAR("¿Cómo podía caer un gigante así? Porque llevaba años comprando, empaquetando y revendiendo lo mismo que había hundido las casas americanas: hipotecas que nunca se iban a pagar. Y cuando esos paquetes dejaron de valer nada, nadie quiso rescatarlo.",
    ai('paquetes_hipotecas', 'a towering stack of bound mortgage files wrapped like gift packages collapsing on a trading desk, papers flying, dramatic motion', at='empaquetando y revendiendo'))
NEW("Tres semanas después, su presidente, Richard Fuld, tuvo que explicarse ante el Congreso de los Estados Unidos.",
    ph('Richard Fuld Congress 2008', at='Richard Fuld', lt=['Richard Fuld', 'Presidente de Lehman Brothers', 'banca']))
USA("Me despierto cada noche preguntándome qué podría haber hecho de otra manera.",
    cd(dict(type='quote', text='Me despierto cada noche preguntándome qué podría haber hecho de otra manera.', attrib='Richard Fuld ante el Congreso de EE. UU. · 6 de octubre de 2008 (traducción)'), at='Me despierto'))
B('accion')
NAR("[dramatically] Lo que vino después se llamó pánico. Las bolsas se desploman. Los bancos dejan de fiarse unos de otros. En Estados Unidos, el Gobierno rescata a la mayor aseguradora del mundo. En Europa caen bancos en Islandia, en Irlanda, en Bélgica, en el Reino Unido.",
    ph('Wall Street October 2008', at='Las bolsas se desploman'),
    ai('pantalla_desplome', 'a giant electronic stock board showing plunging red arrows over a crowded street, people stopped looking up, night, motion', at='Lo que vino después se llamó pánico'),
    cd(dict(type='map', title='El contagio · otoño de 2008', bbox=[-75, 25, 30, 66], points=[dict(name='Nueva York', lon=-74.0, lat=40.7, big=1), dict(name='Reikiavik', lon=-21.9, lat=64.1), dict(name='Dublín', lon=-6.26, lat=53.35), dict(name='Londres', lon=-0.13, lat=51.51), dict(name='Bruselas', lon=4.35, lat=50.85), dict(name='Madrid', lon=-3.70, lat=40.42)], arrows=[dict(path=[[-74.0, 40.7], [-30, 50], [-6.26, 53.35]]), dict(path=[[-74.0, 40.7], [-35, 42], [-3.70, 40.42]])]), at='En Europa caen bancos'))
DAT("La Bolsa española no se libró. El Ibex treinta y cinco, el índice de las grandes empresas cotizadas, cerró dos mil ocho con una caída de casi el cuarenta por ciento. El peor año de su historia.",
    cd(dict(type='counter', to=39.4, dec=1, prefix='−', suffix=' %', label='caída del Ibex 35 en 2008 · el peor año de su historia'), at='El Ibex treinta y cinco'))
PRE("Tres de octubre de dos mil ocho. El Congreso de Estados Unidos aprueba, al segundo intento, un plan de rescate de setecientos mil millones de dólares para comprar los activos tóxicos de los bancos. Unos días antes lo había rechazado y Wall Street había vivido su mayor caída en puntos de la historia.",
    ph('United States Capitol 2008', at='El Congreso de Estados Unidos'),
    cd(dict(type='counter', to=700000, label='millones de dólares · plan de rescate de EE. UU. (TARP)', prefix='$'), at='setecientos mil millones'))
DOC("En España, el Gobierno aprueba en octubre un fondo de hasta cincuenta mil millones de euros para comprar activos a los bancos y avales públicos de hasta cien mil millones para que pudieran seguir financiándose.",
    cd(dict(type='list', header='España · octubre de 2008', items=[('Fondo de Adquisición de Activos Financieros', 'hasta 50.000 millones'), ('Avales del Estado a la banca', 'hasta 100.000 millones')]), at='En España, el Gobierno aprueba'))
NEW("Y España, que juraba estar a salvo, descubrió que el problema no era americano. Era suyo. Porque aquí no había hipotecas basura empaquetadas: había algo peor. Un país entero endeudado para comprar casas que valían mucho menos de lo que se había pagado por ellas.",
    ai('balance_ladrillo', 'an old-fashioned balance scale with a stack of house keys on one side and a mountain of debt papers on the other, the debt side crashing down, dramatic', at='era suyo'))
NAR("En septiembre de dos mil ocho, el presidente del Gobierno llegó a presumir en Nueva York de que la banca española era probablemente la más sólida del mundo. Y en parte lo parecía: los grandes bancos no habían comprado apenas aquellos paquetes tóxicos americanos. El veneno estaba en otro sitio. En los balances de las cajas. Y en los pisos sin vender.",
    ai('veneno_balance', 'a cracked marble savings bank facade with dark water seeping through the cracks into the street, symbolic editorial image, night, dramatic', at='El veneno estaba en otro sitio'))
DAT("La deuda de las familias españolas superaba ya el ochenta por ciento de todo lo que producía el país en un año. Y el crédito a promotores y constructoras pasaba del cuarenta por ciento.",
    cd(dict(type='split', left=dict(title='Deuda de las familias', lines=['Más del 80 % del PIB']), right=dict(title='Crédito al ladrillo', lines=['Cerca del 42 % del PIB', 'a promotoras y constructoras']), strike=False), at='La deuda de las familias españolas'))
NAR("De hecho, el primer gran golpe había llegado aquí dos meses antes que Lehman. Julio de dos mil ocho. La inmobiliaria Martinsa-Fadesa, una de las mayores del país, se declara en concurso de acreedores. La mayor suspensión de pagos de la historia de España.",
    ph('Martinsa Fadesa', at='Martinsa-Fadesa', lt=['Martinsa-Fadesa', 'Inmobiliaria · concurso en julio de 2008', 'banca']),
    ai('oficina_cerrada', 'a modern real estate company headquarters lobby with the lights being switched off, a security guard locking a glass door, evening, empty', at='concurso de acreedores'))
NEW("Mientras tanto, el Gobierno seguía evitando una palabra. Durante la primera mitad de dos mil ocho, el presidente habló de desaceleración, de dificultades, de un ajuste. Hasta el verano no pronunció en público la palabra crisis.",
    ph('Zapatero 2008', at='el presidente habló de desaceleración'),
    cd(dict(type='kw', word='«DESACELERACIÓN»', sub='la palabra que se usó durante meses'), at='evitando una palabra'))
NAR("[pause] Pero ya daba igual cómo se llamara. Porque en las obras de toda España, una tras otra, las hormigoneras se paraban. Y lo que venía detrás de ellas era el paro.",
    ai('hormigonera_parada', 'an abandoned concrete mixer truck in an empty construction site with weeds growing, rusted rebar sticking out of concrete, overcast, desolate', at='las hormigoneras se paraban'))

DAT("Paradójicamente, las hipotecas pronto empezaron a bajar. Para frenar el desastre, el Banco Central Europeo recortó sus tipos de interés del cuatro coma veinticinco al uno por ciento en menos de un año. El euríbor se desplomó. Pero de poco sirve que baje la cuota si te quedas sin sueldo.",
    cd(dict(type='split', left=dict(title='Julio de 2008', lines=['Tipo del BCE: 4,25 %']), right=dict(title='Mayo de 2009', lines=['Tipo del BCE: 1 %', 'el euríbor se desploma']), strike=False), at='del cuatro coma veinticinco al uno'))
# ---------------- CAPÍTULO 4 · SEIS MILLONES ----------------
T('Seis millones', '2008 · 2013', num='IV', secs=4.5, sting='tema')
B('drama')
NAR("[serious] Una oficina de empleo de cualquier barrio de España, invierno de dos mil nueve. La cola sale por la puerta y da la vuelta a la esquina. Albañiles, encofradores, electricistas, administrativos de inmobiliaria, vendedores de pisos.",
    ai('cola_inem', 'a long line of men in work jackets and a few women waiting outside a Spanish employment office in winter, breath visible, seen from behind, wide', at='La cola sale por la puerta'),
    ai('casco_banco', 'a worn construction helmet and work gloves left on a park bench, a crane silhouette far behind, cold morning, still life', at='Albañiles, encofradores'))
DAT("En el verano de dos mil siete, España tenía alrededor de un millón ochocientos mil parados. Era el mejor dato en casi treinta años.",
    cd(dict(type='counter', to=1800000, label='parados en España · verano de 2007'), at='un millón ochocientos mil'))
NEW("El ladrillo había creado millones de empleos. Y se los llevó con la misma velocidad. Más de la mitad de los puestos de trabajo de la construcción desaparecieron. Detrás cayeron las fábricas de cemento, de azulejos, de muebles, de electrodomésticos. Y los bares de las obras.",
    ai('fabrica_azulejos', 'a ceramic tile factory with stacks of unsold tiles and silent machines, a worker closing a huge metal shutter, Castellón style industrial warehouse, dusk', at='de azulejos'),
    ai('bar_obra', 'a roadside bar near a construction site with all chairs stacked on tables and a closed shutter, an empty parking lot, lonely', at='Y los bares de las obras'))
DAT("La construcción llegó a dar trabajo a unos dos millones setecientas mil personas en dos mil siete. Seis años después, no llegaba a un millón.",
    cd(dict(type='split', left=dict(title='Construcción · 2007', lines=['Unos 2,7 millones', 'de ocupados']), right=dict(title='Construcción · 2013', lines=['Menos de 1 millón']), strike=False), at='dos millones setecientas mil'))
NAR("El Gobierno intentó frenar la caída con obra pública. A finales de dos mil ocho lanza el Plan E: ocho mil millones de euros para que los ayuntamientos hicieran obras pequeñas y rápidas. Aceras, plazas, polideportivos. Dio trabajo durante unos meses. Pero cuando se acabó el dinero, el paro siguió subiendo.",
    ph('Plan E cartel obra', at='el Plan E'),
    cd(dict(type='counter', to=8000, label='millones de euros · Fondo Estatal de Inversión Local (Plan E)'), at='ocho mil millones'),
    ai('obra_acera', 'workers repaving a town sidewalk with a large official sign board without readable text, orange safety fences, sunny, busy', at='Aceras, plazas'))
PRE("En la primavera de dos mil nueve, la ministra de Economía, Elena Salgado, aseguró que ya se veían brotes verdes en la economía. La expresión se hizo tan famosa como la de la Champions. Y es que el paro siguió subiendo todavía cuatro años más.",
    ph('Elena Salgado', at='Elena Salgado', lt=['Elena Salgado', 'Ministra de Economía · 2009-2011', 'gobierno']),
    cd(dict(type='kw', word='«BROTES VERDES»', sub='primavera de 2009'), at='brotes verdes'))
DAT("El precio de aquel esfuerzo apareció en las cuentas públicas. En dos mil siete, el Estado tenía superávit y una deuda de apenas el treinta y seis por ciento del producto interior bruto. En dos mil nueve, el déficit superó el once por ciento. Y la deuda pública acabaría superando el cien por cien en dos mil catorce.",
    HOY(['2007', 'Superávit', 'Deuda pública: 36 % del PIB'], ['2009 · 2014', 'Déficit de más del 11 %', 'Deuda: más del 100 % del PIB'], at='El precio de aquel esfuerzo'))
NEW("Y llegó la segunda ola. En dos mil diez, la crisis de las hipotecas se convirtió en una crisis de deuda. Grecia pide un rescate. Los mercados empiezan a dudar de que España pueda pagar lo que debe.",
    ai('acropolis_protesta', 'a massive protest crowd in front of a parliament building with neoclassical columns, smoke, riot police lines, seen from above, action', at='Grecia pide un rescate'))
NAR("Doce de mayo de dos mil diez. El presidente sube a la tribuna del Congreso y anuncia lo que hasta pocos días antes había descartado: el mayor recorte de la democracia. Los sueldos de los funcionarios bajan un cinco por ciento. Las pensiones se congelan.",
    ph('Congreso de los Diputados hemiciclo', at='la tribuna del Congreso'),
    cd(dict(type='list', header='Recortes de mayo de 2010', items=[('Sueldos públicos', '−5 % de media'), ('Pensiones', 'congeladas en 2011'), ('Cheque bebé', 'suprimido')]), at='el mayor recorte de la democracia'))
NEW("Un año después, en el verano de dos mil once, los dos grandes partidos se ponían de acuerdo en algo casi inédito: reformar la Constitución en pocas semanas para que el pago de la deuda pública tuviera prioridad absoluta.",
    cd(dict(type='doc', title='Reforma del artículo 135 de la Constitución', lines=['Estabilidad presupuestaria', 'El pago de la deuda tendrá «prioridad absoluta»'], source='Boletín Oficial del Estado · 27 de septiembre de 2011'), at='reformar la Constitución'))
B('accion')
NAR("[dramatically] Pero antes de eso, la calle ya había estallado. Quince de mayo de dos mil once. Miles de personas, muchas de ellas jóvenes, salen a manifestarse en decenas de ciudades. Y esa noche, unas cuantas se quedan a dormir en la Puerta del Sol de Madrid.",
    ph('Acampada Sol 15M 2011', at='la Puerta del Sol', lt=['Acampada de Sol', 'Madrid · mayo de 2011', 'ciudadanos']),
    ai('sol_noche', 'thousands of young people sitting and standing in a Madrid square at night under improvised tarps and tents, hands raised, banners without readable text, epic aerial', at='la calle ya había estallado'))
PRE("[softly] El lema de aquella primera manifestación lo resumía todo.",
    ph('15M Puerta del Sol pancartas', at='El lema'))
PRE("[serious] No somos mercancía en manos de políticos y banqueros.",
    cd(dict(type='quote', text='No somos mercancía en manos de políticos y banqueros.', attrib='Lema de la manifestación del 15 de mayo de 2011 · Democracia Real Ya'), at='No somos mercancía'))
NEW("La acampada de Sol duró casi un mes y se copió en plazas de toda España. Se la conoció como el movimiento del Quince M, o de los indignados. Y de aquel movimiento saldrían, años después, nuevos partidos que cambiaron el mapa político español.",
    ph('Movimiento 15M indignados', at='los indignados'),
    ai('asamblea_plaza', 'a large open-air assembly in a city square, people sitting on the ground listening to a speaker with a megaphone seen from behind, afternoon sun, dense crowd', at='se copió en plazas de toda España'))
PRE("Cuando levantaron el campamento, a mediados de junio, colgaron una pancarta enorme en la plaza. Decía: no nos vamos, nos mudamos a tu conciencia.",
    cd(dict(type='quote', text='No nos vamos. Nos mudamos a tu conciencia.', attrib='Pancarta de la acampada de Sol · 12 de junio de 2011'), at='no nos vamos'))
B('drama')
NAR("[serious] En noviembre de dos mil once hubo elecciones y cambió el Gobierno. Pero el paro no dejó de subir. Hasta que en la primavera de dos mil trece llegó el peor dato de la historia de España.",
    ph('Mariano Rajoy 2011', at='cambió el Gobierno', lt=['Mariano Rajoy', 'Presidente del Gobierno · 2011-2018', 'gobierno']))
NEW("El nuevo Gobierno aprobó en febrero de dos mil doce una reforma laboral que abarataba el despido. Y en verano, más recortes: subió el IVA hasta el veintiuno por ciento y se suprimió la paga extra de Navidad de los funcionarios. Los dos grandes partidos, uno tras otro, acabaron aplicando el ajuste que pedía Europa.",
    cd(dict(type='list', header='Ajustes de 2012', items=[('Reforma laboral', 'febrero de 2012'), ('IVA general', 'del 18 % al 21 %'), ('Paga extra de Navidad', 'suprimida a los funcionarios')]), at='una reforma laboral'))
PRE("Y la calle respondió. Huelgas generales en marzo y en noviembre de dos mil doce. Las mareas: la verde de la educación, la blanca de la sanidad. Manifestaciones cada semana frente al Congreso.",
    ph('Huelga general 2012 España', at='Huelgas generales'),
    ai('marea_verde', 'a massive street demonstration of teachers in green t-shirts filling a wide Madrid avenue, drums, banners without readable text, aerial epic, action', at='Las mareas'))
DAT("Seis millones doscientas dos mil setecientas personas en paro. El veintisiete por ciento de la población activa. Más de uno de cada cuatro españoles que querían trabajar.",
    cd(dict(type='counter', to=6202700, label='parados · primer trimestre de 2013, récord histórico'), at='Seis millones doscientas dos mil'),
    cd(dict(type='counter', to=27.16, dec=2, suffix=' %', label='tasa de paro · récord desde 1976'), at='El veintisiete por ciento'))
DAT("Entre los menores de veinticinco años, el paro llegó al cincuenta y siete por ciento. Y había casi dos millones de hogares en los que no trabajaba nadie.",
    cd(dict(type='split', left=dict(title='Paro juvenil', lines=['57 %', 'menores de 25 años']), right=dict(title='Hogares sin ingresos de trabajo', lines=['Casi 2 millones', 'todos sus miembros en paro']), strike=False), at='Entre los menores de veinticinco'))
NEW("Fue la generación que había oído toda su vida que estudiar y comprarse un piso era el camino seguro. Muchos hicieron las maletas y se fueron a Alemania, al Reino Unido o a Francia a buscar lo que aquí no había.",
    ai('aeropuerto_maletas', 'a young woman with a large suitcase walking through an airport departures hall toward the gates, seen from behind, a parent waving in the distance, emotional light', at='hicieron las maletas'))
NAR("[pause] Seis millones de parados. Un país que había presumido de jugar la Champions League se había convertido, en apenas cinco años, en el segundo con más paro de toda la Unión Europea, solo por detrás de Grecia. [short pause] Y todavía faltaba la peor parte de la historia.",
    cd(dict(type='kw', word='SEGUNDO EN PARO DE LA UE', sub='solo por detrás de Grecia · 2013'), at='el segundo con más paro'))
B('fondo')
NEW("[short pause] Antes de seguir, recapitulemos. Hasta aquí, cuatro claves.",
    cd(dict(type='recap', title='Hasta aquí', items=[('Dinero barato y suelo abierto', 'el euro y la ley de 1998'), ('Más de 800.000 casas al año', 'muchas sin comprador real'), ('Lehman cae en 2008', 'y el crédito se corta'), ('6,2 millones de parados', 'el peor dato de la historia')]), at='recapitulemos'))
NAR("Y ahora viene lo que más dolió. Porque perder el trabajo es terrible. Pero perder el trabajo con una hipoteca a treinta años firmada en lo más alto de la burbuja era otra cosa. [pause] Era perder la casa. Y seguir debiéndola.",
    ai('llaves_mesa', 'a set of house keys left on an empty kitchen counter of a vacated apartment, an open door behind, dusty light, melancholy close-up', at='Era perder la casa'))
NEW("Por cierto, si te está gustando, en DocuVox preparamos la siguiente historia: Bankia, el banco que salió a bolsa y pidió el rescate diez meses después. Suscríbete para no perdértela.",
    ph('Torre Bankia Madrid', at='Bankia, el banco'))

# ---------------- CAPÍTULO 5 · LAS CASAS VACÍAS ----------------
T('Las casas vacías', '2009 · 2014', num='V', secs=4.5, sting='tema')
B('drama')
NAR("[serious] Una mañana cualquiera de dos mil doce, en un bloque de cualquier barrio obrero. Llega la comisión judicial. Llega la policía. Y delante del portal esperan decenas de vecinos con camisetas verdes, dispuestos a impedir que una familia se quede en la calle.",
    ph('Stop Desahucios PAH', at='camisetas verdes', lt=['Plataforma de Afectados por la Hipoteca', 'Stop Desahucios', 'ciudadanos']),
    ai('portal_vecinos', 'dozens of neighbours wearing green t-shirts standing arm in arm in front of an apartment building door facing a line of police, seen from behind the police, tense standoff', at='esperan decenas de vecinos'))
NEW("Eran de la Plataforma de Afectados por la Hipoteca, la PAH, nacida en Barcelona en dos mil nueve. Su campaña Stop Desahucios convirtió en noticia diaria algo que hasta entonces pasaba en silencio.",
    ph('Plataforma de Afectados por la Hipoteca manifestación', at='nacida en Barcelona'))
PRE("Las imágenes de aquellos desahucios se convirtieron en parte del paisaje: cerrajeros cambiando cerraduras, muebles en la acera, vecinos sentados en el portal. Muchas veces el desahucio se aplazaba en el último minuto. Muchas otras, no.",
    ai('muebles_acera', 'household furniture, a mattress and cardboard boxes piled on a city sidewalk in front of an apartment building, a locksmith working at the door in the background, overcast morning', at='muebles en la acera'))
DAT("Las cifras del Consejo General del Poder Judicial dan la dimensión. En dos mil ocho se iniciaron cincuenta y ocho mil ejecuciones hipotecarias. En dos mil nueve, más de noventa y tres mil. Entre dos mil ocho y dos mil catorce, según los cálculos de Amnistía Internacional, más de medio millón.",
    cd(dict(type='timeline', header='Ejecuciones hipotecarias iniciadas', events=[('2008', '58.686'), ('2009', '93.319'), ('2008-2014', 'más de medio millón')]), at='Las cifras del Consejo General'),
    cd(dict(type='counter', to=578000, label='ejecuciones hipotecarias iniciadas · 2008-2014 (estimación de Amnistía Internacional)'), at='más de medio millón'))
DAT("Un dato para comparar con hoy. En aquellos años, la mayoría de los desahucios eran por no poder pagar la hipoteca. Desde dos mil quince, más de la mitad son por no poder pagar el alquiler.",
    HOY(['Años de la crisis', 'La mayoría de desahucios', 'por hipoteca'], ['Desde 2015', 'Más de la mitad', 'por impago del alquiler'], at='Un dato para comparar con hoy'))
NEW("Y había un detalle de la ley española que muchos desconocían cuando firmaron. Si el banco se quedaba con tu casa y la subastaba por menos de lo que debías, la diferencia la seguías debiendo tú. Te quedabas sin casa. Y con la deuda.",
    cd(dict(type='split', left=dict(title='Lo que muchos creían', lines=['Si no pago, entrego la casa', 'y la deuda se acaba']), right=dict(title='Lo que decía la ley', lines=['El banco subasta la casa', 'lo que falte, lo sigues debiendo']), strike=True), at='un detalle de la ley española'),
    ai('subasta', 'a nearly empty courtroom auction with a clerk at a desk and a single bidder raising a paper, cold fluorescent light, no readable text', at='la subastaba por menos'))
DOC("Lo dice el artículo mil novecientos once del Código Civil, vigente desde el siglo diecinueve: del cumplimiento de las obligaciones responde el deudor con todos sus bienes, presentes y futuros.",
    cd(dict(type='doc', title='Código Civil · artículo 1911', lines=['Del cumplimiento de las obligaciones responde el deudor', 'con todos sus bienes, presentes y futuros'], source='Código Civil español · 1889'), at='artículo mil novecientos once'))
PRE("En dos mil trece, una iniciativa legislativa popular para cambiar esa ley, la de la dación en pago, llegó al Congreso con casi un millón y medio de firmas. Ese mismo año, el Tribunal de Justicia de la Unión Europea dio la razón a un vecino de Martorell, en Barcelona, frente a las cláusulas de su hipoteca. La ley tuvo que cambiar.",
    ph('Tribunal de Justicia de la Unión Europea Luxemburgo', at='el Tribunal de Justicia de la Unión Europea'),
    ai('cajas_firmas', 'dozens of cardboard boxes full of signed petition sheets stacked in front of a parliament entrance, volunteers carrying more, sunny, hopeful', at='casi un millón y medio de firmas'))
NEW("Y a los desahucios se sumaron otros escándalos. Las cláusulas suelo, que impedían que la cuota de la hipoteca bajara aunque bajara el euríbor, fueron anuladas por el Tribunal Supremo en mayo de dos mil trece si no se habían explicado con claridad. Y las participaciones preferentes: productos complejos que las cajas vendieron como si fueran depósitos a cientos de miles de ahorradores, muchos de ellos jubilados.",
    ph('Tribunal Supremo Madrid', at='el Tribunal Supremo'),
    ai('jubilados_protesta', 'a group of elderly people with umbrellas protesting peacefully in front of a bank branch, holding handmade signs without readable text, rain, dignified', at='muchos de ellos jubilados'))
DAT("Las cláusulas suelo estaban en una parte enorme de las hipotecas firmadas durante la burbuja. Años después, el Tribunal de Justicia de la Unión Europea obligó en dos mil dieciséis a devolver todo lo cobrado de más desde el principio.",
    cd(dict(type='kw', word='CLÁUSULA SUELO', sub='anulada si no se explicó con claridad · Supremo, 2013 · TJUE, 2016'), at='Las cláusulas suelo estaban'))
NAR("[pause] Mientras miles de familias perdían su casa, el país estaba lleno de casas vacías. El censo de dos mil once contó más de tres millones cuatrocientas mil viviendas sin nadie dentro.",
    cd(dict(type='counter', to=3400000, label='viviendas vacías · Censo de 2011, más de'), at='tres millones cuatrocientas mil'),
    ai('bloque_vacio', 'a brand new apartment building at night with every window dark except one, a bank for-sale banner without readable text hanging on the facade, eerie', at='lleno de casas vacías'))
B('ironia')
NEW("Y luego estaban los monumentos de la burbuja. Castellón, veinticinco de marzo de dos mil once. Se inaugura un aeropuerto que ha costado más de ciento cincuenta millones de euros. Hay autobuses fletados, discursos y fanfarria. Lo único que no hay son aviones.",
    ph('Aeropuerto de Castellón', at='Se inaugura un aeropuerto', lt=['Aeropuerto de Castellón', 'Vilanova d\'Alcolea · inaugurado en 2011']),
    ai('pista_vacia', 'an enormous brand new airport runway completely empty under a blue sky, a crowd of visitors in festive clothes walking on the tarmac, no planes, absurd', at='Lo único que no hay son aviones'))
NAR("Su gran impulsor, el presidente de la Diputación, Carlos Fabra, respondió así a las críticas aquel mismo día.",
    ph('Carlos Fabra', at='Carlos Fabra', lt=['Carlos Fabra', 'Presidente de la Diputación de Castellón', 'gobierno']))
FAB("Hay quien dice que estamos locos por inaugurar un aeropuerto sin aviones. No han entendido nada. Es un aeropuerto para las personas.",
    cd(dict(type='quote', text='Hay quien dice que estamos locos por inaugurar un aeropuerto sin aviones. No han entendido nada.', attrib='Carlos Fabra · inauguración del aeropuerto de Castellón, 25 de marzo de 2011'), at='Hay quien dice'))
NEW("Aquel día invitó a los vecinos a pasear por las pistas. Junto a la entrada se levantó una escultura de veinticuatro metros en homenaje al impulsor de la obra. El primer vuelo comercial tardó cuatro años en llegar. Para entonces, Fabra ya estaba en prisión, condenado por fraude fiscal.",
    ai('escultura_gigante', 'a 24 meter tall abstract metal sculpture of a giant figure beside an empty airport access road, low angle, dramatic sky, slightly absurd', at='una escultura de veinticuatro metros'),
    ai('primer_avion', 'a single passenger airplane landing at a lonely modern airport at sunrise, a few people watching behind a fence, hopeful light', at='El primer vuelo comercial'))
NAR("No fue el único. El aeropuerto de Ciudad Real costó más de mil millones de euros, abrió en plena crisis y cerró en dos mil doce casi sin haber tenido pasajeros.",
    ph('Aeropuerto de Ciudad Real', at='El aeropuerto de Ciudad Real', lt=['Aeropuerto de Ciudad Real', 'Castilla-La Mancha']))
B('drama')
NEW("Y en Seseña, la ciudad de El Pocero se quedó a medias. De los trece mil quinientos pisos proyectados se terminaron unos cinco mil seiscientos. En aquellos años vivían allí poco más de dos mil personas. Bloques enteros vacíos, calles sin coches, locales con la persiana bajada. La prensa extranjera empezó a llamarla la ciudad fantasma.",
    ph('Seseña Residencial Francisco Hernando vacío', at='se quedó a medias'),
    cd(dict(type='split', left=dict(title='Proyectados', lines=['13.500 pisos']), right=dict(title='Terminados', lines=['Unos 5.600', 'y unos 2.300 vecinos']), strike=False), at='se terminaron unos cinco mil seiscientos'),
    ai('calle_fantasma', 'a wide empty avenue between red brick apartment blocks with closed shop shutters and no cars, a plastic bag blowing in the wind, harsh light, ghost town', at='la ciudad fantasma'))
NEW("El director de comunicación del grupo de Francisco Hernando lo veía de otra manera.",
    ai('rueda_prensa', 'a press conference table with microphones from several media under bright lights, an empty chair, a backdrop without readable text', at='lo veía de otra manera'))
DOC("Seseña tiene un futuro espléndido, aunque ahora viva un paréntesis.",
    cd(dict(type='quote', text='Seseña tiene un futuro espléndido, aunque ahora viva un paréntesis.', attrib='Alfredo Urdaci, director de comunicación del grupo de Francisco Hernando · en idealista'), at='Seseña tiene un futuro'))
NAR("[pause] Aquel paréntesis iba a durar más de una década. Y para que el país no se hundiera del todo, faltaba todavía la factura más grande. La que no iban a pagar los bancos. [short pause] La íbamos a pagar todos.",
    ai('factura', 'a gigantic paper bill unrolling down the steps of a classical bank building over a crowd of tiny people below, surreal, dramatic low angle', at='la factura más grande'))
