# L2 D lane — paragraph jobs for the 55 type-D papers

Hand-coded, one paper at a time. No batch classification script: `para_extract.py`
only measures line geometry, `record.py` only validates and assembles, `check.py`
only recounts. Every job in `jobs-d.jsonl` was read off the page by a human pass.

## Inputs (read only)

| path | use |
|---|---|
| `artifacts/corpus/manifest.jsonl` | queue: `eligible_paper` and `problem_type == "D"`, ordered by `(year, relative_path, file_name)` → `queue.txt` (55) |
| `artifacts/language-units/P-D-*.json` | `chapter_layouts` (chapter, printed pages, `paragraph_count`, `paragraph_functions`) and `units` |
| `artifacts/papers/P-D-*/text/pages/*.txt` | text layer, used for the page map only |
| `artifacts/papers/P-D-*/rendered/*.png` | rendered page, read through `make_review_proxy.py --max-bytes 450000` when a block boundary is ambiguous |
| `artifacts/paragraph-ledger.jsonl` | frozen at `snapshot/paragraph-ledger.jsonl`, sha256 `1122e62ebcf2fc89f52567f881b141ba9b0fd5f1cbba5104d28c7735c87f4ef2`, 190 rows; the original is never written from this lane |

## Writes (this lane only)

`jobs-d.jsonl`, `notes/<pid>.md`, `layout/<pid>.json`, `records/<pid>.json`,
`furniture.json`, `reports/`, `snapshot/`, `tools/`, `queue.txt`, this file.

Forbidden: `artifacts/**`, `~/.claude/skills/**`, `~/.claude/skills/mcm-icm-master-skill/**`,
`tmp/para-taxonomy.md`, other lane directories, other paper types.

## Methods

1. **Queue.** `queue.txt` is the manifest order above. One paper is finished (record,
   recount, note) before the next is opened.
2. **Measurement.** `python -I lanes/L2-d-ledger/tools/para_extract.py layout <pid>`
   rebuilds paragraph boundaries from PyMuPDF geometry: modal body font size, left margin
   voted per page and per column from lines ≥25 chars at that size (falling back to the
   document margin), median line spacing, first-line indent > 6 pt, page-break
   continuation (a paragraph continues across a break unless the previous line closed a
   sentence with `.`/`!`/`?`/`:` and the next starts uppercase), and any body fragment
   under 5 words folded into the previous block. Rows that share a baseline within
   0.45×font size and are adjacent (overlap, or gap < 12 pt) are one visual line, never
   across the page gutter, and the pieces are ordered by baseline bucket then x0, so a
   superscript citation lands after the words it closes instead of in front of them.
   Nothing about jobs is automatic.
3. **Reading.** `python -I lanes/L2-d-ledger/tools/dump_paper.py <pid>` writes
   `.proxy/<pid>-read.txt` with every measured block (number, kind, pages, word count,
   first 380 and last 80 characters). The paper is read from that file, and any block
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
own work).

## Verification

`python -I lanes/L2-d-ledger/tools/check.py <pid> [<pid> ...]` reports, per chapter,
`group_count` against the stored `paragraph_count` with a `delta` flag, flags any group
whose `open` or `close` is empty, flags a stored chapter never coded, and re-runs
`para_extract.py` to confirm the layout hash is identical. A delta is allowed only when
the record's note states the cause. A paper that prints a numbered chapter the stored
layout never captured — P-D-2016-47876-968a1156 prints section 9, Conclusions, between
its strength table and its reference list — is coded under its printed name, and
`check.py` accepts the missing stored count only when the note says the chapter is not in
the stored layout.

`python -I lanes/L2-d-ledger/tools/verify_quotes.py <pid> [<pid> ...]` tests the lane's
promise that every job carries a verbatim original sentence: each unit's `open` must be
a substring of `artifacts/papers/<pid>/text/full.txt` after dropping ligature codepoints,
the running page header (`Team # 35780 Page 16 of 22`, which the text layer splices into
paragraphs that cross a page break) and all whitespace. Word order and punctuation still
have to match, so a block whose span order was scrambled fails instead of passing.

`open` and `close` are read off the group's first and last block only, never off the
joined group text, so a display equation in a later block cannot be spliced into the
opening quote. A table has no prose sentence to open with, and its cells reach the text
layer in column order while the layout measures them in row order; such a unit may name
its opening line explicitly in the record as `"quotes": {"<first block>": "<caption>"}`,
and `verify_quotes.py` checks that caption like any other quote.

A running head that the text layer dropped in without its page number survives the
`PAGE_FURNITURE` pattern; those strings are named per paper under `heads` in
`furniture.json` and removed before folding, so the removal is visible in the lane
instead of hidden in the tool. The pattern takes the `#` of `Team # 55295 Page 5 of 20`
as optional, because some papers print the team number without it. `furniture.json` also
has a `drop_chars` section naming codepoints that carry no prose for one paper and that
PyMuPDF emits in a different order on the page than in `full.txt` — P-D-2016-44173-aa1c9913
maps its comma-space to a caron-plus-letter run, so the two carons are dropped and the
word order decides. P-D-2017-56632-67f41f43 needs two kinds: it prints `.=` where
`full.txt` sets `=.` in its variable definitions, so the equals sign is dropped; and its
text layer loses the ﬀ, ﬃ and ﬄ ligatures outright, leaving `di cult` where the page sets
"difficult", so those three codepoints are dropped on both sides. Dropping runs before
the ﬀ→ff mapping, because otherwise the dropped ligature would have been spelled out
first and the gap in `full.txt` would never line up.

