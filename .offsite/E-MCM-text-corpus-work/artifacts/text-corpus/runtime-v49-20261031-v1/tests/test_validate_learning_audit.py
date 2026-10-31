from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_learning_audit.py"
SPEC = importlib.util.spec_from_file_location("validate_learning_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


DIMENSIONS = (
    "language",
    "modeling",
    "logic",
    "visualization",
    "verification",
    "data",
    "assumption",
    "result",
    "weakness",
    "other",
)


def language_unit(unit_id: str, chapter: str, pattern_id: str) -> dict[str, object]:
    return {
        "language_unit_id": unit_id,
        "chapter": chapter,
        "candidate_pattern_ids": [pattern_id],
    }


def chapter_layout(chapter: str, paragraphs: int) -> dict[str, object]:
    return {"chapter": chapter, "paragraph_count": paragraphs}


def equation(equation_id: str) -> dict[str, object]:
    return {"equation_id": equation_id}


def model(model_id: str, equation_id: str) -> dict[str, object]:
    return {
        "model_id": model_id,
        "equation_status": {"status": "present"},
        "governing_equations": [equation(equation_id)],
    }


def observation(token: str, dimension: str, page: int = 1) -> dict[str, object]:
    return {
        "observation_id": f"O-A-{token}",
        "paper_id": "P-A-2010-audit-aaaaaaaa",
        "problem_type": "A",
        "year": "2010",
        "page": page,
        "dimension": dimension,
    }


def fixtures() -> tuple[
    dict[str, object],
    dict[str, object],
    dict[str, object],
    dict[str, object],
    list[dict[str, object]],
    dict[str, object],
]:
    paper_id = "P-A-2010-audit-aaaaaaaa"
    source_hash = "a" * 64
    language = {
        "schema_version": 3,
        "paper_id": paper_id,
        "problem_type": "A",
        "year": "2010",
        "source_sha256": source_hash,
        "available_chapters": ["abstract", "introduction", "model-establishment"],
        "units": [
            language_unit("LU-A-AUDIT-ABS-001", "abstract", "LP-A-ABS-TASK"),
            language_unit("LU-A-AUDIT-ABS-002", "abstract", "LP-A-ABS-RESULT"),
            language_unit("LU-A-AUDIT-INT-001", "introduction", "LP-A-INT-GAP"),
            language_unit("LU-A-AUDIT-MOD-001", "model-establishment", "LP-A-MOD-DEF"),
        ],
        "chapter_layouts": [
            chapter_layout("abstract", 2),
            chapter_layout("introduction", 1),
            chapter_layout("model-establishment", 2),
        ],
        "review_status": "validated",
    }
    models = {
        "schema_version": 2,
        "paper_id": paper_id,
        "problem_type": "A",
        "year": "2010",
        "source_sha256": source_hash,
        "models": [
            model("MU-A-AUDIT-BASE-001", "EQ-A-AUDIT-BASE-001"),
            model("MU-A-AUDIT-EXT-002", "EQ-A-AUDIT-EXT-002"),
        ],
        "dependency_edges": [],
        "review_status": "validated",
    }
    card = {
        "paper_id": paper_id,
        "problem_type": "A",
        "year": "2010",
        "source": {"sha256": source_hash, "page_count": 10},
        "review_status": "validated",
        "protocol_v2_records": {
            "language": {
                "schema_version": 3,
                "unit_count": 4,
                "chapters": ["abstract", "introduction", "model-establishment"],
                "review_status": "validated",
            },
            "models": {
                "model_count": 2,
                "equation_count": 2,
                "review_status": "validated",
            },
        },
        "writing_logic": [
            {"page": 2, "summary": "The task is decomposed before the model handoff."}
        ],
        "visualization_observations": [
            {"page": 5, "section": "Results", "summary": "Response curve."},
            {"page": 6, "section": "Validation", "summary": "Residual comparison."},
        ],
        "weaknesses": [{"page": 8, "summary": "One bounded source limitation."}],
    }
    observations = [
        observation("LANG-001", "language"),
        observation("LANG-002", "language"),
        observation("LANG-003", "language"),
        observation("MODEL-001", "modeling", 4),
        observation("LOGIC-001", "logic", 2),
        observation("VIS-001", "visualization", 5),
        observation("VIS-002", "visualization", 6),
        observation("WEAK-001", "weakness", 8),
    ]
    counts = {dimension: 0 for dimension in DIMENSIONS}
    for item in observations:
        counts[str(item["dimension"])] += 1
    audit = {
        "schema_version": 1,
        "audit_id": "LA-A-2010-AUDIT-001",
        "paper_id": paper_id,
        "problem_type": "A",
        "year": "2010",
        "source_sha256": source_hash,
        "priority_order": [
            "language-imitation",
            "organization-logic",
            "formula-error-watch",
        ],
        "chapter_saturation": [
            {
                "chapter": chapter,
                "pass_count": 2,
                "last_pass_new_moves": 0,
                "coverage_status": "complete",
                "gaps": [],
            }
            for chapter in language["available_chapters"]
        ],
        "language_unit_dispositions": [
            {
                "language_unit_id": "LU-A-AUDIT-ABS-001",
                "disposition": "supports-existing",
                "target_pattern_ids": ["LP-A-ABS-TASK"],
                "reason": "",
            },
            {
                "language_unit_id": "LU-A-AUDIT-ABS-002",
                "disposition": "opens-candidate",
                "target_pattern_ids": ["LP-A-ABS-RESULT"],
                "reason": "",
            },
            {
                "language_unit_id": "LU-A-AUDIT-INT-001",
                "disposition": "supports-existing",
                "target_pattern_ids": ["LP-A-INT-GAP"],
                "reason": "",
            },
            {
                "language_unit_id": "LU-A-AUDIT-MOD-001",
                "disposition": "paper-specific-nonreusable",
                "target_pattern_ids": [],
                "reason": "Depends on paper-specific notation and cannot transfer safely.",
            },
        ],
        "paragraph_chains": [
            {
                "chapter": "abstract",
                "visual_paragraph_count": 2,
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": 1,
                        "dominant_move": "task-method",
                        "language_unit_ids": ["LU-A-AUDIT-ABS-001"],
                    },
                    {
                        "paragraph_index": 2,
                        "dominant_move": "result-boundary",
                        "language_unit_ids": ["LU-A-AUDIT-ABS-002"],
                    },
                ],
            },
            {
                "chapter": "introduction",
                "visual_paragraph_count": 1,
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": 1,
                        "dominant_move": "context-gap-roadmap",
                        "language_unit_ids": ["LU-A-AUDIT-INT-001"],
                    }
                ],
            },
        ],
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "task framing",
                "model construction",
                "validation",
                "decision meaning",
            ],
            "section_progressions": [
                {
                    "chapter": "abstract",
                    "moves": [
                        "input: official task and the paper's principal result",
                        "rhetorical job: compress task -> method -> result -> boundary",
                        "analytical job: select the result that answers the task",
                        "output: a quantitative solution preview",
                        "handoff: introduction, which establishes the context and gap",
                    ],
                    "positive_pattern": "The result preview establishes the route that follows.",
                },
                {
                    "chapter": "introduction",
                    "moves": [
                        "input: official task context and the opening context move",
                        "rhetorical job: guide the reader through context -> gap -> roadmap",
                        "analytical job: establish the unresolved need and preview the solution route",
                        "output: a bounded model roadmap",
                        "handoff: model-establishment, beginning with the mechanism",
                    ],
                    "positive_pattern": "The gap leads directly to the model roadmap.",
                },
                {
                    "chapter": "model-establishment",
                    "moves": [
                        "input: the introduction roadmap and the mechanism to formalize",
                        "rhetorical job: guide the reader through mechanism -> variables -> equations -> handoff",
                        "analytical job: convert the mechanism into an auditable mathematical formulation",
                        "output: equations and a defined model output",
                        "handoff: the next decision stage and its validation need",
                    ],
                    "positive_pattern": "Each model output feeds the next decision stage.",
                },
            ],
            "main_argument_chains": [
                {
                    "claim": "The selected response is preferable.",
                    "support_steps": ["derive response", "compare baseline", "validate trend"],
                    "decision_consequence": "Recommend the bounded operating region.",
                    "source_pages": [4, 5, 6],
                }
            ],
        },
        "formula_error_watch": {
            "mode": "last-pass-warning-only",
            "completed_after_positive_passes": True,
            "warnings": [
                {
                    "model_id": "MU-A-AUDIT-BASE-001",
                    "equation_id": "EQ-A-AUDIT-BASE-001",
                    "page": 4,
                    "warning": "Check the stated validity domain before reuse.",
                }
            ],
        },
        "model_retention": {
            "model_count": 2,
            "retained_model_ids": ["MU-A-AUDIT-BASE-001", "MU-A-AUDIT-EXT-002"],
            "retained_equation_ids": ["EQ-A-AUDIT-BASE-001", "EQ-A-AUDIT-EXT-002"],
            "central_equations": [
                {
                    "model_id": "MU-A-AUDIT-BASE-001",
                    "equation_ids": ["EQ-A-AUDIT-BASE-001"],
                    "all_central_equations_retained": True,
                },
                {
                    "model_id": "MU-A-AUDIT-EXT-002",
                    "equation_ids": ["EQ-A-AUDIT-EXT-002"],
                    "all_central_equations_retained": True,
                },
            ],
        },
        "visualization_dispositions": [
            {
                "paper_card_visual_index": 1,
                "visual_record_id": "V-A-AUDIT-001",
                "disposition": "important-visual-record",
                "analytical_purpose": "Show the response curve used by the decision.",
            },
            {
                "paper_card_visual_index": 2,
                "visual_record_id": "V-A-AUDIT-002",
                "disposition": "important-visual-record",
                "analytical_purpose": "Show validation residuals against the baseline.",
            },
        ],
        "dimension_counts": counts,
        "positive_reusable_language_count": 3,
        "weakness_record_count": 1,
        "review_status": "validated",
    }
    manifest = {
        "paper_id": paper_id,
        "problem_type": "A",
        "year": "2010",
        "sha256": source_hash,
        "page_count": 10,
        "eligible_paper": True,
    }
    return audit, language, models, card, observations, manifest


