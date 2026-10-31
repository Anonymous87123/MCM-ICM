# Blocked work: where manual paragraph jobs are still missing

Snapshot as in `report.md`: frozen ledger copy
`merge/snapshot/paragraph-ledger.jsonl` (180 rows, sha256 `c6194c0b…97b83a1`);
`jobs-f.jsonl` (672 records, sha256 `f28f3d88…830227`). Recompute with

```bash
python -I -X utf8 lanes/L1-f-structure/tools/freeze_ledger.py   # refresh the snapshot
python -I -X utf8 lanes/L1-f-structure/tools/audit_merge.py      # then measure
```

per-paper rows are in `blocked-papers.csv` (407 rows: 264 papers with no manual row
at all, 143 papers partially coded). The live ledger is appended by another session
while this audit runs, so the row count above is the exact population these numbers
describe; re-freeze and re-run before quoting them.

## Papers without manual jobs

| type | eligible papers | papers with ≥1 manual chapter row | papers with none | in-scope chapter gaps on coded papers |
|---|---|---|---|---|
| A | 84 | 84 | 0 | 858 |
| B | 76 | 24 | 52 | 258 |
| C | 112 | 5 | 107 | 48 |
| D | 55 | 5 | 50 | 26 |
| E | 60 | 5 | 55 | 31 |
| F | 48 | 48 | 0 | 26 |

A–E manual coverage is 123 papers of 387 eligible (31.8%). The 132 A–E ledger rows
are 93 A rows (84 model-establishment, 9 results) plus 39 B–E rows (B 24, C 5, D 5,
E 5), all model-establishment. So 264 of 387 A–E papers have no manual paragraph job
at all; of the 123 that do, all but nine are coded on the model chapter only.

## Which chapters are missing

Counts are stored labels from `artifacts/language-units/*/chapter_layouts`, mapped
through the merge table only for comparison (`problem-restatement`,
`problem-analysis`, `literature-review` → introduction; `sensitivity-robustness` →
sensitivity-analysis; `model-improvement`, `algorithm`, `metrics` →
model-establishment; `robustness-verification` → model-testing). Full per-label
counts: `metrics.json` → `blockage`.

| type | largest gaps (papers missing that chapter) |
|---|---|
| A | introduction 84, assumptions 81, results 75, conclusion 71, sensitivity-analysis 71 |
| B | introduction 76, assumptions 73, results 70, memo 68, notation 64 |
| C | introduction 112, results 112, assumptions 109, model-establishment 107, strengths-limitations 97 |
| D | results 55, introduction 54, strengths-limitations 54, model-establishment 50, assumptions 49 |
| E | results 60, introduction 59, model-establishment 55, assumptions 54, notation 39 |

The stored corpus uses labels outside the fourteen-value vocabulary that coding
would have to normalise first: `title` (A 8, B 25), `limitations` (A 10, B 10, C 12,
E 21), `strengths` (A 7, B 8, C 9, E 21), `error-analysis` (A 5, B 4, C 4, D 2,
E 1). These are not paragraphs in the job sense and need a scope decision before
they are counted as gaps.

## F residuals (48/48 papers coded, 26 buckets unmatched — all 26 now decided)

F has no uncoded paper, but 20 F papers carry 26 stored buckets with no matching
coded chapter: memo 15, sensitivity-analysis 4, data-preprocessing 2, results 2,
conclusion 1, notation 1, robustness-verification 1. Full list in
`blocked-papers.csv` (type F), whose `bucket_class` column now carries the
reconciliation verdict; the evidence is in `reconcile/bucket-decisions.jsonl` and
`reconcile/README.md`. Every bucket is one of:

- **a, covered by another record — 7 buckets.** Stored bucketing is coarser than
  the printed sections, and a coded record covers the span under a different
  label: `results` in `P-F-2016-43181-88427331` (`Result 2:` / `Result 3:` runs)
  and `P-F-2016-44348-d3da2a69`, `conclusion` in `P-F-2016-43181-88427331`
  (strengths/weaknesses list), `sensitivity-analysis` in
  `P-F-2019-1916704-dd8d036e` (6.5 plus Figure 6), `notation` in
  `P-F-2022-2218577-d61b87f7` (2.2 Notations table), `data-preprocessing` in
  `P-F-2022-2224021-25b6c5d5` (normalization inside 4.3), and
  `robustness-verification` in `P-F-2025-2517199-1033f2d4` (verification
  paragraphs plus 5 Model Evaluation). No text is uncoded.
- **c, no such printed section — 19 buckets.** 15 memo, 3 sensitivity-analysis
  (`P-F-2020-2013233-f7fd24e3`, `P-F-2020-2013733-073f48f7`,
  `P-F-2020-2013772-594465e5`) and 1 data-preprocessing
  (`P-F-2016-43181-88427331` pp.4-6). The text layers never use the function's
  vocabulary — no memo marker in 15 papers, no `sensitiv` in 3, no preprocessing
  word in 1 — and the stored span holds prose, figures or a policy chapter
  already coded under another label. The page-level reads are in
  `reconcile/proxies/`.
- **b, printed and uncoded — 0 buckets.** No stored F bucket hides uncoded text.
  Every measured block in all 26 spans is already in a record (`uncovered = []`
  for all 26).

The hand read also repaired three coding defects inside F records (two uncoded
heading blocks glued to the paragraph they head, one bare `5.2.1` heading
restored after the watermark filter dropped it); `jobs-f.jsonl` was rebuilt and
is deterministic under `tools/record.py`. Details in `reconcile/README.md`.

## Blockers to promotion, independent of the share test

1. **Sample size.** C, D and E have 5 read papers each and B has 24. 60% of 5 is
   three papers, so a C–E rule would rest on three; the usable samples (A 84
   model-establishment papers, B 24, F 48) disagree at position 0.
2. **No verbatim sentences.** 0 of 132 A–E ledger rows contain a quoted sentence;
   only F records carry `units[].open` / `units[].close` (672 records, 6794 units).
   The promotion rule requires one verbatim sentence per claim, so A–E rules cannot
   be promoted until those papers are read in full and quoted.
3. **Label vocabulary.** A–E rows carry raw corpus labels, F rows the normalised
   fourteen. A cross-type sequence claim must fix one vocabulary first; this audit
   deliberately does not rewrite the A–E rows.

## Reproduction

```bash
python -I -X utf8 lanes/L1-f-structure/tools/freeze_ledger.py
python -I -X utf8 lanes/L1-f-structure/tools/audit_merge.py
```

refreezes the snapshot, then writes `blocked-papers.csv` and `metrics.json`.
Counts above are read from `metrics.json` → `coverage`, `blockage`; `blocked-papers.csv`
lists every paper with its missing labels and its state (`no manual row` / `partial`).
