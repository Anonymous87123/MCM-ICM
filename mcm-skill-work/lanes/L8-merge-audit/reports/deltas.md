# Deltas — every counted difference, with a ruling

Machine source: `reports/recount.json` (sha256 `2c7c0082…dda0f4` at the time of
writing). `tools/audit.py` recomputes every number below; nothing here is
hand-maintained arithmetic.

Snapshot caveat: C, D and the live `artifacts/paragraph-ledger.jsonl` are being
written by other sessions while this audit runs. Numbers are a snapshot; re-running
the tool can move the C and D rows and the ledger row count. B and the six lanes'
`layout/`, `notes/` and records for A, B, E, F are stable.

## 1. Three denominators per lane

| lane | papers | chapter records | groups (records) | job rows | group_count sum | quote rows | groups = quotes |
|---|---|---|---|---|---|---|---|
| A | 84 | 93 | 3,232 | n/a | n/a | 3,232 | yes |
| B | 76 | 1,068 | 10,333 | 1,068 | 10,333 | 10,333 | yes |
| C | 112 | 1,112 | 10,404 | 1,112 | 10,404 | 10,404 | yes |
| D | 49 | 527 | 4,646 | 527 | 4,646 | 4,507 | **no, −139** |
| E | 60 | 662 | 5,024 | 662 | 5,024 | none | n/a |
| F | 48 | 672 | 6,794 | 672 | 6,794 | none | n/a |

Records-vs-jobs agrees in every lane that has jobs rows (A has none), and the
`literal_blocks` sums agree with the record block counts to the block. A, B and C
also match the quote layer exactly. One denominator break remains, in D: the paper
`P-D-2024-2417831-f399a6df` was coded after L7 emitted `quotes-d.jsonl`, so it holds
139 groups and zero quote rows (11 chapters). Every other "chapter without quotes"
entry the earlier run showed has disappeared: C caught up completely when its lane
closed, and the remaining zero-group chapters carry no rows either way (see §6).

Ruling: do not synthesize quote rows in the merge lane. D is not merge-ready until
L7 re-emits `quotes-d.jsonl` for the paper coded after its last run; D's author is
the only writer of its records and L7 the only writer of the quote files.

## 2. Job labels outside 13 jobs + 2 extras

| lane | offending labels | count | current value | expected | ruling |
|---|---|---|---|---|---|
| A | `unresolved` | 2 | blocks 29 and 30 of `P-A-2018-76271-27d535ab`, chapter `model-establishment` | one of the 13 jobs or `ext:context` / `ext:claim` | defect in the A record; those two rows must not be merged. L6 must recode them (`derive` is the likely job, the blocks are derivation steps). Excluded from the merge candidate count until fixed. |
| B/C/D/E/F | none | 0 | all labels normalise to the 13 jobs + 2 extras, optionally `+close:<job>` | same | pass, no action |

L7's `labels_outside_vocabulary` blocks in `reports/coverage.json` (B `claim` 290,
`ext:context` 183, `ext:claim` 47, and the `+close:` forms) are not defects: that
field counts raw strings before `ext:` stripping and `+close:` splitting. After
normalisation every one of them is inside the vocabulary. Ruling: the merge reads
`job` verbatim and derives `base_job` and `close_job`; it must not re-derive a new
`claim` job. `claim` → `interpret` remains a vocabulary decision for the merge
session, not for this lane (L7 README, same position).

## 3. Chapter labels outside the fourteen functions

In-vocabulary counts: A 93, B 899, C 866, D 432, E 496, F 626. Out-of-vocabulary
labels, with the ruling that unblocks the merge:

