from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from corpus_reader import acknowledge, author_text_coverage, build_batch, next_batch, start, state
from text_corpus import json_new
from test_text_corpus import fixture


class ReaderQueryPolicyTests(unittest.TestCase):
    def test_new_session_binds_query_policy_and_refuses_changed_policy_on_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog = fixture(root,count=1)
            run = root/'run'
            start(catalog,'abstract',run)
            session,cursor,_,_ = state(catalog,run)
            self.assertEqual(len(session['query_policy_sha256']),64)
            with patch('corpus_reader.query_policy_hash',return_value='0'*64):
                with self.assertRaisesRegex(ValueError,'Query policy changed'):
                    next_batch(catalog,run)
                with self.assertRaisesRegex(ValueError,'Query policy changed'):
                    build_batch(catalog,session,cursor,0)
            self.assertFalse((run/'batches').exists())
            self.assertFalse((run/'receipts').exists())

    def test_old_corpus_new_policy_only_allows_explicit_unverified_preview(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog = fixture(root,count=1)
            json_new(root/'scope.json',{'input_sha256':{'queries':'0'*64}})
            with self.assertRaisesRegex(ValueError,'new immutable generation'):
                start(catalog,'abstract',root/'strict')
            self.assertFalse((root/'strict').exists())
            start(catalog,'abstract',root/'preview',allow_unverified=True)
            session,_,_,_ = state(catalog,root/'preview')
            self.assertEqual(session['query_policy_status'],'unfrozen-policy-preview')

    def test_unfrozen_policy_preview_never_claims_final_read_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog = fixture(root,count=1)
            json_new(root/'scope.json',{'input_sha256':{'queries':'0'*64}})
            run = root/'preview'
            start(catalog,'abstract',run,allow_unverified=True)
            batch = next_batch(catalog,run)
            observations = [{'paper_id':chunk['paper_id'],
                'block_ids':[block['block_id'] for block in chunk['source_blocks']],
                'observation':'Synthetic fixture only, no real paper read.'} for chunk in batch['chunks']]
            result = acknowledge(catalog,run,batch['completion_marker'],observations)
            self.assertTrue(result['traversal_complete'])
            self.assertEqual(result['unresolved'],0)
            self.assertFalse(result['full_read_acceptance'])

    def test_unfrozen_policy_preview_cannot_grant_all_chapter_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            catalog = fixture(root,count=1)
            json_new(root/'scope.json',{'input_sha256':{'queries':'0'*64}})
            run = root/'preview'
            start(catalog,'all_author_text',run,allow_unverified=True)
            batch = next_batch(catalog,run)
            observations = [{'paper_id':chunk['paper_id'],
                'block_ids':[block['block_id'] for block in chunk['source_blocks']],
                'observation':'Synthetic fixture only; no actual-paper reading.'} for chunk in batch['chunks']]
            acknowledge(catalog,run,batch['completion_marker'],observations)
            result = author_text_coverage(catalog,[run])
            self.assertEqual(result['all_author_text_processed_papers'],1)
            self.assertFalse(result['all_chapters_read_acceptance'])


if __name__ == '__main__':
    unittest.main()
