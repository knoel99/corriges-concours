# CAPES Maths — Épreuve d'admissibilité 2 (bac+3) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures, calculatrice autorisée, sans document. Trois parties indépendantes, deux documents joints.

## Partie 1 — Exercices de critique et rédaction mathématique

Pour chacun des exercices ci-après, on critique la réponse proposée, puis on en rédige une version correcte.

### Exercice 1

**Énoncé.** Résoudre dans $\mathbb R$ l'équation $x^3+x^2+x+1=0$.

**Réponse proposée.** Si $x$ est solution, en multipliant l'équation par $x$, on obtient $x^4+x^3+x^2+x=0$. Mais $x^3+x^2+x=-1$, donc $x^4=1$.
 Il s'ensuit que les seules solutions de l'équation sont $x=-1$ et $x=1$.

**Critique.** Le raisonnement proposé n'est qu'une **analyse** : il établit une condition nécessaire ($x$ solution $\Rightarrow x^4=1$, donc $x\in\{-1,1\}$), mais la **synthèse** manque : rien ne garantit que $-1$ et $1$
 sont effectivement solutions. Or $1$ n'est pas solution ($1+1+1+1=4\neq0$). De plus, multiplier une équation par $x$ n'est pas une équivalence : cela peut introduire une racine parasite ($x=0$).

**Rédaction correcte.** Pour tout $x\in\mathbb R$,

$$
\begin{aligned}
x^3+x^2+x+1&=x^2(x+1)+(x+1)\\
&=(x+1)(x^2+1).
\end{aligned}
$$

Or $x^2+1>0$ pour tout réel $x$, donc

$$
\begin{aligned}
x^3+x^2+x+1=0&\iff x+1=0\\
&\iff x=-1.
\end{aligned}
$$

$$
\boxed{\mathcal S=\{-1\}.}
$$

### Exercice 2

**Énoncé.** Soit $f$ une fonction définie sur $\mathbb R$, à valeurs réelles, continue sur $\mathbb R$ et telle que : $\forall x\in\mathbb R,\ (f(x))^2=1$. Montrer que $f$ est constante.

**Réponse proposée.** Soit $x\in\mathbb R$. L'équation $(f(x))^2=1$ admet pour solutions $1$ ou $-1$, donc $f$
 est constante égale à $-1$ ou $1$.

**Critique.** L'hypothèse s'écrit $\forall x\in\mathbb R,\ \exists\varepsilon\in\{-1,1\},\ f(x)=\varepsilon$, où $\varepsilon$ dépend *a priori* de $x$ : la réponse proposée échange les quantificateurs ($\exists\varepsilon\ \forall x$). Rien ne garantit que la valeur choisie ne change pas avec $x$. L'hypothèse de continuité, pourtant décisive, n'est pas utilisée.

**Rédaction correcte.** Par hypothèse, $\forall x\in\mathbb R,\ f(x)\in\{-1,1\}$. Supposons $f$ non constante : il existe $x_1,x_2\in\mathbb R$ tels que $f(x_1)\neq f(x_2)$, par exemple $f(x_1)=1$
 et $f(x_2)=-1$. La fonction $f$ étant continue sur $\mathbb R$, elle est continue sur le segment $[x_1,x_2]$ ; comme $0$
 est strictement compris entre $f(x_2)=-1$ et $f(x_1)=1$, le **théorème des valeurs intermédiaires** fournit $x_3\in[x_1,x_2]$ tel que $f(x_3)=0$. Mais alors $(f(x_3))^2=0\neq1$,
 ce qui contredit l'hypothèse. Donc $f$ est constante.

$$
\boxed{f\text{ est constante, égale à }1\text{ ou à }-1.}
$$

### Exercice 3

**Énoncé.** Soit la suite $(u_n)_{n\in\mathbb N}$ définie par $u_0=1$ et, pour tout $n\geq0$, $u_{n+1}=2u_n+1$. La suite $(u_n)_{n\in\mathbb N}$ est-elle convergente ? Si oui, donner la valeur de sa limite.

**Réponse proposée.** On montre par récurrence que la suite est positive (la proposition $\mathcal H_n$ : « pour tout $n\in\mathbb N$, $u_n\geq0$ » est initialisée en $n=0$ et héréditaire). Or $u_{n+1}-u_n=u_n+1\geq0$,
 donc la suite est croissante. Ainsi, elle converge. Soit $\ell$ sa limite. Par continuité de $x\mapsto2x+1$, $\ell$ vérifie $\ell=2\ell+1$, soit $\ell=-1$.
 La suite converge donc vers $-1$.

**Critique.** Trois défauts. (i) La proposition de récurrence est mal quantifiée (« on suppose $\mathcal H_n$ vraie pour tout $n$ »). (ii) « Croissante donc convergente » est faux : il faut de plus que la suite soit **majorée**. (iii) La limite trouvée, $\ell=-1<0$, contredit la positivité de la suite : cette contradiction aurait dû alerter. La suite est en réalité divergente.

**Rédaction correcte.** Posons $v_n=u_n+1$. Alors

$$
\begin{aligned}
v_{n+1}&=u_{n+1}+1\\
&=2u_n+2=2v_n.
\end{aligned}
$$

et $v_0=u_0+1=2$. La suite $(v_n)$ est donc géométrique de raison $2$ et de premier terme $2$ :

$$
\boxed{u_n=2^{n+1}-1\quad(n\in\mathbb N).}
$$

Comme $2^{n+1}\to+\infty$, la suite $(u_n)$ **diverge vers $+\infty$** : elle n'est pas convergente.

