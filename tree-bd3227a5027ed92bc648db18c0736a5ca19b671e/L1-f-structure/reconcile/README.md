# Bucket reconciliation for the 26 unmatched F buckets

Twenty F papers carry 26 stored chapter buckets
(`artifacts/language-units/P-F-*.json` → `chapter_layouts`) that no coded record
answers to under the merge label map. `merge/blocked-papers.csv` lists them as
`chapters_missing`. This directory decides every one of them, with evidence, and
re-checks that no measured block of any F paper is left uncoded.

Nothing here writes `artifacts/**`, the A–E records, or `~/.claude/skills/**`.
Inputs are read-only: `jobs-f.jsonl`, `layout/<pid>.json`,
`artifacts/language-units/P-F-*.json`, and the rendered pages
`artifacts/papers/P-F-*/rendered/page-*.png` through the review proxies in
`proxies/`.

## Class definitions

A bucket is one of three things, and the decision file says which:

- **a — covered by another chapter record.** The printed text does the bucket's
  function, and a coded record covers it under a differently normalised label
  (e.g. the paper prints `Result 2:` runs where the corpus says `results`, and
  the lane codes them as `model-establishment`). The decision names the exact
  record ids and quotes the printed sentence.
- **b — printed and uncoded.** The section exists in print and no record holds
  it. This class requires a new record in `records/<pid>.json`, a rerun of
  `tools/record.py`, and hand reading of every new group. **Zero buckets are
  class b.**
- **c — no such printed section.** The print has no section performing that
  function; the stored span is prose, a figure page, or a TOC already coded under
  other labels. The evidence is the page-level read plus a text-layer check for
  the function's vocabulary.

## Method

1. Take the 26 buckets from `reconcile/worklist.json` (paper, stored label,
   stored page span, stored count, stored words), which was generated from
   `blocked-papers.csv` and the `chapter_layouts`.
2. For each bucket, compute which measured layout blocks fall in the page span
   and which coded record holds each one. All 26 spans have `uncovered = []`:
   every measured block in every bucket is already in some record.
3. Read the bucket's printed pages. One page per bucket, rendered through
   `scripts/make_review_proxy.py` (max 450,000 bytes, `detail: high`), storing
   19 proxies here because two buckets share a page and one paper has two
   memo-adjacent buckets.
4. Grep the full text layer for the bucket's own function words (memo markers,
   `sensitiv`, preprocessing words). A class-c decision needs both: the page
   does not print the section, and the paper's text layer never uses the
   function's vocabulary. Where a paper had no text for a region,
   `extraction.json` → `empty_or_near_empty_pages` confirmed the gap was in the
   raster, not in extraction.
5. Record the decision in `bucket-decisions.jsonl` with class, records, span
   block count, printed heading, one verbatim quote with its page, and (for class
   c) the proxy file and what the page actually prints.
6. `check_buckets.py` recomputes everything from the raw inputs and fails if a
   decision is missing, has an unknown class, has record ids that do not equal
   the computed covering set (class a), has any uncovered block, or is class c
   without render evidence.

## Result

| class | buckets | papers |
|---|---|---|
| a — covered elsewhere | 7 | 6 |
| b — printed, uncoded | 0 | 0 |
| c — no such printed section | 19 | 14 |

The seven class-a buckets are the coarse-bucket cases:

| paper | bucket | printed as | records |
|---|---|---|---|
| 2016-43181 | results pp.9-13 | `Result 2:` / `Result 3:` runs | #04, #05, #06 |
| 2016-43181 | conclusion p.18 | `5 Conclusion` (strengths, then weaknesses) | #08, #09 |
| 2016-44348 | results pp.15-17 | 6.3, 7 Scalability, 8 Cobweb policy | #06–#09 |
| 2019-1916704 | sensitivity-analysis pp.9-19 | 6.5 Sensitivity analysis, Figure 6 | #05–#12 |
| 2022-2218577 | notation p.5 | 2.2 Notations table | #02, #03 |
| 2022-2224021 | data-preprocessing pp.8-9 | normalization inside 4.3 Weight of Index | #05, #06, #07 |
| 2025-2517199 | robustness-verification pp.19-22 | verification paragraphs, 5 Model Evaluation | #07–#10 |

