"""Close paper 85 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]

ROW = (
    "| 85 | P-D-2015-34985-c7be0d8b | mcm-9a | closed 2026-10-24 sha cf71e1c0e57d7da0 "
    "(figures=11 tables=3 excluded=0 unaccounted=0; 20 pages, 14 measured regions over 12 of them - "
    "eleven figure rows and three grids, nothing refused, so the pass needed no argument here: every "
    "region is a framed pasted chart or a ruled grid and the page-wide vector bands that wrecked "
    "papers 72 and 73 never appear; families line 2, map-or-plan-view 2, heatmap-or-contour 2, "
    "node-link-network 2, composite-panel 2, bar 1, table-grid 3; "
    "THE PAPER PRINTS NO NUMBERED TABLE AT ALL - the word 'Table' never occurs in the text layer, and "
    "all three grids take their names from a title row inside the box or from the appendix heading "
    "above it (GWP weights 3x4 with two column pairs in one closed box and a spanning title row; the "
    "top-ten ranking 10x4 of country names in four columns and no numeric column at all; the "
    "appendix equation grid 13 rows for 12 numbers because row 3 is printed twice, with the "
    "birth-rate equation arriving as '.070428-5.62ln(x)' and row 12's stack of three fractions "
    "overrunning its column); "
    "THE SUMMARY SHEET REPEATS FIGURE 6 - the p1 bitmap (COST at the foot, thirty arrows through the "
    "factor boxes into the two index sinks) is the same function map Figure 6 prints on p13, drawn "
    "again with no number, no caption and no citation, so the paper carries a second invisible copy "
    "of its central diagram where a reader is likeliest to see it; neither map has an axis, a scale "
    "or a single printed number, and their blue/orange arrow split is keyed nowhere; "
    "FIGURE 5 IS TWO MEASURED REGIONS UNDER ONE CAPTION - the (a) and (b) halves are separate pasted "
    "bitmaps of three-by-two automata snapshots (wealth left, population right, Initial / 10 Years / "
    "20 Years on the arrow between them), so two rows carry the identical caption, and the (b) "
    "subcaption prints 'Trended initial wealth distribution.' while the shared caption above calls "
    "the same seed 'biased'; "
    "captions fail three ways - the glyph runs on pp7 and p12 reach the layer with every space "
    "dropped ('Figure2: GraphofthetheoreticalincomedistributionI(x)andadjustedincomedistribution', "
    "its last token 'A(x)' pushed onto a second line) so both verbs are typed from the crops; Figure "
    "6's caption is set INSIDE a sentence, p12 ending on 'we created a map of the main factors that "
    "influence the Socioeconomic' and the page resuming under the caption 'and Ecological Indices of "
    "Zambia.'; and Figure 4's caption welds its two panels into one run-on line with no space "
    "between the subscript and the panel letter 'B:'; "
    "Figure 2 is the paper's one chart with no y axis at all - two smooth curves named by boxed "
    "annotations inside the plot, red 'Theoretical Income Distribution I(x)' and blue 'Adjusted "
    "Income Distribution (1-x)I(x)' which the caption calls 'A(x)'; Figures 1 and 3 are the same "
    "world choropleth in the same five-step ramp keyed inside the lower left with the words Low and "
    "High and no numbers, and both leave their no-data countries white while the prose says they are "
    "coloured grey; Figure 7 is the honest one (three marked curves against a labelled investment "
    "axis, inside legend in the Greek alpha, vertical rule at the 1.2 billion budget); Figure 8 puts "
    "six legend entries over seven groups of paired bars, prints each alpha twice so solid against "
    "hatched is the only cue for first decade against second, and keys its hatched 0.5 with a blue "
    "swatch over pink bars; Figure 9 promises panels that are 'respectively' D_i, E_i and S but "
    "carries no panel letters, no axis titles and no y numbers at all, and its middle panel is "
    "scaled differently from its neighbours; "
    "citation is the weakest block - four of the nine numbered figures (1, 2, 3, 8) are never named "
    "in prose, Figures 4, 7 and 9 get one or two pointers on their own pages, Figure 5 two, and "
    "Figure 6 is named twice but both times away from the art, once on p14 with lead_pages -1 and "
    "once on p20 from the appendix; the grids are cited only as 'the table' and 'the above table') |"
)

claims = LANE / "CLAIMS.md"
lines = claims.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("| 85 | P-D-2015-34985-c7be0d8b |"):
        continue
    out.append(line)
out.append(ROW)
claims.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

recovery = LANE / "CLAIMS-rows-mcm-9a.md"
keep = [l for l in recovery.read_text(encoding="utf-8").splitlines()
        if not l.startswith("| 85 | P-D-2015-34985-c7be0d8b |")]
keep.append(ROW)
recovery.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")

readme_row = (
    "| 85 | P-D-2015-34985-c7be0d8b | 20 | 14 | 11 | 3 | closed, `check.py` layout identical, "
    "unaccounted 0; 14 measured regions over 12 of 20 pages = 11 figure rows + 3 grids, nothing "
    "refused, because every region is a framed chart or a ruled grid and this paper has none of the "
    "page-wide prose bands that broke 72 and 73; no numbered table exists - 'Table' never appears in "
    "the text layer and all three grids are named by an in-grid title row or the appendix heading; "
    "the summary sheet repeats Figure 6's function map unnumbered and uncited; Figure 5 is two "
    "regions under one caption, its (b) half subcaptioned 'Trended' while the caption calls the seed "
    "'biased'; caption glyph runs lose every space on pp7 and p12 so those two verbs are typed from "
    "the crops; Figure 2 has no y axis at all, Figure 8 prints each alpha twice with a mismatched "
    "swatch, Figure 9 has no axis titles or y numbers, and Figures 1 and 3 key their classes with "
    "'Low'/'High' and no numbers; four of nine figures never cited |\n"
)

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
idx = next(i for i, l in enumerate(rows) if l.startswith("| 121 |"))
rows.insert(idx, readme_row.rstrip("\n"))
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")

print("claims rows", len(out), "readme inserted at", idx)