P-D-2017-67316-f37f83c8 hands out every math-italic character twice inside a block
(`\U0001d706\U0001d706` for one lambda), and `full.txt` copies the doubling, so a unit whose
opening clause runs into a formula can never match; such units quote the heading, caption
or prose clause that opens them, listed per paper in the record's `quotes`.

P-D-2018-73156-1a30e830 keeps its mathematics in Symbol-font private-use codepoints
(`` for `=`, `` for `×`, `` for `Σ`) and sets many formulas inline, so the
layout reads the formula first where `full.txt` leaves it after the words; nine units
quote the prose clause that opens them for that reason.

P-D-2018-78826-ed3ee7b7 carries a bookstore advertisement ("精品数模资料，各类比赛优秀论文…") spliced
mid-sentence into many paragraphs in both the measured text and `full.txt`, so a unit whose
opening clause runs into the splice cannot match; three units quote the prose clause, caption
or sub-head that opens them for that reason.

Two C-lane conventions carry over unchanged:

- A stored label outside the thirteen-job vocabulary is kept verbatim in the record
  `note` and mapped to the closest job after the fact; the stored name is never renamed.
- A chapter whose text layer is empty (raster pages) is recorded as a vacated chapter
  with `vacant_units` and `vacant_reason` instead of invented blocks.

## Progress

| # | paper | chapters | groups | deltas | status |
|---|---|---|---|---|---|
| 1 | P-D-2015-34985-c7be0d8b | 11/11 | 35 | abstract −2, problem-restatement −1, introduction −1, assumptions +3, results −1, conclusion −1 | done |
| 2 | P-D-2015-35780-97fea85b | 11/11 | 40 | introduction −2 | done |
| 3 | P-D-2015-38727-eeb1090f | 6/6 | 30 | model-establishment +3, results +1 | done |
| 4 | P-D-2015-38996-1efe10af | 7/7 | 31 | abstract −2, introduction +5, assumptions +3, model-establishment +2, strengths-limitations +1 | done |
| 5 | P-D-2016-42220-7261f9d3 | 7/7 | 25 | abstract +1, introduction +1, model-establishment +1, strengths-limitations +1 | done |
| 6 | P-D-2016-44173-aa1c9913 | 7/7 | 21 | abstract +2, introduction +1, assumptions +1, results −2 | done |
| 7 | P-D-2016-47876-968a1156 | 8/7 | 24 | abstract +2, model-establishment +1, results +2, conclusion not stored | done |
| 8 | P-D-2016-49436-4c3ef010 | 7/7 | 27 | abstract −2, introduction +2, assumptions +2, model-establishment +4, results +4, strengths-limitations +1 | done |
| 9 | P-D-2016-54740-539566f6 | 9/8 | 29 | abstract +1, data-preprocessing +2, model-establishment +4, results +4, conclusion not stored | done |
| 10 | P-D-2017-55285-1835cc0b | 10/9 | 31 | abstract +2, problem-restatement +3, model-establishment +3, results +3, model-improvement +2, sensitivity-analysis +2, references not stored | done |
| 11 | P-D-2017-55295-9001b6d9 | 9/7 | 89 | abstract +3, introduction +1, model-establishment +20, results +14, model-improvement +23, sensitivity-analysis +13, strengths-limitations +2, conclusion and references not stored | done |
| 12 | P-D-2017-56632-67f41f43 | 10/7 | 72 | introduction +1, model-establishment +27, algorithm +3, results +20, model-improvement +4, future-improvements, conclusion and references not stored | done |
| 13 | P-D-2017-67316-f37f83c8 | 13/10 | 100 | abstract −1, introduction +6, assumptions +1, model-establishment +25, results +12, model-improvement +20, sensitivity-analysis +1, memo +8, strengths-limitations +2, cultural-analysis, conclusion and future-improvements not stored | done |
| 14 | P-D-2017-68942-f0b0893e | 12/12 | 99 | abstract vacated (−2, empty text layer), introduction +6, assumptions +19, data-preprocessing +1, notation +13, model-establishment +7, results +9, model-improvement +18, sensitivity-analysis +8, memo +4, strengths-limitations +1 | done |
| 15 | P-D-2018-73156-1a30e830 | 10/10 | 153 | abstract +4, introduction +5, problem-restatement +4, assumptions +3, model-establishment +90, results +18, sensitivity-analysis +3, strengths-limitations +7, memo +3 | done |
| 16 | P-D-2018-78826-ed3ee7b7 | 10/10 | 89 | abstract +5, introduction +2, problem-restatement +5, assumptions +1, model-establishment +22, results +26, model-improvement +7, strengths-limitations +4, memo +3 | done |
