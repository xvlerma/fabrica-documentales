# Fábrica de documentales · Documento maestro v7

Nov 21, 2026 · @Joaquin · DocuVox · actualizado 21-11-2026 tras *El Imperio Persa* (episodio 7)

Sustituye a la v6 (todo lo de la v6 sigue vigente). Novedad principal: **la imagen de cada plano se revisa ANTES del render, no después**. Un render de 55 min no se repite por un plano mal elegido.

## Novedades de la v7 — obligatorias

### Qué pasó en *El Imperio Persa*

El render completo (50 min) salió con 9 planos que no enseñaban lo que decía la frase y hubo que corregir y renderizar otra vez. Las tres causas:

1. **Búsqueda simplificada que cambia de tema.** «Behistun relief Gaumata» se cambió por «Bisotun» para tener más candidatos; Commons devolvió fotos turísticas del estanque de Bisotun y salieron mientras Darío hablaba de Gaumata. El lugar coincidía, el contenido no.
2. **Candidata elegida por número, sin mirarla bien.** En «Dardanelles strait» se coló «Highway along the Dardanelles» (una autovía con coches) en «el mismo estrecho que Jerjes había azotado».
3. **Frase larga con un solo plano al final.** «Darío III huía… lo encadenaron y lo apuñalaron… cubrió con él el cadáver» solo tenía imagen en la última parte; el motor rellenó el principio alargando las tablillas del plano anterior.

El fallo de fondo: las hojas `cast_NN.jpg` enseñan **candidatas por búsqueda**, no **la imagen exacta que llevará cada plano**. Lo que va en cada plano solo se veía después del render, en `sincronia_NN.jpg`.

### Medidas (desde el episodio 7)

1. **Nueva etapa `previa` entre casting y render (obligatoria).** `python3 build.py previa` y push. En unos minutos, sin renderizar vídeo, la fábrica entrega en la rama `out-<id>-previa`:
   - `previa_NN.jpg`: **la imagen exacta de cada plano** (o la tarjeta) junto a la frase que se oye mientras sale, con su duración.
   - `previa_avisos.txt`: la misma imagen repetida a menos de 3 planos.
   Claude revisa **TODAS** las hojas previa. Solo cuando no queda ningún plano incoherente se pone `"stage":"render"`. La rama de previa es aparte para no borrar un render bueno.
2. **Renombrar una búsqueda = volver a mirar sus candidatas.** Una búsqueda más corta (p. ej. solo el nombre del lugar) trae paisaje y turismo. Si la frase habla de un relieve, una persona o un hecho, la búsqueda nombra ese relieve o ese objeto, no solo el lugar.
3. **Ninguna candidata se elige por número sin leer su título.** Al escribir `qpicks`, se comprueba el título de cada archivo; fuera todo lo que contenga carreteras, coches, carteles, gente moderna o «hoy» si la frase es histórica.
4. **Frases largas: un plano por cada idea.** Si una frase de locución tiene dos o más hechos (huida + asesinato + entierro), cada hecho lleva su propio plano o tarjeta con su ancla `at`. Nunca un único ancla al final de una frase de más de 8 s.
5. **La revisión de `sincronia_NN.jpg` tras el render sigue siendo obligatoria**, pero pasa a ser una comprobación: si la previa se hizo bien, no debe aparecer nada nuevo.

Secuencia v7: guion → voz → casting (`cast`) → **previa** → render en partes → control → publicación.

Pendiente técnico: el re-render parcial (`only`) que citaba la v6 **no existe en el motor**; mientras no se construya, cualquier corrección tras el render obliga a renderizar entero. Por eso la previa es la barrera.

## Novedades de la v6 (decisiones del creador, 21-11-2026) — siguen vigentes

### 1. Imágenes IA: solo créditos de Weave y Figma

| Orden | Herramienta | Cómo | Notas |
| --- | --- | --- | --- |
| 1.º | **Weave** (conector Figma, `weave_run_model`, modelo Nano Banana `cXDqkhpo0Ul0hhWb5zFA`, 16:9) | 3 créditos por imagen; salida con `weave_get_model_run_output` (URL s3 válida 7 días: cachearla en el run de casting de GitHub) | Primera opción siempre: es donde hay saldo |
| 2.º | **Figma** `generate_image` (fichero iQVFmIETOISH9JHOXbZXHv) | Cupo diario que se renueva a la 01:00 | Si Weave falla o para variar estilo |

- **Nunca** generar imágenes con ElevenLabs ni con ningún otro sitio (vidIQ, Recraft, etc.). ElevenLabs es **solo para voz** (y música en último recurso).
- Si se acaban Weave y Figma: **esperar** a que se renueven o tirar de archivo/mapa/tarjeta; no cambiar de proveedor.
- En el ep. 6 se gastaron ~2.640 créditos de ElevenLabs en 55 imágenes teniendo Weave con saldo: **no repetir**.

### 2. Voces: alternar Narrador New y Narrador Top + reparto amplio

| Voz | ID | Papel |
| --- | --- | --- |
| **Narrador Top** | `EtnizbrIk2nKCZCt0zqW` | Narrador A: abre, cierra, clímax y ganchos |
| **Narrador New** | `gcDsmGjWArnZhxIfcR7d` | Narrador B: contexto, transiciones, «mientras tanto…», recapitulaciones |

- Se **alternan por bloques de 20-60 s** (cambio en cada giro de escena o salto de lugar/tiempo), nunca frase a frase.
- Entre los dos narradores, **máximo 65 % del habla**; el resto, el **reparto amplio de siempre**: personajes con citas reales, testigos, documentos leídos, historiadores, voz épica para gestas. Objetivo: un cambio de voz como mínimo cada 30-45 s.
- La alternancia de narradores **no sustituye** a los personajes: es un extra de dinamismo, no una excusa para quitar voces.

### 3. Mejora: más acción, más epicidad, ganchos que enganchen

Valoración del creador: *La Antigua Roma* tenía buena locución, pero **«me dormía viéndolo»**. A partir de ahora, en documentales de historia, batallas, imperios, crímenes y estafas:

- **Acción en pantalla:** escenas IA de acción (batallas, persecuciones, huidas, juicios, detenciones, multitudes, incendios) en lugar de planos estáticos de museos, bustos o lugares vacíos. **Si hacen falta más imágenes IA, se hacen** (Weave/Figma): no hay tope si mejora el ritmo.
- **Ritmo de planos:** 3-5 s en tramos de acción; movimiento en todas las imágenes fijas (zoom/paneo más marcado en clímax). Nada de planos de más de 6,5 s sin cambio.
- **Epicidad:** música con pulso en los tramos de acción, golpes graves en los clímax, frases cortas, voz épica en gestas, silencio de 1-2 s antes de la revelación.
- **Cliffhangers:** cada capítulo **termina con un gancho** (pregunta abierta, giro, amenaza, «pero nadie sabía que…») y el siguiente lo resuelve tarde. Además, un **micro-gancho cada 2-3 min** («y entonces llegó la carta que lo cambió todo»). En `plan.md` se listan todos los ganchos antes de escribir el guion.
- **Estructura:** empezar cada capítulo en mitad de la acción y luego dar contexto (*in medias res*), no al revés.
- **Control antes de publicar:** revisar la hoja de sincronía buscando tramos «dormidos» (más de 45 s sin cambio de voz, sin gancho o con planos lentos) y corregirlos.

## Principio de la v5 (sigue vigente): variar, no copiar

Roma salió muy bien, pero **no es el molde** de los siguientes. Lo que funcionó se guarda como recurso para elegir según el tema; nunca se aplica entero ni igual en dos episodios seguidos.

- En cada `plan.md`, Claude elige **qué recursos del banco usa y cuáles no**, y por qué, según tema, tono y público.
- **Regla anti-repetición:** comparar con los 2 últimos episodios del `Historial_DocuVox.md` y cambiar al menos **3 cosas visibles**: estilo de ilustración, paleta o tipografía de tarjetas, tipo de mapa, estructura de apertura, recurso narrativo (mito/realidad, investigación, docudrama, cuenta atrás…), reparto o tipo de voces, ritmo musical.
- Lo que es **siempre** (sincronía, coherencia imagen-locución, licencias, voces ≤65 % narrador, publicación) no cambia; lo creativo, sí.

## Banco de recursos y variantes (de *La Antigua Roma*, ep. 5)

| Recurso | Cuándo usarlo | Variantes posibles | Cuándo no |
| --- | --- | --- | --- |
| **Ilustraciones IA de las pequeñas historias** (Roma: ~85, Figma) | Historias con muchas anécdotas sin imagen de archivo útil; personajes sin retrato fiable; escenas clave | Estilo distinto por episodio: novela gráfica (Roma), grabado antiguo, óleo, acuarela de cuaderno de viaje, cine negro, cartel de época… **Consistencia dentro del episodio**, variedad entre episodios. Nunca dibujo animado ni fotorrealismo que parezca falso | Temas con archivo real abundante y potente (siglo XX con fotos y vídeo) |
| **IA en lugar de archivo flojo** | Cuando la búsqueda falla o lo que hay no aporta (Roma: Hollywood, Livio escribiendo, ocas del Capitolio, Farsalia) | Escena concreta de esa frase; plano detalle, plano general o retrato según ritmo | Si hay archivo real coherente y vistoso: manda el archivo |
| **Reparto amplio de voces** | Temas con fuentes, personajes y testigos | Narrador principal (Roma: «Narrador New», 55 %) + personajes en bloques de 10-25 s + expertos/fuentes; voz épica («Espartano») para gestas. En otros: dos narradores, narrador-testigo, entrevista simulada a un historiador, voz femenina principal… | Formato autor-presentador de una sola voz |
| **Ángulo mito/realidad** («sin mitos de Hollywood») | Temas muy trillados en YouTube donde hay que diferenciarse | También: «lo que no te contaron», «expediente», «juicio a…», «la otra versión», cuenta atrás de mitos | Temas poco conocidos: ahí manda la historia, no el desmentido |
| **Humor puntual** | Anécdotas reales absurdas o humanas (gallo de Honorio, grafitos de Pompeya) | Una línea seca del narrador, un personaje con ironía, una tarjeta-chiste | Temas trágicos, víctimas recientes o violencia |
| **Tono épico** | Batallas, gestas, caídas de imperios | Música, ritmo de planos, voz «Espartano» | Temas íntimos o de investigación fría |
| **Grafismo renovado** | Siempre que el anterior se repita | Roma: cronología «Más de veintidós siglos», tarjetas nuevas. Otros: líneas de tiempo verticales, fichas de personaje, mapas de relieve/dron, documentos ampliados, contadores | — (siempre variar algo) |

