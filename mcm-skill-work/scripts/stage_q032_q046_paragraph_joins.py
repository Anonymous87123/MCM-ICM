"""Bind two individually inspected cross-page prose continuations, create-only."""
from pathlib import Path

from corpus_reader import Catalog
from corpus_queries import select_sections, selected_blocks
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_paragraph_reviews import apply_paragraph_reviews,validate_paragraph_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from source_absence_reviews import prepare_review_bundles
from text_corpus import digest,file_hash,json_new,make_document,read_json,rows,text_with_block_spans


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    directory=base/'reviews/20261031';root=base/'reflow-20261031-v19'
    targets=[directory/name for name in ('q032-paragraph-continuation-v1.json',
        'q046-paragraph-continuation-v1.json','q032-q046-paragraph-preflight-v1.json')]
    if any(p.exists() for p in targets):
        raise ValueError('Create-only paragraph proof exists; preserve it')
    catalog=Catalog(root);results=[]
    specifications=[('P-A-2016-54164-57a2b533','q032-opening-mixed-contents-layout-v1.json',
        'p3-nontechnical-paragraph-4','p4-author-continuation-1',[3,4],'abstract',7515,
        'spans the length and width of the bathtub'),
        ('P-A-2019-1926690-fc36d223','q046-opening-layout-v1.json',
         'p2-letter-paragraph-5','p3-letter-paragraph-1',[2,3],'memo',7072,
         'prey species (assumed to be deer)')]
    for target,(pid,layout_name,left_gid,right_gid,numbers,query,expected,phrase) in zip(targets,specifications):
        old=catalog.document(pid);pages=rows(root/'papers'/pid/'raw/pages.jsonl')
        working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
        layouts=list(old.get('layout_reviews',[]));repairs=list(old.get('text_repair_reviews',[]))
        layout=read_json(directory/layout_name)
        if pid.startswith('P-A-2019-'):
            layouts.append(layout);repairs.append(read_json(directory/'q046-opening-word-repairs-v1.json'))
        applied=apply_layout_reviews(old,working,layouts)
        candidate=make_document({k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
        candidate['layout_reviews']=applied;apply_text_repairs(candidate,repairs)
        validate_layout_reviews(candidate,pages)
        a=next(b for b in candidate['blocks'] if b.get('layout_group_id')==left_gid)
        b=next(b for b in candidate['blocks'] if b.get('layout_group_id')==right_gid)
        before=[(x['text'],list(x['source_line_ids'])) for x in candidate['blocks']]
        evidence=list(layout['evidence']);files=dict(layout['evidence_files'])
        for proof in evidence:
            files[proof['path']]=proof['sha256']
        review={'schema':'source-paragraph-join-review-v1',
                **{k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
                'reviewer':'Codex root;2026-10-31; the two physical pages actually inspected',
                'reason':'One printed author paragraph continues across the physical page boundary, with only running furniture between its fragments.',
                'checked_pages':numbers,'evidence':evidence,'evidence_files':files,
                'joins':[{'left_block_id':a['block_id'],'right_block_id':b['block_id'],
                          'left_text_sha256':digest(a['text'].encode()),'right_text_sha256':digest(b['text'].encode()),
                          'separator':' ','reason':'Exact source continuation: '+phrase}],
                'source_fidelity_approved':False,'whole_paper_source_acceptance':False,
                'formula_verification':'paused','figure_distillation':'paused'}
        apply_paragraph_reviews(candidate,[review]);validate_paragraph_reviews(candidate)
        if before!=[(x['text'],list(x['source_line_ids'])) for x in candidate['blocks']]:
            raise ValueError('Paragraph linking changed a source block')
        ids,excluded=select_sections(candidate,query)
        selected=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text,spans=text_with_block_spans(selected)
        if len(text)!=expected or phrase not in text:
            raise ValueError('Source continuation not restored exactly')
        for span,block in zip(spans,selected):
            if text[span['start']:span['end']]!=block['text']:
                raise ValueError('Source span changed after paragraph join')
        json_new(target,review)
        _,copies=prepare_review_bundles([target],identity_fields=('paper_id',),application_status='preflight only')
        results.append({'paper_id':pid,'query':query,'characters':len(text),'text_sha256':digest(text.encode()),
                        'left_block_id':a['block_id'],'right_block_id':b['block_id'],
                        'unchanged_source_blocks':True,'source_span_roundtrip':True,
                        'portable_evidence_files':len(copies),'source_fidelity_approved':False})
    result={'parent_dataset_id':catalog.identity,'results':results,'ai_processing_receipts_created':0}
    json_new(targets[2],result);print(result,flush=True)


if __name__=='__main__':
    main()
