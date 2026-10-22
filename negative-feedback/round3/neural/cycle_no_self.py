"""No-positive-self-loop witness: N80 oracle directional derivative, no full FD Jacobian."""
from pathlib import Path
import json,numpy as np
from oracle import policy,field
from view_spectrum import reference
from mixing import predicted,moments
ROOT=Path(__file__).resolve().parent

def main():
    m=20;d=8;f=reference(m);q0=policy(f);C=np.zeros((m,m))
    for j in range(m):C[j,(j-1)%m]=C[j,(j+1)%m]=.5
    P=np.kron(np.eye(4),C);mu=np.cos(2*np.pi*np.arange(1,m)/m);gap=float(1-mu.max())
    assert np.all(np.diag(P)==0) and np.max(abs(P.sum(axis=1)-1))==0
    direction=np.zeros_like(f);direction[:m,2]=np.cos(2*np.pi*np.arange(m)/m);direction/=np.linalg.norm(direction)
    h=1e-4;checks=[];spectra=[]
    for K in [11,12]:
        mo=moments(K,'natural',1);pred,_=predicted(K,gap,m)
        total=pred['negative_softmax_mass'];lp=mo['normal_one'];lb=mo['adaptive_balance']
        expected=float((lp-total*mu.max()/2)/m)
        for pol in ['frozen','adaptive']:
            q=q0 if pol=='frozen' else None
            observed=(field(f+h*direction,P,K,q,L=128)-field(f-h*direction,P,K,q,L=128))/(2*h)
            rayleigh=float(np.sum(direction*observed));residual=float(np.linalg.norm(observed-expected*direction))
            relative=abs(rayleigh/expected-1)
            checks.append({'K':K,'policy':pol,'expected_normal_eigenvalue':expected,'observed_rayleigh':rayleigh,
                           'vector_residual_norm':residual,'rayleigh_relative_error':relative,
                           'passed':bool(residual<1e-8 and relative<1e-4)})
        for pol in ['frozen','adaptive']:
            bal=mo[pol+'_balance'];ab=mo[pol+'_ab']
            mean=np.array([bal]+[ab]*2+[lp]*6+[mo['normal_ab']]*6+[0]*13)/m
            normal=(lp-total*mu/2)/m;plane=normal+bal/(2*m)
            ev=np.concatenate([mean,np.tile(plane,4),np.tile(np.repeat(normal,6),4)])
            assert len(ev)==4*m*(d-1)
            spectra.append({'K':K,'policy':pol,'predicted_dimension':len(ev),'negative_modes':int(sum(ev< -1e-10)),
                            'rotation_zeros':int(sum(abs(ev)<1e-10)),'min_nonrotation_eigenvalue':float(ev[np.abs(ev)>1e-10].min()),
                            'normal_view_eigenvalues':normal.tolist(),'plane_view_eigenvalues':plane.tolist()})
    out={'m':m,'N':len(f),'d':d,'positive_channel':'simple undirected20cycle,neighbors1/2,diagonal0',
         'positive_diagonal_max':float(np.max(np.diag(P))),'positive_gap':gap,
         'gap_certificate':'../journal/zero_self_cycle_certificate.json','h':h,'quadrature_nodes':128,
         'scope':'analytic corollary and finite-population normal derivative; not ordinary warmup or semantic erasure',
         'checks':checks,'analytic_full_spectra':spectra,'passed':all(r['passed'] for r in checks)}
    (ROOT/'results'/'cycle_no_self.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='analytic_full_spectra'},indent=2));assert out['passed']
    assert [r['negative_modes'] for r in spectra]==[0,0,48,48]
if __name__=='__main__':main()
