# CAPES Maths — Épreuve disciplinaire appliquée (bac+5) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie 1 — Angles

**I. Angle au collège — A. Somme des angles d'un triangle par pliage**

### Question 1

L'activité de pliage s'inscrit dans le triptyque **« Manipuler – Verbaliser – Abstraire »** : en ramenant les trois sommets sur le point $H$, l'élève **constate concrètement** que les trois angles $\widehat A,\widehat B,\widehat C$ se juxtaposent le long de la droite $(BC)$ pour former un **angle plat**. L'activité permet ainsi de **conjecturer** le résultat (« la somme vaut un angle plat ») à partir d'une expérience, avant d'en construire une démonstration : elle donne du sens à la propriété et motive sa preuve.

### Question 2.a

Soit $H$ le pied de la hauteur issue de $A$ ; $(AH)\perp(BC)$.

*Les points $I$ et $J$ sont des milieux.* $(d')$ est la médiatrice de $[CH]$ : comme $C$ et $H$ appartiennent à
$(BC)$, le segment $[CH]$ est porté par $(BC)$, donc $(d')\perp(BC)$, c'est-à-dire $(d')\parallel(AH)$. Dans le triangle $AHC$, la droite
$(d')$ passe par le milieu $M$ de $[CH]$ et est parallèle au côté $(AH)$ ; d'après le **théorème de la droite des milieux** (réciproque), elle coupe $(AC)$ en son milieu : $I$ est le **milieu de
$[AC]$**. De même, $J$ est le **milieu de $[AB]$**.

*La droite $(IJ)$ est parallèle à $(BC)$.* $I$ et $J$ étant les milieux de $[AC]$ et $[AB]$,
$(IJ)$ est la droite des milieux du triangle $ABC$, donc $(IJ)\parallel(BC)$, et $(IJ)$ est à mi-hauteur entre $A$ et $(BC)$.

*Transport des angles.*
- La réflexion $s$ d'axe $(IJ)$ : $(IJ)$ est perpendiculaire à $(AH)$ et passe par le milieu de $[AH]$ (mi-hauteur), c'est donc la **médiatrice de $[AH]$** ; ainsi
$s(A)=H$, et $s$ fixe $I,J$. Donc $s$ envoie le triangle $AIJ$ sur $HIJ$ :
$\widehat A=\widehat{IAJ}=\widehat{IHJ}$.
- La réflexion $s'$ d'axe $(d')$ (médiatrice de $[CH]$) : $s'(C)=H$ et fixe $I$ (car $I\in(d')$). Comme
$I\in[AC]$ et $H\in[BC]$, $\widehat C=\widehat{ACB}=\widehat{(CI),(CH)}$, et $s'$ l'envoie sur $\widehat{(HI),(HC)}=\widehat{IHC}$.
- De même, $s''$ d'axe $(d'')$ donne $\widehat B=\widehat{JHB}$.

*Conclusion.* Les points $B,H,C$ sont alignés, donc les rayons $[HB)$ et $[HC)$ sont opposés et

$$
\widehat{JHB}+\widehat{IHJ}+\widehat{IHC}=\text{angle plat}=180^\circ,
$$

soit $\widehat B+\widehat A+\widehat C=180^\circ.$ $\qquad\square$

### Question 2.b

Traçons par $A$ la droite $(\Delta)$ parallèle à $(BC)$. Les droites $(AB)$ et $(AC)$ sont sécantes à ce couple de parallèles. D'après la propriété des **angles alternes-internes** : l'angle que fait $(\Delta)$ avec
$(AB)$ d'un côté de $A$ est égal à $\widehat B$, et l'angle que fait $(\Delta)$ avec $(AC)$ de l'autre côté est égal à $\widehat C$. Ces deux angles et l'angle
$\widehat A=\widehat{BAC}$ forment, en $A$, un **angle plat** le long de $(\Delta)$. Donc $\widehat A+\widehat B+\widehat C=180^\circ.$ $\qquad\square$

### Question 3

*« Un triangle $ABC$ a deux angles qui mesurent $\widehat A=40^\circ$ et $\widehat B=75^\circ$. On souhaite le construire en traçant d'abord le côté $[AB]$ de longueur $8$ cm. Quelle est la mesure de l'angle $\widehat C$ ? Construire alors le triangle. »*

L'élève doit déterminer $\widehat C=180^\circ-40^\circ-75^\circ=65^\circ$ pour pouvoir construire, ce qui mobilise la propriété sans qu'elle soit mentionnée.

**I. Angle au collège — B. Figure codée**

### Question 4

- **Raisonner** : à partir du codage de la figure (côtés égaux, angle droit, angle de $45^\circ$), l'élève doit **enchaîner des déductions** (losange, puis carré, puis médiatrice…) en mobilisant propriétés et théorèmes pour conclure sur la nature du triangle $KUS$ : c'est bien « utiliser un raisonnement logique et des règles établies pour parvenir à une conclusion ».
- **Communiquer** : l'élève doit **expliquer et justifier par écrit** sa démarche (rédaction d'une chaîne d'arguments, emploi correct du vocabulaire et des notations), c'est-à-dire « expliquer […] son raisonnement […] et argumenter ».

### Question 5

*Réussites.* La chaîne déductive est globalement correcte et pertinente : (i) « 4 côtés égaux $\Rightarrow$ losange » ; (ii) « losange avec un angle droit $\Rightarrow$ carré » ; (iii) à partir de $KR=RS$ et de l'alignement, « $R$ milieu de $[KS]$ » ; (iv) $(UR)\perp(KR)$ donc
$(UR)$ est la **médiatrice** de $[KS]$ ; (v) exploitation de la **symétrie** pour transférer l'angle de $45^\circ$ et obtenir $KU=US$ ; (vi) conclusion correcte : $KUS$ isocèle rectangle en $U$. L'élève maîtrise donc la notion de médiatrice et la conservation des angles.

*Fragilités.* La rigueur est insuffisante : l'élève invoque « par symétrie » **sans nommer la symétrie axiale** d'axe $(UR)$ ni justifier qu'elle **échange $K$ et $S$** (ce qui vaut précisément parce que $(UR)$ est la médiatrice de $[KS]$) ; l'**alignement de $K,R,S$** est utilisé implicitement ; les notations d'angles restent approximatives. Ce sont des défauts de justification, non des erreurs de raisonnement.

### Question 6

Trois propriétés requises (en distinguant leurs statuts) :
1. **(Définition/propriété)** Un quadrilatère dont les quatre côtés ont la même longueur est un **losange**.
2. **(Propriété)** Un losange ayant un angle droit est un **carré**.
3. **(Propriété caractéristique de la médiatrice)** Tout point équidistant des extrémités d'un segment appartient à sa médiatrice, et **une symétrie axiale conserve les longueurs et les mesures d'angles** (donc échange les extrémités d'un segment lorsqu'elle a pour axe sa médiatrice).

**I. Angle au collège — C. Circonférence terrestre (Ératosthène)**

### Question 7

Pour déterminer l'angle $\widehat a$ à partir de l'obélisque (hauteur $50$ m) et de son ombre ($6{,}33$ m), on admet implicitement que **l'obélisque est vertical, perpendiculaire au sol horizontal** : le triangle « sommet de l'obélisque – pied – extrémité de l'ombre » est **rectangle**, ce qui autorise $\tan(\widehat a)=\dfrac{\text{ombre}}{\text{hauteur}}=\dfrac{6{,}33}{50}$.

### Question 8

Un prérequis par question :
- **a)** Trigonométrie dans le triangle rectangle (**tangente** d'un angle aigu, lien avec $\arctan$ / calculatrice).
- **b)** Propriété des **angles alternes-internes** : les rayons solaires étant parallèles, l'angle $\widehat b$ (au centre $O$) est alterne-interne de $\widehat a$, donc $\widehat b=\widehat a$.
- **c)** **Proportionnalité** entre la longueur d'un arc et l'angle au centre (règle de trois), et conversion d'unités (stades $\to$ mètres).

### Question 9

- *Flash 1 (tangente).* « $ABC$ rectangle en $B$, $AB=4$, $BC=3$. Donner $\tan(\widehat A)$. »
- *Flash 2 (alternes-internes).* « Deux droites parallèles sont coupées par une sécante ; un angle mesure $40^\circ$. Donner la mesure de son angle alterne-interne. »
- *Flash 3 (proportionnalité).* « Sur un cercle, un arc correspondant à un angle au centre de $30^\circ$ mesure $5$ cm. Quelle est la longueur totale du cercle ? »

**II. Angle au lycée — A. Fonctions trigonométriques**

### Question 10

Soit $\alpha\in\,]0,\tfrac\pi2[$. Dans le cercle trigonométrique $(O,I,J)$, le point $M$ associé au réel $\alpha$ (longueur d'arc $\widehat{IM}=\alpha$) a pour coordonnées $(\cos\alpha,\sin\alpha)$ : c'est la **définition du lycée**. Soit
$H$ le projeté orthogonal de $M$ sur $(OI)$. Comme $\alpha\in\,]0,\tfrac\pi2[$, on a $\cos\alpha>0$ et $\sin\alpha>0$, donc dans le triangle
$OHM$ rectangle en $H$ : $OH=\cos\alpha$, $HM=\sin\alpha$, et l'hypoténuse $OM=1$ (rayon). L'angle géométrique $\widehat{HOM}$ a pour mesure en radian la longueur d'arc
$\alpha$. La **définition du collège** appliquée à cet angle aigu donne

$$

\begin{aligned}
\cos(\widehat{HOM})&=\frac{\text{adjacent}}{\text{hypoténuse}}=\frac{OH}{OM}\\
&=\frac{\cos\alpha}{1}=\cos\alpha.
\end{aligned}

$$

Le cosinus (collège) de l'angle $\widehat{HOM}$ coïncide donc avec le cosinus (lycée) du réel $\alpha$ : les deux définitions sont cohérentes. $\qquad\square$

### Question 11

Pour tout réel $x$ tel que $\cos x\neq 0$, on pose

$$
\tan x=\frac{\sin x}{\cos x}.
$$

Le domaine de définition est $\{x\in\mathbb R:\cos x\neq 0\}=\mathbb R\setminus\Big\{\tfrac\pi2+k\pi,\ k\in\mathbb Z\Big\}.$

**II. Angle au lycée — B. Calcul d'une valeur remarquable**

### Question 12

Soit $ABC$ un triangle équilatéral de côté $a$. Chacun de ses angles vaut $\tfrac\pi3$. Soit $H$ le pied de la hauteur issue de $A$ : dans un triangle équilatéral, cette hauteur est aussi médiane, donc $H$ est le milieu de
$[BC]$ et $BH=\tfrac a2$. Le triangle $AHB$ est rectangle en $H$, et $\widehat{HAB}=\tfrac\pi2-\widehat{ABH}=\tfrac\pi2-\tfrac\pi3=\tfrac\pi6$. Par définition du sinus dans le triangle rectangle,

$$

\begin{aligned}
\sin\!\Big(\tfrac{\pi}{6}\Big)=\sin(\widehat{HAB})&=\frac{\text{opposé}}{\text{hypoténuse}}=\frac{BH}{AB}\\
&=\frac{a/2}{a}=\frac12.
\end{aligned}

$$

$$
\boxed{\sin\!\big(\tfrac{\pi}{6}\big)=\tfrac12}
$$

Donc $\sin\!\big(\tfrac\pi6\big)=\dfrac12.$ $\qquad\square$

### Question 13

Soit $\theta\in\mathbb R$ et $M$ le point du cercle trigonométrique associé à $\theta$, de coordonnées $(\cos\theta,\sin\theta)$. Le point $M$ appartient au cercle de centre $O$ et de **rayon
$1$**, donc $OM=1$. Or, par la formule de la distance,

$$
OM^2=(\cos\theta-0)^2+(\sin\theta-0)^2=\cos^2\theta+\sin^2\theta.
$$

Comme $OM=1$, on obtient $\cos^2\theta+\sin^2\theta=1^2=1$, et ceci **pour tout réel $\theta$** (la position de $M$ sur le cercle, quel que soit le quadrant, ne change pas $OM=1$). $\qquad\square$

**II. Angle au lycée — C. Formule d'Al-Kashi**

### Question 14.a

Avec $AB=6$, le cercle de centre $B$ et de rayon $4$, et $\widehat{BAC}=25^\circ$ (angle **non compris** entre les deux longueurs connues $AB$ et $BC=4$), la demi-droite issue de
$A$ faisant un angle de $25^\circ$ **coupe le cercle en deux points $C$ et $D$**. On obtient donc **deux triangles distincts** $ABC$ et $ABD$ ayant pourtant
$AB=6$, $BC=BD=4$ et $\widehat A=25^\circ$. La figure montre ainsi que, lorsqu'on connaît deux longueurs et un angle **non compris** entre elles, le triangle **n'est pas déterminé de façon unique** : cela répond à la dernière question (« non, pas toujours le même »).

### Question 14.b

Les échanges établissent qu'avec **deux longueurs et l'angle compris entre elles** (cas SAS), le triangle est **déterminé de façon unique** : il existe donc une relation calculant la troisième longueur à partir des deux autres et de cet angle. La **formule d'Al-Kashi** $b^2=a^2+c^2-2ac\cos(\widehat B)$ fournit exactement ce calcul. Son introduction est ainsi légitimée : elle répond au besoin, apparu dans la discussion, de **déterminer effectivement** la troisième longueur dans le cas où l'angle est compris entre les deux côtés connus.

### Question 15

Avec les notations de l'annexe ($a=BC$, $b=AC$, $c=AB$, $\widehat B=\widehat{ABC}$), la formule s'écrit $b^2=a^2+c^2-2ac\cos(\widehat B)$. Si $\widehat B=90^\circ$, alors
$\cos(\widehat B)=0$, d'où

$$
b^2=a^2+c^2, \text{soit}  AC^2=BC^2+AB^2,
$$

qui est le **théorème de Pythagore** dans le triangle rectangle en $B$. La formule d'Al-Kashi **généralise** donc Pythagore, le terme $-2ac\cos(\widehat B)$ mesurant l'écart au cas rectangle. $\qquad\square$

### Question 16.a

Deux prérequis : le **théorème de Pythagore** (dans les triangles rectangles $AHB$ et $AHC$) et la **trigonométrie dans le triangle rectangle** (le cosinus comme rapport adjacent/hypoténuse, pour obtenir $x=c\cos\widehat B$).

### Question 16.b

Soit $H$ le pied de la hauteur issue de $A$ sur $(BC)$. $\widehat B$ étant obtus, $H$ est sur le prolongement de $[CB]$ au-delà de
$B$. Posons $AH=h$ et $BH=x>0$.
- Dans $AHB$ rectangle en $H$ : $c^2=AB^2=h^2+x^2$.
- $H$ étant au-delà de $B$, $HC=HB+BC=x+a$ ; dans $AHC$ rectangle en $H$ :

$$

\begin{aligned}
b^2=AC^2=h^2+(x+a)^2&=\underbrace{(h^2+x^2)}_{=\,c^2}+a^2+2ax\\
&=c^2+a^2+2ax.
\end{aligned}

$$

- L'angle $\widehat{ABH}$ est le supplémentaire de $\widehat{ABC}$ : $\widehat{ABH}=\pi-\widehat B$. Dans $AHB$ rectangle en $H$ : $\cos(\widehat{ABH})=\dfrac{BH}{AB}=\dfrac xc$, d'où
$x=c\cos(\pi-\widehat B)=-c\cos\widehat B$.

En reportant : $2ax=-2ac\cos\widehat B$, donc

$$
b^2=c^2+a^2-2ac\cos(\widehat B).\qquad\square
$$

(Comme $\widehat B$ est obtus, $\cos\widehat B<0$ et $b^2>a^2+c^2$, ce qui est cohérent.)

### Question 17

$$

\begin{aligned}
b^2=AC^2&=\|\vec{BC}-\vec{BA}\|^2\\
&=\|\vec{BC}\|^2+\|\vec{BA}\|^2-2\,\vec{BC}\cdot\vec{BA}.
\end{aligned}

$$

Or $\|\vec{BC}\|=a$, $\|\vec{BA}\|=c$, et $\vec{BC}\cdot\vec{BA}=\|\vec{BC}\|\,\|\vec{BA}\|\cos\big(\widehat{(\vec{BC},\vec{BA})}\big)=ac\cos(\widehat B)$. D'où

$$
b^2=a^2+c^2-2ac\cos(\widehat B).\qquad\square
$$

**II. Angle au lycée — D. Optimisation**

### Question 18

On amène l'élève à un **contrôle d'homogénéité (dimensionnel)** : « $A$ est une **aire** (en $\text{m}^2$), donc $\pi A$ est encore une aire ; or un **volume** s'exprime en $\text{m}^3$. L'égalité $V=\pi A$ est donc impossible pour des raisons d'unités. » On peut compléter par un **contre-exemple numérique** : $V_{\text{cyl}}=\pi r^2 h$, tandis que
$\pi A=\pi(2rh)=2\pi rh$ ; pour $r=h=1$, $\pi r^2h=\pi$ mais $2\pi rh=2\pi$ : les deux ne coïncident pas.

### Question 19

Trois éléments attestant de la compétence **« Chercher »** (annexe 0) :
1. **Expérimenter avec un logiciel pour émettre une conjecture** : « Avec GeoGebra je conjecture que l'aire du rectangle est $2\sin\alpha\cos\alpha$ ».
2. **Tester / vérifier** : « J'ai vérifié avec ma calculatrice le tracé de la courbe […] maximale en $\tfrac\pi4$ ».
3. **Décomposer le problème en sous-problèmes / particulariser** : ramener le volume à l'aire du rectangle et exprimer $h=\sin\alpha$, $r=\cos\alpha$ (introduction d'une variable adaptée).

### Question 20

Coup de pouce : « Place-toi dans le triangle rectangle $OHM$ (avec $OM=R=1$). Exprime $r=OH$ et $h=HM$ en fonction de l'angle $\alpha$ (ou choisis $r$ comme variable et exprime
$h$). Écris ensuite le volume du cylindre **en fonction d'une seule variable**. »

### Question 21

Dans le triangle $OHM$ rectangle en $H$, avec $OM=R=1$ et $\alpha=\widehat{HOM}\in\,]0,\tfrac\pi2[$ :

$$

\begin{aligned}
r=OH&=\cos\alpha,\\
h=HM&=\sin\alpha.
\end{aligned}

$$

Le volume du cylindre est, pour $\alpha\in\,]0,\tfrac\pi2[$,

$$
V(\alpha)=\pi r^2 h=\pi\cos^2\alpha\,\sin\alpha.
$$

$V$ est dérivable sur $]0,\tfrac\pi2[$, et en posant $f(\alpha)=\cos^2\alpha\sin\alpha$ :

$$

\begin{aligned}
f'(\alpha)&=2\cos\alpha(-\sin\alpha)\sin\alpha+\cos^2\alpha\cos\alpha\\
&=\cos\alpha\,(\cos^2\alpha-2\sin^2\alpha)\\
&=\cos\alpha\,(1-3\sin^2\alpha).
\end{aligned}

$$

Sur $]0,\tfrac\pi2[$, $\cos\alpha>0$, donc le signe de $f'$ est celui de $1-3\sin^2\alpha$. Comme $\sin$ est croissante positive sur cet intervalle :

$$
1-3\sin^2\alpha>0\iff \sin\alpha<\tfrac{1}{\sqrt3}.
$$

| $\alpha$ | $0$ | | $\alpha_0$ | | $\tfrac\pi2$ |
|---|---|---|---|---|---|
| $f'(\alpha)$ | | $+$ | $0$ | $-$ | |
| $f$ | | $\nearrow$ | max | $\searrow$ | |

où $\alpha_0$ vérifie $\sin\alpha_0=\tfrac1{\sqrt3}$. Le volume est donc **maximal** en $\alpha_0$. Alors :

$$

\begin{aligned}
h=\sin\alpha_0&=\frac1{\sqrt3}=\frac{\sqrt3}{3},\\
r^2=\cos^2\alpha_0&=1-\tfrac13=\tfrac23,\qquad r=\sqrt{\tfrac23}=\frac{\sqrt6}{3}.
\end{aligned}

$$

$$

\begin{aligned}
V_{\max}=\pi r^2 h&=\pi\cdot\tfrac23\cdot\tfrac1{\sqrt3}\\
&=\frac{2\pi}{3\sqrt3}=\frac{2\sqrt3}{9}\,\pi\approx1{,}21\ \text{m}^3.
\end{aligned}

$$

$$
\boxed{V_{\max}=\frac{2\sqrt3}{9}\,\pi\approx1{,}21\ \text{m}^3}
$$

**Le volume est maximal pour $h=\dfrac{\sqrt3}{3}$ m et $r=\dfrac{\sqrt6}{3}$ m.** $\qquad\square$

### Question 22

La contrainte « $M$ sur la sphère » donne $OH^2+HM^2=OM^2$, soit $r^2+h^2=1$.
- Variable $\alpha$ (trigonométrique) : $\;V(\alpha)=\pi\cos^2\alpha\,\sin\alpha,\quad\alpha\in\,]0,\tfrac\pi2[.$
- Variable $h$ (sans trigonométrie) : $r^2=1-h^2$, donc $\;V(h)=\pi(1-h^2)h=\pi(h-h^3),\quad h\in\,]0,1[.$

(On pourrait aussi prendre $V(r)=\pi r^2\sqrt{1-r^2}$, $r\in\,]0,1[$.) La fonction polynomiale $V(h)=\pi(h-h^3)$ se dérive sans trigonométrie : $V'(h)=\pi(1-3h^2)$, maximum en $h=\tfrac1{\sqrt3}$, cohérent avec la Q21.

---

## Partie 2 — Évolutions discrètes

**A. Des patterns**

### Question 1

Pattern **répétitif** : le pattern n°2 (le motif de base $A\,B\,C\,B$ se répète à l'identique). Pattern **évolutif** : le pattern n°1 (le motif grandit d'un rang à l'autre ; de même les patterns n°3 et n°4).

### Question 2

Pattern n°1 : rang 1 $\to 2$ carreaux, rang 2 $\to 4$ carreaux. Deux prolongements possibles :
- **Règle arithmétique** ($+2$ à chaque rang, soit $a_n=2n$) : rang 3 $\to 6$ carreaux.
- **Règle géométrique** ($\times 2$ à chaque rang, soit $a_n=2^n$) : rang 3 $\to 8$ carreaux.

Avec seulement deux termes, le pattern est sous-déterminé : plusieurs règles conviennent.

### Question 3

D'après l'annexe 2.4, l'activité « déterminer le nombre d'allumettes selon le rang » relève des **exercices et problèmes ouverts favorisant la prise d'initiatives** (tâche de recherche et de généralisation).

### Question 4

Question intermédiaire ne dénaturant pas le type de tâche : *« Combien d'allumettes faut-il pour construire le motif de rang 5 ? »* On fait franchir un rang un peu éloigné (sans révéler le modèle d'évolution), ce qui incite l'élève à chercher une structure sans lui fournir la règle.

En se référant à l'annexe 2.5 (passage à l'abstraction algébrique), on modifie la présentation du pattern en **distinguant par une couleur les allumettes ajoutées d'un rang au suivant** (et celles reprises du rang précédent). Rendre visible l'**incrément constant** (ici $+5$ allumettes par maison) facilite l'écriture d'une expression générale et le passage au modèle algébrique.

### Question 5

Deux intérêts : (i) **mettre en évidence la pluralité des stratégies** (décompositions différentes du motif) conduisant au **même résultat** ; (ii) **favoriser le débat et l'argumentation** entre pairs, et motiver le **calcul littéral** en prouvant l'**équivalence** des écritures obtenues.

### Question 6

Une maison isolée compte $6$ allumettes ; chaque maison supplémentaire partage une allumette verticale avec la précédente, soit $5$ allumettes de plus. Au rang $n$ : $u_n=6+5(n-1)=5n+1$. Vérification : $u_1=6,\ u_2=11,\ u_3=16$.
- Élève 1 : $2n+2n+(n+1)=5n+1$ $\Rightarrow$ **juste**.
- Élève 2 : $6n-(n-1)=5n+1$ $\Rightarrow$ **juste**.
- Élève 3 : $5n+1$ $\Rightarrow$ **juste**.
- Élève 4 : $4n+4$ ; pour $n=1$, $8\neq6$ $\Rightarrow$ **faux**.

**Les réponses justes sont celles des élèves 1, 2 et 3.**

### Question 7

> **Bilan.** Pour trouver le nombre d'allumettes au rang $n$, plusieurs démarches sont possibles :
> - en comptant séparément les groupes d'allumettes (toits, horizontales, verticales) : $2n+2n+(n+1)$ ;
> - en partant d'une maison isolée ($6$ allumettes) et en retirant les allumettes communes : $6n-(n-1)$ ;
> - en remarquant qu'on ajoute $5$ allumettes à chaque maison à partir de $6$ : $5n+1$.
>
> Ces trois écritures sont **égales** : $2n+2n+(n+1)=6n-(n-1)=5n+1$. Différentes stratégies, correctement menées, conduisent donc à **la même formule générale $5n+1$** : il n'y a pas une seule bonne méthode.

### Question 8

Critère sur « Communiquer » : **la justification de la formule et l'emploi du langage algébrique**. L'élève 2 **explique** sa procédure (« une maison contient 6 allumettes… il faut enlever les bords communs ») et l'écrit **symboliquement** ($6\times \text{rang}-(\text{rang}-1)$) ; l'élève 3 se borne à décrire une procédure en langage naturel (« je multiplie le rang par 5 et je rajoute 1 ») **sans justification ni écriture algébrique**. L'élève 2 satisfait le critère, pas l'élève 3.

### Question 9

« À quel rang faut-il exactement **101 allumettes** ? » Cela conduit à résoudre l'**équation** $5n+1=101$, soit $n=20$.

**B. Une suite linéaire récurrente**

### Question 10

On définit la suite $(u_n)$ par

$$

\begin{aligned}
u_1&=1,\quad u_2=1,\\
\text{pour tout entier }n\ge 3,\quad u_n&=u_{n-1}+u_{n-2}.
\end{aligned}

$$

On demande de déterminer $u_{50}$.

### Question 11

**Non.** Au regard de l'annexe 2.8, le programme de première ne prévoit le calcul d'une **formule explicite** que pour les suites **arithmétiques** et **géométriques**. Or $(u_n)$ n'est **ni arithmétique** ($u_2-u_1=0$ mais $u_3-u_2=1$ : différences non constantes) **ni géométrique** ($u_2/u_1=1$ mais $u_3/u_2=2$ : quotients non constants). Les méthodes du programme ne s'appliquent donc pas, et l'on ne peut exiger une formule explicite : seule la **relation de récurrence** est accessible.

### Question 12

Dans le tableur, l'élève a saisi la **valeur** littérale « $=3+2$ » en B6, ce qui ne se recopie pas. Correction exploitant le tableur : saisir $u_1,u_2$ comme valeurs en B2 et B3, puis en **B4** entrer la formule **`=B3+B2`** (référence relative aux deux cellules précédentes), et **recopier vers le bas** jusqu'à la ligne 51 (le rang $50$ correspond à la ligne $51$). Le tableur recalcule alors automatiquement tous les termes.

### Question 13

Question supplémentaire incitant à l'algorithme : *« Déterminer le plus petit rang $n$ pour lequel $u_n\ge 10^6$. »* La recherche d'un **seuil**, dont on ignore a priori le rang, appelle naturellement une boucle **tant que** (while).

### Question 14

La boucle **`for`** est préférable car le **nombre d'itérations est connu à l'avance** : pour calculer le terme de rang $n$ donné, on effectue exactement $n-2$ pas. On réserve la boucle **`while`** aux cas où le nombre de répétitions est inconnu (recherche de seuil, Q13).

Traçons `suite(4)` : `u=1, v=1`, `range(3,5)` donne $i=3,4$.
- $i=3$ : `u=v` $\to$ `u=1` ; `v=u+v` $\to$ `v=1+1=2`.
- $i=4$ : `u=v` $\to$ `u=2` ; `v=u+v` $\to$ `v=2+2=4`. Retour : $4$.

Or $u_4=3$ (car $u_3=2$, $u_4=u_3+u_2=3$) : **le programme est incorrect**. L'erreur : `v=u+v` utilise la **nouvelle** valeur de `u` (déjà écrasée par `u=v`), ce qui calcule $v+v=2v$ au lieu de $u_{\text{ancien}}+v$. Correction avec variable temporaire :
```python
def suite(n):
    u = 1
    v = 1
    for i in range(3, n+1):
        w = u + v
        u = v
        v = w
    return v
```
Vérification `suite(4)` : $i=3$ : $w=2,u=1,v=2$ ; $i=4$ : $w=3,u=2,v=3$ ; retour $3$ (et `suite(1)=suite(2)=1`). On peut aussi écrire l'affectation simultanée `u, v = v, u+v`.

### Question 15

Il s'agit de la **suite de Fibonacci** ; la constante apparaissant dans sa formule explicite (formule de Binet) est le **nombre d'or** $\varphi=\dfrac{1+\sqrt5}{2}$.

### Question 16

En l'absence de formule explicite accessible (Q11), on ne peut pas **anticiper** $u_{50}$ par un calcul direct : il faut **exécuter pas à pas** la relation de récurrence (répéter le même calcul en progressant de rang en rang). Cette démarche **procédurale, itérative**, relève — au sens de l'annexe 2.5 — de la **pensée algorithmique** (par opposition à la pensée algébrique, fondée sur l'anticipation par une formule générale).

**C. Une figure fractale (flocon de Koch)**

### Question 17

Deux prérequis : les **suites géométriques** (raison, terme général, comportement de $q^n$ et somme $1+q+\dots+q^{n}$) et la **notion de limite d'une suite** (convergence, théorèmes de comparaison ; convergence des suites croissantes majorées).

### Question 18

Groupe 2 : **réussite** — il a correctement repéré le schéma multiplicatif ($3,12,48$ : le nombre de segments est **multiplié par $4$** à chaque étape, et la longueur d'un segment **divisée par $3$**). **Erreur** — la formule générale proposée « $u_{n+1}=4n:\big(\tfrac13\big)^{n+1}$ » est fausse et confuse : notation $4n$ au lieu de $4^n$, mélange entre nombre de segments et longueur, absence d'une suite géométrique correctement écrite.

Intérêt de confronter groupes 1 et 3 : le **groupe 1** mène un calcul **complet et rigoureux** du périmètre ($p_n=3a(4/3)^n\to+\infty$ via la suite géométrique), tandis que le **groupe 3** **conjecture** la relation $u_{n+1}=\tfrac43 u_n$ et écrit $u_n=u_0(4/3)^n$. Les présenter ensemble permet d'articuler **conjecture et démonstration**, de valoriser différents degrés de formalisation et de montrer comment passer d'une idée à une preuve.

### Question 19

Montrons par récurrence que pour tout réel $a>0$ et tout $n\in\mathbb N$, $(1+a)^n\ge 1+na$.
*Initialisation* ($n=0$) : $(1+a)^0=1\ge 1+0\cdot a=1$.
*Hérédité* : supposons $(1+a)^n\ge 1+na$ pour un entier $n$ fixé. Comme $1+a>0$,

$$

\begin{aligned}
(1+a)^{n+1}=(1+a)^n(1+a)&\ge(1+na)(1+a)\\
&=1+(n+1)a+na^2\ge 1+(n+1)a,
\end{aligned}

$$

car $na^2\ge 0$.
Par récurrence, l'inégalité est vraie pour tout $n\in\mathbb N$. $\qquad\square$

On pose $a=\tfrac13>0$, de sorte que $\tfrac43=1+\tfrac13$. Par Bernoulli,

$$
\Big(\tfrac43\Big)^n=\Big(1+\tfrac13\Big)^n\ge 1+\tfrac n3.
$$

Or $1+\tfrac n3\to+\infty$ quand $n\to+\infty$ ; par **théorème de comparaison** (minoration par une suite tendant vers $+\infty$), $\Big(\tfrac43\Big)^n\to+\infty.$ $\qquad\square$

**Non.** Contre-exemple : la suite géométrique de raison $q=-1$, $\big((-1)^n\big)=1,-1,1,-1,\dots$, **n'a pas de limite** (elle prend indéfiniment deux valeurs distinctes). Plus généralement, pour $q\le -1$ la suite $(q^n)$ n'a pas de limite.

> **Propriété.** Soit $q\in\mathbb R$ et la suite $(q^n)_{n\in\mathbb N}$.
> - si $q>1$ : $q^n\to+\infty$ ;
> - si $q=1$ : $q^n=1\to 1$ ;
> - si $-1<q<1$ : $q^n\to 0$ ;
> - si $q\le -1$ : $(q^n)$ n'a pas de limite.
>
> **Démonstration (cas au programme).** *Cas $q>1$* : on écrit $q=1+a$ avec $a=q-1>0$ ; par l'inégalité de Bernoulli, $q^n\ge 1+na\to+\infty$, donc $q^n\to+\infty$. *Cas $-1<q<1$* : si
> $q=0$, c'est immédiat ; sinon $0<|q|<1$, donc $\tfrac1{|q|}>1$ et $\big(\tfrac1{|q|}\big)^n\to+\infty$ par le cas précédent ; ainsi $|q|^n=\dfrac1{\big(1/|q|\big)^n}\to 0$, d'où $q^n\to 0$. *Cas
> $q=1$* : suite constante. Enfin, pour $q=-1$, les sous-suites paires et impaires valent respectivement $1$ et $-1$. Pour $q<-1$, elles tendent respectivement vers $+\infty$ et $-\infty$, puisque $|q|>1$. Dans ces deux cas, $(q^n)$ n'a donc pas de limite, même infinie.

### Question 20

L'enseignant peut s'appuyer sur le **théorème admis** de l'annexe 2.14 : « toute suite **croissante majorée** converge ». La suite $(a_n)$ des aires est **croissante** (on ajoute de l'aire à chaque étape) et **majorée** (le flocon reste contenu dans une région bornée, par exemple le disque circonscrit au triangle initial) : elle **converge** donc, ce qui prouve que l'aire est **finie**, sans recourir à l'expression de $a_n$.

### Question 21

On admet $a_n=\dfrac{\sqrt3}{4}\ell^2\Big[1+\dfrac35\big(1-(\tfrac49)^n\big)\Big]$. Comme $0<\tfrac49<1$, on a $\big(\tfrac49\big)^n\to 0$. Par opérations sur les limites,

$$
a_n\xrightarrow[n\to+\infty]{}\frac{\sqrt3}{4}\ell^2\Big[1+\frac35(1-0)\Big]=\frac{\sqrt3}{4}\ell^2\cdot\frac85=\frac{2\sqrt3}{5}\ell^2.
$$

L'aire du flocon de Koch est donc **finie**, égale à $\dfrac{2\sqrt3}{5}\ell^2=\dfrac85\times\dfrac{\sqrt3}{4}\ell^2$, c'est-à-dire **$\tfrac85$ de l'aire du triangle initial**.

### Question 22

*Énoncé proposé.*
> On note $\ell$ la longueur du côté du triangle équilatéral de rang $0$, $c_n$ le nombre de côtés du polygone de rang $n$, et $\lambda_n$ la longueur d'un côté au rang $n$. On rappelle que l'aire d'un triangle équilatéral de côté
> $s$ est $\tfrac{\sqrt3}{4}s^2$.
> 1. Justifier que $c_0=3$ et que, pour tout $n$, $c_{n+1}=4\,c_n$. En déduire $c_n$.
> 2. Justifier que $\lambda_n=\dfrac{\ell}{3^n}$.
> 3. Au passage du rang $n$ au rang $n+1$, on construit un petit triangle équilatéral de côté $\lambda_{n+1}$ sur chacun des $c_n$ côtés. Exprimer l'aire ajoutée $t_n=a_{n+1}-a_n$, et montrer que $t_n=\dfrac{\sqrt3}{4}\ell^2\cdot\dfrac13\Big(\dfrac49\Big)^n$.
> 4. En écrivant $a_n=a_0+\displaystyle\sum_{k=0}^{n-1}t_k$ et en calculant cette somme géométrique, retrouver $a_n=\dfrac{\sqrt3}{4}\ell^2\Big[1+\dfrac35\big(1-(\tfrac49)^n\big)\Big]$.

*Vérification (pour le correcteur).* $c_n=3\cdot4^n$, $\lambda_{n+1}=\ell/3^{n+1}$, aire d'un petit triangle $=\tfrac{\sqrt3}{4}\ell^2/9^{n+1}$, donc $t_n=3\cdot4^n\cdot\tfrac{\sqrt3}{4}\ell^2/9^{n+1}=\tfrac{\sqrt3}{4}\ell^2\cdot\tfrac13(4/9)^n$. Puis $\sum_{k=0}^{n-1}(4/9)^k=\tfrac{9}{5}\big(1-(4/9)^n\big)$, d'où $a_n=\tfrac{\sqrt3}{4}\ell^2\big[1+\tfrac35(1-(4/9)^n)\big]$.
