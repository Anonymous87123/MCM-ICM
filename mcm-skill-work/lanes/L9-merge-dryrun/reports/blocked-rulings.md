# Blocked rulings — what a human still has to decide

Nine questions, same list as `lanes/L8-merge-audit/reports/merge-plan.md` §5, now
with the row impact measured. The row file already reflects a *proposed* answer
for each: aliases applied per L8 §3, unruled labels nulled and blocked, `claim`
kept verbatim, duplicates blocked, empty chapters rowless, both page spans kept,
quote level left null where L7 emits only a lane census. None of these proposals
writes an artifact; changing one is a rebuild, not a re-code.

Totals at snapshot `9b6b9cdc…4369e18`: 41,088 rows = 40,406 `merge` + 606
`blocked` + 76 `excluded`. Every open item below is now a vocabulary decision:
the quote layer is complete in all six lanes and the duplicate-block defects are
closed, so nothing is blocked on evidence or on a coding error.

## 1. Ledger fate

`artifacts/paragraph-ledger.jsonl` is chapter-level: 223 rows, one per
`(paper, chapter)`, with `stored_count` / `jobs` / `function_strings`. This lane
produces 4,205 chapter rows' worth of groups, 41,088 rows. They cannot be
appended to each other.

- Rows affected: all 41,088, by granularity.
- Options: (a) new group-level artifact beside the ledger; (b) regenerate the
  ledger from merged rows; (c) retire the ledger; (d) keep the ledger as a
  chapter index and never mix the two.
- Decides: the merge session's owner, with the artifacts owner's consent.

## 2. Chapter alias map

2,635 rows carry a chapter label that is outside the fourteen and mapped by an
alias rather than by a ruling from its own lane:

| lane | label | rows | → |
|---|---|---|---|
| B | `problem-analysis` | 415 | introduction |
| B | `sensitivity-robustness` | 241 | sensitivity-analysis |
| B | `problem-restatement` | 131 | introduction |
| B | `future-improvements` | 97 | strengths-limitations |
| B | `limitations` | 30 | strengths-limitations |
| B | `strengths` | 30 | strengths-limitations |
| B | `error-analysis` | 34 | results |
| C | `problem-analysis` | 728 | introduction |
| C | `future-improvements` | 351 | strengths-limitations |
| C | `problem-restatement` | 62 | introduction |
| C | `limitations` | 26 | strengths-limitations |
| C | `strengths` | 26 | strengths-limitations |
| C | `sensitivity-robustness` | 16 | sensitivity-analysis |
| C | `error-analysis` | 9 | results |
| D | `problem-restatement` | 56 | introduction |
| D | `future-improvements` | 41 | strengths-limitations |
| D | `problem-analysis` | 35 | introduction |
| D | `sensitivity-robustness` | 17 | sensitivity-analysis |
| D | `error-analysis` | 9 | results |
| E | `sensitivity-robustness` | 76 | sensitivity-analysis |
| E | `problem-restatement` | 71 | introduction |
| E | `strengths` | 61 | strengths-limitations |
| E | `limitations` | 48 | strengths-limitations |
| E | `problem-analysis` | 11 | introduction |
| E | `future-improvements` | 3 | strengths-limitations |
| E | `error-analysis` | 1 | results |
| F | `future-improvements` | 10 | strengths-limitations |

- Stakes: these 2,635 rows change `chapter_normalized` if the map is amended;
  `chapter` never changes either way.
- Note: B and E READMEs keep `limitations` / `strengths` / `error-analysis`
  verbatim; the map only fills `chapter_normalized`, it does not rename.
- Decides: merge session.

## 3. D's nine local labels

70 rows in 9 papers, none of them documented in the D README.

