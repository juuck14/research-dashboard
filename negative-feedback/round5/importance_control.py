"""Independent exact tuple intervention; no inherited scientific oracle imports."""
from pathlib import Path
from itertools import product
import json, numpy as np

ROOT=Path(__file__).resolve().parent
C=4;EPS=.05;T=np.log(4.)
BITS=np.array(list(product([-1.,1.],repeat=2)))
ETF=np.column_stack([BITS,BITS[:,0]*BITS[:,1],np.zeros(C)])/np.sqrt(3.)
COARSE=np.zeros((C,C));COARSE[:2,0]=1;COARSE[2:,0]=-1
PI=(np.ones((C,C))-np.eye(C))/(C-1)

def norm(f):return f/np.linalg.norm(f,axis=1,keepdims=True)
def policy(f):
    w=np.exp(-T*(f@f.T));np.fill_diagonal(w,0)
    return EPS*PI+(1-EPS)*w/w.sum(axis=1,keepdims=True)

def exact(f,K,mode):
    f=norm(f);s=f@f.T;q=policy(f)
    co=np.zeros((C,C));loss=0.
    for i in range(C):
        candidates=[j for j in range(C) if j!=i]
        ix=np.array(list(product(candidates,repeat=K)),int)
        source=np.prod(q[i,ix],axis=1)
        if mode=='uniform':prob=np.prod(PI[i,ix],axis=1)
        elif mode=='corrected':prob=source*np.prod(PI[i,ix]/q[i,ix],axis=1)
        else:prob=source
        w=np.exp(s[i,ix]-1);D=1+w.sum(axis=1)
        loss+=float(prob@np.log(D))/C
        for r in range(K):
            np.add.at(co[i],ix[:,r],prob*w[:,r]/D/C)
    g=(co+co.T)@f
    g-=np.sum(g*f,axis=1,keepdims=True)*f
    return loss,g

def shape(delta):
    return np.column_stack([np.sqrt(1/3+delta)*BITS[:,0],
                            np.sqrt(1/3-delta)*BITS[:,1],
                            BITS[:,0]*BITS[:,1]/np.sqrt(3),np.zeros(C)])

rng=np.random.default_rng(8151)
states={'etf':ETF,'perturbed_etf':norm(ETF+.013*rng.normal(size=ETF.shape)),
        'coarse':COARSE,'perturbed_coarse':norm(COARSE+.013*rng.normal(size=COARSE.shape))}
rows=[];shape_rows=[]
for name,f in states.items():
    for K in [1,2,3]:
        lu,gu=exact(f,K,'uniform');la,ga=exact(f,K,'adaptive');lc,gc=exact(f,K,'corrected')
        rows.append({'state':name,'K':K,'uniform_loss':lu,'adaptive_composed_loss':la,
                     'corrected_expected_loss':lc,'corrected_field_error':float(np.max(np.abs(gc-gu))),
                     'corrected_loss_error':abs(lc-lu),'adaptive_vs_uniform_field':float(np.linalg.norm(ga-gu))})
for K in [1,2,3]:
    h=3e-6;z=np.column_stack([np.sqrt(3)/2*BITS[:,0],-np.sqrt(3)/2*BITS[:,1],np.zeros((C,2))])
    a=np.exp(-C/(C-1));D=1+K*a;threshold=1-a/D
    for mode in ['adaptive','uniform','corrected']:
        dg=(exact(shape(h),K,mode)[1]-exact(shape(-h),K,mode)[1])/(2*h)
        observed=float(np.sum(dg*z)/np.sum(z*z))
        eta=T*(1-EPS) if mode=='adaptive' else 0.
        expected=4*K*a/((C-1)**2*D)*(threshold-eta)
        shape_rows.append({'K':K,'mode':mode,'observed_shape_eigenvalue':observed,
                           'predicted':expected,'abs_error':abs(observed-expected)})
summary={'rows':rows,'shape_checks':shape_rows,
         'max_corrected_field_error':max(r['corrected_field_error'] for r in rows),
         'max_shape_error':max(r['abs_error'] for r in shape_rows),
         'composed_risk_caveat':'ETF is the global optimum of the fixed uniform law. The composed adaptive risk can prefer coarse collapse; no unchanged-objective optimizer-failure claim is made.',
         'scope':'known product importance identity and independent exact gradient intervention; not a novel method'}
assert summary['max_corrected_field_error']<1e-12
assert summary['max_shape_error']<1e-7
(ROOT/'importance_control.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({'max_corrected_field_error':summary['max_corrected_field_error'],
                  'max_shape_error':summary['max_shape_error'],
                  'K1_composed_ETF':rows[0]['adaptive_composed_loss'],
                  'K1_composed_coarse':next(r['adaptive_composed_loss'] for r in rows if r['state']=='coarse' and r['K']==1)},indent=2))
