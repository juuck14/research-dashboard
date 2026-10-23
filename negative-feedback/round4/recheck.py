"""Replay scope checks and one fixed non-oracle seed without replacing raw outputs."""
from pathlib import Path
import json, os, shutil, subprocess, sys, tempfile, time

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
scripts=['assumptions/check_assumptions.py','value_audit/task_meaning_check.py',
         'temperature_check.py','nonoracle/symmetry_check.py']
rows=[]
with tempfile.TemporaryDirectory(prefix='negative-scope-recheck-') as tmp:
    stage=Path(tmp)
    shutil.copytree(REPO/'negative-feedback',stage/'negative-feedback',
                    ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    for script in scripts:
        start=time.monotonic()
        p=subprocess.run([sys.executable,'negative-feedback/round4/'+script],
                         cwd=stage,env=env,text=True,capture_output=True)
        rows.append({'script':script,'exit_code':p.returncode,
                     'elapsed_seconds':time.monotonic()-start,'stderr':p.stderr[-2000:]})
    code="""
import sys,json
sys.path.insert(0,'negative-feedback/round4/nonoracle')
import run
rows=[]
for K in [4,8,16]:
 row,_,_=run.run(6201,K,'adaptive',2.,8000,'root_recheck')
 rows.append(row)
print(json.dumps(rows))
"""
    p=subprocess.run([sys.executable,'-c',code],cwd=stage,env=env,text=True,capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr)
    repeated=json.loads(p.stdout)
    original=json.loads((HERE/'nonoracle/results/summary.json').read_text())['rows']
    comparisons=[]
    for row in repeated:
        ref=next(x for x in original if x['seed']==6201 and x['K']==row['K'] and x['policy']=='adaptive' and x['arm']=='base')
        deltas={key:abs(row[key]-ref[key]) for key in ['best_square_error','view_variance','full_field_norm']}
        comparisons.append({'K':row['K'],'absolute_differences':deltas,
                            'matches':max(deltas.values())<1e-8})
result={'script_checks':rows,'nonoracle_seed6201_replay':comparisons,
        'passed':all(x['exit_code']==0 for x in rows) and all(x['matches'] for x in comparisons),
        'scope':'same-source isolated rerun, not independent implementation, additional seed or importance evidence'}
(HERE/'recheck.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if not result['passed']:raise SystemExit(1)
