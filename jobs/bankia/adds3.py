import json,sys
# uso: adds3.py RUNID|hashpath|signature ...   (formato s3-alpha-sig, Expires fijo)
r=json.load(open('weave_runs.json')); inv={v:k for k,v in r.items()}
res=json.load(open('recursos.json'))
for a in sys.argv[1:]:
    rid,path,sig=a.split('|')
    res['ai'][inv[rid]]=f'https://s3-alpha-sig.figma.com/img/{path}.png?Expires=1795996800&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature={sig}'
json.dump(res,open('recursos.json','w'),indent=1); print(len(res['ai']),'IA')
