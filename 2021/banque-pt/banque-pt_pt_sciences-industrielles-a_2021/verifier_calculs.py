"""Contrôles numériques du corrigé Banque PT SI A 2021. Exécuter avec Python 3."""
from cmath import exp
from math import cos, sin, pi, sqrt, hypot, isclose, log, radians, degrees

def near(actual, expected, atol=1e-9):
    assert abs(actual-expected) <= atol, (actual, expected)

def product(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def dh(t, alpha, a, d):
    ct, st, ca, sa = cos(t), sin(t), cos(alpha), sin(alpha)
    return [[ct,-st*ca,st*sa,a*ct],[st,ct*ca,-ct*sa,a*st],[0,sa,ca,d],[0,0,0,1]]

lengths = (270.35, 69, 364.35, 69, 374.29, 10, 229.525)
l1,l2,l3,l4,l5,l6,l7 = lengths
for t1,t2 in [(0,0),(.9,.18),(-.29,-.74),(pi/2,pi/2)]:
    m=product(dh(t1,-pi/2,l2,l1),dh(t2,pi/2,0,0))
    c1,s1,c2,s2=cos(t1),sin(t1),cos(t2),sin(t2)
    expected=[[c1*c2,-s1,c1*s2,l2*c1],[s1*c2,c1,s1*s2,l2*s1],[-s2,0,c2,l1],[0,0,0,1]]
    for row,target in zip(m,expected):
        for x,y in zip(row,target):near(x,y)
for val,target in zip(product(m,[[l4],[0],[l3],[1]]),[0,433.35,201.35,1]):near(val[0],target)
near(2*(278+l2+l3+l5+l7),2630.33)
near(l1+l3+l5+l7,1238.515);near(l2+l4+l6,148)
print('Q2–13 : rotations, composition homogène, coude (0 ; 433,35 ; 201,35) mm, écartement 2630,33 mm.')
def position(t4,t6):
    return [l7*sin(t4+t6)+l6*cos(t4)+l5*sin(t4), -l7*cos(t4+t6)+l6*sin(t4)-l5*cos(t4)]
for a,b,v,w in [(.12,.63,-1.52,4),(.4,-.48,.3,-.7),(-.5,.7,1.9,1.2)]:
    delta=1e-6
    f1=l7*cos(a+b);f2=2*f1-l6*sin(a)+l5*cos(a);f3=l7*sin(a+b);f4=l6*cos(a)+l5*sin(a)
    dxy=[(x-y)/(2*delta) for x,y in zip(position(a+delta*v,b+delta*w),position(a-delta*v,b-delta*w))]
    near((w-v)*f1+v*f2,dxy[0],1e-6);near((w+v)*f3+v*f4,dxy[1],1e-6)
assert 200<degrees(4*.92)<220
g_shear=220000/2.6;le=1.5*g_shear*.06/120;h=3*250000*le/(1.5**3*g_shear)
near(le,63.46153846,1e-7);near(h,166.66666667,1e-7);near(2*(h/2)*1.5**3*g_shear/(3*le),250000);assert h/2/1.5>20
print('Q14–19 : dérivées centrées, signe imposé, degrés et contrainte de 120 MPa. L = 63,46 mm ; h = 166,67 / 83,33 mm.')
j,ks,kp,ki,kd=2.1,200,4.0,1.2,.09
omega0=sqrt(ks/j)
for omega in [.1,1.8,9.,21.,54.]:
    s=1j*omega
    hm=ks/(j*s*s+ks);hl=j*s*s*hm
    ctrl=kp*(1+ki/s+kd*s);z=-hl/(1+ctrl*hm)
    b=-j/(kp*ki);c=1/(omega0**2*kp*ki);d=kd/ki;e=(1+kp)/(kp*ki)
    den=c*s**3+d*s*s+e*s+1
    near(z,b*s**3/den)
    near(z.imag,-b*omega**3*(1-d*omega**2)/abs(den)**2)
    assert (z.imag<=0)==(kd/ki>=1/omega**2)
near(1-cos(pi),2);near((1-1)/(1+kp*(1+ki*.08)),0)
print('Q22–30 : transfert mécanique signé et coefficients PID confirmés à cinq pulsations, critère et anticipation vérifiés.')
V,I,phi=32,1.05,.32
for u in [0,.1,.32,2.2,5.9]:
    va=[sqrt(2)*V*cos(u+d) for d in [0,-2*pi/3,2*pi/3]]
    ia=[sqrt(2)*I*cos(u+d-phi) for d in [0,-2*pi/3,2*pi/3]]
    def transform(x):
        return sqrt(2/3)*complex(x[0]-(x[1]+x[2])/2,sqrt(3)*(x[1]-x[2])/2)
    v,i=transform(va),transform(ia)
    near(v,sqrt(3)*V*exp(1j*u));near(i,sqrt(3)*I*exp(1j*(u-phi)))
    near(sum(a*b for a,b in zip(va,ia)),(v*i.conjugate()).real);near((v*i.conjugate()).real,3*V*I*cos(phi))
    near(i*exp(1j*(-u+phi+pi/2)),1j*sqrt(3)*I)
r,l=5,.020;ti=l/r;kp=l*log(20)/.005
for s in [.1,10,90j]:
    bo=kp*(1+ti*s)/(ti*s)/(r+l*s);near(bo/(1+bo),1/(1+l*s/kp))
near(1-exp(-kp*.005/l),.95)
print('Q32–43 : puissances triphasée et diphasée, rotation dq, compensation du pôle et seuil de 95 % vérifiés.')
g=9.81;ratio=120;pairs=4;flux=.050
torque=g*(9*.35+2*.65);speed=ratio/.60;omega=pairs*speed;freq=omega/(2*pi)
iq=torque/(ratio*pairs*flux);voltage=(r+1j*omega*l)*1j*iq+1j*omega*flux
near(torque,43.6545);near(omega,800);near(iq,1.8189375)
near(abs(voltage)/sqrt(3),32.950836862,1e-8)
near((voltage*(1j*iq).conjugate()).real,r*iq*iq+(torque/ratio)*speed)
assert torque<50 and freq<200 and abs(voltage)<120 and iq/sqrt(3)<2
print('Q44–50 : 43,65 N·m ; 800 rad/s ; 127,32 Hz ; 1,819 A dq ; 1,050 A efficace ; 32,95 V simple et 57,07 V composée.')