| label | rows | paper |
|---|---|---|
| `recommendations` | 24 | `P-D-2020-2003723-28f692ff` |
| `gcn-evidence` | 9 | `P-D-2021-2101855-c4682962` |
| `cultural-analysis` | 8 | `P-D-2017-67316-f37f83c8` |
| `our-work` | 7 | `P-D-2019-1900007-65267201` |
| `technology-impact` | 7 | `P-D-2018-82504-6cc63169` |
| `advice` | 5 | `P-D-2020-2015044-db9655c7` |
| `future-considerations` | 5 | `P-D-2020-2022868-71331b90` |
| `illustration` | 4 | `P-D-2018-82794-47f05792` |
| `heavy-trucks` | 1 | `P-D-2018-82794-47f05792` |

- Proposed by L8: `our-work` → introduction, `recommendations` → memo,
  `future-considerations` → future-improvements, `heavy-trucks` /
  `gcn-evidence` → model-establishment, and the rest to whichever chapter carries
  the printed section. Applied: nothing. All 70 rows are `blocked`.
- Decides: D's author confirms the mapping; the merge session applies it.

## 4. F's `recommendation` and `model-testing`

534 rows in 34 papers — 13% of F and the largest single block of blocked rows in
the file.

| label | rows | papers |
|---|---|---|
| `recommendation` | 399 | 23 |
| `model-testing` | 135 | 11 |

- L8 counted the chapters (29 and 13). At row level these are 534 rows, because
  each chapter carries 10-20 groups.
- Options: keep as first-class labels and extend the vocabulary, or normalise
  (`recommendation` → memo, `model-testing` → robustness-verification).
- Decides: F's author (the README declares them as corpus labels) plus the merge
  session.

## 5. `claim` and `context`

1,079 rows carry `base_job = claim` (B 340, C 156, D 386, F 197) and 447 carry
`base_job = context` (B 183, C 6, D 86, F 172); 332 rows also carry a
`close_job`.

- Options: merge verbatim under two vocabularies, or normalise `claim` →
  `interpret` (L7 README's suggestion).
- Stakes: a fan-out over `base_job` changes shape if `claim` folds into
  `interpret`; `job` stays verbatim in either case.
- Decides: merge session, as L7 already recorded.

## 6. Duplicate block references

Closed, not decided: 0 rows blocked and 0 duplicated blocks at this snapshot.
Earlier builds flagged 36 rows (C 30 in 8 papers, D 6 in 3 papers) where one
printed unit was coded into two groups; both lane owners removed the duplicates
while this lane ran. The key list stays in `conflicts.md` §4 so a regression is
attributable. Nothing here needs a human ruling now.

## 7. Empty chapter rows

50 chapter rows with zero groups (C 31, D 2, E 10, F 7) produce no merge row.

- Options: keep them in the chapter index only (current behaviour), or drop them
  from the index as well.
- Decides: merge session. Nothing changes in `rows.jsonl` either way.

## 8. Page-span policy

Every row carries `pages_declared` (the record's chapter span; null for A) and
`pages_coded` (min/max of the group's layout blocks). 806 rows have coded pages
falling outside the declared span (B 88, C 341, D 142, E 83, F 152), because the
stored span is inherited from `artifacts/language-units/` and a heading glued to
the first block can push it a page later.

- Options: accept declared-with-coded-beside-it (current), or re-derive `pages`
  from coded blocks lane by lane.
- Decides: merge session, with each lane author's consent since it edits records.

## 9. Quote verification level

L7 emits `levels-<lane>.json` as a census only, so no row can say whether *its*
quote was `exact`, `nfkc`, `squeezed`, `span`, `gapped`, `layout-only`,
`ocr-only` or `unverified`. `quote_level` is therefore `in-record` for A and
`null` for B-F, and `inputs/levels.json` carries the lane census beside it:
B `unverified` 280, C 181 + `layout-only` 97, D 72, E 83, F 154 — 770 unverified
and 97 layout-only rows, none of them individually identifiable. Every lane is now
fully quoted, so each lane's census covers all of its rows.

- Options: (a) accept the census and treat the whole lane as partly unverified;
  (b) ask L7 to emit a per-row level (a `quote_level` field on its own rows);
  (c) re-verify in the merge session.
- Recommended: (b). It is a one-field change on L7's side and it is the only
  option that lets the merged artifact quarantine the 867 weak rows without
  dropping whole lanes.
- Decides: L7's owner.
