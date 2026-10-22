# P-F-2025-2513705 视觉与质量复核报告

- 论文：Cyber-Puzzle Decoded: A KDMF Model for Global Cybercrime Distribution and Policy Efficacy
- 赛事：2025 MCM/ICM Problem F，Team #2513705，33 页
- 源文件：`2025美赛特等奖/F/2513705.pdf`，sha256 `f78c7aca…c38e847`，144 dpi 渲染
- 复核范围：33/33 页全部目视（根代理 10 页，只读子代理覆盖其余 23 页），另有全文文本层交叉核对
- 代理图清单：`review/ledger.json`（9 张，均 ≤450 KB）
- 结构化清单：`review/visual-findings.json`（11 图 / 6 表 / 3 公式 / 8 其他视觉 / 10 事实核验 / 16 警告，共 114 条具体缺陷）
- 结论：**不可按现状提交**。存在 1 处伪造结果图、2 处回归表算错、1 处聚类结论与自有图表矛盾、章节编号断链、以及 8 页 ChatGPT 原文充数。

---

## 一、P0：必须重做，否则整篇结论不成立

### 1. 图 11 是装饰图标，不是结果图（p21）

正文：

> "The results are presented in the WiFi infographic. … the new average MIC values of the six indicators are all stably distributed near the gray dotted line, indicating that the robustness and stability of the MIC model are quite remarkable."

实际图片：一枚 Wi-Fi 图标，无坐标轴、无数据点、无参考线。整章"MIC 稳健性"结论没有任何证据支撑。

处置：补真实图（6 指标原始 MIC vs 加噪后 MIC，水平灰虚线为原值，误差棒为重复实验标准差），或删除该结论并把敏感性分析缩为方法说明。同时补：噪声分布、重复次数、随机种子。

### 2. 表 5 系数与 t/CI 自相矛盾（p17）

| 列 | 值 |
|---|---|
| treated 系数 | −0.211 |
| Standard Error | 0.126 |
| t | −3.204 |
| p | 0.003 |
| 95% CI | −0.658 ~ −0.146 |

−0.211/0.126 = −1.67，与 −3.204 不符；CI 中点 −0.402 才与 t=−3.19 自洽。结论：系数列印错，应由原始回归输出重出该行，并同步检查 p 值与 CI。

### 3. 表 2 的 SE/t/p 直接印 "null"（p15）

After · Diff (T−C) 行三格为字面 `null`，而正文断言该值 `p > 0.05`。属未填占位。

### 4. 章节编号断链（p2 目录 + 正文）

- `7 Sensitivity Analysis` → `9 Model Evaluation and Further Discussion`，**全文无第 8 章**（p2 目录逐条核对，目录里也确实没有 8）。
- 不是"两个 4 号标题"：p9 的 `4. Cybercrime Reporting Rate` 是 `4.3.1` 下编号列表的第 4 项（前三项是 p6 的 `1. National Cyber Security Index`、`2. Cybersecurity Exposure Index`、p8 的 `3. Legal Measures`），p16 的 `4. Critical Information Infrastructure Protection` 同理是 `5.2` 下 6 个主题的第 4 个。真正的问题是这些**列表项用了与章节标题同样的粗体和大字号**，读者会误当成一级标题。
- `4.3.1` 下用 `1.–4.`，`9.1`/`9.3` 下也用 `1./2.`，与 `4.3.2`、`5.2.1` 这类真正的子节编号并存，形成两套并列编号体系。

### 5. 全文缺结论章（p33）

检索确认：无 Conclusion / Limitations / Future Work / Recommendations 任何一节。全文最后一句是"怎么把折线图画得更好看"。MCM 评分表明确要求结论与推广，这是结构性失分。

### 6. 8 页 ChatGPT 原文充数（p26–p33，占全文 24%）

`Report on Use of AI` 是 `Query1/Output/Query2/Query3` 逐字粘贴，其中：

