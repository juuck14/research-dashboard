#!/usr/bin/env python3
import csv,json
import numpy as np
from run_study import matrices,sparse_bases,ROOT,make_points,R

def audit(e,scale,seed):
    A1,_=matrices(1.,scale)
    A=np.vstack([A1,np.zeros((4,2))])
    C=A@R
    B=np.vstack([A1@R,e*np.eye(2),e*np.eye(2)])
    am,an,_=sparse_bases(A)
    bm,bn,_=sparse_bases(B)
    S=make_points(seed);Z=S@R
    return dict(epsilon=e,true_min_sparsity=am,true_nonaligned_min=an,
        candidate_reference_min_sparsity=bm,candidate_reference_nonaligned_min=bn,
        distance=float(np.linalg.norm(C-B,2)),predicted_distance=float(np.sqrt(2)*e),
        true_min_singular=float(np.linalg.svd(A,compute_uv=False).min()),
        candidate_min_singular=float(np.linalg.svd(B,compute_uv=False).min()),
        same_law_error=float(np.max(np.abs(S@A.T-Z@C.T))),
        quotient_angle_degrees=45.)

rows=[audit(e,None,20261022) for e in [.1,.03,.01,.003,.001,1e-4,1e-6]]
rng=np.random.default_rng(20261025)
confirm=[audit(float(10**rng.uniform(-7,-1)),rng.uniform(.7,1.4,4),20261025) for _ in range(20)]
for name,rr in [('fixed_base',rows),('fixed_base_confirmation',confirm)]:
    with (ROOT/f'results/{name}.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rr[0]));w.writeheader();w.writerows(rr)
summary=dict(cases=len(rows)+len(confirm),fixed_true_reference=True,
    true_sparsity_min=sorted({x['true_min_sparsity'] for x in rows+confirm}),
    candidate_reference_sparsity_min=sorted({x['candidate_reference_min_sparsity'] for x in rows+confirm}),
    minimum_true_gap=min(x['true_nonaligned_min']-x['true_min_sparsity'] for x in rows+confirm),
    minimum_candidate_gap=min(x['candidate_reference_nonaligned_min']-x['candidate_reference_min_sparsity'] for x in rows+confirm),
    max_distance_error=max(abs(x['distance']-x['predicted_distance']) for x in rows+confirm),
    max_same_law_error=max(x['same_law_error'] for x in rows+confirm),
    limitation='zero observation rows and a larger candidate-reference sparsity budget are allowed')
(ROOT/'results/fixed_base_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
