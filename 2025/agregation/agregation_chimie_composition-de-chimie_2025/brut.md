# Agrégation Chimie — Composition de chimie 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve A de 5 heures (calculatrice autorisée), sujet « Critères de choix d'un solvant », 60 questions en cinq parties. Les données (constantes d'acidité, de formation, table IR, guide des solvants) sont regroupées en fin d'énoncé. Sauf mention contraire, les constantes d'équilibre sont exprimées avec l'état standard $C^\circ = 1\ \mathrm{mol\cdot L^{-1}}$.

## Partie I — Propriétés générales des solvants

### A. Propriétés physiques des solvants

#### Question 1

L'éthoxyéthane $\mathrm{CH_3CH_2{-}O{-}CH_2CH_3}$ possède un atome d'oxygène porteur de deux doublets non liants : la géométrie autour de O est **coudée** (angle $\mathrm{C{-}O{-}C} \approx 110^\circ$), la molécule n'est pas linéaire. Chaque liaison $\mathrm{C{-}O}$ est polarisée vers l'oxygène plus électronégatif que le carbone : $\mathrm{C^{\delta+}{-}O^{\delta-}}$. La somme vectorielle des deux moments de liaison n'est pas nulle :

$$
\boxed{\vec{\mu} \neq \vec{0}\ :\ \text{moment dipolaire permanent porté par la bissectrice de l'angle } \mathrm{C{-}O{-}C},\ \text{dirigé du pôle négatif (O) vers le pôle positif}}
$$

#### Question 2

La permittivité relative $\varepsilon_r$ divise la force électrostatique de Coulomb entre deux charges par $\varepsilon_r$ : elle mesure le **pouvoir écranteur** du solvant, donc son caractère dispersant (ou ionisant). Avec $\varepsilon_r = 4$ (contre 79 pour l'eau), l'éthoxyéthane écrante très mal les interactions électrostatiques : c'est un solvant **peu dispersant**. Conséquence pour un composé ionique $\mathrm{MX}$ :

$$
\boxed{\mathrm{MX}\ \text{reste sous forme non dissociée, ou au mieux de paires d'ions } (\mathrm{M^+},\mathrm{X^-})\text{, et non } \mathrm{M^+}_{(sol)} + \mathrm{X^-}_{(sol)}}
$$

#### Question 3

Un solvant **protique** est un solvant capable de **donner** une liaison hydrogène, c'est-à-dire qui possède au moins un atome d'hydrogène porté par un atome très électronégatif (O–H, N–H ou F–H). L'éthoxyéthane ne comporte que des liaisons C–H et C–O : il ne peut pas donner de liaison hydrogène.

$$
\boxed{\text{L'éthoxyéthane est un solvant aprotique}}
$$

#### Question 4

Critères de classement : la molécule est **apolaire** si sa géométrie la rend symétrique ($\vec{\mu} = \vec{0}$) ; **polaire** sinon, et l'on distingue **dispersant** (grande permittivité relative, de plusieurs dizaines) de **peu dispersant** ($\varepsilon_r$ faible) ; le solvant est **protique** s'il possède une liaison O–H (ou N–H), **apotique** sinon.

| | Polaire dispersant | Polaire dispersant | Polaire peu dispersant | Polaire peu dispersant | Apolaire |
|---|---|---|---|---|---|
| | Protique | Aprotique | Protique | Aprotique | |
| Solvants | eau (εr = 79) | DMSO (εr = 49), DMF (εr = 37) | acide éthanoïque (εr = 6) | éthoxyéthane (εr = 4), dichlorométhane (εr = 9) | tétrachlorométhane (εr = 2,2) |

Justifications géométriques : l'eau est coudée et possède deux liaisons O–H (protique, très dispersante) ; le DMSO $\mathrm{(CH_3)_2S{=}O}$ et le DMF $\mathrm{HCON(CH_3)_2}$ présentent respectivement une géométrie pyramidale autour de S et plane autour du carbone du carbonyle, fortement polaires et sans liaison O–H (apotiques dispersants) ; l'acide éthanoïque possède une liaison O–H (protique) mais une permittivité faible ; le dichlorométhane est tétraédrique, les deux moments $\mathrm{C{-}Cl}$ ne se compensent pas (polaire, aprotique) ; l'éthoxyéthane est coudé, polaire mais peu dispersant ; le tétrachlorométhane est tétraédrique régulier, les quatre moments $\mathrm{C{-}Cl}$ se compensent :

$$
\boxed{\mathrm{CCl_4}\ \text{est le seul solvant apolaire de la liste } (\vec{\mu} = \vec{0})}
$$

#### Question 5

Le DMSO est un solvant **polaire aprotique** : il solvate bien les cations par interactions ion–dipôle, mais ne solvate **pas** l'anion nucléophile par liaison hydrogène (il n'en donne pas). Le nucléophile est donc « nu », beaucoup plus réactif. Exemple pertinent de $\mathrm{S_N2}$ : l'iodométhane réagit avec l'ion hydroxyde,

$$
\mathrm{CH_3I + HO^- \longrightarrow CH_3OH + I^-}
$$

(le substrat méthylé ne peut donner lieu qu'à une substitution bimoléculaire). Le solvant aprotique abaisse l'énergie d'activation de la réaction : sur le profil réactionnel, une **seule** barrière (mécanisme en une étape), abaissée par rapport à un solvant protique.

### B. Éco-compatibilité d'un solvant

#### Question 6

a. L'hexane est un hydrocarbure (scores : santé 7, environnement-eau 8). On le remplace par un hydrocarbure de polarité comparable mais mieux noté globalement : le **n-heptane** (santé 4, air 4, eau 7) ou l'isooctane, dans la même catégorie « hydrocarbure ».

b. L'éthoxyéthane est un éther-oxyde (sécurité 9, inflammable). On le remplace par un éther de propriétés physiques voisines et mieux noté, par exemple le **2-méthyltétrahydrofurane** (biosourcé, sécurité 5) ou le CPME. Il ne faut **pas** le remplacer par la propanone : cétone électrophile, elle réagirait dans la synthèse réalisée.

#### Question 7

La température d'ébullition $T_{\text{éb}}$ fixe le **domaine de température accessible** : la synthèse se mène le plus souvent **à reflux** du solvant, et les vapeurs ne « partent » pas dans la nature. Elle gouverne aussi l'**élimination en fin de synthèse** : un solvant de $T_{\text{éb}}$ modérée s'évapore facilement (séchage sous pression réduite) ou se distille, ce qui facilite sa récupération et son recyclage et limite les pertes et les déchets. Une $T_{\text{éb}}$ trop basse pose des problèmes de volatilité et d'inflammabilité ; trop haute, elle complique l'élimination.

## Partie II — Un solvant pour solubiliser

(Modélisation croissante de la dissolution du gypse dans l'eau : modèle idéal, paires d'ions, non-idéalité de Debye-Hückel.)

#### Question 8

Les solvants polaires dispersants solvatent les espèces ioniques par des **interactions électrostatiques de type ion–dipôle** (et non des interactions de van der Waals, qui concernent des molécules neutres). Schéma attendu : autour d'un cation $\mathrm{M^+}$, les molécules de solvant orientent leur pôle $\delta-$ (l'oxygène de l'eau) vers l'ion ; autour d'un anion $\mathrm{X^-}$, elles orientent leur pôle $\delta+$ (les hydrogènes) vers l'ion.

#### Question 9

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

#### Question 10

- solution de chlorure de magnésium (1 mL) : elle sert à vérifier la concentration de l'EDTA (le blanc), la précision est nécessaire → **pipette jaugée de 1 mL** ;
- filtrat (5 mL) : prise d'essai du titrage → **pipette jaugée de 5 mL** ;
- solution tampon (5 mL) : elle fixe seulement le pH, son volume n'intervient pas dans les calculs → **éprouvette graduée de 5 mL** (une pipette jaugée serait inutile).

#### Question 11

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

#### Question 12

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

#### Question 13

Au pH 10, entre $pK_{a2} = 6{,}4$ et $pK_{a3} = 11{,}5$, le NET libre prédomine sous la forme $\mathrm{HInd^{2-}}$, de couleur **bleue**. Avant l'équivalence, une partie du magnésium est complexée à l'indicateur : le complexe $\mathrm{Mg{-}Ind}$ donne une teinte **rose-violet**. À l'équivalence, l'EDTA capte le dernier $\mathrm{Mg^{2+}}$ et libère l'indicateur $\mathrm{HInd^{2-}}$ :

$$
\boxed{\text{virage attendu : rose-violet} \longrightarrow \text{bleu}}
$$

#### Question 14

Ajouter 5 mL de $\mathrm{MgCl_2}$ au lieu de 1 mL **augmente le volume équivalent** $V_e$ : l'excès de $\mathrm{Mg^{2+}}$ est lui aussi titré par l'EDTA, ce qui le met en évidence. Surtout, l'ion magnésium est indispensable au fonctionnement de l'indicateur (formation du complexe coloré $\mathrm{Mg{-}Ind}$) : en augmenter la quantité améliore la **netteté du virage** et la précision du titrage (erreur relative plus faible sur un $V_e$ plus grand).

#### Question 15

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

#### Question 16

L'**effet d'ion commun** s'observe lors de la dissolution d'un sel ionique dans une solution contenant déjà l'un de ses **ions constitutifs** : par déplacement de l'équilibre de dissolution, il **diminue** la solubilité du sel. Ici, le chlorure de sodium apporte $\mathrm{Na^+}$ et $\mathrm{Cl^-}$, qui ne sont **pas** des ions constitutifs du gypse ($\mathrm{Ca^{2+}}$, $\mathrm{SO_4^{2-}}$) : il n'y a donc pas d'effet d'ion commun. De plus, l'effet attendu serait une *diminution* de la solubilité, alors que l'on constate une *augmentation* : l'effet d'ion commun ne permet pas d'expliquer la variation observée.

#### Question 17

Cas idéal (solution infiniment diluée) :

$$
\mu_i(T,P,C_i) = \mu_i^{\,\circ}(T) + RT\ln\!\left(\frac{C_i}{C^\circ}\right)
$$

Cas réel, en introduisant le coefficient d'activité $\gamma_i$ :

$$
\boxed{\mu_i(T,P,C_i) = \mu_i^{\,\circ}(T) + RT\ln a_i = \mu_i^{\,\circ}(T) + RT\ln\!\left(\gamma_i\frac{C_i}{C^\circ}\right)}
$$

avec l'activité $a_i = \gamma_i\,C_i/C^\circ$. L'activité et le coefficient d'activité sont **sans dimension**.

#### Question 18

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

#### Question 19

La loi de Guldberg et Waage s'écrit avec les **activités** :

$$
K_s = a(\mathrm{Ca^{2+}})\,a(\mathrm{SO_4^{2-}}) = \gamma^2\,\frac{[\mathrm{Ca^{2+}}][\mathrm{SO_4^{2-}}]}{(C^\circ)^2}
$$

$K_s$ est une constante thermodynamique. Lorsque du NaCl est ajouté, la force ionique augmente et $\gamma$ **diminue** (question 18) ; pour maintenir le produit des activités constant, le produit $[\mathrm{Ca^{2+}}][\mathrm{SO_4^{2-}}]$ doit donc **augmenter** : la solubilité du gypse **croît** en présence de chlorure de sodium. Le modèle de Debye-Hückel explique ainsi l'évolution observée.

#### Question 20

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

#### Question 21

La démarche est une modélisation **incrémentale**, validée à chaque étape par confrontation à l'expérience : (i) modèle idéal simple ($s = 5{,}1\times10^{-3}\ \mathrm{mol\cdot L^{-1}}$) très insuffisant ; (ii) ajout des paires d'ions ($1{,}0\times10^{-2}$) : net progrès ; (iii) ajout de la non-idéalité (Debye-Hückel) : accord quantitatif avec le titrage ($1{,}4\times10^{-2}$), y compris l'effet de la salinité ($2{,}1\times10^{-2}$ contre $2{,}3\times10^{-2}$ calculé). Chaque raffinement lève une hypothèse simplificatrice et rapproche le modèle des données : c'est une bonne illustration de la construction progressive d'un modèle.

## Partie III — Un solvant pour extraire

#### Question 22

Les trois colorants (figure 1) ne diffèrent que par la longueur des chaînes alkyle portées par l'azote du groupe dialkyamino (méthyle, éthyle, propyle). Plus la chaîne est longue, plus la molécule est **lipophile** et plus les interactions de **dispersion de London** (dipôle induit–dipôle induit) avec le cyclohexane apolaire sont favorables. Ordre de solubilité croissante dans le cyclohexane :

$$
\boxed{\text{rouge méthyle} < \text{rouge éthyle} < \text{rouge propyle}}
$$

#### Question 23

445 nm correspond au **maximum d'absorption** commun aux trois colorants (coefficients d'absorption molaire élevés). Se placer au maximum maximise la **sensibilité** de la mesure de Beer-Lambert et minimise l'erreur due à une légère imprécision sur la longueur d'onde (plateau au sommet du pic).

#### Question 24

On prépare une **gamme étalon** de solutions de concentrations connues $C$ du colorant (dilutions précises à la verrerie jaugée), on mesure l'absorbance $A$ à 445 nm dans la même cuve ($\ell = 1{,}0$ cm), on vérifie la linéarité, puis on trace la **droite d'étalonnage** $A = f(C)$.

D'après Beer-Lambert $A = \varepsilon\,\ell\,C$, la pente de la droite (passant par l'origine) vaut $\varepsilon\,\ell$, d'où $\varepsilon = \text{pente}/\ell$. La régression sur plusieurs points assure une bonne précision.

#### Question 25

Ces colorants sont des **indicateurs acido-basiques** (groupe acide carboxylique et chromophore azoïque) : leur état de protonation modifie la délocalisation électronique, donc l'allure du spectre (position de $\lambda_{\max}$ et valeur de $\varepsilon$). Travailler en solution **tamponnée à pH 7,0** fixe la forme prédominante, donc un $\varepsilon$ bien défini et reproductible à 445 nm.

#### Question 26

Par Beer-Lambert dans la phase aqueuse ($\ell = 1{,}0$ cm) : $[\mathrm{E}]_{aq} = A/(\varepsilon\,\ell)$. Les volumes des deux phases étant égaux ($3{,}0$ mL), la conservation de la matière $C_0 V_{aq} = [\mathrm{E}]_{aq}V_{aq} + [\mathrm{E}]_{org}V_{org}$ donne $[\mathrm{E}]_{org} = C_0 - [\mathrm{E}]_{aq}$, avec $C_0 = 33\ \mu\mathrm{mol\cdot L^{-1}} = 3{,}3\times10^{-5}\ \mathrm{mol\cdot L^{-1}}$ :

| | $[\mathrm{E}]_{aq}$ ($\mathrm{mol\cdot L^{-1}}$) | $[\mathrm{E}]_{org}$ ($\mathrm{mol\cdot L^{-1}}$) |
|---|---|---|
| Rouge méthyle ($A = 0{,}438$, $\varepsilon = 21{,}9\times10^{3}$) | $2{,}0\times10^{-5}$ | $1{,}3\times10^{-5}$ |
| Rouge éthyle ($A = 0{,}247$, $\varepsilon = 19{,}0\times10^{3}$) | $1{,}3\times10^{-5}$ | $2{,}0\times10^{-5}$ |
| Rouge propyle ($A = 0{,}151$, $\varepsilon = 25{,}1\times10^{3}$) | $6{,}0\times10^{-6}$ | $2{,}7\times10^{-5}$ |

#### Question 27

La constante de partage est définie sur les concentrations à l'équilibre, $K = [\mathrm{E}]_{org}/[\mathrm{E}]_{aq}$ :

$$
\boxed{\begin{aligned}
K_{\text{méthyle}} &= \frac{1{,}3\times10^{-5}}{2{,}0\times10^{-5}} = 0{,}65 \\
K_{\text{éthyle}} &= \frac{2{,}0\times10^{-5}}{1{,}3\times10^{-5}} = 1{,}5 \\
K_{\text{propyle}} &= \frac{2{,}7\times10^{-5}}{6{,}0\times10^{-6}} = 4{,}5
\end{aligned}}
$$

#### Question 28

$K$ croît avec la longueur de la chaîne carbonée ($0{,}65 < 1{,}5 < 4{,}5$) : le colorant le plus lipophile est le plus extrait vers la phase organique. Cela **confirme** la prévision de la question 22, gouvernée par les interactions de dispersion avec le cyclohexane.

#### Question 29

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

#### Question 30

Chaque extraction unitaire utilise le volume $V/2$. En appliquant deux fois le résultat de la question 29 :

$$
\boxed{\begin{aligned}
C_2 &= C_0\left(\frac{1}{1 + K\,\dfrac{V}{2V_0}}\right)^{2} \\
\rho_2 &= 1 - \left(\frac{1}{1 + K\,\dfrac{V}{2V_0}}\right)^{2}
\end{aligned}}
$$

#### Question 31

Pour $N$ fixé, $\rho_N = 1 - \left(1 + K\dfrac{V}{N V_0}\right)^{-N}$ est une fonction **croissante** du rapport $V/V_0$. Indépendamment du nombre d'extractions, il est donc préférable d'utiliser un **volume total de solvant organique supérieur au volume de la phase aqueuse** :

$$
\boxed{V > V_0}
$$

#### Question 32

La proportion d'espèce E non extraite après $N$ extractions est $C_N/C_0 = \left(1 + K\dfrac{V}{N V_0}\right)^{-N}$. Les lignes 15, 16, 21 et 23 du code sont modifiées en :

```python
15  def pourcent(K, N):
16      return 100 * (1 + K * V/(N*V0))**(-N)
...
21      plt.plot(K, pourcent(K, n), label=f'N = {n}')
...
23  plt.ylabel("Pourcentage de E non extrait (%)")
```

#### Question 33

- Pour $K = 30$ : même une extraction unique ($N = 1$) laisse quasiment plus d'espèce E en phase aqueuse (figure 3), et $\rho_N/\rho_1 \approx 1$ (figure 2) : multiplier les extractions n'apporte presque rien. **Une extraction unique suffit** (gain de temps, une extraction liquide-liquide prenant du temps).
- Pour $K = 5$ : $\rho_N/\rho_1$ est nettement supérieur à 1 et le pourcentage restant chute fortement avec $N$ : il est **avantageux de fractionner**, par exemple **$N = 3$ extractions** (compromis gain de rendement / temps opératoire).

## Partie IV — Synthèse du Pro-Xylane® dans l'eau

### A. Réaction de Lubineau

#### Question 34

Dans la forme cyclique A du D-glucose, on reconnaît des fonctions **alcool** (un alcool primaire $-\mathrm{CH_2OH}$ et des alcools secondaires) et, au carbone anomère, une fonction **hémiacétal** (carbone portant simultanément $-\mathrm{OH}$ et $-\mathrm{OR}$). Ce n'est **pas** un éther-oxyde : la réactivité est totalement différente.

#### Question 35

L'**acétate d'éthyle** sert à **laver** la phase aqueuse : par extraction liquide-liquide, il élimine l'excès de pentane-2,4-dione et les sous-produits organiques. La **résine Dowex 50X-200** (échangeuse de cations sous forme acide) sert à **neutraliser la phase aqueuse** (et non la phase organique, malgré la coquille de l'énoncé) : elle capte les cations $\mathrm{Na^+}$ et élimine l'hydrogénocarbonate résiduel.

#### Question 36

Avant l'étape « concentrated in vacuo » (évaporation de l'eau sous pression réduite), il faut **filtrer** le milieu pour éliminer la résine solide (étape « filtered » du protocole). Le produit, hydrophile, reste en phase aqueuse : un séchage sur sel anhydre serait hors propos.

#### Question 37

Quatre arguments de chimie verte : (1) **solvant eau**, non toxique et ininflammable ; (2) rendement **quantitatif** (excellente économie d'atomes, quasi pas de déchets) ; (3) **matière première renouvelable** (glucose/xylose issus de la biomasse) ; (4) conditions **douces** : base faible $\mathrm{NaHCO_3}$, pas de catalyseur toxique, pas de groupement protecteur à installer ni à éliminer.

#### Question 38

$\mathrm{A_1}$ et $\mathrm{A_2}$ ne diffèrent que par la configuration du carbone anomère : ce sont des **anomères**, c'est-à-dire des **diastéréoisomères** (épimères au carbone anomère). Dire « stéréoisomères » seul est insuffisant.

#### Question 39

En milieu basique, la mutarotation procède par **ouverture de l'hémiacétal** (et non par une substitution nucléophile) : (1) $\mathrm{HO^-}$ déprotone l'hydroxyle anomère ; (2) rupture de la liaison $\mathrm{C{-}O}$ endocyclique, l'oxygène du cycle partant avec son doublet, ce qui libère la forme ouverte aldéhydique $\mathrm{A_0}$ ; (3) libre rotation autour de la liaison C–C adjacente ; (4) recyclisation par attaque de l'alcoolate sur l'autre face du carbonyle ; (5) protonation donnant $\mathrm{A_2}$. Toutes les flèches courbes partent d'un **doublet** d'électrons, conformément au pH basique du milieu.

#### Question 40

La grandeur mesurable est le **pouvoir rotatoire** $\alpha$ (angle de rotation du plan de polarisation de la lumière), mesuré par polarimétrie. **Loi de Biot** (en solution) :

$$
\boxed{\alpha = [\alpha]_{\lambda}^{T}\cdot\ell\cdot c}
$$

avec $\alpha$ en degrés, $[\alpha]_{\lambda}^{T}$ en $\mathrm{deg\cdot dm^{-1}\cdot(g\cdot mL^{-1})^{-1}}$,
$\ell$ en dm et $c$ en $\mathrm{g\cdot mL^{-1}}$.

À l'équilibre, la rotation est la somme additive des contributions de $\mathrm{A_1}$ et $\mathrm{A_2}$, ce qui donne leurs proportions.

#### Question 41

L'espèce majoritaire est celle dont la conformation chaise place le **maximum de substituants volumineux en position équatoriale** : c'est $\mathrm{A_2}$ (β-D-glucopyranose), dont l'hydroxyle anomère et tous les autres substituants sont équatoriaux. L'effet anomère, qui favoriserait la position axiale, ne suffit pas ici à l'emporter sur l'encombrement stérique.

$$
\boxed{\mathrm{A_2}\ \text{(β-D-glucopyranose) est majoritaire à l'équilibre}}
$$

#### Question 42

Le carbone central de la pentane-2,4-dione est acide (deux carbonyles accepteurs, énolate stabilisé par mésomérie) :

$$
\boxed{pK_a(\text{pentane-2,4-dione}) \approx 9}
$$

L'ion hydrogénocarbonate $\mathrm{HCO_3^-}$ ($pK_a$ du couple $\mathrm{H_2CO_3/HCO_3^-} \approx 6{,}3$) est une **base douce** : il déprotone suffisamment la dione pour générer l'énolate nucléophile, sans provoquer, comme le ferait l'ion hydroxyde (base forte), les dégradations du sucre (épimérisation, Cannizzaro). Équation de déprotonation :

$$
\boxed{\mathrm{CH_3COCH_2COCH_3 + HCO_3^- = CH_3COCH^-COCH_3 + H_2CO_3\ (\to CO_2 + H_2O)}}
$$

#### Question 43

Mécanisme en milieu basique, à partir de la forme ouverte $\mathrm{A_0}$ et de l'énolate de la pentane-2,4-dione : (1) **addition nucléophile** (aldolisation) de l'énolate sur le carbone de l'aldéhyde de $\mathrm{A_0}$ ; (2) **déshydratation** en milieu basique (mécanisme E1cb) donnant l'énone conjuguée (condensation de Knoevenagel) ; (3) **addition nucléophile 1,4 intramoléculaire** (oxa-Michael) d'un hydroxyle du sucre sur l'énone, qui cyclise en pyrane. Le produit $\mathrm{B'}$, de formule brute $\mathrm{C_{11}H_{18}O_7}$ (vérification : $\mathrm{C_6H_{12}O_6 + C_5H_8O_2 - H_2O}$), est le C-glycoside cyclique portant au carbone anomère le groupe $-\mathrm{CH(COCH_3)_2}$.

#### Question 44

Le groupe $-\mathrm{CH(COCH_3)_2}$ de $\mathrm{B'}$ subit une **rétro-Claisen** en milieu basique : $\mathrm{HO^-}$ s'additionne sur l'un des carbonyles (intermédiaire tétraédrique), puis le doublet de l’oxygène reforme le carbonyle tandis que la liaison C–C se rompt : l’espèce partante est l’énolate $-\mathrm{CH^-COCH_3}$ porté par le glycoside, et l’autre fragment est l’acide éthanoïque. Le transfert du proton de cet acide à l’énolate fournit simultanément l’ion éthanoate $\mathrm{CH_3COO^-}$ et la cétone $-\mathrm{CH_2COCH_3}$. On obtient ainsi **B**, la cétone β-C-glycosidique.

### B. Synthèse du Pro-Xylane®

#### Question 45

Le carbone mis en jeu est le carbone de la fonction cétone réduite en alcool (portant $-\mathrm{OH}$, $-\mathrm{CH_3}$, $-\mathrm{H}$ et $-\mathrm{CH_2-}$pyranosyle).

Classement CIP : $-\mathrm{OH}$ (O) priorité **1** ; $-\mathrm{CH_2-}$pyranosyle, dont le premier carbone est lié à (C, H, H), priorité **2** ; $-\mathrm{CH_3}$, lié à (H, H, H), priorité **3** ; $-\mathrm{H}$ priorité **4**. La lecture sur la structure de la figure 4 (H, priorité 4, placé vers l'arrière) donne, en tournant de 1 vers 2 vers 3 dans le sens anti-horaire :

$$
\boxed{\text{stéréodescripteur du stéréoisomère majoritaire : } (S)}
$$

#### Question 46

Par analogie avec l'excès énantiomérique, l'**excès diastéréoisomérique** est $ed = |\,\%_{\text{maj}} - \%_{\text{min}}\,|$, avec $\%_{\text{maj}} + \%_{\text{min}} = 100$. Pour l'essai 1 ($ed = 6\ \%$) :

$$
\boxed{\%_{\text{maj}} = \frac{100 + ed}{2} = 53\ \%}
$$

(et $\%_{\text{min}} = 47\ \%$).

#### Question 47

Le tétrahydroborate de sodium est basique : en présence d'un composé protique comme l'acide éthanoïque, chaque hydrure $\mathrm{H^-}$ rencontre un proton et libère du dihydrogène. Équation ajustée de formation du triacétoxyborohydrure :

$$
\boxed{\mathrm{NaBH_4 + 3\,CH_3COOH \longrightarrow NaBH(OCOCH_3)_3 + 3\,H_2}}
$$

L'essai 6 met en œuvre directement $\mathrm{NaBH(OAc)_3}$ (sans acide ajouté) et conduit à un excès diastéréoisomérique de 92 %, voisin de celui de l'essai 5 ($\mathrm{NaBH_4}$ + AcOH, 90 %) : cela **confirme** que le triacétoxyborohydrure se forme in situ dans l'essai 5, réducteur plus doux et plus diastéréosélectif que $\mathrm{NaBH_4}$.

#### Question 48

L'essai 9 ($\mathrm{H_2}$, catalyseur $\mathrm{Ru/C}$, solvant eau) est retenu industriellement car : (i) le **solvant est l'eau**, éco-compatible ; (ii) le catalyseur est **hétérogène** : il est facilement récupéré par filtration et **recyclable** ; (iii) le réducteur $\mathrm{H_2}$ est économique et assure une forte **économie d'atomes** (pas de déchet boré à traiter) ; (iv) le rendement reste bon (82 %). L'absence de diastéréosélectivité ($ed = 0$) n'est pas rédhibitoire à l'échelle du procédé si le mélange est utilisable.

## Partie V — Synthèse d'un précurseur de Grandifloracine dans l'eau

#### Question 49

Une synthèse **monotope** (« one-pot ») est une synthèse dans laquelle un réactif subit plusieurs transformations successives et/ou simultanées **dans un seul réacteur** (un seul mélange réactionnel), en évitant les longs processus de séparation et de purification des espèces intermédiaires.

#### Question 50

La grandifloracine F porte deux esters benzoate là où le diépoxyde I porte deux époxydes : il faut ouvrir les deux époxydes par un nucléophile porteur du groupe benzoyle. Séquence proposée : traiter le diépoxyde I par le **benzoate de sodium** $\mathrm{PhCOO^-Na^+}$ en milieu aqueux ; les ions carboxylate ouvrent (régiosélectivement) les deux époxydes et installent les deux esters benzoate, donnant F. (Un organomagnésien porteur d'une fonction ester est à proscrire : il serait détruit.)

#### Question 51

L'alcool salicylique G porte **deux** fonctions O–H (phénol et alcool benzylique primaire). Les deux bandes **larges** à 3420 et $3160\ \mathrm{cm^{-1}}$ sont les vibrations d'élongation O–H de ces deux groupes engagés dans des **liaisons hydrogène** : la largeur traduit la distribution de ces liaisons. La bande la plus basse ($3160\ \mathrm{cm^{-1}}$) est cohérente avec une liaison hydrogène **intramoléculaire** forte entre les deux groupes en ortho.

#### Question 52

Le cycle est 1,2-disubstitué : quatre H aromatiques notés b, c, d, e (b et e aux extrémités, chacun avec un seul voisin hydrogène en ortho ; c et d au milieu, chacun avec deux voisins). En ne retenant que les couplages $^3J$, supposés de même ordre de grandeur :

| Proton | Voisins (couplage $^3J$) | Allure du signal |
|---|---|---|
| b | 1 (c) | **doublet** |
| c | 2 (b et d) | **triplet** (dd) |
| d | 2 (c et e) | **triplet** (dd) |
| e | 1 (d) | **doublet** |

#### Question 53

L'ajout de $\mathrm{D_2O}$ échange les **protons labiles** (O–H, N–H) contre du deutérium : les signaux correspondants **disparaissent** du spectre. En comparant les figures 5 et 6, on identifie ainsi les deux signaux d'hydroxyle (celui du phénol vers 9,3 ppm et celui de l'alcool vers 4,9 ppm) ; le signal du $\mathrm{CH_2}$ (f) subsiste et se simplifie (le couplage avec l'OH disparaît : il devient un singulet).

#### Question 54

L'effet mésomère **donneur (+M)** du groupe OH enrichit le cycle en positions **ortho et para**, ce qui **blinde** les H correspondants (δ plus faibles). Attribution du spectre (400 MHz, DMSO-$d_6$) :

| $\delta$ (ppm) | Multiplicité | Intégration | Attribution | Justification |
|---|---|---|---|---|
| 9,28 | singulet | 1H | a (O–H phénolique) | très déblindé (liaison H), échangeable avec $\mathrm{D_2O}$ |
| 7,29 | doublet | 1H | e (H en ortho de $\mathrm{CH_2OH}$, méta de OH) | peu blindé, un seul voisin $^3J$ |
| 7,03 | doublet de doublets (≈ triplet) | 1H | c (H méta de OH) | deux voisins $^3J$ |
| 6,79 (6,74–6,80) | multiplet (d + dd) | 2H | b (ortho de OH) et d (para de OH) | **blindés par l'effet +M du OH** |
| 4,93 | triplet | 1H | g (O–H de l'alcool) | échangeable avec $\mathrm{D_2O}$, couplé au $\mathrm{CH_2}$ |
| 4,49 | doublet | 2H | f ($\mathrm{CH_2}$) | couplé à l'OH (singulet après ajout de $\mathrm{D_2O}$) |

#### Question 55

Après décompte des électrons de valence et schéma de Lewis : $\mathrm{IO_4^-}$ présente 4 liaisons I–O et **aucun doublet non liant** sur l'iode (type $\mathrm{AX_4}$) :

$$
\boxed{\mathrm{IO_4^-}\ :\ \text{géométrie tétraédrique, angles } \approx 109{,}5^\circ}
$$

$\mathrm{IO_3^-}$ présente 3 liaisons I–O et **un doublet non liant** (type $\mathrm{AX_3E}$) :

$$
\boxed{\mathrm{IO_3^-}\ :\ \text{géométrie pyramidale à base triangulaire, angles } \approx 100^\circ < 109{,}5^\circ\ \text{(répulsion du doublet)}}
$$

#### Question 56

L'ester periodate cyclique J se fragmente de façon **concertée** : les électrons de la liaison C–C du pinacol forment les deux liaisons $\mathrm{C{=}O}$, tandis que les liaisons C–O–I se rompent et que l'iode est réduit de I(VII) à I(V). Produits organiques : **deux molécules de propanone** $\mathrm{(CH_3)_2C{=}O}$, soit $K = K' =$ propanone, plus $\mathrm{NaIO_3}$.

#### Question 57

Le clivage oxydatif exige deux fonctions oxygénées **vicinales**. L'alcool salicylique possède un phénol (C1) et un alcool benzylique (C2) en ortho, analogue d'un 1,2-diol : l'iode ponte les **deux oxygènes** (O phénolique et O benzylique) pour former un **ester periodate cyclique** à cheval sur les positions ortho du cycle aromatique.

#### Question 58

Par analogie avec J, la réaction de G avec $\mathrm{NaIO_4}$ forme d'abord l'ester periodate cyclique de la question 57, qui se fragmente en provoquant la **déaromatisation** du cycle : H est la **spiro-époxy-cyclohexa-2,5-diénone** — un cycle cyclohexadiénone portant un époxyde dont le centre spiro est le carbone du cycle initialement porteur du groupe hydroxyméthyle ; l’ancien carbone $\mathrm{CH_2OH}$ constitue l’autre carbone de l’époxyde. Vérification : $\mathrm{C_7H_6O_2}$ compte $\frac{2\times7+2-6}{2} = 5$ insaturations (2 C=C + 1 C=O + 2 cycles), et 2 oxygènes (C=O + époxyde).

#### Question 59

Le passage de H à I est une **cycloaddition de Diels-Alder [4+2]** : H se dimérise, une molécule jouant le rôle de **diène** (la partie diénone en conformation s-cis) et l'autre de **diénophile** (l'une des liaisons C=C conjuguées). Le mécanisme est **concerté** et péricyclique : six électrons π se déplacent simultanément (trois flèches courbes en cycle), formant deux liaisons σ C–C et une nouvelle liaison π, via un état de transition cyclique ; le produit est le squelette bicyclo[2.2.2]octène portant les deux époxydes (= I).

#### Question 60

La réaction étant fortement régiosélective, les autres adduits possibles sont minoritaires : les **régioisomères** correspondant à l'autre orientation relative du diène et du diénophile (mise en jeu de l'autre liaison C=C de la diénone comme diénophile, orientation « tête-bêche » au lieu de « tête-à-tête »), ainsi que les **stéréoisomères endo/exo** de la cycloaddition. On les représente par le squelette bicyclo[2.2.2]octène correspondant, avec les carbonyles et époxydes disposés selon l'orientation alternative.
