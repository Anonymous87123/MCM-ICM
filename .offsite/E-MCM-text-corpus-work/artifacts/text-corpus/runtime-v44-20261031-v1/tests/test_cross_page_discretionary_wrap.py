"""Source-bound repair for a real failure: Executive Summary ends at In addi-."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from source_paragraph_reviews import apply_paragraph_reviews,validate_paragraph_reviews
from text_corpus import digest,text_with_block_spans,title_role


class CrossPageDiscretionaryWrapTests(unittest.TestCase):
    def fixture(self):
        a={'block_id':'a','section_id':'s','kind':'prose','text':'It has strengths. In addi',
           'source_pages':[3],'source_line_ids':['p3']}
        h={'block_id':'h','section_id':'s','kind':'furniture','text':'Control #8362 4',
           'source_pages':[4],'source_line_ids':['header']}
        b={'block_id':'b','section_id':'s','kind':'prose','text':'tion to flexibility, it is efficient.',
           'source_pages':[4],'source_line_ids':['p4']}
        doc={'paper_id':'synthetic','source_sha256':'a'*64,'raw_pages_sha256':'b'*64,
             'blocks':[a,h,b],'sections':[{'section_id':'s','parent_id':None}],
             'text_repair_reviews':[{'operations':[{'block_id':'a','operation':'literal_replace',
                 'old':'addi-','new':'addi','count':1,
                 'before_text_sha256':digest((a['text']+'-').encode()),
                 'after_text_sha256':digest(a['text'].encode())}]}]}
        review={'schema':'source-paragraph-join-review-v1',
            **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
            'reviewer':'Synthetic source fixture','reason':'Checked physical-page wrap.',
            'checked_pages':[3,4],'evidence_files':{'source.txt':'c'*64},
            'evidence':[{'path':'source.txt','sha256':'c'*64,'description':'Synthetic only.'}],
            'joins':[{'left_block_id':'a','right_block_id':'b','separator':'',
                'discretionary_wrap_word':'addition','left_text_sha256':digest(a['text'].encode()),
                'right_text_sha256':digest(b['text'].encode()),'reason':'Source prints addi-/tion.'}]}
        return doc,review

    def test_checked_word_reassembles_without_rewriting_block_spans(self):
        doc,review=self.fixture();before=copy.deepcopy(doc['blocks'])
        apply_paragraph_reviews(doc,[review]);validate_paragraph_reviews(doc)
        text,spans=text_with_block_spans([doc['blocks'][0],doc['blocks'][2]])
        self.assertEqual(text,'It has strengths. In addition to flexibility, it is efficient.')
        for span,block in zip(spans,[before[0],before[2]]):
            self.assertEqual(text[span['start']:span['end']],block['text'])
        self.assertEqual(spans[0]['end'],spans[1]['start'])
        self.assertEqual(text_with_block_spans([doc['blocks'][2]])[0],before[2]['text'])
        doc['blocks'][2]['paragraph_join_separator']=' '
        with self.assertRaises(ValueError):
            validate_paragraph_reviews(doc)

    def test_empty_join_requires_exact_word_and_terminal_hyphen_repair(self):
        for mode in ('word','no_repair','wrong_repair','intervening','section','coverage'):
            doc,review=self.fixture()
            if mode=='word':review['joins'][0]['discretionary_wrap_word']='additional'
            if mode=='no_repair':doc['text_repair_reviews']=[]
            if mode=='wrong_repair':doc['text_repair_reviews'][0]['operations'][0]['new']='other'
            if mode=='intervening':doc['blocks'][1]['kind']='prose'
            if mode=='section':doc['blocks'][2]['section_id']='other'
            if mode=='coverage':review['checked_pages']=[3]
            with self.assertRaises(ValueError,msg=mode):
                apply_paragraph_reviews(doc,[review])

    def test_literal_summary_statement_alias_does_not_capture_ordinary_prose(self):
        self.assertEqual(title_role('Summary Statement',2),'abstract')
        self.assertEqual(title_role('Summary Statement',12),'other')
        self.assertEqual(title_role('Our summary statement follows below.',2),'other')


if __name__=='__main__':
    unittest.main()
