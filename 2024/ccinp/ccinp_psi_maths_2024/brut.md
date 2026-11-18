# CCINP PSI — Mathématiques 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Problème 1 — File d’attente

### Partie I — Temps d’arrivée du n-ième client

### Question 1

L’événement $\{T_1=k\}$ est l’intersection de $\{X_i=0\}$ pour $1\le i<k$ et de $\{X_k=1\}$. L’indépendance des arrivées donne **$\mathbb P(T_1=k)=(1-p)^{k-1}p$**.

### Question 2

$A=\left(\bigcup_{k\ge1}\{T_1=k\}\right)^c$. Les événements de l’union sont deux à deux disjoints. Leur probabilité totale est $p\sum_{j\ge0}(1-p)^j=1$. Ainsi **$\mathbb P(A)=0$**. Presque sûrement, un nouveau client finit par arriver.

### Question 3

Posons $q=1-p\in]0,1[$.

Les coefficients de $G_{T_1}$ pour $k\ge1$ valent $pq^{k-1}$.

Le rapport de deux termes consécutifs en module est $q|t|$ si $t\ne0$.

Le rayon est donc **$R=1/q$**.

Pour $|t|<R$, la somme géométrique donne
$$
\boxed{G_{T_1}(t)=\frac{pt}{1-qt}.}
$$
Aux deux extrémités du domaine réel, les termes ne tendent pas vers zéro.

### Question 4

Comme $1<R$, les dérivées en $1$ donnent les moments factoriels. On a $G_{T_1}'(t)=p/(1-qt)^2$ et $G_{T_1}''(t)=2pq/(1-qt)^3$. Ainsi
$$
\begin{aligned}
\mathbb E(T_1)&=G_{T_1}'(1)=1/p,\\
\operatorname{Var}(T_1)&=G_{T_1}''(1)+G_{T_1}'(1)-G_{T_1}'(1)^2
=\boxed{q/p^2}.
\end{aligned}
$$

### Question 5

Les $T_i$ ont la même loi. La linéarité de l’espérance et l’indépendance pour la variance et les fonctions génératrices donnent
$$
\boxed{\begin{aligned}
\mathbb E(D_n)&=n/p,\\
\operatorname{Var}(D_n)&=nq/p^2,\\
G_{D_n}(t)&=\left(\frac{pt}{1-qt}\right)^n\quad(|t|<1/q).
\end{aligned}}
$$

### Question 6

Pour $|x|<1$, $(1+x)^\alpha=\sum_{j\ge0}\binom{\alpha}{j}x^j$, où $\binom{\alpha}{0}=1$ et $\binom{\alpha}{j}=\alpha(\alpha-1)\cdots(\alpha-j+1)/j!$ pour $j\ge1$.

Pour $\alpha=-n$ et $x=-qt$, on a $\binom{-n}{j}(-1)^j=\binom{n+j-1}{j}$. Ainsi
$$
G_{D_n}(t)=p^n\sum_{j\ge0}\binom{n+j-1}{j}q^j t^{n+j}.
$$
Par unicité des coefficients, **$\mathbb P(D_n=k)=0$ si $k<n$ et $\mathbb P(D_n=k)=\binom{k-1}{k-n}p^nq^{k-n}$ si $k\ge n$**.

### Partie II — Étude du comportement de la file

### II.1 — Une suite récurrente

### Question 7

Pour $0<x<1$, $a(x-1)<0$ et $0<f(x)<1$. L’intervalle est stable, donc tous les $z_n$ y appartiennent.

La fonction $f$ est strictement croissante. Par conséquent $z_{n+2}-z_{n+1}=f(z_{n+1})-f(z_n)$ a le même signe que $z_{n+1}-z_n$, y compris si cette différence est nulle. **Le signe est celui de $z_2-z_1$ à tout rang.**

### Question 8

La suite est monotone par Q7 et bornée par $0$ et $1$. Elle converge donc vers $\ell\in[0,1]$. La continuité de $f$ dans la relation de récurrence donne **$f(\ell)=\ell$**.

### Question 9

Pour $x>0$, on peut comparer $x$ et $f(x)>0$ en prenant le logarithme, qui est strictement croissant.

Comme $\ln f(x)=a(x-1)$, **$\psi(x)\ge0$ équivaut à $f(x)\le x$, et $\psi(x)=0$ à $f(x)=x$**.

La formule de $\psi$, donnée sur $]0,1]$, s’étend ici à tout $x>0$.

