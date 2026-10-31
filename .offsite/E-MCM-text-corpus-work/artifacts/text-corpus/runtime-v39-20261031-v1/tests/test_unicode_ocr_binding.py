from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from bind_unicode_ocr_frontier import verify_manifest
from text_corpus import file_hash,json_new


class UnicodeOcrBindingTests(unittest.TestCase):
    def fixture(self,root):
        page = root/'page.json'
        json_new(page,{'page':2,'review_status':'pending','lines':[{'text':'Unverified literal',
            'score':.91,'pdf_box':[[1,2],[3,2],[3,4],[1,4]]}]})
        manifest = root/'manifest.json'
        paper = {'paper_id':'synthetic','source_sha256':'a'*64}
        json_new(manifest,{**paper,'pages':[{'page':2,'path':'page.json','sha256':file_hash(page),
            'line_count':1,'low_confidence_lines':1}]})
        return manifest,paper

    def test_complete_page_binding_preserves_unverified_ocr(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest,paper = self.fixture(Path(tmp))
            before = {p:file_hash(p) for p in Path(tmp).iterdir()}
            _,counts = verify_manifest(manifest,paper,[2])
            self.assertEqual(counts,{'pages':1,'ocr_lines':1,'low_confidence_lines':1})
            self.assertEqual(before,{p:file_hash(p) for p in Path(tmp).iterdir()})

    def test_missing_page_stale_source_and_changed_evidence_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest,paper = self.fixture(root)
            with self.assertRaises(ValueError):
                verify_manifest(manifest,paper,[2,3])
            with self.assertRaises(ValueError):
                verify_manifest(manifest,dict(paper,source_sha256='b'*64),[2])
            (root/'page.json').write_bytes(b'changed synthetic evidence')
            with self.assertRaises(ValueError):
                verify_manifest(manifest,paper,[2])


if __name__ == '__main__':
    unittest.main()