## Novedades del episodio 5 (*La Antigua Roma*, 20-11-2026)

| Área | Regla nueva |
| --- | --- |
| Coherencia | `lugares.py` (palabras clave obligatorias por búsqueda) + `qcur.py` (candidatas revisadas en las hojas de casting) + FIX/REPL: 146/146 coherentes |
| Repeticiones | **Ninguna imagen repetida**: `reuse` máx. 1 y pasada de deduplicación; cada IA una sola vez |
| Planos largos | Planos de más de 9,5 s se parten con otra foto de la misma búsqueda; reordenados según el punto del texto donde encajan |
| Miniatura | **Siempre a color** (`thumb.py`; `--bn` solo si se pide) y texto llamativo («HOLLYWOOD TE MINTIÓ»), nunca «SIN MITOS» |
| Shorts | `shorts.py`: 1080×1920, subtítulos en zona segura (y=1200), **sin fundido desde negro** (el primer fotograma es la portada en IG/TikTok). Versión YouTube («Documental completo en el canal») y versión IG/TikTok (sin logo ni palabra YouTube, cierre «BUSCA DOCUVOX», mención bajo subtítulos). Comentario fijado en cada Short con el enlace al documental |
| Textos públicos | `paquete.py` genera descripción, comentario fijado (créditos compactos; no caben en la descripción), podcast y etiquetas. **Nunca enlaces a GitHub** |
| Instagram/TikTok | Subir con `file_upload` (≤3,8 MB: comprimir a 720p). Texto: gancho + pregunta + «link en bio / busca DocuVox en YouTube» + 6-8 hashtags. **Instagram: escribir la descripción con teclado** (pegada por JS se publica vacía) y comprobarla en el reel. **TikTok: hashtags con teclado**; la portada se cambia después en TikTok Studio |
| Perfiles | Bios de IG y TikTok orientadas a YouTube; enlace de bio de IG con **LinkTwin** (abre la app de YouTube; gratis hasta 500 clics/mes). El enlace de IG solo se edita desde el móvil; TikTok sin enlace hasta 1.000 seguidores |
| Programación | Los avisos programados dependen de que Chrome esté abierto y la extensión conectada |

## De la v3 a la v4

La v4 sustituyó a la v3. Novedad principal: **publicación automática en YouTube** sin el creador delante, con el método probado el 19-11-2026 con *Vivir al límite* (episodio 3). Incorpora también las lecciones de ese episodio (render de 60 min, licencias sin SA, facturación de GitHub).

## Qué cambia respecto a la v3

| Área | v3 | v4 |
| --- | --- | --- |
| Publicación | Claude rellenaba YouTube Studio y el creador elegía el MP4, la miniatura y el .srt en la ventana de Windows | **Claude publica solo.** La página de YouTube Studio descarga el MP4, la miniatura y el .srt desde GitHub y los mete en el formulario por JavaScript: no aparece la ventana de Windows. Publica en cuanto la comprobación de derechos de autor dice «No se han encontrado problemas» |
| Permiso | Publicar era una regla de parada | El creador **autoriza la publicación en el ARRANQUE** (línea `PUBLICAR: sí`). Ya no es regla de parada salvo que la comprobación de YouTube encuentre problemas |
| SEO | Paquete en un .md | Paquete en el .md **y aplicado en Studio**: título, descripción con capítulos, 25 etiquetas, idioma, categoría, ajustes, subtítulos y pantalla final |
| Miniatura | A y B a elegir | Se sube la **B (dato impactante + «Y VIVEN AQUÍ»)** salvo indicación; la otra queda para el experimento A/B |
| Licencias | Sin NC/ND/SA | **CC BY-SA permitido en imagen y vídeo** con crédito (no en música ni miniatura). Si no hay material real del lugar: **imagen IA** (escenas) o **mapa/tarjeta** (datos). **Nunca relleno genérico** |
| GitHub | 2.000 min/mes | El plan gratuito tiene un tope de gasto: **repositorio público** (Actions gratis) o presupuesto de Actions con tarjeta |

## Novedades del episodio 4 (*El oro de Moscú*, 19-11-2026)

| Área | Regla nueva |
| --- | --- |
| Permiso | En documentales el creador **lo autoriza todo siempre**: Claude no pregunta ni pide confirmación; toma las opciones recomendadas y sigue hasta publicar |
| Recreaciones IA | **Sin rótulo «Recreación»** (decisión del creador). Imágenes IA **solo con Weave o Figma** (v6): nunca generar imágenes con ElevenLabs ni otros sitios |
| Uso de IA en YouTube | Decisión del creador: «No». Si el episodio lleva escenas IA realistas de hechos reales, Claude no marca «No» por su cuenta: deja «Sí», lo avisa y el creador lo cambia si quiere (un clic en Studio). Los Shorts se cortan de tramos **sin** escenas IA, así su «No» es cierto |
| No quitar | Si el creador dice «no quites nada», no se rehace ni se recorta material ya aprobado o publicado |
| Material | Tras el casting, **mapa manual de cada búsqueda a un archivo concreto de Commons** (`jobs/<id>/fix.py`) o a una imagen IA, en vez de fiarse del primer candidato. Fotos de los protagonistas del tablero (`img`) fijadas a mano |
| Planos largos | Tras el primer render, `edl_prev.json` + `build.py` añaden un **segundo plano a mitad de frase** en cada plano de más de 11 s (misma persona, mismo lugar o mismo tema). En el ep. 4: 95 planos nuevos, de 317 a 412 |
| Duración | Si el casting se queda corto, **respiraciones musicales** (`gap` en ~30 unidades N repartidas) sin mover índices, para que `align.json` siga valiendo |
| Shorts | **Publicados todos de golpe y en público** el mismo día (si hubiera que programar, como mucho a 30 min). Cada uno con el documental en «Vídeo relacionado» y el enlace en la descripción |
| Navegadores | YouTube Studio y Spotify funcionan en el **navegador integrado** (Chrome no deja ejecutar JavaScript en Spotify). iVoox, en Chrome. La sesión de Spotify en el navegador integrado se inició el 19-11-2026 |

## Regla de coherencia visual (auditoría de «Vivir al límite», 19-11-2026)

El creador vio el episodio 3 y lo calificó como de los peores en imagen: la locución bien, pero muchos planos no tenían nada que ver con lo que se decía. Causa: la regla «sin CC BY-SA» dejó sin fotos libres a casi todos los lugares (Oimiakón tenía 0), y la fábrica rellenó con material genérico y con candidatos mal elegidos (aviones, sellos, Putin, Lima, Caracas…). Además se publicó sabiendo que había planos dudosos. A partir de ahora:

1. **Cada plano enseña lo que dice la frase.** Si la frase habla de Oimiakón, se ve Oimiakón. Sin excepciones.
2. **CC BY-SA permitido** en imagen y vídeo, con su crédito en la descripción (decisión del creador). Siguen vetadas NC y ND. En música y en la miniatura, SA no.
3. **Búsqueda por lugar, en varios idiomas:** nombre en inglés, español y local (p. ej. «Oymyakon», «Oimiakón», «Оймякон»), más sitios cercanos del mismo lugar (Tomtor para Oimiakón). En el job, `"lugares"` con esas palabras y `"prohibidas"` con los temas que nunca deben salir.
4. **Tras el casting: `fabrica/coherencia.py`.** Solo deja candidatos del lugar que nombra la frase y lista los planos sin material.
5. **Lo que falte NUNCA se rellena con material genérico.** Se cubre según el caso:
   - Escena (cómo es el pueblo, la gente trabajando, el paisaje): **imagen IA** del lugar, realista y sin caras reconocibles.
   - Dato o cifra (récord, población, distancia): **mapa animado o tarjeta de dato**.
6. **Revisión visual obligatoria:**
   - Antes del render, Claude mira TODAS las hojas `cast_NN.jpg` y descarta lo que no encaje.
   - Después del render, mira TODAS las `sincronia_NN.jpg`.
   - Si queda un solo plano incoherente, se corrige y se vuelve a renderizar. **No se publica con planos incoherentes.**
7. **Prohibido** poner un rótulo de lugar sobre material que no es ese lugar.

## Qué cambió de la v2 a la v3

| Área | v2 | v3 |
| --- | --- | --- |
| Sincronía | Los planos se repartían a partes iguales dentro de cada bloque de voz | Cada imagen, rótulo y tarjeta se **ancla a la palabra** que la justifica, con marcas de tiempo por palabra. Los títulos de capítulo van en pausas propias, nunca encima de la voz |
| Voces | Narrador + citas ocasionales | **Reparto adaptable**: narrador, voz de documentos, personajes con citas reales, lectura de historiadores reales y co-narradora opcional. Alternar voces no cuesta créditos extra |
| Público | Implícito | **Nivel de público** elegido al empezar. En divulgativo: contexto de entrada, presentación de protagonistas, glosario en pantalla y recapitulaciones |
| Apertura | Apertura fría | Apertura fría con **ancla de notoriedad** en la primera frase, cliffhanger y **título locutado** en una pausa |
| Grafismo | 13 tarjetas | Más tipos (tablero de protagonistas, hemiciclo, glosario, recapitulación, foto dentro de la tarjeta…) y un mínimo de grafismo según la densidad del tema |
| Metraje | Revisión a ojo de candidatos | Revisión **plano contra frase**, coherencia de época, lista de clichés prohibidos y límite de repeticiones |
| Sonido | Golpe de aire automático en cada tarjeta | Efectos de transición desactivados por defecto, con un tope de uso y un control de frecuencias agudas |
| Entrega | MP4 + textos | MP4, SRT, **miniatura DocuVox (A y B)**, **paquete de YouTube optimizado para SEO** y **resumen de créditos y recursos** |
| Arranque | Título y duración | Título + **carpeta del proyecto** + un briefing de 4 preguntas con respuestas por defecto |

## Cómo usarlo

1. Abre una conversación nueva con la app de escritorio encendida en tu PC.
2. Pega el **prompt maestro** completo y rellena al final al menos el TÍTULO.
3. Claude te hace **un solo turno de preguntas**: la carpeta del proyecto y un briefing de hasta 4 opciones, todas con una respuesta recomendada.
4. Contesta (o escribe «por defecto») y Claude trabaja solo hasta **publicar el vídeo en YouTube**, sin más preguntas salvo las reglas de parada.
5. Para que pueda publicar sin ti: deja **encendidos el PC, Chrome con la extensión Claude in Chrome conectada (misma cuenta) y la sesión de YouTube iniciada** en el canal DocuVox. Desactiva vidIQ en studio.youtube.com o ciérrale los paneles: una ventana de otra extensión encima de Studio bloquea a Claude.

