# Merge plan — candidates, totals, conflicts, human rulings

Everything below is recomputed by `tools/audit.py`; the totals section is the
`merge` block of `reports/recount.json`, and `python tools/audit.py` reproduces it
byte for byte while the inputs stand still (proven twice, `2c7c0082…dda0f4`). C, D
and the live ledger are still being written by other sessions, so re-running the
tool later will move the C and D rows and the ledger count.

Nothing in this plan writes to `artifacts/`. No artifacts file is created, edited
or appended by this lane.

## 1. Rows available per lane

| lane | papers | chapter rows | group rows | quote-backed | quote level source |
|---|---|---|---|---|---|
| A | 84 | 93 | 3,232 | 3,232 | in-record quote per block |
| B | 76 | 1,068 | 10,333 | 10,333 | L7 `quotes-b.jsonl` |
| C | 112 | 1,112 | 10,404 | 10,404 | L7 `quotes-c.jsonl` |
| D | 49 | 527 | 4,646 | 4,507 | L7 `quotes-d.jsonl` (−139) |
| E | 60 | 662 | 5,024 | 0 | none |
| F | 48 | 672 | 6,794 | 0 | none |
| **total** | **429** | **4,134** | **40,433** | **28,476** | |

- Group rows are the merge unit (one printed unit, one job, one quote slot).
- Merge-candidate rows are 40,294, not 40,433. Rule used: a lane that has a quote
  layer contributes its quote rows; a lane with no quote layer (E, F) contributes
  its group rows marked `quote_level = missing`. D therefore contributes 4,507, and
  the 139 groups of `P-D-2024-2417831-f399a6df`, coded after L7 ran, are held back
  until L7 re-emits. This is `merge.total` in `recount.json`.
- Chapter rows are 4,134, but only 3,858 distinct `(paper, chapter)` keys exist,
  because F repeats chapter labels inside a paper (276 extra rows).
- Quote-backed rows: 28,476 (70.7%). Rows with no quote layer: 11,818 (E 5,024 +
  F 6,794, 29.3%).
- Rows blocked by a defect rather than by a missing quote layer: A 2
  (`unresolved` job), C 23 and D 3 duplicate-block rows that would double-count a
  printed unit.

## 2. Divergence from `artifacts/paragraph-ledger.jsonl`

| | ledger | lanes |
|---|---|---|
| granularity | chapter-level | group-level |
| rows | 223 | 40,294 groups / 4,134 chapter rows |
| papers | 214 | 429 |
| types | A 93, B 67, C 5, D 5, E 5, F 48 | A 84, B 76, C 111, D 48, E 60, F 48 papers |
| keys | 223 distinct `(paper, chapter)`, 0 duplicates, all inside the fourteen-value vocabulary | 3,858 distinct keys |

The ledger is a 5.8% partial chapter index (3,635 lane chapter keys absent), not a
competing row count. Its schema (`stored_count`, `jobs`, `function_strings`) is the
stored language-units paragraph index, which is why `stored_count` there is a
paragraph count and not a group count: the two are not interchangeable (B alone has
10,333 groups against 9,833 stored slots, and the per-chapter sign of that delta is
documented in each note).

The lane goal's text names 181 ledger rows; the file held 222 when this lane opened
and 223 at the snapshot, so the goal's number is stale, not a second denominator.

Ruling: the merge produces a **new** group-level artifact and leaves the
chapter-level ledger untouched. Whether the ledger should later be regenerated from
the merged rows, kept as an index, or dropped is a human decision (§5, item 1).

## 3. Conflict keys

1. **`(paper, chapter)` in F** — 48 of 48 papers repeat a label; 276 extra rows;
   worst case `P-F-2022-2209952-fcd31d6e` with `model-establishment` 11 times.
   Resolved by adding `chapter_index` (row-shape §2). F records must gain that
   field; groups and jobs do not change.
2. **`(paper, block_index)` in C and D** — 23 + 3 blocks coded into two groups or
   chapters. A merge must refuse the paper rather than emit two jobs for one block.
