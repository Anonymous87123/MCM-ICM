"""Create and verify a same-version reading-run copy; leave every F: byte intact."""
from pathlib import Path
import sys

sys.path.insert(0, r'F:\MCM\mcm-skill-work\scripts')
from text_corpus import file_hash, json_new, read_json, write_new


def main():
    source = Path(r'F:\MCM\mcm-skill-work\artifacts\text-corpus\reading-runs\abstract-preview-20261030-v16')
    target = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus\reading-runs\abstract-preview-20261030-v16')
    report = target.parent.parent / 'reading-storage-copy-20261031-v1.json'
    if target.exists() or report.exists():
        raise ValueError('Create-only copy state exists; preserve it')
    session = read_json(source / 'session.json')
    if (session['run_id'] != '541d2520dc494e22a4ae952bd718d398' or
            session['dataset_id'] != '7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65'):
        raise ValueError('Exact existing same-version run required')
    paths = sorted(path for path in source.rglob('*') if path.is_file())
    if any(path.is_symlink() for path in source.rglob('*')):
        raise ValueError('Unexpected symlink in run')
    frozen = {str(path.relative_to(source)): file_hash(path) for path in paths}
    for relative, sha in frozen.items():
        original = source / relative
        data = original.read_bytes()
        write_new(target / relative, data)
        if file_hash(original) != sha or file_hash(target / relative) != sha:
            raise ValueError('Copy or original bytes changed')
    if any(file_hash(source / name) != sha for name, sha in frozen.items()):
        raise ValueError('Original run changed during copy')
    json_new(report, {'schema': 'same-version-reading-storage-copy-v1',
        'source_preserved': str(source), 'continued_run': str(target), 'files_sha256': frozen,
        'run_id': session['run_id'], 'dataset_id': session['dataset_id'],
        'reason': 'Fvolume exhausted; preserve failedv35and every old artifact. Continue on availableEvolume.',
        'source_files_modified': 0, 'new_ai_receipts_created': 0, 'cross_dataset_receipts_transferred': 0,
        'continuation_rule': 'Use only this byte-identical same-session copy for future acknowledgements; do not fork additional receipts in original F run.'})
    print({'copied_files': len(frozen), 'continued_run': str(target), 'same_run_id': session['run_id'], 'original_unchanged': True})


if __name__ == '__main__':
    main()
