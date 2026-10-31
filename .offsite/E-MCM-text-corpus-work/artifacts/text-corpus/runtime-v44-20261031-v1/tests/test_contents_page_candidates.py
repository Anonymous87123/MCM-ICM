import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from contents_page_candidates import explicit_leader_contents


class ContentsPageCandidateTests(unittest.TestCase):
    def lines(self,texts):
        return [{'line_id':str(i),'text':t} for i,t in enumerate(texts)]

    def test_hyphen_and_dotted_leaders_identify_the_same_explicit_toc(self):
        for leader in ('-------------','................','. . . . . . .'):
            lines=self.lines(['CONTENTS',f'1. Introduction{leader}3',
                              f'2. Assumptions{leader}4',f'3. Model{leader}6','3.1 Method'])
            result=explicit_leader_contents(lines)
            self.assertEqual(result['label_line_ids'],['0'])
            self.assertEqual(result['leader_line_ids'],['1','2','3'])
            self.assertEqual(len(lines),5)

    def test_mentions_sparse_leaders_and_ocr_superseded_labels_do_not_promote(self):
        base=['The contents of this report follow.','1 Introduction-----------3',
              '2 Model-----------4','3 Results-----------6']
        self.assertIsNone(explicit_leader_contents(self.lines(base)))
        self.assertIsNone(explicit_leader_contents(self.lines(['CONTENTS']+base[1:3])))
        lines=self.lines(['CONTENTS']+base[1:]);lines[0]['superseded_by_ocr']=True
        self.assertIsNone(explicit_leader_contents(lines))


if __name__=='__main__':
    unittest.main()
