# BCE ECG — Maths appliquées (emlyon) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures, sans calculatrice ni document. Les bibliothèques Python sont importées sous les noms `np`, `rd` et `plt`.

## Exercice 1 — Partie A : Étude d'une fonction de deux variables

### Question 1

**a)** Sur l'ouvert $\mathcal D$, on a $1+xy>0$ et $f$ est de classe $\mathcal C^2$ (composée et somme de fonctions de classe $\mathcal C^2$). Pour $(x,y)\in\mathcal D$ :

$$\begin{aligned}\partial_1f(x,y)&=1+\frac{y}{1+xy},\\\partial_2f(x,y)&=\frac{x}{1+xy}.\end{aligned}$$

Donc

$$\boxed{\nabla f(x,y)=\begin{pmatrix}1+\dfrac{y}{1+xy}\\[2mm]\dfrac{x}{1+xy}\end{pmatrix}.}$$

**b)** $(x,y)\in\mathcal D$ est un point critique si et seulement si $\nabla f(x,y)=0$.

- La seconde équation $\frac{x}{1+xy}=0$ donne $x=0$.
- La première devient alors $1+y=0$, soit $y=-1$.

Réciproquement, $(0,-1)\in\mathcal D$ car $1+0\times(-1)=1>0$, et le gradient y est nul. **$f$ admet un unique point critique : $(x_0,y_0)=(0,-1)$.**

**c)** Pour $(x,y)\in\mathcal D$ :

$$\begin{aligned}
\partial^2_{1,1}f(x,y)&=-\frac{y^2}{(1+xy)^2},\\
\partial^2_{1,2}f(x,y)=\partial^2_{2,1}f(x,y)&=\frac{(1+xy)-yx}{(1+xy)^2}=\frac1{(1+xy)^2},\\
\partial^2_{2,2}f(x,y)&=-\frac{x^2}{(1+xy)^2}.
\end{aligned}$$

Au point $(0,-1)$, on a $1+xy=1$, d'où

$$\boxed{\nabla^2f(0,-1)=\begin{pmatrix}-1&1\\1&0\end{pmatrix}.}$$

Ses valeurs propres sont les réels $\lambda$ tels que $\nabla^2f(0,-1)-\lambda I$ n'est pas inversible, c'est-à-dire tels que

$$(-1-\lambda)(-\lambda)-1=\lambda^2+\lambda-1=0.$$

Elles valent $\lambda_1=\frac{-1-\sqrt5}2<0$ et $\lambda_2=\frac{-1+\sqrt5}2>0$. Elles sont non nulles et de signes opposés : **$(0,-1)$ est un point selle (point col) de $f$**, qui n'est donc pas un extremum local.

### Question 2

**a)** Soit $(x,y)\in\mathcal D$ avec $x\neq0$.

Comme $1+xy>0$ et que $\ln$ est une bijection de $]0,+\infty[$ sur $\mathbb R$, de réciproque $\exp$ :

$$\begin{aligned}
f(x,y)=k&\iff\ln(1+xy)=k-x\\
&\iff1+xy=e^{k-x}\\
&\iff y=\frac{e^{k-x}-1}{x}\qquad(x\neq0).
\end{aligned}$$

**b)** Ligne 5 complétée :

```python
    M = [(np.exp(k-x)-1)/x for x in X]
```

`np.linspace(-2,2,100)` renvoie les réels $-2+\frac{4i}{99}$, $0\le i\le99$, qui ne s'annulent jamais (il faudrait $i=49{,}5$) : la division par `x` est licite.

La liste `K` contient les réels $-0{,}4+\frac i5$ pour $i\in[\![0,7]\!]$. Le graphique représente donc les lignes de niveau

$$\boxed{k\in\{-0{,}4\,;\,-0{,}2\,;\,0\,;\,0{,}2\,;\,0{,}4\,;\,0{,}6\,;\,0{,}8\,;\,1\}.}$$

Le trait vertical en $x=0$ vient de ce que `plt.plot` relie le dernier point d'abscisse négative au premier d'abscisse positive : pour $k\neq0$, la fonction $x\mapsto\frac{e^{k-x}-1}x$ tend vers $\pm\infty$ de part et d'autre de $0$.

## Exercice 1 — Partie B : Étude de la ligne de niveau zéro

### Question 3

Soit $x\in\mathbb R^*$.

- Si $x>0$, alors $-x<0$ donc $e^{-x}<1$ : le numérateur est strictement négatif et le dénominateur strictement positif.
- Si $x<0$, alors $e^{-x}>1$ : le numérateur est strictement positif et le dénominateur strictement négatif.

Dans les deux cas, $\boxed{g(x)<0\text{ pour tout }x\in\mathbb R^*.}$

### Question 4

Au voisinage de $0$, $e^u=1+u+\frac{u^2}2+o(u^2)$. Avec $u=-x$ :

