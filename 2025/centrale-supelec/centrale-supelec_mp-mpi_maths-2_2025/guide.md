# Centrale-Supélec MP/MPI — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve commune MP/MPI dure quatre heures et compte quarante-quatre questions. Elle étudie des modèles de ferromagnétisme dans un cadre probabiliste et utilise deux démarches autonomes.

La partie A mobilise la réduction des matrices. Elle commence par un encadrement de l'énergie issu du théorème spectral, puis examine plusieurs matrices d'interaction. Les décalages cycliques décrivent le modèle d'Ising à une dimension. Le produit de Kronecker permet d'en déduire un modèle bidimensionnel. La Q9 demande une fonction Python.

La partie B porte sur la limite de la magnétisation. Pour Ising, une matrice de taille deux permet de ramener la somme sur les configurations à une trace. Pour Curie-Weiss, une identité gaussienne ramène la pression à une intégrale qui se concentre près du minimum d'une fonction. La dernière sous-partie étudie la convergence en loi à partir d'une limite admise pour des moyennes lissées.

Q1–Q5, Q8–Q10, Q13–Q16, Q18 et Q25–Q30 sont des points d'entrée accessibles. Q31–Q39 demandent de suivre précisément l'hypothèse sur $h$ et la position du minimiseur. Q40–Q44 peuvent se traiter à part en s'appuyant sur la convergence admise. Une répartition possible réserve environ 1 h 30 à A, 45 minutes à B.I–II, 1 h à B.III, 30 minutes à B.IV et 15 minutes à la relecture.

## Partie A — Étude du spectre de la matrice d’interaction

Les matrices sont réelles symétriques. La structure particulière de chacune permet d'en calculer ou d'en encadrer le spectre.

### I — Quelques inégalités générales


### Question 1

> [!INDICATION]
> Identifiez les deux propriétés de la matrice qui permettent d'appliquer le théorème spectral.

#### Solution

La matrice $J_n$ est réelle symétrique. Par le théorème spectral, **elle est diagonalisable dans une base orthonormée de $\mathbb R^n$**.

### Question 2

> [!INDICATION]
> Reconnaissez une forme quadratique et exprimez-la dans une base orthonormée de vecteurs propres.

> [!INDICATION]
> Utilisez la quantité que le changement de base conserve et qui est facile à calculer pour une configuration.

#### Solution

Pour $x\in\Lambda_n$, soit $y$ son vecteur de coordonnées dans une base orthonormée de vecteurs propres de $J_n$, associée aux valeurs propres $\lambda_1,\ldots,\lambda_n$. Le changement de base préserve la norme, donc $\sum_i y_i^2=\|x\|^2=n$.

Ainsi,
$$
\begin{aligned}
\sum_{i,j}J_n(i,j)x_i x_j
&={}^{\mathsf T}\!x J_n x\\
&=\sum_{i=1}^n\lambda_i y_i^2 .
\end{aligned}
$$
Chaque $y_i^2$ est positif ou nul, donc **cette somme appartient à $[n\lambda_{\min},n\lambda_{\max}]$**.

> [!JURY]
> Le rapport rappelle que, lors d'un changement de base orthonormée, les coordonnées d'un vecteur à signes peuvent changer et cesser d'être toutes égales à $\pm1$. Sa norme reste constante.

### Question 3

> [!INDICATION]
> Encadrez séparément les deux termes de l'énergie. Tenez compte du signe du facteur devant la forme quadratique.

#### Solution

Puisque $-n\leq\sum_i x_i\leq n$ et $h\geq0$, le terme de champ est compris entre $-nh$ et $nh$. Le facteur $-\beta/2$ inverse l’ordre des bornes de Q2. En additionnant,
$$
\boxed{n\left(-h-\frac{\beta\lambda_{\max}}2\right)
\leq H_n(h,x)\leq n\left(h-\frac{\beta\lambda_{\min}}2\right).}
$$

### Question 4

> [!INDICATION]
> Appliquez la conservation de la norme à un vecteur propre. Que donnerait une matrice diagonalisable dont le spectre serait réduit à une seule valeur ?

#### Solution

Si $v\ne0$ est un vecteur propre réel de valeur propre $\lambda$, l’orthogonalité impose $\|\lambda v\|=\|v\|$, donc $|\lambda|=1$.

Les valeurs propres sont réelles par Q1.

Si une seule des valeurs $1$ et $-1$ apparaissait, la diagonalisation donnerait $J_n=I_n$ ou $J_n=-I_n$, cas exclus.

Q3 donne donc
$$
\boxed{-n(h+\beta/2)\leq H_n(h,x)\leq n(h+\beta/2).}
$$

### II — Le modèle de Curie-Weiss


### Question 5

> [!INDICATION]
> Calculez l'image d'un vecteur pour la matrice dont les coefficients valent tous un.

> [!INDICATION]
> Distinguez la droite du vecteur constant et son orthogonal, puis examinez l'effet d'une transformation affine de la matrice.

#### Solution

La matrice $U_n$ ne contient que des $1$.

Avec $e=(1,\ldots,1)^{\mathsf T}$, elle vérifie $U_n x=(\sum_i x_i)e$.

Elle vaut $n$ fois l’identité sur la droite engendrée par $e$ et s’annule sur son orthogonal.

Ces sous-espaces ont pour dimensions $1$ et $n-1$ et sont supplémentaires.

Ainsi **$U_n$ a pour valeurs propres $n$ et $0$, de multiplicités $1$ et $n-1$**.

Comme $J_n^{(C)}=(U_n-I_n)/n$, les mêmes sous-espaces donnent **$1-1/n$ et $-1/n$, de multiplicités respectives $1$ et $n-1$**.

> [!JURY]
> Le rapport distingue une inclusion du spectre et son calcul complet. Donner les deux sous-espaces propres et leurs dimensions justifie la liste et les multiplicités.

