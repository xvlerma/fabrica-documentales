import json,sys
# uso: wr.py run1 run2 ...  (asigna a las siguientes claves sin run, en orden)
r=json.load(open('weave_runs.json')); p=json.load(open('/tmp/wp.json'))
pend=[k for k in p if k not in r]
for k,rid in zip(pend,sys.argv[1:]): r[k]=rid
json.dump(r,open('weave_runs.json','w'),indent=0)
pend=[k for k in p if k not in r]; print(len(r),'lanzadas ·',len(pend),'pendientes')
for k in pend[:int(sys.argv[0:1] and 12)]: pass