$$e^{-x}-1=-x+\frac{x^2}2+o(x^2).$$

En divisant par $x\neq0$ :

$$g(x)=-1+\frac x2+o(x).$$

Donc $g(x)\to-1$ quand $x\to0$ : **$g$ admet un prolongement continu en $0$, en posant $g(0)=-1$.**

### Question 5

Pour $x\neq0$, par le développement limité de la question 4 :

$$\begin{aligned}
\frac{g(x)-g(0)}{x-0}&=\frac{g(x)+1}{x}\\
&=\frac12+o(1).
\end{aligned}$$

Le taux d'accroissement a une limite finie en $0$ : **$g$ est dérivable en $0$ et $\boxed{g'(0)=\frac12}$.**

### Question 6

**a)** $g$ est dérivable sur $\mathbb R^*$ comme quotient de fonctions dérivables dont le dénominateur ne s'annule pas. Pour $x\neq0$ :

$$\begin{aligned}
g'(x)&=\frac{-e^{-x}\,x-(e^{-x}-1)}{x^2}\\
&=\boxed{\frac{1-(1+x)e^{-x}}{x^2}.}
\end{aligned}$$

**b)** Posons $h(x)=1-(1+x)e^{-x}$ pour $x\in\mathbb R$. La fonction $h$ est dérivable et

$$\begin{aligned}
h'(x)&=-e^{-x}+(1+x)e^{-x}\\
&=xe^{-x}.
\end{aligned}$$

Donc $h'<0$ sur $]-\infty,0[$ et $h'>0$ sur $]0,+\infty[$.

Ainsi $h$ est strictement décroissante sur $]-\infty,0]$ et strictement croissante sur $[0,+\infty[$.

Elle admet en $0$ un minimum strict, $h(0)=0$. Ainsi $h(x)>0$ pour $x\neq0$ et, comme $x^2>0$ :

$$\boxed{g'(x)>0\text{ pour tout }x\in\mathbb R^*.}$$

**c)** *En $+\infty$.* On a $e^{-x}\to0$, donc $e^{-x}-1\to-1$, et $\frac1x\to0$ : $\boxed{\lim_{x\to+\infty}g(x)=0.}$

Plus précisément, $g(x)\sim-\frac1x$, donc $g$ tend vers $0$ par valeurs négatives.

*En $-\infty$.* Posons $u=-x\to+\infty$. Alors

$$g(x)=\frac{e^u-1}{-u}=-\frac{e^u}{u}+\frac1u.$$

Par croissances comparées, $\frac{e^u}u\to+\infty$, donc $\boxed{\lim_{x\to-\infty}g(x)=-\infty.}$

*Variations.* $g$ est continue sur $\mathbb R$ (question 4) et strictement croissante sur $]-\infty,0]$ et sur $[0,+\infty[$ (question 6.b), donc strictement croissante sur $\mathbb R$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $+$ | $\frac12$ | $+$ | |
| $g$ | $-\infty$ | $\nearrow$ | $-1$ | $\nearrow$ | $0^-$ |

### Question 7

**a)** La courbe d'équation $1+xy=0$ est l'hyperbole d'équation $y=-\frac1x$, $x\neq0$ (aucun point d'abscisse nulle ne la vérifie). Ce n'est pas une droite. Elle a deux branches, asymptotes aux deux axes.

Par la question 2.a avec $k=0$, la ligne de niveau 0 est la réunion :

- de la droite $x=0$, puisque $f(0,y)=0+\ln1=0$ pour tout $y$ ;
- de la courbe de $g$ (privée du point d'abscisse $0$, qui est sur la droite).

Position relative : pour $x\neq0$, $g(x)-\big(-\frac1x\big)=\frac{e^{-x}}x$. La courbe de $g$ est donc au-dessus de l'hyperbole pour $x>0$, en dessous pour $x<0$ : elle reste dans $\mathcal D$, comme il se doit.

Elle passe par $(0,-1)$ avec la pente $\frac12$.

![Figure 1 — Ligne de niveau 0 de f (droite x = 0 et courbe de g, en trait plein), hyperbole 1 + xy = 0 (tirets) et zones hachurées où f est positive](figures/q7-ligne-niveau-zero.svg)

**b)** Le domaine $\mathcal D$ est formé des points tels que $y>-\frac1x$ si $x>0$, $y<-\frac1x$ si $x<0$, et de toute la droite $x=0$.

Pour $(x,y)\in\mathcal D$ avec $x\neq0$ :

$$\begin{aligned}
f(x,y)>0&\iff\ln(1+xy)>-x\\
&\iff1+xy>e^{-x}\\
&\iff xy>e^{-x}-1.
\end{aligned}$$

- Pour $x>0$ : $f(x,y)>0\iff y>g(x)$, la zone **au-dessus** de la courbe de $g$.
- Pour $x<0$ : en divisant par $x<0$, $f(x,y)>0\iff y<g(x)$, la zone **en dessous** de la courbe de $g$.

