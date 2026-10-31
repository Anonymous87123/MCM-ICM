"""Bind actual42-page prose/layout census to source-local abstract absence only."""
import copy
from pathlib import Path
import re

from corpus_reader import Catalog
from source_absence_reviews import apply_absence_reviews, prepare_absence_reviews
from text_corpus import file_hash, json_new, read_json, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v26'
    directory = base / 'reviews/20261031'
    output = directory / 'q011-abstract-absence-v1.json'
    combined_path = directory / 'q011-whole-source-layout-findings-v1.json'
    if output.exists() or combined_path.exists():
        raise ValueError('Create-only evidence exists; preserve it')
    doc = Catalog(root).document('P-A-2012-14990-e2428f0d')
    folder = base / 'source-reviews/q011-whole-source-20261030-v1'
    manifest_path = folder / 'manifest.json'
    manifest = read_json(manifest_path)
    census_path = base / 'reviews/20261030/q011-full-native-prose-census-v1.json'
    census = read_json(census_path)
    finding_paths = [
        base / 'reviews/20261030/q011-opening-layout-findings-v1.json',
        directory / 'q011-pages4-6-layout-findings-v1.json',
        directory / 'q011-pages7-27-layout-findings-v1.json',
        base / 'reviews/20261030/q011-pages28-30-layout-findings-v1.json',
        directory / 'q011-pages31-42-layout-findings-v1.json']
    findings = [read_json(p) for p in finding_paths]
    identity = ('paper_id', 'source_sha256', 'raw_pages_sha256')
    if any(any(item[k] != doc[k] for k in identity) for item in [manifest, census, *findings]):
        raise ValueError('Frozen source identities differ')
    pages = list(range(1, 43))
    coverage = [p for item in findings for p in item.get('checked_physical_pages', item.get('checked_pages', []))]
    if (doc['page_count'] != 42 or census['native_prose_read_pages'] != pages or
            coverage != pages or manifest['page_count'] != 42):
        raise ValueError('Exact source census and actual layout coverage required')
    by_name = {x['overview']: x for x in manifest['files'] if x.get('overview')}
    # Opening pages were checked with individual JPEGs, not overview00.
    opening_proofs = findings[0]['evidence']
    if len(opening_proofs) != 3:
        raise ValueError('Opening page proofs differ')
    for item in opening_proofs:
        path = work / item['path']
        if file_hash(path) != item['sha256'] or path.stat().st_size != item['bytes'] or item['bytes'] > 450000:
            raise ValueError('Actually inspected opening JPEG changed')
    inspected = ['overview-01.jpg']
    if findings[1]['overview_sha256'] != by_name['overview-01.jpg']['sha256']:
        raise ValueError('Page4–6 overview differs')
    for item in findings[2]['overviews_actually_checked'] + findings[4]['overviews_actually_checked']:
        declared = by_name[item['file']]
        if item['sha256'] != declared['sha256'] or item['physical_pages'] != declared['physical_pages']:
            raise ValueError('Actually inspected overview binding differs')
    inspected += [x['file'] for x in findings[2]['overviews_actually_checked']]
    inspected += findings[3]['overviews_actually_checked']
    inspected += [x['file'] for x in findings[4]['overviews_actually_checked']]
    if inspected != [f'overview-{n:02d}.jpg' for n in range(1, 14)]:
        raise ValueError('Actual overview coverage lost or repeated')
    for item in manifest['files']:
        for field, sha in (('native_text', 'native_text_sha256'), ('raw_png', 'raw_png_sha256'), ('overview', 'sha256')):
            if item.get(field) and file_hash(folder / item[field]) != item[sha]:
                raise ValueError('Prepared native/raster/proxy evidence changed')
        if item.get('overview') and (item['bytes'] > 450000 or
                (folder / item['overview']).stat().st_size != item['bytes']):
            raise ValueError('Proxy byte guard differs')
    records_path = work / 'artifacts/corpus/manifest.jsonl'
    records = rows(records_path)
    team = re.compile(r'(?<!\d)14990(?!\d)')
    matches = [r for r in records if team.search(r['file_name'])]
    source = Path(read_json(root / 'scope.json')['source_root'])
    candidates = [p for p in source.rglob('*14990*') if p.is_file()]
    exact = [p for p in candidates if team.search(p.name)]
    if (len(records) != 604 or len(matches) != 1 or matches[0]['sha256'] != doc['source_sha256'] or
            len(exact) != 1 or file_hash(exact[0]) != doc['source_sha256']):
        raise ValueError('Alternative local source inventory differs')
    independent = root / 'papers' / doc['paper_id'] / 'raw/pdftotext.bin'
    if re.search(r'\b(?:abstract|summary)\b', independent.read_bytes().decode('utf-8', 'strict'), re.I):
        raise ValueError('Unreviewed independent synopsis occurrence')
    combined = {'schema': 'whole-source-heading-layout-findings-v1', **{k: doc[k] for k in identity},
        'reviewer': 'Codex root;2026-10-30/31;all42 native prose pages and complete physical heading/layout coverage actually checked',
        'checked_physical_pages': pages, 'opening_individual_jpegs': opening_proofs,
        'overviews_actually_checked': [by_name[name] for name in inspected],
        'bounded_findings_sha256': {str(p): file_hash(p) for p in finding_paths},
        'whole_source_abstract_finding': 'The local42-page PDF contains a title cover, Contents, Introduction, task analysis, assumptions, nomenclature, four model chapters with local Introductions/Conclusions, appraisal, references, an explicitly addressed editor letter, and appendix objects/code. There is no independent headed or unheaded abstract/summary. The editor letter is retained separately, not substituted for an abstract.',
        'whole_paper_source_fidelity_approved': False, 'ai_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(combined_path, combined)
    evidence = [
        {'path': str(manifest_path), 'bundle_root': str(folder), 'sha256': file_hash(manifest_path),
         'description': 'Complete42-page native/raster evidence and bounded overview files; overview00 was prepared but NOT used as actual-reading evidence.'},
        {'path': str(census_path), 'sha256': file_hash(census_path),
         'description': 'Earlier actual42-page native-prose census; its old image-pending limitation remains preserved.'},
        {'path': str(combined_path), 'sha256': file_hash(combined_path),
         'description': 'Later complete physical heading/layout coverage; exact inspected-image and bounded-finding bindings.'}]
    evidence += [{'path': str(p), 'sha256': file_hash(p), 'description': 'Preserved actual bounded heading/layout findings.'} for p in finding_paths]
    evidence += [{'path': str(work / p['path']), 'sha256': p['sha256'],
                  'description': 'Actually inspected individual opening-page JPEG.'} for p in opening_proofs]
    proof = {'schema': 'source-absence-review-v1', **{k: doc[k] for k in identity},
        'role': 'abstract', 'reviewer': combined['reviewer'], 'page_count': 42, 'checked_pages': pages,
        'reason': combined['whole_source_abstract_finding'] + ' Source-local only; no external completeness or whole-paper fidelity claim.',
        'full_native_prose_read': True, 'physical_page_heading_layout_checked': True,
        'independent_text_check': {'path': f"papers/{doc['paper_id']}/raw/pdftotext.bin", 'sha256': file_hash(independent),
            'status': 'Strict UTF-8; zero Abstract/Summary word occurrences. Not full-text fidelity acceptance.'},
        'alternative_copy_check': {'manifest_sha256': file_hash(records_path), 'manifest_records': len(records),
            'matching_file_count': len(exact), 'substring_candidates': [
                {'relative_path': p.relative_to(source).as_posix(), 'sha256': file_hash(p),
                 'same_team_token': bool(team.search(p.name))} for p in candidates],
            'result': 'All604 records and local filename candidates checked; only the same42-page PDF.'},
        'evidence': evidence, 'application_status': 'Staged for later immutable generation; parent/history/receipts unchanged.',
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output, proof)
    prepared, copies = prepare_absence_reviews([output])
    apply_absence_reviews(copy.deepcopy(doc), prepared)
    print({'paper_id': doc['paper_id'], 'source_checked_pages': 42, 'portable_evidence_files': len(copies),
           'abstract_absence': 'staged source-local only', 'whole_paper_acceptance': False}, flush=True)


if __name__ == '__main__':
    main()
