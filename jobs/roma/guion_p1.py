# -*- coding: utf-8 -*-
# «La Antigua Roma (Historia Completa)» · parte 1: apertura, capítulos I a III
from lib import *

# ---------------- APERTURA ----------------
B('tension')
NAR("[serious] Has visto mil veces la Antigua Roma. Gladiadores, legiones, emperadores locos, un imperio que cae en una sola noche. [short pause] Casi todo lo que crees saber de Roma te lo contó Hollywood. Y casi todo está mal.",
    ph('Colosseum Rome aerial', at='Has visto'),
    ph('Pollice Verso Gerome', at='Gladiadores'),
    ai('legion_marcha', 'a Roman legion marching in the rain along a stone road, seen from behind, shields on their backs', at='legiones'),
    ph('Nero bust Capitoline Museums', at='emperadores locos'),
    K('HOLLYWOOD', 'Hollywood film set Rome 1950s', at='Hollywood'))
ESP("[dramatically] Esta es la otra historia. La real. La de una aldea de pastores que llegó a gobernar a uno de cada cuatro seres humanos del planeta. Y que lo hizo durante más de mil años.",
    ai('aldea_palatino', 'a small village of oval thatched huts on a hill above a marshy river valley at dawn, smoke rising, Iron Age Italy', at='una aldea de pastores'),
    cd(dict(type='counter', to=60000000, label='habitantes del Imperio en su apogeo, según los cálculos modernos'), at='uno de cada cuatro'),
    ph('Forum Romanum panorama', at='más de mil años'))
FUE("¿Quién hay tan necio o tan indolente que no quiera saber cómo, y bajo qué sistema de gobierno, casi todo el mundo habitado cayó bajo el dominio único de los romanos en menos de cincuenta y tres años?",
    PAP('¿Quién hay tan necio o tan indolente que no quiera saber cómo, y bajo qué sistema de gobierno, casi todo el mundo habitado cayó bajo el dominio único de los romanos en menos de cincuenta y tres años?',
        'Polibio', 'Historias, libro I · hacia 150 a. C.', at='Quién hay'))
NAR("Lo escribió Polibio, un griego que vio a Roma desde dentro, como rehén. Esa es la pregunta. Y hay otras dos. ¿Por qué esa máquina invencible se rompió? [pause] ¿Y de verdad se rompió?",
    ph('Polybius relief Kleitor', at='Polibio', lt=['Polibio', 'Historiador griego · rehén en Roma desde 167 a. C.', 'oriente']),
    ai('maquina_rota', 'a colossal broken marble statue of a Roman emperor lying in tall grass among ruins, dusk light, crows', at='se rompió'),
    ph('Forum Romanum ruins sunset', at='de verdad'))
NAR("[serious] Durante una hora vamos a recorrer doce siglos. Con los que lo vivieron, con lo que dejaron escrito en libros, en piedra y hasta en las paredes de los bares. [short pause] Bienvenido a la verdadera historia de Roma.",
    ph('Roman inscription marble Capitoline', at='en piedra'),
    ph('Pompeii graffiti wall', at='las paredes de los bares'),
    ph('Via Appia Antica', at='Bienvenido'))
T('La Antigua Roma', 'Historia completa', secs=5.5, sting='tema', text='[dramatically] La Antigua Roma. Historia completa.', chapter=False)

# ---------------- I · LA LOBA Y LOS REYES ----------------
T('La loba y los reyes', '753 – 509 a. C.', num='I', sting='tema')
B('tema')
NAR("Roma presume de una fecha de nacimiento exacta: el veintiuno de abril del año setecientos cincuenta y tres antes de Cristo. Y de una historia de película.",
    ph('Palatine Hill Rome view', at='veintiuno de abril', lt=['El Palatino', 'Roma · hoy']),
    ph('Capitoline Wolf', at='una historia de película'))
