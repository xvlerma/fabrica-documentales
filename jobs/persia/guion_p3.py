# -*- coding: utf-8 -*-
# «El Imperio Persa: la historia que 300 no te contó» · parte 3: capítulos VI a IX y cierre
from lib import *

NEW("[serious] Recapitulemos, antes de cruzar al otro lado del mito. Ciro fundó el imperio ganándose a los vencidos. Darío lo organizó con provincias, caminos y moneda. Y Jerjes cruzó a Europa, ganó en las Termópilas y perdió en Salamina. [short pause] Ahora toca mirar dentro. A los soldados, a la corte y a los mitos.",
    cd(dict(type='recap', title='Hasta aquí', items=[['550 a. C.', 'Ciro funda el imperio'], ['522 a. C.', 'Darío lo organiza'], ['480 a. C.', 'Termópilas y Salamina'], ['465 a. C.', 'Jerjes, asesinado']]), at='Recapitulemos'))

# ---------------- VI · LOS INMORTALES ----------------
T('Los Inmortales', 'Y otros mitos', num='VI', sting='tema')
B('maravilla')
NEW("Susa, en el suroeste de Irán, año mil ochocientos ochenta y cinco. Una pareja de arqueólogos franceses, Marcel y Jane Dieulafoy, encuentra entre las ruinas del palacio de Darío miles de ladrillos vidriados de colores. Al montarlos, aparece un desfile de soldados a tamaño casi natural.",
    ph('Susa archaeological site', at='Susa', lt=['Susa', 'Irán']),
    ph('Jane Dieulafoy portrait', at='Marcel y Jane Dieulafoy', lt=['Jane Dieulafoy', 'Arqueóloga francesa · 1851 – 1916', 'otros']),
    ph('Frieze of Archers Susa Louvre', at='un desfile de soldados'))
NAR("[serious] Hoy está en el Louvre: el friso de los arqueros. Túnicas bordadas, lanzas con una granada en el extremo, el carcaj a la espalda, la barba rizada. [short pause] Es lo más parecido que tenemos a una foto de la guardia del rey persa. La que los griegos llamaron los Inmortales.",
    ph('Frieze of Archers Susa Louvre detail', at='el friso de los arqueros', lt=['Friso de los arqueros', 'Susa, hacia 510 a. C. · Louvre']),
    ph('Persepolis Apadana relief soldiers', at='la guardia del rey persa'))
HER("Eran diez mil, y se les llamaba Inmortales porque, si alguno moría o caía enfermo, otro ocupaba su lugar. Así nunca eran ni más ni menos de diez mil. Llevaban más oro encima que nadie y viajaban con sus mujeres y sus criados.",
    PAP('Si alguno moría o caía enfermo, otro ocupaba su lugar. Así nunca eran ni más ni menos de diez mil.', 'Heródoto, sobre los Inmortales', 'Historias, VII, 83', at='Eran diez mil'),
    ai('inmortales_desfile', 'ranks of elite Persian guardsmen in embroidered robes with spears and quivers marching through a palace gate in perfect formation, golden morning light', at='Llevaban más oro'))
NEW("En Trescientos, los Inmortales son monstruos sin rostro, con máscaras de metal y dientes afilados. [short pause] En las tablillas de Persépolis, en cambio, no aparecen por ningún lado con ese nombre. Y hay una teoría curiosa: que Heródoto, o quien le informó, entendió mal una palabra persa.",
    OTRA(['Monstruos enmascarados', 'Soldados sin rostro ni nombre'], ['Guardia de élite de la nobleza', 'Barba rizada, túnica bordada', 'Quizá ni se llamaban así'], at='monstruos sin rostro'),
    ph('Persepolis Fortification Archive', at='En las tablillas de Persépolis'))
NAR("[serious] En persa antiguo, anusiya significa compañeros, los del séquito del rey. Y anausa, casi igual, significa inmortales. [short pause] Es solo una hipótesis, y hay expertos que la rechazan. Pero sería una ironía perfecta: que el cuerpo militar más temido de la Antigüedad deba su nombre a un error de traducción.",
    cd(dict(type='split', left=dict(title='anusiya', lines=['«compañeros»', 'el séquito del rey']), right=dict(title='anausa', lines=['«inmortales»', 'lo que quizá entendieron los griegos']), strike=False), at='anusiya'))
