import json,sys
# uso: mkbatch.py nodes.json  -> asigna las próximas unidades sin voz a esos nodos y escribe el payload
g=json.load(open('gens.json')); v=json.load(open('/tmp/vunits.json'))
pool=json.load(open(sys.argv[1]))
rest=[x for x in v if str(x[0]) not in g][:len(pool)]
m={}; up=[]
for n,(i,vid,t) in zip(pool,rest): m[str(i)]=n; up.append(dict(node_id=n,prompt=t,voice_id=vid,label=f'U{i}'))
json.dump(m,open('nodes_batch.json','w')); json.dump(up,open('/tmp/up.json','w'),ensure_ascii=False)
print(len(up), 'unidades', rest[0][0] if rest else None, '->', rest[-1][0] if rest else None, sum(len(x[2]) for x in rest),'caracteres')
