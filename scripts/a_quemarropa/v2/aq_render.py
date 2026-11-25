import json, sys, time, traceback
from aq_build import render
P = json.load(open('/home/claude/w/aq/plan.json'))
only = set(int(x) for x in sys.argv[1:]) if len(sys.argv) > 1 else None
t0 = time.time(); bad = []
for i, s in enumerate(P):
    if only and s['n'] not in only: continue
    try: render(s)
    except Exception as e: bad.append(s['n']); print('FAIL', s['n'], str(e)[-900:], flush=True)
    if i % 10 == 0: print(f'{i}/{len(P)} n={s["n"]} {time.time()-t0:.0f}s', flush=True)
print('DONE bad=', bad, f'{time.time()-t0:.0f}s', flush=True)
