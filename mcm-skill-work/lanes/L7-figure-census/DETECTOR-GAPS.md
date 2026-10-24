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

## A caption can be a bare label with no words at all

P-A-2022-2200289-b3e3573b, pp16, 18, 19, 20. Four of the twenty-one exhibits are
captioned with nothing but a number and a colon - "Figure 10:", "Figure 15:", "Figure
16:", "Figure 18:" - and the description they are missing is printed as (a)/(b)
sub-labels 6.66-6.89 pt under the panel boxes, outside every measured region.

Consequence: a caption test that wants a noun phrase, three words, or a capitalised
title drops a fifth of this paper's exhibits and reports twenty-one captions as
seventeen. `caption.words` is 2 on those four rows and 4-11 on the other seventeen, so
the field is populated correctly and only the acceptance rule is wrong. The words
themselves have to be taken from the sub-labels if a census wants to describe what the
figure shows.

## A wrapped body mention can sit hundreds of points above its own art

Same paper, pp15 and 17. The body writes "Therefore, we smooth it as shown in" and "the
optimization process curve is shown in", and the wrap leaves "Figure 9." and "Figure
13." alone at the start of the next line - 217 pt above Figure 9's art on the following
page, 459 pt above Figure 13's art on its own page. Both are body pointers, not
captions, and both are closer to the top of a page than to any box.

Consequence: a detector keyed on a line that begins with "Figure N." produces two
phantom captions and, in the p17 case, two candidate captions for one exhibit. The
discriminator here is punctuation: all twenty real captions take an ASCII colon and
these two take a full stop. It cannot be position alone, because one of the two sits
near the top of a page where a real caption above a table would also sit.

## Distortion can be a pairing artefact rather than a scaling policy

Same paper. All four two-panel figures are squeezed into 212.6x141.7 pt (aspect 1.500)
boxes from rasters of aspect 1.334 (875x656) and 2.341-2.462 (1557x665, 1551x630) or
2.071 (2400x1159), so x and y dpi disagree - 296x333, 527x338, 525x320, 813x589 - while
all sixteen single-panel rasters match their box aspect to three decimals.

Consequence: an aspect test that samples a few figures can conclude the file has no
scaling problem, since every standalone figure is pixel-exact. The failure is confined
to the paired layout, where the two panels were scaled to a fixed width and the height
allowed to follow. Recording panel_count is what makes it visible: the aspect mismatch
and panel_count == 2 are the same eleven exhibits here, with no counterexample.

## A heading printed below an exhibit cannot own that exhibit

Same paper, eleven of 21 regions, and 19 of 21 paths. The context extractor assigns a
region to the last heading at or above its box, but this paper prints section headings
after the art, so Figure 1 on p5 is filed under "2 Assuptions and Justifications"
although it sits in "1.3 Our Work", Figure 3 on p9 under "5.1.2" although it belongs to
"5.1.1 Power Curve", Figure 12 on p17 under "6.1 Weather Conditions" although it is in
"5.4", Figure 16 on p19 under 6.2 although it belongs to 6.1, and Table 1 on p7 under
"5.1.1 Power Curve" although "4 Notations" prints under it.

Consequence: every place assignment in this file needed hand replacement, and the
context section paths also carry TOC debris ("5 Analysis and Modeling 6", where the 6 is
the TOC page number) and the parent heading echoed twice. The record's 21 place fields
come from a text-layer scan, not from the context file; the override has to supply
section_path, section_numbered and section_kind together because the merge reads the
region's own key eagerly.

## Table rules can be drawn past the edge of the sheet

Same paper, p7. Table 1 is booktabs - three horizontal strokes at y 107.3, 122.1 and
512.6, no vertical rule, no box - and all three run from x 72.0 to x 612.6 on a 595.3 pt
page, so 17.3 pt of every rule is off-sheet and clipped.

Consequence: a detector that trusts the drawn extent measures a table 540.6 pt wide whose
right edge does not exist, and a column fit derived from that extent puts the third
column entirely outside the printable area. The body text column here is 72.0-523.3; the
table's rules are the outlier, not the text. The width came from the text extents in the
record, and the rule span is reported as measured rather than corrected.

## Row counts in this table cannot come from text baselines

Same paper. Table 1 has 28 rows (a header and 27 symbols) laid out over 390.5 pt at a
14.46 pt pitch, but its 80 text lines collapse to only 55 distinct baselines at 0.1 pt
precision - the symbol, its description and its unit share a line - and superscripts
shift some baselines by 0.3 pt.

Consequence: clustering lines into rows by baseline yields 55 rows, and clustering with a
0.5 pt tolerance yields 28 only by accident of the pitch. The reading taken here is the
rule geometry (three rules over 390.5 pt = 27 data rows, confirmed by 27 text lines in
the x 120-160 symbol column) and it agrees with what the page prints.

## A zero-height header rule makes every page look furnished

Same paper, all 25 pages. There is no stamp, no watermark and no background raster
anywhere in the file, but every page carries one drawing: a hairline of zero height
running x 72.0-523.3 at y 48.9 (y 98.8 on the title page), the header rule under the live
running head "Team # 2200289 Page N of 24". It never encloses anything and has no
interior, so no region was emitted for it.

Consequence: a furniture detector that hunts for any repeated mark finds 25 candidates
and would file a header rule as twenty-five background regions, while a detector that
only subtracts large blocks finds none at all. Both readings are wrong the same way: the
correct exclusion list for this paper is four panel fragments and nothing else, and the
running head is text at y 37 that never enters a box. Absence of furniture is a finding
that has to be recorded as an absence, not inferred from a detector staying silent.

## One drawing can serve two figures and one course two renderings

Same paper. Figures 5 and 6 print the same cyclist-and-bicycle silhouette - identical
helmet, torso, frame, saddle and rear-derailleur cluster - rotated a few degrees and
carrying different force vectors; and one course is rendered twice, as Figure 13's
isometric loop and as the flat distance-elevation curve of Figure 18's right panel. But
Figure 2, captioned as a topographic map of the same 2021 course, is a thresholded
terrain silhouette with a twin-peak skyline and no drawn route line at all.

Consequence: two traps. A reuse check needs the crops side by side, because the silhouette
is rotated, so neither a hash nor an aspect test catches it; and the family split - 10
line, 5 flowchart-or-schematic, 3 scatter, 1 surface-or-3D, 1 other - cannot be predicted
from captions that all say the same thing, since "Power Distribution" is a line ten
times, "Analysis on vw" is a scatter, and one hill is classed surface-or-3D in Figure 13
while its sibling panel is a plain 2-D line. Figure 2's caption says "map" and its pixels
say "black skyline with nothing drawn inside", so a caption-driven classifier would file
it as a map and never notice there is no route on it.
