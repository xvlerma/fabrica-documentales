# Lista master de recursos DocuVox

Fuentes gratuitas, orden de uso y condición de cada una. El control automático está en `fabrica/licencias.py`.

## Reglas fijas
1. **Ficha de cada recurso**: URL de la ficha, autor, licencia, fecha de descarga y crédito exacto. La fábrica la escribe en `out/licencias.json`.
2. **Si un recurso necesita crédito y no lo tiene, el episodio no se publica.** Mira `out/licencias_estado.txt`: debe decir `PUBLICAR: SÍ`.
3. **Un único máster para YouTube e iVoox**: música, efectos y audio de archivo deben valer para los dos destinos. La imagen basta con que valga para YouTube, salvo la **miniatura**, que también va a iVoox en versión cuadrada.
4. **Orden de producción**: música elegida y con licencia verificada → material real → mapa y archivo → stock de apoyo → diseño sonoro y mezcla → subida en privado y revisión de las comprobaciones de Studio.
5. Antes de publicar, pega `out/creditos_publicos.txt` en la descripción de YouTube **y** de iVoox.

## 1. Lugar, persona o hecho real (siempre primero)
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | Wikimedia Commons | Ficha original: autor, procedencia y licencia | `{"commons": "File:..."}` o `{"photo": "...", "src": "commons"}` |
| 2 | Archivo local o institución de origen | Rige su licencia. Openverse solo para localizar | `{"url": "...", "fuente": "<fuente>", "title": "...", "license": "...", "credit": "..."}` |

## 2. Archivo español
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | Biblioteca Digital Hispánica (BNE) | CC BY 4.0. Crédito obligatorio: «Imágenes procedentes de los fondos de la Biblioteca Nacional de España» | `{"bne": "URL de la imagen", "title": "...", "page": "ficha"}` |
| 2 | Hemeroteca Digital (BNE) | Mismo crédito. Que el periódico sea antiguo no libera todo su contenido: revisa la ficha y los derechos de terceros | igual |
| 3 | CNIG | Crédito del producto | `{"url": "...", "fuente": "cnig", "title": "..."}` |

## 3. Cine antiguo, propaganda y archivo industrial
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | National Screening Room (Library of Congress) | Derechos de cada película, incluida la banda sonora, y alcance territorial | `{"url": "...", "fuente": "loc"}` |
| 2 | Prelinger Archives (Internet Archive) | Lo mismo (la fábrica avisa) | `{"video": "...", "old": true}` |
| 3 | US National Archives | Lo mismo | `{"url": "...", "fuente": "nara"}` |

## 4. Arte, grabados, objetos y foto de época
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | Europeana | Manda la etiqueta de cada objeto (sin NC) | `"src": "europeana"` |
| 2 | The Met Open Access | Solo CC0 o dominio público | `"src": "met"` |
| 3 | Smithsonian Open Access | CC0 | `{"url": "...", "fuente": "smithsonian"}` |
| 4 | Rijksmuseum | Dominio público o CC0 | `{"url": "...", "fuente": "rijksmuseum"}` |
| 5 | Library of Congress Free to Use | Solo «No known restrictions» (la búsqueda filtra) | `"src": "loc"` |
| — | Cleveland Museum of Art | CC0 | `"src": "cleveland"` |

En `{"photo": "...", "src": "europeana,met,loc,commons"}` el orden de `src` es el orden de búsqueda.

## 5. Mapas y satélite
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | Natural Earth | Dominio público. Base de los mapas propios | tarjetas `map` / `mapfly` (ya integrado) |
| 2 | Landsat (EarthExplorer, USGS) | Dominio público. Compara fechas solo si el cambio se ve en el vídeo | `{"url": "...", "fuente": "landsat"}` |
| 3 | Copernicus Browser | Reconocimiento del producto | `{"url": "...", "fuente": "copernicus", "title": "Sentinel-2, 2024"}` |
| 4 | Sanborn Maps | Ciudades históricas de EE. UU. | `{"url": "...", "fuente": "loc"}` |

## 6. Espacio, clima y naturaleza
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | NASA Scientific Visualization Studio | Mayoritariamente dominio público; revisa el material de terceros | `{"url": "...", "fuente": "nasa"}` |
| 2 | NASA Image Library | Lo mismo (la búsqueda descarta lo marcado como de terceros) | `"src": "nasa"` en `photo` o `video` |
| 3 | ESO / ESA-Hubble | Crédito visible según la ficha | `{"url": "...", "fuente": "eso" \| "esahubble", "title": "..."}` |
| 4 | NOAA / USGS Multimedia | Océanos y geología | `{"url": "...", "fuente": "noaa" \| "landsat"}` |

