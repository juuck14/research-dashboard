"""Independent periodic convolution audit, no Bessel functions or root imports."""
from pathlib import Path
import csv,json
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OP=ROOT/"prevalidation-20261022/operational-uncertainty/results"

def density(a,b,size):
    angle=2*np.pi*np.arange(size)/size
    pa=np.exp(a*(np.cos(angle)-1))
    pb=np.exp(b*(np.cos(angle)-1))
    pa/=pa.sum();pb/=pb.sum()
    # Probability masses; no analytic Fourier/Bessel coefficients used.
    mass=np.fft.irfft(np.fft.rfft(pa)**2*np.fft.rfft(pb),n=size)
    assert mass.min()>0
    return mass

def divergence(p,q):
    ratio=(p-q)/q
    assert abs(ratio).max()<.5
    # (1+u)log(1+u)-u = sum_{k>=2} (-1)^k u^k/[k(k-1)].
    values=np.zeros_like(ratio)
    for k in range(2,60):values+=(-1)**k*ratio**k/(k*(k-1))
    return float(q@values)

with (OP/"population.csv").open() as f: published=list(csv.DictReader(f))
rows=[]
for c in [1.,2.,4.]:
    for t in [.04,.08,.16]:
        reference=next(r for r in published if float(r["c"])==c and float(r["t"])==t)
        for size in [4096,8192]:
            plus=density(c+t,c-2*t,size)
            minus=density(c-t,c+2*t,size)
            zero=density(c,c,size)
            k4=divergence(plus,zero);k6=divergence(plus,minus)
            rows.append({"c":c,"t":t,"grid":size,"kl_to_diagonal":k4,"kl_between_signs":k6,"relative_error_kl4":abs(k4/float(reference["kl_to_diagonal"])-1),"relative_error_kl6":abs(k6/float(reference["kl_between_signs"])-1)})
err4=max(r["relative_error_kl4"] for r in rows)
err6=max(r["relative_error_kl6"] for r in rows)
assert max(err4,err6)<1e-5
with (HERE/"results/root_kl_audit.csv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
with (OP/"lrt.csv").open() as f:lrt=list(csv.DictReader(f))
total=sum(2*int(r["n"]) for r in lrt)
with (OP/"summary.json").open() as f:report=json.load(f)
assert total==report["generated_pair_count"]
summary={"kl_grid_conditions":len(rows),"max_relative_error_kl4":err4,"max_relative_error_kl6":err6,"lrt_rows":len(lrt),"lrt_truth_datasets":2*len(lrt),"generated_pair_count":total,"note":"Independent deterministic FFT numerical audit; LRT samples not independently rerun"}
(HERE/"results/root_audit.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
