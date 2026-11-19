# -*- coding: utf-8 -*-
# «El oro de Moscú» · parte 1: apertura, contexto, capítulos 1 y 2
from lib import *

# ---------------- APERTURA ----------------
B('tension')
DER("[serious] Guerra Civil española. Otoño de mil novecientos treinta y seis. Una noche de octubre, en el puerto de Cartagena, cuatro barcos soviéticos cargan siete mil ochocientas cajas de madera. [short pause] Dentro va casi todo el oro de España.",
    vid('Spanish Civil War 1936 newsreel', at='Guerra Civil'),
    ph('Cartagena port 1930s', at='puerto de Cartagena', lt=['Cartagena', 'octubre de 1936']),
    cd(dict(type='counter', to=7800, label='cajas de oro del Banco de España'), at='siete mil ochocientas'),
    ph('gold bars Bank vault 1930s', at='casi todo el oro'))
IZQ("[serious] Quinientas diez toneladas. La cuarta reserva de oro del mundo. La República la envía a Moscú para pagar las armas que nadie más le quiere vender.",
    cd(dict(type='counter', to=510, label='toneladas de oro'), at='Quinientas diez'),
    ph('Banco de España Madrid fachada', at='La cuarta reserva', lt=['Banco de España', 'Madrid']),
    ph('Moscow Kremlin 1930s', at='a Moscú', lt=['Moscú', 'Unión Soviética']))
DER("Y ese oro no volvió nunca. [pause] Veinte años después, en mil novecientos cincuenta y siete, el Gobierno soviético dio su versión oficial: ya no quedaba nada. Todo se había gastado.",
    ph('Kremlin Moscow winter', at='no volvió nunca'),
    ph('Pravda newspaper 1957', at='Gobierno soviético'),
    K('NO QUEDA NADA', 'Moscow 1950s street', at='ya no quedaba nada'))
IZQ("[softly] ¿Fue la única salida de una República abandonada por las democracias? [short pause] ¿O la mayor entrega de soberanía de nuestra historia, decidida por unos pocos y en secreto?",
    ph('Spanish Republic soldiers 1936', at='República abandonada'),
    ph('Spanish Republic government 1936', at='decidida por unos pocos'))
DER("[serious] ¿Cuánto oro llegó de verdad a Moscú? ¿Quién lo contó? [pause] Y la pregunta que lleva casi noventa años abierta: ¿se pagaron armas... o se pagó algo más?",
    ph('gold coins pile', at='Cuánto oro'),
    ph('Stalin 1936', at='Quién lo contó', lt=['Iósif Stalin', 'Secretario general del Partido Comunista de la URSS', 'urss']),
    ph('Soviet T-26 tank Spain', at='se pagaron armas'))
T('El oro de Moscú', 'El viaje sin retorno de la reserva de España', secs=5.5, sting='tema', text='[dramatically] El oro de Moscú.', chapter=False)

# ---------------- CONTEXTO DE ENTRADA ----------------
B('tema')
DER("Para entender lo que pasó con ese oro hay que viajar a julio de mil novecientos treinta y seis. Una parte del Ejército se subleva contra el Gobierno de la Segunda República. El golpe fracasa en Madrid, en Barcelona, en Valencia. Pero triunfa en media España. Y empieza una guerra.",
    ph('Madrid July 1936', at='julio de mil', lt=['Madrid', 'julio de 1936']),
    cd(dict(type='map', title='España, julio de 1936', bbox=[-10, 35.5, 4.5, 44], points=[dict(name='Madrid', lon=-3.70, lat=40.42, at=0.3, big=1), dict(name='Barcelona', lon=2.17, lat=41.39, at=0.45), dict(name='Valencia', lon=-0.38, lat=39.47, at=0.55), dict(name='Sevilla', lon=-5.98, lat=37.39, at=0.65), dict(name='Burgos', lon=-3.70, lat=42.34, at=0.75)]), at='triunfa en media España'))