HER("Suelen deliberar sobre los asuntos más serios estando borrachos. Al día siguiente, ya sobrios, el dueño de la casa donde deliberaron les vuelve a plantear lo decidido. Si sobrios les sigue pareciendo bien, lo hacen. Si no, lo dejan. Y lo que han decidido sobrios, lo vuelven a examinar borrachos.",
    ai('consejo_vino', 'Persian noblemen reclining on cushions around low tables with wine cups debating loudly at night, lamps, then the same hall at morning with sober faces, split mood', at='estando borrachos'))
NAR("[softly] Un sistema de doble control que más de un gobierno debería probar.",
    ph('Achaemenid gold rhyton', at='doble control'))
NEW("El otro gran mito es el del déspota oriental rodeado de esclavos. Las escaleras de la sala de audiencias de Persépolis cuentan otra historia: veintitrés pueblos del imperio subiendo en fila con regalos. Lidios con jarrones, indios con hachas y oro en polvo, etíopes con un colmillo de elefante, árabes con un dromedario.",
    ph('Apadana staircase delegations Persepolis', at='las escaleras de la sala de audiencias', lt=['Escalera de la Apadana', 'Persépolis']),
    ph('Persepolis Apadana relief Lydian delegation', at='Lidios con jarrones'),
    ph('Apadana Arabs', at='árabes con un dromedario'))
NAR("[serious] Y algo llama la atención: en esos relieves nadie lleva cadenas, nadie se arrodilla ante un látigo. Muchos van de la mano de un oficial persa o medo, que los guía hacia el rey. [short pause] Es propaganda, claro. Pero es la imagen que Persia quería dar de sí misma: un imperio de pueblos que se presentan juntos.",
    ph('Persepolis Apadana relief Persian Median guards', at='de la mano de un oficial persa'),
    ai('delegaciones_suben', 'colorful delegations of many nations in different costumes climbing a great stone staircase carrying gifts, vases, textiles, a camel and a horse, toward a columned hall, festive morning', at='un imperio de pueblos'))
HER("Los persas son, de todos los hombres, los que más adoptan las costumbres extranjeras. Visten el traje de los medos, porque lo consideran más bello que el suyo. Y para la guerra usan la coraza de los egipcios.",
    ph('Persepolis Apadana relief Persian Median guards', at='Visten el traje de los medos'))
NEW("Lo vemos también en el ejército. El general que conquistó Jonia para Persia era un medo. En Salamina, una de las capitanas de Jerjes era una reina caria. Y en Babilonia, el gobernador persa convivía con los sacerdotes de siempre, los mismos jueces y la misma lengua. [short pause] Mientras pagaran, cada pueblo seguía siendo él mismo.",
    ph('Babylon ruins Iraq', at='en Babilonia'),
    ai('escriba_babilonia', 'a Babylonian scribe writing cuneiform on a wet clay tablet beside a Persian official reading an Aramaic scroll, oil lamp, an archive room', at='la misma lengua'))
JER("Dice Jerjes el rey: entre estos países había un lugar donde antes se adoraba a los falsos dioses. Por la gracia de Ahuramazda destruí aquel santuario, y proclamé: los falsos dioses no serán adorados.",
    PAP('Destruí aquel santuario, y proclamé: los falsos dioses no serán adorados.', 'Jerjes I', 'Inscripción de los daivas · Persépolis', at='destruí aquel santuario'))
NAR("[dramatically] Pero que nadie se confunda: era un imperio. Tolerante mientras le convenía. Con impuestos duros, deportaciones de pueblos rebeldes y castigos atroces para los traidores. [short pause] La diferencia es que su arma favorita no fue la espada. [pause] Fue el oro.",
    ai('castigo_rebeldes', 'rebel prisoners in chains led away from a burned city by Persian soldiers, dark smoke, grim dusk, faces hidden', at='deportaciones de pueblos rebeldes'),
    ph('Oxus Treasure gold chariot British Museum', at='Fue el oro'))

