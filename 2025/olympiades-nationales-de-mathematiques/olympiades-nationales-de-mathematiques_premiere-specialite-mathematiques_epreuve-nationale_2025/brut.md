# Olympiades nationales de mathématiques — Première spécialité mathématiques — Épreuve nationale 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Exercice 1 — Plus fort !

### 1.a

Après cinq pas, on retrouve le point de départ. De la position 1, six pas en laissent un après le tour complet : on arrive en **2**. Douze pas en laissent deux après deux tours complets : on arrive en **3**.

### 1.b

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

Une reformulation est : **avec une audition intacte, Beethoven aurait été un compositeur de moindre envergure, cela est certain.** L’affirmation porte sur le rôle prêté à sa surdité dans sa grandeur de compositeur.

### 2.b

La mairie interdit de ramasser les escargots. Une association qui veut organiser une course a demandé la levée de cette interdiction. **La mairie maintient l’interdiction.**

### 3.

Le rayon et la hauteur du petit cône valent chacun la moitié de ceux du grand. La formule $V=\pi r^2h/3$ donne un volume huit fois plus petit. On remplit donc **huit coupes** à mi-hauteur.

### 4.

Soit $R$ le rayon. Au départ la surface horizontale du liquide est à la distance $R/2$ sous le centre de la sphère. Tant que cette surface reste en dessous du bord, le liquide est une calotte de la sphère. Sa hauteur est constante parce que son volume est constant et que le volume d’une calotte croît strictement avec sa hauteur. Pour une inclinaison $x$, le point le plus bas du bord se trouve à $R\sin x$ sous le centre. Le premier débordement correspond au contact, donc $R\sin x=R/2$. **L’angle limite est $30^\circ$.**

### 5.a

La facture est le plus grand des montants $40n$ et $4\,000$ euros. Pour $n\geq100$, chacun paie **40 €**. En dessous de 100 convives, chacun paie $4\,000/n>40$ euros. Pour 90 personnes, la quote-part exacte est **$400/9$ euros**, soit environ 44,44 €.

### 5.b

À 90 personnes, chacun doit $(4\,000-1\,000)/90=100/3$ euros, soit environ **33,33 €**. À 120 personnes, chacun doit $(4\,800-1\,000)/120=95/3$ euros, soit environ **31,67 €**. Jusqu’à 100 convives, le coût $3\,000/n$ décroît strictement. Dès 100 convives, le coût $40-1\,000/n$ croît strictement. Le minimum, **30 € par personne**, est donc atteint pour **exactement 100 convives**.

### 6.

Notons $R$ le rayon et $d$ la distance entre le centre et la droite de coupe. La bissectrice partage le triangle au sommet en deux triangles rectangles isocèles. La base mesure donc $2d$ et l’aire vaut $d^2$. L’aire du secteur étant $\pi R^2/4$, il faut $d^2=\pi R^2/8$. On coupe perpendiculairement à la bissectrice **à la distance $R\sqrt{\pi/8}$ du centre**. La coupe rencontre bien les deux rayons à l’intérieur du disque puisque $\sqrt2d=R\sqrt{\pi}/2<R$.

### 7.

Appelons $O$ le sommet commun et posons $OA=a$, $OB=b$, $OC=c$. Soit $H$ la projection de $O$ sur $AB$. Le segment $OC$ étant perpendiculaire au plan $OAB$, les directions $OH$ et $OC$ sont orthogonales à $AB$. Ainsi $CH$ est une hauteur du triangle $ABC$, avec $CH^2=c^2+OH^2$. Les deux calculs de l’aire de $OAB$ donnent $AB\times OH=ab$. Par conséquent
$$
4\,\mathcal A(ABC)^2=AB^2 CH^2=(a^2+b^2)c^2+a^2b^2.
$$
Les trois termes de droite sont quatre fois les carrés des aires des faces $OAC$, $OBC$ et $OAB$. **Le carré de l’aire oblique est la somme des trois carrés des aires adjacentes à $O$.**

## Exercice 2 — Recherche d’équilibre : les nombres sur le fil

### 1.a

La somme de 1 à 5 vaut 15 et $7+8=15$. La somme de droite croît strictement avec son nombre de termes. **La balance de 6 est 2.**

### 1.b

La somme de 1 à 6 vaut 21. Les sommes commençant à 8 augmentent strictement et deux sommes successives valent $8+9=17$ puis $8+9+10=27$. **7 n’est pas équilibré.**

### 1.c

D’un côté $203\times204/2=20\,706$. De l’autre, les 84 termes de 205 à 288 ont pour somme $84(205+288)/2=20\,706$. **204 est équilibré de balance 84.**

### 2.a

Doubler les deux sommes donne $n(n-1)=b(2n+b+1)$, soit $n^2-n=2bn+b^2+b$. Multiplier par 4 et regrouper donne $8n^2+1=(2n+2b+1)^2$. Comme $2n+2b+1>0$, **$b=(\sqrt{8n^2+1}-2n-1)/2$** et **$8n^2+1$ est un carré parfait**.

### 2.b

