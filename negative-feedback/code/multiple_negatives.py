"""N2 exact multinomial enumeration; no Monte Carlo / cherry-picked seed."""
from pathlib import Path
import itertools,csv,json
import numpy as np
from scipy.special import gammaln,logsumexp,softmax
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results'
def compositions(k):
 return np.array([(a,b,c,k-a-b-c) for a in range(k+1) for b in range(k-a+1) for c in range(k-a-b+1)],float)
def q_at(t,kappa,eps):
 s=np.array([1,np.cos(2*t),-np.cos(2*t),-1]);soft=softmax(kappa*s);return s,eps/4+(1-eps)*soft

def calc(t,kappa,eps,K,qfixed=None):
 s,q=q_at(t,kappa,eps);q=q if qfixed is None else qfixed
 counts=compositions(K);logcoef=gammaln(K+1)-gammaln(counts+1).sum(axis=1)
 prob=np.exp(logcoef+(counts*np.log(q)).sum(axis=1));exp=np.exp(s-1);den=1+counts@exp
 ds=np.array([0,-2*np.sin(2*t),2*np.sin(2*t),0]);g=(counts@(exp*ds))/den
 return float(prob@g),float(prob.sum())
def run():
 rows=[]
 for K,e,k in itertools.product([1,2,4,8,16],[.01,.1,.5],[-8,-4,-2,-1,-.5,0,2]):
  theta=np.pi/4;s,q=q_at(theta,k,e);cts=compositions(K);lp=gammaln(K+1)-gammaln(cts+1).sum(axis=1)+(cts*np.log(q)).sum(axis=1);prob=np.exp(lp)
  den=1+cts@np.exp(s-1);diff=cts[:,2]-cts[:,1];n=cts[:,1]+cts[:,2];r=np.exp(-1)
  hf=float(prob@(4*r*n/den-4*r*r*diff*diff/den**2))
  sm0=1/(2+2*np.cosh(k));fb=float(4*(1-e)*k*sm0/q[1]*r*(prob@(diff*diff/den)))
  h=1e-5;fda=(calc(theta+h,k,e,K)[0]-calc(theta-h,k,e,K)[0])/(2*h);fdf=(calc(theta+h,k,e,K,q)[0]-calc(theta-h,k,e,K,q)[0])/(2*h)
  rows.append(dict(K=K,eps=e,kappa=k,H_frozen=hf,H_adaptive=hf+fb,feedback=fb,fd_error=max(abs(hf-fdf),abs(hf+fb-fda)),prob_sum=float(prob.sum()),compositions=len(cts)))
 assert max(r['fd_error'] for r in rows)<1e-5
 with (OUT/'multi_negative_curvature.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary=dict(settings=len(rows),max_fd_error=max(r['fd_error'] for r in rows),max_probability_sum_error=max(abs(r['prob_sum']-1) for r in rows),main_case=[r for r in rows if r['eps']==.1 and r['kappa']==-2],n_adaptive_unstable=sum(r['H_adaptive']<0 for r in rows))
 (OUT/'multi_negative_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
