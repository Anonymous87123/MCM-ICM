# L6-a-evidence — A 车道逐块原文引证

## 目标

为 `lanes/L1-f-structure/merge/snapshot/paragraph-ledger.jsonl` 中每条 A 记录的每个已编码 job 补一句原文引文，逐字可命中。

## 只读输入

| 输入 | 用途 |
|---|---|
| `artifacts/paragraph-ledger.jsonl`（及其冻结快照 `lanes/L1-f-structure/merge/snapshot/paragraph-ledger.jsonl`） | 唯一的分母来源：`type=="A"` 的 chapter 与其 `jobs` 序列 |
| `artifacts/corpus/manifest.jsonl` | 过滤 `problem_type=="A"` 且 `eligible_paper` |
| `artifacts/papers/P-A-*/text/full.txt`、`text/pages/page-NNNN.txt` | 引文来源；命中判定以 `full.txt` 为准 |
| `artifacts/language-units/P-A-*.json` | 只用于定位每个 chapter 覆盖的物理页范围 |

本车道不写 `artifacts/**`、不改 ledger、不碰其他车道目录。

## 输出

| 文件 | 内容 |
|---|---|
| `quotes-a.jsonl` | 每行 `{paper, chapter, block_index, job, quote, page}`；按 `queue.txt` 的 (year, paper) 顺序，chapter 内 `block_index` 严格 0..n-1 |
| `records-a/<paper>.json` | 每篇一份中间件，供 `assemble.py` 校验后拼装 |
| `reports/coverage.json` | 机器校验结果（行数、缺失命中的行、重复下标、缺失页文本、`quotes_sha256`） |
| `queue.txt` | 84 篇 / 3,232 块 的确定性工作队列 |

## 分母

**3,232 块**：当前快照里 84 篇 eligible A 论文、93 条 chapter 记录（84 条 model-establishment + 9 条 results）的 job 总数。
（早期 `merge/report.md` 里的 53 行 / 884 块出自旧的 122 行快照，已作废。）

## 引证规则

1. **逐块一句**：每个 job 对应一句引文，写在 `block_index` 等于该 job 在 ledger `jobs` 中位置的记录上。
2. **逐字**：引文必须能在 `full.txt` 中命中；匹配时**折叠空白**（连续空白/换行视为一个空格）。保留原始词序、连字符与标点。
3. **块边界由人工重建**：ledger 只存 job 名，不含字符偏移或页码。因此块的起点由人工在读 `text/pages/*.txt` 后选定；同一 job 序列内按原文顺序推进，不跨 chapter。
4. **公式主导块**：引该块首句**解释性散文**（如 "In which …"、"We obtain …"、"Thus, … can be calculated by"），不引公式行本身。
5. **双栏排版**：`page-NNNN.txt` 按行切块，单栏一行常是半句。此时允许把**连续若干候选块拼成一句**再引（`emit.py` 的 `a-b` 跨度语法）；拼接只插入空格，折叠空白后仍与 `full.txt` 一致。
6. **续接词剥离**：`quote_for()` 会剥掉引文开头 1–2 字母的虚词（"To"、"In"、"We" 等）与页眉页脚残留，保证引文从实词开始。

## 工具链

```
build_queue.py        # manifest + ledger -> queue.txt（84 篇 / 3,232 块）
chapter_digest.py     # 打印某 chapter 的候选块：cap>0 全长截断，cap=0 清洗句，cap<0 仅散文
show_blocks.py        # 打印指定候选块全文
inventory.py          # 一次列出某 chapter 全部候选块及其从句切分（挑下标用）
emit.py               # 人工挑选下标 -> records-a/<paper>.json
assemble.py           # 校验 job 序列、下标连续性后拼 quotes-a.jsonl
check.py              # 行数 / 命中 / 重复下标 / 页文件，写 reports/coverage.json
```

`emit.py` 的 chapter 规格语法：

