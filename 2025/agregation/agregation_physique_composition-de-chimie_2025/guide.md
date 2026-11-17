# Agrégation Physique — Composition de chimie 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Format.** Composition de chimie, concours externe d’agrégation, section physique-chimie, option physique, session 2025 : durée 5 heures, calculatrice autorisée, tout ouvrage et document rigoureusement interdit. Le sujet (« Les chimistes font leur cinéma ») comporte quatre parties indépendantes et 63 questions au total, de difficulté croissante au sein de chaque partie ; les données D1 à D13 et une annexe (courbes courant–potentiel de la sous-partie B, à compléter et rendre) sont fournies avec l’énoncé.

**Thèmes mobilisés.** Chimie des solutions aqueuses et spectrophotométrie UV-visible (dosage de l’ozone, Q1–7), thermodynamique chimique (équilibres de la foudre, températures d’inversion, Q8–14), thermochimie d’une réaction explosive et premier principe (Q15–24), électrochimie et corrosion (courbes courant–potentiel, Q25–32), cinétique chimique appliquée à un polymère (Q33–38), chimie organique et stéréochimie (synthèse de l’adrénaline, Q39–53), structure de la matière, spectroscopies et qubits (complexes de cuivre(II), Q54–63).

**Ce que dit le rapport 2025** (rapport sur la composition de chimie, p. 18-27) : moyenne de l’épreuve **7,4/20** pour les candidats ayant composé, **11,1/20** pour les admissibles. « Toutes les questions ont ainsi été abordées au moins une fois et le jury a eu la satisfaction de lire un nombre important de réponses correctes. » Le jury insiste sur la présentation et la rigueur — « il est nécessaire de spécifier l’état physique (liquide, solide, gazeux, en solution) des différentes espèces chimiques » dans toute équation —, sur la précision et la concision des réponses, et sur le commentaire critique des résultats numériques. La question ouverte Q14 était « bien valorisée » mais majoritairement ignorée.

**Gestion du temps.** Sécuriser d’abord les questions de cours et d’application directe (chaque partie commence par là), puis les enchaînements guidés ; réserver du temps pour les questions ouvertes de fin de partie (Q14, Q24) et garder quelques minutes pour relire états physiques, unités et chiffres significatifs.

## Première partie — Les conséquences d'impacts de foudre

Cette partie construit un modèle thermodynamique de la production d’ozone par un éclair : structures de Lewis et polarité (Q1–2), oxydoréduction et dosage iodométrique (Q3–5), spectrophotométrie (Q6–7), puis définitions, équilibres et températures d’inversion (Q8–13), et une question ouverte de bilan énergétique (Q14).

### Question 1

> [!INDICATION]
> Appliquer Klechkowski pour les structures électroniques, puis construire les structures de Lewis en comptant d'abord le nombre total d'électrons de valence et en interdisant toute hypervalence sur une entité de la 2ᵉ période.

#### Solution

$\text{N}$ ($Z=7$) : $1s^2\,2s^2\,2p^3$. $\text{O}$ ($Z=8$) : $1s^2\,2s^2\,2p^4$.

$\text{NO}_2$ : $5+2\times6 = 17$ électrons de valence, soit un **électron célibataire** (radical). Structure coudée, azote central :

$$
\text{O}=\overset{\displaystyle\oplus}{\text{N}}{}^{\!\bullet}\!-\overset{\displaystyle\ominus}{\text{O}}\ \longleftrightarrow\ \overset{\displaystyle\ominus}{\text{O}}\!-\overset{\displaystyle\oplus}{\text{N}}{}^{\!\bullet}\!=\text{O}
$$

L'azote porte l'électron non apparié et une charge formelle $+$, l'oxygène simplement lié une charge $-$ ; aucune entité ne dépasse l'octet (N totalise 7 électrons, admissible pour un radical).

$\text{O}_3$ : $18$ électrons de valence, molécule coudée non cyclique, oxygène central :

$$
\text{O}=\overset{\displaystyle\oplus}{\text{O}}\!-\overset{\displaystyle\ominus}{\text{O}}\ \longleftrightarrow\ \overset{\displaystyle\ominus}{\text{O}}\!-\overset{\displaystyle\oplus}{\text{O}}=\text{O}
$$

> [!JURY]
> Réussite 64 %, mais le jury signale que **la formule de $\text{NO}_2$ est fausse dans plus de deux tiers des copies** : oubli de l'électron célibataire (on dessine $\text{NO}_2^+$ ou $\text{NO}_2^-$), non-respect du décompte des électrons, et surtout hypervalence interdite — « aucun élément de la deuxième période ne saurait être hypervalent ». Compter les électrons de valence avant de tracer.

### Question 2

> [!INDICATION]
> Relier solubilité dans l'eau (solvant polaire) à la polarité des solutés, elle-même déduite de la géométrie.

#### Solution

$\text{O}_2$ est linéaire et homonucléaire : moment dipolaire nul, molécule **apolaire**. $\text{O}_3$ est **coudée** ; les deux liaisons polarisées ne se compensent pas, le moment dipolaire résultant est non nul : molécule **polaire**. L'eau étant polaire, les interactions dipôle-dipôle (voire liaisons hydrogène) stabilisent $\text{O}_3$ en solution bien davantage que $\text{O}_2$ : d'où une solubilité de l'ozone nettement supérieure.

> [!JURY]
> 42 %. Inutile de discuter la géométrie de $\text{O}_2$ (diatomique, forcément linéaire). L'erreur pointée : invoquer la géométrie « sans examen de la polarité ». Le moment dipolaire est une grandeur **vectorielle** : c'est sa non-compensation qui importe.

### Question 3

> [!INDICATION]
> Calculer les nombres d'oxydation (n.o.) de O dans $\text{O}_3$ et $\text{O}_2$ pour montrer que le couple brut ne fait apparaître aucun transfert, puis introduire l'eau pour lever l'obstacle.

#### Solution

Dans $\text{O}_3$ et $\text{O}_2$ (corps homonucléaires), tous les atomes d'oxygène sont au n.o. **0**. Écrit sous la forme $\text{O}_3(aq)/\text{O}_2(aq)$, le couple ne manifeste aucune variation de n.o. : impossible de déterminer le nombre d'électrons échangés, ce qui bloque les élèves.

En introduisant l'eau, $\text{O}_3(aq)/\text{O}_2(aq),\text{H}_2\text{O}(\ell)$, un atome d'oxygène passe du n.o. $0$ (dans $\text{O}_3$) au n.o. $-\mathrm{II}$ (dans $\text{H}_2\text{O}$) : il gagne **2 électrons**. La demi-équation s'écrit :

$$
\text{O}_3(aq) + 2\,\text{H}^+ + 2\,e^- = \text{O}_2(aq) + \text{H}_2\text{O}(\ell)
$$

Vérification : O : $3 = 2+1$ ; H : $2=2$ ; charge : $-2+2 = 0$. 

> [!JURY]
> 47 %. Le jury rappelle que « le nombre d'oxydation se rapporte à un élément dans une entité » et que le nombre d'électrons échangés **égale la différence des n.o.**, sans ajustement par les électrons une fois les éléments équilibrés.

### Question 4

> [!INDICATION]
> Combiner les demi-équations des couples $\text{O}_3/\text{O}_2,\text{H}_2\text{O}$ et $\text{I}_3^-/\text{I}^-$, puis exprimer $K°$ à partir des potentiels standard.

#### Solution

L'ozone (oxydant, $E°=2{,}08$ V) oxyde les iodures (réducteur, $E°=0{,}54$ V) :

$$
\text{O}_3(aq) + 3\,\text{I}^-(aq) + 2\,\text{H}^+(aq) = \text{O}_2(aq) + \text{I}_3^-(aq) + \text{H}_2\text{O}(\ell)
$$

À l'équilibre, l'égalité des potentiels de Nernst donne

$$
\log K° = \frac{n\,(E°_1 - E°_2)}{0{,}059}
$$

$$
\log K° = \frac{2\,(2{,}08-0{,}54)}{0{,}059} \approx 52
$$

$$
\boxed{K° \approx 10^{52}}
$$

$K°$ est colossale : la réaction est quantitative. Le $\text{I}_3^-$ (diiode) formé colore en **bleu-noir** le papier amidonné ; même une trace d'ozone donne une réaction détectable visuellement.

> [!JURY]
> 52 %. Beaucoup appliquent une expression de $K°$ « sans recul » : elle doit ici se déduire des **potentiels standard**. Le rôle de l'**amidon** (révélateur du diiode) est trop rarement perçu.

### Question 5

> [!INDICATION]
> Écrire d'abord la réaction de titrage, remonter à $n(\text{O}_3)$ en tenant compte du rendement de solubilisation, convertir en teneur et comparer au seuil.

#### Solution

Titrage du diiode par le thiosulfate :

$$
\text{I}_3^-(aq) + 2\,\text{S}_2\text{O}_3^{2-}(aq) = 3\,\text{I}^-(aq) + \text{S}_4\text{O}_6^{2-}(aq)
$$

À l'équivalence : $n(\text{S}_2\text{O}_3^{2-}) = C\,V_{eq} = 5{,}0\cdot10^{-3}\times 11{,}0\cdot10^{-3} = 5{,}5\cdot10^{-5}$ mol, d'où $n(\text{I}_3^-) = \tfrac12 n(\text{S}_2\text{O}_3^{2-}) = 2{,}75\cdot10^{-5}$ mol.

D'après la question 4, $n(\text{O}_3)_{\text{dissous}} = n(\text{I}_3^-) = 2{,}75\cdot10^{-5}$ mol. Le rendement de solubilisation étant de 90 % :

$$
n(\text{O}_3)_{\text{air}} = \frac{2{,}75\cdot10^{-5}}{0{,}90} = 3{,}06\cdot10^{-5}\ \text{mol (dans 10 m}^3).
$$

Masse : $m = 3{,}06\cdot10^{-5}\times 48{,}0 = 1{,}47\cdot10^{-3}$ g. Teneur :

$$
\frac{1{,}47\ \text{mg}}{10\ \text{m}^3} = 147\ \mu\text{g}\cdot\text{m}^{-3} < s = 180\ \mu\text{g}\cdot\text{m}^{-3}.
$$

Le seuil de recommandation n'était **pas dépassé**. Pour repérer l'équivalence : ajouter de l'empois d'amidon en fin de titrage — l'équivalence est marquée par la **disparition de la coloration bleue**.

