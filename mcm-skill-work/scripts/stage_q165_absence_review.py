"""Freeze an actually completed local prose/layout absence check; create-only."""
from pathlib import Path
import copy
import re

from corpus_reader import Catalog
from source_absence_reviews import apply_absence_reviews, prepare_absence_reviews
from text_corpus import file_hash, json_new, read_json, rows


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261030-v12'
    reviews = base / 'reviews/20261030'
    output = reviews / 'q165-abstract-absence-v1.json'
    if output.exists():
        raise ValueError('Create-only proof exists; inspect, never overwrite')
    doc = Catalog(root).document('P-C-2011-10607-6ed4fd93')
    census_path = reviews / 'q165-full-native-prose-census-v1.json'
    findings_path = reviews / 'q165-whole-source-layout-findings-v1.json'
    census, findings = read_json(census_path), read_json(findings_path)
    folder = base / 'source-reviews/q165-whole-source-20261030-v1'
    manifest_path = folder / 'manifest.json'
    manifest = read_json(manifest_path)
    pages = list(range(1, 21))
    for evidence in (census, findings, manifest):
        if any(evidence[k] != doc[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')):
            raise ValueError('Source identity changed')
    if (census['native_prose_read_pages'] != pages or
            findings['checked_physical_pages'] != pages or
            [p['physical_page'] for p in manifest['files'] if p.get('physical_page')] != pages or
            [p for g in findings['overviews_actually_checked'] for p in g['pages']] != pages):
        raise ValueError('Full native/physical-page census differs')
    proxies = [p for p in manifest['files'] if p.get('overview')]
    if len(proxies) != 7 or [p['overview'] for p in proxies] != [p['file'] for p in findings['overviews_actually_checked']]:
        raise ValueError('Actually inspected overview list differs')
    for item in manifest['files']:
        for name, key in (('native_text', 'native_text_sha256'), ('raw_png', 'raw_png_sha256'), ('overview', 'sha256')):
            if item.get(name) and file_hash(folder / item[name]) != item[key]:
                raise ValueError('Evidence bytes changed')
    if any(p['bytes'] > 450000 or (folder / p['overview']).stat().st_size != p['bytes'] for p in proxies):
        raise ValueError('Proxy size differs or exceeds transport guard')
    source = Path(read_json(root / 'scope.json')['source_root'])
    team = re.compile(r'(?<!\d)10607(?!\d)')
    inventory = [p for p in source.rglob('*10607*') if p.is_file()]
    exact = [p for p in inventory if team.search(p.name)]
    records = rows(work / 'artifacts/corpus/manifest.jsonl')
    matches = [r for r in records if team.search(r['file_name'])]
    if (len(records) != 604 or len(exact) != 1 or file_hash(exact[0]) != doc['source_sha256'] or
            len(matches) != 1 or matches[0]['sha256'] != doc['source_sha256']):
        raise ValueError('Local alternative-source inventory changed')
    independent = root / 'papers' / doc['paper_id'] / 'raw/pdftotext.bin'
    independent_text = independent.read_bytes().decode('utf-8', 'strict')
    if re.search(r'\b(?:abstract|summary)\b', independent_text, re.I):
        raise ValueError('Independent text has an unreviewed summary/abstract occurrence')
    proof = {
        'schema': 'source-absence-review-v1',
        **{k: doc[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')},
        'role': 'abstract', 'reviewer': findings['reviewer'],
        'page_count': 20, 'checked_pages': pages,
        'reason': findings['whole_source_abstract_finding'] + ' Source-local only, not external archive completeness or whole-paper prose fidelity.',
        'full_native_prose_read': True, 'physical_page_heading_layout_checked': True,
        'independent_text_check': {
            'path': f"papers/{doc['paper_id']}/raw/pdftotext.bin",
            'sha256': file_hash(independent),
            'status': 'Strict UTF-8 extraction retained; zero abstract/summary word occurrences. Not a formula check or full-page equality certificate.'},
        'alternative_copy_check': {
            'manifest_sha256': file_hash(work / 'artifacts/corpus/manifest.jsonl'),
            'manifest_records': len(records), 'matching_file_count': len(exact),
            'substring_candidates': [{'relative_path': p.relative_to(source).as_posix(),
                'sha256': file_hash(p), 'same_team_token': bool(team.search(p.name))} for p in inventory],
            'result': 'All604 records and source filename inventory checked. The unrelated2021 file2106074 is only a substring match, not a second team10607 source.'},
        'evidence': [
            {'path': str(manifest_path), 'bundle_root': str(folder), 'sha256': file_hash(manifest_path),
             'description': 'All20 native pages and source rasters retained; seven bounded JPEG overviews actually inspected for heading/prose layout only.'},
            {'path': str(census_path), 'sha256': file_hash(census_path),
             'description': 'Earlier actual full native-prose traversal, with its then-unread image limitation preserved.'},
            {'path': str(findings_path), 'sha256': file_hash(findings_path),
             'description': 'Subsequent actual all20-page heading/layout findings; no formula/figure interpretation.'}],
        'application_status': 'Staged for a future immutable generation; no parent, legacy progress or history modified.',
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output, proof)
    prepared, copies = prepare_absence_reviews([output])
    apply_absence_reviews(copy.deepcopy(doc), prepared)
    print({'paper_id': doc['paper_id'], 'checked_physical_pages': len(pages),
        'portable_evidence_files': len(copies), 'jpeg_bytes_actually_transported': sum(p['bytes'] for p in proxies),
        'source_local_abstract_absence': 'staged only', 'whole_paper_acceptance': False})


if __name__ == '__main__':
    main()
