"""Exact source-reviewed inline labels must preserve the entire first paragraph."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from text_corpus import digest, make_document, section_text


class ReviewedInlineHeadingTests(unittest.TestCase):
    def fixture(self):
        texts = ['1. Introduction An entire first sentence remains author prose.',
                 'A second paragraph belongs to the same introduction.',
                 '2. Problem Statement A different first sentence remains intact.']
        lines = [{'line_id': f'p0004-n{i:04d}-l0000', 'page': 4,
                  'native_block': i, 'text': text, 'bbox': [70,100+i*50,520,112+i*50],
                  'font_size': 11, 'bold': False, 'spans': []}
                 for i,text in enumerate(texts)]
        pages = [{'page':p, 'width':612, 'height':792, 'lines':lines if p==4 else [],
                  'comparison':{'status':'agreement'}} for p in range(1,5)]
        groups = [{'group_id':f'g{i}', 'kind':'prose', 'source_line_ids':[line['line_id']],
                   'text_sha256':digest(line['text'].encode()), 'reason':'Source-reviewed paragraph.'}
                  for i,line in enumerate(lines)]
        groups[0]['opens_section']={'role':'introduction','level':1,'inline_title_prefix':'1. Introduction'}
        groups[2]['opens_section']={'role':'problem_restatement','level':1,'inline_title_prefix':'2. Problem Statement'}
        meta = {'paper_id':'test-inline','source_sha256':'a'*64,'raw_pages_sha256':'b'*64}
        review = {'schema':'source-text-layout-review-v1', **meta,
                  'reviewer':'Synthetic regression fixture', 'reason':'Literal inline headings.',
                  'evidence_files':{'fixture':'c'*64}, 'paragraph_boundaries_checked':True,
                  'reading_lanes_checked':True,'pages':[{'page':4,'groups':groups}]}
        return meta,pages,review,texts

    def test_inline_label_keeps_first_sentence_and_exact_source_ownership(self):
        meta,pages,review,texts = self.fixture()
        applied=apply_layout_reviews(meta,pages,[review])
        doc=make_document(meta,pages,improved=True)
        doc['layout_reviews']=applied
        validate_layout_reviews(doc,pages)
        intro=next(s for s in doc['sections'] if s['role']=='introduction')
        problem=next(s for s in doc['sections'] if s['role']=='problem_restatement')
        self.assertEqual(intro['title'],'1. Introduction')
        self.assertEqual(intro['origin'],'reviewed-inline-heading')
        self.assertEqual(section_text(doc,[intro['section_id']]), '\n\n'.join(texts[:2]))
        self.assertEqual(section_text(doc,[problem['section_id']]),texts[2])
        self.assertEqual([b['text'] for b in doc['blocks']],texts)
        self.assertEqual([x for b in doc['blocks'] for x in b['source_line_ids']],
                         [x['line_id'] for x in pages[3]['lines']])
        changed=copy.deepcopy(doc)
        next(s for s in changed['sections'] if s['role']=='introduction')['title']='Introduction invented'
        with self.assertRaises(ValueError):
            validate_layout_reviews(changed,pages)

    def test_inline_title_must_be_literal_prefix_with_correct_role(self):
        meta,pages,review,_=self.fixture()
        for changes in ({'inline_title_prefix':'Introduction'},
                        {'inline_title_prefix':'1. Intro'}, {'role':'model'}):
            bad=copy.deepcopy(review)
            bad['pages'][0]['groups'][0]['opens_section'].update(changes)
            with self.assertRaises(ValueError):
                apply_layout_reviews(meta,copy.deepcopy(pages),[bad])


if __name__=='__main__':
    unittest.main()
