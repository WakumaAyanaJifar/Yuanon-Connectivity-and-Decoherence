import numpy as np, mpmath as mp
from scipy import integrate
# (1) general-n Im G above threshold: Im G = S_{n-1}/(2(2pi)^n) * pi * (w^2-m^2)^{(n-2)/2}
from math import gamma, pi
def S(nm1): # surface area of unit sphere in R^{nm1+1}
    k=nm1+1; return 2*pi**(k/2)/gamma(k/2)
for n in [1,2,3]:
    for w2m2 in [0.5,2.0]:
        pred = S(n-1)/(2*(2*pi)**n)*pi*w2m2**((n-2)/2)
        # numeric: Im of int d^nq/(2pi)^n 1/(q^2 - (w2m2) - i eps): radial delta function
        # Im 1/(q^2-a-i0) = pi delta(q^2-a) -> int S q^{n-1} dq pi delta(q^2-a)/(2pi)^n = S pi a^{(n-2)/2}/(2 (2pi)^n)
        print(n,w2m2,pred)
# (2) Liu-Houck calibration
fc=7.7; D=0.25  # GHz (times 2pi)
s=2*fc*D; Cm2=(2*D/fc)**1.5
print('C/m^2 =',Cm2,' gamma_edge/2pi(GHz)=',np.sqrt(3)*D)
# exact check of locked ratio with our dispersion F(w)=w^2-m^2+g^2/(2 sqrt(m^2-w^2)), m=1, C=Cm2
m=1.0; g2=2*m*Cm2
wb=np.sqrt(1-(m*Cm2)**(2/3)); print('Delta/m exact',1-wb,' approx',(m*Cm2)**(2/3)/2, ' target', D/fc)
f=lambda w: w**2-1+g2/(2*mp.sqrt(1-w**2)) 
x=(g2/2)**(2/3); guess=mp.sqrt(1-x*mp.e**(2j*mp.pi/3))
def Gc(w):
    s_=mp.sqrt(1-w**2)
    if mp.re(w)>1 and mp.im(s_)>0: s_=-s_
    return 1/(2*s_)
r=mp.findroot(lambda w: w**2-1+g2*Gc(w), guess); print('complex pole',r,' gamma/Delta=',float(-2*mp.im(r))/(1-wb), ' sqrt3=',np.sqrt(3))
# above-edge locked relation gamma = 2 Delta^{3/2} (Om-m)^{-1/2}
for dOm in [0.05,0.1,0.2]:
    Om=1+dOm; rr=mp.findroot(lambda w: w**2-Om**2+g2*Gc(w), mp.mpc(Om,-1e-3))
    Dl=1-wb
    print(dOm,'exact gamma',float(-2*mp.im(rr)),' locked formula',2*Dl**1.5/np.sqrt(dOm),' markov',g2/(2*Om*np.sqrt(Om**2-1)))
