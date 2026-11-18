# Centrale-Supélec PSI — Mathématiques 1 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*


## Présentation du sujet

Le problème étudie le conditionnement pour la norme euclidienne. Soit $A$ inversible. Si le second membre $Y$ du système $AX=Y$ change de $\delta Y$, la solution change de $\delta X=A^{-1}\delta Y$. En encadrant les deux produits matrice-vecteur, on obtient pour $Y\ne 0$ :
$$\frac{\|\delta X\|}{\|X\|}\le
\operatorname{cond}(A)\,\frac{\|\delta Y\|}{\|Y\|}.$$
Le conditionnement mesure ainsi l’amplification que peut subir une erreur relative sur le second membre.

La partie A construit la norme matricielle à partir de la norme des vecteurs. La partie B définit le conditionnement et montre qu’il peut croître très vite sur un exemple triangulaire. La partie C passe au spectre de la matrice symétrique $A^\top A$, puis D calcule celui d’une matrice tridiagonale. La partie E prouve deux fois la majoration de Kantorovich, par un discriminant puis par une espérance.

Le sujet compte 43 questions pour quatre heures. Les applications directes du cours (Q1–Q3, Q6–Q12, Q16–Q19 et Q29) permettent de prendre des points rapidement en soignant les justifications. Si Q13 ou Q30 bloque, les résultats demandés peuvent être repris dans les questions suivantes. Garder du temps pour E : la minoration de Q34 et les questions probabilistes restent accessibles même après un blocage en D.

## Partie A — Construction d’une norme sur $M_n(\mathbb R)$

La norme $N$ est le plus grand facteur d’amplification sur les vecteurs unitaires. On justifie d’abord son existence, puis on étudie les cas où les symétries de la norme euclidienne facilitent le calcul.

### I — Étude de l’application $N$

### Question 1

> [!INDICATION]
> Écris une coordonnée de $AX$ à l’aide d’une ligne de $A$.

> [!INDICATION]
> Applique Cauchy-Schwarz avant de sommer les carrés.

#### Solution

Pour tout $i$, la $i$-ième coordonnée de $AX$ vaut $\langle L_i,X\rangle$, en identifiant la ligne à un vecteur de $\mathbb R^n$.

Par Cauchy-Schwarz, $|\langle L_i,X\rangle|\le M$ puisque $\|X\|=1$.

En sommant les carrés, on obtient $\|AX\|^2\le nM^2$, donc $\boxed{\|AX\|\le M\sqrt n}$.

### Question 2

> [!INDICATION]
> Vérifie les deux conditions d’existence d’une borne supérieure réelle.

> [!INDICATION]
> Pour comparer les deux ensembles de valeurs, normalise chaque vecteur non nul et teste aussi les vecteurs déjà unitaires.

#### Solution

L’ensemble des valeurs $\|AX\|$ sur la sphère unité est non vide, puisqu’elle contient $E_1$, et majoré d’après Q1. Sa borne supérieure existe.

Si $X_0\ne 0$, le vecteur $X=X_0/\|X_0\|$ est unitaire et $\|AX_0\|/\|X_0\|=\|AX\|$. Réciproquement, tout vecteur unitaire fournit le même quotient que sa valeur $\|AX\|$. Les deux ensembles de valeurs coïncident, donc
$$\boxed{N(A)=\sup_{X_0\ne 0}\frac{\|AX_0\|}{\|X_0\|}.}$$

> [!JURY]
> Le rapport 2025 insiste sur les deux conditions d’existence de la borne supérieure. Il distingue un majorant, la borne supérieure et une valeur effectivement atteinte.

### Question 3

> [!INDICATION]
> Vérifie les axiomes séparément. Pour la séparation, teste la matrice sur une base.

> [!INDICATION]
> Cherche une borne uniforme pour la norme de $(A+B)X$ sur la sphère unité.

#### Solution

Les valeurs dont on prend la borne supérieure sont positives ou nulles, donc $N(A)\ge 0$. Pour $A=0$, elles sont toutes nulles.

Si $N(A)=0$, alors pour tout $i$, $0\le\|AE_i\|\le N(A)=0$. Toutes les colonnes de $A$ sont donc nulles.

Pour tout scalaire $\alpha$, $\|\alpha AX\|=|\alpha|\|AX\|$. Pour $\alpha\ne0$, la multiplication par $|\alpha|$ conserve l’ordre et transforme la borne supérieure en $|\alpha|N(A)$. Pour $\alpha=0$, les deux membres sont nuls.

