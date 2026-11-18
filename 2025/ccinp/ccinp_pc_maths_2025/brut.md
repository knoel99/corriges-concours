# CCINP PC — Mathématiques 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Exercice 1 — Étude d’un endomorphisme matriciel

### Partie I — Généralités

### Question 1

Le produit $AM$ est une matrice de $\mathcal M_n(\mathbb C)$.

La distributivité et la compatibilité avec les scalaires donnent $A(\alpha M+\beta N)=\alpha AM+\beta AN$ pour toutes matrices $M,N$ et tous scalaires $\alpha,\beta$. **$\varphi_A$ est donc un endomorphisme de $\mathcal M_n(\mathbb C)$.**

### Question 2

Pour toute $M\in\mathcal M_n(\mathbb C)$, l’associativité donne $(\varphi_A\circ\varphi_B)(M)=A(BM)=(AB)M$. **Ainsi $\varphi_A\circ\varphi_B=\varphi_{AB}$.**

### Question 3

Si $A$ est inversible, Q2 donne $\varphi_A\circ\varphi_{A^{-1}}=\varphi_{I_n}$ et l’identité dans l’autre ordre. Donc $\varphi_{A^{-1}}$ est l’inverse de $\varphi_A$.

Si $\varphi_A$ est un isomorphisme, sa surjectivité donne une matrice $B$ telle que $AB=I_n$. En prenant les déterminants, $\det A\det B=1$, donc $A$ est inversible. **Les deux propriétés sont équivalentes.**

### Partie II — Étude d’un exemple

### Question 4

La matrice triangulaire $A$ a pour valeurs propres $1$ et $a$.

Si $a\ne1$, elles sont distinctes et $A$ est diagonalisable.

Si $a=1$, une matrice diagonale semblable à $A$ devrait être $I_2$, ce qui imposerait $A=I_2$, en contradiction avec le coefficient hors diagonale. **$A$ est diagonalisable si et seulement si $a\ne1$.**

### Question 5

Dans l’ordre donné, les quatre matrices élémentaires sont $E_{11},E_{12},E_{21},E_{22}$. Leurs images sont respectivement $E_{11}$, $E_{12}$, $E_{11}+aE_{21}$ et $E_{12}+aE_{22}$. En plaçant leurs coordonnées en colonnes, on obtient
$$
\boxed{\operatorname{Mat}_{\mathcal C}(\varphi_A)=
\begin{pmatrix}
1&0&1&0\\
0&1&0&1\\
0&0&a&0\\
0&0&0&a
\end{pmatrix}.}
$$

### Question 6

La matrice de Q5 est triangulaire.

Si $a\ne1$, les valeurs propres sont $1$ et $a$, chacune de multiplicité algébrique $2$.

La différence avec $I_4$ impose que les deux dernières coordonnées soient nulles.

La différence avec $aI_4$ donne $(1-a)x_1+x_3=0$ et $(1-a)x_2+x_4=0$.

Dans chaque cas, deux coordonnées restent libres, donc les deux sous-espaces propres sont de dimension $2$.

Si $a=1$, la seule valeur propre est $1$. Le noyau de la différence avec $I_4$ impose encore $x_3=x_4=0$. **Le seul sous-espace propre est alors de dimension $2$.**

### Question 7

En Q6, la somme des dimensions des sous-espaces propres est $4$ si $a\ne1$, et $2$ si $a=1$.

Elle est égale à la dimension de $\mathcal M_2(\mathbb C)$ dans le premier cas seulement. **$\varphi_A$ est diagonalisable si et seulement si $a\ne1$.**

### Partie III — Réduction de φA si A est diagonalisable

### Question 8

Pour $k=0$, $\varphi_A^0=\mathrm{Id}=\varphi_{I_n}=\varphi_{A^0}$. Si $\varphi_A^k=\varphi_{A^k}$, Q2 donne $\varphi_A^{k+1}=\varphi_A\circ\varphi_{A^k}=\varphi_{A^{k+1}}$. **L’identité vaut donc pour tout $k\in\mathbb N$.**

### Question 9

