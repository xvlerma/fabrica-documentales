import json,sys
# uso: addw.py clave=e608/8562/hash:firma ...  (salida de Weave, URL firmada 7 días)
r=json.load(open('recursos.json'))
B='https://blobs.figma.com/blobs/us/download/figma-alpha/img/'
Q='.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWCRABUPZ5K%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature='
for a in sys.argv[1:]:
    k,v=a.split('=',1); p,s=v.split(':'); r['ai'][k]=B+p+Q+s
json.dump(r,open('recursos.json','w'),indent=1); print(len(r['ai']),'IA')
