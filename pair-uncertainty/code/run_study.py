#!/usr/bin/env python3
"""Exact population calculations and preregistered finite-sample checks.

This is a low-dimensional channel model, not a neural MCInfoNCE reproduction.
Run with OPENBLAS_NUM_THREADS=1 python pair-uncertainty/code/run_study.py
"""
from pathlib import Path
import csv
import json
import platform
import sys
from fractions import Fraction as F

import numpy as np
import scipy
from scipy.optimize import least_squares
from scipy.special import iv, i0
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "results"
OUT.mkdir(exist_ok=True)


def write_csv(name, rows):
    with (OUT / name).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def q(a):
    return a * np.eye(3) + (1-a) * np.ones((3, 3))/3


def categorical_laws(a, b):
    e, k = q(a), q(b)
    pair = e @ k @ e.T / 3
    # R shares anchor Z; positive X2 has transitioned Z2.
    other = e @ k
    triple = np.einsum("iz,jz,kz->ijk", e, other, e)/3
    pred = triple/pair[:, :, None]
    return pair, triple, pred


def brier_regret(ptrue, phat, pairtrue):
    return float(np.sum(pairtrue[:, :, None]*(ptrue-phat)**2))


def clipped_log_regret(ptrue, phat, pairtrue):
    phat = np.clip(phat, 1e-15, 1)
    return float(np.sum(pairtrue[:, :, None]*ptrue*np.log(ptrue/phat)))


def bcoeff(a, b, nmax):
    n = np.arange(1, nmax+1)
    return (iv(n, a)/i0(a))**2 * (iv(n, b)/i0(b))


def invert_coeff(a, b, nmax):
    target = bcoeff(a, b, nmax)
    # Relative log coefficients avoid burying high-order modes in absolute loss.
    # This is an oracle inverse diagnostic, NOT a finite-sample estimator.
    def residual(p):
        return np.log(bcoeff(*np.exp(p), nmax))-np.log(target)
    rows=[]
    for aa in [.2, .6, 1.5, 4., 10.]:
        for bb in [.2, 1., 4., 10.]:
            fit=least_squares(residual, np.log([aa,bb]),
                bounds=(np.log([.1,.1]),np.log([12.,12.])),
                xtol=1e-13, ftol=1e-13, gtol=1e-13, max_nfev=1500)
            est=np.exp(fit.x)
            rows.append(dict(a=a,b=b,nmax=nmax,start_a=aa,start_b=bb,
                a_hat=float(est[0]),b_hat=float(est[1]),
                log_residual=float(np.linalg.norm(fit.fun)),
                parameter_error=float(np.linalg.norm(est-[a,b])),
                success=bool(fit.success)))
    return rows


def exact_toy():
    Q=[[F(3,5) if i==j else F(1,5) for j in range(3)] for i in range(3)]
    R=[[F(1,15) if i==j else F(7,15) for j in range(3)] for i in range(3)]
    def pair(e):
        return [[sum(e[i][z]*e[j][z] for z in range(3))/3 for j in range(3)] for i in range(3)]
    p,q0=pair(Q),pair(R)
    tq=sum(Q[0][z]**3 for z in range(3))/3
    tr=sum(R[0][z]**3 for z in range(3))/3
    assert p==q0
    return dict(pair_diag=str(p[0][0]),pair_off=str(p[0][1]),
        triple_Q=str(tq),triple_R=str(tr),
        predictive_Q=str(tq/p[0][0]),predictive_R=str(tr/p[0][0]),
        triple_difference=str(tq-tr),
        entropy_Q=float(-sum(float(x)*np.log(float(x)) for x in Q[0])),
        entropy_R=float(-sum(float(x)*np.log(float(x)) for x in R[0])))


def population():
    rows=[]
    checks=[]
    for c in [.02,.16,.5,.9]:
        p0,_,_=categorical_laws(np.sqrt(c),1.)
        lo=(1+6*c+2*c**1.5)/(3*(1+2*c))
        for a in np.linspace(np.sqrt(c),1,101):
            b=c/a**2
            pair, triple, pred=categorical_laws(a,b)
            formula=(1+2*a*a+4*c+2*a*c)/(3*(1+2*c))
            checks.extend([np.max(abs(pair-p0)),abs(formula-pred[0,0,0])])
            pairloss=-np.sum(p0*np.log(pair))
            ent=-sum(x*np.log(x) for x in q(a)[0] if x>0)
            rows.append(dict(c=c,a=float(a),b=float(b),
                pair_cross_entropy=float(pairloss),posterior_entropy=float(ent),
                repeat_given_agreement=float(pred[0,0,0]),
                sharp_lower=lo,sharp_upper=1.,
                agreement_event_minimax_brier_regret=3*(1-lo)**2/8))
    write_csv("population_ridge.csv",rows)
    return dict(max_exact_formula_error=float(max(checks)),n_population_rows=len(rows))