Les deux zones hachurées sur la figure sont donc $\{x>0,\ y>g(x)\}$ et $\{x<0,\ y<g(x)\}$. Dans les deux autres zones (entre la courbe de $g$ et l'hyperbole), $f$ est négative.

## Exercice 1 — Partie C : Aire de la surface délimitée par la ligne de niveau zéro

### Question 8

La fonction $g$ (prolongée) est continue sur $\mathbb R$ : sur $\mathbb R^*$ comme quotient de fonctions continues, et en $0$ par la question 4.

Pour tout $x$, $G(x)$ est l'intégrale d'une fonction continue sur le segment d'extrémités $0$ et $x$, donc existe.

Par le théorème fondamental de l'analyse, $G$ est la primitive de $g$ sur $\mathbb R$ qui s'annule en $0$. Elle est donc dérivable, de dérivée $g$ continue :

$$\boxed{G\in\mathcal C^1(\mathbb R)\quad\text{et}\quad G'=g.}$$

### Question 9

Soit $x>0$. Par la relation de Chasles, puis par linéarité de l'intégrale sur le segment d'extrémités $1$ et $x$ (sur lequel $t\mapsto\frac{e^{-t}}t$ et $t\mapsto\frac1t$ sont continues) :

$$\begin{aligned}
G(x)&=G(1)+\int_1^x\frac{e^{-t}-1}t\,dt\\
&=G(1)+\int_1^x\frac{e^{-t}}t\,dt-\int_1^x\frac{dt}t\\
&=\boxed{G(1)+\int_1^x\frac{e^{-t}}t\,dt-\ln(x).}
\end{aligned}$$

### Question 10

*Convergence de $\int_1^{+\infty}\frac{e^{-t}}t\,dt$.* Pour $t\ge1$, on a $0\le\frac{e^{-t}}t\le e^{-t}$. L'intégrale $\int_1^{+\infty}e^{-t}dt$ converge (elle vaut $e^{-1}$).

Par comparaison de fonctions positives, $\int_1^{+\infty}\frac{e^{-t}}t\,dt$ converge ; notons $L$ sa valeur.

Pour $x>1$, par la question 9 :

$$\frac{G(x)}{-\ln(x)}=1-\frac{G(1)+\int_1^x\frac{e^{-t}}t\,dt}{\ln(x)}.$$

Le numérateur de la fraction tend vers $G(1)+L$, réel fixe, et $\ln(x)\to+\infty$ : la fraction tend vers $0$. Donc $\frac{G(x)}{-\ln(x)}\to1$, c'est-à-dire

$$\boxed{G(x)\underset{x\to+\infty}{\sim}-\ln(x).}$$

### Question 11

Soit $x>0$. Par la question 9 :

$$\begin{aligned}
\int_x^1\frac{e^{-t}}t\,dt&=-\int_1^x\frac{e^{-t}}t\,dt\\
&=-\ln(x)+G(1)-G(x).
\end{aligned}$$

$G$ est dérivable en $0$ avec $G(0)=0$ et $G'(0)=g(0)=-1$. Elle admet donc en $0$ le développement limité d'ordre 1 :

$$G(x)=G(0)+G'(0)x+o(x)=-x+o(x).$$

En reportant :

$$\boxed{\int_x^1\frac{e^{-t}}t\,dt=-\ln(x)+G(1)+x+o(x).}$$

## Exercice 2 — Partie A : Un endomorphisme de $\mathcal M_2(\mathbb R)$

### Question 1

Soit $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, $N=\begin{pmatrix}a'&b'\\c'&d'\end{pmatrix}$ et $\lambda\in\mathbb R$. La matrice $\lambda M+N$ a pour coefficients diagonaux $\lambda a+a'$ et $\lambda d+d'$, donc

$$\begin{aligned}
\mathrm{tr}(\lambda M+N)&=(\lambda a+a')+(\lambda d+d')\\
&=\lambda\,\mathrm{tr}(M)+\mathrm{tr}(N).
\end{aligned}$$

**L'application $\mathrm{tr}$ est linéaire.**

### Question 2

**a)** Pour toute $M\in\mathcal M_2(\mathbb R)$, $\varphi(M)=\mathrm{tr}(M)I-M$ appartient à $\mathcal M_2(\mathbb R)$. Pour $M,N\in\mathcal M_2(\mathbb R)$ et $\lambda\in\mathbb R$, par linéarité de la trace (question 1) :

$$\begin{aligned}
\varphi(\lambda M+N)&=\big(\lambda\,\mathrm{tr}(M)+\mathrm{tr}(N)\big)I-\lambda M-N\\
&=\lambda\big(\mathrm{tr}(M)I-M\big)+\big(\mathrm{tr}(N)I-N\big)\\
&=\lambda\varphi(M)+\varphi(N).
\end{aligned}$$

**$\varphi$ est une application linéaire de $\mathcal M_2(\mathbb R)$ dans lui-même : c'est un endomorphisme.**

**b)** $\mathrm{tr}(I)=2$, donc $\varphi(I)=2I-I=\boxed{I.}$

