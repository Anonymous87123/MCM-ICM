"""Explicit reviewed paragraphs must not inherit an unused gap inference."""
import copy
from collections import Counter
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from text_corpus import digest, make_document


class ReviewedSpacingPathTests(unittest.TestCase):
    def setUp(self):
        self.meta = {'paper_id': 'synthetic-spacing', 'source_sha256': 'a' * 64,
                     'raw_pages_sha256': 'b' * 64}
        self.lines = [{'line_id': 'heading', 'page': 1, 'native_block': 0,
            'text': 'Summary', 'bbox': [240, 80, 330, 96], 'font_size': 14, 'bold': True}]
        self.lines += [{'line_id': f'line-{i}', 'page': 1, 'native_block': i + 1,
            'text': f'The source continuation contains many original author words number {i}' + ('.' if i == 7 else ''),
            'bbox': [72, 120 + i * 24, 520, 132 + i * 24], 'font_size': 11, 'bold': False} for i in range(8)]
        self.pages = [{'page': 1, 'width': 595, 'height': 842, 'lines': self.lines,
                       'comparison': {'status': 'agreement'}}]
        self.groups = [self.group('heading', 'heading', self.lines[:1]),
                       self.group('paragraph', 'prose', self.lines[1:])]
        self.groups[0]['opens_section'] = {'role': 'abstract', 'level': 1}
        self.review = {'schema': 'source-text-layout-review-v1', **self.meta,
            'reviewer': 'synthetic-test-only', 'reason': 'Synthetic complete source paragraph fixture.',
            'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
            'evidence_files': {'synthetic.txt': 'c' * 64}, 'pages': [{'page': 1, 'groups': self.groups}]}

    @staticmethod
    def group(name, kind, lines):
        return {'group_id': name, 'kind': kind, 'source_line_ids': [x['line_id'] for x in lines],
                'text_sha256': digest(' '.join(x['text'] for x in lines).encode()), 'reason': 'Synthetic checked source group.'}

    def reviewed(self):
        pages = copy.deepcopy(self.pages)
        reviews = apply_layout_reviews(self.meta, pages, [self.review])
        doc = make_document(self.meta, pages, improved=True)
        doc['layout_reviews'] = reviews
        validate_layout_reviews(doc, self.pages)
        return doc

    def test_reviewed_path_uses_exact_groups_not_gap_heuristic(self):
        with patch('text_corpus.prose_gap_limit', side_effect=AssertionError('Unused inference invoked')):
            doc = self.reviewed()
        self.assertEqual(doc['blocks'][-1]['text'], ' '.join(x['text'] for x in self.lines[1:]))
        self.assertNotIn('expanded_line_spacing_review', [x['code'] for x in doc['defects']])
        self.assertEqual(Counter(lid for b in doc['blocks'] for lid in b['source_line_ids']),
                         Counter(x['line_id'] for x in self.lines))

    def test_unreviewed_path_still_flags_wide_spacing(self):
        doc = make_document(self.meta, copy.deepcopy(self.pages), improved=True)
        self.assertIn('expanded_line_spacing_review', [x['code'] for x in doc['defects']])
        self.assertTrue(all(s['boundary_status'] == 'pending' for s in doc['sections']))

    def test_layout_does_not_approve_section_or_remove_glyph_review(self):
        self.lines[1]['text'] += ' \uf061'
        self.groups[1] = self.group('paragraph', 'prose', self.lines[1:])
        doc = self.reviewed()
        self.assertIn('private_use_glyph_review', [x['code'] for x in doc['defects']])
        self.assertTrue(all(s['boundary_status'] == 'pending' for s in doc['sections']))

    def test_missing_duplicate_or_stale_groups_rejected_before_reconstruction(self):
        for mutation in ('missing', 'duplicate', 'stale'):
            review = copy.deepcopy(self.review)
            group = review['pages'][0]['groups'][1]
            if mutation == 'missing':
                group['source_line_ids'].pop()
            elif mutation == 'duplicate':
                group['source_line_ids'].append(group['source_line_ids'][0])
            else:
                group['text_sha256'] = 'f' * 64
            with self.assertRaises(ValueError):
                apply_layout_reviews(self.meta, copy.deepcopy(self.pages), [review])


if __name__ == '__main__':
    unittest.main()
