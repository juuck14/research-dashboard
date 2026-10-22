"""Read-only audit of learned encoder gradients and stored OLS results.

The source module writes config.json at import time. Its AST is loaded with that
one top-level write removed; all model/training/probe functions stay unchanged.
No files in the encoder author's directory are written by this audit.
"""
from pathlib import Path
import ast,json
import numpy as np

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'encoder'/'run_encoder.py'
tree=ast.parse(SOURCE.read_text())
removed=[]
kept=[]
for item in tree.body:
    if isinstance(item,ast.Expr) and isinstance(item.value,ast.Call):
        call=item.value
        if isinstance(call.func,ast.Attribute) and call.func.attr=='write_text':
            removed.append(ast.unparse(item));continue
    kept.append(item)
assert len(removed)==1 and 'config.json' in removed[0]
tree.body=kept
scope={'__file__':str(SOURCE),'__name__':'encoder_readonly_audit'}
exec(compile(ast.fix_missing_locations(tree),str(SOURCE),'exec'),scope)

checks=[]
for seed in [4391,5017]:
    p=scope['random_params'](seed)
    frozen=scope['random_params'](seed+101)
    rng=np.random.default_rng(seed+1)
    x1,x2=scope['batch'](rng,9)
    f1,_=scope['forward'](x1,p);f2,_=scope['forward'](x2,p)
    z1,_=scope['forward'](x1,frozen);z2,_=scope['forward'](x2,frozen)
    for policy in ['uniform','adaptive','frozen']:
        q=scope['sampler'](z1@z2.T if policy=='frozen' else f1@f2.T,
                           'adaptive' if policy=='frozen' else policy)
        value,grad=scope['lossgrad'](x1,x2,p,policy,frozen)
        coordinates=[(key,i) for key,val in p.items() for i in range(val.size)]
        selected=rng.choice(len(coordinates),25,replace=False)
        for index in selected:
            key,i=coordinates[index];old=p[key].flat[i];h=1e-6
            p[key].flat[i]=old+h
            hi=scope['lossgrad'](x1,x2,p,policy,q_override=q,need_grad=False)
            p[key].flat[i]=old-h
            lo=scope['lossgrad'](x1,x2,p,policy,q_override=q,need_grad=False)
            p[key].flat[i]=old
            numeric=(hi-lo)/(2*h);analytic=float(grad[key].flat[i])
            checks.append(dict(seed=seed,policy=policy,parameter=key,index=i,
                               analytic=analytic,finite_difference=numeric,
                               absolute_error=abs(numeric-analytic)))
    va,ga=scope['lossgrad'](x1,x2,p,'adaptive')
    vf,gf=scope['lossgrad'](x1,x2,p,'frozen',p)
    assert va==vf
    assert all(np.array_equal(ga[key],gf[key]) for key in p)

model_source=SOURCE.parent/'results'/'models.json'
model_values=json.loads(model_source.read_text())
expected={row['name']:row for row in json.loads((SOURCE.parent/'results'/'ols_audit.json').read_text())}
ols=[]
for name,raw in model_values.items():
    p={key:np.array(val) for key,val in raw.items()}
    ft,_=scope['forward'](scope['XTRAIN'],p);fz,_=scope['forward'](scope['XTEST'],p)
    mx=ft.mean(0);my=scope['YTRAIN'].mean(0)
    # Independent pseudoinverse calculation, compared with saved lstsq results.
    weights=np.linalg.pinv(ft-mx,rcond=1e-10)@(scope['YTRAIN']-my)
    prediction=(fz-mx)@weights+my
    accuracy=np.mean((prediction>0)==(scope['YTEST']>0),axis=0)
    error=max(abs(float(accuracy[0])-expected[name]['ols_a']),
              abs(float(accuracy[1])-expected[name]['ols_b']))
    ols.append(dict(name=name,ols_a=float(accuracy[0]),ols_b=float(accuracy[1]),
                    saved_result_error=error))

summary=dict(gradient_coordinates=len(checks),
             max_absolute_gradient_error=max(row['absolute_error'] for row in checks),
             max_relative_gradient_error_non_tiny=max(row['absolute_error']/abs(row['analytic']) for row in checks if abs(row['analytic'])>1e-6),
             reconstructed_clean_ols_models=len(ols),
             max_saved_ols_accuracy_discrepancy=max(row['saved_result_error'] for row in ols),
             matched_fork_checks=2,
             source_ast_top_level_writes_removed=removed,
             checks=checks,ols=ols)
destination=HERE/'results'/'encoder_independent_audit.json'
destination.write_text(json.dumps(summary,indent=2)+'\n')
assert summary['max_absolute_gradient_error']<1e-6
assert summary['max_saved_ols_accuracy_discrepancy']==0
print(json.dumps({key:value for key,value in summary.items() if key not in ['checks','ols','source_ast_top_level_writes_removed']},indent=2))
