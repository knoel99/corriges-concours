# DGFiP Inspecteur externe — Mathématiques, statistiques et probabilités 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Les quatre exercices couvrent l’intégralité de la partie 2 à réponses courtes, pages 14 à 16 du cahier. Le QCM commun figure séparément dans le même cahier.*

## Présentation du sujet

Quatre exercices indépendants portant sur des séries de fonctions, une loi discrète, des matrices et une parabole.

## Exercice 1 — Série de fonctions

### Question 1

> [!INDICATION]
> Fixe $x$ et compare au terme d’une série de Riemann convergente.

#### Solution

Pour $x$ fixé, $|u_n(x)|=2|x|/(x^2+n^2\pi^2)\le 2|x|/(n^2\pi^2)$. La série numérique de ce majorant converge. La série converge donc absolument en chaque $x$, notamment en zéro où les termes sont nuls.

### Question 2

> [!INDICATION]
> Sur un segment, majore le numérateur par $2a$. Sur la droite entière, teste $x=n\pi$.

#### Solution

Sur $[-a,a]$, la norme uniforme est majorée par $2a/(n^2\pi^2)$, donc la convergence est normale. Sur $\mathbb R$, l’inégalité $(|x|-n\pi)^2\ge0$ donne $|u_n(x)|\le1/(n\pi)$, avec égalité à $x=n\pi$. La somme des normes diverge : la convergence n’est pas normale sur $\mathbb R$.

### Question 3

> [!INDICATION]
> La convergence normale sur un segment entraîne la convergence uniforme sur ce segment.

#### Solution

Les $u_n$ sont continues sur $\mathbb R$, leurs dénominateurs étant strictement positifs. La somme $U$ est continue sur chacun des segments $[-a,a]$ par convergence uniforme. Chaque réel appartient à l’intérieur d’un tel segment, donc $U$ est continue partout.

## Exercice 2 — Loi discrète

### Question 1

> [!INDICATION]
> Itère la relation de récurrence et utilise la somme des probabilités.

#### Solution

Si $p_1=\mathbb P(X=1)$, on obtient $\mathbb P(X=n)=p_1\,4^{n-1}/(n-1)!$ pour tout $n\ge1$. La somme des coefficients vaut $e^4$, donc $\mathbb P(X=1)=e^{-4}$ et $\mathbb P(X=n)=e^{-4}4^{n-1}/(n-1)!$.

### Question 2

> [!INDICATION]
> Reconnais la loi de $X-1$, puis regarde l’effet d’une translation.

#### Solution

Pour $k\ge0$, $\mathbb P(X-1=k)=e^{-4}4^k/k!$. Ainsi $X-1$ suit la loi de Poisson de paramètre 4. Donc $\mathbb E(X)=5$ et $\mathrm{Var}(X)=4$.

## Exercice 3 — Matrice à coefficients constants

### Question 1(a)

> [!INDICATION]
> Chaque coefficient du produit additionne $n$ termes égaux à 1.

#### Solution

$J^2=nJ$.

### Question 1(b)

> [!INDICATION]
> Pose $J=A-I_n$ dans le polynôme annulateur de $J$.

#### Solution

On a $(A-I_n)^2-n(A-I_n)=0$. Le polynôme $(T-1)(T-(n+1))=T^2-(n+2)T+n+1$ annule donc $A$.

### Question 2

> [!INDICATION]
> Isole le terme constant dans la relation quadratique.

#### Solution

La relation $A((n+2)I_n-A)=(n+1)I_n$ donne $A^{-1}=((n+2)I_n-A)/(n+1)=I_n-J/(n+1)$.

### Question 3(a)

> [!INDICATION]
> Quel théorème s’applique à une matrice réelle symétrique ?

#### Solution

La matrice $A$ est réelle symétrique. Le théorème spectral donne une base orthonormée de vecteurs propres. En les mettant en colonnes dans $P$, on obtient $P$ orthogonale et $A=PDP^{-1}$ avec $D$ diagonale.

### Question 3(b)

> [!INDICATION]
> Sépare le vecteur dont toutes les coordonnées valent 1 et les vecteurs dont la somme des coordonnées vaut zéro.

#### Solution

Si $e=(1,\ldots,1)^T$, alors $Je=ne$ et $Ae=(n+1)e$. Sur l’hyperplan de somme nulle, $J$ agit par zéro et $A$ par l’identité. On peut donc prendre $D=\operatorname{diag}(n+1,1,\ldots,1)$. Pour $n=1$, seule la valeur propre 2 figure.

## Exercice 4 — Parabole et tangentes

### Question 1

> [!INDICATION]
> Remplace $t$ par la coordonnée $y$.

#### Solution

On a $x=y^2$ et toutes les valeurs réelles de $y$ sont atteintes. C’est la parabole de sommet $O$, d’axe horizontal $Ox$, ouverte vers les abscisses positives.

### Question 2

> [!INDICATION]
> Dérive le couple de coordonnées. Un vecteur normal a un produit scalaire nul avec la dérivée.

#### Solution

Le vecteur $(2t,1)$ est tangent car il est la dérivée du paramétrage et ne s’annule jamais. Le vecteur $(1,-2t)$ lui est orthogonal et donne une normale.

### Question 3

> [!INDICATION]
> Soustrais les deux équations de tangentes, puis utilise $a
e b$.

#### Solution

La soustraction donne $(a-b)(a+b-2y)=0$. Donc $y=(a+b)/2$. En reportant dans la première équation, $x=2ay-a^2=ab$. Les tangentes se coupent en $M(ab\,;\,(a+b)/2)$.

## Bilan

Pour la convergence, précise le domaine. Pour une matrice, vérifie la dimension des sous-espaces propres.
