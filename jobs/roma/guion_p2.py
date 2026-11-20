# -*- coding: utf-8 -*-
# «La Antigua Roma (Historia Completa)» · parte 2: capítulos IV a VI
from lib import *

# ---------------- IV · LA REPÚBLICA SE DEVORA ----------------
T('La República se devora', '133 – 44 a. C.', num='IV', sting='tema')
B('tension')
NAR("Roma ya no tenía rivales fuera. El problema, ahora, estaba dentro. Las conquistas habían traído a Italia oro, esclavos por cientos de miles y enormes fincas en manos de unos pocos. Y los campesinos soldados que habían ganado esas guerras volvían a casa para descubrir que lo habían perdido todo.",
    ai('latifundio_esclavos', 'a vast Roman estate with long lines of chained slaves working olive groves under a harsh sun, an overseer on horseback, wide shot', at='esclavos por cientos de miles'),
    ai('veterano_ruina', 'a weary Roman veteran soldier with his shield on his back standing before his abandoned, overgrown farmhouse, evening, seen from behind', at='lo habían perdido todo'))
NAR("Un joven tribuno de la plebe, Tiberio Graco, propone repartir las tierras públicas entre los pobres. Su discurso, tal como lo recoge Plutarco, sigue poniendo los pelos de punta.",
    ph('Gracchi brothers statue Guillaume', at='Tiberio Graco', lt=['Tiberio Graco', 'Tribuno de la plebe · 133 a. C.', 'roma']))
V('GRA', "[serious] Las fieras que habitan Italia tienen cada una su guarida, su madriguera. Pero los que luchan y mueren por Italia solo tienen el aire y la luz. Les llaman señores del mundo... y no tienen ni un terrón de tierra propio.",
    PAP('Las fieras que habitan Italia tienen cada una su guarida. Pero los que luchan y mueren por Italia solo tienen el aire y la luz. Les llaman señores del mundo, y no tienen ni un terrón de tierra propio.',
        'Tiberio Graco, según Plutarco', 'Vida de Tiberio Graco, 9', at='Las fieras'))
V('GRA', "[serious] Vagan sin casa ni hogar con sus mujeres y sus hijos. Y los generales mienten cuando les piden que luchen por las tumbas y los altares de sus antepasados, porque ninguno de esos romanos tiene ya ni altar familiar ni tumba de sus padres. Luchan y mueren para que otros vivan en el lujo.",
    ai('graco_discurso', 'a young Roman orator in a toga speaking passionately from a high platform to a vast crowd of poor citizens in the Forum, seen from behind the crowd, dramatic sky', at='Vagan sin casa'))
ESP("[serious] Los senadores no lo soportaron. Un grupo de ellos, armados con patas de bancos y garrotes, mató a Tiberio y a cientos de sus seguidores. Arrojaron los cuerpos al Tíber. Diez años después, su hermano Cayo intentó lo mismo y corrió la misma suerte. Era la primera vez en casi cuatro siglos que la sangre política corría por las calles de Roma. No sería la última.",
    ai('graco_muerte', 'a mob of men in togas wielding broken wooden benches and clubs on the steps of a temple on a hill, chaos, a fallen figure, no gore, dusk', at='patas de bancos'),
    ph('Death of Gaius Gracchus painting', at='su hermano Cayo'))
NAR("A partir de aquí, la República entra en un siglo de generales cada vez más poderosos. Mario, que abre el ejército a los pobres: ahora los soldados son profesionales... y son leales a su general, no a Roma. Y Sila, que marcha con sus legiones contra su propia ciudad y publica listas de enemigos para asesinar. Las proscripciones.",
    ph('Gaius Marius bust Munich', at='Mario', lt=['Cayo Mario', 'Siete veces cónsul · 157 – 86 a. C.', 'roma']),
    ph('Sulla bust Munich Glyptothek', at='Sila', lt=['Lucio Cornelio Sila', 'Dictador · 138 – 78 a. C.', 'roma']),
    ai('proscripciones', 'a crowd gathering at night around a list of names nailed to a wall in the Forum, torchlight, fear', at='publica listas'))
ESP("Y desde abajo, el terremoto. Año setenta y tres antes de Cristo. Un gladiador tracio, Espartaco, escapa de una escuela de Capua con unos setenta compañeros, armados con cuchillos de cocina. En pocos meses tiene un ejército de decenas de miles de esclavos. Derrota a varios ejércitos romanos. Recorre Italia de punta a punta.",
    ph('Spartacus statue Louvre Foyatier', at='Espartaco', lt=['Espartaco', 'Gladiador tracio · murió en 71 a. C.', 'barbaros']),
    ai('espartaco_fuga', 'gladiators breaking out of a training school at night with kitchen knives and cleavers, a burning gate, running figures, dramatic', at='cuchillos de cocina'),
    ai('ejercito_esclavos', 'a huge ragged army of escaped slaves marching through the Italian countryside with improvised weapons, mountains of Vesuvius behind', at='decenas de miles'))
NAR("Le aplasta finalmente Marco Licinio Craso, el hombre más rico de Roma, en el año setenta y uno. El castigo es una advertencia para todos los esclavos del mundo romano: seis mil prisioneros crucificados a lo largo de la Vía Apia, entre Capua y Roma.",
    ph('Crassus bust Louvre', at='Craso', lt=['Marco Licinio Craso', 'El hombre más rico de Roma', 'roma']),
    cd(dict(type='counter', to=6000, label='crucificados a lo largo de la Vía Apia'), at='seis mil'),
    ai('via_apia_cruces', 'a long straight Roman road disappearing to the horizon lined with crosses in silhouette against a red sunset, no bodies visible in detail, haunting', at='a lo largo de la Vía Apia'))
