# -*- coding: utf-8 -*-
# «El Imperio Persa: la historia que 300 no te contó» · parte 1: apertura, capítulos I y II
from lib import *

# ---------------- APERTURA ----------------
B('batalla')
NAR("[serious] Termópilas, año cuatrocientos ochenta antes de Cristo. Trescientos espartanos frente a un ejército sin fin. Así lo cuenta la película 300: los persas son monstruos, esclavos con máscaras de metal, y su rey es un gigante cubierto de oro y cadenas. [short pause] Esta es la historia de esos monstruos. Contada, por una vez, desde el otro lado.",
    ph('Thermopylae pass Leonidas monument', at='Termópilas', lt=['Las Termópilas', 'Grecia · hoy']),
    ai('falange_carga', 'a phalanx of Greek hoplites with bronze shields clashing against a wave of Persian infantry in a narrow mountain pass by the sea, dust and spears, seen from behind the Greek line', at='Trescientos espartanos'),
    ai('ejercito_sin_fin', 'an immense Persian army stretching to the horizon across a plain at dawn, banners, cavalry and chariots, seen from a hilltop behind a lone rider', at='un ejército sin fin'),
    K('300', 'Persepolis Apadana relief soldiers', at='la película 300'),
    ph('Frieze of Archers Susa Louvre', at='Esta es la historia'))
NEW("Porque en Persépolis, la capital de esos monstruos, han aparecido decenas de miles de tablillas de barro. Son las cuentas del imperio. Y cuentan que los obreros cobraban un salario, que las mujeres podían dirigir talleres y que las que acababan de dar a luz recibían raciones extra.",
    ph('Persepolis ruins aerial view', at='en Persépolis', lt=['Persépolis', 'Irán']),
    ph('Persepolis Fortification tablet Elamite', at='tablillas de barro'),
    ai('obreros_paga', 'workers in a vast stone quarry at sunset lining up to receive measured jars of barley from a scribe holding a clay tablet, Persepolis under construction behind', at='cobraban un salario'),
    ai('madre_racion', 'a young mother holding a swaddled newborn receives a basket of grain and a jar of wine from a storehouse official, warm interior light, ancient Persia', at='acababan de dar a luz'))
NAR("[dramatically] Persia fue el imperio más grande que el mundo había visto. Del Danubio al río Indo. De Egipto a Asia Central. [short pause] Y casi todo lo que sabemos de él lo escribieron sus enemigos.",
    cd(dict(type='counter', to=5500000, label='kilómetros cuadrados: el imperio persa en su apogeo, hacia 500 a. C.'), at='el imperio más grande'),
    ph('Behistun inscription relief Darius', at='Del Danubio'),
    ph('Herodotus bust Metropolitan Museum', at='lo escribieron sus enemigos'))
NEW("[serious] ¿Quién era de verdad el rey que azotó el mar? ¿Por qué un pueblo de pastores de las montañas llegó a gobernar el mundo conocido? [pause] ¿Y por qué Alejandro Magno, después de quemar su capital, acabó vistiéndose como un persa?",
    ai('rey_olas', 'a lone royal figure in a purple cloak standing on a rocky headland facing a raging sea, shipwreck debris in the waves, lightning', at='azotó el mar'),
    ai('pastores_montes', 'nomadic herders with horses and sheep crossing a high mountain pass of the Zagros at dawn, snow peaks, ancient Iran', at='un pueblo de pastores'),
    ai('columnas_humo', 'towering stone columns of a palace standing black against a red night sky full of smoke and sparks, a young conqueror on horseback watching from below', at='quemar su capital'))
NAR("[serious] Esta es la otra versión. La de las tablillas, los cilindros y las piedras que los persas dejaron escritas. [short pause] La historia que 300 no te contó.",
    ph('Cyrus Cylinder British Museum', at='los cilindros'),
    ph('Naqsh-e Rostam tombs', at='las piedras'))
T('El Imperio Persa', 'La historia que 300 no te contó', secs=5.5, sting='tema', text='[dramatically] El Imperio Persa. La historia que trescientos no te contó.', chapter=False)

