"""Individual checked prose/paragraph repairs; no formula interpretation."""
import copy
from pathlib import Path

from corpus_queries import select_sections, selected_blocks
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, rows


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    root=base/'reflow-20261030-v17'
    out=base/'reviews/20261031'
    findings=out/'q029-q030-q031-opening-findings-v1.json'
    paths=[out/name for name in ('q029-summary-word-repair-v1.json',
        'q030-summary-prose-layout-v1.json','q031-summary-abstract-layout-v1.json',
        'q029-q030-q031-opening-preflight-v1.json')]
    if any(p.exists() for p in paths):
        raise ValueError('Create-only staged proof exists')
    catalog=Catalog(root)

    def proofs(queue):
        folder=base/f'source-reviews/q{queue:03d}-opening-20261031-v1'
        return folder,[{'path':str(findings),'sha256':file_hash(findings),
            'description':'Actual bounded physical-page findings and explicit unreviewed limits.'},
            {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
             'bundle_root':str(folder),'description':'Source-bound individual proxies, raw lines, positions and retained block context.'}]

    q29=catalog.document('P-A-2016-44845-998bce33')
    operations=[]
    for bid,old,new in (('b000004','w- e','we'),('b000006','v- i','vi')):
        block=next(b for b in q29['blocks'] if b['block_id']==bid)
        if block['text'].count(old)!=1:
            raise ValueError('Checked discretionary word preimage changed')
        after=block['text'].replace(old,new)
        operations.append({'block_id':bid,'operation':'literal_replace','old':old,'new':new,'count':1,
            'before_text_sha256':digest(block['text'].encode()),'after_text_sha256':digest(after.encode()),
            'reason':'Printed discretionary word hyphen at the right line margin; next line continues the same word.'})
    _,evidence=proofs(29)
    # Literal evidence uses explicit files; layout bundles additionally copy the
    # whole source-evidence folder when that layout is applied in a later build.
    repair={**{k:q29[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root; 2026-10-31; physical page1 actually inspected',
        'checked_pages':[1],'operations':operations,
        'evidence':evidence+[{'path':str(base/'source-reviews/q029-opening-20261031-v1/page-0001.jpg'),
            'sha256':file_hash(base/'source-reviews/q029-opening-20261031-v1/page-0001.jpg'),
            'description':'Actually inspected bounded source JPEG; how-/ever and deriv-/ing line endings.'}],
        'reason':'Join only two source-checked discretionary word breaks; no prose rewriting.',
        'formula_verification':'paused','figure_distillation':'paused'}
    checked29=copy.deepcopy(q29)
    apply_text_repairs(checked29,[repair])

    def group(page,name,kind,ids,opening=None):
        lookup={x['line_id']:x for x in page['lines']}
        if not ids or any(not lookup[x]['text'].strip() for x in ids):
            raise ValueError('Empty checked group')
        return {'group_id':name,'kind':kind,'source_line_ids':ids,
            'text_sha256':digest(' '.join(lookup[x]['text'].strip() for x in ids).encode()),
            'reason':'Source-checked prose lanes/paragraph boundaries; preserve original words and unverified symbol bytes.',
            **({'opens_section':opening} if opening else {})}

    def block_ids(page,blocks):
        return [x['line_id'] for x in page['lines'] if x['native_block'] in blocks and
                x['text'].strip() and not x.get('superseded_by_ocr')]

    def lid(page,block,line):
        return f'p{page:04d}-n{block:04d}-l{line:04d}'

    def layout(doc,queue,selected):
        folder,evidence=proofs(queue)
        return {'schema':'source-text-layout-review-v1',
            **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
            'reviewer':'Codex root; 2026-10-31; selected physical page JPEGs actually inspected',
            'reason':'Restore checked complete author paragraphs and separate form/cover metadata without deleting any source text.',
            'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
            'evidence':evidence,'evidence_files':{str(p):file_hash(p) for p in folder.iterdir() if p.is_file()},
            'application_status':'Staged for later generation; not applied to v17 or running v18.',
            'remaining_uncertainties':['Only the specified opening pages checked; no whole-paper source acceptance.',
                'Formula/symbol semantics and correctness remain paused; all raw symbol bytes are retained.'],
            'formula_verification':'paused','figure_distillation':'paused'}

    q30=catalog.document('P-A-2016-46830-92f43919')
    pages30=rows(root/'papers'/q30['paper_id']/'raw/pages.jsonl');p=pages30[0]
    second=block_ids(p,[23,24])+[lid(1,25,i) for i in (0,2,1,3,5,4,6)]+[
        lid(1,26,i) for i in (0,2,3,1,4)]+block_ids(p,[27,28,29])
    third=[lid(1,30,i) for i in (0,1,2,3,5,6,4,7)]+block_ids(p,[31])
    groups30=[group(p,'p1-competition-form','front_matter',block_ids(p,range(18))),
        group(p,'p1-title','title',block_ids(p,[18])),
        group(p,'p1-summary-heading','heading',block_ids(p,[19]),{'role':'abstract','level':1}),
        group(p,'p1-opening','prose',block_ids(p,[21])),
        group(p,'p1-firstly','prose',block_ids(p,[22])),
        group(p,'p1-secondly','mixed',second),group(p,'p1-thirdly','mixed',third),
        group(p,'p1-finally','prose',block_ids(p,[32]))]
    review30=layout(q30,30,[{'page':1,'groups':groups30}])

    q31=catalog.document('P-A-2016-48649-e4d30266')
    pages31=rows(root/'papers'/q31['paper_id']/'raw/pages.jsonl');a,b=pages31[:2]
    groups31a=[group(a,'p1-competition-form','front_matter',block_ids(a,range(17))),
        group(a,'p1-summary-heading','heading',block_ids(a,[17]),{'role':'abstract','level':1}),
        *[group(a,f'p1-paragraph-{i}','prose',block_ids(a,blocks))
          for i,blocks in enumerate(([18],[19,20],[21],[22],[23],[24]),1)]]
    groups31b=[group(b,'p2-running-header','furniture',block_ids(b,[0])),
        group(b,'p2-team-date','front_matter',block_ids(b,[1,2])),
        group(b,'p2-abstract-heading','heading',block_ids(b,[3]),{'role':'abstract','level':1}),
        group(b,'p2-context-paragraph','prose',block_ids(b,[4])),
        group(b,'p2-model-paragraph','prose',block_ids(b,[5])),
        group(b,'p2-keywords','keywords',block_ids(b,[6]))]
    review31=layout(q31,31,[{'page':1,'groups':groups31a},{'page':2,'groups':groups31b}])
    summaries=[]
    for doc,pages,review in ((q30,pages30,review30),(q31,pages31,review31)):
        working,_=prepare_flow_pages(doc,pages,base/'span-metrics-20261030-v1')
        applied=apply_layout_reviews(doc,working,[review])
        candidate=make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
        candidate['layout_reviews']=applied
        validate_layout_reviews(candidate,pages)
        ids,excluded=select_sections(candidate,'abstract')
        blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text='\n\n'.join(b['text'] for b in blocks)
        if any(s in text for s in ('For office use only','MCM/ICM','January 28')):
            raise ValueError('Checked non-author metadata remains in abstract')
        if doc['paper_id']==q30['paper_id']:
            if len([b for b in blocks if b['kind']!='heading'])!=5 or 'declines to T min1 and stopping' not in text:
                raise ValueError('Checked prose paragraph/inline flow not retained')
        else:
            if {p for block in blocks for p in block['source_pages']}!={1,2} or len([b for b in blocks if b['kind']!='heading'])!=8:
                raise ValueError('Both checked source summaries must be retained')
        summaries.append({'paper_id':doc['paper_id'],'abstract_characters':len(text),
            'abstract_blocks':len(blocks),'abstract_pages':sorted({p for block in blocks for p in block['source_pages']})})
    for path,value in zip(paths[:3],(repair,review30,review31)):
        json_new(path,value)
    _,copies=prepare_review_bundles(paths[1:3],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'q29_discretionary_word_joins':2,
        'layout_summaries':summaries,'portable_layout_evidence_files':len(copies),
        'source_fidelity_approved':False,'ai_processing_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'}
    json_new(paths[3],result);print(result,flush=True)


if __name__=='__main__':
    main()
