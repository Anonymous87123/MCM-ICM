# L2 D lane — paragraph jobs for the 55 type-D papers

Hand-coded, one paper at a time. No batch classification script: `para_extract.py`
only measures line geometry, `record.py` only validates and assembles, `check.py`
only recounts. Every job in `jobs-d.jsonl` was read off the page by a human pass.

## Inputs (read only)

| path | use |
|---|---|
| `artifacts/corpus/manifest.jsonl` | queue: `eligible_paper` and `problem_type == "D"`, ordered by `(year, relative_path, file_name)` → `queue.txt` (55) |
| `artifacts/language-units/P-D-*.json` | `chapter_layouts` (chapter, printed pages, `paragraph_count`, `paragraph_functions`) and `units` |
| `artifacts/papers/P-D-*/text/pages/*.txt` | text layer, used for the page map only |
| `artifacts/papers/P-D-*/rendered/*.png` | rendered page, read through `make_review_proxy.py --max-bytes 450000` when a block boundary is ambiguous |
| `artifacts/paragraph-ledger.jsonl` | frozen at `snapshot/paragraph-ledger.jsonl`, sha256 `1122e62ebcf2fc89f52567f881b141ba9b0fd5f1cbba5104d28c7735c87f4ef2`, 190 rows; the original is never written from this lane |

## Writes (this lane only)

`jobs-d.jsonl`, `notes/<pid>.md`, `layout/<pid>.json`, `records/<pid>.json`,
`furniture.json`, `reports/`, `snapshot/`, `tools/`, `queue.txt`, this file.

Forbidden: `artifacts/**`, `~/.claude/skills/**`, `~/.claude/skills/mcm-icm-master-skill/**`,
`tmp/para-taxonomy.md`, other lane directories, other paper types.

## Methods

1. **Queue.** `queue.txt` is the manifest order above. One paper is finished (record,
   recount, note) before the next is opened.
2. **Measurement.** `python -I lanes/L2-d-ledger/tools/para_extract.py layout <pid>`
   rebuilds paragraph boundaries from PyMuPDF geometry: modal body font size, left margin
   voted per page and per column from lines ≥25 chars at that size (falling back to the
   document margin), median line spacing, first-line indent > 6 pt, page-break
   continuation (a paragraph continues across a break unless the previous line closed a
   sentence with `.`/`!`/`?`/`:` and the next starts uppercase), and any body fragment
   under 5 words folded into the previous block. Rows that share a baseline within
   0.45×font size and are adjacent (overlap, or gap < 12 pt) are one visual line, never
   across the page gutter, and the pieces are ordered by baseline bucket then x0, so a
   superscript citation lands after the words it closes instead of in front of them.
   Nothing about jobs is automatic.
3. **Reading.** `python -I lanes/L2-d-ledger/tools/dump_paper.py <pid>` writes
   `.proxy/<pid>-read.txt` with every measured block (number, kind, pages, word count,
   first 380 and last 80 characters). The paper is read from that file, and any block
   whose boundary or kind is doubtful is re-read from the rendered page through
   `make_review_proxy.py --max-bytes 450000`, one image per call, `detail: "high"`.
4. **Coding.** One job per printed paragraph. A *group* is a list of measured block
   numbers that belong to one printed unit: a heading glued into a body tail, the rows
   of one table, a bullet list that tight leading merged into one block, a display
   equation torn into fragments, a page-break split. Groups always follow the printed
   page, never the measured count.
5. **Chapter labels.** The stored `chapter_layouts` names are kept verbatim so counts
   stay comparable (`abstract`, `introduction`, `problem-analysis`, `notation`,
   `assumptions`, `model-establishment`, `results`, `strengths-limitations`,
   `conclusion`, `future-improvements`, …). No renaming happens in this lane.
6. **Page numbering.** Printed page = file page − offset, stated per paper in the note
   when the offset is not zero. `pages` in a record are file pages, because the layout
   is indexed by file page.

## Job vocabulary

Thirteen jobs, plus `ext:` codes and a `+close:<job>` suffix:

| job | what the paragraph does |
|---|---|
| `route` | states where the paper is going, or points at a figure/table as the plan |
| `define` | fixes a term, a symbol, a decision matrix, a classification rule |
| `source` | brings in outside data, literature, or an established fact |
| `select` | chooses among data, alternatives, models, or parameters |
| `derive` | turns assumptions or theory into a formula, step by step |
| `compute` | substitutes numbers and reports the arithmetic |
| `read-figure` | walks a figure, table, or axis dump |
| `compare` | puts two models, materials, or results side by side |
| `check` | tests or verifies an outcome (sensitivity, robustness, validation) |
| `limit` | states an assumption, a weakness, or a bound |
| `mechanism` | explains why the result holds |
| `interpret` | reads meaning out of a number or a ranking |
| `handoff` | passes the conclusion to an outside actor (policy, future work) |

Out-of-table codes, used only when no job fits: `ext:context` (background that carries
no quantity and no citation) and `ext:claim` (a bare evaluative claim about the paper's
own work).

## Verification

`python -I lanes/L2-d-ledger/tools/check.py <pid> [<pid> ...]` reports, per chapter,
`group_count` against the stored `paragraph_count` with a `delta` flag, flags any group
whose `open` or `close` is empty, flags a stored chapter never coded, and re-runs
`para_extract.py` to confirm the layout hash is identical. A delta is allowed only when
the record's note states the cause. A paper that prints a numbered chapter the stored
layout never captured — P-D-2016-47876-968a1156 prints section 9, Conclusions, between
its strength table and its reference list — is coded under its printed name, and
`check.py` accepts the missing stored count only when the note says the chapter is not in
the stored layout.

`python -I lanes/L2-d-ledger/tools/verify_quotes.py <pid> [<pid> ...]` tests the lane's
promise that every job carries a verbatim original sentence: each unit's `open` must be
a substring of `artifacts/papers/<pid>/text/full.txt` after dropping ligature codepoints,
the running page header (`Team # 35780 Page 16 of 22`, which the text layer splices into
paragraphs that cross a page break) and all whitespace. Word order and punctuation still
have to match, so a block whose span order was scrambled fails instead of passing.

`open` and `close` are read off the group's first and last block only, never off the
joined group text, so a display equation in a later block cannot be spliced into the
opening quote. A table has no prose sentence to open with, and its cells reach the text
layer in column order while the layout measures them in row order; such a unit may name
its opening line explicitly in the record as `"quotes": {"<first block>": "<caption>"}`,
and `verify_quotes.py` checks that caption like any other quote.

A running head that the text layer dropped in without its page number survives the
`PAGE_FURNITURE` pattern; those strings are named per paper under `heads` in
`furniture.json` and removed before folding, so the removal is visible in the lane
instead of hidden in the tool. The pattern takes the `#` of `Team # 55295 Page 5 of 20`
as optional, because some papers print the team number without it. `furniture.json` also
has a `drop_chars` section naming codepoints that carry no prose for one paper and that
PyMuPDF emits in a different order on the page than in `full.txt` — P-D-2016-44173-aa1c9913
maps its comma-space to a caron-plus-letter run, so the two carons are dropped and the
word order decides. P-D-2017-56632-67f41f43 needs two kinds: it prints `.=` where
`full.txt` sets `=.` in its variable definitions, so the equals sign is dropped; and its
text layer loses the ﬀ, ﬃ and ﬄ ligatures outright, leaving `di cult` where the page sets
"difficult", so those three codepoints are dropped on both sides. Dropping runs before
the ﬀ→ff mapping, because otherwise the dropped ligature would have been spelled out
first and the gap in `full.txt` would never line up.

P-D-2017-67316-f37f83c8 hands out every math-italic character twice inside a block
(`\U0001d706\U0001d706` for one lambda), and `full.txt` copies the doubling, so a unit whose
opening clause runs into a formula can never match; such units quote the heading, caption
or prose clause that opens them, listed per paper in the record's `quotes`.

P-D-2018-73156-1a30e830 keeps its mathematics in Symbol-font private-use codepoints
(`` for `=`, `` for `×`, `` for `Σ`) and sets many formulas inline, so the
layout reads the formula first where `full.txt` leaves it after the words; nine units
quote the prose clause that opens them for that reason.

P-D-2018-78826-ed3ee7b7 carries a bookstore advertisement ("精品数模资料，各类比赛优秀论文…") spliced
mid-sentence into many paragraphs in both the measured text and `full.txt`, so a unit whose
opening clause runs into the splice cannot match; three units quote the prose clause, caption
or sub-head that opens them for that reason.