> [!JURY]
> 46 %. Partir de la réaction support est indispensable ; la formule « $C_1V_1=C_2V_2$ » est fausse. Le rendement de 90 % est « source d'erreurs inattendues ». La **conductimétrie est inadaptée** (nombreux ions, dont oxonium) : on privilégie le repérage par changement de couleur explicité.

### Question 6

> [!INDICATION]
> Énoncer principe et loi, préciser le domaine de validité avec ordres de grandeur, puis choisir le maximum d'absorption.

#### Solution

*Principe* : la spectroscopie UV-visible sonde les **transitions électroniques** ; l'échantillon absorbe une partie de la lumière incidente, on mesure l'absorbance en fonction de la longueur d'onde.

*Loi de Beer-Lambert* : $A = \varepsilon\,\ell\,c$, avec $A$ absorbance (sans dimension, $A = \log(I_0/I) \ge 0$),
$\varepsilon$ coefficient d'absorption molaire ($\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$),
$\ell$ longueur de la cuve (cm) et $c$ concentration ($\text{mol}\cdot\text{L}^{-1}$).

*Validité* : lumière monochromatique, solutions **diluées** ($c \lesssim 10^{-2}\ \text{mol}\cdot\text{L}^{-1}$), milieu homogène non diffusant, absence de réaction chimique ou de phénomène de fluorescence.

Pour la mesure, régler le détecteur au **maximum d'absorption**, lu sur la figure 1 vers $\lambda \approx 255$ nm : la sensibilité ($\mathrm dA/\mathrm dc$) y est maximale et la dépendance en $\lambda$ localement faible.

> [!JURY]
> 50 %. Des définitions mènent à une « absorbance négative ». Les conditions de validité doivent être chiffrées (« un ordre de grandeur est attendu »).

### Question 7

> [!INDICATION]
> Traduire 25 ppbv en fraction molaire, calculer la quantité d'ozone dans $1\ \text{m}^3$ via le gaz parfait, puis **ajouter** cette masse à la teneur de la question 5.

#### Solution

$25$ ppbv $= 25\cdot10^{-9}$ en fraction volumique $=$ fraction molaire (gaz parfait). Dans $1\ \text{m}^3$ d'air à $298$ K, $10^5$ Pa :

$$
n_{\text{tot}} = \frac{PV}{RT}
$$

$$
n_{\text{tot}} = \frac{10^5\times 1}{8{,}314\times 298} = 40{,}4\ \text{mol}
$$

$$
n(\text{O}_3) = 25\cdot10^{-9}\times 40{,}4 = 1{,}01\cdot10^{-6}\ \text{mol}
$$

$$
m(\text{O}_3) = 1{,}01\cdot10^{-6}\times 48{,}0 = 4{,}8\cdot10^{-5}\ \text{g}
$$

$$
\boxed{m(\text{O}_3) = 48\ \mu\text{g}\ \text{par m}^3}
$$

Juste après 19 h, la teneur passerait de $147\ \mu\text{g}\cdot\text{m}^{-3}$ (Q5) à $147 + 48 = 195\ \mu\text{g}\cdot\text{m}^{-3} > 180$ : le seuil **aurait été dépassé** (comparaison faite avec les 180 µg·m⁻³ de la question 5, seule valeur chiffrée fournie par l’énoncé).

> [!JURY]
> 12 %. Difficulté majeure : lire que les 25 ppbv sont une augmentation **absolue** (à ajouter à la quantité de la question 5), non relative. L'usage de valeurs « connues » de volume molaire exige de préciser la température.

### Question 8

> [!INDICATION]
> Restituer la définition exacte de $\Delta_r Z$ (variables bloquées), l'approximation d'Ellingham et l'état standard des gaz.

#### Solution

$\displaystyle \Delta_r Z = \left(\frac{\partial Z}{\partial \xi}\right)_{T,P}$ : dérivée de la grandeur extensive $Z$ par rapport à l'avancement, **à $T$ et $P$ constants**.

*Approximation d'Ellingham* : $\Delta_r H°$ et $\Delta_r S°$ sont supposées **indépendantes de la température** (hors changement d'état sur l'intervalle considéré).

*État standard d'un gaz* : gaz **pur**, **parfait**, sous la pression $P° = 1$ bar, à la température considérée (il n'existe pas de température standard).

> [!JURY]
> 31 %. Les variables bloquées sont « parfois écrites de manière aléatoire ». Le jury insiste : gaz parfait **et pur**, et « il n'existe pas de température standard ».

### Question 9

> [!INDICATION]
> Invoquer la définition de l'état standard de référence d'un élément.

#### Solution

À 298 K, $\text{N}_2(g)$ et $\text{O}_2(g)$ sont les **corps simples de référence** des éléments azote et oxygène (forme la plus stable sous $P°$). Par convention, l'enthalpie standard de formation d'un corps simple de référence est nulle :

$$
\Delta_f H°(\text{N}_2,g) = \Delta_f H°(\text{O}_2,g) = 0.
$$

> [!JURY]
> 50 %. La valeur est connue, la justification « peu rigoureuse » : distinguer corps pur / corps simple / corps simple de référence, et état standard d'une espèce / état standard de référence d'un élément.

### Question 10

> [!INDICATION]
> Comparer $Q_r$ à $K°$ (inchangée à $T$ fixée) lors d'une variation de $P$, via le signe de $\Delta n_{\text{gaz}}$.

#### Solution

À $T$ fixée, $K°$ est inchangée ; une augmentation de $P$ modifie $Q_r$ et le système évolue dans le sens qui diminue le nombre de moles de gaz.
- (1) $\text{N}_2+\text{O}_2 = 2\,\text{NO}$ : $\Delta n_{\text{gaz}} = 2-2 = 0$ → **aucune influence** de $P$.
- (2) $2\,\text{NO}+\text{O}_2 = 2\,\text{NO}_2$ : $\Delta n_{\text{gaz}} = 2-3 = -1$ → une hausse de $P$ **favorise le sens direct**.
- (3) $6\,\text{NO}_2 = 3\,\text{N}_2 + 4\,\text{O}_3$ : $\Delta n_{\text{gaz}} = 7-6 = +1$ → une hausse de $P$ **favorise le sens inverse**.

> [!JURY]
> 31 %. Le résultat est souvent juste, mais justifié par Le Châtelier, « qui ne figure plus dans les programmes de CPGE ». Raisonner par $Q_r$ et le second principe ; $K°$ ne dépend que de $T$.

### Question 11

> [!INDICATION]
> Définir $G$, calculer $\Delta_r H°_2$ et $\Delta_r S°_2$ à partir de D3, puis donner la forme affine et les valeurs numériques.

#### Solution

$G = H - TS$. Pour (2), $2\,\text{NO}+\text{O}_2 = 2\,\text{NO}_2$ :

$$
\Delta_r H°_2 = 2(33{,}10) - 2(90{,}29) = -114{,}38\ \text{kJ}\cdot\text{mol}^{-1}
$$

$$
\Delta_r S°_2 = 2(240{,}04) - 2(210{,}76) - 205{,}15 = -146{,}6\ \text{J}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}
$$

$$
\Delta_r G°_2(T) = \Delta_r H°_2 - T\,\Delta_r S°_2
$$

$$
\Delta_r G°_2(T) = -114{,}38 + 0{,}1466\,T\quad(\text{kJ}\cdot\text{mol}^{-1})
$$

À $298$ K : $\Delta_r G°_2 = -114{,}38 + 43{,}7 = \boxed{-70{,}7\ \text{kJ}\cdot\text{mol}^{-1}}$.
À $20\,000$ K : $\Delta_r G°_2 = -114{,}38 + 2932 = \boxed{+2{,}82\cdot10^{3}\ \text{kJ}\cdot\text{mol}^{-1}}$.

> [!PIEGE]
> 58 %. Attention aux unités ($\text{kJ}\cdot\text{mol}^{-1}$ pour $\Delta_r H°,\Delta_r G°$ ; $\text{J}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$ pour $\Delta_r S°$) et préciser les unités dans l'expression semi-numérique. Kirchhoff est hors programme ici.

### Question 12

> [!INDICATION]
> Relier le signe de $\Delta_r H°$ au sens favorisé en température par la loi de Van't Hoff, énoncée explicitement.

#### Solution

Loi de Van't Hoff : $\dfrac{\mathrm d\ln K°}{\mathrm dT} = \dfrac{\Delta_r H°}{RT^2}$.

- Réaction (1) : $\Delta_r H°_1 = +180{,}58\ \text{kJ}\cdot\text{mol}^{-1} > 0$ (endothermique) → $K°$ **croît avec $T$** → sens direct favorisé à **haute température**.
- Réaction (2) : $\Delta_r H°_2 = -114{,}38\ \text{kJ}\cdot\text{mol}^{-1} < 0$ (exothermique) → $K°$ **décroît avec $T$** → sens direct favorisé à **basse température**.

