# Olympiades nationales de mathématiques — Première hors spécialité mathématiques — Épreuve nationale 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Deux heures sont consacrées à cette partie nationale de la zone Métropole, La Réunion, Mayotte, Europe, Afrique et Orient. Ce parcours réunit la voie générale sans spécialité mathématiques et toutes les voies technologiques. Les deux exercices peuvent se chercher dans n’importe quel ordre. Réserver environ la moitié du temps à chacun. Commencer par les petites situations de calcul et les exemples numériques permet de vérifier rapidement ses premiers résultats. La seconde partie de la recherche fait passer des sommes de termes consécutifs à une récurrence puis à un programme.

## Exercice 1 — Plus fort !

Les sept situations sont pour l’essentiel indépendantes. Selon la question, il faut traduire une phrase, comparer des coûts ou choisir une longueur qui simplifie le calcul géométrique.

### 1.a

> [!INDICATION]
> Sur le cadran à cinq positions, décompose le déplacement en tours complets puis en pas restants.

#### Solution

Après cinq pas, on retrouve le point de départ. De la position 1, six pas en laissent un après le tour complet : on arrive en **2**. Douze pas en laissent deux après deux tours complets : on arrive en **3**.

### 1.b

> [!INDICATION]
> Compare les déplacements de douze pas et d’un seul pas.

#### Solution

Les deux déplacements ont le même effet si et seulement si leur différence, onze pas, représente un nombre entier de tours. Le nombre de graduations divise donc 11. Puisque $n\geq 2$ et que 11 est premier, **$n=11$**. Voici le cadran, dans le sens horaire :

```text
              11
         10         1
       9               2
      8                 3
        7             4
            6     5
```

### 2.a

> [!INDICATION]
> Distingue l’affirmation principale du raisonnement au conditionnel.

#### Solution

Une reformulation est : **avec une audition intacte, Beethoven aurait été un compositeur de moindre envergure, cela est certain.** L’affirmation porte sur le rôle prêté à sa surdité dans sa grandeur de compositeur.

### 2.b

> [!INDICATION]
> Identifie d’abord la règle en vigueur, puis ce que demande l’association et enfin la décision prise.

#### Solution

La mairie interdit de ramasser les escargots. Une association qui veut organiser une course a demandé la levée de cette interdiction. **La mairie maintient l’interdiction.**

### 3.

> [!INDICATION]
> Une coupe à moitié de sa hauteur contient un cône semblable au cône entier.

#### Solution

Le rayon et la hauteur du petit cône valent chacun la moitié de ceux du grand. La formule $V=\pi r^2h/3$ donne un volume huit fois plus petit. On remplit donc **huit coupes** à mi-hauteur.

> [!METHODE]
> Quand toutes les longueurs sont multipliées par $k$, le volume est multiplié par $k^3$.

### 4.

> [!INDICATION]
> Prolonge mentalement le verre en une sphère et observe la profondeur du point le plus bas du bord quand on incline le verre.

#### Solution

Soit $R$ le rayon. Au départ la surface horizontale du liquide est à la distance $R/2$ sous le centre de la sphère. Tant que cette surface reste en dessous du bord, le liquide est une calotte de la sphère. Sa hauteur est constante parce que son volume est constant et que le volume d’une calotte croît strictement avec sa hauteur. Pour une inclinaison $x$, le point le plus bas du bord se trouve à $R\sin x$ sous le centre. Le premier débordement correspond au contact, donc $R\sin x=R/2$. **L’angle limite est $30^\circ$.**

### 5.a

> [!INDICATION]
> Exprime d’abord le prix du groupe, puis divise-le par l’effectif.

#### Solution

La facture est le plus grand des montants $40n$ et $4\,000$ euros. Pour $n\geq100$, chacun paie **40 €**. En dessous de 100 convives, chacun paie $4\,000/n>40$ euros. Pour 90 personnes, la quote-part exacte est **$400/9$ euros**, soit environ 44,44 €.

### 5.b

> [!INDICATION]
> Retire la subvention de la facture totale avant de la répartir. Étudie séparément les deux règles de facturation.

