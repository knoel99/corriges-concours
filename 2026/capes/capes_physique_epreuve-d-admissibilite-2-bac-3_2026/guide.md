# CAPES Physique — Épreuve d'admissibilité 2 (bac+3) 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Nature de l'épreuve.** Seconde épreuve d'admissibilité du concours externe et CAFEP (bac+3), section physique-chimie, session 2026 — **majeure physique** : « Centrale solaire orbitale ». Durée 3 heures, coefficient 2, notée sur 20 (une note globale ≤ 5 est éliminatoire). La copie doit reprendre le titre de la partie traitée (« MAJEURE PHYSIQUE »). La partie A fournit des données et un corpus de 8 documents (lancement d'un satellite, formule de Tsiolkovski, ergols UDMH-NTO, transmission atmosphérique, analyseur d'ozone, diffraction, rectenna) ; la partie B comporte 28 questions réparties en trois blocs indépendants : B.1 satellite en orbite et propulsion (Q1–Q10), B.2 acheminement sans fil de l'énergie (Q11–Q21), B.3 antenne réceptrice/rectenna (Q22–Q28). Calculatrice autorisée ; aucun ouvrage ni matériel électronique.

**Statistiques (rapport 2026).** Moyenne de la majeure physique : 10,99 (écart-type 3,84) ; barre d'admissibilité 9,13/20. Taux de réussite décroissants selon les blocs : B.1.a ≈ 40 %, B.1.b ≈ 44 %, B.2.a ≈ 48 %, B.2.b ≈ 42 %, B.2.c ≈ 29 %, B.3.a ≈ 26 %, B.3.b ≈ 17 %.

**Exigences transversales du rapport 2026.** « L'établissement d'expressions littérales est attendu afin de permettre la vérification de l'homogénéité du résultat proposé » ; « un nombre cohérent de chiffres significatifs doit être utilisé » ; « des résultats mis en évidence – par exemple par encadrement » ; « les schémas – correctement légendés – peuvent illustrer à profit le propos » ; « La démarche doit systématiquement être explicitée et les lois utilisées doivent être énoncées. »

**Gestion du temps.** Sur 3 heures : lire d'abord l'ensemble du sujet et les documents pour repérer les questions indépendantes et accessibles (B.1.a, B.2.a, Q19), puis traiter les blocs dans l'ordre en réutilisant les résultats des questions précédentes au sein d'un même bloc ; garder 10 minutes pour les applications numériques et la relecture (homogénéité, unités, chiffres significatifs).

## B.1. Satellite en orbite

### Q1.

> [!INDICATION]
> Appliquer le principe fondamental de la dynamique au satellite (modélisé comme un point matériel) dans le référentiel géocentrique supposé galiléen ; faire un schéma (système, force, base locale).

> [!INDICATION]
> Mouvement circulaire de rayon $r_g$ à vitesse $v_g$ : quelle est l'accélération ? Projeter le PFD sur la base locale.

#### Solution

Système : {satellite de masse $m$}. Référentiel : géocentrique $\mathcal{R}$ supposé galiléen. Force unique : l'attraction gravitationnelle de la Terre,

$$
\vec{F} = -\frac{G M_T m}{r_g^{2}}\,\vec{u_r}.
$$

Pour un mouvement circulaire de rayon $r_g$ parcouru à vitesse $v_g$, l'accélération est purement centripète : $\vec{a} = -\dfrac{v_g^{2}}{r_g}\,\vec{u_r}$. Le PFD $m\vec{a}=\vec{F}$ projeté sur $\vec{u_r}$ donne

$$
\frac{m v_g^{2}}{r_g} = \frac{G M_T m}{r_g^{2}}
\quad\Longrightarrow\quad
\boxed{\,v_g = \sqrt{\dfrac{G M_T}{r_g}}\,}.
$$

(La projection sur $\vec{u_\theta}$ donne $m\,\mathrm{d}v_g/\mathrm{d}t = 0$ : le mouvement est bien uniforme.)

> [!JURY]
> Rapport 2026 : « Le jury attend une démonstration de l’expression de la vitesse du satellite à partir d’une étude dynamique (une analyse dimensionnelle seule ne convient pas). » Ne pas écrire $a = \mathrm{d}v/\mathrm{d}t$ pour le mouvement circulaire.

### Q2.

> [!INDICATION]
> Relier la vitesse à la période de révolution ($v = 2\pi r/T$), égaler à l'expression de Q1, et isoler le rayon $r_g$.

> [!INDICATION]
> Quelle loi obtient-on ? La nommer.

#### Solution