# ---------------- VII · EL ORO DEL GRAN REY ----------------
T('El oro del Gran Rey', '479 – 336 a. C.', num='VII', sting='tema')
B('tension')
NEW("Tras la muerte de Jerjes, Persia dejó de mandar ejércitos a Grecia. Ya no le hacía falta. Los griegos se estaban matando entre ellos: Atenas contra Esparta, en una guerra que duró casi treinta años. [short pause] Y Persia descubrió que podía decidir quién la ganaba.",
    ai('griegos_guerra', 'Athenian and Spartan hoplites fighting each other among burning olive groves, a Persian envoy watching from a hill on horseback, smoke', at='Atenas contra Esparta'))
NAR("[serious] Al final de la guerra del Peloponeso, Esparta no tenía flota ni dinero para vencer a Atenas en el mar. Un joven príncipe persa, Ciro el Joven, le dio el oro para construirla y pagar a los remeros. [short pause] En el año cuatrocientos cuatro, Atenas se rindió. Los dáricos persas habían hecho lo que no lograron los Inmortales.",
    ph('Daric gold coin Achaemenid', at='le dio el oro'),
    ai('flota_oro', 'Spartan warships being built in a busy harbor, a Persian prince handing a heavy chest of gold coins to a Spartan admiral on the dock, sunset', at='pagar a los remeros'))
NEW("Ese mismo príncipe quiso después ser rey en lugar de su hermano. Contrató a diez mil mercenarios griegos y marchó hasta el corazón de Mesopotamia. En Cunaxa, cerca de Babilonia, en el año cuatrocientos uno, Ciro el Joven murió en la batalla.",
    ai('cunaxa_carga', 'a young Persian prince charging on horseback straight at the bodyguard of his brother the king in the middle of a huge battle on the Mesopotamian plain, dust and spears', at='En Cunaxa'))
GRI("Ciro, al ver al rey y la escolta que lo rodeaba, no pudo contenerse y gritó: «¡Lo veo!». Se lanzó contra él y le golpeó en el pecho, hiriéndolo a través de la coraza. Pero en ese momento alguien le clavó una jabalina bajo el ojo.",
    PAP('Ciro, al ver al rey, no pudo contenerse y gritó: «¡Lo veo!», y se lanzó contra él.', 'Jenofonte, testigo de la batalla', 'Anábasis, I, 8', at='Lo veo'))
NAR("[serious] Quien lo cuenta es Jenofonte, uno de aquellos diez mil griegos. Atrapados en mitad del imperio, sin jefe, cruzaron las montañas del Kurdistán y de Armenia en pleno invierno hasta llegar al mar Negro. [short pause] Su relato, la Anábasis, demostró a los griegos una cosa peligrosa: que se podía llegar al corazón de Persia. Y volver.",
    ph('Xenophon bust', at='Jenofonte', lt=['Jenofonte', 'Soldado e historiador ateniense · hacia 430 – 354 a. C.', 'griegos']),
    ai('diez_mil_nieve', 'a column of Greek mercenaries struggling through deep snow in high mountains, shields on their backs, wind and blizzard, exhausted men helping each other', at='en pleno invierno'),
    ai('thalatta', 'exhausted soldiers on a mountain ridge shouting and raising their arms at the first sight of the distant sea, a cairn of stones, golden light', at='hasta llegar al mar Negro'))
NEW("Aun así, quien mandaba seguía siendo el Gran Rey. En el año trescientos ochenta y siete, las ciudades griegas firmaron un tratado que se conoce con un nombre elocuente: la Paz del Rey. Las condiciones las dictó Artajerjes II desde Susa. [short pause] Un siglo después de Maratón, los griegos de Asia volvían a ser persas.",
    cd(dict(type='doc', title='La Paz del Rey · 387 a. C.', lines=['El rey Artajerjes considera justo', 'que las ciudades de Asia sean suyas', 'y que las demás ciudades griegas sean autónomas'], source='Texto del tratado, según Jenofonte, Helénicas, V, 1', hl='sean suyas'), at='la Paz del Rey'),
    ph('Artaxerxes II tomb Persepolis', at='Artajerjes II', lt=['Artajerjes II', 'Rey de Persia · 404 – 358 a. C.', 'persia']))
NEW("Heródoto cierra su libro con un consejo que pone en boca de Ciro el Grande, cuando los persas le pidieron dejar sus montañas pobres por tierras más ricas.",
    ph('Zagros mountains Fars Iran', at='sus montañas pobres'))
