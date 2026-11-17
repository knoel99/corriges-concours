# CAPES Physique — Épreuve d'admissibilité 2 (bac+3) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Session 2026, concours externe et CAFEP (bac+3), section physique-chimie — **majeure physique** : « Centrale solaire orbitale ». Seconde épreuve d'admissibilité : durée 3 heures, coefficient 2. L'épreuve consiste à répondre de façon argumentée à un questionnement construit autour d'une problématique, en s'appuyant sur un corpus de documents (partie A) ; les questions (partie B) relèvent principalement du programme de la discipline majeure. Calculatrice autorisée (circulaire du 17 juin 2021) ; tout ouvrage, dictionnaire ou autre matériel électronique est interdit.

*Donnée d'énoncé corrigée* : la constante de gravitation universelle imprimée $G = 6{,}67\times10^{-1}$ est une erreur d'impression ; on utilise $G = 6{,}67\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

## B.1. Satellite en orbite

**B.1.a. Orbite géostationnaire**

### Q1.

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

### Q2.

$$
\frac{4\pi^{2} r_g^{2}}{T^{2}} = \frac{G M_T}{r_g}
\quad\Longrightarrow\quad
r_g^{3} = \frac{G M_T\, T^{2}}{4\pi^{2}}
\quad\Longrightarrow\quad
\boxed{\,r_g = \left(\dfrac{G M_T\, T^{2}}{4\pi^{2}}\right)^{1/3}}.
$$

La relation $r_g^{3}\propto T^{2}$ est la **troisième loi de Kepler (loi des périodes)**.

### Q3.

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

### Q4.

$$
\boxed{\,E_p(r) = -\dfrac{G M_T m}{r}\,}.
$$

### Q5.

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

### Q6.

$$
\boxed{\,\Delta v = v_g - v_a \approx 3{,}07\times10^{3} - 1{,}60\times10^{3} \approx 1{,}48\times10^{3}\ \mathrm{m\,s^{-1}}\,}.
$$

Le document 1 donne un accroissement de 1 477 m·s⁻¹ : accord confirmé.

**B.1.b. Propulsion chimique**

### Q7.

AN : $\dfrac{\Delta v}{g_0 I_{sp}} = \dfrac{1{,}48\times10^{3}}{9{,}81\times305} = 0{,}493$, $e^{-0{,}493} = 0{,}611$ :

$$
\boxed{\,m_{\text{prop}} = 6{,}0\times10^{3}\,(1-0{,}611) \approx 2{,}3\times10^{3}\ \mathrm{kg}\,}.
$$

Commentaire : le propergol représente ≈ 39 % de la masse initiale pour cette seule circularisation — fraction considérable, qui illustre le poids du carburant dans les bilans de masse spatiaux.

### Q8.

- Carbone : $2 = \beta \Rightarrow \beta = 2$.
- Hydrogène : $8 = 2\delta \Rightarrow \delta = 4$.
- Oxygène : $4\alpha = 2\beta + \delta = 8 \Rightarrow \alpha = 2$.
- Azote : $2 + 2\alpha = 2\gamma \Rightarrow \gamma = 3$.

$$
\boxed{\,\mathrm{C_2H_8N_2} + 2\,\mathrm{N_2O_4} = 2\,\mathrm{CO_2} + 3\,\mathrm{N_2} + 4\,\mathrm{H_2O}\,}\qquad(\alpha,\beta,\gamma,\delta)=(2,2,3,4).
$$

### Q9.

$$
m_{\text{prop}} = n_1 M_1 + n_2 M_2 = n_1 (M_1 + 2 M_2).
$$

$$
\boxed{\,n_1 = \dfrac{m_{\text{prop}}}{M_1 + 2 M_2},\qquad n_2 = \dfrac{2\,m_{\text{prop}}}{M_1 + 2 M_2}\,}.
$$

### Q10.

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

**B.2.a. Propagation d'énergie sans fil**

### Q11.

L'équation donnée est l'**équation de d'Alembert**, ou équation de propagation des ondes. En la comparant à $\Delta\vec E-c^{-2}\partial_t^2\vec E=\vec0$, on obtient

$$
\boxed{c=\frac1{\sqrt{\mu_0\varepsilon_0}}.}
$$