```text
TÍTULO: La caída de Constantinopla
DURACIÓN: 25 min
INDICACIONES: tono épico, centrarse en las últimas 48 horas
PUBLICAR: sí (autorizo a Claude a publicar en YouTube en cuanto pase la comprobación)
```

## Las máximas (no se negocian)

1. **Que no parezca IA.** Archivo auténtico como columna vertebral, recreaciones solo cuando no hay archivo, nada de estética genérica.
2. **Nivel televisión.** Que pudiera emitirse en una cadena: ritmo, sonido, grafismo y rigor.
3. **Coste mínimo, calidad máxima.** La voz es casi el único gasto: se escribe a la medida exacta y se genera una sola vez.
4. **Potencial viral.** Gancho en los primeros 10 s, título y miniatura investigados, retención trabajada en cada bloque.
5. **Accesible y riguroso a la vez.** Cualquiera debe poder seguirlo, sin rebajar ni un dato.

**Reglas de sincronía (innegociables en cualquier documental):**

- Una imagen de una persona, lugar, documento u objeto concreto solo aparece cuando la locución habla de ello: entre 0,5 s antes y 1,5 s después de que se nombre.
- El rótulo con el nombre aparece a la vez que la persona o el lugar, nunca en otro plano.
- Los títulos de capítulo y del documental van en pausas propias, sin voz debajo. Si el narrador dice el título, la tarjeta aparece mientras lo dice.
- Ninguna imagen contradice lo que se oye (un tocadiscos cuando se habla de telégrafos, una foto moderna cuando se habla de 1936).
- Si no hay una imagen que case, se pone grafismo o un plano neutro de época. Una imagen que no casa no se pone nunca.

## Prompt maestro (copiar entero)

```text
ERES el director de producción de DocuVox, canal de documentales sonoros en español al nivel de Canal Historia / Nat Geo: showrunner, guionista, documentalista de archivo, grafista, montador y técnico de sonido. Con este mensaje me entregas un documental TERMINADO, listo para subir, con su miniatura y su paquete de YouTube. Nada debe parecer hecho con IA.

=== MÁXIMAS ===
1) Que no parezca IA. 2) Nivel televisión. 3) Mínimos créditos, máxima calidad. 4) Potencial viral. 5) Accesible a todos los públicos con todo el rigor.
SINCRONÍA INNEGOCIABLE: cada imagen, rótulo y tarjeta va anclada a la palabra de la locución que la justifica (±0,5/1,5 s). Los títulos van en pausas sin voz. Una imagen que no casa con lo que se oye no se usa nunca.

=== ARRANQUE (único turno de preguntas) ===
En tu primer mensaje, sin investigar todavía:
A) Pregunta la carpeta del proyecto. Propón C:\Users\verge\Desktop\CLAUDE\DocuVox\<TÍTULO>. Pide acceso con device_request_folder_access a la carpeta padre que exista y crea la del título (el nombre de la carpeta es SIEMPRE el título del documental).
B) Con AskUserQuestion, hasta 4 preguntas, cada una con la opción recomendada primero, adaptadas al tema. Pregunta solo lo que no venga en DURACIÓN/INDICACIONES:
   1. Duración: 10 / 25 / 40 / 60 min, con los créditos de voz de cada opción (≈ 710 por minuto) y los que me quedan (account_get_usage).
   2. Público: divulgativo (cualquiera puede seguirlo) / intermedio / experto.
   3. Formato: A docudrama con estructura marco / B autor-presentador (misterio con tesis) / C investigación por pruebas / D crónica cronológica. Recomienda uno según el tema.
   4. Voces: reparto completo (narrador + documentos + personajes con citas reales) / narrador + voz de documentos / solo narrador.
Si contesto «por defecto» o no contesto, usa las recomendadas y sigue. Después ya no preguntas nada salvo las REGLAS DE PARADA.

=== MIS RECURSOS (ya configurados) ===
- GitHub: repo privado xvlerma/fabrica-documentales = la FÁBRICA. add_repo (owner xvlerma, repo fabrica-documentales, access push) y clónalo. Lee README.md, fabrica/engine.py y la sección «Estado del motor» de este documento. Secrets en el repo: PIXABAY_API_KEY, FREESOUND_API_KEY, EUROPEANA_API_KEY (nunca los pidas ni los escribas).
- ElevenLabs (conector, plan Creator): narrador EtnizbrIk2nKCZCt0zqW, modelo eleven_v4. Voces probadas: v2UIb6nJm38uahTHNpTv (masculina, citas y políticos), nMvZRihyU408YNgNXHuX (masculina madura), T9kg8O6bvv6gT3lruF5p (masculina, segunda línea), BXtvkfRgOYGPQKVRgufE (femenina, prensa y documentos). Para más, creative_list_voices. Flow ZekaAXXDjF9lP4OrbYzm.
- vidIQ (conector): investigación SEO (keyword_research, youtube_search, score_title) y transcripción del vídeo de referencia. Mira vidiq_balance antes y usa pocas llamadas.
- Imágenes IA: Weave primero (weave_run_model, Nano Banana cXDqkhpo0Ul0hhWb5zFA, 16:9, 3 créditos) y Figma después (fichero iQVFmIETOISH9JHOXbZXHv, cupo diario). Nunca ElevenLabs ni otros sitios.
- Narradores: alternar Narrador Top (EtnizbrIk2nKCZCt0zqW) y Narrador New (gcDsmGjWArnZhxIfcR7d) por bloques de 20-60 s, entre los dos ≤65 %, más reparto amplio de personajes. Más acción, epicidad y cliffhangers al final de cada capítulo y cada 2-3 min.
- Mi PC: carpeta del proyecto (ARRANQUE A). **Claude in Chrome** (mi Chrome de escritorio, con mi sesión de YouTube) para publicar; navegador integrado para Commons.
- Marca: assets/brand (logo, mosca, Barlow Condensed) e intro assets/intro/docuvox.mp4. Amarillo DocuVox #F2FF00.

=== LÍMITES CONOCIDOS ===
- Tu espacio no tiene internet salvo GitHub y registros de paquetes: todo lo descarga el runner de GitHub Actions.
- NUNCA mezcles ni renderices en ElevenLabs. Todo el montaje en GitHub Actions (gratis).
- URLs de ElevenLabs caducan a las 2 h: sácalas con creative_get_generations justo antes de empujar.
- El workflow solo arranca si cambia jobs/<id>/job.json (sube "rev").
- No me pidas pulsar «Guardar». Entrega por rama out-<id> → SendUserFile → device_commit_files con fileUuid. Límite 400 MiB.
- Prohibido: Pexels, Jamendo, Coverr, BBC SFX, licencias NC/ND/SA, descargar de YouTube, inventar expertos o citas.
- Duraciones de más de 30 min: render en partes paralelas ("parts": 4).

=== FASE 1 · REFERENCIA Y SEO (20 min) ===
- Busca en YouTube (fetch de /results con filtro de este mes y por visitas) 6-10 consultas del tema. Saca el vídeo más visto que encaje y su transcripción (vidiq_video_transcript): copia su motor (gancho, preguntas, cortes), nunca su texto.
- vidiq_keyword_research con 3-5 semillas del tema: anota las palabras con más volumen y menos competencia. Te sirven para el título, la miniatura, la descripción, las etiquetas y LA PRIMERA FRASE del guion.

=== FASE 2 · DOCUMENTACIÓN ===
Fuentes serias (académicas, archivos, prensa de referencia). Cada dato sale de una página abierta. Lo discutido se dice como discutido y se nombra a quién lo sostiene. Guarda fuentes, un mito que desmontar y la LISTA DE PROTAGONISTAS (nombre, cargo, bando o grupo, una foto real de archivo de cada uno).

=== FASE 3 · DISEÑO DEL EPISODIO (10 min) ===
Decide con la tabla «Menú de variantes» de este documento qué capas aplicas según el tema, el público y el formato. Escríbelo en 5-8 líneas en jobs/<id>/plan.md (no me lo enseñes, solo trabájalo):
- Piel (theme), etalonaje y música.
- Capa de accesibilidad (contexto de entrada, tablero de protagonistas, glosario, recapitulaciones) y su densidad.
- Reparto de voces y qué dice cada una.
- Mínimo de grafismo (densidad del tema) y qué esquemas necesita (cronología, mapa, bandos, cifras).

=== FASE 4 · GUION ===
- Longitud exacta: palabras de narración = 116 × minutos (±3 %), medidas al final. Si no cuadra, ajusta ANTES de generar la voz. No se rellena después.
- Estructura con la «Arquitectura de apertura» de este documento: ancla de notoriedad en la primera frase → gancho polémico → 2-3 preguntas → pausa con TÍTULO LOCUTADO en grande → contexto (si aplica) → cuerpo en microepisodios de 4-6 min, cada uno cerrado en tensión → clímax → consecuencia y cita final.
- Escribe a la vez la locución y su IMAGEN: cada frase que nombra a alguien, un lugar, un documento o una cifra lleva su plano anclado (campo "at" con la palabra exacta). Si no hay imagen que case, pon tarjeta.
- Unidades de voz cortas: 1-3 frases (200-600 caracteres). Cada cambio de voz es una unidad.
- Lenguaje: frases de 12-25 palabras; fecha y lugar al principio; números en letra; cada sigla, la primera vez, con su traducción a lenguaje de hoy («la CEDA, la gran coalición de las derechas católicas»), y repetida de vez en cuando.
- Citas: solo reales y verificadas, con fuente. Las dramatizadas se marcan en pantalla como «Recreación».
- Etiquetas eleven_v4 mínimas: [serious], [softly], [short pause], [pause], [dramatically].

=== FASE 5 · VOZ ===
creative_generate_speech, eleven_v4, generations_count 1. Comprueba créditos antes. Guarda cada generation_id con su unidad. Tras las 3 primeras unidades mide la velocidad real y, si se desvía más de un 5 %, recalcula la longitud del resto del guion antes de seguir.

=== FASE 6 · MÚSICA Y SONIDO (gratis primero) ===
1) Repositorios libres (Internet Archive, Commons/Musopen, Openverse, Freesound, Incompetech; solo PD, CC0, CC BY). 2) Biblioteca pagada del flow si encaja. 3) Solo si nada sirve, eleven_music una vez.
- Un tema principal con carácter de la época o del lugar y 2-3 camas de apoyo distintas; ninguna cama suena más de 4 min seguidos.
- Efectos de transición: desactivados salvo títulos y cliffhangers; el mismo efecto, como mucho 5 veces por episodio. Descarta cualquier efecto o dron con agudos chirriantes (revisa musica.jpg: nada con energía fuerte por encima de 4 kHz).

=== FASE 7 · ARCHIVO Y METRAJE ===
- 60 % de la pantalla, archivo auténtico de la época: fotografía, prensa, documentos, carteles, película de dominio público. Busca primero por NOMBRE PROPIO (persona, lugar exacto, periódico y fecha) y en inglés y español.
- Vídeo de stock moderno: solo para lugares que se ven hoy y rotulado como tal. Nunca objetos o escenas que se hagan pasar por la época. Lista de clichés prohibidos en este documento.
- Cada recurso, como mucho 2 veces por episodio y con 10 min de separación. Nunca se rellena repitiendo planos: si falta material, tarjeta o plano largo con movimiento.

=== FASE 8 · RECREACIONES (máx. 1 cada 60-90 s) ===
Solo lo que no existe en archivo (o para dar acción, v6). **Weave primero, luego Figma generate_image** (1920x1080). **Nunca ElevenLabs ni otros sitios para imágenes** (decisión del creador, 19-11-2026). Sin rótulo «Recreación». Nunca caras reconocibles ni escritura. Plantilla y criterios en «Manual de vídeo».

=== FASE 9 · CASTING CON FRASE ===
Escribe jobs/<id>/job.json con "stage":"cast". La fábrica alinea la voz palabra a palabra y entrega hojas cast_NN.jpg con cada plano junto a LA FRASE QUE SE OYE mientras sale. Revisa TODAS: rechaza lo que no case con la frase, lo anacrónico, lo moderno, lo repetido, lo de baja calidad, carteles o fotos de otra época. Elige en "picks"/"qpicks". Mira musica.jpg. Copia out/align.json a jobs/<id>/align.json (así el render no vuelve a transcribir). Revisa sincronia.txt y corrige anclas o añade planos.

=== FASE 9 bis · PREVIA (obligatoria desde la v7) ===
Pon "stage":"previa" y empuja. Revisa TODAS las hojas previa_NN.jpg de la rama out-<id>-previa (imagen exacta de cada plano + frase que se oye) y previa_avisos.txt. Corrige y repite la previa hasta que no quede ningún plano incoherente. Solo entonces pon "stage":"render" y empuja.

=== FASE 10 · CONTROL DE CALIDAD (obligatorio, máx. 2 rondas) ===
Une las partes y revisa:
- control.jpg (24 fotogramas) + TODAS las hojas sincronia_NN.jpg (cada plano de persona, lugar o documento con la frase que se oye): ¿coincide lo que se ve con lo que se oye? ¿La foto es de quien dice el rótulo?
- Títulos y rótulos: comprueba con silencedetect que cada título de capítulo cae en una pausa y que cada rótulo coincide con su mención.
- Repeticiones: ningún recurso más de 2 veces.
- Sonido: −16 LUFS, pico −1,5 dB, sin efectos chirriantes repetidos.
Para corregir, usa el modo de re-render parcial o un parche por superposición con una sola recodificación (nunca empalmes HEVC con -c copy).

=== FASE 11 · ENTREGA ===
En la carpeta del proyecto (SendUserFile + device_commit_files):
1) <Título>.mp4 · 2) <Título>.srt · 3) <Título>_miniatura_A.jpg y _B.jpg (fabrica/thumb.py, Design System DocuVox, ver «Miniatura») · 4) <Título>_YouTube.md (paquete SEO completo, ver «Paquete de YouTube») · 5) <Título>_creditos_completos.txt · 6) <Título>_guion.md.
Después, sin esperar respuesta, pasa a la FASE 12.

=== FASE 12 · PUBLICACIÓN EN YOUTUBE, IVOOX, SPOTIFY Y SHORTS (si PUBLICAR: sí) ===
Sigue «Fase final · Publicación automática en YouTube» de este documento: Chrome → Studio → MP4, miniatura B y .srt inyectados desde GitHub → paquete SEO completo → pantalla final → esperar la comprobación → Público → Publicar. Si la comprobación encuentra problemas, NO publiques: deja el vídeo en privado y avísame.
Después publica el episodio en iVoox siguiendo «Fase final · Publicación en iVoox» (MP3 + portada cuadrada, mismo título que en YouTube, Uso de la IA «Sí») y en Spotify siguiendo «Fase final · Publicación en Spotify». Por último monta y programa 5 Shorts siguiendo «Fase final · Shorts de cada documental».
Cierra con el RESUMEN FINAL (plantilla en este documento): enlace del vídeo publicado, duración, créditos de cada servicio, recursos usados y una mejora para el siguiente.

=== REGLAS DE PARADA ===
1) El turno de ARRANQUE. 2) No hay créditos de ElevenLabs suficientes: di cuántos faltan y propón una duración que quepa. 3) Una conexión no responde tras un reintento. 4) El tema exige una decisión que no puedo deshacer. Publicar en YouTube NO es regla de parada si PUBLICAR: sí; sí lo es si la comprobación de derechos de autor encuentra problemas o si PUBLICAR: no. 5) GitHub bloquea el render por facturación: avísame con el enlace a Billing.

TÍTULO:
DURACIÓN:
INDICACIONES:
PUBLICAR: sí
```

