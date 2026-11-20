# -*- coding: utf-8 -*-
# «La Antigua Roma (Historia Completa)» · parte 3: capítulos VII a X y epílogo
from lib import *

# ---------------- VII · LA ROMA DE LA CALLE ----------------
T('La Roma de la calle', 'Cómo vivía la gente de verdad', num='VII', sting='tema')
B('noche')
MUR("Olvida por un momento a los emperadores. La mayoría de los romanos nunca vio a uno. Vivía en una ciudad de casi un millón de habitantes, la más grande del mundo antiguo, apretada en bloques de pisos de hasta seis plantas: las ínsulas.",
    ai('insula_calle', 'a crowded narrow street in ancient Rome lined with five and six storey brick apartment blocks, laundry, shops at street level, bustling crowd, afternoon light', at='la mayoría de los romanos'),
    ph('Insula Ara Coeli Rome', at='las ínsulas', lt=['Ínsula del Aracoeli', 'Bloque de pisos del siglo II · Roma']))
MUR("Abajo, tiendas y tabernas. Arriba, cuanto más alto, más pobre. Sin agua corriente, sin cocina, con un riesgo constante de incendio y de derrumbe. Los ricos vivían en casas con jardín. Los pobres comían en la calle, en los termopolios, los bares de comida caliente.",
    ph('Thermopolium Pompeii', at='los termopolios', lt=['Termopolio', 'Bar de comida caliente · Pompeya']),
    ph('House of the Vettii peristyle Pompeii', at='casas con jardín'))
MUR("Y los romanos escribían en las paredes. Muchísimo. En Pompeya se han catalogado miles de grafitos: anuncios electorales, insultos, declaraciones de amor, cuentas, chistes.",
    ph('Pompeii electoral inscription', at='anuncios electorales'),
    ph('Pompeii graffiti wall', at='en las paredes'))
MUR("Algunos parecen sacados de una campaña electoral de hoy.",
    ph('Pompeii electoral programmata', at='campaña electoral'))
FUE("Todos los vendedores de fruta, junto con Helvio Vestal, os piden que elijáis a Marco Holconio Prisco como duunviro.",
    cd(dict(type='grafito', latin='M HOLCONIVM PRISCVM IIVIRVM POMARI VNIVERSI CVM HELVIO VESTALE ROG', text='Todos los vendedores de fruta, con Helvio Vestal, os piden que elijáis a Marco Holconio Prisco como duunviro.', ref='Cartel electoral de Pompeya · CIL IV 202'), at='Todos los vendedores'))
MUR("Otros, a ídolos de su tiempo. En una pared de Pompeya alguien escribió sobre un gladiador tracio llamado Celado: «el suspiro de las chicas». Los gladiadores eran las estrellas del rock de Roma.",
    cd(dict(type='grafito', latin='SVSPIRIVM PVELLARVM CELADVS THRAEX', text='Celado, el tracio, el suspiro de las chicas.', ref='Grafito de Pompeya · CIL IV 4342'), at='el suspiro de las chicas'))
MUR("Y hay uno que lo resume todo. Está escrito, precisamente, en una pared.",
    ph('Pompeii Basilica graffiti', at='Está escrito'))
MUR("[softly] Me admiro, pared, de que no te hayas derrumbado, tú que soportas las tonterías de tantos escritores.",
    cd(dict(type='grafito', latin='ADMIROR TE PARIES NON CECIDISSE RUINIS QUI TOT SCRIPTORUM TAEDIA SUSTINEAS', text='Me admiro, pared, de que no te hayas derrumbado, tú que soportas las tonterías de tantos escritores.', ref='Grafito de Pompeya · CIL IV 1904'), at='Me admiro'))
NAR("Dos mil años antes de internet, Roma ya tenía comentarios.",
    K('CIL IV 1904', 'Pompeii Basilica graffiti', at='Roma ya tenía comentarios'))
MUR("[softly] Y no, los romanos no tenían una sala para vomitar en mitad de los banquetes. El «vomitorio» existe, pero era otra cosa: las salidas del anfiteatro por las que la multitud se «vomitaba» a la calle.",
    MITO('En los banquetes romanos había un «vomitorio» para vomitar y seguir comiendo.', 'Vomitorium era la salida de un anfiteatro, por donde el público salía en masa. Ninguna fuente antigua habla de salas para vomitar.', at='no, los romanos no'),
    ph('Colosseum vomitorium entrance', at='las salidas del anfiteatro'))
