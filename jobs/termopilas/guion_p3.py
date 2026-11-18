# -*- coding: utf-8 -*-
# Parte 3: recapitulación, capítulos 6 (la última mañana), 7 (lo que quedó) y 8 (epílogo)
from lib import *

R('NAR', "Hasta aquí: durante dos días, los griegos han frenado en el desfiladero a las mejores tropas de Persia, Inmortales incluidos. Pero un hombre de la zona, Efialtes, ha guiado a los Inmortales por el sendero de la montaña. Los focenses que lo vigilaban se han apartado. Al amanecer del tercer día, los persas bajan por la espalda de Leónidas.",
  cd(dict(type='recap', title='Hasta aquí', items=[['Días 1 y 2', 'el muro de bronce resiste'], ['La noche', 'Efialtes guía a los Inmortales por Anopea'], ['El sendero', 'los focenses se retiran a la cumbre'], ['Día 3', 'los persas bajan por la espalda']]), at='Hasta aquí'))

# ---------------- CAPÍTULO 6 · LA ÚLTIMA MAÑANA ----------------
T('La última mañana', 'Capítulo 6', sting='tema', chapter=True)
B('noche')
N("En el campamento griego, todavía era de noche cuando empezaron a llegar las noticias. Primero, el adivino del ejército, Megistias, examinó las entrañas de los animales sacrificados, como se hacía antes de cada batalla. Y anunció que la muerte les llegaría con el amanecer.",
  ph('Greek seer extispicy vase hepatoscopy', src='met,cleveland,commons', at='el adivino del ejército', lt=['Megistias', 'Adivino del ejército griego', 'griegos']),
  ai('fire camp', at='con el amanecer'))
N("Después llegaron unos desertores del campo persa con la noticia del rodeo. Y al rayar el día, bajaron corriendo los vigías que habían apostado en las alturas. Ya no había duda. En pocas horas estarían rodeados.",
  ph('Greek runner vase', src='met,cleveland', at='bajaron corriendo los vigías'))
N("[serious] Los griegos se reunieron en consejo. Unos querían quedarse. Otros, la mayoría, irse mientras aún se pudiera. Y aquí está el gran misterio de las Termópilas. Al final, casi todo el ejército se retiró hacia el sur. Pero Leónidas y sus espartanos se quedaron.",
  ph('Greek warriors council vase', src='met,cleveland', at='se reunieron en consejo'),
  K('SE QUEDARON', 'Leonidas at Thermopylae David', at='se quedaron'))
N("¿Por qué? Heródoto ofrece dos versiones. Según la primera, los aliados se fueron por su cuenta, desmoralizados. Según la segunda, la que él prefiere, fue Leónidas quien los despidió, para salvarlos, porque para él y para los espartanos no era honroso abandonar el puesto que habían venido a defender.",
  cd(dict(type='split', left=dict(title='Versión 1', lines=['los aliados se marchan', 'por su cuenta']), right=dict(title='Versión 2 · la de Heródoto', lines=['Leónidas los despide', 'y se queda a cubrirlos']), strike=False), at='Heródoto ofrece dos versiones'))
R('HER', "«Si se quedaba, dejaría un gran nombre, y la prosperidad de Esparta no sería borrada.»",
  cd(dict(type='quote', text='Si se quedaba, dejaría un gran nombre, y la prosperidad de Esparta no sería borrada.', attrib='Heródoto, Historia VII, 220 · lectura', commons=IMG['herodoto']), at='Si se quedaba'))
N("[serious] Ahí está el oráculo: o la ciudad o el rey. Para Heródoto, Leónidas eligió morir para que Esparta viviera. Los historiadores de hoy añaden una razón más militar. Si todos se iban a la vez, por un camino estrecho y con la caballería persa detrás, el ejército entero podía ser masacrado en la retirada. Alguien tenía que quedarse a frenar al enemigo.",
  ph('Delphi Apollo temple', src='commons', at='Ahí está el oráculo'),
  ph('Greek hoplites retreating road vase', src='met,cleveland', at='Si todos se iban a la vez'))
