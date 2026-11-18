# Centrale-Supélec MP–MPI — Mathématiques 1 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le problème dure quatre heures et porte sur l'inégalité de Carleman, qui contrôle la somme des moyennes géométriques successives d'une suite positive. Les trois parties proposent deux preuves puis une borne plus fine. Elles se travaillent en grande partie indépendamment.

- **Partie I (Q1–Q10).** Prouver l'analogue intégral de Knopp, puis revenir aux suites par une fonction en escalier. Convexité, convergence dominée et intégration par parties.
- **Partie II (Q11–Q22).** Construire des maxima sur des simplexes et exploiter leurs conditions de stationnarité. Compacité, dérivées partielles et homogénéité.
- **Partie III (Q23–Q29).** Développer une fonction en série entière, puis améliorer la borne de Carleman en pondérant les termes. Séries entières et télescopage.

Q2–Q4, Q7–Q8, Q11–Q16 et Q23–Q24 permettent d'avancer par des méthodes de cours. Les questions Q10, Q20 et Q29 demandent de contrôler une construction ou une récurrence dans son ensemble. En cas de blocage, il est possible de commencer II sans avoir terminé I, ou III.A indépendamment des deux premières. III.B utilise en revanche l'inégalité arithmético-géométrique de II.A.

Lire une indication, reprendre la recherche, puis consulter la suivante si besoin. Les précisions sur l'existence des intégrales apparaissent dans les solutions Q1 et Q5–Q6.

## I — Inégalité de Knopp

On contrôle une moyenne géométrique continue par une intégrale pondérée. La fonction en escalier transmet ensuite cette borne aux moyennes géométriques d'une suite.

### I.A — Deux inégalités intégrales

### I.A.1 — Inégalité intégrale de Jensen

### Question 1

> [!INDICATION]
> Appliquer la convexité à la moyenne de valeurs prises sur une subdivision régulière.

> [!INDICATION]
> Préciser quelles fonctions il faut rendre intégrables, et à quel moment la continuité de la fonction convexe intervient.

> [!INDICATION]
> Tester un intervalle ouvert en une extrémité et une fonction continue par morceaux dont une limite latérale atteint cette extrémité.

#### Solution

Tel quel, l'énoncé ne garantit pas l'existence d'une intégrale finie à droite.

Sur $[0,1]$, prenons $f(0)=1$ et $f(t)=t$ pour $t>0$.

Avec $J=]0,1]$ et $\varphi(u)=1/u$, la fonction $\varphi$ est continue et convexe sur $J$, mais $\int_0^1 \varphi(f(t))\,dt$ diverge.

Supposons par exemple que les valeurs de $f$ soient contenues dans un segment $[c,d]\subset J$.

Les limites latérales de $f$ appartiennent alors aussi à ce segment et $\varphi\circ f$ est continue par morceaux.

Pour les sommes de Riemann à droite, posons $t_{j,N}=a+j(b-a)/N$.

La convexité appliquée à $N$ poids égaux à $1/N$, dont la somme vaut $1$, donne

$$
\begin{aligned}
\varphi\left(\frac1N\sum_{j=1}^N f(t_{j,N})\right)&\\
&\le \frac1N\sum_{j=1}^N\varphi(f(t_{j,N})).
\end{aligned}
$$

Les deux moyennes convergent par le théorème des sommes de Riemann appliqué aux fonctions continues par morceaux sur $[a,b]$. La moyenne de $f$ appartient à $[c,d]$ par comparaison, ce qui permet de passer à la limite en appliquant la continuité de $\varphi$. Pour $a<b$, on obtient

$$
\boxed{\varphi\left(\frac1{b-a}\int_a^b f(t)\,dt\right)
\le \frac1{b-a}\int_a^b\varphi(f(t))\,dt.}
$$

> [!JURY]
> Le rapport signale que la continuité de la fonction convexe sur $J$ ne suffit pas à rendre la composée intégrable. Il attend aussi la justification du passage à la limite dans les deux sommes de Riemann et le rappel que les poids associés à la convexité somment à un.

### I.A.2 — Une autre inégalité intégrale

### Question 2

> [!INDICATION]
> Borner $f$ au voisinage de zéro sur un segment fixé d'avance.

> [!INDICATION]
> Après la majoration, intégrer la fonction $t$ avant de simplifier le facteur qui dépend de $x$.

#### Solution

La fonction $f$ est bornée sur le segment fixe $[0,1]$, car elle y est continue par morceaux. Si $M$ est un majorant, alors pour $0<x\le1$,

$$
\begin{aligned}
0&\le g(x)\\
 &\le\frac{M}{x}\int_0^x t\,dt\\
 &=\frac{Mx}{2}.
\end{aligned}
$$

Donc **$g(x)\to0$ quand $x\to0^+$.**

> [!JURY]
> Le rapport relève des majorants qui dépendent de $x$. Fixer d'abord un segment contenant les petits intervalles donne une constante indépendante de $x$.