IZQ("De un lado, la República: un Gobierno elegido en las urnas cinco meses antes, el del Frente Popular. Del otro, los militares sublevados, que pronto tendrán un jefe: el general Francisco Franco.",
    ph('Frente Popular 1936', at='Frente Popular'),
    ph('Francisco Franco 1936', at='Francisco Franco', lt=['Francisco Franco', 'General sublevado · jefe del bando nacional desde octubre de 1936', 'derecha']))
DER("Estos son los nombres que vas a oír una y otra vez. Merece la pena retenerlos, porque todos tuvieron algo que ver con el destino del oro.",
    cd(dict(type='cast', title='Los protagonistas', groups=[
        dict(name='La República', color=IZ, people=[
            dict(name='Manuel Azaña', role='Presidente de la República', commons=IMG['azana']),
            dict(name='Francisco Largo Caballero', role='Presidente del Gobierno 1936-37', commons=IMG['largo']),
            dict(name='Juan Negrín', role='Ministro de Hacienda', commons=IMG['negrin']),
            dict(name='Indalecio Prieto', role='Ministro de Marina y Aire', commons=IMG['prieto'])]),
        dict(name='La URSS', color=SO, people=[
            dict(name='Iósif Stalin', role='Dirigente soviético', commons=IMG['stalin']),
            dict(name='Alexander Orlov', role='Jefe de la NKVD en España', commons=IMG['orlov'])]),
        dict(name='Los sublevados', color=DE, people=[
            dict(name='Francisco Franco', role='Jefe del bando nacional', commons=IMG['franco'])])]), at='Estos son'),
    )
IZQ("Y hay una palabra que conviene aclarar desde ya: la NKVD. Era la policía política de Stalin. El servicio que espiaba, detenía y ejecutaba dentro y fuera de la Unión Soviética. Uno de sus hombres va a ser el encargado de llevarse el oro.",
    ph('NKVD headquarters Lubyanka Moscow', at='la NKVD', gloss=['NKVD', 'policía política de Stalin', 'urss']),
    ph('Alexander Orlov', at='Uno de sus hombres'))
DER("[serious] Hasta hoy, dos lecturas de esta historia se enfrentan. Y en este documental vas a escuchar las dos, a dos voces.",
    cd(dict(type='versus', title='Dos lecturas', left=dict(name='La necesidad', color=IZ, lines=['la República no tenía otra salida', 'las democracias la dejaron sola']),
          right=dict(name='La entrega', color=DE, lines=['se dio el oro a Stalin sin garantías', 'y con él, la independencia'])), at='dos lecturas'))
IZQ("Una dice que la República no tuvo otra opción. La defiende, sobre todo, el historiador Ángel Viñas, que lleva casi cincuenta años estudiando los papeles del oro.",
    K('LA NECESIDAD', 'Spanish Republic poster 1936', at='no tuvo otra opción'),
    ph('Spanish Civil War archive documents', at='Ángel Viñas', lt=['Ángel Viñas', 'Historiador y diplomático', 'izquierda']))
IZQ("Para Viñas, el oro de Moscú no fue un robo ni una traición, sino el pago de una República a la que las democracias dejaron sin otra salida. Y la leyenda del robo fue, sobre todo, un invento de la propaganda de Franco.",
    ph('Spanish Republic 1936 poster defense', at='sin otra salida'))
DER("La otra sostiene que se entregó la mayor riqueza del país a una dictadura opaca, sin control, y que ese oro ató a la República a Moscú. Es la tesis de historiadores económicos como Pablo Martín Aceña. [short pause] Vamos a seguir el oro, caja a caja. Y que cada uno saque sus conclusiones.",
    K('LA ENTREGA', 'Stalin portrait 1930s', at='dictadura opaca'),
    ph('Banco de España archive ledger', at='Pablo Martín Aceña', lt=['Pablo Martín Aceña', 'Historiador económico', 'derecha']),
    ph('wooden crates warehouse 1930s', at='caja a caja'))

