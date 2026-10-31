"""Measure everything a distillation record needs except the judgement calls.

Writes .proxy/<pid>-ctx.json and a readable .proxy/<pid>-ctx.txt holding:
  headings   numbered and named section titles, in page order
  captions   every line that starts with Figure/Fig./Table + a number
  mentions   every in-body reference, with its whole sentence and page
  regions    per measured region: section path, page order, page zone, area, solo page,
             nearest caption, and the reference sentences that name it

It never decides a family, a caption style, or whether a sentence "interprets". Those
are read from the crop and the surrounding paragraph by hand; this file only supplies
the verbatim text and the geometry so the hand pass can quote instead of retype.

Usage: python -I lanes/L7-figure-census/tools/context_extract.py <pid>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

RUNNING = re.compile(r"^(team\s*#?\s*\d+|page\s+\d+\s+of\s+\d+|[\d\s]+)$", re.I)
NUMBERED = re.compile(r"^(\d+(?:\.\d+)*)\.?\s*([A-Z][^.]{2,88})$")
ROMAN = re.compile(r"^([IVX]{1,4})\.\s+([A-Z][^.]{2,88})$")
NAMED = {
    "abstract", "introduction", "assumptions", "assumption", "symbols",
    "notation", "model", "results", "analysis", "sensitivity analysis",
    "strengths and weaknesses", "evaluation", "conclusion", "conclusions",
    "summary", "references", "appendix", "discussion", "verification",
    "testing", "validation", "data", "method", "methods",
}
CAPTION = re.compile(r"^(figure|fig\.?|table)\s*(\d+)\s*[:.]?\s*(.*)$", re.I)
CAPTION_END = re.compile(r"^((?:figure|fig\.?|table)\s*\d+[.:]?\s+[^.]{2,200}\.)", re.I)
REFERENCE = re.compile(r"\b(figure|fig\.?|table)\s*(\d+)\b", re.I)
BODY_WORDS = {"shows", "show", "tells", "tell", "illustrates", "illustrate",
              "indicates", "indicate", "clearly", "also", "which", "is", "are",
              "and", "in", "for", "with", "as", "can", "we", "the"}
SECTION_WORDS = [
    ("abstract", ("abstract", "summary")),
    ("introduction", ("introduction", "background", "overview of the problem")),
    ("assumption", ("assumption", "hypothes")),
    ("symbols", ("symbol", "notation")),
    ("test", ("test", "validation", "verification", "check", "review")),
    ("evaluation", ("evaluat", "assessment", "conclusion", "strength", "weakness",
                    "discussion", "summary")),
    ("sensitivity", ("sensitivity",)),
    ("model", ("model", "method", "formulation", "construction", "establish")),
    ("solution", ("solution", "solving", "algorithm", "computation", "calculation",
                  "simulation")),
    ("result", ("result", "outcome", "output", "analysis")),
    ("appendix", ("appendix", "annex")),
]


def raw_lines(pid: str, page: int) -> list[str]:
    """Line structure of the page text layer, running heads removed.

    schema.page_text collapses newlines for substring checks; headings and captions
    need the lines back, so this reads the file directly.
    """
    path = schema.PAPERS / pid / "text" / "pages" / f"page-{page:04d}.txt"
    if not path.exists():
        return []
    out = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = " ".join(raw.split())
        if not line or RUNNING.match(line):
            continue
        out.append(line)
    return out


def section_kind(title: str) -> str:
    low = title.lower()
    for kind, keys in SECTION_WORDS:
        if any(k in low for k in keys):
            return kind
    return "other"


TRUNCATED = {"for", "and", "the", "of", "to", "with", "is", "are", "in", "a", "an",
             "that", "which", "as", "by", "on", "at", "from"}


def _title_case_ratio(title: str) -> float:
    """Share of the long words that open with a capital letter."""
    words = re.findall(r"[A-Za-z]{4,}", title)
    if not words:
        return 0.0
    return sum(1 for w in words if w[0].isupper()) / len(words)


def is_heading(prev: str, line: str, nxt: str) -> dict | None:
    if len(line) > 70 or "...." in line:
        return None
    # Roman numerals are not accepted as section numbers: in these papers "I ...",
    # "II ..." are list items inside an evaluation section far more often than
    # chapters, and a wrong section path is worse than a missing one.
    m = NUMBERED.match(line)
    if m:
        title = m.group(2).strip()
        toks = title.split()
        # A wrapped sentence fragment opening with a digit looks numbered too: it stops
        # on a preposition. Headings do not.
        if not 1 <= len(toks) <= 12 or toks[-1].lower().strip(".,;:") in TRUNCATED:
            return None
        if len(toks) > 8:
            # Beyond eight words the line is usually a wrapped caption, a list-of-figures
            # entry or a numbered definition, not a heading. A real heading of that length
            # is set in title case and is not broken off on a comma, a hyphen or a page
            # number -- "6.2 Sensitivity with Respect to Number of Self Driving Cars" is
            # the case this admits.
            if toks[-1].endswith((",", "-", ";")) or toks[-1].rstrip(".,;:-").isdigit():
                return None
            if _title_case_ratio(title) < 0.5:
                return None
        return {"number": m.group(1), "title": title, "numbered": True}
    low = line.lower().rstrip(":. ")
    if low in NAMED and len(line.split()) <= 6 and line[:1].isupper():
        return {"number": "", "title": line.rstrip(":."), "numbered": False}
    return None


def build(pid: str) -> dict:
    layout = json.loads((LANE / "layout" / f"{pid}.json").read_text(encoding="utf-8"))
    pages = list(range(1, int(layout["page_count"]) + 1))
    texts = {p: schema.page_text(pid, p) for p in pages}

    headings: list[dict] = []
    stack: list[dict] = []
    captions: list[dict] = []
    mentions: list[dict] = []
    for page in pages:
        lines = raw_lines(pid, page)
        i = 0
        while i < len(lines):
            line = lines[i]
            i += 1
            head = is_heading(lines[i - 1] if i else "", line,
                              lines[i + 1] if i + 1 < len(lines) else "")
            if head:
                parts = head["number"].split(".") if head["number"] else []
                while stack and (not stack[-1]["number"] or len(
                        stack[-1]["number"].split(".")) >= len(parts or [1])):
                    stack.pop()
                head.update({"page": page, "kind": section_kind(head["title"]),
                             "label": (f"{head['number']} {head['title']}".strip())})
                headings.append(head)
                if head["numbered"]:
                    stack.append(head)
                continue
            m = CAPTION.match(line)
            if m and "...." not in line and len(line) <= 240:
                text = line
                # A bare "Figure 7" line is the whole caption in these papers: the
                # caption is a bold centred label with no body, and the line under it
                # (often a bulleted sentence) is body prose. So no joining when the
                # part after the number is empty.
                bare = not m.group(3).strip()
                while (not bare
                       and i < len(lines) and len(text) < 260
                       and not CAPTION.match(lines[i])
                       and not is_heading("", lines[i], "")
                       and not text.rstrip().endswith(".")
                       and not lines[i][:1].isupper()):
                    text = text.rstrip() + " " + lines[i]
                    i += 1
                # A joined caption can swallow the paragraph under it. Cut at the first
                # sentence end after the numbering token; a caption with no terminal
                # period (a bare title) keeps only its own first line.
                cut = CAPTION_END.match(text)
                if cut:
                    text = cut.group(1)
                elif text != line:
                    text = line
                tail = m.group(3).strip().split()
                head_word = tail[0].lower().strip(",") if tail else ""
                captions.append({
                    "page": page, "kind": m.group(1).lower().rstrip("."),
                    "number": int(m.group(2)), "text": text,
                    "suspect_body": head_word in BODY_WORDS})
                continue
        for sent in schema.sentences(texts[page]):
            if CAPTION.match(sent):
                continue
            for m in REFERENCE.finditer(sent):
                mentions.append({"page": page, "kind": m.group(1).lower().rstrip("."),
                                 "number": int(m.group(2)), "sentence": sent,
                                 "spelling": m.group(0)})

    def path_for(page: int) -> tuple[list[str], bool]:
        here = [h for h in headings if h["page"] <= page]
        if not here:
            return ["未编号标题 正文开篇"], False
        last = here[-1]
        chain = [h["label"] for h in here
                 if h["numbered"] and h["number"] != last["number"]
                 and last["number"].startswith(h["number"] + ".")]
        if last["numbered"]:
            return (chain + [last["label"]], True)
        return ([f"未编号标题 {last['title']}"] + chain, False)

    regions = []
    for pg in layout["pages"]:
        page = pg["page"]
        height = pg["height"]
        ordered = sorted(pg["regions"], key=lambda r: r["bbox"][1])
        for idx, r in enumerate(ordered, 1):
            y0, y1 = r["bbox"][1], r["bbox"][3]
            mid = (y0 + y1) / 2 / height
            zone = "top" if mid < 0.34 else "bottom" if mid > 0.67 else "middle"
            solo = r["area_frac"] >= 0.55 and len([o for o in pg["regions"]
                                                   if o is not r]) == 0
            section, numbered = path_for(page)
            near = (r.get("caption_above", "") or "") + " " + (
                r.get("caption_below", "") or "")
            keys = [(m.group(1).lower().rstrip("."), int(m.group(2)))
                    for m in REFERENCE.finditer(near)]
            refs = [m for m in mentions
                    if (m["kind"], m["number"]) in keys][:6]
            regions.append({
                "page": page, "region": idx, "bbox": r["bbox"],
                "area_frac": round(r["area_frac"], 3),
                "kind": r.get("kind"), "paths": r.get("path_count"),
                "page_zone": zone, "solo_page": solo,
                "section_path": section, "section_numbered": numbered,
                "section_kind": (next((k for k in
                                       (section_kind(t) for t in reversed(section))
                                       if k != "other"), "other")
                                 if numbered else "other"),
                "caption_above": r.get("caption_above", ""),
                "caption_below": r.get("caption_below", ""),
                "text_inside": r.get("text_inside", "")[:400],
                "refs": [{"page": m["page"], "sentence": m["sentence"],
                          "spelling": m["spelling"]} for m in refs],
            })
    return {"paper": pid, "pages": pages, "headings": headings,
            "captions": captions, "mentions": mentions, "regions": regions}


def render(data: dict) -> str:
    out = [f"paper {data['paper']}  pages {len(data['pages'])}  "
           f"regions {len(data['regions'])}", "", "== headings"]
    for h in data["headings"]:
        out.append(f"  p{h['page']:>3} {'#' * h['number'].count('.') if h['number'] else ''}"
                   f" {h['label']}   [{h['kind']}]")
    out += ["", "== captions"]
    for c in data["captions"]:
        out.append(f"  p{c['page']:>3} {c['kind']} {c['number']}: {c['text'][:110]}")
    out += ["", "== mentions"]
    for m in data["mentions"]:
        out.append(f"  p{m['page']:>3} {m['kind']} {m['number']} "
                   f"[{m['spelling']}] {m['sentence'][:150]}")
    out += ["", "== regions"]
    for r in data["regions"]:
        out.append(f"  p{r['page']:>3} r{r['region']} {r['kind']} zone={r['page_zone']} "
                   f"solo={r['solo_page']} area={r['area_frac']} "
                   f"sec={' > '.join(r['section_path'])} [{r['section_kind']}]")
        if r.get("caption_above"):
            out.append(f"      cap^: {r['caption_above'][:120]}")
        if r.get("caption_below"):
            out.append(f"      cap_|: {r['caption_below'][:120]}")
        if r.get("text_inside"):
            out.append(f"      in: {r['text_inside'][:160]}")
        for m in r.get("refs", []):
            out.append(f"      ref p{m['page']}: {m['sentence'][:140]}")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if not argv:
        raise SystemExit("usage: context_extract.py <pid>")
    pid = argv[0]
    data = build(pid)
    proxy = LANE / ".proxy"
    proxy.mkdir(exist_ok=True)
    (proxy / f"{pid}-ctx.json").write_text(
        json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    (proxy / f"{pid}-ctx.txt").write_text(render(data), encoding="utf-8")
    print(f"{pid}: headings={len(data['headings'])} captions={len(data['captions'])} "
          f"mentions={len(data['mentions'])} regions={len(data['regions'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
