import numpy as np, mpmath as mp
# MTE conventions (Ning, PhilArchive NINGME): omega^2 = mu^2 - g^2 G_D(omega), G_D(omega,k=0) = 1/(2 sqrt(m^2-omega^2)), retarded
def GD_cont(w, m):
    s = mp.sqrt(m**2 - w**2)
    if mp.re(w) > m and mp.im(s) > 0: s = -s   # continue onto the second (decaying) sheet
    return 1/(2*s)
def pole(mu, m, g2, guess=None):
    f = lambda w: w**2 - mu**2 + g2*GD_cont(w, m)
    if guess is None: guess = mp.mpc(mu, -0.01)
    r = mp.findroot(f, guess)
    return complex(r)
def markov_gamma(Om, m, g2):
    return g2/(2*Om*np.sqrt(Om**2-m**2))
def bound_freq(mu, m, g2):
    # real root below m on physical sheet (requires mu^2 - C > 0)
    f = lambda w: w**2 - mu**2 + g2/(2*mp.sqrt(m**2-w**2))
    try:
        r = mp.findroot(f, (mp.mpf(1e-6), mp.mpf(m)-mp.mpf(1e-12)), solver='bisect')
        return float(r)
    except Exception: return np.nan

# lattice simulation: Psi'' = -mu^2 Psi + g phi_0 ; phi_j'' = lap - m^2 phi_j + (g/a) Psi delta_j0
def simulate(mu, m, g, T=300., a=0.05, dt=0.01, L=None, rec_every=5):
    if L is None: L = T*1.05 + 5
    N = int(L/a); n = 2*N+1; c = N
    phi = np.zeros(n); pphi = np.zeros(n)
    Psi, pPsi = 1.0, 0.0
    def acc(phi, Psi):
        lap = np.empty_like(phi)
        lap[1:-1] = phi[2:]-2*phi[1:-1]+phi[:-2]
        lap[0] = phi[1]-2*phi[0]; lap[-1] = phi[-2]-2*phi[-1]   # Dirichlet walls at |y|=L
        aphi = lap/a**2 - m**2*phi
        aphi[c] += g/a*Psi
        aPsi = -mu**2*Psi + g*phi[c]
        return aphi, aPsi
    aphi, aPsi = acc(phi, Psi)
    steps = int(T/dt); ts=[]; Ps=[]; Es=[]
    for s in range(steps):
        pphi += 0.5*dt*aphi; pPsi += 0.5*dt*aPsi
        phi += dt*pphi; Psi += dt*pPsi
        aphi, aPsi = acc(phi, Psi)
        pphi += 0.5*dt*aphi; pPsi += 0.5*dt*aPsi
        if s % rec_every == 0:
            ts.append(s*dt); Ps.append(Psi); Es.append(0.5*pPsi**2+0.5*mu**2*Psi**2)
    return np.array(ts), np.array(Ps), np.array(Es)

def fit_rate(t, E, t0, t1):
    # envelope of E: local maxima of E (E oscillates at 2*Omega around a slow decay); use running max
    sel = (t>t0)&(t<t1)
    tt, ee = t[sel], E[sel]
    # coarse-grain over windows
    w = max(1, len(tt)//200)
    k = len(tt)//w
    tm = tt[:k*w].reshape(k,w).mean(1); em = ee[:k*w].reshape(k,w).max(1)
    p = np.polyfit(tm, np.log(em), 1)
    return -p[0]
