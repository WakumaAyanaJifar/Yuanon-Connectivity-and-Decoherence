from core import *; from style import *
from dde import dde, lattice_k, vg
import matplotlib.pyplot as plt
m=1.0; Om=2.0; C=0.02; g2=2*m*C; g=np.sqrt(g2); a_lat=0.05
gam=markov_gamma(Om,m,g2); T2=2/gam
rows=np.load('dde_rows.npy')
fig,axs=plt.subplots(1,2,figsize=(12,4.4),gridspec_kw={'width_ratios':[1.35,1]})
ax=axs[0]
def env(t,P,w=60):
    k=len(P)//w; return t[:k*w].reshape(k,w).mean(1), np.abs(P[:k*w]).reshape(k,w).max(1)
for Lw,c in [(30,CRIMSON),(60,ORANGE),(120,PURPLE)]:
    N=int(Lw/a_lat); Leff=(N+1)*a_lat; k=lattice_k(Om,a_lat); tau=2*Leff/vg(k,a_lat)
    t,P,E=simulate(Om,m,g,T=520,L=Lw); te,pe=env(t,P)
    ax.plot(te,pe,color=c,lw=2.2,alpha=0.55,label=rf'lattice, $L={Lw}/m$')
    td,ad=dde(gam,tau,-np.exp(2j*k*Leff),520)
    ax.plot(td,np.abs(ad),'--',color=c,lw=1.3)
t,P,E=simulate(Om,m,g,T=520); te,pe=env(t,P)
ax.plot(te,pe,color=NAVY,lw=2.2,label=r'lattice, $L\to\infty$')
ax.plot([],[],'k--',lw=1.3,label='delay model')
ax.set_xlabel(r'time $t\,m$'); ax.set_ylabel(r'coherence $|\Psi|_{\max}/\Psi(0)$'); ax.set_xlim(0,520); ax.set_ylim(0,1.05)
ax.legend(fontsize=8.8,loc='lower left',ncol=1); tag(ax,'a',x=-0.09)
ax=axs[1]
xs=np.linspace(0.02,2.0,90); ths=np.linspace(-np.pi,np.pi,90)
import os
if os.path.exists('lam_map.npy'): Z=np.load('lam_map.npy')
else:
    Z=np.zeros((len(ths),len(xs)))
    for j,x in enumerate(xs):
        tau=x*T2
        for i,th in enumerate(ths):
            td,ad=dde(gam,tau,np.exp(1j*th),4*tau,dt=max(0.05,tau/400))
            Z[i,j]=1-np.abs(ad[td>tau]).max()
pc=ax.pcolormesh(xs,ths,Z,cmap='magma_r',shading='auto',vmin=0,vmax=0.4,rasterized=True)
cb=plt.colorbar(pc,ax=ax,pad=0.02); cb.set_label(r'irreversibility $\lambda_{\rm QRF}$')
ax.scatter(rows[:,1],rows[:,2],c=rows[:,3],cmap='magma_r',vmin=0,vmax=0.4,s=70,edgecolors='white',linewidths=1.6,zorder=5)
ax.set_xlabel(r'reference size $t_{\rm rev}/T_2$'); ax.set_ylabel(r'round-trip phase $\theta=\arg R$')
ax.set_yticks([-np.pi,0,np.pi]); ax.set_yticklabels([r'$-\pi$','0',r'$\pi$']); tag(ax,'b')
plt.tight_layout(); plt.savefig('figs/F_fig6_frame.png'); plt.savefig('figs/F_fig6_frame.pdf')