### III — Le modèle sinus


### Question 6

> [!INDICATION]
> Cherchez un télescopage après multiplication par $2\sin x$.

> [!INDICATION]
> Développez $\sin((2k+1)x)-\sin((2k-1)x)$ avec les formules d'addition.

#### Solution

La formule d’addition du sinus donne, pour tout $k$,
$$
2\sin(x)\cos(2kx)=\sin((2k+1)x)-\sin((2k-1)x).
$$
En sommant de $1$ à $p$, il ne reste que $\sin((2p+1)x)-\sin x$ à droite. Comme $x\notin\pi\mathbb Z$, la division par $2\sin x$ donne
$$
\boxed{\sum_{k=1}^{p}\cos(2kx)=
\frac12\left(\frac{\sin((2p+1)x)}{\sin x}-1\right).}
$$

### Question 7

> [!INDICATION]
> Pour chaque produit scalaire de colonnes, transformez le produit de deux sinus en une différence de cosinus.

> [!INDICATION]
> Distinguez les indices égaux et distincts avant d'appliquer Q6. Une fréquence nulle doit être traitée à part.

#### Solution

Posons $d=2n+1$ et $S(m)=\sum_{k=1}^n\cos(2\pi km/d)$ pour $m\in\mathbb Z$.

Q6 appliquée à $\pi m/d$ donne $S(m)=-1/2$ si $m$ n’est pas multiple de $d$.

On a $S(0)=n$.

La matrice est symétrique. Par la formule $2\sin a\sin b=\cos(a-b)-\cos(a+b)$, le produit scalaire des colonnes $i$ et $j$ vaut
$$
\frac{2}{d}\bigl(S(i-j)-S(i+j)\bigr).
$$
Si $i\ne j$, les deux arguments sont non multiples de $d$, donc le produit est nul.

Si $i=j$, le premier terme vaut $n$ et le second $-1/2$, car $2\leq2i\leq2n$.

Le produit vaut alors $1$.

Les colonnes forment donc une base orthonormée et **$J_n^{(S)}$ est orthogonale symétrique**.

> [!JURY]
> Le rapport demande deux vérifications distinctes. Deux colonnes différentes sont orthogonales et chaque colonne a pour norme un. La fréquence nulle intervient dans la seconde vérification.

### IV — Le modèle d’Ising unidimensionnel


### Question 8

> [!INDICATION]
> Repérez la colonne du coefficient non nul de chaque ligne dans chacun des deux décalages. Vérifiez aussi les deux extrémités de la numérotation.

#### Solution

Dans $C_{9,1}$, le coefficient $1$ de la ligne $i$ est dans la colonne du prédécesseur de $i$ modulo $9$.

Dans $C_{9,8}$, il est dans la colonne du successeur.

Les deux colonnes sont distinctes.

Le dessin porte exactement les arêtes entre entiers consécutifs de $1$ à $9$, avec l’arête $\{9,1\}$.

**$J_9^{(1)}$ est donc la matrice d’adjacence du cycle représenté.**

### Question 9

> [!INDICATION]
> Allouez une ligne indépendante pour chaque sommet. Pour un voisin de la liste associée à un sommet, déterminez la case à modifier et gardez le sens de l'arc.

#### Solution

La ligne $i$ est construite à partir de la liste des voisins sortants de $i$. Les lignes sont allouées séparément et un arc de $i$ vers $i$ donne un $1$ sur la diagonale.

```python
def mat_adj(graphe):
    m = len(graphe)
    matrice = [[0 for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in graphe[i]:
            matrice[i][j] = 1
    return matrice
```

> [!PIEGE]
> Une construction qui duplique la même liste pour toutes les lignes partage aussi ses modifications. Allouer les lignes indépendamment évite ce problème.

### Question 10

> [!INDICATION]
> Calculez l'action de chaque matrice sur la base canonique en comprenant les indices modulo la taille.

#### Solution

Notons $e_1,\ldots,e_n$ les vecteurs de la base canonique et étendons leurs indices modulo $n$.

La définition de $C_{n,k}$ donne $C_{n,k}e_j=e_{j+k}$.

En particulier, $C_{n,1}$ avance chaque indice d’une unité.

En itérant $k$ fois, on obtient $C_{n,1}^k e_j=e_{j+k}$ pour chaque $j$.

Donc **$C_{n,1}^k=C_{n,k}$**.

### Question 11

> [!INDICATION]
> Q10 fournit un polynôme annulateur. Pour justifier l'inclusion inverse, construisez un vecteur propre pour une racine choisie.

> [!INDICATION]
> Cherchez des coordonnées en progression géométrique. Le raccord entre le dernier et le premier indice utilise l'équation satisfaite par la racine.

#### Solution

Par Q10, $C_{n,1}^n=C_{n,n}=I_n$, donc $X^n-1$ est annulateur et le spectre complexe est inclus dans ses racines.

Pour toute racine $\zeta$ de $X^n-1$, le vecteur $v_\zeta=\sum_{j=0}^{n-1}\zeta^{-j}e_{j+1}$ est non nul.

Le décalage cyclique des composantes donne $C_{n,1}v_\zeta=\zeta v_\zeta$, le terme qui franchit l’indice $n$ étant compatible avec $\zeta^n=1$.

Ainsi **le spectre complexe est exactement l’ensemble des $n$-ièmes racines de l’unité**, toutes de multiplicité $1$.

Les valeurs propres réelles sont celles de ces racines qui sont réelles.

> [!JURY]
> Le rapport insiste sur le sens de l'implication fournie par un polynôme annulateur. Chaque valeur propre est une racine de ce polynôme. La construction des vecteurs propres établit l'autre inclusion.

### Question 12

