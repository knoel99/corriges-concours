# CAPES Maths — Épreuve d'admissibilité 1 (bac+3) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Exercice 1 : Vrai/Faux

### Assertion 1

**FAUSSE.** Prenons $f:\mathbb R\to\mathbb R$, $x\mapsto x^3$, dérivable sur $\mathbb R$, et $a=0$. On a $f'(x)=3x^2$, donc $f'(0)=0$. Pourtant, pour tout
$\varepsilon>0$ :

$$

\begin{aligned}
f(\varepsilon)&=\varepsilon^3>0=f(0),\\
f(-\varepsilon)&=-\varepsilon^3<0=f(0).
\end{aligned}

$$

Dans tout voisinage de $0$, $f$ prend des valeurs strictement supérieures et strictement inférieures à $f(0)$ : $f$ n'admet en $0$ ni maximum ni minimum local.

### Assertion 2

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

### Assertion 4

**VRAIE.** Soit $P\in\mathbb R[X]$ de degré impair $n$, de coefficient dominant $c\neq0$. La fonction polynomiale $P$ est continue sur $\mathbb R$. Si $c>0$, alors
$\lim_{x\to+\infty}P(x)=+\infty$ et, comme $n$ est impair, $\lim_{x\to-\infty}P(x)=-\infty$ ; si $c<0$, on applique ce qui précède à $-P$. Dans les deux cas, $P$ prend des valeurs de signes contraires, donc par le théorème des valeurs intermédiaires il existe
$x\in\mathbb R$ tel que $P(x)=0$.

### Assertion 5

**VRAIE.** Posons $\varphi(P,Q)=P(0)Q(0)+P(1)Q(1)$ sur $\mathbb R_1[X]$. La bilinéarité et la symétrie sont immédiates (les évaluations en $0$ et en $1$ sont linéaires, et le produit de $\mathbb R$ est commutatif). Positivité : $\varphi(P,P)=P(0)^2+P(1)^2\ge0$. Caractère défini : si
$\varphi(P,P)=0$, alors $P(0)^2+P(1)^2=0$, somme de deux réels positifs, donc $P(0)=P(1)=0$ ; un polynôme de degré au plus $1$ ayant deux racines distinctes est nul. Ainsi $\varphi$ est une forme bilinéaire symétrique définie positive : c'est un produit scalaire.

### Assertion 6

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

### Assertion 7

**VRAIE.** Sur tout intervalle $I$ de $\mathbb R\setminus\{1\}$, l'équation s'écrit $y'+\dfrac{1}{1-x}y=0$ ; une primitive de $x\mapsto\dfrac{1}{1-x}$ est $x\mapsto-\ln|1-x|$, donc les solutions sur $I$ sont les
$x\mapsto C|1-x|$, $C\in\mathbb R$. Considérons directement $f:\mathbb R\to\mathbb R$, $x\mapsto x-1$ : elle est dérivable sur $\mathbb R$ et vérifie, pour tout $x\in\mathbb R$,

$$
(1-x)f'(x)+f(x)=(1-x)\cdot1+(x-1)=0.
$$

C'est une solution définie sur $\mathbb R$ tout entier, non nulle.

## Exercice 2 : Une suite d'intégrales

### Question 1

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

### Question 2

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

### Question 4

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

**(a)** Une série de Riemann est une série de la forme $\sum_{n\ge1}\dfrac{1}{n^{\alpha}}$ avec $\alpha\in\mathbb R$ ; elle converge si et seulement si $\alpha>1$.

**(b)** La suite $(S_n)$ est la suite des sommes partielles de la série de Riemann $\sum\frac{1}{n^2}$, pour laquelle $\alpha=2>1$ : cette série converge, donc $(S_n)$ converge.

**(c)** La suite $(H_n)$ est la suite des sommes partielles de la série de Riemann $\sum\frac{1}{n}$ ($\alpha=1$), qui diverge ; comme elle est à termes positifs, ses sommes partielles tendent vers $+\infty$ :

$$
\boxed{\lim_{n\to+\infty}H_n=+\infty}
$$

### Question 6

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

### Question 7

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

## Exercice 3 : Puissances universelles

#### Première partie — dans $\mathbb Z/n\mathbb Z$

### Question 1 (cas $n=6$)

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

