"""New immutable continuous author views, q96 recovery and complete q110 summary."""
import os
from pathlib import Path
from corpus_reader import Catalog
from corpus_queries import selected_blocks
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json, write_new
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work);base=work/'artifacts/text-corpus'
    parent=base/'reflow-20261031-v24';output=base/'reflow-20261031-v25'
    request=base/'build-request-reflow-20261031-v25.json';report=base/'integrity-reflow-20261031-v25.json'
    if any(p.exists() for p in (output,request,report)):
        raise ValueError('Create-only build state exists; preserve it')
    accepted=read_json(base/'integrity-reflow-20261031-v24.json')
    audit_path=base/'span-origin-flow-full-20261031-v19.json';audit=read_json(audit_path)
    catalog=Catalog(parent);scope=read_json(parent/'scope.json');directory=base/'reviews/20261031'
    layouts=[directory/f'q{n:03d}-opening-layout-v1.json' for n in (96,110)]
    repairs=[directory/f'q{n:03d}-opening-word-repairs-v1.json' for n in (96,110)]
    paragraphs=[directory/'q096-opening-paragraph-v1.json']
    reviews=[directory/'q110-summary-source-review-v1.json']
    exact={str(p.resolve()):file_hash(p) for p in (*layouts,*repairs,*paragraphs,*reviews)};totals=audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id']!=catalog.identity or
            audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256']!=exact or
            (totals['papers'],totals['pages'],totals['source_lines'])!=(435,11552,954866) or
            totals['contents_pages_before']!=352 or totals['contents_pages_after']!=352):
        raise ValueError('Exact frozen full prospective replay required')
    q96=read_json(directory/'q096-opening-preflight-v1.json')
    q110=read_json(directory/'q110-opening-preflight-v1.json')
    if (q96['parent_dataset_id']!=catalog.identity or q110['parent_dataset_id']!=catalog.identity or
            q96['results']['abstract']['characters']!=6673 or q110['characters']!=1790 or
            not q96['source_lines_accounted_once'] or not q110['source_lines_accounted_once']):
        raise ValueError('Individual source preflight differs')
    frozen={name:file_hash(work/'scripts'/name) for name in audit['implementation_sha256']}
    if frozen!=audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name:file_hash(work/'scripts'/name) for name in
        ('index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py')})
    fields=('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
        'absence_review_sha256','layout_review_sha256','paragraph_join_review_sha256')
    inputs={field:[] for field in fields}
    for field in fields:
        for name,sha in scope.get(field,{}).items():
            path=Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Source proof changed: '+name)
            inputs[field].append(path)
    inputs['layout_review_sha256']+=layouts;inputs['text_repair_sha256']+=repairs
    inputs['paragraph_join_review_sha256']+=paragraphs;inputs['source_review_sha256']+=reviews
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('Unverified Unicode OCR must stay unapplied')
    native=base/'native-20261029-v1';native_id=Catalog(native).identity
    if native_id!=scope['parent_dataset_id']:
        raise ValueError('Original native generation required')
    bindings={field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    old_abstract={s['paper_id']:s for s in catalog.select('abstract')}
    metrics=base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':native_id,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'implementation_sha256':frozen,'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Add continuous author.md plus exact external source map for all435papers. Preserve full.md evidence export. Individually restore q96two technical summaries/memo ownership and q110complete seven-paragraph Summary Sheet/two-page Contents; one q110section source review.',
        'remaining_limit':'Other source defects, later bodies and actual all-chapter reading remain pending.',
        'source_section_reviews_added':1,'whole_paper_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],
        metrics,inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py','index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py'):
        write_new(output/'inputs'/name,(work/'scripts'/name).read_bytes())
    write_new(output/'inputs/build_text_corpus_v25.py',Path(__file__).read_bytes())
    write_new(output/'inputs/build-request.json',request.read_bytes())
    print(index(output),flush=True);built=Catalog(output)
    expected={q96['paper_id']:(6673,10,{1,3,4},q96['results']['abstract']['sha256']),
              q110['paper_id']:(1790,7,{1},q110['sha256'])}
    for item in built.select('abstract'):
        pid=item['paper_id']
        if pid not in expected:
            if item['text_sha256']!=old_abstract[pid]['text_sha256']:
                raise ValueError('Unrelated abstract changed: '+pid)
            continue
        text,spans=built.text_and_spans(item);blocks=selected_blocks(built.document(pid),item)
        chars,count,pages,sha=expected[pid]
        logical=sum(b['kind'] in {'prose','list'} for b in blocks)-sum(bool(b.get('paragraph_continues_from')) for b in blocks)
        if (len(text)!=chars or item['text_sha256']!=sha or {p for s in spans for p in s['pages']}!=pages or logical!=count):
            raise ValueError('Checked individual summary contract changed')
        if pid==q110['paper_id'] and item['status']!='verified':
            raise ValueError('Actually checked q110Summary did not retain source review')
    result=validate(output,work,True)
    if (result['defects'].get('contents_page_boundary_review',0)!=352 or
            result['totals'].get('continuous_author_views_checked')!=435):
        raise ValueError('Contents preservation or continuous author views differ; retain candidate')
    if any(file_hash(Path(p))!=sha for mapping in bindings.values() for p,sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work/'scripts'/name)!=sha for name,sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report,result);print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate retained without acceptance')


if __name__=='__main__':
    main()
