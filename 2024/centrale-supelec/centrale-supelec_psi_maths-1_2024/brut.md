# CentraleSupélec PSI — Mathématiques 1 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Intégrale de Wallis et Intégrale de Gauss

### I.A

#### Question 1

Pour $0<t<\pi/2$, on a $0<\cos t<1$, donc $\cos^{n+1}t<\cos^n t$. La différence est continue et strictement positive sur l'intérieur de l'intervalle. En intégrant, on obtient **$0<W_{n+1}<W_n$ pour tout $n\in\mathbb N$**.

#### Question 2

On intègre par parties sur $[0,\pi/2]$ en dérivant $\cos^{n+1}t$ et en intégrant $\cos t$. Le terme de bord $[\sin t\,\cos^{n+1}t]_0^{\pi/2}$ est nul. Ainsi
$$
W_{n+2}=(n+1)\int_0^{\pi/2}\sin^2t\,\cos^n t\,dt
=(n+1)(W_n-W_{n+2}).
$$
On en déduit **$(n+2)W_{n+2}=(n+1)W_n$**.

#### Question 3

D'après la question 2, $(n+2)W_{n+1}W_{n+2}=(n+1)W_nW_{n+1}$. La suite $((n+1)W_nW_{n+1})_{n\ge0}$ est donc constante. Comme $W_0=\pi/2$ et $W_1=[\sin t]_0^{\pi/2}=1$,
$$
\boxed{(n+1)W_nW_{n+1}=\frac{\pi}{2}.}
$$

#### Question 4

Les questions 1 et 2 donnent
$$
\frac{n+1}{n+2}=\frac{W_{n+2}}{W_n}\le\frac{W_{n+1}}{W_n}\le1.
$$
Donc $W_{n+1}/W_n\to1$. Par la question 3, $W_n^2=(W_n/W_{n+1})\pi/(2(n+1))\sim\pi/(2n)$. En prenant les racines positives,
$$
\boxed{W_n\sim\sqrt{\frac{\pi}{2n}}\qquad(n\to+\infty).}
$$

### I.B

#### Question 5

