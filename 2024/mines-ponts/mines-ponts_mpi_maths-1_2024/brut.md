# Mines-Ponts MPI — Mathématiques 1 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Calcul d’une intégrale

### Question 1

Le dénominateur ne peut s'annuler. En effet, $te^{i\theta}=-1$ imposerait $t=1$ et $e^{i\theta}=-1$, exclu sur $]-\pi,\pi[$. L'intégrande est donc continue pour $t>0$.

Pour $0<t\le1/2$, l'inégalité triangulaire inverse donne $|1+te^{i\theta}|\ge 1-t\ge1/2$.

Le module de l'intégrande est alors majoré par $2t^{x-1}$, intégrable près de zéro puisque $x>0$.

Pour $t\ge2$, on a $|1+te^{i\theta}|\ge t-1\ge t/2$.

Le module est au plus $2t^{x-2}$, intégrable à l'infini car $x<1$.

**L'intégrande est intégrable sur $]0,+\infty[$.**

### Question 2

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

### Question 3

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

### Question 4

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

### Question 5

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

Prolongeons l'intégrande de Q5 par zéro pour $u<\cot\theta$, ce qui donne une intégrale sur $\mathbb R$.

Quand $\theta\to\pi^-$, $\cot\theta\to-\infty$ et, pour tout $u$ fixé, $u\sin\theta-\cos\theta\to1$.

L'intégrande prolongé tend donc vers $(1+u^2)^{-1}$.

Sur son domaine non nul, sa base est positive ou nulle et majorée par $1+|u|$. Le majorant $(1+|u|)^x/(1+u^2)$ est continu et intégrable sur $\mathbb R$, puisqu'il est de l'ordre de $|u|^{x-2}$ à l'infini. Toutes les fonctions prolongées sont continues par morceaux. Par convergence dominée le long de toute suite $\theta\to\pi^-$,

$$
\boxed{\lim_{\theta\to\pi^-}g(\theta)\sin(x\theta)
=\int_{-\infty}^{+\infty}\frac{du}{1+u^2}.}
$$

### Question 7

L'intégrale de Q6 vaut $\pi$ par la primitive $\arctan$. Par Q3, $g(\theta)=g(0)=r(0)$. La continuité du sinus et $\sin(\pi x)>0$ donnent

$$
\boxed{\int_0^{+\infty}\frac{t^{x-1}}{1+t}\,dt
=\frac{\pi}{\sin(\pi x)}.}
$$

## Partie II — Une expression (utile) de la fonction sinus

### Question 8

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

Pour $N\ge0$, la formule géométrique finie donne sur $]0,1]$

$$
\frac{t^{x-1}}{1+t}=\sum_{k=0}^N(-1)^k t^{k+x-1}
+\frac{(-1)^{N+1}t^{N+x}}{1+t}.
$$

Chaque terme est intégrable en zéro puisque $x>0$. La valeur absolue de l'intégrale du reste est au plus $\int_0^1t^{N+x}\,dt=1/(N+x+1)$, qui tend vers zéro. On déduit

$$
\boxed{\int_0^1\frac{t^{x-1}}{1+t}\,dt=\sum_{k=0}^{+\infty}\frac{(-1)^k}{k+x}.}
$$

### Question 10

