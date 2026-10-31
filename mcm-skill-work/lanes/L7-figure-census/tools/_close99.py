"""Close paper 99 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-C-2016-42939-5fccbebc"

ROW = (
    "| 99 | P-C-2016-42939-5fccbebc | mcm-9a | closed 2026-10-24 sha 5fccbebc "
    "layout 803560792a4e36e1 (figures=11 tables=2 excluded=1 unaccounted=0; 25 pages, 14 measured "
    "regions over 12 of them, resolving into ELEVEN FIGURE ROWS, TWO TABLE ROWS and ONE EXCLUSION - "
    "the pure-white raster on the title page - with nothing unaccounted; THE DEFINITIONS TABLE IS AN "
    "IMAGE - p9 prints the heading '1.3 Detailed Definitions & Assumptions', the sub-heading '1.3.1 "
    "Detailed Definitions:' and then a bitmap of three columns (Name, Definition, Denotation) over a "
    "header and ten body rows, so the paper's ENTIRE NOTATION (X_j, delta-X_j, Y_1j to Y_mj, F_i, "
    "beta_i, ROI_1j, fROI_1j, P_1j, ROI_j) has no text layer and no cell is machine-readable, and it "
    "is the only table in the paper with NO NUMBER AND NO CAPTION; TABLE 2 PRINTS NINE ROWS UNDER A "
    "'TOP 10' CAPTION with no tenth row on the page or the two after it, scores to EIGHT DECIMALS "
    "(79.60372162 against 79.06066895) for an index built from four 0-to-100 variables, and NO RANK "
    "COLUMN although ranking is its only content; SEVEN PRINTED TABLES CARRY NO MEASURED REGION - "
    "Table 3's post-LASSO coefficients (p14) and Tables 4 to 8's five years of investment strategy "
    "(pp19/21/22), five of them the same three-column twenty-institution layout with no rule between "
    "the two that share a page - plus the untitled institution listing that runs off the foot of the "
    "p2 letter onto p3, all declared gaps; FIGURE 4 AND FIGURE 5 ARE ONE PICTURE PRINTED TWICE - the "
    "same diamond cloud, blue GAM curve, grey ribbon, axes (0e+00 to 9e+08, 0.25 to 1.00) and in-frame "
    "title 'GAM estimation of PCTPELL vs Donation' - and Figure 5 differs only by three added glyphs "
    "(orange delta-h segment, orange tick, green delta-x/delta-f bracket) yet is NAMED BY NO SENTENCE "
    "while its caption 'Demonstration of f ROI1' is the only statement of what it illustrates; the "
    "CHOSEN SHRINKAGE IS UNREADABLE ON THE EXHIBIT THAT CHOSE IT - Figure 3's cross-validated trace is "
    "flat at about 40 from s = 0.1 to s = 1.0 with no marker at 0.6, so the prose's 'minimum between "
    "0.4-0.8. We choose 0.6' cannot be located, and Figures 2 and 3 print a page BEFORE the sentences "
    "that read them; Figure 2's top axis carries twelve unlabelled vertical rules and tick numbers 0 1 "
    "2 3 4 5 7 9 12 13 15 20 (the non-zero count, never named) and its six variable names sit OUTSIDE "
    "the frame at the right margin; FIGURE 7'S OWN ENDPOINT LIST CONTRADICTS ITSELF - both ends are "
    "called 'The minimum of deviations of all institutions', one value is written 2/4 where its mirror "
    "is 4/3, and the maximum is never named; Figure 8 is a mapping-tool SCREENSHOT with fifteen red "
    "pins, no scale bar, no graticule, no legend and NO MAGNITUDE on any pin, its callouts truncated "
    "by the tool itself ('The State University of...', 'Marion Military Instit...') and two collided "
    "into 'SUNY at FredoniaBoston', so the amounts live only in the unmeasured Table 4; THE FOUR "
    "APPENDIX PANELS ARE NOT DRAWN ON A COMMON SCALE - Figures 4, 5 and 9 run 0.00 to 1.00 on the "
    "ordinate and Figure 10 runs 0 to 60 - so the four fits the appendix exists to compare cannot be "
    "laid against each other, Figure 9's ribbon crosses BELOW ZERO for a proportion and its ordinate "
    "label collides with the 0.50 tick, and Figures 9 and 10 are named by nothing; Figure 1 is a "
    "presentation-tool pipeline whose left-margin 'Donation amount' feedback line runs the page height "
    "THROUGH the downward arrow channel and whose right-hand column re-enters from below with NO "
    "JUNCTION MARK at any crossing; Table 1 and Table 2 are FULL GRIDS (rule under the header, rule "
    "between every body row, vertical rules at both edges and between the columns) - the opposite of "
    "the booktabs shape - with captions printing ABOVE, and Table 1 is named by no sentence; CITATION "
    "IS SEVEN EXHIBITS - Figures 1, 2, 3, 4, 6, 7, 8 and Table 2, while Figures 5, 9, 10 and Table 1 "
    "are named by nothing and Figure 6 is named THREE TIMES ON ONE PAGE, more than any other exhibit; "
    "families scatter 4, line 4, flowchart-or-schematic 1, map-or-plan-view 1, table-as-figure 1, "
    "table-grid 2) |"
)

READ = (
    "| 99 | P-C-2016-42939-5fccbebc | 25 | 14 | 11 | 2 | closed, `check.py` layout identical, "
    "unaccounted 0; 14 measured regions over 12 of 25 pages resolving into 11 figure rows, 2 tables "
    "and 1 exclusion (the pure-white raster on the title page, min=max=255); the definitions table on "
    "p9 is an embedded IMAGE with no text layer, so the paper's entire notation is unreadable to any "
    "extractor and the table carries no number and no caption; Table 2 is captioned 'The Top 10 "
    "Institutions' and prints NINE rows, to eight decimals, with no rank column; seven printed tables "
    "have no measured region (Table 3 and Tables 4 to 8, plus the p2-to-p3 listing) and are declared "
    "gaps; Figures 4 and 5 are the same GAM picture, the second differing only by three annotation "
    "glyphs and named by no sentence; Figure 3's cross-validated trace is flat from s = 0.1 to 1.0 so "
    "the chosen 0.6 is not locatable, and Figures 2-3 print a page before the sentences that read "
    "them; Figure 7's endpoint list calls both ends 'the minimum' and writes 2/4 where its mirror is "
    "4/3; Figure 8 is a mapping-tool screenshot with truncated and colliding callouts and no magnitude "
    "on any pin; the four GAM panels are not on a common scale (three 0.00-1.00, one 0-60) and Figure "
    "9's ribbon crosses below zero; only seven exhibits are named by a sentence |"
)

prefix = f"| 99 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 99 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
