# Agrégation Physique — Composition de chimie 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

Composition de chimie de l'agrégation externe de physique-chimie (option physique), session 2026 (EAE PHP 2) : 5 heures, calculatrice autorisée, tout ouvrage et autre matériel électronique interdits. Le sujet « Les homophones /vɛʁ/ » décline quatre parties indépendantes autour des homophones vert / vers / verre : I. Vert minéral (élément chlore, radiochimie, eau de Javel, titrages calorimétrique et colorimétrique, simulation Monte-Carlo), II. Le vert de bromocrésol (structure, spectrophotométrie, pKa, titrage pH-métrique et TAC d'une eau du robinet), III. Vers de la chimie plus verte (pyridine et bipyridine, méthode de Job, catalyse, jasmone, CO2 supercritique), IV. Verres organiques (procédé industriel du carbonate de diméthyle : bilans de matière, azéotrope, distillation). 69 questions de difficulté croissante. D'après le rapport 2026, la moyenne de l'épreuve est de 7,3/20 pour les candidats ayant composé (7,4/20 en 2025) et de 11,01/20 pour les admissibles, pour une barre d'admissibilité de 46,8/120.

> [!JURY]
> « Il est recommandé de ne pas recopier les questions de l'énoncé, mais d'y répondre, en justifiant son propos, de manière à la fois précise et concise (un unique mot clé ne peut être suffisant) » (rapport 2026, p. 16).

> [!JURY]
> « Un commentaire critique des résultats numériques est par ailleurs grandement apprécié » ; « il importe de spécifier l'état physique (liquide, solide, gazeux, en solution) des différentes espèces chimiques » (rapport 2026, p. 16).

## I. Vert minéral : à propos de l'élément chlore

#### 1. Propriétés radiochimiques

### Q1

> [!INDICATION]
> Quelle règle de remplissage jusqu'à $Z=17$ ?

#### Solution

$\text{Cl}$ : $1s^2\,2s^2\,2p^6\,3s^2\,3p^5$. $\square$

> [!JURY]
> « Les candidats sont invités à lire la question et à y répondre strictement afin de gagner du temps de composition » (rapport 2026, p. 16).

### Q2

> [!INDICATION]
> Quelles sous-couches comptent comme valence : seulement la couche de $n$ maximal, ou aussi les sous-couches en cours de remplissage ?

#### Solution

Pour $\text{Cl}$, $n_{\max}=3$ : les électrons de valence sont $3s^2\,3p^5$, soit **7 électrons de valence**.

> [!JURY]
> « ils omettent fréquemment les sous-couches en cours de remplissage dans la définition utile pour dénombrer les électrons de valence » (rapport 2026, p. 16).

### Q3

> [!INDICATION]
> Depuis la configuration : ligne, colonne, famille chimique ?

#### Solution

Dernière couche $n=3$ → **4ᵉ ligne ? non : 3ᵉ période**. Le bloc $p$ avec $3p^5$ (5 électrons $p$) place le chlore en **colonne 17**. Famille des **halogènes**.

> [!JURY]
> « la ligne étant toutefois assez souvent oubliée » ; « certains confondent les halogènes avec les alcalins » (rapport 2026, p. 16).

### Q4

> [!INDICATION]
> Définition d'isotope ; composition du noyau de $^{35}\text{Cl}$ ?

#### Solution

Deux isotopes d'un même élément ont le **même nombre de protons $Z$** mais des **nombres de neutrons différents** (donc des nombres de masse $A$ différents). $^{35}_{17}\text{Cl}$ : **17 protons et $35-17=18$ neutrons**.

### Q5

> [!INDICATION]
> Quelle grandeur tabulée relie masse molaire atomique et proportions des isotopes stables ?

#### Solution

Soit $x$ la fraction de $^{35}\text{Cl}$ : $35x + 37(1-x) = 35{,}5 \Rightarrow 37 - 2x = 35{,}5 \Rightarrow x = 0{,}75$.

$$
\boxed{75\%\ \text{de}\ ^{35}\text{Cl},\quad 25\%\ \text{de}\ ^{37}\text{Cl}.}
$$

> [!JURY]
> « La question a été mal comprise par bon nombre de candidats » (rapport 2026, p. 17).

### Q6

> [!INDICATION]
> Deux voies de désintégration du $^{36}\text{Cl}$ : nommer les émissions et écrire les équations codifiées (règles de Soddy).

#### Solution

$$
\beta^- \ (98\%)\ :\quad ^{36}_{17}\text{Cl} \longrightarrow\ ^{36}_{18}\text{Ar} + ^{\ 0}_{-1}\text{e} + \overline{\nu}_e
$$

$$
\text{capture électronique}\ (2\%)\ :\quad ^{36}_{17}\text{Cl} + ^{\ 0}_{-1}\text{e} \longrightarrow\ ^{36}_{16}\text{S} + \nu_e
$$

La désintégration **minoritaire** est la **capture électronique** : le noyau capture un **électron du cortège** et émet un **neutrino électronique**.

### Q7

> [!INDICATION]
> Définir la période radioactive $\tau$ ; intégrer la loi de vitesse d'ordre 1 pour relier $\lambda$ et $\tau$.

#### Solution

La **période radioactive** $\tau$ est la durée au bout de laquelle la moitié des noyaux initiaux se sont désintégrés. Pour une cinétique d'ordre 1, $N(t)=N_0\,e^{-\lambda t}$ ; à $t=\tau$, $N=N_0/2$ donne $e^{-\lambda\tau}=\tfrac12$, soit

$$
\lambda = \frac{\ln 2}{\tau}.
$$

Avec $\tau_{36}=3{,}02\cdot10^{5}\ \text{ans} = 3{,}02\cdot10^{5}\times 3{,}156\cdot10^{7}\ \text{s} = 9{,}53\cdot10^{12}\ \text{s}$ :

$$
\lambda = \frac{0{,}693}{9{,}53\cdot10^{12}} = \boxed{7{,}3\cdot10^{-14}\ \text{s}^{-1}.}
$$

#### 2. L'eau de Javel

##### a. Propriétés chimiques

### Q8

> [!INDICATION]
> Sur le diagramme E-pH, quelle espèce du couple est oxydante ? Une espèce n'est oxydante que relativement à un couple.

#### Solution

Une espèce n'est pas « oxydante » en soi : $\text{ClO}^-$ est l'**oxydant du couple $\text{ClO}^-/\text{Cl}^-$**. Sur le diagramme (figure 1a), $\text{ClO}^-$ occupe le domaine de **haut potentiel** (au-dessus de $\text{Cl}^-$), et ce domaine est situé **au-dessus de la frontière $\text{O}_2/\text{H}_2\text{O}$** ($E°=1{,}23$ V).
$\text{ClO}^-$ est donc un oxydant fort, capable d'oxyder l'eau : ses propriétés oxydantes sont ainsi justifiées.

> [!JURY]
> « une espèce chimique n'est intrinsèquement ni oxydante ni réductrice ; en revanche, on parle de l'espèce oxydante ou réductrice d'un couple oxydant / réducteur » (rapport 2026, p. 17).

### Q9

> [!INDICATION]
> Équation de la médiamutation en milieu acide (ions oxonium, pas hydroxyde) ; toxicité du dichlore formé.

#### Solution

Les degrés du chlore : $+\mathrm{I}$ dans $\text{ClO}^-$, $-\mathrm{I}$ dans $\text{Cl}^-$, $0$ dans $\text{Cl}_2$. La réunion de
$+\mathrm{I}$ et $-\mathrm{I}$ en $0$ est une **médiamutation** :

