"""Continuous product-S2 law: moment, density and independent tuple checks."""
from pathlib import Path
import csv,json
import numpy as np
from numpy.polynomial.legendre import leggauss
from verify_multilevel import curvature,critical,policy

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
t=np.log(4.)

def write(name,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def moment(a):
    z,w=leggauss(96);e=np.exp(a*z);w=w/2
    return np.array([np.sum(w*e*z**j) for j in range(3)])

def L(m,c):
    M,D,D2=moment(c/m)
    return 2*(D2*M-D*D)*M**(m-2)

floors=[];moment_errors=[]
for m in [2,3,4,8,16,32,128]:
    Z=moment(t/m)[0]**m
    aa=(t-1)*L(m,1-t);bb=Z*L(m,1)
    ec=aa/(aa+bb)
    a=t/m
    exactM=np.sinh(a)/a
    exactD=(a*np.cosh(a)-np.sinh(a))/a**2
    exactD2=((a*a+2)*np.sinh(a)-2*a*np.cosh(a))/a**3
    moment_errors.append(float(np.max(np.abs(moment(a)-[exactM,exactD,exactD2]))))
    for eps in [.25,.3]:
        floors.append({'factor_count':m,'sphere_r':3,'eps':eps,'critical_floor':float(ec),
                       'analytic_eventual_stability':bool(eps>ec),'limit_floor':float(1-1/t)})

curverows=[];values={};density_errors=[]
for n in [96,192]:
    x,w=leggauss(n)
    s=np.concatenate([(x-1)/2,(x+1)/2]);g=np.concatenate([w/2,w/2])
    p=g*(1-np.abs(s));h2=4/3*(1-np.abs(s))**2
    density_errors.append(abs(p.sum()-1));density_errors.append(abs(p@h2-2/3))
    # Independent m2 moment formula vs the analytically marginalized density.
    for c in [-2.,-1.,0.,1.,2.]:
        density_errors.append(abs(p@(h2*np.exp(c*s))-L(2,c)))
    for eps in [.25,.3]:
        hs,diag=curvature(s,h2,p,t,eps,1,np.arange(1,65))
        values[(n,eps)]=hs
        for K,H in enumerate(hs,1):
            curverows.append({'quadrature_nodes_per_half':n,'eps':eps,'K':K,
                             'curvature':float(H),**diag})

def field(delta,n,eps,K):
    z,w=leggauss(n);w=w/2
    z1,z2=np.meshgrid(z,z,indexing='ij');p=np.outer(w,w).ravel()
    h=(z1-z2).ravel();s=((.5+delta)*z1+(.5-delta)*z2).ravel()
    q,_=policy(s,p,t,eps);W=np.exp(s-1)
    if K==1:return np.sum(q*W*h/(1+W))
    D=1+W[:,None]+W[None,:]
    return np.sum(q[:,None]*q[None,:]*(W[:,None]*h[:,None]+W[None,:]*h[None,:])/D)

fdrows=[]
for n in [12,16,24]:
    for eps in [.25,.3]:
        for K in [1,2]:
            for step in [1e-5,3e-6]:
                fd=(field(step,n,eps,K)-field(-step,n,eps,K))/(2*step)
                truth=values[(192,eps)][K-1]
                fdrows.append({'nodes_per_factor':n,'eps':eps,'K':K,'step':step,
                               'direct_joint_tuple_fd':float(fd),'tagged_density_curvature':float(truth),
                               'absolute_error':float(abs(fd-truth))})

conv=max(float(np.max(np.abs(values[(96,e)]-values[(192,e)]))) for e in [.25,.3])
violations=[];onsets=[]
for eps in [.25,.3]:
    hs=values[(192,eps)];pos=np.flatnonzero(hs>1e-9)
    if len(pos) and np.any(hs[pos[0]:]<-1e-9):violations.append(eps)
    onsets.append({'eps':eps,'first_positive_through64':int(pos[0]+1) if len(pos) else None,
                   'H1':float(hs[0]),'H64':float(hs[-1])})
summary={'model':'m2 product S2; z1,z2 iid Uniform[-1,1]',
         'max_density_moment_error':float(max(density_errors)),
         'max_closed_vs_quad_moment_error':float(max(moment_errors)),
         'max_resolution_curvature_difference':conv,
         'max_independent_joint_tuple_fd_error':max(r['absolute_error'] for r in fdrows),
         'stable_to_unstable_violations':violations,'onsets':onsets,
         'floor_rows':floors}
write('continuous_floors.csv',floors);write('continuous_curvatures.csv',curverows)
write('continuous_joint_tuple_checks.csv',fdrows)
(OUT/'continuous_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
assert conv<1e-8
assert max(density_errors)<1e-10
assert max(r['absolute_error'] for r in fdrows)<2e-7
assert not violations
print(json.dumps(summary,indent=2))
