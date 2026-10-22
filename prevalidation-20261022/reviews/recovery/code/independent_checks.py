"""Independent exact-flow checks. Run from any directory; writes adjacent results/."""
from pathlib import Path
import csv
import json
import platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)
N, M = 3, 2
ETA, BETA = .02, .2
R = np.diag([.8, .6])


def pack(a, b, c):
    return np.concatenate([a.ravel(), b.ravel(), c.ravel()])


def unpack(z):
    return z[:6].reshape(N, M), z[6:15].reshape(N, N), z[15:].reshape(N, M)


def flow(z):
    a, b, c = unpack(z)
    residual = -b @ a + c @ R
    return pack(b.T @ residual - ETA*a,
                residual @ a.T - ETA*b,
                BETA*(a-c))


def rotate(z, q):
    a, b, c = unpack(z)
    return pack(q @ a, q @ b @ q.T, q @ c)


rng = np.random.default_rng(2718)
s = (np.diag(R)+np.sqrt(np.diag(R)**2-4*ETA))/2
a = np.zeros((N, M)); a[:M, :] = np.diag(s)
b = np.diag([*s, 0.])
z = pack(a, b, a)
k0 = rng.normal(size=(N, N)); k = k0-k0.T
k /= np.linalg.norm(k)
q = expm(.01*k)
neighbor = rotate(z, q)
random_z = rng.normal(size=z.size)
tangent = pack(k@a, k@b-b@k, k@a)
symmetry = {
    "equilibrium_residual": float(np.linalg.norm(flow(z))),
    "neighbor_equilibrium_residual": float(np.linalg.norm(flow(neighbor))),
    "neighbor_distance": float(np.linalg.norm(neighbor-z)),
    "equivariance_residual": float(np.linalg.norm(flow(rotate(random_z,q))-rotate(flow(random_z),q))),
    "tangent_norm": float(np.linalg.norm(tangent)),
    "jacobian_tangent": [],
}
for h in [1e-4, 1e-5, 1e-6]:
    jac = np.column_stack([(flow(z+h*np.eye(z.size)[i])-flow(z-h*np.eye(z.size)[i]))/(2*h)
                           for i in range(z.size)])
    eig = np.linalg.eigvals(jac)
    symmetry["jacobian_tangent"].append({
        "h": h,
        "action_norm": float(np.linalg.norm(jac@tangent)),
        "small_eigenvalue_count_at_1e-7": int(np.sum(np.abs(eig)<1e-7)),
        "max_real_eigenvalue": float(np.max(eig.real)),
    })

# Balanced SimSiam/no-EMA limit: w=p=s, teacher=w, zero decay.
rho, threshold = .8, .4
def primitive(x):
    return np.log(x/(rho-x))/rho**2-1/(rho*x)

rows = []
def event(t, y):
    return y[0]-threshold
event.terminal = True
event.direction = 1
for initial in [.001, .003, .01, .03, .1]:
    exact = primitive(threshold)-primitive(initial)
    sol = solve_ivp(lambda t,y: y*y*(rho-y), (0,exact*1.2+1), [initial],
                    events=event, rtol=1e-10, atol=1e-13, max_step=2.)
    observed = float(sol.t_events[0][0])
    rows.append({"initial":initial,"rho":rho,"threshold":threshold,
                 "exact_time":float(exact),"ode_event_time":observed,
                 "relative_error":abs(observed-exact)/exact})
with (OUT/"delay_control.csv").open("w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
result = {"symmetry":symmetry,"delay_max_relative_error":max(r["relative_error"] for r in rows),
          "environment":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__},
          "seed":2718}
(OUT/"independent_checks.json").write_text(json.dumps(result,indent=2)+"\n")
assert symmetry["equilibrium_residual"] < 1e-10
assert symmetry["neighbor_equilibrium_residual"] < 1e-10
assert symmetry["equivariance_residual"] < 1e-10
assert all(d["action_norm"]<1e-7 for d in symmetry["jacobian_tangent"])
assert result["delay_max_relative_error"]<1e-5
print(json.dumps(result,indent=2))
