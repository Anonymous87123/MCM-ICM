"""Source-checked restoration of three distinct summary pages, create-only."""
import copy
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
    base=Path(__file__).resolve().parents[1]/'artifacts/text-corpus';root=base/'reflow-20261031-v19'
    out=base/'reviews/20261031';catalog=Catalog(root);results=[]
    targets=[out/name for name in ('q047-summary-repair-v1.json','q048-summary-repair-v1.json',
        'q049-summary-layout-v1.json','q047-q048-q049-preflight-v1.json')]
    if any(p.exists() for p in targets):
        raise ValueError('Create-only source proof exists; preserve it')
    for queue,pid in [(47,'P-A-2020-2001334-a7774d36'),(48,'P-A-2020-2002354-f00d018f'),
                      (49,'P-A-2020-2003298-d28634b8')]:
        old=catalog.document(pid);folder=out/f'q{queue:03d}-summary-page-v1'
        findings=out/f'q{queue:03d}-summary-findings-v1.json'
        evidence=[{'path':str(findings),'sha256':file_hash(findings),'description':'Actual individual source-page findings.'},
                  {'path':str(folder/'manifest.json'),'sha256':file_hash(folder/'manifest.json'),
                   'bundle_root':str(folder),'description':'Actually inspected bounded source page/native evidence.'}]
        files={str(p):file_hash(p) for p in folder.iterdir() if p.is_file()};files[str(findings)]=file_hash(findings)
        meta={k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
        if queue in (47,48):
            candidate=copy.deepcopy(old);ops=[]
            for text,kind in [('MCM/ICM','front_matter'),('关注数学模型','furniture')]:
                matches=[b for b in candidate['blocks'] if b['source_pages']==[1] and b['text']==text]
                if len(matches)!=1 or matches[0]['kind']!='prose':
                    raise ValueError('Exact source banner/promotion preimage changed')
                block=matches[0];sha=digest(block['text'].encode())
                ops.append({'block_id':block['block_id'],'operation':'classify','from_kind':'prose','to_kind':kind,
                            'before_text_sha256':sha,'after_text_sha256':sha,
                            'reason':'Source-confirmed competition banner or separate QR promotion; no source bytes removed.'})
            if queue==47:
                block=next(b for b in candidate['blocks'] if b['block_id']=='b000015')
                if block['text'].count('u- t')!=1:
                    raise ValueError('Checked q47 distribution preimage changed')
                ops.append({'block_id':block['block_id'],'operation':'literal_replace','old':'u- t','new':'ut','count':1,
                            'before_text_sha256':digest(block['text'].encode()),
                            'after_text_sha256':digest(block['text'].replace('u- t','ut').encode()),
                            'reason':'Source-checked printed distribu-/tion word wrap only.'})
            proof={**meta,'reviewer':'Codex root;2026-10-31; actual individual page1 inspection',
                   'checked_pages':[1],'reason':'Retain complete author paragraphs and separately store form/promotional text.',
                   'evidence':evidence,'operations':ops,'source_fidelity_approved':False,
                   'formula_verification':'paused','figure_distillation':'paused'}
            apply_text_repairs(candidate,[proof]);target=targets[queue-47]
        else:
            pages=rows(root/'papers'/pid/'raw/pages.jsonl');page=pages[0]
            def group(name,kind,natives,opening=None,exclude=(),only=None):
                members=[x for x in page['lines'] if x['text'].strip() and x['native_block'] in natives
                         and x['line_id'] not in exclude and (only is None or x['line_id'] in only)]
                return {'group_id':name,'kind':kind,'source_line_ids':[x['line_id'] for x in members],
                        'text_sha256':digest(' '.join(x['text'].strip() for x in members).encode()),
                        'reason':'Physical page1 checked; source title, paragraphs and QR material have separate ownership.',
                        **({'opens_section':opening} if opening else {})}
            summary=['p0001-n0007-l0002']
            groups=[group('p1-form','front_matter',range(5,10),exclude=summary),
                    group('p1-summary-sheet','heading',[7],{'role':'abstract','level':1},only=summary),
                    group('p1-paper-title','title',[10]),
                    *[group(f'p1-summary-paragraph-{n-10}','prose',[n]) for n in range(11,17)],
                    group('p1-keywords','keywords',[17]),group('p1-qr-promotion','furniture',range(4))]
            proof={'schema':'source-text-layout-review-v1',**meta,
                   'reviewer':'Codex root;2026-10-31; physical page1 actually inspected',
                   'reason':'Preserve six complete summary paragraphs; separate the printed title/form/keywords/promotion.',
                   'paragraph_boundaries_checked':True,'reading_lanes_checked':True,
                   'pages':[{'page':1,'groups':groups}],'evidence':evidence,'evidence_files':files,
                   'source_fidelity_approved':False,
                   'remaining_uncertainties':['Next-page boundary and all later prose unreviewed.'],
                   'formula_verification':'paused','figure_distillation':'paused'}
            working,_=prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
            applied=apply_layout_reviews(old,working,[proof]);candidate=make_document(meta,working,improved=True)
            candidate['layout_reviews']=applied;validate_layout_reviews(candidate,pages)
            source=Counter(x['line_id'] for p in pages for x in p['lines'])
            used=Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
            used.update(x['line_id'] for x in candidate['excluded_source_lines'])
            if used!=source or any(n!=1 for n in used.values()):
                raise ValueError('Q49 source line lost or duplicated')
            target=targets[2]
        ids,excluded=select_sections(candidate,'abstract')
        blocks=selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text,spans=text_with_block_spans(blocks)
        if ('关注数学模型' in text or 'MCM/ICM' in text or
                any(b['source_pages']!=[1] for b in blocks) or
                len([b for b in blocks if b['kind']!='heading'])!={47:6,48:8,49:6}[queue] or
                (queue==49 and 'Keeping up with the Migrating Fish' in text)):
            raise ValueError('Checked summary paragraph/ownership restoration differs')
        json_new(target,proof)
        if queue==49:
            prepare_review_bundles([target],identity_fields=('paper_id',),application_status='preflight only')
        results.append({'queue':queue,'paper_id':pid,'abstract_characters':len(text),
                        'author_paragraphs':sum(b['kind']!='heading' for b in blocks),'abstract_text_sha256':digest(text.encode()),
                        'source_fidelity_approved':False,'ai_processing_receipts_created':0})
    result={'parent_dataset_id':catalog.identity,'results':results,'old_files_overwritten':0}
    json_new(targets[3],result);print(result,flush=True)


if __name__=='__main__':
    main()
