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
| 140 | P-F-2017-68940-3e5f9c47 | 52 | 46 | 11 | 10 | closed by mcm-5e, `check.py` layout identical, unaccounted 0; 46 measured regions = 11 figures + 10 tables + 25 exclusions (23 NetLogo code pages pp26-48, the p1 summary-sheet control block, the p2 POLICY ADVISORY banner). The paper is close to captionless: twelve of its 21 exhibits print no caption at all, and the five that do split into two grammars - 'Figure N:' sentences below the artwork (Figure 1, Figure 3 printed once over a three-panel row, Figure 4) and the bare words 'Table 1' / 'Table 2' above the appendix grids. The p16 pair and the p20 triple are single figures whose regions were measured separately, so each set repeats one doc_order and carries `is_panel_of`; neither set shares a y scale, the p20 panels topping out at 200, 205 and 246. Families: six ggplot histograms, one NetLogo life-cycle flow chart, and three line series of which two are pasted screen captures - the p10 Gapminder chart still prints its country chip and time scrubber inside the image, and the p11 Canadian series labels its x axis with bare two-digit years 95 to 15. All ten grids are boxed with verticals at every cell boundary and none is shaded; only the four-column maternity/paternity grid merges cells or carries two header rows. Six grids are announced by a deictic sentence on their own page, two are read only from below, and Tables 1 and 2 are announced on p7 for pp24-25 - a seventeen-page lead. p2 is an A4 sheet inside a US letter document, the paper's one page-size break. |

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
