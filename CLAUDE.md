# Fábrica de documentales DocuVox

- Recursos, licencias y créditos: sigue `docs/RECURSOS.md` (lista master). El control está en `fabrica/licencias.py`.
- Modo seguro activado por defecto: no uses fuentes vetadas (Pexels, Coverr, Jamendo, BBC SFX, Pixabay Music, Openverse/ccMixter, música de Internet Archive, Biblioteca de YouTube estándar, licencias NC/ND; SA solo en música). Marca `"revisado": true` solo tras comprobar de verdad la ficha.
- Al preparar un job: elige la música primero (Mixkit Music por defecto; Scott Buckley si hace falta tono cinematográfico) y da a cada recurso manual su `"fuente"`.
- Antes de publicar un episodio: `out/licencias_estado.txt` debe decir `PUBLICAR: SÍ`. Si dice `NO`, corrige los bloqueos y relanza; no publiques.
- Pega `out/creditos_publicos.txt` en la descripción de YouTube y de iVoox. Si existe `out/locucion_cierre.txt`, esa línea va locutada al cierre de la versión de iVoox.
- Los créditos públicos nunca mencionan voces sintéticas ni ElevenLabs.
- CC BY-SA está permitido en imagen y vídeo con crédito (19-11-2026), no en música ni en la miniatura.
- Coherencia imagen-locución: cada plano debe enseñar lo que dice la frase. Después del casting ejecuta `fabrica/coherencia.py` y revisa TODAS las hojas `cast_NN.jpg`. Lo que no tenga material coherente pasa a imagen IA (escenas, sin caras reconocibles) o a mapa/tarjeta (datos y cifras). Nunca relleno genérico ni rótulo de lugar sobre algo que no es ese lugar.
- Tras el render, revisa todas las `sincronia_NN.jpg`: si hay planos que no encajan con la frase, corrige y vuelve a renderizar antes de publicar.
