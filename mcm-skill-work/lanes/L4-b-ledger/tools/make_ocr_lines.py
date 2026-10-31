"""Run RapidOCR over a paper's rendered pages and cache the line boxes lane-locally.

The upstream `artifacts/papers/<pid>/ocr-lines.jsonl` only exists for papers that
were OCR'd when the corpus was built. Papers flagged `partial-text-review` have
image pages that no text layer covers, so the lane produces the same geometry
from `artifacts/papers/<pid>/rendered/page-*.png` itself and keeps the result in
`.proxy/ocr/<paper_id>.jsonl`, which `ocr_layout.py` reads in preference to the
artifacts file. Nothing under `artifacts/**` is written.

Usage:
  python -I lanes/L4-b-ledger/tools/make_ocr_lines.py <paper_id>
"""
import json
import pathlib
import re
import sys

from rapidocr_onnxruntime import RapidOCR

ROOT = pathlib.Path(__file__).resolve().parents[3]
PAPERS = ROOT / "artifacts" / "papers"
CACHE = pathlib.Path(__file__).resolve().parents[1] / ".proxy" / "ocr"


def page_number(path: pathlib.Path) -> int:
    match = re.search(r"(\d+)", path.stem)
    if not match:
        raise ValueError(f"no page number in {path.name}")
    return int(match.group(1))


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: make_ocr_lines.py <paper_id>")
    paper_id = sys.argv[1]
    pages = sorted((PAPERS / paper_id / "rendered").glob("page-*.png"), key=page_number)
    if not pages:
        sys.exit(f"no rendered pages for {paper_id}")

    engine = RapidOCR()
    out = CACHE / (paper_id + ".jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fh:
        for path in pages:
            result, elapsed = engine(str(path))
            lines = [
                {"box": box, "confidence": round(float(score), 6), "text": text}
                for box, text, score in (result or [])
            ]
            fh.write(json.dumps({"page_index": page_number(path),
                                 "engine_elapsed": [round(float(e), 6) for e in elapsed],
                                 "lines": lines}, ensure_ascii=False) + "\n")
    tmp.replace(out)
    print(f"wrote {out.relative_to(ROOT)} {len(pages)} pages")


if __name__ == "__main__":
    main()