> [!JURY]
> 53 %. « La seule donnée du nom [Van't Hoff] ne peut suffire : il fallait donner l'expression de la loi » et mener le raisonnement jusqu'au bout.

### Question 13

> [!INDICATION]
> Calculer $T_{\text{inv}} = \Delta_r H°/\Delta_r S°$ pour (1) et (2), puis bâtir le scénario chronologique de formation d'ozone (chauffage puis refroidissement).

#### Solution

Pour (1), $\Delta_r G°_1 = 180{,}58 - 0{,}025\,T$ donne $\Delta_r H°_1 = 180{,}58\ \text{kJ}\cdot\text{mol}^{-1}$, $\Delta_r S°_1 = 25\ \text{J}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$ :

$$
T_{\text{inv}}(1) = \frac{180\,580}{25} \approx \boxed{7{,}2\cdot10^{3}\ \text{K}}
$$

Pour (2) ($\Delta_r H°_2$ et $\Delta_r S°_2$ tous deux négatifs) :

$$
T_{\text{inv}}(2) = \frac{-114\,380}{-146{,}6} \approx \boxed{7{,}8\cdot10^{2}\ \text{K}}
$$

*Scénario.* Au point d'impact, $T \approx 30\,000\,°\text{C} \approx 3{,}0\cdot10^4$ K $>T_{\text{inv}}(1)$ : la réaction (1) est déplacée dans le sens direct → formation de $\text{NO}$.
Lors du refroidissement, dès que $T < T_{\text{inv}}(2) \approx 780$ K, la réaction (2) (exothermique) est favorisée → formation de $\text{NO}_2$.
Enfin la réaction (3), quantitative dans ces conditions, décompose $\text{NO}_2$ en $\text{N}_2$ et $\text{O}_3$ : l'ozone apparaît au terme de cette chaîne « chauffage puis trempe ».

> [!PIEGE]
> 36 %. Les valeurs doivent rester **positives** et cohérentes avec les signes de Q11-12. Les déplacements d'équilibre successifs sont le cœur de l'explication.

### Question 14

> [!INDICATION]
> Question ouverte valorisée. Dimensionner le cylindre, calculer la matière disponible, identifier le réactif limitant, puis exploiter le bilan net pour majorer la masse d'ozone, et vérifier que l'énergie n'est pas limitante.

#### Solution

*Géométrie.* Cylindre de rayon $r = 0{,}25$ m, longueur $L = 5{,}0\cdot10^3$ m :

$$
V = \pi r^2 L
$$

$$
V = \pi (0{,}25)^2 (5000) = 9{,}8\cdot10^{2}\ \text{m}^3
$$

*Matière.* $n_{\text{tot}} = \dfrac{PV}{RT} = \dfrac{10^5\times 982}{8{,}314\times 298} = 3{,}96\cdot10^4$ mol, d'où (D5) $n(\text{O}_2) = 0{,}21\,n_{\text{tot}} = 8{,}3\cdot10^3$ mol (réactif limitant en oxygène), $n(\text{N}_2) = 0{,}78\,n_{\text{tot}} = 3{,}1\cdot10^4$ mol (en excès).

*Bilan net.* En combinant $3\times(1) + 3\times(2) + (3)$, le diazote est régénéré et il reste :

$$
3\,\text{O}_2 = 2\,\text{O}_3
$$

L'azote joue le rôle de catalyseur du cycle. La masse maximale d'ozone est donc fixée par l'oxygène disponible :

$$
n(\text{O}_3)_{\max} = \tfrac{2}{3}\,n(\text{O}_2)
$$

$$
n(\text{O}_3)_{\max} = \tfrac{2}{3}(8{,}3\cdot10^3) = 5{,}5\cdot10^3\ \text{mol}
$$

$$
m(\text{O}_3)_{\max} = 5{,}5\cdot10^3 \times 48{,}0 = 2{,}7\cdot10^5\ \text{g} \approx \boxed{2{,}7\cdot10^2\ \text{kg}}.
$$

*Vérification énergétique.* Il faudrait $\Delta H \approx \frac{n(\text{O}_3)}{2}\times 2\Delta_f H°(\text{O}_3) = \frac{5500}{2}\times 285 = 7{,}8\cdot10^5\ \text{kJ} = 7{,}8\cdot10^8$ J, inférieur à l'apport $10^{10}$ J : **la matière, et non l'énergie, limite** la production. La valeur obtenue est une borne supérieure (conversion totale de l'oxygène du cylindre).

> [!JURY]
> 6 %. Question « plus longue, bien valorisée », désertée. Le jury récompense toute démarche engagée. Écueils signalés : absence d'identification du réactif limitant, bilan énergétique mené avec $G$ au lieu de $H$, volumes molaires inadaptés, et oubli des composés azotés. Le choix de la voie dépend de l'interprétation retenue : l'essentiel est d'afficher clairement hypothèses et bilan.

## Deuxième partie — La chimie des effets spéciaux

Trois sous-parties indépendantes sur les effets spéciaux : l’explosion pyrotechnique et la température de flamme (A, Q15–24), la corrosion de l’acier et les courbes courant–potentiel (B, Q25–32), la cinétique de dégradation du polystyrène par la propanone (C, Q33–38).

**A — Les impacts de balles**

### Question 15

> [!INDICATION]
> Relier les signes à thermicité et à la variation de quantité de matière gazeuse, puis justifier le caractère total par $K°$.

#### Solution

$\Delta_r H°_5 = -1790{,}4\ \text{kJ}\cdot\text{mol}^{-1} < 0$ : réaction **exothermique**. $\Delta_r S°_5 = +1984{,}5\ \text{J}\cdot\text{K}^{-1}\cdot\text{mol}^{-1} > 0$ : forte augmentation du désordre, cohérente avec la formation de **11 moles de gaz** à partir de réactifs solides.

Obstacle pour les élèves : confondre réaction **totale** (équilibre rompu à l'état final) et réaction **équilibrée**. Ici $\Delta_r G°_5(298) = -1790{,}4 - 298\times 1{,}9845 = -2{,}38\cdot10^3\ \text{kJ}\cdot\text{mol}^{-1}$, soit $\log K° = -\Delta_r G°/(RT\ln 10) \approx 4\cdot10^{2}$, d'où $K° \approx 10^{417}$ : la transformation est **légitimement totale**.

> [!JURY]
> 37 %. Relier $\Delta_r S°$ à l'évolution de la quantité de gaz (pas seulement « désordre »). La distinction totale/équilibrée est mal maîtrisée.

### Question 16

> [!INDICATION]
> Énoncer les conditions conjointes d'une explosion (chimique).

#### Solution

La transformation réunit les conditions d'une explosion :
1. **Fortement exothermique** ($\Delta_r H°_5 \ll 0$) : libération brutale de chaleur.
2. **Production abondante de gaz** (11 mol de gaz par mole d'avancement) à partir de solides : augmentation brutale de volume/pression.
3. **Cinétique rapide** une fois amorcée (énoncé).
4. En milieu **confiné** (tube), l'élévation de température accroît encore la pression des gaz produits.

L'association chaleur + gaz + rapidité + confinement provoque une surpression explosive. La seule production de gaz ne suffirait pas.

> [!JURY]
> 17 %. « Une transformation produisant des gaz n'est pas toujours explosive » : plusieurs conditions précises sont attendues.

### Question 17

> [!INDICATION]
> Montrer que « adiabatique + isochore » rend $Q=0$ et $W=0$, donc $\Delta U = 0$ et $T$, $P$ maximales.

#### Solution

Un transfert thermique vers l'extérieur abaisserait la température finale ; une détente fournirait un travail aux dépens de l'échauffement. L'hypothèse **adiabatique** ($Q=0$) et **isochore** ($W = -\!\int P_{\text{ext}}\,\mathrm dV = 0$) conduit donc aux valeurs **extrêmes (maximales)** de $T$ et de $P$.

Premier principe appliqué au contenu du tube : $\Delta U = Q + W = 0$, soit

$$
\boxed{\Delta U = 0.}
$$

C'est l'énergie interne (et non l'enthalpie) qui est la fonction d'état conservée.

> [!JURY]
> 27 %. Le jury est « surpris » que $U$ ne soit pas identifiée comme la fonction d'état pertinente ; des candidats appliquent la loi de Laplace, « parfois à un solide ». Ce n'est **pas** un calcul de température de flamme isobare.

### Question 18

> [!INDICATION]
> Appliquer (6) avec $\sum \nu_i^{\text{gaz}} = 11$.

#### Solution

$\sum_i \nu_i^{\text{gaz}} = 4 + 3 + 2 + 2 = 11$.

$$
\Delta_r U°_5 = \Delta_r H°_5 - RT\sum_i \nu_i^{\text{gaz}} = -1790{,}4\cdot10^3 - 8{,}314\times 298\times 11
$$

$$
\Delta_r U°_5 = -1790{,}4\cdot10^3 - 2{,}73\cdot10^4 = \boxed{-1{,}82\cdot10^3\ \text{kJ}\cdot\text{mol}^{-1}}.
$$

(Correspond à la ligne 31 : `DU = DH - R*T0*nuGaz*1.e-3`.)

> [!PIEGE]
> 47 %. Bien traitée. Prendre $T = 298$ K (page de garde) et ne pas recalculer $\Delta_r H°$, donnée.

### Question 19

> [!INDICATION]
> Préciser les conditions de (7), rappeler que $U$ ne dépend que de $T$ pour les phases considérées, puis construire le cycle fictif « réaction isotherme + échauffement isochore ».

#### Solution

La relation $\Delta U = \xi\,\Delta_r U°$ suppose une transformation **isotherme** (à $T_0$), $\Delta_r U°$ indépendante de la composition. Or pour un **gaz parfait**, comme pour une **phase condensée indilatable et incompressible**, $U$ ne dépend que de $T$.

On décompose la transformation réelle en deux étapes fictives de même état initial et final (fonction d'état) :
- Étape 1 : réaction complète à $T_0 = 298$ K. $\Delta U_1 = \xi_{\max}\,\Delta_r U°_5$.
- Étape 2 : échauffement isochore des produits de $T_0$ à $T_f$. $\Delta U_2 = \Big(\sum_i n_i\,C_{V,i}\Big)(T_f - T_0)$.

Comme $\Delta U = \Delta U_1 + \Delta U_2 = 0$ :

$$
\boxed{T_f = T_0 - \frac{\Delta_r U°_5}{\displaystyle\sum_i \nu_i\,C_{V,i}}}
$$

(le $\xi_{\max}$ se simplifie), avec $C_{V} = C_P - R$ pour les gaz et $C_V \approx C_P$ pour $\text{K}_2\text{S}(s)$.

> [!JURY]
> 15 %. Le jury note que la dépendance de $U$ en la seule température est « inconnue d'un bon nombre » et que l'on voit « toujours un calcul de température de flamme isobare ». Le cycle est la clé.

### Question 20

> [!INDICATION]
> Évaluer $\sum \nu_i C_{V,i}$, en déduire $\Delta T$, et compléter la ligne 35.

#### Solution

Capacités (par mole d'avancement) :

$$
\sum \nu_i C_{V,i} = 2(142{,}3) + 4(37{,}12-R) + 3(29{,}15-R) + 2(33{,}59-R) + 2(29{,}12-R) = 5{,}54\cdot10^{2}\ \text{J}\cdot\text{K}^{-1}.
$$

$$
\Delta T = -\frac{\Delta_r U°_5}{\sum \nu_i C_{V,i}}
$$

$$
\Delta T = \frac{1{,}818\cdot10^{6}}{554{,}5} = 3{,}28\cdot10^{3}\ \text{K}
$$

$$
T_f = T_0 + \Delta T \approx 3{,}6\cdot10^{3}\ \text{K}
$$

**Ligne 35** cohérente avec le script (DU en kJ, $C_V$ en $\text{J}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$) :
```python
DT = -DU*1.e3/(2*CV_K2S + 4*CV_CO2 + 3*CV_CO + 2*CV_H2O + 2*CV_N2)
```
Hypothèse ajoutée : $\text{K}_2\text{S}$ reste solide (énoncé).

> [!JURY]
> 8 %. Erreur emblématique : « le signe et/ou le facteur $10^3$ de conversion… oublié(s) ». L'énoncé indique que le script renvoie $T_f = 4{,}09\cdot10^3$ K ; la valeur $T_f = 4{,}09\cdot10^3$ K renvoyée par le script « modifié en conséquence » intègre la fusion de $\text{K}_2\text{S}$ (enthalpie de fusion et $C_P$ du liquide, voir Q21) ; on la retient pour la suite, comme fourni.

### Question 21

> [!INDICATION]
> Confronter $T_f$ à $T_{\text{fus}}(\text{K}_2\text{S})$.

#### Solution

$T_{\text{fus}} = 840\,°\text{C} = 1113$ K. Or $T_f \gg T_{\text{fus}}$ : le sulfure de potassium ne reste **pas solide**, il **fond** (voire se vaporise). L'hypothèse de la question 20 est invalidée. Un calcul rigoureux doit intégrer la **fusion** ($\Delta_{\text{fus}}H°$) et la capacité thermique du **liquide** ($C_P = 101{,}0$), ce qui modifie $T_f$ (et explique l'écart avec la valeur $4{,}09\cdot10^3$ K obtenue par le script tenant compte de l'état liquide).

> [!JURY]
> 21 %. « L'état liquide de $\text{K}_2\text{S}$ en fin de transformation est généralement bien identifié. »

### Question 22

> [!INDICATION]
> Appliquer la loi des gaz parfaits avec $V_{\text{final}}$ corrigé du volume de $\text{K}_2\text{S}$, en utilisant $T_f = 4{,}09\cdot10^3$ K.

#### Solution

$m(\text{K}_2\text{S}) = 2\,\xi_{\max}\,M = 2\times 5\cdot10^{-3}\times 110{,}26 = 1{,}10$ g, soit $V(\text{K}_2\text{S}) = \dfrac{1{,}10\cdot10^{-3}}{1{,}81\cdot10^3} = 6{,}1\cdot10^{-7}\ \text{m}^3$.

$$
V_{\text{final}} = 1{,}75\cdot10^{-6} - 6{,}1\cdot10^{-7} = 1{,}14\cdot10^{-6}\ \text{m}^3.
$$

$n_{\text{gaz}} = 11\,\xi_{\max} = 5{,}5\cdot10^{-2}$ mol. D'où

$$
p_f = \frac{n_{\text{gaz}} R T_f}{V_{\text{final}}} = \frac{5{,}5\cdot10^{-2}\times 8{,}314\times 4{,}09\cdot10^3}{1{,}14\cdot10^{-6}} \approx 1{,}6\cdot10^{9}\ \text{Pa} \approx \boxed{1{,}6\cdot10^{4}\ \text{bar}}.
$$

Cette surpression gigantesque, libérée très rapidement, provoque l'éclatement brutal attendu pour simuler un impact de balle : résultat cohérent avec l'usage.

> [!PIEGE]
> 16 %. Ne pas négliger le volume du solide. A.N. souvent fautives.

### Question 23

> [!INDICATION]
> Traiter $\text{Na}$ comme intermédiaire : combiner (8) et (9) via le bilan de matière, pas par addition directe d'équations.

#### Solution

$n(\text{N}_2)$ nécessaire pour $V_a = 140$ L à $1$ bar, $298$ K : $n(\text{N}_2) = \dfrac{10^5\times 0{,}140}{8{,}314\times 298} = 5{,}65$ mol.

Soit $x$ mol d'avancement de (8) et $y$ de (9). Bilan sur le sodium (intermédiaire, consommé en totalité) : $2x = 10y \Rightarrow x = 5y$. Diazote total : $3x + y = 16y = 5{,}65 \Rightarrow y = 0{,}353$ mol, $x = 1{,}77$ mol.

$$
n(\text{NaN}_3) = 2x = 3{,}53\ \text{mol}
$$

$$
\boxed{m(\text{NaN}_3) = 3{,}53\times 65{,}01 = 2{,}3\cdot10^{2}\ \text{g}}
$$

$$
n(\text{KNO}_3) = 2y = 0{,}71\ \text{mol}
$$

$$
\boxed{m(\text{KNO}_3) = 0{,}71\times 101{,}1 = 71\ \text{g}}
$$

> [!JURY]
> 13 %. « Le sodium est une espèce intermédiaire » : ne pas additionner les équations. Utiliser la loi des gaz parfaits, non un volume molaire tabulé.

### Question 24

> [!INDICATION]
> Exprimer le **volume initial des réactifs solides** (et non du gaz) en fonction d'un avancement, le contraindre à $< 1$ mL et en déduire des masses.

#### Solution

Volume initial $= \dfrac{m(\text{NaN}_3)}{\rho(\text{NaN}_3)} + \dfrac{m(\text{KNO}_3)}{\rho(\text{KNO}_3)}$, avec $m(\text{NaN}_3) = 10y\,M(\text{NaN}_3)$ et $m(\text{KNO}_3) = 2y\,M(\text{KNO}_3)$ (en conservant $x=5y$). On obtient $V_{\text{initial}} = y\times 4{,}5\cdot10^{-4}\ \text{m}^3$, soit $V < 1\ \text{mL} \Leftrightarrow y < 2{,}2\cdot10^{-3}$ mol.

Choix $y = 2{,}0\cdot10^{-3}$ mol :

$$
m(\text{NaN}_3) = 10y\,M
$$

$$
m(\text{NaN}_3) = 2{,}0\cdot10^{-2}\times 65{,}01 = 1{,}3\ \text{g}
$$

$V(\text{NaN}_3) = 0{,}70\ \text{mL}$

$$
m(\text{KNO}_3) = 2y\,M
$$

$$
m(\text{KNO}_3) = 4{,}0\cdot10^{-3}\times 101{,}1 = 0{,}40\ \text{g}
$$

$V(\text{KNO}_3) = 0{,}19\ \text{mL}$
Volume initial total $\approx 0{,}89\ \text{mL} < 1\ \text{mL}$. On propose donc $\boxed{m(\text{NaN}_3)\approx 1{,}3\ \text{g},\ m(\text{KNO}_3)\approx 0{,}40\ \text{g}}$.

> [!JURY]
> 5 %. « Ce n'est pas le volume (final) de gaz mais le volume (initial) des réactifs » qui doit être inférieur à 1 mL.

**B — La durabilité d'un acier**

### Question 25

> [!INDICATION]
> Décrire le montage à trois électrodes avec potentiostat et rôles.

#### Solution

Montage à **trois électrodes** piloté par un potentiostat :
- **Électrode de travail** (ET) : le matériau étudié, siège de la réaction examinée.
- **Électrode de référence** (ESH, ECS) : impose la référence de potentiel ; **aucun courant** ne la traverse.
- **Contre-électrode** (auxiliaire) : ferme le circuit et écoule le courant.
On mesure $E$ (entre ET et référence) au voltmètre (grande impédance) et $I$ (dans la branche ET/contre-électrode) à l'ampèremètre.

*Schéma décrit en texte : cellule à trois électrodes reliée à un potentiostat ; voltmètre entre ET et référence, ampèremètre dans la branche ET–contre-électrode.*

> [!PIEGE]
> 28 %. Erreurs fréquentes : oubli du générateur/ampèremètre/voltmètre, rôles confondus, **courant non nul dans la référence**.

### Question 26

> [!INDICATION]
> Définir rapidité/lenteur par la cinétique du transfert, tracer les deux allures, placer les surpotentiels.

#### Solution

Un système est **rapide** si le transfert électronique est cinétiquement aisé : le courant croît fortement dès que $E$ s'écarte du potentiel d'équilibre $E_{eq}$ (surpotentiel négligeable). Il est **lent** si un **surpotentiel** $\eta = E - E_{eq}$ significatif est nécessaire pour établir un courant notable : $\eta_a > 0$ (anodique), $\eta_c < 0$ (cathodique).

*Schéma décrit en texte : $j = f(E)$ ; système rapide = vague raide centrée sur $E_{eq}$ ; système lent = branches décalées, avec $\eta_a>0$ et $\eta_c<0$ repérés depuis $E_{eq}$.*

> [!JURY]
> 30 %. Définitions souvent « réduites à la description des courbes » ; ne pas confondre $E_{eq}$ et $E°$.

### Question 27

> [!INDICATION]
> Citer deux facteurs cinétiques du transfert à l'interface.

#### Solution

Deux facteurs influençant la **vitesse du transfert électronique à la surface** :
- **Nature du matériau d'électrode** (électrocatalyse) : l'énergie d'activation du transfert dépend de l'électrode (ex. surtension du dihydrogène très différente sur Pt et sur Fe).
- **Température** : une hausse de $T$ accélère le transfert (loi d'Arrhenius appliquée à la constante de vitesse électrochimique).

> [!PIEGE]
> 41 %. Bien lire : ce sont les facteurs de la **vitesse de transfert à l'électrode** qui sont demandés.

### Question 28

> [!INDICATION]
> Identifier un palier de diffusion cathodique et le lire.

#### Solution

Le palier du couple $\text{O}_2(g)/\text{H}_2\text{O}(\ell)$ est un **courant limite de diffusion** : la réduction de $\text{O}_2$ est limitée par l'apport diffusif de $\text{O}_2$ dissous (faible solubilité). Ce courant est **cathodique**, donc **négatif**. Lecture graphique du plateau : $j_{\lim} \approx -3$ à $-4\ \text{mA}\cdot\text{cm}^{-2}$ (valeur modeste, cohérente avec la faible solubilité de $\text{O}_2$).

> [!JURY]
> 37 %. Palier « parfois confondu avec le mur du solvant » ; il doit être « compté négativement ».

### Question 29

> [!INDICATION]
> Reconnaître l'électrode mixte, écrire les deux demi-équations, évaluer le surpotentiel par rapport à $E_{eq}$ corrigé par Nernst.

#### Solution

Lors de la corrosion, le fer constitue une **électrode mixte** : il est simultanément siège d'une oxydation et d'une réduction.

$$
\text{Fe}(s) \rightarrow \text{Fe}^{2+}(aq) + 2e^- \qquad\text{(oxydation, anodique)}
$$

$$
2\,\text{H}^+(aq) + 2e^- \rightarrow \text{H}_2(g) \qquad\text{(réduction, cathodique)}
$$

À $\text{pH} = 1$ et $P(\text{H}_2) = P°$, le potentiel d'équilibre du couple $\text{H}^+/\text{H}_2$ vaut (Nernst) :

$$
E_{eq} = E° - 0{,}06\,\text{pH} = -0{,}06\ \text{V}.
$$

Le surpotentiel cathodique se lit graphiquement comme $\eta_c = E_{\text{corr}} - E_{eq}$, négatif (de l'ordre de $-0{,}3$ V d'après la figure, là où la branche cathodique de $\text{H}^+/\text{H}_2$ atteint le courant de corrosion).

> [!JURY]
> 30 %. Le surpotentiel s'apprécie « à partir du potentiel d'équilibre donné par Nernst », en tenant compte du pH, et non du seul $E°$.

### Question 30

> [!INDICATION]
> Identifier branches anodique/cathodique, positionner le potentiel de corrosion (mixte) et lire $j_{\text{corr}}$ à l'intersection.

#### Solution

Sur la figure 2 :
- couple $\text{H}^+/\text{H}_2$ (carrés) : branche **cathodique** ($2\text{H}^+ + 2e^- \to \text{H}_2$) pour $E<E_{eq}$, branche anodique ($\text{H}_2 \to 2\text{H}^+ + 2e^-$) pour $E>E_{eq}$ ;
- couple $\text{Fe}^{2+}/\text{Fe}$ (triangles) : branche **anodique** ($\text{Fe}\to\text{Fe}^{2+}+2e^-$) pour $E>E_{eq}(\text{Fe})$.

Au potentiel de corrosion $E_{\text{corr}}$ (potentiel mixte), l'intensité anodique d'oxydation du fer égale en valeur absolue l'intensité cathodique de réduction de $\text{H}^+$.
Graphiquement, le **courant de corrosion** $j_{\text{corr}}$ se lit à l'intersection de la branche anodique $\text{Fe}^{2+}/\text{Fe}$ et de la branche cathodique $\text{H}^+/\text{H}_2$ :
on relève $|j_{\text{corr}}|$ de l'ordre de quelques $\text{mA}\cdot\text{cm}^{-2}$.

*Schéma décrit en texte : annexe complétée — branches annotées, $E_{\text{corr}}$ au croisement, $j_{\text{corr}}$ reporté sur l'axe.*

> [!JURY]
> 31 %. La courbe $i$–$E$ sert de « diagramme de prédominance » : attention au sens d'écriture des demi-équations sur chaque vague.

### Question 31

> [!INDICATION]
> Définir la passivation, discuter la peinture, proposer une autre protection.

#### Solution

La **passivation** est la formation, à la surface du métal, d'une couche (souvent un oxyde) adhérente et peu conductrice qui **bloque cinétiquement** la poursuite de la corrosion. Protection par **peinture** : oui, elle isole physiquement le métal du milieu corrosif tant qu'elle reste intègre (barrière). Autre méthode : **protection galvanique par anode sacrificielle** (ex. zinc, plus réducteur que le fer, qui s'oxyde à sa place), ou protection cathodique par courant imposé, galvanisation, alliage passivable (acier inoxydable).

> [!PIEGE]
> 41 %. Méthodes bien connues ; expliciter chaque terme et justifier l'emploi (ou non) de la peinture.

### Question 32

> [!INDICATION]
> Comparer, sur la figure, le courant de corrosion sans / avec film.

#### Solution

Sur fer nu, le courant de corrosion (intersection $\text{Fe}^{2+}/\text{Fe}$ anodique / $\text{H}^+/\text{H}_2$ cathodique) est non négligeable. Sur fer recouvert de polyaniline, la courbe « Fe avec film » présente un courant anodique **très fortement abaissé** : l'intersection avec les branches cathodiques (inchangées) donne un courant de corrosion **quasi nul**. Le film freine cinétiquement l'oxydation du fer : il constitue donc une protection adaptée contre la corrosion.

> [!JURY]
> 24 %. Utiliser **explicitement** les courbes : mentionner que le **courant de corrosion devient nul** — « il s'agit de cinétique de l'oxydoréduction ».

**C — La simulation d'une attaque acide**

### Question 33

> [!INDICATION]
> Lire les pictogrammes D8 et en déduire les précautions.

#### Solution

La propanone porte le pictogramme **« inflammable »** (flamme, H225 : liquide et vapeurs très inflammables) et le pictogramme **« point d'exclamation »** (irritant, H319 irritation des yeux, H336 somnolence/vertiges). Précautions : travailler **à l'écart de toute flamme/étincelle/source de chaleur**, sous **hotte ventilée** (vapeurs), port de **lunettes de protection** et **gants** (irritation, EUH066 dessèchement de la peau), éviter le contact répété.

> [!PIEGE]
> 55 %. Question correctement traitée.

### Question 34

> [!INDICATION]
> Reconnaître une loi de vitesse avec constante d'Arrhenius ; donner la signification et les dimensions des paramètres.

#### Solution

$\dfrac{\mathrm d\alpha}{\mathrm dt} = A\,(1-\alpha)^n\,\exp\!\left(-\dfrac{E_a}{RT}\right)$ est une **loi de vitesse** : la vitesse de conversion est le produit d'une constante de vitesse $k(T) = A\exp(-E_a/RT)$ (**loi d'Arrhenius**) par un terme $(1-\alpha)^n$ (fraction de polymère non converti, « ordre » $n$).
- $A$ : **facteur préexponentiel**. Comme $\mathrm d\alpha/\mathrm dt$ est en $\text{s}^{-1}$ et $(1-\alpha)^n$ et l'exponentielle sont sans dimension, $[A] = \text{s}^{-1}$.
- $n$ : ordre apparent, **sans dimension**.
- $E_a$ : **énergie d'activation**, en $\text{J}\cdot\text{mol}^{-1}$ (car $E_a/RT$ sans dimension).

> [!JURY]
> 27 %. Arrhenius (orthographe !) reconnue, mais « la forme générale d'une loi de vitesse rarement perçue ». Les dimensions sont explicitement demandées.

### Question 35

> [!INDICATION]
> Relier polydispersité et conservation de masse.

#### Solution

Un polymère polydisperse est un mélange de chaînes de longueurs (nombres de motifs) différentes : la « quantité de matière » (nombre de moles de chaînes) et la masse molaire moyenne sont mal définies et **évoluent** au cours de la décomposition (les ruptures de chaînes créent de nouvelles molécules, modifiant la distribution). En revanche, la **masse** est directement mesurable (gravimétrie) et insensible à la distribution des longueurs : c'est pourquoi le taux de conversion $\alpha$ est défini à partir de la masse $m$, et non d'une quantité de matière.

> [!JURY]
> 11 %. « Notion de polydispersité et lien avec la cinétique mal expliqués. »

### Question 36

> [!INDICATION]
> Séparer les variables, changer $t$ en $T$ via $\beta$, et surtout **changer les bornes**.

#### Solution

De (12) : $\dfrac{\mathrm d\alpha}{(1-\alpha)^n} = A\exp\!\left(-\dfrac{E_a}{RT}\right)\mathrm dt$. Avec $\beta = \mathrm dT/\mathrm dt$ constant, $\mathrm dt = \mathrm dT/\beta$ :

$$
\frac{\mathrm d\alpha}{(1-\alpha)^n} = \frac{A}{\beta}\exp\!\left(-\frac{E_a}{RT}\right)\mathrm dT.
$$

Intégration avec changement cohérent des bornes : $\alpha=0 \leftrightarrow T=0$ K (pas de réaction à $0$ K, hypothèse énoncé) et $\alpha=\alpha_{\text{fin}} \leftrightarrow T=T_{\text{fin}}$ :

$$
\underbrace{\int_0^{\alpha_{\text{fin}}}\frac{\mathrm d\alpha}{(1-\alpha)^n}}_{F(\alpha_{\text{fin}})} = \frac{A}{\beta}\int_0^{T_{\text{fin}}}\exp\!\left(-\frac{E_a}{RT}\right)\mathrm dT. \qquad\blacksquare
$$

> [!JURY]
> 39 %. Les « changements de bornes ne sont quasiment jamais mentionnés » : c'est l'exigence de rigueur ici.

### Question 37

> [!INDICATION]
> Justifier $n=1$, simplifier (15) via $2RT_{\text{fin}}/E_a \ll 1$, proposer une régression linéaire.

#### Solution

*Justification $n=1$* : une décomposition où chaque motif (ou chaque chaîne) réagit indépendamment avec une probabilité donnée conduit à une vitesse proportionnelle à la quantité restante $(1-\alpha)$, soit un ordre $1$ (dégénérescence de l'ordre vis-à-vis du solvant en large excès).

*Simplification* : $E_a$ étant grande ($\sim 10^2\ \text{kJ}\cdot\text{mol}^{-1}$) et $RT_{\text{fin}}$ de quelques $\text{kJ}\cdot\text{mol}^{-1}$, $\dfrac{2RT_{\text{fin}}}{E_a} \ll 1$, donc $\left(1 - \dfrac{2RT_{\text{fin}}}{E_a}\right)\approx 1$ :

$$
\ln\!\left[-\frac{\ln(1-\alpha_{\text{fin}})}{T_{\text{fin}}^2}\right] \approx \ln\!\left(\frac{AR}{\beta E_a}\right) - \frac{E_a}{R\,T_{\text{fin}}}.
$$

*Méthode* : tracer $y = \ln\!\big[-\ln(1-\alpha_{\text{fin}})/T_{\text{fin}}^2\big]$ en fonction de $1/T_{\text{fin}}$.
La droite a pour **pente** $-E_a/R$ (→ $E_a$) et pour **ordonnée à l'origine** $\ln(AR/\beta E_a)$ (→ $A$, $\beta$ connu).

> [!JURY]
> 5 %. Question « ramenant à des considérations classiques de cinétique », très peu abordée.

### Question 38

> [!INDICATION]
> Exploiter la non-constance de $E_a$ (figure 3) et conclure sur l'intérêt du chauffage.

#### Solution

La figure 3 montre que l'énergie d'activation **dépend du taux de conversion** (elle croît fortement puis décroît) : elle n'est pas constante. Le modèle (12), qui suppose $A$, $n$ et $E_a$ uniques, est donc une **simplification** : la dégradation procède en réalité par **plusieurs processus/étapes** aux énergies d'activation différentes.

La décomposition requiert de franchir une barrière de $\sim 10^2$ à $2\cdot10^2\ \text{kJ}\cdot\text{mol}^{-1}$ : à température ambiante, $\exp(-E_a/RT)$ est infime, la vitesse est négligeable. Il faut **chauffer la propanone** pour accroître $k(T)$ (Arrhenius) et rendre la dégradation du polystyrène suffisamment rapide (effet visuel convaincant d'« attaque acide »).

> [!PIEGE]
> 3 %. Très peu traitée ; le lien vitesse–chauffage est la clé.

## Troisième partie — La synthèse de l'adrénaline

Synthèse totale de l’adrénaline : stéréochimie et RMN (Q39–40), mécanismes réactionnels de la voie de synthèse (Q41–48), comparaison avec la biosynthèse (Q49–50), puis dédoublement par l’acide tartrique (Q51–53).

### Question 39

> [!INDICATION]
> Classer les substituants selon CIP et dessiner l'énantiomère (R) ; préciser la relation entre les deux stéréoisomères.

#### Solution

Le seul atome de carbone asymétrique est le carbone portant l'hydroxyle benzylique (carbinol). Ses substituants et leur priorité CIP :

$$
-\text{OH}\ (1) \;>\; -\text{CH}_2\text{NHCH}_3\ (2,\ \text{premier atome N}) \;>\; -\text{Ar (noyau, premiers atomes C,C,C)}\ (3) \;>\; -\text{H}\ (4).
$$

En plaçant $\text{H}$ vers l'arrière, la rotation $\text{OH}\to\text{CH}_2\text{NHCH}_3\to\text{Ar}$ doit être **horaire** pour (R).

*Schéma décrit en texte : adrénaline (R) en représentation de Cram ; C* avec OH, CH₂NHCH₃, cycle catéchol, H en arrière, sens horaire.*

Avec un unique centre stéréogène, les deux stéréoisomères de configuration (R et S) sont **énantiomères** (images l'un de l'autre dans un miroir, non superposables).

> [!JURY]
> 35 %. Le classement CIP « doit apparaître clairement » ; énantiomérie parfois confondue avec diastéréoisomérie.

### Question 40

> [!INDICATION]
> Attribuer chaque signal via intégration, multiplicité et déplacement (blindage), en s'appuyant sur D12.

#### Solution

- **2,29 ppm, 3H, singulet** : le groupe $\text{N–CH}_3$ (méthylamino). Trois protons équivalents, sans couplage observable (le $\text{NH}$ échangeable n'est pas indiqué), $\delta$ typique d'un $\text{CH}_3$ porté par N.
- **2,49 ppm (1H, dd, $J=12{,}0$ et $4{,}3$) et 2,52 ppm (1H, dd, $J=12{,}0$ et $8{,}3$)** : les deux protons **diastéréotopes** du $\text{CH}_2$ voisin du centre asymétrique.
Le couplage géminal $|{}^2J| = 12{,}0$ Hz (D12.2 : $\text{CH}_2$, 10–16 Hz) les relie ; chacun couple en outre au méthine avec $4{,}3$ et $8{,}3$ Hz.
- **4,44 ppm (1H, dd, $J=8{,}3$ et $4{,}3$)** : le méthine $\text{CH–OH}$ benzylique, couplé aux deux protons du $\text{CH}_2$ ($8{,}3$ et $4{,}3$ Hz).
Déblindé ($\delta\approx 4{,}4$) par l'oxygène et le cycle.
- **6,55–6,72 ppm (3H, massif)** : les trois protons aromatiques du cycle trisubstitué (déblindés par le courant de cycle).

> [!JURY]
> 28 %. Le méthyle est bien repéré, mais le **blindage électronique** à l'origine des déplacements est « mal ou méconnu » : on inverse signaux aromatiques et aliphatiques.

### Question 41

> [!INDICATION]
> Comparer la stabilité des bases conjuguées (mésomérie), choisir une base cohérente avec $\text{p}K_A(\text{phénol})\approx 9{,}9$, écrire le mécanisme (déprotonation + SN2).

#### Solution

Le phénolate délocalise sa charge négative sur le cycle aromatique par **mésomérie** (les doublets, non les charges, se délocalisent) :

$$
\text{PhO}^- \longleftrightarrow\ \text{charges portées par les carbones ortho/para du cycle.}
$$

Cette stabilisation rend le phénolate plus stable que le cyclohexanolate (charge localisée, aucune délocalisation). Base conjuguée plus stable ⇒ acide plus fort ⇒ $\text{p}K_A$(phénol) $\approx 9{,}9 \ll 16$ (cyclohexanol).

*Base adaptée pour $\text{A}\to\text{B}$* : une base dont l'acide conjugué a un $\text{p}K_A > 9{,}9$, par exemple le carbonate $\text{K}_2\text{CO}_3$ ($\text{p}K_A(\text{HCO}_3^-/\text{CO}_3^{2-}) = 10{,}3$).

*Mécanisme (synthèse de Williamson)* :
1. **Déprotonation** du phénol (équilibre acido-basique, réversible) : $\text{ArOH} + \text{CO}_3^{2-} \rightleftharpoons \text{ArO}^- + \text{HCO}_3^-$.
2. **Substitution nucléophile $S_N2$** : l'oxygène du phénolate attaque le carbone benzylique de $\text{BnBr}$, départ de $\text{Br}^-$ → éther benzylique.
Les deux groupes phénol de A sont ainsi benzylés (B = catéchol dibenzylé portant l'aldéhyde).

> [!JURY]
> 21 %. « Comparer la stabilité des bases conjuguées » ; écrire les formes mésomères avec doublets ; la base choisie doit être cohérente. Dans le mécanisme, les flèches partent d'un **doublet**, pas d'un atome ; chaque étape ajustée ; réversibilité des étapes acido-basiques explicitée.

### Question 42

> [!INDICATION]
> Écrire la réaction de formation du Grignard et énoncer les précautions avec leur justification.

#### Solution

$$
\text{R–X} + \text{Mg} \xrightarrow{\text{éther anhydre}} \text{R–Mg–X}
$$

Précautions :
- **Milieu anhydre** et solvant éthéré sec (éther, THF) : l'organomagnésien, base/nucléophile très fort, est détruit par l'eau et tout composé à H labile ($\text{RMgX} + \text{H}_2\text{O} \to \text{RH} + \text{Mg(OH)X}$).
- **Atmosphère inerte** (absence de $\text{O}_2$, $\text{CO}_2$) qui réagissent avec $\text{RMgX}$.
- Limiter les réactions parasites : **couplage de Würtz** ($\text{R–R}$), **équilibre de Schlenk** ($2\,\text{RMgX} \rightleftharpoons \text{R}_2\text{Mg} + \text{MgX}_2$) — d'où ajout lent du dérivé halogéné, verrerie sèche.

> [!JURY]
> 37 %. Conditions anhydres connues, mais Schlenk et Würtz « peu cités ».

### Question 43

> [!INDICATION]
> Relier différence d'électronégativité C–métal, polarisation/nucléophilie du carbone, et compatibilité avec l'ester.

#### Solution

La liaison C–Mg est plus polarisée que la liaison C–Zn : $\Delta\chi(\text{C–Mg}) = 2{,}55 - 1{,}31 = 1{,}24$ contre $\Delta\chi(\text{C–Zn}) = 2{,}55 - 1{,}65 = 0{,}90$. Le carbone de l'organomagnésien est donc **plus nucléophile/basique** que celui de l'organozincique.

L'organomagnésien $\text{EtO}_2\text{C–CH}_2\text{MgBr}$ attaquerait la fonction **ester** du même réactif (auto-condensation) et réagirait de façon non sélective. L'**organozincique**, moins polarisé donc **moins réactif et plus sélectif**, **tolère l'ester** (réactif de type Reformatsky) et s'additionne proprement sur l'aldéhyde. D'où son choix.

> [!JURY]
> 5 %. Raisonnement électronégativité → nucléophilie → réactivité vis-à-vis de l'ester « quasiment pas mené ».

### Question 44

> [!INDICATION]
> Reconnaître une addition de Reformatsky, donner la structure de C et son mécanisme.

#### Solution

$\text{B} = \text{Ar–CHO}$ ($\text{Ar} = $ 3,4-bis(benzyloxy)phényle). L'organozincique $\text{BrZn–CH}_2\text{–CO}_2\text{Et}$ s'additionne sur l'aldéhyde :

*Mécanisme* : le carbone nucléophile de l'organozincique attaque le carbone du carbonyle (flèche du doublet C–Zn vers le C=O ; le doublet $\pi$ bascule sur l'oxygène), formant un **alcoolate de zinc** $\text{Ar–CH(OZnBr)–CH}_2\text{–CO}_2\text{Et}$. L'**hydrolyse acide** ($\text{H}_3\text{O}^+$) protone l'alcoolate :

$$
\boxed{\text{C} = \text{Ar–CH(OH)–CH}_2\text{–CO}_2\text{Et}}\quad(\text{3-hydroxy-3-arylpropanoate d'éthyle}).
$$

Cohérent avec D (hydrazide formée ensuite par $\text{H}_2\text{N–NH}_2$ sur l'ester).

> [!JURY]
> 25 %. Structure et mécanisme corrects « dans un certain nombre de copies » ; mêmes vigilances qu'en Q41 (flèches, carbone fonctionnel explicite).

### Question 45

> [!INDICATION]
> Justifier NaH par sa basicité forte, non nucléophile, et le $\text{p}K_A$ du N–H de l'oxazolidinone.

#### Solution

La première étape $\text{E}\to\text{F}$ est la **déprotonation du N–H** de l'oxazolidinone ($\text{p}K_A \approx 21$, D9) pour former l'amidure, suivie d'une méthylation par $\text{ICH}_3$ ($S_N2$).
$\text{NaH}$ est une **base forte** ($\text{p}K_A(\text{H}_2/\text{H}^-) = 38 \gg 21$ : déprotonation quantitative, libération de $\text{H}_2$) et **non nucléophile** :
il déprotone le N–H sans entrer en compétition avec $\text{ICH}_3$ (pas de réaction parasite d'alkylation de la base).

> [!JURY]
> 11 %. Le caractère **non nucléophile** de $\text{NaH}$ n'est mentionné qu'« exceptionnellement ».

### Question 46

> [!INDICATION]
> Dessiner le montage à reflux et écrire l'hydrolyse du carbamate cyclique (perte de CO₂), vérifiée par la formule brute de G.

#### Solution

*Schéma décrit en texte : montage à reflux — ballon sur chauffe-ballon et support élévateur, réfrigérant droit vertical, eau circulant de **bas en haut**, points de fixation (pinces) indiqués.*

Au reflux en milieu $\text{HCl}$ concentré, le **carbamate cyclique** (oxazolidinone) est hydrolysé : ouverture du cycle en amino-alcool avec **libération de $\text{CO}_2$**. Les éthers benzyliques subsistent (clivés plus tard par $\text{H}_2/\text{Pd}$). G est l'amino-alcool dibenzylé :

$$
\text{F} + \text{H}_2\text{O} \xrightarrow{\text{HCl}} \underbrace{(\text{BnO})_2\text{C}_6\text{H}_3\text{–CH(OH)–CH}_2\text{–NH–CH}_3}_{\text{G},\ \text{C}_{23}\text{H}_{25}\text{NO}_3} + \text{CO}_2.
$$

Vérification : $14 + 6 + 1 + 1 + 1 = 23$ C ; 1 N ; $2(\text{OBn}) + 1(\text{OH}) = 3$ O. 

> [!JURY]
> 11 %. Montage à reflux à soigner (points de fixation, circulation d'eau) ; l'équation (dégagement de $\text{CO}_2$) est « très rarement vue ».

### Question 47

> [!INDICATION]
> Identifier la protection et l'étape qu'elle rend possible.

#### Solution

L'étape $\text{A}\to\text{B}$ **protège les deux fonctions phénol** sous forme d'éthers benzyliques. Sans protection, les phénols (acides et nucléophiles) réagiraient lors de l'étape à l'organozincique (réaction acido-basique détruisant le réactif, consommation de réactif), empêchant l'addition sur l'aldéhyde. La protection benzylique, stable dans ces conditions, est ensuite retirée par **hydrogénolyse** ($\text{H}_2/\text{Pd}$) en fin de synthèse. (On distingue bien **phénol** et **alcool** : réactivités différentes.)

> [!PIEGE]
> 19 %. Préciser **quelle étape** poserait problème sans protection ; ne pas confondre alcool et phénol (différence étudiée en Q41).

### Question 48

> [!INDICATION]
> Localiser la création du centre asymétrique et conclure au racémique.

#### Solution

L'unique carbone asymétrique est créé lors de l'**addition de Reformatsky** (formation de C, Q44), sur un aldéhyde prochiral avec des réactifs achiraux : les deux faces du carbonyle sont attaquées indifféremment, sans aucune induction. Toutes les étapes étant achirales, le produit final est obtenu sous forme de **mélange racémique** $(\pm)$ (50 % R, 50 % S). La synthèse n'est pas stéréosélective.

> [!PIEGE]
> 25 %. Annoncer le racémique ne suffit pas : il faut **identifier l'étape** créant le C*.

### Question 49

> [!INDICATION]
> Repérer l'étape enzymatique créant le carbinol.

#### Solution

Dans la biosynthèse (figure 6), le carbone asymétrique (carbinol) est créé lors de l'hydroxylation de la **dopamine en noradrénaline** catalysée par la **dopamine β-hydroxylase**. Cette enzyme est **stéréospécifique** : elle ne forme qu'un seul énantiomère (R). C'est l'étape-clé du contrôle stéréochimique.

> [!JURY]
> 24 %. Étape « généralement bien identifiée ».

### Question 50

> [!INDICATION]
> Comparer les deux voies via sélectivité, conditions et économie d'atomes explicitée.

#### Solution

Avantages de la biosynthèse :
- **Énantiosélectivité** enzymatique : obtention directe du seul stéréoisomère actif, sans étape de dédoublement (gain en étapes et en matière).
- **Absence de groupes protecteurs** : la synthèse chimique mobilise une protection/déprotection benzylique ($\text{BnBr}$, puis $\text{H}_2/\text{Pd}$), des réactifs comme l'hydrazine — autant d'atomes non incorporés au produit et perdus en sous-produits.
- **Conditions douces** (milieu aqueux, température physiologique), moins de réactifs toxiques/dangereux.
- **Économie d'atomes** supérieure : la fraction massique des réactifs retrouvée dans le produit est plus élevée (les groupes protecteurs et réactifs auxiliaires de la voie chimique dégradent fortement cette économie).

> [!JURY]
> 11 %. L'économie d'atomes, suggérée par l'énoncé, « est souvent citée mais pas toujours explicitée ».

### Question 51

> [!INDICATION]
> Dénombrer les stéréoisomères (dont le méso), discuter l'activité optique, proposer la polarimétrie.

#### Solution

Acide tartrique : $\text{HOOC–CHOH–CHOH–COOH}$, deux carbones asymétriques équivalents.
- **(R,R)** et **(S,S)** : deux énantiomères, chacun **chiral** et **optiquement actif** (l'un dextrogyre, l'autre lévogyre, pouvoirs rotatoires opposés).
- **(R,S)** = composé **méso** : possède un plan de symétrie interne, donc **achiral**, **optiquement inactif**.

Soit 3 stéréoisomères de configuration (une paire d'énantiomères + le méso).

*Schéma décrit en texte : les trois en projection de Cram ; (R,R) et (S,S) images miroir, (R,S) avec plan de symétrie.*

Pour déterminer la pureté (optique) d'un échantillon : **polarimétrie** — mesure du pouvoir rotatoire comparée à la valeur de l'énantiomère pur (excès énantiomérique) ; appoint possible par point de fusion ou CPG chirale.

> [!PIEGE]
> 14 %. Nomenclature et Cram à maîtriser ; ne pas oublier le **méso achiral** ; relier activité optique et chiralité.

### Question 52

> [!INDICATION]
> Tracer le diagramme de prédominance du diacide (pKa 3,0 et 4,4), celui de l'adrénaline (amine), puis écrire la protonation.

#### Solution

Acide tartrique ($\text{H}_2\text{T}$), $\text{p}K_{A1} = 3{,}0$, $\text{p}K_{A2} = 4{,}4$ :

$$
\text{H}_2\text{T} \;\big|_{\,\text{pH}=3{,}0}\; \text{HT}^- \;\big|_{\,\text{pH}=4{,}4}\; \text{T}^{2-}
$$

Adrénaline : le site basique est l'**amine secondaire** (ion ammonium conjugué, $\text{p}K_A \approx 10{,}7$, cf. $(\text{H}_3\text{C})_2\text{NH}_2^+/(\text{H}_3\text{C})_2\text{NH}$) ; les phénols ($\text{p}K_A\approx 9{,}9$) n'interviennent qu'à pH élevé.

$$
\text{AdrH}^+ \;\big|_{\,\text{pH}\approx 10{,}7}\; \text{Adr (amine libre)}
$$

En présence d'acide tartrique **en excès**, le milieu est acide (pH $\sim 2$–3) : l'amine de l'adrénaline est entièrement **protonée**. Équation (acide fort relatif vis-à-vis de l'amine) :

$$
\text{Adr} + \text{H}_2\text{T} \;\longrightarrow\; \text{AdrH}^+ + \text{HT}^-.
$$

> [!JURY]
> 7 %. Le diagramme de l'acide tartrique est généralement correct (préciser les $\text{p}K_A$ et les structures) ; celui de l'adrénaline et sa transformation en ammonium « ne sont généralement pas vus ».

### Question 53

> [!INDICATION]
> Montrer que l'acide tartrique énantiopur forme des sels diastéréoisomères, séparables par cristallisation (dédoublement).

#### Solution

En choisissant un acide tartrique **énantiopur** (par ex. L-(+)), sa réaction avec l'adrénaline racémique produit **deux sels diastéréoisomères** :

$$
(\text{R-AdrH}^+)(\text{L-tartrate})\quad\text{et}\quad(\text{S-AdrH}^+)(\text{L-tartrate}).
$$

Des diastéréoisomères possèdent des propriétés physiques **différentes** (solubilité, point de fusion, aptitude à cristalliser), contrairement à des énantiomères. On peut donc les **séparer par cristallisation fractionnée**, puis libérer chaque énantiomère de l'adrénaline par traitement basique. Cette opération est le **dédoublement** (résolution) d'un racémique.

> [!PIEGE]
> 4 %. Peu abordée ; les diastéréoisomères et le dédoublement sont le cœur de la réponse.

## Quatrième partie — La réalisation d'un ordinateur quantique

Choix d’un complexe de cuivre(II) comme qubit : spin S = 1/2 (Q54–55), géométries et paramètre τ (Q56–58), diagramme d’orbitales (Q59–60), spectroscopie IR lointain et temps de relaxation (Q61–63).

### Question 54

> [!INDICATION]
> Relier $S=1/2$ à un système à deux niveaux de durée de vie suffisante.

#### Solution

Un qubit exige **deux états quantiques identifiables** ($|0\rangle, |1\rangle$).
Un spin électronique total $S = 1/2$ possède exactement **deux états** ($m_S = +1/2$ et $m_S = -1/2$) : il réalise naturellement un système à deux niveaux.
Une valeur $S=1/2$ (un seul électron non apparié) fournit deux états bien définis et isolables, propices à un temps de vie $\ge 1\ \mu\text{s}$. D'où la condition $S = 1/2$.

> [!JURY]
> 26 %. Un « grand nombre de candidats justifient correctement… en détaillant les deux états de spin ».

### Question 55

> [!INDICATION]
> Établir la configuration du cuivre (exception), puis celle de $\text{Cu}^{2+}$, et vérifier $S=1/2$ ; nommer les règles.

#### Solution

Règles utilisées : **Klechkowski** (ordre de remplissage), principe d'exclusion de **Pauli**, règle de **Hund**.

$\text{Cu}$ ($Z=29$) : la configuration attendue $[\text{Ar}]3d^9 4s^2$ est supplantée par $[\text{Ar}]3d^{10}4s^1$ (**irrégularité** : sous-couche $d$ pleine plus stable) :

$$
\text{Cu} : 1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,3d^{10}\,4s^1 = [\text{Ar}]\,3d^{10}\,4s^1.
$$

$\text{Cu}^{2+}$ : on retire d'abord l'électron $4s$ puis un électron $3d$ :

$$
\text{Cu}^{2+} = [\text{Ar}]\,3d^{9}.
$$

Avec 9 électrons $d$, il reste **un électron célibataire** → $S = 1/2$ : $\text{Cu}^{2+}$ respecte la condition de la question 54.

> [!PIEGE]
> 38 %. L'irrégularité du cuivre est connue, mais la configuration du **cation** est souvent fausse (ne pas écrire $3d^9$ en retirant les $d$ avant le $4s$). Le jury demande de **nommer** les règles, pas de les énoncer.

### Question 56

> [!INDICATION]
> Déduire la géométrie de chaque $\tau$, puis justifier par le champ de ligands l'existence d'une alternative au tétraèdre.

#### Solution

$\tau \to 0$ : plan carré ; $\tau \to 1$ : tétraédrique.
- $\tau_1 = 0{,}62$ : structure **intermédiaire fortement distordue** (tétraèdre aplati vers le plan carré).
- $\tau_2 = 0{,}066$ et $\tau_3 = 0{,}053$ : $\approx 0$ → géométrie **plan carré**.

Nature des interactions : le **champ de ligands** (interactions électrostatiques/covalentes métal–ligand) lève la dégénérescence des orbitales $d$. Pour un cation $d^9$, la stabilisation par le champ de ligands (associée à l'effet Jahn-Teller) favorise la géométrie **plan carré** plutôt que tétraédrique, bien que le complexe soit tétracoordiné.

> [!PIEGE]
> 8 %. Rarement abordée ; utiliser les valeurs de $\tau$ pour conclure, puis décrire brièvement les interactions.

### Question 57

> [!INDICATION]
> Définir ligand polydente et justifier l'intérêt par l'effet chélate (entropie).

#### Solution

Un **ligand polydente** possède plusieurs atomes donneurs (sites de coordination) capables de se lier simultanément au même centre métallique. Intérêt : l'**effet chélate** — un complexe chélaté est thermodynamiquement **plus stable** (constante de formation plus grande) que l'analogue à ligands monodentes. L'origine est essentiellement **entropique** : la complexation d'un ligand polydente libère davantage de molécules (solvant, ligands monodentes déplacés), augmentant le désordre.

> [!JURY]
> 17 %. Ligand polydente bien défini ; « effet chélate peu connu », origine entropique à préciser.

### Question 58

> [!INDICATION]
> Croiser $\tau$, $d(\text{Cu–N})$ et structure des ligands pour classer la rigidité, puis éliminer le complexe 1.

#### Solution

La rigidité augmente avec la contrainte structurale du ligand et la brièveté/régularité des liaisons :
- Complexe **1** : ligands les plus souples, $\tau_1 = 0{,}62$ (forte distorsion possible), $d(\text{Cu–N}) = 0{,}1955$ nm la plus longue → **le moins rigide**.
- Complexe **2** : ponté, intermédiaire.
- Complexe **3** : noyaux aromatiques fusionnés imposant une géométrie plane figée → **le plus rigide**.

Classement (rigidité croissante) : $\boxed{1 < 2 < 3}$.

*Élimination du complexe 1* : son $\tau_1 = 0{,}62$ traduit une forte déviation du plan carré vers le tétraèdre, et sa flexibilité favorise les **déformations/vibrations** (relaxation locale) qui raccourcissent le temps de cohérence. Il ne satisfait donc pas à l'exigence d'un temps de vie $\ge 1\ \mu\text{s}$ : on l'écarte.

> [!JURY]
> 10 %. « Les candidats qui réfléchissent proposent la bonne réponse. »

### Question 59

> [!INDICATION]
> Remplir le diagramme de la figure 8 avec 9 électrons $d$ et conclure sur le spin unique.

#### Solution

$\text{Cu}^{2+}$ apporte 9 électrons $d$. On remplit par énergie croissante : les quatre orbitales les plus basses ($d_{xz}, d_{yz}, d_{xy}, d_{z^2}$) sont **doublement occupées** (8 électrons) ; l'orbitale la plus haute $d_{x^2-y^2}$ reçoit le **9ᵉ électron, célibataire** (dans le niveau de spin le plus bas).

*Schéma décrit en texte : diagramme complété — $d_{xz},d_{yz},d_{xy},d_{z^2}$ avec deux électrons chacune ; $d_{x^2-y^2}$ avec un seul électron.*

Il subsiste donc **un électron non apparié** → $S = 1/2$, et deux états de spin distinguables pour cet électron : le $\text{Cu}^{2+}$ dans cet environnement **reste un candidat qubit**.

> [!PIEGE]
> 13 %. Diagramme bien rempli ; le lien avec les **états de spin identifiables** n'est pas toujours mentionné.

### Question 60

> [!INDICATION]
> Relier l'écart énergétique spin up / spin down à un système à deux niveaux adressable.

#### Solution

L'écart d'énergie entre les orientations de spin (up/down) de l'orbitale singulièrement occupée définit un **système à deux niveaux bien séparés** : $|0\rangle$ = spin up, $|1\rangle$ = spin down. Cet écart $\Delta E$ fixe une **fréquence de transition** à laquelle le qubit peut être manipulé (résonance par rayonnement électromagnétique) et permet de préparer des superpositions contrôlées $a|0\rangle + b|1\rangle$. Une séparation nette garantit deux états distinguables et stables : d'où des qubits judicieux.

> [!JURY]
> 4 %. Arguments souvent bons mais « limités à un caractère qualitatif ».

### Question 61

> [!INDICATION]
> Relier $\Delta_l$ (en cm⁻¹) aux positions des bandes du spectre IR lointain.

#### Solution

Le spectre IR lointain (figure 9) donne les nombres d'onde des **modes de vibration collectifs/intermoléculaires**. Le paramètre $\Delta_l$ (en $\text{cm}^{-1}$) modélisant la relaxation locale correspond précisément à l'**énergie du mode de vibration (phonon local)** responsable de cette relaxation. Il s'identifie donc à la **position d'une bande** du spectre IR lointain : $\Delta_2 = 213\ \text{cm}^{-1}$ (complexe 2) et $\Delta_3 = 328\ \text{cm}^{-1}$ (complexe 3) coïncident avec les maxima d'absorption calculés (bande du complexe 3 décalée vers les plus grands nombres d'onde). Le lien est **quantitatif** : $\Delta_l \leftrightarrow \tilde\nu$ du mode.

> [!JURY]
> 4 %. Le jury « félicite ceux qui décrivent un lien quantitatif » et non une simple coïncidence d'unités.

### Question 62

> [!INDICATION]
> Relier la plus grande rigidité du complexe 3 à une vibration de plus haute énergie, donc une relaxation locale plus tardive.

#### Solution

Le complexe 3, plus rigide (noyaux aromatiques fusionnés, constantes de force plus élevées), présente des modes de vibration de **plus haute énergie** : d'où $\Delta_3 > \Delta_2$ (328 contre 213 $\text{cm}^{-1}$). Une valeur de $\Delta_l$ plus élevée signifie que le mode local de relaxation est **moins peuplé thermiquement** à une température donnée (facteur de Boltzmann $\exp(-hc\,\Delta_l/k_B T)$, inférieur à 1) : la contribution de la relaxation locale est **retardée**, le temps de cohérence est **plus long**. Il est donc préférable de **sélectionner le complexe 3**.

> [!PIEGE]
> 4 %. Très peu abordée.

### Question 63

> [!INDICATION]
> Lire sur la figure 10 la température où $t_1 = 1\ \mu\text{s}$ et identifier la contribution dominante.

#### Solution

Le cahier des charges impose $t_1 \ge 1\ \mu\text{s}$. Sur la figure 10, la courbe expérimentale (et le modèle) de $t_1(T)$ atteint $t_1 = 1\ \mu\text{s}$ vers $T \approx 2\cdot10^{2}\ \text{K}$ : c'est la **température maximale d'utilisation** du complexe 3. À cette température (régime de haute température), la contribution dominante au $1/t_1$ est le terme **Raman** (tirets-pointillés), qui impose alors la perte de cohérence. La relaxation principale mise en jeu est donc de **type Raman**.

> [!JURY]
> 6 %. « Quelques candidats analysent bien les différentes données ». Lecture graphique soignée attendue.

## Bilan

**Rigueur transversale.** Préciser l’état physique de chaque espèce dans toute équation ; mener le calcul littéral avant l’application numérique, avec les unités ; commenter chaque résultat chiffré (ordre de grandeur, cohérence physique).

**Thermodynamique et solutions.** Compter les électrons de valence avant toute structure de Lewis (aucune hypervalence en deuxième période) ; le nombre d’électrons échangés égale la différence des degrés d’oxydation ; $K°$ se déduit des potentiels standard ; raisonner sur $Q_r$ et $K°(T)$ plutôt que par un énoncé de Le Châtelier ; pour un gaz parfait comme pour une phase condensée, $U$ ne dépend que de $T$ — construire un cycle fictif pour les transformations adiabatiques ; repérer le réactif limitant avant tout bilan de matière.

**Électrochimie et cinétique.** Montage à trois électrodes, électrode mixte et potentiel de corrosion lu à l’intersection des branches ; systèmes rapides/lents et surpotentiels signés ; loi d’Arrhenius, ordre et dimensions d’une loi de vitesse ; séparation de variables avec changement explicite des bornes.

**Chimie organique et stéréochimie.** Comparer les stabilités des bases conjuguées (mésomérie) pour les pKa ; mécanismes fléchés depuis les doublets ; protection des phénols avant l’étape à l’organozincique (Reformatsky, tolérant à l’ester) ; classement CIP et création du centre asymétrique ; mélange racémique puis dédoublement par sels diastéréoisomères avec l’acide tartrique énantiopur.

**Structure et spectroscopies.** Un qubit exige un système à deux niveaux : $S = 1/2$ ; le paramètre $\tau$ distingue plan carré et tétraèdre ; l’effet chélate est d’origine entropique ; le temps de cohérence se lit sur les contributions directe, Raman et modes locaux de $1/t_1(T)$.
