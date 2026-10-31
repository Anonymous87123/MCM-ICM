"""Full-scope source-origin flow audit, without changing any corpus generation."""
import argparse
from collections import Counter
from pathlib import Path
from corpus_reader import Catalog
from source_span_metrics import prepare_flow_pages
from source_layout_reviews import apply_layout_reviews
from resegment_text_corpus import apply_reviews
from source_text_repairs import apply_text_repairs
from source_absence_reviews import apply_absence_reviews,prepare_absence_reviews,prepare_review_bundles
from source_paragraph_reviews import apply_paragraph_reviews,validate_paragraph_reviews
from source_ocr_page_reviews import apply_ocr_page_reviews
from text_corpus import digest,encoded,file_hash,json_new,make_document,read_json,rows,section_text


def contents_pages(document):
    return {d['page'] for d in document.get('defects',[])
            if d['code']=='contents_page_boundary_review'}


def lost_contents_pages(previous,candidate):
    """This batch must not silently lose any already identified contents page.

    Preserving a candidate is not source approval. A deliberate future reversal
    requires a separate source-reviewed batch, not a weakened aggregate counter.
    """
    return sorted(contents_pages(previous)-contents_pages(candidate))


def merge_text_repairs(existing, additional, paper_id):
    """Add new checked proofs; replace existing ones only by an exact binding.

    Actual source/preimage validation remains in apply_text_repairs. The preview
    must also support a paper's first literal repair, not only rebinding an old
    proof after a layout change.
    """
    repairs = list(existing)
    for review in additional:
        if review['paper_id'] != paper_id:
            continue
        previous = review.get('binding_transfer', {}).get('previous_review_sha256')
        if previous is not None:
            matches = [r for r in repairs if digest(encoded(r)) == previous]
            if len(matches) != 1:
                raise ValueError('Replacement does not bind exactly one previous review')
            repairs[repairs.index(matches[0])] = review
        else:
            if any(digest(encoded(r)) == digest(encoded(review)) for r in repairs):
                raise ValueError('Additional source-text repair already declared')
            repairs.append(review)
    return repairs


