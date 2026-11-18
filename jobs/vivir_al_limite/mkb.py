import json,sys
# uso: mkb.py k  -> lote k (20 unidades) sobre los 20 primeros nodos
k=int(sys.argv[1]); v=json.load(open('vunits.json')); n=json.load(open('/tmp/nodes.json'))[:20]
rest=v[k*20:(k+1)*20]; m={}; up=[]
for node,(i,vid,t) in zip(n,rest): m[node]=i; up.append(dict(node_id=node,prompt=t,voice_id=vid,label=f'U{i}'))
json.dump(m,open(f'/tmp/batch{k}.json','w'))
print(json.dumps(up,ensure_ascii=False)); print(len(up),sum(len(x[2]) for x in rest),file=sys.stderr)