## Menú de variantes (qué aplicar según el documental)

Las mejoras de contenido no son obligatorias en todos los episodios. Claude elige según el tema, el público y el formato, y lo anota en `plan.md`. Lo marcado como **siempre** no se negocia.

| Capa | Cuándo se aplica | Cuándo no | Cómo |
| --- | --- | --- | --- |
| Sincronía palabra a palabra | **Siempre** | — | Manual de sincronía |
| Apertura con ancla de notoriedad + cliffhanger + título locutado | **Siempre** | — | Arquitectura de apertura |
| Música y efectos sin repeticiones molestas | **Siempre** | — | Manual de audio |
| Coherencia de metraje y límite de repeticiones | **Siempre** | — | Manual de vídeo |
| Rótulo en cada persona, lugar y documento concretos | **Siempre** la primera vez; luego, si han pasado más de 5 min | — | Rótulo inferior |
| Contexto de entrada «lo que necesitas saber» (60-120 s) | Temas con muchos nombres, siglas o antecedentes (política, guerras, procesos judiciales); público divulgativo | Historias de un solo protagonista o temas muy conocidos | Tras el título, antes del cuerpo |
| Tablero de protagonistas por bandos | 5 o más protagonistas, o dos bandos enfrentados | Uno o dos protagonistas | Tarjeta `cast` y colores fijos por bando |
| Glosario en pantalla (siglas y términos) | Siglas, cargos o instituciones que hoy no se entienden | Temas sin jerga | Chip `gloss` sobre el plano, la primera vez y de recuerdo cada ~10 min |
| Recapitulación cada 8-12 min (15-25 s) | Episodios de más de 25 min o con trama enrevesada | Episodios cortos | Narrador + tarjeta `recap` |
| Reparto de voces completo | Temas con documentos, cartas, discursos o declaraciones reales | Formato B autor-presentador (una sola voz) | Manual de voces |
| Co-narradora | Episodios de más de 40 min, densos y expositivos | Docudrama corto o autor | Alterna bloques de 10-40 s |
| Grafismo denso (≥ 30 % de pantalla) | Temas abstractos, con cifras, votaciones, procesos, mapas | Temas muy visuales con buen archivo | Manual de grafismo |
| Ilustración IA de las pequeñas historias | Muchas anécdotas sin archivo útil | Archivo real abundante y potente | Banco de recursos (v5): estilo distinto en cada episodio |
| Ángulo mito/realidad | Temas trillados en YouTube | Temas poco conocidos | Banco de recursos (v5) |
| Humor puntual | Anécdotas reales absurdas | Temas trágicos | Banco de recursos (v5) |
| Paralelismos con la actualidad | Solo si ayudan a entender y son exactos («coalición de izquierdas», «lo que hoy sería un ministro del Interior») | Nunca para equiparar partidos o personas de entonces con los de hoy | Lenguaje de hoy para describir, no para comparar |

## Arquitectura de apertura

La primera frase engancha el tema con lo más conocido que lo rodea (**ancla de notoriedad**): si el episodio es sobre las elecciones de 1936, la primera frase nombra la Guerra Civil. El espectador sabe en 5 s por qué le importa.

| Tramo | Duración | Qué pasa |
| --- | --- | --- |
| Intro DocuVox | 6,8 s | Siempre igual |
| Gancho | 0-25 s | Ancla de notoriedad + afirmación polémica o cifra imposible, en presente. Frases cortas. Imágenes de máxima fuerza |
| Preguntas | 25-50 s | 2-3 preguntas que el documental va a responder; la última, la grande |
| Cliffhanger + título | 50-65 s | Corte de voz, golpe musical, el narrador dice el título y la tarjeta de título aparece en grande en una pausa propia (3-5 s sin otra voz) |
| Contexto de entrada (si aplica) | 60-120 s | «Para entender lo que pasó, hay que conocer a…»: tablero de protagonistas por bandos, mapa, cronología rápida |
| Cuerpo | — | Microepisodios de 4-6 min, cada uno abre con fecha y lugar y cierra con un gancho |

Ejemplo de gancho válido (tema político): «En julio de 1936 empezó la Guerra Civil española. Cinco meses antes, España había votado. Ganó la izquierda. Pero ¿ganó en las urnas… o en los despachos?». El sensacionalismo vale en la pregunta; la respuesta llega después con rigor.

## Manual de sincronía (la regla número uno)

**El problema que tenía la fábrica:** repartía los planos a partes iguales dentro de cada bloque de voz (bloques de 30-70 s). Si un bloque nombraba a Prieto en el segundo 40, su foto podía salir en el 10. Y cuando faltaban planos, repetía los de stock para rellenar: de ahí el vinilo y el libro una y otra vez.

**Cómo se trabaja ahora:**