$$
\frac{4\pi^{2} r_g^{2}}{T^{2}} = \frac{G M_T}{r_g}
\quad\Longrightarrow\quad
r_g^{3} = \frac{G M_T\, T^{2}}{4\pi^{2}}
\quad\Longrightarrow\quad
\boxed{\,r_g = \left(\dfrac{G M_T\, T^{2}}{4\pi^{2}}\right)^{1/3}}.
$$

La relation $r_g^{3}\propto T^{2}$ est la **troisième loi de Kepler (loi des périodes)**.

> [!JURY]
> Rapport 2026 : « Il s’agit d’aller au bout de la question en exprimant le rayon en fonction des grandeurs, et non le cube du rayon. » La loi est la troisième loi de Kepler (loi des périodes), pas la loi des aires.

### Q3.

> [!INDICATION]
> L'altitude s'obtient par $h_g = r_g - R_T$ ; quelle est la période d'un satellite géostationnaire ?

> [!INDICATION]
> Une donnée imprimée est inhomogène : la signaler avant l'application numérique.

#### Solution

*Remarque d'énoncé.* La donnée $G=6{,}67\times10^{-1}$ est inhomogène ; on corrige en $G=6{,}67\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.
Un satellite géostationnaire a pour période le jour sidéral $T = 23\,\text{h}\,56\,\text{min} \approx 8{,}616\times10^{4}\ \mathrm{s}$. Alors

$$
\frac{G M_T T^{2}}{4\pi^{2}} = \frac{(3{,}98\times10^{14})(8{,}616\times10^{4})^{2}}{39{,}5} = 7{,}49\times10^{22}\ \mathrm{m^3},
$$

$$
r_g = 4{,}21\times10^{7}\ \mathrm{m},\qquad
\boxed{\,h_g = 4{,}21\times10^{7} - 6{,}38\times10^{6} \approx 3{,}58\times10^{4}\ \mathrm{km}\,}.
$$

Valeur cohérente avec l'altitude ≈ 36 000 km annoncée.

> [!JURY]
> Rapport 2026 : « Une erreur d’impression est présente dans les données fournies par l’énoncé : la constante de gravitation universelle vaut G = 6,67 × 10−11 m3 ⋅kg−1 ⋅s−2. » et « La période de révolution d’un satellite géostationnaire doit être connue. »

### Q4.

> [!INDICATION]
> La force gravitationnelle dérive d'une énergie potentielle : intégrer $F_r = -\mathrm{d}E_p/\mathrm{d}r$.

> [!INDICATION]
> Fixer la constante d'intégration avec la référence $E_p(\infty)=0$ ; attention au signe.

#### Solution

$$
\boxed{\,E_p(r) = -\dfrac{G M_T m}{r}\,}.
$$

> [!PIEGE]
> Erreur fréquente sur le signe de $E_p$ ; l'énoncé demande de déterminer la constante d’intégration à l’aide de la référence fournie ($E_p(\infty)=0$).

### Q5.

> [!INDICATION]
> Justifier la conservation de l'énergie mécanique (force conservative) et l'écrire à l'apogée, où $r = r_g$.

> [!INDICATION]
> $r_p$ et $r_g$ sont des rayons (distances au centre de la Terre), pas des altitudes.

#### Solution

$$
\mathcal{E}_m = \frac{1}{2}m v_a^{2} - \frac{G m M_T}{r_g} = -\frac{G m M_T}{r_p + r_g}.
$$

D'où

$$
\frac{1}{2}v_a^{2} = G M_T\!\left(\frac{1}{r_g} - \frac{1}{r_p+r_g}\right) = \frac{G M_T\, r_p}{r_g\,(r_p+r_g)},
\qquad
\boxed{\,v_a = \sqrt{\dfrac{2 G M_T\, r_p}{r_g\,(r_p+r_g)}}\,}.
$$

AN : $r_p = R_T + 200 = 6{,}58\times10^{6}\ \mathrm{m}$, $r_g = R_T + 35\,786 = 4{,}217\times10^{7}\ \mathrm{m}$, $r_p+r_g = 4{,}875\times10^{7}\ \mathrm{m}$ :

$$
v_a = \sqrt{\frac{2(3{,}98\times10^{14})(6{,}58\times10^{6})}{(4{,}217\times10^{7})(4{,}875\times10^{7})}} \approx 1{,}60\times10^{3}\ \mathrm{m\,s^{-1}}.
$$

Conforme au document 1 (1 597 m·s⁻¹).

> [!JURY]
> Rapport 2026 : « De nombreux candidats exploitent correctement – en oubliant parfois de la justifier – la conservation de l’énergie mécanique du satellite à son apogée de la trajectoire pour obtenir la vitesse demandée. » Confusions fréquentes entre altitude et rayon dans l'AN.

