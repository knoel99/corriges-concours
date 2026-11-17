# Agrégation Chimie — Problème de chimie 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Sujet « Le Phosphore » : 76 questions en quatre parties (épreuve de 6 heures, calculatrice autorisée).

## Présentation du sujet

**Thème.** « Le Phosphore » : 76 questions en quatre parties — I. l'élément phosphore et sa RMN (Q1–Q11) ; II. l'acide phosphorique et les phosphates, procédé industriel de récupération (struvite) et dosage colorimétrique (Q12–Q30) ; III. réaction de Wittig, ylure non stabilisé puis stabilisé, études mécanistiques et stéréochimie (Q31–Q58) ; IV. phosphines en catalyse asymétrique : synthèse et dédoublement du BINAP, puis modélisation des effets non linéaires (Q59–Q76). Épreuve de 6 heures, calculatrice autorisée, sans document. Les questions fondamentales sont marquées d'une étoile (*) dans l'énoncé.

**Ce qu'en dit le rapport 2026.** Moyenne des admissibles 10,91/20, des admis 12,87/20. « 5 % du total des points de la copie ont été attribués à la présentation, à la qualité de rédaction, au soin apporté à l’écriture et aux schémas. » « Le sujet comportait 28 questions fondamentales sur un total de 75 questions […]. Elles représentaient 38 % du barème total » avec « un taux de réussite moyen de 26 %, contre environ 18 % pour l’ensemble des questions ». Sur la rigueur exigée partout : « les mécanismes doivent être écrits en faisant partir les flèches courbes des doublets non liants et pas des charges négatives », « tous les doublets non liants d’un atome doivent être représentés », et « une constante thermodynamique d’équilibre est sans dimension et doit donc faire apparaître la concentration standard C⁰ ».

**Difficulté et gestion du temps.** Sujet long mais balisé : sécuriser d'abord les questions fondamentales (*) — restitutions de cours et applications directes (26 % de réussite seulement). Parties II et IV comportent les blocs calculatoires les plus denses (tampon phosphate et Debye-Hückel Q14–Q17 ; struvite Q18–Q23 ; effets non linéaires Q68–Q76). Une coquille de l'énoncé est à signaler en Q52 (renvoi de figure). Répartition indicative : environ 1 h 15 pour la partie I, 1 h 45 pour la partie II, 1 h 45 pour la partie III, 1 h 15 pour la partie IV, en gardant du temps pour les schémas (Lewis, mécanismes, Cram) demandés explicitement.

---

# Agrégation Chimie — Problème de chimie 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 6 heures, calculatrice autorisée, sans document. Sujet « Le Phosphore » : 76 questions en quatre parties — I. l'élément phosphore et sa RMN (Q1–Q11) ; II. l'acide phosphorique et les phosphates (Q12–Q30) ; III. réaction de Wittig, ylure non stabilisé puis stabilisé (Q31–Q58) ; IV. phosphines en catalyse asymétrique, synthèse du BINAP et effets non linéaires (Q59–Q76). Les questions suivies d'une étoile (*) sont les questions fondamentales signalées par l'énoncé.

## I. L'élément phosphore et sa RMN

### Question 1*

> [!INDICATION]
> Remplissage des sous-couches pour $Z=15$ ; nombre de neutrons $N=A-Z$.

#### Solution

$^{31}_{15}\mathrm{P}$ : $Z=15$ électrons, configuration électronique

$$
1s^2\,2s^2\,2p^6\,3s^2\,3p^3.
$$

Nombre de neutrons : $N=A-Z=31-15=\boxed{16}$. $\square$

### Question 2

> [!INDICATION]
> En $\beta^{-}$, un neutron devient un proton : $Z\to Z+1$, $A$ constant. Ne pas oublier l'antineutrino.

#### Solution

Émission $\beta^{-}$ : un neutron se transforme en proton, $Z\to Z+1$, $A$ constant :

$$
^{32}_{15}\mathrm{P}\;\longrightarrow\;^{32}_{16}\mathrm{S}+\,^{\,0}_{-1}e+\bar\nu_e.
$$

La radioactivité $\beta^{-}$ s'accompagne d'un **changement d'élément** (P → S). $\square$

> [!JURY]
> « la radioactivité conduit à un changement d'élément, ce qui n'est pas maîtrisé par l'ensemble des candidats. »

### Question 3*

> [!INDICATION]
> Désintégration = cinétique d'ordre 1 : donner l'expression de $[^{32}\mathrm{P}](t)$ **et** $t_{1/2}=\ln2/\lambda$.

#### Solution

Le temps de demi-vie $t_{1/2}$ est la durée au bout de laquelle la moitié des noyaux initialement présents se sont désintégrés. La désintégration suit une loi d'ordre 1 :

$$
[^{32}\mathrm{P}](t)=[^{32}\mathrm{P}]_0\,e^{-\lambda t}.
$$

À $t=t_{1/2}$ : $[^{32}\mathrm{P}]_0/2=[^{32}\mathrm{P}]_0\,e^{-\lambda t_{1/2}}$, d'où

$$
\begin{aligned}
\lambda\\
& =\frac{\ln 2}{t_{1/2}}\\
& =\frac{0{,}693}{14{,}26~\mathrm{j}}\\
& =4{,}86\times10^{-2}~\mathrm{j^{-1}}\\
& =\boxed{5{,}6\times10^{-7}~\mathrm{s^{-1}}}.
\end{aligned}
$$
$\square$

> [!JURY]
> « de nombreux candidats se sont contentés de répondre à la première et à la dernière partie de la question » : donner aussi l'évolution $[^{32}\mathrm{P}](t)$.

### Question 4*

> [!INDICATION]
> Condition RMN : spin nucléaire $I\neq0$ ; $I=0$ si $A$ et $Z$ tous deux pairs.

#### Solution

Un noyau est observable en RMN si son **spin nucléaire $I$ est non nul**. $I=0$ lorsque $A$ **et** $Z$ sont tous deux pairs. Pour $^{31}\mathrm{P}$,
 $A=31$ est impair : $I\neq0$ (ici $I=\tfrac12$), le noyau est **actif en RMN**. $\square$

### Question 5*

> [!INDICATION]
> Appliquer le critère de Q4 à $^{32}\mathrm{P}$ ($A$ pair, $Z$ impair).

#### Solution

$^{32}\mathrm{P}$ : $A=32$ (pair), $Z=15$ (impair) : $A$ et $Z$
 ne sont pas tous deux pairs, donc $I\neq0$ — le noyau serait **observable en RMN**. $\square$

### Question 6*

> [!INDICATION]
> En RMN $^{31}\mathrm{P}$ de $\mathrm{PH_3}$ : 3 protons équivalents couplés à P, règle $n+1$.

#### Solution

En RMN $^{31}\mathrm{P}$ de $\mathrm{PH_3}$, le phosphore couple avec les 3 protons équivalents ($I=\tfrac12$) : multiplicité $n+1=4$, soit un **quadruplet** d'intensités relatives $1:3:3:1$. $\square$

### Question 7*

> [!INDICATION]
> En RMN $^1\mathrm{H}$ : chaque H ne couple qu'avec le seul P, règle $n+1$.

#### Solution

En RMN $^1\mathrm{H}$ de $\mathrm{PH_3}$, chaque proton couple avec un unique noyau $^{31}\mathrm{P}$ : **doublet**, intensités $1:1$. $\square$

### Question 8*

> [!INDICATION]
> P engage 5 liaisons ; représenter **tous** les doublets non liants des oxygènes.

#### Solution

Structure de Lewis du diéthylphosphonate $\mathrm{HP(O)(OEt)_2}$ : P central, lié à H (liaison simple), à O par une double liaison $\mathrm{P{=}O}$, et à deux oxygènes $\mathrm{O{-}CH_2CH_3}$ (liaisons simples) ; chaque oxygène porte deux doublets non liants. *Schéma attendu : P au centre, une liaison P–H, une double liaison P=O, deux liaisons P–O–CH₂CH₃, tous les doublets non liants des oxygènes représentés.* P engage 5 liaisons. $\square$

> [!JURY]
> « une structure de Lewis doit présenter toutes les liaisons, ainsi que les doublets non liants, et a été souvent confondue avec une formule semi-développée ».

### Question 9*

> [!INDICATION]
> L'exposant d'une constante de couplage = nombre de liaisons entre les deux noyaux.

#### Solution

L'exposant des constantes de couplage indique le **nombre de liaisons** entre les deux noyaux : $^{1}J$ = couplage à travers 1 liaison (noyaux directement liés), $^{2}J$ = 2 liaisons, $^{3}J$ = 3 liaisons (couplage vicinal). $\square$

