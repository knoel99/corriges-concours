# ENS · MP-PC · Mathématiques-informatique 2006 — corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 25 novembre 2026

**Révision** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

Le calcul se fait d’abord coefficient par coefficient. Les convergents transforment ensuite une excellente approximation d’une racine carrée en une équation polynomiale. Celle-ci permet de reconnaître une primitive logarithmique.

## Partie 1 · Calcul dans les séries de Laurent

### Question 1.1 · Valuations et convolution

Regarder le premier indice possible pour chacune des opérations. Dans une addition, le plus petit des deux indices initiaux reste visible sauf si les deux séries commencent ensemble et se compensent. Dans un produit, les indices doivent vérifier simultanément $j\ge r$ et $i-j\ge s$. Cela laisse au plus $i-r-s+1$ termes si cet entier est positif, aucun sinon. À la première diagonale atteinte, il n’y a qu’un produit non nul. Une série non nulle se recentre à l’indice zéro en ôtant le facteur $z^r$.

La borne sur le nombre de produits est atteinte, par exemple lorsque $a_j=1$ pour tout $j\ge r$ et $b_j=1$ pour tout $j\ge s$. Il s’agit du nombre de termes non nuls avant leur addition, même si leur somme s’annule dans le corps $K$. Si l’une des séries est nulle, tous ces produits sont nuls et la somme des séries est l’autre série.

### Question 1.2 · Structure d’anneau

Raisonner à un indice fixé permet de n’utiliser que les lois du corps. Les valuations bornent inférieurement tous les indices et leur somme est prescrite. Même avec trois facteurs, les regroupements de sommes sont donc légitimes. L’unité a pour unique terme non nul le coefficient constant un.

### Question 1.3 · Inversion

Après décalage du premier coefficient à zéro, résoudre les équations du produit avec l’inverse cherché dans l’ordre des degrés. La nouvelle inconnue a toujours pour coefficient le même scalaire non nul $u_0$. Chaque étape est donc possible et unique. Replacer le décalage dans l’autre sens donne la valuation opposée.

### Question 1.4 · Inverse tronqué

Construire la sortie de gauche à droite. Voici une version qui accumule directement l’opposé de la convolution.
```text
u ← inverse(A[0])
résultat ← tableau de longueur k
résultat[0] ← u
pour n de 1 à k−1
    t ← 0
    pour j de 0 à n−1
        t ← t − résultat[j] × A[n−j]
    résultat[n] ← u × t
renvoyer résultat
```
Avant le tour $n$, le produit vaut un modulo $z^n$. Le tour annule son coefficient suivant. La somme des longueurs des boucles internes est $k(k-1)/2$.

### Question 1.5 · Newton et doublement

Il faut suivre simultanément le dénominateur et l’erreur. Le terme constant de $B_0$ vaut un et celui de son erreur vaut zéro. Si l’erreur commence assez loin, le correctif ne modifie pas le terme constant de $B_j$, donc la division suivante restera possible. En élevant $B_j-E_j/(2B_j)$ au carré puis en retranchant $U$, tous les termes de premier ordre s’éliminent. Le carré de l’erreur divisé par une unité double sa valuation.

### Question 1.6 · Existence de la racine

Fixer d’abord un nombre de coefficients à connaître. Dès que le seuil d’erreur dépasse le dernier indice demandé, toutes les corrections suivantes commencent plus loin. Le coefficient stabilisé définit donc sans ambiguïté la série limite $B$. Pour calculer un coefficient de son carré, on ne lit qu’un préfixe fini de $B$. Ce préfixe est déjà celui d’un itéré dont le carré coïncide à ce rang avec $U$. Ainsi $B^2=U$, et la puissance $z^k$ rétablit le décalage de la racine.

![Figure 1 — Les premières itérations garantissent respectivement un, deux, quatre et huit coefficients exacts pour la racine de terme constant un.](figures/precision-newton.svg)

## Partie 2 · Convergents sur un corps

### Question 2.1 · Récurrences du numérateur et du dénominateur

Observer qu’un étage de fraction continue est une homographie. Remonter les étages revient à multiplier leurs matrices dans l’ordre $a_0,\ldots,a_k$. La première colonne du produit donne le numérateur et le dénominateur et sa seconde colonne garde l’ancienne première. Cela donne deux fois la même récurrence avec les initialisations du sujet. Pour une valeur dans le corps il faut un dénominateur final non nul. Dès trois termes sur un corps quelconque, le choix $a_1=1,a_2=-1$ peut l’annuler.

### Question 2.2 · Une seule inversion

