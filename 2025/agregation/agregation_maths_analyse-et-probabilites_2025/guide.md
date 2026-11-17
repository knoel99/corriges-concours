# Agrégation Maths — Analyse et probabilités 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*
## Présentation du sujet

**Cadre.** Épreuve de composition d'analyse et probabilités de l'agrégation externe de mathématiques, session 2025 : 6 heures, sans calculatrice ni document. Le problème comporte six parties et 28 questions, sur l'opérateur d'intégration (opérateur de Volterra) et le semi-groupe de Riemann–Liouville $(V_s)_{s>0}$ dans lequel il se plonge.

**Découpage et ce que fait chaque partie.**

- *Partie I (I.1–I.5)* : préliminaires indépendants — orthogonalité des cosinus, EDO du second ordre avec conditions au bord, théorème fondamental de l'analyse, adjoint et norme d'opérateur, opérateur diagonal sur un Hilbert.
- *Partie II (II.1–II.3)* : fonctions $\Gamma$ et $\mathrm{B}$ (définition, relation fonctionnelle, continuité, formule $\Gamma(s)\Gamma(s')=\mathrm{B}(s,s')\Gamma(s+s')$), puis équivalent des intégrales $I_n(\alpha)$ par intégration de contour.
- *Partie III (III.1–III.5)* : l'opérateur $J$ sur $C([0,1])$ — norme 1, injectif, spectre ponctuel vide, itérés explicites, compact (Ascoli).
- *Partie IV (IV.1–IV.5)* : le même opérateur $V$ sur $L^2(0,1)$ — adjoint, valeurs propres de $V^*\circ V$, base hilbertienne $(f_n)$, norme $\|V\|=2/\pi$.
- *Partie V (V.1–V.4)* : le semi-groupe $(V_s)_{s>0}$ — inégalité de convolution, continuité forte en $0$, loi de semi-groupe, compacité de chaque $V_s$.
- *Partie VI (VI.1–VI.6)* : classe de Hilbert–Schmidt — indépendance de la base, compacité, puis $V_s$ Hilbert–Schmidt $\iff s>1/2$ et nucléaire (somme absolument convergente de rang 1) $\iff s>1$.

**Notions du programme mobilisées.** Intégration (convergence dominée, continuité sous le signe somme, Fubini–Tonelli, changement de variable), équations différentielles (Cauchy–Lipschitz, ordre 2 à coefficients constants), analyse complexe (théorème de Cauchy, détermination principale du logarithme), espaces de Hilbert (base hilbertienne, Parseval, Bessel, adjoint, norme d'opérateur), compacité (Ascoli, limite uniforme de compacts, rang fini), convolution $L^1*L^p$, théorème de Weierstrass, fonctions $\Gamma$ et $\mathrm{B}$.

**Difficulté et longueur.** Sujet long (6 heures) et très guidé dans les parties I–IV ; les parties V–VI sont plus techniques (extraction diagonale, noyaux, séries d'opérateurs). Les questions discriminantes signalées par le rapport 2025 : I.5 (Pythagore sur une somme orthogonale), I.3.b (preuve du TFA), II.3.c (contour, log complexe), II.3.e (gestion des équivalents), III.5 (Ascoli), VI (partie entière). Rapport 2025 (p. 49) : « le jury est particulièrement attentif au soin et à la précision de la rédaction en début de sujet », et lire l'énoncé « évite des confusions dans la nature des objets (notamment entre $V$ et $J$ dans ce sujet) ».

**Questions à ne pas laisser passer.** I.1–I.5, II.1–II.2, III.1–III.3, IV.1–IV.2, IV.4–IV.5 et V.1–V.2 sont des questions « de cours » bien payées ; VI.1–VI.2 se traitent en admettant les résultats de V. La partie III se traite indépendamment de II.3.

**Gestion du temps.** Compter environ 1 h 15 sur les parties I–II (jusqu'à II.2), 1 h sur III, 1 h sur IV, 1 h 15 sur V, et garder 30–45 min pour VI en récoltant d'abord VI.1–VI.2.

## Partie I — Préliminaires

Cinq résultats indépendants, tous réutilisés ensuite : orthogonalité des cosinus, résolution d'une EDO avec conditions au bord, théorème fondamental de l'analyse, norme d'un opérateur et de son adjoint, norme d'un opérateur diagonal. C'est le début de sujet : le rapport y exige un soin particulier de rédaction.

### I.1

> [!INDICATION]
> Linéariser le produit de deux cosinus (formule produit-somme).

> [!INDICATION]
> Pour $k\in\mathbb Z^*$, que vaut $\int_0^1\cos(k\pi x)\,dx$ ? Et pour $k=0$ ? Ne pas oublier de traiter à part le cas $n=m$.

#### Solution

Pour tous $a,b\in\mathbb R$, $\cos a\cos b=\frac12\big(\cos(a+b)+\cos(a-b)\big)$, donc

$$

\cos\!\Big(\frac{(2n+1)\pi x}{2}\Big)\cos\!\Big(\frac{(2m+1)\pi x}{2}\Big)
=\frac12\Big(\cos\big((n+m+1)\pi x\big)+\cos\big((n-m)\pi x\big)\Big).

$$

Pour $k\in\mathbb Z^*$, $\int_0^1\cos(k\pi x)\,dx=0$, et pour $k=0$ cette intégrale vaut $1$. Comme $n+m+1\ge1$, le premier terme s'annule toujours ;
le second vaut $1$ si $n=m$, et $0$ sinon. Ainsi

$$
\boxed{\int_0^1\cos\!\Big(\frac{(2n+1)\pi x}{2}\Big)\cos\!\Big(\frac{(2m+1)\pi x}{2}\Big)\,dx=\frac12\,\delta_{n,m}.}
$$

> [!JURY]
> Rapport 2025 (p. 49) : « le calcul par double IPP a souvent été privilégié, mais le cas particulier $n=m$ a été fait complètement à part, lorsqu’il n’était pas oublié. »

### I.2

> [!INDICATION]
> (a) Écrire l'ensemble des zéros de $\cos$, puis ne garder que ceux qui sont strictement positifs.

> [!INDICATION]
> (b) Équation caractéristique de $\lambda g''+g=0$ ; imposer $g'(0)=0$ puis $g(1)=0$, et discuter selon que $\cos(1/\sqrt\lambda)$ s'annule ou non.

#### Solution

**(a)** On a $\cos t=0\iff t\in\{(k+\tfrac12)\pi:k\in\mathbb Z\}$. Comme $\lambda>0$, le réel $\frac{1}{\sqrt\lambda}$ est strictement positif, donc seuls les $k\in\mathbb N$ conviennent, c'est-à-dire

$$

\boxed{\lambda=\frac{4}{(2k+1)^2\pi^2}\quad(k\in\mathbb N).}

$$

**(b)** L'équation caractéristique de $\lambda g''+g=0$ est $\lambda r^2+1=0$, de racines $r=\pm\frac{i}{\sqrt\lambda}$, donc les solutions sont

$$

g(x)=a\cos\!\Big(\frac{x}{\sqrt\lambda}\Big)+b\sin\!\Big(\frac{x}{\sqrt\lambda}\Big),\qquad a,b\in\mathbb C.

$$

On a $g'(x)=\frac{1}{\sqrt\lambda}\big(-a\sin(\frac{x}{\sqrt\lambda})+b\cos(\frac{x}{\sqrt\lambda})\big)$, donc $g'(0)=0\iff b=0$. La condition $g(1)=0$ s'écrit alors $a\cos(\frac{1}{\sqrt\lambda})=0$. Notons $\lambda_k=\frac{4}{(2k+1)^2\pi^2}$. D'après (a) :
Si $\lambda=\lambda_k$ pour un $k\in\mathbb N$, alors

$$

\boxed{E_\lambda=\Big\{x\mapsto a\cos\!\Big(\frac{x}{\sqrt\lambda}\Big):a\in\mathbb C\Big\}}

$$

et sinon

$$

\boxed{E_\lambda=\{0\}.}

$$

> [!JURY]
> Rapport 2025 (p. 49) : « certains candidats n’ont pas vu que l’ensemble des solutions dépendait de $\lambda$. »

### I.3

> [!INDICATION]
> (a) C'est le théorème fondamental de l'analyse.

> [!INDICATION]
> (b) Majorer $\big|\frac{F(x)-F(x_0)}{x-x_0}-f(x_0)\big|$ par l'oscillation de $f$ sur le segment d'extrémités $x,x_0$, que la continuité rend arbitrairement petite.

#### Solution

**(a)** Pour tout $x\in[0,1]$,

$$
\boxed{F'(x)=f(x).}
$$

**(b)** Fixons $x_0\in[0,1]$. Pour $x\in[0,1]$, $x\neq x_0$, la relation de Chasles et $\int_{x_0}^x f(x_0)\,dt=(x-x_0)f(x_0)$ donnent

$$

\frac{F(x)-F(x_0)}{x-x_0}-f(x_0)=\frac{1}{x-x_0}\int_{x_0}^x\big(f(t)-f(x_0)\big)\,dt.

$$

Notons $I_{x,x_0}$ le segment d'extrémités $x$ et $x_0$. L'inégalité triangulaire intégrale donne, que $x>x_0$ ou $x<x_0$,

$$

\Big|\frac{F(x)-F(x_0)}{x-x_0}-f(x_0)\Big|\le\sup_{t\in I_{x,x_0}}|f(t)-f(x_0)|.

$$

Soit $\varepsilon>0$.
Par continuité de $f$ en $x_0$, il existe $\delta>0$ tel que $t\in\,]x_0-\delta,x_0+\delta[\,\cap[0,1]$ implique $|f(t)-f(x_0)|<\varepsilon$.
Alors, pour $x\in\,]x_0-\delta,x_0+\delta[\,\cap[0,1]$, tout $t\in I_{x,x_0}$ vérifie la même condition, donc le taux d'accroissement est majoré par $\varepsilon$.
Ainsi $F$ est dérivable en $x_0$ avec $F'(x_0)=f(x_0)$, et ceci pour tout $x_0\in[0,1]$ :

$$
\boxed{F\text{ est dérivable sur }[0,1]\text{ et }F'=f.}
$$

> [!PIEGE]
> $f$ est à valeurs complexes : si l’on invoque un théorème de la moyenne, il faut séparer partie réelle et partie imaginaire. Une réponse $F'=f-f(0)$ est fausse.

> [!JURY]
> Rapport 2025 (p. 49) : « trop de copies ont donné une réponse fausse (en indiquant $f-f(0)$) » ; pour la preuve, « elle était le plus souvent ignorée, ou fausse, ou simplement mal rédigée. »

### I.4

> [!INDICATION]
> (a) Écrire $\|T(x)\|_H^2$ comme un produit scalaire, puis faire passer l'adjoint et appliquer Cauchy–Schwarz.

> [!INDICATION]
> (b) Passer au sup sur la boule unité, utiliser la sous-multiplicativité de la norme d'opérateur, et conclure par symétrie en utilisant $(T^*)^*=T$.

#### Solution

**(a)** Pour $x\in H$,

$$

\|T(x)\|_H^2=\langle T(x),T(x)\rangle_H=\langle x,(T^*\circ T)(x)\rangle_H.

$$

L'inégalité de Cauchy–Schwarz donne alors

$$
\boxed{\|T(x)\|_H^2\le\|(T^*\circ T)(x)\|_H\,\|x\|_H.}
$$

**(b)** Pour $\|x\|_H\le1$, (a) donne $\|T(x)\|_H^2\le\|T^*\circ T\|$, donc par passage au sup sur la boule unité fermée,

$$
\|T\|^2\le\|T^*\circ T\|.
$$

La norme d'opérateur étant sous-multiplicative, $\|T\|^2\le\|T^*\|\,\|T\|$ ; si $\|T\|\neq0$, on simplifie en $\|T\|\le\|T^*\|$ (l'inégalité est triviale si $\|T\|=0$).
Comme $(T^*)^*=T$ (car $\langle h_1,(T^*)^*h_2\rangle=\langle T^*h_1,h_2\rangle=\langle h_1,Th_2\rangle$), appliquer cette inégalité à $T^*$ donne $\|T^*\|\le\|T\|$.
D'où $\|T^*\|=\|T\|$, puis en réinjectant dans la première inégalité $\|T\|^2\le\|T^*\circ T\|\le\|T^*\|\,\|T\|=\|T\|^2$ :

$$

\boxed{\|T^*\|=\|T\|}

$$

$$

\boxed{\|T^*\circ T\|=\|T\|^2.}

$$

> [!METHODE]
> À retenir en norme $C^*$ : $\|T^*\|=\|T\|$ et $\|T^*\circ T\|=\|T\|^2$, valables sur tout espace de Hilbert.

### I.5

> [!INDICATION]
> Sur $\mathrm{Vect}(b_n)$, calculer $\|D_\Lambda(x)\|_H^2$ grâce au théorème de Pythagore (famille orthonormée).

> [!INDICATION]
> Prolonger par densité (théorème de prolongement, $H$ complet) ; pour l'égalité de norme, minorer en évaluant sur chaque $b_n$.

#### Solution

Soit $x=\sum_{n=0}^N a_n b_n\in\mathrm{Vect}(b_n)$. Par linéarité, $D_\Lambda(x)=\sum_{n=0}^N a_n\lambda_n b_n$, et le théorème de Pythagore (famille $(b_n)$ orthonormée) donne

$$

\begin{aligned}
\|D_\Lambda(x)\|_H^2&=\sum_{n=0}^N|a_n|^2|\lambda_n|^2\\
&\le\|\Lambda\|_\infty^2\sum_{n=0}^N|a_n|^2\\
&=\|\Lambda\|_\infty^2\,\|x\|_H^2.
\end{aligned}

$$

Donc $D_\Lambda$ est continue sur $\mathrm{Vect}(b_n)$, à valeurs dans l'espace complet $H$ ;
comme ce sous-espace est dense ($\ (b_n)$ base hilbertienne), le théorème de prolongement fournit une unique application linéaire continue sur $H$, encore notée $D_\Lambda$, avec $\|D_\Lambda\|\le\|\Lambda\|_\infty$.
Réciproquement, pour tout $n$, $\|b_n\|_H=1$ donc

$$

\begin{aligned}
|\lambda_n|&=\|\lambda_n b_n\|_H\\
&=\|D_\Lambda(b_n)\|_H\\
&\le\|D_\Lambda\|,
\end{aligned}

$$

d'où $\|\Lambda\|_\infty\le\|D_\Lambda\|$ en passant au sup. Finalement

$$
\boxed{\text{\ }D_\Lambda\text{ se prolonge uniquement en une application continue et }\|D_\Lambda\|=\|\Lambda\|_\infty=\sup_{n\in\mathbb N}|\lambda_n|.}
$$

> [!PIEGE]
> Ne pas confondre somme $\ell^1$ et somme $\ell^2$ : c’est le théorème de Pythagore qui donne $\|\sum a_n\lambda_n b_n\|^2=\sum|a_n|^2|\lambda_n|^2$.

> [!JURY]
> Rapport 2025 (p. 49) : « de façon très surprenante, cette question a mis en grande difficulté une large majorité de candidats. Très souvent, expliciter la norme d’une somme de vecteurs orthogonaux n’était pas comprise (Pythagore ignoré) avec des confusions entre somme $\ell^1$ et somme $\ell^2$. »

## Partie II — Fonctions $\Gamma$ et $\mathrm{B}$

On définit et on étudie les fonctions $\Gamma$ et $\mathrm{B}$ (intégrabilité, relation fonctionnelle, continuité, lien entre elles), puis on obtient par analyse complexe un équivalent des intégrales $I_n(\alpha)$, qui servira en VI.3.

### II.1

> [!INDICATION]
> (a) Deux bornes à étudier séparément : $0^+$ (équivalent) et $+\infty$ (croissance comparée).

> [!INDICATION]
> (b) IPP sur $[\varepsilon,M]$ avec $u=t^s$, $v=-e^{-t}$, puis passer à la limite. (c) Récurrence. (d) Théorème de continuité sous le signe somme, avec une domination uniforme sur chaque segment $[a,b]$, scindée en $t<1$ et $t\ge1$.

#### Solution

**(a)** Soit $s>0$. La fonction $t\mapsto t^{s-1}e^{-t}$ est continue et positive sur $]0,+\infty[$.
Au voisinage de $0^+$, $t^{s-1}e^{-t}\sim t^{s-1}$ avec $s-1>-1$ : intégrable. Au voisinage de $+\infty$, $t^{s-1}e^{-t}=o(t^{-2})$ par croissance comparée : intégrable. Donc

$$
\boxed{\Gamma\text{ est bien définie sur }]0,+\infty[.}
$$

**(b)** Soit $s>0$ et $0<\varepsilon<M$. Avec $u(t)=t^s$ et $v(t)=-e^{-t}$, de classe $C^1$ sur $]0,+\infty[$, l'IPP donne

$$

\int_\varepsilon^M t^s e^{-t}\,dt=\Big[-t^s e^{-t}\Big]_\varepsilon^M+s\int_\varepsilon^M t^{s-1}e^{-t}\,dt.

$$

Or $\varepsilon^s e^{-\varepsilon}\to0$ (car $s>0$) et $M^s e^{-M}\to0$ (croissance comparée). En passant à la limite $\varepsilon\to0^+$, $M\to+\infty$ :

$$
\boxed{\Gamma(s+1)=s\,\Gamma(s).}
$$

**(c)** On a $\Gamma(1)=\int_0^{+\infty}e^{-t}\,dt=1=0!$. Si $\Gamma(n+1)=n!$, alors (b) donne $\Gamma(n+2)=(n+1)\Gamma(n+1)=(n+1)!$. Par récurrence :

$$
\boxed{\Gamma(n+1)=n!\qquad(n\in\mathbb N).}
$$

**(d)** Fixons $0<a<b<+\infty$. Pour $a\le s\le b$ : si $0<t<1$,

$$

0\le t^{s-1}e^{-t}\le t^{a-1}e^{-t},

$$

et si $t\ge1$ :

$$

0\le t^{s-1}e^{-t}\le t^{b-1}e^{-t},

$$

donc $0\le t^{s-1}e^{-t}\le t^{a-1}e^{-t}+t^{b-1}e^{-t}=:g(t)$, et $g$ est intégrable d'après (a).
Les hypothèses du théorème de continuité sous le signe somme étant vérifiées (continuité en $s$, mesurabilité en $t$, domination uniforme sur $[a,b]$), $\Gamma$ est continue sur $[a,b]$, pour tous $a<b$ :

$$
\boxed{\Gamma\text{ est continue sur }]0,+\infty[.}
$$

> [!JURY]
> Rapport 2025 (p. 49) : « on attendait au b. d’être prudent avec les bornes dans l’I.P.P. généralisée », « une rédaction propre de la récurrence était attendue » (c), et « dans ce cas précis, la domination a posé des difficultés » (d). Le jury ajoute : « le jury est particulièrement attentif au soin et à la précision de la rédaction en début de sujet. »

### II.2

> [!INDICATION]
> (a) Deux singularités : en $0$ et en $1$ (ne pas oublier la borne $1$).

> [!INDICATION]
> (b)(i) Montrer que $\varphi$ est bijective en explicitant sa réciproque, et vérifier que l'image est bien incluse dans l'ouvert d'arrivée. (ii) Fubini–Tonelli (positivité), changement de variable $(u,v)=\varphi(x,y)$ en calculant le jacobien, puis séparer les variables.

#### Solution

**(a)** Soient $s,s'>0$. La fonction $t\mapsto t^{s-1}(1-t)^{s'-1}$ est continue positive sur $]0,1[$.
En $0^+$, elle est équivalente à $t^{s-1}$, intégrable car $s-1>-1$.
En $1^-$, elle est équivalente à $(1-t)^{s'-1}$, intégrable car $s'-1>-1$. Donc

$$
\boxed{\mathrm{B}\text{ est bien définie sur }]0,+\infty[\times]0,+\infty[.}
$$

**(b)(i)** Pour $(x,y)\in\,]0,+\infty[\times]0,1[$ : $xy>0$ et $x(1-y)>0$, donc $\varphi(x,y)\in\,]0,+\infty[^2$ (l'image est bien incluse dans l'ouvert d'arrivée). Réciproquement, $\varphi(x,y)=(u,v)$ équivaut au système

$$

\begin{aligned}
xy&=u\\
x&=xy+v=u+v,
\end{aligned}

$$

soit $x=u+v$ et $y=\frac{u}{u+v}$, avec $u+v>0$ et $y\in\,]0,1[$. Donc $\varphi$ est bijective, de réciproque

$$

\varphi^{-1}(u,v)=\Big(u+v,\ \frac{u}{u+v}\Big).

$$

$\varphi$ est $C^1$ (composantes polynomiales) et $\varphi^{-1}$ est $C^1$ (composantes rationnelles, à dénominateur $u+v>0$ qui ne s'annule pas) :

$$
\boxed{\varphi\text{ est un }C^1\text{-difféomorphisme de }]0,+\infty[\times]0,1[\text{ sur }]0,+\infty[^2.}
$$

**(b)(ii)** Les intégrandes étant positifs, Fubini–Tonelli donne

$$

\Gamma(s)\Gamma(s')=\iint_{]0,+\infty[^2}u^{s-1}v^{s'-1}e^{-(u+v)}\,du\,dv.

$$

La matrice jacobienne de $\varphi$ en $(x,y)$ est $\begin{pmatrix}y&x\\1-y&-x\end{pmatrix}$, de déterminant $-xy-x(1-y)=-x$, donc $|\mathrm{Jac}\,\varphi(x,y)|=x$.
Par la formule de changement de variable $(u,v)=\varphi(x,y)$ (avec $u+v=x$) :

$$

\Gamma(s)\Gamma(s')=\iint_{]0,+\infty[\times]0,1[}(xy)^{s-1}\big(x(1-y)\big)^{s'-1}e^{-x}\,x\,dx\,dy.

$$

En développant, $(xy)^{s-1}\big(x(1-y)\big)^{s'-1}x=x^{s+s'-1}y^{s-1}(1-y)^{s'-1}$, donc par Fubini–Tonelli à nouveau (variables séparées) :

$$

\boxed{\Gamma(s)\Gamma(s')=\mathrm{B}(s,s')\,\Gamma(s+s').}
$$

> [!JURY]
> Rapport 2025 (p. 49) : « les candidats n’ont pas toujours vu en 2.a. qu’il fallait s’occuper (même rapidement) de la borne "1" », « le fait que l’image de $\varphi$ soit bien incluse dans $\mathbb R^{+\ast}\times\mathbb R^{+\ast}$ a souvent été oublié », « Le recours au théorème d’inversion local, souvent invoqué, était inutile et concrètement insuffisant tel quel », et « le changement de variable a été trop peu souvent explicité ».

### II.3

> [!INDICATION]
> (a) Primitive explicite ; simplifier $e^{-2i\pi n}$.

> [!INDICATION]
> (b) IPP généralisée (vérifier la limite en $0$), puis borner le terme intégral restant.

> [!INDICATION]
> (c) Appliquer le théorème de Cauchy sur $\mathbb C\setminus\mathbb R^-$ (ouvert étoilé) au lacet $C_\varepsilon$ ; paramétrer chaque morceau en calculant $\log$ directement sur ce morceau (pas de $\log(ab)=\log a+\log b$).

> [!INDICATION]
> (d) Majorer $|R_n(\alpha)|$, changer $\theta=-t$, et utiliser la concavité de $\sin$ sur $[0,\frac\pi2]$.

> [!INDICATION]
> (e) Combiner (c) et (d), faire le changement $v=2\pi nu$ dans l'intégrale restante, puis comparer les ordres de grandeur des restes ($\alpha+1<1$).

#### Solution

**(a)** Pour $n\ge1$, comme $e^{-2i\pi n}=1$,

$$

\begin{aligned}
I_n(0)&=\int_0^1 e^{-2i\pi nu}\,du\\
&=\Big[\frac{e^{-2i\pi nu}}{-2i\pi n}\Big]_0^1\\
&=0.
\end{aligned}

$$

$$
\boxed{I_n(0)=0.}
$$

**(b)** Soit $\alpha\in\,]0,1[$.
Les fonctions $u\mapsto u^\alpha$ et $u\mapsto e^{-2i\pi nu}$ sont $C^1$ sur $]0,1]$, et $u^\alpha e^{-2i\pi nu}\to0$ en $0^+$, donc l'IPP généralisée s'applique :

$$

I_n(\alpha)=-\frac{1}{2i\pi n}\Big[u^\alpha e^{-2i\pi nu}\Big]_0^1+\frac{\alpha}{2i\pi n}\int_0^1 u^{\alpha-1}e^{-2i\pi nu}\,du.

$$

Le crochet vaut $e^{-2i\pi n}-0=1$, donc

$$

I_n(\alpha)=-\frac{1}{2i\pi n}+\frac{\alpha}{2i\pi n}\,I_n(\alpha-1).

$$

Or $|I_n(\alpha-1)|\le\int_0^1 u^{\alpha-1}\,du=\frac1\alpha$ (car $|e^{-2i\pi nu}|=1$), d'où

$$
\boxed{I_n(\alpha)=O\!\Big(\frac1n\Big).}
$$

**(c)** Pour $z\in\mathbb C\setminus\mathbb R^-$, $\log z=\log|z|+i\,\arg_{]-\pi,\pi[}(z)$ ; la fonction $f(z)=\exp(\alpha\log z-2i\pi nz)$ est holomorphe sur l'ouvert étoilé $\mathbb C\setminus\mathbb R^-$, et le lacet $C_\varepsilon$ y est contenu.
Par le théorème de Cauchy, $\int_{C_\varepsilon}f(z)\,dz=0$, soit, en décomposant selon les quatre morceaux du contour ($q\gamma_\varepsilon$ est le chemin $\gamma_\varepsilon$ parcouru en sens inverse) :

$$

0=\int_{[1,\varepsilon]}f+\int_{q\gamma_\varepsilon}f+\int_{[-i\varepsilon,-i]}f+\int_{\gamma_1}f.

$$

*Segment $[1,\varepsilon]$* : sur $\mathbb R^{+*}$, $\log t$ est réel, donc

$$

\int_{[1,\varepsilon]}f=\int_1^\varepsilon t^\alpha e^{-2i\pi nt}\,dt=-\int_\varepsilon^1 t^\alpha e^{-2i\pi nt}\,dt.

$$

*Segment $[-i\varepsilon,-i]$* : pour $t>0$, $\log(-it)=\log t-\frac{i\pi}{2}$, donc, en paramétrant par $z=-it$,
$t$ de $\varepsilon$ à $1$, $dz=-i\,dt$ :

$$

\int_{[-i\varepsilon,-i]}f=-i\int_\varepsilon^1\exp\!\Big(\alpha\log t-\frac{i\alpha\pi}{2}-2\pi nt\Big)\,dt
=e^{-(\alpha+1)\frac{i\pi}{2}}\int_\varepsilon^1 t^\alpha e^{-2\pi nt}\,dt.

$$

*Arcs $\gamma_r$* : en paramétrant par $z=re^{i\theta}$, $\theta\in[-\frac\pi2,0]$, où $\log(re^{i\theta})=\log r+i\theta$ et $dz=ire^{i\theta}d\theta$ :

$$

\int_{\gamma_r}f=i r\int_{-\pi/2}^0\exp\!\Big(\alpha\log r+i\alpha\theta-2i\pi n re^{i\theta}+i\theta\Big)\,d\theta.

$$

En reportant dans l'égalité de Cauchy et en faisant $\varepsilon\to0^+$ : les intégrales sur les segments tendent vers $I_n(\alpha)$ et $\int_0^1 t^\alpha e^{-2\pi nt}\,dt$ (convergence car $|t^\alpha e^{-2i\pi nt}|=t^\alpha$ est intégrable, $\alpha>-1$) ;
la contribution de $\gamma_\varepsilon$ tend vers $0$, car pour $\theta\in[-\frac\pi2,0]$ on a $\sin\theta\le0$ donc

$$

\Big|i\varepsilon\int_{-\pi/2}^0\exp\!\Big(\alpha\log\varepsilon+i\alpha\theta-2i\pi n\varepsilon e^{i\theta}+i\theta\Big)d\theta\Big|
\le\frac\pi2\,\varepsilon^{\alpha+1}\xrightarrow[\varepsilon\to0^+]{}0

$$

(car $\alpha+1>0$). On obtient finalement

$$

\boxed{I_n(\alpha)=e^{-(\alpha+1)\frac{i\pi}{2}}\int_0^1 u^\alpha e^{-2\pi nu}\,du+R_n(\alpha),
R_n(\alpha)=i\int_{-\pi/2}^0\exp\!\Big(-2i\pi n e^{i\theta}+i(\alpha+1)\theta\Big)\,d\theta.}
$$

**(d)** Comme $|\exp(-2i\pi ne^{i\theta}+i(\alpha+1)\theta)|=e^{2\pi n\sin\theta}$, on a

$$

|R_n(\alpha)|\le\int_{-\pi/2}^0 e^{2\pi n\sin\theta}\,d\theta.

$$

Le changement $\theta=-t$ donne

$$

|R_n(\alpha)|\le\int_0^{\pi/2}e^{-2\pi n\sin t}\,dt.

$$

Sur $[0,\frac\pi2]$, $\sin$ est concave, donc au-dessus de sa corde : $\sin t\ge\frac{2}{\pi}t$. D'où

$$

\begin{aligned}
|R_n(\alpha)|&\le\int_0^{\pi/2}e^{-4nt}\,dt\\
&=\frac{1-e^{-2n\pi}}{4n}\\
&\le\frac{1}{4n},
\end{aligned}

$$

$$
\boxed{R_n(\alpha)=O\!\Big(\frac1n\Big).}
$$

**(e)** Par (c) et (d), puis le changement $v=2\pi nu$ :

$$

\int_0^1 u^\alpha e^{-2\pi nu}\,du=\frac{1}{(2\pi n)^{\alpha+1}}\int_0^{2\pi n}v^\alpha e^{-v}\,dv
=\frac{\Gamma(\alpha+1)+o(1)}{(2\pi n)^{\alpha+1}}.

$$

Donc

$$

I_n(\alpha)=\frac{\Gamma(\alpha+1)\,e^{-(\alpha+1)\frac{i\pi}{2}}}{(2\pi n)^{\alpha+1}}+o\!\Big(\frac{1}{n^{\alpha+1}}\Big)+O\!\Big(\frac1n\Big).

$$

Pour $-1<\alpha<0$, on a $\alpha+1<1$, donc $\frac1n=o\big(\frac{1}{n^{\alpha+1}}\big)$ : le terme $O(1/n)$ est absorbé par le $o(1/n^{\alpha+1})$. Ainsi

$$
\boxed{I_n(\alpha)\underset{n\to+\infty}{\sim}\frac{\Gamma(\alpha+1)}{(2\pi n)^{\alpha+1}}\,e^{-(\alpha+1)\frac{i\pi}{2}}\qquad(-1<\alpha<0).}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « beaucoup trop de candidats ne simplifient pas $\exp(2in\pi)$ » (a, b) ; pour le contour (c) : « le log complexe est manipulé sans aucune précaution (en particulier attention au log d’un produit !), les hypothèses de la formule de Cauchy, notamment la nature du domaine, ne sont pas mentionnées » et « cette question est très rarement correctement traitée » ; pour (e) : « la gestion des équivalents et des comparaisons a été en général fragile. »

## Partie III — L'opérateur d'intégration sur $C([0,1])$

On étudie l'opérateur de Volterra $J$ sur $C([0,1])$ : continuité, norme, injectivité, spectre ponctuel vide, itérés explicites par Taylor, et compacité par Ascoli.

### III.1

> [!INDICATION]
> (a) $J(f)$ est dérivable (I.3.b) ; pour la norme, majorer $|J(f)(x)|$ par $x\|f\|_\infty$ et exhiber une fonction réalisant l'égalité. (b) Si $J(f)=0$, dériver. (c) Toute image de $J$ s'annule en $0$.

#### Solution

**(a)** Pour $f\in C([0,1])$, $J(f)$ est dérivable sur $[0,1]$ de dérivée $f$ (I.3.b), donc $J(f)\in C([0,1])$ ;
$J$ est linéaire par linéarité de l'intégrale. De plus, pour tout $x\in[0,1]$,

$$

\begin{aligned}
|J(f)(x)|&\le\int_0^x|f(t)|\,dt\\
&\le x\,\|f\|_\infty\\
&\le\|f\|_\infty,
\end{aligned}

$$

donc $\|J(f)\|_\infty\le\|f\|_\infty$ et $\|J\|\le1$.
Pour $f\equiv1$ (notée $p_0$), $\|p_0\|_\infty=1$ et $J(p_0)(x)=x$, donc $\|J(p_0)\|_\infty=1$. D'où

$$
\boxed{J:C([0,1])\to C([0,1])\text{ est linéaire continue et }\|J\|=1.}
$$

**(b)** Si $J(f)=0$, alors $f=(J(f))'=0$ d'après I.3.b (attention : $f$ est à valeurs complexes, on ne peut pas conclure directement d'une intégrale nulle). Donc

$$
\boxed{\ker J=\{0\},\quad J\text{ est injective.}}
$$

**(c)** Pour toute $f\in C([0,1])$, $J(f)(0)=0$.
Or la fonction constante égale à $1$ appartient à $C([0,1])$ et vaut $1$ en $0$ : elle n'est pas dans l'image de $J$. Donc

$$
\boxed{J\text{ n'est pas surjective.}}
$$

> [!JURY]
> Rapport 2025 (p. 50) : pour l’injectivité, « certains candidats ont affirmé que, si l’intégrale d’une fonction continue est nulle alors cette fonction est nulle » — ce qui est faux ici, $f$ étant à valeurs complexes a priori. Passer par la dérivée $f=(J(f))'$.

### III.2

> [!INDICATION]
> Écrire $f=\frac1\lambda J(f)$ : on gagne une dérivabilité par « bootstrap », et $f'=\frac1\lambda f$.

#### Solution

Soit $\lambda\in\mathbb C^*$, $f\in C([0,1])$ avec $J(f)=\lambda f$. Alors $f=\frac1\lambda J(f)$.
Par I.3.b, $J(f)$ est dérivable de dérivée $f$, donc $f$ est dérivable et

$$

f'=\frac1\lambda (J(f))'=\frac1\lambda f.

$$

Comme $f$ est continue, $f'$ l'est aussi, donc $f\in C^1([0,1])$ :

$$
\boxed{f\in C^1([0,1])\text{ et }f\text{ est solution de }y'=\frac1\lambda y.}
$$

### III.3

> [!INDICATION]
> $\lambda=0$ est exclu par l'injectivité. Pour $\lambda\neq0$, résoudre l'EDO $y'=\frac1\lambda y$ et utiliser la condition au bord $f(0)=0$ (car $J(f)(0)=0$).

#### Solution

Soit $\lambda$ une valeur propre de $J$ : il existe $f\neq0$ avec $J(f)=\lambda f$.
Si $\lambda=0$, l'injectivité (III.1.b) donne $f=0$, absurde. Si $\lambda\neq0$, III.2 donne $f(x)=ke^{x/\lambda}$ pour un $k\in\mathbb C$.
Mais $J(f)(0)=0$ impose $f(0)=\frac1\lambda J(f)(0)=0$, donc $k=0$ et $f=0$, absurde. Ainsi

$$
\boxed{\sigma_p(J)=\varnothing.}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « beaucoup de candidats ont oublié que $f$ devait s’annuler en $0$ » et ont conclu $\sigma_p(J)=\mathbb C\setminus\{0\}$.

### III.4

> [!INDICATION]
> (a) Récurrence sur $n$, avec le fait que $(J^{n+1}(f))'=J^n(f)$. (b) Utiliser $J(g)(0)=0$. (c) Appliquer la formule de Taylor avec reste intégral à l'ordre $n$ à $J^n(f)$, en annulant les termes de bord.

#### Solution

**(a)** Montrons par récurrence sur $n$ la propriété $\mathcal P_n$ : « $J^n(f)\in C^n([0,1])$ et $(J^n(f))^{(k)}=J^{n-k}(f)$ pour tout $0\le k\le n$ ».
Pour $n=0$ : $J^0(f)=f\in C^0$ et $(J^0(f))^{(0)}=f=J^0(f)$.
Si $\mathcal P_n$ est vraie, alors $J^n(f)\in C^n\subset C^0$, donc $J^{n+1}(f)=J(J^n(f))$ est dérivable avec $(J^{n+1}(f))'=J^n(f)$ (I.3.b) ;
comme $J^n(f)\in C^n$, on a $J^{n+1}(f)\in C^{n+1}$. Pour $1\le k\le n+1$ :

$$

\begin{aligned}
\big(J^{n+1}(f)\big)^{(k)}&=\big((J^{n+1}(f))'\big)^{(k-1)}\\
&=\big(J^n(f)\big)^{(k-1)}\\
&=J^{n-(k-1)}(f)\\
&=J^{n+1-k}(f),
\end{aligned}

$$

par hypothèse de récurrence (licite car $k-1\le n$). D'où $J^n(f)\in C^n([0,1])$ et, pour tout $0\le k\le n$,

$$

\boxed{(J^n(f))^{(k)}=J^{n-k}(f).}

$$

**(b)** Pour $0\le k<n$, on a $n-k\ge1$, donc par (a)

$$

(J^n(f))^{(k)}=J^{n-k}(f)=J\big(J^{n-k-1}(f)\big),

$$

et $J(g)(0)=0$ pour toute $g\in C([0,1])$, d'où

$$
\boxed{(J^n(f))^{(k)}(0)=0\ \ (0\le k<n).}
$$

**(c)** $J^n(f)\in C^n([0,1])$ d'après (a). La formule de Taylor avec reste intégral à l'ordre $n$ en $0$, pour $n\ge1$ et $x\in[0,1]$, s'écrit

$$

(J^n(f))(x)=\sum_{k=0}^{n-1}\frac{(J^n(f))^{(k)}(0)}{k!}x^k+\frac{1}{(n-1)!}\int_0^x(x-t)^{n-1}(J^n(f))^{(n)}(t)\,dt.

$$

Par (b), tous les $(J^n(f))^{(k)}(0)$, $0\le k<n$, sont nuls, et par (a), $(J^n(f))^{(n)}=J^0(f)=f$. Donc

$$
\boxed{(J^n(f))(x)=\frac{1}{(n-1)!}\int_0^x(x-t)^{n-1}f(t)\,dt\qquad(n\ge1,\ x\in[0,1]).}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « peu de candidats ont pensé à utiliser une formule de Taylor et beaucoup se sont lancés dans une récurrence, qu’ils ont eu en fait du mal à gérer » ; « beaucoup de confusions entre $J$ et $J(f)$ ».

### III.5

> [!INDICATION]
> (a) Relation de Chasles et $\|f\|_\infty\le1$. (b) Appliquer le théorème d'Ascoli à $A=\{J(f):\|f\|_\infty\le1\}$ : équicontinuité (a) et bornitude ponctuelle (III.1.a).

#### Solution

**(a)** Soit $f\in C([0,1])$ avec $\|f\|_\infty\le1$. Pour $x,y\in[0,1]$, la relation de Chasles donne

$$

\begin{aligned}
|J(f)(x)-J(f)(y)|&=\Big|\int_y^x f(t)\,dt\Big|\\
&\le\|f\|_\infty|x-y|\\
&\le|x-y|.
\end{aligned}

$$

$$
\boxed{J(f)\text{ est }1\text{-lipschitzienne sur }[0,1].}
$$

**(b)** Posons $A=\{J(f):f\in C([0,1]),\ \|f\|_\infty\le1\}$. D'après (a), toutes les fonctions de $A$ sont $1$-lipschitziennes, donc $A$ est équicontinue.
D'après III.1.a, pour tout $x\in[0,1]$, l'ensemble $\{g(x):g\in A\}$ est borné (par $1$).
Le théorème d'Ascoli sur le compact $[0,1]$ assure que $A$ est relativement compacte dans $C([0,1])$ :

$$
\boxed{J\text{ est un opérateur compact de }C([0,1])\text{ dans lui-même.}}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « très peu de candidats ont pensé à invoquer le théorème d’Ascoli qui donnait immédiatement le résultat. »

## Partie IV — L'opérateur d'intégration sur $L^2(0,1)$

Même opérateur noté $V$, vu sur l'espace de Hilbert $L^2(0,1)$ : adjoint, valeurs propres de $V^*\circ V$, base hilbertienne des cosinus, et norme exacte de $V$.
Ne pas confondre $V$ (sur $L^2$) et $J$ (sur $C([0,1])$).

### IV.1

> [!INDICATION]
> (a) Cauchy–Schwarz sur l'accroissement $|V(f)(x)-V(f)(x_0)|$ pour obtenir la continuité (voire le caractère höldérien), puis $\|V(f)\|_2\le\|V(f)\|_\infty\le\|f\|_2$. (b) Calculer $\langle V(g),f\rangle_2$, justifier Fubini par $L^2\subset L^1$, et identifier l'adjoint.

#### Solution

**(a)** Soient $f\in L^2(0,1)$ et $x_0\le x$ dans $[0,1]$. Par Cauchy–Schwarz,

$$

\begin{aligned}
|V(f)(x)-V(f)(x_0)|&=\Big|\int_{x_0}^x f(t)\,dt\Big|\\
&\le\Big(\int_{x_0}^x dt\Big)^{1/2}\Big(\int_{x_0}^x|f(t)|^2\,dt\Big)^{1/2}\\
&\le\sqrt{x-x_0}\,\|f\|_2.
\end{aligned}

$$

Le cas $x\le x_0$ est symétrique, donc $|V(f)(x)-V(f)(x_0)|\le\sqrt{|x-x_0|}\,\|f\|_2$ : $V(f)$ est $\frac12$-höldérienne, donc continue. Ainsi $V(L^2(0,1))\subset C([0,1])$.
De plus $V(f)(0)=0$, donc $|V(f)(x)|\le\sqrt{x}\,\|f\|_2\le\|f\|_2$, d'où $\|V(f)\|_\infty\le\|f\|_2$.
Comme $\|g\|_2\le\|g\|_\infty$ sur $[0,1]$ pour toute fonction continue $g$, on obtient $\|V(f)\|_2\le\|f\|_2$.
Donc $V$ est linéaire continue de $L^2(0,1)$ dans lui-même et

$$
\boxed{V(L^2(0,1))\subset C([0,1]),\qquad \|V\|\le1.}
$$

**(b)** Pour $f,g\in L^2(0,1)$,

$$

\langle g,V^*(f)\rangle_2=\langle V(g),f\rangle_2=\int_0^1\Big(\int_0^x g(t)\,dt\Big)\overline{f(x)}\,dx.

$$

Comme $L^2(0,1)\subset L^1(0,1)$, on a $\int_0^1\int_0^x|g(t)||f(x)|\,dt\,dx\le\|g\|_1\|f\|_1<+\infty$, donc Fubini s'applique :

$$

\langle g,V^*(f)\rangle_2=\int_0^1 g(t)\Big(\int_t^1\overline{f(x)}\,dx\Big)dt
=\Big\langle g,\ x\mapsto\int_x^1 f(u)\,du\Big\rangle_2.

$$

Posons $T(f)(x)=\int_x^1 f(u)\,du$. On a $|T(f)(x)|\le\|f\|_1\le\|f\|_2$, donc $\|T(f)\|_2\le\|T(f)\|_\infty\le\|f\|_2$ : $T$ est continue. L'égalité $\langle g,V^*(f)\rangle_2=\langle g,T(f)\rangle_2$ pour tout $g$ donne, par unicité de l'adjoint,

$$
\boxed{V^*(f)(x)=\int_x^1 f(t)\,dt\quad\text{pour presque tout }x\in[0,1].}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « Le b. a été souvent maltraité, les candidats se contentant de calculs formels. » L’interversion de Fubini doit être justifiée, et la conclusion par unicité de l’adjoint.

> [!PIEGE]
> Ne pas confondre $V$ (sur $L^2(0,1)$, classes de fonctions) et $J$ (sur $C([0,1])$). Rapport 2025 (p. 49) : lire l’énoncé « évite des confusions dans la nature des objets (notamment entre $V$ et $J$ dans ce sujet) ».

### IV.2

> [!INDICATION]
> (a) Exprimer $\langle(V^*\circ V)(h),h\rangle_2$ de deux façons. (b) Poser $f(x)=\frac1\lambda\int_x^1 V(h)(t)\,dt$ (représentant continu de $h$) et reconnaître $\lambda f=c-V^2(f)$. (c) Dériver deux fois l'équation obtenue, trouver les conditions au bord $f(1)=0$, $f'(0)=0$, utiliser I.2.b, puis vérifier la réciproque par double intégration.

#### Solution

**(a)** D'une part $\langle(V^*\circ V)(h),h\rangle_2=\langle V(h),V(h)\rangle_2=\|V(h)\|_2^2\ge0$ ; d'autre part $(V^*\circ V)(h)=\lambda h$ donne $\langle(V^*\circ V)(h),h\rangle_2=\lambda\|h\|_2^2$.
Comme $h\neq0$, $\|h\|_2^2>0$, et comme $\lambda\neq0$, on ne peut avoir $\|V(h)\|_2=0$ (sinon $\lambda h=0$) ; donc

$$
\boxed{\lambda\in\mathbb R\text{ et }\lambda>0.}
$$

**(b)** Comme $\lambda\neq0$, pour presque tout $x$,

$$

h(x)=\frac1\lambda(V^*\circ V)(h)(x)=\frac1\lambda\int_x^1 V(h)(t)\,dt.

$$

Posons, pour tout $x\in[0,1]$,

$$

f(x)=\frac1\lambda\int_x^1 V(h)(t)\,dt.

$$

Alors $f=h$ presque partout, et $V(h)\in C([0,1])$ (IV.1.a), donc $f\in C([0,1])$. De plus, avec $c=\int_0^1 V(h)(t)\,dt$,

$$

\lambda f(x)=c-\int_0^x V(h)(t)\,dt=c-V^2(h)(x).

$$

Comme $f=h$ p.p., $V^2(f)=V^2(h)$, et cette égalité a lieu pour tout $x$, avec la constante $c=\int_0^1 V(h)$, $f\in C([0,1])$ et $f=h$ p.p. :

$$

\boxed{\lambda f=c-V^2(f).}

$$

**(c)** $f$ étant continue, $V^2(f)=J^2(f)$, et (b) donne $f=\frac c\lambda-\frac1\lambda J^2(f)$. Or $J^2(f)\in C^2$ avec $(J^2(f))''=f$ (III.4.a), donc $f\in C^2$ et

$$

f''=-\frac1\lambda f.

$$

D'autre part, par définition de $f$, $f(1)=0$ ; et en dérivant (b), $f'=-\frac1\lambda(J^2(f))'=-\frac1\lambda J(f)$, donc $f'(0)=0$. Ainsi $f\in E_\lambda$ (notations de I.2.b).
Si $\lambda\neq\lambda_k:=\frac{4}{(2k+1)^2\pi^2}$ pour tout $k\in\mathbb N$, alors $E_\lambda=\{0\}$, donc $f=0$ p.p., c'est-à-dire $h=0$ : exclu.
Toute valeur propre non nulle de $V^*\circ V$ est donc l'un des $\lambda_k$, et un vecteur propre associé $h_k$ vérifie, p.p.,

$$

h_k(x)=a\cos\!\Big(\frac{x}{\sqrt{\lambda_k}}\Big)=a\cos\!\Big(\frac{(2k+1)\pi x}{2}\Big),\ a\in\mathbb C^*.

$$

Réciproquement, pour $h_k(x)=\cos(\frac{(2k+1)\pi x}{2})$ :

$$

V(h_k)(x)=\frac{2}{(2k+1)\pi}\sin\!\Big(\frac{(2k+1)\pi x}{2}\Big),

$$

$$

\begin{aligned}
V^*(V(h_k))(x)&=\int_x^1 V(h_k)(t)\,dt\\
&=\frac{4}{(2k+1)^2\pi^2}\Big[-\cos\!\Big(\frac{(2k+1)\pi t}{2}\Big)\Big]_x^1\\
&=\frac{4}{(2k+1)^2\pi^2}h_k(x),
\end{aligned}

$$

car $\cos(\frac{(2k+1)\pi}{2})=0$. Donc $(V^*\circ V)(h_k)=\lambda_k h_k$. En conclusion :

$$

\boxed{\sigma_p(V^*\circ V)\setminus\{0\}=\Big\{\lambda_k=\frac{4}{(2k+1)^2\pi^2}:k\in\mathbb N\Big\}}

$$

$$

\boxed{\ker(V^*\circ V-\lambda_k)=\mathbb C\,h_k.}

$$

> [!PIEGE]
> $h$ est une classe de $L^2$, $f$ un représentant continu : bien distinguer les deux dans la rédaction (rapport 2025, p. 50, sur la « nature des objets »).

### IV.3

> [!INDICATION]
> (a) Exprimer $\widehat G(n)$ par $1$-périodicité sur $[-\frac12,\frac12]$, changer $u=-t$ sur la partie négative, et reconnaître $2\cos$.
(b) Si $g\perp\mathrm{Vect}(f_n)$, montrer que tous les $\widehat G(n)$, $n\in\mathbb Z$, sont nuls (penser à la parité du cosinus pour les $n<0$), conclure $G=0$ puis $g=0$ ;
conclure avec I.1.

#### Solution

**(a)** On a $|G(u)|=|g(\pm2u)|$, donc par $1$-périodicité $G\in L^2$ et $\widehat G(n)=\langle G,e_n\rangle_2=\int_0^1 G(t)e^{-2i\pi nt}\,dt$ est bien défini. Par $1$-périodicité,

$$

\widehat G(n)=\int_{-1/2}^{1/2}G(t)e^{-2i\pi nt}\,dt
=\int_{-1/2}^0 g(-2t)e^{-i\pi t}e^{-2i\pi nt}\,dt+\int_0^{1/2}g(2t)e^{-i\pi t}e^{-2i\pi nt}\,dt.

$$

Dans la première intégrale, le changement $u=-t$ donne

$$

\begin{aligned}
\widehat G(n)&=\int_0^{1/2}g(2u)\big(e^{(2n+1)i\pi u}+e^{-(2n+1)i\pi u}\big)\,du\\
&=2\int_0^{1/2}g(2t)\cos\big((2n+1)\pi t\big)\,dt,
\end{aligned}

$$

puis le changement $s=2t$ conclut :

$$
\boxed{\widehat G(n)=\int_0^1 g(t)\cos\!\Big(\frac{(2n+1)\pi t}{2}\Big)\,dt.}
$$

**(b)** Soit $g\in L^2(0,1)$ orthogonale à $\mathrm{Vect}(f_n)$. Pour tout $n\in\mathbb N$, par (a),

$$

\begin{aligned}
0=\langle g,f_n\rangle_2&=\sqrt2\int_0^1 g(t)\cos\!\Big(\frac{(2n+1)\pi t}{2}\Big)\,dt\\
&=\sqrt2\,\widehat G(n),
\end{aligned}

$$

donc $\widehat G(n)=0$. Pour $n>0$, par parité du cosinus,

$$

\begin{aligned}
\widehat G(-n)&=\int_0^1 g(t)\cos\!\Big(\frac{(2n-1)\pi t}{2}\Big)\,dt\\
&=\widehat G(n-1)\\
&=0.
\end{aligned}

$$

Donc $\widehat G(n)=0$ pour tout $n\in\mathbb Z$.
L'application $G\mapsto(\widehat G(n))_{n\in\mathbb Z}$ étant injective (la famille $(e_n)$ est une base hilbertienne de $L^2(0,1)$), on a $G=0$ dans $L^2$,
c'est-à-dire $g(2u)=0$ pour presque tout $u\in[0,\frac12]$, donc $g=0$ dans $L^2(0,1)$.
L'orthogonal de $\mathrm{Vect}(f_n)$ est réduit à $\{0\}$ : ce sous-espace est dense. Par ailleurs, d'après I.1, $\langle f_n,f_m\rangle_2=2\cdot\frac12\delta_{n,m}=\delta_{n,m}$ : la famille $(f_n)$ est orthonormée. Orthonormée et totale,

$$
\boxed{(f_n)_{n\in\mathbb N}\text{ est une base hilbertienne de }L^2(0,1).}
$$

> [!METHODE]
> Pour couvrir tous les $n\in\mathbb Z$, utiliser la parité du cosinus : $\widehat G(-n)=\widehat G(n-1)$. C’est l’injectivité de la transformée de Fourier qui conclut.

### IV.4

> [!INDICATION]
> Diagonaliser $V^*\circ V$ dans la base hilbertienne $(f_n)$ (IV.2.c, IV.3.b) et appliquer I.5.

#### Solution

D'après IV.2.c, $(V^*\circ V)(f_n)=\lambda_n f_n$ avec $\lambda_n=\frac{4}{(2n+1)^2\pi^2}$. Dans la base hilbertienne $(f_n)$ (IV.3.b), $V^*\circ V=D_\Lambda$ au sens de I.5, donc

$$

\begin{aligned}
\|V^*\circ V\|&=\|\Lambda\|_\infty\\
&=\sup_{n\in\mathbb N}\lambda_n\\
&=\lambda_0\\
&=\frac{4}{\pi^2},
\end{aligned}

$$

$$
\boxed{\|V^*\circ V\|=\frac{4}{\pi^2}.}
$$

### IV.5

> [!INDICATION]
> Appliquer I.4.b : $\|V\|^2=\|V^*\circ V\|$.

#### Solution

Par I.4.b, $\|V\|^2=\|V^*\circ V\|$, donc

$$
\boxed{\|V\|=\frac{2}{\pi}.}
$$

## Partie V — Un semi-groupe d'opérateurs

On plonge $V$ dans le semi-groupe de Riemann–Liouville $(V_s)_{s>0}$ : continuité en $s=0$, loi de semi-groupe, compacité de chaque $V_s$ par approximation par des opérateurs de rang fini.

### V.1

> [!INDICATION]
> Se ramener à la convolution sur $\mathbb R$ en prolongeant par $0$, et utiliser le théorème $L^1*L^p\to L^p$ ; ou bien Fubini–Tonelli pour la bonne définition puis inégalité triangulaire intégrale (Minkowski) pour la norme.

#### Solution

Prolongeons $f$ et $w$ par $0$ hors de $[0,1]$ en $\tilde f\in L^p(\mathbb R)$ et $\tilde w\in L^1(\mathbb R)$,
avec $\|\tilde f\|_{L^p(\mathbb R)}=\|f\|_{L^p(0,1)}$ et $\|\tilde w\|_{L^1(\mathbb R)}=\|w\|_{L^1(0,1)}$.
Le théorème de convolution $L^1*L^p\to L^p$ sur $\mathbb R$ donne que $(\tilde w*\tilde f)(x)$ est bien défini pour presque tout $x\in\mathbb R$, que $\tilde w*\tilde f\in L^p(\mathbb R)$, avec

$$
\|\tilde w*\tilde f\|_{L^p(\mathbb R)}\le\|\tilde w\|_{L^1(\mathbb R)}\|\tilde f\|_{L^p(\mathbb R)}.
$$

Or, pour $x\in[0,1]$, $(\tilde w*\tilde f)(x)=\int_{\mathbb R}\tilde w(x-t)\tilde f(t)\,dt=\int_0^x w(x-t)f(t)\,dt=(w*f)(x)$, car $\tilde f(t)=0$ si $t\notin[0,1]$ et $\tilde w(x-t)=0$ si $t>x$.
Donc $(w*f)(x)$ est bien défini pour presque tout $x\in[0,1]$, $w*f\in L^p(0,1)$, et

$$
\boxed{\|w*f\|_{L^p(0,1)}\le\|w\|_{L^1(0,1)}\|f\|_{L^p(0,1)}.}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « Le début de cette partie a été abordé par une petite proportion de candidats avec une réussite inégale. »

### V.2

> [!INDICATION]
> (a) Reconnaître $V_s(f)=w_s*f$ avec $w_s(t)=\frac{t^{s-1}}{\Gamma(s)}\in L^1(0,1)$, et appliquer V.1. (b) Changement de variable $t=xu$, reconnaître $\mathrm{B}(n+1,s)$.
(c) Inégalité triangulaire : séparer la variation du coefficient (continuité de $\Gamma$) et $\|p_{n+s}-p_n\|_2$.
(d) Densité des polynômes dans $L^2$ (Weierstrass) puis argument $3\varepsilon$, en utilisant que $\|V_s\|$ est bornée au voisinage de $0$.
(e) Calculer $V_{s_1}\circ V_{s_2}$ sur les $p_n$ (formule de (b) étendue à tout exposant réel $\alpha\ge0$) puis conclure par densité ; ou bien double Fubini avec le changement $u=(1-\lambda)t+\lambda x$ et $\mathrm{B}(s_1,s_2)$.

#### Solution

**(a)** Posons $w_s(t)=\frac{1}{\Gamma(s)}t^{s-1}$ pour $t\in\,]0,1]$. Alors $w_s\in L^1(0,1)$ et $V_s(f)=w_s*f$.
Par V.1 avec $p=2$, $V_s(f)(x)$ est bien défini p.p., $V_s(f)\in L^2(0,1)$, et

$$

\begin{aligned}
\|V_s(f)\|_2&\le\|w_s\|_{L^1(0,1)}\|f\|_2,\\
\|w_s\|_{L^1(0,1)}&=\frac1{\Gamma(s)}\int_0^1 t^{s-1}\,dt\\
&=\frac{1}{s\Gamma(s)}=\frac{1}{\Gamma(s+1)}
\end{aligned}

$$

(relation II.1.b). Donc $V_s$ est linéaire continue et

$$
\boxed{\|V_s\|\le\frac{1}{\Gamma(s+1)}.}
$$

**(b)** Pour $x\in\,]0,1]$, le changement de variable $t=xu$ donne

$$

\begin{aligned}
V_s(p_n)(x)&=\frac1{\Gamma(s)}\int_0^x(x-t)^{s-1}t^n\,dt\\
&=\frac{x^{n+s}}{\Gamma(s)}\int_0^1(1-u)^{s-1}u^n\,du\\
&=\frac{x^{n+s}}{\Gamma(s)}\mathrm{B}(n+1,s).
\end{aligned}

$$

Par II.2.b(ii), $\mathrm{B}(n+1,s)=\frac{\Gamma(n+1)\Gamma(s)}{\Gamma(n+1+s)}$, et $\Gamma(n+1)=n!$ (II.1.c), donc

$$
\boxed{V_s(p_n)=\frac{n!}{\Gamma(n+1+s)}\,p_{n+s}.}
$$

**(c)** Par (b) et l'inégalité triangulaire,

$$

\begin{aligned}
\|V_s(p_n)-p_n\|_2&\le\frac{n!}{\Gamma(n+1+s)}\,\|p_{n+s}-p_n\|_2\\
&\quad+\Big|\frac{n!}{\Gamma(n+1+s)}-1\Big|\,\|p_n\|_2.
\end{aligned}

$$

Par continuité de $\Gamma$ (II.1.d), $\Gamma(n+1+s)\to\Gamma(n+1)=n!$ quand $s\to0^+$, donc le second terme tend vers $0$. D'autre part,

$$

\begin{aligned}
\|p_{n+s}-p_n\|_2^2&=\int_0^1|t^{n+s}-t^n|^2\,dt\\
&\le\int_0^1 t^{2n}|t^s-1|^2\,dt\\
&\le\int_0^1|t^s-1|^2\,dt=\frac{1}{2s+1}-\frac{2}{s+1}+1\xrightarrow[s\to0^+]{}0.
\end{aligned}

$$

$$
\boxed{\lim_{s\to0^+}\|V_s(p_n)-p_n\|_2=0.}
$$

**(d)** Les polynômes sont denses dans $L^2(0,1)$ : $C([0,1])$ y est dense, et le théorème de Weierstrass approche uniformément sur $[0,1]$ (et $\|\cdot\|_2\le\|\cdot\|_\infty$).
Soit $f\in L^2(0,1)$, $\varepsilon>0$, et $p=\sum_{n=0}^N a_np_n$ un polynôme avec $\|f-p\|_2\le\varepsilon$.
Par linéarité, (c) donne $\|V_s(p)-p\|_2\to0$ quand $s\to0^+$. Alors

$$

\begin{aligned}
\|V_s(f)-f\|_2&\le\|V_s(f-p)\|_2+\|V_s(p)-p\|_2+\|p-f\|_2\\
&\le\big(\|V_s\|+1\big)\|f-p\|_2+\|V_s(p)-p\|_2.
\end{aligned}

$$

Par (a), $\|V_s\|\le\frac{1}{\Gamma(s+1)}\to\frac{1}{\Gamma(1)}=1$, donc $\limsup_{s\to0^+}\|V_s(f)-f\|_2\le2\varepsilon$. Ceci valant pour tout $\varepsilon>0$ :

$$
\boxed{\lim_{s\to0^+}\|V_s(f)-f\|_2=0\qquad(f\in L^2(0,1)).}
$$

**(e)** Remarquons d'abord que la formule de (b) vaut pour tout réel $\alpha\ge0$ : $V_s(p_\alpha)=\frac{\Gamma(\alpha+1)}{\Gamma(\alpha+1+s)}p_{\alpha+s}$. Alors, pour $n\in\mathbb N$,

$$

\begin{aligned}
(V_{s_1}\circ V_{s_2})(p_n)&=\frac{n!}{\Gamma(n+1+s_2)}\,V_{s_1}(p_{n+s_2})\\
&=\frac{n!}{\Gamma(n+1+s_2)}\cdot\frac{\Gamma(n+1+s_2)}{\Gamma(n+1+s_1+s_2)}\,p_{n+s_1+s_2}\\
&=V_{s_1+s_2}(p_n).
\end{aligned}

$$

Les deux opérateurs continus $V_{s_1}\circ V_{s_2}$ et $V_{s_1+s_2}$ coïncident sur $\mathrm{Vect}(p_n)$, qui est dense dans $L^2(0,1)$ d'après (d) ; par continuité, ils coïncident sur $L^2(0,1)$ :

$$
\boxed{V_{s_1}\circ V_{s_2}=V_{s_1+s_2}\qquad(s_1,s_2>0).}
$$

### V.3

> [!INDICATION]
> (a) Procédé d'extraction diagonale : extraire successivement pour $T_0,T_1,\dots$, puis définir $\varphi(n)=(\varphi_0\circ\cdots\circ\varphi_n)(n)$.
(b) Argument $3\varepsilon$ : approcher $T$ en norme par un $T_{k_0}$, utiliser le caractère de Cauchy de $(T_{k_0}(x_{\varphi(n)}))_n$ et la complétude de $H$.

#### Solution

**(a)** Par compacité de $T_0$, il existe une application strictement croissante $\varphi_0:\mathbb N\to\mathbb N$ telle que $(T_0(x_{\varphi_0(n)}))_n$ converge dans $H$.
Par récurrence, pour tout $j\ge0$, on construit $\varphi_{j+1}$ strictement croissante telle que $(T_{j+1}(x_{(\varphi_0\circ\cdots\circ\varphi_{j+1})(n)}))_n$ converge. Posons

$$

\varphi(n)=(\varphi_0\circ\cdots\circ\varphi_n)(n).

$$

Alors $\varphi$ est strictement croissante : en effet $\varphi_{n+1}(n+1)\ge n+1$ et la composée $\varphi_0\circ\cdots\circ\varphi_n$ est strictement croissante, donc

$$

\varphi(n+1)=(\varphi_0\circ\cdots\circ\varphi_n)(\varphi_{n+1}(n+1))>(\varphi_0\circ\cdots\circ\varphi_n)(n)=\varphi(n).

$$

De plus, pour $k$ fixé, la suite $(T_k(x_{\varphi(n)}))_{n\ge k}$ est une sous-suite de $(T_k(x_{(\varphi_0\circ\cdots\circ\varphi_k)(n)}))_n$, qui converge. Donc

$$
\boxed{\forall k\in\mathbb N,\ (T_k(x_{\varphi(n)}))_{n\in\mathbb N}\text{ converge dans }H.}
$$

**(b)** Soit $\varepsilon>0$. Comme $\|T_n-T\|\to0$, il existe $k_0$ tel que $\|T_{k_0}-T\|\le\varepsilon$.
La suite $(T_{k_0}(x_{\varphi(n)}))_n$ converge (a), donc est de Cauchy : il existe $N$ tel que pour $n,m\ge N$,

$$
\|T_{k_0}(x_{\varphi(n)})-T_{k_0}(x_{\varphi(m)})\|_H\le\varepsilon.
$$

Alors, pour $n,m\ge N$, comme $\|x_{\varphi(n)}\|_H\le1$,

$$

\begin{aligned}
\|T(x_{\varphi(n)})-T(x_{\varphi(m)})\|_H&\le\|(T-T_{k_0})(x_{\varphi(n)})\|_H\\
&\quad+\|T_{k_0}(x_{\varphi(n)})-T_{k_0}(x_{\varphi(m)})\|_H\\
&\quad+\|(T-T_{k_0})(x_{\varphi(m)})\|_H\\
&\le2\|T-T_{k_0}\|+\varepsilon\le3\varepsilon.
\end{aligned}

$$

La suite $(T(x_{\varphi(n)}))_n$ est donc de Cauchy dans le complet $H$ : elle converge. Ainsi, l'image par $T$ de toute suite de la boule unité fermée admet une sous-suite convergente :

$$
\boxed{T\text{ est compacte.}}
$$

> [!METHODE]
> « Limite uniforme d’opérateurs compacts est compacte » : le schéma diagonal + $3\varepsilon$ de V.3 est réutilisé en VI.2.b.

### V.4

> [!INDICATION]
> (a) $K_n$ est à image dans $\mathrm{Vect}(p_0,\dots,p_{d_n})$ (dimension finie) et continue par Cauchy–Schwarz : c'est un opérateur de rang fini, donc compact. (b) Écrire $V_s(f)-K_n(f)$ comme une convolution par $\psi_s-Q_n$ et appliquer l'inégalité de Minkowski intégrale. (c) $\psi_s\in L^1(-1,1)$ et les polynômes y sont denses (Weierstrass) : $\|V_s-K_n\|\to0$, conclure avec V.3.b.

#### Solution

**(a)** On a $K_n(f)=\sum_{j=0}^{d_n}\big(\int_0^1 f(u)P_{j,n}(u)\,du\big)p_j$, donc $K_n$ est linéaire et son image est contenue dans $F=\mathrm{Vect}(p_0,\dots,p_{d_n})$, de dimension finie. Par Cauchy–Schwarz, $|\int_0^1 fP_{j,n}|\le\|f\|_2\|P_{j,n}\|_2$, et $\|p_j\|_2\le1$, donc

$$

\begin{aligned}
\|K_n(f)\|_2&\le\sum_{j=0}^{d_n}\|p_j\|_2\,\|f\|_2\|P_{j,n}\|_2\\
&\le C_n\|f\|_2,\qquad C_n=\sum_{j=0}^{d_n}\|P_{j,n}\|_2<+\infty.
\end{aligned}

$$

$K_n$ est donc continue, de rang fini, donc compacte (toute suite bornée de $F$, de dimension finie, admet une sous-suite convergente) :

$$
\boxed{K_n\text{ est une application linéaire continue compacte de }L^2(0,1).}
$$

**(b)** On a $V_s(f)(x)=\int_0^1 f(u)\psi_s(x-u)\,du$ (car $\psi_s(x-u)=0$ si $u>x$) et, avec la notation de l'énoncé $Q_n(x-u)=\sum_{j=0}^{d_n}x^jP_{j,n}(u)$,

$$
K_n(f)(x)=\int_0^1 f(u)Q_n(x-u)\,du.

$$

Donc, pour presque tout $x$,

$$

\begin{aligned}
(V_s(f)-K_n(f))(x)&=\int_{-1}^1(\psi_s-Q_n)(t)F(x,t)\,dt,\\
F(x,t)&=f(x-t)\mathbf 1_{0\le x-t\le1}.
\end{aligned}

$$

Par l'inégalité de Minkowski intégrale,

$$

\begin{aligned}
\|V_s(f)-K_n(f)\|_2&\le\int_{-1}^1|\psi_s-Q_n|(t)\Big(\int_0^1|F(x,t)|^2\,dx\Big)^{1/2}dt,\\
\int_0^1|F(x,t)|^2\,dx&=\int_{[0,1]\cap[-t,1-t]}|f(u)|^2\,du\le\|f\|_2^2,
\end{aligned}

$$

d'où

$$
\boxed{\|V_s(f)-K_n(f)\|_2\le\|\psi_s-Q_n\|_{L^1(-1,1)}\,\|f\|_2.}
$$

**(c)** La fonction $\psi_s$ appartient à $L^1(-1,1)$ : elle est continue sur $[-1,1]\setminus\{0\}$ et $u\mapsto u^{s-1}$ est intégrable au voisinage de $0$ car $s>0$.
Les polynômes sont denses dans $L^1(-1,1)$ (densité de $C^0$ dans $L^1$, Weierstrass, et $\|g\|_{L^1(-1,1)}\le2\|g\|_\infty$).
Soit $\varepsilon>0$ : il existe un polynôme $Q_n$ tel que $\|\psi_s-Q_n\|_{L^1(-1,1)}\le\varepsilon$.
Par (b), $\|V_s(f)-K_n(f)\|_2\le\varepsilon\|f\|_2$ pour tout $f$, donc $\|V_s-K_n\|\le\varepsilon$. Ainsi $\|V_s-K_n\|\to0$. Les $K_n$ étant compacts (a), V.3.b conclut :

$$
\boxed{V_s\text{ est compacte sur }L^2(0,1),\text{ pour tout }s>0.}
$$

## Partie VI — Opérateurs de Hilbert–Schmidt

Généralités sur la classe de Hilbert–Schmidt (indépendance de la base, compacité), puis caractérisation pour $V_s$ : Hilbert–Schmidt si et seulement si $s>1/2$, et somme absolument convergente d'opérateurs de rang 1 si et seulement si $s>1$.

### VI.1

> [!INDICATION]
> Partir de Parseval dans une base, faire apparaître $T^*$ via $\langle T(b_k),\gamma_n\rangle=\langle b_k,T^*(\gamma_n)\rangle$, échanger les sommes (Fubini–Tonelli, termes positifs), puis Parseval dans l'autre base.

#### Solution

($\Leftarrow$) C'est la définition. ($\Rightarrow$) Supposons $\sum_k\|T(b_k)\|_H^2<+\infty$ pour une base $(b_k)$, et soit $(\gamma_n)$ une autre base hilbertienne. Par la formule de Parseval dans $(\gamma_n)$,

$$

\sum_k\|T(b_k)\|_H^2=\sum_k\sum_n|\langle T(b_k),\gamma_n\rangle|^2
=\sum_k\sum_n|\langle T^*(\gamma_n),b_k\rangle|^2.

$$

Fubini–Tonelli (termes positifs) permet d'échanger les sommes, puis Parseval dans $(b_k)$ donne

$$

\sum_k\|T(b_k)\|_H^2=\sum_n\sum_k|\langle T^*(\gamma_n),b_k\rangle|^2=\sum_n\|T^*(\gamma_n)\|_H^2.

$$

Cette égalité valant pour tout couple de bases, on en déduit aussi $\sum_n\|T(\gamma_n)\|_H^2=\sum_n\|T^*(\gamma_n)\|_H^2<+\infty$ :

$$
\boxed{T\in\mathcal H_s(H)\iff\sum_n\|T(\gamma_n)\|_H^2<+\infty\text{ pour toute base hilbertienne }(\gamma_n).}
$$

> [!JURY]
> Rapport 2025 (p. 50) : « Cette dernière partie a été significativement abordée par extrêmement peu de candidats. »

### VI.2

> [!INDICATION]
> (a) Écrire $x-P_{F_n}x=\sum_{k>n}\langle x,b_k\rangle b_k$, appliquer $T$, puis inégalité triangulaire, Cauchy–Schwarz et Bessel. (b) Le reste de la série converge tend vers $0$ ; $S_n$ est de rang fini donc compact, conclure avec V.3.b.

#### Solution

**(a)** On a $x-P_{F_n}x=\sum_{k>n}\langle x,b_k\rangle b_k$, donc par linéarité et continuité de $T$,

$$
(T-S_n)(x)=T(x-P_{F_n}x)=\sum_{k>n}\langle x,b_k\rangle T(b_k).
$$

Par inégalité triangulaire, Cauchy–Schwarz et Bessel :

$$

\begin{aligned}
\|(T-S_n)(x)\|_H&\le\sum_{k>n}|\langle x,b_k\rangle|\,\|T(b_k)\|_H\\
&\le\Big(\sum_{k>n}|\langle x,b_k\rangle|^2\Big)^{1/2}\Big(\sum_{k>n}\|T(b_k)\|_H^2\Big)^{1/2}\\
&\le\|x\|_H\Big(\sum_{k>n}\,\|T(b_k)\|_H^2\Big)^{1/2},
\end{aligned}

$$

d'où

$$
\boxed{\lVert T-S_n\rVert^2\le\sum_{k=n+1}^{+\infty}\|T(b_k)\|_H^2.}
$$

**(b)** La série $\sum_k\|T(b_k)\|_H^2$ converge, donc son reste tend vers $0$ : $\|T-S_n\|\to0$. Or $S_n=T\circ P_{F_n}$ a son image dans $T(F_n)$, de dimension finie : $S_n$ est de rang fini, donc compact. Par V.3.b,

$$
\boxed{T\text{ est compacte.}}
$$

### VI.3

> [!INDICATION]
> (a) Fubini (justifié par l'intégrabilité de $u^{s-1}$) pour exprimer $\langle V_s(e_n),e_n\rangle_2$ avec $I_n(s-1)-I_n(s)$, puis utiliser II.3.b et II.3.e. (b) Si $V_s$ est Hilbert–Schmidt, $\sum_n\|V_s(e_n)\|_2^2<\infty$ ; minorer par les $\langle V_s(e_n),e_n\rangle_2$ (Cauchy–Schwarz) et conclure par le critère de Riemann.

#### Solution

**(a)** Avec le changement $u=x-t$,

$$

\langle V_s(e_n),e_n\rangle_2=\frac1{\Gamma(s)}\int_0^1\Big(\int_0^x e^{-2i\pi n(x-t)}(x-t)^{s-1}\,dt\Big)dx.

$$

Comme $|e^{-2i\pi nu}u^{s-1}|=u^{s-1}$ est intégrable ($s>0$), Fubini donne

$$

\langle V_s(e_n),e_n\rangle_2=\frac1{\Gamma(s)}\int_0^1 e^{-2i\pi nu}u^{s-1}(1-u)\,du
=\frac{I_n(s-1)-I_n(s)}{\Gamma(s)}.

$$

Pour $s\in\,]0,1[$, on a $s-1\in\,]-1,0[$, donc II.3.e donne $I_n(s-1)\sim\frac{\Gamma(s)}{(2\pi n)^s}e^{-i\pi s/2}$, et II.3.b donne $I_n(s)=O(1/n)$. Comme $s<1$, $O(1/n)=o(n^{-s})$, donc

$$
\boxed{\langle V_s(e_n),e_n\rangle_2\underset{n\to+\infty}{\sim}\frac{e^{-i\pi s/2}}{(2\pi n)^s}.}
$$

**(b)** Si $V_s$ est Hilbert–Schmidt, VI.1 appliqué à la base $(e_n)_{n\in\mathbb Z}$ donne $\sum_n\|V_s(e_n)\|_2^2<+\infty$. Par Cauchy–Schwarz, $|\langle V_s(e_n),e_n\rangle_2|\le\|V_s(e_n)\|_2$, donc $\sum_{n\ge1}|\langle V_s(e_n),e_n\rangle_2|^2<+\infty$.
Or d'après (a), $|\langle V_s(e_n),e_n\rangle_2|\sim\frac{1}{(2\pi n)^s}$ : la série $\sum n^{-2s}$ converge, ce qui impose $2s>1$, c'est-à-dire

$$
\boxed{V_s\in\mathcal H_s(L^2(0,1))\ \Rightarrow\ s>\frac12.}
$$

> [!PIEGE]
> Dans (a), c’est $I_n(s-1)$ (exposant dans $]-1,0[$, donc II.3.e) qui domine, et $I_n(s)=O(1/n)$ (II.3.b) qui est absorbé car $s<1$.

### VI.4

> [!INDICATION]
> Cauchy–Schwarz en $y$ pour définir $T_K(f)$ p.p. et borner sa norme ; puis Fubini–Tonelli + Parseval appliquées à $K_x$ pour sommer $\sum_n\|T_K(b_n)\|_2^2$.

#### Solution

Par Cauchy–Schwarz, pour $f\in L^2(0,1)$,

$$

\int_0^1|K(x,y)||f(y)|\,dy\le\|f\|_2\Big(\int_0^1|K(x,y)|^2\,dy\Big)^{1/2}.

$$

Par Fubini–Tonelli, $\int_0^1\int_0^1|K(x,y)|^2\,dy\,dx=\|K\|_{L^2}^2<+\infty$, donc pour presque tout $x$, $\int_0^1|K(x,y)|^2\,dy<+\infty$ ; ainsi $T_K(f)(x)$ est défini p.p. et

$$

|T_K(f)(x)|^2\le\|f\|_2^2\int_0^1|K(x,y)|^2\,dy.

$$

En intégrant en $x$, $\|T_K(f)\|_2^2\le\|f\|_2^2\|K\|_{L^2}^2$, donc $T_K$ est linéaire continue avec $\lVert T_K\rVert\le\|K\|_{L^2}$.
Soit $(b_n)$ une base hilbertienne et $K_x(y)=K(x,y)$ (dans $L^2$ pour p.t. $x$).
Par Fubini–Tonelli puis Parseval (appliquée à $K_x$ dans la base $(\overline{b_n})$, aussi hilbertienne),

$$

\begin{aligned}
\sum_n\|T_K(b_n)\|_2^2&=\int_0^1\sum_n\Big|\int_0^1 K(x,y)b_n(y)\,dy\Big|^2dx\\
&=\int_0^1\|K_x\|_2^2\,dx\\
&=\|K\|_{L^2([0,1]^2)}^2<+\infty,
\end{aligned}

$$

$$
\boxed{T_K\text{ est continue et Hilbert–Schmidt, avec }\sum_n\|T_K(b_n)\|_2^2=\|K\|_{L^2([0,1]^2)}^2.}
$$

### VI.5

> [!INDICATION]
> Le sens direct est VI.3.b. Pour la réciproque, écrire $V_s=T_{K_s}$ avec le noyau $K_s(x,y)=\frac{1}{\Gamma(s)}\mathbf 1_{[0,x[}(y)(x-y)^{s-1}$, calculer $\|K_s\|_{L^2}^2$ et appliquer VI.4.

#### Solution

Si $V_s$ est Hilbert–Schmidt, alors $s>\frac12$ (VI.3.b). Réciproquement, soit $s>\frac12$. On a $V_s=T_{K_s}$ avec

$$

K_s(x,y)=\frac1{\Gamma(s)}\mathbf 1_{[0,x[}(y)\,(x-y)^{s-1},\qquad(x,y)\in[0,1]^2.

$$

Comme $2s-1>0$,

$$

\begin{aligned}
\int_0^1\int_0^1|K_s(x,y)|^2\,dy\,dx&=\frac1{\Gamma(s)^2}\int_0^1\int_0^x(x-y)^{2s-2}\,dy\,dx\\
&=\frac1{\Gamma(s)^2}\int_0^1\frac{x^{2s-1}}{2s-1}\,dx\\
&=\frac{1}{2s(2s-1)\Gamma(s)^2}<+\infty.
\end{aligned}

$$

Donc $K_s\in L^2([0,1]^2)$ et, par VI.4, $V_s=T_{K_s}$ est Hilbert–Schmidt :

$$
\boxed{V_s\in\mathcal H_s(L^2(0,1))\iff s>\frac12.}
$$

### VI.6

> [!INDICATION]
> Un opérateur de rang $1$ s'écrit $x\otimes y$ avec $\lVert x\otimes y\rVert=\|x\|_2\|y\|_2$ ;
si la série est absolument convergente, montrer que $\sum_n|\langle V_s(e_n),e_n\rangle_2|<\infty$ (Fubini, Cauchy–Schwarz, Parseval), puis distinguer $0<s<1$ (série de Riemann via VI.3.a) et $s=1$ (calcul explicite de $V_1(e_n)$).
Réciproquement, pour $s>1$, factoriser $V_s=V_{s/2}\circ V_{s/2}$ avec $V_{s/2}$ Hilbert–Schmidt (VI.5, V.2.e) et développer en série de rang 1 absolument convergente.

#### Solution

($\Rightarrow$) Toute application linéaire continue de rang $1$ sur $L^2(0,1)$ s'écrit $x\otimes y:h\mapsto\langle h,y\rangle_2\,x$, avec $\lVert x\otimes y\rVert=\|x\|_2\|y\|_2$.
Si $V_s=\sum_{k\ge0}x_k\otimes y_k$ avec $\sum_k\|x_k\|_2\|y_k\|_2<+\infty$, alors

$$

\langle V_s(e_n),e_n\rangle_2=\sum_k\langle e_n,y_k\rangle_2\langle x_k,e_n\rangle_2,

$$

et par Fubini–Tonelli, Cauchy–Schwarz et Parseval :

$$

\begin{aligned}
\sum_n|\langle V_s(e_n),e_n\rangle_2|&\le\sum_k\sum_n|\langle e_n,y_k\rangle_2||\langle x_k,e_n\rangle_2|\\
&\le\sum_k\Big(\sum_n|\langle e_n,y_k\rangle_2|^2\Big)^{1/2}\Big(\sum_n|\langle x_k,e_n\rangle_2|^2\Big)^{1/2}\\
&=\sum_k\|x_k\|_2\|y_k\|_2<+\infty.
\end{aligned}

$$

Si $0<s<1$, VI.3.a donne $|\langle V_s(e_n),e_n\rangle_2|\sim(2\pi n)^{-s}$, et $\sum_{n\ge1}n^{-s}$ diverge : contradiction.
Si $s=1$, on calcule $V_1(e_n)(x)=\int_0^x e^{2i\pi nt}\,dt=\frac{e_n(x)-1}{2i\pi n}$, donc $\langle V_1(e_n),e_n\rangle_2=\frac{1}{2i\pi n}$ (car $\langle 1,e_n\rangle_2=0$ pour $n\neq0$) et $\sum_{n\ge1}\frac{1}{2\pi n}$ diverge : contradiction.
Donc nécessairement $s>1$.

($\Leftarrow$) Soit $s>1$. Alors $\frac s2>\frac12$, donc $V_{s/2}$ est Hilbert–Schmidt (VI.5), et $V_{s/2}\circ V_{s/2}=V_s$ (V.2.e). Pour $f\in L^2(0,1)$,

$$

\begin{aligned}
V_s(f)&=V_{s/2}\big(V_{s/2}(f)\big)\\
&=\sum_{n\in\mathbb Z}\langle V_{s/2}(f),e_n\rangle_2\,V_{s/2}(e_n)\\
&=\sum_{n\in\mathbb Z}\langle f,V_{s/2}^*(e_n)\rangle_2\,V_{s/2}(e_n)
=\sum_{n\in\mathbb Z}\big(V_{s/2}(e_n)\otimes V_{s/2}^*(e_n)\big)(f).
\end{aligned}

$$

Cette série d'opérateurs de rang $1$ est absolument convergente en norme : par Cauchy–Schwarz et VI.1,

$$

\begin{aligned}
\sum_n\lVert V_{s/2}(e_n)\otimes V_{s/2}^*(e_n)\rVert&=\sum_n\|V_{s/2}(e_n)\|_2\|V_{s/2}^*(e_n)\|_2\\
&\le\Big(\sum_n\|V_{s/2}(e_n)\|_2^2\Big)^{1/2}\Big(\sum_n\|V_{s/2}^*(e_n)\|_2^2\Big)^{1/2}\\
&=\sum_n\|V_{s/2}(e_n)\|_2^2<+\infty,
\end{aligned}

$$

quantité finie car $V_{s/2}$ est Hilbert–Schmidt (l'égalité des deux sommes vient de VI.1). Finalement

$$
\boxed{V_s\text{ est somme absolument convergente d'applications linéaires continues de rang }1\iff s>1.}
$$

> [!METHODE]
> Le seuil $s>1$ est celui de la nucléarité : produit de deux opérateurs de Hilbert–Schmidt ($V_s=V_{s/2}\circ V_{s/2}$), alors que $s>1/2$ est le seuil de Hilbert–Schmidt (VI.5).

## Bilan

**Méthodes à retenir.**

- Opérateur diagonal sur un Hilbert : Pythagore + prolongement par densité + minoration sur les vecteurs de base (I.5), qui donne la norme et sert en IV.4.
- Norme d'adjoint sur un Hilbert : $\|T^*\|=\|T\\|$, $\|T^*\circ T\|=\\|T\\|^2$ (I.4), d'où $\|V\\|=2/\pi$ (IV.5).
- Compacité : Ascoli sur $C([0,1])$ (III.5), limite uniforme d'opérateurs compacts avec extraction diagonale (V.3), approximation par des opérateurs de rang fini via la densité des polynômes dans $L^1$ (V.4), Hilbert–Schmidt $\Rightarrow$ compact (VI.2).
- Densité + argument $3\varepsilon$ : polynômes denses dans $L^2$ (Weierstrass) pour la continuité forte en $0$ du semi-groupe (V.2.d).
- Analyse complexe prudente : domaine étoilé, log calculé morceau par morceau, jamais $\log(ab)=\log a+\log b$ (II.3.c).
- Seuils à retenir : $V_s$ compact pour tout $s>0$ (V.4.c), Hilbert–Schmidt $\iff s>1/2$ (VI.5), somme absolument convergente de rang 1 $\iff s>1$ (VI.6).

**Prérequis à revoir.** Théorème fondamental de l'analyse et sa preuve (I.3), IPP généralisée et continuité sous le signe somme (II.1), changement de variable en dimension 2 (II.2.b), théorème de Cauchy et déterminations du log (II.3.c), théorème d'Ascoli (III.5), bases hilbertiennes et Parseval (I.5, IV.3, VI.1), convolution $L^1*L^p$ (V.1).

**Questions classiques transposables.** Norme de l'opérateur de Volterra sur $L^2$ ($2/\pi$, IV.4–IV.5) ; spectre de $V^*V$ et base des cosinus (IV.2–IV.3) ; compacité par Ascoli (III.5) ; semi-groupe de Riemann–Liouville et ses seuils (V, VI) — des variantes figurent dans de nombreux sujets d'agrégation et de CAPES.