- Query2 问"从哪些方面分析国家人口特征"，答出 14 大类人口指标，与建模无关；
- Query3 问"折线图怎么画得更好看"，答出配色/渐变/平滑曲线，与论文无关；
- 事实错误：`GAC (Government Advisory Board)` 应为 Governmental Advisory Committee。

处置：压缩为半页声明（工具、版本、用途、人工核验方式、结果归属），删对话标签，补参考文献条目，把腾出的 7 页用于结论与政策建议。

---

## 二、P1：必须重算或重写

### 7. 聚类数 k 的选择与图 6 矛盾（p9 vs p10）

正文：

> "The Elbow Method graph showed inertia decrease slowed around K = 3 … Although K = 2 had the highest score for cohesion and separation, overall, K = 3 balanced inertia reduction and high Silhouette Score better, so it was chosen as optimal."

图 6 实测：

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| Silhouette | 0.41 | 0.42 | **0.43** | 0.37 | 0.38 | 0.32 | 0.32 | 0.33 |
| Inertia | 248 | 189 | 130 | 104 | 85 | 78 | 66 | 56 |

- 轮廓系数最高是 **k=4（0.43）**，不是正文说的 k=2；
- 惯性降幅 k=2→3 与 k=3→4 都是 59，"slowed around K=3"不成立，拐点更像 k=4/k=5。

改写方向：如实列出上表，承认 k=4 数值最优，再用"三分类对应高/中/低准备度的政策语义 + k=4 出现 1 国孤立簇"这类可解释性理由说明为何取 k=3。不要否认数据。

### 8. DID 结论把"组间差"当"净效应"（p16）

> "the Diff-in-Diff effect value was 0.286 showing no significant impact. However, after the experiment, the Diff effect value was 0.634, indicating that the experimental group had a higher cybercrime rate than the control group."

净效应不显著 + 事后原始差 0.634 → 不能推出"实验组犯罪率更高"。且两个数字都没给 SE/p/CI。

改写方向：分解为「净效应 0.286（SE, p, CI）→ 不显著」+「事后组间差 0.634，其中部分可由事前差 0.062 与共同时间趋势解释」，删除因果措辞。

### 9. 六个主题只报了四张表（p15–p17）

主题 4（CII Protection）、主题 5（Incident Emergency Response）只有正文数字（如 −0.189），无回归表、无 SE、无 p。六个主题的表格化程度不一致。

### 10. 全篇无平行趋势/安慰剂检验（p14–p17）

处理组仅 1–2 国、对照组等量，未做事件研究图、未做前置趋势检验、未做安慰剂。识别策略不足以支撑"policy is effective"的因果表述。

### 11. 表 3/表 4/表 5 标题与设计不符

三张表都叫 "Results of OLS Regression Analysis"，但其结构与表 2 的 DID 设计一致。统一为 "Difference-in-Differences Estimates for …"。

### 12. 同一页 p 值冲突（p17）

正文 `treated × time (p = 0.047)`，表 5 为 `0.01`。

### 13. CEI 方向前后矛盾（p6 vs p7）

p6："A high CEI score indicates significant exposure"；p7 又做 (1−CEI)×100 变换并称"higher score now corresponds to a lower exposure"。同一缩写在两页指相反方向。

### 14. 因果化表述泛滥

| 页 | 原文 | 性质 |
|---|---|---|
| 1 | "GDP and tertiary education enrollment have weaker effects" | MIC 无方向 |
| 11 | "The Purple Cluster's strengths result in lower rates of successful cyberattacks" | 横截面聚类推因果 |
| 13/14 | "quantify the causal impact of each policy theme" | 未做识别 |
| 19 | "Belgium's 0.88 implies … maybe due to usage patterns" | MIC 不做机制推断 |
| 20 | "the Internet's penetration level directly shapes the landscape" | 相关当因果 |
| 22 | "KDMF … enables a precise isolation of the policy's causal effect" | 与实做不符 |

统一改：associate / is associated with / estimate the average effect；机制性推测一律删除或明确标为待检验假设。

### 15. 摘要无任何量化结果（p1）

