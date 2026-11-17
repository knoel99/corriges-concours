# CAPES Physique — Épreuve disciplinaire appliquée (bac+5) 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 5 heures, notée sur 20 (coefficient 2), en trois parties : phénomènes d'ordre 1 (décroissance radioactive et cinétique chimique), contrôle qualité des « cristaux de soude » (thermochimie, dissolution, titrage acido-basique) et réchauffement climatique (bilan radiatif, effet de serre, montée des eaux, observations satellitaires). Les 45 questions (sous-questions comptées chacune pour une) sont traitées ci-dessous dans la numérotation du sujet.

## Partie 1 — Étude de phénomènes d'ordre 1

### Q1. À propos des transformations nucléaires

*Question 1 de l'évaluation diagnostique (document 1.1).* L'arsenic $^{72}$As possède **a) 72 nucléons** : 72 est le nombre de masse $A$, somme des protons et des neutrons.

- b) « 72 est le nombre de masse $A$ ; le nombre de neutrons vaut $N = A - Z = 72 - 33 = 39$. »
- c) « Le nombre de protons est le numéro atomique $Z$ ; pour l'arsenic $Z = 33$, lu dans la classification périodique. »

*Question 2.* Un atome radioactif est **c) instable** : un noyau radioactif se désintègre spontanément, c'est une transformation nucléaire spontanée.

- a) « Un noyau radioactif est par définition instable ; la stabilité caractérise les noyaux non radioactifs. »
- b) « Un atome est électriquement neutre ; la radioactivité est une propriété du noyau, elle ne charge pas l'atome (ne pas confondre atome et ion). »

*Question 3.* La population de noyaux radioactifs d'un échantillon **a) diminue au cours du temps** et **b) est divisée par 2 au bout d'une demi-vie**.

- c) « Après deux demi-vies il reste $N_0/4$ des noyaux : la décroissance est exponentielle, elle tend vers zéro sans jamais l'atteindre (limite asymptotique nulle). »

### Q2a. Questions 1, 4 et 6 de l'activité de modélisation (documents 1.2a et 1.2b)

*Question 1.* Lancer un dé à six faces est un événement **aléatoire** : à chaque lancer, chaque dé a une probabilité **constante** $1/6$ de tomber sur la face « 1 », indépendante de son histoire passée et des autres dés. Cela modélise les deux caractères de la désintégration radioactive : le caractère aléatoire pour un noyau donné, et une probabilité de désintégration constante par unité de temps (absence de mémoire du noyau).

*Question 4* (les numéros de lignes sont ceux du programme du document 1.2b) :

- a. Caractère aléatoire de la désintégration : **ligne 10**, `valeurDe = random.randint(1, nbFaces)` (le test des lignes 11–12 en découle) ;
- b. Remplissage de la liste du nombre de dés restants : **ligne 20**, `historiqueNbDes.append(nbDes)` (liste initialisée à la ligne 16) ;
- c. Tracé de la courbe : **ligne 23**, `plt.plot([float(y) for y in historiqueNbDes])`, dans la fonction `affichageCourbe` définie ligne 22 et appelée ligne 31.

*Question 6.* Pour modéliser un échantillon de **nature différente** (autre noyau, donc autre probabilité de désintégration), on modifie `nbFaces` (**ligne 5**) : la probabilité de « succès » devient $1/\text{nbFaces}$. Pour un échantillon de **taille différente**, on modifie `nbDesDepart` (**ligne 4**), qui fixe le nombre initial de noyaux.

### Q2b. Deux arguments en faveur du langage de programmation

1. **Effectif simulable** : le programme lance $10^5$ « noyaux », un nombre inaccessible au lancer manuel de dés ; les fluctuations statistiques relatives sont alors négligeables ($\sim 1/\sqrt{N}$) et la loi exponentielle apparaît nettement.
2. **Rapidité, reproductibilité et exploration** : la simulation se relance instantanément et les paramètres (`nbDesDepart`, `nbFaces`) se modifient en une ligne, ce qui permet de comparer plusieurs échantillons (nature et taille différentes) sans refaire l'expérience à la main.

### Q3a. Questions 1 et 2 de l'activité de modélisation mathématique (document 1.3a)

*Question 1.* Le document 1 donne $\mathrm{d}N = -\lambda\, N(t)\, \mathrm{d}t$, d'où l'équation différentielle vérifiée par $N(t)$ :

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = -\lambda\, N(t).
$$

*Question 2.* Posons $N(t) = N_0\, e^{-\lambda t}$. Alors

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = -\lambda\, N_0\, e^{-\lambda t} = -\lambda\, N(t),
$$

et $N(0) = N_0$ : la loi de décroissance radioactive du document 2 est bien l'unique solution de l'équation différentielle vérifiant la condition initiale. $\square$

