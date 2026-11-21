#!/usr/bin/env python3
"""Paquete de YouTube/iVoox/Spotify de «Las estafas más grandes de la historia». Uso: python3 paquete.py <carpeta_out>
Escribe youtube.md, descripcion_youtube.txt, comentario_fijado.txt, descripcion_podcast.txt y etiquetas.txt."""
import os, sys

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
caps = open(f'{OUT}/capitulos.txt', encoding='utf-8').read().strip()
cred = [l for l in open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().splitlines() if l.strip() and l.strip() != 'Créditos']
FULL = 'https://github.com/xvlerma/fabrica-documentales/blob/out-estafas/creditos_publicos.txt'

TITULO = 'Las estafas más grandes de la historia: de Ponzi a Madoff'
ALT = ['De Ponzi a Madoff: las estafas que engañaron al mundo', 'Fórum Filatélico, Madoff, Ponzi: así te engañan']
TAGS = ['estafas más grandes de la historia', 'madoff', 'bernie madoff', 'estafa piramidal', 'esquema ponzi', 'charles ponzi',
        'fórum filatélico', 'forum filatelico', 'afinsa', 'gescartera', 'victor lustig', 'torre eiffel vendida', 'ivar kreuger',
        'gregor macgregor', 'poyais', 'estafas famosas', 'fraude financiero', 'esquema piramidal', 'harry markopolos',
        'estafa sellos', 'cnmv', 'chiringuitos financieros', 'cómo detectar una estafa', 'historia de las estafas',
        'documental estafas', 'documental', 'historia en español', 'true crime', 'docuvox']
def compact(l):
    p = [x.strip() for x in l.split(' · ')]
    if len(p) >= 2:
        head, lic = p[0], p[1]
        if ' — ' in head: tit, aut = head.split(' — ', 1)
        else: tit, aut = head, ''
        tit = tit.replace('Archivo: ', '')[:48]
        return f'{tit} — {aut[:40]} ({lic})' if aut else f'{tit} ({lic})'
    return l[:100]

desc = f"""Un hombre del que se fiaba todo Wall Street confesó en 2008: «Todo es una gran mentira». No era el primero. Esta es la historia de las mayores estafas de la historia, contada como un expediente: quién las montó, cómo funcionaban y por qué tanta gente lista cayó.

En este documental:
· Gregor MacGregor y Poyais, el país que nunca existió (Londres, 1822)
· Charles Ponzi y los cupones de correo que dieron nombre al esquema (Boston, 1920)
· Victor Lustig, el hombre que «vendió» la Torre Eiffel (París, 1925)
· Ivar Kreuger, el rey de las cerillas y su imperio de papel (1932)
· Gescartera, Fórum Filatélico y Afinsa: los sellos que no valían nada (España, 2001-2006)
· Bernie Madoff, el analista que lo vio venir y la mayor estafa piramidal conocida (Nueva York, 2008)
· Las señales que se repiten en todas, para que no te pase a ti

Capítulos
{caps}

Fuentes principales: sentencias de la Audiencia Nacional y del Tribunal Supremo (Fórum Filatélico, Afinsa, Gescartera), CNMV, informes de la SEC y de su Inspector General (2009), testimonio de Harry Markopolos ante el Congreso (2009), hemeroteca del Boston Post (1920), David Sinclair (The Land That Never Was), Mitchell Zuckoff (Ponzi's Scheme), Jeff Maysh y Floyd Miller sobre Victor Lustig, Frank Partnoy (The Match King) y Diana B. Henriques (The Wizard of Lies).

{CRED}

Este vídeo es divulgación histórica, no asesoramiento financiero. Antes de invertir, consulta el registro de entidades autorizadas de la CNMV.

Suscríbete a DocuVox para más historias reales.

#estafas #madoff #forumfilatelico #esquemaponzi #documental #historia #truecrime"""

CRED = open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().strip()
desc = desc.replace('{CRED}', CRED)
if len(desc) > 4950:   # límite de YouTube: créditos completos en el comentario fijado y enlace
    desc = desc.replace(CRED, 'Créditos de imagen y música (autor y licencia): en el comentario fijado y completos en ' + FULL)
com = '¿Conoces a alguien que cayera en una de estas? Cuéntalo abajo 👇\n\nCréditos de imagen (autor y licencia):\n' + '\n'.join(compact(l) for l in cred)
com = com[:9800]

pod = f"""Las estafas más grandes de la historia, de Ponzi a Madoff: el país inventado de Poyais, los cupones de Charles Ponzi, la Torre Eiffel «vendida» por Victor Lustig, el imperio de cerillas de Ivar Kreuger, Gescartera, Fórum Filatélico y Afinsa, y la confesión de Bernie Madoff. Documental sonoro de 46 minutos.

{caps}

Versión en vídeo: busca «DocuVox» en YouTube. Sigue DocuVox para más historias reales.

{CRED}"""

open(f'{HERE}/descripcion_youtube.txt', 'w').write(desc)
open(f'{HERE}/comentario_fijado.txt', 'w').write(com)
open(f'{HERE}/descripcion_podcast.txt', 'w').write(pod)
open(f'{HERE}/etiquetas.txt', 'w').write(','.join(TAGS))
md = f"""# Las estafas más grandes de la historia · paquete de YouTube

**Título (recomendado):** {TITULO}  ({len(TITULO)} caracteres)
**Alternativas A/B:** {ALT[0]} · {ALT[1]}

**Etiquetas** ({len(','.join(TAGS))} caracteres): {', '.join(TAGS)}

**Ajustes:** Educación · Español (España) · no creado para niños · sin promoción pagada · Uso de IA: No · capítulos automáticos desactivados · subtítulos estafas.srt · pantalla final 1 vídeo + suscribirse

## Descripción ({len(desc)} caracteres)

{desc}

## Comentario fijado ({len(com)} caracteres)

{com}
"""
open(f'{HERE}/youtube.md', 'w').write(md)
print(len(desc), len(com), len(pod), len(','.join(TAGS)))
