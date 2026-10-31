"""Derive a NEW section/paragraph generation from frozen native page evidence."""
from __future__ import annotations

import argparse
import json
import re
import copy
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import digest, encoded, export_document, file_hash, json_new, make_document, read_json, rows, section_text, write_new
from source_text_repairs import apply_text_repairs
from source_absence_reviews import apply_absence_reviews, prepare_absence_reviews,prepare_review_bundles
from source_layout_reviews import apply_layout_reviews
from source_span_metrics import prepare_flow_pages


def independent_key(text):
    # Only alphabetic presentation ligatures and whitespace; never normalize
    # arbitrary symbols/numbers or alter the canonical source text.
    table = dict(zip("\ufb00\ufb01\ufb02\ufb03\ufb04\ufb05\ufb06", ("ff", "fi", "fl", "ffi", "ffl", "st", "st")))
    return re.sub(r"\s+", "", "".join(table.get(c, c) for c in text))


def resolve_exact_comparisons(document, pages, independent_bytes):
    try:
        independent = independent_bytes.decode("utf-8", errors="strict").split("\f")
    except UnicodeError:
        return  # A decoding failure remains an open defect.
    for page in pages:
        index = page["page"] - 1
        if index >= len(independent) or page.get("ocr_status") == "candidate" or page.get("ocr_evidence"):
            continue
        native = "\n".join(line["text"] for line in page["lines"])
        if not independent_key(native) or independent_key(native) != independent_key(independent[index]):
            continue
        for defect in document["defects"]:
            if defect["code"] == "cross_engine_review" and defect["page"] == page["page"]:
                defect.update(status="resolved", resolution="whole-page independent text equality",
                              normalization="whitespace and alphabetic presentation ligatures only",
                              independent_bytes_sha256=digest(independent_bytes),
                              normalized_page_sha256=digest(independent_key(native).encode()))


def validate_exact_comparisons(document, pages, independent_bytes):
    resolved = [d for d in document.get("defects", []) if d.get("status") == "resolved" and
                d.get("resolution") == "whole-page independent text equality"]
    if not resolved:
        return
    try:
        independent = independent_bytes.decode("utf-8", errors="strict").split("\f")
        for defect in resolved:
            index = defect["page"]-1
            page = pages[index]
            native = "\n".join(line["text"] for line in page["lines"])
            key = independent_key(native)
            if (defect["code"] != "cross_engine_review" or page.get("ocr_status") == "candidate" or
                    page.get("ocr_evidence") or not key or
                    page["page"] != defect["page"] or key != independent_key(independent[index]) or
                    defect.get("independent_bytes_sha256") != digest(independent_bytes) or
                    defect.get("normalized_page_sha256") != digest(key.encode())):
                raise ValueError("Independent text resolution proof differs")
    except (UnicodeError, IndexError, KeyError) as exc:
        raise ValueError("Independent text resolution proof invalid") from exc


def apply_reviews(document, reviews):
    for review in reviews:
        if review["paper_id"] != document["paper_id"]:
            continue
        if (review["source_sha256"] != document["source_sha256"] or
                review["raw_pages_sha256"] != document["raw_pages_sha256"]):
            raise ValueError("Source review no longer binds this native generation")
        found = [s for s in document["sections"] if s["section_id"] == review["section_id"]]
        if len(found) != 1:
            raise ValueError("Reviewed section missing")
        section = found[0]
        if digest(section_text(document, [section["section_id"]]).encode()) != review["text_sha256"]:
            raise ValueError("Reviewed section text changed; re-review before promotion")
        previous = section["boundary_status"]
        section["boundary_status"] = "verified"; section["review"] = review
        if not Catalog.review_valid(document, section):
            section["boundary_status"] = previous
            raise ValueError("Incomplete source-fidelity review")
        for defect in document["defects"]:
            if defect["code"] == "section_boundary_pending" and defect["section_id"] == section["section_id"]:
                defect.update(status="resolved", resolution="source-bound explicit review", review_sha256=digest(encoded(review)))