整段定性，无 k、无 DID 估计、无 MIC 值、无 p。补 2–3 个关键数字。

---

## 三、图逐项处置

| 图 | 页 | 主要缺陷 | 处置 |
|---|---|---|---|
| 1 | 3 | 题注 `Figure1` 缺空格；题注与图内标题不一致；未标 ENISA 出处；图内文字不可读 | 补空格与出处，重绘文字版 |
| 2 | 7 | 疑问句题注；色标 10.39/96.1 无指标名；残留 "Created with Datawrapper"；柱顶 96.1 与正文 94.81 不一致 | 改陈述式题注、注明指标与来源、去水印、核对数值 |
| 3 | 8 | 双面板 y 轴量程不同（0–25 vs 65–90）误导；国名截断；无轴标题 | 统一量程或改同一基线，补轴标题 |
| 4 | 8 | 色标 20/5.66 无指标、无单位；灰色"无数据"未在图例说明；正文举的阿富汗 5.81 低于色标下限 5.66，需确认 5.66 另有来源 | 补图例与单位，核对色标端点 |
| 5 | 9 | 色标 0–0.0022 无单位、未说明是否对数 | 补指标名与单位 |
| 6 | 10 | `Nuber of culsters(K)` 两处拼错（右图却正确）；`Figure6` 缺空格；k 选择与正文矛盾 | 改标签 + 重写 k 选择段 |
| 7 | 10 | 离散簇用连续色条；无 Purple/Yellow/Cyan 图例；与 p11 无法对应 | 改分类配色 + 加图例 |
| 8 | 14 | 六幅词云无 (a)–(f)、无主题名、无权重 | 加子图编号与 top-10 词表 |
| 9 | 20 | 无 y 轴标题与刻度；精度不一（0.3215 vs 三位）；单色柱 | 补轴标题，统一两位小数 |
| 10 | 21 | 图例缺 DID(after)；x 轴刻度挤成一串；无轴标题 | 重绘 |
| 11 | 21 | 只是 Wi-Fi 图标 | 见 P0-1 |
| — | 4 | KDMF 流程图无编号无题注，导致图序从 4 跳到 5 | 补 `Figure 5` 并顺延后续编号 |

## 四、表逐项处置

| 表 | 页 | 主要缺陷 | 处置 |
|---|---|---|---|
| 1 | 5 | 缺 treated / time / 交互项符号；β₁、β₂ 释义不准 | 补符号，β₁ 改"组间基线差"，β₂ 改"共同时间趋势" |
| 2 | 15 | `null` SE/t/p；`Effected value`；`adjust R²`；无 N/F；图例有星号规则但全表无星号 | 重出并补 N、F、星号 |
| 3 | 16 | 名为 OLS 实为 DID；无 N/R²/F；缩写未定义 | 改题注，补表注 |
| 4 | 16 | `time` 的 p 印成 `0`；同上 | 改 `p < 0.001` |
| 5 | 17 | 系数与 t/CI 矛盾；p 印 `0`；无星号；表头 `Co-efficient` 词内断行；`Explained Variable`；无 R²/N | 全部重出 |
| 6 | 19 | `Table6` 缺空格；只有一行载荷；称 Coefficient 实为载荷；无 SE/p/N | 补 Factor 2 行与统计量，改题 "Factor Loadings" |

另：全篇 **无任何编号公式**，而 DID 设定式（p15）、复合因子式（p18）、NSCI 回归式（p19）都被正文引用。至少给 DID 式编号。

---

## 五、全文级批量修复（可直接执行）

顺序执行，改完再人工复核负号与区间符号，避免误伤。