### Question 3

> [!INDICATION]
> Mettre tout le calcul sur le même domaine d'intégration par une indicatrice.

> [!INDICATION]
> Contrôler $t/x$ lorsque l'indicatrice est non nulle, puis étudier ce même rapport quand $t$ est fixé.

#### Solution

Pour $x>0$, la fonction $t\mapsto (t/x)f(t)\mathbf 1_{[0,x]}(t)$ est continue par morceaux et comprise entre $0$ et $f(t)$.

Pour chaque $t$ fixé, elle tend vers zéro quand $x\to+\infty$.

Le majorant $f$ est intégrable sur $\mathbb R_+$.

Le théorème de convergence dominée, appliqué le long de toute suite de paramètres tendant vers $+\infty$, donne **$g(x)\to0$ quand $x\to+\infty$.**

> [!PIEGE]
> Une fonction continue par morceaux et intégrable sur une demi-droite peut être non bornée à l'infini. La domination ici est par la fonction $f$ elle-même.

### Question 4

> [!INDICATION]
> Écrire la primitive du produit $tf(t)$ et reconnaître la dérivée qui fait apparaître le facteur $x^{-2}$.

> [!INDICATION]
> Travailler d'abord entre deux bornes strictement positives et finies. Leurs termes de bord se ramènent à la fonction étudiée en Q2 et Q3.

#### Solution

Pour $0<\varepsilon<R$, la primitive $G(x)=\int_0^x tf(t)\,dt$ est continue et de classe $\mathcal C^1$ par morceaux sur $[\varepsilon,R]$. Sur chaque morceau, $G'(x)=xf(x)$. On intègre par parties, puis on somme les morceaux dont les termes de bord intérieurs se compensent.

$$
\begin{aligned}
\int_\varepsilon^R h(x)\,dx
&=\left[-\frac{G(x)}x\right]_\varepsilon^R
  +\int_\varepsilon^R\frac{G'(x)}x\,dx\\
&=g(\varepsilon)-g(R)+\int_\varepsilon^R f(x)\,dx.
\end{aligned}
$$

Les limites de Q2 et Q3 et l'intégrabilité de $f$ donnent la convergence de l'intégrale de $h$, qui est positive. En séparant les deux limites à une borne fixe, par exemple $1$, on obtient

$$
\boxed{\int_0^{+\infty} h(x)\,dx=\int_0^{+\infty} f(x)\,dx.}
$$

### I.B — Démonstration de l’inégalité de Knopp

### Question 5

> [!INDICATION]
> Utiliser l'indication du sujet avant d'appliquer Jensen à une fonction dérivée du logarithme.

> [!INDICATION]
> Si la quantité $tf(t)$ peut s'approcher de zéro, imposez-lui un plancher $\delta>0$ avant d'appliquer Q1. Évaluez séparément la moyenne de $\ln t$.

#### Solution

La positivité de $f$ ne garantit pas que $\ln f$ soit intégrable au voisinage d'un bord de morceau.

Par exemple, posons $f(t)=e^{-1/t}$ pour $0<t\le1$, avec $f(0)=1$, puis $f(t)=e^{-t}$ pour $t>1$.

Cette fonction est strictement positive et intégrable, alors que $\int_0^1\ln f=-\infty$.

Les logarithmes sont bornés supérieurement sur chaque segment puisque $f$ y est bornée.

Leurs intégrales impropres ont donc un sens dans $\mathbb R\cup\{-\infty\}$, les seuls points éventuellement singuliers étant les bords des morceaux.

On convient que $\exp(-\infty)=0$.

Si l'on exige des intégrales finies dans l'exposant, il faut supposer en plus $\ln f$ localement intégrable, y compris en $0$.

Fixons $x>0$ et $\delta>0$.

On applique Q1 à $u_\delta(t)=\max(tf(t),\delta)$ sur $[0,x]$ et à la fonction convexe $-\ln$.

Les valeurs de $u_\delta$ sont dans un segment de $\mathbb R_+^*$.

Par comparaison, on obtient

$$
\begin{aligned}
\frac1x\int_0^x \ln(tf(t))\,dt
&\le\frac1x\int_0^x\ln u_\delta(t)\,dt\\
&\le\ln\left(\frac1x\int_0^x u_\delta(t)\,dt\right).
\end{aligned}
$$

Comme $0\le u_\delta(t)-tf(t)\le\delta$ et que l'intégrale de $tf(t)$ est strictement positive, le membre de droite tend vers le logarithme de la moyenne de $tf(t)$ quand $\delta\to0^+$.

Par la primitive $t\ln t-t$ et la limite $t\ln t\to0$ en $0^+$, $\ln t$ est intégrable sur $]0,x]$ et sa moyenne vaut $\ln x-1$.

Ainsi, en soustrayant la moyenne de $\ln t$ à celle de $\ln(tf(t))$ puis en prenant l'exponentielle,

