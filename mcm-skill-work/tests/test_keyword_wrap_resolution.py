"""Checked keyword restoration retains author-query separation and exact proofs."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from corpus_queries import all_author_blocks
from source_text_repairs import apply_text_repairs, replay_block, validate_hyphen_resolutions
from text_corpus import digest, encoded, text_with_block_spans


class KeywordWrapResolutionTests(unittest.TestCase):
    def fixture(self, kind='keywords'):
        original = 'Keywords: Perfor- mance Metrics.'
        restored = 'Keywords: Performance Metrics.'
        keyword = {'block_id': 'k', 'kind': kind, 'section_id': 's', 'text': original,
                   'source_line_ids': ['k1', 'k2'], 'source_pages': [1], 'issues': ['hyphen_join_review']}
        document = {'paper_id': 'synthetic-keyword', 'source_sha256': 'a' * 64, 'raw_pages_sha256': 'b' * 64,
            'sections': [{'section_id': 's', 'role': 'abstract', 'parent_id': None}],
            'blocks': [{'block_id': 'body', 'kind': 'prose', 'section_id': 's', 'text': 'The full author paragraph.',
                        'source_pages': [1], 'source_line_ids': ['a1'], 'issues': []}, keyword],
            'defects': [{'code': 'hyphen_join_review', 'block_id': 'k', 'page': 1}]}
        literal = {'block_id': 'k', 'operation': 'literal_replace', 'old': 'Perfor- ', 'new': 'Perfor', 'count': 1,
                   'before_text_sha256': digest(original.encode()), 'after_text_sha256': digest(restored.encode()),
                   'reason': 'Synthetic exact printed wrap.'}
        resolution = {'block_id': 'k', 'operation': 'resolve_hyphen_join_review',
            'before_text_sha256': digest(restored.encode()), 'after_text_sha256': digest(restored.encode()),
            'source_line_ids_sha256': digest(encoded(['k1', 'k2'])),
            'transcription_operations_sha256': digest(encoded([literal])), 'reason': 'Synthetic complete keyword check.'}
        review = {'paper_id': document['paper_id'], 'source_sha256': document['source_sha256'],
            'raw_pages_sha256': document['raw_pages_sha256'], 'reviewer': 'synthetic-test-only',
            'reason': 'Restore separate keyword text only.', 'checked_pages': [1],
            'operations': [literal, resolution], 'evidence': [{'path': 'synthetic.txt', 'sha256': 'c' * 64,
                                                             'description': 'Synthetic source evidence.'}]}
        return document, review, original, restored

    def test_keyword_wrap_replays_but_never_enters_default_author_text(self):
        document, review, original, restored = self.fixture()
        apply_text_repairs(document, [review])
        keyword = document['blocks'][1]
        self.assertEqual((keyword['kind'], keyword['text'], keyword['issues']), ('keywords', restored, []))
        self.assertEqual(replay_block(document, keyword, original), restored)
        self.assertEqual(text_with_block_spans(all_author_blocks(document))[0], 'The full author paragraph.')
        self.assertEqual(document['defects'][0]['status'], 'resolved')
        for field, value in [('text', restored + ' changed'), ('source_line_ids', ['k1'])]:
            changed = copy.deepcopy(document)
            changed['blocks'][1][field] = value
            with self.assertRaises(ValueError):
                validate_hyphen_resolutions(changed)

    def test_no_resolution_for_other_non_author_objects_or_unbound_keyword(self):
        for kind in ('caption', 'title', 'furniture', 'front_matter'):
            document, review, _, _ = self.fixture(kind)
            with self.assertRaises(ValueError):
                apply_text_repairs(document, [review])
        document, review, _, _ = self.fixture()
        review['operations'][-1]['source_line_ids_sha256'] = '0' * 64
        with self.assertRaises(ValueError):
            apply_text_repairs(document, [review])


if __name__ == '__main__':
    unittest.main()