The nineteen class-c buckets split into the three shapes the earlier audit
guessed at, now separated by evidence:

- **15 memo buckets, no memo printed.** 2020-2013733, 2020-2013772, 2021-2102185,
  2021-2103649, 2021-2106074, 2021-2109443, 2021-2122374, 2021-2123945,
  2022-2204803, 2022-2208238, 2022-2209952, 2022-2211240, 2022-2218577,
  2022-2220722, 2022-2224021. Zero occurrences of `MEMO`, `Memorandum`, `To:`,
  `From:`, `Subject:` or `Dear` in any of the fifteen text layers; the stored span
  is in each case the paper's impact, policy or evaluation chapter, already coded.
- **3 sensitivity-analysis buckets, no sensitivity printed.** 2020-2013233,
  2020-2013733, 2020-2013772: zero occurrences of `sensitiv` in the text layer.
  The spans are the policy chapter, the model-extension chapter, and chapter 7
  `Testing the model` (consistency ratio, not a sensitivity test).
- **1 data-preprocessing bucket, no preprocessing chapter.** 2016-43181 pp.4-6
  holds 2.1 Parameters only; the text layer has no `preprocess` / `data clean` /
  `data collect`.

So the F residual is not uncoded text. It is 7 coarse stored buckets and 19
stored buckets whose printed section does not exist.

## Record repairs made while checking

The hand read surfaced three coding defects, all inside this lane's own records;
none changes a group count or a job sequence.

1. `P-F-2016-43181-88427331` introduction: block 10 is the printed heading
   `1.1 Background`. It is now glued to the paragraph it heads, group 10-11,
   instead of staying uncoded.
2. `P-F-2021-2106074-d0b37839` introduction: block 14 is the heading
   `1 Introduction 1.1 Background`, glued into group 14-15 the same way.
3. `P-F-2025-2504223-019dfa54` model-establishment: block 54 is the bare `5.2.1`
   heading, which the clean-word filter had dropped as a watermark token. It is
   now group 54-55 with its title. Blocks 70 and 118 in that chapter remain
   uncoded because they hold nothing but the `m m m ...` watermark.

After the repairs `tools/record.py` reruns leave `jobs-f.jsonl` byte-identical
(sha256 `f28f3d88…830227`): 672 records, 48 papers, 6,794 groups, 10,713 blocks,
6,794 units, 7 vacant, 0 empty open/close.

## Coverage after reconciliation

`check_buckets.py` recomputes per-paper block coverage for all 48 F papers:
`dup 0`, `extra 0`, and every uncoded block inside a paper's coded page range
falls in one of the lane's documented scope exclusions — reference 427,
appendix 67, contents 65, front-matter 45, banner 2, **unexplained 0**. Units
equal groups on every paper (6,794 = 6,794).

## Files

| file | what it is |
|---|---|
| `worklist.json` | the 26 buckets, from `blocked-papers.csv` + `chapter_layouts` |
| `bucket-decisions.jsonl` | 26 decisions: class, record ids, span size, printed heading, quote + page, render evidence for class c, reason |
| `bucket-coverage.json` | generated: per-bucket span/covered/record ids, per-paper dup/extra/miss-by-class |
| `proxies/*.jpg` | 19 review proxies, one per read page, ≤450,000 bytes |
| `check_buckets.py` | the verifier; exits 1 on any failure |

## Reproduction

```
cd mcm-skill-work
python -I -X utf8 lanes/L1-f-structure/reconcile/check_buckets.py
python -I -X utf8 lanes/L1-f-structure/tools/record.py <pid>     # after a record edit
python -I -X utf8 lanes/L1-f-structure/tools/audit_merge.py      # regenerates merge/blocked-papers.csv
```

`check_buckets.py` prints `buckets 26 tally {...}` and the per-paper coverage
line, and prints `FAIL ...` plus exit code 1 if any check breaks. A proxy is made
with
`python scripts/make_review_proxy.py --input artifacts/papers/<pid>/rendered/page-00NN.png --output lanes/L1-f-structure/reconcile/proxies/<pid>-p00NN.jpg --max-bytes 450000`.