N("[softly] Hay otra forma de verlo, que no excluye las anteriores. Para un espartano, retirarse sin orden era la mayor vergüenza posible. Toda su vida, desde los siete años, se había preparado para no hacerlo. Quizá la pregunta no sea por qué se quedaron, sino cómo habrían podido irse.",
  ph('Spartan hoplite statue', src='commons,met', at='Para un espartano'))
N("Leónidas incluso intentó salvar al adivino Megistias y lo mandó marcharse. Megistias se negó. Hizo irse a su único hijo, que también estaba en el ejército, y él se quedó.",
  ph('Greek father son farewell vase', src='met,cleveland', at='a su único hijo'))
N("[softly] No se quedaron solo los espartanos. Se quedaron también setecientos hombres de Tespias, una pequeña ciudad de Beocia, con su jefe Demófilo. Nadie les obligó. Heródoto dice que se negaron a abandonar a Leónidas. Su ciudad sería la siguiente en caer, y lo sabían.",
  ph('Thespiae Boeotia landscape', src='commons', at='setecientos hombres de Tespias', lt=['Demófilo', 'Jefe de los 700 tespios', 'griegos']),
  K('700 TESPIOS', 'Boeotian hoplite vase', at='Nadie les obligó'))
N("Se quedaron también cuatrocientos tebanos, pero estos, según Heródoto, contra su voluntad, como rehenes, porque Tebas era sospechosa de estar del lado persa. Muchos historiadores dudan de esta versión, escrita por un autor que no apreciaba a los tebanos. Y con todos ellos, los ilotas, quizá cientos, cuyo nombre nadie apuntó.",
  ph('Theban hoplite vase Boeotian', src='met,cleveland', at='cuatrocientos tebanos'),
  cd(dict(type='list', header='Los que se quedaron', items=[['Espartanos', 'los supervivientes de los 300'], ['Tespios', '700, por voluntad propia'], ['Tebanos', '400, según Heródoto como rehenes'], ['Ilotas', 'hasta 900, sin nombre']]), at='Y con todos ellos'))
N("[serious] Los tespios pagaron muy caro su gesto. Semanas después, el ejército persa llegó a su ciudad y la quemó. Sus habitantes habían huido al Peloponeso. Y al año siguiente, en Platea, los tespios supervivientes volvieron a luchar contra Persia, aunque ya sin armadura de hoplita: no les quedaba con qué comprarla.",
  ph('Thespiae Boeotia', src='commons', at='Los tespios pagaron', lt=['Tespias', 'Beocia']),
  ai('field', at='la quemó'))
N("Unos mil cuatrocientos hombres, quizá más con los ilotas. Ese es el número real de la última resistencia. Muchos más de trescientos. Y, aun así, nada frente a lo que venía.",
  cd(dict(type='counter', to=1400, label='griegos en la última resistencia (sin contar ilotas)'), at='Unos mil cuatrocientos'))
N("De esa mañana, autores muy posteriores cuentan que Leónidas dijo a sus hombres algo así:",
  ph('Greek hoplites meal vase', src='met,cleveland', at='esa mañana'))
R('LEO', "«Desayunad bien, que esta noche cenaremos en el Hades.»",
  cd(dict(type='quote', text='Desayunad bien, que esta noche cenaremos en el Hades.', attrib='Leónidas, según Diodoro y Plutarco · siglos I a. C. - II d. C.'), at='Desayunad'))
N("[serious] Puede que lo dijera, puede que no. Lo que hizo, en cambio, lo cuenta Heródoto. Jerjes esperó a media mañana para atacar, como le había dicho Efialtes, para dar tiempo a los Inmortales a bajar del monte. Y Leónidas, en lugar de esperar tras la muralla, salió.",
  ph('Achaemenid king relief', src='commons', at='Jerjes esperó a media mañana'),
  K('SALIÓ', 'hoplite charge black-figure amphora', at='salió'))
