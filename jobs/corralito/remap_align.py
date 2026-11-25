import json
al=json.load(open('align.json')); j=json.load(open('job.json'))
bys={v['key'].split(':',1)[1]:v['words'] for v in al.values()}
new={}
for i,u in enumerate(j['units']):
    s=u.get('url','')[-40:]
    if u.get('url') and s in bys: new[str(i)]=dict(key=f"{i}:{s}",words=bys[s])
json.dump(new,open('align.json','w'),ensure_ascii=False); print(len(new),'alineadas reutilizadas')
