import matplotlib as mpl
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':10.5,'axes.labelsize':11.5,'axes.titlesize':11,'xtick.labelsize':10,'ytick.labelsize':10,
 'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':0.8,'xtick.major.width':0.8,'ytick.major.width':0.8,
 'legend.frameon':False,'legend.fontsize':9,'figure.dpi':150,'savefig.dpi':300,'savefig.bbox':'tight','mathtext.fontset':'dejavusans'})
NAVY='#1f3b73'; TEAL='#16a085'; ORANGE='#e67e22'; CRIMSON='#c0392b'; PURPLE='#6c5ce7'; GRAY='#7f8c8d'; GOLD='#d4a017'
def tag(ax, s, x=-0.14, y=1.04): ax.text(x,y,s,transform=ax.transAxes,fontsize=12,fontweight='bold',va='bottom')