B('batalla')
N("En los días anteriores habían defendido la parte más estrecha. Ahora avanzaron hasta donde el paso se ensanchaba, para matar a cuantos más persas pudieran antes del final. Ya no buscaban sobrevivir.",
  ph('hoplites fighting Persians vase', src='met,cleveland', at='avanzaron'),
  ai('battle dust', at='Ya no buscaban sobrevivir'))
R('HER', "«Cayeron muchísimos bárbaros. Detrás de cada batallón, sus jefes los empujaban a latigazos hacia delante. Muchos cayeron al mar y se ahogaron. Muchos más murieron pisoteados unos por otros.»",
  ph('Persian soldiers relief', src='commons', at='Detrás de cada batallón'),
  cd(dict(type='quote', text='Los jefes los empujaban a latigazos hacia delante.', attrib='Heródoto, Historia VII, 223 · lectura', commons=IMG['herodoto']), at='a latigazos'))
N("[serious] La mayoría de los griegos tenían ya las lanzas rotas. Siguieron con las espadas. Y en esa lucha cayó Leónidas, el rey de Esparta, luchando en primera línea. Heródoto escribe que se informó de los nombres de los trescientos, porque fueron hombres dignos de memoria.",
  ph('broken spear hoplite fallen warrior vase', src='met,cleveland', at='las lanzas rotas'),
  ph('Leonidas at Thermopylae David', src='commons', at='cayó Leónidas', lt=['Leónidas', 'Rey de Esparta · muere en 480 a. C.', 'griegos'], tr='black'))
N("Del lado persa también cayeron nombres importantes: dos hermanos del propio Jerjes, Abrocomes e Hiperantes, hijos del rey Darío. La batalla había llegado al corazón de la familia real.",
  ph('Achaemenid prince relief Persepolis', src='commons', at='dos hermanos del propio Jerjes', lt=['Abrocomes e Hiperantes', 'Hermanos de Jerjes', 'persas']))
N("Entonces se libró la pelea más feroz de la batalla, alrededor del cuerpo de Leónidas. Los persas querían llevárselo. Los griegos no lo permitieron. Heródoto dice que lo rescataron a fuerza de valor y que hicieron retroceder al enemigo cuatro veces.",
  ph('battle over body of fallen warrior vase Patroclus', src='met,cleveland,commons', at='alrededor del cuerpo de Leónidas'),
  cd(dict(type='counter', to=4, label='veces que rechazaron al enemigo junto al cuerpo del rey'), at='cuatro veces'))
N("[pause] Y en ese momento llegaron los Inmortales, por detrás.",
  ai('immortals arrive', at='llegaron los Inmortales', tr='black'))
N("[serious] Los griegos que quedaban retrocedieron hasta la parte estrecha del paso, cruzaron la muralla y se juntaron todos en una pequeña colina. Todos menos los tebanos. Heródoto cuenta lo que pasó en aquella colina con una frase que no se olvida.",
  ph('Kolonos hill Thermopylae', src='commons', at='una pequeña colina', lt=['Colina del Kolonós', 'Termópilas']))
R('HER', "«Allí se defendieron con las espadas, los que todavía las tenían, y con las manos y con los dientes. Y los bárbaros los sepultaron bajo sus proyectiles.»",
  cd(dict(type='quote', text='Se defendieron con las espadas, y con las manos y con los dientes.', attrib='Heródoto, Historia VII, 225 · lectura', commons=IMG['herodoto']), at='Allí se defendieron'),
  ph('ancient arrowheads bronze', src='met,cleveland,commons', at='bajo sus proyectiles'))
N("[pause] Los persas no se acercaron a rematarlos. Los fueron matando desde lejos, con flechas, jabalinas y piedras, hasta que no quedó nadie en pie.",
  ai('hill silence', at='hasta que no quedó nadie'))
M('batalla', 14)
N("¿Y los tebanos? Según Heródoto, al ver el final se separaron de los demás y se acercaron a los persas con las manos extendidas, gritando que siempre habían estado de su lado. A algunos los mataron al llegar. Al resto, por orden de Jerjes, los marcaron con hierro con la señal del rey.",
  ph('Boeotian warriors vase', src='met,cleveland', at='¿Y los tebanos?'))
