# CAPES Maths — Épreuve d'admissibilité 1 (bac+3) 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Première épreuve écrite d'admissibilité du CAPES externe de mathématiques (bac+3), session 2026 : 5 heures, calculatrice autorisée, tout ouvrage et tout matériel électronique interdits. Le sujet est composé de quatre exercices indépendants, qui balayent le tronc commun de licence : raisonnement et calcul (exercice 1, Vrai/Faux à sept assertions), analyse (exercice 2, étude d'une suite d'intégrales et équivalents), algèbre et réduction (exercice 3, puissances universelles dans $\mathbb Z/n\mathbb Z$ puis dans $\mathcal M_n(\mathbb R)$), probabilités discrètes (exercice 4, jeu de dés).

Le rapport 2026 donne une moyenne de 10,51 et une médiane de 11,20 pour cette épreuve ; le barème permet d'obtenir 20/20 sans traiter l'intégralité du sujet, mais le jury met en garde contre le « grappillage ». Ordre conseillé : commencer par l'exercice 1, très rentable, puis l'exercice 2, largement guidé ; l'exercice 3 exige une lecture exacte de la définition de « puissance universelle » ; l'exercice 4, « nettement moins abordé » par les candidats, est le plus discriminant.

> [!JURY]
> « Les copies sont trop souvent lapidaires : les raisonnements sont trop peu explicités, les liens logiques peu formulés et les réponses trop rarement justifiées. » (rapport 2026, p. 57) Nommez chaque propriété utilisée (croissance de l'intégrale, théorème d'encadrement, limite monotone…), au moins lors de sa première utilisation.

## Exercice 1 : Vrai/Faux

### Assertion 1

> [!INDICATION]
> Une implication « point critique ⇒ extremum local » est-elle vraie en général ? Cherchez un contre-exemple simple.

> [!INDICATION]
> Pensez à une fonction dérivable dont la dérivée s'annule en un point sans changer de signe.

#### Solution

**FAUSSE.** Prenons $f:\mathbb R\to\mathbb R$, $x\mapsto x^3$, dérivable sur $\mathbb R$, et $a=0$. On a $f'(x)=3x^2$, donc $f'(0)=0$. Pourtant, pour tout
$\varepsilon>0$ :

$$

\begin{aligned}
f(\varepsilon)&=\varepsilon^3>0=f(0),\\
f(-\varepsilon)&=-\varepsilon^3<0=f(0).
\end{aligned}

$$

Dans tout voisinage de $0$, $f$ prend des valeurs strictement supérieures et strictement inférieures à $f(0)$ : $f$ n'admet en $0$ ni maximum ni minimum local.

> [!JURY]
> « la fonction cube a souvent été correctement choisie » (rapport 2026, p. 58)

### Assertion 2

> [!INDICATION]
> Comment calculer une intégrale de $\sin^2$ sur un segment de longueur multiple de $\pi$ ?

> [!INDICATION]
> Linéarisez $\sin^2$ à l'aide de $\cos(2x)$.

#### Solution

**VRAIE.** Par linéarisation, $\sin^2 x=\dfrac{1-\cos 2x}{2}$ pour tout $x$. Donc

$$

\begin{aligned}
\int_0^{n\pi}\sin^2 x\,\mathrm dx
&=\frac12\int_0^{n\pi}\bigl(1-\cos 2x\bigr)\,\mathrm dx\\
&=\frac12\left[x-\frac{\sin 2x}{2}\right]_0^{n\pi}\\
&=\frac{n\pi}{2}.
\end{aligned}

$$

$$
\boxed{\int_0^{n\pi}\sin^2 x\,\mathrm dx=\frac{n\pi}{2}}
$$

### Assertion 3

> [!INDICATION]
> Calculez les affixes des vecteurs du triangle, puis les trois longueurs.

> [!INDICATION]
> Reconnaissez une égalité de Pythagore — pensez à la réciproque du théorème.

#### Solution

**VRAIE.** Les affixes des vecteurs sont $z_{\overrightarrow{BA}}=t-1$, $z_{\overrightarrow{BC}}=i(1-t)$ et $z_{\overrightarrow{AC}}=(1-t)(1+i)$. Donc

$$

\begin{aligned}
BA&=|t-1|,\\
BC&=|1-t|,\\
AC&=\sqrt{2}\,|1-t|.
\end{aligned}

$$

Comme $t\neq1$, on a $BA=BC>0$ : le triangle est isocèle en $B$. De plus

$$
AC^2=2(1-t)^2=BA^2+BC^2,
$$

si bien que, par la réciproque du théorème de Pythagore, le triangle $ABC$ est rectangle en $B$. Il est isocèle et rectangle.

> [!JURY]
> un futur enseignant doit savoir « distinguer le théorème de Pythagore de sa réciproque » (p. 58)

### Assertion 4

> [!INDICATION]
> Un polynôme de degré impair est continu sur $\mathbb R$ ; que dire de ses limites en $\pm\infty$ ?

> [!INDICATION]
> Attention au signe du coefficient dominant : la limite en $+\infty$ n'est pas toujours $+\infty$.

#### Solution

**VRAIE.** Soit $P\in\mathbb R[X]$ de degré impair $n$, de coefficient dominant $c\neq0$. La fonction polynomiale $P$ est continue sur $\mathbb R$. Si $c>0$, alors
$\lim_{x\to+\infty}P(x)=+\infty$ et, comme $n$ est impair, $\lim_{x\to-\infty}P(x)=-\infty$ ; si $c<0$, on applique ce qui précède à $-P$. Dans les deux cas, $P$ prend des valeurs de signes contraires, donc par le théorème des valeurs intermédiaires il existe
$x\in\mathbb R$ tel que $P(x)=0$.