Enfin, pour tout $X$ unitaire,
$$\begin{aligned}
\|(A+B)X\|&\le\|AX\|+\|BX\|\\
&\le N(A)+N(B).
\end{aligned}$$
Le dernier membre est un majorant commun à ces valeurs, donc $N(A+B)\le N(A)+N(B)$. **Ainsi $N$ est une norme.**

> [!PIEGE]
> L’existence de $N(A)$ relève de Q2. La séparation exige ici d’exploiter $N(A)=0$ pour conclure $A=0$. L’homogénéité de la norme comporte une valeur absolue.

### Question 4

> [!INDICATION]
> Cherche une matrice triangulaire non nulle dont la diagonale est nulle. Quand peut-on la construire ?

#### Solution

Si $n\ge 2$, prenons la matrice $M$ dont le seul coefficient non nul vaut $1$ en position $(1,2)$. Elle est triangulaire de diagonale nulle, donc $\rho(M)=0$, alors que $M\ne 0$.

**Pour $n\ge 2$, $S$ contredit l’axiome de séparation et n’est pas une norme.** Pour $n=1$, $S([m])=|m|$, qui est une norme.

### Question 5

> [!INDICATION]
> Développe le carré de la norme de $\Delta X$, puis majore la somme terme à terme.

> [!INDICATION]
> Pour atteindre ta borne, choisis un vecteur de la base canonique.

#### Solution

Posons $d=\max_i|\delta_i|$ et choisissons $j$ tel que $|\delta_j|=d$.

Pour $X$ unitaire, $\|\Delta X\|^2=\sum_i\delta_i^2 x_i^2\le d^2$. De plus, $\|\Delta E_j\|=d$. La majoration et son atteinte donnent
$$\boxed{N(\Delta)=\max_{i\in\{1,\ldots,n\}}|\delta_i|.}$$

> [!METHODE]
> Pour calculer un supremum, commence par prouver une borne valable pour tout vecteur. L’égalité demande ensuite un vecteur qui réalise cette borne.

### Question 6

> [!INDICATION]
> Identifie le domaine de la fonction à optimiser et vérifie les hypothèses du théorème des bornes atteintes.

#### Solution

L’application $X\mapsto AX$ est linéaire sur un espace de dimension finie, donc continue. La norme est continue, donc leur composée est continue. La sphère unité est non vide, fermée et bornée en dimension finie. Le théorème des bornes atteintes donne
$$\boxed{N(A)=\max_{\|X\|=1}\|AX\|.}$$

> [!JURY]
> Le rapport 2025 rappelle d’indiquer la dimension finie pour justifier la continuité de l’application linéaire.

### Question 7

> [!INDICATION]
> Pour un vecteur non nul, utilise la caractérisation de Q2. Traite le vecteur nul à part.

#### Solution

Pour $X\ne0$, Q2 montre que $\|AX\|/\|X\|\le N(A)$. Pour $X=0$, les deux membres sont nuls. Ainsi $\boxed{\|AX\|\le N(A)\|X\|}$ pour tout $X$.

### Question 8

> [!INDICATION]
> Applique Q7 deux fois, en commençant par le vecteur $BX$.

> [!INDICATION]
> La borne obtenue dépend-elle du choix de $X$ unitaire ?

#### Solution

Pour tout $X$ unitaire, Q7 appliquée à $BX$ donne $\|ABX\|\le N(A)\|BX\|\le N(A)N(B)$. Ce majorant étant indépendant de $X$,
$$\boxed{N(AB)\le N(A)N(B).}$$

> [!METHODE]
> La borne de Q7 s’applique même si $BX=0$. Le produit $AB$ peut être nul avec deux facteurs non nuls. La preuve passe par un majorant uniforme, sans diviser par $\|BX\|$.

### Question 9

> [!INDICATION]
> Choisis un vecteur unitaire dont l’image est la colonne qui t’intéresse.

#### Solution

Chaque $E_i$ est unitaire et $AE_i=C_i$. On a donc $\|C_i\|\le N(A)$ pour chaque $i$, et $\boxed{\max_i\|C_i\|\le N(A)}$.

### Question 10

> [!INDICATION]
> Repère la seule coordonnée de $X$ dont dépend $AX$.

> [!INDICATION]
> Quel vecteur canonique donne l’égalité dans ta majoration ?

#### Solution

Pour $X$ unitaire, $AX=x_nC_n$, donc $\|AX\|\le\|C_n\|$ puisque $|x_n|\le 1$.

