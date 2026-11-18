# Mines-Ponts MP — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*


## Présentation du sujet

Ce problème de quatre heures cherche à compter les racines d’un polynôme réel scindé dont le module est strictement inférieur à un. Il traduit ce comptage en nombre de valeurs propres positives d’une matrice symétrique. Le cas singulier demande de séparer les racines qui vont par paires réciproques des autres, puis d’utiliser une déformation du polynôme.

A étudie le polynôme réciproque et ses racines. B construit une famille libre, puis C utilise un télescopage pour factoriser la matrice. D transforme cette factorisation en une égalité de comptage par congruence, et E caractérise l’inversibilité. F traite des racines réciproques simples par une dérivation en paramètre. G sépare le cas général en couches auxquelles on applique ces résultats.

Les questions Q1–Q3, Q6, Q10, Q12–Q13 et Q15–Q17 fournissent des points d’entrée, même après un blocage. Q9 et Q11 demandent de choisir une organisation des calculs. En fin d’épreuve, Q22–Q23 et Q27 peuvent se traiter sans avoir mené à bien la dérivation matricielle.

## A — Propriétés du polynôme $p_0$ et stabilité des racines

Le réciproque s’obtient en renversant les coefficients jusqu’au degré du polynôme. Les racines nulles demandent une attention particulière, car elles ne donnent aucun inverse.

### Question 1

> [!INDICATION]
> Développez $p(1/x)$ puis multipliez par la puissance convenable de $x$.

> [!INDICATION]
> Repartez ensuite de la factorisation en racines. Comment passer d’une égalité pour les réels non nuls à une égalité de polynômes ?

#### Solution

Pour $x\ne0$, le développement donne $x^np(1/x)=\sum_{k=0}^n a_k x^{n-k}=p_0(x)$. Or, par scindement de $p$,
$$
x^np(1/x)=a_n\prod_{j=1}^n(1-\alpha_j x).
$$
Les deux polynômes coïncident en une infinité de points. On en déduit **$p_0=a_n\prod_{j=1}^n(1-\alpha_j X)$**.

> [!JURY]
> Le rapport insiste sur le passage d’une identité sur les réels non nuls à une identité de polynômes. L’infinité de l’ensemble où les deux polynômes coïncident justifie ce passage.

### Question 2

> [!INDICATION]
> Reliez l’existence d’un facteur commun à celle d’une racine commune, en utilisant une hypothèse sur $p$.

> [!INDICATION]
> Vérifiez si zéro peut être une racine commune avant d’appliquer Q1.

#### Solution

Si $\alpha$ est une racine stable, elle est non nulle et vérifie $p(\alpha)=p(1/\alpha)=0$. Par Q1, $p_0(\alpha)=0$. Le PGCD est donc divisible par $X-\alpha$.

Réciproquement, tout diviseur non constant de $p$ a une racine réelle puisque $p$ est scindé sur $\mathbb R$.

Si le PGCD est non constant, il existe donc une racine commune $\alpha$.

Elle est non nulle, car $p_0(0)=a_n\ne0$.

La formule de Q1 donne alors $p(1/\alpha)=0$.

**Ainsi $p\wedge p_0=1$ exactement lorsque $p$ ne possède aucune racine stable.**

> [!JURY]
> Le rapport rappelle que le scindement de p est ce qui permet de trouver une racine réelle dans un facteur commun non constant. Il signale aussi le cas d’une racine nulle.

### Question 3

> [!INDICATION]
> Comparez les ensembles de racines avec leurs multiplicités, puis utilisez le degré.

> [!INDICATION]
> Dans ce cas particulier, le degré ne baisse pas lorsqu’on prend le réciproque. Que donne un second passage au réciproque ?

#### Solution

Toutes les racines de $p$ sont non nulles et leur ensemble est invariant par inversion.

Par simplicité, la formule de Q1 donne à $p_0$ les mêmes $n$ racines simples que $p$.

En particulier, $p_0$ est de degré $n$ et il existe $\lambda\in\mathbb R^*$ tel que $p=\lambda p_0$.

Le passage au réciproque des deux polynômes de degré $n$ donne $p_0=\lambda p$. Il vient $\lambda^2=1$, donc **$\lambda\in\{-1,1\}$**.

### Question 4

> [!INDICATION]
> Dérivez l’identité de Q1 combinée à Q3 avant de multiplier par $x$.

> [!INDICATION]
> Calculez séparément le réciproque de $h$ en partant de son degré réel.