La fonction $x\mapsto e^{-x^2}$ est continue et positive sur $[0,+\infty[$. Pour $x\ge1$, elle est majorée par $e^{-x}$, intégrable sur $[1,+\infty[$. **L'intégrale $I$ converge.**

#### Question 6

Pour $n\ge1$, on pose $f_n(x)=(1-x^2/n)^n$ sur $[0,\sqrt n]$ et $f_n(x)=0$ au-delà. Ces fonctions sont continues, car elles s'annulent au point de raccordement.

Pour $x\ge0$ fixé et $n>x^2$, le développement de $\log(1-u)$ au voisinage de $0$ donne $n\log(1-x^2/n)\to-x^2$, d'où $f_n(x)\to e^{-x^2}$.

Pour $0\le x\le\sqrt n$, l'inégalité $1-u\le e^{-u}$, appliquée à $u=x^2/n$, donne $0\le f_n(x)\le e^{-x^2}$. Le majorant convient aussi au-delà de $\sqrt n$ et est intégrable par la question 5. Le théorème de convergence dominée fournit
$$
\boxed{\lim_{n\to+\infty}\int_0^{\sqrt n}(1-x^2/n)^n\,dx=I.}
$$

#### Question 7

Pour $n\ge1$, $u\mapsto\sqrt n\sin u$ est une bijection croissante de classe $C^1$ de $[0,\pi/2]$ sur $[0,\sqrt n]$. L'intégrande est continue sur ce dernier segment. La formule de changement de variable donne
$$
\int_0^{\sqrt n}(1-x^2/n)^n\,dx
=\sqrt n\int_0^{\pi/2}(\cos^2u)^n\cos u\,du
=\boxed{\sqrt n\,W_{2n+1}}.
$$

#### Question 8

Par les questions 4, 6 et 7, $I=\lim_{n\to+\infty}\sqrt n\,W_{2n+1}=\sqrt\pi/2$. La fonction $x\mapsto e^{-x^2}$ est paire. Les deux demi-intégrales convergent et sont égales. Ainsi
$$
\boxed{\begin{aligned}I&=\frac{\sqrt\pi}{2},\\J&=\sqrt\pi.\end{aligned}}
$$

## Partie II — Autour d'une équation différentielle

### II.A

#### Question 9

L'énoncé imprime $\mathbb R[X]$.

Si l'on impose à $y$ d'être un polynôme non nul de degré $d$, le terme $xy$ a degré $d+1$, tandis que $xy''+y'$ a degré au plus $d-1$ s'il est non nul.

La seule solution polynomiale est donc nulle. Pour que la question 10 ait un sens, on cherche les solutions développables en série entière sur $\mathbb R$.

Si $y(x)=\sum_{k\ge0}a_kx^k$ a un rayon de convergence strictement positif, on peut dériver deux fois terme à terme à l'intérieur de son intervalle de convergence. L'identification des coefficients dans $xy''+y'+xy=0$ donne $a_1=0$ puis $(k+2)^2a_{k+2}+a_k=0$ pour $k\ge0$.

Tous les coefficients impairs sont nuls et, pour $m\ge0$, la récurrence donne $a_{2m}=(-1)^ma_0/(4^m(m!)^2)$.

Réciproquement, pour tout $a_0\in\mathbb R$, la série obtenue a un rayon infini. En effet, pour $x\ne0$, le rapport des modules de deux termes successifs de la série en $m$ sans son facteur $a_0$ vaut $|x|^2/(4(m+1)^2)\to0$.

Ses coefficients vérifient les relations ci-dessus. La dérivation terme à terme redonne donc l'équation sur $\mathbb R$. **Toutes les solutions demandées sont les fonctions suivantes, pour $a_0\in\mathbb R$**
$$
\boxed{y(x)=a_0\sum_{m=0}^\infty\frac{(-1)^m x^{2m}}{4^m(m!)^2}.}
$$

#### Question 10

Dans la famille de la question 9, $y(0)=a_0$. La condition choisit exactement $a_0=1$, d'où **l'existence et l'unicité** de
$$
\boxed{S(x)=\sum_{m=0}^\infty\frac{(-1)^m x^{2m}}{4^m(m!)^2}.}
$$

### II.B

#### Question 11

Pour tout $x$, $t\mapsto\cos(x\sin t)$ est continue et intégrable sur $[0,\pi]$. L'intégrande et ses deux dérivées partielles en $x$ sont continues sur $\mathbb R\times[0,\pi]$.

Les deux dérivées, $-\sin t\sin(x\sin t)$ et $-\sin^2t\cos(x\sin t)$, sont chacune majorées en module par $1$, intégrable sur ce segment et indépendant de $x$.

Par le théorème de dérivation des intégrales à paramètre, **$G$ est de classe $C^2$ sur $\mathbb R$** et
$$
\begin{aligned}
G'(x)&=-\frac1\pi\int_0^\pi\sin t\sin(x\sin t)\,dt, \\
G''(x)&=-\frac1\pi\int_0^\pi\sin^2t\cos(x\sin t)\,dt.
\end{aligned}
$$

#### Question 12

En utilisant les expressions de la question 11,
$$
\begin{aligned}
\pi\bigl(xG''(x)+G'(x)+xG(x)\bigr)
&=\int_0^\pi\bigl[x\cos^2t\cos(x\sin t)-\sin t\sin(x\sin t)\bigr]\,dt\\
&=[\cos t\sin(x\sin t)]_0^\pi=0.
\end{aligned}
$$
**$G$ satisfait l'équation sur $\mathbb R$, y compris en $0$.**

#### Question 13

Pour tout $x\in\mathbb R$ fixé, la série du cosinus appliquée à $x\sin t$ converge uniformément en $t\in[0,\pi]$, car le module du terme d'indice $m$ est majoré par $|x|^{2m}/(2m)!$. On intègre terme à terme sur le segment. Cela donne
$$
G(x)=\sum_{m=0}^\infty
\left(\frac{(-1)^m}{\pi(2m)!}\int_0^\pi\sin^{2m}t\,dt\right)x^{2m}.
$$
Les coefficients sont indépendants de $x$ et cette série converge pour tout $x$ par la même majoration. Puisque $G(0)=1$ et que $G$ satisfait l'équation, la question 10 donne **$G=S$**.

## Partie III — Étude d'un endomorphisme sur un espace préhilbertien

### III.A — Les polynômes d'Hermite

#### Question 14

Les trois premières dérivées de $e^{-x^2}$ sont, dans l'ordre, $-2xe^{-x^2}$, $(4x^2-2)e^{-x^2}$ et $(12x-8x^3)e^{-x^2}$. Après multiplication par $(-1)^ne^{x^2}$, on trouve
$$
\boxed{\begin{aligned}H_1(x)&=2x,\\H_2(x)&=4x^2-2,\\H_3(x)&=8x^3-12x.\end{aligned}}
$$

#### Question 15

La dérivation de la définition de $H_n$ donne
$$
H_n'(x)=2xH_n(x)+(-1)^ne^{x^2}w^{(n+1)}(x)
=2xH_n(x)-H_{n+1}(x).
$$
Ainsi **$H_{n+1}=2XH_n-H_n'$**.

#### Question 16

On raisonne par récurrence sur la propriété « $H_n$ est de degré $n$ et $H_n(-x)=(-1)^nH_n(x)$ ». Elle est vraie au rang $0$ puisque $H_0=1$.

Si elle est vraie au rang $n$, le terme $2XH_n$ a degré $n+1$ et $H_n'$ est nul ou de degré au plus $n-1$. La différence de la question 15 est donc de degré $n+1$.

De plus, $2XH_n$ a la parité opposée à celle de $H_n$. En dérivant $H_n(-x)=(-1)^nH_n(x)$, on obtient aussi $H_n'(-x)=(-1)^{n+1}H_n'(x)$. Donc $H_{n+1}$ a la parité de $n+1$.

**Pour tout $n$, $H_n$ est de degré $n$ et de la parité de $n$.**

#### Question 17

Si $c_n$ est le coefficient dominant de $H_n$, le terme de degré $n+1$ dans la question 15 provient de $2XH_n$. Donc $c_{n+1}=2c_n$ et $c_0=1$.

**Le coefficient dominant de $H_n$ est $2^n$.**

### III.B — Un produit scalaire

#### Question 18

L'ensemble $E$ contient la fonction nulle. Pour $f,g\in E$ et $a,b\in\mathbb R$, $af+bg$ est continue et
$$
0\le(af+bg)^2e^{-x^2}\le2a^2 f^2 e^{-x^2}+2b^2 g^2 e^{-x^2}.
$$
Le majorant est intégrable, donc $E$ est un sous-espace de $C^0(\mathbb R,\mathbb R)$.

Pour tout polynôme $P$, $P^2e^{-x^2/2}$ est bornée par croissance comparée aux deux infinis et continuité. Il existe donc $C\ge0$ tel que $0\le P^2e^{-x^2}\le C e^{-x^2/2}$. Or $e^{-x^2/2}$ est intégrable par dilatation de l'intégrale de la question 8. **Ainsi $\mathbb R[X]\subset E$.**

#### Question 19

Si $f,g\in E$, la fonction $fge^{-x^2}$ est continue et $2|fg|e^{-x^2}\le(f^2+g^2)e^{-x^2}$. L'intégrale est donc absolument convergente. La symétrie résulte de $fg=gf$, et la bilinéarité, de la linéarité de l'intégrale dans chaque variable.

La forme est positive. Si $f$ prend une valeur non nulle en un point, la continuité de $f^2e^{-x^2}$ donne un segment de longueur positive sur lequel cette fonction est minorée par une constante strictement positive. Dans ce cas $\langle f,f\rangle>0$. **La forme est donc définie positive et constitue un produit scalaire sur $E$.**

### III.C — Lien entre le produit scalaire et les polynômes d'Hermite

#### Question 20

La définition donne $H_ne^{-x^2}=(-1)^nw^{(n)}$. Pour $n\ge1$, on intègre $Pw^{(n)}$ par parties sur $[-A,A]$. Le terme de bord tend vers zéro quand $A\to+\infty$ car, d'après la définition et la question 16, $Pw^{(n-1)}=(-1)^{n-1}PH_{n-1}e^{-x^2}$ tend vers zéro aux deux infinis. Les intégrales restantes convergent absolument par les questions 18 et 19. Par conséquent,
$$
\begin{aligned}
\langle P,H_n\rangle&=\frac{(-1)^n}{\sqrt\pi}\int_{\mathbb R}P(x)w^{(n)}(x)\,dx\\
&=\frac{(-1)^{n-1}}{\sqrt\pi}\int_{\mathbb R}P'(x)w^{(n-1)}(x)\,dx\\
&=\boxed{\langle P',H_{n-1}\rangle}.
\end{aligned}
$$

#### Question 21

En appliquant $n$ fois la question 20, $\langle P,H_n\rangle=\langle P^{(n)},H_0\rangle$. Si $P\in\mathbb R_{n-1}[X]$, $P^{(n)}=0$. Donc **$\langle P,H_n\rangle=0$**.

#### Question 22

Si $i<j\le n$, on a $H_i\in\mathbb R_{j-1}[X]$ par la question 16, donc $\langle H_i,H_j\rangle=0$ par la question 21. Chaque $H_i$ est non nul puisqu'il est de degré $i$.

La famille orthogonale de $n+1$ vecteurs non nuls est libre dans l'espace de dimension $n+1$. **Elle en est une base orthogonale.**

#### Question 23

Pour $n\ge1$, on applique la question 20 successivement aux couples $(H_n,H_n),(H_n',H_{n-1}),\ldots,(H_n^{(n-1)},H_1)$. On obtient
$$
\boxed{\|H_n\|^2=\langle H_n^{(n)},H_0\rangle.}
$$
Pour $n=0$ l'égalité est immédiate.

#### Question 24

Par la question 17, $H_n^{(n)}=2^n n!$. Or $H_0=1$ et $\langle1,1\rangle=J/\sqrt\pi=1$ par la question 8. De la question 23 on tire
$$
\boxed{\|H_n\|=\sqrt{2^n n!}.}
$$

### III.D — Étude d'un endomorphisme autoadjoint

#### Question 25

La dérivation, la multiplication par $X$ et l'identité sont des applications linéaires de $\mathbb R[X]$ dans lui-même. Ainsi $u$ est linéaire.

Si $P\in\mathbb R_n[X]$, chacun des termes $-P''$, $2XP'$ et $P$ est de degré au plus $n$ lorsqu'il est non nul, ce qui inclut les cas des polynômes constants ou de faible degré.

**$\mathbb R_n[X]$ est stable par $u$.**

#### Question 26

En appliquant les compositions à un polynôme $P$,
$$
\begin{aligned}
(v\circ w)(P)&=2XP'-P''=u(P)-P, \\
(w\circ v)(P)&=(2XP-P')'=2P+2XP'-P''\\
&=u(P)+P.
\end{aligned}
$$
**$v\circ w=u-\mathrm{Id}$ et $w\circ v=u+\mathrm{Id}$.**

#### Question 27

Grâce à la question 26 et à l'associativité de la composition,
$$
\begin{aligned}
u\circ v&=(v\circ w+\mathrm{Id})\circ v\\
&=v\circ(u+\mathrm{Id})+v\\&=v\circ u+2v.
\end{aligned}
$$
Donc **$u\circ v-v\circ u=2v$**.

#### Question 28

Si $u(P)=\lambda P$, la question 27 et la linéarité de $v$ donnent
$$
u(v(P))=v(u(P))+2v(P)=\boxed{(\lambda+2)v(P)}.
$$

#### Question 29

On a $u(H_0)=H_0$, puisque $H_0=1$. Par la question 15, $v(H_k)=H_{k+1}$.

Si $u(H_k)=(2k+1)H_k$, la question 28 donne $u(H_{k+1})=(2k+3)H_{k+1}$. Par récurrence, la relation est vraie pour tout $k\ge0$.

Chaque $H_k$ est non nul d'après la question 16. **$H_k$ est donc vecteur propre de $u$ pour la valeur propre $2k+1$.**

#### Question 30

La base $(H_0,\dots,H_n)$ de $\mathbb R_n[X]$ donnée par la question 22 est faite de vecteurs propres de $u_n$ d'après la question 29. Sa matrice dans cette base a pour diagonale $(1,3,\ldots,2n+1)$. **$u_n$ est diagonalisable sur $\mathbb R$.**

#### Question 31

En intégrant par parties sur $[-A,A]$, le terme de bord est $[P'Qe^{-x^2}]_{-A}^A$. Il tend vers zéro par croissance comparée aux deux infinis. Toutes les intégrales de produits de polynômes par le poids convergent absolument par les questions 18 et 19. Le passage à la limite donne
$$
\begin{aligned}
\langle P',Q'\rangle
&=-\frac1{\sqrt\pi}\int_{\mathbb R}(P''-2xP')Qe^{-x^2}\,dx\\
&=\boxed{\langle u(P),Q\rangle-\langle P,Q\rangle}.
\end{aligned}
$$

#### Question 32

Pour $P,Q\in\mathbb R_n[X]$, la question 31 donne $\langle u_n(P),Q\rangle=\langle P',Q'\rangle+\langle P,Q\rangle$. Le second membre est symétrique en $P,Q$. La symétrie du produit scalaire entraîne $\langle u_n(P),Q\rangle=\langle P,u_n(Q)\rangle$. **$u_n$ est autoadjoint.**

#### Question 33

L'espace $\mathbb R_n[X]$, muni du produit scalaire de la question 19, est un espace euclidien car sa dimension est finie. L'endomorphisme $u_n$ est autoadjoint par la question 32. **Le théorème spectral fournit une base orthonormée de vecteurs propres de $u_n$ sur $\mathbb R$.**

#### Question 34

Par les questions 22, 24 et 29, il suffit de normaliser chaque élément de la base orthogonale propre. Une base orthonormale cherchée est
$$
\boxed{\left(\frac{H_k}{\sqrt{2^k k!}}\right)_{0\le k\le n}.}
$$

## Partie IV — Une famille totale

### Question 35

La seconde occurrence de $\xi$ dans l'énoncé désigne $f\in E$. Pour $f\in E$ et $\xi\in\mathbb R$, la fonction demandée est continue et
$$
|f(x)e^{-ix\xi}e^{-x^2}|=|f(x)|e^{-x^2}
\le \tfrac12\bigl(f(x)^2e^{-x^2}+e^{-x^2}\bigr).
$$
Le membre de droite est intégrable par définition de $E$ et par la question 8. **La fonction est absolument intégrable sur $\mathbb R$.**

### Question 36

Pour tout $p\ge0$, $x^{2p}e^{-x^2/2}$ est bornée par continuité et croissance comparée. La fonction continue positive $x^{2p}e^{-x^2}$ est donc intégrable par comparaison avec un multiple de $e^{-x^2/2}$. On a $M_0=\sqrt\pi$ par la question 8.

Pour $p\ge1$, comme $(e^{-x^2})'=-2xe^{-x^2}$, une intégration par parties sur $[-A,A]$ donne
$$
\int_{-A}^A x^{2p}e^{-x^2}\,dx
=\left[-\tfrac12 x^{2p-1}e^{-x^2}\right]_{-A}^A
+\frac{2p-1}{2}\int_{-A}^A x^{2p-2}e^{-x^2}\,dx.
$$
Le terme de bord tend vers zéro. On obtient $M_p=\frac{2p-1}{2}M_{p-1}$. En multipliant ces rapports et en séparant les facteurs pairs et impairs de $(2p)!$,
$$
\boxed{M_p=\sqrt\pi\,\frac{(2p)!}{4^p p!}\qquad(p\ge0).}
$$

### Question 37

Pour tout $x$ réel et tout $\xi$ réel, la série de l'exponentielle donne
$$
f(x)e^{-x^2}\sum_{n=0}^\infty\frac{(-i)^n\xi^nx^n}{n!}
=f(x)e^{-x^2}e^{-ix\xi}.
$$
La somme des fonctions est intégrable par la question 35. On obtient donc l'identité demandée en intégrant cette égalité point par point. L'interversion de la série et de l'intégrale est justifiée à la question suivante.

### Question 38

Soit $B=\bigl(\int_{\mathbb R} f^2e^{-x^2}\bigr)^{1/2}$. Par Cauchy-Schwarz sur $[-A,A]$, puis par passage à la limite en utilisant la définition de $E$ et la question 36,
$$
\int_{\mathbb R}|x|^n|f(x)|e^{-x^2}\,dx\le B\sqrt{M_n}.
$$
En particulier, chaque terme de la série de la question 37 est intégrable. Pour $R>0$, la série de terme $b_n=R^n\sqrt{M_n}/n!$ converge puisque
$$
\frac{b_{n+1}}{b_n}=\frac{R}{n+1}\sqrt{\frac{2n+1}{2}}\longrightarrow0.
$$
Pour $|\xi|\le R$, la somme des intégrales des modules des termes de la question 37 est donc majorée par $B\sum b_n$. La somme des fonctions est continue par la question 37. Le théorème d'intégration terme à terme (appliqué aux parties réelle et imaginaire) donne
$$
\boxed{\mathcal F(f)(\xi)=\sum_{n=0}^\infty
\left(\frac{(-i)^n}{n!}\int_{\mathbb R}x^nf(x)e^{-x^2}\,dx\right)\xi^n.}
$$
Comme $R>0$ est arbitraire, la série entière obtenue a un rayon de convergence infini.

### Question 39

Pour tout $n\ge0$, $X^n$ appartient à $\operatorname{Vect}(H_0,\dots,H_n)$ par la question 22. L'hypothèse d'orthogonalité implique $\langle X^n,f\rangle=0$. En multipliant par $\sqrt\pi$, on obtient **$\int_{\mathbb R} x^n f(x)e^{-x^2}\,dx=0$**.

### Question 40

La question 39 annule chacun des coefficients de la série entière obtenue à la question 38. Cette série représente $\mathcal F(f)$ sur tout $\mathbb R$, donc **$\mathcal F(f)=0$**.

### Question 41

L'injectivité de $\mathcal F$ sur $E$ est admise dans l'énoncé. La question 40 donne donc $f=0$. La fonction nulle appartient à l'orthogonal, d'où $(\operatorname{Vect}(H_n,\ n\in\mathbb N))^\perp=\{0\}$. **La famille $(H_n)_{n\in\mathbb N}$ est totale dans $E$.**
