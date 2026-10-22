#!/usr/bin/env python3
"""Audit a proven all-candidate bound using an exact nonlinear same-law family."""
import csv,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def h(s,b):return s+b*np.sin(s[:,::-1])
def dh(s,b):
    J=np.broadcast_to(np.eye(2),(len(s),2,2)).copy()
    J[:,0,1]=b*np.cos(s[:,1]);J[:,1,0]=b*np.cos(s[:,0])
    return J
def hinv(z,b):
    s=z.copy()
    for _ in range(12):
        step=np.linalg.solve(dh(s,b),(h(s,b)-z)[...,None])[...,0]
        s-=step
        if np.max(np.abs(step))<1e-14:break
    return s
def g0(s):
    x,y=s.T
    return np.column_stack([x+.1*x**3,1.2*x+.05*x**3,y+.07*y**3,.9*y+.1*y**3,x+y+.1*x*y])
def dg0(s):
    x,y=s.T;J=np.zeros((len(s),5,2))
    J[:,0,0]=1+.3*x*x;J[:,1,0]=1.2+.15*x*x
    J[:,2,1]=1+.21*y*y;J[:,3,1]=.9+.3*y*y
    J[:,4,0]=1+.1*y;J[:,4,1]=1+.1*x
    return J
def audit(s,b,group):
    z=h(s,b);si=hinv(z,b)
    B=dh(s,b);A=dg0(s);C=dg0(z)
    actual_candidate_J=dg0(si)@np.linalg.inv(dh(si,b))
    jacerr=np.linalg.norm(actual_candidate_J-C,ord=2,axis=(1,2))
    c0=np.linalg.norm(g0(si)-g0(z),axis=1)
    delta=3*b/(1-b)+np.sqrt(2)*b
    L=1+b;a=.9;eta=delta*(1+L)
    residual=np.linalg.norm(A-C@B,axis=2).max()
    return dict(group=group,beta=b,points=len(s),inverse_error=float(np.max(np.abs(si-s))),
        same_law_error=float(np.max(np.abs(g0(si)-g0(s)))),
        measured_candidate_C0=float(c0.max()),measured_candidate_C1=float(jacerr.max()),
        analytic_delta=delta,eta=eta,theorem_condition=bool(eta<a/np.sqrt(2)),
        measured_row_residual=float(residual),residual_bound=eta,
        measured_offblock=float(np.abs(B[:,[0,1],[1,0]]).max()),
        offblock_bound=L*eta/a,
        measured_C0_to_block=float(np.abs(h(s,b)-s).max()),
        block_C0_bound=.6*L*eta/a,
        minimum_true_row_norm=float(np.linalg.norm(A,axis=2).min()),
        candidate_reference_sparsity_max=int(np.count_nonzero(C,axis=(1,2)).max()))

grid=np.linspace(-.6,.6,61);S=np.array(np.meshgrid(grid,grid)).reshape(2,-1).T
T=np.random.default_rng(20261024).uniform(-.6,.6,(1024,2))
rows=[audit(s,b,name) for name,s in [('primary',S),('confirmation',T)] for b in [.001,.003,.01,.03,.05]]
with (ROOT/'results/positive_bound.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
norm_rows=[]
for e in [.1,.03,.01,.003]:
    norm_rows.append(dict(epsilon=e,offblock_upper=e*e,
        diagonal_derivative_range_at_s0=1.2*e,
        global_C1_distance_lower=.6*e,
        lower_to_offblock_ratio=.6/e,
        second_derivative_entry_bound=1.))
with (ROOT/'results/norm_control.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(norm_rows[0]));w.writeheader();w.writerows(norm_rows)
summary=dict(cases=len(rows),all_theorem_conditions=all(r['theorem_condition'] for r in rows),
    max_inverse_error=max(r['inverse_error'] for r in rows),
    max_same_law_error=max(r['same_law_error'] for r in rows),
    max_leakage_fraction=max(max(r['measured_candidate_C0'],r['measured_candidate_C1'])/r['analytic_delta'] for r in rows),
    max_offblock_bound_fraction=max(r['measured_offblock']/r['offblock_bound'] for r in rows),
    max_block_C0_bound_fraction=max(r['measured_C0_to_block']/r['block_C0_bound'] for r in rows),
    confirmation_seed=20261024,
    evidence='Nonlinear exact same-law construction; not trained autoencoder; all-candidate assertion is proven separately')
(ROOT/'results/positive_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
