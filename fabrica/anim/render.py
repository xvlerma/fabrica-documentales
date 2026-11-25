"""Renderiza las animaciones de un episodio. Uso: python render.py <jobdir> <calidad: l|h> [nombre ...]"""
import sys, os, json, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
job = os.path.abspath(sys.argv[1]); q = sys.argv[2]; only = set(sys.argv[3:])
plan = json.load(open(f'{job}/anim/plan.json'))
out = os.path.abspath(os.path.join(job, '..', '..', 'media', os.path.basename(job), 'anim' if q == 'h' else 'anim_prev')); os.makedirs(out, exist_ok=True)
def one(it):
    if only and it['name'] not in only: return it['name'], 'skip'
    env = dict(os.environ, ANIM_CUES=f"{job}/anim/cues/{it['name']}.json")
    md = f"/tmp/manim_{it['name']}"
    args = ['manim', '--media_dir', md, '-o', it['name'], '--disable_caching']
    args += (['-r', '1920,1080', '--fps', '30'] if q == 'h' else ['-r', '960,540', '--fps', '10'])
    r = subprocess.run(args + [f'{HERE}/docuanim.py', it['scene']], env=env, capture_output=True, text=True)
    if r.returncode: return it['name'], 'ERROR ' + r.stderr[-1500:]
    f = next(os.path.join(dp, fn) for dp, _, fs in os.walk(md) for fn in fs if fn == it['name'] + '.mp4')
    shutil.copy(f, f"{out}/{it['name']}.mp4"); shutil.rmtree(md, ignore_errors=True)
    return it['name'], 'ok'
with ThreadPoolExecutor(int(os.environ.get('ANIM_JOBS', 2))) as ex:
    for n, s in ex.map(one, plan): print(n, s, flush=True)
