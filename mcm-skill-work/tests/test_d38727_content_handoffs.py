import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import stage_d38727_content_handoffs as content


class D38727ContentHandoffTests(unittest.TestCase):
    def setUp(self):
        self.pages = {7: "\n" * 45 + "Case Study: test\nA complete data set was available\n" + "\n" * 6}
        self.chain = copy.deepcopy(content.CHAINS[0])
        self.chain["nodes"] = [content.node("input", 7, 46, 47, "complete data set"),
                               content.node("output", 7, 47, 47, "was available")]

    def test_witnesses_keep_exact_line_anchors_and_transition(self):
        result = content.attach_witnesses([self.chain], self.pages)[0]
        self.assertEqual(len(result["transitions"]), 1)
        self.assertEqual(result["nodes"][0]["printed_page"], 6)
        self.assertEqual(result["nodes"][0]["text"], "Case Study: test\nA complete data set was available")
        self.assertEqual(len(result["nodes"][0]["excerpt_sha256"]), 64)

    def test_paused_formula_chart_table_and_reference_ranges_rejected(self):
        for page, line in [(3, 4), (7, 15), (9, 23), (13, 37), (14, 5), (16, 29), (18, 4)]:
            bad = copy.deepcopy(self.chain)
            bad["nodes"][0].update(physical_page=page, first_line=line, last_line=line)
            with self.subTest(page=page, line=line), self.assertRaisesRegex(ValueError, "outside allowed author prose"):
                content.attach_witnesses([bad], self.pages)

    def test_wrong_source_phrase_rejected(self):
        self.chain["nodes"][0]["expected_phrase"] = "not in this source"
        with self.assertRaisesRegex(ValueError, "source phrase drift"):
            content.attach_witnesses([self.chain], self.pages)

    def test_causal_effect_promotion_rejected(self):
        self.chain["terminal_status"] = "causally_verified_effect"
        with self.assertRaisesRegex(ValueError, "evidentiary promotion"):
            content.attach_witnesses([self.chain], self.pages)

    def test_existing_language_links_required(self):
        chains = content.attach_witnesses([self.chain], self.pages)
        units = [{"language_unit_id": f"LU-D-2015-38727-REPAIR-{n:03d}"} for n in [5, 16, 17]]
        mapping = copy.deepcopy(units)
        content.validate_links(chains, units, mapping)
        self.assertEqual(len(chains[0]["language_unit_ids"]), 3)
        with self.assertRaisesRegex(ValueError, "unknown or unlinked"):
            content.validate_links(chains, units, mapping[:-1])

    def test_boundary_and_complete_transition_path_required(self):
        chains = content.attach_witnesses([self.chain], self.pages)
        chains[0]["boundary"] = ""
        with self.assertRaisesRegex(ValueError, "incomplete content"):
            content.validate_links(chains, [], [])
        chains = content.attach_witnesses([self.chain], self.pages)
        chains[0]["transitions"] = []
        with self.assertRaisesRegex(ValueError, "incomplete handoff path"):
            content.validate_links(chains, [], [])

    def test_existing_output_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            keep = path / "previous.txt"
            keep.write_bytes(b"preserve")
            with self.assertRaises(FileExistsError):
                content.build(path)
            self.assertEqual(keep.read_bytes(), b"preserve")


if __name__ == "__main__":
    unittest.main()