Soit $P(X)=\sum_{k=0}^d c_kX^k$. Pour toute matrice $M$, Q8 donne
$$
\begin{aligned}
P(\varphi_A)(M)&=\sum_{k=0}^d c_k A^kM\\
&=P(A)M.
\end{aligned}
$$
Les deux applications coïncident sur toute matrice. **$P(\varphi_A)=\varphi_{P(A)}$.**

### Question 10

Un endomorphisme en dimension finie, ou sa matrice, est diagonalisable si et seulement s’il admet un polynôme annulateur non nul scindé à racines simples sur le corps de base.

D’après Q9, $P(A)=0$ implique $P(\varphi_A)=0$.

Réciproquement, si $P(\varphi_A)=0$, évaluons $\varphi_{P(A)}$ en $I_n$ pour obtenir $P(A)=0$.

Les deux objets ont les mêmes polynômes annulateurs. **$A$ et $\varphi_A$ sont donc diagonalisables simultanément.**

### Question 11

Cayley-Hamilton donne $\chi_A(A)=0$.

Q9 entraîne $\chi_A(\varphi_A)=0$.

Si $\mu$ est une valeur propre de $\varphi_A$ et $M$ un vecteur propre non nul associé, alors $0=\chi_A(\varphi_A)(M)=\chi_A(\mu)M$.

Donc $\chi_A(\mu)=0$ et $\mu$ est une valeur propre de $A$.

Réciproquement, pour tout vecteur propre $v\ne0$ de $A$ de valeur propre $\lambda$, plaçons $v$ dans la première colonne de $M$ et des zéros dans les autres.

On a $AM=\lambda M$ et $M\ne0$. **Les spectres de $A$ et de $\varphi_A$ sont égaux.**

### Question 12

Si $M$ a pour colonnes $C_1,\ldots,C_n$, alors $AM$ a pour colonnes $AC_1,\ldots,AC_n$.

Ainsi $AM=\lambda M$ équivaut à $AC_j=\lambda C_j$ pour tout $j$. **L’appartenance de $M$ au sous-espace propre équivaut à l’appartenance de chacune de ses colonnes à $E_\lambda(A)$**, y compris les colonnes nulles.

### Question 13

Pour chaque valeur propre $\lambda$ de $A$, notons $m_\lambda=\dim E_\lambda(A)$. Comme $A$ et $\varphi_A$ sont diagonalisables par Q10, leurs multiplicités algébriques sont les dimensions des sous-espaces propres. Q12 donne $\dim E_\lambda(\varphi_A)=nm_\lambda$.

En multipliant les valeurs propres avec leurs multiplicités pour le déterminant et en les additionnant pour la trace, on trouve
$$
\boxed{\begin{aligned}
\det(\varphi_A)&=(\det A)^n,\\
\operatorname{Tr}(\varphi_A)&=n\operatorname{Tr}(A).
\end{aligned}}
$$

## Exercice 2 — Les polynômes de Hermite

### Partie I — Préliminaires

### I.1 — Un produit scalaire sur l’espace des polynômes

### Question 14

