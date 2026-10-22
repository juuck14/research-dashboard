"""Re-execute decisive checks in an isolated copy; never overwrite delivered raw data."""
from pathlib import Path
import hashlib, json, os, platform, shutil, subprocess, sys, tempfile, time
import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CHECKS = [
    'foundations/verify_multilevel.py',
    'foundations/hypercube_prediction.py',
    'foundations/continuous_check.py',
    'neural/validate_oracle.py',
    'neural/check_parameter_gradient.py',
    'neural/certify_mixing.py',
    'review/window_certificate_check.py',
    'correlation/certify.py',
    'review/correlation_check.py',
    'review/endpoint_check.py',
    'journal/zero_self_cycle_certificate.py',
    'review/cycle20_certificate_check.py',
    'neural/cycle_no_self.py',
    'review/standard_ode_recheck.py',
]

def main():
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    rows = []
    with tempfile.TemporaryDirectory(prefix='count-rescue-audit-') as temp:
        stage = Path(temp)
        shutil.copytree(REPO/'negative-feedback', stage/'negative-feedback',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        for script in CHECKS:
            rel = 'negative-feedback/round3/'+script
            start = time.monotonic()
            process = subprocess.run([sys.executable, rel], cwd=stage,
                                     env=env, text=True, capture_output=True)
            row = {'script': script, 'exit_code': process.returncode,
                   'elapsed_seconds': time.monotonic()-start,
                   'stdout_sha256': hashlib.sha256(process.stdout.encode()).hexdigest()}
            if process.returncode:
                row['stderr_tail'] = process.stderr[-3000:]
            rows.append(row)
            print(json.dumps(row), flush=True)
        isolated = stage/'negative-feedback/round3'
        # Exact expected quantities; wall-clock fields intentionally excluded.
        comparisons = [
            ('foundations/results/continuous_summary.json', 'max_resolution_curvature_difference'),
            ('neural/results/oracle_validation.json', None),
            ('correlation/results/rational_certificate.json', None),
            ('review/window_certificate_check.json', None),
            ('review/cycle20_certificate_check.json', None),
        ]
        quantity_checks = []
        def close(a, b):
            if isinstance(a, dict):
                return a.keys() == b.keys() and all(close(a[k], b[k]) for k in a)
            if isinstance(a, list):
                return len(a) == len(b) and all(close(x, y) for x, y in zip(a, b))
            if isinstance(a, (int, float)) and not isinstance(a, bool):
                return bool(np.isclose(a, b, rtol=1e-8, atol=1e-10))
            return a == b
        for path, key in comparisons:
            reference = json.loads((HERE/path).read_text())
            actual = json.loads((isolated/path).read_text())
            quantity_checks.append({'path': path, 'key': key,
                                    'matches': close(reference if key is None else reference[key],
                                                     actual if key is None else actual[key])})
    result = {'python': platform.python_version(), 'numpy': np.__version__,
              'scipy': scipy.__version__, 'scripts': rows,
              'delivered_quantity_checks': quantity_checks,
              'passed': all(row['exit_code'] == 0 for row in rows)
                        and all(row['matches'] for row in quantity_checks),
              'scope': 'isolated-copy source reproducibility, not a new scientific effect or independent mathematical proof'}
    (HERE/'audit_snapshot.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'passed': result['passed'], 'checks': len(rows)}, indent=2))
    if not result['passed']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