# ---------------- CAPÍTULO 1 ----------------
T('La cuarta reserva del mundo', 'Capítulo 1', secs=5.0, text='[serious] Capítulo uno. [short pause] La cuarta reserva del mundo.')
B('tema')
DER("Madrid, calle de Alcalá, julio de mil novecientos treinta y seis. Bajo el edificio del Banco de España hay una cámara acorazada a muchos metros de profundidad. Para llegar a ella hay que atravesar puertas blindadas y un foso que se podía inundar.",
    ph('Banco de España Madrid 1930s', at='calle de Alcalá', lt=['Banco de España', 'calle de Alcalá, Madrid']),
    ph('bank vault door 1930s', at='cámara acorazada'),
    ph('Banco de España cámara del oro', at='puertas blindadas'))
DER("Allí dentro, el día del golpe, hay más de setecientas toneladas de oro. Lingotes, sí, pero sobre todo monedas: libras inglesas, dólares, francos, pesos, liras. Siglos de comercio y de ahorro de un país entero.",
    cd(dict(type='counter', to=700, label='toneladas de oro en el Banco de España, julio de 1936'), at='setecientas toneladas'),
    ph('gold sovereign coins', at='libras inglesas'),
    ph('gold coins collection 19th century', at='Siglos de comercio'))
IZQ("Era la cuarta reserva de oro del mundo. Solo tres países guardaban más. España no había luchado en la Primera Guerra Mundial y había vendido a los dos bandos. Ese oro era el resultado.",
    K('4.ª RESERVA DEL MUNDO', 'Banco de España gold vault', at='cuarta reserva'),
    ph('Spanish neutrality World War I trade port', at='vendido a los dos bandos'))
DER("Y hay un detalle que casi nadie recuerda. En mil novecientos treinta y seis, el Banco de España no era del Estado. Era una sociedad anónima, con accionistas privados, que tenía el privilegio de emitir los billetes. No se nacionalizó hasta mil novecientos sesenta y dos.",
    ph('Banco de España share certificate', at='no era del Estado'),
    ph('peseta banknote 1931 Banco de España', at='emitir los billetes'),
    K('BANCO PRIVADO HASTA 1962', 'Banco de España building', at='mil novecientos sesenta y dos'))
DER("Ese oro respaldaba la peseta, y la ley decía que solo podía salir de la cámara con condiciones muy estrictas. [short pause] Recuérdalo, porque en septiembre esas condiciones se van a saltar.",
    ph('Banco de España gold reserve law', at='respaldaba la peseta'))
IZQ("Es verdad que era un banco privado. Pero en una guerra, la reserva de oro de un país es un asunto de Estado, la tenga quien la tenga. Ningún Gobierno del mundo habría dejado esas setecientas toneladas a merced de un ejército sublevado.",
    ph('Spanish Republic government building 1936', at='un asunto de Estado'))
IZQ("[serious] Y desde el dieciocho de julio, ese oro se convierte en la única arma que le queda a la República. Porque una guerra no se gana solo con hombres. Se gana con fusiles, con aviones, con munición. Y todo eso hay que comprarlo fuera.",
    ph('Republican militia Madrid 1936 rifles', at='la única arma'),
    ph('Spanish Civil War aircraft 1936', at='con aviones'))
DER("El Gobierno de José Giral empieza a vender oro casi enseguida. Ya en el verano de mil novecientos treinta y seis, aviones cargados de cajas salen hacia París. Allí, el Banco de Francia lo compra y la República recibe francos para pagar armas.",
    ph('José Giral', at='José Giral', lt=['José Giral', 'Presidente del Gobierno, julio-septiembre de 1936', 'izquierda']),
    ph('Barajas airport 1930s aerial', at='aviones cargados'),
    ph('Banque de France Paris 1930s', at='el Banco de Francia', lt=['Banco de Francia', 'París']))
