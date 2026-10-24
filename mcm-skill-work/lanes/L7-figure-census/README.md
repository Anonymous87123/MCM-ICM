# L7 — figure census lane (what was actually drawn, all 435 papers)

Hand-pass census, one paper at a time. `fig_extract.py` only measures page geometry
(image blocks plus vector drawing clusters). It never decides a family. `record.py`
only validates the vocabulary and assembles. `check.py` only recounts. Every family
label in `records/` was read off a cropped proxy by a human pass.

The question this lane answers: **what charts are actually drawn in these papers**,
not what the captions say. Caption vocabulary already exists elsewhere and must not be
cited for the drawing (`references/visualization-core.md`: "no chart type" 0.65–0.77
by problem type, bar 0.00 everywhere, explicit limit "caption vocabulary, not chart
usage").

## Hard boundaries

Writes stay inside this directory:

`queue.txt`, `tools/`, `layout/`, `records/`, `notes/`, `reports/`, `snapshot/`,
`.proxy/`, this file.

Never written from here:

- `artifacts/**` (owned by the root session; `paragraph-ledger.jsonl` is single-writer)
- `~/.claude/skills/**`, `tmp/para-taxonomy.md`
- any other lane directory
- any source PDF under `F:\MCM\MCM-ICM-master`

## Inputs (read only)

| path | use |
|---|---|
| `artifacts/corpus/manifest.jsonl` | queue: `eligible_paper == true`, ordered `(year, relative_path, file_name)` → `queue.txt`, 435 rows |
| `artifacts/papers/<pid>/rendered/page-NNNN.png` | the authoritative raster for crops, 433 papers / 11,204 pages |
| `artifacts/papers/<pid>/text/pages/page-NNNN.txt` | text layer, caption candidate text only |
| `artifacts/papers/<pid>/extraction.json` | page status flags (empty text layer, partial text) |
| `mcm-skill-work/scripts/make_review_proxy.py` | crop proxy at `--max-bytes 450000`, one image per call, `detail: "high"` |

The three papers with no text layer are not skipped: they still have rendered pages and
the census is visual. Where they have no text, caption text is typed from the crop into
`caption_verbatim` and marked `caption_source: "typed-from-crop"`.

## Vocabulary (closed at lane start — 14 families, plus one table code)

    line  scatter  bar  histogram  box-or-violin  heatmap-or-contour
    surface-or-3D  node-link-network  flowchart-or-schematic  map-or-plan-view
    photo-or-raster-image  table-as-figure  composite-panel  other

Plus `table-grid`, used only for printed tables, recorded in a separate list from
figure items so the two distributions never mix.

Rules:

- No family is added mid-lane. A chart that fits nothing goes to `other` with a
  one-line `other_note`. If `other` exceeds 10% of a type, the census reports that
  as a finding, it does not widen the vocabulary retroactively.
- `composite-panel` means one exhibit holding ≥2 sub-plots of different families, or
  sub-plots whose family cannot be named from the crop. Multi-panel exhibits of the
  *same* family keep that family and carry `panel_count ≥ 2`; they are not
  `composite-panel`.
- A table printed as a grid uses `table-grid` even when it is numbered as a figure.
  A table rendered as an image goes to `table-as-figure`.

## Method, one paper at a time

1. **Geometry.** `python -I lanes/L7-figure-census/tools/fig_extract.py layout <pid>`
   opens the PDF with PyMuPDF and builds candidate exhibit regions from two sources:
   image blocks (`page.get_image_info`) and vector drawing clusters (`page.get_drawings`,
   union-find on bbox proximity). Region filters: minimum area and minimum side,
   header/footer band exclusion, full-page-background exclusion. Every region carries
   `page`, `bbox`, `area_frac`, `raster|vector|mixed`, `aspect`, `path_count`, and the
   nearest text line below (then above) as `caption_candidate`. Output:
   `layout/<pid>.json`.
   Fusion matters: these papers draw charts as vector paths, so an image-block-only
   pass under-counts exactly the charts the census wants. A single plot also shatters
   into hundreds of paths, so the cluster threshold is per-paper and checked by eye on
   the first papers, not fixed globally.
   Two extractor defects were found by peers on papers outside this range and are
   fixed here, with a regression run over every layout on disk before the fix was
   released. (a) A paper that paints a white, stroke-free rectangle over the whole page
   put that rectangle into the path list, where it chained every other path into one
   full-page cluster and the full-page-area guard discarded the page — losing every
   figure on it (paper 122 measured 4 regions against 13 printed figures).
   `is_page_background` now drops such a rectangle before clustering. (b) The heading
   index capped numbered titles at eight words, which silently dropped long but real
   headings such as "6.2 Sensitivity with Respect to Number of Self Driving Cars"
   (paper 123); titles up to twelve words are now accepted when they are set in title
   case and do not break off on a comma, a hyphen or a page number.
2. **Reading.** `python -I lanes/L7-figure-census/tools/dump_paper.py <pid>` writes
   `.proxy/<pid>-read.txt`: regions in reading order with page, kind, bbox, area,
   caption candidate, and the text lines around the region. The paper is read from
   that file; every region whose boundary or identity is doubtful is re-read from the
   render.
3. **Cropping.** One region per call:
   `python -I ../scripts/make_review_proxy.py --input artifacts/papers/<pid>/rendered/page-NNNN.png --output lanes/L7-figure-census/.proxy/<pid>-p<N>-r<k>.jpg --crop L T R B --max-bytes 450000`
   then one Read at `detail: "high"`. Never a full page at `detail: "original"`,
   never two images in one call.
4. **Classify and record.** `tools/record.py <pid>` validates the family vocabulary,
   requires a verbatim caption or an explicit `caption_source`, requires `confidence`
   and `panel_count`, and appends `records/<pid>.json` plus `notes/<pid>.md`.
   Job: one family per printed exhibit. Where the family is genuinely not decidable
   from the page, it is recorded as `other` with `other_note` naming what was seen —
   never guessed.
5. **Recount.** `python -I lanes/L7-figure-census/tools/check.py <pid>` re-runs the
   geometry and confirms the layout hash is identical, then reports region count
   against recorded items, and flags any recorded item with no bbox on the page.

## Rule changes, each bought by looking at a page

**Rule change 1 — bbox from item geometry, not `drawing["rect"]`.** A plot frame drawn
as four lines has zero height on its horizontal edges, and PyMuPDF reports a degenerate
rect as empty, so a frame-only filter dropped every ruled plot frame. Found on
P-A-2010-6749 page 19: `get_drawings` returned 121 items, only 7 usable boxes, and the
Figure 7 frame vanished. `draw_bounds()` now unions the item points (`l`, `re`, `qu`, `c`).
Effect on that paper: 40 → 46 candidate regions before the rules below.

**Rule change 2 — containment, not overlap, when fusing images.** The first fusion test
dropped any path cluster that merely overlapped an image block. Figures 18, 28 and 26 all
hold a pasted screenshot *inside* their plot area, so the whole figure was deleted and
only the screenshot survived. Now a path cluster is dropped only when an image block
contains it. Effect: the missing Figure 18 frame reappeared on page 27.

**Rule change 3 — a thin vector wrapper around one image is that image's frame.** When a
path cluster has ≤20 paths and one image covers ≥80% of its area, the cluster is the
frame and is dropped, keeping the image. Pages 11 and 40 needed this; without it every
framed pasted scan counted twice.

**Rule change 4 — an image that a path cluster traces to within 4 pt is the same exhibit.**
The image copy is dropped, the traced region kept.

**Rule change 5 — shaded caption boxes are not exhibits.** A region with ≤4 paths whose
inside text starts `Figure N`/`Table N` is a caption background (page 33 of the same
paper). Dropped before counting, not counted as `other`.

**Rule change 6 — Booktabs tables are horizontal rules only.** P-A-2010-7571 prints every
table three-line style: a 3.6 pt cluster per rule, no vertical strokes. The rule filter
(`h < RULE_HEIGHT_PT` and `w > 0.8 page_w`) deleted each one, so the paper recorded
`tables = 0` while printing Tables 1–14. Two or more page-wide neutral rules stacked within
`TABLE_GAP_PT` are now one table, and their clusters are consumed. Effect: 21 → 38 regions,
21 → 21 figures plus 17 table regions on that paper. Paper 1 has no booktabs table and its
44 regions did not move.

**Rule change 6a — the rules of one table share both ends.** First cut grabbed each page's
running-header underline as the table's top rule and dragged the paragraph above the table
into the bbox (page 18 spanned 69–309 instead of 171–309). Rules now have to agree on x0
and x1 within `RULE_ALIGN_PT`; a group without two aligned rules is not a table. That also
freed page 31, where the header underline and one table rule had nothing in common.

**Rule change 6b — a coloured stroke is a hyperlink underline, not a rule.** Page 33's
bibliography prints blue underlines across half the text column; the census read them as a
two-rule table. Rules must now be greyscale (`COLOR_NEUTRAL_MAX`).

**Rule change 6c — a table's body rows may sit outside its last rule.** Several tables print
only the top rule and the header rule and no closing rule, so the rows below fell outside
the span and the crop showed a bare header (page 25 spanned 348–380 of a 348–524 table).
The span now absorbs following lines that carry at least `ROW_MIN_NUMERIC` numeric cells at
row pitch, and stops at prose.

**Rule change 6d — a table tail left alone on the next page.** Page 31 opens with two data
rows and a closing double rule whose opening rule is on page 30; with one rule it was
measured nowhere. A single rule with a run of numeric cells above it (not crossing any
other rule, not inside an already found table) is now a `rule-table-tail` region, and a tail
rule sitting just below a found table extends that table instead.

**Rule change 6e — a caption or a section heading between two rules splits the table.**
Page 21 merged Tables 6, 7 and 8 into one 421 pt region because they all align and sit
within `TABLE_GAP_PT`; the section headings inside the box made the crop unreadable. A
between-rules line equal to `Table`/`Figure` or a numbered heading (`4.3.2.`, trailing
period, left of x = 140) now ends the group. A bare integer cell such as `0` or `1` is not
a heading — the first version of this rule did match them and silently deleted the table
on page 23.

**Rule change 7 — a long notation table keeps its closing rule; an image is not a caption
box.** Two defects, both seen on P-C-2017-55583 page 7 and page 10.

7a. A symbol/definition table prints its header rules 20 pt apart and its closing rule 220 pt
below them, because its body is text rather than numbers (`_absorb_rows` needs at least two
numeric cells per row and gives up). The two-rules group therefore comes out 20.6 pt tall,
under `MIN_SIDE_PT`, and the table is dropped. When a group's span is still thinner than
`MIN_SIDE_PT`, the span now extends to the next page-wide rule that starts and ends at the
same margin. Affected: P-B-2010-8362 (p17, p27), P-B-2011-10496 (p18, p21),
P-C-2011-11325 (p9), P-A-2011-9665 (p3), P-C-2017-55278 (p6), P-A-2022-2207343 (p7),
P-A-2022-2209812 (p5), P-C-2017-55583 (p7) — every one a printed table that the census had
been missing.

7b. `is_caption_background` tested `path_count <= 4` plus inside text starting `Figure N`.
An image block has `path_count == 1` by construction, so a pasted figure whose own white
margin spans the caption line was deleted as a caption box: P-C-2017-55583 page 10 lost the
whole Cellular-Automaton figure that way. The guard now only applies to vector clusters.

Both hunks are additive: a full rebuild of every layout on disk changed 8 of 39 hashes and
each change added 1-2 regions, with no region removed and no existing bbox moved. The eight
layout files were rewritten in the same pass, so `check.py` reports `layout identical` again
for all of them.

## Engineering fix, not a rule change

**Grid candidate search in `cluster()`.** The union-find step used to test every pair of
boxes that overlapped in y, which is quadratic when a page is dense. Page 21 of
P-B-2010-7947 holds 108,891 drawing paths and the layout pass never finished (killed
after five minutes). Boxes are now bucketed into cells of size `tol` and a query only
looks at cells its bbox covers after expanding by `tol` — exactly the boxes that can sit
within `tol`. Same pairs, so same components: all six closed papers re-run through
`check.py` report `layout identical`, and paper 7's 108k-path page now lays out in under
three minutes. This is a speed fix with no change in what counts as a region, so it does
not count against the rule-change budget.

**Cell-clique contraction in `cluster()`, second pass.** The grid above still compared one
box against every candidate box, which is fine for a plot frame and hopeless for a point
cloud: page 16 of P-C-2017-55585 prints 123,159 paths, the grid query returns ~4,000
candidates per box, and 239 million pairs pass the `tol` test, so the per-pair union never
finished (350 s and still inside the loop). Two boxes that both sit inside one grid cell
(side `== tol`) are always within `tol` of each other, because their coordinates differ by
at most one cell side on each axis — so a cell is a clique and contracts to one node. A
box straddling a cell border stays an individual node and needs one union per cell it
reaches, not one per qualifying box, for the same reason. The components are therefore the
same as the exhaustive pair sweep; only the order of the unions differs, and a union-find
partition does not depend on order. Verified two ways: partition-for-partition identical
to the old algorithm on 57 pages of three papers, and a full rebuild of all 46 layouts on
disk reports `same 46 changed 0 err 0`. Page 16 now clusters in ~90 s instead of never
finishing. Speed only, no change in what counts as a region.

## Proxy discipline

Per `AGENTS.md`: at most eight proxies per context segment, then further visual
inspection goes to a fresh read-only subagent (`fork_turns: "none"`) that returns a
concise textual audit only. No batching of images, `detail: "high"` only, crop first.

## Progress

| # | paper | pages | regions | items | tables | status |
|---|---|---|---|---|---|---|
| 1 | P-A-2010-6749-395f556a | 52 | 44 | 35 | 5 | closed, `check.py` layout identical, unaccounted 0 |
| 2 | P-A-2010-7571-1ac2a627 | 33 | 40 | 21 | 14 | closed, `check.py` layout identical, unaccounted 0 |
| 3 | P-A-2010-7586-ff69029f | 15 | 23 | 15 | 0 | closed, `check.py` layout identical, unaccounted 0 |
| 4 | P-A-2010-7920-06d31c2b | 24 | 18 | 9 | 0 | closed, `check.py` layout identical, unaccounted 0 |
| 5 | P-B-2010-7273-e234c9a6 | 19 | 12 | 12 | 0 | closed, `check.py` layout identical, unaccounted 0 |
| 6 | P-B-2010-7507-24d34e5d | 46 | 33 | 24 | 1 | closed, `check.py` layout identical, unaccounted 0 |
| 7 | P-B-2010-7947-b6007ae0 | 28 | 18 | 16 | 2 | closed, `check.py` layout identical, unaccounted 0 |
| 8 | P-B-2010-8362-bd23db32 | 33 | 37 | 31 | 2 | closed, `check.py` layout identical, unaccounted 0 |
| 9 | P-B-2010-8479-b934962b | 26 | 11 | 6 | 5 | closed, `check.py` layout identical, unaccounted 0 |
| 10 | P-C-2010-6947-c5305f34 | 11 | 13 | 3 | 6 | closed, `check.py` layout identical, unaccounted 0 |
| 11 | P-C-2010-7812-c2fa13fd | 10 | 18 | 11 | 6 | closed, `check.py` layout identical, unaccounted 0 |
| 12 | P-C-2010-8048-a080a4e2 | 11 | 20 | 14 | 1 | closed, `check.py` layout identical, unaccounted 0 |
| 13 | P-C-2010-8088-e7ab6731 | 11 | 10 | 3 | 0 | closed, `check.py` layout identical, unaccounted 0 |
| 14 | P-A-2011-11199-cfe6d809 | 21 | 28 | 18 | 0 | closed, `check.py` layout identical, unaccounted 0 |
| 15 | P-A-2011-12149-cb2b7105 | 24 | 14 | 12 | 2 | closed, `check.py` layout identical, unaccounted 0 |
| 16 | P-A-2011-9159-41b0c737 | 23 | 25 | 23 | 1 | closed, `check.py` layout identical, unaccounted 0 |
| 17 | P-A-2011-9582-99696cfc | 34 | 68 | 59 | 3 | closed, `check.py` layout identical, unaccounted 0 |
| 18 | P-B-2011-10496-de9286d6 | 34 | 29 | 15 | 5 | closed, `check.py` layout identical, unaccounted 0; two Algorithm pseudocode boxes excluded after the fig_extract rule-span fix exposed them |
| 19 | P-B-2011-11759-ee4be862 | 51 | 27 | 22 | 5 | closed, `check.py` layout identical, unaccounted 0; Figures 3 and 9 unresolved |
| 20 | P-B-2011-12114-03fd7440 | 28 | 31 | 28 | 0 | closed, `check.py` layout identical, unaccounted 0; Figure 1 unresolved |
| 21 | P-B-2011-9440-95f0fa40 | 41 | 54 | 15 | 10 | closed, `check.py` layout identical, unaccounted 0 |
| 22 | P-C-2011-10607-6ed4fd93 | 20 | 17 | 8 | 9 | closed, `check.py` layout identical, unaccounted 0; Figures 5, 6, 11 and Table 6 unresolved |
| 23 | P-C-2011-11325-4609137d | 26 | 11 | 8 | 3 | closed, `check.py` layout identical, unaccounted 0; Tables 0.1 and 3.2 unresolved |
| 24 | P-C-2011-11422-caf513f2 | 20 | 19 | 9 | 9 | closed, `check.py` layout identical, unaccounted 0; paper prints no captions at all, one table block unmeasured |
| 25 | P-C-2011-11893-6a9ea7d9 | 24 | 34 | 15 | 15 | closed, `check.py` layout identical, unaccounted 0; 15 tables against 7 printed numbers, because five unlabelled "Notations" blocks are tables too |
| 26 | P-C-2011-8882-54492a1f | 27 | 54 | 41 | 13 | closed, `check.py` layout identical, unaccounted 0; 41 items against 26 printed figure numbers, because twelve figures are three-panel |
| 27 | P-C-2011-9089-838e50df | 20 | 29 | 13 | 15 | closed, `check.py` layout identical, unaccounted 0; every label written "Figure.N"/"Table.N", so the ctx dump saw no captions at all and both layers were rebuilt by hand |
| 28 | P-A-2011-9665-6560aced | 30 | 30 | 19 | 4 | closed, `check.py` layout identical, unaccounted 0; drawing-heavy paper, seven exclusions (three display equations, one glossary block, one nested raster underlay, two halves of a split appendix table); p3 symbol table added after the fig_extract rule-span fix |
| 29 | P-A-2012-14297-5cb8073e | 45 | 39 | 16 | 12 | closed, `check.py` layout identical, unaccounted 0; twelve table blocks against nine printed labels, because Tables 1, 7 and 11 each break over a page turn; eleven embedded table illustrations excluded |
| 30 | P-A-2012-14990-e2428f0d | 42 | 103 | 38 | 17 | closed, `check.py` layout identical, unaccounted 0; 38 items against four printed figure labels and no printed table numbers; eleven cover rasters plus the drawn title block excluded as page furniture |
| 31 | P-A-2012-15065-1cbc0cd9 | 29 | 53 | 48 | 0 | closed, `check.py` layout identical, unaccounted 0; the paper prints no exhibit numbers and no caption lines at all, so 48 measured blocks are the whole count and both table halves are table-as-figure |
| 32 | P-A-2012-16831-ec8f03fd | 54 | 58 | 54 | 4 | closed, `check.py` layout identical, unaccounted 0; eleven printed numbers attach to fifteen blocks (Figures 18, 19, 21 printed twice, 23 four times, no Figure 8, "figure 25." lower case inside the Figure 24 line); Tables 1, 5, 9 and 10 measured as bands only, and the tail of Table 1 plus Tables 2–4 and 6–8 and 11 print unmeasured |
| 33 | P-B-2012-13074-8fc549d2 | 22 | 18 | 4 | 11 | closed, `check.py` layout identical, unaccounted 0; every exhibit numbered "Chart1"–"Chart15" with no space and no period, so the ctx dump saw no captions and no mentions and all fifteen labels were read off crops; Chart10 is one calendar over pp. 12–15, counted once on the caption-bearing p15 band with the other three bands excluded `split-across-pages` |
| 34 | P-B-2012-13955-a0e5e63c | 18 | 12 | 7 | 4 | closed, `check.py` layout identical, unaccounted 0; eleven printed figures against seven items and four counted tables, because Figures 3.1, 4.1, 4.2 and 4.4 are printed grids recorded as `table-grid`; Figure 2.2's caption opens p8 and Figure 2.3's closes it, one page after their strips; p16-r1 excluded `not-an-exhibit` (6.1 heading plus one prose paragraph) |
| 35 | P-B-2012-15171-ce229936 | 36 | 22 | 22 | 0 | closed, `check.py` layout identical, unaccounted 0; twenty-two regions against twenty-two printed figures, one-to-one, no tables and no exclusions; ten figures cited in text within a page, Figures 11 and 12 introduced on p18 but printed on p20 so left unmentioned; `Table 1: Parameters` on p5 is a declared gap with no measured block |
| 36 | P-B-2012-15417-df1dd905 | 26 | 12 | 4 | 0 | closed, `check.py` layout identical, unaccounted 0; the Java-listing paper — eight of twelve measured regions are code blocks excluded `not-an-exhibit`, leaving four figure items against four printed numbers; Figures 1 and 2 are raster state grids side by side on p8; eight further pages carry unmeasured code paths (p6, p18, p20-p25) |
| 37 | P-B-2012-15420-8b46b980 | 21 | 10 | 8 | 2 | closed, `check.py` layout identical, unaccounted 0; eight printed figures all measured, three of them single-region composite panels (Figure 5 is 2x2, Figures 7 and 8 are a wide Schedule panel over two histograms); the two counted tables are unnumbered grids (p4 vessel counts 3x5, p14 model comparison 23x7) with `caption_source: none`; Figures 2 and 3 are three-step day-by-campsite diagrams with no axes |
| 38 | P-B-2012-15878-825774ea | 23 | 20 | 12 | 8 | closed, `check.py` layout identical, unaccounted 0; twenty regions against eight printed figures and six printed tables, no exclusions; Figures 5-8 are each a 3-D surface printed above its own contour map, so twelve rows for eight figures (surface-or-3D over heatmap-or-contour); Table 6 is one caption over three stacked five-by-five grids, so eight counted tables for six printed ones; only Table 1 (called back to from p10, negative `lead_pages`) and Tables 4+5 are cited in running text |
| 39 | P-C-2012-12218-14ded715 | 19 | 12 | 6 | 6 | closed, `check.py` layout identical, unaccounted 0; twelve regions against six printed figures and six of seven printed tables; five tables are two side-by-side blocks of the same columns, so `cols` counts the physical grid (4 or 6); Figures 1 and 2 are `node-link-network`, Figures 3-5 marker staircases with a dashed discriminating line, Figure 6 a concept/property box diagram; declared gap: Table 4 on p11 has no measured region |
| 40 | P-C-2012-13215-607f0f06 | 19 | 15 | 13 | 2 | closed, `check.py` layout identical, unaccounted 0; fifteen regions against nine printed figures and six printed tables — Figure 4 is two stacked panels across a page turn and Figure 8 a 2x2 block, so thirteen rows for nine figures; Table 4 is transposed (rank numbers in the header row, four metric rows of names only); four tables (1, 2, 3, 5) are printed as unruled text columns and measured by nothing, declared gaps; every caption is the bare number in `Figure. N` form and only Figure 9 carries a title line |
| 41 | P-C-2012-13855-8ff9127d | 19 | 14 | 1 | 10 | closed, `check.py` layout identical, unaccounted 0; fourteen regions against thirteen printed tables and one printed figure, with three typeset `Algorithm 1`-`3` boxes excluded `not-an-exhibit`; ten tables are counted and three (Tables 4, 8, 13) print as unruled text columns with no measured region, declared gaps; nine of the ten counted tables are several side-by-side blocks of the same two or four columns, so `cols` is the physical grid; two rule styles split them, closed-box `vertical-rules` for Tables 2, 3, 6, 9, 11, 12 against open `booktabs` for Tables 1, 5, 7, 10 |
| 42 | P-C-2012-14531-6018365f | 20 | 12 | 7 | 4 | closed, `check.py` layout identical, unaccounted 0; twelve regions against seven printed figures, five printed tables and the summary sheet's drawn title block (excluded `background`); Table 4 on p15 is a declared gap because Figure 5 fills the page's only measured band; Tables 2 and 5 are transposed (people across the columns, row labels down the first one) and Tables 1 and 3 are fully ruled while Tables 2 and 5 are horizontal-rules-only; the text cites Table 1 as 'Table 2.1', kept as the citing spelling; Figure 2 is a polar target diagram (concentric rings 0 to 1) recorded as `scatter` |
| 43 | P-C-2012-15356-6b8f0a28 | 20 | 15 | 10 | 5 | closed, `check.py` layout identical, unaccounted 0; fifteen regions against nine printed figure numbers plus one uncaptioned chart, and four printed table numbers plus the unnumbered symbol glossary; two exhibits are both numbered `Figure 7` (the p15 workflow and the p19 infection model) and both are recorded as printed; Tables 1 and 3 are two side-by-side blocks under one merged `Task 1/Task 2 Statistics` title row, so one table each with `merged_cells`; Table 3's in-grid title says Task 2 against a caption that still says Task 1; the p12 paired-bar chart beside Table 4 has no number and no caption and is cited by nothing; Figure 3's caption carries no colon, giving the one `Figure N` numbering in the paper; only Figure 1 is cited in running text, from p3 |
| 44 | P-C-2012-16075-4bbf9219 | 22 | 20 | 13 | 7 | closed, `check.py` layout identical, unaccounted 0; twenty regions against ten printed figure numbers and nine printed table numbers — Figure 3 is split into its two framed panels (a)/(b) and Figure 8 into its three topic layouts, so thirteen rows for ten numbers, while Figures 4 and 5 are one raster holding two panels each and stay one row with `panel_count` 2; Table 1 on p5 and Table 8 on p19 print but return no measured region (both pages report dozens of paths and no rectangle) and are declared gaps; Table 5 runs over the p15/p16 turn and only its second half is measured, recorded `continued`; Figure 6 is a 2x2 block of three scatters and one bar panel, family `composite-panel`; Figure 9's y-axis prints `/通用格式` placeholder text because the pasted chart's typeface is missing, and its caption repeats Table 8's word for word; Table 9's header prints seven labels over rows of six values; Tables 7 and 9 are `booktabs` against `boxed` everywhere else |
| 45 | P-C-2012-17160-8b6c54d2 | 23 | 10 | 0 | 9 | closed, `check.py` layout identical, unaccounted 0; the paper prints no figures at all — ten measured regions are nine ruled grids plus the p10 displayed conductance formula, excluded `in-body-diagram`; six numbered tables plus the unnumbered appendix listing `A Complete Listing of Results`, which runs over p21–p23 with no caption line and is recorded as three continued fragments (33 + 42 + 7 rows = the full 82 employees); Table 3 is `booktabs` and everything else `boxed`; Tables 4, 5 and 6 are several Name/Guilt blocks side by side, 16, 8 and 4 physical columns with merged group headings; Table 2's cells are phrases, so its numeric column count is zero |
| 46 | P-A-2013-20559-c8c96095 | 16 | 26 | 10 | 0 | closed, `check.py` layout identical, unaccounted 0; 5624 raw regions collapse to 26 unique ones because page 2 paints a full-page parody advertisement as one raster tile repeated thousands of times — twelve of its squares are excluded `background` and four inset panels `not-an-exhibit`, leaving ten figure rows against eleven printed figures. Figure 2 prints one caption over two separately measured panels side by side, so it takes a row per panel with the printed number repeated. Figures 5 and 6 are declared gaps: they print on p8 as typed Time/Temperature rows inside the body text, with a caption line and no measured region at all. The paper prints no table it calls a table — the one grid, Figure 7 'Table of tallies for different shapes over all tested pan areas', is numbered as a figure and stays in the figure block as `table-as-figure`: six columns by twelve rows, a vertical rule between every column and a rule under every row but no closing rule at the top, bottom or right. Families: four `line` (the efficiency sweeps varying α, β, γ and cρ over Polygon Sides 4–20 and Efficiency 0.84–1, legend inside the frame), one `flowchart-or-schematic` (the calorimetry rig), four `other` with `other_note` (octagon lattice, square and hexagon tessellations, and the labelled hexagon defining side/apothem/radius). Every caption prints below, `Figure N:`, 6–17 words, one sentence, none stating a unit or drawing a conclusion. The paper prints no numbered headings at all, so `section_path` uses the five printed sub-headings in the unnumbered form; only Figures 1, 2, 4 and 7 are named in prose, and the one sentence that names Figures 5 and 6 names them together |
| 47 | P-A-2013-23004-8dba2d4c | 21 | 77 | 23 | 3 | closed, `check.py` layout identical, unaccounted 0; 23 figure rows against 23 printed figures, three recorded tables, 51 exclusions all inside the paper's own machinery — the eight text boxes of the Figure 18 flowchart and the six+two arrangement thumbnails printed inside Tables 4 and 5 are `fragment-of-other`, one nine-path vector band over a line of body text on p5 is `not-an-exhibit`, and the remaining 34 regions are the two advertising sheets on p20–p21, which the paper announces itself on p19 ('See advertising Sheets on Next Two Pages.'): two page-filling vector frames `background`, 32 text bands and product renderings `not-an-exhibit`, none carrying a number or a caption. Tables 1 (Notation, p3) and 2 (Parameters of Standard State, p5) print captions but return no measured region and are declared gaps. Families: 10 `other` with `other_note` (arrangement lattices, dot-centred patterns, the labelled L/W rectangle, the bare-arrow centre-dot matrices of Figures 16 and 17), 3 `heatmap-or-contour` (Figures 20–22, the temperature field rendered onto hexagonal and octagonal plates with no axes and no bar), 2 `composite-panel` (Figure 1 photograph cluster + wireframe, Figure 23 line-art strip + two surfaces), 2 `surface-or-3D` (Figures 3 and 5, MATLAB perspective with colour bar), 2 `flowchart-or-schematic` (Figure 2 heat-flow arrows, Figure 18 algorithm flowchart), 2 `line` (Figures 4 and 6, edge temperature curves), 1 `scatter` (Figure 7: ten markers plus one fitted straight line), 1 `photo-or-raster-image` (Figure 19, three catalogue photographs), plus 3 `table-grid`. All three tables are `booktabs` and none is cited. No exhibit is cited by number: all 28 captions print as `Fig. N` / `Table N` and every pointer in the prose is deictic, so every `mention` block is empty. Table captions print above their grid, figure captions below their artwork. The paper prints no numbered headings, so `section_path` uses printed titles in the unnumbered form |
| 48 | P-B-2013-21185-c7f22f59 | 43 | 41 | 22 | 17 | closed, `check.py` layout identical, unaccounted 0; 41 regions over 26 pages — 22 figure rows, 17 printed tables and 2 exclusions (the objective function and its constraint bracket on p24, both `in-body-diagram`). No exhibit carries a number: captions print as bare `Figure` / `Figure.` with no digit, and nine of the seventeen tables have no caption line at all. Six figure rows quote the printed caption (p17, p20 ×2, p22 ×2, p25, p33 ×5 repeated block by block; the p22 line is garbled in the text layer and typed from the crop). Families: 7 `table-as-figure` rows (the α colour grid on p22 and the five β blocks on p33, 31 provinces ranked across five framed blocks), 6 `line` (p7 curve, 4-panel p11, 3-panel p12, GM prediction p14, 31-province surface-water series p17, desalination-timing chart p27), 4 `map-or-plan-view` (nine watersheds, three terraces, α choropleth, six water-transfer routes), 3 `scatter` (p8 observations with linear, quadratic+power and five-entry overlaid fits), 2 `flowchart-or-schematic` (consumption decomposition tree p10, AHP hierarchy p35), 1 `bar` (pollution-control demand by watershed p31), plus 17 `table-grid`. Two tables run across a page break and record `continued` (province ranking p18–p19, province numbering p22–p23); the province numbering headers are split by rows. Declared gap: p36 prints two 4×4 AHP judgment matrices on 108 vector paths with no measured region. No exhibit is cited by number anywhere, so every `mention` block is empty |
| 49 | P-C-2013-18492-ab739371 | 21 | 21 | 9 | 3 | closed, `check.py` layout identical, unaccounted 0; 21 measured regions over 10 pages — 9 figure rows, 3 printed tables and 9 exclusions. Exhibits are numbered by SECTION, not in a flat sequence (`Figure 3-1`, `Figure 3.1.2-1`, `Table 3.1.2-1`, `Table 3.1.4-1`, `Figure 3.1.4-1`, `Figure 3.3.5-1`, `Figure 3.4-1`, `Table 4.1-1`, `Figures 4.3-1`…`4.3-4`), and no such form is in `NUMBERINGS`, so every record carries numbering `none` with the printed label inside the quoted caption. Families: 3 `line` (the situation 1–3 simulation charts), 2 `flowchart-or-schematic` (Forrester's five-factor world model p6; the pre-condition/transfer/post-condition state diagram p14), 1 `bar` (the only extruded 3-D chart in the lane, p16), 1 `heatmap-or-contour` (the 5×5 square lattice, p14), 1 `map-or-plan-view` (western-US state map with ring nodes, p5), 1 `node-link-network` (bipartite Bayesian network, p9), plus 3 `table-grid`. Four exhibits (p16, p17 ×2, p18) each open a second measured box around the same artwork, because the page paints an empty frame image over a live vector chart; those four are excluded `fragment-of-other`, not counted as panels. Two p7 prose bands and three p19 bands (page furniture, prose, display equations 16/18/19) are also excluded. Nine exhibits carry a mention block; `Table 3.1.2-1` and `Figure 4.3-1` are never cited. No declared gaps |
| 50 | P-C-2013-21165-17e64d15 | 19 | 17 | 14 | 3 | closed, `check.py` layout identical, unaccounted 0; 17 measured regions over 11 pages — 14 figure rows and 3 printed tables, no exclusions. The first paper in this run whose numbering fits the enum: flat `Figure 1`…`Figure 10`, `Table 1`…`Table 3`, with only Figure 1 needing the colon form (`Figure N:`). Families: 10 `line` (the World3 screen plot p3; Figure 2's three population/transport/N2O panels p4; the six case-study plots p10, p12 ×2, p14, p15 ×2), 2 `map-or-plan-view` (the two greyscale world choropleths of Figure 7, 1970 and 2008), 1 `bar` (Figure 5's eighteen countries, printed as columns although the caption says 'critical nodes'), 1 `node-link-network` (Figure 3's global and local node architecture, with its own two-entry symbol key), plus 3 `table-grid` (the colour-raster AQI bands with no rules, the booktabs notation list, and the spanner-header input/output grid with one vertical rule). Figure 9 on p15 reprints the Figure 6(a) artwork almost pixel for pixel; counted as its own exhibit per caption, reuse declared in the note. Figure 4 is the only exhibit with no citing sentence. No declared gaps |
| 51 | P-A-2014-25142-c5c79dc7 | 34 | 29 | 18 | 1 | closed, `check.py` layout identical, unaccounted 0; 29 measured regions over 18 pages — 18 figure rows, one printed table and 10 exclusions (the typed MATLAB listings on p27, p29, p30, p31 ×3, p32 ×2, p33 and p34, all `not-an-exhibit`). Exhibits are numbered flatly and the enum holds: every figure prints `Figure N:` and the table `Table 1:`. Seven captions print two to a line across a column break, each column cut mid-word, so a row quotes only the fragment that carries its own figure number and keeps the printed tail ('Rules(2 lanes)', 'lanes, keep-right)', 't Speed Limits(3 lanes, unrestricted)') in its note; the four paired pages (16, 18, 20, 21) are assigned left and right off the crop x positions. Families: 9 `bar` (the four per-lane density panels, the four danger-index panels, the stacked passing-event counts of Figure 11), 8 `line` (the safe-gap curves, the tempo-spatial diagram, the four velocity sweeps, the intelligent-system plot), 1 `other` with `other_note` (the p12 overtaking velocity triangle, a labelled vector diagram with no axes). Table 1 is live vector text, three horizontal rules and no verticals (`booktabs`), captioned above; all eighteen figures are captioned below. Tables 2 and 3 (p10) and Tables 4 and 5 (p23) print caption lines and typed cell rows but return no measured region from the layout pass, so they are declared gaps. Only Figures 2, 4 and 5 are cited by number. Figure 11 is the paper's only stacked column chart and the only drawing with no y-axis title; Figure 14's legend names speed limits 29/32/38 m/s where its sibling prints 28/32/36 and the prose says 28 and 36 |
| 52 | P-A-2014-26911-00c95da0 | 22 | 8 | 3 | 5 | closed, `check.py` layout identical, unaccounted 0; only eight measured regions in a 22-page paper, and every one an exhibit — 3 figure rows and 5 printed tables, no exclusions and no declared gaps, because all but five pages are prose, equations and references. Flat colon numbering throughout: `Figure 1:` to `Figure 3:`, `Table 1:` to `Table 5:`. Families: 2 `line` (the two p10 Google Trends screenshots — one blue interest line each, no y-axis scale, no frame, no legend, peaks lettered A–G and A–N in place and never keyed), 1 `flowchart-or-schematic` (the p12 AHP hierarchy, box-and-arrow on a raster), plus 5 `table-grid`. All five tables are pasted rasters whose caption line is pixels as well, so all five are `typed-from-crop`, all five print their caption BELOW the grid, and all five share one construction — solid blue header band, alternating light-blue body tints, thin vertical rules — so all five are `vertical-rules` with `zebra` true, none booktabs. The three weight tables repeat one seven-entry AHP weight vector verbatim across football, basketball and baseball while the Maxent&GRC row changes. The paper's only numbered citation is broken: p12 prints `As is vividly shown in Figure 2` while introducing the hierarchy drawn on that page as Figure 3, and the sentence before it loses its number altogether (`… is displayed in Figure`), so the mention sits on Figure 2 with `lead_pages` −2 and the hierarchy carries none. Table 5 prints a tight colon (`Table 5:Top 5 …`) where Tables 1–4 have a space |
| 53 | P-A-2014-29282-f92c8e1b | 30 | 33 | 22 | 9 | closed, `check.py` layout identical, unaccounted 0; 33 measured regions over 19 pages — 22 figure rows, 9 printed tables and 2 exclusions (the p1 summary-sheet control-number form grid and title band, both `not-an-exhibit`), no unresolved and no declared gaps. Flat colon numbering throughout, `Figure 1:`…`Figure 22:` and `Table 1:`…`Table 9:`, and every caption reaches the text layer, so none is typed from the crop. Families: 11 `flowchart-or-schematic` (the p4 roadmap, the p15 general flowchart and its p16 `Go` sub-flowchart — the only two that print numbers, T=2000/S=1000/p1=0.3/p2=0.7/d=2 — the p12 freeway schematic and the seven drawn road strips of Figures 2, 4, 6, 7, 15, 16 and 18), 6 `line` (Figure 3's three-series state plot, the radar of Figure 17, the four two-curve comparisons of Figures 19–22), 5 `scatter` (Figures 10–14, blue dots under a red fitted curve, legend boxed inside at a corner) and 9 `table-grid`. Figure 17 is the radar the enum cannot name — five spokes, ring gridlines, radial ticks 0–1, key outside right — so it is `line` on the page-9 precedent of `P-A-2022-2209466-5952dd05` with the construction in `other_note`. Figures 15 and 16 are captioned "a printscreen" but are drawn strips; Figure 18's caption promises RHT and LHT while the panels are sub-labelled "New Rule 2 in LHT" and "New Rule 2 in RHT", 1×2, no legend. Tables 2, 3 and 4 share one merged-row `booktabs` construction and no zebra exists in the paper; Table 1 is the dense grid, a rule after every body row with two internal verticals and no outer sides. Citations run both ways — Figures 10–13 are discussed on p18 and drawn on p17, and Tables 6, 7, 9 with Figure 17 are each cited a page before their page — so those blocks carry negative `lead_pages`; Tables 2–4 are never cited by number, only by the p19 deictic clause "results are shown in following tables", so all three record that clause with an empty style list and count 0. Faults: Figure 2's caption is corrupted to `overtaking(i¡j)`, Table 1 prints `Traffic flow)`, Table 9 heads its index column `Traffic Rule`, Table 3 prints `11.6%` to one decimal, Figure 3 plots twenty transitions against a caption reading "several", and Figures 6 and 7 are near-duplicate strips |
| 54 | P-A-2014-29911-ac64b43b | 40 | 53 | 24 | 5 | closed, `check.py` layout identical, unaccounted 0; 53 measured regions over 28 pages — 24 figure rows, 5 printed tables and 24 exclusions, no unresolved and no declared gaps. Flat stop numbering throughout, `Figure 1.`…`Figure 22.` and `Table 1.`…`Table 5.`, and every caption is in the text layer, so none is typed from the crop. Families: 13 `line` (the three rule-versus-density curves of Figures 3–5, the three optimal-velocity curves of Figures 6–8, Figure 11's three-curve flow plot and the two comparison sets of Figures 15–17 and 19–21), 4 `scatter` (the four panel rows of the density visualisations), 4 `flowchart-or-schematic` (the two cell strips, the Median flowchart and the online-algorithm strip), 3 `surface-or-3D` (the continuum model's 3-D density meshes, `three_d` `surface-mesh`, two panels each) and 5 `table-grid`. Twenty-two printed figure numbers over 24 rows because Figures 9 and 10 are each two panels. Every exhibit captions BELOW its art, tables included — against the lane's habit. Two tables break across pages and are counted once with `continued`: Table 1 from p6 to p7 and Table 5 from p8 to p9, whose caption prints on p9 and which skips Step 12; Figure 18 is one flowchart measured as seven regions, so six are `fragment-of-other`; the p32–p40 appendix is twelve bands of typed C++ excluded `not-an-exhibit`. Tables 2, 3 and 4 are never cited by number — Table 2 takes the deictic clause that introduces the equations and Tables 3 and 4 the p7 sentence on the lane-changing rule, all three with an empty style list and count 0. Faults: Figures 3–5 keep the Chinese single-entry legend `系列2` in English artwork, Figures 6–8 are captioned "Optimal Maximum Velocity" while the art only plots phi against Vmax with no optimum marked, the combined peak (0.72) sits above the light-traffic one (0.69), Figure 14's caption prints on the page after its meshes, and Table 3 carries one merged blank cell in its third column |
| 55 | P-A-2014-30532-8f80536d | 29 | 21 | 16 | 3 | closed, `check.py` layout identical, unaccounted 0; 21 measured regions over 19 pages — 16 figure rows, 3 printed tables and 2 exclusions (the p1 summary-sheet form and the p21 tail of Table 2), no unresolved and no declared gaps. Families: 11 `line`, 3 `scatter` (the big-car-fraction, lane-change-probability and random-braking plates, which are unconnected point clouds where Figures 2–4 are connected line charts), 3 `table-grid`, 1 `heatmap-or-contour` (Figure 1, the space-time state lattice whose cells print a digit 0–5 for the vehicles in each section) and 1 `flowchart-or-schematic` (the uncaptioned p5 "analyzing procedure" chart). Nineteen printed figure numbers resolve into fifteen numbered rows and one uncaptioned chart, because five raster regions carry two numbered exhibits each (8+9 on p17, 10+11 on p18, 13+14 on p23, 17+18 on p26, 19 plus a reused "Figure 12" on p27) and Figures 2–7 carry three sub-panels in a 2×2 plate with one cell empty. Colon numbering `Figure 1:`…`Figure 19:` against bare `Table 1`…`Table 3` with no title; every caption is in the text layer and every caption prints below its art. No exhibit is cited by number anywhere — all seventeen pointers are deictic ("the flowchart below", "the figures show that", "get following curves", "the following are figures of flow, lane change frequency and average speed"), three of them pointing back a page. Table 2 breaks at the page break (five rows p20, x6–x8 on p21 with title and header repeated) and is counted once with `continued`. Faults: Figures 5–6 switch the same x variable between a 0–1 and a 0–100 scale, Figure 5's axis reads "bic car fraction", Figure 7's typeset sub-captions are swapped against its in-image titles, Figure 13's caption prints "Factor sore", and the p27 plate reuses Figure 12's number and title for a different chart |
| 56 | P-A-2014-31333-acc8bc3b | 17 | 8 | 8 | 0 | closed, `check.py` layout identical, unaccounted 0; eight measured regions over four pages (p8–p11) and every one an exhibit — 8 figure rows, no tables, no exclusions, nothing unresolved and no declared gaps. All eight are `bar`: grouped vertical bars over twelve simulation types (Fast/Slow × Computer/Accident Prone/Normal × Heavy/Light), one flow chart and one accident chart per rule system, keyed outside right in a grey-to-black lane-count ramp, complete frame with horizontal gridlines and rotated x labels. NOT ONE exhibit is numbered — no chart has a caption line in the text layer at all, the titles are drawn inside the artwork in small caps ("AVERAGE FLOW RATES OF RIGHT HAND RULE"), and no prose sentence cites a figure by number, so all eight rows carry an empty caption, `caption_source` none and numbering none, with the only pointers the section-4.2 lead ("The figures presented on the following pages summarize the data…") and one positional reference on p12 ("the second figure of Section 4.2.4", `lead_pages` −1). Faults: the three flow charts use y 0–4, 0–4 and 0–3.5 so they are not comparable by eye; the p9 accident legend lists "three lanes" twice and never "four lanes"; no group on the p8 or p9 flow plates draws all five series the legend promises; only the p11 accident plate labels its data (211.3, 98.8, 66.2, 97.3, 30.6, 102, 86.1 — and nothing on the two tall bars); and the p8 x labels print "Fast-Accident Proine-Light" |
| 57 | P-B-2014-26160-510e6a16 | 36 | 57 | 14 | 32 | closed, `check.py` layout identical, unaccounted 0; fifty-seven measured regions over twenty-nine pages, every one accounted — 14 figure rows, 32 tables, 11 refusals, nothing unresolved and no declared gaps. Families: `bar` 9, `line` 2, `flowchart-or-schematic` 2, `composite-panel` 1, plus 32 `table-grid`. The paper is table-heavy because the same five-name rank table prints four times (p1 abstract, p10 twice — Grey and Fuzzy, p27 §9.1, p30 the letter) and six appendix grids carry the raw coach data. Every table is booktabs — top rule, rule under the header, bottom rule, no verticals, no box — and only five carry pale-blue zebra (Table 7 p12, Table 8 p14, Table 12 p19, Table 13 p20, ranks-comparison Table 15 p22). Seven chart plates are ONE Excel 3D column chart exported as a bitmap inside a vector frame that carries the title and axis text (Figures 3–8, 13), so seven regions are refused as `fragment-of-other` plot bodies; the p24 pair by contrast is flat 2D MATLAB columns with annotation boxes, the p22 and p25 plates are line charts, and p28 is a decorated Honor Roll poster holding three ranked tables (`composite-panel`, `panel_count` 3). Traps: Tables 2, 3 and 4 all print the caption "Pairwise comparison matrix of hierarchyⅡ-Ⅲ", and two unrelated tables are both numbered Table 15 six pages apart; Figure 6 is captioned basketball while its artwork is titled field hockey and carries field-hockey names, Figure 7 the reverse; p23 cites Figure 9 for what is Figure 10 (recorded as a trailing sentence on the Figure 9 row, not as a Figure 10 citation); five tables were measured only as a header band because their interiors carry no rules — Table 4 p8, Table 8 p14, and the header strips of Table 7 p12 and Table 12 p19, whose grids are counted once on the body region; the p17 comment set prints NO header row and `header_rows` is floored at 1, with the deviation spelled out in the note; the appendix grids take their appendix list item as caption with `numbering` none and four of them continue across a page break with the header row reprinted (`continued` true, empty caption on the tail) |
| 58 | P-B-2014-26333-27e7d8ab | 54 | 63 | 33 | 12 | closed, `check.py` layout identical, unaccounted 0; sixty-three measured regions over thirty-four pages — 33 figure rows, 12 tables, 18 refusals, nothing unresolved, one declared gap. Families: `bar` 18, `line` 10, `flowchart-or-schematic` 4, `photo-or-raster-image` 1, plus 12 `table-grid`. Eighteen of the 33 figures print one number over two side-by-side panels, so the paper shows 51 chart panels under 33 numbers and every right panel is refused as `fragment-of-other`. Figures 6–15 are MATLAB line charts with a boxed legend inside the upper-right; 16–33 are flat grouped bar charts in which light and heavy traffic are two adjacent bars inside ONE panel, never two panels. Captions print BELOW every figure and ABOVE every table, numbering bare `Figure N` / `Table N` with no punctuation anywhere. The six evaluated-rule and sensitivity grids on p40–p44 keep one internal vertical rule between the stub and the first data column; the four on p45–p46 are booktabs with horizontals only. Two traps: **Table 3 on p16 is printed and captioned but returned no region** — declared a gap in the note, so the paper prints 13 tables and 12 are measured; and p22 cites the two time-space diagrams as "Figure 8", which is the flow-rate-of-each-lane figure three pages later, leaving Figure 6 with no named citation. Eleven figures are never cited by number (3, 6, 10, 12, 13, 14, 15, 29, 30, 31, 32) and five are cited a page or two after the art (Figures 4, 11, 18, 21, and 24, whose first name is "Figure 24(a)" on p39) |
| 59 | P-B-2014-26636-060c74b1 | 38 | 48 | 4 | 27 | closed, `check.py` layout identical, unaccounted 0; forty-eight measured regions over twenty-two pages — 27 tables, 4 figure rows, 17 refusals, nothing unresolved, one declared partial. Families: `table-grid` 27, `line` 3, `composite-panel` 1; no bar, scatter, map or schematic anywhere. Twenty-five numbered grids plus two unnumbered notation grids (p5 symbol glossary under 2.2.1 Notations, p22 Shannon-entropy notation under 7.1.2 Notation), all 27 measured and all the same full-ruled box — outer box, row rules, column verticals, no booktabs, `header_rows` 1 except the floored blanks. Captions print ABOVE every table and BELOW every figure. The rule this paper settles: **the row is the fragment that carries the caption**, so ten continuations (p11r1, p12r1, p13r1, p14r1, p21r1, p22r1, p25r1, p26r1, p27r1, p28r1) are refused as `split-across-pages` and twelve grids produce twelve rows, never a second. Table 3 splits three ways — caption plus three rows at the foot of p10, 22 rows filling p11 with one orphan row holding a lone "9", a two-row tail on p12. Traps: the layer welds Table 14's caption into "Table 147.", prints "Table 2.Interrelationship" and "Table 7.1.Top 5college" with no space, and gives Tables 11 and 12 titles of "Table 11." / "Table 12." only; **Table 7.2's caption is on p15 and its grid on p16** (quoted from p15, `position` above); Tables 21–23 print rho at U+F072 and the equals sign at U+F03D with a space before it, so those captions were copied from the layer, and Table 23's header carries the stray Chinese "公式"; Table 10 prints five rows but only four fall inside its measured box — Ned Harkness sits in p17's 23-path block that measured as no region, declared in the note; p3 and p37 body prose and p7's display formula are white per-line text-frame patches read as vectors and refused as `not-an-exhibit`; the p37 photo strip (Wooden, Bryant, Summitt) is butted edge to edge with no number and no caption, so one `composite-panel` row with `panel_count` 3 and two `fragment-of-other` refusals. Shading is semantic: Tables 5 and 16 shade the top five and say so in a footnote ("gray" / "grey"), Table 19 is the only true zebra, Table 17's five shaded rows (2, 3, 7, 8, 9) have no key and are recorded `zebra: false`. Eight tables are never cited by number (4, 5, 8, 9, 10, 18 and both unnumbered grids); 6.1/6.2 and 7.1/7.2 each share one joint sentence; Table 20 is cited twice and carries the paper's only admission that its methods disagree; the three p18 Excel line charts are cited one page early from p17 and Figure 3's caption was pushed to p19 |
| 60 | P-B-2014-28414-5bd5b982 | 33 | 56 | 10 | 22 | closed, `check.py` layout identical, unaccounted 0; fifty-six measured regions over twenty-three pages - 22 tables, 10 figure rows, 24 refusals, nothing unresolved, three declared decisions. Families: `table-grid` 22, `line` 6, `flowchart-or-schematic` 3, `bar` 1, `other` 1 (Figure 7.6 is a radar pentagon and the family vocabulary has no radar member, so it is filed as `other` with an `other_note`). Twenty-two numbered grids plus four unnumbered notation grids under 2.1 Symbols and Definitions, all 26 measured; the house frame is the full box and exactly three grids break it (Tables 4.3, 6.1, 6.2 print horizontals only), Table 4.3 also labels BOTH its fourth and fifth aspect column `X3`. **Captions print BELOW every exhibit in this paper** - the exact inverse of paper 59. The row rule settled in 59 is applied unchanged: five grids have their caption on the far side of a page break (Tables 5.2, 6.2, 6.4, 6.7, 7.2), so the header fragment carries the row and the caption is quoted from the page that prints it. Two grids are two tables inside one frame (Table 4.2 and Table 6.1 repeat the header with a centre divider, six printed columns carrying ten ranks in five rows); only Table 4.1 (Goal cell spans 14 rows) and Table 6.7 (aspect stubs merge over their metric rows) merge cells. Shading four ways: Tables 6.4-6.6 band 238/255 and mark moved names in bold rather than fill, Table 4.3 bands in two-row pairs, Tables 6.3 and 6.8 shade a fixed set of rows with no key, the rest shade only the header. Exactly ONE by-number citation in the paper - changes of weight distribution can be seen clearly in Figure 7.1 (p26, same page as the art) - the other 25 numbered exhibits are pointed at with the following table shows / shown in following table / Here are our results: / The following figure shows / (See figure). Figures 7.4 and 7.5 share one printed caption line, Figure 7.4 && 7.5. Traps: Table 7.1's caption prints on the same line as the tail of formula 3 so the layer interleaves them and that verbatim is typed from the crop (typed-from-crop); Table 3.1 prints four of the ten coaches its own prose promises, with a row holding nothing but an ellipsis, and the row count records what the page prints; Table 3.2 jumps 1987-88 to 2012-13 with no omission marker; section IX is a captionless three-sport photo block whose header row prints just ABOVE the measured region, fifteen portraits refused as fragments and the two p31 grey rank bands as continuations |
| 61 | P-B-2014-28875-728f6f07 | 35 | 38 | 11 | 18 | closed, `check.py` layout identical, unaccounted 0; thirty-eight measured regions over twenty-four of thirty-five pages - 11 figure rows, 18 tables, 9 refusals, nothing unresolved, six declared decisions. Families: `table-grid` 18, `flowchart-or-schematic` 6, `line` 4, `photo-or-raster-image` 1; no bar, scatter, map or surface anywhere, and the one raster is the p24 photo strip. Eighteen numbered grids, every one cited by number at least once except Tables 15, 16 and 17, which the paper prints as the model-vs-website comparison triple and never names in prose. **Captions split by kind and never mix: all 18 grids caption ABOVE, all 11 figures caption BELOW.** Ruling is two registers - 11 fully boxed (outer box, row rules, column verticals) and 7 booktabs (Tables 3, 6, 8, 9, 11, 12, 14 with only top, mid and bottom rules) - no grid is ruled vertically only, no grid is unruled, and no grid bands a single row except the two grey 'Metrics'-label rows of Table 2; `zebra` is false on all 18. Merged cells appear in exactly 3 grids: Table 4 spanners its two level-1 stub groups over their level-2 rows (6 printed columns, 17 rows), Table 5 merges its two-row header, Table 13 leaves its year stubs wrapped tall rather than merged. Header depth is one row in 16 of 18; the two two-row headers are Table 5 and Table 7, both the 3x10 weight vectors for the two-level model. Seventeen grids run the full text measure and exactly one, Table 3 (6x3, the NCAA Basketball top five), is set at half width. Numbering is intact throughout - 'Figure N' 11 of 11 and 'Table N' 18 of 18 - but the caption TEXT is not: **Table 10's caption is welded to its own header stubs** ('Table 10 The weight of each metrics w1 w2 w3 w4 w5 w6 w7 0.'), so the verbatim carries the column glyphs, and **Figure 2's caption carries a stray in-art token** ('Figure 2 SOS The metrics for NCAA Football coach.'), which is why that one row is `typed-from-crop` and the other 10 figure captions come from the layer. The heading detector failed on this paper - 7 headings over 35 pages, one of them bogus - so every `section_path` here is the printed heading taken by hand and prefixed `未编号标题 ` with `section_numbered` false; the ctx paths are unusable from p21 on, where all eleven rows of the second half inherit the same bogus label '0.25 Then got the coach Fuzzy Evaluation composite score'. Exhibit placement: 10 of 18 grids and 5 of 11 figures sit in a Results-named section, 4 grids under Modeling test, 2 grids and 5 figure rows under the model-building headings, and Table 1 alone under Symbols Definitions. Citation behaviour is thin and two-faced: Table mentions are mostly one and done (14 of 18 cited exactly once, 3 never, Table 5 three times), figure mentions run 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 4 - and **the paper misdirects twice**: p16 opens a paragraph describing the two-level metrics tree with 'As shown in Figure 1' when the art under it is Figure 4, recorded as a second by-number mention of Figure 4, and Figure 9 prints at the head of p27 with no introduction, first reached only afterwards as 'The results similar to Figure 7, Figure 9'. Traps: p17r1 is the continuation of Table 4 (its Classification 3 block, W3 row and By+1..By+2 rows with no caption) and is refused `split-across-pages`, so Table 4's 17 rows are counted once on p16; Table 13 prints a score column with no header row at all, so its `header_rows` is floored to 1 and the missing stubs are declared in the note; p10r1 is a display formula's bracket cluster and p2r1 the sentence 'Dimensional reasonableness ... 0.0297' read as a block, p24r2 a four-path prose band, p28r1 and p29r4 prose bands under Conclusion, p30r1 and p32r1 the same, p34r1 the reference list - all eight refused `not-an-exhibit` |
| 62 | P-B-2014-29696-84be6e3a | 44 | 76 | 16 | 17 | closed, `check.py` layout identical, unaccounted 0; seventy-six measured regions over thirty-four of forty-four pages - 16 figure rows, 17 tables, 43 refusals, nothing unresolved, seven declared gaps. Families: `table-grid` 17, `flowchart-or-schematic` 3, `bar` 3, `line` 3, `other` 3, `scatter` 2, `photo-or-raster-image` 1, `map-or-plan-view` 1; the three `other` rows are the vector-angle illustrations (Figs 2, 3, 4), which no family names, and each carries an `other_note`. **The paper runs two number series**: the MCM summary sheet prints bold `Figure 1` and `Figure 2` with no caption text at all, the body prints `Fig 1.` to `Fig 13`, and fifteen printed numbers cover sixteen exhibits because the page-2 execution flow chart is never numbered and never captioned (`caption_source` none). Captions split by kind and never mix: all 15 figure captions print BELOW the art and all 15 captioned grids print ABOVE the grid. Ruling is three registers: the SPSS grids are booktabs (three horizontal rules, no verticals anywhere - Tables 2, 3, 5, 6, 7, 8, 9, 11, 12, 21, 22, and the three sport grids 17-19 whose body rows are separated by fine DASHED rules), Table 1 is a boxed grid with open sides (top rule, double rule under the header, row rules, one centre vertical, no outer side borders), and the two appendix dumps are full grids (outer box, a rule under every row, a vertical at every column boundary). No grid bands a row and none shades a cell; `zebra` false on all 17. Merged cells appear exactly once, Table 8's `before time optimized` / `After time optimized` spanner over two name columns. Header depth is one row in 16 of 17; Table 8 is the only two-row header, and it is a broken one - the leftover `Ranking / Name. / Gender` label row is outgrown by a body that prints two names and no gender. Nine grids are set short of the measure (76 to 87 per cent, each measured in its note) so `full` here means the wide bucket rather than the exact measure; two grids print more labels than the body has fields (Table 9 twelve labels over ten Sig. values, Table 21 thirteen over twelve). **Seven numbered tables print with NO measured region** - Table 4 (p15, only its caption band boxed as a 25-path fragment), Tables 10 (p25), 13, 14, 15 (p30), 16 (p31) and 20 (p36) - declared in the note; every one is visibly ruled with the same three-rule house style and spans only 158-437 pt of a 595 pt page, so the region pass had no enclosing box to key on. The heading detector is unusable (112 heading records, every text null, section paths assembled from racing-result rows such as `8 Bill Self M` and `12 Different Factors`), so all forty `section_path` values are the printed numbered headings, which the text layer does carry verbatim, with `section_numbered` true. Traps: **Tables 17, 18 and 19 carry a coach PHOTOGRAPH inside the Name column of every row**, twelve rasters in all, refused as fragments of those tables (one of them printed above the next table's closing rule); Figure 1 is three coach photographs boxed six times (one row, `panel_count` 3, five refusals) and Figure 2's two flanking pictures twice (one row, two fragments, two duplicates); the page-2 flow chart is boxed twice and its rotated side label once (one row, two refusals); Fig 12's map is boxed twice (one row, one duplicate); Table 5 is one exhibit printed as two stacked blocks with its header row repeated mid-table; Table 6's region holds its heading, caption, header and row 1 only, rows 2-10 printing outside the box; Table 3's region is the header band only, the eleven factor rows below it unruled with no bottom rule; Table 22 splits p37/p38 with seven name pairs on the far page and no repeated header; the appendix is two 60-row dumps (`Original Data` 38+22, `Modified Data` 18+41+1) each recorded as one unnumbered table with three refusals. Ten rows are never named by number (Figs 8, 9, 10, 12, 13, Tables 1, 3, 6, 8, 17, 18, 19 - Figs 3, 9 and 10 and Tables 3 and 6 are introduced by deixis only) and four are cited a page before they print (Fig 1 from p12, Fig 4 from p15, Fig 11 from p28, Table 12 from p27). Recorded defects: the y axis of Fig 1 reads `Inflence`; Fig 2's caption runs the number into the title (`Fig 2.Explanation`); Table 8 misspells Comparison as `Camparson`; Table 3 numbers without a space (`Table3.`); Table 4's caption line extracts twice on p15; Table 9's header spends both T and G twice and Table 21's header prints thirteen labels over twelve fields; Table 15 is titled `Softball Coach Ranking` while listing baseball coaches, with Ron Fraser printed twice; Fig 12 is a cartoon map with no scale, no state shading, no state labels and no title, credited only by `Fig.12 Map of U.S.A. [22]` and a right-aligned `Images come from Google Image Search`; and two appendix names are truncated (`Brenda Fres`) with three wrapped across the row |
| 63 | P-B-2014-30680-9f0c0d05 | 21 | 9 | 5 | 4 | closed, `check.py` layout identical, unaccounted 0; nine measured regions over nine of twenty-one pages - 5 figure rows, 4 tables, 0 refusals, nothing unresolved, three declared gaps. Families: `table-grid` 4, `node-link-network` 3, `line` 2; no panels, no scatter, no colour beyond the two density curves. Not one grid in this paper is numbered or captioned, and all four are complete closed grids, so all four are `vertical-rules` - two LaTeX, one Cambria on the magazine spread. Figure 2's caption contradicts the sentence that introduces it, and both density figures print their axis titles outside the box they are measured by |
| 64 | P-C-2014-25318-eac62e81 | 21 | 14 | 11 | 3 | closed, `check.py` layout identical, unaccounted 0; fourteen measured regions over twelve of twenty-one pages - 11 figure rows, 3 tables, 0 refusals, nothing unresolved, four declared gaps. Families: `node-link-network` 4, `scatter` 3, `line` 2, `flowchart-or-schematic` 2, `table-grid` 3. The paper prints eleven figures and seven tables; Tables 1, 2, 3 and 7 return no measured region because each is a two-rule booktabs grid whose two rules stand 178-314 pt apart, past the 120 pt grouping gap, and the table-tail fallback cannot fire on a zero-height rule. Two grids are two side-by-side blocks inside one ruled frame with the header band printed twice (Tables 5 and 6), so `cols` counts the physical 6 and 4; Table 5 prints three rules and no vertical at all, Table 6 three rules plus one centre divider, so both are `booktabs` and neither is a closed grid. Captions split by kind with no exception - eleven figure captions below, three table captions above - and Figure 3's is the only one set as a justified two-line paragraph. Traps: Table 5's measured box stops at 564.1 pt while its closing rule prints at 589.6 pt, so ranks 11-12 and 23-24 fall outside; Figure 6's ticks are logarithms of the quantities its axis titles name; Figure 9 plots fourteen markers against Table 7's fifteen rows with the 238-million star missing and no note anywhere; Figure 7 carries Figure 4's caption verbatim over a co-star network of actors; Figure 2 labels two of its three axes 'Normalization Degree Centrality'; Figure 3 promises a power law on two linear axes; Section 6's art prints at the top of the reference page, so the `References` heading sits BELOW Figure 11 and the governing heading is the numbered 6 on p20 |
| 65 | P-C-2014-27688-856eb1b7 | 19 | 14 | 6 | 7 | closed, `check.py` layout identical, unaccounted 0; fourteen measured regions over ten of nineteen pages - 6 figure rows, 7 tables, 0 refusals, 1 exclusion, nothing unresolved and no unmeasured exhibit. Families: `table-grid` 7, `node-link-network` 4, `flowchart-or-schematic` 1, `composite-panel` 1. The paper prints six figures and seven tables and all thirteen own a measured region - the first paper in the lane whose printed table count and measured table count agree. **Every one of the seven grids is a closed box** - full-height vertical rules at every column boundary plus a horizontal rule on every row, 4 to 7 verticals across and 5 to 17 horizontals down - so all seven are `vertical-rules` and not one `booktabs` grid prints here, the mirror image of paper 64. Three grids are two blocks side by side that print their header band twice (Table 2 six physical columns, Table 4 four, Table 7 the four of two `(Rank, Company)` pairs), so `cols` counts the physical grid; Table 2 is 416.5 pt against a 418.3 pt measure (99.6 %) and overhangs the right margin by about a point. Figure 6 is the paper's one composite: a four-sided rule box divided at 276.2 pt into a TYPESET pseudo-code cell and a 356x500 bitmap flowchart cell, with its caption printed INSIDE the box - the only caption in the paper that is neither below its art nor above its grid - and the bitmap is a measured region of its own, excluded `fragment-of-other`. Traps: Figure 4 draws hundreds of nodes with hubs numbered 8 and 13 where its section counts 16 papers, and the page never reconciles the two; Figure 3 hangs a year axis under the art that no node sits on; Figure 1 claims 511 vertices and 18000 edges for a drawing of a few hundred unlabelled discs; Table 5's fourth header prints `C(S(0.5-0.95))` where the sentence setting the experiment says a random value from 0 to 1 and the sentence below the grid says 0.5 to 0.95; Table 6's Score column mixes whole numbers with one- and three-place decimals and only three of its fifteen companies print a non-zero in-degree; Table 3's first header cell prints the two words `In Degree` over one column, which the word x-positions settle (186.6-194.8 and 197.2-227.9 pt, both inside 181.0-233.0); the heading detector returns p12's nine pseudo-code lines and p15's twelve Table-7 rows as headings, so every `section_path` is the printed governing heading. Five figure rows and three table rows are never named by number in prose and carry `none_mention`, and two lowercase by-name citations (`show them in table 1`, `list in table 4`) are recorded as they print - the style check is case-sensitive |
| 76 | P-B-2015-36178-d0225ad0 | 20 | 11 | 10 | 0 | closed, `check.py` layout identical, unaccounted 0; eleven measured regions over nine of the twenty pages — 10 figure rows and 1 exclusion, no printed table. Families: `flowchart-or-schematic` 4, `scatter` 3, `map-or-plan-view` 2, `line` 1. The paper prints seven numbered figures and all seven own a row; the other three are the unnumbered pictures of the closing press release. Row restored 2026-10-24 after a peer ledger reset dropped it (record file unchanged) |
| 77 | P-B-2015-38720-26d38781 | 61 | 47 | 38 | 0 | closed, `check.py` layout identical, unaccounted 0; 47 measured regions on 30 pages — 38 figure rows (37 numbered + the p16 aircraft specification grid pasted in as a picture) and 9 refusals. Families: `line` 11, `histogram` 9, `scatter` 7, `flowchart-or-schematic` 5, `surface-or-3D` 2, `map-or-plan-view` 1, `composite-panel` 1, `photo-or-raster-image` 1, `table-as-figure` 1. **Not one of the 37 captions reaches the text layer** — they are painted into the pictures, so all 38 rows are `typed-from-crop`. Three printed rule-grid tables (p13 29 rules, p14 30, p41 14) get no measured region at all: a declared gap, not patched. Row restored 2026-10-24 after a peer ledger reset dropped it (record file unchanged) |
| 78 | P-B-2015-39173-b8260835 | 32 | 18 | 18 | 0 | closed, `check.py` layout identical, unaccounted 0; 18 measured regions on 14 pages, all exhibits — 13 numbered figures + 5 uncaptioned pictures, no refusal, no printed table. Families: `line` 8, `table-as-figure` 4, `flowchart-or-schematic` 3, `map-or-plan-view` 1, `surface-or-3D` 1, `bar` 1. Figure 11's caption says "Map representation" over a ruled seven-column probability table, kept as printed. Section 3's title sits at the foot of p16 and the heading index reads pp17-22 as 2.6.2 Weaknesses, so every `section_path` was rebuilt from the printed lines; ten of the thirteen figures are never named in prose and all three citations lag their exhibit. Row restored 2026-10-24 after a peer ledger reset dropped it (record file unchanged) |
| 79 | P-B-2015-40612-8bcdc1a7 | 34 | 19 | 14 | 5 | closed, `check.py` layout identical, unaccounted 0; 19 measured regions on 14 pages, all exhibits — 14 numbered figures + 5 printed grids. Families: `heatmap-or-contour` 7, `table-grid` 5, `map-or-plan-view` 3, `composite-panel` 2, `flowchart-or-schematic` 1, `scatter` 1. **Figure 9 is printed twice** — Figure 2's artwork on p14 carries an inset heatmap captioned "Figure 9: Underwater Search Posterior PDF for Impact Location" *inside the picture*, twelve pages before the same figure appears on p20. Tables 2, 3, 4 and 6 get no measured region (declared gap); Table 5 prints two rules and no closing rule. The heading index files Figure 1 under 6.2 and Figure 2 under 6.4.1.1 although both headings print *below* the pictures, so every `section_path` was rebuilt from the printed line tops. Citation is the best in the run: 18 of 19 exhibits named in prose. Row restored 2026-10-24 after a peer ledger reset dropped it |
| 81 | P-C-2015-33900-7f8065e8 | 20 | 13 | 11 | 1 | closed, `check.py` layout identical, unaccounted 0; 13 measured regions on 10 pages — 11 figure rows, 1 grid, 1 exclusion. The paper numbers 11 figures and 4 tables, so every figure and one table own a region. Families: `line` 3, `flowchart-or-schematic` 3, `bar` 2, `node-link-network` 2, `scatter` 1, `table-grid` 1. **Table 4 repeats Table 3 number for number** — the sigma sweep on p16 and the mu sweep on p17 print the same twelve values under captions promising different parameters, and the prose reads the second as independent confirmation. **Caption collapse**: Figures 1-5 carry full descriptions, Figures 6-11 are captioned "Task 2.1" through "Task 6" and nothing else. The one exclusion is Figure 1's own key box on p6 (hatch swatches for Manager/Branch Offices), returned as a separate region 8 pt under the chart and declared `fragment-of-other`. Tables 2, 3 and 4 print with no rules at all and get no measured region — the unruled-grid blind spot again. 3.2/3.2.1 on p6 and 3.3 on p8 all print *below* the pictures they would otherwise be credited with |
| 121 | P-B-2017-68303-6c8a9ede | 21 | 19 | 15 | 4 | closed by mcm-5e, `check.py` layout identical, unaccounted 0 |
| 123 | P-B-2017-70174-8bf62421 | 18 | 15 | 15 | 0 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 6.2 heading lost to the word cap, so Figures 8 and 9 sit on their parent section path |
| 128 | P-C-2017-55585-278f2f68 | 36 | 55 | 19 | 4 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 20 printed figures and 4 printed tables against 19 item rows, because Figs 13+14 and Figs 16+17 are each one measured region holding two separately captioned charts (recorded as one `composite-panel` row apiece, both captions quoted in the note); 32 exclusions, mostly the vehicle-bitmap strips inside the nine lane schematics |
| 129 | P-D-2017-55285-1835cc0b | 33 | 50 | 31 | 2 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 31 printed figures and 2 printed tables against 50 measured regions and 17 exclusions — 14 of those are bitmaps pasted inside a larger drawing (seven steps of the Figure 1 queuing diagram, five lane blocks of the Figure 12 PBQ diagram, one axes fragment of Figure 17, one clip-art raster inside Figure 19) and 3 are the ruled header bands of the code-listing pages 21/22/31; nine exhibits have no citing sentence anywhere (Figures 3, 10, 14 and all seven appendix plates), recorded as `mention.count=0` rather than invented; twelve captions are broken across a column break and store the fragment carrying the figure number, with the tail in the row note |
| 130 | P-D-2017-55295-9001b6d9 | 25 | 26 | 19 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 19 printed figures and 5 printed tables against 26 measured regions and 2 exclusions, both on page 21 — Figure 18 is one captioned pair returned as two side-by-side regions, so the left panel carries the row (`panel_count` 2) and the right panel plus the three-entry legend box nested inside it are `fragment-of-other`; two exhibits are cited by no sentence at all (Table 3, Figure 2); all 24 captions print below their exhibit, `Figure N:` / `Table N:`, 3–18 words, one sentence, none stating a unit; three captions are `typed-from-crop` because the text layer interleaves Figures 7 and 8 on one line and hyphenates Figure 19 across a line break |
| 131 | P-D-2017-56632-67f41f43 | 22 | 28 | 10 | 0 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; ten printed figures and no tables against 28 measured regions and 18 exclusions. Eight of the ten figures are one printed number covering two side-by-side panels, so each row carries the left panel (`panel_count` 2) and each right panel is `fragment-of-other` — the row count equals the printed-number count. Ten of the excluded regions are not artwork: six boxed Assumption paragraphs, the X/W/Y definition box, the two boxed equations (5) and (6), and the Algorithm 1 pseudo-code listing. The prose cites by pointing at the page rather than by number — five of the ten figures are never named, Figure 3 has no referring sentence at all (`first_page=null`) and Figure 4 is first named on the page after it prints (`lead_pages` -1); all ten captions print below, `Figure N:`, 19–29 words, no unit and no conclusion; Figures 2 and 4 are `typed-from-crop` because the typesetter hyphenated 'inter-arrival' and 'passenger' across a line break |
| 132 | P-D-2017-67316-f37f83c8 | 30 | 42 | 16 | 3 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; sixteen printed figures and three recorded tables against 42 measured regions and 23 exclusions. Three of the sixteen "figures" are printed tables — Figure 10 (ruleless, zebra-banded, 11 columns), Figure 13 and Figure 14 — and carry family `table-as-figure`, the one place where the caption word and the exhibit form disagree. Four printed tables (Tables 1–4) have no measured region at all: the detector returns paths but no rectangle on pages 9, 11 and 13, so they are declared gaps rather than invented bboxes. Figure 12 is a single woven infographic returned as seventeen nested rasters — the row carries the smiley disc, six boxes are `fragment-of-other` and ten are `duplicate`. Three caption bands (Figures 6, 8, 9) are `caption-background`, and the green-framed "To Security Managers" letter that breaks across pages 17–18 is `not-an-exhibit` plus one `fragment-of-other`. Numbering is `Figure N` / `Table N` with no colon anywhere; all nineteen captions print below, 4–24 words, one sentence, not one states a unit and not one draws a conclusion; five are `typed-from-crop` (Figure 6 hyphenated across a line, Figures 8 and 9 wrapped around a two-column body, Figures 15 and 16 interleaved on one line with mangled μ/σ). The prose names only two of the nineteen exhibits by number |
| 133 | P-D-2017-68942-f0b0893e | 37 | 30 | 12 | 17 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; twelve printed figures and seventeen printed tables against 30 measured regions and a single exclusion — page 1, the MCM summary sheet as one full-page raster, which is not artwork. This is the first paper in the lane with no fragmentation at all: no panel split, no duplicate box, no caption strip. The prose cites by the wrong numbers throughout — three sentences call the zone schematic "Figure 4", the WTMD bar chart is introduced and then read as "Figure 11", the slow-traveller table as "Figure 15", and section 8.1 refers to its own table as an unresolved "Table ??". Nine tables and five figures are never cited. All seventeen tables are fully boxed with vertical rules on every column, grey header rows and no zebra striping; not one is booktabs; nine merge the generation-probability column over a five-row block and two stack a second header row. Tables 16 and 17 are one grid reprinted at 30% and 40% and parked before appendix A with no heading of their own. Legends split three ways: inside for the three throughput line charts, one horizontal row below the x-axis title for the five grouped bar charts, none for the rest |
| 134 | P-E-2017-61502-f0a50d47 | 21 | 11 | 4 | 4 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; four printed figures and four printed tables against 11 measured regions and 3 exclusions. The exclusions are both duplicate and one fragment: the MCM summary sheet on page 1 reprints Figure 2.1 and Figure 4.1 in its right column with unnumbered four-word captions ("Process flow for model creation", "Current and Projected Results for the analyzed cities"), and the second box on the landscape page 21 is a fragment of Table A-2. Caption side is rigidly split by exhibit type and never mixed — all four figures caption below the artwork, all four tables caption above the grid. Every number is printed with a hyphen glued to it and no period or colon ("Figure 2.1-Process flow", "Table 2.1-", "Table A-1-"), which is outside the numbering vocabulary and is recorded as `Figure N` / `Table N` with the hyphen declared in the row note. Three of the four tables are ruled three different ways: fully boxed (Tables 2.1 and 4.1), outer box plus column rules with an open body (Table A-1), and not ruled at all (Table A-2, held together by five coloured banner strips and a lavender TOTAL strip on the paper's only landscape page). Two of the four figures are Infogr.am exports and say so in their own captions; both drop the axis title and print a single-row legend below the plot. Table 4.1 runs from x=10.2 to x=601.2 on a 612-point page, i.e. past the left margin. Half the exhibits are appendices announced ten to sixteen pages early: Table A-1 on page 4 (`lead_pages` 16), Figure A-1 and Table A-2 on page 8 (`lead_pages` 12 and 13). One coverage gap is declared rather than patched: the printed Table A-2 grid is one continuous table from y=84.8 pt (green banner) to y=490.9 pt (lavender TOTAL strip), but the detector returns only its top 133 pt and one mid-table box at 383.1-421.1, so 165 pt of printed grid - the tail of Smart Community, all of Smart Development and the Smart Housing banner and opening rows - falls inside no measured region |
| 135 | P-E-2017-65123-e36461ec | 23 | 21 | 15 | 3 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; fifteen printed figures and three printed tables against 21 measured regions and 3 exclusions (the Tab.1 continuation on page 6, the second Ningguo satellite tile of Figure 6, and the EWM correlation-coefficient display equation, which the detector box under-covers on the left). Seven of the fifteen figures are not drawn for print: Figures 1-4 are Office drawings pasted as low-resolution rasters whose shapes carry broken words ("Compartson", "Developm ent", "Coordi nation"), Figure 8 is a libsvm grid-search export, Figure 15 a MATLAB surf export and Figure 6 a pair of web-GIS screenshots, so only those two tool exports print an axis title at all - the evaluation line charts of Figures 9-11 have ticks and no axis names, and Figure 12 prints its unit "10000 people" inside the plot frame. The caption grammar never settles: "Fig.1" and "Fig.2" carry no period, "Fig.3." through "Fig.12." do, "Fig 13." and "Fig 14." use a space, "Fig.15" drops it again, and the tables print "Tab.1"/"Tab.2" - three spellings outside the numbering vocabulary, all recorded normatively with the printed form in the row note. All fifteen figure captions print below the artwork and both captioned tables print above the grid; the page-4 symbol glossary prints with no caption and no number at all. The three tables are ruled three ways and only Tab.2 is boxed: the glossary is booktabs, Tab.1 is a filled navy header band with thin row rules, zebra shading and no frame anywhere, and Tab.2 merges each first-class metric over its block (IOL and SED five rows, CD five, TQ four, EDL three) with two cells spanning the whole right half. Tab.1 breaks across pages 5-6 without repeating its header and cuts one row in half, and its own introducing sentence breaks the same way ("...the weight composition are" ends page 10, "shown as below." opens page 11). Table records three cross-reference faults: section 3.5.2 cites "fig.4" for the standard that Figure 5 draws, section 7.2 cites "Fig.8" (the SVM contour) for the population curve of Figure 12, and the two evaluation diagrams are read as rankings of the individual initiatives. Figures 13 and 14 are one five-radar template printed twice, arrow glitch included: the last hop is 2046-2050 and is still labelled "Half decade". Two coverage gaps are declared rather than patched - the two 5x5 judgment matrices at the foot of page 9 print with no rules and no caption, and the appendix MATLAB listing on page 23 is a full-page code block, neither returning a region |
| 136 | P-E-2017-67171-0a99e096 | 22 | 36 | 9 | 10 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; nine printed figures and ten printed tables against 36 measured regions and 17 exclusions - thirteen of the exclusions are pieces of typeset display math (five on p11 for equations 6, 7, 8, five on p12 for 9, 10 and three unnumbered displays, and the F line of 11 on p19), two are table continuations across page turns, two are the outer panels of the three-panel Figure 2 and one is a window that fell on three lines of the reference list. The numbering skips Table 9 outright and prints four different prefixes - "Figure 1" with no stop, "Table1:" with no space, "Table 2:" with a colon, "Fig 2." and "Table 3." onwards with a stop, then "Table10." with no space again - all recorded normatively with the printed form in the row note. Not one exhibit is ever cited by number: every "Fig N" and "Table N" string in the text layer is a caption, the prose points only with "the following table", "the following figure" and "the following list", so all nineteen mention blocks carry an empty style list, a zero count and a null first_page, and the deixis is what gets quoted as the lead sentence (twelve exhibits have one, seven do not). Figure 1 is a colour sunburst - the only "other" family in the paper - with its caption printing 6 pt below the box and overhanging the right text margin by 26 pt; Figures 4, 5 and 6 are three vector panels whose captions interleave line by line in the text layer, so all three are typed from the crop; Figures 3 and 7 are the two three-dimensional axes boxes, Fig 7 spelling Wellington as "Willton" inside the drawing while the caption spells it correctly. All ten tables use the same full grid - outer frame, a rule between every column and every row, no booktabs anywhere and not one zebra-striped table - and seven of the ten merge cells: Table 1 merges its first column over nine rows and each stage cell over three, Table 2 merges the Expression cell over four, Table 5 and Table 6 merge the SGI row's three value columns into one, Table 11 merges each SGI value across all three value columns, and Table10's header merges "Ranking" over two rows and each city over two columns. Three tables break across a page turn and none repeats a header: Table 6 closes p13 with a bottom rule that makes its two-row half look self-terminating, Table10 prints two header rows on p17 and eight body rows on p18, and Table 1 is worse - its caption and header row sit on p6, which returns no region at all, so the grid is measured from its second line down and the header is a declared gap. Every equation number in the paper prints outside the box that measured its equation, p12's box for equation 10 cuts the closing bracket of the final column vector, and three display equations - two on p11 and one at the foot of p12 - have no box at all |
| 137 | P-E-2017-68242-753e0037 | 22 | 23 | 10 | 10 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; ten printed figures and nine printed tables against 23 measured regions and 3 exclusions (the right panel of Figure 7, the p16 continuation of Table 7, the right panel of Figure 8). Nine of the ten figures are drawings rather than plots: Figures 1, 3, 4 and 5 are one three-circle Venn template reused once per section that introduces a component set, with every circle label printed inside its circle and a single leader-line annotation in the upper right - recorded as family `other`, because that annotation keys no colour and repeats no entry, so all four record `legend: none` even though they look keyed; Figures 2 and 10 are box-and-arrow schematic flows; only the radar (Figure 6), the two 3-D column blocks (Figure 7) and the bar pair (Figure 8) and the sensitivity curve (Figure 9) carry axes. Caption side splits by exhibit type and never mixes: all ten figure captions print under the artwork, all ten table captions over the grid, and the p5 variable glossary prints with no caption and no number at all (`caption_source: none`, every caption field a placeholder). The numbering splinters four ways - `Figure1.` to `Figure4.` glue the number to the title, `Figure 5.` spaces it and keeps the stop, `Figure 6` and `Figure 7` space it and drop the stop, `Figure 8.` to `Figure 10.` return to the stop, the four indicator tables carry a stop and Tables 5-9 drop it - and one citation glues its number to the word (`table7`). The prose cites every numbered exhibit once except four: Figure 2 and Figure 9 are never cited by number (deixis only, like the predecessor paper's whole set) and Tables 2, 3 and 4 are cited a second time together in one sentence on p12 (`Refer to Table 2, Table 3 and Table 4`), the only bundled cross-reference in the paper. Figure 10 is announced seven pages before it prints (`More intuitive flow refers to figure 10(Appendix)` on p15, the drawing alone on the appendix page p22). The three indicator grids (Tables 2, 3, 4) share one grouped layout - an outer metric cell spanning every data row, a group cell and its code spanning each block - and all the colour in this paper is column and block tint, not one row-striped table in the ten. Rule styles: verticals everywhere in Tables 2, 3, 4, 6, 7 and the glossary, verticals inside the two header rows only in Table 5, a frame with per-row rules and partial verticals in Table 1, and booktabs in Tables 8 and 9, the rank table ending with no closing rule. Table 7 breaks p15 into p16 with no header repeat. Two half-measured exhibits and one declared gap: Figure 7 and Figure 8 are two measured boxes each and one row per figure carries one panel, and Table 8's two stacked city blocks return a region for the Anchorage block only, so the Wellington header and its three 4-dp rows are a declared gap rather than a second table |
| 138 | P-E-2017-71672-f2a1a712 | 23 | 5 | 0 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; five printed tables and not one figure - the first paper in the lane whose figure list is empty, so every geometry field in the schema goes unused and the whole record is the table half. The five regions are Tables 1-5 on pp9, 11, 14, 17 and 18, each a LaTeX float with its caption printed BELOW the grid and numbered with a colon (`Table 1:` through `Table 5:`), the only numbering form in the paper - the exact inverse of the sibling paper one row up, whose tables all captioned above, which is the cleanest evidence yet that caption side is decided per paper and not per exhibit type. All five grids are boxed identically: top rule, a doubled rule under the header, a rule between every body row, a closing rule at the foot, and verticals at every cell boundary; none is shaded, so the paper has no zebra striping and no coloured cell anywhere. Four of the five are one template four times - a two-column `Metric / Value` grid of twelve rows (a one-row header, `P1`-`P10`, then `L`) whose L row is ruled off from the ten principle rows and set in italic rather than bold - for Boulder current (0.7753), Canberra current (0.5882), Boulder proposed (0.8338) and Canberra proposed (0.7443). Only Table 5 differs: a five-column grid under a two-tier header (`Initiative / Boulder / Canberra` over `L and ΔL`), five body rows A-E, merged city cells, and the paper's only decimal-aligned figures; it is also the only grid wider than a narrow centred block (about half the text width against 0.14 of the page for the four metric grids). Four of the five print a page after the sentence announcing them (pp8, 10 and 17 for pp9, 11 and 18) and the two that print on their own page are the two proposed-plan grids, but no table breaks across a page turn, so float displacement and table continuation are independent here. Citation grammar is fixed: each table named exactly once, always by number, twice as `Table N summarizes ...` with the table as subject and three times as `... are summarized in Table N`. Captions are 19-20 words, single sentences, nominal phrases with no verb, stating no unit, no condition and no conclusion; not one grid prints a note line. Two extraction artefacts are declared rather than patched: the p14 text layer drops Table 3's P7 value and the p17 layer drops Table 4's P5 value, so each reads as a one-row misalignment, but the raster prints every value on its label's row - the only misalignment this paper has is in the text layer |
| 139 | P-F-2017-64486-62f12f04 | 34 | 33 | 25 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 33 measured regions = 25 figures + 5 tables + 3 exclusions. Caption side repeats 138's split and inverts it: all 25 figure captions print under their artwork, all 5 table captions over their grid, and the paper uses one numbering form only, `Figure N:` and `Table N:`, number then colon then space. The exhibits are tool exports, not figures: nine of the twenty-five are histograms (Figures 4-11 as one 4x2 block whose y ticks print at about 4 pt, plus Figure 23), four are node-link diagrams (1, 13, 18, 22), two are schematics (3, 16), Figure 2 is a word cloud and the remaining five are spreadsheet and plotting defaults (14, 15, 19, 20, 21); only Figure 12 packs unlike content together - a spreadsheet capture, a flowchart and eight lettered plots in one frame, so its panel count comes from the caption's `(a)`-`(h)` enumeration rather than from the boxes on the page. Figure 1 is a Word hierarchy still carrying eleven blue text-selection highlights and two coloured dots that key nothing; Figure 3 still shows its editor grid; Figure 15 keeps a leftover `net_domestic_product` text box and a clipped `wage` label; Figure 19 prints `x 10^000` on one axis and `x 10000` on the other; Figure 21 mixes a decimal comma with a point in adjacent y ticks; Figures 24 and 25 misspell GDP as `GPD($)`. Legends are rare and inconsistent: inside the frame on 12, 19, 24 and 25, above the plot on 15, and none on the other twenty, including the eight-panel block that needs one most. Eleven captions are typed from the crop because p11's four pairs, p15's pair and p17's pair print interleaved across the two columns they sit under, which also breaks the printed words `educa-tional` and `dia-gram`; the text-layer forms that failed are kept in the row notes. Cross-references: Figures 10 and 11 are discussed in a sentence that never names them, Figures 14 and 16 are never cited at all, Figure 18 is announced two pages early, Figure 23 a page late, and p16 calls the class-transition chart `Table 5` while Table 5 is the income grid printed under that sentence. Tables: 3 booktabs (1, 4, 8) and 2 stub-ruled class grids (5, 6); no zebra striping anywhere; only Table 8 merges cells and only it carries two header rows, while Table 6 has none so its leading block-label row is counted as the header; only Table 4 aligns on a decimal point, and units are handled three different ways - a dedicated Unit column in Table 1, `Income($)` inside Table 5's stub, and `m * 10^n` in every cell of Table 8. Three printed tables are declared gaps, not patched: Tables 2 and 3 at the top of p9 return no region though Table 4 at the foot of the same page does, and Table 7 on p20 returns none. Three regions are excluded as `not-an-exhibit`: the ICM summary-sheet control block on p1 and the two MATLAB code slabs on pp27 and 34, whose interior pages 28-33 print the same 291 glyph paths each and return no region at all |

Paper 2 was recorded twice: the first pass, before rule change 6, reported `tables = 0`
while the paper prints Tables 1–15. The recount finds 14 counted tables plus 5 continuations
excluded as `split-across-pages`. Every counted table has its own caption line above it and
every continuation has none — that check is now part of the per-paper review.

Paper 4 needed **no** geometry rule change, but it exposed a different problem the
geometry cannot solve: nine of its eighteen measured regions are display equations
typeset as vector paths (pages 7, 8, 9 ×2, 10 ×2, 12, 13, 17). They measure 180–290 pt
wide and 30–60 pt tall, which is indistinguishable from a small plot, so the extractor
counts them. They are recorded as `excluded / not-an-exhibit`, not dropped and not
widened into `other`. No geometry rule was added for them, because no verified
discriminator exists — an equation and a small chart differ in what the paths spell,
not in their bbox. This is a known over-fire class to report in the census findings,
not something to patch speculatively.

Paper 5 also needed no rule change: twelve raster blocks, twelve captions, one exhibit
per block. Two properties of the paper are worth keeping in mind for later papers
without changing any code. First, its captions sit **below** the graphic, so a caption
has to be matched to the region directly above its line, not below; the geometry pass
already records the nearest line in both directions. Second, six of the twelve exhibits
are blocky rainbow probability grids carrying a node-link or dot overlay on top. The
overlay is named in each note, and the family stays `heatmap-or-contour` — an overlay
does not make an exhibit `composite-panel`, which the vocabulary reserves for two or more
sub-plots of different families.

Paper 6 also needed no rule change, and it is the first paper to exercise three parts of
the vocabulary at once:

- **First `other`.** Page 27 is a dendrogram: a linkage tree with leaf indices on x and
  `Gold Distance` on y. `node-link-network` would be a wrong label for it, because it is
  not a graph of entities and relations, and nothing in the closed set covers it. It is
  recorded as `other` with `other_note` naming the shape, per the vocabulary rule.
- **A printed table the rule engine could not see.** Page 37 prints a three-column
  `Offender / kappa-bar_S / kappa_S` table with vertical rules. Rule 6 only groups
  *page-wide* horizontal rules, and this table's rules are column-width, so the table
  arrived as an ordinary vector cluster. It is recorded as `table-grid` on the strength
  of the crop, not of the geometry. This is the mirror of paper 2 (rules but no figure
  code) and belongs in the findings: `table-grid` counting must be caption/visual, not
  rule-based.
- **Rasterised label text inside a flow chart.** Page 17's flow chart embeds its label
  lines as six tiny images, and page 26's embeds one boxed label. They measure as
  separate regions but are parts of the chart, so they are excluded as `in-body-diagram`
  rather than counted as six exhibits.

Paper 7 needed no rule change either, and it is the case that shows why the table code has
to stay visual: both its tables (pages 9 and 20) are set as ordinary vector text with no
page-wide rule at all, so rule 6 cannot see them, yet both are plainly tables. Two other
shapes recur: a five-panel figure (page 21, panels a–e) arrives as five measured regions
and is counted as five items, and one panel (page 24 top) is an embedded hill-shaded
basemap, recorded `map-or-plan-view` on the strength of its own drawing while the panel
below it is a heat map.

Paper 8 needed no rule change: thirty-seven measured regions, of which twenty are lettered
probability panels (a)–(t) on pages 22–32, each its own region and its own item. Three
pages measure as regions but are typeset program listings, not exhibits, and are excluded
`not-an-exhibit`; a code listing has no drawing at all, so no geometry rule can catch it.
Two tables are counted where the paper prints data, one numbered (page 25) and one not
(page 27), which confirms the earlier finding that `table-grid` has to be decided from the
page and not from a caption number. None of the twenty panels carries a basemap — they are
plain longitude/latitude frames with a colour raster — so none is recorded as a map.

Paper 9 needed no rule change, and it is the first paper where a **known under-count**
survives into the record. Page 16 prints two tables, Table 5 and Table 6, separated by
prose; only Table 5's header-and-body band was measured, because its rules span 251 pt of
a 612 pt page and rule 6 only groups rules wider than half the page. The record counts one
table there and says so in the note. Widening rule 6 to column-width rules was rejected:
a plot frame is also a column-width rule set, so the change would trade one missed table
for an unknown number of fake ones. The gap is reported, not patched.

Two other shapes on this paper: page 14 is five scatter sub-plots of the same family with
one caption, recorded as `scatter` with `panel_count 5`; and none of the jeopardy-surface
panels has a basemap or a 3D mesh, so they are `heatmap-or-contour`, not `surface-or-3D`
and not `map-or-plan-view`.

Paper 10 closes the ten-paper run. No rule change again: six of its thirteen regions are
printed tables and only three are exhibits. Its flow chart rasterises its own labels as
per-word images, so four regions inside it are excluded as parts of the chart; its two
charts are Excel-style figures with a data grid attached under the axis, counted once each
as `line` and `bar`, not as tables.

Papers 11–17 needed **no** geometry rule change either — no entry was added to the rule
list above, and every rule recorded on those papers cites an exhibit field already in the
schema. What they did exercise is caption and table attribution, which geometry cannot
decide:

- **Paper 12** keeps Figures 3–6 under §3.1 / §3.2, which are printed but absent from the
  heading index, so `section_path` falls back to the unnumbered form and the two titles are
  copied from the text layer.
- **Paper 13** is the mirror of paper 4: Figures 1, 3 and 5 are *declared and cited* and
  have no measured region at all, because their bodies are typeset text and equation
  glyphs. They are recorded as declared-but-unmeasured gaps rather than forced into a
  region. Only three regions in the whole paper are exhibits.
- **Paper 14** carries four exhibits the teams numbered as figures that are printed tables
  (Figures 3, 11, 13, 18). They stay in the figure block as `table-as-figure`, because the
  table block is for printed tables the paper itself calls tables.
- **Paper 15** adds two uncaptioned body tables to twelve figures, and page 9's single
  region holds two stacked tables (a six-column results grid plus a two-column key) —
  counted once, because they were measured as one region.
- **Paper 16** measures the panel pairs of Figures 7, 8, 9 and 17 as separate regions
  sharing one caption, and its captions are set `Fig N:` with no period. On page 19 two
  captions are set side by side and the text layer interleaves them line by line, so only
  the first line of each is quotable and only that line is quoted.

**Paper 17** is the densest so far and the one that took the most hand work: 68 measured
regions, 59 figure items, 3 tables, 6 excluded, unaccounted 0. Three shapes recur:

- **A sketch sequence that crosses a page break.** Figure 11 is three sketches — the
  caption prints under the second sketch on p13 — so it is counted once at p13 with
  `panel_count 3`, and the p12 and p13 sketches without the caption are excluded as
  `fragment-of-other`.
- **Panel blocks that cross a page break.** Figures 25 and 30 each run over two pages. Each
  measured panel is its own item and the shared caption is quoted on the first panel;
  where the `Figure N` string on the earlier page is a *body mention* rather than a
  printed caption (p32 for Figure 30), that panel records `caption_source: none` instead of
  quoting prose as a caption.
- **A table that continues across a page break.** The parameter list is counted once, at
  p3 with `continued: true`, and its p4 continuation is excluded as `split-across-pages`.

Three small "Default Values" grids print no header row at all. `record.py` requires
`header_rows >= 1`, so forcing them into `table-grid` would mean inventing a header. They
are recorded as `table-as-figure` items with `caption_source: none` and a note saying the
header is absent — the grid is still described faithfully, and no header is fabricated.

Cost note: five of its 34 pages carry ~46 000 vector paths each. `cluster()` spends
82–163 s on each of them, so a single `layout` run or `check.py` on this paper takes about
twelve minutes. That is expected cost for dense vector pages, not a hang; the grid fix
above is what keeps it at minutes rather than quadratic.

**Paper 18** is the first paper whose *heading index* had to be rebuilt, and it adds one new
geometry shape without a rule change: 29 measured regions resolve to 15 figure items, 5
tables and 9 excluded regions, unaccounted 0.

- **Two Algorithm boxes were invisible until the `fig_extract` rule-span fix.** The Algorithm
  2 "Main Network Generation Algorithm" box on p18 and the Algorithm 4 "Assign Channels" box
  on p21 print inside ruled frames whose top and bottom rules sit farther apart than
  `TABLE_GAP_PT`; the old detector dropped the span for being thinner than `MIN_SIDE_PT` and
  only the header rules of Algorithms 1 and 3 on pp. 9 and 20 ever surfaced. All four are
  pseudocode, not data grids, so all four are excluded `not-an-exhibit`.

- **Heading index unusable.** `context_extract` returns the table of contents (pages 2-3) as
  headings, and on p21 four rows of the channel table come back as headings named `2 B/A'`,
  `3 C/B'` and so on. The extracted path therefore put Table 1 under §5.3 Coverage when its
  printed position is §5.1, and put Figure 2 under §4.4 when the heading above it is §4.3.
  The record places every exhibit by finding its heading's printed y on the page, so the
  path is the printed one. This is a lane-tool observation, not a paper quirk: any paper
  with a contents page can hit it.
- **A raster drawn inside a vector frame.** Figure 1 is six panels: five vector frames of
  two-square plots each, filled by a pasted-in density image, plus one bare raster panel.
  The frame is the exhibit and the image inside it is a fragment, so panels (a)-(b), (c)-(d)
  and (e) are one item each even where two measured regions cover them; panel (e) is measured
  twice (a vector bbox with a nested raster bbox) and the inner one is excluded as the same
  plot. The lone panel (f), the real population grid, is its own item — read as a coarse
  density field, `heatmap-or-contour`, not as a photograph.
- **Caption ending in body prose.** Tables 1 and 4 have captions that run into the next
  sentence in the text layer ("...constructing the net- work" then body text; "...distribu-
  tions" then "was valid across..."). Only the printed caption is quoted; the record states
  where it stops.
- **Two algorithm listings.** p9 and p20 measure only the rule and header line of
  `Algorithm 1` / `Algorithm 3`, because their bodies are ordinary text. Excluded as
  `not-an-exhibit`, the class paper 8 established for program listings.

**Paper 19** is the largest page count so far (51) and the first paper with figures the
geometry pass could not measure at all. 27 measured regions resolve to 22 figure items and 5
tables, unaccounted 0, and 24 numbered figures exist in print.

- **Two declared figures carry no measured region.** Figures 3 and 9 ("Surface Plot of Users",
  p15 and p19) were pasted in as a stack of twelve 17 pt horizontal image strips plus a 4 pt
  tail. `fig_extract` drops any box with a side under 25 pt, so nothing survives to record
  against, and record.py refuses a bbox the tool never measured. They are left unresolved and
  named here rather than given invented geometry. This is the extractor's only observed blind
  spot so far: a tiled raster pasted strip by strip.
- **Placement plots are maps, not scatter.** Sixteen figures draw a -40..40 Mile frame with a
  grey user field, red and green repeater dots and coverage circles. They read like scatter
  plots, but both axes are titled Miles and the circles are drawn in that coordinate frame, so
  the family is map-or-plan-view. Four parity diagrams (signed circles joined by thin links)
  are node-link-network, and two flow charts are flowchart-or-schematic.
- **Appendix A reprints.** Pages 29-35 reprint seven body figures at full page as Figures
  18-24, each with its own caption. They are separate exhibits by the paper's own numbering,
  so they are recorded separately even though the artwork repeats Figures 4, 6, 7, 10, 12, 13
  and 15. Their bboxes bleed past the page (x from -50.4 to 662.4 pt on p29), which made the
  standard crop helper abort at the render bounds; the proxies were built by clamping the crop
  to the rendered page.
- **Caption strings and prose references.** Two captions carry no full stop, so the extracted
  caption string has the next body sentence glued on (Figure 7 on p18, Figure 17 on p25); the
  record quotes the printed caption line only. Only Figures 1 and 2 are ever referred to in
  prose, so the other twenty items honestly carry `lead_pattern: none`.
- **Table style.** All five tables here are full boxes (every row ruled, both columns
  separated), not three-line booktabs: three uncaptioned two-column parameter glossaries and
  two 4x3 sensitivity grids.

**Paper 20** is the first with no table worth the name and the first whose captions break
every line convention: 31 measured regions resolve to 28 figure items and 3 excluded program
listings, unaccounted 0, out of 15 numbered figures.

- **Captions printed inline.** Figure 2's caption sits at the end of a prose line ("... we only
  Figure 2: Circles of radii 40 and 10."), Figure 3's two panels each carry their own inline
  label above a caption printed under the pair, and Figure 10's caption is split over three
  indented lines with a hyphen break ("distribu- tion"). A line-anchored caption finder misses
  all three, so the fifteen captions are typed from the text layer and each is verified as a
  verbatim substring of its page before the record is written.
- **One more unmeasurable figure.** Figure 1 (p6) is a text table of UK repeater channels with
  three thin rules and no image block, so nothing clears the extractor's 25 pt minimum side and
  there is no region to record against. Unresolved, as with paper 19's Figures 3 and 9.
- **Family by axis title.** Seventeen figures are point clouds with filled coverage discs, and
  every one of them has unitless -40..40 axes: family `scatter`. Paper 19's placement plots are
  the same marker vocabulary but carry "Miles" axis titles, which is what makes them
  map-or-plan-view. That axis-title test is now the stated rule separating the two.
- **Program listings.** Pages 14, 17 and 19 carry `Program 1-3` blocks (ruled title bar plus
  parameter definitions), excluded as `not-an-exhibit`; page 19 prints one directly above the
  Figure 8 panels, so a page can mix listings and figures.
- **One figure, three regions.** Figures 8, 9, 11 and 13 are three panels each and Figures 12,
  14 and 15 two each; every panel is a separate measured region recorded as its own item that
  shares the figure's caption.

**Paper 21** is the first paper whose *tables* dominate the page count: 54 measured regions
resolve to 15 figure items, 10 tables and 29 excluded regions, unaccounted 0, out of 15
numbered figures and 10 numbered tables.

- **Long tables, one record each.** Table 4 prints as ten narrow horizontal strips (p17
  r2-r9, p18 r1-r2) because its rules are column-width inside two side-by-side blocks; the
  first strip carries the column headings and is the table, the other nine are excluded as
  `split-across-pages`. Tables 2, 6, 8, 9 and 10 continue the same way, each counted once on
  its caption-bearing region with `continued: true`, and 17 further regions excluded.
- **Table cells measured as regions.** The geometry pass sees every hexagon thumbnail pasted
  into Table 2's diagram column as its own small raster (p14 r2-r4, p15 r2-r9), so eleven
  regions inside a recorded table are excluded as `fragment-of-other` rather than counted.
- **Family split on the placement drawings.** Figures 4, 6, 7 and 11 are point markers on a
  unitless -40..40 frame: `scatter`, per paper 20's axis-title test. Figures 5 and 12 fill the
  same frame with unfilled Voronoi polygon cells: `map-or-plan-view`, because the ink is a
  planar subdivision and no marker vocabulary is in play. Figures 8-10 are labelled nodes with
  drawn edges (`node-link-network`), and Figures 2, 3 and 1 are hexagon geometry
  (`flowchart-or-schematic`).
- **Caption reconstruction.** Figure 14's caption is set in three interleaved column pieces
  ("... obtained by the / ve solution. The red and black points correspond to the case of /
  proposed algorithm and the Naï / N=10000 and N=1000 ..."), so only the short contiguous run
  is quotable. Figure 15's caption is printed at the top of the *next* page (p36); it is quoted
  for the p35 raster and recorded with `position: below`.
- **False headings.** Pages 19-23 return their own axis tick numbers as headings ("0 R1 R6",
  "20 R8 R11", "30 Rp4"). Section paths are taken from the printed running order instead, so
  Figures 4-10 sit under §5 Algorithm.
- **One display equation.** p34 measures a square-root formula split out of its paragraph and
  is excluded `not-an-exhibit`, the class paper 4 established.

**Paper 22** is the first paper where every measured region resolves to an exhibit with nothing
left over: 17 regions become 8 figure items and 9 tables, no exclusions, unaccounted 0, out of
eleven numbered figures and ten numbered tables.

- **Four exhibits unresolved, not fudged.** Figures 5 and 6 (p11), Figure 11 (p19) and Table 6
  (p10) are numbered, cited and printed, but nothing on those pages clears the extractor's
  25 pt minimum side, so they have no bbox and are named in the record's note rather than
  given an invented rectangle. p11 in particular measures only the Table 7 band while its two
  charts occupy the blank text area above the caption.
- **3-D point clouds are scatter.** Figures 2, 3 and 4 are MATLAB `view(3)` boxes holding
  open-circle points: the ink is a marker cloud, no surface is rendered, so the family is
  `scatter` and the note says why `surface-or-3D` does not apply. Family still comes off the
  crop, never off the caption or the surrounding prose, exactly as for the placement drawings
  in paper 21.
- **Two schematics and one graph.** Figure 1 is a z/x/y coordinate sketch of a point source
  and its plume; Figures 8 and 9 are energy-loss chains that carry percentages on the arrows
  (`flowchart-or-schematic`); Figure 10 is the AHP hierarchy with drawn edges between the goal,
  five criteria and four alternatives (`node-link-network`), read off a raster page image.
- **Table rules split the paper.** Nine tables are three-line booktabs with grey bands and no
  vertical rules; only the two AHP matrices (Tables 9 and 10) put a heavy rule between the stub
  column and the matrix. Table 7 is the one unshaded table. Tables 8 and 10 carry two header
  rows because their group labels span two sub-columns.
- **Captions below, uniformly.** Every caption prints under its exhibit. Table 1 is the only
  apparent exception — its title is repeated as a stub above the grid — but the numbered
  caption is the one below, so `position: below` holds for all 17.
- **Section IX has no heading.** "Determining the Weight of Different Electricity Generation"
  is printed on pp. 18-19 but never extracted as a heading; those six exhibits therefore carry
  `section_numbered: false` with the title copied from the text layer. Section paths otherwise
  follow the printed order, including the two pages where a second heading starts mid-page.

**Paper 23** is the sparsest measurement so far: 26 pages, eleven regions, and they resolve to
eight figures and three tables with nothing left over, out of eight numbered figures and five
numbered tables.

- **Table 2.2 surfaced after the `fig_extract` rule-span fix.** The rate-and-capacity constant
  table on p9 (parameter, variable, value, units, ten rows) was dropped by the old detector
  for the same reason as paper 18's algorithm boxes: its header and closing rules are farther
  apart than `TABLE_GAP_PT`. It is now recorded as the third table, which is why the
  "unresolved tables" note above no longer lists Table 2.2.

- **One region per figure.** Figures 3.1-3.5 are the same chart re-plotted for five scenarios,
  so each page contributes exactly one region and the family, legend corner and gridlines
  carry over from the base case. Figures 3.7 and 3.8 stack two charts on p20 and are the
  only page in the paper with two regions.
- **Three tables unresolved.** Tables 0.1 (p3), 2.2 (p9) and 3.2 (p18) are numbered and cited
  but drawn with rules too faint to clear the 25 pt minimum side, so they have no bbox and are
  named in the note. Table 2.2 in particular sits on the same page as the measured Table 2.1
  and still leaves nothing.
- **Caption side splits by family.** Every table caption prints above its grid, every figure
  caption below its exhibit — the first paper in the lane where the two families disagree, so
  `caption.position` is per exhibit rather than per paper.
- **Legend corner is the discriminator.** Figures 3.1-3.5 keep a boxed legend inside the
  bottom-right corner; 3.6 puts its keys beyond the right edge of the axes; 3.7 and 3.8 move
  the legend inside the top-right and top-left corners. Monochrome line styles in 3.1-3.5,
  colour in 3.6-3.8.
- **Two table styles.** Table 2.1 is three-line booktabs with no shading; Table 3.1 is fully
  framed with a vertical rule between every column and ten perturbation rows.
- **Missing heading.** Section 3.1 (the economic sensitivity analysis, cited from p13) never
  appears in the heading index, so Table 3.1 carries the chapter path rather than a fabricated
  subsection.

**Paper 24** prints no captions anywhere. The text layer holds not one `Figure N` or
`Table N` token; the prose only says "the following table" and "are shown below". Nineteen
measured regions resolve to nine figures, nine tables and one excluded legend box, with
nothing unaccounted.

- **Captionless by construction.** Every item carries `caption_source: none` and an empty
  verbatim caption, `mention` carries the null form, and `caption.position` keeps the
  placeholder `below` because a caption that does not exist has no side. One chart is the
  exception: its title is baked into the image raster ("Cellular Automata Model of
  Spreading of Electric Cars Based on Initial Seeding") and is recorded `typed-from-crop`.
- **A pie chart with no class.** The 2009 electricity mix is a pie, and the vocabulary has
  no pie family; it is recorded `other` with an explicit `other_note` rather than forced
  into `bar`, which would misdescribe the ink.
- **One exhibit, two regions.** p15 measures the six-series chart and, separately, the
  legend box hanging beyond the right edge of the axes; the legend is excluded
  `fragment-of-other` so the exhibit counts once.
- **Screenshot as exhibit.** The cellular-automaton grid is a pasted raster with the viewer
  chrome still visible, so it is `photo-or-raster-image` and the six-series seeding chart
  below it is a separate item even though both sit inside one image block.
- **One table block unmeasured.** The "Proportion of Seeds / E in 2060" table at the top of
  p18 has no measured region, and the alpha = 500,000 cost block is split across pp. 18-19
  with only the p19 half measured; both are named in the note.

**Paper 25** (P-C-2011-11893-6a9ea7d9) labels its exhibits `Fig. N` and `Tbl. N`, and the
table half of that is invisible to `context_extract.py`, whose caption pattern knows
`figure|fig|table` but not the abbreviation. Thirty-four measured regions resolve to fifteen
figures, fifteen tables and four excluded fragments, nothing unaccounted.

- **`Tbl.` is a tool blind spot, not a paper quirk.** The page text prints "Tbl. 1" through
  "Tbl. 7" with whitespace as inconsistent as the font ("Tbl. 6" with a space, "Tbl.7"
  without), so all seven table labels were read off the page text by hand and typed into the
  payload. Every other label in this paper was lifted from the ctx dump as usual.
- **Seven printed table numbers, fifteen ruled tables.** Five unlabelled "Notations" blocks
  (p3, p9, p10, p12, p13) are two-column ruled tables with one vertical rule after the
  symbol column, and the constraint table splits across pp. 14-15 with the `Tbl. 6` label
  printed only under the p15 half. The unnumbered blocks are counted as tables; a count of
  "tables" from printed numbers alone would undercount this paper by more than half.
- **A perspective surface among flat charts.** p5 r2 looks like a dense line chart in the
  crop list (26 622 paths), but the axes are P and S with D as the vertical and the ink is a
  wireframe mesh in a receding box, so it is `surface-or-3D` with `three_d: surface-mesh`
  and the three trajectories riding on it are its series.
- **Fourteen series in one key.** p17 r1 puts eta = 0.5 to 4 over six named supply sources;
  the key sits outside at the right and two "Critical Point: eta = 0.85" annotations point
  into the coal and transmission groups. It is the only figure in the paper with an
  outside legend; every other key is boxed inside the frame.
- **Nested regions on p19.** The Fig. 15 composite measures as one region covering the three
  pies, and the three pies plus their five-swatch legend are measured *again* as four
  regions inside that bbox. The composite is the exhibit; the four inner regions are
  excluded `fragment-of-other`.
- **Headings the extractor could not trust.** The paper numbers the ordinary-car chapter
  "2" a second time, and three "headings" in the ctx dump are really figure or table text
  (`2 D(CV)` on p7, `5 Power sector to xc 10` on p15, `56 Critical Point:` on p17). Each
  region is filed under the real heading above it, which moves Fig. 3 into section 5 and
  keeps the p19 pies in the EV sensitivity section rather than in the Conclusion.

**Paper 26** (P-C-2011-8882-54492a1f) is the EV/HEV siting paper for France, USA and
China. Fifty-four measured regions resolve to forty-one items, thirteen tables and no
exclusions, nothing unaccounted.

- **Twenty-six printed figure numbers, forty-one items.** Twelve printed figures are
  three-panel figures, one export per country, and the panels carry no caption of their
  own: the page prints one label run under the row ("Figure 2 Figure 3 Figure 4",
  "Figure 5. Figure 6."). Each panel is a measured block, so it is an item, and its
  caption quotes its own label out of that run.
- **One figure, two measurements.** Fig. 8 is a drawn 24-hour demand curve at the foot of
  p9 plus a raster screenshot of a web chart dropped in beside it; the two blocks are
  recorded separately and the caption is printed at the head of p10, not under the ink.
- **The only bar chart.** The Fig. 13 panels on p14 are eleven dark-blue five-year
  columns per country; every other plotted block in the paper is a connected series.
- **The run-of-numbers blind spot.** `context_extract.py` resolves only the first number of
  a run, so "Figure 9, 10 and 11" yields a mention for Fig. 9 alone and "Figure 23, 24, 25,
  26" for Fig. 23 alone. Figs. 10, 11 and 24 therefore carry a null mention with count 0 —
  the text does name them, the reader does not see it.
- **Headings below the ink.** The p19 parameter block and Fig. 18 are printed above the
  "6.2" heading and Fig. 21 above "6.5", so the ctx dump's last-heading attribution would
  file them one section late; the payload follows the printed order.
- **Two printing faults kept in the quote.** Table 3 is labelled "Tabel 3.", and the Fig.
  13 caption is clipped by the gutter after "in France, USA and".

**Paper 27** (P-C-2011-9089-838e50df) is the "What will Electric Vehicle Bring to the
World?" paper. Twenty-nine measured regions resolve to thirteen figures, fifteen tables and
one excluded strip, nothing unaccounted.

- **A second caption blind spot, worse than `Tbl.`.** Every label here is written
  `Figure.1`, `Table.1` — a full stop *before* the number — so the caption pattern, which
  expects the digits right after the word, matches nothing. The ctx dump reports
  `captions=0` and `mentions=0` and both layers were rebuilt by hand from the page text,
  including the reference counts, using the literal `Figure.N` token with a negative
  lookahead so `Figure.1` does not match inside `Figure.10`.
- **Table 1 runs off the page.** p1 carries the header plus the HEV and PHEV rows, and the
  BEV row is printed alone at the head of p2. That strip is excluded `split-across-pages`;
  the recorded table keeps its three printed rows.
- **`Figure.11` printed twice.** The AHP structure on p14 and the 2020 generation mix on
  p17 both carry that label. Both keep their own caption quote; the duplicate is named in
  the note rather than renumbered.
- **One non-chart family.** p17 r1 is an exploded 3-D doughnut with callout labels, recorded
  as `other` with an `other_note`; everything else is bar, line or box-and-arrow.
- **Captions above the exhibit.** This paper sets every caption above its figure or table,
  the opposite of paper 26, so `caption.position` is `above` throughout.
- **Headings below the ink, again.** p14 carries Table 15 and the savings bar chart above
  its own "2.3" heading and the AHP diagram below it; p5 carries both of its charts above
  "2.1.2". Section paths follow the printed order.

**Paper 28** (P-A-2011-9665-6560aced) is the snowboarding half-pipe design paper. Thirty
measured regions resolve to nineteen figures, four tables and seven exclusions, nothing
unaccounted.

- **The notation table appears only after the `fig_extract` rule-span fix.** p3's "II Symbol
  Definitions" table (symbol and definition, eight rows) was dropped by the old table
  detector because its header and closing rules sit farther apart than `TABLE_GAP_PT`, which
  left the span thinner than `MIN_SIDE_PT`. The region exists in the layout as of the
  2026-10-23 rebuild and is recorded with `numbering: none`; the paper prints no `Table N`
  label for it.
- **Fifteen of the nineteen figures are drawings, not plots.** The half-pipe sections, the
  force and torque diagrams and the two panel sketches are all recorded as
  `flowchart-or-schematic`; only Fig. 7, Fig. 8, Fig. 9 and the four Fig. 15 panels carry
  plotted data and are recorded as `line`. Nothing in the paper prints axis numbers except
  the accelerometer traces and the sensitivity panels, so `printed_numbers` is false
  throughout the schematics.
- **Fig. 15 is one subplot grid, four measured blocks.** Each panel keeps the same printed
  caption and `panel_count: 1`, following the lane's region-level counting convention.
- **Five vector blocks are not exhibits.** pp. 12 and 16 measure display equations as
  7–8 vector paths each (p12 twice, the same equation cut across two lines), and p5 r3 is a
  bulleted glossary whose bullets the vector filter reads as a block. All five are excluded
  `not-an-exhibit`, and the figure numbering closes over the gaps.
- **A raster nested inside its own vector twin.** p5 r1 is the labelled schematic (Entry
  Ramp, Platform, Lip, Vertical, Transition, Wall, Flat) and p5 r2 is a raster of the same
  drawing whose bbox `[146.85, 147.25, 463.35, 358.75]` sits wholly inside r1's
  `[89.85, 116.15, 505.45, 362.15]`. r2 is excluded `duplicate`; r1 is Fig. 1.
- **The appendix table breaks across the page.** Appendix A5's reference-data table carries
  its header and first row at the foot of p29 and the rest at the head of p30, and the p30
  block also holds the head of a second uncaptioned table. Both blocks are excluded
  `split-across-pages`, so the appendix data is counted nowhere rather than half-counted.
- **Captions with a stray space, and captions whose symbols are pictures.** "Figure 7 .The
  relationship of ⟨symbols⟩ and v y" and "Figure 10 .The distilled relationship…" keep the
  printed spacing; the symbols that follow are set as images, so the quotes stop at the
  words the text layer holds. Fig. 5's caption breaks off after "of" for the same reason.
- **Headings below the ink, per page.** p23 opens with Table 2 and its own "7.2" heading
  above the four Fig. 15 panels; p22 carries Fig. 14 under 6.2 and Table 1 under 7.1. Section
  paths follow the printed order rather than the heading stack.

**Paper 29** (P-A-2012-14297-5cb8073e) is the leaf-morphology and tree-modelling paper from
2012. Thirty-nine measured regions resolve to sixteen figures, twelve table blocks and
eleven exclusions, nothing unaccounted.

- **Twelve table blocks, nine printed labels.** Tables 1, 7 and 11 each break over a page
  turn and the second half prints without a caption, so pp. 8, 38 and 41 carry headerless
  continuations. Each continuation keeps the label of the half it belongs to, carries
  `continued: true` and says so in its note. `header_rows` cannot fall below 1 in the
  scheme, so a continuation keeps 1 and the note records that the header sits on the
  previous page.
- **Labels 4 and 10 do not exist.** The printed sequence runs 1, 2, 3, 5, 6, 7, 8, 9, 11.
  Two more label quirks: Tables 2 and 3 use a colon ("Table 2: Computation of Overlapping
  Areas") and the in-text cross-references run one behind the printed labels.
- **Eleven excluded blocks are all illustrations inside a table.** Table 1 holds seven
  plant photographs across its two halves; Tables 2 and 3 hold two leaf-pair diagrams and
  two ray-and-shadow sketches each, drawn inside a cell. Each measures as its own raster
  block and each is a `fragment-of-other`, not a `photo-or-raster-image` exhibit.
- **One region, two printed figures.** p35 measures as a single drawing cluster but prints
  Figure 15 (kei against perimeter, fitted U-curve) and Figure 16 (product against time,
  error bars) stacked in one block. Recorded once as a `line` item with `panel_count: 2`,
  the second figure named in the note; the block cannot be split without inventing geometry.
- **The shape functions are polar plots.** Figs. 4-9 are drawn on polar frames with radial
  and cardinal numbers, so they are `line` with `printed_numbers` true; Figs. 1-3, 11-14 and
  17 have no coordinate frame at all.
- **Fig. 17 is a shaded lattice.** The finite-volume figure is a hexagonal cell lattice with
  value-shaded cells, a dashed red boundary and a numbered hexagon inset acting as the key,
  recorded as `heatmap-or-contour` with `legend: inside`.
- **A misnumber left as printed.** p31's body text refers to "(Figure 1)" while showing the
  round-platform drawing, which is labelled Figure 14 on its own caption; the mention count
  follows the literal token.

**Paper 30** (P-A-2012-14990-e2428f0d) is "A Close Look On Leaves", a 42-page modelling
paper on leaf shape and tree profile. One hundred and three measured regions resolve to
thirty-eight figure items, seventeen printed tables and forty-eight exclusions, nothing
unaccounted.

- **Four printed numbers, fifty-five exhibits.** The paper numbers only Figures 2.1-2.4 and
  prints no table numbers at all, so the census counts measured blocks: 34 photographs and
  drawings, one vector phase diagram, three table photographs as `table-as-figure` and
  seventeen measurable grids `table-grid`.
- **The captions are bare labels, not caption lines.** Each of the four prints simply
  "Figure 2.1" (etc.) at the end of a parameter sentence — "… (refer to figure 2.1) … Figure
  2.1 Where AR stands for the aspect ratio" — so `caption.verbatim` is the label alone and
  `caption.sentences` is 1.
- **A citation with no printed label.** p20 names "figure 3.1" for the leaf/tree pair while
  no caption anywhere prints that number. The reference is recorded as printed and the pair
  stands as two uncaptioned `photo-or-raster-image` items; the gap is named, not filled.
- **The cover is page furniture.** p1 holds eleven rasters (leaf grid poster, clover, autumn
  branch, shamrock tile, sunset silhouette, fisheye canopy, sunburst, loop-symbol tree,
  traced leaf outline, tree with drawn rectangle, maple leaf over construction lines) plus
  the drawn title block. All twelve are excluded — the rasters as `background`, the title
  block as `not-an-exhibit`. The cover is the only page whose non-header regions are all
  excluded; the "leaf outline on axes" tile is cover art too, not a plot of the paper's data.
- **Thirty-six running heads, six pages without one.** The "Team #14990 n / 42" strip is
  402x26 pt at the same coordinates on every measured page. pp. 10, 11, 12, 25, 33 and 34
  print no strip because their top region is a table or a chart, so those pages carry no
  header exclusion.
- **One raster, six panels.** p9-r3 is a single 387x125 pt block holding a row of six
  numbered monochrome leaf photographs, the six leaf types of section 5.2. It is recorded
  once as `composite-panel` with `panel_count: 6` and `panel_layout: "row of 6"`, not as six
  items.
- **Three photographs of tables.** pp29, 30 and 39 measure as rasters whose content is a
  printed table (survival and sequestration rates, and the species lookup). With no
  measurable grid they are recorded as `table-as-figure` items, so the record does not claim
  row and column counts it cannot verify; one of them carries its key line printed beneath.
- **Four headerless table blocks.** The p5 nomenclature table (24 symbol/definition rows),
  the p10-r1 continuation of the p9-r4 comparison grid, the p12-r1 seven-row grid and the
  p33-r1 continuation of the p32-r2 age table all measure without a header row.
  `header_rows` cannot fall below 1, so each keeps 1 and its note states where the header
  really sits; p32-r2's two-level header (Hardwood and Conifer over Slow/Moderate/Fast) is
  the one table with `merged_cells: true`.
- **Rule style splits three ways.** The comparison matrices (p9-r4, p10-r1, p11-r2) and the
  one-row CO2 table (p28-r2) print horizontal rules with a shaded header band and no
  verticals; the formula tables and most grids box every cell; p23-r4 draws no rules at all,
  only band shading.

**Paper 31** (P-A-2012-15065-1cbc0cd9) is "A Vector Tree Model", the 2012 paper that grows
a tree from branch transformation matrices, adds a Sunlight Model and then matches leaf
shape to crown profile. Fifty-three measured regions resolve to forty-eight figure items
and five exclusions, nothing unaccounted.

- **No exhibit in this paper is numbered or captioned.** `context_extract` finds 0 captions
  and 0 mentions across all 29 pages, so every row is uncaptioned, every `mention` block is
  empty with `first_page: null`, and there is no printed-count gap to report: the measured
  blocks are the whole count.
- **The one caption is set inside the figure.** p16 prints "This figure is the detailed
  implementation of poplar tree with Deltoid leaves (numerical discretion is adopted)" inside
  a bordered text box, and that box measures as its own region inside the composite. The
  composite carries the quote, the box is excluded `fragment-of-other`.
- **Six shape glyphs are `other`, not photographs.** The four silhouettes at the head of p6
  (Elliptic, Linear, Deltoid, Palmate) and the two outline pairs on p15-r1 and p15-r2 are
  flat labelled leaf glyphs used as a key, so each carries an `other_note` saying what it is
  rather than being force-fitted into `photo-or-raster-image` or `line`.
- **Two grid illustrations, six measured stages.** p6-r5 to p6-r10 are photographed leaves
  on the printed 0.5 cm grid: bare grid, occupied cells, simulating polygon, twice. They stay
  `photo-or-raster-image` because the ink is a photograph with a vector overlay, and they are
  counted as the six measured blocks the text calls "two illustrations".
- **Rendered scenes, one photograph.** Every computer rendering - the three generated
  profiles, the three earth-orbit figures, the two exposure scenes, the case-study camphor
  and the p23 profile trio - is `surface-or-3D`. The single outdoor photograph of the real
  Cinnamomum camphora on p20-r2 is the only `photo-or-raster-image` tree in the paper.
- **The extractor split one web illustration into four regions.** p8-r1 is the annotated
  "STRUCTURE OF A TREE" plate; r2 (the orange "top" arrow strip), r3 (the root-system band
  carrying the infovisual source credit) and r4 (the root-collar band) all fall inside or
  hard against its bbox and are excluded `fragment-of-other`.
- **One flow chart, one magnified box.** p7-r4 is the printed decision tree (convex? →
  leaf index 3.5 → D/L ratio). p7-r5 is a re-crop of its middle box and is excluded as a
  fragment; both blocks measure because the box text was set apart from the vector frames.
- **The comparison table exists only as a raster.** The p15/p16 profile-by-leaf table with
  the rounded exposure ratios is a picture of a ruled table, so both halves are
  `table-as-figure` items and this paper contributes 0 `table-grid` rows - the grid is not
  measurable.
- **A re-printed artwork counted as a re-print.** p12-r1 repeats the p11-r3 globe-and-loops
  figure verbatim with two blue arrows added, for the circle-A-to-circle-B argument. It is
  recorded as its own item with the re-use named in the note.

**Paper 32** (P-A-2012-16831-ec8f03fd) models leaf shape, light interception and leaf mass
for a tree, and it is the clearest case in the lane of printed numbers that do not correspond
to measured blocks. Fifty-eight measured regions resolve to fifty-four figures and four
table bands, with nothing excluded and nothing unaccounted.

- **Eleven printed numbers, fifteen blocks.** Figures 18, 19 and 21 are each printed twice,
  Figure 23 four times, and Figure 8 is never printed. Fifteen blocks therefore carry a
  number, so a count taken from the caption lines alone is off by four before any table work
  starts.
- **"figure 25." never gets a caption.** The line under the two p33 bar groups reads "Figure
  24. statistics in 4 areas          figure 25. total statistics": lower case, second half of
  one baseline. Both panels are one measured block, recorded as a two-panel `bar` item whose
  note names the second number.
- **A caption can carry two labels on one baseline.** p5 prints "Figure 1. NR" and "Figure 2.
  LEA" side by side under two 99 pt rasters. Each row quotes only its own half of that line;
  quoting the whole line for both would double-count the words of the other figure.
- **The prose names five exhibits.** Only "Figure3", "Figure 4", "Figure 6 and Figure 7" (one
  sentence for two figures) and "Figure 15" appear as references in running text. Every other
  row keeps `first_page: null` rather than treating the caption line as a mention, which is
  why this record has four populated `mention` blocks out of fifty-eight.
- **The leaf-bitmap plate runs over a page break.** p6-r2 to p6-r4 and p7-r1 are four
  measured bands of one plate of labelled `.bmp` thumbnails whose "type 1" to "Type 4"
  headings are spread across the two pages. They are `composite-panel`, each with its own
  grid, and no printed number attaches to any of them.
- **Two labels attach to the same pair of leaf montages.** p9-r3 and p9-r4 are "Type 1" and
  "Type 2" scan grids with no number, while the p10 pair prints "Figure 9. classifying result"
  under both blocks. Figures 6 and 7 are the MATLAB training and regression plots, not the
  montages, so an audit that reads "Figure 6 Figure 7" as the montage labels mis-attributes
  two exhibits.
- **Twenty-eight paths, no measured region, three times.** p13's 48 paths are the tail of
  Table 1, p23's 28 are an unnumbered sensitivity table, and p32's 154 are Tables 6, 7 and 8.
  All nine missing table bodies are named in the record note; none is invented as a row, and
  the four `table-grid` entries are a lower bound on the printed tables.
- **A measured table band is the head of a table, not the table.** Table 1's band holds the
  header and one row out of six; Table 9's holds the header plus the top of one data row;
  Table 5's holds a green fill band and two rows. `continued` is set where the body runs past
  the block, and each note says what is outside it.
- **A verbatim re-print is still its own exhibit.** p19-r1 repeats the p17-r1 curve figure
  under the same number and the same caption, once for the no-petiole case and once for the
  petiole case, each above its own result table. Both are recorded, as with paper 31.

**Paper 33** (P-B-2012-13074-8fc549d2) is the Big Long River scheduling paper from 2012.
Eighteen measured regions resolve to four figure items, eleven counted tables and three
excluded continuations: fifteen exhibits, fifteen printed labels, nothing unaccounted.

- **Every exhibit is numbered "ChartN".** No space, no period, no colon — `Chart1`,
  `Chart15`. `context_extract.py` looked for `Figure`/`Table` and found zero captions and
  zero mentions, so all fifteen labels were read off the crops and then quoted from the
  text layer. `schema.NUMBERINGS` has no "Chart N" value, so every row carries
  `numbering: "none"` and the printed label lives only in `caption.verbatim`. This is the
  concrete case behind the deferred `context_extract` caption-group change.
- **One calendar, four bands, counted once.** Chart10 prints 1 March to 31 August across
  pp. 12-15. The Sun.-Sat. header row is in the p12 band, the caption line under the p15
  band, and pp. 13 and 14 repeat neither. The table is counted on its caption-bearing p15
  band with `header_rows: 1` standing for the header three pages above, and the p12, p13
  and p14 bands are excluded `split-across-pages`, the paper-2 rule rather than the
  paper-29 one.
- **The two p7 exhibits are marked axes, not plots.** Chart4 draws a thick number line
  with filled dots at Start, 1, 26, 51 and two closing formulas; Chart5 generalises it with
  black dots at each `7|Y/7|` boundary, blue triangles between them and a formula pair over
  every block. Nothing is plotted against anything, so both are `flowchart-or-schematic`;
  reading them as `line` would file a symbol diagram as data.
- **The schedule grids carry ellipses in both directions.** Charts 3, 6 and 8 are boxed
  grids with vertical rules, a `Day` column and a row of campsite numbers that both end in
  an ellipsis, so `rows` and `cols` count labelled rows and columns only, and `continued` is
  set on all three because the bracketed cycle is followed by further days inside the band.
- **Chart7 belongs to 5.2.2, not to 5.2.3.** The 26-row route table for the first two days
  prints at the top of p9 above the 5.2.3 heading, but the paragraph that decodes it
  ("In the chart above, in the sign 'I j-k'…") runs above that heading too, so placement
  and use agree.
- **Chart2's caption sits under its tree, Chart10's under its last band.** Fourteen captions
  print below the exhibit; the ambiguity was Chart2, where the caption line falls between the
  tree and the 5.2 heading — the crop shows the line under the drawing.
- **One boxed sensitivity table.** Charts 11, 13, 14 and 15 are horizontal-rule-only numeric
  tables; Chart12, the 27-row trip-type census with merged group cells and three Total rows,
  is the single fully boxed one. Chart13 is three side-by-side column pairs under a two-row
  header, so it records `cols: 6` and `header_rows: 2`.
- **Nothing else floats free.** No page furniture, no watermark raster, no display equation
  measured on this paper; the three exclusions are all Chart10 bands.

**Paper 34** (P-B-2012-13955-a0e5e63c) is the second Big Long River paper in the queue.
Twelve measured regions resolve to seven figure items, four counted tables and one
exclusion: eleven printed numbers, eleven counted exhibits.

- **Four printed figures are printed tables.** Figures 3.1, 4.1, 4.2 and 4.4 are ruled
  numeric grids the authors numbered as figures. The lane rule settles them — a table
  printed as a grid uses `table-grid` even when it is numbered as a figure — so they are
  recorded in the table block and this paper contributes no `table-as-figure` rows.
- **Two captions cross a page turn the other way round.** Figure 2.2's strip prints at the
  foot of p7 and its caption opens p8; Figure 2.3's strip is mid-p8 and its caption is the
  last line of the same page. Quoting each caption from the page that carries it, and
  quoting the whole multi-line sentence rather than its first line, is the difference
  between a caption and a fragment.
- **Figure 2.4's caption sits above it.** The only exhibit in the paper with the caption
  line over the drawing: p9 is a full-page flowchart and "Figure 2.4: Visual depiction of
  scheduling algorithm." is the page's first text line.
- **Three strips, three numbers, three items.** The p7/p8 occupancy strips are one diagram
  form printed three times, which a crop-only audit read as one exhibit split across pages;
  the printed numbers 2.1, 2.2 and 2.3 and their three captions make them three exhibits.
  Each is `flowchart-or-schematic`: ruled two-row strips, colour-filled cells, a
  "Downstream ->" arrow, no axes and no plotted marks.
- **Two two-row headers.** Figures 4.2 and 4.4 carry spanned header and stub cells, so both
  record `header_rows: 2` with `merged_cells: true` — 4.2 as a 5x5 cross-tabulation with a
  spanned "Number of campsites on river, Y", 4.4 with a spanned "Distribution of trip
  lengths, D".
- **Figures 3.2 and 3.3 are one data set, two exhibits.** Both are line plots of the same
  simulation — group location and priority against night — each with four colour-keyed
  series and an outside-right legend, and both carry the in-chart tag "(Figure 3.1)" that
  names the table they came from. The tag is not their number; the numbers 3.2 and 3.3 sit
  under them.
- **Figure 4.3 is the only raster.** A filled contour plot in five colour bands with five
  inline contour labels (3500, 3000, 2500, 2000, 1500), no legend and no colour bar; the
  caption names the ridge along R = 1:1.
- **One region is prose.** p16-r1 measures as a block but holds section 6.1's heading and
  one paragraph about capacity overestimation, nothing drawn, so it is excluded
  `not-an-exhibit` rather than recorded as an `other` figure.

**Paper 35** (P-B-2012-15171-ce229936) is the third Big Long River paper in the queue, 36
pages. Twenty-two measured regions over sixteen pages, and every one of them carries a
printed `Figure N:` caption: twenty-two items, twenty-two numbers, one-to-one, no tables
in the block, no exclusions.

- **The captions are buried in tick numbers.** This paper's plots were exported with the
  in-plot title and both tick runs flattened into the text layer beside the caption line,
  so a caption read to end-of-line reads "Figure 6: F vs. Y (∆ = 7) In this model the
  carrying capacity…". Every caption here is cut out of the page text between the
  `Figure N:` label and the first token of whatever follows it on that page.
- **`Table 1: Parameters` is a declared gap.** The paper numbers it on p5 and the geometry
  pass measures nothing on that page, so it is named in the note and not counted: a table
  with no measured region cannot enter the table block without breaking the accounting.
- **Fourteen of twenty-two are marker clouds.** Figures 1-7 and 9-15 each hold one axes of
  filled navy circles, most carrying short capped error bars, on printed tick frames with
  no legend. `scatter`, not `line` — nothing is joined.
- **Figure 8 is the only bar chart.** One solid bar per campsite on a common zero baseline,
  axis titles `Campsite` and `µ`; the prose reads it as low utilization before mile 20 and
  after mile 90.
- **Figure 16 is drawn art.** The boat-placement schematic: a horizontal river rule from
  "First Launch" to "Final Exit", tick partitions, five triangular raft glyphs, an `x` mark
  with an open hull glyph, three `D` spacing labels and a `δ` arrow. No axes, no scales, so
  `printed_numbers` is false and the family is `flowchart-or-schematic`.
- **The six appendix panels are the line figures.** One axes each, five or six smooth
  probability curves, a heavy 1% cutoff rule, a boxed inside legend keyed `P(fast)` and a
  boxed note giving the river location, site spacing (7.5, 3.75, 1.25 miles) and campsite
  count (29, 59, 99) for that run.
- **Figures 11 and 12 are printed two pages after their introduction.** p18 runs "Figure 11
  shows…" and "Figure 12 shows…" and the plots are on p20, so `lead_pages` would have to be
  2 and the lane records no mention row for them; the ten figures cited within one page
  (4, 5, 7, 8, 9, 10 and 15 from the page before, 13 and 14 read back from p22, and 16 on
  its own page) are recorded.
- **Three plot titles pose as headings.** `context_extract` reports "18 Time Optimization
  (∆X = 6 y = 100)", "80 Minimum Nights for Slow Boat (∆X = 6 y = 100)" and "100 Campsite µ
  (Y=100, ∆X = 6)" as numbered headings; they are in-plot titles and no `section_path`
  uses them.
- **Section paths are parent-and-leaf.** Figures 1 and 2 sit under 5.2.2 Optimizations,
  Figures 3-8 under 5.2.3 Results (the heading prints after them on p13), Figures 9-15
  under 5.3.2 Results, Figure 16 under 5.4 Probability Model, and the appendix six under
  7 Appendix / 7.1 Probabilistic Model.

**Paper 36** (P-B-2012-15417-df1dd905) is the Java paper, 26 pages: the model is a program,
so most of the printed body is source code. Twelve measured regions resolve to four figure
items and eight exclusions, unaccounted 0.

- **Eight regions are typeset listings, not exhibits.** p5 (`generateSchedule()` under a
  printed "Algorithm generateSchedule()." title bar), p7 (the tail of the same listing),
  p9 (`addBoats(int day)`), p10 (`reschedule(Boat boat)`), p17 (the whole of `Boat.java`),
  p19 twice (`Boat.java` cut by the footer, then the opening lines of `River.java`) and p26
  (the driver tail). Paper 8's `not-an-exhibit` class covers program listings, so all eight
  go out of the figure block; the layout pass measures them only because their code text
  draws vector paths.
- **Eight further pages carry code that was never measured.** p6, p18 and p20-p25 print
  `fig_extract` warnings of 163-208 paths and no region, i.e. listing bodies outside the
  pass's rules. They are named in the record note as a declared gap rather than invented.
- **Figures 1 and 2 are two raster images on one baseline.** p8 prints two shaded state
  grids side by side, each a three-column table headed `Site` / `Day k` / `Day k + 1` over
  six site rows, the cells holding raft glyphs with "Priority: n" and "Next desired site:
  n". Each image carries its own number and its own caption paragraph underneath — the
  second one wraps — so they are two items, both `flowchart-or-schematic`, the same call as
  paper 34's occupancy strips.
- **Figure 3 is markers only.** `Graph of Magic Numbers`: blue diamonds over grey
  gridlines, axis titles "Number of rescheduled trips" and "Number of Site (Y)", no legend.
  Two isolated points near Y = 34-35 sit far above the rest; the rest break into two low
  runs split at Y ≈ 42, the period-7 pattern the section names.
- **Figure 4 draws its fit.** Markers plus a smooth fitted quadratic through them, with
  `y = -26.173x^2+66.222x+617.96` and `R^2 = 0.9968` printed inside the frame. A continuous
  curve is present, so the family is `line`; the markers are noted rather than treated as
  the family.
- **Figure 4's caption runs into the prose.** The printed line is "Figure 4: The ratio
  changes, and efficiency increases more trips (because 44 is a magic number for 12 hours
  too) but, not enough to warrant the extra stress for the rowers and motors." and the next
  sentence is body text, so the quote stops at the full stop.
- **The heading index is code.** `context_extract` returns lines like "87 Boat temp =
  nextBoat;" as numbered headings, so all three section paths are unnumbered headings taken
  from the text layer with `section_numbered: false`: Representation of a Schedule (p8),
  Magic Numbers (p11) and Error/Sensitivity Analysis (p13).

**Paper 37** (P-B-2012-15420-8b46b980) records the schedule as a matrix and pictures it,
21 pages. Ten measured regions: eight figure items - three of them single-region composite
panels - and two counted tables, no exclusions.

- **Three composites in one region each.** Figure 5 is a 2x2 grid titled "Bones",
  "Intermediate", "Max" and "Final"; Figures 7 and 8 are a wide "Schedule" panel over a
  "Histogram of Trip Lengths" bar panel and a "Histogram of Campsites Used" line panel. One
  measured block per figure, so one row per figure with `panel_count` 4, 3 and 3 and family
  `composite-panel` rather than one item per panel.
- **Figures 2 and 3 are step diagrams, not tables.** Three day-by-campsite grids labelled
  "step 1", "step 2", "step 3", cells filled red, green and blue for three trips, "Day" over
  the columns and a rotated "Campsite" against the rows, no tick numbers and no legend. The
  crop audit read them as `table-as-figure`; they carry no values, only colour, and paper
  34's occupancy strips set the call, so they are `flowchart-or-schematic` with
  `panel_count: 3`.
- **Two printed grids carry no number.** The p4 vessel-type counts (3x5, quoted inline in
  the assumptions) and the p14 model comparison (23x7, seven blocks of rows split by heavy
  rules) are `table-grid` with `caption_source: none` and an empty caption, since
  `record.py` requires a header row and these grids print one.
- **Captions that run into prose.** Four printed caption lines continue straight into body
  text: Figure 4's descriptive caption stops before the stray "period with 200 campsites",
  Figure 5's before the algorithm's numbered step list, Figure 6's before "This model can be
  extended", Figure 8's before "6 Analysis of Results". Figures 4, 7 and 8 keep the
  descriptive sentences that belong to the caption.
- **Figure 6's colour key is in the caption.** "Blue are Motor Boats. Purple are Oar
  Powered Rubber Rafts" - there is no legend inside the frame, and the in-plot title is
  "Bone Growth with Motors and Oars".
- **Figure 1 is a histogram, not a bar chart.** Binned frequencies with a "Frequency" axis
  against "Distance in Miles", in-plot title "Observed Distance Between Campsites Along 3
  Rivers"; the text uses its collapse to justify uniform spacing.
- **The 3.1 label is not indexable.** p4 prints "3 Assumptions" and "3.1 Distribution of
  Oar-Powered Rubber Rafts to Motor Boats and Trip Lengths" merged in one text-layer line,
  so the vessel table is filed under the numbered parent "3 Assumptions" and the record does
  not claim a 3.1 path.

**Paper 38** (P-B-2012-15878-825774ea) is the cellular-automaton rafting paper, 23 pages.
Twenty measured regions: twelve figure rows for eight printed figures, eight counted tables
for six printed tables, no exclusions.

- **Four figures are really eight panels.** Figures 5 to 8 are each a perspective surface
  printed directly above a flat contour map of the same field, both under one caption. Each
  half is its own measured region, so each figure is recorded twice: the upper row
  `surface-or-3D` with `three_d: surface-mesh` and a vertical colour bar, the lower row
  `heatmap-or-contour` with a boxed swatch key at the upper right instead of a bar. The
  caption is quoted on both rows and sits under the pair.
- **Table 6 is one caption over three grids.** p19 prints three five-by-five frames stacked
  a fifth of a page apart - number of visitors, percentage off schedule, percentage
  rejected - and one `Table 6:` caption under the third. All three are recorded, each as a
  counted `table-grid` carrying the same quoted caption; the record says which band is
  which.
- **Table 6's λ column labels are missing.** Every frame has a stub cell ("Number of
  Visitors", "% Off Schedule", "% Rejected Visitors") beside a header cell holding only the
  symbol λ, spanning the four value columns; the stub column then reads α = 0, 10, 20, 30.
  So the rows are the degradation factor and the columns are four λ settings whose actual
  values are never printed - a merged header cell with no complete column labels.
- **Figure 4 is a movement schematic, not a photograph.** A raster banner of mottled
  photo-textured water with two cartoon boats, two more wooden ones, and two equal-length
  rightward arrows: constant velocity shown as equal displacement. No printed word inside
  the region at all. `flowchart-or-schematic`, the same call as paper 35's raster
  boat-placement schematic, rather than `photo-or-raster-image`.
- **Figure 4's caption is above the exhibit**, the only one in the paper; every other
  caption sits below its region.
- **Two placements disagree with the printed headings.** Figure 2 draws the generalised
  rules of 7.2 but the `7.3 An Ideal Implementation` heading prints between it and its own
  prose, so the placement rule would file it under 7.3; and Table 3 summarises the control
  implementations of 7.4 although section 8's heading prints lower on the same page. Both
  follow use over placement: 7.2 and 7.4.
- **Only two exhibits are cited in running text.** Table 1 is called back to from p10, six
  pages after the p4 grid ("as defined in Table 1"), so its mention carries a negative
  `lead_pages`; Tables 4 and 5 are named together by the single sentence that follows them
  on p14. No figure is ever named in prose - the caption is the only label.
- **Table 2 is the one unframed grid.** Only a rule under the header and a rule between the
  stub and the two data columns; no box, no rules between body rows. Recorded
  `booktabs` against the `boxed` used by the other five.

**Paper 39** (P-C-2012-12218-14ded715) ranks conspirators in a criminal network, 19 pages.
Twelve measured regions: six figure items for six printed figures and six counted tables
out of the seven the paper prints.

- **Half the tables are two blocks printed side by side.** Tables 2, 3, 5, 6 and 7 are laid
  out as two columns of `Name` with the metric beside it, repeated: the left block runs the
  list's first half, the right block the second. `cols` therefore counts the physical grid
  (4 for a `Name`/`CD metric` pair, 6 for `Name`/`Fusion Value`/`Rank`), not the column set.
- **Table 1 is the only fully ruled grid.** Ten rows of `Name | CD metric | Rank` inside a
  complete box, ruled between every row and column, with tied ranks printed once per tie
  group. Every other table has a rule under each block's header, no rules between body rows,
  one rule between the two blocks and a closing rule at the foot.
- **Table 4 was never measured.** p11 prints `Partial Outputs of Centrality Analysis`,
  twenty staff rows against Degree, Closeness and Betweeness, but the layout pass finds no
  region anywhere on p11. It is named in the record note as a declared gap.
- **Figures 1 and 2 are the network pair.** Figure 1 is ten nodes A to J on a dashed ring
  with thin and thick arcs and an inset table of the five `P'` paths; Figure 2 is the
  supergraph, five topic nodes on a pentagon with all ten edges. Both `node-link-network`,
  and both captions are printed on one line, so each quote is cut at the other's marker.
- **Figures 3, 4 and 5 are marker staircases.** One open circle per ranked person against
  `Rank` and `CD Metric`, joined into a staircase, plus a horizontal dashed line drawn at
  the biggest jump — that line is the discriminating cut the caption names. Figure 3 labels
  every point; Figures 4 and 5 label none and carry about forty markers each.
- **Figure 6 is a box diagram, not a graph.** Sub-concept boxes feed a `Concept` frame that
  nests `Major Concept` boxes, joined to `Property` and on to `Sub-property`, with a dashed
  two-way `Range Concepts` arrow. Rectangles and elbow connectors, so
  `flowchart-or-schematic`.
- **Figure 4's caption sits inside a sentence.** p8 reads "the possible conspirators are:
  Elsie, Jean, Alex, Elsie, Figure 4: Discriminating Line for Requirement 1 Paul, Harvey,
  Ulf, ..." — the caption interrupts the list it illustrates, so the quote stops at
  "Paul, Harvey, Ulf".
- **Two placements disagree with the headings.** Figure 4 prints above the `3.2` heading
  while still belonging to requirement 1, and Table 3 with Figure 5 print above the `4.1`
  heading while finishing requirement 2. Both follow use over placement. Table 6 likewise
  prints above `5.2 Text Analysis` and scores the semantic web of 5.1.

**Paper 40** (P-C-2012-13215-607f0f06) fits four ranking models to one network of eighty-two
people, 19 pages. Fifteen measured regions: thirteen figure rows for nine printed figures and
two counted tables out of six printed.

- **Four of the six tables are not measured at all.** Tables 1, 2, 3 and 5 print as bare
  columns of text — a name beside a number, no rules anywhere — so the layout pass finds no
  region for them: on p4, p8, p11 and at the head of p15. Only Table 4 and Table 6 are ruled
  grids and only those two are counted; the four are declared gaps in the record note.
- **Table 4 is transposed.** The header row is `rank | 1 | 2 ... 10` and the four rows under
  it are the metric names `CD`, `CB`, `CC`, `C`, each holding ten names. So the body carries
  no numbers at all and `text_cols` is the full eleven columns.
- **Figure 4 is one caption over two panels printed across a page turn.** The upper panel
  closes p7 with `e(t)` decaying from 4, the zoomed lower panel opens p8 on 0 to 0.15, and
  the caption prints under that lower panel only. Both regions are recorded, both quoting it.
- **Figure 8 is a 2x2 block with no shared vertical scale.** Four bar panels on one rank axis
  read 0-20, 0-0.2, 0-0.015 and 0-1, each with its own truncated axis title, so the four are
  four rows and none claims shared axes.
- **Grey is data in the network figures.** Figure 3's three dashed panels are the same graph
  at `t = 0`, `t = 1` and `t = 2 ... the last condition`, with the grey spreading out of the
  seven black conspirator nodes panel by panel; Figure 6's three panels do the same under
  `d = 0`, `d = 1`, `d = 2`. Neither has an axis, so neither carries printed numbers.
- **The caption form is `Figure. 1`, not `Figure 1.`** The full stop prints after the word on
  every one of the nine figures — `Figure. 1` through `Figure. 9` in the text layer — and only
  Figure 9 continues into a title, `The expanded relationship network`. `Figure 5` and
  `Figure 6` drop the stop. No enum value carries that period-first form, so the numberings
  read `Figure N.` and the oddity is stated in the row notes.
- **Figure 1's legend is outside the plot.** Two series, blue for suspicious messages and red
  for messages with known conspirators, keyed at the right of the frame; the axes themselves
  are untitled, so the prose names them.
- **All five headings are unnumbered.** The paper prints `Introduction`, `Validation` and
  `Strengths and weaknesses` with no numbers, so every `section_path` is an unnumbered
  text-layer heading with `section_numbered` false. Figure 8's four panels and Table 4 sit
  under `Validation`, Figure 9 and Table 6 under `Strengths and weaknesses`.

**Paper 41** (P-C-2012-13855-8ff9127d) propagates suspiciousness through a company's message
network, 19 pages. Fourteen measured regions: ten counted tables, one figure item and three
typeset Algorithm boxes; three of the thirteen printed tables have no measured region.

- **The paper is a table paper with one picture.** Thirteen printed tables against a single
  `node-link-network` drawing, Figure 1, which is the whole 83-node hairball with grey message
  edges, yellow topic-1 edges, red Chris edges and the seven known conspirators filled red.
  Its colour key lives in the citing sentence, not in a legend.
- **Nine of the ten counted tables are block grids.** The same two or four columns are printed
  two to five times side by side and filled down each block in turn, so `cols` counts the
  physical grid: Table 2 is four blocks of `ID | S value` (eight columns), Tables 11 and 12
  are five blocks (ten columns), Table 10 is three blocks of `ID | S | Rank | Change` (twelve
  columns).
- **Two rule styles split the paper.** Tables 2, 3, 6, 9, 11 and 12 are closed boxes with
  vertical rules between every column and no rules between body rows; Tables 1, 5, 7 and 10
  are open-sided with three horizontal rules only, which is `booktabs`.
- **Three printed tables were never measured.** Table 4 (p11, the five senior staff against
  their S values), Table 8 (the head of p15, the From/To message pairs for topic 1) and
  Table 13 (p19, the appendix rank comparison) print as bare text columns with no rules, and
  the layout pass finds no region for them. Tables 5 and 9 fill the measured bands on p11 and
  p15 in their place.
- **Three Algorithm boxes are not exhibits.** p6, p7 and p8 each carry a typeset pseudocode
  box under a printed title bar — `Algorithm 1 Top view of the whole methodology`,
  `Algorithm 2 Si Algorithm for calculating`, `Algorithm 3` — with Initialization and phase
  steps inside. Excluded `not-an-exhibit`, the class paper 8 established for program listings.
- **Table 1 is the only uncited exhibit.** The symbol glossary on p4 closes the definitions
  section with no referring sentence anywhere; every other counted table is named at least
  once, and Table 13 is cited from p13 and twice more from p14 before the appendix prints it.
- **Numbers bunch and the printed precision follows.** Table 10 prints four decimals for the
  whole ranking and nine people land on exactly 1.0000; with both decay rates at 1 (Table 11)
  the list collapses to 1, 0.999999, 0.974359 in the first blocks, so the digits are spent
  where the values crowd together.
- **Every heading is numbered**, so all eleven recorded rows carry a numbered `section_path`
  and `section_numbered` is true — the first paper in a while with no junk heading to route
  around.

**Paper 42** (P-C-2012-14531-6018365f) fits logistic regression and LeaderRank to the same
83-person message network, 20 pages. Twelve measured regions: seven printed figures, four of
the five printed tables and the summary sheet's drawn title block.

- **The summary sheet is drawn, not typeset.** Its half-page title block measures as a region
  on p1 because the title and the `Problem Clarification` band are vector paths. Excluded
  `background` — page furniture, the same class as the cover rasters of paper 30.
- **Two tables are transposed.** Tables 2 and 5 put the people across the columns and the
  labels down the first column: `Name | Dolores | Crystal | ...` over a `Node No.` row and a
  `Probability of conspiracy` row, so each block is three rows tall and six columns wide.
  Table 5 stacks two such blocks, ten rows in all.
- **Table 1 is an adjacency matrix.** The seven known conspirators appear both as the column
  header and as the first column, the top-left cell is blank, and the cells hold the topic
  numbers of the messages between each pair with a star on the conspiratorial ones. Fully
  ruled, every row and every column, which is `boxed`; Table 3 is the other `boxed` grid and
  Tables 2 and 5 are horizontal-rules-only.
- **Table 4 was never measured.** `Partial results of LeaderRank on G'TS` — Yao 2.67, Alex
  2.21, Paul 1.92, Elsie 1.62 — prints at the foot of p15, and Figure 5 fills the only band
  the layout pass finds on that page. Named in the record note as a declared gap.
- **Figure 2 is a target diagram.** Concentric rings ticked 0, 0.25, 0.5, 0.75 and 1 with a
  dashed cross and arrowheads, so a person's possession rate reads as radius: seven blue stars
  (known conspirators) crowd the inner rings, eight red stars (known non-conspirators) sit
  outside. Recorded as `scatter`, which is what it is once the rings are read as a radial axis.
- **Figure 4 is a schematic, not a graph.** Rounded message boxes feed chevron `suspicious
  word` entries inside a bracket labelled `Conspiratorial Dictionary`, and arrows leave the
  bracket for undetermined messages — `flowchart-or-schematic`, with a two-entry legend box
  inside the frame.
- **The text misnumbers Table 1 as `Table 2.1`.** The citing sentence reads "Table 2.1 is the
  topics mentioned between known conspirators", so `mention.style` keeps that spelling and
  the row note says why.
- **Table 5 repeats a row of numbers.** The second block's `Prob. of conspiracy (previous)`
  row prints the first block's five values verbatim under five different names — 0.555, 0.508,
  0.388, 0.316, 0.299 — which reads as a typesetting slip in the paper, not a result. The row
  note says so rather than editing the values.

**Paper 43** — `P-C-2012-15356-6b8f0a28`, the iRank suspicion model and its semantic-network
extension, 20 pp, 15 measured regions on 12 pages.

- **Two exhibits carry the number Figure 7.** The semantic-analysis workflow prints on p15 and
  the infection-cells model on p19, both captioned `Figure 7`, and both are recorded on their
  own row rather than renumbered — the second one's note says it is the repeat.
- **The p4 glossary has no number and no caption.** `Symbol | Definition | Formula` over
  twenty-four symbols, `caption_source: none` with an empty caption, counted as a table.
- **Tables 1 and 3 are two blocks under one title row.** Each grid carries a merged full-width
  row reading `Task 1 Statistics` or `Task 2 Statistics` over two copies of `Sender | Topic |
  Receiver | Count`, so each is one table with `merged_cells: true`, not two. Table 3's in-grid
  title says Task 2 while its printed caption still says "in Task 1"; the caption is quoted as
  printed and the mismatch is in the note.
- **An uncaptioned chart sits beside Table 4.** p12 returns two overlapping regions — the
  `Node # | iR` grid and a paired-bar chart printed to its right — and the chart is uncited by
  any sentence, so it is its own row with an empty caption and an empty mention block.
- **One caption has no colon.** `Figure 3 Abnormal nodes observed by correlation ...`, so its
  numbering reads `Figure N` against `Figure N:` everywhere else.
- **Only Figure 1 is cited in running text** — "In Figure 1, from the total number of
  conversations (left bar)" on p3, a forward citation one page on, giving `lead_pages` -1. The
  other fourteen rows are read through their captions alone.
- **Every figure here is a pasted raster with bare tick marks.** Figures 1, 2 and 4 and the p12
  chart print ticks with no tick numbers, so `printed_numbers` is false on all four even where
  the axis is visible; the two dot clouds (Figures 3 and 5) tag their outlying points with a
  hand-drawn ellipse and a plain-text label — `abnormal nodes` and `leadership` — which is not
  a legend and is recorded under the row note.
- **All four headings are unnumbered** (Summary, Introduction, Assumptions, References), so
  every row routes to `未编号标题 Introduction` with `section_numbered: false`.

**Paper 44** — `P-C-2012-16075-4bbf9219`, ECNAM plus the semantic extension, 22 pp, 20
measured regions on 11 pages against ten printed figure numbers and nine printed table numbers.

- **Two tables print and measure nothing.** Table 1 (`Symbol description`) closes p5 and Table 8
  (`indexes of topic 7, 11, 13`) sits under Figure 8 on p19; both pages report 46 and 53 paths and
  no rectangle, so both are declared gaps and no bbox is invented for either.
- **Table 5 splits over the p15/p16 turn.** The caption and the first half print at the foot of
  p15, the rest at the head of p16; only the p16 half is measured, so that row carries
  `continued` and the note says where the caption prints.
- **Figure 3 and Figure 8 are panel-level rows.** The paper numbers each once but frames the
  panels separately — 3(a) `Original result` and 3(b) `Gretchen is a conspirator`, and three
  topic-layout panels for 7, 11 and 13 — so each framed panel is a row repeating the number,
  following the paper 40 precedent. Figures 4 and 5 are one raster holding two unframed panels
  each and stay one row with `panel_count` 2.
- **Figure 9's scale is unreadable.** The pasted chart prints `/通用格式` on every
  y-axis tick because its typeface is missing, so `printed_numbers` is false there even though
  ticks are drawn; the values are in Table 8 and the prose instead. Its caption also repeats
  Table 8's caption — `indexes of topic 7, 11, 13` — word for word.
- **Figure 6 mixes plot types.** One 2x2 block: three scatters (degree, closeness, betweenness)
  and one bar panel (path length against frequency), so family `composite-panel` rather than
  `scatter`.
- **Table 9 prints seven header labels over rows of six values.** Index, Name, Data, Degree,
  Betweenness, Closeness, Score with 7.8 / 0.24 / 0.10 / 0.04 / 100.00 under them — kept as
  printed, noted in the row.
- **Two tables are `booktabs`, the rest `boxed`.** Tables 7 and 9 print one rule under the
  header and one under the last row with no verticals; Tables 2 to 6 print as closed boxes with
  rules between every row and column.
- **Table 2 and Table 3 are introduced by a bare colon sentence** — "The conspirators identified
  by Fisher Discriminant are:" — and by no numbered citation, so their mention blocks are empty.
  Figure 6 and Figure 7 are the reverse: cited one page *after* they print, giving `lead_pages`
  -1 each.

**Paper 45** — `P-C-2012-17160-8b6c54d2`, the circuit-analogy ranking with the clustering
model, 23 pp, 10 measured regions — and **not one figure in the paper**.

- **Every exhibit is a table.** Six numbered tables and one appendix listing; `family_counts`
  is `table-grid` nine and the item list is empty. This is the first paper in the lane with a
  zero figure count, and the only measured region that is not a table is the displayed
  conductance formula on p10, excluded `in-body-diagram`.
- **The appendix listing has no caption line.** `A Complete Listing of Results` runs over
  p21–p23 as one 82-row table, resumes each page with no header row and carries no caption
  anywhere, so its three fragments have empty captions and `caption_source: none`; the later two
  carry `continued`. Row counts are 33, 42 and 7, which is why the three come to the whole
  roster.
- **Table 3 is the paper's only `booktabs` grid.** Horizontal rules above the group headings,
  under the column headings and under the last row, no verticals — which also makes it the only
  table here that is not a closed box.
- **Tables 4, 5 and 6 are block grids.** Eight, four and two Name/Guilt blocks side by side
  under italic group headings, so `cols` is the physical grid (16, 8, 4) and `merged_cells` is
  true; Table 4's eight blocks repeat the same ten names once per conspirator left out.
- **Table 2 holds phrases, not numbers.** Every cell reads "5 guilty, 2 innocent [7 total]",
  so its numeric column count is zero — the encoder's usual text/numeric split has to follow
  the cell content, not the column position.
- **Captions sit below and run long.** Five of the six are two-sentence statements of purpose
  ("The table below shows whether or not each pair of duplicate names are grouped…"), not
  titles; Table 2's second sentence explains the p2p/p2t/both rows.
- **Five of six tables are cited; Table 6 is not.** Tables 1, 3, 4 and 5 are cited one page
  before they print (`lead_pages` 1), Table 2 on its own page, and Table 6 is never named in
  the discussion that follows it.

**Paper 46** — `P-A-2013-20559-c8c96095`, the optimal baking-pan algorithm (lattice packing,
a heat model fitted to a calorimetry experiment, an efficiency sweep), 16 pp, 26 unique measured
regions out of 5624 raw ones.

- **One page paints the same tile five thousand times.** Page 2 is not an exhibit page: it is a
  parody advertisement for "Polythermal Bakeware", live typeset text over wood-grain artwork laid
  down as one raster tile repeated across the lower half. `fig_extract` returns 5614 regions on
  that page and they collapse to twelve distinct 122.8 pt squares, plus four inset panels. Twelve
  are excluded `background` and four `not-an-exhibit`, which is the whole of the paper's exclusion
  budget and the reason the region count had to be deduplicated before it meant anything.
- **Eleven printed figures, ten rows.** Figure 2 prints one caption over two separately measured
  panels standing side by side — squares on the right, hexagons on the left — so it takes a row per
  panel with the printed number repeated and the same caption quoted twice (paper 40 and paper 44
  precedent). The extractor orders the square panel first only because it sits 40 pt higher.
- **Two figures have no region at all.** Figures 5 and 6 are the calorimetry data, printed on p8 as
  typed rows — "Time (min) 0 10 20 30 40 50 / Temperature (C) 22 72 99 102 104 116" — inside the
  body text under a caption line. They are declared gaps, never invented bboxes; the only sentence
  naming them names both at once.
- **A printed grid numbered as a figure.** Figure 7, "Table of tallies for different shapes over
  all tested pan areas", is a real grid — six columns `p | 4 | 6 | 18 | 20 | circle`, twelve rows,
  a vertical rule between every column and a rule under every row, no closing rule at the top,
  bottom or right. It stays in the figure block as `table-as-figure`, because the table list is for
  grids the paper itself calls tables (paper 14 and paper 132 precedent).
- **Four drawings are `other`.** The octagon lattice, the two tessellation panels and the labelled
  hexagon that defines side, apothem and radius are line drawings with a printed pattern and no
  axes, so each carries an `other_note` naming what it is; the geometric definition diagram is the
  case where "schematic" would have implied a process the page does not show.
- **Four sweeps are `line`.** Figures 8–11 plot Efficiency (0.84–1, or 0.75–1 in the last) against
  Polygon Sides 4–20 with markers joined by straight lines, four to seven series each, every legend
  inside the frame and horizontal gridlines only. They differ only in which constant is varied —
  α, β, γ, cρ — which is exactly the sensitivity study the section runs.
- **No numbered headings exist.** The paper sets five printed sub-headings and no numbers anywhere,
  so every `section_path` uses the unnumbered form and `section_kind` is read from the heading's
  job (`model` for the packing and heat sections, `result` for Optimal Shapes, `sensitivity` for the
  sweep).
- **Five figures are never cited by number.** Figures 1, 2, 4 and 7 are named in prose; Figure 3 is
  a definition diagram no sentence points at, and the four efficiency charts are announced by the
  section title rather than by number.

**Paper 47** — `P-A-2013-23004-8dba2d4c`, "The Design of Ultimate Brownie Pan" (a heat model for
polygonal pans, a centre-dot arrangement algorithm, three arrangements tested), 21 pp plus two
advertising sheets, 77 measured regions over 17 pages.

- **Two pages are a brochure, not a paper.** Pages 20 and 21 are the team's own sales sheet —
  "The Ultimate Brownie Pan", product renderings, "Pick From Four Choices or Customize Your Own" —
  and the paper announces them itself on p19: "The authors provided advertising sheets attached at
  the end of the article... See advertising Sheets on Next Two Pages." Their 34 measured regions
  carry no number and no caption anywhere on the page: two page-filling vector frames are excluded
  `background`, the 32 text bands and renderings `not-an-exhibit`. That is two thirds of the
  paper's exclusion budget, spent on pages that are not exhibits.
- **Twenty-three figures, three tables, and no showpiece grids.** Figures 1–23 print as
  `Fig. N` and Tables 3–5 as `Table N`; Tables 1 (Notation) and 2 (Parameters of Standard State)
  print captions but return no measured region and are declared gaps rather than invented bboxes.
  The paper's real results are pictures: a temperature field rendered onto the pan cells
  (Figures 20–22) is the answer, and no grid tabulates it.
- **Not one exhibit is cited by number.** All 28 captions print with a number, and not a single
  sentence in the paper uses one. The prose points by position — "The flow chart of Algorithm is
  listed as follow.", "The figure above shows the temperature distribution of a rectangular pan.",
  "See advertising Sheets on Next Two Pages." Every `mention` block is therefore empty, `count` 0,
  and the citation column cannot be read as "uncited exhibit": the paper simply never names one.
- **Eleven figures are line art, so they are `other`.** Figures 8–17 are polygon lattices,
  dot-centred arrangement patterns, a labelled L-by-W rectangle and two bare-arrow centre-dot
  matrices — no axes scale, no ticks, no values. Each carries an `other_note` naming the drawing.
  Figure 16 is the hard case: it prints two plain arrow axes, but the marks on them are polygon
  cells on a lattice with no scale, so it is not a scatter plot and is not recorded as one.
- **Four exhibits need a judgement, not a caption word.** Figure 1 is a photograph cluster beside
  a wireframe pan drawing and Figure 23 is a line-art strip above two 3-D surfaces, so both are
  `composite-panel` (2 and 3 panels). Figure 7 plots ten markers with one fitted straight line —
  the markers are the observations and the line is the model, so it is `scatter`. Figures 3 and 5
  are MATLAB perspective surfaces with colour bars; Figures 20–22 render the same field onto the
  plate with no axes and no bar, so they are `heatmap-or-contour`, not `surface-or-3D`.
- **Three tables hold pictures in their cells.** Tables 4 and 5 are "All the Arrangements for
  Optimization" — three columns of shape, pattern 1, pattern 2, where the pattern columns are
  thumbnails, so `numeric_cols` is zero. Eight thumbnails come back as their own measured rasters
  inside the table frame and are excluded `fragment-of-other`; the same happens to the eight text
  boxes of the Figure 18 flowchart on p14. All three tables print horizontal rules only.
- **No numbered headings exist.** `Model 1: The Distribution of Heat at the Edges of Polygon` is
  printed only where it shares a line with Figure 1's caption, so every `section_path` uses the
  unnumbered form and `section_kind` is read from the heading's job — `model` for the two models,
  `test` for the arrangement trials, `evaluation` for Strengths and Weaknesses.

**Paper 48** — `P-B-2013-21185-c7f22f59`, a Chinese water-resources strategy paper (demand
forecasting, storage, cross-basin transfer, desalination, pollution control, water saving), 43 pp,
41 measured regions over 26 pages.

- **Nothing in this paper is numbered.** No "Figure 1", no "Table 1", anywhere. Five caption lines
  print as bare `Figure` or `Figure.` with no digit — "Figure China's Nine Watersheds",
  "Figure. China's Three Terrace", "Figure. Six Optimal Water Transfer Routes of China",
  "Figure. Classification of Water Consumption of a Unit GDP (β)". Everything else is announced by
  prose alone ("the following table shows the results", "the figure above"), so nine of the
  seventeen printed tables record `caption_source: none` and every `mention` block is empty. The
  paper is the lane's cleanest case of a citation column that says nothing about whether an
  exhibit is discussed.
- **Seventeen printed tables, two of them across page breaks.** The notation lists
  (`Nomenclatures` p5–p6, `5.2 Terminology` p26, `6.2.3 Terminology` p29) are ruled grids with a
  symbol column and a definition column; the province ranking runs p18–p19 and the province
  numbering runs p22–p23, both recorded `continued` with the note naming where the header prints.
  Three tables draw a full cell grid; the rest print horizontal rules only, and the worked
  Beijing example on p24 draws no rules at all.
- **Two grids are numbered as figures.** The α colour scale on p22 is a screenshot of a
  spreadsheet colour scale — five shaded bands of 31 provinces, α minus its mean — captioned
  "Figure Colored Graph Based on water supply pressure α"; the β table on p33 prints as five
  separately framed blocks, all 31 provinces ranked 0.005079 to 0.176276, under one caption that
  the text later calls "the table above". Both stay in the figure block as `table-as-figure`.
- **Two caption quirks.** The p22 caption is destroyed in the text layer — "Figure Colored Graph
  Based on at r pply pr r α", the watermark cutting the words — so it is typed from the crop
  (`typed-from-crop`) and the gallery row says so. The p33 caption carries a mathematical bold
  beta (U+1D6C3), quoted exactly as printed.
- **Four maps, three of them rasters of other people's cartography.** The nine-watershed map and
  the three-terrace relief map share p20; the α choropleth and the six-transfer-route map reuse
  the same provincial base. None prints a scale value or a colour key of its own: the classes are
  readable only against the p22 grid above them.
- **Two panels-families, not composites.** p11 stacks four single-line charts and p12 stacks three
  dual-axis charts; each is one family in several panels, so both keep `line` with a panel count
  rather than taking `composite-panel`.
- **Two exclusions, and they are equations.** p24 r1 is the objective function
  `z = min{η = Δw/E = min{|Δw_i|,|Δw_j|}/E}` with its constraint bracket, and r2 is the same
  bracket wrapped across the line with the worked value Δw_j = 29.1552. Both are live vector math,
  the two smallest regions on any page in the paper, excluded `in-body-diagram`.
- **One declared gap.** p36 prints two 4×4 AHP judgment matrices (ratios such as 1, 5/6, 5/6, 5/3)
  as 108 vector paths and `fig_extract` measures no region on that page, so the matrices are a
  declared gap; `check.py` names the page in a warning rather than the census inventing a bbox.

**Paper 49** — `P-C-2013-18492-ab739371`, a two-tier communication-network model of global
health (nodes, links, topology, a revised Bayesian belief network, policy simulation), 21 pp,
21 measured regions over 10 pages.

- **Numbering by section, which the enum cannot hold.** Every exhibit is labelled with its
  section prefix — "Figure 3-1", "Figure 3.1.2-1", "Table 3.1.2-1", "Table 3.1.4-1",
  "Figure 3.1.4-1", "Fig. 3.3.5-1", "Figure 3.3.5-1", "Figure 3.4-1", "Table 4.1-1",
  "Figure 4.3-1"…"Figure 4.3-4" — and `NUMBERINGS` knows only the flat "Figure N" forms. All
  twelve records carry `numbering: none` with the label left inside the quoted caption, rather
  than the record silently claiming the paper prints "Figure 1". Nine of them are cited in the
  prose by the same label, so the mention blocks store the literal spellings (`Fig. 3-1`,
  `table 3.1.4-1`, `Fig. 4.3-2`).
- **Four charts are measured twice.** p16's bar chart and the three p17/p18 situation charts
  each produce an outer region (caption line, shadow band, legend) and an inner one (plot area
  only). The page holds one image object in the p16 case and none of the chart's own ink in the
  p17/p18 cases: those pages paint an *empty* frame image over live vector artwork, and the
  extractor opens a box for each. The exhibit is recorded once and the inner box is excluded
  `fragment-of-other` — the lane's first case where the duplicate region is caused by a blank
  raster rather than by a pasted bitmap of the drawing.
- **One map, one graph, and the line between them.** p5 places ring nodes on a western-US state
  map with dashed edges and a PACIFIC OCEAN node; the ink is a geographic partition, so it is
  `map-or-plan-view`. p9's bipartite Bayesian network has no basemap under it, so it is
  `node-link-network`. Both are the same test the lane has used since paper 20.
- **The only extruded chart so far.** p16 draws five 3-D bars (Environment, Resources,
  Population, Industry, "Argiculture") in an embedded ~200 dpi raster inside a vector frame, so
  `three_d: perspective-bars` — the first row in the lane to use that value.
- **A cell grid with no numbers at all.** The p14 "square lattice in 2-dimensions" is 5×5 thin
  vector cells with six filled black, no axes, no labels, no key: `heatmap-or-contour`.
- **Three tables, one rule scheme.** All three print a single internal vertical rule after the
  stub column, no outer verticals, and separate rows by alternating grey fill, so all three are
  `vertical-rules` with `zebra: true`; the p7 index column prints bands ("0~50") and the p9 table
  prints two formula cells ("Vn*3.0", "Vn*0.6"), so no column is numeric end to end.
- **Nine exclusions.** Two prose bands on p7 (bold lead-in words measure as extra paths), three
  bands on p19 (running head plus prose; prose plus equation (18); the edge-betweenness equation
  (19)), and the four duplicate chart boxes.

**Paper 50** — `P-C-2013-21165-17e64d15`, a linked neural-network model of global air quality
(global and local nodes, AQI, fit verification, critical nodes, sensitivity, three case
studies), 19 pp, 17 measured regions over 11 pages.

- **The numbering finally fits.** Every exhibit carries a flat number — `Figure 1` to
  `Figure 10`, `Table 1` to `Table 3` — so the enum holds without a note. Only Figure 1 uses the
  colon form, and only because the page prints `Figure 1: World3 Computer Model Scenario 2 …`.
- **Three tables, three constructions, in one paper.** Table 1 (p4) is a *pasted colour raster*:
  an AQI band grid whose rows are separated by solid fill and white gaps, with no rule strokes at
  all, so `rule_style: no-rules` and `zebra: false` even though the bands are coloured. Table 2
  (p5) is a plain booktabs notation list with two extra heavy rules grouping the symbols. Table 3
  (p8) is a spanner-header grid — `Input` and `Output` over two `Name and Notation` columns each
  — with the paper's only vertical rule. Raster-versus-vector is *not* a reliable table/figure
  predictor here: the raster one is a table and every real figure except the p4 panels is vector.
- **Panels as separate regions, twice.** Figure 2's three panels arrive as three small rasters in
  one row under a single caption that splits them (`(a) (b)` under "The Increasing rates of
  change in human activity", `(c)` under "Global scale changes"); Figures 6 and 7 each print two
  panels as two separately measured regions with identical frames. All stay one family with a
  panel layout rather than becoming `composite-panel`.
- **A caption that oversells the drawing.** Figure 5 is captioned "Identifying the critical
  nodes", but the ink is eighteen glossy columns, one per country, y 0–600, China at about 550 —
  a bar chart, not a node graph. The family follows the ink.
- **Choropleths with no key.** Figure 7's two panels are greyscale world maps on a lat/lon
  graticule, 1970 and 2008; the classes are readable only against the sentence "the darker the
  color, the more serious the pollution". No legend, no scale bar, no colour ramp printed.
- **One artwork printed twice.** Figure 9 (p15, India) is the Figure 6(a) plot reused almost
  pixel for pixel — same curve, same scattered forecast markers, same frame — while Figure 6(b)
  (China) is the well-fitted arc. Both are printed exhibits with their own captions, so both keep
  their rows and the reuse is declared in Figure 9's note.
- **One scale that differs.** The six case-study plots share a 1970–2010 frame with a blue actual
  line, red `+` forecast markers and an outside-right legend, except Figure 10 (Hungary), whose y
  axis runs to 200 where the others stop at 160 — read per region, never assumed from the
  template.
- **No exclusions and one silent exhibit.** Nothing measured here is anything but a figure or a
  table. Figure 4 (stepwise forecast, Belgium) is the only exhibit the prose never names.

**Paper 51** — `P-A-2014-25142-c5c79dc7`, a cellular-automaton freeway study (minimum safe
gap, overtaking probability, keep-right versus unrestricted lanes, danger index, speed-limit
sensitivity, an intelligent-system rule), 34 pp, 29 measured regions over 18 pages.

- **Numbering fits, for the second paper running.** Every exhibit prints a flat number —
  `Figure 1:` through `Figure 18:`, `Table 1:` — so no record needs `numbering: none`. What does
  need care is the *caption*, not the number.
- **Seven captions printed two to a line.** From p16 onward the paper sets its side-by-side
  panels with their captions in two columns on one text line, and each column is cut mid-word:
  `Figure 4: Average Velocity under Different | Figure 5: Average Velocity under Different` on
  one line, `Rules(2 lanes) | Rules(3 lanes )` on the next. No row quotes that line whole. Each
  row quotes the fragment carrying its own figure number and keeps the printed tail — including
  the misprints (`lanes, keep-right)`, `t Rules(3 lanes)`, and Figure 15's tail, which loses its
  closing parenthesis) — in the note.
- **The side-by-side pairs are still separate regions.** Every one of the eleven paired-page
  crops holds exactly one drawing with its own frame; the "two charts in a box" case does not
  occur here. Each panel gets its own row with a `left of pair` / `right of pair` layout, and in
  every pair the left chart takes the earlier figure number: p18 row 1 is Figure 7 left and
  Figure 8 right, p20 row 1 is Figure 12 left and Figure 13 right.
- **Family follows the ink, and the ink alternates.** p18's four density panels, p19's passing
  events, p20's two danger-index panels and p21's two are all grouped or stacked *columns* —
  `bar` — while the velocity panels printed on the same pages are polylines — `line`. Nothing is
  decided from the caption's wording: the p18 axes are even labelled with a bare `D`, which
  Table 1 defines as the danger index, when they plot density per lane.
- **One table, four gaps.** Table 1 (p5) is the notation list: live vector text, header `Symbol |
  Meaning`, eighteen rows, three horizontal rules and no verticals. Tables 2 and 3 (p10, the
  acceleration and deceleration probabilities for fast and slow vehicles) and Tables 4 and 5
  (p23, the same two under the intelligent system) print caption lines and typed cell rows in the
  text layer, but the layout pass measures nothing on either page, so all four are declared gaps
  rather than given invented boxes.
- **One drawing with no y axis title.** Figure 11 counts passing events over five minutes as
  stacked columns — yellow `unrestricted(left)`, red `unrestricted(right)`, blue `keep-right` —
  with a single horizontal legend row inside the upper left and y ticks running 0 to 25000 by
  5000 under no axis title at all. It is the only stacked column chart on the paper.
- **The velocity triangle is not a plot.** Figure 2 draws V0, V1 and the acceleration a as a
  labelled vector triangle with no axes, no ticks and no scale, so it is recorded `other` with an
  `other_note` naming the drawing instead of being forced into `line`.
- **A legend that contradicts the prose.** Figure 14's key names speed limits 29 m/s, 32 m/s and
  38 m/s while the paragraph above says the limit was changed from 32 to 28 and to 36; its
  sibling Figure 15 keys 28/32/36 and matches. Both are recorded as printed — the ink wins, and
  the disagreement is declared rather than reconciled.
- **Ten exclusions, all code.** The appendix prints ten bands of typed MATLAB source (the inflow
  function, the inflow, acceleration, deceleration, urgent-deceleration, overtaking-judgement and
  free-driving blocks, the traffic-flow count, and the whole `Xdensity` function body). None
  carries a number or a caption; all are excluded `not-an-exhibit`.
- **Only three exhibits are named in prose.** `as is shown in the figure 2` on p12 and the p16
  sentence naming figures 4 and 5 (once as `figure 4 and figure 5`, once as `figure 4 and 5`) are
  the whole of the numbered citation in this paper; the other fifteen rows carry empty `mention`
  blocks, introduced by deictic prose or by their captions alone.


**Paper 52** — `P-A-2014-26911-00c95da0`, a coaching-great evaluation model (metric hierarchy,
Google Trends evidence, AHP plus grey-relation/MaxEnt weights, sensitivity and universality
testing), 22 PDF pages, 8 measured regions — every one of them an exhibit.

- **Eight exhibits in twenty-two pages.** Three figure rows and five printed tables, no
  exclusions and nothing to declare as a gap. The paper is prose, equations and references almost
  throughout; the layout pass finds regions on only five pages.
- **Every table is a picture of a table.** All five are pasted rasters: the grid, the blue header
  band and the caption line are all pixels, so no caption text reaches the text layer and all five
  are recorded `caption_source: "typed-from-crop"`. This is the first paper in this run where the
  tables' captions are unreadable to the text layer while the *figures'* captions are perfectly
  readable — so the source is read per exhibit, never from `kind`.
- **Table captions print below their grids.** All five, against the lane's rule that tables
  caption above. Recorded as printed.
- **One table construction, five times.** Solid blue header band with white bold labels,
  alternating light-blue body tints, faint rules between rows and thin vertical rules between the
  columns: `vertical-rules` with `zebra: true` on every row. Nothing here is booktabs, and Table 1
  is not `boxed` — it carries inner verticals like the rest.
- **A weight vector shared across three sports.** Tables 2, 3 and 4 (football, basketball,
  baseball) all begin with the same seven-entry AHP row, `(0.28,0.11,0.25,0.08,0.03,0.20,0.07)`,
  because the subjective weights are common to every sport; only the Maxent&GRC row differs. The
  repetition is real and is recorded rather than deduplicated.
- **Two Google Trends screenshots, no scale.** Figures 1 and 2 are pasted browser captures: one
  thin blue line from 2005 to 2013, three faint horizontal gridlines, no frame, no y axis at all,
  and the peaks lettered A to G and A to N in place with no key anywhere. `legend: none`,
  `printed_numbers: true` only for the x ticks.
- **The one numbered citation is wrong.** p12 reads "… the following Index Hierarchy Relationship
  Figure is displayed in Figure" — the number has simply fallen out — and then "As is vividly
  shown in Figure 2, AHP provides a systematic assessment", which is the hierarchy on that page,
  printed as Figure 3. The mention is recorded on Figure 2 with `lead_pages: -2` (the prose points
  two pages back from where the sentence is printed), and Figure 3's block is left empty with the
  miscitation explained in its note.
- **A hierarchy, not a network.** Figure 3's boxes are labelled rectangles joined by drawn
  arrows, so the family is `flowchart-or-schematic` rather than `node-link-network` — the same
  call this lane makes for every box-and-arrow drawing, and the reason the AHP entry in paper 48's
  table and its narrative sentence read differently.
- **A tight colon.** Table 5 prints `Table 5:Top 5 Women's Volleyball College Coaches` — no space
  after the colon, where Tables 1 to 4 all have one. The quoted caption keeps the raster's
  spacing and its typographic apostrophe.


**Paper 53** — `P-A-2014-29282-f92c8e1b`, the keep-right-except-to-pass traffic-rule paper (a
cellular-automaton freeway simulation, three proposed rules, an AHP evaluation and an
intelligent-driver comparison), 30 PDF pages, 33 measured regions.

- **Thirty-one exhibits and two exclusions.** Twenty-two figure rows and nine printed tables over
  nineteen pages, plus the two summary-sheet regions on page 1 (the control-number form grid and
  the title band), both `not-an-exhibit`. Nothing is unresolved and nothing is declared a gap.
- **Flat colon numbering, and it holds.** `Figure 1:` to `Figure 22:`, `Table 1:` to `Table 9:`.
  Every caption in this paper reaches the text layer, so not one is typed from the crop — the
  opposite of the two papers before it.
- **Dense exhibit pages, empty ones elsewhere.** The bulk sits on four pages: p17 carries Table 1
  and a 2×2 block of plots, p19 and p20 carry the sensitivity grids, p23 and p24 pair a table with
  a plot or with the next table, p28 carries a second 2×2 block. Nine pages hold two or more
  regions each.
- **Figures caption below, tables caption above.** Every figure caption sits under its art and
  every table caption sits over its grid — the lane's normal split, and here the paper agrees with
  it. Pages 17 and 28 print two captions to a line, so each panel takes its own row and quotes the
  fragment carrying its own number.
- **Five `scatter` rows.** Figures 10 to 14 are the paper's only scatter plots: blue data dots read
  off a raster paste with a red fitted curve through them, legend boxed inside at a corner, corner
  varying panel by panel (upper right on Figures 10, 11, 14 and 20; upper left elsewhere).
- **A radar with no family to name it.** Figure 17 compares the four rules as four closed
  polylines on five spokes — TFI, SI, ATSI, USLI, OSLI — with ring gridlines, radial ticks 0 to 1
  along the top spoke and the key set outside the frame at the right. The enum has no radar family,
  so the row is `line` on the lane's precedent (page 9 of `P-A-2022-2209466-5952dd05`) and the
  radar construction is spelled out in `other_note` rather than approximated.
- **Eleven `flowchart-or-schematic` rows.** Two decision flowcharts (Figures 8 and 9, the second a
  sub-flowchart of the first), the paper's roadmap, the freeway schematic and seven drawn road
  strips. Figures 15 and 16 are captioned "a printscreen of simulation" but are drawn strips of
  green bars with a red direction arrow, not screenshots — recorded by what is drawn, with the
  misdescription kept in the note.
- **Figure 18 promises two systems and labels two panels.** The caption reads "RHT and LHT traffic
  systems" while the sub-labels under the panels read "New Rule 2 in LHT" and "New Rule 2 in RHT",
  with the left-hand panel printed first. Two panels, `1x2`, and no legend — the direction cross
  between them is an in-figure annotation.
- **Three tables share one merged construction.** Tables 2, 3 and 4 open with a full-width merged
  row ("p1 = 0.3(original value)", "p2 = 0.7(original value)", "d = 2(original value)") over four
  data rows, with horizontal rules only: `booktabs`, `merged_cells: true`, no zebra anywhere in
  the paper. Table 1 is the one dense grid — a rule after every body row, two internal verticals,
  still no outer side frame — and Tables 5, 6, 8 and 9 carry single or multiple internal verticals
  with no outer sides either.
- **Citations run both ways.** Figures 10 to 13 are captioned on p17 and discussed on p18, and
  Tables 6, 7 and 9, plus Figure 17, are each cited one page *before* the page their grid or art
  prints on. Those blocks carry a negative `lead_pages`. Tables 2, 3 and 4 are never cited by
  number at all: the only pointer is the p19 clause "results are shown in following tables", a
  deictic reference that prints no number, so each of the three records that clause with an empty
  style list and `count: 0`.
- **Faults worth carrying downstream.** Figure 2's caption is corrupted to `overtaking(i¡j)` where
  the art shows the subscripts; Table 1 prints "Traffic flow)" with a stray closing parenthesis and
  lower-cases an index that Table 5 capitalises; Table 9's first column is headed "Traffic Rule"
  over the composite index `EIC`; Table 3 prints `11.6%` to one decimal against two everywhere
  else; Figure 3's caption says "after several transitions" where twenty are plotted; Figures
  6 and 7 are near-duplicate strips.


**Paper 54** — `P-A-2014-29911-ac64b43b`, the double-lane cellular-automaton study of the
keep-right-except-to-pass rule, with a continuum model, a Monte Carlo simulation, an optimal
maximum velocity, three alternative rules and an intelligent-system "median" rule, 40 PDF pages,
53 measured regions.

- **Twenty-nine exhibits and twenty-four exclusions.** Twenty-four figure rows and five printed
  tables over eighteen pages, plus 24 exclusions: the Table 1 tail on p7 and the five Table 5
  bands on p9 (`split-across-pages`), the six Figure 18 label blocks on p27 (`fragment-of-other`),
  and the twelve p32–p40 bands of typed C++ (`not-an-exhibit`). 29 + 24 = 53 exactly, nothing
  unresolved and no declared gaps.
- **A flat stop.** `Figure 1.` to `Figure 22.` and `Table 1.` to `Table 5.`, no sections, no
  `Fig.` and no unnumbered panels, so the stop forms of the enum cover the paper and every
  caption also reaches the text layer — including the four raster figures.
- **Every exhibit captions below its art, tables included.** Tables 1 to 5 each close with their
  caption, the reverse of the lane's habit of captioning tables above. Two of them caption on the
  far side of the page break: Table 1's caption and its asterisk note print on p7 after the four
  tail rows, and Table 5's on p9 after Step 18.
- **Five tables, two of them headerless.** Table 1 is the dense notation grid — a rule under the
  header and between every body row, one full-height inner vertical, no outer frame — and Table 3
  is its three-column cousin with two inner verticals and one merged blank cell. Table 2 is a
  framed pair of numbered equations and Table 5 the two-column procedure list; neither prints a
  header row at all, so both take the schema floor of `header_rows` 1 with the first row standing
  in the slot, which is stated in their notes rather than hidden.
- **Figures 9 and 10 are two panels each.** The low- and high-density visualisations are measured
  as separate left and right regions, so each gets a row per panel: the caption and the single
  citation sit on the leftmost panel and the right panel carries neither. The panels have no
  axes, no ticks and no lane label, so which lane is which is fixed by the measured x positions
  (165 against 496), not by anything drawn.
- **Figures 12 to 14 are 3-D density meshes.** Two panels each of density against distance and
  time, `surface-mesh`, recorded `surface-or-3D` rather than forced into `line` — the third of
  the set is the one exhibit whose caption parts company with its art, since the meshes close
  p21 and `Figure 14. Normal or Higher Density` opens p22.
- **The same triple plotted twice.** Figures 15 to 17 key three traffic rules across three
  colours inside the frame; Figures 19 to 21 plot the same flow/safety/energy quantities again
  with only `Equipped` against `Not Equipped`. Figure 11 is the only plot that writes values onto
  its own data — the critical points of both lanes plus four density arrows on the x axis.
- **A Chinese legend left in place.** Figures 3, 4 and 5 carry a single-entry legend reading
  `系列2`, outside the frame at the right, in otherwise English artwork. It is recorded where it
  is, not translated, and `geometry.legend` is `outside-right` for all three.
- **Citations are all forward but one is late.** Twenty-two figure citations and five table
  citations, `lead_pages` 0 or 1 throughout, with no negative lead: every exhibit is pointed at on
  its own page or the page before. Tables 2, 3 and 4 are never cited by number at all — Table 2
  takes the deictic clause that introduces the equations and Tables 3 and 4 the p7 sentence on
  the lane-changing rule, each with an empty style list and `count: 0`.
- **Faults worth carrying downstream.** Figures 6 to 8 are captioned "Optimal Maximum Velocity"
  while the artwork only plots phi against Vmax with no optimum marked, and the combined peak
  (0.72) sits above the light-traffic one (0.69), which a mixture ought not to do; Figures 9 and
  10 claim lane and time axes the artwork does not draw; Table 5 prints no Step 12, skipping from
  Step 11 to Step 13; Table 1's caption carries a stray asterisk note about pre-evaluation; and
  Figure 22's measured region catches only the occupancy band of an illustration that extends
  past the top edge of what the layout pass found.


**Paper 55** — `P-A-2014-30532-8f80536d`, the multi-lane cellular-automaton study of the
Keep-Right-Except-Pass rule: a simulation panel over five parameters, three alternative rules
compared, and a factor-analysis score used to rank the rules, 29 PDF pages, 21 measured regions.

- **Nineteen exhibits and two exclusions.** Sixteen figure rows and three printed tables over
  nineteen pages, plus the p1 summary-sheet form and the p21 tail of Table 2, both excluded.
  19 + 2 = 21 exactly, nothing unresolved and no declared gaps.
- **Five regions, two numbers each.** The layout pass cannot split a raster, so the p17 plate
  holds Figures 8 and 9, p18 holds 10 and 11, p23 holds 13 and 14, and p26 holds 17 and 18; each
  is one row quoting the first caption, with the second caption quoted in the row's note. `record.py`
  refuses a region counted twice, so one row per region is the only legal shape here. The p27
  plate is the odd one: Figure 19 above, and below it a chart the page labels "Figure 12: Density
  vs. Factor Score" — the number and title of the page-22 plate, reused for a different drawing.
- **Figures 2 to 7 are three-quarters of a 2x2 cell.** Panel a top left, b top right, c bottom
  left, bottom-right empty, each panel with its own small in-image title and its own axis titles;
  the typeset sub-captions print below the panels and the text layer reads them b, a, c, so the
  quoted caption keeps that printed order. The first three plates are connected line charts and
  the last three are unconnected point clouds.
- **Figure 1 is a state lattice, not a plot.** Two side-by-side blocks, one per lane, each cell
  printing a digit 0 to 5 for the vehicles in that road section, with bare "Space" and "Time"
  arrow axes and no ticks at all — recorded `heatmap-or-contour`.
- **The p5 flowchart has no caption.** Section 2.2 says "The analyzing procedure can be
  illustrated by the flowchart below:" and never numbers the drawing, so that row carries an
  empty caption, `caption_source` none and numbering none.
- **Not one exhibit is cited by number.** All seventeen pointers are deictic — "the flowchart
  below", "the figures show that", "compare this two figures", "get following curves", "the
  following are figures of flow, lane change frequency and average speed" — recorded with an
  empty style list and `count: 0`. Three run backwards: the p25 sentence introduces both the p26
  and the p27 plates, and the p22 sentence introducing the factor-score curves is reused for p23.
- **Three tables, one SPSS-style construction.** A merged title cell, an empty spacer row, a
  header row of Factor1 to Factor4 over a blank stub, rules under the title and header and
  between every body row, full-height vertical rules and a complete outer frame, no zebra, with
  decimal-aligned statistics. All three captions are the bare words "Table 1", "Table 2" and
  "Table 3" — no titles at all — and all print below their grid. Table 2 breaks across p20/p21.
- **Six series per factor plate.** Figures 12 to 16 key traffic flow solid and safety dashed for
  KROL, KREP and HLLR, in an outside legend below the plot, using the x variable name as the
  legend header instead of an axis title, and drawing the x-axis through y = 0 rather than at the
  foot of the frame.
- **Faults worth carrying downstream.** Figures 5 and 6 plot the same x variable on a 0 to 1
  scale in panel a and a 0 to 100 scale in panels b and c; Figure 5's axis is titled "bic car
  fraction" twice; Figure 7's typeset sub-captions are swapped against its in-image titles, so
  the letter b sits under the panel titled "vs. Velocity"; Figure 12's traffic-flow series swings
  through 1.05 and back below zero; Figure 13's caption misspells "Factor score" as "Factor
  sore"; and the p27 plate reuses Figure 12's number and title for a chart with different curves
  and a different axis range.


**Paper 56** — `P-A-2014-31333-acc8bc3b`, the Nagel-Schreckenberg cellular-automaton replay over
four rule systems, 17 PDF pages, 8 measured regions.

- **Eight exhibits and nothing else.** One flow chart and one accident chart for each of the four
  rule systems, on pages 8 to 11, one pair per page. No tables, no exclusions, nothing unresolved.
- **Not one exhibit is numbered.** There is no caption line in the text layer anywhere in the
  paper — the chart titles are drawn inside the artwork in small caps, "AVERAGE FLOW RATES OF
  RIGHT HAND RULE" and the like — and no prose sentence cites a figure by number. So all eight
  rows carry an empty caption, `caption_source` none and numbering none, and the titles live in
  the row notes rather than in the caption field.
- **One construction, eight times.** Grouped vertical bars over twelve simulation types
  (Fast/Slow × Computer/Accident Prone/Normal × Heavy/Light), a grey-to-black ramp of lane-count
  series keyed outside the frame at the right, a complete frame with horizontal gridlines at every
  tick, rotated text labels on an x axis with no numeric scale, and no data labels — except on one
  plate.
- **The flow charts do not share a vertical scale.** 0 to 4 on p8, 0 to 4 on p9, 0 to 3.5 on p10,
  so only the accident charts (2000, 2500, 2500, 3000) are even roughly comparable, and the
  paper's comparison section reads them side by side anyway.
- **The accident plates are mostly empty by design.** Accidents appear only in the two
  accident-prone-heavy groups, so ten of the twelve x slots carry no bar on most accident charts.
  An empty group is not a missing series.
- **Only the p11 accident plate labels its data** — 211.3, 98.8, 66.2, 97.3, 30.6, 102 and 86.1
  beside the small bars, and nothing beside the two tall accident-prone-heavy bars, which is
  exactly the drop the prose is pointing at.
- **Two defective legends.** The p9 accident chart lists five swatches of which two both read
  "three lanes" and none reads "four lanes"; and on both p8 and p9 no group draws all five series
  the legend promises.
- **Faults worth carrying downstream.** The p8 x labels print "Fast-Accident Proine-Light" where
  p9 spells it correctly; p10's accident title reads "FOR NO CHANGE RULE" where its siblings read
  "OF"; the p11 pair alone uses a two-entry legend ("lane three" against "lane five"); and the
  section-4.2 lead sentence is the only pointer six of the eight rows have.

**Paper 57** — `P-B-2014-26160-510e6a16`, an AHP-plus-Grey-Correlation-plus-Fuzzy paper that ranks
the all-time best college coaches of basketball, field hockey and football, 36 pages. Fifty-seven
measured regions over twenty-nine pages, all accounted: 14 figure rows, 32 tables, 11 refusals.

- **The paper repeats its own answer four times.** The five-name rank table (Rank × Basketball /
  Field hockey / Football) prints in the abstract on p1, twice on p10 — once as the Grey model's
  result and once as the Fuzzy model's, with different names in football — again in §9.1 on p27, and
  a fourth time inside the letter on p30. None of the four carries a caption or a number; each is
  recorded with an empty caption and its lead-in sentence in the mention block.
- **Column vocabulary for a table census.** Every one of the 32 tables is `booktabs` — a top rule, a
  rule under the header, a bottom rule, no vertical rules and no outer box anywhere in the paper. Only
  five carry pale-blue zebra shading (Table 7 p12, Table 8 p14, Table 12 p19, Table 13 p20, the
  ranks-comparison Table 15 p22); the other 27 are plain white.
- **Five tables are measured only as a header band.** A grid whose interior carries no rules cannot be
  separated from the prose above it, so the detector stops at the top rule: Table 4 on p8 and Table 8
  on p14 lose all their data rows this way, and Table 7 on p12 and Table 12 on p19 are returned as a
  header strip plus a body block. Each table is still counted once — the row records the bigger
  region, the strip is refused as `fragment-of-other`, and the note says where the grid continues.
- **Seven chart plates are one Excel chart in two layers.** Figures 3, 4, 5, 6, 7, 8 and 13 are a
  bitmap plot body — bars plus gridlines — pasted inside a vector frame that carries the in-artwork
  title and the axis text. Each is one chart and one row; the nested raster is refused. All seven are
  `three_d: perspective-bars`; the flat 2D plates are the p24 pair, which are MATLAB columns with
  tick marks on all four sides and dashed annotation boxes.
- **Two plates contradict their own captions.** Figure 6 is captioned "Scores of top 15 basketball
  coaches" while its artwork is titled field hockey and three field-hockey names (Enza Steele, Sally
  Scatton, Brenda Meese) gatecrash the top of its order; Figure 7 is captioned field hockey while its
  artwork is titled football and near-duplicates the chart printed beneath it. Both are recorded as
  printed, with the contradiction in the note.
- **p23 misnumbers its citation.** "The difference between ranks considering coaching start time or
  not is shown in Figure 9" belongs to Figure 10 on the next page. The row for Figure 9 carries the
  sentence as a trailing mention rather than a second citation being invented for Figure 10.
- **Duplicate table numbers are printed, not repaired.** Tables 2, 3 and 4 all print the caption
  "Pairwise comparison matrix of hierarchyⅡ-Ⅲ" (personal quality, training quality, team
  achievements), and two unrelated tables are both numbered Table 15 — the football top-5 grid on p21
  and the ranks comparison on p22. Captions are quoted verbatim and the clash is named in the notes.
- **Four transposed grids with no header row proper.** Tables 9, 10, 14 and 15 print coach names as
  the header row and only Scores and Rank as data rows, so each is three rows deep. The p17 comment
  set goes further and prints no header row at all — `header_rows` is floored at 1 by the schema, so
  the row records 1 and the note says the two printed rows are Level and Score.
- **The Honor Roll is a poster, not a figure.** p28 is a full-page raster — olive border, gold medal
  ribbon, three sport clip-art icons — holding three ranked tables stacked down the page, so it is one
  `composite-panel` row with `panel_count` 3 and `panel_layout` "column of 3"; the football-player
  icon between the first two tables is `in-body-diagram`. It is the only page in the paper whose
  exhibits were drawn as an image rather than typeset.
- **The appendix takes its list item as a caption.** Appendix grids 1–6 print "1. Original data of
  college basketball coaches" and the like above the grid and no table number at all, so `numbering`
  is none while the title is quoted. Four of the six continue across a page break with the header row
  reprinted: the first fragment carries the title, the tail carries `continued` true and an empty
  caption.
- **Nothing unresolved** — no `unresolved` rows, no declared gaps: all 57 measured regions map onto
  an exhibit or an explicit refusal, and `record.py` closed it at `figures=14 tables=32 excluded=11
  unaccounted=0`.

**Paper 58** — `P-B-2014-26333-27e7d8ab`, a 2014 B paper that builds a two-lane lane-changing
model, an extended "Ring Road" cellular automaton and a refined version with entrance and exit
ramps, then ranks nine overtaking rules with a fuzzy synthetic evaluation over lane count, speed
limits, signal-before-shifting and intelligent systems, 54 pages. Sixty-three measured regions over
thirty-four pages, all accounted: 33 figure rows, 12 tables, 18 refusals, nothing unresolved.

- **One number, two panels, eighteen times.** Figures 6, 8, 10, 11, 16–24, 26–29 and 32 print one
  number and one caption below a side-by-side pair, so the paper shows 51 chart panels under 33
  numbers. The right panel is always refused as `fragment-of-other` and the row is the left panel,
  with two exceptions forced by the detector: it numbered the p30, p48 and p49-lower rows right to
  left, so those rows are r2 and the left panel is the refusal.
- **Light and heavy are bars, not panels.** From Figure 16 on, every comparison is a flat grouped
  bar chart where the two traffic regimes are two adjacent bars inside ONE axes. Only the printed
  (a)/(b) sub-captions ever create a second panel, so no figure in the paper is split by regime.
- **Two chart technologies, one paper.** Figures 6–15 are MATLAB default line plots — one axes, no
  gridlines, no in-plot title, boxed legend inside the upper right. Figures 16–33 are flat grouped
  bars, still 2-D; there is no 3-D, surface or perspective anywhere in the paper, and the only
  raster photograph is Figure 5, a satellite view of a real interchange.
- **Value labels come and go.** Bar panels 16–23 and 27–33 print a numeric value above nearly every
  bar; the rule-comparison panels 24–26 print none, so their ranking has to be read off heights.
- **Table 3 is a declared gap, not a row.** p16 prints the caption "Table 3 Characteristics of
  Vehicles" at y=290 with a booktabs grid under it (Car 1 cell 6 cells/sec 60%, Bus 2 cells
  5 cells/sec 30%, Truck 2 cells 3 cells/sec 10%), but the detector returned no region for it — the
  page's only region is the Figure 3 raster below. The table is named in the note instead of being
  given an invented bbox, so the paper prints thirteen tables and twelve are measured.
- **Two rule styles coexist.** Tables 1, 2 keep a top rule, a header rule and a foot rule with no
  verticals and one spanning group row each (Constants on p8, Variables on p9). Tables 4–9 on
  p40–p44 add ONE internal vertical between the stub and the first data column; Tables 10–13 on
  p45–p46 are booktabs with horizontals only. Nothing is zebra-shaded, nothing is continued across a
  page, and the percent stub of every sensitivity grid prints no header text at all.
- **Transposed and one-row.** Tables 5 and 6 are a single data row (`F_i`) against the five rule
  names, i.e. Table 4 transposed; header cells wrap rather than abbreviate throughout ("sharp
  breaking frequency", "std. deviation of speed", `partial-assigned-lane-and-keep-right`).
- **The first exhibit number is misapplied.** "The time space diagram (Figure 8)" on p22 points at
  the two time-space diagrams printed on that same page as Figure 6, while Figure 8 is the
  flow-rate-of-each-lane pair three pages later. Figure 6 therefore ends with no named citation and
  Figure 8 carries a lead of three pages.
- **Faults worth carrying downstream.** Figure 15's caption prints the source file name —
  "Std. deviation of speed.png under the condition of different occupancies"; Figure 12's caption
  wraps to two lines; Figure 23 is the only figure whose legend sits ABOVE the axes; Figure 11's
  bottom y tick is cropped; p40 points at a broken "Table ??" for the ideal alternative and p47's
  pointer prints "(tableand table. )" with both numbers lost; and Figure 27's pointer is hyphenated
  across a line break as "speed fig- ure.(Figure 27)".

**Paper 59** — `P-B-2014-26636-060c74b1`, a 2014 B paper that ranks college coaches: a fuzzy
preferential relation over wins, winning percentage, national championships and coach awards, a
grey-relational ranking checked against four published lists, a Shannon-entropy cross-check and a
sweep of the matrix parameter, 38 pages. Forty-eight measured regions over twenty-two pages, all
accounted: 27 tables, 4 figure rows, 17 refusals, nothing unresolved.

- **A table paper.** Twenty-five numbered grids plus two unnumbered notation grids, and only four
  rows that are pictures at all — three charts and one photograph. Families: `table-grid` 27, `line`
  3, `composite-panel` 1. There is no bar, scatter, map, schematic or 3-D anywhere, so the only
  family judgement this paper forces is telling a chart from a grid.
- **One grid, one style, twenty-seven times.** Every table is the same full-ruled Word grid — outer
  box on four sides, a rule between every row, a vertical between every column — and the two
  unnumbered notation grids are boxed exactly like the numbered ones. Not one grid is booktabs and
  not one is rule-free, which is the opposite of paper 58's three coexisting styles.
- **Twelve splits, no repeated headers.** Tables 3, 4, 5, 14, 15, 16, 18, 20 and 22 cross a page
  break and no continuation reprints its header row, so five tails are bare columns of numbers whose
  meaning survives only from the previous page. Table 3 is the worst: the caption and three rows at
  the foot of p10, twenty-two rows filling the whole of p11 with one orphan row holding a lone "9",
  and a two-row tail at the top of p12 ending in the foot rule.
- **The row is the fragment that carries the caption.** That is the rule this paper settles, and it
  differs from paper 57's "bigger region": the ledger's page and bbox should point at the printed
  title, not at whatever happens to be largest. All ten continuations are refused as
  `split-across-pages`, so the ten split grids produce ten rows and ten refusals, never a second row.
- **Shading is semantic, and one grid is unexplained.** Tables 5 and 16 shade exactly the top five
  coaches and say so in a table footnote — Table 5's says "gray", Table 16's "grey" — so those two
  are `zebra: true` with the note naming the rows. Table 19 is the only genuinely alternating zebra
  in the paper. Table 17 shades five rows (2, 3, 7, 8, 9) with no legend, and since row 7 is one of
  the agreeing ranks the shading cannot be marking disagreement, so it stays `zebra: false`.
- **The caption strings are worse than the page.** The layer welds one caption into "Table 147."
  where the page prints "Table 14."; prints "Table 2.Interrelationship" with no space after the
  number, "Table 7.1.Top 5college" with the name welded to the number, "Table 11." and "Table 12."
  with no title at all, and "Table 7.2.Top 5 college men's ice hockey coaches" on p15 while its grid
  starts at the top of p16 — the one table whose caption and body are on different pages, recorded
  with the caption quoted from p15.
- **A Symbol-font parameter.** Tables 21–23 print the matrix parameter as the Symbol-font rho
  (U+F072), not a lambda, and print the equals sign in the same Symbol run at U+F03D — both
  private-use code points, both invisible in a terminal, so these caption strings were copied out of
  the text layer instead of typed, and the space the caption leaves before the equals sign came with
  them. Table
  23's header cell also prints the stray Chinese "公式" after its closing parenthesis, the only
  Chinese text in the document.
- **Twenty-five tables, twenty-five citations of a sort.** Eight are never cited by number (4, 5, 8,
  9, 10, 18 and the two unnumbered grids, which have no number to cite), four share a single pointing
  sentence in pairs ("Table 6.1 and Table 6.2", "Table 7.1 and Table 7.2 respectively"), Table 20 is
  cited twice and is also the paper's only statement that its own two methods disagree, and the
  three charts are cited on the page BEFORE the art — p17's three sentences describe the charts that
  print on p18, with Figure 3's caption pushed on to p19.
- **Declared partial and declared refusals.** Table 10 prints five rows and four fall inside the
  measured box: Ned Harkness sits at the top of p17 in the block the detector counted as 23 paths
  but measured as no region, so the row count is the printed five and the note says so rather than
  inventing a bbox. Also refused rather than repaired: p3 and p37's body prose and p7's display
  formula are measured as vector regions only because this document's producer emits an invisible
  white fill rectangle behind every text line.
- **The appendix is three photographs butted into one strip.** p37's Wooden, Bryant and Summitt
  photographs share edges with no gutter, print no figure number and no caption, and sit under three
  rhetorical paragraphs ("May be he is John Wooden …"), so the strip is one `composite-panel` row
  with `panel_count` 3 on the leftmost panel and the other two refused as fragments. The charts are
  one construction repeated: an Excel line chart pasted as a bitmap inside a thin vector frame,
  in-art title, horizontal gridlines only, single series, legend below the plot area, no data labels.

**Paper 60 — P-B-2014-28414-5bd5b982, thirty-three pages, fifty-six regions.** A coach-ranking
paper (AHP, fuzzy synthetic evaluation, aggregation model, then time weights, other sports,
parameter sweeps, presidents). Twenty-two tables, ten figure rows, twenty-four refusals.

- **Every caption prints BELOW its exhibit.** All twenty-two numbered grids, all six charts and
  all three diagrams put the number under the object — the exact inverse of paper 59, and the
  reason `position` is `below` on every row here.
- **Five grids have their caption on the far side of a page break** (Tables 5.2, 6.2, 6.4, 6.7,
  7.2): header and first rows at the foot of one page, the last data rows plus the caption at the
  top of the next. Under the lane rule the row is the topmost fragment, so the header fragment
  carries the row and the caption is quoted from the page that prints it.
- **Four unnumbered notation grids** sit under 2.1 Symbols and Definitions, each introduced by a
  bold bullet ("Symbols for AHP:", …) with no number and no caption; one of them is itself split
  across p4/p5.
- **Two grids are two tables inside one frame** — Table 4.2 and Table 6.1 repeat their header and
  drop a vertical divider down the middle, so six printed columns carry ten ranks in five rows.
- **Only two grids merge cells, both vertically**: Table 4.1's Goal cell spans all fourteen body
  rows, Table 6.7's aspect stubs span their metric rows. A wrapped header or a two-line
  turning-point cell is one cell, not a merge.
- **The house frame is the full box, and three grids break it** — Tables 4.3, 6.1 and 6.2 print
  horizontals only (`booktabs`), and Table 4.3 also beheads its own header by labelling both the
  fourth and the fifth aspect column `X3`.
- **Shading is used four ways.** Tables 6.4–6.6 band rows 238/255 and mark the coaches whose rank
  moved in **bold**, not with fill; Table 4.3 bands in two-row pairs; Tables 6.3 and 6.8 shade a
  fixed set of rows with no key; the rest shade only their header row.
- **The one exhibit the layer cannot quote.** Table 7.1's caption prints on the same line as the
  tail of formula 3, so the text layer interleaves them and that verbatim is typed from the crop
  (`typed-from-crop`). Everything else here is quoted from the layer.
- **Exactly one by-number citation in the whole paper**: "changes of weight distribution can be
  seen clearly in Figure 7.1" (p26). The other twenty-five numbered exhibits are pointed at with
  "the following table shows", "shown in following table", "Here are our results:", "The following
  figure shows" or "(See figure)", so their mention count is zero.
- **Figure 7.6 is a radar plot** and the family vocabulary has no radar member, so it is filed as
  `other` with an `other_note` rather than forced into `line` or `surface-or-3D`. Figures 7.4 and
  7.5 share one printed caption line, "Figure 7.4 && 7.5", and each carries it as its verbatim.
- **Section IX is a captionless three-sport photo block**: header `Rank | college basketball |
  college football | college hockey`, five ranks, hairlines and grey rank bands, no number and no
  title. Its header row prints just above the measured region; the fifteen coach portraits are
  separate rasters and are refused as fragments, the two grey rank bands of p31 as continuations.
- **Table 3.1 prints four of the ten coaches its own prose promises**, with a row holding nothing
  but an ellipsis where the other six would be. The row count records what the page prints.

**Paper 61 — P-B-2014-28875-728f6f07, thirty-five pages, thirty-eight regions.** The same
NCAA coach-ranking problem as papers 59 and 60, built the other way round: one paper-wide
metrics tree, an IAHP-FCE score, then four sports, four time-line comparisons, a
model-vs-website check and a sensitivity flowchart. Eleven figure rows, eighteen grids,
nine refusals.

- **Caption side is decided by kind, not by paper.** All eighteen grids caption ABOVE, all
  eleven figures caption BELOW. This is the first paper in the batch where the two sides
  separate cleanly along the table/figure line, so `position` here is a property of the
  object class and nothing else.
- **Table 10's caption swallows its own header.** The layer reads "Table 10 The weight of
  each metrics w1 w2 w3 w4 w5 w6 w7 0." — the stub row was set on the caption's baseline.
  The verbatim is quoted as printed, glyphs and all.
- **Figure 2's caption carries an in-art token.** It prints "Figure 2 SOS The metrics for
  NCAA Football coach."; the stray "SOS" is a column label that escaped the art. Because
  the layer text cannot be matched to the measured caption band as a clean sentence, this
  row alone is `typed-from-crop`.
- **Table 4 is split by a page break and counted once.** Its p16 block prints the first
  level-1 group (Classification 1, W1, B1..Bx) and its p17 block the second (Classification
  3, W3, By+1..), with no caption on p17. The p17 block is refused `split-across-pages`.
- **The heading detector gave out.** Seven headings over thirty-five pages, one of them
  bogus, and from p21 every measured row inherits the same junk label "0.25 Then got the
  coach Fuzzy Evaluation composite score". Every `section_path` in this record is typed
  from the printed heading with `section_numbered` false instead.
- **Two prose misdirections.** p16 says "As shown in Figure 1" over Figure 4's tree, and
  Figure 9 appears on p27 with no introduction at all — the first sentence that names it
  compares it to Figure 7 after the fact.

**Paper 62** (`P-B-2014-29696-84be6e3a`) ranks college coaches four times over — PCA factors,
adjusted cosine similarity, a time-line-horizon pass and a gender pass — then extends the
factor pool to other sports and countries and stress-tests it with noise, 44 pages. Four
lessons from it:

- **Two number series in one paper.** The summary sheet prints `Figure 1` and `Figure 2` in
  bold with no caption text at all, the body starts a second series at `Fig 1.` on p13, and
  the unnumbered page-2 execution flow chart is captioned nowhere, so sixteen measured figure
  rows stand against fifteen printed numbers. `caption_source` is `none` for that one row
  rather than a title typed out of the art.
- **Seven numbered tables have no region.** Tables 4, 10, 13, 14, 15, 16 and 20 are ruled
  three ways the same as every other grid in the paper, but each rule set spans only 158 to
  437 pt of a 595 pt page with no enclosing box, so the region pass boxed nothing. They are
  declared in the note, not invented as rows: `record.py` needs a measured bbox and there is
  none. This is the largest declared gap in the batch so far and the reason the paper's 22
  numbered tables record as 15 rows plus 2 unnumbered appendix dumps.
- **Photographs live inside table cells.** Every row of Tables 17, 18 and 19 carries a colour
  coach portrait in its Name column, twelve rasters across three grids. The detector boxes
  each portrait separately, so the grids are the header bands and twelve fragments come off.
  Figure 1's three-panel photograph collage and Figure 2's two flanking pictures are the same
  pattern one level up: one row each, `panel_count` 3 and 1, the repeats refused.
- **The heading detector is worse here than on paper 61, not better.** 112 heading records
  and every single text field is null, while the section paths it does emit are rows of
  racing results (`8 Bill Self M`, `10 John Thompson Billy Donovan`) and one axis title
  (`12 Different Factors`). Unlike paper 61, though, this paper's printed headings are clean
  and numbered, and all forty of them are verbatim in the text layer, so `section_numbered`
  is true here with the printed label — the opposite decision to #61 and worth keeping
  straight.

**Paper 63** (P-B-2014-30680-9f0c0d05) is the coaches-of-the-century paper: one directed game
network per season, eigenvector centrality for team skill, Powell's method for coach skill. Nine
measured regions, nine exhibits, no refusals and nothing unresolved - the smallest exhibit count
in the block so far.

- **Four grids and not one caption.** Every table in the paper is unnumbered and uncaptioned.
  The introduction is prose each time: `These coaches are:`, `Below is a table of top ranks from
  eigenvector centrality compared to the AP and USA Today polls`, `The table above shows the
  results of running Powell's method`, `we arrived at the following table`. The four printed
  figures, by contrast, all carry `Figure N:` on the caption line. A paper can be careful about
  one exhibit class and careless about the other, and the record shows which is which.
- **Two typesetters, one rule design.** The magazine spread (pages 2-3) is Cambria on a 433.1 pt
  measure with its rules drawn as 0.5 pt filled rectangles; the body is LaTeX on a 343.7 pt
  measure with stroked rules and a CMBX10 bold header. Both print a complete closed grid - a rule
  under every row including the header, a vertical between every column - so all four are
  `vertical-rules` and the type engine is a note, not a field. Widths: 443.6 pt (102 % of the
  spread measure), 336.0 (98 %), 263.8 (77 %), 382.3 (111 %, overrunning the right text edge by
  39.8 pt into the margin).
- **The measured box is not the figure.** Figures 3 and 4 are one indigo density curve each on
  open L-axes, and both print `Probability` above the top edge of the box and `Margin of Win`
  past its right edge at the axis terminus, at a 5-6 pt cap height. A crop of the region alone
  holds neither title, which is why both notes name where the titles print. Neither curve has
  ticks, a scale or a legend, so `printed_numbers` is false on a figure whose whole argument is
  about a horizontal shift.
- **The nearest heading is not the section.** The Figure 2 page gets `6 Separating the Coach
  Effect` from the heading pass, a heading printed 130 pt *below* the picture; the Figure 4 page
  gets `6.2 Margin of Win Probability`, printed 200 pt below it. Nine of the 49 heading records
  are rows of the poll table (`1 Duke Kansas Kansas`). All five numbered labels used here are
  printed headings, verbatim in the text layer, so `section_numbered` is true and the path is the
  heading that actually governs the region; the two magazine-spread regions carry the unnumbered
  `Summary` prefix and are recorded with `section_numbered` false.

**Paper 64** (P-C-2014-25318-eac62e81) is the Erdos1 paper: degree, betweenness and eigenvector
centrality for 511 co-authors, then a revised PageRank over a 24-paper citation network and the
authority-popularity plane that ranks the stars of a co-star network. Fourteen measured regions over
twelve pages, eleven figure rows and three tables, no refusals and nothing unresolved.

- **Seven tables, three measured.** Tables 1, 2, 3 and 7 print as plain two-rule booktabs grids -
  a rule above the header and a rule below the last row, no header rule, no verticals - and the two
  rules of each stand 314.1, 178.7, 178.5 and 180.4 pt apart. The grouper joins rules only within
  120 pt, so no cluster forms and the page returns no box. The table-tail fallback does not rescue
  them either, and that is the interesting part: it seeds its search window from
  `max(b[3] for rules with b[3] <= box[1])`, and a stroked rule arrives from `get_drawings` with
  zero height, so the closing rule's own bottom edge equals its top and the window collapses to
  nothing (`fig_extract.py:493`). The tail path therefore can fire only for a rule with real
  thickness, and this paper's rules are all hairline strokes. All four are declared gaps, and a
  paper whose table count exceeds its measured table regions is a signal to check for exactly this
  shape before blaming the extractor for a lost frame.
- **Two grids print their header twice.** Tables 5 and 6 are two side-by-side blocks inside one
  ruled frame, each with its own header band, so `cols` counts the physical grid - 6 and 4 - and the
  block structure goes in the note. Table 5 carries three rules in all (above the header, under the
  header, below the last row) and no vertical anywhere, not even between the blocks; Table 6 adds
  one full-height centre divider and no side verticals. Both are `booktabs`: no cell is closed, so
  neither is `vertical-rules` however many rules the eye counts.
- **Captions split by exhibit type with no exceptions.** Eleven figure captions print BELOW their
  art and three table captions print ABOVE their grid, which is the same split paper 62 showed and
  the inverse of paper 59. The one asymmetry inside the figures is typographic: Figure 3's caption
  is set as a justified two-line paragraph across the full 419.4 pt measure, every other caption is
  a centred single line.
- **The measured box is not the exhibit, part two.** Table 5's region stops at 564.1 pt; the block's
  closing rule prints at 589.6 pt and its last two lines at 565.5 and 576.9 pt, so ranks 11-12 and
  23-24 sit below the box the record carries. The absorber stopped there because rank 23's PR value
  prints on a line of its own, one numeric cell, under the two-cell threshold. The same page shows
  the other half of the same trap in Figure 6: its ticks print 0.5 to 4.5 and 2.6 to 4.2, and those
  are the LOGARITHMS the prose set, not the quantities the axis titles name.
- **Two counts inside the paper disagree.** Figure 9 plots fourteen markers against the fifteen rows
  of Table 7 on the same page; the missing point is the 238-million-search star, with no ink at that
  coordinate and no note anywhere. Figure 7 carries Figure 4's caption verbatim - `The directed
  citation network with weight added to links` - over a co-star network of actors. Both are recorded
  as printed and named in the notes; the census does not repair the paper.

**Paper 65** (P-C-2014-27688-856eb1b7) is the Erdos1-network paper: centrality for the 511 co-authors,
a topological-sorting algorithm over the 16-paper citation network that beats PageRank for cost, and
the same algorithm run over about 500 US media companies. Fourteen measured regions over ten pages,
six figure rows, seven tables, one exclusion and nothing unmeasured.

- **No ghost grid, for once.** Thirteen printed numbers - Figures 1 to 6, Tables 1 to 7 - and
  thirteen measured regions, the first paper in the lane where the printed count and the measured
  count agree. The reason is the ruling: every grid is a closed box whose consecutive horizontal
  rules stand 16.1 pt apart, inside `TABLE_GAP_PT` of 120, so `_cluster` forms one group per grid and
  the box it returns is the grid. Paper 64's four unmeasured grids failed for the opposite reason -
  two rules 178 to 314 pt apart - which is why the two papers, measured by the same pass, disagree
  about their table counts.
- **One ruling register, seven times.** Not one `booktabs` grid prints here. Each of the seven grids
  carries a full-height vertical rule at every column boundary and a horizontal rule on every row,
  verified from `get_drawings` rather than from the image: 6, 7, 5, 5, 6, 4 and 5 verticals. The only
  irregular band in the paper is Table 2's header at 31.7 pt against 16.1 pt for every body row - the
  one grid whose two blocks each hold a name and two numbers rather than a single field.
- **A caption inside its own box.** Figures caption below, tables caption above, thirteen times in a
  row - and then Figure 6, whose caption prints at y 358 pt, inside the ruled frame, in the bottom of
  its right cell. The frame is not decoration: it is the exhibit. The measured region runs 84.4 to
  511.1 pt, the full frame, and the flowchart bitmap inside it (281.8 to 505.2 pt) is a second
  measured region that would double the exhibit if it were recorded as a row. It is excluded as
  `fragment-of-other`.
- **The header cell that looks like two columns.** Table 3 prints `In Degree Closeness Betweenness
  Eigenvector` over four columns, and the natural reading is five labels over four columns - a defect
  worth recording. The word positions settle it: `In` prints at 186.6-194.8 pt and `Degree` at
  197.2-227.9 pt, both inside the first column's 181.0-233.0 pt, so the first header cell is the two
  words `In Degree` and the grid is a clean four. Measurement beats the text layer's reading order
  wherever a header and its body disagree.
- **Decimals get three different answers in one paper.** Table 2 is genuinely decimal-aligned:
  two decimals throughout, points on one x. Table 1 is not - its values all carry three decimals and
  all start on the same left edge, so the format fakes the alignment. Table 6 is neither: 3825,
  2231.1 and 970.924 are centred in the column and their points stand wherever the centring puts
  them. Fixed precision is not alignment, and the record keeps `decimal_aligned` false for the two
  grids whose digits only look lined up.

**Counting conventions, fixed here for the whole lane.** Two questions keep coming back
from audits, so they are settled once:

1. `family_counts` is *region level*: it counts every recorded exhibit, tables included
   (`table-grid`), so its values sum to `len(items) + len(tables)`. It is not a count of
   printed figure numbers.
2. `items` counts *measured layout blocks*, not figure numbers. A three-panel figure whose
   panels are measured separately is three items sharing one caption, and a figure whose
   panels were drawn as one cluster is one item. Any "average figures per paper" figure
   must therefore name which of the two it means; the two differ by roughly half on the
   multi-panel papers.

**Known gaps carried into the record, not patched.** (1) Display equations measured as
vector paths, excluded `not-an-exhibit` (paper 4, nine regions). (2) Type set program
listings measured as regions, excluded `not-an-exhibit` (paper 8, three regions). (3) A
column-width ruled table missed by rule 6's page-width threshold (paper 9, Table 6 has no
measured region; Table 5 counted from a partial band). (4) Tables set as plain vector text
are found only because a vector cluster happens to survive the area filter (papers 6, 7),
so `table-grid` counting is reliable only with a crop, never from geometry alone.

## `notes/<pid>.md` is generated

`record.py` writes `notes/<pid>.md` from the record's `rules` list every time it runs,
including a `--force` rewrite. A hand-appended section in that file (a pattern write-up,
a declared gap, an appendix reading) is destroyed by the next rewrite of the same paper
and must be re-appended afterwards. Two consequences for anyone auditing:

- The `rules` list inside `records/<pid>.json` is the authority on what the record
  claims. A note paragraph that contradicts it is stale, not a second opinion.
- If a rewrite is planned, keep the hand-written prose outside the file until the last
  `record.py` run for that paper, then append once.

## One region, one exhibit

`record.py` requires every exhibit `bbox` to equal a measured region and counts a region
at most once. Consequence for reproduced third-party sheets (handouts, guidance letters,
scanned appendices): an opaque full-sheet raster can carry only one row, however many
displays are printed on it. The rule used when that happens is to record the sheet as one
`composite-panel` item and read every table printed inside it in the item note and in the
paper's notes file, with its grid dimensions and rule style, so the omission is declared
and checkable. Sub-region bboxes are not accepted, and inventing them would be a schema
change, not a census decision.

## Where an exhibit belongs when it floats above its section

Layout sometimes puts an exhibit at the top of a page and the heading of the section
that discusses it a few lines lower. Two rules could apply and they disagree, so the
lane picks one: **use wins over placement**. `place.section_path` is the section whose
body cites or reads the exhibit, even when the figure sits above that section's heading.
Fall back to physical placement only when no body sentence cites the exhibit at all.

Use has two halves, and both are needed:

- **use wins over placement** — the section that discusses the exhibit owns it, even when
  the exhibit was floated above that section's heading;
- **consumption beats mere mention** — when a section cites an exhibit only to postpone it
  ("we will analyse fig. 16 later"), the exhibit belongs to the section that actually
  reads it, not to the paragraph that promised it. Otherwise the record files a result
  under the sentence that defers it.

Why use: the census asks which section *uses* which family, and an exhibit floated
forward is still the result of the section that reads it. A consumer cannot tell the two
rules apart from the record, and a mixed record is worse than either.

Every exhibit row needs an explicit path in the spec. A missing override is not an error:
`build_payload.py` falls through to the ctx heading at the exhibit's page, silently, and
the resulting row looks exactly like an audited one. Two of the ten defects in the #278
round came from that fallback, so a paper is only reviewable when each row's `place` was
written by hand and then checked against the printed heading.

## `section_path` labels come from the text layer, folios and all

`ctx.headings` is keyed off the table of contents as well as the body, so several
level-1 labels arrive with the TOC folio glued on (`1 Introduction 2`,
`5 Piecewise Nonlinear Programming for Time Trial 6`). A path built from those labels
can also repeat its own root (`1 Introduction 2 > 1 Introduction > 1.1 ...`), and a
chapter can inherit the wrong root when the TOC line and the body heading disagree
about which chapter a subsection belongs to. Both are visible in the record, so every
path is checked against the printed heading before it is stored: strip a folio whose
remainder equals the next level, drop a root whose number is not the parent of the next
level, and keep the printed title otherwise.

Unnumbered sections must start with the placeholder `未编号标题` (`schema.check_place`);
a plate with no printed heading at all is named `未编号标题 Appendix plate (no printed
heading)` so the path declares the absence instead of inventing a title.

A heading that the extractor failed to index does not lose its attribution. `check_place`
resolves a numbered label against `ctx.headings` first and, when that misses, against
`schema.printed_lines(pid)` - every raw line of the text layer. The label is stored as
printed and the record note names the index defect, so the row points at the section it is
actually under. The fallback is verbatim-only: a mistyped or invented label is not a
printed line and is still refused.

A heading that shares its line with a watermark glyph run is accepted in two further
spellings, both still contiguous substrings of the printed line: the tail starting at each
section-number token (`ğ els 5.5 Model Evaluation` → `5.5 Model Evaluation`) and the line
with every non-ASCII run collapsed to a space (`ྐ 8.2 Insights and Advice for NOCs ...` →
`8.2 Insights and Advice for NOCs ...`). Wrapped headings are not joined: joining two
lines produces a string that was never printed as one, so a heading whose title continues
on a second line is named `未编号标题 <number> <first line>` instead, which keeps the number
visible without folding watermark bytes or a guessed join into a grouping key.

First use is 2022 A `P-A-2022-2212245-8b85eeb2`, whose
`7.3 Sensitivity Analysis of the deviations from the target power` (p18) is missing from
the index - `context_extract.is_heading` drops numbered headings longer than eight tokens
unless the title-case ratio is high enough.

## A composite row bounds one panel, and says so

`geometry.panel_count` describes the artwork; `bbox` describes the one region the row was
measured from. For a wide composite those disagree, and the record has to pick a side out
loud. The convention: the row's bbox is the first panel the extractor emitted, the other
panels are `fragment-of-other` exclusions, and the item `note` states which panels the box
covers and which were never measured. A `panel_count` of 6 over a one-panel box is correct
as long as the note says so; leaving it unsaid reads as an unmeasured grid.

## One region, two printed exhibits

The converse case, met on #128 (p16: Figures 13 and 14, p18: Figures 16 and 17): two
separately captioned charts printed side by side whose drawing clusters fuse into a single
measured region. `record.py` refuses two rows on one bbox — `item 14: region counted twice` —
and inventing a half-width box breaks the region match, so the pair is one row with
`geometry.family = composite-panel`, `panel_count = 2`, `panel_layout = 1x2`, and a note that
names both printed figure numbers and quotes both caption fragments. `caption_verbatim` keeps
the caption that belongs to the region's own number and the second caption is quoted in the
note, because a joined reconstruction of two column-broken captions is not a substring of
anything the paper printed. `mention.count` sums the citations of both figures; `first_page`
is the earlier of the two.

## Two boxes are stored unclamped

`fig_extract` occasionally returns a container that runs past the page trim (negative x, or
y1 beyond the page height) and swallows body prose. `record.py` accepts it because it *is*
the measured region, and inventing a tighter bbox would break the region match. So the row
keeps the measured box and the note declares the overreach with the actual numbers, plus
the advice that a consumer cropping by bbox should crop the upper or central band instead.
Both known cases are in 2022 A: Figure 1 reaches y = 846.8 on a 792 pt page, Figure 14
reaches x = -85.6.

## When the layout pass changes under a closed paper

`fig_extract` gains and loses regions. A paper recorded against an older layout stops
validating - `payload layout_sha256 does not match the measured layout`, or
`N measured region(s) unaccounted` - and the record must be rebuilt, not patched:

1. snapshot the old context dump (`.proxy/<pid>-ctx.json` to `.proxy/_ctx<pid>_old.json`),
2. re-run `context_extract.py`, which renumbers regions,
3. remap every spec `region` index by rounded bbox from the snapshot, never by position,
4. add a row for each newly measured region, then `build_payload.py` and `record.py --force`,
5. re-append the notes block, because the record run rewrites `notes/<pid>.md` from `rules`.

A late region is usually a table whose cells hold display maths: the group spans from the
header rule to the closing rule, the wrapped equation rows push the closing rule past the
gap limit, and the grid measures thinner than the minimum side until the span fix lands.
Table 4 of 2022 A (p7) and Table 1 of 2022 A (p5) both appeared this way.

## A full-page raster is content when the page has nothing else

The layout pass drops images that cover the whole page, because on a scanned or decorated
page that is background. The guard is wrong on the opposite case: a page whose only object
is one full-page image, with no text layer and no drawings, is a page of content. 2025 C
(2521556) has three such pages - p8, p9 and p23 - each one image at [0,0,612,792], zero
characters, zero paths. Two of them hold four printed figures between them (Figures 4, 5,
22, 23).

Test, on the source PDF, before deciding what a missing exhibit is:

- image at page size **and** `len(page.get_text().strip()) == 0` **and**
  `len(page.get_drawings()) == 0` -> content. Measure one region over the page, then split by
  eye when the page holds two exhibits.
- image at page size with any text or drawings on the page -> background, exclusion stands.

Until the guard is fixed, the affected papers carry a declared gap that names the guard and
counts measured against printed (`22 measured exhibits against 26 printed`), and no bbox is
invented for an unmeasured figure. This is the one case where a missing exhibit is the
extractor's fault rather than a reading decision, so say so in the note.

## Half-measured exhibits, and boxes that host equations

Three shapes recur once a paper puts a table or an equation over a page turn, and they are stored
three different ways:

- **both halves measured, second on the next page** — one row for the exhibit plus the second
  region as `split-across-pages`. #136 does this twice: Table 6 (p13 head, p14 tail) and Table10
  (p17 header, p18 body). Neither paper repeats the header and neither prints a "continued"
  marker, so `table.continued` is the only field that records the split.
- **one half measured, the other on a page that returns no region** — the row keeps the measured
  half and the missing half becomes a declared gap, not a second row. #136 Table 1: its caption
  and header row print at the foot of p6, p6 returns no region at all, and the grid is measured
  from its second line down, so one exhibit is simultaneously counted and gapped. Say which rows
  are missing rather than inventing a box for the caption band.
- **an exhibit whose printed grid is measured only in part on the same page** — #134 Table A-2,
  where 165 pt of continuous grid sat between two measured boxes. Same handling: name the span.

The same caution applies to display math. On #136 every equation number (6)-(11) prints outside
the box that measured its equation, page 11's box for (6) leaves the `max SGI` objective line
above its top edge, page 12's box for (10) cuts the closing bracket of the final column vector,
and three display equations on those two pages have no box at all. An equation fragment box is a
detector artefact, not an exhibit: record it `in-body-diagram` and state in the note what the box
misses, because the alternative — treating the number's presence as coverage — turns a cluster of
math into eight phantom figures.

One ordering trap worth naming: `fig_extract` sorts a page's regions by top edge first. When three
panels in one row differ in height by a point or two, the middle panel can sort ahead of the left
one (#136 page 8: #1 is the middle pie, #3 is the left). Read the x coordinates before deciding
which panel a row carries, or the row will describe the wrong panel while the bbox stays correct.

## Duplicate is not fragment

The extractor emits each raster region about four times (2022 A #280: 266 raw entries, 77
distinct boxes). `measured_regions` counts distinct boxes, so the two exclusion reasons do
different jobs: `duplicate` is an exact or near-exact copy of another row's bbox, and
`fragment-of-other` is a different panel or half of the same exhibit. Using one for the
other hides which duplicates were extractor noise and which were structure.

## Why a printed grid can return no region

A table is measured by its rules, not by its title. `fig_extract` clusters vector paths, so a
grid that prints without any horizontal or vertical rule returns nothing even when it is
captioned, numbered, cited and zebra-shaded; a ruled grid returns a region whether or not a
caption sits above it. The two properties are independent, and conflating them was a mistake
in this lane's earlier wording: `#289` (P-B-2022-2228168-d50f161d, mcm-65) prints an open-ruled
table that the prose names by number and the detector still does not box. What a declared gap
is missing is the rules, not the label — the record has to say which of the two is absent,
because only the second can be reconstructed from the text layer.

Three cases have now all been seen, and they are not the same fault:

- **rules absent, label present** — the open-ruled grid (#290 above); the caption exists and
  the censused facts about the caption are sound, only the grid is unmeasurable;
- **label absent on one exhibit** — the uncaptioned table or chart inside a paper that
  captions everything else (`caption_source: "none"`, empty verbatim);
- **label absent across the whole paper** — #290 P-C-2022-2200401-824b71b2 prints five grids and
  gives none of them a number, a caption or a title; rules present and complete, so all five are
  measured, and every `caption` block is empty. This is a paper-level house style, not six
  separate omissions, and the record note has to say so or an auditor will read it as neglect.

The mirror fault exists too: #290 p22 r1 returns a 40x43 pt region in the memorandum margin
that holds only the COMAP brush-script wordmark — no rule, no data, no caption. Excluded
`not-an-exhibit`. So the failure is two-sided: an exhibit without rules returns nothing, and an
ornament without content returns a region.

One aggregation caveat that follows: **`caption.position` is a placeholder, not an
observation, whenever `caption.verbatim` is empty.** The enum has no "no caption" value, so an
uncaptioned grid carries `position: "above"` for shape reasons only. Any count of "captions
above the grid" must exclude rows whose `caption_source` is `none` (6 of the 20 tables in
#288-#290; the page-4 symbol glossary in #135), otherwise the aggregate reports a placement
nobody printed.

## Caption defects that force `typed-from-crop`

A caption is stored as `caption_source: "text-layer"` only while the printed sentence is
also a contiguous substring of the page text. Seven shapes break that, and every one of them
is recorded as `typed-from-crop` with the printed wording, while the row note names the
text-layer form that failed the check. Register a new shape here before using it, so the
same defect is not re-diagnosed paper by paper.

| # | shape | what the text layer shows | example |
|---|---|---|---|
| 1 | word hyphenated across a line break | the printed hyphen plus a space, or a bare space | `distri- bution` (#129), `inter- arrival` and `pas- senger` (#131), `to- gether` (#132) |
| 2 | two captions interleaved on one line | caption N, then caption N+1, then both tails | Figures 7 and 8 (#130), Figures 15 and 16 (#132) |
| 3 | space before the colon | `Figure 6 : Model height diagram` | #286 (mcm-65) |
| 4 | full-width colon | `Figure 10：…` | #286 (mcm-65) |
| 5 | caption runs into the next paragraph, continuation below the artwork | the caption line stops mid-clause and resumes after body text | #287 (mcm-65) |
| 6 | caption wrapped around a two-column body | caption clause, body clause, caption clause | Figure 8 and Figure 9 (#132) |
| 7 | caption printed as unstyled body prose, no break, no marker for where it ends | a clean contiguous sentence that still cannot be separated from the paragraph it sits in | Table 5 and Table 6 (#132), #287 (mcm-65) |
| 8 | one caption printed twice, interleaved word by word | the two copies overlaid by a broken two-column pass, so every other token belongs to the other copy | Figure 7 of #291 (mcm-65) |
| 140 | P-F-2017-68940-3e5f9c47 | 52 | 46 | 11 | 10 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 46 measured regions = 11 figures + 10 tables + 25 exclusions (23 NetLogo code pages pp26-48, the p1 summary-sheet control block, the p2 POLICY ADVISORY banner). The paper is close to captionless: twelve of its 21 exhibits print no caption at all, and the five that do split into two grammars - 'Figure N:' sentences below the artwork (Figure 1, Figure 3 printed once over a three-panel row, Figure 4) and the bare words 'Table 1' / 'Table 2' above the appendix grids. The p16 pair and the p20 triple are single figures whose regions were measured separately, so each set repeats one doc_order and carries `is_panel_of`; neither set shares a y scale, the p20 panels topping out at 200, 205 and 246. Families: six ggplot histograms, one NetLogo life-cycle flow chart, and three line series of which two are pasted screen captures - the p10 Gapminder chart still prints its country chip and time scrubber inside the image, and the p11 Canadian series labels its x axis with bare two-digit years 95 to 15. All ten grids are boxed with verticals at every cell boundary and none is shaded; only the four-column maternity/paternity grid merges cells or carries two header rows. Six grids are announced by a deictic sentence on their own page, two are read only from below, and Tables 1 and 2 are announced on p7 for pp24-25 - a seventeen-page lead. p2 is an A4 sheet inside a US letter document, the paper's one page-size break. |
| 141 | P-F-2017-72197-93a3c66b | 35 | 22 | 18 | 3 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 22 measured regions = 18 figures + 3 tables + 1 exclusion (the p29 footnote block), so every region is accounted for on a paper whose last three pages carry no text layer. The structural finding is a double numbering run: the body captions number 'Figure 1.' to 'Figure 9.' with a period and print BELOW their artwork, while the appendix restarts at 'Figure 1:' to 'Figure 3:' with a colon and prints ABOVE its capture, so one paper carries two 'Figure 1's and the caption side tracks the part of the paper rather than the exhibit type. The citations drift one place ahead of the captions from Figure 4 on - the p13 sentence promises 'Figure 5' for the caption 'Figure 4', p17 promises 'figure6 and 7' for the captions 5 and 6, p19 names no number at all ('(see Figure)') and p21 names 'Figure 10' for the caption 'Figure 9' - so four consecutive cross-references point one exhibit too far. Captions are 6-9 words, never name a unit, a variable or a condition, never conclude, and one ('Figure 7.') is a bare number over a three-series plot the next sentence never describes. Geometrically the paper is one Excel template and one drawn diagram: eight of the nine body figures share a single chart engine (five line charts, three of them staircases of the human-capital distribution, and three bar charts whose only legend is a lone 'Frequency' chip outside the right edge), in-plot titles stand in for captions on eight of the nine, and the ninth is a wage/People schematic cut into labelled Deficit, Tax, GDP and In-Labor-Force regions - the paper's only exhibit with no numbers on it. Nothing is 3-D and no colourbar appears; the only colour scale is the green-yellow-orange-red fill inside the decision matrix. Tables are reduced to one page: p26 is the paper's only landscape sheet and its only grid, and the detector returns it as three separate bands - a weight strip with sliced row labels ('ort Run Valuati', 'ng Run Valuatio'), a 25-discipline by 5-value by 8-application block, and a detached two-column SR/LR score block - which are one table, header band repeating above the first two and the misspelled title 'Weighted Decison Matrix Model' printing under the last. Only those two score columns are decimal-aligned and only there does raw spreadsheet precision reach print (0.316111, 0.055555556). The appendix is three Excel dashboard screenshots (worksheet gridlines, grey header cells, colour-filled inputs, one large black rectangle over half the dashboard) plus a Mathematica plot that still prints the code cells that drew it, and then pp33-35 print five uncaptioned full-page plates that reprint Figures 1, 4, 5, 6, 8 and 9 - the appendix restates what the body already numbered, with no caption, no number and no citation reaching them. Context extraction again missed every heading (`headings=0` against twelve printed lettered sections), so the section paths were taken from the text layer directly |
| 142 | P-F-2017-72283-776dd1c3 | 25 | 14 | 9 | 4 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 14 measured regions = 9 figures + 4 tables + the p1 MCM summary sheet, the only exclusion. The paper has two drawing tools and each tool decides whether an exhibit gets a number. The four raster MATLAB screenshots (Figures 1-4) carry the only figure captions, all printed below their artwork and all in the colon form 'Figure N:', and each carries a legend - a boxed inside legend at upper right on the p6 age pair, and an outside-right legend on the dissimilarity pair whose ten italic entries run wider than the plot they belong to. The five vector charts carry no caption, no number and no frame: two scatters on p10, the Lorenz curve on p13 and the two migration curves on pp20-21. They paste their axis titles at the END of the axis ('Happiness' above the y axis, 'Unemployment Rate' past the x axis), print no plot title, and write thousands with a space, so the two dialects are separable at a glance. Caption side splits by exhibit type, not by part of the paper: all four figure captions below, all four table captions above. Citation runs two grammars and never mixes them within a sentence - numbered ('Looking at Figure 3', 'as follows in Table 1') for the four numbered figures and the tables, deixis ('We see in the figure below', 'The lower curve above', 'This graph shows') for the five unnumbered charts. Two exhibits are never cited at all: Figure 4 and the scenario-1 population curve on p20, both the second member of a pair whose first member is discussed. One cross-reference is wrong - the p18 sentence summarizing the gender/age weights says 'summarized in Table 4' while Table 3 is the grid printed directly under it, so Table 3 is the only table no sentence names and Table 4 is announced twice, on p18 and again on p19 with the words 'shown in Table 4 below'. Tables are announced a page before they print (p17 for p18, p18 for p19) while figures print on or after their lead page, so the two numberings displace differently. All four grids are boxed with a rule under the single header row and a rule between every body row; none is shaded, none merges a cell, none has a two-tier header, none prints a unit in the header, none has a note line and none continues onto a second page. Width is the only table variable - 60 per cent of the text width for the two-column Likert scale, full width for the two five-metric grids. Only Table 4 breaks decimal alignment, its five-decimal 0.78709 sitting right of the six-decimal cells around it, because no grid aligns on the decimal at all. Nothing in the paper is three-dimensional and no colourbar appears anywhere. p1 is the MCM summary form, a control page rather than an exhibit |
| 143 | P-A-2018-76082-bbcfb427 | 25 | 18 | 12 | 1 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 18 measured regions = 12 figures + 1 table + 5 exclusions, and all five exclusions are MathType display equations pasted as graphics (equations 11 and 12 on p8, 18, 19 and 20 on p12), so on this paper the region detector counts inline mathematics as artwork. Every one of the twelve captions prints below its figure, with no table caption to compare against except the paper's only grid, which has none. Numbering is 'Figure N' for ten figures and glued for two - 'Figure1' on p5 and 'Figure6' on p15 - so a grep for either form misses exhibits. The inventory is balanced between drawing and plotting: five drawn schematics (the skywave hop with its hatched layer and d1/d2/theta labels, the double-edged terrain profile, the boat with an x/y/z triad, the curved-earth propagation diagram with receivers RA/RB/RC, and the ionospheric fan under a 'Glide spread' envelope), five MATLAB line plots, one Excel-style bar chart and one surface. Exactly one exhibit is three-dimensional - Figure 3, a flat-shaded sea surface colour-coded by height with no wireframe edges, no axis titles, no colour scale, spikes overshooting the z box, and the worst aliasing in the paper; it is also the only exhibit printing in the bottom third of a page, against seven in the top third. Legends appear on five figures: inside at upper right on Figures 2, 4 and 5, and outside-right on the sensitivity pair where the twelve-entry box overflows the frame. Caption-region hygiene is the weak point. Figure 9 is never cited by its own number - the sentence printed under its caption reads 'shown in Figure 8[15]', the same sentence already used for Figure 8 a page earlier, so the two consecutive schematics share one reference. Figure 6 is announced on p14 as 'a schematic of the Epstein-Peterson method' and captioned 'Double-edged peak diffration', and the same exhibit is cited on p15 in roman numerals as 'Figure VI'. Figures 11 and 12 are announced together by the plural deictic 'as shown in the following figures', Figure 11's legend keys twelve series for two visible traces, and Figure 12's y axis runs 1.6582 to 1.6586 in four decimals on a 0.00006 step so adjacent labels repeat and the axis carries no usable scale. Three references displace by exactly one page (Figure 2 on p8 for p9, Figure 6 on p14 for p15, Figure 12 inside the p20 plural) and no reference displaces further. The p4 notation glossary is two columns and fifteen rows, uncaptioned and unnumbered, announced by a sentence ending in a colon, and is the lane's only grid whose style is booktabs horizontals plus a single internal vertical rule with no side rules |
| 144 | P-A-2018-76271-27d535ab | 31 | 31 | 18 | 8 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 31 measured regions = 18 figures + 8 tables + 5 exclusions, and all five exclusions are pasted LaTeX display equations (3)-(10 on p10, 11-15 on p11, 18 on p13), so the region detector counts a third of this paper's mathematics as artwork. Caption side is decided by exhibit kind and never varies: all eighteen figure captions print BELOW their artwork, all eight table captions print ABOVE their grid, and one numbering grammar covers both ('Figure N.' / 'Table N.', period then space, no colon, no roman, no glue). The tables are the cleanest half of the record - eight grids, one template (outer box plus a vertical at every cell boundary, no booktabs), zero zebra striping, zero merged cells, zero diagonal headers, zero note lines, no continuation, centred rather than decimal-aligned figures - and only width varies: half the column for the two 3-column power grids, 80 per cent for the three 4-column sensitivity grids, full for the four 5-column distance grids. Units move between header, stub and caption consistently except on Table 5, the one grid with empty cells, which is also the only one that prints its unit in the caption. The figures split by tool: five box plots share one glyph (unfilled blue box, red median bar, black dashed whiskers) across seven panels, three terrain surfaces are the only 3-D exhibits and the only ones with a labelled z axis, four exhibits carry colour bars - the two electron-density disks of Figure 8 and the cell grids 12-14 - and nothing else does, so colour encodes a field only where the axes are a parameter plane. Figures 12 and 13 share axes to the tick, but 14 steps elevation by 10 degrees and frequency by 5 MHz, so the three plates in one column cannot be read across. Two figures are captured web basemaps with a map pin and one arrow, printed without axes, scale or legend, and those are exactly the two the text never cites. The appendix is a plate section: all fourteen appendix figures are announced from the body 10 to 15 pages ahead and no appendix page cites another exhibit. Citations are the weak point - the prose prints 'the numerical values are shown in 1' twice on p16, so Tables 1 and 3 are announced without a number and Tables 2 and 4 are never announced at all, leaving five of twenty-six exhibits uncited (Figures 3, 4 and Tables 2, 4, 5). One caption states a result (Figure 15 carries a second sentence) and one caption covers only half its exhibit (Figure 11 plots calm against turbulent water in its left panel while the title names terrain). |
| 145 | P-A-2018-77845-746864a6 | 32 | 43 | 18 | 7 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 43 measured regions = 18 figures + 7 tables + 18 exclusions, and eleven of the exclusions are pasted display equations ((1)-(2) p7, (3)-(4) p8, (5)-(7) p11, (8)-(9) p12, (11) p13, (12) p14) while (10) and (13) alone survive as vector text, so the region detector counts this paper's mathematics as artwork for the fourth time in the batch; the twelfth exclusion is a pasted terrain-category bullet list on p14 and the last seven are the MATLAB code bands of Appendix B on pp27-32. Caption side is invariant and inverted from the table convention: all 18 figure captions AND all 7 table captions print BELOW their artwork, one colon grammar ('Figure N:' 17 times, 'Table N:' 6 times) covering both, and only the appendix's two reprints carry neither number nor caption, announced as 'the following figure' and 'the following table'. Drawing language is one engine - 15 of the 18 figure rows are MATLAB line plots (joined traces, no markers, key inside the top-right corner, no colourbar, no annotated data) and the other three are hand-drawn ray schematics with no axes - and key position is the field that exposes the one borrowed exhibit, Figure 10, whose six-entry key alone sits below its x axis. Panel count is a grammar rather than a taste: 8 exhibits on one frame, 8 on two (1x2 for the parameter sweeps, 2x1 for Figure 16) and only the two propagation-process exercises (Figures 12 and 15) get a 2x2, with the x axis shared inside each column. Every grid is booktabs - no zebra, no merge, no diagonal header, no note row, no continuation - and the only structural exceptions are Table 2's second header band and Table 4's two abutting blocks, Table 4 being the paper's worst defect because its headers are transposed against the columns beneath them ('20M Hz' heads a column of grazing angles, '15' a column of frequencies) and one cell prints '17:65MHz'. Recorded defects: Figure 8's caption is stranded in the gutter between two plots, Figure 16 names three F-layer altitudes and plots two, Figure 14's artwork carries MATLAB data-cursor tooltips burned in as if they were data labels, and Table 5 calls a negative dBw entry a power. Exhibits are announced on their own page or one page early with Figure 4 the only two-page lead; 12 of the 25 sit in the middle band, 10 in the top third, and the 3 foot-band cases (Figure 1, Figure 13, Table 6) close their page with the caption as the last line. |
| 146 | P-A-2018-86103-6d21eb9d | 28 | 34 | 18 | 6 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 34 measured regions = 18 figures + 6 tables + 10 exclusions, the exclusions being the display mathematics pasted as images ((1)-(4) p9, (7)-(8) p11, (10) p12 alone, (11)-(13) p12 inside one band) plus the two MATLAB code bands of pp25 and p27, so the detector reads this paper's equations and its appendix listings as artwork. The finding that makes this paper worth a note is that it runs its figure numbers TWICE: the abstract prints 'Figure 1 The wave situation when the wind scale is 6' and 'Figure 2 The relationship between the wind scale and the first reflection intensity', and the body then re-spends both numbers on 'Figure 1 HF propagation diagram' and 'Figure 2 Inner layers of ionosphere' - four real exhibits, two numbers, and no sentence anywhere reconciles the runs. The abstract also prints its two exhibits in reverse order (Figure 2 above Figure 1) and sets its prose in two interleaved columns, which is why neither thumbnail has a readable lead sentence except 'we analyze the possible superposition of waves, and get the three-dimensional simulation diagram of the waves, and simulate it'. Caption side is the cleanest rule in the batch: side follows exhibit kind, 23 of 23 - all 18 figure captions below the artwork, all 5 numbered table captions above the grid - and the single page (16) that carries both kinds shows the rule twice in one column; the grammar is the barest recorded so far, 'Figure N' / 'Table N' with no colon and no period, a noun-phrase title of 4 to 18 words (median 8) in which exactly one caption names a plotted symbol (Figure 10's 'P1') and none states a unit, a parameter value or a conclusion. Drawing is three tools and the census can name each: six MATLAB surf rows (the abstract surface, Figure 3's four frames - measured as four separate rows because the export left a wide gutter, and the only place where panel_count and doc_order disagree - and Figure 13, the paper's only colourbar, jet, -50 to 100, and its only 3-D exhibit whose vertical axis carries a measured quantity rather than a surface height); four MATLAB line plots whose key sits inside the frame, always upper right for a single frame and lower left for a pair; three pasted Excel clustered-column screenshots carrying their numeric data tables baked in under the plot with dashed leader lines down to them, which means the same chart is printed three times (abstract Figure 2, Figure 10, and Figure 12 with a recast x axis); and five hand-drawn schematics with no axes and no key. Grid style follows the software the same way caption side follows exhibit kind: four native Word tables are booktabs with internal verticals and no outer box, two imported multi-tier grids are fully boxed with a rule at every cell boundary - Table 2 with three header tiers, merged spans and a slanted corner cell, Table 3 with two merged two-column spans and eps(F/m)/sigma(S/m) in the header - the uncaptioned notation glossary on p7 is the paper's only zebra grid and its only note row ('P.s. Other symbols instruction will be given in the text.'), and Table 5 is the only grid with no printed header, its caption welding itself to the first band row. Announcement is always same-page (21 rows at lead 0, the glossary the only row with no mention at all) and 21 of 24 rows are reached by their own printed number, but the prose gives deixis rather than number ('as follows:', 'we get the following chart by calculation:', 'The related parameters are shown in the table.'), and only Figures 7, 12 and 13 get a trail sentence that reads the exhibit back. Recorded defects: p17 announces Table 2 with the wrong kind word, 'The following figure shows the atmospheric noise table'; Table 4's caption prints 'f =15Hz' for a 15 MHz frequency; Table 1 prints 'w' for watts; Figure 4's decomposition tree labels the ionospheric term 'La' while equation (5) directly above it writes 'Li'; Figure 11's right frame is titled 'sea surface reflection loss' on a ground-reflection chart because the plot was cloned and one axis title never edited; Figure 13's x ticks print '00' for the leading zero; Figure 12's x title sits below its own embedded data table; Table 3's caption is a formula fragment with no verb; and a red Chinese shop-watermark band crosses the running header on every page. |
| 147 | P-A-2018-88255-2023cf14 | 21 | 35 | 19 | 1 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 35 measured regions = 19 figure rows + 1 grid + 15 exclusions, and the exclusions are of four kinds inside one document for the first time in the batch - eight pasted display-mathematics regions ((2) p5, (5)-(6) p6, (9)-(13) p8, (14)-(15) p9, (16)-(19) p11, (22)-(23) p12, the attenuation factor and (25) p13), one raster copy of the Fresnel pair, one running-header and heading rule band on p5, one caption band on p8 and three raster interiors of vector figure frames on pp18-19 - so this is also the cleanest case of the detector measuring one image twice, and the paper's mathematics is counted as artwork for the fifth paper running. Caption side follows exhibit kind and INVERTS between kinds instead of moving as a block: all 19 figure rows print their caption below the artwork and the single grid prints its caption above, which makes the paper's only table its only above-caption and the exact opposite of #145 where every exhibit was below. The numbering grammar is one colon form ('Figure N:' 18 rows, 'Table N:' once) with one exception that no vocabulary covers - Figure 6 prints the batch's first full-width colon, 'Figure 6：The relationship between Lcal or Ltur and f', so the field records the bare 'Figure N' and the note carries the punctuation. Captions are noun-phrase or single-clause titles of 7 to 27 words (median 15); 11 of 19 name one to four plotted symbols (Lbf, Lcal, Ltur, Lt, n, f, eps_r, sigma) and 10 of 19 pin a parameter setting in the caption itself, but none states a unit and none concludes - what the paper does instead is print a second caption line on the three hop-budget figures ('n: number of hops, f = 3MHz, reflected by calm oceans'), the only place those plots' setting is written down. Drawing is one engine and one hand: 14 of 19 rows are MATLAB line plots with the key always inside the frame, 4 are hand-drawn ray or wave schematics with no axes and no key, and 1 is the paper's only 3-D exhibit - Figure 3's four surf panels in a 2x2 grid on four separate z scales with no colourbar, so the wind-speed order survives only inside each rotated z label and the height field is unreadable. Panel grammar is thin and unlabelled: Figure 3's four panels share one region, Figures 5 and 12 are each split into two rows by the export gutter, Figure 9 borrows one altitude strip across its pair, and the only panel labelling anywhere is the words '(left)' and '(right)' inside Figure 12's caption. The single grid is booktabs with two header rows and merged spans (Geology across both, eps_r and sigma each over a Range/Average pair) and nothing else - no zebra, no slanted corner, no verticals, no note row, no continuation, no unit in either sigma column. Two house templates are reprinted: the hop-budget frame appears FOUR times (Figure 10 calm sea n=1..8, Figure 12 left smooth n=1..8, Figure 12 right rugged n=1..5, Figure 13 shipboard n=1..5, all with the same dashed 150 dB threshold) and the received-power frame TWICE (Figures 7 and 11, sea states against terrains, sharing the misspelt axis 'frequence / (Hz)' in a 3-30 MHz paper). Announcement is same-page for 14 rows and one page early for 4, and two exhibits are never cited from the body at all - Figure 2, a geometry schematic, and Figure 9, a borrowed textbook plate whose caption carries the reference. Recorded defects: Figure 2's label chain reuses theta for the incidence angle and the refraction angle, Figure 4 draws no normal vectors in a section about normal-vector distributions, Figure 5's panels differ by two orders of magnitude (0.12 against 12 dB) with only tick labels to say so while its caption calls the turbulent surface 'tough', Figure 7's key reads 'clam oceean', Figure 10's y title reads 'attennation' and its x10^4 multiplier contradicts the '(km)' unit in its caption, Figure 11's key reads 'rugid terrain', Figure 13's five arcs do not meet and leave two thirds of the frame empty, Figure 14's tick values (2767, 5786) are transposed against the prose's own ranges (2676, 5768) with no key for its red spans, Figure 16's caption stutters and its four curves overlap so completely that a 20 percent perturbation is invisible, Table 1 gives no unit for sigma, and a red Chinese shop-watermark band crosses every running header. Coverage gap: the fifteen-row two-column 'Abbreviation / Full Name' glossary at the top of p5 is a real table the layout does not contain at all - the detector boxed the rule band above it - so the region pass follows images rather than tables. |
| 148 | P-B-2018-73410-069a3764 | 28 | 47 | 12 | 12 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 47 measured regions on 23 pages = 24 exhibit rows + 23 exclusions, and every exclusion is display mathematics - (1) p5, (2)-(6) p6, the 22x22 matrix (7) p7, the rate definitions p8, the eigenvector p9, the block transition matrix and (14)-(15) p12, the English-only matrix p13, the initial vector and similarity parameter p14, (17) p17, (18) p18 and the weight coefficients pp19-20 - the fifth paper running where the detector counts equations as artwork and the cleanest case yet, because the mathematics is typeset live rather than pasted (decimal points print as colons: 'k = 0:1', 'when > 0:021') while the region pass boxes it anyway. Caption side is one convention for both kinds: all 12 figure captions below the artwork and all 5 captioned grids below their last rule, which repeats #145 and inverts #146 and #147, so 'tables above' is one paper's habit rather than a batch rule. This is the first paper in the batch whose grids are MOSTLY uncaptioned - seven of twelve carry neither number nor caption (the symbol grids of 2.1.1, 3.1.2 and 4.2, the 2017 and 2067 office grids of 4.3, both Memo grids) and are recorded with an empty caption block and caption_source 'none', because a census of what was drawn cannot skip the grids without numbers. Numbering is therefore one colon grammar twice over and only five times on the table side: 'Figure N:' twelve times, 'Table N:' five, no roman, no period, no other form. Captions are one-line roman titles of 9 to 19 words on the figure side and 9 to 15 on the grid side; none states a unit, none concludes, only three name a parameter ('When k=0.1', 'When k=10', 'Top 6 to 16 Language Groups'), and no captioned grid names a variable at all. Drawing is one engine and three idioms plus one exhibit the vocabulary cannot name: 7 of 12 figures are MATLAB line plots, 2 are hand-laid state-transition graphs (Figure 1's diamond of Y1/Y2/y1/y2 with self-loops 1+alpha11-beta11, 1+alpha22-beta22, 1-beta33, 1-beta44 and edges gamma32, alpha24, alpha13, gamma41, and Figure 3's eight-state ring with alpha-bar, p12a2, 1/(sigma2 d12), p21a1, r1, r2, 1/(sigma1 d21) as stacked fractions), 2 are 2x5 appendix plates of ten titled panels, and 1 is a PIE CHART (Figure 6, eleven wedges labelled outside the circle, no axes, no values) filed 'other' with an other_note because no FAMILIES member covers a share-of-total diagram. Nothing is three-dimensional and no colourbar appears anywhere - no surf, no heatmap, no contour - so every quantity is read off a position against a printed tick; keys are rare and never inside the frame (Figures 7 and 8 key twenty-six curves in a bordered box OUTSIDE the plot area at the upper right, illegible at print size), seven figures label marks inline, three carry neither key nor label, and shared axes are used zero times in the whole paper while the two plates repeat 'Time/year' and 'Death rate/%' panel by panel with no panel letter anywhere. The grid side is invariant booktabs across all twelve: three horizontal rules, no vertical at any cell boundary, no outer box, no zebra, no slanted corner - including the four whose content reaches the layout as raster. Merged cells appear exactly once (Table 1's 'Language' spanning both header rows, the four measure labels wrapping inside the second), header depth is one row for eleven of twelve, only the two office grids add a footer band (a rule above an 'Accumulated scores' totals row), no grid prints a source line or a note row that reaches the text layer (the paper's only note-like line is the closing j = 0 definition inside the section 4.2 raster), and grid width splits by function rather than size - Table 1 wraps at about 60 percent of the measure while the 17-row symbol grid and the 19-row economic table run full measure. Announcement leads the artwork here more often than not: 5 of the 9 cited rows are named a page early (Figures 3, 4, 5, 6, 8), 4 on their own page (Figures 1, 2, 7 and Table 1), citation vocabulary is a parenthetical rotation (8 of 9 rows introduced by '(Figure N)' or '(Table N)' glued to a sentence end, Figure 3 the only as-shown-in construction), and 15 of 24 rows are never cited from the body at all - Figures 9 to 12 and the eleven uncaptioned or appendix grids, reached only by 'See: Apendix B', 'See: Appendix A' and 'the data in 2013 is in Appendix A'. Recorded defects: Figure 2's caption prints 'Rate ( )' where the learning-rate symbol fell out while the axis title keeps 'Learning rate(gamma)'; Figure 9 is captioned Birth Rate while all ten of its panels read 'Death rate/%' and Figure 10's panels read the same, so the two plates cannot be told apart from their labels; Figures 11 and 12 truncate their y axes at 50 and inflate every trend; Figure 11 inline-labels fifteen languages against a caption promising ranks 6 to 16 while Figure 12's ten match its title; Figures 7 and 8's twenty-six-entry outside keys are a grey blur with the bottom eighteen curves merged below 350 million; Table 1 prints '?' in both non-native Japanese columns; Tables 6 and 7 share one caption word for word with BOTH eta glyphs missing so the weighting condition prints as '1 = 2; 2 = 3 = 1'; Table 8 prints Spain twice plus 'Rassia' for Russia and 'Bengaladesh' for Bangladesh with 17 to 19 significant digits; the Memo grid misspells Berlin as 'Beilin'; the section 2.1.1 grid spends 'ii' on two different rates, the 3.1.2 grid flips its own subscript ('0 < p_ij < 1' in the p_ji row), the 4.2 grid puts a unit on two rows and none on the other six; and a red Chinese shop-watermark band crosses every running header. Two coverage gaps: Tables 2, 3 and 5 are printed text tables with rules that the layout does not contain at all - the region pass boxed only Table 4 on p25 because that one happens to be raster - so the detector follows images rather than tables for the second paper running; and three measured boxes cut across printed objects (the p25 box runs from Table 3's caption through Table 4 into Table 5's header, and the p20 and p21 boxes each hold one office grid plus four rows of the next). |
| 149 | P-B-2018-74316-1198d12d | 39 | 115 | 56 | 35 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 115 measured regions on 32 of 39 pages (28 printed, p9 blank apart from the watermark) = 91 exhibit rows + 24 exclusions, and the exclusions are of three kinds - eleven display-mathematics regions (the FPE/AIC/BIC criteria and the co-integration relation p7, the ECM derivation p8, logistic growth p10, the piecewise total-speaker system and the d2N/dt2 conditions p11, the 226x226 transition matrix with the n-step matrix, the population recursion and the steady-state product p16, the M0 matrix p17, the fuzzy relation p20, the density and MIC definitions p21), six caption bands of the Appendix-1 correlograms that the detector boxed separately from the plots, and five column slices of the two 54-row panel tables - so this is the sixth paper running where the region pass reads equations as artwork, and the first where the same printed object is measured three or four times because the raster is wider than one box. Caption side follows kind and the appendix inverts it: 41 of 56 figure captions print below the artwork and all 15 above ones are appendix plates captioned by their Appendix heading, grids 25 below and 10 above. Numbering is broken three ways at once - 32 'Figure N:' against 24 unnumbered, Figure 12 printed twice (p13, p14), Figure 5 twice (p6, p30), Figures 19 and 20 out of order on p21, one map captioned with the bare word 'Figure', and the appendix re-using a body number as 'Table2:' with the colon glued to it. Units reach 3 captions out of 91, no caption names a plotted variable, none concludes and none states a condition. Drawing is MATLAB throughout: 19 line plots, 17 plates, 12 surface meshes, 4 dendrograms, 2 schematic lon/lat maps, 1 bar chart and 1 scatter, with no histogram, box plot, heatmap, contour or pie; the 14 three-dimensional exhibits (12 surface figures plus the 2 Appendix-13 plates) are all longitude/latitude meshes and none carries a colourbar, so absolute value sits on height alone; keys are 32 inside, 17 none, 3 above, 3 outside right and 1 outside left; panels are a single frame (39), a 1x3 correlogram strip (10), a 1x4 or 2x2 sweep (4) or a 1x2 pair (3), always identified by inline text rather than a panel letter. The grid side is 23 booktabs, 11 boxed and one vertical-rules outlier (the Appendix-12 coordinate blocks), with 6 merged grids, 3 two-row headers, 23 decimal-aligned grids and 35 of 35 at full measure. Announcement is the batch's outlier: only 3 of 91 exhibits are named in prose and two of those are re-read after they printed, no figure is ever cited by number, and the two trail sentences that exist weld a formula number to a table name. Recorded defects: Figure 15's class breaks overlap so its legend is not a partition, Figure 18's four dendrograms span three orders of magnitude with no axis titles, Figure 20's caption is cut at 'Geographic Distribution of 8', Figures 7 to 9 lose their delta and mu glyphs, Figures 19 and 21 plot the same MIC surface on different z windows, Table 13 loses every symbol except 'P' and 'I, J', and Table 2 is three stacked 17-row bands read as one 51-row table. Coverage gaps: the eight pasted raster appendices are dimensioned from the render because their text layer keeps only what OCR reached, Appendix 6's six dumps are one printed table inside six boxes, and page 1 carries 21 paths but no measured region. |
| 150 | P-B-2018-77238-4380ec81 | 23 | 50 | 18 | 19 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 50 measured regions on 18 of 23 pages = 37 exhibit rows + 13 exclusions (nine node-box fragments of the two flowcharts, one caption band under the p9 map, three display formulas on p11). Caption side is kind-driven and invariant here: 18 of 18 figures below the artwork, 17 of 17 captioned grids above the box, plus two uncaptioned blocks (the Notation grid, the memo's answer grid). Numbering is plain - 'Figure N' / 'Table N', no colon, no period, 35 captions, nothing reprinted. Drawings split along the paper's own seam: schematics and two small grids in the model half, six 16-curve line plates plus three bubble-and-name maps plus a node-link example in the solution half, grids only in the sensitivity half, and an uncaptioned flow map before the memo's booktabs answer grid. Nothing is three-dimensional and no exhibit carries a colourbar. Grids are 17 boxed against one booktabs and one vertical-rules outlier (Table 11, open right and bottom), merged in three grids, decimal-aligned in none, unit-in-header in one (Table 2). Coverage gap: seven of the paper's fifteen numbered tables are native text the region pass never boxes. |
| 151 | P-B-2018-79002-238b850f | 29 | 43 | 20 | 17 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 43 measured regions on 21 of 29 pages = 37 exhibit rows + 6 exclusions (five display-equation rasters and one prose region). Caption side is kind-driven: 19 of 20 figures below the artwork, 17 of 17 tables above the grid. Numbering is the bare 'Figure N' / 'Table N' and reaches only 15 figures and 15 tables. Grid form is one hybrid repeated 16 times - three horizontals plus a single stub divider - with the Table 4 continuation as the only exception. No zebra, no merged cells, no diagonal header, no decimal alignment anywhere; units migrate between caption, header cell and screenshot header. Families: composite-panel 5, map-or-plan-view 4, table-as-figure 5, other 3 (screenshot pie/donut), scatter 1, node-link-network 1, bar 1. Every exhibit is a pasted raster except the p7 network; no 3-D, no colourbar. Figure 5 is one object in two region boxes. Not one exhibit is cited by its own number: the prose points at Figures 3, 14, 17, 18 and Tables 7, 9, none of which exist, and every one of those holes is exactly where a cross-reference lands. Both page-crossing tables (4 and 6) continue headerless with no caption |
| 152 | P-B-2018-91566-2607f7ec | 26 | 24 | 7 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 24 measured regions on 15 of 26 pages = 12 exhibit rows + 12 exclusions, because the paper pastes nearly every formula as a raster (pages 12, 13, 14 are each one page-sized screenshot of prose plus math) so half the regions are displays. Caption side is kind-driven with no exception: 7 of 7 figures below, 5 of 5 tables above. Numbering is the colon form 'Figure N:' / 'Table N:' - the first paper in this lane to print it - and three appendix fragments go unlabelled. All five grids are booktabs, horizontal rules only: the first zero-vertical-rule paper here. Families: composite-panel 5, flowchart-or-schematic 1, node-link-network 1; no 3-D, no colourbar. ONE region holds TWO printed figures four times over (3+4, 5+6, 7+8, 9+10), so region counting understates the printed figure count by four, and the paired caption lines are physically broken (no separator on p16/p18, 'Proportions inFigure 6' plus a wrapped '2068' on p17) - map captions to panels by horizontal position, never by line adjacency. No table is ever cited by number. Coverage gap: Table 2 and Tables A1/A2/A5/A6/A8 are native text columns the region pass never boxes |
| 153 | P-C-2018-72969-f2349d15 | 30 | 57 | 13 | 8 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 57 measured regions on 23 of 30 pages = 21 exhibit rows + 36 exclusions, split into 19 panel fragments (the detector boxes each panel of a composed figure separately) and 17 non-exhibits (ten pasted 87-92 dpi strips of prose and display maths on pp9/11/12/13/15/16/17/18/19, plus the three MATLAB appendix listings on pp26-30 boxed as seven table-like regions). Region count is more than double exhibit count. Caption side is kind-driven with no exception: 13 of 13 figures below the artwork, 8 of 8 grids above. Numbering is the colon form on all 21 and 17 of the 21 captions run under twelve words. All eight grids are booktabs with no vertical rule and no zebra; two grids carry two header rows and both are stacked blocks over one shared stub set (Table 3 ten item names twice, Table 4 eight factor names twice); merged cells appear once (Table 8's NM/TX spans); nothing is decimal-aligned and no unit sits in a header. Families: line 5, flowchart-or-schematic 3, scatter 2, heatmap-or-contour 1, bar 1, other 1 (four radars, a type the vocabulary does not name). 10 of 13 figures are multi-panel and the 1x3 row is the standard, used five times. Nothing is three-dimensional; one figure carries colourbars. Mentions: 12 of 13 cited, six same page, four one page early, two one page late (Figures 2 and 9 cited AFTER they print); Figure 6 never cited; three figures get no reading sentence. Coverage gap, declared not patched: Table 2 (p7) and Table 7 (p20) print with captions but own no region, so 8 of 10 printed tables are recorded, and Figure 2's swatch key, Figure 11's shared legend and Figure 12's legend plus fourth radar all fall outside every box. Traps: panel indices are not reading order (p18 stored right-to-left, p13 row-major by x only, so panel (a) is region 3 on both); p12 r1 is a second placement of p11 r2's image, which is why equations (11) and (12) are printed nowhere |
| 154 | P-C-2018-73767-a72d3a8a | 29 | 35 | 19 | 10 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 35 measured regions on 20 of 29 pages = 29 exhibit rows + 6 exclusions, and here the surplus runs the other way: the six are display maths and pasted prose (equation (1) p8, equation (2) p11, the three-equation block (3) p12, the standardisation block (4) p14, the fifteen-line prose-plus-equations raster p15, and p17 as one 0.555-area strip), and NO region holds two printed exhibits. Caption side is NOT kind-driven: 19 of 19 figures and 9 of 10 grids are captioned below, Table 16 alone above. Numbering is the colon form on all 29 and every caption is a verbless lower-case noun phrase of 2-8 words. Eight of the ten grids are closed boxes with full-height verticals; one plain frame (Table 2, side rules and no internal vertical) and one booktabs grid (Table 8); zebra shades exactly one (Table 9, also the only decimal-aligned one); six grids merge header cells; five carry two header rows and all five are group-spanner blocks; no unit ever enters a header - the three appendix grids put it inside every cell. Families: line 6, bar 4, other 4 (four pies - a chart type the closed vocabulary does not name), scatter 2, flowchart-or-schematic 2, map-or-plan-view 1; nothing 3-D, no colourbar anywhere. Legends 8 inside, 7 absent, 4 outside-right, and the two bars with no key are the same chart as the bar that has one. Mentions: only 7 of 29 exhibits are cited by number and 22 are read cold, every appendix exhibit among them; six citations land on the exhibit's own page and Figure 5 is the exception, cited at the foot of p12 and printed atop p13. Coverage gap, declared not patched: eighteen tables print with captions, ten are boxed - Tables 3/13/15/17 are one boxless 'cutline' key plate four times (stale 'in Figure 2 and Figure 3', misspelt 'Fuel enthanol'), Tables 4/11/12 are native text grids, Table 7 prints above the p15 raster's box edge, and Table 8 has a region only because a page-sized prose strip swallows it AND its caption - p18's text layer loses its whole upper half, so that caption is typed from the crop. Traps: the key plates reuse figure numbers already spent on pp9/10/24/25/27/28/29, so eight numbers appear twice in a naive caption scan; 'Appendix C Profiles of Texas' prints at the foot of p26, four pages before its exhibits; p19's two scenario boxes share 95 per cent of their y extent and separate only in x; Table 16 reprints California's numbers under a New Mexico caption and Table 18 alone drops the 'Data from 1960 to 2009' spanner |
| 155 | P-C-2018-78577-919f0d0f | 27 | 36 | 20 | 7 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 36 measured regions on 16 of 23 pages = 27 exhibit rows + 9 exclusions, the surplus coming from BOTH directions at once: six rows are panel boxes (p9 boxes each four-panel strip as four separate bitmaps, so Figures 1 and 2 spend eight regions for two printed exhibits) and the nine exclusions are five raster strips that are not exhibits (two Summary paragraphs p1, equations (2)(3)(4) p13, equation (5) p14, prose plus equation (6) p16, equations (7)(8) p20) against four duplicate detections of an already-claimed exhibit (p10 r3/r4 the raster layer inside Figure 3's axis box, p15 r3 over Figure 9 at IoU 0.93, p18 r3 nested 96 per cent inside Figure 13). Fourteen printed figures and nine printed tables fill 21 boxes; Tables 4 and 5 print above every box on p15 and are declared unboxed. Caption side is kind-driven without exception - 20 figure rows below, 7 table rows above - and numbering is the colon form on all 27, every caption a verbless 4-8 word noun phrase, only Figure 12 naming a variable symbol, which is why Figures 13 and 14 share one caption verbatim. Families: bar 10 (8 of them strip panels), line 9, flowchart-or-schematic 1; nothing 3-D, no colourbar, printed numbers on every chart but the schematic. Legends 11 inside (ten upper-right, one upper-left on the only stacked bar), 9 absent, and in five of those nine the gap is the defect. Tables split 4 booktabs / 3 with an internal vertical, 2 full-measure / 5 at 0.49-0.81, one unit-in-header (Table 2) against two unit-in-stub grids, two decimal-aligned, and zero zebra, merged cells, diagonal headers, landscape grids or continuations. All 14 figures and 6 of 9 tables are cited by number; the glossary never is; three pointer shapes - figure first, figure as subject, figure last - plus two exhibits reached from inside a subordinate clause. Defects: Figures 4 and 9 print 0.000 per cent data ink while the prose ranks four states from Figure 9; Figure 14 reuses Figure 13's caption; x ticks of Figures 3/4/9 are unreadable glyph clusters and the fuel category is misspelt 'PATROLEUM' in all eight panels; Table 8 glues wind and solar into one row label; Table 9's two totals both fail to foot. Traps: page 1 is a letter-format cover against 595.5x842 elsewhere, so two page geometries; p1, p16 and p20 lose whole blocks from the text layer and Figures 12/13 bake their ticks into the bitmap; p9's region indices are not reading order (Figure 1 runs r2, r1, r3, r4); p15's Table 4/5 captions and bodies sit above every detected box |
| 156 | P-C-2018-80560-ad2eea75 | 27 | 35 | 23 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 35 measured regions on 18 of 27 pages = 23 figure rows + 5 tables + 7 exclusions, with the region count off in both directions at once. Four boxes hold two separately captioned printed figures each (p16 r1/r2 = Figures 15/16 and 17/18, p18 r1/r2 = 20/21 and 22/23), so 23 rows cover 27 printed figure numbers; and Figures 3, 5, 7, 8 and 13 are grids sold as figures, so five rows are `table-as-figure`. No duplicate and no nested box anywhere. **Two pages are pasted page images** (83 characters of text layer each): p13 carries Figure 14's 3x5 regression grid, its caption and an unnumbered `Model Parameters` grid; p14 carries prose and equations (8)-(12) and nothing else. The 5.2 heading lives only in that raster, so Figure 14's caption is `typed-from-crop` and every 5.2 row takes the last numbered heading the text layer prints. Three printed grids have no caption at all - the p13 parameter grid and **both p21 results grids**, which are raster images the prose calls `these figures` - recorded with `caption_source` none. Caption side is uniform and inverted against the lane habit: all 25 captioned rows print BELOW their artwork, tables included. Citation is deictic throughout - 31 rows carry an empty style list, count 0 and a null first page - and the single printed number reference, `Figure 9-12` on p15, points back at four figures already drawn, so it is Table 2's trailing sentence. Families: table-as-figure 5, line 6, composite-panel 5, flowchart-or-schematic 2, map-or-plan-view 2, bar 2, other 1 (Figure 4's four bar-of-pie panels, the paper's only 3-D exhibit - perspective pies with drop shadows, `three_d` `perspective-bars` with the deviation stated). Grids: `boxed` 2, `vertical-rules` 3, all portrait, none continued. Traps: Table 2's two-level header is a FALSE spanner (state names centred in their 2025 column, the 2050 header cells left empty) and the grid overruns the right margin by 72 pt; no grid prints a unit in its header and none aligns on the decimal point; Figure 5's caption binds to the wrong box (the band also falls inside Figure 6's region); the map credit on p8 owns no region at all; Figure 20's legend says `Negative Demand Shock` against a caption that says supply; Figures 19 and 27 plot an index 0-80 against captions that say 1970-2050, while Figure 18's right panel uses decimal years; Figures 24/25 show six clean categories normalised to 1.0 against Table 2's ten; Figure 19 is monochrome with ~4 pt type; the p13 parameter header prints `Detotation`; and the p27 appendix line prints in red (224,0,0) |
| 157 | P-C-2018-82150-43b69981 | 37 | 55 | 14 | 12 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 55 measured regions on 31 of 37 pages = 14 figure rows + 12 tables + 29 exclusions, and the miscount is on the TABLE side: three printed tables have no row of their own. Table 3-2 prints on p6 at y216.7-230.0 between two measured boxes; the appendix TEC grid prints at y608-718 just below a box that fuses two other grids; and the appendix unit-price grid is fused INTO p24 r1, which spans y55.6-576.0 and carries both it and the 21-row sector grid - **the join between region and exhibit has to be made grid by grid, never box by box**. **The appendix is not images** but 0.5 pt vector FRAMES round live extractable code: pages 24-37 return zero images, no `fill-image`, and 17 page-height frame regions (byte-identical at (90,72)-(506,759) on 8 pages), all excluded `not-an-exhibit`; the four real appendix exhibits are rule-only grids titled `Table:` with no number, so numbering `none`. Table 2-1 (nomenclature) is the paper's only exhibit that owns its caption - the grid is one JPEG with the title inked inside the box - so its caption is `typed-from-crop`. Other traps: p11 r2 is a nested second detection of Figure 4-9 and p7 r3/r4 are rasterised rotated axis-label strips of Figures 4-1/4-2 (fragment/duplicate); nine more regions are prose or display maths; p14's text layer returns 1,572 characters for ~40 printed lines and p16's coefficient matrix and p18 equation band never reach the layer. Caption side splits by type - 12 tables above, 13 of 14 figures below (Figure 4-5 above). Families: line 6, bar 5, map-or-plan-view 2, flowchart-or-schematic 1; the two maps are the paper's only colourbars and nothing is 3-D. Grids: booktabs 11, vertical-rules 1, one merged cell (the sector grid), no unit in any header, no decimal alignment; five grids overrun the 424 pt measure and Table 4-1 overhangs the LEFT margin by 21.6 pt. Citation: 8 of 26 rows numbered, 18 deictic, and two references arrive after the artwork - so one row has lead_pages 0 and one -1 |
| 158 | P-D-2018-73156-1a30e830 | 29 | 31 | 10 | 8 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 31 measured regions on 18 of 29 pages = 10 figure rows + 8 table rows + 13 exclusions, with 16 printed exhibits and the surplus running in BOTH directions. On the exhibit side Tables 5 and 6 are each **one caption over two separately boxed grids** (goodness-of-fit + maximum-likelihood, 30 pt apart), so p24's four boxes hold two printed tables and the region-to-exhibit join must be made **grid by grid**. On the exclusion side the paper pastes its MATHS as rasters: p10's whole optimisation model and p13's suburban model are images while the rest of the maths is vector, p13 r1 is a `s.t.` spill of a p12 block, and p15's three logistic regressions, p18's Minkowski distance and p19's standardisation are display bands boxed for being the widest ink on the page - four equation images plus three equation bands, all `not-an-exhibit`. **The appendix is code, not figures**: pages 24-29 return zero image XObjects and no fill-image; p24 holds the only printed grids and p25-29 a two-column MATLAB listing plus the SAS run that made Tables 5/6, framed by a stroked rectangle on p25 and hairline fills on p26-29. **This is a watermarked resale scan and the watermark is the trap** - the Chinese shop line prints above nine region-bearing pages and the detector reads it as `caption_above` four times over a raster and five times over a code frame; it is never a caption. **Caption side is the cleanest split in the run so far**: all 10 figures below, all 8 table rows above, no exception - including Figure 8 and Figure 10, which open their pages with the box in the margin above the ink and still keep their captions underneath. Only TWO exhibits are ever named by number ('as shown in figure 2', 'From Figure 3'); the other 14 arrive by deixis or not at all; Figure 8 is introduced on p16, Figure 10 on p18 (lead 1 each) and Tables 5/6 on p15 as 'the test results are shown in the appendix' (lead 9). Families: map-or-plan-view 4, line 4, node-link-network 1, scatter 1 - no bar chart, no colourbar, nothing 3-D, every figure single-panel, legends inside on 2 and absent on 8 because series are labelled INLINE. Grids: boxed 6, booktabs 1, vertical-rules 1; SIX of eight print NO header row; Table 4 is the only true row shading (inputs against outputs) while Table 2 shades COLUMNS 10/30/50/90~100 in both rows and breaks at 70/80; appendix grids are the only merged cells and the only two-row headers; no unit in any header, no decimal alignment, seven of eight grids at 72-81 per cent of the measure and Table 2 alone at 99 |
| 159 | P-D-2018-78826-ed3ee7b7 | 23 | 39 | 26 | 7 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 39 measured regions on 17 of 23 pages = 26 figure rows + 7 table rows + 6 exclusions, for 24 printed exhibits, and **the surplus of nine rows is custody**: Figure 4.1 is **six separately pasted panels** in a 3x2 paste (caption 6.2 pt under the bottom-right one, and two of the six panels are EMPTY - axes drawn, no series), Figure 4.8 is three boxes across the top of p12, and Appendix 2 is three stacked array screenshots. **The paper pastes its prose as rasters**: p6/p7 hold the pixel-honeycomb derivation, p11 three paragraphs plus four formulas, p12 the logistic model, p14 the 4.3.1 cost factor and p15 the P/TC/AI formulas; p7 returns **no text layer at all**, and its 497x652 pt box would read as the largest figure in the paper to a regions-only census. **Wider box, wrong exhibit, three pages running** - p15's 497x278 pt formula paste is not Figure 4.11 (the 345x146 pt bar 87 pt below it is), p14's wide box is the 4.3.1 paste and p11's is the service-capacity prose. **Four exhibits print no caption at all**: the p4 symbol table (a 581x355 printed bitmap with its title baked in, recorded with `caption_source` none), the p5 control block diagram, the 4.3.2 decision chart and the handout's three-segment range aid. **Appendix 2 is not what its title says** - 'The location of charging stations in Lubbock, US' over three numeric-array screenshots - and Figure 4.8's third panel is bit-identical to Figure 4.7 (one image object printed twice under two numbers). Same Chinese resale watermark above nine pages, plus a caption lie native to this paper: `Figure 4.5.` at the foot of p8 is the last line of a body paragraph, flush left - 18 caption strings, 17 captions. Caption side inverts at the appendix: every numbered body figure below, Appendix 1 and Appendix 2's three boxes above, all 7 tables above. Families: map-or-plan-view 8, line 7, bar 3, flowchart-or-schematic 3, table-as-figure 3, composite-panel 1, scatter 1; **no legend on any of the 26**, no colourbar, nothing 3-D, nine explicit panel rows and three two-panel composites. Grids: boxed 6, booktabs 1; **five of seven print a real header row** - the opposite of the lane habit - the exceptions being the symbol bitmap and Appendix 3's 31-row, 62-entry list; no zebra, no merged cell, no diagonal, no unit in any header, no decimal alignment; 83-88 per cent of the measure for six grids, Appendix 3 alone at the full 459.3 pt. Citation: 17 of 33 rows numbered, 12 distinct exhibits named, eight of them inside 4.1/4.2 where one sentence names two; Appendix 3 promised on p11 and printed on p23 (lead 12); no exhibit ever cited twice. Captions: median 10 words, longest 15, voice `none` on all 29, and Table 4.1's Rural total is wrong (1.20 + 0.04 prints as 1.20) |
| 160 | P-D-2018-80386-b757100d | 25 | 29 | 13 | 2 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 29 measured regions on 14 of 25 pages = 13 figure rows + 2 table rows + 14 exclusions, and **the surplus runs the other way for the first time**: twenty printed exhibits, fifteen rows, because the paper typesets none of its mathematics and pastes every derivation as a raster. **Both largest boxes in the document are non-exhibits** - p5's 425x409 pt symbol table (34.72 per cent) and p12's 445x391 pt (34.71 per cent) which is **section 5.2.4 pasted whole**, heading included. **Six captioned exhibits own no region**: Figures 3 and 4 print only a merged caption line on p10 with no artwork on the page at all, and Tables 3-6 are three-band text blocks the region pass never clusters (p22's '22 paths, no region' is its stacked Table 5+6). **The numbering is one level off and the TOC lies**: '4 Model Parameters' and '5.2.4 Commercial Model' exist only inside bitmaps, never in the text layer. Three pages print **two captions on one line** (p10, p15, p16), so the join is made on the caption fragment's x-range. Families: line 7, scatter 5, map-or-plan-view 1; the five scatters are one bare-X/Y discriminant template at four countries with no legend, no title and **no shared scale**; legends 8 none / 3 inside / 1 outside-left (Figure 7's stepped Gini band stack) / 1 below; **no colourbar anywhere** and nothing 3-D. Figures 13-15 are native vectors, so axis numbers leak into the text layer ahead of the caption, and Figure 15 measures as three regions because two bitmap patches sit on top of its own plot. Figure 6's caption still says 'Data analysis of the figure X.' Grids: **booktabs 2 of 2 with zebra on both** - the previous paper had zero - an 18x3 symbol table with the unit in a real column and a 4x3 decimal-aligned result grid at half measure; the four unmeasured grids are 12x4, 7x2, 5x2 and 5x3. Citation is degenerate: **one numbered reference in the whole body**, and it leads by -1 page; 11 lead sentences, zero trail sentences, no exhibit named twice. Captions: 13 figures below, 2 tables above, median 7 words, voice `none` on all, no unit/variable/condition/conclusion |
| 161 | P-D-2018-81402-e1ca1921 | 29 | 20 | 12 | 2 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 20 measured regions on 15 of 29 pages = 12 figure rows + 2 table rows + 6 exclusions, for 19 printed captions, so **five captioned exhibits own no region**: Tables 1-4 and 7 print as **bare unruled text with no table object at all** - Table 3 is one text block holding its own caption plus six rows, caption welded to row one at 1.5 pt overlap - and the page has exactly one drawing object (the header rule). Only Tables 5 and 6 are ruled, both as **closed boxes** (frame + every column + every row), the inverse of #160's booktabs, transposed layouts 4x6 and 5x7 with a YEAR header row. **Caption side is uniform**: all 12 figures and both tables below - the first paper in this block where figure and table captions agree - with gaps 10.6 to 58.3 pt (Figure 7's 58.3 pt the widest in the census). The model half **pastes its maths**: pp6-8 are three text regions and p10's is the EX1-EX4 payoff derivation while the Nash tables print 328 pt below it. Families: scatter 5, surface-or-3D 2 (perspective mesh, grid walls - the only 3-D), contour 2, line 2, schematic 1; **no colourbar on either filled contour**, so half of each surface/contour pair is unquantified; legends 9 none / 3 inside. Faults kept: Figure 2 captioned Salt Lake City over Nashville coordinates, Figures 4 and 6 captioned 'Connections' over zero-edge clouds, Table 6's caption swallowing a body sentence. Citation forecast-first: 11 of 14 named, 6 one page early, **labels glued to numbers** ('figure1', 'Table3', 'Fig- ure 7'), 11 lead sentences, zero trail, no exhibit cited twice; the paper's only two-page lead (Tables 3, 4) belongs to rows that own no region. Red Taobao banner on ALL 29 pages |
| 162 | P-D-2018-82504-6cc63169 | 43 | 20 | 8 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 20 measured regions on 12 of 43 pages = 8 figure rows + 5 table rows + 7 exclusions, for 16 printed captions, so **three captions print alone on pages with no artwork** and their exhibits sit on the previous page (p10, p25, p29). The exclusions are **five rasters of mathematics** (pp7, 9, 11 twice - one p9 box bakes two whole paragraphs of prose into the image, so the text layer skips them) plus a boxed Algorithm 1 block and appendix furniture. **New apparatus class: p19 is a 425x487 pt screenshot of an entire TYPESET PAGE** - body prose, displays (8)-(10), the Markov transition matrix - so that page's text layer is EMPTY while the region pass sees a quarter-page box. **Caption side is perfectly kind-driven**: all 8 figures below, all 5 tables above, 12-16 pt gaps. Two rows carry **two welded captions AND one pasted image holding both numbers' artwork** (Figures 5/6 = two Seoul basemaps split by a white gutter; Figures 7/8 = two in-plot-titled line panels). Families: line 4, map-or-plan-view 2, bar 1, scatter 1; **no 3-D, no contour, no colourbar in 43 pages**; legends 4 none / 3 inside / 1 below the axis. Table 3 prints three rules yet owns no region - declared gap. Grids: **booktabs 4 of 5, no verticals**, including a 3x5 transposed period series with periods as the header row, plus ONE boxed 4x4 classification with merged cells on both axes that overruns the margin; two grids overflow the measure. Citation is the opposite extreme from #161: **zero exhibits named by number in 43 pages**, eight unlabelled deictics ('the picture below', 'is as the chart shown'), five never referenced. Captions 3-15 words, voice `none` on all 13 rows. Red Taobao banner on ALL 43 pages |
| 163 | P-D-2018-82794-47f05792 | 27 | 23 | 16 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 23 measured regions = the 21 printed exhibits (Figures 1-16, Tables 1-5) plus two exclusions (p9's pasted equation (6), p26's appendix opener) - the first exact 1:1 census in this lane, because the equations are typeset text and never measure. **Caption side perfect**: 16 figures below, 5 tables above, and Table 1 prints its caption BETWEEN the doubled top rule and the header row. **Two welded caption pairs**: Figures 11/12 on one line, Figures 13/14 on one line. Families: node-link-network 4, line 4, map-or-plan-view 3, bar 2, other 2 (a nested doughnut and a Venn diagram - outside the vocabulary), schematic 1; **no 3-D, no contour, ONE colourbar in the whole document**; legends none 5 / inside 4 / outside-right 3 / below 2 / outside-left 1 / above 1; every row single-panel and none shares axes. Grids: **booktabs 3, boxed 2**, and the boxed pair is exactly the pair with two-axis merges, header units and decimal alignment; nothing overflows the 425 pt measure (353-388 pt). **Tables 2 and 5 print the identical caption.** Citation: 18 of 21 pointed at, only 11 by number, **three one page early**, three never, and one mis-pointer naming Table 3 over the wrong quantity. Placement: Figure 3 intrudes between the bullets that introduce Figure 4 and is never referenced. Red Taobao banner on ALL 27 pages; printed page numbers offset by two |
| 164 | P-E-2018-72968-5f2ee223 | 37 | 29 | 8 | 2 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 29 measured regions on 19 of 37 pages = 8 figure rows + 2 table rows + 19 exclusions, for TWELVE printed exhibits - **the worst region-to-exhibit ratio in the lane**, and the two missing exhibits are missing for a new reason: **Table 3 (p17) and Table 4 (p22) print as three horizontal rules with no closed frame**, so the clustering pass never sees them, while thirteen pasted display equations - which the census does not want - are kept because a raster always has a tall bbox. The nineteen exclusions: 13 pasted equations whose numbers are printed INSIDE the image (p15's text layer holds no equation body at all), **p26's whole prose paragraph pasted as one raster** (section 6.1.2 has a heading, an image of a paragraph, and the next heading), three overlapping crops of ONE landscape screenshot of Appendix A's 178-country table, and two appendix code-and-heading runs. **Caption side perfect**: 8 figures below, 2 tables above, Table 1's caption inside the top rule. **The pointer layer uses a different format from the caption layer**: every citation is parenthetical - 'Table (1)', 'Table (2)', 'Figure (2)', 'Figure (7)' twice, 'Figure (8)' - six pointers over four numbers and zero occurrences of 'Figure N:', and **both 'Figure (7)' pointers name the wrong exhibit**, so Figure 7 is never correctly cited. Families: other 3 (a pie disc and TWO TREEMAPS whose hue-to-category mapping changes between them), map 1, node-link 1, surface-or-3D 1, bar 1, line 1; **the lane's first genuine 3-D chart** (Figure 5, perspective scatter, colourbar labelled 10-60 over an axis running 0-80); legends none 3 / above 3 / inside 2. Grids booktabs 2 of 2, Table 1 the tallest yet at 26 rows, Table 2 the only numeric grid with a header unit and decimal alignment. Citation: 4 exhibits never referenced, **lead_pages +1 once and -1 once**. Red Taobao banner on 5 pages; folio 6 behind |
| 165 | P-E-2018-73119-79c4dde3 | 27 | 23 | 9 | 9 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 23 measured regions on 16 of 27 pages = 9 figure rows + 9 table rows + 5 exclusions, for NINETEEN printed exhibits - nine charts and ten grids - so the deficit is one and again it is a rule-only grid: **Table 1 (p7), the symbol table, prints as three horizontal rules with its caption between the top rule and the header row**, the same blind spot that cost #164 its Tables 3 and 4. **The paper runs two caption systems and they disagree about what the object is**: the body numbers Figures 1-9 and Tables 1-4, while the two p27 grids are captioned 'Figure 10'/'Figure 11' in the text layer OVER their own titles pasted in the image, 'Table 2.6' and 'Table 2' (the second colliding with the main body's Table 2). Ten grids print and only four are numbered; four have no caption at all. **Figure 2 is a table wearing a figure caption** - 17x5 indicator hierarchy, pastel bands, dashed separators, an unlabelled column of +/- marks - and the prose then lists the same sixteen indicators again. Nothing is 3-D and nothing carries a colourbar, but the same index is drawn on **four different y windows** (0.30-0.36, 0.28-0.44, 0.32-0.42, 0.35-0.65). Figure 4 has no axis titles and no legend - its caption is the key, 19 words, no space after the colon, 'rep-resent' left hyphenated - and Figure 9's caption AND legend both lost the Greek symbol ('Analysis of 1', '01 = 0.8'). Grids boxed 5 / booktabs 3 / no-rules 1, zero zebra, no decimal alignment anywhere, decimals printed as colons in Table 2, the unruled matrix overflowing the measure at 482 pt of 451. Citation: **7 pointed at by number, 11 of 18 with no number in any pointer**, four positional only, lead_pages 0 six times and -1 once |
| 166 | P-E-2018-74971-2b1f503a | 23 | 46 | 13 | 3 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 46 measured regions on 12 of 23 pages = 13 figure rows + 3 table rows + 30 exclusions, for SEVENTEEN printed exhibits - thirteen charts and four grids - so the deficit is one and it is again a rule-only grid: **Table 3 (p15), six horizontal rules and no verticals, owns no region**. **The region list is the finding: twenty of the 46 regions are ONE infographic** (the p8 mind map arrives as twelve label rasters, five vector ellipses and three blank rasters) and five more are one two-panel schematic on p7, so 25 of the 30 exclusions are fragments and the recorded area for a split figure is the **union** of its fragments - Fig.4 is 0.271 of the page, not the 0.072 its largest fragment reports. **Numbering runs backwards**: Fig.11 prints on p16 and Fig.10 on p18, and the sentence reading Fig.11 on p17 calls the country **Kenya** in a section titled 'Climate characteristics of Mexico'. Four charts are never named by number, and the pointer to the piecewise curve says 'As the Fig.3 shows'. **Two families have no vocabulary word**: Fig.5 is four dendrograms, Fig.4 a radial mind map, both filed node-link. Nothing is 3-D and nothing carries a colourbar, but colour gradient is both decoration and value channel; only Fig.6 keys it, with a legend below the frame whose first word prints 'impregnabl'. Fig.6's four band thresholds are exactly Table 4's values, so the tipping point exists twice in two formats. Fig.9's caption keys its panels '(a), (b), (c), (b)' for a grid lettered (a)-(d); Fig.7 double-prints every glyph and clips its four rank names at the margin. Grids booktabs 2 / boxed 1, zero zebra, categorical shading instead, Table 2 the only merged and only decimal-aligned grid and the only one the text layer scrambles; no unit in any header; Table 1 splits over the p4/p5 fold. Caption side is the cleanest in the lane (13 figures below, 3 tables above) in the form 'Fig.1' with no space and no colon. Citation: **12 pointed at by number, 4 never named**, two backward pointers, and the two captions that stand in for a missing legend (Fig.10, Fig.13). Two phantom headings are chart furniture ('28 Annual mean temperature', '52.0 FCI 30') |
| 167 | P-E-2018-78511-395a90c3 | 28 | 33 | 11 | 3 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 33 measured regions on 18 of 28 pages = 11 figure rows + 3 table rows + 19 exclusions, for FOURTEEN printed exhibits and therefore **a deficit of zero - the lane's second exact census**. The mechanism inverts every booktabs paper before it: **Table 1 and Table 3 are drawings of tables, not ruled grids** - three stacked vector blocks each, heavy full-width separators, short column stubs, no closed box - so the ink-following clustering pass sees a picture of a table while it misses a table made of three rules. Six exclusions are their four fragments and the recorded area is the **union**, so Table 1 is 0.245 of the page and Table 3 is the largest exhibit in the document at 0.247. **The caption layer is the finding**: fourteen captions, none naming a variable, unit, condition or conclusion, all six to seventeen words, one sentence, colon form, figures below and tables above, panel key on a wrapped second line. **Every two-panel figure is one raster and no two panels share a window** (y 0.25-0.31 beside 0.36-0.43, x 0-4 beside 0-0.2, y 0-25 beside 0-1.2), so 'similar' claims describe drawn shape. Two radar pairs (Fig.4, Fig.9) have no vocabulary word and print every value and no ring. The only 3-D is Fig.2's isometric pyramid, asserting an order no weight supports. Zero colourbars; near-white 'before' polygons vanish at print. Grids booktabs 3, zero zebra: **Table 1 and Table 3 share one caption with different numbers** while the prose calls them similar, and only Table 1's columns sum to 100 (Table 3: 101/99/111). Table 2 is the one true grid - merged country cells, double vertical rule, decimal-aligned, summary row ruled off. No unit in any header; the only unit in the paper is Fig.8's 'billion dollars'. Citation is the densest in the lane: all fourteen exhibits named, no positional-only pointer, two backward placements (Fig.7 p19 to p21, Fig.10 p22 to p23) |
| 168 | P-E-2018-88902-cefa4db9 | 28 | 39 | 13 | 5 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 39 measured regions on 17 of 28 pages = 13 figure rows + 5 table rows + 21 exclusions, for EIGHTEEN printed exhibits and therefore **a deficit of zero - the lane's third exact census**. **Two new region-pass mechanisms**: the pass boxes **one drawing twice** (Fig.4 vector plus raster over the same coordinates; all four Fig.8 panels captured twice, so eight regions hold four drawings - anchor 0.118 against a 0.225 union) and **one region can hold two side-by-side drawings** (both p19 pairs). **Caption side is a paper-level habit, not a law**: 18 of 18 captions print below, figures under art AND tables under grid - the inverse of #167's tables-above - and the text layer still lists the caption before the grid, which is how a caption-side record goes wrong. Captions are the richest in the lane: colon form, 4-11 words, one sentence, and **8 of 18 name the quantity plotted** against zero in the previous three. **No multipanel figure shares axes**: Fig.8 has four y windows, two tick steps and a legend order that rotates panel by panel (red is Social in one box, Economic in the next); Fig.10 runs 0-35% beside 0-45%. **Colourbar exactly once** (Fig.13); Fig.2's ring and Fig.3's quadrant gradients shade a value nothing decodes. Only 3-D is Fig.9's four perspective boxes with three named axes and no tick numbers. Grids boxed 2 / booktabs 2 / open-sided zebra 1, zero merged, zero diagonal, zero units-in-header, zero decimal-aligned; **Table 4's caption says 'WFSI C' and drops the CCIC column Table 3 carries**, and **Table 5 welds every cost to its unit** so the column cannot be summed. Table 5 is misplaced under 11 Task 5 although its argument is 10 Task 4, and **Fig.13(b) is a 'continent' index shaded by country** with the prose admitting the reading fails. All eighteen named; 16 pointed at on their own page or one earlier; Fig.7 is a negative lead (art p16, pointer p17). Folio breaks at the end ('Page 25 of 24' on p28); resale banner on every page, invisible to the text layer |
| 169 | P-E-2018-89499-90bc677f | 22 | 22 | 11 | 6 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 22 measured regions on 14 of 22 pages = 11 figure rows + 6 table rows + 5 equation exclusions, against EIGHTEEN printed exhibits (12 figures, 6 tables), so **the deficit is ONE - Figure 8 is drawn, captioned and pointed at but has no measured region**, the pass returned one box on p11 and it belongs to Figure 7. **Caption side splits inside one paper**: all six table captions ABOVE the grid, all twelve figure captions BELOW the art. **Table 1's caption is ink only** - 'Table 1 Notations of the model' prints over a two-column symbol grid and the text layer skips from '2.2 Notations' to '3 The Model of Fragility', so the row is `typed-from-crop` and the exhibit is never announced. **Region area is a floor** on three charts (Figs 7, 10, 12 record 0.0261, 0.0227, 0.0118 of the page: plotting band only, title and legend outside). Twelve figures, **two designs**: five flowcharts (Figs 1-5) and seven computed charts that are either stacked bars with a fragility line overlaid (7, 9, 11 - one design reissued three times, y windows 0-0.8 / 0-0.6 / 0-0.6) or multi-series lines (6, 8, 10, 12). **No multipanel figure, no shared axis, no colourbar, no 3-D**; the only dimensional trick is Fig 6's **second y axis** (rank 20-140 left, fragility 0-0.7 right). Legends below 5 / outside-right 1 / inside 0. Grids booktabs 2 / boxed 4, zero zebra, zero diagonal, zero units-in-header, **one merged cell** (Table 6's Total Cost); **decimal alignment tracks the data, not the paper** - Table 3 aligns, Table 5 with the identical measures does not; **every cost welds its currency** so the column cannot be summed. 12/17 pointers 'as shown in', 3 direct, 2 none; Fig 1 is a **negative lead** (art p5, pointer p6). **Copy-paste is the signature fault**: 5.1.2 is still titled '...fragile Sudan' in the Egypt section, Fig 9's lead says 'the fragility of Sudan', Table 5's caption is Table 3's. The p9 variation-coefficient equation renders illegibly; two phantom headings ('0.45 Before', '0.4 After') are minted from Fig 12's axis furniture; a red resale banner stamps every page and never reaches the text layer; the folio says 'Page N of 21' across 22 pages; welds land inside exhibit text ('Fragilityin', 'Figure1', 'indicatorsare', 'in2028', 'SouthSudan', 'Table 2Range') |

Two more classes are not caption defects but are recorded the same way, because the text
layer cannot reconstruct the sentence: a caption whose glyphs are mangled math italics
(`μ`/`σ` come out as private-use characters, #132 Figures 15/16), and a caption printed as
part of a pasted raster.

Shape 8 is the only one that cannot be fixed inside the payload: both `resolve_caption` and
the substring test in `build_payload` reject the interleaved text, so the row is typed from
the crop and the payload is patched after `build_payload` returns rather than before.

## An annotation is not a legend

Figures 1, 3, 4 and 5 of #137 P-E-2017-68242-753e0037 are one three-circle Venn template
reused once per section that introduces a component set. All four print the same device in
the upper right: the phrase "Smart Growth", "Smart Growth Economically Prosperous", "Smart
Growth Socially Equitable" and so on, set inside the artwork with a single straight leader
line ending in a filled dot at the triple overlap.

That reads as a legend at a glance and two independent crop passes called it one. It is not.
A legend keys series or colours and repeats the entries it explains; this is a label for the
whole drawing, drawn once, keying nothing. All four rows therefore record `legend: none`, and
the device is described in the row note instead. The consequence is an aggregate one: any
count of "figures that draw a legend" must exclude leader-line callouts, or a paper whose only
figure furniture is a pointer will look like the most heavily keyed paper in the census.

The same distinction settles the bar pair of Figure 8, which does print a real key - three
sample swatches for "after adjustment", "before adjustment" and "current plan" - and is
recorded `legend: below`.

## One printed table, two city blocks, one measured region

Table 8 of #137 prints two stacked blocks in one grid: a Wellington header with three stage
rows carrying W1-W7, then an Anchorage header with three stage rows carrying A1-A7, sharing one
caption above and one note below. The measurement returned the lower block only (y=562.3 to
602.2 pt); the Wellington block, which sets between the caption and that box, returns no region
at all.

Three ways out exist and two are wrong. Recording the whole table on the measured box would
claim 4 rows and 10 columns for a grid that carries 8 rows in two header bands. Inventing a
second table row for the unmeasured block would double-count one printed table. What the record
does instead: the measured block is the row, `rows` counts that block, and the missing block is
stated in the row note as a declared gap with its printed extent - the same treatment the
earlier half-measured exhibits get, except that here the gap is a whole block of a table whose
other block measured cleanly.

The generalisation: a table whose repetition repeats its *header*, not only its body, has two
possible region shapes, and only the measured one may be described.

## Three things the detector calls a table and none of them is

The `not-an-exhibit` exclusion exists because a region with cell-like structure does not
have to be an exhibit. Three faces of the same case are now on record, and the test that
separates them from a real grid is the same in all three: no column header, no caption, and
no sentence in the running text that cites it.

- A **wordmark** in the margin - the COMAP logo box of #290 (mcm-65) returns as a small
  multi-cell region and is furniture, not a table.
- A **code listing** - the Appendix 1 slab of #291 (mcm-65) draws a monospaced block that
  measures like a grid with one wide column; it is an algorithm, so it is excluded, and when
  such a listing carries a real caption the row instead becomes family `other` (the
  Algorithm 1 case of #290).
- A **letter header** - p22 of #291 (mcm-65) returns a region carrying only `To:`, `From:`,
  `Date:` and `Subject:` with their values. A two-column label/value block by shape, a
  memorandum masthead by function: nothing cites it, it captions nothing, and it prints on
  no page that carries an exhibit.

Because all three are excluded rather than recorded, none of them reaches `family` counts,
and the paper's own table count stays what the prose cites. That is the point: an exclusion
is a claim that a printed thing exists and is not an exhibit, so it needs a `reason`, a
bbox and a note, and the note has to name which of these faces it is.

## A value one position off is an extraction artefact until a crop says otherwise

Four independent papers now print a table whose extracted text puts a value on the wrong row while
the raster is clean. The shapes differ, so this is a class, not a one-off:

- one cell goes missing and every value below it shifts up a row - #138 P-E-2017-71672-f2a1a712,
  where Table 3 loses the P7 value on p14 and Table 4 loses the P5 value on p17;
- a symbol stub and its description column come back as two separate blocks, so every symbol is
  paired with the description of the row above - #292 (mcm-65), Table 4;
- three columns each lose one value at the same row and shift down together - #292, Table 5;
- a row label comes back alone with its two cells dropped to the next line - #292, Table 3.

The rule these four give: a numeric or paired column in which exactly one row disagrees with its
neighbours is an extraction artefact until a crop contradicts it, and the crop decides. Writing a
misalignment into a record from the text layer alone is the failure mode, because a one-row shift
is always plausible - it looks like a printing error, not like a parser error.

## The caption printed inside the header line

#292 (mcm-65) prints `Symbols` and `Table N: Notations / Variable parameters` on one baseline with
`Descripition` pushed to the next line, so the caption and the first header cell share a line and
the second header cell lands below both. `caption.position` stays `above` - the caption is above the
grid - but the header is split by it, so a header-row read keeps one column name and silently loses
the other, and a `header_rows: 1` record made from that read describes a table that does not exist.
The check that catches it: the caption line must contain no cell text, and the header block must
account for every printed column before the first body row.

#139 P-F-2017-64486-62f12f04 has the mirror shape - its Table 6 prints the stub header cell `Class`
before the caption line in the text layer - and is recorded the same way: caption verbatim without
the stray token, the stray token described in the row note.

## Caption side: per paper, with one licensed exception

The rule holds - the side is decided per paper and never inferred from exhibit type - but it needs
its sub-case. #292 (mcm-65) prints 18 figure captions below and 8 table captions above without a
single exception, then breaks once: Figure 16's caption is the first line of a back-matter memo page
and genuinely sits above its artwork. So the statement to record is "one side per paper by default,
and a figure that opens a fresh back-matter page takes the side the page forces". A record that says
"figures below" flatly is falsified by that one row; a record that says "this paper puts its figures
below except where a figure opens a page" survives the aggregate.

#139 is the control case: 25 figures all below and 5 recorded tables all above, no exception, so its
per-paper rule is uniform and needs no licence.

## Checkpoint 144-146: page order, uncaptioned caption side, repeated exhibits

Three papers closed back to back (#144 P-A-2018-76271-27d535ab, #145 P-A-2018-77845-746864a6,
#146 P-A-2018-86103-6d21eb9d) were re-read against their records, and the cross-paper pass found
two field-level defects that no single-paper check could have caught.

**Page order against a side-by-side pair.** #144 p17 prints Figure 3 and Figure 4 in the two
columns of one band, and the record had assigned `place.page_order` by bbox top, which put the
right-hand exhibit first (Figure 4 = 1, Figure 3 = 2) while `place.doc_order` kept the reading
order (Figure 3 = 7, Figure 4 = 8). Two orderings of the same page contradicting each other is
never a reading of the page, it is a tie-break bug: within one band the left column is read
first, so both fields must agree. Both exhibits now read 1 and 2 on the page and 7 and 8 in the
document. The lesson generalises - `doc_order` and `page_order` are computed by different passes
and will silently disagree wherever two regions share a band, so the audit must compare them
rather than trust either.

**Caption side for a grid with no caption.** #146's p7 notation glossary is the one grid in that
paper that prints no caption at all, and the payload's `cap()` default had recorded
`caption.position = below` for it. That is a value about nothing: the glossary's title is its
section heading, printed above the grid, and a `below` there made the record's table side read
"one below, five above" while the paper's rule is uniformly tables-above. The rule text was not
wrong and the aggregate would have been. Recorded as `above`, matching the side the paper uses
for every grid it does caption, so a null caption no longer smuggles a counter-example into the
side counts. #144 and #145 had already set their uncaptioned grids to their paper's side by
hand, which is why the defect appeared exactly once.

**What the three papers say together.** Their caption-side rules are all different and all
correct: #144 figures below and tables above, #145 figures below and tables BELOW (the only
paper so far whose grid captions sit under the grid), #146 figures below and tables above again.
So the field is a per-paper rule, not a house rule, and the corrected #146 aggregate (18 below,
5 above, one uncaptioned recorded on the paper's side) is the value to compare future papers
against. Two more cross-paper facts worth keeping: #146 prints the same Excel chart three times
(abstract Figure 2, Figure 10, Figure 12) and each printed instance keeps its own row - the
census records exhibits as printed, and a duplicate is a fact about the paper, not a reason to
merge rows; and all three papers paste their display mathematics as images, which is now five
papers running, so "equation rendered as a picture" is a stable property of this batch rather
than an accident of any one detector run.

## Checkpoint 145-147: caption side per kind, one colon nobody covers, templates reprinted

Three papers, three different answers to the same question about caption side, and the rule that
survives is narrower than any of them.

#145 put every exhibit below its artwork - eighteen figures and seven tables - the first paper in
the batch where side did not track kind. #146 put all eighteen figures below and all five numbered
tables above, 23 of 23, and the one page carrying both kinds showed the rule twice in one column.
#147 repeats #146's split exactly - nineteen figure rows below, one grid above - so the pattern is
now: where a paper carries both kinds, side follows kind; where it carries only one, the paper
chooses and #145 chose below for both. What the census may not do is carry a batch-level default,
because the paper that disagrees is always one row away. Recorded as `caption.position`, counted
per paper, and never inferred from the neighbouring exhibit.

The numbering vocabulary has a hole. #147 prints "Figure 6：The relationship between Lcal or Ltur
and f" - a full-width colon, the first in the batch. `NUMBERINGS` has no such member and inventing
one for a single caption would be a vocabulary of one, so the field takes the bare "Figure N" form
and the note carries the punctuation. If a second paper turns up with the same habit the set should
grow; one caption is not evidence.

Two findings on the drawing side that belong together. First, this paper reprints one plot
template four times - the hop-budget frame with a dashed 150 dB threshold - and a second one twice,
and only the caption and the key change between printings. #146 gave the same phenomenon in a
different tool: one Excel clustered-column chart printed three times as abstract Figure 2, Figure
10 and Figure 12. A "family" count therefore counts printings, not designs, and the note has to
say so or the aggregate will read as eleven different plot ideas where the paper had two.

Second, #147 is the batch's cleanest case of the detector measuring the same image twice: three
figures on pp18-19 are each a vector frame with a raster interior, so `fig_extract.py` reports two
boxes and the census must exclude one. The same page pair also shows the gap on the other side -
the fifteen-row abbreviation glossary at the top of p5 is a real table with printed rules, and the
layout has no box for it anywhere; the detector boxed the rule band above it and nothing else. The
region pass follows images, not tables, and a paper can therefore carry a table the census cannot
see. That is worth stating once here, because the alternative - inventing a bbox - is worse.

Queue position: #169 closed, next #170. The 166-168 checkpoint is written directly
below; the 163-165 checkpoint sits under it, the 160-162 checkpoint under that, and
the 153-155, 150-152, 146-148 and 145-147 checkpoints further down.

## Checkpoint 166-168: the region list both over-counts and under-counts, and caption side is a habit
Three papers, 118 measured regions on 79 pages for 48 rows against 49 printed exhibits - one
deficit in 49, and it is #166's rule-only Table 3. Two exact censuses in a row after it (#167 and
#168, fourteen and eighteen exhibits), and the reason is not that the detector got better: it is
that these papers give their tables ink. Every grid in the three papers that carries a frame or a
shading is measured; what still escapes is the one grid made of three thin rules.

**The region list over-counts as well as under-counts, and both faults come from the same
rule.** The pass follows ink, so a drawing made of two overlapping image layers is two regions.
#168 is the clean demonstration: Figure 4 is one drawing captured once as vector and once as raster
over nearly the same coordinates, and all four panels of Figure 8 are captured twice each - eight
regions, four drawings. The recorded area is therefore always the UNION of the exhibit's regions and
the anchor is always the largest measured region, never the first one: Figure 8's anchor reports
0.118 of the page and the grid is 0.225, Figure 13's anchor reports 0.052 against 0.107. This is
the same convention the fragment papers already forced, now applied in the other direction. The
mirror fault sits in the same paper: one region can hold TWO side-by-side drawings - both pairs on
p19 are two panels in one box - so region count can also be lower than drawing count. State both
halves once: a region is not a drawing, in either direction, and a census that equates them is wrong
by however much the authoring pipeline duplicated or merged its images.

**Caption side is a paper-level habit, and it flips.** #167 prints its eleven figures below and its
three tables ABOVE. #168 prints thirteen figures AND five tables below, 18 of 18. #166 splits the
same way its two neighbours do - figures below, tables above. Three papers, two opposite table
conventions, all internally consistent, none of them stated anywhere in the document. The
consequence for this lane is procedural: caption side must be read off the crop every time, and the
text layer cannot be used as an inference route, because the text layer lists a caption in reading
order wherever the extractor found it. #168's Figure 12 is the proof case - the caption is
geometrically UNDER the plot and the text layer emits it before the axes - and Table 1 of #168 is
the same trap on a grid.

**Numbering errors and section errors are different faults, and only one of them is cheap.**
#166 runs its figure numbers backwards (Fig.11 on p16, Fig.10 on p18) and never names four of its
thirteen charts. #168 has the opposite profile - all eighteen named, sixteen on their own page or
one page before - and still misplaces one exhibit, because Table 5's argument is in 10 Task 4 on
p21 and the table prints on p22 under 11 Task 5. A backward pointer costs the reader a page flip; a
table under the wrong heading costs the section its evidence, and no caption check will find it.
Check `place.section_path` against the pointer sentence, not against what the table is about.

**The caption layer is where a paper's honesty shows up first.** #167's fourteen captions name no
variable at all. #168's eight of eighteen name the quantity, and the same paper is the first in
this lane whose exhibits argue against each other: Figure 13 panel (b) is labelled a continent
index and shaded country by country, Table 4's caption says 'WFSI C' and drops the column its
predecessor carried, and Table 5 welds every cost to its unit so the column cannot be summed. None
of those is a layout fault and all of them are exactly what the six field groups are for. A census
that only counts regions would score this paper perfect, and it is the most self-contradictory
paper the lane has taken.

**Apparatus faults are the last thing the text layer can be trusted about.** #166 invents two
phantom section headings out of chart furniture ('28 Annual mean temperature', '52.0 FCI 30').
#168 stamps one identical red Chinese resale banner on every one of its 28 pages and the text
layer contains no trace of it, while its folio breaks at the end ('Page 24 of 24' on p27, 'Page 25
of 24' on p28) - a defect only a page-by-page read finds. Read the folio on the first and last page
of every paper; read the banner layer only from the crop.

## Checkpoint 163-165: what decides whether an exhibit is measured, and who owns the number

Three papers, 75 measured regions on 91 pages for 49 rows against 52 printed exhibits. Five
findings, all of them about the three layers a census has to reconcile - the region list, the
caption layer and the pointer layer - and none of them about artwork size, which the last three
checkpoints kept blaming.

**A table's rule style, not its size, decides whether the detector sees it.** #163 lost nothing
(23 regions, 21 exhibits, 1:1) because every one of its grids is boxed or booktabs-with-a-frame
and its maths is typeset. #164 lost two of twelve to three-rule grids and #165 lost one of
nineteen to the same fault - and in all three cases the table the census cannot see is the
best-built table in the paper. #165 supplies the inverse proof: it measures nine of its ten
grids, and the eight that measure are the eight that have a closed outer frame, while the
ninth is an unruled whitespace matrix that the detector DID catch because its text block is
dense enough to cluster. So the region pass follows ink, and three thin rules are less ink than
one word: state this once and stop checking for size first.

**Caption layers are plural.** #163 printed two captions on one line ('Figure 11: mix map
Figure 12: distribution of supercharging sta-') and printed one caption twice for two different
grids. #164 captioned in 'Figure N:' and cited in 'Figure (N)' with two of six pointers naming
the wrong object. #165 runs two numbering SYSTEMS on one page and one number twice across the
document. Reconciling captions against regions is therefore only the first pass; the second
pass is caption against pointer, and the third is caption against the object it sits on - #165's
'Figure 10' sits on a table whose own pasted title says 'Table 2.6', which no caption-vs-region
count can detect.

**Being pointed at is not the same as being findable.** #163 pointed at 18 of 21 rows but only
11 by number; #164 managed six pointer lines over four numbers; #165 numbers seven of eighteen
and introduces four more only positionally ('shown in the figure below'). The metric worth keeping
is binary and blunt: can a reader who reads the prose reach the exhibit. By that measure #165 is
the weakest paper of the three despite having the neatest one-exhibit-per-step structure.

**The figure/table distinction is paper-local.** #164 grew two treemaps and a pie disc out of a
fourteen-family vocabulary that has no word for them. #165 puts a 17x5 ruled grid under a figure
caption and a pair of 13-column grids under figure numbers too, then leaves four ordinary grids
with no caption, number or title. The family count therefore describes the graphic, and the
figure/table split describes the label - a census that aggregates 'figure_items' against
'table_items' is aggregating the paper's own filing, not the artwork's nature, and the note has
to say so.

**Scale discipline is absent in every paper and only visible when a chart plots a bounded
index.** #163's one scale-consistent pair got that way by hand; #164 mislabelled the colourbar of
its only 3-D chart; #165 plots one fragility index on four disjoint y windows across four charts
so that no two can be compared, and annotates two thresholds with no label at all. None of the
five geometry fields can hold this. Until one can, the note on any chart of a 0-1 index should
print the plotted window, because that number alone decides whether the reader sees a trend or a
wiggle.

## Checkpoint 160-162: three deficits in a row, and a paper that screenshots whole pages

Three papers, 97 measured regions on 76 pages for 42 rows against 55 printed exhibits. The
row count is below the exhibit count for the third paper running, and #162 shows why the
deficit is not going away: its exhibits are the only objects on the page that were
*typeset*, and everything the paper could not typeset it pasted instead. Five findings.

**The deficit is now the diagnostic, and its size tracks how much maths the paper pasted.**
#160 had 20 exhibits for 15 rows and pasted fourteen derivations. #161 had 19 for 14 and
pasted its model half. #162 has 16 for 13 and pasted five equation strips plus a whole page.
The three papers bracket the whole census: #159's surplus came from one figure split into
six panels, this stretch's deficits come from derivations rendered as pixels. So the rule
holds in a sharper form than at 159-161 - reconcile captions against regions, and read the
SIGN of the gap as a statement about the paper's production process, not about the detector.

**A new apparatus fault class: the pasted page.** Previous papers pasted equations; #162
pastes a page. p19 carries a 425x487 pt image of dense body prose, displays (8), (9), (10),
the spectral-decomposition radical, a four-node Markov transition matrix and the ergodic
vector - all typeset, all illegible to extraction, so the page's text layer is EMPTY and
anything downstream of the text layer (mentions, caption quotes, section paths) silently
loses that page. Two lesser members of the same family: p9's box bakes two whole paragraphs
of prose into the raster so the text layer jumps from "after some original improvements" to
"By the above improvements", and p7's box ends mid-sentence at its top edge. Consequence
worth stating once: on these papers the text layer is not a subset of the content, it is a
lossy sample of it, and a quote-not-found error may mean the content was never typed.

**The orphan caption is a distinct failure from the missing-artwork caption, and #162 has
three of them.** #160's Figures 3 and 4 printed a merged caption line with no artwork on the
page at all. #162's Figures 2, 9 and 10 print their captions ALONE on p10, p25 and p29 while
their artwork sits on the previous page - same page, no ink, one turn away. The detector sees
two correct objects and a reader sees a broken promise, which is why ownership there had to
be argued from caption text and doc order rather than from proximity. mcm-d0's #268 adds a
third variant with the same shape: a page-foot stamp that FUSES with a caption on pp8-9, so
the caption's own line carries furniture.

**Caption side has settled into a kind-driven majority, but the kind is what the NUMBER
says, not what the drawing is.** #162 is the cleanest instance yet: eight figure captions
below, five table captions above, no exception in 43 pages. #161 was uniform-below (both
kinds below), #160 kind-split, #159 inverted by part of the paper. mcm-d0's #268 supplies the
counter-case that makes the axis non-trivial: in that paper two bars charts are numbered and
captioned as Tables, so the caption side follows the printed label rather than the artwork -
**read the number, then place the caption; do not classify the drawing first.** The
consequence for a census is that family and caption side can disagree on the same row, and
both are then correct: the drawing is a bar chart, the exhibit is a table.

**Citation style has now been seen to degenerate to zero, and the pointers that remain carry
the claim.** #160 printed one numbered reference in its whole body. #162 prints NONE in 43
pages: eight exhibits are introduced by unlabelled deictics ("The picture below is the
distribution of destination charging stations...", "As in the pictures shown below, the
distribution is similar to each other, verifying our model's reliability") and five are
never referenced at all. Against #161's 11-of-14 named with labels glued to numbers, this
settles the axis: reference density ranges from 0 to nearly 1 inside one paper block, so a
detector keyed on "Figure N" will find between none and all of a paper's exhibits. Worth
copying from #162 is the deictic's payload - the sentence states the reading ("similar to
each other") before the reader reaches the picture; worth avoiding is that nothing in the
sentence or the artwork says which of two side-by-side plans is Markov and which is SFCLM.

**Apparatus, once, for all three.** The Chinese resale banner is a constant of this block and
now of the whole block: above ALL 43 pages of #162, text pages and image pages alike, as it
was for all 29 of #161, so on any paper in this lane a page that opens with a box reads as
caption_above until proven otherwise. Merged caption lines remain the standard symptom of a
two-in-one paste: #162's Figures 5/6 and 7/8 each weld two captions into one line AND ship
one image holding both numbers' artwork, which is the same custody problem #159 had at six
panels, arriving through the caption instead of the box. And #162 contributes a grid boundary
worth naming: booktabs 4 of 5 with no verticals at all, and the single boxed grid is the only
one that needed merged cells on two axes - a correspondence, not a coincidence, that the
next few papers should test.

## Checkpoint 159-161: the surplus flips to a deficit, and the detector follows rules rather than tables

Three papers, 88 measured regions on 77 pages for 62 rows against 63 printed exhibits - and
for the first time in this lane the row count is BELOW the exhibit count, twice over. Five
findings, plus the axes these three papers settle against the rest of the block.

**The row-to-exhibit gap runs both ways, and the sign says what the paper did.** #159 had
39 regions for 24 exhibits and 33 rows: nine of its rows were pure custody, because it
pasted one figure as six panels. #160 had 29 regions for 20 exhibits and 15 rows, #161 20
regions for 19 captions and 14 rows - because both papers rasterise what they could not
typeset. #160 pasted fourteen derivations and called two numbered exhibits with no artwork
at all; #161 pasted its model half and printed five of its seven tables as ordinary text.
So a census that reads regions as exhibits over-counts #159 and under-counts #160 and #161
by a third. The rule to carry: count captions AND regions, then reconcile; neither number
is the exhibit count on its own.

**Tables are a detector problem before they are a design problem.** Across the three
papers the grids split perfectly on one property - whether the paper drew a border. #161's
Tables 5 and 6 are closed boxes (frame plus every internal rule) and both measured; its
five unruled tables printed as text blocks welded to their own captions and NONE measured,
including one where the caption and six body rows form a single text block with a 1.5 pt
overlap. #159 measured six of seven boxed grids and missed the one horizontal-only bitmap;
#160 measured its one captured bitmap grid and missed four unruled-or-lightly-ruled bands.
mcm-d0's #267, running the other way, measured all three of its grids because all three
are closed vertical-rule boxes. Five papers, one conclusion: the region pass follows
RULES, not tables, and an unruled table is invisible to it at any column count.

**Caption side has now been seen in four arrangements, and only one of them is
kind-driven by accident.** #161 is the clean case: all twelve figure captions and both
table captions below, identical rule for both kinds. #160 was kind-split (thirteen figures
below, two tables above), #159 inverted by PART of the paper (body below, all three
appendix boxes and every table above), and mcm-d0's #267 is kind-split with a third
caption population - twenty-seven bare two-word "Figure N" labels with no title at all,
which is a caption set the title-oriented template cannot describe. Caption gap is not a
constant either: 1.2 pt at its tightest (#160's Figure 15, welded onto a heading) and 58.3
pt at its widest (#161's Figure 7), and in #161 the wide gaps are simply the column's
white space, not sloppiness - which is why ownership there had to be argued from
alignment rather than distance.

**Citation styles are diverging, and one of them breaks regexes.** #159 cited 17 of 33
rows but never twice; #160 cited exactly ONE exhibit by number in its whole body and
leaned on "the figure above"/"the table below"; #161 cites 11 of 14 rows, six of them a
page BEFORE the exhibit prints, with the label glued to the number ("figure1", "Table3",
"Figure10", and one broken across a line as "Fig- ure 7"). mcm-d0's #267 reports the same
glue on seven of twenty-seven labels. A census regex on "Figure \d" therefore finds
most of #161 and mcm-d0's #267, and almost nothing in #160 - the three papers together say
the style axis is not cosmetic, it decides whether the citation trail can be used to find
exhibits at all.

**Two new axes these papers opened.** First, three dimensions finally appear - #161's
Figures 3 and 7 are perspective surface meshes with grid walls on three panes, and they
are the only 3-D rows in 62. Their conditions are narrow and worth recording: geographic
x/y shared with a sibling figure, a real vertical quantity with printed ticks, and a plain
wireframe projection rather than a shaded solid. Second, the colourbar question inverted
from what the earlier checkpoints assumed: #160's choropleth keyed its ramp as eight
discrete legend bands, and #161's two filled contours carry NO colourbar at all - so a
detector that equates "filled chart" with "colourbar" is wrong on both papers, in opposite
directions.

**Apparatus, once, for all three.** The Chinese resale banner is not confined to raster
pages: #159 saw it above nine region-bearing pages, #160 above six, and #161 above ALL
twenty-nine pages including text pages, so every page that opens with a box reads it as
caption_above. Merged caption lines are another repeat offender - #160's p10/p15/p16 and
#161's p16/p19 each pack two captions into one text-layer unit, but only #160's were
genuinely printed on one line; #161's were two separate lines with no terminal full stop.
And #161's appendix contributes a new false positive worth naming: a region that is a
rule-bracketed SECTION HEADING (423x26 pt, two 0.6 pt rules around an 11 pt red title), and
one that is page furniture (header rule + one code line + closing rule).

## Checkpoint 156-158: the surplus moves from the box to the caption, and two ways to get a caption wrong

Three papers, three quarters of the same failure with three different mechanisms: 121 measured
regions on 67 pages for 156-158. Five findings, then the traps that belong to a single paper but
will bite the next one.

**Region surplus now comes from the caption, not from the box.** #156 had four boxes holding two
separately captioned figures; #158 takes the mirror form: Tables 5 and 6 are each ONE caption over
TWO separately boxed grids (a goodness-of-fit block and a maximum-likelihood block, 30 pt apart), so
p24's four boxes hold two printed tables and 16 printed exhibits produce 18 rows. #157 goes the
other way - three printed tables own no row at all, two of them because one appendix box fuses two
complete grids. The reconciliation is no longer "count boxes against printed numbers"; it is "walk
each printed caption to its grid" **grid by grid, never box by box**, and the walk has to run in
both directions.

**Headerless grids are the norm in half the batch, and the contract has no value for them.** #263's
KMO plate prints no header row at all and the KMO value sits in the slot a header would occupy; #158
prints six of eight table rows with no header (the stub column is the header: Degree/Year,
Index/Country, NAV/NCS/AST/NSC). `header_rows >= 1` forces those rows to record one and put the fact
in the note, which is the honest form of a field that cannot express zero. Say so in the
table note every time, or the next reader will believe the header count.

**Caption side is a per-paper property and the per-paper answer is not guessable.** #157: 12 tables
above, 13 of 14 figures below. #158: all 8 table rows above, all 10 figures below, no exception -
including Figure 8 and Figure 10, which open their pages with the box in the margin ABOVE the ink
and still keep their captions underneath, where the text layer's order makes the caption look as
though it precedes the art. #265 is the third arrangement: all 16 captions BELOW, tables included,
the mirror image of #264 where every table caption printed above. Three consecutive papers, three
different answers, one of them not even type-driven. Read every caption's ink position.

**Two ways for a caption detector to lie, and both are cheap to catch.** #157's appendix is not
images at 0.5 pt vector frames round live code; #158 is a watermarked resale scan whose Chinese shop
line prints above nine region-bearing pages and is read as `caption_above` four times over a raster
and five times over a code frame. In the first case the caption pass sees a frame and calls it art;
in the second it sees the same repeated string nine times and calls it a caption nine times. The
tell in both is repetition: a caption that appears verbatim on ten pages is not a caption.

**Citation discipline keeps splitting, and the backward reference is now the minority.** #158 names
two of sixteen exhibits in the prose and both on the page that prints them; the rest arrive by deixis
("as follows", "as below"). #157 named 8 of 26 but placed two of those AFTER the artwork, giving
lead_pages 0 and -1; #158's longest forward lead is 9, where the prose points at the appendix
("the test results are shown in the appendix") fifteen pages before Tables 5 and 6 print. So
`lead_pages` needs its sign checked per paper, not assumed.

Three single-paper traps worth carrying. #264: a spanning table and a page-foot banner fused into one
measured box, an unnumbered notation table whose numbering starts at 2, and a printed order that
disagrees with the order the citing sections would imply - so document order has to be read off the
page, not off the prose. #265: four tables print their rank ordinals in an unruled left gutter
OUTSIDE the first vertical rule, so a crop or bbox tight to that rule silently loses column 1, and
p11's Table 4 box starts at y54.07 and swallows the 2 pt page-header band, showing a spurious double
top rule that is the bbox's fault and not the grid's. #157: two figures whose numbered references
arrive after the art.

**The detector gap that stays open.** #262, paper `P-D-2021-2107091-7ebae97f`, Table 4 on p12: the
table is printed and drawn and owns no measured region, because tol-based stroke clustering fuses
each rule pair with its cell verticals into a 17.2 pt cluster that is too tall to seed on
(`h <= RULE_HEIGHT_PT` = 12.0) and too short for the ordinary region path
(`h < MIN_SIDE_PT` = 25.0), so both paths miss it. The loss happens in the clustering step before
the seed, gap-grouping and alignment filters ever see a rule box. No detector change was made from
this lane; a real fix means seeding on per-drawing strokes instead of clusters, which moves every
paper already closed and is the tool owner's call.

## Checkpoint 153-155: region count runs both ways at once, and the caption side is a habit to verify, not a law to apply

Three consecutive 2018 C papers on the same problem, 128 measured regions, 77 exhibit rows and 25
grid rows. Five findings.

**Region count can overstate and understate in the same paper.** #155 is both cases at once: six of
its 27 rows are panel boxes for two four-panel strips, so eight regions buy two printed figures, and
four more regions are duplicate detections of exhibits already claimed - the raster plot layer inside
a vector axis box (p10), a second box over the same artwork (p15, IoU 0.93), a bitmap nested 96 per
cent inside its frame (p18). #152 had the opposite failure, one region holding two printed figures.
#154 had neither. So the reconciliation has to be run both directions every time: printed caption
numbers against region count, and region count against claimed rows. Claiming panels as items with
`is_panel_of` keeps the coverage honest and makes the family aggregate count panels - state that in
the note, because the number no longer equals printed figures.

**The caption side is kind-driven on two of three papers, and the exception is one row.** #153: 13 of
13 figures below, 8 of 8 tables above. #155: 20 of 20 below, 7 of 7 above. #154: 28 of 29 below,
Table 16 alone above. Three papers, one violation, and the violation is a 13-word appendix caption
that prints above its grid. Read it as a default that gets checked per paper, never as an invariant
that lets you skip the crop.

**The grid recipe is a paper constant only in the strong cases.** #153 is all booktabs, five of five
in #152 too. #154 is the opposite extreme: eight of ten closed boxes with full-height verticals.
#155 is neither - four booktabs against three with a stub divider, and the split follows the kind of
grid rather than the paper (definition and data grids booktabs, coefficient grids with a divider).
Reading one grid gives the recipe for the papers that have a recipe; #155 and #150 are the papers
where you must read every grid.

**Table citation is not decaying, it is bimodal.** #153 cites no table by number, #151 cites no
exhibit at all, #154 cites 7 of 29, and #155 cites all 14 figures and 6 of 9 tables. The same batch
contains "figures referenced, tables ignored" and "everything referenced". Citation discipline is a
property of the team, not of the year.

**The unboxed native table is now a standing gap, and it comes in two shapes.** #153: ten printed
tables, eight boxed. #154: eighteen printed, ten boxed. #155: nine printed, seven boxed, and its two
missing ones print side by side above every detected box on the page - so the gap is not only
"native text the detector cannot see" but also "grid above the first artwork of the page, where the
region pass has nothing to anchor to". Declare both, patch neither.

Two smaller things worth carrying forward. #155 is the first paper in the lane with two page
geometries (a letter-format cover at 612x792 against 595.5x842 for the body), so any area fraction on
page 1 is computed against a different frame than the rest and the note must say so. And the
display-mathematics stream has grown a companion: pasted strips of typeset PROSE. #155 loses both
Summary paragraphs on p1 to a bitmap, plus a prose-plus-equation band on p16 - text that the text
layer never contains, so a quote from that region cannot be verified and must not be attempted.

## Checkpoint 150-152: region count is not exhibit count, and the grid recipe is a paper-level constant

Three consecutive 2018 B/A papers, 95 measured regions, 45 figure rows and 41 grid rows. Four
findings, all of them process rather than one-paper trivia.

**Region count runs both ways.** #151 prints one object and the detector boxes it twice (Figure 5,
one caption line under two halves), so regions overstate. #152 prints sixteen numbered figures and
delivers them in twelve regions, because four regions each hold TWO pasted figures behind one
image, so regions understate by four. Neither direction is safe: count printed caption numbers and
use regions only to locate them. Every future pass should reconcile the caption list against the
region list in both directions before writing rows.

**Rule style is chosen once per paper, not once per table.** #151 repeats one hybrid (three
horizontals plus a single stub divider) in 16 of 17 grids; #152 uses horizontal rules only in 5 of
5. Reading one grid tells you the paper's recipe. #150 is the counter-example that keeps this
honest - 17 boxed, one booktabs, one open-right vertical-rules grid - so the constant is a habit,
not a law, and it still has to be checked on each grid that differs in kind or section.

**Numbering punctuation is a paper-level constant too.** Bare `Figure N` / `Table N` in #150 and
#151; colon-form `Figure N:` / `Table N:` in #152, on both kinds, without exception. One caption
settles the paper.

**Citation discipline decays across the corpus, and #152 marks the step.** #151 cites no exhibit by
its own number at all and every citation lands on a numbering hole. #152 cites five of seven figures
accurately, by number, one page early - and cites no table by number even though both captioned
tables and all eight appendix tables are printed. So the 2018 habit is: figures are referenced,
tables are not.

**Systematic coverage gap, now twice observed.** Native Word tables produce no region: seven of
#150's fifteen numbered tables, six of #152's eleven. The region detector only boxes raster and
vector image blocks. Any paper with text-layer `Table N:` captions must be diffed against its
regions, and the difference declared in the note rather than patched with invented boxes.

## Checkpoint 146-148: the above-caption turns out to be a heading, and three kinds of box that are not exhibits

#146 and #147 agreed so exactly on caption side - 18 figures below and 6 grids above, then 19 below
and 1 above - that the rule looked settled: where a paper carries both kinds, side follows kind.
#148 breaks it in one page-pair: 12 grids captioned below and 7 recorded above, and the split does
not track section kind. It tracks `caption_source`. All seven "above" grids are unnumbered and
uncaptioned - three symbol grids, three office grids and the section 5 grid - and all five "below"
grids print a "Table N:" line. So on an uncaptioned grid the recorded position is not a caption
side at all, it is where the identifying HEADING sits; the census may not average the two states
together. #149, closed today, repeats the phenomenon on the figure side at four times the scale:
15 of its 56 figure captions sit above the artwork and every one of them is an appendix plate whose
"caption" is the Appendix heading over the frame. Rule of the batch so far: a caption above the
artwork is a heading above the block until a page shows otherwise, and the field that says which is
`caption_source`.

The exclusion list stopped being one thing. #146, #147 and #148 carry 10, 15 and 23 exclusions, and
display mathematics is the bulk of each (8, 8 and 23 recorded as such) - the detector reads typeset
equations as artwork in every paper in this batch that has more than two of them, which is now six
papers in a row. But each paper also added a class that has nothing to do with mathematics: #146
boxed two MATLAB code bands, #147 boxed four raster duplicates of its own vector figures and two
caption bands plus a rule band, and #149 boxed six caption bands and five column slices of two
pasted panel tables. `not-an-exhibit` therefore says only "not an exhibit"; the note has to say
which kind of not-exhibit, or the exclusion counts across papers will not be comparable. Duplicate,
fragment-of-other and caption-background are the labels that keep #147 legible; #149's column
slices needed a fourth and are filed as not-an-exhibit with the object named, because the slice is
neither a duplicate nor a fragment of another exhibit but the same raster measured in overlapping
windows.

The gap on the other side widened too. #147 showed one table the layout cannot see (a fifteen-row
abbreviation glossary with printed rules and no box). #148 has three: Tables 2, 3 and 5 are native
text tables, and the region pass boxed only Table 4 on p25 because that one happens to be raster,
while the p25 box runs from Table 3's caption through Table 4 into Table 5's header and the p20 and
p21 boxes each hold one office grid plus four rows of the next. So the detector follows images, and
where two printed objects touch it returns one box that belongs to neither. A census that claims
"every measured region is one exhibit" is false for that page; what it can honestly claim is that
every region is accounted for exactly once, with the note naming the printed objects it spans.
Everything this notebook has recorded since #144 rests on that weaker claim, and #149 is the
cleanest illustration of why the weaker one is the true one: its two 54-row appendix panel tables
are each measured three or four times because the raster is wider than any single box.