CIR("[serious] Las tierras blandas suelen criar hombres blandos. No es posible que una misma tierra dé frutos maravillosos y hombres valientes en la guerra.",
    PAP('Las tierras blandas suelen criar hombres blandos.', 'Ciro, según Heródoto', 'Historias, IX, 122', at='Las tierras blandas'))
NAR("[dramatically] Persia parecía eterna. Y sus reyes vivían en los palacios más ricos de la Tierra. [pause] Pero en el año trescientos cincuenta y seis, en Pela, la capital de un reino del norte de Grecia que los griegos consideraban casi bárbaro, nació un niño. [short pause] Su padre se llamaba Filipo de Macedonia. Al niño lo llamaron Alejandro.",
    ph('Pella', at='en Pela'),
    ph('Alexander the Great bust Acropolis Museum', at='Al niño lo llamaron Alejandro'))

# ---------------- VIII · ALEJANDRO ----------------
T('Alejandro', '336 – 330 a. C.', num='VIII', sting='batalla')
B('batalla')
NEW("En el año trescientos treinta y cuatro, Alejandro cruzó el Helesponto, el mismo estrecho que Jerjes había azotado ciento cincuenta años antes. Tenía veintidós años y un ejército de unos cuarenta mil hombres. [short pause] Su excusa era la venganza por los templos que quemó Jerjes.",
    ph('Dardanelles strait Canakkale', at='el mismo estrecho'),
    ph('Alexander the Great bust Acropolis Museum', at='Tenía veintidós años', lt=['Alejandro Magno', 'Rey de Macedonia · 356 – 323 a. C.', 'macedonia']))
ESP("[dramatically] En el Gránico, Alejandro cruza el río a caballo bajo una lluvia de flechas. Un noble persa le parte el casco de un hachazo. Otro levanta la espada para rematarlo. Y un oficial macedonio, Clito el Negro, le corta el brazo justo a tiempo.",
    ai('granico_cruce', 'a cavalry battle in a river, a young commander with a broken white-plumed helmet fighting Persian noblemen on horseback, one raising a sword behind him while another rider strikes first, water spray', at='le parte el casco'))
NAR("Enfrente tenía a Darío III, un rey que había llegado al trono tras una cadena de asesinatos en palacio. Valiente en la guerra, decían. [short pause] En el río Gránico, en Asia Menor, los sátrapas persas perdieron la primera batalla. Y en Isos, en el año trescientos treinta y tres, el propio Darío.",
    cd(dict(type='mapfly', title='La campaña de Alejandro, 334 – 330 a. C.', keys=[[20, 24, 60, 44], [26, 26, 58, 40]],
        points=[dict(name='Gránico', lon=27.4, lat=40.2, at=0.1), dict(name='Isos', lon=36.2, lat=36.85, at=0.3), dict(name='Gaugamela', lon=43.5, lat=36.36, at=0.6), dict(name='Babilonia', lon=44.4, lat=32.5, at=0.7), dict(name='Persépolis', lon=52.89, lat=29.93, at=0.9)],
        arrows=[dict(path=[[26.4, 40.15], [27.4, 40.2], [30.5, 37.9], [34.0, 36.9], [36.2, 36.85], [38.5, 36.6], [43.5, 36.36], [44.4, 32.5], [48.25, 32.19], [52.89, 29.93]], color=MA, at=0.15, dur=3.5)]), at='En el río Gránico'),
    ph('Alexander Mosaic Darius III Naples', at='Darío III', lt=['Darío III', 'Rey de Persia · 336 – 330 a. C.', 'persia']))
ESP("[dramatically] En Isos, Alejandro cargó directamente contra el carro del rey. Darío dio la vuelta y huyó. Dejó atrás su arco, su escudo, su manto. [pause] Y a su madre, a su esposa y a sus hijas.",
    ph('Alexander Mosaic Naples', at='En Isos', lt=['Mosaico de Alejandro', 'Pompeya · hacia 100 a. C. · Nápoles']),
    ai('carga_isos', 'a young cavalry commander on a black horse charging through a mass of soldiers straight toward a royal war chariot that turns to flee, spears and dust, epic battle', at='contra el carro del rey'))
