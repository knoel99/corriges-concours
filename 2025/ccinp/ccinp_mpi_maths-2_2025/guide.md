# CCINP MPI — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve dure quatre heures, sans calculatrice. Les deux exercices et le problème sont indépendants. Le premier exercice relie une inégalité sur le logarithme, la moyenne arithmético-géométrique et le déterminant d’une matrice symétrique définie positive. Le second construit une base orthonormale de polynômes en transformant un produit scalaire intégral en intégrales trigonométriques.

Le problème étudie les matrices de rang $1$. Les calculs de probabilités, le rang et la trace occupent la première partie. Dans la seconde, le noyau et l’image guident le calcul des polynômes caractéristique et minimal, puis la construction de bases de réduction. Les points les plus délicats sont le traitement des bornes de l’intégrale en Q9 et Q12, puis le choix de l’ordre des vecteurs de base en Q23.

Les trois blocs peuvent être abordés séparément. À l’intérieur de chacun, rédige les questions dans l’ordre pour réutiliser les résultats déjà établis. C’est aussi une exigence que le rapport 2025 rappelle pour la présentation de la copie.

## Exercice 1

L’égalité dans l’inégalité logarithmique détermine toutes les conditions d’égalité de l’exercice. Repère comment elle se transmet quand on passe des nombres aux valeurs propres, puis aux coefficients diagonaux.

### Question 1

> [!INDICATION]
> Compare le logarithme à sa tangente en $1$.

> [!INDICATION]
> Étudie la différence par dérivation, puis applique l’inégalité à des quotients ayant tous le même dénominateur.

#### Solution