Dans $\mathbb Z/4\mathbb Z$ : $\overline{0}^{2}=\overline{0}$, $\overline{1}^{2}=\overline{1}$, $\overline{2}^{2}=\overline{0}$, $\overline{3}^{2}=\overline{1}$. L'ensemble des carrés est donc $\{\overline{0},\overline{1}\}$. Or une puissance universelle est en particulier une puissance
$2$-ième (un carré) : ni $\overline{2}$ ni $\overline{3}$ n'en est une.

$$
\boxed{\text{Les seules puissances universelles de }\mathbb Z/4\mathbb Z\text{ sont }\overline{0}\text{ et }\overline{1}.}
$$

### Question 3 (cas $p$ premier)

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

Soit $a\in\mathbb R$. Si $a$ est une puissance universelle, c'est en particulier un carré : $a=x^2\ge0$. Réciproquement, si $a\ge0$, alors pour tout $k\in\mathbb N^*$, $a=\bigl(a^{1/k}\bigr)^k$ avec
$a^{1/k}\ge0$.

$$
\boxed{\text{L'ensemble des puissances universelles de }\mathbb R\text{ est }\mathbb R_+=[0,+\infty[}
$$

### Question 5

**(a)** Si $N^k=D$, alors par télescopage $(PNP^{-1})^k=PN^kP^{-1}=PDP^{-1}=A$.

**(b)** Soit $k\in\mathbb N^*$. Si $D=N^k$, alors d'après (a), $A=(PNP^{-1})^k$ est une puissance $k$-ième. Réciproquement, comme $D=P^{-1}AP$, si $A=M^k$, alors
$D=(P^{-1}MP)^k$. Ces équivalences valant pour chaque $k$ :

$$
\boxed{A\text{ est une puissance universelle }\iff D\text{ l'est}}
$$

### Question 6

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

### Question 8

**La propriété proposée est fausse.** La matrice $R_\pi=\mathrm{diag}(-1,-1)$ est diagonale, à coefficients diagonaux égaux à $-1<0$, et pourtant elle est une puissance universelle d'après la question 7(b). L'hypothèse « coefficients deux à deux distincts » de la question 6(b) était indispensable : ici $-I_2$ commute avec toute matrice, donc l'argument de 6(a) ne s'applique plus.

## Exercice 4 : Tous à 6

### Question 1

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

### Question 2

**(a)** Après $n$ lancers, le nombre de dés ayant donné 6 est un entier entre $0$ et $N$ :

$$
\boxed{S_n(\Omega)=\llbracket0,N\rrbracket}
$$

**(b)** Au premier lancer, on répète $N$ fois, de façon indépendante, la même épreuve de Bernoulli de succès « obtenir 6 », de probabilité $\frac16$ ; $S_1$ compte le nombre de succès. Donc

$$
\boxed{S_1\sim\mathcal B\Bigl(N,\frac16\Bigr)}
$$

### Question 3

Sachant $\{S_n=i\}$, il reste $N-i$ dés à relancer, et le nombre de nouveaux « 6 » parmi eux suit $\mathcal B(N-i,\frac16)$. Obtenir $S_{n+1}=k$ exige exactement $k-i$ nouveaux succès, donc pour $i\in\llbracket0,k\rrbracket$ :

$$

\begin{aligned}
P(S_{n+1}=k\mid S_n=i)&\\
&=\binom{N-i}{k-i}\Bigl(\frac16\Bigr)^{k-i}\Bigl(\frac56\Bigr)^{N-k}.
\end{aligned}

$$

**Résultat :** $P(S_{n+1}=k\mid S_n=i)=\binom{N-i}{k-i}\bigl(\frac16\bigr)^{k-i}\bigl(\frac56\bigr)^{N-k}$.

### Question 4

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

### Question 5

Montrons par récurrence sur $n\in\mathbb N^*$ que $S_n\sim\mathcal B\bigl(N,1-(\frac56)^n\bigr)$. *Initialisation* : $S_1\sim\mathcal B(N,\frac16)$ (question 2) et $1-\frac56=\frac16$. *Hérédité* : si $S_n\sim\mathcal B(N,p_n)$ avec $p_n=1-(\frac56)^n$, alors par 4(c),
$S_{n+1}$ suit une loi binomiale de premier paramètre $N$ et de second paramètre $\frac{1+5p_n}{6}$, et

$$
\frac{1+5p_n}{6}=1-\Bigl(\frac56\Bigr)^{n+1}.
$$

$$
\boxed{\forall n\in\mathbb N^*,\quad S_n\sim\mathcal B\Bigl(N,1-\Bigl(\frac56\Bigr)^{n}\Bigr)}
$$

### Question 6

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