MUR("En diciembre llegaban las Saturnales, la fiesta más esperada del año. Una semana de banquetes y regalos en la que se permitía casi todo: los esclavos podían hablar con libertad, jugar a los dados y, en algunas casas, eran servidos a la mesa por sus amos. Muchas de nuestras costumbres navideñas tienen algo de aquella fiesta.",
    ai('saturnales', 'a lively Roman household feast in December lit by many oil lamps, servants and masters dining together and laughing, felt caps, gifts on the table, warm', at='las Saturnales'))
MUR("El día a día giraba en torno a tres lugares. Las termas, donde por una moneda ibas a bañarte, a hacer ejercicio, a cerrar negocios y a enterarte de todo. El Foro, para la política y los juicios. Y los espectáculos.",
    ph('Baths of Caracalla ruins', at='Las termas', lt=['Termas de Caracalla', 'Roma · siglo III']),
    ai('termas_interior', 'interior of a grand Roman bath hall with a steaming pool, marble columns, bathers in towels chatting, light through high windows, faces small and indistinct', at='a enterarte de todo'))
ESP("El Circo Máximo, para las carreras de carros, admitía a unas ciento cincuenta mil personas. Las carreras eran la pasión del pueblo. Los aficionados se dividían en equipos por colores, los verdes y los azules, y había conductores de cuadrigas más ricos que muchos senadores.",
    ph('Circus Maximus Rome', at='El Circo Máximo', lt=['Circo Máximo', 'Roma · hoy']),
    ai('carrera_cuadrigas', 'four-horse chariots racing at full speed around the turning post of a huge circus, dust, a roaring crowd, green and blue team colours, dynamic motion', at='carreras de carros'))
MUR("El poeta Juvenal, siempre amargado, se burlaba de ese pueblo que antes repartía mandos y legiones y ahora solo pedía dos cosas.",
    ph('Juvenal', at='Juvenal', lt=['Juvenal', 'Poeta satírico · siglos I y II d. C.', 'roma']))
FUE("[serious] Solo desea ansiosamente dos cosas: pan y juegos de circo.",
    PAP('Duas tantum res anxius optat: panem et circenses.', 'Juvenal', 'Sátiras, X, 81', at='pan y juegos'))
MUR("Pero Roma también descansaba sobre algo que las películas suelen esconder: la esclavitud. En Italia, quizá uno de cada cuatro o cinco habitantes era esclavo, según la mayoría de los cálculos. Trabajaban en minas, en el campo, en las casas. Algunos eran médicos, maestros o secretarios. Podían comprar su libertad o recibirla de su amo. Y los libertos, y sobre todo sus hijos, podían llegar muy alto.",
    ph('Roman slave collar inscription', at='la esclavitud'),
    ai('esclavos_mina', 'chained workers in a dark Roman mine carrying baskets of ore by oil-lamp light, exhausted, faces in shadow', at='en minas'),
    ph('Roman freedman funerary relief', at='los libertos'))
MUR("Las mujeres no votaban ni ocupaban cargos. Pero muchas administraban patrimonios, tenían negocios y, en las clases altas, mandaban más de lo que admitían los historiadores antiguos. Y casi todas las que conocemos de nombre, las conocemos por sus tumbas. Como esta. La de una mujer llamada Claudia, en el siglo segundo antes de Cristo.",
    ph('Roman funerary portrait woman Fayum', at='Las mujeres'),
    ph('Roman tombstone woman relief', at='por sus tumbas'))
MUR("[softly] Extranjero, lo que tengo que decir es poco: detente y léelo. Esta es la tumba, nada hermosa, de una mujer hermosa. Sus padres la llamaron Claudia. Amó a su marido con todo su corazón. Tuvo dos hijos: a uno lo deja sobre la tierra; al otro, bajo la tierra. Fue de conversación agradable y de andar elegante. Cuidó la casa. Hiló la lana. He dicho. Vete.",
    PAP('Extranjero, lo que tengo que decir es poco: detente y léelo. Esta es la tumba, nada hermosa, de una mujer hermosa. Sus padres la llamaron Claudia. Amó a su marido con todo su corazón. Tuvo dos hijos: a uno lo deja sobre la tierra; al otro, bajo la tierra. Fue de conversación agradable y de andar elegante. Cuidó la casa. Hiló la lana. He dicho. Vete.',
        'Epitafio de Claudia', 'Roma, siglo II a. C. · CIL VI 15346', at='Extranjero'))
M('noche', 6)

