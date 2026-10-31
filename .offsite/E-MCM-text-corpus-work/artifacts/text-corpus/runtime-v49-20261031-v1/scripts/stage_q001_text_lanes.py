"""Freeze only the source prose boundaries actually checked on pages6,7,17.

Object text stays verbatim in the structured/full export with source line IDs.
It is excluded from default prose, without interpreting equations or diagrams.
"""
from pathlib import Path
from corpus_reader import Catalog
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest,file_hash,json_new,make_document,rows


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    root=base/'reflow-20261030-v11';catalog=Catalog(root)
    old=catalog.document('P-A-2010-6749-395f556a')
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    selected=[]
    def page(number,spec):
        raw=pages[number-1];byid={x['line_id']:x for x in raw['lines']}
        def ids(block,*indexes):
            return [x['line_id'] for x in raw['lines'] if x['native_block']==block and
                    x['text'].strip() and (not indexes or int(x['line_id'].rsplit('l',1)[1]) in indexes)]
        groups=[]
        for name,kind,parts,opening in spec(ids):
            members=[lid for part in parts for lid in part]
            group={'group_id':f'p{number:04d}-{name}','kind':kind,'source_line_ids':members,
                   'text_sha256':digest(' '.join(byid[lid]['text'].strip() for lid in members).encode()),
                   'reason':'Actually compared physical page prose boundaries and text/object location; preserve all original glyph text.'}
            if opening:
                group['opens_section']=opening
            groups.append(group)
        selected.append({'page':number,'groups':groups})
    page(6,lambda i:[
        ('header','furniture',[i(0)],None),
        ('chapter','heading',[i(1)],{'role':'model','level':2}),
        ('drawing-labels','source_object',[i(n) for n in range(7,13)],None),
        ('caption','caption',[i(2,1)],None),
        ('lead','prose',[i(2,2)],None),
        ('display-source','source_object',[i(3)],None),
        ('definitions-lead','prose',[i(4,0)],None),
        ('definition-1','prose',[i(4,2,3)],None),
        ('definition-2','prose',[i(4,5)],None),
        ('definition-3','prose',[i(5,1),i(6,0)],None),
        ('definition-4','prose',[i(6,2,3)],None),
        ('definition-5','prose',[i(6,5)],None)])
    page(7,lambda i:[
        ('header','furniture',[i(0)],None),
        ('definition-6','prose',[i(1,1),i(2,0)],None),
        ('definition-7','prose',[i(2,2,3)],None),
        ('definition-8','prose',[i(2,5)],None),
        ('lead-2','prose',[i(3)],None),
        ('display-source-2','source_object',[i(4)],None),
        ('definitions-lead','prose',[i(5,0)],None),
        ('definition-9','prose',[i(5,2,3)],None),
        ('definition-10','prose',[i(5,5)],None),
        ('definition-11','prose',[i(5,7)],None),
        ('definition-12','prose',[i(6,1),i(7,0)],None),
        ('definition-13','prose',[i(7,2,3)],None),
        ('lead-3','prose',[i(8)],None),
        ('display-source-3','source_object',[i(9)],None),
        ('definition-14','prose',[i(10)],None),
        ('output-lead','prose',[i(11)],None),
        ('display-source-4','source_object',[i(n) for n in range(12,21)],None),
        ('subchapter','heading',[i(22)],{'role':'other','level':3}),
        ('case-title','heading',[i(23)],None),
        ('case-prose-page-fragment','prose',[i(24)],None)])
    page(17,lambda i:[
        ('header','furniture',[i(0)],None),
        ('display-source-21a','source_object',[i(n) for n in range(1,5)],None),
        ('display-source-21b','source_object',[i(n) for n in range(5,10)],None),
        ('italic-description-unrecovered','mixed',[i(10)],None),
        ('mass-lead','prose',[i(11)],None),
        ('display-source-22','source_object',[i(12),i(13)],None),
        ('measurement-item','list',[i(14),i(15)],None),
        ('handoff-paragraph','prose',[i(16)],None),
        ('chapter','heading',[i(17)],{'role':'other','level':1}),
        ('subchapter','heading',[i(18)],{'role':'other','level':2}),
        ('data-prose','prose',[i(19,0,1,2)],None),
        ('caption','caption',[i(19,3)],None),
        ('table-text-location','source_object',[i(20)],None)])
    folder=base/'source-reviews/q001-span-origin-20261030-v1'
    review={'schema':'source-text-layout-review-v1',
        **{k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root;2026-10-30;three bounded JPEGs actually checked',
        'reason':'Recover checked prose item/heading boundaries and isolate object text. No formula or chart interpretation.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
        'evidence':[{'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
            'bundle_root':str(folder),'description':'Source-bound physical pages6,7,17 PNGs and bounded JPEGs; only prose boundaries reviewed.'}],
        'evidence_files':{x.name:file_hash(x) for x in folder.iterdir() if x.is_file()},
        'remaining_uncertainties':['Native mathematical-font glyph duplication in surrounding prose remains unrecovered.',
            'Page7 final paragraph continues onpage8; this review does not accept that cross-page join.',
            'Object glyph order/meaning is not reviewed; all native IDs are retained.',
            'This is a local paragraph/layout check, not source fidelity or whole-section acceptance.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[review])
    doc=make_document(old,working,improved=True);doc['layout_reviews']=applied
    validate_layout_reviews(doc,pages)
    output=base/'reviews/20261030/q001-pages6-7-17-text-lanes-v1.json'
    json_new(output,review)
    print({'checked_pages':[6,7,17],'retained_groups':sum(len(x['groups']) for x in selected),
           'output':str(output),'source_fidelity_approved':False})


if __name__=='__main__':
    main()
