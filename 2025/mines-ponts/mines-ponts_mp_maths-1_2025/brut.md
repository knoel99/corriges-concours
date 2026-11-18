# Mines-Ponts MP — Mathématiques 1 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Inégalité de Hölder

### Question 1

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

### Question 2

Si $\mathbb E(X^p)=0$ ou $\mathbb E(Y^q)=0$, la variable positive correspondante est nulle presque sûrement, donc $\mathbb E(XY)=0$.

Sinon, posons $A=\mathbb E(X^p)^{1/p}$ et $B=\mathbb E(Y^q)^{1/q}$.

On applique Q1 à $X/A$ et $Y/B$.

Par linéarité de l'espérance et définition de $A$ et $B$,

$$
\mathbb E\left(\frac{XY}{AB}\right)
\le \frac1p+\frac1q=1.
$$

En multipliant par $AB>0$, on obtient **$\mathbb E(XY)\le\mathbb E(X^p)^{1/p}\mathbb E(Y^q)^{1/q}$.**

### Question 3

On retrouve l'inégalité de Cauchy-Schwarz. Pour des variables réelles quelconques, prenons $P(t)=\mathbb E((X+tY)^2)$, qui est positif ou nul pour tout $t\in\mathbb R$. Si $\mathbb E(Y^2)=0$, alors $Y=0$ presque sûrement et l'inégalité est immédiate. Sinon, en développant,

$$
P(t)=\mathbb E(Y^2)t^2+2\mathbb E(XY)t+\mathbb E(X^2).
$$

Puisque ce trinôme est partout positif ou nul et de coefficient dominant strictement positif, son discriminant est négatif ou nul. Il en résulte

$$
\boxed{|\mathbb E(XY)|\le\mathbb E(X^2)^{1/2}\mathbb E(Y^2)^{1/2}.}
$$

## Une inégalité de déviation

### Question 4

Les développements en série entière, valables pour tout réel $t$, donnent

$$
\begin{aligned}
\operatorname{ch}(t)&=\sum_{j=0}^{+\infty}\frac{t^{2j}}{(2j)!},\\
e^{t^2/2}&=\sum_{j=0}^{+\infty}\frac{t^{2j}}{2^j j!}.
\end{aligned}
$$

Le produit des facteurs pairs de $(2j)!$ vaut $2^j j!$, et le produit des facteurs impairs est au moins $1$. Cette comparaison vaut aussi pour $j=0$, où les deux coefficients sont égaux. Comme chaque $t^{2j}$ est positif ou nul, **$\operatorname{ch}(t)\le e^{t^2/2}$**.

### Question 5

On écrit $S=\sum_{i=1}^n c_i X_i$ et $\sigma^2=\sum_{i=1}^n c_i^2$. Les variables $e^{tc_i X_i}$ sont indépendantes, comme fonctions des variables indépendantes $X_i$. La loi de Rademacher donne $\mathbb E(e^{tc_i X_i})=\operatorname{ch}(tc_i)$. Par indépendance puis par Q4,

$$
\begin{aligned}
\mathbb E(e^{tS})
&=\prod_{i=1}^n\operatorname{ch}(tc_i)\\
&\le \boxed{e^{t^2\sigma^2/2}}.
\end{aligned}
$$

### Question 6

Pour $x\ge0$, on a $e^{x|S|}=\max(e^{xS},e^{-xS})\le e^{xS}+e^{-xS}$.

Q5 appliquée aux coefficients $c_i$ puis $-c_i$ donne $\mathbb E(e^{x|S|})\le2e^{x^2\sigma^2/2}$.

La variable $e^{x|S|}$ est positive et intégrable, et le seuil $e^{tx}$ est strictement positif.

Par Markov,

$$
\boxed{\mathbb P(e^{x|S|}>e^{tx})\le 2e^{-tx}e^{x^2\sigma^2/2}.}
$$

### Question 7

Comme le vecteur des coefficients est non nul, $\sigma^2>0$.

Si $t=0$, la borne vaut $2$ et s'applique immédiatement.

Pour $t>0$, choisissons $x=t/\sigma^2>0$, qui minimise le trinôme $-tx+x^2\sigma^2/2$.

Par stricte croissance de l'exponentielle et positivité de $x$, l'événement $\{e^{x|S|}>e^{tx}\}$ est exactement $\{|S|>t\}$.

Q6 donne

$$
\boxed{\mathbb P(|S|>t)\le2\exp\left(-\frac{t^2}{2\sigma^2}\right).}
$$

## Inégalités de Khintchine

### Question 8

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

### Question 9

La fonction intégrée est continue sur $\mathbb R_+$. Entre $0$ et une borne finie, le changement de variable $u=t^2/2$ donne $t^3\,dt=2u\,du$. La primitive $-(u+1)e^{-u}$ de $ue^{-u}$ a une limite nulle à l'infini. Ainsi l'intégrale converge et

$$
\int_0^{+\infty} t^3e^{-t^2/2}\,dt
=2\int_0^{+\infty}ue^{-u}\,du=2.
$$