### Question 10*

> [!INDICATION]
> $\nu\propto\gamma$ à $B_0$ fixé ; le champ est le même que celui du spectre $^1\mathrm{H}$ à 400 MHz.

#### Solution

À champ $B_0$ fixé, $\nu=\gamma B_0/(2\pi)$. Le spectromètre étant calibré à $f=400~\mathrm{MHz}$ pour $^1\mathrm{H}$, le champ $B_0$ est commun et

$$
\begin{aligned}
\nu_{\text{réf}}(^{31}\mathrm{P})\\
& =\frac{\gamma_P}{\gamma_H}\,f\\
& =\frac{10{,}841}{26{,}752}\times400~\mathrm{MHz}\\
& =162{,}1~\mathrm{MHz}.
\end{aligned}
$$

Pour un signal de déplacement chimique $\delta$ (référence $\mathrm{H_3PO_4}$ à 0) :

$$
\boxed{\nu=\frac{\gamma_P}{\gamma_H}\,f\left(1+\delta\times10^{-6}\right).}
$$

L'écart à la référence vaut $\Delta\nu=\delta\times10^{-6}\times\nu_{\text{réf}}=7{,}3\times10^{-6}\times162{,}1\times10^{6}=\boxed{1{,}18\times10^{3}~\mathrm{Hz}}$, soit $\nu\approx162{,}1~\mathrm{MHz}+1183~\mathrm{Hz}$. $\square$

### Question 11

> [!INDICATION]
> Spectre $^{31}\mathrm{P}$ **non découplé** : compter les H couplés à P et les liaisons qui les séparent ($^{1}J$, $^{3}J$, $^{4}J$).

#### Solution

Spectre $^{31}\mathrm{P}$ **non découplé** du proton de $\mathrm{HP(O)(OEt)_2}$ : trois types de couplages $^1\mathrm{H}$–$^{31}\mathrm{P}$.

- le H directement lié à P : $^{1}J\approx650~\mathrm{Hz}$ (1 H) → **doublet** ;
- les 4 H des deux $\mathrm{O{-}CH_2}$ (P–O–C–H, 3 liaisons) : $^{3}J\approx8~\mathrm{Hz}$ → **quintuplet** (intensités $1:4:6:4:1$) ;
- les 6 H des $\mathrm{CH_3}$ (4 liaisons) : $^{4}J<1~\mathrm{Hz}$, non observé.

Le spectre est un **doublet de quintuplets** centré sur $\delta=7{,}3~\mathrm{ppm}$ : deux massifs séparés d'environ $650~\mathrm{Hz}$, chacun éclaté en 5 raies espacées d'environ $8~\mathrm{Hz}$. *Schéma attendu : à $\delta=7{,}3~\mathrm{ppm}$, deux groupes de 5 raies $(1:4:6:4:1)$,
 séparation inter-groupes $^{1}J\simeq650~\mathrm{Hz}$, intra-groupe $^{3}J\simeq8~\mathrm{Hz}$.* $\square$

## II. L'acide phosphorique et les phosphates

### Question 12*

> [!INDICATION]
> Ajuster l'équation élément par élément (y compris l'eau de cristallisation) ; nommer le type de réaction.

#### Solution

$$
\mathrm{Ca_{10}(PO_4)_6F_2}+10\,\mathrm{H_2SO_4}+20\,\mathrm{H_2O}\rightarrow6\,\mathrm{H_3PO_4}+10\,\mathrm{CaSO_4\cdot 2H_2O}+2\,\mathrm{HF}.
$$