Ne calculer aucun quotient intermédiaire. Garder les deux derniers numérateurs et les deux derniers dénominateurs.
```text
si k = 0 : renvoyer a₀
précédent ← (a₀, 1)
courant ← (a₀ × a₁ + 1, a₁)
pour i de 2 à k
    (précédent, courant) ← (courant, aᵢ × courant + précédent)
si courant.dénominateur = 0 : signaler que la valeur est infinie
renvoyer courant.numérateur × inverse(courant.dénominateur)
```
Les opérations du tour se font composante par composante. L’initialisation coûte une multiplication et une addition, chaque tour en coûte deux de chaque espèce. Le dernier calcul ajoute une inversion et une multiplication.

### Question 2.3 · Différence de deux convergents

La différence de deux fractions voisines possède pour numérateur le déterminant de leurs deux colonnes. Chaque nouvel étage change le signe du déterminant car sa matrice a déterminant $-1$. Au premier étage, le numérateur de la différence vaut $1$. Les signes alternent ensuite.

### Question 2.4 · Convergence réelle

La récurrence domine celle de Fibonacci. Les dénominateurs finissent donc par devenir arbitrairement grands, tout en restant positifs. Les déplacements d’un convergent au suivant alternent en signe et décroissent vers zéro en valeur absolue. Les sommes partielles convergent par le théorème des séries alternées.

## Partie 3 · Fractions continues de polynômes

### Question 3.1 · Substitution et troncature

Le terme dominant de $U(x)$ devient celui de plus petit exposant après la substitution. Inverser change le signe de la valuation. Pour $\psi$, on peut tronquer une somme terme à terme. Dans un produit, deux puissances situées de part et d’autre du degré zéro peuvent en revanche donner une constante, comme $z$ et $z^{-1}$. La composition qui tronque puis substitue restitue donc exactement les séries déjà dépourvues de partie strictement positive.

### Question 3.2 · Limite formelle des convergents

Ici les degrés des dénominateurs augmentent au moins de un à chaque étage. La formule de différence montre que deux fractions successives coïncident de plus en plus loin dans leurs développements. En sommant les différences suivantes, les coefficients déjà acquis restent acquis. On peut donc définir chaque coefficient de la limite lorsqu’il s’est stabilisé. Les puissances négatives sont bornées dès le premier convergent, ce qui assure qu’il s’agit bien d’une série de Laurent.

### Question 3.3 · Développer une série irrationnelle

Ôter la partie polynomiale laisse des puissances positives de $z$. Le reste ne peut s’annuler car l’algorithme donnerait alors une expression rationnelle finie de $F$. Son inverse commence donc par une puissance négative, assurant un quotient polynomial de degré positif. Replacer le quotient complet de la série formelle après les $k+1$ premiers étages remplace une variable de la matrice des convergents par $\alpha_{k+1}$. Soustraire $p_k/q_k$ donne un numérateur constant $\pm1$. La valuation des deux facteurs du dénominateur vaut au total $-d_k-d_{k+1}$. Cette erreur tend bien vers zéro au sens formel.

### Question 3.4 · Meilleure approximation

Retenir d’abord la précision propre à une colonne de convergent. Son résidu $E_i$ a valuation exactement égale au degré du dénominateur suivant. Deux colonnes voisines ont un déterminant constant inversible, donc toute paire de polynômes possède des coordonnées polynomiales $a,b$ dans cette base.

Si $q$ se situe dans l’intervalle de degrés indiqué et n’est pas proportionnel au premier dénominateur, aucune coordonnée ne peut s’annuler. La première colonne seule obligerait son multiplicateur à être constant puisque $p,q$ sont premiers entre eux. La seconde seule aurait un dénominateur trop grand. Le bas degré de $q$ impose alors une compensation en tête, soit $\deg a-\deg b=d_k-d_{k-1}>0$. Dans $aE_{k-1}+bE_k$, le premier terme commence strictement avant le second, d’où la valuation $d_k-\deg a$.

Pour conclure dans tous les cas, comparer la fraction candidate au dernier convergent dont le dénominateur ne dépasse pas son degré. Le déterminant croisé est un polynôme. Les deux erreurs d’approximation, multipliées par les dénominateurs opposés, ont des valuations positives, donc leur différence aussi. L’image d’un polynôme non nul a toujours valuation négative ou nulle. Le déterminant doit s’annuler, ce qui identifie la fraction.

### Question 3.5 · Partie polynomiale de la racine

