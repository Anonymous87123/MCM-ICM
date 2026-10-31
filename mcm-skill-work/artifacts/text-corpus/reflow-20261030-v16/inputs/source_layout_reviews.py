"""Source-bound explicit text lanes for exceptional prose/sidebar layouts."""
from __future__ import annotations

from collections import Counter

from text_corpus import ROLES, digest, encoded, title_role


def check_layout_review(document, pages, review):
    if (review.get("schema") != "source-text-layout-review-v1" or
            review.get("paper_id") != document["paper_id"] or
            review.get("source_sha256") != document["source_sha256"] or
            review.get("raw_pages_sha256") != document["raw_pages_sha256"] or
            not review.get("reviewer") or not review.get("reason") or not review.get("evidence_files") or
            review.get("paragraph_boundaries_checked") is not True or
            review.get("reading_lanes_checked") is not True):
        raise ValueError("Incomplete or stale source layout review")
    selected = review.get("pages",[])
    if not selected or len({p["page"] for p in selected}) != len(selected):
        raise ValueError("Layout review physical-page coverage invalid")
    for page_review in selected:
        number = page_review["page"]
        if type(number) is not int or not 1 <= number <= len(pages):
            raise ValueError("Layout physical page outside source")
        raw = pages[number-1]
        originals = {x["line_id"]:x for x in raw["lines"]}
        expected = [x["line_id"] for x in raw["lines"] if x["text"].strip() and not x.get("superseded_by_ocr")]
        actual = []; gids = set()
        groups = page_review.get("groups", [])
        for group_index, group in enumerate(groups):
            if (not group.get("group_id") or group["group_id"] in gids or not group.get("reason") or
                    group.get("kind") not in {"prose","list","heading","mixed","author_callout",
                                                "front_matter","furniture","title","caption","keywords","source_object"}):
                raise ValueError("Layout group identity/classification invalid")
            gids.add(group["group_id"])
            ids = group.get("source_line_ids",[])
            if not ids or any(lid not in originals for lid in ids):
                raise ValueError("Layout group native lines missing")
            text = " ".join(originals[lid]["text"].strip() for lid in ids)
            if digest(text.encode()) != group.get("text_sha256"):
                raise ValueError("Layout group literal preimage changed")
            opening=group.get("opens_section")
            if opening is not None:
                if (not isinstance(opening, dict) or opening.get('role') not in ROLES or
                        type(opening.get('level')) is not int or not 1 <= opening['level'] <= 12):
                    raise ValueError('Reviewed section opening invalid')
                if 'trailing_label_group_id' in opening:
                    # A source-checked appendix sheet may print its label BELOW
                    # the object. Keep that literal order; never move the label
                    # or leave the object in the preceding bibliography.
                    label = groups[group_index+1] if group_index+1 < len(groups) else {}
                    label_ids = label.get('source_line_ids', [])
                    if (set(opening) != {'role', 'level', 'trailing_label_group_id'} or
                            group['kind'] != 'source_object' or opening['role'] != 'appendix' or
                            label.get('group_id') != opening['trailing_label_group_id'] or
                            label.get('kind') != 'caption' or label.get('opens_section') is not None or
                            not label_ids or any(lid not in originals for lid in label_ids) or
                            title_role(' '.join(originals[lid]['text'].strip() for lid in label_ids), number) != 'appendix'):
                        raise ValueError('Reviewed section opening invalid')
                elif (set(opening) != {'role', 'level'} or group['kind'] != 'heading' or
                        opening['role'] != title_role(text, number)):
                    raise ValueError('Reviewed section opening invalid')
            actual += ids
        if Counter(actual) != Counter(expected) or len(set(actual)) != len(actual):
            raise ValueError("Layout review must account for every active page line exactly once")


def apply_layout_reviews(document, pages, reviews):
    applied = []
    for review in reviews:
        if review.get("paper_id") != document["paper_id"]:
            continue
        check_layout_review(document,pages,review)
        rid = digest(encoded(review))
        for item in review["pages"]:
            page = pages[item["page"]-1]
            if page.get("reviewed_text_groups"):
                raise ValueError("Duplicate reviewed page layout")
            page["reviewed_text_groups"] = item["groups"]
            page["layout_review_sha256"] = rid
        applied.append(review)
    return applied


def validate_layout_reviews(document, pages):
    declared = {}
    for review in document.get("layout_reviews",[]):
        check_layout_review(document,pages,review)
        rid = digest(encoded(review))
        for item in review["pages"]:
            number = item["page"]
            if number in declared:
                raise ValueError("Duplicate layout proof page")
            declared[number] = (rid,item["groups"])
    reviewed_blocks = [b for b in document["blocks"] if b.get("layout_group_id")]
    if len(reviewed_blocks) != sum(len(groups) for _,groups in declared.values()):
        raise ValueError("Layout groups and retained blocks differ")
    for number,(rid,groups) in declared.items():
        actual = [b for b in document["blocks"] if b.get("layout_group_id") and b["source_pages"]==[number]]
        if len(actual) != len(groups):
            raise ValueError("Layout page block count differs")
        for block,group in zip(actual,groups):
            if (block["layout_group_id"] != group["group_id"] or
                    block.get("layout_review_sha256") != rid or block["source_line_ids"] != group["source_line_ids"] or
                    block.get("pre_repair_kind",block["kind"]) != group["kind"]):
                raise ValueError("Reviewed layout ordering/classification changed")
            if group.get('opens_section'):
                section=next(s for s in document['sections'] if s['section_id']==block['section_id'])
                opening=group['opens_section']
                trailing = opening.get('trailing_label_group_id')
                label = next((b for b in actual if b['layout_group_id'] == trailing), None) if trailing else block
                origin = 'reviewed-trailing-appendix-label' if trailing else 'reviewed-printed-heading'
                if (label is None or section['title']!=label['text'] or section['role']!=opening['role'] or
                        section['level']!=opening['level'] or section['origin']!=origin or
                        section['block_ids'][0]!=block['block_id']):
                    raise ValueError('Reviewed section opening ownership changed')
                if trailing and (label['section_id'] != section['section_id'] or
                        section.get('source_label_group_id') != trailing or
                        section.get('source_label_line_ids') != label['source_line_ids']):
                    raise ValueError('Reviewed section opening ownership changed')
