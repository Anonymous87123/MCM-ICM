"""Close paper 182 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-E-2019-1902917-3fb00373"

ROW = (
    "| 182 | P-E-2019-1902917-3fb00373 | mcm-9a | closed 2026-10-24 sha 3fb00373 "
    "layout 48f0cf414772fc42 (figures=9 tables=3 excluded=4 unaccounted=0; 24 pages, 16 measured "
    "regions over 11 of them resolving into nine figure rows, three table rows and four refusals - the "
    "notation grid's body p5, Figures 1-3 as hand-drawn AHP trees, Table 2's band grid, Table 3's scored "
    "grid, Figure 4's MATLAB plot, and five pasted screenshots in the appendix; FOUR REGIONS ARE PAGE "
    "FURNITURE, refused not censused - three running headers and the References block on p21, plus "
    "Table 2's own overflow; THREE SYMBOL SYSTEMS DESCRIBE THE SAME TWO SUMS - the notation grid defines "
    "CS, PC and EC, the body writes CS = PC + EC and B_S = sum B_t/(1+r)^t + B21 + B22, and the three "
    "tree plates use C, C1, C2, C12, C21-C25, B, B1, B2, B12, with index 11 SKIPPED IN BOTH TREES (C1's "
    "only child is C12, B1's is B12); THE ONE ARITHMETIC RESULT STANDS ON NOTHING THE PAPER PRINTS - p16 "
    "gives the cost score as G1 = pw0 = 372 while p = (5,5,7,1,3,5) against w0 = (1/2, 5/42, 1/14, "
    "5/42, 1/21, 1/7) gives 4.571, and the sensitivity section fits the same score at 0.858a+4.142, so "
    "372 is forty to eighty times every scale in the paper; TABLE 3 CONTRADICTS TABLE 2 IN THE ROW "
    "DIRECTLY ABOVE ITS MIRROR - soil quality's 0.1 is scored rank 5 although Table 2's soil bands step "
    "0.3/0.2/0.1, while water quality's identical 0.1 is scored rank 4, and the other four rows and the "
    "capital row (4,120/3,000 = 1.373 AC) do follow the bands; TABLE 2 IS SPLIT ACROSS PAGES - bands 4 "
    "and 5 fall on p12 under the running header with no repeated header, so the grid carries continued "
    "and the overflow is refused as split-across-pages; THE APPENDIX IS SOMEONE ELSE'S BOOK - five of "
    "the nine figure rows are screenshots of a printed Chinese textbook (a TVA road map captioned only "
    "by a pasted 'May 2005 map of TVA sites' strip, a construction-cost table titled 表 3-2 with the "
    "utility mistyped 'TWA' and its last three plants on the next page with two unexplained em dashes, "
    "and a revenue table for 1947-1957 continued out of order as 1966-1958 with two rows struck through "
    "and one blank cell), none carrying a figure number, a caption in the paper's language or a unit, "
    "and the revenue table's only identity fails by exactly 100 at 1953 and by TEN MILLION at 1952 "
    "(85,004,390 printed for 95,004,390); FIGURE 4 PROVES ITS OWN TAUTOLOGY - its two fitted functions "
    "0.295a+4.705 and 0.858a+4.142 both reduce to exactly 5.0 at a = 1, so the 'converge to 5' the "
    "text reads off the plate was imposed at fitting time; POINTERS ARE WRITTEN WITHOUT A SPACE - "
    "'Figure.1', 'Figure.2', 'Figure.3', 'Figure.4', 'Table2', 'Tab.2' - and seven of the twelve "
    "exhibits are named by no sentence at all; the MATLAB listing the paper introduces as 'These are "
    "Matlab codes' is live text on pp23-24 and is not a measured region, so it is not in the census; "
    "the map's legend swatches (red/purple/orange) do not match its own red/yellow markers and the "
    "plate is singular in its lead-in while covering seven states; families table-as-figure 4, "
    "flowchart-or-schematic 3, line 1, map-or-plan-view 1, table-grid 3) |"
)

READ = (
    "| 182 | P-E-2019-1902917-3fb00373 | 24 | 16 | 9 | 3 | closed, `check.py` layout identical, "
    "unaccounted 0; 16 measured regions over 11 of 24 pages resolving into 9 figure rows, 3 table rows "
    "and 4 refusals (three running headers, the References block, and Table 2's overflow); three symbol "
    "systems for two sums (CS/PC/EC, C/C1/C2/C12, B/B1/B2/B12) with index 11 skipped in both trees; p16 "
    "prints G1 = pw0 = 372 where the printed p and w0 give 4.571; Table 3 scores soil's 0.1 as rank 5 "
    "while water's identical 0.1 is rank 4 against Table 2's bands; Table 2 splits across pp11-12 with "
    "no repeated header; five appendix rows are screenshots of a Chinese textbook with no figure "
    "numbers, and the revenue table's total misses its row sum by ten million at 1952 |"
)

prefix = f"| 182 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 182 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
