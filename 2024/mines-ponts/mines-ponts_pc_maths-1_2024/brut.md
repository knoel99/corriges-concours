# Mines-Ponts PC — Mathématiques 1 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie 1 — Résultats préliminaires

### Question 1

Supposons $|f(x)|\leq\sum_{j=0}^d a_j|x|^j$. La somme reste un majorant si l’on remplace les $a_j$ par leurs valeurs absolues.

Sur $|x|\leq1$, chaque puissance $|x|^j$ est au plus 1. Sur $|x|\geq1$, elle est au plus $|x|^d$. En posant $C=1+\sum_{j=0}^d|a_j|$, on obtient
$$
|f(x)|\leq C(1+|x|^d)
$$
pour tout réel $x$. C’est la propriété de croissance lente.

### Question 2

Soit $f$ continue et à croissance lente. Le produit $f\varphi$ est continu et
$$
|f(x)\varphi(x)|\leq\frac{C}{\sqrt{2\pi}}(1+|x|^k)e^{-x^2/2}.
$$
Par croissance comparée, $|x|^2$ fois ce majorant tend vers zéro lorsque $|x|$ tend vers l’infini. Le produit $f\varphi$ est donc absolument intégrable aux deux infinis par comparaison à $1/x^2$, et aussi sur les segments par continuité. **Ainsi $f\in L^1(\varphi)$.**

### Question 3

Le sous-ensemble $CL(\mathbb R)$ contient la fonction nulle. Si $f,g$ sont à croissance lente, il existe des fonctions polynomiales en $|x|$, positives ou nulles, $A,B$ telles que $|f|\leq A$ et $|g|\leq B$.

Pour $\lambda,\mu\in\mathbb R$, on a $|\lambda f+\mu g|\leq |\lambda|A+|\mu|B$ et $|fg|\leq AB$. Les deux majorants sont des fonctions polynomiales en $|x|$. Par Q1, $CL(\mathbb R)$ est un sous-espace vectoriel de l’espace des fonctions réelles et est stable par produit.

### Question 4

Dans la suite, écrivons $a_t=e^{-t}$, $b_t=\sqrt{1-e^{-2t}}$ et $z_t(x,y)=a_tx+b_ty$. Pour tout $t\geq0$,
$$
|z_t(x,y)|\leq|x|+|y|.
$$
Si $f$ a pour majorant $C(1+|u|^k)$, on peut choisir $k\geq1$ en augmentant $C$ si nécessaire. L’inégalité $|x|+|y|\leq 2\max(|x|,|y|)$ donne
$$
|f(z_t(x,y))|\leq C\bigl(1+2^k|x|^k+2^k|y|^k\bigr).
$$
Pour $x$ fixé, la fonction de $y$ est continue et à croissance lente par Q1. La Q2 donne l’intégrabilité absolue après multiplication par $\varphi(y)$. La linéarité de l’intégrale s’applique à tous les points $x$, donc $P_t$ est linéaire sur $C^0(\mathbb R)\cap CL(\mathbb R)$.

### Question 5

Pour $x,y$ fixés, $z_t(x,y)$ tend vers $y$, car $a_t\to0$ et $b_t\to1$.

La continuité de $f$ donne la convergence de l’intégrande vers $f(y)\varphi(y)$.

Pour $x$ fixé, le majorant de Q4 multiplié par $\varphi(y)$ est intégrable en $y$ et indépendant de $t$. Pour toute suite de paramètres tendant vers l’infini, le théorème de convergence dominée donne donc la même limite. Par la caractérisation séquentielle admise dans l’énoncé,
$$
\lim_{t\to+\infty}P_t(f)(x)=\int_{\mathbb R} f(y)\varphi(y)\,\mathrm dy.
$$

### Question 6

À $t$ fixé, l’intégrande est continu en $x$ pour chaque $y$.

