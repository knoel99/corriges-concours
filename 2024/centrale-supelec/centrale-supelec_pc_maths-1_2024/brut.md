# Centrale-Supélec PC — Mathématiques 1 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## I — Approximations de la racine carrée de 2

### I.A — Développement en série entière

### Question 1

Si $\alpha=m\in\mathbb N$, le facteur $\alpha-m$ intervient dans $a_n$ dès que $n\ge m+1$. La série est alors polynomiale et son rayon vaut $+\infty$.

Si $\alpha\notin\mathbb N$, aucun coefficient ne s’annule et
$$
\left|\frac{a_{n+1}}{a_n}\right|=\frac{|\alpha-n|}{n+1}\longrightarrow1.
$$
Le critère de d’Alembert donne la convergence absolue pour $|x|<1$ et la divergence pour $|x|>1$. Le rayon vaut donc $1$.

### Question 2

Sur $]-R,R[$, la fonction somme est **$x\mapsto(1+x)^\alpha$**.

### Question 3

Pour $\alpha=1/2$, les coefficients vérifient $a_{n+1}=\frac{1-2n}{2(n+1)}a_n$. D’autre part, $b_0=-1$, et la simplification des factorielles donne, pour tout $n\ge0$,
$$
\frac{b_{n+1}}{b_n}=\frac{2n-1}{2(n+1)}.
$$
La suite $((-1)^{n+1}b_n)$ satisfait donc la même récurrence que $(a_n)$, avec la même valeur initiale $1$. Ainsi, pour $|x|<1$,
$$
\sqrt{1+x}=\sum_{n=0}^{+\infty}(-1)^{n+1}b_nx^n.
$$

### Question 4

La formule de Stirling donne
$$
\frac{(2n)!}{4^n(n!)^2}\sim\frac{1}{\sqrt{\pi n}}.
$$
Comme $2n-1\sim2n$, **$b_n\sim1/(2\sqrt\pi\,n^{3/2})$**. Par comparaison avec une série de Riemann d’exposant $3/2$, la série $\sum_{n\ge0}(-1)^{n+1}b_n$ converge absolument.

### Question 5

Sur $[-1,1]$, on a $|(-1)^{n+1}b_nx^n|\le|b_n|$. La série numérique $\sum_{n\ge0}|b_n|$ converge d’après Q4. La série de fonctions converge donc normalement, puis uniformément sur $[-1,1]$. Sa somme $S$ y est continue, car chaque terme est continu.

Sur $]-1,1[$, Q3 donne $S(x)=\sqrt{1+x}$. En passant à la limite lorsque $x\to1^-$,
$$
\boxed{\sum_{n=0}^{+\infty}(-1)^{n+1}b_n=\sqrt2.}
$$

### Question 6

Pour $n\ge1$, $b_n>0$ et le quotient calculé en Q3 est strictement compris entre $0$ et $1$. La suite $(b_n)_{n\ge1}$ décroît vers zéro. L’estimation du reste d’une série alternée donne, pour $n\ge1$,
$$
\left|\sqrt2-\sum_{k=0}^n(-1)^{k+1}b_k\right|\le b_{n+1}.
$$
Or $b_{n+1}=O(n^{-3/2})$ d’après Q4. On obtient le développement demandé.

### I.B — Méthode de Héron

### Question 7

Fixons $a\ge0$. Au rang $0$, $c_0(a)=1$ est défini et strictement positif.

Supposons $c_n(a)$ défini et strictement positif à un rang $n$. Le quotient $a/c_n(a)$ est alors défini et positif ou nul. La moyenne de $c_n(a)>0$ et de ce quotient est strictement positive. Ainsi $c_{n+1}(a)$ est défini et strictement positif, ce qui achève la récurrence.

### Question 8

En développant le carré de la relation de récurrence, on obtient
$$
\boxed{c_{n+1}(a)^2-a=\frac{(c_n(a)^2-a)^2}{4c_n(a)^2}.}
$$
Le second membre est positif ou nul. Comme $c_{n+1}(a)>0$, il en résulte $c_{n+1}(a)\ge\sqrt a$ pour tout $n\ge0$, donc la minoration vaut à partir du rang $1$.

### Question 9

Pour $n\ge1$, Q8 donne
$$
c_{n+1}(a)-c_n(a)=\frac{a-c_n(a)^2}{2c_n(a)}\le0.
$$
La suite à partir du rang $1$ est décroissante et minorée par $\sqrt a$. Elle converge vers un réel $\ell\ge0$.

On passe à la limite dans $2c_{n+1}(a)c_n(a)=c_n(a)^2+a$ et l’on trouve $\ell^2=a$. Ainsi **$c_n(a)\to\sqrt a$**, y compris lorsque $a=0$.

### Question 10

On a $c_1(2)=3/2$. Posons $e_n=c_n(2)^2-2$. Pour $n\ge1$, les questions précédentes donnent
$$
\begin{aligned}e_{n+1}&=\frac{e_n^2}{4c_n(2)^2}\\&\le\frac{e_n^2}{8}.\end{aligned}
$$
Comme $e_1=1/4$, on déduit par récurrence que
$$
0\le\frac{e_n}{8}\le\left(\frac1{32}\right)^{2^{n-1}}.
$$
En effet, l’égalité vaut au rang $1$ et l’inégalité $(e_{n+1}/8)\le(e_n/8)^2$ double l’exposant à chaque passage. Enfin,
$$
c_n(2)-\sqrt2=\frac{e_n}{c_n(2)+\sqrt2}
=O\left(\left(\frac1{32}\right)^{2^{n-1}}\right).
$$

### I.C — Comparaison et calcul

### Question 11

Pour $n\ge1$, $2^{n-1}\ge n$, comme on le vérifie par récurrence en utilisant $2n\ge n+1$. Ainsi
$$
0\le n^{3/2}\left(\frac1{32}\right)^{2^{n-1}}\le n^{3/2}32^{-n}\longrightarrow0.
$$
Le rapport de la seconde suite à la première tend donc vers zéro. La suite de Héron fournit la borne d’erreur qui décroît le plus vite.

### Question 12

Au rang $4$, la borne de Q10 donne $c_4(2)^2-2\le 8\cdot32^{-8}<10^{-11}$. On encadre exactement $\sqrt2$ entre $2/c_4(2)$ et $c_4(2)$. Les deux bornes ont le même arrondi à dix décimales, ce que les opérations entières suivantes vérifient.

```python
def arrondi_echelle(num, den, echelle):
    # Entier le plus proche de echelle * num / den, au demi supérieur.
    return (2 * echelle * num + den) // (2 * den)

u, v = 1, 1
for _ in range(4):
    u, v = u * u + 2 * v * v, 2 * u * v

echelle = 10**10
bas = arrondi_echelle(2 * v, u, echelle)
haut = arrondi_echelle(u, v, echelle)
assert bas == haut
assert (2 * v * echelle) // u == (u * echelle) // v == 14142135623
entier, decimales = divmod(haut, echelle)
print(f"{entier}.{decimales:010d}")
```

La mise à jour calcule la moyenne de $u/v$ et $2v/u$. L’affichage obtenu est **$1{,}4142135624$** à dix décimales.

La troncature à dix décimales vaut $1{,}4142135623$ : les parties entières des deux bornes multipliées par $10^{10}$ valent toutes deux $14142135623$.

## II — Racine carrée d’une matrice symétrique positive

### II.A — Racines orthogonales de l’identité

### Question 13

Les matrices orthogonales d’ordre $2$ sont les rotations et les symétries axiales. Elles s’écrivent respectivement
$$
R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\qquad
S_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{pmatrix}
\quad(\theta\in\mathbb R).
$$

### Question 14

Comme $R_\theta^2=R_{2\theta}$, une rotation est une racine carrée de $I_2$ exactement lorsque $\theta\in\pi\mathbb Z$. Cela fournit les deux matrices $I_2$ et $-I_2$.

Pour tout $\theta$ réel, le calcul donne $S_\theta^2=I_2$. Les racines recherchées sont donc $\{I_2,-I_2\}\cup\{S_\theta:\theta\in\mathbb R\}$. Les matrices $S_\theta$ sont distinctes pour $\theta\in[0,2\pi[$. En particulier, $I_2$ a une infinité de racines carrées.

### II.B — Existence et unicité

### Question 15

Une matrice symétrique réelle est positive **si et seulement si son spectre est inclus dans $[0,+\infty[$**.

### Question 16

D’après le théorème spectral, il existe une matrice orthogonale $P$ telle que $M=P\,\mathrm{diag}(\lambda_1,\dots,\lambda_q)P^{\mathsf T}$. Les $\lambda_i$ sont positifs ou nuls. On pose
$$
B=P\,\mathrm{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_q})P^{\mathsf T}.
$$
La matrice $B$ est symétrique. Ses valeurs propres sont positives ou nulles, donc elle est positive par Q15. Comme $P^{\mathsf T}P=I_q$, on a $B^2=M$.

### Question 17

Soit $D$ une racine carrée symétrique positive de $M$. Puisque $M=D^2$, les matrices $M$ et $D$ commutent.

Pour toute valeur propre $\lambda$ de $M$, le sous-espace propre $E_\lambda(M)$ est donc stable par $D$.

La restriction de $D$ à ce sous-espace est symétrique pour le produit scalaire induit et positive. Son carré est $\lambda$ fois l’identité. Par le théorème spectral, chacune de ses valeurs propres est positive ou nulle et a pour carré $\lambda$. Elle vaut donc $\sqrt\lambda$, et la restriction est $\sqrt\lambda$ fois l’identité.

Ainsi $D$ coïncide avec $B$ sur chaque sous-espace propre de $M$. Leur somme directe est tout l’espace, donc **$D=B$**.

### II.C — Itération de Héron matricielle

### Question 18

Pour $n=0$, la formule vaut puisque $c_0(\lambda_i)=1$ pour tout $i$. Supposons-la établie au rang $n$. Les termes $c_n(\lambda_i)$ sont strictement positifs d’après Q7, donc $M_n$ est inversible et
$$
M_n^{-1}=P\,\mathrm{diag}\bigl(1/c_n(\lambda_1),\dots,1/c_n(\lambda_q)\bigr)P^{\mathsf T}.
$$
En substituant les expressions diagonales dans la récurrence, on obtient
$$
\begin{aligned}M_{n+1}&=P\,\mathrm{diag}(d_1,\dots,d_q)P^{\mathsf T},\\
d_i&=\frac{c_n(\lambda_i)+\lambda_i/c_n(\lambda_i)}{2}\quad (1\le i\le q).\end{aligned}
$$
Le $i$-ième coefficient diagonal intérieur est $c_{n+1}(\lambda_i)$, ce qui achève la récurrence.

### Question 19

Les matrices diagonales dans Q18 convergent coefficient par coefficient vers $\mathrm{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_q})$ d’après Q9. Les propriétés de convergence rappelées dans l’énoncé permettent de multiplier par $P$ à gauche et $P^{\mathsf T}$ à droite. La limite est donc la racine carrée symétrique positive construite en Q16. Par l’unicité de Q17, **$M_n\to\sqrt M$**.


## III — Méthode de Newton numérique

### III.A — Convergence locale

### Question 20

La dérivée $f'$ est continue et ne s’annule pas sur l’intervalle $I$. Le théorème des valeurs intermédiaires implique qu’elle garde un signe strict. Le théorème des accroissements finis donne alors la stricte monotonie de $f$ sur $I$. En particulier, $f$ possède **au plus un zéro** dans $I$.

### Question 21

Le segment $J_r$ est compact et les fonctions $|f'|$ et $|f''|$ y sont continues. Elles y atteignent leurs bornes.

Ainsi $s_r$ est fini et le minimum $i_r$ est la valeur de $|f'|$ en un point de $J_r$. Puisque $f'$ n’y a pas de zéro, on a $i_r>0$.

### Question 22

Choisissons $r_0>0$ tel que $J_{r_0}\subset I$, ce qui est possible puisque $I$ est ouvert et contient $c$.

Pour $0<r\le r_0$, l’inclusion des segments donne $s_r\le s_{r_0}$ et $i_r\ge i_{r_0}>0$.

Donc $0\le K_r\le K_{r_0}$. On prend $r>0$ assez petit pour que $rK_{r_0}<1$. Il vérifie bien $0\le rK_r<1$.

### Question 23

Le segment entre $c_n$ et $c$ est dans $J_r$. L’inégalité de Taylor-Lagrange à l’ordre un donne
$$
\bigl|f(c)-f(c_n)-f'(c_n)(c-c_n)\bigr|
\le\frac{s_r}{2}|c-c_n|^2.
$$
Comme $f(c)=0$ et $c_{n+1}=c_n-f(c_n)/f'(c_n)$, le membre de gauche vaut $|f'(c_n)|\,|c_{n+1}-c|$. En le divisant par $|f'(c_n)|\ge i_r$,
$$
\boxed{|c_{n+1}-c|\le K_r|c_n-c|^2.}
$$
En particulier, $|c_{n+1}-c|\le K_rr^2<r$ et $c_{n+1}\in J_r$.

### Question 24

Si $c_0\in J_r$, la suite est bien définie et reste dans $J_r$ par Q23.

Si $K_r=0$, la même estimation donne $c_1=c$, puis $c_n=c$ pour tout $n\ge1$. La borne de l’énoncé, qui divise par $K_r$, concerne le cas $K_r>0$.

Dans ce cas, posons $u_n=K_r|c_n-c|$. Alors $0\le u_0\le rK_r<1$ et $u_{n+1}\le u_n^2$. Par récurrence, $u_n\le u_0^{2^n}$ pour tout $n\ge0$. On obtient
$$
\boxed{|c_n-c|\le\frac{(K_r|c_0-c|)^{2^n}}{K_r}.}
$$
Le membre de droite tend vers zéro, donc $c_n\to c$.

### III.B — Implémentation de Newton

### Question 25

On teste le résidu de $c_0$ avant toute itération, puis celui de chaque nouvel itéré jusqu’à $c_{50}$ inclus. Le retour est déterminé par le seuil indiqué dans l’énoncé.

```python
def newton(c0, f, df):
    c = c0
    for n in range(51):
        try:
            fc = f(c)
            if abs(fc) < 1e-10:
                return c
            if n == 50:
                return None
            pente = df(c)
            if pente == 0:
                return None
            c -= fc / pente
        except (ValueError, ZeroDivisionError, OverflowError):
            return None
```

La division par la pente est possible tant que les itérés restent dans $I$. Le code renvoie aussi `None` si un calcul de l’itération échoue.

## IV — Décomposition de Jordan-Chevalley-Dunford

### IV.A — Une méthode de Newton matricielle

### Question 26

Pour chaque racine $\lambda_i$ de $P$, on a $P'(\lambda_i)=\prod_{j\ne i}(\lambda_i-\lambda_j)\ne0$, puisque les racines de $P$ sont distinctes.

Si $P'(\mu)=0$, alors $\mu$ n’est pas une valeur propre de $M$, d’où l’inversibilité de $M-\mu I_q$.

Si $s=1$, $P'(M)=I_q$.

Sinon, la factorisation de $P'$ sur $\mathbb C$ exprime $P'(M)$ comme un produit d’un scalaire non nul et de facteurs $M-\mu I_q$, tous inversibles. Ainsi $P'(M)$ est inversible.

### Question 27

Dans le polynôme caractéristique, les valeurs propres distinctes sont $\lambda_1,\dots,\lambda_s$ avec des multiplicités $m_i$ positives de somme $q$. Chacune vérifie $m_i\le q$. Ainsi $\chi_M$ divise $P^q$.

D’après le théorème de Cayley-Hamilton, $\chi_M(M)=0$. En évaluant la relation de divisibilité en $M$, on obtient **$P(M)^q=0$**. La matrice $P(M)$ est donc nilpotente.

### Question 28

Soit $n_0\in\mathbb N$ tel que $2^{n_0}\ge q$. Pour $n\ge n_0$, la propriété admise et Q27 donnent
$$
P(M_n)=P(M)^{2^n}B_n=0.
$$
La récurrence matricielle se réduit alors à $M_{n+1}=M_n$. La suite est donc stationnaire à partir du rang $n_0$.

### Question 29

Au rang zéro, $M_0=M$ commute avec $M$.

Si $M_n$ commute avec $M$, alors tout polynôme en $M_n$ commute avec $M$, en particulier $P(M_n)$ et $P'(M_n)$.

Pour une matrice inversible $T$, l’égalité $MT=TM$, multipliée à gauche et à droite par $T^{-1}$, donne $T^{-1}M=MT^{-1}$.

Ainsi $P'(M_n)^{-1}$ commute aussi avec $M$ et la formule de récurrence donne la commutation de $M_{n+1}$ avec $M$.

Le même argument appliqué à $M_nP'(M_n)=P'(M_n)M_n$ justifie que $M_n$ et $P'(M_n)^{-1}$ commutent.

### Question 30

Avec $n_0$ choisi en Q28, $A=M_{n_0}$ et $P(A)=0$.

Le polynôme $P$ est scindé sur $\mathbb C$ à racines simples. Le critère de diagonalisation par un polynôme annulateur montre que **$A$ est diagonalisable sur $\mathbb C$**.

### Question 31

D’après Q29, $A$ commute avec $M$. Elle commute donc avec $N=M-A$. De plus, en sommant les différences consécutives jusqu’au rang de stationnarité fixé en Q28,
$$
N=\sum_{n=0}^{n_0-1}P(M_n)P'(M_n)^{-1}.
$$
La propriété admise donne $P(M_n)=P(M)^{2^n}B_n$. Comme $2^n\ge1$, chaque terme de la somme est un multiple de $P(M)$. Plus précisément,
$$
\begin{aligned}N&=P(M)\,D,\\
D&=\sum_{n=0}^{n_0-1}P(M)^{2^n-1}B_nP'(M_n)^{-1}.\end{aligned}
$$
Les matrices $B_n$ sont des polynômes en $M$. Les matrices $P'(M_n)^{-1}$ commutent avec $M$ d’après la preuve de Q29. Chaque facteur de cette somme commute donc avec $P(M)$.

Il s’ensuit que $D$ commute avec $P(M)$ et que $N^q=P(M)^qD^q=0$. La somme vide vaut zéro si $n_0=0$.

### IV.B — Racine carrée d’une matrice réelle à spectre positif

### Question 32

Prenons pour $R_q$ la partie polynomiale du développement limité de $\sqrt{1+x}$ à l’ordre $q-1$, par exemple
$$
R_q(X)=\sum_{k=0}^{q-1}(-1)^{k+1}b_kX^k
$$
avec les $b_k$ de Q3. Pour $x\to0$, on a $\sqrt{1+x}-R_q(x)=o(x^{q-1})$. En multipliant par $\sqrt{1+x}+R_q(x)$, qui reste borné, on obtient
$$
1+x-R_q(x)^2=o(x^{q-1}).
$$
Un polynôme qui satisfait cette propriété a tous ses coefficients de degrés $0$ à $q-1$ nuls. En effet, s’il avait un premier terme non nul de degré $k<q$, il serait équivalent à ce terme, en contradiction avec le petit $o$. Ainsi **$X^q$ divise $1+X-R_q(X)^2$**.

### Question 33

Si $N$ est nilpotente de taille $q$, toutes ses valeurs propres complexes sont nulles. Son polynôme caractéristique vaut donc $X^q$, et Cayley-Hamilton donne $N^q=0$.

En évaluant en $N$ l’identité de divisibilité de Q32, on obtient $I_q+N-R_q(N)^2=0$. Par conséquent, **$R_q(N)$ est une racine carrée de $I_q+N$**.

### Question 34

Les valeurs propres de $M$ sont réelles, donc $P$ et $P'$ ont des coefficients réels. Partant de $M_0=M$ réelle, la récurrence conserve des coefficients réels.

En effet, l’inverse d’une matrice réelle inversible sur $\mathbb C$ est réel, par unicité de l’inverse après conjugaison complexe. Par stationnarité, $A$ est réelle, et $N=M-A$ aussi.

L’égalité $P(A)=0$ reste valable sur $\mathbb R$. Le polynôme $P$ s’y scinde à racines simples, donc **$A$ est diagonalisable sur $\mathbb R$**.

### Question 35

Si $AX=\mu X$ avec $X\ne0$, alors $P(A)X=P(\mu)X=0$.

Donc $P(\mu)=0$ et $\mu$ est l’une des valeurs propres de $M$. Ainsi **$\mathrm{Sp}(A)\subset\mathbb R_+^*$**.

### Question 36

Diagonaliser $A$ sur $\mathbb R$ donne $A=S\,\mathrm{diag}(a_1,\dots,a_q)S^{-1}$ avec $S$ inversible et $a_i>0$.

Partons de $U_0=I_q$ et itérons $U_{n+1}=(U_n+AU_n^{-1})/2$. Le même calcul qu’en Q18, avec $S^{-1}$ à la place de la transposée orthogonale, donne
$$
U_n=S\,\mathrm{diag}(c_n(a_1),\dots,c_n(a_q))S^{-1}.
$$
Les itérés sont inversibles par Q7 et convergent par Q9 vers
$$
A'=S\,\mathrm{diag}(\sqrt{a_1},\dots,\sqrt{a_q})S^{-1}.
$$
On a $(A')^2=A$. Comme $A$ commute avec $N$, l’identité puis chaque itéré $U_n$ commutent avec $N$, par stabilité de la commutation sous somme, produit et inverse.

Le passage à la limite montre que $A'$ commute avec $N$.

Posons $K=A^{-1}N$. L’inverse existe d’après Q35. Comme $A$ et $N$ commutent et $N^q=0$, on a $K^q=A^{-q}N^q=0$.

La matrice $A'$ commute avec $A^{-1}$ car elle commute avec son propre carré $A$. Elle commute donc avec $K$ et avec $R_q(K)$. Le résultat de Q33 donne finalement
$$
\begin{aligned}\bigl(A'R_q(K)\bigr)^2&=A\,R_q(K)^2\\
&=A(I_q+K)\\&=A+N=M.\end{aligned}
$$
Une racine carrée réelle de $M$ est donc **$A'R_q(A^{-1}N)$**.

FIN
