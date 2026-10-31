"""Metric sidecars require exact native identity; OCR is not a native span."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from extract_text_span_metrics import match_page


class TextSpanMetricsTests(unittest.TestCase):
    def fixture(self):
        span={'text':'Original prose','bbox':[10,20,100,35],'font':'Times','size':12,'flags':0}
        raw={'page':1,'lines':[{'line_id':'p0001-n0000-l0000','native_block':0,
             'text':span['text'],'bbox':span['bbox'],'spans':[span]},
             {'line_id':'p0001-ocr-l0000','native_block':-1,'text':'OCR candidate'}]}
        fresh={'blocks':[{'type':0,'lines':[{'bbox':span['bbox'],'dir':[1,0],'wmode':0,
             'spans':[{**span,'origin':[10,32],'ascender':1.0,'descender':-.25}]}]}]}
        return raw,fresh

    def test_preserves_native_identity_and_does_not_change_ocr_or_raw(self):
        raw,fresh=self.fixture();original=copy.deepcopy(raw)
        result=match_page(raw,fresh)
        self.assertEqual(len(result['lines']),1)
        self.assertEqual(result['lines'][0]['spans'][0]['origin'],[10,32])
        self.assertEqual(raw,original)

    def test_reordered_native_blocks_changed_glyphs_fonts_or_coordinates_rejected(self):
        for key,value in [('text','Different prose'),('font','Another font'),('bbox',[11,20,100,35])]:
            raw,fresh=self.fixture();fresh['blocks'][0]['lines'][0]['spans'][0][key]=value
            with self.assertRaises(ValueError):
                match_page(raw,fresh)
        raw,fresh=self.fixture();fresh['blocks'].insert(0,{'type':1})
        with self.assertRaises(ValueError):
            match_page(raw,fresh)
        raw,fresh=self.fixture();fresh['blocks']=[]
        with self.assertRaises(ValueError):
            match_page(raw,fresh)


if __name__=='__main__':
    unittest.main()
