import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from corpus_queries import select_sections, selected_blocks
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from text_corpus import digest, make_document, text_with_block_spans, title_role


class ReviewedExecutiveSummaryTests(unittest.TestCase):
    def fixture(self):
        texts = [[], ['Summary', 'Opening technical abstract.'],
                 ['1 Introduction', 'The main paper starts here.'], [], [],
                 ['References', 'A bibliography entry.'],
                 ['Executive Summary', 'A complete later executive summary.']]
        pages = []
        for number, values in enumerate(texts[1:], 1):
            lines = [{'line_id': f'p{number:04d}-n{i:04d}-l0000',
                      'page': number, 'native_block': i, 'text': text,
                      'bbox': [70, 100 + i*22, 520, 114 + i*22],
                      'font_size': 11, 'bold': i == 0, 'spans': []}
                     for i, text in enumerate(values)]
            pages.append({'page': number, 'width': 612, 'height': 792,
                          'lines': lines, 'comparison': {'status': 'agreement'}})
        groups = []
        for i, line in enumerate(pages[-1]['lines']):
            groups.append({'group_id': f'g{i}', 'kind': 'heading' if i == 0 else 'prose',
                           'source_line_ids': [line['line_id']],
                           'text_sha256': digest(line['text'].encode()),
                           'reason': 'Source-checked late independent Executive Summary.',
                           **({'opens_section': {'role': 'abstract', 'level': 1,
                               'source_context': 'independent-executive-summary'}} if i == 0 else {})})
        meta = {'paper_id': 'synthetic', 'source_sha256': 'a'*64, 'raw_pages_sha256': 'b'*64}
        review = {'schema': 'source-text-layout-review-v1', **meta,
                  'reviewer': 'Synthetic regression', 'reason': 'Later summary must be separately selectable.',
                  'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
                  'evidence_files': {'synthetic': 'c'*64}, 'pages': [{'page': 6, 'groups': groups}]}
        return meta, pages, review

    def test_reviewed_late_summary_is_selected_after_bibliography_without_changing_global_guess(self):
        meta, pages, review = self.fixture()
        originals = copy.deepcopy(pages)
        self.assertEqual(title_role('Executive Summary', 6), 'conclusion')
        applied = apply_layout_reviews(meta, pages, [review])
        doc = make_document(meta, pages, improved=True)
        doc['layout_reviews'] = applied
        validate_layout_reviews(doc, originals)
        ids, excluded = select_sections(doc, 'abstract')
        text, _ = text_with_block_spans(selected_blocks(doc, {'section_ids': ids,
                                                           'excluded_roles': sorted(excluded)}))
        self.assertIn('Opening technical abstract.', text)
        self.assertIn('complete later executive summary.', text)
        self.assertNotIn('bibliography entry', text)
        self.assertNotIn('main paper starts', text)
        late = next(s for s in doc['sections'] if s['title'] == 'Executive Summary')
        self.assertIsNone(late['parent_id'])
        self.assertEqual(late['origin'], 'reviewed-context-heading')
        late['source_role_context'] = 'guessed'
        with self.assertRaises(ValueError):
            validate_layout_reviews(doc, originals)

    def test_context_rejects_an_ordinary_conclusion_wrong_role_and_child_level(self):
        for mutation in ('wrong-title', 'wrong-role', 'child-level', 'extra-field'):
            meta, pages, review = self.fixture()
            group = review['pages'][0]['groups'][0]
            if mutation == 'wrong-title':
                pages[-1]['lines'][0]['text'] = 'Conclusions'
                group['text_sha256'] = digest(b'Conclusions')
            elif mutation == 'wrong-role':
                group['opens_section']['role'] = 'conclusion'
            elif mutation == 'child-level':
                group['opens_section']['level'] = 2
            else:
                group['opens_section']['arbitrary_override'] = True
            with self.assertRaises(ValueError):
                apply_layout_reviews(meta, pages, [review])


if __name__ == '__main__':
    unittest.main()