DER("Es la otra parte de esta historia, mucho menos famosa: el llamado oro de París. Casi doscientas toneladas, más de una cuarta parte de la reserva, acabaron vendidas en Francia. [short pause] De ese oro casi nadie habla. Y no por casualidad: no sirve para la propaganda de nadie.",
    K('EL ORO DE PARÍS', 'Paris 1936 street', at='oro de París'),
    cd(dict(type='counter', to=193, label='toneladas vendidas en Francia'), at='Casi doscientas'))
IZQ("Y hay otra parte del oro de la que tampoco se habla. Desde antes de la guerra, el Banco de España guardaba unas cuarenta toneladas en Mont-de-Marsan, en el sur de Francia, como garantía de unas operaciones con el Banco de Francia. Ese oro quedó bloqueado durante toda la guerra. La República nunca pudo usarlo. [short pause] Y en mil novecientos treinta y nueve, Francia se lo entregó a Franco.",
    ph('Mont-de-Marsan France 1930s', at='Mont-de-Marsan', lt=['Mont-de-Marsan', 'Francia']),
    K('BLOQUEADO', 'Banque de France vault', at='quedó bloqueado'),
    ph('Francisco Franco 1939', at='se lo entregó a Franco'))
IZQ("Es un buen ejemplo de lo que podía pasar con el oro que la República dejara en manos de las democracias occidentales.",
    ph('Paris 1939 street', at='democracias occidentales'))
IZQ("[serious] Pero en agosto pasa algo que cambia todo. Francia y Gran Bretaña, las dos grandes democracias de Europa, proponen un pacto: nadie venderá armas a ningún bando de la guerra de España. Lo llamaron No Intervención.",
    ph('Léon Blum 1936', at='Francia', lt=['Léon Blum', 'Primer ministro de Francia', 'centro']),
    ph('Neville Chamberlain Anthony Eden 1936', at='Gran Bretaña'),
    K('NO INTERVENCIÓN', 'Non-Intervention Committee London 1936', at='No Intervención'))
IZQ("Lo más doloroso para la República es que el primer Gobierno francés de izquierdas, el de Léon Blum, quería ayudarla. En los primeros días de la guerra llegaron a salir algunos aviones franceses hacia España. Pero la presión de Londres y de la derecha francesa le hizo dar marcha atrás. Y la ayuda se cortó.",
    ph('Léon Blum Front Populaire 1936', at='Léon Blum'),
    ph('French aircraft Potez 54 Spain 1936', at='algunos aviones franceses'))
IZQ("Firmaron casi treinta países. Entre ellos, la Alemania de Hitler y la Italia de Mussolini. Y las dos siguieron mandando a Franco aviones, tanques, pilotos y soldados como si no hubieran firmado nada.",
    ph('Non-Intervention Committee meeting', at='casi treinta países'),
    ph('Hitler Mussolini 1937', at='Hitler'),
    ph('Condor Legion Junkers Spain', at='aviones, tanques'))
IZQ("[softly] Para la República, el resultado fue una trampa. Era el Gobierno legal de España. Y no podía comprar armas legalmente en casi ningún sitio. Ángel Viñas lo llama la soledad de la República.",
    ph('Spanish Republic soldiers trench 1936', at='una trampa'),
    K('LA SOLEDAD DE LA REPÚBLICA', 'Spanish Republic flag 1936', at='la soledad'))
DER("Eso es cierto. Pero hay que añadir algo. La República siguió comprando, a través de intermediarios y traficantes, en media Europa y en México. Caro y mal, pero compró. [short pause] El problema no era que el oro no sirviera. El problema era dónde ponerlo a salvo.",
    ph('Spanish Civil War arms ship', at='intermediarios'),
    ph('Mexico 1936 Lázaro Cárdenas', at='México'),
    ph('gold bars stack', at='dónde ponerlo a salvo'))
M('tema', 10)

