"""Stage checked source prose misclassified as captions; no diagram learning."""
from pathlib import Path
from corpus_reader import Catalog
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest,file_hash,json_new,make_document,rows,title_role


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    root=base/'reflow-20261030-v11';catalog=Catalog(root);old=catalog.document('P-A-2010-6749-395f556a')
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl');selected=[]
    def add(number,spec):
        page=pages[number-1];byid={x['line_id']:x for x in page['lines']}
        def ids(block,*indexes):
            return [x['line_id'] for x in page['lines'] if x['native_block']==block and x['text'].strip() and
                    (not indexes or int(x['line_id'].rsplit('l',1)[1]) in indexes)]
        groups=[]
        for name,kind,parts,level in spec(ids):
            members=[lid for part in parts for lid in part];text=' '.join(byid[lid]['text'].strip() for lid in members)
            group={'group_id':f'p{number:04d}-{name}','kind':kind,'source_line_ids':members,
                   'text_sha256':digest(text.encode()),'reason':'Actually checked prose item boundaries; Figure-number sentences here belong to author paragraphs, not captions.'}
            if level:
                group['opens_section']={'role':title_role(text,number),'level':level}
            groups.append(group)
        selected.append({'page':number,'groups':groups})
    add(25,lambda i:[
        ('header','furniture',[i(0)],None),
        ('chart-label-location','source_object',[i(n) for n in range(9,19)],None),
        ('caption-all-fragments','caption',[i(2),i(3),i(4),i(5)],None),
        ('mass-item-title','heading',[i(6)],None),
        ('mass-qualitative-to-quantitative','prose',[i(7)],None),
        ('experimental-comparison','prose',[i(8)],None)])
    add(31,lambda i:[
        ('header','furniture',[i(0)],None),
        ('previous-page-fragment','prose',[i(1)],None),
        ('conditional-conclusion','prose',[i(2,0,1,2,3)],None),
        ('local-why-title','heading',[i(2,5,6)],None),
        ('corking-tradeoff','prose',[i(2,7,8,9,10,11)],None),
        ('equality-rationale','prose',[i(3)],None),
        ('problem3-title','heading',[i(4)],2),
        ('problem3-question-and-handoff','prose',[i(5)],None),
        ('illustration-title','heading',[i(6)],3),
        ('illustration-prose','prose',[i(7)],None)])
    folder=base/'source-reviews/q001-body-boundaries-20261030-v2'
    review={'schema':'source-text-layout-review-v1',
        **{k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root;2026-10-30;page25 andpage31 bounded JPEGs actually read',
        'reason':'Restore author sentences beginning Figure17/Figure4/Figure23 that the caption regex omitted from prose. Preserve source chapter numbers/grammar.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
        'evidence':[{'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
            'bundle_root':str(folder),'description':'Two frozen source pages and bounded proxies, prose-only review.'}],
        'evidence_files':{p.name:file_hash(p) for p in folder.iterdir() if p.is_file()},
        'remaining_uncertainties':['Unrecovered inline glyphs are retained; equations and charts are not interpreted.',
            'Page31 initial fragment requires page30 cross-page check; no join is certified.',
            'The author prints 5.3 twice for ProblemsII/III. Keep the printed numbering; do not silently renumber.',
            'Local prose grouping only; no whole-section or whole-paper source acceptance.'],
        'application_status':'Staged after v12 prospective freeze; apply in a later batch, not to immutable prior generations.',
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[review]);meta={k:old[k] for k in (
        'paper_id','problem_type','year','queue_position','page_count','source_relative_path','source_sha256','raw_pages_sha256')}
    document=make_document(meta,working,improved=True);document['layout_reviews']=applied
    validate_layout_reviews(document,pages)
    for number,needle in ((25,'Figure 17 also tells us'),(25,'Figure 4 which is drawn'),(31,'Figure 23 is an illustration')):
        if not any(b['kind']=='prose' and b['source_pages']==[number] and needle in b['text'] for b in document['blocks']):
            raise ValueError('Checked missing author sentence not restored')
    output=base/'reviews/20261030/q001-pages25-31-text-lanes-v1.json';json_new(output,review)
    print({'checked_pages':[25,31],'groups':sum(len(p['groups']) for p in selected),
           'source_fidelity_approved':False,'output':str(output)})


if __name__=='__main__':
    main()
