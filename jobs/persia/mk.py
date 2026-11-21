import json,sys
n=int(sys.argv[1]) if len(sys.argv)>1 else 20
gt=json.load(open('gens_text.json')); v=json.load(open('/tmp/vunits.json')); pool=json.load(open('pool.json'))
rest=[x for x in v if x[2] not in gt][:n]
m={}; up=[]
for nd,(i,vid,t) in zip(pool,rest): m[nd]=i; up.append(dict(node_id=nd,prompt=t,voice_id=vid,label=f'persia U{i}'))
json.dump(m,open('batch_map.json','w'))
print(json.dumps(up,ensure_ascii=False))
print(json.dumps(list(m.keys())))
print(len(up),'unidades',sum(len(x[2]) for x in rest),'car · quedan',len([x for x in v if x[2] not in gt])-len(up),file=sys.stderr)
