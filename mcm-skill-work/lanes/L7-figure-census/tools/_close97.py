"""Close paper 97 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2016-48573-960f7126"

ROW = (
    "| 97 | P-B-2016-48573-960f7126 | mcm-9a | closed 2026-10-24 sha 960f7126fce7260b "
    "layout 40637cb3603fcd2f (figures=12 tables=1 excluded=0 unaccounted=0; 30 pages, 13 measured "
    "regions over 13 of them, resolving into TWELVE FIGURE ROWS, ONE TABLE ROW and NO EXCLUSION - "
    "but the paper prints FOUR tables' worth of grid and fig_extract boxed only one, so the RI "
    "coincidence scale on p22, the AHP score table on p23 and the ranking table inside the executive "
    "summary on p29 are declared gaps with no row; THE PAIR CARRYING THE RESULT IS DRAWN ON TWO "
    "RULERS - Figures 3, 5, 7 and 8 are one MATLAB template (Sh, Sl, D over Time 0-150, left axis "
    "'Spacecraft Number x 10^3' 0-4) that prints FOUR different debris axes, 0-4e4 with a second "
    "floating 'x 10^4' above the frame on Figure 3, 0-2e6 on Figure 5, 0-600x10^3 on Figure 7 and "
    "0-16000x10^3 on Figure 8, and not one of them assigns a curve to an axis, so with-ODR against "
    "without-ODR is compared across spans that differ fiftyfold; Figure 8's paragraph reads its "
    "year-60 debris as '168 thousand' while the magenta curve sits near two units of a thousand-scaled "
    "tick, so the printed axis and the printed prose cannot both be right; THE DIAGRAMS STATE A "
    "SYMBOL THE EQUATIONS DO NOT - Figure 4 and Figure 6 label their satellite-loss edges minus "
    "theta(l) D Sl while the ODE system printed on the same page as Figure 4 writes dSl/dt = -beta(l) "
    "D Sl + alpha(l) - gamma(l), only the cleaner edge -delta W D agreeing, and both drop four of the "
    "system's five terms while clipping their outer nodes against the frame edges; THE BETA PAIR IS "
    "THINNEST OF ALL - Figures 9 and 10 plot four satellite curves and NO debris curve although the "
    "collision rate is the parameter under test, spell one word two ways inside one legend "
    "('SH(Original Beta)' against 'SL(Origin Beta)'), run 0-1.6 where every neighbour runs 0-4, sit a "
    "page's height apart on the same sheet keyed only by a sentence that names no number, and Figure "
    "9 is INSERTED INTO THE MIDDLE OF A SENTENCE whose first half stops at the foot of p18 and whose "
    "second half resumes under the caption as 'bigger beta.'; CITATION IS TWO FIGURES - only Figures "
    "1 and 2 are named by a sentence, both on p4 with Figure 2 printing on p5, and the other ten "
    "figures plus Table 1 are pointed at only by 'A diagram can be drawn to illustrate the structure "
    "of the system', 'shown in the following figure', 'The first figure shows the result ... The "
    "second shows the result', 'is shown in the following figure'; Table 1 is the one cleanly ruled "
    "exhibit and nobody names it - three columns, booktabs rules, caption BELOW the table, five "
    "criteria stacked against four alternatives with no line relating them - and the uncaptioned "
    "grouped bar chart on p23 that carries the adopted ranking abbreviates two of those criteria away "
    "from the vocabulary Table 1 establishes ('PC' for Production Cycle, 'Life Span' for Life "
    "Expectancy) with no axis title, no value label and no title in the frame; families line 7, "
    "node-link-network 2, bar 1, photo-or-raster-image 1, surface-or-3D 1, table-grid 1) |"
)

READ = (
    "| 97 | P-B-2016-48573-960f7126 | 30 | 13 | 12 | 1 | closed, `check.py` layout identical, "
    "unaccounted 0; 13 measured regions over 13 of 30 pages resolving into 12 figure rows and 1 "
    "table, no exclusion, while three further printed tables (p22 RI scale, p23 score table, p29 "
    "ranking table in the executive summary) carry no measured region and are declared gaps; the "
    "four population figures of one MATLAB template print four different debris axes and none "
    "assigns a curve to an axis, so the with-ODR/without-ODR comparison spans fiftyfold different "
    "rulers; the two node-link diagrams label their loss edges theta where the ODE system on the same "
    "page writes beta; the beta pair plots no debris curve at all, misspells its own legend, and "
    "Figure 9 is inserted into the middle of a sentence; only Figures 1 and 2 are ever named; the one "
    "cleanly ruled table is uncited and the uncaptioned bar chart that carries the ranking abbreviates "
    "its own criteria |"
)

prefix = f"| 97 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 97 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
