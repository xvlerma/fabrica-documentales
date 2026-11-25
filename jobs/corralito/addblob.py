import json,sys
# uso: addblob.py run8|ruta|firmahex ...  (blobs.figma.com, X-Amz-Date fijo)
r=json.load(open('weave_runs.json')); inv={v[:8]:k for k,v in r.items()}
res=json.load(open('recursos.json'))
D=sys.argv[1]
for a in sys.argv[2:]:
    rid,path,sig=a.split('|')
    res['ai'][inv[rid]]=(f'https://blobs.figma.com/blobs/us/download/figma-alpha/img/{path}.png?X-Amz-Algorithm=AWS4-HMAC-SHA256'
      f'&X-Amz-Credential=AKIAQ4GOSFWC3WM52WPH%2F{D[:8]}%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date={D}&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature={sig}')
json.dump(res,open('recursos.json','w'),indent=1)
p=[v for k,v in r.items() if k not in res['ai']]
print(len(res['ai']),'con URL ·',len(p),'pendientes'); open('/tmp/pend.json','w').write(json.dumps(p))
