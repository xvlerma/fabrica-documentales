#!/usr/bin/env python3
"""Paquete de YouTube/iVoox/Spotify de «Bankia». Uso: python3 paquete.py <carpeta_out>
Escribe youtube.md, descripcion_youtube.txt, comentario_fijado.txt, descripcion_podcast.txt y etiquetas.txt."""
import os, sys

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
caps = open(f'{OUT}/capitulos.txt', encoding='utf-8').read().strip()
cred = [l for l in open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().splitlines() if l.strip() and l.strip() != 'Créditos']

TITULO = 'Bankia: salió a bolsa y 10 meses después pidió el rescate'
ALT = ['El banco que salió a bolsa y se hundió en 10 meses: Bankia', 'Caso Bankia: la salida a bolsa que acabó en rescate']
TAGS = ['bankia', 'caso bankia', 'salida a bolsa bankia', 'rescate bankia', 'historia de bankia', 'rodrigo rato', 'tarjetas black',
        'nacionalización de bankia', 'absueltos caso bankia', 'pequeños ahorradores bankia', 'caída de bankia', 'preferentes',
        'crisis bancaria españa', 'rescate bancario', 'caja madrid', 'bancaja', 'frob', 'goirigolzarri', 'prima de riesgo',
        'crisis 2012', 'whatever it takes', 'caixabank', 'documental bankia', 'documental', 'docuvox']
def compact(l):
    p = [x.strip() for x in l.split(' · ')]
    if len(p) >= 2:
        head, lic = p[0], p[1]
        if ' — ' in head: tit, aut = head.split(' — ', 1)
        else: tit, aut = head, ''
        tit = tit.replace('Archivo: ', '')[:48]
        return f'{tit} — {aut[:40]} ({lic})' if aut else f'{tit} ({lic})'
    return l[:100]

desc = f"""Bankia salió a bolsa el 20 de julio de 2011 a 3,75 euros con 347.000 pequeños accionistas. Diez meses después pidió 19.000 millones al Estado: el mayor rescate bancario de la historia de España. ¿Cómo pudo pasar? ¿Quién lo sabía? ¿Y quién pagó la factura?

Siete cajas de ahorros, una torre de papel, un inspector del Banco de España que avisó por correo, una campaña para convertir a medio país en «bankero», unas cuentas que pasaron de ganar 309 millones a perder casi 3.000 y un juicio que terminó como casi nadie esperaba. Lo contamos como un thriller, día a día.

En este documental:
· Siete cajas y una torre: Caja Madrid, Bancaja y la fusión fría
· El inspector: los correos de Casaus y la «bombona de oxígeno»
· La campana: la salida a bolsa del 20 de julio de 2011
· El castillo de naipes: el auditor y el «presidente, no va»
· Diecinueve mil millones: dimisión de Rato, nacionalización y rescate europeo
· La factura: preferentes, accionistas, despidos y Sareb
· El juicio: tarjetas black, absoluciones y la paradoja del folleto
· El final: CaixaBank y lo que el Estado nunca recuperó

Capítulos
{caps}

Fuentes principales: folleto de la OPV de Bankia (CNMV, 2011), sentencias de la Audiencia Nacional (2020), del Tribunal Supremo (Sala de lo Civil, 2016; Sala de lo Penal, 2022) y de las tarjetas black (2017), Banco de España (Informe sobre la crisis financiera y bancaria, 2017), FROB, memorando de entendimiento del Eurogrupo (2012) y hemeroteca de El País, El Mundo, Expansión y RTVE.

{{CRED}}

Este vídeo es divulgación, no asesoramiento financiero ni jurídico.

Viene de: «Crisis de 2008: así se arruinó España». Suscríbete a DocuVox para el próximo caso.

#Bankia #CasoBankia #RodrigoRato"""

CRED = open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().strip()
desc = desc.replace('{CRED}', CRED)
if len(desc) > 4950:   # límite de YouTube: créditos completos en el comentario fijado y enlace
    desc = desc.replace(CRED, 'Créditos de imagen y música (autor y licencia): en el comentario fijado.')
com = '¿Tú o alguien de tu familia compró acciones o preferentes de Bankia? ¿Recuperasteis el dinero? Cuéntalo abajo 👇\n\nCréditos de imagen (autor y licencia):\n' + '\n'.join(compact(l) for l in cred)
com = com[:9800]

pod = f"""Bankia salió a bolsa el 20 de julio de 2011 con 347.000 pequeños accionistas. Diez meses después pidió 19.000 millones al Estado: el mayor rescate bancario de España. De la fusión de siete cajas a los correos del inspector, del «presidente, no va» del auditor a la nacionalización, las preferentes, las tarjetas black, el juicio y la absorción por CaixaBank. Documental sonoro de 43 minutos.

{caps}

Versión en vídeo: busca «DocuVox» en YouTube. Sigue DocuVox para no perderte el próximo caso.

{CRED}"""

open(f'{HERE}/descripcion_youtube.txt', 'w').write(desc)
open(f'{HERE}/comentario_fijado.txt', 'w').write(com)
open(f'{HERE}/descripcion_podcast.txt', 'w').write(pod)
open(f'{HERE}/etiquetas.txt', 'w').write(','.join(TAGS))
md = f"""# Bankia · paquete de YouTube

**Título (recomendado):** {TITULO}  ({len(TITULO)} caracteres)
**Alternativas A/B:** {ALT[0]} · {ALT[1]}

**Etiquetas** ({len(','.join(TAGS))} caracteres): {', '.join(TAGS)}

**Ajustes:** Educación · Español (España) · no creado para niños · sin promoción pagada · Uso de IA: No · capítulos automáticos desactivados · subtítulos bankia.srt · pantalla final 1 vídeo + suscribirse

## Descripción ({len(desc)} caracteres)

{desc}

## Comentario fijado ({len(com)} caracteres)

{com}
"""
open(f'{HERE}/youtube.md', 'w').write(md)
print(len(desc), len(com), len(pod), len(','.join(TAGS)))
