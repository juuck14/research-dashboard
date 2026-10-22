"""Fixed post hoc measurement audit; does not change encoder training or primary gates."""
import json,platform
from pathlib import Path
import numpy as np
import scipy
import run_encoder as e

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'

def ols(ft,y,fz):
    mx=ft.mean(0);my=y.mean(0)
    w=np.linalg.lstsq(ft-mx,y-my,rcond=1e-10)[0]
    pred=(fz-mx)@w+my
    return np.mean((pred>0)==(e.YTEST>0),axis=0)

def main():
    models=json.loads((OUT/'models.json').read_text());rows=[]
    for name,raw in models.items():
        p={k:np.array(v) for k,v in raw.items()};ft,_=e.forward(e.XTRAIN,p);fz,_=e.forward(e.XTEST,p)
        a=ols(ft,e.YTRAIN,fz)
        rng=np.random.default_rng(9031);nt=ft+e.CFG['feature_noise']*rng.normal(size=ft.shape);nz=fz+e.CFG['feature_noise']*rng.normal(size=fz.shape)
        b=ols(nt,e.YTRAIN,nz)
        rows.append({'name':name,'ols_a':float(a[0]),'ols_b':float(a[1]),'worst_ols':float(a.min()),'noise_ols_a':float(b[0]),'noise_ols_b':float(b[1]),'worst_noise_ols':float(b.min()),'min_feature_singular_value':float(np.linalg.svd(ft-ft.mean(0),compute_uv=False)[-1]),'max_unit_norm_error':float(np.max(np.abs(np.linalg.norm(fz,axis=1)-1)))})
    (OUT/'ols_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
    initials=[];initmodels={}
    for seed in e.CFG['primary']+e.CFG['confirmation']:
        for arm in ['warmup','pca']:
            p=e.random_params(seed) if arm=='warmup' else e.pca_params(seed)
            if arm=='warmup':p,_=e.train(p,seed+10000,'uniform',e.CFG['warmup_steps'])
            x1,x2=e.batch(np.random.default_rng(seed+20000),e.CFG['batch'])
            f1,_=e.forward(x1,p);f2,_=e.forward(x2,p);s=f1@f2.T
            q=e.sampler(s,'adaptive');mask=~np.eye(len(q),dtype=bool)
            la,ga=e.lossgrad(x1,x2,p,'adaptive');lf,gf=e.lossgrad(x1,x2,p,'frozen',p)
            initials.append({'seed':seed,'arm':arm,**e.evaluate(p),'fork_loss_difference':abs(la-lf),'fork_gradient_max_difference':max(float(np.max(np.abs(ga[k]-gf[k]))) for k in p),'min_negative_probability':float(q[mask].min()),'theoretical_probability_floor':e.CFG['epsilon']/(len(q)-1)})
            initmodels[f'{seed}/{arm}']={k:v.tolist() for k,v in p.items()}
    (OUT/'initial_probe_audit.json').write_text(json.dumps(initials,indent=2)+'\n')
    (OUT/'models_initial.json').write_text(json.dumps(initmodels)+'\n')
    check=json.loads((OUT/'gradient_check.json').read_text());non=[r for r in check['checks'] if abs(r['analytic'])>1e-6]
    audit={'max_relative_gradient_error_non_tiny':max(r['abs_error']/abs(r['analytic']) for r in non),'min_abs_derivative_checked':min(abs(r['analytic']) for r in non),'initial_probes_reconstructed_from_fixed_seeds':len(initials),'final_ols_models':len(rows),'maximum_fork_loss_difference':max(r['fork_loss_difference'] for r in initials),'maximum_fork_gradient_difference':max(r['fork_gradient_max_difference'] for r in initials),'maximum_unit_norm_error':max(r['max_unit_norm_error'] for r in rows),'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__}
    (OUT/'audit_summary.json').write_text(json.dumps(audit,indent=2)+'\n')
    print(json.dumps(audit))

if __name__=='__main__':main()
