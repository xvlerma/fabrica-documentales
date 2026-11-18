# -*- coding: utf-8 -*-
# Parte 2: capítulos 3 (las Puertas Calientes), recapitulación, 4 (dos días) y 5 (el sendero)
from lib import *

# ---------------- CAPÍTULO 3 · LAS PUERTAS CALIENTES ----------------
T('Las Puertas Calientes', 'Capítulo 3', sting='tema', chapter=True)
B('tension')
N("¿Por qué allí? Para bajar desde el norte hacia el centro de Grecia, un ejército grande tenía que pasar por un sitio concreto: una franja de tierra entre el monte Calídromo y el golfo Maliaco. Los griegos la llamaban Termópilas, las «Puertas Calientes», por los manantiales de agua caliente que brotan allí.",
  cd(dict(type='mapfly', title='Las Termópilas', keys=[[19, 36, 27, 41.5], [22.2, 38.6, 23.0, 39.0]], points=[dict(name='Termópilas', lon=22.56, lat=38.8, at=0.55, pulse=1, big=1), dict(name='Golfo Maliaco', lon=22.6, lat=38.88, at=0.7), dict(name='Monte Calídromo', lon=22.55, lat=38.74, at=0.75)]), at='un sitio concreto'),
  ph('Thermopylae hot springs', src='commons', at='las «Puertas Calientes»', lt=['Manantiales de las Termópilas', 'hoy']))
N("Hoy el paisaje engaña. Los ríos han arrastrado tanto sedimento en veinticinco siglos que el mar se ha retirado varios kilómetros, y donde estaba el paso hay una llanura con una autopista. Pero en el cuatrocientos ochenta el agua llegaba casi hasta la roca.",
  ph('Thermopylae plain highway today', src='commons', at='Hoy el paisaje engaña', lt=['Las Termópilas', 'hoy']),
  cd(dict(type='split', left=dict(title='480 a. C.', lines=['el mar casi tocaba la montaña', 'un camino de pocos metros']), right=dict(title='Hoy', lines=['una llanura de varios kilómetros', 'creada por los sedimentos']), strike=False), at='Pero en el cuatrocientos'))
N("[serious] Era el lugar perfecto para anular una ventaja numérica. Por mucho ejército que tengas, en un camino así solo pueden luchar a la vez unos pocos cientos de hombres. Y en ese tipo de lucha, cuerpo a cuerpo y en un frente estrecho, los griegos tenían algo que los persas no tenían.",
  ph('Thermopylae narrow pass Kallidromo slope', src='commons', at='el lugar perfecto'))
N("Los griegos levantaron de nuevo una vieja muralla que habían construido allí los focenses, sus vecinos, y acamparon tras ella. Y había una segunda pieza del plan: en el mar, a unos setenta kilómetros, la flota griega, con Atenas al frente, cerraba el estrecho de Artemisio para que los barcos persas no pudieran rodear el paso.",
  ai('wall', at='una vieja muralla'),
  cd(dict(type='mapfly', title='Tierra y mar', keys=[[21.5, 38.3, 24.2, 39.6], [22.0, 38.5, 23.8, 39.3]], points=[dict(name='Termópilas', lon=22.56, lat=38.8, at=0.3, pulse=1), dict(name='Artemisio', lon=23.25, lat=39.0, at=0.6, pulse=1, big=1)]), at='en el mar'))
N("Detrás de esa estrategia estaba un ateniense muy astuto, Temístocles. La idea era sencilla de decir y terrible de cumplir: aguantar en tierra y en el mar a la vez, todo el tiempo que hiciera falta.",
  ph('Themistocles bust Ostia', src='commons', at='Temístocles', lt=['Temístocles', 'General de Atenas', 'griegos']),
  ph('Greek trireme Olympias', src='commons', at='en el mar a la vez', lt=['Olympias', 'réplica moderna de un trirreme · hoy']))
