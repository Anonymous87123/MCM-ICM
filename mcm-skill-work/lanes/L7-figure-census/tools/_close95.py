"""Close paper 95 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2016-54164-57a2b533"

ROW = (
    "| 95 | P-A-2016-54164-57a2b533 | mcm-9a | closed 2026-10-24 sha 2a0211e17c37cbc1 "
    "layout c7f1436449189cc4 (figures=35 tables=0 excluded=0 unaccounted=0; 44 pages, 35 measured "
    "regions over 32 of them, resolving into THIRTY-FIVE FIGURE ROWS with NO TABLE AND NO EXCLUSION - "
    "the paper prints no table of any kind; THIRTY-ONE OF THE THIRTY-FIVE EXHIBITS PRINT NO CAPTION "
    "AND NO NUMBER, the four that do being Figures 1 to 4, three of which are the closing product "
    "pictures, so the only captioned exhibit in the body chapters is a cartoon of hands swirling the "
    "bath water; the twenty-one uncaptioned spreadsheet and MATLAB screenshots keep whatever title "
    "the plotting program drew inside its own frame and the eight Inventor renders carry no label at "
    "all, each identified only by the dimension paragraph on the FOLLOWING page; SECTION 5 IS ONE "
    "TEMPLATE RUN EIGHT TIMES - seven alternative tub designs each get an unlabelled render alone on "
    "one page and a deviance-against-flow-rate chart on the next, sharing abscissa 'Flow Rate (GPM)' "
    "1.0 to 16.0, a unitless 'Deviance' ordinate whose limits swing from 2-32 (square tub) to 1000-4000 "
    "(fiberglass) and an unframed outside-left legend of 'Bathtub' and 'Minimum' - AND THE STANDARD "
    "TUB'S CHART IS PRINTED TWICE, on p16 as 4.3.1's flow-rate selection and again on p20 as 5.1's "
    "first case, identical title 'Optimal Flow Rate (SA: 1800, V: 25200)' and identical curve; NO "
    "MINIMUM POINT IS VISIBLE IN ANY OF THE EIGHT CHARTS although the text sends the reader to 'the "
    "point indicated at the bottom of the graph, at (1.81, 10.179381314125882)' - the appendix code "
    "appends it as a single point at the curve's floor, which in three of the eight charts lies below "
    "the frame's lowest tick; THE FOUR K REGRESSIONS ON PP12-14 ARE THE SAME FOUR POINTS PLOTTED "
    "FOUR TIMES against V^2/SA^3, its square, its square root and its cube root, with R squared "
    "0.99764, 0.996529, 0.999294 and 0.999299 inside the frames, and the adopted fit is reported in "
    "the body as 'R2 = 0.99929854436231100000' - twenty significant digits from four points; TWO "
    "DEFECTS CHANGE WHAT THE EXHIBITS SAY - p10's fit labels print 'Y = 77e^-0.029x' with the "
    "asymptote constant missing while equations (8)-(10) all read 'y = 77e^-knx + 23', and p11's "
    "second plot is the SAME experiment after the offset was subtracted (37 degree bath water "
    "appearing at 16 degrees) still against a 'Temperature [degrees Celsius]' axis under the "
    "identical title, the constant restored as +21 in equation (24) rather than the beakers' +23; "
    "citation is the thinnest in the lane - ONLY FIGURE 1 IS EVER NAMED, on the abstract page five "
    "pages before it prints ('as shown in Figure 1'), Figures 2, 3 and 4 are never named, and the "
    "other thirty-one are pointed at only by bare phrases that name no figure; families line 16, "
    "surface-or-3D 8, scatter 7, photo-or-raster-image 3, flowchart-or-schematic 1) |"
)

READ = (
    "| 95 | P-A-2016-54164-57a2b533 | 44 | 35 | 35 | 0 | closed, `check.py` layout identical, "
    "unaccounted 0; 35 measured regions over 32 of 44 pages resolving into 35 figure rows with no "
    "table and no exclusion, because the paper prints no table at all; 31 of the 35 exhibits print no "
    "caption and no number and only Figure 1 is ever named, on the abstract page five pages before it "
    "prints; section 5 runs one template eight times (render alone on one page, deviance chart on the "
    "next) and prints the standard tub's chart twice, on p16 and p20; no minimum point is visible in "
    "any of the eight deviance charts the text tells the reader to read one from; the four k "
    "regressions are the same four points against four transforms of one predictor; p10's fit labels "
    "drop the +23 asymptote and p11 plots the offset-subtracted series on a Celsius axis under the "
    "same title |"
)

prefix = f"| 95 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 95 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
