# Conflicts — every row-level difference, with a ruling

Machine source: `reports/rows.jsonl` and `reports/stats.json` at snapshot
`9b6b9cdc…4369e18` (rows `19f4dad3…48ae04a1`). Every count below is recomputed by
`tools/build_rows.py`; nothing is hand arithmetic.

Scope: L8 listed the *audit* deltas. This file lists what those deltas look like
once rows exist — which rows are affected, in which paper, under which key.

## 1. Denominators: record groups vs quote rows vs built rows

| lane | record groups | quote rows | built rows | quote joined | shortfall |
|---|---|---|---|---|---|
| A | 3,232 | 3,232 | 3,232 | 3,232 | 0 |
| B | 10,333 | 10,333 | 10,333 | 10,333 | 0 |
| C | 10,397 | 10,397 | 10,397 | 10,397 | 0 |
| D | 5,308 | 5,308 | 5,308 | 5,308 | 0 |
| E | 5,024 | 5,024 | 5,024 | 5,024 | 0 |
| F | 6,794 | 6,794 | 6,794 | 6,794 | 0 |
| total | **41,088** | **41,088** | **41,088** | **41,088** | **0** |

Every lane now joins to the quote layer with no shortfall and no unused quote row.
Two defects this section carried earlier were closed by their owners while the
lane ran, not by this lane:

- D's `P-D-2025-2519935-f07f7c47` had 116 groups and zero quote rows because
  `quotes-d.jsonl` predated the paper's closure. L7 re-emitted it at 02:00 with 55
  papers and 5,308 rows, and the paper's 116 units are now quoted.
- C and D removed the duplicate block references listed in §4, which is also why
  their group counts fell (C 10,404 → 10,397, D 5,309 → 5,308).

The re-emit spec this file previously carried is withdrawn: the file it described
now exists. `quotes-d.jsonl` remains L7's file and is never written from here.

## 2. Jobs outside the 13 + 2 vocabulary

| lane | rows | keys | ruling |
|---|---|---|---|
| A | 2 | `P-A-2018-76271-27d535ab` / `model-establishment` / `group_index` 30 and 31 / `block_index` 29 and 30, job `unresolved` | record defect; L6 must recode. Blocked, not merged. |
| B–F | 0 | — | every job normalises to a base job plus an optional `+close:` |

`base_job` is derived as `job.split("+close:")[0]` minus the `ext:` prefix, so
`ext:claim` → `claim` and `ext:context` → `context`; those two are the declared
extras, not defects. `claim` → `interpret` remains a merge-session decision.

## 3. Chapter labels and `chapter_normalized`

Distinct labels per lane: A 2, B 24, C 23, D 29, E 23, F 13 — against a
fourteen-value vocabulary. Rows whose `chapter_normalized` is null, by reason:

| lane | front matter (`title`, excluded) | structural (`appendix`) | `references` | unruled | total null |
|---|---|---|---|---|---|
| A | 0 | 0 | 0 | 0 | 0 |
| B | 76 | 91 | 67 | 0 | 234 |
| C | 0 | 46 | 82 | 0 | 128 |
| D | 0 | 18 | 96 | **70** | 184 |
| E | 0 | 22 | 76 | 0 | 98 |
| F | 0 | 0 | 0 | **534** | 534 |

Alias rows (`problem-analysis`, `problem-restatement`, `sensitivity-robustness`,
`future-improvements`, `strengths`, `limitations`, `error-analysis`) normalise per
L8 `deltas.md` §3 and are not counted as null: `chapter` stays verbatim,
`chapter_normalized` carries the fourteen-value target.

Unruled labels — blocked, `chapter_normalized = null`, no silent mapping — 604
rows in total (D 70, F 534):

| lane | label | rows | papers |
|---|---|---|---|
| D | `recommendations` | 24 | 1 |
| D | `gcn-evidence` | 9 | 1 |
| D | `cultural-analysis` | 8 | 1 |
| D | `our-work` | 7 | 1 |
| D | `technology-impact` | 7 | 1 |
| D | `advice` | 5 | 1 |
| D | `future-considerations` | 5 | 1 |
| D | `illustration` | 4 | 1 |
| D | `heavy-trucks` | 1 | 1 |
| F | `recommendation` | 399 | 23 |
| F | `model-testing` | 135 | 11 |

`chapter-label-unknown` is empty: every label in the corpus is either one of the
fourteen, a ruled alias, structural, front matter, or one of the eleven above.

