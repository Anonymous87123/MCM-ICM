"""Verify/restore the checksummed full-text backup from a Git checkout.

Restoration is create-only. It restores bytes, not NTFS compression/hardlinks.
By default verify-only does not allocate another corpus copy.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath


def safe_join(root, relative):
    part = PurePosixPath(relative)
    if part.is_absolute() or not part.parts or any(p in ("..", ".") or ":" in p or "\\" in p for p in part.parts):
        raise ValueError("Unsafe relative backup path")
    result = root.joinpath(*part.parts)
    if not result.resolve().is_relative_to(root.resolve()):
        raise ValueError("Backup path escapes its root")
    for node in (result, *result.parents):
        if node == root.parent:
            break
        if node.exists() and (node.is_symlink() or getattr(node.lstat(), "st_file_attributes", 0) & 1024):
            raise ValueError("Reparse-point backup path")
    return result


def verify_or_restore(checkout, manifest, destinations=None):
    results = {"files": 0, "bytes": 0, "split_files": 0}
    for row in manifest["files"]:
        target = None
        if destinations:
            target = safe_join(destinations[row["volume"]], row["relative_path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise FileExistsError(target)
        digest = hashlib.sha256()
        total = 0
        output = target.open("xb") if target else None
        try:
            parts = row.get("parts") or [{"path": row["path"], "sha256": row["sha256"], "bytes": row["bytes"]}]
            results["split_files"] += bool(row.get("parts"))
            for part in parts:
                source = safe_join(checkout, part["path"])
                part_digest = hashlib.sha256()
                part_bytes = 0
                with source.open("rb") as stream:
                    while data := stream.read(1024**2):
                        part_digest.update(data); digest.update(data)
                        total += len(data); part_bytes += len(data)
                        if output:
                            output.write(data)
                if part_digest.hexdigest() != part["sha256"] or part_bytes != part["bytes"]:
                    raise ValueError("Part checksum/size mismatch: " + part["path"])
            if digest.hexdigest() != row["sha256"] or total != row["bytes"]:
                raise ValueError("Full-file checksum/size mismatch: " + row["relative_path"])
        finally:
            if output:
                output.close()
        results["files"] += 1; results["bytes"] += total
        if results["files"] % 10000 == 0:
            print(json.dumps(results), flush=True)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=Path.cwd())
    parser.add_argument("--restore-to", type=Path, help="New, empty destination; omitted means verify only")
    args = parser.parse_args()
    checkout = args.checkout.resolve()
    manifest = json.loads((checkout / ".offsite/manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema") != "mcm-offsite-backup-v1":
        raise ValueError("Unknown backup schema")
    destinations = None
    if args.restore_to:
        base = args.restore_to.resolve()
        if base.exists():
            raise FileExistsError("Restoration requires a NEW destination")
        if base.is_relative_to(checkout) or checkout.is_relative_to(base):
            raise ValueError("Keep restoration and backup checkout separate")
        base.mkdir(parents=True, exist_ok=False)
        destinations = {name: base / name for name in manifest["volumes"]}
    result = verify_or_restore(checkout, manifest, destinations)
    print(json.dumps({"pass": True, "action": "restore" if destinations else "verify-only", **result}), flush=True)


if __name__ == "__main__":
    main()
