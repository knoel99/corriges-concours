# Mines-Ponts PC — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve de trois heures sans calculatrice étudie des séries alternées dont les dénominateurs suivent une progression arithmétique. Les préliminaires et la première partie établissent une représentation intégrale. La deuxième partie s’en sert pour calculer des sommes exactes, dont certaines par décomposition en éléments simples. La troisième partie compte les couples de paramètres couverts par les formules. La dernière mesure la décroissance de l’erreur des sommes partielles.

Le dénombrement de la troisième partie est accessible indépendamment des calculs complexes. Pour préparer la dernière partie, conserver l’expression du reste obtenue en Q7.

## Préliminaires

La série harmonique alternée sert de point de départ et permet de traiter la famille où le pas vaut 1.

### Question 1

> [!INDICATION]
> Vérifier le signe, la décroissance et la limite du module du terme général.

#### Solution

Pour $p,q\ge1$, la suite $1/(pk+q)$ est positive, décroissante et tend vers zéro. Le critère des séries alternées donne la convergence de $\sum_k(-1)^k/(pk+q)$.

### Question 2

> [!INDICATION]
> Écrire chaque inverse entier comme une intégrale de monôme. Sommer avant d’intégrer.

#### Solution

On a $1/(k+1)=\int_0^1t^k\,\mathrm dt$. En intégrant la somme géométrique finie de raison $-t$, on obtient

$$
\phi_{1,1}(n)=\int_0^1\frac{\mathrm dt}{1+t}-\int_0^1\frac{(-t)^{n+1}}{1+t}\,\mathrm dt.
$$

### Question 3

> [!INDICATION]
> Majorer le reste en remplaçant son dénominateur par 1.

> [!JURY]
> Le rapport privilégie une majoration directe du reste. Elle donne ici une borne explicite sans théorème de passage à la limite sous l’intégrale.

#### Solution

La seconde intégrale de Q2 est majorée en valeur absolue par $\int_0^1t^{n+1}\,\mathrm dt=1/(n+2)$. Elle tend donc vers zéro, tandis que la première intégrale vaut $\ln 2$.

$$
\boxed{S_{1,1}=\ln 2.}
$$

### Question 4

> [!INDICATION]
> Identifier la première valeur de l’indice dans le reste, puis repartir d’un indice nul.

#### Solution

La différence entre $S_{1,1}$ et $\phi_{1,1}(q-2)$ est le reste d’indice initial $q-1$. Avec $k=j+q-1$, son terme est $(-1)^{q-1}(-1)^j/(j+q)$. Ce décalage peut se faire sur des sommes finies, puis passer à la limite par Q1. Ainsi

$$
\boxed{S_{1,q}=(-1)^q\bigl(\phi_{1,1}(q-2)-\ln 2\bigr).}
$$

## Partie 1 — Expression de la somme sous la forme d’une intégrale

On généralise le calcul de Q2 avec une somme finie et une intégrale à paramètre.

### Question 5

> [!INDICATION]
> Vérifier la continuité dans chacune des variables séparément. Une constante intégrable permet de dominer les fonctions.

#### Solution

Écrivons $a=\alpha_{p,q}=p/q>0$. Pour chaque $t\ge0$, la fonction intégrée est continue sur $[0,1]$, avec valeur nulle en zéro.

Pour chaque $x\in[0,1]$, elle dépend continûment de $t$. Sa valeur absolue est au plus 1 sur tout le domaine, et la fonction constante 1 est intégrable sur $[0,1]$. Le théorème de continuité des intégrales à paramètre donne la continuité de $I_{p,q}$ sur $\mathbb R_+$.

### Question 6

> [!INDICATION]
> Remplacer le dénominateur par 1 pour obtenir une puissance dont la primitive est immédiate.

> [!METHODE]
> Comme en Q3, intégrer une puissance fournit en une ligne un majorant qui tend vers zéro.

#### Solution

On a l’encadrement

