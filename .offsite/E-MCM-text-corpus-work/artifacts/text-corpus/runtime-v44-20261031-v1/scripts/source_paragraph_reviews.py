"""Source-checked paragraph links; source-repaired block bytes stay unchanged."""
import re
from text_corpus import digest, encoded


def checked_separator(document, a, b, item):
    separator=item.get('separator')
    if separator==' ' and 'discretionary_wrap_word' not in item:
        return separator
    if separator!='':
        raise ValueError('Paragraph separator requires a checked space or word wrap')
    left=re.search(r'([^\W\d_]+)$',a['text']);right=re.match(r'([^\W\d_]+)',b['text'])
    if not left or not right or item.get('discretionary_wrap_word')!=left[1]+right[1]:
        raise ValueError('Discretionary page wrap lacks the exact source word')
    # An empty separator is permitted only after a separately logged terminal
    # hyphen removal. Preserve both source fragments and their exact offsets;
    # never infer a word join from lowercase text or page position alone.
    for review in document.get('text_repair_reviews',[]):
        for op in review.get('operations',[]):
            old,new=op.get('old'),op.get('new')
            if (op.get('block_id')==a['block_id'] and op.get('operation')=='literal_replace' and
                    isinstance(old,str) and isinstance(new,str) and new and old==new+'-' and
                    op.get('count')==1 and a['text'].endswith(new) and
                    op.get('after_text_sha256')==digest(a['text'].encode()) and
                    op.get('before_text_sha256')==digest((a['text'][:-len(new)]+old).encode())):
                return separator
    raise ValueError('Discretionary page wrap lacks logged terminal hyphen repair')


def checked_links(document, review):
    if (review.get('schema')!='source-paragraph-join-review-v1' or
            any(review.get(k)!=document[k] for k in ('paper_id','source_sha256','raw_pages_sha256')) or
            not review.get('reviewer') or not review.get('reason') or not review.get('evidence_files') or
            not review.get('evidence') or not review.get('joins')):
        raise ValueError('Incomplete or stale paragraph join review')
    blocks=document['blocks'];positions={b['block_id']:i for i,b in enumerate(blocks)}
    checked=set(review.get('checked_pages',[]));result=[]
    for item in review['joins']:
        left=positions.get(item.get('left_block_id'));right=positions.get(item.get('right_block_id'))
        if left is None or right is None or left>=right:
            raise ValueError('Paragraph join block order invalid')
        a,b=blocks[left],blocks[right]
        if (a['kind'] not in {'prose','mixed'} or b['kind'] not in {'prose','mixed'} or
                a['section_id']!=b['section_id'] or a['source_pages'][-1]+1!=b['source_pages'][0] or
                not set(a['source_pages']+b['source_pages'])<=checked or not item.get('reason') or
                not a['text'] or not b['text'] or
                digest(a['text'].encode())!=item.get('left_text_sha256') or
                digest(b['text'].encode())!=item.get('right_text_sha256') or
                any(x['kind']!='furniture' for x in blocks[left+1:right])):
            raise ValueError('Paragraph join lacks exact consecutive source coverage')
        result.append((a,b,checked_separator(document,a,b,item)))
    return result


def apply_paragraph_reviews(document,reviews):
    for review in reviews:
        if review.get('paper_id')!=document['paper_id']:
            continue
        pairs=checked_links(document,review);rid=digest(encoded(review))
        for a,b,separator in pairs:
            if b.get('paragraph_continues_from') or any(x.get('paragraph_continues_from')==a['block_id'] for x in document['blocks']):
                raise ValueError('Duplicate or branching paragraph join')
            b['paragraph_continues_from']=a['block_id'];b['paragraph_join_review_sha256']=rid
            if separator!=' ':
                b['paragraph_join_separator']=separator
            for defect in document.get('defects',[]):
                if (defect['code']=='cross_page_join_review' and defect.get('left')==a['block_id'] and
                        defect.get('right')==b['block_id']):
                    defect.update(status='resolved',resolution='source-checked logical paragraph continuation',
                                  paragraph_join_review_sha256=rid)
        document.setdefault('paragraph_join_reviews',[]).append(review)


def validate_paragraph_reviews(document):
    expected={};outgoing=set()
    for review in document.get('paragraph_join_reviews',[]):
        rid=digest(encoded(review))
        for a,b,separator in checked_links(document,review):
            if b['block_id'] in expected or a['block_id'] in outgoing:
                raise ValueError('Duplicate or branching paragraph join proof')
            outgoing.add(a['block_id']);expected[b['block_id']]=(a['block_id'],rid,separator)
    actual={b['block_id']:(b.get('paragraph_continues_from'),b.get('paragraph_join_review_sha256'),
                           b.get('paragraph_join_separator',' '))
            for b in document['blocks'] if any(k in b for k in
                ('paragraph_continues_from','paragraph_join_review_sha256','paragraph_join_separator'))}
    if actual!=expected:
        raise ValueError('Paragraph continuation differs from source proofs')