N("[serious] El mar, además, ayudó a los griegos antes incluso de empezar. La flota persa fondeó frente a la costa de Magnesia, junto al cabo Sepias, en una playa demasiado pequeña para tantos barcos. Tuvieron que quedarse anclados en filas, mar adentro. Y entonces se levantó un temporal que duró tres días.",
  cd(dict(type='mapfly', title='El cabo Sepias', keys=[[21.5, 38.3, 24.5, 40.0], [22.8, 38.9, 23.6, 39.5]], points=[dict(name='Cabo Sepias', lon=23.2, lat=39.15, at=0.4, pulse=1, big=1), dict(name='Artemisio', lon=23.25, lat=39.0, at=0.7)]), at='junto al cabo Sepias'),
  ph('stormy sea Aegean rocks coast', src='commons', at='se levantó un temporal'))
N("Según Heródoto, se hundieron al menos cuatrocientos barcos de guerra, además de incontables naves de carga. Los vecinos de la costa estuvieron años recogiendo oro, plata y copas de los naufragios. Los griegos, que habían rezado al viento del norte, lo tuvieron claro: los dioses estaban de su parte.",
  cd(dict(type='counter', to=400, label='barcos persas hundidos por el temporal, según Heródoto'), at='al menos cuatrocientos'),
  ph('ancient Greek gold cup phiale', src='met,cleveland', at='oro, plata y copas'),
  ph('Boreas north wind vase', src='met,cleveland,commons', at='al viento del norte', lt=['Bóreas', 'el viento del norte']))
N("Cuando vieron llegar al ejército persa, muchos griegos quisieron retirarse. Los del Peloponeso proponían volver al istmo de Corinto y defender solo su península. Los focenses y los locrios, que vivían justo detrás del paso, se indignaron. Leónidas decidió quedarse y pedir refuerzos a las ciudades.",
  ph('Greek hoplites assembly vase', src='met,cleveland', at='muchos griegos quisieron'),
  ph('Isthmus of Corinth', src='commons', at='el istmo de Corinto', lt=['Istmo de Corinto', 'hoy']))
N("Jerjes acampó al otro lado y envió a un jinete a espiar. Lo que el explorador vio le pareció tan raro que volvió a contarlo con todo detalle.",
  ph('Persian horseman relief', src='commons,met', at='envió a un jinete'))
R('HER', "«Vio que unos hacían ejercicio desnudos y que otros se peinaban la melena. Se quedó mirándolos asombrado y contó cuántos eran. Nadie lo persiguió. Nadie le hizo el menor caso.»",
  ph('Greek athletes exercising vase', src='met,cleveland', at='hacían ejercicio'),
  cd(dict(type='quote', text='Unos hacían ejercicio y otros se peinaban la melena.', attrib='Heródoto, Historia VII, 208 · lectura', commons=IMG['herodoto']), at='Nadie lo persiguió'))
N("Jerjes no entendía nada. Así que llamó al único hombre de su campamento que podía explicárselo: el espartano exiliado, Demarato.",
  ph('Persepolis king audience relief', src='commons', at='Jerjes no entendía'),
  ph('Achaemenid nobles relief Persepolis', src='commons', at='Demarato', lt=['Demarato', 'Rey espartano exiliado', 'persas']))
R('DEM', "«Esos hombres han venido a luchar por el paso, y se están preparando para ello. Tienen esa costumbre: cuando van a jugarse la vida, se arreglan el pelo. Si vences a estos y a los que se han quedado en Esparta, no habrá ningún otro pueblo que se atreva a levantar la mano contra ti.»",
  cd(dict(type='quote', text='Cuando van a jugarse la vida, se arreglan el pelo.', attrib='Demarato a Jerjes, según Heródoto, Historia VII, 209'), at='Tienen esa costumbre'))
N("[short pause] Jerjes no le creyó. Pensó que un puñado de hombres no podía estar pensando en serio en combatir contra un ejército así. Y esperó. Cuatro días, cuenta Heródoto, esperando a que los griegos se dieran cuenta de su locura y salieran corriendo.",
  cd(dict(type='counter', to=4, label='días de espera de Jerjes'), at='Cuatro días'))
N("De esos días de espera vienen las dos frases más famosas de la batalla. La primera la cuenta Plutarco: Jerjes habría mandado decir a Leónidas que entregara las armas. Y Leónidas habría contestado con dos palabras en griego, «Molón labé».",
  ph('Greek hoplite shield spear vase', src='met,cleveland', at='entregara las armas'))
