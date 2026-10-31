#!/usr/bin/env python3
"""Stage prose-only argument handoffs, without changing any live paper artifact.

These are traced connections between existing language candidates, not new
patterns, new independent support, equation checks or completed paper gates.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PID = "P-D-2015-38727-eeb1090f"
STAGING = Path("artifacts/staging")
V5 = STAGING / "integrity-repair-20261025-v5" / PID
V8 = STAGING / "integrity-repair-20261025-v8" / PID
V10 = STAGING / "integrity-repair-20261025-v10" / PID

# Physical-page text-line ranges, not visually certified paragraph boundaries.
# Formula pages, chart labels/captions, table cells and references are excluded.
PROSE_RANGES = {
    7: [(46, 53)], 8: [(4, 23), (27, 33)], 9: [(29, 54)],
    10: [(4, 45)], 11: [(4, 50)], 12: [(5, 51)],
    13: [(4, 34)], 15: [(40, 47)], 16: [(33, 56)], 17: [(10, 23)],
}


def node(role, page, first, last, phrase):
    return {"role": role, "physical_page": page, "first_line": first,
            "last_line": last, "expected_phrase": phrase}


CHAINS = [
    {
        "chain_id": "CONTENT-01", "title": "Case eligibility becomes a bounded demonstration",
        "unit_numbers": [5, 16, 17], "terminal_status": "bounded_demonstration",
        "nodes": [
            node("case-purpose-and-eligibility", 7, 46, 53, "A complete data set was available"),
            node("excluded-complications", 8, 4, 5, "should be avoided as complicating factors"),
            node("priority-alignment", 8, 19, 23, "declared national priorities"),
        ],
        "handoff": "Practical eligibility bounds the case; diagnosis and stated national priorities jointly motivate the agenda.",
        "writing_mechanism": "先说明案例为何适合演示，再交代被排除的复杂条件，最后说明建议与谁的目标对齐。",
        "boundary": "Tractability is not representative sampling or a universal applicability result.",
    },
    {
        "chain_id": "CONTENT-02", "title": "An education need becomes an operational programme",
        "unit_numbers": [19, 23, 24, 25, 26], "terminal_status": "proposed_effect",
        "nodes": [
            node("diagnostic-need", 9, 43, 48, "low expected education indicators"),
            node("programme-components", 11, 4, 11, "four major courses of study"),
            node("support-and-recipient-commitment", 11, 13, 18, "agree to work in these fields"),
            node("stated-workforce-purpose", 11, 35, 45, "prevent “brain drain”"),
        ],
        "handoff": "A diagnosed need leads to named training components; tuition support carries a service condition, which the authors link to workforce retention and access.",
        "writing_mechanism": "把建议写到专业设置、资助条件和服务去向，说明各设计部件各自承担什么作用。",
        "boundary": "The retention and access benefits are intentions, not measured programme effects; no cost or feasibility proof is inferred.",
    },
    {
        "chain_id": "CONTENT-03", "title": "A transport bottleneck receives a targeted fix and delivery condition",
        "unit_numbers": [22, 24, 25, 26, 27], "terminal_status": "proposed_effect",
        "nodes": [
            node("cross-sector-consequence", 10, 30, 35, "limits the ability"),
            node("operational-bottleneck", 12, 8, 13, "landslides and winter closure"),
            node("targeted-actions-and-feasibility", 12, 15, 20, "where possible"),
            node("community-contribution", 12, 21, 22, "funds matching"),
            node("intended-downstream-services", 12, 26, 36, "Improve access to education and health care"),
        ],
        "handoff": "Access failures motivate road, bridge and winter-service actions; local matching describes participation, while the separate benefit list names intended downstream uses.",
        "writing_mechanism": "先写运行失败及其后果，再给局部修复、可行性限定与投入条件，最后交代下游服务用途。",
        "boundary": "The prose does not estimate a transport-to-health or emergency-response effect size.",
    },
    {
        "chain_id": "CONTENT-04", "title": "An urban sanitation diagnosis acquires allocation and delivery roles",
        "unit_numbers": [20, 25, 26, 28, 39, 40], "terminal_status": "proposed_effect",
        "nodes": [
            node("anticipated-need", 9, 43, 46, "future need for a sanitation system"),
            node("location-and-coverage-rationale", 12, 38, 43, "large percentages"),
            node("resource-and-priority-rule", 12, 45, 49, "population density, and level of need"),
            node("behavioural-programme", 12, 50, 51, "public health education campaign"),
            node("named-delivery-partners", 13, 4, 5, "community health workers and midwives"),
            node("intended-service-benefits", 13, 9, 15, "Improve access to sanitation"),
        ],
        "handoff": "The authors connect urban growth to sanitation need, explain where reach is expected, specify loan priority, and identify health-education delivery partners.",
        "writing_mechanism": "把覆盖范围、资源分配标准、执行伙伴与受益目标分开写清，不把它们混成一个泛泛的建议段。",
        "boundary": "The named partners administer the education campaign; the text does not assign them ownership of every infrastructure action or demonstrate reach quantitatively.",
    },
    {
        "chain_id": "CONTENT-05", "title": "A favourable assessment preserves a residual-action branch",
        "unit_numbers": [22, 25, 26], "terminal_status": "proposed_effect",
        "nodes": [
            node("favourable-overview-and-residual-exposure", 10, 25, 35, "There is room for improvement"),
            node("targeted-building-requirement", 13, 6, 7, "basic earthquake safety standards"),
            node("intended-outcome", 13, 9, 15, "Improve earthquake safety"),
        ],
        "handoff": "A favourable overall risk narrative does not cancel the earthquake exposure; a specific requirement is proposed for that remaining issue.",
        "writing_mechanism": "保留总体评价中的例外，并把例外交给明确的局部动作，而不是因总体较好就省略它。",
        "boundary": "The prose contains no tested reduction in earthquake losses or verified construction compliance.",
    },
    {
        "chain_id": "CONTENT-06", "title": "A no-action outlook is not silently closed by an adjacent programme",
        "unit_numbers": [19, 26, 38], "terminal_status": "explicit_no_action_outlook",
        "nodes": [
            node("distinct-social-issues", 9, 50, 54, "departing refugees"),
            node("no-action-outlook", 10, 4, 5, "Barring action on these issues"),
            node("separate-programme-intentions", 11, 22, 33, "Improve gender equality"),
        ],
        "handoff": "The authors identify refugee tensions and gender inequality, then state a no-action outlook; the education benefit list addresses gender equality but does not explicitly supply a refugee-repatriation programme.",
        "writing_mechanism": "追踪到具体问题，而不只追踪到同名部门；相邻措施只覆盖其中一项时，保留另一项的未交接状态。",
        "boundary": "The missing handoff is a bounded observation about the reviewed programme prose, not proof that no relevant policy exists elsewhere or an estimated counterfactual effect.",
    },
    {
        "chain_id": "CONTENT-07", "title": "Local action and an external residual remain separate",
        "unit_numbers": [21, 25, 30, 34], "terminal_status": "qualified_projection",
        "nodes": [
            node("external-versus-local-diagnosis", 10, 16, 23, "room for improvement within Bhutan"),
            node("local-action", 13, 6, 7, "cook stove ventilation"),
            node("projected-exception", 15, 41, 47, "The only sector not improved"),
            node("wider-response-boundary", 17, 10, 17, "a more regional approach"),
        ],
        "handoff": "The prose distinguishes external pollution from locally addressable practices, proposes a local building requirement, preserves the projected environmental exception and later proposes a regional response.",
        "writing_mechanism": "把可行动部分与外部约束分开；局部方案不自动消除总体例外，再将超出本地主体权限的问题交给更大尺度。",
        "boundary": "These are author-stated explanations and a proposed response, not independently verified pollution attribution or a proved policy effect.",
    },
    {
        "chain_id": "CONTENT-08", "title": "Programme prose hands off to assumed updates, then a qualified outlook",
        "unit_numbers": [23, 29, 30, 31], "terminal_status": "qualified_projection",
        "nodes": [
            node("programme-proposal", 10, 39, 45, "a 20 year development program"),
            node("scenario-convention", 13, 31, 34, "All values not mentioned"),
            node("conditional-result-report", 15, 41, 47, "After updating the parameters"),
            node("input-quality-ceiling", 16, 33, 42, "only as accurate as the available data"),
        ],
        "handoff": "Recommendations are followed by selected assumed changes with a fixed remainder, then reported projected improvement and an input-quality boundary.",
        "writing_mechanism": "显式写出建议到情景的接口，再用条件性结果和数据边界收束，不把设定后的预测写成干预已经生效。",
        "boundary": "This traces prose only: no table values, equations, calibrated policy-response function, visual result or observed treatment effect is verified.",
    },
]

TERMINAL_STATUSES = {"bounded_demonstration", "proposed_effect",
                     "explicit_no_action_outlook", "qualified_projection"}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def normalized(text):
    return " ".join(text.split())


def attach_witnesses(chains, pages):
    result = copy.deepcopy(chains)
    for chain in result:
        if chain["terminal_status"] not in TERMINAL_STATUSES:
            raise ValueError("unsupported evidentiary promotion")
        for item in chain["nodes"]:
            page, first, last = (item[k] for k in ("physical_page", "first_line", "last_line"))
            if not any(lo <= first <= last <= hi for lo, hi in PROSE_RANGES.get(page, [])):
                raise ValueError("source range outside allowed author prose")
            lines = pages[page].splitlines()
            if last > len(lines):
                raise ValueError("source line range missing")
            excerpt = "\n".join(lines[first - 1:last])
            if normalized(item["expected_phrase"]) not in normalized(excerpt):
                raise ValueError("source phrase drift")
            item.update(printed_page=page - 1, text=excerpt,
                        excerpt_sha256=digest(excerpt.encode("utf-8")))
        chain["transitions"] = [
            {"from_role": a["role"], "to_role": b["role"],
             "basis": "root interpretation of the cited author prose; not a causal estimate"}
            for a, b in zip(chain["nodes"], chain["nodes"][1:])]
    return result


def validate_links(chains, units, mapping):
    available = {u["language_unit_id"] for u in units}
    linked = {m["language_unit_id"] for m in mapping}
    ids = [c["chain_id"] for c in chains]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate content chain")
    for chain in chains:
        if not all(chain.get(k) for k in ("handoff", "writing_mechanism", "boundary", "nodes", "unit_numbers")):
            raise ValueError("incomplete content handoff")
        if len(chain["nodes"]) < 2 or len(chain["transitions"]) != len(chain["nodes"]) - 1:
            raise ValueError("incomplete handoff path")
        chain["language_unit_ids"] = [f"LU-D-2015-38727-REPAIR-{n:03d}" for n in chain["unit_numbers"]]
        if not set(chain["language_unit_ids"]) <= available & linked:
            raise ValueError("unknown or unlinked language unit")


def put_new(path, raw):
    with path.open("xb") as handle:
        handle.write(raw)


def build(output):
    # Fail before reading inputs when a generation already exists.
    output.mkdir(parents=True, exist_ok=False)
    bound = {}

    def read(path):
        absolute = ROOT / path
        raw = absolute.read_bytes()
        bound[str(absolute)] = digest(raw)
        return raw

    recovery = json.loads(read(V10 / "recovery-report.json"))
    for path, expected in recovery["input_sha256"].items():
        if digest(Path(path).read_bytes()) != expected:
            raise ValueError("frozen recovery input changed")
        bound[path] = expected
    fresh = read(V10 / "fresh-native-full.bin")
    if digest(fresh) != recovery["fresh_native_sha256"]:
        raise ValueError("fresh text generation changed")
    parts = fresh.replace(b"\r\n", b"\n").replace(b"\r", b"\n").split(b"\f")
    if parts and not parts[-1].strip():
        parts.pop()
    if len(parts) != 19:
        raise ValueError("physical page count changed")
    pages = {}
    for n, part in enumerate(parts, 1):
        raw = read(V10 / "fresh-native/pages" / f"page-{n:04d}.txt")
        expected = (part.decode("utf-8").rstrip() + "\n").encode("utf-8")
        if raw != expected:
            raise ValueError("page not bound to the fresh source generation")
        # Reading bytes establishes provenance; only prose allowlist is used below.
        pages[n] = raw.decode("utf-8")
    candidate = json.loads(read(V5 / "language-units.draft.json"))
    mapping = json.loads(read(V8 / "unit-pattern-rule-map.draft.json"))
    read(V5 / "text-review.draft.json")
    read(V8 / "link-verification.json")
    chains = attach_witnesses(CHAINS, pages)
    validate_links(chains, candidate["units"], mapping)
    report = {
        "paper_id": PID, "status": "prose-content-draft-not-formal-G4-acceptance",
        "scope": "author prose only; chart/table distillation and formula verification paused",
        "reviewer": "root; no subagent", "chains": chains,
        "chain_count": len(chains), "witness_span_count": sum(len(c["nodes"]) for c in chains),
        "language_units_unchanged": len(candidate["units"]),
        "independent_paper_count": 1, "new_language_units": 0, "new_patterns": 0,
        "new_original_examples": 0, "new_observations": 0, "new_rules": 0,
        "source_generation": "v10 fresh-native; not historical/NFKC equivalence or layout authority",
        "page_convention": "physical PDF page; printed page = physical - 1 for these spans",
        "input_sha256": bound,
        "acceptance_not_claimed": ["full-scope saturation", "formal G4 section acceptance",
                                  "equation verification", "complete visual review", "paper closure",
                                  "cross-paper promotion", "installed skill update"],
        "bounded_scan_result": "No new independent author-prose mechanism beyond the frozen 41 units; formula/symbol dictionaries, plots, tables and references excluded.",
        "missing_handoff": "CONTENT-06: education intentions do not explicitly supply a refugee-repatriation programme within the reviewed programme prose.",
    }
    if any(digest(Path(p).read_bytes()) != h for p, h in bound.items()):
        raise ValueError("input changed during content tracing")
    put_new(output / "recipe.py", Path(__file__).read_bytes())
    raw = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    put_new(output / "content-handoffs.draft.json", raw)
    print(json.dumps({k: report[k] for k in ("status", "chain_count", "witness_span_count",
                                           "language_units_unchanged", "new_patterns")}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
