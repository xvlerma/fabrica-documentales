# -*- coding: utf-8 -*-
# «Vivir al límite» · parte 3: Tristán de Acuña, recapitulación, La Rinconada, final
from lib import *

# ---------------- 8 · TRISTÁN DE ACUÑA ----------------
T('El fin del mundo', 'Tristán de Acuña, Atlántico Sur', secs=4.5, sting='tension')
B('isla')
N("Atlántico Sur, más o menos a mitad de camino entre Ciudad del Cabo y Buenos Aires. Tristán de Acuña es una montaña volcánica que sale del océano. Y en su costa norte está el asentamiento permanente más remoto del planeta: Edimburgo de los Siete Mares.",
  MAPA('Tristán de Acuña', -12.28, -37.11, 'Tristán de Acuña', span=40, at='Atlántico Sur'),
  ph('Tristan da Cunha island', at='Tristán de Acuña es', lt=['Tristán de Acuña', 'territorio británico de ultramar']),
  ph('Edinburgh of the Seven Seas', at='Edimburgo de los Siete Mares', lt=['Edimburgo de los Siete Mares', 'el asentamiento más remoto']))
N("La isla lleva el nombre del navegante portugués Tristão da Cunha, que la avistó en mil quinientos seis, aunque el mar le impidió desembarcar. Durante siglos fue solo un punto en las cartas náuticas. Los primeros pobladores permanentes llegaron a principios del siglo diecinueve, cuando Gran Bretaña instaló allí una guarnición.",
  ph('Tristão da Cunha navigator portrait', at='Tristão da Cunha', lt=['Tristão da Cunha', 'navegante portugués · 1506']),
  ph('Tristan da Cunha old map', at='en las cartas náuticas'))
C("El vecino más cercano está en la isla de Santa Elena, a unos dos mil cuatrocientos kilómetros. Ciudad del Cabo, a casi dos mil ochocientos. No hay aeropuerto. No hay puerto profundo. Solo se llega por mar.",
  cd(dict(type='list', header='Tristán de Acuña', items=['Santa Elena: unos 2.400 km', 'Ciudad del Cabo: unos 2.800 km', 'Sin aeropuerto', 'Solo se llega en barco']), at='El vecino más cercano'))
N("El periodista Andy Isaacson llegó a bordo de un buque polar sudafricano, el Agulhas Dos. Lo contó en National Geographic: es uno de los apenas nueve viajes programados al año desde Ciudad del Cabo. Siete días de mar a la ida. Y otros siete a la vuelta.",
  ph('SA Agulhas II ship', at='el Agulhas Dos', lt=['S. A. Agulhas II', 'buque polar sudafricano']),
  cd(dict(type='counter', to=7, label='días de navegación desde Ciudad del Cabo'), at='Siete días de mar'))
C("En la isla viven unas doscientas cincuenta personas. Y comparten apenas siete apellidos, heredados de los primeros colonos y de los náufragos que se quedaron en el siglo diecinueve. Las tierras son comunales. Se pesca langosta, se cuidan ovejas y vacas, y se cultivan patatas en unas parcelas a unos cuatro kilómetros del pueblo: los Potato Patches.",
  ph('Tristan da Cunha islanders', at='En la isla viven'),
  K('7 APELLIDOS', 'Tristan da Cunha settlement houses', at='siete apellidos'),
  ph('Tristan da Cunha Potato Patches', at='los Potato Patches', lt=['Potato Patches', 'los huertos de patatas · Tristán']))
N("Para visitar la isla no basta con comprar un billete. Hay que pedir permiso al consejo de la isla y esperar a que haya plaza en uno de esos barcos. [short pause] Y si alguien enferma de gravedad, el hospital más cercano con todos los medios está a una semana de navegación.",
  ph('Tristan da Cunha harbour Calshot', at='Para visitar la isla'),
  ph('Tristan da Cunha hospital', at='si alguien enferma'))
