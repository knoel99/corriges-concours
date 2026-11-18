# Centrale-Supélec PC — Mathématiques 2 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Le sujet relie la régularité höldérienne des fonctions continues périodiques à leur vitesse d’approximation uniforme par des polynômes trigonométriques. La preuve construit un noyau positif puis utilise une inégalité de Bernstein.

La Q7 contient une coquille relevée par le jury. La solution vérifie précisément les appartenances nécessaires à la suite du sujet.

## Partie A — Préliminaires

### Question 1

> [!INDICATION]
> Majorez la dérivée du sinus sur tout son domaine.

#### Solution

Le cosinus est borné en valeur absolue par 1. L’inégalité des accroissements finis donne $|\sin(s)-\sin(t)|\leq |s-t|$. Pour les couples tels que $|s-t|\leq h$, cette différence est majorée par $h$. Le passage au supremum donne $\omega_g(h)\leq h$.

### Question 2

> [!INDICATION]
> Réduisez la recherche d’une borne de la fonction à une période. Pour une fonction complexe, utilisez l’intégrale de la dérivée.

#### Solution

**a)** La continuité de $g$ sur $[-\pi,\pi]$ et la périodicité donnent une borne $M=\max_{[-\pi,\pi]}|g|$ valable sur $\mathbb R$. L’ensemble des différences en valeur absolue est donc inclus dans $[0,2M]$. Il contient zéro, obtenu avec $s=t$. Son supremum est un réel bien défini.

**b)** La dérivée est continue et périodique, donc également bornée. L’intégration de $g'$ entre $s$ et $t$ donne
$$
|g(s)-g(t)|\leq |s-t|\,\lVert g'\rVert_\infty.
$$
Ainsi $0\leq\omega_g(h)\leq h\lVert g'\rVert_\infty$. Par encadrement, $\omega_g(h)$ tend vers zéro quand $h$ tend vers zéro par valeurs positives.

### Question 3

> [!INDICATION]
> Pour la sous-additivité, placez un point intermédiaire sur le segment entre les deux arguments.

#### Solution

**a)** Si $h\leq h'$, tout couple admissible pour $h$ l’est pour $h'$. Cela donne l’inégalité par passage au supremum.

**b)** Soient $s,t$ à distance au plus $h+h'$. Si $|s-t|\leq h$, prenons $r=t$. Sinon, choisissons $r$ sur le segment à distance $h$ du premier argument.

Dans les deux cas $|s-r|\leq h$ et $|r-t|\leq h'$. L’inégalité triangulaire donne $|g(s)-g(t)|\leq\omega_g(h)+\omega_g(h')$. On prend le supremum.

**c)** La sous-additivité donne par récurrence $\omega_g(nh)\leq n\omega_g(h)$. Avec $m=\lceil\lambda\rceil$, la croissance donne
$$
\begin{aligned}
\omega_g(\lambda h)&\leq\omega_g(mh),\\
\omega_g(mh)&\leq m\omega_g(h)\leq(1+\lambda)\omega_g(h).
\end{aligned}
$$
Ces preuves utilisent uniquement la définition et la finitude du supremum. Elles valent aussi pour $g$ seulement continue.

### Question 4

> [!INDICATION]
> Faites varier la position de l’intervalle en gardant sa longueur constante.

#### Solution

Posons $F(x)=\int_{x-\pi}^{x+\pi}g(t)\,\mathrm dt$. Le théorème fondamental donne $F'(x)=g(x+\pi)-g(x-\pi)=0$ par périodicité. Les parties réelle et imaginaire de $F$ sont donc constantes. La valeur de $F$ en zéro donne l’égalité demandée.

### Question 5

> [!INDICATION]
> Calculez l’image d’une exponentielle élémentaire et repérez ce qui dépend de la variable de sortie.

#### Solution

Pour $-n\leq k\leq n$, soit $e_k(x)=e^{ikx}$. Alors
$$
\Delta(e_k)(x)=e_k(x)\int_{-\pi}^{\pi}e^{-ikt}g(t)\,\mathrm dt.
$$
Le facteur intégral est indépendant de $x$. Par linéarité de l’intégrale, $\Delta$ est linéaire et son image sur l’espace engendré par ces $e_k$ est incluse dans cet espace. C’est donc un endomorphisme de $\mathcal T_n$.

