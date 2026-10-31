"""Separate q14's source-checked handout from its summary, preserving all lanes."""
from pathlib import Path

from corpus_queries import select_sections
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest, file_hash, json_new, make_document, rows, section_blocks


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    root=base/'reflow-20261030-v16'
    output=base/'reviews/20261030/q014-summary-handout-layout-v1.json'
    report=base/'reviews/20261030/q014-summary-handout-preflight-v1.json'
    if output.exists() or report.exists():
        raise ValueError('Create-only proof/report exists; preserve it')
    catalog=Catalog(root)
    doc=catalog.document('P-A-2013-20559-c8c96095')
    pages=rows(root/'papers'/doc['paper_id']/'raw/pages.jsonl')
    active=[x for x in pages[1]['lines'] if x['text'].strip() and not x.get('superseded_by_ocr')]
    definitions=[
        ('p2-handout-title','heading',lambda x:x['line_id']=='p0002-n0016-l0000',
         {'role':'other','level':1}),
        ('p2-tagline','author_callout',lambda x:x['line_id']=='p0002-n0016-l0001' or x['native_block']==17,None),
        ('p2-intro-paragraph','prose',lambda x:1<=x['native_block']<=12,None),
        ('p2-input-design-paragraph','prose',lambda x:13<=x['native_block']<=15 or 20<=x['native_block']<=34,None),
        ('p2-footer-slogan','author_callout',lambda x:38<=x['native_block']<=41,None),
        ('p2-fictional-contact','front_matter',lambda x:x['native_block']==44,None)]
    groups=[]
    for name,kind,predicate,opening in definitions:
        members=[x for x in active if predicate(x)]
        groups.append({'group_id':name,'kind':kind,
            'source_line_ids':[x['line_id'] for x in members],
            'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
            'reason':'Actually checked source lanes; main prose precedes its separate footer callout.',
            **({'opens_section':opening} if opening else {})})
    folder=base/'source-reviews/q014-opening-20261030-v1'
    findings=base/'reviews/20261030/q014-summary-handout-findings-v1.json'
    review={'schema':'source-text-layout-review-v1',
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root; 2026-10-30; actual source physical pages1/2',
        'reason':'Close the summary before the separate promotional handout; restore its left-to-right paragraph continuation without deleting author prose.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
        'pages':[{'page':2,'groups':groups}],
        'evidence':[{'path':str(folder/'manifest.json'),'bundle_root':str(folder),
            'sha256':file_hash(folder/'manifest.json'),'description':'Both bounded opening source pages actually checked.'},
            {'path':str(findings),'sha256':file_hash(findings),'description':'Checked summary end, separate handout and prose lane continuation; remaining limits.'}],
        'evidence_files':{str(p):file_hash(p) for p in folder.iterdir() if p.is_file()},
        'application_status':'Staged for a later repair batch; not included in running v17 build.',
        'remaining_uncertainties':['Page1 literal spacing/hyphens and whole-paper source fidelity remain pending.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(doc,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(doc,working,[review])
    candidate=make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    candidate['layout_reviews']=applied
    validate_layout_reviews(candidate,pages)
    ids,excluded=select_sections(candidate,'abstract')
    abstract=section_blocks(candidate,ids,excluded_roles=excluded)
    if {p for b in abstract for p in b['source_pages']}!={1}:
        raise ValueError('Handout still contaminates abstract')
    para=next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p2-input-design-paragraph')
    if 'prefer even heating over' not in para['text'] or 'our goal.' in para['text']:
        raise ValueError('Main-column continuation still mixed with footer')
    json_new(output,review)
    _,copies=prepare_review_bundles([output],identity_fields=('paper_id',),application_status='preflight only')
    json_new(report,{'parent_dataset_id':catalog.identity,'paper_id':doc['paper_id'],
        'layout_groups':len(groups),'abstract_pages':[1],
        'abstract_characters':len('\n\n'.join(b['text'] for b in abstract)),
        'cross_column_continuation_pass':True,'source_line_accounting_pass':True,
        'portable_evidence_files':len(copies),'source_fidelity_approved':False,
        'ai_reading_receipts_created':0,'included_in_v17':False})
    print(report.read_text(encoding='utf-8'))


if __name__=='__main__':
    main()
