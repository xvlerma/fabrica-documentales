import json,sys
# uso: addfig.py EXPIRES run8|ruta|firma ...   (run8 = primeros 8 caracteres del run de Weave)
r=json.load(open('weave_runs.json')); inv={v[:8]:k for k,v in r.items()}
res=json.load(open('recursos.json')); e=sys.argv[1]
for a in sys.argv[2:]:
    rid,path,sig=a.split('|')
    res['ai'][inv[rid]]=f'https://s3-alpha-sig.figma.com/img/{path}.png?Expires={e}&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature={sig}'
json.dump(res,open('recursos.json','w'),indent=1); print(len(res['ai']),'IA con URL de',len(r))