## Partie B — Un noyau d’approximation trigonométrique

### I — La fonction Jₙ

### Question 6

> [!INDICATION]
> Sommez la progression géométrique et transformez les deux différences d’exponentielles en sinus.

#### Solution

Pour $t\notin 2\pi\mathbb Z$, la somme géométrique vaut $(e^{i(n+1)t}-1)/(e^{it}-1)$. En utilisant $e^{iv}-1=2ie^{iv/2}\sin(v/2)$, le facteur de phase du quotient vaut $e^{int/2}$ et compense le facteur extérieur. On obtient
$$
\phi_n(t)=\frac{\sin((n+1)t/2)}{\sin(t/2)}.
$$
La formule de $f_n$ est la quatrième puissance du quotient.

### Question 7

> [!INDICATION]
> Lisez les fréquences dans la somme qui définit la fonction. Regardez séparément les cas où les fréquences sont entières.

#### Solution

La somme définissant $\phi_n$ a les fréquences $k-n/2$ pour $0\leq k\leq n$. Lorsque $n$ est pair, elles sont entières et $\phi_n\in\mathcal T_n$.

Lorsque $n$ est impair, $\phi_n(t+2\pi)=-\phi_n(t)$. Comme $\phi_n(0)=n+1$, elle n’appartient pas à $\mathcal T_n$. Cette première assertion de l’énoncé comporte donc une coquille, signalée par le jury.

En revanche,
$$
\phi_n(t)^2=\sum_{k,j=0}^{n}e^{i(k+j-n)t}
$$
est dans $\mathcal T_n$, tout comme $\phi_{2n}$ dont les fréquences sont les entiers de $-n$ à $n$.

En mettant $\phi_n^2$ au carré, les fréquences s’ajoutent et restent comprises entre $-2n$ et $2n$. Ainsi $f_n\in\mathcal T_{2n}$.

### Question 8

> [!INDICATION]
> Vérifiez le signe de la fonction et évaluez-la en zéro.

#### Solution

Le quotient de Q6 est réel hors de $2\pi\mathbb Z$. La continuité de $\phi_n$ sur $\mathbb R$ étend cette propriété aux points exclus. Ainsi $f_n$ est réelle, continue et positive ou nulle.

De plus $f_n(0)=(n+1)^4>0$. Son intégrale sur $[-\pi,\pi]$ est donc finie et strictement positive. Son inverse est l’unique constante positive $c_n$ demandée.

### II — Contrôle du moment du noyau

### Question 9

> [!INDICATION]
> Vérifiez la parité avant de remplacer les intégrales symétriques par des intégrales sur un demi-intervalle.

#### Solution

D’après Q6, $f_n$ est paire hors de $2\pi\mathbb Z$, donc partout par continuité. La fonction $t\mapsto |t|f_n(t)$ est également paire. Avec la définition de $c_n$, leurs deux intégrales symétriques se réduisent à deux fois l’intégrale sur $[0,\pi]$. Les facteurs 2 se simplifient dans le quotient.
$$
\int_{-\pi}^{\pi}|t|J_n(t)\,\mathrm dt=
\frac{\displaystyle\int_0^\pi t f_n(t)\,\mathrm dt}
{\displaystyle\int_0^\pi f_n(t)\,\mathrm dt}.
$$

### Question 10

> [!INDICATION]
> Utilisez une corde de la courbe du sinus pour l’une des bornes, et un contrôle de la dérivée pour l’autre.

#### Solution

Pour $0<t<\pi/2$, le théorème des accroissements finis appliqué sur $[0,t]$ puis $[t,\pi/2]$ donne deux pentes égales à des valeurs du cosinus. Comme le cosinus est décroissant, la première pente est au moins la seconde.
$$
\frac{\sin t}{t}\geq\frac{1-\sin t}{\pi/2-t}.
$$
Après multiplication par les dénominateurs positifs, cela donne $\sin t\geq2t/\pi$. Aux extrémités, c’est une égalité. La borne $\sin t\leq t$ résulte de Q1 en comparant $t$ à zéro.

### Question 11

