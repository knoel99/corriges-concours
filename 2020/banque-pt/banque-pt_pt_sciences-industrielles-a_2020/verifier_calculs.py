"""Contre-calcul des réponses numériques et du moment en B, par différences finies."""
from math import cos, sin, sqrt, pi, log, hypot, isclose
def proche(calcul, attendu, tol):
    assert abs(calcul-attendu)<tol,(calcul,attendu)
def main():
    E,S,L,I=2e5,4500,720,15e6
    vz=[z*L/(E*S) for z in [50500,-70500]]
    vx=6500*L**3/(3*E*I)
    proche(vz[0],.0404,.00001);proche(vz[1],-.0564,.00001);proche(vx,.27,.001)
    print("Socle en mm",vz,vx)
    # Trois masses ponctuelles réalisent un corps étendu. L'accélération d'un point
    # est obtenue directement par différences sur sa position cartésienne absolue.
    L2=1.2;positions=[(.3,.08,3),(.9,.16,4),(.8,-.07,2)];m=sum(row[2] for row in positions)
    a=sum(a*mi for a,b,mi in positions)/m;b=sum(b*mi for a,b,mi in positions)/m
    B4=sum(mi*(a*a+b*b) for a,b,mi in positions)
    def q(t):return .2+.7*t+.5*.4*t*t,1.1-.3*t+.5*.6*t*t
    def point(t,a,b):
        u,v=q(t);return (L2*sin(u)+a*sin(u+v)-b*cos(u+v),L2*cos(u)+a*cos(u+v)+b*sin(u+v))
    dx=1e-4;delta=0.;bx,bz=point(0,0,0)
    for aa,bb,mi in positions:
        x,z=point(0,aa,bb);p=point(dx,aa,bb);n=point(-dx,aa,bb)
        ax=(p[0]-2*x+n[0])/dx**2;az=(p[1]-2*z+n[1])/dx**2
        delta+=mi*((z-bz)*ax-(x-bx)*az)
    D=a*cos(1.1)+b*sin(1.1);H=a*sin(1.1)-b*cos(1.1)
    exact=B4*(.4+.6)+m*L2*(D*.4+H*.7**2)
    proche(delta,exact,2e-6);print("Moment dynamique échantillon",delta,exact)
    omega=sqrt(10);ki=(1+log(20)/(.01*omega))/(omega*.04);kp=log(20)/12.1
    proche(ki,757,.5);proche(kp,.248,.001);print("Seuils vitesse et position",ki,kp)
    jeq=.48+.037+(2*.5+2+1.8+2*(30+12*1.5)*2.5**2)/16**2
    proche(jeq,2.88,.01);print("Inertie kg cm²",jeq)
    apeak=5.2/.0003*.025/16;proche(apeak,27.08,.01)
    vpeak=2*pi*4500/60*.025/16;assert vpeak>.50 and apeak>1
    print("Vitesse et accélération de pointe",vpeak,apeak)
    vmax=sqrt(6)*230;umin=vmax*cos(pi/6);proche(vmax-umin,75.5,.2)
    pairs=[(2,1),(0,1),(0,2),(1,2),(1,0),(2,0)]
    for j,(top,bot) in enumerate(pairs):
        volts=[sqrt(2)*230*sin(j*pi/3-i*2*pi/3) for i in range(3)]
        assert volts.index(max(volts))==top and volts.index(min(volts))==bot
    print("Pont (V)",umin,vmax,vmax-umin)
    e=62*80*60/(2*pi*1000);iu=3.5
    print("Tensions efficaces",hypot(e+11.6*iu,.037*160*iu),hypot(e/sqrt(3)+11.6*iu,.037*160*iu))
if __name__=='__main__':main()