NAR("En el Senado, mientras tanto, la batalla es de palabras. Y el gran maestro de las palabras es Marco Tulio Cicerón, abogado, cónsul y el mejor orador de Roma. En el año sesenta y tres descubre una conspiración para hacerse con el poder, la de Catilina. Y le ataca a la cara, con el conspirador sentado delante.",
    ph('Cicero bust Capitoline Museums', at='Marco Tulio Cicerón', lt=['Marco Tulio Cicerón', 'Orador y cónsul · 106 – 43 a. C.', 'roma']),
    ph('Cicero denounces Catiline Maccari', at='le ataca a la cara'))
V('CIC', "[dramatically] ¿Hasta cuándo, Catilina, abusarás de nuestra paciencia? [short pause] ¡Oh, tiempos! ¡Oh, costumbres!",
    PAP('¿Hasta cuándo, Catilina, abusarás de nuestra paciencia? ¡Oh tiempos, oh costumbres!', 'Cicerón', 'Primera Catilinaria, 63 a. C.', at='Hasta cuándo'))
NAR("Pero el futuro no era de los oradores. Era de tres hombres que se repartieron Roma en secreto: Craso, el dinero. Pompeyo, el general más famoso de su tiempo. Y un político joven, endeudado hasta las cejas y con un talento inmenso: Cayo Julio César.",
    cd(dict(type='list', header='El primer triunvirato · 60 a. C.', items=['Craso · el dinero', 'Pompeyo · el prestigio militar', 'César · la ambición']), at='tres hombres'),
    ph('Pompey the Great bust Copenhagen', at='Pompeyo', lt=['Cneo Pompeyo Magno', 'General · 106 – 48 a. C.', 'roma']),
    ph('Julius Caesar Tusculum bust', at='Cayo Julio César', lt=['Cayo Julio César', 'General y dictador · 100 – 44 a. C.', 'roma']))
NAR("[softly] Para entender a César, basta una anécdota de juventud que cuenta Plutarco. Unos piratas le secuestran y piden veinte talentos de rescate. César se ríe: les dice que vale por lo menos cincuenta. Durante semanas les recita sus poemas, les llama ignorantes si no aplauden y les promete, entre risas, que los crucificará a todos.",
    ai('cesar_piratas', 'a young Roman aristocrat lounging confidently on the deck of a pirate ship, reading aloud from a scroll to a group of rough pirates, Mediterranean sun, his face turned away', at='Unos piratas'),
    ai('cesar_piratas2', 'rough pirates laughing around a campfire on a rocky island while a young Roman in a fine toga stands with arms crossed, night', at='les promete'))
ESP("Le pagan el rescate. César reúne unos barcos, los persigue, los captura... y cumple su promesa. Ese era Julio César.",
    ai('piratas_captura', 'Roman warships surrounding a pirate vessel at dawn, armed men boarding, calm sea', at='los captura'))
ESP("Entre el año cincuenta y ocho y el cincuenta antes de Cristo conquista la Galia, la actual Francia. Ocho años de campaña. En Alesia, encierra al gran jefe galo, Vercingétorix, con un doble muro de asedio: uno para que no salgan los sitiados y otro para que no entren los que vienen a rescatarlos. Gana.",
    cd(dict(type='imperio', title='La conquista de la Galia', bbox=[-6, 41, 12, 52], stages=[dict(year='58 a. C.', label='La Provenza, ya romana', zona=[{'c': 'FRA', 'box': [2.0, 42.3, 7.7, 45.0]}, 'ITA']),
        dict(year='50 a. C.', label='Toda la Galia', zona=['FRA', 'BEL', 'LUX', 'CHE', 'ITA', {'c': 'NLD', 'box': [3, 50.7, 7.2, 52]}, {'c': 'DEU', 'box': [6, 49, 8.2, 51]}])],
        puntos=[]), at='conquista la Galia'),
    ai('alesia_muros', 'aerial view of a hilltop Celtic fortress encircled by two concentric Roman siege walls with towers and trenches, armies, autumn', at='un doble muro'),
    ph('Vercingetorix throws down his arms Lionel Royer', at='Vercingétorix', lt=['Vercingétorix', 'Jefe de los galos arvernos', 'barbaros']))
V('CES', "Toda la Galia está dividida en tres partes. Una la habitan los belgas; otra, los aquitanos; y la tercera, los que en su lengua se llaman celtas y en la nuestra, galos. Los más valientes de todos son los belgas, porque viven más lejos de la civilización y el refinamiento de nuestra provincia.",
    PAP('Toda la Galia está dividida en tres partes. Una la habitan los belgas; otra, los aquitanos; y la tercera, los que en su lengua se llaman celtas y en la nuestra, galos.', 'Julio César', 'La guerra de las Galias, I, 1', at='Toda la Galia'))
NAR("El precio de la conquista fue brutal. Según los propios autores antiguos, murió alrededor de un millón de galos y otro millón fue esclavizado. César lo contó todo en su propio libro, en tercera persona: la primera gran campaña de propaganda de la historia.",
    ph('Commentarii de Bello Gallico manuscript', at='su propio libro'))
