# L9 — merge dry run (staging rows, no artifacts write)

Turns the row shape that `lanes/L8-merge-audit/reports/row-shape.md` specifies
into an executable builder, and emits one staging row per coded group. This lane
decides nothing and writes no corpus artifact: it produces the candidate rows,
the conflict list and the unanswered questions, so a merge session can start from
a measured file instead of a prose spec.

Writes only `lanes/L9-merge-dryrun/**`.

## Inputs (read-only)

| input | use |
|---|---|
| `lanes/L6-a-evidence/records-a/*.json`, `quotes-a.jsonl` | A rows (block shape, quote in-record) |
| `lanes/L4-b-ledger/records/*.json`, `layout/` | B rows |
| `lanes/L3-c-ledger/records/*.json`, `layout/` | C rows |
| `lanes/L2-d-ledger/records/*.json`, `layout/` | D rows |
| `lanes/L5-e-ledger/records/*.json`, `layout/` | E rows |
| `lanes/L1-f-structure/records/*.json`, `layout/` | F rows |
| `lanes/L7-quote-backfill/quotes-{b,c,d,e,f}.jsonl`, `reports/levels-*.json` | quote layer and per-lane match-level census |
| `artifacts/corpus/manifest.jsonl` | `page_count`, for the page-in-PDF check |

Forbidden: `artifacts/**`, any other lane directory, `~/.claude/skills/**`,
`tmp/**`, `plan.md`, `~/.claude/settings.json`.

## Outputs

| file | content |
|---|---|
| `README.md` | this file |
| `tools/build_rows.py` | `snapshot` and `build` modes |
| `inputs/records.jsonl` | frozen projection of the six record sets, one line per chapter row |
| `inputs/quotes.jsonl` | frozen projection of the quote layer, one line per quote row |
| `inputs/pages.json` | frozen `paper -> {layout block n: pages}` index |
| `inputs/levels.json` | frozen per-lane match-level census |
| `reports/snapshot.json` | sha256 of every original input and of each projection |
| `reports/rows.jsonl` | one row per coded group, 24 fields, sorted |
| `reports/stats.json` | per-lane and total counts, blocked-reason census, dedupe result |
| `reports/conflicts.md` | every row-level conflict with lane, count, keys |
| `reports/blocked-rulings.md` | the questions a human still has to answer, with row impact |

## Why the inputs are frozen twice

The C and D lanes and the quote layer are written by other sessions while this
lane runs. A build that read them live could not be reproduced even twice in a
row. So `snapshot` writes a *projection* — the fields a merge row needs, the
quote's sha256 and length instead of its text, and a page index instead of the
39 MB of `layout/` — and records the sha256 of both the projection and the
originals it came from. `build` reads only the projection and refuses to run if a
projection file changed. `reports/rows.jsonl` is therefore byte-stable while the
live lanes keep moving; `snapshot` again to move to a newer state and the
snapshot hash in `stats.json` changes with it.

Quote text is not copied. Each row carries `quote_sha256`, `quote_len`, `page`,
`source_quote_file` and `source_quote_row`, so a merge session reads the verbatim
quote from the source file by line number and can re-verify the hash.

## Row shape

Field list, ordering and key are L8's (`reports/row-shape.md` §2), with one
addition: `source_quote_file`, because two lanes' quotes no longer live in one
directory.

- Ordering: `(type, paper, chapter_index, group_index)`.
- Dedupe key: `(paper, chapter_index, group_index)`.
- `chapter_index` is 1-based print order inside the paper. E/F quote rows carry it
  themselves (0-based, shifted here); A-D get it from the record's chapter order,
  which is why B/C/D must not have repeated labels — they do not.
- `block_index` is the first block of the group. `block_index_basis` says
  `layout-paragraph-n` (B-F) or `record-ordinal-0` (A).
- `status`: `merge`, `blocked` (see `blocked_reasons`) or `excluded`
  (front matter: the `title` rows, kept so the row count still matches the quote
  layer, but not part of the merge stream).

## Status at the pinned snapshot

`reports/snapshot.json` sha256 `9b6b9cdc…4369e18`,
`reports/rows.jsonl` sha256 `19f4dad3…48ae04a1`,
`reports/stats.json` sha256 `9122a4b0…b0b98559`. Two consecutive `build` runs are
byte-identical.

| lane | papers | chapter rows | groups = rows | quote rows | merge | blocked | excluded |
|---|---|---|---|---|---|---|---|
| A | 84 | 93 | 3,232 | 3,232 | 3,230 | 2 | 0 |
| B | 76 | 1,068 | 10,333 | 10,333 | 10,257 | 0 | 76 |
| C | 112 | 1,112 | 10,397 | 10,397 | 10,397 | 0 | 0 |
| D | 55 | 598 | 5,308 | 5,308 | 5,238 | 70 | 0 |
| E | 60 | 662 | 5,024 | 5,024 | 5,024 | 0 | 0 |
| F | 48 | 672 | 6,794 | 6,794 | 6,260 | 534 | 0 |
| **total** | **435** | **4,205** | **41,088** | **41,088** | **40,406** | **606** | **76** |

This is the first state in which the quote layer covers every lane completely:
L7 re-emitted `quotes-d.jsonl` at 02:00 with 55 papers, closing the 116-row hole
this lane had flagged, so the join shortfall is 0. C and D also removed their
duplicate block references while this lane ran (C 10,404 → 10,397 groups, D 5,309
→ 5,308), which is why `duplicate-block-ref` no longer appears anywhere. What is
blocked now is vocabulary only: A's two `unresolved` jobs, D's nine unruled local
labels (70 rows) and F's `recommendation` / `model-testing` (534 rows).

Merge total 41,088 rows against L8's 40,294, all of the difference being D's
completion (49 → 55 papers) plus the 139 D rows L8 held back as unquoted.

## Verification

- `rows.jsonl` has one row per record group in every lane; the quote join has no
  shortfall anywhere and leaves no quote row unused.
- `(paper, chapter_index, group_index)` is unique: 41,088 keys, 0 duplicates.
- Quote join integrity: 0 mismatches on paper, chapter, job and page between a
  row and its `source_quote_row`.
- `python -I -X utf8 lanes/L9-merge-dryrun/tools/build_rows.py build` twice gives
  identical `rows.jsonl` and `stats.json`.
- `git status --porcelain artifacts` stays unchanged by this lane.
