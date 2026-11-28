# X-ENS PC 2025 — Physique B · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

**Révision (tour 2)** · modèle exact non renseigné (famille Claude) · effort non renseigné · vitesse non renseignée · 28 novembre 2026

**Production et caractérisation d’impulsions laser attosecondes.** La notation $q^2=e^2/(4\pi\varepsilon_0)$ des questions atomiques désigne une constante coulombienne. Dans les questions spectrales, $q$ désigne le rang entier d’une harmonique.

Le rapport du jury insiste sur le tracé des asymptotes, la justification quantitative des approximations optiques et la distinction entre parité temporelle et sélection des ordres harmoniques.

## Échelles atomiques et focalisation

### Question 1 — Temps de révolution de Bohr

> [!INDICATION]
> Associer équilibre radial et quantification du moment cinétique.

#### Solution

Le mouvement circulaire vérifie $mv^2/r=q^2/r^2$, et l'état fondamental de Bohr impose $mvr=\hbar$. On obtient $v=q^2/\hbar$ et $r=\hbar^2/(mq^2)$. Ainsi $T_e=2\pi r/v=2\pi\hbar^3/[m(q^2)^2]$, en accord avec la valeur fournie $1{,}5\times10^{-16}\ \mathrm s$.

### Question 2 — Domaine spectral

> [!INDICATION]
> Comparer aux limites du spectre visible.

#### Solution

La longueur d'onde $800\ \mathrm{nm}=0{,}8\ \mu\mathrm m$ se situe dans le proche infrarouge, immédiatement au-delà du rouge visible.

### Question 3 — Période et premier ordre assez rapide

> [!INDICATION]
> Effectuer la comparaison avant d’arrondir le rapport des périodes.

#### Solution

$T=\lambda/c=2{,}67\times10^{-15}\ \mathrm s$, soit environ $3\ \mathrm{fs}$ à un chiffre significatif. Il faut $T/n<T_e$, soit $n>17{,}8$ en gardant les chiffres intermédiaires. Le plus petit entier est **18**. Si seules les harmoniques impaires sont émises, comme on l'établira, le premier ordre présent satisfaisant cette condition est 19.

> [!JURY]
> Le rapport relève des périodes de l'ordre de $10^{+17}$ : $8\times10^{-7}$ divisé par $3\times10^{8}$ donne quelques $10^{-15}\ \mathrm s$. Une période optique vaut quelques femtosecondes ; tout autre ordre de grandeur doit alerter.

### Question 4 — Longueur de Rayleigh

> [!INDICATION]
> Calculer le petit paramètre sans dimension $z/z_R$.

#### Solution

$z_R=\pi w_0^2/\lambda=\pi(4\times10^{-3})^2/(8\times10^{-7})\simeq63\ \mathrm m$, soit $6\times10^{1}\ \mathrm m$ à un chiffre significatif. Pour $|z|\le1\ \mathrm m$, $w/w_0=\sqrt{1+(z/z_R)^2}\simeq1+z^2/(2z_R^2)$. La variation relative du rayon est au plus $1{,}3\times10^{-4}$ environ, soit $1\times10^{-4}$ à un chiffre. Le faisceau peut être considéré comme cylindrique sur cette longueur.

### Question 5 — Conditions de Gauss

> [!INDICATION]
> Chiffrer l’ouverture angulaire en amont et en aval.

#### Solution

Le faisceau est centré sur l'axe de la lentille et sa divergence incidente vaut $\lambda/(\pi w_0)\simeq6\times10^{-5}\ \mathrm{rad}$. Après la lentille, un rayon typique situé à $w_0$ de l'axe est dévié de $w_0/f=4\times10^{-3}\ \mathrm{rad}\ll1$. Les rayons qui portent l'essentiel de l'énergie restent paraxiaux.

