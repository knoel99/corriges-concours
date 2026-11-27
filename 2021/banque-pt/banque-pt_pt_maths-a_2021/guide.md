# Banque PT — Mathématiques A · 2021 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

L’exercice de probabilités précède le problème d’algèbre. Les paramètres de transition sont $\alpha$ pour la panne et $\beta$ pour la réparation. Les parties I à III d’algèbre mènent des puissances d’une matrice symétrique à l’entrelacement des valeurs propres d’une compression.

## Probabilités · Disponibilité d’un appareil

### Question P.1.a

> [!INDICATION]
> Conditionner sur l’état du premier jour.

#### Solution

En distinguant les états $X_1=1$ et $X_1=0$, la probabilité de fonctionnement le deuxième jour vaut $p_2=(1-\alpha)p_1+\beta(1-p_1)$.

### Question P.1.b

> [!INDICATION]
> Appliquer le même conditionnement au jour $n$.

#### Solution

Les deux probabilités de transition ne dépendent pas de $n$. La formule des probabilités totales donne $p_{n+1}=(1-\alpha)p_n+\beta(1-p_n)=\beta+(1-\alpha-\beta)p_n$.

### Question P.1.c

> [!INDICATION]
> Soustraire le point fixe de la récurrence.

#### Solution

Posons $\rho=1-\alpha-\beta$ et $\pi=\beta/(\alpha+\beta)$, qui vérifie $\pi=\beta+\rho\pi$. Ainsi $p_{n+1}-\pi=\rho(p_n-\pi)$ et $p_n=\pi+(p_1-\pi)\rho^{n-1}$ pour $n\ge1$. Le premier jour est donné directement si $\rho=0$.

### Question P.1.d

> [!INDICATION]
> Contrôler la valeur absolue du facteur géométrique.

#### Solution

Comme $0<\alpha<1$ et $0<\beta\le1$ (c’est une probabilité), on a $0<\alpha+\beta<2$. Donc $|\rho|<1$, et la formule précédente donne $\lim p_n=\beta/(\alpha+\beta)$.

### Question P.2.a

> [!INDICATION]
> La valeur initiale est maintenant le point fixe de la transition.

#### Solution

Si $p_1=\pi$, P.1.b donne $p_2=\pi$. Donc $X_2$ suit une Bernoulli de paramètre $\pi$ : ses probabilités en $0$ et $1$ sont $1-\pi$ et $\pi$.

### Question P.2.b

> [!INDICATION]
> Multiplier la probabilité de chaque état initial par la transition correspondante.

#### Solution

Avec les lignes dans l’ordre $X_1=0,1$ et les colonnes dans l’ordre $X_2=0,1$, le tableau conjoint est
$$
\begin{pmatrix}(1-\pi)(1-\beta)&(1-\pi)\beta\\ \pi\alpha&\pi(1-\alpha)\end{pmatrix}.
$$
Les lignes ont pour sommes $1-\pi,\pi$ et les colonnes aussi, car $(1-\pi)\beta=\pi\alpha$.

### Question P.2.c

> [!INDICATION]
> Les deux marginales sont des lois de Bernoulli identiques.

#### Solution

Pour $j=1,2$, $\mathbb E X_j=\pi=\beta/(\alpha+\beta)$ et $\operatorname{Var}(X_j)=\pi(1-\pi)=\alpha\beta/(\alpha+\beta)^2$.

### Question P.2.d

> [!INDICATION]
> Le produit des deux indicatrices est l’indicatrice de la cellule $(1,1)$.

#### Solution

La covariance est $\pi(1-\alpha)-\pi^2=\pi(1-\pi)(1-\alpha-\beta)$, soit $\alpha\beta(1-\alpha-\beta)/(\alpha+\beta)^2$.

### Question P.2.e

> [!INDICATION]
> Lorsque la covariance s’annule, vérifier directement les lois conditionnelles.

#### Solution

