from pathlib import Path
import copy
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from preview_span_origin_flow import merge_text_repairs
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded


class ProspectiveLiteralRepairsTests(unittest.TestCase):
    def test_first_repair_is_added_without_mutating_old_proofs_or_hiding_other_papers(self):
        old = [{'paper_id': 'p', 'tag': 'old'}]
        before = copy.deepcopy(old)
        new = {'paper_id': 'p', 'tag': 'new'}
        self.assertEqual(merge_text_repairs(old, [new, {'paper_id': 'other'}], 'p'), old + [new])
        self.assertEqual(old, before)

    def test_replacement_still_requires_exact_old_proof_binding(self):
        old = {'paper_id': 'p', 'tag': 'old'}
        replacement = {'paper_id': 'p', 'binding_transfer':
                       {'previous_review_sha256': digest(encoded(old))}}
        self.assertEqual(merge_text_repairs([old], [replacement], 'p'), [replacement])
        replacement['binding_transfer']['previous_review_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'exactly one previous'):
            merge_text_repairs([old], [replacement], 'p')

    def test_duplicate_addition_cannot_be_silently_applied_twice(self):
        proof = {'paper_id': 'p', 'tag': 'new'}
        with self.assertRaisesRegex(ValueError, 'already declared'):
            merge_text_repairs([], [proof, proof], 'p')

    def test_new_proof_still_runs_source_validation(self):
        proof = {'paper_id': 'p', 'operations': [{'block_id': 'missing'}]}
        merged = merge_text_repairs([], [proof], 'p')
        with self.assertRaisesRegex(ValueError, 'Incomplete or stale'):
            apply_text_repairs({'paper_id': 'p', 'source_sha256': 'a', 'raw_pages_sha256': 'b',
                                'blocks': []}, merged)


if __name__ == '__main__':
    unittest.main()