ESP("Dos gemelos, Rómulo y Remo, hijos del dios Marte, arrojados al río Tíber. Una loba que los amamanta. Un pastor que los cría. Y años después, una pelea por fundar una ciudad que termina con un hermano matando al otro.",
    ai('gemelos_tiber', 'a wicker basket with two newborn babies floating on a dark flooded river among reeds at night, moonlight', at='arrojados al río'),
    ph('Capitoline Wolf', at='Una loba'),
    ai('remo_muerte', 'two young men fighting with swords beside a shallow trench marking the boundary of a future city, one falling, dust, dusk, faces in shadow', at='una pelea'))
NAR("Así lo cuenta Tito Livio, el gran historiador de Roma. Pero Livio, que escribía siete siglos después, era el primero en avisar de que aquello era una leyenda.",
    ph('Titus Livius statue Padua', at='Tito Livio', lt=['Tito Livio', 'Historiador romano · 59 a. C. – 17 d. C.', 'roma']))
FUE("Se concede a la Antigüedad la licencia de mezclar lo humano con lo divino, para hacer más venerables los orígenes de las ciudades.",
    PAP('Se concede a la Antigüedad la licencia de mezclar lo humano con lo divino, para hacer más venerables los orígenes de las ciudades.',
        'Tito Livio', 'Historia de Roma, prefacio', at='Se concede'))
NAR("[softly] Y hay más. El propio Livio recoge que algunos daban una explicación mucho menos poética: en latín, «loba» era también una forma de llamar a las prostitutas. [short pause] Quizá la famosa loba fue simplemente la mujer del pastor.",
    MITO('Una loba salvaje amamantó a Rómulo y Remo.', 'Ya los romanos dudaban: «lupa», loba, también significaba prostituta. Livio recoge que algunos veían en la loba a la mujer del pastor que los crió.',
         fuente='Tito Livio, Historia de Roma, I, 4', at='Y hay más'))
NAR("¿Y qué dice la arqueología? Que en el siglo octavo antes de Cristo había, efectivamente, cabañas sobre la colina del Palatino. Se han encontrado los agujeros de sus postes, excavados en la roca. No una gran ciudad, sino un puñado de aldeas de pastores sobre siete colinas, junto a un pantano.",
    ph('Hut of Romulus Palatine postholes', at='la arqueología'),
    ph('Iron Age hut urn Latium', at='cabañas sobre la colina'),
    ai('aldeas_pantano', 'bird-eye view of scattered hilltop villages of thatched huts over a misty marsh by a winding river, early Rome, dawn', at='un puñado de aldeas'))
NAR("Lo que esas aldeas sí tenían era un lugar privilegiado: un vado para cruzar el Tíber, sal en la desembocadura y un río navegable hasta el mar. El sitio perfecto para comerciar.",
    cd(dict(type='map', title='El Lacio, siglo VIII a. C.', bbox=[11.6, 41.3, 13.4, 42.3], points=[dict(name='Roma', lon=12.48, lat=41.89, big=1), dict(name='Ostia, salinas', lon=12.29, lat=41.75), dict(name='Veyes', lon=12.40, lat=42.02), dict(name='Alba Longa', lon=12.65, lat=41.75)]), at='un lugar privilegiado'),
    ph('Tiber Island Rome', at='cruzar el Tíber'))
NAR("Durante casi dos siglos y medio, Roma tuvo reyes. La tradición cuenta siete. Algunos eran latinos, otros sabinos y los últimos, etruscos: el pueblo más refinado de Italia, que les enseñó a desecar pantanos, a leer el futuro en las entrañas de los animales y a levantar templos.",
    cd(dict(type='list', header='Los siete reyes de la tradición', items=['Rómulo', 'Numa Pompilio', 'Tulo Hostilio', 'Anco Marcio', 'Tarquinio Prisco', 'Servio Tulio', 'Tarquinio el Soberbio']), at='La tradición cuenta siete'),
    ph('Etruscan sarcophagus of the spouses', at='etruscos', lt=['Los etruscos', 'Sarcófago de los esposos · siglo VI a. C.', 'oriente']),
    ph('Cloaca Maxima Rome outlet', at='desecar pantanos'),
    ph('Liver of Piacenza', at='las entrañas'))
