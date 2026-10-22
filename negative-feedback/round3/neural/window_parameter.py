from pathlib import Path
import csv,json,time,numpy as np
from model import *
from oracle import policy
from view_spectrum import positive,reference,jacobian
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
def main():
    x,bits,render=dataset();P=.95*np.eye(16)+.05*positive(4);f0=reference(4);q0=policy(f0)
    Hs={};T=None
    for K in [4,8,16]:
        for pol in ['frozen','adaptive']:
            H,T=jacobian(f0,P,K,q0 if pol=='frozen' else None);Hs[K,pol]=(H+H.T)/2
    traces=[];checks=[];spectra=[];embeddings={};start=time.time()
    for seed in [4101,4102,4301]:
        v=construct(seed);J=output_jacobian(v,x);u,s,vh=np.linalg.svd(J,full_matrices=False)
        rank=int(sum(s>1e-9));Q=vh[:rank].T;JQ=T.T@J@Q;assert rank==112
        for K in [4,8,16]:
            mats={pol:JQ.T@Hs[K,pol]@JQ for pol in ['frozen','adaptive']}
            values,vectors=np.linalg.eigh(mats['adaptive']);idx=int(np.argmin(values)) if K!=8 else int(np.where(values>1e-8)[0][0])
            target=Q@vectors[:,idx];lam=float(values[idx]);rate=abs(lam)
            rng=np.random.default_rng(seed+K);init=v+1e-5*target+1e-7*rng.normal(size=len(v));a0=float(target@(init-v))
            # New channel: direct directional derivative checks actual parameter field.
            h=3e-6;gp=value_gradient(v+h*target,x,P,K)[1];gm=value_gradient(v-h*target,x,P,K)[1]
            directional_error=float(np.linalg.norm(Q.T@(gp-gm)/(2*h)-mats['adaptive']@(Q.T@target)))
            for pol in ['frozen','adaptive']:
                l=np.linalg.eigvalsh(mats[pol]);spectra.append({'seed':seed,'K':K,'policy':pol,'negative_modes':int(sum(l< -1e-8)),
                          'zero_modes':int(sum(abs(l)<=1e-8)),'min_eigenvalue':float(l.min()),
                          'selected_adaptive_eigenvalue':lam,'parameter_direction_error':directional_error})
            for label in (['frozen','adaptive','adaptive_half'] if seed==4101 else ['frozen','adaptive']):
                pol='adaptive' if label=='adaptive_half' else label;lp,up=np.linalg.eigh(mats[pol]);U=Q@up
                steps=3000 if label=='adaptive_half' else 1500;dt=3/(rate*steps);w=init.copy();qf=q0 if pol=='frozen' else None
                for step in range(steps):
                    loss,g=value_gradient(w,x,P,K,qf);rhs=-dt*g
                    w+=rhs+U@((1/(1+dt*lp)-1)*(U.T@rhs))
                    if step in [0,steps//6-1,steps//3-1,2*steps//3-1,steps-1]:
                        amp=float(target@(w-v));geom=geometry(forward(x,w)[0])
                        traces.append({'seed':seed,'K':K,'policy':label,'step':step+1,'time':dt*(step+1),'scaled_time':rate*dt*(step+1),
                                       'amplitude_ratio':abs(amp/a0),'weaker_energy':geom['weaker_energy'],
                                       'within_view_variance':geom['within_view_variance'],'loss':loss})
                ratio=traces[-1]['amplitude_ratio'];grow=(K==16 or K==4 and pol=='adaptive');passed=ratio>10 if grow else ratio<.15
                checks.append({'seed':seed,'K':K,'policy':label,'predicted_growth':bool(grow),'final_ratio':ratio,'passed':bool(passed)})
                embeddings[f'{seed}/{K}/{label}']=forward(x,w)[0].tolist()
        print(json.dumps({'seed':seed,'completed':True}),flush=True)
    refinement=[]
    for K in [4,8,16]:
        r={c['policy']:c['final_ratio'] for c in checks if c['seed']==4101 and c['K']==K}
        err=abs(r['adaptive']/r['adaptive_half']-1);refinement.append({'K':K,'relative_difference':err,'passed':bool(err<.01)})
    for name,rows in [('window_parameter_spectrum.csv',spectra),('window_parameter_trajectories.csv',traces)]:
        with (OUT/name).open('w') as f:
            wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    summary={'runs':len(checks),'passed':sum(c['passed'] for c in checks),'checks':checks,'step_refinement':refinement,
             'max_direction_error':max(r['parameter_direction_error'] for r in spectra),'elapsed_seconds':time.time()-start}
    (OUT/'window_parameter_summary.json').write_text(json.dumps(summary,indent=2)+'\n');(OUT/'window_parameter_embeddings.json').write_text(json.dumps(embeddings)+'\n')
    print(json.dumps(summary,indent=2));assert all(c['passed'] for c in checks) and all(c['passed'] for c in refinement)
if __name__=='__main__':main()
