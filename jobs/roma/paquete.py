#!/usr/bin/env python3
"""Paquete de YouTube/iVoox/Spotify de «La Antigua Roma». Uso: python3 paquete.py <carpeta_out>
Escribe youtube.md, descripcion_youtube.txt, comentario_fijado.txt, descripcion_podcast.txt y etiquetas.txt."""
import os, sys

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
caps = open(f'{OUT}/capitulos.txt', encoding='utf-8').read().strip()
cred = [l for l in open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().splitlines() if l.strip() and l.strip() != 'Créditos']
FULL = 'https://github.com/xvlerma/fabrica-documentales/blob/out-roma/creditos_publicos.txt'

TITULO = 'La Antigua Roma: Historia Completa (sin mitos de Hollywood)'
ALT = ['Historia de Roma completa: lo que Hollywood no te contó', 'La Antigua Roma en 1 hora: la historia REAL']
TAGS = ['antigua roma', 'historia de roma', 'roma historia completa', 'imperio romano', 'república romana', 'historia antigua',
        'julio césar', 'augusto', 'aníbal', 'cartago', 'nerón', 'calígula', 'coliseo', 'gladiadores', 'pompeya', 'caída de roma',
        'caída del imperio romano', 'espartaco', 'cleopatra', 'marco aurelio', 'constantino', 'hispania romana', 'mitos de la historia',
        'legiones romanas', 'senado romano', 'imperio romano de occidente', 'roma antigua documental', 'historia en español', 'historia real', 'documental', 'documental historia', 'documental roma']

def compact(l):
    p = [x.strip() for x in l.split(' · ')]
    if len(p) >= 2:
        head, lic = p[0], p[1]
        if ' — ' in head: tit, aut = head.split(' — ', 1)
        else: tit, aut = head, ''
        tit = tit.replace('Archivo: ', '')[:48]
        return f'{tit} — {aut[:40]} ({lic})' if aut else f'{tit} ({lic})'
    return l[:100]

desc = f"""¿Y si casi todo lo que crees saber de la Antigua Roma viniera de Hollywood? La historia completa de Roma, de la loba a la caída, contada con las fuentes antiguas y separando cada mito de lo que de verdad pasó.

En este documental:
· Cómo una aldea de cabañas en el Palatino conquistó el Mediterráneo
· Aníbal, Cannas y la guerra que casi borra a Roma del mapa
· Julio César, los piratas, el Rubicón y los idus de marzo (y sus verdaderas últimas palabras)
· Augusto, Calígula, Nerón y el incendio de Roma: lo que dicen Tácito y Suetonio
· La Roma de la calle: grafitos de Pompeya, termas, esclavos, mujeres y pan y circo
· La crisis del siglo III, Constantino y la caída de Occidente en 476… que casi nadie notó
· Por qué Roma, en realidad, nunca murió

Capítulos
{caps}

Fuentes principales: Polibio, Tito Livio, Plutarco, Suetonio, Tácito, Plinio el Joven, Res Gestae Divi Augusti, Corpus Inscriptionum Latinarum (CIL IV y VI), Edward Gibbon y Mary Beard (SPQR).

Música: Mixkit (licencia Mixkit). Imágenes de archivo de Wikimedia Commons y museos con licencias abiertas; la lista completa de autores y licencias está en el comentario fijado.
Ilustraciones de escenas: recreaciones artísticas, no imágenes de época.

Suscríbete a DocuVox para más historia real, sin mitos.

#antiguaroma #historiaderoma #documental #imperioromano #juliocesar #historia #roma #historiaantigua"""

com = 'Si pudieras viajar a un momento de la historia de Roma, ¿cuál elegirías? 👇\n\nCréditos de imagen (autor y licencia):\n' + '\n'.join(compact(l) for l in cred)
assert len(com) <= 9800, len(com)

pod = f"""La historia completa de la Antigua Roma, sin mitos: de la fundación en el Palatino a la caída del Imperio romano de Occidente, contada con las fuentes antiguas. Documental sonoro de una hora.

Protagonistas: Rómulo, Aníbal, Escipión, Espartaco, Cicerón, Julio César, Cleopatra, Augusto, Calígula, Nerón, Vespasiano, Trajano, Marco Aurelio, Diocleciano, Constantino, Alarico, Atila y Rómulo Augústulo.

{caps}

Versión en vídeo, con mapas e imágenes: busca «DocuVox» en YouTube. Sigue DocuVox para más historia real.

Fuentes: Polibio, Tito Livio, Plutarco, Suetonio, Tácito, Plinio el Joven, Res Gestae, CIL, Gibbon, Mary Beard. Música: Mixkit. Créditos de imagen: en el comentario fijado del vídeo de DocuVox en YouTube."""

open(f'{HERE}/descripcion_youtube.txt', 'w').write(desc)
open(f'{HERE}/comentario_fijado.txt', 'w').write(com)
open(f'{HERE}/descripcion_podcast.txt', 'w').write(pod)
open(f'{HERE}/etiquetas.txt', 'w').write(','.join(TAGS))
md = f"""# La Antigua Roma (Historia Completa) · paquete de YouTube

**Título (recomendado):** {TITULO}  ({len(TITULO)} caracteres)
**Alternativas A/B:** {ALT[0]} · {ALT[1]}

**Miniatura B (subida):** «HOLLYWOOD / TE MINTIÓ», Pollice Verso de Gérôme a color · **Miniatura A:** «ROMA / NUNCA CAYÓ», Coliseo

**Etiquetas** ({len(','.join(TAGS))} caracteres): {', '.join(TAGS)}

**Ajustes:** Educación · Español (España) · no creado para niños · sin promoción pagada · Uso de IA: No (ilustraciones claramente dibujadas) · capítulos automáticos desactivados · remixes solo audio · subtítulos roma.srt · pantalla final 1 vídeo + suscribirse

## Descripción ({len(desc)} caracteres)

{desc}

## Comentario fijado ({len(com)} caracteres)

{com}
"""
open(f'{HERE}/youtube.md', 'w').write(md)
print(len(desc), len(com), len(pod), len(','.join(TAGS)))
