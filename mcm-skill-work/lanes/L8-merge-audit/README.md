# L8 — merge audit (pre-merge reconciliation lane)

Read-only audit of the six coding lanes and the quote layer, producing the counts,
deltas, row shape and merge plan that the `artifacts/language-units/` merge needs
before anything is written there. This lane writes nothing outside
`lanes/L8-merge-audit/`.

## Inputs (read-only)

| input | used for |
|---|---|
| `lanes/L6-a-evidence/records-a/*.json`, `quotes-a.jsonl` | A lane rows (block-level, quote in-record) |
| `lanes/L4-b-ledger/records/*.json`, `jobs-b.jsonl`, `layout/` | B lane rows |
| `lanes/L3-c-ledger/records/*.json`, `jobs-c.jsonl`, `layout/` | C lane rows |
| `lanes/L2-d-ledger/records/*.json`, `jobs-d.jsonl`, `layout/` | D lane rows |
| `lanes/L5-e-ledger/records/*.json`, `jobs-e.jsonl`, `layout/` | E lane rows |
| `lanes/L1-f-structure/records/*.json`, `jobs-f.jsonl`, `layout/` | F lane rows |
| `lanes/L7-quote-backfill/quotes-{b,c,d}.jsonl`, `reports/coverage.json` | B/C/D quote rows and match levels |
| `artifacts/corpus/manifest.jsonl` | eligible papers per type |
| `artifacts/language-units/P-*.json` | chapter `paragraph_count` / `paragraph_functions`, and the nine-corpus chapter census |
| `artifacts/paragraph-ledger.jsonl` | live ledger, compared only; never written |

Forbidden: `artifacts/**`, any other lane directory, `~/.claude/skills/**`, `tmp/**`,
`plan.md`, `~/.claude/settings.json`.

## Outputs

| file | content |
|---|---|
| `README.md` | this file |
| `tools/audit.py` | recount and check tool; writes `reports/recount.json` |
| `reports/recount.json` | machine recount: per lane papers, chapters, groups, blocks, pages, job and chapter censuses, three-way denominators, check rows, merge totals, ledger comparison |
| `reports/deltas.md` | every difference, each with current value / expected value / ruling |
| `reports/row-shape.md` | unified row shape for the merge, the two existing shapes, quote-level distribution, E/F gaps per paper |
| `reports/merge-plan.md` | merge candidates, totals, conflict keys, human rulings needed |

## Three denominators

Every lane is counted three ways, and the audit prints all three:

1. **records** — `records/<pid>.json` (A: `records-a/<pid>.json`), excluding
   `*.skipped.json`. Chapters, groups and blocks are recomputed from those files.
2. **jobs** — `jobs-<lane>.jsonl` line count and the per-row `group_count` /
   `literal_blocks` fields. A has no jobs file.
3. **quotes** — L7 `quotes-{b,c,d}.jsonl` and `records-a`-backed `quotes-a.jsonl`.
   Each quote row is one group; E and F have no quote layer.

`groups == quote rows` per lane is the target. A shortfall is a delta even when it
is documented elsewhere.

## Two record shapes

- **Chapter shape** (B, C, D, E, F): one file per paper, a list of
  `{chapter, heading, pages, groups, jobs, note}`; `groups` is a list of block-index
  lists; `jobs` is parallel to `groups`.
- **Block shape** (A): a list of `{paper, chapter, blocks: [{block_index, job, quote,
  page}]}`, already block-level with the quote inline, and `block_index` is 0-based
  while every other lane's block index is the layout's 1-based `n`.

## Chapter vocabulary

The stored schema admits 24 labels. Fourteen are chapter functions:

`abstract, introduction, assumptions, notation, data-preprocessing,
model-establishment, model-improvement, algorithm, results, sensitivity-analysis,
robustness-verification, strengths-limitations, memo, conclusion`

The other ten are structural or variant labels: `title`, `problem-restatement`,
`problem-analysis`, `error-analysis`, `sensitivity-robustness`, `strengths`,
`limitations`, `future-improvements`, `references`, `appendix`.

Lanes already ruled on some of these: B treats `title` as out of scope and keeps
`limitations`, `strengths`, `error-analysis` verbatim (B README); E keeps the same
plus `sensitivity-robustness` verbatim (E README); F relabels local names into
`recommendation`, `model-testing` and `future-improvements`, which are themselves
outside the fourteen. D's nine ad-hoc labels (`cultural-analysis`,
`technology-impact`, `illustration`, `heavy-trucks`, `our-work`, `recommendations`,
`advice`, `future-considerations`, `gcn-evidence`) were never ruled on and are
merge-blocking, not merely cosmetic.

## Job vocabulary

Thirteen jobs — `route, define, source, select, derive, compute, read-figure,
compare, check, limit, mechanism, interpret, handoff` — plus the two extras
`ext:context` and `ext:claim`, optionally suffixed `+close:<job>`. Anything else is
a defect.

## Verification

- `python tools/audit.py` twice leaves `reports/recount.json` byte-identical.
- Every mismatch between the three denominators appears in `reports/deltas.md` with
  a non-empty ruling.
- `reports/row-shape.md` covers both record shapes and lists E and F gaps per paper.
- `reports/merge-plan.md` totals are recomputable by `tools/audit.py`.
- `git status --porcelain artifacts` stays empty while this lane runs.

## Status

`reports/recount.json` sha256 `2c7c0082…dda0f4`, written by two consecutive
`tools/audit.py` runs with identical bytes. 108 checks, 21 of them `delta`; every
delta appears in `reports/deltas.md` with a ruling.

| lane | papers | chapter rows | groups | quote rows | state |
|---|---|---|---|---|---|
| A | 84 | 93 | 3,232 | 3,232 | complete, 2 blocks with job `unresolved` |
| B | 76 | 1,068 | 10,333 | 10,333 | complete |
| C | 112 | 1,112 | 10,404 | 10,404 | complete, 23 duplicate block references |
| D | 49 | 527 | 4,646 | 4,507 | still coding, 6 papers outstanding |
| E | 60 | 662 | 5,024 | none | complete, no quote layer |
| F | 48 | 672 | 6,794 | none | complete, 276 chapter-key collisions |

Merge candidates: 40,294 rows (groups 40,433; quote-backed 28,476; E/F unquoted
11,818; D's 139 unquoted groups held back). Chapter rows 4,134, distinct
`(paper, chapter)` keys 3,858. Live `artifacts/paragraph-ledger.jsonl`: 223 rows,
chapter-level, 3,635 lane chapter keys absent from it.

C, D and the live ledger move while other sessions run, so `recount.json` is a
snapshot and the reports cite that snapshot. Only `lanes/L8-merge-audit/` was
written; `artifacts/paragraph-ledger.jsonl` remains modified by another session,
which the session-start `git status` already showed.
