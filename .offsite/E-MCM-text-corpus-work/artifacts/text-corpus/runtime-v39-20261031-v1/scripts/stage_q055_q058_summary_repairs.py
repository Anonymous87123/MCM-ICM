"""Two individually checked page layouts; no corpus-wide paragraph guesses."""
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
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus';root=base/'reflow-20261031-v21'
    out=base/'reviews/20261031';report=out/'q055-q058-summary-preflight-v1.json'
    targets=[out/f'q{q:03d}-summary-{suffix}-v1.json' for q in (55,58) for suffix in ('layout','word-repairs')]
    if report.exists() or any(p.exists() for p in targets):
        raise ValueError('Create-only source proof exists; preserve it')
    catalog=Catalog(root);results=[]
    for queue,pid,start,end,title_natives,summary_native,keyword_native,qr_start,changes in [
        (55,'P-A-2021-2100454-dc37ed6a',12,19,[9,10],11,19,20,
         {2:[('x- p','xp'),('t- i','ti'),('x- t','xt')],3:[('i- m','im')],
          4:[('m- p','mp')],5:[('m- p','mp'),('r- e','re'),('j´a','já')],7:[('t- n','tn')]}),
        (58,'P-A-2021-2110178-2aed1e20',11,17,[9],10,17,18,
         {2:[('i- f','i-f')],3:[('g- t','g-t')],4:[('n- s','ns'),('n- m','nm')],
          5:[('i- n','in'),('i- r','ir')]})]:
        old=catalog.document(pid);pages=rows(root/'papers'/pid/'raw/pages.jsonl')
        findings=out/f'q{queue:03d}-summary-findings-v1.json';evidence=[{
            'path':str(findings),'sha256':file_hash(findings),'description':'Individual literal source findings and remaining limits.'}]
        files={str(findings):file_hash(findings)}
        for folder in (out/f'q{queue:03d}-summary-page-v1',out/f'q{queue:03d}-summary-end-v1'):
            evidence.append({'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
                'bundle_root':str(folder),'description':'Actually inspected bounded source page or next-page boundary evidence.'})
            files.update({str(p):file_hash(p) for p in folder.iterdir() if p.is_file()})
        def group(name,kind,natives,opening=None,exclude=(),only=None):
            members=[x for x in pages[0]['lines'] if x['text'].strip() and x['native_block'] in natives
                and x['line_id'] not in exclude and (only is None or x['line_id'] in only)]
            return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
                'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason':'Explicit paragraph and source-text ownership checked on this individual page.',
                **({'opens_section':opening} if opening else {})}
        summary=['p0001-n0006-l0002']
        groups=[group('p1-form','front_matter',range(4,9),exclude=summary),
            group('p1-summary-sheet','heading',[6],{'role':'abstract','level':1},only=summary),
            group('p1-paper-title','title',title_natives),
            group('p1-summary-label','heading',[summary_native],{'role':'abstract','level':1}),
            *[group(f'p1-paragraph-{n-start+1}','prose',[n]) for n in range(start,end)],
            group('p1-keywords','keywords',[keyword_native]),
            group('p1-watermark-and-promotion','furniture',[*range(4),*range(qr_start,qr_start+4)])]
        meta={k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
        layout={'schema':'source-text-layout-review-v1',**meta,'reviewer':'Codex root;2026-10-31; physical pages1and2',
            'reason':'Restore each printed summary paragraph and literal inline lead-in; retain all non-body text separately.',
            'paragraph_boundaries_checked':True,'reading_lanes_checked':True,'pages':[{'page':1,'groups':groups}],
            'evidence':evidence,'evidence_files':files,'source_fidelity_approved':False,
            'remaining_uncertainties':['Later paper body unreviewed; no whole-paper acceptance.'],
            'formula_verification':'paused','figure_distillation':'paused'}
        working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
        applied=apply_layout_reviews(old,working,[layout]);candidate=make_document(meta,working,improved=True)
        candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
        operations=[]
        for number,pairs in changes.items():
            block=next(b for b in candidate['blocks'] if b.get('layout_group_id')==f'p1-paragraph-{number}')
            text=block['text']
            for before,after in pairs:
                if text.count(before)!=1:
                    raise ValueError(f'Checked q{queue} paragraph{number} literal differs: '+before)
                updated=text.replace(before,after)
                operations.append({'block_id':block['block_id'],'operation':'literal_replace','old':before,'new':after,
                    'count':1,'before_text_sha256':digest(text.encode()),'after_text_sha256':digest(updated.encode()),
                    'reason':'Exact source-checked discretionary wrap, retained lexical hyphen or printed city accent.'})
                text=updated
        repair={**meta,'reviewer':layout['reviewer'],'reason':'Individual literal text transcription only; no author grammar edits.',
            'checked_pages':[1,2],'operations':operations,'evidence':evidence,'source_fidelity_approved':False,
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
        if ({p for s in spans for p in s['pages']}!={1} or sum(b['kind']!='heading' for b in blocks)!=end-start or
                'MCM/ICM' in text or 'Keywords:' in text or '关注' in text):
            raise ValueError('Individual checked summary paragraph/ownership differs')
        if queue==55 and 'different fungi and their effect' not in text:
            raise ValueError('Checked GAME sentence still split')
        if queue==58 and 'a multi-fungi decomposition model' not in text:
            raise ValueError('Checked ModelI continuation still split')
        layout_path=out/f'q{queue:03d}-summary-layout-v1.json'
        json_new(layout_path,layout);json_new(out/f'q{queue:03d}-summary-word-repairs-v1.json',repair)
        prepare_review_bundles([layout_path],identity_fields=('paper_id',),application_status='preflight only')
        results.append({'queue':queue,'paper_id':pid,'characters':len(text),'author_paragraphs':end-start,
            'text_sha256':digest(text.encode()),'literal_repairs':len(operations),'source_lines_accounted_once':True,
            'source_fidelity_approved':False,'ai_receipts_created':0})
        print({'queue':queue,'text':text},flush=True)
    result={'parent_dataset_id':catalog.identity,'results':results,'old_files_overwritten':0}
    json_new(report,result);print(result,flush=True)


if __name__=='__main__':
    main()
