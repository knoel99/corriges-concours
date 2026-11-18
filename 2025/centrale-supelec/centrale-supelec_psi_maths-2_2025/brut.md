# Centrale-Supélec PSI — Mathématiques 2 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie A — Deux approches pour une valeur à $1+2+\cdots+n+\cdots$

**I — Une première approche**

### Question 1

La série est géométrique de raison $e^{-x}$. Elle converge exactement lorsque $|e^{-x}|<1$, soit $x>0$. Ainsi, **$D_f=]0,+\infty[$ et $f(x)=(1-e^{-x})^{-1}$** sur $D_f$.

### Question 2

Sur $D_f$, $1-e^{-x}$ est de classe $\mathcal C^1$ et ne s'annule pas. Son inverse est donc de classe $\mathcal C^1$ et la dérivée de $1-e^{-x}$ est $e^{-x}$. On obtient

$$
\boxed{f'(x)=-\frac{e^{-x}}{(1-e^{-x})^2}.}
$$

### Question 3

En multipliant le numérateur et le dénominateur de la fraction par $e^x$, on obtient l'inverse de $e^x+e^{-x}-2$. Les développements des exponentielles à l'ordre quatre donnent

$$
e^x+e^{-x}-2=x^2+\frac{x^4}{12}+o(x^4).
$$

On factorise $x^2$, puis on utilise $(1+u)^{-1}=1-u+o(u)$ avec $u=x^2/12+o(x^2)$. Ainsi,

$$
\begin{aligned}
\frac{e^{-x}}{(1-e^{-x})^2}
&=\frac{1}{x^2}\left(1-\frac{x^2}{12}+o(x^2)\right)\\
&=\frac{1}{x^2}-\frac1{12}+o(1).
\end{aligned}
$$

Les coefficients sont uniques, par identification successive après multiplication par $x^2$, puis par $x$ après retrait du terme en $x^{-2}$. **$a=1$, $b=0$ et $c=-1/12$.**

### Question 4

Les fonctions $x\mapsto e^{-nx}$ sont de classe $\mathcal C^1$ et leur série converge simplement sur $D_f$ d'après Q1.

Sur tout segment $[a,b]\subset D_f$, les dérivées sont majorées en valeur absolue par $ne^{-na}$.

La série de ces majorants converge par la règle de d'Alembert, car le rapport des termes successifs tend vers $e^{-a}<1$.

La série des dérivées converge donc normalement, puis uniformément, sur tout segment de $D_f$.

Le théorème de dérivation des séries de fonctions donne $\sum_{n\ge0}ne^{-nx}=-f'(x)$.

Par Q2 et Q3,

$$
\boxed{\lim_{x\to0^+}\left(\sum_{n=0}^{+\infty}ne^{-nx}-\frac1{x^2}\right)=-\frac1{12}.}
$$

**II — Une deuxième approche**

**II.1 — Une généralisation du théorème des sommes de Riemann pour les fonctions de classe $\mathcal C^1$**

### Question 5

Comme $x>0$, $a<a+nx\le b$ équivaut à $0<n\le (b-a)/x$.

Pour $n$ entier, cette dernière condition équivaut à $1\le n\le \lfloor(b-a)/x\rfloor$.

**L'ensemble est celui des entiers de $1$ à $\lfloor(b-a)/x\rfloor$**, vide si cette partie entière est nulle.

### Question 6

La définition de la partie entière donne $L/x-1<\lfloor L/x\rfloor\le L/x$. Comme $x>0$, on en déduit

$$
\boxed{0\le L-\lfloor L/x\rfloor x<x.}
$$

### Question 7

Posons $N=\lfloor(b-a)/x\rfloor$.

La relation de Chasles décompose $\int_a^b f$ en les intégrales sur les $N$ intervalles $[a+(n-1)x,a+nx]$, puis sur $[a+Nx,b]$.

Sur le $n$-ième intervalle, $xf(a+nx)$ est l'intégrale de la constante $f(a+nx)$.

Par linéarité,

$$
\begin{aligned}
x\sum_{n=1}^N f(a+nx)-\int_a^b f(t)\,dt
&=\sum_{n=1}^N\int_{a+(n-1)x}^{a+nx}\bigl(f(a+nx)-f(t)\bigr)\,dt\\
&\quad-\int_{a+Nx}^b f(t)\,dt .
\end{aligned}
$$

### Question 8

Les fonctions $f$ et $f'$ sont continues sur le segment, donc bornées. Notons $M=\|f'\|_\infty$ et $F=\|f\|_\infty$. Sur chaque intervalle de Q7, l'inégalité des accroissements finis donne $|f(a+nx)-f(t)|\le Mx$. La valeur absolue de l'intégrale terminale est au plus $F(b-a-Nx)\le Fx$ d'après Q6. Ainsi,

$$
\begin{aligned}
\left|x\sum_{n=1}^N f(a+nx)-\int_a^b f(t)\,dt\right|
&\le NMx^2+Fx\\
&\le \bigl(M(b-a)+F\bigr)x .
\end{aligned}
$$

**La somme pondérée converge vers $\int_a^b f(t)\,dt$ quand $x\to0^+$.**

**II.2 — Un développement asymptotique lorsque $x$ tend vers $0$ de $\sum_{n=1}^{+\infty}n\varphi(nx)$**

Dans cette sous-partie, $N=\lfloor K/x\rfloor$, $I_n=[(n-1)x,nx]$ et toutes les limites en $x=0$ sont prises à droite.

### Question 9

On a $\psi(0)=0$ et $\psi'(0)=\varphi(0)=1$ par la formule de dérivation du produit. Comme $\psi(K)=\psi'(K)=0$, le calcul par primitive donne

$$
\begin{aligned}
\int_0^K\psi'(t)\,dt&=0\\
\int_0^K\psi''(t)\,dt&=-1.
\end{aligned}
$$

### Question 10

Les fonctions $\psi$, $\psi'$ et $\psi''$ sont de classe $\mathcal C^1$ sur $[0,K]$. On applique Q8 à chacune d'elles, puis Q9 aux deux dernières intégrales. Comme $\psi(nx)=nx\varphi(nx)$,

$$
\begin{aligned}
x\sum_{n=1}^N nx\varphi(nx)&\longrightarrow\int_0^K\psi(t)\,dt,\\
x\sum_{n=1}^N\psi'(nx)&\longrightarrow0,\\
x\sum_{n=1}^N\psi''(nx)&\longrightarrow-1.
\end{aligned}
$$

### Question 11

On applique la formule de Taylor avec reste intégral à $\psi^{(l)}$, qui est de classe $\mathcal C^{k+1}$, entre $K$ et $t$ à l'ordre $k$.

Ses dérivées d'ordre $0$ à $k$ s'annulent toutes en $K$.

L'intégrale orientée restante donne, pour tout $t\ge0$,

$$
\boxed{\psi^{(l)}(t)=\int_K^t \frac{(t-s)^k}{k!}\psi^{(k+l+1)}(s)\,ds.}
$$

### Question 12

Fixons $k,l\in\mathbb N$ et posons $M=\max_{[0,K]}|\psi^{(k+l+1)}|$. Pour $Nx\le t\le K$, Q11 donne

$$
|\psi^{(l)}(t)|\le \frac{M}{(k+1)!}(K-t)^{k+1}.
$$

D'après Q6, $K-Nx\le x$. En intégrant la majoration, on obtient

$$
\left|\frac{1}{x^k}\int_{Nx}^K \psi^{(l)}(t)\,dt\right|
\le \frac{M}{(k+2)!}x^2 .
$$

**La limite demandée vaut $0$.**

### Question 13

Posons $M=\max_{[0,K]}|\psi^{(k+l)}|$. Sur $I_n$, la valeur absolue de l'intégrale intérieure définissant $R_{k,l}$ est majorée par $M(nx-t)^{k+1}/(k+1)!$. En intégrant sur $I_n$ puis en utilisant $Nx\le K$, on obtient

$$
\begin{aligned}
\left|\frac{R_{k,l}(x)}{x^k}\right|
&\le \frac{NMx^{k+2}}{(k+2)!\,x^k}\\
&\le \frac{KM}{(k+2)!}x.
\end{aligned}
$$

**La limite demandée vaut $0$.**

### Question 14

Pour $t\in I_n$, la fonction $\psi^{(l)}$ est de classe $\mathcal C^{p+1}$. Taylor à l'ordre $p$ au point $nx$ donne, après retrait du terme d'ordre zéro,

$$
\begin{aligned}
\psi^{(l)}(t)-\psi^{(l)}(nx)
&=\sum_{k=1}^p \frac{(t-nx)^k}{k!}\psi^{(k+l)}(nx)\\
&\quad+\int_{nx}^t\frac{(t-s)^p}{p!}\psi^{(p+l+1)}(s)\,ds.
\end{aligned}
$$

On intègre sur $I_n$ et on somme. **On obtient l'identité de Q14**, puisque la somme des intégrales des restes est par définition $R_{p,l+1}(x)$.

### Question 15

Dans Q14, on prend $l=0$ et $p=2$.

En posant $u=t-nx$, on intègre $u$ et $u^2/2$ sur $[-x,0]$.

On trouve respectivement $-x^2/2$ et $x^3/6$.

Après division par $x^2$,

$$
\begin{aligned}
\frac1{x^2}\sum_{n=1}^N \int_{I_n}(\psi(t)-\psi(nx))\,dt
&=-\frac12\sum_{n=1}^N\psi'(nx)+\frac{x}{6}\sum_{n=1}^N\psi''(nx)\\
&\quad+\frac{R_{2,1}(x)}{x^2}.
\end{aligned}
$$

### Question 16

On applique Q7 avec $a=0$, $b=K$ et $f=\psi'$ de classe $\mathcal C^1$. En utilisant $\int_0^K\psi'=0$ par Q9, on obtient

$$
\begin{aligned}
x\sum_{n=1}^N\psi'(nx)&=\sum_{n=1}^N\int_{I_n}(\psi'(nx)-\psi'(t))\,dt\\
&\quad-\int_{Nx}^K\psi'(t)\,dt.
\end{aligned}
$$

### Question 17

On prend $l=1$ et $p=1$ dans Q14. L'intégrale de $t-nx$ sur $I_n$ vaut $-x^2/2$. La somme d'intégrales figurant en Q16 est l'opposée de celle de Q14. En la substituant puis en divisant par $x$, on obtient

$$
\begin{aligned}
\sum_{n=1}^N\psi'(nx)&=\frac{x}{2}\sum_{n=1}^N\psi''(nx)-\frac{R_{1,2}(x)}x\\
&\quad-\frac1x\int_{Nx}^K\psi'(t)\,dt.
\end{aligned}
$$

### Question 18

Dans Q17, le premier terme à droite tend vers $-1/2$ d'après Q10.

Le deuxième tend vers zéro d'après Q13 avec $k=1$ et $l=2$, et le dernier d'après Q12 avec $k=l=1$.

Par conséquent $\sum_{n=1}^N\psi'(nx)\longrightarrow-1/2$.

Dans Q15, on applique alors cette limite au premier terme, Q10 au deuxième et Q13 avec $k=2$ et $l=1$ au dernier.

Cela donne

$$
\begin{aligned}
\lim_{x\to0^+}\frac1{x^2}\sum_{n=1}^N\int_{I_n}(\psi(t)-\psi(nx))\,dt
&=\frac14-\frac16\\
&=\boxed{\frac1{12}}.
\end{aligned}
$$

### Question 19

On applique Q7 à $\psi$ sur $[0,K]$. On isole $x\sum_{n=1}^N\psi(nx)$, puis on divise par $x^2$ et on utilise $\psi(nx)=nx\varphi(nx)$, ce qui donne

$$
\begin{aligned}
\sum_{n=1}^N n\varphi(nx)
&=\frac1{x^2}\int_0^K\psi(t)\,dt\\
&\quad-\frac1{x^2}\sum_{n=1}^N\int_{I_n}(\psi(t)-\psi(nx))\,dt
-\frac1{x^2}\int_{Nx}^K\psi(t)\,dt.
\end{aligned}
$$

### Question 20

Pour $n>N$, on a $nx>K$, donc $\varphi(nx)=0$.

La série est ainsi égale à la somme finie de Q19.

Par Q18 et Q12 (avec $k=2,l=0$), les deux termes soustraits tendent respectivement vers $1/12$ et $0$.

En posant $A=\int_0^K t\varphi(t)\,dt$, on obtient

$$
\boxed{\sum_{n=1}^{+\infty}n\varphi(nx)=\frac{A}{x^2}-\frac1{12}+o(1).}
$$

## Partie B — Les sommes infinies au sens de Ramanujan

**I — La formule d’Euler-Maclaurin**

### Question 21

On intègre $B_1'=1$, puis on fixe la constante par $\int_0^1 B_1=0$. Il vient $B_1(X)=X-1/2$. On intègre ensuite $B_2'=2X-1$, d'où $B_2(X)=X^2-X+c$. La condition d'intégrale nulle donne $c=1/2-1/3=1/6$. Ainsi,

$$
\begin{aligned}
B_1(X)&=X-\frac12\\
B_2(X)&=X^2-X+\frac16.
\end{aligned}
$$

### Question 22

Pour $p=0$, $B_0=1$ vérifie la relation.

Supposons-la vraie au rang $p$ et posons $D(X)=B_{p+1}(1-X)-(-1)^{p+1}B_{p+1}(X)$.

En dérivant et en utilisant l'hypothèse de récurrence, on obtient $D'=0$.

Le changement de variable $u=1-t$ montre que $\int_0^1 D(t)\,dt=0$, car $B_{p+1}$ est d'intégrale nulle.

La constante $D$ est donc nulle.

**Pour tout $p\in\mathbb N$, $B_p(1-X)=(-1)^p B_p(X)$.**

### Question 23

Si $p\ge2$, alors $p-1\ge1$ et

$$
B_p(1)-B_p(0)=p\int_0^1 B_{p-1}(t)\,dt=0.
$$

Pour $p\ge3$ impair, Q22 donne $B_p(1)=-B_p(0)$. **On a donc $B_p(1)=b_p$ pour $p\ge2$ et $b_p=0$ pour $p\ge3$ impair.**

### Question 24

Sur $[k,k+1[$, on a $\widetilde B_j(t)=B_j(t-k)$.

On peut remplacer $\widetilde B_j$ par ce polynôme dans les intégrales sur $[k,k+1]$, car la valeur au point $k+1$ n'affecte pas l'intégrale.

Le polynôme $B_{p+1}(t-k)/(p+1)!$ est une primitive de $B_p(t-k)/p!$ sur ce segment.

Par intégration par parties,

$$
\begin{aligned}
\int_k^{k+1}\frac{\widetilde B_p(t)}{p!} f^{(p)}(t)\,dt
&=\frac{B_{p+1}(1)f^{(p)}(k+1)-B_{p+1}(0)f^{(p)}(k)}{(p+1)!}\\
&\quad-\int_k^{k+1}\frac{\widetilde B_{p+1}(t)}{(p+1)!} f^{(p+1)}(t)\,dt .
\end{aligned}
$$

### Question 25

On prend $p=0$ dans Q24 et on somme pour $k=1,\dots,n-1$. D'après Q21, le terme de bord sur $[k,k+1]$ vaut $(f(k+1)+f(k))/2$. Par Chasles,

$$
\int_1^n f(t)\,dt=\sum_{k=1}^{n-1}\frac{f(k+1)+f(k)}{2}-r_{1,n}.
$$

La demi-somme vaut $\sum_{k=1}^n f(k)-(f(1)+f(n))/2$, y compris pour $n=1$. **On en déduit la formule de Q25.**

### Question 26

Pour tout $j\ge2$, on applique Q24 avec l'indice $p=j-1$, puis on somme de $k=1$ à $n-1$. Les valeurs aux deux extrémités de $B_j$ coïncident par Q23. Les termes de bord se télescopent et donnent

$$
r_{j-1,n}=\frac{b_j}{j!}\bigl(f^{(j-1)}(n)-f^{(j-1)}(1)\bigr)-r_{j,n}.
$$

Pour $l\ge1$, on applique cette identité aux indices $2l$ et $2l+1$. Comme $b_{2l+1}=0$, on obtient

$$
r_{2l-1,n}=\frac{b_{2l}}{(2l)!}\bigl(f^{(2l-1)}(n)-f^{(2l-1)}(1)\bigr)+r_{2l+1,n}.
$$

En sommant de $l=1$ à $p$ et en reportant le résultat dans Q25,

$$
\begin{aligned}
\sum_{k=1}^n f(k)
&=\int_1^n f(t)\,dt+\frac{f(1)+f(n)}2\\
&\quad+\sum_{l=1}^p\frac{b_{2l}}{(2l)!}\bigl(f^{(2l-1)}(n)-f^{(2l-1)}(1)\bigr)+r_{2p+1,n}.
\end{aligned}
$$

**II — La constante de Ramanujan**

### Question 27

Pour $p\ge q$, $\widetilde B_{2p+1}$ est bornée par périodicité et continuité de $B_{2p+1}$ sur $[0,1]$.

Son produit par $f^{(2p+1)}$ est continu par morceaux et absolument intégrable sur $[1,+\infty[$.

Ainsi, $r_{2p+1,n}$ a une limite finie $r_{2p+1,\infty}$ et **$C_p$ est bien définie**, y compris pour $p=0$ si $q=0$.

Par la relation obtenue en Q26 au rang $l=p+1$,

$$
r_{2p+1,n}-r_{2p+3,n}
=\frac{b_{2p+2}}{(2p+2)!}\bigl(f^{(2p+1)}(n)-f^{(2p+1)}(1)\bigr).
$$

On fait tendre $n$ vers l'infini. L'hypothèse $f^{(2p+1)}(n)\to0$ donne

$$
r_{2p+1,\infty}-r_{2p+3,\infty}
=-\frac{b_{2p+2}}{(2p+2)!}f^{(2p+1)}(1).
$$

En reportant dans la différence des définitions de $C_p$ et $C_{p+1}$, les deux termes se compensent. Cette comparaison pour tout $p\ge q$ établit **l'indépendance de $C_p$**.

### Question 28

Pour $f(t)=1$, $t$ ou $t^2$, toutes les dérivées d'ordre $2p+1$ sont nulles pour $p\ge1$.

On peut donc prendre $q=1$ et calculer $C_1$, dont le reste intégral est nul.

Par Q21, $b_2/2!=1/12$.

La formule à appliquer est

$$
C_1=\frac{f(1)}2-\int_0^1 f(t)\,dt-\frac{f'(1)}{12}.
$$

Pour $1$, les trois contributions valent $1/2$, $-1$ et $0$.

Pour $t$, elles valent $1/2$, $-1/2$ et $-1/12$.

Pour $t^2$, elles valent $1/2$, $-1/3$ et $-1/6$.

On trouve

$$
\begin{aligned}
\sum_{k\ge1}^{R}1&=-\frac12\\
\sum_{k\ge1}^{R}k&=-\frac1{12}\\
\sum_{k\ge1}^{R}k^2&=0.
\end{aligned}
$$

### Question 29

Puisque $q=0$, la somme de Ramanujan vaut $C_0$. D'après Q25 et la relation de Chasles,

$$
\sum_{k=1}^n f(k)-\int_0^n f(t)\,dt
=\frac{f(1)+f(n)}2-\int_0^1 f(t)\,dt+r_{1,n}.
$$

Par hypothèse $f(n)\to0$ et, d'après Q27 au rang $0$, $r_{1,n}\to r_{1,\infty}$. Le membre de droite tend donc vers $C_0$, ce qui prouve l'égalité demandée. Si l'intégrale sur $[0,+\infty[$ converge, la suite des sommes partielles converge elle aussi. En passant à la limite,

$$
\boxed{\sum_{k\ge1}^{R}f(k)=\sum_{k=1}^{+\infty}f(k)-\int_0^{+\infty}f(t)\,dt .}
$$

## Partie C — Développements tayloriens généralisés

**I — Les formules de Taylor généralisés**

### Question 30

On part de $P_0=1$.

Si $P_n$ est connu, alors $G_n(X)=(n+1)\int_0^X P_n(s)\,ds$ est un polynôme obtenu en intégrant les monômes de $P_n$.

Tout polynôme de dérivée $(n+1)P_n$ s'écrit $G_n+c$.

Comme $\varphi(1)=1$, $\varphi(G_n+c)=\varphi(G_n)+c$.

L'unique choix qui annule cette valeur est

$$
\boxed{P_{n+1}=G_n-\varphi(G_n).}
$$

On obtient par récurrence l'existence et l'unicité de la suite entière.

### Question 31

Par continuité de $\varphi$, on choisit $C\ge0$ tel que $|\varphi(g)|\le C\|g\|_\infty$ pour tout $g\in E$.

Pour $x\in[0,1]$, l'intégrale dans $G_n(x)$ est de longueur au plus $1$, donc $\|G_n\|_\infty\le(n+1)\|P_n\|_\infty$.

Par Q30,

$$
\begin{aligned}
\|P_{n+1}\|_\infty
&\le \|G_n\|_\infty+|\varphi(G_n)|\\
&\le \boxed{(n+1)(1+C)\|P_n\|_\infty}.
\end{aligned}
$$

### Question 32

Comme $\|P_0\|_\infty=1$, Q31 donne par récurrence $\|P_k\|_\infty\le k!(1+C)^k$. Posons $R=1/(1+C)>0$. Si $|t|<R$, alors pour tout $x\in[0,1]$,

$$
\left|\frac{P_k(x)}{k!}t^k\right|\le \bigl((1+C)|t|\bigr)^k .
$$

La série des majorants est géométrique convergente. **Pour chaque $|t|<R$, la série définissant $S$ converge normalement sur $[0,1]$.**

### Question 33

Fixons $|t|<R$.

Les termes de la série sont de classe $\mathcal C^1$ et la série converge simplement d'après Q32.

Pour $k\ge1$, le terme dérivé est $t$ fois le terme d'indice $k-1$, puisque $P_k'=kP_{k-1}$.

Par Q32, la série des dérivées converge donc normalement et uniformément sur $[0,1]$.

Le théorème de dérivation des séries de fonctions montre que $x\mapsto S(x,t)$ est de classe $\mathcal C^1$ et donne

$$
\boxed{\frac{\partial S}{\partial x}(x,t)=tS(x,t).}
$$

### Question 34

D'après Q33, la dérivée de $x\mapsto e^{-tx}S(x,t)$ est nulle sur $[0,1]$. Cette fonction est donc constante, de valeur $S(0,t)$. **Il existe ainsi $\alpha(t)=S(0,t)$ tel que $S(x,t)=\alpha(t)e^{tx}$.**

### Question 35

Par Q32, les sommes partielles convergent vers $S(\cdot,t)$ pour la norme uniforme. La continuité de $\varphi$ et la linéarité donnent

$$
\begin{aligned}
\varphi(S(\cdot,t))&=\lim_{N\to+\infty}\sum_{k=0}^N\frac{t^k}{k!}\varphi(P_k)\\
&=1,
\end{aligned}
$$

car seul le terme de rang $0$ contribue. Par Q34, $\alpha(t)\varphi(x\mapsto e^{tx})=1$. En particulier, le dénominateur est non nul et

$$
\boxed{\alpha(t)=\frac{1}{\varphi(x\mapsto e^{tx})}.}
$$

### Question 36

La forme $\varphi(g)=\int_0^1g(u)\,du$ est linéaire, vérifie $\varphi(1)=1$ et $|\varphi(g)|\le\|g\|_\infty$.

Elle est donc continue.

Ses polynômes $P_k$ sont exactement les $B_k$ par Q30, ce qui prouve leur existence et leur unicité.

Pour $t\ne0$, $\int_0^1 e^{tu}\,du=(e^t-1)/t$, tandis que l'intégrale vaut $1$ pour $t=0$.

D'après Q32, Q34 et Q35, sur $]-R,R[$ la série entière converge et sa somme vaut

$$
\boxed{
\sum_{k=0}^{+\infty}\frac{B_k(x)}{k!}t^k=
\begin{cases}
\dfrac{te^{tx}}{e^t-1}, & t\ne0,\\[4pt]
1, & t=0 .
\end{cases}}
$$

### Question 37

Pour $x,y\in\mathbb R$ et $p\ge0$, posons

$$
J_p(x,y)=\int_y^x\frac{P_p(x+y-t)}{p!}f^{(p+1)}(t)\,dt.
$$

Comme $P_0=1$, $J_0(x,y)=f(x)-f(y)$.

Pour $p\ge1$, une intégration par parties entre $y$ et $x$ donne, en utilisant $P_p'=pP_{p-1}$ et la dérivée de $x+y-t$,

$$
J_p(x,y)=\frac{P_p(y)}{p!}f^{(p)}(x)-\frac{P_p(x)}{p!}f^{(p)}(y)+J_{p-1}(x,y).
$$

On somme ces différences de $1$ à $p$ et on remplace $J_0$ par $f(x)-f(y)$. En isolant $f(x)$,

$$
\begin{aligned}
f(x)
&=f(y)+\sum_{k=1}^p\left(\frac{P_k(x)}{k!}f^{(k)}(y)-\frac{P_k(y)}{k!}f^{(k)}(x)\right)\\
&\quad+\int_y^x\frac{P_p(x+y-t)}{p!}f^{(p+1)}(t)\,dt .
\end{aligned}
$$

La somme est vide pour $p=0$, et les intégrales restent orientées quand $x<y$.

### Question 38

Fixons $x$.

Tous les termes de Q37 sont continus en $y$ sur $[0,1]$.

Pour le reste $J_p(x,y)$, on peut développer le polynôme $P_p(x+y-t)$ en puissances de $t$, à coefficients polynomiaux en $y$.

Chaque intégrale résultante de $t^j f^{(p+1)}(t)$ entre $y$ et $x$ est continue en $y$ par le théorème fondamental de l'analyse.

On applique donc $\varphi$ à Q37.

Elle conserve $f(x)$, constant en $y$, et annule chaque $P_k(y)$ pour $k\ge1$.

Ainsi,

$$
\boxed{
f(x)=\sum_{k=0}^p\frac{P_k(x)}{k!}\varphi(y\mapsto f^{(k)}(y))
+\varphi\bigl(y\mapsto J_p(x,y)\bigr).}
$$

### Question 39

L'évaluation en $0$ est linéaire et $|g(0)|\le\|g\|_\infty$, donc elle est continue sur $E$.

Ici $P_n(0)=0$ pour $n\ge1$.

Partant de $P_0=1$, la relation $P_n'=nP_{n-1}$ donne par récurrence $P_n(X)=X^n$.

En évaluant les fonctions de $y$ en $0$ dans Q38, on retrouve la formule de Taylor à l'origine avec reste intégral,

$$
\boxed{f(x)=\sum_{k=0}^p\frac{x^k}{k!}f^{(k)}(0)+\int_0^x\frac{(x-t)^p}{p!}f^{(p+1)}(t)\,dt.}
$$

### Question 40

On applique Q38 en $x=0$ à $F_j:u\mapsto f(u+j)$, de classe $\mathcal C^\infty$ sur $\mathbb R$.

Pour le reste, le changement de variable $t=u+j$ transforme l'intégrale entre $y$ et $0$ en une intégrale entre $y+j$ et $j$.

En inversant les bornes,

$$
\begin{aligned}
f(j)
&=\sum_{k=0}^p\frac{P_k(0)}{k!}\varphi(y\mapsto f^{(k)}(y+j))\\
&\quad-\varphi\left(y\mapsto \int_j^{y+j}\frac{P_p(y+j-t)}{p!}f^{(p+1)}(t)\,dt\right).
\end{aligned}
$$

**II — Formule d’Euler-Boole**

### Question 41

La demi-somme des évaluations en $0$ et $1$ est linéaire, vaut $1$ sur la constante $1$ et vérifie $|\varphi(g)|\le\|g\|_\infty$.

Q32, Q34 et Q35 s'appliquent avec $\varphi(x\mapsto e^{tx})=(1+e^t)/2$.

**Il existe $R>0$ tel que**, pour tout $x\in[0,1]$ et $|t|<R$,

$$
\boxed{\sum_{k=0}^{+\infty}\frac{E_k(x)}{k!}t^k=\frac{2e^{tx}}{1+e^t}.}
$$

### Question 42

Pour $x\in[0,1]$, l'expression de Q41 en $(1-x,t)$ coïncide avec son expression en $(x,-t)$, car

$$
\frac{2e^{t(1-x)}}{1+e^t}=\frac{2e^{-tx}}{1+e^{-t}}.
$$

L'unicité des coefficients d'une série entière donne $E_n(1-x)=(-1)^nE_n(x)$ sur $[0,1]$. Les deux polynômes coïncident sur une infinité de points, donc **$E_n(1-X)=(-1)^nE_n(X)$**.

### Question 43

On applique Q40 à la demi-somme des évaluations aux deux extrémités. Dans le reste, le terme en $y=0$ est nul, et pour $y=1$, Q42 donne $E_p(1-(t-j))=(-1)^pE_p(t-j)$. On obtient

$$
\begin{aligned}
f(j)
&=\frac12\sum_{k=0}^p\frac{e_k}{k!}\bigl(f^{(k)}(j)+f^{(k)}(j+1)\bigr)\\
&\quad-\frac12\int_j^{j+1}\frac{(-1)^p E_p(t-j)}{p!}f^{(p+1)}(t)\,dt.
\end{aligned}
$$

### Question 44

Pour $j=1,\dots,n$, on multiplie Q43 par $(-1)^{j-1}$ et on somme.

Pour chaque $k$, les coefficients de $f^{(k)}(j)$ se compensent pour $2\le j\le n$.

Il reste les contributions en $1$ et $n+1$, de signes respectifs $+$ et $(-1)^{n-1}$.

Dans le reste, pour $t\in[j,j+1[$, on a $\lfloor t\rfloor=j$ et $-(-1)^{j-1}(-1)^p E_p(t-j)=\widetilde E_p(t)$.

Cette fonction est continue par morceaux sur le segment et les valeurs aux entiers n'affectent pas les intégrales.

Par Chasles,

$$
\begin{aligned}
\sum_{j=1}^n(-1)^{j-1}f(j)
&=\frac12\sum_{k=0}^p\frac{e_k}{k!}f^{(k)}(1)\\
&\quad+\frac{(-1)^{n-1}}2\sum_{k=0}^p\frac{e_k}{k!}f^{(k)}(n+1)\\
&\quad+\frac12\int_1^{n+1}\frac{\widetilde E_p(t)}{p!}f^{(p+1)}(t)\,dt.
\end{aligned}
$$