1. **Alineación palabra a palabra.** La fábrica transcribe la voz con faster-whisper en GitHub Actions (gratis), con marcas de tiempo por palabra, y la casa con el texto del guion.
2. **Anclas en el guion.** Cada plano lleva `"at": "palabra o frase exacta"`. Empieza 0,1 s antes de esa palabra y dura hasta el siguiente ancla. Los planos sin ancla se reparten entre las anclas.
3. **Rótulos anclados.** `lt` se muestra desde la mención hasta 4 s después, en el plano donde se nombra.
4. **Títulos en unidades propias.** El título del documental y los de capítulo son unidades `T` en la línea de tiempo: llevan su propia pausa, su golpe musical y, si se locutan, su voz. Nunca van dentro de una unidad de narrador.
5. **Cero relleno por repetición.** Si entre dos anclas hay más de 8 s sin plano, la fábrica avisa en el casting y Claude añade una tarjeta o un plano nuevo.
6. **Comprobación automática en el informe:** planos de persona sin mención a ±2 s, títulos con voz debajo, recursos repetidos más de 2 veces.

Regla de escritura: cada persona, lugar, documento o cifra que se nombra lleva su plano con `at`; al menos un plano anclado cada 6-8 s. Si el informe dice que un plano dura más de 8 s, se añade otro plano o una tarjeta, nunca una repetición.

## Manual de voces

Una voz que guía y otras que prueban. Con una sola voz durante 50 minutos suena a lectura; alternar voces no cuesta más créditos, porque se paga por carácter, no por voz.

| Rol | Cuándo | Cómo | Pantalla |
| --- | --- | --- | --- |
| Narrador | Siempre | Grave, sobrio, ~115 ppm en escenas y hasta 160 en tramos expositivos | — |
| Co-narradora | Episodios largos y densos | Alterna bloques de 10-40 s con el narrador | — |
| Voz de documento | Actas, leyes, telegramas, prensa | Neutra, algo más seca | Tarjeta `doc` o `quote` con la fuente |
| Personaje con cita real | Declaraciones, discursos, cartas, diarios de los protagonistas | Una voz fija por personaje, 5-25 s | Foto + nombre + «Palabras de X, fecha» |
| Lectura de historiador | Valoraciones de historiadores reales publicadas | Voz distinta del narrador | «Manuel Álvarez Tardío, historiador · lectura de su libro (año)» |
| Personaje dramatizado | Diálogos de escena que no constan literalmente | Frases de menos de 5 s | «Recreación» siempre visible |

**No se hace nunca:** inventar expertos, testigos o citas. Un experto con voz de IA presentado como real es un testimonio falso y además choca con las normas de YouTube.

**Alternancia que funciona:** pregunta del narrador → respuesta de un documento o un personaje. Afirmación → cita que la demuestra, justo después. El narrador abre y cierra el documental. Objetivo: narrador 60-70 % del habla, otras voces 30-40 % en reparto completo.

**Dinamismo de la locución:** respiraciones de música sola de 6-15 s cada 1-2 min, bloques de 30-60 s tras los ganchos fuertes, frases más cortas en los clímax.

## Manual de accesibilidad y contexto

El objetivo es que un espectador que no sepa nada del tema lo siga, y uno que sepa mucho no se aburra ni encuentre errores.

- **Contexto de entrada** (si aplica): quién gobierna, quién se enfrenta y qué está en juego, en menos de 2 minutos y con grafismo.
- **Tablero de protagonistas:** cada uno con foto real, nombre, cargo y su bando o grupo en un color fijo durante todo el episodio. Cuando vuelve a salir, su rótulo lleva el mismo color.
- **Traducción a lenguaje de hoy:** «la CEDA, la gran coalición de las derechas», «el Frente Popular, la alianza de republicanos de izquierda, socialistas y comunistas». Describe, no equipara con partidos actuales.
- **Repetición útil:** cada 8-10 min, recuerda en una frase quién es quién y en qué punto estamos.
- **Cifras con referencia:** «cincuenta escaños, casi uno de cada nueve del Parlamento».
- **Nivel experto:** quita el contexto de entrada y el glosario y deja los rótulos.

## Manual de grafismo

El grafismo explica lo que la voz no puede: quién es quién, cuándo, dónde y cuánto. Debe sentirse de cadena de televisión: movimiento sobrio, entradas escalonadas y tipografía de la piel del episodio. Nada de plantillas tipo Canva con rebotes o elementos de stock: esa estética delata lo amateur.

**Densidad mínima de grafismo:** 15-20 % de pantalla en temas muy visuales; 30-35 % en temas con muchos nombres, cifras o procesos.

**Tarjetas** (las nuevas están marcadas; ver «Estado del motor»):

| Tarjeta | Para qué |
| --- | --- |
| `title` | Título del documental y de capítulo, siempre en unidad `T` |
| `cast` (nueva) | Tablero de protagonistas: fotos reales, nombre, cargo y bando, agrupados en columnas o en un arco |
| `ficha` | Presentar a un protagonista: foto real a pantalla, nombre y cargo |
| `gloss` (nueva) | Chip superpuesto sobre el plano: «CEDA · coalición de derechas» |
| `recap` (nueva) | Recapitulación: 3-4 puntos con iconos o fotos pequeñas |
| `seats` (nueva) | Hemiciclo o barras de escaños o votos que se dibujan y cambian |
| `versus` (nueva) | Dos bandos enfrentados con sus líderes y cifras |
| `photo` dentro de tarjeta (nueva) | Cualquier tarjeta puede llevar una foto o un vídeo dentro de un marco |
| `quote` | Cita con foto del autor y fuente |
| `doc` | Documento real con acercamiento y subrayado de la frase que se lee |
| `timeline` | Cronología que avanza con la narración, con fotos en los hitos |
| `map` / `mapfly` | Mapa de época o viaje de cámara, con puntos y flechas |
| `board` | Tablero de investigación con hilo rojo |
| `counter` | Cifra que se cuenta sola |
| `split` | Versión oficial frente a pruebas |
| `scan` | Hallazgo marcado sobre una imagen real |
| `list` | Enumeraciones |
| `kw` | Palabra clave a pantalla completa |

**Reglas:** máximo 2 tarjetas seguidas salvo en el contexto de entrada; cada tarjeta, anclada a su frase; títulos de capítulo con locución si el formato lo pide.

## Manual de vídeo

**Reparto de pantalla:** 55-65 % archivo auténtico, 20-35 % grafismo según densidad, 0-15 % recreaciones.

**Archivo auténtico:**

- Busca por nombre propio y fecha antes que por concepto. «Indalecio Prieto 1936» antes que «político socialista».
- Busca en inglés y español; en Commons, categorías antes que texto libre.
- Verifica que es de la época: un cartel de 2001 en un archivo provincial no es de 1936. La miniatura no basta: mira el título, la fecha y la descripción del archivo.
- No dejes que coincida por error en el nombre del autor: «Leon Caceres» no es Cáceres.

**Vídeo de stock:**

- En temas históricos, solo para lugares que siguen ahí, rotulados con «Hoy» o con su nombre actual.
- Nada de color moderno haciéndose pasar por la época, aunque se pase a blanco y negro.

**Clichés prohibidos** (salvo que el tema trate de ellos): tocadiscos o vinilo girando, libro abriéndose, reloj de arena, mazo de juez, lupa sobre papel, máquina de escribir moderna, manos sobre teclado, ojos en primer plano, banderas ondeando en CGI, mapas antiguos genéricos de otra zona, humo genérico como plano principal.

**Repeticiones:** cada recurso como mucho 2 veces, con 10 min de separación. Las fotos de rostro, solo cuando se habla de esa persona.

**Recreaciones:** sin caras ni escritura; manos, espaldas, sombras, objetos y contraluces; dirección de fotografía en el prompt; atrezo verificado; 2,5-3 s; siempre entre dos planos reales.

**Rótulos inferiores:** persona (nombre + cargo + color de bando), lugar (nombre + fecha), documento (título + archivo), «Hoy» para el vídeo actual. Las recreaciones IA van **sin rótulo** (decisión del creador, 19-11-2026). Los títulos de mapa sin flechas «→»: la fuente no las tiene (salen como un cuadro); usar «De Madrid a Cartagena».

## Manual de audio

**Voz:**

- Una toma por unidad.
- Tempo 0,90 y silencios alargados (pause_stretch 0,45, tope 0,6 s).
- Huecos de 1,5 s tras el narrador y de 1,0 s tras una cita.
- Ritmo real medido en el episodio 2: 116 palabras/min de media, incluidas las pausas.

**Niveles:**

| Capa | Nivel |
| --- | --- |
| Voz | −20 dB RMS |
| Cama bajo la voz | −35 a −37 dB (≈ 7 dB por debajo en percepción) |
| Música sola en respiraciones y títulos | −22 dB |
| Efectos | −28 a −32 dB |
| Máster | −16 LUFS, pico −1,5 dB |

**Música:**

- Tema principal con carácter de la época o del lugar (en el episodio 2, la *Leyenda* de Albéniz funcionó muy bien).
- 2-3 camas de apoyo que cambian por capítulo.
- Respiraciones de música sola cada 1-2 min.

**Efectos:**

- `auto_sfx` desactivado por defecto: en el episodio 2, el mismo golpe de aire sonaba en cada una de las 57 tarjetas y era el sonido chirriante que molestaba.
- Solo golpe grave en títulos y cliffhangers.
- Foley en recreaciones.
- El mismo efecto como mucho 5 veces.
- Nada con agudos fuertes por encima de 4 kHz.

**Prohibido:** mezclar en ElevenLabs, música NC/ND/SA, regenerar música de la biblioteca.

## Miniatura DocuVox

Se entregan dos variantes (A y B) para el experimento A/B de YouTube, en 1280×720.

- **Imagen:** foto real de archivo en blanco y negro, contraste alto. La A con un rostro protagonista en primer plano a la derecha; la B con una escena o un objeto clave. Fondo de textura de documento oscurecida si suma.
- **Texto:** la palabra clave del tema en Barlow Condensed Black blanca y grande (2-3 palabras), y la segunda parte en la caja amarilla #F2FF00 con letra negra. Ejemplo: «PUCHERAZO» / «DEL 36». El texto lo dicta la búsqueda (FASE 1) y lo que pida el creador; no repite el título del vídeo palabra por palabra si el creador no lo pide.
- **Línea secundaria:** Barlow Condensed SemiBold gris claro, mayúsculas, con el punto amarillo.
- **Marca:** logo DocuVox horizontal arriba a la izquierda, pequeño.
- **Composición:** texto a la izquierda sobre un degradado negro, foto a la derecha. Esquina inferior derecha libre (ahí va la duración).
- **Nunca:** caras generadas por IA, texto pequeño ilegible en móvil, más de 5 palabras.

Comprueba la legibilidad reduciéndola a 320×180 antes de entregar.

## Paquete de YouTube (SEO)