3. **`block_index` meaning across lanes** — A is a 0-based chapter ordinal, B-F are
   1-based layout paragraph numbers, and the quote files' `block_index` is a 0-based
   group ordinal. Resolved by naming the basis per row and by keying the join on
   `group_index`, not on `block_index`.
4. **`(paper, chapter, block_index)` in the quote layer** — zero duplicates today in
   A-D, so the quote join is safe for the rows that exist.

## 4. Per-paper readiness

| lane | status | blocking items |
|---|---|---|
| A | one fix from ready | 2 blocks with job `unresolved` (`P-A-2018-76271-27d535ab` 29, 30) |
| B | ready under the alias rulings | 0 record defects; 169 chapter labels outside the fourteen need the alias map in `deltas.md` §3; 21 page-span understatements (carry both spans, do not rewrite) |
| C | not ready | lane complete and quote layer complete; 23 duplicate block references; 31 empty chapter rows; 246 off-vocabulary chapter labels |
| D | not ready | lane still coding (6 papers of 55 outstanding); `P-D-2024-2417831-f399a6df` coded after L7 ran (139 rows without quotes); 9 unruled D-local chapter labels; 3 duplicate block references |
| E | rows ready, quotes absent | 0 record defects; 5,024 rows need a quote pass; 166 off-vocabulary labels already ruled by the E README |
| F | not ready | 276 chapter-key collisions need `chapter_index`; `recommendation` (29) and `model-testing` (13) unruled; 6,794 rows need a quote pass |

Merge order that respects the dependencies: B (alias map approved) → A (2-block
fix) → C after its duplicate-block papers are fixed → E and F as quote-less rows
marked `quote_level = missing` → D after its lane closes and L7 re-emits.

## 5. Items that need a human ruling

1. Ledger fate: new group-level artifact beside the chapter-level ledger, or
   regenerate the ledger from merged rows, or retire it.
2. Alias map: `problem-analysis`, `problem-restatement` → `introduction`;
   `sensitivity-robustness` → `sensitivity-analysis`; `strengths`, `limitations`,
   `future-improvements` → `strengths-limitations`; `error-analysis` → `results`;
   `references`, `appendix` marked structural; `title` dropped. Approve or amend.
3. D's nine local labels (`cultural-analysis`, `technology-impact`, `illustration`,
   `heavy-trucks`, `our-work`, `recommendations`, `advice`, `future-considerations`,
   `gcn-evidence`) — one row each, no ruling exists in the D lane. Proposed mapping
   in `deltas.md` §3; D's author must confirm.
4. F's `recommendation` (29 rows) and `model-testing` (13 rows) — normalise to
   `memo` and `robustness-verification`, or keep as first-class labels and extend
   the vocabulary. F README already treats them as declared corpus labels.
5. `claim` → `interpret`: B carries 290 `claim` rows plus `ext:claim` forms. Merge
   verbatim (two vocabularies in one artifact) or normalise.
6. Duplicate block references in C (23) and D (3): C/D authors fix, or the merge
   excludes the affected papers.
7. Empty chapter rows (C 29, D 1, E 10, F 7): emit no group row and keep the
   chapter in the index, or drop the chapter row entirely.
8. Page-span policy: accept `pages_declared` (stored chapter span) with
   `pages_coded` beside it, or re-derive `pages` from coded blocks lane by lane.
9. Unverified quotes: 406 B/C/D rows are `unverified` and 97 are `layout-only`. Keep
   them flagged, or hold them back from the merged artifact until re-verified.

## 6. Recompute

```
python -I -X utf8 lanes/L8-merge-audit/tools/audit.py
```

Writes `reports/recount.json`; the `merge` block holds `rows_by_lane`, `total`,
`rows_without_quote_layer`, `chapters`, and `gap_by_paper` (E and F per paper), and
the `ledger` block holds the comparison in §2. Running it twice on unchanged inputs
produces a byte-identical file.
