import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from source_paragraph_reviews import apply_paragraph_reviews, validate_paragraph_reviews
from text_corpus import digest, section_text, text_with_block_spans


class SourceParagraphReviewTests(unittest.TestCase):
    def fixture(self):
        blocks=[{'block_id':'a','section_id':'s','kind':'prose','text':'The author sentence crosses',
                 'source_pages':[3],'source_line_ids':['l1']},
                {'block_id':'h','section_id':'s','kind':'furniture','text':'Repeated header',
                 'source_pages':[4],'source_line_ids':['l2']},
                {'block_id':'b','section_id':'s','kind':'prose','text':'the physical page boundary.',
                 'source_pages':[4],'source_line_ids':['l3']},
                {'block_id':'c','section_id':'s','kind':'prose','text':'A new paragraph starts here.',
                 'source_pages':[4],'source_line_ids':['l4']}]
        doc={'paper_id':'synthetic','source_sha256':'a'*64,'raw_pages_sha256':'b'*64,'blocks':blocks,
             'sections':[{'section_id':'s','parent_id':None}],
             'defects':[{'code':'cross_page_join_review','left':'a','right':'b'}]}
        review={'schema':'source-paragraph-join-review-v1',
                **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
                'reviewer':'Synthetic source fixture','reason':'Explicit checked continuation.',
                'checked_pages':[3,4],'evidence_files':{'synthetic.txt':'c'*64},
                'evidence':[{'path':'synthetic.txt','sha256':'c'*64,'description':'Synthetic only.'}],
                'joins':[{'left_block_id':'a','right_block_id':'b','separator':' ',
                          'left_text_sha256':digest(blocks[0]['text'].encode()),
                          'right_text_sha256':digest(blocks[2]['text'].encode()),
                          'reason':'The same sentence spans these two pages.'}]}
        return doc,review

    def test_rendering_joins_checked_fragments_and_preserves_each_source_block(self):
        doc,review=self.fixture();before=copy.deepcopy(doc['blocks'])
        apply_paragraph_reviews(doc,[review]);validate_paragraph_reviews(doc)
        text=section_text(doc,['s'])
        self.assertEqual(text,'The author sentence crosses the physical page boundary.\n\nA new paragraph starts here.')
        self.assertEqual([b['text'] for b in doc['blocks']],[b['text'] for b in before])
        rendered,spans=text_with_block_spans([doc['blocks'][i] for i in (0,2,3)])
        self.assertEqual(rendered,text)
        for span,block in zip(spans,[before[i] for i in (0,2,3)]):
            self.assertEqual(rendered[span['start']:span['end']],block['text'])
        self.assertEqual(doc['defects'][0]['status'],'resolved')
        # Selecting the right fragment alone must never synthesize unseen text.
        self.assertEqual(text_with_block_spans([doc['blocks'][2]])[0],before[2]['text'])
        doc['blocks'][2]['paragraph_continues_from']='wrong'
        with self.assertRaises(ValueError):
            validate_paragraph_reviews(doc)

    def test_join_rejects_changed_text_missing_page_and_intervening_author_content(self):
        for change in ('text','coverage','section','intervening'):
            doc,review=self.fixture()
            if change=='text': doc['blocks'][2]['text']='Changed author words.'
            if change=='coverage': review['checked_pages']=[3]
            if change=='section': doc['blocks'][2]['section_id']='other'
            if change=='intervening': doc['blocks'][1]['kind']='heading'
            with self.assertRaises(ValueError):
                apply_paragraph_reviews(doc,[review])


if __name__=='__main__':
    unittest.main()