N("[serious] Después, Jerjes recorrió el campo de batalla entre los muertos. Y cuando le dijeron cuál era el cuerpo de Leónidas, hizo algo que, según el propio Heródoto, los persas no solían hacer, porque solían honrar a los enemigos valientes.",
  ai('field', at='recorrió el campo'))
R('HER', "«Ordenó que le cortaran la cabeza y la clavaran en un palo. Y para mí, esta es la prueba más clara de que el rey Jerjes había odiado a Leónidas, mientras vivía, más que a ningún otro hombre.»",
  cd(dict(type='quote', text='Ordenó que le cortaran la cabeza y la clavaran en un palo.', attrib='Heródoto, Historia VII, 238 · lectura', commons=IMG['herodoto']), at='Ordenó'))
N("Después, Jerjes mandó llamar a Demarato, el espartano que le había avisado de todo. Y por primera vez le dio la razón.",
  ph('Achaemenid nobles relief Persepolis', src='commons', at='mandó llamar a Demarato'))
R('JER', "«Demarato, eres un hombre de bien. Todo lo que dijiste ha ocurrido. Ahora dime: ¿cuántos lacedemonios quedan? ¿Y son todos tan buenos guerreros como estos?»",
  cd(dict(type='quote', text='Todo lo que dijiste ha ocurrido. ¿Cuántos lacedemonios quedan?', attrib='Jerjes a Demarato, según Heródoto, Historia VII, 234 · lectura', commons=IMG['jerjes']), at='Demarato, eres'))
R('DEM', "«Los lacedemonios son muchos, rey, y tienen muchas ciudades. En Esparta hay unos ocho mil hombres, y todos son iguales a los que han luchado aquí.»",
  cd(dict(type='quote', text='En Esparta hay unos ocho mil hombres, y todos son iguales a los que han luchado aquí.', attrib='Demarato a Jerjes, según Heródoto, Historia VII, 234'), at='En Esparta hay'))
N("[serious] Ocho mil como esos. Jerjes acababa de ganar una batalla. Pero había empezado a entender lo que le costaría ganar la guerra.",
  ph('Persian king relief Persepolis', src='commons', at='Ocho mil como esos'))
M('noche', 12)

# ---------------- CAPÍTULO 7 · LO QUE QUEDÓ ----------------
T('Lo que quedó en la colina', 'Capítulo 7', sting='tema', chapter=True)
B('tema')
N("La batalla había terminado. Pero Jerjes todavía tenía un problema: su flota. Los marineros llevaban días oyendo hablar del desfiladero y sabían que algo había ido mal. Así que el rey preparó un espectáculo.",
  ph('ancient trireme relief', src='commons,met', at='su flota'))
N("[serious] Según Heródoto, de sus propios muertos, unos veinte mil, dejó a la vista solo un millar. A los demás los enterró en zanjas cubiertas de hojas y tierra. Y después invitó a los marineros a cruzar y ver el campo de batalla. Pero no engañó a nadie. Daba risa, dice Heródoto: un millar de persas por un lado y los griegos amontonados por otro.",
  cd(dict(type='counter', to=20000, label='muertos persas según Heródoto'), at='unos veinte mil'),
  ai('trenches', at='los enterró en zanjas'))
N("Durante siglos, esa colina fue solo un nombre en un libro. Hasta que en mil novecientos treinta y nueve un arqueólogo griego, Spyridon Marinatos, excavó una pequeña elevación del paso, el Kolonós. Y encontró cientos de puntas de flecha.",
  ph('Kolonos hill Thermopylae Simonides', src='commons', at='esa colina'),
  ph('ancient arrowheads bronze', src='met,cleveland,commons', at='cientos de puntas de flecha', lt=['Puntas de flecha', 'como las halladas en el Kolonós']))