# ---------------- VIII · AL BORDE DEL ABISMO ----------------
T('Al borde del abismo', '117 – 284 d. C.', num='VIII', sting='tema')
B('tema')
NAR("A Trajano le sucede otro hispano, Adriano. Viajero incansable, amante de Grecia y pragmático: renuncia a las conquistas más difíciles y empieza a amurallar el imperio. En Britania manda levantar un muro de ciento diecisiete kilómetros, de costa a costa.",
    ph('Hadrian bust British Museum', at='Adriano', lt=['Adriano', 'Emperador · 117 – 138 d. C.', 'roma']),
    ph('Hadrian Wall Housesteads', at='un muro', lt=['Muro de Adriano', 'Northumberland, Reino Unido · hoy']))
NAR("Le siguen Antonino Pío y Marco Aurelio. Con ellos, el imperio vive su época dorada.",
    ph('Marcus Aurelius equestrian statue Capitoline', at='Marco Aurelio', lt=['Marco Aurelio', 'Emperador y filósofo · 161 – 180 d. C.', 'roma']))
V('HIS', "Si se pidiera a alguien que señalara el periodo de la historia del mundo en que la condición del género humano fue más feliz y próspera, nombraría sin dudarlo el que va desde la muerte de Domiciano hasta la llegada de Cómodo.",
    PAP('Si se pidiera a alguien que señalara el periodo de la historia en que la humanidad fue más feliz y próspera, nombraría sin dudarlo el que va desde la muerte de Domiciano hasta la llegada de Cómodo.', 'Edward Gibbon', 'Decadencia y caída del Imperio romano, cap. 3', at='Si se pidiera'))
NAR("Gibbon exageraba, por supuesto. Pero algo de razón tenía. Marco Aurelio era el emperador filósofo. Escribió en griego, para sí mismo, un diario de pensamientos que hoy se vende en todas las librerías. Empieza así.",
    ph('Antoninus Pius bust', at='algo de razón', lt=['Antonino Pío', 'Emperador · 138 – 161 d. C.', 'roma']))
V('CAT', "[softly] Al amanecer, dite a ti mismo: hoy me encontraré con un entrometido, un ingrato, un insolente, un tramposo, un envidioso. Ninguno de ellos puede hacerme daño.",
    PAP('Al amanecer, dite a ti mismo: hoy me encontraré con un entrometido, un ingrato, un insolente, un tramposo, un envidioso. Ninguno de ellos puede hacerme daño.',
        'Marco Aurelio', 'Meditaciones, II, 1', at='Al amanecer'))
V('CAT', "[softly] Pronto lo habrás olvidado todo. Y pronto todos te habrán olvidado a ti.",
    PAP('Pronto lo habrás olvidado todo; pronto todos te habrán olvidado.', 'Marco Aurelio', 'Meditaciones, VII, 21', at='Pronto lo habrás'))
NAR("Lo escribió el hombre más poderoso del mundo. En una tienda de campaña, junto al Danubio.",
    ai('marco_tienda', 'a tired older man writing by oil lamp in a military tent at night, a stylus and wax tablet, snow outside the open flap, seen from behind', at='En una tienda'))
ESP("[serious] Pero su reinado fue de todo menos tranquilo. Guerras sin fin en el Danubio contra los germanos. Y una epidemia, la llamada peste antonina, que llegó con las legiones desde Oriente en el año ciento sesenta y cinco y mató, según distintas estimaciones, a millones de personas.",
    ai('danubio_invierno', 'Roman legionaries in fur-lined cloaks on a frozen river bank in winter, Germanic warriors across the ice in the mist', at='en el Danubio'),
    ai('peste', 'an empty Roman street at dusk, a cart with covered bodies, a mourning woman in a doorway, oil lamps, somber, no gore', at='la peste antonina'))
NAR("Y Marco Aurelio rompió la regla de oro de sus antecesores: en lugar de adoptar al mejor, dejó el trono a su hijo, Cómodo. Un emperador que se creía Hércules y bajaba a la arena del Coliseo a luchar como gladiador.",
    ph('Commodus as Hercules Capitoline', at='Cómodo', lt=['Cómodo', 'Emperador · 180 – 192 d. C.', 'roma']))
NAR("[softly] Tras su asesinato llega el momento más vergonzoso: en el año ciento noventa y tres, la guardia pretoriana mata al emperador y, literalmente, subasta el imperio al mejor postor. Lo gana un senador rico, Didio Juliano. Duró sesenta y seis días.",
    ai('subasta_imperio', 'soldiers in armour standing on the walls of a fortified camp shouting bids to two rich men in togas below, coins, absurd scene, daylight', at='subasta el imperio'),
    cd(dict(type='counter', to=66, label='días duró el emperador que compró el trono'), at='sesenta y seis días'))