$$
\boxed{
\exp\left(\frac1x\int_0^x\ln(f(t))\,dt\right)
\le \frac{e}{x^2}\int_0^x tf(t)\,dt .}
$$

> [!JURY]
> Le rapport souligne deux étapes souvent manquantes. La décomposition des logarithmes intervient avant de conclure avec Jensen. La primitive de $\ln t$ justifie son intégrabilité en zéro.

### Question 6

> [!INDICATION]
> Lire le membre de droite de Q5 à l'aide de la fonction de Q4.

> [!INDICATION]
> Pour l'intégrabilité, contrôler la régularité de la primitive de $\ln f$ sur les intervalles où elle demeure finie.

#### Solution

Notons $E(x)$ le membre de gauche de Q5.

Sur l'intervalle où l'intégrale de $\ln f$ est finie, sa primitive est continue et $E$ l'est aussi.

Si la partie négative de $\ln f$ donne une intégrale infinie à partir d'une certaine borne, $E$ vaut ensuite zéro par la convention de Q5.

Au point de transition éventuel dans $]0,+\infty[$, la partie positive de $\ln f$ a une intégrale continue, et la primitive de sa partie négative est croissante, donc a une limite à gauche, finie ou infinie.

$E$ y possède donc une limite à gauche et est continue par morceaux sur $]0,+\infty[$.

D'après Q5, $0\le E\le eh$, et $h$ est intégrable par Q4. Par comparaison, $E$ l'est aussi, et

$$
\boxed{\int_0^{+\infty}E(x)\,dx\le e\int_0^{+\infty} f(x)\,dx.}
$$

### I.C — Application à l’inégalité de Carleman

### Question 7

> [!INDICATION]
> Traiter d'abord la fonction constante du premier cas.

> [!INDICATION]
> Réunir le terme qui dépend de $x$ sous la forme d'une constante divisée par $x$. Utiliser la décroissance de la suite pour signer cette constante.

#### Solution

$v_1$ est constante, donc atteint notamment son minimum en $1$. Si $k\ge2$, on réécrit

$$
v_k(x)=\ln a_k+\frac1x\sum_{i=1}^{k-1}(\ln a_i-\ln a_k).
$$

La somme est positive ou nulle puisque la suite est décroissante et le logarithme croissant. Comme $x\mapsto1/x$ décroît sur $[k-1,k]$, $v_k$ est décroissante au sens large et **son minimum est atteint en $k$.**

> [!JURY]
> Le rapport relève l'oubli du rang $k=1$ et les calculs qui n'utilisent pas la décroissance. Le signe de la somme est précisément le point où cette hypothèse intervient.

### Question 8

> [!INDICATION]
> Découper l'intégrale intérieure suivant les marches de l'escalier.

> [!INDICATION]
> Pour $x$ sur la dernière marche, reconnaître la fonction de Q7 puis se servir de la longueur de l'intervalle extérieur.

#### Solution

Pour $k-1<x\le k$, les $k-1$ premières marches ont longueur $1$, et la dernière portion a longueur $x-k+1$.

La moyenne de $\ln f$ vaut donc $v_k(x)$, y compris pour $0<x\le1$.

Par Q7 et la croissance de l'exponentielle,

$$
\begin{aligned}
E(x)&\ge \exp(v_k(k))\\
&=\exp\left(\frac1k\sum_{i=1}^{k}\ln a_i\right).
\end{aligned}
$$

Le membre de droite est constant en $x$. L'intégration sur un intervalle de longueur $1$ donne **l'inégalité demandée.**

### Question 9

> [!INDICATION]
> Appliquer Q8 à une somme finie de marches et utiliser Q6 sur toute la demi-droite.

> [!INDICATION]
> Pour conclure à la convergence, penser au signe des termes.

#### Solution

On suppose $\sum a_k<+\infty$. La fonction en escalier définie par la suite est positive et continue par morceaux, et son intégrale vaut $\sum a_k$ par Chasles. D'après Q8, pour tout $N$, la somme des $N$ premières moyennes géométriques est majorée par $\int_0^N E(x)\,dx$. Par Q6, cette quantité est majorée par $e\sum_{k\ge1} a_k$. Les sommes partielles sont croissantes et majorées, d'où

$$
\boxed{\begin{aligned}
\sum_{k=1}^{+\infty}(a_1\cdots a_k)^{1/k}&\\
&\le e\sum_{k=1}^{+\infty} a_k.
\end{aligned}}
$$

### Question 10

> [!INDICATION]
> Pour majorer un produit de $k$ termes, chercher les $k$ plus grands termes disponibles.

> [!INDICATION]
> La suite tend vers zéro. Expliquer pourquoi un maximum existe parmi les termes non encore choisis et pourquoi chaque indice sera choisi.

#### Solution

Comme $a_k\to0$ et $a_k>0$, les valeurs peuvent être énumérées en ordre décroissant, en conservant leurs multiplicités. En effet, parmi les termes restants, en choisir un de valeur $v>0$ suffit à localiser un maximum dans l'ensemble fini des termes de valeur au moins $v$. En prenant un maximum à chaque étape, tout indice de départ finit par être choisi, car il n'y a qu'un nombre fini de termes supérieurs ou égaux à sa valeur. Notons $(b_k)$ ce réarrangement. La somme positive est inchangée.

Pour chaque $k$, les $k$ premiers termes de $(b_i)$ sont les $k$ plus grands.

Si l'on trie les $k$ premiers termes de $(a_i)$ entre eux, le $j$-ième de ce tri est au plus $b_j$ pour $1\le j\le k$.

On multiplie ces inégalités pour obtenir $a_1\cdots a_k\le b_1\cdots b_k$.

**La majoration de Q9 pour $(b_k)$ s'applique ainsi aux sommes partielles de $(a_k)$**, et le passage à la limite donne l'inégalité de Carleman.

> [!METHODE]
> Pour une suite positive tendant vers zéro, les termes supérieurs ou égaux à un seuil positif sont en nombre fini. Cette propriété permet à la fois de construire le réarrangement et de vérifier qu'il reprend tous les termes.

## II — Inégalité de Carleman

On maximise d'abord un produit, puis une somme de moyennes géométriques, à somme de coordonnées fixée. Les variations qui laissent cette somme inchangée donnent les équations utiles.

### II.A — Inégalité arithmético-géométrique

### Question 11

> [!INDICATION]
> Pour le produit, dériver une seule coordonnée et conserver toutes les autres comme constantes.

#### Solution

La dérivée partielle du produit selon sa $k$-ième coordonnée est le produit des autres coordonnées, soit $f(x)/x_k$ sur $U_n$. Celle de la somme selon toute coordonnée vaut $1$. Ainsi,

$$
\begin{aligned}
\nabla f(x)&=\left(\frac{f(x)}{x_1},\ldots,\frac{f(x)}{x_n}\right),\\
\nabla g_s(x)&=(1,\ldots,1).
\end{aligned}
$$

### Question 12

> [!INDICATION]
> Inclure les points du bord dans le domaine sur lequel on cherche un maximum.

> [!INDICATION]
> Montrer que le domaine de contrainte est fermé et borné. Comparer ensuite un point dont toutes les coordonnées sont égales à un point du bord.

#### Solution

L'ensemble $X_s$ est l'intersection du fermé $\overline U_n=(\mathbb R_+)^n$ avec l'hyperplan affine d'équation $\sum_k x_k=s$, fermé comme niveau d'une fonction continue. Il est borné puisque chacune de ses coordonnées appartient à $[0,s]$ et il contient $(s/n,\ldots,s/n)$. Il est donc compact et non vide. La fonction continue $f$ y atteint son maximum.

Le produit est strictement positif en $(s/n,\ldots,s/n)$ et il s'annule dès qu'une coordonnée est nulle. **Tout maximum est donc atteint dans $X_s\cap U_n$.**

> [!JURY]
> Le rapport attend à la fois la preuve de compacité et la localisation d'un maximum intérieur. Comparer les valeurs du produit sur le bord et en un point intérieur distingue ces deux étapes.

### Question 13

> [!INDICATION]
> Chercher une variation qui modifie deux coordonnées en laissant leur somme inchangée.

> [!INDICATION]
> Utiliser l'annulation de la dérivée dans cette direction au maximum intérieur, puis Q11 pour déterminer le signe de la valeur commune.

#### Solution

Pour $k\ge2$, la courbe $t\mapsto a+t(e_k-e_1)$ reste dans $X_s\cap U_n$ pour $|t|$ assez petit.

La somme des coordonnées est inchangée et la stricte positivité de celles de $a$ laisse un intervalle ouvert autour de zéro.

La restriction de $f$ à cette courbe est dérivable et maximale en $0$, donc sa dérivée y est nulle.

Par Q11, cela donne $\partial_k f(a)=\partial_1 f(a)$.

En posant $\lambda=f(a)/a_1>0$, on obtient, pour tout $k$,

$$
\boxed{a_k=f(a)/\lambda.}
$$

Pour $n=1$, le choix de $\lambda$ donne directement la seule égalité.

> [!METHODE]
> Une variation de la forme $t(e_j-e_i)$ respecte une contrainte de somme. En un maximum intérieur, on peut l'effectuer dans les deux sens et utiliser une condition de stationnarité en une variable.

### Question 14

> [!INDICATION]
> Utiliser la somme fixée pour déterminer la coordonnée commune du maximum trouvé en Q13.

> [!INDICATION]
> Pour un $n$-uplet arbitraire, distinguer les coordonnées toutes positives et le cas d'un produit nul.

#### Solution

Toutes les coordonnées de $a$ sont égales d'après Q13. Comme leur somme vaut $s$, elles valent $s/n$. La maximalité du produit en $a$ donne pour $x\in X_s\cap U_n$

$$
\begin{aligned}
\left(\prod_{i=1}^n x_i\right)^{1/n}&\le \frac{s}{n}\\
&=\frac1n\sum_{i=1}^n x_i .
\end{aligned}
$$

Pour un $n$-uplet strictement positif quelconque, on choisit $s$ égal à la somme de ses coordonnées. S'il contient une coordonnée nulle, son produit est nul et la somme est positive ou nulle. **L'inégalité vaut donc sur $(\mathbb R_+)^n$.**

### II.B — Démonstration de l’inégalité de Carleman

### Question 15

> [!INDICATION]
> Considérer la dérivée partielle selon $x_k$ et examiner quels produits de la somme dépendent de cette coordonnée.

> [!INDICATION]
> Pour ces produits, isoler la puissance de $x_k$ avant de dériver.

#### Solution

Pour $x\in U_n$, posons $p_j(x)=(x_1\cdots x_j)^{1/j}$.

Si $j<k$, $p_j$ ne dépend pas de $x_k$.

Si $j\ge k$, sa dérivée partielle selon $x_k$ est $p_j(x)/(j x_k)$.

Ainsi,

$$
\begin{aligned}
\partial_k F_n(x)&=\frac1{x_k}\sum_{j=k}^n\frac{p_j(x)}{j},\\
\nabla h_n(x)&=(1,\ldots,1).
\end{aligned}
$$

Les $n$ dérivées partielles affichées sont les composantes du gradient de $F_n$.

### Question 16

> [!INDICATION]
> Appliquer le théorème des bornes atteintes en reprenant la démarche de Q12. Vérifier la continuité jusque sur la frontière.

#### Solution

L'ensemble $\overline U_n\cap H_n$ est fermé et contenu dans $[0,1]^n$.

Il est compact et contient $(1/n,\ldots,1/n)$.

Chaque fonction $p_j$ est continue jusque sur $\overline U_n$, par continuité du produit et de la racine $j$-ième sur $\mathbb R_+$.

**$F_n$ atteint donc son maximum sur $\overline U_n\cap H_n$.**

### Question 17

> [!INDICATION]
> Utiliser le fait admis dans l'énoncé pour prendre de petites variations admissibles dans les deux sens.

> [!INDICATION]
> Au maximum, comparer les dérivées partielles deux à deux, puis utiliser leur expression en Q15.

#### Solution

On utilise l'hypothèse admise selon laquelle $a$, point de maximum, appartient à $U_n\cap H_n$.

Comme dans Q13, les courbes $t\mapsto a+t(e_k-e_1)$ restent admissibles autour de $0$.

La dérivée de $F_n$ le long de ces courbes en $0$ est nulle, donc toutes les composantes de $\nabla F_n(a)$ sont égales à $\lambda=\partial_1F_n(a)$.

Cette quantité est strictement positive par Q15 et la positivité des $\gamma_j$ et de $a_1$.

Le cas $n=1$ utilise directement $\lambda=\partial_1F_1(a)$.

D'après Q15 et $a\in H_n$,

$$
\boxed{\begin{aligned}
\sum_{j=k}^n\frac{\gamma_j}{j}&=\lambda a_k
\qquad (k=1,\ldots,n),\\
\sum_{k=1}^n a_k&=1.
\end{aligned}}
$$

> [!JURY]
> Le rapport signale l'oubli de la stricte positivité du multiplicateur. Elle suit ici de la formule explicite pour sa valeur, donnée par la première composante du gradient.

### Question 18

> [!INDICATION]
> Pour a), compter les apparitions d'un terme de la somme triangulaire, à indice fixé.

