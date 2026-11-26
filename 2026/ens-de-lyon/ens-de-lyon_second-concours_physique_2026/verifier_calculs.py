"""Vérifications du modèle de corde. L'argument PDF facultatif donne les pentes des marqueurs réels."""
from math import exp,isclose,sqrt
import sys
g,L,mu,v=9.81,1.,.05,10.
c0=sqrt(g/L)/2
for z in [.12,.3,.6,.9]:
    Z=sqrt(z/L)
    close=lambda a,b: isclose(a,b,rel_tol=1e-11,abs_tol=1e-12)
    assert close(2*L*Z*c0,sqrt(g*z))
    # Profil polynomial de test : Y=Z³, y=(z/L)^(3/2).
    Yp,Ypp=3*Z**2,6*Z
    yp=1.5*sqrt(z)/L**1.5;ypp=.75/(sqrt(z)*L**1.5)
    assert close(g*(yp+z*ypp),c0**2*(Ypp+Yp/Z))
    assert close(g*z*ypp,c0**2*(Ypp-Yp/Z))
    c=sqrt(v*v+g*z)
    assert close((c-v)*(c+v),g*z)
print('Pseudo-célérité (s⁻¹), tensions basse et haute (N), vitesses au sommet (m/s), temps lent (s)',c0,mu*v*v,mu*(v*v+g*L),sqrt(v*v+g*L)-v,-sqrt(v*v+g*L)-v,2*v/g)
if sys.argv[1:]:
    import fitz
    with fitz.open(sys.argv[1]) as doc:draw=doc[3].get_drawings()
    # Cadre du panneau droit. L'abscisse va de 0 à 0,8 s, l'ordonnée de 0,1 à 1.
    frame=next(d['rect'] for d in draw if d['fill']==(1,1,1) and d['rect'].x0>310 and d['rect'].width>120 and d['rect'].height>130)
    groups=[[],[]]
    for d in draw:
        co=d['color'];r=d['rect']
        if not co or abs(co[0]-co[2])<.4 or not 520<r.y0<670 or r.x0<320:continue
        xc=(r.x0+r.x1)/2;yc=(r.y0+r.y1)/2
        groups[int(co[0]>.5)].append((.8*(xc-frame.x0)/frame.width,.1+.9*(frame.y1-yc)/frame.height))
    def slope(pairs):
        mx=sum(x for x,y in pairs)/len(pairs);my=sum(y for x,y in pairs)/len(pairs)
        return sum((x-mx)*(y-my) for x,y in pairs)/sum((x-mx)**2 for x,y in pairs)
    blue,red=groups
    branches=[[p for p in blue if p[0]<.195],[p for p in blue if .22<p[0]<.75],red]
    estimates=[slope(p) for p in branches]
    print('Marqueurs de la figure 2, pente Z/t par ajustement',[(len(p),round(m,5)) for p,m in zip(branches,estimates)])
    assert all(1.25<abs(m)<1.65 for m in estimates) and estimates[0]>0>estimates[1] and estimates[2]<0