> [!INDICATION]
> Les deux termes de la somme sont des puissances d'une même matrice. Cherchez leur action dans la base de Q11.

> [!INDICATION]
> Simplifiez la somme d'une racine de l'unité et de son inverse, puis comptez les vecteurs de la base qui fournissent chaque valeur.

#### Solution

Les vecteurs de Q11, associés à $n$ valeurs propres distinctes, forment une base de $\mathbb C^n$.

Q10 donne $J_n^{(1)}=C_{n,1}+C_{n,1}^{n-1}$.

Sur le vecteur propre associé à $\zeta_k=e^{2\mathrm i\pi k/n}$, cette somme agit par multiplication par $\zeta_k+\zeta_k^{-1}$.

La base fournit la liste complète pour $k$ de $0$ à $n-1$, avec répétitions éventuelles,
$$
\boxed{\lambda_k=2\cos(2\pi k/n).}
$$
Ces valeurs sont réelles, et $J_n^{(1)}$ est réelle symétrique.

> [!JURY]
> Le rapport met en garde contre l'addition des spectres sans hypothèse. Ici ce sont les mêmes vecteurs propres qui permettent d'additionner les valeurs correspondantes.

### V — Le modèle d’Ising bidimensionnel


### Question 13

> [!INDICATION]
> Fixez successivement l'une et l'autre matrice. Dans chaque cas, lisez la dépendance bloc par bloc.

#### Solution

À $B$ fixé, le bloc $(i,j)$ du produit est $a_{ij}B$, expression linéaire en $A$.

À $A$ fixé, la multiplication de $B$ par chaque scalaire $a_{ij}$ est linéaire.

Donc **le produit de Kronecker est bilinéaire**.

### Question 14

> [!INDICATION]
> Écrivez le bloc de ligne et colonne données dans le produit. Sortez les coefficients scalaires de la somme de blocs.

#### Solution

