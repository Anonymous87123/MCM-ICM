# blocked 行：job 越界 2 行的逐行裁定建议（只出建议，不落裁定）

- 对象：`lanes/L9-merge-dryrun/reports/rows.jsonl` 中 `blocked==["job-outside-vocabulary"]` 的 2 行
- 共同归属：论文 `P-A-2018-76271-27d535ab`，章 `model-establishment`（`heading` 为 null），类型 A，`quote_level` = `in-record`
- 现状：两行的 `job`、`base_job` 均为占位值 `unresolved`，`close_job` 为 null，都不在 `JOBS_13`（route, define, source, select, derive, compute, read-figure, compare, check, limit, mechanism, interpret, handoff）内，故被挡
- 证据来源：`lanes/L6-a-evidence/records-a/P-A-2018-76271-27d535ab.json` 的 blocks 29 / 30，行文本与 `quote` 字段逐字一致
- 本文件不给裁定；下表的"建议"由用户拍板

## 结论

| 行 | 论文 | block | 页 | 现 job | 建议 job | 置信 |
|---:|------|------:|---:|--------|----------|------|
| 1161 | P-A-2018-76271-27d535ab | 29 | 9 | `unresolved` | `route` | 中（`mechanism` 可辩） |
| 1162 | P-A-2018-76271-27d535ab | 30 | 10 | `unresolved` | `derive` | 高 |

两值均在 `JOBS_13` 内，`JOBS_13` 不需扩容；采纳后仅需改该 record 的 block 29/30 并重跑 dry-run。

## 邻接上下文（同论文相邻 block，均已是 merge 状态）

| block_index | job | page | 引文（截断） |
|---|---|---|---|
| 26 | `interpret` | 7 | All the signal loss occurs between the two antennae, with no loss due to cabling, |
| 27 | `compare` | 8 | The communications link only needs to be complete in one direction, meaning that |
| 28 | `route` | 9 | The model is constructed in order to accurately create the path of the bouncing signal. |
| **29** | **`unresolved`** | **9** | 见下 |
| **30** | **`unresolved`** | **10** | 见下 |

## 行 1161

- `paper` = P-A-2018-76271-27d535ab，`block_index` = 29，`page` = 9，`chapter` = model-establishment，`status` = blocked
- 引文（逐字）："The first portion of the model consists of the signal travelling from the ground to the ionosphere, refracting, and travelling from the ionosphere back to the ground."
- 建议 `job` = **`route`**
- 理由：该句把信号传播拆成"地面→电离层→折射→回流"的路段，与紧邻的 block 28（`route`，明确说模型用于刻画 bouncing signal 的 path）说的是同一条径迹的延续，故按路径追踪编码。
- 备选：`mechanism`。若判定这句是在说明物理过程如何发生、而非描述几何径迹，则改 `mechanism` 更准；两者差别就是"路径"对"机理"，本句同时含两者成分，属边界句。
- 不建议：`define`（未给术语定义）、`derive`（无公式推导）、`compute`（无数值）。

## 行 1162

- `paper` = P-A-2018-76271-27d535ab，`block_index` = 30，`page` = 10，`chapter` = model-establishment，`status` = blocked
- 引文（逐字）："The distance from the transmitter to the ionosphere is determined from the law of sines using the equation"
- 建议 `job` = **`derive`**
- 理由：句子陈述"由正弦定理按方程求出该距离"，是以公式/定律导出量，符合 `derive`；`using the equation` 明确指向推导而非代入数值。
- 备选：`compute`。若紧随的方程已给出全部数值、该句实际在算具体距离，则改 `compute`；建议用户看该页方程是否纯符号。
- 不建议：`route`（不描路径）、`select`（不在候选中挑）、`read-figure`（未引图）。

## 影响与前置条件

- 这两行一旦给定 `job`，`status` 从 blocked 转 merge，`job` 分布统计（`stats.json`）与 `row-shape.md` 的 merge 计数会同步变化；本文件不改 `rows.jsonl`、不改 `stats.json`、不改 record。
- 若用户采用 `route` + `derive`，则 `JOBS_13` 不需要扩容：两值均已在词表内，改动仅落在 record 的 block 29 / 30 与重跑 dry-run。
- 若用户改选 `mechanism` / `compute`，同样无需扩容。

## 合计核对

- 本文件覆盖 2 行（1161、1162）
- 与 `blocked-labels.md` 的 604 行相加 = **606**，等于 `status=="blocked"` 行总数
