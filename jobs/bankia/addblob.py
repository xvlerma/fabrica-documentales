import json,sys
# uso: addblob.py RUNID:hashpath:signature[:amzdate] ...
r=json.load(open('weave_runs.json')); inv={v:k for k,v in r.items()}
res=json.load(open('recursos.json'))
B='https://blobs.figma.com/blobs/us/download/figma-alpha/img/'
for a in sys.argv[1:]:
    p=a.split(':'); rid,path,sig=p[0],p[1],p[2]; d=p[3] if len(p)>3 else '20261122T120000Z'
    day=d[:8]
    res['ai'][inv[rid]]=f'{B}{path}.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWCRABUPZ5K%2F{day}%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date={d}&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature={sig}'
json.dump(res,open('recursos.json','w'),indent=1); print(len(res['ai']),'IA')
