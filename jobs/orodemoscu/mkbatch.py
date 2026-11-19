import json
g=json.load(open('gens.json')); v=json.load(open('/tmp/vunits.json')); pool=json.load(open('pool.json'))
rest=[x for x in v if str(x[0]) not in g][:len(pool)]
m={}; up=[]
for n,(i,vid,t) in zip(pool,rest): m[n]=i; up.append(dict(node_id=n,prompt=t,voice_id=vid,label=f'U{i}'))
json.dump(m,open('batch_map.json','w'))
print(json.dumps(up,ensure_ascii=False))
import sys; print(len(up),'unidades',rest[0][0] if rest else None,'->',rest[-1][0] if rest else None,sum(len(x[2]) for x in rest),'car',file=sys.stderr)
