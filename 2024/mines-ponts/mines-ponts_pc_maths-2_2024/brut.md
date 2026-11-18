# Mines-Ponts PC — Mathématiques 2 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie 1 — Matrices de Hadamard

### Question 1

La matrice $(1)$ convient en ordre 1. En ordre 2, on prend

$$
H_2=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

Ses lignes sont orthogonales et ont chacune pour norme $\sqrt2$. Ainsi $H_2/\sqrt2$ est orthogonale.

### Question 2

Changer le signe d’une ligne ou permuter deux lignes de $H/\sqrt n$ transforme sa famille de lignes orthonormée en une autre famille orthonormée. Pour les mêmes opérations sur les colonnes, on utilise leur orthonormalité. Les entrées restent dans $\{-1,1\}$, donc chaque matrice obtenue est de Hadamard.

### Question 3

Pour chaque colonne dont l’entrée de première ligne est $-1$, on applique le changement de signe de Q2. La première ligne est alors entièrement égale à 1. Si $n\ge2$, son produit scalaire avec la deuxième ligne est nul. La deuxième ligne comporte donc autant d’entrées $1$ que $-1$, ce qui impose **$n$ pair**.

### Question 4

Après Q3, on permute les colonnes de manière à ranger les $n/2$ coefficients $1$ de la deuxième ligne avant les $n/2$ coefficients $-1$. La première ligne reste constante.

Soient $a$ et $b$ les nombres de $1$ dans les deux moitiés de la troisième ligne.

Son orthogonalité à la première ligne donne $2(a+b)-n=0$. Son orthogonalité à la deuxième donne $(2a-n/2)-(2b-n/2)=0$. On en déduit $a=b=n/4$. Comme $a$ est entier, **$4$ divise $n$**.

## Partie 2 — Endomorphismes symétriques

### Question 5

Le théorème spectral pour un endomorphisme symétrique réel donne une base orthonormée de vecteurs propres. En les rangeant dans l’ordre croissant de leurs valeurs propres comptées avec multiplicité, on obtient **$f(e_i)=\lambda_i e_i$** pour tout $i$.

### Question 6

La dimension de $T_k$ est $n-k+1$, car les vecteurs $e_k,\ldots,e_n$ sont indépendants. La formule des dimensions donne

$$
\dim(S_k\cap T_k)=k+(n-k+1)-\dim(S_k+T_k)\ge1.
$$

Il existe donc un vecteur non nul dans l’intersection.

### Question 7

On choisit un vecteur non nul de $S_k\cap T_k$ et on le normalise. Écrivons-le $x=\sum_{i=k}^n c_i e_i$, avec $\sum_{i=k}^nc_i^2=1$. Alors

$$
\begin{aligned}
(x,f(x))&=\sum_{i=k}^n\lambda_i c_i^2\\
&\ge\lambda_k.
\end{aligned}
$$

Comme $x$ est admissible dans le maximum sur les vecteurs unitaires de $S_k$, ce maximum est au moins $\lambda_k$.

### Question 8

Q7 donne une borne inférieure $\lambda_k$ pour tous les maxima. Pour $S=\operatorname{Vect}(e_1,\ldots,e_k)$, tout vecteur unitaire a une décomposition avec des coefficients dont la somme des carrés vaut 1.

Le produit $(x,f(x))$ est alors une moyenne pondérée des $\lambda_i$ pour $i\le k$, donc vaut au plus $\lambda_k$. L’égalité est réalisée par $x=e_k$. Ce choix de $S$ atteint la borne inférieure, d’où

$$
\boxed{\lambda_k=\min_{S\in\pi_k}\ \max_{\substack{x\in S\\\|x\|=1}}(x,f(x)).}
$$

### Question 9

Si $M$ est symétrique positive, le théorème spectral donne $M=O\operatorname{diag}(\mu_1,\ldots,\mu_n)O^T$, avec $O$ orthogonale et $\mu_i\ge0$. En prenant $B=\operatorname{diag}(\sqrt{\mu_1},\ldots,\sqrt{\mu_n})O^T$, on a $M=B^TB$.

Dans le second cas, on complète $u$ en une base orthonormée de vecteurs propres de $M$. Dans cette base, $\lambda uu^T-M$ a une valeur propre nulle sur $u$ et sur chaque autre vecteur propre une valeur propre égale à l’opposé de celle de $M$. Toutes sont positives ou nulles. La première partie fournit donc

$$
\boxed{M=\lambda uu^T-B^TB.}
$$

## Partie 3 — Caractérisation des MDE

### Question 10

La matrice $ee^T$ est symétrique, donc $P$ aussi. Puisque $e^Te=n$, pour tout vecteur $x$,

$$
Px=x-\frac{e^Tx}{n}e.
$$

Le vecteur retranché appartient à $\operatorname{Vect}(e)$ et $e^TPx=0$. Cette décomposition orthogonale prouve que $P$ est la projection sur $\operatorname{Vect}(e)^\perp$. En particulier $Pe=0$ et $P^2=P$.

### Question 11

L’entrée $(i,j)$ de $D$ vaut $\|x_i-x_j\|^2=\|x_i\|^2+\|x_j\|^2-2x_i^Tx_j$. Ainsi

$$
D=Ce^T+eC^T-2M_A^TM_A.
$$

En multipliant par $P$ des deux côtés, les deux termes qui contiennent $e$ disparaissent. Il vient $T(D)=(M_AP)^T(M_AP)$. Cette matrice est symétrique positive et annule $e$, car $Pe=0$. Donc **$T(D)\in\Omega_n$**.