## 7. Planos de apoyo y foto actual (solo relleno)
| # | Fuente | Condición | En job.json |
|---|---|---|---|
| 1 | Pexels | Sin crédito. Cuidado con marcas y personas identificables | automático con `PEXELS_API_KEY` |
| 2 | Coverr | Descarta los clips IA, premium y patrocinados (la fábrica avisa) | `{"url": "...", "fuente": "coverr"}` |
| 3 | Mixkit Video | Solo Free License | `{"url": "...", "fuente": "mixkit_video"}` |
| 4 | Pixabay | Para ampliar | automático |
| 5 | Dareful | CC BY 4.0, con crédito | `{"url": "...", "fuente": "dareful", "title": "..."}` |
| — | Unsplash | Foto fija | `{"url": "...", "fuente": "unsplash"}` |

Orden automático de búsqueda de vídeo: `pexels,pixabay,pixabay_must,commons,archive` (cámbialo con `"src"`; añade `nasa` para espacio).

## 8. Música (se elige antes del montaje)
| # | Fuente | Condición | En job.json (`music` / `beds`) |
|---|---|---|---|
| 1 | **Mixkit Music (Free License)** | Por defecto. Sin crédito. No registrarla en Content ID, ni usarla en pistas solo musicales ni en TV/radio | `{"mixkit": "URL del mp3", "title": "..."}` |
| 2 | **Scott Buckley (CC BY 4.0)** | Tono cinematográfico. Crédito en las dos descripciones desde la primera subida | `{"buckley": "URL del mp3", "title": "..."}` |
| 3 | Incompetech (CC BY) | Crédito escrito + línea locutada al cierre de iVoox (`out/locucion_cierre.txt`) | `{"incompetech": "Título exacto"}` |
| 4 | Biblioteca de audio de YouTube, solo pistas CC | Copia el texto del icono CC (va en `credit`) | `{"url": "...", "fuente": "youtube_cc", "credit": "texto completo del icono CC"}` |
| ✕ | Biblioteca de YouTube, licencia estándar | Solo para piezas exclusivas de YouTube: **bloquea** el máster | `"fuente": "youtube_std"` |
| ✕ | Pixabay Music | Último recurso (la fábrica avisa) | `"fuente": "pixabay_music"` |
| — | Archive / Commons / Openverse / Freesound | Dominio público, CC0 o CC BY sin NC/ND/SA (ya integrado) | `{"search": "...", "src": "archive,commons,openverse,freesound"}` |

Las pistas sin ficha (`"tema": "https://..."` sin `fuente` ni `license`) bloquean la publicación; las de ElevenLabs no se revisan.

## 9. Ambientes, maquinaria e impactos
| # | Fuente | Condición |
|---|---|---|
| 1 | Sonniss GDC Bundle | Editar e integrar sí; no venderlos ni redistribuirlos sueltos; no usarlos para entrenar IA. Guarda la licencia junto a cada lote (sube los sonidos a `assets/sfx/sonniss/`) |
| 2 | Freesound | Solo CC0 o CC BY (ya integrado en `sfx`) |
| 3 | Mixkit SFX | Free License |
| 4 | 99Sounds | Términos de cada paquete |
| 5 | ZapSplat Basic | Solo si aceptas el crédito «Sound effects obtained from https://www.zapsplat.com» |

## Plantilla de créditos (la genera `creditos_publicos.txt`)
```
Música: [Título] by Scott Buckley – released under CC-BY 4.0. www.scottbuckley.com.au
Música: [Título] Kevin MacLeod (incompetech.com) – Licensed under Creative Commons: By Attribution 4.0
Imágenes procedentes de los fondos de la Biblioteca Nacional de España
Vídeo: [Título] — Dareful (CC BY 4.0)
[Título] — ESO   ·   [Título] — ESA/Hubble
Sound effects obtained from https://www.zapsplat.com
```
Los créditos públicos no mencionan voces sintéticas ni ElevenLabs.

## Sin verificar (reglas prudentes ya aplicadas)
- Si la licencia vigente de Sonniss es la v2.0 de agosto de 2026.
- Si Incompetech exige locutar el crédito en pódcast.