**c)** Par linéarité de la trace :

$$\begin{aligned}
\mathrm{tr}\big(\varphi(M)\big)&=\mathrm{tr}(M)\,\mathrm{tr}(I)-\mathrm{tr}(M)\\
&=2\,\mathrm{tr}(M)-\mathrm{tr}(M)=\boxed{\mathrm{tr}(M).}
\end{aligned}$$

### Question 3

**a)** On a $\mathrm{tr}(E_1)=\mathrm{tr}(E_4)=1$ et $\mathrm{tr}(E_2)=\mathrm{tr}(E_3)=0$, et $I=E_1+E_4$. Donc

$$\begin{aligned}
\varphi(E_1)&=I-E_1=E_4,\\
\varphi(E_2)&=-E_2,\\
\varphi(E_3)&=-E_3,\\
\varphi(E_4)&=I-E_4=E_1.
\end{aligned}$$

La matrice de $\varphi$ dans la base $\mathcal B$, dont les colonnes sont les coordonnées des images, est une matrice de $\mathcal M_4(\mathbb R)$ :

$$\boxed{A=\begin{pmatrix}0&0&0&1\\0&-1&0&0\\0&0&-1&0\\1&0&0&0\end{pmatrix}.}$$

**b)** Le calcul donne $\boxed{A^2=I_4.}$

On le retrouve sans calcul : $\varphi\circ\varphi$ échange deux fois $E_1$ et $E_4$, et multiplie deux fois $E_2$ et $E_3$ par $-1$.

Ainsi $A\times A=I_4$ : **$A$ est inversible et $A^{-1}=A$.**

**c)** Soit $\lambda\in\mathbb R$ et $X={}^t(x_1,x_2,x_3,x_4)$. L'équation $AX=\lambda X$ s'écrit

$$\begin{cases}x_4=\lambda x_1\\-x_2=\lambda x_2\\-x_3=\lambda x_3\\x_1=\lambda x_4.\end{cases}$$

Les première et dernière équations donnent $x_1=\lambda^2x_1$ et $x_4=\lambda^2x_4$.

Si $\lambda\notin\{-1,1\}$, alors $x_1=x_4=0$, et $(1+\lambda)x_2=(1+\lambda)x_3=0$ donne $x_2=x_3=0$ : seul $X=0$ convient, et $\lambda$ n'est pas valeur propre.

- $\lambda=1$ : le système équivaut à $x_2=x_3=0$ et $x_4=x_1$. Le sous-espace propre est $E_1(A)=\mathrm{Vect}\big({}^t(1,0,0,1)\big)$, non réduit à $\{0\}$.
- $\lambda=-1$ : le système équivaut à $x_4=-x_1$, avec $x_2$ et $x_3$ libres. Donc $E_{-1}(A)=\mathrm{Vect}\big({}^t(1,0,0,-1),{}^t(0,1,0,0),{}^t(0,0,1,0)\big)$.

Ces trois vecteurs forment une famille libre (leurs deuxième et troisième coordonnées séparent les deux derniers, et le premier est le seul à avoir une première coordonnée non nulle) : c'est une base de $E_{-1}(A)$. Le vecteur ${}^t(1,0,0,1)$, non nul, est une base de $E_1(A)$.

$$\boxed{\mathrm{Sp}(A)=\{-1,1\}.}$$

En termes de matrices de $\mathcal M_2(\mathbb R)$ : $E_1+E_4=I$ engendre le sous-espace propre de $\varphi$ pour $1$, et $(E_1-E_4,E_2,E_3)$ est une base du sous-espace propre pour $-1$.

## Exercice 2 — Partie B : Deux formules d'inversion

### Question 4

$\mathrm{tr}(M)=a+d$, donc

$$\begin{aligned}
\varphi(M)&=\begin{pmatrix}a+d&0\\0&a+d\end{pmatrix}-\begin{pmatrix}a&b\\c&d\end{pmatrix}\\
&=\boxed{\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.}
\end{aligned}$$

Puis

$$\begin{aligned}
M\varphi(M)&=\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\\
&=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}\\
&=\boxed{\det(M)\,I.}
\end{aligned}$$

### Question 5

**a)** *Si $\det(M)\neq0$.* Par la question 4, $M\Big(\frac1{\det(M)}\varphi(M)\Big)=I$. Pour des matrices carrées, cela suffit : $M$ est inversible et

$$\boxed{M^{-1}=\frac1{\det(M)}\varphi(M).}$$