$$
\text{Cl}^-(aq) + \text{ClO}^-(aq) + 2\,\text{H}^+(aq) \longrightarrow \text{Cl}_2(g) + \text{H}_2\text{O}(\ell)
$$

Transformation d'**oxydoréduction**. Le $\text{Cl}_2$ produit est un **gaz toxique** : il ne faut jamais mélanger l'eau de Javel à un acide fort.

> [!JURY]
> « faire apparaître soit les ions oxonium (en milieu acide) soit les ions hydroxyde (en milieu basique), mais pas les deux simultanément » (rapport 2026, p. 17).

### Q10

> [!INDICATION]
> Depuis la masse molaire de $\text{Cl}_2$ et l'approximation $\rho\approx\rho_{\text{eau}}$, retrouver $C=0{,}52\ \text{mol}\cdot\text{L}^{-1}$ en explicitant les hypothèses.

#### Solution

$100$ g de solution produisent, par décomposition **totale**, $3{,}7$ g de $\text{Cl}_2$. D'après Q9, $1$ mol de $\text{ClO}^-$ donne $1$ mol de
$\text{Cl}_2$. Avec $M(\text{Cl}_2)=71\ \text{g}\cdot\text{mol}^{-1}$ :

$$
\begin{aligned}
n(\text{ClO}^-) &= n(\text{Cl}_2) \\
&= \frac{3{,}7}{71} \\
&= 5{,}2\cdot10^{-2}\ \text{mol dans 100 g}.
\end{aligned}
$$

En supposant $\rho_{\text{solution}}\approx\rho_{\text{eau}}=1{,}00\ \text{kg}\cdot\text{L}^{-1}$, $100$ g $=0{,}100$ L :

$$
C_{\text{Javel}} = \frac{5{,}2\cdot10^{-2}}{0{,}100} = \boxed{0{,}52\ \text{mol}\cdot\text{L}^{-1}.}\ \checkmark
$$

> [!JURY]
> « en explicitant les hypothèses requises, (ici de transformation totale et approximation de la masse volumique de la solution à celle de l'eau) même si elles sont données dans l'énoncé » (rapport 2026, p. 17).

### Q11

> [!INDICATION]
> Formule de Nernst complète (avec grandeurs standard) pour chaque couple de l'eau ; gaz à 1 bar.

#### Solution

$\text{O}_2(g)/\text{H}_2\text{O}(\ell)$ : $\text{O}_2 + 4\text{H}^+ + 4e^- = 2\text{H}_2\text{O}$,

$$
E = 1{,}23 + \frac{0{,}06}{4}\log\big([\text{H}^+]^4 P_{\text{O}_2}\big) = 1{,}23 - 0{,}06\,\text{pH}.
$$

$\text{H}^+/\text{H}_2(g)$ : $2\text{H}^+ + 2e^- = \text{H}_2$,

$$
E = 0 + \frac{0{,}06}{2}\log\frac{[\text{H}^+]^2}{P_{\text{H}_2}} = -0{,}06\,\text{pH}.
$$

> [!JURY]
> « Nombre de candidats manquent de rigueur dans l'écriture de la formule de Nernst en omettant les grandeurs standards » (rapport 2026, p. 17).

### Q12

> [!INDICATION]
> Domaines de prédominance disjoints de l'eau et de $\text{ClO}^-$ : pourquoi faut-il doser l'eau de Javel ?

#### Solution

Le domaine de prédominance de $\text{ClO}^-$ (au-dessus de la droite $\text{O}_2/\text{H}_2\text{O}$) est **disjoint** de celui de l'eau : $\text{ClO}^-$ est thermodynamiquement **instable** en solution (il oxyde lentement l'eau). Sa concentration **diminue dans le temps** ; il faut donc **doser** la solution pour connaître la concentration réelle $C_0$.

### Q13

> [!INDICATION]
> Définitions précises de « direct » (réaction support du titrage) et « indirect » (réaction préalable avec réactif en excès, puis titrage).

#### Solution

Dans un **titrage direct**, l'espèce dosée réagit directement avec le réactif titrant (une seule réaction support, quasi-totale). Dans un **titrage indirect**, l'espèce à doser réagit d'abord **quasi-totalement** avec un réactif ajouté en **excès** ; on titre ensuite l'un des produits formés, en quantité reliée à celle de l'espèce recherchée.

> [!JURY]
> « le titrage indirect ne semble pas maîtrisé ; la notion de transformation quasi-totale pour la première étape ou de réactif en excès n'apparaissant pas systématiquement » (rapport 2026, p. 17).

##### b. Titrage direct calorimétrique

### Q14