P-D-2018-80386-b757100d sets its symbol names in Symbol-font private-use codepoints and
mixes prose into display formulas, so a paragraph whose opening runs straight into a formula
(`Finally, we can get the regional difference coefficient: (x1, x2), i = 1, 2, 3 … n (5.3.1)`)
reaches the layout in a different order than in `full.txt`; eight units quote the prose clause,
heading or caption that opens them. It also repeats the same bookstore advertisement as paper 16,
spliced into nine paragraphs.

P-D-2018-81402-e1ca1921 sets its optimisation model as one display block of an objective plus
seven numbered constraints, and the measured layout splits it into six fragments with no prose
in five of them, so the block is coded as one unit quoting the sentence that introduces it; its
figures and tables put captions under an advertisement splice, so four units name a caption, and
one table's cell order differs from `full.txt`, so the unit quotes the prose that opens it.

P-D-2018-82504-6cc63169 prints its whole summary as one 478-word block with no sentence break
on a paragraph boundary, so the abstract is a single unit against a stored count of two; ten more
units quote a table header, figure caption or prose clause because their cells reach `full.txt`
in column order while the layout measures them in row order, or because a bookstore advertisement
sits inside the sentence.

P-D-2018-82794-47f05792 prints three numbered sections that the stored ten chapters never captured —
1.3 Illustration, 2 Notations and 8 Comment on Heavy Trucks — so each is coded under its printed name
with the absence named in the note. Two printed units mix a displayed formula with the prose that
carries it, and each is coded as one group: the complete-graph sentence with display (10) and its
`where` line, which the text layer interleaves with the formula itself, and the threshold paragraph
with display (18), which has no prose of its own. Seven units quote the clause, caption or table
header that opens them, because the formula fragment or the column header reaches the layout ahead
of the words, and Table 4's rows reach `full.txt` with the row label under the header line rather
than in front of it.

P-D-2019-1900007-65267201 prints three sections the stored ten chapters never captured — 1.3 Our work,
2.2 Notation and the References list — so each is coded under its printed name with the absence named
in the note. Its notation table floats to the head of section 3.1, so the 2.2 chapter carries only the
lead sentence and the table is coded where it is printed, inside the modelling chapter. Five displays
and tables are coded with the prose or caption that carries them because their fragments reach the
layout ahead of the words: (1) to (3) with the junction-point paragraph, the piecewise (6) with the
sentence that announces it, (8) with the MATLAB route lengths, and Tables 3 and 4 with their captions.
Six units quote the clause or caption that opens them, four of them because a subscripted symbol
(`α(s) exit`, `N (i) mesh`) lands in a different order in the layout than in `full.txt`. The section
3.8 sensitivity analysis is printed before section 4 but stored as its own chapter, so the results
chapter covers 3.6 to 3.7 and then section 4, skipping the sensitivity blocks that sit between them.

P-D-2019-1902407-b8153b5d numbers its model section VI while its subsections print 4.1 to 4.7, and both the numeral
and the numbers are kept verbatim where they are printed. Its nine equations (4-1) to (4-9) carry no prose of their
own, so they are coded with the phase-division paragraph that introduces them and that group jumps the three figure
captions the layout prints between the prose and the display; those captions stay a unit of their own. The section
6.3 test of blocked areas and its ranking are stored under one function, ranked-impact, so the test and its conclusion
are coded in the sensitivity chapter while 6.1, 6.2 and 6.4 stay in the model-improvement chapter, and the 6.3 heads,
which sit in the tail of the block that closes 6.2.1, stay with that block by the glued-head rule. Twelve units quote
the clause or caption that opens them because a math-italic run reaches the layout in a different place than in
`full.txt`; for the subscripted symbols (R_x^w, V1,s, T5K) and the disaster factor the ordering differs inside the
symbol itself, and one sentence naming N_X and its destination is torn after `T1NX` and coded as one group.

P-D-2019-1908810-3e19ea18 splits its material across stored labels that do not follow its printed sections: the
results chapter holds the personnel timing of 4.4.2 and the simulation results of 6.3 with the 6.1 and 6.2 blocks
between them coded in the sensitivity chapter, and the algorithm chapter holds Algorithms 1, 2 and 3 from sections
3.5, 4.3 and 6.1, so both records are non-contiguous in block numbers and say so in the note. A pseudo-code body has
no prose sentence to open with, so those units quote the printed algorithm head. Its matrix display reaches
`full.txt` as bracket glyphs (``, ``) with the cell labels interleaved, which cannot be quoted at all, so
the unit quotes the prose clause that introduces it. One quote uses the curly apostrophe of the text layer
(`It’s`) rather than the ASCII one the page suggests; folding forgives whitespace, ligatures and the running head,
not punctuation.

