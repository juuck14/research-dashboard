"""Exact 8-state BN-free cosine self-distillation; no labels in updates."""
from __future__ import annotations
import argparse, copy, itertools, json, pathlib, platform, time
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[1]
X=np.array(list(itertools.product([-1.,1.],repeat=3)))

def law(rho):
    p=np.prod((1+X[:,None,:]*X[None,:,:]*np.array(rho))/2,axis=2)/8
    return p

def norm(z):
    return z/np.sqrt(np.sum(z*z,axis=1,keepdims=True)+1e-12)

def enc(theta):
    h=np.tanh(X@theta['w1']); z=h@theta['w2']
    return h,z

def loss_grad(theta,teacher,p):
    h,z=enc(theta); q=z@theta['pred']; t=norm(enc(teacher)[1]); u=norm(q)
    loss=2-2*np.sum(p*(u@t.T))
    du=-2*p@t
    qnorm=np.sqrt(np.sum(q*q,axis=1,keepdims=True)+1e-12)
    dq=du/qnorm-q*np.sum(du*q,axis=1,keepdims=True)/qnorm**3
    dz=dq@theta['pred'].T
    g={'pred':z.T@dq,'w2':h.T@dz,'w1':X.T@((dz@theta['w2'].T)*(1-h*h))}
    return float(loss),g

def stats(theta,teacher,p):
    f=norm(enc(theta)[1]); t=norm(enc(teacher)[1]); out={}
    sigma=.1
    for prefix,z in [('f',f),('t',t)]:
        cov=z.T@z/8; c=X.T@z/8
        r2=np.einsum('ij,jk,ik->i',c,np.linalg.inv(cov+sigma**2*np.eye(3)),c)
        sens=np.sum(c*c,axis=1)
        for j in range(3): out[f'{prefix}_r2_{j+1}']=float(r2[j]);out[f'{prefix}_sens_{j+1}']=float(sens[j])
    out['teacher_gap']=float(np.mean(np.sum((f-t)**2,axis=1)))
    out['loss']=loss_grad(theta,teacher,p)[0]
    return out

def initialize(seed):
    rng=np.random.default_rng(seed)
    return {'w1':rng.normal(size=(3,12))/np.sqrt(3),'w2':rng.normal(size=(12,3))/np.sqrt(12),'pred':np.eye(3)+.05*rng.normal(size=(3,3))}

def state(theta):
    return dict(theta=copy.deepcopy(theta),teacher={k:theta[k].copy() for k in ['w1','w2']},m={k:np.zeros_like(v) for k,v in theta.items()},v={k:np.zeros_like(v) for k,v in theta.items()},step=0)

def train(s,p,steps,matched=None):
    traces=[dict(step=0,**stats(s['theta'],s['teacher'],p))]; sizes=[]
    for n in range(steps):
        _,g=loss_grad(s['theta'],s['teacher'],p);s['step']+=1; size={}; gn={}
        for k in s['theta']:
            s['m'][k]=.9*s['m'][k]+.1*g[k];s['v'][k]=.999*s['v'][k]+.001*g[k]**2
            if 'tblocks' in s: s['tblocks'][k]+=1
            kt=s['tblocks'][k] if 'tblocks' in s else s['step']
            u=.003*(s['m'][k]/(1-.9**kt))/(np.sqrt(s['v'][k]/(1-.999**kt))+1e-8)
            if matched is not None: u=u*(matched[n][k]/max(np.linalg.norm(u),1e-30))
            size[k]=float(np.linalg.norm(u));gn[k]=float(np.linalg.norm(g[k]));s['theta'][k]-=u
        for k in s['teacher']:s['teacher'][k]=.99*s['teacher'][k]+.01*s['theta'][k]
        sizes.append(size)
        if (n+1)%50==0:traces.append(dict(step=n+1,**stats(s['theta'],s['teacher'],p),**{f'update_{k}':v for k,v in size.items()},**{f'grad_{k}':v for k,v in gn.items()}))
    return traces,sizes

