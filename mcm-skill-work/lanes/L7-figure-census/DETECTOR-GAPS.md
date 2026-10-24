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

## A caption eight points below the art can be read as eight points above

P-A-2022-2207343-9469a4fe, pp14, 16, 19 and 21. Figures 12, 16, 20 and 22 were recorded
with `caption.position` "above". Every one of the four captions is printed UNDER its
region: the gap from the region's bottom edge to the caption's line box is 7.93, 8.20,
7.94 and 8.21 pt.

Why the inherited reading went the wrong way: all four regions sit at the top of their
page (y0 74.98-75.42), so the caption line lands in the band where a body heading would
print, and the section heading that follows the exhibit is what the page actually
delivers next. A reader who takes the caption's side from the surrounding page structure
sees "text below the box" and calls the exhibit uncaptioned-from-below; the offset alone
settles it, but only if the reader bothers to measure it.

Consequence: four of the paper's twenty-three figures were drawn on the wrong side, and
the error is systematic - every figure that opens a page has it. Side has to be measured
against the box, never inferred from where the art sits on the sheet.

## Two table captions print inside their own grid

Same paper, p16. Table 8's caption overlaps its measured region by 1.24 pt and Table 9's
by 1.12 pt, while the other eight table captions clear theirs by 1.16-1.24 pt. The ten
captions come from one paragraph of introduction set above each grid, and the two on p16
were typeset tight enough that the caption's last line box crosses the header rule.

Consequence: a caption-side test that wants a positive clearance reports Tables 8 and 9 as
uncaptioned, which drops two of the paper's ten measured tables. The reading order of the
page is the only evidence that survives here; the gap does not. Same failure as the
overlapping caption in P-F-2021-2123945-e8b5b6e5, but this paper produces it twice in one
column of one page.

## A table printed as live text owns no region and no rules

Same paper, p11. Table 6, "The results of each turn", prints as five lines of plain text
inside the flow - caption line, header row (Curve number / A / B / C / D / E), a Pout row
and a v row - with no rule, no cell fill, no raster and no box. The paper's other ten
tables are booktabs with three drawn rules each; this one is a table the layout pass
cannot see, so the census carries ten table-grid rows against eleven printed table
numbers, and the numbering run reads 5, 7 with 6 missing.

Consequence: "the paper has eleven tables" and "the census measured ten tables" are both
true statements and a completeness check that compares them will report a defect that is
not there. The missing region is the correct measurement. Reconciling the two counts needs
the text layer, not the drawing layer.

## A promotional sheet fragments into one region per pasted tile

Same paper, pp24 and 25. The two appendix sheets are RIDERMAN flyers and the layout pass
splits them into eighteen regions on p24 and seven on p25. On p24 the enclosing leaflet
raster is region 12 at [27.84, 452.28, 566.34, 821.82] and ten smaller rasters sit inside
its top band; on p25 the enclosing raster is region 1 at [28.44, 18.84, 566.34, 717.78]
with two chart tiles inside it. The same picture is therefore measured once as a whole and
again as each of its parts.

Consequence: a per-region census of these two pages reports 25 exhibits where the paper
prints three, and a "count the regions, count the exhibits" check disagrees by 22. The
tiles have to be excluded as fragments of the enclosing raster, which only works if the
fragment reason is available and the enclosing box is recorded first. Both sheets also
carry four line-art cyclist cartoons at the page foot, in the same y band as the leaflet,
so proximity alone does not separate furniture from tile.

## A cover photograph is not page furniture

Same paper, p24. The flyer's masthead is region 1 at [0.0, 0.0, 595.14, 201.18] - the full
page width, `area_frac` 0.239 - carrying the headline "SWIFT TO WIN! WITH OUR MATHEMATICAL
OPTIMIZATION MODEL" over a forest-road photograph with overlaid force vectors and a best-
racing-route arrow. It was excluded in the inherited draft as a "raster tile of the
appendix sheet's photo collage", together with ten rasters that really are tiles inside it.