NAR("Lo que hicieron los etruscos en Roma se puede tocar todavía. La Cloaca Máxima, la gran alcantarilla que convirtió una ciénaga en la plaza más famosa de la historia: el Foro.",
    ph('Cloaca Maxima Rome', at='Cloaca Máxima', lt=['Cloaca Máxima', 'Roma · siglo VI a. C.']),
    ph('Roman Forum view from Capitoline', at='el Foro'))
ESP("[serious] Hasta que llegó el último rey, Tarquinio el Soberbio. Su hijo violó a una noble romana, Lucrecia. Ella contó a su familia lo que había pasado y se quitó la vida. [short pause] Su pariente, Lucio Junio Bruto, juró sobre el puñal que no volvería a haber un rey en Roma.",
    ai('tarquinio_trono', 'a dark throne room of an archaic Italian king, a heavy figure seen from behind on a carved throne, torches, threatening atmosphere', at='Tarquinio el Soberbio'),
    ph('Death of Lucretia painting', at='Lucrecia'),
    ph('Oath of Brutus painting', at='juró sobre el puñal'))
NAR("Año quinientos nueve antes de Cristo, según la tradición. Los romanos expulsan a su rey. Y desde entonces, la palabra «rey» será el peor insulto que se pueda lanzar a un político. Recuerda esto, porque va a costarle la vida a Julio César.",
    ph('Capitoline Brutus bust', at='expulsan a su rey', lt=['Lucio Junio Bruto', 'Fundador de la República, según la tradición', 'roma']),
    K('REX', 'Roman inscription marble letters', at='el peor insulto'),
    ph('Julius Caesar Tusculum bust', at='Julio César'))

# ---------------- II · LA REPÚBLICA QUE NO SE RENDÍA ----------------
T('La República que no se rendía', '509 – 264 a. C.', num='II', sting='tema')
B('tema')
NAR("En lugar de un rey, Roma inventa un sistema que todavía nos suena: la República, la «cosa pública». Dos cónsules elegidos cada año, que se vigilan entre sí. Un Senado de antiguos magistrados. Y asambleas donde vota el pueblo.",
    ph('SPQR inscription', at='la República'),
    cd(dict(type='list', header='La República romana', items=['Dos cónsules, elegidos cada año', 'El Senado, de antiguos magistrados', 'Las asambleas del pueblo', 'Los tribunos de la plebe, con derecho de veto']), at='Dos cónsules'),
    ph('Cicero denounces Catiline Maccari', at='un Senado'))
NAR("Cuatro letras lo resumen todo. S, P, Q, R: el Senado y el Pueblo Romano. Hoy siguen grabadas en las alcantarillas de Roma.",
    K('SPQR', 'SPQR manhole cover Rome', at='Cuatro letras'),
    ph('SPQR manhole cover Rome', at='alcantarillas'))
NAR("[softly] Pero ojo: no era una democracia. Los ricos votaban primero y su voto valía mucho más. Los pobres, la plebe, tuvieron que pelear durante dos siglos por sus derechos. Y su arma fue sorprendente: la huelga. Se marchaban en masa de la ciudad y dejaban a los patricios sin soldados.",
    MITO('Roma fue una democracia, como Atenas.', 'Votaba el pueblo, pero los más ricos votaban primero y su voto pesaba mucho más. Muchas votaciones se decidían antes de que votaran los pobres.', at='no era una democracia'),
    ai('secesion_plebe', 'a long column of poor Roman men, women and carts leaving a walled city along a dusty road toward a hill, seen from behind, early Republic', at='Se marchaban en masa'))
ESP("Era una Roma de campesinos soldados. Como Cincinato. En el año cuatrocientos cincuenta y ocho antes de Cristo, un ejército romano queda atrapado. Los senadores van a buscar a Cincinato y lo encuentran arando su pequeña granja.",
    ai('cincinato_arado', 'an older Roman farmer in a simple tunic ploughing a small field with oxen, seen from behind, envoys in togas approaching across the field', at='arando su pequeña granja'))