# ---------------- I · EL REY QUE ENTRÓ SIN LUCHAR ----------------
T('El rey que entró sin luchar', '559 – 530 a. C.', num='I', sting='tema')
B('tema')
NAR("Babilonia, octubre del año quinientos treinta y nueve antes de Cristo. La ciudad más rica del mundo tiene murallas tan anchas que, según los griegos, por encima podía pasar un carro de cuatro caballos. [short pause] Y aun así, esa noche cae.",
    ph('Ishtar Gate Pergamon Museum', at='Babilonia', lt=['Babilonia', 'Puerta de Ishtar · Museo de Pérgamo, Berlín']),
    ai('murallas_babilonia', 'the colossal walls of ancient Babylon at night lit by torches, a four-horse chariot driving along the top of the wall, the Euphrates below', at='murallas tan anchas'),
    ai('babilonia_cae', 'Persian soldiers wading through a lowered river into a sleeping city at night under the walls of Babylon, moonlight on the water', at='esa noche cae'))
HER("Ciro desvió el río hacia un lago y, cuando el agua bajó, sus hombres entraron por el cauce. Los babilonios estaban de fiesta, bailando, y los que vivían en el centro no se enteraron de que los extremos de la ciudad ya habían caído.",
    PAP('Los babilonios estaban de fiesta, bailando, y los que vivían en el centro no se enteraron de que los extremos de la ciudad ya habían caído.', 'Heródoto', 'Historias, I, 191', at='desvió el río'),
    ai('fiesta_babilonia', 'a lavish night banquet in a Babylonian palace hall, dancers and musicians, oil lamps, unaware guests while in the dark doorway armored soldiers appear', at='estaban de fiesta'))
NEW("Así lo cuenta Heródoto, el historiador griego que escribió casi un siglo después. Pero los propios babilonios dejaron otra versión, grabada en una tablilla que hoy está en el Museo Británico. Y es mucho más extraña.",
    ph('Herodotus bust Metropolitan Museum', at='Heródoto', lt=['Heródoto', 'Historiador griego · hacia 484 – 425 a. C.', 'griegos']),
    ph('Nabonidus Chronicle British Museum', at='grabada en una tablilla'))
PIE("El día dieciséis, Ugbaru, gobernador de Gutium, y el ejército de Ciro entraron en Babilonia sin combatir. [pause] Ciro entró en Babilonia. Ramas verdes se extendían ante él. La paz se impuso en la ciudad.",
    cd(dict(type='doc', title='Crónica de Nabonido', lines=['El ejército de Ciro entró en Babilonia sin combatir', 'Ramas verdes se extendían ante él', 'Octubre de 539 a. C.'], source='Tablilla babilonia · Museo Británico', hl='sin combatir'), at='El día dieciséis'),
    ai('ramas_verdes', 'crowds laying green palm branches on the street before a Persian king entering a Mesopotamian city on horseback, seen from behind, golden dust', at='Ramas verdes'))
NAR("[serious] Sin combatir. La ciudad más poderosa de la Tierra abrió las puertas a un extranjero. [short pause] Para entender por qué, hay que conocer al hombre que llegaba. Y al pueblo del que venía.",
    OTRA(['Un río desviado', 'Un asalto por sorpresa', 'Una ciudad borracha de fiesta'], ['Una entrada sin combate', 'Ramas verdes al paso del rey', 'La paz en la ciudad'], at='Sin combatir'))
NEW("Los persas eran entonces un pueblo menor. Pastores y jinetes de las montañas de Fars, en el suroeste del actual Irán, sometidos a un reino vecino más fuerte: el de los medos. Hacia el año quinientos cincuenta y nueve, su pequeño rey se llamaba Ciro.",
    cd(dict(type='map', title='Hacia 560 a. C.', bbox=[38, 24, 62, 40], points=[dict(name='Persia (Fars)', lon=53.0, lat=29.6, big=1), dict(name='Ecbatana, capital meda', lon=48.5, lat=34.8), dict(name='Babilonia', lon=44.4, lat=32.5), dict(name='Susa', lon=48.25, lat=32.19)]), at='las montañas de Fars'),
    ph('Zagros mountains Fars Iran', at='montañas de Fars'),
    ph('Pasargadae tomb of Cyrus', at='se llamaba Ciro', lt=['Ciro II el Grande', 'Rey de Persia · hacia 559 – 530 a. C.', 'persia']))