NAR("Del caos sale un general africano, nacido en Leptis Magna, en la actual Libia: Septimio Severo. Gobierna con el ejército. Y en su lecho de muerte, según el historiador Dion Casio, dejó a sus hijos un consejo que resume dos siglos de historia.",
    ph('Septimius Severus bust Glyptothek', at='Septimio Severo', lt=['Septimio Severo', 'Emperador · 193 – 211 d. C. · nacido en África', 'roma']),
    ph('Leptis Magna arch', at='Leptis Magna', lt=['Leptis Magna', 'Libia · hoy']))
V('AUG', "[serious] Llevaos bien entre vosotros. Enriqueced a los soldados. Y despreciad a todos los demás.",
    PAP('Llevaos bien entre vosotros, enriqueced a los soldados y despreciad a todos los demás.', 'Septimio Severo, según Dion Casio', 'Historia romana, LXXVII, 15', at='Llevaos bien'))
NAR("No le hicieron caso en lo primero. Ese mismo año, Caracalla mandó asesinar a su hermano Geta en brazos de su propia madre.",
    ph('Severan Tondo Geta erased', at='su hermano Geta', lt=['Tondo severiano', 'El rostro de Geta, borrado tras su asesinato']))
NAR("En el año doscientos doce, el emperador Caracalla toma una decisión enorme, aunque casi nadie la recuerda: concede la ciudadanía romana a todos los hombres libres del imperio. De Britania a Egipto, todos son romanos. La historiadora Mary Beard termina precisamente en ese año su célebre historia de Roma: para ella, ahí acaba un modo de ser romano y empieza otro.",
    ph('Caracalla bust Naples', at='Caracalla', lt=['Caracalla', 'Emperador · 211 – 217 d. C.', 'roma']),
    K('TODOS ROMANOS', 'Constitutio Antoniniana papyrus Giessen', at='todos son romanos'))
ESP("[serious] Y después, el abismo. Entre el año doscientos treinta y cinco y el doscientos ochenta y cuatro, en solo medio siglo, más de veinte emperadores reconocidos. Casi todos asesinados por sus propios soldados. Guerras civiles, invasiones en todas las fronteras, la moneda convertida en casi cobre puro, inflación desbocada.",
    cd(dict(type='counter', to=20, prefix='+', label='emperadores en cincuenta años (235 – 284)'), at='más de veinte emperadores'),
    ph('Antoninianus debased coin', at='la moneda'),
    ai('crisis_soldados', 'soldiers raising a new emperor on a shield in a muddy military camp while the body of the previous one lies covered nearby, torches, grim', at='asesinados por sus propios soldados'))
NAR("En el año doscientos sesenta, la humillación definitiva. El emperador Valeriano es derrotado y capturado por el rey persa Sapor. Es el primer emperador romano hecho prisionero. Sapor lo grabó en la roca para la eternidad.",
    ph('Naqsh-e Rostam Shapur Valerian relief', at='lo grabó en la roca', lt=['Naqsh-e Rostam', 'Relieve de Sapor I · Irán']))
NAR("Y el imperio llega a partirse en tres: un imperio galo al oeste, el reino de la reina Zenobia de Palmira al este y, en medio, lo que queda de Roma. Hasta que un emperador soldado, Aureliano, lo vuelve a unir... y rodea Roma de murallas. Por primera vez en siglos, la capital del mundo tiene miedo.",
    cd(dict(type='imperio', title='El imperio partido en tres · hacia el 271', stages=[dict(year='271 d. C.', label='Imperio galo · Roma · Palmira', zona=['ITA', 'AUT', 'SVN', 'HRV', 'BIH', 'SRB', 'MNE', 'ALB', 'MKD', 'GRC', 'BGR', {'c': 'TUN'}, {'c': 'LBY', 'box': [9, 30.5, 19, 33.5]}, {'c': 'DZA', 'box': [-1, 34.5, 9, 37.3]}])],
        color=RO), at='partirse en tres'),
    ph('Aurelian Walls Rome', at='murallas', lt=['Muralla Aureliana', 'Roma · 271 d. C.']))