Consequence: an area filter that drops full-width bands reports this photograph as
background, and a detector tuned to subtract page furniture from a flyer page will subtract
the most prominent picture in the whole appendix. The band is content: it is recorded here
as a `photo-or-raster-image` exhibit with no caption, and the ten rasters nested inside it
carry the fragment reason instead.

## The ligature in "fig." hides every pointer from an ASCII scan

Same paper, whole document. The text layer spells the abbreviation with U+FB01, so
"ﬁg. 4" is one character plus "g", and a regex that looks for `fig` or `Figure` finds
twenty-nine numbered matches of which only five are real pointers - the ASCII "Fig." once,
"Figure 19" once and three "Table N". Normalising U+FB01 to "fi" first turns up twenty-four
ligature pointers that were invisible before, and the paper goes from "four exhibits are
cited" to "twenty-two are".

Consequence: this is not a flaky detector, it is a total blind spot on any paper typeset
with a ligature-aware font. Counting pointers without normalising gives a number low by a
factor of five. The same normalisation is needed before subtracting caption lines, because
the caption "Figure 3:" is ASCII while its pointers are not.

## A pointer can wrap between the abbreviation and its number

Same paper, pp3, 7 and 12. Three pointers put the abbreviation at the end of a line and
the number at the start of the next: "shown in ﬁg." then "11)." on p12, a bare "ﬁg. 1."
alone on a line of p3, and "the power curve in ﬁg .3" on p7 - that last one with a space
between the abbreviation and its number where the paper prints it that way.

Consequence: a line-scoped pointer scan misses all three and reports Figures 1 and 11 as
never cited, which they are not. The p7 case is worse than a wrap: the token is
"ﬁg .3", so even a normalised regex keyed on `fig\.\s*\d` fails until the space before the
number is allowed. [mention.style] keeps the printed form, space and all.

## A running head can disagree with the folio by three pages

Same paper, every sheet. The header reads "Team # 2207343 / Page N of 22" and runs one
behind the physical page - p11 prints "Page 10 of 22" - but the file has twenty-five
pages, because the three appendix sheets are not counted in the header at all. So the head
is off by one at the front and by three at the back, and the two errors cancel nowhere in
between.

Consequence: any cross-check that joins a measured page number to a printed folio has to
add one, and any check that trusts "of 22" as the page count truncates the last three
sheets - the three that hold the only photo and the only uncaptioned appendix exhibits in
the paper. Printed folios are not page indices.

## Per-column rule segments can put a table under the half-page bar

P-E-2022-2202838-75410db9, pp8, 18 and 19. Six table numbers print and only three own a
drawn region. Tables 2, 5 and 6 draw their booktabs rules as a run of per-column segments
rather than one page-wide stroke: the widest single segment in each band is 93.7, 98.9 and
87.1 pt, and `rule_table_regions()` needs `w >= 0.5 * page_w` (306 pt on Letter) before it
will consider a rule at all. So no rule qualifies, the segments are discarded as dividers,
and the three tables vanish - p19 is even reported as "165 paths but no measured region",
which reads like a broken page and is in fact a complete table.

Consequence: the half-page gate is a width test on one stroke, and a LaTeX table set with
column-separated rules leaves no stroke wide enough to pass it however dense the grid is.
A gap warning on a page that is plainly furnished is a signal to measure the band directly
(the sum of the segments in one row equals the table width) rather than to trust the empty
region list. Census here carries three table rows against six printed numbers, and the
deficit is the detector's, not the paper's.

## A measured region can stop short of its own table's last rows

Same paper, p5. Table 1's box ends at y 168.4 while two notation descriptions still print at
173.4 and 191.4 and their vector glyphs run to 203.2, all inside the column and all inside
the drawn caption-to-body rule pair. The region is a correct measurement of the *rules and
the rows they enclose up to the last horizontal rule*, and the table has no closing rule
under its final row, so the box closes early by two rows.