R('LEO', "«Venid a cogerlas.»",
  cd(dict(type='quote', text='Venid a cogerlas.', attrib='Leónidas, según Plutarco, Dichos de espartanos 225c'), at='Venid'))
N("[serious] Es una frase perfecta. Demasiado perfecta, quizá: Heródoto, que escribió mucho más cerca de los hechos, no la menciona. La segunda, en cambio, sí la cuenta él. Un hombre de Traquis, la ciudad de al lado, avisó a los griegos de que los persas eran tantos que, cuando disparaban sus flechas, tapaban el sol. Un espartano llamado Dieneces le respondió sin inmutarse.",
  cd(dict(type='split', left=dict(title='«Venid a cogerlas»', lines=['Plutarco', 'casi seis siglos después']), right=dict(title='«Lucharemos a la sombra»', lines=['Heródoto', 'unos cuarenta años después']), strike=False), at='Demasiado perfecta'),
  ph('Persian archers Susa frieze glazed', src='commons', at='cuando disparaban sus flechas'))
R('DIE', "«Buenas noticias nos trae este extranjero. Si los medos tapan el sol, lucharemos a la sombra.»",
  cd(dict(type='quote', text='Si los medos tapan el sol, lucharemos a la sombra.', attrib='Dieneces, según Heródoto, Historia VII, 226'), at='lucharemos'))
N("Heródoto dice que Dieneces fue el más valiente de todos. Y que esa frase, y otras parecidas, fueron lo que dejó como recuerdo de sí mismo. [pause] Al quinto día, Jerjes se cansó de esperar.",
  ph('Greek warrior helmet profile vase', src='met,cleveland', at='el más valiente'),
  ph('Achaemenid king relief Persepolis throne', src='commons', at='Al quinto día', tr='black'))
M('tension', 10)
R('NAR', "Hasta aquí: Jerjes ha entrado en Grecia con el ejército más grande de su tiempo. Unos siete mil griegos, con Leónidas y sus trescientos espartanos al frente, cierran el paso de las Termópilas, mientras la flota griega bloquea el mar en Artemisio. Y el Gran Rey, tras cuatro días de espera, va a atacar.",
  cd(dict(type='recap', title='Hasta aquí', items=[['Jerjes', 'invade Grecia con 120.000-300.000 hombres'], ['Leónidas', 'cierra las Termópilas con unos 7.000 griegos'], ['La flota griega', 'bloquea el mar en Artemisio'], ['Día 5', 'Jerjes se cansa de esperar']]), at='Hasta aquí'))

# ---------------- CAPÍTULO 4 · EL MURO DE BRONCE ----------------
T('El muro de bronce', 'Capítulo 4', sting='tema', chapter=True)
B('batalla')
N("[serious] Primer día de combate. Jerjes manda por delante a los medos y a los cisios, pueblos del corazón del imperio, con una orden: traer a los griegos vivos ante él. Avanzan por el camino estrecho, cientos y luego miles. Y se encuentran con algo que no habían visto nunca.",
  ph('Median soldier Persepolis relief', src='commons', at='los medos', lt=['Medos y cisios', 'Infantería del imperio', 'persas']),
  ph('Persian infantry relief', src='commons', at='Avanzan por el camino'))
N("Delante de ellos hay una pared. Hoplitas: soldados de a pie con armadura pesada. Casco de bronce, coraza, grebas en las piernas y un escudo redondo enorme, de casi un metro, el hoplon, que les cubría desde la barbilla hasta los muslos. Y una lanza de más de dos metros.",
  ph('Corinthian helmet bronze', src='met,cleveland', at='Casco de bronce'),
  ph('hoplite armor greaves bronze', src='met,cleveland', at='grebas'),
  ph('hoplite shield aspis vase', src='met,cleveland', at='un escudo redondo'))
N("Formaban en falange: filas apretadas, hombro con hombro, cada escudo cubriendo también el costado del compañero. Desde fuera parecía un muro de bronce erizado de lanzas. Para romperlo había que acercarse. Y acercarse era morir.",
  ph('phalanx hoplites vase Chigi', src='commons,met', at='Formaban en falange'),
  cd(dict(type='list', header='La falange', items=[['Escudo', 'protege al soldado y al compañero de la izquierda'], ['Lanza', 'más de dos metros; golpean varias filas a la vez'], ['Filas', 'los de atrás empujan y relevan a los de delante']]), at='cada escudo'),
  K('UN MURO DE BRONCE', 'hoplite phalanx black-figure', at='un muro de bronce'))