HER("Astiages, rey de los medos, soñó que de su nieta nacería una vid que cubriría toda Asia. Asustado, ordenó matar al niño nada más nacer. Pero el hombre encargado no se atrevió, y un pastor lo crió como si fuera suyo.",
    ai('sueno_vid', 'an old king asleep on a canopied bed while above him a giant golden vine grows and spreads over a painted map of mountains and rivers, dreamlike', at='soñó que'),
    ai('pastor_nino', 'a shepherd and his wife in a simple mountain hut holding a newborn baby wrapped in royal cloth, firelight, sheep outside', at='un pastor lo crió'))
NAR("[softly] Es una leyenda, claro: casi todos los fundadores de imperios tienen una parecida. Lo que sí es historia es lo que pasó en el año quinientos cincuenta. Ciro se rebeló contra su abuelo. Y el ejército de los medos, en mitad de la batalla, se pasó a su bando.",
    ai('ciro_rebelion', 'a young Persian king on a rearing horse leading horsemen across a plain while an opposing army lowers its spears and turns to join him, dust, sunset', at='Ciro se rebeló'),
    ph('Ecbatana Hamadan ruins', at='el ejército de los medos'))
NEW("[serious] Aquí aparece la primera idea que hizo grande a Persia. Ciro no arrasó Ecbatana, la capital meda. No mató a su abuelo. Lo mantuvo en su corte, y a los nobles medos les dio cargos en su gobierno. Los vencidos pasaron a ser socios.",
    ph('Ecbatana Hamadan ruins', at='Ecbatana'),
    ai('nobles_medos', 'Median and Persian noblemen in long robes and tall felt hats standing together in a royal audience hall, a king receiving them, warm lamplight', at='les dio cargos'))
NAR("Al oeste, en la actual Turquía, reinaba el hombre más rico de su tiempo: Creso de Lidia. Tan rico que su nombre todavía se usa como sinónimo de fortuna. Antes de atacar a Ciro, Creso preguntó al oráculo de Delfos qué pasaría.",
    ph('Sardis ruins temple of Artemis', at='en la actual Turquía', lt=['Sardes', 'Capital de Lidia · Turquía, hoy']),
    ph('Croeseid gold coin Lydia', at='el hombre más rico'),
    ph('Delphi temple of Apollo ruins', at='oráculo de Delfos'))
HER("Si Creso hace la guerra a los persas, destruirá un gran imperio.",
    PAP('Si Creso hace la guerra a los persas, destruirá un gran imperio.', 'Respuesta del oráculo de Delfos, según Heródoto', 'Historias, I, 53', at='Si Creso'))
NEW("[short pause] Creso lo entendió a su favor. Cruzó el río Halis, atacó... y el imperio que destruyó fue el suyo. En el año quinientos cuarenta y seis, Ciro tomó Sardes, su capital, en pleno invierno, cuando nadie hacía la guerra.",
    ai('sardes_invierno', 'Persian cavalry with camels charging through snow toward a hilltop citadel in winter, Lydian horses panicking at the camels, ancient Anatolia', at='en pleno invierno'),
    ph('Sardis acropolis', at='tomó Sardes'))
NAR("Heródoto cuenta que Ciro mandó quemar a Creso en una pira. Hay un vaso griego que lo pinta sentado en lo alto de la hoguera.",
    ph('Croesus on the pyre amphora Louvre', at='un vaso griego', lt=['Creso en la pira', 'Ánfora ática · hacia 500 a. C. · Louvre']),
    ai('creso_pira', 'a dethroned king sitting on top of a large wooden pyre about to be lit, soldiers with torches below, sudden rain clouds gathering, ancient Lydia', at='quemar a Creso'))
HER("En lo alto de la pira, Creso suspiró y gritó tres veces un nombre: «¡Solón!». Ciro quiso saber qué significaba. Y Creso le contó que aquel sabio de Atenas le había advertido que a ningún hombre se le puede llamar feliz hasta el día de su muerte. Ciro, pensando que él también era un hombre, mandó apagar el fuego.",
    PAP('A ningún hombre se le puede llamar feliz hasta el día de su muerte.', 'Solón a Creso, según Heródoto', 'Historias, I, 86', at='gritó tres veces'),
    ai('pira_lluvia', 'a burning pyre being doused by a sudden torrential rain, soldiers rushing to pull a king down from the flames, steam and smoke, dramatic sky', at='mandó apagar el fuego'))
