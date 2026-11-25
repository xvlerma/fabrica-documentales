import json,sys
r=json.load(open('weave_runs.json')); p=json.load(open('/tmp/wp.json'))
n=int(sys.argv[1]) if len(sys.argv)>1 else 12
for k in [k for k in p if k not in r][:n]: print(json.dumps(p[k],ensure_ascii=False))
