# Banque PT PT — Physique B - Thermodynamique 2016 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille Claude) · effort non renseigné · vitesse non renseignée

Épreuve de 2 heures, sans calculatrice, sur la géothermie domestique : 25 questions (1.1 à 3.7.d) en trois parties indépendantes. Les 25 questions sont traitées. Le sujet ne comporte aucun diagramme thermodynamique à lire : les enthalpies massiques du R407C viennent du tableau de la page 6 de l'énoncé, et les valeurs $\ln 5 = 1{,}6$, $\sqrt{1/0{,}3} = 1{,}8$ et $\ln 0{,}03 = -3{,}5$ sont fournies.

[Sujet officiel](https://www.banquept.fr/documents/2016/ph_b_th_2016_pt.pdf) · [Rapport du jury](https://www.banquept.fr/documents/ecrit/rapport/2016/rapport_phys_b_ecrit_2016.pdf)

## Partie 1 — Études préliminaires sur les ondes thermiques

### Question 1.1 — Équation de la diffusion thermique

*Système.* La tranche de sol de section $S$ comprise entre $z$ et $z+\mathrm{d}z$, de masse $\rho S\,\mathrm{d}z$. C'est un système fermé, immobile, formé d'une phase condensée indilatable : il ne reçoit aucun travail et son énergie interne ne dépend que de la température, avec $\mathrm{d}U = \rho S\,\mathrm{d}z\,c\,\mathrm{d}T$.

*Variation d'énergie interne entre $t$ et $t+\mathrm{d}t$.*

$$\mathrm{d}U = \rho c S\,\mathrm{d}z\,\big[T(z,t+\mathrm{d}t)-T(z,t)\big] = \rho c S\,\mathrm{d}z\,\frac{\partial T}{\partial t}\,\mathrm{d}t$$

*Transfert thermique reçu.* Le flux est vertical : on note $j(z,t)$ la composante selon $z$ du vecteur densité de flux thermique. La tranche reçoit de la chaleur par sa face en $z$ et en cède par sa face en $z+\mathrm{d}z$ :

$$\delta Q = j(z,t)\,S\,\mathrm{d}t - j(z+\mathrm{d}z,t)\,S\,\mathrm{d}t = -\frac{\partial j}{\partial z}\,S\,\mathrm{d}z\,\mathrm{d}t$$

*Premier principe* ($\mathrm{d}U = \delta Q$, sans travail) :

$$\rho c\,\frac{\partial T}{\partial t} = -\frac{\partial j}{\partial z}$$

*Loi de Fourier* : $j = -\lambda\,\dfrac{\partial T}{\partial z}$, avec $\lambda$ uniforme. On obtient

$$\boxed{\rho c\,\frac{\partial T}{\partial t} = \lambda\,\frac{\partial^2 T}{\partial z^2}}$$

### Question 1.2 — Pulsations annuelle et journalière

Les périodes associées sont $T_A = 2\pi/\omega_A = 1$ an et $T_J = 2\pi/\omega_J = 1$ jour.

- $\omega_A$ décrit l'**alternance des saisons** (variation annuelle de la température extérieure moyenne, été et hiver).
- $\omega_J$ décrit l'**alternance du jour et de la nuit** (variation journalière).

Vérification des valeurs : un an vaut $365\times 24\times 3600 \approx 3{,}2\times 10^{7}$ s, d'où $\omega_A \approx 2{,}0\times 10^{-7}\ \mathrm{rad\cdot s^{-1}}$ ; un jour vaut $86\,400$ s, d'où $\omega_J \approx 7{,}3\times 10^{-5}\ \mathrm{rad\cdot s^{-1}}$.

### Question 1.3 — Expression de δ

On pose $u = \omega t + \varphi - z/\delta$ et $E = \mathrm{e}^{-z/\delta}$, de sorte que $T = T_0 + \alpha E\cos u$.

Dérivée temporelle :

$$\frac{\partial T}{\partial t} = -\alpha\,\omega\,E\,\sin u$$

Dérivées spatiales, avec $\dfrac{\partial E}{\partial z} = -\dfrac{E}{\delta}$ et $\dfrac{\partial u}{\partial z} = -\dfrac{1}{\delta}$ :

$$\frac{\partial T}{\partial z} = \frac{\alpha E}{\delta}\,\big(\sin u - \cos u\big)$$

$$\frac{\partial^2 T}{\partial z^2} = \frac{\alpha E}{\delta^2}\,\big[-(\sin u - \cos u) - (\cos u + \sin u)\big] = -\frac{2\,\alpha E}{\delta^2}\,\sin u$$

L'équation de diffusion s'écrit alors, pour tout $z$ et tout $t$,

$$-\rho c\,\alpha\,\omega\,E\,\sin u = -\frac{2\lambda\,\alpha E}{\delta^2}\,\sin u$$

ce qui impose $\rho c\,\omega = \dfrac{2\lambda}{\delta^2}$, soit

$$\boxed{\delta = \sqrt{\frac{2\lambda}{\rho c\,\omega}}}$$

La forme proposée vérifie en outre la condition en surface, $T(0,t) = T_0 + \alpha\cos(\omega t+\varphi)$ avec $\alpha = a$, et reste bornée quand $z \to +\infty$. Homogénéité : $\lambda/(\rho c)$ est une diffusivité en $\mathrm{m^2\cdot s^{-1}}$, donc $\delta$ est bien une longueur.

### Question 1.4 — Sens physique de δ

$\delta$ est une longueur, appelée **épaisseur de peau thermique** ou profondeur de pénétration de l'onde thermique.

- Dans le facteur $\mathrm{e}^{-z/\delta}$, c'est la **distance caractéristique d'amortissement** : l'amplitude des oscillations de température est divisée par $\mathrm{e} \approx 2{,}7$ chaque fois que la profondeur augmente de $\delta$. Au-delà de quelques $\delta$ (amplitude réduite à 5 % en $3\delta$, à moins de 1 % en $5\delta$), le sol ne ressent plus les variations de surface et reste à $T_0$.
- Dans la phase $\omega t + \varphi - z/\delta$, c'est aussi l'échelle du **retard** : l'oscillation à la profondeur $z$ est en retard de $z/(\omega\delta)$ sur celle de la surface, et la longueur d'onde vaut $2\pi\delta$.

$\delta$ diminue quand la pulsation augmente : les variations rapides pénètrent moins que les variations lentes.

### Question 1.5 — Phénomène analogue

L'**effet de peau** en électromagnétisme : dans un conducteur ohmique de conductivité $\gamma$, le champ et le courant de pulsation $\omega$ vérifient eux aussi une équation de diffusion et ne pénètrent que sur une épaisseur

$$\delta_{\text{ém}} = \sqrt{\frac{2}{\mu_0\,\gamma\,\omega}}$$

Elle joue le même rôle que $\delta$ : amortissement exponentiel et dépendance en $1/\sqrt{\omega}$ (le courant alternatif se concentre à la surface des conducteurs à haute fréquence).

### Question 1.6 — Valeurs de δ

On a $\rho c = 1500\times 1000 = 1{,}5\times 10^{6}\ \mathrm{J\cdot m^{-3}\cdot K^{-1}}$ et $2\lambda = 1{,}0\ \mathrm{W\cdot m^{-1}\cdot K^{-1}}$.

*Variations journalières* ($\omega_J = 7\times 10^{-5}\ \mathrm{rad\cdot s^{-1}}$) :

$$\delta_J = \sqrt{\frac{1{,}0}{1{,}5\times 10^{6}\times 7\times 10^{-5}}} = \sqrt{\frac{1}{105}}\ \mathrm{m}$$

$$\boxed{\delta_J \approx 0{,}1\ \mathrm{m} = 10\ \mathrm{cm}}$$

*Variations annuelles* ($\omega_A = 2\times 10^{-7}\ \mathrm{rad\cdot s^{-1}}$) :

$$\delta_A = \sqrt{\frac{1{,}0}{1{,}5\times 10^{6}\times 2\times 10^{-7}}} = \sqrt{\frac{1}{0{,}3}}\ \mathrm{m}$$

$$\boxed{\delta_A \approx 1{,}8\ \mathrm{m}}$$

*Commentaire.* Le rapport $\delta_A/\delta_J = \sqrt{\omega_J/\omega_A} \approx 19$ traduit la dépendance en $1/\sqrt{\omega}$. L'alternance du jour et de la nuit n'affecte que les premiers décimètres du sol : à quelques dizaines de centimètres de profondeur, elle a disparu. Les variations saisonnières pénètrent de plusieurs mètres : il faut descendre à 5 ou 10 m pour trouver une température pratiquement constante sur l'année, égale à $T_0$. C'est ce qui rend le sol intéressant comme source de chaleur en hiver (et de fraîcheur en été), à condition d'enterrer les tuyaux assez profondément.

### Question 1.7 — Profondeur d'atténuation par 5

L'amplitude à la profondeur $z$ est $\alpha\,\mathrm{e}^{-z/\delta}$. Elle est divisée par 5 quand $\mathrm{e}^{-z/\delta} = 1/5$, soit

$$\boxed{z_5 = \delta\,\ln 5 \approx 1{,}6\,\delta}$$

Pour $\omega_A = 2{,}0\times 10^{-7}\ \mathrm{rad\cdot s^{-1}}$, $\delta = \delta_A = 1{,}8$ m, d'où

$$z_5 = 1{,}6\times 1{,}8 = 2{,}9\ \mathrm{m}$$

$$\boxed{z_5 \approx 3\ \mathrm{m}}$$

À 3 m de profondeur, l'écart annuel de température n'est plus que le cinquième de celui de la surface.

## Partie 2 — Dimensionnement d'un puits canadien

### Question 2.1 — Renouvellement de l'air et rôle du puits

*Pourquoi renouveler l'air.* Les occupants et leurs activités consomment le dioxygène et chargent l'air en dioxyde de carbone, en vapeur d'eau (respiration, cuisine, douches) et en polluants. Il faut évacuer cet air vicié et cette humidité (risque de condensation et de moisissures) et apporter de l'air neuf.

*Inconvénient.* En hiver, l'air qui entre est à $T_{EXT} = -4\ \mathrm{°C}$ et l'air chauffé à $T_L = 19\ \mathrm{°C}$ est rejeté : il faut dépenser de l'énergie de chauffage pour amener en permanence l'air entrant à la température du logement. Le renouvellement d'air est une perte thermique.

*Durée de renouvellement.* Le volume du logement est $V = 100\times 2 = 200\ \mathrm{m^3}$ :

$$\tau = \frac{V}{D_V} = \frac{200}{50}$$

$$\boxed{\tau = 4\ \mathrm{h}}$$

*Rôle du puits canadien.* Il préchauffe l'air neuf en hiver en le faisant circuler dans le sol, dont la température $T_0 = 12\ \mathrm{°C}$ est supérieure à celle de l'air extérieur et presque constante en profondeur (partie 1). L'air entre moins froid, ce qui réduit la dépense de chauffage. En été, le même dispositif rafraîchit l'air entrant.

### Question 2.2 — Température maximale et puissance gagnée

*Température maximale.* L'air n'échange de la chaleur qu'avec le sol à $T_0$. Si le tuyau est assez long, il atteint l'équilibre thermique avec le sol :

$$\boxed{T_{\max} = T_0 = 12\ \mathrm{°C}}$$

Il ne peut pas la dépasser : le transfert thermique cesse quand les températures sont égales.

*Puissance gagnée.* L'air est un fluide en écoulement stationnaire, de débit massique $D_m = \rho D_V$, chauffé à pression constante sans travail utile. Le premier principe pour un système ouvert en régime stationnaire donne la puissance thermique nécessaire pour faire passer l'air d'une température d'entrée $T_e$ à $T_L$ : $P_{\text{ch}} = D_m c_P\,(T_L - T_e)$. On compare les deux situations.

$$P_{\text{sans}} = \rho D_V c_P\,(T_L - T_{EXT})$$

$$P_{\text{avec}} = \rho D_V c_P\,(T_L - T_0)$$

$$\boxed{P = P_{\text{sans}} - P_{\text{avec}} = \rho D_V c_P\,(T_0 - T_{EXT})}$$

Application numérique, avec $D_V = 50/3600 = 1{,}4\times 10^{-2}\ \mathrm{m^3\cdot s^{-1}}$ :

$$D_m = \rho D_V = \frac{1{,}275\times 50}{3600} = 1{,}8\times 10^{-2}\ \mathrm{kg\cdot s^{-1}}$$

$$P = 1{,}8\times 10^{-2}\times 1000\times \big(12-(-4)\big) = 1{,}8\times 10^{-2}\times 1000\times 16$$

$$\boxed{P \approx 2{,}8\times 10^{2}\ \mathrm{W} \approx 0{,}3\ \mathrm{kW}}$$

*Commentaire.* Sans puits, le chauffage de l'air neuf coûte $P_{\text{sans}} = 1{,}8\times 10^{-2}\times 1000\times 23 \approx 4{,}1\times 10^{2}$ W ; avec un puits idéal, $P_{\text{avec}} \approx 1{,}2\times 10^{2}$ W. Le puits supprime donc environ 70 % de la perte par renouvellement d'air, sans autre dépense que celle du ventilateur. En valeur absolue, 0,3 kW reste modeste devant la puissance de chauffage d'un logement (quelques kilowatts, 7 kW au maximum dans la partie 3) : le puits canadien est un appoint, pas un moyen de chauffage. Il ne peut pas amener l'air à 19 °C.

### Question 2.3 — Profil de température dans le tuyau

*Système.* L'air contenu dans la tranche de tuyau fixe comprise entre $x$ et $x+\mathrm{d}x$ : c'est un **système ouvert**, traversé par le débit massique $D_m = \rho D_V$, en **régime permanent**.

*Premier principe pour un écoulement stationnaire.* On néglige les variations d'énergie cinétique (section et masse volumique constantes, donc vitesse constante) et d'énergie potentielle ; il n'y a aucune pièce mobile, donc aucun travail utile. En notant $h_m$ l'enthalpie massique de l'air et $\delta P_{\text{th}}$ la puissance thermique reçue par l'air à travers la paroi de la tranche :

$$D_m\,\big[h_m(x+\mathrm{d}x) - h_m(x)\big] = \delta P_{\text{th}}$$

L'air est assimilé à un gaz parfait (la pression est de plus constante) : $\mathrm{d}h_m = c_P\,\mathrm{d}T$.

*Puissance reçue.* La loi de Newton donne, à travers la paroi latérale d'aire $2\pi R\,\mathrm{d}x$, un flux dirigé du plus chaud vers le plus froid. La puissance reçue par l'air de la part du sol est

$$\delta P_{\text{th}} = h\,\big(T_0 - T(x)\big)\,2\pi R\,\mathrm{d}x = -h\,\theta(x)\,2\pi R\,\mathrm{d}x$$

*Équation différentielle.* Comme $T_0$ est uniforme, $\mathrm{d}T = \mathrm{d}\theta$ :

$$\rho D_V c_P\,\frac{\mathrm{d}\theta}{\mathrm{d}x} = -2\pi R\,h\,\theta$$

$$\boxed{\frac{\mathrm{d}\theta}{\mathrm{d}x} + K\,\theta = 0 \quad\text{avec}\quad K = \frac{2\pi h R}{\rho D_V c_P}}$$

*Solution.* C'est une équation linéaire du premier ordre à coefficient constant. Avec $\theta(0) = \theta_i = T_{EXT} - T_0$ à l'entrée du puits,

$$\boxed{\theta(x) = \theta_i\,\mathrm{e}^{-Kx}}$$

$K$ est l'inverse d'une longueur ; ici $\theta_i = -4 - 12 = -16\ \mathrm{°C}$. On retrouve $\theta \to 0$, c'est-à-dire $T \to T_0$, pour un tuyau très long (question 2.2).

*Contrôle de la valeur de $K$ donnée à la question suivante.* Avec $D_V = 1{,}39\times 10^{-2}\ \mathrm{m^3\cdot s^{-1}}$ et $R = 0{,}050$ m, l'expression de l'énoncé donne $h \approx 8{,}5\ \mathrm{W\cdot m^{-2}\cdot K^{-1}}$, puis $K = 2\pi\times 8{,}5\times 0{,}050/(1{,}275\times 1{,}39\times 10^{-2}\times 1000) \approx 0{,}15\ \mathrm{m^{-1}}$ : c'est bien la valeur fournie (ce calcul n'est pas faisable à la main et n'est pas demandé).

### Question 2.4 — Longueur du puits

La température Celsius maximale est $T_0 = 12\ \mathrm{°C}$. On veut en sortie

$$T_{\text{FINALE}} = 0{,}96\,T_0 = 11{,}52\ \mathrm{°C}$$

soit

$$\theta(L) = T_{\text{FINALE}} - T_0 = -0{,}04\,T_0 = -0{,}48\ \mathrm{°C}$$

Avec $\theta_i = -16\ \mathrm{°C}$ :

$$\frac{\theta(L)}{\theta_i} = \frac{0{,}48}{16} = 0{,}03 = \mathrm{e}^{-KL}$$

$$\boxed{L = -\frac{\ln 0{,}03}{K} = \frac{1}{K}\,\ln\frac{\theta_i}{\theta(L)}}$$

$$L = \frac{3{,}5}{0{,}15}$$

$$\boxed{L \approx 23\ \mathrm{m}}$$

C'est une longueur réaliste pour une tranchée dans un jardin. Comme la température de sortie croît avec la longueur, toute longueur supérieure convient ; 23 m est la longueur minimale.

### Question 2.5 — Effet du débit

Pour un rapport $\theta(L)/\theta_i$ fixé, $L = 3{,}5/K$ est proportionnelle à $1/K$. En reportant $h = 1{,}18\,D_V^{0{,}8}/R^{1{,}8}$ dans $K$ :

$$K = \frac{2\pi\times 1{,}18}{\rho\,c_P}\,\frac{1}{D_V^{0{,}2}\,R^{0{,}8}}$$

$$\boxed{L \propto \frac{1}{K} \propto D_V^{0{,}2}\,R^{0{,}8}}$$

À rayon fixé, deux effets s'opposent quand le débit augmente.

- *Transport.* Le débit massique d'air à réchauffer augmente : chaque tranche d'air séjourne moins longtemps dans le tuyau (vitesse $v = D_V/\pi R^2$ plus grande) et dispose de moins de temps pour se réchauffer. Cet effet, seul, rendrait $L$ proportionnelle à $D_V$.
- *Échange à la paroi.* Le coefficient $h$ augmente avec le débit (en $D_V^{0{,}8}$) : un écoulement plus rapide brasse mieux l'air et amincit la couche limite thermique, le transfert conducto-convectif est plus efficace. Cet effet, seul, raccourcirait $L$.

Les deux effets se compensent presque : **la longueur nécessaire augmente avec le débit, mais très faiblement**, en $D_V^{0{,}2}$. Doubler le débit ne l'allonge que de 15 % ($2^{0{,}2} \approx 1{,}15$), soit 27 m au lieu de 23 m.

### Question 2.6 — Effet du diamètre

D'après la question 2.5, à débit fixé, $K \propto h\,R \propto R^{-0{,}8}$ et $L \propto R^{0{,}8}$. Deux effets s'opposent quand le rayon (donc le diamètre) augmente.

- *Surface d'échange.* L'aire de paroi par unité de longueur, $2\pi R$, augmente : à $h$ donné, l'échange serait meilleur et $L$ plus courte (en $1/R$).
- *Échange à la paroi.* À débit fixé, la vitesse de l'air $v = D_V/\pi R^2$ diminue fortement, et $h$ chute en $R^{-1{,}8}$ : l'air, plus lent et plus éloigné en moyenne de la paroi, échange moins bien avec elle.

Le second effet l'emporte : **la longueur nécessaire augmente avec le diamètre**, presque proportionnellement ($R^{0{,}8}$). Doubler le rayon multiplie $L$ par $2^{0{,}8} \approx 1{,}7$, soit environ 40 m. Du seul point de vue thermique, un tuyau fin est préférable ; mais un tuyau trop fin impose une vitesse élevée et une perte de charge importante, donc un ventilateur plus puissant. C'est pourquoi l'énoncé retient finalement un diamètre fixé par la perte de charge et non par la contrainte thermique.

## Partie 3 — Remplacement d'un chauffage électrique par un chauffage géothermique horizontal

### Question 3.1 — Principe d'une pompe à chaleur

Une pompe à chaleur est une **machine thermique ditherme réceptrice**. Un fluide frigorigène y décrit un cycle au cours duquel :

- il reçoit un **travail** $W > 0$ de la part du compresseur (énergie électrique consommée) ;
- il **prélève** un transfert thermique $Q_f > 0$ à la **source froide** (ici le sol, par l'intermédiaire de l'eau glycolée du circuit capteur) ;
- il **cède** un transfert thermique à la **source chaude** (ici l'eau du circuit de chauffage, donc le logement) : $Q_c < 0$.

Le transfert de chaleur du froid vers le chaud n'est pas spontané (second principe) : c'est le travail fourni qui le permet. Sur un cycle, le premier principe donne $W + Q_c + Q_f = 0$, donc $|Q_c| = Q_f + W$ : le logement reçoit plus d'énergie thermique que la machine ne consomme d'énergie électrique, la différence étant puisée gratuitement dans le sol. L'intérêt se mesure par l'efficacité $e = |Q_c|/W > 1$.

![Figure 1 — Principe de la pompe à chaleur : sources, sens et signes des transferts d'énergie reçus par le fluide](figures/principe-pompe-a-chaleur.svg)

### Question 3.2 — Place du circuit capteur

Le circuit capteur est enterré : l'eau glycolée qui y circule se réchauffe au contact du sol, puis transporte cette chaleur jusqu'à la pompe à chaleur. Elle joue le rôle de **source froide**. Elle doit donc être en contact thermique avec l'élément où le fluide frigorigène **reçoit** de la chaleur, c'est-à-dire l'**évaporateur** (transformation 4 → 1).

Justification : dans l'évaporateur, le fluide est à basse pression (6 bar) et se vaporise à basse température (5 °C), ce qui absorbe de la chaleur ($q_f = h_1 - h_4 > 0$). Sa température y est assez basse pour qu'il puisse recevoir de la chaleur de l'eau glycolée venue du sol. Le condenseur, à 60 °C, est au contraire en contact avec l'eau du circuit de chauffage, à laquelle le fluide cède de la chaleur en se liquéfiant.

### Question 3.3 — Puissance moyenne de chauffage

Toute l'énergie annuelle de chauffage, $E = 7000$ kWh, est consommée pendant les six mois de chauffe, supposée continue (jour et nuit). Six mois représentent

$$\Delta t = \frac{365\times 24}{2} \approx 4{,}4\times 10^{3}\ \mathrm{h}$$

$$\boxed{P_{\text{moy}} = \frac{E}{\Delta t} = \frac{7000}{4{,}4\times 10^{3}} \approx 1{,}6\ \mathrm{kW}}$$

### Question 3.4 — Puissance maximale de 7000 W

La puissance maximale retenue, 7 kW, vaut environ **4,4 fois la puissance moyenne** de 1,6 kW (soit 70 W par mètre carré habitable).

Cet écart est justifié. Le besoin de chauffage n'est pas constant : il est proportionnel à l'écart entre la température intérieure et la température extérieure, faible en automne et au printemps, élevé lors des jours les plus froids. L'installation doit être dimensionnée pour **la pointe** (vague de froid, remise en température après une absence), et non pour la moyenne, sans quoi la température de consigne ne serait pas tenue ces jours-là. En contrepartie, la machine ne fonctionne à pleine puissance qu'une petite partie du temps : fournir 7000 kWh à 7 kW ne demande que 1000 heures, soit moins du quart de la saison de chauffe. Le reste du temps, elle fonctionne par intermittence ou à puissance réduite. Un surdimensionnement excessif serait inutile et coûteux (machine et circuit capteur plus grands).

### Question 3.5.a — Diagramme de Clapeyron et isothermes

Dans le diagramme de Clapeyron (pression $P$ en ordonnée, volume massique $v$ en abscisse), on trace d'abord la **courbe de saturation** : courbe d'ébullition à gauche, courbe de rosée à droite, qui se rejoignent au **point critique C** (86,1 °C ; 46,3 bar). Le liquide est à gauche, la vapeur sèche à droite, le mélange liquide-vapeur sous la courbe.

Les trois températures (5 °C, 60 °C, 70 °C) sont **inférieures à la température critique** : chaque isotherme présente donc trois portions.

- Dans le domaine liquide, une branche presque verticale (le liquide est très peu compressible).
- Sous la courbe de saturation, un **palier horizontal** à la pression de vapeur saturante : 6 bar pour 5 °C, 27 bar pour 60 °C (tableau), et une pression plus élevée, comprise entre 27 bar et 46,3 bar, pour 70 °C (le tableau ne la donne pas).
- Dans le domaine vapeur, une branche décroissante, d'allure hyperbolique.

Les isothermes ne se coupent pas ; plus la température est élevée, plus l'isotherme est haute et plus son palier est court. L'isotherme 70 °C passe, dans le domaine vapeur, par le point de pression 27 bar : c'est l'état (2).

![Figure 2 — Allure du diagramme de Clapeyron du R407C : courbe de saturation, isothermes 5 °C, 60 °C et 70 °C, et cycle 1-2-3-4 de la pompe à chaleur](figures/clapeyron-r407c-cycle.svg)

### Question 3.5.b — Titre en vapeur de l'état (4)

L'état (3) est du liquide saturant à 27 bar : $h_3 = 295\ \mathrm{kJ\cdot kg^{-1}}$ (tableau, ligne 60 °C). La détente est isenthalpique : $h_4 = h_3$.

L'état (4) est un mélange diphasé à 6 bar et 5 °C, de titre massique en vapeur $x_4$. L'enthalpie étant extensive,

$$h_4 = x_4\,h_V + (1-x_4)\,h_L$$

avec $h_L = 210\ \mathrm{kJ\cdot kg^{-1}}$ et $h_V = 410\ \mathrm{kJ\cdot kg^{-1}}$ (tableau, ligne 5 °C). D'où

$$\boxed{x_4 = \frac{h_3 - h_L}{h_V - h_L} = \frac{295-210}{410-210} = \frac{85}{200} \approx 0{,}43}$$

Environ 43 % de la masse du fluide est déjà vaporisée à la sortie du détendeur.

### Question 3.5.c — Tracé du cycle

On place les quatre états sur le diagramme de la figure 2.

- **(1)** : vapeur saturante à 6 bar, sur la courbe de rosée, à l'extrémité droite du palier 5 °C.
- **(2)** : vapeur sèche à 27 bar et 70 °C, sur l'isobare 27 bar, à droite de la courbe de rosée, à l'intersection avec l'isotherme 70 °C.
- **(3)** : liquide saturant à 27 bar, sur la courbe d'ébullition, à l'extrémité gauche du palier 60 °C.
- **(4)** : mélange diphasé à 6 bar, sur le palier 5 °C, à la fraction $x_4 = 0{,}43$ du palier comptée depuis la courbe d'ébullition (théorème des moments).

Les transformations sont : 1 → 2 compression adiabatique (courbe montante vers les petits volumes, plus raide que les isothermes) ; 2 → 3 refroidissement de la vapeur puis liquéfaction, sur l'horizontale 27 bar ; 3 → 4 détente isenthalpique (irréversible, tracée en tirets) ; 4 → 1 vaporisation sur l'horizontale 6 bar.

**Le cycle 1-2-3-4 est parcouru dans le sens trigonométrique** : c'est un cycle récepteur ($W > 0$), comme il se doit pour une pompe à chaleur.

### Question 3.6 — Transferts thermiques et travail massiques

*Cadre.* Chaque organe est un système ouvert traversé par le fluide en écoulement stationnaire ; on néglige les variations d'énergie cinétique et d'énergie potentielle. Le premier principe s'écrit, pour l'unité de masse de fluide qui traverse l'organe,

$$\Delta h = w_i + q$$

où $w_i$ est le travail indiqué massique (reçu des pièces mobiles) et $q$ le transfert thermique massique reçu.

*Enthalpies massiques (tableau de l'énoncé).* $h_1 = 410\ \mathrm{kJ\cdot kg^{-1}}$ (vapeur saturante à 6 bar), $h_2 = 435\ \mathrm{kJ\cdot kg^{-1}}$ (vapeur à 70 °C et 27 bar), $h_3 = 295\ \mathrm{kJ\cdot kg^{-1}}$ (liquide saturant à 27 bar), $h_4 = h_3$.

*Source chaude (condenseur, 2 → 3).* Pas de pièce mobile, $w_i = 0$ :

$$\boxed{q_c = h_3 - h_2 = 295 - 435 = -140\ \mathrm{kJ\cdot kg^{-1}}}$$

Le fluide cède 140 kJ par kilogramme à l'eau du circuit de chauffage.

*Compresseur (1 → 2).* Compression adiabatique, $q = 0$ :

$$\boxed{w_i = h_2 - h_1 = 435 - 410 = 25\ \mathrm{kJ\cdot kg^{-1}}}$$

*Source froide (évaporateur, 4 → 1).* L'enthalpie est une fonction d'état : sur un cycle, $\Delta h_{\text{cycle}} = 0$. Le détendeur n'échange ni travail ni chaleur (détente isenthalpique). La somme des bilans sur les quatre organes donne

$$w_i + q_c + q_f = 0$$

$$\boxed{q_f = -q_c - w_i = 140 - 25 = 115\ \mathrm{kJ\cdot kg^{-1}}}$$

Vérification directe : $q_f = h_1 - h_4 = 410 - 295 = 115\ \mathrm{kJ\cdot kg^{-1}}$. Le fluide prélève 115 kJ par kilogramme à l'eau glycolée du circuit capteur.

### Question 3.7.a — Efficacité et efficacité de Carnot

*Efficacité.* La grandeur utile est la chaleur cédée à la source chaude, la grandeur coûteuse est le travail fourni au fluide :

$$\boxed{e = \frac{-q_c}{w_i} = \frac{140}{25} = 5{,}6}$$

*Efficacité de Carnot.* Pour un cycle ditherme, le premier principe donne $W + Q_c + Q_f = 0$ et le second $\dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} \leqslant 0$, avec égalité pour un cycle réversible. On en tire $W \geqslant -Q_c\,(1 - T_f/T_c)$, soit $e \leqslant e_C$ avec

$$\boxed{e_C = \frac{T_c}{T_c - T_f}}$$

Avec $T_c = 60\ \mathrm{°C} = 333$ K et $T_f = 5\ \mathrm{°C} = 278$ K : $e_C = 333/55 \approx 6{,}1$, valeur donnée par l'énoncé.

*Comparaison.* On a bien $e = 5{,}6 < e_C = 6{,}1$, conformément au second principe : l'efficacité de Carnot est une borne supérieure, atteinte seulement par un cycle réversible. Le cycle étudié ne l'est pas : la détente isenthalpique dans le détendeur est irréversible, et la vapeur surchauffée à 70 °C se refroidit au contact d'une source plus froide. L'écart reste faible ($e/e_C \approx 0{,}92$) parce que le modèle est idéalisé : dans une machine réelle, il faut des écarts de température entre le fluide et les sources dans les échangeurs et la compression est irréversible, de sorte que l'efficacité est nettement plus basse (typiquement 3 à 4).

### Question 3.7.b — Puissance électrique du compresseur

L'efficacité est aussi un rapport de puissances : la puissance mécanique que le compresseur doit transmettre au fluide pour fournir $P_{\text{th}} = 7000$ W au circuit de chauffage est

$$P_{\text{méca}} = \frac{P_{\text{th}}}{e} = \frac{7000}{5{,}6} = 1250\ \mathrm{W}$$

Le rendement électromécanique $\eta = 0{,}75$ est le rapport de cette puissance à la puissance électrique consommée :

$$\boxed{P_{\text{élec}} = \frac{P_{\text{th}}}{\eta\,e} = \frac{7000}{0{,}75\times 5{,}6} = \frac{7000}{4{,}2} \approx 1{,}7\ \mathrm{kW}}$$

Le compresseur consomme environ 1,7 kW électrique pour 7 kW thermiques fournis : l'efficacité globale, pertes du moteur comprises, vaut $\eta\,e = 4{,}2$. Le débit massique de R407C correspondant est $D_m = P_{\text{th}}/|q_c| = 7000/(140\times 10^{3}) = 0{,}05\ \mathrm{kg\cdot s^{-1}}$.

### Question 3.7.c — Consommation électrique annuelle

Le logement a toujours besoin de $E = 7000$ kWh de chaleur par an. Avec le chauffage électrique, toute cette énergie était électrique. Avec la pompe à chaleur, efficacité et rendement étant supposés constants, le rapport de la question 3.7.b s'applique aux énergies :

$$\boxed{E_{\text{élec}} = \frac{E}{\eta\,e} = \frac{7000}{4{,}2} \approx 1{,}7\times 10^{3}\ \mathrm{kWh}}$$

La consommation électrique annuelle est divisée par 4,2. La différence, environ 5300 kWh, est prélevée dans le sol (et, pour une faible part, perdue dans le moteur).

### Question 3.7.d — Gain annuel

L'énergie électrique économisée chaque année est $E - E_{\text{élec}} = 7000 - 1667 \approx 5{,}3\times 10^{3}$ kWh. Au prix de 0,15 euro le kilowattheure :

$$\boxed{G = (E - E_{\text{élec}})\times 0{,}15 \approx 5{,}3\times 10^{3}\times 0{,}15 \approx 8\times 10^{2}\ \text{euros par an}}$$

La facture de chauffage passe de $7000\times 0{,}15 = 1050$ euros à environ 250 euros par an.

*Commentaire.* L'ordre de grandeur est raisonnable : quelques centaines d'euros par an. Il faut le comparer au coût de l'installation (pompe à chaleur, terrassement et pose de 400 m de tuyaux enterrés), de l'ordre de dix mille euros ou davantage : le temps de retour sur investissement dépasse la dizaine d'années au prix actuel du kilowattheure. Le gain augmente si ce prix monte, ce que l'énoncé envisage. Le calcul est par ailleurs optimiste : il suppose une efficacité de 5,6 en toutes circonstances et ignore la consommation des pompes de circulation et l'entretien. L'intérêt n'est pas seulement financier : les trois quarts de la chaleur fournie au logement proviennent du sol, source gratuite et renouvelable.
