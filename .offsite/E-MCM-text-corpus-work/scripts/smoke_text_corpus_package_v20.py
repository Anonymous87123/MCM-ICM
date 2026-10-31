"""Create-only relative-attachment smoke test; never acknowledge AI reading."""
import json
from pathlib import Path
import subprocess
import sys

STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
PACKAGE = STORE.parent / 'skill-packages/text-corpus-preview-20261031-v20/mcm-icm-master-skill'
RUN = STORE / 'reading-runs/package-smoke-20261031-v20'
REPORT = STORE / 'package-smoke-20261031-v20.json'
CWD = Path(r'D:\code LateX\elegantbook\physics')
sys.path.insert(0, str(PACKAGE / 'scripts'))
from text_corpus import json_new


def call(*args, success=True):
    result = subprocess.run([sys.executable, '-X', 'utf8', str(PACKAGE / 'scripts/corpus_reader.py'), *args],
                            cwd=CWD, capture_output=True, text=True, encoding='utf-8')
    if success and result.returncode:
        raise RuntimeError(result.stderr)
    return result


def main():
    if RUN.exists() or REPORT.exists():
        raise ValueError('Preserve existing smoke run/report')
    started = json.loads(call('start', '--section', 'abstract', '--scope', 'all', '--mode', 'exhaustive',
                              '--allow-unverified', '--run-dir', str(RUN)).stdout)
    first = json.loads(call('next', '--run-dir', str(RUN)).stdout)
    repeated = json.loads(call('next', '--run-dir', str(RUN)).stdout)
    state = json.loads(call('status', '--run-dir', str(RUN)).stdout)
    missing = call('--corpus-root', str(STORE / 'deliberately-missing-package-smoke-v20'), 'sections', success=False)
    if (started['target_papers'] != 435 or first != repeated or state['batches_acknowledged'] != 0
            or missing.returncode == 0 or 'No fallback to language-unit fragments' not in missing.stderr
            or state['dataset_id'] != 'c4b0662c32223c0eb8875492772c5ab0e80340ae29c0011616fc9c7e972a2d95'):
        raise ValueError('Relative attachment, pending replay or missing-database invariant failed')
    result = {'package': str(PACKAGE), 'dataset_id': state['dataset_id'], 'target_papers': state['target_papers'],
              'preview': state['preview'], 'default_relative_attachment_pass': True,
              'pending_batch_replay_identical': True, 'ai_reading_receipts_created': state['batches_acknowledged'],
              'initial_completion_marker': first['completion_marker'],
              'initial_delivered_papers': [chunk['paper_id'] for chunk in first['chunks']],
              'missing_database_error': missing.stderr.strip(), 'installed_skill_modified': False,
              'full_read_acceptance': False, 'query_policy_status': state['query_policy_status'], 'unrelated_cwd': str(CWD)}
    json_new(REPORT, result)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