### Q6.

> [!INDICATION]
> $\Delta v = v_g - v_a$ : calculer $v_g$ sur l'orbite géostationnaire (Q1) et $v_a$ (Q5).

> [!INDICATION]
> Confirmer la valeur à l'aide du tableau 1 du document 1 (dernière colonne).

#### Solution

$$
\boxed{\,\Delta v = v_g - v_a \approx 3{,}07\times10^{3} - 1{,}60\times10^{3} \approx 1{,}48\times10^{3}\ \mathrm{m\,s^{-1}}\,}.
$$

Le document 1 donne un accroissement de 1 477 m·s⁻¹ : accord confirmé.

> [!JURY]
> Rapport 2026 : « cette démarche de validation est valorisée même si le candidat n’obtient pas la bonne application numérique. »

**B.1.b. Propulsion chimique**

### Q7.

> [!INDICATION]
> Formule de Tsiolkovski : isoler le rapport $m_i/m_f$, puis la masse de propergol $m_{\text{prop}} = m_i - m_f$.

> [!INDICATION]
> $I_{sp} = 305$ s pour le mélange UDMH-NTO (document 3).

#### Solution

AN : $\dfrac{\Delta v}{g_0 I_{sp}} = \dfrac{1{,}48\times10^{3}}{9{,}81\times305} = 0{,}493$, $e^{-0{,}493} = 0{,}611$ :

$$
\boxed{\,m_{\text{prop}} = 6{,}0\times10^{3}\,(1-0{,}611) \approx 2{,}3\times10^{3}\ \mathrm{kg}\,}.
$$

Commentaire : le propergol représente ≈ 39 % de la masse initiale pour cette seule circularisation — fraction considérable, qui illustre le poids du carburant dans les bilans de masse spatiaux.

> [!JURY]
> Rapport 2026 : « Il faut bien distinguer la masse initiale du satellite, de la masse de carburant. »

### Q8.

> [!INDICATION]
> Équilibrer atome par atome (C, H, O, N) et justifier chaque étape du bilan.

#### Solution

- Carbone : $2 = \beta \Rightarrow \beta = 2$.
- Hydrogène : $8 = 2\delta \Rightarrow \delta = 4$.
- Oxygène : $4\alpha = 2\beta + \delta = 8 \Rightarrow \alpha = 2$.
- Azote : $2 + 2\alpha = 2\gamma \Rightarrow \gamma = 3$.

$$
\boxed{\,\mathrm{C_2H_8N_2} + 2\,\mathrm{N_2O_4} = 2\,\mathrm{CO_2} + 3\,\mathrm{N_2} + 4\,\mathrm{H_2O}\,}\qquad(\alpha,\beta,\gamma,\delta)=(2,2,3,4).
$$

> [!JURY]
> Rapport 2026 : « il est quand même surprenant de trouver des erreurs dans l’équilibrage. L’énoncé indique explicitement de bien justifier la démarche adoptée. »

### Q9.

> [!INDICATION]
> Proportions stœchiométriques : $n_{\text{NTO}} = 2\,n_{\text{UDMH}}$ ; bilan de masse $m_{\text{prop}} = n_1 M_1 + n_2 M_2$.

> [!INDICATION]
> L'énoncé ne demande pas l'application numérique ici.

#### Solution

$$
m_{\text{prop}} = n_1 M_1 + n_2 M_2 = n_1 (M_1 + 2 M_2).
$$

$$
\boxed{\,n_1 = \dfrac{m_{\text{prop}}}{M_1 + 2 M_2},\qquad n_2 = \dfrac{2\,m_{\text{prop}}}{M_1 + 2 M_2}\,}.
$$

> [!JURY]
> Rapport 2026 : « Attention, l’énoncé ne demande pas de réaliser l’application numérique de ces quantités de matière. »

### Q10.

> [!INDICATION]
> $m_i = n_i M_i$ ; calculer $M(\mathrm{C_2H_8N_2})$ et $M(\mathrm{N_2O_4})$ avec les masses molaires données en données.

> [!INDICATION]
> Vérifier $m_1 + m_2 = m_{\text{prop}}$ et les chiffres significatifs.

#### Solution

$$
m_1 = \frac{m_{\text{prop}}\,M_1}{M_1+2M_2},\qquad m_2 = \frac{2\,m_{\text{prop}}\,M_2}{M_1+2M_2}.
$$

AN avec $m_{\text{prop}} = 2{,}3\times10^{3}\ \mathrm{kg}$ :