*Si $\det(M)=0$.* Raisonnons par l'absurde en supposant $M$ inversible. Alors $M\varphi(M)=0$ ; en multipliant à gauche par $M^{-1}$, on obtient $\varphi(M)=0$, c'est-à-dire $M=\mathrm{tr}(M)I$.

En prenant la trace, $\mathrm{tr}(M)=2\,\mathrm{tr}(M)$, donc $\mathrm{tr}(M)=0$ et $M=0$, qui n'est pas inversible : contradiction.

Ainsi **$M$ est inversible si et seulement si $\det(M)\neq0$**, et dans ce cas $M^{-1}=\frac1{\det(M)}\varphi(M)$.

**b)** $M$, $N$ et $M+N$ sont inversibles, donc leurs déterminants sont non nuls (question a). Par a), $\det(M)M^{-1}=\varphi(M)$ et $\det(N)N^{-1}=\varphi(N)$.

Par linéarité de $\varphi$, puis par a) appliquée à $M+N$ :

$$\begin{aligned}
\frac{\det(M)}{\det(M+N)}M^{-1}+\frac{\det(N)}{\det(M+N)}N^{-1}&=\frac{\varphi(M)+\varphi(N)}{\det(M+N)}\\
&=\frac{\varphi(M+N)}{\det(M+N)}\\
&=(M+N)^{-1}.
\end{aligned}$$

D'où

$$\boxed{(M+N)^{-1}=\frac{\det(M)}{\det(M+N)}M^{-1}+\frac{\det(N)}{\det(M+N)}N^{-1}.}$$

## Exercice 2 — Partie C : Polynômes de Tchebychev et trace des matrices de déterminant 1

### Question 6

**a)** Avec $n=1$ puis $n=2$ dans la relation de récurrence :

$$\begin{aligned}
P_2(x)&=xP_1(x)-P_0(x)=\boxed{x,}\\
P_3(x)&=xP_2(x)-P_1(x)=\boxed{x^2-1.}
\end{aligned}$$

**b)** On montre par récurrence double, pour $n\in\mathbb N^*$, la propriété $\mathcal H(n)$ : « $\deg(P_n)=n-1$ et $\deg(P_{n+1})=n$ ».

*Initialisation.* $\deg(P_1)=0$ et $\deg(P_2)=1$ : $\mathcal H(1)$ est vraie.

*Hérédité.* Supposons $\mathcal H(n)$ vraie pour un $n\ge1$. Alors $xP_{n+1}$ est de degré $n+1$ et $P_n$ de degré $n-1<n+1$. Le degré d'une somme de deux polynômes de degrés différents est le plus grand des deux.

Donc $P_{n+2}=xP_{n+1}-P_n$ est de degré $n+1$, et $\mathcal H(n+1)$ est vraie.

Par récurrence, $\boxed{\deg(P_n)=n-1\text{ pour tout }n\in\mathbb N^*.}$

### Question 7

On note $t=\mathrm{tr}(M)$. Alors $a_0=P_0(t)=0$, $a_1=P_1(t)=1$, et pour $n\ge1$, $a_{n+1}=ta_n-a_{n-1}$ (relation de récurrence évaluée en $t$).

**a)** Par la question 4 et $\det(M)=1$ : $M\varphi(M)=I$, soit $M\big(tI-M\big)=I$. En développant, $tM-M^2=I$, d'où

$$\boxed{M^2=\mathrm{tr}(M)M-I.}$$

**b)** Récurrence sur $n\ge1$.

*Initialisation.* $-a_0I+a_1M=M=M^1$.

*Hérédité.* Supposons $M^n=-a_{n-1}I+a_nM$. Alors, avec a) :

$$\begin{aligned}
M^{n+1}&=M\,M^n=-a_{n-1}M+a_nM^2\\
&=-a_{n-1}M+a_n(tM-I)\\
&=-a_nI+(ta_n-a_{n-1})M\\
&=-a_nI+a_{n+1}M.
\end{aligned}$$

La relation $a_{n+1}=ta_n-a_{n-1}$ justifie la dernière égalité. Par récurrence, pour tout $n\ge1$ :

$$\boxed{M^n=-a_{n-1}I+a_nM.\qquad(*)}$$

**c)** Par linéarité de la trace et $\mathrm{tr}(I)=2$ :

$$\begin{aligned}
\mathrm{tr}(M^n)&=-2a_{n-1}+a_n\,t\\
&=tP_n(t)-2P_{n-1}(t).
\end{aligned}$$

Le polynôme $Q_n=XP_n-2P_{n-1}$ convient. Comme $XP_n=P_{n+1}+P_{n-1}$ :

$$\boxed{\begin{aligned}Q_n&=P_{n+1}-P_{n-1},\\\mathrm{tr}(M^n)&=Q_n\big(\mathrm{tr}(M)\big).\end{aligned}}$$

Vérification : $Q_1=P_2-P_0=X$ et $\mathrm{tr}(M)=t$ ; $Q_2=P_3-P_1=X^2-2$, et $\mathrm{tr}(M^2)=t^2-2$ par a).

