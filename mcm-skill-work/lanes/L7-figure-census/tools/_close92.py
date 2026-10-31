"""Close paper 92 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2016-44845-998bce33"

ROW = (
    "| 92 | P-A-2016-44845-998bce33 | mcm-9a | closed 2026-10-24 sha 078aa8aaed9bf783 "
    "layout 169a3c55594b9e60 (figures=50 tables=1 excluded=2 unaccounted=0; 44 pages, 53 measured "
    "regions over 29 of them, resolving into FIFTY FIGURE ROWS, ONE TABLE AND TWO EXCLUSIONS; the "
    "paper prints thirty-five figure captions and NO table caption or table number anywhere in its "
    "forty-four pages - the one table is the unlabelled 3-column parameter grid on p11 (vertical "
    "strokes between columns, one rule under the header, twenty rows, units and bracketed citation "
    "superscripts inside cells) named only by p10's 'The following table contains the model "
    "parameters that can be altered as well as their nominal values'; FIFTEEN TWO-PANEL EXHIBITS "
    "supply thirty of the fifty rows (Figures 17 to 28, 32, 33, 34) and each row keeps its own "
    "family, so Figure 18 pairs a heat map with a line plot and Figures 32 and 33 pair a line plot "
    "with a heat map under one caption; fourteen captions are carried into a pointer sentence and "
    "twenty-one figures are named by no sentence at all, with Figure 33 the worst - p38 writes 'The "
    "same results are shown in 33 below', dropping the word Figure, so no page ever prints 'Figure "
    "33' - and four pointers (Figures 24, 31, 32, 35) sit a page before their exhibit; TWO CAPTIONS "
    "CANNOT BE QUOTED FROM THE LINEAR TEXT LAYER because the two-column wrap runs the caption's "
    "second line through the body column ('Figure 7: Graphical Illustration of the Ther- be zero, as "
    "no mass or energy can be accu- modynamic System', 'Figure 29: Illustration of Properly Tuned of "
    "the three components of a PID controller PID Controller[11]'), so both are typed from the "
    "printed block geometry, hyphen break included; the two exclusions are form lettering (p1's 'For "
    "office use only / Team Control Number 44845' control box) and logo art (p44's 'Superior "
    "Products*: Applied Mathematical Consulting Firm' letterhead), both not-an-exhibit; SECTION "
    "PLACEMENT FOLLOWS PRINTED HEADING POSITIONS, NOT THE CONTEXT DUMP, which puts p7 r1 under 3.2 "
    "(it is above that heading, so 3.1), p10 r1 under section 4 (3.2), p14 r1 under 6.1 (5.2), "
    "pp19-21 under a formula line, p31 under 8.4 (8.3) and p35 and p37 one subsection too far; "
    "EXHIBIT DEFECTS: Figure 29's raster prints a foreign label from its source ('Figure 20a. "
    "Illustration of Properly Tuned'), its abscissa is a bare 't' and its ordinate untitled; Figure "
    "16's in-plot title misspells propagation as 'Propogation'; Figure 23's panel title reads 'Varied "
    "of Diffusivity over Full Length'; Figure 28's first panel title is clipped mid-phrase; Figure 10 "
    "fills its frame with a slope whose ordinate spans 1.8 deg C; FIGURE 22 PUTS THE SAME OBJECTIVE "
    "FUNCTION ON TWO ORDINATES AT ONCE (-1.4 to -0.2 left, 0 to 8 right, both labelled 'Objective "
    "Function [deg C]') and Figures 30, 31 and 34 repeat the dual-ordinate habit; almost every "
    "comparison pair is drawn on non-common scales - Figures 19 a/b, 20 a/b, 21 a/b, 25 a/b and 26 "
    "a/b use ordinate or colour windows an order of magnitude apart, so the 'comparison' cannot be "
    "read off the page without rescaling one half, and Figures 32 b and 33 b certify uniformity with "
    "colour bars 0.0003 deg C wide; only three annotated optima (38.0425 deg C, 0.006518 kg/s) and "
    "Figure 29's borrowed gains Kp=5, Ki=3, Kd=3 print a data value on the marks; families line 31, "
    "heatmap-or-contour 16, flowchart-or-schematic 3, table-grid 1) |"
)

READ = (
    "| 92 | P-A-2016-44845-998bce33 | 44 | 53 | 50 | 1 | closed, `check.py` layout identical, "
    "unaccounted 0; 53 measured regions over 29 of 44 pages resolving into 50 figure rows, 1 table "
    "and 2 exclusions, with 35 printed captions and no table caption or table number anywhere; 15 "
    "two-panel exhibits supply 30 of the 50 rows and each row keeps its own family, so Figures 18, "
    "32 and 33 each pair a heat map with a line plot under one caption; 21 figures are named by no "
    "sentence and p38 introduces Figure 33 as 'shown in 33 below', dropping the word Figure; two "
    "captions interleaved with the body column (Figures 7 and 29) were typed from printed block "
    "geometry; Figure 29 carries a foreign 'Figure 20a.' label in its own raster; Figure 22 puts the "
    "same objective function on two ordinates at once and Figures 19-21, 25 and 26 draw their "
    "comparison pairs on non-common scales |"
)

prefix = f"| 92 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 92 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
