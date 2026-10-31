"""Conservative discovery of explicit contents pages with dot OR dash leaders.

Candidate classification only. It cannot prove completeness, source absence or
that a page sharing a contents label has no author prose.
"""
import re


def explicit_leader_contents(lines):
    active=[x for x in lines if x['text'].strip() and not x.get('superseded_by_ocr')]
    labels=[x for x in active if re.fullmatch(r'(?:table of )?contents?',x['text'].strip(),re.I)]
    if not labels:
        return None
    leaders=[x for x in active if re.search(r'(?:[.\-]\s*){6,}\s*\d+\s*$',x['text'])]
    if len(leaders)<3:
        return None
    return {'rule':'explicit-dot-or-dash-leader-contents-v1',
            'label_line_ids':[x['line_id'] for x in labels],
            'leader_line_ids':[x['line_id'] for x in leaders],
            'review_status':'machine page classification; complete source boundary review still required'}