#### Solution

À 90 personnes, chacun doit $(4\,000-1\,000)/90=100/3$ euros, soit environ **33,33 €**. À 120 personnes, chacun doit $(4\,800-1\,000)/120=95/3$ euros, soit environ **31,67 €**. Jusqu’à 100 convives, le coût $3\,000/n$ décroît strictement. Dès 100 convives, le coût $40-1\,000/n$ croît strictement. Le minimum, **30 € par personne**, est donc atteint pour **exactement 100 convives**.

### 6.

> [!INDICATION]
> Appelle $d$ la distance du sommet à la coupe. Tant que la coupe rencontre les deux rayons, elle délimite un triangle rectangle isocèle.

#### Solution

Notons $R$ le rayon et $d$ la distance entre le centre et la droite de coupe. La bissectrice partage le triangle au sommet en deux triangles rectangles isocèles. La base mesure donc $2d$ et l’aire vaut $d^2$. L’aire du secteur étant $\pi R^2/4$, il faut $d^2=\pi R^2/8$. On coupe perpendiculairement à la bissectrice **à la distance $R\sqrt{\pi/8}$ du centre**. La coupe rencontre bien les deux rayons à l’intérieur du disque puisque $\sqrt2d=R\sqrt{\pi}/2<R$.

### 7.

> [!INDICATION]
> Sur une des faces rectangles, projette le sommet commun aux trois angles droits sur l’hypoténuse. Cette projection donne aussi un pied de hauteur de la face oblique.

#### Solution

Appelons $O$ le sommet commun et posons $OA=a$, $OB=b$, $OC=c$. Soit $H$ la projection de $O$ sur $AB$. Le segment $OC$ étant perpendiculaire au plan $OAB$, les directions $OH$ et $OC$ sont orthogonales à $AB$. Ainsi $CH$ est une hauteur du triangle $ABC$, avec $CH^2=c^2+OH^2$. Les deux calculs de l’aire de $OAB$ donnent $AB\times OH=ab$. Par conséquent
$$
4\,\mathcal A(ABC)^2=AB^2 CH^2=(a^2+b^2)c^2+a^2b^2.
$$
Les trois termes de droite sont quatre fois les carrés des aires des faces $OAC$, $OBC$ et $OAB$. **Le carré de l’aire oblique est la somme des trois carrés des aires adjacentes à $O$.**

## Exercice 3 — Recherche d’équilibre : les nombres sur le fil

La balance compare deux sommes consécutives. Transformer cette définition en critère arithmétique permet ensuite de produire des exemples sans additionner leurs termes un à un.

### 1.

> [!INDICATION]
> Écris la même somme dans les deux sens et additionne par colonnes.

#### Solution

Pour $S=1+\cdots+m$, chaque terme $j$ de la somme dans l’ordre croissant fait face à $m+1-j$ dans l’ordre décroissant. Les $m$ couples valent tous $m+1$. Donc $2S=m(m+1)$, soit **$S=m(m+1)/2$**.

### 2.

> [!INDICATION]
> Mets à part la contribution de $n$ dans chacun des $b$ termes.

#### Solution

Les $b$ termes ont pour somme $bn+(1+\cdots+b)=bn+b(b+1)/2$, d’où **$b(2n+b+1)/2$**.

### 3.a

> [!INDICATION]
> Utilise les premiers entiers qui suivent 6.

#### Solution

La somme de 1 à 5 vaut 15 et $7+8=15$. La somme de droite croît strictement avec son nombre de termes. **La balance de 6 est 2.**

### 3.b

> [!INDICATION]
> Encadre la somme de gauche entre deux sommes successives commençant à 8.

#### Solution

La somme de 1 à 6 vaut 21. Les sommes commençant à 8 augmentent strictement et deux sommes successives valent $8+9=17$ puis $8+9+10=27$. **7 n’est pas équilibré.**

### 3.c

> [!INDICATION]
> Compare deux sommes arithmétiques par leurs premier et dernier termes.

#### Solution

