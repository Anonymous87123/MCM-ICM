# L4 B lane — paragraph jobs for the 76 eligible type-B papers

Hand-coded, one paper at a time, same discipline as `lanes/L3-c-ledger`. No batch
classifier: `para_extract.py` measures line geometry, `dump_paper.py` writes the
reading list, `record.py` validates and assembles, `check.py` recounts. Every job
in `jobs-b.jsonl` is read off the page.

## Inputs (read only)

| path | use |
|---|---|
| `artifacts/corpus/manifest.jsonl` | queue: `eligible_paper` and `problem_type == "B"`, ordered by `(year, relative_path, file_name)` → `queue.txt` (76 of 99 B rows; 23 excluded by the corpus) |
| `artifacts/language-units/P-B-*.json` | `chapter_layouts` (chapter, printed pages, `paragraph_count`, `paragraph_functions`) |
| `artifacts/papers/P-B-*/text/pages/*.txt` | text layer, page map only |
| `artifacts/papers/P-B-*/rendered/*.png` | read through `scripts/make_review_proxy.py --max-bytes 450000`, one page per call, `detail: "high"`, only when a boundary or block kind is doubtful |
| `F:\MCM\MCM-ICM-master\<relative_path>` | the PDF, for `para_extract.py layout` |
| `artifacts/paragraph-ledger.jsonl` | frozen to `snapshot/paragraph-ledger.jsonl`, sha256 `1a9deff4…1f75b6e`, 177 rows, 21 of them B; the live file is never written from this lane and has since grown to 181 rows, so the snapshot is deliberately stale and the B rows it holds are the earlier pass's single-chapter samples |

## Writes (this lane only)

`queue.txt`, `README.md`, `layout/`, `records/`, `notes/`, `jobs-b.jsonl`,
`reports/`, `snapshot/`, `tools/`, `.proxy/`.

Forbidden: `artifacts/**`, `~/.claude/skills/**`, `tmp/para-taxonomy.md`, other lane
directories, other paper types (including the C lane's `jobs-c.jsonl` and the F
lane's `jobs-f.jsonl`).

## Method

1. **Queue.** `queue.txt` is manifest order; one paper is finished (layout,
   record, recount, note) before the next is opened.
2. **Measurement.** `python -I lanes/L4-b-ledger/tools/para_extract.py layout <pid>`
   rebuilds paragraph boundaries from PyMuPDF geometry: modal body size, modal left
   margin per column side, median line spacing, first-line indent > 6 pt, page-break
   continuation, and body fragments under 5 words folded into the previous block.
   Two-column pages are read as two streams, left column first.
3. **Reading.** `python -I lanes/L4-b-ledger/tools/dump_paper.py <pid>` writes
   `.proxy/<pid>-read.txt` with every measured block (number, kind, pages, words,
   first 380 and last 80 characters). Doubtful blocks are re-read from the rendered
   page.
4. **Coding.** One job per printed paragraph. A *group* is the list of measured
   block numbers that form one printed unit: a heading glued to its body, table rows,
   a merged bullet list, a torn display equation, a page-break split. Groups follow
   the printed page, not the measured count.
5. **Chapter labels.** Stored `chapter_layouts` names are kept verbatim. No renaming
   in this lane. Where a stored bucket has no printed section — a `title` sheet, a
   `problem-restatement` span that is really the contents page, a chapter covered by
   another record — the paper gets `records/<pid>.skipped.json`, one entry per stored
   chapter with the reason, and `check.py` prints it as declared rather than failing.
   Nothing is dropped silently: every skipped entry names either an exclusion class in
   `reports/coverage.json` or the record that already holds the text.
6. **Page numbering.** Printed page = file page − offset, stated per paper when the
   offset is not zero; `pages` in a record are file pages.
7. **Evidence.** Every group carries a verbatim opening and closing sentence
   (`units[].open` / `units[].close`) produced by `record.py` from the measured text.

## Scope decisions for B labels outside the fourteen-value vocabulary

The B corpus uses four stored labels that are not chapter functions. Decision, to be
applied consistently and quoted in each affected note:

- **`title` (25 stores)** — out of scope, same class as `abstract`, `references`,
  `appendix`. The title sheet is front matter, never a paragraph job, and is
  documented in the coverage report as `front-matter` rather than coded.
- **`limitations` (10 stores)** — kept verbatim, coded as its own chapter with the
  jobs the printed text actually performs. It is not merged into
  `strengths-limitations` in this lane, so stored counts stay comparable.
- **`strengths` (8 stores)** — same: kept verbatim and coded, not merged.
- **`error-analysis` (4 stores)** — same: kept verbatim and coded.

Two defects found in the stored layout while applying this ruling, both handled
without renaming:

- A `title` bucket that is not front matter. `P-B-2014-29696-84be6e3a` stores
  `title` at pages 3-6, and those pages carry the Sports Illustrated article draft,
  not a cover sheet. The bucket is coded under its stored name and its note says so;
  the exclusion above applies only where the bucket really is a title sheet.
  `P-B-2015-32879-2c587e51` is the second case, where the `title` bucket holds the
  contents page instead.
- A chapter whose text has no measured block of its own.
  `P-B-2014-29696-84be6e3a` stores `data-preprocessing` at pages 41-44, the appended
  factor-data tables, but those tables sit inside measured block 355 together with
  the reference list. Splitting a measured block is not allowed here, so the chapter
  is declared in `.skipped.json` and the shared block is counted once, as `reference`.

Where a paper stores `strengths` and `limitations` as separate buckets, the record
set keeps them separate and the note states that the paper prints them as two
sections. Any later merge to `strengths-limitations` belongs to the merge audit, not
to this lane.

Counts verified against the 76 queued papers' `chapter_layouts` (1,170 stored label
values in total): `title` 25, `limitations` 10, `strengths` 8, `error-analysis` 4,
which is exactly the four out-of-vocabulary labels named in the task. The decisions
above are the lane's 口径 ruling; per-paper application is recorded in
`records/<pid>.skipped.json` (title always out of scope) and in each record's note
(limitations, strengths, error-analysis kept under their stored names).