Si $\sigma^2=1$, on applique Q8 à $|S|$ avec $p=4$ et on majore sa probabilité de queue par Q7. On obtient

$$
\boxed{\mathbb E(S^4)\le 8\int_0^{+\infty} t^3e^{-t^2/2}\,dt=16.}
$$

### Question 10

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

Si $\sigma=0$, tous les coefficients sont nuls et l'inégalité est immédiate. Sinon, $Z=|S|/\sigma$ est une variable positive à valeurs finies. Q8 et Q7 donnent

$$
\mathbb E(Z^p)\le 2p\int_0^{+\infty}t^{p-1} e^{-t^2/2}\,dt.
$$

L'intégrande est continue sur $]0,+\infty[$ et bornée au voisinage de zéro. À l'infini, elle est $O(t^{-2})$ par croissance comparée. L'intégrale est donc finie et strictement positive. En prenant sa valeur multipliée par $2p$ à la puissance $1/p$ pour $\beta_p$, puis en réutilisant Q10,

$$
\boxed{\|S\|_p\le\beta_p\|S\|_2.}
$$

### Question 12

Pour $p=2$, on a l'égalité.

Pour $p>2$, Q2 appliquée à $|S|^2$ et à la constante $1$ avec les exposants conjugués $p/2$ et $p/(p-2)$ donne $\mathbb E(|S|^2)\le\mathbb E(|S|^p)^{2/p}$.

Ainsi **$\|S\|_2\le\|S\|_p$**.

### Question 13

Pour $1\le p<2$, on a $1/4<1/2<1/p$.

Il existe donc un unique coefficient $\theta\in]0,1[$ tel que $1/2=\theta/p+(1-\theta)/4$.

En isolant $\theta$, on trouve **$\theta=p/(4-p)$**, effectivement strictement compris entre $0$ et $1$.

### Question 14

On écrit $|S|^2=|S|^{2\theta}|S|^{2(1-\theta)}$. Les nombres $r=p/(2\theta)$ et $s=4/(2(1-\theta))$ sont conjugués, car $2\theta/p+2(1-\theta)/4=1$ par Q13. Leurs inverses sont strictement positifs, donc chacun est strictement supérieur à $1$. Q2 donne

$$
\boxed{\mathbb E(S^2)
\le\mathbb E(|S|^p)^{2\theta/p}\mathbb E(S^4)^{(1-\theta)/2}.}
$$

### Question 15

Si $\sigma=0$, l'inégalité est immédiate. Sinon, Q9 appliquée aux coefficients $c_i/\sigma$ donne $\mathbb E(S^4)\le16\sigma^4$, donc $\|S\|_4\le2\sigma$. Par Q10, $\sigma=\|S\|_2$. En prenant la racine carrée dans Q14,

$$
\|S\|_2\le\|S\|_p^\theta\,(2\|S\|_2)^{1-\theta}.
$$

On divise par $\|S\|_2^{1-\theta}>0$, puis on élève à la puissance $1/\theta$. On obtient **$\widetilde\alpha_p\|S\|_2\le\|S\|_p$** avec $\widetilde\alpha_p=2^{-(1-\theta)/\theta}>0$.

### Question 16

Pour $p\ge2$, Q12 donne l'inégalité avec $\alpha_p=1$. Pour $1\le p<2$, Q15 donne l'inégalité avec $\alpha_p=\widetilde\alpha_p$. **Dans tous les cas, $\alpha_p>0$ peut être choisie indépendamment des coefficients et du nombre de termes.**

## Une première conséquence

### Question 17

La linéarité de l'espérance et la commutativité du produit donnent la bilinéarité et la symétrie de $\varphi$. En outre, $\varphi(X,X)=\mathbb E(X^2)\ge0$. Si cette quantité est nulle, $X^2$ est nulle presque sûrement, donc $X=0$ selon l'identification de l'énoncé. L'espérance est inchangée si l'on modifie une variable sur un événement de probabilité nulle. **$\varphi$ est donc un produit scalaire.**

### Question 18

L'hypothèse d'une suite infinie indépendante est incompatible avec la finitude de $\Omega$.

Pour tout $m$, les $2^m$ configurations de signes des $m$ premières variables auraient chacune probabilité $2^{-m}$ et correspondraient donc à $2^m$ événements non vides et disjoints.

C'est impossible lorsque $2^m>|\Omega|$.

Le programme de MP admet l'existence d'un espace probabilisé portant une suite de variables indépendantes de lois discrètes données. On peut donc prendre un tel espace portant une suite de variables de Rademacher, et choisir comme espace d'arrivée les variables à valeurs finies modulo égalité presque sûre. L’identité démontrée ci-dessous vaut également sur l'espace fini initial pour toute famille indépendante finie, en restreignant les suites aux indices de cette famille. Dans les deux versions, la preuve de Q17 s'applique sur l'espace d'arrivée.

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

### Question 19

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

### Question 20

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

### Question 21

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
