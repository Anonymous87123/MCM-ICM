"""Literal source-checked summary/newspaper restoration, preserving all evidence."""
from collections import Counter
from pathlib import Path

from corpus_reader import Catalog
from corpus_queries import select_sections,selected_blocks
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest,file_hash,json_new,make_document,rows,text_with_block_spans


def main():
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus'
    root=base/'reflow-20261031-v21';out=base/'reviews/20261031'
    targets=[out/name for name in ('q053-opening-layout-v1.json','q053-opening-word-repairs-v1.json','q053-opening-preflight-v1.json')]
    if any(p.exists() for p in targets):
        raise ValueError('Create-only proof exists; preserve it')
    catalog=Catalog(root);old=catalog.document('P-A-2020-2017785-c87378f9')
    pages=rows(root/'papers'/old['paper_id']/'raw/pages.jsonl')
    folder=out/'q053-opening-pages-v1';findings=out/'q053-opening-findings-v1.json'
    evidence=[{'path':str(findings),'sha256':file_hash(findings),'description':'Actually checked individual source-page findings.'},
              {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
               'bundle_root':str(folder),'description':'Three physically checked bounded JPEG/native evidence pages.'}]
    files={str(p):file_hash(p) for p in folder.iterdir() if p.is_file()};files[str(findings)]=file_hash(findings)
    def group(page,name,kind,natives,opening=None,exclude=(),only=None):
        members=[x for x in pages[page-1]['lines'] if x['text'].strip() and x['native_block'] in natives
                 and x['line_id'] not in exclude and (only is None or x['line_id'] in only)]
        return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
                'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason':'Individual source-page paragraph, column-continuation and text ownership check.',
                **({'opens_section':opening} if opening else {})}
    summary=['p0001-n0006-l0002']
    groups1=[group(1,'p1-form','front_matter',range(4,9),exclude=summary),
             group(1,'p1-summary','heading',[6],{'role':'abstract','level':1},only=summary),
             *[group(1,f'p1-paragraph-{n-8}','prose',[n]) for n in range(9,16)],
             group(1,'p1-promotion','furniture',range(4))]
    groups2=[group(2,'p2-masthead','front_matter',range(4,8)),
             group(2,'p2-newspaper-title','heading',[8],{'role':'other','level':1}),
             group(2,'p2-byline','front_matter',[9]),
             group(2,'p2-opening-paragraph','prose',[10]),
             group(2,'p2-image-caption','caption',[11]),
             group(2,'p2-cross-column-paragraph','prose',[12,13]),
             group(2,'p2-territorial-paragraph','prose',[14]),
             group(2,'p2-strategy-opening','prose',[15]),
             *[group(2,f'p2-strategy-{n-15}','list',[n]) for n in range(16,20)],
             group(2,'p2-closing-paragraph','prose',[20]),
             group(2,'p2-promotion','furniture',range(4))]
    meta={k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
    layout={'schema':'source-text-layout-review-v1',**meta,'reviewer':'Codex root;2026-10-31; individual physical pages1–3',
            'reason':'Separate seven-paragraph summary from complete two-column handout; preserve four strategies and all other text.',
            'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
            'pages':[{'page':1,'groups':groups1},{'page':2,'groups':groups2}],
            'evidence':evidence,'evidence_files':files,'source_fidelity_approved':False,
            'remaining_uncertainties':['Later body unreviewed; handout role other pending semantic category mapping.'],
            'formula_verification':'paused','figure_distillation':'paused'}
    working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied=apply_layout_reviews(old,working,[layout]);candidate=make_document(meta,working,improved=True)
    candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
    operations=[]
    replacements={'p1-paragraph-2':[('e- g','eg')],
        'p2-opening-paragraph':[('r- a','ra')],
        'p2-cross-column-paragraph':[('o퐶in','°C in'),('e- g','eg')],
        'p2-strategy-opening':[('r- t','rt')],
        'p2-strategy-1':[('ﬁsh- ing','ﬁshing'),('m- p','mp')],
        'p2-strategy-2':[('r- v','rv')],
        'p2-strategy-4':[('a- p','ap')]}
    for gid,changes in replacements.items():
        block=next(b for b in candidate['blocks'] if b.get('layout_group_id')==gid)
        text=block['text']
        for old_text,new_text in changes:
            if text.count(old_text)!=1:
                raise ValueError('Source-checked short preimage differs: '+gid+' '+old_text)
            updated=text.replace(old_text,new_text)
            operations.append({'block_id':block['block_id'],'operation':'literal_replace','old':old_text,'new':new_text,'count':1,
                'before_text_sha256':digest(text.encode()),'after_text_sha256':digest(updated.encode()),
                'reason':'Literal individually checked source word wrap or prose unit glyph/spacing; no paraphrase.'})
            text=updated
    repair={**meta,'reviewer':layout['reviewer'],'reason':'Restore only individually checked printed prose word wraps and unit glyph.',
            'checked_pages':[1,2,3],'operations':operations,'evidence':evidence,
            'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(candidate,[repair]);validate_layout_reviews(candidate,pages)
    source=Counter(x['line_id'] for p in pages for x in p['lines'])
    used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source!=used or any(n!=1 for n in used.values()):
        raise ValueError('Source line lost or duplicated')
    results={}
    for query,expected_pages,count in [('abstract',{1},7),('A Fishy Situation',{2},9)]:
        ids,excluded=select_sections(candidate,query,exact_title=query!='abstract')
        blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text,spans=text_with_block_spans(blocks)
        author=[b for b in blocks if b['kind']!='heading']
        if ({p for s in spans for p in s['pages']}!=expected_pages or len(author)!=count or
                '$1.00' in text or 'Projected herring distribution' in text or 'MCM/ICM' in text):
            raise ValueError('Checked paragraph/ownership contract differs: '+query)
        if query!='abstract' and ('losing access to the herring' not in text or
                not text.endswith('Take action now!') or sum(b['kind']=='list' for b in blocks)!=4):
            raise ValueError('Newspaper continuation/four strategies/ending incomplete')
        results[query]={'characters':len(text),'author_paragraphs_and_items':len(author),'sha256':digest(text.encode())}
        print(query,text,sep='\n',flush=True)
    json_new(targets[0],layout);json_new(targets[1],repair)
    prepare_review_bundles([targets[0]],identity_fields=('paper_id',),application_status='preflight only')
    result={'parent_dataset_id':catalog.identity,'paper_id':old['paper_id'],'results':results,'operations':len(operations),
            'source_lines_accounted_once':True,'source_fidelity_approved':False,'ai_receipts_created':0}
    json_new(targets[2],result);print(result,flush=True)


if __name__=='__main__':
    main()
