import json,sys
n=int(sys.argv[1]) if len(sys.argv)>1 else 14
gt=json.load(open('gens_text.json'))
rest=[(i,vid,t) for i,vid,t in json.load(open('/tmp/vunits.json')) if t not in gt][:n]
for i,vid,t in rest: print(f'{i}|{vid}|{t}')
