"""Independent exact-law checks. No owner implementation imported.

Run from repository root:
OPENBLAS_NUM_THREADS=1 python prevalidation-20261022/reviews/uncertainty/independent_check.py
"""
import csv
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.special import i0e

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)


def orthogonal_fixing_ones(theta):
    one = np.ones(3) / np.sqrt(3)
    first = np.array([2., -1., -1.]) / np.sqrt(6)
    second = np.array([0., 1., -1.]) / np.sqrt(2)
    basis = np.column_stack((one, first, second))
    c, s = np.cos(theta), np.sin(theta)
    rot = np.array([[1., 0., 0.], [0., c, -s], [0., s, c]])
    return basis @ rot @ basis.T


def categorical_checks():
    a = .4
    projector = np.ones((3, 3)) / 3
    eye = np.eye(3)
    q = projector + a * (eye - projector)
    pair_target = q @ q.T / 3
    angles = list(np.linspace(0., 2 * np.pi, 1001))
    angles += list(np.random.default_rng(7319).uniform(0, 2*np.pi, 200))
    rows = []
    err_pair = err_triple = err_formula = err_marginal = 0.
    min_entry = 1.
    for i, theta in enumerate(angles):
        e = projector + a * orthogonal_fixing_ones(theta) @ (eye-projector)
        # Independently enumerate finite latent and observation outcomes.
        pair = np.zeros((3, 3))
        triple = np.zeros((3, 3, 3))
        for z in range(3):
            for x in range(3):
                for y in range(3):
                    pair[x, y] += e[x, z]*e[y, z]/3
                    for w in range(3):
                        triple[x, y, w] += e[x, z]*e[y, z]*e[w, z]/3
        direct = triple[0,0,0]/pair[0,0]
        predicted = (1+6*a*a+2*a**3*np.cos(3*theta))/(3*(1+2*a*a))
        err_pair = max(err_pair, float(abs(pair-pair_target).max()))
        err_triple = max(err_triple, float(abs(triple.sum(axis=2)-pair).max()))
        err_formula = max(err_formula, abs(direct-predicted))
        err_marginal = max(err_marginal, float(abs(e.sum(axis=0)-1).max()),float(abs(e.sum(axis=1)-1).max()))
        min_entry = min(min_entry, float(e.min()))
        rows.append({"split":"primary" if i<1001 else "confirmation", "theta":float(theta),"p3_given_11":float(direct),"formula":float(predicted),"pair_error":float(abs(pair-pair_target).max())})
    with (OUT/"categorical_orbit.csv").open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    low=(1+6*a*a-2*a**3)/(3*(1+2*a*a))
    high=(1+6*a*a+2*a**3)/(3*(1+2*a*a))
    assert max(err_pair,err_triple,err_formula,err_marginal)<1e-12
    assert min_entry>=0
    return {"primary_count":1001,"confirmation_count":200,"confirmation_seed":7319,"max_pair_error":err_pair,"max_triple_marginal_error":err_triple,"max_formula_error":err_formula,"max_stochastic_error":err_marginal,"min_entry":min_entry,"sharp_interval":[low,high],"scope":"uniform3, square doubly-stochastic emissions, fixed isotropic Gram; not arbitrary priors or emission families"}


def log_bessel_series(n,x):
    """Log sum_k x^k/[k! (n+1)...(n+k)] without Bessel underflow."""
    term=total=1.
    for k in range(1,10000):
        term *= x/(k*(n+k))
        total += term
        if term < total*1e-17:
            return math.log(total),k
    raise RuntimeError("series did not converge")


def bessel_expansion_checks():
    rows=[]
    for a,b in [(.5,.5),(1.,2.),(2.,1.),(2.,2.),(4.,8.),(8.,4.)]:
        x,y=a*a/4,b*b/4
        s=2*x+y
        r=2*x*x+y*y
        coeff3=s-r/2
        coeff4=2*(-x+2*x*x)+(-y+2*y*y)
        for n in [5,10,20,40,80,160,320]:
            sa,ka=log_bessel_series(n,x)
            sb,kb=log_bessel_series(n,y)
            actual=2*sa+sb
            approximation=s/n-s/n**2+coeff3/n**3
            residual=actual-approximation
            rows.append({"a":a,"b":b,"n":n,"log_normalized_series":actual,"third_order_approximation":approximation,"residual":residual,"residual_times_n4":residual*n**4,"limiting_residual_times_n4":coeff4,"terms_a":ka,"terms_b":kb})
    with (OUT/"bessel_expansion.csv").open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    # No claim that finite-n residuals themselves prove the analytic theorem.
    return {"count":len(rows),"note":"finite-order diagnostic only; proof is in exact_identification.md", "n320_residual_times_n4":[{k:row[k] for k in ["a","b","residual_times_n4","limiting_residual_times_n4"]} for row in rows if row["n"]==320]}


summary={"categorical":categorical_checks(),"bessel":bessel_expansion_checks(),"environment":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,"platform":platform.platform()}}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
