"""Evidence pass for P-B-2018-73410-069a3764: caption strings, counts, citations, places."""

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))
import schema  # noqa: E402

PID = "P-B-2018-73410-069a3764"
RAW = (LANE / ".proxy" / f"{PID}-pages.txt").read_text(encoding="utf-8")
PAGES: dict[int, str] = {}
for block in RAW.split("=== page ")[1:]:
    num, _, body = block.partition("\n")
    PAGES[int(num)] = body

CTX = json.loads((LANE / ".proxy" / f"{PID}-ctx.json").read_text(encoding="utf-8"))
out: list[str] = []

CAPS = [
    ("F1", 5, "Figure 1: Transition Between Different Groups with Only Two Languages"),
    ("F2", 7, None),
    ("T1", 9, "Table 1: Projections for Population Statistics of Major Languages in 2017"),
    ("F3", 12, "Figure 3: Example Graph of Transition Between Different Groups in a Bilingual Model"),
    ("F4", 15, "Figure 4: Graph of Population of Top Five Language Groups in the Next Fifty Years"),
    ("T2", 15, None),
    ("F5", 16, None),
    ("F6", 16, None),
    ("F7", 17, None),
    ("F8", 18, None),
    ("T3", 25, None),
    ("T4", 25, "Table 4: Birth Rate and Death Rate of Major Language Groups"),
    ("T5", 25, None),
    ("T6", 26, None),
    ("T7", 26, None),
    ("T8", 26, "Table 8: Economic Outlook for the Next Fifty Years"),
    ("F9", 27, "Figure 9: Graph of Birth Rate in the Next Fifty Years"),
    ("F10", 27, None),
    ("F11", 27, None),
    ("F12", 28, None),
]

out.append("== caption candidates (raw repr windows)")
for tag, page, seen in CAPS:
    label = f"Figure {tag[1:]}" if tag.startswith("F") else f"Table {tag[1:]}"
    body = PAGES.get(page, "")
    found = []
    for p in (page - 1, page, page + 1):
        text = PAGES.get(p, "")
        for m in re.finditer(re.escape(label) + r"\s*:", text):
            s = max(0, m.start() - 40)
            found.append((p, repr(text[s:m.start() + 260])))
    out.append(f"-- {tag} p{page} {label}")
    for p, snippet in found:
        out.append(f"   p{p} {snippet}")

out.append("")
out.append("== body-only citation counts")
for tag, page, _ in CAPS:
    label = f"Figure {tag[1:]}" if tag.startswith("F") else f"Table {tag[1:]}"
    total = 0
    where = []
    for p, text in PAGES.items():
        for m in re.finditer(re.escape(label) + r"(?![\d])", text):
            line = text[max(0, m.start() - 80):m.start() + 80].replace("\n", " ")
            if re.match(re.escape(label) + r"\s*:", text[m.start():]):
                continue
            if "精品数模" in line:
                continue
            total += 1
            where.append(p)
    out.append(f"{tag} {label}: count={total} pages={sorted(set(where))}")

out.append("")
out.append("== headings for path probes")
for h in CTX["headings"]:
    out.append(f"  p{h['page']:>2} {h['title']!r} [{h['kind']}]")

out.append("")
out.append("== place probes")
PATHS = {
    "P_INTRO": ["1 Introduction"],
    "P_SYM": ["2 Preliminary Model", "2.1 Notations and Symbol Description",
              "2.1.1 Symbol Description"],
    "P_231": ["2 Preliminary Model", "2.3 Analysis of the Problem", "2.3.1 N=2 Model"],
    "P_24": ["2 Preliminary Model", "2.4 Calculating and Simplifying the Model"],
    "P_25": ["2 Preliminary Model", "2.5 The Model Results"],
    "P_31": ["3 Modified Model", "3.1 Notations and Symbool Description",
             "3.1.2 Additional Symbol Description"],
    "P_33": ["3 Modified Model", "3.3 Analysis of the Problem"],
    "P_351": ["3 Modified Model", "3.5 The Model Results",
              "3.5.1 Graph of Population of Different Language Groups"],
    "P_352": ["3 Modified Model", "3.5 The Model Results",
              "3.5.2 Graph of the Scale of Migration"],
    "P_353": ["3 Modified Model", "3.5 The Model Results",
              "3.5.3 Distribution of Non-native English Speakers"],
    "P_361": ["3 Modified Model", "3.6 Sensitivity Analysis", "3.6.1 High Uniformity Scenario"],
    "P_362": ["3 Modified Model", "3.6 Sensitivity Analysis", "3.6.2 Low Uniformity Scenario"],
    "P_42": ["4 Application of Our Model", "4.2 Symbol Descrption"],
    "P_431": ["4 Application of Our Model", "4.3 Calculating and Simplifying",
              "4.3.1 The Year of 2017"],
    "P_432": ["4 Application of Our Model", "4.3 Calculating and Simplifying",
              "4.3.2 The Year of 2067"],
    "P_MEMO": ["6 Memo"],
    "P_APPA": ["References"],
}
for name, path in PATHS.items():
    try:
        schema.check_place({"section_path": path, "section_numbered": True}, PID)
        out.append(f"{name}: OK")
    except Exception as exc:  # noqa: BLE001
        out.append(f"{name}: FAIL {exc}")

dest = LANE / ".proxy" / f"{PID}-evidence.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest)
