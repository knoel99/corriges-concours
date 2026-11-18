# Mines-Ponts MPI — Mathématiques 1 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve dure trois heures, sans calculatrice. Le problème montre que les normes d'ordre $p$ d'une somme de variables de Rademacher se comparent à sa norme d'ordre deux avec des constantes qui dépendent seulement de $p$. Une variable de Rademacher prend les valeurs $-1$ et $1$ avec la même probabilité.

- **Q1–Q3, Hölder.** Passer d’une inégalité sur des nombres à une inégalité entre espérances.
- **Q4–Q7, déviation.** Factoriser une espérance exponentielle, appliquer Markov puis optimiser la borne.
- **Q8–Q16, Khintchine.** Écrire un moment à l’aide des probabilités de queue et comparer les normes par interpolation.
- **Q17–Q19, première conséquence.** Montrer la conservation du produit scalaire et l’équivalence des normes sur les sommes finies.
- **Q20–Q21, deuxième conséquence.** Construire dans $\mathbb R^n$ un sous-espace où les normes d’ordre un et deux se comparent à l’échelle $\sqrt n$.

Q1–Q5, Q10 et Q17–Q18 reposent sur des méthodes de cours. Le passage de Q8 à Q11 puis l'interpolation de Q14–Q15 demandent plus de suivi des exposants. Pour les deux dernières questions, commencer par repérer comment une moyenne sur les signes devient une somme de coordonnées. Le passage à une famille infinie en Q18 est incompatible avec la finitude de l'espace probabilisé fixée au début du sujet. La solution précise le cadre dans lequel les preuves de Q18–Q19 s'appliquent.

Lire une indication puis reprendre la recherche avant d'ouvrir la suivante. Conserver les notations de somme et de norme mises en place pour le premier calcul de déviation afin de limiter les erreurs d'indices.

