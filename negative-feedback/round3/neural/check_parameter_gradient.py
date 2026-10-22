"""Independent scalar-loss finite difference of the shared manual parameter backward."""
from pathlib import Path
import json,numpy as np
from model import dataset,random,forward,value_gradient,CUT,KEYS
from oracle import policy
from view_spectrum import positive
ROOT=Path(__file__).resolve().parent

def main():
    x,_,_=dataset();v=random(3801);q=policy(forward(x,v)[0]);P=.95*np.eye(16)+.05*positive(4)
    loss,g=value_gradient(v,x,P,4,q,L=96);rows=[];h=1e-6
    for block,key in enumerate(KEYS):
        for j in np.linspace(CUT[block],CUT[block+1]-1,5,dtype=int):
            vp=v.copy();vm=v.copy();vp[j]+=h;vm[j]-=h
            numerical=(value_gradient(vp,x,P,4,q,L=96)[0]-value_gradient(vm,x,P,4,q,L=96)[0])/(2*h)
            err=abs(numerical-g[j]);rel=err/max(abs(numerical),abs(g[j]),1e-15)
            rows.append({'block':key,'index':int(j),'analytic':float(g[j]),'loss_finite_difference':float(numerical),
                         'absolute_error':float(err),'relative_error':float(rel),
                         'relative_check_applicable':bool(abs(g[j])>1e-5),
                         'passed':bool(err<1e-6 and (abs(g[j])<=1e-5 or rel<1e-5))})
    out={'seed':3801,'K':4,'rho':.05,'q':'frozen at random reference','quadrature_nodes':96,'h':h,'rows':rows,
         'max_absolute_error':max(r['absolute_error'] for r in rows),
         'max_applicable_relative_error':max(r['relative_error'] for r in rows if r['relative_check_applicable']),
         'all_passed':bool(all(r['passed'] for r in rows))}
    (ROOT/'results'/'parameter_gradient_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2));assert out['all_passed']
if __name__=='__main__':main()