Le choix $X=E_n$ atteint cette borne. **On a $N(A)=\|C_n\|$, soit $\sqrt2$ dans l’exemple.**

### II — Cas des matrices orthogonales et symétriques

### Question 11

> [!INDICATION]
> Développe le carré de la norme de $UX$ et utilise la définition matricielle de l’orthogonalité.

#### Solution

Comme $U^\top U=I_n$, on a $\|UX\|^2=X^\top U^\top UX=\|X\|^2$ pour tout $X$. Toutes les valeurs $\|UX\|$ sur la sphère unité valent $1$, donc $\boxed{N(U)=1}$.

### Question 12

> [!INDICATION]
> L’orthogonalité agit ici sur le vecteur de sortie $AX$.

#### Solution

Pour tout $X$ unitaire, $\|UAX\|=\|AX\|$ par conservation de la norme euclidienne. Les deux bornes supérieures sont donc égales et $\boxed{N(UA)=N(A)}$.

### Question 13

> [!INDICATION]
> Utilise la sous-multiplicativité pour obtenir un premier sens.

> [!INDICATION]
> Pour le sens opposé, quel vecteur unitaire $Y$ vérifie $UY=X_0$ ?

#### Solution

Par Q8 et Q11, $N(AU)\le N(A)$. Prenons $X_0$ unitaire avec $\|AX_0\|=N(A)$, comme le permet Q6.

Le vecteur $Y=U^\top X_0$ est unitaire et $UY=X_0$, donc $\|AUY\|=N(A)$.

Il en résulte $N(AU)\ge N(A)$, puis $\boxed{N(AU)=N(A)}$.

> [!METHODE]
> Un facteur orthogonal à gauche préserve la norme de chaque sortie. Un facteur orthogonal à droite envoie la sphère unité sur elle-même.

### Question 14

> [!INDICATION]
> Rends $A$ diagonale dans une base appropriée.

> [!INDICATION]
> Que sait-on des deux matrices qui entourent la diagonale dans l’écriture fournie par le théorème spectral ?

#### Solution

Par le théorème spectral, $A=P\Delta P^\top$ avec $P$ orthogonale et $\Delta$ diagonale réelle. Les coefficients diagonaux de $\Delta$ sont les valeurs propres de $A$. Les questions 12 et 13 donnent $N(A)=N(\Delta)$ et Q5 donne
$$\boxed{N(A)=\rho(A).}$$

### Question 15

> [!INDICATION]
> Décompose $A$ en la somme de l’identité et d’une matrice à coefficients constants.

> [!INDICATION]
> Étudie séparément la droite des vecteurs constants et l’hyperplan des vecteurs dont les coordonnées somment à zéro.

#### Solution

On a $A=I_3+J$ où $J$ est la matrice dont tous les coefficients valent $1$. Pour $v=(1,1,1)^\top$, on a $Jv=3v$, d’où $Av=4v$.

Si $X\in v^\perp$, la somme de ses coordonnées est nulle, donc $JX=0$ et $AX=X$.

Ces sous-espaces supplémentaires donnent le spectre $\{1,4\}$. D’après Q14, $\boxed{N(A)=4}$.

## Partie B — Conditionnement d’une matrice pour la norme $N$

Contrôler à la fois $A$ et $A^{-1}$ est essentiel. L’exemple triangulaire montre que de petits coefficients dans $A$ peuvent coexister avec des coefficients très grands dans son inverse.

### I — Quelques résultats sur le conditionnement

### Question 16

> [!INDICATION]
> Fais apparaître l’identité comme produit de deux matrices dont les normes interviennent dans le conditionnement.

#### Solution

D’après Q11, $N(AA^{-1})=N(I_n)=1$. D’après Q8, $N(AA^{-1})\le N(A)N(A^{-1})$, soit $\boxed{1\le\operatorname{cond}(A)}$.

### Question 17

> [!INDICATION]
> Écris l’inverse de $\alpha A$ puis applique l’homogénéité à chacun des facteurs.

#### Solution

Pour $\alpha\ne 0$, on a $(\alpha A)^{-1}=\alpha^{-1}A^{-1}$. Par homogénéité, les deux normes sont multipliées par $|\alpha|$ et $|\alpha|^{-1}$ respectivement. Ainsi $\boxed{\operatorname{cond}(\alpha A)=\operatorname{cond}(A)}$.

### Question 18

> [!INDICATION]
> Identifie la nature de l’inverse d’une matrice orthogonale et reprends Q11.

#### Solution