La fonction $t^n e^{-t^2}$ est continue sur $[0,+\infty[$. À l’infini, $t^{n+2}e^{-t^2}$ tend vers zéro par croissance comparée. Ainsi $0\le t^n e^{-t^2}\le t^{-2}$ pour $t$ assez grand, ce qui assure l’intégrabilité sur la demi-droite positive.

La substitution $t=-s$ donne la même intégrale en valeur absolue sur la demi-droite négative. **La fonction est donc intégrable sur $\mathbb R$.**

### Question 15

Un polynôme est une combinaison linéaire finie de monômes. En multipliant son expression par $e^{-t^2}$, on obtient une combinaison finie des fonctions intégrables sur $\mathbb R$ de Q14. **La fonction $t\mapsto R(t)e^{-t^2}$ est intégrable sur $\mathbb R$.**

### Question 16

Q15 appliquée à $R=PQ$ assure que $\varphi(P,Q)$ est définie. La linéarité de l’intégrale donne la bilinéarité. La commutativité du produit donne la symétrie.

Enfin $\varphi(P,P)$ est l’intégrale de la fonction continue et positive ou nulle $P(t)^2e^{-t^2}$. Si cette intégrale est nulle, la fonction est identiquement nulle, puisqu’une valeur strictement positive donnerait par continuité une intégrale strictement positive sur un petit intervalle. Le poids est partout strictement positif, donc $P=0$. **La forme est ainsi un produit scalaire.**

### I.2 — Calcul de l’intégrale de Gauss

### Question 17

La fonction $t\mapsto e^{-t^2}$ est continue sur $\mathbb R$. Le théorème fondamental de l’analyse appliqué à son intégrale à borne supérieure variable donne **$u\in\mathcal C^1(\mathbb R)$ et $u'(x)=e^{-x^2}$**.

### Question 18

Notons $h(x,t)=e^{-(1+t^2)x^2}/(1+t^2)$ pour $t\in[0,1]$.

Pour chaque $x$, cette fonction de $t$ est continue, donc intégrable.

Pour chaque $t$, c’est une fonction de classe $\mathcal C^1$ en $x$, avec $\partial_x h=-2x e^{-(1+t^2)x^2}$.

Sur tout segment $[-K,K]$ avec $K>0$, on a $|\partial_x h(x,t)|\le2K$, fonction constante intégrable sur $[0,1]$.

Par le théorème de dérivation d’une intégrale à paramètre sur chacun de ces segments, **$v$ est de classe $\mathcal C^1$ sur $\mathbb R$** et
$$
\boxed{v'(x)=-2x e^{-x^2}\int_0^1 e^{-x^2t^2}\,\mathrm dt.}
$$

### Question 19

La fonction $t\mapsto u(xt)$ a pour dérivée $x e^{-x^2t^2}$. En intégrant de zéro à un, on obtient $x\int_0^1 e^{-x^2t^2}\,\mathrm dt=u(x)$, pour tout réel $x$.

Ainsi Q17 et Q18 donnent $v'(x)=-2u(x)u'(x)$.

La dérivée de $u^2+v$ est nulle sur $\mathbb R$.

Comme $u(0)=0$ et $v(0)=[\arctan t]_0^1=\pi/4$, **$u(x)^2+v(x)=\pi/4$ pour tout $x$**.

### Question 20

Pour $t\in[0,1]$, l’intégrande de $v(x)$ est entre zéro et $e^{-x^2}$. Donc $0\le v(x)\le e^{-x^2}$ et $v(x)\to0$ quand $x\to+\infty$.

Par Q14, $u(x)$ converge vers l’intégrale sur $[0,+\infty[$. Cette limite est positive, donc Q19 donne $\int_0^\infty e^{-t^2}\,\mathrm dt=\sqrt\pi/2$. Par parité,
$$
\boxed{\int_{\mathbb R} e^{-t^2}\,\mathrm dt=\sqrt\pi.}
$$

### Partie II — Quelques propriétés des polynômes de Hermite

### Question 21

$H_0=1$ a pour degré zéro et coefficient dominant $1=2^0$.

Supposons $H_n$ de degré $n$ et de coefficient dominant $2^n$.

Alors $2XH_n$ a pour degré $n+1$ et pour coefficient dominant $2^{n+1}$.

Le terme $H_n'$ est nul si $n=0$ et de degré $n-1$ sinon.

Il ne change donc pas le terme dominant de $H_{n+1}$. **La propriété vaut par récurrence.**

### Question 22

Pour $n=0$, $H_0=1$ donne l’identité. Si elle est vraie au rang $n$, dérivons en utilisant $f'(x)=-2xf(x)$.
$$
\begin{aligned}
f^{(n+1)}(x)&=(-1)^n\bigl(H_n'(x)-2xH_n(x)\bigr)f(x)\\
&=(-1)^{n+1}H_{n+1}(x)f(x).
\end{aligned}
$$
Le dernier passage utilise la récurrence définissant $H_{n+1}$. **L’identité demandée vaut pour tout $n$.**

### Question 23

Pour $k=0$, Q22 remplace $H_qf$ par $(-1)^q f^{(q)}$ dans le produit scalaire.

Soit $0\le k<q$. Sur $[-R,R]$, intégrons $H_p^{(k)} f^{(q-k)}$ par parties avec la primitive $f^{(q-k-1)}$. Le terme de bord $[H_p^{(k)}f^{(q-k-1)}]_{-R}^R$ tend vers zéro par Q22 et croissance comparée. Les deux intégrandes sont des produits de polynômes et de $f$, donc intégrables par Q15. On peut passer à la limite et obtenir
$$
\int_{\mathbb R} H_p^{(k)}(t)f^{(q-k)}(t)\,\mathrm dt
=-\int_{\mathbb R} H_p^{(k+1)}(t)f^{(q-k-1)}(t)\,\mathrm dt.
$$
Le signe se combine avec $(-1)^{q-k}$ pour donner $(-1)^{q-k-1}$. **La récurrence donne la formule pour tout $0\le k\le q$.**

### Question 24

Pour $p<q$, Q23 au rang $k=q$ donne $\varphi(H_p,H_q)=0$, car $H_p^{(q)}=0$ par Q21.

La famille est donc orthogonale par symétrie et ses éléments sont non nuls par Q21.

Elle est libre et compte $d+1$ éléments dans l’espace de dimension $d+1$. **C’est une base orthogonale de $\mathbb R_d[X]$.**

### Question 25

En Q23, prenons $q=p$ et $k=p$. Q21 donne $H_p^{(p)}=2^p p!$, puisque les termes de degré inférieur disparaissent. Par Q20, le carré de la norme vaut $2^p p!\sqrt\pi$. **Ainsi $\|H_p\|=\sqrt{2^p p!\sqrt\pi}$.**

### Partie III — Série génératrice exponentielle des polynômes de Hermite

### III.1 — Expression de la série génératrice

### Question 26

Le développement de l’exponentielle sur $\mathbb C$ donne
$$
\begin{aligned}
e^{2xz}&=\sum_{n\ge0}\frac{(2x)^n}{n!}z^n,\\
e^{-z^2}&=\sum_{n\ge0}\frac{(-1)^n}{n!}z^{2n}.
\end{aligned}
$$
Chaque série converge absolument pour tout $z$ par convergence absolue de la série de l’exponentielle à l’argument considéré. **Les deux rayons sont infinis, y compris si $x=0$.**

### Question 27

On a $e^{-(x-z)^2}=e^{-x^2}e^{2xz}e^{-z^2}$. Par Q26, à chaque $z$ les deux dernières fonctions sont les sommes de séries absolument convergentes.

Leur produit de Cauchy est une série entière, de coefficients indépendants de $z$, qui converge absolument en chaque $z$ vers le produit. Après multiplication par $e^{-x^2}$, on obtient **une série $\sum c_nz^n$ de rayon infini et de somme $e^{-(x-z)^2}$**.

### Question 28

Sur l’axe réel, dérivons $n$ fois en zéro l’identité $f(x-t)=\sum_{j\ge0}c_jt^j$, en utilisant la dérivation terme à terme d’une série entière à l’intérieur de son rayon. On obtient $n!c_n=(-1)^nf^{(n)}(x)$.

Par Q22, ceci vaut $H_n(x)e^{-x^2}$. En remplaçant $c_n$ dans la série complexe de Q27 et en multipliant par $e^{x^2}$, on trouve
$$
\boxed{e^{2xz-z^2}=\sum_{n\ge0}\frac{H_n(x)}{n!}z^n \qquad(z\in\mathbb C).}
$$
Le rayon reste infini par Q27.

### III.2 — Expression intégrale des polynômes de Hermite

### Question 29

Pour chaque $n$, le facteur exponentiel complexe qui définit $g_n$ a pour module un. Ainsi $\sup_{\theta\in[0,2\pi]}|g_n(\theta)|=|H_n(x)|/n!$. La série de ces majorants converge par convergence absolue de la série entière de Q28 en $z=1$. **La convergence est normale sur $[0,2\pi]$.**

### Question 30

Par Q28 en $z=e^{\mathrm i\theta}$, $G_x(e^{\mathrm i\theta})e^{-\mathrm ip\theta}=\sum_{n\ge0}g_n(\theta)$. Les $g_n$ sont continues et la convergence est uniforme sur le segment par Q29. Le théorème d’intégration terme à terme s’applique, aux parties réelle et imaginaire si besoin.

L’intégrale de $e^{\mathrm i(n-p)\theta}$ sur le segment vaut $2\pi$ si $n=p$. Sinon, une primitive est $e^{\mathrm i(n-p)\theta}/(\mathrm i(n-p))$ et les valeurs aux deux bords coïncident. Seul le terme $n=p$ reste. Par conséquent,
$$
\boxed{H_p(x)=\frac{p!}{2\pi}\int_0^{2\pi}G_x(e^{\mathrm i\theta})e^{-\mathrm ip\theta}\,\mathrm d\theta.}
$$

## Exercice 3 — Succession de tirages dans une urne

### Partie I — Probabilité de l’événement E

### Question 31

Posons $A_n=\bigcap_{k=1}^n B_k$. Comme $A_{n+1}\subset A_n$, la suite $p_n=\mathbb P(A_n)$ décroît. Elle est minorée par zéro, donc converge. Or $E=\bigcap_{n\ge1} A_n$. Par continuité décroissante de la probabilité, **$\mathbb P(E)=\lim_{n\to\infty}p_n$.**

### Question 32

Sur $A_k$, chaque tirage précédent a ajouté le nombre prescrit de boules blanches après remise de la boule tirée. Il y a donc $S_k=1+\sum_{i=1}^ku_i$ boules blanches et toujours une boule rouge.

L’événement $A_k$ a une probabilité strictement positive. En effet $A_1$ a pour probabilité $1/2$ et toute histoire faite uniquement de tirages blancs possède au moins une boule blanche au tirage suivant. Le tirage uniforme parmi les $S_k+1$ boules donne **$\mathbb P(B_{k+1}\mid A_k)=S_k/(S_k+1)$.**

### Question 33

On a $p_1=1/2=S_0/(S_0+1)$. Pour $k\ge1$, la formule des probabilités composées et Q32 donnent $p_{k+1}=p_k S_k/(S_k+1)$. Par récurrence,
$$
\boxed{p_n=\prod_{k=0}^{n-1}\frac{S_k}{S_k+1}.}
$$

### Partie II — Caractérisation de la propriété P(E) = 0

### Question 34

Chaque $u_k$ est un entier au moins égal à un. Donc $S_n\ge n+1$. **La suite tend vers $+\infty$.**

### Question 35

Par Q34, $1/S_k\to0$. Or
$$
-\ln\!\left(\frac{S_k}{S_k+1}\right)=\ln(1+1/S_k)\sim \frac1{S_k}.
$$
Ces termes sont strictement positifs. Par comparaison de séries à termes positifs, **la série des logarithmes demandée et celle des $1/S_k$ ont la même nature**.

### Question 36

D’après Q33, $-\ln p_n=\sum_{k=0}^{n-1}\ln(1+1/S_k)$. Les termes sont positifs, donc la somme partielle tend vers $+\infty$ exactement quand la série diverge. Comme $p_n$ tend vers $\mathbb P(E)$ par Q31, ceci équivaut à $\mathbb P(E)=0$.

Par Q35, **$\mathbb P(E)=0$ si et seulement si $\sum_k 1/S_k$ diverge**. Lorsque la série converge, $-\ln p_n$ a une limite réelle et le passage à l’exponentielle donne une probabilité strictement positive.

### Question 37

Si tous les $u_k$ valent un, $S_k=k+1$. La série des inverses est harmonique et diverge. **Par Q36, $\mathbb P(E)=0$.**

### Question 38

Prenons $u_k=2^{k-1}$ pour $k\ge1$. Alors $S_k=2^k$ pour tout $k\ge0$. Les inverses forment une série géométrique convergente, donc **$\mathbb P(E)>0$** par Q36.
