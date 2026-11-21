# Rama temporal: miniaturas A/B de «Crisis de 2008» (A: Zapatero, La Moncloa; B: ilustración propia de una grúa).
import sys, subprocess, json
subprocess.run("sudo apt-get install -y -q python3-pil python3-requests >/dev/null 2>&1", shell=True)
sys.path.insert(0, 'fabrica')
import sources as SRC, requests, thumb as TH
out = '/tmp/pc'; import os; os.makedirs(out, exist_ok=True)
c = SRC.commons_file('Presidente José Luis Rodriguez Zapatero - La Moncloa 2011.jpg'); p = SRC.download(c['url'], '.jpg')
print('FOTO A', c.get('title'), '|', c.get('credit'), '|', c.get('license'), '|', c.get('page'))
json.dump(c, open(f'{out}/foto_A.json', 'w'), ensure_ascii=False)
from PIL import Image; im = Image.open(p); print('tam', im.size)
TH.make(f'{out}/crisis2008_miniatura_A.jpg', p, '2008', '¿SE REPITE?', 'LA BURBUJA QUE ARRUINÓ A ESPAÑA')
r = requests.get('https://www.figma.com/api/mcp/asset/80f6f6ae-7b8c-401a-87aa-1e863af39959.png', timeout=60); print('grua', r.status_code, len(r.content))
open('/tmp/grua.png', 'wb').write(r.content)
TH.make(f'{out}/crisis2008_miniatura_B.jpg', '/tmp/grua.png', '2008', '¿SE REPITE?', 'LA BURBUJA QUE ARRUINÓ A ESPAÑA')
for f in os.listdir(out): print(f)