## Coverage discipline

`reports/coverage.json` is written by `check.py --coverage` and recomputes, per coded
paper: `dup` (a block in two groups), `extra` (a coded block the layout does not
contain), `miss` (an uncoded block inside the coded page range, classified as
`front-matter` / `contents` / `banner` / `reference` / `appendix` / `unexplained`),
and the assertion `len(units) == sum(group_count)`. `unexplained` must stay empty.

## Progress

| papers coded | papers queued | note |
|---|---|---|
| 62 | 76 | 62 papers, 876 chapter records, 8,296 groups, 14,905 blocks, 447,623 clean words, 62 notes. `P-B-2010-7273-e234c9a6` 8 records / 75 groups; `P-B-2010-7507-24d34e5d` 13/182; `P-B-2010-7947-b6007ae0` 14/106; `P-B-2010-8362-bd23db32` 13/90; `P-B-2010-8479-b934962b` 14/100; `P-B-2011-10496-de9286d6` 15/93; `P-B-2011-11759-ee4be862` 15/97; `P-B-2011-12114-03fd7440` 14/97; `P-B-2011-9440-95f0fa40` 14/112; `P-B-2012-13074-8fc549d2` 11/45; `P-B-2012-13955-a0e5e63c` 13/95; `P-B-2012-15171-ce229936` 11/90; `P-B-2012-15417-df1dd905` 12/67; `P-B-2012-15420-8b46b980` 13/110; `P-B-2012-15878-825774ea` 11/139; `P-B-2013-21185-c7f22f59` 13/152; `P-B-2014-26160-510e6a16` 14/126; `P-B-2014-26333-27e7d8ab` 15/313; `P-B-2014-26636-060c74b1` 17/158; `P-B-2014-28414-5bd5b982` 19/161; `P-B-2014-28875-728f6f07` 16/132; `P-B-2014-29696-84be6e3a` 13/139; `P-B-2014-30680-9f0c0d05` 12/96; `P-B-2015-32879-2c587e51` 18/160; `P-B-2015-36178-d0225ad0` 16/128; `P-B-2015-38720-26d38781` 15/229; `P-B-2015-39173-b8260835` 15/125; `P-B-2015-40612-8bcdc1a7` 16/210; `P-B-2016-42745-4dc9ed2b` 16/159; `P-B-2016-48573-960f7126` 17/150; `P-B-2016-52221-f8094e57` 15/143; `P-B-2017-56731-a60a9459` 15/161; `P-B-2017-68303-6c8a9ede` 15/150; `P-B-2017-69427-b04ae242` 18/179; `P-B-2017-70174-8bf62421` 16/110; `P-B-2017-70545-8e86fcfa` 14/140; `P-B-2018-73410-069a3764` 15/171; `P-B-2018-74316-1198d12d` 15/151; `P-B-2018-77238-4380ec81` 13/86; `P-B-2018-79002-238b850f` 12/80; `P-B-2018-91566-2607f7ec` 16/76; `P-B-2019-1908286-37248927` 15/125; `P-B-2019-1908904-8b5a9e33` 15/109; `P-B-2019-1915782-41065334` 15/102; `P-B-2019-1923964-678ee565` 18/119; `P-B-2019-1924588-bd69a632` 12/108; `P-B-2020-2007698-75afc422` 14/135; `P-B-2020-2010821-2af4f390` 17/127; `P-B-2020-2011873-0d3ec7b7` 14/106; `P-B-2020-2019696-961d6242` 14/135; `P-B-2020-2013836-4c773f05` 13/147; `P-B-2021-2102199-f3e89239` 12/163; `P-B-2021-2104673-da993d23` 12/120; `P-B-2021-2105363-52f891b1` 14/212; `P-B-2021-2116496-6a60d0e7` 13/178; `P-B-2021-2127300-7985ddca` 13/177; `P-B-2022-2200084-66b742a2` 11/147; `P-B-2022-2202748-102f6d4c` 12/178; `P-B-2022-2207864-75af6d15` 12/149; `P-B-2022-2211922-6aa59818` 15/120; `P-B-2022-2213970-3f0a69d2` 15/123; `P-B-2022-2228168-d50f161d` 13/133. Lane totals: dup 0, extra 0, unexplained 0, `len(units) == sum(group_count)` for every paper, `jobs-b.jsonl` byte-identical across two full rebuilds (`407736d7…dfccc1`, 876 lines) |

