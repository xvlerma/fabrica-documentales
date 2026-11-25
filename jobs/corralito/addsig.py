import json,sys
# uso: addsig.py EXPIRES gid:session:sig ...
B='https://elevenlabsusercontent.com/database/workspace/7b4fe3a6bf44426a98da0b2e9ea701e0/content_generation/'
u=json.load(open('urls.json')); e=sys.argv[1]
for a in sys.argv[2:]:
    g,s,sig=a.split(':',2); u[g]=f'{B}{s}/{g}/content.mp3?Expires={e}&KeyName=assets-cdn-key-1&Signature={sig}'
json.dump(u,open('urls.json','w'),indent=0); print(len(u),'urls')