Note that L8 counted these as *chapter rows* (D 9 labels 1 row each; F 29 + 13).
At row level F's two labels cover 534 rows across 34 papers, which is why F's
blocked count is the largest in the file despite having the fewest labels.

## 4. Duplicate block references

Resolved: 0 rows blocked, 0 duplicated blocks in any lane at this snapshot.

Earlier builds flagged 36 rows (C 8 papers / 23 blocks / 30 rows, D 3 papers / 3
blocks / 6 rows) where one layout block was coded into two groups of the same
paper. Both C and D owners removed the duplicates while this lane ran; the group
counts fell accordingly (C 10,404 → 10,397, D 5,309 → 5,308) because a group that
lost its only block disappeared with it. The historical key list, kept for
traceability:

| lane | papers | blocks | rows | keys |
|---|---|---|---|---|
| C | 8 | 23 | 30 | `P-C-2011-11893-6a9ea7d9` 22; `P-C-2013-21165-17e64d15` 39; `P-C-2024-2401298-07d37078` 160, 180, 189, 194, 202; `P-C-2024-2401445-6a882749` 74-83; `P-C-2024-2403774-be4a823f` 24, 48, 64; `P-C-2024-2406176-bd7757f9` 225; `P-C-2024-2409961-92b90752` 60, 179; `P-C-2024-2410482-2f099d31` 100 |
| D | 3 | 3 | 6 | `P-D-2016-49436-4c3ef010` 192; `P-D-2017-55285-1835cc0b` 181; `P-D-2021-2101855-c4682962` 209 |

A, B, E and F never had one. The check stays in the tool, so a regression in any
lane reappears here rather than being silently merged.

## 5. Front matter

B carries 8 `title` chapters, 76 groups. Those rows are emitted with
`evidence_class = front-matter` and `status = excluded` so the row count still
equals the block count, but they are not part of the merge stream. No other lane
stores a `title` chapter.

## 6. Blocks, pages, and layout

| check | rows | ruling |
|---|---|---|
| `block-missing-in-layout` (record cites a block the layout does not have) | 0 | pass; every coded block exists as a paragraph `n` |
| `page-outside-pdf` (quote page beyond the manifest `page_count`) | 0 | pass |
| `pages_coded` unavailable | 0 | every row has a page span; A takes it from the block page, B-F from the layout index |
| `pages_declared` null | 3,232 | A stores no chapter span; `pages_declared = null` is expected there |

Page-span understatement (declared span narrower than the coded blocks) is
carried, not repaired: `pages_declared` and `pages_coded` are both on every row,
so the merge can choose. L8 counted the understating chapters per lane.

## 7. Quote layer joins

| check | rows | ruling |
|---|---|---|
| duplicate `(lane, paper, chapter_index|chapter, block_index)` quote keys | 0 | join is unambiguous |
| row↔quote mismatch on paper, chapter, job or page | 0 | 41,088 joined rows checked, four fields each |
| unused quote rows (quote with no group) | 0 | no orphan evidence |

The join is keyed on the group ordinal, not on the layout block: A–D quote rows
carry `block_index` = 0-based group ordinal inside the chapter, E/F add a 0-based
`chapter_index`. Rows carry `block_index` = the group's first layout block plus
`block_index_basis`, so the two meanings never get confused downstream.

## 8. Empty chapter rows

Coded chapter rows with zero groups contribute no merge row: C 31, D 2, E 10, F 7
(50 of 4,205 chapter rows). They stay in the chapter index and are absent from
`rows.jsonl`. Ruling: keep them in the index, emit nothing; a chapter with no
printed unit must not create a row with an empty quote.

## 9. Advisory — short quotes

2,301 rows carry a quote shorter than 15 characters (A 13, B 601, C 569, D 350,
E 320, F 448), mostly heading-shaped quotes such as `1.1Background`. They are
verbatim and legal, but they are weak evidence for a language row. Not a defect.
Ruling: a merge session that needs a minimum evidence strength should filter on
`quote_len`, not on the record.

## 10. Relationship to L8

L8's snapshot was 40,294 candidate rows (49 D papers, no E/F quotes). This file
is built on 41,088 rows (55 D papers, every lane quoted), so the two totals differ
by 794 rows: 662 from D's growth (5,308 − 4,646 groups), 139 that L8 held back as
unquoted D groups and that are now quoted, less 7 groups C removed with its
duplicate blocks (10,404 → 10,397). L8's audit
remains correct for its own snapshot; its row-shape and merge-plan sections stay
the specification this lane implements.
