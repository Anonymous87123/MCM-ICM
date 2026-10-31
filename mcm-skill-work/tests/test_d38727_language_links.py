import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import stage_d38727_language_links as links


def fixture_record():
    units = []
    specs = [
        (1, 1, 1, "abstract", "[tool] identifies [condition] so [audience] can prioritise [action]."),
        (36, 1, 2, "introduction", "The [tool] connects [unmet need] and [candidate action] through [measured consequence]."),
        (37, 37, 3, "model-establishment", "[inputs] were selected for their reported relation to [target], not because every input is an established causal driver."),
    ]
    for number, pattern_number, page, chapter, frame in specs:
        units.append({
            "language_unit_id": f"LU-D-2015-38727-REPAIR-{number:03d}",
            "candidate_pattern_ids": [f"CP-D-2015-38727-REPAIR-{pattern_number:02d}"],
            "chapter": chapter, "page": page, "printed_page": None if page == 1 else page - 1,
            "section": chapter, "function": "synthetic functional variant " + str(number),
            "source_excerpt": "An independent source witness.", "reusable_pattern": frame,
            "information_order": ["context", "operation", "handoff"],
            "g3": {"slots": ["semantic role"], "variants": ["positional variant"], "boundary": ["No stronger evidentiary claim."]},
            "occurrences": [{"page": page, "section": chapter, "locator": "opening", "source_excerpt": "An independent source witness."}],
            "features": {"voice": "active", "tense": "present", "modality": "limited",
                         "original_instantiations": [f"The register assigns uncertain ownership entries to another review session {number}.",
                                                     f"The access map keeps both temporary pathways available throughout the repair interval {number}."]},
        })
    return {"paper_id": links.PID, "source_sha256": "a" * 64,
            "source_specific_terms": [], "units": units}


class D38727LanguageLinkTests(unittest.TestCase):
    def setUp(self):
        self.record = fixture_record()
        self.package = links.assemble(self.record)

    def test_complete_variant_aware_links_preserve_every_example(self):
        self.assertEqual(links.validate_links(self.record, self.package), [])
        self.assertEqual(len(self.package["patterns"]), 2)
        shared = self.package["patterns"][0]
        self.assertEqual(shared["source_unit_count"], 2)
        self.assertEqual(len(shared["original_instantiations"]), 4)
        self.assertEqual(shared["independent_paper_count"], 1)
        self.assertEqual(len(self.package["mapping"]), 3)

    def test_every_frame_placeholder_has_a_typed_slot(self):
        for unit in self.record["units"]:
            self.assertTrue(all(s["semantic_type"] for s in links.slot_records(unit)))
        bad = copy.deepcopy(self.record["units"][0])
        bad["reusable_pattern"] += " [unreviewed slot]"
        with self.assertRaisesRegex(ValueError, "typed slot mismatch"):
            links.slot_records(bad)

    def test_two_variant_pairs_are_scanned_without_truncation(self):
        profile = links.anticopy.build_source_profile("The synthetic source has no example wording.", 8)
        scans = links.scan_examples(self.record, profile)
        self.assertEqual(len(scans), 3)
        self.assertTrue(all(s["example_count"] == 2 and s["result"] == "pass" for s in scans))
        self.assertEqual(sum(s["example_count"] for s in scans), 6)

    def test_missing_variant_example_is_rejected(self):
        self.package["patterns"][0]["original_instantiations"].pop()
        self.assertTrue(any("example loss" in e for e in links.validate_links(self.record, self.package)))

    def test_independent_paper_inflation_is_rejected(self):
        self.package["patterns"][0]["independent_paper_count"] = 2
        self.assertTrue(any("inflated pattern support" in e for e in links.validate_links(self.record, self.package)))

    def test_premature_rule_promotion_is_rejected(self):
        self.package["rules"][0]["lifecycle"] = "promoted"
        self.assertTrue(any("unjustified rule promotion" in e for e in links.validate_links(self.record, self.package)))

    def test_missing_mapping_and_wrong_page_are_rejected(self):
        self.package["mapping"][0]["physical_page"] = 19
        self.assertTrue(any("page drift" in e for e in links.validate_links(self.record, self.package)))
        self.package["mapping"].pop()
        self.assertTrue(any("not bijective" in e for e in links.validate_links(self.record, self.package)))

    def test_observation_shape_matches_existing_schema_fields(self):
        for obs in self.package["observations"]:
            self.assertEqual(set(obs), set(links.paper.REQUIRED_OBSERVATION_FIELDS))
            self.assertIsInstance(obs["source_basis"], str)
            self.assertIsInstance(obs["applicability"], list)
            self.assertIsInstance(obs["counterevidence"], list)
        self.package["observations"][0]["source_basis"] = {"excerpt": "incorrect adapter"}
        self.package["observations"][0]["review_status"] = "extra field"
        errors = links.validate_links(self.record, self.package)
        self.assertIn("observation additional fields", errors)
        self.assertIn("observation non-text source_basis", errors)

    def test_rule_evidence_backlink_cannot_be_removed(self):
        self.package["rules"][0]["evidence_ids"].pop()
        self.assertTrue(any("backlink" in e or "evidence link loss" in e for e in links.validate_links(self.record, self.package)))

    def test_existing_output_is_preserved_before_reading_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            keep = path / "old.txt"
            keep.write_bytes(b"previous generation")
            with mock.patch.object(links.storage, "read_json") as reader:
                with self.assertRaises(FileExistsError):
                    links.build(path)
                reader.assert_not_called()
            self.assertEqual(keep.read_bytes(), b"previous generation")


if __name__ == "__main__":
    unittest.main()
