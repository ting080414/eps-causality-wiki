#!/usr/bin/env python3
"""可重複執行的 Karpathy-style Wiki 品質檢查；不做網路連線。"""
from pathlib import Path
from bs4 import BeautifulSoup
import json,re,datetime
BASE=Path(__file__).resolve().parents[1]
checks=[]
def add(name,ok,details=''):
    checks.append(dict(check=name,passed=bool(ok),details=details))

cat=json.loads((BASE/'sources/catalog.json').read_text('utf-8'))
manifest=json.loads((BASE/'sources/ingestion_manifest.json').read_text('utf-8'))
records=json.loads((BASE/'audit/ingest_records.json').read_text('utf-8'))
notes=sorted((BASE/'wiki').glob('0[1-5]-*.md'))
add('五份不同來源',len(cat)==5 and len({x['url'] for x in cat})==5,'來源數 '+str(len(cat)))
add('五篇主題知識頁',len(notes)==5,'主題頁 '+str(len(notes)))
add('在 ChatGPT 中完成五份來源整合',manifest.get('in_chat_source_ingests_completed')==5 and records.get('total_ingests')==5,'不同於外部 Coding Agent 操作')
log=(BASE/'wiki/log.md').read_text('utf-8')
found=re.findall(r'^## \[2026-11-22\] ingest \| (S[1-5])\b',log,flags=re.MULTILINE)
add('五筆 Ingest 日誌',len(found)==5 and set(found)=={f'S{i}' for i in range(1,6)},f'找到 {found}')
add('Query 與 Lint 日誌','query |' in log and 'lint |' in log)
for i in range(1,6):
    sid=f'S{i}'; note=BASE/f'raw/verified_notes/{sid}-verified.md'
    diffs=list((BASE/'audit/ingest_diffs').glob(sid+'_*.diff'))
    rec=next((x for x in records['records'] if x['source_id']==sid),None)
    add(f'{sid} 來源讀取與變更紀錄',note.exists() and bool(diffs) and bool(rec) and all((BASE/'wiki'/p).exists() for p in rec['updated_pages']),f'{len(diffs)} 個 Wiki 差異檔')
for p in notes:
    body=p.read_text('utf-8')
    add(f'{p.name} 有來源標記',bool(re.search(r'\[S[1-5]\]',body)) and 'https://' in body)

# Resolve Obsidian-style wiki link target, count every inbound from main five pages + index
slugs={p.stem for p in notes}|{'log','index'}
inbound={k:0 for k in slugs}
broken=[]
for p in notes+[BASE/'wiki/index.md']:
    for link in re.findall(r'\[\[([^\]]+)\]\]',p.read_text('utf-8')):
        target=link.split('|')[0].strip().removesuffix('.md')
        if target not in slugs: broken.append((p.name,target))
        else: inbound[target]+=1
add('Wiki 內部連結有效',not broken,str(broken))
orphan=[p.stem for p in notes if inbound[p.stem]==0]
add('沒有孤兒主題頁',not orphan,str(orphan))

slides=BeautifulSoup((BASE/'slides.html').read_text('utf-8'),'html.parser')
add('11 頁 HTML 教學簡報',len(slides.select('.slide'))==11,f'count={len(slides.select(".slide"))}')
add('互動計算器與小測驗存在',bool(slides.select_one('#shareRange')) and len(slides.select('[data-q]'))==4)
add('每一頁都有可溯源教學構造',len(slides.select('.sourcefooter'))>=9,f'{len(slides.select(".sourcefooter"))} source footers')

for f in ['index.html','wiki.html','slides.html','workflow.html','繳交報告.html']:
    soup=BeautifulSoup((BASE/f).read_text('utf-8'),'html.parser')
    missing=[]
    for a in soup.select('a[href]'):
        href=a['href'].split('#')[0]
        if href and not href.startswith(('https:','http:','mailto:','javascript:')) and not (BASE/href).exists():
            missing.append(href)
    add(f'{f} 相對連結',not missing,str(missing))

report=(BASE/'繳交說明_可複製.md').read_text('utf-8')
add('繳交說明有六項',all('## '+str(i)+'.' in report for i in range(1,7)))
add('保留真實完成界線','不是' in report and 'Codex' in report and 'GitHub Pages' in report)
results={'date':'2026-11-22','total_checks':len(checks),'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'checks':checks}
(BASE/'audit/wiki_lint_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print('Wiki lint:', results['passed'],'/',results['total_checks'])
for c in checks:print('OK' if c['passed'] else 'FAIL',c['check'],c.get('details',''))
if results['failed']:raise SystemExit(1)