### Question 12

Par Q9, écrivons $A=B^TB$ et notons $b_i$ les colonnes de $B$. Alors $a_i=A_{ii}=\|b_i\|^2$ et

$$
K(A)_{ij}=\|b_i\|^2+\|b_j\|^2-2b_i^Tb_j=\|b_i-b_j\|^2.
$$

Les $n$ points $b_i$ de $\mathbb R^n$ réalisent donc $K(A)$, qui est une MDE.

### Question 13

Pour $A\in\Omega_n$, on a $Ae=0$ et $e^TA=0$ par symétrie.

Ainsi $AP=PA=A$. D’après Q12, $T$ est applicable à $K(A)$.

Les termes $ea^T$ et $ae^T$ s’annulent par multiplication par $P$ des deux côtés, et le terme $-2A$ donne

$$
\boxed{T(K(A))=PAP=A.}
$$

### Question 14

Si $D$ est une MDE, la positivité de $-PDP/2$ suit de Q11.

Réciproquement, supposons $A=-PDP/2$ positive. Elle est symétrique et annule $e$, donc $A\in\Omega_n$.

Pour deux indices $i,j$, notons $v=e_i-e_j$, avec $e_i,e_j$ les vecteurs de la base canonique.

Comme $v$ est orthogonal à $e$, $Pv=v$. La diagonale nulle et la symétrie de $D$ donnent

$$
v^TAv=-\tfrac12v^TDv=d_{ij}.
$$

Par ailleurs, $v^TAv=A_{ii}+A_{jj}-2A_{ij}=K(A)_{ij}$. Ainsi $D=K(A)$ et Q12 donne **$D\in\Delta_n$**.

### Question 15

Normalisons le vecteur propre $e$ en posant $u=e/\sqrt n$. Par Q9, la matrice considérée s’écrit $D=\lambda uu^T-B^TB$, où $\lambda>0$ est la valeur propre dont l’espace propre est de dimension 1. Puisque $Pu=0$, il vient

$$
-\tfrac12 PDP=\tfrac12(BP)^T(BP).
$$

Cette matrice est positive. Les conditions sur les entrées et la diagonale permettent d’appliquer Q14. Donc $D$ est une MDE.

## Partie 4 — Spectre des MDE

### Question 16

La somme des valeurs propres comptées avec multiplicité est la trace. Comme une MDE a une diagonale nulle, **$\sum_{i=1}^n\lambda_i=0$**.

### Question 17

Par Q11, $-PDP/2$ est positive. Pour $x\in\operatorname{Vect}(e)^\perp$, on a $Px=x$. Ainsi $0\le -x^TDx/2$, soit **$x^TDx\le0$**.

### Question 18

Une MDE non nulle impose $n\ge2$. L’espace $\operatorname{Vect}(e)^\perp$ est de dimension $n-1$. Q7 appliquée à cet espace donne que le maximum de $x^TDx$ sur ses vecteurs unitaires est au moins $\lambda_{n-1}$. Par Q17, ce maximum est négatif ou nul, donc $\lambda_{n-1}\le0$.

Il y a au plus une valeur propre strictement positive, multiplicités comprises. Si toutes étaient négatives ou nulles, leur somme nulle par Q16 les obligerait à être toutes nulles, et la symétrie de $D$ donnerait $D=0$ par diagonalisation. Il y a donc exactement une valeur propre strictement positive, $\lambda_n$.

## Partie 5 — Problème inverse

### Question 19

Comme $U$ est orthogonale, $D=U^T\Lambda U$ est symétrique et semblable à $\Lambda$. Ses valeurs propres sont les $\lambda_i$ et l’espace propre pour $\lambda_1$ est de dimension 1, puisque les autres sont négatives ou nulles.

Notons $h_{ki}$ les entrées de $H$. Comme elles valent $\pm1$, chaque entrée diagonale de $D$ vaut $n^{-1}\sum_k\lambda_k=0$. Pour tous $i,j$, la première ligne constante donne

$$
nd_{ij}=\lambda_1+\sum_{k=2}^n\lambda_k h_{ki}h_{kj}.
$$

Chaque produit $h_{ki}h_{kj}$ est au plus 1. Comme $\lambda_k\le0$ pour $k\ge2$, le membre de droite est au moins $\lambda_1+\sum_{k=2}^n\lambda_k=0$. **Toutes les entrées sont positives ou nulles.**

### Question 20

La première colonne de $U^T$ est $e/\sqrt n$ puisque la première ligne de $H$ est constante égale à 1. C’est un vecteur propre de $D$ associé à $\lambda_1$, car $DU^T=U^T\Lambda$.

Donc $e$ est un vecteur propre pour l’unique valeur propre strictement positive, simple. D’après Q19, $D$ remplit les autres conditions de Q15. **$D$ est une MDE.**

### Question 21

On choisit la matrice de Hadamard

$$
H=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}.
$$

Les quatre lignes sont orthogonales deux à deux et chacune a pour norme 2. On applique Q19–Q20 avec $U=H/2$ et $\Lambda=\operatorname{diag}(5,-1,-2,-2)$. Le calcul donne

$$
\boxed{D=\begin{pmatrix}
0&3/2&2&3/2\\
3/2&0&3/2&2\\
2&3/2&0&3/2\\
3/2&2&3/2&0
\end{pmatrix}.}
$$

Cette matrice est une MDE et sa similitude à $\Lambda$ donne le spectre demandé.