NAR("Craso había muerto en Oriente, contra los partos. Pompeyo, celoso, se pone del lado del Senado, que ordena a César licenciar su ejército. Si obedece, le juzgarán. Si no, es la guerra civil. En enero del año cuarenta y nueve, César llega al río Rubicón, la frontera de Italia.",
    ph('Rubicon river', at='río Rubicón', lt=['El Rubicón', 'Frontera de Italia en 49 a. C.']),
    ai('rubicon', 'a Roman general on horseback at night pausing at the edge of a small river, legion torches behind him, his face hidden by shadow', at='llega al río'))
V('CES', "[serious] La suerte está echada.",
    PAP('Alea iacta est. La suerte está echada.', 'Julio César, según Suetonio', 'Vida de los doce césares, César, 32', at='La suerte'))
ESP("Cruza. Pompeyo huye a Grecia. César le derrota en Farsalia. Pompeyo escapa a Egipto, donde le cortan la cabeza para regalársela a César. Y en Egipto, César conoce a la joven reina Cleopatra.",
    ph('Pharsalus battle', at='Farsalia'),
    ph('Cleopatra Berlin bust Altes Museum', at='Cleopatra', lt=['Cleopatra VII', 'Reina de Egipto · 69 – 30 a. C.', 'oriente']))
ESP("La reina estaba en guerra con su propio hermano y no podía entrar en el palacio de Alejandría. Según Plutarco, llegó de noche en una barca, se escondió dentro de un fardo de ropa de cama y se hizo llevar así, a hombros de un criado, hasta los aposentos de César. Él tenía cincuenta y dos años. Ella, veintiuno.",
    ai('cleopatra_fardo', 'a servant carrying a large rolled bedding bundle on his shoulder through a torch-lit marble corridor of an Egyptian palace at night, guards looking away, intrigue', at='un fardo de ropa'))
NAR("Después vence en Asia Menor, en Zela, en una campaña relámpago de cinco días. Y la resume en el parte de guerra más corto de la historia.",
    cd(dict(type='counter', to=5, label='días de campaña · Zela, 47 a. C.'), at='cinco días'))
V('CES', "Llegué. Vi. Vencí.",
    PAP('Veni, vidi, vici. Llegué, vi, vencí.', 'Julio César, según Suetonio', 'Vida de los doce césares, César, 37', at='Llegué'))
NAR("César vuelve a Roma como dueño absoluto. Reforma el calendario: el que usamos hoy, con sus años bisiestos, es casi el suyo. Perdona a muchos enemigos. Y se hace nombrar dictador... perpetuo. Para muchos senadores, eso era un rey con otro nombre.",
    ph('Fasti calendar Roman marble', at='Reforma el calendario'),
    ph('Julius Caesar denarius dictator perpetuo', at='dictador... perpetuo'),
    K('REX', 'Roman Senate Curia Julia interior', at='un rey con otro nombre'))
FUE("[softly] Le afeaba mucho la calvicie, que a menudo le valía las burlas de sus enemigos. Por eso solía peinarse hacia delante el escaso pelo de la coronilla. Y de todos los honores que le concedieron el Senado y el pueblo, ninguno aceptó con más gusto que el derecho a llevar siempre la corona de laurel.",
    ph('Julius Caesar Chiaramonti bust', at='la calvicie'),
    PAP('De todos los honores, ninguno aceptó con más gusto que el derecho a llevar siempre la corona de laurel.', 'Suetonio', 'Vida de los doce césares, César, 45', at='la corona de laurel'))
NAR("[softly] Sí: la famosa corona de laurel también servía para tapar la calva.",
    ph('Julius Caesar laurel wreath coin', at='tapar la calva'))
V('CES', "Que esta sea la nueva manera de vencer: hacernos fuertes con la clemencia y la generosidad.",
    PAP('Que esta sea la nueva manera de vencer: hacernos fuertes con la clemencia y la generosidad.', 'Julio César', 'Carta a Opio y Balbo, 49 a. C., conservada por Cicerón', at='la nueva manera'))
ESP("[serious] Quince de marzo del año cuarenta y cuatro antes de Cristo. Los idus de marzo. Un grupo de unos sesenta senadores, entre ellos Bruto, al que César había perdonado y protegido, le rodea en una sala junto al teatro de Pompeyo. Veintitrés puñaladas.",
    ph('Death of Caesar Gerome', at='Los idus de marzo'),
    ai('idus_marzo', 'a group of men in togas surrounding a figure in a dim columned hall, daggers raised, dramatic chiaroscuro, faces hidden', at='le rodea'),
    cd(dict(type='counter', to=23, label='puñaladas · según Suetonio, solo una fue mortal'), at='Veintitrés puñaladas'))
NAR("¿Y sus últimas palabras? «Tú también, Bruto», ese «Et tu, Brute», es de Shakespeare. Suetonio dice que César murió sin decir nada. Aunque añade que algunos contaban que, al ver a Bruto, le dijo en griego: «¿Tú también, hijo?».",
    MITO('Las últimas palabras de César fueron «Et tu, Brute».', 'La frase en latín es de Shakespeare, de 1599. Suetonio dice que murió sin decir palabra, aunque recoge que algunos le atribuían, en griego: «¿Tú también, hijo?».',
         fuente='Suetonio, César, 82', at='sus últimas palabras'))