DER("Septiembre de mil novecientos treinta y seis. Las columnas de Franco avanzan hacia Madrid desde el sur. Toledo cae a finales de mes. Muchos creen que la capital caerá antes del invierno. [short pause] Y en la capital está el oro.",
    ph('Nationalist column advance Madrid 1936', at='avanzan hacia Madrid'),
    ph('Alcázar de Toledo 1936', at='Toledo cae', lt=['Toledo', 'septiembre de 1936']),
    ph('Madrid 1936 defense barricades', at='la capital caerá'))
IZQ("El cuatro de septiembre se forma un nuevo Gobierno. Lo preside el líder socialista Francisco Largo Caballero. En Hacienda entra un médico canario, catedrático de Fisiología, que hablaba varios idiomas: Juan Negrín.",
    ph('Francisco Largo Caballero', at='Francisco Largo Caballero', lt=['Francisco Largo Caballero', 'Presidente del Gobierno', 'izquierda']),
    ph('Juan Negrín', at='Juan Negrín', lt=['Juan Negrín', 'Ministro de Hacienda', 'izquierda']))
DER("Nueve días después, el trece de septiembre, Negrín lleva a la firma del presidente Azaña un decreto reservado. Autoriza al ministro a sacar el oro y la plata del Banco de España y llevarlos a donde considere más seguro. No dice adónde. [short pause] Ese hueco en blanco es el corazón de esta historia.",
    ph('Manuel Azaña', at='presidente Azaña', lt=['Manuel Azaña', 'Presidente de la República', 'izquierda']),
    DOCC('Decreto reservado', 'Autoriza al ministro de Hacienda a trasladar el oro y la plata del Banco de España al lugar que estime más seguro.', 'Decreto de 13 de septiembre de 1936 · resumen', at='un decreto reservado'),
    K('SIN DESTINO', 'Banco de España vault', at='No dice adónde'))
DER("En el consejo del Banco de España hubo protestas: el oro era la garantía de la peseta, y la ley no permitía sacarlo así. Pero el Gobierno no esperó. [short pause] Al día siguiente, el catorce de septiembre, empezaron a vaciar la cámara.",
    ph('Banco de España consejo sala', at='consejo del Banco'),
    ph('peseta banknote 1935', at='garantía de la peseta'),
    ph('Banco de España vault gold boxes', at='vaciar la cámara'))
IZQ("Hay que entender el ambiente de esos días. Madrid está bombardeada. Las milicias piden armas a gritos. Y nadie sabe si el Gobierno seguirá en la ciudad la semana siguiente. De hecho, en noviembre se marchará a Valencia. Sacar el oro de Madrid no era una locura. Era lo que haría cualquier Gobierno.",
    ph('Madrid bombing 1936', at='Madrid está bombardeada'),
    ph('militia Madrid 1936', at='Las milicias'),
    ph('Valencia 1936', at='a Valencia', lt=['Valencia', 'sede del Gobierno desde noviembre de 1936']))
DER("Sacarlo de Madrid, no. La pregunta es otra: por qué no se quedó en España, y por qué acabó precisamente en manos de Stalin.",
    ph('Madrid Puerta de Alcalá 1936', at='Sacarlo de Madrid'),
    ph('Stalin 1930s portrait', at='manos de Stalin'))
DER("En pocos días, cientos de cajas salen en camiones y trenes hacia el sureste. Su destino: Cartagena, la gran base de la Armada republicana. Allí, en la bahía, hay unos viejos polvorines excavados en la roca: La Algameca.",
    ph('Spanish railway 1930s train', at='camiones y trenes'),
    cd(dict(type='mapfly', title='Madrid → Cartagena', keys=[[-7, 36.5, 1, 41.8], [-3, 37.2, 0, 39]], points=[dict(name='Madrid', lon=-3.70, lat=40.42, at=0.2, big=1), dict(name='Cartagena', lon=-0.98, lat=37.60, at=0.7, pulse=1, big=1)]), at='hacia el sureste'),
    ph('La Algameca Cartagena', at='La Algameca', lt=['La Algameca', 'Polvorines de la Armada · Cartagena']))
