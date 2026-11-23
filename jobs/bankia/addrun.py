import json,sys
# uso: addrun.py RUNID=URL ...  (mapea el run de Weave a su clave de escena)
r=json.load(open('weave_runs.json')); inv={v:k for k,v in r.items()}
res=json.load(open('recursos.json'))
for a in sys.argv[1:]:
    rid,u=a.split('=',1); res['ai'][inv[rid]]=u
json.dump(res,open('recursos.json','w'),indent=1); print(len(res['ai']),'IA')