L’indépendance imposerait une covariance nulle. Comme $\pi(1-\pi)>0$, il faut $\alpha+\beta=1$. Dans ce cas $\mathbb P(X_2=1\mid X_1=0)=\beta=1-\alpha=\mathbb P(X_2=1\mid X_1=1)=\pi$. Les probabilités de $0$ coïncident aussi. Les deux variables sont donc indépendantes exactement dans ce cas.

### Question P.3

> [!INDICATION]
> Utiliser le produit des probabilités conditionnelles le long du chemin sans panne.

#### Solution

Sachant $X_1=1$, le premier jour en panne est $N=k+1$ si les $k-1$ premières transitions maintiennent le fonctionnement et si la suivante mène à la panne. La propriété de dépendance au seul état courant donne $\mathbb P(N-1=k)=(1-\alpha)^{k-1}\alpha$ pour $k\ge1$. La masse totale vaut un. Donc $N-1$ est géométrique de paramètre $\alpha$ sur $\mathbb N^*$.

### Question P.4.a

> [!INDICATION]
> Sommer la série géométrique à partir de l’indice un.

#### Solution

Posons $q=1-p$. Pour $|qs|<1$, $G_{Y_1}(s)=\sum_{j\ge1}p q^{j-1}s^j=ps/(1-qs)$. Si $p=1$, $Y_1=1$ et la même expression vaut $s$ pour tout $s$.

### Question P.4.b

> [!INDICATION]
> L’indépendance permet de factoriser une espérance de produit.

#### Solution

Dans le même domaine, $G_{Y_1+Y_2}(s)=\mathbb E(s^{Y_1}s^{Y_2})=G_{Y_1}(s)G_{Y_2}(s)=[ps/(1-qs)]^2$.

### Question P.4.c

> [!INDICATION]
> Le minimum dépasse un niveau si les deux durées le dépassent.

#### Solution

Pour $t<1$, $F_Z(t)=0$. Pour $t\ge1$, $\mathbb P(Z>t)=q^{2\lfloor t\rfloor}$, donc $F_Z(t)=1-q^{2\lfloor t\rfloor}$. Par différence, $\mathbb P(Z=j)=(1-q^2)(q^2)^{j-1}$ pour $j\ge1$. Le minimum est géométrique de paramètre $1-q^2$. Pour $p=1$ il est constant égal à $1$.

### Question P.4.d

> [!INDICATION]
> Travailler sur l’événement où les deux variables sont au plus égales au seuil.

#### Solution

Pour chaque entier $j\ge0$, $\mathbb P(T\le j)=(1-q^j)^2$, avec $F_T(0)=0$. La masse en $j\ge1$ vaut donc $(1-q^j)^2-(1-q^{j-1})^2$. Elle est nulle ailleurs. Dans le cas $p=1$, le maximum est également égal à $1$ presque sûrement.

### Question P.5

> [!INDICATION]
> Distinguer le nombre de transitions écoulées et le numéro du jour.

#### Solution

Le nombre de transitions jusqu’à la première panne d’un des deux appareils est le minimum de deux variables indépendantes géométriques de paramètre $\alpha$. Sa moyenne est $1/[1-(1-\alpha)^2]=1/[\alpha(2-\alpha)]$ jours écoulés après le premier jour. Le numéro moyen du jour de la première panne, si le départ est le jour 1, est donc $1+1/[\alpha(2-\alpha)]$.

## Algèbre, partie I · Deux exemples de moments matriciels

### Question I.1.a

> [!INDICATION]
> Reconnaître l’hypothèse du théorème spectral réel.

#### Solution

La matrice $B$ donnée est réelle et symétrique. Son endomorphisme $g$ possède donc une base orthonormée de vecteurs propres réels, dans laquelle sa matrice est diagonale.

### Question I.1.b

> [!INDICATION]
> Tester la direction des sommes de lignes et les directions symétrique et antisymétrique en première et troisième coordonnées.

#### Solution

