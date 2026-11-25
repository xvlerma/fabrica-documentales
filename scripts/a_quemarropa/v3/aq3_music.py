"""Música v3: un tema por expediente con fundido cruzado de 1,2 s, ducking de −20/−22 dB bajo la voz,
cama grave continua (≈ −30 LUFS) donde antes había silencio digital y bajo los carteles de expediente."""
import json, re, subprocess, numpy as np, os
AQ = '/home/claude/w/aq'; SR = 48000; FPS = 25
P = json.load(open(AQ + '/plan3.json')); ROWS = {int(r['#']): r for r in json.load(open(AQ + '/edl.json')) if str(r['#']).isdigit()}
for _k in (1000, 1001): ROWS[_k] = {'Bloque': 'B0', 'Música / sonido': 'SIN música', 'Tipo': 'apertura'}
TR = {'B0': None, 'E1': 'fallen', 'E2': 'masking', 'E3': 'moonwalk', 'E4': 'discover', 'E5': 'vertigo', 'E6': 'delirium',
      'E7': 'bangkok', 'E8': 'feedback', 'E9': 'shame', 'E10': 'goats', 'E11': 'selpan', 'E12': 'xanthos', 'E13': 'farewell',
      'E14': 'river', 'E15': 'fallen', 'E16': 'masking', 'E17': 'moonwalk'}
FAM_C = {'E13', 'E14'}
MUTE = {1000, 1001, 1, 2, 3, 17, 18, 19, 142, 143, 161, 196, 197, 337, 346, 347, 348, 349}
BED_DB = -14.0        # cama: ≈ −30 LUFS (pistas normalizadas a −16)
_T = {}
def track(name):
    if name not in _T:
        af = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,loudnorm=I=-16:TP=-2:LRA=11,aresample=48000' + (',lowpass=f=900,highpass=f=40' if name == 'BED' else '')
        src = 'moonwalk' if name == 'BED' else name
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{AQ}/media/m_{src}.mp3', '-af', af, '-ac', '2', '-f', 'f32le', '-'], capture_output=True).stdout
        _T[name] = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2)
    return _T[name]
def plan_music():
    out = []
    for s in P:
        n = s['n']; D = round(s['D'] * FPS) / FPS; r = ROWS.get(n, {'Bloque': 'E17', 'Música / sonido': '', 'Tipo': ''})
        b = r['Bloque']; tipo = s['tipo']; mus = r.get('Música / sonido', '')
        voice = tipo == 'voz' or 'ocuci' in tipo.lower()
        if b == 'B0': want = 'epical' if 5 <= n <= 16 else ('selpan' if n >= 20 else None)
        elif b == 'E14' and n < 335: want = None
        elif b == 'E17' and n >= 448: want = 'drawing'
        else: want = TR.get(b)
        quiet = bool(re.search(r'^Silencio|silencio total|Nota sola; silencio|Respiro', mus)) or n in MUTE or bool(re.search(r'sin música', mus, re.I))
        name, g = None, None
        if tipo == 'intro': pass
        elif tipo == 'silencio' and not s.get('bed'): pass
        elif want and not quiet:
            name = want; g = (-20.0 if tipo != 'voz' else -22.0) if voice else -10.0
            if b in FAM_C: g -= 4
        else:
            name = 'BED'; g = BED_DB - (2.0 if voice else 0.0)
            if tipo == 'silencio' or s.get('bed'): g = BED_DB
        if s.get('bed') and name and name != 'BED' and not voice: g = -12.0     # cartel de expediente sobre cama musical
        out.append((n, name, g, D))
    return out
if __name__ == '__main__':
    M = plan_music()
    tot = sum(int(round(m[3] * SR)) for m in M); ms = int(round(tot / SR * 1000)) + 1
    names = sorted({m[1] for m in M if m[1]})
    env = {k: np.zeros(ms, np.float32) for k in names}; t = 0
    for (n, name, g, D) in M:
        k = int(round(D * 1000))
        if name: env[name][t:t + k] = 10 ** (g / 20)
        t += k
    ker = np.ones(1200, np.float32) / 1200
    E = {}
    for name in names:
        e = np.convolve(env[name], ker, mode='same')
        if e.max() > 0: E[name] = (e, int(np.argmax(e > 0)) * SR // 1000)
    fo = open(AQ + '/music3.raw', 'wb'); CH = 30 * SR
    for c0 in range(0, tot, CH):
        c1 = min(tot, c0 + CH); n_ = c1 - c0; mix = np.zeros((n_, 2), np.float32)
        tt = (np.arange(c0, c1) / SR * 1000)
        for name, (e, first) in E.items():
            ee = np.interp(tt, np.arange(ms), e).astype(np.float32)
            if ee.max() <= 1e-5: continue
            tr = track(name); idx = (np.arange(c0, c1) - first) % len(tr)
            mix += tr[idx] * ee[:, None]
        fade0 = tot - 3 * SR
        if c1 > fade0:
            k = np.arange(c0, c1); f = np.clip((tot - k) / (3 * SR), 0, 1).astype(np.float32); mix *= f[:, None]
        fo.write(np.clip(mix * 32767, -32768, 32767).astype(np.int16).tobytes())
    fo.close()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', '48000', '-ac', '2', '-i', AQ + '/music3.raw', AQ + '/music3.wav'], check=True)
    os.remove(AQ + '/music3.raw')
    json.dump(M, open(AQ + '/music3_plan.json', 'w'), ensure_ascii=False)
    print('music3 ok', tot / SR)
