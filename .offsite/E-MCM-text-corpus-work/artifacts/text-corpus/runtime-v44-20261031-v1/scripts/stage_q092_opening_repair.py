"""Separate one individually checked cover from its three-paragraph summary."""
from collections import Counter
from pathlib import Path
from corpus_reader import Catalog
from corpus_queries import select_sections,selected_blocks
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest,file_hash,json_new,make_document,rows,text_with_block_spans


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    root=base/'reflow-20261031-v23';out=base/'reviews/20261031'
    target=out/'q092-opening-layout-v1.json';report=out/'q092-opening-preflight-v1.json'
    if target.exists() or report.exists():
        raise ValueError('Create-only q92 proof exists; preserve it')
    catalog=Catalog(root);old=catalog.document('P-B-2011-12114-03fd7440')
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    folder=out/'q092-opening-pages-v1';findings=out/'q092-opening-findings-v1.json'
    evidence=[{'path':str(findings),'sha256':file_hash(findings),'description':'Actually checked source-page prose and boundary findings.'},
        {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
         'bundle_root':str(folder),'description':'Three individually inspected bounded JPEG/native physical pages.'}]
    files={str(p):file_hash(p) for p in folder.iterdir() if p.is_file()};files[str(findings)]=file_hash(findings)
    def group(page,name,kind,natives,opening=None):
        members=[x for x in pages[page-1]['lines'] if x['text'].strip() and x['native_block'] in natives]
        return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
            'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
            'reason':'Individual physical-page printed text ownership and paragraph boundary check.',
            **({'opens_section':opening} if opening else {})}
    meta={k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
    review={'schema':'source-text-layout-review-v1',**meta,'reviewer':'Codex root;2026-10-31; physical pages1–3',
        'reason':'Separate cover and page headers from the complete three-paragraph Summary Statement.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
        'pages':[{'page':1,'groups':[group(1,'p1-title','title',[0]),
            group(1,'p1-control-date','front_matter',[1,2]),group(1,'p1-page','furniture',[3])]},
            {'page':2,'groups':[group(2,'p2-header','furniture',[0]),
                group(2,'p2-summary-title','heading',[1],{'role':'abstract','level':1}),
                *[group(2,f'p2-paragraph-{n-1}','prose',[n]) for n in (2,3,4)]]}],
        'evidence':evidence,'evidence_files':files,'source_fidelity_approved':False,
        'remaining_uncertainties':['Later source pages and full-paper chapter mapping unreviewed.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[review]);candidate=make_document(meta,working,improved=True)
    candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
    source=Counter(x['line_id'] for p in pages for x in p['lines'])
    used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source!=used or any(n!=1 for n in used.values()):
        raise ValueError('Source line lost or duplicated')
    ids,excluded=select_sections(candidate,'abstract')
    blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
    text,spans=text_with_block_spans(blocks)
    if ({p for s in spans for p in s['pages']}!={2} or sum(b['kind']!='heading' for b in blocks)!=3 or
            'Control #' in text or 'February' in text or not text.endswith('a radius of 40 miles.')):
        raise ValueError('Checked summary text scope differs')
    json_new(target,review)
    prepare_review_bundles([target],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'paper_id':old['paper_id'],'characters':len(text),
        'sha256':digest(text.encode()),'author_paragraphs':3,'literal_repairs':0,
        'source_lines_accounted_once':True,'source_fidelity_approved':False,'ai_receipts_created':0}
    json_new(report,result);print(text,flush=True);print(result,flush=True)


if __name__=='__main__':
    main()
