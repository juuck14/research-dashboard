from pathlib import Path
import json,csv
import numpy as np
from scipy.special import gammaln
from verify_multilevel import curvature,critical
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
rows=[];t=np.log(4.)
for m in [2,3,4,8,16,32,128]:
    r=np.arange(m+1);s=(m-2*r)/m
    p=np.exp(gammaln(m+1)-gammaln(r+1)-gammaln(m-r+1)-m*np.log(2))
    h2=8*r*(m-r)/(m*(m-1));ec=critical(s,h2,p,t)
    for eps in [.25,.3]:
        row={'m':m,'t':float(t),'eps':eps,'critical_floor':float(ec),'analytic_eventual_stability':bool(eps>ec)}
        def H(K):return float(curvature(s,h2,p,t,eps,1,[K])[0][0])
        if eps<=ec:
            row.update(first_positive_K=None,last_negative_K=None,last_negative_margin=None,first_positive_margin=None,
                       H1=H(1),H64=H(64),classification='all finite K negative by theorem')
        else:
            high=1
            while high<=8192 and H(high)<=0:high*=2
            assert high<=8192
            low=0 if high==1 else high//2
            while high-low>1:
                mid=(high+low)//2
                if H(mid)>0:high=mid
                else:low=mid
            row.update(first_positive_K=high,last_negative_K=low,last_negative_margin=H(low) if low else None,
                       first_positive_margin=H(high),H1=H(1),H64=H(64),classification='onset numerically bracketed; all-K order from theorem')
        rows.append(row)
with (OUT/'fixed_floor_predictions.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
A=np.exp(-1);eps=.3
threshold=1/(1-t*(1-eps))-1/A
summary={'fixed_K_high_factor_first_positive':int(np.floor(threshold)+1),'limiting_continuous_K_boundary':float(threshold),
         't':float(t),'eps':eps,'large_factor_critical_floor':float(1-1/t),'rows':rows}
(OUT/'fixed_floor_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
