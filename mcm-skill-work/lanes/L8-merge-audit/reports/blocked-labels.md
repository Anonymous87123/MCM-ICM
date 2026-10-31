# blocked 行：未裁定章标签的处置建议（只出建议，不落裁定）

- 对象：`lanes/L9-merge-dryrun/reports/rows.jsonl` 中 `status=="blocked"` 且 `blocked==["chapter-label-unruled"]` 的行
- 行数：604 行，11 个标签，跨 33 篇论文（`recommendation` 与 `model-testing` 有 9 篇重叠）
- 行号 = `rows.jsonl` 的物理行号（从 1 起）；每行另可经 `source_quote_file` + `source_quote_row` 回溯到引文
- 词表基线：`lanes/L9-merge-dryrun/tools/build_rows.py`（14 章功能 + `ALIASES` 7 条 + `STRUCTURAL`/`FRONT_MATTER` 3 条）
- 本文件不给裁定；下列"建议动作/归入"是提案，最终由用户拍
- 11 个标签逐个核过正文引文（不只看章名），其中 2 个按行段拆开（见"细分"节）

## 结论表

| # | 原标签 | 行数 | 论文 | 行号范围 | 建议动作 | 归入词表项 | 一句理由 |
|---|--------|-----:|-----:|----------|----------|------------|----------|
| 1 | `recommendation` | 399 | 23 | 34392–40518 | 归并 | `memo` | 被标此名的章一律是队伍对外递交的政策文书（致联合国秘书长信、Policy Proposal、Policy Setting、UN Charter），正是 `memo` 的对外文书功能 |
| 2 | `model-testing` | 135 | 11 | 37107–40146 | 归并 | `robustness-verification` | 章内动作是对已建模型回测检验（一致性矩阵检验、Historical/Regional 校验、Model Validation、回归检验），即"建成后再验"（13 行例外除外，见细分 A） |
| 3 | `recommendations` | 24 | 1 | 26076–26099 | 归并 | `memo` | 主体（6.2 两节）是"基于分析结果的建议"条目，动作多为 select/handoff；6.1 的 4 行属结果，见细分 B |
| 4 | `gcn-evidence` | 9 | 1 | 26975–26983 | 归并 | `results` | 章名 "Evidence from GCN: Can We Find More Information from the Structure"，报的是训练后网络给出的发现，非方法 |
| 5 | `cultural-analysis` | 8 | 1 | 24494–24501 | 归并 | `strengths-limitations` | "Inter-cultural Applicability"全节在讲模型换到别国文化假设下还成不成立（如优先级队列的可接受性），是适用边界讨论 |
| 6 | `technology-impact` | 7 | 1 | 25231–25237 | 归并 | `model-establishment` | "Impact from Advanced Technologies / 6.1 Batteries"是把技术趋势写进情景设定，属建模设定输入 |
| 7 | `our-work` | 7 | 1 | 25431–25437 | 归并 | `introduction` | "1.3 Our work"是引言章下的路线声明（"We construct two distinctive models…"），与已裁定的 `problem-analysis→introduction` 同位 |
| 8 | `advice` | 5 | 1 | 26509–26513 | 归并 | `results` | 5 个 block 全是教练条件下的指标分析与解读（read-figure/interpret），是结果不是建议；章名虽曰 advice，编码内容不含建议 |
| 9 | `future-considerations` | 5 | 1 | 26614–26618 | 归并 | `future-improvements` | 引文为 "With more time, we could create networks…"，标准 future work；该名已是既有别名（→`strengths-limitations`） |
| 10 | `illustration` | 4 | 1 | 25271–25274 | 归并 | `introduction` | 位于 1.3，与同章的 `problem-restatement`（已裁定→introduction）并列，是背景铺垫 |
| 11 | `heavy-trucks` | 1 | 1 | 25408 | 归并 | `results` | "8 Comment on Heavy Trucks"是分析正文对一类车型的补充评述（重卡续航与超充需求），是分析结论 |

**动作分布：归并 604 行 / 新增 0 行 / 丢弃 0 行。**
11 个标签全部可被既有 24 项词表吸收，无需扩词表。若用户不接受 `recommendation→memo` 这类跨族归并，最小改动是新增 1 个建议族名（并给 `recommendations`/`advice` 各留 1 条别名），其余照表。

## 采纳后的 604 行去向

| 归入项 | 行数 | 构成 |
|--------|-----:|------|
| `memo` | 419 | `recommendation` 399 + `recommendations` 20 |
| `robustness-verification` | 122 | `model-testing` 135 − 13 |
| `model-establishment` | 20 | `model-testing` 例外 13 + `technology-impact` 7 |
| `results` | 19 | `gcn-evidence` 9 + `advice` 5 + `recommendations` 4 + `heavy-trucks` 1 |
| `strengths-limitations` | 13 | `cultural-analysis` 8 + `future-considerations` 5 |
| `introduction` | 11 | `our-work` 7 + `illustration` 4 |