NEW("[short pause] Sea verdad o no, Creso acabó como consejero del rey persa. Otra vez: el vencido, convertido en socio.",
    ph('Sardis acropolis', at='consejero del rey persa'))
NEW("Faltaba la gran presa: Babilonia. Su último rey, Nabonido, se había pasado diez años fuera, en un oasis de Arabia, y había molestado a los sacerdotes del dios Marduk. Cuando Ciro llegó, en el año quinientos treinta y nueve, muchos babilonios lo esperaban como a un libertador.",
    ph('Nabonidus stele British Museum', at='Nabonido', lt=['Nabonido', 'Último rey de Babilonia · 556 – 539 a. C.', 'otros']),
    ph('Tayma oasis Saudi Arabia', at='un oasis de Arabia'),
    ph('Ishtar Gate Pergamon Museum', at='como a un libertador'))
CIR("Yo soy Ciro, rey del universo, el gran rey, el rey poderoso, rey de Babilonia, rey de Sumer y Acad, rey de las cuatro partes del mundo. [pause] A los dioses que allí vivían los devolví a sus casas. Reuní a todos sus pueblos y les devolví sus moradas.",
    ph('Cyrus Cylinder British Museum', at='Yo soy Ciro', lt=['Cilindro de Ciro', '539 a. C. · Museo Británico']),
    PAP('Reuní a todos sus pueblos y les devolví sus moradas.', 'Ciro el Grande', 'Cilindro de Ciro · 539 a. C.', at='Reuní a todos'))
NEW("[serious] Es el Cilindro de Ciro, encontrado en las ruinas de Babilonia en el año mil ochocientos setenta y nueve. Una réplica está en la sede de la ONU, y en el siglo veinte se le llamó la primera declaración de derechos humanos de la historia.",
    ph('Cyrus Cylinder British Museum', at='encontrado en las ruinas'),
    ph('United Nations headquarters New York', at='la sede de la ONU'))
NAR("[short pause] Los historiadores no lo ven así. Irving Finkel, el experto del Museo Británico que lo ha traducido, lo resume en una frase: en la Antigüedad no existían los derechos humanos. Es propaganda. Un rey presumiendo de ser mejor que el anterior. [short pause] Pero es una propaganda que dice algo enorme: que el nuevo rey quería ganarse a los vencidos, no aplastarlos.",
    OTRA(['«Primera carta de derechos humanos»', 'Ciro, un rey santo'], ['Propaganda real babilonia', 'Un rey que devuelve dioses y pueblos', 'Y que quiere ganarse a los vencidos'], at='Los historiadores'))
NEW("Entre esos pueblos devueltos había uno pequeño, deportado a Babilonia medio siglo antes: los judíos. Ciro les dejó volver a Jerusalén y reconstruir su templo. Por eso la Biblia, que no tiene piedad con casi ningún rey extranjero, lo trata de un modo único.",
    ai('regreso_jerusalen', 'a long caravan of families with donkeys and carts walking through hills toward the ruined walls of Jerusalem at sunrise, seen from behind', at='volver a Jerusalén'),
    ph('Isaiah Scroll Dead Sea', at='la Biblia'))
HER("Así dice Jehová a su ungido, a Ciro, al cual tomé yo por su mano derecha, para sujetar gentes delante de él.",
    PAP('Así dice Jehová a su ungido, a Ciro, al cual tomé yo por su mano derecha, para sujetar gentes delante de él.', 'Libro de Isaías, 45, 1', 'Biblia · traducción Reina-Valera, 1909', at='Así dice Jehová'))