Avec les valeurs fournies,

$$
c=\frac1{\sqrt{(1{,}26\times10^{-6})(8{,}85\times10^{-12})}}
\approx 3{,}0\times10^8\ \mathrm{m\,s^{-1}}.
$$

### Q12.

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

$$
\boxed{\,I = \dfrac{E_0^{2}}{2\mu_0 c}\,}.
$$

### Q14.

Sur la figure 3 du document 4, la transmittance atmosphérique est de l'ordre de **50 à 70 % autour de $1\ \mu\mathrm m$**, longueur d'onde du laser envisagé, contre une valeur **proche de 100 % pour des micro-ondes de 5 à 10 cm**. À puissance émise égale, la fraction transmise est donc plus grande pour ces micro-ondes. Le document souligne aussi qu'un faisceau laser est davantage affecté par les nuages et la diffusion : le choix micro-ondes facilite le transfert à travers l'atmosphère.

L'inconvénient majeur est la **diffraction** : leur longueur d'onde élevée entraîne une divergence importante à taille d'émetteur donnée. Il faut de très grandes antennes pour concentrer le faisceau sur le récepteur terrestre (voir Q21).

**B.2.b. Absorption du rayonnement par l'ozone**

### Q15.

Un spectrophotomètre UV-visible mesure l'absorption d'un rayonnement en fonction de sa longueur d'onde. Une source fournit le rayonnement ; un **monochromateur** sélectionne une bande étroite centrée sur la longueur d'onde choisie. Le faisceau traverse la cuve contenant l'échantillon, puis un **détecteur** mesure l'intensité transmise $I$.

Une mesure de référence, avec le blanc dans la même cuve, fournit $I_0$. L'appareil calcule la transmittance $T=I/I_0$ et l'absorbance

$$
\boxed{A=\log_{10}\!\left(\frac{I_0}{I}\right).}
$$

Le balayage en longueur d'onde donne le spectre d'absorption ; à longueur d'onde fixée, une relation d'étalonnage permet un dosage.

### Q16.

La lampe à vapeur de mercure émet une raie intense à **253,7 nm**. Sur la figure 4 du document 5, le maximum d'absorption de l'ozone est situé autour de **250–255 nm**, donc très près de cette raie. À concentration et longueur de cellule données, travailler près du maximum augmente l'absorbance et la sensibilité du dosage. Cette lampe fournit ainsi un rayonnement adapté à la mesure de la concentration en ozone.

### Q17.

Le coefficient $p = \varepsilon\ell$ correspond à $\ell = 0{,}800\ \mathrm{m}$. Pour $\ell' = 0{,}050\ \mathrm{m}$, $A' = \varepsilon\ell' C' = p\,\dfrac{\ell'}{\ell}\,C'$, d'où

$$
C' = \frac{A'\,\ell}{p\,\ell'} = \frac{(7{,}08\times10^{-2})(0{,}800)}{(4{,}94\times10^{-3})(0{,}050)}
\approx \boxed{\,2{,}3\times10^{2}\ \mathrm{mg\,m^{-3}}\,}.
$$

**B.2.c. Diffraction**

### Q18.

Dans une cuve à ondes, un vibrateur crée à la surface de l'eau une onde progressive plane de longueur d'onde $\lambda$. On interpose un obstacle percé d'une fente de largeur $a$ comparable à $\lambda$. On observe en aval que l'onde n'est pas limitée à l'ombre géométrique de la fente : elle s'étale angulairement, les fronts devenant circulaires derrière l'ouverture. Cet étalement, d'autant plus marqué que $a$ est petit devant $\lambda$, est caractéristique de la **diffraction**. (On peut mener la même expérience avec des ultrasons et un récepteur mobile.)

### Q19.

$$
\lambda = \frac{(5{,}22\times10^{-3})(1{,}00\times10^{-4})}{2{,}44\times0{,}410} \approx \boxed{\,5{,}2\times10^{2}\ \mathrm{nm}\,}.
$$

Valeur cohérente avec un laser à diode verte.

### Q20.

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

### Q21.

Longueur d'onde : $\lambda = \dfrac{c}{f} = \dfrac{3{,}0\times10^{8}}{5{,}8\times10^{9}} = 5{,}2\times10^{-2}\ \mathrm{m}$.
La limite de diffraction d'une ouverture circulaire impose une divergence $\theta \approx 1{,}22\,\dfrac{\lambda}{d'}$. Avec $\theta = 100\ \mu\mathrm{rad} = 10^{-4}\ \mathrm{rad}$ :

