from core import *; from style import *
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
m=1.0
def exact_T2(Om,C):
    g2=2*m*C
    w=np.sqrt(Om**2 - 1j*g2/(2*np.sqrt(np.maximum(Om**2-m**2,1e-6)+0j)))  # guess
    w=w.real - 1j*np.abs(w.imag)
    for _ in range(80):
        s=-1j*np.sqrt(w**2-m**2); F=w**2-Om**2+g2/(2*s)
        ds=-1j*w/np.sqrt(w**2-m**2); dF=2*w - g2*ds/(2*s**2)
        w=w-F/dF
    return 2/(-2*w.imag)
Om=np.linspace(0.3,3.2,420); Cs=np.logspace(-3,0,300)
O,Cg=np.meshgrid(Om,Cs)
T=np.full(O.shape,np.nan); cont=O>1.0
T[cont]=exact_T2(O[cont],Cg[cont])
fig,ax=plt.subplots(figsize=(6.6,4.4))
pc=ax.pcolormesh(O,Cg,np.where(cont&(Cg<O**2),T,np.nan),norm=LogNorm(vmin=3,vmax=3e4),cmap='viridis',shading='auto',rasterized=True)
cb=plt.colorbar(pc,ax=ax,pad=0.02); cb.set_label(r'coherence time $T_2\,m$')
ax.fill_between(Om,1e-3,1,where=Om<=1.0,color=TEAL,alpha=0.18,lw=0)
ax.fill_between(Om,np.minimum(Om**2,1),1,where=Om<=1.0001e9,color=CRIMSON,alpha=0.22,lw=0)
ax.plot(Om,np.minimum(Om**2,1),color=CRIMSON,lw=1.8)
ax.axvline(1.0,color=ORANGE,lw=2.2)
Tm=np.where(cont&(Cg<O**2),T,np.nan)
ax.contour(O,Cg,Tm,levels=[10,100,1000,10000],colors='white',linewidths=0.9)
for lv,(xx) in [(10,1.75),(100,2.6),(1000,2.6),(10000,2.6)]:
    yy=2*xx*np.sqrt(xx**2-1)/lv
    ax.text(xx,yy*1.12,rf'$T_2m=10^{{{int(np.log10(lv))}}}$',color='white',fontsize=8.6,ha='center',va='bottom',rotation=12)
ax.set_yscale('log'); ax.set_xlabel(r'mode frequency $\Omega/m$'); ax.set_ylabel(r'Yuanon connectivity $C/m^2$')
ax.text(0.62,2.2e-3,'I  bound\n(no decay,\n$T_2\\to\\infty$)',ha='center',color='#0e6655',fontsize=10.3,fontweight='bold')
ax.text(1.04,1.15e-2,'II  band edge\n$T_2\\propto C^{-2/3}$',color=ORANGE,fontsize=9.8,fontweight='bold')
ax.text(1.95,4.0e-3,'III  Markovian\n$T_2\\propto C^{-1}$',color='white',fontsize=10.3,fontweight='bold',ha='center')
ax.text(0.52,0.5,'IV  symmetry\nbroken\n$C>\\mu^2$',color=CRIMSON,fontsize=7.8,fontweight='bold',ha='center')
ax.set_xlim(0.3,3.2); ax.set_ylim(1e-3,1)
plt.tight_layout(); plt.savefig('figs/F_fig5_phasediagram.png'); plt.savefig('figs/F_fig5_phasediagram.pdf')
# validate solver vs mp
print(exact_T2(np.array([2.0]),np.array([0.04])), 2/(-2*pole(2.0,1.0,0.08).imag))