Les matrices $U$ et $U^{-1}=U^\top$ sont orthogonales. Leurs normes valent donc $1$ et $\boxed{\operatorname{cond}(U)=1}$.

### Question 19

> [!INDICATION]
> Calcule les deux inverses en respectant l’ordre des facteurs.

> [!INDICATION]
> Applique l’invariance de la norme sous multiplication à gauche et à droite.

#### Solution

Les inverses de $UA$ et $AU$ sont respectivement $A^{-1}U^\top$ et $U^\top A^{-1}$. Par Q12 et Q13, $N(UA)=N(AU)=N(A)$. De même, $N(A^{-1}U^\top)=N(U^\top A^{-1})=N(A^{-1})$. Par conséquent,
$$\boxed{\operatorname{cond}(UA)=\operatorname{cond}(AU)=\operatorname{cond}(A).}$$

> [!PIEGE]
> Le rapport 2025 signale l’erreur consistant à égaler $N(A)$ et $N(A^{-1})$. Pour $A=2I_n$, ces deux normes valent respectivement $2$ et $1/2$.

### II — Un exemple de minoration du conditionnement d’une matrice

### Question 20

> [!INDICATION]
> Les lignes successives donnent une relation à deux termes, sauf la dernière.

> [!INDICATION]
> Compare $x_i$ et $x_{i+1}$ avant de calculer la $i$-ième coordonnée de $AX$.

#### Solution

La matrice $A$ est triangulaire supérieure de diagonale égale à $1$, donc inversible.

Pour les coordonnées de $X$, on a $x_n=1$ et $x_i=-2x_{i+1}$ pour $i<n$.

Or $(AX)_i=x_i+2x_{i+1}=0$ pour $i<n$, et $(AX)_n=x_n=1$. Donc $\boxed{AX=E_n}$.

### Question 21

> [!INDICATION]
> Teste $A^{-1}$ sur un vecteur unitaire déjà apparu à Q20.

> [!INDICATION]
> Il suffit ensuite de garder une coordonnée de l’image dans le calcul de sa norme.

#### Solution

D’après Q20, $A^{-1}E_n=X$. Comme $E_n$ est unitaire, $N(A^{-1})\ge\|X\|$. La norme euclidienne de $X$ est au moins $|x_1|=2^{n-1}$. On obtient $\boxed{N(A^{-1})\ge 2^{n-1}}$.

### Question 22

> [!INDICATION]
> Lis la deuxième colonne de $A$. Combine la borne obtenue avec Q21 et vérifie la dimension nécessaire.

#### Solution

Si $n\ge2$, alors $AE_2=2E_1+E_2$, donc $\|AE_2\|=\sqrt5>2$. Ainsi $N(A)>2$ et, par Q21,
$$\boxed{\operatorname{cond}(A)>2^n\quad\text{pour }n\ge2.}$$
Pour $n=1$, $E_2$ n’existe pas et $A=[1]$ est de conditionnement $1$.

> [!PIEGE]
> La question suppose implicitement $n\ge2$. Une minoration stricte de $N(A)$ suffit, puisque la borne inférieure de $N(A^{-1})$ est strictement positive.

## Partie C — Conditionnement pour une matrice réelle inversible

La matrice $A^\top A$ fait intervenir le carré de la norme de $AX$ et permet d’utiliser le théorème spectral pour une matrice $A$ quelconque.

### Question 23

> [!INDICATION]
> Développe $X$ dans la base $\mathcal C$.

> [!INDICATION]
> Interprète les carrés de ses coordonnées comme des poids de somme $1$, puis cherche un vecteur propre qui atteint la borne.

#### Solution

Les valeurs propres de $S$ sont positives ou nulles, car $\lambda_i=\langle SV_i,V_i\rangle$. D’après Q14, $N(S)=\lambda_n$. Si $X=\sum_i x_iV_i$ est unitaire, alors
$$\begin{aligned}
\langle SX,X\rangle&=\sum_i\lambda_i x_i^2,\\
0\le\langle SX,X\rangle&\le\lambda_n.
\end{aligned}$$
Pour $X=V_n$, on obtient $\lambda_n$. Donc
$$\boxed{N(S)=\max_{\|X\|=1}|\langle SX,X\rangle|.}$$

> [!METHODE]
> Sur la sphère unité, exprimer une forme quadratique dans une base orthonormée de vecteurs propres donne une moyenne pondérée des valeurs propres. Les vecteurs propres extrêmes réalisent les bornes.

### Question 24

> [!INDICATION]
> Calcule le produit scalaire de $A^\top AX$ avec $X$.

