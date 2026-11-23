# LLM Wiki 操作日誌（log.md）

> 真實範圍：以下五次 Ingest 是**本次 ChatGPT 對話中**使用網頁查閱工具逐篇讀取原始公開網頁，並在專案內**實際更新 Markdown** 的紀錄；可查 `raw/verified_notes/` 與 `audit/ingest_diffs/`。不是使用者本機 Claude Code／Codex 的操作截圖，也不是第三方 hosted LLM Wiki 的 API 匯入。

## [2026-11-22] discuss | 先討論教學範圍
- 與使用者前段對話確認採 Karpathy 的 LLM Wiki 設計，沿用股票回購、EPS、相關與因果的教學主題。
- 目標讀者為一般大學生；原則為先說明 EPS 與回購，再說明因果疑問，最後才介紹 Fuzzy RDD。
- 預先訂出來源查核規則：不可將「回購導致 EPS 上升」當作必然、不可把相關當因果、不可外推 RDD 的局部發現。

## [2026-11-22] ingest | S1 — IAS 33 – Earnings per Share
- 原始資料：https://www.ifrs.org/issued-standards/list-of-standards/ias-33-earnings-per-share.html/
- 讀到的原文位置：About（IAS 33 的基本 EPS、稀釋 EPS 與分母說明）
- 抽取重點：IAS 33 規範基本與稀釋每股盈餘的呈現；基本 EPS 的分母是報導期間加權平均流通在外普通股數，期間股數的變動可能影響分母。
- 增量修改：`wiki/01-eps.md`；重新整理 `wiki/index.md`。
- 查核／風險：本教學的固定盈餘、固定股數比較是簡化示例；實際計算應考慮回購時間、權益證券變動與盈餘定義。
- 留存證據：`raw/verified_notes/S1-verified.md`、`audit/ingest_diffs/S1_*.diff`。

## [2026-11-22] ingest | S2 — SEC Rule 10b-18 Proposed Rule (2002)
- 原始資料：https://www.sec.gov/files/rules/proposed/33-8160.htm
- 讀到的原文位置：Action: Proposed rule；I. Introduction
- 抽取重點：SEC 2002 年的修正提案說明，公司買回自身股份可能出於回饋股東、配合員工持股安排、調整股本等原因；並討論買回交易的方式、時間、價格、數量安全港條件及揭露議題。
- 增量修改：`wiki/02-buyback.md`, `wiki/01-eps.md`；重新整理 `wiki/index.md`。
- 查核／風險：2002 年文件是提案而非最新現行規則；不得藉此直接推論個別公司已執行回購。
- 留存證據：`raw/verified_notes/S2-verified.md`、`audit/ingest_diffs/S2_*.diff`。

## [2026-11-22] ingest | S3 — The Real Effects of Share Repurchases – Harvard Law Forum author overview
- 原始資料：https://corpgov.law.harvard.edu/2016/02/08/the-real-effects-of-share-repurchases/
- 讀到的原文位置：2016-02-08 作者文章，討論門檻與後四季企業決策（內文前半與研究結果）
- 抽取重點：Almeida、Fos、Kronlund 利用假設沒有回購時 EPS 會否略低於分析師預期的門檻，研究因 EPS 需求而提高回購機率的公司；作者報告後續四季資本支出、研發、聘僱下降的結果。
- 增量修改：`wiki/03-research.md`, `wiki/02-buyback.md`, `wiki/01-eps.md`；重新整理 `wiki/index.md`。
- 查核／風險：此來源是作者對論文的公開介紹，不等於全文實證表格；不應說成所有公司回購一定降低投資。
- 留存證據：`raw/verified_notes/S3-verified.md`、`audit/ingest_diffs/S3_*.diff`。

## [2026-11-22] ingest | S4 — The Effect Ch. 8 – Causal Paths and Closing Back Doors
- 原始資料：https://www.theeffectbook.net/ch-CausalPaths.html
- 讀到的原文位置：8.1 I Walk the Line；causal paths / alternate explanations
- 抽取重點：因果圖的不同路徑可以解釋為什麼兩個變數有相關；共同原因形成額外路徑，使相關不必然代表關心的直接因果關係。
- 增量修改：`wiki/04-endogeneity.md`, `wiki/03-research.md`；重新整理 `wiki/index.md`。
- 查核／風險：因果圖方向代表研究者的因果假設，單靠觀察到相關不等於已驗證每一支箭頭。
- 留存證據：`raw/verified_notes/S4-verified.md`、`audit/ingest_diffs/S4_*.diff`。

## [2026-11-22] ingest | S5 — Causal Inference: The Mixtape Ch. 6 – Regression Discontinuity
- 原始資料：https://mixtape.scunning.com/06-regression_discontinuity
- 讀到的原文位置：6.2.7 The Fuzzy RD Design；6.3 Challenges to Identification
- 抽取重點：Sharp RDD 中處理狀態由門檻確定；Fuzzy RDD 中處理機率在門檻出現跳躍，但處理不是完全確定。該章提到 IV 相關識別假設及門檻附近受影響者的局部效果。
- 增量修改：`wiki/05-rdd.md`, `wiki/03-research.md`, `wiki/04-endogeneity.md`；重新整理 `wiki/index.md`。
- 查核／風險：需要檢查門檻附近連續性、操弄等威脅；投影片中的跳躍線條只是概念圖，不是論文原始回歸結果。
- 留存證據：`raw/verified_notes/S5-verified.md`、`audit/ingest_diffs/S5_*.diff`。

## [2026-11-22] query | 以 Wiki 生成人看得懂的教學簡報
- 問題：「沒有金融背景的人，如何理解股票回購、EPS 與因果研究？」
- 查詢路徑：先讀 `wiki/index.md`，依概念導覽讀 `02-buyback.md`、`01-eps.md`、`03-research.md`、`04-endogeneity.md`、`05-rdd.md`。
- 產出：`slides.html` 的 11 頁教學順序與來源標註，並保存 `audit/query_trace.md`。

## [2026-11-22] lint | 來源連結、Wiki 交叉參照與 HTML 功能查核
- 檢查來源共 5 篇、概念頁 5 篇、五次來源讀取、跨頁連結、投影片頁數、互動計算器、測驗與本機相對路徑。
- 歷程中的可觀察錯誤：先前組裝時簡報頁數漏計封面；增加索引與日誌後，測試腳本曾把管理檔誤算成 Wiki 主題頁。
- 調整：在檔案結構和 HTML 建置階段檢查頁數與檔案類型；更早在 Ingest 核對 EPS 加權平均股數、SEC 提案年代與 Fuzzy RDD 的推論限制。
- 留存證據：`audit/test_results.json`、`audit/wiki_lint_results.json` 與 `audit/query_trace.md`。