Puisque $1-x\in]0,1[$, on applique Q9 avec $x$ puis $1-x$ pour évaluer les deux intégrales de Q8. Chaque série converge d'après la preuve précédente. Ainsi,

$$
\boxed{\begin{aligned}
\int_0^{+\infty}\frac{t^{x-1}}{1+t}\,dt
&=\sum_{n=0}^{+\infty}\frac{(-1)^n}{n+x}\\
&\quad+\sum_{n=0}^{+\infty}\frac{(-1)^n}{n+1-x}.
\end{aligned}}
$$

### Question 11

Dans la seconde série de Q10, on décale l'indice d'une unité pour qu'il commence à $1$. On retire le terme $1/x$ de la première. Les deux séries restantes étant convergentes, on additionne leurs sommes partielles au même indice. Le terme d'indice $n\ge1$ vaut

$$
(-1)^n\left(\frac1{n+x}-\frac1{n-x}\right)
=-\frac{2(-1)^nx}{n^2-x^2}.
$$

D'après Q7, **la formule obtenue est**

$$
\boxed{\frac{\pi}{\sin(\pi x)}=\frac1x-\sum_{n=1}^{+\infty}\frac{2(-1)^nx}{n^2-x^2}.}
$$

### Question 12

Prenons $y\in]0,\pi[$ et posons $x=y/\pi$ dans Q11.

Après division par $\pi$, le terme d'indice $n$ s'écrit $2(-1)^ny/(y^2-n^2\pi^2)$ lorsqu'on inclut le signe de la soustraction.

On multiplie ensuite par $\sin y$ et on retranche le terme $\sin y/y$.

Ainsi,

$$
\boxed{\sum_{n=1}^{+\infty}\frac{2(-1)^n y\sin y}{y^2-n^2\pi^2}
=1-\frac{\sin y}{y}.}
$$

## Partie III — Calcul d’une intégrale de Dirichlet généralisée

### Question 13

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

### Question 14

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

On somme Q14 pour $n=1,\ldots,N$. Par Chasles, le membre de gauche devient l'intégrale de $\pi/2$ à $N\pi+\pi/2$, qui tend vers l'intégrale jusqu'à $+\infty$ d'après Q13.

Sur $[0,\pi/2]$, on a $|2t\sin t|\le\pi$ et $n^2\pi^2-t^2\ge(3/4)n^2\pi^2$. Le terme d'indice $n$ de la série de droite, même multiplié par $(\cos t)^{2p}$, est donc majoré uniformément en module par $4/(3\pi n^2)$. Les termes sont continus, et la série converge normalement, donc uniformément sur ce segment. On intègre terme à terme et on obtient

$$
\boxed{\begin{aligned}
\int_{\pi/2}^{+\infty}(\cos t)^{2p}\frac{\sin t}{t}\,dt
&=\int_0^{\pi/2}(\cos t)^{2p}
\sum_{n=1}^{+\infty}\frac{2(-1)^n t\sin t}{t^2-n^2\pi^2}\,dt .
\end{aligned}}
$$

### Question 16

Dans Q15, la série vaut $1-\sin t/t$ pour $0<t\le\pi/2$ par Q12.

Au point $0$, la formule s'étend par continuité, car la série est uniformément convergente et $\sin t/t\to1$.

On ajoute aux deux membres l'intégrale de $(\cos t)^{2p}\sin t/t$ de $0$ à $\pi/2$.

On trouve

$$
\boxed{\int_0^{+\infty}(\cos t)^{2p}\frac{\sin t}{t}\,dt
=\int_0^{\pi/2}(\cos t)^{2p}\,dt.}
$$

### Question 17

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

### Question 18

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

### Question 19

Chaque $X_k$ est d'espérance nulle par symétrie. Comme $X_k^2=1$ presque sûrement, sa variance vaut $1$. Par linéarité de l'espérance et additivité des variances pour des variables indépendantes,

$$
\boxed{\begin{aligned}
\mathbb E(S_n)&=0,\\
\operatorname{Var}(S_n)&=n.
\end{aligned}}
$$

### Question 20

On développe $\cos(S+T)=\cos S\cos T-\sin S\sin T$.

L'indépendance de $S$ et $T$ permet de factoriser l'espérance de chaque produit.

Comme $T$ et $-T$ sont de même loi et que le sinus est impair, $\mathbb E(\sin T)=-\mathbb E(\sin T)$, donc cette espérance est nulle.

On obtient **$\mathbb E(\cos(S+T))=\mathbb E(\cos S)\mathbb E(\cos T)$.**

### Question 21

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

### Question 23

Pour $s=0$, les deux membres sont nuls. Pour $s\ne0$, l'intégrande est bornée en zéro par le développement de $\cos(st)$ et majorée à l'infini par $2/t^2$. Elle est continue pour $t>0$, donc intégrable. Sur des bornes finies, le changement de variable $u=|s|t$ et la parité du cosinus donnent, après passage aux limites,

$$
\int_0^{+\infty}\frac{1-\cos(st)}{t^2}\,dt
=|s|\int_0^{+\infty}\frac{1-\cos u}{u^2}\,du .
$$

L'intégrale de droite vaut $\pi/2$ par Q18 pour $p=0$. **Le résultat est donc $\pi|s|/2$.**

### Question 24

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

### Question 25

Pour $n\ge1$, on applique Q24 au rang $2n-1$, puis Q18 avec $p=n-1$. Le facteur $\pi/2$ se simplifie et le dénominateur devient $2^{2n-2}((n-1)!)^2$. Par Q22, le même résultat vaut au rang $2n$. Finalement,

$$
\boxed{\mathbb E(|S_{2n}|)=\mathbb E(|S_{2n-1}|)
=\frac{(2n-1)!}{2^{2n-2}((n-1)!)^2}.}
$$
