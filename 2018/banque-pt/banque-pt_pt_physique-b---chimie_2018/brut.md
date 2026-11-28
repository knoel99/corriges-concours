# Banque PT PT — Physique B - Chimie 2018 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille Claude) · effort non renseigné · vitesse non renseignée

Épreuve de 2 heures, sans calculatrice, sur l'eau de Javel et une solution de remplacement, le percarbonate de sodium : 40 questions en trois parties indépendantes, un papier millimétré à rendre (annexe 3). Les 40 questions sont traitées. Les valeurs lues sur les annexes et sur le graphique de la question 21 sont signalées à l'endroit où elles servent. Les applications numériques emploient les valeurs approchées fournies par l'énoncé. Une incohérence numérique de l'énoncé (quantité d'ions iodure) est signalée à la question 17.

[Sujet officiel](https://www.banquept.fr/documents/2018/ph_b_ch_2018_pt.pdf) · [Rapport du jury](https://www.banquept.fr/documents/ecrit/rapport/2018/rapport_phys_b_ecrit_2018.pdf)

## Partie 1 — Préparation de l'eau de Javel

### Question 1 — Domaines de prédominance

Nombres d'oxydation du chlore : $-\mathrm{I}$ dans $\mathrm{Cl^-}$, $0$ dans $\mathrm{Cl_2}$, $+\mathrm{I}$ dans $\mathrm{HClO}$ et dans $\mathrm{ClO^-}$.

- Le potentiel croît avec le nombre d'oxydation : $\mathrm{Cl^-}$ occupe le bas du diagramme, les espèces au degré $+\mathrm{I}$ le haut, et $\mathrm{Cl_2}$ s'intercale entre les deux.
- $\mathrm{HClO}$ et $\mathrm{ClO^-}$ forment un couple acide-base : l'acide $\mathrm{HClO}$ prédomine à gauche de la frontière verticale ($\mathrm{pH} < 7{,}5$), la base $\mathrm{ClO^-}$ à droite.
- $\mathrm{Cl_2}$ n'a de domaine que dans le petit triangle situé entre $E = 1{,}43\ \mathrm V$ et $E = 1{,}56\ \mathrm V$ à $\mathrm{pH} = 0$, et qui se ferme au point A ($\mathrm{pH}_A = 2{,}2$).

**Bilan : $\mathrm{HClO}$ en haut à gauche, $\mathrm{ClO^-}$ en haut à droite, $\mathrm{Cl_2}$ dans le triangle acide, $\mathrm{Cl^-}$ dans toute la partie basse.**

![Figure 1 — Diagramme E-pH du chlore avec les domaines des quatre espèces, les points A et B et les pentes des frontières](figures/diagramme-e-ph-chlore.svg)

### Question 2 — Solution de dichlore portée entre les pH de A et de B

Au-delà du point A, le dichlore n'a plus de domaine de stabilité : entre $\mathrm{pH}_A$ et $\mathrm{pH}_B$, les seules espèces stables sont $\mathrm{HClO}$ (degré $+\mathrm I$) et $\mathrm{Cl^-}$ (degré $-\mathrm I$). Le dichlore (degré $0$) se **dismute** :

$$\boxed{\mathrm{Cl_{2(aq)}} + \mathrm{H_2O_{(l)}} = \mathrm{HClO_{(aq)}} + \mathrm{Cl^-_{(aq)}} + \mathrm{H^+_{(aq)}}}$$

Vérification : un atome de chlore passe de $0$ à $+\mathrm I$, l'autre de $0$ à $-\mathrm I$ ; les charges sont équilibrées ($0 = -1 + 1$). Comme le pH est augmenté par ajout d'une base, on peut aussi écrire $\mathrm{Cl_2} + \mathrm{HO^-} = \mathrm{HClO} + \mathrm{Cl^-}$.

### Question 3 — Pente de la droite (AB)

La droite (AB) sépare $\mathrm{HClO}$ et $\mathrm{Cl^-}$ :

$$\mathrm{HClO} + \mathrm{H^+} + 2\,e^- = \mathrm{Cl^-} + \mathrm{H_2O}$$

Relation de Nernst :

$$E = E^\circ_3 + \frac{0{,}06}{2}\log\frac{[\mathrm{HClO}]\,[\mathrm{H^+}]}{[\mathrm{Cl^-}]\,c^\circ}$$

Sur la frontière, $[\mathrm{HClO}] = [\mathrm{Cl^-}]$ :

$$E = E^\circ_3 - 0{,}03\,\mathrm{pH}$$

$$\boxed{\text{pente de (AB)} = -0{,}03\ \mathrm{V\ par\ unité\ de\ pH}}$$

### Question 4 — pKa du couple HClO/ClO⁻

La frontière verticale passant par B sépare l'acide $\mathrm{HClO}$ et sa base $\mathrm{ClO^-}$. Sur cette frontière $[\mathrm{HClO}] = [\mathrm{ClO^-}]$, et la relation $\mathrm{pH} = \mathrm{p}K_a + \log\dfrac{[\mathrm{ClO^-}]}{[\mathrm{HClO}]}$ donne $\mathrm{pH} = \mathrm{p}K_a$. On lit l'abscisse de B sur l'annexe 1 :

$$\boxed{\mathrm{p}K_a(\mathrm{HClO}/\mathrm{ClO^-}) = \mathrm{pH}_B = 7{,}5}$$

### Question 5 — Potentiel standard E°₃ du couple HClO/Cl⁻

Demi-équations des trois couples, écrites pour un atome de chlore :

$$\mathrm{HClO} + \mathrm{H^+} + e^- = \tfrac12\,\mathrm{Cl_2} + \mathrm{H_2O} \qquad (E^\circ_2,\ 1\ \text{électron})$$

$$\tfrac12\,\mathrm{Cl_2} + e^- = \mathrm{Cl^-} \qquad (E^\circ_1,\ 1\ \text{électron})$$

$$\mathrm{HClO} + \mathrm{H^+} + 2\,e^- = \mathrm{Cl^-} + \mathrm{H_2O} \qquad (E^\circ_3,\ 2\ \text{électrons})$$

La troisième est la somme des deux premières ; les enthalpies libres standard de demi-réaction $-nFE^\circ$ s'ajoutent :

$$-2FE^\circ_3 = -FE^\circ_2 - FE^\circ_1$$

$$E^\circ_3 = \frac{E^\circ_1 + E^\circ_2}{2} = \frac{1{,}4 + 1{,}6}{2}$$

$$\boxed{E^\circ_3 = 1{,}5\ \mathrm V}$$

Contrôle sur le diagramme : au point A, la frontière $\mathrm{HClO}/\mathrm{Cl^-}$ donne $E = 1{,}5 - 0{,}03\times 2{,}2 = 1{,}43\ \mathrm V$, valeur portée sur l'annexe 1.

### Question 6 — Équation de formation de l'eau de Javel

En milieu basique ($\mathrm{pH} > 7{,}5$), le dichlore se dismute en ion hypochlorite et en ion chlorure :

$$\boxed{\mathrm{Cl_2} + 2\,\mathrm{HO^-} = \mathrm{ClO^-} + \mathrm{Cl^-} + \mathrm{H_2O}}$$

soit, avec les ions sodium spectateurs, $\mathrm{Cl_2} + 2\,\mathrm{NaOH} = \mathrm{NaClO} + \mathrm{NaCl} + \mathrm{H_2O}$. Les ions hypochlorite et chlorure sont formés en quantités égales.

### Question 7 — Mélange avec un détergent acide

L'eau de Javel contient $\mathrm{ClO^-}$ et $\mathrm{Cl^-}$ en quantités égales. Si l'on acidifie :

- en dessous de $\mathrm{pH} = 7{,}5$, $\mathrm{ClO^-}$ est converti en $\mathrm{HClO}$ ;
- en dessous de $\mathrm{pH}_A = 2{,}2$, $\mathrm{HClO}$ et $\mathrm{Cl^-}$ ont des domaines disjoints, séparés par celui du dichlore : ils réagissent l'un sur l'autre (médiamutation, réaction inverse de la dismutation).

$$\boxed{\mathrm{ClO^-} + \mathrm{Cl^-} + 2\,\mathrm{H^+} = \mathrm{Cl_2} + \mathrm{H_2O}}$$

Le dichlore, peu soluble, se dégage : **le gaz toxique est le dichlore $\mathrm{Cl_2}$**, irritant et suffocant.

Conclusion : **il ne faut jamais mélanger l'eau de Javel avec un produit acide** (détartrant, gel pour sanitaires) ; cette mise en garde figure sur les emballages.

### Question 8 — Maille de NaCl et sites octaédriques

Les ions chlorure occupent les sommets du cube et les centres des six faces. Les sites octaédriques d'un réseau cubique à faces centrées sont :

- le **centre du cube**, entouré par les six anions des centres des faces ;
- les **milieux des douze arêtes**, chacun entouré de six anions à la distance $a/2$ (les deux sommets de l'arête, les centres des deux faces qui la contiennent, et deux centres de faces des mailles voisines).

Les ions sodium les occupent tous.

![Figure 2 — Maille de NaCl : ions chlorure aux sommets et aux centres des faces, ions sodium au centre du cube et aux milieux des arêtes](figures/maille-nacl.svg)

### Question 9 — Nombre de motifs et coordinences

Ions chlorure : 8 sommets comptant pour $1/8$ et 6 centres de faces comptant pour $1/2$.

$$N(\mathrm{Cl^-}) = 8\times\frac18 + 6\times\frac12 = 4$$

Ions sodium : 1 au centre, comptant pour 1, et 12 milieux d'arêtes comptant pour $1/4$.

$$N(\mathrm{Na^+}) = 1 + 12\times\frac14 = 4$$

$$\boxed{\text{4 motifs NaCl par maille}}$$

La maille est bien électriquement neutre. **Coordinence** : chaque ion sodium a pour plus proches voisins 6 ions chlorure, à la distance $a/2$, aux sommets d'un octaèdre ; par symétrie des deux sous-réseaux, chaque ion chlorure est entouré de 6 ions sodium à la distance $a/2$.

$$\boxed{\text{coordinence 6 pour } \mathrm{Na^+} \text{ et pour } \mathrm{Cl^-}\ (\text{coordinence 6/6})}$$

### Question 10 — Ordre de grandeur de la masse volumique

La maille de volume $a^3$ contient 4 motifs NaCl de masse molaire $M = M_{\mathrm{Na}} + M_{\mathrm{Cl}} = 58\ \mathrm{g\cdot mol^{-1}}$ :

$$\rho = \frac{4\,(M_{\mathrm{Na}} + M_{\mathrm{Cl}})}{N_a\,a^3}$$

Application numérique, avec $a = 600\ \mathrm{pm} = 6{,}00\cdot 10^{-8}\ \mathrm{cm}$ :

$$a^3 = 216\cdot 10^{-24}\ \mathrm{cm^3} = 2{,}16\cdot 10^{-22}\ \mathrm{cm^3}$$

$$\rho = \frac{4\times 58}{6\cdot 10^{23}\times 2{,}16\cdot 10^{-22}} = \frac{232}{130} \approx 1{,}8\ \mathrm{g\cdot cm^{-3}}$$

$$\boxed{\rho \approx 1{,}8\cdot 10^{3}\ \mathrm{kg\cdot m^{-3}} \approx 2\cdot 10^{3}\ \mathrm{kg\cdot m^{-3}}}$$

Ordre de grandeur cohérent pour un solide ionique : environ deux fois la masse volumique de l'eau.

### Question 11 — Relation de tangence anion-cation

Dans un cristal ionique, le contact se fait entre ions de signes opposés. Le long d'une arête se succèdent un anion (sommet), un cation (milieu de l'arête) et un anion (sommet) : l'arête contient deux rayons anioniques et un diamètre cationique.

$$\boxed{a = 2\left(r_{\mathrm{Na^+}} + r_{\mathrm{Cl^-}}\right)}$$

soit $r_{\mathrm{Na^+}} + r_{\mathrm{Cl^-}} = a/2 = 300\ \mathrm{pm}$.

### Question 12 — Inégalité vérifiée par le rayon des anions

Deux anions plus proches voisins sont séparés par une demi-diagonale de face, $a\sqrt2/2$. Ils ne se touchent pas si cette distance dépasse deux rayons anioniques :

$$2\,r_{\mathrm{Cl^-}} < \frac{a\sqrt2}{2}$$

$$\boxed{r_{\mathrm{Cl^-}} < \frac{a\sqrt2}{4}}$$

Avec $a = 600\ \mathrm{pm}$ : $r_{\mathrm{Cl^-}} < 212\ \mathrm{pm}$ environ.

### Question 13 — Valeur limite du rapport des rayons

En reportant $a = 2\,(r_{\mathrm{Na^+}} + r_{\mathrm{Cl^-}})$ dans $4\,r_{\mathrm{Cl^-}} < a\sqrt2$ :

$$4\,r_{\mathrm{Cl^-}} < 2\sqrt2\left(r_{\mathrm{Na^+}} + r_{\mathrm{Cl^-}}\right)$$

$$\sqrt2\,r_{\mathrm{Cl^-}} < r_{\mathrm{Na^+}} + r_{\mathrm{Cl^-}}$$

$$\boxed{\frac{r_{\mathrm{Na^+}}}{r_{\mathrm{Cl^-}}} > \sqrt2 - 1 \approx 0{,}41}$$

La valeur limite est $\sqrt2 - 1 \approx 0{,}41$ : en dessous, le cation serait trop petit pour écarter les anions, qui se toucheraient, et la structure ne serait plus stable.

## Partie 2 — Dosage indirect de l'eau de Javel

### Question 14 — Ordre d'introduction des réactifs

L'acide doit être introduit **en dernier**, quand les ions iodure en excès sont déjà au contact des ions hypochlorite. Si l'on acidifiait d'abord la solution $S_0$, les ions $\mathrm{ClO^-}$ réagiraient avec les ions $\mathrm{Cl^-}$ pour former du dichlore (question 7) :

- ce gaz est toxique (sécurité de l'opérateur) ;
- en se dégageant, il emporte une partie de l'oxydant à doser : la quantité de diiode formée ensuite serait trop faible et le titre trouvé serait sous-estimé.

En présence d'ions iodure, l'oxydant est réduit en solution par $\mathrm{I^-}$ dès l'acidification, sans perte de matière.

### Question 15 — Demi-équations des couples ClO⁻/Cl⁻ et I₂/I⁻

$$\boxed{\mathrm{ClO^-} + 2\,\mathrm{H^+} + 2\,e^- = \mathrm{Cl^-} + \mathrm{H_2O}}$$

$$\boxed{\mathrm{I_2} + 2\,e^- = 2\,\mathrm{I^-}}$$

Le chlore passe du degré $+\mathrm I$ au degré $-\mathrm I$ : deux électrons sont bien échangés.

### Question 16 — Réaction avant le dosage ; caractère quasi total

$$\boxed{\mathrm{ClO^-} + 2\,\mathrm{I^-} + 2\,\mathrm{H^+} = \mathrm{Cl^-} + \mathrm{I_2} + \mathrm{H_2O}}$$

**Caractère quasi total.** Les deux couples du chlore fournis ($E^\circ = 2{,}0\ \mathrm V$ et $1{,}4\ \mathrm V$) ont des potentiels standard très supérieurs à celui du couple $\mathrm{I_2}/\mathrm{I^-}$ ($0{,}5\ \mathrm V$) : l'oxydant $\mathrm{ClO^-}$ et le réducteur $\mathrm{I^-}$ ont des domaines largement disjoints, la réaction est très favorisée.

Quantitativement, comme à la question 5 (un électron par atome de chlore dans chacun des deux couples) :

$$E^\circ(\mathrm{ClO^-}/\mathrm{Cl^-}) = \frac{2{,}0 + 1{,}4}{2} = 1{,}7\ \mathrm V$$

La réaction échange 2 électrons ; avec $\dfrac{RT}{F}\ln 10 = 0{,}06\ \mathrm V$ à 298 K :

$$\log K^\circ = \frac{2\,\left(1{,}7 - 0{,}5\right)}{0{,}06} = 40$$

$$\boxed{K^\circ = 10^{40} \gg 1}$$

La réaction est quasi totale.

### Question 17 — Relation entre les quantités de matière

La réaction de la question 16 est quasi totale et, d'après l'énoncé, les ions iodure (comme les ions $\mathrm{H^+}$) sont en excès : l'ion hypochlorite est le réactif limitant. Une mole de $\mathrm{ClO^-}$ donne une mole de $\mathrm{I_2}$ :

$$\boxed{n(\mathrm{I_2})_{\text{formé}} = n(\mathrm{ClO^-})_{\text{initial}}}$$

La quantité d'ions iodure introduite, $n(\mathrm{I^-}) = c_1V_1$, n'intervient pas dans le résultat ; il faut seulement que $c_1V_1 > 2\,n(\mathrm{ClO^-})$.

**Remarque sur les données.** Avec les valeurs du protocole, $c_1V_1 = 0{,}10\times 20\cdot 10^{-3} = 2{,}0\cdot 10^{-3}\ \mathrm{mol}$, alors que le résultat de la question 19 ($n(\mathrm{ClO^-}) = 1{,}5\cdot 10^{-3}\ \mathrm{mol}$) demanderait $3{,}0\cdot 10^{-3}\ \mathrm{mol}$ d'ions iodure. Les valeurs numériques de l'énoncé ne sont donc pas cohérentes avec l'excès annoncé. On suit ici l'énoncé, qui affirme que les ions iodure sont en excès ; sur une copie, signaler l'écart en une ligne et poursuivre.

### Question 18 — Réaction de dosage du diiode par le thiosulfate

Demi-équations :

$$\mathrm{I_2} + 2\,e^- = 2\,\mathrm{I^-}$$

$$2\,\mathrm{S_2O_3^{2-}} = \mathrm{S_4O_6^{2-}} + 2\,e^-$$

Bilan :

$$\boxed{\mathrm{I_2} + 2\,\mathrm{S_2O_3^{2-}} = 2\,\mathrm{I^-} + \mathrm{S_4O_6^{2-}}}$$

Elle est quasi totale ($E^\circ(\mathrm{I_2}/\mathrm{I^-}) = 0{,}5\ \mathrm V$ très supérieur à $E^\circ(\mathrm{S_4O_6^{2-}}/\mathrm{S_2O_3^{2-}}) = 0{,}1\ \mathrm V$, soit $\log K^\circ = 2\times 0{,}4/0{,}06 \approx 13$) et rapide, comme l'exige une réaction de titrage. L'équivalence est repérée par la disparition de la couleur bleu-noir du complexe formé par le diiode et l'empois d'amidon.

### Question 19 — Quantités de diiode et d'ions hypochlorite

À l'équivalence :

$$n(\mathrm{I_2}) = \frac{n(\mathrm{S_2O_3^{2-}})_{\text{versé}}}{2} = \frac{c_2\,V_E}{2}$$

$$n(\mathrm{I_2}) = \frac{0{,}15\times 20\cdot 10^{-3}}{2}$$

$$\boxed{n(\mathrm{I_2}) = 1{,}5\cdot 10^{-3}\ \mathrm{mol}}$$

D'après la question 17 :

$$\boxed{n(\mathrm{ClO^-}) = n(\mathrm{I_2}) = 1{,}5\cdot 10^{-3}\ \mathrm{mol}}$$

dans la prise d'essai $V_0 = 10{,}0\ \mathrm{mL}$ de solution $S_0$.

### Question 20 — Concentration de la solution commerciale et degré chlorométrique

**Concentrations.** Dans la solution $S_0$ :

$$[\mathrm{ClO^-}]_{S_0} = \frac{n(\mathrm{ClO^-})}{V_0} = \frac{1{,}5\cdot 10^{-3}}{10{,}0\cdot 10^{-3}} = 0{,}15\ \mathrm{mol\cdot L^{-1}}$$

La solution commerciale est dix fois plus concentrée :

$$\boxed{[\mathrm{ClO^-}]_{\text{com}} = 1{,}5\ \mathrm{mol\cdot L^{-1}}}$$

**Degré chlorométrique.** L'acidification complète d'un litre de solution commerciale libère, d'après l'équation de définition, une mole de dichlore par mole d'ions hypochlorite (les ions chlorure sont présents en quantité au moins égale, question 6) : $n(\mathrm{Cl_2}) = 1{,}5\ \mathrm{mol}$. Ce gaz, supposé parfait, occupe à $T = 273\ \mathrm K$ et $P = 1{,}0\cdot 10^{5}\ \mathrm{Pa}$ le volume

$$V = \frac{n(\mathrm{Cl_2})\,R\,T}{P}$$

$$V = \frac{1{,}5\times 8{,}3\times 273}{1{,}0\cdot 10^{5}} = 3{,}4\cdot 10^{-2}\ \mathrm{m^3} = 34\ \mathrm L$$

(calcul à la main : $8{,}3\times 273 \approx 2{,}27\cdot 10^{3}$, soit un volume molaire de $22{,}7\ \mathrm{L\cdot mol^{-1}}$, multiplié par 1,5).

$$\boxed{D \approx 34^\circ\ \text{chl}}$$

**Comparaison.** L'étiquette annonce 36° chl « au conditionnement » : l'écart relatif est de $2/36 \approx 6\ \%$. Le résultat est du bon ordre de grandeur et légèrement inférieur à la valeur annoncée, ce qui est cohérent avec la lente décomposition des ions hypochlorite depuis la fabrication (questions 21 à 23), à laquelle s'ajoutent les incertitudes du dosage.

### Question 21 — Justification de la recommandation du fabricant

Lectures sur le graphique de l'énoncé (concentration initiale voisine de $2{,}1\ \mathrm{mol\cdot L^{-1}}$, valeurs lues à 0,05 près) :

| Température | Après 50 jours | Après 90 à 100 jours | Durée pour perdre la moitié |
|---|---|---|---|
| 20 °C | $\approx 1{,}8\ \mathrm{mol\cdot L^{-1}}$ | $\approx 1{,}5\ \mathrm{mol\cdot L^{-1}}$ | $\approx 175$ jours |
| 30 °C | $\approx 1{,}0\ \mathrm{mol\cdot L^{-1}}$ | $\approx 0{,}5\ \mathrm{mol\cdot L^{-1}}$ | $\approx 45$ jours |
| 40 °C | $\approx 0{,}35\ \mathrm{mol\cdot L^{-1}}$ | $< 0{,}1\ \mathrm{mol\cdot L^{-1}}$ | $\approx 20$ jours |

Ces courbes montrent que :

- la concentration en ions hypochlorite décroît au cours du temps, même à 20 °C : au bout de trois mois, il ne reste qu'environ 70 % du titre initial. Le produit concentré a donc une durée de vie limitée, d'où la consigne de le diluer **dans les trois mois** ;
- la décomposition est d'autant plus rapide que la température est élevée : à 30 °C il ne reste qu'un quart du titre après trois mois, à 40 °C presque rien. D'où le délai raccourci en **période chaude** et la consigne de conserver **au frais**.

Les courbes ne renseignent pas sur l'effet de la lumière, que l'étiquette mentionne aussi (décomposition photochimique).

### Question 22 — Loi montrant que la température est un facteur cinétique

Il s'agit de la **loi d'Arrhenius** :

$$\boxed{k = A\,\exp\!\left(-\frac{E_a}{RT}\right)}$$

ou, sous forme différentielle, $\dfrac{\mathrm d\ln k}{\mathrm dT} = \dfrac{E_a}{RT^2}$, avec :

- $k$ : constante de vitesse de la réaction (son unité dépend de l'ordre) ;
- $A$ : facteur préexponentiel (ou facteur de fréquence), de même unité que $k$ ;
- $E_a$ : énergie d'activation, en $\mathrm{J\cdot mol^{-1}}$, positive ;
- $R = 8{,}3\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}$ : constante des gaz parfaits ;
- $T$ : température absolue, en kelvins.

Comme $E_a > 0$, $k$ croît avec $T$ : la réaction est plus rapide à chaud.

### Question 23 — Conservation d'une solution diluée

**Oui, la solution diluée se conserve mieux.** La concentration du réactif est un facteur cinétique : pour une loi de vitesse $v = k\,[\mathrm{ClO^-}]^{\alpha}$ avec $\alpha > 0$, diluer diminue la vitesse de décomposition. On le voit sur les courbes : la pente (vitesse de disparition) diminue à mesure que la concentration baisse. C'est cohérent avec l'étiquette, qui impose un délai pour diluer le concentré mais non pour utiliser la solution diluée.

Précision : le gain porte sur la fraction décomposée seulement si l'ordre est supérieur à 1 (le temps de demi-réaction, en $1/(k\,c_0)$ pour un ordre 2, augmente alors par dilution) ; pour un ordre exactement égal à 1, le temps de demi-réaction ne dépendrait pas de la concentration et seule la vitesse absolue diminuerait.

## Partie 3 — Le percarbonate de sodium, aspect thermodynamique

### Question 24 — Entropie standard de la réaction (1)

Pour la réaction (1), $\mathrm{H_2O_{2(aq)}} = \mathrm{H_2O_{(l)}} + \tfrac12\,\mathrm{O_{2(g)}}$ :

$$\Delta_r S^\circ = S^\circ(\mathrm{H_2O_{(l)}}) + \tfrac12\,S^\circ(\mathrm{O_{2(g)}}) - S^\circ(\mathrm{H_2O_{2(aq)}})$$

$$\Delta_r S^\circ = 70 + \tfrac12\times 200 - 140$$

$$\boxed{\Delta_r S^\circ = +30\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}}$$

**Signe.** La réaction produit du gaz à partir d'espèces en phase condensée ($\sum \nu_{i,\text{gaz}} = +\tfrac12 > 0$) : le désordre augmente, $\Delta_r S^\circ > 0$.

### Question 25 — Enthalpie standard de formation du dioxygène gazeux

$$\boxed{\Delta_f H^\circ(\mathrm{O_{2(g)}}) = 0}$$

Le dioxygène gazeux est le corps simple correspondant à l'**état standard de référence** de l'élément oxygène à 298 K. Sa réaction de formation, $\mathrm{O_{2(g)}} = \mathrm{O_{2(g)}}$, ne transforme rien : son enthalpie standard est nulle.

### Question 26 — Enthalpie standard de la réaction (1)

$$\Delta_r H^\circ = \Delta_f H^\circ(\mathrm{H_2O_{(l)}}) + \tfrac12\,\Delta_f H^\circ(\mathrm{O_{2(g)}}) - \Delta_f H^\circ(\mathrm{H_2O_{2(aq)}})$$

$$\Delta_r H^\circ = -290 + 0 - (-190)$$

$$\boxed{\Delta_r H^\circ = -100\ \mathrm{kJ\cdot mol^{-1}}}$$

$\Delta_r H^\circ < 0$ : **la réaction est exothermique**, la décomposition de l'eau oxygénée dégage de la chaleur.

### Question 27 — Constante d'équilibre à 300 K et stabilité de l'eau oxygénée

Dans l'approximation d'Ellingham ($\Delta_r H^\circ$ et $\Delta_r S^\circ$ indépendantes de $T$) :

$$\Delta_r G^\circ(T) = \Delta_r H^\circ - T\,\Delta_r S^\circ = -RT\ln K^\circ$$

$$\boxed{K^\circ(T) = \exp\!\left(-\frac{\Delta_r H^\circ - T\,\Delta_r S^\circ}{RT}\right) = \exp\!\left(-\frac{\Delta_r H^\circ}{RT} + \frac{\Delta_r S^\circ}{R}\right)}$$

Contrôle à $T = 300\ \mathrm K$ :

$$\Delta_r G^\circ = -100\cdot 10^{3} - 300\times 30 = -109\cdot 10^{3}\ \mathrm{J\cdot mol^{-1}}$$

$$\ln K^\circ = \frac{109\cdot 10^{3}}{8{,}31\times 300} \approx 43{,}7$$

soit $K^\circ = 10^{43{,}7/2{,}3} \approx 10^{19}$, en accord avec la valeur fournie $K^\circ = 1{,}0\cdot 10^{19}$.

**Conclusion.** $K^\circ \gg 1$ : la dismutation est quasi totale à l'équilibre. **L'eau oxygénée n'est pas stable du point de vue thermodynamique.** Si elle se conserve néanmoins, c'est que la réaction est lente (blocage cinétique, état métastable), ce qu'étudie la suite.

### Question 28 — Influence d'une augmentation de température isobare

Relation de Van't Hoff :

$$\frac{\mathrm d\ln K^\circ}{\mathrm dT} = \frac{\Delta_r H^\circ}{RT^2}$$

Ici $\Delta_r H^\circ < 0$ : $K^\circ$ est une fonction **décroissante** de la température.

Partons d'un état d'équilibre, où $Q_r = K^\circ(T)$, avec

$$Q_r = \frac{\left(P_{\mathrm{O_2}}/P^\circ\right)^{1/2}}{[\mathrm{H_2O_2}]/c^\circ}$$

(l'eau, solvant, a une activité égale à 1). On augmente $T$ à pression constante : juste après la perturbation, la composition et la pression n'ont pas changé, donc $Q_r$ est inchangé, alors que $K^\circ$ a diminué. On a désormais

$$Q_r > K^\circ(T + \mathrm dT)$$

Le système évolue dans le sens qui diminue $Q_r$, c'est-à-dire dans le **sens indirect** (sens de formation de $\mathrm{H_2O_2}$).

$$\boxed{\text{Une élévation de température déplace l'équilibre (1) dans le sens indirect, endothermique.}}$$

C'est la loi de modération de Van't Hoff. La constante reste cependant énorme : le déplacement est sans conséquence pratique.

### Question 29 — Influence d'une augmentation de pression isotherme

À température constante, $K^\circ(T)$ est inchangée. Le quotient de réaction s'écrit, avec $P_{\mathrm{O_2}} = x_{\mathrm{O_2}}\,P$ ($x_{\mathrm{O_2}}$ fraction molaire du dioxygène dans la phase gazeuse, égale à 1 s'il est le seul gaz) :

$$Q_r = \frac{c^\circ}{[\mathrm{H_2O_2}]}\left(\frac{x_{\mathrm{O_2}}\,P}{P^\circ}\right)^{1/2}$$

Partant d'un état d'équilibre ($Q_r = K^\circ$), on augmente $P$ à composition fixée : $Q_r$, proportionnel à $\sqrt P$, **augmente**, tandis que $K^\circ$ ne varie pas. Donc

$$Q_r > K^\circ$$

et le système évolue dans le **sens indirect**, celui qui consomme le gaz.

$$\boxed{\text{Une élévation de pression déplace l'équilibre (1) dans le sens indirect (diminution de la quantité de gaz).}}$$

C'est la loi de modération de Le Chatelier : $\sum \nu_{i,\text{gaz}} = +\tfrac12 > 0$ dans le sens direct.

### Question 30 — Conditions minimisant la décomposition

D'après l'étude thermodynamique précédente, la décomposition (sens direct) est défavorisée par :

- une **température élevée** (question 28, réaction exothermique) ;
- une **pression élevée**, en particulier une forte pression partielle de dioxygène, par exemple en récipient fermé (question 29).

$$\boxed{\text{Du point de vue thermodynamique : haute température et haute pression.}}$$

**Portée de cette réponse.** Avec $K^\circ \approx 10^{19}$ à 300 K, ces leviers sont inopérants en pratique : même à 400 K, $\ln K^\circ = \dfrac{100\cdot 10^{3}}{8{,}31\times 400} + \dfrac{30}{8{,}31} \approx 34$, soit $K^\circ \approx 10^{15}$. La conservation réelle de l'eau oxygénée relève du contrôle cinétique, et les conditions sont alors opposées pour la température : conservation **au frais** (loi d'Arrhenius), à l'abri de la lumière, dans un flacon propre, **sans catalyseur** (ions métalliques, poussières). Sur une copie, donner la réponse thermodynamique demandée, puis distinguer explicitement cet argument cinétique.

## Partie 3 (suite) — Le percarbonate de sodium, aspect cinétique

### Question 31 — Définition d'un catalyseur

Un **catalyseur** est une espèce chimique qui **augmente la vitesse** d'une réaction thermodynamiquement possible **sans figurer dans son équation bilan** : consommé lors d'une étape, il est régénéré lors d'une étape ultérieure, et se retrouve en fin de transformation. Il ne modifie ni l'état d'équilibre ni les grandeurs thermodynamiques de la réaction ($K^\circ$, $\Delta_r G^\circ$) ; il agit à faible dose.

### Question 32 — Grandeur sur laquelle agit un catalyseur ; schéma

Un catalyseur agit sur l'**énergie d'activation** : il remplace le mécanisme initial par un autre chemin réactionnel, souvent en plusieurs étapes, dont les barrières d'énergie sont plus basses. D'après la loi d'Arrhenius, la constante de vitesse $k$ augmente donc, à température donnée.

Les niveaux d'énergie des réactifs et des produits sont inchangés : $\Delta_r H^\circ$, $\Delta_r G^\circ$ et $K^\circ$ ne sont pas modifiés.

![Figure 3 — Profil énergétique de la réaction avec et sans catalyseur : mêmes états initial et final, énergie d'activation abaissée](figures/profil-energetique-catalyse.svg)

### Question 33 — Type de catalyse réalisée avec le fil de platine

Il s'agit d'une **catalyse hétérogène** : le platine est un solide, alors que le réactif $\mathrm{H_2O_2}$ est en solution aqueuse. Catalyseur et réactif ne sont pas dans la même phase ; la réaction a lieu à la surface du métal (d'où l'intérêt d'une grande surface de contact).

Par comparaison, la catalyse par les ions ferriques dissous est homogène, et celle par la catalase est enzymatique.

### Question 34 — Loi de vitesse

En notant $\alpha$ l'ordre de la réaction par rapport au peroxyde d'hydrogène et $k$ la constante de vitesse (qui inclut ici l'effet du catalyseur, de concentration constante) :

$$\boxed{v = k\,[\mathrm{H_2O_2}]^{\alpha}}$$

Par définition de la vitesse volumique de la réaction (1), dans laquelle $\mathrm{H_2O_2}$ a le nombre stœchiométrique 1 :

$$v = -\frac{\mathrm d[\mathrm{H_2O_2}]}{\mathrm dt}$$

### Question 35 — Hypothèse d'un ordre 1

On note $c(t) = [\mathrm{H_2O_2}](t)$ et $c_0 = c(0)$. Pour un ordre 1 :

$$\boxed{\frac{\mathrm dc}{\mathrm dt} = -k\,c}$$

Séparation des variables et intégration entre $0$ et $t$ :

$$\int_{c_0}^{c}\frac{\mathrm dc'}{c'} = -k\int_0^t \mathrm dt'$$

$$\ln\frac{c}{c_0} = -k\,t$$

$$\boxed{c(t) = c_0\,e^{-kt} \quad\Longleftrightarrow\quad \ln c = \ln c_0 - k\,t}$$

Contrôles : $c(0) = c_0$ ; $c \to 0$ quand $t \to \infty$ (réaction totale) ; $k$ s'exprime en $\mathrm{min^{-1}}$ ou en $\mathrm{s^{-1}}$, de sorte que $kt$ est sans dimension.

### Question 36 — Hypothèse d'un ordre 2

Pour un ordre 2 :

$$\boxed{\frac{\mathrm dc}{\mathrm dt} = -k\,c^2}$$

Séparation des variables et intégration entre $0$ et $t$ :

$$-\int_{c_0}^{c}\frac{\mathrm dc'}{c'^2} = k\int_0^t \mathrm dt'$$

$$\frac1c - \frac1{c_0} = k\,t$$

$$\boxed{\frac{1}{c(t)} = \frac{1}{c_0} + k\,t \quad\Longleftrightarrow\quad c(t) = \frac{c_0}{1 + k\,c_0\,t}}$$

Contrôles : $c(0) = c_0$ ; $c \to 0$ quand $t \to \infty$ ; $k$ s'exprime ici en $\mathrm{L\cdot mol^{-1}\cdot min^{-1}}$, de sorte que $k\,c_0\,t$ est sans dimension.

### Question 37 — Détermination de l'ordre et de la constante de vitesse

**Méthode (méthode intégrale).** On teste chaque hypothèse en traçant la grandeur qui doit être affine en $t$ :

- ordre 1 : $\ln c$ en fonction de $t$ doit être une droite de pente $-k$ ;
- ordre 2 : $1/c$ en fonction de $t$ doit être une droite de pente $+k$.

L'ordre retenu est celui pour lequel les points expérimentaux sont alignés.

**Mise en œuvre.** Pentes entre points successifs, calculées à partir du tableau :

| Intervalle (min) | 0 à 5 | 5 à 10 | 10 à 20 | 20 à 30 | 30 à 35 |
|---|---|---|---|---|---|
| $\Delta(\ln c)/\Delta t$ ($\mathrm{min^{-1}}$) | $-0{,}06$ | $-0{,}06$ | $-0{,}05$ | $-0{,}07$ | $-0{,}06$ |
| $\Delta(1/c)/\Delta t$ ($\mathrm{L\cdot mol^{-1}\cdot min^{-1}}$) | $1{,}0$ | $1{,}0$ | $1{,}8$ | $4{,}2$ | $5{,}6$ |

Pour $\ln c$, la pente est constante aux arrondis près du tableau (valeurs données à 0,1 près) : les points sont alignés. Pour $1/c$, la pente est multipliée par plus de cinq entre le début et la fin : les points dessinent une courbe nettement convexe. **La réaction est d'ordre 1** par rapport au peroxyde d'hydrogène.

![Figure 4 — Logarithme de la concentration en peroxyde d'hydrogène en fonction du temps : points du tableau alignés, pente égale à l'opposé de la constante de vitesse, lecture du temps de demi-réaction](figures/cinetique-ordre-1.svg)

**Constante de vitesse.** La pente de la droite, prise entre les points extrêmes, vaut

$$-k = \frac{-4{,}7 - (-2{,}6)}{35 - 0} = -\frac{2{,}1}{35}$$

$$\boxed{k \approx 6{,}0\cdot 10^{-2}\ \mathrm{min^{-1}} = 1{,}0\cdot 10^{-3}\ \mathrm{s^{-1}}}$$

(Une régression linéaire sur les six points donne la même valeur, $k = 0{,}060\ \mathrm{min^{-1}}$.)

### Question 38 — Temps de demi-réaction

**Définition.** Le temps de demi-réaction $t_{1/2}$ est la durée au bout de laquelle l'avancement atteint la moitié de sa valeur finale ; la réaction étant totale, c'est la durée au bout de laquelle la moitié du réactif limitant a été consommée : $c(t_{1/2}) = c_0/2$.

**Expression.** Pour l'ordre 1, $\ln\dfrac{c_0/2}{c_0} = -k\,t_{1/2}$ :

$$\boxed{t_{1/2} = \frac{\ln 2}{k}}$$

Il est indépendant de la concentration initiale.

**Application numérique**, avec $\ln 2 = 0{,}7$ :

$$t_{1/2} = \frac{0{,}7}{6{,}0\cdot 10^{-2}}$$

$$\boxed{t_{1/2} \approx 12\ \mathrm{min}}$$

Cohérent avec le tableau : $c_0/2 = 3{,}65\cdot 10^{-2}\ \mathrm{mol\cdot L^{-1}}$ est atteint entre 10 min ($4{,}20\cdot 10^{-2}$) et 20 min ($2{,}4\cdot 10^{-2}$).

### Question 39 — Détermination graphique du temps de demi-réaction

Deux méthodes équivalentes :

- sur la courbe $c = f(t)$ : placer l'ordonnée $c_0/2 = 3{,}65\cdot 10^{-2}\ \mathrm{mol\cdot L^{-1}}$, tracer l'horizontale jusqu'à la courbe et lire l'abscisse du point d'intersection ;
- sur la droite $\ln c = f(t)$ de l'annexe 3 : placer l'ordonnée $\ln c_0 - \ln 2 = -2{,}6 - 0{,}7 = -3{,}3$ et lire l'abscisse correspondante sur la droite (figure 4).

On lit dans les deux cas $t_{1/2} \approx 12\ \mathrm{min}$. Pour un ordre 1, on peut contrôler que la concentration est encore divisée par deux sur l'intervalle suivant ($c_0/4$ atteint vers 24 min).

### Question 40 — Effet d'une température plus élevée

D'après la loi d'Arrhenius, $k = A\exp(-E_a/RT)$ avec $E_a > 0$ : **la constante de vitesse augmente** quand la température augmente. Comme $t_{1/2} = \ln 2/k$, **le temps de demi-réaction diminue** : la décomposition est plus rapide à chaud.

Ce résultat cinétique ne contredit pas la question 28 : la température agit en sens contraire sur la position de l'équilibre (thermodynamique) et sur la vitesse à laquelle il est atteint (cinétique).
