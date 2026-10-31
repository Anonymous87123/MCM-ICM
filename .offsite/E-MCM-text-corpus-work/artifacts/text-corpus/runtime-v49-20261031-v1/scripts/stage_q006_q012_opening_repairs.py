"""Create-only literal word/bullet recovery and checked summary/cover lanes."""
from pathlib import Path

from corpus_queries import select_sections
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, rows, section_blocks


def main():
    base = Path(__file__).resolve().parents[1] / 'artifacts/text-corpus'
    root = base / 'reflow-20261030-v16'
    review_dir = base / 'reviews/20261030'
    outputs = [review_dir/name for name in ('q006-determinate-word-repair-v1.json',
        'q012-summary-cover-layout-v1.json','q012-list-bullet-transcription-v1.json',
        'q006-q012-opening-preflight-v1.json')]
    if any(p.exists() for p in outputs):
        raise ValueError('Create-only proof exists; preserve it')
    catalog = Catalog(root)
    findings = review_dir / 'q006-q012-opening-text-findings-v1.json'

    def evidence(folder):
        return [{'path':str(findings),'sha256':file_hash(findings),
                 'description':'Actual bounded source wording, lane findings and limitations.'},
                {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
                 'description':'Frozen source identity and individual page/proxy hashes.'},
                *[{'path':str(p),'sha256':file_hash(p),
                   'description':'Actually inspected bounded source page JPEG.'}
                  for p in sorted(folder.glob('*.jpg'))]]

    def literal(doc, pages, operations, proofs, reason):
        return {**{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
            'reviewer':'Codex root; 2026-10-30; exact source text inspected',
            'checked_pages':pages,'operations':operations,'evidence':proofs,'reason':reason,
            'formula_verification':'paused','figure_distillation':'paused'}

    def replacement(block, old, new, reason):
        if block['text'].count(old)!=1:
            raise ValueError('Literal preimage occurrence differs')
        after=block['text'].replace(old,new)
        return {'block_id':block['block_id'],'operation':'literal_replace',
            'old':old,'new':new,'count':1,'before_text_sha256':digest(block['text'].encode()),
            'after_text_sha256':digest(after.encode()),'reason':reason}

    q6 = catalog.document('P-A-2011-12149-cb2b7105')
    block = next(b for b in q6['blocks'] if b['block_id']=='b000006')
    q6_review = literal(q6,[1],[replacement(block,'r- m','rm',
        'Printed right-margin deter- continues mine on the next line; join this one word only.')],
        evidence(base/'source-reviews/q006-abstract-20261030-v1'),
        'Recover a source-checked discretionary line-break hyphen without rewriting author prose.')
    import copy
    checked6=copy.deepcopy(q6)
    apply_text_repairs(checked6,[q6_review])
    if 'to determine the acceleration' not in checked6['blocks'][q6['blocks'].index(block)]['text']:
        raise ValueError('Checked word was not restored')

    q12=catalog.document('P-A-2012-15065-1cbc0cd9')
    pages=rows(root/'papers'/q12['paper_id']/'raw/pages.jsonl')
    active=[x for x in pages[0]['lines'] if x['text'].strip() and not x.get('superseded_by_ocr')]
    definitions=[
        ('p1-form','front_matter',lambda x:x['native_block']<18),
        ('p1-summary-form-heading','front_matter',lambda x:x['line_id']=='p0001-n0018-l0000'),
        ('p1-goal','prose',lambda x:x['line_id'] in ('p0001-n0018-l0001','p0001-n0018-l0002')),
        ('p1-models-lead','prose',lambda x:x['line_id']=='p0001-n0018-l0004'),
        ('p1-vector-model','list',lambda x:x['native_block']==19),
        ('p1-sunlight-model','list',lambda x:x['native_block']==20 and
         x['line_id'] in [f'p0001-n0020-l{n:04d}' for n in range(5)]),
        ('p1-shape-comparison','prose',lambda x:x['native_block']==20 and
         x['line_id'] in [f'p0001-n0020-l{n:04d}' for n in range(6,17)]),
        ('p1-mass-application','prose',lambda x:x['native_block']==20 and
         x['line_id'] in [f'p0001-n0020-l{n:04d}' for n in range(18,24)])]
    groups=[]
    for name,kind,predicate in definitions:
        members=[x for x in active if predicate(x)]
        groups.append({'group_id':name,'kind':kind,
            'source_line_ids':[x['line_id'] for x in members],
            'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
            'reason':'Actually checked Summary Sheet; native bullet lines precede their model sentences.'})
    cover=[x for x in pages[1]['lines'] if x['text'].strip() and not x.get('superseded_by_ocr')]
    selected=[{'page':1,'groups':groups},{'page':2,'groups':[{
        'group_id':'p2-separate-cover','kind':'front_matter',
        'source_line_ids':[x['line_id'] for x in cover],
        'text_sha256':digest(' '.join(x['text'].strip() for x in cover).encode()),
        'reason':'Actually checked separate cover, not a summary continuation; all wording retained.'}]}]
    folder=base/'source-reviews/q012-opening-20261030-v1'
    layout={**{k:q12[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'schema':'source-text-layout-review-v1','pages':selected,
        'reviewer':'Codex root; 2026-10-30; physical pages1/2 actually inspected',
        'reason':'Restore complete Summary Sheet paragraphs and bullet order; preserve the separate cover as front matter.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
        'evidence':[{**p,**({'bundle_root':str(folder)} if p['path']==str(folder/'manifest.json') else {})}
                    for p in evidence(folder)],
        'evidence_files':{str(p):file_hash(p) for p in folder.iterdir() if p.is_file()},
        'remaining_uncertainties':['Only opening pages1/2 checked; whole-paper and section fidelity remain pending.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(q12,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(q12,working,[layout])
    doc=make_document({k:q12[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    doc['layout_reviews']=applied
    validate_layout_reviews(doc,pages)
    bullets=[b for b in doc['blocks'] if b.get('layout_group_id') in ('p1-vector-model','p1-sunlight-model')]
    bullet_review=literal(q12,[1],[replacement(b,'\uf06c','•',
        'The source visibly prints a solid round list marker before the model name.') for b in bullets],
        evidence(folder),'Transcribe two checked list markers only; retain every sentence and its original grammar.')
    apply_text_repairs(doc,[bullet_review])
    validate_layout_reviews(doc,pages)
    ids,excluded=select_sections(doc,'abstract')
    abstract=section_blocks(doc,ids,excluded_roles=excluded)
    if {p for b in abstract for p in b['source_pages']}!={1} or len(abstract)!=6:
        raise ValueError('Summary/cover scope differs')
    if not all(b['text'].startswith('• The ') for b in bullets):
        raise ValueError('Checked bullet placement differs')
    for path,value in zip(outputs[:3],(q6_review,layout,bullet_review)):
        json_new(path,value)
    _,copies=prepare_review_bundles([outputs[1]],identity_fields=('paper_id',),application_status='preflight only')
    json_new(outputs[3],{'parent_dataset_id':catalog.identity,'q6_word_repairs':1,
        'q12_bullet_repairs':2,'q12_layout_groups':9,'q12_abstract_pages':[1],
        'q12_abstract_blocks':len(abstract),'q12_abstract_characters':len('\n\n'.join(b['text'] for b in abstract)),
        'portable_layout_evidence_files':len(copies),'source_fidelity_approved':False,
        'ai_reading_receipts_created':0})
    print(outputs[3].read_text(encoding='utf-8'))


if __name__=='__main__':
    main()
