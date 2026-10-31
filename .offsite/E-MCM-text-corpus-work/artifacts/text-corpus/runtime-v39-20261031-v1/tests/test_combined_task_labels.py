"""Real corpus combined task labels must expose the shared chapter to each task."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from corpus_queries import task_numbers,select_sections,selected_blocks


class CombinedTaskLabelTests(unittest.TestCase):
    def test_real_combined_titles_and_explicit_ranges(self):
        examples=[('3 TASK 1 & 2: Guiding Cycling Races Based on Power Curves',{1,2}),
                  ('4 TASK 3 & 4: Sensitivity to Weather and Power Distribution’s',{3,4}),
                  ('3 TASK1&2: Point-tracking Evaluation PCA-TOPSIS Model',{1,2}),
                  ('Model II:Wear Distribution Modelsolving Problem 2 and 3',{2,3}),
                  ('Task 1 & 4: Lampreys and Other Species',{1,4}),
                  ('Questions II, III and IV: Comparison',{2,3,4}),
                  ('Tasks 1, 2, and 4: Shared solution',{1,2,4}),
                  ('Tasks 1–4: Combined solution',{1,2,3,4}),
                  ('Tasks 1 through 5: Combined solution',{1,2,3,4}),
                  ('Problems one to three: A shared model',{1,2,3})]
        for title,expected in examples:
            with self.subTest(title=title):
                self.assertEqual(task_numbers(title),expected)

    def test_chapter_and_year_numbers_do_not_create_task_matches(self):
        for title in ('3.2 Model with 1 to 4 input variables','Problem 12: Other task',
                      '2024 Final results','4 Sensitivity analysis','问题12：其他任务'):
            with self.subTest(title=title):
                self.assertEqual(task_numbers(title),set())
        self.assertEqual(task_numbers('Task 1: Model fitted to 2 species for 4 years'),{1})
        self.assertEqual(task_numbers('Task 1 & 4: Three cases'),{1,4})

    def test_second_task_returns_complete_shared_parent_and_child_once(self):
        doc={'sections':[{'section_id':'s1','title':'3 TASK 1 & 2: Combined Model','role':'model','parent_id':None},
                         {'section_id':'s2','title':'3.1 Calibration','role':'model','parent_id':'s1'},
                         {'section_id':'s3','title':'4 Task 3','role':'model','parent_id':None}],
             'blocks':[{'block_id':'b1','section_id':'s1','kind':'prose','text':'The shared chapter opening.'},
                       {'block_id':'b2','section_id':'s2','kind':'prose','text':'The complete shared calibration.'},
                       {'block_id':'b3','section_id':'s3','kind':'prose','text':'An unrelated third task.'}]}
        for query in ('task_1','task_2'):
            ids,excluded=select_sections(doc,query)
            blocks=selected_blocks(doc,{'section_ids':ids,'excluded_roles':sorted(excluded)})
            self.assertEqual([b['block_id'] for b in blocks],['b1','b2'])


if __name__=='__main__':
    unittest.main()