P-D-2019-1922074-a699b77f is the first D paper whose printed order collides with a stored label
at a section boundary rather than inside a prose run: its 30 stored model-establishment functions
are one per model move, not one per printed paragraph, so the record merges printed displays,
symbol runs and torn sentences into 30 units over 99 blocks, and three of its stored chapters are
non-contiguous, results over blocks 129-133, 154-170 and 192-200, conclusion over 207-225 and 245,
and algorithm over 142-143 alone inside the personnel subsection. Five units open on a clause
instead of a first sentence because the layout breaks before the words: 86 after the chain
thickness, 110 after `the 2nd floor is`, 122 after equation number (13), 136 before the graph
symbol run, and 240 before a bullet glyph the layout drops into the middle of `used for the •
evacuation planning`. Blocks 254-309 are two xls-writing Python programs and are not coded.

D-lane stored layouts do carry page spans, under `page_start`/`page_end`, and all 558 chapters in
the 55 `artifacts/language-units/P-D-*.json` files have non-empty ones. They are printed pages
(PDF page minus two in this paper: section 1 prints on `p3` and is stored at 1) but they are not a
partition: the spans overlap where one printed section is coded in two stored chapters, so
model-establishment 3-17, algorithm 11-11 and results 10-16 all cover printed 11, and the
conclusion span 17-20 reaches across the portability and sensitivity sections to its recap. A
chapter's extent therefore still comes from its printed section and its span is read only as a
cross-check, which is why the results chapter can carry blocks from printed 10, 14, 15 and 17
while skipping the model blocks between them.

P-D-2019-1922748-25e53f6c is the first paper in this lane whose stored function list double-counts
a printed paragraph. The 9.3.2 nontermination paragraph is printed once, at block 159, and the
stored layout names it both as the fourth function of strengths-limitations and as the first of
conclusion, so the strengths chapter records three units against a stored four and the delta is
stated in the note rather than repaired by splitting or reusing a block. Two more shapes are worth
naming: the stored conclusion names nodes under 9.3.2 and the paper prints no conclusion head at
all, so the chapter is keyed to the section it actually sits in; and 12 of 12 stored counts
otherwise matched, which is the first exact run since paper 24. The introduction is non-contiguous
because the stored problem-analysis chapter owns 1.2, so the record codes 1.1 at block 19 and 1.3
at blocks 32-34 and says so. Figure 14's caption is printed between the two halves of the section 8
list, so it rides with the list while the margin reading itself stays in the results chapter at
block 147. Six units quote a clause instead of a first sentence: 34 a caption with a section head
glued to it, 35 an assumption list hyphenated across a line break, 36 symbol rows that reach the
layout a cell at a time, 44 a block opening on the equation number (1), 50 a sentence whose
derivative is split across the layout, and 95 a block opening on the matrix sum. Blocks 1-4 are the
team sheet, year line, title and the bare 'Summary' head, blocks 11-18 are the keyword line and the
table of contents, and blocks 183-195 are the appendix figures and four MATLAB programs; none is
coded.

Paper 26 (P-D-2020-2002526-23eb8c8d, 2020 ICM football team performance) shifts the mismatch
from the span to the count itself. Its stored function list is itemised per bullet, while the
geometry layout measures each bullet run as one block: the four 1.2 task bullets sit inside a
single block, the four assumptions in another, and the two preprocessing decisions in a third, so
introduction carries 3 units against 7, assumptions 1 against 4 and data-preprocessing 1 against
2, three deltas that no re-cutting of group boundaries could close. Two further deltas come from
the same layout granularity seen from the other side: the coefficient sentence and its physical
translation are one printed paragraph counted twice (memo −1), and the conclusion's thesis
sentence is torn by the page break after 'Increase the relative frequency' with the watermark
between the halves (conclusion −1). The paper also shows a section head that the text layer
delivers inside a watermark display rather than as a heading block: '5. Evaluation and Promotion
of Model' opens the strengths chapter through that display, which is why that unit quotes the
head itself. Printed page equals PDF page for this paper, unlike the 2019 papers' minus two.

