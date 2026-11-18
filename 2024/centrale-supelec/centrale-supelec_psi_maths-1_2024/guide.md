# CentraleSupélec PSI — Mathématiques 1 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Cette épreuve de quatre heures relie l'intégrale de Gauss aux séries entières et à l'orthogonalité. Les questions 1 à 8 calculent l'intégrale à partir de Wallis. Les questions 9 à 13 traitent une équation différentielle au moyen des séries entières et d'une intégrale à paramètre. La troisième partie construit les polynômes d'Hermite, calcule leur norme et les utilise pour diagonaliser un endomorphisme. La dernière partie combine moments gaussiens, séries et orthogonalité.

Le programme de PCSI fournit les outils élémentaires d'intégration et les propriétés des polynômes. Celui de PSI intervient pour les intégrales généralisées et à paramètre, les séries entières, les espaces préhilbertiens et le théorème spectral. La définition de la transformation de Fourier et son injectivité sont données par l'énoncé.

Commencez chaque partie en repérant le résultat antérieur dont elle dépend. Les calculs directs et les récurrences du début de la partie III sont abordables après la partie I, même si la partie II vous retient. Gardez assez de temps pour rédiger les hypothèses des théorèmes d'intégration, puis pour la majoration de Q38. Le jury demande particulièrement de contrôler les termes de bord et de soigner les étapes des récurrences. [Sujet officiel](https://www.concours-centrale-supelec.fr/sites/default/files/2025-01/M070.pdf) · [Rapport 2024, rubrique Mathématiques 1](https://www.concours-centrale-supelec.fr/sites/default/files/documents/Rapport%20CCS%202024%20PSI_0.pdf).

## Partie I — Intégrale de Wallis et Intégrale de Gauss

Une relation entre deux rangs de même parité permet de contrôler le quotient de termes voisins. Elle fournit ensuite l'asymptotique nécessaire pour identifier l'intégrale gaussienne.

### I.A

### Question 1

> [!INDICATION]
> Comparez deux puissances successives de la même valeur sur l'intérieur du segment.

#### Solution

Pour $0<t<\pi/2$, on a $0<\cos t<1$, donc $\cos^{n+1}t<\cos^n t$. La différence est continue et strictement positive sur l'intérieur de l'intervalle. En intégrant, on obtient **$0<W_{n+1}<W_n$ pour tout $n\in\mathbb N$**.

### Question 2

> [!INDICATION]
> Isolez un facteur qui possède une primitive simple.

> [!INDICATION]
> Après l'intégration par parties, exprimez le facteur en sinus à l'aide de l'identité trigonométrique du cercle.

#### Solution

On intègre par parties sur $[0,\pi/2]$ en dérivant $\cos^{n+1}t$ et en intégrant $\cos t$. Le terme de bord $[\sin t\,\cos^{n+1}t]_0^{\pi/2}$ est nul. Ainsi
$$
W_{n+2}=(n+1)\int_0^{\pi/2}\sin^2t\,\cos^n t\,dt
=(n+1)(W_n-W_{n+2}).
$$
On en déduit **$(n+2)W_{n+2}=(n+1)W_n$**.

> [!PIEGE]
> Le terme $\cos^n t$ n'a pas pour primitive $\cos^{n+1}t/(n+1)$. L'intégration par parties repose sur la primitive du facteur $\cos t$ isolé.

### Question 3

> [!INDICATION]
> Cherchez une expression dont la valeur au rang suivant se ramène à celle au rang courant grâce à la relation de Q2.

> [!INDICATION]
> Une fois la constance obtenue, revenez au premier rang.

#### Solution

D'après la question 2, $(n+2)W_{n+1}W_{n+2}=(n+1)W_nW_{n+1}$. La suite $((n+1)W_nW_{n+1})_{n\ge0}$ est donc constante. Comme $W_0=\pi/2$ et $W_1=[\sin t]_0^{\pi/2}=1$,
$$
\boxed{(n+1)W_nW_{n+1}=\frac{\pi}{2}.}
$$

### Question 4

> [!INDICATION]
> Pour transformer le produit de deux termes consécutifs en carré, cherchez leur quotient.

> [!INDICATION]
> Encadrez ce quotient en utilisant aussi le terme situé deux rangs plus loin.

#### Solution

Les questions 1 et 2 donnent
$$
\frac{n+1}{n+2}=\frac{W_{n+2}}{W_n}\le\frac{W_{n+1}}{W_n}\le1.
$$
Donc $W_{n+1}/W_n\to1$. Par la question 3, $W_n^2=(W_n/W_{n+1})\pi/(2(n+1))\sim\pi/(2n)$. En prenant les racines positives,
$$
\boxed{W_n\sim\sqrt{\frac{\pi}{2n}}\qquad(n\to+\infty).}
$$