> [!INDICATION]
> Pour majorer le quotient, minorez le sinus au dénominateur avant de changer de variable.

#### Solution

Pour $0<t\leq\pi$, Q10 donne $\sin(t/2)\geq t/\pi$. Avec $f_n$ donné par Q6, on a
$$
t f_n(t)\leq\pi^4\frac{\sin^4((n+1)t/2)}{t^3}.
$$
L’intégrande majorant admet un prolongement continu en zéro car $|\sin u|\leq |u|$. En intégrant puis en posant $u=(n+1)t/2$, on trouve
$$
\int_0^\pi t f_n(t)\,\mathrm dt
\leq\pi^4\left(\frac{n+1}{2}\right)^2
\int_0^{(n+1)\pi/2}\frac{\sin^4 u}{u^3}\,\mathrm du.
$$

### Question 12

> [!INDICATION]
> Pour minorer le quotient, utilisez l’autre borne sur le sinus.

#### Solution

Pour $0<t\leq\pi$, $\sin(t/2)\leq t/2$, d’où $f_n(t)\geq16\sin^4((n+1)t/2)/t^4$. Le quotient admet en zéro une limite finie, car $\sin u/u\to1$. Le même changement de variable $u=(n+1)t/2$ donne
$$
\int_0^\pi f_n(t)\,\mathrm dt
\geq 2(n+1)^3\int_0^{(n+1)\pi/2}\frac{\sin^4 u}{u^4}\,\mathrm du.
$$

### Question 13

> [!INDICATION]
> Majorez l’intégrale du numérateur sur une demi-droite et minorez celle du dénominateur sur un intervalle fixe.

#### Solution

Posons $U=\int_0^{+\infty}\sin^4(u)u^{-3}\,\mathrm du$. En zéro, l’intégrande est majoré par $u$. À l’infini, il est majoré par $u^{-3}$. Donc $U$ est fini et strictement positif. Posons aussi $V=\int_0^{\pi/2}\sin^4(u)u^{-4}\,\mathrm du$, qui est fini par prolongement en zéro et positif car l’intégrande est strictement positif sur l’intervalle ouvert.

Comme $(n+1)\pi/2\geq\pi/2$, l’intégrale de Q12 est au moins $V$. Celle de Q11 est au plus $U$. Les estimations donnent dans Q9
$$
\int_{-\pi}^{\pi}|t|J_n(t)\,\mathrm dt
\leq\frac{a}{n+1}.
$$
Ici $a=\pi^4 U/(8V)>0$ est indépendant de $n$.

### III — Approximation uniforme

### Question 14

> [!INDICATION]
> Après substitution, utilisez la périodicité du produit pour ramener l’intégrale sur l’intervalle initial.

#### Solution

Dans la définition de $T_n g(x)$, posons $u=x-t$. On obtient l’intégrale de $J_n(u)g(x-u)$ sur $[x-\pi,x+\pi]$. Cet intégrande est continu et $2\pi$-périodique en $u$. La Q4 donne donc
$$
T_n g(x)=\int_{-\pi}^{\pi}J_n(t)g(x-t)\,\mathrm dt.
$$
Comme l’intégrale de $J_n$ vaut 1, on a également $g(x)=\int_{-\pi}^{\pi}J_n(t)g(x)\,\mathrm dt$. On soustrait puis on applique l’inégalité triangulaire, en utilisant $J_n\geq0$.
$$
|T_n g(x)-g(x)|\leq\int_{-\pi}^{\pi}J_n(t)|g(x-t)-g(x)|\,\mathrm dt.
$$

### Question 15

> [!INDICATION]
> Transformez l’écart entre deux valeurs en un facteur proportionnel à la distance. Pour l’appartenance à un espace trigonométrique, revenez à Q5.

#### Solution

**a)** D’après Q2b, la différence dans l’intégrande est au plus $|t|\lVert g'\rVert_\infty$. La borne Q13 est indépendante de $x$, donc
$$
\lVert T_n g-g\rVert_\infty\leq\frac{a\lVert g'\rVert_\infty}{n+1}.
$$

**b)** Le noyau $J_n$ appartient à $\mathcal T_{2n}$. La Q5 appliquée avec $p=J_n$ donne $T_ng\in\mathcal T_{2n}$. La majoration précédente tend vers zéro, d’où la convergence uniforme.