Paper 27 (P-D-2020-2003723-28f692ff, 2020 ICM football teaming strategies) exposes a new
stored-layout defect: five of its ten function lists are padded with literal placeholders, the
entries read 'continuation paragraph 1' through 'continuation paragraph 10', and the counts those
placeholders fill, model-establishment 18, model-improvement 16, results 10, future-improvements
16, strengths-limitations 6 and conclusion 6, are therefore counts of a template rather than of the
printed paper. The same layout drops chapter 6 whole: its ten chapters jump from 5.5.3 to chapter
7, so 'Structural Strategy Analysis and Suggestions' with its 24 printed units and the whole 5.1
individual-contribution sub-model carry no stored count. The record keeps the stored names where
they exist, codes the printed units where they do not, and states both directions of delta, +20 for
model-improvement and -3 for results, rather than letting one cancel the other.

Paper 28 (P-D-2020-2006782-8d6d48b4, 2020 ICM teaming wisdom) repeats the paper-25 defect in a
larger form and adds a layout shape of its own. Its stored layout lists the same eight TASK 4
paragraphs twice, once as the tail of the results chapter and once as the whole conclusion
chapter, so a paper that prints no conclusion section at all is still charged with eight
conclusion functions; they are coded once, under conclusion, and the results delta is stated
against the printed chapter 5 instead. The same paper's text layer breaks every chapter into
printed lines rather than paragraphs, so its twenty-five stored model functions are carried by
sixty-two measured blocks and its twenty stored evaluation functions by fifty-six; the record
follows the stored functions, not the line count, and says so in each note.

Paper 29 (P-D-2020-2013140-d02fd0c3, 2020 ICM passing-network and team-performance model) counts
in the opposite direction from most of the lane and names a chapter after a heading it never
prints. Its paragraph_functions are topic-level, one function per subsection chunk rather than per
printed paragraph: model-establishment's twenty-two functions cover forty-four body paragraphs
('BPBC tactic description and coordinate inequality' alone is four of them) and
model-improvement's eighteen cover thirty-nine, so both chapters code per printed paragraph and
carry the upward delta, +17 and +7. The chapter stored as conclusion has pages 17-19 and five
functions that are exactly the five units of printed chapter 4, Generalization and Expansion of
the Model; the paper prints no Conclusion heading anywhere, and its actual closing remarks are the
5.2 disadvantages paragraph coded under strengths-limitations. The stored count still matches at
5, so unlike paper 28 the defect shows only in the name, not in the number; the note states this
rather than renaming the stored chapter. The same paper's weight chain is also the first in this
lane whose appendix holds the only reproducible part, the three AHP matrices and their MATLAB
programs, printed after the references with no stored chapter, so the appendix is coded as a
chapter of its own with the not-in-the-stored-layout marker.

Paper 30 (P-D-2020-2013245-e4e7ae08, 2020 ICM cooperation structure and sliding window) is the
first paper in this lane whose stored counts collapse printed units instead of splitting them, and
it does so twice. The assumptions chapter is stored as a single unit, 'four bullet assumptions',
where the text prints four bullets and tears the first across two blocks, so the record carries +3
on a chapter whose stored count is 1; the appendix is stored as one unit, 'Python code for
sliding window network analysis', where the text prints a ten-page listing in six sections, so
that chapter carries +5. Both are the mirror image of paper 26, where stored counts itemised
bullets the layout measures as one block, and both are resolved the same way: code the printed
units, state the direction of the delta. The same paper repeats the paper-29 naming defect in a
cleaner form, a stored chapter called conclusion whose printed heading is numbered chapter 6, 'how
to design more effective teams', with no Conclusion heading anywhere; its stored two functions
cover only two of the five printed units, so the delta is +3 and the stored name is kept. The
introduction is the one place the lane has had to code downward here without a stored defect: four
problem statements and an 'extra information' sentence are printed inside a single 395-word
paragraph, so six printed units stand against eight stored ones.

