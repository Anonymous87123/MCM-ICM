from pathlib import Path
import json
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from corpus_queries import select_sections, selected_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from text_corpus import (digest, encoded, exported_section_text, export_document,
                         file_hash, json_new, section_text)


class AuthorQueryScopeTests(unittest.TestCase):
    def document(self,title='Summary',role='abstract'):
        return {'sections':[
            {'section_id':'root','title':title,'role':role,'parent_id':None},
            {'section_id':'child','title':'Author continuation','role':'other','parent_id':'root'},
            {'section_id':'refs','title':'References','role':'references','parent_id':'root'},
            {'section_id':'ref-child','title':'Nested material','role':'other','parent_id':'refs'},
            {'section_id':'toc','title':'Contents','role':'contents','parent_id':'root'},
            {'section_id':'ai','title':'AI Use Report','role':'ai_disclosure','parent_id':'root'}],
            'blocks':[{'block_id':sid,'section_id':sid,'kind':'prose','source_pages':[1],
                       'text':'References and AI are mentioned in author prose.' if sid=='root' else 'Literal '+sid}
                      for sid in ('root','child','refs','ref-child','toc','ai')]}

    def blocks(self,doc,query,exact=False):
        ids,excluded = select_sections(doc,query,exact_title=exact)
        return [b['block_id'] for b in selected_blocks(doc,{'section_ids':ids,'excluded_roles':sorted(excluded)})]

    def test_every_named_author_query_excludes_non_author_descendants_but_keeps_author_prose(self):
        cases = [('abstract','Summary','abstract'),('introduction','Introduction','introduction'),
            ('problem_restatement','Restatement','problem_restatement'),('problem_analysis','Analysis','problem_analysis'),
            ('assumptions','Assumptions','assumptions'),('notation','Notation','notation'),
            ('model_building_and_solution','Model construction','model'),
            ('sensitivity_validation','Sensitivity Analysis','sensitivity'),
            ('improvements_evaluation','Model Evaluation','discussion'),('appendix','Appendix A','appendix')]
        cases += [(f'task_{n}',f'Solution to Problem {n}','model') for n in range(1,5)]
        for query,title,role in cases:
            with self.subTest(query=query):
                self.assertEqual(self.blocks(self.document(title,role),query),['root','child'])

    def test_exact_author_title_keeps_nested_author_text_not_bibliography(self):
        self.assertEqual(self.blocks(self.document('Custom Method','other'),'Custom Method',exact=True),['root','child'])

    def test_explicit_non_author_request_still_returns_its_separate_preserved_text(self):
        doc = self.document()
        self.assertEqual(self.blocks(doc,'references'),['refs','ref-child'])
        self.assertEqual(self.blocks(doc,'References',exact=True),['refs','ref-child'])
        self.assertEqual(self.blocks(doc,'ai_disclosure'),['ai'])

    def test_real_non_author_kinds_are_addressable_without_leaking_into_author_text(self):
        doc = self.document()
        kinds = {'refs':'references', 'ref-child':'source_object', 'toc':'contents', 'ai':'ai_disclosure'}
        for block in doc['blocks']:
            block['kind'] = kinds.get(block['block_id'], block['kind'])
        self.assertEqual(self.blocks(doc,'references'),['refs','ref-child'])
        self.assertEqual(self.blocks(doc,'References',exact=True),['refs','ref-child'])
        self.assertEqual(self.blocks(doc,'contents'),['toc'])
        self.assertEqual(self.blocks(doc,'ai_disclosure'),['ai'])
        self.assertEqual(self.blocks(doc,'abstract'),['root','child'])

    def test_explicit_non_author_objects_keep_captions_but_exclude_page_furniture(self):
        doc = self.document()
        doc['blocks'] += [
            {'block_id':kind,'section_id':'refs','kind':kind,'text':kind,'source_pages':[1]}
            for kind in ('caption','running_header','running_footer','front_matter')]
        self.assertEqual(self.blocks(doc,'references'),['refs','ref-child','caption'])

    def test_chapter_exports_sqlite_and_reader_share_the_same_complete_view(self):
        doc = self.document()
        doc.update(paper_id='synthetic',source_sha256='f'*64,raw_pages_sha256='e'*64,page_count=1,defects=[])
        for section in doc['sections']:
            section['boundary_status'] = 'pending'
        for block in doc['blocks']:
            block['kind'] = {'refs':'references','ref-child':'source_object',
                'toc':'contents','ai':'ai_disclosure'}.get(block['block_id'],block['kind'])
        canonical = section_text(doc,['root'])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); folder = root/'papers/synthetic'
            export_document(folder,doc)
            saved = json.loads((folder/'document.json').read_text(encoding='utf-8'))
            self.assertEqual(section_text(saved,['root']),canonical)
            self.assertEqual(exported_section_text(doc,'root'),canonical)  # old policy remains readable
            self.assertIn('Literal refs',(folder/'full.md').read_text(encoding='utf-8'))
            json_new(root/'scope.json',{'scope_id':'synthetic','paper_count':1,'physical_page_count':1,
                'records':[{'paper_id':'synthetic','queue_position':1,'problem_type':'A','year':2020,
                            'page_count':1,'sha256':'f'*64}]})
            json_new(folder/'COMPLETE.json',{'scope_id':'synthetic',
                'files':{p.relative_to(folder).as_posix():file_hash(p) for p in folder.rglob('*') if p.is_file()}})
            index(root); catalog = Catalog(root)
            con = sqlite3.connect(root/'corpus.sqlite3')
            try:
                for sid,query in (('root','abstract'),('refs','references'),('toc','contents'),('ai','ai_disclosure')):
                    with self.subTest(query=query):
                        text,spans = catalog.text_and_spans(catalog.select(query)[0])
                        self.assertEqual(exported_section_text(saved,sid),text)
                        self.assertEqual(con.execute('SELECT text FROM sections WHERE section_id=?',(sid,)).fetchone()[0],text)
                        self.assertEqual(con.execute('SELECT text FROM section_search WHERE section_id=?',(sid,)).fetchone()[0],text)
                        self.assertTrue((folder/f'sections/{sid}.md').read_text(encoding='utf-8').endswith('\n'+text+'\n'))
                author = exported_section_text(saved,'root')
                self.assertIn('References and AI are mentioned in author prose.',author)
                self.assertNotIn('Literal refs',author)
                self.assertIn('Literal ref-child',exported_section_text(saved,'refs'))
            finally:
                con.close()

    def test_single_section_export_uses_ids_even_when_titles_repeat(self):
        doc = self.document()
        doc['sections'][1]['title'] = 'Summary'
        doc['sections'][1]['parent_id'] = None
        doc['chapter_view_policy'] = 'query-selected-v1'
        self.assertNotIn('Literal child',exported_section_text(doc,'root'))
        self.assertEqual(exported_section_text(doc,'child'),'Literal child')


if __name__ == '__main__':
    unittest.main()
