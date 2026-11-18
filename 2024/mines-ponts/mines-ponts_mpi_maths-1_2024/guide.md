# Mines-Ponts MPI — Mathématiques 1 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Cette épreuve de trois heures, sans calculatrice, calcule une intégrale de Dirichlet généralisée puis utilise sa valeur pour déterminer l'espérance de la distance à l'origine d'une marche aléatoire symétrique.

| Partie | Questions | Outils et objectif |
|---|---|---|
| I | Q1–Q7 | Étudier une intégrale à paramètre complexe, en déduire une valeur exacte par convergence dominée. |
| II | Q8–Q12 | Développer une fraction en série géométrique et obtenir une expression du sinus utile pour le calcul suivant. |
| III | Q13–Q18 | Calculer l'intégrale de Dirichlet par intégration par parties, regroupement d'intervalles et développement du cosinus. |
| IV | Q19–Q25 | Utiliser l'indépendance et la parité pour obtenir un moment absolu d'une somme de signes. |

Les majorations décisives se trouvent en Q2, Q6 et Q15. Q9–Q10 demandent une autre méthode, fondée sur le contrôle du reste de la somme finie. La partie IV repart de résultats élémentaires de probabilités. On peut travailler Q19–Q22 sans avoir achevé le calcul des parties précédentes.

Chercher d'abord chaque question, puis ouvrir une indication si le calcul bloque. Pour les intégrales à paramètre, écrire sur le brouillon le domaine de la variable d'intégration et celui du paramètre avant de choisir un majorant.

## Partie I — Calcul d’une intégrale

On multiplie l'intégrale à paramètre par une exponentielle afin d'obtenir une fonction constante. Sa valeur se lit alors lorsque le paramètre approche la borne de son intervalle.

### Question 1

> [!INDICATION]
> Chercher quelles conditions imposerait l'annulation du dénominateur.

> [!INDICATION]
> Pour l'intégrabilité, comparez le module près de zéro et à l'infini. Le dénominateur n'a pas la même taille dans les deux zones.

#### Solution

Le dénominateur ne peut s'annuler. En effet, $te^{i\theta}=-1$ imposerait $t=1$ et $e^{i\theta}=-1$, exclu sur $]-\pi,\pi[$. L'intégrande est donc continue pour $t>0$.

Pour $0<t\le1/2$, l'inégalité triangulaire inverse donne $|1+te^{i\theta}|\ge 1-t\ge1/2$.

Le module de l'intégrande est alors majoré par $2t^{x-1}$, intégrable près de zéro puisque $x>0$.

Pour $t\ge2$, on a $|1+te^{i\theta}|\ge t-1\ge t/2$.

Le module est au plus $2t^{x-2}$, intégrable à l'infini car $x<1$.

**L'intégrande est intégrable sur $]0,+\infty[$.**

> [!JURY]
> Le rapport relève l'oubli de vérifier que le dénominateur ne s'annule pas et les comparaisons écrites entre nombres complexes. Les majorations s'appliquent au module.

### Question 2

> [!INDICATION]
> Dériver l'intégrande par rapport à l'angle, puis borner son module lorsque le paramètre reste dans un sous-intervalle fixé.

> [!INDICATION]
> Écrire le carré du module sous la forme $(1+t)^2-4t\sin^2(\theta/2)$. Comparez $4t$ à $(1+t)^2$.

#### Solution

Notons $F(\theta,t)=t^{x-1}/(1+te^{i\theta})$. Pour $t>0$, cette fonction est de classe $\mathcal C^1$ en $\theta$ et

$$
\frac{\partial F}{\partial\theta}(\theta,t)
=-\frac{ie^{i\theta}t^x}{(1+te^{i\theta})^2}.
$$

Soit $0<\beta<\pi$. Pour $|\theta|\le\beta$, on a $\cos\theta\ge\cos\beta$, d'où

$$
|1+te^{i\theta}|^2
\ge 1+2t\cos\beta+t^2
=(t+\cos\beta)^2+\sin^2\beta.
$$

De plus, puisque $4t\le(1+t)^2$,

