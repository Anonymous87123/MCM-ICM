"""Create-only PDF text corpus. Resumable extraction; never edits legacy artifacts."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

from text_corpus import digest, encoded, export_document, file_hash, json_new, make_document, read_json, rows, write_new


def freeze_scope(work: Path, output: Path, source: Path) -> dict:
    manifest = work / "artifacts/corpus/manifest.jsonl"
    progress = work / "artifacts/progress.jsonl"
    eligible = {m["paper_id"]: m for m in rows(manifest) if m.get("eligible_paper")}
    queue = sorted(rows(progress), key=lambda p: p["queue_position"])
    if len(eligible) != len(queue) or {p["paper_id"] for p in queue} != set(eligible):
        raise ValueError("Eligible corpus and deterministic queue differ")
    if [p["queue_position"] for p in queue] != list(range(1, len(queue)+1)):
        raise ValueError("Queue positions are not unique contiguous positions")
    records = [{**eligible[p["paper_id"]], "queue_position": p["queue_position"]} for p in queue]
    signature = {"manifest": file_hash(manifest), "progress": file_hash(progress),
                 "builder": file_hash(Path(__file__)), "library": file_hash(Path(__file__).with_name("text_corpus.py")),
                 "pymupdf": importlib.metadata.version("PyMuPDF")}
    identity = digest(encoded({"inputs": signature, "records": records}))
    if (output / "scope.json").exists():
        old = read_json(output / "scope.json")
        if old["scope_id"] != identity:
            raise ValueError("Inputs or builder changed; use a NEW output version, never overwrite")
        return old
    if output.exists() and any(output.iterdir()):
        raise ValueError("Nonempty output has no valid scope; refusing to adopt it")
    forbidden = [work / "artifacts/papers", work / "artifacts/transactions", work / "artifacts/corpus",
                 work / "artifacts/language-units", work / "artifacts/model-units"]
    for f in forbidden:
        if output.resolve().is_relative_to(f.resolve()):
            raise ValueError("Output overlaps protected legacy data")
    output.mkdir(parents=True, exist_ok=True)
    legacy_audit = work / "artifacts/transactions/integrity-audit-20261025-v1.json"
    bindings = {}
    if legacy_audit.exists():
        for rel in read_json(legacy_audit)["source_sha256"]:
            p = work / rel
            bindings[rel] = file_hash(p) if p.is_file() else None
    scope = {"schema_version": 1, "scope_id": identity, "source_root": str(source.resolve()),
             "input_sha256": signature, "paper_count": len(records),
             "physical_page_count": sum(m["page_count"] for m in records),
             "records": records, "exclusions": len(rows(manifest))-len(records),
             "stage": "text-database-only; not full-paper closure"}
    json_new(output / "legacy-preimages.json", bindings)
    write_new(output / "inputs/manifest.jsonl", manifest.read_bytes())
    write_new(output / "inputs/progress.jsonl", progress.read_bytes())
    json_new(output / "scope.json", scope)
    return scope


def compare_text(native: str, other: str) -> dict:
    # A diagnostic only: agreement is NEVER a completeness certificate.
    def words(t):
        return Counter(re.findall(r"[A-Za-z]{2,}", t.lower()))
    a, b = words(native), words(other)
    denominator = max(sum(a.values()), sum(b.values()), 1)
    score = sum((a & b).values()) / denominator
    return {"word_multiset_agreement": round(score, 6), "native_word_count": sum(a.values()),
            "comparison_word_count": sum(b.values()),
            "status": "agreement" if score >= .97 else "review-required"}


def extract_record(scope: dict, record: dict, output: Path) -> dict:
    import pymupdf
    pid = record["paper_id"]
    target = output / "papers" / pid
    if (target / "COMPLETE.json").is_file():
        done = read_json(target / "COMPLETE.json")
        for rel, sha in done["files"].items():
            if file_hash(target / rel) != sha:
                raise ValueError(f"Existing extraction modified: {pid}/{rel}")
        return done["summary"]
    if target.exists():
        raise ValueError(f"Incomplete extraction retained for investigation; use a new version: {target}")
    source = Path(scope["source_root"]) / record["relative_path"]
    if file_hash(source) != record["sha256"]:
        raise ValueError(f"Source PDF hash differs: {pid}")
    executable = shutil.which("pdftotext")
    if not executable:
        raise ValueError("pdftotext is required for independent comparison")
    result = subprocess.run([executable, "-layout", "-enc", "UTF-8", str(source), "-"],
                            capture_output=True, check=True, timeout=300)
    native_other = result.stdout.decode("utf-8", errors="replace").replace("\r\n", "\n").split("\f")
    if native_other and not native_other[-1].strip():
        native_other.pop()
    target.mkdir(parents=True)
    write_new(target / "raw/pdftotext.bin", result.stdout)
    pages = []
    with pymupdf.open(source) as pdf:
        if len(pdf) != record["page_count"]:
            raise ValueError(f"Physical page mismatch: {pid}")
        for i, page in enumerate(pdf, 1):
            data = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES)
            lines = []
            for bi, block in enumerate(data["blocks"]):
                if block["type"] != 0:
                    continue
                for li, line in enumerate(block["lines"]):
                    spans = [{k: span[k] for k in ("text", "bbox", "font", "size", "flags")} for span in line["spans"]]
                    if not spans:
                        continue
                    lines.append({"line_id": f"p{i:04d}-n{bi:04d}-l{li:04d}", "native_block": bi,
                                  "page": i, "bbox": list(line["bbox"]),
                                  "text": "".join(s["text"] for s in spans), "spans": spans,
                                  "font_size": max(s["size"] for s in spans),
                                  "bold": any(s["flags"] & 16 for s in spans)})
            text = "\n".join(x["text"] for x in lines)
            other = native_other[i-1] if i <= len(native_other) else ""
            pages.append({"page": i, "width": page.rect.width, "height": page.rect.height,
                          "rotation": page.rotation, "lines": lines,
                          "comparison": compare_text(text, other),
                          "embedded_image_rectangles": [list(x["bbox"]) for x in page.get_image_info()],
                          "ocr_status": "not-run", "source_sha256": record["sha256"]})
    raw = b"".join((json.dumps(p, ensure_ascii=True, sort_keys=True) + "\n").encode() for p in pages)
    write_new(target / "raw/pages.jsonl", raw)
    meta = {k: record[k] for k in ("paper_id", "problem_type", "year", "queue_position", "page_count")}
    meta.update(source_relative_path=record["relative_path"], source_sha256=record["sha256"],
                scope_id=scope["scope_id"], raw_pages_sha256=digest(raw),
                independent_page_count=len(native_other))
    document = make_document(meta, pages)
    export_document(target, document)
    summary = {"paper_id": pid, "queue_position": record["queue_position"], "pages": len(pages),
               "sections": len(document["sections"]), "blocks": len(document["blocks"]),
               "defects": len(document["defects"]), "status": "machine-draft"}
    files = {str(p.relative_to(target)).replace("\\", "/"): file_hash(p)
             for p in sorted(target.rglob("*")) if p.is_file()}
    json_new(target / "COMPLETE.json", {"scope_id": scope["scope_id"], "summary": summary, "files": files})
    return summary


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--work-root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--source-root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--paper-id", action="append")
    p.add_argument("--limit", type=int)
    args = p.parse_args(argv)
    scope = freeze_scope(args.work_root.resolve(), args.output.resolve(), args.source_root.resolve())
    records = scope["records"]
    if args.paper_id:
        if set(args.paper_id)-{r["paper_id"] for r in records}:
            raise ValueError("Unknown requested paper")
        records = [r for r in records if r["paper_id"] in args.paper_id]
    if args.limit:
        records = records[:args.limit]
    for record in records:
        print(json.dumps(extract_record(scope, record, args.output.resolve())), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
