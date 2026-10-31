"""Plan removal only for byte-identical closed-paper scratch and untracked caches."""
import collections
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import stat

ROOT = Path(r"F:\MCM")
WORK = ROOT / "mcm-skill-work"
OUT = Path(r"E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5")


def sha(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def new_json(name, value):
    with (OUT / name).open("x", encoding="utf-8") as output:
        json.dump(value, output, indent=2)


def safe(path):
    path = Path(os.path.abspath(path))
    if not path.is_relative_to(ROOT) or path == ROOT:
        raise ValueError(f"Outside F:/MCM: {path}")
    for part in (path, *path.parents):
        if part.stat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            raise ValueError(f"Reparse point: {part}")
        if part == ROOT:
            break


def main():
    spec = importlib.util.spec_from_file_location("guard", OUT.parents[1] / "scripts/guard_f_cleanup_evidence.py")
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    guard.OUT = OUT
    guard.snapshot()
    before = json.loads((OUT / "preservation-before.json").read_text(encoding="utf-8"))
    protected = {p.casefold() for p in before["bindings"]}
    cleanup = json.loads((WORK / "tmp/_cleanup-manifest.json").read_text(encoding="utf-8"))
    preserve_roots = [str(WORK / p.replace("\\", "/")).casefold() for p in cleanup["kept"]]
    # Historical transaction strings are protected conservatively, even if not a binding.
    def protect_strings(value):
        if isinstance(value, dict):
            for child in value.values():
                protect_strings(child)
        elif isinstance(value, list):
            for child in value:
                protect_strings(child)
        elif isinstance(value, str):
            normalized = value.replace("\\", "/")
            if normalized.lower().startswith("tmp/"):
                preserve_roots.append(str(WORK / normalized).casefold())
            elif normalized.lower().startswith("f:/mcm/"):
                protected.add(str(Path(normalized)).casefold())
    with (WORK / "artifacts/transactions/history.jsonl").open(encoding="utf-8") as source:
        for line in source:
            protect_strings(json.loads(line))
    inventory = [json.loads(line) for line in (OUT / "inventory.jsonl").open(encoding="utf-8")]
    by_path = {row["path"]: row for row in inventory}
    progress = {row["paper_id"]: row for row in
                map(json.loads, (WORK / "artifacts/progress.jsonl").open(encoding="utf-8"))}
    groups = collections.defaultdict(list)
    for row in inventory:
        parts = row["path"].split("/")
        if len(parts) >= 4 and parts[:2] == ["mcm-skill-work", "tmp"]:
            if re.fullmatch(r"q\d+-extraction(?:-final)?(?:-v\d+)?", parts[2]):
                groups["/".join(parts[:4])].append(row)
    delete_files = []
    redundant_dirs = []
    retained = collections.Counter()
    for relative, rows in sorted(groups.items()):
        target = ROOT / relative
        paper_id = target.name
        official = WORK / "artifacts/papers" / paper_id
        if progress.get(paper_id, {}).get("status") != "closed" or not official.is_dir():
            retained["not_closed_or_no_official_copy"] += 1
            continue
        if any(r["tracked"] or str(ROOT / r["path"]).casefold() in protected for r in rows):
            retained["tracked_or_historically_bound"] += 1
            continue
        prefix = str(target).casefold()
        if any(p == prefix or p.startswith(prefix + "\\") or prefix.startswith(p + "\\") for p in preserve_roots):
            retained["prior_keep_list_or_transaction_reference"] += 1
            continue
        safe(target)
        if any(Path(base).is_symlink() or any((Path(base) / d).stat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
               for d in children) for base, children, _ in os.walk(target, followlinks=False)):
            retained["reparse_inside"] += 1
            continue
        matches = []
        for row in rows:
            path = ROOT / row["path"]
            canonical = official / path.relative_to(target)
            if not canonical.is_file() or canonical.stat().st_size != row["bytes"]:
                break
            safe(path)
            safe(canonical)
            digest = sha(path)
            if sha(canonical) != digest:
                break
            matches.append({**row, "retained_copy": str(canonical), "sha256": digest,
                            "reason": "byte-identical closed-paper scratch; official copy retained"})
        if len(matches) != len(rows) or not matches:
            retained["unique_or_changed_bytes"] += 1
            continue
        delete_files.extend(matches)
        redundant_dirs.append({"path": str(target), "retained_copy": str(official),
                               "files": len(matches), "bytes": sum(r["bytes"] for r in rows)})
    for row in inventory:
        relative = row["path"]
        parts = relative.split("/")
        if row["tracked"] or "artifacts/text-corpus/" in relative or "/lanes/" in relative:
            continue
        if not ("__pycache__" in parts[:-1] and relative.endswith(".pyc") or ".pytest_cache" in parts[:-1]):
            continue
        path = ROOT / relative
        if str(path).casefold() in protected:
            continue
        safe(path)
        delete_files.append({**row, "sha256": sha(path), "reason": "untracked regenerable Python/pytest cache"})
    plan = {"root": str(ROOT), "protected_binding_count": len(protected),
            "directories": redundant_dirs, "files": delete_files,
            "retained_groups": dict(retained), "removed_files_planned": len(delete_files),
            "logical_bytes_planned": sum(r["bytes"] for r in delete_files)}
    new_json("f-delete-plan.json", plan)
    print(json.dumps({k: v for k, v in plan.items() if k not in ("files", "directories")}), flush=True)
    print(json.dumps({"redundant_directories": len(redundant_dirs), "examples": redundant_dirs[:3]}), flush=True)


if __name__ == "__main__":
    main()