Le produit matriciel donne $B(1,1,1)^T=-3(1,1,1)^T$, $B(1,0,-1)^T=2(1,0,-1)^T$ et $B(1,-2,1)^T=6(1,-2,1)^T$. Les vecteurs sont orthogonaux, non nuls et au nombre de trois. Dans l’ordre demandé, on choisit $e_1=(1,1,1)/\sqrt3$, $e_2=(1,0,-1)/\sqrt2$, $e_3=(1,-2,1)/\sqrt6$.

### Question I.1.c

> [!INDICATION]
> Dans une base propre orthonormée, seul le produit des composantes de même indice intervient.

#### Solution

Pour $x=\sum x_i e_i$, on a $\langle x,x\rangle=x_1^2+x_2^2+x_3^2$ et $\langle gx,x\rangle=-3x_1^2+2x_2^2+6x_3^2$. Puisque $g^n e_i=\lambda_i^n e_i$, on obtient $v_n(x)=(-3)^n x_1^2+2^n x_2^2+6^n x_3^2$.

### Question I.1.d

> [!INDICATION]
> Choisir le plus grand module propre effectivement présent dans le vecteur.

#### Solution

Si $x_3\ne0$, alors $v_n/6^n\to x_3^2>0$. Si $x_3=0$ et $x_1\ne0$, $v_n/(-3)^n\to x_1^2>0$. Enfin, si $x_3=x_1=0$ et $x\ne0$, on a $v_n=2^n x_2^2>0$. Dans chaque cas la suite est non nulle à partir d’un certain rang.

### Question I.1.e

> [!INDICATION]
> Factoriser la même puissance dominante aux deux rangs.

#### Solution

Si $x_3\ne0$, $v_n=6^n(x_3^2+o(1))$. Le dénominateur est non nul pour $n$ assez grand et le quotient $v_n/v_{n-1}$ tend vers $6$.

### Question I.2.a

> [!INDICATION]
> Écrire $C$ comme une combinaison de l’identité et de la matrice de tous les uns.

#### Solution

$C=3I-2J$, où $J$ envoie $x$ sur la somme de ses coordonnées multipliée par $(1,1,1)$. Ainsi $Ce_1=-3e_1$ et $Ce_2=3e_2$, $Ce_3=3e_3$. La même base orthonormée diagonalise $C$.

### Question I.2.b

> [!INDICATION]
> Calculer les moments d’un vecteur propre unitaire.

#### Solution

Pour chaque $e_i$, $w_n(e_i)$ est la puissance $n$-ième de sa valeur propre pour $C$. Les trois rapports sont donc constants et leurs limites, dans l’ordre des trois vecteurs, valent $-3,3,3$.

### Question I.2.c

> [!INDICATION]
> Séparer les indices pairs des indices impairs.

#### Solution

Posons $a=x_1^2$ et $b=x_2^2+x_3^2$. Alors $w_n=3^n[b+(-1)^n a]$. Pour $x\ne0$, $a+b>0$ et les termes pairs ne s’annulent pas. Les termes impairs sont non nuls exactement si $a\ne b$. Le vecteur nul est également exclu par ce dernier critère. Ainsi $D=\{x:x_1^2\ne x_2^2+x_3^2\}$.

### Question I.2.d

> [!INDICATION]
> Prendre deux composantes de poids positifs et inégaux sur les valeurs propres opposées.

#### Solution

Avec $x_0=e_1+2e_2$, on a $a=1,b=4$. Pour $n$ pair, le rapport $w_n/w_{n-1}$ vaut $3(5/3)=5$. Pour $n$ impair, il vaut $3(3/5)=9/5$. Ces deux valeurs alternent et sont distinctes, bien que $x_0\in D$.

### Question I.2.e

> [!INDICATION]
> Deux indices séparés de deux ont le même signe de parité.

#### Solution

Pour $x\in D$, l’expression de I.2.c donne $w_n=9w_{n-2}$ et le dénominateur est non nul. La limite du quotient est donc $9$.

## Algèbre, partie II · Rôle des valeurs propres dominantes

### Question II.1

> [!INDICATION]
> N’utiliser que les projections sur la base propre du nouvel endomorphisme.