HER("Al entrar en la tienda, Sisigambis se arrodilló ante Hefestión, el amigo de Alejandro, porque era más alto y lo confundió con el rey. Al darse cuenta, quiso morirse de vergüenza. Y Alejandro la levantó.",
    ai('hefestion_error', 'an elderly queen kneeling by mistake before a tall officer in a tent while a younger man beside him smiles and reaches out to lift her, attendants gasping', at='lo confundió con el rey'))
ALE("[softly] No te has equivocado, madre. También él es Alejandro.",
    PAP('No te has equivocado, madre. También él es Alejandro.', 'Alejandro a Sisigambis, según Arriano y Diodoro', 'Anábasis de Alejandro, II, 12', at='No te has equivocado'))
NEW("[serious] Alejandro las trató como a reinas. Sisigambis, la madre de Darío, acabaría tan unida a él que, según cuentan los autores antiguos, cuando Alejandro murió dejó de comer hasta morir. [short pause] Pero eso llegaría años después. Antes faltaba la batalla final.",
    ai('sisigambis', 'a dignified elderly queen in dark robes seated in a tent surrounded by princesses, a young conqueror bowing slightly before her, lamp light, seen from behind', at='las trató como a reinas'))
NEW("La noche antes de la última batalla, su general Parmenión le aconsejó atacar a oscuras, por sorpresa. La respuesta de Alejandro se hizo famosa.",
    ai('noche_gaugamela', 'two commanders talking in a dark camp before a battle, thousands of enemy campfires glittering across the plain in the distance, tension', at='atacar a oscuras'))
ALE("[serious] No robaré la victoria.",
    PAP('No robaré la victoria.', 'Alejandro a Parmenión, según Plutarco', 'Vida de Alejandro, 31', at='No robaré la victoria'))
ESP("[dramatically] Gaugamela, cerca de la actual Mosul, uno de octubre del año trescientos treinta y uno. Darío ha reunido al mayor ejército que le queda: carros con cuchillas en las ruedas, elefantes de la India, caballería de todo el imperio. [pause] Y vuelve a pasar lo mismo. Alejandro abre un hueco, carga hacia el rey. Y el rey huye.",
    ph('Gaugamela', at='Gaugamela', lt=['Gaugamela', 'Cerca de Mosul, Irak']),
    ai('carros_cuchillas', 'Persian scythed chariots charging across a flat plain toward Macedonian infantry that opens lanes to let them pass, blades spinning on the wheels, dust storm', at='carros con cuchillas'),
    ai('dario_huye', 'a royal chariot fleeing through clouds of dust away from a collapsing battle line, a cavalry charge closing in behind, sunset', at='el rey huye'))
NAR("[serious] Babilonia y Susa abrieron sus puertas. Y a principios del año trescientos treinta, Alejandro llegó a Persépolis. Plutarco cuenta que, para llevarse el tesoro, hicieron falta diez mil parejas de mulas y cinco mil camellos.",
    ph('Persepolis', at='llegó a Persépolis'),
    ai('tesoro_mulas', 'an endless caravan of mules and camels loaded with chests of gold and silver leaving a palace city, soldiers guarding it, dust and evening light', at='cinco mil camellos'))
ALE("[serious] ¿Debo pasar de largo y dejarte tirado, por la guerra que hiciste a los griegos? ¿O levantarte, por tu grandeza de espíritu y tu virtud?",
    ai('estatua_caida', 'a young conqueror standing before a toppled colossal stone statue of a Persian king lying on the floor of a palace hall, soldiers looting in the background, contemplative', at='Debo pasar de largo'),
    PAP('¿Debo pasar de largo y dejarte tirado, por la guerra que hiciste a los griegos? ¿O levantarte, por tu grandeza de espíritu?', 'Alejandro ante una estatua caída de Jerjes, según Plutarco', 'Vida de Alejandro, 37', at='O levantarte'))
NEW("Así le habló Alejandro, según Plutarco, a una estatua de Jerjes derribada por sus soldados. Se quedó un buen rato en silencio, mirándola. Y siguió su camino. [pause] Unos meses después, Persépolis ardió.",
    ph('Persepolis Apadana columns', at='Persépolis ardió'))
