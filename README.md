# Fábrica de documentales

Del manifiesto `jobs/<id>/job.json` al documental terminado, con vídeo real libre (Pixabay, Wikimedia, Internet Archive, Europeana), archivo de museos (Cleveland, Met), efectos (Freesound), grafismo animado propio y la locución de ElevenLabs.

- Motor: `fabrica/engine.py` · fuentes: `fabrica/sources.py` · grafismo: `fabrica/cards.py`
- Al subir un `job.json`, GitHub Actions fabrica el vídeo y publica la salida en la rama `out-<id>` (vídeo en trozos de 90 MB, subtítulos, capítulos, créditos, hoja de control).