IZQ("[serious] El oro estaba lejos del frente, protegido por la Marina, y junto a un puerto. Desde Cartagena se podía llevar a cualquier parte. [short pause] A esas alturas, todavía no estaba decidido adónde.",
    ph('Cartagena naval base 1930s', at='protegido por la Marina'),
    ph('Cartagena harbour', at='a cualquier parte'))

# ---------------- CAPÍTULO 2 ----------------
T('La decisión', 'Capítulo 2', secs=5.0, text='[serious] Capítulo dos. [short pause] La decisión.')
B('tension')
DER("Octubre de mil novecientos treinta y seis. Valencia y Madrid. Lo que pasa en estas semanas lo sabemos por muy pocos papeles. Porque la decisión de mandar el oro a Moscú la tomaron muy pocas personas.",
    ph('Valencia 1936 street', at='Valencia y Madrid'),
    ph('Spanish Civil War documents archive', at='muy pocos papeles'))
DER("Según el propio Largo Caballero en sus escritos posteriores, la idea la propuso Negrín, y él la aprobó. El Consejo de Ministros no la discutió. Y a Azaña, el presidente de la República, no se le explicó el destino del oro.",
    ph('Francisco Largo Caballero 1936', at='Largo Caballero'),
    ph('Juan Negrín 1937', at='la propuso Negrín'),
    ph('Manuel Azaña 1936', at='a Azaña'))
IZQ("Y hay que ponerse en su lugar. Largo Caballero había visto caer Toledo. Sabía que, si Madrid caía con el oro dentro, la República perdía la guerra en una semana: sin dinero no hay armas, y sin armas no hay República.",
    ph('Francisco Largo Caballero front 1936', at='ponerse en su lugar'))
IZQ("Los defensores de Negrín tienen respuesta para eso. Era una operación de guerra. Si se hubiera debatido en un Consejo con veinte ministros, en una zona llena de espías, el oro no habría llegado nunca a su destino. El secreto era la única forma de protegerlo.",
    ph('Spanish Republic cabinet 1936', at='un Consejo con veinte'),
    K('SECRETO', 'Spanish Civil War telegram', at='El secreto'))
IZQ("Y recordemos quiénes eran esos pocos. No eran conspiradores. Eran el presidente del Gobierno y su ministro de Hacienda, con un decreto firmado por el presidente de la República que les autorizaba a poner el oro a salvo. Legalmente, tenían el poder para hacerlo.",
    ph('Spanish Republic Gaceta de Madrid 1936', at='un decreto firmado'))
DER("Legalmente, sí. El decreto decía «a salvo». No decía «a la Unión Soviética». Y ese destino, la decisión más trascendental de todas, no lo votó nadie más.",
    K('«A SALVO»', 'Manuel Azaña 1936', at='a salvo'))
DER("Además, el secreto tiene un precio: cuando el oro desaparece de la vista, también desaparece el control. Y el control de esta operación no lo iba a tener la República.",
    ph('locked safe 1930s', at='desaparece de la vista'))
IZQ("[serious] Vamos a las razones de fondo. ¿Por qué Moscú? Los historiadores que defienden la decisión dan tres. [short pause] La primera, que Francia y Gran Bretaña no eran de fiar. Con la No Intervención, el oro podía quedarse bloqueado en un banco de Londres o de París por presiones políticas.",
    cd(dict(type='list', header='¿Por qué Moscú?', items=[['1', 'Londres y París no eran de fiar'], ['2', 'La URSS era el único gran vendedor de armas'], ['3', 'Pagar en oro daba crédito para comprar']]), at='dan tres'),
    ph('Bank of England London 1930s', at='un banco de Londres'))
IZQ("La segunda, que la Unión Soviética era la única gran potencia dispuesta a vender armas a la República. Y la tercera, que tener el oro allí le daba a la República crédito inmediato para comprar. Su nieta, Carmen Negrín, lo resume así:",
    ph('Soviet arms factory 1930s', at='dispuesta a vender armas'),
    ph('Juan Negrín portrait', at='Carmen Negrín'))