M('tension', 5)
NAR("Recapitulemos. Roma ha tenido su época dorada con emperadores hispanos y filósofos. Pero en el siglo tercero ha estado a punto de desaparecer. La pregunta ya no es cómo crecer. Es cómo sobrevivir.",
    cd(dict(type='recap', title='Hasta aquí', items=[['27 a. C.', 'Augusto, primer emperador'], ['117 d. C.', 'Máxima extensión, con Trajano'], ['212 d. C.', 'Todos los hombres libres, ciudadanos'], ['235 – 284', 'Medio siglo de caos']]), at='Recapitulemos'))

# ---------------- IX · LA CRUZ Y LA ESPADA ----------------
T('La cruz y la espada', '284 – 395 d. C.', num='IX', sting='tema')
B('tema')
NAR("La respuesta la da un hombre de origen humildísimo, nacido en Dalmacia, quizá hijo de un antiguo esclavo: Diocleciano. Su conclusión es simple. El imperio es demasiado grande para un solo hombre. Lo divide entre cuatro gobernantes, la tetrarquía, dobla el ejército, fija por ley los precios de mil productos y persigue con dureza a los cristianos.",
    ph('Diocletian bust Istanbul', at='Diocleciano', lt=['Diocleciano', 'Emperador · 284 – 305 d. C.', 'roma']),
    ph('Portrait of the Four Tetrarchs Venice', at='la tetrarquía', lt=['Los tetrarcas', 'Basílica de San Marcos, Venecia']),
    ph('Edict on Maximum Prices inscription', at='fija por ley los precios'))
NAR("Y luego hace algo que ningún emperador había hecho: se jubila. Se retira a su palacio de Split, en la actual Croacia. Cuando años después le piden que vuelva para arreglar otra guerra civil, según cuenta una crónica antigua, contesta:",
    ph('Diocletian Palace Split', at='palacio de Split', lt=['Palacio de Diocleciano', 'Split, Croacia · hoy']))
V('VES', "[softly] Si pudierais ver las coles que he plantado con mis propias manos en Salona, no me pediríais semejante cosa.",
    PAP('Si pudierais ver las coles que he plantado con mis propias manos en Salona, no me pediríais semejante cosa.', 'Diocleciano', 'Epítome de los césares, 39', at='Si pudierais ver'),
    ai('coles_diocleciano', 'an old man in a simple tunic tending a vegetable garden of cabbages in front of a huge seaside palace, peaceful, warm evening light, seen from behind', at='las coles'))
ESP("Su sistema no le sobrevivió. Tras otra guerra civil, en el año trescientos doce, un general llamado Constantino se enfrenta a su rival junto al puente Milvio, a las puertas de Roma. Según los autores cristianos, antes de la batalla vio una señal en el cielo y ordenó pintar en los escudos un símbolo de Cristo. Gana.",
    ph('Constantine colossus Capitoline head', at='Constantino', lt=['Constantino I', 'Emperador · 306 – 337 d. C.', 'roma']),
    ph('Battle of the Milvian Bridge Raphael', at='puente Milvio'),
    ai('chi_rho_escudos', 'soldiers painting a Chi-Rho Christian symbol on their shields by firelight on the eve of battle, a river bridge in the distance, night', at='en los escudos'))
NAR("Un año después, el edicto de Milán garantiza la libertad de culto. Los cristianos pasan de perseguidos a protegidos. Y en el año trescientos treinta, Constantino inaugura una nueva capital en el estrecho del Bósforo, sobre la vieja ciudad griega de Bizancio. La llama Nueva Roma. El mundo la conocerá como Constantinopla.",
    ph('Hagia Sophia Istanbul', at='Constantinopla', lt=['Constantinopla', 'Hoy Estambul, Turquía']),
    cd(dict(type='map', title='Una nueva capital, 330 d. C.', bbox=[10, 35, 32, 46], points=[dict(name='Roma', lon=12.48, lat=41.89), dict(name='Constantinopla', lon=28.98, lat=41.01, big=1), dict(name='Milán', lon=9.19, lat=45.46)]), at='el estrecho del Bósforo'))
ESP("Hubo un último intento de volver atrás. El emperador Juliano, sobrino de Constantino, quiso restaurar los viejos dioses. Murió en el año trescientos sesenta y tres, en Persia, de una lanzada. Y la leyenda cristiana le atribuyó una última frase, mirando al cielo: «Has vencido, galileo».",
    ph('Julian the Apostate coin', at='Juliano', lt=['Juliano', 'Emperador · 361 – 363 d. C.', 'roma']),
    MITO('Juliano murió diciendo «Has vencido, galileo».', 'La frase aparece por primera vez en un historiador cristiano, Teodoreto, casi un siglo después. Los testigos de su muerte no la recogen.', at='Has vencido'))
