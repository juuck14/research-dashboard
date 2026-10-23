from pathlib import Path
from itertools import product
import json,sys
import numpy as np
from scipy.special import ndtr

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'round3'/'neural'))
from oracle import field,policy

X=np.array(list(product([-1.,1.],repeat=3)))
F0=np.column_stack([X[:,0]/np.sqrt(2),X[:,1]/np.sqrt(2),np.zeros(8)])
direction=np.column_stack([np.zeros(8),np.zeros(8),X[:,2]])
P=.95*np.eye(8)+.05*np.kron(np.eye(4),np.ones((2,2))/2)
checks=[]
for K in [8,16]:
    for sampler in ['frozen','adaptive']:
        q=policy(F0) if sampler=='frozen' else None
        for h in [1e-5,1e-4]:
            derivative=(field(F0+h*direction,P,K,q,L=128)-field(F0-h*direction,P,K,q,L=128))/(2*h)
            restoring=float(np.sum(derivative*direction)/np.sum(direction**2))
            residual=float(np.linalg.norm(derivative-restoring*direction))
            checks.append({'K':K,'sampler':sampler,'step':h,'restoring':restoring,'flow_grows':bool(restoring<0),'eigen_residual':residual})
assert all(c['flow_grows']==(c['K']==16) for c in checks)

information=[]
tasks=[]
for alpha in [0.,.001,.01,.1,.3,.6]:
    f=np.column_stack([np.sqrt((1-alpha*alpha)/2)*X[:,0],np.sqrt((1-alpha*alpha)/2)*X[:,1],alpha*X[:,2]])
    _,counts=np.unique(np.round(f,12),axis=0,return_counts=True)
    p=counts/counts.sum();entropy=float(-np.sum(p*np.log2(p)))
    information.append({'alpha':alpha,'I_a_bits':1.,'I_b_bits':1.,'I_v_bits':0. if alpha==0 else 1.,'I_X_bits_exact_formula':2. if alpha==0 else 3.,'I_X_bits_finite_enumeration':entropy,
                        'linear_a_accuracy':float(np.mean(np.sign(f[:,0])==X[:,0])),'linear_b_accuracy':float(np.mean(np.sign(f[:,1])==X[:,1])),'linear_v_accuracy':.5 if alpha==0 else float(np.mean(np.sign(f[:,2])==X[:,2]))})
    for sigma in [.2,.5]:
        semantic=float(ndtr(np.sqrt((1-alpha*alpha)/2)/sigma));view=float(ndtr(alpha/sigma))
        for view_weight in [0.,.1,.5,1.]:
            tasks.append({'alpha':alpha,'sigma':sigma,'semantic_bayes_accuracy':semantic,'view_bayes_accuracy':view,'view_task_weight':view_weight,'weighted_accuracy':(1-view_weight)*semantic+view_weight*view})

rectangles=[]
for sigma in [.2,.5]:
    for theta in [np.pi/4,.7545192717973]:
        a=float(ndtr(np.cos(theta)/sigma));b=float(ndtr(np.sin(theta)/sigma))
        for a_weight in [.1,.5,.9]:
            rectangles.append({'theta':theta,'sigma':sigma,'task_a_accuracy':a,'task_b_accuracy':b,'a_task_weight':a_weight,'weighted_accuracy':a_weight*a+(1-a_weight)*b})

result={'purpose':'scope counterexample; task meaning is not implied by stability','normal_direction_field_checks':checks,'exact_information':information,'gaussian_tasks':tasks,'positive_invariant_rectangular_tasks':rectangles,
        'limitations':['f_alpha is a declared perturbation family, not a solved nonlinear flow endpoint','Gaussian observation noise and task weights are evaluation assumptions, not consequences of contrastive training','v is not positive-invariant; separate rectangular a/b comparison addresses that caveat','Task dependence is established knowledge, not a new publication contribution']}
(HERE/'task_meaning_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'field_checks':checks,'information':information,'rectangle_sigma_half': [r for r in rectangles if r['sigma']==.5]},indent=2))
