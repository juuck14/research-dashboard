from pathlib import Path
import json,csv,time
import numpy as np
from oracle import policy,field
from model import *
from view_spectrum import reference,positive,tangent,jacobian
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'

def main():
    x,bits,Qrender=dataset();P=positive(4);fstar=reference(4);results=[];matrices={}
    for K in [4,5]:
        for pol in ['frozen','adaptive']:
            H,T=jacobian(fstar,P,K,policy(fstar) if pol=='frozen' else None)
            matrices[K,pol]=(H+H.T)/2
    models={};trajectories=[];checks=[];start=time.time()
    for seed in [3501,3502,3701]:
        v=construct(seed);f,c=forward(x,v);J=output_jacobian(v,x);u,s,vh=np.linalg.svd(J,full_matrices=False)
        rank=int(np.sum(s>1e-9));Q=vh[:rank].T;JT=T.T@J;JQ=JT@Q
        for K in [4,5]:
            H=matrices[K,'adaptive'];B=JQ.T@H@JQ;B=(B+B.T)/2
            vals,vec=np.linalg.eigh(B);nonzero=vals[np.abs(vals)>1e-8];target_idx=int(np.argmin(vals)) if K==4 else int(np.where(vals>1e-8)[0][0])
            target=Q@vec[:,target_idx];rate=abs(vals[target_idx])
            _,res=value_gradient(v,x,P,K)
            # Direct parameter gradient derivative, not merely the pullback formula.
            FD=np.empty_like(B);h=3e-6
            for j in range(rank):
                d=Q[:,j];gp=value_gradient(v+h*d,x,P,K)[1];gm=value_gradient(v-h*d,x,P,K)[1]
                FD[:,j]=Q.T@(gp-gm)/(2*h)
            err=float(np.linalg.norm(FD-B)/np.linalg.norm(B))
            results.append({'seed':seed,'K':K,'tangent_rank':rank,'expected_rank':112,'output_reference_error':float(np.max(abs(f-fstar))),
                'smallest_nonzero_singular':float(s[rank-1]),'parameter_stationary_residual':float(np.linalg.norm(res)),
                'pullback_relative_error':err,'negative_modes':int(np.sum(vals< -1e-8)),
                'zero_modes':int(np.sum(abs(vals)<=1e-8)),'target_eigenvalue':float(vals[target_idx]),
                'smallest_positive':float(nonzero[nonzero>0].min())})
            assert rank==112 and err<1e-5
            theta=np.pi/4+1e-5;p=unpack(v.copy());p['W2'][0,0]=np.cos(theta)/np.tanh(1);p['W2'][1,1]=np.sin(theta)/np.tanh(1)
            rng=np.random.default_rng(seed+1);init=pack(p)+1e-7*rng.normal(size=len(v))
            a0=float(target@(init-v));assert abs(a0)>1e-8
            for pol in (['frozen','adaptive','adaptive_half'] if seed==3501 else ['frozen','adaptive']):
                basepol='adaptive' if pol=='adaptive_half' else pol
                Hp=matrices[K,basepol];Bp=JQ.T@Hp@JQ;lp,up=np.linalg.eigh((Bp+Bp.T)/2);U=Q@up
                w=init.copy();nsteps=3000 if pol=='adaptive_half' else 1500;dt=3/(rate*nsteps);qfixed=policy(fstar) if pol=='frozen' else None
                for step in range(nsteps):
                    _,g=value_gradient(w,x,P,K,qfixed);rhs=-dt*g;proj=U.T@rhs
                    w+=rhs+U@((1/(1+dt*lp)-1)*proj)
                    if step in [0,nsteps//6-1,nsteps//3-1,2*nsteps//3-1,nsteps-1]:
                        amp=float(target@(w-v));geom=geometry(forward(x,w)[0])
                        trajectories.append({'seed':seed,'K':K,'policy':pol,'step':step+1,'scaled_time':rate*dt*(step+1),
                             'time':dt*(step+1),'amplitude_ratio':abs(amp/a0),'initial_amplitude':a0,'amplitude':amp,
                             'weaker_energy':geom['weaker_energy'],'within_view_variance':geom['within_view_variance']})
                ratio=trajectories[-1]['amplitude_ratio'];passed=(ratio>10 if K==4 and basepol=='adaptive' else ratio<.15)
                checks.append({'seed':seed,'K':K,'policy':pol,'ratio':ratio,'passed':bool(passed),'step_scaled':rate*dt,
                               'backward_euler_prediction':float((1+dt*vals[target_idx])**(-nsteps)) if basepol=='adaptive' else None})
                models[f'{seed}/{K}/{pol}']=forward(x,w)[0].tolist()
            print(json.dumps(results[-1]),flush=True)
    for name,rows in [('parameter_spectrum.csv',results),('parameter_trajectories.csv',trajectories)]:
        with (OUT/name).open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary={'spectral_settings':len(results),'dynamical_runs':len(checks),'criteria_passed':sum(x['passed'] for x in checks),
             'max_pullback_relative_error':max(x['pullback_relative_error'] for x in results),'max_stationary_residual':max(x['parameter_stationary_residual'] for x in results),
             'elapsed_seconds':time.time()-start,'checks':checks,'spectra':results}
    (OUT/'parameter_summary.json').write_text(json.dumps(summary,indent=2)+'\n');(OUT/'parameter_final_embeddings.json').write_text(json.dumps(models)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
