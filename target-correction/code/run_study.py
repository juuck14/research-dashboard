#!/usr/bin/env python3
"""Exact population audit. All designs registered in ../protocol.md before running."""
from pathlib import Path
import csv, json, platform, sys, time
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'
OUT.mkdir(exist_ok=True)

def save_csv(name, rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

def flow(t,y,rho,eta,beta,frozen=False):
    w,p,a=y
    e=rho*a-p*w
    return [p*e-eta*w,w*e-eta*p,0. if frozen else beta*(w-a)]

def solve(rho,eta,beta,s0,T=1500.,frozen=False,t_eval=None):
    r=solve_ivp(flow,[0,T],[s0,s0,s0],args=(rho,eta,beta,frozen),
                method='DOP853',rtol=1e-9,atol=1e-12,t_eval=t_eval)
    if not r.success: raise RuntimeError(r.message)
    return r

def roots(rho,eta):
    disc=rho*rho-4*eta
    return (None,None) if disc<0 else ((rho-np.sqrt(disc))/2,(rho+np.sqrt(disc))/2)

def expected(rho,eta,s0):
    lo,hi=roots(rho,eta)
    return 0. if hi is None or (eta>0 and s0<lo) else hi

def jac(y,rho,eta,beta):
    w,p,a=y
    return np.array([[-p*p-eta,rho*a-2*p*w,p*rho],
                     [rho*a-2*p*w,-w*w-eta,w*rho],
                     [beta,0.,-beta]])

def main():
    start=time.time()
    env={'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
         'matplotlib':matplotlib.__version__,'platform':platform.platform(),
         'command':'python target-correction/code/run_study.py',
         'confirmation_seeds':[20261022,20261023,20261024]}
    (OUT/'environment.json').write_text(json.dumps(env,indent=2))
    # Explicit finite-state transition K with all entries > 0.
    states=np.array([[-1,-1],[-1,1],[1,-1],[1,1]],float)
    rho=np.array([.9,.5]); a0=np.array([1.,.1]); rows=[]; maxerr=0.
    K=np.ones((4,4))
    for j in range(2): K*= (1+rho[j]*states[:,j,None]*states[None,:,j])/2
    assert K.min()>0 and np.allclose(K.sum(1),1)
    for beta in [.1,.5,1.]:
        G=states*a0
        for t in range(201):
            amps=np.mean(states*G,axis=0)
            exact=a0*(1-beta+beta*rho)**t
            maxerr=max(maxerr,float(np.max(np.abs(amps-exact))))
            for j in range(2):
                amp=exact[j]
                for sigma in [0.,.01]:
                    r2=1. if sigma==0 else amp*amp/(amp*amp+sigma*sigma)
                    rows.append({'beta':beta,'step':t,'factor':j+1,'amplitude':amp,
                         'readout_noise_sd':sigma,'r2_observed_factor':r2,
                         'r2_latent_factor':rho[j]*r2,
                         'noiseless_bayes_latent_accuracy':(1+np.sqrt(rho[j]))/2})
            G=((1-beta)*G+beta*K@G)
    save_csv('operator_modes.csv',rows)
    # Independent normalization controls, computed by recurrence.
    Gg=states*a0; Gw=states*a0; normrows=[]
    for t in range(201):
        ag=np.mean(states*Gg,axis=0); aw=np.mean(states*Gw,axis=0)
        normrows.append({'step':t,'global_factor1':ag[0],'global_factor2':ag[1],
                        'whiten_factor1':aw[0],'whiten_factor2':aw[1]})
        Gg=K@Gg; Gg/=np.sqrt(np.mean(np.sum(Gg*Gg,axis=1)))
        Gw=K@Gw; Gw/=np.sqrt(np.mean(Gw*Gw,axis=0))
    save_csv('normalization_controls.csv',normrows)
    # Primary grid.
    grid=[]
    for r in [.5,.8]:
      for eta in [0.,.02,.06]:
       for beta in [.1,1.,10.]:
        for s0 in [.01,.1,.4,.8]:
            sol=solve(r,eta,beta,s0)
            end=sol.y[:,-1]; target=expected(r,eta,s0)
            grid.append({'rho':r,'eta':eta,'beta':beta,'initial':s0,'T':1500,
               'w_final':end[0],'p_final':end[1],'a_final':end[2],
               'predicted_equilibrium':target,'max_abs_error':float(np.max(np.abs(end-target))),
               'solver_evaluations':sol.nfev,'balanced_error':float(np.max(np.abs(sol.y[0]-sol.y[1])))})
    save_csv('primary_grid.csv',grid)
    # Held-out rho,beta and independently jittered positive balanced starts.
    confirm=[]
    for r in [.35,.65,.95]:
     for eta in [.005,.025]:
      for beta in [.03,.3,3.]:
       lo,hi=roots(r,eta)
       for seed in [20261022,20261023,20261024]:
        rng=np.random.default_rng(seed)
        for multiplier in [.5,1.5]:
            s0=lo*multiplier*rng.uniform(.95,1.05)
            sol=solve(r,eta,beta,s0,T=4000.)
            end=sol.y[:,-1]; target=expected(r,eta,s0)
            confirm.append({'rho':r,'eta':eta,'beta':beta,'seed':seed,'initial':s0,
                  'T':4000,'predicted_equilibrium':target,'w_final':end[0],
                  'max_abs_error':float(np.max(np.abs(end-target)))})
    save_csv('confirmation_grid.csv',confirm)
    # Jacobian analytical eigenvalue multiset check.
    jr=[]
    for r in [.35,.65,.95]:
     for eta in [.005,.025]:
      for beta in [.03,.3,3.]:
       for name,s in zip(['minus','plus'],roots(r,eta)):
        numerical=np.sort(np.linalg.eigvals(jac([s,s,s],r,eta,beta)).real)
        block=np.array([[-2*s*s,r*s],[beta,-beta]])
        exact=np.sort(np.r_[-2*eta,np.linalg.eigvals(block).real])
        jr.append({'rho':r,'eta':eta,'beta':beta,'branch':name,
              'largest_eigenvalue':float(numerical[-1]),
              'eigenvalue_formula_error':float(np.max(np.abs(numerical-exact)))})
    save_csv('jacobian_checks.csv',jr)
    # Analytically chosen frozen/EMA contrast, registered before numerical run.
    r=.5; eta=.02; beta=1.; lo,hi=roots(r,eta)
    s0=(eta/r+lo)/2; traj=[]
    t=np.linspace(0,1500,1001)
    for frozen in [False,True]:
        sol=solve(r,eta,beta,s0,frozen=frozen,t_eval=t)
        for k,tt in enumerate(t):
            traj.append({'teacher':'frozen' if frozen else 'EMA','time':tt,
                'w':sol.y[0,k],'p':sol.y[1,k],'a':sol.y[2,k]})
    save_csv('frozen_vs_ema.csv',traj)
    # No decay: distinguish long delay from attraction to collapse.
    escape=[]
    for s0 in [.001,.003,.01]:
        def event(t,y,*args): return y[0]-.2
        event.terminal=True; event.direction=1
        sol=solve_ivp(flow,[0,5000],[s0]*3,args=(.8,0.,1.,False),events=event,
                      method='DOP853',rtol=1e-10,atol=1e-13)
        hit=float(sol.t_events[0][0])
        exact_simsiam=(1/.8)*(1/s0-1/.2)+(1/.8**2)*np.log((.2/(.8-.2))/(s0/(.8-s0)))
        escape.append({'initial':s0,'rho':.8,'eta':0.,'beta':1.,
             'time_to_w_0.2':hit,'rho_initial_time':.8*s0*hit,
             'instant_teacher_exact_time':exact_simsiam})
    save_csv('no_decay_escape.csv',escape)
    # Fixed-predictor analytic stability, excluding a learned-predictor confound.
    fixed=[]
    for r in [.35,.65,.95]:
     for p in [.1,.5,1.]:
      for eta in [0.,.025]:
       for beta in [.03,.3,3.]:
        M=np.array([[-(p*p+eta),p*r],[beta,-beta]])
        eig=np.linalg.eigvals(M)
        fixed.append({'rho':r,'predictor':p,'eta':eta,'beta':beta,
             'largest_eigenvalue':float(np.max(eig.real)),
             'stability_margin':p*p+eta-p*r,
             'criterion_matches':bool((np.max(eig.real)<-1e-12)==(p*p+eta-p*r>1e-12))})
    save_csv('fixed_predictor_stability.csv',fixed)
    summary={'operator_max_error':maxerr,'K_min_entry':float(K.min()),
       'primary_runs':len(grid),'primary_max_equilibrium_error':max(x['max_abs_error'] for x in grid),
       'confirmation_runs':len(confirm),'confirmation_max_equilibrium_error':max(x['max_abs_error'] for x in confirm),
       'jacobian_checks':len(jr),'jacobian_max_formula_error':max(x['eigenvalue_formula_error'] for x in jr),
       'fixed_predictor_checks':len(fixed),'fixed_predictor_criterion_all_match':all(x['criterion_matches'] for x in fixed),
       'frozen_contrast':{'rho':.5,'eta':.02,'initial':float((.02/.5+roots(.5,.02)[0])/2),
             'predicted_frozen_equilibrium':float(np.sqrt(.5*((.02/.5+roots(.5,.02)[0])/2)-.02)),
             'predicted_ema_equilibrium':0.},'elapsed_seconds':time.time()-start}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2))
    fig,ax=plt.subplots(1,3,figsize=(12,3.4))
    for j in [1,2]:
        rr=[x for x in rows if x['beta']==.5 and x['factor']==j and x['readout_noise_sd']==0]
        ax[0].semilogy([x['step'] for x in rr],[x['amplitude'] for x in rr],label=f'factor {j}')
        rr=[x for x in rows if x['beta']==.5 and x['factor']==j and x['readout_noise_sd']==.01]
        ax[1].plot([x['step'] for x in rr],[x['r2_observed_factor'] for x in rr],label=f'factor {j}, noise .01')
    ax[1].axhline(1,color='black',ls='--',label='both factors, noiseless')
    for name in ['frozen','EMA']:
        rr=[x for x in traj if x['teacher']==name]
        ax[2].semilogy([x['time'] for x in rr],np.maximum([x['w'] for x in rr],1e-15),label=name)
    for a,title in zip(ax,['Exact Bayes refresh amplitude','Linear access with fixed readout noise','Same initial target, learned predictor']):
        a.set_title(title,fontsize=9);a.set_xlabel('iteration' if a is not ax[2] else 'flow time');a.legend(fontsize=7)
    fig.tight_layout();fig.savefig(OUT/'controls.png',dpi=160);plt.close(fig)
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