Vérification : Ca $10=10$ ; P $6=6$ ; F $2=2$ ; S $10=10$ ; O $24+40+20=84=24+60$
 ; H $20+40=60=18+40+2$. Il s'agit d'une **réaction acido-basique** (déplacement des phosphates par l'acide sulfurique, plus fort), accompagnée de la **précipitation** du sulfate de calcium. $\square$

### Question 13*

> [!INDICATION]
> Axe gradué en **pH** (pas en p$K_a$), bornes aux trois p$K_a$.

#### Solution

Diagramme de prédominance sur un axe de **pH** (et non de p$K_a$), borné aux trois p$K_a$ :

$$
\mathrm{H_3PO_4}\;|\;2{,}12\;|\;\mathrm{H_2PO_4^-}\;|\;7{,}18\;|\;\mathrm{HPO_4^{2-}}\;|\;12{,}36\;|\;\mathrm{PO_4^{3-}}.
$$

*Schéma attendu : axe horizontal gradué en pH, les quatre espèces séparées par les trois p$K_a$.* $\square$

> [!JURY]
> le jury s'inquiète de voir « des domaines de prédominances sur une échelle de pKa et non de pH ».

### Question 14*

> [!INDICATION]
> Dans un tampon, la réaction prépondérante est acide + base conjuguée ($K=1$) : utiliser directement Henderson-Hasselbalch.

#### Solution

Tampon $\mathrm{HPO_4^{2-}/H_2PO_4^-}$ (p$K_{a2}=7{,}18$) ; la réaction prépondérante est l'échange acide/base conjuguée ($K=1$). Avec $[\mathrm{HPO_4^{2-}}]=10{,}1~\mathrm{mmol\cdot L^{-1}}$ et $[\mathrm{H_2PO_4^-}]=1{,}8~\mathrm{mmol\cdot L^{-1}}$ :

$$
\begin{aligned}
\mathrm{pH}\\
& =\mathrm{p}K_{a2}+\log\frac{[\mathrm{HPO_4^{2-}}]}{[\mathrm{H_2PO_4^-}]}\\
& =7{,}18+\log\frac{10{,}1}{1{,}8}\\
& =7{,}18+0{,}75\\
& =\boxed{7{,}9}.
\end{aligned}
$$
$\square$

> [!JURY]
> « Dans la solution tampon, la réaction prépondérante est celle de l'acide avec sa base conjuguée (dont la constante vaut K = 1) » ; on attend des pH « proches de 7,4 », un pH de 14 signale un problème.

### Question 15

> [!INDICATION]
> Passer aux activités, appliquer Debye-Hückel ($\log\gamma_i=-z_i^2A\sqrt I$), calculer $I$ avec **tous** les ions.

#### Solution

En écrivant la définition de $K_{a2}$ avec les activités puis la loi de Debye-Hückel $\log\gamma_i=-z_i^2A\sqrt I$ :

$$
\log\frac{\gamma_{\mathrm{HPO_4^{2-}}}}{\gamma_{\mathrm{H_2PO_4^-}}}=-\left(4-1\right)A\sqrt I=-3A\sqrt I,
$$

d'où

$$
\boxed{\mathrm{p}K_{a2}'=\mathrm{p}K_{a2}-3A\sqrt I.}
$$

$$
\mathrm{pH}=\mathrm{p}K_{a2}'+\log\frac{[\mathrm{HPO_4^{2-}}]}{[\mathrm{H_2PO_4^-}]}.
$$

Force ionique (tous les ions, en mol·L⁻¹) : $\mathrm{Na^+}$ $0{,}1572$ ; $\mathrm{K^+}$ $0{,}0045$ ; $\mathrm{Cl^-}$
 $0{,}1397$ ; $\mathrm{HPO_4^{2-}}$ $0{,}0101$ ; $\mathrm{H_2PO_4^-}$ $0{,}0018$ :

$$
I=\tfrac12\big(0{,}1572+0{,}0045+0{,}1397+4\times0{,}0101+0{,}0018\big)=0{,}17~\mathrm{mol\cdot L^{-1}}.
$$

$\sqrt I=0{,}415$ et $A=0{,}509$ : $\mathrm{p}K_{a2}'=7{,}18-3\times0{,}509\times0{,}415=6{,}55$, d'où

$$
\mathrm{pH}=6{,}55+0{,}75=\boxed{7{,}3}.
$$
$\square$

> [!JURY]
> « Il y a eu également des erreurs pour le calcul de la force ionique (tous les ions doivent être pris en compte) et des confusions entre activité et concentration pour le calcul du pH. »

### Question 16*

> [!INDICATION]
> Appliquer la relation empirique donnant p$K_{a2}''$ à la force ionique calculée.

#### Solution

Avec la relation empirique à $I=0{,}17~\mathrm{mol\cdot L^{-1}}$ :

$$
\begin{aligned}
\mathrm{p}K_{a2}''\\
& =7{,}18-1{,}52\sqrt I+1{,}96\,I\\
& =7{,}18-1{,}52\times0{,}415+1{,}96\times0{,}17\\
& =6{,}89,
\end{aligned}
$$

$$
\begin{aligned}
\mathrm{pH}\\
& =6{,}89+\log\frac{10{,}1}{1{,}8}\\
& =6{,}89+0{,}75\\
& =\boxed{7{,}6}.
\end{aligned}
$$
$\square$

### Question 17

> [!INDICATION]
> Imposer le rapport base/acide correspondant à pH 7,4 et résoudre en $x$ ; l'acide ajouté n'est pas $(10^{-\mathrm{pH}})V$.

#### Solution

HCl convertit $\mathrm{HPO_4^{2-}}$ en $\mathrm{H_2PO_4^-}$ ; à $\mathrm{pH}=7{,}4$ le rapport vaut $10^{7{,}4-6{,}89}=10^{0{,}51}=3{,}3$. Avec $x$ (mmol·L⁻¹) la concentration d'HCl ajoutée :

$$
\begin{aligned}
\frac{10{,}1-x}{1{,}8+x}\\
& =3{,}3\\
& \Rightarrow 10{,}1-x\\
& =5{,}87+3{,}26x\\
& \Rightarrow x\\
& =\boxed{0{,}99~\mathrm{mmol\cdot L^{-1}}}.
\end{aligned}
$$

(L'ajout d'acide fort ne vaut pas $(10^{-\mathrm{pH}})V$ : c'est l'équilibre de contrôle du tampon qui fixe le rapport base/acide.) $\square$

> [!JURY]
> « La quantité d'acide fort à ajouter pour faire varier le pH d'une solution tampon n'est pas égale à Δ(10⁻ᵖᴴ)×V. Si tel était le cas ce ne serait pas une solution tampon mais de l'eau ».

### Question 18*

> [!INDICATION]
> Convertir la teneur massique en concentration molaire, puis appliquer les proportions P:Mg:N.

#### Solution

Teneur en P : $[\mathrm{P}]=\dfrac{1452~\mathrm{mg\cdot L^{-1}}}{31~\mathrm{g\cdot mol^{-1}}}=46{,}8~\mathrm{mmol\cdot L^{-1}}$. Proportions $\mathrm{P:Mg:N}=1:1{,}2:1$, donc

$$
\begin{aligned}
n(\mathrm{MgCl_2})\\
& =1{,}2\times46{,}8\\
& =\boxed{56{,}2~\mathrm{mmol\cdot L^{-1}}}
\end{aligned}
$$

$$
\begin{aligned}
n(\mathrm{NH_4Cl})\\
& =\boxed{46{,}8~\mathrm{mmol\cdot L^{-1}}}.
\end{aligned}
$$
$\square$

### Question 19*

> [!INDICATION]
> Depuis l'espèce prédominante à chaque pH, enchaîner les rapports $10^{\mathrm{pH}-\mathrm{p}K_a}$.

#### Solution

À $\mathrm{pH}=3{,}6$ (entre p$K_{a1}$ et p$K_{a2}$), l'espèce prédominante est $\mathrm{H_2PO_4^-}\approx46{,}8~\mathrm{mmol\cdot L^{-1}}$, et

$$
\begin{aligned}
[\mathrm{PO_4^{3-}}]\\
& =[\mathrm{H_2PO_4^-}]\,10^{\mathrm{pH}-\mathrm{p}K_{a2}}\,10^{\mathrm{pH}-\mathrm{p}K_{a3}}\\
& =4{,}68\times10^{-2}\times10^{-3{,}58}\times10^{-8{,}76}\\
& =\boxed{2{,}1\times10^{-14}~\mathrm{mol\cdot L^{-1}}}.
\end{aligned}
$$

À $\mathrm{pH}=9$ (entre p$K_{a2}$ et p$K_{a3}$), prédomine $\mathrm{HPO_4^{2-}}$ :

$$
\begin{aligned}
[\mathrm{PO_4^{3-}}]\\
& =[\mathrm{HPO_4^{2-}}]\,10^{9-12{,}36}\\
& =4{,}68\times10^{-2}\times10^{-3{,}36}\\
& =\boxed{2{,}0\times10^{-5}~\mathrm{mol\cdot L^{-1}}}.
\end{aligned}
$$

$\mathrm{PO_4^{3-}}$ existe à tous les pH, même acide, en quantité très faible (ultraminoritaire $\neq$ absent). $\square$

### Question 20*

> [!INDICATION]
> Couple $\mathrm{NH_4^+/NH_3}$ (p$K_a=9{,}25$) ; le pH est fixé, on détermine directement les quantités (pas $[\mathrm B^-]=[\mathrm H^+]$).

#### Solution

Couple $\mathrm{NH_4^+/NH_3}$, p$K_a=9{,}25$ ; $N_{\text{tot}}=46{,}8~\mathrm{mmol\cdot L^{-1}}$. À $\mathrm{pH}=3{,}6\ll\mathrm{p}K_a$ : $[\mathrm{NH_4^+}]\approx\boxed{46{,}8~\mathrm{mmol\cdot L^{-1}}}$.
 À $\mathrm{pH}=9$ : $\frac{[\mathrm{NH_4^+}]}{[\mathrm{NH_3}]}=10^{9{,}25-9}=1{,}78$, d'où $[\mathrm{NH_4^+}]=\frac{1{,}78}{2{,}78}\times46{,}8=\boxed{30~\mathrm{mmol\cdot L^{-1}}}$. (Le pH étant contrôlé, on ne pose pas $[\mathrm B^-]=[\mathrm H^+]$.) $\square$

### Question 21*

> [!INDICATION]
> Écrire $K_s$, calculer le produit ionique $Q$ dans chaque réacteur et comparer à $K_s$.

#### Solution

$$
\begin{aligned}
\mathrm{MgNH_4PO_4\cdot 6H_2O}\\
& \rightleftharpoons\mathrm{Mg^{2+}}+\mathrm{NH_4^+}+\mathrm{PO_4^{3-}}+6\,\mathrm{H_2O}
\end{aligned}
$$

$$
\begin{aligned}
K_s\\
& =\frac{[\mathrm{Mg^{2+}}][\mathrm{NH_4^+}][\mathrm{PO_4^{3-}}]}{(C^0)^3}\\
& =10^{-13{,}15}\\
& =7{,}1\times10^{-14}.
\end{aligned}
$$

Réacteur 4 ($\mathrm{pH}=3{,}6$) : $Q=5{,}62\times10^{-2}\times4{,}68\times10^{-2}\times2{,}1\times10^{-14}=5{,}6\times10^{-17}<K_s$ → pas de précipitation. Réacteur 1 ($\mathrm{pH}=9$) : $Q=5{,}62\times10^{-2}\times3{,}0\times10^{-2}\times2{,}0\times10^{-5}=3{,}4\times10^{-8}\gg K_s$ → précipitation. C'est l'augmentation de $[\mathrm{PO_4^{3-}}]$ avec le pH qui déclenche la sursaturation. $\square$

> [!JURY]
> « les calculs des conditions de précipitation ont souvent été inexistants (Q vs K) » ; « il ne faut pas confondre ultraminoritaire et absence d’une espèce chimique en solution ».

### Question 22

> [!INDICATION]
> $K_s$ dépend de $T$ : la température fixe la sursaturation, donc nucléation/croissance et qualité cristalline.

#### Solution

$K_s$ (donc la solubilité) dépend de la température $T$. Fixer $T=298~\mathrm{K}$ impose un degré de sursaturation reproductible, qui contrôle les vitesses de **nucléation** et de **croissance** : on obtient des **cristaux de struvite de taille et de pureté maîtrisées**, directement réutilisables comme engrais. Une température mal contrôlée modifierait la solubilité, donc le rendement et la qualité cristalline. $\square$

### Question 23*

> [!INDICATION]
> Masse maximale = $n(\mathrm P)\times M(\text{struvite})$ par m³ ; rendement = masse réelle / masse maximale.

#### Solution

$M(\mathrm{MgNH_4PO_4\cdot 6H_2O})=24{,}3+14+4+31+64+108=245{,}3~\mathrm{g\cdot mol^{-1}}$. Par m³ : $n(\mathrm P)=46{,}8~\mathrm{mol}$, d'où

$$
m_{\max}=46{,}8\times245{,}3=11{,}48~\mathrm{kg\cdot m^{-3}}\approx\boxed{11{,}5~\mathrm{kg\cdot m^{-3}}}.
$$

Rendement de récupération : $\frac{11{,}40}{11{,}48}=\boxed{99~\%}$ (un rendement de 30 % ne serait pas cohérent avec un procédé industriel). $\square$

> [!JURY]
> « un rendement de 30 % de récupération n’est pas cohérent avec un processus industriel et doit interroger. »

### Question 24*

> [!INDICATION]
> Dans un sel, les contre-ions ($\mathrm{NH_4^+}$) ne font pas partie de l'édifice : calculer le n.o. sur l'anion seul.

#### Solution

$\mathrm{MoO_4^{2-}}$ : $n.o.(\mathrm{Mo})+4(-2)=-2\Rightarrow\boxed{+\mathrm{VI}}$. Dans $(\mathrm{NH_4})_6\mathrm{Mo_7O_{24}}$, les 6 $\mathrm{NH_4^+}$ sont des contre-ions ($+6$)
 : l'édifice anionique est $\mathrm{Mo_7O_{24}^{6-}}$, d'où $7\,n.o.(\mathrm{Mo})+24(-2)=-6\Rightarrow n.o.(\mathrm{Mo})=\boxed{+\mathrm{VI}}$. $\square$

> [!JURY]
> « l’ammonium n’était qu’un contre-ion positif […] et on n’attribue pas un nombre d’oxydation à un édifice polyatomique ».

### Question 25*

> [!INDICATION]
> n.o. par les électronégativités (liaisons attribuées à O), pas égal au nombre de liaisons ; justifier par Lewis.

#### Solution

$\mathrm{H_3PO_4}$ : $n.o.(\mathrm{P})+3(+1)+4(-2)=0\Rightarrow\boxed{+\mathrm{V}}$. Justification par Lewis : P lié à une double liaison $\mathrm{P{=}O}$ et à trois $\mathrm{O{-}H}$ ; chaque liaison P–O est attribuée à O (plus électronégatif), P perd ses 5 électrons de valence → $+\mathrm V$. (Le n.o. n'est pas égal au nombre de liaisons.) $\square$

> [!JURY]
> « le nombre d’oxydation d’un atome [n'est pas] égal au nombre de liaisons qu’il forme ».

### Question 26

> [!INDICATION]
> Électroneutralité de $[\mathrm{H_4PMo_{12}O_{40}}]^{3-}$ avec $x$ Mo à +VI et $12-x$ à +V.

#### Solution

Dans $[\mathrm{H_4PMo_{12}O_{40}}]^{3-}$ : $4(+1)+(+5)+[6x+5(12-x)]+40(-2)=-3$, soit $-11+x=-3\Rightarrow x=8$. Donc **8 atomes de Mo au degré +VI** et **4 au degré +V**. $\square$

### Question 27

> [!INDICATION]
> Exploiter le **contraste** entre la figure a (témoin sans phosphate) et la figure b.

#### Solution

À faible acidité (0 et 4 mmol de $\mathrm{H^+}$), le molybdate se réduit **même sans phosphate** (figure a) : bleu parasite (faux positif). À forte acidité (16–20 mmol), le complexe ne se forme **plus**, même avec $\mathrm{PO_4^{3-}}$ (figure b). Entre 8 et 12 mmol de $\mathrm{H^+}$ : bleu intense **uniquement** en présence de phosphate et incolore sans → bon contraste et sélectivité. L'objectif est le **contraste entre les deux figures**, témoin compris. $\square$

> [!JURY]
> « beaucoup de copies ne discutent que de la figure b et pas de la figure a témoin. L’objectif est de voir le bon contraste entre les deux ».

### Question 28

> [!INDICATION]
> Choisir les quantités sur le plateau du signal utile (105 nmol) tout en gardant le témoin (0 nmol) bas.

#### Solution

Pour 105 nmol de $\mathrm{PO_4^{3-}}$, la courbe d'absorbance sature ; le témoin (0 nmol) reste faible. On retient $24{,}3~\mu\mathrm{mol}$ de molybdate d'ammonium et $5{,}68~\mu\mathrm{mol}$ d'acide ascorbique : plateau du signal utile et témoin bas, soit un **contraste maximal** pour la quantification. $\square$

### Question 29

> [!INDICATION]
> Objectif : la droite d'étalonnage $A=f(n_{\mathrm{PO_4^{3-}}})$ pour une détermination quantitative.

#### Solution

Mesurer l'absorbance (à $820~\mathrm{nm}$) pour des quantités variables et connues de $\mathrm{PO_4^{3-}}$ établit la **droite d'étalonnage** $A=f(n_{\mathrm{PO_4^{3-}}})$ (Beer-Lambert, $R^2=0{,}9992$) : elle valide la linéarité et autorise la détermination quantitative d'une teneur inconnue en phosphate. $\square$

### Question 30

> [!INDICATION]
> Stœchiométrie de l'équation a (Mo/P) ; bilan électronique : 4 Mo réduits, 2 e⁻ par ascorbique → ascorbique/P.

#### Solution

Équation a : 12 $\mathrm{MoO_4^{2-}}$ pour 1 $\mathrm{PO_4^{3-}}$ → rapport théorique **Mo/P = 12**. Réduction (Q26) : 4 Mo passent de +VI à +V (4 électrons) ; chaque acide ascorbique fournit 2 électrons → rapport théorique **ascorbique/P = 2**. Conditions optimisées (105 nmol de $\mathrm{PO_4^{3-}}$) : Mo/P $=24{,}3\times10^{-6}/105\times10^{-9}\approx2{,}3\times10^{2}$ et ascorbique/P $\approx54$ : les réactifs sont en **large excès** devant la stœchiométrie, assurant réaction totale et signal maximal. $\square$

## III. Réaction de Wittig

### A — Ylure non stabilisé

### Question 31*

> [!INDICATION]
> KHMDS est une **base** : elle déprotone en $\alpha$ de P ; écrire les deux formes mésomères de l'ylure.

#### Solution

Le KHMDS est une base forte qui arrache un proton en $\alpha$ du phosphore du sel de phosphonium. L'ylure **1** est $\mathrm{Ph_2(Et)P{=}CH{-}CH_3}$ (non stabilisé), de formes mésomères :

$$
\mathrm{Ph_2(Et)P^{+}{-}CH^{-}{-}CH_3}\;\longleftrightarrow\;\mathrm{Ph_2(Et)P{=}CH{-}CH_3}.
$$

Le carbanion n'est stabilisé par aucun groupe électroattracteur. *Schéma attendu : les deux formes mésomères, avec tous les doublets non liants.* $\square$

> [!JURY]
> « un certain nombre de candidats n’ont pas compris que le KHMDS est une base, ou qui ont fait intervenir les substituants du phosphore dans l’écriture des formes mésomères de l’ylure ».

### Question 32

> [!INDICATION]
> Configuration Z : les deux substituants volumineux du même côté de la double liaison.

#### Solution

Isomère majoritaire **Z** du composé 2 : double liaison $\mathrm{CH{=}CH}$ portant du même côté la chaîne $\mathrm{C(CH_3)_2CH_2Ph}$ et le groupe $\mathrm{CH_3}$, et de l'autre côté les deux H vinyliques. *Schéma attendu : alcène $\mathrm{Ph{-}CH_2{-}C(CH_3)_2{-}CH{=}CH{-}CH_3}$ en configuration Z.* $\square$

### Question 33*

> [!INDICATION]
> Stabilité thermodynamique : l'isomère E minimise la gêne stérique (substituants *trans*).

#### Solution

L'isomère **E** est thermodynamiquement **plus stable** que le Z : les deux substituants volumineux y sont en position *trans*, ce qui minimise la gêne stérique. $\square$

### Question 34

> [!INDICATION]
> $^{3}J_{\text{cis}}<^{3}J_{\text{trans}}$ : attribuer chaque isomère à sa constante vinyle–vinyle, en schéma.

#### Solution

$^{3}J_{\text{cis}}=4$–$12~\mathrm{Hz}$, $^{3}J_{\text{trans}}=14$–$19~\mathrm{Hz}$. Isomère **a** : $^{3}J_{\mathrm{H-H}}=12{,}0~\mathrm{Hz}$
 → couplage **cis** → **Z**. Isomère **b** : $15{,}5~\mathrm{Hz}$ → **trans** → **E**. *Schéma attendu (forme demandée) : pour chaque isomère, les deux H vinyliques avec leurs $\delta$ ($5{,}37$ et $5{,}27~\mathrm{ppm}$ pour a ; $5{,}45$
 et $5{,}23~\mathrm{ppm}$ pour b), $^{3}J_{1\text{-}2}$ entre eux ($12{,}0$ / $15{,}5~\mathrm{Hz}$), $^{3}J$
 avec le $\mathrm{CH_3}$ ($7{,}2$ / $6{,}4~\mathrm{Hz}$) et $^{4}J$ allylique ($1{,}6~\mathrm{Hz}$).*
 $\square$

### Question 35*

> [!INDICATION]
> Peracide ; addition concertée et ***syn*** de l'oxygène : stéréospécificité conservée.

#### Solution

On époxyde les alcènes correspondants $\mathrm{CH_3{-}CH{=}CH{-}C(CH_3)_2CH_2Ph}$ (E et Z) par un **peracide** (ex. m-CPBA). L'addition d'oxygène est **concertée et *syn*** (état de transition « papillon ») : l'alcène *trans* donne l'époxyde *trans*, le *cis* donne le *cis*. *Schéma attendu : mécanisme concerté, transfert d'un atome O du peracide vers la face de l'alcène, un seul état de transition cyclique.* $\square$

### Question 36

> [!INDICATION]
> $S_N2$ de $\mathrm{Ph_2P^-}$ sur le carbone le **moins encombré**, avec inversion de Walden ; représenter en Cram.

#### Solution

Ouverture de l'époxyde par $\mathrm{Ph_2P^{-}}$ sur le carbone le moins encombré, par $S_N2$ avec **inversion de Walden**. Le composé **3** est $\mathrm{Ph_2P{-}CH(CH_3){-}CH(OH){-}C(CH_3)_2{-}CH_2Ph}$. *Schéma attendu (Cram) : les deux isomères a et b, différant par la configuration relative des deux centres $\mathrm{CH(CH_3)}$ et $\mathrm{CH(OH)}$ ; l'époxyde trans conduit à a, le cis à b.* $\square$

> [!JURY]
> « bon nombre d’ouvertures d’époxydes n’ont pas respecté une inversion de Walden due à une SN2 ».

### Question 37

> [!INDICATION]
> L'anion $\mathrm{Ph_2P^-}$ attaque par l'un de ses deux doublets non liants ; régiosélectivité = accès stérique.

#### Solution

$\mathrm{Ph_2PLi}$ fournit l'**anion** $\mathrm{Ph_2P^{-}}$ (contre-ion $\mathrm{Li^+}$), nucléophile mou. L'un de ses deux doublets non liants attaque le carbone **le moins encombré** de l'époxyde (le $\mathrm{CH{-}CH_3}$, pas le CH voisin du $\mathrm{C(CH_3)_2}$),
 par $S_N2$ (inversion de Walden) : ouverture du cycle en alcoolate, protonation ($\mathrm{H_3O^+}$) donnant l'alcool. La régiosélectivité vient de l'**accès stérique** au carbone attaqué. *Schéma attendu : flèche courbe partant d'un doublet non liant de $\mathrm{Ph_2P^-}$ vers le carbone, rupture de la liaison C–O, alcoolate formé ; tous les doublets non liants représentés.* $\square$

### Question 38

> [!INDICATION]
> Le doublet du P attaque $\mathrm{CH_3CH_2I}$ ($S_N2$) ; écrire le sel **complet**, avec $\mathrm{I^-}$.

#### Solution

Le doublet non liant du phosphore de **3** attaque le carbone électrophile de l'iodoéthane $\mathrm{CH_3CH_2I}$ ($S_N2$, $\mathrm{I^-}$ partant). Le composé **4** est le sel de phosphonium **complet** :

$$
[\mathrm{Ph_2(Et)P{-}CH(CH_3){-}CH(OH){-}C(CH_3)_2CH_2Ph}]^+\,\mathrm{I^-}.
$$

*Schéma attendu (Cram) : configurations des deux centres inchangées pour a et b.* $\square$

> [!JURY]
> « Un produit chimique doit être complet, car il sera isolé ainsi : s'il s'agit d'un sel, l'ensemble des ions doit être écrit (iodure...) ».

### Question 39

> [!INDICATION]
> Déprotonation de OH puis attaque intramoléculaire de O sur $\mathrm{P^+}$ → oxaphosphétane ; corréler cis/trans et a/b.

#### Solution

NaHMDS déprotone l'hydroxyle en alcoolate : $\mathrm{P^{+}{-}CH(CH_3){-}CH(O^-){-}R}$. L'oxygène attaque le phosphore **intramoléculairement** → oxaphosphétane **5** (cycle à 4 chaînons P–C–C–O). *Schéma attendu : flèche partant du doublet de l'alcoolate vers $\mathrm{P^+}$, fermeture du cycle.* La décomposition étant *syn* (Q40), l'oxaphosphétane *cis* donne l'alcène **Z (a)** et le *trans* l'alcène **E (b)**. $\square$

### Question 40

> [!INDICATION]
> Cyclo-réversion [2+2] ***syn*** : faire apparaître la stéréochimie de l'oxaphosphétane et l'alcène formé.

#### Solution

L'oxaphosphétane se fragmente par **cyclo-réversion [2+2]** : rupture *syn* des liaisons P–C et C–O, formation de l'alcène **2** et de l'oxyde de phosphine $\mathrm{Ph_2(Et)P{=}O}$. La réaction est **stéréospécifique** (*syn*) : chaque oxaphosphétane donne un seul alcène de configuration définie. *Schéma attendu : état de transition à 4 centres, deux flèches courbes, départ de $\mathrm{Ph_2EtP{=}O}$, stéréochimie de l'oxaphosphétane apparente.* $\square$

### Question 41

> [!INDICATION]
> Lire le minimum de la courbe de Karplus.

#### Solution

D'après la courbe de Karplus, $^{3}J$ est minimal (proche de 0, ici $\approx2~\mathrm{Hz}$) lorsque l'angle dièdre est **proche de $90°$** (entre $\sim80°$ et $100°$). $\square$

### Question 42

> [!INDICATION]
> $J_{\mathrm{P-H4}}$ faible → angle $\approx90°$ → conformation plane ; $J=11~\mathrm{Hz}$ → $\approx160°$ → papillon.

#### Solution

Isomère **b** : $J_{\mathrm{P-H4}}<1~\mathrm{Hz}$ → angle dièdre $\approx90°$ → **conformation plane** (dièdre C–C–C–H $\approx95°$). Isomère **a** : $J_{\mathrm{P-H4}}=11~\mathrm{Hz}$ → angle $\approx160°$ → conformation **plissée (« papillon »)**. La conformation plane correspond à l'**isomère b = E = oxaphosphétane trans**. $\square$

### Question 43

> [!INDICATION]
> Effet $-I$ du Cl → carbonyle plus électrophile ; l'autre aldéhyde est très encombré.

#### Solution

Le **4-chlorobenzaldéhyde** est plus réactif : Cl exerce un effet inductif attracteur ($-I$) qui appauvrit le carbonyle en électrons (carbone plus électrophile). L'aldéhyde $\mathrm{Ph{-}CH_2{-}C(CH_3)_2{-}CHO}$ est aliphatique et très **encombré** par le $\mathrm{C(CH_3)_2}$ voisin. $\square$

### Question 44

> [!INDICATION]
> Si la formation de l'oxaphosphétane était réversible, l'ylure régénéré réagirait avec l'aldéhyde le plus électrophile ; l'absence de cet alcène prouve l'**irréversibilité** → contrôle cinétique.

#### Solution

Si la formation de l'oxaphosphétane était **réversible**, l'ylure régénéré réagirait avec l'aldéhyde le plus électrophile (4-chlorobenzaldéhyde) pour donner $\mathrm{p{-}ClC_6H_4{-}CH{=}CH{-}CH_3}$. Cet alcène **n'est pas formé** : la formation de l'oxaphosphétane est **irréversible**, la réaction est sous **contrôle cinétique**. $\square$

> [!JURY]
> « les expériences de compétition avec le 4-chlorobenzaldéhyde […] tendaient à prouver que la réaction de Wittig […] n’est pas réversible ».

### Question 45

> [!INDICATION]
> Intermédiaires observés = oxaphosphétanes ; stéréochimie fixée à l'étape irréversible de leur formation.

#### Solution

Les intermédiaires observés par RMN sont les **oxaphosphétanes** (5a et 5b) ; aucune bétaïne distincte n'est détectée. Le rapport cis/trans des oxaphosphétanes égale le rapport Z/E des alcènes et la décomposition est stéréospécifique : la stéréochimie est **fixée dès l'étape irréversible de formation de l'oxaphosphétane** (addition de l'ylure sur l'aldéhyde). $\square$

### Question 46

> [!INDICATION]
> $\delta=32{,}8~\mathrm{ppm}$, type $\mathrm{R_3PO}$ : oxyde de phosphine.

#### Solution

Le signal croissant à $\delta=32{,}8~\mathrm{ppm}$ correspond à l'**oxyde de phosphine** $\mathrm{Ph_2(Et)P{=}O}$ (type $\mathrm{R_3PO}$, déplacement positif), produit de la décomposition des oxaphosphétanes. $\square$

### Question 47*

> [!INDICATION]
> Sous contrôle cinétique, comparer les énergies des deux états de transition pour prédire le produit majoritaire.

#### Solution

La réaction étant sous **contrôle cinétique** (Q44), le rapport des produits (Z/E) est fixé par la **différence d'énergie des états de transition** menant aux oxaphosphétanes cis et trans : le plus bas en énergie donne l'alcène majoritaire. Comparer ET1-cis et ET1-trans permet donc de **prédire l'issue stéréochimique** (l'analyse des états de transition n'a de sens que sous contrôle cinétique). $\square$

> [!JURY]
> « trop peu de candidats ont identifié que l'analyse des états de transition pour prédire le produit final n'a de sens que sous contrôle cinétique ».

### Question 48

> [!INDICATION]
> Dans l'ET1-trans plan : interaction 1,2-éclipsée $\mathrm{R_1/R_2}$ et gêne $\mathrm{R_1}$/ligand L.

#### Solution

Dans l'ET1-*trans* (conformation plutôt plane), deux interactions défavorables, absentes de l'ET1-*cis* (plissé) : (1) une interaction **1,2-éclipsée** entre $\mathrm{R_1}$ (carbone du carbonyle) et $\mathrm{R_2}$ (carbone de l'ylure) alignés dans le plan ; (2) une gêne stérique entre $\mathrm{R_1}$ et l'un des **ligands L du phosphore** (pseudo-axial). $\square$

### Question 49

> [!INDICATION]
> Lire la tendance Z/E en fonction du nombre de phényles sur P (figure 9).

#### Solution

D'après la figure 9 : $\mathrm{Ph_3P}$ → $Z/E=99/1$ ; $\mathrm{Ph_2EtP}$ → $5{,}7/1$ ; $\mathrm{Et_2PhP}$
 → $1{,}3/1$. **Plus le phosphore porte de groupes phényle, plus la réaction est Z-sélective.** $\square$

### Question 50

> [!INDICATION]
> Les gênes de l'ET1-trans impliquent L : discuter **chacun** des trois cas (Ph₃P, Ph₂EtP, Et₂PhP).

#### Solution

Les interactions défavorables de l'ET1-*trans* (Q48) impliquent les **ligands L** du phosphore. L = Ph (large) : gênes sévères → ET1-*trans* fortement déstabilisé → oxaphosphétane *cis* privilégié → forte sélectivité Z ($\mathrm{Ph_3P}$ : 99/1). Un Ph remplacé par Et (plus petit) : gêne diminuée → davantage d'E ($\mathrm{Ph_2EtP}$ : 5,7/1). Deux Et ($\mathrm{Et_2PhP}$) : sélectivité quasi perdue (1,3/1). Discussion cas par cas des trois ylures. $\square$

### B — Ylure stabilisé

### Question 51*

> [!INDICATION]
> Basicité de l'azote sp² de l'amidine : protonation → amidinium à charge délocalisée.

#### Solution

Le DBU est une amidine ; l'azote le plus basique est l'azote **sp² de l'imine** ($\mathrm{N{=}C}$) : sa protonation forme un cation **amidinium** dont la charge est **délocalisée sur les deux azotes** (mésomérie), fortement stabilisé. L'azote sp³ (amine) n'en bénéficie pas. $\square$

### Question 52

> [!INDICATION]
> Formes mésomères de l'ylure stabilisé par l'effet $-M$ de l'ester (charge sur O) ; coquille de figure à signaler (figure 10).

#### Solution

*(Coquille de l'énoncé signalée : la figure citée est la figure 10, et non la 9.)* Ylures : $\mathrm{Ph_3P{=}CH{-}CO_2Et}$ et $\mathrm{Ph_2(Me)P{=}CH{-}CO_2Et}$, de formes mésomères :

$$
\begin{aligned}
\mathrm{R_3P^{+}{-}CH^{-}{-}CO_2Et}\;\\
& \longleftrightarrow\;\mathrm{R_3P{=}CH{-}CO_2Et}\;\\
& \longleftrightarrow\;\mathrm{R_3P^{+}{-}CH{=}C(O^-){-}OEt}.
\end{aligned}
$$

Le carbanion est **conjugué au carbonyle de l'ester** (effet $-M$) : la charge négative est délocalisée sur l'oxygène → ylure **stabilisé**. *Schéma attendu : les formes mésomères en structures de Lewis complètes.* $\square$

> [!JURY]
> « Il y avait une erreur de numérotation d’une figure à la question 52, mais celle-ci a été très bien corrigée par les candidats » ; « dans les questions 51 et 52, il aurait voulu voir des formes mésomères représentées ».

### Question 53

> [!INDICATION]
> Ylure stabilisé → alcène **E** majoritaire ; représenter la double liaison en *trans*.

#### Solution

Alcène majoritaire **E** du composé 6 : $\mathrm{Ph{-}CH_2{-}CH_2{-}CH{=}CH{-}CO_2Et}$, la chaîne $\mathrm{CH_2CH_2Ph}$ et le groupe $\mathrm{CO_2Et}$ en *trans*. *Schéma attendu : double liaison $\mathrm{CH{=}CH}$ en configuration E.* $\square$

### Question 54

> [!INDICATION]
> LDA déprotone le $\mathrm{CH_2}$ (acide conjugué $\mathrm{iPr_2NH}$) ; addition de type aldol sur l'aldéhyde ; deux énantiomères.

#### Solution

LDA ($\mathrm{Li^+}$, $\mathrm{iPr_2N^-}$ ; acide conjugué $\mathrm{iPr_2NH}$) déprotone le $\mathrm{CH_2}$ entre P et ester (carbanion stabilisé) ; addition de type aldol sur $\mathrm{PhCH_2CH_2CHO}$,
 puis protonation ($\mathrm{H_3O^+}$). Le composé **7** est $\mathrm{Ph_2P{-}CH(CO_2Et){-}CH(OH){-}CH_2{-}CH_2{-}Ph}$, obtenu en couple d'énantiomères $(R,R)$ et $(S,S)$. *Schéma attendu : les deux énantiomères en Cram, flèches courbes partant des doublets non liants (les deux doublets de l'azote du LDA représentés).* $\square$

### Question 55

> [!INDICATION]
> Sel 8 après méthylation ; cyclisation de l'alcoolate sur $\mathrm{P^+}$ ; les oxaphosphétanes *cis* mènent au Z.

#### Solution

Après méthylation du P (MeOTf), le sel **8** est $[\mathrm{Ph_2(Me)P{-}CH(CO_2Et){-}CH(OH){-}CH_2CH_2Ph}]^+\,\mathrm{TfO^-}$. Le DBU déprotone l'OH ; l'alcoolate cyclise sur $\mathrm{P^+}$ → oxaphosphétane. L'alcène **Z** provient des oxaphosphétanes **cis** (substituants $\mathrm{CO_2Et}$ et $\mathrm{CH_2CH_2Ph}$ du même côté du cycle). *Schéma attendu : les deux oxaphosphétanes cis énantiomères, cycle P–C–C–O.* $\square$

### Question 56

> [!INDICATION]
> Dans l'ET2-trans, la conjugaison ylure–ester ($-M$) est mieux conservée → ET plus stable.

#### Solution

Le paramètre électronique est la **conjugaison du carbone ylure avec le carbonyle de l'ester** : dans l'ET2-*trans*, cette délocalisation (effet $-M$) est mieux conservée, ce qui **abaisse l'énergie** de l'état de transition menant à l'oxaphosphétane *trans*. $\square$

### Question 57

> [!INDICATION]
> Dans l'ET2-cis : interaction 1,2-éclipsée $\mathrm{R_1/R_2}$ et gêne $\mathrm{R_1}$/L, absentes du trans.

#### Solution

Dans l'ET2-*cis*, les deux substituants ($\mathrm{CO_2R}$ et $\mathrm{R_1=CH_2CH_2Ph}$) sont du **même côté** du cycle en formation : (1) interaction **1,2-éclipsée** entre $\mathrm{R_1}$ et $\mathrm{R_2}$ ; (2) gêne entre $\mathrm{R_1}$ et un **ligand L** du phosphore. Absentes de l'ET2-*trans*. $\square$

### Question 58

> [!INDICATION]
> Me plus petit que Ph → gêne $\mathrm{R_1}$/L diminuée dans l'ET2-cis → sélectivité E diminuée ; discuter.

#### Solution

Passer de $\mathrm{Ph_3P^+}$ à $\mathrm{MePh_2P^+}$ remplace un phényle par un **méthyle plus petit**, ce qui **minimise l'interaction stérique entre $\mathrm{R_1}$ et le ligand L** dans l'ET2-*cis* : cet état de transition est moins déstabilisé → davantage d'oxaphosphétane *cis* → davantage d'alcène **Z** ; la sélectivité E diminue (de $Z/E>4/96$ à $19/81$). $\square$

## IV. Utilisation des phosphines en catalyse asymétrique

### A — Synthèse du BINAP

### Question 59*

> [!INDICATION]
> L'estérification ne change pas la configuration : identifier seulement l'ordre de priorité des substituants (pas de réexposé des règles CIP).

#### Solution

L'acide L-(+)-tartrique est $(2R,3R)$ ; l'estérification $\mathrm{OH\to OBz}$ ne change ni la géométrie ni le rang de priorité (O reste prioritaire). Ordre de priorité sur chaque carbone : $\mathrm{OBz}>\mathrm{COOH}>\mathrm{C_{voisin}}>\mathrm{H}$. Les deux centres sont donc $\boxed{(2R,3R)}$. $\square$

> [!JURY]
> « il ne faut pas réexposer les règles de Cahn-Ingold-Prelog. Cependant, il faut tout de même préciser l’ordre des substituants pour justifier une configuration absolue ».

### Question 60*

> [!INDICATION]
> Loi de Biot : signification **et unités** de chaque terme.

#### Solution

**Loi de Biot** : $\alpha=[\alpha]_\lambda^T\,\ell\,c$, avec $\alpha$ = angle de rotation mesuré (°), $[\alpha]_\lambda^T$ = pouvoir rotatoire spécifique (°·cm³·g⁻¹·dm⁻¹, à la longueur d'onde $\lambda$ et à la température $T$),
 $\ell$ = longueur de la cuve (dm), $c$ = concentration massique (g·cm⁻³). $\square$

> [!JURY]
> « La loi de Biot […] est en général restituée de façon très imprécise en ce qui concerne les unités de ses termes. »

### Question 61

> [!INDICATION]
> 9 est énantiopur → les deux adduits sont des **diastéréoisomères** (solubilités différentes).

#### Solution

Le composé **9** étant **énantiopur** (L), les adduits $(R)$-BINAPO·9 et $(S)$-BINAPO·9 sont des **diastéréoisomères** : propriétés physiques différentes, notamment **solubilités distinctes** — fondement du dédoublement par cristallisation. $\square$

> [!JURY]
> « La notion de dédoublement d’énantiomères par la formation de diastéréoisomères n’est malheureusement pas toujours bien comprise ».

### Question 62

> [!INDICATION]
> Liaison faible du cristal : liaison H entre $\mathrm{COOH}$ du DBT et $\mathrm{P{=}O}$ du BINAPO.

#### Solution

Le cristal est maintenu par des **liaisons hydrogène** entre les groupes **acide carboxylique** du DBT ($\mathrm{O{-}H}$) et les oxygènes des **oxydes de phosphine** du BINAPO ($\mathrm{P{=}O}$) : $\mathrm{O{-}H\cdots O{=}P}$. $\square$

> [!JURY]
> « La notion de liaison hydrogène est mal maîtrisée : des liaisons H sont vues là où il n'y en a pas […] et pas là où il y en a ».

### Question 63

> [!INDICATION]
> La soude déprotone les deux fonctions acide du DBT → BINAPO neutre libéré, carboxylate en solution.

#### Solution

La soude déprotone les deux fonctions acide du DBT, libérant le BINAPO neutre (extrait en phase organique) et le carboxylate hydrosoluble :

$$
(S)\text{-BINAPO}\cdot\mathrm{DBT(H)_2}+2\,\mathrm{OH^-}\rightarrow(S)\text{-BINAPO}+\mathrm{DBT^{2-}}+2\,\mathrm{H_2O}.
$$
$\square$

### Question 64

> [!INDICATION]
> Le $(R)$-BINAPO non cristallisé est dans le **filtrat** ; le récupérer par traitement à la soude puis extraction.

#### Solution

Le $(R)$-BINAPO non cristallisé reste dans le **filtrat** (eaux-mères) ; on le récupère en traitant ce filtrat par la soude (comme en Q63) puis par **extraction** organique et évaporation. $\square$

> [!JURY]
> « Peu de candidats ont identifié que le (R)-BINAPO se trouvait dans le filtrat ».

### B — Effets non linéaires

### Question 65*

> [!INDICATION]
> Double addition d'un magnésien sur un ester → alcool tertiaire ; avec CuI, cuprate → addition conjuguée 1,4 (chimiosélectivité).

#### Solution

Sur l'éthanoate de méthyle, $\mathrm{EtMgBr}$ s'additionne **deux fois** (via la cétone $\mathrm{CH_3COEt}$), donnant après hydrolyse l'**alcool tertiaire** $\mathrm{CH_3{-}C(Et)_2{-}OH}$ (3-méthylpentan-3-ol). Le substrat **10** porte un ester $\alpha,\beta$-insaturé ; avec **CuI**, le magnésien forme un **cuprate** qui réalise l'**addition conjuguée 1,4** sur le C=C (Michael) au lieu d'attaquer l'ester (1,2) : le cuivre assure la **chimiosélectivité**. $\square$

> [!JURY]
> « la chimie des cuprates est ignorée de la majorité des candidats ».

### Question 66

> [!INDICATION]
> $\%R=(100+ee_{\text{prod}})/2$, $\%S=(100-ee_{\text{prod}})/2$ ; application numérique.

#### Solution

$ee=\%R-\%S$ et $\%R+\%S=100$, donc $\%R=\frac{100+ee_{\text{prod}}}{2}$ et $\%S=\frac{100-ee_{\text{prod}}}{2}$. Pour $ee=93~\%$ :

$$
\begin{aligned}
\%R\\
& =\boxed{96{,}5~\%}
\end{aligned}
$$

$$
\begin{aligned}
\%S\\
& =\boxed{3{,}5~\%}.
\end{aligned}
$$
$\square$

> [!JURY]
> « la réponse à la question 66 manque de rigueur, il était spécifiquement demandé l’expression des pourcentages en énantiomères R et S ».

### Question 67

> [!INDICATION]
> CuI:L = 1:1 → un seul ligand par métal → pas d'espèce $\mathrm{ML_2}$ → pas d'effet non linéaire → droite.

#### Solution

Avec $\mathrm{CuI:L}=1:1$, chaque métal ne porte qu'**un seul ligand** : il n'existe pas d'espèce $\mathrm{ML_2}$ susceptible de « piéger » le ligand minoritaire. Il n'y a donc **pas d'effet non linéaire** : $ee_{\text{prod}}$ est **proportionnel** à $ee_L$, et la modélisation par une **droite** (figure 15a) est justifiée. $\square$

### Question 68*

> [!INDICATION]
> Compter $\mathrm{L_R}$ et $\mathrm{L_S}$ incorporés dans $\mathrm{ML_RL_R}$, $\mathrm{ML_SL_S}$, $\mathrm{ML_RL_S}$.

#### Solution

$n(\mathrm{L_R})=2x+z$ (de $\mathrm{ML_RL_R}$ et $\mathrm{ML_RL_S}$) ; $n(\mathrm{L_S})=2y+z$. Donc

$$
\begin{aligned}
ee_L\\
& =\frac{n(\mathrm{L_R})-n(\mathrm{L_S})}{n(\mathrm{L_R})+n(\mathrm{L_S})}\\
& =\frac{2x-2y}{2(x+y+z)}\\
& =\boxed{\frac{x-y}{x+y+z}}.
\end{aligned}
$$
$\square$

### Question 69*

> [!INDICATION]
> $\mathrm{ML_RL_R}$ et $\mathrm{ML_SL_S}$ sont énantiomères → leurs constantes de vitesse sont **identiques** (pas de signe opposé).

#### Solution

$\mathrm{ML_RL_R}$ et $\mathrm{ML_SL_S}$ sont **énantiomères** : leurs constantes de vitesse sont **identiques** (et non de signe opposé) :

$$
\boxed{k_{RR}=k_{SS}.}
$$
$\square$

> [!JURY]
> « peu de candidats ont identifié que les constantes de vitesse de deux énantiomères sont identiques (question 69), et non pas de signe opposé ».

### Question 70

> [!INDICATION]
> Ordre 1 en catalyseur, 0 en substrat → vitesse constante ; répartir R/S avec $ee_{\max}$.

#### Solution

Loi de vitesse d'ordre 1 en catalyseur, 0 en substrat : $\frac{\mathrm d[11]_{RR}}{\mathrm dt}=k_{RR}\,x$ (constant), d'où $[11]_{RR}(t)=k_{RR}\,x\,t$. Ce catalyseur donne $ee_{\max}$ (R majoritaire) : $\%R=(1+ee_{\max})/2$. Donc

$$
\begin{aligned}
[11R]_{RR}\\
& =k_{RR}\,x\,t\,\frac{1+ee_{\max}}{2}
\end{aligned}
$$

$$
\begin{aligned}
[11S]_{RR}\\
& =k_{RR}\,x\,t\,\frac{1-ee_{\max}}{2}.
\end{aligned}
$$
$\square$

### Question 71

> [!INDICATION]
> Sommer les contributions $(R-S)$ et $(R+S)$ des trois catalyseurs ($k_{SS}=k_{RR}$, hétérochiral racémique).

#### Solution

Excès $(R-S)$ : de $\mathrm{ML_RL_R}$ : $+k_{RR}x\,t\,ee_{\max}$ ; de $\mathrm{ML_SL_S}$ : $-k_{RR}y\,t\,ee_{\max}$ ; de $\mathrm{ML_RL_S}$ : 0. D'où

$$
\begin{aligned}
R-S\\
& =k_{RR}\,t\,ee_{\max}(x-y)
\end{aligned}
$$

$$
\begin{aligned}
R+S\\
& =t\big[k_{RR}(x+y)+k_{RS}\,z\big],
\end{aligned}
$$

$$
\boxed{ee_{\text{prod}}=\frac{ee_{\max}(x-y)}{(x+y)+\dfrac{k_{RS}}{k_{RR}}\,z}=\frac{ee_{\max}(x-y)}{(x+y)+g\,z}.}
$$
$\square$

### Question 72

> [!INDICATION]
> Injecter $ee_L$ (Q68) et poser $\beta=z/(x+y)$ dans l'expression de Q71.

#### Solution

De Q68, $x-y=ee_L(x+y+z)$. En reportant dans Q71 et avec $\beta=z/(x+y)$ :

$$
\begin{aligned}
\frac{x+y+z}{x+y}\\
& =1+\beta
\end{aligned}
$$

$$
\begin{aligned}
\frac{(x+y)+gz}{x+y}\\
& =1+g\beta,
\end{aligned}
$$

$$
\boxed{ee_{\text{prod}}=ee_{\max}\cdot ee_L\cdot\frac{1+\beta}{1+g\beta}.}
$$
$\square$

### Question 73

> [!INDICATION]
> Avec $K=z^2/(xy)$ et $x+y=1$, obtenir une équation du second degré en $\beta$ ; prendre la racine positive.

#### Solution

Normalisons $x+y=1$ : $\beta=z$, $x-y=ee_L(1+z)$ et $xy=(1-(x-y)^2)/4$. Avec $K=z^2/(xy)$ :

$$
K=\frac{4\beta^2}{1-ee_L^2(1+\beta)^2},
$$

soit $(4+K\,ee_L^2)\beta^2+2K\,ee_L^2\beta-K(1-ee_L^2)=0$, de racine positive :

$$
\boxed{\beta=\frac{-K\,ee_L^2+\sqrt{K(4+K\,ee_L^2)-4K\,ee_L^2}}{4+K\,ee_L^2}.}
$$
$\square$

### Question 74

> [!INDICATION]
> Composer Q72 et Q73 pour exprimer $ee_{\text{prod}}$ selon $ee_L$, $ee_{\max}$, $K$, $g$.

#### Solution

En reportant $\beta$ (Q73) dans l'expression de Q72 :

$$
\begin{aligned}
ee_{\text{prod}}\\
& =ee_{\max}\,ee_L\,\frac{1+\beta}{1+g\beta}
\end{aligned}
$$

$$
\begin{aligned}
\beta\\
& =\frac{-K\,ee_L^2+\sqrt{K(4+K\,ee_L^2)-4K\,ee_L^2}}{4+K\,ee_L^2},
\end{aligned}
$$

ce qui exprime $ee_{\text{prod}}$ en fonction de $ee_L$, $ee_{\max}$, $K$ et $g$ uniquement. $\square$

### Question 75

> [!INDICATION]
> Ligand énantiopur ($ee_L=1$) → $z=0$, $\beta=0$ → $ee_{\text{prod}}=ee_{\max}$ ; lire $ee_{\max}$ sur l'entrée 3.

#### Solution

L'entrée 3 (complexe 12 + $\mathrm{L_R}$ supplémentaire) fournit un ligand **énantiopur** ($ee_L=1$) : alors $z=0$, $\beta=0$ et

$$
ee_{\text{prod}}=ee_{\max}\cdot1\cdot\frac{1+0}{1+0}=ee_{\max}.
$$

L'entrée 3 donnant $ee=93~\%$, on lit $\boxed{ee_{\max}=0{,}93}$. $\square$

### Question 76

> [!INDICATION]
> $K\gg4$ : $\mathrm{ML_RL_S}$ formé préférentiellement (réservoir du ligand minoritaire) ; $g\ll1$ : il est peu réactif → effet non linéaire positif.

#### Solution

$K=30\gg4$ (valeur statistique d'une répartition aléatoire) : le complexe **hétérochiral $\mathrm{ML_RL_S}$ est formé préférentiellement** — il **piège le ligand minoritaire** (effet « réservoir »). $g=k_{RS}/k_{RR}=0{,}15\ll1$ : ce complexe est **beaucoup moins réactif** que les homochiraux. Conjugués, ces deux effets produisent un fort **effet non linéaire positif (amplification de chiralité)** : la catalyse est portée par le complexe homochiral du ligand majoritaire, le ligand minoritaire étant séquestré dans un complexe quasi inactif. $\square$

---

## Bilan

**Méthodes à retenir.**

- **Partie I (nucléaire/RMN)** : $I
eq0$ si $A$ ou $Z$ impair ; loi d'ordre 1 de la désintégration ($t_{1/2}=\ln2/\lambda$) ; fréquence RMN proportionnelle au rapport gyromagnétique à $B_0$ fixé ; multiplicité $n+1$ ; exposant de $J$ = nombre de liaisons.
- **Partie II (chimie des solutions)** : diagrammes de prédominance sur un axe de **pH** ; tampon = réaction acide/base conjuguée ($K=1$), Henderson-Hasselbalch, puis correction par Debye-Hückel avec **tous** les ions dans $I$ ; $Q$ vs $K_s$ pour la précipitation ; n.o. par électronégativité, contre-ions exclus des édifices ioniques ; dosage colorimétrique = droite d'étalonnage sur le composé coloré.
- **Partie III (Wittig)** : ylure = mésomères $\mathrm{P^+-C^-}$ / $\mathrm{P{=}C}$ ; mécanismes en flèches courbes depuis les doublets ; époxydation *syn* par un peracide ; ouverture d'époxyde par $S_N2$ (inversion de Walden, carbone le moins encombré) ; oxaphosphétane puis cyclo-réversion [2+2] *syn* stéréospécifique ; contrôle cinétique (irréversibilité) → comparer les états de transition, et non les produits.
- **Partie IV (catalyse asymétrique)** : loi de Biot avec unités ; dédoublement par diastéréoisomères (solubilités) ; liaisons H du cristal ; cuprate = addition 1,4 (chimiosélectivité) ; $ee$, $k_{RR}=k_{SS}$, modèle $\mathrm{ML_2}$ et effet non linéaire $ee_{\text{prod}}=ee_{\max}\,ee_L\frac{1+\beta}{1+g\beta}$.

**Pièges signalés par le rapport 2026.** domaines de prédominance sur une échelle de p$K_a$ ; flèches courbes partant d'une charge ; Lewis incomplètes ; confusion activité/concentration et oubli de $C^0$ ; n.o. = nombre de liaisons ; $[\mathrm B^-]=[\mathrm H^+]$ à pH contrôlé ; $Q$ vs $K$ non calculés ; rendement non critiqué ; contre-ion dans l'édifice ; KHMDS non vu comme une base ; sel incomplet (iodure oublié) ; inversion de Walden oubliée ; réversibilité mal discutée ; loi de Biot sans unités ; liaison H fantaisiste ; cuprates ignorées ; $k$ d'énantiomères « opposées » ; 5 % des points sur la présentation.

**Pré-requis à revoir.** configurations électroniques et radioactivité ; RMN (spin, multiplicité, déplacements) ; acide phosphorique (p$K_a$, tampons, Debye-Hückel, solubilité) ; oxydo-réduction et n.o. ; mécanismes organiques et stéréochimie (Wittig, époxydation, SN2) ; loi de Biot ; énantiomérie/diastéréoisomérie ; cinétique formelle et effets non linéaires.