Order note: `P-B-2020-2019696-961d6242` is queue row 51 and was read before rows 49
and 50 (`P-B-2020-2011873-0d3ec7b7`, `P-B-2020-2013836-4c773f05`), which a peer
session had reported as open. Rows 49, 50 and 52-62 are now coded and row 63
is next in queue order; each record is independent, so
the ledger's per-paper rows are unaffected.

`P-B-2022-2228168-d50f161d` shows the wrinkle that decides the sign of a delta at the
level of the block: this paper's paragraphs are measured as long bodies, so a whole
seven-entry bibliography arrives as one block (`references`, -6) while its bulleted
sections arrive pre-fragmented and therefore split into more groups than the store counts
(`introduction` +1, `model-establishment` +2, `algorithm` +1, `memo` +1). The net is -2
and no chapter's sign is a judgement call: it follows from how the measurement cut the
page. Its `model-establishment` is the widest non-contiguous set yet, taking 4.1.1-4.1.5
(blocks 81-146), 5.1 (170-182) and 5.3 (194-201), because the store files constraint
subsections and upper-level models together regardless of section number.

`P-B-2022-2213970-3f0a69d2` splits its buckets the most ways of any paper so far:
`model-establishment` holds 5.1, 5.2.1, 6.1 *and* 6.3, `algorithm` holds 5.2.2, 6.4 *and*
7.2, `problem-analysis` holds 2.2 plus 6.2, and `model-improvement` holds 5.4 plus 7.1. Four
of the fifteen chapters therefore take blocks from two to four separate page ranges. The
store allocates by what a section is — a model, a solution method, an analysis — not by where
it prints, and its own unit excerpts settle which is which. The paper's net is -21, and it
is negative throughout except the memo: most chapters lose one to five units because the
page is measured as long paragraph blocks while the store counts the moves inside them,
the `appendix` loses three because a single Python listing is one group against four stored
units, and the `memo` gains one because that page sets both of its figures out of the text
flow, so they survive as their own groups.