### Assertion 5

> [!INDICATION]
> Quelles propriétés doit vérifier une forme bilinéaire symétrique pour être un produit scalaire ?

> [!INDICATION]
> Le point délicat est le caractère défini : que vaut un polynôme de degré $\le1$ qui s'annule en $0$ et en $1$ ?

#### Solution

**VRAIE.** Posons $\varphi(P,Q)=P(0)Q(0)+P(1)Q(1)$ sur $\mathbb R_1[X]$. La bilinéarité et la symétrie sont immédiates (les évaluations en $0$ et en $1$ sont linéaires, et le produit de $\mathbb R$ est commutatif). Positivité : $\varphi(P,P)=P(0)^2+P(1)^2\ge0$. Caractère défini : si
$\varphi(P,P)=0$, alors $P(0)^2+P(1)^2=0$, somme de deux réels positifs, donc $P(0)=P(1)=0$ ; un polynôme de degré au plus $1$ ayant deux racines distinctes est nul. Ainsi $\varphi$ est une forme bilinéaire symétrique définie positive : c'est un produit scalaire.

### Assertion 6

> [!INDICATION]
> Sous quelle forme s'écrivent les racines $n$-ièmes de l'unité ? La somme demandée est-elle une somme géométrique ?

> [!INDICATION]
> Avant d'appliquer la formule de la somme géométrique, vérifiez la condition sur la raison.

#### Solution

**VRAIE.** Posons $\omega_k=e^{2ik\pi/n}$ pour $k\in\llbracket0,n-1\rrbracket$, et $q=e^{2ip\pi/n}$. Comme $p\in\llbracket1,n-1\rrbracket$, on a $0<\dfrac{2p\pi}{n}<2\pi$, donc $q\neq1$. Alors

$$

\begin{aligned}
\sum_{k=0}^{n-1}\omega_k^{\,p}
&=\sum_{k=0}^{n-1}q^k\\
&=\frac{1-q^n}{1-q}\\
&=0,
\end{aligned}

$$

car $q^n=e^{2ip\pi}=1$.

$$
\boxed{\sum_{k=0}^{n-1}\omega_k^{\,p}=0}
$$

> [!JURY]
> erreur fréquente relevée : « l'oubli de la condition sur la raison dans la formule de somme d'une suite géométrique » (p. 58)

### Assertion 7

> [!INDICATION]
> Le coefficient $1-x$ s'annule en $1$ : sur quels intervalles la théorie des équations différentielles linéaires s'applique-t-elle ?

> [!INDICATION]
> Une solution définie sur $\mathbb R$ tout entier peut aussi être proposée directement, à condition de vérifier le calcul pour tout réel $x$.

#### Solution

**VRAIE.** Sur tout intervalle $I$ de $\mathbb R\setminus\{1\}$, l'équation s'écrit $y'+\dfrac{1}{1-x}y=0$ ; une primitive de $x\mapsto\dfrac{1}{1-x}$ est $x\mapsto-\ln|1-x|$, donc les solutions sur $I$ sont les
$x\mapsto C|1-x|$, $C\in\mathbb R$. Considérons directement $f:\mathbb R\to\mathbb R$, $x\mapsto x-1$ : elle est dérivable sur $\mathbb R$ et vérifie, pour tout $x\in\mathbb R$,

$$
(1-x)f'(x)+f(x)=(1-x)\cdot1+(x-1)=0.
$$

C'est une solution définie sur $\mathbb R$ tout entier, non nulle.

> [!JURY]
> « se placer successivement sur les intervalles où la théorie générale est valide, avant d'étudier le recollement » (p. 58)

## Exercice 2 : Une suite d'intégrales

### Question 1

> [!INDICATION]
> Quel est le développement en série entière usuel à connaître ici ?

> [!INDICATION]
> Un rayon de convergence est un réel positif ou $+\infty$ — pas un ensemble ni un intervalle.

#### Solution

La fonction exponentielle est développable en série entière sur $\mathbb R$, de rayon de convergence $R=+\infty$, et

$$

\begin{aligned}
\forall x&\in\mathbb R,\\
e^x&=\sum_{n=0}^{+\infty}\frac{x^n}{n!}.
\end{aligned}

$$

$$
\boxed{R=+\infty}
$$

> [!JURY]
> « Un rayon de convergence est un réel positif ou $+\infty$, et non un ensemble ou un intervalle. » (p. 58)

### Question 2

> [!INDICATION]
> (a) Quelle est la primitive de $x\mapsto\frac{1}{x+1}$ ?

> [!INDICATION]
> (b) Décomposez la fraction rationnelle en éléments simples (inconnues $a$, $b$).

> [!INDICATION]
> (c) Intégrez terme à terme le résultat de (b).

#### Solution

**(a)**

$$

\begin{aligned}
I_1&=\int_0^1\frac{\mathrm dx}{x+1}\\
&=\bigl[\ln(1+x)\bigr]_0^1\\
&=\ln 2.
\end{aligned}

$$

$$
\boxed{I_1=
\ln 2}
$$

**(b)** On cherche $a,b$ tels que, pour tout $x\in[0,1]$,

$$
\frac{1}{(x+1)(x+2)}=\frac{a}{x+1}+\frac{b}{x+2},
$$

c'est-à-dire $1=a(x+2)+b(x+1)=(a+b)x+(2a+b)$. Par identification, $a+b=0$ et $2a+b=1$, d'où

$$
\boxed{a=1,\ b=-1}
$$

**(c)**

$$

\begin{aligned}
I_2&=\int_0^1\left(\frac{1}{x+1}-\frac{1}{x+2}\right)\mathrm dx\\
&=\bigl[\ln(1+x)-\ln(2+x)\bigr]_0^1\\
&=2\ln 2-\ln 3.
\end{aligned}

