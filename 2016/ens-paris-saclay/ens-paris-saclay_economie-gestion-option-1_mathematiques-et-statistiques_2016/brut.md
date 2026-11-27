# ENS Cachan–ENSAI · Économie et gestion D2 · Mathématiques et statistiques 2016 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

**Révision (tour 1)** · GPT-6.2 Astra Ultra · vitesse non renseignée

Le sujet C1692 comporte trois problèmes indépendants. La notation des probabilités avec une barre oblique dans le fascicule est transcrite par une barre conditionnelle. Le graphique demandé en III.4 superpose les deux familles de paramètres admissibles.

## Problème 1 · Composition de deux applications linéaires

### Question I.1

Les trois colonnes de $H$ sont les images des trois vecteurs de la base canonique par $u$. Elles donnent $H=\begin{pmatrix}2&0&-1\\3&1&2\end{pmatrix}$.

### Question I.2

Les images par $v$ de $(1,0)$ et $(0,1)$ sont respectivement $(1,0,2)$ et $(1,-1,-1)$. Donc $K=\begin{pmatrix}1&1\\0&-1\\2&-1\end{pmatrix}$.

### Question I.3

De $2z_1-z_3=0$ puis $3z_1+z_2+2z_3=0$ on tire $z_3=2z_1$ et $z_2=-7z_1$. Ainsi $\ker u=\mathbb R(1,-7,2)$ est une droite et $u$ n’est pas injective.

### Question I.4

Le théorème du rang donne $\dim\operatorname{Im}u=3-1=2$. Comme l’espace d’arrivée est $\mathbb R^2$, l’image est tout cet espace. L’application est surjective.

### Question I.5

Le produit représentant $u\circ v$ est $HK=\begin{pmatrix}2-2&2+1\\3+4&3-1-2\end{pmatrix}=\begin{pmatrix}0&3\\7&0\end{pmatrix}$.

### Question I.6

On calcule $(HK)^2=\begin{pmatrix}21&0\\0&21\end{pmatrix}=21I_2$. Le scalaire demandé est $\lambda=21$.

### Question I.7

Puisque $21\ne0$, $HK$ multiplié par $(HK)/21$ donne $I_2$ dans les deux ordres. Ainsi $HK$ est inversible avec cet inverse.

### Question I.8

La matrice de $(u\circ v)^2$ est $(HK)^2$. C’est donc l’homothétie de rapport $21$ sur $\mathbb R^2$, qui envoie $(x,y)$ sur $(21x,21y)$.

## Problème 2 · Extrema sur le cercle unité

### Question II.1

Avec $g(x,y)=x^2+y^2-1$, prenons $L(x,y,\mu)=x^3+y^3-\mu(x^2+y^2-1)$. Le programme cherche les extrema de $f=x^3+y^3$ sous $g=0$.

### Question II.2

La qualification demande $\nabla g=(2x,2y)\ne(0,0)$ en tout point admissible. C’est le cas car $x^2+y^2=1$.

### Question II.3

Le gradient dans l’ordre $(x,y,\mu)$ est $(x(3x-2\mu),y(3y-2\mu),1-x^2-y^2)$. On impose sa nullité pour obtenir les points critiques contraints.

### Question II.4

Pour $\mu=3/2$, chaque coordonnée vaut zéro ou un. La contrainte impose exactement une coordonnée égale à un. D’où $(1,0)$ et $(0,1)$.

### Question II.5

Pour $\mu=-3/2$, chaque coordonnée vaut zéro ou moins un. On obtient $(-1,0)$ et $(0,-1)$.

### Question II.6

Avec $xy\ne0$, les équations donnent $x=y=2\mu/3$. En posant $a=1/\sqrt2$, la contrainte impose $(a,a)$ et $(-a,-a)$, de multiplicateurs respectifs $3a/2$ et $-3a/2$. Les points des deux axes ont déjà tous été traités.

### Question II.7

Dans l’ordre $(\mu,x,y)$, la Hessienne de $L$ est
$$H_b=\begin{pmatrix}0&-2x&-2y\\-2x&6x-2\mu&0\\-2y&0&6y-2\mu\end{pmatrix}.$$
La convention consistant à border par $+\nabla g$ change le signe de la première ligne et de la première colonne, sans changer le déterminant.

### Question II.8

En un point critique, le vecteur tangent unitaire $v=(-y,x)$ donne la dérivée seconde le long du cercle, $D=(6x-2\mu)y^2+(6y-2\mu)x^2$. En effet, en dérivant deux fois $f$ le long d’une paramétrisation du cercle, la relation $\nabla f=\mu\nabla g$ élimine la dérivée seconde de la paramétrisation et donne cette Hessienne restreinte. Aux points $(-1,0)$ et $(0,-1)$, $D=3>0$. Au point $(a,a)$, $D=3a>0$. Ce sont trois minima locaux stricts. Les deux premiers ont valeur $-1$ et le dernier valeur $a$.

### Question II.9

Aux points $(1,0)$ et $(0,1)$, $D=-3<0$. Au point $(-a,-a)$, $D=-3a<0$. Ce sont trois maxima locaux stricts, de valeurs $1,1,-a$. La qualification et la liste complète de II.4–6 excluent tout autre extremum local.

## Problème 3 · Variables indicatrices et estimateurs

### Question III.1

La loi donne $\mathbb E X=a-b$. Le paramètre restant $1-a-b$ est la probabilité de la valeur zéro.

### Question III.2a

La variable $Y=X^2$ vaut un avec probabilité $a+b$ et zéro avec probabilité $1-a-b$. C’est une loi de Bernoulli de paramètre $a+b$.