NAR("[serious] Su ungido. En hebreo, mesías. Es el único extranjero de toda la Biblia al que se le da ese nombre. [short pause] Y mientras tanto, Ciro seguía conquistando hacia el este, hasta Asia Central. Allí, en el año quinientos treinta, encontró por fin a alguien que no quiso ser su socio.",
    cd(dict(type='imperio', title='El imperio de Ciro', bbox=[20, 22, 75, 46], stages=[
        dict(year='550 a. C.', label='Persia y el reino medo', zona=[{'c': 'IRN', 'box': [44.0, 26.0, 61.0, 39.5]}]),
        dict(year='546 a. C.', label='Lidia y Asia Menor', zona=[{'c': 'IRN', 'box': [44.0, 26.0, 61.0, 39.5]}, 'TUR', 'ARM', 'AZE']),
        dict(year='539 a. C.', label='Babilonia, Siria y Palestina', zona=[{'c': 'IRN', 'box': [44.0, 26.0, 61.0, 39.5]}, 'TUR', 'ARM', 'AZE', 'IRQ', 'SYR', 'LBN', 'ISR', 'JOR', 'PSE']),
        dict(year='530 a. C.', label='Hasta Asia Central', zona=['IRN', 'TUR', 'ARM', 'AZE', 'IRQ', 'SYR', 'LBN', 'ISR', 'JOR', 'PSE', 'TKM', 'AFG', {'c': 'UZB', 'box': [56.0, 37.0, 68.0, 42.0]}])]), at='seguía conquistando'))
HER("Tomiris, reina de los masagetas, le advirtió: «Vuelve a tu reino. Y si no, te juro por el sol que te saciaré de sangre, por muy insaciable que seas».",
    ai('tomiris_jinetes', 'a warrior queen on horseback in scale armor at the head of a horde of steppe archers on a vast grassland, her back to the viewer, storm clouds', at='Tomiris'),
    PAP('Te juro por el sol que te saciaré de sangre, por muy insaciable que seas.', 'Tomiris, reina de los masagetas, según Heródoto', 'Historias, I, 212', at='te juro por el sol'))
ESP("[dramatically] Hubo batalla. La más feroz entre bárbaros, dice Heródoto. Primero, flechas. Después, lanzas y espadas, cuerpo a cuerpo, durante horas. Nadie quería huir. [short pause] Y cuando terminó, el ejército persa estaba deshecho. Y Ciro, el rey del universo, había muerto.",
    ai('batalla_masagetas', 'a ferocious battle on the steppe, Persian infantry and nomad horse archers locked in close combat, clouds of arrows, broken chariots, dust and blood-red sunset', at='Hubo batalla'),
    ai('ciro_caido', 'a fallen king lying on the battlefield among broken spears and a toppled standard, his golden armor catching the last light, horses running away, seen from a distance', at='había muerto'))
NEW("Heródoto añade que Tomiris metió su cabeza en un odre lleno de sangre. Otras fuentes antiguas cuentan una muerte distinta. [short pause] Lo seguro es que su cuerpo volvió a Persia y que su tumba sigue en pie en Pasargadas, la ciudad que fundó. Es una casa de piedra, sencilla, sobre seis escalones.",
    ph('Tomyris Rubens head of Cyrus painting', at='metió su cabeza'),
    ph('Pasargadae tomb of Cyrus', at='su tumba sigue en pie', lt=['Tumba de Ciro', 'Pasargadas, Irán']),
    ph('Pasargadae palace ruins', at='la ciudad que fundó'))
NAR("[serious] Ciro dejó el imperio más grande hasta entonces y una forma nueva de gobernar: respetar los dioses y las costumbres de cada pueblo, mientras paguen y obedezcan. [short pause] Pero dejó también dos hijos. [pause] Y uno de ellos iba a morir dos veces.",
    ph('Pasargadae tomb of Cyrus sunset', at='una forma nueva de gobernar'),
    ai('dos_hijos', 'two young princes in purple robes standing apart in a shadowy palace corridor, one glancing back at the other, tension, torchlight', at='dos hijos'))

# ---------------- II · EL HERMANO QUE VOLVIÓ DE LA TUMBA ----------------
T('El hermano que volvió de la tumba', '530 – 522 a. C.', num='II', sting='tema')
B('tension')
NEW("Pelusio, en la frontera de Egipto, año quinientos veinticinco antes de Cristo. El hijo mayor de Ciro, Cambises, se enfrenta al último faraón de la dinastía de Sais. [short pause] Y gana. Egipto, la civilización más antigua del mundo, pasa a ser una provincia persa.",
    cd(dict(type='map', title='525 a. C.: Cambises en Egipto', bbox=[24, 22, 40, 34], points=[dict(name='Pelusio', lon=32.57, lat=31.04, big=1), dict(name='Menfis', lon=31.25, lat=29.85), dict(name='Oasis de Siwa', lon=25.52, lat=29.2), dict(name='Tebas', lon=32.65, lat=25.7)]), at='Pelusio'),
    ai('pelusio_batalla', 'Persian and Egyptian armies clashing in the desert near the Nile delta, chariots and archers, palm trees, smoke, the sun low', at='Y gana'))