$$
\begin{aligned}
0\le I_{p,q}(n)&\le\int_0^1x^{(n+1)a}\,\mathrm dx,\\
\int_0^1x^{(n+1)a}\,\mathrm dx&=\frac1{1+(n+1)a}.
\end{aligned}
$$

Comme $a>0$, on en déduit $I_{p,q}(n)\to0$.

### Question 7

> [!INDICATION]
> Le dénominateur de la somme géométrique est toujours strictement positif. Intégrer la somme finie et calculer les intégrales des monômes généralisés.

#### Solution

Pour $x\in[0,1]$, la somme géométrique vaut

$$
\sum_{k=0}^n(-x^a)^k=\frac{1+(-1)^nx^{(n+1)a}}{1+x^a}.
$$

Pour tout $k\ge0$, $\int_0^1 x^{ka}\,\mathrm dx=1/(ka+1)=q/(pk+q)$. En intégrant la somme finie puis en divisant par $q$, on obtient

$$
\boxed{\phi_{p,q}(n)=\frac1q\left(\int_0^1\frac{\mathrm dx}{1+x^a}+(-1)^n I_{p,q}(n)\right).}
$$

### Question 8

> [!INDICATION]
> Passer à la limite avec Q6, puis choisir une substitution qui transforme la puissance fractionnaire en puissance entière.

#### Solution

Par Q6 et Q7, $S_{p,q}=q^{-1}\int_0^1(1+x^{p/q})^{-1}\,\mathrm dx$. Avec $x=t^q$ et $\mathrm dx=q t^{q-1}\,\mathrm dt$, il vient

$$
\boxed{S_{p,q}=\int_0^1\frac{t^{q-1}}{1+t^p}\,\mathrm dt.}
$$

## Partie 2 — Calcul explicite dans trois cas

Deux cas reviennent à la série harmonique alternée. Le cas restant utilise les pôles de la fraction rationnelle et leurs conjugués.

### Question 9

> [!INDICATION]
> Si les paramètres sont égaux, la puissance du numérateur fait apparaître la dérivée de la variable à substituer.

#### Solution

Si $p=q$, on pose $u=t^p$ dans Q8. L’intégrale vaut alors $p^{-1}\int_0^1(1+u)^{-1}\,\mathrm du$, d’où **$S_{p,p}=\ln(2)/p$**.

### Question 10

> [!INDICATION]
> Extraire le diviseur commun du dénominateur et reconnaître la situation de Q4.

#### Solution

Écrivons $q=p\lambda$, où $\lambda=q/p$ est un entier au moins égal à 2. La factorisation de $p$ dans $pk+q$ donne $S_{p,q}=S_{1,\lambda}/p$. D’après Q4 et le réindexage $k=j+1$ de la somme partielle,

$$
\boxed{S_{p,q}=\frac{(-1)^{\lambda-1}}p
\left(\ln 2-\sum_{k=1}^{\lambda-1}\frac{(-1)^{k-1}}k\right).}
$$

### Question 11

> [!INDICATION]
> Déterminer les arguments des racines du dénominateur et vérifier qu’elles sont simples. La conjugaison permet de réunir les pôles par paires.

> [!PIEGE]
> Pour p impair, isoler la racine réelle avant de compter les paires conjuguées.

#### Solution

Les racines de $1+X^p$ sont les $e^{i(2j+1)\pi/p}$, pour $0\le j<p$. Elles sont simples, car aucune ne s’annule et la dérivée du dénominateur est $pX^{p-1}$. Si $p$ est impair, $-1$ est la seule racine réelle. Les autres se regroupent en couples conjugués.

On choisit $\omega_{p,k}=e^{i\theta_k}$ avec $\theta_k=(2k+1)\pi/p$ et $0\le k<\lfloor p/2\rfloor$. Ce sont les racines de partie imaginaire strictement positive.

Pour justifier la décomposition, notons $D=1+X^p$. Les $p$ polynômes $D/(X-w)$, où $w$ parcourt les pôles, sont de degré $p-1$.