> [!INDICATION]
> Pour b), soustraire deux équations consécutives du système, puis traiter sa dernière ligne séparément.

#### Solution

**a)** On somme les $n$ équations de Q17. Pour chaque $j$, le terme $\gamma_j/j$ apparaît exactement $j$ fois. Ainsi,

$$
\boxed{\begin{aligned}
\lambda&=\sum_{j=1}^n\gamma_j\\
&=M_n.
\end{aligned}}
$$

**b)** Pour $k<n$, la différence des équations d'indices $k$ et $k+1$ donne $\gamma_k/k=\lambda(a_k-a_{k+1})$.

Pour $k=n$, la dernière équation donne $\gamma_n/n=\lambda a_n$.

Ainsi, avec les $\omega_k$ définis par l'énoncé,

$$
\boxed{\gamma_k=\lambda\omega_k a_k.}
$$

En particulier, chaque $\omega_k$ est strictement positif.

### Question 19

> [!INDICATION]
> Prenez l'inverse du terme à comparer à $1/e$, puis le logarithme. Utilisez une inégalité simple sur $\ln(1+u)$.

#### Solution

Pour $u\ge0$, la fonction $u-\ln(1+u)$ est croissante et nulle en zéro, donc $\ln(1+u)\le u$. Pour $k\in\mathbb N$, on applique cette inégalité à $u=1/(k+1)$ et on obtient

