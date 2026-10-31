import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from preview_span_origin_flow import lost_contents_pages


class ProspectiveContentsRegressionTests(unittest.TestCase):
    def doc(self,pages):
        return {'defects':[{'code':'contents_page_boundary_review','page':p} for p in pages]}

    def test_a_shift_to_more_candidates_cannot_hide_loss_of_an_old_page(self):
        self.assertEqual(lost_contents_pages(self.doc([2,3]),self.doc([2,4,5])),[3])

    def test_retaining_old_candidates_does_not_make_a_source_approval(self):
        old=self.doc([2]);new=self.doc([2,3])
        self.assertEqual(lost_contents_pages(old,new),[])
        self.assertNotIn('source_completeness_accepted',new)
        self.assertNotIn('boundary_status',new)


if __name__=='__main__':unittest.main()