### Question 10

Sur $]0,1[$, $\psi'(x)=1/x-a>0$ si $a\le1$.

Or $\psi(1)=0$.

Ainsi $\psi<0$ sur $]0,1[$ et $1$ est son seul zéro sur $]0,1]$.

De plus, $f(0)=e^{-a}>0$.

Le seul point fixe de $f$ dans $[0,1]$ est donc $1$.

Par Q8, **$z_n\to1$**.

### Question 11

Si $a>1$, $\psi$ croît strictement sur $]0,1/a]$ et décroît strictement sur $[1/a,1]$.

Comme $\psi(1)=0$, le maximum $\psi(1/a)$ est positif.

Avec $\psi(x)\to-\infty$ lorsque $x\to0^+$, il existe un unique zéro $\alpha\in]0,1/a[$ en plus de $1$.

Le signe de $\psi$ est négatif sur $]0,\alpha[$ et positif sur $]\alpha,1[$.

Avec $f(0)>0$, les seuls points fixes de $[0,1]$ sont donc $\alpha$ et $1$.

Si $z_1\le\alpha$, la croissance de $f$ maintient $z_n\le\alpha$.

Si $z_1>\alpha$, Q9 donne $z_2<z_1$, et la suite décroît tout en restant au-dessus de $\alpha$.

Dans les deux cas, $1$ est exclu comme limite. **$z_n\to\alpha$.**

### II.2 — Groupes de clients

### Question 12

Un groupe vide ne peut produire aucun client du groupe suivant. **$Z$ décrit l’extinction de la file issue du client initial**, autrement dit une période d’activité qui se termine après un nombre fini de groupes. Il peut y avoir de nouvelles arrivées après cette extinction.

### Question 13

$N_n=\sum_{i=1}^nX_i$ est la somme de $n$ variables de Bernoulli indépendantes de paramètre $p$. **$N_n\sim\mathcal B(n,p)$**, avec $N_0=0$ si l’intervalle est vide.

### Question 14

Conditionnellement à $S=n$, $V_1=N_n$ en loi par indépendance. Pour $0\le k\le n$, la probabilité conditionnelle vaut $\binom nk p^kq^{n-k}$. Pour $k>n$, elle vaut zéro.

La formule des probabilités totales, avec $j=n-k$, donne
$$
\begin{aligned}
\mathbb P(V_1=k)
&=\sum_{n\ge k}e^{-\lambda}\frac{\lambda^n}{n!}\binom nk p^k q^{n-k}\\
&=e^{-\lambda}\frac{(\lambda p)^k}{k!}\sum_{j\ge0}\frac{(\lambda q)^j}{j!}
=\boxed{e^{-\lambda p}\frac{(\lambda p)^k}{k!}}.
\end{aligned}
$$
**$V_1$ suit la loi de Poisson de paramètre $\lambda p$.**

### Question 15

Les événements $\{V_n=0\}$ croissent avec $n$, puisqu’un groupe vide entraîne l’extinction des suivants. La continuité croissante des probabilités donne **$z_n\uparrow\mathbb P(Z)$**. Si l’on indexe à partir de zéro, on pose $V_0=1$ pour le client initial.

### Question 16

Si $j=0$, l’absence de premier groupe entraîne celle de tous les suivants. La probabilité conditionnelle vaut $1$, comme le produit vide.

Pour $j\ge1$, le calcul attendu utilise le modèle de branchement implicite dans cette question. Chaque service utilise une durée fraîche indépendante et un bloc frais d’essais d’arrivée. Sous ce modèle, chacun des $j$ clients du premier groupe engendre une descendance indépendante ayant la même loi que celle du client initial.

Le groupe $n+1$ est vide exactement si chacune de ces $j$ descendances est vide à sa génération $n$. Chaque événement a pour probabilité $z_n$. Par indépendance,

**$\mathbb P(V_{n+1}=0\mid V_1=j)=z_n^j$**.

Pour $n=0$ et $j\ge1$, les descendants à la génération zéro sont les clients eux-mêmes, donc la probabilité est bien $0$. La seule indépendance explicitement énoncée entre $S$ et les arrivées suffit pour Q14. Pour Q16, il faut aussi le renouvellement indépendant des services.

### Question 17

Les événements $\{V_1=j\}$ forment un système complet. Par Q14 et Q16, en notant $a=\lambda p$,
$$
z_{n+1}=\sum_{j\ge0}z_n^j e^{-a}\frac{a^j}{j!}
=\boxed{e^{a(z_n-1)}}.
$$

### Question 18

$z_1=e^{-a}\in]0,1[$.

Lorsque $\lambda p\le1$, Q10 et Q15 donnent $\mathbb P(Z)=1$.

Lorsque $\lambda p>1$, Q11 donne $\mathbb P(Z)=\alpha$, où $\alpha\in]0,1[$ est l’unique point fixe strictement inférieur à $1$. **La file s’éteint presque sûrement dans le premier cas.**

**Dans le second, sa probabilité de persister indéfiniment vaut $1-\alpha>0$.**

## Exercice — Équivalent de Stirling

### Question 19

Au voisinage de $0$, $t^{x-1}e^{-t}\sim t^{x-1}$. Le critère de Riemann y donne la convergence exactement si $x>0$.

À l’infini, $t^{x+1}e^{-t}\to0$ pour tout $x\in\mathbb R$. L’intégrande positif est donc majoré à partir d’un certain rang par $1/t^2$. **L’intégrale converge exactement pour $x>0$.**

### Question 20

Sur $[\varepsilon,A]$, on intègre $t^x e^{-t}$ par parties. Le terme de bord $-t^x e^{-t}$ tend vers zéro à l’infini et en $0^+$ pour $x>0$. Les intégrales convergent par Q19. Ainsi **$\Gamma(x+1)=x\Gamma(x)$**.

Comme $\Gamma(1)=\int_0^\infty e^{-t}\,\mathrm dt=1$, la récurrence donne **$\Gamma(n)=(n-1)!$** pour $n\ge1$.

### Question 21

Avec $t=u^2$, $\Gamma(1/2)=2\int_0^\infty e^{-u^2}\,\mathrm du=\sqrt\pi$. La relation de Q20 donne
$$
\begin{aligned}
\Gamma(n+1/2)&=\sqrt\pi\prod_{k=1}^n\frac{2k-1}{2}\\
&=\boxed{\frac{(2n)!}{2^{2n}n!}\sqrt\pi}.
\end{aligned}
$$
La dernière égalité sépare les facteurs pairs et impairs de $(2n)!$. Pour $n=0$, le produit est vide.

### Question 22

Q20 donne $\ln\Gamma(n)=\sum_{k=1}^{n-1}\ln k$. Dans chaque terme, remplaçons $\ln k$ par $\rho_k+\int_{k-1/2}^{k+1/2}\ln t\,\mathrm dt$. Par Chasles, les intégrales contiguës se regroupent et donnent
$$
\boxed{\ln\Gamma(n)=\int_{1/2}^{n-1/2}\ln t\,\mathrm dt+\sum_{k=1}^{n-1}\rho_k}.
$$
Pour $n=1$, l’intervalle est réduit à un point et la somme est vide. Les deux membres sont nuls.

### Question 23

Avec le changement $t=k+s$ dans la définition de $\rho_k$, puis $s=-t$ sur la moitié négative,
$$
\rho_k=\int_0^{1/2}\bigl(2\ln k-\ln(k+t)-\ln(k-t)\bigr)\,\mathrm dt.
$$
Comme $k-t>0$, on regroupe les logarithmes et on obtient **$\rho_k=\int_0^{1/2}-\ln(1-t^2/k^2)\,\mathrm dt$**.

### Question 24

Pour $0\le u\le1/4$, $-\ln(1-u)=\int_0^u (1-v)^{-1}\,\mathrm dv\le4u/3$. Or $0\le t^2/k^2\le1/4$ dans Q23. Ainsi $0\le\rho_k\le \frac4{3k^2}\int_0^{1/2}t^2\,\mathrm dt$. **La série des $\rho_k$ converge par comparaison à $\sum k^{-2}$.**

### Question 25

Posons $L=\sum_{k\ge1}\rho_k$. Par Q22, on a
$$
\ln\Gamma(n)=(n-1/2)\ln(n-1/2)-(n-1/2)
-\left(\tfrac12\ln(1/2)-\tfrac12\right)+L+o(1).
$$
Or $(n-1/2)\ln(1-1/(2n))=-1/2+o(1)$. On obtient
$$
\begin{aligned}
\ln\Gamma(n)&=(n-1/2)\ln n-n+c+o(1),\\
c&=L-\tfrac12\ln(1/2)+\tfrac12.
\end{aligned}
$$
En exponentiant et en utilisant $e^{o(1)}\to1$, **$\Gamma(n)\sim e^c n^{n-1/2}e^{-n}$**.

### Question 26

Substituons $t=nu$. On a $\mathrm dt=n\,\mathrm du$ et $t^{x-1}=n^{x-1}u^{x-1}$. En faisant tendre la borne inférieure vers zéro dans l’intégrale ainsi transformée,
$$
\boxed{\Gamma_n(x)=n^x\int_0^1u^{x-1}(1-u)^n\,\mathrm du}.
$$

### Question 27

Notons $B_n(x)$ l’intégrale de Q26 sans le facteur $n^x$, pour $n\ge0$.

On a $B_0(x)=1/x$ pour $x>0$.

Pour $n\ge1$, une intégration par parties avec la primitive $u^x/x$ donne $B_n(x)=n B_{n-1}(x+1)/x$.

Le terme de bord s’annule en $0$ car $x>0$ et en $1$ car $n\ge1$. En itérant jusqu’à $B_0(x+n)$,
$$
\boxed{\Gamma_n(x)=\frac{n^x n!}{x(x+1)\cdots(x+n)}}.
$$

### Question 28

Pour $t>0$ fixé, dès que $n>t$, on a $(1-t/n)^n\to e^{-t}$, car $n\ln(1-t/n)\to -t$.

Les intégrandes prolongés par zéro hors de $]0,n[$ convergent donc simplement vers $t^{x-1}e^{-t}$ sur $]0,+\infty[$.

Sur $]0,n[$, $\ln(1-t/n)\le-t/n$ donne $0\le(1-t/n)^n\le e^{-t}$. Hors de cet intervalle, le prolongement nul vérifie la même domination après multiplication par $t^{x-1}$. Le majorant $t^{x-1}e^{-t}$ est intégrable par Q19. La convergence dominée, puis Q27, donnent
$$
\boxed{\Gamma_n(x)\longrightarrow\Gamma(x)
=\lim_{n\to\infty}\frac{n^x n!}{x(x+1)\cdots(x+n)}}.
$$

### Question 29

Par itération de Q20, $x(x+1)\cdots(x+n)=\Gamma(x+n+1)/\Gamma(x)$. Comme $\Gamma(x)>0$, Q28 donne
$$
\frac{n^x\Gamma(n+1)}{\Gamma(x+n+1)}\longrightarrow1.
$$
Son inverse est $\frac{x+n}{n}\frac{\Gamma(x+n)}{\Gamma(n)n^x}$. Le premier facteur tend vers $1$, donc **$\Gamma(x+n)/(\Gamma(n)n^x)\to1$**.

Prenons $x=1/2$. Par Q21 et Q20,
$$
1\ \sim\ \frac{\Gamma(n+1/2)}{\Gamma(n)\sqrt n}
=\frac{\sqrt{\pi n}\,(2n)!}{4^n(n!)^2}.
$$
La forme de Q25 entraîne $n!=n\Gamma(n)\sim e^c n^{n+1/2}e^{-n}$, et le même équivalent s’applique à $(2n)!$ avec $2n$. En remplaçant ces deux expressions, le dernier quotient tend vers $\sqrt{2\pi}\,e^{-c}$. Ainsi **$e^c=\sqrt{2\pi}$**.

## Problème 2 — Blocs de Jordan

### Partie I — Irréductibilité de Jλ

### Question 30

$u_0(e_j)=e_{j+1}$ pour $j<p$ et $u_0(e_p)=0$.

Ainsi $u_0^2(e_j)=e_{j+2}$ pour $j\le p-2$ et vaut zéro sinon. $J_0^2$ a donc des $1$ sur la deuxième sous-diagonale et des zéros ailleurs, et elle est nulle si $p=2$.

Plus généralement, $u_0^r(e_j)=e_{j+r}$ si $j+r\le p$, et vaut zéro sinon.

Donc $J_0^{p-1}$ n’a qu’un coefficient non nul, $1$ à la position $(p,1)$, et $J_0^p=0$. **L’indice de nilpotence est $p$.**

### Question 31

La matrice $J_\lambda$ est triangulaire, de diagonale constante égale à $\lambda$.

Son unique valeur propre est $\lambda$.

Comme $u_\lambda-\lambda\,\mathrm{Id}=u_0$, son sous-espace propre est $\ker u_0$.

Or $u_0$ décale chaque $e_j$ pour $j<p$ sur le vecteur suivant. **$\operatorname{Sp}(u_\lambda)=\{\lambda\}$ et $E_\lambda=\mathbb R e_p$.**

### Question 32

Pour $v\in V$, les vecteurs $u_\lambda(v)$ et $u_0(v)$ diffèrent de $\lambda v\in V$. **L’un appartient à $V$ exactement lorsque l’autre y appartient.**

### Question 33

Les $k$ premiers vecteurs de $\widetilde B$ sont dans $V$, et leurs images sont dans $V$ par stabilité. Leurs colonnes ont donc des zéros aux lignes $k+1$ à $p$. La matrice est
$$
\boxed{\begin{pmatrix}\operatorname{Mat}_{( \tilde e_1,\ldots,\tilde e_k)}(v)&B\\0&C\end{pmatrix}},
$$
avec les blocs complémentaires de tailles $k\times(p-k)$ et $(p-k)\times(p-k)$. Si $k=p$, seul le premier bloc subsiste.

### Question 34

Le déterminant par blocs donne $\chi_{u_\lambda}(X)=\chi_v(X)\det(XI_{p-k}-C)$, avec facteur complémentaire $1$ si $k=p$. Ainsi $\chi_v$ divise $(X-\lambda)^p$.

Il est unitaire et de degré $k\ge1$, donc vaut $(X-\lambda)^k$.

L’endomorphisme $v$ a un vecteur propre non nul dans $V$ pour la valeur propre $\lambda$.

Vu dans $\mathbb R^p$, ce vecteur appartient à $\mathbb R e_p$ par Q31. **Il s’ensuit que $e_p\in V$.**

### Question 35

Si deux sous-espaces non nuls $V$ et $W$ sont stables, Q34 impose $e_p\in V\cap W$. Puisque $e_p\ne0$, cette intersection est non nulle. **Il ne peut donc pas s’agir d’une somme directe.**

### Partie II — Stabilité du système linéaire associé

### Question 36

Comme $J_\lambda X_0=\lambda X_0$, la fonction $\widetilde X(t)=e^{\lambda t}X_0$ est de classe $\mathcal C^1$ et vérifie $\widetilde X'(t)=\lambda e^{\lambda t}X_0=J_\lambda\widetilde X(t)$. **C’est une solution de $(S)$.**

### Question 37

Posons $P(t)=\sum_{k=0}^{p-1}t^kJ_0^k/k!$. C’est un polynôme matriciel et
$$
\begin{aligned}
P'(t)&=\sum_{k=0}^{p-2}\frac{t^k}{k!}J_0^{k+1}\\
&=J_0P(t).
\end{aligned}
$$
le dernier terme de $J_0P(t)$ s’annulant par nilpotence. Par la règle du produit, $\varphi'(t)=(\lambda I+J_0)e^{\lambda t}P(t)=J_\lambda\varphi(t)$. Comme $\varphi(t)$ est un scalaire multiplié par un polynôme en $J_0$, elle commute avec $J_\lambda$. **$\varphi'(t)=J_\lambda\varphi(t)=\varphi(t)J_\lambda$.**

### Question 38

Les termes de la somme infinie donnée sont nuls dès $k=p$. Elle est donc égale à la somme finie de la définition.

Le produit $F(t)=\varphi(t)\varphi(-t)$ est dérivable, et Q37 donne
$$
F'(t)=\varphi(t)J_\lambda\varphi(-t)-\varphi(t)J_\lambda\varphi(-t)=0.
$$
Comme $F(0)=I$, on a $\varphi(t)\varphi(-t)=I$ et, en remplaçant $t$ par $-t$, l’identité dans l’autre ordre. **$\varphi(t)^{-1}=\varphi(-t)$.**

### Question 39

Pour $X$ de classe $\mathcal C^1$, la règle du produit et Q37 donnent $Y'(t)=\varphi(-t)(X'(t)-J_\lambda X(t))$. Par Q38, ce vecteur est nul pour tout $t$ exactement lorsque $X$ résout $(S)$.

