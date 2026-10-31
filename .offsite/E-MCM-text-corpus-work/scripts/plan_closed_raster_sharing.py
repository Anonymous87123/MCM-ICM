"""Find identical immutable closed-paper PNG copies, preserving all existing paths."""
import hashlib
import json
from pathlib import Path
import re
import stat

ROOT = Path(r"F:\MCM")
WORK = ROOT / "mcm-skill-work"
OUT = Path(r"E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5")


def sha(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def safe(path):
    for part in (path, *path.parents):
        if part.stat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            raise ValueError(f"Reparse point: {part}")
        if part == ROOT:
            return
    raise ValueError("Outside F:/MCM")


def main():
    progress = {r["paper_id"]: r for r in map(json.loads, (WORK / "artifacts/progress.jsonl").open(encoding="utf-8"))}
    deleted = {r["path"] for r in json.loads((OUT / "f-delete-plan.json").read_text(encoding="utf-8"))["files"]}
    pairs = []
    distinct = set()
    for line in (OUT / "inventory.jsonl").open(encoding="utf-8"):
        row = json.loads(line)
        parts = row["path"].split("/")
        if row["path"] in deleted or row["tracked"] or len(parts) != 6:
            continue
        if parts[:2] != ["mcm-skill-work", "tmp"] or not re.fullmatch(r"q\d+-extraction(?:-final)?(?:-v\d+)?", parts[2]):
            continue
        if parts[4] != "rendered" or not re.fullmatch(r"page-\d+\.png", parts[5]):
            continue
        paper_id = parts[3]
        if progress.get(paper_id, {}).get("status") != "closed":
            continue
        target = ROOT / row["path"]
        source = WORK / "artifacts/papers" / paper_id / "rendered" / parts[5]
        if not target.is_file() or not source.is_file() or target.stat().st_size != source.stat().st_size:
            continue
        safe(target)
        safe(source)
        ti, si = target.stat(), source.stat()
        if ti.st_ino == si.st_ino and ti.st_dev == si.st_dev:
            continue
        digest = sha(target)
        if sha(source) != digest:
            continue
        distinct.add((ti.st_dev, ti.st_ino))
        pairs.append({"target": str(target), "canonical": str(source), "sha256": digest,
                      "bytes": ti.st_size, "original_links": ti.st_nlink})
    with (OUT / "closed-raster-sharing-plan.json").open("x", encoding="utf-8") as output:
        json.dump(pairs, output, indent=2)
    print(json.dumps({"identical_png_pairs": len(pairs), "distinct_original_files": len(distinct),
                      "duplicate_logical_bytes": sum(r["bytes"] for r in pairs), "paths_deleted": 0}), flush=True)


if __name__ == "__main__":
    main()