N("Hace más de un siglo, la vida aquí era todavía más dura. Entre mil novecientos seis y mil novecientos nueve vivió en la isla un matrimonio inglés, el reverendo John Barrow y su mujer, Katherine. Ella llevó un diario, que se publicó en mil novecientos diez. Así describía el lugar:",
  ph('Tristan da Cunha settlement 1900s', at='Hace más de un siglo'),
  ph('Three Years in Tristan da Cunha Barrow book', at='Ella llevó un diario'))
R('DOC', "No hay comunicación regular con la isla, y no tiene puerto. [pause] A veces pasan meses sin que se vean el té, el café, el azúcar, la harina, la sal o el jabón. [short pause] En cuanto a la comida, las patatas ocupan el lugar del pan.",
  cd(dict(type='doc', title='Three Years in Tristan da Cunha', lines=['«A veces pasan meses sin que se vean el té, el café, el azúcar, la harina, la sal o el jabón.»'], source='Katherine M. Barrow, 1910 · dominio público · traducción'), at='No hay comunicación'))
C("Hoy hay electricidad, internet por satélite, una escuela, un pequeño hospital, un supermercado y hasta un bar, el Albatross. Pero los barcos siguen mandando. Si el mar está bravo, ni siquiera se puede desembarcar: el puerto es diminuto y hay días en que las lanchas no pueden salir.",
  ph('Albatross Bar Tristan da Cunha', at='hasta un bar', lt=['Albatross Bar', 'Edimburgo de los Siete Mares']),
  ph('Tristan da Cunha harbour boats waves', at='Si el mar está bravo'))
N("La isla tiene incluso código postal británico, para que los pedidos por internet encuentren el camino. Aunque tarden meses en llegar. Vive de la pesca de langosta y de sus sellos de correos, muy buscados por los coleccionistas. Y alrededor, en las islas vecinas deshabitadas, anidan millones de aves marinas, como los pingüinos de penacho amarillo.",
  ph('Tristan da Cunha stamps', at='sus sellos de correos'),
  ph('rockhopper penguin Tristan da Cunha', at='los pingüinos de penacho amarillo', lt=['Pingüino de penacho amarillo', 'Tristán de Acuña']))
C("Pero el gran capítulo de Tristán llegó en mil novecientos sesenta y uno. En agosto empezaron los temblores. En octubre, la tierra se abrió a unos cientos de metros de las casas. El volcán estaba entrando en erupción junto al pueblo.",
  ph('Tristan da Cunha 1961 eruption', at='en mil novecientos sesenta y uno'),
  cd(dict(type='timeline', header='1961-1963', events=[['agosto 1961', 'temblores'], ['10 de octubre', 'erupción y evacuación'], ['1962', 'los isleños en Inglaterra'], ['1963', 'la mayoría vuelve']]), at='En agosto'))
N("El diez de octubre de mil novecientos sesenta y uno, los doscientos sesenta y cuatro vecinos de la isla fueron evacuados. Primero a la isla de Nightingale. Luego, en barco, a Ciudad del Cabo. Y desde allí a Inglaterra.",
  ph('Tristan da Cunha evacuees 1961', at='fueron evacuados'),
  ph('Nightingale Island Tristan', at='la isla de Nightingale'),
  ph('Tristan da Cunha islanders Southampton 1961', at='a Inglaterra', lt=['Llegada a Southampton', '1961']))
C("Les dieron casas en un antiguo cuartel de la aviación, cerca de Southampton. Calles asfaltadas, coches, televisión, trabajo. Todo lo que en la isla no tenían. [pause] ¿Y qué hicieron? Cuando los científicos dijeron que el volcán se había calmado, la gran mayoría votó volver. Y en mil novecientos sesenta y tres, volvieron. A su roca. En mitad del océano.",
  ph('Calshot Tristan da Cunha islanders', at='Les dieron casas', lt=['Calshot', 'Hampshire, Inglaterra']),
  ph('Tristan da Cunha return 1963', at='la gran mayoría votó volver'),
  K('VOLVER', 'Tristan da Cunha island sea', at='A su roca'))