```
<chapter>:<token>,<token>,...
token := <idx>#<n>      第 idx 个候选块的第 n 句（clean_sentences 口径）
       | <idx>$<n>      同上，但用更细的从句切分（clause 口径，用于一句拆多 job 的块）
       | <a>-<b>#<n>    把候选块 a..b 拼成一段后取第 n 句
```

`emit.py` 在 picks 数与 ledger job 数不等时直接退出，防止错位写盘。

## 校验

```
python -X utf8 lanes/L6-a-evidence/tools/assemble.py
python -X utf8 lanes/L6-a-evidence/tools/check.py
```

`check.py` 的判据：

- `rows` == Σ len(ledger_jobs)（当前快照 3,232）
- `quote_not_in_fulltxt` 为空（折叠空白后子串命中）
- `duplicate_block_index` 为空
- `page_file_missing` 为空

当前状态：`rows 3232/3232 | miss_text 0 | dup_idx 0 | pages_missing 0 | hit 100.0000%`（84/84 篇）。

## 进度

| 项 | 值 |
|---|---|
| 已完成论文 | 84 / 84 |
| 已写引文 | 3,232 / 3,232 |
| 命中率 | 100% |

`quotes-a.jsonl` 的 `quotes_sha256` = `0ba1edf25a88bcad4c2b206286f97edcf73c3b9758c8d13df5d6c5de39c9a0f3`；连续两次 `assemble.py` 输出字节一致。

已完成：P-A-2010-6749、P-A-2010-7571、P-A-2010-7586、P-A-2010-7920、P-A-2011-11199、P-A-2011-12149、P-A-2011-9159、P-A-2011-9582、P-A-2011-9665、P-A-2012-14297、P-A-2012-14990、P-A-2012-15065、P-A-2012-16831、P-A-2013-20559、P-A-2013-23004、P-A-2014-25142、P-A-2014-26911、P-A-2014-29282、P-A-2014-29911、P-A-2014-30532、P-A-2014-31333、P-A-2015-32150、P-A-2015-32722、P-A-2015-34317、P-A-2015-35532、P-A-2015-40764、P-A-2016-42221、P-A-2016-44398、P-A-2016-44845、P-A-2016-46830、P-A-2016-48649、P-A-2016-54164、P-A-2017-55069、P-A-2017-55280、P-A-2017-65448、P-A-2017-66500、P-A-2018-76082、P-A-2018-76271、P-A-2018-77845、P-A-2018-86103、P-A-2018-88255、P-A-2019-1902727、P-A-2019-1917933、P-A-2019-1919022、P-A-2019-1924781、P-A-2019-1926690、P-A-2020-2001334、P-A-2020-2002354、P-A-2020-2003298、P-A-2020-2003485、P-A-2020-2004833、P-A-2020-2007799、P-A-2020-2017785、P-A-2020-2018167、P-A-2021-2100454、P-A-2021-2101951、P-A-2021-2103782、P-A-2021-2110178、P-A-2021-2120808、P-A-2021-2122025、P-A-2022-2200289、P-A-2022-2207343、P-A-2022-2209466、P-A-2022-2209812、P-A-2022-2210307、P-A-2022-2212245、P-A-2022-2216547、P-A-2023-2300336、P-A-2023-2300661、P-A-2023-2303950、P-A-2023-2309229、P-A-2023-2316994、P-A-2023-2321860、P-A-2023-2322687、P-A-2024-2400996、P-A-2024-2405424、P-A-2024-2407093、P-A-2024-2424371、P-A-2024-2425397、P-A-2025-2500836、P-A-2025-2501567、P-A-2025-2501909、P-A-2025-2504218、P-A-2025-2511565。

## 已知限制

- **块边界不可复原**：ledger 无坐标，`block_index` 表达的是 job 在 chapter 内的序号，而非原文偏移；同一 job 序列的不同重建只要顺序一致即视为合规。
- **图表/表格主导的 chapter**（如 P-A-2011-11199 的 results）只能引表行或图注；这类引文仍是逐字命中，但信息密度低于散文引文。
- **OCR 噪声**：部分两栏论文的页文本把公式上下标渲染成私有区字形，引文若包含这些字形会命中失败，需改引同一块内的散文句。