Sur un segment $|x|\leq R$, la borne de Q4 multipliée par $\varphi(y)$ est uniformément majorée par une fonction intégrable de $y$, en remplaçant $|x|^k$ par $R^k$.

Le théorème de continuité des intégrales à paramètre montre que $P_t(f)$ est continue sur tout segment, donc sur $\mathbb R$.

En intégrant la borne de Q4 sans restreindre $x$, et en utilisant $\int\varphi=1$, on obtient
$$
|P_t(f)(x)|\leq C\left(1+2^k|x|^k+2^k\int_{\mathbb R}|y|^k\varphi(y)\,\mathrm dy\right).
$$
Le moment gaussien est fini par Q2. Ce majorant est polynomial en $|x|$ et indépendant de $t$. Les Q1 et Q2 donnent alors **$P_t(f)\in L^1(\varphi)$**.

### Question 7

Comme $\varphi'(x)=-x\varphi(x)$, on a $(f'\varphi)'=L(f)\varphi$. Le produit $L(f)g$ est continu et à croissance lente par Q3, puisque la fonction identité, $f'$, $f''$ et $g$ le sont. Par Q2, le membre gauche est absolument convergent.

Sur $[u,v]$, une intégration par parties donne
$$
\int_u^v L(f)g\varphi
=[f'g\varphi]_u^v-\int_u^v f'g'\varphi.
$$
Le crochet tend vers zéro aux deux extrémités, car $f'g$ est à croissance lente et la gaussienne l’emporte sur toute puissance. En prenant séparément les limites à gauche et à droite, on obtient la convergence de l’intégrale impropre de $f'g'\varphi$ et l’identité
$$
\boxed{\int_{\mathbb R}L(f)g\varphi=-\int_{\mathbb R}f'g'\varphi.}
$$
L’intégrale de droite est ici prise au sens impropre.

## Partie 2 — Dérivée de $P_t(f)$

### Question 8

Pour $x$ fixé et $t>0$,
$$
\partial_t z_t(x,y)=-xa_t+\frac{a_t^2}{b_t}y.
$$
L’intégrande est de classe $C^1$ en $t$ et, par Q4, intégrable pour tout $t$.

Pour $t\in[\delta,T]$ avec $0<\delta<T$, on a $a_t\leq1$ et $b_t\geq b_\delta>0$.

La dérivée de l’intégrande est donc majorée en module par $(|x|+|y|/b_\delta)\varphi(y)$ multiplié par un majorant polynomial en $|y|$ de $|f'(z_t(x,y))|$, fourni par le calcul de Q4 appliqué à $f'$. Ce produit est intégrable par Q2. La dérivation sous l’intégrale s’applique localement sur $]0,+\infty[$. Elle donne la régularité $C^1$ et
$$
\partial_tP_t(f)(x)=\int_{\mathbb R}\left(-xa_t+\frac{a_t^2}{b_t}y\right)f'(z_t(x,y))\varphi(y)\,\mathrm dy.
$$

### Question 9

À $t$ fixé, $\partial_xz_t=a_t$ et l’intégrande est de classe $C^2$ en $x$.

Pour $x$ dans un segment, le calcul de Q4 appliqué à $f'$ puis à $f''$ borne en module les deux dérivées par des fonctions polynomiales en $|y|$ multipliées par $\varphi(y)$.

Les facteurs $a_t$ et $a_t^2$ sont au plus 1. Les majorants sont intégrables par Q2.

La dérivation sous l’intégrale donne la régularité $C^2$ et les deux identités
$$
\begin{aligned}
(P_t(f))'(x)&=a_t\int_{\mathbb R}f'(z_t(x,y))\varphi(y)\,\mathrm dy,\\
(P_t(f))''(x)&=a_t^2\int_{\mathbb R} f''(z_t(x,y))\varphi(y)\,\mathrm dy.
\end{aligned}
$$
Le raisonnement inclut $t=0$, pour lequel $b_t=0$.

### Question 10

Fixons $t>0$ et $x\in\mathbb R$. Comme $y\varphi(y)=-\varphi'(y)$, l’intégration par parties en $y$ donne
$$
\int_{\mathbb R}y f'(z_t(x,y))\varphi(y)\,\mathrm dy
=b_t\int_{\mathbb R} f''(z_t(x,y))\varphi(y)\,\mathrm dy.
$$
Les deux intégrales sont absolument convergentes par les majorations polynomiales de Q4 et Q2. Le terme de bord est nul par la domination de la gaussienne sur les puissances. Dans Q8, le terme en $-xa_t$ devient $-x(P_t(f))'(x)$ par Q9. Celui en $a_t^2/b_t$, après l’intégration par parties, devient $(P_t(f))''(x)$. D’où
$$
\boxed{\partial_tP_t(f)(x)=L(P_t(f))(x).}
$$

## Partie 3 — Inégalité de log-Sobolev pour la gaussienne

### Question 11

Pour $u>0$, posons $H(u)=u\ln u$. La dérivée $1+\ln u$ est négative sur $]0,e^{-1}[$ et positive sur $]e^{-1},+\infty[$.

La fonction décroît puis croît et atteint en $e^{-1}$ son minimum $-e^{-1}$. Elle tend vers $+\infty$ à l’infini.

Comme $u\ln u\to0$ quand $u\to0^+$, le choix $H(0)=0$ la prolonge continûment sur $\mathbb R_+$.

### Question 12

Si $0<u\leq1$, Q11 donne $|u\ln u|\leq e^{-1}$. Si $u\geq1$, alors $0\leq\ln u\leq u$, donc $|u\ln u|\leq u^2$. En particulier,
$$
|g(x)\ln g(x)|\leq e^{-1}+g(x)^2.
$$
Ce majorant est à croissance lente par Q3. La fonction $H\circ g$ est continue et à croissance lente par cette estimation. La Q2 assure alors que son produit avec $\varphi$ est absolument intégrable. **L’entropie est donc bien définie.**

### Question 13

La Q6 donne la continuité et, via Q1, la croissance lente de $P_t(f)$. Le produit $f(z_t(x,y))\varphi(y)$ est strictement positif et continu en $y$. Son intégrale est donc strictement positive pour tout $x$.

La propriété d’invariance admise après Q6 donne $\int_{\mathbb R}P_t(f)\varphi=\int_{\mathbb R}f\varphi=1$. La Q12 s’applique. Ainsi **$S(t)$ est bien définie pour tout $t\geq0$**.

### Question 14

Pour $x$ fixé, l’intégrande de $P_t(f)(x)$ est continu en $t\geq0$, y compris en zéro, car $a_t$ et $b_t$ sont continus.

Le majorant intégrable de Q4, indépendant de $t$, donne donc la continuité de $t\mapsto P_t(f)(x)$.

D’après Q6, il existe une fonction polynomiale positive ou nulle $M$ en $|x|$ telle que $|P_t(f)(x)|\leq M(x)$ pour tout $t\geq0$. La borne de Q12 donne
$$
|H(P_t(f)(x))\varphi(x)|\leq(e^{-1}+M(x)^2)\varphi(x).
$$
Ce majorant est intégrable par Q2. Pour chaque $x$, l’intégrande de $S$ est continu en $t$ par continuité de $H$ et de $P_t(f)(x)$.

Une seconde application du théorème de continuité des intégrales à paramètre donne **la continuité de $S$ sur $\mathbb R_+$**.

### Question 15

On a $z_0(x,y)=x$. Comme $\int\varphi=1$, on obtient $P_0(f)=f$, donc $S(0)=\operatorname{Ent}_\varphi(f)$.

Par Q5 et normalisation, $P_t(f)(x)\to1$ pour tout $x$. Par continuité de $H$, l’intégrande converge vers $H(1)\varphi(x)=0$. Le majorant de Q14 est intégrable et indépendant de $t$. Le théorème de convergence dominée appliqué le long de toute suite de paramètres tendant vers l’infini donne, par caractérisation séquentielle, **$S(t)\to0$**.

### Question 16

Les fonctions $f,f',f''$ sont à croissance lente et $f$ est de classe $C^2$. La Q10 s’applique donc à tout $t>0$. En remplaçant la dérivée dans l’expression admise, on trouve
$$
S'(t)=\int_{\mathbb R}L(P_t(f))(x)\bigl(1+\ln(P_t(f)(x))\bigr)\varphi(x)\,\mathrm dx.
$$

### Question 17

Écrivons $u=P_t(f)$, de classe $C^2$ par Q9 et strictement positive par Q13. La dérivée de $1+\ln u$ vaut $u'/u$. L’identité de Q7, autorisée pour ces fonctions par l’énoncé, donne à partir de Q16
$$
-S'(t)=\int_{\mathbb R}\frac{u'(x)^2}{u(x)}\varphi(x)\,\mathrm dx.
$$
Enfin Q9 donne $u'=e^{-t}P_t(f')$. D’où
$$
\boxed{-S'(t)=e^{-2t}\int_{\mathbb R}\frac{P_t(f')(x)^2}{P_t(f)(x)}\varphi(x)\,\mathrm dx.}
$$

