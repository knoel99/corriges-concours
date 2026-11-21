# Olympiades internationales de mathématiques — Lycée — Mathématiques 1959 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Les six problèmes de la première édition, publiés en anglais dans l’archive de l’IMO, parcourent arithmétique, radicaux, angles doubles et constructions géométriques. Les questions 1 et 2 donnent des points d’entrée courts. Dans les constructions 4 et 6, réserver du temps à la réciproque et aux cas où la figure existe. Le cinquième problème se prête à un repère commun aux trois demandes.

### 1959/1

> [!INDICATION]
> Cherche une combinaison entière des deux expressions qui élimine le terme en $n$.

#### Solution

Tout diviseur commun à $21n+4$ et $14n+3$ divise aussi $3(14n+3)-2(21n+4)=1$. **La fraction est irréductible pour tout entier naturel $n$.**

### 1959/2

> [!INDICATION]
> Avant de développer le carré de la somme, détermine son domaine. Prends garde à la racine d’un carré.

#### Solution

La racine intérieure impose $x\geq1/2$. Pour ces valeurs, $x\geq0$ et $x^2-(2x-1)=(x-1)^2\geq0$, donc les deux racines extérieures existent. Notons $S$ leur somme. Alors
$$
S^2=2x+2\sqrt{x^2-2x+1}=2x+2|x-1|.
$$
Sur $[1/2,1]$, $S=\sqrt2$ ; sur $[1,+\infty[$, $S=\sqrt{4x-2}$. On obtient donc **(a) $x\in[1/2,1]$ ; (b) aucune solution ; (c) $x=3/2$**.

> [!METHODE]
> Une racine carrée est positive ou nulle : écrire $\sqrt{(x-1)^2}=x-1$ sans distinction de signe ferait disparaître tout un intervalle.

### 1959/3

> [!INDICATION]
> Exprime le double angle en fonction de $\cos^2x$. Examine l’information de signe perdue en élevant au carré.

#### Solution

Posons $t=\cos x$ et $z=\cos(2x)=2t^2-1$, avec $a\ne0$. L’équation initiale donne $2bt=-[a(z+1)+2c]$. En l’élevant au carré, on obtient l’équation du second degré cherchée pour les images des racines :
$$
\boxed{[a(z+1)+2c]^2-2b^2(z+1)=0.}
$$
Plus précisément, si les racines algébriques de $at^2+bt+c$ sont $t_1,t_2$, les deux racines de ce polynôme en $z$ sont $2t_1^2-1$ et $2t_2^2-1$ (avec leurs multiplicités). Pour un angle réel, chaque racine initiale conduit à une solution de l’équation en double angle. L’inverse, pour **le même angle $x$**, exige de rétablir le signe dans $2b\cos x=-[a(\cos 2x+1)+2c]$. En effet une équation en $\cos 2x$ ne distingue pas $x$ et $x+\pi$, alors que l’équation initiale peut les distinguer.

Pour $(a,b,c)=(4,2,-1)$, le nouveau polynôme vaut $16z^2+8z-4$. Après division par 4, **les deux polynômes ont les mêmes coefficients et les mêmes valeurs racines** $(-1\pm\sqrt5)/4$. Ce sont respectivement les valeurs de $\cos x$ dans le premier problème et de $\cos 2x$ dans le second. Les ensembles d’angles ne coïncident pas : par exemple, en posant $r=(-1+\sqrt5)/4$ et $x=\arccos r$, l’angle $x+\pi$ satisfait l’équation en double angle mais pas l’initiale.

### 1959/4

> [!INDICATION]
> Utilise le cercle de diamètre l’hypoténuse et calcule l’aire du triangle de deux façons.

#### Solution

Plaçons les extrémités $A,B$ de l’hypoténuse à distance $c$ et notons $I$ leur milieu. Le sommet droit $C$ doit être sur le cercle de centre $I$ et de rayon $c/2$. La condition demandée devient $CA\cdot CB=CI^2=c^2/4$. Or, si $h$ est la distance de $C$ à $AB$, l’aire donne $CA\cdot CB=c h$. Il faut et il suffit donc que **$h=c/4$**.

**Construction.** Tracer le cercle de diamètre $AB$ et les deux parallèles à $AB$ à la distance $c/4$, obtenue par deux bissections de la longueur $c$. Prendre $C$ à l’une des intersections. Le triangle est rectangle et vérifie l’égalité des aires précédente, donc la condition de moyenne géométrique. Comme $c/4<c/2$, il y a quatre positions possibles de $C$, symétriques et donnant des triangles isométriques.

### 1959/5.a

> [!INDICATION]
> Dans un repère porté par $AB$, calcule le produit scalaire des directions $AF$ et $BC$. Quels sont les diamètres des cercles ?

#### Solution

Posons $A=(0,0), B=(L,0), M=(m,0)$ avec $0<m<L$. Ainsi $C=(m,m)$ et $F=(m,L-m)$. Le produit scalaire de $(m,L-m)$ et de $(m-L,m)$ est nul. Les droites $AF$ et $BC$ sont donc perpendiculaires et se rencontrent en $N'$. Comme $N'$ est sur la droite passant par $A,F$ et sur celle passant par $B,C$, il appartient aux cercles de diamètres $AC$ et $BF$ : ces diamètres sont les diagonales des deux carrés. Cela reste vrai lorsque $m=L/2$ et $C=F=N'$, extrémité des deux diamètres. Enfin $M$ n’appartient pas à $AF$, donc $N'\ne M$. **Le second point d’intersection est $N=N'$.**

### 1959/5.b

> [!INDICATION]
> La corde commune est perpendiculaire à la droite des centres. Exprime la droite passant par $M$ avec cette direction normale.

#### Solution

Les centres sont $P=(m/2,m/2)$ et $Q=((L+m)/2,(L-m)/2)$. Leur différence vaut $(L/2,(L-2m)/2)$. La corde commune $MN$ est perpendiculaire à $PQ$, d’où son équation
$$
L(x-m)+(L-2m)y=0.
$$
Les coordonnées **$S=(L/2,-L/2)$** vérifient cette égalité pour tout $m$. C’est le point de la médiatrice de $AB$ situé du côté opposé aux carrés, à la distance $L/2$ de $AB$.

### 1959/5.c

> [!INDICATION]
> Prends la moyenne des coordonnées des centres et utilise les inégalités strictes imposées à $m$.

#### Solution

Le milieu a pour coordonnées $((L+2m)/4,L/4)$. Lorsque $m$ parcourt $]0,L[$, l’abscisse parcourt exactement $]L/4,3L/4[$. **Le lieu est le segment ouvert de cette droite horizontale entre les abscisses $L/4$ et $3L/4$, à hauteur $L/4$ au-dessus de $AB$.**

### 1959/6

> [!INDICATION]
> La direction commune des bases est imposée par les deux plans. Dans le plan des bases, utilise l’axe de symétrie et la somme des longueurs des bases.

#### Solution

Chaque base appartient à un des plans et elles sont parallèles. Leur direction est donc celle de l’intersection $p$. Traçons par $A$ et $C$ les parallèles à $p$. Elles sont distinctes : si elles coïncidaient, elles appartiendraient aux deux plans et formeraient $p$ elle-même. Elles déterminent un plan et deux droites supports de distance $h>0$. Soit $H$ la projection orthogonale de $C$ sur le support de $A$ et posons $t=AH$.

Orientons ce support de $A$ vers $H$ quand $t>0$. Si $u=AB$ et $v=CD$, la symétrie du trapèze isocèle donne $t=(u+v)/2$. Sa jambe a pour longueur $\sqrt{h^2+((u-v)/2)^2}$. Comme deux tangentes issues d’un même sommet à un cercle ont même longueur, l’existence du cercle inscrit impose que les bases aient pour somme celle des deux jambes. La longueur d’une jambe doit donc être $t$, et
$$
\left(\frac{u-v}{2}\right)^2=t^2-h^2.
$$
**Si $t<h$, la construction est impossible.** Si $t\geq h$, construire $d=\sqrt{t^2-h^2}$ comme l’autre côté d’un triangle rectangle d’hypoténuse $t$ et de côté $h$. Sur la parallèle par $A$, placer $B$ dans le sens $AH$ à distance $u=t+d$ ; sur la parallèle par $C$, placer $D$ dans le sens opposé à distance $v=t-d$. On peut aussi intervertir $u$ et $v$. Ces bases sont positives car $h>0$. Leurs milieux ont même projection suivant l’axe des bases : le quadrilatère est isocèle et les jambes ont longueur $t$.

Pour vérifier le cercle inscrit, prenons $O$ au milieu du segment qui joint les milieux des bases. Il est à distance $h/2$ des deux bases et sur l’axe de symétrie. Dans le triangle $AOD$, l’aire vaut $(u+v)h/8=th/4$ (utiliser l’axe et les demi-bases, ou des coordonnées). Comme $AD=t$, la distance de $O$ à $AD$ est $h/2$, et il en est de même pour l’autre jambe. Le cercle de centre $O$ et de rayon $h/2$ convient. **Les deux choix sont les seules solutions pour $t>h$. Lorsque $t=h$, ils coïncident en un carré** (si le mot trapèze impose une seule paire de côtés parallèles, ce cas est à écarter).

## Bilan

Une condition nécessaire ne suffit pas à une construction : repartir de l’objet construit et vérifier chaque tangence ou longueur. Dans les problèmes algébriques, relever ce qu’oublie une opération : élever au carré perd un signe, doubler un angle peut confondre deux angles.
