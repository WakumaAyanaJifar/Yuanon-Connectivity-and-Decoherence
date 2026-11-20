from core import *; from style import *
import matplotlib.pyplot as plt
m=1.0
fig,axs=plt.subplots(1,3,figsize=(11,3.4))
w=np.linspace(0.01,3,2000)
re=np.where(w<m,1/(2*np.sqrt(np.abs(m**2-w**2))),np.nan); im=np.where(w>m,1/(2*np.sqrt(np.abs(w**2-m**2))),np.nan)
re[w>=m]=0; re=np.where(w>=m,np.nan,re)
ax=axs[0]; ax.axvspan(0,m,color=TEAL,alpha=0.10,lw=0)
ax.plot(w,re,color=NAVY,lw=2,label=r'Re $\tilde G_D$ (dispersive)')
ax.plot(w[w>m],0*w[w>m],color=NAVY,lw=2); ax.plot(w[w<m],0*w[w<m],color=CRIMSON,lw=2); ax.plot(w,im,color=CRIMSON,lw=2,label=r'Im $\tilde G_D$ (absorptive)')
ax.set_ylim(0,3); ax.set_xlim(0,3); ax.set_xlabel(r'$\omega/m$'); ax.set_ylabel(r'$m\,\tilde G_D$')
ax.text(0.5,2.2,'gap:\nno\nabsorption',ha='center',color=TEAL,fontsize=9.8)
ax.annotate(r'$\propto(\omega^2-m^2)^{-1/2}$'+'\n(1D band edge)',xy=(1.1,1.1),xytext=(1.55,1.55),fontsize=9.8,arrowprops=dict(arrowstyle='->',color=GRAY))
ax.legend(loc='upper right',bbox_to_anchor=(1.02,1.0)); tag(ax,'a')
ax=axs[1]; q=np.linspace(-3,3,400); ax.fill_between(q,np.sqrt(m**2+q**2),3.3,color=CRIMSON,alpha=0.08,lw=0)
ax.plot(q,np.sqrt(m**2+q**2),color=CRIMSON,lw=2)
for Om,lab,c in [(0.75,r'$\Omega<m$: bound',TEAL),(1.0,r'$\Omega=m$: band edge',ORANGE),(2.0,r'$\Omega>m$: radiates',NAVY)]:
    ax.axhline(Om,color=c,lw=1.6,ls='--'); ax.text(-2.9,Om+(0.07 if Om!=0.75 else -0.2),lab,color=c,fontsize=9.8)
ax.set_xlim(-3,3); ax.set_ylim(0,3.3); ax.set_xlabel(r'auxiliary momentum $q/m$'); ax.set_ylabel(r'frequency $\omega/m$')
ax.text(1.3,2.75,'thought-field\ncontinuum',color=CRIMSON,fontsize=9.8,ha='center'); tag(ax,'b')
ax=axs[2]
for Om,c in [(1.5,PURPLE),(2.0,NAVY),(3.0,TEAL)]:
    rs=[]; 
    for C in np.linspace(0.005,0.6,40):
        g2=2*m*C; rs.append(pole(Om,m,g2,guess=mp.mpc(Om,-0.001)))
    rs=np.array(rs); ax.plot(rs.real,rs.imag,'-',color=c,lw=2,label=rf'$\Omega={Om}m$')
    ax.plot(rs.real[-1],rs.imag[-1],'o',color=c,ms=4)
rs=[]
for C in np.linspace(0.002,0.12,40):
    g2=2*m*C; x=(g2/2)**(2/3); rs.append(pole(1.0,m,g2,guess=mp.sqrt(m**2-x*mp.e**(2j*mp.pi/3))))
rs=np.array(rs); ax.plot(rs.real,rs.imag,'-',color=ORANGE,lw=2,label=r'$\Omega=m$ (edge)')
ax.plot([m,3.3],[0,0],color=CRIMSON,lw=3,alpha=0.5); ax.text(2.2,0.006,'branch cut',color=CRIMSON,fontsize=9.2)
ax.set_xlabel(r'Re $\omega/m$'); ax.set_ylabel(r'Im $\omega/m$'); ax.set_xlim(0.9,3.3)
ax.annotate('increasing $C$',xy=(2.03,-0.075),xytext=(2.25,-0.11),fontsize=9.2,arrowprops=dict(arrowstyle='->',color=GRAY))
ax.legend(loc='lower left'); tag(ax,'c')
plt.tight_layout(); plt.savefig('figs/F_fig2_spectral.png'); plt.savefig('figs/F_fig2_spectral.pdf')