$$
\boxed{\,m_1 = 2{,}3\times10^{3}\times\tfrac{60}{244} \approx 5{,}7\times10^{2}\ \mathrm{kg}},\qquad
\boxed{\,m_2 = 2{,}3\times10^{3}\times\tfrac{184}{244} \approx 1{,}8\times10^{3}\ \mathrm{kg}\,}.
$$

Vérification : $m_1+m_2 \approx 2{,}3\times10^{3}\ \mathrm{kg} = m_{\text{prop}}$.

## B.2. Acheminer l'énergie sans fil

### Q11.

> [!INDICATION]
> Nommer cette équation d'onde ; identifier $1/c^2 = \mu_0\varepsilon_0$ par comparaison avec la forme canonique.

> [!INDICATION]
> Application numérique avec $\varepsilon_0$ et $\mu_0$ des données.

#### Solution


L'équation donnée est l'**équation de d'Alembert**, ou équation de propagation des ondes. En la comparant à $\Delta\vec E-c^{-2}\partial_t^2\vec E=\vec0$, on obtient

$$
\boxed{c=\frac1{\sqrt{\mu_0\varepsilon_0}}.}
$$

Avec les valeurs fournies,

$$
c=\frac1{\sqrt{(1{,}26\times10^{-6})(8{,}85\times10^{-12})}}
\approx 3{,}0\times10^8\ \mathrm{m\,s^{-1}}.
$$

> [!JURY]
> Rapport 2026 : « Le jury attend le nom particulier de cette forme d’équation d’onde (équation de d’Alembert). » On estime ici $c$ par une AN : on ne cherche pas la valeur fixée par le Système International.

### Q12.

> [!INDICATION]
> Obtenir $\vec{B}$ par l'équation de Maxwell-Faraday (ou la relation de structure de l'onde plane) ; puis $\vec{\Pi} = \vec{E}\times\vec{B}/\mu_0$.

> [!INDICATION]
> Vigilance sur les signes (rotationnel, intégration du sinus) et sur $\vec{e_x}\times\vec{e_y}$.

#### Solution

$$
(\vec{\nabla}\times\vec{E})_y = \frac{\partial E_x}{\partial z} = E_0\,k\sin(2\pi f t - kz).
$$

Donc $\dfrac{\partial B_y}{\partial t} = -E_0 k\sin(2\pi f t - kz)$, et en intégrant (constante continue nulle) :

$$
B_y = \frac{E_0 k}{2\pi f}\cos(2\pi f t - kz) = \frac{E_0}{c}\cos(2\pi f t - kz),
$$

car $\dfrac{k}{2\pi f} = \dfrac{k}{\omega} = \dfrac{1}{c}$. Ainsi

$$
\boxed{\,\vec{B} = \dfrac{E_0}{c}\cos(2\pi f t - kz)\,\vec{e_y}\,}.
$$

Vecteur de Poynting :

$$
\vec{\Pi} = \frac{\vec{E}\times\vec{B}}{\mu_0} = \frac{E_0^{2}}{\mu_0 c}\cos^{2}(2\pi f t - kz)\,\vec{e_z},
$$

puisque $\vec{e_x}\times\vec{e_y} = \vec{e_z}$ : l'énergie se propage bien selon $+z$.

### Q13.

> [!INDICATION]
> $I = \langle\|\vec{\Pi}\|\rangle_t$ est un scalaire ; utiliser $\langle\cos^2\rangle_t = 1/2$.

#### Solution

$$
\boxed{\,I = \dfrac{E_0^{2}}{2\mu_0 c}\,}.
$$

> [!JURY]
> Rapport 2026 : « Les candidats doivent faire attention à ne pas écrire une égalité entre une grandeur scalaire et une grandeur vectorielle. »

### Q14.

> [!INDICATION]
> Argument quantitatif : lire la transmittance sur la figure 3 du document 4 à $\lambda \approx 1\ \mu$m (laser) et à 5–10 cm (micro-ondes).

> [!INDICATION]
> Citer un inconvénient majeur du choix micro-ondes (diffraction, donc divergence du faisceau).

#### Solution


Sur la figure 3 du document 4, la transmittance atmosphérique est de l'ordre de **50 à 70 % autour de $1\ \mu\mathrm m$**, longueur d'onde du laser envisagé, contre une valeur **proche de 100 % pour des micro-ondes de 5 à 10 cm**. À puissance émise égale, la fraction transmise est donc plus grande pour ces micro-ondes. Le document souligne aussi qu'un faisceau laser est davantage affecté par les nuages et la diffusion : le choix micro-ondes facilite le transfert à travers l'atmosphère.

