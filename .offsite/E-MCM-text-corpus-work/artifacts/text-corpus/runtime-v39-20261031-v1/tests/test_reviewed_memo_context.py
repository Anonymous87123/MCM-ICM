import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from corpus_queries import select_sections, selected_blocks
from text_corpus import digest, make_document, text_with_block_spans


class ReviewedMemoContextTests(unittest.TestCase):
    def fixture(self):
        texts = ['An untitled technical abstract.', 'To: River managers',
                 'Date: February 13, 2012', 'Subject: Campsite utilization',
                 '1. Summary', 'This summary belongs to the management memo.',
                 '1 Summary', 'A second technical abstract remains separate.']
        pages = []
        for number, indices in ((1, [0]), (2, list(range(1, 6))), (3, [6, 7])):
            lines = [{'line_id': f'p{number:04d}-n{i:04d}-l0000', 'page': number,
                      'native_block': i, 'text': texts[i], 'bbox': [70, 100+i*20, 520, 112+i*20],
                      'font_size': 11, 'bold': i == 6, 'spans': []} for i in indices]
            pages.append({'page': number, 'width': 612, 'height': 792, 'lines': lines,
                          'comparison': {'status': 'agreement'}})
        def group(number, name, kind, indices, opening=None):
            lines = [line for line in pages[number-1]['lines'] if line['native_block'] in indices]
            return {'group_id': name, 'kind': kind, 'source_line_ids': [x['line_id'] for x in lines],
                    'text_sha256': digest(' '.join(x['text'] for x in lines).encode()),
                    'reason': 'Synthetic source-checked ownership.',
                    **({'opens_section': opening} if opening else {})}
        groups = [group(2, 'header', 'author_callout', [1, 2, 3],
                        {'role': 'memo', 'level': 1, 'source_context': 'memo-recipient-header'}),
                  group(2, 'summary', 'heading', [4],
                        {'role': 'other', 'level': 2, 'source_context': 'memo-summary-subsection'}),
                  group(2, 'memo-body', 'prose', [5])]
        meta = {'paper_id': 'synthetic', 'source_sha256': 'a'*64, 'raw_pages_sha256': 'b'*64}
        review = {'schema': 'source-text-layout-review-v1', **meta,
                  'reviewer': 'Synthetic regression', 'reason': 'Memo has a local Summary heading.',
                  'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
                  'evidence_files': {'synthetic': 'c'*64}, 'pages': [{'page': 2, 'groups': groups}]}
        return meta, pages, review

    def test_memo_summary_keeps_literal_text_and_is_not_a_technical_abstract(self):
        meta, pages, review = self.fixture()
        original = copy.deepcopy(pages)
        applied = apply_layout_reviews(meta, pages, [review])
        doc = make_document(meta, pages, improved=True)
        doc['layout_reviews'] = applied
        validate_layout_reviews(doc, original)
        def text(query):
            ids, excluded = select_sections(doc, query)
            return text_with_block_spans(selected_blocks(doc, {'section_ids': ids,
                'excluded_roles': sorted(excluded)}))[0]
        self.assertIn('untitled technical abstract', text('abstract'))
        self.assertIn('second technical abstract', text('abstract'))
        self.assertNotIn('management memo', text('abstract'))
        self.assertIn('1. Summary', text('memo'))
        self.assertIn('management memo', text('memo'))
        summary = next(s for s in doc['sections'] if s['title'] == '1. Summary')
        self.assertEqual(next(s for s in doc['sections'] if s['section_id'] == summary['parent_id'])['role'], 'memo')
        summary['parent_id'] = None
        with self.assertRaises(ValueError):
            validate_layout_reviews(doc, original)

    def test_context_is_limited_to_exact_source_recipient_header_and_local_summary(self):
        for mutation in ('missing-date', 'wrong-role', 'orphan-summary', 'arbitrary-context'):
            meta, pages, review = self.fixture()
            groups = review['pages'][0]['groups']
            if mutation == 'missing-date':
                pages[1]['lines'][1]['text'] = 'An ordinary body sentence.'
                groups[0]['text_sha256'] = digest(' '.join(x['text'] for x in pages[1]['lines'][:3]).encode())
            elif mutation == 'wrong-role':
                groups[1]['opens_section']['role'] = 'abstract'
            elif mutation == 'orphan-summary':
                del groups[0]['opens_section']
            else:
                groups[0]['opens_section']['source_context'] = 'guess-from-theme'
            with self.assertRaises(ValueError):
                apply_layout_reviews(meta, pages, [review])


if __name__ == '__main__':
    unittest.main()