*Variante.* Une récurrence immédiate donne $u_n\geq0$, et $u_{n+1}-u_n=u_n+1>0$ : la suite est strictement croissante. Si elle était majorée, elle convergerait vers un réel $\ell$ qui, par continuité de $x\mapsto2x+1$, vérifierait $\ell=2\ell+1$,
 soit $\ell=-1$. Or $u_n\geq0$ pour tout $n$ entraîne $\ell\geq0$ : contradiction. La suite n'est donc pas majorée et diverge vers $+\infty$.
 $\square$

## Partie 2 — Questions sur le document 1

### Question 1

Échelonner la matrice $\begin{pmatrix}1&1&1\\-1&2&3\\2&2&1\end{pmatrix}$ à l'aide d'opérations élémentaires dûment détaillées.

$$
\begin{pmatrix}1&1&1\\-1&2&3\\2&2&1\end{pmatrix}\xrightarrow[\substack{L_2\leftarrow L_2+L_1\\ L_3\leftarrow L_3-2L_1}]{}\begin{pmatrix}1&1&1\\0&3&4\\0&0&-1\end{pmatrix}.
$$

La matrice obtenue est échelonnée (le nombre de zéros précédant le premier terme non nul d'une ligne augmente strictement ligne par ligne), avec pour pivots $1$, $3$, $-1$. Le rang d'une matrice échelonnée étant le nombre de ses lignes non nulles :

$$
\boxed{\operatorname{rg}\begin{pmatrix}1&1&1\\-1&2&3\\2&2&1\end{pmatrix}=3.}
$$

### Question 2

Démontrer que l'ensemble des solutions d'un système linéaire homogène $AX=0_{\mathbb R^m}$, où $A\in\mathcal M_{m,n}$ et d'inconnue $X\in\mathbb R^n$, est un sous-espace vectoriel de $\mathbb R^n$.

Notons $E_0=\{X\in\mathbb R^n : AX=0_{\mathbb R^m}\}$. On a $A\,0_{\mathbb R^n}=0_{\mathbb R^m}$, donc $0_{\mathbb R^n}\in E_0$. Soient $X_1,X_2\in E_0$ et $\lambda,\mu\in\mathbb R$. Par linéarité du produit matriciel :

$$
\begin{aligned}
A(\lambda X_1+\mu X_2)&=\lambda AX_1+\mu AX_2\\
&=\lambda\,0_{\mathbb R^m}+\mu\,0_{\mathbb R^m}\\
&=0_{\mathbb R^m}.
\end{aligned}
$$

Donc $\lambda X_1+\mu X_2\in E_0$ : $E_0$ est stable par combinaison linéaire et non vide, c'est donc un sous-espace vectoriel de $\mathbb R^n$. $\square$

### Question 3

Soit $\lambda\in\mathbb R$ et $U=\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$. Déterminer, en fonction de $\lambda$, le rang de $U-\lambda I_3$, puis en déduire les valeurs propres de $U$.

$$
U-\lambda I_3=\begin{pmatrix}1-\lambda&1&1\\1&1-\lambda&1\\1&1&1-\lambda\end{pmatrix}\xrightarrow[L_1\leftrightarrow L_3]{}\begin{pmatrix}1&1&1-\lambda\\1&1-\lambda&1\\1-\lambda&1&1\end{pmatrix}
$$

$$
\xrightarrow[\substack{L_2\leftarrow L_2-L_1\\ L_3\leftarrow L_3-(1-\lambda)L_1}]{}\begin{pmatrix}1&1&1-\lambda\\0&-\lambda&\lambda\\0&\lambda&2\lambda-\lambda^2\end{pmatrix}\xrightarrow[L_3\leftarrow L_3+L_2]{}\begin{pmatrix}1&1&1-\lambda\\0&-\lambda&\lambda\\0&0&\lambda(3-\lambda)\end{pmatrix}.
$$

Les opérations élémentaires ne changent pas le rang (Proposition 1), qui vaut le nombre de lignes non nulles de la forme échelonnée :

- si $\lambda=0$ : $\operatorname{rg}(U-\lambda I_3)=1$ ;
- si $\lambda=3$ : $\operatorname{rg}(U-\lambda I_3)=2$ ;
- sinon : $\operatorname{rg}(U-\lambda I_3)=3$.

Une matrice carrée est inversible si et seulement si son rang est maximal (Proposition 2) ; $\lambda$ est valeur propre de $U$ si et seulement si $U-\lambda I_3$ n'est pas inversible, c'est-à-dire $\operatorname{rg}(U-\lambda I_3)<3$.

$$
\boxed{\operatorname{Sp}(U)=\{0,3\}.}
$$

### Question 4

Démontrer la Proposition 3 (solutions d'un système linéaire non homogène) : si $AX=B$ possède au moins une solution $X_0$, l'ensemble des solutions est $\{X_0+u : u\in E_0\}$, où $E_0$ est l'ensemble des solutions du système homogène associé $AX=0_{\mathbb R^m}$.

Soit $X_0$ une solution de $AX=B$. Pour $X\in\mathbb R^n$ :

$$
\begin{aligned}
AX=B&\iff AX-AX_0=0_{\mathbb R^m}\\
&\iff A(X-X_0)=0_{\mathbb R^m}\\
&\iff X-X_0\in E_0\\
&\iff X\in X_0+E_0.
\end{aligned}
$$

L'ensemble des solutions est donc exactement $\{X_0+u : u\in E_0\}$. $\square$

### Question 5

Quel est le point en commun entre la Proposition 3 et la résolution de l'équation différentielle $y'=ay+b$, où $a,b:I\to\mathbb R$ sont continues sur un intervalle $I$ de $\mathbb R$ ?

Dans les deux cas, l'ensemble des solutions d'un problème **affine** (système non homogène $AX=B$, ou équation $y'=ay+b$) s'écrit :

**une solution particulière + l'espace vectoriel des solutions du problème homogène associé.**

Pour $AX=B$ : $\mathrm{Sol}=X_0+E_0$ avec $E_0$ sous-espace vectoriel de $\mathbb R^n$. Pour $y'=ay+b$
 : si $y_0$ est une solution particulière, $\mathrm{Sol}=\{y_0+y_h\}$ où les solutions $y_h$ de $y'=ay$ forment une droite vectorielle (sous-espace vectoriel de dimension $1$).
 C'est la **structure affine** de l'ensemble des solutions. $\square$

### Question 6

Démontrer le Théorème 2 (caractérisation d'une combinaison linéaire d'équations), en utilisant les résultats qui précèdent : si $S$ est un système de $m$ équations à $n$ inconnues de solutions non vides et si $S'=S\cup\{(E)\}$ admet les mêmes solutions que $S$,
 alors $(E)$ est une combinaison linéaire des équations de $S$.

Appliquons l'algorithme de Gauss à $S$ : on obtient un système échelonné équivalent, de rang $r$ ; d'après la Remarque 3, $r$ inconnues (les inconnues principales) s'expriment en fonction des $n-r$ autres, libres. L'équation $(E)$
 peut, par combinaison linéaire des $r$ équations échelonnées, être débarrassée des inconnues principales : on obtient une équation $(E')$ ne portant que sur les $n-r$ inconnues libres, et $(E)$ est combinaison linéaire des équations de $S$
 si et seulement si $(E')$ est l'équation triviale $0=0$.

Supposons que $S'$ ait les mêmes solutions que $S$. Si $(E')$ n'était pas triviale, elle imposerait une contrainte supplémentaire sur les inconnues libres, et l'ensemble des solutions de $S'$ serait strictement inclus dans celui de $S$
 (les inconnues libres peuvent prendre toutes les valeurs réelles dans une solution de $S$). Cela contredit l'égalité des ensembles de solutions. Donc $(E')$ est triviale, c'est-à-dire que $(E)$ est combinaison linéaire des équations de $S$. $\square$

### Question 7

Dans le Théorème 2, obtient-on un résultat valide si l'on remplace l'assertion « Si $S'$ admet les mêmes solutions que $S$ alors $(E)$ est combinaison linéaire des équations de $S$ » par l'équivalence « $S'$
 admet les mêmes solutions que $S$ si, et seulement si, $(E)$ est une combinaison linéaire des équations de $S$ » ?

**Oui**, l'équivalence est valide. Notons $S'=S\cup\{(E)\}$.

- ($\Rightarrow$) Si $S'$ a les mêmes solutions que $S$, le Théorème 2 (Question 6) donne : $(E)$ est combinaison linéaire des équations de $S$.
- ($\Leftarrow$) Réciproquement, si $(E)=\sum_{i=1}^m\alpha_i E_i$, alors toute solution de $S$ vérifie $(E)$, donc $\mathrm{Sol}(S')=\mathrm{Sol}(S)\cap\mathrm{Sol}(E)=\mathrm{Sol}(S)$
 (l'opération élémentaire $L_{m+1}\leftarrow L_{m+1}-\sum_i\alpha_i L_i$ transforme $(E)$ en $0=0$). $\square$

### Question 8

Soit $P$ le plan de l'espace passant par l'origine du repère et engendré par $\vec\imath$ et $\vec\jmath+2\vec k$. Démontrer, à l'aide d'un calcul de rang, que $P=\{(x,y,z)\in\mathbb R^3 : z-2y=0\}$.

Soit $M=(x,y,z)$. Dans la base $(\vec\imath,\vec\jmath,\vec k)$, $\vec\imath=(1,0,0)$ et $\vec\jmath+2\vec k=(0,1,2)$. Par définition de $P$ :

$$
M\in P\iff (\overrightarrow{OM},\vec\imath,\vec\jmath+2\vec k)\text{ est liée}\iff \operatorname{rg}\begin{pmatrix}x&1&0\\y&0&1\\z&0&2\end{pmatrix}<3.
$$

Par opérations sur les colonnes puis sur les lignes :

$$
\operatorname{rg}\begin{pmatrix}x&1&0\\y&0&1\\z&0&2\end{pmatrix}=\operatorname{rg}\begin{pmatrix}1&0&x\\0&1&y\\0&2&z\end{pmatrix}=\operatorname{rg}\begin{pmatrix}1&0&x\\0&1&y\\0&0&z-2y\end{pmatrix}.
$$

Cette dernière matrice est échelonnée ; son rang est $<3$ si et seulement si sa troisième ligne est nulle, c'est-à-dire $z-2y=0$. Donc

$$
\boxed{P=\{(x,y,z)\in\mathbb R^3 : z-2y=0\}.}
$$

$\square$

### Question 9

Soient deux plans distincts $P_1$ et $P_2$ d'équations respectives $3x+4y-z=1$ et $x+y+z=5$. Démontrer, à l'aide de la méthode de Gauss, que $P_1\cap P_2$ est une droite dont on déterminera un point et un vecteur directeur.

Le système est $\begin{cases}x+y+z=5\\3x+4y-z=1\end{cases}$. Matrice augmentée :

$$
\begin{pmatrix}1&1&1&\vline&5\\3&4&-1&\vline&1\end{pmatrix}\xrightarrow[L_2\leftarrow L_2-3L_1]{}\begin{pmatrix}1&1&1&\vline&5\\0&1&-4&\vline&-14\end{pmatrix}.
$$

On en tire $y=-14+4z$ et $x=5-y-z=19-5z$. En prenant $z$ comme paramètre :

$$
(x,y,z)=(19,-14,0)+z\,(-5,4,1).
$$

$$
\boxed{P_1\cap P_2\text{ est la droite passant par }A(19,-14,0)\text{ et de vecteur directeur }\vec u(-5,4,1).}
$$

### Question 10

Retrouver, à l'aide du théorème de Rouché-Fontené, les différents cas possibles d'intersection de deux plans quelconques $P_1\cap P_2$ dans l'espace, et les illustrer par des croquis en perspective.

Écrivons $(E_1):a_1x+b_1y+c_1z=d_1$ et $(E_2):a_2x+b_2y+c_2z=d_2$, $A=\begin{pmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\end{pmatrix}$ et $A'=(A\,|\,B)$. Les plans étant donnés par une équation, $\operatorname{rg}(A)\in\{1,2\}$. D'après le théorème de Rouché-Fontené :

- **Cas $\operatorname{rg}(A')>\operatorname{rg}(A)$** (donc $\operatorname{rg}(A')=2$ et $\operatorname{rg}(A)=1$) : le système est incompatible. Les deux plans ont la même direction mais sont distincts : **plans strictement parallèles**, $P_1\cap P_2=\varnothing$. *Croquis : deux plans horizontaux superposés en perspective, distincts, sans point commun.*
- **Cas $\operatorname{rg}(A')=\operatorname{rg}(A)=1$** : les deux équations sont proportionnelles, les plans sont **confondus**, $P_1\cap P_2=P_1$. *Croquis : un seul plan dessiné.*
- **Cas $\operatorname{rg}(A')=\operatorname{rg}(A)=2$** : le système est compatible avec $n-r=3-2=1$ indéterminée : **l'intersection est une droite**. *Croquis : deux plans sécants se coupant suivant une droite tracée en gras.*

Le cas $\operatorname{rg}(A)=3$ est impossible (deux équations seulement). $\square$

![Figure 1 — Les trois configurations de deux plans](figures/p2-q10-plans.svg)

### Question 11

**i)** Démontrer la Remarque 6 (produit vectoriel) : deux plans $P_1,P_2$ de $\mathbb R^3$ sont parallèles si et seulement si leurs vecteurs normaux $\vec n_1,\vec n_2$ vérifient $\vec n_1\wedge\vec n_2=\vec 0$.

$P_1\parallel P_2$ signifie que leurs directions coïncident, c'est-à-dire que les normales $\vec n_1,\vec n_2$ sont colinéaires. Or deux vecteurs de $\mathbb R^3$ sont colinéaires si et seulement si leur produit vectoriel est nul. $\square$

**ii)** Pour quelle(s) valeur(s) de $m\in\mathbb R$ les plans d'équations $(1-m)x+(2+m)y-z=3$ et $2x+(4-2m)y+(m-2)z=m$ sont-ils parallèles ?

Les normales sont $\vec n_1=(1-m,2+m,-1)$ et $\vec n_2=(2,4-2m,m-2)$. Leur produit vectoriel vaut

$$
\vec n_1\wedge\vec n_2=\big(m(m-2),\ m(m-3),\ 2m(m-4)\big).
$$

Les plans sont parallèles si et seulement si ce vecteur est nul, c'est-à-dire

$$
\begin{aligned}
m(m-2)&=0,\quad m(m-3)=0,\\
2m(m-4)&=0.
\end{aligned}
$$

dont la seule solution commune est $m=0$.

$$
\boxed{\text{Les plans sont parallèles si et seulement si }m=0.}
$$

**iii)** Pour $m=0$, les équations deviennent $x+2y-z=3$ et $2x+4y-2z=0$, soit $x+2y-z=0$ après division par $2$.
 Les premiers membres sont proportionnels mais les seconds membres ($3$ et $0$) diffèrent : les plans sont strictement parallèles, **non confondus** (par exemple $(0,0,0)$ appartient au second, pas au premier).

$$
\boxed{\text{Pour }m=0,\text{ les plans sont parallèles non confondus.}}
$$

### Question 12

Soient $P_1,P_2$ deux plans d'équations respectives $(E_1)$ et $(E_2)$, non parallèles. Expliquer pourquoi l'équation $\alpha(E_1)+\beta(E_2)$, où $\alpha,\beta$ sont deux réels non tous deux nuls, représente toujours un plan.

Écrivons $(E_1):ax+by+cz=d$ et $(E_2):a'x+b'y+c'z=d'$. L'équation $\alpha(E_1)+\beta(E_2)$ s'écrit

$$
(\alpha a+\beta a')x+(\alpha b+\beta b')y+(\alpha c+\beta c')z=\alpha d+\beta d'.
$$

C'est l'équation d'un plan si et seulement si le triplet de coefficients $(\alpha a+\beta a',\alpha b+\beta b',\alpha c+\beta c')$ est non nul. Or $P_1$ et $P_2$ non parallèles ont des normales $\vec n_1=(a,b,c)$ et $\vec n_2=(a',b',c')$
 non colinéaires : la famille $(\vec n_1,\vec n_2)$ est libre. Si $\alpha\vec n_1+\beta\vec n_2=\vec 0$ avec $(\alpha,\beta)\neq(0,0)$, on contredit cette liberté. Le triplet est donc non nul, et $\alpha(E_1)+\beta(E_2)$ représente bien toujours un plan. $\square$

### Question 13

**i)** $\operatorname{tr}:\mathcal M_n\to\mathbb R$ est une forme linéaire. Pour $A=(a_{ij}),B=(b_{ij})\in\mathcal M_n$ et $\lambda\in\mathbb R$ :

$$
\begin{aligned}
\operatorname{tr}(\lambda A+B)&=\sum_{i=1}^n(\lambda a_{ii}+b_{ii})\\
&=\lambda\sum_{i=1}^n a_{ii}+\sum_{i=1}^n b_{ii}\\
&=\lambda\operatorname{tr}(A)+\operatorname{tr}(B).
\end{aligned}
$$

C'est une application linéaire à valeurs dans $\mathbb R$ : une forme linéaire sur $\mathcal M_n$.

**ii)** $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ pour tout $(A,B)\in\mathcal M_n^2$. Avec $A=(a_{ij}),B=(b_{ij})$ :

$$
\begin{aligned}
\operatorname{tr}(AB)&=\sum_{i=1}^n\Big(\sum_{k=1}^n a_{ik}b_{ki}\Big)\\
&=\sum_{k=1}^n\sum_{i=1}^n b_{ki}a_{ik}\\
&=\operatorname{tr}(BA),
\end{aligned}
$$

par interversion des sommes finies.

**iii)** Exemple de forme linéaire $\phi$ sur $\mathcal M_n$ ne vérifiant pas $\phi(AB)=\phi(BA)$ pour tout couple : prenons $n=2$ et $\phi:M=(m_{ij})\mapsto m_{1,1}$,
 qui est linéaire. Avec $A=E_{1,2}$ et $B=E_{2,1}$ : $AB=E_{1,1}$ donc $\phi(AB)=1$, tandis que $BA=E_{2,2}$
 donc $\phi(BA)=0$. Ainsi $\phi(AB)\neq\phi(BA)$.

**iv)** Soit $\phi$ une forme linéaire sur $\mathcal M_n$ telle que $\forall(A,B)\in\mathcal M_n^2,\ \phi(AB)=\phi(BA)$. Montrons que $\phi$ est proportionnelle à $\operatorname{tr}$,
 en utilisant la base canonique $(E_{ij})$ et la relation $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

- Pour $i\neq j$ : $\phi(E_{ii})=\phi(E_{ij}E_{ji})=\phi(E_{ji}E_{ij})=\phi(E_{jj})$. Tous les $\phi(E_{ii})$ sont donc égaux à un même réel $\lambda$.
- Pour $i\neq j$ : $\phi(E_{ij})=\phi(E_{ii}E_{ij})=\phi(E_{ij}E_{ii})=\phi(0)=0$.

Pour $M=\sum_{i,j}m_{ij}E_{ij}$, par linéarité :

$$
\begin{aligned}
\phi(M)&=\sum_{i,j}m_{ij}\phi(E_{ij})\\
&=\lambda\sum_{i}m_{ii}=\lambda\operatorname{tr}(M).
\end{aligned}
$$

Donc $\phi=\lambda\operatorname{tr}$. $\square$

### Question 14

Montrer, en utilisant la trace, qu'il n'existe pas de matrices $A,B\in\mathcal M_n$ telles que $AB-BA=I_n$.

Pour tous $A,B\in\mathcal M_n$, par linéarité de la trace et la Question 13(ii) :

$$
\operatorname{tr}(AB-BA)=\operatorname{tr}(AB)-\operatorname{tr}(BA)=0.
$$

Or $\operatorname{tr}(I_n)=n\neq0$. Si $AB-BA=I_n$ était réalisée, on aurait $0=n$ : contradiction.

$$
\boxed{\text{Il n'existe pas de telles matrices }A,B.}\quad\square
$$

### Question 15

Une forme linéaire non nulle $\phi$ sur $E$ est-elle toujours injective ? Toujours surjective ?

- **Surjectivité.** $\operatorname{Im}\phi$ est un sous-espace vectoriel de $\mathbb R$, non réduit à $\{0\}$ car $\phi\neq0$. Le seul sous-espace vectoriel non nul de $\mathbb R$
 est $\mathbb R$ lui-même : $\operatorname{Im}\phi=\mathbb R$. **Toute forme linéaire non nulle est surjective.**
- **Injectivité.** Par le théorème du rang, $\dim\ker\phi=\dim E-\operatorname{rg}\phi=\dim E-1$. La forme $\phi$ est injective si et seulement si $\ker\phi=\{0\}$, c'est-à-dire $\dim E=1$. Elle n'est donc **pas toujours injective** (dès que $\dim E\geq2$,
 par exemple $\phi:(x,y)\mapsto x$ sur $\mathbb R^2$).

$$
\boxed{\text{Non toujours injective ; toujours surjective.}}
$$

### Question 16

Justifier que la famille $\left(\tfrac12X(X-1),\ \tfrac12(X-1)(X-2),\ -X(X-2)\right)$ est une base de $\mathbb R_2[X]$, et préciser sa base duale.

Posons $P_0=\tfrac12X(X-1)$, $P_1=\tfrac12(X-1)(X-2)$, $P_2=-X(X-2)$, et notons $\mathrm{ev}_a$ la forme « évaluation en $a$ » pour $a\in\{0,1,2\}$. On calcule :

$$
\begin{aligned}
\mathrm{ev}_0(P_0)=0,&\quad \mathrm{ev}_1(P_0)=0,\quad \mathrm{ev}_2(P_0)=1,\\
\mathrm{ev}_0(P_1)=1,&\quad \mathrm{ev}_1(P_1)=0,\quad \mathrm{ev}_2(P_1)=0,\\
\mathrm{ev}_0(P_2)=0,&\quad \mathrm{ev}_1(P_2)=1,\quad \mathrm{ev}_2(P_2)=0.
\end{aligned}
$$

**Liberté.** Si $\alpha P_0+\beta P_1+\gamma P_2=0$, en évaluant en $0$ on obtient $\beta=0$, en $1$ on obtient $\gamma=0$,
 en $2$ on obtient $\alpha=0$. La famille est libre. Elle compte $3$ vecteurs dans $\mathbb R_2[X]$, espace de dimension $3$
 : c'est une **base** de $\mathbb R_2[X]$ (ce sont les polynômes de Lagrange associés aux nœuds $0,1,2$, dans l'ordre $2,0,1$).

**Base duale.** La base duale $(P_0^*,P_1^*,P_2^*)$ vérifie $P_i^*(P_j)=\delta_{ij}$. D'après le calcul ci-dessus :

$$
\boxed{\begin{aligned}
P_0^*&=\mathrm{ev}_2,\quad P_1^*=\mathrm{ev}_0,\\
P_2^*&=\mathrm{ev}_1.
\end{aligned}}
$$

### Question 17

Donner une preuve de la Proposition 5 (base de l'espace dual) en utilisant les résultats qui la précèdent.

Soit $\mathcal B=(e_1,\dots,e_n)$ une base de $E$ et, pour $x\in E$, $x_i$ sa $i$-ème coordonnée ; posons $\varphi_i(x)=x_i$.

1. Par définition des coordonnées : $\forall x\in E,\ x=\sum_{i=1}^n x_i e_i=\sum_{i=1}^n\varphi_i(x)e_i$.
2. Les coordonnées de $e_j$ sont $(\delta_{1j},\dots,\delta_{nj})$, donc $\varphi_i(e_j)=\delta_{ij}$.
3. **Liberté de $(\varphi_1,\dots,\varphi_n)$** : si $\sum_i\alpha_i\varphi_i=0$ (forme nulle), en évaluant sur $e_j$ : $\sum_i\alpha_i\varphi_i(e_j)=\alpha_j=0$ pour tout $j$.
 La famille est libre. Comme $\dim E^*=n$ (Remarque 8) et qu'elle compte $n$ vecteurs libres, c'est une base de $E^*$ : la **base duale** de $\mathcal B$. $\square$

### Question 18

Rédiger une démonstration du Théorème 4 (hyperplans et noyaux de formes linéaires) à partir des commentaires sur la démonstration.

**1)** Soit $H$ un sous-espace vectoriel de $E$. Montrons : $H$ hyperplan $\iff H=\ker\varphi$ pour une forme linéaire non nulle $\varphi$.

($\Leftarrow$) Soit $\varphi\in E^*$, $\varphi\neq0$, et $H=\ker\varphi$. L'image $\operatorname{Im}\varphi$
 est un sous-espace vectoriel non nul de $\mathbb R$, donc $\operatorname{Im}\varphi=\mathbb R$ : $\operatorname{rg}\varphi=1$. Par le théorème du rang, $\dim H=\dim E-1$ : $H$ est un hyperplan.

($\Rightarrow$) Soit $H$ un hyperplan. Prenons une base $(e_1,\dots,e_{n-1})$ de $H$ et complétons-la en une base $(e_1,\dots,e_n)$
 de $E$ ; soit $(\varphi_1,\dots,\varphi_n)$ la base duale associée. Montrons $H=\ker\varphi_n$ par double inclusion. Pour $i<n$, $\varphi_n(e_i)=0$,
 donc $H=\mathrm{Vect}(e_1,\dots,e_{n-1})\subseteq\ker\varphi_n$. Réciproquement, si $x=\sum_{i=1}^n x_ie_i\in\ker\varphi_n$, alors $x_n=\varphi_n(x)=0$, donc $x\in\mathrm{Vect}(e_1,\dots,e_{n-1})=H$. Ainsi $H=\ker\varphi_n$
 avec $\varphi_n\neq0$.

**2)** Soient $\varphi,\psi\in E^*$ non nulles telles que $\ker\varphi=\ker\psi=H$. Prenons $a\notin H$ (possible car $H\neq E$) ; alors $\psi(a)\neq0$.
 Posons $\lambda=\dfrac{\varphi(a)}{\psi(a)}\in\mathbb R^*$. Prenons $(e_1,\dots,e_{n-1})$ une base de $H$ et $e_n=a$ : c'est une base de $E$
 (Proposition 6). Tout $x=\sum_{i=1}^n x_ie_i$ vérifie $\varphi(x)=x_n\varphi(a)$ et $\psi(x)=x_n\psi(a)$ (car $\varphi$ et $\psi$
 s'annulent sur $H$). Donc :

$$
\begin{aligned}
\varphi(x)&=x_n\varphi(a)\\
&=\lambda\,x_n\psi(a)\\
&=\lambda\psi(x).
\end{aligned}
$$

Ainsi $\varphi=\lambda\psi$ avec $\lambda\neq0$. $\square$

### Question 19

**Premier point.** Soit $\varphi$ une forme linéaire sur $\mathbb R^n$. Démontrer qu'il existe un unique $(a_1,\dots,a_n)\in\mathbb R^n$ tel que $\forall(x_1,\dots,x_n)\in\mathbb R^n,\ \varphi(x_1,\dots,x_n)=\sum_{i=1}^n a_ix_i$.

Soit $(e_1,\dots,e_n)$ la base canonique de $\mathbb R^n$. *Existence* : posons $a_i=\varphi(e_i)$ ; alors, par linéarité, $\varphi(x_1,\dots,x_n)=\varphi\big(\sum_i x_ie_i\big)=\sum_i x_i\varphi(e_i)=\sum_i a_ix_i$. *Unicité* : si $\sum_i a_ix_i=\sum_i a_i'x_i$
 pour tout $x$, en prenant $x=e_j$ on obtient $a_j=a_j'$ pour tout $j$.

$$
\boxed{\text{Le vecteur }(a_1,\dots,a_n)\text{ existe et est unique.}}
$$

**Second point.** Soit $F$ un sous-espace vectoriel de $E$ de dimension $k\in\llbracket1,n-1\rrbracket$, $\mathcal B=(e_1,\dots,e_n)$ une base de $E$.
 Par le Théorème 5, $F=\bigcap_{i=1}^{n-k}H_i$ où les $H_i$ sont des hyperplans vectoriels. Par le Théorème 4, chaque $H_i=\ker\varphi_i$ pour une forme linéaire non nulle $\varphi_i$. D'après le premier point, il existe $(a_{i,1},\dots,a_{i,n})$
 tel que $\varphi_i(x)=\sum_j a_{i,j}x_j$. Posons $A=(a_{i,j})\in\mathcal M_{n-k,n}$. Alors :

$$
\begin{aligned}
x\in F&\iff \forall i\in\llbracket1,n-k\rrbracket,\ x\in H_i\\
&\iff \forall i,\ a_{i,1}x_1+\dots+a_{i,n}x_n=0,
\end{aligned}
$$

ce qui est exactement le système annoncé (les $n-k$ équations définissent $F$ comme intersection d'hyperplans). $\square$

### Question 20

Soit $P$ le plan vectoriel de la Question 8 ($P:\ z-2y=0$). Déterminer une équation cartésienne du plan affine $\mathcal P$ parallèle à $P$ et passant par $(1,2,-1)$.

Un plan affine parallèle à $P$ a une équation de la forme $z-2y=d$ (même partie linéaire). Le point $(1,2,-1)$ donne $d=(-1)-2\times2=-5$. Donc :

$$
\boxed{\mathcal P:\ z-2y+5=0.}\quad\square
$$

## Partie 3 — Questions sur le document 2

On rappelle que $I=(1,0,1)$, $J=(1,1,0)$, $K=(0,1,1)$, $F=(1,1,1)$, et que $I,J,K$
 sont les milieux respectifs des arêtes $[EF]$, $[FB]$, $[FG]$ du cube $ABCDEFGH$. On confond un point avec ses coordonnées.

### Question A

Déterminer les coordonnées des sommets du cube $ABCDEFGH$ et vérifier qu'elles sont toutes égales à $1$ ou $-1$.

$I$ milieu de $[EF]$ donne $E=2I-F=(1,-1,1)$. $K$ milieu de $[FG]$
 donne $G=2K-F=(-1,1,1)$. $J$ milieu de $[FB]$ donne $B=2J-F=(1,1,-1)$.

Les trois arêtes issues de $F$ ont pour vecteurs $\overrightarrow{FE}$, $\overrightarrow{FG}$, $\overrightarrow{FB}$, et le sommet opposé à $F$ est $F+\overrightarrow{FE}+\overrightarrow{FG}+\overrightarrow{FB}=E+G+B-2F$. Le centre du cube est donc

$$
O=\frac{F+(E+G+B-2F)}{2}=\frac{E+G+B-F}{2}.
$$

Or $E+G+B=(1,-1,1)+(-1,1,1)+(1,1,-1)=(1,1,1)=F$, donc $O=(0,0,0)$ : **le centre du cube est l'origine du repère**.

Par symétrie centrale de centre $O$, les sommets opposés sont : $A=-G=(1,-1,-1)$, $C=-E=(-1,1,-1)$, $D=-F=(-1,-1,-1)$, $H=-B=(-1,-1,1)$. Récapitulatif :

$$
A(1,-1,-1),\ B(1,1,-1),\ C(-1,1,-1),\ D(-1,-1,-1),
$$

$$
E(1,-1,1),\ F(1,1,1),\ G(-1,1,1),\ H(-1,-1,1).
$$

Toutes les coordonnées valent bien $\pm1$. $\square$

### Question B

Déterminer une équation cartésienne des plans $(ABC)$ et $(IJK)$, et le faisceau de plans engendré par $(ABC)$ et $(IJK)$.

$A,B,C$ ont pour cote $z=-1$, donc :

$$
\boxed{(ABC):\ z=-1.}
$$

soit $(E_1):\ z+1=0$.
Pour $(IJK)$ : $\overrightarrow{IJ}=(0,1,-1)$, $\overrightarrow{IK}=(-1,1,0)$, et

$$
\overrightarrow{IJ}\wedge\overrightarrow{IK}=(1,1,1).
$$

Le plan passant par $I=(1,0,1)$ de normale $(1,1,1)$ a pour équation $(x-1)+y+(z-1)=0$, soit :

$$
\boxed{(IJK):\ x+y+z=2.}
$$

soit $(E_2):\ x+y+z-2=0$.
Les normales $(0,0,1)$ et $(1,1,1)$ ne sont pas colinéaires : les plans sont sécants. Le faisceau engendré par $(ABC)$ et $(IJK)$ est l'ensemble des plans d'équation $\alpha(E_1)+\beta(E_2)=0$ avec $(\alpha,\beta)\neq(0,0)$ :

$$
\boxed{\mathcal F:\ \beta x+\beta y+(\alpha+\beta)z+(\alpha-2\beta)=0,\quad(\alpha,\beta)\neq(0,0).}
$$

Le vecteur normal $(\beta,\beta,\alpha+\beta)$ est non nul dès que $(\alpha,\beta)\neq(0,0)$ (sinon $\beta=0$ puis $\alpha=0$) : chaque combinaison est bien une équation de plan. D'après le Théorème 3, comme les plans sont sécants, ce faisceau est l'ensemble de tous les plans contenant la droite $(ABC)\cap(IJK)$. $\square$

### Question C

Déterminer les coordonnées des points $M=(AB)\cap(IJ)$ et $N=(BC)\cap(JK)$.

La droite $(IJ)$ se paramètre en $I+t\,\overrightarrow{IJ}=(1,t,1-t)$, $t\in\mathbb R$. La droite $(AB)$ est $\{(1,s,-1):s\in\mathbb R\}$
 ($x=1$, $z=-1$). L'intersection impose $1-t=-1$, soit $t=2$ :

$$
\boxed{M=(1,2,-1).}
$$

(On vérifie que $J$ est le milieu de $[IM]$ : $\tfrac12(I+M)=(1,1,0)=J$.)

La droite $(JK)$ se paramètre en $J+t\,\overrightarrow{JK}=(1-t,1,t)$ et $(BC)=\{(s,1,-1):s\in\mathbb R\}$ ($y=1$, $z=-1$). L'intersection impose $t=-1$ :

$$
\boxed{N=(2,1,-1).}
$$

(On vérifie que $J$ est le milieu de $[NK]$ : $\tfrac12(N+K)=(1,1,0)=J$.) $\square$

### Question D

Soient $O=(0,0,0)$ et $P=(0,1,-1)$. Démontrer que le plan $(IJP)$ contient $O$.

On a $\overrightarrow{IO}=O-I=(-1,0,-1)$, $\overrightarrow{IJ}=(0,1,-1)$, $\overrightarrow{IP}=P-I=(-1,1,-2)$, et :

$$
\overrightarrow{IP}-\overrightarrow{IJ}=(-1,0,-1)=\overrightarrow{IO}.
$$

Le vecteur $\overrightarrow{IO}$ est combinaison linéaire de $\overrightarrow{IJ}$ et $\overrightarrow{IP}$, qui engendrent le plan $(IJP)$ passant par $I$.
 Donc $O\in(IJP)$. $\square$

### Question E

Déterminer l'intersection du plan $(IJP)$ et de la droite $(EH)$.

D'après la Question D, $O\in(IJP)$ : ce plan est vectoriel, engendré par $\overrightarrow{OI}=(1,0,1)$ et $\overrightarrow{OJ}=(1,1,0)$. Une normale est

$$
\overrightarrow{OI}\wedge\overrightarrow{OJ}=(-1,1,1),
$$

d'où $(IJP):\ -x+y+z=0$, soit $x-y-z=0$.

La droite $(EH)$, avec $E=(1,-1,1)$ et $H=(-1,-1,1)$, est $\{(x,-1,1):x\in\mathbb R\}$, de vecteur directeur $(1,0,0)$.
 Ce vecteur n'est pas orthogonal à la normale $(-1,1,1)$ : $(1,0,0)\cdot(-1,1,1)=-1\neq0$, donc la droite n'est pas parallèle au plan et l'intersection est un unique point. On résout $x-(-1)-1=0$, soit $x=0$ :

$$
\boxed{(IJP)\cap(EH)=\{(0,-1,1)\}.}\quad\square
$$

### Question F

Le plan $(IJP)$ contient $O$, donc c'est un plan vectoriel. Déterminer une forme linéaire $\phi:\mathbb R^3\to\mathbb R$ telle que $\ker\phi=(IJP)$. Cette forme est-elle unique ?

D'après la Question E, $(IJP)=\{(x,y,z):x-y-z=0\}$. Posons

$$
\boxed{\phi:(x,y,z)\mapsto x-y-z.}
$$

Alors $\ker\phi=(IJP)$. La forme n'est **pas unique** : pour tout $\mu\in\mathbb R^*$, $\ker(\mu\phi)=\ker\phi$. Réciproquement, d'après le Théorème 4(2), toute forme linéaire non nulle de noyau $(IJP)$ est de la forme $\mu\phi$
 avec $\mu\neq0$ : $\phi$ est unique **à un facteur multiplicatif non nul près**. $\square$

### Question G

L'hypothèse « $F=(1,1,1)$ » est-elle nécessaire, ou peut-elle être déduite de « $I=(1,0,1)$, $J=(1,1,0)$, $K=(0,1,1)$ » (avec $I,J,K$ milieux des arêtes issues de $F$) ?

Elle est **nécessaire** : $F$ n'est pas déterminé par $I,J,K$ seuls. En effet, si $a$ désigne la longueur d'une arête, le triangle $FIJ$ est rectangle isocèle en $F$, avec $FI=FJ=a/2$. Or les coordonnées données, indépendantes de $F$, donnent $IJ=\sqrt2$. Ainsi $IJ^2=2(a/2)^2$, donc $a=2$ et $FI=FJ=FK=1$. Le triangle $IJK$ est équilatéral de côté $\sqrt2$ (par exemple $|IJ|=\sqrt{0^2+1^2+(-1)^2}=\sqrt2$). Le point $F$
 est donc à l'intersection des trois sphères de rayon $1$ centrées en $I,J,K$ : il se trouve sur la droite passant par le centre de gravité $\Omega=\big(\tfrac23,\tfrac23,\tfrac23\big)$ du triangle $IJK$, orthogonale au plan $(IJK)$
 (de normale $(1,1,1)$) : $F=\Omega+t(1,1,1)$. La condition $FI^2=1$ s'écrit :

$$
\begin{aligned}
FI^2=1&\iff 3t^2+\tfrac23=1\\
&\iff t^2=\tfrac19\\
&\iff t=\pm\tfrac13.
\end{aligned}
$$

Pour $t=\tfrac13$ : $F=(1,1,1)$ ; pour $t=-\tfrac13$ : $F=\big(\tfrac13,\tfrac13,\tfrac13\big)$. Deux positions de $F$
 sont compatibles avec $I,J,K$. En effet, ces deux points sont symétriques par rapport au plan $(IJK)$ : la réflexion du premier cube dans ce plan fixe ses trois milieux $I,J,K$ et donne un second cube. L'hypothèse sur $F$ ne peut donc pas en être déduite, elle est nécessaire. $\square$