> [!INDICATION]
> Applique Q23 en reliant le maximum du carré au maximum de la norme.

#### Solution

La matrice $A^\top A$ est symétrique et, pour tout $X$, $\langle A^\top AX,X\rangle=\|AX\|^2\ge0$. Elle est donc positive. Par Q23 et Q6,
$$\begin{aligned}
N(A^\top A)&=\max_{\|X\|=1}\|AX\|^2\\
&=N(A)^2,
\end{aligned}$$
la fonction carré étant croissante sur les réels positifs et le maximum étant atteint. **Ainsi $N(A^\top A)=N(A)^2$.**

### Question 25

> [!INDICATION]
> Identifie la propriété de $A^\top A$ qui permet d’invoquer Q14.

#### Solution

La matrice $A^\top A$ étant symétrique réelle, Q14 donne $N(A^\top A)=\rho(A^\top A)$. Par Q24 et positivité de la norme,
$$\boxed{N(A)=\sqrt{\rho(A^\top A)}.}$$

### Question 26

> [!INDICATION]
> Reconnais dans l’égalité proposée la formule d’un changement de base matriciel.

#### Solution

L’égalité $A^\top A=A^{-1}(AA^\top)A$ montre que les deux matrices sont semblables. **Elles ont les mêmes valeurs propres, avec les mêmes multiplicités.**

### Question 27

> [!INDICATION]
> Applique Q25 à $A$, puis à $A^{-1}$.

> [!INDICATION]
> Relie la matrice obtenue pour $A^{-1}$ à l’inverse de $AA^\top$ et demande-toi quel extrême spectral devient le plus grand par passage à l’inverse.

#### Solution

Pour $X\ne0$, $\|AX\|^2>0$ puisque $A$ est inversible. La matrice $A^\top A$ est donc définie positive et Q25 donne $N(A)=\sqrt{\mu_M}$.

Par Q26, $AA^\top$ a les mêmes valeurs propres, toutes strictement positives. Dans une base propre, son inverse a les valeurs propres réciproques, dont la plus grande vaut $1/\mu_m$. Or
$$(A^{-1})^\top A^{-1}=(AA^\top)^{-1}.$$
On applique donc Q25 à $A^{-1}$, ce qui donne $N(A^{-1})=1/\sqrt{\mu_m}$. Ainsi
$$\boxed{\operatorname{cond}(A)=\sqrt{\frac{\mu_M}{\mu_m}}.}$$

> [!PIEGE]
> Dans $(A^{-1})^\top A^{-1}$, applique la règle d’inversion d’un produit en renversant l’ordre. La similarité de Q26 relie ensuite les deux ordres.

### Question 28

> [!INDICATION]
> Prends une base propre de $A$. Quel effet le carré a-t-il sur les éléments diagonaux et sur leur ordre ?

#### Solution

Si $A$ est symétrique définie positive, elle est diagonalisable et ses valeurs propres sont strictement positives. Les valeurs propres de $A^\top A=A^2$ sont leurs carrés. Si $\lambda_{\min}$ et $\lambda_{\max}$ sont les extrêmes pour $A$, alors Q27 donne
$$\boxed{\operatorname{cond}(A)=\frac{\lambda_{\max}}{\lambda_{\min}}.}$$

## Partie D — Calcul explicite de conditionnement

Les coordonnées trigonométriques proposées répondent à une relation entre trois termes consécutifs. Les extrémités jouent le rôle de deux coordonnées supplémentaires imposées à zéro.

### Question 29

> [!INDICATION]
> Identifie la propriété de $T$ qui donne accès au théorème spectral.

#### Solution

La matrice $T$ est symétrique réelle. Par le théorème spectral, **toutes ses valeurs propres sont réelles.**

### Question 30

> [!INDICATION]
> Introduis deux coordonnées fictives de part et d’autre du vecteur pour écrire une formule valable sur chaque ligne.

> [!INDICATION]
> Réunis les deux sinus voisins avec la formule d’addition et vérifie que la première coordonnée proposée ne s’annule pas.

#### Solution

Posons $\theta=k\pi/(n+1)$ et $u_i=\sin(i\theta)$ pour $0\le i\le n+1$. On a $u_0=u_{n+1}=0$, donc les lignes extrêmes se traitent avec la même formule que les autres.

Pour tout $1\le i\le n$, la formule d’addition donne
$$\begin{aligned}
(TU_k)_i
&=2u_i-u_{i-1}-u_{i+1}\\
&=2(1-\cos\theta)u_i.
\end{aligned}$$
Comme $k\notin(n+1)\mathbb Z$, $u_1=\sin\theta\ne0$. **Le vecteur $U_k$ est propre, associé à $2-2\cos(k\pi/(n+1))$.**