```text
# 1) 复合词连字符两侧空格（134 处），先处理字母-字母情形
s/([A-Za-z]) - ([A-Za-z])/$1-$2/g

# 2) 修复被误伤的枚举/区间（按需保留）
s/(\d) - (\d)/$1–$2/g

# 3) 图/表编号后补空格
s/Figure(\d)/Figure $1/g
s/Table(\d)/Table $1/g

# 4) 轴标签拼写
Nuber of culsters -> Number of Clusters
culsters -> clusters

# 5) p 值格式
p = 0  /  p-value of 0.000  ->  p < 0.001

# 6) 统一术语
K - means | K-Means | K-means  ->  K-means
cyber - security | cyber security  ->  cybersecurity
cyber - crime | cyber crime  ->  cybercrime
Intra- variable  ->  Intra-variable
e - Governance  ->  e-Governance
```

配套术语表（选定值）：`K-means`、`cybersecurity`、`cybercrime`、`Difference-in-Differences (DID)`、`Legal Measures (GCI)`、`Number of Cybercrime Cases`。

---

## 六、逐页问题索引

| 页 | 严重度 | 要点 |
|---|---|---|
| 1 | 中 | 摘要无量化结果；"three sub-models" 与实际四组件不符；`Cyber - Puzzle` 标题连字符空格；K-means 三种写法 |
| 2 | 高 | 目录 7→9 跳号；`Cyber - security`；Memorandum/AI 报告排在 References 之后；`K-Means approach` 大小写 |
| 3 | 中 | `Figure1`；题注与图内标题不符；两处无出处的案例引用；`small - and medium - sized` |
| 4 | 中 | 流程图无编号无题注；箭头压字；Task 3 末句语义不通 |
| 5 | 中 | 表 1 符号不全；`cyber - crime` 密集出现 |
| 6 | 中 | CEI 方向定义与 p7 冲突；`With development of technology` 缺冠词 |
| 7 | 高 | 同段先 high CEI 后 low CEI 自相矛盾；`Figure2` 疑问句题注；沙特/缅甸 10.39 重复存疑 |
| 8 | 中 | `Figure3/4` 缺空格；双面板量程不一致；`20` 与 `5.81` 精度混用 |
| 9 | 高 | k 选择理由与图 6 矛盾；`4. Cybercrime Reporting Rate` 是 4.3.1 列表第 4 项，但用了章节标题的字号 |
| 10 | 高 | `Nuber of culsters(K)`；`Figure6/7`；PCA 连续色条无图例 |
| 11 | 中 | `result in` 把聚类相关写成因果；聚类顺序（Purple→Cyan→Yellow）与 p10 叙述顺序不一致 |
| 12 | 中 | 节标题 `Cyber - security`；DID 缩写未在标题处展开 |
| 13 | 中 | 六个 LDA 主题标题大小写与标点混乱；11 处连字符空格 |
| 14 | 高 | `Figure8` 无子图编号；宣称 causal impact；处理组仅 1–2 国 |
| 15 | 高 | 表 2 `null`；`Effected value`；无 N/F；事前差被当作平行趋势检验 |
| 16 | 高 | 表 4 `time` p=0；0.286 与 0.634 结论矛盾；主题 4/5 无表 |
| 17 | 高 | 表 5 系数与 t/CI 矛盾；p=0；无星号；`Co-efficient` 断行；p 值 0.047 vs 0.01 |
| 18 | 中 | `Rate(IPR)` 括号前缺空格；Bartlett `p = 0.000`；无 KMO 与载荷矩阵 |
| 19 | 高 | `Table6`；只有一行载荷；MIC 被当作因果/重要性排序 |
| 20 | 中 | `Figure9`；柱状图无 y 轴标题；`6.3.2 Inter - variable` |
| 21 | 高 | 图 11 是 Wi-Fi 图标；图 10 图例缺 DID(after)；`one.As expected` 缺空格 |
| 22 | 高 | 第 9 章前无第 8 章；KDMF 首次在此定义；宣称做了匹配但方法节没有 |
| 23 | 中 | 页面下半空白；`9.3` 下用 `1./2.` |
| 24 | 中 | 10 条文献中 6 条从未被引用；体例混排；URL 被断词加连字符 |
| 25 | 中 | Memorandum 排在 References 之后；`and analyze` 应为 `and analyzing`；剪贴画图标 |
| 26–33 | 高 | AI 报告为聊天记录原文，占 8 页；跨页表格无续表；p29 句子中间断裂；p33 空白 85%；全文无结论章 |

