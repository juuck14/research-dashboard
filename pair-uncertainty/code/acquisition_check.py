#!/usr/bin/env python3
"""Preregistered lineage and acquisition-budget control, a restricted model."""
from pathlib import Path
import csv,json
import numpy as np

OUT=Path(__file__).resolve().parents[1]/"results"
rows=[]
for split,seeds in [("primary",range(20,30)),("confirmation",range(201,211))]:
    for n in [1000,10000,100000]:
        for seed in seeds:
            rng=np.random.default_rng(seed)
            z=rng.integers(0,3,n)
            zp=np.where(rng.random(n)<.25,z,rng.integers(0,3,n))
            x=np.where(rng.random(n)<.8,z,rng.integers(0,3,n))
            xp=np.where(rng.random(n)<.8,zp,rng.integers(0,3,n))
            repeat=np.where(rng.random(n)<.8,z,rng.integers(0,3,n))
            chat=float(np.clip((3*np.mean(x==xp)-1)/2,0,1))
            rhat=float(np.clip((3*np.mean(x==repeat)-1)/2,0,1))
            ahat=float(np.sqrt(rhat));bhat=float(np.clip(chat/rhat,0,1))
            nb=n*3//2
            zmore=rng.integers(0,3,nb)
            zpmore=np.where(rng.random(nb)<.25,zmore,rng.integers(0,3,nb))
            xmore=np.where(rng.random(nb)<.8,zmore,rng.integers(0,3,nb))
            xpmore=np.where(rng.random(nb)<.8,zpmore,rng.integers(0,3,nb))
            cmore=float(np.clip((3*np.mean(xmore==xpmore)-1)/2,0,1))
            rows.append(dict(split=split,n=n,seed=seed,total_genuine_acquisitions=3*n,
                c_hat_from_n_pairs=chat,c_hat_from_budget_matched_more_pairs=cmore,
                repeat_a_hat=ahat,repeat_b_hat=bhat,
                wrong_independence_assumed_copy_a_hat=1.,
                more_pairs_population_a_width=1-np.sqrt(.16),
                more_pairs_plugin_a_width=1-np.sqrt(cmore)))
with (OUT/"acquisition.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary=[]
for split in ["primary","confirmation"]:
    for n in [1000,10000,100000]:
        rs=[r for r in rows if r["split"]==split and r["n"]==n]
        item=dict(split=split,n=n)
        for key in ["repeat_a_hat","repeat_b_hat","c_hat_from_n_pairs","c_hat_from_budget_matched_more_pairs","more_pairs_plugin_a_width"]:
            vals=[r[key] for r in rs]
            item[key+"_mean"]=float(np.mean(vals));item[key+"_sd"]=float(np.std(vals,ddof=1))
        summary.append(item)
with (OUT/"acquisition_summary.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
print(json.dumps(summary,indent=2))