NAR("Le nombran dictador: un cargo de emergencia, con poder absoluto, durante seis meses como máximo. Cincinato derrota al enemigo, renuncia al cargo a los dieciséis días y vuelve a su arado. [short pause] Por eso hay una ciudad en Estados Unidos que se llama Cincinnati.",
    ph('Cincinnatus statue Cincinnati', at='dictador'),
    cd(dict(type='counter', to=16, label='días con poder absoluto antes de renunciar'), at='a los dieciséis días'),
    ph('Cincinnati skyline', at='Cincinnati', lt=['Cincinnati', 'Ohio, Estados Unidos · hoy']))
ESP("[serious] Hacia el año trescientos noventa antes de Cristo, la catástrofe. Un ejército de galos, guerreros celtas del norte, aplasta a los romanos junto al río Alia y entra en la ciudad. Roma arde.",
    ph('Dying Gaul Capitoline', at='galos', lt=['Los galos', 'Pueblos celtas del norte de Italia y de la Galia', 'barbaros']),
    ai('galos_roma_arde', 'Celtic warriors with long hair and spears entering a burning early Roman town at night, silhouettes against flames', at='Roma arde'))
NAR("Solo resiste la colina del Capitolio. Y aquí viene uno de los momentos más absurdos y gloriosos de la historia de Roma. Una noche, los galos trepan en silencio por la roca. Los perros no ladran. Pero las ocas sagradas del templo de Juno se ponen a graznar... y despiertan a los defensores.",
    ph('Capitoline Hill Rome', at='Capitolio'),
    ai('ocas_capitolio', 'white sacred geese honking wildly at night beside a temple on a rocky hill, a startled Roman soldier waking with a torch, dramatic', at='las ocas sagradas'))
NAR("[softly] Roma, salvada por unas ocas. Los romanos lo recordaron durante siglos: cada año paseaban una oca en litera, adornada con oro... y crucificaban a un perro.",
    ph('Capitoline geese painting', at='salvada por unas ocas'))
NAR("Los galos solo se marchan a cambio de mil libras de oro. Cuando los romanos protestan porque la balanza está trucada, el jefe galo, Breno, arroja su espada sobre la balanza y pronuncia la frase.",
    ph('Brennus and his share of the spoils', at='Breno', lt=['Breno', 'Jefe galo', 'barbaros']))
V('ENE', "[dramatically] ¡Ay de los vencidos!",
    PAP('Vae victis. ¡Ay de los vencidos!', 'Breno, según Tito Livio', 'Historia de Roma, V, 48', at='Ay de los vencidos'))
NAR("Roma aprendió la lección. Nunca volvería a ser débil. En los siguientes cien años construye murallas de piedra, reorganiza su ejército y, poco a poco, guerra a guerra y pacto a pacto, se hace dueña de Italia.",
    ph('Servian Wall Rome Termini', at='murallas de piedra', lt=['Muralla Serviana', 'Roma · siglo IV a. C.']),
    ai('legion_manipulos', 'early Roman infantry in checkerboard formation advancing across a hilly field, oval shields, morning haze, seen from above', at='reorganiza su ejército'))
NAR("Y la disciplina de ese ejército era temible. Polibio describe el castigo para una unidad que huía del combate.",
    ai('legion_formada', 'a Roman legion standing in silent ranks on a parade ground under a grey sky, an officer walking between the lines, tense, faces in shadow', at='la disciplina'))
FUE("[serious] El tribuno reúne a la legión, saca al frente a los culpables y elige por sorteo a uno de cada diez. Los elegidos mueren apaleados sin piedad. A los demás se les da cebada en lugar de trigo, y se les obliga a acampar fuera de la protección del campamento.",
    PAP('El tribuno elige por sorteo a uno de cada diez; los elegidos mueren apaleados sin piedad.', 'Polibio', 'Historias, VI, 38', at='El tribuno'),
    K('DIEZMAR', 'Roman legionary relief', at='uno de cada diez'))
NAR("De ahí viene nuestra palabra «diezmar».",
    ph('Roman legionaries Trajan Column relief', at='diezmar'))