def resegment(source: Path, output: Path, ocr_manifests=(), review_files=(), text_repair_files=(), absence_review_files=(), layout_review_files=(), span_metrics_root=None):
    catalog = Catalog(source)
    if output.exists():
        raise ValueError("Output exists; all derived generations are create-only")
    old_scope = read_json(source / "scope.json")
    scope = dict(old_scope)
    scope["parent_dataset_id"] = catalog.identity
    scope["input_sha256"] = {"library": file_hash(Path(__file__).with_name("text_corpus.py")),
                              "resegmenter": file_hash(Path(__file__))}
    scope["ocr_manifest_sha256"] = {str(p.resolve()): file_hash(p) for p in ocr_manifests}
    scope["source_review_sha256"] = {str(p.resolve()): file_hash(p) for p in review_files}
    scope["text_repair_sha256"] = {str(p.resolve()): file_hash(p) for p in text_repair_files}
    scope["absence_review_sha256"] = {str(p.resolve()):file_hash(p) for p in absence_review_files}
    scope["layout_review_sha256"] = {str(p.resolve()):file_hash(p) for p in layout_review_files}
    scope["input_sha256"]["text_repairs"] = file_hash(Path(__file__).with_name("source_text_repairs.py"))
    scope["input_sha256"]["absence_reviews"] = file_hash(Path(__file__).with_name("source_absence_reviews.py"))
    scope["input_sha256"]["layout_reviews"] = file_hash(Path(__file__).with_name("source_layout_reviews.py"))
    scope["input_sha256"]["queries"] = file_hash(Path(__file__).with_name("corpus_queries.py"))
    metrics_manifest=None
    if span_metrics_root is not None:
        metrics_manifest=read_json(span_metrics_root/'manifest.json')
        if (set(metrics_manifest['files'])!=set(catalog.by_id) or
                metrics_manifest['papers']!=scope['paper_count'] or
                metrics_manifest['physical_pages']!=scope['physical_page_count']):
            raise ValueError('Span metrics scope differs from corpus')
        scope['span_metrics_manifest_sha256']=file_hash(span_metrics_root/'manifest.json')
        scope['input_sha256']['span_flow']=file_hash(Path(__file__).with_name('source_span_metrics.py'))
        scope['input_sha256']['span_extractor']=file_hash(Path(__file__).with_name('extract_text_span_metrics.py'))
    reviews = [read_json(p) for p in review_files]
    repairs = [read_json(p) for p in text_repair_files]
    absence_reviews, absence_copies = prepare_absence_reviews(absence_review_files)
    layout_reviews, layout_copies = prepare_review_bundles(layout_review_files,identity_fields=("paper_id",),
            application_status="applied text reading lanes; not whole-section source acceptance")
    if any(review["paper_id"] not in catalog.by_id for review in absence_reviews):
        raise ValueError("Absence review paper is outside frozen scope")
    # Check evidence before creating the generation; portable copies live inside it.
    evidence_copies = {}
    for review in repairs:
        for proof in review["evidence"]:
            evidence = Path(proof["path"]).resolve()
            if not evidence.is_file() or file_hash(evidence) != proof["sha256"]:
                raise ValueError("Source-text repair evidence changed")
            rel = "inputs/text-repair-evidence/" + proof["sha256"] + evidence.suffix.lower()
            evidence_copies[rel] = evidence
            proof["path"] = rel
    if len({(r["paper_id"], r["section_id"]) for r in reviews}) != len(reviews):
        raise ValueError("Duplicate section reviews")
    overrides = {}
    for path in ocr_manifests:
        manifest = read_json(path)
        pid = manifest["paper_id"]
        paper = catalog.by_id.get(pid)
        if not paper or manifest["source_sha256"] != paper["source_sha256"]:
            raise ValueError("OCR evidence is for another source")
        for item in manifest["pages"]:
            pagefile = path.parent / item["path"]
            if file_hash(pagefile) != item["sha256"]:
                raise ValueError("OCR page evidence changed")
            key = (pid, item["page"])
            if key in overrides:
                raise ValueError("Duplicate OCR override")
            overrides[key] = (manifest, pagefile)
    scope["scope_id"] = digest(encoded({"parent": catalog.identity, "inputs": scope["input_sha256"],
                                       "ocr": scope["ocr_manifest_sha256"], "reviews": scope["source_review_sha256"],
                                       "text_repairs": scope["text_repair_sha256"],
                                       "absence_reviews": scope["absence_review_sha256"],
                                       "layout_reviews": scope["layout_review_sha256"],
                                       **({'span_metrics':scope['span_metrics_manifest_sha256']} if metrics_manifest else {})}))
    output.mkdir(parents=True)
    json_new(output / "scope.json", scope)
    for name in ("legacy-preimages.json",):
        write_new(output / name, (source / name).read_bytes())
    for path in (source / "inputs").rglob("*"):
        if path.is_file():
            write_new(output / "inputs/native-generation" / path.relative_to(source / "inputs"), path.read_bytes())
    write_new(output / "inputs/text_corpus.py", Path(__file__).with_name("text_corpus.py").read_bytes())
    write_new(output / "inputs/resegment_text_corpus.py", Path(__file__).read_bytes())
    write_new(output / "inputs/source_text_repairs.py", Path(__file__).with_name("source_text_repairs.py").read_bytes())
    write_new(output / "inputs/source_absence_reviews.py",Path(__file__).with_name("source_absence_reviews.py").read_bytes())
    write_new(output / "inputs/source_layout_reviews.py",Path(__file__).with_name("source_layout_reviews.py").read_bytes())
    write_new(output / "inputs/corpus_queries.py",Path(__file__).with_name("corpus_queries.py").read_bytes())
    if metrics_manifest:
        for name in ('source_span_metrics.py','extract_text_span_metrics.py'):
            write_new(output/'inputs'/name,Path(__file__).with_name(name).read_bytes())
        write_new(output/'inputs/span-metrics/manifest.json',(span_metrics_root/'manifest.json').read_bytes())
    for rel,(source_path,sha) in {**absence_copies,**layout_copies}.items():
        data=source_path.read_bytes()
        if digest(data) != sha:
            raise ValueError("Absence evidence changed during build")
        write_new(output/rel,data)
    for i,review in enumerate(absence_reviews):
        json_new(output/"inputs/absence-reviews"/f"{i:04d}.json",review)
    for i,review in enumerate(layout_reviews):
        json_new(output/"inputs/layout-reviews"/f"{i:04d}.json",review)
    for rel, evidence in evidence_copies.items():
        write_new(output / rel, evidence.read_bytes())
    for i, review in enumerate(repairs):
        json_new(output / "inputs/text-repairs" / f"{i:04d}.json", review)
    for i, review in enumerate(reviews):
        json_new(output / "inputs/source-reviews" / f"{i:04d}.json", review)
    for paper in catalog.papers:
        pid = paper["paper_id"]; old = catalog.document(pid); target = output / "papers" / pid
        old_folder = source / "papers" / pid
        for rel in ("raw/pages.jsonl", "raw/pdftotext.bin"):
            if file_hash(old_folder / rel) != paper["files"][f"papers/{pid}/{rel}"]:
                raise ValueError("Native evidence changed")
            if rel != "raw/pages.jsonl":
                write_new(target / rel, (old_folder / rel).read_bytes())
        pages = rows(old_folder / "raw/pages.jsonl")
        native_raw = (old_folder / "raw/pages.jsonl").read_bytes()
        for page in pages:
            key = (pid, page["page"])
            if key not in overrides:
                continue
            manifest, pagefile = overrides[key]
            ocr = read_json(pagefile)
            write_new(target / "raw/ocr" / pagefile.name, pagefile.read_bytes())
            for original in page["lines"]:
                original["superseded_by_ocr"] = True
            ocrlines = []
            for n, value in enumerate(ocr["lines"]):
                points = value["pdf_box"]
                box = [min(p[0] for p in points), min(p[1] for p in points),
                       max(p[0] for p in points), max(p[1] for p in points)]
                text = value["text"]
                size = max(5, (box[3]-box[1])*.95)
                ocrlines.append({"line_id": f"p{page['page']:04d}-ocr-l{n:04d}", "native_block": -1,
                                 "page": page["page"], "bbox": box, "text": text, "font_size": size,
                                 "bold": text.strip().lower() in {"summary", "abstract", "introduction", "contents"},
                                 "spans": [], "ocr_score": value["score"], "engine": "rapidocr"})
            page["lines"] += ocrlines
            page["ocr_status"] = "candidate"
            page["ocr_evidence"] = {"path": f"raw/ocr/{pagefile.name}", "sha256": file_hash(pagefile),
                                    "models": manifest["model_sha256"], "version": manifest["ocr_version"]}
        raw = b"".join((json.dumps(p, ensure_ascii=True, sort_keys=True)+"\n").encode() for p in pages)
        write_new(target / "raw/pages.jsonl", raw)
        write_new(target / "raw/parent-pages.jsonl", native_raw)
        keys = ("paper_id", "problem_type", "year", "queue_position", "page_count", "source_relative_path",
                "source_sha256", "raw_pages_sha256", "independent_page_count")
        meta = {k: old[k] for k in keys}; meta["scope_id"] = scope["scope_id"]
        meta["parent_raw_pages_sha256"] = old["raw_pages_sha256"]
        meta["raw_pages_sha256"] = digest(raw)
        flow=None
        if metrics_manifest:
            evidence_folder=span_metrics_root/'papers'/pid
            if file_hash(evidence_folder/'COMPLETE.json')!=metrics_manifest['files'][pid]:
                raise ValueError('Frozen span metrics paper changed')
            flow_pages,flow=prepare_flow_pages(meta,pages,span_metrics_root)
            for name in ('COMPLETE.json','span-metrics.jsonl'):
                write_new(output/'inputs/span-metrics/papers'/pid/name,(evidence_folder/name).read_bytes())
        else:
            flow_pages=copy.deepcopy(pages)
        applied_layout=apply_layout_reviews(meta,flow_pages,layout_reviews)
        document = make_document(meta, flow_pages, improved=True)
        if flow is not None:
            document['span_origin_flow']={'schema':flow['schema'],'metrics_sha256':flow['metrics_sha256'],
                'changed_lines':len(flow['changed_lines']),'source_fidelity_approved':False}
        if applied_layout:
            document["layout_reviews"]=applied_layout
        resolve_exact_comparisons(document, pages, (old_folder / "raw/pdftotext.bin").read_bytes())
        apply_text_repairs(document, repairs)
        apply_reviews(document, reviews)
        apply_absence_reviews(document,absence_reviews)
        export_document(target, document)
        files = {str(p.relative_to(target)).replace("\\", "/"): file_hash(p) for p in target.rglob("*") if p.is_file()}
        summary = {"paper_id": pid, "queue_position": old["queue_position"], "pages": old["page_count"],
                   "sections": len(document["sections"]), "blocks": len(document["blocks"]),
                   "defects": len(document["defects"]), "status": "machine-draft"}
        json_new(target / "COMPLETE.json", {"scope_id": scope["scope_id"], "files": files, "summary": summary})
        if old["queue_position"] % 25 == 0:
            print(json.dumps(summary), flush=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True); p.add_argument("--output", type=Path, required=True)
    p.add_argument("--ocr-manifest", type=Path, action="append", default=[])
    p.add_argument("--source-review", type=Path, action="append", default=[])
    p.add_argument("--text-repair", type=Path, action="append", default=[])
    p.add_argument("--absence-review",type=Path,action="append",default=[])
    p.add_argument("--layout-review",type=Path,action="append",default=[])
    p.add_argument('--span-metrics-root',type=Path)
    args = p.parse_args()
    resegment(args.input.resolve(), args.output.resolve(), args.ocr_manifest, args.source_review, args.text_repair,args.absence_review,args.layout_review,args.span_metrics_root)