#### Solution

Pour $x\ne0$, dérivons $p(x)=\lambda x^np(1/x)$, puis multiplions par $x$. On obtient
$$
xp'(x)=np(x)-\lambda x^{n-1}p'(1/x).
$$
Comme $\deg p'=n-1$, le dernier produit sans son coefficient $-\lambda$ vaut $(p')_0(x)$. L’égalité polynomiale suit, car elle est vraie pour tout $x\ne0$.

Par ailleurs, comme $\deg h=n$, on a $h_0(x)=x^{n-1}p'(1/x)=(p')_0(x)$ pour $x\ne0$. L’égalité vaut donc entre polynômes. Comme $\lambda^2=1$,
$$
\boxed{\begin{aligned}
h&=np-\lambda(p')_0,\\
h_0&=\lambda(np-Xp').
\end{aligned}}
$$

> [!PIEGE]
> Le degré intervient dans la définition du réciproque. Écrivez l’exposant pour chacun des polynômes considérés au lieu de traiter l’opération comme une application linéaire indépendante du degré.

### Question 5

> [!INDICATION]
> Appliquez Rolle sur les intervalles délimités par les racines distinctes de $p$. Combien de racines de $p'$ obtenez-vous ?

> [!INDICATION]
> Si un réel annule $h$ et son réciproque, que dit Q4 sur ce réel ? Exploitez alors simplicité et non-nullité.

#### Solution

Si $n\ge2$, considérons chacun des $n-1$ segments joignant deux racines consécutives, qui sont distinctes. Le polynôme $p$ est continu sur chaque segment, dérivable à l’intérieur et nul aux deux bornes.

Rolle donne une racine de $p'$ à l’intérieur de chaque intervalle.

Ce sont $n-1$ racines distinctes, donc $p'$ est scindé.

Pour $n=1$, $p'$ est constant non nul.

Le polynôme $h=Xp'$ est scindé.

Si $h$ et $h_0$ avaient un diviseur commun non constant, ils auraient une racine réelle commune $\beta$.

D’après Q4, $p(\beta)=0$.

La racine $\beta$ de $p$ est non nulle et simple, donc $h(\beta)=\beta p'(\beta)\ne0$, contradiction.

Ainsi $h\wedge h_0=1$.

Si une racine non nulle de $p'$ avait son inverse aussi racine, ces deux nombres seraient également racines de $h$. La formule du réciproque appliquée à $h$ contredirait alors $h\wedge h_0=1$. **Le polynôme $p'$ ne possède aucune racine stable.**

> [!JURY]
> Le rapport attend une application de Rolle avec ses hypothèses. Vérifiez la continuité sur le segment fermé, la dérivabilité sur son intérieur et l’égalité des valeurs aux deux extrémités.

## B — Liberté d’une famille de polynômes

Le problème de liberté se ramène à l’action d’opérateurs sur les facteurs d’une fraction. Il faut distinguer un pôle admissible et une valeur en laquelle on a le droit d’évaluer.

### Question 6

> [!INDICATION]
> Comparez $j$ à l’indice $i$ de la racine donnée. Selon le cas, repérez un facteur de type $X-\alpha_i$ ou un facteur qui s’annule au même point.

> [!INDICATION]
> Tous les polynômes ont un degré borné. Quelle est la dimension du sous-espace des polynômes de ce degré qui s’annulent en un point fixé ?

#### Solution

Pour $j\le i$, le produit définissant $f_j$ contient le facteur $1-\alpha_kX$ puisque $k>j$.

Il s’annule en $\alpha_i$.

Pour $j>i$, le produit contient le facteur $X-\alpha_i$.

Ainsi tous les $f_j$ s’annulent en $\alpha_i$.

Ils sont de degré au plus $n-1$. Le sous-espace de ces polynômes divisibles par $X-\alpha_i$ est de dimension $n-1$, car il s’obtient en multipliant $\mathbb R_{n-2}[X]$ par ce facteur. Il contient les $n$ polynômes, donc **$(f_1,\ldots,f_n)$ est liée**.

> [!METHODE]
> Une racine commune donne une contrainte linéaire sur un espace de polynômes de degré borné. C’est la comparaison du nombre de polynômes avec la dimension de ce sous-espace qui montre la dépendance.

### Question 7

> [!INDICATION]
> Vérifiez d’abord que l’on peut évaluer $f$ en $\alpha_j$, grâce à l’absence de racines stables.

> [!INDICATION]
> Réduisez au même dénominateur. Pour le noyau, étudiez ce que doit valoir la fraction $(1-\alpha_j X)f$.

#### Solution

Fixons $j$ et écrivons $a=\alpha_j$. L’absence de racine stable assure qu’aucun facteur de dénominateur autorisé ne s’annule en $a$. En particulier, $1-a^2\ne0$ et l’évaluation $f\mapsto f(a)$ est bien définie et linéaire sur $E$.

Écrivons $f=A/B$ avec $B$ un produit de facteurs autorisés. Alors
$$
P_j(f)=\frac{(1-aX)A-(1-a^2)f(a)B}{(X-a)B}.
$$
Le numérateur s’annule en $a$. Après simplification, le dénominateur $B$ est autorisé, donc $P_j(f)\in E$. La formule étant linéaire en $f$, $P_j$ est un endomorphisme de $E$.

Si $P_j(f)=0$, $(1-aX)f$ est constant. Réciproquement, pour $f=c/(1-aX)$, on a $(1-a^2)f(a)=c$, donc $P_j(f)=0$. Finalement,
$$
\boxed{\ker P_j=\operatorname{Vect}\left(\frac{1}{1-\alpha_j X}\right).}
$$

> [!JURY]
> Le rapport insiste sur le fait que l’application prend ses valeurs dans E et sur la démonstration des deux inclusions pour son noyau. La simplification du facteur au point d’évaluation est la première étape.

### Question 8

> [!INDICATION]
> Calculez la valeur en $\alpha_j$ de la fraction à laquelle s’applique $P_j$.

#### Solution

La fraction $f=(X-\alpha_j)g/(1-\alpha_j X)$ appartient à $E$.

Comme $g$ n’a pas de pôle en $\alpha_j$ et que $1-\alpha_j^2\ne0$, on a $f(\alpha_j)=0$.

En remplaçant dans la définition, **$P_j(f)=g$**.

### Question 9

> [!INDICATION]
> Réécrivez $g_j$ pour faire apparaître des facteurs de la forme $(X-\alpha_i)/(1-\alpha_i X)$.

> [!INDICATION]
> Dans une relation, regardez l’effet successif des opérateurs sur le premier terme encore présent et sur les termes qui le suivent.

#### Solution

Posons $r_i=(X-\alpha_i)/(1-\alpha_i X)$ et $s_i=1/(1-\alpha_i X)$. La définition donne
$$
g_j=a_n r_1\cdots r_{j-1}s_j.
$$
Dans une relation linéaire non triviale entre les $g_j$, soit $m$ le plus grand indice de coefficient non nul. Appliquons successivement $P_1,\ldots,P_{m-1}$. À chaque étape $i$, Q7 annule le terme devenu multiple de $s_i$ et Q8 retire le facteur $r_i$ des termes d’indice supérieur.

Il ne reste que le terme d’indice $m$, devenu un multiple non nul de $s_m$, contradiction. Le cas $m=1$ donne la même contradiction sans appliquer d’opérateur. Ainsi les $g_j$ sont libres. Leur dénominateur commun est un polynôme non nul, donc **les $f_j$ sont libres**.

## C — Expression de la matrice $J(p)$

Remplacer un facteur à la fois permet de relier les deux produits qui définissent la matrice. La différence élémentaire est de rang au plus un.

### Question 10

> [!INDICATION]
> Faites agir $S^\top$ sur chaque vecteur de la base canonique, puis itérez.

#### Solution

Si $(e_1,\ldots,e_n)$ est la base canonique des colonnes, on a $U=e_1$. Par définition de $S$, $S^\top e_j=e_{j+1}$ pour $j<n$, et $S^\top e_n=0$.

Par récurrence, $(S^\top)^iU=e_{i+1}$ pour $0\le i\le n-1$. **La famille demandée est la base canonique.**

### Question 11

> [!INDICATION]
> Définissez des produits intermédiaires en remplaçant un facteur à chaque étape, entre le réciproque et le polynôme initial.

> [!INDICATION]
> Exprimez chaque différence de produits matriciels au moyen de $f_j$, puis sommez.

#### Solution

Pour $0\le j\le n$, posons
$$
p_j=a_n\prod_{k\le j}(X-\alpha_k)\prod_{k>j}(1-\alpha_kX).
$$
Ainsi $p_n=p$ et, dans cette notation intermédiaire, $p_0$ est le réciproque. Pour $1\le j\le n$, on a $p_{j-1}(S)=C_j f_j(S)$ et $p_j(S)=B_j f_j(S)$. En transposant, l’ordre des facteurs s’inverse. Par conséquent,
$$
\begin{aligned}
&p_{j-1}(S)^\top p_{j-1}(S)-p_j(S)^\top p_j(S)\\
&\qquad=f_j(S)^\top(C_j^\top C_j-B_j^\top B_j)f_j(S).
\end{aligned}
$$
La somme télescope, d’où
$$
\boxed{J(p)=\sum_{j=1}^n f_j(S)^\top(C_j^\top C_j-B_j^\top B_j)f_j(S).}
$$

> [!JURY]
> Le rapport signale les erreurs d’ordre des facteurs à la transposition. Les polynômes d’une même matrice commutent, mais cette propriété ne permet pas d’intervertir sans justification une matrice et une transposée.

### Question 12

> [!INDICATION]
> Développez chacun des deux produits et comparez leurs termes non diagonaux.

> [!INDICATION]
> Déterminez la matrice $S^\top S$ en appliquant d’abord $S$ aux vecteurs de la base canonique.

#### Solution

Pour $a=\alpha_j$, les développements donnent
$$
\begin{aligned}
C_j^\top C_j&=I_n-a(S+S^\top)+a^2S^\top S,\\
B_j^\top B_j&=S^\top S-a(S+S^\top)+a^2I_n.
\end{aligned}
$$
Comme $Se_1=0$ et $Se_j=e_{j-1}$ pour $j\ge2$, on a $S^\top S=I_n-UU^\top$. En soustrayant,
$$
\boxed{C_j^\top C_j-B_j^\top B_j=(1-\alpha_j^2)UU^\top.}
$$

### Question 13

> [!INDICATION]
> Dans Q11, remplacez la différence centrale par le résultat de Q12.

> [!INDICATION]
> Identifiez le vecteur colonne qui apparaît. Vérifiez comment la transposition agit sur un polynôme de $S$.

#### Solution

La transposée d’une puissance de $S$ est la même puissance de $S^\top$. Par linéarité, $f_j(S)^\top U=f_j(S^\top)U=V_j$. Les questions 11 et 12 donnent donc
$$
\boxed{\begin{aligned}
J(p)&=\sum_{j=1}^n(1-\alpha_j^2)V_jV_j^\top\\
&=VDV^\top.
\end{aligned}}
$$
La dernière égalité vient de la multiplication par la matrice diagonale $D$.

### Question 14

> [!INDICATION]
> Une racine stable peut coïncider avec son inverse. Dans ce cas, examinez les coefficients de $D$.

> [!INDICATION]
> Si les deux racines sont distinctes, utilisez Q6 pour étudier les colonnes de $V$.

#### Solution

Si $p$ admet $1$ ou $-1$ parmi ses racines, un coefficient diagonal de $D$ est nul. Par Q13, le rang de $J(p)$ est alors strictement inférieur à $n$.

Sinon, une racine stable et son inverse sont distincts et figurent à deux indices distincts. La famille $(f_j)$ est liée par Q6, donc les colonnes $V_j$ sont liées par linéarité de $f\mapsto f(S^\top)U$. La factorisation Q13 donne encore $\operatorname{rg}J(p)<n$. **Dans les deux cas, $J(p)$ est non inversible.**

> [!JURY]
> Le rapport attend un traitement séparé des racines égales à leur propre inverse. Un seul indice suffit alors à rendre D singulière.

## D — Cas où $J(p)$ est inversible, critère de Schur-Cohn

Le nombre de valeurs propres positives est la dimension maximale d’un sous-espace où la forme quadratique est strictement positive. Cette caractérisation se transporte par changement de variables.

### Question 15

> [!INDICATION]
> Transportez un sous-espace de positivité par l’application linéaire associée à $P$.

> [!INDICATION]
> Réécrivez ensuite $B$ à l’aide de $A$ et de l’inverse de $P$.

#### Solution

Si $F$ vérifie $(C_A)$, la restriction de l’automorphisme $X\mapsto PX$ est un isomorphisme de $F$ vers $PF$.

Pour $Y=PX\ne0$ dans $PF$, on a
$$
Y^\top BY=X^\top AX>0.
$$
Donc $PF$ vérifie $(C_B)$ et a même dimension que $F$. Ainsi $d(B)\ge d(A)$. En utilisant $B=(P^{-1})^\top AP^{-1}$, on obtient l’inégalité inverse. **$d(A)=d(B)$.**

> [!METHODE]
> Une congruence transporte la forme quadratique par changement de variables. Le sous-espace d’arrivée est l’image du sous-espace de départ par cette application.

### Question 16

> [!INDICATION]
> Prenez une base orthonormée de vecteurs propres de la matrice symétrique.

> [!INDICATION]
> Dans cette base, retenez les directions qui donnent une contribution strictement positive à la forme.

#### Solution

Le théorème spectral donne une base orthonormée $(v_1,\ldots,v_n)$ de vecteurs propres de $M$, de valeurs propres $\lambda_1,\ldots,\lambda_n$. Posons $F_M=\operatorname{Vect}(v_i:\lambda_i>0)$. Cet espace a dimension $\pi(M)$.

Si $X=\sum_{\lambda_i>0}x_i v_i$ est non nul, alors $X^\top MX=\sum_{\lambda_i>0}\lambda_i x_i^2>0$. **L’espace $F_M$ vérifie $(C_M)$ et $d(M)\ge\pi(M)$.**

### Question 17

> [!INDICATION]
> Estimez la dimension de $F_M^\perp\cap G$ par la formule de Grassmann.

> [!INDICATION]
> Écrivez la forme quadratique sur un vecteur non nul de cette intersection dans la base de Q16.

#### Solution

Si $G$ vérifie $(C_M)$ et $\dim G>\pi(M)$, alors
$$
\begin{aligned}
\dim(F_M^\perp\cap G)
&=\dim F_M^\perp+\dim G-\dim(F_M^\perp+G)\\
&\ge \dim G-\pi(M)\\
&\ge1.
\end{aligned}
$$
Pour $X\ne0$ dans cette intersection, ses coordonnées selon les vecteurs propres de valeur propre strictement positive sont nulles. Dans la base orthonormée de Q16, il vient $X^\top MX\le0$. Cela contredit $(C_M)$ sur $G$. Avec Q16, **$d(M)=\pi(M)$**.

### Question 18

> [!INDICATION]
> Déduisez la non-stabilité des racines de Q14. Contrôlez le rang de la matrice de passage dans Q13.

> [!INDICATION]
> Utilisez les questions de cette partie pour comparer les nombres de directions positives des deux matrices symétriques.

#### Solution

Si $J(p)$ est inversible, Q14 exclut les racines stables. Par Q13, $V$ est inversible puisque $n=\operatorname{rg}J(p)\le\operatorname{rg}V$.

La factorisation est une congruence, avec la matrice de passage $V^\top$.

Les matrices $D$ et $J(p)$ étant symétriques, les questions 15 à 17 donnent $\pi(J(p))=\pi(D)$.

Or $1-\alpha_j^2>0$ exactement lorsque $-1<\alpha_j<1$.

Par conséquent **$\pi(J(p))=\sigma(p)$**.

> [!JURY]
> Le rapport rappelle que la symétrie est nécessaire dans l’identification obtenue en Q16–Q17. La factorisation utilisée est une congruence et ne demande aucune orthogonalité de V.

## E — Condition nécessaire et suffisante d’inversibilité

Une relation linéaire entre les colonnes de la factorisation se traduit en une relation entre les coefficients d’un polynôme de petit degré.

### Question 19

> [!INDICATION]
> Examinez $D$ en l’absence de racine stable, puis tirez une conséquence sur $V$ de la singularité supposée.

> [!INDICATION]
> Une relation entre les colonnes est obtenue en évaluant une relation entre polynômes. Utilisez Q9 pour contrôler le polynôme ainsi construit.

#### Solution

En l’absence de racine stable, aucune racine n’est égale à $1$ ou $-1$.

La matrice $D$ est donc inversible.

Si $V$ était inversible, les trois facteurs de Q13 seraient inversibles, ce qui contredirait l’hypothèse sur $J(p)$.

Donc $V$ est singulière.

Il existe donc des réels $c_j$, non tous nuls, tels que $\sum_{j=1}^n c_j V_j=0$.

Posons $q=\sum_{j=1}^n c_j f_j$. Ce polynôme est non nul par Q9, de degré au plus $n-1$, et **$q(S^\top)U=0$**.

### Question 20

> [!INDICATION]
> Appliquez Q10 aux coefficients du polynôme de Q19, puis rappelez l’implication donnée par Q14.

#### Solution

D’après Q10, l’application qui envoie $q=\sum_{i=0}^{n-1}b_iX^i$ sur $\sum_{i=0}^{n-1}b_i(S^\top)^i U$ est injective. Le polynôme non nul de Q19 ne peut exister. Cela donne l’inversibilité en l’absence de racine stable. Avec Q14, **$J(p)$ est inversible si et seulement si $p$ n’a aucune racine stable**.

## F — Un cas particulier

On rapproche les racines du seuil de module un par un paramètre. La dérivation donne une matrice limite et le signe du facteur de renormalisation échange les comptes positif et négatif.

### Question 21

> [!INDICATION]
> Comparez les racines non nulles de $h$ et de $p'$, puis revenez au critère de Q20.

#### Solution

Par Q5, $p'$ est scindé et ne possède aucune racine stable. Le polynôme $h=Xp'$ est scindé. La racine ajoutée est nulle et n’entre pas dans la définition de la stabilité. Les racines non nulles de $h$ étant exactement celles de $p'$, $h$ n’a aucune racine stable. **$J(h)$ est inversible par Q20.**

### Question 22

> [!INDICATION]
> Écrivez les racines du polynôme dilaté et repérez celles qui peuvent entrer ou sortir de l’intervalle.

> [!INDICATION]
> Pour une paire réciproque après dilatation, quelle valeur doit prendre le produit de deux racines initiales ? Il n’y a qu’un nombre fini de produits à éviter.

#### Solution

Pour $r>0$, les racines de $p(rX)$ sont les $\alpha_j/r$ avec leurs multiplicités, donc ce polynôme est scindé.

Choisissons $b\in[0,1[$ au moins égal à tous les $|\alpha_j|<1$ et à tous les $\sqrt{\alpha_i\alpha_j}$ pour lesquels $0<\alpha_i\alpha_j<1$.

Cette famille de contraintes est finie, y compris lorsque l’une des listes est vide.

Si $b<r<1$, les racines initialement dans $]-1,1[$ y restent après division par $r$.

Celles dont le module vaut au moins $1$ restent à l’extérieur.

En outre, une paire de racines inverses imposerait $\alpha_i\alpha_j=r^2$, en autorisant $i=j$.

Les produits strictement entre $0$ et $1$ ont une racine carrée au plus $b$, et les autres ne peuvent valoir $r^2$.

**On peut prendre $\eta=1-b$.**

> [!PIEGE]
> Pour exclure les paires réciproques, les deux indices peuvent être égaux. Cela couvre les racines de module un.

### Question 23

> [!INDICATION]
> Pour un paramètre proche du seuil, appliquez les conclusions de Q18 et Q22.

> [!INDICATION]
> Avant de passer à la limite, étudiez le signe du facteur qui multiplie la matrice.

#### Solution

Pour $r\in]1-\eta,1[$ suffisamment près de $1$, Q22 et Q20 donnent l’inversibilité de $F(r)$. Par Q18, cette matrice symétrique a $\sigma(p)$ valeurs propres strictement positives. Elle a donc $n-\sigma(p)$ valeurs propres strictement négatives.

Le facteur $n/(2(r-1))$ est strictement négatif. La quantité étudiée est ainsi constante sur un voisinage à gauche de $1$ et
$$
\boxed{\lim_{r\to1^-}\pi\left(\frac{n}{2(r-1)}F(r)\right)=n-\sigma(p).}
$$

### Question 24

> [!INDICATION]
> Exprimez le réciproque de $p(rX)$ à partir de $p_0$ par comparaison des coefficients.

> [!INDICATION]
> Dérivez les deux familles de matrices à part et n’appliquez la règle du produit qu’ensuite.

#### Solution

Notons $p_r=p(rX)$.

Pour $r>0$, son degré est $n$ et $(p_r)_0(X)=r^n p_0(X/r)$.

Les deux matrices $p_r(S)$ et $(p_r)_0(S)$ ont des coefficients polynomiaux en $r$, donc $F$ est dérivable à valeurs dans les matrices symétriques.

La dérivée de $p_r(S)$ en $r=1$ vaut $h(S)=p'(S)S$. Pour le réciproque, elle vaut $(np_0-Xp_0')(S)=h_0(S)$, par $p_0=\lambda p$ et Q4.

Posons $A=p(S)$ et $H=h(S)$. Alors $p_0(S)=\lambda A$ et $h_0(S)=\lambda(nA-H)$. Par la règle de dérivation d’un produit et $\lambda^2=1$,
$$
\begin{aligned}
F'(1)
&=(nA-H)^\top A+A^\top(nA-H)-H^\top A-A^\top H\\
&=2n A^\top A-2H^\top A-2A^\top H.
\end{aligned}
$$
En réintroduisant $A$ et $H$, cela donne
$$
\boxed{\begin{aligned}
F'(1)={}&2n\,p(S)^\top p(S)\\
&-2S^\top p'(S)^\top p(S)-2p(S)^\top p'(S)S.
\end{aligned}}
$$

### Question 25

> [!INDICATION]
> Évaluez la famille de matrices au seuil. Le quotient doit faire apparaître la dérivée de Q24.

> [!INDICATION]
> Développez $J(h)$ à l’aide de la formule pour $h_0$, en surveillant les termes quadratiques en $h$.

#### Solution

Puisque $p_0=\lambda p$ avec $\lambda^2=1$, on a $F(1)=0$. D’après les notations de Q24 et Q4,
$$
\begin{aligned}
J(h)&=(nA-H)^\top(nA-H)-H^\top H\\
&=n^2 A^\top A-n(H^\top A+A^\top H)\\
&=\frac n2 F'(1).
\end{aligned}
$$
La définition de la dérivée en $1$ donne alors
$$
\boxed{\frac{n}{2(r-1)}F(r)=J(h)+o(1)\qquad(r\to1).}
$$

### Question 26

> [!INDICATION]
> Utilisez la continuité des valeurs propres et le fait qu’aucune valeur propre de la matrice limite n’est nulle.

> [!INDICATION]
> Refaites la factorisation de Q13 pour $h=Xp'$ en prenant la racine zéro en premier. Comparez les coordonnées restantes avec celles construites pour $p'$ à une taille inférieure.

#### Solution

Par Q21, aucune valeur propre de $J(h)$ n’est nulle. La continuité admise des valeurs propres ordonnées et Q25 assurent que, pour $r<1$ assez proche de $1$, le nombre de valeurs propres positives ne change pas. Ainsi $\pi(J(h))=n-\sigma(p)$ par Q23.

Précisons la taille de $J$.

Notons $J_N(q)$ la matrice construite avec le décalage de taille $N$, pour un polynôme scindé $q$ de degré $d\le N$.

Si $d\ge1$, les preuves de Q11–Q13 s’appliquent avec $d$ facteurs et des colonnes de taille $N$.

Les polynômes intermédiaires $f_j$ sont de degré au plus $d-1$, donc chacun de ces vecteurs a ses $N-d$ dernières coordonnées nulles, par Q10.

Ses $d$ premières coordonnées reproduisent exactement le calcul de taille $d$.

En notant $\operatorname{Diag}$ aussi pour une diagonale par blocs, on obtient
$$
J_N(q)=\operatorname{Diag}(J_d(q),0_{N-d}).
$$
Pour $q$ constant non nul, son réciproque est lui-même et $J_N(q)=0$.

Si $n\ge2$, appliquons la factorisation Q13 à $h=Xp'$ en choisissant la racine nulle en premier.

Le télescopage de Q11 fonctionne dans n’importe quel ordre.

Le premier polynôme $f_1$ vaut $(p')_0$ et son coefficient dans $D$ vaut $1$.

La première coordonnée de la colonne correspondante $v=f_1(S^\top)U$ est le coefficient dominant non nul de $p'$.

Pour les autres colonnes, le facteur $X$ apparaît dans $f_j$ et les polynômes restants sont les $f_{j-1}$ de $p'$.

Par Q10, les colonnes sont donc nulles en première coordonnée et leur partie inférieure donne la factorisation de $J_{n-1}(p')$.

En notant $W=(v,e_2,\ldots,e_n)$, inversible par la première coordonnée de $v$, on obtient
$$
J(h)=W\operatorname{Diag}(1,J_{n-1}(p'))W^\top.
$$
Les questions 15–17 donnent $\pi(J(h))=1+\pi(J_{n-1}(p'))$.

Cette dernière valeur de $\pi$ vaut aussi $\pi(J_n(p'))$ par la stabilité de taille démontrée ci-dessus.

Si $n=1$, $p'$ est constant non nul et $J_1(h)$ est le carré de ce coefficient constant, donc positif.

La même relation sur $\pi$ vaut dans ce cas.

Finalement,
$$
\boxed{\sigma(p)=n-1-\pi(J(p')).}
$$

> [!METHODE]
> Un comptage par signe est localement constant près d’une matrice symétrique inversible lorsque les valeurs propres varient continûment. Le passage de $h$ à $p'$ est ensuite un calcul de congruence distinct.

## G — Méthode générale

Le PGCD recueille la partie des racines qui est commune au polynôme et à son réciproque. Les multiplicités deviennent ensuite un empilement de facteurs à racines simples.

### Question 27

> [!INDICATION]
> Pour une racine non nulle, comparez sa multiplicité à celle de son inverse avant et après division par le PGCD.

> [!INDICATION]
> Appliquez le critère à la taille du degré de $g$, puis justifiez un éventuel changement de taille.

#### Solution

Pour $\alpha\ne0$, notons $m(\alpha)$ sa multiplicité dans $p$, avec la valeur $0$ si ce n’est pas une racine.

Par la factorisation de Q1, sa multiplicité dans $p_0$ vaut $m(1/\alpha)$.

Dans le PGCD $f$, elle vaut le minimum des deux, et dans $g=p/f$, elle vaut donc
$$
\max\{m(\alpha)-m(1/\alpha),0\}.
$$
Cette quantité et celle obtenue pour $1/\alpha$ ne peuvent être toutes deux strictement positives.

Cela inclut $\alpha=\pm1$, dont la multiplicité dans $g$ est nulle.

Le polynôme $g$ est scindé puisqu’il divise $p$.

Pour $\deg g>0$, Q20 et Q18 à la taille $\deg g$ donnent $\sigma(g)=\pi(J_{\deg g}(g))$.

La stabilité de taille de Q26 permet de reprendre la taille $n$.

Si $g$ est constant, les deux nombres valent zéro. **Dans tous les cas, $\sigma(g)=\pi(J(g))$.**

### Question 28

> [!INDICATION]
> Regroupez les racines distinctes par seuils successifs sur leurs multiplicités.

> [!INDICATION]
> Additionnez les comptes obtenus grâce à Q26 et Q27. Remplacez la somme des degrés des facteurs par le degré du PGCD.

#### Solution

Le PGCD $f$ est unitaire et n’a pas de racine nulle puisque $p_0(0)\ne0$. Pour chaque $\alpha\ne0$, les multiplicités de $\alpha$ et de $1/\alpha$ dans $f$ coïncident par Q27.

Soit $\ell$ la plus grande multiplicité d’une racine de $f$, ou $0$ si $f=1$.

Pour $1\le j\le\ell$, définissons $g_j$ comme le produit des facteurs $X-\alpha$ sur les racines distinctes de $f$ dont la multiplicité est au moins $j$.

Chaque $g_j$ a des racines simples et leur ensemble est invariant par inversion.

Le facteur $X-\alpha$ apparaît dans exactement autant de $g_j$ que sa multiplicité dans $f$.

On a donc $f=\prod_{j=1}^\ell g_j$, avec produit vide égal à $1$.

Les nombres de racines dans $]-1,1[$ s’additionnent dans un produit, multiplicités comprises. Q26 s’applique à chacun des $g_j$ et Q27 à $g$. La somme des degrés des $g_j$ vaut $\deg f=n-\deg g$. Il vient
$$
\boxed{\sigma(p)=n-\deg g-\ell+\pi(J(g))-\sum_{j=1}^{\ell}\pi(J(g_j')).}
$$
Le terme $\pi(J(g))$, dupliqué dans la liste finale de l’énoncé, intervient une seule fois.

## Bilan

Pour un polynôme réciproque, suivez le degré réel et les racines nulles. Pour transformer une famille de polynômes en une famille de vecteurs, identifiez clairement l’application linéaire et l’espace de départ. La factorisation matricielle de cette épreuve rassemble ces deux opérations.

Retenez que la congruence préserve la dimension maximale d’un sous-espace où la forme est positive. Le théorème spectral relie cette dimension au nombre de valeurs propres strictement positives. Cette caractérisation explique aussi pourquoi l’ajout d’un bloc nul ne modifie pas le nombre cherché.

Quand un paramètre approche une valeur singulière, ramenez la famille à une limite inversible par un développement. Vérifiez le signe du facteur de renormalisation avant de comparer les inerties. Enfin, lorsque les racines ont des multiplicités, décomposer celles-ci en seuils successifs ramène le problème à des familles de racines simples.