V('HIS', "«El único país que aceptó recibirlo, protegerlo y hacerlo fructificar era la URSS.»",
  Q('El único país que aceptó recibirlo, protegerlo y hacerlo fructificar era la URSS.', 'Carmen Negrín, nieta de Juan Negrín · entrevista publicada', at='El único país'))
DER("[serious] Ahora, el otro lado. La Unión Soviética de mil novecientos treinta y seis no era un banco. Era una dictadura en plena época del Terror. Ese mismo verano habían empezado los grandes procesos de Moscú, en los que Stalin mandaba fusilar a los viejos dirigentes bolcheviques.",
    ph('Moscow trials 1936', at='procesos de Moscú', lt=['Procesos de Moscú', 'agosto de 1936']),
    ph('Stalin 1936 portrait', at='Stalin mandaba fusilar'))
DER("Era un país que no rendía cuentas a nadie. Sin prensa libre, sin tribunales independientes, sin oposición. Si un día decidía que el oro se había gastado, no había a quién reclamar. Y eso es exactamente lo que pasó.",
    ph('Kremlin walls Moscow 1930s', at='no rendía cuentas'),
    K('¿A QUIÉN RECLAMAR?', 'Moscow Red Square 1930s', at='no había a quién reclamar'))
DER("Por eso Pablo Martín Aceña sostiene que había alternativas mejores: repartir el oro entre varios países, venderlo poco a poco en distintas plazas, no poner toda la reserva en manos de un solo Estado. Viñas responde que esas alternativas, en la práctica, no existían.",
    ph('gold bars different banks', at='varios países'),
    cd(dict(type='split', left=dict(title='Martín Aceña', lines=['había alternativas', 'repartir el riesgo']), right=dict(title='Viñas', lines=['no había alternativas', 'solo la URSS vendía'])), at='Viñas responde'))
IZQ("[softly] Y conviene recordar el calendario. A mediados de octubre, Madrid parecía perdida. Los primeros barcos soviéticos con armas llegaron a España en esos mismos días. Los tanques y aviones rusos que defendieron Madrid en noviembre ya estaban en camino.",
    ph('Soviet ship Spain 1936 Komsomol', at='Los primeros barcos'),
    ph('T-26 tank Madrid 1936', at='Los tanques'),
    ph('Polikarpov I-15 Spain', at='aviones rusos'))
DER("El calendario funciona también al revés: el oro salió entero, de una sola vez, antes de saber qué se iba a recibir a cambio. No se fue pagando lo que llegaba. Se entregó todo por adelantado.",
    K('POR ADELANTADO', 'gold bars stack dark', at='por adelantado'))
M('tension', 9)
IZQ("Para entender por qué Stalin dijo que sí, hay que mirar a Moscú. Durante el verano, la Unión Soviética había firmado la No Intervención como todos. Pero a finales de septiembre, viendo que Alemania e Italia la incumplían sin disimulo, el Kremlin cambió de política. Decidió mandar armas a la República en secreto. Lo llamaron Operación X.",
    ph('Kremlin 1936', at='mirar a Moscú'),
    K('OPERACIÓN X', 'Soviet cargo ship 1936', at='Operación X'))
DER("Y aquí conviene no ser ingenuos. Stalin no ayudaba por solidaridad. Le interesaba que Hitler se desgastara en España, lejos de sus fronteras. Le interesaba ganar peso en Europa. Y le interesaba, por supuesto, cobrar.",
    ph('Stalin Molotov 1936', at='Stalin no ayudaba'),
    ph('Hitler 1936', at='que Hitler se desgastara'))
IZQ("Nadie dice que Stalin fuera un benefactor. Lo que dicen los defensores de la República es más sencillo: era el único vendedor dispuesto. Y cuando solo hay un vendedor, se compra al que hay.",
    K('EL ÚNICO VENDEDOR', 'Soviet arms factory 1936', at='el único vendedor'))