El archivo `<Título>_YouTube.md` lleva, investigado con vidIQ y la búsqueda de YouTube:

| Campo | Contenido |
| --- | --- |
| Títulos | 3 opciones de menos de 60 caracteres, con la palabra clave al principio y la puntuación de vidiq_score_title. Recomendada + alternativa para el A/B |
| Texto de miniatura | Para A y B |
| Descripción | 2 primeras líneas con gancho y palabra clave (es lo que se ve sin desplegar) + qué vas a ver + capítulos con minutos + fuentes principales + créditos de música e imágenes con atribución + 3 hashtags |
| Comentario fijado | Pregunta que invite a comentar + créditos completos |
| Etiquetas | Llenar hasta ~480/500 caracteres: el tema concreto + los grandes términos de búsqueda vecinos que el público ya busca (p. ej. guerra civil, guerra civil española, franco, franquismo para un episodio de 1936) + protagonistas + fechas + «documental», «documental historia». Sin etiquetas genéricas vacías (tips, viral, tutorial) |
| Hashtags | Al final de la descripción, 8-10. Los 3 primeros salen encima del título: tema amplio + nicho + #documental (ej. #guerracivil #historiadeespaña #documental) |
| Ajustes | Categoría Educación, idioma Español (España), no creado para niños, sin promoción de pago, uso de IA «No», capítulos automáticos desactivados, remixes solo audio, subtítulos con el .srt |
| Uso de IA | **Siempre «No»** (decisión fija del creador, 18-11-2026) |
| Pantalla final | Dónde colocar los elementos (los 15 s finales del vídeo) |

## Fase final · Publicación automática en YouTube

Probado el 19-11-2026 con *Vivir al límite* (58:34, 347 MB): https://youtu.be/WYUMTJsk4GA

**Por qué así.** La ventana de Windows para elegir archivos no la puede manejar Claude, y la herramienta `file_upload` de Claude in Chrome solo admite 3,8 MB. La solución es que **la propia página de YouTube Studio descargue los archivos desde GitHub** (raw.githubusercontent.com permite la descarga desde Studio) y los meta en el formulario con `DataTransfer`. Requisito: la rama `out-<id>` debe poder leerse sin sesión (repositorio público). vidIQ no sube vídeos.

**Requisitos en el PC del creador:** Chrome abierto, extensión Claude in Chrome conectada con la misma cuenta de Claude, sesión de YouTube en el canal **DocuVox - Documentales Sonoros** (UCKTktSCfWs-X8rpq-tjFV6A), sin paneles de vidIQ encima de Studio.

1. **Abrir Studio en una pestaña nueva** del grupo de Claude: `https://studio.youtube.com/channel/UCKTktSCfWs-X8rpq-tjFV6A/videos/upload?d=ud` (abre directamente el diálogo de subida). Comprobar en la captura que el canal es DocuVox. **No usar el menú «Crear»**: un clic desplazado pidió por error acceso a emisiones en directo.
2. **Descargar el vídeo dentro de la página** (las partes de 90 MB de la rama de salida) y crear el archivo:
```js
window.__st='descargando';(async()=>{const b='https://raw.githubusercontent.com/xvlerma/fabrica-documentales/out-<id>/<id>.mp4.part0';const p=[];for(let i=0;i<N_PARTES;i++){const r=await fetch(b+i);p.push(await r.blob());window.__st='parte '+(i+1);}window.__vid=new File(p,'<Título>.mp4',{type:'video/mp4'});window.__st='OK '+window.__vid.size;})();
```
   Consultar `window.__st` cada pocos segundos (sin bucles largos: más de 45 s bloquean la herramienta). ≈1 min para 350 MB.
3. **Inyectar el vídeo** en `input[type=file][name=Filedata]` con `DataTransfer` + evento `change`. La subida empieza al momento (≈3-4 min) y el borrador se guarda en privado.
4. **Detalles** (dentro de `ytcp-uploads-dialog`):
   - Título: triple clic en el cuadro, `ctrl+a`, escribir con `type`.
   - Descripción: foco en el segundo `#textbox` y `document.execCommand('insertText', …)` (respeta los saltos de línea). Comprobar longitud.
   - Miniatura: descargar `<id>_miniatura_B.jpg` de la rama de salida e inyectarla en el `input` con `accept="image/jpeg,image/png"`. Comprobar que aparece «Miniatura subida».
   - Radios por JS (y leer `aria-checked`): `VIDEO_MADE_FOR_KIDS_NOT_MFK`, `VIDEO_PAID_PRODUCT_PLACEMENT_NO`, `VIDEO_HAS_ALTERED_CONTENT_NO` (decisión fija del creador), `REMIX_SOURCE_OPTION_VISUAL_OPT_OUT_AND_PERFORM_ACTIONS` («Permitir solo remixes del audio»).
   - «Mostrar más» → desmarcar «Permitir capítulos automáticos».
   - Etiquetas: para cada una, `input.value = etiqueta`, evento `input` y `keydown` Enter (crea los chips de golpe).
   - Idioma: desplegable → «Español (España)». Categoría: «Educación».
5. **Elementos del vídeo:**
   - Subtítulos → Añadir → Subir archivo → «Con tiempos» marcado → inyectar el .srt (descargado de la rama de salida) en `#captions-file-loader` → Hecho.
   - Pantalla final → Añadir → plantilla «1 vídeo, 1 suscribirse» → Guardar.
6. **Ojo (ep. 4):** en el diálogo de subida «Público» puede venir **marcado por defecto**: al pulsar «Guardar» el vídeo se publica. Si se quiere dejar en privado mientras se revisa, marcar «Privado» explícitamente antes de guardar.
   **Visibilidad:** marcar Público y esperar a que la comprobación diga **«No se han encontrado problemas»** (≈15-20 min en 60 min de vídeo; YouTube avisa de posibles faltas si se publica antes). Entonces **Publicar**. Si la página se bloquea, ir a `studio.youtube.com/video/<id>/edit` → «Editar borrador» → paso Visibilidad.
7. **Cierre:** guardar el enlace en `<Título>_YouTube.md`, darlo en el RESUMEN FINAL y cerrar la pestaña.

**Permiso para publicar.** El sistema de seguridad de Claude puede frenar el clic final de «Publicar» si no ve una autorización clara del creador. Por eso el prompt lleva `PUBLICAR: sí`. Si aun así se bloquea, Claude deja todo listo, avisa con el enlace y el creador solo pulsa Publicar.

**Plan B sin el PC encendido (pendiente de configurar):** publicación desde GitHub Actions con la API de YouTube (`fabrica/publish.py`): sube, pone miniatura y subtítulos y programa la salida a las 18:00 de Madrid. Necesita una autorización única del creador (proyecto de Google Cloud, cliente OAuth en modo «En producción» y los secrets `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`, que el creador pega él mismo en GitHub). Riesgo sin confirmar: Google puede dejar en privado los vídeos de proyectos de la API sin auditar; el script lo detecta y avisa.

## Fase final · Publicación en iVoox

Probado el 19-11-2026 con *Vivir al límite* (episodio 3 del programa «DocuVox | Documentales sonoros»). Se hace justo después de YouTube, en la misma sesión de Chrome.

1. **Preparar en el workspace:** MP3 a 128 kbps estéreo (`ffmpeg -i <id>.mp4 -vn -b:a 128k <id>.mp3` con etiquetas ID3) y **portada cuadrada 1400×1400** con el diseño de la miniatura subida a YouTube (logo, texto grande, caja amarilla, foto a la derecha). Subir los dos a la rama `out-<id>` para que la página pueda descargarlos.
2. **Abrir** `https://podcasters.ivoox.com/#/episodes/upload` (no ivoox.com/upload). Programa «DocuVox | Documentales sonoros» ya marcado → Continuar.
3. **Audio:** descargar el MP3 dentro de la página (`fetch` a raw.githubusercontent.com) e inyectarlo en el `input[type=file]` de audio. La subida tarda ≈1-2 min (56 MB).
4. **Portada:** inyectar la portada en el `input` con `accept="image/*"` → aparece un recorte → **Recortar** con todo el cuadrado.
5. **Campos (SEO iVoox):**
   - **Título: el mismo que en YouTube** (decisión del creador).
   - Descripción: primera frase con las palabras clave que busca la gente (p. ej. «pueblo más frío del mundo», «ciudad más alta del mundo»), los lugares o protagonistas en lista, capítulos `00:00` con el nombre de cada lugar, enlace al vídeo de YouTube, invitación a seguir DocuVox, fuentes y créditos. Sin mencionar voces sintéticas.
   - **Uso de la IA: «Sí»** (decisión del creador, 19-11-2026, para todos los episodios).
   - Género «Documentales y TV» · Idioma «Castellano» · **Categoría según el tema** (no siempre Historia: p. ej. «Ciencia y Cultura / Viajes y lugares» para geografía) · **5 etiquetas** (el máximo), concretas y buscadas · Tipo «Completo» · nº de episodio.
   - Los campos de texto se rellenan con el *setter* nativo + eventos `input`/`change`; las etiquetas, escribiendo cada una + Intro.
6. **Continuar → paso «Compartir»:** marcar «Acepto los Términos y Condiciones de uso de iVoox» y **Publicar**. Aparece «¡Enhorabuena! Tu episodio se ha creado correctamente»; el audio se procesa en unos minutos.

## Fase final · Publicación en Spotify

Programa creado el 19-11-2026 en Spotify for Creators, alojado en Spotify (no por RSS de iVoox, para no duplicar programas): **«DocuVox | Documentales sonoros en español»** (id `0ljuy4XAHcWJft9Ts6ZAKd`), categoría «Documentales», idioma español, portada de marca DocuVox (`docuvox_portada_programa.jpg`, 3000×3000). Episodios publicados el 19-11-2026: 1 *Vivir al límite*, 2 *Termópilas*, 3 *El pucherazo del 36* (v2). Se hace después de iVoox, en la misma sesión de Chrome.

