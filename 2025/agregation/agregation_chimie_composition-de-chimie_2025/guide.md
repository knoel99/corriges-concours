# Agrégation Chimie — Composition de chimie 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve A de 5 heures (calculatrice autorisée), sujet « Critères de choix d'un solvant », 60 questions en cinq parties. Les données (constantes d'acidité, de formation, table IR, guide des solvants) sont regroupées en fin d'énoncé. Sauf mention contraire, les constantes d'équilibre sont exprimées avec l'état standard $C^\circ = 1\ \mathrm{mol\cdot L^{-1}}$.

## Présentation du sujet

**Thème.** « Critères de choix d'un solvant » : le sujet articule le choix d'un solvant de synthèse autour de cinq entrées — propriétés physiques et éco-compatibilité (partie I), solubilisation d'un sel avec une modélisation de plus en plus fine (partie II), extraction liquide-liquide et optimisation du nombre d'extractions (partie III), puis deux synthèses « vertes » menées dans l'eau : le Pro-Xylane® par réaction de Lubineau puis réduction (partie IV), et un précurseur de la grandifloracine par déaromatisation oxydante puis cascade de Diels-Alder (partie V). Épreuve de 5 heures, calculatrice autorisée, 60 questions, données regroupées en fin d'énoncé (constantes d'acidité et de formation, table IR, guide des solvants ACS).

**Découpage.**

| Partie | Questions | Contenu | Notions du programme |
|---|---|---|---|
| I | Q1–Q7 | Moment dipolaire, permittivité, proticité, classement de solvants, SN2 en milieu aprotique, guide éco-compatibilité | interactions intermoléculaires, solvant protique/aprotique, substitution nucléophile |
| II | Q8–Q21 | Dissolution du gypse : titrage EDTA, paires d'ions, Debye-Hückel | produit de solubilité, titrage, activité, force ionique |
| III | Q22–Q33 | Coefficients de partage (Beer-Lambert), extractions fractionnées, lecture de code Python | loi de Beer-Lambert, constante de partage, rendement d'extraction |
| IV | Q34–Q48 | Réaction de Lubineau sur le glucose, mutarotation, réduction stéréosélective du C-glycoside | oses, hémiacétal, mécanismes en milieu basique, CIP, excès diastéréoisomérique |
| V | Q49–Q60 | Synthèse one-pot de la grandifloracine : clivage periodate, déaromatisation, Diels-Alder, spectroscopies IR et RMN | VSEPR, clivage oxydant des diols, cycloaddition [4+2], RMN du proton |

**Difficulté et longueur.** Sujet long (60 questions en 5 h), très progressif dans les parties I–III. Les questions marquées d'un astérisque (*) dans l'énoncé — le « socle » — représentent 50 % du barème ; d'après le rapport 2025 elles ont été traitées 10 % plus souvent que la moyenne et réussies à environ 60 %. **Ce sont elles qu'il ne faut pas laisser passer** : Q1–Q4, Q7–Q13, Q16–Q17, Q22–Q27, Q29, Q34–Q42, Q45–Q46, Q49–Q53, Q55. Les questions les plus discriminantes sont en revanche les modélisations avancées (Q18–Q21), les mécanismes (Q39, Q43–Q44) et la fin de la partie V (Q58–Q60).

**Ce qu'en dit le rapport 2025.** Moyenne des admissibles 11,37 (écart-type 1,97), des admis 12,59 (écart-type 2,81), notes de 5,59 à 20. Le jury déplore des lacunes y compris sur des notions de lycée (formules de Lewis, VSEPR) et insiste sur la rigueur des mécanismes : les flèches courbes partent d'un doublet d'électrons, pas d'une charge formelle négative. Questions les plus réussies : Q23 (90 %), Q37 (91 %), Q57 (89 %) ; les moins abordées : Q60 (7 %), Q44 (11 %), Q21 (14 %).

**Gestion du temps.** Cinq parties d'inégale longueur : prévoir environ 50 min pour la partie I, 70 min pour la partie II (titrage et modélisation), 60 min pour la partie III, 70 min pour la partie IV et 50 min pour la partie V. Dans la partie II, les questions Q9, Q12, Q15, Q18, Q20 s'enchaînent sur les mêmes données : en cas de blocage, passer à la suite et y revenir. La partie III est indépendante du reste et peut se traiter par lecture directe des courbes et du code.

## Partie I — Propriétés générales des solvants

Propriétés générales des solvants : polarité, proticité, permittivité, puis éco-compatibilité via le guide ACS. Beaucoup de questions de socle, à sécuriser en priorité.

### A. Propriétés physiques des solvants

### Question 1

> [!INDICATION]
> Représenter la géométrie autour de l'atome d'oxygène de l'éthoxyéthane avant toute chose.

> [!INDICATION]
> Comparer l'électronégativité du carbone et de l'oxygène, sommer les deux moments de liaison, puis conclure sur le sens du vecteur résultant.

#### Solution

L'éthoxyéthane $\mathrm{CH_3CH_2{-}O{-}CH_2CH_3}$ possède un atome d'oxygène porteur de deux doublets non liants : la géométrie autour de O est **coudée** (angle $\mathrm{C{-}O{-}C} \approx 110^\circ$), la molécule n'est pas linéaire. Chaque liaison $\mathrm{C{-}O}$ est polarisée vers l'oxygène plus électronégatif que le carbone : $\mathrm{C^{\delta+}{-}O^{\delta-}}$. La somme vectorielle des deux moments de liaison n'est pas nulle :

$$
\boxed{\vec{\mu} \neq \vec{0}\ :\ \text{moment dipolaire permanent porté par la bissectrice de l'angle } \mathrm{C{-}O{-}C},\ \text{dirigé du pôle négatif (O) vers le pôle positif}}
$$

> [!JURY]
> Rapport 2025 : « Le moment dipolaire doit être dirigé du pôle négatif vers le pôle positif. » Une géométrie linéaire de l'éthoxyéthane, qui conduirait à $\vec{\mu} = \vec{0}$, est l'erreur sanctionnée.

> [!PIEGE]
> Ne pas dessiner la molécule linéaire : l'angle C–O–C d'un éther est coudé (environ 110°), c'est lui qui rend le moment résultant non nul.

### Question 2

> [!INDICATION]
> Rappeler ce que mesure la permittivité relative vis-à-vis de la force de Coulomb entre deux charges.

> [!INDICATION]
> En déduire l'écriture d'un composé ionique MX dissous dans ce solvant peu dispersant.

#### Solution

La permittivité relative $\varepsilon_r$ divise la force électrostatique de Coulomb entre deux charges par $\varepsilon_r$ : elle mesure le **pouvoir écranteur** du solvant, donc son caractère dispersant (ou ionisant). Avec $\varepsilon_r = 4$ (contre 79 pour l'eau), l'éthoxyéthane écrante très mal les interactions électrostatiques : c'est un solvant **peu dispersant**. Conséquence pour un composé ionique $\mathrm{MX}$ :

$$
\boxed{\mathrm{MX}\ \text{reste sous forme non dissociée, ou au mieux de paires d'ions } (\mathrm{M^+},\mathrm{X^-})\text{, et non } \mathrm{M^+}_{(sol)} + \mathrm{X^-}_{(sol)}}
$$

> [!PIEGE]
> Ne pas confondre caractère polaire/apolaire et caractère dispersant : la permittivité relative gouverne l'écrantage des interactions électrostatiques, pas le moment dipolaire.

### Question 3

> [!INDICATION]
> Définir précisément un solvant protique (penser à la liaison hydrogène).

> [!INDICATION]
> L'éthoxyéthane possède-t-il un atome d'hydrogène porté par un atome très électronégatif ?

#### Solution

Un solvant **protique** est un solvant capable de **donner** une liaison hydrogène, c'est-à-dire qui possède au moins un atome d'hydrogène porté par un atome très électronégatif (O–H, N–H ou F–H). L'éthoxyéthane ne comporte que des liaisons C–H et C–O : il ne peut pas donner de liaison hydrogène.

$$
\boxed{\text{L'éthoxyéthane est un solvant aprotique}}
$$

> [!JURY]
> Rapport 2025 : « Un solvant protique est un solvant capable de donner une liaison hydrogène. » Le voir comme un accepteur de liaison H est faux.

> [!PIEGE]
> Un solvant protique *donne* une liaison H ; c'est le solvant aprotique polaire qui peut seulement *accepter*.

### Question 4

> [!INDICATION]
> Classer d'abord par permittivité relative (dispersant / peu dispersant) et par symétrie de la molécule (polaire / apolaire).

> [!INDICATION]
> Dans chaque case, repérer la présence ou non d'une liaison O–H (protique / aprotique) et justifier chaque placement par la géométrie de la molécule.

#### Solution

Critères de classement : la molécule est **apolaire** si sa géométrie la rend symétrique ($\vec{\mu} = \vec{0}$) ; **polaire** sinon, et l'on distingue **dispersant** (grande permittivité relative, de plusieurs dizaines) de **peu dispersant** ($\varepsilon_r$ faible) ; le solvant est **protique** s'il possède une liaison O–H (ou N–H), **apotique** sinon.

| | Polaire dispersant | Polaire dispersant | Polaire peu dispersant | Polaire peu dispersant | Apolaire |
|---|---|---|---|---|---|
| | Protique | Aprotique | Protique | Aprotique | |
| Solvants | eau (εr = 79) | DMSO (εr = 49), DMF (εr = 37) | acide éthanoïque (εr = 6) | éthoxyéthane (εr = 4), dichlorométhane (εr = 9) | tétrachlorométhane (εr = 2,2) |

Justifications géométriques : l'eau est coudée et possède deux liaisons O–H (protique, très dispersante) ; le DMSO $\mathrm{(CH_3)_2S{=}O}$ et le DMF $\mathrm{HCON(CH_3)_2}$ présentent respectivement une géométrie pyramidale autour de S et plane autour du carbone du carbonyle, fortement polaires et sans liaison O–H (apotiques dispersants) ; l'acide éthanoïque possède une liaison O–H (protique) mais une permittivité faible ; le dichlorométhane est tétraédrique, les deux moments $\mathrm{C{-}Cl}$ ne se compensent pas (polaire, aprotique) ; l'éthoxyéthane est coudé, polaire mais peu dispersant ; le tétrachlorométhane est tétraédrique régulier, les quatre moments $\mathrm{C{-}Cl}$ se compensent :

$$
\boxed{\mathrm{CCl_4}\ \text{est le seul solvant apolaire de la liste } (\vec{\mu} = \vec{0})}
$$

### Question 5

> [!INDICATION]
> Pourquoi un solvant polaire aprotique rend-il le nucléophile anionique plus réactif qu'un solvant protique ?

> [!INDICATION]
> Choisir un substrat pour lequel seule la SN2 est possible, et représenter un profil réactionnel cohérent avec un mécanisme en une étape.

#### Solution

Le DMSO est un solvant **polaire aprotique** : il solvate bien les cations par interactions ion–dipôle, mais ne solvate **pas** l'anion nucléophile par liaison hydrogène (il n'en donne pas). Le nucléophile est donc « nu », beaucoup plus réactif. Exemple pertinent de $\mathrm{S_N2}$ : l'iodométhane réagit avec l'ion hydroxyde,

$$
\mathrm{CH_3I + HO^- \longrightarrow CH_3OH + I^-}
$$

(le substrat méthylé ne peut donner lieu qu'à une substitution bimoléculaire). Le solvant aprotique abaisse l'énergie d'activation de la réaction : sur le profil réactionnel, une **seule** barrière (mécanisme en une étape), abaissée par rapport à un solvant protique.

> [!PIEGE]
> Un exemple noté « RX » n'est pas accepté : R–CH2Br peut aussi réagir par SN1. Prendre un substrat méthylé (iodométhane + HO−).

> [!JURY]
> Rapport 2025 : « Toute réponse évoquant la baisse de l'énergie d'activation a été acceptée. » Le profil doit rester cohérent avec un mécanisme en une seule étape.

### B. Éco-compatibilité d'un solvant

### Question 6

> [!INDICATION]
> Lire le tableau 1 : pour chaque solvant à remplacer, chercher dans la même catégorie un solvant de score global plus favorable.

> [!INDICATION]
> Vérifier que le remplaçant n'introduit pas de réactivité parasite avec le milieu réactionnel.

#### Solution

a. L'hexane est un hydrocarbure (scores : santé 7, environnement-eau 8). On le remplace par un hydrocarbure de polarité comparable mais mieux noté globalement : le **n-heptane** (santé 4, air 4, eau 7) ou l'isooctane, dans la même catégorie « hydrocarbure ».

b. L'éthoxyéthane est un éther-oxyde (sécurité 9, inflammable). On le remplace par un éther de propriétés physiques voisines et mieux noté, par exemple le **2-méthyltétrahydrofurane** (biosourcé, sécurité 5) ou le CPME. Il ne faut **pas** le remplacer par la propanone : cétone électrophile, elle réagirait dans la synthèse réalisée.

> [!PIEGE]
> On ne remplace pas un éther-oxyde par la propanone : cétone électrophile, elle réagirait dans la synthèse. Rester dans la même catégorie de solvant.

### Question 7

> [!INDICATION]
> À quelle température se déroule le plus souvent une synthèse au laboratoire ?

> [!INDICATION]
> Quel avantage une température d'ébullition modérée apporte-t-elle pour l'élimination du solvant en fin de synthèse ?

#### Solution

La température d'ébullition $T_{\text{éb}}$ fixe le **domaine de température accessible** : la synthèse se mène le plus souvent **à reflux** du solvant, et les vapeurs ne « partent » pas dans la nature. Elle gouverne aussi l'**élimination en fin de synthèse** : un solvant de $T_{\text{éb}}$ modérée s'évapore facilement (séchage sous pression réduite) ou se distille, ce qui facilite sa récupération et son recyclage et limite les pertes et les déchets. Une $T_{\text{éb}}$ trop basse pose des problèmes de volatilité et d'inflammabilité ; trop haute, elle complique l'élimination.

## Partie II — Un solvant pour solubiliser

Dissolution du gypse dans l'eau : du modèle idéal ($K_s$ seule) aux paires d'ions puis à la non-idéalité (Debye-Hückel), avec un titrage EDTA pour valider. Les calculs numériques sont le point délicat.

### Question 8

> [!INDICATION]
> Nommer la nature des interactions entre un ion et une molécule polaire.

> [!INDICATION]
> Schématiser l'orientation des molécules de solvant autour d'un cation, puis autour d'un anion.

#### Solution

Les solvants polaires dispersants solvatent les espèces ioniques par des **interactions électrostatiques de type ion–dipôle** (et non des interactions de van der Waals, qui concernent des molécules neutres). Schéma attendu : autour d'un cation $\mathrm{M^+}$, les molécules de solvant orientent leur pôle $\delta-$ (l'oxygène de l'eau) vers l'ion ; autour d'un anion $\mathrm{X^-}$, elles orientent leur pôle $\delta+$ (les hydrogènes) vers l'ion.

> [!JURY]
> Rapport 2025 : « Il ne s'agit pas d’interactions de Van der Waals qui sont des interactions entre des molécules mais d’interactions de nature électrostatique entre un ion et un dipôle. » Schémas exigés pour un anion ET un cation.

> [!PIEGE]
> Les interactions de van der Waals concernent des molécules neutres ; ici, l'ion interagit avec le dipôle du solvant.

### Question 9

> [!INDICATION]
> Exprimer Ks en fonction des concentrations à l'équilibre, avec la stœchiométrie de la réaction (1).

> [!INDICATION]
> Identifier la relation entre la solubilité s et les concentrations des ions, puis conclure avec l'unité adaptée.

#### Solution

Pour la réaction (1) $\mathrm{CaSO_4\cdot 2H_2O}_{(s)} = \mathrm{Ca}^{2+}_{(aq)} + {\mathrm{SO}_4}^{2-}_{(aq)} + 2\mathrm{H_2O}_{(\ell)}$, l'eau étant le solvant en large excès :

$$
K_s = \frac{[\mathrm{Ca^{2+}}]}{C^\circ}\cdot\frac{[\mathrm{SO_4^{2-}}]}{C^\circ}
$$

À la dissolution, $[\mathrm{Ca^{2+}}] = [\mathrm{SO_4^{2-}}] = s$, d'où $K_s = (s/C^\circ)^2$ :

$$
\boxed{s = C^\circ\sqrt{K_s}}
$$

$$
\boxed{s = \sqrt{2{,}6\times10^{-5}}\ \mathrm{mol\cdot L^{-1}} = 5{,}1\times10^{-3}\ \mathrm{mol\cdot L^{-1}}}
$$

> [!METHODE]
> Toujours écrire Ks avec les concentrations rapportées à C°, identifier la relation imposée par la stœchiométrie, puis donner la solubilité avec son unité (mol·L⁻¹).

### Question 10

> [!INDICATION]
> Adapter la précision de la verrerie au rôle de chaque prélèvement dans le titrage.

> [!INDICATION]
> Quelle verrerie pour un volume qui entre dans les calculs, et pour un volume qui n'y intervient pas ?

#### Solution

- solution de chlorure de magnésium (1 mL) : elle sert à vérifier la concentration de l'EDTA (le blanc), la précision est nécessaire → **pipette jaugée de 1 mL** ;
- filtrat (5 mL) : prise d'essai du titrage → **pipette jaugée de 5 mL** ;
- solution tampon (5 mL) : elle fixe seulement le pH, son volume n'intervient pas dans les calculs → **éprouvette graduée de 5 mL** (une pipette jaugée serait inutile).

> [!JURY]
> Rapport 2025 : « Il ne suffit pas de dire « pipette jaugée » pour tous les prélèvements. » Le volume de tampon n'intervient pas dans les calculs : une éprouvette graduée suffit.

> [!PIEGE]
> Penser au rôle de chaque volume dans le titrage, pas seulement à sa valeur.

### Question 11

> [!INDICATION]
> Déterminer la forme prédominante de l'EDTA au pH du tampon, puis écrire les équations de titrage en faisant intervenir la base du tampon.

> [!INDICATION]
> Combiner les constantes (formation des complexes, acidité de l'EDTA et du tampon) et commenter le caractère quantitatif.

#### Solution

Au pH 10 du tampon ammoniacal ($pK_a(\mathrm{NH_4^+/NH_3}) = 9{,}2$), entre $pK_{a3} = 6{,}2$ et $pK_{a4} = 10{,}2$, la forme **prédominante** de l'EDTA est $\mathrm{HY^{3-}}$. Le proton libéré est capté par la base du tampon, $\mathrm{NH_3}$ :

$$
\mathrm{Ca^{2+} + HY^{3-} + NH_3 = CaY^{2-} + NH_4^+}
$$

$$
\mathrm{Mg^{2+} + HY^{3-} + NH_3 = MgY^{2-} + NH_4^+}
$$

Par combinaison des constantes ($\beta_{\mathrm{CaY}} = 10^{10{,}7}$, $\beta_{\mathrm{MgY}} = 10^{8{,}6}$, $K_{a4} = 10^{-10{,}2}$, $K_a(\mathrm{NH_4^+}) = 10^{-9{,}2}$) :

$$
\boxed{\begin{aligned}
K_{\mathrm{Ca}} &= 10^{10{,}7 - 10{,}2 + 9{,}2} = 10^{9{,}7} \\
K_{\mathrm{Mg}} &= 10^{8{,}6 - 10{,}2 + 9{,}2} = 10^{7{,}6}
\end{aligned}}
$$

Les deux constantes sont très supérieures à $10^4$ : les deux réactions sont **quantitatives**, ce qui légitime leur emploi comme support d'un titrage. Le complexe du calcium est plus stable que celui du magnésium.

> [!JURY]
> Rapport 2025 : « l'écriture d'une équation de réaction modélisant le titrage et tenant compte du pH imposé par la solution tampon n'est que très exceptionnellement réussie. »

> [!PIEGE]
> Dans un couple acide/base, l’espèce prédominante est celle de concentration la plus élevée. Elle est majoritaire si elle représente plus de la moitié de la quantité considérée ; un rapport de dix n’est pas la définition de « majoritaire ».

### Question 12

> [!INDICATION]
> Interpréter le blanc (eau à la place du filtrat) : quels ions sont titrés ?

> [!INDICATION]
> Par différence des volumes équivalents, remonter à la quantité de Ca2+ dans la prise d'essai, puis comparer à la question 9.

#### Solution

Le blanc ($V_e = 2{,}5$ mL) titre uniquement l'ion magnésium introduit :

$$
\begin{aligned}
n_{\mathrm{Mg}} &= C_{\mathrm{EDTA}} V_e \\
&= 0{,}010 \times 2{,}5\times10^{-3} = 2{,}5\times10^{-5}\ \mathrm{mol}
\end{aligned}
$$

cohérent avec $1\ \mathrm{mL}$ de $\mathrm{MgCl_2}$ à $0{,}025\ \mathrm{mol\cdot L^{-1}}$. Avec le filtrat ($V_e = 9{,}5$ mL), l'EDTA titre $\mathrm{Mg^{2+}}$ et $\mathrm{Ca^{2+}}$ :

$$
\begin{aligned}
n_{\mathrm{Ca}} &= C_{\mathrm{EDTA}}(V_e - V_{e,\text{blanc}}) \\
&= 0{,}010 \times (9{,}5 - 2{,}5)\times10^{-3} = 7{,}0\times10^{-5}\ \mathrm{mol}
\end{aligned}
$$

pour une prise d'essai de 5 mL, d'où :

$$
\boxed{[\mathrm{Ca^{2+}}]_{\text{sat}} = \frac{7{,}0\times10^{-5}}{5{,}0\times10^{-3}} = 1{,}4\times10^{-2}\ \mathrm{mol\cdot L^{-1}}}
$$

Cette valeur expérimentale est environ 2,7 fois plus grande que celle de la question 9 ($5{,}1\times10^{-3}\ \mathrm{mol\cdot L^{-1}}$) : le modèle simple de la réaction (1) seule **sous-estime nettement** la solubilité, la modélisation doit être enrichie.

> [!METHODE]
> Le blanc (eau à la place du filtrat) titre le seul Mg2+ introduit : il calibre la solution d'EDTA. La différence des volumes équivalents donne le Ca2+ seul.

### Question 13

> [!INDICATION]
> Déterminer la forme prédominante du NET libre au pH 10 (diagramme de prédominance).

> [!INDICATION]
> Quelle est la couleur du complexe Mg–Ind formé avant l'équivalence, et celle de l'indicateur libre après ?

#### Solution

Au pH 10, entre $pK_{a2} = 6{,}4$ et $pK_{a3} = 11{,}5$, le NET libre prédomine sous la forme $\mathrm{HInd^{2-}}$, de couleur **bleue**. Avant l'équivalence, une partie du magnésium est complexée à l'indicateur : le complexe $\mathrm{Mg{-}Ind}$ donne une teinte **rose-violet**. À l'équivalence, l'EDTA capte le dernier $\mathrm{Mg^{2+}}$ et libère l'indicateur $\mathrm{HInd^{2-}}$ :

$$
\boxed{\text{virage attendu : rose-violet} \longrightarrow \text{bleu}}
$$

### Question 14

> [!INDICATION]
> Quel effet un surplus de Mg2+ a-t-il sur le volume équivalent ?

> [!INDICATION]
> Quel rôle joue l'ion Mg2+ dans le fonctionnement de l'indicateur coloré ?

#### Solution

Ajouter 5 mL de $\mathrm{MgCl_2}$ au lieu de 1 mL **augmente le volume équivalent** $V_e$ : l'excès de $\mathrm{Mg^{2+}}$ est lui aussi titré par l'EDTA, ce qui le met en évidence. Surtout, l'ion magnésium est indispensable au fonctionnement de l'indicateur (formation du complexe coloré $\mathrm{Mg{-}Ind}$) : en augmenter la quantité améliore la **netteté du virage** et la précision du titrage (erreur relative plus faible sur un $V_e$ plus grand).

### Question 15

> [!INDICATION]
> Écrire les deux constantes d'équilibre en fonction des concentrations, avec la contrainte de stœchiométrie de la dissolution.

> [!INDICATION]
> Exprimer la solubilité s comme la somme des deux espèces dissoutes, puis comparer au titrage.

#### Solution

La dissolution impose l'égalité des concentrations en calcium et en sulfate libres : $[\mathrm{Ca^{2+}}] = [\mathrm{SO_4^{2-}}] = x$. La réaction (1) donne $x^2/(C^\circ)^2 = K_s$, soit $x = C^\circ\sqrt{K_s}$. La réaction (2) donne, pour la paire d'ions :

$$
\frac{[(\mathrm{Ca^{2+},SO_4^{2-}})]}{C^\circ} = K_2\,K_s
$$

La solubilité est $s = [\mathrm{Ca^{2+}}] + [(\mathrm{Ca^{2+},SO_4^{2-}})]$ :

$$
\boxed{s = C^\circ\left(\sqrt{K_s} + K_2 K_s\right)}
$$

$$
\boxed{s = 5{,}1\times10^{-3} + 2{,}0\times10^{2}\times2{,}6\times10^{-5} = 1{,}0\times10^{-2}\ \mathrm{mol\cdot L^{-1}}}
$$

Le modèle avec paires d'ions se rapproche nettement de la valeur titrée ($1{,}4\times10^{-2}\ \mathrm{mol\cdot L^{-1}}$) mais la sous-estime encore : il faudra tenir compte de la non-idéalité de la solution.

> [!METHODE]
> Combiner les deux équilibres : la dissolution impose [Ca2+] = [SO4 2−], et la solubilité compte les deux espèces dissoutes (ions libres + paire).

### Question 16

> [!INDICATION]
> Définir l'effet d'ion commun et son sens sur la solubilité.

> [!INDICATION]
> Quels ions le NaCl apporte-t-il ? Sont-ils communs avec ceux du gypse ? Le sens de l'effet attendu correspond-il à l'observation ?

#### Solution

L'**effet d'ion commun** s'observe lors de la dissolution d'un sel ionique dans une solution contenant déjà l'un de ses **ions constitutifs** : par déplacement de l'équilibre de dissolution, il **diminue** la solubilité du sel. Ici, le chlorure de sodium apporte $\mathrm{Na^+}$ et $\mathrm{Cl^-}$, qui ne sont **pas** des ions constitutifs du gypse ($\mathrm{Ca^{2+}}$, $\mathrm{SO_4^{2-}}$) : il n'y a donc pas d'effet d'ion commun. De plus, l'effet attendu serait une *diminution* de la solubilité, alors que l'on constate une *augmentation* : l'effet d'ion commun ne permet pas d'expliquer la variation observée.

### Question 17

> [!INDICATION]
> Écrire le potentiel chimique dans le cas idéal, puis introduire le coefficient d'activité.

> [!INDICATION]
> Quelle est l'unité de l'activité ?

#### Solution

Cas idéal (solution infiniment diluée) :

$$
\mu_i(T,P,C_i) = \mu_i^{\,\circ}(T) + RT\ln\!\left(\frac{C_i}{C^\circ}\right)
$$

Cas réel, en introduisant le coefficient d'activité $\gamma_i$ :

$$
\boxed{\mu_i(T,P,C_i) = \mu_i^{\,\circ}(T) + RT\ln a_i = \mu_i^{\,\circ}(T) + RT\ln\!\left(\gamma_i\frac{C_i}{C^\circ}\right)}
$$

avec l'activité $a_i = \gamma_i\,C_i/C^\circ$. L'activité et le coefficient d'activité sont **sans dimension**.

### Question 18

> [!INDICATION]
> Calculer la force ionique dans chaque cas, puis choisir la formule de Debye-Hückel adaptée au domaine de force ionique.

> [!INDICATION]
> Calculer les coefficients d'activité et conclure sur le caractère idéal ou non de la solution saturée.

#### Solution

*Eau permutée* ($[\mathrm{Ca^{2+}}] = [\mathrm{SO_4^{2-}}] = 1{,}4\times10^{-2}\ \mathrm{mol\cdot L^{-1}}$) :

$$
F = \frac12\left(1{,}4\times10^{-2}\times 2^2 + 1{,}4\times10^{-2}\times 2^2\right) = 5{,}6\times10^{-2}\ \mathrm{mol\cdot L^{-1}}
$$

*F = 0,33 mol·L⁻¹ dans l'eau salée* ($[\mathrm{Ca^{2+}}] = 2{,}1\times10^{-2}$, plus $\mathrm{Na^+}$ et $\mathrm{Cl^-}$ à 0,25) :

$$
F = \frac12\left(2\times 2{,}1\times10^{-2}\times 2^2 + 0{,}25 + 0{,}25\right) = 0{,}33\ \mathrm{mol\cdot L^{-1}}
$$

Dans les deux cas $F > 10^{-2}\ \mathrm{mol\cdot L^{-1}}$ (et $F < 1$) : on applique la formule étendue de Debye-Hückel, avec $z^2 = 4$ :

$$
\log\gamma = -\frac12 z^2\left(\frac{\sqrt{F/C^\circ}}{1 + \sqrt{F/C^\circ}} - 0{,}3\,\frac{F}{C^\circ}\right)
$$

- eau permutée : $\sqrt{F} = 0{,}237$, d'où $\log\gamma = -0{,}35$ et $\boxed{\gamma(\mathrm{Ca^{2+}}) = \gamma(\mathrm{SO_4^{2-}}) \approx 0{,}45}$ ;
- eau salée : $\sqrt{F} = 0{,}58$, d'où $\log\gamma = -0{,}53$ et $\boxed{\gamma \approx 0{,}29}$.

Les coefficients d'activité sont **très inférieurs à 1** : la solution saturée est fortement **non idéale**, d'autant plus que la force ionique est grande (cas de l'eau salée).

> [!METHODE]
> Vérifier à chaque fois la force ionique pour choisir entre la formule diluée (F < 10⁻²) et la formule étendue (F < 1 mol·L⁻¹) de Debye-Hückel.

### Question 19

> [!INDICATION]
> Écrire la loi d'action de masse en activités pour la réaction (1).

> [!INDICATION]
> Si la force ionique augmente, comment évolue γ, et que faut-il pour que Ks reste constante ?

#### Solution

La loi de Guldberg et Waage s'écrit avec les **activités** :

$$
K_s = a(\mathrm{Ca^{2+}})\,a(\mathrm{SO_4^{2-}}) = \gamma^2\,\frac{[\mathrm{Ca^{2+}}][\mathrm{SO_4^{2-}}]}{(C^\circ)^2}
$$

$K_s$ est une constante thermodynamique. Lorsque du NaCl est ajouté, la force ionique augmente et $\gamma$ **diminue** (question 18) ; pour maintenir le produit des activités constant, le produit $[\mathrm{Ca^{2+}}][\mathrm{SO_4^{2-}}]$ doit donc **augmenter** : la solubilité du gypse **croît** en présence de chlorure de sodium. Le modèle de Debye-Hückel explique ainsi l'évolution observée.

> [!METHODE]
> Raisonner en activités : Ks = a(Ca2+)·a(SO4 2−) reste constante, donc si γ diminue, les concentrations doivent augmenter.

### Question 20

> [!INDICATION]
> Reprendre le calcul de la solubilité en écrivant Ks et K2 en activités (γ = 1 pour la paire d'ions neutre).

> [!INDICATION]
> Comparer aux deux valeurs expérimentales données dans l'énoncé.

#### Solution

En écrivant les deux constantes en activités ($\gamma_{\text{paire}} = 1$ pour l'espèce neutre) :

$$
K_s = \gamma^2\frac{[\mathrm{Ca^{2+}}]^2}{(C^\circ)^2}
$$

$$
K_2 = \frac{[(\mathrm{Ca^{2+},SO_4^{2-}})]/C^\circ}{K_s}
$$

d'où $[\mathrm{Ca^{2+}}] = C^\circ\sqrt{K_s}/\gamma$ et $[(\mathrm{Ca^{2+},SO_4^{2-}})] = K_2 K_s C^\circ = 5{,}2\times10^{-3}\ \mathrm{mol\cdot L^{-1}}$ (inchangé, la paire est neutre). La solubilité $s = [\mathrm{Ca^{2+}}] + [(\mathrm{Ca^{2+},SO_4^{2-}})]$ vaut alors :

- eau permutée ($\gamma = 0{,}45$) : $[\mathrm{Ca^{2+}}] = 5{,}1\times10^{-3}/0{,}45 = 1{,}1\times10^{-2}$, d'où

$$
\boxed{s_{\text{eau}} \approx 1{,}1\times10^{-2} + 5{,}2\times10^{-3} = 1{,}6\times10^{-2}\ \mathrm{mol\cdot L^{-1}}}
$$

- eau salée ($\gamma = 0{,}29$) : $[\mathrm{Ca^{2+}}] = 5{,}1\times10^{-3}/0{,}29 = 1{,}8\times10^{-2}$, d'où

$$
\boxed{s_{\text{sel}} \approx 1{,}8\times10^{-2} + 5{,}2\times10^{-3} = 2{,}3\times10^{-2}\ \mathrm{mol\cdot L^{-1}}}
$$

Ces valeurs reproduisent le bon **ordre de grandeur** des solubilités expérimentales ($1{,}4\times10^{-2}$ et $2{,}1\times10^{-2}\ \mathrm{mol\cdot L^{-1}}$) et leur **augmentation** avec la salinité.

> [!PIEGE]
> Tenir compte à la fois de la non-idéalité (γ sur les ions) et des paires d'ions (espèce neutre, γ = 1).

### Question 21

> [!INDICATION]
> Reprendre les trois niveaux de modélisation et leurs résultats numériques.

> [!INDICATION]
> Conclure sur l'intérêt de la démarche et sur l'accord final avec l'expérience.

#### Solution

La démarche est une modélisation **incrémentale**, validée à chaque étape par confrontation à l'expérience : (i) modèle idéal simple ($s = 5{,}1\times10^{-3}\ \mathrm{mol\cdot L^{-1}}$) très insuffisant ; (ii) ajout des paires d'ions ($1{,}0\times10^{-2}$) : net progrès ; (iii) ajout de la non-idéalité (Debye-Hückel) : accord quantitatif avec le titrage ($1{,}4\times10^{-2}$), y compris l'effet de la salinité ($2{,}1\times10^{-2}$ contre $2{,}3\times10^{-2}$ calculé). Chaque raffinement lève une hypothèse simplificatrice et rapproche le modèle des données : c'est une bonne illustration de la construction progressive d'un modèle.

## Partie III — Un solvant pour extraire

Extraction liquide-liquide : détermination expérimentale des constantes de partage par spectrophotométrie, puis optimisation du nombre d'extractions et lecture d'un code Python. Partie indépendante, bien notée.

### Question 22

> [!INDICATION]
> Comparer les trois molécules de la figure 1 : que change la longueur de la chaîne alkyle sur le N ?

> [!INDICATION]
> Quelles interactions intermoléculaires gouvernent la solubilité dans le cyclohexane apolaire ?

#### Solution

Les trois colorants (figure 1) ne diffèrent que par la longueur des chaînes alkyle portées par l'azote du groupe dialkyamino (méthyle, éthyle, propyle). Plus la chaîne est longue, plus la molécule est **lipophile** et plus les interactions de **dispersion de London** (dipôle induit–dipôle induit) avec le cyclohexane apolaire sont favorables. Ordre de solubilité croissante dans le cyclohexane :

$$
\boxed{\text{rouge méthyle} < \text{rouge éthyle} < \text{rouge propyle}}
$$

### Question 23

> [!INDICATION]
> Où se situe 445 nm par rapport aux spectres d'absorption des trois colorants ?

> [!INDICATION]
> Pourquoi se placer au maximum d'absorbance ?

#### Solution

445 nm correspond au **maximum d'absorption** commun aux trois colorants (coefficients d'absorption molaire élevés). Se placer au maximum maximise la **sensibilité** de la mesure de Beer-Lambert et minimise l'erreur due à une légère imprécision sur la longueur d'onde (plateau au sommet du pic).

### Question 24

> [!INDICATION]
> Comment détermine-t-on expérimentalement un coefficient d'absorption molaire avec une bonne précision ?

> [!INDICATION]
> Penser à la gamme étalon, à la droite d'étalonnage et à la loi de Beer-Lambert.

#### Solution

On prépare une **gamme étalon** de solutions de concentrations connues $C$ du colorant (dilutions précises à la verrerie jaugée), on mesure l'absorbance $A$ à 445 nm dans la même cuve ($\ell = 1{,}0$ cm), on vérifie la linéarité, puis on trace la **droite d'étalonnage** $A = f(C)$.

D'après Beer-Lambert $A = \varepsilon\,\ell\,C$, la pente de la droite (passant par l'origine) vaut $\varepsilon\,\ell$, d'où $\varepsilon = \text{pente}/\ell$. La régression sur plusieurs points assure une bonne précision.

### Question 25

> [!INDICATION]
> Ces colorants azoïques sont-ils sensibles au pH ?

> [!INDICATION]
> Pourquoi travailler en solution tamponnée à pH fixé ?

#### Solution

Ces colorants sont des **indicateurs acido-basiques** (groupe acide carboxylique et chromophore azoïque) : leur état de protonation modifie la délocalisation électronique, donc l'allure du spectre (position de $\lambda_{\max}$ et valeur de $\varepsilon$). Travailler en solution **tamponnée à pH 7,0** fixe la forme prédominante, donc un $\varepsilon$ bien défini et reproductible à 445 nm.

### Question 26

> [!INDICATION]
> Appliquer Beer-Lambert à la phase aqueuse après agitation.

> [!INDICATION]
> Utiliser la conservation de la matière avec les volumes des deux phases (égaux ici) pour trouver la phase organique.

#### Solution

Par Beer-Lambert dans la phase aqueuse ($\ell = 1{,}0$ cm) : $[\mathrm{E}]_{aq} = A/(\varepsilon\,\ell)$. Les volumes des deux phases étant égaux ($3{,}0$ mL), la conservation de la matière $C_0 V_{aq} = [\mathrm{E}]_{aq}V_{aq} + [\mathrm{E}]_{org}V_{org}$ donne $[\mathrm{E}]_{org} = C_0 - [\mathrm{E}]_{aq}$, avec $C_0 = 33\ \mu\mathrm{mol\cdot L^{-1}} = 3{,}3\times10^{-5}\ \mathrm{mol\cdot L^{-1}}$ :

| | $[\mathrm{E}]_{aq}$ ($\mathrm{mol\cdot L^{-1}}$) | $[\mathrm{E}]_{org}$ ($\mathrm{mol\cdot L^{-1}}$) |
|---|---|---|
| Rouge méthyle ($A = 0{,}438$, $\varepsilon = 21{,}9\times10^{3}$) | $2{,}0\times10^{-5}$ | $1{,}3\times10^{-5}$ |
| Rouge éthyle ($A = 0{,}247$, $\varepsilon = 19{,}0\times10^{3}$) | $1{,}3\times10^{-5}$ | $2{,}0\times10^{-5}$ |
| Rouge propyle ($A = 0{,}151$, $\varepsilon = 25{,}1\times10^{3}$) | $6{,}0\times10^{-6}$ | $2{,}7\times10^{-5}$ |

### Question 27

> [!INDICATION]
> Exprimer K à partir des concentrations à l'équilibre dans les deux phases.

> [!INDICATION]
> Application numérique pour chacun des trois colorants.

#### Solution

La constante de partage est définie sur les concentrations à l'équilibre, $K = [\mathrm{E}]_{org}/[\mathrm{E}]_{aq}$ :

$$
\boxed{\begin{aligned}
K_{\text{méthyle}} &= \frac{1{,}3\times10^{-5}}{2{,}0\times10^{-5}} = 0{,}65 \\
K_{\text{éthyle}} &= \frac{2{,}0\times10^{-5}}{1{,}3\times10^{-5}} = 1{,}5 \\
K_{\text{propyle}} &= \frac{2{,}7\times10^{-5}}{6{,}0\times10^{-6}} = 4{,}5
\end{aligned}}
$$

### Question 28

> [!INDICATION]
> Comparer l'évolution de K avec la longueur de chaîne à la prévision de la question 22.

> [!INDICATION]
> Quelle interaction intermoléculaire explique cette tendance ?

#### Solution

$K$ croît avec la longueur de la chaîne carbonée ($0{,}65 < 1{,}5 < 4{,}5$) : le colorant le plus lipophile est le plus extrait vers la phase organique. Cela **confirme** la prévision de la question 22, gouvernée par les interactions de dispersion avec le cyclohexane.

### Question 29

> [!INDICATION]
> Définir K sur les concentrations, puis écrire la conservation de la matière avec les volumes V0 et V des deux phases.

> [!INDICATION]
> Exprimer le rendement comme la fraction d'espèce extraite.

#### Solution

À l'équilibre, $K = [\mathrm{E}]_{org}/C_1$, soit $[\mathrm{E}]_{org} = K\,C_1$. La conservation de la matière s'écrit avec les **volumes** des deux phases (l'espèce E est initialement tout entière en phase aqueuse) :

$$
C_0 V_0 = C_1 V_0 + [\mathrm{E}]_{org}\,V = C_1 V_0 + K C_1 V
$$

d'où :

$$
\boxed{\begin{aligned}
C_1 &= \frac{C_0}{1 + K\,\dfrac{V}{V_0}} \\
\rho_1 &= \frac{C_0 V_0 - C_1 V_0}{C_0 V_0} = 1 - \frac{1}{1 + K\,\dfrac{V}{V_0}}
\end{aligned}}
$$

> [!JURY]
> Rapport 2025 : « Il est nécessaire d’écrire la conservation de matière en tenant compte des volumes des deux phases pour répondre correctement à la question. »

> [!PIEGE]
> Définir la constante de partage sur les concentrations, pas sur les quantités de matière ; ne pas « bricoler » la formule fournie.

### Question 30

> [!INDICATION]
> Appliquer deux fois le résultat de la question 29, avec le volume V/2 à chaque extraction.

> [!INDICATION]
> Généraliser l'itération à N extractions.

#### Solution

Chaque extraction unitaire utilise le volume $V/2$. En appliquant deux fois le résultat de la question 29 :

$$
\boxed{\begin{aligned}
C_2 &= C_0\left(\frac{1}{1 + K\,\dfrac{V}{2V_0}}\right)^{2} \\
\rho_2 &= 1 - \left(\frac{1}{1 + K\,\dfrac{V}{2V_0}}\right)^{2}
\end{aligned}}
$$

### Question 31

> [!INDICATION]
> Étudier le sens de variation de ρN en fonction du rapport V/V0, à N et K fixés.

> [!INDICATION]
> Conclure : vaut-il mieux un volume total de solvant organique grand ou petit devant V0 ?

#### Solution

Pour $N$ fixé, $\rho_N = 1 - \left(1 + K\dfrac{V}{N V_0}\right)^{-N}$ est une fonction **croissante** du rapport $V/V_0$. Indépendamment du nombre d'extractions, il est donc préférable d'utiliser un **volume total de solvant organique supérieur au volume de la phase aqueuse** :

$$
\boxed{V > V_0}
$$

### Question 32

> [!INDICATION]
> Quelle grandeur la figure 3 représente-t-elle (pourcentage d'espèce non extraite) ?

> [!INDICATION]
> Modifier la fonction tracée (lignes 15–16), son appel dans la boucle (ligne 21) et la légende de l'axe des ordonnées (ligne 23).

#### Solution

La proportion d'espèce E non extraite après $N$ extractions est $C_N/C_0 = \left(1 + K\dfrac{V}{N V_0}\right)^{-N}$. Les lignes 15, 16, 21 et 23 du code sont modifiées en :

```python
15  def pourcent(K, N):
16      return 100 * (1 + K * V/(N*V0))**(-N)
...
21      plt.plot(K, pourcent(K, n), label=f'N = {n}')
...
23  plt.ylabel("Pourcentage de E non extrait (%)")
```

> [!METHODE]
> La proportion non extraite vaut C_N/C_0 : il suffit de tracer 100·(1 + K·V/(N·V0))**(−N) au lieu du rapport ρ_N/ρ_1.

### Question 33

> [!INDICATION]
> Lire les figures 2 et 3 pour K = 30 puis pour K = 5.

> [!INDICATION]
> Arbitrer entre le gain de rendement apporté par N et le temps que prend chaque extraction liquide-liquide.

#### Solution

- Pour $K = 30$ : même une extraction unique ($N = 1$) laisse quasiment plus d'espèce E en phase aqueuse (figure 3), et $\rho_N/\rho_1 \approx 1$ (figure 2) : multiplier les extractions n'apporte presque rien. **Une extraction unique suffit** (gain de temps, une extraction liquide-liquide prenant du temps).
- Pour $K = 5$ : $\rho_N/\rho_1$ est nettement supérieur à 1 et le pourcentage restant chute fortement avec $N$ : il est **avantageux de fractionner**, par exemple **$N = 3$ extractions** (compromis gain de rendement / temps opératoire).

## Partie IV — Synthèse du Pro-Xylane® dans l'eau

La réaction de Lubineau sur le D-glucose en milieu aqueux basique, mécanismes en milieu basique, puis la réduction stéréosélective du C-glycoside (tableau comparatif des réducteurs). Attention aux flèches courbes et au classement CIP.

### A. Réaction de Lubineau

### Question 34

> [!INDICATION]
> Relever les fonctions portées par chaque carbone de la forme cyclique du glucose.

> [!INDICATION]
> Le carbone anomère porte deux atomes d'oxygène : de quelle famille de fonction s'agit-il ?

#### Solution

Dans la forme cyclique A du D-glucose, on reconnaît des fonctions **alcool** (un alcool primaire $-\mathrm{CH_2OH}$ et des alcools secondaires) et, au carbone anomère, une fonction **hémiacétal** (carbone portant simultanément $-\mathrm{OH}$ et $-\mathrm{OR}$). Ce n'est **pas** un éther-oxyde : la réactivité est totalement différente.

### Question 35

> [!INDICATION]
> Quel est le rôle d'un lavage du milieu réactionnel à l'acétate d'éthyle ?

> [!INDICATION]
> Quel est le rôle d'une résine échangeuse de cations sous forme acide ? (Signaler la coquille de l'énoncé si vous la repérez.)

#### Solution

L'**acétate d'éthyle** sert à **laver** la phase aqueuse : par extraction liquide-liquide, il élimine l'excès de pentane-2,4-dione et les sous-produits organiques. La **résine Dowex 50X-200** (échangeuse de cations sous forme acide) sert à **neutraliser la phase aqueuse** (et non la phase organique, malgré la coquille de l'énoncé) : elle capte les cations $\mathrm{Na^+}$ et élimine l'hydrogénocarbonate résiduel.

> [!JURY]
> Rapport 2025 : « Étant donnée la coquille d’énoncé, la notation de cette question a été très large et toute réponse raisonnable a été acceptée. » La résine neutralise la phase aqueuse, pas la phase organique.

> [!PIEGE]
> Signaler la coquille sur la copie, comme le demande l'énoncé, plutôt que de la propager.

### Question 36

> [!INDICATION]
> Lister les étapes du protocole juste avant « concentrated in vacuo ».

> [!INDICATION]
> Quelle espèce solide faut-il éliminer avant d'évaporer l'eau sous pression réduite ?

#### Solution

Avant l'étape « concentrated in vacuo » (évaporation de l'eau sous pression réduite), il faut **filtrer** le milieu pour éliminer la résine solide (étape « filtered » du protocole). Le produit, hydrophile, reste en phase aqueuse : un séchage sur sel anhydre serait hors propos.

### Question 37

> [!INDICATION]
> Choisir quatre arguments parmi les douze principes de la chimie verte réellement illustrés par cette réaction.

> [!INDICATION]
> Penser solvant, réactifs, rendement, matière première, déchets.

#### Solution

Quatre arguments de chimie verte : (1) **solvant eau**, non toxique et ininflammable ; (2) rendement **quantitatif** (excellente économie d'atomes, quasi pas de déchets) ; (3) **matière première renouvelable** (glucose/xylose issus de la biomasse) ; (4) conditions **douces** : base faible $\mathrm{NaHCO_3}$, pas de catalyseur toxique, pas de groupement protecteur à installer ni à éliminer.

### Question 38

> [!INDICATION]
> Comparer les configurations des deux carbones anomères de A1 et A2.

> [!INDICATION]
> Quel lien stéréochimique relie deux molécules ne différant qu'en un seul stéréocentre ?

#### Solution

$\mathrm{A_1}$ et $\mathrm{A_2}$ ne diffèrent que par la configuration du carbone anomère : ce sont des **anomères**, c'est-à-dire des **diastéréoisomères** (épimères au carbone anomère). Dire « stéréoisomères » seul est insuffisant.

> [!JURY]
> Rapport 2025 : « Dire « stéréoisomères » est insuffisant. Il faut préciser qu’il s’agit de diastéréosiomères. »

### Question 39

> [!INDICATION]
> En milieu basique, comment s'ouvre un hémiacétal cyclique ?

> [!INDICATION]
> Décrire l'ouverture en la forme aldéhydique A0, puis la recyclisation sur l'autre face ; les flèches courbes partent d'un doublet.

#### Solution

En milieu basique, la mutarotation procède par **ouverture de l'hémiacétal** (et non par une substitution nucléophile) : (1) $\mathrm{HO^-}$ déprotone l'hydroxyle anomère ; (2) rupture de la liaison $\mathrm{C{-}O}$ endocyclique, l'oxygène du cycle partant avec son doublet, ce qui libère la forme ouverte aldéhydique $\mathrm{A_0}$ ; (3) libre rotation autour de la liaison C–C adjacente ; (4) recyclisation par attaque de l'alcoolate sur l'autre face du carbonyle ; (5) protonation donnant $\mathrm{A_2}$. Toutes les flèches courbes partent d'un **doublet** d'électrons, conformément au pH basique du milieu.

> [!JURY]
> Rapport 2025 : « les flèches courbes représentent des mouvements de doublets d'électrons ; elles doivent donc prendre leur origine sur un doublet d'électrons, et non sur une charge formelle négative. » Respecter le milieu basique : ouverture de l'hémiacétal, pas une SN.

> [!PIEGE]
> En milieu basique, la mutarotation passe par la forme ouverte A0 (aldéhyde), pas par un carbocation.

### Question 40

> [!INDICATION]
> Quelle grandeur physique, mesurable, permet de suivre les proportions de A1 et A2 à l'équilibre ?

> [!INDICATION]
> Énoncer la loi de Biot en solution, avec les unités de chaque grandeur.

#### Solution

La grandeur mesurable est le **pouvoir rotatoire** $\alpha$ (angle de rotation du plan de polarisation de la lumière), mesuré par polarimétrie. **Loi de Biot** (en solution) :

$$
\boxed{\alpha = [\alpha]_{\lambda}^{T}\cdot\ell\cdot c}
$$

avec $\alpha$ en degrés, $[\alpha]_{\lambda}^{T}$ en $\mathrm{deg\cdot dm^{-1}\cdot(g\cdot mL^{-1})^{-1}}$,
$\ell$ en dm et $c$ en $\mathrm{g\cdot mL^{-1}}$.

À l'équilibre, la rotation est la somme additive des contributions de $\mathrm{A_1}$ et $\mathrm{A_2}$, ce qui donne leurs proportions.

### Question 41

> [!INDICATION]
> Comparer les conformations chaise de A1 et A2 : position (axiale ou équatoriale) des substituants volumineux.

> [!INDICATION]
> L'effet anomère suffit-il à renverser cette conclusion ?

#### Solution

L'espèce majoritaire est celle dont la conformation chaise place le **maximum de substituants volumineux en position équatoriale** : c'est $\mathrm{A_2}$ (β-D-glucopyranose), dont l'hydroxyle anomère et tous les autres substituants sont équatoriaux. L'effet anomère, qui favoriserait la position axiale, ne suffit pas ici à l'emporter sur l'encombrement stérique.

$$
\boxed{\mathrm{A_2}\ \text{(β-D-glucopyranose) est majoritaire à l'équilibre}}
$$

> [!PIEGE]
> L'effet anomère ne suffit pas à expliquer la prédominance de A2 : c'est le maximum de substituants équatoriaux de la chaise qui l'emporte.

### Question 42

> [!INDICATION]
> Estimer l'ordre de grandeur du pKa d'une 1,3-dicétone (CH entre deux carbonyles, énolate stabilisé).

> [!INDICATION]
> Pourquoi choisir HCO3− plutôt que HO− comme base ? Écrire l'équation de déprotonation.

#### Solution

Le carbone central de la pentane-2,4-dione est acide (deux carbonyles accepteurs, énolate stabilisé par mésomérie) :

$$
\boxed{pK_a(\text{pentane-2,4-dione}) \approx 9}
$$

L'ion hydrogénocarbonate $\mathrm{HCO_3^-}$ ($pK_a$ du couple $\mathrm{H_2CO_3/HCO_3^-} \approx 6{,}3$) est une **base douce** : il déprotone suffisamment la dione pour générer l'énolate nucléophile, sans provoquer, comme le ferait l'ion hydroxyde (base forte), les dégradations du sucre (épimérisation, Cannizzaro). Équation de déprotonation :

$$
\boxed{\mathrm{CH_3COCH_2COCH_3 + HCO_3^- = CH_3COCH^-COCH_3 + H_2CO_3\ (\to CO_2 + H_2O)}}
$$

### Question 43

> [!INDICATION]
> Écrire l'énolate de la pentane-2,4-dione, puis son addition nucléophile sur le carbone de l'aldéhyde de A0.

> [!INDICATION]
> Enchaîner déshydratation (E1cb) puis addition 1,4 intramoléculaire d'un hydroxyle du sucre ; donner la formule topologique de B'.

#### Solution

Mécanisme en milieu basique, à partir de la forme ouverte $\mathrm{A_0}$ et de l'énolate de la pentane-2,4-dione : (1) **addition nucléophile** (aldolisation) de l'énolate sur le carbone de l'aldéhyde de $\mathrm{A_0}$ ; (2) **déshydratation** en milieu basique (mécanisme E1cb) donnant l'énone conjuguée (condensation de Knoevenagel) ; (3) **addition nucléophile 1,4 intramoléculaire** (oxa-Michael) d'un hydroxyle du sucre sur l'énone, qui cyclise en pyrane. Le produit $\mathrm{B'}$, de formule brute $\mathrm{C_{11}H_{18}O_7}$ (vérification : $\mathrm{C_6H_{12}O_6 + C_5H_8O_2 - H_2O}$), est le C-glycoside cyclique portant au carbone anomère le groupe $-\mathrm{CH(COCH_3)_2}$.

> [!PIEGE]
> Mécanisme en milieu basique : toutes les flèches partent d'un doublet (énolate, alcoolate), jamais d'une charge formelle négative.

### Question 44

> [!INDICATION]
> Le co-produit éthanoate oriente le mécanisme : de quelle coupure C–C s'agit-il ?

> [!INDICATION]
> Écrire le mécanisme de la rétro-Claisen sur le groupe 1,3-dicétone de B', jusqu'à la cétone B.

#### Solution

Le groupe $-\mathrm{CH(COCH_3)_2}$ de $\mathrm{B'}$ subit une **rétro-Claisen** en milieu basique : $\mathrm{HO^-}$ s'additionne sur l'un des carbonyles (intermédiaire tétraédrique), puis le doublet de l’oxygène reforme le carbonyle tandis que la liaison C–C se rompt : l’espèce partante est l’énolate $-\mathrm{CH^-COCH_3}$ porté par le glycoside, et l’autre fragment est l’acide éthanoïque. Le transfert du proton de cet acide à l’énolate fournit simultanément l’ion éthanoate $\mathrm{CH_3COO^-}$ et la cétone $-\mathrm{CH_2COCH_3}$. On obtient ainsi **B**, la cétone β-C-glycosidique.

### B. Synthèse du Pro-Xylane®

### Question 45

> [!INDICATION]
> Lister les quatre substituants du carbone réduit et les classer selon les règles CIP.

> [!INDICATION]
> Sur la figure 4, placer le H (priorité 4) vers l'arrière, puis lire le sens 1 → 2 → 3.

#### Solution

Le carbone mis en jeu est le carbone de la fonction cétone réduite en alcool (portant $-\mathrm{OH}$, $-\mathrm{CH_3}$, $-\mathrm{H}$ et $-\mathrm{CH_2-}$pyranosyle).

Classement CIP : $-\mathrm{OH}$ (O) priorité **1** ; $-\mathrm{CH_2-}$pyranosyle, dont le premier carbone est lié à (C, H, H), priorité **2** ; $-\mathrm{CH_3}$, lié à (H, H, H), priorité **3** ; $-\mathrm{H}$ priorité **4**. La lecture sur la structure de la figure 4 (H, priorité 4, placé vers l'arrière) donne, en tournant de 1 vers 2 vers 3 dans le sens anti-horaire :

$$
\boxed{\text{stéréodescripteur du stéréoisomère majoritaire : } (S)}
$$

> [!PIEGE]
> Dire « R » ou « S » ne suffit pas : il faut donner et justifier le classement CIP des quatre substituants (1 = OH, 2 = CH2–pyranosyle, 3 = CH3, 4 = H).

### Question 46

> [!INDICATION]
> Définir l'excès diastéréoisomérique par analogie avec l'excès énantiomérique.

> [!INDICATION]
> En déduire le pourcentage du diastéréoisomère majoritaire pour ed = 6 %.

#### Solution

Par analogie avec l'excès énantiomérique, l'**excès diastéréoisomérique** est $ed = |\,\%_{\text{maj}} - \%_{\text{min}}\,|$, avec $\%_{\text{maj}} + \%_{\text{min}} = 100$. Pour l'essai 1 ($ed = 6\ \%$) :

$$
\boxed{\%_{\text{maj}} = \frac{100 + ed}{2} = 53\ \%}
$$

(et $\%_{\text{min}} = 47\ \%$).

### Question 47

> [!INDICATION]
> Écrire l'équation ajustée de la réaction entre NaBH4 et un composé protique (penser au dihydrogène libéré).

> [!INDICATION]
> Comparer les résultats des essais 5 et 6 du tableau 4 pour conclure sur l'espèce réellement réductrice.

#### Solution

Le tétrahydroborate de sodium est basique : en présence d'un composé protique comme l'acide éthanoïque, chaque hydrure $\mathrm{H^-}$ rencontre un proton et libère du dihydrogène. Équation ajustée de formation du triacétoxyborohydrure :

$$
\boxed{\mathrm{NaBH_4 + 3\,CH_3COOH \longrightarrow NaBH(OCOCH_3)_3 + 3\,H_2}}
$$

L'essai 6 met en œuvre directement $\mathrm{NaBH(OAc)_3}$ (sans acide ajouté) et conduit à un excès diastéréoisomérique de 92 %, voisin de celui de l'essai 5 ($\mathrm{NaBH_4}$ + AcOH, 90 %) : cela **confirme** que le triacétoxyborohydrure se forme in situ dans l'essai 5, réducteur plus doux et plus diastéréosélectif que $\mathrm{NaBH_4}$.

> [!PIEGE]
> NaBH4 est basique : en présence d'un composé protique, il libère du dihydrogène — l'équation doit être ajustée.

### Question 48

> [!INDICATION]
> Relever les avantages de l'essai 9 (H2, Ru/C, eau) : solvant, catalyseur, réducteur, déchets, coût.

> [!INDICATION]
> Un ed nul est-il rédhibitoire à l'échelle industrielle ?

#### Solution

L'essai 9 ($\mathrm{H_2}$, catalyseur $\mathrm{Ru/C}$, solvant eau) est retenu industriellement car : (i) le **solvant est l'eau**, éco-compatible ; (ii) le catalyseur est **hétérogène** : il est facilement récupéré par filtration et **recyclable** ; (iii) le réducteur $\mathrm{H_2}$ est économique et assure une forte **économie d'atomes** (pas de déchet boré à traiter) ; (iv) le rendement reste bon (82 %). L'absence de diastéréosélectivité ($ed = 0$) n'est pas rédhibitoire à l'échelle du procédé si le mélange est utilisable.

## Partie V — Synthèse d'un précurseur de Grandifloracine dans l'eau

Synthèse one-pot d'un précurseur de la grandifloracine : clivage periodate de l'alcool salicylique, déaromatisation, dimérisation de Diels-Alder, et spectroscopies IR/RMN. Partie la plus difficile (Q58–Q60).

### Question 49

> [!INDICATION]
> Donner la définition rigoureuse d'une synthèse monotope (« one-pot »).

> [!INDICATION]
> Quels processus coûteux évite-t-on ainsi ?

#### Solution

Une synthèse **monotope** (« one-pot ») est une synthèse dans laquelle un réactif subit plusieurs transformations successives et/ou simultanées **dans un seul réacteur** (un seul mélange réactionnel), en évitant les longs processus de séparation et de purification des espèces intermédiaires.

### Question 50

> [!INDICATION]
> Comparer les fonctions de I (deux époxydes) et de F (deux esters benzoate).

> [!INDICATION]
> Quel nucléophile porteur du groupe benzoyle ouvre les époxydes ?

#### Solution

La grandifloracine F porte deux esters benzoate là où le diépoxyde I porte deux époxydes : il faut ouvrir les deux époxydes par un nucléophile porteur du groupe benzoyle. Séquence proposée : traiter le diépoxyde I par le **benzoate de sodium** $\mathrm{PhCOO^-Na^+}$ en milieu aqueux ; les ions carboxylate ouvrent (régiosélectivement) les deux époxydes et installent les deux esters benzoate, donnant F. (Un organomagnésien porteur d'une fonction ester est à proscrire : il serait détruit.)

### Question 51

> [!INDICATION]
> Combien de fonctions O–H porte G ?

> [!INDICATION]
> D'où vient la largeur des bandes d'élongation O–H en spectroscopie IR ?

#### Solution

L'alcool salicylique G porte **deux** fonctions O–H (phénol et alcool benzylique primaire). Les deux bandes **larges** à 3420 et $3160\ \mathrm{cm^{-1}}$ sont les vibrations d'élongation O–H de ces deux groupes engagés dans des **liaisons hydrogène** : la largeur traduit la distribution de ces liaisons. La bande la plus basse ($3160\ \mathrm{cm^{-1}}$) est cohérente avec une liaison hydrogène **intramoléculaire** forte entre les deux groupes en ortho.

### Question 52

> [!INDICATION]
> Pour chaque H aromatique b, c, d, e, compter les voisins hydrogène en ortho (couplages 3J).

> [!INDICATION]
> En déduire la multiplicité de chaque signal, sous l'hypothèse de constantes J3 comparables.

#### Solution

Le cycle est 1,2-disubstitué : quatre H aromatiques notés b, c, d, e (b et e aux extrémités, chacun avec un seul voisin hydrogène en ortho ; c et d au milieu, chacun avec deux voisins). En ne retenant que les couplages $^3J$, supposés de même ordre de grandeur :

| Proton | Voisins (couplage $^3J$) | Allure du signal |
|---|---|---|
| b | 1 (c) | **doublet** |
| c | 2 (b et d) | **triplet** (dd) |
| d | 2 (c et e) | **triplet** (dd) |
| e | 1 (d) | **doublet** |

### Question 53

> [!INDICATION]
> Que fait D2O sur les protons labiles d'un spectre de RMN ?

> [!INDICATION]
> En comparant les figures 5 et 6, quels signaux disparaissent, et que devient le signal du CH2 ?

#### Solution

L'ajout de $\mathrm{D_2O}$ échange les **protons labiles** (O–H, N–H) contre du deutérium : les signaux correspondants **disparaissent** du spectre. En comparant les figures 5 et 6, on identifie ainsi les deux signaux d'hydroxyle (celui du phénol vers 9,3 ppm et celui de l'alcool vers 4,9 ppm) ; le signal du $\mathrm{CH_2}$ (f) subsiste et se simplifie (le couplage avec l'OH disparaît : il devient un singulet).

### Question 54

> [!INDICATION]
> Utiliser l'effet mésomère donneur du groupe OH : quelles positions du cycle sont blindées ?

> [!INDICATION]
> Attribuer chaque signal du spectre (δ, multiplicité, intégration) aux protons a–g en justifiant les multiplicités.

#### Solution

L'effet mésomère **donneur (+M)** du groupe OH enrichit le cycle en positions **ortho et para**, ce qui **blinde** les H correspondants (δ plus faibles). Attribution du spectre (400 MHz, DMSO-$d_6$) :

| $\delta$ (ppm) | Multiplicité | Intégration | Attribution | Justification |
|---|---|---|---|---|
| 9,28 | singulet | 1H | a (O–H phénolique) | très déblindé (liaison H), échangeable avec $\mathrm{D_2O}$ |
| 7,29 | doublet | 1H | e (H en ortho de $\mathrm{CH_2OH}$, méta de OH) | peu blindé, un seul voisin $^3J$ |
| 7,03 | doublet de doublets (≈ triplet) | 1H | c (H méta de OH) | deux voisins $^3J$ |
| 6,79 (6,74–6,80) | multiplet (d + dd) | 2H | b (ortho de OH) et d (para de OH) | **blindés par l'effet +M du OH** |
| 4,93 | triplet | 1H | g (O–H de l'alcool) | échangeable avec $\mathrm{D_2O}$, couplé au $\mathrm{CH_2}$ |
| 4,49 | doublet | 2H | f ($\mathrm{CH_2}$) | couplé à l'OH (singulet après ajout de $\mathrm{D_2O}$) |

> [!JURY]
> Rapport 2025 : « L’effet mésomère donneur du groupe OH permet d’expliquer le blindage supplémentaire des hydrogènes situés en alpha et en para du cycle aromatique. »

> [!METHODE]
> Attribuer d'abord les protons échangeables (D2O, figures 5–6), puis les aromatiques du plus déblindé au plus blindé en justifiant multiplicités et intégrations.

### Question 55

> [!INDICATION]
> Décompter les électrons de valence de chaque ion, puis écrire le schéma de Lewis.

> [!INDICATION]
> Appliquer VSEPR (type AXnEm) et estimer les angles entre liaisons.

#### Solution

Après décompte des électrons de valence et schéma de Lewis : $\mathrm{IO_4^-}$ présente 4 liaisons I–O et **aucun doublet non liant** sur l'iode (type $\mathrm{AX_4}$) :

$$
\boxed{\mathrm{IO_4^-}\ :\ \text{géométrie tétraédrique, angles } \approx 109{,}5^\circ}
$$

$\mathrm{IO_3^-}$ présente 3 liaisons I–O et **un doublet non liant** (type $\mathrm{AX_3E}$) :

$$
\boxed{\mathrm{IO_3^-}\ :\ \text{géométrie pyramidale à base triangulaire, angles } \approx 100^\circ < 109{,}5^\circ\ \text{(répulsion du doublet)}}
$$

> [!METHODE]
> Toujours précéder la prévision VSEPR d'un décompte des électrons de valence et d'un schéma de Lewis (compétence de première attendue à l'agrégation).

### Question 56

> [!INDICATION]
> Partir de l'intermédiaire J : quels électrons forment les deux nouvelles liaisons C=O ?

> [!INDICATION]
> Quel est le nombre d'oxydation de l'iode dans J, et dans NaIO3 ? Donner les formules de K et K'.

#### Solution

L'ester periodate cyclique J se fragmente de façon **concertée** : les électrons de la liaison C–C du pinacol forment les deux liaisons $\mathrm{C{=}O}$, tandis que les liaisons C–O–I se rompent et que l'iode est réduit de I(VII) à I(V). Produits organiques : **deux molécules de propanone** $\mathrm{(CH_3)_2C{=}O}$, soit $K = K' =$ propanone, plus $\mathrm{NaIO_3}$.

### Question 57

> [!INDICATION]
> Quelles sont les deux fonctions oxygénées vicinales de G ?

> [!INDICATION]
> Transposer la structure de J au couple phénol / alcool benzylique en ortho.

#### Solution

Le clivage oxydatif exige deux fonctions oxygénées **vicinales**. L'alcool salicylique possède un phénol (C1) et un alcool benzylique (C2) en ortho, analogue d'un 1,2-diol : l'iode ponte les **deux oxygènes** (O phénolique et O benzylique) pour former un **ester periodate cyclique** à cheval sur les positions ortho du cycle aromatique.

> [!METHODE]
> Le clivage periodate exige un motif 1,2-diol (ou deux oxygénés vicinaux) : repérer le couple phénol/alcool benzylique ortho de G.

### Question 58

> [!INDICATION]
> Compter les insaturations de la formule brute C7H6O2.

> [!INDICATION]
> Par analogie avec la fragmentation de J, quelle structure déaromatisée obtient-on ? S'aider de la formule du diépoxyde I.

#### Solution

Par analogie avec J, la réaction de G avec $\mathrm{NaIO_4}$ forme d'abord l'ester periodate cyclique de la question 57, qui se fragmente en provoquant la **déaromatisation** du cycle : H est la **spiro-époxy-cyclohexa-2,5-diénone** — un cycle cyclohexadiénone portant un époxyde dont le centre spiro est le carbone du cycle initialement porteur du groupe hydroxyméthyle ; l’ancien carbone $\mathrm{CH_2OH}$ constitue l’autre carbone de l’époxyde. Vérification : $\mathrm{C_7H_6O_2}$ compte $\frac{2\times7+2-6}{2} = 5$ insaturations (2 C=C + 1 C=O + 2 cycles), et 2 oxygènes (C=O + époxyde).

> [!PIEGE]
> Vérifier la formule brute (5 insaturations) et s'aider de celle du diépoxyde I : H doit contenir l'époxyde pour que la dimérisation donne un diépoxyde.

### Question 59

> [!INDICATION]
> Reconnaître une cycloaddition [4+2] entre deux molécules de H (qui joue le diène, qui le diénophile ?).

> [!INDICATION]
> Décrire le mécanisme concerté : combien d'électrons π déplacés, combien de flèches courbes en cycle ?

#### Solution

Le passage de H à I est une **cycloaddition de Diels-Alder [4+2]** : H se dimérise, une molécule jouant le rôle de **diène** (la partie diénone en conformation s-cis) et l'autre de **diénophile** (l'une des liaisons C=C conjuguées). Le mécanisme est **concerté** et péricyclique : six électrons π se déplacent simultanément (trois flèches courbes en cycle), formant deux liaisons σ C–C et une nouvelle liaison π, via un état de transition cyclique ; le produit est le squelette bicyclo[2.2.2]octène portant les deux époxydes (= I).

> [!METHODE]
> Diels-Alder : mécanisme concerté, péricyclique, à 6 électrons π — trois flèches courbes en cycle, formation simultanée de deux liaisons σ.

### Question 60

> [!INDICATION]
> Quels autres adduits la cycloaddition peut-elle former ?

> [!INDICATION]
> Penser aux autres orientations relatives diène/diénophile (régioisomères) et aux stéréoisomères endo/exo.

#### Solution

La réaction étant fortement régiosélective, les autres adduits possibles sont minoritaires : les **régioisomères** correspondant à l'autre orientation relative du diène et du diénophile (mise en jeu de l'autre liaison C=C de la diénone comme diénophile, orientation « tête-bêche » au lieu de « tête-à-tête »), ainsi que les **stéréoisomères endo/exo** de la cycloaddition. On les représente par le squelette bicyclo[2.2.2]octène correspondant, avec les carbonyles et époxydes disposés selon l'orientation alternative.

> [!PIEGE]
> La régiosélectivité forte signifie que les autres adduits (autre orientation diène/diénophile, endo/exo) sont possibles mais minoritaires : les représenter sans insister.

## Bilan

**Méthodes à retenir.**

- *Solvants* : classer par géométrie (moment dipolaire), permittivité (dispersant) et liaison O–H (protique) ; un solvant polaire aprotique désolvate l'anion nucléophile et accélère la SN2.
- *Dissolution d'un sel* : écrire $K_s$ en activités, empiler les modèles (idéal → paires d'ions → Debye-Hückel) et les valider par un titrage ; le blanc d'un titrage complexe-EDTA calibre la solution via Mg2+.
- *Extraction* : définir la constante de partage sur les **concentrations**, écrire la conservation de la matière avec les **volumes**, et fractionner les extractions quand $K$ est modéré (pour $K$ grand, une seule suffit).
- *Mécanismes organiques* : en milieu basique, flèches courbes depuis un doublet ; mutarotation = ouverture de l'hémiacétal ; réaction de Lubineau = aldolisation + déshydratation + oxa-Michael 1,4 intramoléculaire, puis rétro-Claisen.
- *Spectroscopies* : VSEPR précédé du schéma de Lewis ; RMN : D2O pour repérer les protons labiles, effet +M d'un OH = blindage des positions ortho et para.

**Prérequis à revoir.** Moments dipolaires et géométries moléculaires ; produit de solubilité et titrages complexométriques (formes prédominantes de l'EDTA selon le pH) ; loi de Beer-Lambert et droite d'étalonnage ; stœchiométrie et classements CIP ; VSEPR ; mécanismes réactionnels en milieu basique ; cycloaddition de Diels-Alder.

**Questions classiques transposables.** Le titrage EDTA de Ca2+/Mg2+ en tampon ammoniacal (Q11–Q14) et la modélisation de Debye-Hückel (Q18–Q21) sont des classiques de l'oral comme de l'écrit ; la détermination d'un coefficient de partage et l'optimisation du nombre d'extractions (Q22–Q33) reviennent régulièrement ; le couple clivage periodate / Diels-Alder (Q56–Q60) est un bel exemple de cascade réactionnelle en milieu aqueux.

**Ce que le jury a sanctionné en 2025** (rapport de la session) : les confusions polaire/dispersant et protique/accepteur de liaison H, les exemples de SN2 notés « RX », les interactions ion–dipôle confondues avec van der Waals, l'absence de justification géométrique dans le classement des solvants, les « bricolages » de la formule de rendement, l'oubli du caractère quantitatif des réactions de titrage, et les flèches courbes qui ne partent pas d'un doublet d'électrons.