Retourner d’abord mentalement les coefficients du polynôme unitaire. La racine commence par un et l’équation du carré au rang $j$ est linéaire dans le prochain coefficient avec facteur deux.
```text
R ← tableau de m+1 coefficients, R[0] ← 1
pour j de 1 à m
    C ← somme des R[k] × R[j−k] pour 1 ≤ k < j
    R[j] ← (D[2m−j] − C) / 2
écrire R[0],…,R[m] comme coefficients de x^m,…,1
```
Ignorer les puissances suivantes est exact pour la partie polynomiale. Aucun polynôme de degré supérieur à celui de l’entrée $2m$ n’est manipulé, et le tableau de sortie correspond au degré $m$.

### Question 3.6 · Quotients complets sans séries infinies

La division par $Q_k$ est exacte dans la mise à jour de $Q_{k+1}$, car $P_{k+1}$ et $-P_k$ sont congrus modulo $Q_k$ et le carré efface leur différence de signe. Le quotient ne peut être nul sans faire de $D$ un carré. La propriété de divisibilité se transmet ainsi dès $Q_0=1$.

Pour une division suivie d’une partie polynomiale, séparer les termes de puissances positives en $z$. Diviser par un polynôme ne peut les faire remonter vers la partie polynomiale. Il suffit de diviser euclidiennement ce qui reste et de garder le quotient. Appliquer cela à $P_k+S$. Le quotient obtenu est précisément $a'_k$. L’inverse du reste a pour expression $Q_k/(S-P_{k+1})$. Multiplier par le conjugué du dénominateur redonne la forme $(S+P_{k+1})/Q_{k+1}$. Par récurrence depuis le rang zéro, les deux procédures calculent les mêmes quotients.

![Figure 2 — Pour D égal à x puissance quatre plus un, les quotients complets reviennent au même état dès le premier rang positif.](figures/quotients-complets.svg)

## Partie 4 · Reconnaître une primitive logarithmique

### Question 4.1 · Une norme constante

Dériver le logarithme, puis éliminer le dénominateur. Le coefficient de la racine donne $a'=hb$ et le terme dépourvu de racine donne $Db'+D'b/2=ha$. Une identité rationnelle ne peut imiter la racine sur un intervalle non dégénéré, sinon l’identité au carré serait polynomiale partout. Multiplier les deux équations respectivement par $2a$ et $2b$, puis soustraire, montre que la dérivée de $a^2-Db^2$ est nulle. Une valeur constante zéro ferait à nouveau de $D$ un carré ou annulerait l’argument du logarithme.

### Question 4.2 · Une solution fournit un convergent

La compensation des termes de plus grand degré dans $a^2-Db^2$ impose que $a$ ait $m$ degrés de plus que $b$, avec même coefficient dominant au signe près. Un diviseur commun non constant ne pourrait diviser la constante non nulle de la norme. Changer le signe de $a$ si besoin pour que la somme avec $bS$ double le terme dominant. Le produit de cette somme et de la différence étant constant, la différence a une valuation positive exactement égale au degré de $a$. Cette précision dépasse le degré de $b$, ce qui caractérise un convergent.

### Question 4.3 · Norme des convergents et quasi-périodicité

Écrire le même quotient complet sous sa forme de fraction issue des convergents et sous sa forme $(P_k+S)/Q_k$. Comparer séparément la constante et le coefficient de $S$. Cela donne $Dq=P_kp+Q_kr$ et $p=P_kq+Q_ks$. Éliminer $P_k$ de $p^2-Dq^2$ donne $Q_k$ fois le déterminant des deux colonnes successives, soit $(-1)^kQ_k$. Pour une primitive logarithmique, l’un de ces couples a norme constante par 4.2. À ce rang le dénominateur $Q_k$ est donc un scalaire $c$ non nul. La prochaine division polynomiale n’a plus de reste. On retrouve $P_1=H$ et $Q_1$ divisé par $c$. La queue est donc celle du rang un multipliée par $c$. À chaque inversion ce facteur est inversé, d’où la répétition des quotients à des scalaires près.

### Question 4.4 · Recherche semi-décidable

Produire les approximations une à une sans imposer de borne à l’indice. Un candidat d’excellente qualité peut avoir une norme constante sans correspondre au numérateur $h$ demandé. Vérifier donc aussi les deux équations différentielles polynomiales de 4.1, en essayant les deux signes relatifs du couple. Une norme constante non nulle exclut tout zéro de l’argument sur l’intervalle. Redimensionner les deux polynômes ensemble pour que l’argument vaille un en $x_0$. Il est alors positif par continuité. La dérivée du logarithme donne l’intégrande et la constante initiale est correcte. Le lemme de meilleure approximation garantit que tout couple solution finit par être testé à une constante commune près. En son absence, l’énumération se poursuit.
