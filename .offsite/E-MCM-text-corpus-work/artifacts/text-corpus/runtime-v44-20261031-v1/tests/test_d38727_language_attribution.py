import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import correct_d38727_language_attribution as attribution
import stage_d38727_language_links as links


def fixture_record():
    units = []
    for n in list(attribution.REVISIONS) + [1]:
        units.append({
            "language_unit_id": f"LU-D-2015-38727-REPAIR-{n:03d}",
            "page": 1, "printed_page": None, "section": "Summary", "chapter": "abstract",
            "source_excerpt": "Independent synthetic witness.", "occurrences": [],
            "candidate_pattern_ids": [f"CP-D-2015-38727-REPAIR-{1 if n == 36 else n:02d}"],
            "disposition": "single-paper draft", "function": "original function", "rhetorical_move": "original function",
            "reusable_pattern": "Original frame.", "information_order": ["original order"],
            "reusable_elements": ["stable function: original function", "order: original order", "slots: original slot"],
            "prohibited_generalizations": ["Keep source limits."],
            "g3": {"stable_function": "original function", "order": ["original order"],
                   "slots": ["original slot"], "boundary": ["Keep source limits."], "cross_paper_support_count": 0},
            "features": {"transition": "original order", "original_instantiations": ["First invented sentence.", "Second invented sentence."]},
        })
    return {"paper_id": attribution.PID, "units": units}


class D38727LanguageAttributionTests(unittest.TestCase):
    def setUp(self):
        self.before = fixture_record()
        self.after, self.notes = attribution.revise(self.before)

    def test_seven_corrections_preserve_source_anchors_and_unaffected_unit(self):
        attribution.verify_preservation(self.before, self.after, self.notes)
        self.assertEqual(len(self.notes), 7)
        self.assertEqual(self.after["units"][-1], self.before["units"][-1])
        self.assertNotEqual(self.after["units"][0], self.before["units"][0])
        self.assertEqual(self.before["units"][0]["function"], "original function")

    def test_source_action_and_editorial_boundary_are_distinct(self):
        note = next(n for n in self.notes if n["language_unit_id"].endswith("-015"))
        self.assertNotIn("universal", note["after"]["function"])
        self.assertIn("does not itself enforce", note["editorial_boundary"])
        self.assertNotEqual(note["observed_action"], note["editorial_boundary"])

    def test_duplicate_annotations_follow_corrected_function_and_order(self):
        for note in self.notes:
            unit = note["after"]
            self.assertEqual(unit["rhetorical_move"], unit["function"])
            self.assertEqual(unit["g3"]["stable_function"], unit["function"])
            self.assertEqual(unit["features"]["transition"], " > ".join(unit["information_order"]))
            self.assertEqual(unit["g3"]["order"], unit["information_order"])
        self.after["units"][0]["rhetorical_move"] = "Unreviewed replacement."
        with self.assertRaisesRegex(ValueError, "differs from the reviewed"):
            attribution.verify_preservation(self.before, self.after, self.notes)

    def test_scenario_is_explicit_in_both_replacement_examples(self):
        unit = next(u for u in self.after["units"] if u["language_unit_id"].endswith("-030"))
        self.assertEqual(len(unit["features"]["original_instantiations"]), 2)
        self.assertTrue(all("scenario" in e and "projected" in e for e in unit["features"]["original_instantiations"]))
        old = next(n["before"] for n in self.notes if n["language_unit_id"].endswith("-030"))
        self.assertEqual(old["features"]["original_instantiations"], ["First invented sentence.", "Second invented sentence."])

    def test_new_slot_names_require_reviewed_types_without_altering_default(self):
        unit = next(u for u in self.after["units"] if u["language_unit_id"].endswith("-036"))
        with self.assertRaisesRegex(ValueError, "typed slot mismatch"):
            links.slot_records(unit)
        slots = links.slot_records(unit, attribution.SLOT_TYPES)
        self.assertIn("analytical consequence", [s["placeholder"] for s in slots])
        bad = copy.deepcopy(unit)
        bad["reusable_pattern"] += " [unknown]"
        with self.assertRaisesRegex(ValueError, "typed slot mismatch"):
            links.slot_records(bad, attribution.SLOT_TYPES)

    def test_changed_source_or_candidate_target_rejected(self):
        self.after["units"][0]["occurrences"].append({"page": 2})
        with self.assertRaisesRegex(ValueError, "source/identity/support field"):
            attribution.verify_preservation(self.before, self.after, self.notes)

    def test_unreviewed_example_change_rejected(self):
        self.after["units"][0]["features"]["original_instantiations"][0] = "Unreviewed replacement."
        with self.assertRaisesRegex(ValueError, "unreviewed example"):
            attribution.verify_preservation(self.before, self.after, self.notes)

    def test_support_inflation_rejected(self):
        self.after["units"][0]["g3"]["cross_paper_support_count"] = 2
        with self.assertRaisesRegex(ValueError, "support count changed"):
            attribution.verify_preservation(self.before, self.after, self.notes)

    def test_existing_generation_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            keep = path / "old.txt"
            keep.write_bytes(b"keep")
            with self.assertRaises(FileExistsError):
                attribution.build(path)
            self.assertEqual(keep.read_bytes(), b"keep")


if __name__ == "__main__":
    unittest.main()
