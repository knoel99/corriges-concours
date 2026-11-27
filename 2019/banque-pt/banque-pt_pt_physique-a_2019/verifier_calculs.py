"""Recoupements numériques du corrigé Physique A 2019, avec la bibliothèque standard."""
from cmath import exp
from math import ceil, cos, isclose, log10, pi, sin, sqrt, tan

def close(x, y, tol=1e-9):
    assert isclose(x, y, rel_tol=tol, abs_tol=tol*max(1e-20, abs(y))), (x, y)

# Comparer U à un calcul par projection pour une électrode de chaque côté.
a, b, e, theta = .024, .008, -.004, .34
for angle in [0., theta, -theta]:
    ex, ey = -e*sin(angle), e*cos(angle)
    va, vb = -ex*a-ey*b, ex*a-ey*b
    close(va-vb, 2*a*e*sin(angle))
# Vérifier les trois lois de nœuds avec une tension de mode commun non nulle.
r, rp, v1e, v2e = 100000., 2000., .41, .4101
v1, v2 = v1e+r*(v1e-v2e)/rp, v2e+r*(v2e-v1e)/rp
vs = v1-v2
close((v1-v1e)/r, (v1e-v2e)/rp)
close((v2-v2e)/r, (v2e-v1e)/rp)
close(v1/2, (vs+v2)/2)
close(vs/(v2e-v1e), -101.)
print('Gain différentiel',vs/(v2e-v1e),'amplitude (mV)',abs(vs)*1000)
for f in (.002,10.,15.,50.,500.):
    x=f/15
    h=1/(1-x*x+1j*sqrt(2)*x)
    close(abs(h),(1+x**4)**-.5)
print('Gains à 15 et 50 Hz (dB)',*[-10*log10(1+(f/15)**4) for f in (15,50)])
# Écarts au milieu des fronts de 9 s et 11 s, en unités de la même image.
for cible,oeil in [(316,331),(432,448)]:
    retard=(oeil-cible)/58
    assert .2<retard<.3
    print('Retard figure 4 (s)',retard)
c=3.e8
lam,dl=820e-9,50e-9
tc=lam**2/(c*dl)
close(tc*c,13.448e-6)
print('Temps (s) et longueur (µm) de cohérence',tc,tc*c*1e6)
# Moyenne temporelle de deux champs normalisés à deux intensités distinctes.
for phase in [.1,pi/2,pi]:
    i1,i2=.85,1.8
    sample=[(sqrt(2*i1)*cos(t*2*pi/500)+sqrt(2*i2)*cos(t*2*pi/500-phase))**2 for t in range(500)]
    close(sum(sample)/len(sample),i1+i2+2*sqrt(i1*i2)*cos(phase))
for angle in [0,.16,.73]:
    close(2/cos(angle)-2*tan(angle)*sin(angle),2*cos(angle))
lam,lc,n=.800,1.80,1.
orders=[m for m in range(-10,11) if abs(m*lam)<lc]
assert orders==[-2,-1,0,1,2] and len(orders)==2*ceil(lc/lam)-1
for m in orders:
    u=m*lam/(2*n)
    close(abs(1+exp(4j*pi*n*u/lam))**2,4)
close(abs(1+exp(4j*pi*n*(lc/(2*n))/lam))**2,2.)
print('Ordres et positions brillantes (µm)',orders,[m*lam/(2*n) for m in orders])
lt=16.14*1.344/1.406*(410-245)/(1045-410)
assert 3.9<lt<4.1
print('Épaisseur lue (mm)',lt)
# Quadrature élémentaire d'un profil puis comparaison des deux pertes de charge.
R,L,eta,rho,B=.001,.4,.003,1050.,.20
dr=R/4000
debit=sum(2*pi*((i+.5)*dr)*B*(1-(((i+.5)*dr)/R)**2)*dr for i in range(4000))
close(debit,pi*B*R**2/2,1e-7)
vm=debit/(pi*R**2)
reynolds=2*rho*vm*R/eta
rh=8*eta*L/(pi*R**4)
close(rh*debit,(64/reynolds)*L/(2*R)*rho*vm**2/2)
alpha=log10(.032/.065)/log10(2);assert abs(alpha+1)<.03
print('Pente lue sur Moody',alpha,'K ramené à la pente −1',65,64)
relative=.02
limit=1/(2*log10(3.71/relative))**2
f=.04
for k in range(10):
    f=(-2*log10(relative/3.71+2.51/(1e12*sqrt(f))))**-2
close(f,limit,1e-7)
rhnet=(4e3-1.6e3)/(.0018/60)
rc=1.2e19
count=4*rc/rhnet
close(rhnet,8e7);close(count,6e11)
# Un groupe a deux tronçons en parallèle par couleur, les deux couleurs en série.
unit=1/(1/rc+1/rc)+1/(1/rc+1/rc)
groups=count/4
close(unit/groups,rhnet)
print('Résistance du réseau (Pa s/m³) et nombre total',rhnet,count)