> [!JURY]
> Énoncer les conditions de Gauss ne suffit pas, il faut vérifier qu'elles sont satisfaites. « Petit » doit être comparé à quelque chose : ici $w_0=4\ \mathrm{mm}\ll f=1\ \mathrm m$, donc des angles de $4\times10^{-3}\ \mathrm{rad}$. Dire que le faisceau est centré sur l'axe ne prouve rien à lui seul.

### Question 6 — Waist du faisceau focalisé

> [!INDICATION]
> Apparier l’angle de la géométrie de focalisation et l’angle d’un faisceau gaussien loin du waist.

#### Solution

Le faisceau converge vers un nouveau waist voisin du foyer, puis diverge. Pour $f\ll z_R$, l'angle de convergence $w_0/f$ est la divergence du nouveau faisceau $\lambda/(\pi w'_0)$. D'où $w'_0\simeq\lambda f/(\pi w_0)\simeq6\times10^{-5}\ \mathrm m$. La nouvelle longueur de Rayleigh est de l'ordre de $1{,}6\ \mathrm{cm}$.

![Figure 1 — Le col du faisceau émergent est proche du foyer. Les ouvertures et le rayon du col sont exagérés.](figures/focalisation.svg)

### Question 7 — Puissance surfacique au foyer

> [!INDICATION]
> Utiliser le rayon focalisé et convertir les femtosecondes en secondes.

#### Solution

