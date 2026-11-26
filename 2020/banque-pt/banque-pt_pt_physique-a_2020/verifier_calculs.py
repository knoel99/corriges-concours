"""Recoupements numériques du corrigé Banque PT Physique A 2020. Python 3 standard."""
from math import acos, cos, exp, isclose, pi, sin, sqrt, tan
from cmath import exp as cexp

G = 6.67e-11
c = 3e8
h = 6.62e-34
eps0 = 8.85e-12
mu0 = 4*pi*1e-7
lam = 600e-9


def verifier_gravitation():
    R, m = 11., 3.8e12
    masse_vol = m / (4*pi*R**3/3)
    for fact in [0.01,0.25,0.7,1,1.2,2,10]:
        r = fact*R
        radial = -G*m*r/R**3 if r<R else -G*m/r**2
        charge = min(r,R)**3*4*pi*masse_vol/3
        assert isclose(4*pi*r*r*radial,-4*pi*G*charge)
    assert isclose(-G*m*R/R**3,-G*m/R**2)
    alpha=(pi*G/2)**(2/3)*m**(5/3)
    valeurs=[]
    for r in [700.,900.,1400.]:
        w=sqrt(2*G*m/r**3)
        f=w/(2*pi)
        v=w*r/2
        ec=.5*m*v*v
        e=2*ec-G*m*m/r
        assert isclose(m*w*w*r/2,G*m*m/r**2)
        assert isclose(ec,G*m*m/(4*r))
        assert isclose(e,-alpha*f**(2/3))
        P=64*G**4*m**5/(5*c**5*r**5)
        df=3*P*f**(1/3)/(2*alpha)
        valeurs.append(df/f**(11/3))
    assert isclose(valeurs[0],valeurs[1]) and isclose(valeurs[0],valeurs[2])
    # Choix de K pour un test dimensionné et bien conditionné de l'intégration.
    f0,K=7.,.0003
    tau=3/(8*K*f0**(8/3))
    def freq(t):
        return f0*(1-t/tau)**(-3/8)
    for t in [0,.2*tau,.8*tau]:
        dt=tau*1e-6
        der=(freq(t+dt)-freq(t-dt))/(2*dt)
        assert isclose(der,K*freq(t)**(11/3),rel_tol=2e-8)


def verifier_michelson():
    e,fo=3e-3,.1
    i1=acos(1-lam/(4*e))
    ii=acos(1-lam/(2*e))
    assert isclose(2*e*cos(i1)/lam,9999.5)
    assert isclose(fo*tan(i1),.001,rel_tol=1e-3)
    for angle in [0,.01,.4,.75]:
        assert isclose(2*e/cos(angle)-2*e*tan(angle)*sin(angle),2*e*cos(angle))
    for angle in [0,.1,pi/2,pi,1.8*pi]:
        champ=(1-cexp(-1j*angle))/2
        assert isclose(abs(champ)**2,(1-cos(angle))/2,abs_tol=1e-14)
    T,fg,Pu,Ls,tau = 1e-4,1e3,10.,6000.,1e-21
    a=pi*fg*T
    moyenne=sin(a)/a
    pas=10000
    moyenne_directe=sum(cos(2*pi*fg*T*((i+.5)/pas-.5))
                         for i in range(pas))/pas
    assert isclose(moyenne,moyenne_directe,rel_tol=2e-8)
    p_mes=Pu/2
    perturbation=4*pi*Ls*tau/lam
    signal=Pu*perturbation/2
    finie=Pu*(sin(perturbation))/2
    assert isclose(signal,finie,rel_tol=1e-12)
    N=p_mes*T*lam/(h*c)
    bruit=sqrt(N)*h*c/(lam*T)
    assert isclose(bruit,sqrt(h*c*p_mes/(lam*T)))
    imprime=sqrt(h*c*lam/(p_mes*T))/(2*pi*Ls)
    deduit=bruit/(Pu*2*pi*Ls/lam)
    assert isclose(imprime,2*deduit)
    gain=(1+.995)/(1-.995)
    assert isclose(gain,399)
    assert signal<bruit<gain*signal
    assert deduit/gain<tau<imprime/gain
    print("Rayons des anneaux sur la sortie sombre puis sur la sortie complémentaire, en mm",
          fo*tan(i1)*1000,fo*tan(ii)*1000)
    print("Intégration centrée 0,1 période, rapport d’amplitude",moyenne)
    print("Photons par fenêtre",N,"signal crête simple et bruit en W",signal,bruit)
    print("Seuils imprimé/déduit puis avec cavités",imprime,deduit,
          imprime/gain,deduit/gain,"rapport signal/bruit avec cavités",gain*signal/bruit)
    for n in [1,2,3,9]:
        L=.22
        f=n*c/(2*L)
        k=2*pi*f/c
        assert abs(sin(k*L))<2e-14
        assert isclose(c/f,2*L/n)


def verifier_miroir():
    P,r,ga=40.,.05,1e7
    S=pi*r*r
    f=c/lam
    w=2*pi*f
    E=sqrt(2*mu0*c*P/S)
    assert isclose(E*E*S/(2*mu0*c),P)
    assert 350<ga/(eps0*w)<370
    delta=sqrt(2/(mu0*ga*w))
    k=(1-1j)/delta
    assert abs(k*k+1j*mu0*ga*w)<2e-15*mu0*ga*w
    assert isclose(abs(cexp(-1j*k*delta)),exp(-1))
    surf=.5*ga*(1e-4*E)**2
    pJ=surf*S*delta/2
    # Quadrature au point milieu sur les vingt premières profondeurs de peau.
    n=50000
    integral=sum(surf*exp(-2*(i+.5)*20/n) for i in range(n))*20*delta/n*S
    assert isclose(integral,pJ,rel_tol=1e-7)
    rho,cap,kappa,L,coef=8e3,400.,400.,1e-3,1e-5
    taux=pJ/(rho*cap*S*delta)
    moyenne=pJ/(rho*cap*S*L)
    tmax=1e-15*lam/(coef*delta*taux)
    diffusivite=kappa/(rho*cap)
    assert isclose(coef*delta*taux*tmax,6e-22)
    assert isclose(coef*pJ*tmax/(rho*cap*S),6e-22)
    assert isclose(L*L/diffusivite,8e-3)
    print("Puissance, E0, fréquence, épaisseur de peau, vitesse de phase (SI)",
          P,E,f,delta,w*delta)
    print("Joule en surface W/m³, Joule total W",surf,pJ)
    print("Échauffement sur peau et épaisseur entière K/s",taux,moyenne)
    print("Durées limite locale, diffusion sur L et sur delta (s)",
          tmax,L*L/diffusivite,delta**2/diffusivite)


if __name__=="__main__":
    verifier_gravitation()
    verifier_michelson()
    verifier_miroir()
    print("Les égalités et les ordres de grandeur testés sont vérifiés.")
