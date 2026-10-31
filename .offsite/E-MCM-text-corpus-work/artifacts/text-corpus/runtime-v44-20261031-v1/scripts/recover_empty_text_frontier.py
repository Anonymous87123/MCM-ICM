"""Resume local OCR for EVERY native-empty page in the frozen corpus queue.

OCR outputs remain unverified evidence; this never changes a corpus, reading
receipt, old artifact or formula/figure review status. Failed attempts survive.
"""
from __future__ import annotations

import argparse
import json
import uuid
from pathlib import Path

from corpus_reader import Catalog
from recover_corpus_text_ocr import recover
from text_corpus import encoded, file_hash, json_new, read_json


def frontier(catalog):
    records = []
    for paper in catalog.papers:
        doc = catalog.document(paper["paper_id"])
        pages = sorted({d["page"] for d in doc.get("defects", [])
                        if d["code"] == "native_text_empty_ocr_required" and d.get("status") != "resolved"})
        if pages:
            records.append({"paper_id": doc["paper_id"], "queue_position": paper["queue_position"],
                            "source_sha256": doc["source_sha256"], "raw_pages_sha256": doc["raw_pages_sha256"],
                            "pages": pages})
    return {"schema_version": 1, "dataset_id": catalog.identity, "records": records,
            "paper_count": len(records), "page_count": sum(len(r["pages"]) for r in records)}


def completed_attempt(parent, record):
    completed = []
    for manifest in sorted(parent.glob("attempt-*/manifest.json")):
        value = read_json(manifest)
        if (value["paper_id"] != record["paper_id"] or value["source_sha256"] != record["source_sha256"] or
                [p["page"] for p in value["pages"]] != record["pages"]):
            raise ValueError("Completed OCR attempt differs from frozen frontier")
        for page in value["pages"]:
            path = (manifest.parent / page["path"]).resolve()
            if not path.is_relative_to(manifest.parent.resolve()) or file_hash(path) != page["sha256"]:
                raise ValueError("Completed OCR evidence modified")
        completed.append(manifest)
    if len(completed) > 1:
        raise ValueError("Multiple completed OCR attempts require explicit adjudication")
    return completed[0] if completed else None


def run(root: Path, output: Path, max_papers=None):
    catalog = Catalog(root); queue = frontier(catalog)
    if max_papers is not None and max_papers < 1:
        raise ValueError("max-papers must be positive")
    frozen = output / "queue.json"
    if frozen.exists():
        if frozen.read_bytes() != encoded(queue):
            raise ValueError("OCR frontier/version changed; create another queue directory")
    elif output.exists():
        raise ValueError("Existing output is not a frozen OCR queue")
    else:
        json_new(frozen, queue)
    new = 0; manifests = []
    for record in queue["records"]:
        parent = output / record["paper_id"]
        done = completed_attempt(parent, record)
        if not done:
            if max_papers is not None and new >= max_papers:
                continue
            number = 1
            while (parent / f"attempt-{number:04d}").exists():
                number += 1
            target = parent / f"attempt-{number:04d}"
            recover(root, record["paper_id"], record["pages"], target)
            done = completed_attempt(parent, record)
            new += 1
        manifests.append({"paper_id": record["paper_id"], "pages": record["pages"],
                          "path": str(done.relative_to(output)).replace("\\", "/"), "sha256": file_hash(done)})
        print(json.dumps({"completed_papers": len(manifests), "target_papers": queue["paper_count"],
                          "completed_pages": sum(len(m["pages"]) for m in manifests),
                          "target_pages": queue["page_count"], "source_review": "pending"}), flush=True)
    report = {"dataset_id": catalog.identity, "target_papers": queue["paper_count"],
              "target_pages": queue["page_count"], "completed_papers": len(manifests),
              "completed_pages": sum(len(m["pages"]) for m in manifests), "manifests": manifests,
              "meaning": "OCR evidence only; no source-fidelity or AI-reading acceptance",
              "formula_verification": "paused", "figure_distillation": "paused"}
    json_new(output / "reports" / (uuid.uuid4().hex + ".json"), report)
    return report


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus-root", type=Path, required=True); p.add_argument("--output", type=Path, required=True)
    p.add_argument("--max-papers", type=int)
    args = p.parse_args()
    run(args.corpus_root.resolve(), args.output.resolve(), args.max_papers)
