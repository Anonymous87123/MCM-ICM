"""Generate a new self-contained skill package, without touching the installed skill."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from corpus_reader import Catalog, status, author_text_coverage, query_policy_hash
from text_corpus import file_hash, json_new, read_json, write_new
from validate_text_corpus import validate


def package(base: Path, corpus: Path, output: Path, *, preview=False, reading_run=None,all_text_reading_run=None):
    if output.exists():
        raise ValueError("Package output already exists; refusing overwrite")
    if output.resolve().is_relative_to(base.resolve()) or output.resolve().is_relative_to(corpus.resolve()):
        raise ValueError("Output overlaps source tree")
    catalog = Catalog(corpus)
    scope_path = corpus/'scope.json'
    frozen_policy = read_json(scope_path).get('input_sha256',{}).get('queries') if scope_path.is_file() else None
    if frozen_policy and frozen_policy != query_policy_hash():
        raise ValueError('Package must freeze query policy in a new immutable corpus generation; no mixed-policy package')
    audit = validate(corpus)
    if not audit["structural_integrity_pass"]:
        raise ValueError("Corpus structural integrity failed")
    if not preview:
        if not audit["source_completeness_accepted"] or reading_run is None:
            raise ValueError("Final package requires source acceptance and an actual exhaustive abstract reading run")
        read_status = status(catalog, reading_run)
        session = read_json(reading_run / "session.json")
        if (not read_status["full_read_acceptance"] or session["query"]["section"] != "abstract" or
                session["query"]["scope"] != "all" or session["query"]["year"] is not None or
                session["allow_unverified"]):
            raise ValueError("Abstract reading acceptance does not cover all papers strictly")
        if all_text_reading_run is None:
            raise ValueError("Final package also requires actual reading acceptance of every author chapter in all papers")
        all_status=status(catalog,all_text_reading_run)
        all_session=read_json(all_text_reading_run/"session.json")
        if (not all_status["full_read_acceptance"] or all_session["query"]["section"]!="all_author_text" or
                all_session["query"]["scope"]!="all" or all_session["query"]["year"] is not None or
                all_session["allow_unverified"] or not author_text_coverage(catalog,[all_text_reading_run])["all_chapters_read_acceptance"]):
            raise ValueError("Complete author-text reading acceptance does not cover every chapter of all papers")
    output.mkdir(parents=True)
    base_bindings = {}
    for source in sorted(base.rglob("*")):
        if source.is_symlink():
            raise ValueError("Symlinks in installed skill require explicit packaging review")
        if not source.is_file() or "__pycache__" in source.parts:
            continue
        rel = source.relative_to(base)
        base_bindings[str(rel)] = file_hash(source)
        if str(rel) == "SKILL.md":
            continue
        write_new(output / rel, source.read_bytes())
    work = Path(__file__).resolve().parents[1]
    original = (base / "SKILL.md").read_text(encoding="utf-8")
    route = (work / "templates/text-corpus-route.md").read_text(encoding="utf-8")
    if "## Routes\n" not in original:
        raise ValueError("Unknown master-skill layout; no blind edit")
    label = ("Text attachment: MACHINE DRAFT, not complete-source acceptance.\n\n" if preview else
             "Text attachment: source-accepted corpus generation.\n\n")
    updated = original.replace("## Routes\n", label + route + "\n## Routes\n", 1)
    updated = updated.replace("Classifies corpus papers by path only", "Also reads complete corpus sections exhaustively on request. Classifies corpus papers by path only", 1)
    write_new(output / "SKILL.md", updated)
    write_new(output / "references/complete-corpus-reading.md", (work / "templates/complete-corpus-reading.md").read_bytes())
    for name in ("corpus_reader.py", "text_corpus.py", "corpus_queries.py"):
        write_new(output / "scripts" / name, (work / "scripts" / name).read_bytes())
    attached = {"catalog.json", "scope.json", "corpus.sqlite3", "legacy-preimages.json"}
    for paper in catalog.papers:
        attached.update(paper["files"])
    for source in (corpus / "inputs").rglob("*"):
        if source.is_file():
            attached.add(str(source.relative_to(corpus)).replace("\\", "/"))
    for rel in sorted(attached):
        source = (corpus / rel).resolve()
        if not source.is_relative_to(corpus.resolve()):
            raise ValueError("Corpus payload escapes root")
        write_new(output / "assets/text-corpus" / rel, source.read_bytes())
    copied_audit = validate(output / "assets/text-corpus")
    if not copied_audit["structural_integrity_pass"]:
        raise ValueError("Packaged corpus lost source accounting or repair evidence")
    if any(file_hash(base / rel) != sha for rel, sha in base_bindings.items()):
        raise ValueError("Installed skill changed during packaging")
    result = {"dataset_id": catalog.identity, "preview": preview, "installed_skill_modified": False,
              "base_skill_preimages": base_bindings, "audit": audit, "copied_corpus_audit": copied_audit,
              "payload_sha256": {str(p.relative_to(output)): file_hash(p) for p in output.rglob("*") if p.is_file()}}
    json_new(output / "package-manifest.json", result)
    return {"output": str(output), "preview": preview, "dataset_id": catalog.identity,
            "files": len(result["payload_sha256"]), "installed_skill_modified": False}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--base-skill", type=Path, required=True)
    p.add_argument("--corpus-root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--preview", action="store_true")
    p.add_argument("--reading-run", type=Path)
    p.add_argument("--all-text-reading-run",type=Path)
    a = p.parse_args()
    print(json.dumps(package(a.base_skill.resolve(), a.corpus_root.resolve(), a.output.resolve(),
                             preview=a.preview, reading_run=a.reading_run,all_text_reading_run=a.all_text_reading_run)))
