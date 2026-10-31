import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import stage_d38996_text_first as stage
import validate_language_units as language


class TextFirstOpeningTests(unittest.TestCase):
    def pages(self):
        base = stage.ROOT / f"artifacts/papers/{stage.PID}/text/pages"
        return {i: (base / f"page-{i:04d}.txt").read_text(encoding="utf-8") for i in (1, 3, 4)}

    def test_create_only_preserves_existing_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "existing.json"
            p.write_bytes(b"original")
            with self.assertRaises(FileExistsError):
                stage.put_new(p, b"replacement")
            self.assertEqual(p.read_bytes(), b"original")

    def test_existing_stage_is_rejected_before_reading_inputs(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileExistsError):
                stage.build(Path(d), root=Path(d) / "missing-root")

    def test_bad_or_corrupt_ranges_are_rejected(self):
        with self.assertRaises(ValueError):
            stage.source_span({1: "a\nb"}, 1, 0, 2)
        with self.assertRaises(ValueError):
            stage.source_span({1: "a\n\ufffd"}, 1, 1, 2)

    def test_all_opening_units_have_source_and_schema_bindings(self):
        pages = self.pages()
        self.assertEqual(len(stage.REGISTERS), len(stage.MECHANISMS))
        for i, item in enumerate(stage.MECHANISMS, 1):
            u = stage.construct_unit(item, i, pages)
            self.assertEqual(language.validate_unit(u, "D", 21, None, i), [])
            self.assertEqual(len(u["features"]["original_instantiations"]), 2)
            self.assertEqual(u["g3"]["cross_paper_support_count"], 0)
            self.assertEqual(u["function"], u["rhetorical_move"])
            self.assertEqual(u["features"]["modality"], stage.REGISTERS[i - 1][1])
            self.assertIn(u["source_excerpt"], u["occurrences"][0]["source_excerpt"])
            anchor = u["source_excerpt_anchor"]
            self.assertEqual(u["source_excerpt"], stage.source_span(pages, anchor["page"], anchor["first_line"], anchor["last_line"]))
            for o in u["occurrences"]:
                self.assertEqual(o["printed_page"], None if o["page"] == 1 else o["page"] - 1)
                self.assertEqual(o["source_excerpt"], stage.source_span(pages, o["page"], o["first_line"], o["last_line"]))

    def test_borrowed_introductory_definition_has_no_positive_unit(self):
        for item in stage.MECHANISMS:
            for page, first, last, *_ in item["spans"]:
                self.assertFalse(page == 3 and first < 24)
        for gid, *_rest, links, _boundary in stage.GROUPS:
            if gid in {"INTRO-01", "INTRO-02", "INTRO-04"}:
                self.assertEqual(links, [])

    def test_causal_and_baseline_boundaries_are_not_waived(self):
        self.assertIn("matched counterfactual", stage.MECHANISMS[3]["boundary"])
        self.assertIn("simulation", stage.MECHANISMS[6]["boundary"])
        self.assertIn("not a verified mathematical identity", stage.MECHANISMS[10]["boundary"])

    def test_announced_work_and_reported_results_keep_distinct_registers(self):
        self.assertIn("reported result", stage.REGISTERS[2][0])
        self.assertIn("simulation-conditioned", stage.REGISTERS[6][1])
        self.assertIn("not a check result", stage.REGISTERS[11][1])
        self.assertEqual(len({r[2] for r in stage.REGISTERS}), 12)


if __name__ == "__main__":
    unittest.main()
