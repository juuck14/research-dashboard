"""Shared nonlinear encoder test, with explicit NumPy backprop and detached sampling."""
from pathlib import Path
from itertools import product
import copy,csv,json,time,platform
import numpy as np
import scipy,matplotlib
from scipy.special import expit,softmax
from scipy.linalg import solve

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
BITS=np.array(list(product([-1.,1.],repeat=2)))
RNG=np.random.default_rng(916)
Q=np.linalg.qr(RNG.normal(size=(16,16)))[0]
CFG=dict(input_dim=16,hidden=32,output=8,batch=64,lr=.05,warmup_steps=1000,fork_steps=3000,
         epsilon=.1,kappa=-2.,nuisance_sd=.25,feature_noise=.05,primary=[1101,1102,1103],confirmation=[2201,2202,2203])
(ROOT/'config.json').write_text(json.dumps(CFG,indent=2)+'\n')

def render(bits,rng):
    s=np.concatenate([bits,rng.normal(scale=CFG['nuisance_sd'],size=(len(bits),14))],axis=1)
    u=s@Q.T
    return u+.1*np.tanh(u)**3

def batch(rng,n=64):
    bits=rng.integers(0,2,size=(n,2))*2.-1.
    return render(bits,rng),render(bits,rng)

def eval_data(seed,n):
    bits=np.tile(BITS,(n//4,1))
    return render(bits,np.random.default_rng(seed)),bits

XTRAIN,YTRAIN=eval_data(7001,512)
XTEST,YTEST=eval_data(7002,2048)
XTRACE,YTRACE=eval_data(7003,256)

def random_params(seed):
    rng=np.random.default_rng(seed)
    return {'W1':rng.normal(size=(16,32))/4,'b1':rng.normal(scale=.1,size=32),
            'W2':rng.normal(size=(32,8))/np.sqrt(32),'b2':rng.normal(scale=.02,size=8)}

def pca_params(seed):
    rng=np.random.default_rng(seed)
    x,_=eval_data(8011,2048)
    vals,vec=np.linalg.eigh(np.cov(x,rowvar=False,bias=True))
    pc=vec[:,-2:]/np.sqrt(vals[-2:])[None,:]
    p={'W1':rng.normal(scale=.05,size=(16,32)),'b1':rng.normal(scale=.05,size=32),
       'W2':rng.normal(scale=.001,size=(32,8)),'b2':np.zeros(8)}
    p['W1'][:,:2]=.5*pc;p['W1'][:,2:4]=-.5*pc;p['b1'][:4]=0.
    p['W2'][:4]=0.;p['W2'][0,0]=1.;p['W2'][2,0]=-1.;p['W2'][1,1]=1.;p['W2'][3,1]=-1.
    return p

def forward(x,p):
    h=np.tanh(x@p['W1']+p['b1'])
    y=h@p['W2']+p['b2'];n=np.linalg.norm(y,axis=1,keepdims=True)
    if np.min(n)<1e-10: raise FloatingPointError('nearzero pre-normalization vector')
    f=y/n
    return f,(x,h,f,n)

def backward(df,cache,p):
    x,h,f,n=cache
    dy=(df-np.sum(df*f,axis=1,keepdims=True)*f)/n
    dh=(dy@p['W2'].T)*(1-h*h)
    return {'W1':x.T@dh,'b1':dh.sum(axis=0),'W2':h.T@dy,'b2':dy.sum(axis=0)}

def sampler(s,policy):
    n=len(s);mask=np.eye(n,dtype=bool)
    if policy=='uniform':q=np.full_like(s,1/(n-1));q[mask]=0.;return q
    logits=CFG['kappa']*s.copy();logits[mask]=-np.inf
    q=(1-CFG['epsilon'])*softmax(logits,axis=1)+CFG['epsilon']/(n-1)
    q[mask]=0.;return q

def lossgrad(x1,x2,p,policy,frozen=None,q_override=None,need_grad=True):
    f1,c1=forward(x1,p);f2,c2=forward(x2,p);s=f1@f2.T
    if q_override is not None:q=q_override
    elif policy=='frozen':
        z1,_=forward(x1,frozen);z2,_=forward(x2,frozen);q=sampler(z1@z2.T,'adaptive')
    else:q=sampler(s,policy)
    delta=s-np.diag(s)[:,None]
    value=float(np.sum(q*np.logaddexp(0,delta))/len(s))
    if not need_grad:return value
    ds=q*expit(delta)/len(s)
    ds[np.diag_indices(len(s))]-=ds.sum(axis=1)
    g1=backward(ds@f2,c1,p);g2=backward(ds.T@f1,c2,p)
    return value,{k:g1[k]+g2[k] for k in p}

def gradient_check():
    p=random_params(123);rng=np.random.default_rng(124);x1,x2=batch(rng,9)
    f1,_=forward(x1,p);f2,_=forward(x2,p);q=sampler(f1@f2.T,'adaptive')
    value,g=lossgrad(x1,x2,p,'adaptive',q_override=q)
    coords=[(k,i) for k,v in p.items() for i in range(v.size)]
    selected=rng.choice(len(coords),size=50,replace=False)
    errors=[]
    for ix in selected:
        k,i=coords[ix];old=p[k].flat[i];h=1e-6
        p[k].flat[i]=old+h;a=lossgrad(x1,x2,p,'adaptive',q_override=q,need_grad=False)
        p[k].flat[i]=old-h;b=lossgrad(x1,x2,p,'adaptive',q_override=q,need_grad=False)
        p[k].flat[i]=old
        fd=(a-b)/(2*h);an=float(g[k].flat[i]);errors.append({'parameter':k,'index':i,'analytic':an,'fd':fd,'abs_error':abs(fd-an)})
    maximum=max(e['abs_error'] for e in errors)
    result={'coordinates':len(errors),'max_absolute_error':maximum,'passed':maximum<1e-6,'loss':value,'checks':errors}
    (OUT/'gradient_check.json').write_text(json.dumps(result,indent=2)+'\n')
    assert result['passed'],result
    return result

def linear_probe(x,y,z):
    mx=x.mean(axis=0);my=y.mean(axis=0);xc=x-mx
    w=np.linalg.solve(xc.T@xc/len(x)+.001*np.eye(x.shape[1]),xc.T@(y-my)/len(x))
    pred=(z-mx)@w+my
    return np.mean((pred>0)==(YTEST>0),axis=0)

def rbf_probe(x,y,z):
    d=np.maximum(np.sum(x*x,axis=1)[:,None]+np.sum(x*x,axis=1)[None,:]-2*x@x.T,0.)
    bandwidth=float(np.median(d[~np.eye(len(x),dtype=bool)]));bandwidth=max(bandwidth,1e-8)
    k=np.exp(-d/bandwidth)
    alpha=solve(k+.001*len(x)*np.eye(len(x)),y,assume_a='pos')
    dz=np.maximum(np.sum(z*z,axis=1)[:,None]+np.sum(x*x,axis=1)[None,:]-2*z@x.T,0.)
    pred=np.exp(-dz/bandwidth)@alpha
    return np.mean((pred>0)==(YTEST>0),axis=0)

def geometry(f,y):
    means=np.stack([f[np.all(y==b,axis=1)].mean(axis=0) for b in BITS])
    coeff=np.concatenate([np.ones((4,1)),BITS,np.prod(BITS,axis=1)[:,None]],axis=1).T@means/4
    en=np.sum(coeff*coeff,axis=1)
    return {'class_means':means.tolist(),'gram':(means@means.T).tolist(),'gram_eigenvalues':np.linalg.eigvalsh(means@means.T).tolist(),
            'walsh_energy_1_a_b_ab':en.tolist(),'interaction_fraction':float(en[3]/max(en[1:].sum(),1e-20))}

def evaluate(p,heavy=True):
    ft,_=forward(XTRAIN,p);fz,_=forward(XTEST,p)
    acc=linear_probe(ft,YTRAIN,fz)
    result={'linear_a':float(acc[0]),'linear_b':float(acc[1]),'worst_linear':float(acc.min())}
    if heavy:
        a=rbf_probe(ft,YTRAIN,fz)
        rng=np.random.default_rng(9031);nt=ft+CFG['feature_noise']*rng.normal(size=ft.shape);nz=fz+CFG['feature_noise']*rng.normal(size=fz.shape)
        na=linear_probe(nt,YTRAIN,nz);nb=rbf_probe(nt,YTRAIN,nz)
        result.update(rbf_a=float(a[0]),rbf_b=float(a[1]),worst_rbf=float(a.min()),noise_linear_a=float(na[0]),noise_linear_b=float(na[1]),worst_noise_linear=float(na.min()),noise_rbf_a=float(nb[0]),noise_rbf_b=float(nb[1]),worst_noise_rbf=float(nb.min()))
    result['geometry']=geometry(fz,YTEST)
    return result

def raw_oracle():
    z=XTEST.copy()
    for _ in range(8):
        t=np.tanh(z);z-=(z+.1*t**3-XTEST)/(1+.3*t*t*(1-t*t))
    source=z@Q
    return np.mean((source[:,:2]>0)==(YTEST>0),axis=0).tolist()

def step(p,g):
    for k in p:p[k]-=CFG['lr']*g[k]

def train(p,seed,policy,steps,frozen=None):
    rng=np.random.default_rng(seed);trace=[]
    for it in range(steps):
        x1,x2=batch(rng,CFG['batch']);value,g=lossgrad(x1,x2,p,policy,frozen)
        step(p,g)
        if not np.isfinite(value):raise FloatingPointError('nonfinite loss')
        if (it+1)%500==0:
            f,_=forward(XTRACE,p);geom=geometry(f,YTRACE)
            trace.append({'step':it+1,'loss':value,'interaction_fraction':geom['interaction_fraction'],'factor_energy_a':geom['walsh_energy_1_a_b_ab'][1],'factor_energy_b':geom['walsh_energy_1_a_b_ab'][2]})
    return p,trace

def write_rows(rows):
    flat=[]
    for r in rows:flat.append({k:v for k,v in r.items() if k not in ['geometry','trace']})
    if flat:
        with (OUT/'runs.csv').open('w') as f:
            w=csv.DictWriter(f,fieldnames=flat[0]);w.writeheader();w.writerows(flat)
    (OUT/'runs.json').write_text(json.dumps(rows,indent=2)+'\n')

def main():
    started=time.time();check=gradient_check();rows=[];warmups=[];models={};errors=[]
    print(json.dumps({'gradient_error':check['max_absolute_error'],'raw_oracle':raw_oracle()}),flush=True)
    for seed in CFG['primary']+CFG['confirmation']:
        for arm in ['warmup','pca']:
            p=random_params(seed) if arm=='warmup' else pca_params(seed)
            if arm=='warmup':p,tr=train(p,seed+10000,'uniform',CFG['warmup_steps'])
            initial=evaluate(p,heavy=False)
            warmups.append({'seed':seed,'arm':arm,**initial})
            (OUT/'initial_geometry.json').write_text(json.dumps(warmups,indent=2)+'\n')
            if arm=='warmup' and initial['worst_linear']<.95:
                errors.append({'seed':seed,'arm':arm,'reason':'warmup prerequisite failed','accuracy':initial['worst_linear']})
                print(json.dumps(errors[-1]),flush=True);continue
            frozen=copy.deepcopy(p)
            for policy in ['uniform','frozen','adaptive']:
                model,trace=train(copy.deepcopy(p),seed+20000,policy,CFG['fork_steps'],frozen)
                metric=evaluate(model,heavy=True)
                row={'seed':seed,'split':'primary' if seed in CFG['primary'] else 'confirmation','arm':arm,'policy':policy,**metric,'trace':trace}
                rows.append(row);models[f'{seed}/{arm}/{policy}']={k:v.tolist() for k,v in model.items()}
                write_rows(rows);(OUT/'models.json').write_text(json.dumps(models)+'\n')
                print(json.dumps({k:v for k,v in row.items() if k not in ['geometry','trace']}),flush=True)
    summary={'gradient_max_error':check['max_absolute_error'],'raw_oracle':raw_oracle(),'runs':len(rows),'warmup_failures':errors,'elapsed_seconds':time.time()-started,'criteria':{}}
    for arm in ['warmup','pca']:
        for split in ['primary','confirmation']:
            subset=[r for r in rows if r['arm']==arm and r['split']==split];seeds=sorted({r['seed'] for r in subset});passed=0
            for seed in seeds:
                by={r['policy']:r for r in subset if r['seed']==seed}
                passed+=by['frozen']['worst_linear']-by['adaptive']['worst_linear']>=.15 and by['frozen']['worst_noise_linear']-by['adaptive']['worst_noise_linear']>=.20
            summary['criteria'][arm+'/'+split]={'passed':int(passed),'total':len(seeds)}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (OUT/'environment.json').write_text(json.dumps({'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__,'platform':platform.platform(),'machine':platform.machine(),'training_command':'OPENBLAS_NUM_THREADS=1 python negative-feedback/round2/encoder/run_encoder.py','threads':'OPENBLAS_NUM_THREADS=1','accelerator':'CPU; no torch or GPU used'},indent=2)+'\n')
    print(json.dumps(summary),flush=True)

if __name__=='__main__':main()