En évaluant une combinaison linéaire en chaque pôle, on voit qu’ils sont indépendants, puisque seul le polynôme correspondant prend une valeur non nulle. Ils forment une base des polynômes de degré au plus $p-1$, espace contenant le numérateur. On divise la décomposition du numérateur dans cette base par $D$.

L’unicité et la réalité des coefficients de $F$ donnent des coefficients conjugués aux pôles conjugués. Ainsi

$$
F(X)=\frac{1-(-1)^p}{2}\frac{a_0}{X+1}
+\sum_{k=0}^{\lfloor p/2\rfloor-1}\left(\frac{b_k}{X-\omega_{p,k}}+\frac{\overline{b_k}}{X-\overline{\omega_{p,k}}}\right),
$$

avec $a_0=0$ par convention si $p$ est pair.

### Question 12

> [!INDICATION]
> Pour un pôle simple, multiplier par le facteur correspondant et évaluer en ce pôle après simplification.

#### Solution

Au pôle simple $w$, le coefficient de $1/(X-w)$ est la limite de $(X-w)F(X)$ en $w$. Le dénominateur divisé par $X-w$ a pour valeur $p w^{p-1}$ au pôle. Ainsi

$$
\frac{w^{q-1}}{p w^{p-1}}=\frac{w^{q-p}}p=-\frac{w^q}p,
$$

car $w^p=-1$. On obtient donc $b_k=-e^{iq\theta_k}/p$, et, si $p$ est impair, $a_0=(-1)^{q-1}/p$.

### Question 13

> [!INDICATION]
> Réunir deux fractions conjuguées sur un dénominateur réel et reconnaître les cosinus au numérateur.

#### Solution

Pour $w=e^{i\theta_k}$, la mise au même dénominateur donne

$$
\frac{w^q}{X-w}+\frac{\overline w^{\,q}}{X-\overline w}
=\frac{2\cos(q\theta_k)X-2\cos((q-1)\theta_k)}{X^2-2\cos(\theta_k)X+1}.
$$

En multipliant par $-1/p$ et en réintroduisant l’éventuel pôle réel,

$$
\boxed{
F(X)=\frac{1-(-1)^p}{2}\frac{(-1)^{q-1}}{p(X+1)}
-\frac2p\sum_{k=0}^{\lfloor p/2\rfloor-1}F_k(X).
}
$$

### Question 14

> [!INDICATION]
> Sommer les puissances de toutes les racines par une progression géométrique. Ensuite, séparer l’éventuel terme réel des paires conjuguées.

#### Solution

La somme des puissances $q$ des $p$ racines de $X^p+1$ est nulle.

En effet, c’est $e^{iq\pi/p}$ multiplié par la somme géométrique de raison $e^{2i\pi q/p}$ sur $p$ termes, et $0<q<p$ exclut une raison égale à 1.

Chaque couple conjugué contribue $2\cos(q\theta_k)$. Pour $p$ impair, le pôle réel contribue $(-1)^q$, donc

$$
\boxed{\sum_{k=0}^{\lfloor p/2\rfloor-1}\cos(q\theta_k)
=\begin{cases}0&\text{si }p\text{ est pair},\\
(-1)^{q+1}/2&\text{si }p\text{ est impair}.
\end{cases}}
$$

### Question 15

> [!INDICATION]
> Insérer la formule d’intégration donnée pour chaque terme. Rassembler tous les multiples de ln 2 avant de simplifier.

#### Solution

Par Q8, on intègre la décomposition de Q13 sur $[0,1]$ et on insère la formule admise pour chaque $F_k$. Comme $\sin(\theta_k/2)>0$, on sépare $\ln(2\sin(\theta_k/2))$ en $\ln 2+\ln\sin(\theta_k/2)$. Le coefficient total de $\ln 2$ est

$$
\frac{1-(-1)^p}{2p}(-1)^{q-1}
-\frac2p\sum_{k=0}^{\lfloor p/2\rfloor-1}\cos(q\theta_k).
$$

Il est nul par Q14, dans les deux cas de parité. On obtient

