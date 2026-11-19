# Fábrica de documentales DocuVox

- Recursos, licencias y créditos: sigue `docs/RECURSOS.md` (lista master). El control está en `fabrica/licencias.py`.
- Modo seguro activado por defecto: no uses fuentes vetadas (Coverr, Pixabay Music, Openverse/ccMixter, música de Internet Archive, Biblioteca de YouTube estándar, licencias NC/ND/SA). Marca `"revisado": true` solo tras comprobar de verdad la ficha.
- Al preparar un job: elige la música primero (Mixkit Music por defecto; Scott Buckley si hace falta tono cinematográfico) y da a cada recurso manual su `"fuente"`.
- Antes de publicar un episodio: `out/licencias_estado.txt` debe decir `PUBLICAR: SÍ`. Si dice `NO`, corrige los bloqueos y relanza; no publiques.
- Pega `out/creditos_publicos.txt` en la descripción de YouTube y de iVoox. Si existe `out/locucion_cierre.txt`, esa línea va locutada al cierre de la versión de iVoox.
- Los créditos públicos nunca mencionan voces sintéticas ni ElevenLabs.
