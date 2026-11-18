import json,sys,os
# uso: rec.py k gen1,gen2,...   (en el orden de los nodos del lote)
k=int(sys.argv[1]); gs=sys.argv[2].split(',')
m=json.load(open(f'/tmp/batch{k}.json')); g=json.load(open('gens.json')) if os.path.exists('gens.json') else {}
assert len(gs)==len(m), (len(gs),len(m))
for (node,i),gid in zip(m.items(),gs): g[str(i)]=gid
json.dump(g,open('gens.json','w'),indent=0); print(len(g))
