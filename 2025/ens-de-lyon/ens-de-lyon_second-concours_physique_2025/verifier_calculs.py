"""Bilan du tissu et contrôle indépendant des modes radiaux par séries de Bessel."""
from math import factorial,pi,sqrt,exp,isclose
def bess(n,x):
    term=(x/2)**n/factorial(n);val=term
    for k in range(1,110):
        term*=-(x/2)**2/(k*(k+n));val+=term
        if abs(term)<1e-16:break
    return val
D=.6/(1000*4200);R=.1;h=30.;lv=2.4e6;alpha=1.5e-4;Bi=h*R/.6
flux=lv*alpha
assert isclose(flux/h,12) and isclose(R**2/D,70000)
def residual(mu):return mu*bess(1,mu)-Bi*bess(0,mu)
roots=[]
for a,b in [(1.,2.3),(4.,5.2),(7.,8.5)]:
    assert residual(a)*residual(b)<0
    for _ in range(65):
        c=(a+b)/2
        if residual(a)*residual(c)<=0:b=c
        else:a=c
    roots.append((a+b)/2)
for mu in roots:
    # Projection d'un profil initial constant sous le produit scalaire pondéré en X.
    N=2000
    vals=[((k+.5)/N,bess(0,mu*(k+.5)/N)) for k in range(N)]
    projection=sum(x*y for x,y in vals)/sum(x*y*y for x,y in vals)
    coef=2*bess(1,mu)/(mu*(bess(0,mu)**2+bess(1,mu)**2))
    assert abs(projection-coef)<3e-6
    assert abs(residual(mu))<1e-10
    print('Racine, coefficient modal projeté',mu,projection)
timescale=R**2/D/3600
print('Fluide et surface (W/m², K), Bi, temps diffusif (h), temps du mode lent (h)',flux,flux/h,Bi,timescale,timescale/roots[0]**2)
assert 4.88<timescale/roots[0]**2<4.93