### Question 16

> [!INDICATION]
> Appliquez la sous-additivité avec un pas de taille $1/n$. Ses preuves sont-elles liées à la dérivabilité ?

#### Solution

**a)** Si $t=0$, la différence est nulle. Sinon, par Q3c, valable également pour $g$ continue, on applique $h=1/n$ et $\lambda=n|t|$ afin d’obtenir
$$
|g(x-t)-g(x)|\leq\omega_g(|t|)
\leq(1+n|t|)\omega_g(1/n).
$$

**b)** Après insertion dans Q14, la masse totale de $J_n$ vaut 1, et $n$ fois son moment est majoré par $an/(n+1)\leq a$ d’après Q13. On obtient $\lVert T_ng-g\rVert_\infty\leq(1+a)\omega_g(1/n)$.

**c)** Par le résultat admis en Q2, le majorant tend vers zéro. La suite des polynômes trigonométriques $T_ng$ converge donc uniformément vers $g$ sur $\mathbb R$.

## Partie C — Inégalités de Bernstein

### I — Une identité algébrique

### Question 17

> [!INDICATION]
> Utilisez le théorème de d’Alembert–Gauss et cherchez une racine commune au polynôme et à sa dérivée.

#### Solution

Le polynôme $T=X^n+1$ a $n$ racines complexes comptées avec multiplicité. Une racine multiple serait aussi racine de $T'=nX^{n-1}$.

Pour $n=1$, $T'$ ne s’annule pas. Pour $n>1$, sa seule racine est 0, qui ne convient pas car $T(0)=1$.

Les $n$ racines sont donc simples. Elles ont toutes module 1 et aucune n’est égale à 1 puisque $T(1)=2$.

### Question 18

> [!INDICATION]
> Isolez dans le produit le facteur qui s’annule au point d’évaluation.

#### Solution

Puisque $T$ est unitaire, $T(X)=(X-z_k)\prod_{j\ne k}(X-z_j)$. En dérivant et en évaluant en $z_k$, seul subsiste le terme issu de la dérivation de $X-z_k$. Il vaut $\prod_{j\ne k}(z_k-z_j)$.

### Question 19

> [!INDICATION]
> Pour isoler le coefficient d’un pôle simple, multipliez par le facteur associé avant d’évaluer.

#### Solution

En multipliant la décomposition par $X-z_k$ puis en évaluant par prolongement en $z_k$, la Q18 donne
$$
\mu_k=\frac{z_k^\ell}{T'(z_k)}
=-\frac{z_k^{\ell+1}}{n},
$$
où la dernière égalité utilise $z_k^n=-1$. À l’infini sur l’axe réel, les fractions simples tendent vers zéro. La fonction $F$ tend vers zéro si $\ell<n$ et vers 1 si $\ell=n$. Le polynôme $E$, ayant une limite finie, est constant et égal à cette limite.

### Question 20

> [!INDICATION]
> Calculez la même dérivée à partir du quotient puis de sa décomposition.

#### Solution

À partir du quotient et de $T(1)=2$, on trouve
$$
F'(1)=\frac{2\ell-n}{4}.
$$
Cela vaut aussi pour $\ell=0$, qui correspond à un numérateur constant. En dérivant la décomposition, $E$ disparaît et Q19 donne
$$
F'(1)=\frac1n\sum_{k=1}^n\frac{z_k^{\ell+1}}{(z_k-1)^2}.
$$
En identifiant les deux valeurs,
$$
\ell=\frac n2+\frac2n\sum_{k=1}^n\frac{z_k^{\ell+1}}{(z_k-1)^2}.
$$

### Question 21

> [!INDICATION]
> Prouvez l’identité sur les monômes avant d’utiliser la linéarité. Pour la somme seule, choisissez un monôme de degré zéro.

#### Solution

**a)** Pour $P=X^\ell$, le membre gauche vaut $\ell X^\ell$. Dans le membre droit, $P(z_k X)=z_k^\ell X^\ell$. Le facteur de $X^\ell$ est exactement le membre droit de Q20. L’identité vaut donc pour chaque monôme de la base et les deux membres dépendent linéairement de $P$.
$$
XP'(X)=\frac n2P(X)+\frac2n\sum_{k=1}^n\frac{z_kP(z_kX)}{(z_k-1)^2}.
$$