NAR("[pause] Los asesinos gritaron que habían salvado la libertad. En realidad acababan de matar a la República.",
    ph('Largo di Torre Argentina Curia of Pompey', at='salvado la libertad', lt=['Largo di Torre Argentina', 'Lugar del asesinato · Roma, hoy']))
NAR("Cicerón no participó en el asesinato. Pero lo celebró. Y meses después, cuando Marco Antonio, el lugarteniente de César, se hizo con el poder, escribió a uno de los conjurados una frase terrible.",
    ph('Cicero bust Capitoline Museums', at='Cicerón no participó'))
V('CIC', "[serious] ¡Cómo me habría gustado que me invitarais a aquel espléndido banquete de los idus de marzo! No habría quedado ninguna sobra.",
    PAP('¡Cómo me habría gustado que me invitarais a aquel espléndido banquete de los idus de marzo! No habría quedado ninguna sobra.', 'Cicerón', 'Carta a Trebonio, 43 a. C.', at='Cómo me habría'))
NAR("La sobra era Marco Antonio. Y esa frase le costaría la vida.",
    ph('Mark Antony bust Vatican', at='La sobra'))

M('tension', 6)
NAR("Recapitulemos. Roma ha pasado de aldea a dueña del Mediterráneo. Ha derrotado a Cartago. Pero sus generales se han hecho más fuertes que sus leyes. Y el hombre que lo había conquistado todo yace muerto a los pies de la estatua de su rival.",
    cd(dict(type='recap', title='Hasta aquí', items=[['753 a. C.', 'Nace Roma: aldeas en el Palatino'], ['509 a. C.', 'Fuera los reyes: la República'], ['146 a. C.', 'Cartago y Corinto, destruidas'], ['44 a. C.', 'Asesinato de Julio César']]), at='Recapitulemos'))

# ---------------- V · AUGUSTO ----------------
T('El hombre que no quiso ser rey', '44 a. C. – 14 d. C.', num='V', sting='tema')
B('tema')
NAR("César había dejado un testamento. Y su heredero era un desconocido: su sobrino nieto, Cayo Octavio, un chico enfermizo de dieciocho años. Nadie daba nada por él. Fue el peor error de cálculo de la historia de Roma.",
    ph('Augustus young bust Ara Pacis', at='Cayo Octavio', lt=['Octavio, después Augusto', 'Heredero de César · 63 a. C. – 14 d. C.', 'roma']))
V('AUG', "A los diecinueve años, por decisión propia y con mi propio dinero, reuní un ejército con el que devolví la libertad a la República, oprimida por el dominio de una facción.",
    PAP('A los diecinueve años, por decisión propia y con mi propio dinero, reuní un ejército con el que devolví la libertad a la República.', 'Augusto', 'Res Gestae, 1', at='A los diecinueve'))
NAR("[softly] Un ejército privado. Ilegal. Pero así lo contaba él.",
    ai('ejercito_privado', 'a very young man in a fine cloak inspecting a line of veteran soldiers in a camp, coins being handed out, his face turned away, dawn', at='Un ejército privado'))
NAR("Primero se alía con Marco Antonio, el lugarteniente de César, para vengarle. Persiguen a los asesinos y publican nuevas listas de proscritos. En una de ellas aparece Cicerón. Le cortan la cabeza y las manos, las manos con las que había escrito contra Antonio, y las clavan en la tribuna del Foro.",
    ph('Mark Antony bust Vatican', at='Marco Antonio', lt=['Marco Antonio', 'Lugarteniente de César · 83 – 30 a. C.', 'roma']),
    ai('rostra_cicero', 'the speaker platform of the Roman Forum decorated with ship prows, a silent crowd looking up at it, grey morning, ominous, nothing explicit shown', at='la tribuna del Foro'))
MUR("En medio de aquel terror, ocurrió algo insólito. Los triunviros quisieron cobrar un impuesto especial a las mil cuatrocientas mujeres más ricas de Roma. Y una de ellas, Hortensia, hija de un gran orador, se plantó en el Foro y les habló a la cara.",
    ai('hortensia_foro', 'a dignified Roman woman in a dark stola addressing three powerful men seated on a high tribunal in the Forum, a group of women behind her, seen from behind, defiant', at='Hortensia'))
MUR("[serious] ¿Por qué tenemos que pagar impuestos, si no tenemos parte en las magistraturas, ni en los honores, ni en el mando, ni en el gobierno del Estado, por el que vosotros os peleáis hasta causarnos tanto mal?",
    PAP('¿Por qué tenemos que pagar impuestos, si no tenemos parte en las magistraturas, ni en los honores, ni en el mando, ni en el gobierno del Estado?', 'Hortensia, según Apiano', 'Guerras civiles, IV, 33 · 42 a. C.', at='Por qué tenemos'))
MUR("Y ganó. Los triunviros redujeron la lista a cuatrocientas mujeres.",
    cd(dict(type='counter', **{'from': 1400}, to=400, label='mujeres obligadas a pagar, tras el discurso de Hortensia'), at='Y ganó'))
ESP("Después, los dos vencedores se enfrentan entre sí. Antonio se instala en Egipto con Cleopatra. Octavio le presenta en Roma como un traidor seducido por una reina extranjera. Año treinta y uno antes de Cristo: batalla naval de Actium. Cleopatra huye con su flota. Antonio la sigue. Un año después, los dos se suicidan en Alejandría.",
    ai('actium', 'a great naval battle at sea between hundreds of ancient warships, burning ships, smoke, a fleet with purple sails fleeing in the distance', at='batalla naval de Actium'),
    ph('Death of Cleopatra painting', at='los dos se suicidan'))
