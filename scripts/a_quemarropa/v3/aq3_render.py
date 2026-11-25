import json, sys, time
from aq3_build import render
P = json.load(open('/home/claude/w/aq/plan3.json'))
args = sys.argv[1:]; shard = None
if args and '/' in args[0]: k, N = map(int, args.pop(0).split('/')); shard = (k, N)
only = set(int(x) for x in args) if args else None
t0 = time.time(); bad = []
for i, s in enumerate(P):
    if only and s['n'] not in only: continue
    if shard and i % shard[1] != shard[0]: continue
    try: render(s)
    except Exception as e: bad.append(s['n']); print('FAIL', s['n'], str(e)[-1500:], flush=True)
    if i % 20 == 0: print(f'{i}/{len(P)} n={s["n"]} {time.time()-t0:.0f}s', flush=True)
print('DONE bad=', bad, f'{time.time()-t0:.0f}s', flush=True)
