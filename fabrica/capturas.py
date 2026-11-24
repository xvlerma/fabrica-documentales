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

MODAL = """
(() => { let n = 0; const A = innerWidth * innerHeight;
  for (const e of document.querySelectorAll('body *')) { const c = getComputedStyle(e);
    if (c.position !== 'fixed' && !(c.position === 'absolute' && parseInt(c.zIndex || '0') >= 50)) continue; const r = e.getBoundingClientRect();
    if (r.width * r.height > 0.12 * A && !(r.top <= 0 && r.height < 220)) { e.style.setProperty('display', 'none', 'important'); n++; } }
  for (const e of document.querySelectorAll('[role=dialog],[aria-modal=true]')) { e.style.setProperty('display', 'none', 'important'); n++; }
  for (const e of [document.documentElement, document.body]) e.style.setProperty('overflow', 'auto', 'important');
  return n; })()
"""

def sh(*a, **k): return subprocess.run(list(a), capture_output=True, text=True, **k)

CLICK = """
(() => { const re = /rechaz|rebutj|reject|deneg|declin|solo (las )?necesarias|sólo (las )?necesarias|continuar sin aceptar/i;
  const no = /pagar|suscri|subscri|config|ajust|prefer|pol[ií]tica|m[aá]s info/i;
  const all = []; const walk = (root) => { for (const e of root.querySelectorAll('*')) { all.push(e); if (e.shadowRoot) walk(e.shadowRoot); } };
  walk(document);
  for (const e of all) {
    const tag = e.tagName; if (tag === 'SCRIPT' || tag === 'STYLE') continue;
    const t = ((e.childElementCount ? '' : (e.textContent || '')).trim() || (e.value && typeof e.value === 'string' ? e.value : '')).trim();
    if (!t || t.length > 45 || !re.test(t) || no.test(t)) continue;
    const r = e.getBoundingClientRect(); if (r.width < 8 || r.height < 8) continue;
    const tgt = e.closest('button, a, input, [role=button], [onclick]') || e;
    for (const ty of ['pointerdown', 'mousedown', 'pointerup', 'mouseup']) tgt.dispatchEvent(new MouseEvent(ty, {bubbles: true, cancelable: true, view: window}));
    tgt.click(); return t; }
  return ''; })()
"""

DBG = """
(() => { const h = document.documentElement.outerHTML; const i = h.search(/Rechazar todas/i);
  return i < 0 ? 'no-en-html iframes=' + document.querySelectorAll('iframe').length : h.slice(Math.max(0, i - 900), i + 300); })()
"""

WB = """
(() => { let n = 0; for (const s of ['#wm-ipp-base', '#wm-ipp', '#wm-ipp-print', '#donato']) for (const e of document.querySelectorAll(s)) { e.style.setProperty('display', 'none', 'important'); n++; } return n; })()
"""

def ev(cx, p, js):
    """evaluate que no depende del script de utilidad de Playwright (hay webs que pisan Map/Set)."""
    try: return p.evaluate(js)
    except Exception:
        try:
            r = cx.new_cdp_session(p).send('Runtime.evaluate', {'expression': js, 'returnByValue': True})
            return (r.get('result') or {}).get('value')
        except Exception as ex: return 'err:' + str(ex)[:40]

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
                    wb = bool(pg.get('wayback'))
                    resp = p.goto(('https://web.archive.org/save/' + url) if wb else url, wait_until='domcontentloaded', timeout=180000 if wb else 60000)
                    p.wait_for_timeout(9000 if wb else 4500)
                    if wb: ev(cx, p, WB)
                    clicked = None
                    pat = re.compile(r'rechaz|rebutj|reject|deneg|declin|solo (las )?necesarias|sólo (las )?necesarias|continuar sin aceptar', re.I)
                    for fr in p.frames:
                        if clicked: break
                        for role in ('button', 'link'):
                            try:
                                bs = fr.get_by_role(role, name=pat)
                                for i in range(min(bs.count(), 4)):
                                    b = bs.nth(i)
                                    if b.is_visible(): b.click(timeout=2500); clicked = 'rechazar'; break
                            except Exception: pass
                            if clicked: break
                    if not clicked and not pg.get('noclick'):
                        for _ in range(3):
                            t = ev(cx, p, CLICK)
                            if t and not str(t).startswith('err:'): clicked = 'rechazar-js(' + str(t)[:30] + ')'; break
                            p.wait_for_timeout(1500)
                    p.wait_for_timeout(1500)
                    if pg.get('dbg'): e['dbg'] = str(ev(cx, p, DBG))[:1400]
                    hid = ev(cx, p, HIDE); p.wait_for_timeout(600)
                    if pg.get('hide'):
                        ev(cx, p, "(() => { let n = 0; for (const e of document.querySelectorAll(%s)) { e.style.setProperty('display', 'none', 'important'); n++; } return n; })()" % json.dumps(pg['hide']))
                    if pg.get('modal'):
                        try: p.keyboard.press('Escape')
                        except Exception: pass
                        hid = str(hid) + '+' + str(ev(cx, p, MODAL)); p.wait_for_timeout(500)
                    if pg.get('scroll'): ev(cx, p, f"window.scrollTo(0, {int(pg['scroll'])})"); p.wait_for_timeout(700)
                    p.screenshot(path=f'{out_dir}/cap_{name}.png')
                    if pg.get('pdfs'):
                        docs = []
                        try:
                            ls = ev(cx, p, "(() => [...document.querySelectorAll('a[href]')].map(a => [a.href, (a.textContent || '').trim().slice(0, 120)]).filter(x => /\\.pdf|\\/stfls\\/|Archivos|descarga/i.test(x[0])).slice(0, 12))()") or []
                            for i, (h, t) in enumerate(ls):
                                try:
                                    b = cx.request.get(h, timeout=60000).body()
                                    if b[:4] == b'%PDF' and len(b) < 24_000_000:
                                        fn = f'doc_{name}_{i + 1:02d}.pdf'; open(f'{out_dir}/{fn}', 'wb').write(b); docs.append(dict(file=fn, texto=t, url=h, bytes=len(b)))
                                    else: docs.append(dict(texto=t, url=h, nota='no es PDF', bytes=len(b)))
                                except Exception as ex: docs.append(dict(texto=t, url=h, error=str(ex)[:80]))
                        except Exception as ex: docs.append(dict(error=str(ex)[:120]))
                        e['docs'] = docs
                    txt = ''
                    try: txt = re.sub(r'\s+', ' ', p.inner_text('body'))[:700]
                    except Exception: txt = re.sub(r'\s+', ' ', str(ev(cx, p, 'document.body.innerText.slice(0, 900)') or ''))[:700]
                    try: ttl = p.title()[:200]
                    except Exception: ttl = str(ev(cx, p, 'document.title') or '')[:200]
                    e.update(ok=True, kind='web', status=resp.status if resp else None, final=p.url, title=ttl, via=('wayback' if wb else 'directo'),
                             cookies=clicked or f'ocultado({hid})', texto=txt, when=time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()))
                    cx.close()
            except Exception as ex:
                e.update(ok=False, error=str(ex)[:300])
            L(name, e.get('ok'), e.get('status', ''), (e.get('title') or e.get('error') or '')[:90]); rep.append(e)
            json.dump(rep, open(f'{out_dir}/capturas.json', 'w'), ensure_ascii=False, indent=1)
        br.close()
    open(f'{out_dir}/run.log', 'w').write('\n'.join(log))