NAR("Y empieza a hacer algo que ninguna otra potencia hacía igual: integrar a los vencidos. Muchas ciudades derrotadas se convertían en aliadas, con derechos, y algunas acababan siendo romanas. El enemigo de ayer era el soldado de mañana.",
    ph('Roman citizenship bronze tablet', at='integrar a los vencidos'))
ESP("Y para mover a esos soldados, una obra genial. En el año trescientos doce antes de Cristo, el censor Apio Claudio empieza la primera gran calzada: la Vía Apia. Más de dos mil trescientos años después, todavía puedes caminar sobre ella.",
    ph('Via Appia Antica paving stones', at='la Vía Apia', lt=['Vía Apia', 'Iniciada en 312 a. C. · hoy']),
    ai('calzada_construccion', 'Roman workers building a paved road in layers, gravel, sand and large polygonal stones, a long straight road vanishing into the hills', at='la primera gran calzada'))
NAR("Hacia el año doscientos setenta antes de Cristo, Roma controla toda la península. Hasta un gran general griego, Pirro, con sus elefantes de guerra, la derrota dos veces... y se marcha arruinado. De ahí viene la expresión «victoria pírrica».",
    cd(dict(type='imperio', title='Roma, dueña de Italia', stages=[dict(year='500 a. C.', label='Una ciudad del Lacio', zona=[{'c': 'ITA', 'box': [12.0, 41.4, 13.2, 42.2]}]),
        dict(year='338 a. C.', label='El Lacio y Campania', zona=[{'c': 'ITA', 'box': [11.5, 40.7, 14.6, 42.4]}]),
        dict(year='270 a. C.', label='Toda la Italia peninsular', zona=[{'c': 'ITA', 'box': [8.0, 37.8, 19.0, 44.0]}])], bbox=[5, 36, 20, 47]), at='controla toda la península'),
    ph('Pyrrhus of Epirus bust', at='Pirro', lt=['Pirro', 'Rey de Epiro', 'oriente']),
    ph('war elephant Pyrrhus', at='elefantes de guerra'))
V('ENE', "Si vencemos a los romanos en una batalla más, estaremos completamente perdidos.",
    PAP('Si vencemos a los romanos en una batalla más, estaremos completamente perdidos.', 'Pirro, según Plutarco', 'Vida de Pirro, 21', at='Si vencemos'))

# ---------------- III · ANÍBAL A LAS PUERTAS ----------------
T('Aníbal a las puertas', '264 – 133 a. C.', num='III', sting='tema')
B('tension')
NAR("Al otro lado del mar había otra potencia. Cartago, en la actual Túnez: una ciudad fenicia de comerciantes, la dueña del Mediterráneo occidental. Tenía la mejor flota del mundo. Roma no tenía ni un barco de guerra.",
    ph('Carthage ruins Byrsa', at='Cartago', lt=['Cartago', 'Túnez · hoy', 'cartago']),
    cd(dict(type='versus', title='264 a. C.', left=dict(name='Roma', color=RO, lines=['potencia terrestre', 'dueña de Italia', 'sin flota de guerra']), right=dict(name='Cartago', color=CA, lines=['potencia naval', 'dueña del comercio', 'la mejor flota del mundo'])), at='la mejor flota'))
ESP("La primera guerra estalla en Sicilia, en el año doscientos sesenta y cuatro. Y Roma hace algo increíble: copia un barco cartaginés que ha encallado en su costa, pieza a pieza, y en pocos meses construye una flota entera. Mientras tanto, los remeros aprenden a remar... sentados en bancos sobre la arena.",
    ai('remeros_arena', 'rows of Roman oarsmen training on wooden benches set on a beach, an instructor shouting, unfinished warships on the shore behind, morning', at='sentados en bancos'),
    ai('flota_construccion', 'a huge shipyard on a beach with dozens of wooden warship hulls under construction, carpenters, timber, smoke', at='construye una flota'))
