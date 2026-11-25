#!/usr/bin/env python3
"""Paquete de YouTube/iVoox/Spotify de «El corralito argentino». Uso: python3 paquete.py <carpeta_out>
Escribe youtube.md, descripcion_youtube.txt, comentario_fijado.txt, descripcion_podcast.txt y etiquetas.txt."""
import os, sys

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
caps = open(f'{OUT}/capitulos.txt', encoding='utf-8').read().strip()
cred = [l for l in open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().splitlines() if l.strip() and l.strip() != 'Créditos']

TITULO = 'El corralito argentino: el día que los bancos se quedaron tu dinero (¿podría pasar en España?)'
ALT = ['Corralito: el día que Argentina no pudo sacar su dinero del banco (¿y en España?)',
       'Corralito 2001: 250 pesos a la semana, cinco presidentes y un helicóptero']
TAGS = ['corralito', 'corralito argentina', 'corralito 2001', 'crisis argentina 2001', 'crisis de 2001', 'historia argentina',
        'de la rua helicoptero', 'domingo cavallo', 'uno a uno', 'convertibilidad', '19 y 20 de diciembre', 'cacerolazo',
        'pesificacion', 'corralon', 'duhalde', 'plan bonex', 'crisis bancaria uruguay 2002', 'corralito españa',
        'puede haber un corralito en españa', 'fondo de garantia de depositos', 'preferentes', 'banco popular',
        'chipre corralito', 'grecia corralito', 'crisis economica', 'documental', 'docuvox']

def compact(l):
    p = [x.strip() for x in l.split(' · ')]
    if len(p) >= 2:
        head, lic = p[0], p[1]
        if ' — ' in head: tit, aut = head.split(' — ', 1)
        else: tit, aut = head, ''
        tit = tit.replace('Archivo: ', '')[:48]
        return f'{tit} — {aut[:40]} ({lic})' if aut else f'{tit} ({lic})'
    return l[:100]

desc = f"""1 de diciembre de 2001. Argentina se despierta y descubre que solo puede sacar 250 pesos a la semana de su propia cuenta. Es el corralito. En veinte días habrá saqueos, estado de sitio, un presidente huyendo en helicóptero desde la azotea de la Casa Rosada y cinco presidentes en dos semanas. Después llegaron el corralón y la pesificación, y millones de ahorradores perdieron casi dos tercios de lo que tenían.

Lo contamos día a día, como un thriller. Y al final, la pregunta que importa: ¿podría pasar algo así en España?

En este documental:
· Un peso, un dólar: la hiperinflación, el Plan Bonex y la convertibilidad de Cavallo
· El sábado del decreto: el Decreto 1570 y los 250 pesos por semana
· La caldera: cuasimonedas, cacerolas y la ola de saqueos
· Estado de sitio: el 19 de diciembre de 2001
· El helicóptero: la renuncia de De la Rúa el 20 de diciembre
· Cinco presidentes: Puerta, Rodríguez Saá, Camaño, Duhalde y la suspensión de pagos
· El corralón: la pesificación asimétrica, los amparos, los Boden y el trueque
· Al otro lado del río: el contagio a Uruguay en 2002
· ¿Y en España?: Chipre, Grecia, Bankia, las preferentes, el Banco Popular y el Fondo de Garantía de Depósitos

Capítulos
{caps}

Fuentes principales: Boletín Oficial de la República Argentina (Ley 23.928, Ley 25.466, Decreto 36/1990, Decreto 1570/2001, Decreto 214/2002), Ley 17.523 de Uruguay, Banco Central de la República Argentina, INDEC, FMI, Eurogrupo, Junta Única de Resolución, FROB, Banco de España y hemeroteca de La Nación, Clarín, Página/12, El Observador, El País y EFE.

{{CRED}}

Este vídeo es divulgación, no asesoramiento financiero ni jurídico.

Viene de: «Bankia: salió a bolsa y 10 meses después pidió el rescate». Suscríbete a DocuVox para el próximo caso.

#corralito #Argentina #crisis2001"""

CRED = open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().strip()
desc = desc.replace('{CRED}', CRED)
if len(desc) > 4950:   # límite de YouTube: créditos completos en el comentario fijado
    desc = desc.replace(CRED, 'Créditos de imagen y música (autor y licencia): en el comentario fijado.')
com = '¿Tu familia vivió el corralito, o lo recuerdas de las noticias? Y si estás en España: ¿crees que algo así podría pasar aquí? Te leemos 👇\n\nCréditos de imagen (autor y licencia):\n' + '\n'.join(compact(l) for l in cred)
com = com[:9800]

pod = f"""1 de diciembre de 2001: Argentina descubre que solo puede sacar 250 pesos a la semana de su propia cuenta. Del uno a uno de Cavallo al Decreto 1570, de los cacerolazos al helicóptero de De la Rúa, de los cinco presidentes en dos semanas a la pesificación, el contagio a Uruguay y la gran pregunta: ¿podría pasar en España? Chipre, Grecia, las preferentes, el Banco Popular y el Fondo de Garantía de Depósitos. Documental sonoro de 45 minutos.

{caps}

Versión en vídeo: busca «DocuVox» en YouTube. Sigue DocuVox para no perderte el próximo caso.

{CRED}"""

open(f'{HERE}/descripcion_youtube.txt', 'w').write(desc)
open(f'{HERE}/comentario_fijado.txt', 'w').write(com)
open(f'{HERE}/descripcion_podcast.txt', 'w').write(pod)
open(f'{HERE}/etiquetas.txt', 'w').write(','.join(TAGS))
md = f"""# El corralito argentino · paquete de YouTube

**Título (recomendado):** {TITULO}  ({len(TITULO)} caracteres)
**Alternativas A/B:** {ALT[0]} · {ALT[1]}

**Etiquetas** ({len(','.join(TAGS))} caracteres): {', '.join(TAGS)}

**Ajustes:** Educación · Español (España) · no creado para niños · sin promoción pagada · Uso de IA: No (escenas IA en grabado, no realistas) · capítulos automáticos desactivados · subtítulos corralito.srt · pantalla final 1 vídeo + suscribirse · prueba A/B de miniatura (A Casa Rosada · B De la Rúa)

**Estudio de palabras clave (vidIQ):** corralito 19.962 búsquedas/mes (competencia baja, puntuación 63) · corralito argentina 8.883 (baja, 65) · historia argentina 17.184 (media) · cavallo 6.747 · crisis económica 6.586

## Descripción ({len(desc)} caracteres)

{desc}

## Comentario fijado ({len(com)} caracteres)

{com}
"""
open(f'{HERE}/youtube.md', 'w').write(md)
print(len(desc), len(com), len(pod), len(','.join(TAGS)))
