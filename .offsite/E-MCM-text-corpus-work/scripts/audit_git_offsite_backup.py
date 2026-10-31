"""Read-only Git backup readiness inventory; never emit credentials or file bodies."""
import collections
import json
import os
from pathlib import Path
import subprocess
import urllib.parse

ROOT = Path(r"F:\MCM")
OUT = Path(r"E:\MCM-text-corpus-work\artifacts\git-offsite-backup-20261031-v1")


def git(*args, check=True):
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if check and result.returncode:
        raise RuntimeError("Git diagnostic failed: " + " ".join(args))
    return result.stdout


def write(name, value):
    with (OUT / name).open("x", encoding="utf-8") as output:
        json.dump(value, output, ensure_ascii=False, indent=2)


def main():
    OUT.mkdir(exist_ok=False)
    remotes = []
    for name in git("remote").decode().splitlines():
        for raw in git("remote", "get-url", "--all", name).decode().splitlines():
            url = urllib.parse.urlsplit(raw)
            remotes.append({"name": name, "host": url.hostname, "path": url.path,
                            "credentials_embedded": bool(url.username or url.password)})
    tracked = {p.decode("utf-8") for p in git("ls-files", "-z").split(b"\0") if p}
    untracked = {p.decode("utf-8") for p in git("ls-files", "--others", "--exclude-standard", "-z").split(b"\0") if p}
    groups = collections.defaultdict(lambda: {"files": 0, "bytes": 0, "tracked": 0})
    files = []
    large_pending = []
    for relative in sorted(tracked | untracked):
        path = ROOT / relative
        if not path.is_file():
            continue
        info = path.stat()
        row = {"path": relative, "bytes": info.st_size, "tracked": relative in tracked}
        files.append(row)
        parts = relative.split("/")
        key = "/".join(parts[:min(3, len(parts)-1)]) or "root-files"
        group = groups[key]
        group["files"] += 1
        group["bytes"] += info.st_size
        group["tracked"] += relative in tracked
        if info.st_size >= 50 * 1024**2:
            large_pending.append(row)
    write("working-files.json", files)
    print(json.dumps({"working_files": len(files), "working_bytes": sum(r["bytes"] for r in files),
                      "untracked_files": len(untracked), "large_pending": large_pending}), flush=True)
    object_lines = git("-c", "core.quotepath=false", "rev-list", "--objects", "--all").decode("utf-8").splitlines()
    object_paths = {}
    for line in object_lines:
        oid, _, path = line.partition(" ")
        object_paths.setdefault(oid, path)
    batch = "\n".join(object_paths) + "\n"
    result = subprocess.run(["git", "-C", str(ROOT), "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize) %(objectsize:disk)"],
                            input=batch.encode("ascii"), capture_output=True, check=True)
    objects = []
    for line in result.stdout.decode("ascii").splitlines():
        oid, kind, size, stored = line.split()
        objects.append({"oid": oid, "type": kind, "bytes": int(size), "stored_bytes": int(stored), "path": object_paths[oid]})
    write("reachable-objects.json", objects)
    refs = git("for-each-ref", "--format=%(refname) %(objectname)").decode().splitlines()
    report = {
        "root": str(ROOT), "remotes": remotes, "head": git("rev-parse", "HEAD").decode().strip(),
        "head_tree": git("rev-parse", "HEAD^{tree}").decode().strip(), "refs": refs,
        "reachable_commits": int(git("rev-list", "--count", "--all")),
        "reachable_objects": len(objects), "reachable_blob_bytes": sum(r["bytes"] for r in objects if r["type"] == "blob"),
        "reachable_stored_bytes": sum(r["stored_bytes"] for r in objects),
        "history_blobs_over_100MiB": [r for r in objects if r["type"] == "blob" and r["bytes"] > 100 * 1024**2],
        "working_files": len(files), "working_bytes": sum(r["bytes"] for r in files),
        "untracked_files": len(untracked), "large_pending": large_pending,
        "largest_groups": [{"path": k, **v} for k, v in sorted(groups.items(), key=lambda x: x[1]["bytes"], reverse=True)[:20]],
        "git_dir_bytes": sum(p.stat().st_size for p in (ROOT / ".git").rglob("*") if p.is_file()),
    }
    write("readiness.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