$$
(k+1)\ln\left(\frac{k+2}{k+1}\right)\le1.
$$

L'exponentielle donne une majoration par $e$, puis le passage aux inverses donne

$$
\boxed{\frac1e\le \left(\frac{k+1}{k+2}\right)^{k+1}.}
$$

### Question 20

> [!INDICATION]
> Commencer par la première moyenne géométrique, puis comparer deux moyennes successives après élévation aux puissances entières.

> [!INDICATION]
> Après introduction des $\omega_k$, encadrer le quotient $\omega_k/(1-\omega_k/k)$ sous l'hypothèse de récurrence. Faire intervenir Q19 à l'étape suivante.

#### Solution

On suppose $\lambda>e$. Comme $\gamma_1=a_1$, Q18b donne $\omega_1=1/\lambda<1/e$. Q19 appliquée à $k=0$ donne $1/e\le1/2$, ce qui initialise la récurrence.

Pour $1\le k<n$, l'identité $\gamma_{k+1}^{k+1}=\gamma_k^k a_{k+1}$ s'obtient en développant les deux produits définissant les moyennes. En remplaçant les $\gamma$ par Q18b, puis en utilisant $a_{k+1}/a_k=1-\omega_k/k$, on obtient

$$
\begin{aligned}
\omega_{k+1}^{k+1}
&=\frac1\lambda\,\omega_k^k\left(\frac{a_k}{a_{k+1}}\right)^k\\
&=\frac1\lambda
\left(\frac{\omega_k}{1-\omega_k/k}\right)^k.
\end{aligned}
$$