### Q3b. Contenu des cases 1 à 6 du tableau d'analogie (document 1.3b, colonne « loi de décroissance radioactive »)

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

### Q4a. Principe de la datation au carbone 14 (une demi-page au maximum)

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

### Q4b. Correction de la résolution de problème (document 1.4a)

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

### Q4c. Capacités ANALYSER / RAISONNER testées (document 1.4b)

La résolution de problème mobilise, pour la compétence ANALYSER / RAISONNER :

- **formuler des hypothèses** : identifier $N_0$ à la teneur en $^{14}$C d'un bois actuel ;
- **proposer une stratégie de résolution** : relier les teneurs, la demi-vie et la durée écoulée ;
- **choisir un modèle ou des lois pertinentes** : la loi de décroissance radioactive ;
- **évaluer des ordres de grandeur** : contrôler le signe et l'ordre de grandeur de la date obtenue.

### Q4d. Reformulation en exercice guidé (cinq questions)

1. Rappeler la loi de décroissance radioactive et exprimer $N(t)$ en fonction de $N_0$, $t$ et $t_{1/2}$.
2. Préciser le sens physique de $N_0$ dans ce contexte, formuler l'hypothèse qui la relie à un morceau de bois actuel, et en déduire la valeur de $N(t)/N_0$.
3. Exprimer la constante radioactive $\lambda$ en fonction de $t_{1/2}$.
4. Isoler $t$ dans l'expression de $N(t)$ et calculer la date d'occupation de la grotte.
5. Vérifier la vraisemblance du résultat (signe, ordre de grandeur).

### Q5a. Association propositions ↔ courbes (document 1.5a)

Allures des courbes : courbe 1, décroissance de 1 vers 0 (limite asymptotique nulle) ; courbe 2, décroissance de 1 vers un plateau non nul (environ 0,2) ; courbe 3, croissance de 0 vers 1.

- **A** (concentration d'un produit) → **courbe 3** ;
- **B** (réactif limitant, transformation totale) → **courbe 1** ;
- **C** (réactif, transformation limitée) → **courbe 2** ;
- **D** (réactif en excès, transformation totale) → **courbe 2**.

$$
\boxed{\text{A-3, B-1, C-2, D-2}}
$$

La courbe 2 correspond simultanément aux propositions C et D : dans les deux cas, il reste du réactif à l'état final.

### Q5b. Courbe analogue à la décroissance radioactive

C'est la **courbe 1** : comme $N(t) = N_0 e^{-\lambda t}$, elle présente une **décroissance exponentielle** depuis sa valeur initiale vers une **limite asymptotique nulle** — un réactif limitant d'une transformation totale d'ordre 1 est entièrement consommé.

### Q5c. Méthodes de suivi cinétique (document 1.5b)

1. **Hydrolyse acide du saccharose** : les espèces sont optiquement actives → suivi **polarimétrique** (angle de rotation du plan de polarisation) ;
2. **Hydrolyse du chlorure de tertiobutyle** : apparition d'ions Cl⁻ et H₃O⁺ à partir d'espèces neutres → suivi **conductimétrique** ou **pH-métrique** ;
3. **Décomposition de l'eau oxygénée** : dégagement de O₂ gazeux → suivi **volumétrique** ou **manométrique** (pression) ; par prélèvements à intervalles réguliers suivis d'une trempe, un **titrage redox** suivi par potentiométrie ou colorimétrie est également possible ;
4. **Dégradation du bleu de méthylène** : espèce colorée → suivi **spectrophotométrique** (absorbance à la longueur d'onde d'absorption maximale).

### Q5d. Transformations donnant une évolution analogue à la décroissance radioactive

Il faut une transformation **totale** (hypothèse du document 1.5b) dont la grandeur mesurée soit **directement proportionnelle à la concentration du réactif limitant**, pour obtenir une décroissance exponentielle vers zéro.

- **Transformation 4** : le bleu de méthylène est le réactif limitant (HO• est maintenu constant, donc ordre 1 apparent) et l'absorbance est proportionnelle à $[\text{BM}]$ (loi de Beer-Lambert) : **convient parfaitement** ;
- **Transformation 3** : en suivant $[\text{H}_2\text{O}_2]$, réactif limitant, par titrage redox : **convient également**.

### Q5e. Associations propositions ↔ compléments (document 1.5c)

$$
\boxed{1\text{-C},\quad 2\text{-B},\quad 3\text{-A}}
$$

- 1 (quantité initiale du réactif divisée par deux) → **C** : valable si et seulement si l'espèce est **limitante** (même pour une transformation totale, seule l'espèce limitante voit sa quantité divisée par deux à $t_{1/2}$) ;
- 2 (concentration du produit à la moitié de sa valeur finale) → **B** : valable si l'espèce n'est **pas présente au début** de la réaction ;
- 3 (avancement volumique $x = x_{\max}/2$) → **A** : valable si et seulement si la transformation est **totale** ($x_{\max} = x_{\text{final}}$).

