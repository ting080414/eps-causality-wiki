# 股票回購與因果推論｜Karpathy LLM Wiki × 互動 HTML 簡報

> **這份是課堂作業的完整可交付專案。** 說明六個必繳項目請看 [繳交說明_可複製.md](繳交說明_可複製.md)，實際流程與反思請看 [workflow.md](workflow.md)。請先把姓名、學號和 GitHub Pages 連結補齊。

## 快速入口

- [網站首頁](index.html) — 可直接在瀏覽器開啟
- [LLM Wiki 網頁](wiki.html) — 五個概念的可瀏覽版本
- [11 頁互動 HTML 教學簡報](slides.html) — 翻頁、EPS 計算器、小測驗
- [流程圖與反思](workflow.html)｜[Markdown 原文](workflow.md)
- [繳交報告](繳交報告.html)｜[可貼上作業區的 Markdown](繳交說明_可複製.md)

## 符合 Karpathy Wiki 的結構

- `AGENTS.md`：Ingest／Query／Lint 工作規則
- `raw/`：五份來源定位卡；`raw/verified_notes/`：本次打開原始公開網頁後寫的來源核對摘要（不是網頁全文）
- `wiki/01–05-*.md`：五個互相連結的知識頁
- `wiki/index.md`：概念索引
- `wiki/log.md`：五筆實際 source-to-wiki Ingest 與 Query／Lint 操作紀錄
- `audit/ingest_diffs/`：逐篇更新 Markdown 的實際 diff
- `audit/query_trace.md`：11 頁簡報從哪個 Wiki 條目來
- `audit/test_results.json` 與 `audit/wiki_lint_results.json`：HTML 與 Wiki 檢查結果

**Ingest 限定語**：五份原始公開網頁是在 **2026-11-22 本次 ChatGPT 對話裡**逐篇開啟並整合至 Wiki。這不是在 GitHub、Codex、Claude Code 或其他外部系統中自動匯入，也沒有捏造使用者端的操作截圖。

## 如何上傳讓老師看到連結

1. 在 GitHub 建立公開 repository，例如 `eps-llm-wiki`。
2. 把**本資料夾裡面**的所有檔案直接上傳到 repository 根目錄，不要多包一層資料夾。
3. GitHub → Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save。
4. 確認網站正式可瀏覽，貼上 `https://帳號.github.io/資料庫名稱/wiki.html` 和 `/slides.html` 的**真實網址**到繳交說明。
5. 把繳交標題中的【學號】、【姓名】換成真實資料即可。

## 原始資料來源

五份資料與網址完整列在 `sources/catalog.json`。LLM Wiki 設計參照 https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f。