1. **Abrir** `https://creators.spotify.com/pod/show/0ljuy4XAHcWJft9Ts6ZAKd/episode/wizard`.
2. **Audio:** descargar el MP3 de la rama `out-<id>` dentro de la página e inyectarlo en `#uploadAreaInput`.
3. **Detalles:**
   - Título: **el mismo que en YouTube**.
   - Descripción (editor enriquecido): **clic real en el editor → teclas `ctrl+a` y `Supr` → pegar** con un evento `paste` (`ClipboardEvent` con `DataTransfer` de texto). Sin el clic y el borrado previos, o con `execCommand`, el texto se ve pero el contador queda en 0 y el campo sale «Obligatorio». Comprobar que el contador marca los caracteres. Misma descripción SEO que en iVoox (sin la lista de créditos: el límite es 4.000 caracteres).
   - **Alternativa probada en el ep. 4 (navegador integrado):** poner la pestaña al frente (`tabs_select`), enfocar el editor por JS (`ed.focus()` + `Range` al final) y escribir con la acción `type`; el contador sube bien. Los clics por coordenadas pueden dejar el foco en el título.
   - Si la página se queda en blanco o vuelve al paso de carga, recargar la URL del borrador (`…/episode/<id>/wizard`): el audio se conserva o hay que reinyectarlo.
   - Portada del episodio: la portada cuadrada, inyectada en el `input` de imagen → «Guardar» en el recorte.
   - Temporada 1 y número de episodio (correlativo en Spotify), tipo «Completo», contenido explícito y promocional «No».
4. **Siguiente → Revisar:** «Ahora» → **Publicar**. Aparece «¡Se ha publicado el episodio!».
5. Pendiente de la primera publicación (ya resuelto): el email de la cuenta de Spotify tiene que estar verificado; si no, el episodio se queda en borrador.

## Fase final · Shorts de cada documental

Objetivo: llevar espectadores al documental largo (vale mucho más por hora vista) y hacer crecer el canal. Los Shorts por sí solos pagan poco. 0 créditos: todo sale del vídeo ya montado.