ESP("Octavio, con treinta y tres años, es el amo del mundo romano. Y aquí viene su golpe de genio: no se proclama rey. Al contrario. En el año veintisiete antes de Cristo, devuelve teatralmente el poder al Senado... que le suplica que se quede. Le dan un nombre nuevo: Augusto, «el venerable».",
    ph('Augustus of Prima Porta', at='es el amo', lt=['Augusto', 'Primer emperador de Roma · 27 a. C. – 14 d. C.', 'roma']),
    K('AUGUSTO', 'Augustus of Prima Porta detail', at='Augusto'))
NAR("Él se llamaba a sí mismo «el primer ciudadano». Mantuvo el Senado, los cónsules, las elecciones. Todo seguía en pie. Solo que todo pasaba por él. En la lista de sus logros que mandó grabar en bronce, lo resumió así.",
    ph('Res Gestae Divi Augusti Ankara', at='grabar en bronce', lt=['Res Gestae', 'Templo de Augusto, Ankara · hoy']))
V('AUG', "Después de haber extinguido las guerras civiles, cuando por consenso universal tenía el control de todo, transferí la república de mi poder al arbitrio del Senado y del pueblo romano.",
    PAP('Después de haber extinguido las guerras civiles, cuando por consenso universal tenía el control de todo, transferí la república de mi poder al arbitrio del Senado y del pueblo romano.',
        'Augusto', 'Res Gestae, 34', at='Después de haber'))
NAR("[softly] Traducido: «yo no mando». Gobernó cuarenta y un años.",
    MITO('Augusto devolvió la República al Senado.', 'Conservó las formas, pero tenía el ejército, el dinero y la última palabra. Fue el primer emperador, aunque nunca usó la palabra «rey».', at='yo no mando'))
NAR("Y con él llega algo que el Mediterráneo no había conocido nunca: la Pax Romana. Unos doscientos años de relativa paz interior. Augusto llena Roma de templos y foros. Y presumía de ello.",
    ph('Ara Pacis Augustae', at='la Pax Romana', lt=['Ara Pacis', 'Altar de la Paz de Augusto · Roma']),
    ph('Forum of Augustus Rome', at='templos y foros'))
V('AUG', "Encontré una Roma de ladrillo y la dejo de mármol.",
    PAP('Encontré una Roma de ladrillo y la dejo de mármol.', 'Augusto, según Suetonio', 'Vida de los doce césares, Augusto, 28', at='Encontré'))
NAR("Y encargó a los poetas la gran epopeya del nuevo orden. Virgilio escribió la Eneida, y en ella dejó grabada la misión que Roma creía tener en el mundo.",
    ph('Virgil mosaic Bardo Museum', at='Virgilio', lt=['Virgilio', 'Poeta · autor de la Eneida', 'roma']))
FUE("Tú, romano, recuerda gobernar a los pueblos con tu mando. Estas serán tus artes: imponer las costumbres de la paz, perdonar a los vencidos y abatir a los soberbios.",
    PAP('Tú, romano, recuerda gobernar a los pueblos con tu mando: imponer las costumbres de la paz, perdonar a los vencidos y abatir a los soberbios.', 'Virgilio', 'Eneida, VI, 851-853', at='Tú, romano'))
NAR("Aunque no todo salió bien. En el año nueve después de Cristo, tres legiones enteras caen en una emboscada en el bosque de Teutoburgo, en Germania. Suetonio cuenta que Augusto, durante meses, se golpeaba la cabeza contra las puertas gritando: «¡Quintilio Varo, devuélveme mis legiones!».",
    ai('teutoburgo', 'Roman legionaries trapped on a muddy forest path in heavy rain, Germanic warriors emerging from dense trees, chaos, dark green palette', at='Teutoburgo'),
    ph('Kalkriese Roman mask', at='en Germania', lt=['Kalkriese', 'Lugar probable de la batalla · Alemania']))
NAR("Murió en el año catorce, a los setenta y cinco. Y según Suetonio, sus últimas palabras a los amigos que le rodeaban fueron las de un actor al acabar la función.",
    ph('Augustus Via Labicana', at='Murió en el año catorce'))
V('AUG', "[softly] Si os ha gustado la comedia... aplaudid.",
    PAP('Si la comedia os ha gustado, aplaudid.', 'Augusto, según Suetonio', 'Vida de los doce césares, Augusto, 99', at='aplaudid'))

# ---------------- VI · LOCOS, DIOSES Y CONSTRUCTORES ----------------
T('Locos, dioses y constructores', '14 – 117 d. C.', num='VI', sting='tema')
B('tension')
NAR("El sistema de Augusto tenía un problema: no había ninguna regla para elegir al siguiente. Y los que vinieron después son los emperadores que conoces por las películas. Ahora toca separar la leyenda de los hechos.",
    cd(dict(type='list', header='Los primeros emperadores', items=['Tiberio · 14 – 37', 'Calígula · 37 – 41', 'Claudio · 41 – 54', 'Nerón · 54 – 68', 'Vespasiano · 69 – 79', 'Tito · 79 – 81', 'Domiciano · 81 – 96']), at='los que vinieron después'))
