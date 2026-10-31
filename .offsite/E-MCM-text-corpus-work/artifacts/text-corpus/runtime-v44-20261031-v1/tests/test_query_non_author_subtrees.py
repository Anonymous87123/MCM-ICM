import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_query_non_author_subtrees import findings


class NonAuthorSubtreeAuditTests(unittest.TestCase):
    def test_named_query_leak_is_separate_from_fulltext_and_does_not_mutate_source(self):
        document = {'sections':[
            {'section_id':'summary','title':'Summary','role':'abstract','parent_id':None},
            {'section_id':'refs','title':'References','role':'references','parent_id':'summary'}],
            'blocks':[
                {'block_id':'a','section_id':'summary','kind':'prose','text':'Author paragraph.','source_pages':[1]},
                {'block_id':'r','section_id':'refs','kind':'prose','text':'Bibliography.','source_pages':[2]}]}
        before = copy.deepcopy(document)
        def legacy_selection(doc,query):
            return (['summary'],set()) if query=='abstract' else (['summary'],{'references'})
        # Retain a detector regression fixture for the preserved old policy;
        # current production policy intentionally excludes these descendants.
        with patch('audit_query_non_author_subtrees.select_sections',side_effect=legacy_selection):
            result = findings(document,('abstract','all_author_text'))
        self.assertEqual(document,before)
        self.assertEqual([x['query'] for x in result],['abstract'])
        self.assertEqual(result[0]['leaked_blocks'][0]['block_id'],'r')
        self.assertEqual(result[0]['leaked_blocks'][0]['excluded_role'],'references')


if __name__ == '__main__':
    unittest.main()
