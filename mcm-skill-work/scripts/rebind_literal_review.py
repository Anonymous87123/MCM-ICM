"""Rebind unchanged reviewed prose using exact source lines and literal bytes.

This transfers an existing, bounded source proof to new block IDs only. A changed
paragraph, line order, kind, source or operation fails; it never approves new text.
"""
from __future__ import annotations
import copy
from collections import defaultdict
from source_text_repairs import apply_text_repairs,check_review,operation
from text_corpus import digest,encoded


def rebind(previous,candidate,review):
    check_review(previous,review)
    for key in ('paper_id','source_sha256','raw_pages_sha256'):
        if previous[key]!=candidate[key]:
            raise ValueError('Literal review source identity changed')
    old_blocks={b['block_id']:b for b in previous['blocks']}
    by_lines=defaultdict(list)
    for block in candidate['blocks']:
        by_lines[tuple(block['source_line_ids'])].append(block)
    grouped=defaultdict(list)
    for op in review['operations']:
        grouped[op['block_id']].append(op)
    binding={}
    for old_id,ops in grouped.items():
        old=old_blocks[old_id];matches=by_lines[tuple(old['source_line_ids'])]
        if len(matches)!=1:
            raise ValueError('Reviewed paragraph source-line chain changed or is ambiguous')
        new=matches[0]
        if old['source_pages']!=new['source_pages'] or old.get('pre_repair_kind',old['kind'])!=new['kind']:
            raise ValueError('Reviewed paragraph location/classification changed')
        text,kind=new['text'],new['kind']
        for op in ops:
            text,kind=operation(text,kind,op)
        if text!=old['text'] or kind!=old['kind']:
            raise ValueError('Reviewed paragraph postimage changed')
        binding[old_id]={'old_block_id':old_id,'new_block_id':new['block_id'],
            'source_line_ids':old['source_line_ids'],'source_pages':old['source_pages'],
            'before_text_sha256':digest(new['text'].encode()),'after_text_sha256':digest(text.encode())}
    result=copy.deepcopy(review)
    for op in result['operations']:
        op['block_id']=binding[op['block_id']]['new_block_id']
    result['binding_transfer']={'schema':'exact-literal-review-rebinding-v1',
        'previous_review_sha256':digest(encoded(review)),
        'paragraphs':list(binding.values()),'new_source_review':False,
        'meaning':'Same ordered native lines, literal pre/postimages and source evidence; only block identifiers changed.'}
    apply_text_repairs(copy.deepcopy(candidate),[result])
    return result
