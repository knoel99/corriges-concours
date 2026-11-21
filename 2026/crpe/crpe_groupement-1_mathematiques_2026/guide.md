# CRPE Groupement 1 — Mathématiques 2026 · Corrigé guidé

*Épreuve EST MAT 1. Corrigé rédigé par IA, non officiel.*

## Présentation du sujet

Le sujet comporte cinq exercices indépendants sur la proportionnalité, les probabilités, la géométrie, le calcul et l’algorithmique.

## Exercice 1 — Visite du musée

### Partie A, question 1

> [!INDICATION]
> Multiplie l’effectif par le prix unitaire dans la même ligne.

#### Solution

Saisir `=B2*C2` en D2. Les références relatives permettent d’étirer la formule jusqu’en D7.

### Partie A, question 2

> [!INDICATION]
> Additionne les montants des six lignes.

#### Solution

Saisir `=SOMME(D2:D7)`.

### Partie A, question 3

> [!INDICATION]
> Après une remise de 15 %, quelle fraction du total reste à payer ?

#### Solution

Saisir `=D8*(1-15%)`, ou `=D8*0,85`.

### Partie B, question 1

> [!INDICATION]
> Même si les 41 élèves viennent, le groupe ne bénéficie pas de la réduction.

#### Solution

Avec 4 adultes, l’effectif est au plus 45. Le coût sans réduction est $4\times16+8{,}50n=64+8{,}50n$ euros.

### Partie B, question 2

> [!INDICATION]
> Déduis d’abord les entrées des quatre adultes.

#### Solution

$n=(378{,}50-64)/8{,}50=37$. **37 élèves** ont participé.

### Partie C, question 1

> [!INDICATION]
> Convertis 1 h 10 min en heures.

#### Solution

$1\text{ h }10\text{ min}=7/6$ h. La vitesse moyenne est $85/(7/6)=510/7$, soit **73 km/h** à l’unité près.

### Partie C, question 2

> [!INDICATION]
> Compte le carburant et le péage dans les deux sens. Le forfait journalier est compté une fois.

#### Solution

L’aller-retour fait 170 km et consomme $170\times30/100=51$ L. Le carburant coûte $51\times1{,}60=81{,}60$ €, le péage $2\times13{,}90=27{,}80$ €, et le forfait 150 €. Total : **259,40 €**.

## Exercice 2 — Tombola

### Partie A, question 1

> [!INDICATION]
> Repère le nombre de billets qui donnent exactement 50 €.

#### Solution

Il y a 2 billets à 50 € sur 500, soit une probabilité de **$1/250$**.

### Partie A, question 2

> [!INDICATION]
> Un lot de 2 € rembourse seulement le billet.

#### Solution

Les lots strictement supérieurs à 2 € correspondent à $1+2+5+20=28$ billets. Probabilité : $28/500=\frac{7}{125}$.

### Partie A, question 3

> [!INDICATION]
> Soustrais tous les billets gagnants, y compris ceux à 2 €.

#### Solution

Il y a $500-(28+50)=422$ billets perdants. La probabilité est $422/500=\frac{211}{250}$.

### Partie B, question 1

> [!INDICATION]
> Pondère chaque nombre de billets vendus par son effectif.

#### Solution

Les 51 élèves ont vendu $4\times10+6\times4+7\times8+10\times14+15\times12+20\times3=500$ billets. La moyenne $500/51$ s’arrondit à **10 billets**.

### Partie B, question 2(a)

> [!INDICATION]
> Avec 51 valeurs ordonnées, cherche la 26e.

#### Solution

Les ventes inférieures ou égales à 7 concernent 22 élèves. Les ventes inférieures ou égales à 10 en concernent 36. La 26e valeur est donc **10**.

### Partie B, question 2(b)

> [!INDICATION]
> La médiane partage les observations en deux groupes, avec d’éventuelles égalités.

#### Solution

Au moins la moitié des élèves a vendu 10 billets ou moins et au moins la moitié en a vendu 10 ou plus.

## Exercice 3 — Cross et balisage

### Question 1

> [!INDICATION]
> Le côté de 65 m est l’hypoténuse.

#### Solution

