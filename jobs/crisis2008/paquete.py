#!/usr/bin/env python3
"""Paquete de YouTube/iVoox/Spotify de «Crisis de 2008». Uso: python3 paquete.py <carpeta_out>
Escribe youtube.md, descripcion_youtube.txt, comentario_fijado.txt, descripcion_podcast.txt y etiquetas.txt."""
import os, sys

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
caps = open(f'{OUT}/capitulos.txt', encoding='utf-8').read().strip()
cred = [l for l in open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().splitlines() if l.strip() and l.strip() != 'Créditos']

TITULO = 'Crisis de 2008: así se arruinó España (y puede repetirse)'
ALT = ['La burbuja que arruinó a España (y vuelve a crecer)', 'Crisis de 2008 en España: ¿se está repitiendo?']
TAGS = ['crisis 2008 españa', 'burbuja inmobiliaria', 'precio vivienda', 'hipotecas', 'rescate bancario', 'Lehman Brothers',
        'Bankia', 'Zapatero', 'crisis de 2008', 'burbuja inmobiliaria españa', 'crisis económica españa', 'desahucios',
        'seseña', 'el pocero', 'aeropuerto de castellón', 'cajas de ahorros', 'euríbor', 'precio del alquiler',
        'vivienda en españa', 'se repite la crisis', '15M', 'prima de riesgo', 'sareb', 'documental', 'docuvox']
def compact(l):
    p = [x.strip() for x in l.split(' · ')]
    if len(p) >= 2:
        head, lic = p[0], p[1]
        if ' — ' in head: tit, aut = head.split(' — ', 1)
        else: tit, aut = head, ''
        tit = tit.replace('Archivo: ', '')[:48]
        return f'{tit} — {aut[:40]} ({lic})' if aut else f'{tit} ({lic})'
    return l[:100]

desc = f"""Crisis de 2008 en España: la burbuja inmobiliaria, el crédito fácil y el rescate bancario. ¿Se está repitiendo hoy con el precio de la vivienda?

En 2006 España levantó más viviendas que Francia, Alemania e Italia juntas. Dos años después cayó Lehman Brothers y el país entero se vino abajo: seis millones de parados, cientos de miles de ejecuciones hipotecarias, aeropuertos sin aviones, ciudades fantasma y un rescate europeo de la banca. Hoy el metro cuadrado vuelve a estar en máximos y comprar o alquilar se ha vuelto imposible para muchos. ¿Estamos otra vez en el mismo punto? Te lo respondemos al final, con datos.

En este documental:
· La fiesta del ladrillo: euro, tipos bajos, cajas de ahorros y El Quiñón de Seseña
· Los que lo vieron venir y por qué nadie lo paró
· El día que cayó Lehman Brothers y la negación en España
· Seis millones de parados, el 15M y la generación que se fue
· Desahucios, la PAH y las cláusulas abusivas
· Las casas vacías: el aeropuerto de Castellón y la ciudad fantasma
· El rescate bancario: Bankia, el MoU de 2012 y la Sareb
· La vivienda hoy: precios, alquiler y la respuesta a «¿se repite?»

Capítulos
{caps}

Fuentes principales: Banco de España (informes anuales e Informe sobre la crisis financiera y bancaria, 2017), INE (EPA, Censo 2011, estadística de ejecuciones hipotecarias), Ministerio de Vivienda (valor tasado de la vivienda libre), Consejo General del Poder Judicial, Eurostat, Tribunal de Cuentas, sentencia del TJUE Aziz (2013) y hemeroteca de El País, El Mundo, Expansión y RTVE.

{CRED}

Este vídeo es divulgación, no asesoramiento financiero ni inmobiliario.

En el próximo: Bankia, el banco que salió a bolsa y pidió el rescate diez meses después. Suscríbete a DocuVox para no perdértelo.

#crisis2008 #burbujainmobiliaria #vivienda"""

CRED = open(f'{OUT}/creditos_publicos.txt', encoding='utf-8').read().strip()
desc = desc.replace('{CRED}', CRED)
if len(desc) > 4950:   # límite de YouTube: créditos completos en el comentario fijado y enlace
    desc = desc.replace(CRED, 'Créditos de imagen y música (autor y licencia): en el comentario fijado.')
com = '¿Crees que se está repitiendo? ¿Cómo viviste tú 2008? Cuéntalo abajo 👇\n\nCréditos de imagen (autor y licencia):\n' + '\n'.join(compact(l) for l in cred)
com = com[:9800]

pod = f"""Crisis de 2008 en España: la burbuja inmobiliaria, el crédito fácil y el rescate bancario. ¿Se está repitiendo hoy con el precio de la vivienda? De El Quiñón de Seseña a Lehman Brothers, de los seis millones de parados a los desahucios, el aeropuerto de Castellón y el rescate de Bankia. Y al final, la respuesta: ¿estamos otra vez en el mismo punto? Documental sonoro de una hora.

{caps}

Versión en vídeo: busca «DocuVox» en YouTube. En el próximo: Bankia, el banco que salió a bolsa y pidió el rescate diez meses después. Sigue DocuVox para no perdértelo.

{CRED}"""

open(f'{HERE}/descripcion_youtube.txt', 'w').write(desc)
open(f'{HERE}/comentario_fijado.txt', 'w').write(com)
open(f'{HERE}/descripcion_podcast.txt', 'w').write(pod)
open(f'{HERE}/etiquetas.txt', 'w').write(','.join(TAGS))
md = f"""# Crisis de 2008 · paquete de YouTube

**Título (recomendado):** {TITULO}  ({len(TITULO)} caracteres)
**Alternativas A/B:** {ALT[0]} · {ALT[1]}

**Etiquetas** ({len(','.join(TAGS))} caracteres): {', '.join(TAGS)}

**Ajustes:** Educación · Español (España) · no creado para niños · sin promoción pagada · Uso de IA: No · capítulos automáticos desactivados · subtítulos crisis2008.srt · pantalla final 1 vídeo + suscribirse

## Descripción ({len(desc)} caracteres)

{desc}

## Comentario fijado ({len(com)} caracteres)

{com}
"""
open(f'{HERE}/youtube.md', 'w').write(md)
print(len(desc), len(com), len(pod), len(','.join(TAGS)))