Sur $]0,+\infty[$, la fonction $g(t)=t-1-\ln t$ a pour dérivée
$$g'(t)=\frac{t-1}{t}.$$
Elle décroît strictement jusqu’à $1$ puis croît strictement. Son minimum vaut $g(1)=0$ et il est atteint en $1$ seulement.

Comme $m>0$, on applique ce résultat à chaque $x_k/m$. En sommant pour $k$ de $1$ à $n$, on obtient
$$\boxed{\sum_k\ln\!\left(\frac{x_k}{m}\right)
\le \sum_k\left(\frac{x_k}{m}-1\right).}$$

### Question 2

> [!INDICATION]
> Simplifie le membre de droite de Q1 en utilisant la définition de la moyenne $m$.

> [!INDICATION]
> Transforme la somme des logarithmes en un seul logarithme, puis utilise une fonction strictement croissante pour revenir au produit.

#### Solution

Le membre de droite de Q1 est nul, puisque $\sum_{k=1}^n x_k=nm$. On en déduit
$$\ln\!\left(\frac{\prod_{k=1}^n x_k}{m^n}\right)\le 0.$$
L’exponentielle est croissante, donc $\prod_{k=1}^n x_k\le m^n$. Par croissance de la racine $n$-ième sur les réels positifs, on obtient, avec les mêmes indices,
$$\boxed{\left(\prod_k x_k\right)^{1/n}\le \frac1n\sum_k x_k.}$$

> [!JURY]
> Le rapport 2025 relève la difficulté à déduire cette inégalité de Q1. La rédaction doit faire apparaître la simplification de la somme et le passage du logarithme au produit.

### Question 3

> [!INDICATION]
> Remonte les transformations de Q2 dans le cas d’égalité.

> [!INDICATION]
> Regarde les signes des écarts terme à terme en Q1, puis cherche quand chacun peut s’annuler.

#### Solution

Les transformations de Q2 sont réversibles pour l’égalité. Celle-ci équivaut donc à $\sum_{k=1}^n g(x_k/m)=0$. Les termes sont tous positifs ou nuls. Leur somme est nulle exactement quand chacun est nul.

Par Q1, cela signifie que tous les $x_k$ sont égaux à $m$. Réciproquement, quand les $x_k$ ont tous la même valeur, celle-ci est leur moyenne $m$. **L’égalité a donc lieu si et seulement si $x_1=\cdots=x_n$.**

> [!METHODE]
> Si une somme finie de termes positifs ou nuls s’annule, chacun est nul. Cet argument conserve le cas d’égalité obtenu pour l’inégalité à un seul terme.

### Question 4

> [!INDICATION]
> Quels nombres strictement positifs associés à $B$ peuvent jouer le rôle des $x_k$ ?

> [!INDICATION]
> Exprime la trace et le déterminant après diagonalisation orthogonale. Dans le cas d’égalité, examine ce qu’un changement de base fait à une matrice scalaire.

#### Solution

Par le théorème spectral, la matrice réelle symétrique $B$ est diagonalisable en base orthonormée. Ses valeurs propres $\lambda_1,\ldots,\lambda_n$, comptées avec multiplicité, sont strictement positives car $B$ est définie positive. La trace est leur somme et le déterminant leur produit. La Q2 donne
$$\boxed{(\det B)^{1/n}\le \frac{\operatorname{Tr}(B)}{n}.}$$
Par Q3, l’égalité équivaut à ce que la diagonale obtenue soit $\lambda I_n$ pour une valeur propre commune $\lambda$. Or une matrice semblable à $\lambda I_n$ est égale à $\lambda I_n$. Réciproquement, une matrice scalaire de $S_n^{++}(\mathbb R)$ a toutes ses valeurs propres égales. **L’égalité équivaut à $B\in\operatorname{Vect}(I_n)$.**

### Question 5

> [!INDICATION]
> Applique la définition d’une matrice définie positive à un vecteur canonique.

#### Solution

Pour chaque $i$, le vecteur canonique $e_i$ est non nul. Puisque $A$ est définie positive,
$$\boxed{a_{i,i}=e_i^\top A e_i>0.}$$

### Question 6

> [!INDICATION]
> Vérifie séparément la symétrie de $B$ et le signe de sa forme quadratique sur un vecteur non nul.

> [!INDICATION]
> Calcule les coefficients diagonaux de $B$ et son déterminant, puis exploite le cas d’égalité de Q4.

#### Solution

La matrice $D$ est définie et inversible par Q5. Comme $A$ et $D$ sont symétriques, $(DAD)^\top=DAD$. Pour $v\ne 0$, on a $Dv\ne 0$, d’où
$$v^\top Bv=(Dv)^\top A(Dv)>0.$$
Ainsi $B$ est symétrique définie positive. Son coefficient diagonal d’indice $i$ est $a_{i,i}/a_{i,i}=1$, donc $\operatorname{Tr}(B)=n$. Par Q4, $(\det B)^{1/n}\le1$, d’où $\det B\le1$.

Par multiplicativité du déterminant,
$$\det B=\frac{\det A}{\prod_{i=1}^n a_{i,i}}.$$
Comme les coefficients diagonaux de $A$ sont strictement positifs, on obtient
$$\boxed{\det A\le\prod_{i=1}^n a_{i,i}.}$$
L’égalité a lieu exactement quand $B$ est scalaire. Comme tous ses coefficients diagonaux valent $1$, cela impose $B=I_n$. Dans ce cas, $A=D^{-2}$ est diagonale.

Réciproquement, si $A$ est diagonale, $B$ est diagonale avec des $1$ sur la diagonale, d’où l’égalité. **L’égalité équivaut à ce que $A$ soit diagonale.**

> [!JURY]
> Le rapport 2025 signale l’oubli fréquent de prouver que $B$ est symétrique définie positive. Il faut vérifier cette hypothèse avant d’appliquer Q4.

## Exercice 2

Les deux premières questions établissent le lien entre la récurrence polynomiale et le cosinus. Ce lien rend les produits scalaires calculables une fois la convergence aux deux bornes justifiée.

### Question 7

> [!INDICATION]
> Vérifie les deux premiers rangs pour préparer la récurrence.

> [!INDICATION]
> Dans la formule de récurrence, compare les degrés des deux termes avant de calculer le coefficient dominant.

#### Solution

Le polynôme $P_0=1$ est de degré $0$ et a pour terme dominant $1$. Le polynôme $P_1=X$ est de degré $1$ et a pour terme dominant $X$.

Supposons connus les résultats aux rangs consécutifs $n$ et $n+1$. Le terme dominant de $2XP_{n+1}$ est $2^{n+1}X^{n+2}$. Le polynôme $P_n$ est de degré $n$, donc la soustraction ne peut annuler ce terme.

**Par récurrence double, $\deg P_n=n$ et le terme dominant est $2^{n-1}X^n$ pour $n\ge1$.**

### Question 8

> [!INDICATION]
> Cherche une récurrence vérifiée par la suite des cosinus des multiples de $\theta$.

> [!INDICATION]
> Additionne les deux formules d’addition du cosinus en prenant pour angle commun $(n+1)\theta$.

#### Solution

Soit $\theta\in\mathbb R$. Les deux premières identités résultent de $P_0=1$ et de $P_1=X$.

Supposons la formule vraie aux rangs $n$ et $n+1$. La récurrence donne
$$P_{n+2}(\cos\theta)=2\cos\theta\cos((n+1)\theta)-\cos(n\theta).$$
Par les formules d’addition du cosinus, le membre de droite vaut $\cos((n+2)\theta)$. Ainsi, par récurrence double,
$$\boxed{P_n(\cos\theta)=\cos(n\theta).}$$

### Question 9

> [!INDICATION]
> Repère où la fonction sous l’intégrale est continue et où elle peut devenir non bornée.

> [!INDICATION]
> Majore la valeur absolue du numérateur sur le segment et cherche une primitive du poids.

#### Solution

La fonction sous l’intégrale est continue sur $]-1,1[$ et donc continue par morceaux. Le produit $PQ$ est continu sur le segment $[-1,1]$, donc il existe $C\ge0$ qui majore $|PQ|$ sur ce segment. On a alors, pour $-1<t<1$,
$$\left|\frac{P(t)Q(t)}{\sqrt{1-t^2}}\right|
\le \frac{C}{\sqrt{1-t^2}}.$$
La fonction positive $t\mapsto 1/\sqrt{1-t^2}$ admet $\arcsin$ pour primitive sur $]-1,1[$. Les deux limites de cette primitive aux bornes sont finies. Par comparaison de fonctions positives, **l’intégrale de l’énoncé converge absolument.**

> [!JURY]
> Le rapport 2025 demande de vérifier la continuité par morceaux et de comparer des fonctions positives. Le passage à la valeur absolue fournit ici une comparaison valable indépendamment du signe de $PQ$.

### Question 10

> [!INDICATION]
> Distingue les propriétés algébriques du produit scalaire de la question de savoir quand sa valeur sur $(P,P)$ s’annule.

> [!INDICATION]
> Si $P$ est non nul, trouve un point où il ne s’annule pas, puis utilise la continuité pour passer de ce point à un intervalle.

#### Solution

La convergence établie en Q9 permet d’appliquer la linéarité de l’intégrale. L’application est bilinéaire et symétrique. Elle est positive, car la fonction sous l’intégrale de $\langle P,P\rangle$ est positive ou nulle.

Si $P$ est non nul, il n’a qu’un nombre fini de racines. Il existe donc $t_0\in]-1,1[$ tel que $P(t_0)\ne0$. La fonction sous l’intégrale de $\langle P,P\rangle$ est continue et strictement positive en $t_0$.

Elle est donc minorée par une constante strictement positive sur un petit segment de longueur non nulle contenant ce point. L’intégrale sur ce segment est strictement positive et la fonction intégrée est positive ou nulle ailleurs. Ainsi $\langle P,P\rangle>0$ si $P\ne0$. **On obtient un produit scalaire sur $\mathbb R_k[X]$.**

> [!METHODE]
> Pour établir la positivité stricte d’une intégrale, une valeur strictement positive en un point suffit ici grâce à la continuité. La contribution d’un petit intervalle autour du point est alors strictement positive.

### Question 11

> [!INDICATION]
> Transforme le produit des deux cosinus en une somme.

> [!INDICATION]
> Repère quand une fréquence s’annule, puis quand les deux s’annulent, avant de chercher des primitives.

#### Solution

Pour $\ell\in\mathbb Z\setminus\{0\}$, une primitive de $\cos(\ell\theta)$ est $\sin(\ell\theta)/\ell$. Ainsi son intégrale de $0$ à $\pi$ est nulle.

Pour $\ell=0$, l’intégrale vaut $\pi$. Or
$$2\cos(n\theta)\cos(m\theta)
=\cos((n-m)\theta)+\cos((n+m)\theta).$$
Si $n\ne m$, les deux fréquences sont non nulles. Si $n=m\ge1$, seule la fréquence $n-m$ est nulle. Si $n=m=0$, les deux le sont. On obtient
$$\boxed{\int_0^\pi\cos(n\theta)\cos(m\theta)\,\mathrm d\theta
=\begin{cases}
0 & \text{si }n\ne m,\\
\pi/2 & \text{si }n=m\ge1,\\
\pi & \text{si }n=m=0.
\end{cases}}$$

> [!JURY]
> Le rapport 2025 relève que beaucoup de copies n’ont pas distingué les trois cas. Traiter la fréquence nulle à part évite de diviser par zéro.

### Question 12

> [!INDICATION]
> Choisis un changement de variable adapté à Q8. Commence avec des bornes intérieures.

> [!INDICATION]
> Utilise Q11 pour distinguer orthogonalité et normalisation. Compare ensuite le cardinal de la famille obtenue à la dimension.

#### Solution

Le changement de variable $t=\cos\theta$ sur un segment intérieur à $]-1,1[$ inverse l’ordre des bornes. Pour $0<\theta<\pi$, on a $\sqrt{1-\cos^2\theta}=\sin\theta$, qui est strictement positif. Le facteur $\sin\theta$ provenant de la dérivée se simplifie. En passant aux limites aux bornes, ce qui est permis par Q9 et par la continuité de la fonction transformée sur $[0,\pi]$, on obtient, par Q8,
$$\langle P_n,P_m\rangle
=\int_0^\pi\cos(n\theta)\cos(m\theta)\,\mathrm d\theta.$$
D’après Q11, la famille $(P_j)_{0\le j\le k}$ est orthogonale. Les normes au carré sont $\pi$ pour $P_0$ et $\pi/2$ pour tout autre $P_j$.

Par Q7, ces polynômes sont dans $\mathbb R_k[X]$. La famille orthogonale est libre car tous ses termes sont non nuls. Elle possède $k+1$ éléments, ce qui est la dimension de l’espace. Une base orthonormale est donc
$$\boxed{\left(\frac{P_0}{\sqrt\pi},\ \left(\sqrt{\frac2\pi}\,P_j\right)_{1\le j\le k}\right).}$$
Pour $k=0$, la famille se réduit au premier terme.

## Problème — Matrices de rang 1

Un produit colonne-ligne permet de lire l’image à partir des colonnes et de calculer le carré de la matrice. Pour choisir une base de réduction, il faut ensuite regarder où se situe cette droite image par rapport au noyau.

### Partie I — Exemples

Dans les exemples aléatoires, la trace se lit sur la diagonale et le rang se lit sur les colonnes. Ces deux observations suffisent à reconnaître les événements utiles.

### Question 13

> [!INDICATION]
> Écris chaque colonne de $M$ comme un multiple de $U$. Identifie alors l’événement où toutes les colonnes sont nulles.

#### Solution

La $i$-ième colonne de $M$ est $X_iU$. Si $U=0$, toutes les colonnes sont nulles. Sinon, elles appartiennent à la droite engendrée par $U$ et au moins l’une est non nulle.

Le rang $Y$ vaut donc zéro si tous les $X_i$ valent zéro, et un sinon. Par indépendance,
$$\mathbb P(Y=0)=(1-p)^n.$$
Donc **$Y$ suit la loi de Bernoulli de paramètre $1-(1-p)^n$.**

### Question 14

> [!INDICATION]
> Compare $X_i$ à son carré sur les valeurs que prend une variable de Bernoulli.

#### Solution

On a $\operatorname{Tr}(M)=\sum_{i=1}^n X_i^2$. Comme $X_i$ prend presque sûrement ses valeurs dans $\{0,1\}$, on a $X_i^2=X_i$ presque sûrement.

La trace a donc la loi de la somme des $n$ variables de Bernoulli indépendantes de même paramètre $p$. **Elle suit la loi binomiale de paramètres $n$ et $p$.**

> [!JURY]
> Le rapport 2025 attend une justification de la loi de la trace qui utilise à la fois la loi de chaque terme diagonal et l’indépendance des variables.

### Question 15

> [!INDICATION]
> Regroupe le produit $U^\top U$ dans le calcul de $M^2$.

> [!INDICATION]
> Traduis l’idempotence en une équation entre un scalaire et une matrice. Que se passe-t-il si la matrice est nulle ?

#### Solution

Le produit $U^\top U$ est le scalaire $\sum_i X_i^2$, soit $\operatorname{Tr}(M)$. Par associativité, $M^2=U(U^\top U)U^\top$. En sortant le facteur scalaire, on obtient
$$\boxed{M^2=\operatorname{Tr}(M)M.}$$
Une matrice est une matrice de projection si et seulement si elle est idempotente. Ici, $M^2=M$ équivaut à $M=0$ ou $\operatorname{Tr}(M)=1$. Puisque $M=0$ équivaut à $U=0$ par Q13, il équivaut aussi à $\operatorname{Tr}(M)=0$.

Les deux événements de trace $0$ et $1$ sont disjoints. Par Q14,
$$\boxed{\mathbb P(M^2=M)=(1-p)^n+np(1-p)^{n-1}.}$$

> [!JURY]
> Le rapport 2025 signale l’oubli fréquent de la matrice nulle. Elle vérifie elle aussi l’équation de projection.

### Question 16

> [!INDICATION]
> Garde le critère de Q15 et décris les configurations d’entiers qui permettent de le satisfaire.

> [!INDICATION]
> Utilise l’indépendance pour calculer la probabilité d’une configuration, puis compte les configurations disjointes.

#### Solution

Le calcul matriciel de Q15 reste valable. Presque sûrement, les $X_i$ sont des entiers positifs ou nuls. Alors la somme de leurs carrés vaut zéro exactement quand ils sont tous nuls. Elle vaut un exactement quand une seule variable vaut un et que les autres sont nulles.

Pour chaque variable, les probabilités de zéro et de un valent respectivement $e^{-\lambda}$ et $\lambda e^{-\lambda}$.

Par indépendance, la première configuration a pour probabilité $e^{-n\lambda}$. Chacune des $n$ configurations de la seconde sorte, disjointes entre elles, a pour probabilité $\lambda e^{-n\lambda}$. Ainsi
$$\boxed{\mathbb P(M^2=M)=e^{-n\lambda}(1+n\lambda).}$$

### Question 17

> [!INDICATION]
> Décris l’action de $J$ sur un vecteur quelconque en utilisant la somme de ses coordonnées.

> [!INDICATION]
> Choisis une base dans le noyau et complète-la par un vecteur dont toutes les coordonnées sont égales.

#### Solution

Soit $s=(1,\ldots,1)^\top$. Toutes les colonnes de $J$ valent $s\ne0$ et les coefficients diagonaux valent $1$. Ainsi **$\operatorname{rg}(J)=1$ et $\operatorname{Tr}(J)=n$.**

Pour tout vecteur $v$, la matrice $J$ envoie $v$ sur la somme de ses coordonnées multipliée par $s$. On a donc $Js=ns$.

Les vecteurs $e_i-e_1$ pour $2\le i\le n$ appartiennent au noyau, l’hyperplan des vecteurs de somme nulle. Ils en forment une base, car ils sont au nombre de $n-1$ et libres par lecture des coordonnées $2$ à $n$.

Cet hyperplan est supplémentaire de la droite engendrée par $s$, puisque la somme des coordonnées de $s$ vaut $n\ne0$.

La matrice de passage est $P=(s\mid e_2-e_1\mid\cdots\mid e_n-e_1)$, écrite par colonnes. Elle vérifie
$$\boxed{P^{-1}JP=\operatorname{Diag}(n,0,\ldots,0).}$$

### Question 18

> [!INDICATION]
> Cherche une matrice à un seul coefficient non nul hors de la diagonale.

> [!INDICATION]
> Examine ce que son carré impliquerait pour ses coefficients diagonaux si elle était diagonalisable.

#### Solution

Posons
$$A_0=\begin{pmatrix}0&0&0\\1&0&0\\0&0&0\end{pmatrix}.$$
La seule colonne non nulle vaut $e_2$, donc $\operatorname{rg}(A_0)=1$. La diagonale est nulle, donc $\operatorname{Tr}(A_0)=0$.

On a $A_0^2=0$. Si $A_0$ était diagonalisable, la matrice diagonale semblable aurait un carré nul. Tous ses coefficients seraient donc nuls, ce qui contredirait $A_0\ne0$. **La matrice est de rang un, de trace nulle et non diagonalisable.**

### Partie II — Résultats généraux

Le noyau a toujours dimension $n-1$. Le choix du vecteur qui complète une base du noyau donne un accès direct au polynôme caractéristique, et la position de la droite image détermine la matrice réduite.

### Question 19

> [!INDICATION]
> Que dit le rang de $A$ sur l’espace engendré par ses colonnes ?

> [!INDICATION]
> Rassemble dans une ligne les coefficients qui expriment chaque colonne en fonction de $C$.

#### Solution

L’espace engendré par les colonnes de $A$ est de dimension un. Comme $C\ne0$, cet espace est la droite engendrée par $C$.

Pour chaque indice $j$, la colonne correspondante vaut donc $\ell_j C$ pour un certain scalaire $\ell_j$. Pour l’indice de $C$, ce scalaire vaut un.

La ligne $L=(\ell_1,\ldots,\ell_n)$ est donc non nulle et le produit $CL$ a exactement les colonnes de $A$. **Ainsi $A=CL$ avec $L\ne0$.**

### Question 20

> [!INDICATION]
> Compare la somme qui définit $LC$ aux coefficients diagonaux de $CL$.

> [!INDICATION]
> Utilise l’associativité pour regrouper le produit ligne-colonne dans $A^2$.

#### Solution

Si $C=(c_1,\ldots,c_n)^\top$, le calcul du produit ligne-colonne donne
$$LC=\sum_{i=1}^n \ell_i c_i.$$
Les coefficients diagonaux de $CL$ sont les $c_i\ell_i$. La commutativité des produits réels donne donc $LC=\operatorname{Tr}(A)$. Par associativité, $A^2=C(LC)L$. Comme $LC$ est scalaire,
$$\boxed{A^2=\operatorname{Tr}(A)A.}$$

### Question 21

> [!INDICATION]
> Complète une base du noyau par un vecteur placé en première position. Combien de colonnes de la matrice peuvent être non nulles dans cette base ?

> [!INDICATION]
> Pour le polynôme minimal, pars de Q20 et demande-toi ce qu’impliquerait un annulateur de degré $1$ pour le rang de $A$.

#### Solution

Notons $u$ l’endomorphisme associé à $A$ et $\tau=\operatorname{Tr}(A)$. Le théorème du rang donne $\dim\ker u=n-1$. Prenons une base du noyau et complétons-la par un vecteur placé en première position.

Dans cette base, toutes les colonnes sauf la première sont nulles. La matrice est triangulaire inférieure et son premier coefficient diagonal vaut $\tau$ par invariance de la trace sous similitude. Avec la convention $\chi_A(X)=\det(XI_n-A)$,
$$\boxed{\chi_A(X)=X^{n-1}(X-\tau).}$$
Par Q20, $X(X-\tau)$ est un polynôme annulateur unitaire de degré deux. Un annulateur de degré un imposerait que $A$ soit scalaire. Une matrice scalaire est de rang zéro ou $n$. Comme $n\ge2$, cela contredirait le rang un.

Le polynôme minimal est donc de degré deux. Comme il divise le polynôme annulateur unitaire de même degré, on a
$$\boxed{\mu_A(X)=X(X-\tau).}$$

> [!JURY]
> Le rapport 2025 relève des erreurs sur les multiplicités et des confusions entre les deux polynômes. Ici, la dimension du noyau et la relation $A^2=\operatorname{Tr}(A)A$ conduisent chacune à un calcul différent.

### Question 22

> [!INDICATION]
> Utilise le critère de diagonalisabilité en fonction du polynôme minimal trouvé en Q21.

#### Solution

Une matrice réelle est diagonalisable si et seulement si son polynôme minimal est scindé sur $\mathbb R$ à racines simples. Le polynôme calculé en Q21 est déjà factorisé en deux facteurs de degré $1$. Leurs racines sont distinctes exactement quand $\operatorname{Tr}(A)\ne0$.

**Ainsi $A$ est diagonalisable si et seulement si $\operatorname{Tr}(A)\ne0$.**

> [!PIEGE]
> Un polynôme caractéristique scindé sur $\mathbb R$ à racines simples suffit pour diagonaliser sur $\mathbb R$. La même condition sur le polynôme minimal est nécessaire et suffisante.

### Question 23

> [!INDICATION]
> Une intersection non nulle avec un noyau peut-elle occuper une partie seulement d’une droite ?

> [!INDICATION]
> Lis les colonnes de la matrice demandée. Quel vecteur doit être l’image du premier vecteur de base, et où doivent se trouver les autres ?

#### Solution

L’image de $u$ est une droite. Son intersection avec $\ker u$ étant non nulle, elle est tout entière contenue dans le noyau.

Choisissons $v$ tel que $u(v)\ne0$ et posons $w=u(v)$. Alors $w$ appartient au noyau. Complétons $(w)$ en une base $(w,w_3,\ldots,w_n)$ du noyau.

Comme $v\notin\ker u$, la famille $(v,w,w_3,\ldots,w_n)$ est une base de $\mathbb R^n$. Dans cette base, $u(v)=w$ et tous les autres vecteurs de base sont annulés. **La seule entrée non nulle de la matrice vaut 1 et se trouve à la ligne 2, colonne 1.**

### Question 24

> [!INDICATION]
> Utilise le théorème du rang et l’hypothèse d’intersection pour décomposer l’espace.

> [!INDICATION]
> Prends un vecteur non nul de l’image et regarde où se trouve son image par $u$. Que contredirait l’annulation de ce second vecteur ?

#### Solution

Puisque $\dim\operatorname{Im}u=1$ et $\dim\ker u=n-1$, la condition d’intersection nulle donne
$$\mathbb R^n=\operatorname{Im}u\oplus\ker u.$$
Prenons un vecteur non nul $v$ de l’image. Le vecteur $u(v)$ appartient encore à cette droite, donc $u(v)=av$ pour un réel $a$. Si $a$ était nul, $v$ appartiendrait aussi au noyau, ce qui est impossible.

En plaçant $v$ en tête d’une base complétée par une base de $\ker u$, on obtient **la matrice $\operatorname{Diag}(a,0,\ldots,0)$ avec $a\ne0$.**

> [!JURY]
> Le rapport 2025 indique que la non-nullité de $a$ a parfois été laissée sans preuve. Elle découle ici de l’intersection nulle.

### Question 25

> [!INDICATION]
> Identifie ce qui se conserve par similitude, puis lis cette quantité sur les deux formes de Q23 et Q24.

#### Solution

Deux matrices semblables ont même trace. Réciproquement, supposons que deux matrices de rang $1$ aient une trace commune $\tau$. Les formes de Q23 et Q24 couvrent tous les cas. La première a trace nulle et la seconde a trace $a\ne0$.

Si $\tau=0$, les deux matrices sont donc semblables à celle de Q23. Si $\tau\ne0$, elles sont toutes deux semblables à $\operatorname{Diag}(\tau,0,\ldots,0)$, puisque le premier coefficient diagonal de la matrice de Q24 est sa trace. Dans les deux cas, elles sont semblables entre elles. **Deux matrices de rang $1$ sont semblables si et seulement si elles ont la même trace.**

## Bilan

Pour transporter une inégalité scalaire vers des matrices symétriques définies positives, diagonalise et traduis les invariants matriciels en somme et produit de valeurs propres. Pour étudier l’égalité, suis-la à chaque étape du raisonnement.

Pour un produit scalaire donné par une intégrale généralisée, vérifie la convergence avant d’utiliser les propriétés de l’intégrale. Une fois le produit scalaire construit, vérifie séparément l’orthogonalité, la normalisation et le nombre de vecteurs de la famille.

Pour une matrice de rang $1$, pars de la droite image et d’un noyau de dimension $n-1$. Les colonnes donnent la factorisation, tandis qu’une base adaptée montre le rôle de l’intersection entre image et noyau.
