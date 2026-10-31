"""Create-only source-bound page/proxy evidence for prose boundary review.

Rendering does not perform formula verification or figure/chart interpretation.
Only the bounded JPEG may be delivered to a model; the PNG stays on disk.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf

from corpus_reader import Catalog
from make_review_proxy import main as proxy_main
from text_corpus import file_hash, json_new, read_json, write_new


def prepare(root: Path, queue: int, pages: list[int], output: Path):
    catalog = Catalog(root); scope = read_json(root / "scope.json")
    records = [p for p in catalog.papers if p["queue_position"] == queue]
    if len(records) != 1 or len(set(pages)) != len(pages) or not pages:
        raise ValueError("Exactly one paper and distinct pages required")
    paper = records[0]; document = catalog.document(paper["paper_id"])
    if any(p < 1 or p > document["page_count"] for p in pages):
        raise ValueError("Physical page outside source")
    if output.exists():
        raise ValueError("Review evidence directory exists; never overwrite")
    source = Path(scope["source_root"]) / document["source_relative_path"]
    if file_hash(source) != document["source_sha256"]:
        raise ValueError("Source PDF hash differs")
    output.mkdir(parents=True)
    evidence = []
    with pymupdf.open(source) as pdf:
        for number in pages:
            png = output / f"page-{number:04d}.png"; jpg = png.with_suffix(".jpg")
            write_new(png, pdf[number-1].get_pixmap(dpi=200, alpha=False).tobytes("png"))
            proxy_main(["--input", str(png), "--output", str(jpg), "--max-bytes", "450000"])
            evidence.append({"physical_page": number, "raw_png": png.name, "raw_sha256": file_hash(png),
                             "proxy": jpg.name, "proxy_sha256": file_hash(jpg), "bytes": jpg.stat().st_size})
    manifest = {"dataset_id": catalog.identity, "paper_id": document["paper_id"],
                "source_sha256": document["source_sha256"], "raw_pages_sha256": document["raw_pages_sha256"],
                "purpose": "prose and paragraph/section boundaries only", "pages": evidence,
                "formula_verification": "paused", "figure_distillation": "paused"}
    json_new(output / "manifest.json", manifest)
    return manifest


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus-root", type=Path, required=True); p.add_argument("--queue", type=int, required=True)
    p.add_argument("--pages", type=int, nargs="+", required=True); p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    prepare(args.corpus_root.resolve(), args.queue, args.pages, args.output.resolve())