L'inconvénient majeur est la **diffraction** : leur longueur d'onde élevée entraîne une divergence importante à taille d'émetteur donnée. Il faut de très grandes antennes pour concentrer le faisceau sur le récepteur terrestre (voir Q21).

> [!JURY]
> Rapport 2026 : « l’énoncé indique clairement la recherche d’un argument quantitatif, invitant donc le candidat à effectuer une lecture graphique de la figure 3. »

**B.2.b. Absorption du rayonnement par l'ozone**

### Q15.

> [!INDICATION]
> Décrire le principe de l'appareil, pas un protocole : source polychromatique, monochromateur, cuve, détecteur.

> [!INDICATION]
> Ne pas oublier que le monochromateur sélectionne une longueur d'onde de la source polychromatique.

#### Solution


Un spectrophotomètre UV-visible mesure l'absorption d'un rayonnement en fonction de sa longueur d'onde. Une source fournit le rayonnement ; un **monochromateur** sélectionne une bande étroite centrée sur la longueur d'onde choisie. Le faisceau traverse la cuve contenant l'échantillon, puis un **détecteur** mesure l'intensité transmise $I$.

Une mesure de référence, avec le blanc dans la même cuve, fournit $I_0$. L'appareil calcule la transmittance $T=I/I_0$ et l'absorbance

$$
\boxed{A=\log_{10}\!\left(\frac{I_0}{I}\right).}
$$

Le balayage en longueur d'onde donne le spectre d'absorption ; à longueur d'onde fixée, une relation d'étalonnage permet un dosage.

> [!JURY]
> Rapport 2026 : « l’énoncé ne demande pas de décrire un protocole de mesure par spectrophotométrie. On attend ici une explication du principe de fonctionnement de l’appareil. » Peu de copies mentionnent la sélection d'une longueur d'onde de la source polychromatique.

### Q16.

> [!INDICATION]
> Relier la raie de la lampe à mercure (253,7 nm) au maximum du spectre d'absorption de l'ozone (figure 4 du document 5).

#### Solution


La lampe à vapeur de mercure émet une raie intense à **253,7 nm**. Sur la figure 4 du document 5, le maximum d'absorption de l'ozone est situé autour de **250–255 nm**, donc très près de cette raie. À concentration et longueur de cellule données, travailler près du maximum augmente l'absorbance et la sensibilité du dosage. Cette lampe fournit ainsi un rayonnement adapté à la mesure de la concentration en ozone.

> [!JURY]
> Rapport 2026 : « il est préférable d’effectuer une mesure de la longueur d’onde où l’absorbance est maximale sur la figure 4, plutôt que rédiger une phrase confuse mentionnant une absorption dans l’UV. »

### Q17.

> [!INDICATION]
> Calculer $A' = \log(I_0/I)$, puis corriger la longueur de cuve par Beer-Lambert : la courbe d'étalonnage vaut pour $\ell = 800$ mm, l'expérience pour $\ell' = 5$ cm.

#### Solution

