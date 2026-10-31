"""Create-only v15: source-bound bibliography/appendix, prose and absence fixes."""
import os
from pathlib import Path

from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json
from validate_text_corpus import validate


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work/'artifacts/text-corpus'
    parent = base/'reflow-20261030-v14'
    output = base/'reflow-20261030-v15'
    request = base/'build-request-reflow-20261030-v15.json'
    report_path = base/'integrity-reflow-20261030-v15.json'
    if any(p.exists() for p in (output,request,report_path)):
        raise ValueError('Create-only build state exists; inspect and preserve it')
    audit_path = base/'span-origin-flow-full-20261030-v7.json'
    audit = read_json(audit_path)
    catalog = Catalog(parent)
    scope = read_json(parent/'scope.json')
    totals = audit['totals']
    if (audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            totals['papers']!=435 or totals['pages']!=11552 or totals['source_lines']!=954866 or
            totals['contents_pages_before']!=352 or totals['contents_pages_after']<352):
        raise ValueError('Full-scope ownership/review/Contents-preservation preview has not passed')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Audited implementation changed: '+name)
    native = base/'native-20261029-v1'
    if Catalog(native).identity!=scope['parent_dataset_id']:
        raise ValueError('Original native generation required, not augmented raw pages')
    fields = ('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
              'absence_review_sha256','layout_review_sha256')
    inputs = {}
    for field in fields:
        inputs[field] = []
        for name,sha in scope[field].items():
            path = Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Existing frozen input changed: '+name)
            inputs[field].append(path)
    reviews = base/'reviews/20261030'
    additions = {
        'absence_review_sha256': [reviews/'q165-abstract-absence-v1.json',reviews/'q170-abstract-absence-v1.json'],
        'layout_review_sha256': [reviews/'q164-pages10-11-appendix-layout-v1.json',reviews/'q165-pages9-10-prose-boundaries-v1.json']}
    extra = {str(p.resolve()):file_hash(p) for paths in additions.values() for p in paths}
    if audit['review_input_sha256']!=extra:
        raise ValueError('Prospective audit did not bind this exact source-proof batch')
    for field,paths in additions.items():
        inputs[field].extend(paths)
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('Retain the same53 frozen OCR inputs; new Unicode OCR remains unverified')
    bindings = {field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    metrics = base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':Catalog(native).identity,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),'inputs':bindings,
        'new_checks':'q164 pages10/11 source ownership; q165 pages9/10 author prose and whole-source abstract absence; q170 whole-source abstract absence.',
        'unverified_unicode_ocr_applied':False,'whole_paper_source_acceptance':False,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    print(index(output),flush=True)
    result = validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=totals['contents_pages_after']:
        raise ValueError('Built Contents census differs; preserve candidate without promotion')
    for mapping in bindings.values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Frozen review/OCR bytes changed during build')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Audited implementation changed during build')
    json_new(report_path,result)
    print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Preserve failed candidate; do not promote')


if __name__ == '__main__':
    main()
