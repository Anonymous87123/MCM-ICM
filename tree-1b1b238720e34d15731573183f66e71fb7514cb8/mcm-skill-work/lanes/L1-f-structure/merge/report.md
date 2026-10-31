# Merge and promotion audit: paragraph jobs across six types

Snapshot. The ledger is appended by another session while this audit runs, so it is
frozen to `merge/snapshot/paragraph-ledger.jsonl` before measuring:
sha256 `c6194c0b…97b83a1`, 180 rows (A 93, B 24, F 48, C 5, D 5, E 5). Refreeze with
`tools/freeze_ledger.py`, then run `tools/audit_merge.py`. F comes from
`jobs-f.jsonl`, sha256 `f28f3d88…830227`, 672 chapter records. The taxonomy is
`tmp/para-taxonomy.md`, sha256 `25375101…2f5b15822`. All hashes and paths are in
`taxonomy-sha256.txt`. Every number below is a field of the `metrics.json` written
by that run, for that frozen snapshot; it goes stale the moment the ledger grows.

## Method

1. **Sequence assembly.** One job sequence per `(type, chapter, paper)`, in print
   order. F comes from `jobs-f.jsonl`; the stale F rows in the ledger, which carry
   87 `unresolved` tokens, are ignored. A–E come from the ledger snapshot. Repeated
   records of one chapter label inside one paper are concatenated in file order, so
   a paper contributes one `results` or `model-establishment` sequence, not several.
2. **Token normalisation.** `+close:<job>` and `ext:` are stripped before
   comparison. `unresolved` is not a job: it marks a block the earlier pass could
   not name. Such tokens are dropped and the row is listed under
   `ledger_rows_with_unresolved` (one row: `P-A-2018-76271-27d535ab`,
   model-establishment, 2 dropped). Dropping shortens the sequence, which can only
   lower a paper's agreement, never raise it.
3. **Candidate patterns.** For each chapter label the pool is every sequence of
   every type. Candidates are the pool's position-wise modal sequence truncated
   where its own support drops below 60%, the pool's first-position modal job, and
   each type's own first-position modal job. Each candidate is scored per type as
   the share of that type's papers whose sequence starts with it.
4. **Rule under test** (`tmp/para-taxonomy.md`, unchanged): a sequence is promoted
   only when it holds in ≥60% of that type's read papers, in ≥4 of 6 types at the
   same position, and every claim carries one verbatim sentence from a paper read
   in full.

## Result 1 — the job vocabulary aligns, but five types barely exercise it

Blocks coded per type. `jobs-by-type.csv` carries all 13 jobs plus the two extras,
per type, with shares and paper counts.

| type | papers | chapter records | blocks | top jobs | jobs never used |
|---|---|---|---|---|---|
| A | 84 | 93 | 3230 | define 920, derive 486, read-figure 375, route 295 | context, claim |
| B | 24 | 24 | 343 | define 121, derive 50, route 28, limit 22 | context, claim |
| C | 5 | 5 | 66 | define 25, compare 9, interpret 7, source 6 | check, context, claim |
| D | 5 | 5 | 35 | define 16, derive 8, source 4, select 3 | compute, read-figure, limit, mechanism, interpret, handoff, context, claim |
| E | 5 | 5 | 86 | define 22, limit 13, route 8, derive 8 | read-figure, handoff, context, claim |
| F | 48 | 672 | 6794 | route 1325, define 1242, derive 726, read-figure 694 | context, claim |

No token outside the 13 jobs plus `ext:context` / `ext:claim` survives
normalisation in any type; the audit stops if one does. A, B and F use all 13 jobs.
C never uses `check`; D never uses six of the thirteen; E never uses `read-figure`
or `handoff`, and C, D and E still rest on 5 papers each, so a zero there means the
sample never needed the job rather than the type never using it. The two extras
appear only in F — 197 `ext:claim` and 172 `ext:context` blocks, concentrated in
introduction and strengths-limitations.

## Result 2 — stored `paragraph_functions` are per-paper labels, not template strings

The premise that A–E, or F, carry six or seven template strings is false. Over all
`chapter_layouts`:

| type | values | distinct | distinct share | median string length | chapters with repeats |
|---|---|---|---|---|---|
| A | 10111 | 9976 | 98.7% | 57 chars | 40 of 1244 |
| B | 10455 | 9088 | 86.9% | 91 chars | 333 of 1170 |
| C | 6006 | 5951 | 99.1% | 62 chars | 8 of 1112 |
| D | 2246 | 2239 | 99.7% | 25 chars | 3 of 558 |
| E | 3311 | 3311 | 100.0% | 34 chars | 0 of 668 |
| F | 4422 | 4353 | 98.4% | 26 chars | 17 of 441 |

The most repeated string in the corpus occurs 87 times (A: `method`), the next 82
(A: `setup`) — both short fragments, not a fixed template. Actual values look like
A `derive the baseline collision response and report the interior sweet-spot
location` and F `introduction paragraph 2: context -> evidence -> unresolved need ->
paper response`. B has the lowest distinct share because one paper family writes
`establish operational context for Summary` (40×) and `retain a scenario and claim
boundary for Summary` (28×); those 68 values are 0.7% of B.

Consequence: the strings locate blocks but cannot be tallied as a vocabulary,
exactly as `tmp/para-taxonomy.md` states. Repeated strings concentrate in A (40 of
1244 chapters) and B (333 of 1170, 28%), but stay a minority of chapters everywhere.