> [!JURY]
> Le rapport 2025 souligne que l’égalité $TU_k=\lambda U_k$ doit être accompagnée de la preuve que $U_k\ne 0$. Les erreurs de trigonométrie ont également beaucoup gêné le calcul final.

### Question 31

> [!INDICATION]
> Sélectionne $n$ entiers consécutifs pour lesquels les angles sont dans $]0,\pi[$.

> [!INDICATION]
> Utilise la monotonie stricte du cosinus, puis compare le nombre de valeurs obtenues à la dimension.

#### Solution

Pour $k=1,\ldots,n$, les angles $k\pi/(n+1)$ sont strictement croissants dans $]0,\pi[$, où le cosinus est strictement décroissant. Q30 donne donc $n$ valeurs propres distinctes. Le polynôme caractéristique étant de degré $n$, on a
$$\boxed{\operatorname{Sp}(T)=\left\{2-2\cos\frac{k\pi}{n+1}\ \middle|\ k\in\{1,\ldots,n\}\right\}.}$$

> [!METHODE]
> Pour conclure que le spectre est complet, isole une famille de $n$ valeurs distinctes. La formule de Q30 décrit des vecteurs pour bien plus d’indices, dont certains redonnent les mêmes valeurs propres.

### Question 32

> [!INDICATION]
> Déduis du spectre que Q28 s’applique et repère les deux indices extrêmes.

> [!INDICATION]
> Les angles aux extrémités de la liste sont supplémentaires.

#### Solution

Toutes les valeurs propres de $T$ sont strictement positives par Q31, donc $T$ est définie positive. La plus petite correspond à $k=1$ et la plus grande à $k=n$.

Posons $\theta=\pi/(n+1)$. Comme $n\theta=\pi-\theta$, la plus grande vaut $2+2\cos\theta$. Par Q28,
$$\boxed{\operatorname{cond}(T)=\frac{1+\cos\theta}{1-\cos\theta}.}$$

## Partie E — Inégalité de Kantorovich

La minoration repose sur Cauchy-Schwarz. Dans les deux preuves de la majoration, la positivité des valeurs propres est nécessaire pour diviser par ces valeurs, et les valeurs propres extrêmes commandent la constante.

### I — Une première démonstration

### Question 33

> [!INDICATION]
> Reprends Q28 avec les valeurs propres dans l’ordre fourni par le sujet.

#### Solution

Par Q28, **$\operatorname{cond}(A)=\lambda_n/\lambda_1$.**

### Question 34

> [!INDICATION]
> Applique Cauchy-Schwarz dans le produit scalaire introduit par le sujet.

> [!INDICATION]
> Choisis le second vecteur de façon que $A$ se simplifie dans le produit scalaire mixte.

#### Solution

Appliquons Cauchy-Schwarz dans le produit scalaire $(\cdot,\cdot)_A$ aux vecteurs $X$ et $A^{-1}X$. Par symétrie de $A$,
$$(X,A^{-1}X)_A=\langle AX,A^{-1}X\rangle=\|X\|^2.$$
Les carrés des normes de ces vecteurs pour ce produit scalaire sont $\langle AX,X\rangle$ et $\langle X,A^{-1}X\rangle$. Par conséquent,
$$\boxed{\|X\|^4\le\langle AX,X\rangle\langle A^{-1}X,X\rangle.}$$

> [!METHODE]
> Le produit scalaire pondéré par $A$ fait apparaître les deux facteurs voulus dans Cauchy-Schwarz. La symétrie de $A$ permet de transférer $A$ d’un vecteur à l’autre dans le produit mixte.

### Question 35

> [!INDICATION]
> Reconnais les deux racines explicites de $P$, puis situe chaque $\lambda_k$ entre elles.

#### Solution

On a $P(t)=(t-\lambda_1)(t-\lambda_n)$. Pour chaque $k$, le premier facteur pris en $\lambda_k$ est positif ou nul et le second est négatif ou nul. Ainsi $\boxed{P(\lambda_k)\le 0}$.

### Question 36

> [!INDICATION]
> Fais agir les deux facteurs de $B$ sur chaque $V_k$.

> [!INDICATION]
> Utilise l’orthonormalité pour écrire le produit scalaire comme une somme de termes dont tu connais le signe.

#### Solution

Dans la base propre $\mathcal C$, $P(A)V_k=P(\lambda_k)V_k$ et $A^{-1}V_k=\lambda_k^{-1}V_k$. Les valeurs propres de $B$ sont donc $P(\lambda_k)/\lambda_k$, toutes négatives ou nulles. Cette base étant orthonormée, si $X=\sum_k x_kV_k$, alors
$$\boxed{\langle BX,X\rangle=\sum_{k=1}^n\frac{P(\lambda_k)}{\lambda_k}x_k^2\le0.}$$

### Question 37

> [!INDICATION]
> Développe $B$ et compare avec $f(1)$. Pour $f(0)$, regarde le spectre de $A^{-1}$.

> [!INDICATION]
> Interprète le signe de $f(0)f(1)$ via le théorème des valeurs intermédiaires. Le discriminant ne s’applique qu’une fois le degré vérifié.

#### Solution

On a $B=A-(\lambda_1+\lambda_n)I_n+\lambda_1\lambda_nA^{-1}$. En prenant le produit scalaire de $BX$ avec $X$, on retrouve $f(1)$.

D’après Q36, $f(1)\le0$. La matrice $A^{-1}$ est définie positive, car ses valeurs propres dans la base orthonormée $\mathcal C$ sont les $\lambda_k^{-1}>0$.

On a donc $f(0)\ge0$, d’où $f(0)f(1)\le0$.

Pour $X=0$, l’inégalité demandée est une égalité.

Pour $X\ne0$, le coefficient de $\lambda^2$ vaut $\langle AX,X\rangle>0$. La fonction $f$ admet un zéro dans $[0,1]$ par continuité, donc son discriminant est positif ou nul. D’où
$$\boxed{(\lambda_1+\lambda_n)^2\|X\|^4-4\lambda_1\lambda_n\langle AX,X\rangle\langle A^{-1}X,X\rangle\ge0.}$$

> [!PIEGE]
> Pour $X=0$, la fonction $f$ est identiquement nulle. Commence par ce cas avant d’utiliser une propriété des polynômes du second degré.

### Question 38

> [!INDICATION]
> Divise l’inégalité $(\star)$ par son coefficient positif devant le produit des deux formes quadratiques.

> [!INDICATION]
> Récris la fraction obtenue à l’aide de Q33 et retrouve la minoration dans les premières questions de E.

#### Solution

En divisant $(\star)$ par $4\lambda_1\lambda_n>0$, on obtient la majoration du produit par $\frac{(\lambda_1+\lambda_n)^2}{4\lambda_1\lambda_n}\|X\|^4$. Avec $c=\operatorname{cond}(A)=\lambda_n/\lambda_1$,
$$\frac{(\lambda_1+\lambda_n)^2}{4\lambda_1\lambda_n}=\frac14\left(\frac1{\sqrt c}+\sqrt c\right)^2.$$
La minoration est celle de Q34. **Ces deux bornes établissent l’inégalité (K).**

### II — Une deuxième démonstration

### Question 39

> [!INDICATION]
> Teste les conditions que doivent remplir les masses attribuées aux indices.

> [!INDICATION]
> Si deux indices ont la même valeur propre, commence par tirer un indice puis observe la valeur propre correspondante.

#### Solution

Les poids $x_i^2$ sont positifs ou nuls et leur somme vaut $1$, car $\mathcal C$ est orthonormée et $\|X\|=1$.

Ces poids définissent une probabilité sur $\Omega=\{1,\ldots,n\}$, en posant $\mathbb P(\{i\})=x_i^2$.

Avec $Z(i)=\lambda_i$, posons $I_t=\{i\in\Omega:\lambda_i=t\}$. On obtient la loi
$$\boxed{\mathbb P(Z=t)=\sum_{i\in I_t}x_i^2.}$$
Si les valeurs propres sont distinctes, on retrouve la formule de l’énoncé. En présence de multiplicités, il faut regrouper les poids correspondant à la même valeur propre.

> [!JURY]
> Le rapport 2025 demande d’expliciter la positivité des poids. Pour rendre la construction valable avec les multiplicités autorisées, la solution pose les masses sur les indices avant de calculer la loi de $Z$.

### Question 40

> [!INDICATION]
> Repère pourquoi les deux variables prennent un nombre fini de valeurs bien définies.

> [!INDICATION]
> Calcule les espérances sur l’espace des indices. Compare avec les produits scalaires écrits dans la base $\mathcal C$.

#### Solution

Les deux variables sont à valeurs dans des ensembles finis et $Z$ ne prend que des valeurs strictement positives, donc elles admettent une espérance. Sur l’espace des indices de Q39 et dans la base $\mathcal C$,
$$\boxed{\begin{aligned}
\mathbb E(Z)&=\sum_{i=1}^n \lambda_ix_i^2=\langle AX,X\rangle,\\
\mathbb E(1/Z)&=\sum_{i=1}^n \frac{x_i^2}{\lambda_i}=\langle A^{-1}X,X\rangle.
\end{aligned}}$$

### Question 41

> [!INDICATION]
> Développe le produit proposé par l’énoncé. Quelle quantité strictement positive permet de faire apparaître l’inverse de $Z$ ?

#### Solution

On a $\lambda_1\le Z\le\lambda_n$, donc $(Z-\lambda_1)(Z-\lambda_n)\le0$. En développant,
$$Z^2-(\lambda_1+\lambda_n)Z+\lambda_1\lambda_n\le0.$$
On divise par $Z>0$ puis on isole son inverse. Ainsi
$$\boxed{\frac1Z\le\frac{\lambda_1+\lambda_n-Z}{\lambda_1\lambda_n}.}$$

### Question 42

> [!INDICATION]
> Passe à l’espérance en nommant les propriétés qui justifient chaque opération.

> [!INDICATION]
> Après multiplication par $\mathbb E(Z)$, reconnais un trinôme en cette quantité et mets-le sous forme canonique.

#### Solution

Par croissance et linéarité de l’espérance appliquée à Q41,
$$\mathbb E(1/Z)\le\frac{\lambda_1+\lambda_n-\mathbb E(Z)}{\lambda_1\lambda_n}.$$
Par positivité, $m=\mathbb E(Z)\ge0$. On peut donc multiplier par $m$, d’où
$$\mathbb E(Z)\mathbb E(1/Z)\le
\frac{(\lambda_1+\lambda_n)m-m^2}{\lambda_1\lambda_n}.$$
En complétant le carré au numérateur, on obtient
$$\boxed{\mathbb E(Z)\mathbb E(1/Z)\le
-\frac{1}{\lambda_1\lambda_n}\left(m-\frac{\lambda_1+\lambda_n}{2}\right)^2
+\frac{(\lambda_1+\lambda_n)^2}{4\lambda_1\lambda_n}.}$$

> [!JURY]
> Le rapport 2025 demande de préciser où interviennent la croissance, la linéarité et la positivité de l’espérance.

### Question 43

> [!INDICATION]
> Isole le signe du terme carré dans la majoration obtenue.

> [!INDICATION]
> Reviens aux formes quadratiques, puis normalise le vecteur pour étendre la borne à toute norme.

#### Solution

En supprimant le terme négatif ou nul dans la majoration de Q42 et en utilisant Q40, on obtient
$$\langle AX,X\rangle\langle A^{-1}X,X\rangle\le
\frac{(\lambda_1+\lambda_n)^2}{4\lambda_1\lambda_n}$$
pour tout $X$ unitaire. Pour $X\ne0$, on applique ce résultat à $X/\|X\|$ et on multiplie par $\|X\|^4$.

Pour $X=0$, les deux membres sont nuls. Avec Q33, le coefficient s’écrit $\frac14(1/\sqrt{\operatorname{cond}(A)}+\sqrt{\operatorname{cond}(A)})^2$. **On retrouve la majoration de (K).**

> [!METHODE]
> Vérifie l’homogénéité d’une inégalité sur les vecteurs. Chaque forme quadratique contribue ici un facteur $\|X\|^2$ au retour de la sphère unité à l’espace entier.

## Bilan

Pour une norme définie par une borne supérieure, sépare trois tâches : prouver son existence, comparer ses valeurs et établir son atteinte. Teste les vecteurs de la base canonique pour obtenir des minorations rapides et les vecteurs propres pour détecter les cas d’égalité après diagonalisation.

Pour un problème de conditionnement, calcule d’abord le spectre de $A^\top A$. La plus petite valeur propre intervient parce que l’inversion échange les extrêmes positifs. Pour les matrices tridiagonales, entraîne-toi à écrire une relation uniforme sur les coordonnées et à vérifier séparément les conditions aux extrémités.

Les deux majorations de Kantorovich partent du même produit $(t-\lambda_1)(t-\lambda_n)$. La première l’applique à un polynôme de la matrice, la seconde à une variable aléatoire. Dans cette seconde approche, les carrés des coordonnées dans une base propre constituent des masses sur les indices. Cette construction reste valable avec des valeurs propres multiples.