$$
\begin{aligned}
1+2t\cos\beta+t^2
&=(1+t)^2-4t\sin^2(\beta/2)\\
&\ge (1+t)^2\cos^2(\beta/2).
\end{aligned}
$$

La dérivée partielle est donc majorée en module par $t^x/[(1+t)^2\cos^2(\beta/2)]$.

Ce majorant est intégrable, par comparaison à $t^x$ en zéro et à $t^{x-2}$ à l'infini.

Pour chaque $\theta$, $F(\theta,\cdot)$ est intégrable par Q1 et la dérivée partielle est continue en $t>0$.

Le théorème de dérivation des intégrales à paramètre s'applique sur $]-\beta,\beta[$, aux parties réelle et imaginaire.

Comme $\beta$ peut être choisi arbitrairement dans $]0,\pi[$, **$r$ est de classe $\mathcal C^1$ sur $]-\pi,\pi[$** et

$$
\boxed{r'(\theta)=-ie^{i\theta}\int_0^{+\infty}\frac{t^x}{(1+te^{i\theta})^2}\,dt.}
$$

> [!METHODE]
> Pour dériver une intégrale à paramètre, la domination peut être locale dans le paramètre. Ici on fixe un segment d'angles strictement à l'intérieur du domaine.

### Question 3

> [!INDICATION]
> Écrire $g$ comme un produit avec la fonction déjà dérivée en Q2.

> [!INDICATION]
> Vérifier que la combinaison des deux intégrandes correspond à une dérivée en $t$. Évaluer son intégrale entre deux bornes finies avant de passer aux limites.

#### Solution

D'après Q2, $g(\theta)=e^{ix\theta}r(\theta)$ est de classe $\mathcal C^1$. La dérivation du produit donne

$$
g'(\theta)=ie^{ix\theta}\int_0^{+\infty}
\left(\frac{xt^{x-1}}{1+te^{i\theta}}-\frac{e^{i\theta}t^x}{(1+te^{i\theta})^2}\right)dt.
$$

L'intégrande est $h'(t)$ par la règle du quotient et ses deux termes sont intégrables par Q1 et la domination de Q2.

Comme $x>0$, $h(t)\to0$ quand $t\to0^+$, donc $h(0)=0$ par prolongement.

À l'infini, $|h(t)|\le2t^{x-1}$ pour $t\ge2$, donc $h(t)\to0$.

On intègre $h'$ d'abord sur un segment, puis on passe aux limites.

L'intégrale vaut zéro.

**Ainsi $g'(\theta)=0$ et $g$ est constante.**

> [!JURY]
> Le rapport signale des applications superflues du théorème de dérivation sous l'intégrale. On a déjà calculé la dérivée de la fonction intégrale. La règle du produit suffit pour continuer.

### Question 4

> [!INDICATION]
> Utiliser la constance de $g$ pour faire apparaître le sinus par les exponentielles.

> [!INDICATION]
> Reconnaître ensuite dans le numérateur deux valeurs de $r$. Réduire la différence des fractions au même dénominateur.

#### Solution

Comme $g$ est constante, $g(-\theta)=g(\theta)$. La formule d'Euler donne alors

$$
\frac{g(-\theta)e^{ix\theta}-g(\theta)e^{-ix\theta}}{2i}
=g(\theta)\sin(x\theta).
$$

Par la définition de $g$, le numérateur à gauche est $r(-\theta)-r(\theta)$. Soustraire les deux intégrandes de Q1 est permis par leur intégrabilité. La différence des inverses des dénominateurs a pour numérateur $t(e^{i\theta}-e^{-i\theta})$ et pour dénominateur $1+2t\cos\theta+t^2$. On obtient

$$
\boxed{g(\theta)\sin(x\theta)
=\sin\theta\int_0^{+\infty}\frac{t^x}{t^2+2t\cos\theta+1}\,dt.}
$$

> [!JURY]
> Le rapport souligne que l'identité $g(-\theta)=g(\theta)$ doit apparaître. Elle est la conséquence de la constance prouvée en Q3.

### Question 5

> [!INDICATION]
> Compléter le carré dans le dénominateur de Q4.

> [!INDICATION]
> Choisir la nouvelle variable en divisant cette expression affine par le facteur trigonométrique strictement positif. Calculer la nouvelle borne inférieure.

#### Solution

Pour $0<\theta<\pi$, posons $u=(t+\cos\theta)/\sin\theta$.

C'est un changement de variable affine croissant.

Le dénominateur s'écrit $(t+\cos\theta)^2+\sin^2\theta$, soit $(1+u^2)\sin^2\theta$, et $dt=\sin\theta\,du$.

La borne $t=0$ devient $\cot\theta$.

En appliquant ce changement sur des segments puis en utilisant la convergence de l'intégrale de Q4,

$$
\boxed{g(\theta)\sin(x\theta)
=\int_{\cot\theta}^{+\infty}\frac{(u\sin\theta-\cos\theta)^x}{1+u^2}\,du.}
$$

### Question 6

> [!INDICATION]
> Définir toutes les intégrandes sur l'ensemble de la droite en ajoutant une indicatrice ou en prolongeant par zéro.

> [!INDICATION]
> Pour la domination, borner la base élevée à la puissance $x$ par une expression en $|u|$ seulement. Comparer son quotient avec une puissance intégrable à l'infini.

#### Solution

Prolongeons l'intégrande de Q5 par zéro pour $u<\cot\theta$, ce qui donne une intégrale sur $\mathbb R$.

Quand $\theta\to\pi^-$, $\cot\theta\to-\infty$ et, pour tout $u$ fixé, $u\sin\theta-\cos\theta\to1$.

L'intégrande prolongé tend donc vers $(1+u^2)^{-1}$.

Sur son domaine non nul, sa base est positive ou nulle et majorée par $1+|u|$. Le majorant $(1+|u|)^x/(1+u^2)$ est continu et intégrable sur $\mathbb R$, puisqu'il est de l'ordre de $|u|^{x-2}$ à l'infini. Toutes les fonctions prolongées sont continues par morceaux. Par convergence dominée le long de toute suite $\theta\to\pi^-$,

$$
\boxed{\lim_{\theta\to\pi^-}g(\theta)\sin(x\theta)
=\int_{-\infty}^{+\infty}\frac{du}{1+u^2}.}
$$

> [!METHODE]
> Quand les bornes dépendent d'un paramètre, travailler sur un domaine fixe permet d'appliquer le théorème de convergence dominée. Vérifier à la fois la limite du facteur de coupure et celle de l'intégrande.

### Question 7

> [!INDICATION]
> Évaluer la valeur constante de $g$ en zéro, puis revenir à la limite de Q6.

> [!INDICATION]
> Intégrer la fonction $(1+u^2)^{-1}$ à l'aide de sa primitive et préciser pourquoi $\sin(\pi x)$ ne s'annule pas.

#### Solution

L'intégrale de Q6 vaut $\pi$ par la primitive $\arctan$. Par Q3, $g(\theta)=g(0)=r(0)$. La continuité du sinus et $\sin(\pi x)>0$ donnent

$$
\boxed{\int_0^{+\infty}\frac{t^{x-1}}{1+t}\,dt
=\frac{\pi}{\sin(\pi x)}.}
$$

## Partie II — Une expression (utile) de la fonction sinus

Un changement de variable ramène toutes les intégrales à un segment. Le développement qui en résulte a une convergence alternée et nécessite un contrôle du reste avant l'intégration.

### Question 8

> [!INDICATION]
> Couper l'intégrale en deux à l'endroit où l'inversion $t\mapsto 1/t$ laisse le point fixe.

> [!INDICATION]
> Appliquer ce changement jusqu'à une borne finie et calculer la puissance qui reste après multiplication par le jacobien.

#### Solution

Par Chasles, on coupe l'intégrale de Q7 en $1$. Sur $[1,+\infty[$, on pose $u=1/t$. Pour une borne supérieure $R>1$, le facteur $dt=-du/u^2$ et le facteur $t^{x-1}/(1+t)=u^{2-x}/(1+u)$ donnent

$$
\int_1^R\frac{t^{x-1}}{1+t}\,dt=\int_{1/R}^1\frac{u^{-x}}{1+u}\,du.
$$

L'intégrande à droite est intégrable en zéro car $x<1$. On fait tendre $R$ vers l'infini, puis on ajoute l'intégrale sur $]0,1]$. Il en résulte

$$
\boxed{\int_0^{+\infty}\frac{t^{x-1}}{1+t}\,dt
=\int_0^1\frac{t^{x-1}+t^{-x}}{1+t}\,dt.}
$$

### Question 9

> [!INDICATION]
> Utiliser une somme géométrique finie avec reste.

> [!INDICATION]
> Intégrer le reste en valeur absolue en majorant le facteur provenant de son dénominateur. Éviter d'intervertir d'emblée les deux opérations.

#### Solution

Pour $N\ge0$, la formule géométrique finie donne sur $]0,1]$

