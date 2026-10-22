# L3 C lane — paragraph jobs for the 112 type-C papers

Hand-coded, one paper at a time. No batch classification script: `para_extract.py`
only measures line geometry, `record.py` only validates and assembles, `check.py`
only recounts. Every job in `jobs-c.jsonl` was read off the page by a human pass.

## Inputs (read only)

| path | use |
|---|---|
| `artifacts/corpus/manifest.jsonl` | queue: `eligible_paper` and `problem_type == "C"`, ordered by `(year, relative_path, file_name)` → `queue.txt` (112) |
| `artifacts/language-units/P-C-*.json` | `chapter_layouts` (chapter, printed pages, `paragraph_count`, `paragraph_functions`) and `units` |
| `artifacts/papers/P-C-*/text/pages/*.txt` | text layer, used for the page map only |
| `artifacts/papers/P-C-*/rendered/*.png` | rendered page, read through `make_review_proxy.py` when a block boundary is ambiguous |
| `artifacts/paragraph-ledger.jsonl` | frozen at `snapshot/paragraph-ledger.jsonl`, sha256 `dbedcb18e5caa70de123c9061a9e83681e0aa217bf4655e660a8e3c2eb6d6b2a`, 174 rows; the original is never written from this lane |

## Writes (this lane only)

`jobs-c.jsonl`, `notes/<pid>.md`, `layout/<pid>.json`, `records/<pid>.json`,
`reports/`, `snapshot/`, `tools/`, `queue.txt`, this file.

Forbidden: `artifacts/**`, `~/.claude/skills/**`, `tmp/para-taxonomy.md`, other lane
directories, other paper types.

## Methods

1. **Queue.** `queue.txt` is the manifest order above. One paper is finished (record,
   recount, note) before the next is opened.
2. **Measurement.** `python -I lanes/L3-c-ledger/tools/para_extract.py layout <pid>`
   rebuilds paragraph boundaries from PyMuPDF geometry: modal body font size, modal
   left margin voted from lines ≥25 chars at that size, median line spacing, first-line
   indent > 6 pt, page-break continuation (a paragraph continues across a break unless
   the previous line closed a sentence with `.`/`!`/`?`/`:` and the next starts
   uppercase), and any body fragment under 5 words folded into the previous block.
   Nothing about jobs is automatic.
3. **Reading.** `python -I lanes/L3-c-ledger/tools/dump_paper.py <pid>` writes
   `.proxy/<pid>-read.txt` with every measured block (number, kind, pages, word count,
   first 900 and last 200 characters). The paper is read from that file, and any block
   whose boundary or kind is doubtful is re-read from the rendered page through
   `make_review_proxy.py --max-bytes 450000`, one image per call, `detail: "high"`.
4. **Coding.** One job per printed paragraph. A *group* is a list of measured block
   numbers that belong to one printed unit: a heading glued into a body tail, the rows
   of one table, a bullet list that tight leading merged into one block, a display
   equation torn into fragments, a page-break split. Groups always follow the printed
   page, never the measured count.
5. **Chapter labels.** The stored `chapter_layouts` names are kept verbatim so counts
   stay comparable (`abstract`, `introduction`, `problem-analysis`, `notation`,
   `assumptions`, `model-establishment`, `results`, `strengths-limitations`,
   `conclusion`, `future-improvements`, …). No renaming happens in this lane.
6. **Page numbering.** Printed page = file page − offset, stated per paper in the note
   when the offset is not zero. `pages` in a record are file pages, because the layout
   is indexed by file page.

## Job vocabulary

Thirteen jobs, plus `ext:` codes and a `+close:<job>` suffix:

| job | what the paragraph does |
|---|---|
| `route` | states where the paper is going, or points at a figure/table as the plan |
| `define` | fixes a term, a symbol, a decision matrix, a classification rule |
| `source` | brings in outside data, literature, or an established fact |
| `select` | chooses among data, alternatives, models, or parameters |
| `derive` | turns assumptions or theory into a formula, step by step |
| `compute` | substitutes numbers and reports the arithmetic |
| `read-figure` | walks a figure, table, or axis dump |
| `compare` | puts two models, materials, or results side by side |
| `check` | tests or verifies an outcome (sensitivity, robustness, validation) |
| `limit` | states an assumption, a weakness, or a bound |
| `mechanism` | explains why the result holds |
| `interpret` | reads meaning out of a number or a ranking |
| `handoff` | passes the conclusion to an outside actor (policy, future work) |