N("[serious] Muchas eran de tipo oriental, como las que usaban los arqueros persas. Estaban justo donde Heródoto decía que habían caído los últimos defensores: bajo una lluvia de proyectiles. Dos mil cuatrocientos años después, la arqueología confirmaba el relato.",
  cd(dict(type='split', left=dict(title='Heródoto', lines=['los últimos griegos mueren en una colina', 'bajo una lluvia de flechas']), right=dict(title='Marinatos · 1939', lines=['puntas de flecha persas', 'concentradas en el Kolonós']), strike=False), at='Muchas eran de tipo oriental'))
N("Cuando Heródoto visitó el paso, sobre aquella colina había un león de piedra en honor de Leónidas. Y había columnas con inscripciones. Una era para todos los que lucharon allí. Otra, solo para los espartanos. Las escribió, o al menos así se creía, el poeta Simónides.",
  ph('Thermopylae Leonidas monument lion', src='commons', at='un león de piedra'),
  ph('Simonides epigram stone Thermopylae', src='commons', at='columnas con inscripciones', lt=['Epitafio de Simónides', 'piedra moderna de 1955 · Termópilas']))
R('DOC', "«Aquí, contra tres millones, lucharon un día cuatro mil hombres del Peloponeso.»",
  cd(dict(type='quote', text='Aquí, contra tres millones, lucharon cuatro mil hombres del Peloponeso.', attrib='Inscripción de las Termópilas, según Heródoto, Historia VII, 228'), at='Aquí'))
N("[pause] Y la de los espartanos. Probablemente el epitafio más famoso de la historia. Dos versos. Ni una palabra de más.",
  K('EXTRANJERO', 'Simonides epigram stone Thermopylae', at='Probablemente el epitafio'))
R('DOC', "«Extranjero, ve a decir a los espartanos que aquí yacemos, obedientes a sus órdenes.»",
  cd(dict(type='quote', text='Extranjero, ve a decir a los espartanos que aquí yacemos, obedientes a sus órdenes.', attrib='Epitafio de los espartanos, según Heródoto, Historia VII, 228'), at='Extranjero'))
N("Heródoto apuntó también a los que más destacaron. Después de Dieneces, dos hermanos espartanos, Alfeo y Marón. Y entre los tespios, que tantas veces se olvidan, uno llamado Ditirambo. Nombres que no salen en ninguna película, y que solo conocemos gracias a él.",
  cd(dict(type='list', header='Los más valientes, según Heródoto', items=[['Dieneces', 'espartano · «lucharemos a la sombra»'], ['Alfeo y Marón', 'hermanos espartanos'], ['Ditirambo', 'de Tespias']]), at='los que más destacaron'))
N("[softly] Hubo también una tercera inscripción, para el adivino Megistias, el que supo que iba a morir y no quiso irse. Esa la pagó Simónides de su bolsillo, porque era su amigo.",
  ph('Greek funerary stele', src='met,cleveland', at='el adivino Megistias'))
N("[serious] ¿Sobrevivió alguien? Dos espartanos se habían quedado atrás antes del final, enfermos de los ojos. Uno, Éurito, al enterarse del rodeo, se puso la armadura, pidió a su ilota que lo llevara al frente y murió luchando. El otro, Aristodemo, volvió a Esparta.",
  ph('Greek hoplite arming vase', src='met,cleveland', at='se puso la armadura'))
N("En Esparta no hubo piedad para él. Nadie le daba fuego para encender su hogar, nadie le dirigía la palabra. Lo llamaban «el Tembloroso». Otro superviviente, Pantites, que había ido como mensajero a Tesalia, se ahorcó de vergüenza al volver.",
  ph('Sparta ruins acropolis', src='commons', at='En Esparta no hubo piedad'),
  K('EL TEMBLOROSO', 'Spartan hoplite figurine', at='el Tembloroso'))
N("Aristodemo tendría su revancha un año más tarde, en la batalla de Platea. Luchó como un loco, buscando la muerte, y la encontró. Heródoto dice que fue el más valiente de aquel día. Pero los espartanos no le concedieron los honores, porque había luchado para morir, no para vencer.",
  ph('Plataea battlefield', src='commons', at='la batalla de Platea', lt=['Platea', '479 a. C.']))