def finite_sample():
    a,b=.8,.25
    pair,_,predtrue=categorical_laws(a,b)
    rows=[]
    for split,seeds in [("primary",range(10)),("confirmation",range(101,111))]:
        for n in [1000,10000,100000]:
            for seed in seeds:
                rng=np.random.default_rng(seed)
                z=rng.integers(0,3,n)
                z2=np.where(rng.random(n)<b,z,rng.integers(0,3,n))
                x1=np.where(rng.random(n)<a,z,rng.integers(0,3,n))
                x2=np.where(rng.random(n)<a,z2,rng.integers(0,3,n))
                chat=float(np.clip((3*np.mean(x1==x2)-1)/2,0,1))
                for policy in ["known_positive_b","assume_same_latent_b1","assume_perfect_observation_a1"]:
                    if policy=="known_positive_b":
                        ahat=float(np.sqrt(np.clip(chat/b,0,1)))
                        bhat=b
                    elif policy=="assume_same_latent_b1":
                        ahat=float(np.sqrt(chat));bhat=1.
                    else:
                        ahat=1.;bhat=chat
                    fitted,_,phat=categorical_laws(ahat,bhat)
                    rows.append(dict(split=split,n=n,seed=seed,policy=policy,
                        c_hat=chat,a_hat=ahat,b_hat=bhat,
                        pair_excess_logloss=float(np.sum(pair*np.log(pair/fitted))),
                        repeat_brier_regret=brier_regret(predtrue,phat,pair),
                        repeat_clipped_log_regret=clipped_log_regret(predtrue,phat,pair),
                        exact_log_regret_is_infinite=bool(np.any((predtrue>0) & (phat==0))),
                        agreement_repeat_prediction=float(phat[0,0,0])))
    write_csv("finite_sample.csv",rows)
    summary=[]
    for split in ["primary","confirmation"]:
        for n in [1000,10000,100000]:
            for policy in ["known_positive_b","assume_same_latent_b1","assume_perfect_observation_a1"]:
                subset=[r for r in rows if r["split"]==split and r["n"]==n and r["policy"]==policy]
                row=dict(split=split,n=n,policy=policy)
                row["n_infinite_exact_log_regret"]=sum(r["exact_log_regret_is_infinite"] for r in subset)
                for key in ["c_hat","pair_excess_logloss","repeat_brier_regret","repeat_clipped_log_regret","agreement_repeat_prediction"]:
                    vals=np.array([r[key] for r in subset])
                    row[key+"_mean"]=float(np.mean(vals))
                    row[key+"_sd"]=float(np.std(vals,ddof=1))
                summary.append(row)
    write_csv("finite_sample_summary.csv",summary)
    return dict(n_datasets=60,n_predictions=len(rows),truth_agreement_prediction=float(predtrue[0,0,0]))


def vmf_inverse():
    rows=[]
    for a,b in [(2.,5.),(5.,2.),(1.,1.),(.5,8.),(8.,.5)]:
        for nmax in [1,2,8]:
            rows.extend(invert_coeff(a,b,nmax))
    rng=np.random.default_rng(20261023)
    confirmation=[]
    for a,b in np.exp(rng.uniform(np.log(.3),np.log(10),(20,2))):
        confirmation.extend(invert_coeff(float(a),float(b),8))
    write_csv("vmf_inverse_primary.csv",rows)
    write_csv("vmf_inverse_confirmation.csv",confirmation)
    exactfits=[r for r in rows if r["nmax"]==8 and r["log_residual"]<1e-8]
    confits=[r for r in confirmation if r["log_residual"]<1e-8]
    # Local derivative singularity: a=b yields proportional columns (2:1).
    # Fourth/eighth harmonic availability alone is not numerical conditioning.
    jacrows=[]
    for a,b in [(2.,5.),(5.,2.),(1.,1.),(.5,8.),(8.,.5)]:
        for nmax in [1,2,8]:
            eps=1e-5
            ja=(bcoeff(a+eps,b,nmax)-bcoeff(a-eps,b,nmax))/(2*eps)
            jb=(bcoeff(a,b+eps,nmax)-bcoeff(a,b-eps,nmax))/(2*eps)
            sv=np.linalg.svd(np.column_stack([ja,jb]),compute_uv=False)
            jacrows.append(dict(a=a,b=b,nmax=nmax,
                sigma_max=float(sv[0]),sigma_min=float(sv[-1]) if len(sv)>1 else 0.))
    write_csv("vmf_moment_jacobian.csv",jacrows)
    return dict(primary_fits=len(rows),confirmation_fits=len(confirmation),
        primary_eight_harmonic_small_residual=len(exactfits),
        max_parameter_error_primary_small_residual=max(r["parameter_error"] for r in exactfits),
        confirmation_small_residual=len(confits),
        max_parameter_error_confirmation_small_residual=max(r["parameter_error"] for r in confits))


def plots():
    data=np.genfromtxt(OUT/"population_ridge.csv",delimiter=",",names=True)
    fig,axs=plt.subplots(1,2,figsize=(9,3.3))
    for c in [.02,.16,.5,.9]:
        dd=data[np.isclose(data["c"],c)]
        axs[0].plot(dd["a"],dd["repeat_given_agreement"],label=f"c={c:g}")
        axs[1].plot(dd["a"],dd["pair_cross_entropy"]-dd["pair_cross_entropy"][0],label=f"c={c:g}")
    axs[0].set(xlabel="Observation concentration a",ylabel="P(repeat=i | X1=X2=i)")
    axs[1].set(xlabel="Observation concentration a",ylabel="Population pair-loss excess")
    axs[1].set_ylim(-1e-12,1e-12)
    axs[1].set_title("Numerical roundoff only (under 1e-15)",fontsize=10)
    for ax in axs: ax.legend(frameon=False);ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(OUT/"pair_equivalent_predictions.png",dpi=160)
    plt.close(fig)


def main():
    summary={"toy":exact_toy(),"population":population(),"finite_sample":finite_sample(),"vmf":vmf_inverse()}
    plots()
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    (OUT/"environment.json").write_text(json.dumps(dict(
        python=sys.version,platform=platform.platform(),numpy=np.__version__,
        scipy=scipy.__version__,matplotlib=matplotlib.__version__,
        command="OPENBLAS_NUM_THREADS=1 python pair-uncertainty/code/run_study.py"),indent=2)+"\n")
    print(json.dumps(summary,indent=2))


if __name__=="__main__":main()