### Question 8

**a)** On garde dans `P0` et `P1` deux termes consécutifs : après le passage d'indice `k` dans la boucle, `P0` contient $P_k(x)$ et `P1` contient $P_{k+1}(x)$.

```python
def P(n,x):
    P0 = 0
    P1 = 1
    for k in range(1,n+1):
        P2 = x*P1 - P0
        P0 = P1
        P1 = P2
    return(P0)
```

Pour $n=0$, la boucle n'est pas exécutée et la fonction renvoie $0=P_0(x)$.

**b)** Par $(*)$, $M^n=-P_{n-1}(t)I+P_n(t)M$ avec $t=\mathrm{tr}(M)$ :

```python
def Puissance(n,M):
    t = M[0,0] + M[1,1]
    return -P(n-1,t)*np.eye(2) + P(n,t)*M
```

Contrôle : pour $M=\begin{pmatrix}2&3\\1&2\end{pmatrix}$ (de déterminant 1), `Puissance(n,M)` coïncide avec $M^n$ pour $n=1,\dots,5$.

## Exercice 3 — Partie A : Rang moyen du premier double pile

### Question 1

**a)** $N-1$ est le rang du premier pile dans une suite de lancers indépendants, chacun donnant pile avec la probabilité $p$. C'est le temps d'attente du premier succès dans un processus de Bernoulli :

$$\boxed{N-1\hookrightarrow\mathcal G(p)}$$

soit $P(N-1=k)=q^{k-1}p$ pour $k\in\mathbb N^*$.

**b)** $N$ prend ses valeurs dans $[\![2,+\infty[\![$ et, pour $n\ge2$, $(N=n)=(N-1=n-1)$, donc

$$\boxed{P(N=n)=q^{n-2}p.}$$

Par linéarité et propriétés de la variance :

$$\begin{aligned}
E(N)&=E(N-1)+1=\boxed{\frac1p+1,}\\
V(N)&=V(N-1)=\boxed{\frac q{p^2}.}
\end{aligned}$$

### Question 2

**a)** Pour $n\ge2$, l'événement $(N=n)\cap S$ est $F_1\cdots F_{n-2}P_{n-1}P_n$. Par indépendance des lancers :

$$\boxed{P\big((N=n)\cap S\big)=q^{n-2}p^2.}$$

**b)** Les événements $(N=n)$, $n\ge2$, forment un système complet d'événements. Par la formule des probabilités totales et a) :

$$\begin{aligned}
P(S)&=\sum_{n=2}^{+\infty}q^{n-2}p^2\\
&=\frac{p^2}{1-q}=\boxed{p.}
\end{aligned}$$

La série géométrique converge car $|q|<1$.

### Question 3

**a)** Les répétitions de la première expérience sont indépendantes, et chacune réalise $S$ avec la probabilité $p$ (question 2.b). $R$ est le rang de la première répétition qui réalise $S$ : c'est le temps d'attente du premier succès dans un processus de Bernoulli de paramètre $p$.

$$\boxed{R\hookrightarrow\mathcal G(p).}$$

**b)** Une répétition qui ne réalise pas $S$ se termine par $\cdots F\,P\,F$ : elle contient un unique pile, précédé d'un face (ou premier lancer de toute la série) et suivi d'un face. Ce pile est isolé. La répétition précédente se termine elle aussi par un face. La répétition qui réalise $S$ se termine par le double pile et ne contient pas de pile isolé.

Le nombre de piles isolés obtenus avant le premier double pile est donc $R-1$, et en moyenne :

$$\boxed{E(R-1)=\frac1p-1=\frac qp.}$$

### Question 4

$N_i=0$ sur $(R<i)$, et $N_i\ge2$ sur $(R\ge i)$. Comme $R\hookrightarrow\mathcal G(p)$, on a $P(R\ge i)=q^{i-1}$, qui est non nul.

**a)** Donc $(N_i=0)=(R<i)$ et

$$\boxed{P(N_i=0)=1-q^{i-1}.}$$

**b)** Pour $k\ge2$, $(N_i=k)\subset(R\ge i)$. Par la formule des probabilités composées et l'énoncé (loi conditionnelle de $N_i$ sachant $R\ge i$) :

$$\begin{aligned}
P(N_i=k)&=P(R\ge i)\,P_{(R\ge i)}(N_i=k)\\
&=q^{i-1}\,q^{k-2}p\\
&=\boxed{p\,q^{i+k-3}.}
\end{aligned}$$