$$
d' \approx \frac{1{,}22\,\lambda}{\theta} = \frac{1{,}22\times5{,}2\times10^{-2}}{10^{-4}} \approx \boxed{\,6\times10^{2}\ \mathrm{m}\,}.
$$

Un diamètre d'émission de l'ordre de plusieurs centaines de mètres (voire ~1 km) est nécessaire : c'est un défi technologique majeur, cohérent avec l'inconvénient identifié en Q14.

## B.3. Antenne réceptrice : rectenna

**B.3.a. Étude du filtre de sortie DC**

### Q22.

- **Très basse fréquence** ($\omega\to0$) : $Z_{L_1} = jL_1\omega \to 0$ (bobine ≡ fil), $Z_{C_1} = 1/(jC_1\omega)\to\infty$ (condensateur ≡ interrupteur ouvert). Le schéma équivalent relie directement l'entrée à $R_c$ : $u_s \approx u_e$, gain $\to 1$. Le signal passe.
- **Très haute fréquence** ($\omega\to\infty$) : $Z_{L_1}\to\infty$ (bobine ≡ interrupteur ouvert), $Z_{C_1}\to0$ (condensateur ≡ fil court-circuitant $R_c$). Alors $u_s\to 0$, gain $\to 0$. Le signal est bloqué.

Les basses fréquences passent, les hautes sont coupées : c'est bien un **filtre passe-bas**. $\square$

### Q23.

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

### Q24.

$$
G = 10^{G_{\mathrm{dB}}/20} = 10^{-43/20} \approx \boxed{\,7\times10^{-3}\,}.
$$

À la fréquence de travail 2,45 GHz, la composante fondamentale du signal redressé et ses harmoniques (de fréquences $\ge 2{,}45$ GHz) sont atténuées d'un facteur ~140 (et davantage pour les harmoniques, le gain décroissant encore). Seule la composante continue (gain ≈ 1 à $\omega\to0$) est transmise à la charge : le filtre DC remplit bien son rôle.

**B.3.b. Adaptation d'impédance**

### Q25.

Sur la caractéristique à $-5\ \mathrm{dBm}$, on lit deux points extrêmes : courant de court-circuit ($U=0$) $I_{cc}\approx 4{,}4\times10^{-4}\ \mathrm{A}$ et tension à vide ($I=0$) $V_s \approx 1{,}25\ \mathrm{V}$. D'où

$$
R_s = \frac{V_s}{I_{cc}} = \frac{1{,}25}{4{,}4\times10^{-4}} \approx \boxed{\,3\times10^{3}\ \Omega\,}.
$$

(Les droites étant parallèles, la même pente — donc le même $R_s$ ≈ 3 kΩ — s'obtient sur les courbes à −10 et −15 dBm, ce qui confirme la constance de $R_s$.)

### Q26.

$$
\boxed{\,\mathcal{P}_c = \dfrac{V_s^{2}\,R_c}{(R_s + R_c)^{2}}\,}.
$$

### Q27.

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

$$
\eta = \frac{\mathcal{P}_c}{\mathcal{P}_{\text{tot}}} = \frac{V_s^{2}R_c/(R_s+R_c)^{2}}{V_s^{2}/(R_s+R_c)} = \boxed{\,\dfrac{R_c}{R_s + R_c}\,}.
$$

À l'adaptation d'impédance $R_c = R_s$ :

$$
\eta = \frac{R_s}{2R_s} = \frac{1}{2} = 50\,\%.
$$

Commentaire : le transfert de **puissance maximale** s'accompagne d'un rendement de seulement 50 %, l'autre moitié étant dissipée dans la résistance interne $R_s$. Il existe donc un compromis : maximiser la puissance extraite n'optimise pas le rendement énergétique — un point important pour un système où l'on cherche à récupérer le plus d'énergie possible.
