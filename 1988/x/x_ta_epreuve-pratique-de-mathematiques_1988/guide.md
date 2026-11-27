# Concours commun Mines-Ponts · École polytechnique, option T.A. — Épreuve pratique de mathématiques 1988 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

**Révision** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

Pour $x>0$, on étudie $f_p(x)=\int_1^x e^t/t^p\,dt$ et $g(x)=e^{-x}f_1(x)$. Les encadrements numériques sont donnés avec arrondi vers l’extérieur.

## I. Étude des intégrales auxiliaires

### I.1. Variations de la première intégrale

> [!INDICATION]
> Le théorème fondamental donne immédiatement la dérivée. La valeur en un fixe ensuite le signe de chaque côté.

Pour $x>0$ et $p\ge1$, $f_p(x)=\int_1^x e^t/t^p\,dt$. On a $f_1'(x)=e^x/x>0$. La fonction est strictement croissante, nulle en $1$, négative à gauche et positive à droite. Ses limites sont $-\infty$ en zéro et $+\infty$ à droite, la première étant précisée ci-dessous et la seconde résultant de $e^t/t\ge1$ pour $t\ge1$.

### I.2.a. Limite en zéro

> [!INDICATION]
> L’intégrale est orientée de $1$ vers $x$. Compare l’intégrande à $1/t$ avant de changer le sens de l’inégalité.

Pour $0<x<1$, $f_1(x)=-\int_x^1e^t/t\,dt\le-\int_x^1dt/t=\ln x$. Donc $f_1(x)\to-\infty$ lorsque $x\to0^+$.

### I.2.b. Partie principale en zéro

> [!INDICATION]
> Sépare le terme singulier $1/t$. Le quotient restant a une limite finie en zéro.

La fonction $(e^t-1)/t$ se prolonge par $1$ en zéro. Son intégrale $C=\int_0^1(e^t-1)/t\,dt$ existe. Ainsi $f_1(x)=\ln x-C+\int_0^x(e^t-1)/t\,dt=\ln x-C+O(x)$. On en déduit $f_1(x)\sim\ln x$ en zéro.

### I.3.a. Première intégration par parties

> [!INDICATION]
> Choisis $e^t$ comme facteur à primitiver. Garde la contribution de la borne fixe.

Une intégration par parties sur les bornes orientées $1,x$ donne $f_1(x)=[e^t/t]_1^x+\int_1^xe^t/t^2\,dt=e^x/x-e+f_2(x)$, pour tout $x>0$.

### I.3.b. Majoration par découpage

> [!INDICATION]
> Sur le premier demi-intervalle, majore l’exponentielle. Sur le deuxième, majore plutôt l’inverse de $t$.

Pour $x\ge2$ la partie intégrée de $1$ à $x/2$ est au plus $e^{x/2}\ln(x/2)$. De $x/2$ à $x$, elle est au plus $(2/x)(e^x-e^{x/2})$. En additionnant puis en simplifiant,

$$
f_1(x)\le e^{x/2}\ln x+2e^x/x.
$$

### I.3.c. Deux constantes pour encadrer la croissance

> [!INDICATION]
> Divise la majoration par $e^x/x$. Pour la minoration, utilise la positivité de $f_2$ au-delà de un.

La quantité $x\ln(x)e^{-x/2}$ tend vers zéro, donc $f_1(x)\le3e^x/x$ pour $x$ assez grand. Par I.3.a, $f_1(x)\ge e^x/x-e\ge e^x/(2x)$ dès que $e^x/x\ge2e$. On peut donc prendre $A=1/2$ et $B=3$.

### I.4.a. Relation entre deux rangs

> [!INDICATION]
> L’intégration par parties précédente fait maintenant intervenir la dérivée de $t^{-n}$.

Pour $n\ge1$ et tout $x>0$,

$$
f_n(x)=[e^t/t^n]_1^x+n\int_1^x e^t/t^{n+1}\,dt=e^x/x^n-e+n f_{n+1}(x).
$$

### I.4.b. Majoration à un rang quelconque

> [!INDICATION]
> Reprends le découpage en $x/2$. Pour $n>1$, la primitive de $1/t^n$ donne une borne uniforme sur le premier morceau.

Pour $n>1$ et $x\ge2$, le premier morceau est au plus $e^{x/2}\int_1^{x/2}t^{-n}dt\le e^{x/2}/(n-1)$. Le second est au plus $(2/x)^n\int_{x/2}^x e^t dt\le 2^ne^x/x^n$. On trouve $f_n(x)\le e^{x/2}/(n-1)+2^ne^x/x^n$. Pour $n=1$, la majoration logarithmique de I.3.b remplace celle du premier terme.