$$

$$
\boxed{I_2=2\ln 2-\ln 3}
$$

### Question 3

> [!INDICATION]
> (a) Comment encadrer $\prod_{k=1}^n(x+k)$ pour $x\in[0,1]$ ? Pensez au produit d'inégalités entre facteurs positifs, puis au passage à l'inverse et à l'intégrale.

> [!INDICATION]
> (b) Par quelle série de référence $I_n$ est-il dominé ? Sommez l'encadrement en reconnaissant $e$.

#### Solution

**(a)** Pour $x\in[0,1]$ et $k\in\llbracket1,n\rrbracket$, on a $k\le x+k\le k+1$, et tous ces facteurs sont positifs. Par produit de facteurs positifs,

$$

\begin{aligned}
n!=\prod_{k=1}^n k&\ \le\ \prod_{k=1}^n(x+k)\\
&\ \le\ \prod_{k=1}^n(k+1)=(n+1)!.
\end{aligned}

$$

Par passage à l'inverse (la fonction inverse est décroissante sur $]0,+\infty[$), puis par croissance de l'intégrale sur $[0,1]$ (segment de longueur $1$) :

$$

\begin{aligned}
\frac{1}{(n+1)!}&\le\frac{1}{\prod_{k=1}^n(x+k)}\le\frac{1}{n!},\\
\frac{1}{(n+1)!}&\le I_n\le\frac{1}{n!}.
\end{aligned}

$$

$$
\boxed{\frac{1}{(n+1)!}\le I_n\le\frac{1}{n!}}
$$

**(b)** La série $\sum\frac{1}{n!}$ converge (série exponentielle, de somme $e$). Comme $0\le I_n\le\frac{1}{n!}$, la série de terme général $I_n$ converge, par comparaison de séries à termes positifs. En sommant l'encadrement de (a) sur $n\ge0$ (séries convergentes à termes positifs) :

$$

\begin{aligned}
e-1=\sum_{n=0}^{+\infty}\frac{1}{(n+1)!}&\ \le\ \sum_{n=0}^{+\infty}I_n\\
&\ \le\ \sum_{n=0}^{+\infty}\frac{1}{n!}=e.
\end{aligned}

$$

$$
\boxed{\alpha=e\ \text{convient}}
$$

> [!PIEGE]
> Ne confondez pas la suite $(I_n)$ et la série $\sum I_n$ : montrer que $I_n\to0$ ne suffit pas à établir la convergence de la série.

> [!JURY]
> « Il a été souvent proposé un raisonnement par récurrence, qui ne convenait pas ici. » (p. 58)

> [!JURY]
> « La confusion entre la suite $(I_n)$ et la série de terme général $I_n$ est particulièrement fréquente. » (p. 58)

### Question 4

> [!INDICATION]
> (a) Quelle inégalité classique relie $1+t$ et $e^t$ (pensez à la convexité de $\exp$) ?

> [!INDICATION]
> (b) Pour montrer $t-t^2\le\ln(1+t)$ sur $[0,1]$, étudiez le signe d'une fonction auxiliaire — il ne suffit pas de vérifier en $0$ et en $1$.

#### Solution

**(a)** La fonction $\exp$ est convexe sur $\mathbb R$ (car $\exp''=\exp>0$), donc sa courbe est au-dessus de chacune de ses tangentes ; la tangente en $0$ a pour équation $y=1+x$. Ainsi :

$$
\boxed{\forall t\in[0,1],\quad 1+t\le e^{t}}
$$

**(b)** Soit $g:[0,1]\to\mathbb R$, $g(t)=\ln(1+t)-t+t^2$. Alors

$$

\begin{aligned}
g'(t)&=\frac{1}{1+t}-1+2t\\
&=\frac{t(2t+1)}{1+t}\ge0\qquad(t\in[0,1]),
\end{aligned}

$$

donc $g$ est croissante sur $[0,1]$, et $g(t)\ge g(0)=0$ : pour tout $t\in[0,1]$,

$$
t-t^2\le\ln(1+t).
$$

La fonction $\exp$ étant croissante sur $\mathbb R$, on en déduit, pour tout $t\in[0,1]$,

$$
\exp(t-t^2)\le\exp(\ln(1+t))=1+t.
$$

$$
\boxed{\forall t\in[0,1],\quad \exp(t-t^2)\le 1+t}
$$

### Question 5

> [!INDICATION]
> (a) Définition d'une série de Riemann et critère de convergence.

> [!INDICATION]
> (b) $(S_n)$ et $(H_n)$ sont-elles des suites de sommes partielles de séries de Riemann ? lesquelles ?

#### Solution

**(a)** Une série de Riemann est une série de la forme $\sum_{n\ge1}\dfrac{1}{n^{\alpha}}$ avec $\alpha\in\mathbb R$ ; elle converge si et seulement si $\alpha>1$.

**(b)** La suite $(S_n)$ est la suite des sommes partielles de la série de Riemann $\sum\frac{1}{n^2}$, pour laquelle $\alpha=2>1$ : cette série converge, donc $(S_n)$ converge.

**(c)** La suite $(H_n)$ est la suite des sommes partielles de la série de Riemann $\sum\frac{1}{n}$ ($\alpha=1$), qui diverge ; comme elle est à termes positifs, ses sommes partielles tendent vers $+\infty$ :

$$
\boxed{\lim_{n\to+\infty}H_n=+\infty}
$$

### Question 6

> [!INDICATION]
> (a) Factorisez $\prod_{k=1}^n(x+k)$ pour faire apparaître $1+\frac{x}{k}$, puis appliquez la question 4 à $t=\frac{x}{k}$.