Paper 31 (P-D-2020-2015044-db9655c7, 2020 ICM passing networks and Markov chain) is the first
paper in this lane whose stored chapter functions name material the chapter does not contain. The
introduction is stored with three functions, the middle one reading 'six-assumption roadmap',
although the six assumptions are printed in chapter 2 and the introduction holds a background
paragraph plus four lettered task statements; the assumptions chapter in turn keeps only three of
those six bullets, dropping (b), (e) and (f) without a trace. The record codes the printed units on
both sides and states +2 and +4 rather than reconciling the pair. The stored results chapter has
the same absorption shape as paper 30's appendix in reverse: it carries eight functions over pages
8-15, two of which, per-coach advice and home-away split, are printed as a separate numbered
chapter 5 that the layout never lists, so that chapter is coded on its own with the not-in-the
marker and its delta is stated against results. Two smaller defects: the sensitivity chapter is
stored as its own chapter although it prints as subsection 4.4.3 of chapter 4, and the eleven-entry
bibliography is stored as one unit, 'methods citation', so the reference chapter carries +10 for
the same reason paper 30's appendix carries +5.

Two C-lane conventions carry over unchanged:

- A stored label outside the thirteen-job vocabulary is kept verbatim in the record
  `note` and mapped to the closest job after the fact; the stored name is never renamed.
- A chapter whose text layer is empty (raster pages) is recorded as a vacated chapter
  with `vacant_units` and `vacant_reason` instead of invented blocks.

## Progress

