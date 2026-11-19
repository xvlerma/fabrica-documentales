import json,sys
# uso: savebatch.py '<json results de run_flow_nodes>' (lista de {node_id, credit_costs})
g=json.load(open('gens.json')); m=json.load(open('batch_map.json'))
res=json.loads(sys.argv[1])
for r in res:
    gid=list(r['credit_costs'].keys())[0]; g[str(m[r['node_id']])]=gid
json.dump(g,open('gens.json','w')); print(len(g),'unidades con voz')
