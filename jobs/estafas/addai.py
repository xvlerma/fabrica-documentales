import json,sys
r=json.load(open('recursos.json')); B='https://www.figma.com/api/mcp/asset/'
for a in sys.argv[1:]:
    k,v=a.split('=',1); r['ai'][k]=v if v.startswith('http') else B+v+('' if '.' in v else '.jpg')
json.dump(r,open('recursos.json','w'),indent=1); print(len(r['ai']),'IA')