Le carré $e^2=8n^2+1$ est impair, donc $e$ est impair. Le nombre $e-2n-1$ est ainsi pair. De plus $e^2-(2n+1)^2=4n(n-1)>0$ puisque $n\geq2$. Les deux nombres comparés sont positifs, donc $e>2n+1$ et **$b=(e-2n-1)/2$ est un entier strictement positif**.

### 2.c

Le sens direct découle de l’égalité des carrés. Réciproquement, pour le $b$ entier positif construit ci-dessus, $2n+2b+1=e$. En mettant au carré puis en développant, on retrouve $b(2n+b+1)=n(n-1)$, donc l’égalité des deux sommes. Ainsi **$n$ est équilibré si et seulement si $8n^2+1$ est un carré parfait.**

### 3.a

Posons $t=\sqrt{8x^2+1}$. D’une part $8(3x+t)^2+1=136x^2+48xt+9$. D’autre part $(8x+3t)^2=64x^2+48xt+9(8x^2+1)$, qui donne la même expression. **L’identité est établie pour tout réel $x$.**

### 3.b

Si $n$ est équilibré, $t=\sqrt{8n^2+1}$ est un entier positif. Le nombre $f(n)=3n+t$ est entier et supérieur à 2. L’identité précédente donne $8f(n)^2+1=(8n+3t)^2$, carré d’un entier. **$f(n)$ est équilibré.**

### 3.c

Le premier terme 6 est équilibré. Le résultat précédent transmet cette propriété de $u_k$ à $u_{k+1}$ : tous les termes sont équilibrés par récurrence. Comme $f(x)>3x>x$ pour $x>0$, **la suite est strictement croissante**.

### 3.d

Pour $x=u_{k-1}>0$, posons $t=\sqrt{8x^2+1}$, puis $y=f(x)=3x+t=u_k$. L’identité de 3.a et le signe positif de $8x+3t$ donnent $\sqrt{8y^2+1}=8x+3t$. Alors $3y-\sqrt{8y^2+1}=9x+3t-8x-3t=x$. Ainsi **$u_{k-1}=3u_k-\sqrt{8u_k^2+1}$**.

### 3.e

Si $x>0$, on a $h'(x)=3/(2\sqrt{x})-4/\sqrt{8x+1}$. Son signe est celui de $3\sqrt{8x+1}-8\sqrt{x}$. Ces deux quantités positives vérifient $9(8x+1)-64x=8x+9>0$, donc **$h$ croît strictement**. Or $g(x)=h(x^2)$ pour $x>0$, et le carré y est strictement croissant. **$g$ croît strictement** également.

### 3.f

On trouve $u_2=18+17=35$. Les seuls nombres équilibrés avant 36 étant $u_1$ et $u_2$, le contre-exemple minimal $n$ est supérieur à 35. La suite croît et n’est pas bornée car $u_{k+1}>3u_k$. Comme $n$ ne fait pas partie de la suite, il existe $m\geq2$ tel que $u_m<n<u_{m+1}$. Par croissance de $g$ et d’après 3.d, $u_{m-1}<g(n)<u_m$.
Posons $t=\sqrt{8n^2+1}\in\mathbb N$. Alors $g(n)=3n-t$ est un entier supérieur à $u_{m-1}\geq6$. En développant, $8g(n)^2+1=(8n-3t)^2$. Par le critère de 2.c, $g(n)$ est équilibré. Il se trouve entre deux termes consécutifs, donc hors de la suite, et il est inférieur à $n$. Cela contredit la minimalité de $n$. **Les $u_k$ sont tous les nombres équilibrés.**

### 4.a

Les deux expressions $u_{k+1}=3u_k+\sqrt{8u_k^2+1}$ et $u_{k-1}=3u_k-\sqrt{8u_k^2+1}$ donnent par addition **$u_{k+1}=6u_k-u_{k-1}$** pour $k\geq2$.

### 4.b

Initialement $i=2$ et $s=1$. Au début de chaque test, $s$ est la somme de 1 à $i-1$. Ajouter $i$ puis augmenter $i$ conserve cette propriété. La boucle s’arrête à $i=n$, y compris si $n=2$ dès le départ. **La fonction renvoie $n(n-1)/2$.**

### 4.c

D’après 3.f, il suffit de tester l’appartenance à la suite. Pour le premier passage on peut initialiser le prédécesseur à 1, car $6\times6-1=35$.

```python
def equilibre(n):
    precedent, courant = 1, 6
    while courant < n:
        precedent, courant = courant, 6 * courant - precedent
    return courant == n
```

La boucle se termine puisque la suite est non bornée. **Elle reconnaît précisément les entiers équilibrés.** Chaque passage multiplie le terme par plus de trois : le nombre de passages est d’ordre au plus logarithmique en $n$. La somme itérative de 4.b demande à elle seule un nombre de passages proportionnel à $n$.

### 5.

On emploie la même récurrence, en enregistrant chaque terme avant de le dépasser.

```python
def liste_equilibres(n):
    termes = []
    precedent, courant = 1, 6
    while courant < n:
        termes.append(courant)
        precedent, courant = courant, 6 * courant - precedent
    return termes
```

Les termes arrivent dans l’ordre strictement croissant et forment tous les nombres équilibrés ; la liste contient donc **exactement ceux qui sont strictement inférieurs à $n$**. Pour $n=6$ elle est vide et pour $n=35$ elle vaut `[6]`.