> [!INDICATION]
> (b) Sur $[0,1]$, $x^2\le x$ : servez-vous-en pour minorer $xH_n-x^2S_n$, puis passez à l'inverse (pensez au signe).

> [!INDICATION]
> (c) Intégrez l'encadrement de (b) ; la primitive de $x\mapsto e^{-\lambda x}$ se calcule directement.

> [!INDICATION]
> (d) Multipliez par $n!H_n$ et faites tendre $n\to+\infty$ : théorème d'encadrement.

#### Solution

**(a)** Pour $x\in[0,1]$,

$$

\begin{aligned}
\prod_{k=1}^n(x+k)&=\prod_{k=1}^n k\Bigl(1+\frac{x}{k}\Bigr)\\
&=n!\prod_{k=1}^n\Bigl(1+\frac{x}{k}\Bigr).
\end{aligned}

$$

Pour chaque $k\in\llbracket1,n\rrbracket$, on a $t=\frac{x}{k}\in[0,1]$, donc d'après la question 4 :

$$
\exp\Bigl(\frac{x}{k}-\frac{x^2}{k^2}\Bigr)\le 1+\frac{x}{k}\le\exp\Bigl(\frac{x}{k}\Bigr).
$$

Tous les membres étant positifs, on multiplie ces inégalités pour $k=1,\dots,n$, ce qui donne, en reconnaissant $H_n$ et $S_n$ :

$$

\begin{aligned}
n!\exp\bigl(xH_n-x^2S_n\bigr)&\le\prod_{k=1}^n(x+k)\\
&\le n!\exp(xH_n).
\end{aligned}

$$

**(b)** Pour $x\in[0,1]$, on a $x^2\le x$, donc $x^2S_n\le xS_n$ (car $S_n\ge0$), d'où $xH_n-x^2S_n\ge x(H_n-S_n)$. Par croissance de $\exp$, puis passage à l'inverse (fonction décroissante sur
$]0,+\infty[$), on obtient :

$$

\begin{aligned}
\frac{1}{n!}\exp(-xH_n)&\le\frac{1}{\prod_{k=1}^n(x+k)}\\
&\le\frac{1}{n!}\exp\bigl(-x(H_n-S_n)\bigr).
\end{aligned}

$$

**(c)** Par croissance de l'intégrale sur $[0,1]$ (les fonctions sont positives) :

$$

\begin{aligned}
\frac{1}{n!}\int_0^1 e^{-xH_n}\,\mathrm dx&\le I_n\\
&\le\frac{1}{n!}\int_0^1 e^{-x(H_n-S_n)}\,\mathrm dx,
\end{aligned}

$$

et, pour $\lambda>0$, $\int_0^1 e^{-\lambda x}\,\mathrm dx=\dfrac{1-e^{-\lambda}}{\lambda}$ (ici $\lambda=H_n>0$ et, pour $n\ge2$, $\lambda=H_n-S_n>0$ ; le cas $n=1$ se vérifie directement :
$1-e^{-1}\le I_1=\ln2\le1$). D'où

$$
\boxed{\forall n\ge2,\quad \frac{1-e^{-H_n}}{n!H_n}\le I_n\le\frac{1-e^{-(H_n-S_n)}}{n!(H_n-S_n)}}
$$

**(d)** Multiplions l'encadrement de (c) par $n!H_n>0$ :

$$

\begin{aligned}
1-e^{-H_n}&\le n!H_nI_n\\
&\le\frac{H_n}{H_n-S_n}\bigl(1-e^{-(H_n-S_n)}\bigr).
\end{aligned}

$$

Quand $n\to+\infty$ : $H_n\to+\infty$ et $(S_n)$ converge, donc $H_n-S_n\to+\infty$ ; ainsi $e^{-H_n}\to0$, $e^{-(H_n-S_n)}\to0$, et

$$
\frac{H_n}{H_n-S_n}=\frac{1}{1-S_n/H_n}\xrightarrow[n\to+\infty]{}1.
$$

Les deux bornes tendent vers $1$ ; par le théorème d'encadrement,

$$
\boxed{I_n\sim\frac{1}{n!H_n}}
$$

> [!PIEGE]
> Toute manipulation d'inégalité (multiplication, passage à l'inverse, composition par $\exp$) exige un argument de signe ou de monotonie ; la fonction inverse n'est décroissante que sur $]0,+\infty[$, pas sur $\mathbb R^*$.

> [!JURY]
> « L'argument de signe nécessaire aux manipulations d'inégalités est très souvent absent. » (p. 59)

> [!METHODE]
> Pour encadrer un produit $\prod(x+k)$, on factorise pour faire apparaître des $1+\frac{x}{k}$, on applique une inégalité connue à chaque facteur (en justifiant le signe), puis on multiplie.

### Question 7

> [!INDICATION]
> (a) Écrivez $\ln n$ comme une somme d'intégrales sur les $[k,k+1]$ pour faire apparaître $u_n$.

> [!INDICATION]
> (b) Majorez chaque terme $\frac1k-\int_k^{k+1}\frac{\mathrm dt}{t}$ grâce à la monotonie de $t\mapsto\frac1t$ ; calculez $u_{n+1}-u_n$.

> [!INDICATION]
> (c) Limite monotone, puis réécrivez $\frac{H_n}{\ln n}$ à l'aide de $u_n$ ; concluez sur l'équivalent de $I_n$.

#### Solution

**(a)** Pour $n\ge2$, on écrit $\ln n=\int_1^n\frac{\mathrm dt}{t}=\sum_{k=1}^{n-1}\int_k^{k+1}\frac{\mathrm dt}{t}$, d'où