Le produit des blocs est admissible pour les tailles données. Son bloc $(i,j)$ vaut
$$
\begin{aligned}
\sum_{\ell=1}^{v} (a_{i\ell}B)(a'_{\ell j}B')
&=\left(\sum_{\ell=1}^{v} a_{i\ell}a'_{\ell j}\right)BB'\\
&=(AA')_{ij}BB'.
\end{aligned}
$$
On reconnaît le bloc $(i,j)$ de $(AA')\otimes(BB')$. **L’identité voulue est établie.**

> [!METHODE]
> Lors d'un produit par blocs, vérifiez les dimensions et calculez un bloc générique. Ce calcul fournit aussi les identités de changement de base des questions suivantes.

### Question 15

> [!INDICATION]
> Multipliez deux produits de Kronecker à l'aide de Q14 pour déterminer la matrice de passage inverse.

> [!INDICATION]
> Conjuguez le produit par le produit des deux matrices de passage et lisez les éléments diagonaux obtenus.

#### Solution

Par Q14, si $P$ et $Q$ sont inversibles, $P\otimes Q$ a pour inverse $P^{-1}\otimes Q^{-1}$, puisque $I_u\otimes I_r=I_{ur}$.

Soient $D=P^{-1}AP$ et $E=Q^{-1}BQ$ deux matrices diagonales. Q14 donne
$$
(P\otimes Q)^{-1}(A\otimes B)(P\otimes Q)=D\otimes E.
$$
Cette dernière matrice est diagonale et ses entrées sont tous les produits $D_{ii}E_{jj}$. Ainsi **$A\otimes B$ est diagonalisable et son spectre est $\{\lambda\mu:\lambda\in\operatorname{Sp}(A),\,\mu\in\operatorname{Sp}(B)\}$**.

### Question 16

> [!INDICATION]
> Numérotez les sommets par un couple d'indices entre 1 et 3. Distinguez les arêtes qui gardent le premier indice de celles qui gardent le second.

> [!INDICATION]
> Repérez les triangles correspondants sur la figure, y compris ceux dont une arête est en pointillés.

#### Solution

Dans l’indexation $i=3(a-1)+b$ où $1\leq a,b\leq3$, $J_3^{(1)}$ a des $1$ hors diagonale et des $0$ sur la diagonale.

Donc $I_3\otimes J_3^{(1)}$ relie les sommets de même premier indice $a$ et de seconds indices distincts.

De même, $J_3^{(1)}\otimes I_3$ relie ceux de même second indice $b$ et de premiers indices distincts.

Le dessin présente les triangles de la première famille sur les groupes $(1,2,3)$, $(4,5,6)$ et $(7,8,9)$.

Les triangles de la seconde sont sur les groupes $(1,4,7)$, $(2,5,8)$ et $(3,6,9)$. On compte aussi les arêtes en pointillés. Les deux familles n’ont aucune arête en commun. **La somme des deux matrices donne exactement les coefficients $0$ ou $1$ du graphe.**

### Question 17

> [!INDICATION]
> Réutilisez une diagonalisation de la matrice d'Ising unidimensionnelle.

> [!INDICATION]
> Appliquez le même changement de base par produit de Kronecker aux deux termes de la somme. Examinez ensuite leurs entrées diagonales.

#### Solution

La matrice $J=J_n^{(1)}$ est réelle symétrique, donc $P^{-1}JP=D$ est diagonale pour une matrice réelle inversible $P$.

Le changement de base $P\otimes P$ conjugue, par Q14, les deux termes de $J_N^{(2)}$ en $I_n\otimes D$ et $D\otimes I_n$.

Leur somme est diagonale.

Ses $n^2$ entrées sont **$\lambda_j+\lambda_k$ pour $0\leq j,k<n$**, énumérées avec multiplicité. L’indexation de $1$ à $n$ du sujet donne la même liste en prolongeant $\lambda_j$ par périodicité.

> [!JURY]
> Le rapport relève que la matrice de passage commune est le point déterminant. En exhibant cette matrice, on additionne directement les deux matrices diagonales.

## Partie B — Étude de la convergence de la magnétisation

La dérivée de la pression à taille finie est une espérance. On étudie ensuite sa limite par deux représentations très différentes de la fonction de partition.

### I — Magnétisation spontanée


### Question 18

> [!INDICATION]
> Vérifiez la positivité de la fonction de partition, puis dérivez son logarithme.

> [!INDICATION]
> Identifiez après dérivation le poids probabiliste de chaque configuration, et utilisez la formule de transfert.

#### Solution

Pour chaque configuration $x$, posons $s_n(x)=\sum_i x_i$.

Le poids $e^{-H_n(h,x)}$ est une exponentielle du paramètre $h$, multipliée par une constante positive.

Donc $Z_n$ est une somme finie de fonctions dérivables et strictement positives, et $\psi_n=(\ln Z_n)/n$ est dérivable, y compris par prolongement à $h=0$.

La dérivation puis la formule de transfert donnent
$$
\begin{aligned}
\psi'_n(h)&=\frac{1}{nZ_n(h)}\sum_{x\in\Lambda_n}s_n(x)e^{-H_n(h,x)}\\
&=\boxed{\mathbb E(M_{n,h})=m_n(h)}.
\end{aligned}
$$

> [!JURY]
> Les rapports demandent de justifier la stricte positivité de la fonction de partition avant le logarithme. Ils signalent aussi la nécessité de distinguer les variables aléatoires des valeurs d'une configuration dans la formule de transfert.

### II — Le modèle d’Ising


### Question 19

> [!INDICATION]
> Écrivez séparément les contributions du prédécesseur et du successeur dans la forme quadratique. Comparez leurs sommes à l'aide de la convention cyclique.

#### Solution

Les deux décalages apportent respectivement $\sum_i x_i x_{i-1}$ et $\sum_i x_i x_{i+1}$ à la forme quadratique. Ces deux sommes coïncident par décalage cyclique. Cela reste vrai pour $n=2$, où la matrice additionne deux fois le même décalage. On a donc
$$
-H_n(h,x)=\sum_{i=1}^n(\beta x_i x_{i+1}+hx_i).
$$
L’exponentielle d’une somme étant le produit des exponentielles, **$Z_n(h)=\sum_{x\in\Lambda_n}\prod_{i=1}^n e^{\beta x_i x_{i+1}+hx_i}$**.

> [!PIEGE]
> À deux particules, les deux termes de la matrice d'interaction contribuent chacun au même décalage. La somme cyclique compte correctement cette multiplicité.

### Question 20

> [!INDICATION]
> Raisonnez par récurrence sur la puissance. Dans la multiplication par un facteur supplémentaire, interprétez l'indice sommé comme un nouvel indice intermédiaire.

#### Solution

Pour $p=2$, la formule est celle du produit de deux matrices, le produit central étant vide.

Supposons l’identité vraie à l’ordre $p\geq2$.

Dans $(M^{p+1})(i,j)=\sum_{r=1}^q(M^p)(i,r)M(r,j)$, substituons la formule d’ordre $p$ et renommons $r$ en $k_{p+1}$.

Les indices de sommation sont alors $k_2,\ldots,k_{p+1}$.

Le dernier lien est $M(k_{p+1},j)$.

**La récurrence donne exactement le produit demandé**.

### Question 21

> [!INDICATION]
> Associez les deux lignes et colonnes aux deux valeurs possibles d'une particule. Écrivez l'entrée de la matrice en fonction des deux états.

> [!INDICATION]
> Dans Q20, imposez que l'état final soit égal à l'état initial et sommez sur cet état.

#### Solution

Dans l’ordre des états $-1,+1$, l’entrée de $A$ de ligne $a$ et colonne $b$ est $e^{\beta ab+ha}$.

Par Q20, la trace de $A^n$ est la somme sur les chemins fermés de longueur $n$, autrement dit
$$
\operatorname{tr}(A^n)=\sum_{x_1,\ldots,x_n\in\{-1,1\}}
   A_{x_1,x_2}\cdots A_{x_n,x_1},
$$
où les indices désignent les états correspondants. Par Q19, **$\operatorname{tr}(A^n)=Z_n(h)$**.

> [!METHODE]
> Une trace ferme le dernier indice sur le premier. Les coefficients de la matrice portent chacun l'interaction avec le prochain état et le champ du seul état courant.

### Question 22

> [!INDICATION]
> Utilisez trace et déterminant pour écrire le polynôme caractéristique.

> [!INDICATION]
> Pour contrôler le discriminant, remplacez le carré du cosinus hyperbolique par une expression contenant le carré du sinus hyperbolique.

#### Solution

La trace est $2e^\beta\cosh h$ et le déterminant est $e^{2\beta}-e^{-2\beta}=2\sinh(2\beta)$. Posons
$$
\Delta(h)=\sqrt{e^{2\beta}\sinh^2 h+e^{-2\beta}}.
$$
Le discriminant du polynôme caractéristique vaut $4\Delta(h)^2>0$. Ses deux racines sont
$$
\boxed{\lambda_\pm(h)=e^\beta\cosh h\pm\Delta(h).}
$$
Elles sont toutes deux positives puisque leur somme et leur produit sont strictement positifs, et $\lambda_+>\lambda_-$.

> [!JURY]
> Le rapport attend que le signe du discriminant soit vérifié avant l'écriture des valeurs propres. Le terme strictement positif subsiste même lorsque le champ est nul.

### Question 23

> [!INDICATION]
> Exprimez la trace de la puissance dans une base propre.

> [!INDICATION]
> Factorisez par la puissance de la valeur propre la plus grande et encadrez le terme restant après le logarithme.

#### Solution

Les deux valeurs propres étant distinctes, $A$ se diagonalise. Par Q21 et invariance de la trace par similitude,
$$
\begin{aligned}
\psi_n(h)&=\frac1n\ln\bigl(\lambda_+^n+\lambda_-^n\bigr)\\
&=\ln\lambda_++\frac1n\ln\left(1+(\lambda_-/\lambda_+)^n\right).
\end{aligned}
$$
Le second terme est compris entre $0$ et $(\ln 2)/n$. Comme $\Delta(h)^2=e^{2\beta}\cosh^2 h-2\sinh(2\beta)$, la limite est **le logarithme de $e^\beta\cosh h+\sqrt{e^{2\beta}\cosh^2h-2\sinh(2\beta)}$**.

### Question 24

> [!INDICATION]
> Dérivez le logarithme de la plus grande valeur propre. Pour simplifier, exprimez la dérivée de la racine à partir de la dérivée de son carré.

> [!INDICATION]
> Appliquez la relation admise entre pression et magnétisation pour les champs strictement positifs, puis passez à la limite en zéro.

#### Solution

Notons $a(h)=e^\beta\cosh h$. La relation $\Delta^2=a^2-2\sinh(2\beta)$ donne $\Delta'=aa'/\Delta$. Donc
$$
\begin{aligned}
\psi'(h)&=\frac{a'+aa'/\Delta}{a+\Delta}\\
&=\frac{a'}{\Delta}.
\end{aligned}
$$
La relation admise entre $m$ et $\psi'$ s’applique puisque le radicand reste strictement positif. Pour $h>0$,
$$
\boxed{m(h)=\frac{e^\beta\sinh h}{\sqrt{e^{2\beta}\sinh^2 h+e^{-2\beta}}}.}
$$
Cette expression tend vers $0$ lorsque $h\to0^+$.

De plus, à $h=0$, la symétrie $x\mapsto-x$ force $m_n(0)=0$ pour tout $n$.

**On a $m^+=0$ et $m(0)=0$.**

### III — Le modèle de Curie-Weiss


### Question 25

> [!INDICATION]
> Développez le carré de la somme des coordonnées. Isolez la diagonale qui est absente de la matrice d'interaction.

#### Solution

La matrice $J_n^{(C)}$ a pour coefficients $1/n$ hors diagonale et $0$ sur la diagonale. Puisque $x_i^2=1$, sa forme quadratique vaut $(s_n(x)^2-n)/n$. Par définition de l’énergie,
$$
\boxed{Z_n(h)=e^{-\beta/2}\sum_{x\in\Lambda_n}
 \exp\left(\frac{\beta}{2n}s_n(x)^2+hs_n(x)\right).}
$$

### Question 26

> [!INDICATION]
> La fonction est continue sur les segments. Sur les deux queues, comparez le carré de la variable à sa valeur absolue.

#### Solution

La fonction positive $x\mapsto e^{-x^2/2}$ est continue sur $\mathbb R$. Pour $|x|\geq1$, elle est majorée par $e^{-|x|/2}$, intégrable sur les deux queues. **L’intégrale converge.** Sa valeur admise est $\sqrt{2\pi}$.

> [!JURY]
> Le rapport souligne le rôle de la continuité à distance finie et des comparaisons au voisinage des deux infinis. Une fonction de référence peut ne servir que sur ces queues.

### Question 27

> [!INDICATION]
> Complétez le carré dans l'exposant.

> [!INDICATION]
> Translatez puis dilatez la variable pour vous ramener à l'intégrale gaussienne admise.

#### Solution

Pour $a>0$ et $u\in\mathbb R$, la complétion du carré donne
$$
ut-\frac{t^2}{2a}=\frac{au^2}{2}-\frac{(t-au)^2}{2a}.
$$
Le changement de variable $z=(t-au)/\sqrt a$ transforme la seconde exponentielle en la gaussienne de Q26, avec un facteur $\sqrt a$ dans la différentielle. L’intégrale existe et
$$
\boxed{\int_{\mathbb R} e^{ut-t^2/(2a)}\frac{\mathrm dt}{\sqrt{2\pi a}}
=e^{au^2/2}.}
$$

### Question 28

> [!INDICATION]
> Choisissez les deux paramètres de Q27 de façon à retrouver le carré de la somme des coordonnées.

> [!INDICATION]
> La somme sur les configurations est finie. Surveillez le facteur devant l'intégrale après avoir regroupé les constantes.

#### Solution

On utilise Q27 avec $a=\beta/n$ et $u=s_n(x)$ dans chacun des termes de Q25. Chaque intégrale converge. Comme la somme sur $\Lambda_n$ est finie, la linéarité donne
$$
\boxed{Z_n(h)=\sqrt{\frac{n}{2e^\beta\pi\beta}}
\int_{\mathbb R}\left(\sum_{x\in\Lambda_n}e^{(t+h)s_n(x)}\right)
e^{-nt^2/(2\beta)}\,\mathrm dt.}
$$

> [!JURY]
> Le rapport précise que l'interversion relève de la linéarité pour une somme finie. Aucun théorème d'interversion avec une série infinie n'est nécessaire.

### Question 29

> [!INDICATION]
> Écrivez la somme comme des sommes emboîtées sur les coordonnées. Chacune ne porte que sur deux valeurs.

#### Solution

La somme sur $\Lambda_n=\{-1,1\}^n$ porte indépendamment sur chacune des coordonnées. Par distributivité,
$$
\begin{aligned}
\sum_{x\in\Lambda_n}\prod_{i=1}^{n}e^{(t+h)x_i}
&=\prod_{i=1}^{n}\bigl(e^{-(t+h)}+e^{t+h}\bigr)\\
&=\boxed{(2\cosh(t+h))^n}.
\end{aligned}
$$

### Question 30

> [!INDICATION]
> Remplacez la somme de Q28 par l'expression de Q29, puis translatez la variable pour supprimer le décalage dans le cosinus hyperbolique.

#### Solution

Dans Q28, on remplace la somme par le résultat de Q29, puis on pose $x=t+h$. Le produit des termes exponentiels devient $\exp\bigl(-n[(x-h)^2/(2\beta)-\ln(2\cosh x)]\bigr)$. Ainsi
$$
\boxed{Z_n(h)=\sqrt{\frac{n}{2e^\beta\pi\beta}}\int_{\mathbb R}e^{-nG_h(x)}\,\mathrm dx.}
$$

### Question 31

> [!INDICATION]
> Exprimez le signe de $G_h'$ en comparant $x-\beta\tanh x$ à $h$.

> [!INDICATION]
> Étudiez les variations de cette fonction sur le demi-axe positif. Si elle commence par décroître, repérez le niveau à partir duquel sa branche croissante rencontre les valeurs positives.

#### Solution

Posons $F(x)=x-\beta\tanh x$. Alors, sur $\mathbb R$,
$$
\begin{aligned}
\beta G'_h(x)&=F(x)-h,\\
F'(x)&=1-\frac{\beta}{\cosh^2 x}.
\end{aligned}
$$
On a $F(0)=0$ et $F(x)\to+\infty$ lorsque $x\to+\infty$, car $\tanh$ est bornée.

**Cas $\beta\leq1$.** Pour $x>0$, $F'(x)>0$.

Ainsi $F$ est strictement croissante sur $\mathbb R_+$ et atteint une seule fois la valeur $h$, en un point $u_h$.

Pour $h=0$, ce point vaut $0$.

Pour $h>0$, il est positif et $G'_h$ est négative avant ce point puis positive après.

Pour $h=0$, $G'_0$ est positive sur $]0,+\infty[$.

Dans les deux cas $u_h$ est l’unique minimiseur.

**Cas $\beta>1$.** Le cosinus hyperbolique croît strictement de $1$ vers $+\infty$ sur $\mathbb R_+$.

Il existe donc un unique $a>0$ tel que $\cosh^2 a=\beta$.

La fonction $F$ décroît de $0$ sur $[0,a]$ et croît strictement sur $[a,+\infty[$.

Comme $F(a)<0$, cette seconde branche atteint la valeur $h\geq0$ en un unique point $u_h>a$.

Pour $0<x<u_h$, $F(x)<h$, et pour $x>u_h$, $F(x)>h$.

Le signe de $G'_h$ donne **un unique minimum en $u_h>0$**.

Cela vaut aussi lorsque $h=0$, bien que $G'_0(0)$ s'annule.

Dans tous les cas, $F(u_h)=h$.

Puisque $\beta G'_0=F$, on a **$G'_h(u_h)=0$ et $h=\beta G'_0(u_h)$**.

Pour $h>0$, $u_h$ appartient à une branche où $F'(u_h)>0$.

Ainsi **$G''_h(u_h)=F'(u_h)/\beta>0$**.

> [!PIEGE]
> À champ nul et au-dessus du seuil en inverse de température, le point zéro est aussi critique, mais le signe de la dérivée sur le demi-axe départage les deux points.

### Question 32

> [!INDICATION]
> Comparez les valeurs de la fonction en deux points opposés. Repérez la partie paire et le terme qui distingue leurs signes.

#### Solution

Pour $x>0$, le terme $\ln(2\cosh x)$ est pair et
$$
G_h(-x)-G_h(x)=\frac{2hx}{\beta}>0.
$$
Tout point négatif a donc une valeur strictement supérieure à celle de son opposé. Par Q31, **$u_h$ est l’unique minimiseur sur $\mathbb R$**.

### Question 33

> [!INDICATION]
> Recentrez l'intégrale autour du minimum, puis adoptez l'échelle indiquée par l'argument de la fonction centrée.

> [!INDICATION]
> Extrayez l'exponentielle du minimum et vérifiez la compensation entre la différentielle et le facteur devant l'intégrale.

#### Solution

Dans Q30, posons $x=u_h+t/\sqrt n$. Le minimum de $G_h$ vaut $G_h(u_h)$ par Q32. En extrayant l’exponentielle du minimum et en simplifiant le facteur $1/\sqrt n$ du changement de variable,
$$
Z_n(h)=
\frac{e^{-nG_h(u_h)}}{\sqrt{2e^\beta\pi\beta}}
\int_{\mathbb R}e^{-n\widehat G_h(t/\sqrt n)}\,\mathrm dt.
$$
En prenant le logarithme et en divisant par $n$,
$$
\boxed{\begin{aligned}
\psi_n(h)&=-G_h(u_h)-\frac{\ln(2e^\beta\pi\beta)}{2n}\\
&\quad+\frac1n\ln\left(\int_{\mathbb R}e^{-n\widehat G_h(t/\sqrt n)}\,\mathrm dt\right).
\end{aligned}}
$$

> [!METHODE]
> Recentrer puis changer d'échelle isole le terme dominant et produit une intégrale de taille finie. Vérifier les constantes avant de prendre le logarithme réduit le risque d'un facteur oublié.

### Question 34

> [!INDICATION]
> Développez la fonction au minimum par Taylor-Young. Utilisez l'annulation de sa dérivée première avant de diviser.

#### Solution

Comme $G_h$ est de classe $\mathcal C^2$ et $G'_h(u_h)=0$, la formule de Taylor-Young donne
$$
\widehat G_h(x)=\frac{\gamma_h}{2}x^2+o(x^2)
\quad(x\to0).
$$
Le quotient tend donc vers $\gamma_h/2$. Il est continu pour $x\ne0$. **Le prolongement en posant $f_h(0)=\gamma_h/2$ est continu sur $\mathbb R$.**

### Question 35

> [!INDICATION]
> Sur un segment, exploitez la stricte positivité et la continuité du quotient prolongé.

> [!INDICATION]
> À l'infini, comparez le terme quadratique à la croissance du logarithme du cosinus hyperbolique.

#### Solution

Par unicité du minimum, $\widehat G_h(x)>0$ pour tout $x\ne0$, d’où $f_h(x)>0$. De plus, $f_h(0)>0$ par Q31.

Pour tout réel $z$, $0\leq\ln(2\cosh z)\leq |z|+\ln2$. Dans le quotient $\widehat G_h(x)/x^2$, ce terme et la constante extraite sont négligeables à l’infini. Le terme quadratique donne donc
$$
\lim_{|x|\to\infty} f_h(x)=\frac1{2\beta}>0.
$$
Hors d’un segment $[-R,R]$, on peut minorer $f_h$ par $1/(4\beta)$. Sur ce segment, sa continuité lui assure un minimum strictement positif. **La plus petite de ces deux bornes est une constante $c_h>0$ convenable.**

> [!PIEGE]
> Une fonction strictement positive sur la droite peut avoir une borne inférieure nulle. La limite strictement positive fournit ici une minoration uniforme hors d'un segment.

### Question 36

> [!INDICATION]
> Réécrivez l'exposant en faisant intervenir le quotient prolongé. Pour la limite ponctuelle, utilisez sa valeur en zéro.

> [!INDICATION]
> Cherchez une gaussienne intégrable qui domine les intégrandes pour tout indice à l'aide de Q35.

#### Solution

Pour $t$ fixé, $n\widehat G_h(t/\sqrt n)=t^2 f_h(t/\sqrt n)$, y compris pour $t=0$. Par Q34, cette quantité tend vers $\gamma_h t^2/2$. Par Q35, les intégrandes continues sont dominées par $e^{-c_h t^2}$, intégrable par Q26 et changement d’échelle. Le théorème de convergence dominée donne
$$
\boxed{\int_{\mathbb R} e^{-n\widehat G_h(t/\sqrt n)}\,\mathrm dt
\longrightarrow \int_{\mathbb R}e^{-\gamma_h t^2/2}\,\mathrm dt
=\sqrt{\frac{2\pi}{\gamma_h}}.}
$$
La limite est finie et strictement positive. Dans Q33, le logarithme divisé par $n$ tend donc vers zéro, de même que le terme constant en $1/n$. **$\psi(h)=-G_h(u_h)$ pour $h>0$.**

> [!METHODE]
> La convergence ponctuelle vient du développement local au minimum. La domination uniforme en indice vient de la minoration globale établie séparément.

### Question 37

> [!INDICATION]
> Reprenez le tableau de variations de Q31 et restreignez la dérivée au domaine indiqué.

> [!INDICATION]
> Exprimez le minimiseur au moyen de la réciproque et vérifiez l'hypothèse de dérivation sur les champs strictement positifs.

#### Solution

D’après Q31, $G'_0=F/\beta$ est continue et strictement croissante sur $[u_0,+\infty[$.

Elle vaut $0$ en $u_0$ et tend vers $+\infty$.

Le théorème de la bijection donne une bijection continue de $[u_0,+\infty[$ sur $\mathbb R_+$ à réciproque continue.

Par Q31,
$$
u(h)=(G'_0)^{-1}(h/\beta).
$$
Ainsi **$u$ est continue sur $\mathbb R_+$**.

Pour $h>0$, la dérivée de $G'_0$ en $u(h)$ est $G''_h(u_h)>0$.

Le théorème de dérivation de la réciproque donne **la dérivabilité de $u$ sur $\mathbb R_+^\ast$**.

### Question 38

> [!INDICATION]
> Dérivez la formule de Q36 composée avec le minimiseur.

> [!INDICATION]
> Dans le coefficient de la dérivée du minimiseur, cherchez la condition d'optimalité obtenue en Q31.

#### Solution

Pour $h>0$, Q36 donne $\psi(h)=\ln(2\cosh u(h))-(u(h)-h)^2/(2\beta)$. Les fonctions intervenant dans cette expression sont dérivables par Q37. Ainsi
$$
\psi'(h)=u'(h)\left(\tanh u(h)-\frac{u(h)-h}{\beta}\right)
+\frac{u(h)-h}{\beta}.
$$
Le coefficient de $u'(h)$ est nul par $G'_h(u(h))=0$. Par la relation admise entre $m$ et $\psi'$,
$$
\boxed{m(h)=\frac{u(h)-h}{\beta}\quad(h>0).}
$$

> [!METHODE]
> Dans une fonction évaluée à un minimiseur dérivable, la dérivation par la position du minimiseur fait apparaître la dérivée qui s'annule au minimum.

### Question 39

> [!INDICATION]
> Passez à la limite dans Q38 grâce à Q37, puis comparez les valeurs possibles du minimiseur à champ nul.

#### Solution

Par la continuité de $u$ en $0$, la formule de Q38 donne $m^+=u_0/\beta$.

Par Q31, **$m^+=0$ si $\beta\leq1$, et $m^+>0$ si $\beta>1$**.

### IV — Convergence en loi pour la loi de Curie-Weiss au point critique


### Question 40

> [!INDICATION]
> Utilisez le fait que la variable aléatoire prend un nombre fini de valeurs. Majorez l'espérance par une borne sur la fonction test avant de traiter l'intégrale.

#### Solution

L’intégrale $Z_\infty$ est strictement positive et finie. En effet, son intégrande est continue et positive, et, pour $|x|\geq1$, elle est majorée par $e^{-|x|/12}$. La fonction $\varphi_\infty$ est donc une densité continue, bornée par $1/Z_\infty$.

Pour $n$ fixé, la variable $M_n$ a un nombre fini de valeurs. L’espérance figurant sous l’intégrale de $E_{n,f}$ est donc une somme finie de fonctions continues de $t$. Sa valeur absolue est majorée par $\|f\|_\infty$. Une fois multiplié par la densité gaussienne, cet intégrande est absolument intégrable par Q26. **$E_{n,f}$ est donc bien défini.**

### Question 41

> [!INDICATION]
> Placez l'espérance non perturbée sous l'intégrale en utilisant la normalisation gaussienne.

> [!INDICATION]
> Appliquez l'inégalité lipschitzienne au décalage et calculez le premier moment absolu de la gaussienne ainsi obtenu.

#### Solution

Écrivons $Y_n=n^{1/4}M_n$. Comme la gaussienne normalisée a pour intégrale $1$, on peut placer la constante $\mathbb E(f(Y_n))$ sous l’intégrale. La propriété lipschitzienne donne
$$
\begin{aligned}
|E_{n,f}-\mathbb E(f(Y_n))|
&\leq \int_{\mathbb R}\frac{K|t|}{n^{1/4}}
\frac{e^{-t^2/2}}{\sqrt{2\pi}}\,\mathrm dt\\
&=\boxed{\frac{2K}{n^{1/4}\sqrt{2\pi}}}.
\end{aligned}
$$
En effet, l’intégrale de $t e^{-t^2/2}$ sur $\mathbb R_+$ vaut $1$. Cette majoration tend vers zéro. En utilisant la limite admise de $E_{n,f}$, on trouve **$\mathbb E(f(Y_n))\to\int_{\mathbb R}f(u)\varphi_\infty(u)\,\mathrm du$**.

### Question 42

> [!INDICATION]
> Repérez les pentes des trois morceaux. Pour deux points séparés par un raccord, découpez l'intervalle au raccord avant de majorer la variation.

#### Solution

La fonction $f_k$ est continue aux raccords en $x$ et $x+1/k$.

Sur les trois intervalles délimités par ces points, elle est affine de pente de module au plus $k$.

Pour $u<v$, subdivisons $[u,v]$ en ajoutant les éventuels points de raccord.

L’inégalité triangulaire appliquée aux variations successives donne $|f_k(v)-f_k(u)|\leq k(v-u)$.

Ainsi **$f_k$ est $k$-lipschitzienne**.

### Question 43

> [!INDICATION]
> Comparez la rampe proposée à deux fonctions indicatrices. Appliquez Q41 à cette rampe.

> [!INDICATION]
> Séparez l'erreur de convergence de l'erreur due au déplacement du seuil.

#### Solution

On a point par point
$$
\mathbf 1_{]-\infty,x]}\leq f_k\leq\mathbf 1_{]-\infty,x+1/k]}.
$$
La fonction $f_k$ est bornée et lipschitzienne. Par Q41, il existe donc $n_0$ tel que, pour $n\geq n_0$,
$$
\begin{aligned}
\mathbb P(Y_n\leq x)
&\leq\mathbb E(f_k(Y_n))\\
&\leq\frac{\varepsilon}{2}+\int_{\mathbb R} f_k(u)\varphi_\infty(u)\,\mathrm du\\
&\leq\boxed{\frac{\varepsilon}{2}+\int_{-\infty}^{x+1/k}\varphi_\infty(u)\,\mathrm du}.
\end{aligned}
$$

### Question 44

> [!INDICATION]
> Contrôlez l'intégrale de la densité sur un intervalle de longueur égale à la largeur de la rampe.

> [!INDICATION]
> Pour obtenir une minoration symétrique, translatez la rampe de manière qu'elle atteigne zéro au seuil demandé.

#### Solution

Posons $L(x)=\int_{-\infty}^x\varphi_\infty(u)\,\mathrm du$. La borne $\varphi_\infty\leq 1/Z_\infty$ et le choix de $k$ donnent
$$
L(x+1/k)-L(x)\leq\frac{1}{kZ_\infty}\leq\frac{\varepsilon}{2}.
$$
Par Q43, $\mathbb P(Y_n\leq x)\leq L(x)+\varepsilon$ pour $n$ assez grand.

Pour l’autre sens, posons $g_k(u)=f_k(u+1/k)$. Cette fonction bornée et $k$-lipschitzienne vérifie
$$
\mathbf 1_{]-\infty,x-1/k]}\leq g_k\leq\mathbf 1_{]-\infty,x]}.
$$
Q41 appliquée à $g_k$ donne, pour $n$ assez grand,
$$
\begin{aligned}
\mathbb P(Y_n\leq x)
&\geq \mathbb E(g_k(Y_n))\\
&\geq L(x-1/k)-\frac{\varepsilon}{2}\\
&\geq L(x)-\varepsilon.
\end{aligned}
$$
Puisque $\varepsilon>0$ est arbitraire, **$\mathbb P(n^{1/4}M_n\leq x)\to\int_{-\infty}^x\varphi_\infty(u)\,\mathrm du$ pour tout $x\in\mathbb R$**.

> [!PIEGE]
> L'encadrement d'une fonction de répartition demande deux inégalités. Une rampe placée du seul côté droit donne uniquement la majoration en Q43.

## Bilan

- Le théorème spectral donne des encadrements de formes quadratiques par conservation de la norme. Pour une somme de matrices, recherchez une base propre commune avant d'additionner des valeurs.
- La trace d'une puissance combine des produits matriciels sur des parcours dont le dernier état revient au premier. Cette écriture aide à exploiter une condition cyclique.
- Pour une intégrale gouvernée par son minimum, vérifiez successivement l'unicité, le développement local et une domination valable sur tout le domaine après changement d'échelle.
- Pour passer d'une convergence d'espérances de fonctions lipschitziennes à la convergence des fonctions de répartition, encadrez l'indicatrice par deux rampes et contrôlez l'intégrale sur leurs intervalles de transition.
