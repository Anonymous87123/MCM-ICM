"""Create local OCR evidence for specified pages; never alter the native corpus.

This recovers text only. It neither interprets figures nor verifies equations.
"""
from __future__ import annotations

import argparse
import importlib.metadata
import importlib.util
import json
from pathlib import Path

from text_corpus import file_hash, json_new, read_json


def recover(root: Path, pid: str, pages: list[int], output: Path, dpi=240) -> dict:
    import numpy as np
    import pymupdf
    from rapidocr import RapidOCR

    scope = read_json(root / "scope.json")
    matches = [r for r in scope["records"] if r["paper_id"] == pid]
    if len(matches) != 1:
        raise ValueError("Paper not uniquely in frozen scope")
    record = matches[0]
    if not pages or len(pages) != len(set(pages)) or any(p < 1 or p > record["page_count"] for p in pages):
        raise ValueError("Invalid/duplicate physical page")
    if output.exists():
        raise ValueError("OCR output exists; use a new evidence directory")
    source = Path(scope["source_root"]) / record["relative_path"]
    if file_hash(source) != record["sha256"]:
        raise ValueError("Source hash differs")
    models = Path(importlib.util.find_spec("rapidocr").origin).parent / "models"
    model_files = {"Det": models / "PP-OCRv6_det_small.onnx",
                   "Rec": models / "PP-OCRv6_rec_small.onnx",
                   "Cls": models / "ch_ppocr_mobile_v2.0_cls_mobile.onnx"}
    if any(not p.is_file() for p in model_files.values()):
        raise ValueError("Pinned local OCR models missing; refusing implicit download")
    params = {f"{stage}.model_path": str(path) for stage, path in model_files.items()}
    params.update({"Global.text_score": 0.0, "EngineConfig.onnxruntime.intra_op_num_threads": 2,
                   "EngineConfig.onnxruntime.inter_op_num_threads": 1})
    engine = RapidOCR(params=params)
    output.mkdir(parents=True)
    manifest = {"paper_id": pid, "source_sha256": record["sha256"], "scope_id": scope["scope_id"],
                "ocr_version": importlib.metadata.version("rapidocr"), "dpi": dpi,
                "model_sha256": {k: file_hash(v) for k, v in model_files.items()},
                "purpose": "text recovery only; formula verification and figure distillation paused",
                "pages": []}
    with pymupdf.open(source) as pdf:
        for number in sorted(pages):
            pix = pdf[number-1].get_pixmap(dpi=dpi, alpha=False, colorspace=pymupdf.csRGB)
            # In-memory raster only. No image bytes sent to an API or model context.
            image = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
            result = engine(image)
            values = []
            if result.txts is not None:
                for box, text, score in zip(result.boxes, result.txts, result.scores):
                    points = box.tolist()
                    values.append({"text": text, "score": float(score), "pixel_box": points,
                                   "pdf_box": [[x*72/dpi, y*72/dpi] for x, y in points]})
            record_page = {"page": number, "width_pixels": pix.width, "height_pixels": pix.height,
                           "lines": values, "review_status": "pending", "elapsed_seconds": float(result.elapse)}
            relative = f"page-{number:04d}.json"
            json_new(output / relative, record_page)
            manifest["pages"].append({"page": number, "path": relative, "sha256": file_hash(output / relative),
                                      "line_count": len(values), "low_confidence_lines": sum(v["score"] < .95 for v in values)})
            print(json.dumps({"paper_id": pid, **manifest["pages"][-1]}), flush=True)
    json_new(output / "manifest.json", manifest)
    return manifest


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus-root", type=Path, required=True)
    p.add_argument("--paper-id", required=True)
    p.add_argument("--pages", type=int, nargs="+", required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    recover(args.corpus_root.resolve(), args.paper_id, args.pages, args.output.resolve())
