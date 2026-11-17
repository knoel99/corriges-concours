# Agrégation Chimie — Problème de chimie 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 6 heures, calculatrice autorisée, sans document. Sujet « Le Phosphore » : 76 questions en quatre parties — I. l'élément phosphore et sa RMN (Q1–Q11) ; II. l'acide phosphorique et les phosphates (Q12–Q30) ; III. réaction de Wittig, ylure non stabilisé puis stabilisé (Q31–Q58) ; IV. phosphines en catalyse asymétrique, synthèse du BINAP et effets non linéaires (Q59–Q76). Les questions suivies d'une étoile (*) sont les questions fondamentales signalées par l'énoncé.

## I. L'élément phosphore et sa RMN

### Question 1*

$^{31}_{15}\mathrm{P}$ : $Z=15$ électrons, configuration électronique

$$
1s^2\,2s^2\,2p^6\,3s^2\,3p^3.
$$

Nombre de neutrons : $N=A-Z=31-15=\boxed{16}$. $\square$

### Question 2

Émission $\beta^{-}$ : un neutron se transforme en proton, $Z\to Z+1$, $A$ constant :

$$
^{32}_{15}\mathrm{P}\;\longrightarrow\;^{32}_{16}\mathrm{S}+\,^{\,0}_{-1}e+\bar\nu_e.
$$

La radioactivité $\beta^{-}$ s'accompagne d'un **changement d'élément** (P → S). $\square$

### Question 3*

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

### Question 4*

Un noyau est observable en RMN si son **spin nucléaire $I$ est non nul**. $I=0$ lorsque $A$ **et** $Z$ sont tous deux pairs. Pour $^{31}\mathrm{P}$,
 $A=31$ est impair : $I\neq0$ (ici $I=\tfrac12$), le noyau est **actif en RMN**. $\square$

### Question 5*

$^{32}\mathrm{P}$ : $A=32$ (pair), $Z=15$ (impair) : $A$ et $Z$
 ne sont pas tous deux pairs, donc $I\neq0$ — le noyau serait **observable en RMN**. $\square$

### Question 6*

En RMN $^{31}\mathrm{P}$ de $\mathrm{PH_3}$, le phosphore couple avec les 3 protons équivalents ($I=\tfrac12$) : multiplicité $n+1=4$, soit un **quadruplet** d'intensités relatives $1:3:3:1$. $\square$

### Question 7*

En RMN $^1\mathrm{H}$ de $\mathrm{PH_3}$, chaque proton couple avec un unique noyau $^{31}\mathrm{P}$ : **doublet**, intensités $1:1$. $\square$

### Question 8*

Structure de Lewis du diéthylphosphonate $\mathrm{HP(O)(OEt)_2}$ : P central, lié à H (liaison simple), à O par une double liaison $\mathrm{P{=}O}$, et à deux oxygènes $\mathrm{O{-}CH_2CH_3}$ (liaisons simples) ; chaque oxygène porte deux doublets non liants. *Schéma attendu : P au centre, une liaison P–H, une double liaison P=O, deux liaisons P–O–CH₂CH₃, tous les doublets non liants des oxygènes représentés.* P engage 5 liaisons. $\square$

### Question 9*

L'exposant des constantes de couplage indique le **nombre de liaisons** entre les deux noyaux : $^{1}J$ = couplage à travers 1 liaison (noyaux directement liés), $^{2}J$ = 2 liaisons, $^{3}J$ = 3 liaisons (couplage vicinal). $\square$

### Question 10*

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

Spectre $^{31}\mathrm{P}$ **non découplé** du proton de $\mathrm{HP(O)(OEt)_2}$ : trois types de couplages $^1\mathrm{H}$–$^{31}\mathrm{P}$.

- le H directement lié à P : $^{1}J\approx650~\mathrm{Hz}$ (1 H) → **doublet** ;
- les 4 H des deux $\mathrm{O{-}CH_2}$ (P–O–C–H, 3 liaisons) : $^{3}J\approx8~\mathrm{Hz}$ → **quintuplet** (intensités $1:4:6:4:1$) ;
- les 6 H des $\mathrm{CH_3}$ (4 liaisons) : $^{4}J<1~\mathrm{Hz}$, non observé.