### Question III.2b

On obtient $\mathbb E Y=1(a+b)+0(1-a-b)=a+b$.

### Question III.2c

Par $Y=X^2$, $\operatorname{Var}(X)=\mathbb E Y-(\mathbb E X)^2=a+b-(a-b)^2$.

### Question III.2d

On obtient $\operatorname{Var}(Y)=a+b-(a+b)^2=(a+b)(1-a-b)$.

### Question III.2e

On a $P=(X^2+X)/2=\mathbf1_{\{X=1\}}$, de loi de Bernoulli de paramètre $a$.

### Question III.2f

De $M=(X^2-X)/2=\mathbf1_{\{X=-1\}}$ il résulte que $M$ a la loi de Bernoulli de paramètre $b$.

### Question III.3a

L’événement $X=1$ est inclus dans $Y=1$, qui a probabilité $a+b>0$. Donc $\mathbb P(X=1\mid Y=1)=a/(a+b)$.

### Question III.3b

Puisque $X=1$ impose $Y=1$ et que $a>0$, $\mathbb P(Y=1\mid X=1)=1$.

### Question III.3c

Elles sont égales exactement lorsqu’elles sont toutes deux nulles, soit lorsque $X=0$. On obtient $\mathbb P(P=M)=1-a-b$.

### Question III.3d

Les variables $P$ et $M$ sont les indicatrices des événements $X=1$ et $X=-1$, qui sont incompatibles. Ainsi $PM=0$ à chaque issue et la probabilité demandée vaut un.

### Question III.4a

Comme $P=0$ signifie $X\ne1$, $\mathbb P(X=0\mid P=0)=(1-a-b)/(1-a)$. La première équation devient $a(1-a)=(a+b)(1-a-b)$, soit $b(1-2a-b)=0$. Avec $b>0$, la solution est $b=1-2a$, $0<a<1/2$. Cette portion de droite est représentée avec l’autre famille en III.4b.

### Question III.4b

L’équation est $b/(a+b)=(1-a-b)/(1-b)$, équivalente à $a(1-a-2b)=0$. Comme $a>0$, ses solutions sont $a=1-2b$, $0<b<1/2$. Les extrémités des deux segments sont exclues par les hypothèses.

![Figure 1 — Les deux segments ouverts se croisent en (1/3, 1/3) à l’intérieur du triangle admissible.](figures/droites-probabilites.svg)

### Question III.4c

Le système $2a+b=1$, $a+2b=1$ donne en soustrayant $a=b$, puis $a=b=1/3$. Ce point vérifie $a+b=2/3<1$. C’est l’unique solution commune.

### Question III.5a

Par III.2e, $S_P=\sum_{i=1}^n\mathbf1_{\{X_i=1\}}$. Chaque tirage égal à un ajoute exactement une unité, les autres n’en ajoutent aucune.

### Question III.5b

Les $P_i$ sont les images respectives des $X_i$ indépendantes par une même fonction. Elles sont indépendantes et de loi de Bernoulli de paramètre $a$. Donc $S_P\sim\mathcal B(n,a)$.

### Question III.5c

De $\mathbb E S_P=na$ et $\operatorname{Var}(S_P)=na(1-a)$, on tire $\mathbb E\widehat a_1=a$ et $\operatorname{Var}(\widehat a_1)=a(1-a)/n$.

### Question III.6a

Si $a=b$, la condition $a+b<1$ devient $2a<1$. Ainsi $0<a<1/2$.

### Question III.6b.i

Le compteur $S_M$ enregistre les occurrences de $X_i=-1$, chacune de probabilité $b=a$. Leur fréquence empirique $\widehat a_0=S_M/n$ estime donc le même paramètre et converge vers lui par la loi des grands nombres.

### Question III.6b.ii

Comme $S_M\sim\mathcal B(n,a)$, $\mathbb E\widehat a_0=a$ et $\operatorname{Var}(\widehat a_0)=a(1-a)/n$.

### Question III.6c.i

Par linéarité, $\mathbb E\widehat a_t=a$. Pour un même indice, $P_iM_i=0$, donc $\operatorname{Cov}(P_i,M_i)=-a^2$. Pour des indices différents la covariance est nulle par indépendance. Ainsi $\operatorname{Cov}(\widehat a_1,\widehat a_0)=-a^2/n$ et
$$\operatorname{Var}(\widehat a_t)=\frac{a(1-a)(t^2+(1-t)^2)-2a^2t(1-t)}{n}=\frac{a(1-a)-2at(1-t)}{n}.$$

### Question III.6c.ii

Puisque $a>0$, la variance est minimale au maximum de $t(1-t)=1/4-(t-1/2)^2$. L’unique optimum est $t^*=1/2$.

### Question III.6d

La variance de $\widehat a_{1/2}$ vaut $a(1-2a)/(2n)$, inférieure de $a/(2n)>0$ à celle des deux fréquences seules. Tous sont sans biais, donc $\widehat a_{1/2}$ a la plus petite erreur quadratique moyenne des trois.

### Question III.6e

On a $P_i+M_i=Y_i$. Par suite $\widehat a_{t^*}=(S_P+S_M)/(2n)=(2n)^{-1}\sum_{i=1}^nY_i$. La variable $\sum_iY_i$ compte les observations non nulles. Elle suit $\mathcal B(n,2a)$ lorsque $a=b$. Cette loi donne directement $\operatorname{Var}(\widehat a_{t^*})=n(2a)(1-2a)/(4n^2)=a(1-2a)/(2n)$, conformément au calcul par covariance.