**c)** $N_i$ prend ses valeurs dans $\{0\}\cup[\![2,+\infty[\![$. Elle admet une espérance si et seulement si la série $\sum_kk\,P(N_i=k)$ converge absolument ; ses termes sont positifs. Or

$$\begin{aligned}k\,P(N_i=k)&=k\,p\,q^{i+k-3}\\&=q^{i-1}\,k\,P(N=k),\end{aligned}$$

et $\sum_kk\,P(N=k)$ converge, de somme $E(N)=\frac{1+p}p$ (question 1.b). Donc $N_i$ admet une espérance et

$$\boxed{E(N_i)=q^{i-1}\,\frac{1+p}p.}$$

### Question 5

La série $\sum_{i\ge1}q^{i-1}$ est géométrique de raison $q$, avec $|q|<1$ : elle converge et sa somme vaut $\frac1{1-q}=\frac1p$. Donc $\sum_{i\ge1}E(N_i)$ converge et

$$\boxed{\sum_{i=1}^{+\infty}E(N_i)=\frac{1+p}{p^2}.}$$

### Question 6

**a)** Notons $U_n=N_1+\cdots+N_n$. Soit $k\in[\![0,n]\!]$.

- Sur $(R\le n)$, on a $N_i=0$ pour $i>n$, donc $T=U_n$.
- Sur $(R>n)$, les $N_1,\dots,N_n$ valent tous au moins 2, donc $U_n\ge2n>n$, et $T\ge U_n>n$.

Ainsi $(T=k)$ est contenu dans $(R\le n)$, sur lequel $T=U_n$. De même, $(U_n=k)$ est contenu dans $(R\le n)$. Donc $(T=k)=(U_n=k)$ et

**$P(T=k)=P(N_1+\cdots+N_n=k)$.**

**b)** $U_n$ est une somme de $n$ variables admettant une espérance, donc admet une espérance $E(U_n)=\sum_{i=1}^nE(N_i)$. C'est une variable à valeurs dans $\mathbb N$, donc $E(U_n)=\sum_{k\ge0}k\,P(U_n=k)$, série à termes positifs. Avec a) :

$$\begin{aligned}
\sum_{k=2}^nk\,P(T=k)&=\sum_{k=2}^nk\,P(U_n=k)\\
&\le\sum_{k=0}^{+\infty}k\,P(U_n=k)=\sum_{i=1}^nE(N_i).
\end{aligned}$$

On a donc bien majoré $\sum_{k=2}^nk\,P(T=k)$ par $\sum_{i=1}^nE(N_i)$, ce qui est l'inégalité demandée.

**c)** $T$ prend ses valeurs dans $[\![2,+\infty[\![$. La série $\sum_kk\,P(T=k)$ est à termes positifs. Par b) et la question 5, ses sommes partielles sont majorées par $\sum_{i=1}^{+\infty}E(N_i)=\frac{1+p}{p^2}$.

Une série à termes positifs dont les sommes partielles sont majorées converge : **$T$ admet une espérance**, et

$$E(T)\le\sum_{i=1}^{+\infty}E(N_i).$$

### Question 7

L'inégalité $E(T)\le\sum_{i\ge1}E(N_i)$ vient d'être établie. Inversement, pour tout $n\ge1$, les $N_i$ sont positifs, donc $U_n=N_1+\cdots+N_n\le T$. Par croissance de l'espérance ($U_n$ et $T$ en admettent une) :

$$\sum_{i=1}^nE(N_i)\le E(T).$$

En faisant tendre $n$ vers $+\infty$, $\sum_{i=1}^{+\infty}E(N_i)\le E(T)$. Finalement

$$\boxed{\begin{aligned}E(T)&=\sum_{i=1}^{+\infty}E(N_i)\\&=\frac{1+p}{p^2}.\end{aligned}}$$

## Exercice 3 — Partie B : Simulation informatique

### Question 8

`rd.random() < p` simule un pile (probabilité $p$) et `rd.random() >= p` un face.

```python
def Exp_1(p):
    N = 1
    while rd.random() >= p :
        N = N + 1

    if rd.random() < p :
        S = 1
    else:
        S = 0
    return N+1, S
```

La boucle compte les lancers jusqu'au premier pile inclus ($N$ est le rang du premier pile), puis on effectue le lancer supplémentaire. Chaque appel à `rd.random()` simule un nouveau lancer.

### Question 9

```python
def Exp_2(p):
    R = 0
    S = 0
    T = 0
    while S == 0:
        R = R + 1
        E = Exp_1(p)
        S = E[1]
        T = T + E[0]
    return R, T
```

`E[0]` et `E[1]` sont la première et la deuxième composante du couple renvoyé par `Exp_1`.

### Question 10

**a)**

```python
def Freq_T(n,p):
    c = 0
    for i in range(10**4):
        if Exp_2(p)[1] == n:
            c = c + 1
    return c/10**4
```

**b)** Calculons $P(T=4)$ pour $p=\frac12$. Le premier double pile occupe les lancers 3 et 4. Le lancer 2 est alors un face (sinon le double pile serait en 2-3), et le lancer 1 est quelconque. Les issues favorables sont $F_1F_2P_3P_4$ et $P_1F_2P_3P_4$, donc

$$\begin{aligned}P(T=4)&=2\times\frac1{2^4}\\&=\frac18=0{,}125.\end{aligned}$$

La fréquence observée sur $10^4$ réalisations est proche de cette probabilité (loi faible des grands nombres) ; l'écart-type de la fréquence est $\sqrt{\frac{0{,}125\times0{,}875}{10^4}}\approx0{,}003$. **L'affichage `0.123` est cohérent.**

## Exercice 3 — Partie C : Nombre de doubles piles

### Question 11

$Y_n$ ne prend que les valeurs $0$ et $1$, et $P(Y_n=1)=P(P_nP_{n+1})=p^2$ par indépendance des lancers. Donc

$$\boxed{\begin{aligned}&Y_n\hookrightarrow\mathcal B(p^2),\\&E(Y_n)=p^2,\\&V(Y_n)=p^2(1-p^2).\end{aligned}}$$

### Question 12

**a)** *$Y_n$ et $Y_{n+1}$.* L'événement $[Y_n=1]\cap[Y_{n+1}=1]$ est $P_nP_{n+1}P_{n+2}$. Par indépendance des lancers, sa probabilité vaut $p^3$.

Or $P(Y_n=1)\,P(Y_{n+1}=1)=p^4$, et $p^3\neq p^4$ puisque $p\in\,]0,1[$. **$Y_n$ et $Y_{n+1}$ ne sont pas indépendantes.**

*$Y_n$ et $Y_m$ avec $m\ge n+2$.* La variable $Y_n$ est une fonction des résultats des lancers $n$ et $n+1$.

De même, $Y_m$ est une fonction des résultats des lancers $m$ et $m+1$.

Comme $m>n+1$, ces lancers sont distincts. Les lancers étant mutuellement indépendants, le lemme des coalitions montre que **$Y_n$ et $Y_m$ sont indépendantes.**

**b)** $Y_nY_{n+1}$ vaut 1 exactement sur $[Y_n=1]\cap[Y_{n+1}=1]$, donc $E(Y_nY_{n+1})=p^3$. Par la formule de König-Huygens :