DER("¿Y Prieto, el ministro de Marina y Aire, el gran rival de Largo Caballero dentro del socialismo? Según varias versiones, se enteró del embarque casi por casualidad, porque estaba en Cartagena por otros asuntos. [short pause] Un ministro de la República descubría en un muelle adónde iba el oro de su país.",
    ph('Indalecio Prieto', at='Prieto', lt=['Indalecio Prieto', 'Ministro de Marina y Aire', 'izquierda']),
    ph('Cartagena dock 1936', at='en Cartagena por otros asuntos'))
IZQ("La petición se canalizó a través del embajador soviético en Madrid, Marcel Rosenberg, que había llegado a España a finales de agosto. Era la primera vez en la historia que la Unión Soviética tenía embajada en España.",
    ph('Marcel Rosenberg Soviet ambassador', at='Marcel Rosenberg', lt=['Marcel Rosenberg', 'Embajador soviético en Madrid', 'urss']),
    ph('Soviet embassy Madrid 1936 Palace Hotel', at='embajada en España'))
DER("Apunta su nombre, porque se repite un patrón. Rosenberg sería llamado a Moscú a principios de mil novecientos treinta y siete y, poco después, fusilado en las purgas. De los soviéticos que tocaron el oro español, muy pocos sobrevivieron a Stalin.",
    K('UN PATRÓN', 'Moscow 1937 purge', at='se repite un patrón'))
DER("En Moscú, la petición española llega al despacho de Stalin a mediados de octubre. La respuesta es rápida. Y el hombre al que se encarga la operación es Alexander Orlov, jefe de la NKVD en España.",
    ph('Stalin office Kremlin 1930s', at='despacho de Stalin'),
    ph('Alexander Orlov', at='Alexander Orlov', lt=['Alexander Orlov', 'Jefe de la NKVD en España', 'urss']))
IZQ("Orlov había llegado a Madrid en septiembre con pasaporte diplomático, como simple agregado de la embajada. Años después desertó a Estados Unidos, y en sus memorias contó cómo recibió la orden. Según su relato, era un telegrama cifrado, firmado con un nombre en clave.",
    ph('Soviet embassy Madrid 1936', at='agregado de la embajada'),
    ph('Alexander Orlov United States Senate 1955', at='desertó a Estados Unidos'),
    ph('cipher telegram 1930s', at='telegrama cifrado'))
V('ORL', "«Si los españoles exigen un recibo, rehúse, repito, rehúse. Diga que el Banco del Estado entregará un recibo oficial en Moscú. Le hago personalmente responsable de la operación.»",
  DOCC('Telegrama a Orlov', 'Si los españoles exigen un recibo, rehúse. Diga que el Banco del Estado entregará un recibo oficial en Moscú.', 'Telegrama citado por Alexander Orlov en su relato de 1967', at='Si los españoles'))
DER("[serious] No dar recibo. Esa es la primera instrucción que, según Orlov, llegó de Moscú. Hay que decirlo con cautela: es el relato de un desertor, escrito treinta años después. Pero lo que pasó en las semanas siguientes encaja con él.",
    K('SIN RECIBO', 'receipt document 1930s', at='No dar recibo'),
    ph('Alexander Orlov portrait', at='relato de un desertor'))
IZQ("Lo que sí consta en los documentos es la aprobación de Stalin y la carta en la que el Gobierno español pedía el depósito. La República no regalaba el oro: lo dejaba en depósito, a su nombre, para irlo vendiendo según lo necesitara. Sobre el papel, seguía siendo suyo.",
    ph('Spanish Republic official letter 1936', at='la carta'),
    K('EN DEPÓSITO', 'Gosbank Moscow building', at='en depósito'))
DER("Sobre el papel. [pause] La noche del veintidós de octubre, Orlov sale de Cartagena hacia La Algameca con una columna de camiones. Lo que pasó durante las tres noches siguientes es una de las operaciones más extrañas de toda la guerra.",
    ph('Cartagena night 1936', at='veintidós de octubre'),
    ph('trucks convoy 1930s night', at='una columna de camiones'))
