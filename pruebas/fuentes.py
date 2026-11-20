# Rama temporal: genera las miniaturas de «estafas» y las vuelca en base64 en el informe.
import sys, os, base64
import subprocess; subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--user", "--break-system-packages", "pillow", "requests"]); import site; sys.path.append(site.getusersitepackages())
sys.path.insert(0, 'fabrica')
import sources as SRC, thumb as TH
SRC.SEGURO = True
for nombre in ['BernardMadoff.jpg', 'Bernard Madoff 2009 mug shot (3x4 cropped).jpg']:
    try:
        c = SRC.commons_file(nombre); p = SRC.download(c['url'], '.jpg')
        print('FOTO', nombre, '|', c.get('credit', ''), '|', c.get('license', ''), '|', c.get('url'))
        break
    except Exception as e: print('fallo', nombre, e)
V = [('A', '65.000 MILLONES', 'LA MAYOR ESTAFA', 'De Ponzi a Madoff'),
     ('B', 'TODO ERA MENTIRA', '65.000 MILLONES', 'Las estafas más grandes de la historia')]
for n, g, cj, sub in V:
    out = f'/tmp/estafas_miniatura_{n}.jpg'
    TH.make(out, p, g, cj, sub)
    print(f'IMG{n}', base64.b64encode(open(out, 'rb').read()).decode())
