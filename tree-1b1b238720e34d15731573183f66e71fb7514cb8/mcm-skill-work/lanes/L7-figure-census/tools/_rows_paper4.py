"""One-off: assemble paper 4 coder rows into the merged payload file.

This paper typesets every display equation as vector paths, so nine of the eighteen
measured regions are equations rather than exhibits. They are recorded as excluded
with reason not-an-exhibit, not silently dropped.
"""

import json
from pathlib import Path

P = Path("lanes/L7-figure-census/.proxy")

# page, region, family, confidence, panels, is_table, caption, excluded, other_note, note
ROWS = [
    (6, 1, "flowchart-or-schematic", "medium", 1, False, "Figure 1", "", "",
     "hand-drawn bat profile with upward force arrows, pivot and direction labels"),
    (6, 2, "flowchart-or-schematic", "medium", 1, False, "Figure 2", "", "",
     "bat outline with curved rotation arrow and Center of Mass label"),
    (7, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "three inline momentum, energy and restitution equations in an indented list"),
    (8, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "display equation for b, Brody power equation"),
    (9, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "display equation for final velocity vf with a bracketed fraction"),
    (9, 2, "line", "high", 1, False,
     "Graph A: Final Speeds at Given Distance from Pivot", "", "",
     "single curve of final speed versus distance b, title inside the axes"),
    (9, 3, "", "high", 1, False, "", "not-an-exhibit", "",
     "display equation, derivative of vf set to zero"),
    (10, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "quadratic-formula display equation solving for b"),
    (10, 2, "", "high", 1, False, "", "not-an-exhibit", "",
     "display equation substituting numeric values for b"),
    (12, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "single display equation for the final ball velocity vf"),
    (13, 1, "", "high", 1, False, "", "not-an-exhibit", "",
     "numbered display equation, Equation 3, for vf"),
    (15, 1, "flowchart-or-schematic", "medium", 1, False, "Figure 3", "", "",
     "three ellipses linked by arrows showing quadrupole deformation stages"),
    (17, 1, "surface-or-3D", "high", 1, False,
     "Graph B: Sweet Spot due to Initial Velocities", "", "",
     "wireframe 3D surface with a shaded sweet-spot patch on top"),
    (17, 2, "", "high", 1, False, "", "not-an-exhibit", "",
     "display equation for final velocity vf with nested fractions"),
    (18, 1, "line", "high", 1, False, "Graph C: Final Speed vs. Bat Mass", "", "",
     "single rising straight line, final speed against bat mass"),
    (18, 2, "line", "high", 1, False, "Graph D: Final Speed vs. Initial Bat Velocity", "", "",
     "single rising straight line, final speed against initial bat velocity"),
    (19, 1, "line", "high", 1, False, "Graph E: Final Speed vs. Moment of Inertia", "", "",
     "single rising straight line, final speed against moment of inertia"),
    (20, 1, "line", "high", 1, False, "Graph F: Final Speed vs. Initial Ball Velocity", "", "",
     "single rising straight line, final speed against initial ball velocity"),
]


def main() -> None:
    out = []
    for page, region, family, conf, panels, table, caption, excluded, other, note in ROWS:
        out.append({
            "page": page, "region": region, "family": family, "confidence": conf,
            "panel_count": panels, "table": table, "caption_verbatim": caption,
            "caption_source": "text-layer" if caption else "none",
            "excluded": excluded or None, "other_note": other or None, "note": note,
        })
    path = P / "P-A-2010-7920-06d31c2b-rows-merged.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rows {len(out)} -> {path}")


if __name__ == "__main__":
    main()