NAR("[softly] Siglos más tarde, un escritor griego contó que los persas ganaron gracias a los gatos: los pusieron delante de sus filas, y los egipcios, que los adoraban, no se atrevieron a disparar. [short pause] Es una anécdota estupenda. Y casi seguro inventada.",
    ai('gatos_escudos', 'Persian soldiers advancing in the desert with cats walking before their shields, Egyptian archers in the distance lowering their bows, absurd and solemn', at='gracias a los gatos'),
    ph('Bastet cat statue bronze Egyptian', at='que los adoraban'))
NEW("La leyenda negra de Cambises viene de Heródoto, que lo pinta como un loco: dice que se burló de los dioses de Egipto y que, con su daga, mató al toro sagrado Apis.",
    ph('Apis bull statue Serapeum Louvre', at='toro sagrado Apis'))
PIE("Pero en el Serapeo de Menfis, donde se enterraba a los toros sagrados, los arqueólogos encontraron la lápida de un Apis muerto en tiempos de Cambises. Fue enterrado con todos los honores. Y la lápida muestra al propio rey persa arrodillado ante él.",
    ph('Serapeum Saqqara Apis tomb', at='el Serapeo de Menfis', lt=['El Serapeo', 'Saqqara, Egipto']),
    ph('Apis stele Cambyses Louvre', at='la lápida de un Apis'),
    OTRA(['Cambises mató al toro sagrado', 'Un rey loco y sacrílego'], ['El Apis fue enterrado con honores', 'Cambises, arrodillado ante él'], at='arrodillado'))
NAR("[serious] Lo que sí parece cierto es el desastre del desierto. Cambises envió a cincuenta mil hombres contra el oasis de Siwa. A mitad de camino, mientras comían, se levantó una tormenta de arena. [pause] Nunca más se supo de ellos.",
    ph('Siwa oasis desert', at='el oasis de Siwa'),
    ai('ejercito_perdido', 'a long column of ancient soldiers swallowed by a gigantic wall of sand in the Sahara, the last banners disappearing in the storm, apocalyptic', at='una tormenta de arena'))
NEW("Los arqueólogos llevan más de un siglo buscando ese ejército perdido. Nadie lo ha encontrado. [short pause] Y mientras Cambises estaba en Egipto, en el año quinientos veintidós, le llegó desde Persia una noticia imposible. Su hermano pequeño, Bardiya, se había proclamado rey.",
    ai('mensajero_egipto', 'an exhausted messenger kneeling before a king in a tent in Egypt, the king rising in shock, dusty light, palm trees outside', at='una noticia imposible'))
NAR("[dramatically] Imposible, porque Bardiya estaba muerto. [short pause] Cambises lo había mandado matar en secreto años atrás. Eso, al menos, es lo que contaría después el siguiente rey. Cambises salió hacia Persia a toda prisa. Al montar, se hirió en el muslo con su propia espada. [pause] La herida se gangrenó, y murió en Siria.",
    ai('asesinato_secreto', 'two hooded men carrying a wrapped body out of a palace at night through a side gate, moonlight, ancient Persia', at='en secreto'),
    ai('herida_espada', 'a king mounting a horse in haste, his sword slipping from its sheath and cutting his thigh, soldiers rushing, dust', at='se hirió en el muslo'))
NEW("Durante siete meses, Persia tuvo un rey que se llamaba Bardiya, que decía ser hijo de Ciro, y al que el pueblo aceptaba encantado: perdonó los impuestos y el servicio militar durante tres años. [short pause] ¿Era el verdadero hermano? ¿O un impostor?",
    ai('rey_impostor', 'a young king on a throne seen from behind, receiving cheering crowds in a courtyard, scrolls of tax tablets being broken, ambiguous shadow over his face', at='un rey que se llamaba Bardiya'))