NAR("Y como no saben luchar en el mar, convierten las batallas navales en batallas de infantería: inventan el «cuervo», una pasarela con un pico de hierro que se clava en el barco enemigo. Veintitrés años de guerra. Roma gana. Sicilia es su primera provincia.",
    ai('corvus', 'a Roman boarding bridge with an iron spike slamming down onto an enemy warship deck, legionaries charging across, sea spray', at='el «cuervo»'),
    cd(dict(type='counter', to=23, label='años de la Primera Guerra Púnica (264 – 241 a. C.)'), at='Veintitrés años'))
NAR("Pero en Cartago, un general derrotado, Amílcar Barca, no lo acepta. Se lleva a su familia a la península Ibérica a construir un nuevo imperio. Y antes de partir, según cuenta Polibio, hace jurar algo a su hijo de nueve años.",
    ph('Cartagena Punic wall', at='la península Ibérica', lt=['Qart Hadasht, hoy Cartagena', 'Fundada por los Barca hacia 227 a. C.', 'cartago']))
FUE("Le hizo poner la mano sobre la víctima del sacrificio y jurar que jamás sería amigo de los romanos.",
    PAP('Le hizo poner la mano sobre la víctima del sacrificio y jurar que jamás sería amigo de los romanos.', 'Polibio', 'Historias, III, 11', at='Le hizo poner'),
    ai('juramento_anibal', 'a child placing his hand on a sacrificial altar in a dim Punic temple, a bearded father in shadow behind him, fire light, faces not visible', at='jurar'))
ESP("[dramatically] Ese niño se llamaba Aníbal. Y cumplió su juramento como nadie lo ha cumplido nunca.",
    ph('Hannibal bust Naples', at='Aníbal', lt=['Aníbal Barca', 'General cartaginés · 247 – 183 a. C.', 'cartago']))
NAR("Su gran enemigo, el romano Tito Livio, le odiaba. Y aun así no pudo evitar describirle con admiración.",
    ph('Hannibal Barca coin Carthage', at='le odiaba'))
FUE("Nunca un mismo carácter fue más apto para cosas tan contrarias: obedecer y mandar. Era el más audaz para afrontar los peligros y el más prudente en medio de ellos. Ningún trabajo cansaba su cuerpo ni vencía su ánimo. Muchos le vieron dormir en el suelo, envuelto en su capa de soldado, entre los centinelas.",
    PAP('Nunca un mismo carácter fue más apto para cosas tan contrarias: obedecer y mandar.', 'Tito Livio', 'Historia de Roma, XXI, 4', at='Nunca un mismo'),
    ai('anibal_duerme', 'a general wrapped in a simple soldier cloak sleeping on the bare ground among sentries beside a campfire, war elephants dimly visible behind, night, his face hidden', at='dormir en el suelo'))
NAR("Año doscientos diecinueve antes de Cristo. Aníbal ataca Sagunto, aliada de Roma, en la actual Valencia. Ocho meses de asedio. Es la excusa para la Segunda Guerra Púnica. Y Aníbal tiene un plan que nadie se espera: atacar Roma por tierra, cruzando los Alpes.",
    ph('Sagunto castle', at='Sagunto', lt=['Sagunto', 'Valencia · hoy']),
    cd(dict(type='mapfly', title='La marcha de Aníbal, 218 a. C.', keys=[[-6, 35.5, 14, 47], [-1, 39.5, 14, 47.5]],
        points=[dict(name='Cartagena', lon=-0.98, lat=37.6, at=0.1), dict(name='Sagunto', lon=-0.27, lat=39.68, at=0.2), dict(name='Los Alpes', lon=6.9, lat=45.2, at=0.6), dict(name='Roma', lon=12.48, lat=41.89, at=0.85)],
        arrows=[dict(path=[[-0.98, 37.6], [-0.27, 39.68], [2.2, 41.4], [3.5, 43.3], [4.8, 44.0], [6.9, 45.2], [8.6, 45.1], [10.5, 44.8]], color=CA, at=0.25, dur=2.5)]), at='cruzando los Alpes'))