B('tension')
NAR("[serious] Cómo empezó el fuego es uno de los grandes misterios de la Antigüedad. Plutarco y Diodoro cuentan una fiesta. Alejandro y sus oficiales bebiendo. Y una cortesana ateniense, Tais, que propone vengar a Atenas quemando el palacio de Jerjes.",
    ai('fiesta_tais', 'a drunken banquet in a columned palace hall at night, a woman in a Greek dress raising a torch high, officers rising with goblets, firelight on gold', at='una cortesana ateniense'))
HER("Alejandro se puso en pie, con una corona en la cabeza y una antorcha en la mano, y fue el primero. Los demás lo siguieron entre gritos, y rodearon el palacio.",
    ai('persepolis_llamas', 'the great columned hall of Persepolis engulfed in flames at night, cedar roof collapsing, silhouettes of Macedonian soldiers with torches', at='una antorcha en la mano'),
    PAP('Alejandro se puso en pie, con una corona en la cabeza y una antorcha en la mano, y fue el primero.', 'Plutarco', 'Vida de Alejandro, 38', at='fue el primero'))
NEW("Arriano, otro historiador antiguo que se basa en generales de Alejandro, da una versión más fría: fue una decisión política. Castigar a los persas por la quema de Atenas. [short pause] La arqueología apunta a algo planeado: el tesoro se vació antes, y el fuego arrasó sobre todo los grandes salones de Darío y de Jerjes.",
    OTRA(['Una borrachera y una cortesana', 'Un incendio por capricho'], ['Una decisión política', 'El fuego, en los palacios de Jerjes', 'Venganza por la Acrópolis'], at='una versión más fría'))
NAR("[serious] Pero hubo algo que el fuego no alcanzó. [short pause] En un cuarto de la muralla, lejos de los palacios, seguían guardadas miles de tablillas de barro con las cuentas del imperio. Allí se quedaron, enterradas, durante veintitrés siglos. [pause] El incendio que debía borrar Persia no pudo con su contabilidad.",
    ai('tablillas_fuego', 'stacks of clay tablets lying untouched in a dark storeroom inside a thick mud-brick wall while the glow of a distant fire flickers through a crack, smoke outside', at='el fuego no alcanzó'),
    ph('Persepolis Fortification Archive', at='veintitrés siglos'))
NEW("Darío III huía hacia el este. En julio del año trescientos treinta, sus propios sátrapas, encabezados por Beso, lo encadenaron y lo apuñalaron. Alejandro llegó tarde. Según Plutarco, se quitó su manto y cubrió con él el cadáver de su enemigo.",
    cd(dict(type='map', title='330 a. C.: la huida de Darío III', bbox=[44, 30, 62, 40], points=[dict(name='Ecbatana', lon=48.51, lat=34.8), dict(name='Puertas Caspias', lon=52.3, lat=35.6), dict(name='Hecatómpilo', lon=54.5, lat=36.4, big=1)]), at='huía hacia el este'),
    PAP('Lo encadenaron, lo metieron en un carro y, al ver llegar a Alejandro, lo hirieron y lo dejaron morir.', 'Arriano', 'Anábasis de Alejandro, III 21', at='lo encadenaron'),
    ai('dario_muerto', 'a dying king lying in an abandoned wagon in the desert, a young conqueror kneeling and covering him with his own red cloak, soldiers standing back, dawn', at='cubrió con él el cadáver'))
NAR("[serious] Lo mandó enterrar con honores reales, junto a los reyes persas. Y persiguió a Beso hasta capturarlo. [short pause] Ahí termina, oficialmente, el Imperio Aqueménida. Doscientos veinte años después de que Ciro se rebelara contra los medos. [pause] Pero aquí viene lo más inesperado.",
    cd(dict(type='timeline', header='El Imperio Aqueménida', events=[['550 a. C.', 'Ciro se rebela contra los medos'], ['522 a. C.', 'Darío llega al trono'], ['480 a. C.', 'Termópilas y Salamina'], ['330 a. C.', 'Muerte de Darío III']]), at='termina, oficialmente'))