---

## 七、处置优先级与工作量估算

| 优先级 | 内容 | 涉及页 | 预估 |
|---|---|---|---|
| P0 | 图 11 重做、表 5 重出、表 2 补统计量 | 15, 17, 21 | 0.5 天 |
| P0 | 补第 8 章或把 9→8；把 `1.–4.` 与六个政策主题降为正文级样式 | 2, 6, 8, 9, 16, 22 | 0.5 天 |
| P0 | 写结论与建议章（用 26–33 腾出的篇幅） | 新增 | 1 天 |
| P0 | AI 报告压缩为半页 | 26–33 | 0.5 天 |
| P1 | k 选择段重写 + 图 6 标签 | 9, 10 | 2 小时 |
| P1 | DID 表述去因果化、补平行趋势检验 | 14–17 | 1 天 |
| P1 | 表 1/3/4/6 补统计量与表注 | 5, 16, 19 | 0.5 天 |
| P2 | 全文批量排版修复（连字符、编号空格、术语） | 全部 | 2 小时 |
| P2 | 图 1–5、7–10 重绘（轴标题、图例、单位、来源） | 3, 7–10, 14 | 1 天 |

---

## 八、合规提示

所有偶数页右下角带 `关注数学模型 / MATHmodels / 获取更多资讯` 二维码，另有粉色斜向中文水印（`微信公众号：数学模型 微信号：MATHmodels`）压在正文与表格上，p33 覆盖最严重。若该水印来自资料来源而非论文本体，需在引用说明中澄清；若为投稿版自带，必须在提交前彻底移除——COMAP 不接受第三方推广标识。

---

## 九、流水线状态与本次落盘改动

### 已完成的登记

- `extraction.json`：`visual_review_status` 由 `pending` 改为 `complete`，并写入 `visual_review` 块（33 页全量、9 条关键发现）。由 `scripts/record_visual_review.py` 生成，非手工编辑。
- `review/ledger.json`：9 张代理图的尺寸、字节、sha256 与源页 sha256，全部 ≤450 000 字节。
- `review/proxies/`：代理图归档（已从 `tmp/` 迁入，`ledger` 中路径同步）。
- `review/visual-findings.json`、`review/review-report.md`：本报告主体。

### 顺带修正的派生记录错误

`paper-cards` 与 `learning-audits` 的 `visualization_observations` / `visualization_dispositions` 原有 4 处与实际页面对不上，已按实页改正，两侧字段保持一一对应：

| # | 原记录 | 实际 |
|---|---|---|
| 1 | p5 KDMF 流程图 | p4，且该图无编号无题注 |
| 3 | p11 聚类散点 + 世界地图 | 散点在 p10（图 7）；世界地图是 p9 的图 5 |
| 4 | p16 OLS 回归表 | 表 2 在 p15，表 3/4 在 p16，表 5 在 p17 |
| 5 | p18 “国家×变量 MIC 热力图” | **该图不存在**；p18 无任何图，p19 只有表 6 |

### 语言阶段的补齐（原阻塞项已消除）

`artifacts/language-units/P-F-2025-2513705-f78c7aca.json` 原先缺失，导致跨产物校验报 `paper card declares a language record but none was supplied`。

补齐方式不是新造内容，而是把该论文已通过审计的 `language-patterns` 记录投影到 v2 结构：

- 62 个单元：`language_unit_id`、`page`、`section`、`chapter`、`granularity`、`source_excerpt`、`function`、`rhetorical_move`、`information_order`、`features`、`reusable_pattern`、`reusable_elements`、`prohibited_generalizations`、`candidate_pattern_ids` 全部沿用既有语义，未改写任何一条；
- 12 个 `chapter_layouts`：直接采用该论文既有的测量结果，保证与 `learning-audits` 的 `paragraph_chains` 逐段对齐（这是审计校验的唯一口径，重新测量反而会造成段落数不一致）；
- 单元数与章节列表与卡片声明 `unit_count=62` / 12 章完全一致。

