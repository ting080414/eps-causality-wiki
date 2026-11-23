# LLM Wiki 索引（index.md）

主題：**股票回購真的會犧牲企業投資嗎？從 EPS 到因果推論**。對象：沒有財務與計量背景的初學者。

> 2026-11-22 已透過本次 ChatGPT 對話依序開啟五個公開原始網址、提取要點、與既有筆記比較、逐篇更新 Wiki 並記錄差異。這是 **Karpathy-style Markdown Wiki 實作**；沒有宣稱在外部專用平台或使用者本機 Agent 執行 CLI。

## 概念入口（每頁可回溯來源）

- [[01-eps|EPS 的定義與計算]]：基本、稀釋 EPS，加權平均股數。[S1][S2][S3]
- [[02-buyback|什麼是股票回購]]：目的、回購交易、授權和執行差別。[S2][S3]
- [[03-research|回購與企業投資研究]]：Almeida、Fos、Kronlund（2016）的研究問題、門檻比較與結果。[S3][S4][S5]
- [[04-endogeneity|相關與因果／內生性]]：成長機會等共同原因、後門路徑。[S4][S3][S5]
- [[05-rdd|Fuzzy RDD 方法]]：門檻附近的處理機率跳躍、第一階段及識別假設。[S5][S3]

## 五份已讀來源的查核摘要

- [S1] `raw/verified_notes/S1-verified.md` — IAS 33
- [S2] `raw/verified_notes/S2-verified.md` — SEC 2002 proposed rule
- [S3] `raw/verified_notes/S3-verified.md` — 作者對股票回購研究的介紹
- [S4] `raw/verified_notes/S4-verified.md` — The Effect Ch.8
- [S5] `raw/verified_notes/S5-verified.md` — The Mixtape Ch.6

## 閱讀路線

[[02-buyback|股票回購]] → [[01-eps|EPS]] → [[03-research|研究問題]] → [[04-endogeneity|內生性]] → [[05-rdd|Fuzzy RDD]]。

**完整來源資訊**：`sources/catalog.json`；**逐篇更新日誌**：[[log]]；**教學查詢紀錄**：`audit/query_trace.md`。