# ---------------- IX · LO QUE DEJÓ PERSIA ----------------
T('Lo que dejó Persia', 'El conquistador conquistado', num='IX', sting='tema')
B('tema')
NEW("Pasargadas, año trescientos veinticuatro. Alejandro vuelve de la India y encuentra la tumba de Ciro saqueada. [short pause] Manda castigar al saqueador, ordena restaurarla y pide que le lean la inscripción que había en ella.",
    ph('Pasargadae tomb of Cyrus', at='la tumba de Ciro saqueada'))
CIR("[serious] Hombre, quienquiera que seas y de dondequiera que vengas, porque sé que vendrás: yo soy Ciro, el que dio a los persas su imperio. No me envidies este poco de tierra que cubre mi cuerpo.",
    PAP('Hombre, quienquiera que seas y de dondequiera que vengas: yo soy Ciro, el que dio a los persas su imperio. No me envidies este poco de tierra que cubre mi cuerpo.', 'Inscripción de la tumba de Ciro, según Plutarco', 'Vida de Alejandro, 69', at='quienquiera que seas'),
    ai('alejandro_tumba', 'a lone conqueror standing before a simple stone tomb on six steps in a windswept plain at sunset, his helmet in his hands, his face turned away', at='No me envidies'))
NAR("[softly] Plutarco dice que aquellas palabras conmovieron profundamente a Alejandro. [short pause] Y quizá explican lo que hizo después. Porque el hombre que vino a vengar a Grecia acabó adoptando la túnica de los reyes persas, su ceremonial y sus costumbres de corte, ante el escándalo de sus generales macedonios.",
    ai('alejandro_persa', 'a young king wearing Persian royal robes and diadem receiving bowing courtiers in a Persian palace, Macedonian officers watching with disapproval in the shadows', at='adoptando la túnica'))
NEW("En Susa, en el año trescientos veinticuatro, organizó una boda colectiva: él mismo y unos ochenta de sus oficiales se casaron con mujeres de la nobleza persa y meda. Alejandro, con Estatira, la hija de Darío III. [short pause] El conquistador quería un imperio mixto. Persa y griego a la vez.",
    ai('bodas_susa', 'a grand mass wedding ceremony in a huge tent at Susa, dozens of couples in Greek and Persian dress seated side by side, gold and purple canopies, festive torchlight', at='una boda colectiva'),
    ph('Susa archaeological site', at='En Susa'))
NEW("En Opis, según el historiador Arriano, Alejandro celebró un banquete con nueve mil invitados, macedonios y persas sentados juntos. Y rezó a los dioses por la concordia entre los dos pueblos, y por que gobernaran el imperio como socios.",
    ai('banquete_opis', 'an enormous banquet under a vast canopy with thousands of Macedonian and Persian guests seated together, a king raising a golden cup in a libation, torches and evening sky', at='nueve mil invitados'),
    ph('Alexander the Great bust Acropolis Museum', at='como socios'))
NAR("[serious] Murió un año después, en Babilonia, con treinta y dos años. Su imperio se partió entre sus generales. Pero la máquina que montaron Ciro y Darío siguió funcionando: las satrapías, los caminos, la moneda, la idea de gobernar a muchos pueblos sin borrarlos. Los seléucidas, los partos y los sasánidas la heredaron.",
    cd(dict(type='list', header='Lo que heredaron los siguientes imperios', items=['Provincias con gobernador: las satrapías', 'Caminos y correo con postas', 'Una moneda de oro para todo el imperio', 'Tolerancia con dioses y leyes locales']), at='la máquina que montaron'),
    ph('Taq-e Kasra Ctesiphon', at='los sasánidas'))
NEW("Y nos dejó palabras. Los persas llamaban pairidaeza a sus jardines cerrados, llenos de árboles y agua. Los griegos la convirtieron en parádeisos. [short pause] Y de ahí viene la palabra que usamos hoy para el lugar más feliz que podemos imaginar: paraíso. [short pause] Jenofonte cuenta que el espartano Lisandro visitó uno, en Sardes.",
    ph('Eram Garden Shiraz Persian garden', at='sus jardines cerrados', lt=['Jardín persa', 'Irán · hoy']),
    KA('PARAÍSO', 'jardin_persa', 'a walled Persian garden with long water channels, cypress and fruit trees, a pavilion at the end, birds, soft morning light', at='paraíso'))
