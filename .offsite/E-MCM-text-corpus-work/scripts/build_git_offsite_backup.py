"""Freeze, scan, upload and verify the authorized MCM offsite snapshot.

No raw corpus copy, source editing, local-index editing or deletion is performed.
New Git objects live only in the explicitly budgeted E: bare staging repository.
"""
import argparse
import collections
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

F = Path(r"F:\MCM")
E = Path(r"E:\MCM-text-corpus-work")
OUT = E / "artifacts/git-offsite-backup-20261031-v1"
BARE = OUT / "upload.git"
REMOTE = "https://github.com/Anonymous87123/MCM-ICM.git"
BRANCH = "storage-backup-20261031-v1"
PARENT = "23fdab683cb57c4a070206ec35a74680d2ddcd14"
MAX_FILE = 100 * 1024**2
PART = 32 * 1024**2
BATCH = 384 * 1024**2
SELECTED_REFLOWS = {"reflow-20261031-v46", "reflow-20261031-v48", "reflow-20261031-v49"}
SKIP_TEXT_DIRS = {"package-smoke-20261031-v19", "package-smoke-run-20261031-v18"}


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)


def env():
    value = os.environ.copy()
    for name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES"):
        value.pop(name, None)
    value.update(GIT_ALTERNATE_OBJECT_DIRECTORIES=(F / ".git/objects").as_posix(),
                 GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
    return value


def git(*args, data=None, bare=True, check=True, timeout=600):
    command = ["git", "--git-dir=" + str(BARE)] if bare else ["git", "-C", str(F)]
    process = subprocess.run([*command, *args], input=data, capture_output=True,
                             env=env(), timeout=timeout)
    if check and process.returncode:
        raise RuntimeError("Git failed: " + " ".join(args) + "\n" + process.stderr.decode("utf-8", "replace")[-3000:])
    return process


def signature(path):
    stat = path.stat()
    if path.is_symlink() or getattr(stat, "st_file_attributes", 0) & 1024:
        raise ValueError("Reparse-point source not permitted: " + str(path))
    return [stat.st_size, stat.st_mtime_ns, stat.st_dev, stat.st_ino]


def walk(root):
    for current, dirs, files in os.walk(root, followlinks=False):
        current = Path(current)
        for name in dirs:
            node = current / name
            if node.is_symlink() or getattr(node.lstat(), "st_file_attributes", 0) & 1024:
                raise ValueError("Reparse-point directory: " + str(node))
        for name in files:
            yield current / name


def selected_files():
    tracked = {p.decode("utf-8") for p in git("ls-files", "-z", bare=False).stdout.split(b"\0") if p}
    others = {p.decode("utf-8") for p in git("ls-files", "--others", "--exclude-standard", "-z", bare=False).stdout.split(b"\0") if p}
    # Include frozen runtime files even where legacy Git ignores their bytecode.
    corpus = F / "mcm-skill-work/artifacts/text-corpus"
    full = {p.relative_to(F).as_posix() for p in walk(corpus)}
    for relative in sorted(tracked | others | full):
        node = F / relative
        if not node.is_file():
            raise ValueError("Tracked/current file disappeared: " + relative)
        if relative.startswith(".offsite/"):
            raise ValueError("Offsite namespace already used")
        yield "F-MCM", relative, relative, node
    for path in sorted(walk(E / "scripts")):
        if "__pycache__" not in path.parts and path.suffix != ".pyc":
            relative = path.relative_to(E).as_posix()
            yield "E-MCM-text-corpus-work", relative, ".offsite/E-MCM-text-corpus-work/" + relative, path
    store = E / "artifacts/text-corpus"
    for child in sorted(store.iterdir()):
        if child.is_dir() and ((child.name.startswith("reflow-") and child.name not in SELECTED_REFLOWS) or child.name in SKIP_TEXT_DIRS):
            continue
        nodes = walk(child) if child.is_dir() else (child,)
        for path in sorted(nodes):
            relative = path.relative_to(E).as_posix()
            yield "E-MCM-text-corpus-work", relative, ".offsite/E-MCM-text-corpus-work/" + relative, path
    for child in sorted((E / "artifacts").iterdir()):
        if child.is_dir() and child.name.startswith("storage-"):
            for path in sorted(walk(child)):
                relative = path.relative_to(E).as_posix()
                yield "E-MCM-text-corpus-work", relative, ".offsite/E-MCM-text-corpus-work/" + relative, path
    # Only completed cleanup evidence, never abandoned archive files.
    archive = E / "archives/F-MCM-obsolete-generations-20261031-v4"
    for path in sorted(walk(archive)):
        if path.name not in {"obsolete.tar.gz", "manifest.jsonl.gz"}:
            relative = path.relative_to(E).as_posix()
            yield "E-MCM-text-corpus-work", relative, ".offsite/E-MCM-text-corpus-work/" + relative, path


def source(row):
    return (F if row["volume"] == "F-MCM" else E) / row["relative_path"]


def load_scanner():
    spec = importlib.util.spec_from_file_location("local_secret_screen", E / "scripts/scan_git_backup_secrets.py")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


class HashReader:
    def __init__(self, stream, size):
        self.stream = stream
        self.sha = hashlib.sha256()
        self.oid = hashlib.sha1(("blob " + str(size) + "\0").encode("ascii"))
    def read(self, size):
        data = self.stream.read(size)
        self.sha.update(data); self.oid.update(data)
        return data


def prepare():
    if (OUT / "frozen-files.json").exists():
        raise FileExistsError("Freeze already exists; use its checkpoint")
    if git("rev-parse", "HEAD", bare=False).stdout.decode().strip() != PARENT:
        raise ValueError("Original Git HEAD changed")
    old_scan = json.loads((OUT / "secret-scan.json").read_text(encoding="utf-8"))
    if old_scan["finding_count"]:
        raise ValueError("Unresolved historical secret findings")
    scanner = load_scanner()
    cache = {}; files = []; findings = []; counts = collections.Counter()
    seen_paths = set()
    for volume, relative, mapped, path in selected_files():
        if mapped in seen_paths or any(c in mapped for c in ("\0", "\n", "\r", "\t")):
            raise ValueError("Duplicate/unsupported Git path")
        seen_paths.add(mapped)
        before = signature(path)
        key = tuple(before)
        if key not in cache:
            with path.open("rb") as raw:
                reader = HashReader(raw, before[0])
                # SQLite is screened too: it contains recovered author prose.
                if path.suffix.lower() not in scanner.BINARY or path.suffix.lower() in {".sqlite3", ".sqlite", ".db"}:
                    scanner.scan(reader, before[0], {"volume": volume, "path": relative}, findings)
                    counts["unique_sources_screened"] += 1
                else:
                    while reader.read(1024**2):
                        pass
            if signature(path) != before:
                raise ValueError("Source changed during freeze: " + mapped)
            cache[key] = (reader.sha.hexdigest(), reader.oid.hexdigest())
        sha, oid = cache[key]
        row = {"volume": volume, "relative_path": relative, "path": mapped,
               "bytes": before[0], "sha256": sha, "oid": oid, "signature": before}
        files.append(row); counts[volume + "_files"] += 1; counts[volume + "_bytes"] += before[0]
        if len(files) % 5000 == 0:
            print(json.dumps({"frozen_files": len(files), "unique_reads": len(cache), "findings": len(findings)}), flush=True)
    write_new(OUT / "new-content-secret-scan.json", {"findings": findings, "finding_count": len(findings), **counts,
              "limitation": "Pattern screening is not proof that arbitrary personal/private information is absent; user authorized complete paper-text publication."})
    if findings:
        raise ValueError("New content requires secret-finding review; no new content uploaded")
    write_new(OUT / "frozen-files.json", {"files": files, "counts": dict(counts), "parent": PARENT,
              "excluded": ["obsolete E reflows except46/48/49", "old preview packages", "abandoned archive streams", "private runtime/credentials and ignored temporary files outside frozen corpora"]})
    print(json.dumps({"pass": True, "freeze_files": len(files), **counts}), flush=True)


def init():
    if BARE.exists():
        raise FileExistsError(BARE)
    result = subprocess.run(["powershell.exe", "-NoProfile", "-File", str(E / "scripts/assert_corpus_storage_budget.ps1"),
                             "-OutputPath", str(BARE), "-EstimatedNewBytes", str(16 * 1024**3)], capture_output=True, check=True)
    write_new(OUT / "staging-storage-preflight.json", json.loads(result.stdout))
    subprocess.run(["git", "init", "--bare", str(BARE)], check=True, capture_output=True)
    for key, value in [("gc.auto", "0"), ("core.longpaths", "true"), ("pack.threads", "2"),
                       ("pack.windowMemory", "128m"), ("pack.packSizeLimit", "768m"),
                       ("user.name", git("config", "user.name", bare=False).stdout.decode().strip()),
                       ("user.email", git("config", "user.email", bare=False).stdout.decode().strip())]:
        git("config", key, value)
    git("remote", "add", "origin", REMOTE)
    git("read-tree", PARENT)
    git("update-ref", "refs/heads/" + BRANCH, PARENT)
    print(json.dumps({"pass": True, "bare_initialized": str(BARE)}), flush=True)


def hash_data(data):
    return git("hash-object", "-w", "--stdin", data=data).stdout.decode().strip()


def update_index(rows):
    data = b"".join(("100644 " + row["oid"] + "\t" + row["path"] + "\0").encode("utf-8") for row in rows)
    if data:
        git("update-index", "-z", "--index-info", data=data)


def checkpoint_path():
    return OUT / "upload-checkpoint.json"


def save_checkpoint(value):
    # Runtime checkpoint, not a frozen authoritative source; replace atomically.
    temp = OUT / "upload-checkpoint.next.json"
    write_new(temp, value)
    os.replace(temp, checkpoint_path())


def push(oid):
    process = git("-c", "credential.interactive=false", "push", "origin", oid + ":refs/heads/" + BRANCH, check=False, timeout=1800)
    (OUT / ("push-" + oid + ".log")).write_bytes(process.stderr + process.stdout)
    remote = git("ls-remote", "origin", "refs/heads/" + BRANCH).stdout.decode().split()
    if not remote or remote[0] != oid:
        raise ValueError("Push not verified; checkpoint retained; Git output in bounded local log")


def store_small(rows):
    if not rows:
        return
    for start in range(0, len(rows), 256):
        group = rows[start:start+256]
        for row in group:
            if signature(source(row)) != row["signature"]:
                raise ValueError("Source changed since freeze: " + row["path"])
        paths = "".join(json.dumps(source(row).as_posix(), ensure_ascii=False) + "\n" for row in group).encode("utf-8")
        actual = git("hash-object", "-w", "--no-filters", "--stdin-paths", data=paths).stdout.decode().splitlines()
        if actual != [row["oid"] for row in group]:
            raise ValueError("Source bytes changed while writing Git objects")
        for row in group:
            if signature(source(row)) != row["signature"]:
                raise ValueError("Source changed while storing: " + row["path"])


def store_parts(row):
    path = source(row)
    if signature(path) != row["signature"]:
        raise ValueError("Split source changed")
    result = []; full = hashlib.sha256()
    with path.open("rb") as stream:
        while data := stream.read(PART):
            full.update(data)
            oid = hash_data(data)
            result.append({"path": ".offsite/chunks/" + row["sha256"] + "/" + f"{len(result):04d}.part",
                           "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "oid": oid})
    if full.hexdigest() != row["sha256"] or signature(path) != row["signature"]:
        raise ValueError("Split source changed during storage")
    return result


def upload():
    frozen = json.loads((OUT / "frozen-files.json").read_text(encoding="utf-8"))
    if not BARE.exists():
        init()
    if checkpoint_path().exists():
        state = json.loads(checkpoint_path().read_text(encoding="utf-8"))
    else:
        state = {"next_file": 0, "head": PARENT, "commits": [], "parts": {}}
        save_checkpoint(state)
    if state.get("complete"):
        finalize_remote(state, len(frozen["files"]))
        return
    # Restore index from last frozen commit; an interrupted unsaved batch is safe to repeat.
    git("read-tree", state["head"])
    if state["head"] != PARENT:
        push(state["head"])
    known = {r["oid"] for r in json.loads((OUT / "reachable-objects.json").read_text(encoding="utf-8"))}
    known.update(git("rev-list", "--objects", "--no-object-names", state["head"]).stdout.decode().splitlines())
    files = frozen["files"]
    while state["next_file"] < len(files):
        start = state["next_file"]; end = start; budget = 0; additions = []; new_small = []; new_parts = {}
        while end < len(files):
            row = files[end]
            extra = 0 if row["oid"] in known else row["bytes"]
            if end > start and budget + extra > BATCH:
                break
            if row["bytes"] > MAX_FILE:
                parts = store_parts(row); additions.extend(parts); new_parts[str(end)] = parts
            else:
                additions.append(row)
                if row["oid"] not in known:
                    new_small.append(row)
            known.add(row["oid"]); budget += extra; end += 1
        store_small(new_small)
        update_index(additions)
        tree = git("write-tree").stdout.decode().strip()
        oid = git("commit-tree", tree, "-p", state["head"], "-m",
                  f"Back up current paper text and learning evidence ({end}/{len(files)})").stdout.decode().strip()
        git("update-ref", "refs/heads/" + BRANCH, oid, state["head"])
        # Local checkpoint first; a network error resumes the SAME commit, not a duplicate append.
        state["head"] = oid; state["next_file"] = end; state["commits"].append(oid); state["parts"].update(new_parts)
        save_checkpoint(state)
        print(json.dumps({"checkpoint_commit": oid, "files": end, "total_files": len(files), "new_raw_bytes": budget}), flush=True)
        push(oid)
    entries = []
    for index, original in enumerate(files):
        row = {k: v for k, v in original.items() if k != "signature"}
        if str(index) in state["parts"]:
            row["parts"] = state["parts"][str(index)]; row.pop("oid")
        entries.append(row)
    manifest = {"schema": "mcm-offsite-backup-v1", "volumes": ["F-MCM", "E-MCM-text-corpus-work"],
                "historical_parent": PARENT, "counts": frozen["counts"], "files": entries,
                "excluded": frozen["excluded"],
                "scope_note": "Complete selected current/accepted/reader-required text databases, not a claim of source-completeness or AI reading acceptance. Formula/figure semantic work remains paused."}
    manifest_data = json.dumps(manifest, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if len(manifest_data) > MAX_FILE:
        raise ValueError("Manifest exceeds GitHub ordinary-file limit")
    readme = ("# MCM complete-text offsite backup\n\n"
              "This snapshot includes working F-MCM files and the E: current v49, accepted v48, reader-required v46 databases, reading receipts, frozen runtimes and recovery evidence.\n\n"
              "Files above100MiB are split under `.offsite/chunks/`; the local originals are unchanged. The SHA-256 manifest maps every original file to its exact bytes.\n\n"
              "After cloning, verify without another data copy:\n\n`python .offsite/restore_backup.py --checkout .`\n\n"
              "Restore into a NEW directory (allow enough free disk):\n\n`python .offsite/restore_backup.py --checkout . --restore-to X:/new-empty-path`\n\n"
              "The tool creates F-MCM/ and E-MCM-text-corpus-work/ beneath that destination. It never overwrites existing files. NTFS compression/hardlink relationships are not restored.\n\n"
              "The backup is public at the user's explicit request. Obsolete copies, caches/private runtime and interrupted archives are excluded. This is storage preservation, NOT proof that all source sections are correct or AI-read.\n").encode()
    metadata = [{"path": ".offsite/manifest.json", "oid": hash_data(manifest_data)},
                {"path": ".offsite/README.md", "oid": hash_data(readme)},
                {"path": ".offsite/restore_backup.py", "oid": hash_data((E / "scripts/restore_git_offsite_backup.py").read_bytes())}]
    update_index(metadata)
    tree = git("write-tree").stdout.decode().strip()
    oid = git("commit-tree", tree, "-p", state["head"], "-m", "Finalize checksummed full-text backup and create-only restoration tool").stdout.decode().strip()
    git("update-ref", "refs/heads/" + BRANCH, oid, state["head"])
    state.update(head=oid, complete=True, tree=tree, manifest_sha256=hashlib.sha256(manifest_data).hexdigest())
    state["commits"].append(oid); save_checkpoint(state)
    finalize_remote(state, len(files))


def finalize_remote(state, file_count):
    oid = state["head"]
    push(oid)
    # Only fast-forward after every selected source file and restoration metadata is on the backup branch.
    git("-c", "credential.interactive=false", "push", "origin", oid + ":refs/heads/main", timeout=1800)
    remote = git("ls-remote", "origin", "refs/heads/main", "refs/heads/" + BRANCH).stdout.decode().splitlines()
    if len(remote) != 2 or any(line.split()[0] != oid for line in remote):
        raise ValueError("Final remote refs do not match")
    if not (OUT / "uploaded.json").exists():
        write_new(OUT / "uploaded.json", {"commit": oid, "tree": state["tree"], "remote_refs": remote,
                  "manifest_sha256": state["manifest_sha256"], "files": file_count, "split_files": len(state["parts"]), "commits": len(state["commits"])})
    print(json.dumps({"pass": True, "uploaded": oid, "files": file_count, "split_files": len(state["parts"])}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "upload"))
    args = parser.parse_args()
    {"prepare": prepare, "upload": upload}[args.action]()


if __name__ == "__main__":
    main()