[Annales officielles, archive des sujets 2025](https://concoursminesponts.fr/annales/) · [Rapport, section 1.2 et annexe A](https://concoursminesponts.fr/wp-content/uploads/2025/10/Rapport-Ecrit-2025-VF.pdf) · [BO MP2I](https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm) · [BO MPI](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111756A.htm)

## Inégalité de Hölder

L'inégalité numérique se démontre sur les nombres positifs puis s'étend aux bords. Pour les espérances, la normalisation permet d'appliquer la même inégalité terme à terme.

### Question 1

> [!INDICATION]
> Pour des arguments strictement positifs, utiliser la concavité du logarithme sur deux puissances.

> [!INDICATION]
> Choisir les poids à partir des exposants conjugués. Examiner séparément le produit lorsque l'un des deux arguments est nul.

#### Solution

Si $x=0$ ou $y=0$, le produit est nul et le membre de droite est positif ou nul.

Supposons $x,y>0$.

Par concavité de $\ln$ et puisque les poids $1/p$ et $1/q$ sont positifs et somment à $1$,

$$
\begin{aligned}
\ln\left(\frac{x^p}{p}+\frac{y^q}{q}\right)
&\ge \frac1p\ln(x^p)+\frac1q\ln(y^q)\\
&=\ln(xy).
\end{aligned}
$$

L'exponentielle étant croissante, **$xy\le x^p/p+y^q/q$** dans tous les cas.

> [!JURY]
> Le rapport insiste sur le cas d'un argument nul. Le logarithme intervient uniquement après avoir écarté ce cas.

### Question 2

> [!INDICATION]
> Commencer par des puissances dont les espérances valent un.

> [!INDICATION]
> Ramener le cas général au cas normalisé par division. Avant de diviser, déterminer ce qu'implique l'annulation de l'une des deux espérances.

#### Solution

Si $\mathbb E(X^p)=0$ ou $\mathbb E(Y^q)=0$, la variable positive correspondante est nulle presque sûrement, donc $\mathbb E(XY)=0$.

Sinon, posons $A=\mathbb E(X^p)^{1/p}$ et $B=\mathbb E(Y^q)^{1/q}$.

On applique Q1 à $X/A$ et $Y/B$.

Par linéarité de l'espérance et définition de $A$ et $B$,

$$
\mathbb E\left(\frac{XY}{AB}\right)
\le \frac1p+\frac1q=1.
$$

En multipliant par $AB>0$, on obtient **$\mathbb E(XY)\le\mathbb E(X^p)^{1/p}\mathbb E(Y^q)^{1/q}$.**

> [!JURY]
> Le rapport demande de traiter séparément le cas où une espérance de puissance s'annule. Toute normalisation par une norme exige d'abord qu'elle soit non nulle.

### Question 3

> [!INDICATION]
> Pour une preuve directe, partir de l'espérance d'un carré faisant intervenir un paramètre réel.

> [!INDICATION]
> Distinguer le cas de degré deux du cas où le coefficient dominant s'annule. Dans le premier cas, utiliser le signe du discriminant.

#### Solution

On retrouve l'inégalité de Cauchy-Schwarz. Pour des variables réelles quelconques, prenons $P(t)=\mathbb E((X+tY)^2)$, qui est positif ou nul pour tout $t\in\mathbb R$. Si $\mathbb E(Y^2)=0$, alors $Y=0$ presque sûrement et l'inégalité est immédiate. Sinon, en développant,

$$
P(t)=\mathbb E(Y^2)t^2+2\mathbb E(XY)t+\mathbb E(X^2).
$$

Puisque ce trinôme est partout positif ou nul et de coefficient dominant strictement positif, son discriminant est négatif ou nul. Il en résulte

$$
\boxed{|\mathbb E(XY)|\le\mathbb E(X^2)^{1/2}\mathbb E(Y^2)^{1/2}.}
$$

> [!JURY]
> Le rapport attend une preuve directe et relève le cas où le coefficient de degré deux est nul. Un argument de discriminant s'applique après sa vérification.

## Une inégalité de déviation

On contrôle d'abord une espérance exponentielle grâce à l'indépendance. La dernière question choisit le paramètre de la borne en fonction du seuil.

### Question 4

> [!INDICATION]
> Comparer les coefficients de même degré dans les séries entières.

> [!INDICATION]
> Dans la factorielle, séparer les facteurs pairs des facteurs impairs.

#### Solution

Les développements en série entière, valables pour tout réel $t$, donnent

$$
\begin{aligned}
\operatorname{ch}(t)&=\sum_{j=0}^{+\infty}\frac{t^{2j}}{(2j)!},\\
e^{t^2/2}&=\sum_{j=0}^{+\infty}\frac{t^{2j}}{2^j j!}.
\end{aligned}
$$

Le produit des facteurs pairs de $(2j)!$ vaut $2^j j!$, et le produit des facteurs impairs est au moins $1$. Cette comparaison vaut aussi pour $j=0$, où les deux coefficients sont égaux. Comme chaque $t^{2j}$ est positif ou nul, **$\operatorname{ch}(t)\le e^{t^2/2}$**.

> [!METHODE]
> Pour comparer des séries à termes positifs, une comparaison coefficient par coefficient suffit une fois les variables et les puissances mises sous la même forme.

### Question 5

> [!INDICATION]
> Décomposer l'exponentielle de la somme comme un produit.

> [!INDICATION]
> Expliquer pourquoi les facteurs sont indépendants. Calculer l'espérance d'un facteur en utilisant les deux valeurs équiprobables.

#### Solution

On écrit $S=\sum_{i=1}^n c_i X_i$ et $\sigma^2=\sum_{i=1}^n c_i^2$. Les variables $e^{tc_i X_i}$ sont indépendantes, comme fonctions des variables indépendantes $X_i$. La loi de Rademacher donne $\mathbb E(e^{tc_i X_i})=\operatorname{ch}(tc_i)$. Par indépendance puis par Q4,

$$
\begin{aligned}
\mathbb E(e^{tS})
&=\prod_{i=1}^n\operatorname{ch}(tc_i)\\
&\le \boxed{e^{t^2\sigma^2/2}}.
\end{aligned}
$$

> [!JURY]
> Le rapport attend le passage de l'indépendance des variables initiales à celle des facteurs exponentiels. Cette justification précède la factorisation de l'espérance.

### Question 6

> [!INDICATION]
> Appliquer Markov à l'exponentielle de la valeur absolue.

> [!INDICATION]
> Majorer cette exponentielle avec celles de la somme et de son opposée. Utiliser Q5 pour chacune.

#### Solution

Pour $x\ge0$, on a $e^{x|S|}=\max(e^{xS},e^{-xS})\le e^{xS}+e^{-xS}$.

Q5 appliquée aux coefficients $c_i$ puis $-c_i$ donne $\mathbb E(e^{x|S|})\le2e^{x^2\sigma^2/2}$.

La variable $e^{x|S|}$ est positive et intégrable, et le seuil $e^{tx}$ est strictement positif.

Par Markov,

$$
\boxed{\mathbb P(e^{x|S|}>e^{tx})\le 2e^{-tx}e^{x^2\sigma^2/2}.}
$$

### Question 7

> [!INDICATION]
> Pour un paramètre strictement positif, transformer la comparaison entre exponentielles en une comparaison entre leurs exposants.

> [!INDICATION]
> Optimiser le trinôme de l'exposant de la majoration. Examiner séparément le seuil nul si le minimiseur se trouve sur le bord.

#### Solution

Comme le vecteur des coefficients est non nul, $\sigma^2>0$.

Si $t=0$, la borne vaut $2$ et s'applique immédiatement.

Pour $t>0$, choisissons $x=t/\sigma^2>0$, qui minimise le trinôme $-tx+x^2\sigma^2/2$.

Par stricte croissance de l'exponentielle et positivité de $x$, l'événement $\{e^{x|S|}>e^{tx}\}$ est exactement $\{|S|>t\}$.

Q6 donne

$$
\boxed{\mathbb P(|S|>t)\le2\exp\left(-\frac{t^2}{2\sigma^2}\right).}
$$

> [!JURY]
> Le rapport relève que la seule croissance ne justifie pas l'égalité des deux événements. Ici la stricte croissance de l'exponentielle est utilisée avec un paramètre strictement positif.

## Inégalités de Khintchine

La répartition d'une variable à valeurs finies donne une autre expression de ses moments. On s'en sert pour obtenir un contrôle commun, puis Hölder fournit la borne inférieure.

### Question 8

> [!INDICATION]
> Décomposer la probabilité en une somme portant sur les valeurs possibles de la variable.

> [!INDICATION]
> Écrire chaque condition $x_j>t$ à l'aide d'une indicatrice. Vérifier la régularité et le comportement près des deux bornes avant d'intégrer.

#### Solution

Soient $x_1,\ldots,x_m$ les valeurs de $X$, toutes positives ou nulles, et $w_j=\mathbb P(X=x_j)$.

Pour $t\ge0$, $F_X(t)=\sum_{j=1}^m w_j\mathbf 1_{[0,x_j[}(t)$.

Le produit avec $t^{p-1}$ est continu par morceaux et nul au-delà de la plus grande valeur de $X$.

Il est aussi borné près de zéro puisque $p\ge1$.

L'intégrale converge et, par linéarité appliquée à une somme finie,

$$
\begin{aligned}
p\int_0^{+\infty} t^{p-1}F_X(t)\,dt
&=\sum_{j=1}^m w_j p\int_0^{x_j} t^{p-1}\,dt\\
&=\sum_{j=1}^m w_j x_j^p\\
&=\boxed{\mathbb E(X^p)}.
\end{aligned}
$$

> [!JURY]
> Le rapport distingue une fonction continue d'une fonction en escalier continue par morceaux. Le caractère fini des valeurs rend aussi l'intégrande nulle au-delà d'un seuil.

### Question 9

> [!INDICATION]
> Essayer le changement de variable qui simplifie l'exponentielle. Le faire d'abord jusqu'à une borne finie.

> [!INDICATION]
> Employer la formule du moment avec la valeur absolue de la somme, puis la borne de Q7.

#### Solution

La fonction intégrée est continue sur $\mathbb R_+$. Entre $0$ et une borne finie, le changement de variable $u=t^2/2$ donne $t^3\,dt=2u\,du$. La primitive $-(u+1)e^{-u}$ de $ue^{-u}$ a une limite nulle à l'infini. Ainsi l'intégrale converge et

$$
\int_0^{+\infty} t^3e^{-t^2/2}\,dt
=2\int_0^{+\infty}ue^{-u}\,du=2.
$$

Si $\sigma^2=1$, on applique Q8 à $|S|$ avec $p=4$ et on majore sa probabilité de queue par Q7. On obtient

$$
\boxed{\mathbb E(S^4)\le 8\int_0^{+\infty} t^3e^{-t^2/2}\,dt=16.}
$$

> [!METHODE]
> La même formule de queue s'applique à une variable de signe quelconque après passage à sa valeur absolue. Pour un moment pair, on retrouve alors la puissance initiale.

### Question 10

> [!INDICATION]
> Développer le carré. Pour chaque produit mixte, exprimer son espérance à l'aide de l'indépendance.

> [!INDICATION]
> Calculer les deux premiers moments d'une variable de Rademacher à partir de sa définition.

#### Solution

Chaque variable $X_i$ a une espérance nulle, car elle vaut $1$ et $-1$ avec la même probabilité. Son carré est identiquement égal à $1$. Pour $i\ne j$, l'indépendance donne $\mathbb E(X_iX_j)=0$. En développant le carré, puis en prenant l'espérance,

$$
\begin{aligned}
\mathbb E(S^2)
&=\sum_{i=1}^n c_i^2\mathbb E(X_i^2)
 +2\sum_{1\le i<j\le n}c_i c_j\mathbb E(X_iX_j)\\
&=\boxed{\sum_{i=1}^n c_i^2}.
\end{aligned}
$$

### Question 11

> [!INDICATION]
> Ramener la somme à une variable d'échelle fixée en utilisant la somme des carrés des coefficients.

> [!INDICATION]
> Reprendre l'argument de Q9 pour un moment général. Examiner l'intégrabilité du majorant à zéro et à l'infini.

#### Solution

Si $\sigma=0$, tous les coefficients sont nuls et l'inégalité est immédiate. Sinon, $Z=|S|/\sigma$ est une variable positive à valeurs finies. Q8 et Q7 donnent

$$
\mathbb E(Z^p)\le 2p\int_0^{+\infty}t^{p-1} e^{-t^2/2}\,dt.
$$

L'intégrande est continue sur $]0,+\infty[$ et bornée au voisinage de zéro. À l'infini, elle est $O(t^{-2})$ par croissance comparée. L'intégrale est donc finie et strictement positive. En prenant sa valeur multipliée par $2p$ à la puissance $1/p$ pour $\beta_p$, puis en réutilisant Q10,

$$
\boxed{\|S\|_p\le\beta_p\|S\|_2.}
$$

> [!METHODE]
> Le terme constant obtenu pour une somme normalisée doit être indépendant du nombre de coefficients. La formule avec l'intégrale de queue rend cette indépendance visible.

### Question 12

> [!INDICATION]
> Au-delà de l'égalité pour $p=2$, appliquer Hölder à un produit dont un facteur vaut constamment un.

> [!INDICATION]
> Choisir le premier exposant pour que la puissance de la somme à l'intérieur de l'espérance devienne $p$.

#### Solution

Pour $p=2$, on a l'égalité.

Pour $p>2$, Q2 appliquée à $|S|^2$ et à la constante $1$ avec les exposants conjugués $p/2$ et $p/(p-2)$ donne $\mathbb E(|S|^2)\le\mathbb E(|S|^p)^{2/p}$.

Ainsi **$\|S\|_2\le\|S\|_p$**.

### Question 13

> [!INDICATION]
> Placer les trois inverses sur une droite réelle. Une moyenne pondérée à deux coefficients doit produire celui du milieu.

> [!INDICATION]
> On peut isoler le coefficient dans l'équation, puis vérifier ses deux bornes.

#### Solution

Pour $1\le p<2$, on a $1/4<1/2<1/p$.

Il existe donc un unique coefficient $\theta\in]0,1[$ tel que $1/2=\theta/p+(1-\theta)/4$.

En isolant $\theta$, on trouve **$\theta=p/(4-p)$**, effectivement strictement compris entre $0$ et $1$.

### Question 14

> [!INDICATION]
> Écrire le carré de la valeur absolue comme un produit de deux puissances. Appliquer Hölder.

> [!INDICATION]
> Les puissances choisies ont pour somme deux. Par Q13, leurs quotients par les exposants des moments voulus somment à un.

#### Solution

On écrit $|S|^2=|S|^{2\theta}|S|^{2(1-\theta)}$. Les nombres $r=p/(2\theta)$ et $s=4/(2(1-\theta))$ sont conjugués, car $2\theta/p+2(1-\theta)/4=1$ par Q13. Leurs inverses sont strictement positifs, donc chacun est strictement supérieur à $1$. Q2 donne

$$
\boxed{\mathbb E(S^2)
\le\mathbb E(|S|^p)^{2\theta/p}\mathbb E(S^4)^{(1-\theta)/2}.}
$$

> [!PIEGE]
> Ne pas appeler indistinctement $p$ et $4$ les exposants de Hölder. Ces nombres sont les ordres des moments recherchés. Les exposants conjugués dépendent aussi des puissances des deux facteurs.

### Question 15

> [!INDICATION]
> Ramener Q9 au cas général par homothétie des coefficients, puis utiliser Q10.

> [!INDICATION]
> Prendre la racine carrée dans Q14. Lorsque la norme d'ordre deux est non nulle, rassembler ses facteurs d'un même côté avant d'isoler la norme d'ordre $p$.

#### Solution

Si $\sigma=0$, l'inégalité est immédiate. Sinon, Q9 appliquée aux coefficients $c_i/\sigma$ donne $\mathbb E(S^4)\le16\sigma^4$, donc $\|S\|_4\le2\sigma$. Par Q10, $\sigma=\|S\|_2$. En prenant la racine carrée dans Q14,

$$
\|S\|_2\le\|S\|_p^\theta\,(2\|S\|_2)^{1-\theta}.
$$

On divise par $\|S\|_2^{1-\theta}>0$, puis on élève à la puissance $1/\theta$. On obtient **$\widetilde\alpha_p\|S\|_2\le\|S\|_p$** avec $\widetilde\alpha_p=2^{-(1-\theta)/\theta}>0$.

### Question 16

> [!INDICATION]
> Comparer les domaines d'application de Q12 et Q15. Vérifier que la constante ne dépend pas des coefficients.

#### Solution

Pour $p\ge2$, Q12 donne l'inégalité avec $\alpha_p=1$. Pour $1\le p<2$, Q15 donne l'inégalité avec $\alpha_p=\widetilde\alpha_p$. **Dans tous les cas, $\alpha_p>0$ peut être choisie indépendamment des coefficients et du nombre de termes.**

## Une première conséquence

Les produits de deux variables de la famille s'annulent en moyenne lorsqu'elles sont distinctes. Cette propriété permet de relier les coefficients d'une somme à la norme d'ordre deux de la variable.

### Question 17

> [!INDICATION]
> Vérifier les propriétés usuelles d'un produit scalaire dans l'ordre. Identifier le sens de l'annulation de l'espérance d'un carré.

#### Solution

La linéarité de l'espérance et la commutativité du produit donnent la bilinéarité et la symétrie de $\varphi$. En outre, $\varphi(X,X)=\mathbb E(X^2)\ge0$. Si cette quantité est nulle, $X^2$ est nulle presque sûrement, donc $X=0$ selon l'identification de l'énoncé. L'espérance est inchangée si l'on modifie une variable sur un événement de probabilité nulle. **$\varphi$ est donc un produit scalaire.**

> [!JURY]
> Le rapport relève des justifications trop rapides du caractère défini positif. La conclusion est une égalité presque sûre, interprétée conformément à l'identification du sujet.

### Question 18

> [!INDICATION]
> Développer l'espérance du produit de deux sommes à support fini. Distinguer les indices égaux et distincts.

> [!INDICATION]
> Pour examiner la compatibilité des hypothèses, demander combien de configurations différentes les $m$ premières variables peuvent réaliser avec une probabilité positive.

#### Solution

L'hypothèse d'une suite infinie indépendante est incompatible avec la finitude de $\Omega$.

Pour tout $m$, les $2^m$ configurations de signes des $m$ premières variables auraient chacune probabilité $2^{-m}$ et correspondraient donc à $2^m$ événements non vides et disjoints.

C'est impossible lorsque $2^m>|\Omega|$.

Le programme de mathématiques de MPI admet l’existence d'un espace probabilisé portant une suite de variables indépendantes de lois discrètes données. On peut donc prendre un tel espace portant une suite de variables de Rademacher, et choisir comme espace d'arrivée les variables à valeurs finies modulo égalité presque sûre. L’identité démontrée ci-dessous vaut également sur l'espace fini initial pour toute famille indépendante finie, en restreignant les suites aux indices de cette famille. Dans les deux cadres, la preuve de Q17 s’applique sur l’espace d’arrivée.

Pour toute suite $u$ à support fini, $\psi(u)=\sum_i u_iX_i$ est une somme finie de variables à valeurs finies.

Elle est donc à valeurs finies.

Si $u,v$ sont à support fini, on développe le produit et on prend l'espérance.

Comme dans Q10, $\mathbb E(X_iX_j)$ vaut $0$ si $i\ne j$ et $1$ si $i=j$.

Par conséquent,

$$
\begin{aligned}
\varphi(\psi(u),\psi(v))
&=\sum_{i,j\ge0}u_iv_j\mathbb E(X_iX_j)\\
&=\sum_{i\ge0}u_iv_i\\
&=\boxed{\langle u,v\rangle}.
\end{aligned}
$$

> [!METHODE]
> L'orthogonalité se lit dans les espérances des produits distincts. Le calcul n'utilise que les variables associées aux supports finis des coefficients.

### Question 19

> [!INDICATION]
> Comparer chacune des deux normes à la norme d'ordre deux par Q11 et Q16.

> [!INDICATION]
> Pour une majoration dans un sens, prendre la borne supérieure pour la norme de gauche et la borne inférieure pour celle de droite.

#### Solution

On reprend le cadre cohérent de Q18. Tout $X\in R$ est une combinaison finie de variables de Rademacher indépendantes. Les preuves de Q11 et Q16 ne dépendent que de la loi conjointe de la famille finie concernée, qui est la loi uniforme sur le cube des signes. Elles donnent, pour $r=p$ puis $r=q$,

$$
\alpha_r\|X\|_2\le\|X\|_r\le\beta_r\|X\|_2.
$$

Les constantes ne dépendent pas du support des coefficients. Ainsi,

$$
\boxed{
\frac{\alpha_q}{\beta_p}\|X\|_p\le\|X\|_q
\le\frac{\beta_q}{\alpha_p}\|X\|_p.}
$$

**Les deux normes sont donc équivalentes sur $R$.**

## Une deuxième conséquence

Les configurations de signes deviennent les indices des coordonnées d'un vecteur. C'est cette réindexation qui fait le lien entre la probabilité sur le cube et les normes usuelles de $\mathbb R^n$.

### Question 20

> [!INDICATION]
> Équiper l'ensemble des configurations de signes d'une probabilité uniforme et définir les variables coordonnées.

> [!INDICATION]
> Vérifier leur indépendance en calculant les probabilités des vecteurs de signes. Faire apparaître la somme demandée en écrivant une espérance.

#### Solution

Sur $\{-1,1\}^k$ muni de la probabilité uniforme, les fonctions coordonnées $\varepsilon_i$ sont des variables de Rademacher indépendantes.

En effet, chaque vecteur de signes a une probabilité $2^{-k}$, produit des $k$ probabilités marginales $1/2$.

Posons $S_a=\sum_{i=1}^k a_i\varepsilon_i$.

Comme $n=2^k$, on a

$$
\mathbb E(|S_a|)
=\frac1n\sum_{\varepsilon\in\{-1,1\}^k}
\left|\sum_{i=1}^k a_i\varepsilon_i\right|.
$$

Par Q10, $\|S_a\|_2=\|a\|_2^{\mathbb R^k}$. On applique Q11 et Q16 avec $p=1$, puis on multiplie par $n$. On obtient

$$
\boxed{\begin{aligned}
\alpha_1 n\|a\|_2^{\mathbb R^k}&\\
&\le \sum_{\varepsilon\in\{-1,1\}^k}\left|\sum_{i=1}^k a_i\varepsilon_i\right|\\
&\le \beta_1 n\|a\|_2^{\mathbb R^k}.\end{aligned}}
$$

> [!METHODE]
> Le facteur $n$ apparaît lorsqu'on passe d'une espérance sur $n$ issues équiprobables à une somme brute.

### Question 21

> [!INDICATION]
> Chercher l'image de l'application proposée et établir sa dimension en étudiant le noyau.

> [!INDICATION]
> Calculer la norme euclidienne au carré de l'image par la même probabilité uniforme qu'en Q20. Relier ensuite sa norme d'ordre un à la somme de Q20.

#### Solution

L'application $T$ de l'énoncé est linéaire, chaque coordonnée étant une forme linéaire des coefficients $a_i$. Avec le même espace uniforme qu'en Q20, Q10 donne

$$
\begin{aligned}
\bigl(\|Ta\|_2^{\mathbb R^n}\bigr)^2
&=\sum_{\varepsilon\in\{-1,1\}^k}
   \left(\sum_{i=1}^k a_i\varepsilon_i\right)^2\\
&=n\mathbb E(S_a^2)\\
&=n\bigl(\|a\|_2^{\mathbb R^k}\bigr)^2.
\end{aligned}
$$

Ainsi $Ta=0$ entraîne $a=0$.

Le sous-espace $F=\operatorname{Im}(T)$ est donc de dimension $k$ par le théorème du rang.

Pour $x=Ta\in F$, on a $\|x\|_2^{\mathbb R^n}=\sqrt n\,\|a\|_2^{\mathbb R^k}$ et la somme de Q20 est $\|x\|_1^{\mathbb R^n}$.

On obtient

$$
\boxed{\begin{aligned}
\alpha_1\sqrt n\,\|x\|_2^{\mathbb R^n}&\\
&\le\|x\|_1^{\mathbb R^n}\\
&\le\beta_1\sqrt n\,\|x\|_2^{\mathbb R^n}\qquad(x\in F).\end{aligned}}
$$

> [!PIEGE]
> L'injectivité de $T$ permet de conclure que son rang vaut $k$ par le théorème du rang. Le passage du carré de la norme à la norme explique le facteur $\sqrt n$.

## Bilan

- Pour appliquer une inégalité après normalisation, isoler les variables de norme nulle avant toute division.
- Pour obtenir une borne de déviation, factoriser l'espérance grâce à l'indépendance, appliquer Markov à une quantité positive et choisir le paramètre en dernier.
- Pour déterminer un moment par une intégrale de queue sur un espace à valeurs finies, décomposer d'abord la probabilité selon les valeurs possibles.
- Pour interpoler des normes, calculer les exposants conjugués à partir des puissances de la factorisation et des moments voulus.
- Pour réutiliser une inégalité probabiliste sur tous les vecteurs de signes, munir le cube de la loi uniforme. Les facteurs $n$ et $\sqrt n$ suivent de la conversion entre somme, moyenne et norme euclidienne.
