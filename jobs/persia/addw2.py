import json,sys
# uso: addw2.py clave=b7f1/4f87/hash:firma ...  (Weave, URL firmada hasta el 30-11)
r=json.load(open('recursos.json'))
B='https://s3-alpha-sig.figma.com/img/'; Q='.png?Expires=1795996800&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature='
for a in sys.argv[1:]:
    k,v=a.split('=',1); p,s=v.split(':',1); r['ai'][k]=B+p+Q+s
json.dump(r,open('recursos.json','w'),indent=1); print(len(r['ai']),'IA')
