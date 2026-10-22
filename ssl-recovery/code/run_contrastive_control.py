"""Amendment2: exact population infinite-negative InfoNCE with tau=1."""
import copy,json,time
import numpy as np
from run_population import X,ROOT,norm,enc,initialize,law

TAU=1.
def loss_grad(theta,p):
 h,z=enc(theta);f=norm(z);s=f@f.T/TAU;smax=s.max(axis=1,keepdims=True);a=np.exp(s-smax);q=a/a.sum(axis=1,keepdims=True)
 loss=-np.sum(p*s)+np.mean(smax[:,0]+np.log(a.mean(axis=1)))
 ds=-p+q/8;df=(ds+ds.T)@f/TAU
 zn=np.sqrt(np.sum(z*z,axis=1,keepdims=True)+1e-12);dz=df/zn-z*np.sum(df*z,axis=1,keepdims=True)/zn**3
 return float(loss),{'w2':h.T@dz,'w1':X.T@((dz@theta['w2'].T)*(1-h*h))}

def metrics(theta,p):
 f=norm(enc(theta)[1]);c=X.T@f/8;r=np.einsum('ij,jk,ik->i',c,np.linalg.inv(f.T@f/8+.01*np.eye(3)),c)
 return dict(loss=loss_grad(theta,p)[0],**{f'r2_{j+1}':float(v) for j,v in enumerate(r)})
def train(theta,p,steps,m=None,v=None,t=0):
 if m is None:m={k:np.zeros_like(z) for k,z in theta.items()};v=copy.deepcopy(m)
 tr=[dict(step=0,**metrics(theta,p))]
 for it in range(steps):
  _,g=loss_grad(theta,p);t+=1
  for k in theta:
   m[k]=.9*m[k]+.1*g[k];v[k]=.999*v[k]+.001*g[k]**2
   theta[k]-=.003*(m[k]/(1-.9**t))/(np.sqrt(v[k]/(1-.999**t))+1e-8)
  if (it+1)%50==0:tr.append(dict(step=it+1,**metrics(theta,p)))
 return tr,m,v,t

def main():
 start=time.time();theta={k:v for k,v in initialize(34).items() if k!='pred'};p=law((.9,.9,.9));_,g=loss_grad(theta,p);errs=[]
 for k in theta:
  for ind in np.ndindex(theta[k].shape):
   old=theta[k][ind];eps=1e-5;theta[k][ind]=old+eps;lp=loss_grad(theta,p)[0];theta[k][ind]=old-eps;lm=loss_grad(theta,p)[0];theta[k][ind]=old;errs.append(abs(g[k][ind]-(lp-lm)/(2*eps)))
 assert max(errs)<1e-6
 rows=[];summary=[]
 for seed in [0,1,2,3,101,102,103,104]:
  initial={k:v for k,v in initialize(seed).items() if k!='pred'};theta=copy.deepcopy(initial);tr,_,_,_=train(theta,p,3000)
  target=tr[-1]['r2_3'];rows +=[dict(seed=seed,policy='scratch',**r) for r in tr]
  theta=copy.deepcopy(initial);tr,m,v,t=train(theta,law((.9,.9,0)),1500);rows +=[dict(seed=seed,policy='deficit',**r) for r in tr]
  tr,_,_,_=train(theta,p,15000,m,v,t);rows +=[dict(seed=seed,policy='continue',**r) for r in tr]
  hit=None
  for i in range(len(tr)-2):
   if min(r['r2_3'] for r in tr[i:i+3])>=.9*target:hit=tr[i]['step'];break
  summary.append(dict(seed=seed,scratch_final=target,switch_r2=tr[0]['r2_3'],r2_3000=[r for r in tr if r['step']==3000][0]['r2_3'],r2_15000=tr[-1]['r2_3'],t90=hit,all_r2_final=[tr[-1][f'r2_{j}'] for j in [1,2,3]]));print(json.dumps(summary[-1]),flush=True)
 out=dict(seconds=time.time()-start,max_abs_grad_error=max(errs),tau=TAU,summary=summary)
 (ROOT/'results/contrastive_summary.json').write_text(json.dumps(out,indent=2))
 from trace_storage import store_traces
 store_traces('contrastive',rows)
if __name__=='__main__':main()
