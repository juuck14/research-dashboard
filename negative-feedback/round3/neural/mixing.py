from pathlib import Path
import sys,csv,json,numpy as np
from view_spectrum import reference,positive,jacobian
from oracle import policy
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'
sys.path.insert(0,str(ROOT.parents[1]/'round2'/'theory'/'code'))
from verify_controls import moments
from verify_general import counts3,A,B

def predicted(K,rho,m=4):
    mo=moments(K,'natural',1);ct,lc=counts3(K);U,N,W=ct.T
    prob=np.exp(lc+ct@np.log([mo['u'],2*mo['v'],mo['w']]))
    D=1+U+A*N+B*W;mass=float(prob@((D-1)/D));lp=mo['normal_one'];lb=mo['adaptive_balance']
    normal=(lp-.5*mass*(1-rho))/m;plane=normal+.5*lb/m
    mean=np.sort([lb]+[mo['adaptive_ab']]*2+[lp]*6+[mo['normal_ab']]*6+[0]*13)/m
    spectrum=np.sort(np.concatenate([mean,np.repeat(plane,4*(m-1)),np.repeat(normal,4*(m-1)*6)]))
    return {'K':K,'rho':rho,'negative_softmax_mass':mass,'critical_rho':1-2*lp/mass,
            'mean_balance':lb/m,'within_normal':normal,'within_plane':plane,
            'full_stable':bool(min(lb,mo['adaptive_ab'],lp,mo['normal_ab'],normal,plane)>1e-10)},spectrum

def main():
    rows=[]
    for K in range(1,129):
        for rho in [0,.025,.05,.075,.1,.15,.3,1]:rows.append(predicted(K,rho)[0])
    checks=[];f=reference(4);I=np.eye(16);P=positive(4)
    for K in [3,5,16,64]:
        for rho in [0,.05,.1,.2,1]:
            H,T=jacobian(f,(1-rho)*I+rho*P,K)
            ev=np.linalg.eigvalsh((H+H.T)/2);row,pr=predicted(K,rho)
            checks.append({'K':K,'rho':rho,'max_spectrum_error':float(np.max(np.abs(ev-pr))),
                           'observed_negative':int(np.sum(ev< -1e-7)),'predicted_negative':int(np.sum(pr< -1e-7)),
                           'symmetry_error':float(np.max(abs(H-H.T)))})
    with (OUT/'mixing_curve.csv').open('w') as file:
        wr=csv.DictWriter(file,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    with (OUT/'mixing_fd.csv').open('w') as file:
        wr=csv.DictWriter(file,fieldnames=list(checks[0]));wr.writeheader();wr.writerows(checks)
    groups=[]
    for rho in [0,.025,.05,.075,.1,.15,.3,1]:
        chosen=[r for r in rows if r['rho']==rho];stable=[r['K'] for r in chosen if r['full_stable']]
        groups.append({'rho':rho,'stable_K_in_1_128':stable,'critical_rho_K1':chosen[0]['critical_rho'],
                       'critical_rho_K5':chosen[4]['critical_rho'],'critical_rho_K128':chosen[-1]['critical_rho']})
    summary={'fd_checks':len(checks),'max_spectrum_error':max(r['max_spectrum_error'] for r in checks),'groups':groups}
    (OUT/'mixing_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
    assert summary['max_spectrum_error']<1e-7
if __name__=='__main__':main()
