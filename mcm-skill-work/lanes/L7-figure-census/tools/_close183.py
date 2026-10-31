"""Close paper 183 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-E-2019-1903455-a52f7980"

ROW = (
    "| 183 | P-E-2019-1903455-a52f7980 | mcm-9a | closed 2026-10-25 sha a52f7980 "
    "layout 3bfacc238768dc8c (figures=15 tables=7 excluded=25 unaccounted=0; 25 pages, 47 measured "
    "regions, twenty-two exhibits resolving into fifteen figure rows and seven table rows; "
    "TWENTY-FIVE REGIONS ARE ONE ADVERTISER'S BANNER - a 678-path vector block at y=767-839 printing "
    "关注数学模型 2 MATHmodels 获取更多资讯 at the foot of every page, refused page by page rather "
    "than collapsed; Table 1 (Notations) is LIVE TEXT at the foot of p4 and is not a measured region, "
    "so it is not censused; THE WEIGHT GRID PRINTS TWO NORMALISATIONS AND NO PAGE RECONCILES THEM - "
    "Table 2's four band weights sum to exactly 1.0000 and its eleven leaf weights also sum to "
    "exactly 1.0000, while every band total fails its own sub-rows (provisioning 0.2591 against "
    "0.2806, regulating 0.2647 against 0.2989, biotope 0.1900 against 0.1975, cultural 0.2862 against "
    "0.2230), the distinction between the two scales is carried by cell shading rather than a column "
    "label, and the ESI formula multiplies W1 to W4 by the four class indices without saying which "
    "scale W1 to W4 belong to; THE PROSE QUOTES ONE CLASSIFICATION STANDARD AND FIGURE 3 PRINTS FIVE "
    "- p10 fixes 29.45 and 68.37 as the only thresholds while the plate carries per-row cut points "
    "(25.2/57.92, 47.34/69.04, 35.6/68.12, 24.89/55.63) and only the aggregate row uses the quoted "
    "pair, which is neither a total of the four below it nor on their boundaries; THE PANEL PAIRS ARE "
    "ONE MODEL ON TWO ORIGINS - Figure 6(a) truncates its ordinate at 2 while 6(b) starts at 0, so "
    "the comparison the pair exists to make cannot be read across it, and Figure 7's panels disagree "
    "in shape (a parabola peaking near 13.5 at 2013 against a near-straight rise to about 6) while "
    "the paragraph reading them cites 'Figure.8(a)' for what is Figure 7's left panel; ONE FIGURE "
    "RENAMES ITS OWN SERIES - Figure 7(a) keys the data 'Income-cost ratio vs. Year' on axes labelled "
    "benefit-cost ratio and panel (b) keys the same quantity 'Benefit vs. Year'; THE FITS CANNOT "
    "GENERATE THE SERIES - Table 5 fits B = a exp(b dt) + c with b positive for all four projects, so "
    "each benefit grows without bound, while Table 4 and all three appendix grids run the "
    "non-sustainable series to exactly zero at a printed year (2033, 2028, 2020, 2056), dt is defined "
    "nowhere, no R2 or n is printed, and PD's amplitude 11.98 is a seventh of its siblings'; THE "
    "APPENDIX GRIDS ARE THE PAPER'S ONE CHECKABLE DEVICE AND THEIR CHECKS PASS - in every one of the "
    "four nine-column grids the maximum stands where 'Highest' prints, every arrow matches its step's "
    "sign, and the two series meet exactly where 'Intersection' stands - but their annotation rows "
    "break every decimal column, the final value prints as bare '0', the arrow glyphs are keyed "
    "nowhere, the corner cell reads 'Year', the metric is BCR in Table 4 and ICR in all three "
    "appendices, and Appendix 3's opening pair for PD (N 1.06, Y 0.73) is Table 4's opening pair for "
    "PA digit for digit; FIGURE 9 IS FAITHFUL AND FIGURE 10 IS DECORATION - the four 3-D pies print "
    "71/29, 67/33, 91/9 and 54/46 and the sentence quoting 91% names the PC panel, while Figure 10 is "
    "six clip-art icons with the mouse cursors still in the screenshot, no link of any kind drawn "
    "between them, and a seventh unlabelled icon beside the centre disc; Figure 1 lays out a pipeline "
    "of EWM/CVM, ESM index, HC, SVM, SDF and cost-benefit that no later plate returns to; families "
    "line 6, table-grid 7, scatter 3, flowchart-or-schematic 2, bar 2, other 2) |"
)

READ = (
    "| 183 | P-E-2019-1903455-a52f7980 | 25 | 47 | 15 | 7 | closed, `check.py` layout identical, "
    "unaccounted 0; 47 measured regions, 22 exhibits and 25 refusals - the same 678-path advertiser "
    "banner at the foot of all 25 pages; Table 1 is live text on p4 and not censused; Table 2's band "
    "weights sum to 1.0000 and its leaf weights sum to 1.0000 with every band total failing its own "
    "sub-rows; p10 quotes one threshold pair while Figure 3 prints five; Figure 6(a) truncates its "
    "ordinate at 2 against 6(b)'s 0; p15 cites 'Figure.8(a)' for Figure 7's left panel; Table 5's "
    "positive exponents cannot produce Table 4's and the appendices' series, which land on exact "
    "zero; all four nine-column grids pass their internal checks but print bare '0', unkeyed arrows "
    "and 'Year' in the corner cell, and Appendix 3 copies PA's 1995 pair into PD; Figure 10 is a "
    "screenshot with cursor artefacts still in it |"
)

prefix = f"| 183 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 183 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
