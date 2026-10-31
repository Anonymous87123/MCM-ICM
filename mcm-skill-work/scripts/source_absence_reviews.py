"""Freeze and apply source-local absence reviews; never infer absence from OCR gaps."""
from __future__ import annotations

import copy
import re
from pathlib import Path

from text_corpus import absence_review_valid, digest, encoded, file_hash, read_json


def prepare_review_bundles(paths, *, identity_fields, application_status):
    reviews = []; copies = {}; seen = set()
    for path in paths:
        review = copy.deepcopy(read_json(path))
        key = tuple(review.get(k) for k in identity_fields)
        if key in seen:
            raise ValueError("Duplicate absence review")
        seen.add(key)
        files = {}
        for proof in review.get("evidence",[]):
            source = Path(proof["path"]).resolve()
            if not source.is_file() or file_hash(source) != proof["sha256"]:
                raise ValueError("Absence review proof missing or changed")
            bundle = Path(proof["bundle_root"]).resolve() if proof.get("bundle_root") else None
            if bundle:
                if not source.is_relative_to(bundle):
                    raise ValueError("Absence proof outside evidence bundle")
                sources = sorted(p for p in bundle.rglob("*") if p.is_file())
                if any(p.is_symlink() or not p.resolve().is_relative_to(bundle) for p in bundle.rglob("*")):
                    raise ValueError("Absence evidence bundle must not contain links or escaping paths")
                bindings = {p.relative_to(bundle).as_posix():file_hash(p) for p in sources}
                prefix = "inputs/absence-evidence/"+digest(encoded(bindings))
                for p in sources:
                    rel = prefix+"/"+p.relative_to(bundle).as_posix()
                    copies[rel] = (p,bindings[p.relative_to(bundle).as_posix()]); files[rel] = copies[rel][1]
                proof["path"] = prefix+"/"+source.relative_to(bundle).as_posix()
                proof.pop("bundle_root",None)
            else:
                rel = "inputs/absence-evidence/"+proof["sha256"]+source.suffix.lower()
                copies[rel] = (source,proof["sha256"]); files[rel] = proof["sha256"]
                proof["path"] = rel
        if not files:
            raise ValueError("Absence review needs checked evidence files")
        review["evidence_files"] = files
        review["application_status"] = application_status
        reviews.append(review)
    return reviews, copies


def prepare_absence_reviews(paths):
    return prepare_review_bundles(paths,identity_fields=("paper_id","role"),
            application_status="applied source-local absence; not an abstract read or whole-paper acceptance")


def apply_absence_reviews(document, reviews):
    for review in reviews:
        if review.get("paper_id") != document["paper_id"]:
            continue
        role = review.get("role")
        if not absence_review_valid(document,role,review) or not review.get("evidence_files"):
            raise ValueError("Incomplete, stale or contradictory whole-source absence review")
        if role in document.get("verified_absent_roles",[]):
            raise ValueError("Absence review already applied")
        document.setdefault("absence_reviews",{})[role] = review
        document.setdefault("verified_absent_roles",[]).append(role)
        # A source-local absence is not a waiver of any prose, layout or other
        # section defect. Existing unresolved flags are deliberately untouched.


def validate_absence_reviews(root: Path, document):
    roles = document.get("verified_absent_roles",[])
    if len(set(roles)) != len(roles) or set(roles) != set(document.get("absence_reviews",{})):
        raise ValueError("Absence roles and proofs differ")
    for role in roles:
        review = document["absence_reviews"][role]
        if not absence_review_valid(document,role,review) or not review.get("evidence_files"):
            raise ValueError("Invalid source-local absence proof")
        validate_review_bundle(root,review)


def validate_review_bundle(root: Path,review):
    if not review.get("evidence_files") or not review.get("evidence"):
        raise ValueError("Source review has no portable evidence")
    for rel,sha in review["evidence_files"].items():
        path = (root/rel).resolve()
        if (Path(rel).is_absolute() or not path.is_relative_to(root.resolve()) or
                not re.fullmatch(r"[a-f0-9]{64}",sha) or not path.is_file() or file_hash(path) != sha):
            raise ValueError("Source review evidence missing, escaped or changed")
    if any(review["evidence_files"].get(p["path"]) != p["sha256"] for p in review["evidence"]):
        raise ValueError("Source review evidence declaration differs from bundle")
