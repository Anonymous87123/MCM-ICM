"""Keep inventories and frozen hash catalogs, not old corpus payloads."""
import gzip
import hashlib
import json
from pathlib import Path
import shutil

OUT = Path(r"E:\MCM-text-corpus-work\archives\F-MCM-obsolete-generations-20261031-v4")
BASE = Path(r"F:\MCM\mcm-skill-work\artifacts")


def sha(path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def main():
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    if len(plan["roots"]) != 49:
        raise ValueError("Require32oldgenerations+17packages")
    kept = []
    for name in plan["roots"]:
        root = Path(name)
        if root.name in {"native-20261029-v1", "reflow-20261030-v16"}:
            raise ValueError("Keep-set overlap")
        paths = [root / "catalog.json", root / "scope.json"]
        inner = root / "mcm-icm-master-skill"
        paths += [inner / "package-manifest.json", inner / "assets/text-corpus/catalog.json",
                  inner / "assets/text-corpus/scope.json"]
        for p in paths:
            if not p.is_file():
                continue
            target = OUT / "retained-manifests" / (p.relative_to(BASE).as_posix() + ".gz")
            target.parent.mkdir(parents=True, exist_ok=True)
            with p.open("rb") as source, target.open("xb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=1) as compressed:
                shutil.copyfileobj(source, compressed, 1024**2)
            with gzip.open(target, "rb") as restored:
                digest = hashlib.file_digest(restored, "sha256").hexdigest()
            expected = sha(p)
            if digest != expected:
                raise ValueError("Manifest preservation mismatch")
            kept.append({"original": str(p), "retained": str(target), "sha256": expected})
    files = logical = entries = 0
    with (OUT / "source-before.tsv").open(encoding="utf-8") as f:
        for line in f:
            _, _, kind, size, _ = line.rstrip("\n").split("\t")
            entries += 1
            if kind == "F":
                files += 1
                logical += int(size)
    if (files, logical) != (1088001, 119124749322):
        raise ValueError("Unexpected inventory")
    result = {"policy": "user-approved-permanent-deletion-manifests-only", "roots": plan["roots"],
              "files": files, "logical_bytes": logical, "entries": entries,
              "plan_sha256": sha(OUT / "plan.json"), "source_index_sha256": sha(OUT / "source-before.tsv"),
              "retained_manifests": kept, "old_payloads_recoverable": False}
    with (OUT / "manifest-only-ready.json").open("x", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(json.dumps({"ready": True, "retained_manifests": len(kept), "files": files,
                      "logical_bytes": logical, "old_payloads_recoverable": False}), flush=True)


if __name__ == "__main__":
    main()