Si $\omega_k\le k/(k+1)$, alors $1-\omega_k/k\ge k/(k+1)>0$, et le quotient ci-dessus est au plus $1$. Par Q19,

$$
\omega_{k+1}^{k+1}\le\frac1\lambda
<\frac1e
\le\left(\frac{k+1}{k+2}\right)^{k+1}.
$$

En prenant la racine positive, l'hérédité est établie. **$\omega_1\le1/e$ et $\omega_k\le k/(k+1)$ pour $1\le k\le n$.**

> [!METHODE]
> Quand deux moyennes géométriques ont des longueurs consécutives, élever chacune à son nombre de facteurs fait apparaître un lien immédiat entre les deux produits.

### Question 21

> [!INDICATION]
> Comparer la borne obtenue en Q20 à la valeur fixée du dernier coefficient. Revenir ensuite au maximum de $F_n$.

#### Solution

La conclusion de Q20 est incompatible avec $\omega_n=n$. L'hypothèse $\lambda>e$ est donc fausse. Par Q18a, $M_n=\lambda\le e$. Pour tout $x\in U_n$ de somme $1$,

$$
\boxed{\sum_{k=1}^n(x_1\cdots x_k)^{1/k}\le e.}
$$

### Question 22

> [!INDICATION]
> Normaliser les $N$ premiers termes par leur somme. Vérifier comment cette normalisation affecte chacune de leurs moyennes géométriques.

#### Solution

Pour $N\ge1$, posons $s_N=\sum_{k=1}^N a_k>0$. On applique Q21 au $N$-uplet $(a_k/s_N)_{1\le k\le N}$. Chaque moyenne géométrique est homogène de degré un, donc

$$
\sum_{k=1}^N(a_1\cdots a_k)^{1/k}\le e s_N .
$$

Si $\sum a_k$ converge, le membre de droite est borné et les sommes partielles de gauche croissent. Elles convergent et, par passage à la limite, **on retrouve l'inégalité de Carleman.**

## III — Inégalité de Carleman-Yang

La première sous-partie identifie les coefficients d'une série entière. La seconde choisit des poids pour faire apparaître cette fonction dans la borne et compare les nouveaux coefficients à ceux de Carleman.

### III.A — Un développement en série entière

### Question 23

> [!INDICATION]
> Écrire la puissance à l'aide de l'exponentielle et étudier la limite de son exposant.

#### Solution

Quand $t\to0$, $\ln(1-t)=-t+o(t)$.

Pour $t\ne0$, le logarithme de $\varphi(t)$ vaut $(1-1/t)\ln(1-t)$, qui tend vers $1$.

Par continuité de l'exponentielle, **le prolongement vaut $\varphi(0)=e$.**

> [!PIEGE]
> Un équivalent dans un exposant ne donne pas en général un équivalent après exponentiation. Ici l'exposant a une limite finie et on utilise la continuité.

### Question 24

> [!INDICATION]
> La formule de récurrence utilise tous les indices précédents. Majorer uniformément les facteurs $1/(k+1)$.

> [!INDICATION]
> Pour une valeur fixée de $t$ strictement à l'intérieur de l'intervalle, chercher un majorant géométrique des termes.

#### Solution

