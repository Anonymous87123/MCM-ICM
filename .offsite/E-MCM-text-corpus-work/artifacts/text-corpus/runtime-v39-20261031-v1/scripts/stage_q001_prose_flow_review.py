"""Freeze the actually checked page5 prose repair; never approve other pages."""
from pathlib import Path
from corpus_reader import Catalog
from source_text_repairs import apply_text_repairs
from text_corpus import digest,file_hash,json_new,make_document,rows


def main():
    work=Path(__file__).resolve().parents[1]
    root=work/'artifacts/text-corpus/reflow-20261030-v10'
    catalog=Catalog(root)
    old=catalog.document('P-A-2010-6749-395f556a')
    meta={k:old[k] for k in ('paper_id','problem_type','year','queue_position','page_count',
                            'source_relative_path','source_sha256','raw_pages_sha256')}
    doc=make_document(meta,rows(root/'papers'/old['paper_id']/'raw/pages.jsonl'),improved=True)
    paragraphs=[b for b in doc['blocks'] if b['source_pages']==[5] and b['kind']=='prose']
    expected=('To find out the','Then we build','To predict and compare')
    if len(paragraphs)!=3 or any(not b['text'].startswith(prefix) for b,prefix in zip(paragraphs,expected)):
        raise ValueError('Checked page no longer has its three original paragraphs')
    ops=[]
    for block,count in zip(paragraphs,(1,1,2)):
        before=block['text'];oldglyph='𝐵𝐵𝐵𝐵𝐵𝐵'
        if before.count(oldglyph)!=count:
            raise ValueError('Abbreviation transcription preimage changed')
        ops.append({'operation':'literal_replace','block_id':block['block_id'],
            'before_text_sha256':digest(before.encode()),'after_text_sha256':digest(before.replace(oldglyph,'BBS').encode()),
            'old':oldglyph,'new':'BBS','count':count,
            'reason':'Actually read page5 proxy prints the ordinary abbreviation BBS in these four prose occurrences; retain author grammar and all surrounding words.'})
    folder=Path('artifacts/text-corpus/source-reviews/q001-prose-flow-20261030-v1')
    review={**{k:old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')},
        'checked_pages':[5],'reviewer':'Codex root;2026-10-30;page5 bounded JPEG and all three prospective prose paragraphs actually compared',
        'reason':'Recover the printed BBS abbreviation and source prose order only; no formula correctness or chart interpretation.',
        'operations':ops,'evidence':[{'path':str(folder/name).replace('\\','/'),'sha256':file_hash(work/folder/name),
            'description':'Source-bound page5 '+name} for name in ('manifest.json','page-0005.jpg')],
        'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(doc,[review])
    json_new(work/'artifacts/text-corpus/reviews/20261030/q001-page5-prose-transcription-v1.json',review)
    json_new(work/'artifacts/text-corpus/reviews/20261030/q001-page5-prose-order-v1.json',{
        'paper_id':old['paper_id'],'source_sha256':old['source_sha256'],'raw_pages_sha256':old['raw_pages_sha256'],
        'checked_pages':[5],'source_order_checked':True,'source_paragraph_count':3,
        'blocks':[{'block_id':b['block_id'],'source_line_ids':b['source_line_ids'],'text_sha256':digest(b['text'].encode())} for b in paragraphs],
        'scope':'Only page5 surrounding prose order and three paragraph boundaries actually compared. Other222 whole-paper inferred line boxes remain unverified. No whole-section or whole-paper approval.',
        'evidence':review['evidence'],'formula_verification':'paused','figure_distillation':'paused'})
    print({'staged_literal_operations':len(ops),'checked_page':5,'whole_paper_accepted':False})


if __name__=='__main__':
    main()