Le coefficient $p = \varepsilon\ell$ correspond à $\ell = 0{,}800\ \mathrm{m}$. Pour $\ell' = 0{,}050\ \mathrm{m}$, $A' = \varepsilon\ell' C' = p\,\dfrac{\ell'}{\ell}\,C'$, d'où

$$
C' = \frac{A'\,\ell}{p\,\ell'} = \frac{(7{,}08\times10^{-2})(0{,}800)}{(4{,}94\times10^{-3})(0{,}050)}
\approx \boxed{\,2{,}3\times10^{2}\ \mathrm{mg\,m^{-3}}\,}.
$$

> [!JURY]
> Rapport 2026 : « Il est nécessaire d’exploiter la loi de Beer-Lambert pour prendre en compte cette modification de la longueur traversée. »

**B.2.c. Diffraction**

### Q18.

> [!INDICATION]
> Proposer une expérience avec une onde mécanique (cuve à ondes, fente de largeur $a \sim \lambda$), avec schéma légendé.

> [!INDICATION]
> Ne pas confondre diffraction et interférences, et ne pas utiliser un laser (onde lumineuse).

#### Solution

Dans une cuve à ondes, un vibrateur crée à la surface de l'eau une onde progressive plane de longueur d'onde $\lambda$. On interpose un obstacle percé d'une fente de largeur $a$ comparable à $\lambda$. On observe en aval que l'onde n'est pas limitée à l'ombre géométrique de la fente : elle s'étale angulairement, les fronts devenant circulaires derrière l'ouverture. Cet étalement, d'autant plus marqué que $a$ est petit devant $\lambda$, est caractéristique de la **diffraction**. (On peut mener la même expérience avec des ultrasons et un récepteur mobile.)

> [!JURY]
> Rapport 2026 : « Quelques candidats confondent les phénomènes d’interférences et de diffraction. D’autres ont mal lu la consigne et présentent une expérience de diffraction avec un laser. » Un schéma clair et légendé est attendu.

### Q19.

> [!INDICATION]
> Disque d'Airy : $D = 2{,}44\,\lambda L/d$ ; inverser pour $\lambda$ avec $d = 100\ \mu$m, $L = 41{,}0$ cm, $D = 0{,}522$ cm.

#### Solution

$$
\lambda = \frac{(5{,}22\times10^{-3})(1{,}00\times10^{-4})}{2{,}44\times0{,}410} \approx \boxed{\,5{,}2\times10^{2}\ \mathrm{nm}\,}.
$$

Valeur cohérente avec un laser à diode verte.

### Q20.

> [!INDICATION]
> $u(\bar\lambda) = \sigma_{\exp}/\sqrt{N}$ avec $N = 15$ mesures ; présenter $\lambda = (\bar\lambda \pm u)\ \mathrm{nm}$ avec 1 ou 2 chiffres significatifs pour $u$.

> [!INDICATION]
> Écart normalisé $z$ avec la valeur de référence 640 nm ; commenter.

#### Solution

$$
u(\bar\lambda) = \frac{\sigma_{\exp}(\lambda)}{\sqrt{N}} = \frac{4{,}56}{\sqrt{15}} \approx 1{,}2\ \mathrm{nm}.
$$

Résultat de la mesure :

$$
\boxed{\,\lambda = (627{,}4 \pm 1{,}2)\ \mathrm{nm}\,}.
$$

Comparaison à $\lambda_{\text{réf}} = 640\ \mathrm{nm}$ :

$$
z = \frac{|\bar\lambda - \lambda_{\text{réf}}|}{u(\bar\lambda)} = \frac{|627{,}36 - 640|}{1{,}2} \approx 11.
$$

Comme $z \gg 2$, la mesure est **incompatible** avec la valeur nominale du fabricant. L'écart (≈ 13 nm) est très supérieur à l'incertitude : il révèle un biais systématique de la méthode et/ou le caractère purement indicatif de la longueur d'onde nominale d'une diode laser générique (dispersion de fabrication).

> [!JURY]
> Rapport 2026 : « Le jury rappelle qu’on ne conserve que 1 ou 2 chiffres significatifs pour l’incertitude-type, lors de la présentation du résultat d’une mesure avec son incertitude. » L'énoncé demande un commentaire sur l'écart important avec la donnée du constructeur.

### Q21.

> [!INDICATION]
> Longueur d'onde $\lambda = c/f$ ; divergence d'une ouverture circulaire par diffraction : $\theta \approx 1{,}22\,\lambda/d'$.

> [!INDICATION]
> Inverser pour obtenir le diamètre $d'$ de l'antenne émettrice.

#### Solution

Longueur d'onde : $\lambda = \dfrac{c}{f} = \dfrac{3{,}0\times10^{8}}{5{,}8\times10^{9}} = 5{,}2\times10^{-2}\ \mathrm{m}$.
La limite de diffraction d'une ouverture circulaire impose une divergence $\theta \approx 1{,}22\,\dfrac{\lambda}{d'}$. Avec $\theta = 100\ \mu\mathrm{rad} = 10^{-4}\ \mathrm{rad}$ :

$$
d' \approx \frac{1{,}22\,\lambda}{\theta} = \frac{1{,}22\times5{,}2\times10^{-2}}{10^{-4}} \approx \boxed{\,6\times10^{2}\ \mathrm{m}\,}.
$$

Un diamètre d'émission de l'ordre de plusieurs centaines de mètres (voire ~1 km) est nécessaire : c'est un défi technologique majeur, cohérent avec l'inconvénient identifié en Q14.

> [!JURY]
> Rapport 2026 : « Moins de la moitié des candidats abordent cette question » ; il faut « réaliser un schéma clair et détaillé […] et illustrer la divergence du faisceau ».

## B.3. Antenne réceptrice : rectenna

### Q22.

> [!INDICATION]
> Schéma équivalent en très basse fréquence (bobine = fil, condensateur = ouvert) et en très haute fréquence (inverses) ; conclure sur le type de filtre.

#### Solution

- **Très basse fréquence** ($\omega\to0$) : $Z_{L_1} = jL_1\omega \to 0$ (bobine ≡ fil), $Z_{C_1} = 1/(jC_1\omega)\to\infty$ (condensateur ≡ interrupteur ouvert). Le schéma équivalent relie directement l'entrée à $R_c$ : $u_s \approx u_e$, gain $\to 1$. Le signal passe.
- **Très haute fréquence** ($\omega\to\infty$) : $Z_{L_1}\to\infty$ (bobine ≡ interrupteur ouvert), $Z_{C_1}\to0$ (condensateur ≡ fil court-circuitant $R_c$). Alors $u_s\to 0$, gain $\to 0$. Le signal est bloqué.