$$

\begin{aligned}
u_n&=H_n-\ln n\\
&=\frac1n+\sum_{k=1}^{n-1}\Bigl(\frac1k-\int_k^{k+1}\frac{\mathrm dt}{t}\Bigr).
\end{aligned}

$$

**(b)** La fonction $t\mapsto\frac1t$ est décroissante sur $\mathbb R_+^*$. Pour $t\in[k,k+1]$, on a $\frac1t\le\frac1k$, donc $\frac1k-\int_k^{k+1}\frac{\mathrm dt}{t}\ge0$ : chaque terme de la somme est positif, et $\frac1n>0$, d'où
$u_n\ge0$. De plus

$$
u_{n+1}-u_n=\frac{1}{n+1}-\int_n^{n+1}\frac{\mathrm dt}{t}\le0,
$$

car $\int_n^{n+1}\frac{\mathrm dt}{t}\ge\frac{1}{n+1}$. La suite $(u_n)_{n\ge2}$ est donc décroissante et à valeurs positives.

**(c)** Par le théorème de la limite monotone, $(u_n)_{n\ge2}$ converge, donc elle est bornée. Alors

$$
\frac{H_n}{\ln n}=1+\frac{u_n}{\ln n}\xrightarrow[n\to+\infty]{}1,
$$

puisque $\ln n\to+\infty$. Donc $H_n\sim\ln n$, et en composant avec l'équivalent de la question 6(d) :

$$
\boxed{I_n\sim\frac{1}{n!\ln n}}
$$

> [!JURY]
> « Les arguments de passage à la limite doivent être explicités. » (p. 59)

## Exercice 3 : Puissances universelles

#### Première partie — dans $\mathbb Z/n\mathbb Z$

### Question 1 (cas $n=6$)

#### Solution

**(a)** Dans $\mathbb Z/6\mathbb Z$ :

$$

\begin{aligned}
\overline{2}^{2}&=\overline{4}, & \overline{3}^{2}&=\overline{9}=\overline{3},\\
\overline{4}^{2}&=\overline{16}=\overline{4}, & \overline{5}^{2}&=\overline{25}=\overline{1}.
\end{aligned}

$$

**(b)** Comme $\overline{3}^{2}=\overline{3}$, une récurrence immédiate donne $\overline{3}^{\,k}=\overline{3}$ pour tout $k\in\mathbb N^*$ (de même $\overline{4}^{\,k}=\overline{4}$). Ainsi, pour tout $k\in\mathbb N^*$, $\overline{3}=(\overline{3})^k$ est une puissance
$k$-ième : $\overline{3}$ est une puissance universelle.

$$
\boxed{\text{$\overline{0}$ et $\overline{1}$ ne sont pas les seules puissances universelles de }\mathbb Z/6\mathbb Z}
$$

### Question 2 (cas $n=4$)

#### Solution

Dans $\mathbb Z/4\mathbb Z$ : $\overline{0}^{2}=\overline{0}$, $\overline{1}^{2}=\overline{1}$, $\overline{2}^{2}=\overline{0}$, $\overline{3}^{2}=\overline{1}$. L'ensemble des carrés est donc $\{\overline{0},\overline{1}\}$. Or une puissance universelle est en particulier une puissance
$2$-ième (un carré) : ni $\overline{2}$ ni $\overline{3}$ n'en est une.

$$
\boxed{\text{Les seules puissances universelles de }\mathbb Z/4\mathbb Z\text{ sont }\overline{0}\text{ et }\overline{1}.}
$$

### Question 3 (cas $p$ premier)

#### Solution

**(a)** Petit théorème de Fermat : si $p$ est premier, alors pour tout entier $b$, $b^{p}\equiv b\pmod p$ ; et si $p\nmid b$, alors $b^{p-1}\equiv1\pmod p$.

**(b)** Dans $\mathbb Z/p\mathbb Z$, la première forme s'écrit $\overline{a}^{\,p}=\overline{a}$ pour tout $\overline{a}$ : tout élément de $\mathbb Z/p\mathbb Z$ est une puissance $p$-ième (de lui-même). Soit $\overline{a}$ une puissance universelle ; c'est en particulier une puissance
$(p-1)$-ième : $\overline{a}=\overline{x}^{\,p-1}$. Si $\overline{a}\neq\overline{0}$, alors $\overline{x}\neq\overline{0}$, donc $p\nmid x$, et la seconde forme donne $\overline{a}=\overline{x}^{\,p-1}=\overline{1}$. Réciproquement,
$\overline{0}$ et $\overline{1}$ sont des puissances universelles.

$$
\boxed{\text{Les seules puissances universelles de }\mathbb Z/p\mathbb Z\text{ sont }\overline{0}\text{ et }\overline{1}.}
$$

**(c)** **Non** : l'hypothèse « $n$ premier » n'est pas nécessaire, seulement suffisante. La question 2 en fournit un contre-exemple : $4$ n'est pas premier, et pourtant $\overline{0}$ et $\overline{1}$ sont les seules puissances universelles de $\mathbb Z/4\mathbb Z$.

#### Deuxième partie — dans $\mathcal M_n(\mathbb R)$

### Question 4 (cas $n=1$)

#### Solution

Soit $a\in\mathbb R$. Si $a$ est une puissance universelle, c'est en particulier un carré : $a=x^2\ge0$. Réciproquement, si $a\ge0$, alors pour tout $k\in\mathbb N^*$, $a=\bigl(a^{1/k}\bigr)^k$ avec
$a^{1/k}\ge0$.

