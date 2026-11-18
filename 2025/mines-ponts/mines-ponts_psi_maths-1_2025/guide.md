# Mines-Ponts PSI — Mathématiques 1 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

On cherche à reconnaître les matrices semblables à leur inverse. Les deux premières parties exploitent les coefficients et les racines du polynôme caractéristique. La suite étudie les produits de symétries, les matrices nilpotentes et la décomposition en blocs admise dans l’énoncé.

## Partie 1 — Polynômes réciproques

### Question 1

> [!INDICATION]
> Dans le polynôme renversé, cherchez de quel terme provient le coefficient de degré $k$.

#### Solution

On développe puis on change l’indice de sommation.
$$
\begin{aligned}
X^pP(1/X)&=\sum_{k=0}^pa_kX^{p-k},\\
&=\sum_{k=0}^pa_{p-k}X^k.
\end{aligned}
$$
Par unicité des coefficients, $P$ est réciproque si et seulement si $a_k=a_{p-k}$ pour tout $k\in\{0,\ldots,p\}$.

### Question 2

> [!INDICATION]
> Répartissez le facteur $X^p$ entre les facteurs de multiplicité $m_i$. Regardez aussi le terme constant de $P$.

#### Solution

Comme $\sum_{i=1}^d m_i=p$, on obtient l’identité polynomiale
$$
X^pP(1/X)=a_p\prod_{i=1}^d(1-\lambda_iX)^{m_i}.
$$
Si $P$ est réciproque, Q1 donne $P(0)=a_p\ne0$. Chaque $\lambda_i$ est donc non nul.

Les facteurs $1-\lambda_iX$ s’annulent aux points distincts $1/\lambda_i$. Comme le produit ci-dessus est $P$, chacun de ces points est racine de multiplicité exactement $m_i$.

### Question 3

> [!INDICATION]
> Évaluez l’identité en 1, factorisez par $X-1$, puis appliquez le renversement au facteur restant.

#### Solution

En $X=1$, l’antiréciprocité donne $Q(1)=-Q(1)$, donc $Q(1)=0$. Écrivons $Q=(X-1)P$ avec $\deg P=p-1$. En reportant dans l’identité,
$$
(X-1)P(X)=(X-1)X^{p-1}P(1/X).
$$
On simplifie le facteur commun et on conclut que $P$ est constant si $p=1$, et réciproque sinon.

### Question 4

> [!INDICATION]
> Regroupez les racines par paires inverses en isolant les points fixes de l’inversion.

#### Solution

Les racines différentes de $1$ et de $-1$ se répartissent en paires $\{a,1/a\}$ de multiplicité commune $m$. Chaque paire contribue $a^m(1/a)^m=1$ au produit.

Le facteur issu de $1$ vaut 1 et celui issu de $-1$ vaut $(-1)^{m_-}$, où $m_-$ est sa multiplicité, égale à zéro si cette racine est absente.

Le produit vaut donc **$(-1)^{m_-}\in\{-1,1\}$**.

### Question 5

> [!INDICATION]
> Comparez les racines avec multiplicités et le coefficient dominant du polynôme renversé.

#### Solution

Notons $p=\deg R$, $a_p$ son coefficient dominant et $a_0$ son terme constant.

Comme 0 n’est pas racine, $X^pR(1/X)$ est de degré $p$. Par la factorisation de Q2, ses racines sont les inverses de celles de $R$, avec les mêmes multiplicités. Par hypothèse, cette liste est celle de $R$.

Ces deux polynômes sont donc proportionnels. Le rapport du renversé à $R$ vaut $a_0/a_p$.

En évaluant la factorisation de $R$ en zéro, on trouve que $a_0/a_p$ est $(-1)^p$ fois le produit des racines avec multiplicités. La Q4 donne $a_0/a_p=\pm1$. **Ainsi $R$ est réciproque ou antiréciproque.**

## Partie 2 — Le cas diagonalisable

### Question 6

> [!INDICATION]
> Faites apparaître $A^{-1}$ dans la factorisation matricielle avant de prendre les déterminants.

#### Solution

