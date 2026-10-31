"""Archive only obsolete generated snapshots; never delete source files.

The companion PowerShell deletion step requires independent archive and current
source checks. Hardlinked content is stored once in the compressed tar stream.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tarfile
import time
import itertools
from types import SimpleNamespace

BASE = Path(r"F:\MCM\mcm-skill-work\artifacts")
OUT = Path(r"E:\MCM-text-corpus-work\archives\F-MCM-obsolete-generations-20261031-v4")
KEEP = {"native-20261029-v1", "reflow-20261030-v16"}
RESERVE = 20 * 1024**3
MAX_ARCHIVE = 12 * 1024**3


def dump_new(path: Path, value):
    with path.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")


def sha_file(path: Path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def safe(path: Path):
    absolute = Path(os.path.abspath(path))
    if not absolute.is_relative_to(BASE):
        raise ValueError(f"Outside artifact root: {absolute}")
    for item in (absolute, *absolute.parents):
        if item.exists() and getattr(item.lstat(), "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            raise ValueError(f"Refuse reparse point: {item}")
    return absolute


def roots():
    selected = []
    for folder in (BASE / "text-corpus").iterdir():
        if re.fullmatch(r"reflow-202610(?:29|30|31)-v\d+", folder.name) and folder.name not in KEEP:
            selected.append(safe(folder))
    for folder in (BASE / "skill-packages").iterdir():
        if re.fullmatch(r"text-corpus-preview-202610(?:29|30|31)-v\d+", folder.name):
            selected.append(safe(folder))
    if len(selected) != 49:
        raise ValueError(f"Expected exactly 32 obsolete generations + 17 packages, found {len(selected)}")
    if any(p.name in KEEP for p in selected):
        raise ValueError("Keep-set overlap")
    return sorted(selected)


def walk(root: Path):
    """Deterministic, non-following traversal; reject junctions and special files."""
    s = root.lstat()
    if getattr(s, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
        raise ValueError(f"Reparse entry: {root}")
    if not (stat.S_ISDIR(s.st_mode) or stat.S_ISREG(s.st_mode)):
        raise ValueError(f"Special file: {root}")
    yield root, s
    if stat.S_ISDIR(s.st_mode):
        with os.scandir(root) as entries:
            children = sorted(entries, key=lambda x: x.name)
        for child in children:
            yield from walk(Path(child.path))


def stamp(s):
    return [s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, stat.S_IFMT(s.st_mode)]


def tree_update(h, relative, s):
    h.update(json.dumps([relative, stamp(s)], separators=(",", ":")).encode())
    h.update(b"\n")


def derived_exports(root):
    """Reuse immutable catalog hashes only within their completed freeze time.

    All unique archived content is fully hashed and independently reverified.
    Files newer than their corpus/package manifest always take the full-read path.
    """
    prefix = ""
    corpus = root
    if root.parent.name == "skill-packages":
        prefix = "mcm-icm-master-skill/assets/text-corpus/"
        corpus = root / "mcm-icm-master-skill/assets/text-corpus"
    catalog = corpus / "catalog.json"
    if not catalog.exists():
        return {}, 0
    value = json.loads(catalog.read_text(encoding="utf-8"))
    hints = {}
    for paper in value.get("papers", []):
        for relative, digest in paper.get("files", {}).items():
            if relative.startswith("papers/") and re.fullmatch("[0-9a-f]{64}", digest):
                hints[prefix + relative] = digest
    frozen_time = catalog.stat().st_mtime_ns
    if root.parent.name == "skill-packages":
        # The copied catalog precedes the copied payload. The package manifest,
        # written AFTER copying and validation, is the package's freeze boundary.
        completed = root / "mcm-icm-master-skill/package-manifest.json"
        if completed.is_file():
            frozen_time = max(frozen_time, completed.stat().st_mtime_ns)
    return hints, frozen_time


def indexed(phase):
    with (OUT / f"source-{phase}.tsv").open(encoding="utf-8") as f:
        for line in f:
            root, relative, kind, length, ns = line.rstrip("\n").split("\t")
            ns = int(ns)
            s = SimpleNamespace(st_dev=0, st_ino=0, st_size=int(length), st_mtime_ns=ns,
                 st_mtime=ns // 10**9, st_mode=(stat.S_IFDIR | 0o777) if kind == "D" else (stat.S_IFREG | 0o666),
                 st_nlink=1, st_uid=0, st_gid=0)
            yield root, BASE / relative, s


def same_content_stamp(actual, expected):
    return (actual.st_size, actual.st_mtime_ns, stat.S_IFMT(actual.st_mode)) == (expected.st_size, expected.st_mtime_ns, stat.S_IFMT(expected.st_mode))


class HashReader:
    def __init__(self, f):
        self.f, self.h = f, hashlib.sha256()

    def read(self, size=-1):
        data = self.f.read(size)
        self.h.update(data)
        return data


def create():
    selected = roots()
    if not OUT.is_dir() or {p.name for p in OUT.iterdir()} != {"source-before.tsv"}:
        raise ValueError("Require only the freshly generated native source index")
    if shutil.disk_usage(OUT.parent.parent).free < RESERVE + 2 * 8 * 1024**3:
        raise ValueError("Insufficient archive budget")
    plan = {"schema": "obsolete-generated-archive-v1", "base": str(BASE),
            "roots": [str(p) for p in selected], "kept": sorted(KEEP),
            "source_deletion_performed": False}
    dump_new(OUT / "plan.json", plan)
    known = {}
    inodes = {}
    content = {}
    total_files = total_bytes = regular_bytes = links = entries = 0
    trees = {}
    start = time.monotonic()
    with (OUT / "obsolete.tar.gz").open("xb") as raw, \
            gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=1, mtime=0) as compressed, \
            tarfile.open(fileobj=compressed, mode="w|", format=tarfile.PAX_FORMAT,
                         dereference=False, copybufsize=1024**2) as tar, \
            gzip.open(OUT / "manifest.jsonl.gz", "xt", encoding="utf-8", compresslevel=1) as manifest:
        root_order = []
        for root_name, group in itertools.groupby(indexed("before"), key=lambda r: r[0]):
            root = Path(root_name)
            root_order.append(root)
            hints, catalog_time = derived_exports(root)
            h = hashlib.sha256()
            files = logical = root_entries = 0
            for _, path, before in group:
                relative = path.relative_to(BASE).as_posix()
                tree_update(h, relative, before)
                local = path.relative_to(root).as_posix()
                info = tarfile.TarInfo(relative)
                info.mode = stat.S_IMODE(before.st_mode)
                info.uid, info.gid = before.st_uid, before.st_gid
                # Fractional source timestamps are retained in the manifest.
                info.mtime = int(before.st_mtime)
                record = {"path": relative, "stamp": stamp(before), "bytes": 0}
                inode = (before.st_dev, before.st_ino)
                prior = inodes.get(inode) if before.st_nlink > 1 else None
                hint = hints.get(local) if before.st_mtime_ns <= catalog_time else None
                reused_export = False
                if prior is None and hint is not None and hint in content:
                    prior = content[hint]
                    reused_export = True
                if stat.S_ISDIR(before.st_mode):
                    info.type = tarfile.DIRTYPE
                    record["kind"] = "directory"
                    tar.addfile(info)
                elif prior is not None:
                    target, sha, length = prior
                    if length != before.st_size:
                        raise ValueError("Hardlink size mismatch")
                    info.type, info.linkname = tarfile.LNKTYPE, target
                    record.update(kind="hardlink", sha256=sha, bytes=length, target=target)
                    if reused_export:
                        record["reuse"] = "frozen-catalog-sha256-and-unchanged-mtime"
                    tar.addfile(info)
                    if before.st_nlink > 1:
                        inodes[inode] = prior
                    links += 1
                elif stat.S_ISREG(before.st_mode):
                    info.type, info.size = tarfile.REGTYPE, before.st_size
                    with path.open("rb") as f:
                        if not same_content_stamp(os.fstat(f.fileno()), before):
                            raise ValueError(f"Source changed before read: {path}")
                        reader = HashReader(f)
                        tar.addfile(info, reader)
                        sha = reader.h.hexdigest()
                        if not same_content_stamp(os.fstat(f.fileno()), before):
                            raise ValueError(f"Source changed during read: {path}")
                    record.update(kind="file", sha256=sha, bytes=before.st_size)
                    regular_bytes += before.st_size
                    item = (relative, sha, before.st_size)
                    content.setdefault(sha, item)
                    if before.st_nlink > 1:
                        inodes[inode] = item
                else:
                    raise ValueError(f"Unsupported archive member: {relative}")
                tar.members.clear()  # Do not retain a million TarInfo objects.
                manifest.write(json.dumps(record, ensure_ascii=True, separators=(",", ":")) + "\n")
                entries += 1
                root_entries += 1
                if record["kind"] != "directory":
                    files += 1
                    logical += before.st_size
                if entries % 20000 == 0:
                    print(f"ARCHIVE entries={entries} files={total_files+files} "
                          f"logicalGiB={(total_bytes+logical)/1024**3:.2f} "
                          f"storedGiB={raw.tell()/1024**3:.2f} seconds={time.monotonic()-start:.0f}", flush=True)
                    if raw.tell() > MAX_ARCHIVE or shutil.disk_usage(OUT).free < RESERVE:
                        raise ValueError("Archive exceeded explicit storage budget; sources untouched")
            trees[str(root)] = {"entries": root_entries, "files": files, "logical_bytes": logical,
                                "metadata_sha256": h.hexdigest()}
            total_files += files
            total_bytes += logical
            print(f"ROOT ARCHIVED {root.name} files={files}", flush=True)
        if root_order != selected:
            raise ValueError("Indexed root set/order differs")
    result = {"plan_sha256": sha_file(OUT / "plan.json"), "archive_sha256": sha_file(OUT / "obsolete.tar.gz"),
              "manifest_sha256": sha_file(OUT / "manifest.jsonl.gz"), "trees": trees,
              "files": total_files, "entries": entries, "logical_bytes": total_bytes,
              "regular_stored_bytes_before_compression": regular_bytes, "hardlink_entries": links,
              "archive_bytes": (OUT / "obsolete.tar.gz").stat().st_size,
              "source_deletion_performed": False}
    dump_new(OUT / "archive-created.json", result)
    print(json.dumps({k: v for k, v in result.items() if k != "trees"}), flush=True)


def records():
    with gzip.open(OUT / "manifest.jsonl.gz", "rt", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def verify():
    created = json.loads((OUT / "archive-created.json").read_text(encoding="utf-8"))
    for name, key in (("plan.json", "plan_sha256"), ("obsolete.tar.gz", "archive_sha256"),
                      ("manifest.jsonl.gz", "manifest_sha256")):
        if sha_file(OUT / name) != created[key]:
            raise ValueError(f"Frozen archive binding changed: {name}")
    targets = {r["target"] for r in records() if r["kind"] == "hardlink"}
    canon = {}
    count = files = logical = 0
    expected = iter(records())
    with tarfile.open(OUT / "obsolete.tar.gz", "r|gz", bufsize=1024**2, stream=True) as tar:
        for member in tar:
            r = next(expected)
            if member.name != r["path"]:
                raise ValueError("Member order/path differs from source manifest")
            if member.isdir():
                if r["kind"] != "directory":
                    raise ValueError("Directory mismatch")
            elif member.isreg():
                if r["kind"] != "file" or member.size != r["bytes"]:
                    raise ValueError("Regular member mismatch")
                data = tar.extractfile(member)
                actual = hashlib.file_digest(data, "sha256").hexdigest()
                if actual != r["sha256"]:
                    raise ValueError(f"Archived source bytes differ: {member.name}")
                if member.name in targets:
                    canon[member.name] = (actual, member.size)
            elif member.islnk():
                if (r["kind"] != "hardlink" or member.linkname != r["target"] or
                        canon.get(member.linkname) != (r["sha256"], r["bytes"])):
                    raise ValueError("Unverified hardlink target")
            else:
                raise ValueError("Unsupported archive type")
            count += 1
            if not member.isdir():
                files += 1
                logical += r["bytes"]
            if count % 100000 == 0:
                print(f"VERIFY entries={count} files={files}", flush=True)
    if next(expected, None) is not None or (count, files, logical) != (created["entries"], created["files"], created["logical_bytes"]):
        raise ValueError("Archive coverage mismatch")
    dump_new(OUT / "archive-verified.json", {"pass": True, "files": files, "entries": count,
             "logical_bytes": logical, "archive_sha256": created["archive_sha256"],
             "manifest_sha256": created["manifest_sha256"], "plan_sha256": created["plan_sha256"]})
    print(f"PASS archive verified files={files} entries={count}", flush=True)


def check_sources():
    created = json.loads((OUT / "archive-created.json").read_text(encoding="utf-8"))
    verified = json.loads((OUT / "archive-verified.json").read_text(encoding="utf-8"))
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    if not verified["pass"] or sha_file(OUT / "plan.json") != verified["plan_sha256"]:
        raise ValueError("Verified archive required")
    if [str(p) for p in roots()] != plan["roots"]:
        raise ValueError("Current target set changed")
    checked = []
    for name, group in itertools.groupby(indexed("after"), key=lambda r: r[0]):
        checked.append(name)
        h = hashlib.sha256()
        count = files = logical = 0
        safe(Path(name))
        for _, path, s in group:
            tree_update(h, path.relative_to(BASE).as_posix(), s)
            count += 1
            if stat.S_ISREG(s.st_mode):
                files += 1
                logical += s.st_size
        actual = {"entries": count, "files": files, "logical_bytes": logical, "metadata_sha256": h.hexdigest()}
        if actual != created["trees"][name]:
            raise ValueError(f"Source changed since archived: {name}")
        print(f"SOURCE UNCHANGED {Path(name).name}", flush=True)
    if checked != plan["roots"]:
        raise ValueError("After-index roots differ")
    dump_new(OUT / "sources-unchanged.json", {"pass": True, "roots": plan["roots"],
             "plan_sha256": verified["plan_sha256"], "archive_sha256": verified["archive_sha256"]})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("create", "verify", "check-sources"))
    action = parser.parse_args().action
    {"create": create, "verify": verify, "check-sources": check_sources}[action]()