419 + 122 + 20 + 19 + 13 + 11 = **604**。

## 细分（两处按行段拆，不是整标签一个去向）

### A. `model-testing` 的 13 行不是检验
- P-F-2024-2417340-491a7b05 "6.3.2 Training of BP Neural Network"，4 行，40143–40146 → `model-establishment`
- P-F-2022-2220722-8f8dab63 "7.3 Prediction of impacts by GM forecasting model"，9 行，38868–38876 → `model-establishment`
- 判据：训练与预测是建模/应用，不是对已建模型的回测；其余 122 行（含 "3.5 Model Validation"、"5.3 Multivariate Linear Regression Test"、"7.1 Consistency Inspection of Pairwise Comparison Matrix A"）保留 `robustness-verification`

### B. `recommendations` 的 4 行不是建议
- 26076–26079 落在 6.1 "Results of Team Performance Model of Huskies Team"（含 2 行标题 block、1 行回归、1 行多重共线性检验）→ `results`
- 26080–26099 落在 6.2.1/6.2.2 "Suggestions Based on …"，动作以 select/handoff 为主 → `memo`
- 判据：同一标签跨"结果"与"建议"两节，按 block 所在小节切分，不按标签切分

## 逐标签明细（论文 → 行段）

### 1. `recommendation` — 399 行 / 23 篇

| 论文 | 行数 | 行号 |
|------|-----:|------|
| P-F-2016-43181-88427331 | 10 | 34392–34401 |
| P-F-2016-44348-d3da2a69 | 5 | 34527–34531 |
| P-F-2020-2013233-f7fd24e3 | 36 | 36813–36848 |
| P-F-2020-2013733-073f48f7 | 6 | 36918–36923 |
| P-F-2020-2013772-594465e5 | 6 | 37044–37049 |
| P-F-2021-2102185-018cbd61 | 22 | 37186–37207 |
| P-F-2021-2103649-5f40ae4f | 54 | 37353–37406 |
| P-F-2021-2106074-d0b37839 | 33 | 37502–37541 |
| P-F-2021-2109443-9398701f | 21 | 37679–37699 |
| P-F-2021-2122374-0c765494 | 19 | 37848–37866 |
| P-F-2021-2123945-e8b5b6e5 | 27 | 38008–38034 |
| P-F-2022-2204803-b65fac0e | 18 | 38185–38202 |
| P-F-2022-2208238-5a8ba6a9 | 23 | 38275–38326 |
| P-F-2022-2209952-fcd31d6e | 13 | 38459–38471 |
| P-F-2022-2211240-e209939c | 11 | 38591–38601 |
| P-F-2022-2218577-d61b87f7 | 9 | 38719–38727 |
| P-F-2022-2220722-8f8dab63 | 6 | 38877–38882 |
| P-F-2022-2224021-25b6c5d5 | 15 | 39030–39044 |
| P-F-2023-2311258-7008e4b0 | 8 | 39364–39371 |
| P-F-2023-2311517-83b94523 | 12 | 39513–39524 |
| P-F-2023-2315018-a355e166 | 9 | 39694–39702 |
| P-F-2024-2409949-da56f15f | 22 | 39768–39789 |
| P-F-2024-2426941-d347a3c2 | 14 | 40442–40518 |

支撑：章名 "Policy recommendation letter"、"A Letter to UN: A Policy Recommendation"、"6.1 Policy recommendations"、"6 Policy Proposal"、"9. UN Charter for Asteroid Development"；引文 "Dear UN Secretary General and the Chief of Migration, …"。

已知不纯但不拆的 3 章（共 36 行）：P-F-2021-2106074 "4.2 Vision for the next 15 years"（15 行，37502–37516）、P-F-2022-2208238 "7.3 Asteroid Mining Vision"（11 行，38275–38285）、P-F-2021-2109443 "5.2 The Ideal Vision for Italy's Higher Education System"（10 行，37679–37688）。这三节是"愿景/目标"而非条文，严格说更近 `assumptions`；但 7.3 愿景与同篇 "9. UN Charter" 是同一个提案包，拆开会把一份文书劈成两格，故整标签归 `memo`，只在此备案。

### 2. `model-testing` — 135 行 / 11 篇

| 论文 | 行数 | 行号 | 备注 |
|------|-----:|------|------|
| P-F-2020-2013772-594465e5 | 11 | 37107–37117 | 一致性矩阵检验 |
| P-F-2021-2109443-9398701f | 29 | 37700–37728 | 政策有效性评估 |
| P-F-2021-2122374-0c765494 | 6 | 37879–37884 | 反比关系检验 |
| P-F-2021-2123945-e8b5b6e5 | 26 | 38035–38060 | 有效性评估 |
| P-F-2022-2204803-b65fac0e | 4 | 38138–38141 | Model Validation |
| P-F-2022-2208238-5a8ba6a9 | 12 | 38248–38262 | 公平性交叉核 |
| P-F-2022-2209952-fcd31d6e | 8 | 38391–38398 | Model Validation |
| P-F-2022-2220722-8f8dab63 | 24 | 38802–38876 | 含 9 行预测（38868–38876）→ 见细分 A |
| P-F-2022-2224021-25b6c5d5 | 3 | 38958–38960 | Validation |
| P-F-2024-2413565-15e84639 | 8 | 40005–40012 | 多元线性回归检验 |
| P-F-2024-2417340-491a7b05 | 4 | 40143–40146 | BP 训练 → 见细分 A |