M('tema', 12)

# ---------------- CAPÍTULO 8 · EPÍLOGO ----------------
T('La derrota que ganó la guerra', 'Capítulo 8', sting='tema', chapter=True)
B('tema')
N("[serious] Las Termópilas fueron una derrota. Tras el paso, el ejército persa bajó por Grecia central, quemó ciudades y llegó a Atenas. Los atenienses habían evacuado la ciudad. Los persas incendiaron la Acrópolis.",
  cd(dict(type='mapfly', title='Tras las Termópilas', keys=[[21.5, 37.4, 24.5, 39.2], [22.6, 37.6, 24.2, 38.6]], points=[dict(name='Termópilas', lon=22.56, lat=38.8, at=0.15), dict(name='Atenas', lon=23.73, lat=37.98, at=0.5, pulse=1, big=1), dict(name='Salamina', lon=23.5, lat=37.95, at=0.75, pulse=1)]), at='Tras el paso'),
  ph('Acropolis Athens Persian destruction Kritios', src='commons', at='incendiaron la Acrópolis'))
N("Pero el tiempo que compraron en el desfiladero sirvió. Pocas semanas después, la flota griega, guiada por Temístocles, destrozó a la persa en el estrecho de Salamina. Jerjes volvió a Asia. Y un año más tarde, en Platea, el ejército que había dejado en Grecia fue derrotado por una coalición griega con los espartanos al frente.",
  ph('Salamis strait Greece', src='commons', at='el estrecho de Salamina', lt=['Estrecho de Salamina', 'hoy']),
  ph('Battle of Salamis painting Kaulbach', src='commons', at='destrozó a la persa'),
  cd(dict(type='timeline', header='La guerra tras las Termópilas', events=[['480', 'Termópilas y Artemisio'], ['480', 'Atenas incendiada · Salamina'], ['479', 'Platea y Mícala'], ['440', 'Los restos de Leónidas vuelven a Esparta']]), at='Y un año más tarde'))
N("[serious] En Platea, según Heródoto, alguien propuso al general espartano Pausanias hacer con el cadáver del general persa lo mismo que Jerjes había hecho con Leónidas. Pausanias se negó: eso era cosa de bárbaros, dijo. Leónidas, añadió, ya estaba suficientemente vengado.",
  ph('Spartan general hoplite bronze statuette', src='met,cleveland,commons', at='Pausanias', lt=['Pausanias', 'Regente de Esparta · sobrino de Leónidas', 'griegos']))
N("Cuarenta años después de la batalla, los restos de Leónidas fueron llevados a Esparta. Allí, junto a su tumba, se levantó una columna con los nombres de los trescientos. Heródoto pudo verla. Es muy probable que de ahí sacara la lista de nombres que dice haber averiguado.",
  ph('Leonidaion Sparta ruins', src='commons', at='llevados a Esparta'),
  K('LOS 300 NOMBRES', 'Greek inscription stone stele names', at='los nombres de los trescientos'))
N("[serious] Y el paso siguió siendo lo que era: una puerta con una trampa. Doscientos años después, en el doscientos setenta y nueve antes de Cristo, los griegos volvieron a cerrarlo contra un ejército de gálatas que bajaba hacia Delfos. Los gálatas encontraron un camino por la montaña y rodearon a los defensores, que tuvieron que huir por mar.",
  cd(dict(type='timeline', header='Las otras batallas de las Termópilas', events=[['480 a. C.', 'Leónidas contra Jerjes'], ['279 a. C.', 'griegos contra gálatas'], ['191 a. C.', 'Roma contra Antíoco III'], ['1941', 'retaguardia aliada frente a Alemania']]), at='Doscientos años después'),
  ph('Galatians Gauls ancient sculpture Dying Gaul', src='commons', at='un ejército de gálatas'))
