# Rama temporal: descarga la foto de Madoff y el fondo IA y los vuelca en base64.
import sys, base64, subprocess
subprocess.run("sudo apt-get install -y -q python3-pil python3-requests >/dev/null 2>&1", shell=True)
sys.path.insert(0, 'fabrica')
import sources as SRC, requests
c = SRC.commons_file('BernardMadoff.jpg'); p = SRC.download(c['url'], '.jpg')
print('FOTO', c.get('credit'), c.get('license'))
print('B64foto', base64.b64encode(open(p, 'rb').read()).decode())
u = 'https://s3-alpha-sig.figma.com/img/6712/2847/4975ea9e56919a3320334fe22cdd9f81.png?Expires=1795996800&Key-Pair-Id=APKAQ4GOSFWCW27IBOMQ&Signature=gEh6bbZIWDDsk5LbJ1mWBkDW7T-u7rHCixmReZe8Olxfi5iQXegNmIdvA5cRY6JdymoBRcuGEMAgMg3ubQCAM6WxDktM8MgIwKncq7VOC7QEKE0Nn09RHCQ7iGA6JOaJBJO7KY3gA3pQ31cGGvIoonQkHkk1ChyhXe9MCCr1f5Wus2K3rTrAh20tnKd~TMPpJLWf-5anPi1kfmmyPZYxCB-eezCVSqpzUdXhyMKequ8pg4qzjRSf1AGZUhC6QbwWUm45KTj~ZMXeCYfm4EMnFgTNAuIuT3WsPG~w0-6xs2OtxinRNsVxw~l4tTUvbhQHhzsab7bB9E~YGrgRqXF8Nw__'
r = requests.get(u, timeout=60); print('fondo', r.status_code, len(r.content))
print('B64fondo', base64.b64encode(r.content).decode())
