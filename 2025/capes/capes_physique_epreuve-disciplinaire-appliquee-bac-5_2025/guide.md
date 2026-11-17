# CAPES Physique — Épreuve disciplinaire appliquée (bac+5) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve dure **5 heures**, est notée sur **20** (coefficient 2) et porte, à parts égales, sur la physique et la chimie, à travers un corpus de documents de classe (évaluations diagnostiques, activités expérimentales, copies d'élèves, extraits de programmes). Pour la session 2025, la moyenne du CAPES à l'EDA est de **10,38** (écart-type 3,56, note maximale 20, note minimale 2,17 ; CAFEP : moyenne 9,65).

Le sujet comporte **trois parties** et **45 questions** (chaque sous-question compte pour une) :

| Partie | Questions | Contenu | Notions mobilisées |
|---|---|---|---|
| 1 — Phénomènes d'ordre 1 | Q1 à Q5f (15 questions) | transformations nucléaires, modélisation Python de la décroissance radioactive, équation différentielle, datation au carbone 14, cinétique d'ordre 1 | décroissance radioactive, loi d'ordre 1, temps de demi-vie / demi-réaction, programmation Python, datation |
| 2 — Cristaux de soude | Q1a à Q6 (14 questions) | démarche scientifique, loi de Hess, premier principe, cahier de laboratoire, histoire des sciences, conceptions erronées, titrage pH-métrique, séquence STL | thermochimie, dissolution, incertitudes et z-score, titrage acido-basique d'une dibase |
| 3 — Réchauffement climatique | Q1a à Q5 (16 questions) | bilan radiatif et effet de serre, GES, montée des eaux, altimétrie satellitaire, mécanique du satellite, séquence enseignement scientifique | bilan radiatif, effet de serre, mouvement circulaire uniforme, référentiels, nature des savoirs scientifiques |

Deux questions d'**élaboration de séquence** (Q6 de la partie 2 et Q5 de la partie 3) « représentant un cinquième des points du barème de l’épreuve, soient abordées par un nombre insuffisant de candidats » (rapport du jury 2025, p. 16-17) : elles sont fortement discriminantes, il ne faut pas les négliger. Le jury signale par ailleurs « la présence de nombreuses fautes d'orthographe et de syntaxe dans les copies » (p. 16) : soigne la langue. Enfin, « les traces écrites sont très rarement proposées » à l'issue des séquences (p. 17) : prévoir explicitement celle de chaque séance.

**Questions à sécuriser d'abord** (forte réussite attendue) : Q1, Q2a-b, Q3a de la partie 1 ; Q1b, Q5a-b de la partie 2 ; Q4d-e-f de la partie 3. **Questions discriminantes** à investir ensuite : la situation problème (Q1a partie 2), le premier principe (Q1c partie 2), le z-score (Q1d partie 2), l'explication du bilan radiatif (Q2d partie 3), les expériences de montée des eaux (Q3a partie 3), la tâche complexe sur le chronomètre (Q4a partie 3) et les deux séquences.

**Gestion du temps** : environ 1 h 40 pour la partie 1, 1 h 50 pour la partie 2 (dont 25 min pour la séquence Q6), 1 h 30 pour la partie 3 (dont 25 min pour la séquence Q5), et le reste pour la relecture.

## Partie 1 — Étude de phénomènes d'ordre 1

Cette partie fait dialoguer physique nucléaire et cinétique chimique autour de l'analogie « phénomènes d'ordre 1 » : QCM diagnostique, modélisation par lancer de dés puis par programme Python, mise en équation, datation au carbone 14 (résolution de problème évaluée par compétences), puis suivi cinétique d'une transformation d'ordre 1. Outils : décroissance exponentielle, équation différentielle linéaire d'ordre 1, loi de Beer-Lambert pour le suivi spectrophotométrique.

### Q1. À propos des transformations nucléaires

> [!INDICATION]
> Relire les définitions du nombre de masse $A$, du numéro atomique $Z$ et du nombre de neutrons ; pour l'arsenic, $Z = 33$.

> [!INDICATION]
> Pour chaque proposition erronée, nommer la confusion mise en jeu (A/Z, atome/ion, population nulle ou non).

#### Solution

*Question 1 de l'évaluation diagnostique (document 1.1).* L'arsenic $^{72}$As possède **a) 72 nucléons** : 72 est le nombre de masse $A$, somme des protons et des neutrons.

- b) « 72 est le nombre de masse $A$ ; le nombre de neutrons vaut $N = A - Z = 72 - 33 = 39$. »
- c) « Le nombre de protons est le numéro atomique $Z$ ; pour l'arsenic $Z = 33$, lu dans la classification périodique. »

*Question 2.* Un atome radioactif est **c) instable** : un noyau radioactif se désintègre spontanément, c'est une transformation nucléaire spontanée.

- a) « Un noyau radioactif est par définition instable ; la stabilité caractérise les noyaux non radioactifs. »
- b) « Un atome est électriquement neutre ; la radioactivité est une propriété du noyau, elle ne charge pas l'atome (ne pas confondre atome et ion). »

*Question 3.* La population de noyaux radioactifs d'un échantillon **a) diminue au cours du temps** et **b) est divisée par 2 au bout d'une demi-vie**.

- c) « Après deux demi-vies il reste $N_0/4$ des noyaux : la décroissance est exponentielle, elle tend vers zéro sans jamais l'atteindre (limite asymptotique nulle). »

> [!JURY]
> Rapport 2025, p. 18 : « une désintégration radioactive constitue une transformation nucléaire spontanée », qualification que les candidats oublient de mentionner.

### Q2a. Questions 1, 4 et 6 de l'activité de modélisation (documents 1.2a et 1.2b)

> [!INDICATION]
> Question 1 : quels sont les deux caractères de la désintégration radioactive qu'un dé à six faces reproduit (aléa, probabilité constante) ?

> [!INDICATION]
> Question 4 : une seule ligne par étape — repérer dans le programme la commande aléatoire, l'ajout à la liste, le tracé.

> [!INDICATION]
> Question 6 : « nature différente » joue sur la probabilité de désintégration, « taille différente » sur le nombre initial de noyaux.

#### Solution

*Question 1.* Lancer un dé à six faces est un événement **aléatoire** : à chaque lancer, chaque dé a une probabilité **constante** $1/6$ de tomber sur la face « 1 », indépendante de son histoire passée et des autres dés. Cela modélise les deux caractères de la désintégration radioactive : le caractère aléatoire pour un noyau donné, et une probabilité de désintégration constante par unité de temps (absence de mémoire du noyau).

*Question 4* (numéros de lignes du programme du document 1.2b) :

- a. Caractère aléatoire de la désintégration : **ligne 10**, `valeurDe = random.randint(1, nbFaces)` (le test des lignes 11–12 en découle) ;
- b. Remplissage de la liste du nombre de dés restants : **ligne 20**, `historiqueNbDes.append(nbDes)` (liste initialisée à la ligne 16) ;
- c. Tracé de la courbe : **ligne 23**, `plt.plot([float(y) for y in historiqueNbDes])`, dans la fonction `affichageCourbe` définie ligne 22 et appelée ligne 31.

*Question 6.* Pour modéliser un échantillon de **nature différente** (autre noyau, donc autre probabilité de désintégration), on modifie `nbFaces` (**ligne 5**) : la probabilité de « succès » devient $1/\text{nbFaces}$. Pour un échantillon de **taille différente**, on modifie `nbDesDepart` (**ligne 4**), qui fixe le nombre initial de noyaux.

> [!JURY]
> Rapport 2025, p. 18 : « Il est essentiel de bien cibler la fonction spécifique de chaque commande. » Une réponse englobant trop de lignes est pénalisée.

### Q2b. Deux arguments en faveur du langage de programmation

> [!INDICATION]
> Penser effectif simulable (fluctuations statistiques) d'une part, reproductibilité et réglage des paramètres d'autre part.

#### Solution

1. **Effectif simulable** : le programme lance $10^5$ « noyaux », un nombre inaccessible au lancer manuel de dés ; les fluctuations statistiques relatives sont alors négligeables ($\sim 1/\sqrt{N}$) et la loi exponentielle apparaît nettement.
2. **Rapidité, reproductibilité et exploration** : la simulation se relance instantanément et les paramètres (`nbDesDepart`, `nbFaces`) se modifient en une ligne, ce qui permet de comparer plusieurs échantillons (nature et taille différentes) sans refaire l'expérience à la main.

### Q3a. Questions 1 et 2 de l'activité de modélisation mathématique (document 1.3a)

> [!INDICATION]
> Question 1 : le document 1 donne $\mathrm{d}N = -\lambda N(t)\,\mathrm{d}t$ ; passer à la dérivée.

> [!INDICATION]
> Question 2 : dériver la solution proposée et utiliser la condition initiale $N(0) = N_0$.

#### Solution

*Question 1.* Le document 1 donne $\mathrm{d}N = -\lambda\, N(t)\, \mathrm{d}t$, d'où l'équation différentielle vérifiée par $N(t)$ :

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = -\lambda\, N(t).
$$

*Question 2.* Posons $N(t) = N_0\, e^{-\lambda t}$. Alors

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = -\lambda\, N_0\, e^{-\lambda t} = -\lambda\, N(t),
$$

et $N(0) = N_0$ : la loi de décroissance radioactive du document 2 est bien l'unique solution de l'équation différentielle vérifiant la condition initiale. $\square$

### Q3b. Contenu des cases 1 à 6 du tableau d'analogie (document 1.3b)

> [!INDICATION]
> Compléter la colonne « loi de décroissance radioactive » du tableau en traduisant chaque ligne de la colonne « loi de vitesse d'ordre 1 » : même structure, autres grandeurs.

> [!INDICATION]
> Case 5 : résoudre $N(t_{1/2}) = N_0/2$ avec la loi de décroissance. Case 6 : décrire la courbe (décroissance, convexité, asymptote, point remarquable).