NAR("Calígula, el tercer emperador, gobernó menos de cuatro años, entre crueldades y excentricidades. ¿Nombró cónsul a su caballo, Incitato? No. Lo que dice Suetonio es que el caballo tenía un establo de mármol, collares de piedras preciosas... y que, según se decía, Calígula pensaba nombrarlo cónsul.",
    ph('Caligula bust Ny Carlsberg', at='Calígula', lt=['Calígula', 'Emperador · 37 – 41 d. C.', 'roma']),
    MITO('Calígula nombró cónsul a su caballo.', 'Suetonio solo dice que, según se contaba, pensaba hacerlo. El caballo, Incitato, sí tenía establo de mármol y pesebre de marfil.',
         fuente='Suetonio, Calígula, 55', at='Nombró cónsul'),
    ai('incitato', 'a magnificent racehorse in a marble stable with a jewelled collar and an ivory manger, servants bowing, opulent and absurd', at='un establo de mármol'))
NAR("Le mató su propia guardia, la guardia pretoriana, que entonces eligió a su tío Claudio, al que encontraron, según la tradición, escondido detrás de una cortina. Claudio, al que todos tomaban por tonto, conquistó Britania.",
    ai('claudio_cortina', 'a frightened middle-aged man hiding behind a heavy curtain in a palace, only his feet visible, soldiers with torches discovering him', at='detrás de una cortina'),
    ph('Claudius bust Naples', at='Claudio', lt=['Claudio', 'Emperador · 41 – 54 d. C.', 'roma']))
NAR("Pero conquistar Britania costó décadas. Y hubo quien se levantó. En el año sesenta, la reina de los icenos, Boudica, azotada por los romanos y con sus hijas ultrajadas, arrasó Londres. Tácito pone en su boca estas palabras antes de la batalla final.",
    ph('Boudica statue Westminster', at='Boudica', lt=['Boudica', 'Reina de los icenos · murió hacia el 61 d. C.', 'barbaros']))
MUR("[serious] No lucho como descendiente de antepasados nobles, sino como una más del pueblo, para vengar mi libertad perdida, mi cuerpo azotado y la honra ultrajada de mis hijas.",
    PAP('No lucho como descendiente de antepasados nobles, sino como una más del pueblo, para vengar mi libertad perdida.', 'Boudica, según Tácito', 'Anales, XIV, 35', at='No lucho'))
NAR("Y un caudillo de Caledonia, la actual Escocia, Calgaco, resumió en otro discurso que recoge Tácito lo que muchos pueblos sentían ante Roma.",
    ai('caledonia', 'a Celtic chieftain with a long cloak standing on a misty Scottish highland ridge before a gathered war host, seen from behind, dramatic clouds', at='Calgaco'))
V('ENE', "[serious] Robar, asesinar, saquear: a eso, con nombre falso, lo llaman imperio. Y donde crean un desierto, lo llaman paz.",
    PAP('Robar, asesinar, saquear: a eso, con nombre falso, lo llaman imperio. Y donde crean un desierto, lo llaman paz.', 'Calgaco, según Tácito', 'Agrícola, 30', at='Robar, asesinar'))
ESP("[serious] Y después, Nerón. Julio del año sesenta y cuatro. Un incendio arranca junto al Circo Máximo y arde durante seis días. De las catorce regiones de Roma, solo cuatro quedan intactas.",
    ph('Nero bust Capitoline Museums', at='Nerón', lt=['Nerón', 'Emperador · 54 – 68 d. C.', 'roma']),
    ph('Fire of Rome Hubert Robert', at='Un incendio'),
    ai('incendio_roma', 'a vast ancient city burning at night, flames over crowded tenement blocks, people fleeing through narrow streets carrying belongings', at='arde durante seis días'))
FUE("[serious] A todo esto se sumaban los lamentos de las mujeres aterradas, los ancianos sin fuerzas y los niños. Unos miraban por sí mismos, otros por los demás. Mientras miraban atrás, el fuego los alcanzaba por delante o por los costados.",
    PAP('Mientras miraban atrás, el fuego los alcanzaba por delante o por los costados.', 'Tácito', 'Anales, XV, 38', at='A todo esto'))
NAR("¿Tocó Nerón la lira mientras Roma ardía? Tácito, el historiador más serio de la época, dice que Nerón estaba en Antium, a más de cincuenta kilómetros. Que volvió, abrió sus jardines para refugiar a la gente y bajó el precio del grano. Y que corrió el rumor de que había cantado la caída de Troya. Un rumor.",
    MITO('Nerón tocaba la lira mientras Roma ardía.', 'Tácito lo sitúa en Antium cuando empezó el fuego; volvió, abrió sus jardines a los refugiados y abarató el grano. Lo del canto era un rumor. Y el violín de las películas no existía.',
         fuente='Tácito, Anales, XV, 38-39', at='Tocó Nerón'))
NAR("Lo que sí es cierto es lo que hizo después: buscó culpables. Y los encontró en un grupo pequeño y mal visto, los cristianos. Tácito describe cómo los quemaron como antorchas para iluminar sus jardines por la noche.",
    ph('Nero torches Siemiradzki', at='los cristianos'))