N("En el ciento noventa y uno, fue un ejército romano el que se encontró el paso cerrado, esta vez por el rey Antíoco Tercero. Y un oficial romano, Catón, condujo a sus hombres de noche por las alturas del Calídromo y apareció sobre el enemigo. Otra vez el mismo truco, en el mismo sitio.",
  ph('Cato the Elder bust', src='commons', at='Catón', lt=['Marco Porcio Catón', 'Oficial romano · 191 a. C.']),
  ph('Kallidromo mountain Thermopylae', src='commons', at='las alturas del Calídromo'))
N("Y en abril de mil novecientos cuarenta y uno, durante la invasión alemana de Grecia, soldados neozelandeses y australianos defendieron las Termópilas para cubrir la retirada del resto del ejército aliado. Veinticuatro siglos después, la misma misión que Leónidas: aguantar para que otros pudieran irse.",
  ph('1941 Greece New Zealand soldiers', src='commons', at='mil novecientos cuarenta y uno', lt=['Termópilas', 'abril de 1941'], old=True))
N("[softly] Desde entonces, las Termópilas nunca han dejado de contarse. Las contaron los romanos, los pintores del siglo diecinueve, los soldados de las dos guerras mundiales, el cine. Cada época ha encontrado allí lo que buscaba: libertad, sacrificio, patria, o simplemente un buen espectáculo.",
  ph('Leonidas at Thermopylae Jacques-Louis David', src='commons', at='los pintores del siglo diecinueve'),
  ph('Thermopylae Leonidas monument statue', src='commons', at='Cada época'))
N("[serious] Por eso conviene volver a lo que sabemos. No eran trescientos, eran miles. Los persas no eran millones, pero sí muchísimos. Algunas de las frases más famosas las escribió alguien siglos después. Y la batalla no salvó a Grecia por sí sola: la salvaron Salamina y Platea.",
  cd(dict(type='list', header='Lo que sabemos', items=[['No eran 300', 'unos 7.000; al final, unos 1.400 más ilotas'], ['No eran millones', 'entre 120.000 y 300.000 persas'], ['Las frases', '«Venid a cogerlas» es de Plutarco, siglos después'], ['La victoria', 'llegó en Salamina y Platea']]), at='Por eso conviene'))
N("Lo que sí hicieron las Termópilas fue otra cosa, quizá más importante. Demostraron que el ejército del Gran Rey podía ser detenido. Que unas ciudades que se odiaban entre sí podían luchar juntas. Durante tres días, espartanos, tespios, corintios, arcadios y focenses pelearon bajo un mismo mando. Eso, en la Grecia de entonces, era casi tan raro como la propia resistencia.",
  ph('Greek hoplites many vase', src='met,cleveland', at='Que unas ciudades que se odiaban'))
N("Pero hay algo que ni la arqueología ni la crítica moderna han podido desmontar. Una mañana de verano del cuatrocientos ochenta, unos cientos de hombres supieron que iban a morir, pudieron irse y no se fueron.",
  ph('Thermopylae pass dawn', src='commons', at='Una mañana de verano'))
N("Heródoto escribió su obra para que, en sus propias palabras, el tiempo no borrara las grandes hazañas de los griegos y de los bárbaros. De los dos. No es casualidad que el mismo libro que hace inmortal a Leónidas nos muestre a un Jerjes que llora por sus soldados. Para Heródoto, la historia no era de buenos y malos. Era de hombres.",
  D('El propósito de Heródoto', 'herodoto_ms', text='Para que el tiempo no borre lo que hicieron los hombres, ni queden sin gloria las grandes obras de griegos y de bárbaros.', source='Heródoto, Historia I, proemio', at='para que, en sus propias palabras'))
N("[softly] Un hombre de Halicarnaso, cuarenta años después, se tomó la molestia de averiguar sus nombres, uno por uno. Y nos dejó, entre tantos, el de uno que dijo que lucharía a la sombra.",
  ph('Herodotus bust', src='commons,met', at='Un hombre de Halicarnaso'))
N("[pause] Extranjero, ve a decir a los espartanos que aquí yacemos, obedientes a sus órdenes.",
  ph('Simonides epigram stone Thermopylae', src='commons', at='Extranjero', tr='black'))
M('tema', 22, end=True)