#### Solution

Écrivons $x_i=\langle x,e_i\rangle$. Alors $u_n=\sum_i \lambda_i^n x_i^2$. Puisque $|\lambda_d|>|\lambda_{d-1}|$, on a $\lambda_d\ne0$ et $u_n/\lambda_d^n=x_d^2+\sum_{i<d}(\lambda_i/\lambda_d)^n x_i^2\to x_d^2>0$. Le dénominateur du quotient est donc finalement non nul et $u_n/u_{n-1}\to\lambda_d$.

### Question II.2

> [!INDICATION]
> Additionner les carrés de toutes les projections sur le bloc dominant.

#### Solution

La même division donne $\lim u_n/\lambda_d^n=\sum_{i=k+1}^d x_i^2$ puisque les $k$ premiers rapports ont un module strictement inférieur à un. Cette somme est au moins $x_d^2>0$. Par division de deux termes consécutifs, $u_n/u_{n-1}\to\lambda_d$.

### Question II.3

> [!INDICATION]
> Choisir un vecteur ayant des poids inégaux sur les deux directions propres opposées.

#### Solution

Avec $x=e_{d-1}+2e_d$, $u_n=\lambda_d^n[4+(-1)^n]$ ne s’annule jamais. Le quotient vaut $\lambda_d\,5/3$ aux indices pairs, $\lambda_d\,3/5$ aux indices impairs. Comme $\lambda_d\ne0$, les deux limites diffèrent, d’où $x\in D$ et la divergence demandée.

## Algèbre, partie III · Quotient de Rayleigh et entrelacement

### Question III.1

> [!INDICATION]
> Le quotient est une moyenne pondérée des valeurs propres présentes.

#### Solution

Pour $x=\sum_{i=k}^d x_i e_i\ne0$, le quotient $R(x)=\langle f(x),x\rangle/\langle x,x\rangle=\sum_{i=k}^d \lambda_i x_i^2/\sum_{i=k}^d x_i^2$ est au moins $\lambda_k$.

### Question III.2

> [!INDICATION]
> Chercher un vecteur qui atteint la borne.

#### Solution

Le vecteur $e_k\in F_k$ est non nul et $R(e_k)=\lambda_k$. Avec III.1, cela donne $\min_{F_k^*}R=\lambda_k$.

### Question III.3

> [!INDICATION]
> Cette fois, seuls les indices inférieurs ou égaux à $k$ interviennent.

#### Solution

Pour $x\in E_k^*$, $R(x)$ est une moyenne des $\lambda_1,\ldots,\lambda_k$, donc $R(x)\le\lambda_k$. L’égalité en $e_k$ donne $\max_{E_k^*}R=\lambda_k$.

### Question III.4.a

> [!INDICATION]
> Additionner les dimensions des deux sous-espaces.

#### Solution

Pour $V$ de dimension $k$, $\dim(V\cap F_k)=k+(d-k+1)-\dim(V+F_k)\ge1$. Leur intersection contient donc un vecteur non nul.

### Question III.4.b

> [!INDICATION]
> Évaluer le quotient sur un vecteur de cette intersection.

#### Solution

Prenons $x\in V\cap F_k$, $x\ne0$. III.1 donne $R(x)\ge\lambda_k$. Le maximum de $R$ sur $V^*$ existe car $R$ est homogène de degré zéro et continue sur la sphère unité compacte de $V$. Ce maximum vaut au moins $\lambda_k$.

### Question III.4.c

> [!INDICATION]
> Pour transformer la borne en égalité, choisir le sous-espace spectral inférieur.

#### Solution

Pour tout $V$ de dimension $k$, le maximum est au moins $\lambda_k$ par III.4.b. Le choix $V=E_k$ atteint cette borne par III.3. Il vient $\min_{\dim V=k}\max_{x\in V^*}R(x)=\lambda_k$.

### Question III.4.d

> [!INDICATION]
> Échanger les rôles des espaces supérieur et inférieur.

#### Solution

