import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from corpus_queries import all_author_blocks
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from text_corpus import digest, make_document


class ReviewedMixedContentsPageTests(unittest.TestCase):
    def pages(self):
        def line(text,page,number,y,bold=False):
            return {'line_id':f'p{page}-l{number}','text':text,'page':page,'native_block':number,
                'font_size':11,'bold':bold,'bbox':[60,y,500,y+12]}
        return [{'page':1,'width':600,'height':800,'comparison':{'status':'agreement'},'lines':[
            line('Abstract',1,0,80,True),line('An author paragraph spans the length and',1,1,120)]},
            {'page':2,'width':600,'height':800,'comparison':{'status':'agreement'},'lines':[
                line('width of the source page; this is author continuation.',2,0,100),
                line('A complete next author paragraph ends here.',2,1,130),
                line('Contents',2,2,300,True),line('Introduction ........ 3',2,3,340),
                line('Model ........ 4',2,4,370),line('Results ........ 8',2,5,400)]}]

    def test_checked_midpage_contents_heading_preserves_author_text_above_it(self):
        pages=self.pages();meta={'paper_id':'synthetic','source_sha256':'f'*64,'raw_pages_sha256':'e'*64}
        def group(name,kind,ids,opening=None):
            text=' '.join(x['text'] for x in pages[1]['lines'] if x['line_id'] in ids)
            return {'group_id':name,'kind':kind,'source_line_ids':ids,'text_sha256':digest(text.encode()),
                'reason':'Synthetic checked mixed-page fixture.',**({'opens_section':opening} if opening else {})}
        review={**meta,'schema':'source-text-layout-review-v1','reviewer':'synthetic fixture',
            'reason':'Source-checked author continuation before the printed Contents heading.',
            'evidence_files':{'synthetic-evidence':'f'*64},'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
            'pages':[{'page':2,'groups':[
                group('continuation','prose',['p2-l0']),group('next-paragraph','prose',['p2-l1']),
                group('contents-heading','heading',['p2-l2'],{'role':'contents','level':1}),
                group('contents-entries','source_object',['p2-l3','p2-l4','p2-l5'])]}]}
        applied=apply_layout_reviews(meta,pages,[review])
        document=make_document(meta,pages,improved=True);document['layout_reviews']=applied
        validate_layout_reviews(document,self.pages())
        author='\n\n'.join(b['text'] for b in all_author_blocks(document))
        self.assertIn('width of the source page',author)
        self.assertIn('next author paragraph',author)
        self.assertNotIn('Introduction ........',author)
        self.assertEqual([d['page'] for d in document['defects'] if d['code']=='contents_page_boundary_review'],[2])

    def test_unreviewed_contents_detection_remains_an_unaccepted_candidate(self):
        document=make_document({'paper_id':'synthetic'},copy.deepcopy(self.pages()),improved=True)
        self.assertEqual([d['page'] for d in document['defects'] if d['code']=='contents_page_boundary_review'],[2])
        self.assertTrue(all(s['boundary_status']=='pending' for s in document['sections']))


if __name__=='__main__':
    unittest.main()
