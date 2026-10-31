"""Read-only inventory of remaining F:/MCM; write bounded, generated audit reports."""
import collections
import heapq
import json
import os
from pathlib import Path
import stat
import subprocess

ROOT = Path(r"F:\MCM")
OUT = Path(r"E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5")


def main():
    OUT.mkdir(exist_ok=False)
    tracked_raw = subprocess.check_output(["git", "-C", str(ROOT), "ls-files", "-z"])
    tracked = {p.decode("utf-8").replace("\\", "/").casefold()
               for p in tracked_raw.split(b"\0") if p}
    groups = collections.defaultdict(lambda: [0, 0, 0, 0])
    extensions = collections.defaultdict(lambda: [0, 0])
    caches = collections.defaultdict(lambda: [0, 0, 0])
    largest = []
    skipped = []
    errors = []
    with (OUT / "inventory.jsonl").open("x", encoding="utf-8") as output:
        stack = [ROOT]
        while stack:
            directory = stack.pop()
            try:
                entries = list(os.scandir(directory))
            except OSError as exc:
                errors.append({"path": str(directory), "error": str(exc)})
                continue
            for entry in entries:
                info = entry.stat(follow_symlinks=False)
                if info.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                    skipped.append(entry.path)
                    continue
                if entry.is_dir(follow_symlinks=False):
                    stack.append(Path(entry.path))
                    continue
                relative = Path(entry.path).relative_to(ROOT).as_posix()
                parts = relative.split("/")
                size = info.st_size
                is_tracked = relative.casefold() in tracked
                row = {"path": relative, "bytes": size, "mtime_ns": info.st_mtime_ns,
                       "tracked": is_tracked, "links": info.st_nlink}
                output.write(json.dumps(row, ensure_ascii=False) + "\n")
                for depth in range(min(5, len(parts))):
                    key = "/".join(parts[:depth]) if depth else "TOTAL"
                    data = groups[key]
                    data[0] += 1
                    data[1] += size
                    data[2] += is_tracked
                    data[3] += size if is_tracked else 0
                category = "other"
                for prefix in ("mcm-skill-work/tmp/", "mcm-skill-work/artifacts/papers/",
                               "mcm-skill-work/artifacts/text-corpus/"):
                    if relative.startswith(prefix):
                        category = prefix.rstrip("/")
                        break
                ext = Path(entry.name).suffix.lower()
                extensions[category + " " + ext][0] += 1
                extensions[category + " " + ext][1] += size
                for i, component in enumerate(parts[:-1]):
                    if component in ("__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"):
                        cache = caches["/".join(parts[:i+1])]
                        cache[0] += 1
                        cache[1] += size
                        cache[2] += is_tracked
                        break
                if parts[0] != ".git":
                    heapq.heappush(largest, (size, relative))
                    if len(largest) > 25:
                        heapq.heappop(largest)
    def rows(items):
        return [{"path": key, "files": v[0], "bytes": v[1],
                 "tracked_files": v[2], "tracked_bytes": v[3]}
                for key, v in sorted(items, key=lambda x: x[1][1], reverse=True)]
    report = {
        "total": rows([(k, v) for k, v in groups.items() if k == "TOTAL"])[0],
        "tmp_largest_children": rows([(k, v) for k, v in groups.items()
            if k.startswith("mcm-skill-work/tmp/") and k.count("/") == 2])[:25],
        "corpus_children": rows([(k, v) for k, v in groups.items()
            if k.startswith("mcm-skill-work/artifacts/text-corpus/") and k.count("/") == 3]),
        "largest_files": [{"bytes": size, "path": path} for size, path in sorted(largest, reverse=True)],
        "extensions": [{"group": k, "files": v[0], "bytes": v[1]}
                       for k, v in sorted(extensions.items(), key=lambda x: x[1][1], reverse=True)[:25]],
        "caches": [{"path": k, "files": v[0], "bytes": v[1], "tracked_files": v[2]}
                   for k, v in caches.items()],
        "reparse_skipped": skipped, "errors": errors,
    }
    with (OUT / "inventory-summary.json").open("x", encoding="utf-8") as output:
        json.dump(report, output, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