N("Es quizá la mejor respuesta a la pregunta de este documental. Esta gente había conocido la vida cómoda. Y eligió el aislamiento. [short pause] Pero no todos los que viven al límite lo eligen por amor a su tierra. A veces, lo que te ata a un lugar imposible es otra cosa. Brilla. Y pesa muy poco.",
  ph('Edinburgh of the Seven Seas church St Mary', at='Es quizá la mejor respuesta'),
  K('ORO', 'gold nugget', at='Brilla'))
M('isla', 10)

# ---------------- RECAPITULACIÓN 2 ----------------
B('tema')
C("Recapitulemos. Hemos visto a gente que vive bajo tierra, sobre hielo, a sesenta grados bajo cero, bajo cuatro meses de noche, en un único edificio, dentro de un volcán y a una semana de barco del vecino más cercano. Falta el último límite. El que no se ve. El aire.",
  cd(dict(type='recap', title='Hasta aquí', items=[['Longyearbyen', 'casi cuatro meses sin sol'], ['Whittier', 'un pueblo en un edificio'], ['Aogashima', 'un volcán dentro de otro'], ['Tristán de Acuña', 'a una semana del vecino más cercano']]), at='Recapitulemos'),
  K('EL AIRE', 'Andes high altitude thin air', at='El aire'))

# ---------------- 9 · LA RINCONADA ----------------
T('El techo del mundo', 'La Rinconada, Perú', secs=5.0, sting='tension')
B('andes')
N("Volvemos al principio. Cordillera de los Andes, región de Puno, al sureste del Perú. En la ladera del monte Ananea, bajo un glaciar que los vecinos llaman La Bella Durmiente, está La Rinconada. Entre cinco mil y cinco mil trescientos metros de altitud. El asentamiento permanente más alto de la Tierra.",
  MAPA('La Rinconada', -69.45, -14.63, 'La Rinconada', span=25, at='Volvemos al principio'),
  ph('La Rinconada Bella Durmiente glacier', at='La Bella Durmiente', lt=['Glaciar La Bella Durmiente', 'monte Ananea, Perú']),
  ph('La Rinconada Peru aerial', at='El asentamiento permanente más alto'))
C("¿Cuánta gente vive aquí? Nadie lo sabe con exactitud. La agencia oficial peruana Andina habla de unas doce mil seiscientas personas. Otras estimaciones superan las treinta mil. La población sube y baja con algo que se decide muy lejos: el precio del oro.",
  cd(dict(type='split', left=dict(title='Andina (agencia oficial)', lines=['unos 12.600 habitantes']), right=dict(title='Otras estimaciones', lines=['más de 30.000', 'según el precio del oro']), strike=False), at='Cuánta gente vive aquí'))
N("Entre dos mil y dos mil nueve, la población creció más de un doscientos treinta por ciento. Es lo que ocurrió cuando el precio del oro se disparó. Llegaban familias enteras de todo el sur del Perú, con lo puesto, a levantar casas de chapa en la nieve.",
  cd(dict(type='counter', to=230, prefix='+', label='por ciento de población · 2000-2009 · NASA'), at='más de un doscientos treinta'),
  ph('La Rinconada houses tin roofs', at='casas de chapa'))
C("El pueblo nació como un campamento minero temporal hace unas cuatro décadas. Por eso nadie instaló los servicios de una ciudad. No hay red de alcantarillado. Mercurio, cianuro y aguas residuales corren por zanjas abiertas en mitad de la calle.",
  ph('La Rinconada street', at='El pueblo nació'),
  ph('La Rinconada pollution waste', at='Mercurio, cianuro'))
C("La mayoría de las casas son de chapa y bloques, sin calefacción. Por la noche, las familias duermen con varias mantas y la ropa puesta. Y la luz eléctrica, el agua y el gas son un lujo que no todos tienen. Todo cuesta más, porque todo hay que subirlo por una carretera de montaña.",
  ph('La Rinconada houses', at='La mayoría de las casas'),
  ph('La Rinconada road mountain', at='por una carretera de montaña'))
N("Y luego está el trabajo. Muchos mineros trabajan en las minas de la Corporación Ananea con un sistema antiguo llamado cachorreo.",
  ph('La Rinconada mine entrance', at='Y luego está el trabajo'),
  K('CACHORREO', 'La Rinconada miners', at='cachorreo'))