This section, and the coverage numbers in `blocked.md`, are measured on live inputs
(`artifacts/language-units/`, `artifacts/corpus/manifest.jsonl`) that another session
is rewriting while this lane runs: they describe the run that wrote `metrics.json`,
not necessarily the files on disk now. Everything else is measured on the frozen
ledger snapshot.

## Result 3 — no sequence passes the promotion rule

Best candidate per chapter (`metrics.json` → `promotion.tests` holds every
candidate with every per-type share):

| chapter | best candidate | types at ≥60% | verdict |
|---|---|---|---|
| model-establishment | first job `define` | B, D, E (3 of 6) | FAIL |
| model-establishment | first job `route` | F only (38/48 = 79.2%) | FAIL |
| results | first job `route` | F 27/46 = 58.7%, A 2/9 = 22.2% | FAIL |
| results | first job `compute` | A 4/9 = 44.4% | FAIL |
| introduction | `ext:context` | F 25/47 = 53.2%, no other type | FAIL |
| assumptions | `route` | no type | FAIL |
| conclusion | `interpret` | no type | FAIL |
| data-preprocessing | `source` | F only | FAIL |
| future-improvements | `handoff` | no type | FAIL |
| memo | `route` | F only | FAIL |
| model-testing | `route` | F only | FAIL |
| notation | `define` | F only | FAIL |
| recommendation | `route` | F only | FAIL |
| sensitivity-analysis | `route` | F only | FAIL |
| strengths-limitations | `ext:claim` | no type | FAIL |

Only `model-establishment` (six types) and `results` (two types) can be posed
across types at all; the other eleven labels exist in F only in the read set.

`model-establishment`, first position:

| type | `route` | `define` |
|---|---|---|
| A | 31/84 (36.9%) | 32/84 (38.1%) |
| B | 9/24 (37.5%) | 8/24 (33.3%) |
| C | 2/5 (40.0%) | 1/5 (20.0%) |
| D | 0/5 (0.0%) | 4/5 (80.0%) |
| E | 2/5 (40.0%) | 3/5 (60.0%) |
| F | 38/48 (79.2%) | 6/48 (12.5%) |

The three samples large enough to test do not agree: A splits almost evenly between
`route` (36.9%) and `define` (38.1%) with no majority at all, B likewise (37.5% /
33.3%), while F opens with `route` (79.2%). D and E open with `define`
(80.0/60.0%), but on five papers. Counterexamples
with paper ids: `P-A-2010-6749-395f556a` opens `route, route, route` (a `define`
miss); `P-A-2018-88255-2023cf14` opens `define, derive, define` (a `route` miss);
`P-B-2016-48573-960f7126` opens `mechanism, derive, derive`; `P-C-2022-2200688-b6248fa6`
opens `compare, compare, compare`; `P-D-2015-38996-1efe10af` opens `compare, derive,
source`; `P-E-2016-52831-df9e4468` opens `route, define, interpret`;
`P-F-2016-43181-88427331` opens its model-establishment sections with `read-figure`
then `route`, and `route` then `mechanism+close:route`.

Types are not internally stable either. Exact-sequence agreement inside a type:
A/model-establishment 84 papers, modal sequence shared by 1 (1.2%), lengths 2–150;
F/model-establishment 48 papers, modal sequence shared by 1 (2.1%), lengths 13–128;
B/model-establishment 24 papers, modal share 1 (4.2%). The highest figure
anywhere is F/notation: 8 of 24 papers open with the same single job (33.3%). No type
agrees with itself on a full chapter, so no sequence can hold in 60% of it.

## Result 4 — the verbatim-sentence condition is met for F only

665 of the 672 F records carry a per-group opening and closing sentence in
`units[]` (6794 groups, 6794 units); the other 7 carry none, an open gap in this
lane. Example, `P-F-2016-46634-153dc78f`, model-establishment: `We consider the
influence factors of the movement of refugees from three aspects.` The A–E ledger
rows carry no quoted sentence at all — 0 of 132
A–E rows contain quotation marks of any kind — so no A–E pattern can satisfy "every
claim carries one verbatim sentence from a paper read in full" even if it passed the
share test. Promotion of any A–E rule is blocked on evidence, independently of
Result 3.

## Reproducibility

```bash
python -I -X utf8 lanes/L1-f-structure/tools/freeze_ledger.py
python -I -X utf8 lanes/L1-f-structure/tools/audit_merge.py
```

The first command refreezes `merge/snapshot/paragraph-ledger.jsonl` from
`artifacts/paragraph-ledger.jsonl`; the second writes `jobs-by-type.csv`,
`metrics.json`, `taxonomy-sha256.txt` and `blocked-papers.csv` in this directory and
prints the per-chapter verdict line. Skipping the first command measures whatever
snapshot happens to be on disk, which is how the numbers here drifted from the
ledger once already. Two consecutive `audit_merge.py` runs on the same frozen
snapshot produce byte-identical `metrics.json`
(`cba76375…117fcaf4`) and `jobs-by-type.csv` (`ac1bd01b…841ad73e`). Every number in this report is a field of `metrics.json`;
the counterexample papers are the `miss_example` values there, and the F sentences
are `units[].open` / `units[].close` in `jobs-f.jsonl`.

## What this does not support

- Any claim that a type has a characteristic model-establishment sequence; the three
  samples large enough to test (A 84, B 24, F 48) disagree at position 0.
- Any promotion verdict for chapters present in one type only — eleven of thirteen
  labels are F-only in the read set.
- A template reading of `paragraph_functions`: 98%+ distinct everywhere except B.
- A treatment of F's chapter labels as the corpus's own. F labels are normalised
  (lane README, "Merge contract"), so F shares are measured on a vocabulary the
  corpus does not use for A–E.
