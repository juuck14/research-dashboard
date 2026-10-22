"""Deterministic population oracles and predeclared Monte Carlo illustration.
Run from topic root: OPENBLAS_NUM_THREADS=1 python code/run_study.py
"""
from pathlib import Path
import csv,json,platform
import numpy as np
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'; FIG=ROOT/'figures'
OUT.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)

def rotation(t):
    c,s=np.cos(t),np.sin(t)
    return np.array([[c,-s],[s,c]])

def tc_cov(c):
    sign,ld=np.linalg.slogdet(c)
    if sign<=0: raise ValueError('nonpositive covariance')
    return .5*(np.log(np.diag(c)).sum()-ld)

def pair_radius(a,b,delta):
    if np.isclose(a,b,rtol=0,atol=1e-15): return np.pi/4
    return .5*np.arcsin(min(1.,np.sqrt(4*a*b*np.expm1(2*delta)/(a-b)**2)))

def write_csv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def oracle_grid(gammas,deltas,label):
    ts=np.linspace(0,np.pi/4,100001);rows=[]
    max_err=0.;max_cov=0.;max_endpoint=0.
    for g in gammas:
        # direct covariance calculation independent from TC scalar expression
        R=np.stack([np.stack([np.cos(ts),-np.sin(ts)],-1),np.stack([np.sin(ts),np.cos(ts)],-1)],-2)
        D=np.diag([1+g,1-g]); C=np.einsum('...ji,jk,...kl->...il',R,D,R)
        direct=.5*(np.log(np.diagonal(C,axis1=-2,axis2=-1)).sum(1)-np.linalg.slogdet(C)[1])
        formula=.5*np.log1p(g*g*np.sin(2*ts)**2/(1-g*g))
        max_err=max(max_err,float(np.max(np.abs(direct-formula))))
        reconstructed=np.einsum('...ij,...jk,...lk->...il',R,C,R)
        max_cov=max(max_cov,float(np.max(np.abs(reconstructed-D))))
        for delta in deltas:
            radius=pair_radius(1+g,1-g,delta)
            grid=ts[direct<=delta+1e-14]
            gr=float(grid.max());err=abs(gr-radius);max_endpoint=max(max_endpoint,err)
            assert err<=2*(ts[1]-ts[0]),(g,delta,err)
            rows.append(dict(split=label,gamma=g,delta=delta,critical_delta=-.5*np.log1p(-g*g),radius_rad=radius,radius_deg=np.degrees(radius),grid_radius_deg=np.degrees(gr),endpoint_error_rad=err,minimax_angle_lower_deg=np.degrees(radius)/2))
    assert max_err<1e-12 and max_cov<1e-12
    write_csv('oracle_'+label+'.csv',rows)
    return {'split':label,'cases':len(rows),'grid_points_per_gamma':len(ts),'max_tc_formula_error':max_err,'max_observed_covariance_reconstruction_error':max_cov,'max_endpoint_error_rad':max_endpoint}

def sample_study():
    rows=[];true_angle=.37;A=rotation(true_angle)
    for split,seeds in [('exploration',range(100,120)),('confirmation',range(1000,1040))]:
        for g in [.03,.3]:
            D=np.diag([1+g,1-g]);L=A@np.sqrt(D)
            for n in [100,1000,10000]:
                for seed in seeds:
                    rng=np.random.default_rng(seed)
                    x=rng.standard_normal((n,2))@L.T
                    sample=x.T@x/n # known zero mean, trusted population baseline I
                    _,vec=np.linalg.eigh(sample)
                    ang=float(np.arctan2(vec[1,-1],vec[0,-1]))
                    err=abs((ang-true_angle+np.pi/4)%(np.pi/2)-np.pi/4)
                    rows.append(dict(split=split,gamma=g,n=n,seed=seed,axis_error_deg=np.degrees(err),structural_radius_deg=np.degrees(pair_radius(1+g,1-g,.001))))
    write_csv('sample_raw.csv',rows)
    ag=[]
    for split in ['exploration','confirmation']:
        for g in [.03,.3]:
            for n in [100,1000,10000]:
                vals=[r['axis_error_deg'] for r in rows if r['split']==split and r['gamma']==g and r['n']==n]
                ag.append(dict(split=split,gamma=g,n=n,repeats=len(vals),median_axis_error_deg=float(np.median(vals)),mean_axis_error_deg=float(np.mean(vals)),p90_axis_error_deg=float(np.quantile(vals,.9)),structural_radius_deg=np.degrees(pair_radius(1+g,1-g,.001))))
    write_csv('sample_summary.csv',ag)
    return ag

def three_d():
    vals=[1.02,.98,1.8];rows=[]
    for delta in [1e-4,1e-3,.01]:
        for pair in [(0,1),(0,2),(1,2)]:
            i,j=pair;radius=pair_radius(vals[i],vals[j],delta)
            R=np.eye(3);r=rotation(radius);R[np.ix_([i,j],[i,j])]=r
            D=np.diag(vals);C=R.T@D@R
            rows.append(dict(delta=delta,pair=f'{i+1}-{j+1}',a=vals[i],b=vals[j],feasible_radius_deg=np.degrees(radius),TC=tc_cov(C),covariance_reconstruction_error=float(np.max(np.abs(R@C@R.T-D)))))
    write_csv('three_d_pairwise_feasible.csv',rows)
    return rows

checks=[oracle_grid([.01,.03,.1,.3,.6],[1e-6,1e-4,1e-3,.01,.05],'exploration'),oracle_grid([.017,.071,.23,.49],[2e-5,7e-4,.007,.03],'confirmation')]
summary=sample_study();three=three_d()
# Figures: numerical plots are illustration, exact proof resides in theory.md.
fig,ax=plt.subplots(figsize=(6,4))
ds=np.geomspace(1e-7,.1,300)
for g in [.01,.03,.1,.3,.6]:
    ax.semilogx(ds,[np.degrees(pair_radius(1+g,1-g,d)) for d in ds],label=f'gamma={g}')
ax.set(xlabel='Allowed source total correlation (nats)',ylabel='Exact quotient radius (degrees)',ylim=(0,46));ax.legend(fontsize=8);fig.tight_layout();fig.savefig(FIG/'population_radius.png',dpi=150);fig.savefig(FIG/'population_radius.svg');plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(8,3.5),sharey=True)
for ax,g in zip(axes,[.03,.3]):
    rr=[r for r in summary if r['split']=='confirmation' and r['gamma']==g]
    ax.semilogx([r['n'] for r in rr],[r['median_axis_error_deg'] for r in rr],'o-',label='Median sampling error')
    ax.axhline(rr[0]['structural_radius_deg'],color='red',ls='--',label='Structural radius, delta=.001')
    ax.set(title=f'gamma={g}',xlabel='Samples in environment 1',ylabel='Degrees');ax.legend(fontsize=7)
fig.tight_layout();fig.savefig(FIG/'sample_vs_structure.png',dpi=150);fig.savefig(FIG/'sample_vs_structure.svg');plt.close(fig)
with (OUT/'checks.json').open('w') as f:json.dump({'checks':checks,'sample_replicates':360,'three_d_examples':len(three),'all_assertions_passed':True},f,indent=2)
with (OUT/'environment.json').open('w') as f:json.dump({'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__,'command':'OPENBLAS_NUM_THREADS=1 python code/run_study.py'},f,indent=2)
print(json.dumps({'checks':checks,'confirmation_summary':[r for r in summary if r['split']=='confirmation'],'three_d':three},indent=2))
