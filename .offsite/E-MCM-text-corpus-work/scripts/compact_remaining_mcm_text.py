"""Lossless NTFS compression of generated text; retain every path and SHA-256."""
import ctypes
import argparse
from ctypes import wintypes
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import time

ROOT = Path(r"F:\MCM")
OUT = Path(r"E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5")
kernel = ctypes.WinDLL("kernel32", use_last_error=True)
kernel.GetCompressedFileSizeW.argtypes = [wintypes.LPCWSTR, ctypes.POINTER(wintypes.DWORD)]
kernel.GetCompressedFileSizeW.restype = wintypes.DWORD


def allocation(path):
    high = wintypes.DWORD()
    ctypes.set_last_error(0)
    low = kernel.GetCompressedFileSizeW(str(path), ctypes.byref(high))
    if low == 0xFFFFFFFF and ctypes.get_last_error():
        raise ctypes.WinError(ctypes.get_last_error())
    return (high.value << 32) | low


def sha(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def eligible(relative):
    if Path(relative).suffix.lower() not in (".json", ".jsonl", ".bin", ".txt", ".md"):
        return False
    if relative.startswith("mcm-skill-work/tmp/"):
        return True
    for prefix in ("mcm-skill-work/artifacts/text-corpus/native-20261029-v1/",
                   "mcm-skill-work/artifacts/text-corpus/reflow-20261030-v16/",
                   "mcm-skill-work/artifacts/text-corpus/span-metrics-"):
        if relative.startswith(prefix):
            return True
    return False


def eligible_supplemental(relative):
    if Path(relative).suffix.lower() not in (".json", ".jsonl", ".txt", ".md"):
        return False
    prefix = "mcm-skill-work/artifacts/"
    if not relative.startswith(prefix):
        return False
    component = relative[len(prefix):].split("/", 1)[0]
    return component in {"language-units", "model-units", "learning-audits", "observations",
                         "language-layout-specs", "language-layout-drafts", "paper-cards",
                         "type-branches", "language-patterns", "layouts", "staging", "papers"}


def safe(path):
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Outside approved root: {path}")
    for part in (path, *path.parents):
        if part.stat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            raise ValueError(f"Reparse point: {part}")
        if part == ROOT:
            break


def main(supplemental=False):
    start = time.monotonic()
    output_root = OUT / "supplemental-text-compression" if supplemental else OUT
    if supplemental:
        output_root.mkdir(exist_ok=False)
    predicate = eligible_supplemental if supplemental else eligible
    groups = {}
    count = 0
    for line in (OUT / "inventory.jsonl").open(encoding="utf-8"):
        row = json.loads(line)
        if row["bytes"] < 65536 or not predicate(row["path"]):
            continue
        path = ROOT / row["path"]
        if not path.exists():
            continue  # Exact duplicate scratch was removed by the separate audited plan.
        safe(path)
        info = path.stat()
        if info.st_size != row["bytes"] or info.st_mtime_ns != row["mtime_ns"]:
            raise ValueError(f"Input changed since inventory: {path}")
        if info.st_file_attributes & stat.FILE_ATTRIBUTE_COMPRESSED:
            continue
        key = (info.st_dev, info.st_ino)
        if key not in groups:
            groups[key] = {"path": str(path), "all_paths": [], "bytes": info.st_size,
                           "inode": info.st_ino, "allocation_before": allocation(path)}
        groups[key]["all_paths"].append(str(path))
        count += 1
    rows = list(groups.values())
    print(json.dumps({"paths": count, "physical_files": len(rows), "logical_bytes": sum(r["bytes"] for r in rows)}), flush=True)
    with (output_root / "ntfs-compression-plan.json").open("x", encoding="utf-8") as output:
        json.dump(rows, output, indent=2)
    before = __import__("shutil").disk_usage(ROOT).free
    errors = []
    completed = []
    journal = (output_root / "ntfs-compression-journal.jsonl").open("x", encoding="utf-8")
    try:
        for offset in range(0, len(rows), 48):
            batch = rows[offset:offset+48]
            for row in batch:
                row["sha256"] = sha(Path(row["path"]))
                journal.write(json.dumps({"state": "PREPARE", **row}) + "\n")
            journal.flush()
            result = subprocess.run([r"C:\Windows\System32\compact.exe", "/C", "/A", "/Q",
                                     *(row["path"] for row in batch)], capture_output=True)
            for row in batch:
                path = Path(row["path"])
                if path.stat().st_ino != row["inode"] or sha(path) != row["sha256"]:
                    raise ValueError(f"SHA-256/identity mismatch after compression: {path}")
                row["allocation_after"] = allocation(path)
                row["compressed"] = bool(path.stat().st_file_attributes & stat.FILE_ATTRIBUTE_COMPRESSED)
                if not row["compressed"]:
                    errors.append(row["path"])
                journal.write(json.dumps({"state": "VERIFIED", **row}) + "\n")
                completed.append(row)
            journal.flush()
            if result.returncode:
                errors.append({"compact_returncode": result.returncode,
                               "message": (result.stderr or result.stdout)[-1200:].decode(errors="replace")})
            print(json.dumps({"verified": len(completed), "of": len(rows),
                              "saved_bytes": sum(r["allocation_before"] - r["allocation_after"] for r in completed),
                              "elapsed_seconds": round(time.monotonic()-start)}), flush=True)
    finally:
        journal.close()
    report = {"verified_unique_files": len(completed), "covered_paths": count,
              "source_logical_bytes": sum(r["bytes"] for r in rows),
              "reported_storage_before": sum(r["allocation_before"] for r in completed),
              "reported_storage_after": sum(r["allocation_after"] for r in completed),
              "free_before": before, "free_after": __import__("shutil").disk_usage(ROOT).free,
              "all_hashes_unchanged": True, "errors": errors}
    with (output_root / "ntfs-compression-completed.json").open("x", encoding="utf-8") as output:
        json.dump(report, output, indent=2)
    print(json.dumps(report), flush=True)
    if errors:
        raise ValueError("Some files were not compressed; see recorded errors")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--supplemental", action="store_true")
    main(parser.parse_args().supplemental)