def reset_opt(s):
    s['step']=0
    for k in s['theta']:s['m'][k]*=0;s['v'][k]*=0

def check():
    theta=initialize(34); teacher=state(initialize(74))['teacher'];p=law((.9,.9,.9));_,g=loss_grad(theta,teacher,p);err=[]
    for k in theta:
        for ind in np.ndindex(theta[k].shape):
            old=theta[k][ind];h=1e-5;theta[k][ind]=old+h;lp=loss_grad(theta,teacher,p)[0];theta[k][ind]=old-h;lm=loss_grad(theta,teacher,p)[0];theta[k][ind]=old
            err.append(abs(g[k][ind]-(lp-lm)/(2*h)))
    marg=0.;cor=0.
    for rho in [( .9,.9,0),(.9,.9,.9)]:
        q=law(rho);marg=max(marg,np.max(abs(q.sum(axis=0)-1/8)),np.max(abs(q.sum(axis=1)-1/8)));cor=max(cor,np.max(abs(X.T@q@X-np.diag(rho))))
    return {'max_abs_grad_error':float(max(err)),'max_marginal_error':float(marg),'max_correlation_error':float(cor)}

def recovery(trace,target,frac):
    a=[r['f_r2_3'] for r in trace]
    for i in range(len(a)-2):
        if min(a[i:i+3])>=frac*target:return trace[i]['step']
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['pilot','confirmation'],default='pilot');args=ap.parse_args();start=time.time();allrows=[]; summaries=[]; checks=check()
    assert checks['max_abs_grad_error']<1e-6
    seeds=[0,1,2,3] if args.phase=='pilot' else [101,102,103,104]
    p0=law((.9,.9,0));pc=law((.9,.9,.9))
    for seed in seeds:
        theta0=initialize(seed);deficit=state(theta0);deftrace,_=train(deficit,p0,1500)
        scratch=state(theta0);tr,sz=train(scratch,pc,3000);records={'scratch':(tr,sz)}
        cleanlong=state(theta0);tr,sz=train(cleanlong,pc,4500);records['clean_long']=(tr,sz)
        cont=copy.deepcopy(deficit);tr,sz=train(cont,pc,3000);records['continue']=(tr,sz);refs=sz
        for policy in ['optimizer_reset','optimizer_normmatch','teacher_sync','predictor_reset','head_teacher']:
            s=copy.deepcopy(deficit)
            if policy.startswith('optimizer'):reset_opt(s)
            if policy in ['teacher_sync','head_teacher']:
                for k in s['teacher']:s['teacher'][k]=s['theta'][k].copy()
            if policy in ['predictor_reset','head_teacher']:s['theta']['pred']=theta0['pred'].copy()
            records[policy]=train(s,pc,3000,matched=refs if policy=='optimizer_normmatch' else None)
        for row in deftrace:allrows.append(dict(seed=seed,policy='deficit',**row))
        target=records['scratch'][0][-1]['f_r2_3']
        for policy,(tr,sz) in records.items():
            for row in tr:allrows.append(dict(seed=seed,policy=policy,**row))
            sm=dict(seed=seed,policy=policy,initial_r2=tr[0]['f_r2_3'],final_r2=tr[-1]['f_r2_3'],scratch_target=target,recovery={str(frac):recovery(tr,target,frac) for frac in [.8,.9,.95]},mean_update={k:float(np.mean([r[k] for r in sz])) for k in sz[0]});summaries.append(sm)
        print(json.dumps({'seed':seed,'summaries':summaries[-8:]}),flush=True)
    out={'phase':args.phase,'checks':checks,'seeds':seeds,'seconds':time.time()-start,'environment':{'python':platform.python_version(),'numpy':np.__version__},'summary':summaries}
    path=ROOT/'results';path.mkdir(exist_ok=True)
    from trace_storage import store_traces
    out['trace_manifest']=store_traces(args.phase,allrows)
    (path/f'{args.phase}_summary.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out),flush=True)
if __name__=='__main__':main()
