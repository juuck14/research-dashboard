from pathlib import Path
import json,numpy as np
from oracle import normalize,policy,loss_gradient,direct4,field
OUT=Path(__file__).resolve().parent/'results'
rng=np.random.default_rng(3411);rows=[]
for K in [1,2,4,5,8,16]:
    f=normalize(rng.normal(size=(4,5)));q=policy(f);P=rng.dirichlet(np.ones(4),size=4)
    vd,gd=direct4(f,P,K,q)
    for L in [64,96,128]:
        v,g=loss_gradient(f,P,K,q,L)
        rows.append({'K':K,'L':L,'value_error':abs(v-vd),'gradient_error':float(np.max(np.abs(g-gd)))})
f=normalize(rng.normal(size=(16,8)));P=np.kron(np.eye(4),np.ones((4,4))/4);q=policy(f)
conv=[]
for K in [1,2,4,5,8,16]:
    v0,g0=loss_gradient(f,P,K,q,96);v1,g1=loss_gradient(f,P,K,q,128)
    conv.append({'K':K,'value_error':abs(v0-v1),'gradient_error':float(np.max(np.abs(g0-g1)))})
fd=[];v,g=loss_gradient(f,P,5,q,128)
for _ in range(20):
    i,j=rng.integers(16),rng.integers(8);h=1e-6;a=f.copy();b=f.copy();a[i,j]+=h;b[i,j]-=h
    vf=(loss_gradient(a,P,5,q,128)[0]-loss_gradient(b,P,5,q,128)[0])/(2*h)
    fd.append(abs(vf-g[i,j]))
summary={'direct':rows,'node_convergence':conv,'max_fd_error':max(fd),'passed':bool(max([r['value_error'] for r in rows]+[r['gradient_error'] for r in rows]+[r['gradient_error'] for r in conv]+fd)<1e-7)}
(OUT/'oracle_validation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2));assert summary['passed']
