"""Recalcul de la solidification. Un PDF officiel passé en argument permet de relire la figure 4 (PyMuPDF)."""
from math import erf, exp, pi, sqrt
import sys

def zero(f,a,b):
    assert f(a)*f(b)<0
    for _ in range(70):
        mid=(a+b)/2
        if f(a)*f(mid)<=0:b=mid
        else:a=mid
    return (a+b)/2

rho,latent,cp,ls,ll,es,el=920.,334000.,2100.,2.2,.6,9.3e9,2e9
k,al,be=rho/1000.,es/el,ls/ll
A=2*ls*10/(rho*latent)
ds=ls/(rho*cp)
ste=cp*10/latent
eta=zero(lambda x:x*exp(x*x)*erf(x)-ste/sqrt(pi),1e-8,1)
ratio=sqrt(2)*eta/sqrt(ste)
assert 80 < 1/(A*86400)<82 and .989<ratio<.992
print('Front libre en jours, temps diffusif sur temps du front, rapport de Stefan',1/(A*86400),A/ds,ratio)
def mech(u):return (1-k)*u/(al+(k-al)*u)
def q(u):return (1-u)/((1-u)+u/be)
assert abs(mech(1)-(1-k)/k)<1e-14
ac=latent/(273.15*(1/rho-.001))
for slope in [1e7,ac]:
    u=zero(lambda u:slope*10*q(u)/es-mech(u),0,1)
    press=es*mech(u);temp=-10*q(u)
    assert abs(ls*(temp+10)/u-ll*(-temp)/(1-u))<1e-10
    sp=u*(1+mech(u));lp=sp+(1-u)*(1+al*mech(u))
    assert abs(lp-1-(1-k)*sp)<1e-11
    print('Pente (MPa/K), u, surpression (MPa), température (°C), flux (W/m²)',slope/1e6,u,press/1e6,temp,ls*(temp+10)/u)
print('Force maximale (N) et déformation maximale',es*mech(1)*1e-3,mech(1))
if sys.argv[1:]:
    import fitz
    with fitz.open(sys.argv[1]) as doc:
        draws=doc[7].get_drawings()
    curves=[next(p for p in draws if p['color']==c)['items'] for c in [(0.,0.,1.),(1.,0.,0.)]]
    blue,red=curves
    j=next(j for j,(a,b) in enumerate(zip(blue,red)) if a[-1].y>=b[-1].y)
    p1,p2=blue[j][1:];q1,q2=red[j][1:]
    f=(q1.y-p1.y)/((p2.y-p1.y)-(q2.y-q1.y))
    x=p1.x+f*(p2.x-p1.x);y=p1.y+f*(p2.y-p1.y)
    grid=[p['rect'] for p in draws if p['color'] and .80<p['color'][2]<.85 and p['rect'].width>200 and p['rect'].height<.01]
    bottom=max(grid,key=lambda r:r.y0)
    top=sorted((r.y0 for r in grid),reverse=True)[1]
    u=(x-bottom.x0)/bottom.width;Y=(bottom.y0-y)*.01/(bottom.y0-top)
    assert .372<u<.379 and .0091<Y<.0094
    print('Intersection des deux polylignes du PDF : u et ΔP/Es',u,Y)