Consequence: `[table.rows]` here is the printed count - one header row and six body rows at
18 pt pitch - and not the row count the bounding box can be cropped to. A per-region row
count derived from baselines inside the box would report four of six, and the missing two are
exactly the rows a reader checks against the notation list. The absent closing rule is the
tell: a booktabs table with two rules where three are expected has been measured short.

## A caption can overlap the bottom of its own region

Same paper, p17. Figure 7's region ends at y 445.7 and its caption baseline sits at 441.4, so
the caption prints *inside* the last four points of the measured box rather than below it. A
side test written as `caption_y >= region_y1` fails on it; one written as `caption_y >=
region_y0` passes on captions that are hundreds of points above the art.

Consequence: caption side needs a proportional test - the caption's line top against the
region's vertical midpoint - not an edge test against either boundary. Figure 7 is the only
one of fourteen captioned exhibits in this paper where the two disagree, and it is the one
where a naive below-test would have flipped the position flag and, with it, the paper's
otherwise unbroken "captions always below figures" rule.

## An exhibit can belong to the heading above it, not the heading below

Same paper, six rows. The context pass attaches a region to the last heading on the page,
which for a page-opening exhibit is the heading that prints *under* it: Table 1 was placed
in section 4 when it prints above the section 4 heading on p5, Figure 1 in "3 Notation" when
it belongs to 1.3 Our Work, Figure 6 in 6.2.2 when its true section 6.2 heading prints at
y 312.4 below the art at y 87.6. The mirror case is just as common: Table 3 sits above the
6.3 heading at y 573.9 and belongs to 6.2.5, Table 4 and Figure 7 above the section 7 heading
at y 614.9 and belong to 6.3.3, Figure 10 above the section 8 heading at y 435.7 and
Figure 11 above the section 9 heading at y 271.8.

Consequence: `[place.section_path]` has to be read from the printed heading order against
the exhibit's y coordinate, and a heading whose ink starts below the region cannot own it no
matter what the nearest-neighbour attachment says. Seven rows kept the context path and
eight were overridden; the overrides are all of this shape, so the rule is mechanical rather
than judgemental.

## A caption can be split across two lines in reverse order

Same paper, p5. Figure 2's caption is not one text line. The extractor returns the tail of it
above the head - the second line first, then the first - so a slice-and-join in reading order
produces "network with 4 hidden layers in each layer. Figure 2: Schematic of a feed-forward"
and the caption fails the verbatim test on its own page.

Consequence: this row is recorded as `caption_source: "typed-from-crop"` with the assembled
string, and the reorder is stated rather than hidden. Two-line captions elsewhere in the
block print in order and slice cleanly; the variable is the placement engine, not the
caption. A payload builder that trusts line order silently records a caption no reader can
find in the text and a mention matcher then reports zero pointers for a figure cited twice.

## A pointer can print with no space before its number

Same paper, p18. Body text reads "Figure8(b)", the only one of eleven pointer spellings with
the number welded to the word. The other ten are ASCII "Figure N" with the sub-label in
parentheses, and five "Table N" pointers are clean.

Consequence: a scan keyed on `Figure\s+\d` misses that pointer and reports Figure 8 as cited
once when it prints twice. `Figure\s*\(?\d` catches both forms, and the spelling set keeps
the welded form as printed so the row shows the anomaly instead of normalising it away.

## A decorated article page can sit inside an otherwise plain letter file

Same paper, p23. One sheet of twenty-five is 595.32 x 841.92 pt (A4) against 612 x 792 for
the rest, laid out two columns with a headline in display type, foliage behind the text, a
stump clip art and a forest-scene band across the foot - a newspaper-style coda in a
mathematics paper. It carries the file's only uncaptioned photograph, cropped into the text
column, which is an exhibit: it is content, and the paper's argument runs through it.