### I.4.c. Ordre de grandeur pour tout rang fixé

> [!INDICATION]
> L’exponentielle d’exposant moitié est négligeable devant $e^x/x^n$ pour tout $n$ fixé.

Par I.4.b, pour $n>1$ fixé et $x$ assez grand, $f_n(x)\le(1+2^n)e^x/x^n$. La relation de I.4.a et $f_{n+1}(x)\ge0$ donnent $f_n(x)\ge e^x/x^n-e\ge e^x/(2x^n)$ pour $x$ assez grand. Les constantes $A_n=1/2$, $B_n=1+2^n$ conviennent aussi pour $n=1$ grâce à I.3.c.

### I.5.a. Équivalent du premier rang

> [!INDICATION]
> L’encadrement au rang deux transforme le terme résiduel de la relation (1) en un terme négligeable.

On a $f_2=O(e^x/x^2)$ à l’infini. Dans $f_1=e^x/x-e+f_2$, les deux derniers termes sont donc $o(e^x/x)$. Ainsi $f_1(x)\sim e^x/x$.

### I.5.b. Équivalent général

> [!INDICATION]
> Dans la récurrence, compare le rang suivant au terme principal proposé pour le rang courant.

Pour $n$ fixé, $nf_{n+1}=O(e^x/x^{n+1})=o(e^x/x^n)$. La constante $-e$ est également négligeable. Par I.4.a, $f_n(x)\sim e^x/x^n$.

## II. Variations et calcul numérique de la fonction g

### II.1.a. Dérivée de la fonction pondérée

> [!INDICATION]
> Dérive le produit $e^{-x}f_1(x)$, puis élimine $f_1$ grâce à I.3.a.

On a $g'=1/x-g$. Puisque $g=1/x+e^{-x}(f_2-e)$, il vient $g'(x)=e^{-x}(e-f_2(x))$. En particulier $f_2(1)=0$ donne $g'(1)=1$.

### II.1.b. Existence d’un point critique unique