`P-B-2022-2211922-6aa59818` carries the same span-bucket wrinkle as the paper below but
in the other direction: its stores pair sections that print far apart, so
`problem-analysis` holds 4.2 *and* 5.1, `results` holds 4.4, 5.3.2 *and* 6.3, and
`model-improvement` holds 5.2 *and* section 6. Two of those chapters therefore take
blocks from two separated page ranges, with `pages` left as the outer bounds as on
row 59. Its net is -40, the widest negative spread in the lane, and all of it comes
from the two places this lane cannot split: the `memo` magazine spread, whose
two-column text is captured as three blocks against twelve stored moves (-9), and the
`appendix`, whose three code listings and two data tables are five groups against
twenty-six stored moves (-15). The references bucket is coded rather than skipped,
because the paper prints it as section 9.1 inside the appendix and the measurement
still gives two usable blocks.

`P-B-2022-2207864-75af6d15` needed a different reading of its buckets. Its stores are
not one stored label per printed section: `data-preprocessing` holds section 4 *and*
5.2.1 Data processing, `algorithm` holds 5.2.3 *and* 6.2, `results` holds 5.3 *and*
7.3, and `model-improvement` holds 6.1 and 7.1-7.2. The allocation was read off the
page spans the store itself records for each bucket's units (its `units[].page`), not
guessed from the labels, which is why two buckets are non-contiguous. Its deltas run
negative (net -27) for the opposite reason to the paper above: its blocks are long, one
measured block carrying a whole printed paragraph that the store splits into several
moves. A measured block is never split, so the block count is the ceiling.

`P-B-2022-2202748-102f6d4c` is the lane's widest spread between stored and printed
counts so far: net +29 over twelve chapters, from +21 in `model-improvement` to -6 in
`sensitivity-analysis`. The cause is the text layer, not the coding. That paper is
measured almost line by line, and its stores count whole moves, so a bucket such as
6.1.1 prints fifteen paragraphs, each one group of two to seven measured blocks, where
the store gives a single number for the section. No group straddles a printed
paragraph and no measured block is split; the deltas are named per chapter in
`notes/P-B-2022-2202748-102f6d4c.md`.

The frozen ledger holds 21 B rows, one per paper, all `model-establishment`
(35 jobs in the largest). They are the earlier pass's single-chapter samples: this
lane re-lays-out and recounts those papers from the page, and `jobs-b.jsonl` is
authoritative for B, the live ledger is never written.

## Tools

| tool | what it does |
|---|---|
| `tools/build_queue.py` | rebuilds `queue.txt` from the manifest (76 of 99 B rows) |
| `tools/para_extract.py layout <pid>` | measures paragraph boundaries into `layout/<pid>.json` |
| `tools/ocr_layout.py layout <pid>` | same rules from `ocr-lines.jsonl` boxes, for papers with no PDF text layer |
| `tools/dump_paper.py <pid> [head] [tail] [lo] [hi]` | writes `.proxy/<pid>-read.txt` |
| `tools/record.py <pid>` | validates a paper's records, writes `jobs-b.jsonl` + `notes/<pid>.md` |
| `tools/check.py <pid>` | per-paper stored-count / evidence check + layout reproducibility |
| `tools/check.py --coverage` | writes `reports/coverage.json` (dup / extra / miss by class) |