R('DOC', "Cachorreo: treinta días de trabajo sin sueldo. Después, uno o dos días, según a quién se pregunte, en los que el minero se queda con todo el mineral que pueda sacar para sí mismo.",
  cd(dict(type='doc', title='Cachorreo', lines=['30 días sin sueldo · 1 o 2 días para uno mismo'], source='Roads & Kingdoms, 2016'), at='Cachorreo'))
C("Es una lotería. Ese día puede salir una piedra con una fortuna dentro. O nada. Y fuera de la mina, cientos de mujeres, las pallaqueras, rebuscan oro entre las rocas que la mina ha desechado, con las manos, bajo el viento y la nieve.",
  ph('La Rinconada gold ore', at='Es una lotería'),
  ph('pallaqueras La Rinconada women', at='las pallaqueras', lt=['Pallaqueras', 'buscadoras de oro entre los desechos']))
N("[short pause] Un hombre llamado Castañeda se lo describió así a la revista de viajes Roads and Kingdoms:",
  ph('La Rinconada night', at='Un hombre llamado'))
R('T4', "La Rinconada es un lugar solitario para trabajar. La gente echa muchas horas para ganarse la vida y mantener a su familia. Y otros trabajan para gastarse el dinero en alcohol, drogas y prostitución.",
  Q('La Rinconada es un lugar solitario para trabajar.', 'Castañeda · Roads & Kingdoms, 2016 · traducción', at='La Rinconada es un lugar'))
N("La temperatura media del año ronda un grado sobre cero. Los días son fríos y las noches hielan. En la época de lluvias, la nieve y el barro lo cubren todo. No crece un solo árbol. Y la basura se acumula en las laderas, porque durante años no hubo un sistema para retirarla.",
  ph('La Rinconada snow houses', at='La temperatura media'),
  ph('La Rinconada garbage slope', at='la basura se acumula'))
C("Encima del pueblo, el glaciar La Bella Durmiente se encoge año tras año. El agua de su deshielo baja contaminada por los restos de la minería. Y río abajo, hacia el lago Titicaca, los científicos y las autoridades peruanas vigilan la presencia de mercurio.",
  ph('La Rinconada glacier lake', at='se encoge año tras año'),
  ph('Lake Titicaca', at='hacia el lago Titicaca', lt=['Lago Titicaca', 'Perú y Bolivia']))
C("Se la ha llegado a llamar la ciudad sin ley del Perú. Ha sido escenario de conflictos mineros, de asesinatos, de contrabando de oro y de trata de mujeres. El oro informal sale de aquí y, a través de intermediarios, acaba en el mercado mundial.",
  K('SIN LEY', 'La Rinconada town night', at='la ciudad sin ley'),
  ph('La Rinconada gold miners mountain', at='El oro informal'))
N("Y todo esto, a una altura donde el cuerpo humano no debería poder vivir. A cinco mil cien metros, la presión del aire es más o menos la mitad que al nivel del mar. Cada respiración aporta mucho menos oxígeno. Para compensar, el cuerpo fabrica más glóbulos rojos.",
  vd('high altitude Andes mountains snow', at='Y todo esto'),
  cd(dict(type='counter', to=50, label='por ciento de presión del aire · a 5.100 m'), at='la mitad'))
C("En dos mil diecinueve, un equipo de científicos franceses montó un laboratorio en La Rinconada. Lo dirigía el fisiólogo Samuel Vergès, de la Universidad de Grenoble. Llegaron con una idea muy clara de lo que tenían delante.",
  ph('La Rinconada Peru miners town', at='En dos mil diecinueve'))
R('T1', "Normalmente se considera que la vida humana permanente no es posible por encima de los cinco mil metros. La población de La Rinconada es un auténtico desafío para el conocimiento.",
  Q('Se considera que la vida humana permanente no es posible por encima de los 5.000 metros.', 'Samuel Vergès, fisiólogo · Inserm-Universidad de Grenoble · traducción', at='Normalmente se considera'))