$$
\boxed{
\begin{aligned}
S_{p,q}={}&\frac{\pi}{p^2}\sum_{k=0}^{\lfloor p/2\rfloor-1}(p-1-2k)\sin(q\theta_k)\\
&-\frac2p\sum_{k=0}^{\lfloor p/2\rfloor-1}\cos(q\theta_k)\ln\sin(\theta_k/2).
\end{aligned}}
$$

### Question 16

> [!INDICATION]
> Dans chacun des deux cas, un seul indice contribue. Calculer son angle et les trois fonctions trigonométriques utilisées.

#### Solution

Pour $p=2$ et $q=1$, le seul angle est $\pi/2$. Le terme en cosinus est nul, donc **$S_{2,1}=\pi/4$**.

Pour $p=3$ et $q=1$, le seul angle est $\pi/3$. Son sinus vaut $\sqrt3/2$, son cosinus et le sinus du demi-angle valent $1/2$. Q15 donne

$$
\boxed{S_{3,1}=\frac{\pi\sqrt3}{9}+\frac{\ln 2}{3}.}
$$

## Partie 3 — Quelques calculs de probabilités

Le nombre de couples admissibles se déduit de la diagonale et d’un comptage des multiples.

### Question 17

> [!INDICATION]
> Traduire les trois conditions sur les paramètres par des comparaisons strictes ou une égalité, puis décrire leur union.

#### Solution

Sur l’univers des couples ordonnés, on a $E_n=A_n\cup B_n\cup C_n$ par les définitions de $E_1,E_2,E_3$. Les trois événements sont deux à deux disjoints, car ils imposent respectivement $p=q$, $p<q$ et $p>q$.

Si $n\ge2$, ils contiennent respectivement les couples $(1,1)$, $(1,2)$ et $(2,1)$.

Au rang $n=1$, $B_1$ et $C_1$ sont vides et la partition au sens strict se réduit à $\{A_1\}$. L’union disjointe reste valable pour tout $n$.

### Question 18

> [!INDICATION]
> Compter les couples sur la diagonale. Pour les autres, utiliser l’échange des deux coordonnées.

#### Solution

Les $n^2$ couples ordonnés sont équiprobables. Il y a $n$ couples diagonaux. Les $n(n-1)$ couples hors diagonale se répartissent également entre $p>q$ et $q>p$ par échange des coordonnées. Ainsi

$$
\boxed{\begin{aligned}
\mathbb P(A_n)&=1/n,\\
\mathbb P(C_n)&=(n-1)/(2n).
\end{aligned}}
$$

### Question 19

> [!INDICATION]
> Pour un premier tirage fixé, compter ses multiples autorisés au second tirage, en retirant le cas d’égalité.

#### Solution

À $p$ fixé, les multiples de $p$ dans $[1,n]$ sont $p,2p,\ldots,\lfloor n/p\rfloor p$. On écarte le premier. En sommant puis en divisant par le nombre total de couples, et en utilisant l’incompatibilité de $A_n$ et $B_n$, on obtient

$$
\boxed{\begin{aligned}
\mathbb P(B_n)&=\frac1{n^2}\sum_{p=1}^n\left\lfloor\frac np\right\rfloor-\frac1n,\\
\mathbb P(A_n\cup B_n)&=\frac1{n^2}\sum_{p=1}^n\left\lfloor\frac np\right\rfloor.
\end{aligned}}
$$

### Question 20

> [!INDICATION]
> Comparer chaque terme à l’intégrale de la fonction inverse sur un intervalle de longueur un, à gauche ou à droite.

> [!JURY]
> Le rapport demande de dérouler la comparaison somme–intégrale en justifiant les sens des inégalités par la décroissance.

#### Solution

Par décroissance de $x\mapsto1/x$, on minore chaque $1/k$ par l’intégrale sur $[k,k+1]$. Pour $k\ge2$, on le majore par l’intégrale sur $[k-1,k]$. En sommant, on obtient

$$
\ln(n+1)\le H_n\le 1+\ln n.
$$