Les basses fréquences passent, les hautes sont coupées : c'est bien un **filtre passe-bas**. $\square$

> [!JURY]
> Rapport 2026 : « il ne s’agit pas d’indiquer que le diagramme de Bode, qui se trouve en figure 9, est bien celui d’un filtre passe-bas. Le jury attend du candidat de représenter un schéma équivalent du montage en très basses et très hautes fréquences et d’étudier le comportement du filtre. »

### Q23.

> [!INDICATION]
> Diviseur de tension avec l'impédance parallèle $Z_{//} = R_c/(1 + jR_cC_1\omega)$ ; mettre sous la forme canonique du second ordre.

> [!INDICATION]
> Exprimer $\omega_0$ (en rad/s) et $\xi$ ; calculer leurs valeurs numériques.

#### Solution

$$
\underline{H}(j\omega) = \frac{Z_{//}}{jL_1\omega + Z_{//}} = \frac{R_c}{R_c + jL_1\omega(1 + jR_cC_1\omega)}
= \frac{1}{1 + j\dfrac{L_1\omega}{R_c} - L_1C_1\omega^{2}}.
$$

Identification avec $\underline{H} = \dfrac{1}{1 + 2j\xi\frac{\omega}{\omega_0} - \left(\frac{\omega}{\omega_0}\right)^{2}}$ :

$$
\boxed{\,\omega_0 = \dfrac{1}{\sqrt{L_1 C_1}},\qquad \xi = \dfrac{1}{2R_c}\sqrt{\dfrac{L_1}{C_1}}\,}.
$$

AN : $L_1 = 10\ \mathrm{nH}$, $C_1 = 70\ \mathrm{pF}$, $R_c = 5{,}0\ \Omega$ :

$$
\omega_0 = \frac{1}{\sqrt{(10^{-8})(7\times10^{-11})}} \approx 1{,}2\times10^{9}\ \mathrm{rad\,s^{-1}},\qquad
\xi = \frac{1}{10}\sqrt{\frac{10^{-8}}{7\times10^{-11}}} \approx 1{,}2.
$$

> [!PIEGE]
> Unité de la pulsation propre : $\omega_0$ s'exprime en rad·s⁻¹ (rapport 2026 : « Quelques erreurs sont commises sur l’unité de la pulsation propre »).

### Q24.

> [!INDICATION]
> Lire le gain en décibels à 2,45 GHz sur la figure 9, puis convertir en gain linéaire $G = 10^{G_{\mathrm{dB}}/20}$ ; conclure sur l'atténuation de la fondamentale et des harmoniques.

#### Solution

$$
G = 10^{G_{\mathrm{dB}}/20} = 10^{-43/20} \approx \boxed{\,7\times10^{-3}\,}.
$$

À la fréquence de travail 2,45 GHz, la composante fondamentale du signal redressé et ses harmoniques (de fréquences $\ge 2{,}45$ GHz) sont atténuées d'un facteur ~140 (et davantage pour les harmoniques, le gain décroissant encore). Seule la composante continue (gain ≈ 1 à $\omega\to0$) est transmise à la charge : le filtre DC remplit bien son rôle.

> [!JURY]
> Rapport 2026 : « l’énoncé demande de déterminer le gain du filtre : il faut donc effectuer une opération supplémentaire » (passer des dB au gain linéaire).

**B.3.b. Adaptation d'impédance**

### Q25.

> [!INDICATION]
> Modèle de Thévenin : $U = V_s - R_s I$, donc $I(U)$ est une droite de pente $-1/R_s$ (pas $U = RI$).

> [!INDICATION]
> Lire deux points sur une caractéristique de la figure 10 (court-circuit et tension à vide).

#### Solution

Sur la caractéristique à $-5\ \mathrm{dBm}$, on lit deux points extrêmes : courant de court-circuit ($U=0$) $I_{cc}\approx 4{,}4\times10^{-4}\ \mathrm{A}$ et tension à vide ($I=0$) $V_s \approx 1{,}25\ \mathrm{V}$. D'où

$$
R_s = \frac{V_s}{I_{cc}} = \frac{1{,}25}{4{,}4\times10^{-4}} \approx \boxed{\,3\times10^{3}\ \Omega\,}.
$$

(Les droites étant parallèles, la même pente — donc le même $R_s$ ≈ 3 kΩ — s'obtient sur les courbes à −10 et −15 dBm, ce qui confirme la constance de $R_s$.)

> [!JURY]
> Rapport 2026 : « Beaucoup de candidats utilisent la loi d’Ohm U = RI pour trouver la résistance interne, alors que le dipôle est ici modélisé par un modèle de Thévenin. »

### Q26.

> [!INDICATION]
> Maille série : $I = V_s/(R_s + R_c)$ ; puissance dans $R_c$ : $\mathcal{P}_c = R_c I^2$.

#### Solution

$$
\boxed{\,\mathcal{P}_c = \dfrac{V_s^{2}\,R_c}{(R_s + R_c)^{2}}\,}.
$$

### Q27.

> [!INDICATION]
> Dériver $\mathcal{P}_c(R_c)$ par rapport à $R_c$, annuler la dérivée et conclure (maximum).

> [!INDICATION]
> Exprimer $\mathcal{P}_{c,\max}$.

#### Solution


À partir de Q26, pour $R_c>0$,

$$
\frac{\mathrm d\mathcal P_c}{\mathrm dR_c}
=V_s^2\frac{R_s-R_c}{(R_s+R_c)^3}.
$$

Cette dérivée est positive pour $R_c<R_s$, nulle pour $R_c=R_s$, puis négative pour $R_c>R_s$. La puissance reçue est donc maximale à l'**adaptation d'impédance** $R_c=R_s$, avec

$$
\boxed{\mathcal P_{c,\max}=\frac{V_s^2}{4R_s}.}
$$

### Q28.

> [!INDICATION]
> Rendement $\eta = \mathcal{P}_c/\mathcal{P}_{\text{tot}}$ avec $\mathcal{P}_{\text{tot}} = V_s I = V_s^2/(R_s+R_c)$.

> [!INDICATION]
> Valeur à l'adaptation d'impédance $R_c = R_s$ ; commenter.

#### Solution

$$
\eta = \frac{\mathcal{P}_c}{\mathcal{P}_{\text{tot}}} = \frac{V_s^{2}R_c/(R_s+R_c)^{2}}{V_s^{2}/(R_s+R_c)} = \boxed{\,\dfrac{R_c}{R_s + R_c}\,}.
$$

À l'adaptation d'impédance $R_c = R_s$ :

$$
\eta = \frac{R_s}{2R_s} = \frac{1}{2} = 50\,\%.
$$

Commentaire : le transfert de **puissance maximale** s'accompagne d'un rendement de seulement 50 %, l'autre moitié étant dissipée dans la résistance interne $R_s$. Il existe donc un compromis : maximiser la puissance extraite n'optimise pas le rendement énergétique — un point important pour un système où l'on cherche à récupérer le plus d'énergie possible.

> [!JURY]
> Rapport 2026 : « La définition du rendement pose souvent des difficultés. »

## Bilan

- **Mécanique céleste (B.1)** : PFD en base locale avec schéma (système, force, base) pour un mouvement circulaire ; troisième loi de Kepler ; énergie potentielle gravitationnelle avec référence à l'infini ; conservation de l'énergie mécanique sur l'orbite de transfert (attention aux rayons, pas aux altitudes) ; formule de Tsiolkovski pour la masse de propergol ; équilibrage et bilans de matière stœchiométriques.
- **Ondes électromagnétiques (B.2)** : équation de d'Alembert et célérité ; relation de structure $\vec{B} = \vec{k}\times\vec{E}/\omega$ (signes !) ; vecteur de Poynting et intensité $I = E_0^2/(2\mu_0 c)$ ; lecture quantitative d'un spectre de transmission ; spectrophotométrie UV (Beer-Lambert avec longueur de cuve) ; diffraction par une ouverture circulaire ($D = 2{,}44\lambda L/d$, divergence $\theta \approx 1{,}22\lambda/d'$) ; métrologie (incertitude-type de la moyenne $u = \sigma/\sqrt{N}$, écart normalisé $z$).
- **Électrocinétique de la réception (B.3)** : filtre passe-bas par schémas équivalents TBF/THF et forme canonique du second ordre ; lecture d'un diagramme de Bode (dB → gain linéaire) ; modèle de Thévenin (pente de $I(U)$) ; puissance dans la charge et maximum à l'adaptation d'impédance ($R_c = R_s$, $\mathcal{P}_{\max} = V_s^2/(4R_s)$) ; rendement 50 % à l'adaptation.
- **Transversal** : expression littérale avant l'application numérique, homogénéité, unités, chiffres significatifs, résultats encadrés, schémas légendés — les exigences générales du rapport 2026, valables pour les deux majeures de cette épreuve.
