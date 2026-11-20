import json,sys
g=json.load(open('gens.json')); m=json.load(open('batch_map.json')); pool=json.load(open('pool.json'))
gids=sys.argv[1].split(',')
for n,gid in zip(pool,gids):
    if n in m: g[str(m[n])]=gid
json.dump(g,open('gens.json','w')); print(len(g),'unidades con voz')