Seven fixes to the copied C tools: the vacant-chapter path tested `p["page"]`, but the
layout key is `pages`; `--coverage` fixes a queue count that split tokens instead of
lines; a running head such as `Page 5 of 23` is now classified `banner` (it repeats
with a different page number, so the repeated-text rule never caught it); a
number glued to a capitalised endnote, as in `1English, Donald B.K.`, now counts as a
reference item so a numbered endnote list is not left `unexplained`; and an appendix
heading that stands alone at the tail of the last reference (`…/coaches/ Appendix`),
with no letter after it, now opens the appendix instead of letting the appendix pages
fall into the `reference` class. And a contents line that begins `Appendix: …` no longer
opens the appendix: in `P-B-2020-2007698-75afc422` the dotted contents page ends with
the entry `Appendix: Our Code` on a text layer that carries no leaders, and treating it
as the appendix heading swallowed that paper's whole reference list into the appendix
class. Appendix detection now skips blocks on a page already read as contents, which
leaves every earlier paper's tally unchanged. And the seventh fix is in the
reproducibility hash: `check.py` re-ran `para_extract.py` for every layout, which for
a scanned paper would overwrite the OCR measurement with a single block. It now reads
`extractor` from the layout and re-runs whichever tool wrote it, and older papers
still report an identical sha.

A paper with no PDF text layer is measured by `tools/ocr_layout.py` instead. The
corpus already carries RapidOCR line boxes at 200 dpi for it, so the tool applies the
same rules to the boxes converted to points: a body line is `0.75–1.12 ×` the modal
box height (a box carries ascender and descender, so the band is wider than a font
size band), a heading is `≥1.15 ×`, and a first line is indented when it starts past
the line above rather than past the page margin, because an inset bullet list clears
the margin on every line. The layout it writes names its extractor, and the `-read.txt`
dump, the hand coding and the recount are unchanged. Its measurement of
`P-B-2020-2013836-4c773f05` gives 6,750 words against 6,816 in the OCR text pages
(99%), and the OCR contents page there needs one more rule: the leaders that `TOC`
matches survive OCR as nothing, so `check.py --coverage` also reads a page as contents
when its short lines carry an ascending run of six section numbers. The rule runs only
for OCR layouts, so no PDF paper's tally moves. The leader regex matches periods and
ellipses only, so a contents table set in middle dots (U+00B7) is not read as contents:
`P-B-2021-2116496-6a60d0e7`'s contents page falls before the first body block and is
counted with the front matter, which the paper's note states.

One paper's stored buckets are not printed sections at all.
`P-B-2021-2105363-52f891b1` gives `model-establishment` nine disjoint subsections
(2.3, 3.1.1, 3.1.2, 3.2.1, 3.2.2, 3.2.3's SSA half, 4.2.1, 4.2.2, 5.1), `results`
five result subsections, `algorithm` the repeater listing plus 4.1.1, and
`model-improvement` 3.3 plus 5.2. The paper's own `language-units` `section` field
names which printed subsection each bucket holds, so the record set follows it: a
chapter's `groups` are ascending but not contiguous, its `pages` are the outer bounds
of its blocks, and each printed sentence is coded under exactly one bucket. That is
also why two chapters there carry large deltas (`model-establishment` +28,
`algorithm` +34); their notes name the stored subsections and the measured
separations. No stored label is renamed or merged.

Two measurement shapes in `P-B-2021-2127300-7985ddca` are worth naming because they
push a delta in the opposite direction. Page 22 of that paper is measured line by
line, so each printed strength or weakness bullet becomes one group of two to five
blocks and the bucket lands exactly on its stored five. Its symbol table is torn into
cell-sized blocks with no row boundary of its own, so the two stored units are read as
the table's two pages and the chapter is two groups over 34 blocks.

## Reproduction

```
cd mcm-skill-work
python -I -X utf8 lanes/L4-b-ledger/tools/para_extract.py layout <pid>
python -I -X utf8 lanes/L4-b-ledger/tools/dump_paper.py <pid>
python -I -X utf8 lanes/L4-b-ledger/tools/record.py <pid>
python -I -X utf8 lanes/L4-b-ledger/tools/check.py <pid>
```