N("Los persas luchaban de otra manera. Su fuerza eran los arqueros y la caballería en campo abierto. Llevaban lanzas más cortas, escudos de mimbre y poca armadura. En una llanura habrían envuelto a los griegos. En aquel pasillo de roca, chocaban de frente contra la pared.",
  ph('Persian soldier wicker shield vase', src='met,cleveland,commons', at='Los persas luchaban'),
  ph('Greek hoplite fighting Persian kylix', src='met,cleveland', at='chocaban de frente'))
R('HER', "«Cayeron muchos, pero otros ocupaban su lugar. Y dejaron claro a todo el mundo, y sobre todo al propio rey, que eran muchos los seres humanos, pero pocos los hombres.»",
  cd(dict(type='quote', text='Eran muchos los seres humanos, pero pocos los hombres.', attrib='Heródoto, Historia VII, 210 · lectura', commons=IMG['herodoto']), at='Cayeron muchos'))
N("Cuando los medos se retiraron, destrozados, Jerjes mandó a los mejores: los Inmortales, su guardia de élite. Eran diez mil, y se llamaban así porque, según Heródoto, cuando uno caía otro ocupaba enseguida su puesto, de modo que siempre eran diez mil. Los mandaba un general llamado Hidarnes.",
  ph('Immortals frieze of archers Susa Louvre', src='commons', at='los Inmortales', lt=['Los Inmortales', 'Guardia del rey · relieve de Susa', 'persas']),
  cd(dict(type='counter', to=10000, label='Inmortales: siempre el mismo número'), at='Eran diez mil'),
  ph('Achaemenid guard relief spear', src='commons', at='Hidarnes', lt=['Hidarnes', 'Jefe de los Inmortales', 'persas']))
N("Los relieves de los palacios persas nos los muestran todavía hoy: hombres altos, de túnicas bordadas, con lanzas rematadas en granadas de plata y oro. Eran la imagen misma del poder del Gran Rey.",
  ph('Susa archers glazed brick frieze detail', src='commons', at='Los relieves'),
  ph('Persepolis guards spears relief', src='commons', at='granadas de plata'))
N("[serious] Les fue igual que a los medos. Sus lanzas eran más cortas que las griegas, y el número no servía de nada en un frente de pocos metros. Los espartanos, además, tenían un truco. De pronto daban la espalda, como si huyeran. Los persas se lanzaban a perseguirlos gritando, perdían la formación… y entonces los espartanos se giraban todos a la vez y caían sobre ellos.",
  ph('Greek hoplites running vase', src='met,cleveland', at='daban la espalda'),
  ai('feigned', at='se giraban todos'))
N("Los griegos, además, luchaban por turnos, ciudad por ciudad, para que los cansados pudieran descansar. Solo los focenses no entraban en las rotaciones. Leónidas los había mandado a vigilar algo en la montaña. Volveremos a ello.",
  ph('Greek hoplites resting vase', src='met,cleveland', at='luchaban por turnos'),
  ph('Kallidromo mountain forest Greece', src='commons', at='vigilar algo en la montaña'))
N("Desde una altura, sentado en su trono, Jerjes miraba. Y Heródoto nos deja uno de los detalles más humanos de toda su historia.",
  ph('Xerxes throne relief Persepolis Treasury', src='commons', at='sentado en su trono'))
R('HER', "«Se cuenta que, durante aquellos asaltos, el rey, que estaba mirando, saltó tres veces de su trono, temiendo por su ejército.»",
  cd(dict(type='quote', text='El rey saltó tres veces de su trono, temiendo por su ejército.', attrib='Heródoto, Historia VII, 212 · lectura', commons=IMG['herodoto']), at='saltó tres veces'))