$$
\frac{t^{x-1}}{1+t}=\sum_{k=0}^N(-1)^k t^{k+x-1}
+\frac{(-1)^{N+1}t^{N+x}}{1+t}.
$$

Chaque terme est intégrable en zéro puisque $x>0$. La valeur absolue de l'intégrale du reste est au plus $\int_0^1t^{N+x}\,dt=1/(N+x+1)$, qui tend vers zéro. On déduit

$$
\boxed{\int_0^1\frac{t^{x-1}}{1+t}\,dt=\sum_{k=0}^{+\infty}\frac{(-1)^k}{k+x}.}
$$

> [!JURY]
> Le rapport écarte l'inversion fondée sur la somme des intégrales des valeurs absolues, qui diverge ici. Le contrôle du reste permet de conclure sans hypothèse de convergence absolue de la série intégrée.

### Question 10

> [!INDICATION]
> Réutiliser Q9 pour les deux puissances identifiées en Q8.

> [!INDICATION]
> Vérifier que le nouvel exposant s'obtient avec un paramètre qui reste dans le domaine de Q9.

#### Solution

Puisque $1-x\in]0,1[$, on applique Q9 avec $x$ puis $1-x$ pour évaluer les deux intégrales de Q8. Chaque série converge d'après la preuve précédente. Ainsi,

$$
\boxed{\begin{aligned}
\int_0^{+\infty}\frac{t^{x-1}}{1+t}\,dt
&=\sum_{n=0}^{+\infty}\frac{(-1)^n}{n+x}\\
&\quad+\sum_{n=0}^{+\infty}\frac{(-1)^n}{n+1-x}.
\end{aligned}}
$$

### Question 11

> [!INDICATION]
> Mettre à part le terme de rang zéro de la première série et décaler l’indice de la seconde pour faire commencer les deux séries restantes au même rang.

> [!INDICATION]
> Regrouper ensuite les termes de même indice, en gardant le signe qui résulte du décalage de la seconde série.

#### Solution

Dans la seconde série de Q10, on décale l'indice d'une unité pour qu'il commence à $1$. On retire le terme $1/x$ de la première. Les deux séries restantes étant convergentes, on additionne leurs sommes partielles au même indice. Le terme d'indice $n\ge1$ vaut

$$
(-1)^n\left(\frac1{n+x}-\frac1{n-x}\right)
=-\frac{2(-1)^nx}{n^2-x^2}.
$$

D'après Q7, **la formule obtenue est**

$$
\boxed{\frac{\pi}{\sin(\pi x)}=\frac1x-\sum_{n=1}^{+\infty}\frac{2(-1)^nx}{n^2-x^2}.}
$$

> [!PIEGE]
> Les deux séries alternées convergent. Un décalage d'indice et une addition terme à terme de séries convergentes sont permis, avec traitement explicite du premier terme.

### Question 12

> [!INDICATION]
> Faire apparaître $y$ comme le produit $\pi x$ dans Q11.

> [!INDICATION]
> Après changement de variable, multiplier par le sinus et isoler la série.

#### Solution

Prenons $y\in]0,\pi[$ et posons $x=y/\pi$ dans Q11.

Après division par $\pi$, le terme d'indice $n$ s'écrit $2(-1)^ny/(y^2-n^2\pi^2)$ lorsqu'on inclut le signe de la soustraction.

On multiplie ensuite par $\sin y$ et on retranche le terme $\sin y/y$.

Ainsi,

$$
\boxed{\sum_{n=1}^{+\infty}\frac{2(-1)^n y\sin y}{y^2-n^2\pi^2}
=1-\frac{\sin y}{y}.}
$$

## Partie III — Calcul d’une intégrale de Dirichlet généralisée

Après une intégration par parties, on regroupe des intégrales sur des intervalles de longueur $\pi$. La série de la partie II permet de ramener le calcul à un seul segment.

### Question 13

> [!INDICATION]
> Étudier séparément les deux bornes, puis intégrer par parties sur un segment.

> [!INDICATION]
> Pour les termes de bord, contrôler le numérateur en zéro par un développement limité et à l'infini par sa bornitude.

#### Solution

Pour $p\in\mathbb N$, posons $U(t)=1-(\cos t)^{2p+1}$.

Au voisinage de zéro, $\cos t=1-t^2/2+o(t^2)$.

Par le développement de la puissance entière, $U(t)=((2p+1)/2)t^2+o(t^2)$.

L'intégrande $U(t)/t^2$ est donc bornée en zéro.

Elle est continue pour $t>0$ et au plus $2/t^2$ en valeur absolue à l'infini.

**L'intégrale converge absolument.**

Pour $0<\varepsilon<R$, une intégration par parties donne

$$
\int_\varepsilon^R\frac{U(t)}{t^2}\,dt
=\left[-\frac{U(t)}t\right]_\varepsilon^R
+(2p+1)\int_\varepsilon^R(\cos t)^{2p}\frac{\sin t}{t}\,dt.
$$

Le terme de bord tend vers zéro aux deux bornes, par le développement local et la bornitude de $U$. En fixant d'abord $R$ puis $\varepsilon$, on obtient séparément l'existence des limites de l'intégrale de droite en zéro et à l'infini. Au total,

$$
\boxed{\int_0^{+\infty}\frac{1-(\cos t)^{2p+1}}{t^2}\,dt
=(2p+1)\int_0^{+\infty}(\cos t)^{2p}\frac{\sin t}{t}\,dt.}
$$

> [!JURY]
> Le rapport insiste sur le terme de bord de l'intégration par parties. Le contrôler aux deux extrémités donne aussi la convergence de l'intégrale obtenue.

### Question 14

> [!INDICATION]
> Centrer l'intervalle au multiple de $\pi$ qui en est le milieu.

> [!INDICATION]
> Ramener l'intégrale de la partie négative à la partie positive. Examiner le signe du sinus et réduire au même dénominateur.

#### Solution

L'intervalle d'intégration est $[n\pi-\pi/2,n\pi+\pi/2]$. Posons $s=t-n\pi$. Alors $\cos(t)=(-1)^n\cos s$ et $\sin(t)=(-1)^n\sin s$. On obtient

$$
\int_{n\pi-\pi/2}^{n\pi+\pi/2}(\cos t)^{2p}\frac{\sin t}{t}\,dt
=(-1)^n\int_{-\pi/2}^{\pi/2}(\cos s)^{2p}\frac{\sin s}{n\pi+s}\,ds.
$$

En remplaçant $s$ par $-s$ sur la moitié négative, on additionne sur $[0,\pi/2]$ les deux contributions. La parité du cosinus et l'imparité du sinus font alors apparaître

$$
\frac1{n\pi+s}-\frac1{n\pi-s}=\frac{2s}{s^2-n^2\pi^2}.
$$

**On obtient ainsi le membre de droite demandé**, avec $s$ comme variable d'intégration.

### Question 15

> [!INDICATION]
> Sommer Q14 jusqu'à un rang fini. Les intervalles se rejoignent par Chasles.

> [!INDICATION]
> Sur $[0,\pi/2]$, comparer $n^2\pi^2-t^2$ à une fraction fixe de $n^2\pi^2$. Justifier ensuite l'intégration de la série.

#### Solution

On somme Q14 pour $n=1,\ldots,N$. Par Chasles, le membre de gauche devient l'intégrale de $\pi/2$ à $N\pi+\pi/2$, qui tend vers l'intégrale jusqu'à $+\infty$ d'après Q13.

Sur $[0,\pi/2]$, on a $|2t\sin t|\le\pi$ et $n^2\pi^2-t^2\ge(3/4)n^2\pi^2$. Le terme d'indice $n$ de la série de droite, même multiplié par $(\cos t)^{2p}$, est donc majoré uniformément en module par $4/(3\pi n^2)$. Les termes sont continus, et la série converge normalement, donc uniformément sur ce segment. On intègre terme à terme et on obtient

$$
\boxed{\begin{aligned}
\int_{\pi/2}^{+\infty}(\cos t)^{2p}\frac{\sin t}{t}\,dt
&=\int_0^{\pi/2}(\cos t)^{2p}
\sum_{n=1}^{+\infty}\frac{2(-1)^n t\sin t}{t^2-n^2\pi^2}\,dt .
\end{aligned}}
$$

> [!JURY]
> Le rapport distingue ce cas des questions 9–10. La série converge normalement sur le segment d'intégration, ce qui justifie ici l'interversion.

### Question 16

> [!INDICATION]
> Reconnaître la série de Q12 dans Q15.

> [!INDICATION]
> Ajouter la portion de l'intégrale comprise entre $0$ et $\pi/2$. Examiner le comportement de $\sin t/t$ au voisinage de zéro.

#### Solution

Dans Q15, la série vaut $1-\sin t/t$ pour $0<t\le\pi/2$ par Q12.

Au point $0$, la formule s'étend par continuité, car la série est uniformément convergente et $\sin t/t\to1$.

On ajoute aux deux membres l'intégrale de $(\cos t)^{2p}\sin t/t$ de $0$ à $\pi/2$.

On trouve

$$
\boxed{\int_0^{+\infty}(\cos t)^{2p}\frac{\sin t}{t}\,dt
=\int_0^{\pi/2}(\cos t)^{2p}\,dt.}
$$

### Question 17

> [!INDICATION]
> Appliquer le binôme à la somme d'exponentielles qui exprime le cosinus.

> [!INDICATION]
> Isoler le terme central. Regrouper les exponentielles des deux indices symétriques qui se conjuguent.

#### Solution

Écrivons $2\cos t=e^{it}+e^{-it}$. Par le binôme de Newton,

$$
2^{2p}(\cos t)^{2p}=\sum_{k=0}^{2p}\binom{2p}{k}e^{2i(p-k)t}.
$$

Le terme $k=p$ est constant. Pour $k<p$, le terme d'indice $2p-k$ a le même coefficient binomial et l'exponentielle conjuguée. En regroupant ces paires,

$$
\boxed{(\cos t)^{2p}
=2^{-2p}\left(\binom{2p}{p}
+2\sum_{k=0}^{p-1}\binom{2p}{k}\cos(2(p-k)t)\right).}
$$

Pour $p=0$, la somme est vide et l'identité donne $1$.

> [!METHODE]
> Les indices symétriques dans un développement binomial ont le même coefficient. Leur somme transforme les exponentielles conjuguées en cosinus.

### Question 18

> [!INDICATION]
> Intégrer Q17 sur $[0,\pi/2]$ et identifier les termes qui ont une intégrale nulle.

> [!INDICATION]
> Utiliser successivement Q16 et l'intégration par parties de Q13 pour revenir à l'intégrale demandée.

#### Solution

Pour $0\le k<p$, l'intégrale de $\cos(2(p-k)t)$ de $0$ à $\pi/2$ est nulle, car sa primitive donne le sinus de $(p-k)\pi$ au bord. Il reste dans Q17 le terme constant, et Q16 donne

$$
\int_0^{+\infty}(\cos t)^{2p}\frac{\sin t}{t}\,dt
=\frac{\pi}{2^{2p+1}}\binom{2p}{p}.
$$

On multiplie par $2p+1$ d'après Q13 et on développe le coefficient binomial. Ainsi,

$$
\boxed{\int_0^{+\infty}\frac{1-(\cos t)^{2p+1}}{t^2}\,dt
=\frac{\pi}{2}\frac{(2p+1)!}{2^{2p}(p!)^2}.}
$$

## Partie IV — Calcul de $\mathbb E(|S_n|)$

Les variables de signe sont indépendantes et symétriques. On relie une espérance trigonométrique à leur somme, puis on en déduit le moment absolu avec l'intégrale déjà calculée.

### Question 19

> [!INDICATION]
> Calculer les deux premiers moments d'une variable élémentaire, puis utiliser l'indépendance pour les variances.

#### Solution

Chaque $X_k$ est d'espérance nulle par symétrie. Comme $X_k^2=1$ presque sûrement, sa variance vaut $1$. Par linéarité de l'espérance et additivité des variances pour des variables indépendantes,

$$
\boxed{\begin{aligned}
\mathbb E(S_n)&=0,\\
\operatorname{Var}(S_n)&=n.
\end{aligned}}
$$

### Question 20

> [!INDICATION]
> Partir de la formule d'addition du cosinus et factoriser les espérances par indépendance.

> [!INDICATION]
> Utiliser la symétrie de $T$ pour examiner la contribution du sinus.

#### Solution

On développe $\cos(S+T)=\cos S\cos T-\sin S\sin T$.

L'indépendance de $S$ et $T$ permet de factoriser l'espérance de chaque produit.

Comme $T$ et $-T$ sont de même loi et que le sinus est impair, $\mathbb E(\sin T)=-\mathbb E(\sin T)$, donc cette espérance est nulle.

On obtient **$\mathbb E(\cos(S+T))=\mathbb E(\cos S)\mathbb E(\cos T)$.**

### Question 21

> [!INDICATION]
> Appliquer Q20 à la décomposition de $S_{n+1}$ en somme de deux termes.

> [!INDICATION]
> Vérifier le premier rang et expliquer pourquoi les deux nouveaux termes sont indépendants.

#### Solution

Pour $n=1$, $\mathbb E(\cos(tX_1))=\cos t$ puisque $\cos$ est paire.

Pour $n\ge1$, les variables $tS_n$ et $tX_{n+1}$ sont indépendantes par le lemme des coalitions.

Elles prennent un nombre fini de valeurs et $tX_{n+1}$ a une loi symétrique.

En utilisant Q20,

$$
\mathbb E(\cos(tS_{n+1}))
=\mathbb E(\cos(tS_n))\cos t.
$$

Par récurrence, **$\mathbb E(\cos(tS_n))=(\cos t)^n$ pour tout $t\in\mathbb R$ et tout $n\ge1$.**

### Question 22

> [!INDICATION]
> Distinguer les deux signes possibles de $a$ et vérifier lequel a $a+b$ sous l'hypothèse donnée.

> [!INDICATION]
> Pour l'application aux sommes, repérer leur parité au rang précédent et annuler le terme supplémentaire par indépendance.

#### Solution

Si $a>0$, alors $a+b\ge a-|b|\ge0$ et $|a+b|=a+b$. Si $a<0$, alors $a+b\le a+|b|\le0$ et $|a+b|=-a-b$. Dans les deux cas,

$$
\boxed{|a+b|=|a|+\operatorname{signe}(a)b.}
$$

La somme $S_{2n-1}$ est presque sûrement un entier impair, donc son module est au moins $1$.

On peut appliquer l'identité à $a=S_{2n-1}$ et $b=X_{2n}$, dont le module vaut $1$.

Par indépendance de $X_{2n}$ et de la fonction de $S_{2n-1}$, l'espérance de $\operatorname{signe}(S_{2n-1})X_{2n}$ est nulle, puisque $\mathbb E(X_{2n})=0$.

Ainsi,

$$
\boxed{\mathbb E(|S_{2n}|)=\mathbb E(|S_{2n-1}|).}
$$

> [!PIEGE]
> Une somme d'un nombre impair de signes ne peut s'annuler. C'est ce qui assure à la fois que son signe est défini et que l'inégalité numérique s'applique.

### Question 23

> [!INDICATION]
> Séparer le cas nul, puis utiliser la parité du cosinus pour choisir une échelle positive.

> [!INDICATION]
> Quelle valeur particulière de Q18 apparaît après changement de variable ?

#### Solution

Pour $s=0$, les deux membres sont nuls. Pour $s\ne0$, l'intégrande est bornée en zéro par le développement de $\cos(st)$ et majorée à l'infini par $2/t^2$. Elle est continue pour $t>0$, donc intégrable. Sur des bornes finies, le changement de variable $u=|s|t$ et la parité du cosinus donnent, après passage aux limites,

$$
\int_0^{+\infty}\frac{1-\cos(st)}{t^2}\,dt
=|s|\int_0^{+\infty}\frac{1-\cos u}{u^2}\,du .
$$

L'intégrale de droite vaut $\pi/2$ par Q18 pour $p=0$. **Le résultat est donc $\pi|s|/2$.**

### Question 24

> [!INDICATION]
> Appliquer Q23 aux valeurs possibles de la somme aléatoire, chacune pondérée par sa probabilité.

> [!INDICATION]
> La somme est finie. Reconnaître ensuite l'espérance qui permet d'utiliser Q21.

#### Solution

Soit $D_n$ l'ensemble fini des valeurs possibles de $S_n$ et $w_s=\mathbb P(S_n=s)$ pour $s\in D_n$. En multipliant Q23 par $w_s$ et en sommant, les intégrales se regroupent par linéarité, puisque la somme est finie et chaque intégrale converge.

$$
\begin{aligned}
\frac{\pi}{2}\mathbb E(|S_n|)
&=\int_0^{+\infty}\frac{\sum_{s\in D_n} w_s(1-\cos(st))}{t^2}\,dt\\
&=\int_0^{+\infty}\frac{1-\mathbb E(\cos(tS_n))}{t^2}\,dt.
\end{aligned}
$$

On utilise Q21 et on multiplie par $2/\pi$. Ainsi,

$$
\boxed{\mathbb E(|S_n|)
=\frac2\pi\int_0^{+\infty}\frac{1-(\cos t)^n}{t^2}\,dt.}
$$

> [!METHODE]
> Lorsque la variable prend un nombre fini de valeurs, la somme des intégrales pondérées par les probabilités se regroupe sous une seule intégrale par linéarité.

### Question 25

> [!INDICATION]
> Choisir un rang impair dans Q24 pour faire coïncider la puissance avec celle de Q18.

> [!INDICATION]
> Pour passer au rang pair, reprendre l'identité obtenue en Q22.

#### Solution

Pour $n\ge1$, on applique Q24 au rang $2n-1$, puis Q18 avec $p=n-1$. Le facteur $\pi/2$ se simplifie et le dénominateur devient $2^{2n-2}((n-1)!)^2$. Par Q22, le même résultat vaut au rang $2n$. Finalement,

$$
\boxed{\mathbb E(|S_{2n}|)=\mathbb E(|S_{2n-1}|)
=\frac{(2n-1)!}{2^{2n-2}((n-1)!)^2}.}
$$

## Bilan

- Pour une intégrale complexe ou à paramètre, étudier le module et poser un majorant valable sur un domaine fixe de paramètres.
- Pour une alternance géométrique au bord du domaine de convergence normale, écrire d'abord l'identité finie et intégrer le reste.
- Pour calculer une intégrale impropre après transformation, séparer convergence, justification des termes de bord et calcul sur un segment.
- Pour une somme de déplacements indépendants, l'espérance trigonométrique se factorise grâce à l'identité d'addition et à la symétrie.
- Refaire Q6, Q9 et Q15 ensemble pour distinguer convergence dominée, contrôle de reste et convergence normale.