NAR("Y sobre las ruinas, Nerón construyó su Casa Dorada, un palacio de lujo delirante en pleno centro de Roma. En el año sesenta y ocho, abandonado por todos, se quitó la vida. Le siguió un año de caos con cuatro emperadores. El último en pie fue un general de origen modesto y mucho sentido del humor: Vespasiano.",
    ph('Domus Aurea Rome', at='su Casa Dorada', lt=['Domus Aurea', 'La Casa Dorada de Nerón · Roma']),
    ph('Vespasian bust Ny Carlsberg', at='Vespasiano', lt=['Vespasiano', 'Emperador · 69 – 79 d. C.', 'roma']))
NAR("[softly] Vespasiano necesitaba dinero y puso un impuesto sobre la orina de los urinarios públicos, que los curtidores usaban para tratar las pieles. Su hijo Tito le dijo que aquello era indigno. Vespasiano le acercó a la nariz una moneda del primer pago y le preguntó si olía mal. Tito dijo que no.",
    ai('urinarios', 'a Roman public latrine with a row of stone seats and a man collecting urine in large clay jars for tanners, humorous tone, daylight', at='la orina'))
V('VES', "[laughs softly] Pues viene de la orina.",
    PAP('Pecunia non olet. El dinero no huele.', 'Vespasiano, según Suetonio', 'Vida de los doce césares, Vespasiano, 23', at='Pues viene'))
NAR("De ahí viene la expresión «el dinero no huele». Y hasta hoy, en Italia, a los urinarios públicos se les llama «vespasiani». Y bromeó hasta el final. Cuando se sintió morir, Suetonio cuenta que dijo:",
    ph('Vespasienne Paris urinal', at='vespasiani'))
V('VES', "[softly] Ay... creo que me estoy convirtiendo en un dios.",
    PAP('Vae, puto deus fio. Ay, creo que me estoy convirtiendo en dios.', 'Vespasiano, según Suetonio', 'Vespasiano, 23', at='convirtiendo en un dios'))
NAR("Porque a los emperadores muertos se les declaraba dioses. Pero lo que de verdad le hizo inmortal fue otra cosa. Sobre el lago de la Casa Dorada de Nerón, Vespasiano empezó a construir el anfiteatro más grande del mundo romano: el Anfiteatro Flavio. Nosotros lo llamamos Coliseo.",
    ph('Colosseum Rome exterior', at='el Coliseo', lt=['Anfiteatro Flavio · el Coliseo', 'Inaugurado en el año 80 d. C.']))
ESP("Lo inauguró su hijo Tito, en el año ochenta, con cien días de juegos. Unos cincuenta mil espectadores. Animales traídos de tres continentes. Cazas, ejecuciones y combates de gladiadores.",
    cd(dict(type='counter', to=50000, label='espectadores en el Coliseo'), at='cincuenta mil'),
    ai('coliseo_lleno', 'inside a packed ancient amphitheatre full of spectators under a huge canvas awning, gladiators on the sand far below, sunlight beams, epic wide', at='combates de gladiadores'),
    ph('Colosseum hypogeum', at='Animales traídos'))
NAR("Y ahora, el gesto más famoso de la Antigüedad... que quizá nunca existió. El pulgar hacia abajo que condena al gladiador viene de un cuadro de mil ochocientos setenta y dos, de Jean-Léon Gérôme. Los textos antiguos hablan de un «pulgar girado», sin explicar hacia dónde. Y muchos combates no acababan en muerte: un gladiador bien entrenado costaba una fortuna.",
    MITO('El pulgar hacia abajo condenaba a muerte al gladiador.', 'La imagen nace de un cuadro de Gérôme de 1872. Las fuentes hablan de un «pulgar girado», sin decir hacia dónde, y muchos combates acababan sin muertos: un gladiador entrenado era demasiado caro.',
         fuente='Juvenal, Sátiras, III, 36', img='gerome', at='el gesto más famoso'),
    ph('Pollice Verso Gerome', at='un cuadro de 1872'),
    ph('gladiator mosaic Zliten', at='bien entrenado'))
NAR("Un año antes de que se inaugurara el Coliseo, el veinticuatro de agosto del año setenta y nueve, según la fecha tradicional, el Vesubio despertó. Un testigo de dieciocho años lo vio desde el otro lado de la bahía: Plinio el Joven. Su tío, el almirante Plinio el Viejo, murió intentando rescatar a los habitantes de la costa.",
    ph('Vesuvius from Naples', at='el Vesubio', lt=['El Vesubio', 'Bahía de Nápoles · hoy']),
    ai('vesubio_nube', 'a gigantic column of volcanic ash rising from a mountain over a bay, spreading at the top like an umbrella pine, small ships on the water, afternoon light', at='Lo vio'))
FUE("La nube se elevaba como un enorme tronco y luego se abría en ramas. Su forma se parecía más a la de un pino que a la de ningún otro árbol.",
    PAP('Su forma se parecía más a la de un pino que a la de ningún otro árbol: se elevaba como un tronco altísimo y luego se abría en ramas.', 'Plinio el Joven', 'Carta a Tácito, VI, 16', at='La nube'))
FUE("[softly] Se oían los gemidos de las mujeres, los llantos de los niños, los gritos de los hombres. Muchos alzaban las manos a los dioses. Pero muchos más pensaban que ya no quedaba ningún dios, y que aquella era la noche eterna y última del mundo.",
    ai('miseno_oscuridad', 'crowds fleeing along a coastal road in total darkness under falling ash, holding torches and cushions over their heads, a woman carrying a child, eerie', at='Se oían los gemidos'),
    PAP('Muchos pensaban que ya no quedaba ningún dios, y que aquella era la noche eterna y última del mundo.', 'Plinio el Joven', 'Carta a Tácito, VI, 20', at='la noche eterna'))
