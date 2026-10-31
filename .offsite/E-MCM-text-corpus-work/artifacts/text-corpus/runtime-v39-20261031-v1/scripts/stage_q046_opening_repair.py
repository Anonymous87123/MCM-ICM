"""Stage individually checked abstract/letter/inline body boundaries, create-only."""
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
    root=base/'reflow-20261031-v19';out=base/'reviews/20261031'
    targets=[out/name for name in ('q046-opening-layout-v1.json',
        'q046-opening-word-repairs-v1.json','q046-opening-preflight-v1.json')]
    if any(p.exists() for p in targets):
        raise ValueError('Create-only q46 proof already exists; preserve it')
    catalog=Catalog(root);doc=catalog.document('P-A-2019-1926690-fc36d223')
    pages=rows(root/'papers'/doc['paper_id']/'raw/pages.jsonl')
    findings=out/'q046-opening-findings-v1.json'
    evidence=[{'path':str(findings),'sha256':file_hash(findings),
               'description':'Actually inspected physical pages1–4 for author text and exact boundaries.'}]
    files={}
    for name in ('q046-opening-pages-v1','q046-letter-body-boundary-v1'):
        folder=out/name
        evidence.append({'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
                         'bundle_root':str(folder),'description':'Source-bound physical page raster/native/proxy evidence.'})
        files.update({str(p):file_hash(p) for p in folder.iterdir() if p.is_file()})

    def group(page,name,kind,natives=None,opening=None,ids=None):
        members=[x for x in pages[page-1]['lines'] if x['text'].strip() and not x.get('superseded_by_ocr')
                 and (x['line_id'] in ids if ids is not None else x['native_block'] in natives)]
        if not members:
            raise ValueError('Empty q46 source group')
        return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
                'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason':'Individual page check: retain literal author paragraphs and exact printed section boundaries.',
                **({'opens_section':opening} if opening else {})}

    def inline(role,level,prefix):
        return {'role':role,'level':level,'inline_title_prefix':prefix}

    selected=[{'page':1,'groups':[
        group(1,'p1-form-instructions','front_matter',range(12)),
        group(1,'p1-paper-title','title',[12,13]),
        group(1,'p1-team-date','front_matter',[14,15]),
        group(1,'p1-abstract-label','heading',[16],{'role':'abstract','level':1}),
        *[group(1,f'p1-abstract-paragraph-{n-16}','prose',[n]) for n in range(17,21)]]},
        {'page':2,'groups':[
            group(2,'p2-team-header','furniture',ids=['p0002-n0000-l0000']),
            group(2,'p2-letter-label','heading',opening={'role':'memo','level':1},ids=['p0002-n0000-l0001']),
            *[group(2,f'p2-letter-address-{n}','prose',[n]) for n in range(1,7)],
            *[group(2,f'p2-letter-paragraph-{n-6}','prose',[n]) for n in range(7,12)]]},
        {'page':3,'groups':[
            group(3,'p3-repeated-header','furniture',[0]),
            *[group(3,f'p3-letter-paragraph-{n}','prose',[n]) for n in range(1,5)],
            group(3,'p3-letter-closing','prose',[5]),group(3,'p3-letter-signature','prose',[6])]},
        {'page':4,'groups':[
            group(4,'p4-body-header','furniture',[0]),
            group(4,'p4-introduction-paragraph-1','prose',[1],inline('introduction',1,'1. Introduction')),
            group(4,'p4-introduction-paragraph-2','prose',[2]),
            group(4,'p4-problem-statement','prose',[3],inline('problem_restatement',1,'2. Problem Statement')),
            group(4,'p4-data-paragraph-1','prose',[4],inline('data',1,'3. Data Sources and Modeling Approach')),
            group(4,'p4-data-paragraph-2','prose',[5]),group(4,'p4-data-paragraph-3','prose',[6]),
            group(4,'p4-modeling-heading','heading',[7],{'role':'model','level':1}),
            group(4,'p4-unique-model-characteristics','prose',[8],inline('model',2,'4.1. Unique Model Characteristics')),
            group(4,'p4-gold-nugget-nesting','prose',[9],inline('other',3,'Gold Nugget Nesting and Reproduction'))]}]
    review={'schema':'source-text-layout-review-v1',
        **{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'reviewer':'Codex root;2026-10-31; physical pages1–4 actually inspected',
        'reason':'Separate four-paragraph abstract, full two-page letter and actual inline body headings without losing their first prose sentences.',
        'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':selected,
        'evidence':evidence,'evidence_files':files,
        'remaining_uncertainties':['Page2/page3 letter paragraph still has separate physical fragments; logical join pending.',
            'Inline labels remain literally in the first source paragraph; no text was removed or rewritten.',
            'Pages5 onward and whole-paper source fidelity remain unreviewed.'],
        'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(doc,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(doc,working,[review])
    candidate=make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    candidate['layout_reviews']=applied
    validate_layout_reviews(candidate,pages)
    operations=[]
    for gid,old,new in [('p1-abstract-paragraph-2','i- b','ib'),
                        ('p1-abstract-paragraph-2','- l','-l'),
                        ('p1-abstract-paragraph-4','w- e','we'),
                        ('p4-introduction-paragraph-1','r- s','rs'),
                        ('p4-data-paragraph-1','o- l','ol')]:
        block=next(b for b in candidate['blocks'] if b.get('layout_group_id')==gid)
        if block['text'].count(old)!=1:
            raise ValueError('Checked q46 discretionary break preimage changed: '+gid)
        text=block['text'];replaced=text.replace(old,new)
        operations.append({'block_id':block['block_id'],'operation':'literal_replace','old':old,'new':new,'count':1,
                           'before_text_sha256':digest(text.encode()),'after_text_sha256':digest(replaced.encode()),
                           'reason':'Individually checked printed discretionary line break; preserve lexical hyphen in individual-level.'})
        block['text']=replaced
    # Replay against original candidate bytes; operation preimages are sequential.
    candidate=make_document({k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},working,improved=True)
    candidate['layout_reviews']=applied
    repair={**{k:doc[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
            'reviewer':review['reviewer'],'checked_pages':[1,4],'reason':'Five source-checked word wraps only.',
            'evidence':evidence,'operations':operations,'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(candidate,[repair]);validate_layout_reviews(candidate,pages)
    views={}
    for query in ('abstract','memo','introduction','problem_restatement','data','all_author_text'):
        ids,excluded=select_sections(candidate,query)
        blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text='\n\n'.join(b['text'] for b in blocks)
        views[query]={'characters':len(text),'pages':sorted({p for b in blocks for p in b['source_pages']}),
                      'blocks':len(blocks),'sha256':digest(text.encode())}
        if query=='abstract':
            if (views[query]['pages']!=[1] or len(blocks)!=5 or 'Letter to' in text or
                    not all(s in text for s in ('global distribution','individual-level','However, since dragons'))):
                raise ValueError('Q46 abstract boundary/word restoration differs')
        if query=='memo' and (views[query]['pages']!=[2,3] or '1. Introduction' in text or
                             text.count('Letter to George R.R. Martin')!=1):
            raise ValueError('Q46 letter boundary/header repair differs')
        if query=='introduction' and (views[query]['pages']!=[4] or len(blocks)!=2 or '2. Problem Statement' in text):
            raise ValueError('Q46 inline Introduction lost/misowned')
    source=Counter(x['line_id'] for p in pages for x in p['lines'])
    used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source!=used or any(n!=1 for n in source.values()):
        raise ValueError('Q46 native source line lost or duplicated')
    for target,value in zip(targets[:2],(review,repair)):
        json_new(target,value)
    _,copies=prepare_review_bundles([targets[0]],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'paper_id':doc['paper_id'],'views':views,
            'source_line_accounting':'exactly once','word_wrap_repairs':len(operations),
            'portable_layout_evidence_files':len(copies),'source_fidelity_approved':False,
            'cross_page_logical_join':'pending','ai_processing_receipts_created':0}
    json_new(targets[2],result);print(result,flush=True)


if __name__=='__main__':
    main()