D’un côté $203\times204/2=20\,706$. De l’autre, les 84 termes de 205 à 288 ont pour somme $84(205+288)/2=20\,706$. **204 est équilibré de balance 84.**

### 4.a

> [!INDICATION]
> Exprime les deux sommes en fonction de $n$ et de $b$, puis complète le carré.

#### Solution

Doubler les deux sommes donne $n(n-1)=b(2n+b+1)$, soit $n^2-n=2bn+b^2+b$. Multiplier par 4 et regrouper donne $8n^2+1=(2n+2b+1)^2$. Comme $2n+2b+1>0$, **$b=(\sqrt{8n^2+1}-2n-1)/2$** et **$8n^2+1$ est un carré parfait**.

### 4.b

> [!INDICATION]
> Examine la parité de $e$, puis compare son carré à celui de $2n+1$.

#### Solution

Le carré $e^2=8n^2+1$ est impair, donc $e$ est impair. Le nombre $e-2n-1$ est ainsi pair. De plus $e^2-(2n+1)^2=4n(n-1)>0$ puisque $n\geq2$. Les deux nombres comparés sont positifs, donc $e>2n+1$ et **$b=(e-2n-1)/2$ est un entier strictement positif**.

### 4.c

> [!INDICATION]
> Dans le sens réciproque, il reste à vérifier que l’entier construit équilibre réellement les sommes.

#### Solution

Le sens direct découle de l’égalité des carrés. Réciproquement, pour le $b$ entier positif construit ci-dessus, $2n+2b+1=e$. En mettant au carré puis en développant, on retrouve $b(2n+b+1)=n(n-1)$, donc l’égalité des deux sommes. Ainsi **$n$ est équilibré si et seulement si $8n^2+1$ est un carré parfait.**

> [!METHODE]
> Retrouver la condition de départ évite de confondre une condition nécessaire avec une équivalence.

### 5.a

> [!INDICATION]
> Développe les deux carrés en gardant un symbole pour la racine commune.

#### Solution

Posons $t=\sqrt{8x^2+1}$. D’une part $8(3x+t)^2+1=136x^2+48xt+9$. D’autre part $(8x+3t)^2=64x^2+48xt+9(8x^2+1)$, qui donne la même expression. **L’identité est établie pour tout réel $x$.**

### 5.b

> [!INDICATION]
> Applique le critère du carré parfait une première fois à $n$, une seconde fois à son image.

#### Solution

Si $n$ est équilibré, $t=\sqrt{8n^2+1}$ est un entier positif. Le nombre $f(n)=3n+t$ est entier et supérieur à 2. L’identité précédente donne $8f(n)^2+1=(8n+3t)^2$, carré d’un entier. **$f(n)$ est équilibré.**

### 5.c

> [!INDICATION]
> Sépare l’hérédité de la propriété « équilibré » de la comparaison entre deux termes consécutifs.

#### Solution

Le premier terme 6 est équilibré. Le résultat précédent transmet cette propriété de $u_k$ à $u_{k+1}$ : tous les termes sont équilibrés par récurrence. Comme $f(x)>3x>x$ pour $x>0$, **la suite est strictement croissante**.

### 6.

> [!INDICATION]
> Ici $n$ compte les termes demandés. Ajoute le terme courant avant de passer au suivant.

#### Solution

On appelle `sqrt` la racine carrée entière de Python. Comme les radicandes sont des carrés parfaits, elle calcule exactement leur racine, même pour de grands entiers.

```python
from math import isqrt as sqrt

def liste_equilibres(n):
    termes = []
    u = 6
    for _ in range(n):
        termes.append(u)
        u = 3 * u + sqrt(8 * u * u + 1)
    return termes
```

Au début du passage d’indice $k-1$, la variable contient $u_k$. Les $n$ passages ajoutent donc exactement **$u_1,\ldots,u_n$**.

## Bilan

Pour les questions géométriques, déterminer ce qui reste fixe avant de calculer : forme semblable, volume, point de projection. Pour l’arithmétique, un critère utilisable dans les deux sens demande deux preuves. Tester son programme sur 6 et 35 révèle aussitôt une confusion entre le nombre de termes et la borne de la liste.