| # | paper | chapters | groups | deltas | status |
|---|---|---|---|---|---|
| 1 | P-D-2015-34985-c7be0d8b | 11/11 | 35 | abstract −2, problem-restatement −1, introduction −1, assumptions +3, results −1, conclusion −1 | done |
| 2 | P-D-2015-35780-97fea85b | 11/11 | 40 | introduction −2 | done |
| 3 | P-D-2015-38727-eeb1090f | 6/6 | 30 | model-establishment +3, results +1 | done |
| 4 | P-D-2015-38996-1efe10af | 7/7 | 31 | abstract −2, introduction +5, assumptions +3, model-establishment +2, strengths-limitations +1 | done |
| 5 | P-D-2016-42220-7261f9d3 | 7/7 | 25 | abstract +1, introduction +1, model-establishment +1, strengths-limitations +1 | done |
| 6 | P-D-2016-44173-aa1c9913 | 7/7 | 21 | abstract +2, introduction +1, assumptions +1, results −2 | done |
| 7 | P-D-2016-47876-968a1156 | 8/7 | 24 | abstract +2, model-establishment +1, results +2, conclusion not stored | done |
| 8 | P-D-2016-49436-4c3ef010 | 7/7 | 27 | abstract −2, introduction +2, assumptions +2, model-establishment +4, results +4, strengths-limitations +1 | done |
| 9 | P-D-2016-54740-539566f6 | 9/8 | 29 | abstract +1, data-preprocessing +2, model-establishment +4, results +4, conclusion not stored | done |
| 10 | P-D-2017-55285-1835cc0b | 10/9 | 31 | abstract +2, problem-restatement +3, model-establishment +3, results +3, model-improvement +2, sensitivity-analysis +2, references not stored | done |
| 11 | P-D-2017-55295-9001b6d9 | 9/7 | 89 | abstract +3, introduction +1, model-establishment +20, results +14, model-improvement +23, sensitivity-analysis +13, strengths-limitations +2, conclusion and references not stored | done |
| 12 | P-D-2017-56632-67f41f43 | 10/7 | 72 | introduction +1, model-establishment +27, algorithm +3, results +20, model-improvement +4, future-improvements, conclusion and references not stored | done |
| 13 | P-D-2017-67316-f37f83c8 | 13/10 | 100 | abstract −1, introduction +6, assumptions +1, model-establishment +25, results +12, model-improvement +20, sensitivity-analysis +1, memo +8, strengths-limitations +2, cultural-analysis, conclusion and future-improvements not stored | done |
| 14 | P-D-2017-68942-f0b0893e | 12/12 | 99 | abstract vacated (−2, empty text layer), introduction +6, assumptions +19, data-preprocessing +1, notation +13, model-establishment +7, results +9, model-improvement +18, sensitivity-analysis +8, memo +4, strengths-limitations +1 | done |
| 15 | P-D-2018-73156-1a30e830 | 10/10 | 153 | abstract +4, introduction +5, problem-restatement +4, assumptions +3, model-establishment +90, results +18, sensitivity-analysis +3, strengths-limitations +7, memo +3 | done |
| 16 | P-D-2018-78826-ed3ee7b7 | 10/10 | 89 | abstract +5, introduction +2, problem-restatement +5, assumptions +1, model-establishment +22, results +26, model-improvement +7, strengths-limitations +4, memo +3 | done |
| 17 | P-D-2018-80386-b757100d | 11/10 | 122 | abstract +4, introduction +1, problem-restatement +5, model-establishment +58, sensitivity-analysis +6, strengths-limitations +7, memo +7, model-improvement not in the stored layout | done |
| 18 | P-D-2018-81402-e1ca1921 | 12/11 | 141 | abstract +3, introduction +2, problem-restatement +10, assumptions +2, model-establishment +41, data-preprocessing +6, results +32, sensitivity-analysis +12, memo +12, model-improvement not in the stored layout | done |
| 19 | P-D-2018-82504-6cc63169 | 13/11 | 134 | abstract −1, introduction +5, problem-restatement +1, assumptions +2, model-establishment +26, results +43, model-improvement +11, sensitivity-analysis +7, strengths-limitations +6, memo +8, notation and technology-impact not in the stored layout | done |
| 20 | P-D-2018-82794-47f05792 | 13/10 | 164 | abstract +4, introduction +1, problem-restatement +6, assumptions +2, model-establishment +69, results +51, sensitivity-analysis +2, strengths-limitations +3, memo +4, illustration, notation and heavy-trucks not in the stored layout | done |
| 21 | P-D-2019-1900007-65267201 | 13/10 | 120 | abstract +2, introduction +4, problem-restatement +1, assumptions +9, model-establishment +43, results +19, sensitivity-analysis +5, strengths-limitations +7, memo +5, our-work, notation and references not in the stored layout | done |
| 22 | P-D-2019-1902407-b8153b5d | 13/11 | 122 | abstract −1, assumptions +1, model-establishment +30, data-preprocessing +5, results +10, sensitivity-analysis +5, model-improvement +32, strengths-limitations +5, memo +17, notation and references not in the stored layout | done |
| 23 | P-D-2019-1908810-3e19ea18 | 12/12 | 114 | abstract −4, notation +7, model-establishment +44, algorithm +1, results +2, sensitivity-robustness +4, strengths-limitations −1, conclusion +4 | done |
| 24 | P-D-2019-1922074-a699b77f | 12/12 | 70 | none — all twelve stored counts matched exactly | done |
| 25 | P-D-2019-1922748-25e53f6c | 12/12 | 57 | strengths-limitations −1 (the nontermination paragraph is printed once and stored under both strengths and conclusion) | done |
| 26 | P-D-2020-2002526-23eb8c8d | 13/12 | 89 | introduction −4, assumptions −3, data-preprocessing −1 (stored counts itemise bullets that the layout measures inside one block), memo −1, conclusion −1; references not in the stored layout | done |
| 27 | P-D-2020-2003723-28f692ff | 12/10 | 135 | abstract +2, introduction +6, model-improvement +20 (stored list padded with 'continuation paragraph' placeholders and stops at 5.2), results −3, future-improvements +1, strengths-limitations −1, conclusion −3; recommendations and references not in the stored layout | done |
| 28 | P-D-2020-2006782-8d6d48b4 | 11/11 | 120 | introduction +5, assumptions −1, conclusion +5 (TASK 4 printed once, stored under both results and conclusion), sensitivity-analysis +1, strengths-limitations −2 | done |
| 29 | P-D-2020-2013140-d02fd0c3 | 12/11 | 139 | introduction +4, assumptions +1, model-establishment +17, model-improvement +7 (stored functions are topic-level, one per subsection chunk, not per printed paragraph), results +1; appendix not in the stored layout; stored 'conclusion' is printed chapter 4 Generalization | done |
| 30 | P-D-2020-2013245-e4e7ae08 | 10/10 | 69 | introduction −2 (four problem statements and the extra-information sentence print inside one 395-word paragraph), assumptions +3 and appendix +5 (stored counts collapse a four-bullet list and a ten-page code listing into one unit each), model-establishment +9, results +5, conclusion +3 (stored 'conclusion' is printed chapter 6, how to design more effective teams), strengths-limitations +2 | done |
| 31 | P-D-2020-2015044-db9655c7 | 10/9 | 78 | introduction +2 (stored middle function names the six assumptions, which print in chapter 2), assumptions +4 (stored keeps three of the six bullets), model-establishment +5, results +10, sensitivity-analysis +2 (stored as its own chapter but printed as subsection 4.4.3), references +10 (eleven entries stored as one unit); printed chapter 5 advice not in the stored layout, its two functions absorbed by results | done |