N("[pause] El segundo día fue igual. Los persas atacaron pensando que los griegos, pocos y heridos, ya no podrían ni levantar el escudo. Se equivocaban. Al caer la tarde volvieron a retirarse.",
  ph('Greek warrior wounded vase', src='met,cleveland', at='El segundo día'))
N("¿Cómo era aquello por dentro? Hay que imaginar el ruido. El golpe de miles de escudos chocando. Los gritos en una decena de lenguas distintas. El calor de agosto dentro de un casco de bronce cerrado, que apenas dejaba ver y oír. Y el polvo, levantado por decenas de miles de pies, que no dejaba ver más allá de unos metros.",
  ph('Corinthian helmet bronze front', src='met,cleveland', at='dentro de un casco de bronce'),
  ai('battle dust', at='Y el polvo'))
N("Un hoplita cargaba con más de veinte kilos de armadura. Se luchaba empujando con el escudo, buscando con la lanza el hueco del cuello, de la axila o de la ingle. Cuando la lanza se partía, se seguía con la espada corta o con la contera de hierro del otro extremo del asta. En las primeras filas, cada minuto era agotador. Por eso los relevos de Leónidas fueron tan importantes.",
  ph('hoplite fighting spear thrust vase', src='met,cleveland', at='Se luchaba empujando'),
  ph('Greek bronze spear butt sauroter', src='met,cleveland', at='la contera de hierro'))
N("[serious] Dos días. Las mejores tropas del mayor imperio del mundo no habían conseguido avanzar ni un paso. Y en el mar, en Artemisio, la flota persa tampoco lograba romper el bloqueo. Por primera vez desde que salió de Asia, Jerjes no sabía qué hacer.",
  ph('ancient Greek trireme vase ship', src='met,cleveland,commons', at='en el mar'),
  ph('Achaemenid king relief', src='commons', at='Jerjes no sabía'))
N("Mientras tanto, a pocos kilómetros, en el mar de Artemisio, se libraba la otra mitad de la batalla. Los trirremes griegos, unos doscientos setenta, se enfrentaron a la flota persa durante los mismos tres días. Las galeras chocaban con sus espolones de bronce, intentando partir el casco del enemigo. Nadie ganó claramente. Pero los persas no consiguieron pasar.",
  ph('Greek trireme ram bronze', src='met,commons', at='los trirremes griegos'),
  cd(dict(type='counter', to=271, label='trirremes griegos en Artemisio, según Heródoto'), at='unos doscientos setenta'),
  ph('Artemision Euboea coast', src='commons', at='Artemisio', lt=['Cabo Artemisio', 'Eubea · hoy']))
N("Entonces alguien pidió verle.",
  ph('Greek shepherd figurine', src='met,cleveland,commons', at='Entonces', tr='black'))
M('batalla', 10)

# ---------------- CAPÍTULO 5 · EL SENDERO ----------------
T('El sendero', 'Capítulo 5', sting='tema', chapter=True)
B('noche')
N("Se llamaba Efialtes, hijo de Euridemo. Era de la Málide, la comarca de alrededor del paso. Y le ofreció a Jerjes lo que más necesitaba: un camino.",
  ai('shepherd', at='Se llamaba Efialtes', lt=['Efialtes', 'Recreación', 'persas']))
N("Por detrás de las Termópilas, a través del monte, corría un sendero de pastores. Subía por el valle de un río, cruzaba la montaña por un bosque de robles y bajaba justo a la espalda de los griegos. Los de la zona lo llamaban Anopea.",
  cd(dict(type='mapfly', title='El sendero de Anopea', keys=[[22.2, 38.6, 23.0, 39.0], [22.4, 38.7, 22.75, 38.86]], points=[dict(name='Campamento persa', lon=22.47, lat=38.8, at=0.2), dict(name='Anopea', lon=22.56, lat=38.75, at=0.5, pulse=1, big=1), dict(name='Alpenos', lon=22.62, lat=38.81, at=0.8)]), at='corría un sendero'),
  ph('Anopaea path Kallidromo oak forest', src='commons', at='un bosque de robles'),
  ph('Kallidromo mountain path', src='commons', at='Anopea', lt=['Monte Calídromo', 'el sendero de Anopea · hoy']))