N("Lo que encontraron fue asombroso. Algunos mineros tenían en la sangre más de dos kilos de hemoglobina: según el equipo, los valores más altos jamás registrados. Un habitante de Lima tiene, de media, unos setecientos cuarenta y siete gramos.",
  cd(dict(type='versus', title='Hemoglobina total en sangre', left=dict(name='Lima', lines=['al nivel del mar', 'unos 747 gramos']), right=dict(name='La Rinconada', lines=['a 5.100 metros', 'algunos, más de 2 kilos'])), at='más de dos kilos'))
R('DOC', "Estudio sobre mil quinientos noventa y cuatro habitantes de La Rinconada: la edad, el hematocrito y los años vividos en el pueblo se asocian con los síntomas del mal de montaña crónico.",
  cd(dict(type='doc', title='Frontiers in Physiology, 2020', lines=['1.594 habitantes estudiados · mal de montaña crónico'], source='Hancco, Verges y otros · Frontiers in Physiology, 2020'), at='Estudio sobre'))
R('DOC', "Este problema de salud, junto con la falta de servicios básicos adecuados, la insalubridad y la contaminación minera, afecta gravemente a la calidad de vida y a la esperanza de vida de los habitantes de La Rinconada.",
  cd(dict(type='doc', title='Agencia Andina', lines=['«Afecta gravemente a la calidad de vida y a la esperanza de vida.»'], source='Andina, agencia peruana de noticias · traducción'), at='Este problema de salud'))
C("La sangre se vuelve espesa. Llegan los dolores de cabeza, el cansancio, los mareos, el insomnio, las palpitaciones. Es el mal de montaña crónico. Y cuantos más años vive alguien aquí, más probable es que lo sufra. [short pause] Los médicos lo tienen claro: el remedio más eficaz es bajar a menos altura.",
  ph('La Rinconada Peru people', at='La sangre se vuelve espesa'),
  K('MAL DE MONTAÑA', 'Andes snow mountain', at='mal de montaña crónico'))
N("¿Y por qué no se van? Porque, para muchas familias de los Andes, La Rinconada es la única oportunidad real de ganar mucho más de lo que ganarían en su pueblo. Con un buen golpe de suerte, la vida de toda una familia puede cambiar. Y basta una historia así para que muchos otros lo intenten.",
  ph('La Rinconada Peru families', at='Y por qué no se van'),
  K('UN GOLPE DE SUERTE', 'gold nugget', at='un buen golpe de suerte'))
C("Muchos no piensan quedarse para siempre. Vienen por una temporada, por unos años, para pagar una casa abajo, en el valle, o los estudios de sus hijos. El problema es que el oro no siempre aparece. Y los años pasan. Y la montaña se queda con la salud de quien la trabaja.",
  ph('La Rinconada mountain miners', at='Muchos no piensan'),
  ph('La Rinconada mine snow', at='la montaña se queda'))
N("Y sin embargo, por la mañana, a las cinco, vuelven a subir a la mina. Con la esperanza intacta de que el día treinta y uno sea el bueno.",
  ph('La Rinconada mine workers morning', at='por la mañana'),
  vd('mountain dawn snow peaks', at='el día treinta y uno'))
M('andes', 9)

# ---------------- FINAL ----------------
T('¿Por qué se quedan?', 'Epílogo', secs=4.5, sting='tema')
B('tema')
C("Nueve lugares. Ocho límites. Y una pregunta: ¿por qué se quedan? [pause] Después de este viaje, la respuesta tiene tres caras.",
  cd(dict(type='mapfly', title='Vivir al límite', keys=[[-170, -58, 190, 75]], points=[
      dict(name='La Rinconada', lon=-69.4, lat=-14.6, at=.1), dict(name='Coober Pedy', lon=134.8, lat=-29.0, at=.15),
      dict(name='Oimiakón', lon=142.8, lat=63.5, at=.2), dict(name='Yakutsk', lon=129.7, lat=62.0, at=.25),
      dict(name='Norilsk', lon=88.2, lat=69.3, at=.3), dict(name='Longyearbyen', lon=15.6, lat=78.2, at=.35),
      dict(name='Whittier', lon=-148.7, lat=60.8, at=.4), dict(name='Aogashima', lon=139.8, lat=32.5, at=.45),
      dict(name='Tristán de Acuña', lon=-12.3, lat=-37.1, at=.5)]), at='Nueve lugares'))
