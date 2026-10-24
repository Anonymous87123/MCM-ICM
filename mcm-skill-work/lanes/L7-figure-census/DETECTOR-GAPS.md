# Detector gaps found while closing papers

Lane-local record. Not a checkpoint file; the README checkpoints stay with whoever
closes the third paper of each batch.

## Tol-based stroke clustering can hide a drawn table

Paper `P-D-2021-2107091-7ebae97f` (#262), Table 4 on p12. The table is printed and
drawn, and owns no measured region.

Known detector gap: tol-based stroke clustering can fuse a rule pair plus its cell
verticals into a box above `RULE_HEIGHT_PT`, hiding a drawn table.

Measured chain (pymupdf on p12, page 595.28 x 841.89):

- 11 full-width horizontal rules, 398.59 pt, x 98.34 -> 496.93, y 95.57 -> 194.20.
- 9 cell verticals, each exactly 14.4 pt tall, at x 189.5 / 269.3 / 372.5.
- Stroke clustering at tol 8.0 fuses each rule pair with the verticals sitting within
  tolerance of both, giving stroke clusters of height 17.2 pt (e.g. y 112.80 -> 130.00).
- The rule seed filter is `h <= RULE_HEIGHT_PT` (12.0), so those 17.2 pt clusters are
  ineligible as rules. Only the isolated top pair (y 95.57 -> 97.98, h 2.4) survives.
- One seed makes a group of one; `len(group) < 2` drops it; `rule_table_regions` returns
  nothing.
- The same clusters are also too short for the ordinary region path: `h < MIN_SIDE_PT`
  (25.0) rejects them. The table is invisible to both paths.

Why no stroke measurement finds it: the loss happens in the clustering step that runs
before the seed, gap-grouping and alignment filters, so those filters never see a rule
box at all. Same class of failure as a table whose rules are too short to seed on.

No detector change was made from this lane. A real fix means seeding on per-drawing
strokes instead of clusters, which moves every paper already closed and is the tool
owner's call.

## A table with no drawn geometry is invisible to both paths

Paper `P-F-2021-2109443-9398701f` (#274), Table 5 on p12, captioned "the divisions
of McKinsey Matrix". The table is printed, has 2 columns and 4 rows of text, and owns
no measured region: the only region the pass finds on p12 is the display equation (8)
at y 283.9 -> 311.1, well above the table at y 604 -> 667.

Measured chain (pymupdf on p12, page 595.28 x 841.89):

- The table is typeset as plain text lines: no rules, no cell fills, no image.
- The layout pass has nothing to seed on - no stroke cluster, no fill band, no raster
  box - so neither the rule path nor the region path can open a candidate.
- The page's other 34 drawing items (5 black 0.47 pt strokes, 29 black fills) are the
  glyphs of the equation above, so "p12 has drawings" is true and still finds nothing.

Consequence for the census: the exhibit is unmeasurable, not merely unfound. Its row
cannot be recorded at all, and the paper's table list skips 5 while the figures run 1
to 13 without a gap.

## Table rules drawn as thin black FILLS rather than strokes

Same paper. Table 7 on p14 has 39 drawing items and NOT ONE is a stroke: all 39 are
type `f` fills (20 at grey 0.816, 19 black), and the four horizontal rules are 0.72 pt
black fills. Table 2 on p8 has 108 items, 7 of them thin black fills and 101 cell or
band fills (79 at grey 0.851, 8 at 0.557, 21 black).

Why a colour-only classifier fails: the "banding is the grid" case means the body
rules were replaced by alternating row fills, so a reader that looks for stroke colour
reports `no-rules` on a table that prints four rules. Rule style has to be read from
the thin fill bands (height < 1.2 pt) plus the fill colour, not from `color`/`width`.

## A page stamp can fuse into an exhibit region

Same block, P-F-2021-2122374-0c765494 (p10, page 612 x 792). Table 2's head runs to
x 488 and the page-foot WeChat stamp occupies x 448.3 -> 583.1, so the table's right
edge overlaps the stamp's x-range and the layout pass reports ONE region of 826 paths
instead of two. The split is exact and countable: 133 black fills are the table's own
rules (header, Input and Output groups), 689 pink fills at (0.75, 0, 0) plus 4 strokes
at width 0.048 are the 693-path stamp, and 133 + 689 + 4 = 826. The union bbox
[66.4, 159.9, 583.1, 789.1] takes its right edge and its bottom edge from the stamp,
so `area_frac` 0.6708 describes two different objects at once.

Consequence: p10 is the only page in the paper with no standalone stamp region - 25 of
26 pages carry the identical 693-path stamp at [448.3, 721.7, 583.1, 789.1] - and a
per-page "stamp present?" check keyed on a 693-path region would report p10 as
missing its furniture. The stamp has to be identified by the fill colour and the path
sub-count, not by region identity.

## Two image placements can share one page-plus-bbox key

Same paper, p15. Four image placements sit inside Figure 6's frame: two copies of a
293x94 px raster and two of a 294x107 px one, each pair at an IDENTICAL box
([167.0, 82.0, 460.0, 176.0] twice, [167.0, 82.0, 461.0, 189.0] twice). So the paper
has 50 regions but only 48 distinct page-plus-bbox keys, and the record - which
identifies a region as (page, rounded bbox) - reports 48 measured regions.

Consequence: on this paper a region count and a key count are different numbers, and
any completeness check that counts regions while storing keys will disagree by two.
Identifying the duplicate is also not enough to say what it is: the same chart area is
pasted at two heights, one 94 px and one 107 px, so "duplicate" here means two
different raster objects at one box, not one object drawn twice.

## A table can be a bitmap with no rules at all

Same paper, Table 3 on p14. The table is a 474x605 px raster at 137 x 152 dpi - the
raster is stretched 11 per cent vertically after pasting - and it has no rules, no row
banding and no cell fills: the only structure is three coloured header cells (beige,
teal, orange) and 21 ranked rows of type inside the bitmap.

Consequence: the drawing-based table path finds zero items and the rule-style
classifier has nothing to read, while the print is perfectly legible. This is the
mirror image of the fill-rules gap above: there, a fully ruled table looks "ruled" only
through sub-point fills; here, a well-set table has no drawn geometry beyond a
coloured header strip. `rule_style` `no-rules` therefore covers both a degenerate
text-only table and a modern styled one, and only the crop tells them apart.

## A caption can swallow the next sentence's first word

Same paper, p6. The caption prints as "Figure 3 The relationship between the three
dimensions of the status quo of industry performance: coverage" and the following
paragraph begins "is the cornerstone of fairness, and fairness is the basis of
achievement." The sentence's subject is missing because the caption line took it.

Consequence: the caption's tail is prose and the prose's head is missing, so a caption
detector that stops at the first full stop reads a caption that ends mid-thought, and
the artifact text layer additionally splits the word across the line break
("covera" + "e", with the "C" lost), so the same caption reads differently in pymupdf
and in the artifact. Recording the caption verbatim means keeping "covera" and
documenting the split rather than repairing it to "coverage".

## A caption can overlap its own table

Paper P-F-2021-2123945-e8b5b6e5, p5. Table 1's caption prints at the bottom of the
paragraph above the grid, its baseline at y 303.8 against a measured region that starts
at y 302.0, so the caption's line box runs 1.63 pt INTO the table box - the only
negative caption gap in the block. The other four tables in the same paper clear their
grids by 0.65, 1.09 and 4.20 pt.

Consequence: a side test that requires the caption to clear the box ("caption top above
region top by a positive margin") reports this table as uncaptioned, and a detector that
does not care about the box will happily assign the caption to the wrong side. Clearing
distance cannot be used as evidence of side when the print is this tight; only the
reading order of the page settles it.

## A watermark can print as live text inside an exhibit box

Same paper. Every page carries two watermark text baselines, "微信公众号：数学模型" at
y 126.2 and "微信号：MATHmodels" at y 307.5, plus a 693-path pink stamp block at the page
foot. The stamp is caught by the path-count filter and excluded on all 25 pages, but the
y 307.5 text line lands INSIDE six of the sixteen measured exhibit boxes: Figure 1 on
p4, Table 1 on p5, Table 2 on p7, Figure 8 on p19 and both panels of Figures 10 and 11
on p23.

Consequence: those six rows' interior text begins with a WeChat id, so any caption or
title extracted from "the first line inside the box" returns the watermark. The
furniture census must cover text baselines as well as drawing paths; a path-count filter
alone certifies these pages as clean when they are not.

## One captioned figure can be three separate exhibit boxes

Same paper, p10. Figure 2 is a single caption line, "Figure 2: Weight for 3 dimensions",
printed 14.6 pt under a row of three side-by-side donut rasters (556x429, 554x435 and
550x429 px at 300 dpi), each with its own four-key legend. The layout pass measures three
boxes at the same y with three different x-ranges.

Consequence: the exhibit count for the page is one, the region count is three, and the
surplus is not furniture and not a fragment - it is panels. Counting each box as an
exhibit triples one figure; recording one box and dropping the other two loses what the
caption covers. The row is recorded on the left panel with panel_count 3 and the middle
and right boxes are `duplicate` exclusions.

## A wrapped body sentence can pose as a caption

Same paper, p12. The body writes "We apply 3DVA to some countries and obtain the results
shown as Figure 4 and" and the wrap puts "Figure 5." alone on the next line, 200 pt above
the artwork, which itself is captioned "Figure 5: Application 5-8" under its raster.

Consequence: a caption detector keyed on a line that starts with "Figure N." takes the
wrapped tail as Figure 5's caption, leaves the real caption unpaired, and reports the
page as having two captions instead of three. Caption detection needs either the colon
form or a position test against the nearest box, and this paper uses the colon form on
all sixteen of its real captions while the false positive carries a full stop.

## Row counts cannot come from text baselines in these tables

Same paper. Table 1's descriptions wrap, so 17 rows produce 31 text baselines; Table 3 is
laid out transposed, with the eight country names in the header row and "Modulus" and
"Deviation Angle (◦)" in the stub column, so the first column of the text layer is a
metric label rather than a row label.

Consequence: baseline clustering over-counts Table 1 by fourteen rows and misreads
Table 3's header as a data row. Both row counts were taken from the rule geometry
instead (5 rules over a 307.3 pt block at 18 pt per row = 17; 4 rules over 67.6 pt = 3),
which is the only reading that agrees with what the page prints.