| lane | label | count | ruling |
|---|---|---|---|
| A | — | 0 | none; A uses only `model-establishment` and `results` |
| B | `problem-analysis` | 62 | keep the stored label; `chapter_normalized = introduction` |
| B | `problem-restatement` | 22 | keep; normalise to `introduction` |
| B | `sensitivity-robustness` | 19 | keep; normalise to `sensitivity-analysis` (B README does not rule on this alias; E does) |
| B | `future-improvements` | 13 | keep; normalise to `strengths-limitations` |
| B | `appendix` | 13 | keep; structural chapter, `evidence_class = structural`, never a language row |
| B | `references` | 11 | keep; citation-framing only, `evidence_class = references` |
| B | `limitations` | 9 | keep verbatim per B README; normalise to `strengths-limitations` for aggregation only |
| B | `strengths` | 8 | same as `limitations` |
| B | `title` | 8 | out of scope (front matter); excluded from the row stream |
| B | `error-analysis` | 4 | keep verbatim per B README; normalise to `results` for aggregation |
| C | `problem-analysis` | 73 | same as B |
| C | `future-improvements` | 60 | same as B |
| C | `references` | 40 | same as B |
| C | `appendix` | 22 | same as B |
| C | `problem-restatement` | 21 | same as B |
| C | `limitations` | 12 | same as B |
| C | `strengths` | 9 | same as B |
| C | `sensitivity-robustness` | 5 | same as B |
| C | `error-analysis` | 4 | same as B |
| D | `references` | 49 | same as B |
| D | `problem-restatement` | 13 | same as B |
| D | `future-improvements` | 8 | same as B |
| D | `appendix` | 6 | same as B |
| D | `problem-analysis` | 5 | same as B |
| D | `sensitivity-robustness` | 3 | same as B |
| D | `error-analysis` | 2 | same as B |
| D | `cultural-analysis`, `technology-impact`, `illustration`, `heavy-trucks`, `our-work`, `recommendations`, `advice`, `future-considerations`, `gcn-evidence` | 1 each (9 rows) | **unruled, merge-blocking.** These are D-lane local names never documented in the D README. Proposed mapping for a human decision: `our-work` and `recommendations` → `introduction` / `memo` respectively, `future-considerations` → `future-improvements`, `cultural-analysis` / `technology-impact` / `illustration` → the chapter that carries their printed section, `heavy-trucks` and `gcn-evidence` → `model-establishment`. Do not apply silently; D's author must confirm. |
| E | `references` | 59 | as B |
| E | `problem-restatement` | 27 | as B |
| E | `sensitivity-robustness` | 25 | keep verbatim per E README; normalise to `sensitivity-analysis` |
| E | `limitations` | 20 | keep verbatim per E README |
| E | `strengths` | 20 | keep verbatim per E README |
| E | `appendix` | 11 | structural, as B |
| E | `problem-analysis` | 2 | as B |
| E | `error-analysis` | 1 | keep verbatim per E README |
| E | `future-improvements` | 1 | as B |
| F | `recommendation` | 29 | **unruled, merge-blocking.** F README declares it as a corpus label; it is outside the fourteen. Proposed: keep stored label, normalise to `memo` (policy/stakeholder letter) after human confirmation. |
| F | `model-testing` | 13 | **unruled, merge-blocking.** F README declares it; outside the fourteen. Proposed normalisation to `robustness-verification`, matching F's own merge table. |
| F | `future-improvements` | 4 | as B |

No lane renames anything in this lane's scope. The merge adds two fields
(`chapter` verbatim, `chapter_normalized`) and never overwrites a stored label.

## 4. Records citing blocks absent from the layout

| lane | items | status |
|---|---|---|
| A | n/a | A has no `layout/`; its block ordinals are 0-based per chapter and cannot be checked against a layout |
| B, C, D, E, F | 0 | every coded block index exists as a paragraph `n` in `layout/<pid>.json` |

Pass. No action. The audit prints `blocks_missing_in_layout: []` for all five
layout-bearing lanes.

## 5. Page ranges

- Pages beyond the PDF: none. Every declared page is inside the manifest
  `page_count` for its paper (A 2-40, B 1-59, C 1-31, D 1-37, E 1-37, F 1-26).
- Pages beyond the measured layout end: also none that matter; the earlier
  out-of-range candidates were pages such as 25 in a 25-page PDF where the layout
  simply stops at page 24. Ruling: compare pages to the PDF, not to the layout
  extent; the layout stopping early is an extraction fact, not a record defect.
- Page-span understatement: chapters whose coded blocks sit outside the declared
  `pages`, because the declared span is inherited from
  `artifacts/language-units/<pid>.json` `page_start`/`page_end` while a coded block
  can start one page later after a heading is glued to it (B 21 chapters, C 338,
  D 187, E 38, F 14). Ruling: do not rewrite lane `pages`. The merge row carries
  both `pages_declared` (record) and `pages_coded` (min/max of the group's layout
  block pages). Full per-chapter list in `recount.json` →
  `lanes.<lane>.block_pages_outside_chapter`.

## 6. Empty chapters and duplicate block references

Empty chapters (a coded chapter row with zero groups, so it contributes no
mergeable row):

