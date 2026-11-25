# fabrica/anim · Animaciones explicativas DocuVox (Manim)

Módulo reutilizable para explicar mecanismos (repartos de escaños, instituciones, datos, mapas) con animaciones propias, sincronizadas palabra a palabra con la locución. Se estrenó en «Cómo funciona REALMENTE España» (nov 2026).

## Piezas

| Archivo | Qué hace |
|---|---|
| `docuanim.py` | Estilo, utilidades y escenas (Manim Community 0.22) |
| `prep_mapas.py` | Convierte Natural Earth (dominio público) en JSON compactos en `data/` (mundo, Europa, provincias de España con su comunidad, Alemania, Suiza, EE. UU.) |
| `render.py` | Renderiza escenas: `python render.py <jobdir> <l\|h> [Escena …]` (`l` = vista previa, `h` = 1080p30). `ANIM_JOBS=2` en paralelo |
| `data/*.json` | Mapas ya preparados |

Instalación (Linux): `apt-get install libpango1.0-dev libcairo2-dev pkg-config` y `pip install manim geopandas`. Copiar las Barlow de `assets/brand` a `~/.fonts`. Pango no tiene el peso «BLACK»: se usa «HEAVY».

## Estilo

Fondo azul noche `#0A1424`, acento `#3D8BFF`, oro `#F2C14E`, aviso `#E76F51`; tipografía Barlow grande (legible en móvil). Partidos **ficticios** A-E en colores neutros (A `#2EC4B6`, B `#E9C46A`, C `#9AA8BD`, D `#B5838D`, E `#5F6B7A`): nunca colores de partidos reales.

## Sincronía con la voz

Cada escena hereda de `DocuScene`, que lee `ANIM_CUES` (JSON `{dur, t, p}`):
- `t`: diccionario `nombre → segundo` en el que debe arrancar cada paso; en la escena se usa `self.go('nombre')` antes de cada animación y `self.avail()` para repartir el tiempo hasta el siguiente paso.
- `dur`: duración total del plano (voz + 4 s de cola); `self.end()` rellena hasta ahí.
- `p`: parámetros de la escena (p. ej. `Ficha` recibe país, coordenadas, cifra y líneas).

Los tiempos salen de `voz_words.json` (palabras de faster-whisper por unidad). En el job: `cue = (t_palabra − t_ancla) / tempo + 0.1`. Con `tempo` distinto de 1 usar `pause_stretch: 0` para que no se desplacen. Ejemplo en `jobs/comoespana/build.py` (`A(name, at=…, cues=dict(paso='palabra exacta'))`; la búsqueda de palabras es secuencial). `python build.py cues` escribe `anim/cues/*.json`; luego `render.py`.

En el job, cada animación es un plano `{"file": "media/<id>/anim/<Escena>.mp4", "start": 0, "grade": false, "at": "…"}`. `grade: false` evita la corrección de color y la viñeta del motor.

## Utilidades

`T()` texto · `num_es()` números con formato español · `hemicycle()/seat_colors()/dhondt()` hemiciclos y reparto D'Hondt con barrera · `map_group()/world()/europe()/world_proj()` mapas (con `shift` para recolocar Canarias, Alaska…) · `pin`, `chip`, `card`, `arrow`, `bar_h`, `legend` · `self.header()` título con barra azul · `self.source()` fuente y año en una esquina.

## Escenas disponibles

Hemiciclo · DhondtVotos · DhondtTabla · SoriaMadrid · Mayoritario · TresSistemas · ColegioElectoral · OrganigramaEspana · Comparativa · Monarquias · Reinos · Reformas · Tribunales · Mocion · Impeachment · Autonomias · Federales · Cien · Intereses · Deuda · PresionFiscal · UnionEuropea · Euro · BrexitONU · Ficha (genérica: país + cifra) · Repeticion · Recap · Suma.

Para reutilizar: copiar una escena parecida, cambiar textos y datos (siempre con fuente y año en `self.source()`), renderizar en `l`, revisar fotograma a fotograma (sin solapes, sin texto cortado, mosca DocuVox libre arriba a la derecha) y después en `h`.
