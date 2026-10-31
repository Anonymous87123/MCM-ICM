import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rebind_literal_review import rebind
from source_text_repairs import apply_text_repairs
from text_corpus import digest


class LiteralReviewRebindingTests(unittest.TestCase):
    def fixture(self):
        candidate={'paper_id':'p','source_sha256':'a'*64,'raw_pages_sha256':'b'*64,'defects':[],
            'blocks':[{'block_id':'new','kind':'prose','text':'We use XYZ and preserve the entire paragraph.',
                'source_pages':[5],'source_line_ids':['line1','line2'],'issues':[]}]}
        previous=copy.deepcopy(candidate);previous['blocks'][0]['block_id']='old'
        text=candidate['blocks'][0]['text']
        review={k:candidate[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
        review.update(checked_pages=[5],reviewer='synthetic-only',reason='Synthetic literal proof.',
            evidence=[{'path':'proof','sha256':'c'*64,'description':'Synthetic source.'}],
            operations=[{'block_id':'old','operation':'literal_replace','old':'XYZ','new':'BBS','count':1,
                'reason':'Synthetic transcription.', 'before_text_sha256':digest(text.encode()),
                'after_text_sha256':digest(text.replace('XYZ','BBS').encode())}])
        apply_text_repairs(previous,[review])
        return previous,candidate,review

    def test_only_block_identity_changes_and_source_approval_does_not_expand(self):
        previous,candidate,review=self.fixture();untouched=copy.deepcopy(candidate)
        new=rebind(previous,candidate,review)
        self.assertEqual(candidate,untouched)
        self.assertEqual(new['operations'][0]['block_id'],'new')
        self.assertEqual(new['evidence'],review['evidence'])
        self.assertFalse(new['binding_transfer']['new_source_review'])
        apply_text_repairs(candidate,[new])
        self.assertEqual(candidate['blocks'][0]['text'],previous['blocks'][0]['text'])

    def test_changed_words_line_order_kind_location_source_and_ambiguity_rejected(self):
        for mutation in ('words','order','kind','pages','source','ambiguous'):
            previous,candidate,review=self.fixture();b=candidate['blocks'][0]
            if mutation=='words':b['text']+=' Another sentence.'
            if mutation=='order':b['source_line_ids'].reverse()
            if mutation=='kind':b['kind']='mixed'
            if mutation=='pages':b['source_pages']=[6]
            if mutation=='source':candidate['source_sha256']='d'*64
            if mutation=='ambiguous':candidate['blocks'].append(copy.deepcopy(b))
            with self.assertRaises(ValueError):
                rebind(previous,candidate,review)


if __name__=='__main__':
    unittest.main()
