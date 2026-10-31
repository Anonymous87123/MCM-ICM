"""Inventory every stored heading affected by an explicitly versioned task parser."""
import importlib.util
from pathlib import Path

from corpus_reader import Catalog
from corpus_queries import task_numbers
from text_corpus import file_hash,json_new,read_json


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    old_path=base/'transport-runtime-v20-20261031-v1/scripts/corpus_queries.py'
    manifest=read_json(old_path.parent.parent/'manifest.json')
    if file_hash(old_path)!=manifest['files']['corpus_queries.py']:
        raise ValueError('Frozen old query policy changed')
    spec=importlib.util.spec_from_file_location('frozen_v20_task_policy',old_path)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    catalog=Catalog(base/'reflow-20261031-v21');changed=[];checked=0
    for paper in catalog.papers:
        doc=catalog.document(paper['paper_id'])
        for section in doc['sections']:
            checked+=1;title=section['title'];before=old.task_numbers(title);after=task_numbers(title)
            if before!=after:
                changed.append({'queue':paper['queue_position'],'paper_id':paper['paper_id'],
                    'section_id':section['section_id'],'title':title,
                    'old_tasks':sorted(before),'new_tasks':sorted(after)})
    result={'dataset_id':catalog.identity,'papers':len(catalog.papers),'headings_checked':checked,
        'old_query_policy_sha256':file_hash(old_path),
        'new_query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'changed_headings':changed,'source_fidelity_approved':False,'ai_receipts_created':0,
        'meaning':'Exhaustive stored-heading parser difference inventory, not a PDF boundary check.'}
    json_new(base/'reviews/20261031/task-selector-upgrade-inventory-v1.json',result)
    print(result,flush=True)


if __name__=='__main__':
    main()