### Q5f. Définition du temps de demi-réaction

**Le temps de demi-réaction $t_{1/2}$ est la durée au bout de laquelle l'avancement de la réaction atteint la moitié de sa valeur à l'état final** (avancement final $x_f$, et non avancement maximal) : $x(t_{1/2}) = x_f/2$. Cette définition couvre aussi bien les transformations totales que les transformations limitées.

## Partie 2 — Contrôle qualité de « véritables cristaux de soude »

### Q1a. Étapes de la démarche scientifique (documents 2.1, 2.2 et 2.3)

- **Représentation erronée de l'élève** : « les cristaux de soude, c'est la soude caustique NaOH » — le produit commercial est spontanément identifié à l'hydroxyde de sodium ;
- **Deux hypothèses formulées** : H1, les cristaux sont constitués de NaOH(s) (dissolution exothermique, la température devrait augmenter) ; H2, d'après le numéro CAS et une recherche documentaire, les cristaux sont du **carbonate de sodium décahydraté** Na₂CO₃,10H₂O(s) ;
- **Trois investigations scientifiques** : (i) mesure calorimétrique de la variation de température lors de la dissolution ; (ii) recherche documentaire à partir du numéro CAS ; (iii) calcul de l'enthalpie standard de dissolution par la loi de Hess et confrontation à la valeur expérimentale ;
- **Situation problème** : l'expérience révèle une **diminution** de température (dissolution endothermique), alors que l'hypothèse H1 prévoyait une augmentation (exothermique) : cette contradiction entre expérience et prévision constitue la situation problème, qui impose un **retour à l'étape de formulation d'hypothèses** — la démarche n'est pas linéaire mais comporte des boucles rétroactives.

### Q1b. Enthalpie standard de dissolution par la loi de Hess

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

### Q1c. Expression de $\Delta_{\mathrm{diss}}H^\circ$ par le premier principe

**Système** : contenu du calorimètre (eau + cristaux + accessoires), **fermé** et **au repos**. **Hypothèses** : transformation **isobare** et **adiabatique**, le milieu liquide se comporte comme de l'eau pure. Pour une transformation isobare adiabatique, $\Delta H = Q_p = 0$.

On décompose la transformation réelle en deux sous-étapes fictives de même état initial et même état final :

- étape 1, dissolution **isotherme** à $T_i$ : $\Delta H_1 = n\,\Delta_{\mathrm{diss}}H^\circ$ avec $n = m_{\mathrm{cristaux}}/M_{\mathrm{cristaux}}$ ;
- étape 2, variation de température du système de $T_i$ à $T_f$ : $\Delta H_2 = (m_e\, c + C_{\mathrm{cal}})(T_f - T_i)$.

$H$ étant une fonction d'état, $\Delta H = \Delta H_1 + \Delta H_2 = 0$, d'où :

$$
\boxed{\Delta_{\mathrm{diss}}H^\circ = -\,\frac{(m_e\, c + C_{\mathrm{cal}})(T_f - T_i)\,M_{\mathrm{cristaux}}}{m_{\mathrm{cristaux}}}}
$$

C'est l'expression du document 2.1. Notations : $H$ est une fonction d'état, on écrit $\Delta H$ ;
$Q$ et $W$ sont des transferts d'énergie, on écrit $\delta Q$ et $\delta W$ —
les notations $\Delta Q$ et $\Delta W$ sont à proscrire.

### Q1d. Énoncé de la question 11 (compétence VALIDER)

Proposition d'énoncé : « À partir de l'ensemble des valeurs expérimentales de $\Delta_{\mathrm{diss}}H^\circ$ obtenues par les groupes de la classe :

1. calculer la valeur moyenne $\bar{x}$ de la série ;
2. calculer l'écart-type expérimental $s$ de la série ;
3. en déduire l'incertitude-type sur la moyenne $u(\bar{x}) = s/\sqrt{N}$ ($N$ = nombre de mesures) ;
4. calculer le **z-score** (écart normalisé) entre la moyenne de la classe et la valeur de référence obtenue à la question 8 : $z = |\bar{x} - x_{\mathrm{r\acute{e}f}}| / u(\bar{x})$ ;
5. conclure : les deux valeurs sont compatibles si $|z| \le 2$ ; en déduire si l'hypothèse sur la nature des cristaux est validée. »

### Q2a. Deux arguments justifiant l'intérêt du cahier de laboratoire

