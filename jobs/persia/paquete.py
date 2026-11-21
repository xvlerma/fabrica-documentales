#!/usr/bin/env python3
"""Paquete de YouTube/iVoox/Spotify de «El Imperio Persa». Uso: python3 paquete.py <carpeta_out>
Escribe youtube.md, descripcion_youtube.txt, comentario_fijado.txt, descripcion_podcast.txt y etiquetas.txt."""
import os, sys

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
caps = open(f'{OUT}/capitulos.txt', encoding='utf-8').read().strip()
cred = [l for l in open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().splitlines() if l.strip() and l.strip() != 'Créditos']
FULL = 'https://github.com/xvlerma/fabrica-documentales/blob/out-persia/creditos_publicos.txt'

TITULO = 'El Imperio Persa: la historia que 300 no te contó'
ALT = ['Los villanos de 300 no eran así: la verdad del Imperio Persa']
TAGS = ['imperio persa', 'persia', 'jerjes', 'ciro el grande', 'darío', 'darío i', 'persépolis', 'inmortales persas', 'termópilas',
        'esparta', '300', 'alejandro magno', 'imperio aqueménida', 'aqueménidas', 'cilindro de ciro', 'batalla de maratón',
        'salamina', 'heródoto', 'camino real persa', 'historia antigua', 'historia de persia', 'leónidas', 'gaugamela',
        'mitos de la historia', 'documental historia', 'documental', 'historia en español', 'docuvox']

def compact(l):
    p = [x.strip() for x in l.split(' · ')]
    if len(p) >= 2:
        head, lic = p[0], p[1]
        if ' — ' in head: tit, aut = head.split(' — ', 1)
        else: tit, aut = head, ''
        tit = tit.replace('Archivo: ', '')[:48]
        return f'{tit} — {aut[:40]} ({lic})' if aut else f'{tit} ({lic})'
    return l[:100]

desc = f"""La historia del Imperio Persa sin los mitos de la película 300: Ciro, Darío, Jerjes, los Inmortales y la caída ante Alejandro Magno. Lo que Grecia nunca contó de su gran enemigo.

En 300 son monstruos sin rostro. Pero en Persépolis los obreros cobraban un sueldo y las mujeres que acababan de dar a luz recibían raciones extra: lo dicen miles de tablillas de barro. Este documental cuenta el imperio más grande de su tiempo con las dos versiones delante: lo que contó Grecia y lo que dicen las piedras.

En este documental:
· Ciro el Grande y su cilindro: ¿la primera declaración de derechos humanos? (y por qué los historiadores lo discuten)
· Cambises, Egipto y el ejército que se tragó el desierto
· Darío: Behistún, el Camino Real, el correo más rápido de la Antigüedad y la moneda de oro
· Maratón contada desde el otro lado
· Jerjes contra Grecia: el mar azotado, Termópilas vista desde el lado persa, Salamina y Platea
· Los Inmortales y la vida real en Persépolis
· El oro persa que decidió las guerras griegas
· Alejandro Magno, Gaugamela y la noche en que ardió Persépolis
· Lo que dejó Persia

Capítulos
{caps}

Si viste nuestro documental sobre Termópilas, este es el otro lado de la historia. Próximo episodio de la serie: Cartago, la ciudad que Roma necesitó borrar del mapa.

Fuentes principales: Heródoto (Historias), Esquilo (Los persas), Jenofonte (Anábasis y Ciropedia), Arriano (Anábasis de Alejandro), Plutarco (Vidas), la inscripción de Behistún, el Cilindro de Ciro y la Crónica de Nabonido (British Museum), las tablillas del Archivo de Fortificación de Persépolis (Oriental Institute de Chicago), Pierre Briant (From Cyrus to Alexander), Amélie Kuhrt (The Persian Empire) y Lloyd Llewellyn-Jones (Persians: The Age of the Great Kings).

{{CRED}}

Suscríbete a DocuVox para más historias reales.

#imperiopersa #historiaantigua #300"""

CRED = open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().strip()
desc = desc.replace('{CRED}', CRED)
if len(desc) > 4950:   # límite de YouTube: créditos completos en el comentario fijado y enlace
    desc = desc.replace(CRED, 'Créditos de imagen y música (autor y licencia): en el comentario fijado y completos en ' + FULL)
com = '¿Qué versión te habían contado tú, la de 300 o la de las piedras? Cuéntalo abajo 👇\n\nCréditos de imagen (autor y licencia):\n' + '\n'.join(compact(l) for l in cred)
com = com[:9800]

dur = ''
try:
    import json
    dur = f" de {round(json.load(open(f'{OUT}/informe.json')).get('dur', 0) / 60)} minutos"
except Exception: pass
pod = f"""El Imperio Persa sin los mitos de la película 300: Ciro el Grande y su cilindro, Darío y el Camino Real, Jerjes, Termópilas y Salamina vistas desde el otro lado, los Inmortales, las tablillas de Persépolis y la caída ante Alejandro Magno. Documental sonoro{dur}.

{caps}

Versión en vídeo: busca «DocuVox» en YouTube. Próximo episodio: Cartago. Sigue DocuVox para más historias reales.

{CRED}"""

open(f'{HERE}/descripcion_youtube.txt', 'w').write(desc)
open(f'{HERE}/comentario_fijado.txt', 'w').write(com)
open(f'{HERE}/descripcion_podcast.txt', 'w').write(pod)
open(f'{HERE}/etiquetas.txt', 'w').write(','.join(TAGS))
md = f"""# El Imperio Persa · paquete de YouTube

**Título (recomendado):** {TITULO}  ({len(TITULO)} caracteres)
**Alternativa A/B:** {ALT[0]}
**Miniaturas A/B:** persia_miniatura_A.jpg (retrato de Jerjes) · persia_miniatura_B.jpg (relieves de Persépolis)

**Etiquetas** ({len(','.join(TAGS))} caracteres): {', '.join(TAGS)}

**Ajustes:** Educación · Español (España) · no creado para niños · sin promoción pagada · Contenido alterado o sintético: No · capítulos automáticos desactivados · subtítulos persia.srt · lista «Civilizaciones antiguas» · pantalla final: Termópilas + suscribirse

## Descripción ({len(desc)} caracteres)

{desc}

## Comentario fijado ({len(com)} caracteres)

{com}
"""
open(f'{HERE}/youtube.md', 'w').write(md)
print(len(desc), len(com), len(pod), len(','.join(TAGS)))
