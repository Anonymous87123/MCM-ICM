"""Rewrite the CLAIMS rows for papers 73 and 82 in the ledger's own column format."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]

C73 = (
    "| 73 | P-A-2015-35532-1a9fa997 | mcm-9a | closed 2026-10-24 sha 05c683bca13d559f "
    "(figures=15 tables=13 excluded=31 unaccounted=0; 34 pages, 59 measured regions over 27 of them, all accounted - "
    "28 exhibit rows (13 numbered figures, the two uncaptioned delivery-plan bands, 13 tables) and 31 refusals, nothing unresolved; "
    "families line 9, table-grid 13, flowchart-or-schematic 2, map-or-plan-view 2, composite-panel 2; "
    "THE DETECTOR DEFECT THAT SHAPES THIS PAPER IS NEW TO THE LANE - the PDF draws a thin rule round every individual line of type, "
    "so prose and display equations arrive as page-wide vector regions and the running-head rule at y=65.5 drags each box out to the "
    "full 415.4 pt measure; the white-fill discriminator used on paper 72 returns nothing usable and area buys nothing either, since a "
    "prose band reaches 0.59 of the page while the p27 delivery band holding four exhibits reaches only 0.21, so every rejection was "
    "made by eye on the render and the eight not-an-exhibit rows are prose with the page-top rule as their only drawn mark; "
    "every pasted plot is framed by vector rules after pasting, so container and content are two regions - where the frame holds one "
    "plot the frame is the row and the inner raster is refused fragment-of-other, but on p8 one frame holds three separately numbered "
    "plots so the three rasters are the rows and the frame is refused as the band carrying their caption strips; seventeen regions of "
    "pasted bitmap are not exhibits in their own right; "
    "tables collide on shared boxes - Table 6 shares p22's measured box with Table 5, so nine printed tables book as eight rows plus "
    "one shared box, the same class as paper 72; the three symbol lists run to five slices across pp2-4 with the header printed only "
    "twice and the slices disagree with themselves (the open-degree row is defined twice in a row on p4 with C_n repeating F_n's own "
    "wording, G(t) wraps onto a second line, three definitions are cut mid-sentence); Table 5's header disagrees with its own body "
    "('current disease situation' over 2917, 'Population density' over 45.5); Table 4's unit note stops at 'People /per km' after item "
    "1 of four; in Table 2 distances break across two lines inside their cell so 227 prints as '22' over '7' and 309 as '30' over '9', "
    "and the row labelled Mattrujong sits on the diagonal that belongs to Bonthe; Table 9's header reads 'The days use / to control' "
    "and never names its last column, its cells mix bare counts with bracketed percentages, and the sentence after it cites 'Table 2' "
    "instead of Table 9; Table 8's last row reports a death case of 119556 against an initial value an order of magnitude smaller and "
    "its caption baseline is struck through by the top rule of its own grid; "
    "the delivery plan is the quietest failure - six monthly plans announced by one sentence and none numbered, two plots and two grids "
    "on p27, four of each on p28, every grid 3 rows by 4 columns with 'Sierra Leone' wrapping onto a second line and 'Leone' colliding "
    "with the bottom rule at the lower left of p28, every header broken mid-word as 'Infect' over 'ed' over 'case', and no scale, "
    "legend or unit on either plot; "
    "Fig.5's two panels map the same colour to opposite cases, so 'with drug' is the blue curve on one panel and the green curve on the "
    "other and nothing on the page resolves it; Fig.6's choropleth encodes nothing - twelve districts, one flat pink fill - so it is a "
    "key to names and shapes only and its caption ends in a dangling 'Source:'; Fig.7 reuses that fill and collides its district names "
    "with seven red star markers; Fig.1 draws four compartments S, E, I, R while the text beside it says the infectious die to D, so the "
    "cartoon has no D; Fig.8's y ticks are rotated unreadably, Fig.9's 'Beta' label is cut off and its caption has lost its title, "
    "Fig.10's caption survives only as 'creases, and death cases increases', and Fig.11's only label is a bare 'Fig.11' with no title; "
    "citation is thin - 16 of 28 exhibit rows named in prose, each exactly once, 12 never named (the three p8 plots, the two delivery "
    "bands, the five symbol slices, Tables 4 and 5), three citations point backwards across a page break and Table 3 by six pages so "
    "lead_pages is negative there, and the prose drops its own pointer twice ('shown in Table' for Table 6, 'shown Table 3' for Table 3); "
    "the heading pass missed 'Model I' on p5, 'Model II' on p13 and 'Results & analysis' on p25 and invented a heading '2 December' out "
    "of a date in the data prose, so the recorded paths use the printed lines; three captions print with no space after their number "
    "('Fig.2.1the early EBOV transmission period of Guinea', 'Table4:the data of the different district', 'Table 9 The days use') and "
    "the caption vocabulary has no unspaced form, so the nearest form is recorded and the printing described on each row) |"
)

C82 = (
    "| 82 | P-C-2015-35778-39d71af2 | mcm-9a | closed 2026-10-24 sha 90f842165e0c484d "
    "(figures=21 tables=1 excluded=1 unaccounted=0; 22 pages, 23 measured regions on 13 of them - 21 figure rows, one grid and the p1 "
    "title sheet excluded as not-an-exhibit; families line 13, flowchart-or-schematic 3, node-link-network 3, scatter 2, bar 1, "
    "table-grid 1; Figure 1 is captioned a 'distribution structure' and drawn as an organigram and Figure 13 is captioned a 'diagram' "
    "and drawn as 100 isolated points, so both families follow the pixels; Figures 7 and 8 are ten simulation runs per month stacked in "
    "a perspective box with no depth axis, no depth tick and no key; "
    "THE SECOND PANEL OF EVERY CAPTION PAIR WEARS THE FIRST PANEL'S RATE - Figure 12 prints 'enthusiasim when churn rate=25%' under a "
    "caption promising 35% and Figure 14 prints 'benefit per month when churn rate=25%' the same way, and each pair is also drawn on "
    "different windows (0.70-0.86 against 0.65-0.80, 165-195 against 145-185), so the churn comparison fails by label and by shape; "
    "'enthusiasim' and 'Tme/month' are printed misspellings kept verbatim; Figures 17 and 18 are captioned '... of two recruitment' and "
    "stop before the word 'methods'; four captions are typed-from-crop because the p14 and p15 pairs weld two labels onto one printed "
    "line and drop the percentages to a second line; every caption glyph run on pp6-20 has no space glyph in the embedded subset, so "
    "the layer reads 'Figure1: Staffdistributionstructureineachdivision' and every vector axis title arrives reversed ('%52=etar'), "
    "which is why all caption and axis readings came off proxies; Table 1 is the only grid, three full-width rules at 471.5, 490.6 and "
    "550.5 pt across 454.8 pt with no vertical and four numeric columns right-aligned to the cell edge, and the heading index files it "
    "under '4 Sensitivity Analysis' which prints at 707.7 pt below the grid, so the row is placed under 3.2 by hand, while both p20 "
    "figures are filed under '5 Conclusion' at 701.7 pt although they print under 4.1 at 72.3 pt; citation is complete and flat - all "
    "22 exhibits named, 18 exactly once on their own page, Figure 2 twice, Figure 19 twice on p18 and p19, only Figure 16 read a page "
    "after the art, with the body spelling 'Figure.4' and the caption spelling 'Figure 4:' never meeting) |"
)

claims = LANE / "CLAIMS.md"
lines = claims.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("| 73 | P-A-2015-35532-1a9fa997 |"):
        out.append(C73)
        continue
    if line.startswith("| 82 | P-C-2015-35778-39d71af2 |"):
        continue
    out.append(line)
out.append(C82)
claims.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

recovery = LANE / "CLAIMS-rows-mcm-9a.md"
keep = [
    line
    for line in recovery.read_text(encoding="utf-8").splitlines()
    if not line.startswith("| 73 | P-A-2015-35532-1a9fa997 |")
    and not line.startswith("| 82 | P-C-2015-35778-39d71af2 |")
]
keep += [C73, C82]
recovery.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")

print("claims rows", len(out))
print("row73 in claims", sum(line.startswith("| 73 | P-A-2015-35532-1a9fa997 | mcm-9a | closed") for line in out))
print("row82 in claims", sum(line.startswith("| 82 | P-C-2015-35778-39d71af2 | mcm-9a | closed") for line in out))
