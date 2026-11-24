"""etapa "capturas": captura de páginas web (titular, medio y fecha visibles) para documentos del guion.

job: {"stage":"capturas","pages":[{"name","url"}]}  ->  out/cap_<name>.png (parte alta de la página), capturas.json
No acepta cookies: rechaza si hay botón de rechazo y, si no, oculta el aviso. Los PDF se guardan y se rasteriza la 1ª página.
"""
import os, re, json, subprocess, sys, time, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
REJECT = ['Rechazar todo', 'Rechazar todas', 'Rechazar y cerrar', 'Rechazar', 'No aceptar', 'Denegar', 'Continuar sin aceptar',
          'Solo necesarias', 'Sólo necesarias', 'Solo las necesarias', 'Rebutjar', 'Reject all', 'Decline']
HIDE = """
(() => {
  const sel = ['#didomi-host', '#onetrust-consent-sdk', '.qc-cmp2-container', '#qc-cmp2-container', '[id^="sp_message_container"]',
               '#CybotCookiebotDialog', '#CybotCookiebotDialogBodyUnderlay', '.fc-consent-root', '#cmpbox', '#cmpbox2', '.cmp-root',
               '[class*="cookie-banner"]', '[id*="cookie-banner"]', '[class*="cookiewall"]', '[class*="consent"]', '[id*="consent"]',
               '.tp-modal', '.tp-backdrop', '[class*="paywall-overlay"]'];
  let n = 0;
  for (const s of sel) for (const e of document.querySelectorAll(s)) { e.style.setProperty('display', 'none', 'important'); n++; }
  for (const e of [document.documentElement, document.body]) if (e) { e.style.setProperty('overflow', 'auto', 'important'); e.style.setProperty('position', 'static', 'important'); }
  for (const c of ['didomi-popup-open', 'sp-message-open', 'no-scroll', 'modal-open']) document.body && document.body.classList.remove(c);
  return n;
})()
"""

def sh(*a, **k): return subprocess.run(list(a), capture_output=True, text=True, **k)

def run(job, out_dir):
    os.makedirs(out_dir, exist_ok=True); rep = []; log = []
    def L(*a):
        s = ' '.join(str(x) for x in a); print(s, flush=True); log.append(s)
    sh(sys.executable, '-m', 'pip', 'install', '-q', 'playwright')
    r = sh(sys.executable, '-m', 'playwright', 'install', '--with-deps', 'chromium'); L('playwright install:', r.returncode, (r.stderr or '')[-200:])
    sh('sudo', 'apt-get', 'install', '-y', '-qq', 'poppler-utils')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=['--disable-blink-features=AutomationControlled'])
        for pg in job.get('pages', []):
            name, url = pg['name'], pg['url']; e = dict(name=name, url=url)
            try:
                if url.lower().split('?')[0].endswith('.pdf'):
                    f = f'{out_dir}/doc_{name}.pdf'
                    open(f, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=90).read())
                    sh('pdftoppm', '-png', '-r', '170', '-f', '1', '-l', str(pg.get('pages', 2)), f, f'{out_dir}/cap_{name}')
                    e.update(ok=True, kind='pdf', bytes=os.path.getsize(f))
                else:
                    cx = br.new_context(viewport=dict(width=1920, height=pg.get('h', 1300)), device_scale_factor=2, locale='es-ES',
                                        timezone_id='Europe/Madrid', user_agent=UA)
                    p = cx.new_page()
                    resp = p.goto(url, wait_until='domcontentloaded', timeout=60000)
                    p.wait_for_timeout(4500)
                    clicked = None
                    for fr in p.frames:
                        if clicked: break
                        for t in REJECT:
                            try:
                                b = fr.get_by_role('button', name=re.compile('^' + re.escape(t) + '$', re.I)).first
                                if b.count() and b.is_visible(): b.click(timeout=2500); clicked = t; break
                            except Exception: pass
                    p.wait_for_timeout(1200)
                    hid = p.evaluate(HIDE); p.wait_for_timeout(600)
                    if pg.get('scroll'): p.evaluate(f"window.scrollTo(0, {int(pg['scroll'])})"); p.wait_for_timeout(700)
                    p.screenshot(path=f'{out_dir}/cap_{name}.png')
                    txt = ''
                    try: txt = re.sub(r'\s+', ' ', p.inner_text('body'))[:700]
                    except Exception: pass
                    e.update(ok=True, kind='web', status=resp.status if resp else None, final=p.url, title=p.title()[:200],
                             cookies=clicked or f'ocultado({hid})', texto=txt, when=time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()))
                    cx.close()
            except Exception as ex:
                e.update(ok=False, error=str(ex)[:300])
            L(name, e.get('ok'), e.get('status', ''), (e.get('title') or e.get('error') or '')[:90]); rep.append(e)
            json.dump(rep, open(f'{out_dir}/capturas.json', 'w'), ensure_ascii=False, indent=1)
        br.close()
    open(f'{out_dir}/run.log', 'w').write('\n'.join(log))