NAR("El centro del poder se ha mudado al este, donde está la riqueza. En el año trescientos ochenta, el emperador Teodosio convierte el cristianismo en la religión oficial. Y cuando muere, en el trescientos noventa y cinco, el imperio queda repartido entre sus dos hijos. Oriente y Occidente. Ya nunca volverán a unirse.",
    ph('Missorium of Theodosius', at='Teodosio', lt=['Teodosio I', 'Emperador · 379 – 395 d. C. · nacido en Hispania', 'roma']),
    cd(dict(type='versus', title='395 d. C.: un imperio, dos cortes', left=dict(name='Occidente', color=RO, lines=['Honorio, desde Milán y Rávena', 'menos ciudades, menos impuestos', 'fronteras del Rin y el Danubio']), right=dict(name='Oriente', color=OR, lines=['Arcadio, desde Constantinopla', 'la mitad rica del imperio', 'durará otros mil años'])), at='Oriente y Occidente'))

# ---------------- X · LA CAÍDA QUE NADIE VIO ----------------
T('La caída que nadie vio', '395 – 476 d. C.', num='X', sting='tema')
B('tension')
NAR("Hay que matizar la palabra «invasiones». Muchos de esos pueblos, godos, vándalos, francos, no venían a destruir Roma. Venían huyendo de los hunos y querían entrar. Ser romanos. Tierras, dinero y cargos dentro del imperio.",
    MITO('Hordas de bárbaros arrasaron Roma de golpe.', 'Muchos pueblos germanos entraron huyendo de los hunos y pidiendo tierras. Lucharon para Roma, contra Roma y dentro de Roma durante más de un siglo.', at='Hay que matizar'),
    ai('godos_danubio', 'a huge crowd of Gothic families with wagons and cattle waiting on the bank of a wide river at dawn, Roman soldiers watching from the opposite shore', at='Venían huyendo'))
ESP("[serious] En el año trescientos setenta y ocho, los godos, maltratados por los funcionarios romanos que debían acogerlos, se rebelan. En Adrianópolis aplastan al ejército de Oriente. El emperador Valente muere en la batalla. Su cuerpo nunca apareció.",
    ai('adrianopolis', 'heavy cavalry charging out of a dust storm into a disordered Roman army on an open plain, burning wagons, wide shot', at='En Adrianópolis'))
NAR("Y el veinticuatro de agosto del año cuatrocientos diez, por primera vez en ochocientos años, un ejército enemigo entra en Roma. Son los visigodos de Alarico. Tres días de saqueo. La noticia sacudió el mundo. Desde Belén, san Jerónimo escribió:",
    ph('Sack of Rome by the Visigoths Sylvestre', at='los visigodos de Alarico', lt=['Alarico I', 'Rey de los visigodos', 'barbaros']),
    ph('Saint Jerome in his study Caravaggio', at='san Jerónimo'))
FUE("[softly] La voz se me queda pegada a la garganta y los sollozos me cortan las palabras mientras dicto. La ciudad que conquistó el mundo entero... ha sido conquistada.",
    PAP('La ciudad que conquistó el mundo entero ha sido conquistada.', 'San Jerónimo', 'Carta 127 · 412 d. C.', at='La voz se me queda'))
ESP("[softly] ¿Y el emperador de Occidente, Honorio? Estaba a salvo en Rávena. El historiador Procopio cuenta, más de un siglo después, una anécdota que seguramente es falsa pero que lo dice todo. Un criado le anuncia: «Roma ha perecido». Honorio se horroriza... porque tenía un gallo favorito que se llamaba Roma. Cuando le aclaran que es la ciudad, respira aliviado.",
    ph('The Favourites of the Emperor Honorius Waterhouse', at='Honorio', lt=['Honorio', 'Emperador de Occidente · 395 – 423 d. C.', 'roma']),
    MITO('El emperador Honorio confundió la caída de Roma con la muerte de su gallo.', 'Lo cuenta Procopio más de un siglo después y casi seguro es una leyenda. Pero retrata bien a un emperador encerrado en Rávena mientras Occidente se hundía.', fuente='Procopio, Historia de las guerras, III, 2', at='un gallo favorito'))