Consequence: page size is a per-page property even in a single-rendered file, so a detector
that measures in fractions of one page width is measuring against a different sheet here.
Of the four rasters on p23 exactly one is content and three are furniture, and the
discriminator is not size - the foot band is the widest of the four - it is whether the image
prints inside the text column and interrupts the prose. An uncaptioned photograph has to be
recorded as an item with an empty caption, and `[caption.verbatim]` being empty is not
grounds for excluding it.

## A furnished page can report its footer artefact as its only region

Paper `P-D-2019-1902407-b8153b5d` (#176), pp6, 12 and 18. Each of those pages prints a
captioned table with a full Word double-rule grid, and each owns no measured region: the
layout pass returns the page-foot stamp band and nothing above it. p18 is the extreme
case - its entire region list is the footer artefact, so a "does this page have regions"
test says yes while the only content on the page is unmeasured.

The distinction that matters is not "empty page" but "artefact-only page": a page that
produced furniture has been through the whole measurement chain and come out with the
wrong object, which is a different failure from a page that produced nothing. The counter-
case in the same paper is worth recording because it kills the obvious workaround: no
page there emits a region above its footer band at all, so re-measuring the band directly
does not recover the table - there is no band to measure. Recorded as three declared
deficits, taken from notes rather than from boxes, because the record cannot carry a bbox
the measurement layer never produced.

## A caption whose object is a math symbol loses it in the text layer

Same paper, p12: the printed "Figure 8 Strategy to reduce T4" extracts as "Figure 8
Strategy to reduce " followed by unreadable glyphs. Paper `P-E-2022-2203489-75977cc9`
(#307) repeats the mode four times - p13 and p17 "Bubble chart of ... values" with the
whole object replaced by glyph garbage, p22 "Forest's ... - ... Curve" keeping only the
minus sign, and p23 "Sensitivity analysis of" where the line ends on a space and the
object is simply gone.

Consequence: the object of a caption is usually the variable the exhibit measures, so a
caption harvested from the text layer understates the exhibit and a
`caption_flags.variables` computed from it reads false where the printed caption is true.
Those rows are recorded `typed-from-crop`. #307 goes further and doubles every math glyph
in the layer - six `C` glyphs standing for COI, `δδ`, `TTTTTTTT` - so the
corruption is not always loss: a slice-and-join can assemble a caption made of the right
number of the wrong characters and still pass a length check.

## A borderless table is invisible to both measurement paths

Paper `P-E-2022-2203489-75977cc9` (#307), seven printed tables on pp4, 6, 8, 11, 14, 18
and 20. Every one is live text set with column gaps: no rule, no fill, no box. The
band-scoped drawing count inside each table's band prints zero on all seven pages
(p4 y 680-800, p6 y 140-260, p8 y 390-500, p11 y 120-300, p14 y 600-720, p18 y 140-340,
p20 y 570-700). With no drawing operator in the band, neither the rule detector nor the
vector-cluster path has anything to seed on, so twenty-two printed exhibits produce
fifteen regions and the deficit IS the rule.

This is not #274's case (a table with no drawn geometry on a page that still holds a
display-equation region): here the page holds nothing else either, so the loss is total.
Declared as seven deficits in the record; the p4 caption is additionally welded into its
own header cell - "Symbol<12 spaces>Table 1: Notations used in this paper" - which defeats
any caption scan anchored with `re.match` at the start of the line.

## A full-page raster can be an exhibit and own no region

Same paper, p25. One image, 1440x2080 px, covers the sheet: a newspaper-style page with a
masthead, three inset photographs and its entire text rasterised. The pass measures it
nowhere. The only two regions on that page are the team-number stamp in the corner
[-9.0, -8.04, 175.44, 58.8] and the same stamp measured again five points off,
[-4.08, -4.08, 177.36, 60.72], filed `background` and `duplicate`.

So a coverage check has to ask whether a page's ink is accounted for, not whether the page
has regions - the same lesson as #176 from the opposite side. The sheet is also the paper's
thesis object: the exhibits' argument ends on it, so it is the one page that cannot be
dropped as decoration.

## A printed exhibit number is not a key

Same paper. "Figure 2" prints twice (p6 biomass-time curve, p7 NDVI raster) and
"Figure 12" prints twice (p20 a 100 % stacked composition bar, p21 a qualitative Kuznets
sketch with no ticks at all), so fourteen caption rows carry only thirteen distinct
numbers; separately, Figures 3 and 15 are named in prose and never printed anywhere.
Captions repeat too: Table 2's caption is Table 1's word for word, and Tables 5 and 6 share
one caption over two grids of different shape ("height and DHB analysis under different
IOIC in thinning", the paper's only DHB/DBH spelling break).

Consequence: a row keyed on (kind, printed number) collides. Rows must key on the measured
region, with the printed number recorded as a caption property, and a duplicate number is a
finding to report rather than a bug to merge. A pointer to a number that prints nowhere is
evidence the numbering layer is broken upstream, and it belongs in the notes of the exhibit
it should have named.

## A body sentence can pass a caption test

Same paper, both directions. p17 opens "as an example, and the thermal map of the result is
shown in Figure 8. At the same time, our", which a `(Figure|Table)\s*\d+\s*[.:]\s+\S`
scan accepts as a caption - phrase, full stop, capitalised word - and returns sixteen
captions for fifteen figures, with Figure 8 counted twice and its pointer count driven to
zero because the pointer pass strips caption lines before matching. p22 carries the reverse
case: the line "Figure 14:" alone, the caption head with its object on the next line, so
requiring a title after the number discards a real caption.

The rule that survives both, and the cell weld on p4, is: accept the phrase when it opens
the line or follows a run of two or more spaces, require a title after the number, and
prefer the region the caption sits beside over the line itself. Verified on this paper it
returns fifteen figure captions on thirteen numbers, seven table captions, and pointer
counts equal to the record for all fifteen rows.

## A section walk that stops at the page boundary files a page-opening exhibit late

Paper `P-E-2022-2216618-127926c7` (#309). Figure 5 prints at the top of p14 at y 86.4 and the
only heading on that page, "4.5 Evaluating the total value of a forest", prints at y 489, at
the foot of it; the heading that owns the figure, "4.4 Analytic Hierarchy Process (AHP)",
is on p13 at y 604. A forward walk over the headings of the exhibit's own page therefore
finds 4.5 above nothing and either attaches the row to 4.5 or, if it only accepts headings
printed above the art, finds no heading at all and keeps whatever the context pass gave it.
Both answers are one section out, and the error is silent - "4.5" is a real heading of the
right section, it merely prints under the exhibit instead of over it.

The mirror direction is in the same paper: Table 3 and Figure 4 print on p10 below the "3.4
The optimal forest management plan" heading at y 85 while the paragraph introducing them
continues 3.3 from the previous page, and Table 2 prints on p9 above the 3.3 heading, so it
belongs to 3.2. Three rows, three different relations between the printed heading, the
exhibit's y and the prose that introduces it, and in every one the printed heading order
wins over the prose.

Consequence: the walk has to carry the last heading seen in document order across the page
break rather than restart at each page, and it must compare that heading's y against the
region's top edge only when the two share a page. Read as a forward walk over the heading
stream this is the same field mcm-5e recorded failing one or two subsections late on their
papers - one entry, one cause: the heading that owns a page-opening exhibit is usually on
the page before it.

## A caption's math glyphs can be displaced, not only doubled

Papers `P-E-2022-2203489-75977cc9` (#307) and `P-E-2022-2216618-127926c7` (#309). #307
doubles: six "C" glyphs standing for COI, a doubled delta. #309 displaces: the printed
"Figure 11: y¯m1-T˜ curve for Amazon rainforests" extracts from the PDF as
"Figure 11: ¯ym1- ˜T curve for Amazon rainforests" - the macron and the tilde are correct but
have moved to the FRONT of the character they modify, and the hyphen has slipped in front of
the tilde. The text-layer page file keeps the printed order; the PDF line extraction does
not, so the same caption reads two ways inside one paper depending on which layer is asked.

The displacement breaks line matching rather than pointer matching: a check that compares the
first eighteen characters of the recorded caption against an extracted line reports the
caption missing on a page where the caption is present and correct. Matching on a
letters-and-digits key (strip spaces, hyphens, macros and diacritics, compare the first
sixteen characters) survives both the displacement and #307's doubling.

Consequence: a caption read out of the text-layer page file and a caption read out of the PDF
line pass must be compared through a normalised key, never character for character, and the
printed reading stays in `[caption.verbatim]`. The same paper's Figure 12 shows the other
half of the problem: the caption prints "T(y) curves for different w" and extracts with a
space inside "T (y)" and the ff ligature replaced by a return arrow, so no text-layer search
matches it at all and the row is `typed-from-crop`. Count the caption's sentences by eye at
least once per paper - a glyph that changes count changes `[caption.sentences]` too.

## A zero-deficit census is the exception, and it needs the printed count to close

Same paper. Fifteen printed exhibit numbers - Figures 1 to 12 and Tables 1 to 3 - and
seventeen measured regions, every one of them resolving to a row: thirteen figure rows,
three table rows and one refusal. The arithmetic closes exactly, which is not the norm for
a LaTeX-set paper in this lane and must not become the assumption: the census is closed
because the printed count was taken independently (twelve figure captions and three table
captions, no duplicates, no number cited and never printed) and then matched against the
regions, not because the region count happened to look plausible.

Consequence: run the printed-count check first and let the region count be the thing that
has to reach it. "Seventeen regions, seventeen rows" is only evidence after the fifteen
printed numbers are in hand; without them it is a coincidence waiting to be reported as a
closure. The same discipline turns the opposite case into a finding rather than an
embarrassment - `table_items` 0 with no deficit means the paper printed no grids, while a
printed table with no region means the grid printed and the measurement missed it, and the
two look identical in the counts alone.

## Two regions can share a header line

Reported by mcm-5e from their own rows: an object measured twice, with the frame verticals
running unbroken through the cut between the two boxes. The two regions abut along a line
that belongs to both of them, so the second box's top edge and the first box's bottom edge
are the same rule, and nothing in the numbers distinguishes the pair from two genuinely
separate exhibits except that the verticals never break.

Consequence: the positive split test for "one object, measured twice" is a header line the
two boxes share with the verticals unbroken through it; the positive split test for "two
objects" is the verticals breaking or a gap between them. Area and adjacency alone cannot
tell the cases apart, so a duplicate has to be argued from the grid and not from the box.

## When every figure is a raster, the drawing detector has nothing to find

Same paper. All twelve figure regions hold exactly one embedded raster each and the pages
carry no other image anywhere: every quantitative exhibit is a screenshot of a plotting tool,
so the PDF itself draws no axis, no curve and no tick anywhere in the paper. A vector-cluster
pass over `get_drawings()` therefore finds no figure at all on any page, while a raster-box
pass finds all twelve - and the two passes agree on the region only because the raster is the
whole figure.

The tables are the exact opposite and live in the same file: three live-text booktabs grids,
no raster, three horizontal rules each and nothing else. Two of the three set their header
rule narrower than the body rules - Table 2 by 70.8 pt (274.9 against 345.7) and Table 3 by
120.4 pt (293.4 against 413.8) - so a rule detector that counts only full-width segments
counts two rules on those tables instead of three and would report a malformed grid.

Consequence: the raster path and the drawing path have to be run and reconciled rather than
either one trusted, and the rule count inside a table's bbox must accept a horizontal segment
of any width across the table's own columns. A booktabs header rule is measured to the header
text, not to the table's width, and that is the table being correct.

## Two captions can share one printed line

Paper `P-E-2022-2218144-2f85ee8c` (#310). Three pairs of figure captions print on one shared
line: "Figure 9: 2020 bisector surface Figure 10: 2025 bisector surface" on p19, "Figure 12:
Strategy score before      Figure 13: Strategy score after" on p21, and "Figure 14: Change of
Z under different Figure 15: Change of Z under different" over a second line "n under m =
0.0233  m under n = 0.0021" on p22. A detector that accepts a caption only when the phrase
opens its line finds twelve of the fifteen figure captions and reports three missing exhibits
on pages where both captions are printed. The separator between the members is not a fixed
gap - two spaces on p19, six on p21, ONE on p22 - so widening the accept test from "line
start" to "line start or two spaces" still misses p22.

Consequence: after a line-start caption, every further caption phrase on the same line is a
second caption of the same pair and must be taken as one, with no gap test at all; and each
member's sentence is then assembled from the printed fragments, so all four members of the
p21 and p22 pairs (Figures 12, 13, 14, 15) are `typed-from-crop`. Two bare "Figure N." lines
in the same paper are not captions either: "Figure 3." on p7 and "Figure 6." on p12 are the
wrapped ends of the prose sentences that name those figures, so a caption test that accepts a
phrase at line start will invent two captions that do not exist while missing two that do.
The printed count is the only thing that settles it: fifteen numbers, fifteen rows.

## A page the layout pass never emitted is invisible to any loop over its page list

Same paper, p24. The layout JSON carries fifteen page entries - the pages that own a region -
and p24 is not among them: it has no entry, no region list and no bbox, not even an empty one.
A walk written as `for page in lay["pages"]` therefore never visits it, and the page is not
reported as a page with zero regions because it is not reported at all. The page prints the
paper's required newspaper article as ONE raster of 585.8 x 835.9 pt covering the sheet and
carries zero characters of text layer, so no text-side pass can reach it either.

Consequence: the coverage arithmetic has to be closed against `page_count` from the PDF, not
against `len(layout["pages"])`, and the difference between the two is the list of pages that
have to be explained one by one. Here it is one page, it is content, and it cannot be recorded
because there is no measured bbox to record - so it is declared in the rule list. The same
subtraction on a paper where the missing pages are all decoration is the cheap way to prove
the layout pass really did see every sheet.

## A figure that looks drawn by the PDF is usually still a paste

Same paper, Figure 8. The unit-cube vector diagram prints as five arrows, three ticked axes
labelled 0.0 to 1.0 and five coordinate triples - the one exhibit in the paper with no chart
junk, no screenshot frame and a cleanly drawn grid, and the first read of it recorded "drawn
by the PDF itself rather than pasted as a raster". It is a 1225 x 1100 px image pasted at
212.6, 86.4 to 382.7, 228.1, and the page holds no drawing path inside the region at all.

Consequence: apparent vector quality is not evidence of a vector exhibit. The positive test
is `get_drawings()` inside the region and `get_images()` inside the region, run per region,
and this paper makes the point sharply: all fifteen figure regions hold exactly one raster
and zero paths, while every one of the file's 54 drawing paths is a rule - a 422.5 pt header
rule at y 63.3 on every body page, the eleven table rules, and small inline fragments. A
figure counted as "drawn" costs the record its raster note and, worse, invites a reader to
type values off a picture that was never vector in the first place.

## An unnumbered exhibit belongs to the heading that calls itself an appendix

Proposed by mcm-5e from their own papers and adopted here as the rule for unnumbered rows:
when an exhibit carries no number, the section walk's answer is only trustworthy if the
heading it lands on says in its own text that the region is an appendix, an index, a list or
an annex. A page-opening screenshot with no number has nothing else to anchor it - the
nearest heading may be a subsection whose prose continues past it, and the printed order does
not distinguish "belongs to this heading" from "prints on this heading's page".

Consequence: for unnumbered rows the recorded `place.section_path` may not rest on the
heading position alone; the heading's own words have to name the exhibit class, or the
position has to be declared a best reading in the row's note. The check is cheap - the label
is already in the path - and it is the difference between a filing and a guess.
