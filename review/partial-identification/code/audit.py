"""Independent Gaussian ambiguity audit; no imports from the owner's implementation."""
from pathlib import Path
import csv,json,math
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'
OUT.mkdir(exist_ok=True)

def tc(C):
    sign,logdet=np.linalg.slogdet(C)
    if sign<=0:
        raise ValueError('covariance must be SPD')
    return .5*(np.log(np.diag(C)).sum()-logdet)

def rot(theta):
    c,s=np.cos(theta),np.sin(theta)
    return np.array([[c,-s],[s,c]])

records=[]
max_formula=max_reconstruction=max_scaling=0.
for seed in [20261022,8675309]:
    rng=np.random.default_rng(seed)
    for case in range(200):
        a,b=np.exp(rng.uniform(-3,3,2))
        theta=rng.uniform(-math.pi,math.pi)
        Q=rot(theta)
        D=np.diag([a,b])
        C=Q@D@Q.T
        exact=.5*np.log1p((a-b)**2/(4*a*b)*np.sin(2*theta)**2)
        gap=abs(tc(C)-exact)
        reconstruction=np.linalg.norm(Q.T@C@Q-D,ord='fro')
        S=np.diag(np.exp(rng.uniform(-2,2,2)))
        scale_gap=abs(tc(S@C@S)-tc(C))
        max_formula=max(max_formula,gap)
        max_reconstruction=max(max_reconstruction,reconstruction)
        max_scaling=max(max_scaling,scale_gap)
        records.append([seed,case,a,b,theta,tc(C),exact,gap,reconstruction,scale_gap])

# Observed x has covariance D_e; latent u=T x, x=T^-1 u exactly.
delta=.001
epsilon=.8*np.sqrt(np.expm1(2*delta))
T=np.array([[1.,epsilon],[0.,1.]])
B=np.linalg.inv(T)
shear=[]
for e,D in enumerate([np.eye(2),np.diag([1.3,.7])]):
    C=T@D@T.T
    reconstructed=B@C@B.T
    shear.append({'environment':e,'tc':tc(C),'budget':delta,
                  'reconstruction_error':float(np.linalg.norm(reconstructed-D)),
                  'source_covariance':C.tolist()})
C0=T@T.T
S=np.diag(1/np.sqrt(np.diag(C0)))
Tnorm=S@T
Bnorm=np.linalg.inv(Tnorm)
# Component scaling normalizes diagonals but preserves source correlation.
normalized_source_cov=Tnorm@Tnorm.T
orthogonality_error=float(np.linalg.norm(Bnorm@Bnorm.T-np.eye(2)))

# Rare informative environment: conditional-TC average and worst-case budgets differ.
gamma=.6
rare_probability=.01
delta_rare=.01
angles=np.linspace(0,np.pi/4,200001)
k=gamma**2/(1-gamma**2)
tc_grid=.5*np.log1p(k*np.sin(2*angles)**2)
end_max=float(angles[tc_grid<=delta_rare][-1])
end_avg=float(angles[rare_probability*tc_grid<=delta_rare][-1])
end_max_exact=.5*np.arcsin(min(1.,np.sqrt(np.expm1(2*delta_rare)/k)))
end_avg_exact=.5*np.arcsin(min(1.,np.sqrt(np.expm1(2*delta_rare/rare_probability)/k)))
summary={'random_cases':len(records),'max_formula_absolute_error':max_formula,
         'max_reconstruction_frobenius_error':max_reconstruction,
         'max_component_scaling_tc_error':max_scaling,
         'shear_epsilon':float(epsilon),'shear':shear,
         'normalized_source_covariance':normalized_source_cov.tolist(),
         'normalized_mixing_orthogonality_error':orthogonality_error,
         'rare_environment':{'gamma':gamma,'delta':delta_rare,'probability':rare_probability,
         'max_budget_endpoint_degrees':float(np.degrees(end_max)),
         'average_budget_endpoint_degrees':float(np.degrees(end_avg)),
         'max_budget_endpoint_exact_degrees':float(np.degrees(end_max_exact)),
         'average_budget_endpoint_exact_degrees':float(np.degrees(end_avg_exact))}}
assert max_formula<1e-11
assert max_reconstruction<1e-11
assert max_scaling<1e-11
assert all(x['tc']<delta and x['reconstruction_error']<1e-11 for x in shear)
assert abs(normalized_source_cov[0,1])>1e-3 and orthogonality_error>1e-3
assert abs(end_max-end_max_exact)<=2*(angles[1]-angles[0])
assert abs(end_avg-end_avg_exact)<=2*(angles[1]-angles[0])
with (OUT/'random_checks.csv').open('w') as f:
    writer=csv.writer(f)
    writer.writerow(['seed','case','a','b','theta','tc_direct','tc_formula','absolute_error','reconstruction_error','scaling_tc_error'])
    writer.writerows(records)
(OUT/'audit_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