NAR("A partir de ahí, el Occidente romano se deshace por piezas. Los visigodos se instalan en Hispania y en el sur de la Galia. Los vándalos toman el norte de África, el granero de Roma. Britania queda abandonada.",
    cd(dict(type='list', header='Occidente, pieza a pieza', items=['Britania · abandonada hacia el 410', 'Hispania y sur de la Galia · visigodos', 'África · vándalos, 439', 'Galia del norte · francos']), at='se deshace por piezas'))
NAR("Y aquí entra en juego Hispania. El sucesor de Alarico, Ataúlfo, se casó en Narbona con una princesa romana, Gala Placidia, hermana del emperador. Y según el historiador Orosio, Ataúlfo confesó que al principio había soñado con borrar el nombre de Roma.",
    ai('ataulfo_boda', 'a Gothic king in a fur-trimmed cloak and a Roman princess in imperial purple at a wedding feast in a Roman villa, guests in mixed Gothic and Roman dress, warm lamplight, faces in soft shadow', at='Gala Placidia'))
FUE("Quiso que Gothia sustituyera a Romania. Pero la experiencia le enseñó que los godos, por su barbarie indomable, no podían obedecer leyes. Y eligió buscar la gloria restaurando y engrandeciendo el nombre romano con las fuerzas de los godos.",
    PAP('Eligió buscar la gloria restaurando el nombre romano con las fuerzas de los godos.', 'Ataúlfo, según Orosio', 'Historias contra los paganos, VII, 43', at='Quiso que Gothia'))
NAR("Los visigodos acabaron fundando un reino con capital en Toledo. Hablaban latín, usaban el derecho romano y se consideraban herederos de Roma.",
    ph('Toledo Visigothic crown Guarrazar', at='Toledo', lt=['Corona votiva de Recesvinto', 'Tesoro de Guarrazar · Toledo, siglo VII']))
ESP("En el año cuatrocientos cincuenta y uno llega el más temido: Atila, rey de los hunos. Un ejército de romanos y godos, juntos, le frena en los Campos Cataláunicos, en la Galia. Al año siguiente invade Italia y el papa León sale a su encuentro. Atila se retira. Y un año después muere... en su noche de bodas.",
    ph('Attila the Hun Delacroix', at='Atila', lt=['Atila', 'Rey de los hunos · murió en 453', 'barbaros']),
    ph('Meeting of Leo the Great and Attila Raphael', at='el papa León'))
ESP("En el cuatrocientos cincuenta y cinco, los vándalos saquean Roma durante dos semanas. De ahí viene la palabra «vandalismo», aunque fue más un saqueo ordenado que una destrucción sin sentido. Los últimos emperadores de Occidente ya son marionetas de generales de origen germano.",
    ph('Genseric sacking Rome Bryullov', at='los vándalos saquean Roma'))
ESP("[serious] Septiembre del año cuatrocientos setenta y seis. Un general germano, Odoacro, depone al último emperador de Occidente, un adolescente. Su nombre es casi una broma de la historia: Rómulo Augústulo. El nombre del fundador de Roma... y el del primer emperador, en diminutivo.",
    ph('Romulus Augustulus solidus', at='Rómulo Augústulo', lt=['Rómulo Augústulo', 'Último emperador de Occidente · 475 – 476', 'roma']),
    K('ROMULUS AUGUSTULUS', 'Romulus Augustulus coin', at='casi una broma'))
NAR("Odoacro no se proclama emperador. Envía las insignias imperiales a Constantinopla con un mensaje: ya no hace falta un emperador en Occidente. Y al chico no lo mata. Le da una pensión y lo manda a vivir a una villa junto a Nápoles.",
    ai('insignias', 'a messenger presenting a purple imperial cloak and a diadem in a wooden chest to a court in a golden Byzantine hall, faces turned away, solemn', at='Envía las insignias'))
NAR("[pause] Y aquí está lo más extraño de todo. Casi nadie, en el año cuatrocientos setenta y seis, pensó que el mundo se acababa. Siguió habiendo senado, obispos, mercados y leyes romanas. El fin del Imperio romano de Occidente es una fecha que pusieron después los historiadores. La gente que lo vivió no lo vio.",
    MITO('Roma cayó en el año 476.', 'El 476 es una fecha simbólica: el Occidente llevaba décadas desmoronándose y nadie vivió ese año como el fin de nada. Y la mitad oriental del imperio siguió en pie mil años más.', at='lo más extraño de todo'))