| lane | count | chapters | ruling |
|---|---|---|---|
| A, B | 0 | — | pass |
| C | 31 | `conclusion` 8, `future-improvements` 5, `notation` 5, `strengths-limitations` 2, `assumptions` 2, `abstract` 2, then one each of `problem-analysis`, `model-establishment`, `results`, `data-preprocessing`, `introduction`, `sensitivity-analysis`, `references` | keep the chapter row in the chapter index, emit no group row; the merge counts rows from groups, so these inflate `chapter_records` but not `rows`. C's author should confirm each is an intentionally empty stored bucket, not an unfinished paper. |
| D | 1 | `abstract` in `P-D-2017-68942-f0b0893e` | same |
| E | 10 | `memo` 8, `strengths-limitations` 1, `references` 1 | same; E README already documents empty stored buckets |
| F | 7 | `memo` 2, `notation` 3, `assumptions` 1, `data-preprocessing` 1 | same |

Duplicate block references (the same layout block coded into two groups or two
chapters of one paper). Each one inflates the group count and would duplicate a
merge row:

| lane | count | items |
|---|---|---|
| A, B, E, F | 0 | pass |
| C | 23 | `P-C-2011-11893-6a9ea7d9` block 22 (assumptions and model-establishment), `P-C-2013-21165-17e64d15` 39, `P-C-2024-2401298-07d37078` 160, 189, 194, 202, `P-C-2024-2401445-6a882749` 74-83 (ten blocks), `P-C-2024-2403774-be4a823f` 24, 48, 64, `P-C-2024-2406176-bd7757f9` 225, `P-C-2024-2409961-92b90752` 60, 179, `P-C-2024-2410482-2f099d31` 100 |
| D | 3 | `P-D-2016-49436-4c3ef010` block 192, `P-D-2017-55285-1835cc0b` 181, `P-D-2021-2101855-c4682962` 209 |

Ruling: these are coding defects in C and D, not merge decisions. The merge must
refuse a paper whose block set repeats, because the duplicate row would carry two
different jobs for one block. C and D are not merge-ready on these papers until
their authors remove the duplicate. Counted in the "blocked papers" list of
`reports/merge-plan.md`.

## 7. Duplicate `(paper, chapter, block_index)` in the quote layer

Zero in A, B, C and D, and every quote row's ordinal is inside its chapter's group
range with the same job as the record's group at that ordinal (checked per lane,
`quotes.index_out_of_range` and `quotes.job_mismatch` both empty). Pass.

## 8. Duplicate chapter labels inside one paper

F only: 48 of 48 papers, 276 extra chapter rows. F prints several sections under one
normalized function (`model-establishment` up to 11 times in
`P-F-2022-2209952-fcd31d6e`), so `(paper, chapter)` is not unique in F
(6,794 rows, 3,858 distinct keys over all six lanes; F alone 672 rows, 396 keys).

Ruling: the merge key must include a per-paper section ordinal,
`(paper, chapter_index, group_index)`, and F records must gain `chapter_index`
without changing their blocks, groups or jobs. Until then F cannot be merged under
a `(paper, chapter)` key. Per-paper counts in `recount.json` →
`lanes.F.duplicate_chapter_labels`.

## 9. Manifest coverage

| lane | queued (manifest eligible) | coded | missing | ruling |
|---|---|---|---|---|
| A | 84 | 84 | 0 | complete |
| B | 76 | 76 | 0 | complete |
| C | 112 | 112 | 0 | complete |
| D | 55 | 49 | `P-D-2024-2419588-1cc62ede`, `P-D-2024-2429211-de10f571`, `P-D-2025-2504188-db12259e`, `P-D-2025-2507692-249f88dd`, `P-D-2025-2516219-17e4e820`, `P-D-2025-2519935-f07f7c47` (6 at this snapshot; the count falls while D runs) | D still running |
| E | 60 | 60 | 0 | complete |
| F | 48 | 48 | 0 | complete |

E and F have no `queue.txt` in the same form; both are complete against the
manifest counts.

## 10. Live ledger comparison

`artifacts/paragraph-ledger.jsonl` holds 223 rows at this snapshot (A 93, B 67,
C 5, D 5, E 5, F 48), up from the 181 named in the lane goal and from 222 an hour
earlier, because another session appends to it while this lane runs.

- Granularity: the ledger is chapter-level (`stored_count`, `jobs`,
  `function_strings`), one row per `(paper, chapter)`; the lanes hold 4,134 chapter
  rows (3,858 distinct keys) and 40,294 groups. The ledger is not a group-level
  file and cannot be appended to from group rows.
- Every ledger key exists in the lanes (0 orphan keys). 3,635 lane chapter keys are
  absent from the ledger, i.e. the ledger is a 5.8% partial index, not a competing
  count.
- Ledger chapters are all inside the fourteen-value vocabulary; no duplicates.

Ruling: do not write the merge into `paragraph-ledger.jsonl`. Build the group-level
artifact separately and keep the ledger as the chapter-level index; reconciling the
two granularities is a human decision recorded in `reports/merge-plan.md`.
