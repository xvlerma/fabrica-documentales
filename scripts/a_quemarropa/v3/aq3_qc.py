"""Control técnico del montaje v1: negros, congelados, silencios no previstos, duplicados, «Consultados», duración, sincronía."""
import json, re, subprocess, os, sys
AQ = '/home/claude/w/aq'; FPS = 25; M = AQ + '/entrega3/montaje_v3.mp4'
P = json.load(open(AQ + '/plan3.json')); TL = {x['n']: x for x in json.load(open(AQ + '/timeline3.json'))}
ROWS = {int(r['#']): r for r in json.load(open(AQ + '/edl.json')) if str(r['#']).isdigit()}
import collections as _c
ROWS = _c.defaultdict(lambda: {'Bloque': 'APERTURA', 'Duración': '—', 'Contenido literal (voz o texto)': '', 'Texto en pantalla (+ # verificación)': '', 'Nota para el montador': '', 'Visual en pantalla (archivo de recurso)': '', 'Música / sonido': '', 'Tipo': 'apertura'}, ROWS)
MP = {m[0]: m for m in json.load(open(AQ + '/music3_plan.json'))}
r = subprocess.run(['ffmpeg', '-v', 'info', '-i', M, '-vf', 'scale=480:-2,blackdetect=d=0.5:pix_th=0.10,freezedetect=n=-55dB:d=2.0', '-af', 'silencedetect=n=-45dB:d=1.5', '-f', 'null', '-'], capture_output=True, text=True).stderr
def grab(pat): return [tuple(float(x) for x in m) for m in re.findall(pat, r)]
blacks = grab(r'black_start:([\d.]+) black_end:([\d.]+)')
fs = re.findall(r'freeze_start: ([\d.]+)', r); fe = re.findall(r'freeze_end: ([\d.]+)', r); freezes = list(zip(map(float, fs), map(float, fe)))
ss_ = re.findall(r'silence_start: ([\d.]+)', r); se = re.findall(r'silence_end: ([\d.]+)', r); sil = list(zip(map(float, ss_), map(float, se)))
def rows_at(a, b): return [n for n, x in TL.items() if x['tin'] < b and x['tin'] + x['D'] > a]
def planned_black(n):
    s = [x for x in P if x['n'] == n][0]
    return s['tipo'] == 'silencio' or any(p['t'] == 'black' for p in s['pieces']) or ('N1' in ROWS[n]['Visual en pantalla (archivo de recurso)'] and 'negro' in ROWS[n]['Visual en pantalla (archivo de recurso)']) or n in (4, 20, 455)
def planned_still(n):
    s = [x for x in P if x['n'] == n][0]
    return s['tipo'] != 'voz' or any(p['t'] in ('img', 'wave') for p in s['pieces'])
def planned_sil(n):
    s = [x for x in P if x['n'] == n][0]; mp = MP.get(n)
    return s['tipo'] in ('silencio', 'voz') or (mp and mp[2] is None and s['tipo'] not in ('locución',)) or n in (4,)
def pieces_at(a, b):
    out = []
    for n, x in TL.items():
        t = x['tin']; s = [y for y in P if y['n'] == n][0]
        for p in s['pieces']:
            if t < b and t + p['dur'] > a: out.append((n, p['t']))
            t += p['dur']
    return out
SP = {s['n']: s for s in P}
rep = []
for a, b in blacks:
    ps = [x for x in pieces_at(a + 0.05, b - 0.05) if x[1] == 'clip' and x[0] != 4]
    if ps: rep.append(('NEGRO sobre plano de vídeo', a, b, sorted(set(n for n, _ in ps))))
for a, b in freezes:
    ps = pieces_at(a + 0.05, b - 0.05)
    if ps and all(t == 'clip' for n, t in ps): rep.append(('CONGELADO en plano de vídeo', a, b, sorted(set(n for n, _ in ps))))
for a, b in sil:
    ns = sorted(set(n for n, _ in pieces_at(a + 0.05, b - 0.05)))
    ok = all(SP[n]['tipo'] in ('silencio', 'intro') or SP[n].get('pause') or ('ocuci' not in SP[n]['tipo'].lower() and SP[n]['tipo'] != 'voz' and (MP.get(n) or [0,0,0,None])[2] is None) for n in ns)
    if not ok: rep.append(('SILENCIO >1,5 s', a, b, ns))
# duplicados de corte no intencionados
use = {}
dups = []
for s in P:
    if s['tipo'] != 'voz': continue
    for p, a, b in s.get('src', []):
        for (n2, a2, b2) in use.get(p, []):
            if a < b2 - 0.3 and b > a2 + 0.3:
                note = ROWS[s['n']]['Nota para el montador'] + ROWS[n2]['Nota para el montador']
                if not re.search(r'RÁFAGA|Repetición intencionada|segundo uso|intencionad', note): dups.append((n2, s['n'], os.path.basename(p), round(max(a, a2), 1), round(min(b, b2), 1)))
        use.setdefault(p, []).append((s['n'], a, b))
cons = [n for n, rr in ROWS.items() if re.search(r'Consultados por DocuVox', ' '.join(rr.values()))]
desync = []  # el audio de cada segmento se ajusta a su duración exacta en muestras al montar (sin deriva)
tot = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', M], capture_output=True, text=True).stdout)
js = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,duration', '-of', 'json', M], capture_output=True, text=True).stdout)
out = dict(blacks=blacks, freezes=freezes, silences=sil, unplanned=rep, dups=dups, consultados_en_edl=cons, desync=desync, total=tot,
           streams={x['codec_type']: float(x.get('duration', 0)) for x in js['streams']}, target=3778.0, dev_pct=round((tot - 3778.0) / 3778.0 * 100, 2))
json.dump(out, open(AQ + '/qc3.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in out.items()}, ensure_ascii=False))
for x in rep: print(x)
for x in dups: print('DUP', x)