On raisonne par récurrence forte à partir de $|b_0|=1$. Si $|b_j|\le1$ pour $0\le j<n$, alors

$$
\begin{aligned}
|b_n|&\le\frac1n\sum_{k=1}^n\frac{|b_{n-k}|}{k+1}\\
&\le\frac12.
\end{aligned}
$$

Ainsi $|b_n|\le1$ pour tout $n$. Pour $|t|<1$, la série $\sum b_n t^n$ converge absolument par comparaison à la série géométrique. **Son rayon de convergence est au moins $1$.**

### Question 25

> [!INDICATION]
> Développer le logarithme de $\varphi$, puis utiliser Q23 pour inclure le point zéro.

> [!INDICATION]
> Une fois l'équation différentielle obtenue, appliquer la formule de Leibniz et lire les dérivées à l'origine dans la série de $\psi$.

#### Solution

Pour $0<|t|<1$, on utilise le développement en série entière de $\ln(1-t)$ puis on réindexe les deux séries absolument convergentes. Cela donne

$$
\begin{aligned}
\ln\varphi(t)&=(1-1/t)\ln(1-t)\\
&=1-\sum_{m=1}^{+\infty}\frac{t^m}{m(m+1)}.
\end{aligned}
$$

D'après Q23, cette formule reste vraie en $0$.