### 3. `recommendations` — 24 行 / 1 篇
P-D-2020-2003723-28f692ff，26076–26099。章 "6 Structural Strategy Analysis and Suggestions"：6.1 结果（26076–26079 → `results`）、6.2.1 与 6.2.2 建议（26080–26099 → `memo`）。见细分 B。

### 4. `gcn-evidence` — 9 行 / 1 篇
P-D-2021-2101855-c4682962，26975–26983。章 "6.2 Evidence from GCN: Can We Find More Information from the Structure"，引文含 "Figure 16: Principles and Results for GCN"。→ `results`。

### 5. `cultural-analysis` — 8 行 / 1 篇
P-D-2017-67316-f37f83c8，24494–24501，页 16–17。引文："Different cultural norms have an impact on passengers' punctuality."、"…with our passenger arrival behavior model (see Section 7), we can say that the passenger flow in countries where people are…"、"Another cultural impact on our model is the acceptability of priority queueing in different nations."
→ `strengths-limitations`：全节在检验模型对别国文化假设的适用性。备案：24498–24499 两句属"给机场的运营建议"，若用户愿意按 block 切分，这 2 行可走 `memo`。

### 6. `technology-impact` — 7 行 / 1 篇
P-D-2018-82504-6cc63169，25231–25237，页 30–32。章 "6 Impact from Advanced Technologies"，子节 "6.1 Batteries"；引文 "The development of battery technology will influence the charging network in two ways."、"…replacing traditional vehicles with electric ones is the best choice for human development."
→ `model-establishment`：把技术趋势固化成建模情景。（次选 `assumptions`；若用户认为该节不参与建模只作论述，改 `strengths-limitations`。）

### 7. `our-work` — 7 行 / 1 篇
P-D-2019-1900007-65267201，25431–25437。章 "1.3 Our work"；引文 "We construct two distinctive models: the 2D Island-Bridge Model (2D-IBM) and the 3D Cellular Automata Model (3D-CAM)."。→ `introduction`。

### 8. `advice` — 5 行 / 1 篇
P-D-2020-2015044-db9655c7，26509–26513，页 18。章 "5 Advice for Huskies"，子节 "5.1 Conditioned on Coaches"；5 个 block 的 `job` 为 read-figure/interpret（"We plot the distribution of performance indicators conditioned on different coaches in Figure 11."、"For coach 2: we can see coach 2 is not as good as the other coaches…"）。
→ `results`：编码内容是指标分析，不含建议条；若同章后页有真正的建议 block（本 5 行之外），那些 block 需单独看，本表只覆盖这 5 行。

### 9. `future-considerations` — 5 行 / 1 篇
P-D-2020-2022868-71331b90，26614–26618，页 20–21；引文 "With more time, we could create networks using a partitioning of the field where each region is a node."。→ 走既有别名 `future-improvements`（→`strengths-limitations`），不新增名。

### 10. `illustration` — 4 行 / 1 篇
P-D-2018-82794-47f05792，25271–25274，页 5；引文 "Two types of charging stations Tesla currently offers two types of charging stations: (1) destination charging and (2) supercharging."、"A charging station contains only one charger Because our model calculates the number of chargers needed…"。→ `introduction`（1.3，与已裁定的 `problem-restatement` 同章同位）。

### 11. `heavy-trucks` — 1 行 / 1 篇
P-D-2018-82794-47f05792，25408，页 23；引文 "Heavy trucks generally need to travel a long way, as well as their huge traction, which result in that their demand for supercharging stations is greater than that of personalvehicles and they are not suitable for charging in cities."。→ `results`（分析正文内的专类评述）。该标签仅 1 行，用户若倾向 丢弃 也不影响其他论文。

## 合计核对

- 未裁定标签行：399 + 135 + 24 + 9 + 8 + 7 + 7 + 5 + 5 + 4 + 1 = **604**
- 另 `blocked==["job-outside-vocabulary"]` 行：**2**（1161、1162，见 `blocked-jobs.md`）
- 604 + 2 = **606**，等于 `rows.jsonl` 中 `status=="blocked"` 的行数；无遗漏、无重复
- 每条建议均可回溯：标签→论文→行段在本文件列全，行段内的每一行都带 `source_quote_file`+`source_quote_row` 可回查引文