1. **Traçabilité et communication** : le cahier consigne protocole, mesures et observations de façon à **reproduire l'expérience à l'identique** ultérieurement et à **communiquer ses résultats à un tiers** ; la tenue soignée et la lisibilité en sont la contrainte bénéfique ;
2. **Structuration de la démarche** : le remplissage régulier oblige l'élève à **formaliser les étapes de la démarche scientifique** (hypothèses, observations, interprétation), ce qui structure sa pensée — un intérêt renforcé dans la filière STL où la pratique expérimentale est centrale.

### Q2b. Deux améliorations du modèle de cahier de laboratoire (document 2.2)

1. Ajouter une rubrique **incertitudes** : identification systématique des sources d'incertitudes à chaque manipulation, et relevé des résolutions ou tolérances des appareils de mesure et de la verrerie utilisés (indications des fabricants) ;
2. Ajouter une rubrique **sécurité** : pictogrammes, phrases de risque et de danger (mentions H et P) et conditions d'utilisation des espèces chimiques manipulées.

### Q3a. Origine du mot « soude » et usage abusif (document 2.4)

Le mot « soude » dérive du nom de **plantes maritimes salifères** (*Suaeda maritima*, *Salsola soda*, les salicornes) dont les **cendres** sont riches en carbonate de sodium : historiquement, la soude désigne ce que l'on note aujourd'hui Na₂CO₃. Par extensions successives, le mot a désigné toute **espèce chimique basique contenant l'élément sodium** (la potasse, basique mais sans atome de sodium, en est exclue), puis exclusivement l'hydroxyde de sodium sous le nom de « soude caustique ». L'emploi est **abusif** lorsque « soude » désigne NaOH (ou toute base) alors que, dans de nombreux produits d'usage courant, il renvoie toujours au **carbonate de sodium** — c'est le cas des « véritables cristaux de soude ».

### Q3b. Deux aspects de la construction des savoirs scientifiques (documents 2.4 et 2.5)

