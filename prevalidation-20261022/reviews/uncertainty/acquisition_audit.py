"""Independent repeat-budget simulation using inverse-CDF mod3 offsets."""
from pathlib import Path
import csv,json
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=HERE/"results"

def readcsv(path):
    with path.open() as f:return list(csv.DictReader(f))

owner=readcsv(ROOT/"pair-uncertainty/results/acquisition.csv")
summary=readcsv(ROOT/"pair-uncertainty/results/acquisition_summary.csv")
max_error=0.
for row in owner:
    assert int(row["total_genuine_acquisitions"])==3*int(row["n"])
    max_error=max(max_error,abs(float(row["more_pairs_plugin_a_width"])-(1-np.sqrt(float(row["c_hat_from_budget_matched_more_pairs"])))))
for report in summary:
    group=[r for r in owner if r["split"]==report["split"] and r["n"]==report["n"]]
    assert len(group)==10
    for key in ["repeat_a_hat","repeat_b_hat","c_hat_from_n_pairs","c_hat_from_budget_matched_more_pairs","more_pairs_plugin_a_width"]:
        values=np.array([float(r[key]) for r in group])
        for suffix,fn in [("mean",np.mean),("sd",lambda x:np.std(x,ddof=1))]:
            max_error=max(max_error,abs(float(report[key+"_"+suffix])-float(fn(values))))
assert max_error<1e-12

def offset(rng,n,concentration):
    # q(a): diagonal (1+2a)/3, each off-diagonal (1-a)/3.
    p=(1+2*concentration)/3
    u=rng.uniform(size=n)
    return np.where(u<p,0,np.where(u<(p+(1-p)/2),1,2))

rows=[]
for n in [10000,100000]:
    for seed in range(7501,7507):
        rng=np.random.default_rng(seed)
        latent=rng.integers(3,size=n)
        first=(latent+offset(rng,n,.8))%3
        positive=(latent+offset(rng,n,.25)+offset(rng,n,.8))%3
        repeat=(latent+offset(rng,n,.8))%3
        c=(3*np.mean(first==positive)-1)/2
        repeat_corr=(3*np.mean(first==repeat)-1)/2
        ahat=np.sqrt(max(repeat_corr,0))
        bhat=np.clip(c/repeat_corr,0,1)
        nmore=3*n//2
        latent2=rng.integers(3,size=nmore)
        first2=(latent2+offset(rng,nmore,.8))%3
        positive2=(latent2+offset(rng,nmore,.25)+offset(rng,nmore,.8))%3
        cmore=np.clip((3*np.mean(first2==positive2)-1)/2,0,1)
        rows.append({"n":n,"seed":seed,"total_acquisitions_per_arm":3*n,"repeat_a_hat":float(ahat),"repeat_b_hat":float(bhat),"c_more_pairs":float(cmore),"more_pairs_plugin_width":float(1-np.sqrt(cmore))})
with (OUT/"acquisition_confirmation.csv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
fresh=[]
for n in [10000,100000]:
    group=[r for r in rows if r["n"]==n]
    d={"n":n,"datasets":len(group)}
    for key in ["repeat_a_hat","repeat_b_hat","more_pairs_plugin_width"]:
        values=np.array([r[key] for r in group]);d[key+"_mean"]=float(values.mean());d[key+"_sd"]=float(values.std(ddof=1))
    fresh.append(d)
last=fresh[-1]
assert abs(last["repeat_a_hat_mean"]-.8)<.01
assert abs(last["repeat_b_hat_mean"]-.25)<.025
assert abs(last["more_pairs_plugin_width_mean"]-.6)<.02
result={"owner_rows_audited":len(owner),"owner_summary_max_abs_error":max_error,"independent_seeds":list(range(7501,7507)),"independent_datasets":len(rows),"independent_summary":fresh,"sampling":"inverse-CDF of mod3 offset; no owner code imported","note":"plugin structural width, not a finite-sample confidence interval; repeated-measurement principle is classical"}
(OUT/"acquisition_audit.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