La série définit une fonction de classe $\mathcal C^\infty$ sur $]-1,1[$, et donc $\varphi$ aussi par composition avec l'exponentielle.

La dérivation terme à terme de $\ln\varphi$ donne $\psi$ comme dans l'énoncé, d'où **$\varphi'=\varphi\psi$** sur tout $]-1,1[$.

Pour $n\ge1$, on dérive cette égalité $n-1$ fois par la formule de Leibniz. Les coefficients de la série de $\psi$ donnent $\psi^{(k)}(0)=-k!/(k+2)$. Ainsi,

$$
\boxed{\varphi^{(n)}(0)
=-\sum_{k=0}^{n-1}\binom{n-1}{k}
\frac{k!}{k+2}\,\varphi^{(n-1-k)}(0).}
$$

> [!JURY]
> Le rapport relève l'oubli de la régularité en zéro. Le développement convergent du logarithme de $\varphi$ est valable au point prolongé et justifie la dérivation sur tout l'intervalle.

### Question 26

> [!INDICATION]
> Former la série des $b_n$ grâce à Q24 et chercher quelle équation différentielle elle satisfait.

> [!INDICATION]
> Le produit de Cauchy avec $\psi$ réunit les mêmes coefficients que la récurrence. Comparer les deux solutions par un quotient.

#### Solution

Posons $B(t)=\sum_{n=0}^{+\infty}b_n t^n$ pour $|t|<1$. D'après Q24, cette fonction est dérivable terme à terme sur cet intervalle. Le coefficient d'indice $n-1$ de $B\psi$, obtenu par produit de Cauchy de séries absolument convergentes, vaut

$$
-\sum_{k=1}^n\frac{b_{n-k}}{k+1}=n b_n.
$$

La récurrence des $b_n$ montre donc que $B'=B\psi$.

Comme $\varphi'=\varphi\psi$ et $\varphi>0$, le quotient $B/\varphi$ a une dérivée nulle sur $]-1,1[$.

Sa valeur en $0$ est $-1/e$.

On en déduit, pour $|t|<1$,

$$
\boxed{\varphi(t)=e\left(1-\sum_{n=1}^{+\infty} b_n t^n\right).}
$$

> [!METHODE]
> L'identification des dérivées à l'origine ne suffit pas, à elle seule, à montrer qu'une fonction est développable en série entière. Construire la somme de la série et vérifier l'équation différentielle donne l'identité sur tout l'intervalle.

### III.B — Démonstration de l’inégalité de Carleman-Yang

### Question 27

> [!INDICATION]
> Appliquer l'inégalité de II.A aux termes pondérés par les $c_k$.

> [!INDICATION]
> Sommer d'abord jusqu'à une borne finie et échanger les deux indices dans le triangle obtenu. Utiliser la positivité pour majorer la somme tronquée.

#### Solution

On applique Q14 aux $n$ termes $c_i a_i$ puis on divise par $(c_1\cdots c_n)^{1/n}$. On obtient

$$
(a_1\cdots a_n)^{1/n}\le
\frac{(c_1\cdots c_n)^{-1/n}}{n}\sum_{k=1}^n c_k a_k.
$$

Pour $N\ge1$, on somme ces inégalités puis on réordonne la somme finie sur les indices $1\le k\le n\le N$. On obtient

$$
\begin{aligned}
\sum_{n=1}^N (a_1\cdots a_n)^{1/n}&\\
&\le\sum_{k=1}^N c_k a_k\sum_{n=k}^N
\frac{(c_1\cdots c_n)^{-1/n}}{n}.
\end{aligned}
$$

La positivité des termes permet de majorer le membre de droite en étendant les sommes à l'infini. Le passage à la limite à gauche montre **l'inégalité de Q27**, dans $[0,+\infty]$ si une série diverge.

> [!PIEGE]
> Sur la région infinie des indices, les séries peuvent diverger. Le raisonnement par sommes finies et majoration positive permet de conclure même dans ce cas.

### Question 28

> [!INDICATION]
> Développer le produit des poids pour chercher une simplification entre facteurs consécutifs.

> [!INDICATION]
> Transformer la somme intérieure en somme télescopique. Pour le poids final, évaluer $\varphi$ en l'inverse d'un entier adéquat.

#### Solution

Pour le choix indiqué, le produit se télescope, car la puissance $i$ de $i+1$ se simplifie avec le dénominateur du facteur suivant. Il reste $\prod_{i=1}^n c_i=(n+1)^n$. Par conséquent,

$$
\begin{aligned}
\sum_{n=k}^{+\infty}\frac{(c_1\cdots c_n)^{-1/n}}n
&=\sum_{n=k}^{+\infty}\left(\frac1n-\frac1{n+1}\right)\\
&=\frac1k.
\end{aligned}
$$

Le poids de $a_k$ dans Q27 devient $c_k/k=((k+1)/k)^k$. C'est exactement $\varphi(1/(k+1))$, puisque $1-1/(k+1)=k/(k+1)$ et que l'exposant de $\varphi$ y vaut $-k$. D'après Q26, on obtient

$$
\boxed{\begin{aligned}
\sum_{n=1}^{+\infty}(a_1\cdots a_n)^{1/n}&\\
&\le e\sum_{n=1}^{+\infty}
 \left(1-\sum_{k=1}^{+\infty}\frac{b_k}{(n+1)^k}\right)a_n .
\end{aligned}}
$$

### Question 29

> [!INDICATION]
> Isoler le terme en $b_0$ dans la récurrence. Pour exploiter l'hypothèse de récurrence, comparer ensuite deux rangs consécutifs.

> [!INDICATION]
> Séparer le terme d'indice $n-1$, puis comparer la somme restante avec celle qui détermine $b_{n-1}$ à l'aide du quotient des deux dénominateurs.

> [!INDICATION]
> Pour la comparaison des inégalités, considérer l'effet du premier coefficient sur chaque poids et utiliser la représentation positive de ce poids en Q28.

#### Solution

Par la récurrence, $b_1=1/2$. Pour $n\ge2$, supposons $b_1,\ldots,b_{n-1}\ge0$. En isolant le terme qui contient $b_0=-1$ puis en réindexant, on trouve

$$
n b_n=\frac1{n+1}-\frac{b_{n-1}}2-\sum_{j=1}^{n-2}\frac{b_j}{n-j+1}.
$$

Pour $1\le j\le n-2$, le rapport $(n-j)/(n-j+1)$ est au plus $n/(n+1)$. Comme les $b_j$ sont positifs ou nuls, la relation au rang $n-1$ donne

$$
\begin{aligned}
\sum_{j=1}^{n-2}\frac{b_j}{n-j+1}
&\le\frac{n}{n+1}\sum_{j=1}^{n-2}\frac{b_j}{n-j}\\
&=\frac{n}{n+1}\left(\frac1n-(n-1)b_{n-1}\right).
\end{aligned}
$$

Les sommes sont vides si $n=2$, et la relation reste valable. En reportant dans le calcul de $n b_n$, on obtient

$$
n b_n\ge \left(\frac{n(n-1)}{n+1}-\frac12\right)b_{n-1}\ge0.
$$

La dernière parenthèse est positive pour $n\ge2$, car $n/(n+1)\ge2/3$ et $n-1\ge1$. Ainsi **$b_n\ge0$ pour tout $n\ge1$.**

Dans Q28, chaque facteur entre parenthèses est strictement inférieur à $1$, puisque $b_1>0$. Il est positif par sa représentation comme $\varphi(1/(n+1))/e$. Si $\sum a_n$ est finie, la majoration terme à terme donne un membre de droite fini et strictement inférieur à $e\sum a_n$, puisqu'au moins le terme en $a_1>0$ est strictement réduit. **L'inégalité de Carleman-Yang affine donc celle de Carleman.**

## Bilan

- Contrôler les domaines et l'intégrabilité avant d'appliquer Jensen. Dans une preuve par sommes de Riemann, vérifier aussi la composée et le point où la fonction convexe sera évaluée.
- Pour une intégration par parties impropre, calculer entre deux bornes finies, puis étudier les termes de bord avant de conclure.
- Pour un maximum sous contrainte linéaire, déterminer d'abord le domaine compact. Quand un maximum intérieur est connu, les variations qui conservent la somme donnent les relations de stationnarité.
- Pour reconnaître une série entière par une récurrence, justifier le rayon, puis vérifier l'équation satisfaite par sa somme. Dans une double somme positive, traiter les indices sur un domaine fini avant de passer à la limite.
