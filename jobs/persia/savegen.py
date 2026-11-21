import json,sys
# uso: savegen.py IDX:GID IDX:GID ...  (IDX = índice de unidad)
v={str(i):t for i,_,t in json.load(open('/tmp/vunits.json'))}
gt=json.load(open('gens_text.json'))
for a in sys.argv[1:]:
    i,g=a.split(':'); gt[v[i]]=g
json.dump(gt,open('gens_text.json','w'),ensure_ascii=False,indent=0)
done=set(gt); rest=[(i,vid,t) for i,vid,t in json.load(open('/tmp/vunits.json')) if t not in done]
print(len(gt),'hechas ·',len(rest),'pendientes ·',sum(len(t) for *_,t in rest),'car pendientes')