ESP("[serious] Pompeya y Herculano quedaron sepultadas bajo metros de ceniza y flujos de gas ardiente. Y congeladas en el tiempo. Gracias a esa catástrofe sabemos cómo vivía de verdad la gente corriente de Roma. Ahora lo verás.",
    ph('Pompeii forum Vesuvius', at='Pompeya', lt=['Pompeya', 'Campania, Italia · hoy']),
    ph('Pompeii plaster casts', at='congeladas en el tiempo'))
ESP("Era la dinastía flavia. El hijo de Vespasiano, Tito, ya había aplastado nueve años antes una rebelión en Judea y destruido el templo de Jerusalén. Todavía hoy, en el arco que lo celebra en el Foro, se ve a los legionarios desfilando con el gran candelabro del templo.",
    ph('Arch of Titus menorah relief', at='el gran candelabro', lt=['Arco de Tito', 'Foro Romano · hacia 81 d. C.']),
    ph('Arch of Titus Rome', at='en el arco'))
NAR("El siglo termina con buenas noticias. Tras el asesinato del tirano Domiciano, el Senado elige a un anciano respetado, Nerva. Y Nerva tiene una idea brillante: adoptar como hijo y sucesor no a un pariente, sino al mejor hombre disponible. Elige a un general nacido en Hispania, en Itálica, junto a la actual Sevilla. Se llama Trajano.",
    ph('Italica Santiponce amphitheatre', at='Itálica', lt=['Itálica', 'Santiponce, Sevilla · hoy']),
    ph('Trajan bust Glyptothek', at='Trajano', lt=['Trajano', 'Emperador · 98 – 117 d. C. · nacido en Hispania', 'roma']))
ESP("El primer emperador nacido fuera de Italia. Conquista la Dacia, la actual Rumanía, y su oro. Lo celebra con una columna de treinta metros cubierta por una espiral de relieves, que todavía sigue en pie en Roma. En el año ciento diecisiete, Roma alcanza su máxima extensión.",
    ph('Trajan Column Rome', at='una columna', lt=['Columna de Trajano', 'Roma · 113 d. C.']),
    ph('Trajan Column relief detail Dacian', at='una espiral de relieves'),
    cd(dict(type='imperio', title='La máxima extensión', stages=[
        dict(year='44 a. C.', label='Muerte de César', zona=['ITA', 'ESP', 'PRT', 'FRA', 'BEL', 'CHE', 'GRC', 'MKD', 'ALB', 'MNE', 'HRV', 'SYR', 'LBN', {'c': 'TUR', 'box': [26, 36, 38, 42]}, {'c': 'TUN'}, {'c': 'LBY', 'box': [19, 30.5, 25, 33.5]}]),
        dict(year='14 d. C.', label='Muerte de Augusto', zona=['ITA', 'ESP', 'PRT', 'FRA', 'BEL', 'NLD', 'LUX', 'CHE', 'AUT', 'SVN', 'HRV', 'BIH', 'SRB', 'MNE', 'ALB', 'MKD', 'GRC', 'BGR', {'c': 'TUR', 'box': [26, 36, 38, 42]}, 'SYR', 'LBN', 'ISR', 'PSE', {'c': 'EGY', 'box': [[29.0, 29.0, 33.0, 31.7], [30.3, 24.0, 33.3, 29.0]]}, 'TUN', {'c': 'LBY', 'box': [9, 30.5, 25, 33.5]}, {'c': 'DZA', 'box': [-1, 34.5, 9, 37.3]}, {'c': 'MAR', 'box': [-7, 33.5, -1, 36]}]),
        dict(year='117 d. C.', label='Máxima extensión, con Trajano', zona=['ITA', 'ESP', 'PRT', 'FRA', 'BEL', 'NLD', 'LUX', 'CHE', 'AUT', 'SVN', 'HRV', 'BIH', 'SRB', 'MNE', 'ALB', 'MKD', 'GRC', 'BGR', 'ROU', 'TUR', 'CYP', 'SYR', 'LBN', 'ISR', 'PSE', 'JOR', 'ARM', {'c': 'IRQ', 'box': [40, 30.5, 48, 37.3]}, {'c': 'EGY', 'box': [[29.0, 29.0, 33.0, 31.7], [30.3, 24.0, 33.3, 29.0]]}, 'TUN', {'c': 'LBY', 'box': [9, 30.5, 25, 33.5]}, {'c': 'DZA', 'box': [-1, 34.5, 9, 37.3]}, {'c': 'MAR', 'box': [-7, 33.5, -1, 36]}, {'c': 'GBR', 'box': [-6, 50, 2, 55.2]}, {'c': 'DEU', 'box': [5.5, 47.5, 9.5, 51]}, {'c': 'HUN', 'box': [16, 45.7, 19.2, 48]}])]), at='su máxima extensión'))
NAR("Cinco millones de kilómetros cuadrados. Desde Britania hasta el golfo Pérsico. Unos sesenta millones de personas, según los cálculos modernos. Y por primera vez, el centro del mundo lo gobernaba un hispano.",
    cd(dict(type='counter', to=5000000, label='kilómetros cuadrados · año 117 d. C.'), at='Cinco millones'))
