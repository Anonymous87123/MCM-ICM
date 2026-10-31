#!/usr/bin/env python3
"""Normalize audited section progressions into explicit five-part contracts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


PREFIXES = (
    "input:",
    "rhetorical job:",
    "analytical job:",
    "output:",
    "handoff:",
)

ANALYTICAL_JOBS = {
    "title": "identify the decision domain and the paper's organizing focus",
    "abstract": "compress the tasks, methods, principal results, checks, and decision meaning",
    "introduction": "establish the practical need, bound the task, and preview the solution route",
    "problem-restatement": "translate the official request into precise deliverables without changing scope",
    "problem-analysis": "decompose the request into solvable subproblems and dependency order",
    "assumptions": "bound the real system while preserving the mechanism required by the models",
    "notation": "stabilize symbols, indexed objects, units, and downstream references",
    "data-preprocessing": "turn source data into model-ready evidence with explicit transformations",
    "model-establishment": "convert the selected mechanism into variables, equations, constraints, and outputs",
    "model-improvement": "resolve a stated baseline limitation through a bounded extension",
    "algorithm": "turn the mathematical formulation into an executable solution procedure",
    "results": "translate model output into comparisons, interpretations, and requested decisions",
    "sensitivity-analysis": "test how parameter changes affect outputs and decision stability",
    "robustness-verification": "test whether the result survives perturbation, alternatives, or repeated runs",
    "sensitivity-robustness": "test parameter response and the stability of the resulting decision",
    "error-analysis": "bound known error sources and their consequences for reuse",
    "strengths": "connect demonstrated capabilities to the evidence that supports them",
    "limitations": "bound transfer and decision claims by the model's known omissions",
    "strengths-limitations": "balance demonstrated capability with explicit transfer boundaries",
    "future-improvements": "convert current limitations into scoped next analytical steps",
    "conclusion": "close every requested task with results, decisions, caveats, and next steps",
    "memo": "translate modeled evidence into actor-specific actions and conditions",
    "references": "anchor borrowed facts or methods while preserving provenance and transfer limits",
    "appendix": "supply reproducibility detail without interrupting the main argument",
}


def is_contract(moves: Any) -> bool:
    if not isinstance(moves, list) or len(moves) != len(PREFIXES):
        return False
    normalized = [str(move).strip().lower() for move in moves]
    return all(sum(move.startswith(prefix) for move in normalized) == 1 for prefix in PREFIXES)


def contract_moves(
    progression: dict[str, Any],
    previous: dict[str, Any] | None,
    following: dict[str, Any] | None,
) -> list[str]:
    chapter = str(progression.get("chapter", "unknown"))
    moves = progression.get("moves")
    if not isinstance(moves, list) or not moves or not all(
        isinstance(move, str) and move.strip() for move in moves
    ):
        raise ValueError(f"{chapter} has no usable observed move sequence")
    if any(str(move).strip().lower().startswith(PREFIXES) for move in moves):
        raise ValueError(f"{chapter} contains a partial or malformed section contract")

    sequence = " -> ".join(move.strip() for move in moves)
    first_move = moves[0].strip()
    last_move = moves[-1].strip()
    pattern = str(progression.get("positive_pattern", "")).strip()
    if not pattern:
        raise ValueError(f"{chapter} has no positive pattern")

    if previous is None:
        input_text = f"the official task context and the section's observed opening move `{first_move}`"
    else:
        previous_chapter = str(previous.get("chapter", "prior section"))
        previous_moves = previous.get("moves")
        previous_output = (
            previous_moves[-1].strip()
            if isinstance(previous_moves, list)
            and previous_moves
            and isinstance(previous_moves[-1], str)
            else "documented output"
        )
        input_text = (
            f"the `{previous_chapter}` output `{previous_output}` plus "
            f"the current opening move `{first_move}`"
        )

    analytical_job = ANALYTICAL_JOBS.get(
        chapter,
        "perform the chapter's source-observed analytical role and produce a traceable downstream result",
    )
    output_text = (
        f"the observed `{last_move}` output governed by the positive pattern `{pattern}`"
    )

    if following is None:
        handoff_text = "the reader-facing close of the paper or the next source-defined deliverable"
    else:
        next_chapter = str(following.get("chapter", "next section"))
        next_moves = following.get("moves")
        next_input = (
            next_moves[0].strip()
            if isinstance(next_moves, list)
            and next_moves
            and isinstance(next_moves[0], str)
            else "its documented opening move"
        )
        handoff_text = f"`{next_chapter}`, which begins with `{next_input}`"

    return [
        f"input: {input_text}",
        f"rhetorical job: guide the reader through the observed move sequence `{sequence}`",
        f"analytical job: {analytical_job}",
        f"output: {output_text}",
        f"handoff: {handoff_text}",
    ]


def migrate_audit(audit: dict[str, Any]) -> int:
    logic = audit.get("organization_logic")
    if not isinstance(logic, dict):
        raise ValueError("organization_logic must be an object")
    progressions = logic.get("section_progressions")
    if not isinstance(progressions, list) or not progressions:
        raise ValueError("section_progressions must be a nonempty array")

    originals = [dict(progression) for progression in progressions]
    changed = 0
    for index, progression in enumerate(progressions):
        if not isinstance(progression, dict):
            raise ValueError(f"section_progressions[{index + 1}] must be an object")
        if is_contract(progression.get("moves")):
            continue
        previous = originals[index - 1] if index > 0 else None
        following = originals[index + 1] if index + 1 < len(originals) else None
        progression["moves"] = contract_moves(progression, previous, following)
        changed += 1
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-dir", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    report: list[dict[str, Any]] = []
    try:
        for path in sorted(args.audit_dir.glob("*.json")):
            before_bytes = path.read_bytes()
            audit = json.loads(before_bytes.decode("utf-8"))
            if not isinstance(audit, dict):
                raise ValueError(f"{path} must contain an object")
            changed = migrate_audit(audit)
            after_bytes = (json.dumps(audit, ensure_ascii=False, indent=2) + "\n").encode(
                "utf-8"
            )
            if changed and not args.dry_run:
                path.write_bytes(after_bytes)
            report.append(
                {
                    "paper_id": audit.get("paper_id"),
                    "changed_section_contracts": changed,
                    "before_sha256": hashlib.sha256(before_bytes).hexdigest(),
                    "after_sha256": hashlib.sha256(after_bytes).hexdigest(),
                    "status": (
                        "would-change"
                        if args.dry_run and changed
                        else "changed"
                        if changed
                        else "unchanged"
                    ),
                }
            )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1

    result = {
        "status": "pass",
        "paper_count": len(report),
        "changed_papers": sum(item["changed_section_contracts"] > 0 for item in report),
        "changed_section_contracts": sum(
            item["changed_section_contracts"] for item in report
        ),
        "records": report,
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
