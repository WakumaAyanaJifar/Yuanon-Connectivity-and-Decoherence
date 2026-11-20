from style import *
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Ellipse
fig=plt.figure(figsize=(12,4.2)); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,12); ax.set_ylim(0,4.2); ax.axis('off')
def box(x,y,w,h,ec,fc='white',a=1):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.12',ec=ec,fc=fc,lw=1.4,alpha=a))
# panel a: two-field geometry
box(0.15,0.25,3.7,3.55,NAVY)
ax.text(0.3,3.55,'a  MTE two-field model',fontsize=12.1,fontweight='bold',color='k')
yy=np.linspace(0.6,3.2,300)
X,Y=np.meshgrid(np.linspace(1.05,3.7,200),yy)
Z=np.exp(-np.abs(Y-1.9)*1.6)*(0.6+0.4*np.cos(6*X))
ax.pcolormesh(X,Y,Z,cmap='Reds',alpha=0.45,shading='auto',vmin=0,vmax=1.3,zorder=1.5,rasterized=True)
ax.plot([1.05,3.7],[1.9,1.9],color=NAVY,lw=3)
ax.text(2.55,2.0,'experiential spacetime  $y=0$',color=NAVY,fontsize=9.8,ha='center',va='bottom',fontweight='bold')
ax.text(2.55,1.77,r'mind field $\Psi(x)$',color=NAVY,fontsize=9.8,ha='center',va='top')
ax.text(3.65,3.05,r'thought field $\phi(x,y)$'+'\nin auxiliary space ($n=1$)',color=CRIMSON,fontsize=9.2,ha='right',va='top')
ax.annotate('',xy=(0.75,3.1),xytext=(0.75,0.7),arrowprops=dict(arrowstyle='<->',color=GRAY,lw=1.1)); ax.text(0.62,1.9,'$y$',fontsize=11.5,color=GRAY,ha='right',va='center')
for d in [1,-1]:
    ax.annotate('',xy=(1.35,1.9+d*0.95),xytext=(1.35,1.9+d*0.08),arrowprops=dict(arrowstyle='->',color=CRIMSON,lw=1.3))
ax.text(1.45,1.2,r'$g\,\Psi\,\phi|_{y=0}$',fontsize=9.8,color=CRIMSON)
# arrow a->b
ax.add_patch(FancyArrowPatch((3.95,2.0),(4.45,2.0),arrowstyle='-|>',mutation_scale=16,color='k'))
ax.text(4.2,2.15,'integrate\nout $\\phi$',fontsize=8.6,ha='center',va='bottom')
# panel b: open-system form
box(4.5,0.25,3.6,3.55,TEAL)
ax.text(4.65,3.55,'b  Yuanon = system + structured bath',fontsize=12.1,fontweight='bold')
ax.add_patch(Ellipse((5.25,2.0),0.75,0.75,ec=NAVY,fc='#e8eef8',lw=1.6)); ax.text(5.25,2.0,r'$\Psi$'+'\n'+r'$\Omega$',ha='center',va='center',fontsize=10.3,color=NAVY)
w=np.linspace(0,1,200); xs=6.05+w*1.9
J=np.where(w>0.35,1/np.sqrt(np.maximum((w/0.35)**2-1,1e-4)),0)*0.18
J=np.minimum(J,1.2)
ax.fill_between(xs,1.0,1.0+J,color=CRIMSON,alpha=0.35,lw=0); ax.plot(xs,1.0+J,color=CRIMSON,lw=1.4)
ax.plot([6.05,7.95],[1.0,1.0],color='k',lw=0.8); ax.text(7.95,0.88,r'$\omega$',fontsize=10.3,ha='right',va='top')
ax.text(6.05+0.35*1.9,0.88,'$m$',fontsize=10.3,ha='center',va='top',color=CRIMSON)
ax.text(6.4,2.35,r'$J(\omega)=g^2\,{\rm Im}\,\tilde G_D$',fontsize=9.8,color=CRIMSON)
ax.text(6.3,1.25,'gap',fontsize=9.2,color=TEAL,ha='center')
ax.plot([5.62,6.05],[2.0,1.6],color=GRAY,lw=1.2)
ax.text(6.2,3.05,r'static part $\rightarrow C=g^2\tilde G_D(0,0)$',fontsize=9.2,color=NAVY)
ax.text(6.2,2.8,r'absorptive part $\rightarrow$ $T_2$',fontsize=9.2,color=CRIMSON)
ax.text(6.3,0.5,r'$T_2\propto C^{-1}$, $C^{-2/3}$ or $\infty$',fontsize=10.3,ha='center',fontweight='bold')
ax.add_patch(FancyArrowPatch((8.15,2.0),(8.65,2.0),arrowstyle='-|>',mutation_scale=16,color='k'))
ax.text(8.4,2.15,'same\nkernel',fontsize=8.6,ha='center',va='bottom')
# panel c: physical analogue
box(8.7,0.25,3.15,3.55,ORANGE)
ax.text(8.85,3.55,'c  Laboratory analogue',fontsize=12.1,fontweight='bold')
for i in range(9):
    x0=9.0+i*0.3
    ax.add_patch(Rectangle((x0,1.55),0.22,0.32,ec=GRAY,fc='#fdf2e3',lw=1))
    if i<8: ax.plot([x0+0.22,x0+0.3],[1.71,1.71],color=GRAY,lw=1)
ax.text(10.3,1.35,'band-gap waveguide\n(metamaterial / photonic crystal)',fontsize=8.6,ha='center',va='top',color=GRAY)
ax.add_patch(Rectangle((10.1,2.35),0.4,0.4,ec=NAVY,fc='#e8eef8',lw=1.5)); ax.text(10.3,2.55,'Q',ha='center',va='center',fontsize=10.3,color=NAVY,fontweight='bold')
ax.plot([10.3,10.3],[2.35,1.87],color=NAVY,lw=1.4); ax.text(10.38,2.1,r'$g$',fontsize=9.8,color=NAVY)
ax.text(10.3,2.9,r'qubit at $\omega_q\leftrightarrow\Omega$',fontsize=9.2,ha='center',color=NAVY)
ax.text(10.3,0.5,r'band edge $\omega_c\leftrightarrow m$',fontsize=9.8,ha='center',color=ORANGE,fontweight='bold')
plt.savefig('figs/F_fig1_concept.png'); plt.savefig('figs/F_fig1_concept.pdf')