> [!JURY]
> Le rapport relève que la convergence d'une suite ne permet pas en général de conclure à l'équivalence de deux termes consécutifs. Établissez ici un encadrement du quotient.

### I.B

### Question 5

> [!INDICATION]
> Séparez un segment initial du voisinage de l'infini. Comparez les deux puissances de $x$ que l'on peut mettre dans l'exponentielle.

#### Solution

La fonction $x\mapsto e^{-x^2}$ est continue et positive sur $[0,+\infty[$. Pour $x\ge1$, elle est majorée par $e^{-x}$, intégrable sur $[1,+\infty[$. **L'intégrale $I$ converge.**

### Question 6

> [!INDICATION]
> Ramenez les intégrales à un intervalle fixe avant de choisir un théorème de convergence.

> [!INDICATION]
> Sur le support de l'intégrande, comparez le facteur élémentaire à une exponentielle avant de l'élever à la puissance $n$.

#### Solution

Pour $n\ge1$, on pose $f_n(x)=(1-x^2/n)^n$ sur $[0,\sqrt n]$ et $f_n(x)=0$ au-delà. Ces fonctions sont continues, car elles s'annulent au point de raccordement.

Pour $x\ge0$ fixé et $n>x^2$, le développement de $\log(1-u)$ au voisinage de $0$ donne $n\log(1-x^2/n)\to-x^2$, d'où $f_n(x)\to e^{-x^2}$.

Pour $0\le x\le\sqrt n$, l'inégalité $1-u\le e^{-u}$, appliquée à $u=x^2/n$, donne $0\le f_n(x)\le e^{-x^2}$. Le majorant convient aussi au-delà de $\sqrt n$ et est intégrable par la question 5. Le théorème de convergence dominée fournit
$$
\boxed{\lim_{n\to+\infty}\int_0^{\sqrt n}(1-x^2/n)^n\,dx=I.}
$$

> [!METHODE]
> En prolongeant par zéro les intégrandes, on transforme une limite à borne mobile en un problème de convergence dominée sur une demi-droite fixe.

### Question 7

> [!INDICATION]
> Déterminez le segment des valeurs de $u$ et vérifiez le caractère $C^1$ du changement de variable.

> [!INDICATION]
> Combinez le facteur issu de la dérivée et celui issu de l'identité $1-\sin^2u$.

#### Solution

Pour $n\ge1$, $u\mapsto\sqrt n\sin u$ est une bijection croissante de classe $C^1$ de $[0,\pi/2]$ sur $[0,\sqrt n]$. L'intégrande est continue sur ce dernier segment. La formule de changement de variable donne
$$
\int_0^{\sqrt n}(1-x^2/n)^n\,dx
=\sqrt n\int_0^{\pi/2}(\cos^2u)^n\cos u\,du
=\boxed{\sqrt n\,W_{2n+1}}.
$$

> [!JURY]
> Le rapport demande de justifier que le changement de variable est de classe $C^1$. Identifiez aussi ses deux bornes et son sens de variation.

### Question 8

> [!INDICATION]
> Insérez l'équivalent de Q4 dans la limite fournie par Q6 et Q7. Traitez ensuite séparément l'intégrale sur chaque demi-droite.

#### Solution

Par les questions 4, 6 et 7, $I=\lim_{n\to+\infty}\sqrt n\,W_{2n+1}=\sqrt\pi/2$. La fonction $x\mapsto e^{-x^2}$ est paire. Les deux demi-intégrales convergent et sont égales. Ainsi
$$
\boxed{\begin{aligned}I&=\frac{\sqrt\pi}{2},\\J&=\sqrt\pi.\end{aligned}}
$$

## Partie II — Autour d'une équation différentielle

L'identification de coefficients traite le point singulier de l'équation. L'intégrale à paramètre donne un candidat que l'on ramène à la solution normalisée.

### II.A

### Question 9

> [!INDICATION]
> Examinez d'abord ce qu'implique littéralement le domaine écrit. Pour la lecture sur $\mathbb R$, écrivez les coefficients inconnus d'une série entière.

> [!INDICATION]
> Après identification, suivez séparément les indices pairs et impairs. Vérifiez rayon de convergence et réciproque.

#### Solution

L'énoncé imprime $\mathbb R[X]$.

Si l'on impose à $y$ d'être un polynôme non nul de degré $d$, le terme $xy$ a degré $d+1$, tandis que $xy''+y'$ a degré au plus $d-1$ s'il est non nul.

La seule solution polynomiale est donc nulle. Pour que la question 10 ait un sens, on cherche les solutions développables en série entière sur $\mathbb R$.

Si $y(x)=\sum_{k\ge0}a_kx^k$ a un rayon de convergence strictement positif, on peut dériver deux fois terme à terme à l'intérieur de son intervalle de convergence. L'identification des coefficients dans $xy''+y'+xy=0$ donne $a_1=0$ puis $(k+2)^2a_{k+2}+a_k=0$ pour $k\ge0$.

Tous les coefficients impairs sont nuls et, pour $m\ge0$, la récurrence donne $a_{2m}=(-1)^ma_0/(4^m(m!)^2)$.

Réciproquement, pour tout $a_0\in\mathbb R$, la série obtenue a un rayon infini. En effet, pour $x\ne0$, le rapport des modules de deux termes successifs de la série en $m$ sans son facteur $a_0$ vaut $|x|^2/(4(m+1)^2)\to0$.

Ses coefficients vérifient les relations ci-dessus. La dérivation terme à terme redonne donc l'équation sur $\mathbb R$. **Toutes les solutions demandées sont les fonctions suivantes, pour $a_0\in\mathbb R$**
$$
\boxed{y(x)=a_0\sum_{m=0}^\infty\frac{(-1)^m x^{2m}}{4^m(m!)^2}.}
$$

> [!JURY]
> Le rapport confirme la coquille $\mathbb R[X]$ en partie II. La lecture sur $\mathbb R$ explique pourquoi la solution normalisée peut exister.

### Question 10

> [!INDICATION]
> Dans la famille construite, quelle information sur les coefficients donne la valeur en zéro ?

#### Solution

Dans la famille de la question 9, $y(0)=a_0$. La condition choisit exactement $a_0=1$, d'où **l'existence et l'unicité** de
$$
\boxed{S(x)=\sum_{m=0}^\infty\frac{(-1)^m x^{2m}}{4^m(m!)^2}.}
$$

> [!PIEGE]
> Le coefficient de $y''$ s'annule en zéro. Le théorème usuel de Cauchy ne fournit donc pas cette unicité, même en ajoutant une condition sur $y'(0)$.

### II.B

### Question 11

> [!INDICATION]
> Identifiez la variable intégrée et le paramètre. Vérifiez les hypothèses du théorème jusqu'à l'ordre 2.

> [!INDICATION]
> Les facteurs trigonométriques permettent de trouver un même majorant intégrable sur le segment.

#### Solution

Pour tout $x$, $t\mapsto\cos(x\sin t)$ est continue et intégrable sur $[0,\pi]$. L'intégrande et ses deux dérivées partielles en $x$ sont continues sur $\mathbb R\times[0,\pi]$.

Les deux dérivées, $-\sin t\sin(x\sin t)$ et $-\sin^2t\cos(x\sin t)$, sont chacune majorées en module par $1$, intégrable sur ce segment et indépendant de $x$.

Par le théorème de dérivation des intégrales à paramètre, **$G$ est de classe $C^2$ sur $\mathbb R$** et
$$
\begin{aligned}
G'(x)&=-\frac1\pi\int_0^\pi\sin t\sin(x\sin t)\,dt, \\
G''(x)&=-\frac1\pi\int_0^\pi\sin^2t\cos(x\sin t)\,dt.
\end{aligned}
$$

> [!JURY]
> Le rapport signale une connaissance trop imprécise des théorèmes sur les intégrales à paramètre. Indiquez pour chaque ordre utilisé la régularité et un majorant indépendant du paramètre.

### Question 12

> [!INDICATION]
> Rassemblez sous la même intégrale les trois termes de l'équation.

> [!INDICATION]
> Cherchez une dérivée en $t$ d'un produit comprenant une fonction trigonométrique de $t$ et une fonction de $x\sin t$.

#### Solution

En utilisant les expressions de la question 11,
$$
\begin{aligned}
\pi\bigl(xG''(x)+G'(x)+xG(x)\bigr)
&=\int_0^\pi\bigl[x\cos^2t\cos(x\sin t)-\sin t\sin(x\sin t)\bigr]\,dt\\
&=[\cos t\sin(x\sin t)]_0^\pi=0.
\end{aligned}
$$
**$G$ satisfait l'équation sur $\mathbb R$, y compris en $0$.**

### Question 13

> [!INDICATION]
> Pour utiliser l'unicité de Q10, vérifiez toutes ses hypothèses.

> [!INDICATION]
> Développez le cosinus sous l'intégrale. Pour $x$ fixé, majorez chaque terme uniformément par une quantité qui ne dépend plus de $t$.

#### Solution

Pour tout $x\in\mathbb R$ fixé, la série du cosinus appliquée à $x\sin t$ converge uniformément en $t\in[0,\pi]$, car le module du terme d'indice $m$ est majoré par $|x|^{2m}/(2m)!$. On intègre terme à terme sur le segment. Cela donne
$$
G(x)=\sum_{m=0}^\infty
\left(\frac{(-1)^m}{\pi(2m)!}\int_0^\pi\sin^{2m}t\,dt\right)x^{2m}.
$$
Les coefficients sont indépendants de $x$ et cette série converge pour tout $x$ par la même majoration. Puisque $G(0)=1$ et que $G$ satisfait l'équation, la question 10 donne **$G=S$**.

> [!METHODE]
> Être solution et prendre la bonne valeur initiale suffit à appliquer Q10 seulement après avoir établi que $G$ appartient à la classe des fonctions développables en série entière.

## Partie III — Étude d'un endomorphisme sur un espace préhilbertien

La définition d'Hermite fournit à la fois un lien différentiel et une base orthogonale. On les combine pour obtenir les vecteurs propres, puis une seconde preuve de diagonalisabilité.

### III.A — Les polynômes d'Hermite

### Question 14

> [!INDICATION]
> Dérivez le poids gaussien en gardant à chaque étape le facteur exponentiel apparent.

#### Solution

Les trois premières dérivées de $e^{-x^2}$ sont, dans l'ordre, $-2xe^{-x^2}$, $(4x^2-2)e^{-x^2}$ et $(12x-8x^3)e^{-x^2}$. Après multiplication par $(-1)^ne^{x^2}$, on trouve
$$
\boxed{\begin{aligned}H_1(x)&=2x,\\H_2(x)&=4x^2-2,\\H_3(x)&=8x^3-12x.\end{aligned}}
$$

### Question 15

> [!INDICATION]
> Dérivez le produit qui définit $H_n$, puis identifiez le terme qui contient $w^{(n+1)}$.

#### Solution

La dérivation de la définition de $H_n$ donne
$$
H_n'(x)=2xH_n(x)+(-1)^ne^{x^2}w^{(n+1)}(x)
=2xH_n(x)-H_{n+1}(x).
$$
Ainsi **$H_{n+1}=2XH_n-H_n'$**.

### Question 16

> [!INDICATION]
> Transmettez simultanément le degré et la parité par récurrence.

> [!INDICATION]
> Dans la relation de Q15, comparez les degrés des deux termes et déterminez comment dérivation et multiplication par $X$ agissent sur la parité.

#### Solution

On raisonne par récurrence sur la propriété « $H_n$ est de degré $n$ et $H_n(-x)=(-1)^nH_n(x)$ ». Elle est vraie au rang $0$ puisque $H_0=1$.

Si elle est vraie au rang $n$, le terme $2XH_n$ a degré $n+1$ et $H_n'$ est nul ou de degré au plus $n-1$. La différence de la question 15 est donc de degré $n+1$.

De plus, $2XH_n$ a la parité opposée à celle de $H_n$. En dérivant $H_n(-x)=(-1)^nH_n(x)$, on obtient aussi $H_n'(-x)=(-1)^{n+1}H_n'(x)$. Donc $H_{n+1}$ a la parité de $n+1$.

**Pour tout $n$, $H_n$ est de degré $n$ et de la parité de $n$.**

> [!JURY]
> Le rapport attire l'attention sur les récurrences et sur les polynômes constants. Dans l'hérédité, isolez la possibilité que la dérivée soit nulle.

### Question 17

> [!INDICATION]
> Déterminez lequel des deux termes de la relation de Q15 peut contribuer à la plus haute puissance.

#### Solution

Si $c_n$ est le coefficient dominant de $H_n$, le terme de degré $n+1$ dans la question 15 provient de $2XH_n$. Donc $c_{n+1}=2c_n$ et $c_0=1$.

**Le coefficient dominant de $H_n$ est $2^n$.**

### III.B — Un produit scalaire

### Question 18

> [!INDICATION]
> Pour une combinaison linéaire, contrôlez le carré par une somme de carrés.

> [!INDICATION]
> Pour un polynôme, conservez une partie du poids sous la forme d'une gaussienne intégrable. Utilisez l'autre pour absorber la croissance du polynôme.

#### Solution

L'ensemble $E$ contient la fonction nulle. Pour $f,g\in E$ et $a,b\in\mathbb R$, $af+bg$ est continue et
$$
0\le(af+bg)^2e^{-x^2}\le2a^2 f^2 e^{-x^2}+2b^2 g^2 e^{-x^2}.
$$
Le majorant est intégrable, donc $E$ est un sous-espace de $C^0(\mathbb R,\mathbb R)$.

Pour tout polynôme $P$, $P^2e^{-x^2/2}$ est bornée par croissance comparée aux deux infinis et continuité. Il existe donc $C\ge0$ tel que $0\le P^2e^{-x^2}\le C e^{-x^2/2}$. Or $e^{-x^2/2}$ est intégrable par dilatation de l'intégrale de la question 8. **Ainsi $\mathbb R[X]\subset E$.**

> [!METHODE]
> L'espace ambiant naturel est celui des fonctions continues. La condition d'intégrabilité est précisément la propriété à préserver par combinaison linéaire.

### Question 19

> [!INDICATION]
> Avant de vérifier les axiomes, assurez-vous que le produit pondéré est intégrable.

> [!INDICATION]
> Une valeur non nulle de $f$ se propage sur tout un petit intervalle grâce à la continuité.

#### Solution

Si $f,g\in E$, la fonction $fge^{-x^2}$ est continue et $2|fg|e^{-x^2}\le(f^2+g^2)e^{-x^2}$. L'intégrale est donc absolument convergente. La symétrie résulte de $fg=gf$, et la bilinéarité, de la linéarité de l'intégrale dans chaque variable.

La forme est positive. Si $f$ prend une valeur non nulle en un point, la continuité de $f^2e^{-x^2}$ donne un segment de longueur positive sur lequel cette fonction est minorée par une constante strictement positive. Dans ce cas $\langle f,f\rangle>0$. **La forme est donc définie positive et constitue un produit scalaire sur $E$.**

> [!JURY]
> Le rapport demande de justifier l'existence de l'intégrale, de distinguer bilinéarité et linéarité et d'utiliser la continuité pour le caractère défini.

### III.C — Lien entre le produit scalaire et les polynômes d'Hermite

### Question 20

> [!INDICATION]
> Réécrivez le produit du poids et de $H_n$ à partir de sa définition.

> [!INDICATION]
> Sur un segment borné, transférez une dérivation au polynôme. Évaluez les limites du crochet grâce à Q16.

#### Solution

La définition donne $H_ne^{-x^2}=(-1)^nw^{(n)}$. Pour $n\ge1$, on intègre $Pw^{(n)}$ par parties sur $[-A,A]$. Le terme de bord tend vers zéro quand $A\to+\infty$ car, d'après la définition et la question 16, $Pw^{(n-1)}=(-1)^{n-1}PH_{n-1}e^{-x^2}$ tend vers zéro aux deux infinis. Les intégrales restantes convergent absolument par les questions 18 et 19. Par conséquent,
$$
\begin{aligned}
\langle P,H_n\rangle&=\frac{(-1)^n}{\sqrt\pi}\int_{\mathbb R}P(x)w^{(n)}(x)\,dx\\
&=\frac{(-1)^{n-1}}{\sqrt\pi}\int_{\mathbb R}P'(x)w^{(n-1)}(x)\,dx\\
&=\boxed{\langle P',H_{n-1}\rangle}.
\end{aligned}
$$

> [!JURY]
> Le rapport rappelle qu'une intégration par parties généralisée exige de contrôler les limites du crochet. En passant par $[-A,A]$, on voit explicitement où cette condition intervient.

### Question 21

> [!INDICATION]
> Itérez l'identité de Q20 jusqu'à ce que l'indice du polynôme d'Hermite s'annule.

#### Solution

En appliquant $n$ fois la question 20, $\langle P,H_n\rangle=\langle P^{(n)},H_0\rangle$. Si $P\in\mathbb R_{n-1}[X]$, $P^{(n)}=0$. Donc **$\langle P,H_n\rangle=0$**.

### Question 22

> [!INDICATION]
> Pour deux indices distincts, appliquez Q21 avec le plus grand indice.

> [!INDICATION]
> Pour passer de l'orthogonalité à une base, contrôlez les vecteurs non nuls et la dimension.

#### Solution

Si $i<j\le n$, on a $H_i\in\mathbb R_{j-1}[X]$ par la question 16, donc $\langle H_i,H_j\rangle=0$ par la question 21. Chaque $H_i$ est non nul puisqu'il est de degré $i$.

La famille orthogonale de $n+1$ vecteurs non nuls est libre dans l'espace de dimension $n+1$. **Elle en est une base orthogonale.**

> [!JURY]
> Le rapport souligne que la liberté d'une famille orthogonale suppose l'absence de vecteur nul. Le degré de $H_i$ justifie cette hypothèse.

### Question 23

> [!INDICATION]
> Commencez par écrire le carré de la norme sous forme de produit scalaire. Suivez l'effet des applications successives de Q20.

#### Solution

Pour $n\ge1$, on applique la question 20 successivement aux couples $(H_n,H_n),(H_n',H_{n-1}),\ldots,(H_n^{(n-1)},H_1)$. On obtient
$$
\boxed{\|H_n\|^2=\langle H_n^{(n)},H_0\rangle.}
$$
Pour $n=0$ l'égalité est immédiate.

### Question 24

> [!INDICATION]
> Calculez la dérivée d'ordre $n$ à partir du seul terme dominant et retrouvez la masse du poids dans la partie I.

#### Solution

Par la question 17, $H_n^{(n)}=2^n n!$. Or $H_0=1$ et $\langle1,1\rangle=J/\sqrt\pi=1$ par la question 8. De la question 23 on tire
$$
\boxed{\|H_n\|=\sqrt{2^n n!}.}
$$

### III.D — Étude d'un endomorphisme autoadjoint

### Question 25

> [!INDICATION]
> Décomposez $u$ en opérations linéaires. Examinez ce que chacune fait au degré.

#### Solution

La dérivation, la multiplication par $X$ et l'identité sont des applications linéaires de $\mathbb R[X]$ dans lui-même. Ainsi $u$ est linéaire.

Si $P\in\mathbb R_n[X]$, chacun des termes $-P''$, $2XP'$ et $P$ est de degré au plus $n$ lorsqu'il est non nul, ce qui inclut les cas des polynômes constants ou de faible degré.

**$\mathbb R_n[X]$ est stable par $u$.**

> [!PIEGE]
> Dans $\mathbb R_n[X]$, le degré peut être strictement inférieur à $n$. L'argument de stabilité traite également les dérivées nulles.

### Question 26

> [!INDICATION]
> Appliquez les deux compositions à un même polynôme. Dans laquelle des deux compositions faut-il dériver le produit $XP$ ?

#### Solution

En appliquant les compositions à un polynôme $P$,
$$
\begin{aligned}
(v\circ w)(P)&=2XP'-P''=u(P)-P, \\
(w\circ v)(P)&=(2XP-P')'=2P+2XP'-P''\\
&=u(P)+P.
\end{aligned}
$$
**$v\circ w=u-\mathrm{Id}$ et $w\circ v=u+\mathrm{Id}$.**

### Question 27

> [!INDICATION]
> Utilisez les deux réécritures de $u$ obtenues en Q26 et associez autrement les trois applications composées.

#### Solution

Grâce à la question 26 et à l'associativité de la composition,
$$
\begin{aligned}
u\circ v&=(v\circ w+\mathrm{Id})\circ v\\
&=v\circ(u+\mathrm{Id})+v\\&=v\circ u+2v.
\end{aligned}
$$
Donc **$u\circ v-v\circ u=2v$**.

> [!METHODE]
> Dans un calcul d'endomorphismes, on peut changer les parenthèses d'une composition. L'ordre des facteurs doit être conservé.

### Question 28

> [!INDICATION]
> Réécrivez $u\circ v$ grâce à la question précédente et faites passer le scalaire dans l'application linéaire.

#### Solution

Si $u(P)=\lambda P$, la question 27 et la linéarité de $v$ donnent
$$
u(v(P))=v(u(P))+2v(P)=\boxed{(\lambda+2)v(P)}.
$$

### Question 29

> [!INDICATION]
> Trouvez le premier polynôme propre par calcul direct.

> [!INDICATION]
> Interprétez la formule de Q15 en termes de l'endomorphisme $v$, puis utilisez Q28 pour l'hérédité.

#### Solution

On a $u(H_0)=H_0$, puisque $H_0=1$. Par la question 15, $v(H_k)=H_{k+1}$.

Si $u(H_k)=(2k+1)H_k$, la question 28 donne $u(H_{k+1})=(2k+3)H_{k+1}$. Par récurrence, la relation est vraie pour tout $k\ge0$.

Chaque $H_k$ est non nul d'après la question 16. **$H_k$ est donc vecteur propre de $u$ pour la valeur propre $2k+1$.**

### Question 30

> [!INDICATION]
> Réunissez le résultat de base de Q22 et les relations propres de Q29.

#### Solution

La base $(H_0,\dots,H_n)$ de $\mathbb R_n[X]$ donnée par la question 22 est faite de vecteurs propres de $u_n$ d'après la question 29. Sa matrice dans cette base a pour diagonale $(1,3,\ldots,2n+1)$. **$u_n$ est diagonalisable sur $\mathbb R$.**

### Question 31

> [!INDICATION]
> Dans l'intégrale de $P'Q'$ avec le poids, transférez la dérivée de $Q$ au produit de $P'$ par le poids.

> [!INDICATION]
> Examinez le crochet sur un segment borné avant de passer aux deux infinis.

#### Solution

En intégrant par parties sur $[-A,A]$, le terme de bord est $[P'Qe^{-x^2}]_{-A}^A$. Il tend vers zéro par croissance comparée aux deux infinis. Toutes les intégrales de produits de polynômes par le poids convergent absolument par les questions 18 et 19. Le passage à la limite donne
$$
\begin{aligned}
\langle P',Q'\rangle
&=-\frac1{\sqrt\pi}\int_{\mathbb R}(P''-2xP')Qe^{-x^2}\,dx\\
&=\boxed{\langle u(P),Q\rangle-\langle P,Q\rangle}.
\end{aligned}
$$

### Question 32

> [!INDICATION]
> Isolez le produit scalaire contenant $u_n$ et regardez la symétrie de l'autre membre.

#### Solution

Pour $P,Q\in\mathbb R_n[X]$, la question 31 donne $\langle u_n(P),Q\rangle=\langle P',Q'\rangle+\langle P,Q\rangle$. Le second membre est symétrique en $P,Q$. La symétrie du produit scalaire entraîne $\langle u_n(P),Q\rangle=\langle P,u_n(Q)\rangle$. **$u_n$ est autoadjoint.**

### Question 33

> [!INDICATION]
> Vérifiez les hypothèses du théorème spectral en précisant l'espace sur lequel il s'applique.

#### Solution

L'espace $\mathbb R_n[X]$, muni du produit scalaire de la question 19, est un espace euclidien car sa dimension est finie. L'endomorphisme $u_n$ est autoadjoint par la question 32. **Le théorème spectral fournit une base orthonormée de vecteurs propres de $u_n$ sur $\mathbb R$.**

> [!METHODE]
> Le théorème spectral s'applique ici à l'espace de dimension finie $\mathbb R_n[X]$, muni du produit scalaire étudié en partie III.

### Question 34

> [!INDICATION]
> Utilisez la base propre déjà connue et reprenez le calcul des normes de ses vecteurs.

#### Solution

Par les questions 22, 24 et 29, il suffit de normaliser chaque élément de la base orthogonale propre. Une base orthonormale cherchée est
$$
\boxed{\left(\frac{H_k}{\sqrt{2^k k!}}\right)_{0\le k\le n}.}
$$

## Partie IV — Une famille totale

Les coefficients de la transformée sont des intégrales de produits par des monômes. L'orthogonalité aux polynômes d'Hermite permettra de les annuler.

### Question 35

> [!INDICATION]
> Calculez d'abord le module de la phase complexe, puis partagez le poids entre deux facteurs.

> [!INDICATION]
> Pour l'intégrabilité, contrôlez le produit par une somme de carrés ou appliquez Cauchy-Schwarz sur des segments.

#### Solution

La seconde occurrence de $\xi$ dans l'énoncé désigne $f\in E$. Pour $f\in E$ et $\xi\in\mathbb R$, la fonction demandée est continue et
$$
|f(x)e^{-ix\xi}e^{-x^2}|=|f(x)|e^{-x^2}
\le \tfrac12\bigl(f(x)^2e^{-x^2}+e^{-x^2}\bigr).
$$
Le membre de droite est intégrable par définition de $E$ et par la question 8. **La fonction est absolument intégrable sur $\mathbb R$.**

### Question 36

> [!INDICATION]
> La croissance d'une puissance ne change pas la convergence face à une gaussienne.

> [!INDICATION]
> Isolez un facteur $x$ pour obtenir une dérivée du poids, puis exprimez l'intégrale en fonction du moment précédent.

#### Solution

Pour tout $p\ge0$, $x^{2p}e^{-x^2/2}$ est bornée par continuité et croissance comparée. La fonction continue positive $x^{2p}e^{-x^2}$ est donc intégrable par comparaison avec un multiple de $e^{-x^2/2}$. On a $M_0=\sqrt\pi$ par la question 8.

Pour $p\ge1$, comme $(e^{-x^2})'=-2xe^{-x^2}$, une intégration par parties sur $[-A,A]$ donne
$$
\int_{-A}^A x^{2p}e^{-x^2}\,dx
=\left[-\tfrac12 x^{2p-1}e^{-x^2}\right]_{-A}^A
+\frac{2p-1}{2}\int_{-A}^A x^{2p-2}e^{-x^2}\,dx.
$$
Le terme de bord tend vers zéro. On obtient $M_p=\frac{2p-1}{2}M_{p-1}$. En multipliant ces rapports et en séparant les facteurs pairs et impairs de $(2p)!$,
$$
\boxed{M_p=\sqrt\pi\,\frac{(2p)!}{4^p p!}\qquad(p\ge0).}
$$

> [!METHODE]
> Écrivez le facteur gaussien comme produit de deux facteurs gaussiens. Le premier absorbe le monôme et le second fournit une comparaison intégrable.

### Question 37

> [!INDICATION]
> Développez l'exponentielle complexe au point $-ix\xi$. Vérifiez que l'intégrande obtenu est celui dont l'intégrabilité vient d'être établie.

#### Solution

Pour tout $x$ réel et tout $\xi$ réel, la série de l'exponentielle donne
$$
f(x)e^{-x^2}\sum_{n=0}^\infty\frac{(-i)^n\xi^nx^n}{n!}
=f(x)e^{-x^2}e^{-ix\xi}.
$$
La somme des fonctions est intégrable par la question 35. On obtient donc l'identité demandée en intégrant cette égalité point par point. L'interversion de la série et de l'intégrale est justifiée à la question suivante.

> [!PIEGE]
> L'identité demandée garde la somme à l'intérieur de l'intégrale. Pour écrire une série de coefficients intégrés, vérifiez les hypothèses de Q38.

### Question 38

> [!INDICATION]
> Utilisez les moments de Q36 pour majorer l'intégrale du module de chaque terme de la série sous l'intégrale.

> [!INDICATION]
> Après Cauchy-Schwarz, comparez deux majorants successifs à l'aide de la relation de récurrence des moments.

#### Solution

Soit $B=\bigl(\int_{\mathbb R} f^2e^{-x^2}\bigr)^{1/2}$. Par Cauchy-Schwarz sur $[-A,A]$, puis par passage à la limite en utilisant la définition de $E$ et la question 36,
$$
\int_{\mathbb R}|x|^n|f(x)|e^{-x^2}\,dx\le B\sqrt{M_n}.
$$
En particulier, chaque terme de la série de la question 37 est intégrable. Pour $R>0$, la série de terme $b_n=R^n\sqrt{M_n}/n!$ converge puisque
$$
\frac{b_{n+1}}{b_n}=\frac{R}{n+1}\sqrt{\frac{2n+1}{2}}\longrightarrow0.
$$
Pour $|\xi|\le R$, la somme des intégrales des modules des termes de la question 37 est donc majorée par $B\sum b_n$. La somme des fonctions est continue par la question 37. Le théorème d'intégration terme à terme (appliqué aux parties réelle et imaginaire) donne
$$
\boxed{\mathcal F(f)(\xi)=\sum_{n=0}^\infty
\left(\frac{(-i)^n}{n!}\int_{\mathbb R}x^nf(x)e^{-x^2}\,dx\right)\xi^n.}
$$
Comme $R>0$ est arbitraire, la série entière obtenue a un rayon de convergence infini.

> [!METHODE]
> Une convergence ponctuelle du développement exponentiel ne donne pas à elle seule le passage sous l'intégrale. La série des intégrales des modules fournit le contrôle demandé.

### Question 39

> [!INDICATION]
> Placez le monôme dans une base d'un espace de polynômes de dimension finie adaptée à son degré.

#### Solution

Pour tout $n\ge0$, $X^n$ appartient à $\operatorname{Vect}(H_0,\dots,H_n)$ par la question 22. L'hypothèse d'orthogonalité implique $\langle X^n,f\rangle=0$. En multipliant par $\sqrt\pi$, on obtient **$\int_{\mathbb R} x^n f(x)e^{-x^2}\,dx=0$**.

### Question 40

> [!INDICATION]
> Identifiez le lien entre les intégrales de la question précédente et les coefficients calculés à Q38.

#### Solution

La question 39 annule chacun des coefficients de la série entière obtenue à la question 38. Cette série représente $\mathcal F(f)$ sur tout $\mathbb R$, donc **$\mathcal F(f)=0$**.

### Question 41

> [!INDICATION]
> Cherchez dans l'énoncé la propriété qui permet de remonter de la transformée à la fonction. Pensez à vérifier aussi l'inclusion de la fonction nulle dans l'orthogonal.

#### Solution

L'injectivité de $\mathcal F$ sur $E$ est admise dans l'énoncé. La question 40 donne donc $f=0$. La fonction nulle appartient à l'orthogonal, d'où $(\operatorname{Vect}(H_n,\ n\in\mathbb N))^\perp=\{0\}$. **La famille $(H_n)_{n\in\mathbb N}$ est totale dans $E$.**

> [!METHODE]
> Le sujet fournit l'injectivité de $\mathcal F$. Les questions précédentes préparent exactement son utilisation en établissant l'annulation de la transformée sur toute la droite.

## Bilan

- **D'un produit à un équivalent.** Un encadrement du quotient des termes voisins rend exploitable une identité sur leur produit. Cette étape évite d'utiliser un équivalent sans justification.
- **Utiliser l'unicité à bon escient.** Pour une équation dont le coefficient dominant s'annule, la récurrence sur les coefficients donne une méthode d'unicité dans une classe précise. Une représentation intégrale doit ensuite être reconnue comme appartenant à cette classe.
- **Construire et normaliser une base orthogonale.** Une intégration par parties transfère la dérivation. Les degrés, les termes de bord et la normalisation du poids ont chacun un rôle dans le résultat.
- **Développer une intégrale en série entière.** La série connue pour l'intégrande donne les coefficients attendus. L'intégration terme à terme exige un contrôle quantitatif, fourni ici par les moments du poids.