> [!INDICATION]
> Quelle est l’image de $[1,+\infty[$ par $f_2$ ?

La dérivée $f_2'(x)=e^x/x^2$ est strictement positive. La fonction part de $0$ en $1$ et tend vers $+\infty$ par I.5.b. Elle prend donc une seule fois la valeur $e$, en un point $\alpha>1$. Pour $x<1$, $f_2(x)<0$, ce qui exclut tout autre point critique.

### II.1.c. Tableau de variations et valeur maximale

> [!INDICATION]
> Pour déterminer la hauteur du maximum, utilise l’autre expression de la dérivée.

Comme $e^{-x}>0$, $g'$ est positive avant $\alpha$, nulle en $\alpha$ et négative après. La fonction croît donc sur $]0,\alpha]$ et décroît sur $[\alpha,+\infty[$. L’égalité $g'=1/x-g$ donne $g(\alpha)=1/\alpha$. Elle s’annule en $1$ et possède un maximum strictement positif.

### II.1.d. Parties principales aux extrémités

> [!INDICATION]
> Les équivalents obtenus pour $f_1$ restent valides après multiplication par le facteur exponentiel correspondant.

À gauche, $e^{-x}\to1$ et $f_1\sim\ln x$, donc $g(x)\sim\ln x\to-\infty$. À droite, $f_1\sim e^x/x$, donc $g(x)\sim1/x\to0^+$.

### II.2.a. Reste de Taylor sur le premier intervalle

> [!INDICATION]
> Utilise le reste de Lagrange entre zéro et $t$. La dérivée d’ordre $n+1$ est encore l’exponentielle.

Pour $S_n(t)=\sum_{k=0}^n t^k/k!$, $R_n(t)=e^t-S_n(t)$ vaut $e^\xi t^{n+1}/(n+1)!$ avec $0<\xi<t$ si $t>0$. Sur $[0,1]$, on a donc $0\le R_n(t)\le e t^{n+1}/(n+1)!$, avec $R_n(0)=0$.

### II.2.b. Encadrement de la première intégrale

> [!INDICATION]
> Intègre la majoration du reste après division par $t$. Pour $x\le1$, l’orientation crée un signe moins.

Posons $A_n(x)=\ln x+\sum_{k=1}^n(x^k-1)/(k\,k!)$. C’est l’intégrale de $S_n(t)/t$ de $1$ à $x$. Comme $f_1-A_n=-\int_x^1R_n(t)/t\,dt$, il vient pour $0<x\le1$

$$
A_n(x)-\frac{e(1-x^{n+1})}{(n+1)(n+1)!}\le f_1(x)\le A_n(x).
$$

**Sens de l’encadrement.** Pour une abscisse inférieure à un, une majoration positive du reste donne une erreur négative sur l’intégrale orientée de un vers cette abscisse.

### II.2.c. Valeurs en une demie

> [!INDICATION]
> La largeur de l’intervalle se multiplie par $e^{-1/2}$ pour $g$. La relation différentielle donne ensuite $g'$ sans autre intégration.

À $x=1/2$ et $n=6$, $A_6=-1{,}4408663645\ldots$ et la correction maximale est inférieure à $0{,}00007645$. Après multiplication par $e^{-1/2}$, $-0{,}873977<g(1/2)<-0{,}873929$. De $g'=2-g$ on déduit, à $10^{-3}$ près, $g(1/2)\simeq-0{,}874$ et $g'(1/2)\simeq2{,}874$.

### II.3.a. Reste de Taylor entre un et trois

> [!INDICATION]
> Dans le reste de Lagrange issu du développement en zéro, encadre l’exponentielle intermédiaire par $1$ et $e^3$.

Si $1\le t\le3$, la valeur intermédiaire $\xi$ appartient à $]0,t[$. On obtient $t^{n+1}/(n+1)!<R_n(t)\le e^3 t^{n+1}/(n+1)!$. La borne inférieure est stricte puisque $t>0$.

### II.3.b. Encadrement de la seconde intégrale

> [!INDICATION]
> Deux puissances demandent un traitement particulier dans l’intégrale de $S_n(t)/t^2$ : la puissance $-2$ et la puissance $-1$.

Pour $n\ge1$, posons

$$
B_n(x)=1-1/x+\ln x+\sum_{k=2}^n\frac{x^{k-1}-1}{(k-1)k!},\qquad D_n(x)=\frac{x^n-1}{n(n+1)!}.
$$

En intégrant le polynôme divisé par $t^2$ puis les deux bornes du reste, on trouve $B_n+D_n\le f_2\le B_n+e^3D_n$ sur $[1,3]$. À $1$ les trois valeurs sont nulles.

### II.3.c. Valeurs en deux et première localisation de la racine

> [!INDICATION]
> Propage les deux bornes de $f_2$ à l’aide des expressions de $g$ et de $g'$ plutôt que de dériver une approximation.

Avec $n=17$, l’encadrement précédent donne $2{,}0828703186<f_2(2)<2{,}0828703187$. Puis $g'(2)=e^{-2}(e-f_2(2))$ et $g(2)=1/2-g'(2)$. On obtient $0{,}08599359<g'(2)<0{,}08599361$ et $0{,}41400639<g(2)<0{,}41400641$. À $10^{-3}$ près, les trois valeurs sont respectivement **2,083**, **0,414** et **0,086** pour $f_2(2), g(2),g'(2)$. Comme $f_2(2)<e$, on a $\alpha>2$.

### II.3.d. Encadrement plus fin et hauteur du maximum

> [!INDICATION]
> Il suffit de comparer $f_2$ à $e$ aux deux abscisses proposées. La valeur de $g$ au maximum se lit directement sur l’abscisse.

Par II.3.b avec $n=17$, $2{,}45349984<f_2(2{,}2)<2{,}45349986$ et $2{,}83084412<f_2(2{,}4)<2{,}83084414$. La stricte croissance donne $2{,}2<\alpha<2{,}4$. On peut affiner par dichotomie avec le même encadrement. Aux abscisses $2{,}34090$ et $2{,}34091$, les valeurs sont respectivement dans $]2{,}71827397,2{,}71827398[$ et $]2{,}71829293,2{,}71829294[$, donc elles encadrent $e$. Il en résulte $1/2{,}34091<g(\alpha)<1/2{,}34090$, soit $g(\alpha)\simeq0{,}427185$ à $2\times10^{-6}$ près.

### II.4. Courbe représentative

> [!INDICATION]
> Place le zéro et sa pente, le maximum et les deux asymptotes. Les valeurs en une demie et en deux précisent le tracé.

La branche monte depuis l’asymptote $x=0$ avec $g\to-\infty$. Elle passe par $(1,0)$ avec tangente $y=x-1$, puis atteint vers $(2{,}34090,0{,}42719)$ son maximum à tangente horizontale. Elle reste ensuite positive et redescend vers l’axe horizontal, avec $g(x)\sim1/x$.

![Figure 1 — La fonction passe par zéro en 1, atteint son maximum un peu après 2,3 puis décroît vers zéro.](figures/variation-g.svg)

### II.5.a. Coefficients du développement avec reste exact

> [!INDICATION]
> Itère l’intégration par parties. Note séparément la puissance de $1/x$ et le terme de la borne fixe à chaque étape.

L’itération de $f_p=e^x/x^p-e+pf_{p+1}$, multipliée par $e^{-x}$, donne pour $n\ge1$

$$
g(x)=\sum_{p=1}^n\frac{(p-1)!}{x^p}-e^{1-x}\sum_{k=0}^{n-1}k!+n!e^{-x} f_{n+1}(x).
$$

On lit $a_p=(p-1)!$ et $b_n=-e\sum_{k=0}^{n-1}k!$. Au pas suivant, la substitution pour $f_{n+1}$ ajoute $n!/x^{n+1}$ et $-n!e^{1-x}$, ce qui établit aussi la récurrence.

### II.5.b. Divergence du reste à abscisse fixée

> [!INDICATION]
> À $x>1$ fixé, minore l’intégrande sur $[1,x]$ par une expression dont la dépendance en $n$ est explicite.

On a $r_n=n!e^{-x}\int_1^xe^t/t^{n+1}\,dt\ge n!e^{1-x}(x-1)/x^{n+1}>0$. À $x>1$ fixé, le rapport de deux termes successifs de ce minorant vaut $(n+1)/x$, donc le minorant tend vers $+\infty$. Ainsi $r_n\to+\infty$ et une troncature très tardive ne réduit pas l’erreur.

### II.5.c. Indice qui minimise le reste

> [!INDICATION]
> Compare deux restes successifs avec I.4.a. Le signe dépend alors de la position de $n\ln x$ par rapport à $x-1$.

Pour $r_0=e^{-x}f_1(x)>0$ et $n\ge1$, I.4.a donne

$$
r_n-r_{n-1}=(n-1)!e^{-x}(e-e^x/x^n).
$$

Le signe de $r_n/r_{n-1}-1$ est donc celui de $n\ln x-(x-1)$. Posons $q=(x-1)/\ln x>1$. Le reste diminue tant que $n<q$, puis augmente lorsque $n>q$. Un indice minimisant est $n_x=\lfloor q\rfloor$. Si $q$ est entier, $q-1$ et $q$ réalisent tous deux le minimum.

**Point entier.** Si le seuil est exactement entier, deux restes consécutifs sont égaux. L’un ou l’autre des deux indices fournit le minimum.

### II.5.d. Encadrement du reste pour trente

> [!INDICATION]
> La fonction à intégrer est convexe. Sur chacun des deux intervalles du sujet, la corde donne un majorant affine dont l’intégrale est l’aire d’un trapèze.

Pour $x=30$, $29/\ln30=8{,}526409\ldots$, d’où le minimum unique $r_8$. Posons $L(t)=e^t/t^9$. On a $L''=L[(1-9/t)^2+9/t^2]>0$. La corde entre $a$ et $b$ est la fonction affine $[(b-t)L(a)+(t-a)L(b)]/(b-a)$, majorante sur $[a,b]$. En l’intégrant sur $[1,9]$ puis $[9,30]$, on obtient

$$
0<r_8\le8!e^{-30}\left[4(L(1)+L(9))+\tfrac{21}{2}(L(9)+L(30))\right]<6{,}254\times10^{-8}.
$$

Cette dernière valeur est une approximation par excès certifiée du reste.

![Figure 2 — Pour une abscisse de 30, le reste positif est minimal à l’indice 8.](figures/reste-optimal.svg)

### II.5.e. Valeurs finales et précisions garanties

> [!INDICATION]
> Le reste est positif. Un milieu d’intervalle donne une erreur maximale deux fois moindre que la seule borne par excès.

Écrivons $T=\sum_{p=1}^8(p-1)!/30^p-e^{-29}\sum_{k=0}^7k!=0{,}03452711728854\ldots$. On a $T<g(30)<T+6{,}254\times10^{-8}$. Le milieu arrondi donne

$$
g(30)\simeq0{,}034527149,\qquad g'(30)=1/30-g(30)\simeq-0{,}001193815.
$$

L’intervalle certifié pour $g(30)$ est inclus dans $]0{,}03452711728,0{,}03452717984[$. La soustraction à $1/30$ conserve sa largeur. Les deux valeurs affichées ont une erreur strictement inférieure à $3{,}2\times10^{-8}$, arrondis compris.

## Documents de la session

Le bandeau du concours commun indique les options M, P′ et T.A., une durée de deux heures et l’École polytechnique pour l’option T.A. [Fac-similé UPS](https://prepas.org/index.php?module=Sujets&voir=get&file=doc-317ce6bbf6a5b1419fe8) · [Notice officielle du concours](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000697782).
