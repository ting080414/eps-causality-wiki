# 股票回購與因果推論｜Karpathy LLM Wiki × 互動 HTML 簡報


## 快速入口

- [網站首頁](index.html) — 可直接在瀏覽器開啟
- [LLM Wiki 網頁](wiki.html) — 五個概念的可瀏覽版本
- [11 頁互動 HTML 教學簡報](slides.html) — 翻頁、EPS 計算器、小測驗
- [流程圖與反思](workflow.html)｜[Markdown 原文](workflow.md)

## 符合 Karpathy Wiki 的結構

- `AGENTS.md`：Ingest／Query／Lint 工作規則
- `raw/`：五份來源定位卡；`raw/verified_notes/`：本次打開原始公開網頁後寫的來源核對摘要（不是網頁全文）
- `wiki/01–05-*.md`：五個互相連結的知識頁
- `wiki/index.md`：概念索引
- `wiki/log.md`：五筆實際 source-to-wiki Ingest 與 Query／Lint 操作紀錄
- `audit/ingest_diffs/`：逐篇更新 Markdown 的實際 diff
- `audit/query_trace.md`：11 頁簡報從哪個 Wiki 條目來
- `audit/test_results.json` 與 `audit/wiki_lint_results.json`：HTML 與 Wiki 檢查結果


## 原始資料來源

五份資料與網址完整列在 `sources/catalog.json`。LLM Wiki 設計參照 https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f。