**b)** On applique l’identité à $P=1$ pour obtenir
$$
\sum_{k=1}^n\frac{z_k}{(z_k-1)^2}=-\frac{n^2}{4}.
$$

### II — Bornes de dérivées

### Question 22

> [!INDICATION]
> Vérifiez que le supremum est fini, puis utilisez le nombre de racines d’un polynôme non nul.

#### Solution

Le cercle unité est compact, et $z\mapsto |P(z)|$ est continue. Le supremum est donc fini et positif ou nul. S’il vaut zéro, le polynôme s’annule sur tout le cercle, ce qui implique $P=0$. La réciproque est immédiate. L’égalité $|\lambda P(z)|=|\lambda|\,|P(z)|$ donne l’homogénéité, et l’inégalité triangulaire en chaque point du cercle donne celle de la norme après passage au supremum.

### Question 23

> [!INDICATION]
> Exprimez le conjugué d’un point du cercle à l’aide de son inverse.

#### Solution

Pour $|z|=1$, on a $\overline z=1/z$. Ainsi
$$
|z-1|^2=(z-1)(1/z-1)=-\frac{(z-1)^2}{z}.
$$
Comme $z\ne1$, il vient $z/(z-1)^2=-1/|z-1|^2<0$.

### Question 24

> [!INDICATION]
> Dans la majoration issue de Q21a, additionnez les modules des coefficients à l’aide de Q23 et Q21b.

#### Solution

Pour $n=0$, la dérivée est nulle. Si $n\geq1$ et $|z|=1$, alors $|z_kz|=1$ et $|zP'(z)|=|P'(z)|$. La Q21a donne
$$
|P'(z)|\leq\lVert P\rVert\left(\frac n2+
\frac2n\sum_{k=1}^n\left|\frac{z_k}{(z_k-1)^2}\right|\right).
$$
Tous les termes avant prise du module sont strictement négatifs par Q23. La somme des modules est donc l’opposé de la somme Q21b, c’est-à-dire $n^2/4$. Le facteur entre parenthèses vaut $n$. En prenant le supremum sur le cercle, $\lVert P'\rVert\leq n\lVert P\rVert$.

### Question 25

> [!INDICATION]
> Multipliez le polynôme trigonométrique par une exponentielle pour rendre ses indices tous positifs ou nuls.

#### Solution

Écrivons $q(t)=e^{-int}P(e^{it})$, où $P(X)=\sum_{k=-n}^n c_kX^{k+n}$ est de degré au plus $2n$. On a $\lVert q\rVert_\infty=\lVert P\rVert$ puisque $e^{it}$ parcourt le cercle. On dérive
$$
q'(t)=-in q(t)+i e^{-int}e^{it}P'(e^{it}).
$$
Toutes les exponentielles ont module 1. On obtient $\lVert q'\rVert_\infty\leq n\lVert q\rVert_\infty+\lVert P'\rVert$. La Q24 appliquée avec $2n$ donne la borne $3n\lVert q\rVert_\infty$.

## Partie D — Fonctions höldériennes

### I — Exemples

### Question 26

> [!INDICATION]
> À décalage fixé, étudiez comment décroît l’accroissement de la fonction puissance.

#### Solution

