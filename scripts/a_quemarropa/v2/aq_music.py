"""Cama musical provisional (ETAPA 1): temas Mixkit por expediente, nivel bajo, fuera en las zonas SIN música."""
import json, re, subprocess, numpy as np, os
AQ = '/home/claude/w/aq'; SR = 48000; FPS = 25
P = json.load(open(AQ + '/plan.json')); ROWS = {int(r['#']): r for r in json.load(open(AQ + '/edl.json'))}
for _k in (1000, 1001): ROWS[_k] = {'Bloque': 'B0', 'Música / sonido': 'SIN música'}
TR = {'B0': None, 'E1': ('fallen', 0), 'E2': ('masking', 0), 'E3': ('moonwalk', 0), 'E4': ('discover', 0), 'E5': ('vertigo', 0), 'E6': ('delirium', 0),
      'E7': ('bangkok', 0), 'E8': ('feedback', 0), 'E9': ('shame', 0), 'E10': ('goats', 0), 'E11': ('selpan', 0), 'E12': ('xanthos', 0), 'E13': ('farewell', 0),
      'E14': ('river', 0), 'E15': ('fallen', 150), 'E16': ('masking', 120), 'E17': ('moonwalk', 100)}
FAM_C = {'E13', 'E14'}
MUTE = {1000, 1001, 1, 2, 3, 4, 17, 18, 19, 142, 143, 161, 196, 197, 337, 346, 347, 348, 349}
_T = {}
def track(name):
    if name not in _T:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{AQ}/media/m_{name}.mp3', '-af', 'loudnorm=I=-16:TP=-2:LRA=11,aresample=48000', '-ac', '2', '-f', 'f32le', '-'], capture_output=True).stdout
        _T[name] = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2)
    return _T[name]
def take(name, off, n):
    t = track(name); i = int(off * SR) % len(t); out = []
    while n > 0:
        c = t[i:i + n]; out.append(c); n -= len(c); i = 0
    return np.concatenate(out)
def plan_music():
    """por segmento: (tema, offset, ganancia dB | None)"""
    out = []; cur = None; off = 0.0
    for s in P:
        n = s['n']; D = round(s['D'] * FPS) / FPS; b = ROWS[n]['Bloque']; tipo = s['tipo']; mus = ROWS[n]['Música / sonido']
        voice = tipo == 'voz' or 'ocuci' in tipo.lower()
        if b == 'B0': want = ('epical', 0) if 5 <= n <= 16 else (('selpan', 0) if n >= 20 else None)
        elif b == 'E14' and n < 335: want = None
        elif b == 'E17' and n >= 448: want = ('drawing', 0)
        else: want = TR[b]
        if want and (cur is None or cur[0] != (b if not (b == 'B0' or (b == 'E17' and n >= 448)) else f'{b}{want[0]}')):
            cur = (b if not (b == 'B0' or (b == 'E17' and n >= 448)) else f'{b}{want[0]}', want[0]); off = want[1]
        g = None
        if re.search(r'^Silencio|silencio total|Nota sola; silencio|Respiro', mus): want_mute = True
        else: want_mute = False
        if want and not want_mute and n not in MUTE and tipo != 'silencio' and not re.search(r'sin música', mus, re.I) and tipo != 'intro':
            g = -17.0 if voice else -9.0
            if b in FAM_C: g -= 6
            if tipo == 'voz': g -= 3
        out.append((n, cur[1] if (want and cur) else None, off, g, D))
        if want: off += D
    return out
if __name__ == '__main__':
    M = plan_music(); f = open(AQ + '/music.raw', 'wb')
    tot = sum(int(round(m[4] * SR)) for m in M)
    # envolvente a 1 kHz, suavizada 40 ms (sin clics); en los cambios de tema, 0 durante 40 ms
    env = []; prevname = None
    for (n, name, off, g, D) in M:
        k = int(round(D * 1000)); v = 0.0 if (name is None or g is None) else 10 ** (g / 20)
        e = np.full(k, v, np.float32)
        if name != prevname and name is not None: e[:300] = 0
        env.append(e); prevname = name
    env = np.concatenate(env); ker = np.ones(1200, np.float32) / 1200; env = np.convolve(env, ker, mode='same')
    env[-3000:] *= np.linspace(1, 0, 3000).astype(np.float32)
    pos = 0
    for (n, name, off, g, D) in M:
        N = int(round(D * SR))
        buf = np.zeros((N, 2), np.float32) if name is None else take(name, off, N).copy()
        e = np.interp(np.arange(N) / SR * 1000 + pos, np.arange(len(env)), env).astype(np.float32)
        buf *= e[:, None]; pos += N / SR * 1000
        f.write(np.clip(buf * 32767, -32768, 32767).astype(np.int16).tobytes())
    f.close()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', '48000', '-ac', '2', '-i', AQ + '/music.raw', AQ + '/music.wav'])
    os.remove(AQ + '/music.raw')
    json.dump(M, open(AQ + '/music_plan.json', 'w'), ensure_ascii=False)
    print('music ok', sum(m[4] for m in M))