Out-of-table codes, used only when no job fits: `ext:context` (background that carries
no quantity and no citation) and `ext:claim` (a bare evaluative claim about the paper's
own work). Taxonomy snapshot `tmp/para-taxonomy.md`, sha256
`253751016db7479532976a67ec988f066ed0d5c329e0004837e4c452f5b15822`.

## Verification

`python -I lanes/L3-c-ledger/tools/check.py <pid> [<pid> ...]` reports, per chapter,
`group_count` against the stored `paragraph_count` with a `delta` flag, flags any group
whose `open` or `close` is empty, flags a stored chapter never coded, and re-runs
`para_extract.py` to confirm the layout hash is identical. A delta is allowed only when
the record's note states the cause; the two recurring causes are (a) a table or bullet
list the layout split into row-level blocks, (b) a multi-bullet list the layout merged
into one block.

## Progress

| # | paper | chapters | groups | blocks | status |
|---|---|---|---|---|---|
| 1 | `P-C-2010-6947-c5305f34` | 10 | 48 | 81 | done |
| 2 | `P-C-2010-7812-c2fa13fd` | 7 | 77 | 139 | done, deltas: intro -1, model-est +13, data-prep -1 |
| 3 | `P-C-2010-8048-a080a4e2` | 8 | 54 | 119 | done, delta: model-est +17 |
| 4 | `P-C-2010-8088-e7ab6731` | 8 | 28 | 66 | done, delta: results -1 |
| 5 | `P-C-2011-10607-6ed4fd93` | 8 | 117 | 275 | done, deltas: problem +1, model-est +43, results +22, str-lim +4, future +7 |
| 6 | `P-C-2011-11325-4609137d` | 8 | 79 | 131 | done, deltas: intro +2, problem -2, assum -4, model-est +3, results +15, str-lim -5, future +9 |
| 7 | `P-C-2011-11422-caf513f2` | 8 | 59 | 118 | done, deltas: assum +1, model-est +20, str-lim -2, future -1, concl -2 |
| 8 | `P-C-2011-11893-6a9ea7d9` | 8 | 53 | 214 | done, deltas: problem -4, model-est +11, results +4, future +4, concl -4 |
| 9 | `P-C-2011-8882-54492a1f` | 8 | 93 | 201 | done, deltas: intro +1, problem -3, assum -3, model-est +40, results +19, str-lim -5 (no section), future -10 (no section), concl -3 |
| 10 | `P-C-2011-9089-838e50df` | 8 | 92 | 142 | done, deltas: problem -1, model-est +46, results +10, str-lim -2, future +1 |
| 11 | `P-C-2012-12218-14ded715` | 8 | 64 | 130 | done, deltas: intro -2, model-est +20, results +8, future +1, concl -2 |
| 12 | `P-C-2012-13215-607f0f06` | 8 | 76 | 279 | done, deltas: intro -2, problem -4, model-est +21, results +6, str-lim +7 |
| 13 | `P-C-2012-13855-8ff9127d` | 8 | 75 | 157 | done, deltas: intro +1, model-est +17, results +16, concl -1 |
| 14 | `P-C-2012-14531-6018365f` | 8 | 70 | 165 | done, deltas: intro +1, assum +2, model-est +17, results +9, concl -1 |
| 15 | `P-C-2012-15356-6b8f0a28` | 8 | 73 | 156 | done, deltas: problem +1, model-est +26, results +4, str-lim +3, future +2, concl -1 (no section) |
| 16 | `P-C-2012-16075-4bbf9219` | 8 | 102 | 303 | done, deltas: intro +3, problem -1, model-est +29, results +27, str-lim +1 |
| 17 | `P-C-2012-17160-8b6c54d2` | 8 | 73 | 108 | done, deltas: intro -6 (contents+statement), problem +1, assum -2, model-est +20, results +9, str-lim +1, future +1, concl -1 |
| 18 | `P-C-2013-18492-ab739371` | 8 | 129 | 213 | done, deltas: intro +1, assum -2, model-est +77, results +5, str-lim +1, future -2, concl -2 |
| 19 | `P-C-2013-21165-17e64d15` | 8 | 78 | 155 | done, deltas: intro -2 (contents), problem +1, assum +2, model-est +16, results +19, str-lim +3, concl -1 (no section) |
| 20 | `P-C-2014-25318-eac62e81` | 8 | 99 | 182 | done, deltas: intro -1, problem +2, assum +4, model-est +20, results +32, str-lim +2, future +2, concl -2 (no section) |
| 21 | `P-C-2014-27688-856eb1b7` | 8 | 115 | 169 | done, deltas: intro +3, problem +10, assum +2, model-est +21, results +18, str-lim -1, future +5, concl -1 |
| 22 | `P-C-2014-28199-d39873d7` | 8 | 91 | 154 | done, deltas: model-est +31, results +9, str-lim +7, future +6, concl -1 (no section) |
| 23 | `P-C-2014-28747-f6ef544f` | 8 | 157 | 205 | done, deltas: problem +11, assum +4, model-est +74, results +22, str-lim +5, concl -1 (no section) |
| 24 | `P-C-2014-30221-7af27341` | 8 | 140 | 175 | done, deltas: problem +1, assum +2, model-est +59, results +23, str-lim +10, future +6, concl -2 |
| 25 | `P-C-2014-31262-1f9007fa` | 8 | 135 | 139 | done, deltas: problem -1, model-est +62, results +26, str-lim -1, future +1, concl -3 |
| 26 | `P-C-2015-33572-b32fb4b1` | 8 | 175 | 257 | done, deltas: intro -1, assum +2, model-est +90, results +35, future +4, str-lim +2, concl -1 (no section) |
| 27 | `P-C-2015-33900-7f8065e8` | 8 | 107 | 184 | done, deltas: problem +2, assum +4, model-est +53, results +5, future -1, str-lim +2, concl -1 (no section) |
| 28 | `P-C-2015-35778-39d71af2` | 8 | 138 | 392 | done, deltas: intro -5, problem -1, assum +2, model-est +52, results +31, str-lim +1, future +3, concl -1 |
| 29 | `P-C-2015-37075-1d95d60d` | 8 | 168 | 253 | done, deltas: intro +6, assum +4, problem +19, model-est +31, results +42, future +12, str-lim +3, concl -1 |
| 30 | `P-C-2015-37284-dee063ba` | 8 | 172 | 265 | done, deltas: intro -2, problem +25, model-est +57, results +9, str-lim +2, future +11, concl +6 (no section) |
| 31 | `P-C-2015-39160-2b8963a3` | 8 | 137 | 244 | done, deltas: problem +17, assum +14, model-est +36, results +10, str-lim +2 (no section), future +1, concl -4 |
| 32 | `P-C-2016-42939-5fccbebc` | 8 | 119 | 172 | done, deltas: intro +13 (summary+letter), problem -1, assum +3, model-est +40, results 0 (§5.3), future +4, str-lim +5 (strengths in §1.4), concl +3 |
| 33 | `P-C-2016-47823-59d82231` | 8 | 143 | 226 | done, deltas: intro +12 (summary+letter), problem +5, assum +3, model-est +28, results +7 (§6.2.1-appendix), str-lim +3 (§8.1-8.3), concl -7, future +22 (no section, Appendix 2) |
| 34 | `P-C-2016-50193-615bc62f` | 8 | 143 | 340 | done, deltas: intro +9, problem +15, assum +5, model-est +23, results +22, str-lim +4, concl -1 (letter in concl), future -1 |
| 35 | `P-C-2016-52815-2e6f0093` | 8 | 80 | 86 | done, deltas: intro -8 (summary sheet is image-only page 1, §1 has 3), problem +1, assum +1 (§5 + §6.3), model-est +26, results +3, str-lim +1 (§6.2/6.4/8.3; stored cue is §3.5), concl -3 (letter), future +1 |
| 36 | `P-C-2017-55261-f877d0a0` | 8 | 110 | 260 | done, deltas: intro -3 (summary sheet is one paragraph), problem 0, assum +3 (7 bullets split into line blocks), model-est +38, results +8, str-lim +13, concl +3 (letter), future +4 (no section; lane-change weakness list) |
| 37 | `P-C-2017-55278-a011d0e2` | 8 | 140 | 243 | done, deltas: intro -2 (5 summary paragraphs), problem -1, assum +6 (8 bullets), model-est +37, results +32, str-lim 0 (§5.1-5.2), concl +4 (§6+letter), future +1 (§5.3) |
| 38 | `P-C-2017-55583-34388031` | 8 | 105 | 238 | done, deltas: intro -2 (5 summary paragraphs), problem +4 (§1 statement+3 relations), assum +3 (4 bullets+notation table), model-est +16 (3.1-3.3 params split), results +30 (§4.1-4.3.1 bullets), str-lim +1 (§5.1-5.2), concl 0 (letter 8 + §6), future +1 (§5.3) |
| 39 | `P-C-2017-55585-278f2f68` | 8 | 170 | 316 | done, deltas: intro -6 (6 summary paragraphs), problem +7 (§1 8 + §3.1 2), assum +15 (§2.1-2.4 items), model-est +60 (§3.2-3.3 + whole §4), results +17 (§5-§6), str-lim +5 (§7 + §9.1), future +3 (§9.2), concl +2 (§8 + letter) |
| 40 | `P-C-2018-72969-f2349d15` | 8 | 126 | 189 | done, deltas: intro -6 (4 summary paragraphs), problem +17 (§1 14 + §4-4.1 6), assum +3 (§2 4 assumptions + Table 1), model-est +29 (§4.2-4.4), results +20 (§5 5.1-5.2), str-lim +7 (§6 + §7.1), future +2 (§7.2), concl +3 (§8 + memo) |
| 41 | `P-C-2018-73767-a72d3a8a` | 8 | 109 | 163 | done, deltas: intro -7 (5 summary paragraphs), problem +8 (§1 8 + §3 6), assum +2 (4 assumptions + notation table), model-est +35 (§4 profile + §5.1-5.4), results +12 (§6 + §7 goals/actions), str-lim 0 (§9.1), future +2 (§9.2), concl +2 (§8 3 + memo 8) |
| 42 | `P-C-2018-78577-919f0d0f` | 8 | 147 | 203 | done, deltas: intro -8 (2 summary paragraphs), problem +47 (§1 7 + §2 9 + §3 profile 43), assum +3 (3 assumptions + notation table), model-est +16 (§4 + §5.1), results +26 (§5.2 + §6), str-lim +2 (5 strength bullets), future +1 (2 weaknesses), concl +7 (memo 10) |
| 43 | `P-C-2018-80560-ad2eea75` | 8 | 140 | 217 | done, deltas: intro -7 (5 summary paragraphs), problem +16 (§1 12 + §2 8 + §3 8), assum 0 (5 bullets merged into 1 block), model-est +30 (§4 EROI + §5.1-5.3), results +23 (§5.3 policies + §5.4 + §6), str-lim +3 (5 strengths), future +2 (3 weaknesses), concl +18 (§8 11 + memo 17); file pages 13-14 are a text-layer gap, read from the rendered image |
| 44 | `P-C-2018-82150-43b69981` | 8 | 112 | 170 | done, deltas: intro -4 (4 summary paragraphs), problem +22 (§1 4 + §3 4 + §4.1 6 + §4.2 20), assum +5 (5 assumptions), model-est +1 (§4.3 evaluation), results +17 (§4.4 VAR + §5 compact), str-lim +3 (5 strengths), future +2 (3 weaknesses), concl +18 (§7 5 + memo 15) |
| 45 | `P-C-2019-1900577-7ac4ae90` | 8 | 129 | 196 | done, deltas: intro -5 (7 summary paragraphs), problem +19 (§1 16 + §2 7), assum +6 (Table 1 rows + 5 assumptions), model-est +33 (§5.1-5.7), results +7 (§6 3 parts + §7 sensitivity), str-lim +4 (5 strengths), future +3 (5 weaknesses), concl +6 (§8 3 + memo 14) |
| 46 | `P-C-2019-1901213-f6750caa` | 8 | 137 | 221 | done, deltas: intro -7 (5 summary units), problem +10 (§1 13 + §2 2 + §3 4), assum -1 (4.4 heading split over two blocks), model-est +14 (§5.0-5.4), results +33 (§6 36 + §7 9), str-lim +4 (5 strengths + 6 weaknesses), future 0 (3.2 future-work paragraph), concl +9 (§9 5 + §10 6 + letter 10) |
| 47 | `P-C-2019-1901679-1f246132` | 8 | 189 | 267 | done, deltas: intro -6 (6 summary units), problem +17 (§1 2 + §2 18 + §3.3 2 + §3.4 data 9, incl. 4 category runs), assum 0 (§3.1 terminology + §3.2 six assumptions), model-est +39 (§4 Part I mechanics/error/testing + §5 socioeconomic + origin), results +33 (§6 fitting/results/impacts/sensitivity/forecast), str-lim +1 (§8 four overall + five model-specific), future +7 (§9.1 eleven bullet runs), concl +11 (§7 strategies 11 + §9 2 + memo 10) |
| 48 | `P-C-2019-1906204-4e0a421c` | 8 | 147 | 236 | done, deltas: intro -2 (summary sheet printed twice, second copy identical), problem 0 (§1 three paragraphs), assum +2 (three bullets split across line blocks), model-est +66 (§2.1 K-means + §3.1 similarity + §3.2 origin walk + §3.3 SVM + §3.4-3.5 SVR + §3.7 Apriori/correlation/PCA), results 0 (§3.6 maps + §4.3.2-4.3.3 verification), str-lim +2 (weakness list), future 0 (last weakness run = more factors), concl +31 (§4 strategy 22 + memo 18) |
| 49 | `P-C-2019-1922154-b7129095` | 8 | 173 | 229 | done, deltas: intro -6 (summary sheet six units), problem 0 (§1 three paragraphs + 3 asks + 5 planned steps), assum +2 (four assumption/reason pairs split by layout), model-est +57 (§2.1-2.2 terms/symbols + §3.1 preprocess + §3.2 CA rules + §4.1-4.3 factor selection), results +38 (§3.3 spread/CI/threshold + §3.4 RMSE + §4.4 modified results + §4.5 evaluation), str-lim +5 (5 strengths + 2 weaknesses), future 0 (coverage gap run), concl +22 (memo 16 + §4.6 strategy 7 + §6 1) |
| 50 | `P-C-2020-2002116-f6f4a15a` | 8 | 150 | 268 | done, deltas: intro -5 (6 summary units), problem -7 (§1 five paragraphs), assum +3 (5 numbered assumptions), model-est +51 (§2.2 notations + §3 CE-VADER + §4 reputation + §5 AR/fuzzy + §6.2.1 Bayes), results +28 (§3.4 + §4.2 + §5.3 + §6 + §7), str-lim +4 (4 strengths + 2 weaknesses), future -1 (marketing-factor omission), concl +13 (§8 strategies 10 + §10 4 + letter 8) |
| 51 | `P-C-2020-2003717-4c901da6` | 8 | 198 | 326 | done, deltas: intro -3 (9 summary units), problem +43 (§1 background + 2 asks + workflow + §2 cleaning/LDA/2.3), assum 0 (sales-proportionality assumption only), model-est +43 (§3 metrics + §4 reputation + §4.2 windows + §5.1 LSTM), results +40 (§5.2 forecast + §6 ripple/Granger + §7 affective words), str-lim +7 (4 strengths + 2 weaknesses), future 0 (sales-volume assumption), concl +7 (§9 2 + letter 14) |
| 52 | `P-C-2020-2004647-771d613e` | 8 | 192 | 288 | done, deltas: intro -3 (7 summary units), problem +13 (§1 background + 5 asks + related work + framework, assum lead only in stored), assum +2 (5 assumptions), model-est +83 (§3 RRBS vectors + §4 reputation/Kendall + §5 GPR prediction), results +29 (§6.1 incitement + §6.2 wording + §6.3 strategies/features + §7 sensitivity), str-lim +3 (4 strengths), future +1 (2 weaknesses), concl +12 (§9 1 + letter 23) |
| 53 | `P-C-2020-2007707-fbb79044` | 8 | 2 | 2 | done, vector-outline exception: the PDF has no text layer after p. 1 (0 images, 2367 drawings per page, 2 words per page in pages.jsonl), so `para_extract.py layout` returns 3 blocks for 33 pages and deltas are structural, not sampling; all 33 pages read through review proxies. deltas: intro -1 (summary sheet splits into two column blocks 2 and 3, header block 1 excluded; printed §1 on p. 3 is raster), problem -1 (§1 two-ask sentence p. 3), assum -1 (§2 three assumptions + §3 Table 1 lead p. 4), model-est -12 (§4 cleaning/4.2 series/4.2.3 asymmetry/4.2.4 indicators + §5.1 TF-IDF/BP + §5.2 ACF-PACF/difference system + §5.3 PCA success index pp. 5-19), results -1 (§6 sensitivity, 5%/10% text and coefficient stability), str-lim -1 (§7.1 3 strengths + §7.2 2 weaknesses), future -1 (§8 items 1-3), concl -5 (§8 restatement + §9 letter pp. 21-24) |
| 54 | `P-C-2020-2009116-325ae826` | 8 | 148 | 148 | done, deltas: intro +12 (summary sheet 6 + §1 record/asks 8), problem +1 (lexicon decision + three asks), assum +2 (symbol table + 1.5 heading + assumption run), model-est +56 (§2 task-1 preprocessing/descriptives/sentiment + §3 ARIMA + §3.2.1 PCA-built CR + §3.2.2 CS/COM_S + brand ranking), results +38 (§4.2.1 curves + §4.2.2 forecasts + J-T/Wilcoxon + K-means + extreme words), str-lim +3 (§5.1 limitations + §5.2 three strengths), future -1 (no future-work section; PCA concession inside §5.1), concl +7 (letter floated to p. 2, 8 blocks + §6 1) |
| 55 | `P-C-2020-2010638-c32c8549` | 8 | 171 | 197 | done, deltas: intro +9 (summary 1 + §1 3 + two tasks + 6 work bullets), problem +10 (§3.1 seven preprocessing steps + Figure 2), assum +7 (4 assumptions + nomenclature table), model-est +64 (§3.2 NLTK + §3.3 descriptives + §3.4 Pearson + §3.5 multinomial logit + §4 LDA/AHP/Q-cluster), results +39 (§5 AR(1) + decomposition/forecast + §6.1 distributed lag + §6.2 Almon + §7 sensitivity), str-lim +4 (3 strengths + 3 weaknesses), future -1 (no future-work section; holiday/long-term concession inside §8.2), concl +3 (letter 5 units + brand scores + sign-off) |
| 56 | `P-C-2021-2101166-038bd4c8` | 8 | 211 | 217 | done, deltas: intro +19 (9 summary units + 3 background + 6 asks + 3 approach), problem +3 (SMOTE placement + problems 3-5 approach), assumptions +6 (4 data items + 3 behaviour items), model-est +113 (problem 1 difference equation, problem 2 auto-encoder/CNN, problem 3 clustering), results +24 (problem 4 numerical derivative + problem 5 Bayes assessment), str-lim +5 (4 strengths + 2 weaknesses), future +2 (Figure 16 sensitivity), concl +10 (closing 2 + infographic 12); layout sha256 identical 270e403b |
| 57 | `P-C-2021-2101587-8b253851` | 8 | 164 | 214 | done, deltas: intro +11 (5 summary + keywords + 4 background + task bullets), problem 0 (one stored cue printed once), assumptions +3 (4 labelled items), model-est +54 (symbol table, nest locating with AHP, spread model, CNN training), results +40 (confusion matrix, three distance regimes, 1400-photo test, Solow-Roberts victory), str-lim +7 (6 strengths + 4 weaknesses), future +4 (3 update items), concl +10 (memo letter 14 units); layout sha256 identical 7ef1fbae |
| 58 | `P-C-2021-2107815-45f0e8ba` | 8 | 236 | 293 | done, deltas: intro +16 (7 summary units + keywords + background/restatement/approach bullets), problem +4 (3 defects + 3 countermeasures), assumptions +4 (4 numbered), model-est +103 (notation table, pre-analysis, growth-diffusion Eqs. 4-1 to 4-6, LDA and CNN build, 3-D fusion), results +59 (5.5 verification, 5.6 six priority levels, 6 forgetting-factor update, 7 three-condition eradication), str-lim +4 (4 strengths + 2 weaknesses), future -1 (no future-work section; update rule is results machinery), concl +17 (4 conclusion paras + 2-page memo); layout sha256 identical 08b0e4c6 |
| 59 | `P-C-2021-2107870-8021b684` | 8 | 182 | 288 | done, deltas: intro +18 (9 summary units + keywords + 8 TOC rows + restatement/lit review/three tracks), problem 0 (row-level record, unlabeled majority, four-branch unified score), assumptions +11 (nomenclature table + 4 headed assumptions), model-est +67 (data cleaning 3 passes, K-Means inertia/accuracy, k = 17, CNN + sigmoid + BCE, Fisher wave, unification), results +21 (7.1 spread, 7.2 three sets, 7.3 worked sighting, 7.4 eradication, 8 three-fold CV), str-lim +9 (5 strengths + 4 weaknesses), future +7 (priority table + climate/annual update + 4 items), concl +13 (memo header, two tracks, thresholds, counties, form redesign); layout sha256 identical 34175dc4 |
| 60 | `P-C-2021-2109298-1a718172` | 8 | 185 | 234 | done, deltas: intro +9 (5 summary paras + keywords + 8 TOC rows + restatement + approach), problem 0 (three-factor likelihood, prioritization score), assumptions +5 (lead + 5 numbered), model-est +91 (LDA text, 2925-cell grid, suitability S = -log(P)+B, Gaussian population, Moore transition, parameters, Bayes derivation, VGG-11+SVM, seasonal credibility, alpha = 0.1), results +20 (4.2 five branches, 4.3 suitability and initialization sensitivity), str-lim +7 (4 strengths + 3 weaknesses), future +14 (SIR update + 4 eradication criteria), concl +12 (3 conclusion paras + memo with severity table); layout sha256 identical 5ad9e106 |
| 61 | `P-C-2021-2123823-dddc6e65` | 16 | 167 | 303 | done, deltas: abstract 0 (7 summary units), intro +2 (keywords + 12 TOC rows), restatement 0 (items a-e), problem 0 (11 route cues), assumptions 0 (lead + 4), model-est +8 (factor analysis + K-means/GMM + tf-idf + note scoring + combined exponent + regularized logistic + longitudinal), data-prep 0 (14 prep moves), notation 0 (9 symbol groups), results +10 (variance 87.9%, spread peaks, CV, ROC, word clouds, G1 means, 0.94 and 0.96 AUC, 0.99 accuracy, report counts, eradication curves), algorithm +1 (18 procedures), robustness 0 (3 checks), improvement 0 (5 moves), sensitivity 0 (beta and lambda), strengths 0 (3), limitations 0 (2), memo 0 (11); layout sha256 identical d98e96cd |
| 62 | `P-C-2022-2200401-824b71b2` | 15 | 73 | 214 | done, deltas: abstract 0 (5 summary units), intro +3 (keywords + 4 TOC rows + epigraph), restatement 0 (task list), assumptions 0 (3 assumption-reason pairs), notation 0 (3 symbol tables), model-est +3 (vanilla grid, toy arbitrage, ISO/Pro constraints, 0.731 vs 0.595, grid-shift formula), improvement +1 (baseline failure, MA, ARIMA settings), algorithm +13 (Algorithm 1 eleven steps + nine-step backtest with discrete parameter grids), results +11 (ARIMA (6,9,1), eight-strategy comparison, 30000 bound artefact, period allocations), sensitivity +1 (transaction-cost sweep, -20% profit at +50% cost), robustness 0 (Gaussian noise 0.01/0.02), str-lim 0 (5 strengths + 4 weaknesses), conclusion 0 (3 modules + evidence), memo +1 (subject line split), appendix 0 (correlation, ideal benchmark); layout sha256 identical d94cc5ac |
| 63 | `P-C-2022-2200688-b6248fa6` | 14 | 106 | 153 | done, deltas: 0,+2,0,+5,0,+3,+1,+5,0,0,0,0,-1,0; layout sha256 identical ea650d53 |
| 64 | `P-C-2022-2203120-59ecfcb7` | 14 | 80 | 272 | done, deltas: 0,+1,0,0,0,0,+1,+13,0,0,0,0,0,0; layout sha256 identical 4a9625a7 |
| 65 | `P-C-2022-2204883-34c13ed1` | 11 | 105 | 297 | done, deltas: -7,+1,+2,0,0,0,+18,+8,+6,+1,-1; layout sha256 identical 314b982c |
| 66 | `P-C-2022-2208834-e1b081c3` | 10 | 97 | 223 | done, deltas: -3,0,+1,+2,+5,+9,0,-1,+1,+1; layout sha256 identical fe123f2f |
| 67 | `P-C-2022-2212336-9ca07c5b` | 12 | 95 | 177 | done, deltas: 0,+1,-4,+1,+1,-2,-3,+2,+1,-1,0,0; layout sha256 identical e2a5f73e |
| 68 | `P-C-2022-2218743-984f9ab2` | 10 | 67 | 194 | done, deltas: 0,+1,0,0,0,0,+1,+1,0,0; layout sha256 identical e05ae546 |
| 69 | `P-C-2022-2218931-a1aa7569` | 11 | 80 | 306 | done, deltas: 0,+1,0,0,0,0,0,0,0,-4,0; layout sha256 identical 91508ae0 |
| 70 | `P-C-2022-2224507-b26b91d5` | 10 | 85 | 353 | done, deltas: 0,0,0,0,0,+1,0,0,0,0; layout sha256 identical aae7ffc8 |
| 71 | `P-C-2022-2229059-dacff43d` | 13 | 50 | 144 | done, deltas: 0,0,0,0,0,0,0,0,0,0,0,0,-1; layout sha256 identical 8f3a4445 |
| 72 | `P-C-2023-2300348-b8cdbed6` | 13 | 107 | 187 | done, deltas: 0,0,-1,0,0,0,0,0,0,0,-5,-2,-1; layout sha256 identical 3c2570a9 |
| 73 | `P-C-2023-2301192-c71d36ff` | 13 | 48 | 235 | done, deltas: 0,0,0,0,0,0,+2,+1,0,0,0,0,0; layout sha256 identical ede791c1 |
| 74 | `P-C-2023-2307166-ec54f9ce` | 10 | 40 | 170 | done, deltas: -1,0,0,0,0,0,+2,0,0,0; layout sha256 identical e55758ac |
| 75 | `P-C-2023-2307946-61b646ed` | 12 | 57 | 242 | done, deltas: 0,0,0,0,0,0,0,0,0,0,0,0; layout sha256 identical d7510a00 |
| 76 | `P-C-2023-2309397-285a4e67` | 15 | 58 | 236 | done, deltas: 0,-1,-2,-2 in introduction, assumptions, data-preprocessing, rest 0; layout sha256 identical e1c414bf |
| 77 | `P-C-2023-2310767-2f955db2` | 11 | 83 | 232 | done, deltas: 0,0,0,0,0,0,+1,-1,0,+1,0 in results (Task 4 has no stored slot), sensitivity (motivation+method and reading+verdict each print as one paragraph), conclusion (extra features paragraph); layout sha256 identical 1461fc46 |
| 78 | `P-C-2023-2311035-1b2bc274` | 11 | 67 | 233 | done, deltas: 0,0,0,0,0,-3,0,+1,0,+1,0 in problem-analysis (5.4 counted twice in stored: coded once in sensitivity), results (Task 4 has no stored slot), conclusion (extra findings paragraph); layout sha256 identical e86d884f |
