NAR("¿Por qué cayó, entonces? Un historiador alemán, Alexander Demandt, reunió todas las causas que se han propuesto: más de doscientas. Desde las invasiones y los impuestos hasta el plomo de las cañerías o el exceso de baños calientes. En el siglo dieciocho, el inglés Edward Gibbon lo resumió en una frase célebre.",
    cd(dict(type='counter', to=210, label='causas propuestas para la caída de Roma, según Alexander Demandt (1984)'), at='más de doscientas'),
    ph('Edward Gibbon portrait Reynolds', at='Edward Gibbon', lt=['Edward Gibbon', 'Historia de la decadencia y caída del Imperio romano · 1776 – 1789']))
V('HIS', "[serious] La decadencia de Roma fue el efecto natural e inevitable de una grandeza desmedida. La prosperidad hizo madurar el principio de la decadencia. Y en cuanto el tiempo o el azar retiraron los apoyos artificiales, la estupenda construcción cedió bajo la presión de su propio peso.",
    PAP('La decadencia de Roma fue el efecto natural e inevitable de una grandeza desmedida. La prosperidad hizo madurar el principio de la decadencia.', 'Edward Gibbon', 'Decadencia y caída del Imperio romano, cap. 38', at='La decadencia'))

# ---------------- EPÍLOGO · ROMA NO HA MUERTO ----------------
T('Epílogo', 'Roma no ha muerto', secs=4.5, sting='tema')
B('tema')
ESP("[serious] Porque Roma, en realidad, no cayó en el cuatrocientos setenta y seis. La mitad oriental, con capital en Constantinopla, siguió en pie. Sus habitantes se llamaban a sí mismos «romanos». Nosotros los llamamos bizantinos.",
    ph('Theodosian Walls Istanbul', at='siguió en pie', lt=['Murallas de Teodosio', 'Estambul · hoy']))
NAR("Hasta el veintinueve de mayo de mil cuatrocientos cincuenta y tres. Ese día, los turcos otomanos del sultán Mehmed entran en Constantinopla. El último emperador, Constantino Paleólogo, muere luchando en las murallas. Habían pasado más de dos mil doscientos años desde aquellas cabañas en el Palatino.",
    ph('Fall of Constantinople Zonaro', at='entran en Constantinopla'),
    cd(dict(type='timeline', header='Más de veintidós siglos', events=[['753 a. C.', 'Fundación'], ['509 a. C.', 'República'], ['27 a. C.', 'Imperio'], ['476 d. C.', 'Fin de Occidente'], ['1453', 'Fin de Constantinopla']]), at='más de dos mil doscientos años'))
NAR("Y ni siquiera entonces murió del todo. Si hablas español, hablas una forma de latín, el que trajeron los legionarios a Hispania. Cuando dices «julio» o «agosto», nombras a Julio César y a Augusto. Muchas de nuestras leyes vienen del derecho romano. Nuestras carreteras siguen, a menudo, el trazado de sus calzadas.",
    ph('Aqueduct of Segovia', at='a Hispania', lt=['Acueducto de Segovia', 'Siglo I-II d. C. · hoy']),
    ph('Merida Roman theatre', at='del derecho romano', lt=['Teatro romano de Mérida', 'Augusta Emerita · hoy']),
    ph('Roman bridge Alcantara', at='sus calzadas', lt=['Puente de Alcántara', 'Cáceres · 104-106 d. C.']))
ESP("Y Roma le debe mucho a esta tierra. Hispanos fueron el filósofo Séneca, el poeta Marcial, el agrónomo Columela y tres emperadores: Trajano, Adriano y Teodosio. Hispania dio a Roma aceite, plata, soldados... y algunas de sus mejores cabezas.",
    ph('Seneca bust Cordoba', at='Séneca', lt=['Séneca', 'Filósofo · nacido en Córdoba hacia el 4 a. C.', 'roma']),
    ph('Rio Tinto Roman mine', at='plata'))
NAR("Polibio se preguntaba cómo una ciudad pudo conquistar el mundo. Quizá la respuesta es que no lo conquistó del todo. Lo convirtió en romano. Y por eso, dos mil años después, seguimos aquí, contando su historia.",
    ph('Pantheon Rome interior oculus', at='Lo convirtió en romano', lt=['Panteón de Agripa', 'Roma · 126 d. C., todavía en uso']),
    ph('Forum Romanum sunset', at='seguimos aquí'))
ESP("[dramatically] Porque Roma no cayó. Se convirtió en nosotros.",
    ai('legion_final', 'a lone Roman legionary standing on a hill at sunset looking over a modern European city in the distance, cinematic, seen from behind', at='Se convirtió en nosotros'))
