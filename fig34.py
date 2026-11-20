from core import *; from style import *
import matplotlib.pyplot as plt, json
m=1.0; C=0.04; g2=2*m*C; g=np.sqrt(g2)
# ---------- Fig 3: time-domain regimes
fig,axs=plt.subplots(1,3,figsize=(11,3.3),sharey=True)
cases=[(0.75,TEAL,'gap: $\\Omega=0.75m$'),(1.0,ORANGE,'band edge: $\\Omega=m$'),(2.0,NAVY,'continuum: $\\Omega=2m$')]
for ax,(Om,c,lab) in zip(axs,cases):
    t,P,E=simulate(Om,m,g,T=400)
    ax.plot(t,P,color=c,lw=0.3,alpha=0.8,rasterized=True)
    if Om>m:
        gam=markov_gamma(Om,m,g2); ax.plot(t,np.exp(-gam*t/2),'k--',lw=1.2,label=r'$e^{-t/T_2}$, $T_2=2\Omega\sqrt{\Omega^2-m^2}/(mC)$')
        ax.plot(t,-np.exp(-gam*t/2),'k--',lw=1.2)
    elif Om==1.0:
        ax.axhline(2/3,color='k',ls='--',lw=1.2,label='coherent plateau $=2/3$ (universal)'); ax.axhline(-2/3,color='k',ls='--',lw=1.2)
    else:
        wb=bound_freq(Om,m,g2); x=m**2-wb**2; Fp=2*wb+g2*wb/(2*x**1.5); A=2*wb/Fp
        ax.axhline(A,color='k',ls='--',lw=1.2,label=f'bound-state amplitude $={A:.3f}$'); ax.axhline(-A,color='k',ls='--',lw=1.2)
    ax.set_title(lab,color=c,fontweight='bold'); ax.set_xlabel(r'time $t\,m$'); ax.set_xlim(0,400); ax.legend(loc='lower right',fontsize=8.6,frameon=True,facecolor='white',framealpha=0.92,edgecolor='none')
axs[0].set_ylabel(r'mind-field amplitude $\Psi(t)/\Psi(0)$'); axs[0].set_ylim(-1.15,1.15)
for a,l in zip(axs,'abc'): tag(a,l,x=-0.08)
plt.tight_layout(); plt.savefig('figs/F_fig3_timedomain.png'); plt.savefig('figs/F_fig3_timedomain.pdf'); plt.close()

# ---------- Fig 4: scaling laws
Cs=np.logspace(-3,-0.7,14)
res={}
fig,axs=plt.subplots(1,2,figsize=(10,3.9))
ax=axs[0]
for Om,c in [(1.5,PURPLE),(2.0,NAVY),(3.0,TEAL)]:
    T2th=2*Om*np.sqrt(Om**2-m**2)/(m*Cs)
    T2ex=[]
    for Cv in Cs:
        r=pole(Om,m,2*m*Cv,guess=mp.mpc(Om,-1e-3)); T2ex.append(2/(-2*r.imag))
    ax.loglog(Cs,T2th,color=c,lw=2,label=rf'$\Omega={Om}m$  (theory, slope $-1$)')
    ax.loglog(Cs,T2ex,'o',color=c,mfc='white',ms=5,mew=1.3)
    res[str(Om)]=list(T2ex)
# band edge
T2e=[]
for Cv in Cs:
    g2v=2*m*Cv; x=(g2v/2)**(2/3); r=pole(1.0,m,g2v,guess=mp.sqrt(m**2-x*mp.e**(2j*mp.pi/3))); T2e.append(2/(-2*r.imag))
ax.loglog(Cs,4/(np.sqrt(3)*(m*Cs)**(2/3)/m),color=ORANGE,lw=2,label=r'$\Omega=m$  (theory, slope $-2/3$)')
ax.loglog(Cs,T2e,'o',color=ORANGE,mfc='white',ms=5,mew=1.3)
# simulation points
simpts=[]
for Om,c in [(2.0,NAVY)]:
    for Cv in [0.005,0.01,0.02,0.05,0.1]:
        t,P,E=simulate(Om,m,np.sqrt(2*m*Cv),T=min(300,8/markov_gamma(Om,m,2*m*Cv)))
        gm=fit_rate(t,E,5,t[-1]*0.95); simpts.append((Cv,2/gm)); ax.loglog(Cv,2/gm,'s',color=CRIMSON,ms=6,zorder=5)
ax.loglog([],[],'o',color='k',mfc='white',label='exact complex pole'); ax.loglog([],[],'s',color=CRIMSON,label='lattice simulation ($\\Omega=2m$)')
ax.set_xlabel(r'Yuanon connectivity strength $C/m^2$'); ax.set_ylabel(r'coherence time $T_2\,m$'); ax.legend(fontsize=8.4,loc='lower left'); tag(ax,'a')
ax=axs[1]
Oms=np.linspace(1.001,4,400)
for Cv,c in [(0.01,NAVY),(0.05,PURPLE)]:
    ax.semilogy(Oms,2*Oms*np.sqrt(Oms**2-m**2)/(m*Cv),color=c,lw=2,label=rf'Markov law, $C={Cv}m^2$')
    ex=[]; Omx=np.linspace(1.02,4,40)
    for Om in Omx:
        r=pole(Om,m,2*m*Cv,guess=mp.mpc(Om,-1e-3)); ex.append(2/(-2*r.imag))
    ax.semilogy(Omx,ex,'o',color=c,mfc='white',ms=4)
ax.axvspan(0.5,1.0,color=TEAL,alpha=0.12,lw=0); ax.text(0.75,3e3,'gap:\n$T_2\\to\\infty$\n(bound)',ha='center',color=TEAL,fontsize=9.8)
ax.set_xlim(0.5,4); ax.set_ylim(5,1e4); ax.set_xlabel(r'mode frequency $\Omega/m$'); ax.set_ylabel(r'$T_2\,m$')
ax.annotate('band-edge collapse\n(non-Markovian)',xy=(1.03,12),xytext=(1.25,30),fontsize=9.2,arrowprops=dict(arrowstyle='->',color=GRAY))
ax.legend(loc='lower right'); tag(ax,'b')
plt.tight_layout(); plt.savefig('figs/F_fig4_scaling.png'); plt.savefig('figs/F_fig4_scaling.pdf')
json.dump({'sim':simpts},open('fig4_sim.json','w'))
print(simpts)