Pythagore donne $BC^2=65^2-25^2=3600$, donc **$BC=60$ m**.

### Question 2

> [!INDICATION]
> Compare les rapports des distances au point d’intersection $A$.

#### Solution

Sur les deux droites sécantes en $A$, les points $B,A,E$ et $C,A,D$ sont dans le même ordre. Or $AE/AB=15/25=3/5$ et $AD/AC=39/65=3/5$. Par la réciproque du théorème de Thalès, $(BC)$ et $(DE)$ sont parallèles.

### Question 3

> [!INDICATION]
> Le segment $CD$ passe par $A$. Calcule $DE$ par Thalès.

#### Solution

$EB=15+25=40$ m et $CD=65+39=104$ m. Par Thalès, $DE=60\times3/5=36$ m. Le parcours mesure $40+60+104+36=\mathbf{240}$ m.

### Question 4(a)

> [!INDICATION]
> Mets toutes les longueurs en décimètres avant de calculer les volumes.

#### Solution

Le socle mesure $2{,}45\ \mathrm{dm}$ de côté et $0{,}35\ \mathrm{dm}$ de haut. Son volume vaut $2{,}45^2\times0{,}35=2{,}100875\ \mathrm{dm}^3$. Le cône a un rayon de 1 dm et une hauteur de 4,15 dm. Son volume est $4{,}15\pi/3\ \mathrm{dm}^3$. La somme est environ **6,45 dm³** au centième.

### Question 4(b)

> [!INDICATION]
> Une tonne par mètre cube équivaut à un kilogramme par décimètre cube.

#### Solution

À $1{,}6\ \mathrm{kg/dm}^3$, la masse est $1{,}6\times(2{,}100875+4{,}15\pi/3)$ kg, soit **10,3 kg** au dixième.

## Exercice 4 — Vrai ou faux

### Affirmation 1

> [!INDICATION]
> Cherche un petit contre-exemple.

#### Solution

**Faux.** 8 est divisible par 4 et ne l’est pas par 12.

### Affirmation 2

> [!INDICATION]
> Développe le produit et distribue le signe moins.

#### Solution

**Vrai.** Le produit vaut $24x^2-7x-5$. Retrancher $-7x+4$ donne bien $24x^2-9$.

### Affirmation 3

> [!INDICATION]
> Écris les deux relations de divisibilité.

#### Solution

**Vrai.** Si $a=kb$ et $b=lc$ pour deux entiers $k,l$, alors $a/c=kl$, qui est entier.

### Affirmation 4

> [!INDICATION]
> Simplifie d’abord la fraction $3500/56$.

#### Solution

**Vrai.** $3500/56=62{,}5$, donc le nombre est $62{,}5\times10^{-19}=625/10^{20}$, qui a une écriture décimale finie.

### Affirmation 5

> [!INDICATION]
> Multiplie les coefficients des trois augmentations.

#### Solution

**Vrai.** $1{,}20^3=1{,}728$, soit une augmentation de 72,8 %.

## Exercice 5 — Parallélogrammes avec Scratch

### Question 1

> [!INDICATION]
> Deux angles consécutifs d’un parallélogramme sont supplémentaires.

#### Solution

$\alpha=180^\circ-30^\circ=150^\circ$.

### Question 2

> [!INDICATION]
> Le premier côté est horizontal et mesure 50 pas. Le changement de direction est l’angle extérieur.

#### Solution

Ordre **B, D, A, C**. Après B, on tourne à gauche de $30^\circ$ et on avance de 40 pas. En C, il faut tourner à gauche de $150^\circ$ pour prendre le côté horizontal suivant. La seconde répétition ferme le motif.

### Question 3

> [!INDICATION]
> Observe si chaque motif repart de l’origine ou d’un point déplacé.

#### Solution

Le **programme 1 donne la figure A** : le motif revient à son point initial et pivote de $30^\circ$ à chaque tour. Le **programme 2 donne la figure C** : les déplacements de 40 pas décalent successivement les points de départ, et le stylo trace ces déplacements.

## Bilan

Indique les unités, justifie les affirmations et garde les valeurs exactes jusqu’à l’arrondi final.
