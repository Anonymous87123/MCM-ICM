"""Measure candidate exhibit regions in one paper.

Geometry only. Nothing here classifies a chart. Two sources are fused because these
PDFs draw most charts as vector paths, which an image-block pass misses:

  * image blocks        page.get_image_info()
  * vector path clusters page.get_drawings() + union-find on bbox proximity

Output: lanes/L7-figure-census/layout/<pid>.json, deterministic (sorted regions,
rounded coordinates, payload hash), so check.py can re-run and compare.

Usage:
  python -I lanes/L7-figure-census/tools/fig_extract.py layout <pid> [--tol 8]
  python -I lanes/L7-figure-census/tools/fig_extract.py hash <pid>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from math import floor

import numpy as np
import pymupdf

LANE = Path(__file__).resolve().parents[1]
ROOT = LANE.parents[1]  # mcm-skill-work
MANIFEST = ROOT / "artifacts" / "corpus" / "manifest.jsonl"
PAPERS = ROOT / "artifacts" / "papers"
OUT = LANE / "layout"

# region filters, in PDF points and page fractions
MIN_AREA_FRAC = 0.005     # a plot smaller than half a percent of the page is a legend or an inline spark
MIN_SIDE_PT = 25.0        # a box thinner than this is a rule, a divider, or an underline
MAX_AREA_FRAC = 0.85      # fuller than this is a page background or a scanned full page
HEADER_BAND_FRAC = 0.055  # running headers and footers
FOOTER_BAND_FRAC = 0.945
RULE_HEIGHT_PT = 12.0     # isolated horizontal rules
CAPTION_LOOK_PT = 60.0    # how far to look for a caption line below a region
CAPTION_OVERLAP_MIN = 0.25
CAPTION_BOX_PATHS = 4     # a filled box with few paths whose text starts Figure/Table N is a caption background
EDGE_PT = 6.0             # closer than this to the print margin means the exhibit may continue on the next page
FRAGMENT_H_PT = 40.0      # a very shallow cluster is a fragment of an exhibit, kept but flagged
TABLE_GAP_PT = 120.0      # stacked horizontal rules closer than this are one booktabs table
RULE_ALIGN_PT = 4.0       # rules of one table share both ends within this tolerance
COLOR_NEUTRAL_MAX = 0.2   # a rule is greyscale; hyperlink underlines are blue
ROW_STEP_PT = 40.0        # vertical pitch of table body rows
ROW_MIN_NUMERIC = 2       # a body row carries at least this many numeric cells
ABSORB_REACH = 12         # rows to look ahead when extending a table over its body
BACKGROUND_FILL_MIN = 0.98   # a fill this close to white is a page ground, not an exhibit
BACKGROUND_AREA_FRAC = 0.98  # ...when it also covers this much of the page in both axes
OFF_PAGE_FACTOR = 2.0        # a path this many pages wide cannot be an exhibit


def source_pdf(pid: str) -> Path:
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("paper_id") == pid:
            return Path("F:/MCM/MCM-ICM-master") / row["relative_path"]
    raise SystemExit(f"paper id not in manifest: {pid}")


def _rect_tuple(rect) -> tuple[float, float, float, float]:
    return (round(rect.x0, 2), round(rect.y0, 2), round(rect.x1, 2), round(rect.y1, 2))


def _gap(a: tuple, b: tuple) -> float:
    """Largest axis gap between two boxes; negative when they overlap."""
    dx = max(a[0] - b[2], b[0] - a[2])
    dy = max(a[1] - b[3], b[1] - a[3])
    return max(dx, dy)


def draw_bounds(drawing: dict) -> tuple[float, float, float, float] | None:
    """Bounding box of a drawing from its item geometry.

    d["rect"] is unusable for ruled lines: a horizontal or vertical line has a
    degenerate rect that PyMuPDF reports as empty, so a frame drawn as four lines
    disappears if the rect is trusted. Items carry the real points.
    """
    xs: list[float] = []
    ys: list[float] = []
    for item in drawing.get("items", []):
        kind = item[0]
        if kind == "l":
            for p in item[1:3]:
                xs.append(p.x)
                ys.append(p.y)
        elif kind == "re":
            r = item[1]
            xs += [r.x0, r.x1]
            ys += [r.y0, r.y1]
        elif kind == "qu":
            q = item[1]
            for p in (q.ul, q.ur, q.ll, q.lr):
                xs.append(p.x)
                ys.append(p.y)
        elif kind == "c":
            for p in item[1:5]:
                xs.append(p.x)
                ys.append(p.y)
    if not xs:
        return None
    return (round(min(xs), 2), round(min(ys), 2), round(max(xs), 2), round(max(ys), 2))


def is_page_background(drawing: dict, box: tuple, page_w: float, page_h: float) -> bool:
    """True when a drawing is the PDF's own white page ground.

    Some papers paint a white, stroke-free rectangle over the whole page. Left in the
    path list it sits within tol of every other path on that page, so the union-find
    chains the page into one full-page cluster that the MAX_AREA_FRAC guard then
    discards -- and every figure on that page disappears with it.
    """
    if drawing.get("color") is not None or drawing.get("width"):
        return False
    fill = drawing.get("fill")
    if not fill or min(fill) < BACKGROUND_FILL_MIN:
        return False
    return ((box[2] - box[0]) >= BACKGROUND_AREA_FRAC * page_w
            and (box[3] - box[1]) >= BACKGROUND_AREA_FRAC * page_h)


def is_off_page(box: tuple, page_w: float, page_h: float) -> bool:
    """True when a path's coordinates are wildly off the page.

    Some exporters write a filled rectangle with a corner thousands of points outside
    the media box (a `re` of 42394 x 35296 pt on a 612 x 792 pt page). Its bbox then
    reaches across every other path on the page, the union-find produces one cluster,
    and the MAX_AREA_FRAC guard drops the whole page -- silently losing its figures.
    """
    return (box[2] - box[0]) > OFF_PAGE_FACTOR * page_w \
        or (box[3] - box[1]) > OFF_PAGE_FACTOR * page_h


def _union(rects: list[tuple]) -> tuple:
    return (min(r[0] for r in rects), min(r[1] for r in rects),
            max(r[2] for r in rects), max(r[3] for r in rects))


def cluster(rects: list[tuple], tol: float) -> list[list[int]]:
    """Union-find over path boxes. Two boxes join when their gap is within tol.

    Candidates come from a spatial grid, not from a full pairwise sweep. The sweep was
    O(n^2) in the worst case and page 21 of P-B-2010-7947 has 108,891 paths, which
    never finished. Boxes are bucketed by the cells their own bbox covers; a query
    looks only at cells its bbox covers after expanding by tol, which is exactly the
    set of boxes that can sit within tol. Same pairs, same components, same order.
    """
    parent = list(range(len(rects)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    cell = max(tol, 1.0)
    xs0 = np.fromiter((r[0] for r in rects), dtype=np.float64, count=len(rects))
    ys0 = np.fromiter((r[1] for r in rects), dtype=np.float64, count=len(rects))
    xs1 = np.fromiter((r[2] for r in rects), dtype=np.float64, count=len(rects))
    ys1 = np.fromiter((r[3] for r in rects), dtype=np.float64, count=len(rects))

    def joins(a: int, bs) -> np.ndarray:
        """Mask of the boxes in bs whose gap to box a is within tol."""
        bs = np.asarray(bs)
        return np.maximum(np.maximum(xs0[bs] - xs1[a], xs0[a] - xs1[bs]),
                          np.maximum(ys0[bs] - ys1[a], ys0[a] - ys1[bs])) <= tol

    def any_join(left, right) -> bool:
        """True when some box of left is within tol of some box of right.

        Broadcast in row blocks so a dense cell pair does not allocate a huge mask; exits
        at the first hit, which is the common case inside a point cloud.
        """
        if left.size == 0 or right.size == 0:
            return False
        if (xs0[left].min() - xs1[right].max() > tol or xs0[right].min() - xs1[left].max() > tol
                or ys0[left].min() - ys1[right].max() > tol
                or ys0[right].min() - ys1[left].max() > tol):
            return False
        step = max(1, 2_000_000 // max(1, right.size))
        for s in range(0, left.size, step):
            row = left[s:s + step]
            gap = np.maximum(np.maximum(xs0[row][:, None] - xs1[right][None, :],
                                        xs0[right][None, :] - xs1[row][:, None]),
                             np.maximum(ys0[row][:, None] - ys1[right][None, :],
                                        ys0[right][None, :] - ys1[row][:, None]))
            if (gap <= tol).any():
                return True
        return False

    # Boxes are bucketed by every cell their own bbox covers, so a box that sits within tol
    # of another shares a cell with it or touches one of the eight neighbours. Two boxes
    # fully inside one cell (side == tol) are always within tol of each other, so a cell is
    # a clique and can be contracted to one node: that is what turns the dense point cloud
    # of page 16 of P-C-2017-55585 (123,159 paths, 239 million qualifying pairs at tol 8)
    # from a per-pair union into ~3,000 cell comparisons. Boxes straddling a cell border
    # are kept as individual nodes and compared with the old per-box candidate set.
    grid: dict[tuple[int, int], list[int]] = {}
    inside: dict[tuple[int, int], list[int]] = {}
    spanning: list[int] = []
    for i, r in enumerate(rects):
        c0 = (floor(r[0] / cell), floor(r[1] / cell))
        c1 = (floor(r[2] / cell), floor(r[3] / cell))
        if c0 == c1 and cell <= tol:
            inside.setdefault(c0, []).append(i)
        else:
            spanning.append(i)
        for cx in range(c0[0], c1[0] + 1):
            for cy in range(c0[1], c1[1] + 1):
                grid.setdefault((cx, cy), []).append(i)
    buckets = {k: np.fromiter(v, dtype=np.int64) for k, v in grid.items()}
    cells = {k: np.fromiter(v, dtype=np.int64) for k, v in inside.items()}

    leaders = {}
    for c, mem in cells.items():
        lead = int(mem[0])
        leaders[c] = lead
        for j in mem[1:]:
            ri, rj = find(lead), find(int(j))
            if ri != rj:
                parent[rj] = ri

    for (cx, cy), left in cells.items():
        for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1)):
            right = cells.get((cx + dx, cy + dy))
            if right is None:
                continue
            if any_join(left, right):
                ri, rj = find(leaders[(cx, cy)]), find(leaders[(cx + dx, cy + dy)])
                if ri != rj:
                    parent[rj] = ri

    # A straddling box joins a whole cell as soon as ONE of that cell's members is within
    # tol, because those members are a clique. So it needs one union per cell it reaches,
    # never one per qualifying box; a point cloud puts ~2,000 boxes within tol of each
    # straddler, and enumerating them all is the cost this shape avoids.
    spanset = set(spanning)
    straddlers: dict[tuple[int, int], np.ndarray] = {}
    for k, mem in grid.items():
        sub = [j for j in mem if j in spanset]
        if sub:
            straddlers[k] = np.fromiter(sub, dtype=np.int64)

    for i in spanning:
        r = rects[i]
        self_box = np.array([i], dtype=np.int64)
        for cx in range(floor((r[0] - tol) / cell), floor((r[2] + tol) / cell) + 1):
            for cy in range(floor((r[1] - tol) / cell), floor((r[3] + tol) / cell) + 1):
                k = (cx, cy)
                mem = cells.get(k)
                if mem is not None and any_join(self_box, mem):
                    ri, rj = find(i), find(leaders[k])
                    if ri != rj:
                        parent[rj] = ri
                peers = straddlers.get(k)
                if peers is None:
                    continue
                others = peers[peers != i]
                if others.size == 0:
                    continue
                for j in others[joins(i, others)]:
                    ri, rj = find(i), find(int(j))
                    if ri != rj:
                        parent[rj] = ri
    groups: dict[int, list[int]] = {}
    for i in range(len(rects)):
        groups.setdefault(find(i), []).append(i)
    return list(groups.values())


def caption_candidates(page, region: tuple, page_w: float) -> dict:
    """Nearest text line below the region (else above), with horizontal overlap."""
    w = page.get_text("words")
    if not w:
        return {"below": None, "above": None}

    def lines_near(lo: float, hi: float) -> list[tuple[float, str]]:
        hits = []
        for x0, y0, x1, y1, text, *_ in w:
            if not (lo <= (y0 + y1) / 2 <= hi):
                continue
            ov = min(x1, region[2]) - max(x0, region[0])
            if ov / max(page_w, 1) < CAPTION_OVERLAP_MIN and ov < 60:
                continue
            hits.append((y0, text))
        hits.sort()
        return hits

    below = [t for _, t in lines_near(region[3] - 2, region[3] + CAPTION_LOOK_PT)]
    above = [t for _, t in lines_near(region[1] - CAPTION_LOOK_PT, region[1] + 2)]
    return {
        "below": " ".join(below)[:400] if below else None,
        "above": " ".join(above[-6:])[:400] if above else None,
    }


CAPTION_RE = None  # compiled lazily to keep the import list small


def text_inside(page, region: tuple, page_w: float) -> list[str]:
    """Text lines whose centre falls inside the region, in reading order."""
    hits = []
    for x0, y0, x1, y1, text, *_ in page.get_text("words"):
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if region[0] - 2 <= cx <= region[2] + 2 and region[1] - 2 <= cy <= region[3] + 2:
            hits.append((round(cy, 1), round(cx, 1), text))
    hits.sort()
    return [t for *_, t in hits]


def is_caption_background(path_count: int, inside: list[str]) -> bool:
    """A shaded/framed caption: few paths, and the text starts with Figure/Table N."""
    if path_count > CAPTION_BOX_PATHS or not inside:
        return False
    return _caption_re().match(" ".join(inside[:3])) is not None


def _caption_re():
    global CAPTION_RE
    if CAPTION_RE is None:
        CAPTION_RE = re.compile(r"^\s*(Figure|Table)\s*\d+")
    return CAPTION_RE


def body_text_top(page) -> float:
    """Top of the running body text: rules above it are headers, not table rules."""
    tops = [y0 for x0, y0, x1, y1, text, *_ in page.get_text("words") if len(text) >= 4]
    return min(tops) if tops else 0.0


def _is_number(token: str) -> bool:
    return re.fullmatch(r"[(~]?-?\d+(?:\.\d+)?[%)]?", token) is not None


def _rows_above(page, span: tuple, top: float, floor: float) -> tuple | None:
    """Top of a run of numeric cells ending just above `top`, not crossing `floor`."""
    lines: dict[float, list] = {}
    for x0, y0, x1, y1, text, *_ in page.get_text("words"):
        if y1 >= top - 1 or y0 < max(top - ABSORB_REACH * ROW_STEP_PT, floor):
            continue
        if x1 < span[0] - 4 or x0 > span[2] + 4:
            continue
        lines.setdefault(round(y0, 1), []).append((x0, x1, y1, text))

    start = None
    prev = top
    for y0 in sorted(lines, reverse=True):
        cells = lines[y0]
        if prev - max(c[2] for c in cells) > ROW_STEP_PT:
            break
        if sum(1 for *_, t in cells if _is_number(t)) < ROW_MIN_NUMERIC:
            break
        start = y0
        prev = y0
    return start


def _absorb_rows(page, span: tuple, bottom: float) -> tuple:
    """Extend a table's bottom over its own body rows.

    Many of these tables print only two rules (top and under the header) and no
    closing rule, so the rows below the last rule fall outside the span and the crop
    shows a bare header. Body rows are numeric cells; the paragraph that follows is
    not, and a section heading is not either.
    """
    lines: dict[float, list] = {}
    for x0, y0, x1, y1, text, *_ in page.get_text("words"):
        if y0 <= bottom + 1 or y0 > bottom + ABSORB_REACH * ROW_STEP_PT:
            continue
        if x1 < span[0] - 4 or x0 > span[2] + 4:
            continue
        lines.setdefault(round(y0, 1), []).append((x0, x1, y1, text))

    end = bottom
    for y0 in sorted(lines):
        if y0 - end > ROW_STEP_PT:
            break
        cells = lines[y0]
        if sum(1 for *_, t in cells if _is_number(t)) < ROW_MIN_NUMERIC:
            break
        end = max(c[2] for c in cells)
    return (span[0], span[1], span[2], round(end, 2)) if end > bottom else span


def _has_caption_or_heading(page, y_from: float, y_to: float) -> bool:
    """A table caption or a section heading between two rules means two exhibits."""
    for x0, y0, x1, y1, text, *_ in page.get_text("words"):
        if not (y_from <= (y0 + y1) / 2 <= y_to):
            continue
        if text in ("Table", "Figure"):
            return True
        if x0 < 140 and _HEADING_RE.fullmatch(text):
            return True
    return False


# a numbered section heading carries a trailing period; a table cell ("0", "1") does not
_HEADING_RE = re.compile(r"\d+(?:\.\d+)*\.")


def rule_table_regions(page, clusters: list[tuple], neutral: list[bool],
                       x0_min: float) -> list[dict]:
    """Booktabs tables: horizontal rules only, no vertical strokes.

    A three-line table contributes one 3.6 pt cluster per rule, each of which the rule
    filter would delete, so the table disappears entirely. Two or more page-wide rules
    stacked within TABLE_GAP_PT, with the text between them, are one table.
    """
    page_w = page.rect.width
    top = body_text_top(page)
    rules = []
    for i, box in enumerate(clusters):
        w, h = box[2] - box[0], box[3] - box[1]
        if not neutral[i]:  # a coloured stroke is a hyperlink underline, not a rule
            continue
        if h <= RULE_HEIGHT_PT and w >= 0.5 * page_w and box[1] >= top - 2:
            rules.append((box, i))
    rules.sort(key=lambda r: r[0][1])

    groups: list[list[tuple]] = []
    for box, idx in rules:
        if groups and box[1] - groups[-1][-1][0][3] <= TABLE_GAP_PT:
            prev = groups[-1][-1][0]
            overlap = min(prev[2], box[2]) - max(prev[0], box[0])
            if overlap >= 0.5 * min(prev[2] - prev[0], box[2] - box[0]) and not                     _has_caption_or_heading(page, prev[3], box[1]):
                groups[-1].append((box, idx))
                continue
        groups.append([(box, idx)])

    out = []
    used: set[int] = set()
    for group in groups:
        # A booktabs table's rules share one width: they start and end at the same
        # margin. A running-header underline does not, and grouping it with the table
        # below drags the body paragraph into the region.
        aligned = []
        for box, idx in group:
            peers = [b for b, _ in group if abs(b[0] - box[0]) <= RULE_ALIGN_PT
                     and abs(b[2] - box[2]) <= RULE_ALIGN_PT]
            if len(peers) >= 2 and len(peers) > len(aligned):
                aligned = [(b, i) for b, i in group if any(b == p for p in peers)]
        group = aligned  # two rules that do not align are not one table
        if len(group) < 2:
            continue
        boxes = [b for b, _ in group]
        used |= {i for _, i in group}
        span = (min(b[0] for b in boxes), boxes[0][1],
                max(b[2] for b in boxes), boxes[-1][3])
        if span[3] - span[1] < MIN_SIDE_PT:
            # A long, mostly textual table (a notation list) prints its header rule and
            # its closing rule far more than TABLE_GAP_PT apart, so the group holds only
            # the two opening rules and comes out thinner than MIN_SIDE_PT. Extend to the
            # next aligned page-wide rule instead of discarding a real table.
            closing = next(((b, i) for b, i in rules if i not in used
                            and b[1] > span[3] + 1
                            and abs(b[0] - span[0]) <= RULE_ALIGN_PT
                            and abs(b[2] - span[2]) <= RULE_ALIGN_PT), None)
            if closing is not None:
                b, i = closing
                span = (span[0], span[1], span[2], b[3])
                used.add(i)
                group = group + [(b, i)]
        span = _absorb_rows(page, span, boxes[-1][3])
        out.append({"bbox": tuple(round(v, 2) for v in span), "raster": False,
                    "path_count": len(group), "source": "rule-table",
                    "rule_table": True,
                    "consumed": {i for _, i in group}})

    # A table that runs off the page keeps only its closing rule here, the opening rule
    # being on the previous page. Without this the tail rows are measured nowhere.
    for box, idx in rules:
        if idx in used:
            continue
        host = next((o for o in out if o["bbox"][1] <= box[1] <= o["bbox"][3]), None)
        if host is not None:
            continue  # already inside a table that was found whole
        above = next((o for o in out if 0 <= box[1] - o["bbox"][3] <= ROW_STEP_PT
                      and min(o["bbox"][2], box[2]) > max(o["bbox"][0], box[0])), None)
        if above is not None:  # this is that table's own closing rule
            above["bbox"] = (above["bbox"][0], above["bbox"][1], above["bbox"][2],
                             round(box[3], 2))
            above["consumed"].add(idx)
            used.add(idx)
            continue
        floor = max([b[3] for b, _ in rules if b[3] <= box[1]] or [0.0])
        start = _rows_above(page, box, box[1], floor)
        if start is None:
            continue
        out.append({"bbox": (round(box[0], 2), round(start - 2, 2), round(box[2], 2),
                             round(box[3], 2)),
                    "raster": False, "path_count": 1, "source": "rule-table-tail",
                    "rule_table": True, "consumed": {idx}})
    return out


def page_regions(page, tol: float) -> list[dict]:
    page_w, page_h = page.rect.width, page.rect.height
    page_area = page_w * page_h
    regions = []

    # source 1: image blocks
    for info in page.get_image_info():
        box = _rect_tuple(pymupdf.Rect(info["bbox"]))
        regions.append({"bbox": box, "raster": True, "path_count": 1, "source": "image"})

    # source 2: vector path clusters
    boxes = []
    neutral = []
    for d in page.get_drawings():
        bounds = draw_bounds(d)
        if bounds is None:
            continue
        if is_page_background(d, bounds, page_w, page_h):
            continue
        if is_off_page(bounds, page_w, page_h):
            continue
        boxes.append(bounds)
        ink = d.get("fill") or d.get("color") or (0.0, 0.0, 0.0)
        neutral.append(max(ink) - min(ink) <= COLOR_NEUTRAL_MAX)
    if boxes:
        groups = cluster(boxes, tol)
        cluster_boxes = [_union([boxes[i] for i in g]) for g in groups]
        cluster_neutral = [all(neutral[i] for i in g) for g in groups]
        tables = rule_table_regions(page, cluster_boxes, cluster_neutral, MIN_SIDE_PT)
        consumed: set[int] = set()
        for tbl in tables:
            consumed |= tbl.pop("consumed")
        for n, group in enumerate(groups):
            if n in consumed:  # those rules are already one table
                continue
            regions.append({"bbox": cluster_boxes[n], "raster": False,
                            "path_count": len(group), "source": "paths"})
        regions.extend(tables)

    # fuse: drop a path cluster only when an image block CONTAINS it. Overlap is not
    # enough: a plot frame that surrounds a pasted screenshot overlaps it and must stay,
    # otherwise every figure with an inset image vanishes from the census.
    def contained(inner: tuple, outer: tuple, tol: float = 2.0) -> bool:
        return (inner[0] >= outer[0] - tol and inner[1] >= outer[1] - tol
                and inner[2] <= outer[2] + tol and inner[3] <= outer[3] + tol)

    def same_box(a: tuple, b: tuple, tol: float = 4.0) -> bool:
        return all(abs(x - y) <= tol for x, y in zip(a, b))

    def area(box: tuple) -> float:
        return max(0.0, box[2] - box[0]) * max(0.0, box[3] - box[1])

    # pass 1: path clusters that are frames or content of an image
    frames_or_inside = set()
    for i, reg in enumerate(regions):
        if reg["source"] != "paths":
            continue
        if any(o["raster"] and contained(reg["bbox"], o["bbox"]) for o in regions):
            frames_or_inside.add(i)
        elif reg["path_count"] <= 20 and any(
                o["raster"] and contained(o["bbox"], reg["bbox"])
                and area(o["bbox"]) >= 0.8 * area(reg["bbox"]) for o in regions):
            frames_or_inside.add(i)
    kept = [reg for i, reg in enumerate(regions) if i not in frames_or_inside]

    # pass 2: an image retraced by a SURVIVING path cluster is the same exhibit.
    # Both rules cannot fire on one pair, otherwise image and frame each drop the other.
    surviving_paths = [r for r in kept if r["source"] == "paths"]
    kept = [reg for reg in kept
            if not (reg["source"] == "image"
                    and any(same_box(reg["bbox"], o["bbox"]) for o in surviving_paths))]

    out = []
    for reg in kept:
        x0, y0, x1, y1 = reg["bbox"]
        w, h = x1 - x0, y1 - y0
        area_frac = (w * h) / page_area
        if area_frac > MAX_AREA_FRAC:
            continue
        if area_frac < MIN_AREA_FRAC:
            continue
        if w < MIN_SIDE_PT or h < MIN_SIDE_PT:
            continue
        if h < RULE_HEIGHT_PT and w > 0.8 * page_w:
            continue
        if y1 <= HEADER_BAND_FRAC * page_h or y0 >= FOOTER_BAND_FRAC * page_h:
            continue
        inside = text_inside(page, reg["bbox"], page_w)
        # only a vector cluster can be a shaded caption box; an image block whose own
        # white margin carries the caption line under it is a figure, not a caption
        if reg["source"] != "image" and is_caption_background(reg["path_count"], inside):
            continue
        caps = caption_candidates(page, reg["bbox"], page_w)
        out.append({
            "bbox": list(reg["bbox"]),
            "page": page.number + 1,
            "area_frac": round(area_frac, 5),
            "w": round(w, 2),
            "h": round(h, 2),
            "aspect": round(w / h, 3) if h else None,
            "kind": "raster" if reg["raster"] else "vector",
            "path_count": reg["path_count"],
            "rule_table": bool(reg.get("rule_table")),
            "touches_top": y0 <= EDGE_PT,
            "touches_bottom": y1 >= page_h - EDGE_PT,
            "fragment_suspected": h < FRAGMENT_H_PT or len(inside) > 0,
            "text_inside": inside[:12],
            "caption_below": caps["below"],
            "caption_above": caps["above"],
        })
    out.sort(key=lambda r: (r["bbox"][1], r["bbox"][0]))
    return out


def build(pid: str, tol: float) -> dict:
    pdf = source_pdf(pid)
    doc = pymupdf.open(pdf)
    pages = []
    for page in doc:
        regs = page_regions(page, tol)
        if not regs and len(page.get_drawings()) > 20:
            print(f"warning: page {page.number + 1} of {pid} has "
                  f"{len(page.get_drawings())} paths but no measured region",
                  file=sys.stderr)
        if regs:
            pages.append({"page": page.number + 1,
                          "width": round(page.rect.width, 2),
                          "height": round(page.rect.height, 2),
                          "regions": regs})
    payload = {
        "paper": pid,
        "source_pdf": str(pdf).replace("\\", "/"),
        "page_count": len(doc),
        "layout_version": 1,
        "params": {"tol": tol, "min_area_frac": MIN_AREA_FRAC, "min_side_pt": MIN_SIDE_PT,
                   "max_area_frac": MAX_AREA_FRAC},
        "region_total": sum(len(p["regions"]) for p in pages),
        "pages": pages,
    }
    doc.close()
    payload["layout_sha256"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]
    return payload


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["layout", "hash"])
    ap.add_argument("pid")
    ap.add_argument("--tol", type=float, default=8.0)
    args = ap.parse_args(argv)

    if args.command == "hash":
        path = OUT / f"{args.pid}.json"
        if not path.exists():
            raise SystemExit(f"no layout for {args.pid}")
        print(json.loads(path.read_text(encoding="utf-8"))["layout_sha256"])
        return 0

    payload = build(args.pid, args.tol)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{payload['paper']}.json").write_text(
        json.dumps(payload, indent=1, sort_keys=True), encoding="utf-8")
    print(f"{payload['paper']} pages={payload['page_count']} "
          f"pages_with_regions={len(payload['pages'])} regions={payload['region_total']} "
          f"sha={payload['layout_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
