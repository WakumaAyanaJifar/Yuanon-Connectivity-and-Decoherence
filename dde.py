import numpy as np
from core import simulate, markov_gamma
def dde(gam, tau, R, T, dt=0.01):
    """Lossless input-output delay model: emitter a, symmetric two-sided channels,
    perfect mirrors at distance L: in(t) = R * out(t - tau), out = in - i sqrt(gam/2) a."""
    n=int(T/dt); d=int(round(tau/dt)); k=np.sqrt(gam/2)
    a=np.zeros(n,complex); out=np.zeros(n,complex); a[0]=1.0
    for i in range(n-1):
        inn = R*out[i-d] if i>=d else 0.0
        out[i]= inn - 1j*k*a[i]
        # RK2 on a with frozen input over the step
        f=lambda aa: -0.5*gam*aa - 1j*k*2*inn
        a1=a[i]+dt*f(a[i]); a[i+1]=a[i]+0.5*dt*(f(a[i])+f(a1))
    i=n-1; inn = R*out[i-d] if i>=d else 0.0; out[i]=inn-1j*k*a[i]
    return np.arange(n)*dt, a
def lattice_k(Om,a,m=1.0): return 2/a*np.arcsin(a*np.sqrt(Om**2-m**2)/2)
def vg(k,a,Om=2.0): return np.sin(k*a)/(a*Om)
if __name__=='__main__':
    m=1.0; Om=2.0; C=0.02; g2=2*m*C; g=np.sqrt(g2); a_lat=0.05
    gam=markov_gamma(Om,m,g2)
    def lattice_k(Om,a):  # Om^2 = m^2 + (4/a^2) sin^2(ka/2)
        return 2/a*np.arcsin(a*np.sqrt(Om**2-m**2)/2)
    def vg(k,a): return np.sin(k*a)/(a*Om)
    rows=[]
    for Lw in [10,20,40,60,90,130,180,250]:
        N=int(Lw/a_lat); Leff=(N+1)*a_lat; k=lattice_k(Om,a_lat); tau=2*Leff/vg(k,a_lat)
        t,P,E=simulate(Om,m,g,T=4*tau,L=Lw,rec_every=10)
        lam_sim=1-np.abs(P[t>tau]).max()
        R=-np.exp(1j*2*k*Leff)
        td,ad=dde(gam,tau,R,4*tau)
        lam_dde=1-np.abs(ad[td>tau]).max()
        th=np.angle(R)
        rows.append((Lw,tau/(2/gam),th,lam_sim,lam_dde)); print(rows[-1],flush=True)
    np.save('dde_rows.npy',np.array(rows))