En divisant par $\ln n$ pour $n\ge2$, les deux bornes tendent vers 1. En particulier $\ln(n+1)=\ln n+\ln(1+1/n)$. Ainsi **$H_n\sim\ln n$**.

### Question 21

> [!INDICATION]
> Encadrer chaque partie entière entre son argument diminué de 1 et son argument. Sommer les erreurs avant de passer à la limite.

> [!PIEGE]
> Un équivalent valable pour p fixé ne permet pas à lui seul de sommer sur p jusqu’à n. L’erreur uniforme d’au plus une unité par terme résout cette difficulté.

#### Solution

On utilise l’encadrement $n/p-1\le\lfloor n/p\rfloor\le n/p$ uniformément pour $1\le p\le n$. Avec Q19,

$$
\frac{H_n-1}{n}\le\mathbb P(A_n\cup B_n)\le\frac{H_n}{n}.
$$

Comme $H_n\to+\infty$, les deux bornes sont équivalentes à $(\ln n)/n$ par Q20. **La probabilité demandée est donc équivalente à $(\ln n)/n$.**

### Question 22

> [!INDICATION]
> Ajouter les deux contributions disjointes correspondant à la diagonale avec divisibilité et à l’ordre strict restant.

#### Solution

L’union de Q17 est disjointe. La contribution de $C_n$ tend vers $1/2$ par Q18. Celle de $A_n\cup B_n$ tend vers zéro par Q21, puisque $(\ln n)/n\to0$. **Ainsi $\mathbb P(E_n)\to1/2$.**

## Partie 4 — Vitesse de convergence

On part de l’erreur exacte de Q7 pour obtenir un équivalent puis un quotient d’erreurs.

### Question 23

> [!INDICATION]
> Après le changement de variables demandé, mettre le facteur dépendant de n hors de l’intégrale. Chercher un majorant intégrable qui reste valable même si p est inférieur à q.

#### Solution

Dans $R_{p,q}(n)=I_{p,q}(n)/q$, posons $s=x^{n+1}$. En gardant $a=p/q$, on obtient

$$
R_{p,q}(n)=\frac1{q(n+1)}\int_0^1\frac{s^{a-1+1/(n+1)}}{1+s^{a/(n+1)}}\,\mathrm ds.
$$

Pour chaque $s\in]0,1]$, l’intégrande tend vers $s^{a-1}/2$. Il est positif et majoré sur $]0,1]$ par $s^{a-1}$, intégrable puisque $a>0$.

Le théorème de convergence dominée donne une intégrale limite égale à $1/(2a)$. Comme $qa=p$ et $n+1\sim n$,

$$
\boxed{R_{p,q}(n)\sim\frac1{2pn}.}
$$

### Question 24

> [!INDICATION]
> Exprimer l’erreur exacte en fonction de R. Vérifier qu’elle n’est jamais nulle avant de former le quotient.

> [!METHODE]
> La limite du quotient s’obtient à partir d’un équivalent de l’erreur absolue. Le signe alterné ne disparaît qu’après prise du module.

#### Solution

Q7–Q8 donnent $\phi_{p,q}(n)-S_{p,q}=(-1)^nR_{p,q}(n)$. Comme l’intégrande de $R_{p,q}(n)$ est strictement positif sur $]0,1[$, aucune somme partielle n’est égale à la limite. Le rapport des valeurs absolues des erreurs est donc défini. Par Q23,

$$
\left|\frac{\phi_{p,q}(n+1)-S_{p,q}}{\phi_{p,q}(n)-S_{p,q}}\right|
=\frac{R_{p,q}(n+1)}{R_{p,q}(n)}\longrightarrow1.
$$

**La convergence est infra-linéaire.**


## Bilan

- Intégrer une somme géométrique finie puis borner son reste.
- Pour une fraction rationnelle à pôles simples, lire chaque coefficient au pôle et regrouper les conjugués pour revenir à une décomposition réelle.
- Pour sommer des parties entières, contrôler l’erreur uniformément sur tous les indices.
- Vérifier que l’erreur reste non nulle avant de former le quotient de deux erreurs successives.