La puissance de l'impulsion est de l'ordre de $E_L/T_L=2{,}5\times10^{10}\ \mathrm W$. Sur l'aire $\pi w_0'^2$ elle donne $P_L\sim E_L/(T_L\pi w_0'^2)\simeq2\times10^{18}\ \mathrm{W\,m^{-2}}$. Un calcul strictement axial du maximum pour le profil spatial gaussien introduit un facteur 2, et la forme temporelle intervient aussi quant au maximum exact.

> [!PIEGE]
> La surface à utiliser est celle du faisceau au foyer, $\pi w_0'^2$, pas celle du faisceau incident $\pi w_0^2$ : l'écart est un facteur $(w_0/w_0')^2\simeq4\times10^{3}$. Le résultat est une puissance surfacique, en $\mathrm{W\,m^{-2}}$ ; le jury a trouvé des réponses en watts.

### Question 8 — Amplitude du champ

> [!INDICATION]
> Utiliser le vecteur de Poynting et sa moyenne sur la période optique.

#### Solution

Pour une onde localement plane, $B=E/c$ et $\langle\Pi\rangle=E_0^2/(2\mu_0 c)$ pour une amplitude crête sinusoïdale. Ainsi $E_0\sim\sqrt{2\mu_0 c P_L}$, à un facteur d'ordre un selon la convention de moyenne du profil.

### Question 9 — Comparaison solaire

> [!INDICATION]
> Prendre la racine du rapport des flux avant de l’appliquer au champ.

#### Solution

Le flux solaire au sommet de l'atmosphère est de l'ordre de $10^3\ \mathrm{W\,m^{-2}}$ ($1{,}4\ \mathrm{kW\,m^{-2}}$ plus précisément). Le flux variant comme le carré de l'amplitude, $E_0\sim700\sqrt{P_L/(10^3\ \mathrm{W\,m^{-2}})}\sim3\times10^{10}\ \mathrm{V\,m^{-1}}$. L'expression de la question 8 donne $4\times10^{10}\ \mathrm{V\,m^{-1}}$ : l'écart vient de ce qu'une amplitude de $700\ \mathrm{V\,m^{-1}}$ correspond, par cette même formule, à $650\ \mathrm{W\,m^{-2}}$ et non à $10^3$. Les deux estimations s'accordent sur l'ordre de grandeur, quelques $10^{10}\ \mathrm{V\,m^{-1}}$.

> [!JURY]
> Le flux solaire reçu par la Terre hors atmosphère, de l'ordre de $1{,}4\ \mathrm{kW\,m^{-2}}$, relève du programme ; le rapport note que très peu de candidats en donnent l'ordre de grandeur. Il n'y a aucun waist à attribuer au Soleil : seul le rapport des flux surfaciques intervient.

### Question 10 — Champ atomique

> [!INDICATION]
> Convertir une énergie par charge en tension.

#### Solution

Une taille atomique vaut approximativement $a\sim10^{-10}\ \mathrm m$. Une énergie d'ionisation de $10\ \mathrm{eV}$ équivaut au travail d'un champ de l'ordre de $I_P/(ea)\sim10^{11}\ \mathrm{V\,m^{-1}}$ sur cette distance. Le champ focalisé et le champ atomique sont comparables à un facteur de quelques unités près. Cela rend plausible une déformation importante du potentiel.

## Ionisation et recombinaison

### Question 11 — Potentiel coulombien incliné

> [!INDICATION]
> Pour obtenir le terme nucléaire, conserver la distance positive au noyau.

#### Solution

Le potentiel électrostatique du laser, dont le champ pointe vers $-x$, vaut $E_0x$ à une constante près. Pour l'électron,
$$V(x)=-\frac{q^2}{|x|}-eE_0x.$$
Il tend vers $-\infty$ des deux côtés de l'origine. À grande distance son asymptote oblique est $-eE_0x$, donc il monte vers $+\infty$ à gauche et descend vers $-\infty$ à droite. À droite un maximum sépare le puits coulombien de la région d'échappement.

![Figure 2 — Le potentiel diverge vers le bas des deux côtés du noyau. À droite, le niveau lié figuré rencontre une barrière avant la région d’échappement.](figures/barriere.svg)

> [!JURY]
> Le jury dit avoir été « extrêmement surpris » par les difficultés de tracé : la courbe est la somme d'un terme en $-1/|x|$ et d'un terme linéaire. Faire figurer l'asymptote verticale en $x=0$ (les deux branches plongent), l'asymptote oblique $-eE_0x$, le maximum local à droite, et orienter les axes. Sans barrière à droite, la réponse « effet tunnel » de la question 13 n'a plus de support.

### Question 12 — Disparition classique de la barrière

> [!INDICATION]
> Comparer le niveau à la valeur du potentiel au maximum de droite.

#### Solution

Pour $x>0$, $V'(x)=q^2/x^2-eE_0$. Le sommet est en $x_s=\sqrt{q^2/(eE_0)}$ et $V(x_s)=-2\sqrt{q^2eE_0}$. L'électron d'énergie $-I_P$ passe classiquement au-dessus de la barrière si $-I_P>V(x_s)$, soit $E_0>E_{\rm sat}=I_P^2/(4e q^2)$. L'égalité est le cas limite où l'énergie coïncide avec le sommet.

### Question 13 — Échappement sous le seuil

> [!INDICATION]
> Une région classiquement interdite peut être traversée avec une probabilité non nulle.

#### Solution

L'effet tunnel permet à une fonction d'onde d'avoir une amplitude transmise au-delà d'une barrière de largeur finie, même si l'énergie est inférieure à son sommet.

### Question 14 — Équation de Newton

> [!INDICATION]
> Vérifier le sens du terme nucléaire de chaque côté.

#### Solution

Le champ du laser donne une force $+eE_0\sin\omega t$ et l'attraction nucléaire ramène vers zéro. Pour $x>0$, $m\ddot x=-q^2/x^2+eE_0\sin\omega t$. Pour $x<0$, $m\ddot x=+q^2/x^2+eE_0\sin\omega t$. La singularité ponctuelle en zéro signale la limite du modèle classique.

> [!JURY]
> Le rapport regrette que trop de copies ne confrontent pas ces équations au potentiel de la question 11. Le contrôle tient en une ligne : la force totale doit valoir $-\mathrm dV/\mathrm dx$ de chaque côté du noyau.

### Question 15 — Symétrie de demi-période

> [!INDICATION]
> Appliquer ensemble réflexion spatiale et translation temporelle avant d’identifier la réponse forcée.

#### Solution

Notons $F_C(x)$ la force coulombienne impaire. Puisque $F_C(-x)=-F_C(x)$ et $\sin[\omega(t+T/2)]=-\sin\omega t$, la fonction $y(t)=-x(t+T/2)$ satisfait la même équation que $x$. La solution forcée sélectionnée qui respecte la symétrie de l'atome et du champ doit donc vérifier $x(t+T/2)=-x(t)$. L'invariance seule relie deux solutions possibles. L'identification suppose cette réponse symétrique ou l'unicité de la réponse périodique retenue, ce que le modèle non linéaire sans dissipation ne démontre pas en général.

### Question 16 — Harmoniques permises

> [!INDICATION]
> Calculer le facteur acquis par chaque coefficient de Fourier.

#### Solution

La composante complexe $c_ne^{in\omega t}$ est multipliée par $(-1)^n$ après une demi-période. La condition $(-1)^nc_n=-c_n$ annule le terme continu et tous les coefficients pairs. Il reste les rangs impairs, quelle que soit la parité ordinaire du signal autour de $t=0$.

> [!PIEGE]
> Ne pas confondre parité de la fonction et parité du rang des harmoniques, confusion que le rapport signale. Une fonction impaire peut contenir des harmoniques paires ($\sin2\omega t$). C'est l'antisymétrie de demi-période $x(t+T/2)=-x(t)$ qui supprime les rangs pairs.

### Question 17 — Mouvement libéré du noyau

> [!INDICATION]
> La solution générale contient les deux solutions homogènes indépendantes.

#### Solution

Posons $a_0=eE_0/m$ et $x_0=a_0/\omega^2$. De $\ddot x=a_0\sin\omega t$ on tire $\dot x=-(a_0/\omega)\cos\omega t+v_d$ puis $x=-x_0\sin\omega t+v_dt+x_c$. Les deux constantes fixent la dérive et l'origine de position.

> [!JURY]
> Erreur fréquente selon le rapport : se contenter d'une primitive du second membre. La solution générale d'une équation du second ordre porte deux constantes, ici la vitesse de dérive $v_d$ et la position $x_c$.

### Question 18 — Énergie pondéromotrice

> [!INDICATION]
> Faire la moyenne du carré de la vitesse, après avoir annulé la dérive.

#### Solution

La périodicité du mouvement impose $v_d=0$. Avec $\langle\cos^2\omega t\rangle=1/2$, l'énergie cinétique moyenne est $U_P=e^2E_0^2/(4m\omega^2)$.

### Question 19 — Départ sans vitesse

> [!INDICATION]
> Évaluer les deux primitives au même instant d’émission.

#### Solution

Avec $u=\omega t$ et $u_i=\omega t_i$, les conditions $x(t_i)=\dot x(t_i)=0$ donnent
$$\dot x=\frac{a_0}{\omega}(\cos u_i-\cos u),\qquad \frac{x}{x_0}=(u-u_i)\cos u_i-\sin u+\sin u_i.$$
Les deux conditions initiales se retrouvent en remplaçant $u$ par $u_i$.

### Question 20 — Trois trajectoires imposées

> [!INDICATION]
> Reporter les trois valeurs de la phase initiale dans la même formule.

#### Solution

Pour $t_i=0$, $x/x_0=u-\sin u$ croît, avec tangente horizontale à chaque période entière. Pour $t_i=T/4$, $x/x_0=1-\sin u$ oscille entre 0 et 2 et retrouve zéro à $5T/4$. Pour $t_i=T/2$, $x/x_0=-(u-\pi)-\sin u$ décroît. Chaque courbe commence à son propre instant $t_i$, où la vitesse s'annule.

![Figure 3 — Trajectoires pour les trois phases imposées à la question 20. Chaque trace commence quand l’électron quitte l’origine avec une vitesse nulle.](figures/trois-departs.svg)

> [!JURY]
> Il ne fallait pas recopier la figure 1. Les trois courbes demandées sont distinctes : chacune part de son propre $t_i/T$ (0 ; 0,25 ; 0,5), avec une tangente horizontale, et va jusqu'à $t/T=1{,}5$.

### Question 21 — Premier retour

> [!INDICATION]
> Chercher le premier zéro strictement après l’émission.

#### Solution

Pour $u_r=\omega t_r>u_i$ le premier retour non trivial satisfait $(u_r-u_i)\cos u_i-\sin u_r+\sin u_i=0$. La solution évidente $u_r=u_i$ représente l'instant de départ et doit être écartée.

### Question 22 — Photon de recombinaison

> [!INDICATION]
> Un photon emporte la totalité de l’énergie disponible dans le modèle proposé.

#### Solution

La libération d'une énergie $I_P+E_c(t_r)$ correspond à un photon de pulsation $\omega_\gamma=[I_P+E_c(t_r)]/\hbar$. Le terme $I_P$ vient du retour à l'état lié.

### Question 23 — Lecture de la figure 1

> [!INDICATION]
> Comparer les tangentes au dernier point de chaque trajectoire tracée.

#### Solution

L'énergie au retour dépend du carré de la pente $dx/dt$ au passage par zéro. Des quatre courbes, le trait plein $t_i=0{,}30T$ a la plus grande pente en valeur absolue. La courbe pointillée $t_i=0{,}40T$ a la plus faible. La hauteur maximale de la trajectoire n'est pas le critère de comparaison.

### Question 24 — Énergie au retour

> [!INDICATION]
> Exprimer le préfacteur avec $U_P$.

#### Solution

En reprenant la vitesse de la question 19, $E_c(t_r)=m\dot x(t_r)^2/2=2U_P[\cos(\omega t_i)-\cos(\omega t_r)]^2$.

### Question 25 — Courbe paramétrée des retours

> [!INDICATION]
> Identifier la branche et l’ordre des temps de retour en retrouvant les intersections de la figure 1.

#### Solution

La courbe s'obtient en faisant varier $t_i$, en résolvant la question 21 pour le premier retour puis en évaluant la question 24. Dans l'ordre croissant de $t_r/T$, les triplets $(t_i/T,t_r/T,E_c/U_P)$ sont approximativement $(0{,}40;0{,}704;0{,}55)$, $(0{,}35;0{,}817;1{,}97)$, $(0{,}30;0{,}950;3{,}17)$ et $(0{,}26;1{,}115;1{,}32)$. Quand $t_i/T$ passe de $1/2$ vers $1/4$, le premier retour se déplace du voisinage de $T/2$ à $5T/4$. Les deux extrémités ont une énergie limite nulle.

![Figure 4 — Les étiquettes donnent la fraction de période à l’ionisation. Le sommet proche de 3,17 fixe l’énergie cinétique maximale disponible au retour.](figures/retours.svg)

### Question 26 — Peigne et coupure

> [!INDICATION]
> Relier la fin du plateau au maximum d’énergie de recombinaison.

#### Solution

Les pics sont espacés de deux fréquences laser, aux ordres impairs : c'est la sélection établie à la question 16, le rayonnement suivant le mouvement de l'électron. Après la décroissance initiale, une série de pics d'ordres supérieurs forme un plateau approximatif, suivi d'une coupure rapide vers les rangs 29 à 33 sur cette mesure. Les ordres 19 et supérieurs satisfont la condition de la question 3. Le plus grand photon possible correspond au maximum du graphe de retour, $E_{c,\max}\simeq3{,}17U_P$. La loi de coupure est donc $n_{\max}\simeq(I_P+3{,}17U_P)/(\hbar\omega)$, avec les pics effectivement permis situés aux entiers impairs.

## Durée et phases des impulsions

### Question 27 — Puissance d’une superposition

> [!INDICATION]
> Développer exactement le produit du signal analytique par son conjugué.

#### Solution

Pour le signal complexe $A(t)=\sum_q A_qe^{i(q\omega t+\phi_q)}$, la puissance d'enveloppe est proportionnelle à
$$|A(t)|^2=\sum_q A_q^2+2\sum_{q<q'}A_qA_{q'}\cos[(q'-q)\omega t+\phi_{q'}-\phi_q].$$
Le produit avec le conjugué élimine toute phase commune. Cette intensité est l'enveloppe optique mesurée après élimination des oscillations de porteuse aux fréquences sommes.

> [!JURY]
> Le produit $AA^\star=|A|^2$ est réel : en prendre la partie réelle, $\mathrm{Re}(AA^\star)$, est inutile, et le rapport invite les candidats à s'en apercevoir.

### Question 28 — Pics de N harmoniques successives

> [!INDICATION]
> Isoler l’enveloppe d’interférence à partir de la somme géométrique.

#### Solution

Pour des amplitudes $A$ et phases identiques, la série géométrique donne $I(t)\propto A^2[\sin(N\omega t/2)/\sin(\omega t/2)]^2$. La valeur limite est $N^2 A^2$ aux instants $t=kT$. De part et d'autre, les premiers zéros sont à $kT\pm T/N$. La demi-largeur jusqu'au premier zéro vaut donc $T/N$. Si « demi-largeur » désigne celle à mi-hauteur, $[\sin x/x]^2=1/2$ donne $x\simeq1{,}392$, donc une demi-largeur $0{,}443T/N$ pour $N\gg1$. Les pics sont séparés de $T$. C'est la fonction d'interférences à $N$ ondes d'un réseau, le temps jouant le rôle de l'angle.

![Figure 5 — À phases alignées, dix ordres successifs donnent un pic par période laser (question 28) ; cinq ordres impairs en donnent deux (question 35). Amplitudes identiques dans les deux cas.](figures/peignes.svg)

> [!JURY]
> C'est le calcul de l'intensité derrière un réseau à $N$ fentes, explicitement au programme : même somme géométrique, même fonction $[\sin(N\varphi/2)/\sin(\varphi/2)]^2$. Le rapport s'étonne que de très rares candidats aient fait le rapprochement.

### Question 29 — Phases en progression arithmétique

> [!INDICATION]
> Identifier le coefficient de $q$ dans la phase totale.

#### Solution

Pour $\phi_q=\phi_n+(q-n)\delta$, le terme de rang $q$ contient $q(\omega t+\delta)$ plus une phase commune. L'intensité de la question 28 devient $I_0(t+\delta/\omega)$. Les pics sont donc décalés de $-\delta/\omega$, modulo $T$, sans changement de forme.

### Question 30 — Énergie d’un photon harmonique

> [!INDICATION]
> Distinguer énergie du photon et énergie cinétique de l’électron.

#### Solution

$E_q=\hbar q\omega=qh\nu$. Une absorption qui ionise l'atome laisse à l'électron une énergie cinétique $q\hbar\omega-I_P$ en négligeant le recul.

### Question 31 — Deux amplitudes à la même énergie

> [!INDICATION]
> Associer les fréquences positives et négatives de la sonde aux deux harmoniques voisines.

#### Solution

En décomposant les cosinus en exponentielles, le produit contient à la fréquence $(q+1)\omega$ le terme
$$\frac14e^{i(q+1)\omega t}\left[e^{i(\phi_q+\omega\tau)}+e^{i(\phi_{q+2}-\omega\tau)}\right].$$
Le premier chemin absorbe un photon harmonique $q$ et un photon sonde. Le second absorbe un photon $q+2$ et émet un photon sonde. Les deux donnent le même état final d'énergie cinétique $(q+1)\hbar\omega-I_P$.

### Question 32 — Interférence à deux photons

> [!INDICATION]
> Calculer le terme croisé et chercher sa période en retard.

#### Solution

Le carré du module vaut à une constante près $P(\tau)\propto1+\cos[2\omega\tau-(\phi_{q+2}-\phi_q)]$. La probabilité oscille entre zéro et le double de sa moyenne pour les amplitudes égales admises. Deux maxima consécutifs sont séparés par $\pi/\omega=T/2$. Les alternatives quantiques indiscernables s'ajoutent en amplitude avant le calcul de la probabilité.

![Figure 6 — Dans chaque bande latérale, le signal oscille à la fréquence double. Un écart de phase entre deux harmoniques déplace les maxima en retard.](figures/battements.svg)

### Question 33 — Lecture de la carte RABITT

> [!INDICATION]
> Comparer sur la figure 4 une ligne continue et une ligne de points clairs.

#### Solution

Les lignes impaires 17 à 23 sont brillantes et pratiquement indépendantes du retard ; la ligne 25, plus faible, laisse voir une légère modulation. Elles correspondent aux photons harmoniques absorbés directement, seuls présents sur la figure 3. Les bandes intermédiaires paires proviennent des deux transitions de la question 31. Leurs maxima se répètent environ tous les $1{,}3\ \mathrm{fs}$, soit environ 22 à 23 oscillations sur la trentaine de femtosecondes représentée. On retrouve $T\simeq2{,}6$ à $2{,}7\ \mathrm{fs}$, compatible avec $800\ \mathrm{nm}$.

### Question 34 — Test de l’alignement des phases

> [!INDICATION]
> Garder le retard sur l’axe horizontal et comparer les bandes paires.

#### Solution

Pour le canal intermédiaire, le maximum est à $2\omega\tau=\phi_{q+2}-\phi_q\pmod{2\pi}$. Si la différence est indépendante de $q$, les maxima des différentes bandes paires doivent s'aligner verticalement à la même abscisse de retard, à un multiple de $T/2$ près. Un glissement systématique entre bandes signe une différence de phase dépendant du rang.

### Question 35 — Durée d’une impulsion

> [!INDICATION]
> L’écart entre les harmoniques présentes vaut deux fois la pulsation laser.

#### Solution

Les ordres visibles 17, 19, 21, 23 et 25 constituent environ $N=5$ harmoniques impaires séparées de $2\omega$. Si leurs phases ont un incrément constant et que leurs amplitudes sont comparables, les pics se répètent toutes les $T/2$. En remplaçant $T$ par $T/2$ dans la question 28, la demi-largeur jusqu'au premier zéro vaut $T/(2N)\simeq0{,}27\ \mathrm{fs}$. La largeur totale à mi-hauteur est d'environ $0{,}886\,T/(2N)\simeq0{,}24\ \mathrm{fs}$, soit **quelques centaines d'attosecondes** (à un chiffre significatif, $3\times10^{-16}\ \mathrm s$ jusqu'au premier zéro et $2\times10^{-16}\ \mathrm s$ à mi-hauteur). Les amplitudes réelles et la bande effectivement transmise modifient le chiffre précis.

## Spectromètre magnétique

### Question 36 — Rayon cyclotron

> [!INDICATION]
> Évaluer la norme de la force, le signe de la charge fixe seulement le sens de rotation.

#### Solution

Dans un champ uniforme transverse, la force magnétique est perpendiculaire à la vitesse. Elle conserve donc $v_\perp$ et joue le rôle de force centripète. $ev_\perp B=mv_\perp^2/r$ donne $r=mv_\perp/(eB)$.

### Question 37 — Moment cinétique de giration

> [!INDICATION]
> Éliminer $v_\perp$ à l’aide du rayon cyclotron.

#### Solution

Au centre du cercle, le rayon et la quantité de mouvement sont perpendiculaires, donc $J=mrv_\perp=eBr^2$. Ce $J$ décrit la giration autour du centre instantané.

### Question 38 — Hélice

> [!INDICATION]
> Décomposer la vitesse selon et perpendiculairement au champ.

#### Solution

La composante $v_\parallel=v\cos\theta$ est uniforme, tandis que $v_\perp=v\sin\theta$ détermine la giration. Le rayon est $r=mv\sin\theta/(eB)$. Il tend vers zéro pour une entrée parallèle au champ et vers le résultat circulaire pour une entrée perpendiculaire.

> [!METHODE]
> Reprendre la question 36 avec $v_\perp=v\sin\theta$, puis contrôler les limites : $\theta\to0$ donne $r\to0$ (pas de giration), $\theta=\pi/2$ redonne le cercle. Le rapport indique que ce contrôle aurait aidé à critiquer les résultats proposés.

### Question 39 — Variation axiale du champ

> [!INDICATION]
> Suivre l’écartement de deux lignes voisines pour juger de l’intensité.

#### Solution

Sur la figure 5, un même tube de lignes s'élargit de l'entrée à la sortie puis devient pratiquement cylindrique. La conservation du flux magnétique implique que la norme de $B$ diminue le long du tube puis se stabilise vers $B_f<B_i$ dans la partie droite.

### Question 40 — Redressement des trajectoires

> [!INDICATION]
> Conserver à la fois l’énergie cinétique totale et le moment de giration.

#### Solution

La force magnétique ne travaille pas, donc $v$ est constant. L'invariant admis vaut $J=eBr^2=m^2v^2\sin^2\theta/(eB)$. Il en résulte
$$\sin^2\theta_f=(B_f/B_i)\sin^2\theta_i.$$
Lorsque le champ décroît, le mouvement se rapproche de la direction de la ligne de champ. Le cercle de giration s'élargit pourtant : $J=eBr^2$ constant donne $r_f=r_i\sqrt{B_i/B_f}$.

### Question 41 — Incertitude due à l’angle final

> [!INDICATION]
> L’appareil mesure directement la composante axiale de vitesse dans le tube long.

#### Solution

Dans la longue portion uniforme, $\Delta t\simeq L/(v\cos\theta_f)$. Estimer $v$ par $L/\Delta t$ donne $v_{\rm mes}=v\cos\theta_f$, donc un biais par défaut. En valeur relative par rapport à la vitesse vraie,
$$\frac{v-v_{\rm mes}}{v}=1-\sqrt{1-(B_f/B_i)\sin^2\theta_i}\le1-\sqrt{1-B_f/B_i}\simeq\frac{B_f}{2B_i}.$$
Cette borne correspond au cas d'une vitesse initiale presque transverse, pour $B_f/B_i\ll1$. Une normalisation par la vitesse mesurée donne la même borne au premier ordre.

## Bilan

**Méthodes à retenir.** Vérifier une approximation par un nombre sans dimension (questions 4 et 5). Tracer une courbe à partir de ses asymptotes et de ses extremums, puis la confronter aux équations du mouvement (11, 12, 14). Lire une sélection d'harmoniques sur une symétrie du signal, ici l'antisymétrie de demi-période (15, 16). Intégrer une équation du second ordre avec ses deux constantes et les fixer par les conditions initiales (17 à 19). Contrôler un résultat par ses cas limites (38).

**Prérequis à revoir.** Faisceau gaussien et conditions de Gauss ; vecteur de Poynting et ordre de grandeur du flux solaire ; effet tunnel ; séries de Fourier ; interférences à $N$ ondes et réseau ; mouvement d'une charge dans un champ magnétique uniforme.

**Questions transposables.** L'abaissement d'une barrière coulombienne par un champ (12) se retrouve dans l'émission par effet de champ. La somme géométrique de la question 28 sert pour tout peigne de fréquences, dont le laser à modes bloqués. La conservation de $J$ (40) est le principe de la bouteille et du miroir magnétiques.

[Sujet officiel](https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Physique%20B%20PC.pdf) · [Rapport du jury](https://www.polytechnique.edu/admission-cycle-ingenieur/sites/admission/files/content/Ecrits_PC_Physique_B%20OK.pdf)
