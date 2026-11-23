# -*- coding: utf-8 -*-
"""Textos de entrega del montaje v3: guion con fuentes, descripción de YouTube (con capítulos) y créditos públicos.
Uso: python3 entrega3.py <carpeta con capitulos.txt> <carpeta de salida>"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src_dir, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
J = json.load(open(os.path.join(HERE, 'job.json'))); U = J['units']
TIT = 'Pedro Sánchez: la entrevista que nadie le hizo | 10 preguntas, sus respuestas reales'
NAMES = dict(TOP='NARRADOR', NEW='NARRADOR', ENT='PREGUNTA (DocuVox)', DOC='DOCUMENTO')

def srcs(u):
    o = []
    for s in u.get('shots', []):
        c = s.get('card') or {}
        for k in ('attrib', 'source'):
            if c.get(k): o.append(c[k])
        for side in ('left', 'right'):
            if isinstance(c.get(side), dict) and c[side].get('source'): o.append(c[side]['source'])
    return [re.sub(r'^Fuente: ', '', x) for x in o]

# guion con fuentes
L = [f'# {TIT}', '', 'DocuVox · guion con fuentes (montaje v3, versión crítica)', '',
     '> Las respuestas de Pedro Sánchez y del resto de aludidos son cortes reales de archivo, con su fecha y su medio. '
     'Las preguntas y la narración son de DocuVox. Investigado no es condenado: se indica en cada caso el estado procesal.', '']
for u in U:
    if u['k'] == 'T' and u.get('card') and u.get('chapter'): L += ['', f"## {u['card'].get('n', '')} · {u['card'].get('text', '')}", '']
    if u['k'] in ('N', 'R') and u.get('text'):
        L += [f"**{NAMES.get(u['voice'], u['voice'])}** · {re.sub(r'\[[^\]]*\] ?', '', u['text'])}"]
        f_ = srcs(u)
        if f_: L += ['', '  _Fuente en pantalla: ' + ' / '.join(dict.fromkeys(f_)) + '_']
        L += ['']
    if u['k'] == 'C':
        L += [f"▶ **CORTE REAL** · {' · '.join(u.get('lt') or [])}" + (f" · «{u['quote']}»" if u.get('quote') else ''), '']
open(f'{out}/guion_con_fuentes.md', 'w').write('\n'.join(L))

# fuentes únicas: medios y documentos citados en pantalla
cortes = []
for u in U:
    if u['k'] == 'C' and u.get('lt'):
        w = u['lt'][1].replace('RESPUESTA REAL · ', '')
        cortes.append(f"{u['lt'][0]} · {w}")
cortes = list(dict.fromkeys(cortes))
docs = list(dict.fromkeys(x for u in U for x in srcs(u) if x))

cap = open(os.path.join(src_dir, 'capitulos.txt')).read().strip()
music = [v['title'] for v in J['music'].values()]
desc = f"""Diez preguntas a Pedro Sánchez que nadie le hizo así, una detrás de otra. Las respuestas son suyas: cortes reales de archivo, con su medio y su fecha. Después, lo que pasó, con su documento en pantalla.

Pedro Sánchez no ha participado en este documental. Sus respuestas son declaraciones públicas de archivo. Pedro Sánchez no está imputado en ninguna causa. Investigado no significa culpable: en cada persona se indica su situación procesal.

CAPÍTULOS
{cap}

FUENTES DE LOS CORTES (medio y fecha, también en pantalla)
""" + '\n'.join('· ' + c for c in cortes) + """

DOCUMENTOS Y MEDIOS CITADOS
""" + '\n'.join('· ' + d for d in docs) + f"""

Las imágenes marcadas como «RECREACIÓN» están generadas con inteligencia artificial: lugares sin personas reales. Los documentos, mensajes y sentencias que aparecen son siempre capturas reales.
Uso de los cortes al amparo del derecho de cita (art. 32 LPI), con fines de análisis y crítica.
Música: {', '.join(music)} (Mixkit, licencia Mixkit).

#PedroSánchez #Elecciones2026 #DocuVox
"""
open(f'{out}/descripcion_youtube.txt', 'w').write(TIT + '\n\n' + desc)
cred = ('Créditos\nRealización y guion: DocuVox\nCortes de archivo (derecho de cita, art. 32 LPI):\n' + '\n'.join('· ' + c for c in cortes) +
        '\nDocumentos: ' + ' · '.join(docs[:60]) + f'\nMúsica: {", ".join(music)} · Mixkit (licencia Mixkit)\n'
        'Imágenes «RECREACIÓN»: generadas con IA, sin personas reales.\n')
open(f'{out}/creditos_publicos.txt', 'w').write(cred)
json.dump(dict(title=TIT, description=desc[:4990], tags=['Pedro Sánchez', 'elecciones generales', 'documental', 'DocuVox', 'entrevista'],
               category='25', lang='es-ES', synthetic=True, solo_privado=True), open(f'{out}/youtube.json', 'w'), ensure_ascii=False, indent=1)
print(len(desc), 'caracteres de descripción ·', len(cortes), 'cortes ·', len(docs), 'documentos')