#### Solution

- **Case 1** (interprétation microscopique) : probabilité de désintégration d'un noyau par unité de temps ; la désintégration d'un noyau individuel est un événement aléatoire.
- **Case 2** (constante caractéristique) : la constante radioactive $\lambda$, homogène à l'inverse d'un temps.
- **Case 3** (équation différentielle) :

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = -\lambda\, N(t).
$$

- **Case 4** (évolution temporelle) :

$$
N(t) = N_0\, e^{-\lambda t}.
$$

- **Case 5** (grandeur temporelle associée) : le temps de demi-vie

$$
t_{1/2} = \frac{\ln 2}{\lambda},
$$

car $N(t_{1/2}) = N_0/2$.
- **Case 6** (allure) : décroissance exponentielle de $N_0$ à $t = 0$ vers une **limite asymptotique nulle** ; la courbe est décroissante, convexe, tangente en $t=0$ de pente $-\lambda N_0$, et passe par le point $(t_{1/2}, N_0/2)$.

> [!JURY]
> Rapport 2025, p. 18 : « Il convient de distinguer rigoureusement le « temps de demi-vie » utilisé dans le cadre d'une désintégration radioactive du « temps de demi-réaction » employé pour une transformation chimique. »

### Q4a. Principe de la datation au carbone 14

> [!INDICATION]
> Trois idées à enchaîner : production du $^{14}$C dans la haute atmosphère ; équilibre isotopique tant que l'organisme est vivant ; arrêt des échanges à la mort et mesure de l'activité.

> [!INDICATION]
> Conclure par la formule donnant la durée écoulée depuis la mort, et par la limite de validité de la méthode.

#### Solution

Le carbone 14 est produit en permanence dans la haute atmosphère par action du rayonnement cosmique sur l'azote :

$$
{}^{14}_{7}\mathrm{N} + {}^{1}_{0}\mathrm{n} \longrightarrow {}^{14}_{6}\mathrm{C} + {}^{1}_{1}\mathrm{p}.
$$

Le $^{14}$C, radioactif $\beta^-$ ($t_{1/2} = 5730$ ans), s'oxyde en CO$_2$ et est assimilé par les organismes vivants :
tant qu'un organisme est vivant, ses échanges avec l'atmosphère maintiennent son rapport $^{14}$C/$^{12}$C **constant**, égal à celui de l'atmosphère (équilibre isotopique).
À la mort de l'organisme, les échanges cessent : le $^{12}$C, stable, demeure tandis que la proportion de $^{14}$C **diminue** par désintégration radioactive.
La méthode consiste à **mesurer l'activité** $A(t) = \lambda N(t)$ de l'échantillon et à la comparer à l'activité $A_0$ d'un organisme actuel de référence, d'où la durée écoulée depuis la mort :

$$
t = \frac{t_{1/2}}{\ln 2}\,\ln\!\left(\frac{A_0}{A(t)}\right).
$$

La méthode est utilisable en pratique jusqu'à environ 50 000 ans (près d'une dizaine de demi-vies), au-delà desquelles l'activité résiduelle devient trop faible pour être mesurée fiablement.

> [!JURY]
> Rapport 2025, p. 18 : « peu de candidats ont évoqué la mesure de l'activité de l'échantillon comme préalable indispensable à la mise en œuvre de cette méthode », ainsi que « la notion d'équilibre isotopique » et le fait que la proportion en carbone 14 diminue à la mort de l'organisme par arrêt des échanges avec le milieu.

### Q4b. Correction de la résolution de problème (document 1.4a)

> [!INDICATION]
> Commencer par le sens physique de $N_0$ dans ce contexte et par l'hypothèse qui la relie au bois actuel ; en déduire le rapport $N(t)/N_0$.

> [!INDICATION]
> Isoler $t$ dans $N(t) = N_0 e^{-\ln(2)\, t / t_{1/2}}$, calculer, puis contrôler le signe et l'ordre de grandeur.

#### Solution

La loi de décroissance s'écrit, avec $\lambda = \ln 2 / t_{1/2}$ :

$$
N(t) = N_0\, e^{-\frac{\ln 2}{t_{1/2}}\,t}.
$$

**Sens physique de $N_0$** : c'est la quantité de $^{14}$C contenue dans le charbon de bois **à l'époque de l'occupation de la grotte**. **Hypothèse de datation** : cette quantité s'identifie à celle contenue dans un morceau de bois actuel de même masse, car le rapport $^{14}$C/$^{12}$C de l'atmosphère est supposé constant. L'énoncé donne $N_{\text{bois actuel}} = 1{,}5\, N_{\text{charbon}}$, donc :

$$
\frac{N(t)}{N_0} = \frac{1}{1{,}5}.
$$

En isolant $t$ :

$$
t = \frac{t_{1/2}}{\ln 2}\,\ln\!\left(\frac{N_0}{N(t)}\right) = \frac{t_{1/2}}{\ln 2}\,\ln(1{,}5).
$$

Application numérique :

$$
t = \frac{5730}{0{,}693} \times 0{,}405 \approx 3{,}4 \times 10^{3}\ \text{ans}.
$$

$$
\boxed{t \approx 3{,}4 \times 10^{3}\ \text{ans}}
$$

**Contrôle de vraisemblance** : la date est positive et de l'ordre de quelques milliers d'années, cohérent avec une occupation préhistorique de la grotte.

> [!PIEGE]
> Ne jamais conclure à une date négative sans réagir : c'est le signe d'une relation $N_0$/$N(t)$ inversée ou d'une origine des temps mal choisie.

> [!JURY]
> Rapport 2025, p. 19 : « le jury regrette que les candidats n'aient pas toujours explicité le sens physique de N₀, à savoir la quantité de carbone 14 présente dans le charbon à l'époque de l'occupation de la grotte », ce qui a entraîné des erreurs dans la relation entre $N_0$ et $N(t)$, et « certains candidats n'aient exercé aucun regard critique sur leurs résultats, notamment lorsqu'ils ont obtenu une date négative ».

### Q4c. Capacités ANALYSER / RAISONNER testées (document 1.4b)

> [!INDICATION]
> Relire chaque capacité de la compétence ANALYSER / RAISONNER du document 1.4b et la rattacher à une étape concrète de la résolution.

#### Solution

La résolution de problème mobilise, pour la compétence ANALYSER / RAISONNER :

- **formuler des hypothèses** : identifier $N_0$ à la teneur en $^{14}$C d'un bois actuel ;
- **proposer une stratégie de résolution** : relier les teneurs, la demi-vie et la durée écoulée ;
- **choisir un modèle ou des lois pertinentes** : la loi de décroissance radioactive ;
- **évaluer des ordres de grandeur** : contrôler le signe et l'ordre de grandeur de la date obtenue.

### Q4d. Reformulation en exercice guidé

> [!INDICATION]
> Quatre à cinq questions en verbes d'action, du rappel de cours au calcul final, en passant par le sens de $N_0$ et le contrôle du résultat.

#### Solution

1. Rappeler la loi de décroissance radioactive et exprimer $N(t)$ en fonction de $N_0$, $t$ et $t_{1/2}$.
2. Préciser le sens physique de $N_0$ dans ce contexte, formuler l'hypothèse qui la relie à un morceau de bois actuel, et en déduire la valeur de $N(t)/N_0$.
3. Exprimer la constante radioactive $\lambda$ en fonction de $t_{1/2}$.
4. Isoler $t$ dans l'expression de $N(t)$ et calculer la date d'occupation de la grotte.
5. Vérifier la vraisemblance du résultat (signe, ordre de grandeur).

> [!JURY]
> Rapport 2025, p. 19 : le jury « apprécie cependant l'effort réalisé par de nombreux candidats qui ont utilisé des verbes d'action dans leurs consignes », et déplore que les questions « omettent fréquemment d'interroger ces derniers sur le sens physique de N₀ ».

### Q5a. Association propositions ↔ courbes (document 1.5a)

> [!INDICATION]
> Décrire d'abord chaque courbe (valeur initiale, valeur finale, allure) avant d'associer.

> [!INDICATION]
> Une même courbe peut correspondre à deux propositions : réactif non totalement consommé (transformation limitée) et réactif en excès laissent tous deux un reste non nul.

#### Solution

Allures des courbes : courbe 1, décroissance de 1 vers 0 (limite asymptotique nulle) ; courbe 2, décroissance de 1 vers un plateau non nul (environ 0,2) ; courbe 3, croissance de 0 vers 1.