- **Le fonctionnement universel de la communauté scientifique** : les pratiques communes (nomenclature, symboles chimiques) transcendant les origines linguistiques — Na vient de *natrium*, K de *kalium* (de l'arabe *al-qali*, « les cendres ») — forment un **langage universel** qui garantit l'objectivité du savoir ; l'article en est une illustration concrète ;
- **L'évolution du savoir au cours du temps** : l'**extension sémantique** du mot « soude » — des cendres carbonatées aux espèces basiques sodées, puis à la soude caustique — illustre qu'un savoir évolue par continuité et glissements successifs, et non qu'il est fixé une fois pour toutes.

### Q4a. Trois étapes de la dissolution de NaOH(s) et liaisons mises en jeu

1. **Dissociation du réseau ionique** : les ions Na⁺ et HO⁻ du cristal se séparent (rupture des liaisons ioniques du réseau, étape coûteuse en énergie : énergie réticulaire) ;
2. **Solvatation (hydratation)** : chaque ion est entouré d'un cortège de molécules d'eau orientées ;
3. **Dispersion** : les ions hydratés diffusent dans tout le volume de la solution.

Liaisons intermoléculaires soluté–solvant : interactions électrostatiques **ion–dipôle** entre les ions et les molécules d'eau polaires. L'ion HO⁻ peut en outre établir des **liaisons hydrogène** avec l'eau (donneur et accepteur) ; l'ion Na⁺, lui, **ne possède pas de site donneur de liaison hydrogène** et n'interagit avec l'eau que par ion–dipôle.

### Q4b. Réponses correctes au questionnaire (document 2.6) et conceptions visées

*Question 1* : item 1 → **a** (la fusion nécessite une augmentation de température) ; item 2 → **b** (la dissolution nécessite la présence d'un liquide, le solvant).

*Question 2* : réponses correctes **1** (la fusion est le passage de l'état solide à l'état liquide) et **4** (la dissolution est la disparition à l'échelle macroscopique d'un corps, le soluté, dans un liquide, le solvant) ; les propositions 2 et 3 sont fausses.

**Deux conceptions erronées** que le chercheur cherche à faire émerger :

- **l'assimilation de la dissolution à un changement d'état** (confusion dissolution / fusion : « une fois dissoute, l'espèce est devenue liquide ») ;
- **la croyance qu'il faut systématiquement chauffer pour dissoudre un solide**.

### Q4c. Trace écrite rectificative (intégrant « endothermique » et « exothermique »)

Proposition de trace écrite : « La dissolution d'un solide dans l'eau peut être **exothermique** (elle cède de l'énergie au milieu : la température augmente) ou **endothermique** (elle prélève de l'énergie au milieu : la température diminue), selon le bilan entre énergie réticulaire et énergie d'hydratation. Contrairement à la **fusion, qui est toujours endothermique**, la dissolution ne nécessite donc pas forcément d'apport de chaleur : ainsi, la dissolution des cristaux de Na₂CO₃,10H₂O est endothermique et s'accompagne d'un refroidissement du milieu. »

### Q5a. Courbe de titrage du document 2.7

La solution de Na₂CO₃ est une solution de **dibase** CO₃²⁻ titrée par un **acide fort** : on élimine les courbes ascendantes (B et D, titrage d'un acide par une base) et il faut une courbe **descendante à deux sauts de pH** (C ou E). Les deux sauts sont nets car les pKa de la dibase sont suffisamment éloignés ($pK_{a2} - pK_{a1} = 10{,}3 - 6{,}4 = 3{,}9$) et éloignés du $pK_a$ du titrant ($pK_a(\mathrm{H_3O^+/H_2O}) = 0$).

Pour lever l'indétermination entre C et E, on examine les pH caractéristiques :

- à $V = V_{1,\mathrm{\'eq}}/2$ (tampon CO₃²⁻/HCO₃⁻) : $pH = pK_{a2} = 10{,}3$ ;
- à la première équivalence (solution d'**amphotère** HCO₃⁻) : $pH = (pK_{a1} + pK_{a2})/2 = (6{,}4 + 10{,}3)/2 = 8{,}35$ ;
- à $V = (V_{1,\mathrm{\'eq}} + V_{2,\mathrm{\'eq}})/2$ (tampon HCO₃⁻/(CO₂,H₂O)) : $pH = pK_{a1} = 6{,}4$.

Ces valeurs (10,3 ; 8,35 ; 6,4) correspondent à la **courbe E**.

$$
\boxed{\text{courbe E}}
$$

### Q5b. Équations des réactions de titrage et constantes d'équilibre

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

### Q6. Élaboration de la séquence pédagogique (terminale STL, spécialité PCM — thermodynamique chimique)

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

## Partie 3 — À propos du réchauffement climatique

### Q1a. Besoins de remédiation (document 3.1a)

Les réponses correctes sont les plus fréquentes à la question 1 (rayonnement de la Terre dans l'infrarouge, 48 %) et majoritaires à la question 4 (effet de serre = échange d'énergie dans l'infrarouge entre le sol et l'atmosphère, 54 %). En revanche, elles sont minoritaires aux questions 2 et 3, qui appellent une remédiation :

- **Question 2** : seuls 30 % des élèves savent que le rayonnement émis par la Terre est « en très grande partie absorbé par l'atmosphère » ; 55 % répondent « totalement absorbé ». Il faut travailler le fait que l'atmosphère est un **mélange de gaz** dont le comportement vis-à-vis du rayonnement infrarouge diffère, et que le pouvoir d'absorption n'est **pas de 100 %** ;
- **Question 3** : seuls 31 % savent que l'atmosphère émet « vers l'espace et vers la Terre » ; 50 % répondent « vers la Terre seulement ». Il faut travailler le caractère **isotrope** de la réémission du rayonnement IR par l'atmosphère (rayonnement vers l'espace **et** vers la Terre).

### Q1b. Question 2 de l'activité du document 3.1b

Le **verre** interagit avec les rayonnements de manière identique à l'atmosphère terrestre : il est **transparent** au rayonnement **visible** (on voit la tasse à travers) et **opaque** au rayonnement **infrarouge**, qu'il **absorbe** en grande partie (on ne voit presque plus la tasse chaude à la caméra thermique lorsqu'une plaque de verre est interposée). Comme l'atmosphère, le verre laisse passer le rayonnement solaire visible et absorbe le rayonnement IR émis par la surface chaude.

### Q2a. Corrigé des deux questions de l'activité « gaz à effet de serre » (document 3.2a)

*Question 1.* Un **gaz à effet de serre** est caractérisé par sa capacité à **absorber le rayonnement infrarouge** : sur son spectre de transmittance, il présente des **bandes d'absorption** (minimums de transmittance) dans le domaine IR (entre 2 µm et 16 µm environ). C'est le cas de CO₂, CH₄ et H₂O ; N₂ et O₂, qui transmettent environ 100 % du rayonnement IR, ne sont pas des gaz à effet de serre.

*Question 2.* Une simple **corrélation** entre activités humaines et réchauffement ne suffit pas à établir une **causalité**. Pour passer de la corrélation à la causalité, il faut une **explication scientifique d'ordre théorique** : les gaz à effet de serre absorbent le rayonnement IR émis par la surface de la Terre, de sorte qu'une augmentation de leur concentration entraîne une augmentation de température. Comme il est par ailleurs établi que les activités humaines produisent des GES (combustion de ressources fossiles, agriculture, déplacements), on peut conclure à un lien de causalité entre ces activités et le réchauffement observé.

### Q2b. Barème détaillé de la question 1 (notée sur 2 points)

- **1 point** : identifier qu'un gaz à effet de serre **absorbe le rayonnement infrarouge** ;
- **1 point** : justifier par une **lecture graphique** explicite — bandes d'absorption (minimums de transmittance) dans l'IR pour CO₂, CH₄ et H₂O, transmittance proche de 100 % pour N₂ et O₂.

### Q2c. Application du barème à la copie du document 3.2b

L'élève écrit : « Ce qui caractérise un gaz à effet de serre est sa capacité à absorber le rayonnement. En effet nous remarquons dans les graphiques un pic au niveau des diagrammes. »

- Critère 1 (absorption caractérisant un GES) : **acquis**, 1 point ;
- Critère 2 (lecture graphique) : **partiellement acquis** — l'élève parle d'« un pic » sans préciser qu'il s'agit d'un **minimum de transmittance** dans le domaine **infrarouge**, et sans comparer avec N₂ et O₂ (transmittance ≈ 100 %, gaz non absorbants) : 0,5 point.

$$
\boxed{\text{Note : } 1{,}5/2}
$$

**Commentaire à visée formative** : « Tu as bien identifié que l'absorption caractérise un gaz à effet de serre. Pour progresser : précise que cette absorption a lieu dans l'**infrarouge** et qu'elle apparaît sur les spectres sous forme de **minimums de transmittance** (et non de pics) ; appuie-toi sur la comparaison avec N₂ et O₂, qui transmettent la quasi-totalité du rayonnement IR. »

### Q2d. Explication de la phrase sur la perturbation de l'équilibre radiatif (documents 3.2a, 3.2c et 3.2d)

À l'ère préindustrielle, le système Terre–atmosphère était en **équilibre radiatif** : la puissance surfacique reçue par la surface égale la puissance qu'elle émet (sur le schéma du document 3.2c : $171 + 220 = 391\ \mathrm{W \cdot m^{-2}}$ pour la surface). Lorsque la concentration en gaz à effet de serre augmente, l'atmosphère **absorbe davantage** le rayonnement IR émis par la surface (352 W·m⁻² sur le schéma) et en **réémet une plus grande part vers la Terre**. La surface reçoit alors une **puissance radiative additionnelle** : la puissance reçue devient **supérieure** à la puissance émise, ce qui constitue un **déséquilibre radiatif**. L'énergie excédentaire est essentiellement stockée par les océans, mais aussi par l'air et les sols, d'où l'augmentation de la température moyenne à la surface de la Terre. Schéma : Terre émettant un flux IR montant ; ce flux est partiellement absorbé par l'atmosphère, qui réémet vers l'espace et vers la Terre ; lorsque [GES] augmente, la flèche de réémission vers la Terre s'épaissit et le bilan $P_{\mathrm{re\c{c}ue}} > P_{\mathrm{\'emise}}$ n'est plus équilibré.

### Q2e. Réponse à l'élève sur l'« scientifique dissident » (document 3.2d)

Proposition de réponse : « La confiance que l'on accorde à une information scientifique doit être **ajustée à la qualité des preuves** qui la soutiennent et à la **fiabilité de la source**. Or un savoir scientifique se construit **collectivement** : argumentation, niveau de preuve, reproductibilité des études, vérification par les pairs, débat. La parole d'**un seul** scientifique, même présenté comme un génie, n'a pas la même robustesse que le résultat d'un **consensus** établi à partir de milliers d'études expertisées — c'est ce que synthétise le rapport du GIEC. L'argument « l'histoire est pleine de scientifiques de génie qui n'étaient pas écoutés » ne change rien : ce qui fonde la confiance, ce n'est pas d'être minoritaire, c'est la solidité des preuves et la rigueur de la méthode. Il faut donc entendre les voix dissidentes, mais les évaluer à l'aune de leurs preuves, pas de leur seule parole. »

### Q3a. Deux expériences illustrant les causes de la hausse du niveau marin (document 3.3)

Les deux principales causes sont la **dilatation thermique** de l'eau de mer et la **fonte des glaces continentales** (glaces posées sur les terres).

**Expérience 1 — dilatation thermique.** Matériel : ballon rempli d'eau colorée, surmonté d'un **tube capillaire de très faible diamètre** (bouchon percé), placé dans un **chauffe-ballon**, avec thermomètre. Observation attendue : en chauffant, l'eau se dilate et son niveau **monte nettement dans le tube fin**. (L'effet n'est pas mesurable dans un bécher ou une éprouvette : d'où le tube de très faible diamètre.)

**Expérience 2 — fonte des glaces continentales.** Matériel : cristallisoir rempli d'eau, glaçons posés sur un **support émergé** (cale ou plateau au-dessus du niveau de l'eau). Observation attendue : en fondant, l'eau de fusion s'ajoute au liquide et le niveau **monte**. Expérience de contrôle : des glaçons **flottants** (qui modélisent les glaces de mer) ne modifient **pas** le niveau en fondant, car la poussée d'Archimède compense exactement (la masse volumique de la glace est inférieure à celle de l'eau liquide).

### Q3b. Limite de l'analogie laboratoire / montée des eaux mondiale

Les expériences de laboratoire sont **ponctuelles**, à **petite échelle spatiale et temporelle**, et isolent chaque cause : à l'échelle planétaire, les deux contributions se **cumulent** et interagissent avec d'autres phénomènes (variations de salinité, courants marins, apports fluviaux, inertie thermique des océans qui s'étale sur des décennies). L'analogie illustre les mécanismes, elle ne reproduit pas l'ampleur du phénomène global.

### Q4a. Corrigé de la tâche complexe sur l'altimétrie satellitaire (document 3.4a)

Le chronomètre mesure la durée de l'**aller-retour** du signal lumineux entre le satellite et la surface : une variation d'épaisseur $\Delta h$ de la calotte correspond à une variation de durée

$$
\Delta t = \frac{2\,\Delta h}{c},
$$

avec $c = 3{,}0 \times 10^{8}\ \mathrm{m \cdot s^{-1}}$ (vitesse de la **lumière**, pas du son ; d'où le facteur 2 de l'aller-retour).

Lecture graphique (mission ICESat1, 2004–2008) : la plus petite variation d'épaisseur d'une année sur l'autre est $\Delta h \approx 0{,}15\ \mathrm{m}$ (entre 2006 et 2007). D'où :

$$
\Delta t = \frac{2 \times 0{,}15}{3{,}0 \times 10^{8}} = 1{,}0 \times 10^{-9}\ \mathrm{s},
$$

soit $\Delta t = 1\ \mathrm{ns}$.

Pour détecter une telle variation, la précision du chronomètre doit être au plus égale à 1 ns : conviennent les **chronomètres 3 (1 ns), 4 (0,1 ns) et 5 (0,01 ns)**.

$$
\boxed{\text{chronomètres 3, 4 et 5}}
$$

### Q4b. Question et corrigé sur les interactions science / société (document 3.4b)

*Question proposée* : « En quoi les progrès des altimètres laser embarqués sur les satellites (de GLAS sur ICESat1 à ATLAS sur ICESat2) ont-ils fait progresser la connaissance de la fonte des glaces et du réchauffement climatique ? »

*Corrigé* : l'observation d'un phénomène **dépend de l'état des connaissances et des avancées techniques** de l'époque. Le passage d'ICESat1/GLAS (mesures annuelles, variations détectables de l'ordre de la dizaine de centimètres par an) à ICESat2/ATLAS (passages fréquents, variations détectables de l'ordre de 0,1 cm) a permis d'affiner considérablement la mesure de l'amincissement des calottes glaciaires. C'est une illustration de l'**interaction entre sciences et société** : un savoir est tributaire des moyens techniques disponibles pour l'observer.

### Q4c. Deux erreurs de la copie du document 3.4d et commentaires formateurs

- **Erreur 1 (notation)** : l'élève écrit la force gravitationnelle avec une distance notée « $d$ » sans la définir, alors que la distance pertinente est celle du satellite au **centre de la Terre**, $d = R_T + h$. *Origine* : paramétrage non explicité. *Commentaire formatif* : « Précise que $d = R_T + h$ ; définis explicitement chaque grandeur avant de l'utiliser dans un calcul. »
- **Erreur 2 (démonstration non aboutie)** : l'élève conclut que le mouvement est « circulaire uniforme » après avoir écrit l'accélération dans le repère de Frenet, sans avoir montré que sa composante **tangentielle** est nulle. *Origine* : confondre « écrire l'accélération » et « prouver l'uniformité ». *Commentaire formatif* : « La force est purement radiale ; projette la deuxième loi de Newton sur la tangente $\vec{u_t}$ pour établir $\mathrm{d}v/\mathrm{d}t = 0$, condition nécessaire de l'uniformité du mouvement. »

### Q4d. Questions 3, 4 et 5 de l'exercice du document 3.4c

*Question 3.* Dans le référentiel géocentrique supposé galiléen, la deuxième loi de Newton appliquée au satellite, dont la trajectoire est circulaire de rayon $R_T + h$, donne en projection sur la normale centripète :

$$
G\,\frac{m_s M_T}{(R_T + h)^2} = m_s\,\frac{v^2}{R_T + h},
$$

d'où

$$
\boxed{v = \sqrt{\frac{G M_T}{R_T + h}}}.
$$

Application numérique avec $R_T + h = (6{,}38 \times 10^{3} + 1336)\ \mathrm{km} = 7{,}716 \times 10^{6}\ \mathrm{m}$ :

$$
v = \sqrt{\frac{6{,}67 \times 10^{-11} \times 5{,}97 \times 10^{24}}{7{,}716 \times 10^{6}}} \approx 7{,}18 \times 10^{3}\ \mathrm{m \cdot s^{-1}},
$$

soit $v \approx 2{,}59 \times 10^{4}\ \mathrm{km \cdot h^{-1}}$, en accord avec l'énoncé.

*Question 4.* Période de révolution :

$$
T = \frac{2\pi (R_T + h)}{v} = \frac{2\pi \times 7{,}716 \times 10^{6}}{7{,}18 \times 10^{3}} \approx 6{,}75 \times 10^{3}\ \mathrm{s} \approx 112\ \mathrm{min}.
$$

Nombre d'orbites parcourues en 10 jours :

$$
n = \frac{10 \times 86400}{6{,}75 \times 10^{3}} \approx 1{,}28 \times 10^{2}.
$$

$$
\boxed{n \approx 128\ \text{orbites en 10 jours}}
$$

*Question 5.* L'expression $v = \sqrt{G M_T / (R_T + h)}$ ne dépend **pas de la masse du satellite** $m_s$ (qui se simplifie), mais seulement de l'altitude $h$. Topex-Poséidon étant placé à la **même altitude** (1336 km) que Jason-CS/Sentinel-6, sa vitesse orbitale est **identique**, malgré sa masse différente (2400 kg).

### Q4e. Référentiel galiléen

Un **référentiel galiléen** est un référentiel dans lequel le **principe d'inertie** (première loi de Newton) est vérifié : tout point matériel isolé ou pseudo-isolé y est au repos ou animé d'un mouvement rectiligne uniforme. Un référentiel, c'est un solide de référence muni d'une horloge ; ce n'est pas un simple repère d'espace.

### Q4f. Référentiels non galiléens et deuxième loi de Newton

*Deux exemples* : le référentiel lié à un **véhicule en accélération ou en virage** ; le référentiel lié à un **manège en rotation** (le référentiel terrestre lui-même n'est pas strictement galiléen, du fait de la rotation de la Terre).

Dans un référentiel non galiléen $\mathcal{R}'$, la deuxième loi de Newton s'écrit :

$$
m\,\vec{a}(M/\mathcal{R}') = \sum \vec{F}_{\mathrm{ext}} + \vec{F}_{ie} + \vec{F}_{ic},
$$

avec :

- $\vec{a}(M/\mathcal{R}')$ : accélération du point $M$ dans $\mathcal{R}'$ ;
- $\sum \vec{F}_{\mathrm{ext}}$ : résultante des forces « réelles » exercées sur $M$ ;
- $\vec{F}_{ie} = -m\,\vec{a}_e$ : force d'inertie d'**entraînement**, où $\vec{a}_e$ est l'accélération d'entraînement de $\mathcal{R}'$ ;
- $\vec{F}_{ic} = -m\,\vec{a}_c = -2m\,\vec{\Omega} \wedge \vec{v}(M/\mathcal{R}')$ : force d'inertie de **Coriolis**, où $\vec{\Omega}$ est le vecteur rotation de $\mathcal{R}'$ par rapport à un référentiel galiléen et $\vec{v}(M/\mathcal{R}')$ la vitesse de $M$ dans $\mathcal{R}'$.

### Q5. Élaboration de la séquence pédagogique (enseignement scientifique de terminale, thème « complexité du système climatique »)

**Contextualisation et problématique.** Depuis un siècle et demi, on mesure un réchauffement climatique global d'environ +1 °C et une montée du niveau marin d'environ 9 cm depuis 1995. Problématique : « En quoi les activités humaines perturbent-elles l'équilibre radiatif qui existait à l'ère préindustrielle, et quelles en sont les conséquences observables à l'échelle planétaire ? » — reprise explicitement en fin de séquence.

**Séance 1 (2 h) — Bilan radiatif et effet de serre.**

- Objectifs (adossés aux objectifs généraux A et B du programme, document 3.5) : comprendre le mécanisme d'absorption-réémission du rayonnement IR ; mettre en œuvre une démarche expérimentale.
- Activités : évaluation diagnostique (document 3.1a) faisant émerger les conceptions (isotropie de la réémission, absorption non totale) ; **activité expérimentale** (document 3.1b : matériaux interposés entre une tasse d'eau chaude et une caméra thermique) illustrant l'absorption de l'IR ; exploitation du modèle de bilan radiatif (document 3.2c, puissances surfaciques en W·m⁻²). Notion illustrée : absorption du rayonnement IR par les gaz à effet de serre.
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