class LearningAuditValidationTests(unittest.TestCase):
    def validate(self, *items: object) -> list[str]:
        return MODULE.validate_audit(*items)

    def test_complete_audit_passes(self):
        self.assertEqual(self.validate(*fixtures()), [])

    def test_requires_current_validated_language_and_model_records(self):
        audit, language, models, card, observations, manifest = fixtures()
        language["schema_version"] = 2
        models["review_status"] = "source-checked"

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("language schema_version" in error for error in errors))
        self.assertTrue(any("model review_status" in error for error in errors))

    def test_every_chapter_requires_a_completed_saturation_pass(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["chapter_saturation"][0]["pass_count"] = 1
        audit["chapter_saturation"][1]["last_pass_new_moves"] = 1
        audit["chapter_saturation"][2]["gaps"] = ["unreviewed transition"]

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("pass_count" in error for error in errors))
        self.assertTrue(any("last_pass_new_moves" in error for error in errors))
        self.assertTrue(any("gaps must be empty" in error for error in errors))

    def test_saturation_chapters_must_exactly_match_available_chapters(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["chapter_saturation"].pop()

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("chapter_saturation chapters" in error for error in errors))

    def test_every_language_unit_has_exactly_one_disposition(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["language_unit_dispositions"].pop()
        audit["language_unit_dispositions"].append(
            copy.deepcopy(audit["language_unit_dispositions"][0])
        )

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("duplicate language_unit_id" in error for error in errors))
        self.assertTrue(any("language unit dispositions" in error for error in errors))

    def test_disposition_target_and_nonreusable_reason_are_enforced(self):
        audit, language, models, card, observations, manifest = fixtures()
        reusable = audit["language_unit_dispositions"][0]
        nonreusable = audit["language_unit_dispositions"][3]
        reusable["target_pattern_ids"] = ["LP-A-NOT-NOMINATED"]
        nonreusable["reason"] = ""

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("target_pattern_ids" in error for error in errors))
        self.assertTrue(any("nonreusable reason" in error for error in errors))

    def test_missing_catalog_is_not_a_valid_nonreusable_reason(self):
        audit, language, models, card, observations, manifest = fixtures()
        nonreusable = audit["language_unit_dispositions"][3]
        nonreusable["reason"] = "No corroborated body-pattern ID exists yet in the catalog."

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("merely because a catalog" in error for error in errors))

    def test_abstract_and_introduction_paragraph_chains_match_layout(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["paragraph_chains"][0]["visual_paragraph_count"] = 3
        audit["paragraph_chains"][1]["paragraphs"] = []

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("visual paragraph count" in error for error in errors))
        self.assertTrue(any("paragraph chain count" in error for error in errors))

    def test_paragraph_chain_unit_must_belong_to_the_same_chapter(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["paragraph_chains"][0]["paragraphs"][0]["language_unit_ids"] = [
            "LU-A-AUDIT-INT-001"
        ]

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("paragraph language unit chapter" in error for error in errors))

    def test_positive_organization_artifacts_cannot_be_replaced_by_weaknesses(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["organization_logic"]["global_organization_chain"] = []
        audit["organization_logic"]["weakness_substitution_allowed"] = True
        card["writing_logic"] = []

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("global organization chain" in error for error in errors))
        self.assertTrue(any("weakness substitution" in error for error in errors))
        self.assertTrue(any("paper card writing_logic" in error for error in errors))

    def test_section_progressions_require_explicit_section_contract_moves(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["organization_logic"]["section_progressions"][0]["moves"] = [
            "context",
            "gap",
            "roadmap",
        ]

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("exactly five section-contract moves" in error for error in errors))
        self.assertTrue(any("requires one nonempty input move" in error for error in errors))

    def test_section_progressions_exactly_cover_available_chapters(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["organization_logic"]["section_progressions"].pop()

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("must exactly cover available chapters" in error for error in errors))

    def test_formula_error_watch_is_last_pass_warning_only(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["priority_order"] = [
            "formula-error-watch",
            "language-imitation",
            "organization-logic",
        ]
        audit["formula_error_watch"]["mode"] = "primary-output"
        audit["formula_error_watch"]["completed_after_positive_passes"] = False

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("priority_order" in error for error in errors))
        self.assertTrue(any("last-pass-warning-only" in error for error in errors))
        self.assertTrue(any("completed_after_positive_passes" in error for error in errors))

    def test_model_and_equation_retention_must_be_exact(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["model_retention"]["retained_model_ids"].pop()
        audit["model_retention"]["retained_equation_ids"].pop()
        audit["model_retention"]["central_equations"].pop()

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("retained_model_ids" in error for error in errors))
        self.assertTrue(any("retained_equation_ids" in error for error in errors))
        self.assertTrue(any("central equation coverage" in error for error in errors))

    def test_formula_warning_references_known_model_and_equation(self):
        audit, language, models, card, observations, manifest = fixtures()
        warning = audit["formula_error_watch"]["warnings"][0]
        warning["model_id"] = "MU-A-MISSING"
        warning["equation_id"] = "EQ-A-MISSING"

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("formula warning model_id" in error for error in errors))
        self.assertTrue(any("formula warning equation_id" in error for error in errors))

    def test_every_card_visualization_has_an_important_visual_disposition(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["visualization_dispositions"].pop()

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("visualization dispositions" in error for error in errors))

    def test_dimension_counts_must_match_observations(self):
        audit, language, models, card, observations, manifest = fixtures()
        audit["dimension_counts"]["language"] += 1

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("dimension_counts" in error for error in errors))

    def test_positive_reusable_language_must_exceed_weakness_records(self):
        audit, language, models, card, observations, manifest = fixtures()
        observations.extend(
            [observation("WEAK-002", "weakness", 8), observation("WEAK-003", "weakness", 9)]
        )
        audit["dimension_counts"]["weakness"] = 3
        audit["weakness_record_count"] = 3

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("must exceed weakness" in error for error in errors))

    def test_identity_is_cross_validated_against_manifest_and_all_artifacts(self):
        audit, language, models, card, observations, manifest = fixtures()
        manifest["sha256"] = "b" * 64
        card["problem_type"] = "B"

        errors = self.validate(audit, language, models, card, observations, manifest)

        self.assertTrue(any("source_sha256 differs from manifest" in error for error in errors))
        self.assertTrue(any("paper card problem_type differs" in error for error in errors))

    def test_cli_validates_all_six_artifacts(self):
        audit, language, models, card, observations, manifest = fixtures()
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            root = Path(directory)
            paths = {
                "audit": root / "audit.json",
                "language": root / "language.json",
                "model": root / "model.json",
                "card": root / "card.json",
                "observations": root / "observations.jsonl",
                "manifest": root / "manifest.jsonl",
            }
            paths["audit"].write_text(json.dumps(audit), encoding="utf-8")
            paths["language"].write_text(json.dumps(language), encoding="utf-8")
            paths["model"].write_text(json.dumps(models), encoding="utf-8")
            paths["card"].write_text(json.dumps(card), encoding="utf-8")
            paths["observations"].write_text(
                "".join(json.dumps(item) + "\n" for item in observations), encoding="utf-8"
            )
            paths["manifest"].write_text(json.dumps(manifest) + "\n", encoding="utf-8")

            result = MODULE.main(
                [
                    "--audit",
                    str(paths["audit"]),
                    "--language-record",
                    str(paths["language"]),
                    "--model-record",
                    str(paths["model"]),
                    "--paper-card",
                    str(paths["card"]),
                    "--observations",
                    str(paths["observations"]),
                    "--manifest",
                    str(paths["manifest"]),
                ]
            )

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
