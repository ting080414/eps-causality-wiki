from pathlib import Path
from bs4 import BeautifulSoup
import json, subprocess, datetime, http.server, socketserver, threading, functools
from playwright.sync_api import sync_playwright
base=Path(__file__).resolve().parent.parent
checks=[]
def record(name,ok,details):
    checks.append({'check':name,'passed':bool(ok),'details':details})

source=json.loads((base/'sources/catalog.json').read_text('utf-8'))
manifest=json.loads((base/'sources/ingestion_manifest.json').read_text('utf-8'))
notes=list((base/'wiki').glob('0[1-5]-*.md'))
record('5 verified-source records',len(source)==5 and all(x['url'].startswith('https://') for x in source), f'{len(source)} sources in catalog')
record('5 prepared wiki topic notes',len(notes)==5 and len(manifest['items'])==5, f'{len(notes)} topic notes and {len(manifest["items"])} source-to-note mappings; no claim of verified agent ingestion')
record('Karpathy project structure',all((base/x).exists() for x in ['AGENTS.md','wiki/index.md','wiki/log.md','raw/README.md']), 'schema, index, log, and raw folder present')
for f in ['index.html','wiki.html','slides.html','workflow.html']:
    soup=BeautifulSoup((base/f).read_text('utf-8'),'html.parser')
    broken=[]
    for a in soup.select('a[href]'):
        href=a['href'].split('#')[0]
        if href and not href.startswith(('http://','https://','mailto:')) and not (base/href).exists():broken.append(href)
    record(f'local-links {f}',not broken, f'broken relative links: {broken}')
server=socketserver.TCPServer(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(base)))
threading.Thread(target=server.serve_forever,daemon=True).start()
site=f"http://127.0.0.1:{server.server_address[1]}/"
try:
 with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
    page=browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.set_content((base/'slides.html').read_text('utf-8'))
    record('slide count',page.locator('.slide').count()==11,f'count={page.locator(".slide").count()}')
    record('initial slide shown',page.locator('.slide.active').get_attribute('data-slide')=='1','initial active slide = '+str(page.locator('.slide.active').get_attribute('data-slide')))
    page.get_by_role('button',name='下一頁 →').click()
    record('next click',page.locator('.slide.active').get_attribute('data-slide')=='2', f'active slide={page.locator(".slide.active").get_attribute("data-slide")}')
    page.keyboard.press('ArrowRight')
    record('keyboard next',page.locator('.slide.active').get_attribute('data-slide')=='3', f'active slide={page.locator(".slide.active").get_attribute("data-slide")}')
    page.evaluate('(n)=>{at=n-1;render()}',4)
    page.locator('#shareRange').fill('80')
    record('EPS interactive calculator',page.locator('#epsNow').inner_text()=='1.25',f'after setting 80 shares, EPS={page.locator("#epsNow").inner_text()}')
    page.evaluate('(n)=>{at=n-1;render()}',10)
    page.locator('[data-q="1"][data-right="0"]').click()
    record('quiz correct response','答對了' in page.locator('#ans1').inner_text(),page.locator('#ans1').inner_text())
    page.evaluate('(n)=>{at=n-1;render()}',11)
    record('last slide navigation',page.locator('#next').is_disabled(),'next disabled at 11')
    record('JS runtime errors',not errors,str(errors))
    page.screenshot(path=str(base/'audit'/'slides_preview.png'),full_page=False)
    page.set_content((base/'wiki.html').read_text('utf-8'))
    record('wiki five pages',page.locator('.wiki-article').count()==5,f'pages={page.locator(".wiki-article").count()}')
    page.locator('[data-slug="05-rdd"]').click()
    record('wiki navigation',page.locator('#a-05-rdd').is_visible(),'05-rdd displayed')
    page.screenshot(path=str(base/'audit'/'wiki_preview.png'),full_page=False)
    browser.close()
except Exception as e:
    record('browser runtime exception',False,str(e))
finally:
    server.shutdown()
summary={'tested_at':'2026-11-22 (local project build, Asia/Taipei)','total_checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'checks':checks,'manual_review':['IAS 33: basic EPS denominator uses weighted average ordinary shares','The Real Effects of Share Repurchases (2016): report findings local to its design; do not extrapolate to all buybacks','Fuzzy RDD: probability jump, not deterministic assignment','Slide RDD illustration explicitly labeled conceptual rather than empirical']}
(base/'audit'/'test_results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'total':summary['total_checks'],'passed':summary['passed'],'failed':summary['failed']},ensure_ascii=False))
for c in checks:
 print(('OK' if c['passed'] else 'FAIL'),c['check'],'-',c['details'])
if summary['failed']:raise SystemExit(1)
