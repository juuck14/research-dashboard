"""Independent population checks. Run from repository root; no training labels used."""
import csv,json,itertools,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ndtr

OUT=Path(__file__).resolve().parents[1]/'results'
OUT.mkdir(exist_ok=True)

def flow(t,y,rho,eta,beta,frozen=False,no_predictor=False):
    if no_predictor:
        w,a=y
        return [rho*a-(1+eta)*w,0. if frozen else beta*(w-a)]
    w,p,a=y
    err=rho*a-p*w
    return [p*err-eta*w,w*err-eta*p,0. if frozen else beta*(w-a)]

def jac(y,rho,eta,beta):
    w,p,a=y
    return np.array([[-p*p-eta,rho*a-2*p*w,rho*p],
                     [rho*a-2*p*w,-w*w-eta,rho*w],
                     [beta,0.,-beta]])

rows=[]
max_finite_diff=0.
for rho,eta,beta in itertools.product([.35,.8,.95],[.005,.02],[.001,.1,10.]):
    roots=[0.]
    if rho*rho>=4*eta:
        roots +=[(rho-math.sqrt(rho*rho-4*eta))/2,(rho+math.sqrt(rho*rho-4*eta))/2]
    for s in roots:
        y=np.repeat(s,3)
        J=jac(y,rho,eta,beta)
        eps=1e-6
        fd=np.column_stack([(np.array(flow(0,y+np.eye(3)[i]*eps,rho,eta,beta))-np.array(flow(0,y-np.eye(3)[i]*eps,rho,eta,beta)))/(2*eps) for i in range(3)])
        error=float(np.max(np.abs(J-fd)))
        max_finite_diff=max(max_finite_diff,error)
        eig=np.linalg.eigvals(J)
        residual=float(np.max(np.abs(flow(0,y,rho,eta,beta))))
        if s==0:
            predicted=np.array([-eta,-eta,-beta])
        else:
            red=np.array([[-2*s*s,rho*s],[beta,-beta]])
            predicted=np.r_[[-2*eta],np.linalg.eigvals(red)]
        spec_error=float(np.max(np.abs(np.sort_complex(eig)-np.sort_complex(predicted))))
        rows.append(dict(rho=rho,eta=eta,beta=beta,s=s,residual=residual,fd_error=error,spectrum_error=spec_error,max_real=float(np.max(eig.real)),stable=bool(np.max(eig.real)<-1e-10)))
with (OUT/'fixed_point_checks.csv').open('w') as f:
    wr=csv.DictWriter(f,fieldnames=rows[0]);wr.writeheader();wr.writerows(rows)

trajectories=[]
for no_pred,frozen,beta in itertools.product([False,True],[False,True],[.001,.1,10.]):
    y0=[.01,.1] if no_pred else [.01,.01,.1]
    sol=solve_ivp(lambda t,y:flow(t,y,.8,.02,beta,frozen,no_pred),[0,5000],y0,rtol=1e-10,atol=1e-12,dense_output=True)
    y=sol.y[:,-1]
    sample=sol.sol(np.array([0.,1.,10.,100.,1000.,5000.]))
    trajectories.append(dict(no_predictor=no_pred,frozen=frozen,beta=beta,success=sol.success,final=y.tolist(),t=[0,1,10,100,1000,5000],samples=sample.tolist()))
(OUT/'frozen_ema_checks.json').write_text(json.dumps(trajectories,indent=2)+'\n')

states=np.array(list(itertools.product([-1.,1.],repeat=2)))
info=[]
for t in [0,10,100,200]:
    a=np.array([1.,.1])*np.array([.95,.75])**t
    rep=states*a
    unique=len(np.unique(rep,axis=0))
    info.append(dict(t=t,a1=a[0],a2=a[1],state_count=unique,joint_information_bits=math.log2(unique),noiseless_factor_accuracy=1.,fixed_sigma=.01,bayes_accuracy_factor1=float(ndtr(a[0]/.01)),bayes_accuracy_factor2=float(ndtr(a[1]/.01))))
with (OUT/'finite_time_information.csv').open('w') as f:
    wr=csv.DictWriter(f,fieldnames=info[0]);wr.writeheader();wr.writerows(info)

counter=[]
for c in [0.,.001,.5,1.]:
    values=states@np.array([1.,c])
    un,counts=np.unique(values,return_counts=True)
    probs=counts/4
    H=float(-np.sum(probs*np.log2(probs)))
    counter.append(dict(c=c,matrix_rank=1,distinct_states=len(un),joint_information_bits=H,values=values.tolist()))
(OUT/'rank_one_counterexample.json').write_text(json.dumps(counter,indent=2)+'\n')
summary=dict(max_fd_jacobian_error=max_finite_diff,max_fixed_point_residual=max(x['residual'] for x in rows),max_spectrum_error=max(x['spectrum_error'] for x in rows),n_fixed_points=len(rows),all_ode_success=all(x['success'] for x in trajectories))
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
for r in trajectories:
    if not r['no_predictor'] and not r['frozen']: print('learned EMA beta',r['beta'],'final',r['final'])
print('rank-one',counter)
