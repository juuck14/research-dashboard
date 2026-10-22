"""N1 follow-up registered after base model falsification. Exact population."""
import csv,json,itertools
from pathlib import Path
import numpy as np
from scipy.special import expit,softmax,ndtr
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results'
X=np.array(list(itertools.product([-1.,1.],repeat=2)));A=X[:,None,0]*X[None,:,0];B=X[:,None,1]*X[None,:,1]
def quantities(t,k,e):
 s=np.cos(t)**2*A+np.sin(t)**2*B
 d=np.sin(2*t)*(B-A)
 sm=softmax(k*s,axis=1);q=e/4+(1-e)*sm
 return s,d,q

def grad(t,k,e,policy,qfixed=None):
 s,d,q=quantities(t,k,e)
 if policy=='frozen':q=qfixed
 if policy=='uniform':q=np.full((4,4),.25)
 return np.sum(q*expit(s-1)*d)/4

def run():
 center=np.pi/4;curves=[]
 for e,k in itertools.product([.01,.1,.5],[-8,-4,-2,-1,-.5,0,2]):
  z=2+2*np.cosh(k);sm0=1/z;q0=e/4+(1-e)*sm0;sg=expit(-1)
  hf=8*q0*sg*(1-sg);ha=hf+8*(1-e)*k*sm0*sg
  qcenter=quantities(center,k,e)[2];h=1e-5
  fda=(grad(center+h,k,e,'adaptive')-grad(center-h,k,e,'adaptive'))/(2*h)
  fdf=(grad(center+h,k,e,'frozen',qcenter)-grad(center-h,k,e,'frozen',qcenter))/(2*h)
  curves.append(dict(eps=e,kappa=k,H_frozen=hf,H_adaptive=ha,fd_adaptive=fda,fd_frozen=fdf,feedback_term=ha-hf))
 assert max(abs(r['H_adaptive']-r['fd_adaptive']) for r in curves)<1e-6
 assert max(abs(r['H_frozen']-r['fd_frozen']) for r in curves)<1e-6
 rows=[];plot={}
 for e,k,offset,seed in itertools.product([.01,.1,.5],[-8,-4,-2,-1,-.5,0,2],[-1e-3,1e-3,-1e-5,1e-5],[101,211]):
  t0=center+offset*(1+np.random.default_rng(seed).uniform(-.02,.02));qinit=quantities(t0,k,e)[2];qc=quantities(center,k,e)[2]
  for policy in ['adaptive','frozen_initial','frozen_center','uniform']:
   pol='frozen' if policy.startswith('frozen') else policy
   q=qc if policy=='frozen_center' else qinit
   sol=solve_ivp(lambda t,y:[-grad(y[0],k,e,pol,q)],[0,200],[t0],rtol=1e-9,atol=1e-12,dense_output=True)
   end=float(sol.y[0,-1]);amp=min(abs(np.sin(end)),abs(np.cos(end)))
   rows.append(dict(eps=e,kappa=k,offset=offset,seed=seed,policy=policy,theta0=t0,theta_final=end,smaller_factor_amplitude=amp,noisy_probe_accuracy=float(ndtr(amp/.01))))
   if e==.1 and k==-2 and offset==1e-3 and seed==101:
    tt=np.linspace(0,200,500);plot[policy]=(tt,sol.sol(tt)[0])
 for name,data in [('normalized_curvature.csv',curves),('normalized_runs.csv',rows)]:
  with (OUT/name).open('w') as f:w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 fig,ax=plt.subplots(figsize=(7,4))
 for p,(t,v) in plot.items():ax.plot(t,v,label=p)
 ax.axhline(center,color='gray',ls=':');ax.set(xlabel='gradient-flow time',ylabel='factor angle theta',title='Same initial factors: adaptive vs frozen sampler');ax.legend();fig.tight_layout();fig.savefig(OUT/'normalized_feedback.png',dpi=160);fig.savefig(OUT/'normalized_feedback.svg');plt.close(fig)
 summary=dict(n_runs=len(rows),max_jacobian_error=max(abs(r['H_adaptive']-r['fd_adaptive']) for r in curves),main_case=[r for r in curves if r['eps']==.1 and r['kappa']==-2][0],main_trajectories=[r for r in rows if r['eps']==.1 and r['kappa']==-2 and r['offset']==1e-3 and r['seed']==101])
 (OUT/'normalized_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
