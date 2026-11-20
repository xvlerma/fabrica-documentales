import json,sys
# uso: savebatch.py 'gid1,gid2,...' en el orden de batch_map (nodo -> unidad)
g=json.load(open('gens.json')); m=json.load(open('batch_map.json')); gt=json.load(open('gens_text.json'))
v={str(i):t for i,_,t in json.load(open('/tmp/vunits.json'))}
for n,gid in zip(m.keys(), sys.argv[1].split(',')):
    g[str(m[n])]=gid; gt[v[str(m[n])]]=gid
json.dump(g,open('gens.json','w')); json.dump(gt,open('gens_text.json','w'),ensure_ascii=False,indent=0); print(len(gt),'unidades con voz')