Le spectre est un **doublet de quintuplets** centré sur $\delta=7{,}3~\mathrm{ppm}$ : deux massifs séparés d'environ $650~\mathrm{Hz}$, chacun éclaté en 5 raies espacées d'environ $8~\mathrm{Hz}$. *Schéma attendu : à $\delta=7{,}3~\mathrm{ppm}$, deux groupes de 5 raies $(1:4:6:4:1)$,
 séparation inter-groupes $^{1}J\simeq650~\mathrm{Hz}$, intra-groupe $^{3}J\simeq8~\mathrm{Hz}$.* $\square$

## II. L'acide phosphorique et les phosphates

### Question 12*

$$
\mathrm{Ca_{10}(PO_4)_6F_2}+10\,\mathrm{H_2SO_4}+20\,\mathrm{H_2O}\rightarrow6\,\mathrm{H_3PO_4}+10\,\mathrm{CaSO_4\cdot 2H_2O}+2\,\mathrm{HF}.
$$

Vérification : Ca $10=10$ ; P $6=6$ ; F $2=2$ ; S $10=10$ ; O $24+40+20=84=24+60$
 ; H $20+40=60=18+40+2$. Il s'agit d'une **réaction acido-basique** (déplacement des phosphates par l'acide sulfurique, plus fort), accompagnée de la **précipitation** du sulfate de calcium. $\square$

### Question 13*

Diagramme de prédominance sur un axe de **pH** (et non de p$K_a$), borné aux trois p$K_a$ :

$$
\mathrm{H_3PO_4}\;|\;2{,}12\;|\;\mathrm{H_2PO_4^-}\;|\;7{,}18\;|\;\mathrm{HPO_4^{2-}}\;|\;12{,}36\;|\;\mathrm{PO_4^{3-}}.
$$

*Schéma attendu : axe horizontal gradué en pH, les quatre espèces séparées par les trois p$K_a$.* $\square$

### Question 14*

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

### Question 15

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

### Question 16*

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

### Question 18*

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

Couple $\mathrm{NH_4^+/NH_3}$, p$K_a=9{,}25$ ; $N_{\text{tot}}=46{,}8~\mathrm{mmol\cdot L^{-1}}$. À $\mathrm{pH}=3{,}6\ll\mathrm{p}K_a$ : $[\mathrm{NH_4^+}]\approx\boxed{46{,}8~\mathrm{mmol\cdot L^{-1}}}$.
 À $\mathrm{pH}=9$ : $\frac{[\mathrm{NH_4^+}]}{[\mathrm{NH_3}]}=10^{9{,}25-9}=1{,}78$, d'où $[\mathrm{NH_4^+}]=\frac{1{,}78}{2{,}78}\times46{,}8=\boxed{30~\mathrm{mmol\cdot L^{-1}}}$. (Le pH étant contrôlé, on ne pose pas $[\mathrm B^-]=[\mathrm H^+]$.) $\square$

### Question 21*

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

### Question 22

$K_s$ (donc la solubilité) dépend de la température $T$. Fixer $T=298~\mathrm{K}$ impose un degré de sursaturation reproductible, qui contrôle les vitesses de **nucléation** et de **croissance** : on obtient des **cristaux de struvite de taille et de pureté maîtrisées**, directement réutilisables comme engrais. Une température mal contrôlée modifierait la solubilité, donc le rendement et la qualité cristalline. $\square$

### Question 23*

$M(\mathrm{MgNH_4PO_4\cdot 6H_2O})=24{,}3+14+4+31+64+108=245{,}3~\mathrm{g\cdot mol^{-1}}$. Par m³ : $n(\mathrm P)=46{,}8~\mathrm{mol}$, d'où

$$
m_{\max}=46{,}8\times245{,}3=11{,}48~\mathrm{kg\cdot m^{-3}}\approx\boxed{11{,}5~\mathrm{kg\cdot m^{-3}}}.
$$

Rendement de récupération : $\frac{11{,}40}{11{,}48}=\boxed{99~\%}$ (un rendement de 30 % ne serait pas cohérent avec un procédé industriel). $\square$

### Question 24*

$\mathrm{MoO_4^{2-}}$ : $n.o.(\mathrm{Mo})+4(-2)=-2\Rightarrow\boxed{+\mathrm{VI}}$. Dans $(\mathrm{NH_4})_6\mathrm{Mo_7O_{24}}$, les 6 $\mathrm{NH_4^+}$ sont des contre-ions ($+6$)
 : l'édifice anionique est $\mathrm{Mo_7O_{24}^{6-}}$, d'où $7\,n.o.(\mathrm{Mo})+24(-2)=-6\Rightarrow n.o.(\mathrm{Mo})=\boxed{+\mathrm{VI}}$. $\square$

### Question 25*

$\mathrm{H_3PO_4}$ : $n.o.(\mathrm{P})+3(+1)+4(-2)=0\Rightarrow\boxed{+\mathrm{V}}$. Justification par Lewis : P lié à une double liaison $\mathrm{P{=}O}$ et à trois $\mathrm{O{-}H}$ ; chaque liaison P–O est attribuée à O (plus électronégatif), P perd ses 5 électrons de valence → $+\mathrm V$. (Le n.o. n'est pas égal au nombre de liaisons.) $\square$

### Question 26

Dans $[\mathrm{H_4PMo_{12}O_{40}}]^{3-}$ : $4(+1)+(+5)+[6x+5(12-x)]+40(-2)=-3$, soit $-11+x=-3\Rightarrow x=8$. Donc **8 atomes de Mo au degré +VI** et **4 au degré +V**. $\square$

### Question 27

À faible acidité (0 et 4 mmol de $\mathrm{H^+}$), le molybdate se réduit **même sans phosphate** (figure a) : bleu parasite (faux positif). À forte acidité (16–20 mmol), le complexe ne se forme **plus**, même avec $\mathrm{PO_4^{3-}}$ (figure b). Entre 8 et 12 mmol de $\mathrm{H^+}$ : bleu intense **uniquement** en présence de phosphate et incolore sans → bon contraste et sélectivité. L'objectif est le **contraste entre les deux figures**, témoin compris. $\square$

### Question 28

Pour 105 nmol de $\mathrm{PO_4^{3-}}$, la courbe d'absorbance sature ; le témoin (0 nmol) reste faible. On retient $24{,}3~\mu\mathrm{mol}$ de molybdate d'ammonium et $5{,}68~\mu\mathrm{mol}$ d'acide ascorbique : plateau du signal utile et témoin bas, soit un **contraste maximal** pour la quantification. $\square$

### Question 29

Mesurer l'absorbance (à $820~\mathrm{nm}$) pour des quantités variables et connues de $\mathrm{PO_4^{3-}}$ établit la **droite d'étalonnage** $A=f(n_{\mathrm{PO_4^{3-}}})$ (Beer-Lambert, $R^2=0{,}9992$) : elle valide la linéarité et autorise la détermination quantitative d'une teneur inconnue en phosphate. $\square$

### Question 30

Équation a : 12 $\mathrm{MoO_4^{2-}}$ pour 1 $\mathrm{PO_4^{3-}}$ → rapport théorique **Mo/P = 12**. Réduction (Q26) : 4 Mo passent de +VI à +V (4 électrons) ; chaque acide ascorbique fournit 2 électrons → rapport théorique **ascorbique/P = 2**. Conditions optimisées (105 nmol de $\mathrm{PO_4^{3-}}$) : Mo/P $=24{,}3\times10^{-6}/105\times10^{-9}\approx2{,}3\times10^{2}$ et ascorbique/P $\approx54$ : les réactifs sont en **large excès** devant la stœchiométrie, assurant réaction totale et signal maximal. $\square$

## III. Réaction de Wittig

### A — Ylure non stabilisé

### Question 31*

Le KHMDS est une base forte qui arrache un proton en $\alpha$ du phosphore du sel de phosphonium. L'ylure **1** est $\mathrm{Ph_2(Et)P{=}CH{-}CH_3}$ (non stabilisé), de formes mésomères :

$$
\mathrm{Ph_2(Et)P^{+}{-}CH^{-}{-}CH_3}\;\longleftrightarrow\;\mathrm{Ph_2(Et)P{=}CH{-}CH_3}.
$$

Le carbanion n'est stabilisé par aucun groupe électroattracteur. *Schéma attendu : les deux formes mésomères, avec tous les doublets non liants.* $\square$

### Question 32

Isomère majoritaire **Z** du composé 2 : double liaison $\mathrm{CH{=}CH}$ portant du même côté la chaîne $\mathrm{C(CH_3)_2CH_2Ph}$ et le groupe $\mathrm{CH_3}$, et de l'autre côté les deux H vinyliques. *Schéma attendu : alcène $\mathrm{Ph{-}CH_2{-}C(CH_3)_2{-}CH{=}CH{-}CH_3}$ en configuration Z.* $\square$

### Question 33*

L'isomère **E** est thermodynamiquement **plus stable** que le Z : les deux substituants volumineux y sont en position *trans*, ce qui minimise la gêne stérique. $\square$

### Question 34

$^{3}J_{\text{cis}}=4$–$12~\mathrm{Hz}$, $^{3}J_{\text{trans}}=14$–$19~\mathrm{Hz}$. Isomère **a** : $^{3}J_{\mathrm{H-H}}=12{,}0~\mathrm{Hz}$
 → couplage **cis** → **Z**. Isomère **b** : $15{,}5~\mathrm{Hz}$ → **trans** → **E**. *Schéma attendu (forme demandée) : pour chaque isomère, les deux H vinyliques avec leurs $\delta$ ($5{,}37$ et $5{,}27~\mathrm{ppm}$ pour a ; $5{,}45$
 et $5{,}23~\mathrm{ppm}$ pour b), $^{3}J_{1\text{-}2}$ entre eux ($12{,}0$ / $15{,}5~\mathrm{Hz}$), $^{3}J$
 avec le $\mathrm{CH_3}$ ($7{,}2$ / $6{,}4~\mathrm{Hz}$) et $^{4}J$ allylique ($1{,}6~\mathrm{Hz}$).*
 $\square$

### Question 35*

On époxyde les alcènes correspondants $\mathrm{CH_3{-}CH{=}CH{-}C(CH_3)_2CH_2Ph}$ (E et Z) par un **peracide** (ex. m-CPBA). L'addition d'oxygène est **concertée et *syn*** (état de transition « papillon ») : l'alcène *trans* donne l'époxyde *trans*, le *cis* donne le *cis*. *Schéma attendu : mécanisme concerté, transfert d'un atome O du peracide vers la face de l'alcène, un seul état de transition cyclique.* $\square$

### Question 36

Ouverture de l'époxyde par $\mathrm{Ph_2P^{-}}$ sur le carbone le moins encombré, par $S_N2$ avec **inversion de Walden**. Le composé **3** est $\mathrm{Ph_2P{-}CH(CH_3){-}CH(OH){-}C(CH_3)_2{-}CH_2Ph}$. *Schéma attendu (Cram) : les deux isomères a et b, différant par la configuration relative des deux centres $\mathrm{CH(CH_3)}$ et $\mathrm{CH(OH)}$ ; l'époxyde trans conduit à a, le cis à b.* $\square$

### Question 37

$\mathrm{Ph_2PLi}$ fournit l'**anion** $\mathrm{Ph_2P^{-}}$ (contre-ion $\mathrm{Li^+}$), nucléophile mou. L'un de ses deux doublets non liants attaque le carbone **le moins encombré** de l'époxyde (le $\mathrm{CH{-}CH_3}$, pas le CH voisin du $\mathrm{C(CH_3)_2}$),
 par $S_N2$ (inversion de Walden) : ouverture du cycle en alcoolate, protonation ($\mathrm{H_3O^+}$) donnant l'alcool. La régiosélectivité vient de l'**accès stérique** au carbone attaqué. *Schéma attendu : flèche courbe partant d'un doublet non liant de $\mathrm{Ph_2P^-}$ vers le carbone, rupture de la liaison C–O, alcoolate formé ; tous les doublets non liants représentés.* $\square$

### Question 38

Le doublet non liant du phosphore de **3** attaque le carbone électrophile de l'iodoéthane $\mathrm{CH_3CH_2I}$ ($S_N2$, $\mathrm{I^-}$ partant). Le composé **4** est le sel de phosphonium **complet** :

$$
[\mathrm{Ph_2(Et)P{-}CH(CH_3){-}CH(OH){-}C(CH_3)_2CH_2Ph}]^+\,\mathrm{I^-}.
$$

*Schéma attendu (Cram) : configurations des deux centres inchangées pour a et b.* $\square$

### Question 39

NaHMDS déprotone l'hydroxyle en alcoolate : $\mathrm{P^{+}{-}CH(CH_3){-}CH(O^-){-}R}$. L'oxygène attaque le phosphore **intramoléculairement** → oxaphosphétane **5** (cycle à 4 chaînons P–C–C–O). *Schéma attendu : flèche partant du doublet de l'alcoolate vers $\mathrm{P^+}$, fermeture du cycle.* La décomposition étant *syn* (Q40), l'oxaphosphétane *cis* donne l'alcène **Z (a)** et le *trans* l'alcène **E (b)**. $\square$

### Question 40

L'oxaphosphétane se fragmente par **cyclo-réversion [2+2]** : rupture *syn* des liaisons P–C et C–O, formation de l'alcène **2** et de l'oxyde de phosphine $\mathrm{Ph_2(Et)P{=}O}$. La réaction est **stéréospécifique** (*syn*) : chaque oxaphosphétane donne un seul alcène de configuration définie. *Schéma attendu : état de transition à 4 centres, deux flèches courbes, départ de $\mathrm{Ph_2EtP{=}O}$, stéréochimie de l'oxaphosphétane apparente.* $\square$

### Question 41

D'après la courbe de Karplus, $^{3}J$ est minimal (proche de 0, ici $\approx2~\mathrm{Hz}$) lorsque l'angle dièdre est **proche de $90°$** (entre $\sim80°$ et $100°$). $\square$

### Question 42

Isomère **b** : $J_{\mathrm{P-H4}}<1~\mathrm{Hz}$ → angle dièdre $\approx90°$ → **conformation plane** (dièdre C–C–C–H $\approx95°$). Isomère **a** : $J_{\mathrm{P-H4}}=11~\mathrm{Hz}$ → angle $\approx160°$ → conformation **plissée (« papillon »)**. La conformation plane correspond à l'**isomère b = E = oxaphosphétane trans**. $\square$

### Question 43

Le **4-chlorobenzaldéhyde** est plus réactif : Cl exerce un effet inductif attracteur ($-I$) qui appauvrit le carbonyle en électrons (carbone plus électrophile). L'aldéhyde $\mathrm{Ph{-}CH_2{-}C(CH_3)_2{-}CHO}$ est aliphatique et très **encombré** par le $\mathrm{C(CH_3)_2}$ voisin. $\square$

### Question 44

Si la formation de l'oxaphosphétane était **réversible**, l'ylure régénéré réagirait avec l'aldéhyde le plus électrophile (4-chlorobenzaldéhyde) pour donner $\mathrm{p{-}ClC_6H_4{-}CH{=}CH{-}CH_3}$. Cet alcène **n'est pas formé** : la formation de l'oxaphosphétane est **irréversible**, la réaction est sous **contrôle cinétique**. $\square$

### Question 45

Les intermédiaires observés par RMN sont les **oxaphosphétanes** (5a et 5b) ; aucune bétaïne distincte n'est détectée. Le rapport cis/trans des oxaphosphétanes égale le rapport Z/E des alcènes et la décomposition est stéréospécifique : la stéréochimie est **fixée dès l'étape irréversible de formation de l'oxaphosphétane** (addition de l'ylure sur l'aldéhyde). $\square$

### Question 46

Le signal croissant à $\delta=32{,}8~\mathrm{ppm}$ correspond à l'**oxyde de phosphine** $\mathrm{Ph_2(Et)P{=}O}$ (type $\mathrm{R_3PO}$, déplacement positif), produit de la décomposition des oxaphosphétanes. $\square$

### Question 47*

La réaction étant sous **contrôle cinétique** (Q44), le rapport des produits (Z/E) est fixé par la **différence d'énergie des états de transition** menant aux oxaphosphétanes cis et trans : le plus bas en énergie donne l'alcène majoritaire. Comparer ET1-cis et ET1-trans permet donc de **prédire l'issue stéréochimique** (l'analyse des états de transition n'a de sens que sous contrôle cinétique). $\square$

### Question 48

Dans l'ET1-*trans* (conformation plutôt plane), deux interactions défavorables, absentes de l'ET1-*cis* (plissé) : (1) une interaction **1,2-éclipsée** entre $\mathrm{R_1}$ (carbone du carbonyle) et $\mathrm{R_2}$ (carbone de l'ylure) alignés dans le plan ; (2) une gêne stérique entre $\mathrm{R_1}$ et l'un des **ligands L du phosphore** (pseudo-axial). $\square$

### Question 49

D'après la figure 9 : $\mathrm{Ph_3P}$ → $Z/E=99/1$ ; $\mathrm{Ph_2EtP}$ → $5{,}7/1$ ; $\mathrm{Et_2PhP}$
 → $1{,}3/1$. **Plus le phosphore porte de groupes phényle, plus la réaction est Z-sélective.** $\square$

### Question 50

Les interactions défavorables de l'ET1-*trans* (Q48) impliquent les **ligands L** du phosphore. L = Ph (large) : gênes sévères → ET1-*trans* fortement déstabilisé → oxaphosphétane *cis* privilégié → forte sélectivité Z ($\mathrm{Ph_3P}$ : 99/1). Un Ph remplacé par Et (plus petit) : gêne diminuée → davantage d'E ($\mathrm{Ph_2EtP}$ : 5,7/1). Deux Et ($\mathrm{Et_2PhP}$) : sélectivité quasi perdue (1,3/1). Discussion cas par cas des trois ylures. $\square$

### B — Ylure stabilisé

### Question 51*

Le DBU est une amidine ; l'azote le plus basique est l'azote **sp² de l'imine** ($\mathrm{N{=}C}$) : sa protonation forme un cation **amidinium** dont la charge est **délocalisée sur les deux azotes** (mésomérie), fortement stabilisé. L'azote sp³ (amine) n'en bénéficie pas. $\square$

### Question 52

*(Coquille de l'énoncé signalée : la figure citée est la figure 10, et non la 9.)* Ylures : $\mathrm{Ph_3P{=}CH{-}CO_2Et}$ et $\mathrm{Ph_2(Me)P{=}CH{-}CO_2Et}$, de formes mésomères :

$$
\begin{aligned}
\mathrm{R_3P^{+}{-}CH^{-}{-}CO_2Et}\;\\
& \longleftrightarrow\;\mathrm{R_3P{=}CH{-}CO_2Et}\;\\
& \longleftrightarrow\;\mathrm{R_3P^{+}{-}CH{=}C(O^-){-}OEt}.
\end{aligned}
$$

Le carbanion est **conjugué au carbonyle de l'ester** (effet $-M$) : la charge négative est délocalisée sur l'oxygène → ylure **stabilisé**. *Schéma attendu : les formes mésomères en structures de Lewis complètes.* $\square$

### Question 53

Alcène majoritaire **E** du composé 6 : $\mathrm{Ph{-}CH_2{-}CH_2{-}CH{=}CH{-}CO_2Et}$, la chaîne $\mathrm{CH_2CH_2Ph}$ et le groupe $\mathrm{CO_2Et}$ en *trans*. *Schéma attendu : double liaison $\mathrm{CH{=}CH}$ en configuration E.* $\square$

### Question 54

LDA ($\mathrm{Li^+}$, $\mathrm{iPr_2N^-}$ ; acide conjugué $\mathrm{iPr_2NH}$) déprotone le $\mathrm{CH_2}$ entre P et ester (carbanion stabilisé) ; addition de type aldol sur $\mathrm{PhCH_2CH_2CHO}$,
 puis protonation ($\mathrm{H_3O^+}$). Le composé **7** est $\mathrm{Ph_2P{-}CH(CO_2Et){-}CH(OH){-}CH_2{-}CH_2{-}Ph}$, obtenu en couple d'énantiomères $(R,R)$ et $(S,S)$. *Schéma attendu : les deux énantiomères en Cram, flèches courbes partant des doublets non liants (les deux doublets de l'azote du LDA représentés).* $\square$

### Question 55

Après méthylation du P (MeOTf), le sel **8** est $[\mathrm{Ph_2(Me)P{-}CH(CO_2Et){-}CH(OH){-}CH_2CH_2Ph}]^+\,\mathrm{TfO^-}$. Le DBU déprotone l'OH ; l'alcoolate cyclise sur $\mathrm{P^+}$ → oxaphosphétane. L'alcène **Z** provient des oxaphosphétanes **cis** (substituants $\mathrm{CO_2Et}$ et $\mathrm{CH_2CH_2Ph}$ du même côté du cycle). *Schéma attendu : les deux oxaphosphétanes cis énantiomères, cycle P–C–C–O.* $\square$

### Question 56

Le paramètre électronique est la **conjugaison du carbone ylure avec le carbonyle de l'ester** : dans l'ET2-*trans*, cette délocalisation (effet $-M$) est mieux conservée, ce qui **abaisse l'énergie** de l'état de transition menant à l'oxaphosphétane *trans*. $\square$

### Question 57

Dans l'ET2-*cis*, les deux substituants ($\mathrm{CO_2R}$ et $\mathrm{R_1=CH_2CH_2Ph}$) sont du **même côté** du cycle en formation : (1) interaction **1,2-éclipsée** entre $\mathrm{R_1}$ et $\mathrm{R_2}$ ; (2) gêne entre $\mathrm{R_1}$ et un **ligand L** du phosphore. Absentes de l'ET2-*trans*. $\square$

### Question 58

Passer de $\mathrm{Ph_3P^+}$ à $\mathrm{MePh_2P^+}$ remplace un phényle par un **méthyle plus petit**, ce qui **minimise l'interaction stérique entre $\mathrm{R_1}$ et le ligand L** dans l'ET2-*cis* : cet état de transition est moins déstabilisé → davantage d'oxaphosphétane *cis* → davantage d'alcène **Z** ; la sélectivité E diminue (de $Z/E>4/96$ à $19/81$). $\square$

## IV. Utilisation des phosphines en catalyse asymétrique

### A — Synthèse du BINAP

### Question 59*

L'acide L-(+)-tartrique est $(2R,3R)$ ; l'estérification $\mathrm{OH\to OBz}$ ne change ni la géométrie ni le rang de priorité (O reste prioritaire). Ordre de priorité sur chaque carbone : $\mathrm{OBz}>\mathrm{COOH}>\mathrm{C_{voisin}}>\mathrm{H}$. Les deux centres sont donc $\boxed{(2R,3R)}$. $\square$

### Question 60*

**Loi de Biot** : $\alpha=[\alpha]_\lambda^T\,\ell\,c$, avec $\alpha$ = angle de rotation mesuré (°), $[\alpha]_\lambda^T$ = pouvoir rotatoire spécifique (°·cm³·g⁻¹·dm⁻¹, à la longueur d'onde $\lambda$ et à la température $T$),
 $\ell$ = longueur de la cuve (dm), $c$ = concentration massique (g·cm⁻³). $\square$

### Question 61

Le composé **9** étant **énantiopur** (L), les adduits $(R)$-BINAPO·9 et $(S)$-BINAPO·9 sont des **diastéréoisomères** : propriétés physiques différentes, notamment **solubilités distinctes** — fondement du dédoublement par cristallisation. $\square$

### Question 62

Le cristal est maintenu par des **liaisons hydrogène** entre les groupes **acide carboxylique** du DBT ($\mathrm{O{-}H}$) et les oxygènes des **oxydes de phosphine** du BINAPO ($\mathrm{P{=}O}$) : $\mathrm{O{-}H\cdots O{=}P}$. $\square$

### Question 63

La soude déprotone les deux fonctions acide du DBT, libérant le BINAPO neutre (extrait en phase organique) et le carboxylate hydrosoluble :

$$
(S)\text{-BINAPO}\cdot\mathrm{DBT(H)_2}+2\,\mathrm{OH^-}\rightarrow(S)\text{-BINAPO}+\mathrm{DBT^{2-}}+2\,\mathrm{H_2O}.
$$
$\square$

### Question 64

Le $(R)$-BINAPO non cristallisé reste dans le **filtrat** (eaux-mères) ; on le récupère en traitant ce filtrat par la soude (comme en Q63) puis par **extraction** organique et évaporation. $\square$

### B — Effets non linéaires

### Question 65*

Sur l'éthanoate de méthyle, $\mathrm{EtMgBr}$ s'additionne **deux fois** (via la cétone $\mathrm{CH_3COEt}$), donnant après hydrolyse l'**alcool tertiaire** $\mathrm{CH_3{-}C(Et)_2{-}OH}$ (3-méthylpentan-3-ol). Le substrat **10** porte un ester $\alpha,\beta$-insaturé ; avec **CuI**, le magnésien forme un **cuprate** qui réalise l'**addition conjuguée 1,4** sur le C=C (Michael) au lieu d'attaquer l'ester (1,2) : le cuivre assure la **chimiosélectivité**. $\square$

### Question 66

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

### Question 67

Avec $\mathrm{CuI:L}=1:1$, chaque métal ne porte qu'**un seul ligand** : il n'existe pas d'espèce $\mathrm{ML_2}$ susceptible de « piéger » le ligand minoritaire. Il n'y a donc **pas d'effet non linéaire** : $ee_{\text{prod}}$ est **proportionnel** à $ee_L$, et la modélisation par une **droite** (figure 15a) est justifiée. $\square$

### Question 68*

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

$\mathrm{ML_RL_R}$ et $\mathrm{ML_SL_S}$ sont **énantiomères** : leurs constantes de vitesse sont **identiques** (et non de signe opposé) :

$$
\boxed{k_{RR}=k_{SS}.}
$$
$\square$

### Question 70

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

L'entrée 3 (complexe 12 + $\mathrm{L_R}$ supplémentaire) fournit un ligand **énantiopur** ($ee_L=1$) : alors $z=0$, $\beta=0$ et

$$
ee_{\text{prod}}=ee_{\max}\cdot1\cdot\frac{1+0}{1+0}=ee_{\max}.
$$

L'entrée 3 donnant $ee=93~\%$, on lit $\boxed{ee_{\max}=0{,}93}$. $\square$

### Question 76

$K=30\gg4$ (valeur statistique d'une répartition aléatoire) : le complexe **hétérochiral $\mathrm{ML_RL_S}$ est formé préférentiellement** — il **piège le ligand minoritaire** (effet « réservoir »). $g=k_{RS}/k_{RR}=0{,}15\ll1$ : ce complexe est **beaucoup moins réactif** que les homochiraux. Conjugués, ces deux effets produisent un fort **effet non linéaire positif (amplification de chiralité)** : la catalyse est portée par le complexe homochiral du ligand majoritaire, le ligand minoritaire étant séquestré dans un complexe quasi inactif. $\square$
