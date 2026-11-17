# Agrégation Maths — Analyse et probabilités 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Nature de l'épreuve.** Composition d'analyse et de probabilités de l'agrégation externe (session 2026) : 6 heures, calculatrice, téléphones et documents interdits. L'énoncé insiste sur la qualité de la rédaction (« raisonnements clairs, complets et concis ») et autorise à réutiliser les résultats des questions précédentes en citant leur numéro.

**Thème.** Déterminer, pour tout entier $p\ge2$, quels nombres sont sommes finies d'inverses de puissances $p$-ièmes d'entiers naturels distincts — par exemple, pour $p=2$, les rationnels de $]0,\pi^2/6-1[\cup]1,\pi^2/6[$. Le fil directeur aboutit au théorème de Paul Lévy (partie V, loi limite des chiffres de Sylvester d'une uniforme) et au théorème de Ronald Graham (partie VI).

**Découpage.** Six parties, 62 questions. I. développement $p$-adique propre et développement en série de Sylvester (Q1–Q11) ; II. étude de la fonction $T_p$ et de son seuil $t_p$, calcul de $\zeta(2)$ (Q12–Q20) ; III. déterminations du logarithme et application (Q21–Q27) ; IV. ensembles $P_\infty(u)$ de sommes de sous-séries, termes substituables (Q28–Q38) ; V. théorème de Paul Lévy (Q39–Q48) ; VI. théorème de Graham par la méthode de Sprague (Q49–Q62). Les parties I, II, III sont indépendantes ; V ne dépend que de I et III ; IV est un prérequis de VI.

**Notions mobilisées.** Partie entière et suites adjacentes, séries de fonctions (convergence normale, holomorphie), théorème de Cauchy et primitives, déterminations du logarithme, inversion locale holomorphe, transformée de Fourier et lemme de Riemann-Lebesgue, probabilités (loi uniforme, conditionnement, fonctions caractéristiques, théorème de Lévy), algèbre linéaire (trace, matrices par blocs).

**Difficulté et gestion du temps.** I–III sont classiques et accessibles ; IV est technique mais abordable ; V demande de la ténacité sur les estimations (Q43–Q48) ; VI (surtout Q55–Q60) est d'une difficulté arithmétique considérable. Ordre conseillé : traiter I, II, III en entier, puis IV jusqu'à Q36–Q38, puis la mécanique de V (Q39–Q45, puis Q48.e en admettant les estimations intermédiaires), et n'aborder VI qu'une fois le reste sécurisé.

## Partie I — Développement $p$-adique et développement en série de Sylvester

Outils de base : partie entière, suites adjacentes, unicité du développement $p$-adique propre, puis algorithme de Sylvester (suite des restes strictement décroissante, télescopage). Les questions 5, 7.b, 10 et 11 sont les pivots réutilisés en IV et V.

On fixe $p\ge 2$, $x>0$, et les suites $u_n=\lfloor p^nx\rfloor/p^n$, $v_n=u_n+p^{-n}$, $b_0=\lfloor x\rfloor$, $b_n=\lfloor p^nx\rfloor-p\lfloor p^{n-1}x\rfloor$.

### Question 1.a

> [!INDICATION]
> Encadrer $\lfloor p^n x\rfloor$ par deux entiers consécutifs (définition de la partie entière), puis diviser par $p^n$.

#### Solution

Pour tout $n$, $\lfloor p^nx\rfloor\le p^nx<\lfloor p^nx\rfloor+1$. En divisant par $p^n>0$ : $u_n\le x<u_n+p^{-n}=v_n$.

**Pour tout $n\in\mathbb N$ : $u_n\le x<v_n$.** $\square$

### Question 1.b

> [!INDICATION]
> Comparer $\lfloor p^{n+1}x\rfloor$ à $p\lfloor p^n x\rfloor$ pour la croissance de $(u_n)$, et à $p(\lfloor p^n x\rfloor+1)$ pour la décroissance de $(v_n)$.

> [!INDICATION]
> Conclure par le théorème des suites adjacentes, puis passer à la limite dans l'encadrement de 1.a.

#### Solution

Comme $p^{n+1}x\ge p\lfloor p^nx\rfloor$ et $p\lfloor p^nx\rfloor\in\mathbb Z$, on a $\lfloor p^{n+1}x\rfloor\ge p\lfloor p^nx\rfloor$, d'où $u_{n+1}\ge u_n$ : $(u_n)$
croît. De $\lfloor p^{n+1}x\rfloor\le p^{n+1}x<p(\lfloor p^nx\rfloor+1)$ et le membre de droite entier, on tire $\lfloor p^{n+1}x\rfloor+1\le p(\lfloor p^nx\rfloor+1)$, soit $v_{n+1}\le v_n$ : $(v_n)$ décroît. Enfin $v_n-u_n=p^{-n}\to 0$.
Les suites sont adjacentes, de limite commune $\ell$ ; de $u_n\le x<v_n$ et $v_n-u_n\to0$ on tire $\ell=x$.

**Les suites $(u_n)$ et $(v_n)$ sont adjacentes, de limite commune $x$.** $\square$

### Question 2

> [!INDICATION]
> Réutiliser l'encadrement de $\lfloor p^n x\rfloor$ obtenu en 1.b pour encadrer $b_n$.

#### Solution

Les inégalités de 1.b donnent $p\lfloor p^{n-1}x\rfloor\le \lfloor p^nx\rfloor\le p\lfloor p^{n-1}x\rfloor+p-1$, d'où $0\le b_n\le p-1$ ; comme $b_n\in\mathbb Z$, $b_n\in[\![0,p-1]\!]$.

$$
\boxed{b_n\in[\![0,p-1]\!]}
$$
$\square$

### Question 3

> [!INDICATION]
> Écrire $b_n/p^n$ comme une différence $u_n-u_{n-1}$, sommer (télescopage), et utiliser la limite de $(u_n)$.

#### Solution

Pour $n\ge1$, $b_n/p^n=u_n-u_{n-1}$. Donc $\sum_{n=1}^N b_n/p^n=u_N-u_0=u_N-\lfloor x\rfloor$. Les termes étant positifs et $u_N\to x$, la série converge et $\sum_{n\ge1}b_n/p^n=x-\lfloor x\rfloor$, soit $x=\lfloor x\rfloor+\sum_{n\ge1}b_n/p^n$.

$$
\boxed{x=\lfloor x\rfloor+\sum_{n\ge1}\frac{b_n}{p^n}}
$$
$\square$

### Question 4

> [!INDICATION]
> Raisonner par l'absurde : si $(b_n)$ stationnait à $p-1$ à partir d'un rang, que deviendrait la suite $(v_n)$ ? Conclure avec l'inégalité stricte de 1.a.

> [!PIEGE]
> L'inégalité $x<v_n$ de 1.a est stricte : c'est elle qui interdit la stationnarité à $p-1$.

#### Solution

Si $b_n=p-1$ pour tout $n\ge N$, alors $\lfloor p^nx\rfloor+1=p(\lfloor p^{n-1}x\rfloor+1)$, donc $v_n=v_{n-1}$ pour $n>N$
: $(v_n)$ est constante égale à $v_N$ au-delà de $N$. Par passage à la limite $x=v_N$, ce qui contredit $x<v_N$ (Q1.a).

**La suite $(b_n)$ ne stationne pas à la valeur $p-1$.** $\square$

### Question 5

> [!INDICATION]
> Soit $(c_n)$ une autre suite convenable ; pour $m$ fixé, utiliser la non-stationnarité à $p-1$ pour obtenir une inégalité stricte sur la queue $\sum_{n>m}c_n/p^n$, puis reconstruire $\lfloor p^m y\rfloor$ et conclure.

> [!METHODE]
> L'unicité d'un développement propre repose toujours sur la non-stationnarité à la valeur maximale : sans elle, deux écritures coexistent (exemple $0{,}0\overline{(p-1)}=0{,}1\overline{0}$).

#### Solution

Soit $(c_n)_{n\ge1}$ à valeurs dans $[\![0,p-1]\!]$, non stationnaire à $p-1$, avec $y:=x-\lfloor x\rfloor=\sum_{n\ge1}c_n/p^n$. Pour $m$
fixé, comme $(c_n)$ n'est pas constante à $p-1$ au-delà de $m$, il existe $n_0>m$ avec $c_{n_0}\le p-2$,
d'où $\sum_{n>m}c_n/p^n\le p^{-m}-p^{-n_0}<p^{-m}$. Donc $\sum_{k=1}^m c_k/p^k\le y<\sum_{k=1}^m c_k/p^k+p^{-m}$, ce qui donne $\lfloor p^my\rfloor=\sum_{k=1}^m c_kp^{m-k}$. Alors $c_m=\lfloor p^my\rfloor-p\lfloor p^{m-1}y\rfloor=\lfloor p^mx\rfloor-p\lfloor p^{m-1}x\rfloor=b_m$. Avec $c_0=\lfloor x\rfloor$, l'unicité est établie.

**$(b_n)$ est l'unique suite de $[\![0,p-1]\!]$ non stationnaire à $p-1$ telle que $x-\lfloor x\rfloor=\sum c_n/p^n$.** $\square$

### Question 6.a

> [!INDICATION]
> Poser $y_n=\theta_n/b$ et reconnaître l'itération $y\mapsto p(y-\lfloor y\rfloor)$ qui engendre les chiffres $b_n$ ; montrer par récurrence que $y_n=\sum_{k\ge0}b_{n+k}/p^k$.

#### Solution

$\theta_{n+1}/b=p(\theta_n/b-\lfloor\theta_n/b\rfloor)$, soit $y_{n+1}=p(y_n-\lfloor y_n\rfloor)$ avec $y_0=x$. Par récurrence, $y_n=\sum_{k\ge0}b_{n+k}/p^k$ et $\lfloor y_n\rfloor=b_n$.
Pour $n=0$ : $y_0=\lfloor x\rfloor+\sum_{k\ge1}b_k/p^k=\sum_{k\ge0}b_k/p^k$, et $\lfloor y_0\rfloor=\lfloor x\rfloor=b_0$ (partie fractionnaire $<1$ par Q4). Hérédité : $y_{n+1}=p\sum_{k\ge1}b_{n+k}/p^k=\sum_{j\ge0}b_{n+1+j}/p^j$,
de partie entière $b_{n+1}$. Donc $b_n=\lfloor\theta_n/b\rfloor$, et $\theta_n\in\mathbb N$ par récurrence.

**$b_n=\lfloor\theta_n/b\rfloor$ et $\theta_n\in\mathbb N$ pour tout $n$.** $\square$

### Question 6.b

> [!INDICATION]
> ($\Rightarrow$) Si $x=a/b$, majorer les valeurs possibles de $\theta_n$ et en déduire que $(\theta_n)$ est pré-périodique. ($\Leftarrow$) La queue d'une suite pré-périodique est une série géométrique.

#### Solution

($\Rightarrow$) Si $x=a/b$ : $\theta_{n+1}=p(\theta_n\bmod b)\in[\![0,p(b-1)]\!]$, donc $(\theta_n)_{n\ge1}$ prend un nombre fini de valeurs ; comme $\theta_{n+1}$
est fonction de $\theta_n$, la suite est pré-périodique, donc $(b_n)=(\lfloor\theta_n/b\rfloor)$ aussi.
($\Leftarrow$) Si $b_{n+q}=b_n$ pour $n\ge N$, la queue $\sum_{n\ge N}b_n/p^n$ est une série géométrique de raison $p^{-q}$, donc rationnelle, et $x\in\mathbb Q$.

$$
\boxed{x\in\mathbb Q\iff (b_n)\text{ est pré-périodique}}
$$
$\square$

### Question 7.a

> [!INDICATION]
> Étudier le signe de $s_{n+1}-s_n$ et le minorer par $1$ ; en déduire une minoration de $s_n$.

#### Solution

$s_{n+1}-s_n=(s_n-1)^2\ge0$ et, par récurrence, $s_n\ge2>1$ (si $s_n\ge2$, $s_{n+1}=s_n(s_n-1)+1\ge3$). De plus $s_{n+1}-s_n=(s_n-1)^2\ge1$, donc $s_n\ge n+1\to+\infty$.

**$s_n\ge n+1$ pour tout $n$, donc $s_n\to+\infty$.** $\square$

### Question 7.b

> [!INDICATION]
> Trouver une relation entre $s_{n+1}-1$ et $s_n(s_n-1)$, l'écrire comme une différence télescopante, puis sommer.

> [!METHODE]
> L'identité $\frac1{s_n}=\frac1{s_n-1}-\frac1{s_{n+1}-1}$ resservira en IV (Q34) et V (Q43).

#### Solution

Comme $s_{n+1}-1=s_n(s_n-1)$, on a $\dfrac1{s_n}=\dfrac1{s_n-1}-\dfrac1{s_{n+1}-1}$. Donc $\sum_{k=n}^N 1/s_k=\dfrac1{s_n-1}-\dfrac1{s_{N+1}-1}\to\dfrac1{s_n-1}$ puisque $s_N\to\infty$.

$$
\boxed{\sum_{k\ge n}\frac1{s_k}=\frac1{s_n-1}}
$$
$\square$

### Question 8.a

> [!INDICATION]
> Montrer par récurrence que $x_n>0$ entraîne $1/q_n<x_n$ puis $0<x_{n+1}<x_n$, avec $q_n=\lfloor1/x_n\rfloor+1$.

#### Solution

Si $x_n>0$, alors $q_n:=\lfloor 1/x_n\rfloor+1\ge1$ et $1/x_n<q_n$, donc $1/q_n<x_n$, d'où $x_{n+1}=x_n-1/q_n\in\,]0,x_n[$. Avec $x_1=x>0$, la suite est bien définie et strictement positive.

**$0<x_{n+1}<x_n$ : la suite $(x_n)$ est bien définie et strictement positive.** $\square$

### Question 8.b

> [!INDICATION]
> Pour $q_n\ge2$, utiliser $x_n\le 1/(q_n-1)$ pour minorer $1/x_{n+1}$, puis la croissance de la partie entière.

#### Solution

$q_n\ge1>0$. Si $q_n\ge2$ : $\lfloor1/x_n\rfloor=q_n-1\le1/x_n$ donne $x_n\le1/(q_n-1)$, donc $x_{n+1}=x_n-1/q_n\le\frac1{q_n-1}-\frac1{q_n}=\frac1{q_n(q_n-1)}$,
soit $1/x_{n+1}\ge q_n(q_n-1)$ (inégalité triviale si $q_n=1$). Comme $q_n(q_n-1)\in\mathbb Z$, $\lfloor1/x_{n+1}\rfloor\ge q_n(q_n-1)$, d'où $q_{n+1}\ge q_n^2-q_n+1$.

$$
\boxed{q_{n+1}\ge q_n^2-q_n+1}
$$
$\square$

### Question 8.c

> [!INDICATION]
> Télescoper $x_{n+1}=x-\sum_{k\le n}1/q_k$ ; traiter d'abord la phase où $x_n>1$ (alors $q_n=1$), puis utiliser 8.b pour montrer $x_n\to0$.

#### Solution

$\sum_{k=1}^n 1/q_k=x-x_{n+1}$. Tant que $x_n>1$, $q_n=1$ et $x_{n+1}=x_n-1$ : après un nombre fini d'étapes $x_n\le1$,
donc $q_n\ge2$ ; alors $q_{n+1}\ge q_n(q_n-1)+1\ge q_n+1\to\infty$, et $0<x_{n+1}\le 1/(q_n(q_n-1))\to0$. Ainsi $x=\sum_{n\ge1}1/q_n$.

$$
\boxed{x=\sum_{n\ge1}\frac1{q_n}}
$$
$\square$

### Question 9.a

> [!INDICATION]
> Vérifier que $r_n\ge2$ (sinon $x>1$), puis déduire de la récurrence une inégalité entre $1/(r_{n+1}-1)$ et $1/(r_n-1)-1/r_n$.

#### Solution

Si $r_n=1$ pour un $n$, alors $x\ge 1/r_n+\text{(termes}>0)>1$, absurde ; donc $r_n\ge2$. De $r_{n+1}\ge r_n(r_n-1)+1$
on tire $r_{n+1}-1\ge r_n(r_n-1)$, d'où $\frac1{r_{n+1}-1}\le\frac1{r_n-1}-\frac1{r_n}$, soit $\frac1{r_n}\le\frac1{r_n-1}-\frac1{r_{n+1}-1}$.

$$
\boxed{r_n\ge2\text{ et }\frac1{r_n}\le\frac1{r_n-1}-\frac1{r_{n+1}-1}}
$$
$\square$

### Question 9.b

> [!INDICATION]
> Somme télescopique des inégalités de 9.a pour encadrer $x=\sum 1/r_n$, puis encadrer $1/x$ pour reconnaître la partie entière.

#### Solution

En sommant, $x=\sum_{n\ge1}1/r_n\le 1/(r_1-1)$ (car $r_n\to\infty$). D'autre part $x>1/r_1$. Donc $r_1-1\le 1/x<r_1$, soit $\lfloor1/x\rfloor=r_1-1$, c'est-à-dire $r_1=\lfloor1/x\rfloor+1$.

$$
\boxed{r_1=\lfloor1/x\rfloor+1}
$$
$\square$

### Question 10

> [!INDICATION]
> Existence : la suite $(q_n)$ de 8 convient (8.b, 8.c). Unicité : descendre sur la partie entière (traiter le cas $x>1$ à part), puis appliquer 9.b et une récurrence.

> [!PIEGE]
> Traiter d'abord la phase $x>1$ (chiffres égaux à $1$) avant d'appliquer 9.b, qui suppose $x\le1$.

#### Solution

*Existence :* $(q_n)$ de Q8 vérifie $q_{n+1}\ge q_n^2-q_n+1$ (Q8.b) et $x=\sum1/q_n$ (Q8.c).
*Unicité :* soit $(r_n)$ convenant. Si $x>1$, on ne peut avoir $r_1\ge2$ (sinon tous les $r_n\ge2$ et $x\le1/(r_1-1)\le1$)
: donc $r_1=1$ est forcé, et $(r_{n+1})$ convient pour $x-1$ ; par descente finie on se ramène à $x\le1$. Pour $x\le1$,
Q9.b impose $r_1=\lfloor1/x\rfloor+1$, puis $(r_{n+1})$ est la suite de $x-1/r_1$ ; par récurrence $r_n=q_n$.

**Existence et unicité de la suite de Sylvester de $x$.** $\square$

### Question 11.a

> [!INDICATION]
> Si la récurrence est exacte au-delà d'un rang $N$, appliquer l'identité de 7.b à la queue $\sum_{n\ge N}1/r_n$.

#### Solution

Si $r_{n+1}=r_n^2-r_n+1$ pour $n\ge N$, avec $r_N\ge2$ (sinon série divergente), le calcul de Q7.b s'applique : $\sum_{n\ge N}1/r_n=1/(r_N-1)\in\mathbb Q$, donc $x=\sum_{n<N}1/r_n+1/(r_N-1)\in\mathbb Q$.

**Si $r_{n+1}=r_n^2-r_n+1$ pour tout $n\ge N$, alors $x\in\mathbb Q$.** $\square$

### Question 11.b

> [!INDICATION]
> Suivre le numérateur de $x_n$ écrit sous forme irréductible : montrer qu'il décroît strictement jusqu'à valoir $1$, après quoi la récurrence devient exacte.

#### Solution

On peut supposer $x\in\,]0,1[$ (après la phase $x>1$). Écrivons $x_n=a_n/b_n$ irréductible, $q_n=\lfloor b_n/a_n\rfloor+1$. Le numérateur de $x_{n+1}=\frac{a_nq_n-b_n}{b_nq_n}$
vaut $a_nq_n-b_n\in[1,a_n]$ ; si $a_n\ge2$, l'égalité $a_nq_n-b_n=a_n$ exigerait $a_n\mid b_n$ (exclu) : donc le numérateur réduit décroît strictement. Au bout d'un nombre fini d'étapes $a_N=1$,
i.e. $x_N=1/b_N$ ; alors $q_N=b_N+1$ et $x_{N+1}=1/(b_N(b_N+1))=1/(q_N-1)q_N$, d'où $q_{N+1}=q_N^2-q_N+1$ et $x_{N+1}=1/(q_{N+1}-1)$
: la structure se reproduit. Donc $q_{n+1}=q_n^2-q_n+1$ pour $n\ge N$, et par unicité (Q10) $(r_n)=(q_n)$ vérifie la récurrence exacte au-delà de $N$.

**x\in\mathbb Q\iff\exists N,\ \forall n\ge N,\ r_{n+1}=r_n^2-r_n+1** $\square$

## Partie II — Estimations préliminaires

Étude de la série $T_p$, de son seuil $t_p$ (existence, unicité, équivalent $t_p\sim p/\ln2$), prolongement holomorphe $G_p$, transformée de Fourier de $F_p$,
et calcul de $\zeta(2)$ par comparaison avec $(\pi/\sin\pi z)^2$.

$T_p(x)=\sum_{n\ge1}\big(\tfrac{x}{x+n}\big)^p$, $x\ge0$, $p\ge2$.

### Question 12.a

> [!INDICATION]
> Convergence normale sur tout segment $[0,A]$ : majorer uniformément le terme général par le terme d'une série de Riemann convergente, et conclure par continuité.

#### Solution

Sur $[0,A]$, $0\le \tfrac{x}{x+n}\le\tfrac{A}{A+n}\le \tfrac An$, donc $\big(\tfrac{x}{x+n}\big)^p\le (A/n)^p$, terme général d'une série convergente ($p\ge2$). La convergence est normale sur $[0,A]$
; les termes étant continus, $T_p$ est continue sur $[0,A]$, donc sur $[0,+\infty[$.

**$T_p$ est définie et continue sur $[0,+\infty[$.** $\square$

### Question 12.b

> [!INDICATION]
> Chaque terme $x\mapsto(x/(x+n))^p$ est strictement croissante ; sommer.

#### Solution

Chaque $x\mapsto (x/(x+n))^p$ est strictement croissante sur $[0,+\infty[$, donc $T_p$ est **strictement croissante**.

**$T_p$ est strictement croissante sur $[0,+\infty[$.** $\square$

### Question 12.c

> [!INDICATION]
> Pour $N$ fixé, minorer $T_p(x)$ par sa somme partielle de rang $N$, puis faire tendre $x\to+\infty$.

#### Solution

Pour $N$ fixé, $\liminf_{x\to\infty}T_p(x)\ge\lim_{x\to\infty}\sum_{n=1}^N(x/(x+n))^p=N$. Donc $T_p(x)\to+\infty$.

**$T_p(x)\to+\infty$ quand $x\to+\infty$.** $\square$

### Question 12.d

> [!INDICATION]
> Comparaison série/intégrale avec la fonction décroissante $t\mapsto(x/(x+t))^p$ : encadrer la somme par $\int_1^\infty$ et $\int_0^\infty$, et calculer les deux intégrales.

> [!METHODE]
> Pour une fonction positive décroissante, la comparaison série/intégrale encadre toujours la somme entre $\int_1^\infty f$ et $\int_0^\infty f$.

#### Solution

Avec $f(t)=(x/(x+t))^p$ décroissante positive : $\int_1^\infty f<\sum_{n\ge1}f(n)<\int_0^\infty f$. Or $\int_0^\infty \frac{x^p}{(x+t)^p}dt=\frac{x}{p-1}$ et $\int_1^\infty=\frac{x^p}{(p-1)(x+1)^{p-1}}$. D'où $\frac{x^p}{(p-1)(x+1)^{p-1}}<T_p(x)<\frac x{p-1}$.

$$
\boxed{\frac{x^p}{(p-1)(x+1)^{p-1}}<T_p(x)<\frac{x}{p-1}}
$$
$\square$

### Question 13.a

> [!INDICATION]
> Théorème des valeurs intermédiaires + stricte monotonie (12.b, 12.c) pour l'existence et l'unicité.

#### Solution

$T_p$ continue strictement croissante, $T_p(0)=0$, $T_p\to+\infty$ : par le TVI et la stricte monotonie, il existe un unique $t_p$ avec $T_p(t_p)=1$.

**Il existe un unique réel $t_p\ge0$ tel que $T_p(t_p)=1$.** $\square$

### Question 13.b

> [!INDICATION]
> Appliquer la majoration de 12.d en $x=t_p$.

#### Solution

$1=T_p(t_p)<t_p/(p-1)$ (Q12.d), donc $t_p>p-1$.

$$
\boxed{t_p>p-1}
$$
$\square$

### Question 13.c

> [!INDICATION]
> Minorer $T_2(2)$ par une intégrale (sans utiliser $\zeta(2)$, non encore connu), puis conclure par croissance de $T_2$.

> [!PIEGE]
> Ne pas utiliser $\zeta(2)=\pi^2/6$ ici : il n'est pas encore établi ; minorer par une intégrale.

#### Solution

$T_2(2)=4\sum_{m\ge3}1/m^2>4\int_3^\infty dt/t^2=4/3>1=T_2(t_2)$. Par croissance, $t_2<2$.

$$
\boxed{t_2<2}
$$
$\square$

### Question 13.d

> [!INDICATION]
> Pour $m=\lfloor t_p\rfloor$, minorer $T_p(m)$ par une série géométrique grâce à l'inégalité de Bernoulli $(1+1/m)^n\ge1+n/m$ ; exploiter $T_p(m)\le1$.

#### Solution

Soit $m=\lfloor t_p\rfloor\ge1$ (car $t_p>p-1\ge1$). Comme $(1+1/m)^n\ge1+n/m$, on a $(1+n/m)^{-p}\ge(1+1/m)^{-pn}$, d'où, avec $r=(1+1/m)^{-p}$,

$$
T_p(m)=\sum_{n\ge1}(1+n/m)^{-p}>\sum_{n\ge1}r^n=\frac r{1-r}
$$

(inégalité stricte grâce aux termes $n\ge2$). Or $m\le t_p$ donne $T_p(m)\le1$. Donc $r/(1-r)<1$, soit $r<1/2$,
i.e. $(1+1/m)^p>2$, d'où $m<\dfrac1{2^{1/p}-1}$.

$$
\boxed{\lfloor t_p\rfloor<\frac1{2^{1/p}-1}}
$$
$\square$

### Question 14.a

> [!INDICATION]
> Pour $x>0$, chaque base $x/(x+n)$ est dans $]0,1[$ : le terme général décroît strictement en $p$.

#### Solution

Pour $x>0$, chaque base $x/(x+n)\in\,]0,1[$, donc $p\mapsto (x/(x+n))^p$ est strictement décroissante ; par sommation, $(T_p(x))_p$ est strictement décroissante.

**Pour $x>0$ fixé, la suite $(T_p(x))_{p\ge2}$ est strictement décroissante.** $\square$

### Question 14.b

> [!INDICATION]
> Évaluer $T_{p+1}(t_p)$ par décroissance en $p$ (14.a), puis conclure par stricte croissance de $T_{p+1}$.

#### Solution

$T_{p+1}(t_p)<T_p(t_p)=1=T_{p+1}(t_{p+1})$ (Q14.a), et $T_{p+1}$ strictement croissante donne $t_p<t_{p+1}$.

$$
\boxed{t_p<t_{p+1}}
$$
$\square$

### Question 15

> [!INDICATION]
> Étudier les variations de $p\mapsto p\ln(1+t/p)$ en posant $u=t/p$ et en dérivant deux fois la fonction auxiliaire.

#### Solution

$g'(p)=\ln(1+u)-\frac u{1+u}$ avec $u=t/p>0$ ; or $h(u)=\ln(1+u)-\frac u{1+u}$ vérifie $h(0)=0$, $h'(u)=\frac u{(1+u)^2}>0$,
donc $g'>0$. Ainsi $(1+t/p)^p$ croît en $p$, et $(1+t/p)^{-p}$ décroît.

**Pour $t>0$ fixé, la suite $p\mapsto(1+t/p)^{-p}$ est décroissante.** $\square$

### Question 16.a

> [!INDICATION]
> Calcul direct : réécrire chaque terme de $T_p(px)$.

#### Solution

$T_p(px)=\sum_{n\ge1}\big(\tfrac{px}{px+n}\big)^p=\sum_{n\ge1}(1+\tfrac n{px})^{-p}=\sum_n g_n(p)$.

$$
\boxed{T_p(px)=\sum_{n\ge1}\Big(1+\frac{n}{px}\Big)^{-p}}
$$
$\square$

### Question 16.b

> [!INDICATION]
> Convergence dominée sur la mesure de comptage : limite simple $e^{-n/x}$, et domination uniforme en $p$ par le terme en $p=2$ grâce à 15 ; sommer la série géométrique.

> [!METHODE]
> Pour la limite d'une série dépendant d'un paramètre, penser convergence dominée sur la mesure de comptage, avec une domination uniforme obtenue par monotonie en le paramètre (question 15).

#### Solution

$g_n(p)=(1+\tfrac{n/x}p)^{-p}\to e^{-n/x}$. Par Q15 (avec $t=n/x$), $g_n(p)\le g_n(2)=(1+\tfrac n{2x})^{-2}\le 4x^2/n^2$, sommable. Le théorème de convergence dominée donne $T_p(px)\to\sum_n e^{-n/x}=\dfrac{e^{-1/x}}{1-e^{-1/x}}=\dfrac1{e^{1/x}-1}$.

$$
\boxed{\lim_{p\to+\infty}T_p(px)=\frac1{e^{1/x}-1}}
$$
$\square$

### Question 17

> [!INDICATION]
> La fonction $x\mapsto1/(e^{1/x}-1)$ est strictement croissante et vaut $1$ en $1/\ln2$ ; encadrer $t_p/p$ par $1/\ln2\pm\varepsilon$ en appliquant 16.b puis la croissance de $T_p$.

#### Solution

$\ell$ est strictement croissante et $\ell(1/\ln2)=1$. Soit $\varepsilon>0$, $x_\pm=1/\ln2\pm\varepsilon$ ; $\ell(x_-)<1<\ell(x_+)$.
Par Q16.b, pour $p$ grand, $T_p(px_-)<1<T_p(px_+)$, donc (croissance de $T_p$) $px_-<t_p<px_+$. Ainsi $t_p/p\to1/\ln2$, soit $t_p\sim p/\ln2$.

$$
\boxed{t_p\sim\frac{p}{\ln2}}
$$
$\square$

### Question 18

> [!INDICATION]
> Convergence normale sur tout compact de $\mathbb C\setminus\{-n\}$ : pour $n$ assez grand, $|z+n|\ge n/2$ sur le compact ; conclure par stabilité de l'holomorphie.

#### Solution

Sur un compact $K\subset\mathbb C\setminus\{-k\}$, $|z|\le R$ ; pour $n\ge 2R$, $|z+n|\ge n/2$, donc $|(z/(z+n))^p|\le (2R/n)^p$,
sommable. La série converge normalement sur $K$ ; chaque terme étant holomorphe, $G_p$ est holomorphe sur $\mathbb C\setminus\{-k;k\in\mathbb N^*\}$.

**$G_p$ est holomorphe sur $\mathbb C\setminus\{-n:n\in\mathbb N^*\}$.** $\square$

### Question 19.a

> [!INDICATION]
> Vérifier l'intégrabilité en $0^+$ (équivalent en $t^{p-2}$) et en $+\infty$ (équivalent en $t^{p-1}e^{-t}$).

#### Solution

$F_p$ est $C^\infty$ sur $]0,\infty[$ et nulle sur $]-\infty,0]$ ; en $0^+$,
$F_p(t)\sim t^{p-2}$ (limite finie, $=1$ si $p=2$), donc continue par morceaux. En $+\infty$, $F_p(t)\sim t^{p-1}e^{-t}$ : intégrable. Donc $F_p\in L^1(\mathbb R)$.

**$F_p\in L^1(\mathbb R)$.** $\square$

### Question 19.b

> [!INDICATION]
> Domination par $F_p\in L^1$ (19.a).

#### Solution

$|F_p(t)e^{-ixt}|=F_p(t)\in L^1$, donc $\mathcal F(F_p)(x)=\int_0^\infty\frac{t^{p-1}}{e^t-1}e^{-ixt}dt$ est défini pour tout $x\in\mathbb R$.

**$\mathcal F(F_p)(x)$ est définie pour tout $x\in\mathbb R$.** $\square$

### Question 19.c

> [!INDICATION]
> Développer $1/(e^t-1)=\sum_{n\ge1}e^{-nt}$ et intervertir somme et intégrale (Tonelli) ; calculer $\int_0^\infty t^{p-1}e^{-\alpha t}dt$ pour $\Re\alpha>0$.

#### Solution

Pour $t>0$, $\frac1{e^t-1}=\sum_{n\ge1}e^{-nt}$. Comme $\sum_n\int_0^\infty t^{p-1}e^{-nt}dt=\sum_n (p-1)!/n^p<\infty$, l'interversion est licite :

$$
\mathcal F(F_p)(x)=\sum_{n\ge1}\int_0^\infty t^{p-1}e^{-(n+ix)t}dt=(p-1)!\sum_{n\ge1}\frac1{(n+ix)^p}.
$$

(On a utilisé $\int_0^\infty t^{p-1}e^{-\alpha t}dt=(p-1)!/\alpha^p$ pour $\Re\alpha>0$.) Multipliant par $(ix)^p/(p-1)!$ :

$$
\boxed{\frac{(ix)^p}{(p-1)!}\mathcal F(F_p)(x)=\sum_{n\ge1}\Big(\frac{ix}{ix+n}\Big)^p=G_p(ix).}
$$
$\square$

### Question 19.d

> [!INDICATION]
> Une intégration par parties avec $\phi(t)=t/(e^t-1)$ (vérifier $\phi(0^+)=1$) ; le reste est $o(1/x)$ par Riemann-Lebesgue. Relier à $G_2(ix)$ par 19.c.

#### Solution

Avec $\phi(t)=t/(e^t-1)$, $\phi(0^+)=1$, $\phi,\phi'\in L^1(0,\infty)$ : une IPP donne

$$
\mathcal F(F_2)(x)=\frac{\phi(0^+)}{ix}+\frac1{ix}\int_0^\infty\phi'(t)e^{-ixt}dt=-\frac ix+o(1/x)
$$

(dernier terme $o(1)$ par Riemann–Lebesgue). Or $G_2(ix)=-x^2\mathcal F(F_2)(x)\sim -x^2\cdot(-i/x)=ix$.

$$
\boxed{G_2(ix)\sim ix\quad(x\to\pm\infty)}
$$
$\square$

### Question 19.e

> [!INDICATION]
> Itérer les intégrations par parties ($p-1$ fois) : repérer, grâce au comportement de $F_p$ en $0^+$, le seul terme de bord qui survit.

> [!PIEGE]
> Dans les intégrations par parties itérées, repérer quel terme de bord survit grâce au comportement de $F_p$ en $0^+$ ($F_p(t)\sim t^{p-2}$).

#### Solution

Soit $g=F_p$, de classe $C^\infty$ sur $[0,\infty[$ avec $g^{(j)}(0)=0$ pour $j\le p-3$
et $g^{(p-2)}(0)=(p-2)!$ (car $g(t)=t^{p-2}(1+O(t))$), toutes les dérivées étant intégrables et nulles en $+\infty$. Après $(p-1)$ IPP,

$$
\begin{aligned}
\mathcal F(F_p)(x) \\
&= \sum_{j=0}^{p-2}\frac{g^{(j)}(0)}{(ix)^{j+1}}+\frac1{(ix)^{p-1}}\int_0^\infty g^{(p-1)}(t)e^{-ixt}dt \\
&= \frac{(p-2)!}{(ix)^{p-1}}+o\Big(\frac1{|x|^{p-1}}\Big).
\end{aligned}
$$

Donc $G_p(ix)=\frac{(ix)^p}{(p-1)!}\cdot\frac{(p-2)!}{(ix)^{p-1}}(1+o(1))=\dfrac{ix}{p-1}(1+o(1))$.

$$
\boxed{G_p(ix)\sim\frac{ix}{p-1}\quad(x\to\pm\infty)}
$$
$\square$

### Question 20.a

> [!INDICATION]
> Réécrire $G_2(z)/z^2$ et $G_2(-z)/z^2$ pour faire apparaître la somme sur $\mathbb Z$ ; localiser les pôles et les parties principales.

#### Solution

$G_2(z)/z^2=\sum_{n\ge1}1/(z+n)^2$ et $G_2(-z)/z^2=\sum_{n\ge1}1/(z-n)^2$, donc

$$
H(z)=\frac1{z^2}+\sum_{n\ge1}\frac1{(z+n)^2}+\sum_{n\ge1}\frac1{(z-n)^2}=\sum_{n\in\mathbb Z}\frac1{(z+n)^2}.
$$

Les singularités (pôles doubles aux entiers) sont isolées ; $H$ est méromorphe sur $\mathbb C$.

$$
\boxed{H(z)=\sum_{n\in\mathbb Z}\frac1{(z+n)^2},\text{ méromorphe sur }\mathbb C}
$$
$\square$

### Question 20.b

> [!INDICATION]
> Réindexer la série (convergence absolue) pour faire apparaître la périodicité.

#### Solution

La série $\sum_{\mathbb Z}1/(z+n)^2$ étant absolument convergente, un réindexage donne $H(z+1)=\sum_n 1/(z+1+n)^2=H(z)$.

**$H$ est $1$-périodique.** $\square$

### Question 20.c

> [!INDICATION]
> Comparer $H$ à $z\mapsto(\pi/\sin\pi z)^2$ : mêmes pôles doubles et mêmes parties principales, donc la différence est entière ; la rendre bornée sur une bande verticale (périodicité + Liouville).

> [!METHODE]
> Deux fonctions méromorphes ayant mêmes pôles et mêmes parties principales diffèrent d'une fonction entière : rendre cette différence bornée (bande verticale + périodicité) pour appliquer Liouville.

#### Solution

Près de $0$ : $H(z)=1/z^2+O(1)$ et $\Phi(z)=1/z^2+O(1)$ ; par $1$-périodicité, $D=H-\Phi$
se prolonge en fonction **entière** $1$-périodique. Sur la bande $0\le\Re z\le1$, $|H(z)|\le\sum_n1/|z+n|^2\to0$ et $\Phi(z)\to0$ quand $|\Im z|\to\infty$
: $D$ est bornée sur la bande, donc sur $\mathbb C$. Par Liouville $D$ est constante, et $D\to0$ à l'infini donne $D\equiv0$. Ainsi $H(z)=(\pi/\sin\pi z)^2$.

$$
\boxed{H(z)=\Big(\frac{\pi}{\sin\pi z}\Big)^2}
$$
$\square$

### Question 20.d

> [!INDICATION]
> Développer $H(z)-1/z^2$ en $0$ d'un côté, $(\pi/\sin\pi z)^2-1/z^2$ de l'autre, et identifier.

#### Solution

$H(z)-1/z^2\to 2\sum_{n\ge1}1/n^2=2\zeta(2)$ quand $z\to0$. Par ailleurs $\sin^2\pi z=\pi^2z^2(1-\tfrac{\pi^2z^2}3+o(z^2))$, donc $(\pi/\sin\pi z)^2=\tfrac1{z^2}+\tfrac{\pi^2}3+o(1)$, d'où $(\pi/\sin\pi z)^2-1/z^2\to\pi^2/3$.
Par Q20.c, $2\zeta(2)=\pi^2/3$, soit $\displaystyle\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}6$.

$$
\boxed{\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}{6}}
$$
$\square$

## Partie III — Déterminations du logarithme

Déterminations du logarithme : unicité à $2i\pi\mathbb Z$ près sur un connexe, caractérisation par la dérivée $1/z$, exemples explicites ($\Omega_1$, $\Omega_2$, $\mathbb C\setminus\mathbb R_-$), impossibilité sur $\mathbb C^*$, et préparation du théorème central limite de la partie V (Q27.c).

### Question 21

> [!INDICATION]
> $\exp(\varphi_1-\varphi_2)=1$ : que vaut $(\varphi_1-\varphi_2)/(2i\pi)$ ? Utiliser la connexité de $\Omega$ pour conclure que c'est une constante entière.

> [!PIEGE]
> Sans la connexité de $\Omega$, la constante $k$ pourrait changer d'une composante à l'autre.

#### Solution

$e^{\varphi_1-\varphi_2}=1$ donne $(\varphi_1-\varphi_2)/(2i\pi)$ continue à valeurs dans $\mathbb Z$ ; $\Omega$ connexe ⇒ cette fonction est constante. Donc $\varphi_1-\varphi_2=2i k\pi$, $k\in\mathbb Z$.

$$
\boxed{\varphi_1-\varphi_2=2ik\pi,\ k\in\mathbb Z}
$$
$\square$

### Question 22

> [!INDICATION]
> Dériver $z\mapsto z\,e^{-f(z)}$ ; en déduire que $f$ diffère d'une détermination du logarithme d'une constante.

> [!METHODE]
> Le lemme $g'=0$ sur un connexe, avec $g=ze^{-f(z)}$, sert trois fois dans cette partie (23.b, 24.c, 26).

#### Solution

$g(z)=ze^{-f(z)}$ vérifie $g'=e^{-f}(1-zf')=0$, donc $g\equiv a$ sur $\Omega$ connexe, avec $a\ne0$.
Écrivant $a=e^{-c}$, on a $z=e^{f(z)-c}$ ; donc $f-c$ (et à renommage près $f+c'$) est une détermination du logarithme.

**$f-c$ est une détermination du logarithme sur $\Omega$.** $\square$

### Question 23.a

> [!INDICATION]
> Rayon de convergence de la série entière defining $f_1$ ; vérifier que $|1-z|<1$ sur $\Omega_1$.

#### Solution

$\sum w^n/n$ a pour rayon $1$ ; sur $\Omega_1=\{|z-1|<1\}$, $w=1-z$ vérifie $|w|<1$,
donc $f_1$ est définie et holomorphe sur $\Omega_1$.

**$f_1$ est définie et holomorphe sur $\Omega_1$.** $\square$

### Question 23.b

> [!INDICATION]
> Calculer $f_1'$ (série géométrique), reconnaître $1/z$, puis fixer la constante par $f_1(1)=0$ via le lemme de 22.

#### Solution

$f_1'(z)=\sum_{n\ge1}(1-z)^{n-1}=\dfrac1{1-(1-z)}=\dfrac1z$. Posant $g(z)=ze^{-f_1(z)}$, on a $g'=0$ et $g(1)=e^{-f_1(1)}=e^0=1$, donc $g\equiv1$,
soit $e^{f_1(z)}=z$ : $f_1$ est une détermination du logarithme sur $\Omega_1$.

$$
\boxed{e^{f_1(z)}=z\text{ pour tout }z\in\Omega_1}
$$
$\square$

### Question 24.a

> [!INDICATION]
> Montrer que $|z-1|<|z+1|$ équivaut à $\Re z>0$ (comparer les carrés) ; la série en $w=(z-1)/(z+1)$ a pour rayon 1.

#### Solution

Pour $\Re z>0$, $|z-1|<|z+1|$ (car $|z+1|^2-|z-1|^2=4\Re z$), donc $w=(z-1)/(z+1)$ vérifie $|w|<1$
; la série $\sum\frac2{2n+1}w^{2n+1}$ (rayon $1$) converge, et $z\mapsto w(z)$ est holomorphe sur $\Omega_2$. Donc $f_2$ est définie et holomorphe sur $\Omega_2$.

**$f_2$ est définie et holomorphe sur $\Omega_2$.** $\square$

### Question 24.b

> [!INDICATION]
> Pour $x>0$, poser $w=(x-1)/(x+1)$ et reconnaître le développement de $\ln\frac{1+w}{1-w}$ en série impaire.

#### Solution

Pour $x>0$, $w=(x-1)/(x+1)\in\,]-1,1[$ et $\frac{1+w}{1-w}=x$ ; or $\ln\frac{1+w}{1-w}=2\sum_{n\ge0}\frac{w^{2n+1}}{2n+1}=f_2(x)$, donc $f_2(x)=\ln x$.

$$
\boxed{f_2(x)=\ln x\quad(x>0)}
$$
$\square$

### Question 24.c

> [!INDICATION]
> Calculer $f_2'$ en sommant une série géométrique, reconnaître $1/z$, et conclure comme en 23.b.

#### Solution

$f_2'(z)=2w'(z)\sum_{n\ge0}w^{2n}=\frac{2w'(z)}{1-w^2}$. Avec $w'=\frac2{(z+1)^2}$ et $1-w^2=\frac{4z}{(z+1)^2}$, on obtient $f_2'(z)=1/z$. Posant $g(z)=ze^{-f_2(z)}$
: $g'=0$, $g(1)=e^{-f_2(1)}=e^{-\ln1}=1$, donc $e^{f_2(z)}=z$ : $f_2$ est une détermination du logarithme sur $\Omega_2$.

$$
\boxed{f_2'(z)=\frac1z\text{ et }e^{f_2(z)}=z\text{ sur }\Omega_2}
$$
$\square$

### Question 25.a

> [!INDICATION]
> Cas particulier de 25.b lorsque $\exp\circ f$ est holomorphe.

#### Solution

Cas particulier de 25.b avec $\exp\circ f=\mathrm{id}$ (holomorphe).

**Si $\exp\circ f$ est holomorphe, alors $f$ est holomorphe (cas particulier de 25.b).** $\square$

### Question 25.b

> [!INDICATION]
> Inversion locale holomorphe de $\exp$ (sa dérivée ne s'annule pas) : écrire $f$ localement comme composée de fonctions holomorphes.

#### Solution

Soit $z_0\in\Omega$, $w_0=f(z_0)$. Comme $\exp'(w_0)=e^{w_0}\ne0$, $\exp$ est un biholomorphisme d'un voisinage $V$
de $w_0$ sur un voisinage $W$ de $e^{w_0}$, d'inverse holomorphe $L$. Par continuité de $f$,
pour $z$ voisin de $z_0$, $f(z)\in V$ et $\exp(f(z))=(\exp\circ f)(z)\in W$, donc $f(z)=L\big((\exp\circ f)(z)\big)$ : composée de fonctions holomorphes. Ainsi $f$ est holomorphe.

**$f$ est holomorphe sur $\Omega$.** $\square$

### Question 26.a

> [!INDICATION]
> Montrer que $\mathbb C\setminus D$ est étoilé par rapport à un point du rayon opposé, donc simplement connexe ; $1/z$ y admet une primitive (théorème de Cauchy), et 22 conclut.

#### Solution

$\Omega=\mathbb C\setminus D$ ($D=\{re^{i\theta_0}:r\ge0\}$) est étoilé par rapport à tout point $-se^{i\theta_0}$ ($s>0$), donc simplement connexe et ne contenant pas $0$.
La fonction $1/z$ y est holomorphe et admet une primitive $f$ (théorème de Cauchy). Par Q22, $f+c$ est une détermination du logarithme sur $\Omega$.

**Il existe une détermination du logarithme sur $\mathbb C\setminus D$.** $\square$

### Question 26.b

> [!INDICATION]
> Fixer la constante par la valeur en $1$ ; l'unicité vient de 21.

#### Solution

Par 26.a (avec $D=\mathbb R_-$), il existe une détermination $f$ sur $\mathbb C\setminus\mathbb R_-$ (connexe). Comme $f(1)\in 2i\pi\mathbb Z$, $\mathrm{Log}:=f-f(1)$
s'annule en $1$ ; l'unicité résulte de Q21 (deux déterminations diffèrent d'une constante $2ik\pi$, fixée par la valeur en $1$).

**Unicité de la détermination principale $\mathrm{Log}$ sur $\mathbb C\setminus\mathbb R_-$.** $\square$

### Question 26.c

> [!INDICATION]
> Comparer $g(z)=-\sum_{n\ge1}z^n/n$ et $\mathrm{Log}(1-z)$ sur le disque unité : mêmes valeur et dérivée en $0$, ouvert connexe.

#### Solution

Pour $|z|<1$, $\Re(1-z)>0$, donc $1-z\in\mathbb C\setminus\mathbb R_-$. Posons $g(z)=-\sum_{n\ge1}z^n/n$ et $h(z)=\mathrm{Log}(1-z)$
: $g(0)=h(0)=0$, $g'(z)=-\frac1{1-z}=h'(z)$ (car $\mathrm{Log}'(w)=1/w$). Sur le disque connexe, $g=h$ : $\mathrm{Log}(1-z)=-\sum_{n\ge1}z^n/n$.

$$
\boxed{\mathrm{Log}(1-z)=-\sum_{n\ge1}\frac{z^n}{n}\quad(|z|<1)}
$$
$\square$

### Question 26.d

> [!INDICATION]
> Si une détermination existait sur $\mathbb C^*$, elle serait holomorphe de dérivée $1/z$ (25.b), donc primitive de $1/z$ ; contredire avec l'intégrale sur le cercle unité.

> [!METHODE]
> Sur un ouvert $\Omega$, une détermination du logarithme est une primitive holomorphe de $1/z$ (après 25.b) : l'obstruction est topologique (intégrale sur un lacet).

#### Solution

Si $f$ était une détermination sur $\mathbb C^*$, elle serait holomorphe (Q25) de dérivée $1/z$, donc primitive de $1/z$ sur $\mathbb C^*$.
Alors $\oint_{|z|=1}dz/z=0$, contredisant $\oint_{|z|=1}dz/z=2i\pi$. Donc aucune détermination n'existe sur $\mathbb C\setminus\{0\}$.

**Il n'existe aucune détermination du logarithme sur $\mathbb C^*$.** $\square$

### Question 27.a

> [!INDICATION]
> Condition d'intégrabilité en $+\infty$ : écrire le module de l'intégrande comme une puissance de $t$.

#### Solution

$|e^{iz\ln t}/t^2|=t^{-\Im z-2}$, intégrable sur $[1,\infty[$ ssi $\Im z>-1$. Donc $\psi$ est définie sur $\Omega_3$.

**$\psi$ est définie sur l'ouvert $\{\Im z>-1\}$.** $\square$

### Question 27.b

> [!INDICATION]
> Changement de variable $t=e^s$ dans l'intégrale.

#### Solution

Avec $t=e^s$ : $\psi(z)=\int_0^\infty e^{(iz-1)s}ds=\dfrac1{1-iz}$ (car $\Re(iz-1)=-\Im z-1<0$).

$$
\boxed{\psi(z)=\frac1{1-iz}}
$$
$\square$

### Question 27.c

> [!INDICATION]
> Appliquer 27.b à $z/\sqrt n$, puis développer $\mathrm{Log}(1-iz/\sqrt n)$ à l'ordre $2$ pour compenser le terme $-iz\sqrt n$.

#### Solution

Pour $n$ grand, $\psi(z/\sqrt n)=(1-iz/\sqrt n)^{-1}$, donc, en prenant la détermination principale,

$$
\ln\!\Big[(\psi(z/\sqrt n))^n e^{-iz\sqrt n}\Big]=-n\,\mathrm{Log}\big(1-\tfrac{iz}{\sqrt n}\big)-iz\sqrt n.
$$

Or $\mathrm{Log}(1-\tfrac{iz}{\sqrt n})=-\tfrac{iz}{\sqrt n}+\tfrac{z^2}{2n}+o(1/n)$, d'où $-n\,\mathrm{Log}(\cdots)-iz\sqrt n=-z^2/2+o(1)$. Donc $(\psi(z/\sqrt n))^n e^{-iz\sqrt n}\to e^{-z^2/2}$.

$$
\boxed{\big(\psi(z/\sqrt n)\big)^n e^{-iz\sqrt n}\to e^{-z^2/2}}
$$
$\square$

## Partie IV — Sommes de fractions unitaires

Ensembles $P_\infty(u)=\{\sum\varepsilon_nu_n\}$ : structure de segment, d'ensemble fini ou d'ensemble de Cantor selon la suite $u$ ; le rôle décisif revient aux termes substituables ($u_n\le\sum_{k>n}u_k$), et le lien avec le seuil $t_p$ de la partie II (Q36–Q38).

### Question 28.a

> [!INDICATION]
> Majorer $\sum\varepsilon_nu_n$ par $\sum u_n<+\infty$ (série convergente à termes positifs).

#### Solution

Pour $\varepsilon\in\{0,1\}^{\mathbb N^*}$, $0\le\sum\varepsilon_nu_n\le\sum u_n<\infty$ : chaque somme converge, donc $P_\infty(u)$ est bien défini.

**$P_\infty(u)$ est bien défini.** $\square$

### Question 28.b

> [!INDICATION]
> Reconnaître les écritures binaires des entiers entre $0$ et $2^p-1$.

#### Solution

$u$ est à support fini donc $u\in\ell^+$. $P_\infty(u)=\{\sum_{n=1}^p\varepsilon_n2^{n-1}\}=[\![0,2^p-1]\!]$ (représentation binaire).

$$
\boxed{P_\infty(u)=[\![0,2^p-1]\!]}
$$
$\square$

### Question 29

> [!INDICATION]
> Si $u$ est à support fini, $P_\infty(u)$ est fini (28.b). Réciproquement, si une infinité de $u_n$ sont non nuls, exhiber une infinité de valeurs distinctes de $P_\infty(u)$ (les $u_n$ eux-mêmes).

#### Solution

Si $u$ est à support fini, $P_\infty(u)$ est fini. Réciproquement, si $u$ a une infinité de termes non nuls, comme $\sum u_n<\infty$ chaque valeur positive n'apparaît qu'un nombre fini de fois ; il y a donc une infinité de valeurs positives distinctes $u_n$,
toutes dans $P_\infty(u)$, qui est alors infini. **Conclusion :** $P_\infty(u)$ fini $\iff$ $u$ à support fini.

$$
\boxed{P_\infty(u)\text{ fini}\iff u\text{ est à support fini}}
$$
$\square$

### Question 30

> [!INDICATION]
> Les développements binaires des réels de $[0,1]$ décrivent exactement le segment $[0,1]$.

#### Solution

$\sum a/2^n=a<\infty$. $P_\infty(u)=a\{\sum\varepsilon_n/2^n\}=a[0,1]=[0,a]$ (développements binaires de $[0,1]$).

$$
\boxed{P_\infty(u)=[0,a]}
$$
$\square$

### Question 31.a

> [!INDICATION]
> Série géométrique de raison $1/p<1$.

#### Solution

$\sum1/p^n=1/(p-1)<\infty$, donc $u\in\ell^+$.

**$u\in\ell^+$.** $\square$

### Question 31.b

> [!INDICATION]
> Séparer selon $\varepsilon_1=0$ ou $1$ et calculer les deux bornes de $K(S)$.

#### Solution

$K(S)=[0,\tfrac1{p(p-1)}]\cup[\tfrac1p,\tfrac1{p-1}]$. Si $\varepsilon_1=0$, $x=\sum_{n\ge2}\varepsilon_n/p^n\in[0,\tfrac1{p(p-1)}]$ ; si $\varepsilon_1=1$, $x\in[\tfrac1p,\tfrac1{p-1}]$. Donc $P_\infty(u)\subset K(S)$.

$$
\boxed{P_\infty(u)\subset\Big[0,\tfrac1{p(p-1)}\Big]\cup\Big[\tfrac1p,\tfrac1{p-1}\Big]}
$$
$\square$

### Question 31.c

> [!INDICATION]
> Itérer le procédé de 31.b : selon $(\varepsilon_1,\varepsilon_2)$, $x$ tombe dans l'un des quatre segments ; vérifier qu'ils sont disjoints ($p\ge3$).

#### Solution

En itérant : selon $(\varepsilon_1,\varepsilon_2)$, $x$ appartient à l'un des **quatre** segments de longueur $\frac1{p^2(p-1)}$, de bornes gauches $0,\ \tfrac1{p^2},\ \tfrac1p,\ \tfrac1p+\tfrac1{p^2}$. Ils sont disjoints car $p-1>1$.
Le segment est $[\,c,\,c+\tfrac1{p^2(p-1)}\,]$ avec $c=\varepsilon_1/p+\varepsilon_2/p^2$.

**$K(K(S))$ est la réunion de quatre segments disjoints de longueur $\frac1{p^2(p-1)}$, de bornes gauches $0,\frac1{p^2},\frac1p,\frac1p+\frac1{p^2}$.** $\square$

### Question 31.d

> [!INDICATION]
> Décrire $S_n$ par récurrence (segments indexés par les $n-1$ premiers chiffres), puis faire la double inclusion.

#### Solution

Par récurrence, $S_n=\bigsqcup_{(\varepsilon_1,\dots,\varepsilon_{n-1})}[\,c,\,c+\lambda_n\,]$ avec $c=\sum_{k=1}^{n-1}\varepsilon_k/p^k$ et $\lambda_n=\frac1{p^{n-1}(p-1)}$ (l'hérédité vient de $K([c,c+\lambda])=[c,c+\lambda/p]\cup[c+1/p^n,\dots]$). D'où :
- $\subseteq$ : $P_\infty(u)\subset S_n$ pour tout $n$ (argument des chiffres), donc $P_\infty(u)\subset\bigcap_n S_n$.
- $\supseteq$ : si $y\in\bigcap_n S_n$, les segments emboîtés déterminent une suite $(\varepsilon_k)$ avec $|y-\sum_{k<n}\varepsilon_k/p^k|\le\lambda_n\to0$, donc $y=\sum\varepsilon_k/p^k\in P_\infty(u)$.

Ainsi $P_\infty(u)=\bigcap_{n}S_n$.

$$
\boxed{P_\infty(u)=\bigcap_{n\ge1}S_n\text{ (ensemble de Cantor)}}
$$
$\square$

### Question 32.a

> [!INDICATION]
> Comparer $1/p^{\lfloor n\alpha\rfloor}$ et $1/p^n$ ; si $\alpha=a/b\in\mathbb Q$, utiliser la périodicité de $\lfloor(n+b)\alpha\rfloor-\lfloor n\alpha\rfloor$ et 6.b.

#### Solution

$\lfloor n\alpha\rfloor\ge n$ ($\alpha>1$), donc $1/p^{\lfloor n\alpha\rfloor}\le 1/p^n$ : $\beta$ existe. Si $\alpha=a/b\in\mathbb Q$,
$\lfloor(n+b)\alpha\rfloor=\lfloor n\alpha\rfloor+a$, donc la suite des chiffres $d_m=\mathbb 1_{m\in E}$ ($E=\{\lfloor n\alpha\rfloor\}$) vérifie $d_{m+a}=d_m$ pour $m$ grand : pré-périodique, donc $\beta\in\mathbb Q$ (Q6.b).

**$\beta$ existe, et si $\alpha\in\mathbb Q$ alors $\beta\in\mathbb Q$.** $\square$

### Question 32.b

> [!INDICATION]
> Le pas $1/\alpha$ est dans $]0,1[$ : deux parties entières consécutives diffèrent d'au plus 1.

#### Solution

$\lfloor(n+1)/\alpha\rfloor-\lfloor n/\alpha\rfloor\in\{0,1\}$ car le pas $1/\alpha\in\,]0,1[$ ($\alpha>1$).

$$
\boxed{\lfloor\tfrac{n+1}\alpha\rfloor-\lfloor\tfrac n\alpha\rfloor\in\{0,1\}}
$$
$\square$

### Question 32.c

> [!INDICATION]
> Montrer que $n\in E\iff\beta_n=1$ en passant par un entier $k$ tel que $n<k\alpha<n+1$ ($\alpha$ irrationnel), puis conclure par unicité du développement (5).

> [!PIEGE]
> L'irrationalité de $\alpha$ sert à éviter les égalités $k\alpha\in\mathbb Z$ dans le passage par les parties entières.

#### Solution

$\alpha$ irrationnel : $k\alpha\notin\mathbb Z$, donc $n\in E\iff\exists k:\ n<k\alpha<n+1\iff\exists k:\ n/\alpha<k\le(n+1)/\alpha\iff\beta_n=1$. Comme $\beta=\sum_{m\ge1}d_m/p^m$ avec $d_m\in\{0,1\}$
non stationnaire à $p-1$ (car $p\ge3$), $\beta_n$ est, par unicité (Q5), le $n$-ième chiffre de $\beta$ en base $p$.

**$\beta_n$ est le $n$-ième chiffre de $\beta$ en base $p$.** $\square$

### Question 32.d

> [!INDICATION]
> Si $\beta$ était rationnel, ses chiffres seraient pré-périodiques (6.b) ; obtenir une contradiction avec l'irrationalité de $\alpha$.

#### Solution

$\beta=\sum_{n\in E}1/p^n\in P_\infty(u)$. Si $(\beta_n)$ était pré-périodique, $\lfloor n/\alpha\rfloor=cn/q+O(1)$ donnerait $1/\alpha\in\mathbb Q$, absurde. Donc $\beta\notin\mathbb Q$
(Q6.b) : $\beta$ est un irrationnel de $P_\infty(u)$.

**$\beta\notin\mathbb Q$ et $\beta\in P_\infty(u)$.** $\square$

### Question 33

> [!INDICATION]
> Rationnels : les valeurs $u_n=1/m_n$ elles-mêmes, en infinité. Irrationnels : extraire une sous-suite super-décroissante ($u_{n_k}>\sum_{j>k}u_{n_j}$) pour rendre $\varepsilon\mapsto\sum\varepsilon_ku_{n_k}$ injective, donc $P_\infty(u)$ indénombrable.

#### Solution

$u_n=1/m_n$, $m_n\in\mathbb N^*$. *Rationnels :* les valeurs $u_n$ (rationnelles), en nombre infini de valeurs distinctes (car $u_n\to0$), appartiennent à $P_\infty(u)$ : infinité de rationnels.
*Irrationnels :* on extrait $(u_{n_k})$ super-décroissante, i.e. $u_{n_k}>\sum_{j>k}u_{n_j}$ (possible car les queues $\sum_{n\ge N}u_n\to0$). Pour une telle sous-suite, $\varepsilon\mapsto\sum_k\varepsilon_k u_{n_k}$ (autres indices nuls) est injective, donc $P_\infty(u)$
est indénombrable. Comme $\mathbb Q$ est dénombrable, $P_\infty(u)$ contient une infinité (même indénombrable) d'irrationnels.

**$P_\infty(u)$ contient une infinité de rationnels et un ensemble indénombrable d'irrationnels.** $\square$

### Question 34.a

> [!INDICATION]
> Identité télescopante de 7.b.

#### Solution

$\sum1/s_n=1/(s_1-1)=1$ (Q7.b), donc $u\in\ell^+$ et $\sigma=1$.

$$
\boxed{\sigma=\sum_{n\ge1}\frac1{s_n}=1}
$$
$\square$

### Question 34.b

> [!INDICATION]
> Si deux suites $(\varepsilon_n)$ donnent le même $x$, soit $m$ le premier indice où elles diffèrent ; minorer l'écart grâce à la queue $\sum_{k>m}1/s_k=1/(s_{m+1}-1)$ et conclure.

> [!PIEGE]
> Ne pas oublier de vérifier que la queue $\sum_{k>m}1/s_k$ vaut exactement $1/(s_{m+1}-1)$, ce qui force $s_m=2$.

#### Solution

Si $\sum\varepsilon_n/s_n=\sum\varepsilon'_n/s_n$ avec $\varepsilon\ne\varepsilon'$, soit $m$ le premier indice de différence ($\varepsilon_m=1,\varepsilon'_m=0$). Alors $1/s_m\le\sum_{k>m}1/s_k=1/(s_{m+1}-1)=1/(s_m(s_m-1))$,
d'où $s_m-1\le1$, soit $s_m=2$, i.e. $m=1$. Il faut alors $\varepsilon=(1,0,0,\dots)$ et $\varepsilon'=(0,1,1,\dots)$,
donnant $x=1/2$. Donc **seul $x=1/2$** a une représentation non unique ; tout autre élément a une unique suite $(\varepsilon_n)$.

$$
\boxed{x=\frac12\text{ est le seul élément de }P_\infty(u)\text{ à représentation non unique}}
$$
$\square$

### Question 34.c

> [!INDICATION]
> ($\Leftarrow$) Une suite stationnaire donne une somme finie ou une queue géométrique. ($\Rightarrow$) Relier $x$ à sa suite de Sylvester et appliquer 10–11.

#### Solution

($\Leftarrow$) Si $(\varepsilon_n)$ stationne (à $0$ : somme finie ; à $1$ : queue $\sum_{n\ge N}1/s_n=1/(s_N-1)$), alors $x\in\mathbb Q$.
($\Rightarrow$) Supposons $(\varepsilon_n)$ non stationnaire ; alors $A=\{n:\varepsilon_n=1\}$ et son complémentaire sont infinis. Avec $A=\{n_1<n_2<\dots\}$, la suite $(s_{n_j})_j$
vérifie $s_{n_{j+1}}\ge s_{n_j+1}=s_{n_j}^2-s_{n_j}+1$, donc c'est, par unicité (Q10), la suite de Sylvester de $x=\sum_j1/s_{n_j}\le1$. Par Q11, $x\in\mathbb Q$ ⟺ $s_{n_{j+1}}=s_{n_j}^2-s_{n_j}+1=s_{n_j+1}$ pour $j$
grand, i.e. $n_{j+1}=n_j+1$ : $(\varepsilon_n)$ stationnerait à $1$, exclu. Donc $x\notin\mathbb Q$. **Conclusion :** rationnel ⟺ stationnaire.

$$
\boxed{x\in\mathbb Q\iff(\varepsilon_n)\text{ stationne}}
$$
$\square$

### Question 35.a

> [!INDICATION]
> Les suites $(\varepsilon_n)$ constante égale à $0$, puis à $1$.

#### Solution

$0\in P_\infty(u)$ ($\varepsilon=0$) et $\sigma\in P_\infty(u)$ ($\varepsilon$ tout à $1$).

$$
\boxed{0,\sigma\in P_\infty(u)}
$$
$\square$

### Question 35.b

> [!INDICATION]
> Par l'absurde dans les deux cas, en utilisant $u_n\to0$ et la définition de $\sigma$.

#### Solution

Si $\varepsilon\equiv0$ : $u_{n+1}>x$ pour tout $n$, contredisant $u_n\to0$. Si $\varepsilon\equiv1$
: $\sum_{k\le n+1}u_k\le x$ pour tout $n$, donc $\sigma\le x<\sigma$, absurde. Donc $(\varepsilon_n)$ n'est pas constante.

**La suite $(\varepsilon_n)$ n'est pas constante.** $\square$

### Question 35.c

> [!INDICATION]
> Supposer $\varepsilon_n=1$ pour $n\ge N$ avec $\varepsilon_{N-1}=0$ ; contredire la substituabilité de $u_{N-1}$.

#### Solution

Par construction, toutes les sommes partielles $\sum_{k\le n}\varepsilon_ku_k\le x$. Supposons $\varepsilon_n=1$ pour $n\ge N$ (avec $N\ge2$, $\varepsilon_{N-1}=0$)
; soit $s=\sum_{k<N}\varepsilon_ku_k$. Alors $\varepsilon_{N-1}=0$ donne $s+u_{N-1}>x$, tandis que $x\ge s+\sum_{k\ge N}u_k$. Or $u_{N-1}$
substituable : $u_{N-1}\le\sum_{k\ge N}u_k$, d'où $s+u_{N-1}\le x$, contradiction. Donc $(\varepsilon_n)$ ne stationne pas à $1$.

**La suite $(\varepsilon_n)$ ne stationne pas à $1$.** $\square$

### Question 35.d

> [!INDICATION]
> Soit $y=\sum\varepsilon_nu_n\le x$ ; par 35.c il existe une infinité d'indices $n$ avec $\varepsilon_n=0$ et $\sum_{k<n}\varepsilon_ku_k+u_n>x$ ; passer à la limite le long de ces indices pour obtenir $y\ge x$.

> [!METHODE]
> Question pivot de la partie IV : la densité des sommes partielles vient des indices où $\varepsilon_n=0$ ; elle se réutilise en 36, 37, 38.

#### Solution

Soit $y=\sum\varepsilon_nu_n\le x$. Par 35.c, il y a une infinité d'indices $n$ avec $\varepsilon_n=0$, pour lesquels $\sum_{k<n}\varepsilon_ku_k+u_n>x$. En faisant $n\to\infty$
le long de ces indices, $y+0\ge x$, donc $y\ge x$, puis $y=x$. Avec les bornes (35.a) et l'inclusion évidente $P_\infty(u)\subseteq[0,\sigma]$, on conclut $P_\infty(u)=[0,\sigma]$.

$$
\boxed{P_\infty(u)=[0,\sigma]}
$$
$\square$

### Question 36.a

> [!INDICATION]
> Série de Riemann convergente ; sa somme est $\zeta(2)=\pi^2/6$ (20.d).

#### Solution

$\sum1/n^2$ converge, $u\in\ell^+$, $\sigma=\pi^2/6$.

$$
\boxed{\sigma=\frac{\pi^2}{6}}
$$
$\square$

### Question 36.b

> [!INDICATION]
> Comparer la queue $\sum_{k>n}1/k^2$ à l'intégrale $\int_{n+1}^\infty dt/t^2$.

#### Solution

Pour $n\ge2$ : $\sum_{k>n}1/k^2>\int_{n+1}^\infty dt/t^2=1/(n+1)\ge1/n^2$ (car $n^2\ge n+1$). Donc $u_n$ est substituable.

**$u_n$ est substituable pour tout $n\ge2$ (et non pour $n=1$).** $\square$

### Question 36.c

> [!INDICATION]
> Appliquer 35 à la queue $(1/n^2)_{n\ge2}$ (tous substituables), puis translater de $1$ selon $\varepsilon_1$ ; vérifier que les deux segments sont disjoints.

#### Solution

Pour $\varepsilon_1=0$, Q35 appliquée à $(1/n^2)_{n\ge2}$ (tous substituables) donne $[0,\pi^2/6-1]$ ; pour $\varepsilon_1=1$, on translate de $1$
: $[1,\pi^2/6]$. Comme $\pi^2/6-1<1$, ils sont disjoints :

$$
\boxed{P_\infty(u)=\Big[0,\tfrac{\pi^2}6-1\Big]\cup\Big[1,\tfrac{\pi^2}6\Big].}
$$
$\square$

### Question 37.a

> [!INDICATION]
> Série de Riemann convergente, de somme $\zeta(3)$.

#### Solution

$\sum1/n^3$ converge, $u\in\ell^+$, $\sigma=\zeta(3)$.

$$
\boxed{\sigma=\zeta(3)}
$$
$\square$

### Question 37.b

> [!INDICATION]
> Séparer les deux premiers termes de $T_3(x)$ et minorer la queue par une intégrale (fonction décroissante).

#### Solution

$T_3(x)=\frac{x^3}{(x+1)^3}+\frac{x^3}{(x+2)^3}+\sum_{n\ge3}\frac{x^3}{(x+n)^3}$, et $\sum_{n\ge3}\frac1{(x+n)^3}>\int_3^\infty\frac{dt}{(x+t)^3}=\frac1{2(x+3)^2}$ (fonction décroissante). D'où l'inégalité.

$$
\boxed{T_3(x)\ge\frac{x^3}{(x+1)^3}+\frac{x^3}{(x+2)^3}+\frac{x^3}{2(x+3)^2}}
$$
$\square$

### Question 37.c

> [!INDICATION]
> Évaluer la minoration de 37.b en $x=3$, comparer à $T_3(t_3)=1$, et conclure avec 13.b.

#### Solution

Avec $x=3$ : $T_3(3)\ge\frac{27}{64}+\frac{27}{125}+\frac{27}{72}=1{,}0129\dots>1=T_3(t_3)$, donc $t_3<3$ (croissance).

$$
\boxed{t_3<3\text{, donc }\lfloor t_3\rfloor=2}
$$
$\square$

### Question 37.d

> [!INDICATION]
> Un terme $u_n$ est substituable si et seulement si $T_3(n)\ge1$, c'est-à-dire $n\ge t_3$ ; appliquer 35 à la queue $(n\ge3)$ et ajouter les quatre choix de la tête $(\varepsilon_1,\varepsilon_2)$.

#### Solution

$u_n$ substituable ⟺ $1\le n^3\sum_{k>n}1/k^3=T_3(n)$ ⟺ $n\ge t_3$. Comme $\lfloor t_3\rfloor=2$, les termes $n=1,2$
sont libres, les termes $n\ge3$ substituables. Par Q35, $\{\sum_{n\ge3}\varepsilon_n/n^3\}=[0,\rho]$ avec $\rho=\zeta-9/8$. En ajoutant $\varepsilon_1\cdot1+\varepsilon_2/8$ (4 choix, sommes distinctes) :

$$
P_\infty(u)=[0,\zeta-\tfrac98]\cup[\tfrac18,\zeta-1]\cup[1,\zeta-\tfrac18]\cup[\tfrac98,\zeta],
$$

quatre segments disjoints (car $\zeta-9/8\approx0{,}077<1/8$, etc.).

$$
\boxed{P_\infty(u)=[0,\zeta-\tfrac98]\cup[\tfrac18,\zeta-1]\cup[1,\zeta-\tfrac18]\cup[\tfrac98,\zeta]}
$$
$\square$

### Question 38.a

> [!INDICATION]
> Série de Riemann convergente ($p\ge2$).

#### Solution

$\sum1/n^p$ converge ($p\ge2$) : $u\in\ell^+$.

**$u\in\ell^+$.** $\square$

### Question 38.b

> [!INDICATION]
> Même caractérisation par $T_p(n)\ge1$ ; en déduire que les termes non substituables sont les $n\le N_p$ avec $N_p=\lceil t_p\rceil-1$.

#### Solution

$u_n$ substituable ⟺ $T_p(n)\ge1$ ⟺ $n\ge t_p$. Les termes non substituables sont les $n<t_p$, soit $[\![1,N_p]\!]$
avec $N_p=\lceil t_p\rceil-1\ge1$ (car $t_p>1$). D'où l'existence et l'unicité de $N_p$.

$$
\boxed{N_p=\lceil t_p\rceil-1}
$$
$\square$

### Question 38.c

> [!INDICATION]
> Utiliser l'équivalent $t_p\sim p/\ln2$ (17).

#### Solution

$N_p=\lceil t_p\rceil-1=t_p+O(1)$ et $t_p\sim p/\ln2$ (Q17), donc $N_p\sim p/\ln2$.

$$
\boxed{N_p\sim\frac{p}{\ln2}}
$$
$\square$

### Question 38.d

> [!INDICATION]
> Surjectivité par définition de $P_{N_p}$ ; injectivité par le premier indice de différence et la non-substituabilité de cet indice.

#### Solution

La surjectivité est la définition. Pour l'injectivité, si $\sum\varepsilon_k/k^p=\sum\varepsilon'_k/k^p$ avec $\varepsilon\ne\varepsilon'$, soit $m$ le plus petit indice de différence ($\varepsilon_m=1,\varepsilon'_m=0$) : alors $1/m^p\le\sum_{m<k\le N_p}1/k^p\le\sum_{k>m}1/k^p<1/m^p$
(non-substituabilité de $m\le N_p$), absurde. Donc l'application est bijective de $\{0,1\}^{N_p}$ sur $P_{N_p}$.

**L'application $(\varepsilon_k)\mapsto\sum_{k\le N_p}\varepsilon_k/k^p$ est bijective de $\{0,1\}^{N_p}$ sur $P_{N_p}$.** $\square$

### Question 38.e

> [!INDICATION]
> Queue substituable (35) + tête bijective (38.d) : $P_\infty(u)$ est la réunion des segments $[\omega,\omega+\rho_p]$ ; les disjoindre par non-substituabilité du premier indice de différence.

> [!METHODE]
> Structure générale : tête finie bijective + queue substituable = réunion de segments deux à deux disjoints. C'est exactement la définition de $U_p$ en partie VI.

#### Solution

La queue $(1/k^p)_{k>N_p}$ est substituable, donc $\{\sum_{k>N_p}\varepsilon_k/k^p\}=[0,\rho_p]$ (Q35). Ainsi $P_\infty(u)=\{\omega+t:\omega\in P_{N_p},t\in[0,\rho_p]\}=\bigcup_\omega[\omega,\omega+\rho_p]$. Pour $\omega<\omega'$ distincts, en notant $m$ le plus petit indice où leurs chiffres diffèrent ($m\le N_p$),

$$
\begin{aligned}
\omega'-\omega \\
&\ge \frac1{m^p}-\sum_{m<k\le N_p}\frac1{k^p}>\sum_{k>N_p}\frac1{k^p} \\
&= \rho_p,
\end{aligned}
$$

(car $m$ non substituable), donc $\omega+\rho_p<\omega'$ : les segments sont **deux à deux disjoints**.

$$
\boxed{P_\infty(u)=\bigsqcup_{\omega\in P_{N_p}}[\omega,\omega+\rho_p]\text{ (segments deux à deux disjoints)}}
$$
$\square$

## Partie V — Un théorème de Paul Lévy sur les séries de Sylvester

La suite de Sylvester $Q_n$ d'une variable uniforme : loi jointe des chiffres (propriété de Markov, Q43–Q44), décroissance géométrique de $I_n=\sum P_n(k)/k$ (Q45), factorisation des fonctions caractéristiques (Q47), estimations (Q48.a–Q48.d) et théorème de Lévy (Q48.e).

### Question 39

> [!INDICATION]
> Modifier $V$ sur l'ensemble négligeable $\{V=0\}$.

#### Solution

Soit $V\sim\mathcal U[0,1]$. Posons $U=V$ si $V>0$, $U=1$ si $V=0$.
Comme $\mathbb P(V=0)=0$, $U=V$ p.s., donc $U\sim\mathcal U[0,1]$, mesurable, avec $U(\omega)\in\,]0,1]$ pour tout $\omega$.

**Il existe $U\sim\mathcal U[0,1]$ telle que $U(\omega)\in\,]0,1]$ pour tout $\omega$.** $\square$

### Question 40

> [!INDICATION]
> Les restes $x_n$ de l'algorithme de Sylvester sont des fonctions mesurables de $U$ (récurrence), donc $Q_n=\lfloor1/x_n\rfloor+1$ aussi.

#### Solution

Comme $U\in\,]0,1]$, la suite de Sylvester de $U$ est $(q_n(U))$ (Q8–Q10). Les restes $x_{n+1}=x_n-1/(\lfloor1/x_n\rfloor+1)$ sont des fonctions mesurables de $U$
(par récurrence), donc $Q_n=\lfloor1/x_n\rfloor+1$ est une variable aléatoire (à valeurs entières $\ge2$).

**$Q_n$ est une variable aléatoire pour tout $n\in\mathbb N^*$.** $\square$

### Question 41

> [!INDICATION]
> Récurrence sur $n$, en utilisant la croissance de $t\mapsto t^2-t+1$ sur $[1,+\infty[$.

#### Solution

$(s_1,\dots,s_n)\in C_n$ par définition de $(s_n)$. Pour $(k_i)\in C_n$ : $k_1\ge2=s_1$, et comme $t\mapsto t^2-t+1$
croît pour $t\ge1$, $k_i\ge s_i$ entraîne $k_{i+1}\ge k_i^2-k_i+1\ge s_i^2-s_i+1=s_{i+1}$. Donc $k_i\ge s_i$ pour tout $i$.

**$(s_1,\dots,s_n)\in C_n$ et c'est, coordonnée par coordonnée, le plus petit élément de $C_n$.** $\square$

### Question 42

> [!INDICATION]
> Appliquer 9.b à $U$, puis à $U-1/k_1$ sur l'événement $\{Q_1=k_1\}$ ; vérifier l'emboîtement des intervalles grâce à $(k_1,k_2)\in C_2$.

#### Solution

$Q_1=k\iff\lfloor1/U\rfloor=k-1\iff 1/k<U\le1/(k-1)$ (Q9.b). Pour le couple : sur $\{Q_1=k_1\}$, la suite $(Q_2,\dots)$ est celle de $U-1/k_1$, donc $Q_2=k_2\iff \tfrac1{k_1}+\tfrac1{k_2}<U\le\tfrac1{k_1}+\tfrac1{k_2-1}$
; la condition $(k_1,k_2)\in C_2$ ($k_2\ge k_1^2-k_1+1$) assure que cet intervalle est inclus dans $]\tfrac1{k_1},\tfrac1{k_1-1}]$, d'où l'égalité d'événements.

**Les deux égalités d'événements demandées.** $\square$

### Question 43

> [!INDICATION]
> Récurrence : $\{Q_1=k_1,\dots,Q_n=k_n\}=\{a_n<U\le b_n\}$ avec $a_n=\sum_{i\le n}1/k_i$ et $b_n=\sum_{i<n}1/k_i+1/(k_n-1)$ ; conclure par la loi uniforme.

> [!METHODE]
> Avec une loi uniforme, tout événement $\{a<U\le b\}$ a pour probabilité $b-a$ : c'est toute la mécanique de la partie V.

#### Solution

Par récurrence, $\{Q_1=k_1,\dots,Q_n=k_n\}=\{a_n<U\le b_n\}$ avec $a_n=\sum_{i\le n}1/k_i$, $b_n=\sum_{i<n}1/k_i+1/(k_n-1)$ (l'emboîtement $(a_n,b_n]\subset(a_{n-1},b_{n-1}]$ résulte de $k_n\ge k_{n-1}^2-k_{n-1}+1$). Comme $U\sim\mathcal U[0,1]$,

$$
\begin{aligned}
\mathbb P(Q_1=k_1,\dots,Q_n=k_n) \\
&= b_n-a_n \\
&= \frac1{k_n-1}-\frac1{k_n} \\
&= \frac1{k_n(k_n-1)}.\
\end{aligned}
$$

**\mathbb P(Q_1=k_1,\dots,Q_n=k_n)=\frac1{k_n(k_n-1)}** $\square$

### Question 44

> [!INDICATION]
> Somme des probabilités de 43 sur tous les préfixes valides (ils existent d'après 41) ; le nombre de préfixes se simplifie dans le quotient.

#### Solution

$\mathbb P(Q_{n-1}=j)=\sum_{\text{préfixes valides}}\frac1{j(j-1)}=\frac{A}{j(j-1)}$ (Q43), avec $A\ge1$ préfixes (par Q41, $j\ge s_{n-1}$ garantit l'existence). De même $\mathbb P(Q_{n-1}=j,Q_n=k)=\frac{A}{k(k-1)}$. Donc $\mathbb P(Q_{n-1}=j)>0$ et

$$
\begin{aligned}
\mathbb P(Q_n=k\mid Q_{n-1}=j) \\
&= \frac{A/(k(k-1))}{A/(j(j-1))} \\
&= \frac{j(j-1)}{k(k-1)}.\
\end{aligned}
$$

**\mathbb P(Q_n=k\mid Q_{n-1}=j)=\frac{j(j-1)}{k(k-1)}** $\square$

### Question 45.a

> [!INDICATION]
> Formule des probabilités totales conditionnée par $Q_{n-1}$, puis 44.

#### Solution

Par la formule des probabilités totales et Q44,

$$
\begin{aligned}
P_n(k) \\
&= \sum_{j:\,j^2-j+1\le k}\mathbb P(Q_n=k\mid Q_{n-1}=j)\,P_{n-1}(j) \\
&= \sum_{j\ge2,\,j^2-j+1\le k}\frac{j(j-1)}{k(k-1)}P_{n-1}(j).\
\end{aligned}
$$

$$
\boxed{P_n(k)=\sum_{j\ge2,\ j^2-j+1\le k}\frac{j(j-1)}{k(k-1)}P_{n-1}(j)}
$$
$\square$

### Question 45.b

> [!INDICATION]
> Intervertir les deux sommes (Tonelli) et utiliser la décomposition $\frac1{k^2(k-1)}=\frac1{k(k-1)}-\frac1{k^2}$ avec une minoration de $\sum_{k\ge m}1/k^2$.

#### Solution

$$
\begin{aligned}
\sum_{k\ge2}\frac{P_n(k)}k \\
&= \sum_{j\ge2}j(j-1)P_{n-1}(j)\sum_{k\ge m}\frac1{k^2(k-1)},\quad m \\
&= j^2-j+1.
\end{aligned}
$$

Or $\sum_{k\ge m}\frac1{k^2(k-1)}=\frac1{m-1}-\sum_{k\ge m}\frac1{k^2}<\frac1{m-1}-\frac1m=\frac1{m(m-1)}=\frac1{(j^2-j+1)\,j(j-1)}$. D'où $\displaystyle\sum_{k\ge2}\frac{P_n(k)}k\le\sum_{j\ge2}\frac{P_{n-1}(j)}{j^2-j+1}$.

$$
\boxed{\sum_{k\ge2}\frac{P_n(k)}k\le\sum_{j\ge2}\frac{P_{n-1}(j)}{j^2-j+1}}
$$
$\square$

### Question 45.c

> [!INDICATION]
> Majorer $\frac{j}{j^2-j+1}$ par $\frac23$ pour amorcer une récurrence géométrique sur $I_n=\sum_k P_n(k)/k$ ; calculer $I_1$ explicitement (télescopage + $\zeta(2)$).

> [!PIEGE]
> Calculer explicitement $I_1=\sum_{k\ge2}1/(k^2(k-1))$ (télescopage + $\zeta(2)$) pour amorcer la récurrence géométrique.

#### Solution

Comme $\frac{j}{j^2-j+1}\le\frac23$ pour $j\ge2$, on a $\frac1{j^2-j+1}\le\frac2{3j}$, donc $I_n:=\sum_k P_n(k)/k\le\frac23 I_{n-1}$. Or $P_1(k)=1/(k(k-1))$
donne $I_1=2-\pi^2/6<\frac23$. D'où $I_n\le(\tfrac23)^{n-1}I_1\le(\tfrac23)^n$.

$$
\boxed{I_n=\sum_{k\ge2}\frac{P_n(k)}k\le\Big(\tfrac23\Big)^n}
$$
$\square$

### Question 46

> [!INDICATION]
> Pour $\psi_n$ : convergence absolue car $\sum_{k\ge n^2-n+1}\frac{n(n-1)}{k(k-1)}=1$ (série télescopique) ; pour $\phi_n$ : c'est une espérance de variable de module 1.

#### Solution

$\phi_1,\phi_n$ sont des espérances de variables de module $1$, donc définies sur $\mathbb R$. Pour $\psi_n$ : $\sum_{k\ge n^2-n+1}\frac{n(n-1)}{k(k-1)}=n(n-1)\cdot\frac1{n^2-n}=1$,
donc la série converge absolument et $\psi_n$ est définie (et $|\psi_n|\le1$) sur $\mathbb R$.

**$\phi_1$, $(\phi_n)_{n\ge1}$ et $(\psi_n)_{n\ge2}$ sont des suites de fonctions définies sur $\mathbb R$.** $\square$

### Question 47

> [!INDICATION]
> Partir de 43, décomposer $\ln\frac{k_n}{k_1\cdots k_{n-1}}$, et sommer d'abord sur $k_n\ge k_{n-1}^2-k_{n-1}+1$.

#### Solution

Par Q43, $\phi_n(t)=\sum_{(k_1,\dots,k_n)\in C_n}e^{it\ln(k_n/(k_1\cdots k_{n-1}))}\frac1{k_n(k_n-1)}$. En écrivant $\ln\frac{k_n}{k_1\cdots k_{n-1}}=\ln\frac{k_{n-1}}{k_1\cdots k_{n-2}}+\ln\frac{k_n}{k_{n-1}^2}$ et en sommant d'abord sur $k_n\ge k_{n-1}^2-k_{n-1}+1$ :

$$
\sum_{k_n}e^{it\ln(k_n/k_{n-1}^2)}\frac1{k_n(k_n-1)}=\frac{\psi_{k_{n-1}}(t)}{k_{n-1}(k_{n-1}-1)},
$$

d'où $\phi_n(t)=\sum_{(k_1,\dots,k_{n-1})\in C_{n-1}}\dfrac{e^{it\ln(k_{n-1}/(k_1\cdots k_{n-2}))}}{k_{n-1}(k_{n-1}-1)}\psi_{k_{n-1}}(t)$. La convergence absolue vient de $\sum_{C_n}\mathbb P=1$.

$$
\boxed{\phi_n(t)=\sum_{(k_1,\dots,k_{n-1})\in C_{n-1}}\frac{e^{it\ln(k_{n-1}/(k_1\cdots k_{n-2}))}}{k_{n-1}(k_{n-1}-1)}\psi_{k_{n-1}}(t)}
$$
$\square$

### Question 48.a

> [!INDICATION]
> Voir $\psi_n$ comme une somme de Riemann de $\psi(t)=\int_1^\infty e^{it\ln s}/s^2\,ds$ ; utiliser que $s\mapsto e^{it\ln s}$ est lipschitzienne en $\ln s$ et comparer somme et intégrale.

#### Solution

Avec $\frac{n(n-1)}{k(k-1)}=\frac{n-1}n\int_{(k-1)/n^2}^{k/n^2}\frac{ds}{s^2}$ et $g_t(s)=e^{it\ln s}$,

$$
\begin{aligned}
\Big|\psi_n(t)-\frac{n-1}n\int_{1-1/n}^\infty\frac{g_t(s)}{s^2}ds\Big| \\
&\le \frac{n-1}n\sum_{k\ge m}\frac{|t|}{k-1}\cdot\frac{n^2}{k(k-1)} \\
&\le \frac{C''|t|}n,
\end{aligned}
$$

car $|g_t(k/n^2)-g_t(s)|\le|t|/(k-1)$ et $\sum_{k\ge m}\frac1{k(k-1)^2}\le\frac{C}{(n(n-1))^2}$ ($m=n^2-n+1$). Enfin $\big|\frac{n-1}n\int_{1-1/n}^\infty\frac{g_t}{s^2}-\psi(t)\big|\le\frac3n$. D'où $|\psi_n(t)-\psi(t)|\le C(1+|t|)/n$.

$$
\boxed{|\psi_n(t)-\psi(t)|\le\frac{C(1+|t|)}{n}}
$$
$\square$

### Question 48.b

> [!INDICATION]
> Reprendre la formule de 47, majorer $|\psi_{k_{n-1}}-\psi|$ par 48.a, et reconnaître $I_{n-1}$ (45.c).

#### Solution

$$
\phi_n(t)-\psi(t)\phi_{n-1}(t)=\sum_{C_{n-1}}\frac{e^{it\ln(\cdots)}}{k_{n-1}(k_{n-1}-1)}\big(\psi_{k_{n-1}}(t)-\psi(t)\big).
$$

Par 48.a, $|\psi_{k_{n-1}}-\psi|\le\frac{C(1+|t|)}{k_{n-1}}$, donc le module est $\le C(1+|t|)\sum_{C_{n-1}}\frac1{k_{n-1}^2(k_{n-1}-1)}=C(1+|t|)\sum_j\frac{P_{n-1}(j)}{j}=C(1+|t|)I_{n-1}\le C(\tfrac23)^{n-1}(1+|t|)$.

$$
\boxed{|\phi_n(t)-\psi(t)\phi_{n-1}(t)|\le C\Big(\tfrac23\Big)^{n-1}(1+|t|)}
$$
$\square$

### Question 48.c

> [!INDICATION]
> Télescoper $\phi_n-\psi^{n-m}\phi_m=\sum_{j=m}^{n-1}\psi^{n-1-j}(\phi_{j+1}-\psi\phi_j)$, puis sommer la série géométrique (48.b).

#### Solution

Comme $|\psi|\le1$ et $|\phi_{j+1}-\psi\phi_j|\le C(\tfrac23)^j(1+|t|)$ (48.b),

$$
\begin{aligned}
|\phi_n(t)-\psi^{n-m}(t)\phi_m(t)| \\
&\le \sum_{j\ge m}C(\tfrac23)^j(1+|t|) \\
&= 3C(\tfrac23)^m(1+|t|).\
\end{aligned}
$$

$$
\boxed{|\phi_n(t)-\psi^{n-m}(t)\phi_m(t)|\le3C\Big(\tfrac23\Big)^m(1+|t|)}
$$
$\square$

### Question 48.d

> [!INDICATION]
> Appliquer 48.c avec $s=t/\sqrt n$ ; faire tendre $n\to\infty$ à $m$ fixé en invoquant 27.c, puis faire tendre $m\to\infty$.

> [!METHODE]
> Double limite : faire tendre $n\to\infty$ à $m$ fixé (27.c fournit la gaussienne), puis $m\to\infty$ ; ne pas tout faire tendre en même temps.

#### Solution

Pour $s=t/\sqrt n$, 48.c donne $|\phi_n(s)e^{-it\sqrt n}-\psi(s)^{n-m}\phi_m(s)e^{-it\sqrt n}|\le3C(\tfrac23)^m(1+|t|)$. À $m$ fixé, $n\to\infty$ :

$$
\psi(s)^{n-m}\phi_m(s)e^{-it\sqrt n}=\big[\psi(s)^n e^{-it\sqrt n}\big]\cdot\psi(s)^{-m}\phi_m(s)\longrightarrow e^{-t^2/2}\cdot1\cdot1,
$$

d'après Q27.c (avec $z=t$) et $\psi(s)\to1$, $\phi_m(s)\to\phi_m(0)=1$. Donc $\limsup_n|\phi_n(t/\sqrt n)e^{-it\sqrt n}-e^{-t^2/2}|\le3C(\tfrac23)^m(1+|t|)\to0$ ($m\to\infty$) : la limite vaut $e^{-t^2/2}$.

$$
\boxed{\lim_{n\to\infty}\phi_n(t/\sqrt n)\,e^{-it\sqrt n}=e^{-t^2/2}}
$$
$\square$

### Question 48.e

> [!INDICATION]
> Reconnaître la fonction caractéristique de la loi $\mathcal N(0,1)$ et appliquer le théorème de continuité de Lévy.

#### Solution

Soit $W_n=\frac1{\sqrt n}\ln\frac{Q_n}{Q_1\cdots Q_{n-1}}-\sqrt n$. Sa fonction caractéristique est $\mathbb E[e^{itW_n}]=e^{-it\sqrt n}\phi_n(t/\sqrt n)\to e^{-t^2/2}$ (48.d), fonction caractéristique de $\mathcal N(0,1)$. Par le **théorème de Lévy**, $W_n\to\mathcal N(0,1)$ en loi.

**Théorème de Paul Lévy : $W_n\xrightarrow{\text{loi}}\mathcal N(0,1)$.** $\square$

## Partie VI — Un théorème de Ronald Graham

Théorème de Graham : méthode de Sprague — matrices par blocs donnant des sommes de puissances $p$-ièmes égales (Q49–Q51), décomposition en base $2^p$ (Q52–Q53), puis descente sur le reste $R_p$ (Q55–Q60) pour conclure $U_p\cap\mathbb Q=\bigcup_n P_n$ (Q61), et l'exemple $1/4$ (Q62).

On fixe $p\ge2$ et $u=(1/n^p)_{n\in\mathbb N^*}$. Objectif : établir que $U_p\cap\mathbb Q=\bigcup_{n\in\mathbb N^*}P_n$.

### Question 49.a

> [!INDICATION]
> Poser $D_n(k)=\mathrm{tr}(A_n^k)-\mathrm{tr}(B_n^k)$ ; utiliser la structure par blocs et la formule du binôme pour exprimer $D_{n+1}(k)$ en fonction des $D_n(j)$, $j<k$ ; conclure par récurrence.

> [!METHODE]
> Pour des matrices par blocs, exprimer la différence des traces à l'ordre $k$ en fonction des différences aux ordres $<k$ (binôme) et faire une récurrence sur $k$.

#### Solution

Soit $D_n(k)=\mathrm{tr}(A_n^k)-\mathrm{tr}(B_n^k)$. Comme $A_{n+1},B_{n+1}$ sont bloc-diagonales et $c=2^{n+2}$ commute à tout,

$$
D_{n+1}(k)=-\sum_{j=0}^{k-1}\binom kj c^{k-j}D_n(j).
$$

Or $D_1(0)=D_1(1)=0$. Par récurrence, si $D_n(j)=0$ pour $j\in[\![0,n]\!]$, alors $D_{n+1}(k)=0$ pour $k\le n+1$
(la somme ne fait intervenir que des $j\le k-1\le n$). Donc $A_n^k,B_n^k$ ont même trace pour $k\in[\![1,n]\!]$.

**$\mathrm{tr}(A_n^k)=\mathrm{tr}(B_n^k)$ pour tout $k\in[\![1,n]\!]$.** $\square$

### Question 49.b

> [!INDICATION]
> Les matrices $A_p$ et $B_p$ sont diagonales, à coefficients impairs et deux à deux distincts : compter leurs coefficients (il y en a $2^{p+1}$ au total), prendre $q$ égal à la moitié, et appliquer 49.a avec $n=p$.

> [!PIEGE]
> Compter les coefficients diagonaux : $A_p$ et $B_p$ ont chacune $2^p$ coefficients, soit $2^{p+1}$ au total ; la moitié de $2^{p+1}$ n'est pas $2^{p-1}$.

#### Solution

Les matrices $A_p$ et $B_p$ sont diagonales, de taille $2^p$, à coefficients **impairs** (la parité est préservée par l'ajout de $2^{n+2}$). Par récurrence, les $2^{p+1}$
coefficients diagonaux de $A_p$ et $B_p$ sont deux à deux distincts et strictement inférieurs à $2^{p+2}$ (à l'étape $n+1$, les nouveaux coefficients sont les anciens décalés de $2^{n+2}$).
On pose $q=2^p$ (entier pair) et on prend pour $a_1,\dots,a_{2q}$ les $2^{p+1}$ coefficients diagonaux de $A_p$ puis de $B_p$
: $\sum_{i\le q}a_i^k=\mathrm{tr}(A_p^k)$ et $\sum_{i>q}a_i^k=\mathrm{tr}(B_p^k)$, qui sont égaux pour tout $k\in[\![1,p]\!]$ d'après Q49.a.

**Il existe $q=2^p$ (pair) et $2q$ entiers impairs distincts $a_1,\dots,a_{2q}$ tels que $\sum_{i\le q}a_i^k=\sum_{i>q}a_i^k$ pour $k\in[\![1,p]\!]$.** $\square$

### Question 49.c

> [!INDICATION]
> Développer chaque $(X+a_i)^p$ par la formule du binôme et comparer coefficient par coefficient grâce à 49.b (ne pas oublier le coefficient de degré $p$, égal à $q$ des deux côtés).

#### Solution

$\sum_{i\le q}(X+a_i)^p=\sum_{k=0}^p\binom pk X^{p-k}\sum_{i\le q}a_i^k$ ; chaque coefficient (y compris $k=0$, qui vaut $q$ de part et d'autre) coïncide avec celui de $\sum_{i>q}(X+a_i)^p$ par Q49.b. Donc les deux polynômes sont égaux.

**\sum_{i=1}^{q}(X+a_i)^p=\sum_{i=q+1}^{2q}(X+a_i)^p** $\square$

### Question 50.a

> [!INDICATION]
> Les valeurs de $D$ à éviter sont les $(a_k-a_\ell)/(j-i)$ pour $(k,i)\ne(\ell,j)$ : il y en a un nombre fini ; choisir $D$ pair hors de cet ensemble.

#### Solution

$a_k+iD=a_\ell+jD$ avec $(k,i)\ne(\ell,j)$ impose $i\ne j$ (sinon $a_k=a_\ell$, exclu) et $D=\frac{a_k-a_\ell}{j-i}$
: un nombre fini de valeurs interdites. On choisit $D$ pair $\ge2$ hors de cet ensemble fini.

**On peut choisir $D$ pair $\ge2$ tel que les $a_k+iD$ soient deux à deux distincts.** $\square$

### Question 50.b

> [!INDICATION]
> $S_{\bar k}(\omega_p)=n_{\bar k}^p$ avec $n_{\bar k}=\prod_m(\omega_p+a_{k_m}+mD)$, impair si $\omega_p$ est pair ; montrer que les $T_{\bar k}$ sont deux à deux distincts (50.a) et choisir $\omega_p$ pair hors des racines des différences $T_{\bar k}-T_{\bar k'}$.

#### Solution

$S_{\bar k}(\omega_p)=n_{\bar k}^p$ avec $n_{\bar k}=\prod_{m=1}^p(\omega_p+a_{k_m}+mD)$, **impair** si $\omega_p$ pair ($a_{k_m}$ impair, $mD$
pair). Les polynômes $T_{\bar k}=\prod_m(X+a_{k_m}+mD)$ sont distincts pour $\bar k$ distincts (par Q50.a, les $a_k+iD$ sont distincts, donc les multiplicités par « niveau » $m$ déterminent $\bar k$).
On choisit $\omega_p$ pair, positif assez grand, hors des (finiment nombreuses) racines des $T_{\bar k}-T_{\bar k'}$ : les $n_{\bar k}$ sont alors des entiers impairs deux à deux distincts, et $(S_{\bar k}(\omega_p))$ est une famille de $(2q)^p$ puissances $p$-ièmes distinctes.

**Il existe $\omega_p$ pair tel que les $(S_{\bar k}(\omega_p))$ forment $(2q)^p$ puissances $p$-ièmes d'entiers impairs distincts.** $\square$

### Question 50.c

> [!INDICATION]
> Appliquer 49.c au polynôme $X+kD$ ; la parité de $\pi_p$ vient du fait que chaque $M_{k,0}(\omega_p)$ est une somme de $q$ entiers impairs ($q$ pair).

#### Solution

$M_{k,0}(X)=\sum_{i=1}^q(X+kD+a_i)^p$ et $M_{k,1}(X)=\sum_{i=q+1}^{2q}(X+kD+a_i)^p$ ; par Q49.c (avec $X\mapsto X+kD$), $M_{k,0}=M_{k,1}$. Donc $\pi_p=\prod_k M_{k,\varepsilon_k}(\omega_p)$
est **indépendant** de $\varepsilon$. De plus $M_{k,0}(\omega_p)$ est somme de $q$ (pair) entiers impairs, donc pair ; $\pi_p$ est un entier naturel pair.

$$
\boxed{\pi_p=\prod_{k=1}^p M_{k,\varepsilon_k}(\omega_p)\text{ est un entier pair, indépendant de }\varepsilon}
$$
$\square$

### Question 51

> [!INDICATION]
> Développer le produit $\pi_p=\prod_k\sum_{m=1}^q(\omega_p+a_{\varepsilon_kq+m}+kD)^p$ ; les ensembles $M_\varepsilon$ sont disjoints car $\bar k\mapsto n_{\bar k}$ est injective (50.b).

#### Solution

En développant $\pi_p=\prod_{k=1}^p\sum_{m=1}^q(\omega_p+a_{\varepsilon_kq+m}+kD)^p=\sum_{(m_k)}n_{\bar k}^p$ où $\bar k=(\varepsilon_kq+m_k)_k$. Pour chaque $\varepsilon\in\{0,1\}^p$, $M_\varepsilon=\{n_{\bar k}:(m_k)\in[\![1,q]\!]^p\}$ est un ensemble de $q^p$
entiers impairs distincts avec $\pi_p=\sum_{k\in M_\varepsilon}k^p$. Les $M_\varepsilon$ ($2^p$ choix) correspondent à des plages de coordonnées $[\![1,q]\!]$ ou $[\![q+1,2q]\!]$
disjointes ; comme $\bar k\mapsto n_{\bar k}$ est injective (Q50.b), les $M_\varepsilon$ sont **deux à deux disjoints**.

**Il existe $2^p$ ensembles finis non vides d'entiers impairs, deux à deux disjoints, de somme de puissances $p$-ièmes égale à $\pi_p$.** $\square$

### Question 52.a

> [!INDICATION]
> Écrire $m$ en base $B=2^p$.

#### Solution

Écriture de $m$ en base $B=2^p$ : $m=\sum_{k=0}^r b_k(2^p)^k=\sum_k b_k2^{pk}$ avec $b_k\in[\![0,2^p-1]\!]$.

$$
\boxed{m=\sum_{k=0}^r b_k\,2^{pk}\text{ avec }b_k\in[\![0,2^p-1]\!]}
$$
$\square$

### Question 52.b

> [!INDICATION]
> Pour chaque chiffre $b_k\le2^p-1$, réunir les $b_k$ premiers ensembles $M_i$ (disjoints) pour écrire $b_k\pi_p$, puis multiplier par $2^{pk}$
; distinguer les niveaux $k$ par la valuation 2-adique de $2^kj$ ($j$ impair).

> [!METHODE]
> La valuation 2-adique distingue les niveaux $k$ dans les bases $2^kj$ ($j$ impair).

#### Solution

$m\pi_p=\sum_k b_k2^{pk}\pi_p$. Comme $b_k\le2^p-1$, $b_k\pi_p=\sum_{j\in\bigcup_{i\le b_k}M_i}j^p$ (réunion disjointe) ; donc $b_k2^{pk}\pi_p=\sum_j(2^kj)^p$. Les bases $2^kj$
($j$ impair) ont valuation $2$-adique exactement $k$ : distinctes pour $k$ distincts, et distinctes à $k$
fixé. Ainsi $m\pi_p$ est somme de puissances $p$-ièmes d'entiers **distincts**.

**$m\pi_p$ est somme de puissances $p$-ièmes d'entiers naturels distincts.** $\square$

### Question 53

> [!INDICATION]
> Écrire $n=\rho+m\pi_p$ avec $\rho=n\bmod\pi_p$, ajuster le résidu avec les $(k\pi_p+1)^p\equiv1\pmod{\pi_p}$ ($k\le\rho$), appliquer 52.b au quotient ; disjoindre les deux familles de bases par parité et par taille ($j\le\pi_p^{1/p}<\pi_p+1\le k\pi_p+1$).

> [!PIEGE]
> Pour disjoindre les deux familles de bases, jouer sur la parité (impaires contre paires) et sur la taille ($j\le\pi_p^{1/p}<\pi_p+1\le k\pi_p+1$).

#### Solution

Soit $n\ge\Theta_p$, $\rho=n\bmod\pi_p$, $m=(n-\rho)/\pi_p$. Posons $\Sigma=\sum_{k=1}^\rho(k\pi_p+1)^p$ ; comme $(k\pi_p+1)^p=1+\pi_p c_k$,
on a $\Sigma=\rho+\pi_p\sum_{k\le\rho}c_k$, et $n-\Sigma=\pi_p\,m'$ avec $m'=m-\sum_{k\le\rho}c_k$. De $n\ge\Theta_p$ on tire $m\ge\sum_{k=1}^{\pi_p-1}c_k\ge\sum_{k\le\rho}c_k$,
donc $m'\ge0$. Si $m'=0$ (alors $n=\Theta_p$), $n=\Sigma$. Si $m'\ge1$,
$n=\Sigma+m'\pi_p$ : $\Sigma$ est somme des puissances $(k\pi_p+1)^p$ (bases **impaires** $\ge\pi_p+1$, car $\pi_p$
pair) et $m'\pi_p$ est somme (52.b) de puissances de bases $2^kj$ avec $j$ impair $\le\pi_p^{1/p}<\pi_p+1$. Les bases impaires de la seconde famille ($j$)
sont $<\pi_p+1\le k\pi_p+1$, les paires ne rencontrent pas la première : les deux familles sont disjointes. Donc $n$ est somme de puissances $p$-ièmes d'entiers distincts.

**Tout entier $n\ge\Theta_p$ est somme de puissances $p$-ièmes d'entiers naturels distincts.** $\square$

### Question 54

> [!INDICATION]
> Minorer $\sum_{k=1}^n k^p$ par $\int_0^n t^p dt$ et majorer $(n+1)^p$ par $2^p n^p$.

#### Solution

$\sum_{k=1}^n k^p\ge\int_0^n t^p dt=\frac{n^{p+1}}{p+1}$ et $(n+1)^p\le2^pn^p$. Pour $n\ge(p+1)2^p$, $\frac{n^{p+1}}{p+1}\ge2^pn^p\ge(n+1)^p$. Prendre $\delta_p=\max(\Theta_p,(p+1)2^p)$.

**Il existe $\delta_p\ge\Theta_p$ tel que $\sum_{k=1}^n k^p\ge(n+1)^p$ pour tout $n\ge\delta_p$.** $\square$

On fixe un rationnel $x\in U_p$.

### Question 55

> [!INDICATION]
> Prolongez un préfixe en conservant un reste dans la queue, puis contrôlez les écarts entre les sous-sommes finies. Quel choix arithmétique de K rend les divisions simples ?

#### Solution
Écrivons $x=a/b$, avec $a\in\mathbb Z$, $b\in\mathbb N^*$. Par définition de $U_p$ et la question 38, il existe une somme $\omega$ utilisant seulement les premiers termes et un reste $y$ tels que

$$x=\omega+y,\qquad 0\le y<\sum_{j>N_p}j^{-p}.$$

Si $y=0$, $x$ est déjà une somme finie et on peut choisir $\Lambda=x$, $R_p=0$. Sinon, on fixe un entier $N$ assez grand et un préfixe $\omega_N\in P_N$ tel que

$$0\le x-\omega_N<\sum_{j>N}j^{-p},\qquad \left(1+\frac1{N+1}\right)^p<2.$$

Un tel préfixe s'obtient par prolongation gloutonne : au rang $j$, on prend $j^{-p}$ si le reste $r$ est au moins $j^{-p}$, sinon on ne le prend pas. Dans le premier cas, $r-j^{-p}$ reste strictement inférieur à la queue suivante ; dans le second, $r<j^{-p}$ est inférieur ou égal à cette queue par substituabilité. Si le reste devient nul, on est dans le cas précédent. Sinon, il reste strictement inférieur à la queue, car un reste strictement inférieur à la somme totale ne peut devenir égal à une somme de queue après soustraction d'un terme sans avoir déjà été cette borne avant cette soustraction.

Justifions l'approximation finie requise. Pour $K>N+1$, posons $a_j=j^{-p}$, $N+1\le j\le K-1$, et $a_*=a_{K-1}$. On a

$$a_j\le\sum_{i=j+1}^{K-1}a_i+a_*.$$

En effet, l'inégalité est une égalité pour $j=K-1$ ; en remontant, $a_j<2a_{j+1}$ et l'inégalité au rang $j+1$ donnent celle au rang $j$. Il s'ensuit par récurrence que les intervalles $[s,s+a_*]$, où $s$ décrit toutes les sous-sommes de $a_{N+1},\ldots,a_{K-1}$, recouvrent $[0,\sum_{j=N+1}^{K-1}a_j+a_*]$ : à chaque étape, les deux intervalles obtenus en ajoutant ou non le premier terme se touchent ou se recouvrent. Les écarts entre deux sous-sommes consécutives sont donc au plus $a_*$.

Pour $K$ assez grand, $x-\omega_N<\sum_{j=N+1}^{K-1}j^{-p}$. En prenant la plus grande sous-somme $s\le x-\omega_N$, on obtient

$$\Lambda=\omega_N+s\in P_{K-1},\qquad 0\le x-\Lambda<\frac1{(K-1)^p}.$$

L'inégalité est stricte : une sous-somme strictement supérieure au reste existe, et l'écart jusqu'à cette sous-somme est au plus $(K-1)^{-p}$.

Choisissons maintenant $K=K_p$ **premier**, arbitrairement grand, supérieur à $b,N$ et aux bornes déjà imposées par la condition sur $C_p,K_p$. Celle-ci est conservée lorsqu'on augmente $K_p$, puisque les mêmes représentations restent autorisées. Alors $b\mid(K_p-1)!$. Pour tout $j<K_p$, le quotient entier $K_p!/j$ est divisible par $K_p$, puisque $j$ n'est pas divisible par le nombre premier $K_p$. Ainsi

$$R_p=(K_p!)^p(x-\Lambda)$$

est un entier positif ou nul, divisible par $K_p$ (même par $K_p^p$). On a finalement

$$\boxed{x-\Lambda=\frac{R_p}{(K_p!)^p}<\frac1{(K_p-1)^p},\quad \Lambda\in P_{K_p-1},\quad R_p\in K_p\mathbb N.}$$

**Précision utilisable en Q62.** La construction respecte n'importe quel préfixe fixé $\omega_N$ dès que $0\le x-\omega_N<\sum_{j>N}j^{-p}$ : les nouveaux indices utilisés dans $\Lambda$ sont $>N$. Les corrections des questions suivantes utiliseront des indices $\ge K_p$, donc également $>N$.


### Question 56

> [!INDICATION]
> Regroupez les produits selon leur nombre de facteurs. Reliez deux choix de facteurs par des déplacements adjacents, puis comparez les plages des groupes successifs.

#### Solution
Écrivons $C=C_p$, $K=K_p$ et $r=K-C+1$. Les racines $p$-ièmes des éléments de $\mathcal N$ sont exactement les produits de sous-ensembles non vides et propres de $\{C,\ldots,K\}$ : le plus grand produit propre est $(C+1)\cdots K=\Delta_p^{1/p}$, tandis que le produit de tous les facteurs est strictement supérieur à cette borne.

Pour $1\le q\le r-1$, considérons les produits de $q$ facteurs distincts. Leur minimum et leur maximum sont

$$A_q=C(C+1)\cdots(C+q-1),\qquad B_q=(K-q+1)\cdots K.$$

Le graphe des $q$-sous-ensembles, où l'on déplace un indice d'une unité lorsque cela ne crée pas de répétition, est connexe : on peut ramener successivement les indices ordonnés à $C,C+1,\ldots,C+q-1$. Sur chacune de ses arêtes, le rapport du produit le plus grand au plus petit est $(j+1)/j\le2$. Par conséquent, deux valeurs consécutives de la couche ont un rapport au plus $2$ : sinon aucune arête ne traverserait la coupure correspondante, ce qui contredirait la connexité.

Les plages des couches successives se recouvrent. En effet, pour $1\le q\le r-2$, posons $u_q=A_{q+1}/B_q$. On calcule

$$\frac{u_{q+1}}{u_q}=\frac{C+q+1}{K-q}.$$

Ces rapports croissent avec $q$ : la suite $(u_q)$ décroît puis croît, et son maximum se trouve à une extrémité. Or

$$u_1=u_{r-2}=\frac{C(C+1)}K<1,$$

car $K>(C+1)!$ et $C>2\delta_p\ge2$. Donc $A_{q+1}\le B_q$. Une coupure entre deux produits consécutifs de l'union doit être traversée par une couche, puisque les intervalles des couches successives se recouvrent. L'écart de cette couche est au plus $2$, donc il en est de même de l'écart global. En élevant à la puissance $p$,

$$\boxed{m_{k+1}/m_k\le2^p\qquad(1\le k<Z).}$$


### Question 57

> [!INDICATION]
> Cherchez un choix admissible à une extrémité de la liste des produits. Vérifiez les deux bornes sur le reste avant de conclure.

#### Solution
Posons $A=R_p-\Theta_p$. Comme $R_p>0$ est multiple de $K_p>\Theta_p$, $A\ge0$. D'après Q55 et $K_p-1>C_p!$,

$$R_p<\left(\frac{K_p!}{K_p-1}\right)^p<\left(\frac{K_p!}{C_p!}\right)^p=\Delta_p.$$

Ainsi $0\le A<\Delta_p=m_Z$, et le choix $k=0$, $i=Z$ vérifie les inégalités définissant $\mathcal B$. **$0\in\mathcal B$, donc $\mathcal B$ est non vide.**


### Question 58.a

> [!INDICATION]
> Raisonnez par contraposée : si le reste dépasse la borne visée, quelle classe de produits permet de construire un entier admissible trop grand ?

#### Solution
On raisonne par contraposée. Supposons $A\ge(\delta_p C_p)^p=\delta_p^p m_1$. Puisque $A<\Delta_p$, il existe un plus grand indice $j<Z$ tel que

$$m_j\le A/\delta_p^p<m_{j+1}.$$

La Q56 donne $m_{j+1}\le2^p m_j$. Il en résulte

$$\delta_p\le\left(A/m_j\right)^{1/p}<2\delta_p<C_p.$$

L'entier $k=\lfloor(A/m_j)^{1/p}\rfloor$ appartient donc à $\llbracket\delta_p,C_p-1\rrbracket$ et vérifie $k^p m_j\le A<(k+1)^p m_j$. Ainsi $k\in\mathcal B$ et $G\ge\delta_p$. Par contraposée, si $G<\delta_p$,

$$\boxed{\Theta_p\le R_p<\Theta_p+(\delta_p C_p)^p.}$$

Cette borne stricte implique la borne large demandée.


### Question 58.b

> [!INDICATION]
> Utilisez la condition sur C et K, puis traduisez chaque puissance entière en inverse de puissance. Vérifiez séparément les indices et leur distinctitude.

#### Solution
La condition imposée à $C_p,K_p$ et Q58.a donnent une partie finie $M\subset\mathbb N^*$ telle que

$$R_p=\sum_{d\in M}d^p,$$

chaque $d$ étant produit de facteurs distincts de $\llbracket1,K_p\rrbracket$. Chaque $d$ divise donc $K_p!$, et les nombres $j_d=K_p!/d$ sont des entiers distincts. En outre $d^p\le R_p<(K_p!/(K_p-1))^p$, d'où $j_d>K_p-1$ : ils sont tous $\ge K_p$. Ainsi

$$x=\Lambda+\sum_{d\in M}\frac1{j_d^p}.$$

Les indices de $\Lambda$ sont $\le K_p-1$ et ceux de la seconde somme $\ge K_p$ : aucune répétition n'est possible. **$x$ est donc une sous-somme finie de la série, soit $x\in\bigcup_nP_n$.**


### Question 59.a

> [!INDICATION]
> Pour prouver qu’un minimum existe, montrez que l’ensemble est non vide et fini.

#### Solution
L'encadrement associé à $i_0$ donne $G^p m_{i_0}\le A$. Donc $G$ appartient à l'ensemble dont on demande le minimum. C'est une partie non vide de l'ensemble fini $\llbracket1,G\rrbracket$ : **$k_0$ existe.**


### Question 59.b

> [!INDICATION]
> Avant d’utiliser la minimalité au rang précédent, excluez le premier rang à l’aide de la question 54.

#### Solution
On vérifie d'abord que $k_0\ge2$, point nécessaire avant d'utiliser $k_0-1$. Puisque $G\ge\delta_p$, Q54 donne

$$\sum_{k=1}^G k^p\ge(G+1)^p.$$

Par l'encadrement définissant $i_0$, $(G+1)^p m_{i_0}>A$. Ainsi $1$ n'appartient pas à l'ensemble de Q59.a, d'où $k_0\ge2$. La minimalité de $k_0$ donne alors

$$\sum_{k=k_0}^G k^p m_{i_0}\le A<\sum_{k=k_0-1}^G k^p m_{i_0}.$$

En soustrayant la première somme,

$$\boxed{0\le R'_p-\Theta_p<(k_0-1)^p m_{i_0}.}$$


### Question 60

> [!INDICATION]
> Faites décroître un reste entier. Quel invariant garantit que chaque nouveau bloc utilise des bases plus petites que toutes celles déjà extraites ?

#### Solution
Le cas $R_p=0$ donne $x=\Lambda\in P_{K_p-1}$. Supposons $R_p>0$. On applique la descente suivante au reste entier $R$, initialement égal à $R_p$. Les propriétés nécessaires aux Q56–59 sont $\Theta_p\le R<\Delta_p$ ; elles seront conservées. La divisibilité par $K_p$ ne sert qu'à les établir au départ.

Si $G<\delta_p$, Q58 fournit une représentation terminale de $R$ en puissances $p$-ièmes de diviseurs de $K_p!$ produits de facteurs distincts. Sinon, Q59 écrit

$$R=\sum_{k=k_0}^{G}(kq)^p+R',\qquad q=m_{i_0}^{1/p}.$$

Le nombre $q$ est produit de facteurs distincts appartenant à $\llbracket C_p,K_p\rrbracket$ ; comme $1\le k\le G<C_p$, chaque $kq$ est à son tour produit de facteurs distincts de $\llbracket1,K_p\rrbracket$. Les bases extraites dans une étape sont distinctes. De plus, $\Theta_p\le R'<R<\Delta_p$.

La Q59.b donne une propriété plus forte qui garantit la distinctitude entre étapes :

$$R'<\Theta_p+(k_0-1)^p m_{i_0}<k_0^p m_{i_0}.$$

La seconde inégalité vient de $\Theta_p<C_p^p\le m_{i_0}$ et de $k_0^p-(k_0-1)^p\ge1$. **Le nouveau reste est strictement inférieur à la plus petite puissance extraite.** Toute puissance extraite ultérieurement, ou présente dans la représentation terminale, est au plus le reste courant : elle est donc strictement plus petite que toutes les puissances déjà extraites.

Les restes sont des entiers strictement décroissants et restent $\ge\Theta_p$ : la descente s'arrête nécessairement sur le cas $G<\delta_p$. Elle donne

$$R_p=\sum_{d\in M}d^p$$

avec des bases $d$ toutes distinctes, chacune produit de facteurs distincts de $\llbracket1,K_p\rrbracket$. Comme à Q58.b, les indices $K_p!/d$ sont des entiers distincts $\ge K_p$, disjoints de ceux de $\Lambda$. On obtient **$x\in\bigcup_nP_n$.**

Cette démonstration conserve également la précision de Q55 : tout préfixe fixé y reste inchangé.


### Question 61

> [!INDICATION]
> Pour la réciproque, une sous-somme finie peut-elle atteindre l’extrémité droite de la queue infinie correspondante ?

#### Solution
La Q60 établit $U_p\cap\mathbb Q\subseteq\bigcup_nP_n$. Réciproquement, toute sous-somme finie est rationnelle et appartient à $P_\infty(u)$. Dans la décomposition disjointe de Q38, son préfixe détermine un unique intervalle. Sa queue finie est strictement inférieure à la somme de la queue infinie, puisque tous les termes sont strictement positifs. Une sous-somme finie ne peut donc être l'extrémité droite de cet intervalle ; elle appartient à $U_p$. Ainsi

$$\boxed{U_p\cap\mathbb Q=\bigcup_{n\ge1}P_n.}$$


### Question 62.a

> [!INDICATION]
> Imposez un préfixe nul et vérifiez que la valeur demandée reste à l’intérieur de la queue ; reprenez ensuite la construction rationnelle.

#### Solution
La précision de Q55–60 permet d'appliquer la conclusion en conservant un préfixe. Pour $p=2$, fixons les deux premiers coefficients à zéro. On a

$$0<\frac14<\sum_{n=3}^{\infty}\frac1{n^2},$$

la dernière somme étant supérieure à $\int_3^\infty t^{-2}\,dt=1/3$. Le rationnel $1/4$ est donc à l'intérieur du cylindre de ce préfixe ; la construction Q55–60 donne une somme **finie**

$$\boxed{\frac14=\sum_{j=1}^{r}\frac1{n_j^2},\qquad 3\le n_1<\cdots<n_r.}$$

Comme chaque terme est au plus $1/9<1/4$, il y a au moins deux termes (en fait au moins trois).


### Question 62.b

> [!INDICATION]
> Gardez un reste strictement positif après tout préfixe fini. Que donnerait une borne commune sur les supports de toutes les représentations ?

#### Solution
Posons $T_N=\sum_{n>N}n^{-2}$. Pour tout $n\ge2$,

$$T_n>\int_{n+1}^{\infty}t^{-2}\,dt=\frac1{n+1}>\frac1{n^2}.$$

Les deux intervalles ouverts correspondant au choix du coefficient d'indice $n$, à savoir $(0,T_n)$ et $(n^{-2},n^{-2}+T_n)$, se recouvrent. Leur réunion est $(0,T_{n-1})$.

Soit $x$ un rationnel dans l'une des deux composantes ouvertes indiquées. Puisque $N_2=1$, on part du préfixe $\omega_1=0$ si $x<\pi^2/6-1$, et de $\omega_1=1$ si $x>1$. Dans les deux cas $0<x-\omega_1<T_1$. Par récurrence utilisant le recouvrement strict précédent, pour tout $N\ge1$ il existe un préfixe $\omega_N\in P_N$ tel que

$$0<x-\omega_N<T_N.$$

Appliquons la construction Q55–60 en conservant ce préfixe. Elle donne une représentation finie de $x$ qui utilise au moins un indice **strictement supérieur à $N$**, puisque $x-\omega_N>0$. Comme $N$ est arbitrairement grand, les supports de ces représentations ne peuvent appartenir à un ensemble fini de supports finis. **Il existe donc une infinité de suites à valeurs dans $\{0,1\}$, stationnant à zéro, qui représentent $x$.**


## Bilan

**Méthodes à retenir.**

- Développement $p$-adique : unicité du développement propre (non stationnaire à $p-1$), obtenue par reconstruction des parties entières (Q5) ; l'inégalité stricte de l'encadrement de base interdit la stationnarité à la valeur maximale (Q4).
- Série de Sylvester : la suite des restes décroît strictement (Q8.a), la récurrence $q_{n+1}\ge q_n^2-q_n+1$ donne la convergence (Q8.c) et l'unicité (Q9–Q10) ; l'identité télescopante de Q7.b caractérise la rationalité (Q11).
- Sommes de sous-séries : la substituabilité ($u_n\le\sum_{k>n}u_k$) entraîne $P_\infty(u)=[0,\sigma]$ (Q35.d) ; avec une tête finie non substituable, on obtient une réunion disjointe de segments (Q38.e) — structure qui définit $U_p$ en partie VI.
- Analyse : convergence normale sur tout compact pour la continuité/l'holomorphie (Q12.a, Q18) ; convergence dominée sur la mesure de comptage pour les limites de séries (Q16.b) ; comparaison série/intégrale (Q12.d) ; Liouville après appariement des pôles (Q20.c) ; IPP itérées avec terme de bord (Q19.d–e).
- Probabilités : propriété de Markov des chiffres de Sylvester (Q43–Q44), décroissance géométrique de $I_n$ (Q45.c), théorème de continuité de Lévy (Q48.e).
- Arithmétique (partie VI) : matrices par blocs et traces pour égaliser des sommes de puissances (Q49), familles disjointes de puissances $p$-ièmes (Q50–Q51), valuation 2-adique pour distinguer les niveaux (Q52.b), descente sur le reste (Q59–Q60).

**Pré-requis à revoir.** Suites adjacentes et partie entière ; théorème de Cauchy et primitives sur les ouverts étoilés ; inversion locale holomorphe ; transformée de Fourier et Riemann-Lebesgue ; convergence dominée ; théorème de Lévy.

**Questions classiques transposables.** Calcul de $\zeta(2)$ par $(\pi/\sin)^2$ (Q20) ; ensembles de Cantor comme sommes de sous-séries (Q31.d) ; loi des chiffres d'une uniforme (Q43) ; TCL pour les séries de Sylvester (Q48.e) ; méthode de Sprague pour les sommes de puissances distinctes (Q49–Q53).
