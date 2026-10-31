"""Restore all seven Summary Sheet paragraphs and keep two Contents pages separate."""
from collections import Counter
from pathlib import Path
from corpus_reader import Catalog
from corpus_queries import select_sections, selected_blocks, all_author_blocks
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, rows, text_with_block_spans


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    root=base/'reflow-20261031-v24';out=base/'reviews/20261031'
    targets=[out/f'q110-opening-{name}-v1.json' for name in ('layout','word-repairs','preflight')]
    if any(p.exists() for p in targets):
        raise ValueError('Create-only q110 proof exists; preserve it')
    catalog=Catalog(root);old=catalog.document('P-B-2015-38720-26d38781')
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    folder=out/'q110-opening-pages-v1';findings=out/'q110-opening-findings-v1.json'
    evidence=[{'path':str(findings),'sha256':file_hash(findings),'description':'Actually checked source-page prose and navigation ownership findings.'},
        {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
         'bundle_root':str(folder),'description':'Four individually inspected bounded JPEG/native physical pages.'}]
    files={str(p):file_hash(p) for p in folder.iterdir() if p.is_file()};files[str(findings)]=file_hash(findings)
    def group(page,name,kind,natives=None,ids=None,opening=None):
        members=[x for x in pages[page-1]['lines'] if x['text'].strip() and
                 (x['line_id'] in ids if ids is not None else x['native_block'] in natives)]
        return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
            'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
            'reason':'Individually checked printed text lane, bullet paragraph and source ownership.',
            **({'opens_section':opening} if opening else {})}
    def part(name,kind,start,end):
        return group(1,name,kind,ids=[f'p0001-n0000-l{i:04d}' for i in range(start,end+1)])
    groups={1:[part('p1-title','title',0,1),part('p1-context','prose',3,6),part('p1-roadmap','prose',8,12),
        *[group(1,f'p1-bullet-{n}','list',[n]) for n in (1,2,3,4)],group(1,'p1-closing','prose',[5])],
        2:[group(2,'p2-header','furniture',[0]),group(2,'p2-contents-title','heading',[1],opening={'role':'contents','level':1}),
           group(2,'p2-contents-entries','source_object',[2])],
        3:[group(3,'p3-header','furniture',[0]),group(3,'p3-contents-entries','source_object',[1])]}
    meta={k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
    layout={'schema':'source-text-layout-review-v1',**meta,'reviewer':'Codex root;2026-10-31; physical pages1–4',
        'reason':'All four bullet labels are inline Summary Sheet prose; preserve complete bullets and closing. Pages2–3 are Contents.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
        'pages':[{'page':p,'groups':g} for p,g in groups.items()],'evidence':evidence,'evidence_files':files,
        'source_fidelity_approved':False,'remaining_uncertainties':['Later source pages5–61 and full Introduction remain unreviewed.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[layout]);candidate=make_document(meta,working,improved=True)
    candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
    operations=[]
    pairs={1:[(': \u200b',':')],2:[(': \u200b',':'),(',\u200b \u200b',',')],3:[(':\u200b',':')],4:[(': \u200b',':')]}
    for number, replacements in pairs.items():
        block=next(b for b in candidate['blocks'] if b.get('layout_group_id')==f'p1-bullet-{number}')
        text=block['text']
        for before,after in replacements:
            if text.count(before)!=1:
                raise ValueError('Exact invisible-format preimage differs')
            changed=text.replace(before,after)
            operations.append({'block_id':block['block_id'],'operation':'literal_replace','old':before,'new':after,
                'count':1,'before_text_sha256':digest(text.encode()),'after_text_sha256':digest(changed.encode()),
                'reason':'Remove source-checked invisible PDF format artifacts adjacent to literal punctuation; preserve author wording.'})
            text=changed
    repair={**meta,'reviewer':layout['reviewer'],'reason':'Five exact invisible-format replacements; no prose rewriting.',
        'checked_pages':[1,2,3,4],'operations':operations,'evidence':evidence,'source_fidelity_approved':False,
        'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(candidate,[repair]);validate_layout_reviews(candidate,pages)
    source=Counter(x['line_id'] for p in pages for x in p['lines'])
    used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source!=used or any(n!=1 for n in used.values()):
        raise ValueError('Source line lost or duplicated')
    ids,excluded=select_sections(candidate,'abstract')
    blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
    text,spans=text_with_block_spans(blocks)
    if ({p for s in spans for p in s['pages']}!={1} or len(blocks)!=7 or '\u200b' in text or
            not text.startswith('When a plane disappears') or not text.endswith('the majority of lost planes.') or
            '38 hours' not in text or '3.6 hours' not in text or '4.7 hours' not in text or
            'Hidden in Plane Sight' in text):
        raise ValueError('Complete seven-paragraph summary scope differs')
    author,author_spans=text_with_block_spans(all_author_blocks(candidate))
    if any(p in (2,3) for s in author_spans for p in s['pages']):
        raise ValueError('Contents leaked into default author view')
    for path,value in zip(targets[:2],(layout,repair)):
        json_new(path,value)
    prepare_review_bundles([targets[0]],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'paper_id':old['paper_id'],'characters':len(text),
        'sha256':digest(text.encode()),'author_paragraphs':7,'complete_bullets':4,'literal_repairs':len(operations),
        'source_lines_accounted_once':True,'source_fidelity_approved':False,'ai_receipts_created':0,
        'contents_physical_pages':[2,3]}
    json_new(targets[2],result);print(text,flush=True);print(result,flush=True)


if __name__=='__main__':
    main()