1. **Elegir 5 momentos** (uno por gancho fuerte: un dato récord, una pregunta, un giro), de 35 a 60 s, cortando en frases completas con el `.srt`/`align.json`.
2. **Montaje vertical 1080×1920** en el workspace (ffmpeg, ligero): fondo del propio plano desenfocado y oscurecido, vídeo 16:9 centrado, logo DocuVox arriba, **gancho arriba** (línea blanca grande en Barlow Black + caja amarilla #F2FF00), **subtítulos grandes** en mayúsculas (Barlow Condensed ExtraBold), «DOCUMENTAL COMPLETO EN EL CANAL» en amarillo los últimos 6 s, fundido de entrada y salida. Sin símbolos que la fuente no tenga (▶ sale como un cuadro).
3. **Subir** igual que el documental (descarga desde la rama `out-<id>` dentro de Studio e inyección en `Filedata`). Título con el gancho + palabra clave + `#shorts`; descripción de 1-2 líneas + enlace al documental + hashtags; 10 etiquetas; no creado para niños; sin promoción; Uso de IA «No»; español (España); Educación.
4. **Publicar los 5 a la vez y en público** en cuanto el documental esté publicado (decisión del creador, 19-11-2026). Si hubiera que programar, como mucho a 30 min. En la página de edición de cada Short, rellenar **«Vídeo relacionado»** con el documental largo para que el toque lleve al documental; poner además el enlace en la descripción («▶ Documental completo (1 hora): …»).
   - «Vídeo relacionado» da «Vaya, se ha producido un error» si el Short aún se está procesando: esperar 2-3 min y repetir, y **comprobar recargando** la página de edición que se ha guardado.
   - Cortar los Shorts de tramos sin escenas IA (mirar `edl.json`/hojas): así «Uso de IA: No» es cierto.
5. **Trucos de Studio comprobados (19-11-2026):** título y descripción con un `Range` sobre el propio `#textbox` + `insertText` (`execCommand('selectAll')` selecciona toda la página); fecha y hora de «Programar» con triple clic en sus cajas + escribir + Intro; si sale «Aún estamos comprobando tu contenido», pulsar «Entendido» (la programación sigue). El idioma se puede dejar sin poner en los Shorts.
6. **Trucos comprobados en el ep. 4 (navegador integrado):**
   - El título que se escribe por JS justo tras inyectar el archivo **se pisa con el nombre del archivo**: esperar ~10 s, clic real en el título y escribir.
   - Al escribir «#» en la descripción se abre la lista de hashtags y **bloquea el guardado** («Guardando…» sin fin): cerrarla con un clic fuera del cuadro. **No pulsar Escape**: abre «Cancelar la subida».
   - El botón Publicar tarda hasta 30 s en activarse mientras se crea el enlace.
7. **Requisito:** la extensión vidIQ desactivada en Chrome. Su panel bloquea a Claude en Studio, sobre todo en «Visibilidad» y en la página de edición.

## Resumen final (plantilla)

Al terminar, en un mensaje:

| Concepto | Dato |
| --- | --- |
| Enlace de YouTube | https://youtu.be/… (publicado / pendiente y por qué) |
| iVoox | Episodio publicado (nº y categoría) |
| Spotify | Episodio publicado (nº) |
| Duración final | 00:00 (objetivo: 00 min) |
| ElevenLabs | Créditos gastados en voz, imágenes y música · saldo restante |
| Figma | Imágenes generadas (cupo) |
| vidIQ | Créditos gastados |
| GitHub Actions | Minutos de render usados |
| Música | Pistas usadas, fuente y licencia (0 créditos si son libres) |
| Archivo | Nº de imágenes y vídeos por fuente (Commons, BNE, Europeana…) |
| Recreaciones | Cuántas y con qué |
| Entregables | Lista de archivos en la carpeta |
| Mejora para el siguiente | Una línea |

## Arquitectura

Claude piensa, escribe y elige en la conversación; todo lo pesado (descargas, alineación de voz, 2,5D, grafismo, mezcla, codificación) ocurre gratis en GitHub Actions; el resultado llega a la carpeta del proyecto sin pasar por las manos del creador.

Secuencia: **arranque** (carpeta + briefing) → referencia y SEO → documentación → diseño del episodio → guion con anclas → voz → **casting con frase** (GitHub) → **previa plano a plano** (GitHub) → **render en partes** (GitHub) → control de calidad → miniaturas y paquete de YouTube → entrega → **publicación en YouTube, iVoox y Spotify** (Chrome) → resumen.

## Conexiones, cuentas y secretos

| Pieza | Dónde | Para qué | Cuota |
| --- | --- | --- | --- |
| ElevenLabs | Conector · plan Creator | Solo voz y música en último recurso (**nunca imágenes**, v6) | 125.822 créditos/mes |
| Figma | Conector · fichero iQVFmIETOISH9JHOXbZXHv | Recreaciones | Cupo IA diario (01:00) |
| GitHub | Conector · cuenta xvlerma | Fábrica y render (Actions) | Plan gratuito: 12 $ de Actions al mes en repo privado (un episodio de 60 min con pruebas lo agota). Repo público = gratis |
| Claude in Chrome | Extensión en el Chrome del PC | Publicar en YouTube Studio con la sesión del creador | — |
| vidIQ | Conector | SEO y transcripción de referencia | Según plan |
| `PIXABAY_API_KEY`, `FREESOUND_API_KEY`, `EUROPEANA_API_KEY` | Secrets del repo | Stock, sonido, archivo europeo | Gratis |
| App de escritorio | Tu PC | Carpeta del proyecto y navegador integrado | — |

| Elemento | Id |
| --- | --- |
| Narrador | EtnizbrIk2nKCZCt0zqW |
| Voces secundarias probadas | v2UIb6nJm38uahTHNpTv · nMvZRihyU408YNgNXHuX · T9kg8O6bvv6gT3lruF5p · BXtvkfRgOYGPQKVRgufE (femenina) |
| Flow | ZekaAXXDjF9lP4OrbYzm |
| Intro | assets/intro/docuvox.mp4 (6,8 s) |
| Marca | assets/brand (logo, mosca, Barlow Condensed) |

Las claves no están en este documento: viven en los secrets del repositorio.

## Referencia técnica: el job.json

Campos de la v2 que se mantienen:

- `id`, `title`, `stage`, `theme`, `brand`, `music`, `audio`, `intro`, `must`, `overlays`, `cold_secs`, `chapters`, `picks`, `qpicks`, `rev`.
- Codificación: `parts`, `codec: "hevc"`, `max_kbps`, `audio_kbps`.

Novedades v3:

| Campo | Qué es |
| --- | --- |
| `align` | `true`: alinea la voz palabra a palabra (faster-whisper) y activa las anclas. `align_model`: `base` (por defecto) o `small` |
| `"at"` en un plano | Palabra o frase exacta de la unidad donde empieza el plano |
| Unidad `T` | Título o capítulo con pausa propia: `{"k": "T", "card": {...}, "secs": 4, "voice": "url opcional", "sting": "pista"}` |
| `bando` | Paleta por grupo: `{"izquierda": [r,g,b], "derecha": [r,g,b]}`; los rótulos y `cast` lo usan |
| `auto_sfx` | `{}` por defecto (sin golpes automáticos) |
| `reuse` | `{"max": 2, "gap_secs": 600}` límite de repeticiones |
| `no_pad` | `true`: prohibido rellenar repitiendo planos |
| `only` | Re-render parcial: **no implementado en el motor** (ver v7) |

## Estado del motor

Implementado y probado el 18 de noviembre de 2026 con un documental de prueba de 3,7 minutos (`jobs/prueba_sync`), reutilizando voz ya generada, sin gastar créditos.

| Pieza | Estado | Cómo se usa |
| --- | --- | --- |
| Alineación palabra a palabra (faster-whisper `base`, gratis en el runner) | **Hecha** | `"align": true`. Escribe `align.json` en la salida. Cópialo a `jobs/<id>/align.json` tras el casting para que el render no vuelva a transcribir |
| Anclas `at` en los planos | **Hecha** | El plano empieza 0,1 s antes de la palabra (`anchor_lead`). Los planos sin ancla se reparten entre anclas sin salir de su unidad |
| Rótulos con color de bando | **Hecha** | `lt: ["Nombre", "cargo", "izquierda"]` + `"bando": {"izquierda": [r,g,b], …}`. `lt_at` retrasa su entrada |
| Unidad `T` (título o capítulo con pausa propia) | **Hecha** | `{"k": "T", "secs": 5, "sting": "tema", "chapter": true, "card": {...}}`. Opcional `url`/`text` para que el narrador lo diga. Los capítulos `chapter` van solos a `capitulos.txt` |
| Sin relleno por repetición | **Hecha** | `"no_pad": true` (implícito con `align`) |
| Límite de repeticiones | **Hecha** | `"reuse": {"max": 2, "gap": 600}`. Avisa en el informe si no hay alternativa |
| Golpes automáticos | **Hechos** | `auto_sfx` vacío por defecto; `sfx_max` (5) por efecto |
| Glosario en pantalla | **Hecho** | `"gloss": ["CEDA", "la gran coalición de las derechas católicas", "derecha"]`, `gloss_at`, `gloss_dur` |
| Tarjetas `cast`, `seats`, `versus`, `recap` y `ficha` con foto | **Hechas** | Cualquier objeto de una tarjeta con `commons` o `image` se descarga (fotos dentro del grafismo) |
| Casting con frase | **Hecho** | Cada fila de `cast_NN.jpg` lleva la frase que se oye |
| Informe y hojas de sincronía | **Hechos** | `sincronia.txt` (rótulo sin mención, título con voz debajo, plano de más de `max_shot` s) y `sincronia_NN.jpg` (fotograma + frase de cada plano de persona, lugar o documento). Revisarlas es obligatorio en el control de calidad |
| Subtítulos a la palabra | **Hechos** | El `.srt` usa los tiempos reales de cada frase |
| Miniatura DocuVox | **Hecha** | `python fabrica/thumb.py salida.jpg --foto … --grande … --caja … --sub … [--fondo …] [--recorte x0,y0,x1,y1]`. Genera también `_mini.jpg` (320×180) para comprobar la lectura en móvil |
| Re-render parcial `only` | Pendiente | Mientras tanto: parche por superposición con una sola recodificación |

Lo que la prueba confirmó: las fotos, rótulos y tarjetas aparecen en la palabra exacta; el título dicho por el narrador sale mientras lo dice; el capítulo va en su pausa. Lo que sigue dependiendo de Claude es **elegir bien cada imagen**: la hoja de sincronía lo deja a la vista, pero alguien tiene que mirarla.

## Errores conocidos y cómo evitarlos

| Fallo | Causa | Solución |
| --- | --- | --- |
| ≈ 6.600 créditos gastados mezclando | Montaje en el sandbox de ElevenLabs | Todo el montaje en GitHub Actions |
| El render no arranca tras cambiar código | El workflow solo mira `jobs/*/job.json` | Subir `rev` |
| «Forbidden» al descargar voz | URLs de ElevenLabs caducadas | URLs frescas + caché por id |
| Clips sin relación o con CGI | Búsqueda a ciegas en stock | Archivo primero + revisión de cada plano |
| MP4 de más de 400 MiB | Límite de entrega | HEVC a 750 kbps (50 min ≈ 300 MB) |
| Render de 50 min demasiado largo para un runner | Un solo trabajo | `parts: 4` en paralelo (≈ 75 min) |
| Wikimedia devuelve 429 | Demasiadas peticiones | Espaciado de 0,6 s y reintentos |
| **Fotos y rótulos desfasados respecto a la voz** (ep. 2) | Planos repartidos a partes iguales en bloques de 30-70 s | Alineación palabra a palabra + anclas |
| **Título del documental en mitad de una frase** (ep. 2) | El título iba dentro de una unidad de narrador | Unidad `T` en pausa propia |
| **Vinilo y libro repetidos** (ep. 2) | El motor rellenaba repitiendo planos de stock | `no_pad` + `reuse` + clichés prohibidos |
| **Tocadiscos a color cuando se hablaba de telégrafos** (ep. 2) | Búsqueda por concepto genérico y stock moderno | Búsqueda por nombre propio y revisión plano contra frase |
| **Cartel de 2001 como «Cáceres 1936»** (ep. 2, 10 planos) | Un archivo provincial con carteles modernos; otra búsqueda coincidió por el nombre del autor | Verificar fecha y descripción del archivo, no solo la miniatura |
| **Sonido chirriante repetido** (ep. 2) | Golpe de aire automático en las 57 tarjetas | `auto_sfx` desactivado y tope de 5 usos |
| **50,8 min en vez de 60** (ep. 2) | Guion escrito corto: 5.900 palabras en vez de ~7.000 | Contar palabras antes de generar la voz: 116 × min |
| **Narración monótona** (ep. 2) | Narrador el 90 % del tiempo | Reparto de voces y respiraciones musicales |
| **Público perdido con nombres y siglas** (ep. 2) | Sin contexto de entrada ni glosario | Capa de accesibilidad |
| **Cargo cortado en la ficha de Portela** (prueba v3) | El texto del cargo no se ajustaba al ancho | Todas las tarjetas ajustan el cuerpo y saltan de línea solas (hasta 3 líneas); aun así, cargos de menos de 60 caracteres |
| **El casting se colgó 45 min** (ep. 3) | Reintentos largos ante errores 4xx de Openverse | Sin reintentos en 400/401/403/404/410/424 |
| **El render cayó en dos partes** (ep. 3) | Tarjeta `doc` sin imagen | `f_doc` dibuja tarjeta tipográfica si no hay imagen |
| **Imágenes ajenas al lugar** (Putin, aviones, sellos, Lima, Caracas…) (ep. 3) | Búsquedas por nombre de lugar devuelven de todo | Lista de palabras prohibidas y selección por lugar antes del render |
| **Oimiakón sin fotos libres e imágenes sin relación con la locución** (ep. 3; el creador lo calificó de los peores en imagen) | Regla «sin SA» + relleno genérico + candidatos mal filtrados | CC BY-SA permitido, búsqueda por lugar en varios idiomas, `coherencia.py`, IA o tarjeta para lo que falte y revisión visual de todas las hojas antes de publicar |
| **Yakutsk repetida 4-5 veces** (ep. 3) | Pocas fotos libres del lugar | Más candidatos (Openverse) o más grafismo en ese tramo |
| **El montaje final no arrancó** (ep. 3) | Cupo gratuito de Actions agotado (12 $) | Repo público o presupuesto de Actions |
| **Ventana de otra extensión bloqueó a Claude en Studio** (ep. 3) | Panel de vidIQ encima de Studio | Desactivar vidIQ en Studio; si pasa, recargar `video/<id>/edit` → «Editar borrador» |
| **Fotos ajenas a la frase** (ep. 4): recortes de natación, anuncio naviero con esvásticas, tropas de Franco para aviones republicanos, feria «Meet me in Paris», negativo invertido, Kremlin actual con bandera rusa | El primer candidato de cada búsqueda y rotaciones con material de relleno | Mapa manual `fix.py` y revisión de las 27-35 hojas `sincronia_NN.jpg`; se corrigió y se volvió a renderizar |
| **≈130 planos fijos de más de 11 s** (ep. 4, 38 de 60 min) | Pocas imágenes por unidad | Segundo plano automático a mitad de frase desde `edl_prev.json` |
| **Contadores «7.049» o «503» en las hojas** (ep. 4) | La hoja captura el contador a mitad de animación | No es un fallo: el número final es el correcto |
| Empalmar HEVC con `-c copy` rompe el vídeo | Fotogramas que dependen de otros en el corte | Parche por superposición con una recodificación, o re-render parcial |

## Costes y tiempos

Medido en el episodio 2: ≈ 710 caracteres (créditos de voz) por minuto de documental.

| Duración | Voz (créditos) | Render en GitHub | Tiempo total aprox. |
| --- | --- | --- | --- |
| 10 min | ≈ 7.100 | ≈ 20-30 min | ≈ 2 h |
| 25 min | ≈ 17.800 | ≈ 45-60 min | ≈ 3-4 h |
| 40 min | ≈ 28.500 | ≈ 60-75 min (4 partes) | ≈ 4-5 h |
| 60 min | ≈ 42.700 | ≈ 75-90 min (4 partes) | ≈ 5-6 h |

- Con 125.822 créditos al mes caben unos 4 episodios de 40 min o 2 de 60 min (más recreaciones si se usa ElevenLabs).
- Alternar varias voces no sube el coste: se paga por carácter.
- Episodio 2: 36.207 créditos de voz, 0 de música, 0 imágenes generadas.

## Adaptar a otros nichos

| Nicho | Piel | Archivo auténtico | Capa de accesibilidad típica | Voces típicas | Grafismo estrella |
| --- | --- | --- | --- | --- | --- |
| Antigüedad | `antiguo` | Grabados, museo, fotos del XIX | Mapa + cronología | Narrador + fuentes clásicas leídas | `mapfly`, `timeline`, `doc` |
| Edad Media | `medieval` | Manuscritos, mapas antiguos | Mapa + dinastías | Narrador + crónicas leídas | `mapfly`, `cast`, `doc` |
| Siglos XIX-XX, guerras y política | `guerra_moderna` | Fotografía y prensa de época, película PD | **Completa**: contexto, bandos, glosario, recaps | Reparto completo | `cast`, `seats`, `versus`, mapas de frentes |
| Crímenes y misterios | `crimen` | Documentos judiciales, prensa | Tablero de implicados | Narrador + declaraciones reales | `board`, `scan`, `split` |
| Ciencia y exploración | `ciencia` | NASA, ESA, diarios de expedición | Glosario técnico | Narrador + co-narradora | `counter`, esquemas |
| Biografías | `biografia` | Retratos, cartas, lugares | Cronología vital | Narrador + cartas del protagonista | `ficha`, `timeline`, `doc` |
| Asia | `oriente` | Ukiyo-e, fotos del XIX | Mapa + nombres | Narrador + textos clásicos | `mapfly`, `timeline` |

Lo único fijo en cualquier nicho es la capa DocuVox (intro, mosca, punto amarillo en los rótulos, pantalla final y miniatura) y las reglas de sincronía.

## Anexo · Auditoría de *El pucherazo del 36* (episodio 2)

| Área | Nota | Qué funcionó | Qué falló y dónde se corrige |
| --- | --- | --- | --- |
| Guion | 8 | Riguroso, con fuentes, nombres y estudios; se entiende solo escuchando | Sin ancla de notoriedad (apenas nombra la Guerra Civil) y sin contexto para quien no conoce el tema → Arquitectura de apertura y capa de accesibilidad |
| Montaje | — | Mucho archivo real | Fotos de rostro sin rótulo ni relación con la voz → Manual de sincronía |
| Grafismo | — | Estilo correcto | Insuficiente para un tema con tantos nombres y siglas → densidad mínima y nuevas tarjetas |
| Metraje | — | Archivo bien tratado | Stock moderno a color, clichés repetidos, cartel de 2001 → Manual de vídeo |
| Sincronía | — | — | Títulos y rótulos desfasados, título en mitad de una frase → unidad `T` y anclas |
| Locución | — | Narrador sólido | Monótono, pocas voces → Manual de voces |
| Música | — | Albéniz muy acertado | Golpe de aire chirriante en cada tarjeta → `auto_sfx` desactivado |
| Intro | — | Intro DocuVox con locución, muy bien | — |