N("Leónidas lo conocía. Por eso había mandado allí arriba a los mil focenses: para cerrar esa puerta trasera. Pero un sendero de noche, en un bosque, con mil hombres que no esperan a nadie, es una puerta muy fácil de abrir.",
  ph('Greek hoplite guard vase', src='met,cleveland', at='a los mil focenses', lt=['Los focenses', '1.000 hoplitas en el sendero', 'griegos']))
N("Jerjes no se lo pensó. Esa misma tarde, a la hora en que se encienden las lámparas, Hidarnes y sus Inmortales salieron del campamento con Efialtes como guía. Caminaron toda la noche.",
  ph('ancient Greek oil lamp terracotta', src='met,cleveland', at='se encienden las lámparas'),
  ai('night march', at='Caminaron toda la noche'))
R('HER', "«Al amanecer estaban ya en lo alto del monte. Había un gran silencio, y las hojas de los robles cubrían el suelo. Cuando los persas subían, se oía un enorme ruido de hojas pisadas. Los focenses se pusieron en pie de un salto.»",
  ai('oak leaves', at='las hojas de los robles'),
  cd(dict(type='quote', text='Se oía un enorme ruido de hojas pisadas.', attrib='Heródoto, Historia VII, 218 · lectura', commons=IMG['herodoto']), at='ruido de hojas'))
N("[serious] Los focenses, sorprendidos, pensaron que el ataque iba contra ellos. Así que se retiraron a la cumbre para morir allí con honor. Pero los persas, bajo una lluvia de flechas, ni se pararon. No les interesaban los focenses. Siguieron bajando por el otro lado.",
  ph('Greek hoplites hilltop defensive', src='met,cleveland', at='se retiraron a la cumbre'),
  ai('descent', at='Siguieron bajando'))
N("Había sido una marcha brutal. Una columna de miles de hombres, de noche, por un camino de pastores, subiendo y bajando más de mil metros de desnivel por un monte que no conocían. Sin luces que los delataran. Siguiendo a un desconocido que podía estar llevándoles a una emboscada. Al amanecer, estaban sobre la espalda de los griegos.",
  ph('Kallidromo mountain night', src='commons', at='Había sido una marcha'),
  ai('descent', at='Al amanecer'))
N("[pause] La puerta trasera estaba abierta.",
  ph('Thermopylae dawn mountains', src='commons', at='La puerta trasera', tr='black'))
N("[serious] Durante siglos, el nombre de Efialtes ha sido sinónimo de traidor. En griego moderno, la palabra se usa también para «pesadilla». Pero ¿hasta qué punto fue él quien decidió la batalla?",
  K('EFIALTES', 'Kallidromo mountain path', at='sinónimo de traidor'))
N("Heródoto cuenta que había otras versiones, que señalaban a otros dos hombres de la zona. Él se queda con Efialtes porque los griegos pusieron precio a su cabeza. Efialtes huyó a Tesalia y años después, al volver, lo mató otro hombre de Traquis, aunque, según Heródoto, por otro motivo.",
  D('Lo que dice Heródoto de Efialtes', 'herodoto_ms', text='Huyó a Tesalia. La Anfictionía puso precio a su cabeza. Lo mató Atenades de Traquis, por otro motivo.', source='Heródoto, Historia VII, 213-214', at='había otras versiones'))
N("Muchos historiadores de hoy creen que el traidor importa menos de lo que parece. Un ejército como el persa tenía exploradores, aliados griegos del norte y guías locales de sobra. Que existiera un sendero por la montaña no era ningún secreto en la comarca. Tarde o temprano, alguien se lo habría enseñado.",
  cd(dict(type='split', left=dict(title='La versión clásica', lines=['un traidor revela', 'un camino secreto']), right=dict(title='La visión de muchos historiadores', lines=['el sendero era conocido', 'los persas tenían guías y exploradores']), strike=False), at='Muchos historiadores'))
N("[softly] Y queda otra pregunta incómoda: por qué los mil focenses no aguantaron. Heródoto habla de sorpresa. Algunos estudios recientes sugieren causas más turbias, ligadas a rivalidades locales. No lo sabemos. Lo que sí sabemos es lo que ocurrió después.",
  ph('Phocis mountains Greece', src='commons', at='los mil focenses'))
M('noche', 10)