DAR("Dice Darío el rey: había un mago llamado Gaumata. Mintió al pueblo así: «Yo soy Bardiya, el hijo de Ciro». Entonces todo el pueblo se rebeló y se pasó a él. [short pause] No había nadie, ni persa ni medo, que se atreviera a quitarle el reino a ese Gaumata. Hasta que llegué yo.",
    ph('Behistun inscription relief Darius', at='Dice Darío el rey', lt=['Inscripción de Behistún', 'Darío I · hacia 520 a. C. · Irán']),
    ph('Behistun relief Gaumata under foot', at='un mago llamado Gaumata'))
NEW("Es la versión oficial. La que escribió Darío, un noble de una rama lejana de la familia real, que con otros seis conspiradores entró en la fortaleza donde estaba el rey y lo mató. [short pause] Heródoto cuenta incluso cómo eligieron, entre los siete, a quién le tocaba reinar.",
    ai('siete_conjurados', 'seven armed noblemen bursting into a fortress bedchamber at night with daggers drawn, a figure rising from the bed, torchlight and chaos', at='otros seis conspiradores'),
    ph('Darius the Great relief Persepolis treasury', at='La que escribió Darío', lt=['Darío I el Grande', 'Rey de Persia · 522 – 486 a. C.', 'persia']))
HER("Acordaron que sería rey aquel cuyo caballo relinchara primero al salir el sol. El mozo de cuadra de Darío, Ebares, la noche antes llevó allí a una yegua... y el caballo de Darío, al llegar al mismo sitio por la mañana, relinchó.",
    ai('caballo_relincha', 'six noblemen on horseback at dawn outside a city, one black stallion rearing and neighing, lightning in the sky, the others turning to look', at='al salir el sol'))
DAR("Dice Darío el rey: entonces yo, con unos pocos hombres, maté a ese Gaumata el mago y a sus principales seguidores. Le quité el reino. Por la gracia de Ahuramazda, me convertí en rey.",
    ph('Behistun relief Gaumata under foot', at='maté a ese Gaumata'))
NAR("[softly] Truco o leyenda, la mayoría de los historiadores de hoy sospecha otra cosa: que el muerto de aquella noche era el verdadero Bardiya. Que el impostor de esta historia no era Gaumata. [pause] Que el usurpador era el propio Darío.",
    OTRA(['El rey era un mago impostor', 'Darío salvó el trono de Ciro'], ['Solo tenemos la versión de Darío', 'Muchos historiadores sospechan', 'que mató al verdadero hermano'], at='la mayoría de los historiadores'))
ESP("[dramatically] Lo cierto es que el imperio no se lo creyó. Babilonia, Media, Elam, Armenia, incluso la propia Persia: todas se rebelaron. Durante un año entero, Darío corrió de una punta a otra del imperio, apagando incendios.",
    cd(dict(type='map', title='522 – 521 a. C.: el imperio en llamas', bbox=[36, 24, 66, 42], points=[dict(name='Babilonia', lon=44.4, lat=32.5), dict(name='Media', lon=48.5, lat=34.8), dict(name='Elam', lon=48.25, lat=32.19), dict(name='Armenia', lon=44.5, lat=40.1), dict(name='Persia', lon=53.0, lat=29.6), dict(name='Partia', lon=57.5, lat=36.5)]), at='todas se rebelaron'),
    ai('dario_campana', 'a Persian king in a war chariot racing at the head of cavalry across a burning plain, rebel city on fire in the distance, night sky glowing', at='apagando incendios'))
DAR("[serious] Dice Darío el rey: esto es lo que hice, por la gracia de Ahuramazda, en un mismo año desde que fui rey. Libré diecinueve batallas. Capturé a nueve reyes.",
    ph('Behistun relief Darius captive kings', at='capturé a nueve reyes'),
    cd(dict(type='counter', to=19, label='batallas en un solo año, según la inscripción de Behistún'), at='diecinueve batallas'))
NAR("[serious] Nueve reyes, atados por el cuello, uno detrás de otro. Así los mandó esculpir Darío, y debajo mandó escribir su versión de los hechos. En tres idiomas. [short pause] Y eligió un lugar donde nadie pudiera borrarla jamás: una pared de roca, a cien metros de altura.",
    ph('Behistun relief Darius captive kings', at='atados por el cuello'),
    ph('Behistun cliff Kermanshah', at='una pared de roca', lt=['Monte Behistún', 'Kermanshah, Irán']))