ESP("Sale de Cartagena con un ejército enorme y treinta y siete elefantes. Atraviesa los Pirineos, cruza el Ródano y sube a los Alpes en otoño. Nieve, desprendimientos, tribus que les tienden emboscadas. Según Polibio, a Italia llegan apenas veintiséis mil hombres. Pero llegan.",
    ai('alpes_elefantes', 'war elephants and soldiers struggling up a narrow snowy mountain pass in a blizzard, cliffs, epic wide shot, Alps', at='sube a los Alpes'),
    ai('alpes_caida', 'a pack mule slipping off an icy mountain ledge, soldiers in cloaks grabbing ropes, snowstorm', at='desprendimientos'))
NAR("Y entonces empieza la pesadilla de Roma. Aníbal la derrota junto al río Trebia. La destroza en el lago Trasimeno, en una emboscada entre la niebla. Y en agosto del año doscientos dieciséis llega Cannas.",
    ai('trasimeno_niebla', 'Roman soldiers marching along a lakeshore in thick fog, shadows of ambushers on the hillside above, eerie', at='entre la niebla'),
    ph('Lake Trasimeno', at='el lago Trasimeno', lt=['Lago Trasimeno', 'Umbría, Italia · hoy']))
ESP("[serious] En Cannas, Roma reúne el ejército más grande de su historia: más de ochenta mil hombres. Aníbal tiene muchos menos. Deja que los romanos empujen por el centro... y cierra las alas. Los rodea por completo.",
    cd(dict(type='list', header='Cannas · 2 de agosto de 216 a. C.', items=['Roma: más de 80.000 hombres', 'Aníbal: unos 50.000', 'El centro cartaginés cede a propósito', 'Las alas y la caballería cierran el cerco']), at='más de ochenta mil'),
    ai('cannas_cerco', 'aerial view of a vast ancient battle, a dense mass of Roman soldiers encircled on all sides by enemy infantry and cavalry, dust clouds', at='Los rodea por completo'))
NAR("Lo que sigue es una de las peores matanzas de la historia antigua. Polibio habla de unos setenta mil romanos muertos en una sola tarde. Los historiadores de hoy rebajan la cifra, pero la mayoría la sigue situando por encima de los cincuenta mil. Todavía hoy, las academias militares estudian Cannas.",
    cd(dict(type='counter', to=50000, prefix='+', label='romanos muertos en una sola tarde, según los cálculos actuales'), at='una sola tarde'),
    ai('cannas_despues', 'a battlefield at sunset covered with abandoned shields and broken spears, crows, a lone figure walking among them, no gore', at='las academias militares'))
NAR("El camino a Roma está abierto. Y Aníbal... no ataca. Su general de caballería, Maharbal, le reprocha la decisión con una frase que ha pasado a la historia.",
    ph('Hannibal counting rings Cannae', at='no ataca'))
V('ENE', "[serious] Sabes vencer, Aníbal. Pero no sabes aprovechar la victoria.",
    PAP('Sabes vencer, Aníbal; pero no sabes aprovechar la victoria.', 'Maharbal, según Tito Livio', 'Historia de Roma, XXII, 51', at='Sabes vencer'))
NAR("¿Fue un error? Probablemente no. Aníbal no tenía máquinas de asedio y Roma tenía murallas, reservas casi infinitas de hombres y algo más: no se rendía. Nunca. Ni siquiera negoció. [short pause] Y encontró a su propio genio.",
    ph('Servian Wall Rome', at='murallas'),
    K('NO SE RINDE', 'Roman legionary relief', at='no se rendía'))
ESP("Publio Cornelio Escipión, de solo veinticinco años, desembarca en Hispania y toma por sorpresa la capital de los Barca, Cartagena. Después lleva la guerra a África. Y en el año doscientos dos, en Zama, derrota a Aníbal con sus propias tácticas.",
    ph('Scipio Africanus bust', at='Publio Cornelio Escipión', lt=['Escipión el Africano', 'General romano · 236 – 183 a. C.', 'roma']),
    ai('cartagena_asalto', 'Roman soldiers wading through a shallow lagoon at low tide to storm the walls of a coastal city, ladders, dawn', at='toma por sorpresa'),
    ai('zama_elefantes', 'war elephants charging through open lanes between Roman infantry ranks, trumpets, dust, chaos, wide angle', at='en Zama'))