Pour $x\ne0$, on a $xI_n-A=(-xA)(x^{-1}I_n-A^{-1})$. Par multiplicativité du déterminant,
$$
\boxed{\det(xI_n-A)=(-x)^n\det(A)\det(x^{-1}I_n-A^{-1}).}
$$

### Question 7

> [!INDICATION]
> La similitude conserve le déterminant et le polynôme caractéristique. Reportez ces invariants dans Q6.

#### Solution

Comme $A$ et $A^{-1}$ sont semblables, $\det A=\det A^{-1}=1/\det A$. Ainsi **$\det A\in\{1,-1\}$**. Elles ont aussi le même polynôme caractéristique, puisque le changement de base conjugue également $XI_n-A$. En posant $\varepsilon=(-1)^n\det A$, Q6 donne
$$
\chi_A(x)=\varepsilon x^n\chi_A(1/x)
\qquad (x\in\mathbb R^*).
$$
L’égalité vaut en tant qu’identité polynomiale, puisqu’elle vaut en une infinité de points. Selon le signe de $\varepsilon$, $\chi_A$ est réciproque ou antiréciproque.

### Question 8

> [!INDICATION]
> Comparez les termes constants et les multiplicités des racines inverses. Utilisez ensuite les matrices diagonales.

#### Solution

Le renversé de $\chi_B$ a pour terme constant le coefficient dominant de $\chi_B$, soit 1. La réciprocité ou l’antiréciprocité donne donc $\chi_B(0)=\pm1$. Ainsi $B$ est inversible. Dans les deux cas, la factorisation du renversé en Q2 montre que les valeurs propres s’apparient par inversion avec les mêmes multiplicités algébriques.

Comme $B$ est diagonalisable, elle est semblable à une diagonale $D$ contenant chaque valeur propre selon sa multiplicité. La matrice $B^{-1}$ est semblable à $D^{-1}$.

Les diagonales de $D$ et $D^{-1}$ ne diffèrent que par une permutation, donc **$B$ et $B^{-1}$ sont semblables**.

### Question 9

> [!INDICATION]
> Comparez les dimensions des espaces propres pour 2. On peut lire l’espace propre de l’inverse directement sur $B$.

#### Solution

Dans la base canonique $(e_1,e_2,e_3,e_4)$, l’équation $Bv=2v$ impose que les deux dernières composantes soient nulles. Ainsi $E_2(B)=\operatorname{Vect}(e_1,e_2)$. D’autre part, $B^{-1}v=2v$ équivaut à $Bv=\tfrac12v$.

Pour cette seconde équation, les deux premières composantes sont nulles et la quatrième l’est aussi, à cause du coefficient 1 au-dessus de la diagonale du second bloc. Ainsi $E_2(B^{-1})=\operatorname{Vect}(e_3)$.

Ces deux espaces ont des dimensions différentes, alors qu’une similitude induit un isomorphisme entre les espaces propres pour une même valeur propre. **$B$ n’est donc pas semblable à $B^{-1}$.**

## Partie 3 — Produits de matrices de symétries

### Question 10

> [!INDICATION]
> Inversez le produit et essayez de le conjuguer par l’un de ses facteurs.

#### Solution

Puisque $S_i^2=I_n$, chaque facteur est inversible et s’inverse en lui-même. Il s’ensuit que $A^{-1}=S_2S_1$. De plus,
$$
S_1^{-1}AS_1=S_2S_1=A^{-1}.
$$
Donc **$A$ est semblable à son inverse**.

### Question 11

> [!INDICATION]
> Conjuguez le produit entier et répartissez le changement de base entre les deux facteurs.

#### Solution

Oui. Si $A=S_1S_2$ et $A'=R^{-1}AR$, alors
$$
A'=(R^{-1}S_1R)(R^{-1}S_2R).
$$
Pour chaque $i$, le carré de $R^{-1}S_iR$ est $R^{-1}S_i^2R=I_n$. Les deux facteurs sont donc encore des matrices de symétries.

### Question 12

> [!INDICATION]
> Calculez les carrés des deux matrices par blocs, puis exploitez la condition obtenue sur $P$ et $Q$.

#### Solution