> [!INDICATION]
> Méthode des mélanges (hypothèse d'adiabaticité) ou chauffage par résistance ; bilan $\Delta H = 0$ incluant $C_{\text{réacteur}}$.

#### Solution

On introduit une masse $m_1$ d'eau à $T_1$ (équilibre avec le calorimètre), puis une masse $m_2$ d'eau chaude à $T_2$ ; on mesure $T_f$. Grandeurs mesurées : $m_1,m_2,T_1,T_2,T_f$. Système adiabatique et monobare :
$\Delta H = 0$, soit

$$
\big(m_1 C_p + C_{\text{réacteur}}\big)(T_f - T_1) + m_2 C_p (T_f - T_2) = 0,
$$

$$
\boxed{C_{\text{réacteur}} = \frac{m_2 C_p (T_2 - T_f)}{T_f - T_1} - m_1 C_p.}
$$

> [!JURY]
> « certains candidats passent sous silence l'hypothèse d'adiabaticité en l'utilisant néanmoins convenablement dans le bilan thermodynamique » ; « Le jury constate de nombreuses erreurs de signe » (rapport 2026, p. 17).

### Q15

> [!INDICATION]
> Nombres d'oxydation (chiffres romains) de l'iode dans $\text{IO}_3^-$ et $\text{I}^-$ ; potentiel standard par la méthode du barycentre.

#### Solution

$\text{O}$ au n.o. $-\mathrm{II}$ : dans $\text{IO}_3^-$, $n.o.(\text{I}) + 3(-\mathrm{II}) = -\mathrm{I} \Rightarrow \boxed{+\mathrm{V}}$ ; dans $\text{I}^-$, $\boxed{-\mathrm{I}}$.
Combinaison, par barycentre des $\Delta_r G°$ (6 électrons) :

$$
\begin{aligned}
6\,E°(\text{IO}_3^-/\text{I}^-) \\
&= 5\,E°(\text{IO}_3^-/\text{I}_2) + 1\,E°(\text{I}_2/\text{I}^-) \\
&= 5(1{,}18) + 0{,}62 \\
&= 6{,}52,
\end{aligned}
$$

$$
\boxed{E°(\text{IO}_3^-/\text{I}^-) = 1{,}09\ \text{V}.}
$$

> [!JURY]
> « le nombre d'oxydation de l'ion iodate » n'a pas de sens, contrairement à la locution « le nombre d'oxydation de l'élément iode dans l'ion iodate » (rapport 2026, p. 17).

### Q16

> [!INDICATION]
> Équation R1 en milieu basique (ions hydroxyde) : $3\,\text{ClO}^- + \text{I}^-$ ; relier la constante d'équilibre aux $E^\circ$.

#### Solution

Avec $\text{ClO}^-$ en excès, $\text{I}^-$ ($-\mathrm{I}$) est oxydé jusqu'à $\text{IO}_3^-$ ($+\mathrm{V}$) :

$$
\boxed{3\,\text{ClO}^-(aq) + \text{I}^-(aq) = 3\,\text{Cl}^-(aq) + \text{IO}_3^-(aq)} \qquad (R_1)
$$

(Vérification : $6$ électrons échangés, O et charges équilibrés sans eau.) Couples $\text{ClO}^-/\text{Cl}^-$ ($E°=1{,}72$) et $\text{IO}_3^-/\text{I}^-$ ($E°=1{,}09$), $n=6$ :

$$
\begin{aligned}
\log K_1° \\
&= \frac{6\,(1{,}72 - 1{,}09)}{0{,}06} \\
&= 63 \ \\
&\Rightarrow \ \boxed{K_1° = 10^{63}.}
\end{aligned}
$$

$K_1°$ colossale : la réaction est quantitative, ce qui valide son usage comme support de titrage.

### Q17

> [!INDICATION]
> Interpréter la courbe $\theta=f(V)$ : montée (réaction exothermique) puis décroissance (dilution, pertes) ; volume équivalent au maximum.

#### Solution

$R_1$ est **exothermique** : tant que $\text{I}^-$ est le réactif limitant (avant l'équivalence), chaque ajout libère de la chaleur et $\theta$ **croît** linéairement. Au-delà de l'équivalence, $\text{ClO}^-$ est épuisé : l'ajout de solution titrante froide ne provoque plus de réaction mais **dilue et refroidit** le milieu (et compense difficilement les pertes thermiques), d'où la **décroissance**. Le maximum, à l'**intersection des deux droites**, correspond donc au volume équivalent.

### Q18

> [!INDICATION]
> « la relation « $C_1\times V_1 = C_2\times V_2$ » ne peut être valable que dans le cas particulier d'une stœchiométrie 1 :1 »

#### Solution

À l'équivalence, $n(\text{ClO}^-) = 3\,n(\text{I}^-)_{\text{éq}}$, avec $n(\text{I}^-)_{\text{éq}} = c_{\text{titrant}} V_1 = 1{,}00\times 8{,}5\cdot10^{-3} = 8{,}5\cdot10^{-3}$ mol :

$$
n(\text{ClO}^-) = 2{,}55\cdot10^{-2}\ \text{mol dans 50 mL de Javel},
$$

$$
C_0 = \frac{2{,}55\cdot10^{-2}}{50\cdot10^{-3}} = \boxed{0{,}51\ \text{mol}\cdot\text{L}^{-1}.}
$$

> [!JURY]
> « la relation « $C_1\times V_1 = C_2\times V_2$ » ne peut être valable que dans le cas particulier d'une stœchiométrie 1 :1 » (rapport 2026, p. 18).

### Q19

> [!INDICATION]
> $Q=-\xi\,\Delta_r H^\circ$ ; préciser les hypothèses monobare et monotherme.

#### Solution

L'avancement vaut $\xi = c_{\text{titrant}} V$. L'énergie thermique libérée (monobare) est l'opposé de la variation d'enthalpie de réaction :

$$
\boxed{Q(V) = -\,\xi\,\Delta_r H°_{R_1} = -\,c_{\text{titrant}}\,V\,\Delta_r H°_{R_1}\ (>0).}
$$

### Q20

> [!INDICATION]
> Bilan enthalpique sur tout le contenu du calorimètre, capacité thermique $C_{\text{réacteur}}$ incluse ; hypothèses adiabatique et monobare.

#### Solution

$\Delta H = \xi\,\Delta_r H°_{R_1} + C_{\text{tot}}(\theta-\theta_0) = 0$, avec $C_{\text{tot}} = C_{\text{réacteur}} + m C_p°$. La solution initiale (50 mL Javel + 50 mL eau $\approx 100$ g) donne $C_{\text{tot}} = 132 + 100\times 4{,}18 = 550\ \text{J}\cdot\text{K}^{-1}$. D'où

$$
\boxed{\theta(V) = \theta_0 - \frac{c_{\text{titrant}}\,\Delta_r H°_{R_1}}{C_{\text{tot}}}\,V,}
$$

affine en $V$, de pente positive ($\Delta_r H°<0$), cohérente avec la relation 1.

> [!JURY]
> « La capacité thermique du calorimètre est très souvent oubliée alors que sa détermination faisait l'objet d'une question et que sa valeur est indiquée dans l'énoncé » (rapport 2026, p. 18).

### Q21

> [!INDICATION]
> Exploiter la pente de la partie linéaire avant l'équivalence (pertes thermiques, calorimètre non parfaitement calorifugé).

#### Solution

Pente $=0{,}5933\ °\text{C}\cdot\text{mL}^{-1} = 593{,}3\ \text{K}\cdot\text{L}^{-1}$ :

$$
\begin{aligned}
593{,}3 \\
&= -\frac{1{,}00\times \Delta_r H°_{R_1}}{550} \ \\
&\Rightarrow \ (\Delta_r H°_{R_1})_{\exp} \\
&= -593{,}3\times 550 \\
&= \boxed{-3{,}3\cdot10^{2}\ \text{kJ}\cdot\text{mol}^{-1}.}
\end{aligned}
$$

### Q22

> [!INDICATION]
> $\Delta_r H^\circ$ tables depuis les $\Delta_f H^\circ$ ; cohérence avec l'équation de Q16 ; commenter le signe.

#### Solution

$$
(\Delta_r H°_{R_1})_{\text{tables}} = 3\Delta_f H°(\text{Cl}^-) + \Delta_f H°(\text{IO}_3^-) - 3\Delta_f H°(\text{ClO}^-) - \Delta_f H°(\text{I}^-)
$$

$$
= 3(-167{,}2) + (-221{,}3) - 3(-107{,}1) - (-55{,}2) = \boxed{-346{,}4\ \text{kJ}\cdot\text{mol}^{-1}.}
$$

> [!JURY]
> « le jury félicite les candidats exerçant un esprit critique sur leurs résultats » (rapport 2026, p. 18).

### Q23

> [!INDICATION]
> Comparer valeur expérimentale et valeur tabulée : pertes thermiques, calorimètre imparfaitement calorifugé.

#### Solution

$|{-326}| < |{-346{,}4}|$ : la valeur expérimentale **sous-estime** (en module) la chaleur dégagée. Le calorimètre n'étant pas parfaitement calorifugé, une partie de la chaleur est **perdue vers l'extérieur** : l'élévation de température mesurée, et donc $|\Delta_r H°_{\exp}|$, sont plus faibles que prévu.

##### c. Titrage indirect colorimétrique

### Q24

> [!INDICATION]
> Sources d'incertitude sur $V_{\text{eq}}$ seulement : repérage visuel de l'équivalence, précision de la burette.

#### Solution

(i) **Repérage visuel** de l'équivalence (appréciation du changement de teinte, volume d'une goutte) ; (ii) **lecture de la burette** (incertitude liée aux graduations).

### Q25

> [!INDICATION]
> Verrerie jaugée pour l'espèce titrée, éprouvette graduée acceptée pour l'espèce en excès ; jamais de bécher pour un volume.

#### Solution

- 10 mL d'eau de Javel diluée (espèce **dosée**, quantité déterminante) → **pipette jaugée** de 10 mL.
- 15 mL de KI (iode **en large excès**, non titré) → **éprouvette graduée** (précision inutile).
- 15 gouttes d'acide éthanoïque (fixe le pH, sans enjeu quantitatif) → **compte-gouttes**.

> [!JURY]
> « un bécher n'est jamais utilisé pour évaluer un volume, même si celui-ci n'a pas besoin d'être mesuré avec précision » (rapport 2026, p. 18).

### Q26

> [!INDICATION]
> À pH 4 : éviter la formation de $\text{Cl}_2$ ET la dismutation de $\text{I}_2$ (les deux conditions).

#### Solution

À pH $\approx 4$ : (i) on évite le domaine du $\text{Cl}_2$, qui n'apparaît qu'à pH plus acide (pas de dégagement de dichlore toxique) ; (ii) on reste dans le **domaine de stabilité du $\text{I}_2$**, qui **dismute** en $\text{I}^-/\text{IO}_3^-$ en milieu plus basique. Ce pH permet donc la formation et la conservation du diiode à doser.

> [!JURY]
> « De nombreux candidats ont précisé l'intérêt de se placer à pH = 4 pour soit, éviter la formation de dichlore, soit la dismutation du diiode, mais rarement les deux » (rapport 2026, p. 19).

### Q27

> [!INDICATION]
> Deux transformations quasi-totales ; relation à l'équivalence ; la question demande des prises d'initiative.

#### Solution

*Étape 2* ($\text{I}^-$ en large excès, à pH 4) :

$$
\text{ClO}^-(aq) + 2\,\text{I}^-(aq) + 2\,\text{H}^+(aq) \longrightarrow \text{Cl}^-(aq) + \text{I}_2(aq) + \text{H}_2\text{O}(\ell)\quad(\text{quasi-totale})
$$

*Étape 3* (dosage du diiode) :

$$
\text{I}_2(aq) + 2\,\text{S}_2\text{O}_3^{2-}(aq) \longrightarrow 2\,\text{I}^-(aq) + \text{S}_4\text{O}_6^{2-}(aq)
$$

À l'équivalence : $n(\text{S}_2\text{O}_3^{2-}) = 2\,n(\text{I}_2)$ et $n(\text{I}_2) = n(\text{ClO}^-)_{\text{prise}}$. Avec $V_0=10$ mL de prise d'essai et une dilution $15\to200$ mL :

$$
C_0 = \frac{C_{\text{Thio}}\,V_{eq}}{2\,V_0}\times\frac{200}{15}.
$$

A.N. : $C_0 = \dfrac{0{,}0500\times 15{,}50\cdot10^{-3}}{2\times 10\cdot10^{-3}}\times\dfrac{200}{15} = 0{,}03875\times 13{,}33 = \boxed{0{,}517\ \text{mol}\cdot\text{L}^{-1}.}$

### Q28

> [!INDICATION]
> Loi normale ou uniforme selon la donnée (incertitude-type ou tolérance) ; compléter les lignes 15, 17, 19 du programme.

#### Solution

```python
V0_sim  = V0  + rd.uniform(-p_V0, p_V0, N)   # tolérance pipette -> rectangulaire
C_sim   = C   + rd.normal(0, u_C, N)         # incertitude-type -> normale
Veq_sim = Veq + rd.normal(0, u_Veq, N)       # incertitude-type -> normale
```

> [!JURY]
> « De nombreux candidats font la distinction entre une répartition normale et rectangulaire, selon la donnée expérimentale de l'incertitude type ou de la tolérance » (rapport 2026, p. 19).

### Q29

> [!INDICATION]
> Ligne 21 : expression de $C_0$ à partir des grandeurs simulées (reprendre Q27).

#### Solution

```python
C0 = C_sim * Veq_sim / (2 * V0_sim) * (200/15)
```

### Q30

> [!INDICATION]
> Écrire le résultat avec 1 ou 2 chiffres significatifs sur l'incertitude-type.

#### Solution

$u(C_0)=0{,}0062 \to 0{,}006$, d'où

$$
\boxed{C_0 = (0{,}517 \pm 0{,}006)\ \text{mol}\cdot\text{L}^{-1}.}
$$

> [!JURY]
> « Le résultat doit être écrit de façon cohérente, avec un ou deux chiffres significatifs sur l'incertitude type » (rapport 2026, p. 19).

## II. Le vert de bromocrésol

#### 1. Structure chimique

### Q31

> [!INDICATION]
> Stabilité de la base conjuguée : effet inducteur donneur du méthyle ; expliciter les formes limites de résonance.

#### Solution

L'acidité augmente quand la base conjuguée est plus stable. Dans le *p*-crésolate, le groupe **méthyle**, donneur par effet **inducteur (+I)**, **déstabilise** la charge négative portée par l'oxygène par rapport au phénolate : la base conjuguée du *p*-crésol est moins stable, le *p*-crésol est donc moins acide et $pK_a(p\text{-crésol}) = 10{,}3 > pK_a(\text{phénol}) = 10{,}0$.

### Q32

> [!INDICATION]
> Équilibre de tautomérie (flèches courbes) — à ne pas confondre avec des formes limites de résonance.

#### Solution

La liaison $\text{C}-\text{O}$ de la sulfolactone se rompt : le doublet de la liaison $\text{C}-\text{O}$ bascule vers l'oxygène du sulfonate (formation de $\text{R}'-\text{SO}_3\text{H}$ après captation d'un proton), tandis que le carbone central devient $sp^2$ et engage une double liaison avec le cycle (structure **quinoïde**). C'est un **équilibre de tautomérie** (migration de proton et de doubles liaisons), à distinguer d'une simple écriture de formes mésomères.

Schéma attendu : sultone fermée → flèches courbes (rupture C–O, formation C=C quinoïde et –SO₃H) → forme ouverte acide sulfonique..

### Q33

> [!INDICATION]
> Formes mono- et dianioniques du VBC (acide sulfonique fort, phénol).

#### Solution

La forme **acide ionique jaune** est **mono-anionique** : le sulfonate est totalement déprotoné ($-\text{SO}_3^-$), tandis qu'un $-\text{OH}$ phénolique reste protoné. L'équilibre acido-basique entre formes jaune et bleue est la déprotonation de ce phénol :

$$
\begin{aligned}
\underbrace{\text{VBC}^-}_{\text{jaune}} \\
&= \underbrace{\text{VBC}^{2-}}_{\text{bleue}} + \text{H}^+,\qquad pK_a \\
&= 4{,}81.
\end{aligned}
$$

#### 2. Détermination du pK_a

### Q34

> [!INDICATION]
> Identifier les courbes via les $\lambda_{\max}$ et le cercle chromatique ; caractériser le point d'intersection (isobestique, pas une zone de virage).

#### Solution

La forme **acide jaune** absorbe dans le bleu (max vers $\lambda_{\text{travail,2}}\approx 440$ nm) : c'est la **courbe 1**. La forme **basique bleue** absorbe dans l'orangé-rouge (max vers $\lambda_{\text{travail}}\approx 615$ nm) : **courbe 2**. Le point d'intersection est le **point isobestique** : à cette longueur d'onde $\varepsilon_{\text{acide}}=\varepsilon_{\text{base}}$, l'absorbance est **indépendante** de la répartition acide/base (à concentration totale fixée).

### Q35

> [!INDICATION]
> Définir l'absorbance ; Beer-Lambert (additivité, $\varepsilon(\lambda)$, concentrations) ; cadre d'application (dilution, régime linéaire du spectrophotomètre).

#### Solution

$A(\lambda) = \log\dfrac{I_0}{I} \ge 0$. Loi de Beer-Lambert : pour une espèce, $A=\varepsilon(\lambda)\,\ell\,c$. *Validité* : lumière monochromatique, milieu homogène non diffusant, pas de réaction ni de fluorescence, et **absorbance mesurée dans le domaine linéaire** du spectrophotomètre (typiquement $A\lesssim 1$–2, d'où des solutions diluées). Pour le VBC (mélange des deux formes), loi **additive** :

$$
A(\lambda) = \ell\big[\varepsilon_{\text{acide}}(\lambda)\,[\text{VBC}^-] + \varepsilon_{\text{base}}(\lambda)\,[\text{VBC}^{2-}]\big].
$$

> [!JURY]
> « Le critère sur la dilution est principalement lié à la valeur d'absorbance pouvant être mesurée en régime linéaire par le spectrophotomètre utilisé » (rapport 2026, p. 19).

### Q36

> [!INDICATION]
> Pourquoi choisir $\lambda_{\text{travail},2}$ : l'autre espèce n'y absorbe pas.

#### Solution

À $\lambda_{\text{travail}}\approx 615$ nm, la forme **acide n'absorbe pas** ($\varepsilon_{\text{acide}}\approx 0$) : l'absorbance ne reflète alors que la forme basique, ce qui simplifie l'exploitation (proportionnalité directe à $[\text{VBC}^{2-}]$). À $\lambda_{\text{travail,2}}$, les deux formes absorbent.

### Q37

> [!INDICATION]
> Lire $pK_a$ où $A = A_{\max}/2$ (ne pas confondre la courbe avec un titrage) ; diagramme de prédominance.

#### Solution

Le plateau vaut $A_{\max}\approx 0{,}970$ ; à mi-hauteur $A\approx 0{,}485$, les deux formes sont en quantités égales donc $\text{pH}=pK_a$. D'après le tableau 1, $A=0{,}485$ est atteint pour $\text{pH}\approx 4{,}8$ (entre 4,6 et 5,0). D'où $\boxed{pK_a \approx 4{,}8}$.
Diagramme : $\text{VBC}^-$ (jaune) prédomine pour $\text{pH}<4{,}8$, $\text{VBC}^{2-}$ (bleue) pour $\text{pH}>4{,}8$.

### Q38

> [!INDICATION]
> Démontrer $\log\frac{A-A_{\text{acide}}}{A_{\text{base}}-A} = \text{pH} - pK_a$ par conservation de la matière et additivité.

#### Solution

Avec $c=[\text{VBC}^-]+[\text{VBC}^{2-}]$, $A_{\text{acide}}=\varepsilon_a\ell c$, $A_{\text{base}}=\varepsilon_b\ell c$ :

$$
\begin{aligned}
A - A_{\text{acide}} \\
&= \ell[\text{VBC}^{2-}](\varepsilon_b-\varepsilon_a),\qquad A_{\text{base}} - A \\
&= \ell[\text{VBC}^-](\varepsilon_b-\varepsilon_a).
\end{aligned}
$$

Le rapport élimine $\ell(\varepsilon_b-\varepsilon_a)$ :

$$
\frac{A-A_{\text{acide}}}{A_{\text{base}}-A} = \frac{[\text{VBC}^{2-}]}{[\text{VBC}^-]} = \frac{K_a}{[\text{H}^+]}.
$$

En prenant le logarithme : $\log\dfrac{A-A_{\text{acide}}}{A_{\text{base}}-A} = \log K_a - \log[\text{H}^+] = \text{pH} - pK_a.\ \square$

> [!JURY]
> « Une démarche rigoureuse, utilisant la conservation de la matière du vert de bromocrésol et la définition exacte des différentes absorbances est attendue » (rapport 2026, p. 19).

### Q39

> [!INDICATION]
> Exprimer $A$ en fonction de $A_{\text{acide}}$, $A_{\text{base}}$, $K_a$ et $10^{-\text{pH}}$ (et non $10^{\text{pH}}$) ; ajustement numérique.

#### Solution

$A = A_{\text{acide}}\dfrac{[\text{H}^+]}{[\text{H}^+]+K_a} + A_{\text{base}}\dfrac{K_a}{[\text{H}^+]+K_a}$, soit avec $[\text{H}^+]=10^{-\text{pH}}$ :

$$
\boxed{A(\lambda_{\text{travail}}) = \frac{A_{\text{acide}}\,10^{-\text{pH}} + A_{\text{base}}\,K_a}{10^{-\text{pH}} + K_a}.}
$$

> [!JURY]
> « il est demandé d'exprimer l'absorbance en fonction de $10^{-\\text{pH}}$ et non $10^{\\text{pH}}$ » (rapport 2026, p. 19).

### Q40

> [!INDICATION]
> Comparer les deux modélisations numériques (Q38 et Q39), pas une méthode graphique et une numérique.

#### Solution

L'approche **linéarisée** (Q38) exige la mesure préalable de $A_{\text{acide}}$ et $A_{\text{base}}$ (solutions aux pH extrêmes) ; la régression $\text{pH}=f(\log\text{rapport})$ est simple mais **très sensible** aux points proches des extrêmes (le rapport diverge quand $A\to A_{\text{acide}}$ ou $A\to A_{\text{base}}$). L'**ajustement non linéaire** (Q39) exploite directement les 16 points et ajuste simultanément $A_{\text{acide}},A_{\text{base}},pK_a$ : plus robuste, il ne nécessite pas de mesures séparées aux extrêmes, au prix d'un outil de régression non linéaire.

#### 3. Détermination du TAC

### Q41

> [!INDICATION]
> Diagramme de prédominance avec les DEUX couples de $\text{HCO}_3^-$ ; espèce amphotère prédominante à pH 7,2.

#### Solution

$\text{HCO}_3^-$ appartient aux couples $\text{CO}_2/\text{HCO}_3^-$ ($pK_{a1}=6{,}3$) et $\text{HCO}_3^-/\text{CO}_3^{2-}$ ($pK_{a2}=10{,}3$). À $\text{pH}=7{,}2$,
$pK_{a1} < \text{pH} < pK_{a2}$ : $\text{HCO}_3^-$ **prédomine**. C'est une espèce **amphotère** (à la fois acide et base).

### Q42

> [!INDICATION]
> Un pH-mètre mesure une différence de potentiel entre électrode de verre et électrode de référence (souvent combinée).

#### Solution

Le pH-mètre mesure une **différence de potentiel** : il faut une **électrode de verre** associée à une **électrode de référence** (souvent réunies en une **électrode combinée**) — le capteur correspondant parmi les photographies. La chaîne **doit être étalonnée** au préalable à l'aide de **solutions tampons** (au moins deux, encadrant le pH étudié, p. ex. 4 et 7).

### Q43

> [!INDICATION]
> Deux méthodes d'exploitation : tangentes/dérivée ou saut de pH ; un bref schéma est attendu.

#### Solution

(i) **Méthode des tangentes** (deux tangentes parallèles de part et d'autre du saut) ; (ii) **méthode de la dérivée** ($\mathrm dp\text{H}/\mathrm dV$, extremum au volume équivalent). Un schéma annoté illustre la construction.

### Q44

> [!INDICATION]
> Écrire l'équation $\text{HCO}_3^- + \text{H}^+$ avant la relation à l'équivalence ; unités (mol/L, mg/L, degré français).

#### Solution

$\text{HCO}_3^-(aq) + \text{H}_3\text{O}^+(aq) \to \text{CO}_2(aq) + 2\,\text{H}_2\text{O}(\ell)$. À l'équivalence :

$$
\begin{aligned}
n(\text{HCO}_3^-) &= C_{\text{oxonium}} V_{\text{eq}} \\
&= 2{,}0\cdot10^{-2}\times 9{,}3\cdot10^{-3} \\
&= 1{,}86\cdot10^{-4}\ \text{mol},
\end{aligned}
$$

$$
[\text{HCO}_3^-] = \frac{1{,}86\cdot10^{-4}}{50\cdot10^{-3}} = 3{,}7\cdot10^{-3}\ \text{mol}\cdot\text{L}^{-1}.
$$

Avec $M(\text{HCO}_3^-)=61\ \text{g}\cdot\text{mol}^{-1}$ : $[\text{HCO}_3^-] = 3{,}7\cdot10^{-3}\times 61 = 227\ \text{mg}\cdot\text{L}^{-1}$.

$$
\text{TAC} = \frac{227}{12{,}2} = \boxed{18{,}6\ °\text{fH}.}
$$

> [!JURY]
> « Les candidats doivent faire preuve de rigueur dans l'exploitation d'un titrage en écrivant l'équation de la réaction avant de donner la relation vérifiée à l'équivalence » (rapport 2026, p. 20).

## III. Vers de la chimie plus verte

#### 1. Structures tridimensionnelles

### Q45

> [!INDICATION]
> Structure de Lewis de la pyridine (octet respecté, doublet non liant de N dans le plan).

#### Solution

Schéma attendu : cycle hexagonal, 5 C portant chacun 1 H, un N avec un doublet non liant dans le plan du cycle, trois doubles liaisons alternées..

Chaque atome de carbone porte 1 H, l'azote porte un **doublet non liant**.

### Q46

> [!INDICATION]
> Règle de Hückel : compter les électrons $\pi$ délocalisés (6) ; le doublet non liant de N n'y participe pas.

#### Solution

La pyridine est plane ; les 3 doubles liaisons apportent **6 électrons $\pi$ délocalisés** $=4(1)+2$ (règle de Hückel, $m=1$). Le doublet non liant de l'azote est dans une orbitale $sp^2$ **dans le plan** : il **ne participe pas** à la délocalisation. La pyridine est donc **aromatique**.

> [!JURY]
> « le doublet non liant porté par l'azote ne participe pas à cette délocalisation » (rapport 2026, p. 20).

### Q47

> [!INDICATION]
> Encombrement stérique (hydrogènes 1/1 et 6/6) vs délocalisation selon l'angle $\Phi$ ; ordre de grandeur 45° pour le biphényle.

#### Solution

À $\Phi=0$, les atomes d'hydrogène en **positions 2/2′ et 6/6′** (ortho) se trouveraient trop proches : répulsion **stérique**. À $\Phi=90°$, les deux cycles ne sont plus conjugués (perte de la **stabilisation par délocalisation**). L'angle d'équilibre $\approx 45°$ du biphényle résulte du **compromis** entre minimisation de la gêne stérique (favorisant 90°) et maintien de la conjugaison (favorisant 0°).

### Q48

> [!INDICATION]
> Bipy neutre trans (répulsion des doublets) ; mono-protonée cis avec liaison hydrogène intramoléculaire N–H···N (schéma).

#### Solution

Schéma attendu : bipy en conformation *trans* (N opposés, $\Phi=180°$) → forme mono-protonée *cis* ($\Phi=0$) avec pont $\text{N}-\text{H}\cdots\text{N}$..

Dans la bipy neutre, $\Phi=180°$ minimise la **répulsion entre doublets non liants** des deux azotes. Mono-protonée, le proton établit une **liaison hydrogène intramoléculaire** $\text{N}-\text{H}\cdots\text{N}$ : les deux azotes se rapprochent et le système devient coplanaire ($\Phi=0$).

#### 2. Stœchiométrie d'un complexe (méthode de Job)

### Q49

> [!INDICATION]
> Absorbances des solutions pures de ligand et d'ions Fe(III) à 574 nm : nulles ; allure de $A=f(x_L)$.

#### Solution

$A_1(0)=-0{,}0013\approx 0$ (Fe(II) pure) et $A_2(1)=-1{,}6398+1{,}6424=0{,}0026\approx 0$ (ligand pur) : **ni le ligand ni le Fe(II) seuls n'absorbent** à 574 nm ; seul le **complexe** absorbe. La courbe $A=f(x_L)$ est donc **triangulaire** (croissante puis décroissante), maximale pour la **fraction stœchiométrique** où le complexe est le plus concentré.

### Q50

> [!INDICATION]
> Écrire la réaction de formation du complexe et un tableau d'avancement avec l'entier $q$ ; $q = x_L/(1-x_L) = 1$.

#### Solution

Pour un complexe $[\text{ML}_q]^{2+}$ et une concentration totale fixée, $n_L = x_L C_{\text{tot}}V$ et $n_M=(1-x_L)C_{\text{tot}}V$. Le complexe est maximal lorsque réactifs en proportions stœchiométriques, $n_L/n_M=q$, soit

$$
\boxed{q = \frac{x_{L,\max}}{1-x_{L,\max}}.}
$$

L'intersection $A_1=A_2$ : $1{,}5761\,x_L - 0{,}0013 = -1{,}6398\,x_L + 1{,}6424 \Rightarrow x_{L,\max}=0{,}511$. D'où $q=\dfrac{0{,}511}{0{,}489}=1{,}0$ : le complexe est **$[\text{ML}]^{2+}$** ($q=1$).

> [!JURY]
> « Trop peu de candidats ont écrit la réaction de formation du complexe et l'ont exploitée » (rapport 2026, p. 20).

### Q51

> [!INDICATION]
> Expliquer l'écart entre $A_{\max}$ expérimentale et les valeurs modélisées (complexation incomplète).

#### Solution

Les modèles $A_1,A_2$ sont des droites valables **loin** du maximum, extrapolant une complexation **totale**. Au voisinage de $x_{L,\max}$, la complexation n'est pas quantitative (constante de formation finie, dissociation partielle) : le complexe réellement formé est moins concentré, d'où une **$A_{\max}$ expérimentale inférieure** à l'ordonnée d'intersection des deux droites.

#### 3. Complexe chiral à base de 2-phénylpyridine

##### a. Synthèse

### Q52

> [!INDICATION]
> Équation $\text{C}_6\text{H}_5\text{Li} + \text{pyridine} \to$ 2-phénylpyridine, avec formules chimiques.

#### Solution

$$
\text{C}_6\text{H}_5\text{Li} + \text{C}_5\text{H}_5\text{N} \longrightarrow \text{C}_6\text{H}_5-\text{C}_5\text{H}_4\text{N} + \text{LiH}.
$$

### Q53

> [!INDICATION]
> EPI, sorbonne (hotte) ; milieu anhydre et atmosphère inerte (réactivité de la base lithiée).

#### Solution

Le phényllithium est une base/nucléophile très fort, détruit par l'eau, le dioxygène et le dioxyde de carbone : travailler en **milieu strictement anhydre**, **sous atmosphère inerte** ($\text{N}_2$ ou Ar), avec solvant éthéré sec. **EPI** (gants, lunettes) et manipulation **sous hotte** (produit corrosif, inflammable).

> [!JURY]
> « peu de candidats ont identifié la très grande réactivité de la base lithiée en milieu non anhydre » (rapport 2026, p. 20).

### Q54

> [!INDICATION]
> Sites de coordination (N et C) ; ligand bidentate ; complexe octaédrique chiral.

#### Solution

Après cyclométallation, le ligand $\text{C}_6\text{H}_4-\text{C}_5\text{H}_4\text{N}$ se lie à l'iridium par **deux sites** : l'azote de la pyridine (doublet) et le carbone aromatique (carbanion) → ligand **bidentate**. Trois ligands bidentates occupent $3\times2=6$ positions → géométrie **octaédrique**. Avec trois ligands bidentates **dissymétriques**, le complexe $\text{Ir(ppy)}_3$ n'admet aucun axe impropre de symétrie : il est **chiral** (configurations $\Delta/\Lambda$).

##### b. Catalyse pour la chimie verte

### Q55

> [!INDICATION]
> Équation du cycle catalytique ($\text{Ar-Br} + \text{amine} \to \text{Ar-N} + \text{HBr}$).

#### Solution

Le cycle réalise l'amination de l'aryle bromé par la pyrrolidine :

$$
4\text{-CF}_3\text{-C}_6\text{H}_4\text{-Br} + \text{C}_4\text{H}_8\text{NH} \longrightarrow 4\text{-CF}_3\text{-C}_6\text{H}_4\text{-N(C}_4\text{H}_8) + \text{HBr}.
$$

### Q56

> [!INDICATION]
> Nommer ET justifier les étapes entre 3–5, 5–6, 7–9 : addition oxydante, substitution, élimination réductrice.

#### Solution

- **3 → 5** : **addition oxydante** de l'aryle bromé sur le $\text{Ni}^0$ → aryl-$\text{Ni}^{II}$-Br.
- **5 → 6** : **substitution de ligand** (coordination de la pyrrolidine avec départ de $\text{H}^+$ et $\text{Br}^-$) → aryl-$\text{Ni}^{II}$-amidure.
- **7 → 9** : **élimination réductrice** formant la liaison **C–N** (libération du dérivé d'aniline) et régénérant un complexe $\text{Ni}^{I}$-Br.

#### 4. Note florale de jasmin

##### a. Jasmone naturelle

### Q57

> [!INDICATION]
> Groupements de la jasmone : cétone (alpha-énone) et alcène.

#### Solution

La jasmone porte : une **cétone $\alpha,\beta$-insaturée** (énone : C=O conjuguée avec la double liaison du cycle) et un **alcène** (double liaison C=C de la chaîne latérale pent-2-ényle).

### Q58

> [!INDICATION]
> Diastéréoisomérie Z/E (et non énantiomérie) ; descripteur Z de la double liaison.

#### Solution

Les *cis*- et *trans*-jasmone sont des **diastéréoisomères Z/E** de la double liaison de la chaîne latérale. Schéma attendu : *cis*-jasmone, double liaison $\text{CH=CH}$ de configuration **Z** (les deux chaînes du même côté).. Descripteur : **Z**.

> [!JURY]
> « Quelques candidats confondent diastéréoisomérie et énantiomérie » (rapport 2026, p. 21).

### Q59

> [!INDICATION]
> Attribution par partenaires de couplage et constantes $J$ (pas seulement le nombre de voisins) ; multiplicité du signal IV.

#### Solution

Chaîne latérale $=\text{CH}-\text{CH}_2(1)-$ côté cycle et $-\text{CH}=\text{CH}(2,3)-\text{CH}_2(4)-\text{CH}_3(5)$, méthyle du cycle $\text{CH}_3(6)$ :
- **VI** ($0{,}988$ ppm, 3H, **triplet**) = $\text{CH}_3(5)$, couplé au seul $\text{CH}_2(4)$.
- **V** ($2{,}064$ ppm, 3H, **singulet**) = $\text{CH}_3(6)$ sur carbone $sp^2$ quaternaire, sans voisin.
- **IV** ($2{,}157$ ppm, 2H) = $\text{CH}_2(4)$, couplé au $\text{CH}_3(5)$ **et** au proton vinylique $\text{H}(3)$ : partenaires de couplage de constantes **différentes** → **multiplet**.
- **III** ($2{,}939$ ppm, 2H) = $\text{CH}_2(1)$, doublement activé (allylique et $\alpha$ de l'énone), fortement déblindé.

##### b. Aldéhydes cinnamiques

### Q60

> [!INDICATION]
> Identifier le réactif énolisable, puis conserver les huit carbones de l’octanal durant l’aldolisation et la crotonisation.

#### Solution

Le benzaldéhyde ne possède pas d'hydrogène en alpha ; c'est le n-octanal $\mathrm{C_6H_{13}{-}CH_2{-}CHO}$ qui fournit l'énolate.

1. $\mathrm{HO^-}$ prélève un proton du carbone alpha de l'octanal. L'énolate est stabilisé entre les formes $\mathrm{C_6H_{13}{-}CH^-{-}CHO}$ et $\mathrm{C_6H_{13}{-}CH{=}CH{-}O^-}$.
2. Le carbone nucléophile de cet énolate attaque le carbone du carbonyle de $\mathrm{Ph{-}CHO}$ ; la liaison pi C=O est déplacée vers O. On forme $\mathrm{Ph{-}CH(O^-){-}CH(C_6H_{13}){-}CHO}$.
3. La protonation par le solvant donne le beta-hydroxyaldéhyde $\mathrm{Ph{-}CH(OH){-}CH(C_6H_{13}){-}CHO}$.
4. Une nouvelle déprotonation en alpha puis le départ de $\mathrm{HO^-}$ forment la double liaison conjuguée (crotonisation E1cb).

Le produit est donc
$$\boxed{\mathrm{Ph{-}CH{=}C(C_6H_{13}){-}CHO}.}$$
Le substituant issu du n-octanal est **hexyle**, comme le montre le comptage des carbones et le dessin de la figure 12. Le nom « alpha-amylaldéhyde cinnamique » dans sa légende inverse ici amyle et hexyle : c'est la structure dessinée et la conservation des carbones qui fixent la réponse.

### Q61

> [!INDICATION]
> Distinguer le substituant alpha de la molécule nucléophile et le groupe alkyle de la molécule électrophile.

#### Solution

Une molécule de n-octanal fournit l'énolate $\mathrm{C_6H_{13}{-}CH^-{-}CHO}$ ; une seconde fournit le carbonyle électrophile, lié à un groupe $\mathrm{C_7H_{15}}$. Après aldolisation et crotonisation, le produit est
$$\boxed{\mathrm{OHC{-}C(C_6H_{13}){=}CH{-}C_7H_{15}}.}$$
On peut l'écrire explicitement
$$\mathrm{CH_3(CH_2)_5{-}C(CHO){=}CH{-}(CH_2)_6CH_3}.$$
Il s'agit du **2-hexyldéc-2-énal**. Contrôle du bilan : le produit contient 16 carbones, issus des deux molécules de n-octanal, et sa formation élimine une molécule d'eau. Une écriture avec $(CH_2)_5CH_3$ aux deux extrémités perdrait un carbone.

##### c. Extraction au CO₂ supercritique

### Q62

> [!INDICATION]
> Justifier la polarité par la géométrie, puis distinguer dipôle permanent, induction et dispersion.

#### Solution

Le dioxyde de carbone est linéaire : $\mathrm{O=C=O}$, type VSEPR $\mathrm{AX_2}$. Chaque oxygène porte deux doublets non liants. Les deux moments dipolaires de liaison, opposés et de même norme, se compensent : la molécule est **apolaire**.

Les interactions de dispersion de London contribuent à la solvatation des molécules peu polaires par le CO2 dense supercritique. Des interactions d'induction sont aussi possibles avec un soluté polaire : l'absence de dipôle permanent du solvant ne les interdit pas. Cette combinaison explique son aptitude à extraire de nombreux composés organiques peu ou modérément polaires, avec un pouvoir solvant modulable par la densité.

### Q63

> [!INDICATION]
> Variance au point triple ($P$ et $T$ fixés) par la règle de Gibbs : $v = 0$.

#### Solution

$v = (c+2) - \varphi$. Corps pur : $c=1$. Au point triple, trois phases coexistent, $\varphi=3$ :

$$
v = (1+2) - 3 = \boxed{0.}
$$

Le point triple est un point **invariant** ($T$ et $P$ imposées).

> [!JURY]
> « Plusieurs candidats considèrent à tort que la variance doit être égale à 1 au point triple » (rapport 2026, p. 21).

## IV. Verres organiques

#### 1. Synthèse du carbonate de diméthyle

### Q64

> [!INDICATION]
> Fractions massiques en entrée depuis la proportion molaire 4/1 (MeOH/EC) et les masses molaires.

#### Solution

Pour 4 mol MeOH ($M=32$) et 1 mol EC ($M=88$) : $m(\text{MeOH})=128$ g, $m(\text{EC})=88$ g, total $216$ g.

$$
\begin{aligned}
w(\text{MeOH}) \\
&= \frac{128}{216} \\
&= \boxed{59{,}3\%},\qquad w(\text{EC}) \\
&= \frac{88}{216} \\
&= \boxed{40{,}7\%.}
\end{aligned}
$$

### Q65

> [!INDICATION]
> Taux de conversion du réactif limitant (à identifier par la stœchiométrie) : $n$ consommé / $n$ initial.

#### Solution

Masse d'entrée $2$ kg : $m(\text{EC})=0{,}407\times2000=814$ g → $n(\text{EC})_0=814/88=9{,}25$ mol ; $m(\text{MeOH})=1186$ g → $n(\text{MeOH})_0=37{,}1$ mol (rapport 4,0). La réaction consomme 2 MeOH par EC, MeOH étant en excès : **EC est limitant**.
DMC formé : $m(\text{DMC})=0{,}191\times2000=382$ g → $n(\text{DMC})=382/90=4{,}24$ mol $=n(\text{EC})_{\text{consommé}}$.

$$
\begin{aligned}
\text{taux de conversion} &= \frac{n(\text{EC})_{\text{consommé}}}{n(\text{EC})_0} \\
&= \frac{4{,}24}{9{,}25} \\
&= \boxed{0{,}46\ (46\%)}.
\end{aligned}
$$

> [!JURY]
> « La définition du taux de conversion est liée au réactif limitant, à déterminer avec la stœchiométrie de la réaction et les quantités de matière introduites en entrée du réacteur » (rapport 2026, p. 16).

### Q66

> [!INDICATION]
> Diagramme binaire DMC/MeOH à 1 bar : azéotrope à minimum ($w=0{,}70$, $63{,}5\ ^\circ\text{C}$) ; domaines liquide, vapeur, équilibre.

#### Solution

Schéma attendu : diagramme $T=f(w_{\text{MeOH}})$ sous 1 bar. $w=0$ (DMC pur) : $90\,°\text{C}$ ; $w=1$ (MeOH pur) : $65\,°\text{C}$ ; **azéotrope à minimum** en $w=0{,}70$,
$T=63{,}5\,°\text{C}$. Courbe d'ébullition (bas) et de rosée (haut) se rejoignant aux corps purs et à l'azéotrope..

Domaines : au-dessus des deux courbes, **vapeur** ; en dessous, **liquide** ; entre les deux fuseaux, **équilibre liquide-vapeur**.

#### 2. Procédé industriel

### Q67

> [!INDICATION]
> Distillation à pression variable pour séparer l'azéotrope : déplacer la composition de l'azéotrope en jouant sur la pression.

#### Solution

Le binaire MeOH/DMC présente un azéotrope à **minimum** dont la composition dépend de la pression : $w_{\text{MeOH}}=0{,}70$ à 1 bar, $0{,}95$ à 10 bar. Une colonne unique ne peut franchir l'azéotrope, mais **deux colonnes à pressions différentes** le permettent. En sortie du réacteur A, le binaire MeOH/DMC est $w_{\text{MeOH}}=54/(54+19{,}1)=0{,}74$.

- **Tour B à 1 bar.** Le feed ($w_{\text{MeOH}}=0{,}74$) donne en tête l'**azéotrope à 0,70** (fraction la plus volatile), les lourds **EG + EC** restant en pied.
- **Tour C à 10 bar.** L'azéotrope issu de B ($0{,}70$) est désormais **du côté riche en DMC** de l'azéotrope à 10 bar ($0{,}95$) : la distillation donne en **pied le DMC pur**, et en **tête l'azéotrope à 0,95** (recyclé).

Choix retenu : $\boxed{P_B = 1\ \text{bar},\ P_C = 10\ \text{bar}.}$

### Q68

> [!INDICATION]
> Bilan de matière : le haut de colonne C (MeOH) est recyclable en entrée du réacteur A.

#### Solution

La tête de la colonne C est l'**azéotrope à 95 % de MeOH** : ce flux, très riche en méthanol (réactif introduit à A dans le rapport 4/1 avec l'EC), peut être **recyclé en entrée du réacteur A**. Il y réintroduit le MeOH non converti (le peu de DMC qu'il contient étant le produit, inerte vis-à-vis de l'alimentation), ce qui limite les pertes de réactif et améliore l'économie du procédé.

### Q69

> [!INDICATION]
> Réaction d'hydrolyse de l'EC par l'eau (EG + CO2) ; nommer les deux espèces produites.

#### Solution

Dans E, le carbonate d'éthyle (carbonate cyclique) est **hydrolysé** :

$$
\text{EC}(\ell) + \text{H}_2\text{O}(\ell) \longrightarrow \text{EG}(\ell) + \text{CO}_2(g).
$$

L'EC (5 % du mélange EG/EC) est ainsi transformé. Les **deux espèces en sortie** sont l'**éthylène glycol** (liquide, produit valorisé comme fluide réfrigérant) et le **dioxyde de carbone** (gaz).

*Fin de la copie.*

## Bilan

Méthodes à retenir : ne pas recopier l'énoncé, répondre strictement à la question posée ; expliciter les hypothèses même données (transformation totale, adiabaticité, monobare/monotherme) et les états physiques des espèces ; expression littérale avant application numérique, résultat avec 1–2 chiffres significatifs sur l'incertitude-type, et commentaire critique du résultat (signe, ordre de grandeur). En oxydoréduction : raisonner sur les couples et les diagrammes E-pH, écrire la formule de Nernst complète, relier constantes d'équilibre et $E^\circ$. En thermochimie : bilans enthalpiques avec la capacité thermique du calorimètre. En spectrophotométrie : Beer-Lambert additif, point isobestique, $pK_a$ lu à $A_{\max}/2$. En cinétique et Monte-Carlo : loi d'ordre 1, loi normale vs uniforme. En chimie organique : mécanismes avec flèches courbes, stœchiométrie (méthode de Job, réactif limitant), sécurité (base lithiée, milieu anhydre). En génie des procédés : bilans de matière, taux de conversion, diagrammes binaires et azéotropes.

Questions classiques transposables : configurations électroniques et place dans le tableau périodique ; radioactivité (équations de désintégration, $\lambda=\ln 2/	au$) ; diagrammes E-pH et médiamutation ; titrages direct, indirect, calorimétrique et pH-métrique (relations à l'équivalence, TAC) ; simulation Monte-Carlo et incertitude-type ; indicateur coloré (pKa, point isobestique) ; aromaticité (Hückel) ; méthode de Job ; cycles catalytiques (addition oxydante, élimination réductrice) ; stéréochimie Z/E ; variance et azéotropes.
