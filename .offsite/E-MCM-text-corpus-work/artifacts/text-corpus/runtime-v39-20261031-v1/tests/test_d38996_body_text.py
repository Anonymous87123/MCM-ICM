import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import stage_d38996_body_text as body
import stage_d38996_text_first as opening
import validate_language_units as language


class BodyTextTests(unittest.TestCase):
    def pages(self):
        b = body.ROOT / f"artifacts/papers/{body.PID}/text/pages"
        return {i: (b / f"page-{i:04d}.txt").read_text(encoding="utf-8") for i in range(1, 22)}

    def test_constructor_default_replays_frozen_opening(self):
        frozen = json.loads((body.ROOT / f"artifacts/staging/text-first-20261029-v3/{body.PID}/language-units.draft.json").read_text(encoding="utf-8"))
        pages = self.pages()
        self.assertEqual([opening.construct_unit(s, i, pages) for i, s in enumerate(opening.MECHANISMS, 1)], frozen["units"])

    def test_existing_output_rejected_before_reading_inputs(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileExistsError):
                body.build(Path(d), root=Path(d) / "missing")

    def test_units_have_exact_sources_and_valid_structure(self):
        pages = self.pages()
        units = body.build_units(pages)
        self.assertEqual(len(units), 31)
        self.assertEqual(len({u["candidate_pattern_ids"][0] for u in units}), 31)
        for i, u in enumerate(units, 1):
            self.assertEqual(language.validate_unit(u, "D", 21, None, i), [])
            self.assertEqual(u["function"], u["g3"]["stable_function"])
            self.assertEqual(u["information_order"], u["g3"]["order"])
            self.assertEqual(u["g3"]["cross_paper_support_count"], 0)
            for o in u["occurrences"]:
                self.assertEqual(o["source_excerpt"], opening.source_span(pages, o["page"], o["first_line"], o["last_line"]))
                self.assertNotIn("\ufffd", o["source_excerpt"])

    def test_repeated_body_occurrences_do_not_add_mechanisms(self):
        units = body.build_units(self.pages())
        self.assertEqual(len(units), len(opening.MECHANISMS) + len(body.BODY))
        for i in body.AUGMENTS:
            self.assertEqual(len(units[i - 1]["occurrences"]), len(opening.MECHANISMS[i - 1]["spans"]) + len(body.AUGMENTS[i]))

    def test_contracts_have_five_fields_without_formal_acceptance(self):
        self.assertEqual(len(body.contracts()), 8)
        for c in body.contracts():
            for k in ("input", "rhetorical_job", "analytical_job", "output", "handoff"):
                self.assertTrue(c[k])
            self.assertIn("not-formal", c["status"])

    def test_proposed_targets_and_comparisons_keep_boundaries(self):
        units = body.build_units(self.pages())
        self.assertIn("proposed operational", units[25]["features"]["quantitative_role"])
        self.assertIn("not verified comparison", units[27]["features"]["quantitative_role"])
        self.assertIn("not proof of matched inputs", units[27]["g3"]["boundary"][0])
        self.assertIn("not independently established dominance", units[28]["g3"]["boundary"][0])


if __name__ == "__main__":
    unittest.main()