### Question 18

Fixons $t>0$ et $x\in\mathbb R$, et écrivons $z=z_t(x,y)$. Appliquons l’inégalité intégrale de Cauchy–Schwarz aux fonctions $f'(z)\sqrt{\varphi(y)/f(z)}$ et $\sqrt{f(z)\varphi(y)}$.

Leurs carrés sont intégrables par Q4 appliquée à $f'^2/f$ et à $f$, qui sont continues et à croissance lente. Leur produit est $f'(z)\varphi(y)$, donc
$$
P_t(f')(x)^2\leq P_t(f'^2/f)(x)\,P_t(f)(x).
$$
Le dernier facteur est strictement positif par Q13. On divise par ce facteur et on intègre l’inégalité de fonctions contre $\varphi(x)\,\mathrm dx$. Le majorant est intégrable par Q6 appliquée à $f'^2/f$. La Q17 donne
$$
-S'(t)\leq e^{-2t}\int_{\mathbb R}P_t(f'^2/f)(x)\varphi(x)\,\mathrm dx.
$$

### Question 19

La fonction $h=f'^2/f$ est continue puisque $f$ est strictement positive, et elle est à croissance lente par hypothèse. L’invariance admise donne $\int_{\mathbb R}P_t(h)\varphi=\int_{\mathbb R}h\varphi$. Les deux intégrales sont finies par Q2 et Q6. En utilisant Q18, on obtient
$$
-S'(t)\leq e^{-2t}\int_{\mathbb R}\frac{f'(x)^2}{f(x)}\varphi(x)\,\mathrm dx.
$$

### Question 20

Posons $I=\int_{\mathbb R}(f'^2/f)\varphi$, qui est fini par Q2. Pour $0<\varepsilon<T$, la régularité de $S$ admise en Q16 et la borne de Q19 donnent
$$
S(\varepsilon)-S(T)\leq I\int_\varepsilon^T e^{-2t}\,\mathrm dt
=\frac I2\bigl(e^{-2\varepsilon}-e^{-2T}\bigr).
$$
Quand $\varepsilon\to0^+$, la Q14 donne $S(\varepsilon)\to S(0)$. Quand $T\to+\infty$, la Q15 donne $S(T)\to0$. Avec la valeur de $S(0)$, il vient
$$
\boxed{\operatorname{Ent}_\varphi(f)\leq\frac12\int_{\mathbb R}\frac{f'(x)^2}{f(x)}\varphi(x)\,\mathrm dx.}
$$