def preview(root,metrics_root,limit=None,repair_files=(),layout_files=(),absence_files=(),paragraph_files=(),source_review_files=()):
    catalog=Catalog(root);totals=Counter();papers=[];errors=[];replay=[]
    implementation={n:file_hash(Path(__file__).with_name(n)) for n in
                    ('source_span_metrics.py','text_corpus.py','preview_span_origin_flow.py',
                     'source_text_repairs.py','source_layout_reviews.py','source_absence_reviews.py','resegment_text_corpus.py',
                     'corpus_queries.py','corpus_reader.py','source_paragraph_reviews.py','source_ocr_page_reviews.py')}
    extra_repairs=[read_json(p) for p in repair_files]
    extra_layout,_=prepare_review_bundles(layout_files,identity_fields=('paper_id',),application_status='prospective only')
    extra_absence,_=prepare_absence_reviews(absence_files)
    extra_paragraph,_=prepare_review_bundles(paragraph_files,identity_fields=('paper_id',),application_status='prospective only')
    extra_source=[read_json(p) for p in source_review_files]
    inputs={str(p.resolve()):file_hash(p) for p in (*repair_files,*layout_files,*absence_files,*paragraph_files,*source_review_files)}
    for record in catalog.papers[:limit]:
        old=catalog.document(record['paper_id']);pid=old['paper_id']
        raw=root/'papers'/pid/'raw/pages.jsonl'
        if file_hash(raw)!=old['raw_pages_sha256']:
            raise ValueError('Frozen native evidence changed')
        pages=rows(raw)
        working,flow=prepare_flow_pages(old,pages,metrics_root)
        meta={k:old[k] for k in ('paper_id','problem_type','year','queue_position','page_count',
                               'source_sha256','source_relative_path','raw_pages_sha256')}
        layouts=apply_layout_reviews(meta,working,old.get('layout_reviews',[])+extra_layout)
        new=make_document(meta,working,improved=True);new['layout_reviews']=layouts
        lost=lost_contents_pages(old,new)
        if lost:
            errors.append({'paper_id':pid,'error':'Previously identified contents pages lost',
                           'physical_pages':lost})
        raw_ids=[l['line_id'] for p in pages for l in p['lines']]
        actual=[lid for b in new['blocks'] for lid in b['source_line_ids']]
        actual+=[x['line_id'] for x in new['excluded_source_lines']]
        if Counter(raw_ids)!=Counter(actual) or len(raw_ids)!=len(set(raw_ids)):
            errors.append({'paper_id':pid,'error':'Source line ownership differs'})
        before={lid:b['text'] for b in old['blocks'] for lid in b['source_line_ids']}
        changed_groups=sum(any(before.get(lid)!=b['text'] for lid in b['source_line_ids']) for b in new['blocks'])
        try:
            repairs=merge_text_repairs(old.get('text_repair_reviews',[]),extra_repairs,pid)
            apply_text_repairs(new,repairs)
            apply_paragraph_reviews(new,old.get('paragraph_join_reviews',[])+extra_paragraph)
            validate_paragraph_reviews(new)
            apply_reviews(new,[s['review'] for s in old['sections'] if s.get('review')]+extra_source)
            apply_ocr_page_reviews(new,pages)
            apply_absence_reviews(new,list(old.get('absence_reviews',{}).values())+extra_absence)
        except ValueError as exc:
            replay.append({'paper_id':pid,'error':str(exc),
                'disposition':'Do not promote; reviewed source text/IDs need explicit binding to the new candidate.'})
        totals.update(papers=1,pages=len(pages),source_lines=len(raw_ids),changed_flow_lines=len(flow['changed_lines']),
            changed_block_groups=changed_groups,papers_with_changed_flow=bool(flow['changed_lines']),
            contents_pages_before=len(contents_pages(old)),contents_pages_after=len(contents_pages(new)))
        selected=[s['section_id'] for s in new['sections'] if s['role']=='abstract']
        text=section_text(new,selected)
        papers.append({'paper_id':pid,'queue_position':record['queue_position'],
            'metrics_sha256':flow['metrics_sha256'],'changed_flow_lines':flow['changed_lines'],
            'changed_block_groups':changed_groups,'abstract_text_sha256':digest(text.encode()),
            'sections':len(new['sections']),'blocks':len(new['blocks']),
            'contents_pages_before':sorted(contents_pages(old)),
            'contents_pages_after':sorted(contents_pages(new))})
        if len(papers)%50==0:
            print({'span_flow_papers_checked':len(papers)},flush=True)
    if any(file_hash(Path(__file__).with_name(n))!=sha for n,sha in implementation.items()):
        raise ValueError('Candidate implementation changed during audit')
    if any(file_hash(Path(p))!=sha for p,sha in inputs.items()):
        raise ValueError('Prospective review input changed during audit')
    return {'parent_dataset_id':catalog.identity,'metrics_root':str(metrics_root),
        'implementation_sha256':implementation,'review_input_sha256':inputs,'totals':dict(totals),'errors':errors,
        'review_replay_conflicts':replay,'papers':papers,'source_fidelity_approved':False,
        'meaning':'Exact baseline metadata, candidate grouping only; no source review or reading acceptance.'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--corpus-root',type=Path,required=True);p.add_argument('--metrics-root',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True);p.add_argument('--limit',type=int)
    p.add_argument('--text-repair',type=Path,action='append',default=[])
    p.add_argument('--layout-review',type=Path,action='append',default=[])
    p.add_argument('--absence-review',type=Path,action='append',default=[])
    p.add_argument('--paragraph-review',type=Path,action='append',default=[])
    p.add_argument('--source-review',type=Path,action='append',default=[])
    a=p.parse_args()
    if a.report.exists():
        raise ValueError('Create-only report already exists')
    result=preview(a.corpus_root.resolve(),a.metrics_root.resolve(),a.limit,a.text_repair,a.layout_review,a.absence_review,a.paragraph_review,a.source_review);json_new(a.report,result)
    print({k:v for k,v in result.items() if k!='papers'},flush=True)