Réciproquement, si $Y$ est constante égale à $X_0$, l’identité $X(t)=\varphi(t)X_0$ assure elle-même la régularité de $X$. **Les solutions sont exactement $X(t)=\exp(tJ_\lambda)X_0$, pour $X_0=X(0)\in E$.**

### Question 40

Prenons $X_0=e_p$, vecteur propre non nul associé à $\lambda$. Q36 donne une solution de norme $\|e^{\lambda t}e_p\|=e^{\lambda t}$, qui tend vers $+\infty$ si $\lambda>0$. **Il existe une solution non bornée sur $\mathbb R_+$.**

### Question 41

Pour chaque ligne $i$, Cauchy-Schwarz donne
$$
\left|(AX)_i\right|^2
\le\left(\sum_{j=1}^p|a_{ij}|^2\right)\|X\|^2 .
$$
En sommant en $i$ puis en prenant la racine, **$\|AX\|\le N(A)\|X\|$**.

Par Q39 et l’inégalité triangulaire pour $N$, toute solution vérifie pour $t\ge0$
$$
\|X(t)\|\le \|X_0\|\,e^{\lambda t}
\sum_{k=0}^{p-1}\frac{t^k}{k!}N(J_0^k).
$$
Si $\lambda<0$, chaque terme tend vers zéro à l’infini. La continuité sur les intervalles compacts complète l’argument. **Toutes les solutions sont bornées sur $\mathbb R_+$ et tendent vers zéro.**

### Question 42

Si $\lambda=0$, prenons $X_0=e_{p-1}$, qui existe puisque $p\ge2$.

On a $J_0X_0=e_p$ et $J_0^2X_0=0$, donc $X(t)=e_{p-1}+te_p$.

Sa norme vaut $\sqrt{1+t^2}$. **Il existe une solution non bornée**.

Plus précisément, les seules solutions bornées sont les constantes issues de $\ker J_0$, car tout polynôme vectoriel non constant est non borné sur $\mathbb R_+$.