$$
\boxed{\text{L'ensemble des puissances universelles de }\mathbb R\text{ est }\mathbb R_+=[0,+\infty[}
$$

### Question 5

> [!INDICATION]
> (a) Que vaut $(PNP^{-1})^k$ en fonction de $N^k$ ?

> [!INDICATION]
> (b) Faites jouer le même argument avec $P^{-1}$ à la place de $P$, pour chaque $k$ fixé — la matrice cherchée peut dépendre de $k$.

#### Solution

**(a)** Si $N^k=D$, alors par télescopage $(PNP^{-1})^k=PN^kP^{-1}=PDP^{-1}=A$.

**(b)** Soit $k\in\mathbb N^*$. Si $D=N^k$, alors d'après (a), $A=(PNP^{-1})^k$ est une puissance $k$-ième. Réciproquement, comme $D=P^{-1}AP$, si $A=M^k$, alors
$D=(P^{-1}MP)^k$. Ces équivalences valant pour chaque $k$ :

$$
\boxed{A\text{ est une puissance universelle }\iff D\text{ l'est}}
$$

> [!PIEGE]
> Attention aux quantificateurs : « pour tout $k$, il existe $M$ » n'équivaut pas à $A^k=A$ pour tout $k$.

> [!JURY]
> dans une assertion « pour tout $k$, il existe $M$… », « la matrice $M$ peut dépendre de $k$ » (p. 60)

### Question 6

> [!INDICATION]
> (a) Écrivez l'égalité $DM=MD$ coefficient par coefficient ; les $\lambda_i$ distincts annulent les termes hors diagonale.

> [!INDICATION]
> (b) Si $M^k=D$, alors $M$ commute avec $D$ : concluez que $M$ est diagonale et ramenez-vous à $\mu_i^k=\lambda_i$.

> [!INDICATION]
> (c) Une matrice à $n$ valeurs propres réelles distinctes est diagonalisable ; combinez 5(b) et 6(b).

#### Solution

**(a)** Écrivons $D=(d_{ij})$ avec $d_{ii}=\lambda_i$, $d_{ij}=0$ si $i\neq j$, et $M=(m_{ij})$. Alors

$$
(DM)_{ij}=\lambda_i m_{ij},\ (MD)_{ij}=m_{ij}\lambda_j.
$$

Si $DM=MD$, alors $m_{ij}(\lambda_i-\lambda_j)=0$ pour tous $i,j$ ; pour $i\neq j$, $\lambda_i\neq\lambda_j$, donc $m_{ij}=0$ :
$M$ est diagonale.

**(b)** Si $M^k=D$, alors $MD=M^{k+1}=DM$ : $M$ commute avec $D$, donc est diagonale d'après (a), $M=\mathrm{diag}(\mu_1,\dots,\mu_n)$, et $M^k=D\iff\mu_i^k=\lambda_i$ pour tout
$i$. Ainsi $D$ est une puissance $k$-ième si et seulement si chaque $\lambda_i$ est une puissance $k$-ième dans $\mathbb R$. En faisant varier
$k$ (en particulier $k=2$) et d'après la question 4 :

$$
\boxed{D\text{ est une puissance universelle }\iff \forall i,\ \lambda_i\ge0}
$$

**(c)** $A$ admet $n$ valeurs propres réelles deux à deux distinctes : elle est diagonalisable, $A=PDP^{-1}$ avec $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$ et les $\lambda_i$ distincts. D'après 5(b) et 6(b) :

$$
\boxed{A\text{ est une puissance universelle }\iff\text{ toutes ses valeurs propres sont positives ou nulles}}
$$

### Question 7

> [!INDICATION]
> (a) Récurrence sur $k$ à $\theta$ fixé, avec les formules d'addition ; quelle est l'interprétation géométrique de $R_\theta$ ?

> [!INDICATION]
> (b) $R_\pi$ vaut $-I_2$ ; cherchez une racine $k$-ième dans la famille des $R_\theta$.

#### Solution

**(a)** Fixons $\theta\in\mathbb R$. Montrons par récurrence sur $k\in\mathbb N^*$ que $(R_\theta)^k=R_{k\theta}$. L'initialisation $k=1$ est claire. Si $(R_\theta)^k=R_{k\theta}$, alors, par les formules d'addition :

$$

\begin{aligned}
(R_\theta)^{k+1}=R_{k\theta}R_\theta
&=\begin{pmatrix}\cos k\theta&-\sin k\theta\\ \sin k\theta&\cos k\theta\end{pmatrix}
\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}\\
&=R_{(k+1)\theta}.
\end{aligned}

$$

**Interprétation géométrique** : dans une base orthonormée directe de $\mathbb R^2$, $R_\theta$ est la matrice de la rotation vectorielle d'angle $\theta$ ; composer $k$ rotations d'angle $\theta$ donne la rotation d'angle $k\theta$.

**(b)** On a $R_\pi=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=-I_2$. Pour tout $k\in\mathbb N^*$, d'après (a), $(R_{\pi/k})^k=R_{k\pi/k}=R_\pi$.

$$
\boxed{R_\pi\text{ est une puissance universelle}}
$$

> [!JURY]
> « l'interprétation géométrique demandée a été souvent omise » (p. 60)

### Question 8

> [!INDICATION]
> L'hypothèse « coefficients deux à deux distincts » était-elle utilisée de façon cruciale en 6(b) ?

> [!INDICATION]
> Testez la matrice $-I_2$ : ses coefficients diagonaux sont négatifs — est-elle malgré tout puissance universelle ?

#### Solution

**La propriété proposée est fausse.** La matrice $R_\pi=\mathrm{diag}(-1,-1)$ est diagonale, à coefficients diagonaux égaux à $-1<0$, et pourtant elle est une puissance universelle d'après la question 7(b). L'hypothèse « coefficients deux à deux distincts » de la question 6(b) était indispensable : ici $-I_2$ commute avec toute matrice, donc l'argument de 6(a) ne s'applique plus.

## Exercice 4 : Tous à 6

### Question 1

> [!INDICATION]
> Suite arithmético-géométrique : déterminez le point fixe, puis rendez la suite géométrique.

#### Solution

Le point fixe $\ell$ vérifie $\ell=\frac56\ell+\frac16$, d'où $\ell=1$. Posons $v_n=p_n-1$. Alors

$$

\begin{aligned}
v_{n+1}&=p_{n+1}-1=\frac56p_n+\frac16-1\\
&=\frac56(p_n-1)=\frac56 v_n.
\end{aligned}

$$

$(v_n)$ est géométrique de raison $\frac56$ et de premier terme $v_1=p_1-1=-\frac56$, donc $v_n=-\left(\frac56\right)^n$ pour $n\ge1$.

$$
\boxed{p_n=1-\left(\frac56\right)^{n}\qquad(n\in\mathbb N^*)}
$$

> [!JURY]
> « La méthode d'étude des suites arithmético-géométriques, pourtant explicitement au programme du CAPES, n'est pas assez souvent maîtrisée. » (p. 60)

### Question 2

> [!INDICATION]
> (a) Quelles valeurs $S_n$ peut-il prendre ?

> [!INDICATION]
> (b) Pour identifier une loi binomiale, quelles conditions faut-il vérifier et expliciter (nombre d'épreuves, indépendance, probabilité commune) ?

#### Solution

**(a)** Après $n$ lancers, le nombre de dés ayant donné 6 est un entier entre $0$ et $N$ :

$$
\boxed{S_n(\Omega)=\llbracket0,N\rrbracket}
$$

**(b)** Au premier lancer, on répète $N$ fois, de façon indépendante, la même épreuve de Bernoulli de succès « obtenir 6 », de probabilité $\frac16$ ; $S_1$ compte le nombre de succès. Donc

$$
\boxed{S_1\sim\mathcal B\Bigl(N,\frac16\Bigr)}
$$

> [!JURY]
> pour identifier une loi binomiale, « il convient de vérifier et d'expliciter le nombre d'épreuves, leur indépendance et la probabilité commune de succès » (p. 60)

### Question 3

> [!INDICATION]
> Sachant $S_n=i$, combien de dés relance-t-on ? La loi du nombre de nouveaux « 6 » est-elle binomiale ?

#### Solution

Sachant $\{S_n=i\}$, il reste $N-i$ dés à relancer, et le nombre de nouveaux « 6 » parmi eux suit $\mathcal B(N-i,\frac16)$. Obtenir $S_{n+1}=k$ exige exactement $k-i$ nouveaux succès, donc pour $i\in\llbracket0,k\rrbracket$ :

$$

\begin{aligned}
P(S_{n+1}=k\mid S_n=i)&\\
&=\binom{N-i}{k-i}\Bigl(\frac16\Bigr)^{k-i}\Bigl(\frac56\Bigr)^{N-k}.
\end{aligned}

$$

**Résultat :** $P(S_{n+1}=k\mid S_n=i)=\binom{N-i}{k-i}\bigl(\frac16\bigr)^{k-i}\bigl(\frac56\bigr)^{N-k}$.

> [!JURY]
> « Les notations $S_n$, $S_n=k$ et $P(S_n=k)$ désignent des objets de nature différente » (p. 60)

### Question 4

> [!INDICATION]
> (a) Formule des probabilités totales avec le système complet $\bigl((S_n=i)\bigr)_{i\in[\![0,N]\!]}$ — l'indice $i$ varie d'abord de $0$ à $N$.

> [!INDICATION]
> (b) Transformez le produit $\binom{N}{i}\binom{N-i}{k-i}$ en $\binom{N}{k}\binom{k}{i}$.

> [!INDICATION]
> (c) Factorisez les termes indépendants de $i$ et reconnaissez la formule du binôme dans la somme sur $i$.

#### Solution

**(a)** La famille $\bigl((S_n=i)\bigr)_{i\in\llbracket0,N\rrbracket}$ est un système complet d'événements. Par la formule des probabilités totales, avec $S_n\sim\mathcal B(N,p_n)$ et la question 3 (les termes $i>k$ sont nuls) :

$$

\begin{aligned}
P(S_{n+1}=k)&=\sum_{i=0}^{N}P(S_n=i)\,P(S_{n+1}=k\mid S_n=i)\\
&=\sum_{i=0}^{k}\binom{N}{i}p_n^{\,i}(1-p_n)^{N-i}\binom{N-i}{k-i}\frac{1}{6^{k-i}}\Bigl(\frac56\Bigr)^{N-k}.
\end{aligned}

$$

**(b)** Pour $i\in\llbracket0,k\rrbracket$ :

$$

\begin{aligned}
\binom{N}{i}\binom{N-i}{k-i}
&=\frac{N!}{i!(N-i)!}\cdot\frac{(N-i)!}{(k-i)!(N-k)!}\\
&=\frac{N!}{i!(k-i)!(N-k)!}\\
&=\binom{N}{k}\binom{k}{i}.
\end{aligned}

$$

$$
\boxed{\binom{N}{i}\binom{N-i}{k-i}=\binom{N}{k}\binom{k}{i}}
$$

**(c)** En injectant (b) et en factorisant les termes indépendants de $i$ :

$$

\begin{aligned}
P(S_{n+1}=k)&=\binom{N}{k}\Bigl(\frac56\Bigr)^{N-k}(1-p_n)^{N-k}
\sum_{i=0}^{k}\binom{k}{i}p_n^{\,i}\Bigl(\frac{1-p_n}{6}\Bigr)^{k-i}\\
&=\binom{N}{k}\Bigl(\frac56(1-p_n)\Bigr)^{N-k}\Bigl(p_n+\frac{1-p_n}{6}\Bigr)^{k}.
\end{aligned}

$$

Or $p_n+\frac{1-p_n}{6}=\frac{1+5p_n}{6}$ et $\frac56(1-p_n)=1-\frac{1+5p_n}{6}$. Donc

$$
\boxed{P(S_{n+1}=k)=\binom{N}{k}\Bigl(\frac{1+5p_n}{6}\Bigr)^{k}\Bigl(1-\frac{1+5p_n}{6}\Bigr)^{N-k}}
$$

> [!PIEGE]
> Dans la formule des probabilités totales, l'indice de sommation porte d'abord sur toutes les valeurs possibles de $S_n$, pas seulement sur celles compatibles avec $k$.

> [!JURY]
> « l'indice $i$ de la somme devait, dans un premier temps, varier de $0$ à $N$ et non de $0$ à $k$ » (p. 60)

### Question 5

> [!INDICATION]
> Récurrence : initialisation par la question 2(b), hérédité par 4(c) ; vérifiez que $\frac{1+5p_n}{6}=p_{n+1}$.

#### Solution

Montrons par récurrence sur $n\in\mathbb N^*$ que $S_n\sim\mathcal B\bigl(N,1-(\frac56)^n\bigr)$. *Initialisation* : $S_1\sim\mathcal B(N,\frac16)$ (question 2) et $1-\frac56=\frac16$. *Hérédité* : si $S_n\sim\mathcal B(N,p_n)$ avec $p_n=1-(\frac56)^n$, alors par 4(c),
$S_{n+1}$ suit une loi binomiale de premier paramètre $N$ et de second paramètre $\frac{1+5p_n}{6}$, et

$$
\frac{1+5p_n}{6}=1-\Bigl(\frac56\Bigr)^{n+1}.
$$

$$
\boxed{\forall n\in\mathbb N^*,\quad S_n\sim\mathcal B\Bigl(N,1-\Bigl(\frac56\Bigr)^{n}\Bigr)}
$$

> [!METHODE]
> Pour montrer qu'une variable aléatoire suit une loi binomiale par récurrence, on conditionne par la valeur précédente et on reconnaît la formule du binôme.

### Question 6

> [!INDICATION]
> (a) L'événement $\{1\le T\le n\}$ est égal à $\{S_n=N\}$ ; appliquez la loi de $S_n$.

> [!INDICATION]
> (b) Les $\{T=k\}$ sont deux à deux incompatibles : passez à la limite sur les sommes partielles, puis utilisez $\sum_{k\ge0}P(T=k)=1$.

#### Solution

**(a)** L'événement $\{1\le T\le n\}$ signifie que tous les dés ont donné 6 au plus tard au $n$-ième lancer, c'est-à-dire $\{S_n=N\}$ (avec la convention de l'énoncé). Comme $S_n\sim\mathcal B(N,p_n)$ avec $p_n=1-(\frac56)^n$ :

$$

\begin{aligned}
P(1\le T\le n)&=P(S_n=N)\\
&=\Bigl(1-\Bigl(\frac56\Bigr)^{n}\Bigr)^{N}.
\end{aligned}

$$

**Résultat :** $P(1\le T\le n)=\bigl(1-(\frac56)^n\bigr)^N$.

**(b)** Les événements $\{T=k\}$, $k\in\mathbb N^*$, sont deux à deux incompatibles et $\bigsqcup_{k=1}^{n}\{T=k\}=\{1\le T\le n\}$, donc

$$

\begin{aligned}
\sum_{k=1}^{n}P(T=k)&=P(1\le T\le n)=\Bigl(1-\Bigl(\frac56\Bigr)^{n}\Bigr)^{N}\\
&\xrightarrow[n\to+\infty]{}1.
\end{aligned}

$$

La série $\sum P(T=k)$ converge et
**On obtient** $\sum_{k=1}^{+\infty}P(T=k)=1$.
Comme $T$ est à valeurs dans $\mathbb N$, $\sum_{k=0}^{+\infty}P(T=k)=1$, d'où

$$
\boxed{P(T=0)=0}
$$
\ \textbf{Interprétation} : presque sûrement, le joueur finit par amener tous les dés sur 6.

> [!JURY]
> « Les questions suivantes ont été peu abordées. » (p. 60)

## Bilan

Méthodes à retenir : linéariser avant d'intégrer ; nommer chaque propriété utilisée en précisant ses hypothèses de signe et de monotonie ; distinguer suite et série, événement et probabilité, point et vecteur ; en probabilités, vérifier explicitement les trois ingrédients d'une loi binomiale (nombre d'épreuves, indépendance, probabilité commune) ; dans $\mathbb Z/n\mathbb Z$, calculer les carrés avant de conclure ; pour les matrices, le commutant d'une matrice diagonale à valeurs propres deux à deux distinctes est l'ensemble des matrices diagonales.

Questions classiques transposables : équivalents de suites d'intégrales par encadrement exponentiel ; sommes géométriques de racines $n$-ièmes de l'unité ; puissances $k$-ièmes dans un anneau puis dans $\mathcal M_n(\mathbb R)$ ; loi binomiale dans un processus de dés relancés.

Pièges relevés par le jury 2026 (p. 57-60) : confusion suite/série, développement limité vs série entière, séries de Riemann vs sommes de Riemann, oubli de la condition sur la raison d'une somme géométrique, quantificateurs mal lus (« pour tout $k$, il existe $x$ » vs « pour tout $k$, $a^k=a$ »), arguments de signe absents dans les manipulations d'inégalités.