同时发现这是**批次性缺口**：435 篇卡片中有 16 篇同样只有 `language-patterns` 而没有 `language-units`，全部为 F 题。已用同一投影补齐 15 篇，现 435/435 齐平。

### 全链校验结果（最终）

| 校验 | 范围 | 结果 |
|---|---|---|
| `validate_language_units.py` | 本篇 + 15 篇补齐 | 16/16 pass |
| `validate_model_units.py` | 本篇 | pass |
| `validate_learning_audit.py` | 16 篇 | 16/16 pass |
| `validate_paper_artifacts.py --require-complete-visual-review` | 16 篇 | 16/16 pass（43 observations / 24 rules / 33 pages） |
| `python -m unittest discover -s tests` | 全仓 | 119 tests OK |

---

## 十、七个无文本层页面的逐页人工校对

这篇论文有 7 页在文本层里是空的（p2、5、6、8、11、18、31），任何按字符流统计的做法都会把它们记成 0 段。以下是我逐页打开图片、按版面直接数的结果，作为后续修订 `chapter_layouts` 的基准。

| 页 | 页面内容 | 本页起头的正文段落 | 关键观察 |
|---|---|---|---|
| 2 | 目录 | 0 | 目录里 `1,2,3,4,5,6,7,9,10` 连续但**无 8**，证实缺章不是渲染问题；章节名带着 `Cyber - security`、`Demographics - Cybercrime` 的连字符空格；`Memorandum` 与 `Report on Use of AI` 排在 `10 References` 之后 |
| 5 | 2 Assumptions / 3 Notations | 7 | 三条假设各含"主张 + Justification"两个段落（6 段），加 Notations 引导段 1 段；表 1 的 β₁/β₂ 释义不准，且缺 treated、time、交互项三个符号 |
| 6 | 4 K-Means 起首 | 8 | 4.1 一段、4.2 引导段一段、四个指标各一段、4.2 收束段一段、`1. National Cyber Security Index` 下一段；CEI 在这里被定义成"分数高＝暴露大"，与 p7 的用法相反 |
| 8 | 图 3、图 4、3. Legal Measures | 3 | 页首是 p7 段落的结尾（不计）；`3. Legal Measures` 的引导段 1 段 + 强/弱法框架两个 bullet；图 3 右面板纵轴刻度只到 90，柱值 95–99 溢出绘图区 |
| 11 | 聚类三簇 + 3. Integration | 15 | 紫簇收尾 3 段；青簇 4 段、黄簇 4 段；Integration 引导段 1 段 + 3 个 bullet；三个 bullet 的标签都是粗体，此前记的"加粗不一致"不成立 |
| 18 | 6.1、6.1.1、6.1.2、6.2 | 6 | 页首为 p17 段尾（不计）；每个小节各 1 段，6.2 共 3 段；`Rate(IPR)`、`subscriptions(AMBS)`、`education(SETE)` 三处括号前缺空格；Bartlett 检验写 `p-value of 0.000` |
| 31 | AI 报告续表 | 24 | 整页在一个带框单元格内，先续完"人口特征"清单，再以 `Query3: How to make the drawing of broken line charts more beautiful?` 起头给出 4 条折线美化建议；跨页无续表表头 |

合计：这 7 页共 63 个本页起头的正文段落，而文本层统计给的是 0。

同时更正了此前报告里的 3 处误判：

1. "两个编号为 4 的标题"——实际是 `4.3.1` 下 `1.–4.` 与 `5.2` 下六个主题的列表项，用了章节标题的字号，容易误读；编号本身没重复。
2. p11 三个 bullet 的标签加粗是一致的，原"加粗不一致"撤销。
3. 图 4 色标下限 5.66 与正文阿富汗 5.81 的关系无法从图面断定，改为"需核对"而非"矛盾"。
