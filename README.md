# Fábrica de documentales

Motor que convierte un `jobs/<id>/job.json` en un documental terminado (MP4 1080p, subtítulos, capítulos y créditos), usando GitHub Actions.

- Manual completo, prompt maestro y referencia del job: documento maestro v4 (`Fabrica_de_documentales_Documento_maestro_v4.md`).
- Ejemplo completo y probado: `jobs/prueba03/job.json`.

## Flujo
1. Empujar `jobs/<id>/job.json` con `"stage": "cast"` → la rama `out-<id>` recibe `cast_NN.jpg` y `cast.json` (8 candidatos por plano).
2. Copiar los candidatos elegidos en `"picks"` (clave = número de plano; valor = candidato de cast.json o `{"spec": {...}}`), poner `"stage": "render"` y empujar.
3. La rama `out-<id>` recibe `<id>.mp4.partNN`, `.srt`, `capitulos.txt`, `creditos.txt`, `control.jpg`, `edl.json`, `informe.txt`, `run.log` y el control de licencias: `licencias_estado.txt` (PUBLICAR: SÍ/NO), `licencias.json`, `creditos_publicos.txt` y, si procede, `locucion_cierre.txt`.
4. Solo se publica con `PUBLICAR: SÍ`. Fuentes y reglas: `docs/RECURSOS.md`.

El workflow solo arranca si cambia un `job.json`: para relanzar sin otros cambios, subir `"rev"`.

## Módulos
- `fabrica/engine.py`: audio (voz al 96 %, pausas alargadas, camas, interludios, efectos, máster −16 LUFS), guion visual, casting, render por plano, montaje.
- `fabrica/parallax.py`: cámara 2,5D con mapa de profundidad, tratamiento de película para recreaciones, cámara al hombro, cambio de foco, parpadeo de llama.
- `fabrica/cards.py`: grafismo animado: title, ficha, quote, list, timeline, map, mapfly, scan, doc, board, counter, split, palabra clave y rótulo inferior.
- `fabrica/sources.py`: Pixabay, Wikimedia Commons, Internet Archive, Europeana, Cleveland, The Met, NASA, Library of Congress, Freesound, Openverse, Incompetech; fuentes por URL (Mixkit, Scott Buckley, BNE, Dareful, Coverr, ESO, Sonniss…); caché por id.
- `fabrica/licencias.py`: registro de fuentes, bloqueos de licencia y créditos públicos para YouTube e iVoox (`docs/RECURSOS.md`).

Secrets necesarios: `PIXABAY_API_KEY`, `FREESOUND_API_KEY`, `EUROPEANA_API_KEY`.