Si $\dim V=d-k+1$, alors $\dim(V\cap E_k)\ge1$. Un élément non nul de cette intersection a un quotient au plus $\lambda_k$. Le minimum sur $V^*$ existe par compacité de la sphère unité et est au plus $\lambda_k$. Pour $V=F_k$, ce minimum vaut $\lambda_k$ par III.2. Donc $\max_{\dim V=d-k+1}\min_{x\in V^*}R(x)=\lambda_k$.

### Question III.5.a

> [!INDICATION]
> Transposer le produit en respectant l’ordre.

#### Solution

La matrice $A'=Q^TAQ$ est réelle de taille $(d-1)\times(d-1)$ et $(A')^T=Q^TA^TQ=A'$. Le théorème spectral assure donc la base propre orthonormée utilisée ensuite.

### Question III.5.b.i

> [!INDICATION]
> La base canonique est orthonormée.

#### Solution

Si $X,Y$ sont les colonnes de coordonnées, alors $\langle x,y\rangle=X^TY=\sum_{i=1}^{d-1}x_i y_i$.

### Question III.5.b.ii

> [!INDICATION]
> Utiliser l’égalité donnée dans le sens qui conserve la taille des vecteurs.

#### Solution

$\langle q(x),q(y)\rangle=(QX)^TQY=X^T(Q^TQ)Y=X^TY=\langle x,y\rangle$. Cette application isométrique préserve en particulier la norme.

### Question III.5.b.iii

> [!INDICATION]
> La conservation de la norme donne l’injectivité.

#### Solution

Si $q(x)=0$, alors $\|x\|^2=\|q(x)\|^2=0$. La restriction de $q$ à $E'_k$ est injective, donc $\dim q(E'_k)=\dim E'_k=k$.

### Question III.5.c

> [!INDICATION]
> Identifier les deux quotients de Rayleigh par l’application isométrique.

#### Solution

Pour $x\ne0$, le quotient de $A'$ en $x$ vaut $X^TQ^TAQX/(X^TX)=R(qx)$. Appliquée à $A'$, III.3 donne $\lambda'_k=\max_{x\in(E'_k)^*}R(qx)=\max_{z\in q(E'_k)^*}R(z)$.

### Question III.5.d

> [!INDICATION]
> Le maximum trouvé est celui d’un candidat au minimum de III.4.c.

#### Solution

Par III.5.b.iii, $q(E'_k)$ est de dimension $k$. La formule de III.4.c minore donc son maximum par $\lambda_k$. D’où $\lambda'_k\ge\lambda_k$.

### Question III.5.e

> [!INDICATION]
> Pour la borne supérieure, utiliser le sous-espace supérieur de la matrice comprimée.

#### Solution

Posons $F'_k=\operatorname{Vect}(e'_k,\ldots,e'_{d-1})$, de dimension $d-k$. Alors $\lambda'_k=\min_{z\in q(F'_k)^*}R(z)$ par III.2 appliquée à $A'$ et par l’égalité des quotients. L’image est de dimension $d-k=d-(k+1)+1$. III.4.d pour l’indice $k+1$ majore ce minimum par $\lambda_{k+1}$. Finalement $\lambda_k\le\lambda'_k\le\lambda_{k+1}$ pour $1\le k\le d-1$.
![Exemple de compression d’une matrice symétrique de taille trois sur un plan. Ses deux valeurs propres s’intercalent parmi les trois valeurs propres initiales.](figures/entrelacement.svg)

## Sources et rapport du jury

Le jury demande p. 2 de discuter le cas où la covariance s’annule et de justifier le temps de première panne par les transitions. En algèbre, il insiste p. 4 sur les différentes composantes dominantes et p. 5–6 sur le caractère rectangulaire de Q dans la compression.

[Énoncé de la Banque PT](https://www.banquept.fr/documents/2021/math_a_2021_pt.pdf) · [Rapport du jury](https://www.banquept.fr/documents/ecrit/rapport/2021/rapport_math_a_ecrit_2021.pdf)
