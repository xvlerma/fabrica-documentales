import json,sys
g=json.load(open('gens.json')); nodes=json.load(open('nodes_batch.json')); inv={v:k for k,v in nodes.items()}
ns=sys.argv[1].split(','); gs=sys.argv[2].split(',')
assert len(ns)==len(gs)
for n,i in zip(ns,gs): g[inv[n]]=i
json.dump(g,open('gens.json','w')); print(len(g))
