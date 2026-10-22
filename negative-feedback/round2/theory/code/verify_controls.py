"""Fixed post-proof natural-policy and decoupled-denominator controls.
Run from repository root; imports exact count utilities only from verify_general.
"""
from pathlib import Path
import csv,json
import numpy as np
from scipy.linalg import null_space
from verify_general import counts3,counts4,A,B,F0
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results'

def params(kind):
    if kind=='natural':return np.log(4.),.3,0.
    if kind=='matched':return 2.,.1,-.9
    raise ValueError(kind)
def policy(f,kind):
    t,eps,alpha=params(kind);s=f@f.T
    z=np.exp(-t*s+alpha*s*(s*s-1))
    return eps/4+(1-eps)*z/z.sum(axis=1,keepdims=True)
def moments(K,kind,positive):
    t,eps,alpha=params(kind);soft=np.array([np.exp(-t),1,np.exp(t)])/(np.exp(-t)+2+np.exp(t))
    q=np.array([eps/4+(1-eps)*soft[0],2*(eps/4+(1-eps)*soft[1]),eps/4+(1-eps)*soft[2]])
    u,v,w=q[0],q[1]/2,q[2];g=(1-eps)*soft[1]*(-t-alpha)
    ct,coef=counts3(K);p=np.exp(coef+ct@np.log(q));U,N,W=ct.T
    D=positive+U+A*N+B*W;E=lambda x:float(p@x)
    M=E(N/D);R=E(N/D**2)/M;C=E(W/D);S=U*soft[0]/u+N*soft[1]/v+W*soft[2]/w
    bf=A*M-A*A*E(N/D**2);ba=bf+A*g*M/v
    pf=A*M/2-A*A*E((N*N+N)/D**2)/4+B*C
    pa=pf+A*g*(E((N*N+N)/D)/(4*v)-E(N*S/D)/2)
    np_=A*M/2+B*C;nm=-A*M/2+B*C
    return {'K':K,'kind':kind,'positive':positive,'u':u,'v':v,'w':w,'g':g,'eta':-g/v,
            'threshold':1-A*R,'frozen_balance':bf,'adaptive_balance':ba,'frozen_ab':pf,'adaptive_ab':pa,
            'normal_one':np_,'normal_ab':nm,'prob_sum':float(p.sum()),
            'full_adaptive_stable':bool(min(ba,pa,np_,nm)>1e-10)}
def field(f,K,kind,positive,qfixed=None):
    f=f/np.linalg.norm(f,axis=1,keepdims=True);q=policy(f,kind) if qfixed is None else qfixed
    ct,coef=counts4(K);s=f@f.T;co=np.zeros((4,4))
    for i in range(4):
        prob=np.exp(coef+ct@np.log(q[i]));e=np.exp(s[i]-1);D=positive+ct@e
        co[i]=(prob[:,None]*ct*e[None,:]/D[:,None]).sum(axis=0)/4
    grad=(co+co.T)@f
    return grad-(grad*f).sum(axis=1,keepdims=True)*f
def check(K,kind,positive):
    f=F0.copy();basis=[null_space(z[None,:]) for z in f];q=policy(f,kind);h=1e-5
    m=moments(K,kind,positive);res=[]
    for name in ['frozen','adaptive']:
        fun=lambda x:field(x,K,kind,positive,q if name=='frozen' else None)
        J=np.zeros((12,12))
        for j in range(12):
            i,r=divmod(j,3);z=np.zeros_like(f);z[i]=basis[i][:,r]
            v=(fun(f+h*z)-fun(f-h*z))/(2*h)
            J[:,j]=np.concatenate([basis[i].T@v[i] for i in range(4)])
        eig=np.linalg.eigvals(J)
        assert np.abs(eig.imag).max()<1e-7
        expected=np.sort([m[name+'_balance']]+[m[name+'_ab']]*2+[m['normal_one']]*2+[m['normal_ab']]*2+[0]*5)
        res.append(float(np.abs(np.sort(eig.real)-expected).max()))
    return {'K':K,'kind':kind,'positive':positive,'frozen_error':res[0],'adaptive_error':res[1]}
def write(name,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
    rows=[moments(K,kind,pos) for kind in ['natural','matched'] for pos in [0,1] for K in range(1,129)]
    checks=[check(K,kind,pos) for K in [1,2,4,8,16] for kind in ['natural','matched'] for pos in [0,1]]
    assert max(r['frozen_error'] for r in checks)<2e-7
    assert max(r['adaptive_error'] for r in checks)<2e-7
    groups=[]
    for kind in ['natural','matched']:
        selected={pos:[r for r in rows if r['kind']==kind and r['positive']==pos] for pos in [0,1]}
        assert all(r1['threshold']>r0['threshold'] for r0,r1 in zip(selected[0],selected[1]))
        for pos,s in selected.items():
            ts=np.array([r['threshold'] for r in s]);assert np.all(np.diff(ts)>0)
            stable=[r['K'] for r in s if r['full_adaptive_stable']]
            cutoff=min(stable) if stable else None
            groups.append({'kind':kind,'positive':pos,'eta':s[0]['eta'],'first_stable_K':cutoff,
              'q':{key:s[0][key] for key in ['u','v','w']},'T1':s[0]['threshold'],'T128':s[-1]['threshold'],
              'before':s[cutoff-2] if cutoff and cutoff>1 else None,'at':s[cutoff-1] if cutoff else None})
    write('denominator_controls.csv',rows);write('denominator_fd.csv',checks)
    summary={'groups':groups,'full_tangent_checks':len(checks),
       'max_frozen_error':max(r['frozen_error'] for r in checks),
       'max_adaptive_error':max(r['adaptive_error'] for r in checks)}
    (OUT/'denominator_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
