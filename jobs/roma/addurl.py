import json,sys,os
# uso: addurl.py gid:session:expires:signature ...
p='urls.json'; u=json.load(open(p)) if os.path.exists(p) else {}
B='https://elevenlabsusercontent.com/database/workspace/7b4fe3a6bf44426a98da0b2e9ea701e0/content_generation/'
for a in sys.argv[1:]:
    g,s,e,sig=a.split(':',3); u[g]=f'{B}{s}/{g}/content.mp3?Expires={e}&KeyName=assets-cdn-key-1&Signature={sig}'
json.dump(u,open(p,'w'),indent=0); print(len(u),'urls')
