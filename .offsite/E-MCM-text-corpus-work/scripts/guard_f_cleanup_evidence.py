"""Snapshot/check original PDFs, protected learning inputs and reader receipts."""
import argparse
import hashlib
import json
from pathlib import Path

WORK = Path(r"F:\MCM\mcm-skill-work")
STORE = Path(r"E:\MCM-text-corpus-work\artifacts\text-corpus")
OUT = Path(r"E:\MCM-text-corpus-work\archives\F-MCM-obsolete-generations-20261031-v4")


def sha(path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def write_new(path, value):
    with path.open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2)


def snapshot():
    native = WORK / "artifacts/text-corpus/native-20261029-v1"
    legacy = json.loads((native / "legacy-preimages.json").read_text(encoding="utf-8"))
    bindings = {str(WORK / relative): expected for relative, expected in legacy.items()}
    scope = json.loads((native / "scope.json").read_text(encoding="utf-8"))
    source = Path(scope["source_root"])
    pdfs = {}
    with (WORK / "artifacts/corpus/manifest.jsonl").open(encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            pdfs[str(source / row["relative_path"])] = row["sha256"]
    bindings.update(pdfs)
    reader_files = 0
    for base in (WORK / "artifacts/text-corpus/reading-runs", STORE / "reading-runs"):
        for path in base.rglob("*"):
            if path.is_file():
                bindings[str(path)] = sha(path)
                reader_files += 1
    for name in ("history.jsonl", "current-protocol-compliance.json", "current-language-priority-drift.json"):
        p = WORK / "artifacts/transactions" / name
        bindings[str(p)] = sha(p)
    bindings[str(WORK / "artifacts/progress.jsonl")] = sha(WORK / "artifacts/progress.jsonl")
    for name in ("reflow-20261031-v46", "reflow-20261031-v48", "reflow-20261031-v49"):
        for file in ("catalog.json", "scope.json", "corpus.sqlite3"):
            p = STORE / name / file
            bindings[str(p)] = sha(p)
    errors = [path for path, expected in bindings.items() if sha(Path(path)) != expected]
    if errors:
        raise ValueError(f"Pre-cleanup protected input mismatch: {errors[:3]}")
    write_new(OUT / "preservation-before.json", {"bindings": bindings, "legacy_count": len(legacy),
              "source_pdfs": len(pdfs), "reader_files": reader_files})
    print(json.dumps({"pass": True, "legacy_inputs": len(legacy), "source_pdfs": len(pdfs),
                      "reader_files": reader_files, "bindings": len(bindings)}), flush=True)


def check():
    before = json.loads((OUT / "preservation-before.json").read_text(encoding="utf-8"))
    errors = [path for path, expected in before["bindings"].items()
              if not Path(path).is_file() or sha(Path(path)) != expected]
    kept_documents = 0
    for name in ("native-20261029-v1", "reflow-20261030-v16"):
        root = WORK / "artifacts/text-corpus" / name
        catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
        if len(catalog["papers"]) != 435:
            errors.append(str(root) + ": expected435papers")
        for paper in catalog["papers"]:
            relative = paper["document"]
            if not (root / relative).is_file() or sha(root / relative) != paper["files"][relative]:
                errors.append(str(root / relative))
            kept_documents += 1
        expected = catalog.get("sqlite_sha256")
        if expected and sha(root / "corpus.sqlite3") != expected:
            errors.append(str(root / "corpus.sqlite3"))
    result = {k: v for k, v in before.items() if k != "bindings"}
    result.update(pass_=not errors, binding_count=len(before["bindings"]), retained_database_documents_checked=kept_documents, errors=errors)
    write_new(OUT / "preservation-after.json", result)
    print(json.dumps(result), flush=True)
    if errors:
        raise ValueError("Protected source/history/reader bytes changed")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("snapshot", "check"))
    {"snapshot": snapshot, "check": check}[p.parse_args().action]()