$$\begin{aligned}
\mathrm{cov}(Y_n,Y_{n+1})&=E(Y_nY_{n+1})-E(Y_n)E(Y_{n+1})\\
&=p^3-p^4=\boxed{p^3(1-p).}
\end{aligned}$$

$Y_n$ et $Y_m$ sont indépendantes, donc $\boxed{\mathrm{cov}(Y_n,Y_m)=0.}$

### Question 13

**a)** Par linéarité de l'espérance, $E(S_n)=\sum_{k=1}^nE(Y_k)$, donc $\boxed{E(S_n)=np^2.}$

$S_n$ est une variable finie, qui admet une variance. Par bilinéarité et symétrie de la covariance :

$$\begin{aligned}V(S_n)&=\mathrm{cov}(S_n,S_n)\\&=\sum_{k=1}^n\sum_{l=1}^n\mathrm{cov}(Y_k,Y_l).\end{aligned}$$

On sépare les termes selon $|k-l|$, avec la question 12.b :

- les $n$ termes $k=l$ valent $V(Y_k)=p^2(1-p^2)$ ;
- les termes $|k-l|=1$ sont au nombre de $2(n-1)$ et valent $p^3(1-p)$ ;
- les termes $|k-l|\ge2$ sont nuls.

Donc

$$\boxed{V(S_n)=np^2(1-p^2)+2(n-1)p^3(1-p).}$$

**b)** On a $V\big(\frac{S_n}n\big)=\frac{V(S_n)}{n^2}$. Or $1-p^2\le1$ et $p^3(1-p)=p^2\cdot p(1-p)\le p^2$, donc

$$\begin{aligned}
V(S_n)&\le np^2+2(n-1)p^2\\
&\le3np^2.
\end{aligned}$$

D'où

$$\boxed{V\Big(\frac{S_n}n\Big)\le\frac{3p^2}n.}$$

### Question 14

La variable $\frac{S_n}n$ admet une espérance $E\big(\frac{S_n}n\big)=p^2$ et une variance (question 13). L'inégalité de Bienaymé-Tchebychev, avec $\varepsilon>0$, donne

$$\begin{aligned}
P\Big(\Big|\frac{S_n}n-p^2\Big|\ge\varepsilon\Big)&\le\frac{V(S_n/n)}{\varepsilon^2}\\
&\le\boxed{3\Big(\frac p\varepsilon\Big)^2\frac1n.}
\end{aligned}$$

Une probabilité est positive et le majorant tend vers $0$ quand $n\to+\infty$. Par encadrement :

$$\boxed{\lim_{n\to+\infty}P\Big(\Big|\frac{S_n}n-p^2\Big|\ge\varepsilon\Big)=0.}$$
