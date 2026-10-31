"""Individually checked technical/operational summaries, including addi-/tion."""
from collections import Counter
from pathlib import Path

from corpus_reader import Catalog
from corpus_queries import select_sections,selected_blocks
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_paragraph_reviews import apply_paragraph_reviews,validate_paragraph_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest,encoded,file_hash,json_new,make_document,rows,text_with_block_spans


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    root=base/'reflow-20261031-v23';out=base/'reviews/20261031'
    targets=[out/f'q088-opening-{name}-v1.json' for name in ('layout','word-repairs','paragraph','preflight')]
    existing=all(p.exists() for p in targets[:3])
    if targets[3].exists() or (any(p.exists() for p in targets[:3]) and not existing):
        raise ValueError('Completed or partial q88 proof exists; preserve it')
    catalog=Catalog(root);old=catalog.document('P-B-2010-8362-bd23db32')
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    folder=out/'q088-opening-pages-v1';findings=out/'q088-opening-findings-v1.json'
    evidence=[{'path':str(findings),'sha256':file_hash(findings),'description':'Individual physical-page prose and boundary findings.'},
        {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
         'bundle_root':str(folder),'description':'Five individually inspected bounded JPEG/native physical pages.'}]
    files={str(p):file_hash(p) for p in folder.iterdir() if p.is_file()};files[str(findings)]=file_hash(findings)
    def group(page,name,kind,natives,opening=None):
        members=[x for x in pages[page-1]['lines'] if x['text'].strip() and x['native_block'] in natives]
        return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
            'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
            'reason':'Literal source ownership and printed paragraph indentation checked on this physical page.',
            **({'opens_section':opening} if opening else {})}
    groups={1:[group(1,'p1-title','title',[0]),group(1,'p1-control-date','front_matter',[1,2]),
               group(1,'p1-page','furniture',[3])],
        2:[group(2,'p2-header','furniture',[0]),
           group(2,'p2-summary-title','heading',[1],{'role':'abstract','level':1}),
           *[group(2,f'p2-paragraph-{n-1}','prose',[n]) for n in (2,3,4)]],
        3:[group(3,'p3-header','furniture',[0]),
           group(3,'p3-executive-title','heading',[1],{'role':'abstract','level':1}),
           group(3,'p3-salutation','prose',[2]),
           group(3,'p3-paragraph-1','prose',range(3,6)),
           group(3,'p3-paragraph-2','prose',range(6,15)),
           group(3,'p3-paragraph-3','prose',range(15,20)),
           group(3,'p3-paragraph-4','prose',range(20,24)),
           group(3,'p3-paragraph-5a','prose',[24])],
        4:[group(4,'p4-header','furniture',[0]),
           group(4,'p4-paragraph-5b','prose',range(1,9)),
           group(4,'p4-paragraph-6','prose',range(9,16)),
           group(4,'p4-paragraph-7','prose',range(16,24)),
           group(4,'p4-closing','prose',[24])]}
    meta={k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
    layout={'schema':'source-text-layout-review-v1',**meta,'reviewer':'Codex root;2026-10-31; physical pages1–5',
        'reason':'Separate title/form/header text and restore complete literal Summary Statement and two-page Executive Summary.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
        'pages':[{'page':p,'groups':g} for p,g in groups.items()],
        'evidence':evidence,'evidence_files':files,'source_fidelity_approved':False,
        'remaining_uncertainties':['Later source pages6–33 and full-paper chapter mapping remain unreviewed.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[layout]);candidate=make_document(meta,working,improved=True)
    candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
    operations=[]
    for gid,pairs in {'p3-paragraph-2':[('a- t','at'),('oﬀin','oﬀ in')],
                      'p3-paragraph-5a':[('addi-','addi')],
                      'p4-paragraph-6':[('n- n','nn'),('m- p','mp')]}.items():
        block=next(b for b in candidate['blocks'] if b.get('layout_group_id')==gid);text=block['text']
        for before,after in pairs:
            if text.count(before)!=1:
                raise ValueError('Exact checked literal preimage differs: '+gid+' '+before)
            changed=text.replace(before,after)
            operations.append({'block_id':block['block_id'],'operation':'literal_replace','old':before,'new':after,
                'count':1,'before_text_sha256':digest(text.encode()),'after_text_sha256':digest(changed.encode()),
                'reason':'Exact source-checked physical word wrap or missing prose space; preserve author wording.'})
            text=changed
    repair={**meta,'reviewer':layout['reviewer'],'reason':'Five literal source transcription operations; no paraphrase.',
        'checked_pages':[1,2,3,4,5],'operations':operations,'evidence':evidence,
        'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(candidate,[repair])
    left=next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p3-paragraph-5a')
    right=next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p4-paragraph-5b')
    join={'schema':'source-paragraph-join-review-v1',**meta,'reviewer':layout['reviewer'],
        'reason':'Source page3 ends addi- and page4 starts tion; same printed paragraph.',
        'checked_pages':[3,4],'evidence':evidence,'evidence_files':files,
        'joins':[{'left_block_id':left['block_id'],'right_block_id':right['block_id'],
            'separator':'','discretionary_wrap_word':'addition',
            'left_text_sha256':digest(left['text'].encode()),'right_text_sha256':digest(right['text'].encode()),
            'reason':'Only the already source-repaired terminal discretionary hyphen is removed; join the two source fragments without a space.'}],
        'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    apply_paragraph_reviews(candidate,[join]);validate_paragraph_reviews(candidate);validate_layout_reviews(candidate,pages)
    source=Counter(x['line_id'] for p in pages for x in p['lines'])
    used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source!=used or any(n!=1 for n in used.values()):
        raise ValueError('Source line lost or duplicated')
    results={}
    for title,expected_pages,paragraphs in [('Summary Statement',{2},3),('Executive Summary',{3,4},9)]:
        ids,excluded=select_sections(candidate,title,exact_title=True)
        blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text,spans=text_with_block_spans(blocks)
        fragments=sum(b['kind']!='heading' for b in blocks)
        continuations=sum(bool(b.get('paragraph_continues_from')) for b in blocks)
        if ({p for s in spans for p in s['pages']}!=expected_pages or fragments-continuations!=paragraphs or
                'Control #' in text or 'February 22' in text or 'Contents' in text):
            raise ValueError('Checked paragraph ownership differs: '+title)
        if title=='Executive Summary' and ('In addition to the aforementioned' not in text or
                not text.endswith('We wish you luck in your investigations.') or 'loca- tions' in text or 'oﬀin' in text):
            raise ValueError('Executive summary continuation/ending not restored')
        for span,block in zip(spans,blocks):
            if text[span['start']:span['end']]!=block['text']:
                raise ValueError('Literal block/source offsets changed')
        results[title]={'characters':len(text),'sha256':digest(text.encode()),'logical_author_paragraphs':paragraphs,
                        'source_fragments':fragments,'physical_pages':sorted(expected_pages)}
        print(title,text,sep='\n',flush=True)
    ids,excluded=select_sections(candidate,'abstract')
    abstract,spans=text_with_block_spans(selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)}))
    if 'Following the Trail' in abstract or {p for s in spans for p in s['pages']}!={2,3,4}:
        raise ValueError('Normalized abstract union has wrong scope')
    for path,value in zip(targets[:3],(layout,repair,join)):
        if existing:
            if path.read_bytes()!=encoded(value):
                raise ValueError('Existing proof differs; never overwrite it')
        else:
            json_new(path,value)
    # Layout and paragraph reviews have different registries, each keyed by
    # paper. Check them separately, as the corpus builder does.
    for path in (targets[0],targets[2]):
        prepare_review_bundles([path],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'paper_id':old['paper_id'],'results':results,
        'abstract_characters':len(abstract),'abstract_sha256':digest(abstract.encode()),
        'literal_repairs':len(operations),'source_lines_accounted_once':True,
        'source_fidelity_approved':False,'ai_receipts_created':0,'existing_proof_bytes_reused':existing}
    json_new(targets[3],result);print(result,flush=True)


if __name__=='__main__':
    main()
