from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from snapshot_reading_source_issues import checked_corrections
from text_corpus import file_hash,json_new


class ObservationCorrectionTests(unittest.TestCase):
    def test_correction_binds_the_original_batch_receipt_and_issue_without_changing_either(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            receipt=root/'receipts/000000.json'
            batch=root/'batches/000000.json'
            json_new(receipt,{'observations':[{'paper_id':'p','source_issues':[{'code':'old'}]}]})
            json_new(batch,{'original':'source bytes'})
            session={'run_id':'run','dataset_id':'data'}
            value={'schema':'reading-observation-correction-v1',**session,'receipt_sequence':0,
                   'receipt_sha256':file_hash(receipt),'batch_sha256':file_hash(batch),
                   'paper_id':'p','original_issue_code':'old','correction':'Correct the label only.',
                   'reviewer':'Synthetic regression'}
            correction=root/'correction.json'
            json_new(correction,value)
            result=checked_corrections(root,session,[correction])
            self.assertEqual(result[0]['correction'],value)
            self.assertEqual(file_hash(receipt),value['receipt_sha256'])
            self.assertEqual(file_hash(batch),value['batch_sha256'])
            with self.assertRaises(ValueError):
                checked_corrections(root,{'run_id':'other','dataset_id':'data'},[correction])
            invalid=root/'invalid.json'
            json_new(invalid,{**value,'original_issue_code':'unobserved'})
            with self.assertRaises(ValueError):
                checked_corrections(root,session,[invalid])
            receipt.write_bytes(b'changed source record')
            with self.assertRaises(ValueError):
                checked_corrections(root,session,[correction])


if __name__=='__main__':
    unittest.main()