La puissance est croissante, ce qui donne la borne inférieure. Fixons $d=x-y$. Si $d=0$, l’inégalité est immédiate. Pour $d>0$, la fonction $u\mapsto(u+d)^\alpha-u^\alpha$ est continue sur $[0,+\infty[$. Sur $]0,+\infty[$, sa dérivée est
$$
\alpha\big((u+d)^{\alpha-1}-u^{\alpha-1}\big)\leq0.
$$
L’accroissement en $u=y$ est donc au plus sa valeur en $0$, égale à $d^\alpha$.

### Question 27

> [!INDICATION]
> Choisissez comme premier argument le plus grand des deux.

#### Solution

En appliquant Q26 après échange éventuel des deux points, $|h_\alpha(x)-h_\alpha(y)|\leq |x-y|^\alpha$. La fonction est $\alpha$-höldérienne sur $\mathbb R_+$ avec constante 1.

### Question 28

> [!INDICATION]
> Fixez un des points en zéro. Cherchez la limite qui rend le quotient incompatible avec une borne uniforme.

#### Solution

Pour le couple $(x,0)$ avec $x>0$, le quotient pour l’exposant $\beta$ vaut $x^{\alpha-\beta}$. Si $\beta>\alpha$, il diverge quand $x$ tend vers zéro.

Si $\beta<\alpha$, il diverge quand $x$ tend vers l’infini. Dans les deux cas, une constante valable sur tout $\mathbb R_+$ est impossible.

### Question 29

> [!INDICATION]
> Faites varier le point de départ en gardant le décalage égal à $y$.

#### Solution

Pour $0<y<1$, posons $D_y(x)=k(x+y)-k(x)$. La fonction est continue sur $[0,1-y]$ et sa dérivée intérieure est $\ln((x+y)/x)>0$.

Son maximum est atteint en $1-y$ et vaut $k(1)-k(1-y)=(y-1)\ln(1-y)$. Pour $y=1$, l’intervalle se réduit à zéro et les deux membres valent zéro avec la convention $0\ln 0=0$.

### Question 30

> [!INDICATION]
> Encadrez l’accroissement par ses valeurs aux deux extrémités. Comparez ces valeurs à une puissance du décalage.

#### Solution

La croissance utilisée en Q29 donne, pour $0<y<1$ et $0\leq x\leq1-y$,
$$
y\ln y\leq D_y(x)\leq -(1-y)\ln(1-y).
$$
D’une part $y^{1-\alpha}|\ln y|$ est borné sur $]0,1]$, puisqu’il tend vers zéro en zéro. Donc $|y\ln y|\leq K_1y^\alpha$. D’autre part, $-\ln(1-y)=\int_0^y (1-t)^{-1}\,\mathrm dt\leq y/(1-y)$. Ainsi $-(1-y)\ln(1-y)\leq y\leq y^\alpha$.

Ces deux bornes, puis l’échange éventuel des deux points, donnent l’inégalité höldérienne de constante $\max(K_1,1)$ pour tous les couples de points. Pour les décalages 0 et 1, la différence est nulle.

### II — Approximation directe

### Question 31

> [!INDICATION]
> La combinaison linéaire doit conserver la périodicité et un contrôle höldérien.

#### Solution

Une fonction $\alpha$-höldérienne est continue, et toute fonction de $H_{2\pi}^\alpha$ est périodique par définition. La fonction nulle appartient à l’ensemble. Pour deux fonctions de constantes $K_f,K_g$ et des scalaires complexes $\lambda,\mu$, l’inégalité triangulaire donne une borne de coefficient $|\lambda|K_f+|\mu|K_g$ pour $\lambda f+\mu g$. On peut ajouter 1 à cette constante si nécessaire pour la rendre strictement positive. La combinaison reste périodique, ce qui prouve la stabilité et la propriété de sous-espace.

### Question 32

> [!INDICATION]
> Utilisez l’estimation par module de continuité en choisissant un indice dont le double ne dépasse pas le degré autorisé.

#### Solution

Pour $g\in H_{2\pi}^\alpha$ de constante $K$, on a $\omega_g(h)\leq Kh^\alpha$. Pour $n\geq2$, posons $m=\lfloor n/2\rfloor$. Comme $T_mg\in\mathcal T_{2m}\subseteq\mathcal T_n$, Q16 donne
$$
\begin{aligned}
0\leq\delta_n(g)&\leq \lVert T_mg-g\rVert_\infty,\\
\lVert T_mg-g\rVert_\infty&\leq (1+a)K m^{-\alpha}.
\end{aligned}
$$
Comme $m$ est équivalent à $n/2$, la borne est $O(n^{-\alpha})$.

### III — Réciproque

### Question 33

> [!INDICATION]
> Restreignez la minimisation à un sous-ensemble fermé borné de l’espace des polynômes trigonométriques.

#### Solution