GRI("Lisandro se quedó admirado de la belleza de los árboles, plantados a la misma distancia, en filas rectas, y del perfume que lo envolvía al pasear. Ciro le dijo: «Todo esto lo he medido y ordenado yo. Y algunos de estos árboles los planté con mis propias manos».",
    PAP('Todo esto lo he medido y ordenado yo. Y algunos de estos árboles los planté con mis propias manos.', 'Ciro el Joven a Lisandro, según Jenofonte', 'Económico, IV, 21 – 22', at='los planté con mis propias manos'),
    ai('paraiso_sardes', 'a Persian prince in fine robes walking with a Spartan general through an orchard of perfectly aligned fruit trees with water channels, flowers, morning light', at='plantados a la misma distancia'))
NAR("[serious] Incluso los griegos que lo combatieron lo sabían. Ocho años después de Salamina, un veterano de Maratón, el dramaturgo Esquilo, estrenó en Atenas una tragedia llamada Los persas. [short pause] No celebra la victoria griega. Llora la derrota persa. La cuenta desde la corte de Susa, a través de la madre de Jerjes.",
    ph('Aeschylus bust Capitoline', at='Esquilo', lt=['Esquilo', 'Dramaturgo ateniense · veterano de Maratón', 'griegos']),
    ph('Theatre of Dionysus Athens', at='estrenó en Atenas'))
GRI("[softly] ¡Oh, ciudades de toda la tierra de Asia! ¡Oh, tierra de Persia, gran puerto de riqueza! ¡Cómo, de un solo golpe, se ha destruido tanta prosperidad!",
    PAP('¡Oh, tierra de Persia, gran puerto de riqueza! ¡Cómo, de un solo golpe, se ha destruido tanta prosperidad!', 'Esquilo', 'Los persas, 472 a. C.', at='Oh, tierra de Persia'))
NAR("[serious] La primera obra de teatro que se conserva en la historia de Occidente está contada desde el lado persa. [pause] Los que vinieron después, empezando por Hollywood, prefirieron otra cosa: un enemigo sin rostro. Monstruos.",
    ph('Theatre of Dionysus Athens', at='La primera obra de teatro'),
    ai('sombras_ejercito', 'a menacing silhouette of a faceless dark army against a blood red sky, exaggerated and theatrical like an old movie poster but without any text', at='un enemigo sin rostro'))
NEW("[serious] Pero las piedras no cambian de bando. Siguen ahí: la tumba de Ciro en Pasargadas, la pared de Behistún, los palacios quemados de Persépolis. Y en Chicago y en Teherán, decenas de miles de tablillas que todavía se están leyendo.",
    ph('Pasargadae', at='la tumba de Ciro'),
    ph('Bisotun Kermanshah', at='la pared de Behistún'),
    ph('Persepolis Tachara palace ruins', at='los palacios quemados'),
    ph('Persepolis Fortification Archive', at='decenas de miles de tablillas'))
NAR("[serious] El propio Heródoto, el griego que nos contó a Jerjes azotando el mar, empezó su libro con una frase que hoy parece escrita para este documental. [pause]",
    ph('Herodotus bust Metropolitan Museum', at='El propio Heródoto'))
HER("[softly] Escribo esto para que el tiempo no borre lo que hicieron los hombres, y para que las grandes y maravillosas hazañas, tanto de los griegos como de los bárbaros, no se queden sin gloria.",
    PAP('Para que las grandes y maravillosas hazañas, tanto de los griegos como de los bárbaros, no se queden sin gloria.', 'Heródoto', 'Historias, I, 1', at='para que el tiempo no borre'),
    ph('Persepolis Tachara palace ruins', at='no se queden sin gloria'))
NAR("[serious] Tanto de los griegos como de los bárbaros. [short pause] Ni siquiera el primer historiador de Occidente creía que los persas fueran monstruos.",
    ph('Persepolis Apadana relief soldiers', at='Ni siquiera el primer historiador'))
NEW("Si viste nuestro documental sobre las Termópilas, ahora conoces la otra mitad. [short pause] En el próximo episodio de DocuVox: Cartago, la ciudad que Roma necesitó borrar del mapa. Suscríbete para no perdértelo.",
    ph('Thermopylae', at='las Termópilas'),
    ph('Carthage ruins Byrsa', at='Cartago', lt=['Cartago', 'Túnez · hoy']))
M('tema', 8)