N("La primera es la riqueza. El ópalo de Coober Pedy, los diamantes de Yakutia, el níquel de Norilsk, el oro de La Rinconada. Donde la tierra esconde algo valioso, siempre aparece alguien dispuesto a pagar el precio de vivir encima.",
  ph('Coober Pedy opal', at='El ópalo de Coober Pedy'),
  ph('Norilsk Nickel plant', at='el níquel de Norilsk'),
  ph('La Rinconada gold mine', at='el oro de La Rinconada'))
C("La segunda es la costumbre. Para quien ha nacido en Oimiakón, cuarenta bajo cero no es una hazaña. Es martes. Y para un niño de Whittier, ir al colegio por un túnel es lo más normal del mundo.",
  ph('Oymyakon children winter', at='Para quien ha nacido en Oimiakón'),
  K('ES MARTES', 'Oymyakon street winter', at='Es martes'),
  ph('Begich Towers Whittier', at='un niño de Whittier'))
N("Y la tercera es la más difícil de explicar. Es lo que hizo que la mayoría de aquellos doscientos sesenta y cuatro isleños, después de conocer Inglaterra, votaran volver a una roca en mitad del Atlántico. Pertenecer a un sitio. Saber que ese lugar, por duro que sea, es tuyo.",
  ph('Tristan da Cunha island', at='Y la tercera'),
  ph('Edinburgh of the Seven Seas', at='Pertenecer a un sitio'))
C("Y una advertencia. Muchos de estos lugares están cambiando deprisa. El permafrost de Yakutsk y de Norilsk se derrite. El glaciar de La Rinconada retrocede. En Svalbard, el Ártico se calienta más rápido que casi ningún otro sitio. Los límites que han definido la vida en estos lugares durante siglos se están moviendo. Y nadie sabe todavía hacia dónde.",
  ph('Yakutsk thawing permafrost', at='El permafrost de Yakutsk'),
  ph('La Rinconada glacier', at='El glaciar de La Rinconada'),
  ph('Svalbard glacier melting', at='En Svalbard'))
N("Hay algo más. En casi todos estos lugares, la gente depende de los demás mucho más que en una ciudad normal. En Whittier, tu vecino es tu edificio. En Tristán, la isla entera es una familia. En Yakutia se dice que, si un coche se para en la carretera helada, el siguiente conductor se detiene. Siempre. Porque mañana puede ser él.",
  ph('Begich Towers', at='En Whittier'),
  ph('Tristan da Cunha islanders', at='En Tristán'),
  ph('Kolyma highway winter truck', at='En Yakutia'))
C("[softly] Quizá por eso, en los mapas, estos lugares parecen límites. Pero para quienes viven allí, son simplemente casa.",
  vd('aerial mountains clouds sunrise', at='Quizá por eso'))
N("Al final, vivir al límite no es tanto una cuestión de clima como de personas. De mineros que suben cada madrugada a cinco mil metros. De niños que van a clase a cincuenta bajo cero. De isleños que prefirieron una roca a una ciudad. Gente corriente, en lugares que no lo son en absoluto.",
  ph('La Rinconada miners walking', at='De mineros'),
  ph('Oymyakon school children', at='De niños'),
  ph('Tristan da Cunha islanders', at='De isleños'))
N("[serious] Y tú, ¿aguantarías un invierno en alguno de ellos? Cuéntanos cuál elegirías en los comentarios. [pause] Esto ha sido Vivir al límite. Gracias por acompañarnos.",
  ph('La Rinconada Peru glacier', at='Y tú'),
  cd(dict(type='title', title='Vivir al límite', sub='DocuVox'), at='Esto ha sido'))
M('tema', 12, end=True)