Sur $\mathcal T_n$, l’application $q\mapsto\lVert f-q\rVert_\infty$ est continue, car la différence de deux de ses valeurs est en module au plus la distance entre les deux arguments. Le sous-niveau où elle vaut au plus $\lVert f\rVert_\infty$ contient $q=0$. Il est fermé et borné puisque, pour ces $q$,
$$
\lVert q\rVert_\infty\leq\lVert f-q\rVert_\infty+\lVert f\rVert_\infty
\leq2\lVert f\rVert_\infty.
$$
L’espace $\mathcal T_n$ est de dimension finie, car engendré par $2n+1$ exponentielles. Le sous-niveau est donc compact. La fonction atteint un minimum sur ce compact, qui est aussi un minimum global puisque partout ailleurs la valeur dépasse celle obtenue en zéro.

### Question 34

> [!INDICATION]
> Majorez d’abord la différence des approximants par la somme de leurs erreurs d’approximation.

#### Solution

Comme $p_{n+1}-p_n\in\mathcal T_{2^{n+1}}$, Q25 donne
$$
\lVert p'_{n+1}-p'_n\rVert_\infty
\leq3\,2^{n+1}\lVert p_{n+1}-p_n\rVert_\infty.
$$
La dernière norme est au plus $C(2^{-(n+1)\alpha}+2^{-n\alpha})$ par l’inégalité triangulaire et les choix des approximants. La borne demandée suit avec $C'=6C(1+2^{-\alpha})$.

### Question 35

> [!INDICATION]
> Décomposez la dérivée en une somme télescopique et calculez la somme géométrique des majorants.

#### Solution

Posons $r=2^{1-\alpha}>1$. On écrit $p_n'=p_0'+\sum_{j=0}^{n-1}(p'_{j+1}-p'_j)$. Par Q34,
$$
\lVert p_n'\rVert_\infty\leq\lVert p_0'\rVert_\infty
+C'\frac{r^n-1}{r-1}.
$$
En majorant $r^n-1$ par $r^n$, on obtient la borne demandée. Pour $n=0$, la somme est vide et la majoration reste valable.

### Question 36

> [!INDICATION]
> Absorbez le terme initial dans la puissance, qui est toujours au moins 1.

#### Solution

Comme $r^n\geq1$, la Q35 donne $\lVert p'_n\rVert_\infty\leq Ar^n$ avec $A=\lVert p'_0\rVert_\infty+C'/(r-1)>0$.

### Question 37

> [!INDICATION]
> Insérez les valeurs de l’approximant aux deux points, puis utilisez sa borne de dérivée.

#### Solution

On a, pour tous $x,y\in\mathbb R$ et $n\in\mathbb N$,
$$
|f(x)-f(y)|\leq2\lVert f-p_n\rVert_\infty+|p_n(x)-p_n(y)|.
$$
Par intégration de la dérivée sur le segment, le dernier terme est au plus $\lVert p_n'\rVert_\infty|x-y|$. On utilise alors les bornes d’approximation et de dérivée,
$$
|f(x)-f(y)|\leq C2^{1-n\alpha}+A2^{(1-\alpha)n}|x-y|.
$$

### Question 38

> [!INDICATION]
> Choisissez l’échelle dyadique comparable à la distance entre les deux points. Pour les grandes distances, la borne uniforme suffit.

#### Solution

Posons $d=|x-y|$. Si $0<d\leq1$, prenons $n\geq0$ tel que $2^{-n-1}\leq d\leq2^{-n}$. Alors $2^{-n\alpha}\leq 2^\alpha d^\alpha$, tandis que
$$
2^{(1-\alpha)n}d=(2^nd)^{1-\alpha}d^\alpha\leq d^\alpha.
$$
La Q37 donne donc une borne de coefficient $C2^{1+\alpha}+A$ devant $d^\alpha$.

Pour $d>1$, on a $|f(x)-f(y)|\leq2\lVert f\rVert_\infty d^\alpha$, puisque $f$ est continue et périodique, donc bornée. Le cas $d=0$ est immédiat. Le maximum des deux coefficients est une constante höldérienne sur $\mathbb R$.

## Bilan

- Contrôlez les fréquences avant de fixer le degré d’un polynôme trigonométrique.
- Choisissez des constantes indépendantes du point d’évaluation et du degré.
- Dans la réciproque, prenez un degré dyadique comparable à l’inverse de la distance.