On a $S_1^2=\operatorname{diag}(PQ,QP)$, donc $S_1$ est une matrice de symétrie si et seulement si $Q=P^{-1}$. Par multiplication,
$$
S_2=S_1A=\begin{pmatrix}0&PC\\ QB&0\end{pmatrix},
\qquad S_2^2=\operatorname{diag}(PCQB,QBPC).
$$
Les blocs $PC$ et $QB$ sont inversibles. Si l’un de leurs produits vaut $I_n$, chaque bloc est l’inverse de l’autre et le produit dans l’autre ordre vaut aussi $I_n$. En substituant $Q=P^{-1}$, on trouve les conditions nécessaires et suffisantes
$$
\begin{aligned}
Q&=P^{-1},\\
PCP^{-1}&=B^{-1}.
\end{aligned}
$$

### Question 13

> [!INDICATION]
> Identifiez le changement de base fourni par la similitude et reprenez la construction de Q12.

#### Solution

Si $C$ est semblable à $B^{-1}$, il existe $P\in GL_n$ tel que $C=P^{-1}B^{-1}P$. Avec $Q=P^{-1}$, les conditions de Q12 sont remplies.

Les matrices $S_1$ et $S_2=S_1A$ ainsi construites sont des matrices de symétries. Comme $S_1^2=I_{2n}$, **$A=S_1S_2$**.

## Partie 4 — La matrice $J_n(\lambda)$

### Question 14

> [!INDICATION]
> Choisissez un vecteur dont l’image par le dernier itéré non nul est non nulle. Faites agir des puissances de $g$ sur une relation linéaire.

#### Solution

Choisissons $v\in E$ tel que $g^{n-1}(v)\ne0$. Supposons qu’une combinaison des $g^j(v)$ pour $0\leq j\leq n-1$ s’annule, avec au moins un coefficient non nul. Soit $j_0$ le plus petit indice d’un tel coefficient.

En appliquant $g^{n-1-j_0}$ à la relation, les termes d’indice supérieur s’annulent puisque $g^n=0$. Il reste un multiple non nul de $g^{n-1}(v)$, contradiction. Les $n$ vecteurs sont donc libres et forment une base.

Dans l’ordre $(g^{n-1}(v),\ldots,g(v),v)$, $g$ envoie le premier vecteur sur zéro et chaque autre sur celui qui précède. Sa matrice est donc **$N$**.

### Question 15

> [!INDICATION]
> Factorisez par $\lambda$ puis inversez l’identité plus une matrice nilpotente au moyen d’une somme géométrique finie.

#### Solution

Puisque $N^n=0$, le produit de $I_n+\lambda^{-1}N$ par $\sum_{k=0}^{n-1}(-\lambda^{-1}N)^k$ est $I_n$. La somme commute avec le premier facteur. Cela donne un inverse bilatère et
$$
\begin{aligned}
J_n(\lambda)^{-1}&=\lambda^{-1}I_n+N',\\
N'&=\sum_{k=1}^{n-1}(-1)^k\lambda^{-k-1}N^k.
\end{aligned}
$$

### Question 16

> [!INDICATION]
> Factorisez $N'$ par $N$. Pour appliquer Q14, vérifiez aussi que l’avant-dernière puissance est non nulle.

#### Solution

On peut écrire $N'=N(-\lambda^{-2}I_n+NR(N))$ pour un polynôme $R$. Cette écriture vaut aussi lorsque $n=1$, car alors $N=0$.