- **A** (concentration d'un produit) → **courbe 3** ;
- **B** (réactif limitant, transformation totale) → **courbe 1** ;
- **C** (réactif, transformation limitée) → **courbe 2** ;
- **D** (réactif en excès, transformation totale) → **courbe 2**.

$$
\boxed{\text{A-3, B-1, C-2, D-2}}
$$

> [!JURY]
> Rapport 2025, p. 19 : « la courbe 2 correspondait simultanément à deux propositions : C et D ».

### Q5b. Courbe analogue à la décroissance radioactive

> [!INDICATION]
> Chercher la courbe dont la limite à long terme est nulle ; justifier par la nature de la décroissance (exponentielle) et l'asymptote.

#### Solution

C'est la **courbe 1** : comme $N(t) = N_0 e^{-\lambda t}$, elle présente une **décroissance exponentielle** depuis sa valeur initiale vers une **limite asymptotique nulle** — un réactif limitant d'une transformation totale d'ordre 1 est entièrement consommé.

> [!JURY]
> Rapport 2025, p. 19 : le jury attendait une justification portant sur « la nature de la décroissance observée et l'existence d'une limite asymptotique nulle ».

### Q5c. Méthodes de suivi cinétique (document 1.5b)

> [!INDICATION]
> Pour chaque transformation, repérer la propriété physique modifiée (rotation optique, ions, gaz, couleur) et la mesure associée.

#### Solution

1. **Hydrolyse acide du saccharose** : les espèces sont optiquement actives → suivi **polarimétrique** (angle de rotation du plan de polarisation) ;
2. **Hydrolyse du chlorure de tertiobutyle** : apparition d'ions Cl⁻ et H₃O⁺ à partir d'espèces neutres → suivi **conductimétrique** ou **pH-métrique** ;
3. **Décomposition de l'eau oxygénée** : dégagement de O₂ gazeux → suivi **volumétrique** ou **manométrique** (pression) ; par prélèvements à intervalles réguliers suivis d'une trempe, un **titrage redox** suivi par potentiométrie ou colorimétrie est également possible ;
4. **Dégradation du bleu de méthylène** : espèce colorée → suivi **spectrophotométrique** (absorbance à la longueur d'onde d'absorption maximale).

> [!METHODE]
> Retenir le réflexe : apparition d'ions → conductimétrie/pH ; dégagement gazeux → volumétrie/manométrie ; espèce colorée → spectrophotométrie (loi de Beer-Lambert) ; espèce optiquement active → polarimétrie.

### Q5d. Transformations donnant une évolution analogue à la décroissance radioactive

> [!INDICATION]
> Deux critères à croiser : transformation totale, et grandeur mesurée directement proportionnelle à la concentration du réactif limitant.

> [!INDICATION]
> Parmi les quatre transformations, lesquelles ont un réactif limitant identifiable, et quelle grandeur mesurée lui est proportionnelle ?

#### Solution

Il faut une transformation **totale** (hypothèse du document 1.5b) dont la grandeur mesurée soit **directement proportionnelle à la concentration du réactif limitant**, pour obtenir une décroissance exponentielle vers zéro.

- **Transformation 4** : le bleu de méthylène est le réactif limitant (HO• est maintenu constant, donc ordre 1 apparent) et l'absorbance est proportionnelle à $[\text{BM}]$ (loi de Beer-Lambert) : **convient parfaitement** ;
- **Transformation 3** : en suivant $[\text{H}_2\text{O}_2]$, réactif limitant, par titrage redox : **convient également**.

### Q5e. Associations propositions ↔ compléments (document 1.5c)

> [!INDICATION]
> Pour chaque proposition d'élève, chercher dans quel cadre (totale, espèce limitante, espèce absente au départ) elle deviendrait correcte.

> [!INDICATION]
> Piège classique : associer la proposition 1 au complément A — ce n'est correct que si l'espèce est limitante.

#### Solution

$$
\boxed{1\text{-C},\quad 2\text{-B},\quad 3\text{-A}}
$$

- 1 (quantité initiale du réactif divisée par deux) → **C** : valable si et seulement si l'espèce est **limitante** ;
- 2 (concentration du produit à la moitié de sa valeur finale) → **B** : valable si l'espèce n'est **pas présente au début** de la réaction ;
- 3 (avancement volumique $x = x_{\max}/2$) → **A** : valable si et seulement si la transformation est **totale**.

> [!JURY]
> Rapport 2025, p. 20 : « Les paires 1-C, 2-B, 3-A constituaient les seules associations correctes » ; l'association 1-A est « parfois proposée à tort », car « même dans le cas d'une transformation totale, seule l'espèce réactive limitante voit sa quantité initiale divisée par deux au bout d'une durée égale au temps de demi-réaction ».

### Q5f. Définition du temps de demi-réaction

> [!INDICATION]
> Une définition valable aussi pour les transformations non totales : s'appuyer sur l'avancement à l'état final, pas sur $x_{\max}$.

#### Solution

**Le temps de demi-réaction $t_{1/2}$ est la durée au bout de laquelle l'avancement de la réaction atteint la moitié de sa valeur à l'état final** (avancement final $x_f$, et non avancement maximal) : $x(t_{1/2}) = x_f/2$. Cette définition couvre aussi bien les transformations totales que les transformations limitées.

> [!JURY]
> Rapport 2025, p. 20-21 : « La définition du temps de demi-réaction proposée par les candidats n'a pris que rarement en compte le cas des transformations non totales. »

## Partie 2 — Contrôle qualité de « véritables cristaux de soude »

Cette partie centre la chimie autour d'un contrôle qualité en terminale STL (PCM) : dissolution d'un solide ionique et effets thermiques (loi de Hess, premier principe, z-score), cahier de laboratoire, histoire du mot « soude », conceptions erronées des élèves sur la dissolution, titrage pH-métrique d'une dibase, puis élaboration d'une séquence de deux séances sur la thermodynamique chimique. Outils : thermochimie (enthalpies standard, loi de Hess, capacité thermique), constantes d'acidité, incertitudes et écart normalisé.

### Q1a. Étapes de la démarche scientifique (documents 2.1, 2.2 et 2.3)

> [!INDICATION]
> Lire le cahier de laboratoire rempli par l'élève (document 2.2) : quelle représentation initiale, quelles hypothèses, quelles investigations, et que révèle la mesure de température ?

> [!INDICATION]
> La situation problème naît d'une contradiction entre la prévision de l'hypothèse 1 et le résultat expérimental ; la démarche comporte alors une boucle rétroactive.

#### Solution

- **Représentation erronée de l'élève** : « les cristaux de soude, c'est la soude caustique NaOH » — le produit commercial est spontanément identifié à l'hydroxyde de sodium ;
- **Deux hypothèses formulées** : H1, les cristaux sont constitués de NaOH(s) (dissolution exothermique, la température devrait augmenter) ; H2, d'après le numéro CAS et une recherche documentaire, les cristaux sont du **carbonate de sodium décahydraté** Na₂CO₃,10H₂O(s) ;
- **Trois investigations scientifiques** : (i) mesure calorimétrique de la variation de température lors de la dissolution ; (ii) recherche documentaire à partir du numéro CAS ; (iii) calcul de l'enthalpie standard de dissolution par la loi de Hess et confrontation à la valeur expérimentale ;
- **Situation problème** : l'expérience révèle une **diminution** de température (dissolution endothermique), alors que l'hypothèse H1 prévoyait une augmentation (exothermique) : cette contradiction entre expérience et prévision constitue la situation problème, qui impose un **retour à l'étape de formulation d'hypothèses** — la démarche n'est pas linéaire mais comporte des boucles rétroactives.

> [!JURY]
> Rapport 2025, p. 21 : peu de candidats ont perçu que l'expérience « constituait précisément la situation problème nécessitant un retour à l'étape de formulation d'hypothèses », la démarche ayant été « appréhendée de façon linéaire », alors qu'elle impliquait des « boucles rétroactives caractéristiques de la démarche scientifique ».

### Q1b. Enthalpie standard de dissolution par la loi de Hess

> [!INDICATION]
> Écrire d'abord l'équation de dissolution de Na₂CO₃,10H₂O(s), puis appliquer la loi de Hess avec les enthalpies standard de formation tabulées.

> [!INDICATION]
> Attention aux coefficients stœchiométriques (2 Na⁺, 10 H₂O) et au signe de l'enthalpie du réactif.

#### Solution

Équation de dissolution :

$$
\mathrm{Na_2CO_3,10H_2O}(s) \longrightarrow 2\,\mathrm{Na^+}(aq) + \mathrm{CO_3^{2-}}(aq) + 10\,\mathrm{H_2O}(\ell).
$$

Loi de Hess :

$$
\Delta_{\mathrm{diss}}H^\circ = \Big[2\,\Delta_f H^\circ(\mathrm{Na^+}) + \Delta_f H^\circ(\mathrm{CO_3^{2-}}) + 10\,\Delta_f H^\circ(\mathrm{H_2O},\ell)\Big] - \Delta_f H^\circ(\mathrm{Na_2CO_3,10H_2O},s).
$$

Application numérique (valeurs en kJ·mol⁻¹) :

$$
\begin{aligned}
\Delta_{\mathrm{diss}}H^\circ &= \big[2(-240{,}1) + (-677{,}1) + 10(-285{,}8)\big] - (-4081{,}9) \\
&= (-480{,}2 - 677{,}1 - 2858{,}0) + 4081{,}9 \\
&= +66{,}6\ \mathrm{kJ \cdot mol^{-1}}.
\end{aligned}
$$

$$
\boxed{\Delta_{\mathrm{diss}}H^\circ(\mathrm{Na_2CO_3,10H_2O}) = +66{,}6\ \mathrm{kJ \cdot mol^{-1}}}
$$

La valeur est positive : la dissolution est **endothermique**, en accord avec le refroidissement observé.

> [!JURY]
> Rapport 2025, p. 21 : « Le jury se félicite que la loi de Hess soit bien maîtrisée par les candidats, qui ont fait preuve d'initiative en rédigeant l'équation de dissolution du solide ».

### Q1c. Expression de $\Delta_{\mathrm{diss}}H^\circ$ par le premier principe

> [!INDICATION]
> Définir le système et poser les hypothèses (fermé, au repos, isobare, adiabatique) avant tout calcul : $\Delta H = Q_p = 0$.

> [!INDICATION]
> Décomposer la transformation réelle en deux sous-étapes fictives de mêmes états initial et final : dissolution isotherme, puis variation de température.

#### Solution

**Système** : contenu du calorimètre (eau + cristaux + accessoires), **fermé** et **au repos**. **Hypothèses** : transformation **isobare** et **adiabatique**, le milieu liquide se comporte comme de l'eau pure. Pour une transformation isobare adiabatique, $\Delta H = Q_p = 0$.

On décompose la transformation réelle en deux sous-étapes fictives de même état initial et même état final :

- étape 1, dissolution **isotherme** à $T_i$ : $\Delta H_1 = n\,\Delta_{\mathrm{diss}}H^\circ$ avec $n = m_{\mathrm{cristaux}}/M_{\mathrm{cristaux}}$ ;
- étape 2, variation de température du système de $T_i$ à $T_f$ : $\Delta H_2 = (m_e\, c + C_{\mathrm{cal}})(T_f - T_i)$.

$H$ étant une fonction d'état, $\Delta H = \Delta H_1 + \Delta H_2 = 0$, d'où :

$$
\boxed{\Delta_{\mathrm{diss}}H^\circ = -\,\frac{(m_e\, c + C_{\mathrm{cal}})(T_f - T_i)\,M_{\mathrm{cristaux}}}{m_{\mathrm{cristaux}}}}
$$

C'est l'expression du document 2.1.

> [!PIEGE]
> Notations thermodynamiques : $H$ est une fonction d'état (on écrit $\Delta H$) ;
> $Q$ et $W$ sont des transferts d'énergie (on écrit $\delta Q$, $\delta W$).
> Les notations $\Delta Q$ et $\Delta W$ sont à proscrire.

> [!JURY]
> Rapport 2025, p. 21 : les hypothèses attendues sont « système calorimétrique fermé et au repos, transformation isobare et adiabatique » ; « Les notations ΔQ et ΔW, fréquemment utilisées par les candidats, sont donc à proscrire » ; la méthode attendue est de « modéliser la transformation en deux sous-étapes distinctes : l'étape de dissolution isotherme, puis l'étape de refroidissement après dissolution totale ».

### Q1d. Énoncé de la question 11 (compétence VALIDER)

> [!INDICATION]
> Enchaîner moyenne, écart-type, incertitude-type sur la moyenne, puis écart normalisé entre la moyenne de la classe et la valeur de référence ; conclure sur la nature des cristaux.

> [!INDICATION]
> Ne pas confondre écart relatif (hors programme) et z-score.

#### Solution

Proposition d'énoncé : « À partir de l'ensemble des valeurs expérimentales de $\Delta_{\mathrm{diss}}H^\circ$ obtenues par les groupes de la classe :

1. calculer la valeur moyenne $\bar{x}$ de la série ;
2. calculer l'écart-type expérimental $s$ de la série ;
3. en déduire l'incertitude-type sur la moyenne $u(\bar{x}) = s/\sqrt{N}$ ($N$ = nombre de mesures) ;
4. calculer le **z-score** (écart normalisé) entre la moyenne de la classe et la valeur de référence obtenue à la question 8 : $z = |\bar{x} - x_{\mathrm{r\acute{e}f}}| / u(\bar{x})$ ;
5. conclure : les deux valeurs sont compatibles si $|z| \le 2$ ; en déduire si l'hypothèse sur la nature des cristaux est validée. »

> [!JURY]
> Rapport 2025, p. 21-22 : « la compatibilité entre une valeur de référence et l’estimateur d’une série de valeurs mesurées expérimentalement s’évalue par le calcul d'un z-score (ou écart normalisé) » ; « certains candidats ont évoqué à tort le calcul d'un écart relatif ». Il était attendu que le candidat « invite l'élève à conclure sur la nature des cristaux, afin de conserver une trace écrite du raisonnement ».

### Q2a. Deux arguments justifiant l'intérêt du cahier de laboratoire

> [!INDICATION]
> L'intérêt doit être formulé **pour l'élève** (pas seulement pour le professeur) : traçabilité, reproductibilité, communication, structuration de la démarche.

#### Solution

1. **Traçabilité et communication** : le cahier consigne protocole, mesures et observations de façon à **reproduire l'expérience à l'identique** ultérieurement et à **communiquer ses résultats à un tiers** ; la tenue soignée et la lisibilité en sont la contrainte bénéfique ;
2. **Structuration de la démarche** : le remplissage régulier oblige l'élève à **formaliser les étapes de la démarche scientifique** (hypothèses, observations, interprétation), ce qui structure sa pensée — un intérêt renforcé dans la filière STL où la pratique expérimentale est centrale.

> [!JURY]
> Rapport 2025, p. 22 : « son utilisation présente un intérêt pour l'élève lui-même : contrainte à la tenue soignée et à la lisibilité, possibilité de reproduire l'expérience à l'identique ultérieurement (traçabilité), facilitation de la communication avec un tiers » ; le jury félicite les candidats qui ont souligné l'intérêt renforcé par le contexte STL.

### Q2b. Deux améliorations du modèle de cahier de laboratoire

> [!INDICATION]
> Penser « incertitudes et appareils » d'une part, « sécurité » d'autre part.

#### Solution

1. Ajouter une rubrique **incertitudes** : identification systématique des sources d'incertitudes à chaque manipulation, et relevé des résolutions ou tolérances des appareils de mesure et de la verrerie utilisés (indications des fabricants) ;
2. Ajouter une rubrique **sécurité** : pictogrammes, phrases de risque et de danger (mentions H et P) et conditions d'utilisation des espèces chimiques manipulées.

> [!JURY]
> Rapport 2025, p. 22 : ces améliorations « n'aient quasiment jamais été évoquées par les candidats » — les proposer est valorisé.

### Q3a. Origine du mot « soude » et usage abusif (document 2.4)

> [!INDICATION]
> Suivre le fil du texte : plantes maritimes salifères → cendres riches en carbonate de sodium → élargissements successifs du sens.

#### Solution

Le mot « soude » dérive du nom de **plantes maritimes salifères** (*Suaeda maritima*, *Salsola soda*, les salicornes) dont les **cendres** sont riches en carbonate de sodium : historiquement, la soude désigne ce que l'on note aujourd'hui Na₂CO₃. Par extensions successives, le mot a désigné toute **espèce chimique basique contenant l'élément sodium** (la potasse, basique mais sans atome de sodium, en est exclue), puis exclusivement l'hydroxyde de sodium sous le nom de « soude caustique ». L'emploi est **abusif** lorsque « soude » désigne NaOH (ou toute base) alors que, dans de nombreux produits d'usage courant, il renvoie toujours au **carbonate de sodium** — c'est le cas des « véritables cristaux de soude ».

> [!JURY]
> Rapport 2025, p. 22 : « le terme “soude” permet de dénommer toute espèce chimique basique contenant l'élément sodium » ; la « potasse » possède aussi des propriétés basiques mais ne contient pas d'atome de sodium, ce qui la distingue des « soudes » au sens de l'article.

### Q3b. Deux aspects de la construction des savoirs scientifiques (documents 2.4 et 2.5)

> [!INDICATION]
> Choisir deux caractéristiques du document 2.5 et les illustrer concrètement par le texte du document 2.4 (ne pas paraphraser sans justifier).

#### Solution

- **Le fonctionnement universel de la communauté scientifique** : les pratiques communes (nomenclature, symboles chimiques) transcendant les origines linguistiques — Na vient de *natrium*, K de *kalium* (de l'arabe *al-qali*, « les cendres ») — forment un **langage universel** qui garantit l'objectivité du savoir ; l'article en est une illustration concrète ;
- **L'évolution du savoir au cours du temps** : l'**extension sémantique** du mot « soude » — des cendres carbonatées aux espèces basiques sodées, puis à la soude caustique — illustre qu'un savoir évolue par continuité et glissements successifs, et non qu'il est fixé une fois pour toutes.

> [!PIEGE]
> Le jury déplore les réponses qui « se sont souvent contentées de paraphraser les informations sans justifier leurs propositions » (rapport 2025, p. 22) : chaque aspect doit être illustré dans le contexte de l'exercice.

### Q4a. Trois étapes de la dissolution de NaOH(s) et liaisons mises en jeu

> [!INDICATION]
> Penser « réseau ionique » : rupture du réseau, puis hydratation des ions, puis dispersion. Quelles interactions entre ions et molécules d'eau polaires ?

> [!INDICATION]
> Toutes les espèces ne forment pas des liaisons hydrogène : lequel des deux ions en est dépourvu côté donneur ?

#### Solution

1. **Dissociation du réseau ionique** : les ions Na⁺ et HO⁻ du cristal se séparent (rupture des liaisons ioniques du réseau, étape coûteuse en énergie : énergie réticulaire) ;
2. **Solvatation (hydratation)** : chaque ion est entouré d'un cortège de molécules d'eau orientées ;
3. **Dispersion** : les ions hydratés diffusent dans tout le volume de la solution.

Liaisons intermoléculaires soluté–solvant : interactions électrostatiques **ion–dipôle** entre les ions et les molécules d'eau polaires. L'ion HO⁻ peut en outre établir des **liaisons hydrogène** avec l'eau (donneur et accepteur) ; l'ion Na⁺, lui, **ne possède pas de site donneur de liaison hydrogène** et n'interagit avec l'eau que par ion–dipôle.

> [!JURY]
> Rapport 2025, p. 23 : les étapes de dissolution « sont rarement connues et nommées par les candidats », et « l'ion Na⁺ ne possède pas de site donneur de liaisons hydrogène, il ne peut donc pas interagir avec l'eau par ce type de liaison ».

### Q4b. Réponses correctes au questionnaire (document 2.6) et conceptions visées

> [!INDICATION]
> Répondre d'abord au questionnaire, puis généraliser : quelles conceptions erronées ces mauvaises réponses révèlent-elles ?

#### Solution

*Question 1* : item 1 → **a** (la fusion nécessite une augmentation de température) ; item 2 → **b** (la dissolution nécessite la présence d'un liquide, le solvant).

*Question 2* : réponses correctes **1** (la fusion est le passage de l'état solide à l'état liquide) et **4** (la dissolution est la disparition à l'échelle macroscopique d'un corps, le soluté, dans un liquide, le solvant) ; les propositions 2 et 3 sont fausses.

**Deux conceptions erronées** que le chercheur cherche à faire émerger :

- **l'assimilation de la dissolution à un changement d'état** (confusion dissolution / fusion : « une fois dissoute, l'espèce est devenue liquide ») ;
- **la croyance qu'il faut systématiquement chauffer pour dissoudre un solide**.

> [!JURY]
> Rapport 2025, p. 23 : les conceptions erronées ont souvent été proposées « sous forme de paraphrases des réponses au questionnaire, sans la généralisation attendue » ; le jury rappelle « la nécessité systématique de chauffer pour dissoudre un solide », « l'assimilation de la dissolution à un changement d'état », « la croyance qu'une fois dissoute, l'espèce chimique est devenue liquide ».

### Q4c. Trace écrite rectificative (intégrant « endothermique » et « exothermique »)

> [!INDICATION]
> Rectifier la conception « il faut chauffer pour dissoudre » : la dissolution peut être exothermique ou endothermique — et la fusion ?

#### Solution

Proposition de trace écrite : « La dissolution d'un solide dans l'eau peut être **exothermique** (elle cède de l'énergie au milieu : la température augmente) ou **endothermique** (elle prélève de l'énergie au milieu : la température diminue), selon le bilan entre énergie réticulaire et énergie d'hydratation. Contrairement à la **fusion, qui est toujours endothermique**, la dissolution ne nécessite donc pas forcément d'apport de chaleur : ainsi, la dissolution des cristaux de Na₂CO₃,10H₂O est endothermique et s'accompagne d'un refroidissement du milieu. »

> [!JURY]
> Rapport 2025, p. 23 : peu de candidats ont explicité « qu'une dissolution peut être exothermique ou endothermique, contrairement à une fusion qui est toujours endothermique. Cette distinction était pourtant essentielle pour établir le lien avec la conception erronée identifiée. »

### Q5a. Courbe de titrage du document 2.7

> [!INDICATION]
> Éliminer d'abord les courbes ascendantes ; parmi les courbes descendantes à deux sauts, comparer les pH aux demi-équivalences et à la première équivalence.

> [!INDICATION]
> À la première équivalence d'un titrage de dibase, la solution contient un amphotère : quel pH cela impose-t-il ?

#### Solution

La solution de Na₂CO₃ est une solution de **dibase** CO₃²⁻ titrée par un **acide fort** : on élimine les courbes ascendantes (B et D) et il faut une courbe **descendante à deux sauts de pH** (C ou E). Les deux sauts sont nets car les pKa de la dibase sont suffisamment éloignés ($pK_{a2} - pK_{a1} = 3{,}9$) et éloignés du $pK_a$ du titrant ($pK_a(\mathrm{H_3O^+/H_2O}) = 0$).

Pour lever l'indétermination entre C et E :

- à $V = V_{1,\mathrm{\'eq}}/2$ (tampon CO₃²⁻/HCO₃⁻) : $pH = pK_{a2} = 10{,}3$ ;
- à la première équivalence (solution d'**amphotère** HCO₃⁻) : $pH = (pK_{a1} + pK_{a2})/2 = 8{,}35$ ;
- à $V = (V_{1,\mathrm{\'eq}} + V_{2,\mathrm{\'eq}})/2$ (tampon HCO₃⁻/(CO₂,H₂O)) : $pH = pK_{a1} = 6{,}4$.

Ces valeurs (10,3 ; 8,35 ; 6,4) correspondent à la **courbe E**.

$$
\boxed{\text{courbe E}}
$$

> [!JURY]
> Rapport 2025, p. 23-24 : « L'analyse conduisait à la courbe E », et le jury apprécie la justification par l'amphotère : « à la première équivalence, la solution contient un amphotère, impliquant nécessairement pH(V1equiv) = (pKa₁ + pKa₂)/2 ».

### Q5b. Équations des réactions de titrage et constantes d'équilibre

> [!INDICATION]
> Le titrant d'un titrage acido-basique doit être un acide fort : écrire les deux réactions successives de CO₃²⁻ avec H₃O⁺ et exprimer leurs constantes à partir des $K_a$.

> [!INDICATION]
> $K_a$ est la constante de la réaction de l'acide sur l'eau ; les $K^\circ$ sont adimensionnelles (concentration standard $C^\circ$) et doivent être $\gg 1$ pour un titrage.

#### Solution

Le titrant est un **acide fort** (H₃O⁺), nécessaire pour que les réactions de titrage soient totales.

- Avant la première équivalence :

$$
\mathrm{CO_3^{2-}} + \mathrm{H_3O^+} \longrightarrow \mathrm{HCO_3^-} + \mathrm{H_2O},
$$

avec $K_1^\circ = \frac{1}{K_{a2}} = 10^{\,pK_{a2}} = 10^{10{,}3}$.
- Entre les deux équivalences :

$$
\mathrm{HCO_3^-} + \mathrm{H_3O^+} \longrightarrow (\mathrm{CO_2},\mathrm{H_2O}) + \mathrm{H_2O},
$$

avec $K_2^\circ = \frac{1}{K_{a1}} = 10^{\,pK_{a1}} = 10^{6{,}4}$.

Les constantes $K^\circ$ sont **adimensionnelles** : les expressions des constantes d'acidité font intervenir la concentration standard $C^\circ = 1\ \mathrm{mol \cdot L^{-1}}$. On a $K_1^\circ \gg 1$ et $K_2^\circ \gg 1$ : les deux réactions sont bien **totales**, ce qui justifie la forme des sauts de pH.

> [!JURY]
> Rapport 2025, p. 24 : « Le titrage de la dibase s'effectuait nécessairement avec un acide fort et non avec l'eau » ; « le Ka représente la constante d'équilibre associée à la réaction de l'acide faible sur l'eau » ; « les constantes d'équilibre K° constituent des grandeurs adimensionnelles, il convient donc de ne pas omettre la concentration standard C° dans les expressions littérales ».

### Q6. Élaboration de la séquence pédagogique (terminale STL, spécialité PCM — thermodynamique chimique)

> [!INDICATION]
> Cinq exigences à croiser : contextualisation + problématique avec retour en fin de séquence ; cohérence disciplinaire (quelle notion théorique s'introduit avant quelle loi ?) ; activités variées avec trace écrite ; évaluations précisées ; différenciation. Rester dans le programme de **terminale**.

#### Solution

**Contextualisation.** Les chaufferettes chimiques et les packs réfrigérants instantanés reposent sur la dissolution de sels ; plus largement, toute transformation chimique échange de l'énergie avec le milieu extérieur.

**Problématique.** « Comment prévoir et quantifier l'énergie thermique mise en jeu par une transformation chimique, et en déduire son caractère exothermique ou endothermique ? »

**Séance 1 (2 h) — Enthalpie de réaction et loi de Hess.**

- Notions introduites : enthalpie standard de formation $\Delta_f H^\circ$ (grandeur théorique tabulée, introduite **avant** la loi de Hess et jamais à l'issue d'une expérience), enthalpie standard de réaction $\Delta_r H^\circ$, loi de Hess, caractère exothermique / endothermique / athermique (signe de $\Delta_r H^\circ$).
- Activités : activité documentaire d'introduction des valeurs tabulées de $\Delta_f H^\circ$ ; exercices d'application de la loi de Hess $\Delta_r H^\circ = \sum_i \nu_i\, \Delta_f H^\circ_i$ avec interprétation du signe.
- Institutionnalisation : définitions de $\Delta_f H^\circ$ et $\Delta_r H^\circ$, énoncé de la loi de Hess, critère du signe.
- Trace écrite : les deux relations ci-dessus et le critère exo ($\Delta_r H^\circ < 0$) / endo ($\Delta_r H^\circ > 0$).
- Évaluations : diagnostique en début de séance (acquis de première sur les liaisons chimiques), formative sur un calcul de Hess.

**Séance 2 (2 h) — Mesurer un effet thermique : calorimétrie et capacité thermique.**

- Notions introduites : capacité thermique $C$ ; relation $\Delta H = C\,\Delta T$ pour une phase condensée ; bilan enthalpique dans un calorimètre.
- Activité expérimentale (différente de celle du document 2.1) : détermination calorimétrique de l'enthalpie de dissolution d'un sel ou de neutralisation d'un acide fort par une base forte, avec relevé des températures et des masses. Notions illustrées : capacité thermique, bilan enthalpique, caractère exothermique ou endothermique.
- Institutionnalisation : modèle du calorimètre (pertes négligées), relation $\Delta H = C\,\Delta T$, confrontation de la valeur mesurée à une valeur tabulée par un z-score.
- Trace écrite : protocole du bilan enthalpique et expression de $\Delta_r H^\circ$ expérimentale.
- Différenciation : fiches d'aide et énoncé guidé pour les élèves en difficulté ; résolution de problème ouverte pour les plus avancés.
- Évaluation : formative en séance, puis sommative (calcul d'enthalpie de réaction).
- **Retour à la problématique** en conclusion : la mesure calorimétrique confirme (ou infirme) la prévision faite par la loi de Hess.

> [!JURY]
> Rapport 2025, p. 24-25, éléments valorisés : « présence d'une contextualisation initiale et/ou d'une problématique avec retour vers celle-ci » ; cohérence disciplinaire — « l'enthalpie de formation, grandeur théorique, ne peut être introduite à l'issue d'une expérience » et « ne peut être présentée après la loi de Hess » ; « intégration d'expériences variées, particulièrement pertinente pour une séquence destinée à la filière STL » ; « formalisation des relations, concepts et définitions » (trace écrite) ; « prise en compte de la différenciation, organisation de la classe, gestion des groupes ». Le hors-sujet (traiter aussi le programme de première STL sur la dissolution) est sanctionné.
## Partie 3 — À propos du réchauffement climatique

Cette partie est consacrée au climat : bilan radiatif terrestre et effet de serre (évaluation diagnostique, expérience du verre, spectres d'absorption des GES, barème et copie d'élève), hausse du niveau marin (deux expériences de classe et leurs limites), observations satellitaires (tâche complexe sur le chronomètre, exercice de mécanique du satellite, erreurs d'une copie d'élève, référentiels), puis élaboration d'une séquence de deux séances en enseignement scientifique de terminale. Outils : bilan radiatif en puissances surfaciques, spectres de transmittance, cinématique du mouvement circulaire uniforme, deuxième loi de Newton avec forces d'inertie.

### Q1a. Besoins de remédiation (document 3.1a)

> [!INDICATION]
> Comparer, pour chaque item du QCM, le pourcentage de la réponse correcte aux autres ; une remédiation s'impose quand la réponse correcte est minoritaire.

> [!INDICATION]
> Pour les items problématiques, nommer le concept en jeu : absorption partielle de l'IR par l'atmosphère ; émission dans les deux directions.

#### Solution

Les réponses correctes sont les plus fréquentes à la question 1 (rayonnement de la Terre dans l'infrarouge, 48 %) et majoritaires à la question 4 (effet de serre = échange d'énergie dans l'infrarouge entre le sol et l'atmosphère, 54 %). En revanche, elles sont minoritaires aux questions 2 et 3, qui appellent une remédiation :

- **Question 2** : seuls 30 % des élèves savent que le rayonnement émis par la Terre est « en très grande partie absorbé par l'atmosphère » ; 55 % répondent « totalement absorbé ». Il faut travailler le fait que l'atmosphère est un **mélange de gaz** dont le comportement vis-à-vis du rayonnement infrarouge diffère, et que le pouvoir d'absorption n'est **pas de 100 %** ;
- **Question 3** : seuls 31 % savent que l'atmosphère émet « vers l'espace et vers la Terre » ; 50 % répondent « vers la Terre seulement ». Il faut travailler le caractère **isotrope** de la réémission du rayonnement IR par l'atmosphère.

> [!JURY]
> Rapport 2025, p. 25 : le besoin de remédiation porte sur « l'isotropie du modèle de la réémission du rayonnement IR par les gaz à effet de serre, modélisé par un rayonnement vers l'espace et un rayonnement vers la Terre » ; peu de candidats ont mentionné que le pouvoir d'absorption d'un GES n'est pas forcément de 100 %.

### Q1b. Question 2 de l'activité du document 3.1b

> [!INDICATION]
> Dans le tableau de l'activité, quel matériau est transparent au visible et opaque à l'infrarouge, comme l'atmosphère ?

#### Solution

Le **verre** interagit avec les rayonnements de manière identique à l'atmosphère terrestre : il est **transparent** au rayonnement **visible** (on voit la tasse à travers) et **opaque** au rayonnement **infrarouge**, qu'il **absorbe** en grande partie (on ne voit presque plus la tasse chaude à la caméra thermique lorsqu'une plaque de verre est interposée). Comme l'atmosphère, le verre laisse passer le rayonnement solaire visible et absorbe le rayonnement IR émis par la surface chaude.

> [!JURY]
> Rapport 2025, p. 25 : le jury félicite les candidats qui ont « correctement identifié le verre comme ayant un comportement identique à l'atmosphère vis-à-vis des rayonnements visible et IR ».

### Q2a. Corrigé des deux questions de l'activité « gaz à effet de serre » (document 3.2a)

> [!INDICATION]
> Question 1 : lire les spectres de transmittance — un GES se reconnaît à quoi, dans quel domaine spectral ?

> [!INDICATION]
> Question 2 : une corrélation ne suffit pas ; il faut un mécanisme physique (absorption de l'IR) plus le fait établi que les activités humaines produisent des GES.

#### Solution

*Question 1.* Un **gaz à effet de serre** est caractérisé par sa capacité à **absorber le rayonnement infrarouge** : sur son spectre de transmittance, il présente des **bandes d'absorption** (minimums de transmittance) dans le domaine IR (entre 2 µm et 16 µm environ). C'est le cas de CO₂, CH₄ et H₂O ; N₂ et O₂, qui transmettent environ 100 % du rayonnement IR, ne sont pas des gaz à effet de serre.

*Question 2.* Une simple **corrélation** entre activités humaines et réchauffement ne suffit pas à établir une **causalité**. Pour passer de la corrélation à la causalité, il faut une **explication scientifique d'ordre théorique** : les gaz à effet de serre absorbent le rayonnement IR émis par la surface de la Terre, de sorte qu'une augmentation de leur concentration entraîne une augmentation de température. Comme il est par ailleurs établi que les activités humaines produisent des GES (combustion de ressources fossiles, agriculture, déplacements), on peut conclure à un lien de causalité entre ces activités et le réchauffement observé.

> [!PIEGE]
> Ne pas confondre gaz à effet de serre et polluants, ni effet de serre et trou dans la couche d'ozone (rapport 2025, p. 25).

> [!JURY]
> Rapport 2025, p. 25 : « pour établir un lien de causalité entre la variation de la température de la Terre et la variation de la concentration en CO2 dans l’atmosphère, il faut disposer d’une explication scientifique d’ordre théorique ».

### Q2b. Barème détaillé de la question 1 (notée sur 2 points)

> [!INDICATION]
> Deux critères : la notion physique (absorption de l'IR) et la justification par lecture graphique.

#### Solution

- **1 point** : identifier qu'un gaz à effet de serre **absorbe le rayonnement infrarouge** ;
- **1 point** : justifier par une **lecture graphique** explicite — bandes d'absorption (minimums de transmittance) dans l'IR pour CO₂, CH₄ et H₂O, transmittance proche de 100 % pour N₂ et O₂.

> [!JURY]
> Rapport 2025, p. 25 : le jury a valorisé des « indicateurs de réussite cohérents (par exemple : identification du point commun entre les courbes, mention de l'infra-rouge, etc.) ».

### Q2c. Application du barème à la copie du document 3.2b

> [!INDICATION]
> Appliquer strictement les deux critères du barème à la réponse de l'élève, chiffrer, puis rédiger un commentaire qui explicite les leviers de progrès.

#### Solution

L'élève écrit : « Ce qui caractérise un gaz à effet de serre est sa capacité à absorber le rayonnement. En effet nous remarquons dans les graphiques un pic au niveau des diagrammes. »

- Critère 1 (absorption caractérisant un GES) : **acquis**, 1 point ;
- Critère 2 (lecture graphique) : **partiellement acquis** — l'élève parle d'« un pic » sans préciser qu'il s'agit d'un **minimum de transmittance** dans le domaine **infrarouge**, et sans comparer avec N₂ et O₂ : 0,5 point.

$$
\boxed{\text{Note : } 1{,}5/2}
$$

**Commentaire à visée formative** : « Tu as bien identifié que l'absorption caractérise un gaz à effet de serre. Pour progresser : précise que cette absorption a lieu dans l'**infrarouge** et qu'elle apparaît sur les spectres sous forme de **minimums de transmittance** (et non de pics) ; appuie-toi sur la comparaison avec N₂ et O₂, qui transmettent la quasi-totalité du rayonnement IR. »

> [!JURY]
> Rapport 2025, p. 26 : « le jury regrette le manque de pertinence et de précision des commentaires proposés à destination des élèves » ; il faut « expliciter les leviers à mobiliser pour progresser ».

### Q2d. Explication de la phrase sur la perturbation de l'équilibre radiatif

> [!INDICATION]
> Partir de l'équilibre radiatif du document 3.2c (puissances surfaciques en W·m⁻²), puis augmenter [GES] : que devient le flux IR réémis vers la Terre ?

> [!INDICATION]
> Nommer le déséquilibre (puissance reçue > puissance émise), le mécanisme d'absorption-réémission, et le devenir de l'énergie excédentaire.

#### Solution

À l'ère préindustrielle, le système Terre–atmosphère était en **équilibre radiatif** : la puissance surfacique reçue par la surface égale la puissance qu'elle émet (sur le schéma du document 3.2c : $171 + 220 = 391\ \mathrm{W \cdot m^{-2}}$ pour la surface). Lorsque la concentration en gaz à effet de serre augmente, l'atmosphère **absorbe davantage** le rayonnement IR émis par la surface (352 W·m⁻² sur le schéma) et en **réémet une plus grande part vers la Terre**. La surface reçoit alors une **puissance radiative additionnelle** : la puissance reçue devient **supérieure** à la puissance émise, ce qui constitue un **déséquilibre radiatif**. L'énergie excédentaire est essentiellement stockée par les océans, mais aussi par l'air et les sols, d'où l'augmentation de la température moyenne à la surface de la Terre. Schéma : Terre émettant un flux IR montant ; ce flux est partiellement absorbé par l'atmosphère, qui réémet vers l'espace et vers la Terre ; lorsque [GES] augmente, la flèche de réémission vers la Terre s'épaissit et le bilan $P_{\mathrm{re\c{c}ue}} > P_{\mathrm{\'emise}}$ n'est plus équilibré.

> [!JURY]
> Rapport 2025, p. 26 : « Cette question a été très peu traitée par les candidats » ; « la phase de réchauffement climatique en cours est due à un déséquilibre radiatif : la puissance surfacique reçue par la Terre est supérieure à celle qu'elle émet », par le « mécanisme d'absorption-réémission des IR par les gaz à effet de serre ».

### Q2e. Réponse à l'élève sur l'« scientifique dissident »

> [!INDICATION]
> S'appuyer sur le document 3.2d : la confiance s'ajuste à la qualité des preuves et à la fiabilité de la source ; mobiliser le caractère collectif de la construction des savoirs.

#### Solution

Proposition de réponse : « La confiance que l'on accorde à une information scientifique doit être **ajustée à la qualité des preuves** qui la soutiennent et à la **fiabilité de la source**. Or un savoir scientifique se construit **collectivement** : argumentation, niveau de preuve, reproductibilité des études, vérification par les pairs, débat. La parole d'**un seul** scientifique, même présenté comme un génie, n'a pas la même robustesse que le résultat d'un **consensus** établi à partir de milliers d'études expertisées — c'est ce que synthétise le rapport du GIEC. L'argument « l'histoire est pleine de scientifiques de génie qui n'étaient pas écoutés » ne change rien : ce qui fonde la confiance, ce n'est pas d'être minoritaire, c'est la solidité des preuves et la rigueur de la méthode. Il faut donc entendre les voix dissidentes, mais les évaluer à l'aune de leurs preuves, pas de leur seule parole. »

> [!JURY]
> Rapport 2025, p. 26 : il est important de préciser « le caractère collectif de la construction des savoirs scientifique : la parole d’un scientifique isolé n’a pas la même robustesse que le résultat d’un consensus (par exemple le rapport du GIEC) ».

### Q3a. Deux expériences illustrant les causes de la hausse du niveau marin (document 3.3)

> [!INDICATION]
> Deux causes à illustrer : dilatation thermique de l'eau de mer, fonte des glaces continentales. Pour chacune, imaginer un montage de laboratoire « parlant ».

> [!INDICATION]
> Pièges à éviter : un bécher ne convient pas pour la dilatation (effet non mesurable) ; des glaçons flottants ne font pas monter le niveau (glaces de mer ≠ glaces continentales).

#### Solution

Les deux principales causes sont la **dilatation thermique** de l'eau de mer et la **fonte des glaces continentales** (glaces posées sur les terres).

**Expérience 1 — dilatation thermique.** Matériel : ballon rempli d'eau colorée, surmonté d'un **tube capillaire de très faible diamètre** (bouchon percé), placé dans un **chauffe-ballon**, avec thermomètre. Observation attendue : en chauffant, l'eau se dilate et son niveau **monte nettement dans le tube fin**.

**Expérience 2 — fonte des glaces continentales.** Matériel : cristallisoir rempli d'eau, glaçons posés sur un **support émergé** (cale ou plateau au-dessus du niveau de l'eau). Observation attendue : en fondant, l'eau de fusion s'ajoute au liquide et le niveau **monte**. Expérience de contrôle : des glaçons **flottants** (qui modélisent les glaces de mer) ne modifient **pas** le niveau en fondant (poussée d'Archimède ; $\rho_{\mathrm{glace}} < \rho_{\mathrm{eau}}$).

> [!JURY]
> Rapport 2025, p. 26 : le jury attendait « une expérience où des glaçons soient initialement situés sur un support et donc émergés », car « l'expérience de la fonte d'un glaçon qui flotte dans l'eau ne conduit à aucune élévation du niveau d'eau initial » ; et « il est nécessaire d'utiliser un tube d'un très faible diamètre » car « l'effet de dilatation n'est pas mesurable dans un bécher ou dans une éprouvette ».

### Q3b. Limite de l'analogie laboratoire / montée des eaux mondiale

> [!INDICATION]
> Interroger les échelles de temps et d'espace de l'analogie, et les phénomènes non modélisés.

#### Solution

Les expériences de laboratoire sont **ponctuelles**, à **petite échelle spatiale et temporelle**, et isolent chaque cause : à l'échelle planétaire, les deux contributions se **cumulent** et interagissent avec d'autres phénomènes (variations de salinité, courants marins, apports fluviaux, inertie thermique des océans qui s'étale sur des décennies). L'analogie illustre les mécanismes, elle ne reproduit pas l'ampleur du phénomène global.

### Q4a. Corrigé de la tâche complexe sur l'altimétrie satellitaire (document 3.4a)

> [!INDICATION]
> Le chronomètre mesure un aller-retour de la lumière : une variation d'épaisseur $\Delta h$ correspond à $\Delta t = 2\Delta h/c$. Lire sur le graphe la plus petite variation annuelle d'épaisseur.

> [!INDICATION]
> La précision du chronomètre doit être au plus égale à la durée à résoudre ; comparer aux cinq précisions proposées.

#### Solution

Le chronomètre mesure la durée de l'**aller-retour** du signal lumineux entre le satellite et la surface : une variation d'épaisseur $\Delta h$ de la calotte correspond à une variation de durée

$$
\Delta t = \frac{2\,\Delta h}{c},
$$

avec $c = 3{,}0 \times 10^{8}\ \mathrm{m \cdot s^{-1}}$.

Lecture graphique (mission ICESat1, 2004–2008) : la plus petite variation d'épaisseur d'une année sur l'autre est $\Delta h \approx 0{,}15\ \mathrm{m}$ (entre 2006 et 2007). D'où :

$$
\Delta t = \frac{2 \times 0{,}15}{3{,}0 \times 10^{8}} = 1{,}0 \times 10^{-9}\ \mathrm{s},
$$

soit $\Delta t = 1\ \mathrm{ns}$.

Pour détecter une telle variation, la précision du chronomètre doit être au plus égale à 1 ns : conviennent les **chronomètres 3 (1 ns), 4 (0,1 ns) et 5 (0,01 ns)**.

$$
\boxed{\text{chronomètres 3, 4 et 5}}
$$

> [!PIEGE]
> Deux erreurs d'élèves très courantes : utiliser la vitesse du **son** au lieu de celle de la **lumière**, et oublier le facteur 2 de l'aller-retour.

> [!JURY]
> Rapport 2025, p. 27 : la compétence ANALYSER / RAISONNER était mobilisée pour « l'identification de la condition de précision du chronomètre et pour la prise en compte du phénomène d'aller-retour du signal » ; « plusieurs candidats aient traité la propagation du signal laser en s'appuyant sur la vitesse du son dans l'air, et [...] l'aller-retour du signal ait rarement été pris en compte dans le calcul final de Δt ».

### Q4b. Question et corrigé sur les interactions science / société (document 3.4b)

> [!INDICATION]
> Formuler une question portant sur une caractéristique du document 3.4b (par exemple : un savoir tributaire des avancées techniques), avec un corrigé court.

#### Solution

*Question proposée* : « En quoi les progrès des altimètres laser embarqués sur les satellites (de GLAS sur ICESat1 à ATLAS sur ICESat2) ont-ils fait progresser la connaissance de la fonte des glaces et du réchauffement climatique ? »

*Corrigé* : l'observation d'un phénomène **dépend de l'état des connaissances et des avancées techniques** de l'époque. Le passage d'ICESat1/GLAS (mesures annuelles, variations détectables de l'ordre de la dizaine de centimètres par an) à ICESat2/ATLAS (passages fréquents, variations détectables de l'ordre de 0,1 cm) a permis d'affiner considérablement la mesure de l'amincissement des calottes glaciaires. C'est une illustration de l'**interaction entre sciences et société** : un savoir est tributaire des moyens techniques disponibles pour l'observer.

> [!JURY]
> Rapport 2025, p. 27 : « cette question ait été très rarement abordée, car elle permet de mettre en exergue les enjeux épistémiques liés à la discipline » — des questions sur le lien entre avancées technologiques et connaissance des effets du réchauffement climatique pouvaient être formulées.

### Q4c. Deux erreurs de la copie du document 3.4d et commentaires formateurs

> [!INDICATION]
> Relire la copie de l'élève : quelle distance est notée « d » et que vaudrait-elle explicitement ? L'uniformité du mouvement est-elle démontrée ou seulement affirmée ?

#### Solution

- **Erreur 1 (notation)** : l'élève écrit la force gravitationnelle avec une distance notée « $d$ » sans la définir, alors que la distance pertinente est celle du satellite au **centre de la Terre**, $d = R_T + h$. *Origine* : paramétrage non explicité. *Commentaire formatif* : « Précise que $d = R_T + h$ ; définis explicitement chaque grandeur avant de l'utiliser dans un calcul. »
- **Erreur 2 (démonstration non aboutie)** : l'élève conclut que le mouvement est « circulaire uniforme » après avoir écrit l'accélération dans le repère de Frenet, sans avoir montré que sa composante **tangentielle** est nulle. *Origine* : confondre « écrire l'accélération » et « prouver l'uniformité ». *Commentaire formatif* : « La force est purement radiale ; projette la deuxième loi de Newton sur la tangente $\vec{u_t}$ pour établir $\mathrm{d}v/\mathrm{d}t = 0$, condition nécessaire de l'uniformité du mouvement. »

> [!JURY]
> Rapport 2025, p. 27 : erreurs relevées « liées soit à des problèmes de notation (“d” au lieu de “RT+h”, manque d’explicitation du bilan des forces, …) ou bien à des erreurs scientifiques (confusion entre expression du vecteur vitesse et ses coordonnées, démonstration non aboutie pour l’uniformité du mouvement circulaire, …) ».

### Q4d. Questions 3, 4 et 5 de l'exercice du document 3.4c

> [!INDICATION]
> Question 3 : appliquer la deuxième loi de Newton dans le référentiel géocentrique (galiléen) en projection sur la normale centripète, avec $R = R_T + h$.

> [!INDICATION]
> Question 4 : période $T = 2\pi R/v$, puis nombre d'orbites en 10 jours. Question 5 : la vitesse orbitale dépend-elle de la masse du satellite ?

#### Solution

*Question 3.* Dans le référentiel géocentrique supposé galiléen, la deuxième loi de Newton appliquée au satellite, dont la trajectoire est circulaire de rayon $R_T + h$, donne en projection sur la normale centripète :

$$
G\,\frac{m_s M_T}{(R_T + h)^2} = m_s\,\frac{v^2}{R_T + h},
$$

d'où

$$
\boxed{v = \sqrt{\frac{G M_T}{R_T + h}}}.
$$

Application numérique avec $R_T + h = 7{,}716 \times 10^{6}\ \mathrm{m}$ :

$$
v = \sqrt{\frac{6{,}67 \times 10^{-11} \times 5{,}97 \times 10^{24}}{7{,}716 \times 10^{6}}} \approx 7{,}18 \times 10^{3}\ \mathrm{m \cdot s^{-1}},
$$

soit $v \approx 2{,}59 \times 10^{4}\ \mathrm{km \cdot h^{-1}}$, en accord avec l'énoncé.

*Question 4.* Période de révolution :

$$
T = \frac{2\pi (R_T + h)}{v} \approx 6{,}75 \times 10^{3}\ \mathrm{s} \approx 112\ \mathrm{min}.
$$

Nombre d'orbites parcourues en 10 jours :

$$
n = \frac{10 \times 86400}{6{,}75 \times 10^{3}} \approx 1{,}28 \times 10^{2}.
$$

$$
\boxed{n \approx 128\ \text{orbites en 10 jours}}
$$

*Question 5.* L'expression $v = \sqrt{G M_T / (R_T + h)}$ ne dépend **pas de la masse du satellite** $m_s$ (qui se simplifie), mais seulement de l'altitude $h$. Topex-Poséidon étant placé à la **même altitude** (1336 km) que Jason-CS/Sentinel-6, sa vitesse orbitale est **identique**, malgré sa masse différente (2400 kg).

> [!PIEGE]
> Mécanique de base exigée : ne pas confondre lois de Newton et lois de Kepler, ni référentiel galiléen et référentiel géocentrique (rapport 2025, p. 27).

### Q4e. Référentiel galiléen

> [!INDICATION]
> Un référentiel galiléen est défini par la validité du principe d'inertie ; ne pas le confondre avec un simple repère.

#### Solution

Un **référentiel galiléen** est un référentiel dans lequel le **principe d'inertie** (première loi de Newton) est vérifié : tout point matériel isolé ou pseudo-isolé y est au repos ou animé d'un mouvement rectiligne uniforme. Un référentiel, c'est un solide de référence muni d'une horloge ; ce n'est pas un simple repère d'espace.

### Q4f. Référentiels non galiléens et deuxième loi de Newton

> [!INDICATION]
> Citer deux exemples concrets de référentiels non galiléens, puis écrire la deuxième loi de Newton dans un tel référentiel en faisant apparaître les forces d'inertie.

#### Solution

*Deux exemples* : le référentiel lié à un **véhicule en accélération ou en virage** ; le référentiel lié à un **manège en rotation** (le référentiel terrestre lui-même n'est pas strictement galiléen, du fait de la rotation de la Terre).

Dans un référentiel non galiléen $\mathcal{R}'$, la deuxième loi de Newton s'écrit :

$$
m\,\vec{a}(M/\mathcal{R}') = \sum \vec{F}_{\mathrm{ext}} + \vec{F}_{ie} + \vec{F}_{ic},
$$

avec :

- $\vec{a}(M/\mathcal{R}')$ : accélération du point $M$ dans $\mathcal{R}'$ ;
- $\sum \vec{F}_{\mathrm{ext}}$ : résultante des forces « réelles » exercées sur $M$ ;
- $\vec{F}_{ie} = -m\,\vec{a}_e$ : force d'inertie d'**entraînement**, où $\vec{a}_e$ est l'accélération d'entraînement de $\mathcal{R}'$ ;
- $\vec{F}_{ic} = -m\,\vec{a}_c = -2m\,\vec{\Omega} \wedge \vec{v}(M/\mathcal{R}')$ : force d'inertie de **Coriolis**, où $\vec{\Omega}$ est le vecteur rotation de $\mathcal{R}'$ par rapport à un référentiel galiléen.

> [!JURY]
> Rapport 2025, p. 27 : « La 2e loi de Newton intégrant l'accélération d'entrainement et l’accélération de Coriolis a été écrite de manière rigoureuse par les candidats qui ont traité cette question. »

### Q5. Élaboration de la séquence pédagogique (enseignement scientifique de terminale, thème « complexité du système climatique »)

> [!INDICATION]
> Problématiser réellement la séquence (ne pas proposer un simple « contexte global ») et prévoir le retour sur la problématique en fin de séquence ; adosser les objectifs aux trois objectifs généraux du programme (document 3.5).

> [!INDICATION]
> Pour chaque séance : type d'activité, contenu de l'institutionnalisation, trace écrite concrète, évaluations (type + contenu + modalités), et une caractéristique des savoirs scientifiques (document 3.4b).

#### Solution

**Contextualisation et problématique.** Depuis un siècle et demi, on mesure un réchauffement climatique global d'environ +1 °C et une montée du niveau marin d'environ 9 cm depuis 1995. Problématique : « En quoi les activités humaines perturbent-elles l'équilibre radiatif qui existait à l'ère préindustrielle, et quelles en sont les conséquences observables à l'échelle planétaire ? » — reprise explicitement en fin de séquence.

**Séance 1 (2 h) — Bilan radiatif et effet de serre.**

- Objectifs (adossés aux objectifs généraux A et B du programme, document 3.5) : comprendre le mécanisme d'absorption-réémission du rayonnement IR ; mettre en œuvre une démarche expérimentale.
- Activités : évaluation diagnostique (document 3.1a) faisant émerger les conceptions (isotropie de la réémission, absorption non totale) ; **activité expérimentale** (document 3.1b : matériaux interposés entre une tasse d'eau chaude et une caméra thermique) illustrant l'absorption de l'IR ; exploitation du modèle de bilan radiatif (document 3.2c). Notion illustrée : absorption du rayonnement IR par les gaz à effet de serre.
- Institutionnalisation : équilibre radiatif, déséquilibre radiatif dû à l'augmentation des GES, mécanisme d'absorption-réémission.
- Trace écrite : schéma annoté du bilan radiatif et phrase reliant [GES] ↑ → puissance reçue ↑ → réchauffement.
- Caractéristique des savoirs scientifiques abordée (document 3.4b) : la démarche scientifique construit des **modèles** qui expliquent les observations et permettent de prévoir.

**Séance 2 (2 h) — Gaz à effet de serre, indicateurs climatiques et esprit critique.**

- Objectifs (objectifs généraux B et C du programme) : analyser des données et des spectres ; identifier et comprendre les effets de la science sur les sociétés et l'environnement ; distinguer savoirs et croyances.
- Activités : activité documentaire sur les spectres de transmittance des GES (document 3.2a) ; exploitation de courbes d'indicateurs climatiques (teneur en CO₂, température moyenne, niveau marin — documents 3.3 et 3.4a) : lectures graphiques, pourcentages, moyennes, variations absolue et relative ; débat argumenté sur la fiabilité des sources (document 3.2d) à partir du cas du « scientifique dissident » et du consensus du GIEC.
- Institutionnalisation : définition d'un gaz à effet de serre ; passage d'une corrélation à une causalité grâce à une explication théorique ; caractère **collectif**, **réfutable** et évolutif des savoirs scientifiques (document 3.4b).
- Trace écrite : définition d'un GES, critères de fiabilité d'une source (qualité des preuves, fiabilité de la source, consensus).
- Évaluations : diagnostique en séance 1 ; formative en séance 2 (lecture graphique) ; sommative en fin de séquence (production argumentée sur un indicateur climatique, avec contenu et modalités précisés).
- Professionnalisme : différenciation (documents de niveaux variés), organisation de la classe en îlots pour le débat, gestion des groupes — importante dans l'enseignement scientifique où les profils des élèves sont très variés.

> [!JURY]
> Rapport 2025, p. 27-28 : « les candidats se sont souvent contentés d’une proposition de contexte très global, sans problématiser la séquence » ; « Le retour sur la problématique et/ou le contexte a été très rarement observés dans les copies » ; les objectifs doivent être reliés aux trois objectifs généraux du programme (comprendre la nature du savoir scientifique et ses méthodes d'élaboration ; identifier et mettre en œuvre des pratiques scientifiques ; identifier et comprendre les effets de la science sur les sociétés et sur l'environnement) ; le jury attend « des exemples concrets de traces écrites », des évaluations avec « contenu et modalités », et valorise « la prise en compte de la différenciation, les détails concernant l'organisation de la classe, la gestion des groupes ».

## Bilan

**Méthodes à retenir.**

- Phénomènes d'ordre 1 : de l'aléa microscopique à la loi macroscopique — équation différentielle $\mathrm{d}N/\mathrm{d}t = -\lambda N$, solution exponentielle, temps de demi-vie/demi-réaction $t_{1/2} = \ln 2/\text{constante}$ ; l'analogie tableau (document 1.3b) est l'outil de transfert entre radioactivité et cinétique chimique.
- Thermochimie : écrire l'équation de dissolution avant d'appliquer la loi de Hess ; pour le premier principe, définir le système et les hypothèses, puis décomposer en sous-étapes isotherme + thermique ; comparer une mesure à une référence par un **z-score**, jamais par un écart relatif.
- Titrage d'une dibase : courbe descendante à deux sauts ; lever l'indétermination par les pH aux demi-équivalences ($pK_{a2}$, $pK_{a1}$) et à la première équivalence (amphotère, $(pK_{a1}+pK_{a2})/2$).
- Mécanique : mouvement circulaire uniforme dans le référentiel géocentrique, $v = \sqrt{GM_T/(R_T+h)}$ indépendante de la masse ; altimétrie = aller-retour de la lumière, $\Delta t = 2\Delta h/c$.
- Didactique : une séquence réussie articule contextualisation, problématique **avec retour**, activités variées, traces écrites explicites, évaluations détaillées et différenciation — les deux questions de séquence pèsent un cinquième du barème.

**Prérequis à revoir.** Décroissance exponentielle et équation différentielle d'ordre 1 ; loi de Hess et premier principe (notations $\Delta H$ vs $\delta Q$) ; constantes d'acidité et titrages ; incertitudes (écart-type, incertitude-type, z-score) ; mouvement circulaire uniforme et référentiels galiléen/non galiléen ; bilan radiatif et effet de serre.

**Questions classiques transposables.** La datation au carbone 14 (Q4 partie 1) est un grand classique de résolution de problème évaluée par compétences ; le choix d'une courbe de titrage par les pH caractéristiques (Q5 partie 2) se transpose à tout titrage acido-basique ; la tâche complexe sur le chronomètre (Q4a partie 3) illustre la démarche expérimentale évaluée (ANALYSER / RÉALISER / VALIDER) ; les expériences de montée des eaux (Q3a partie 3) demandent de distinguer glaces de mer et glaces continentales.