NAR("Aníbal huyó y acabó envenenándose años después, en Asia, para no caer en manos romanas. Cartago sobrevivió, pero sin flota y pagando a Roma durante medio siglo. Y aun así, en el Senado había un hombre al que eso no le bastaba.",
    ph('Carthage Punic ports', at='Cartago sobrevivió'))
NAR("Catón el Viejo. Un día dejó caer unos higos frescos en el Senado. Los senadores admiraron lo grandes que eran. Catón les explicó que venían de Cartago... a solo tres días de barco. Y terminaba todos sus discursos, hablara de lo que hablara, igual.",
    ph('Cato the Elder bust', at='Catón el Viejo', lt=['Catón el Viejo', 'Senador y censor · 234 – 149 a. C.', 'roma']),
    ai('higos_senado', 'an old stern Roman senator in a toga holding up large fresh figs in front of a hall of senators, seen from the side, faces in shadow', at='unos higos frescos'))
V('CAT', "Estos higos se cogieron en Cartago hace solo tres días. Así de cerca tenemos al enemigo.",
    PAP('Estos higos se cogieron en Cartago hace solo tres días. Así de cerca tenemos al enemigo.', 'Catón, según Plutarco', 'Vida de Catón el Viejo, 27', at='Estos higos'))
V('CAT', "[serious] Y, además, opino que Cartago debe ser destruida.",
    PAP('Ceterum censeo Carthaginem esse delendam.', 'Catón el Viejo', 'Fórmula que la tradición pone en su boca', at='Cartago debe ser destruida'))
ESP("[serious] Lo consiguió. En el año ciento cuarenta y seis antes de Cristo, tras tres años de asedio, los romanos entran en Cartago. Seis días de combates casa por casa. La ciudad es arrasada. Los supervivientes, vendidos como esclavos. Ese mismo año, Roma destruye también Corinto, en Grecia.",
    ai('cartago_arde', 'a great coastal city burning at night, Roman soldiers on the walls in silhouette, smoke over the harbour', at='entran en Cartago'),
    cd(dict(type='imperio', title='146 a. C.: Roma, sin rival en el Mediterráneo', stages=[
        dict(year='241 a. C.', label='Sicilia, primera provincia', zona=[{'c': 'ITA', 'box': [8.0, 36.5, 19.0, 44.0]}]),
        dict(year='201 a. C.', label='Hispania, Cerdeña, Córcega', zona=['ITA', {'c': 'ESP', 'box': [-6.5, 36.0, 3.5, 41.8]}]),
        dict(year='146 a. C.', label='África, Macedonia, Grecia', zona=['ITA', {'c': 'ESP', 'box': [-7.5, 36.0, 3.5, 42.0]}, {'c': 'TUN', 'box': [8.3, 34.5, 11.5, 37.5]}, 'GRC', 'MKD', 'ALB'])]), at='Corinto'))
NAR("Dicen que el general que la destruyó, Escipión Emiliano, lloró ante las llamas. Y que recitó unos versos de Homero sobre la caída de Troya. Cuando le preguntaron por qué, contestó que temía que algún día alguien dijera lo mismo de Roma.",
    ph('Scipio Aemilianus', at='Escipión Emiliano', lt=['Escipión Emiliano', 'Destructor de Cartago y Numancia', 'roma']))
NAR("Hispania tampoco se rindió fácil. Durante veinte años, una pequeña ciudad celtíbera, Numancia, junto a la actual Soria, humilló a un ejército romano tras otro. Hizo falta el mismo Escipión, sesenta mil hombres y un cerco de nueve kilómetros para rendirla por hambre. Muchos numantinos prefirieron morir antes que entregarse. Era el año ciento treinta y tres antes de Cristo.",
    ph('Numantia ruins Soria', at='Numancia', lt=['Numancia', 'Garray, Soria · hoy']),
    ai('numancia_cerco', 'a Celtiberian hilltop town surrounded by a long Roman siege wall with towers in winter, smoke, desolate', at='un cerco de nueve kilómetros'),
    ph('Last Day of Numantia Alejo Vera', at='prefirieron morir'))