Les facteurs commutent. On a donc $(N')^n=0$.

Dans $(N')^{n-1}$, chaque terme utilisant $NR(N)$ contient au moins $n$ facteurs $N$ et s’annule. Il reste
$$
(N')^{n-1}=(-\lambda^{-2})^{n-1}N^{n-1}\ne0.
$$
En effet, $N^{n-1}$ envoie le dernier vecteur canonique sur le premier. Le résultat inclut $n=1$, pour lequel cette puissance est l’identité. Par Q14, $N'$ est semblable à $N$, donc **$J_n(\lambda)^{-1}$ est semblable à $J_n(1/\lambda)$**.

### Question 17

> [!INDICATION]
> Dans la composition, appliquez d’abord la substitution du facteur de droite.

#### Solution

Pour tout polynôme $P$, on a $s_1^2(P)(X)=P(-(-X))=P(X)$ et $s_2^2(P)(X)=P(1-(1-X))=P(X)$. Donc $s_1^2=s_2^2=\operatorname{Id}$.

D’autre part, $s_1(s_2(P))(X)=s_2(P)(-X)=P(1+X)$. Par définition de $g$, on obtient **$s_1\circ s_2=\operatorname{Id}+g$**.

### Question 18

> [!INDICATION]
> Examinez le terme de plus haut degré de chaque différence $(X+1)^k-X^k$.

#### Solution

Soient $d\geq1$ le degré de $P$ et $a_d$ son coefficient dominant. Dans $a_d((X+1)^d-X^d)$, le terme dominant est $d a_dX^{d-1}$.

Pour chaque monôme de degré $k<d$, la différence correspondante est nulle si $k=0$ et de degré au plus $k-1$ sinon. Aucun de ces termes ne compense celui de degré $d-1$. Donc **$\deg(g(P))=d-1$**.

### Question 19

> [!INDICATION]
> Vérifiez l’indice de nilpotence de $g$ sur un polynôme de degré maximal, puis représentez l’identité et les deux symétries dans la même base.

#### Solution

Sur $\mathbb C_{n-1}[X]$, chaque application de $g$ abaisse le degré d’un polynôme non constant et annule les constantes, donc $g^n=0$.

En appliquant $g$ exactement $n-1$ fois à $X^{n-1}$, on obtient une constante non nulle par Q18. Pour $n=1$, ce constat vaut directement puisque $g^0$ est l’identité.

Par Q14, il existe une base dans laquelle $g$ a pour matrice $N$ et $\operatorname{Id}+g$ a pour matrice $J_n(1)$.

Dans cette même base, les matrices de $s_1$ et $s_2$ ont un carré égal à l’identité. Par Q17, **leur produit est $J_n(1)$**.

## Partie 5 — Une caractérisation des matrices semblables à leur inverse

### Question 20

> [!INDICATION]
> Inversez les blocs un par un, puis assemblez les similitudes obtenues en Q16.

#### Solution

L’inversion préserve la similitude. La matrice $A^{-1}$ est donc semblable à l’inverse de la matrice diagonale par blocs donnée, soit $\operatorname{diag}(J_{n_i}(\lambda_i)^{-1})_{1\leq i\leq r}$. Toutes les $\lambda_i$ sont non nulles par inversibilité. Par Q16, chaque bloc inverse est semblable à $J_{n_i}(1/\lambda_i)$. La matrice diagonale par blocs formée avec les changements de base de Q16 établit la similitude demandée.

### Question 21

> [!INDICATION]
> Utilisez l’unicité de la liste des blocs pour former des paires de même taille. Traitez séparément les valeurs propres fixes par inversion.

#### Solution

Puisque $A$ et $A^{-1}$ sont semblables, Q20 et l’unicité des blocs à l’ordre près montrent que le nombre de blocs de taille $m$ et valeur propre $\lambda$ égale celui des blocs de taille $m$ et valeur propre $1/\lambda$.

Pour $\lambda\ne\pm1$, on apparie donc chaque bloc avec un bloc de même taille et de valeur propre inverse.

Pour une telle paire, la Q16 assure que le second bloc est semblable à l’inverse du premier. La Q13 montre que leur somme diagonale est un produit de deux matrices de symétries. Les blocs de valeur propre $1$ ou $-1$ sont chacun de cette forme par Q19 et par le résultat admis pour $-1$.

Après réordonnement des blocs, on réunit les premiers facteurs sur une diagonale par blocs et les seconds sur une autre. Chacune de ces deux matrices a son carré égal à l’identité, et leur produit est la matrice réordonnée. La Q11 transporte cette factorisation à $A$.

**Une matrice inversible est donc semblable à son inverse si et seulement si elle est produit de deux matrices de symétries**, la réciproque étant donnée par Q10.

## Bilan

- Un polynôme renversé permet de suivre les multiplicités des racines inverses.
- Pour établir une similitude entre matrices nilpotentes cycliques, vérifiez l’indice exact de nilpotence puis construisez la base dans le bon ordre.
- Pour réutiliser une factorisation dans une somme diagonale, assemblez séparément les premiers et les seconds facteurs.
