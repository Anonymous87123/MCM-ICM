"""Source-checked q32 opening lanes; preserve a real abstract child on a Contents page."""
from collections import Counter
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
    root=base/'reflow-20261030-v17';out=base/'reviews/20261031'
    paths=[out/name for name in ('q032-opening-mixed-contents-layout-v1.json',
        'q032-temperature-word-repair-v1.json','q032-opening-mixed-contents-preflight-v1.json')]
    if any(p.exists() for p in paths):
        raise ValueError('Create-only q32 proof exists; preserve it')
    findings=out/'q032-opening-mixed-contents-findings-v1.json'
    catalog=Catalog(root);doc=catalog.document('P-A-2016-54164-57a2b533')
    pages=rows(root/'papers'/doc['paper_id']/'raw/pages.jsonl')
    folders=[base/'source-reviews/q032-summary-sheet-20261031-v1',
             base/'source-reviews/q032-opening-20261031-v1']
    evidence=[{'path':str(findings),'sha256':file_hash(findings),
        'description':'Actually checked physical pages1–4, source continuation, genuine child section and midpage Contents.'}]
    files={}
    for folder in folders:
        evidence.append({'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
            'bundle_root':str(folder),'description':'Source-checked individual bounded page proxies and native positions.'})
        files.update({str(p):file_hash(p) for p in folder.iterdir() if p.is_file()})

    def group(number,name,kind,blocks,opening=None):
        members=[x for x in pages[number-1]['lines'] if x['native_block'] in blocks and
                 x['text'].strip() and not x.get('superseded_by_ocr')]
        if not members:
            raise ValueError('Empty source-bound q32 group')
        return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
            'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
            'reason':'Actual page check preserves author paragraphs before the printed Contents and separate cover/form material.',
            **({'opens_section':opening} if opening else {})}

    selected=[{'page':1,'groups':[
        group(1,'p1-form-instructions','front_matter',range(18)),
        group(1,'p1-abstract-heading','heading',[18],{'role':'abstract','level':1}),
        *[group(1,f'p1-paragraph-{n-18}','prose',[n]) for n in range(19,26)]]},
        {'page':2,'groups':[group(2,'p2-separate-cover','front_matter',range(4))]},
        {'page':3,'groups':[
            group(3,'p3-header','furniture',[0]),
            group(3,'p3-abstract-heading','heading',[1],{'role':'abstract','level':1}),
            *[group(3,f'p3-abstract-paragraph-{n-1}','prose',[n]) for n in range(2,9)],
            group(3,'p3-nontechnical-heading','heading',[9],{'role':'other','level':2}),
            *[group(3,f'p3-nontechnical-paragraph-{n-9}','prose',[n]) for n in range(10,14)],
            group(3,'p3-footer','furniture',[14])]},
        {'page':4,'groups':[
            group(4,'p4-header','furniture',[0]),
            *[group(4,f'p4-author-continuation-{n}','prose',[n]) for n in range(1,6)],
            group(4,'p4-contents-heading','heading',[6],{'role':'contents','level':1}),
            group(4,'p4-contents-entries','source_object',range(7,12)),
            group(4,'p4-footer','furniture',[12])]}]
    review={'schema':'source-text-layout-review-v1',
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root;2026-10-31; physical pages1–4 actually inspected',
        'reason':'Retain Summary and Abstract including the actual nontechnical child continuation above midpage Contents; separate cover/form/footer.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
        'evidence':evidence,'evidence_files':files,
        'application_status':'Staged individually for a later immutable generation; no old receipts changed.',
        'remaining_uncertainties':['Cross-page logical paragraph join remains explicitly pending.',
            'Only opening pages1–4 checked; whole-paper prose fidelity and source acceptance pending.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(doc,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(doc,working,[review])
    candidate=make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    candidate['layout_reviews']=applied
    validate_layout_reviews(candidate,pages)
    block=next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p3-abstract-paragraph-2')
    if block['text'].count('m- p')!=1:
        raise ValueError('Checked temperature word preimage changed')
    repair={**{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':review['reviewer'],'checked_pages':[3],'reason':'Join the printed discretionary tem-/perature line break only.',
        'evidence':evidence+[{'path':str(folders[1]/'page-0003.jpg'),
            'sha256':file_hash(folders[1]/'page-0003.jpg'),'description':'Actually checked printed tem-/perature line ending.'}],
        'operations':[{'block_id':block['block_id'],'operation':'literal_replace','old':'m- p','new':'mp','count':1,
            'before_text_sha256':digest(block['text'].encode()),
            'after_text_sha256':digest(block['text'].replace('m- p','mp').encode()),
            'reason':'Source-checked discretionary word break, no author rewrite.'}],
        'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(candidate,[repair])
    ids,excluded=select_sections(candidate,'abstract')
    blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
    text='\n\n'.join(b['text'] for b in blocks)
    if ('width of the bathtub, and attaches' not in text or 'kids.”' not in text or
            any(s in text for s in ('Contents','February 2016','Page 1','Type a summary')) or
            len([b for b in blocks if b['kind']!='heading'])!=23):
        raise ValueError('Q32 source continuation still lost or mixed with non-author material')
    source=Counter(x['line_id'] for p in pages for x in p['lines'])
    used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source!=used or any(n!=1 for n in source.values()):
        raise ValueError('Q32 raw source line lost or duplicated')
    for path,value in zip(paths[:2],(review,repair)):
        json_new(path,value)
    _,copies=prepare_review_bundles([paths[0]],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'paper_id':doc['paper_id'],
        'abstract_characters':len(text),'abstract_pages':sorted({p for b in blocks for p in b['source_pages']}),
        'abstract_blocks':len(blocks),'author_paragraph_fragments':23,'word_repairs':1,
        'portable_layout_evidence_files':len(copies),'source_fidelity_approved':False,
        'cross_page_logical_join':'pending; source-checked sentence preserved in adjacent fragments',
        'ai_processing_receipts_created':0}
    json_new(paths[2],result);print(result,flush=True)


if __name__=='__main__':
    main()
