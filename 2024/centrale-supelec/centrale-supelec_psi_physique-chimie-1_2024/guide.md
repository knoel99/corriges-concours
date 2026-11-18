# Centrale-Supélec PSI — Physique-chimie 1 2024 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*


## Présentation du sujet

Le sujet de quatre heures comporte 39 questions autour de cinq modèles physiques et chimiques. Le circuit primaire mobilise les bilans de diffusion et les écoulements stationnaires. Le circuit secondaire demande de lire puis de construire des cycles dans un diagramme pression–enthalpie. Le modèle d’alternateur combine induction, régime sinusoïdal et conversion de puissance. Les deux dernières parties portent sur les titrages et la solubilité.

Les parties sont indépendantes. Pour avancer rapidement, on peut traiter les premières applications du modèle thermique, le circuit électrique et les équilibres de solution avant de revenir aux bilans les plus longs. Réservez du temps au diagramme des frigoristes et à la lecture des courbes de titrage. Une valeur obtenue graphiquement se justifie par les coordonnées ou les courbes utilisées pour la lire.

## I — Étude du circuit primaire

Deux bilans se succèdent. Le premier suit le flux radial à travers les interfaces. Le second ajoute un écoulement d’eau dans lequel la température varie avec l’altitude.

### I.A — Évolution de la température entre le cœur du combustible et le fluide caloporteur

### Question 1

> [!INDICATION]
> Considérez la surface latérale à partir du diamètre extérieur et de la hauteur.

#### Solution

La surface latérale d’un crayon gainé est le produit du périmètre de la section extérieure par la hauteur. Pour les $N$ crayons,
$$\boxed{S_{\mathrm{tot}}=N\pi d H.}$$

### Question 2

> [!INDICATION]
> Définissez le système comme une couronne de combustible et choisissez un sens positif pour la puissance radiale.

> [!INDICATION]
> Comparez les puissances aux deux faces, ajoutez la production dans le volume et introduisez Fourier après le bilan.

#### Solution

Considérons le combustible entre les rayons $r$ et $r+\mathrm dr$, sur la hauteur $NH$. Le volume est $2\pi rNH\,\mathrm dr$ au premier ordre. Notons $\Phi(r)$ la puissance traversant la surface latérale de rayon $r$, comptée positivement vers l’extérieur.

Entre $t$ et $t+\mathrm dt$, le premier principe appliqué à cette portion de solide immobile donne une variation d’énergie interne $\rho c\,2\pi rNH\,\mathrm dr\,\partial_tT\,\mathrm dt$, pour une phase condensée de masse volumique $\rho$ et de capacité thermique massique $c$.

Il n’y a pas de travail mécanique.

La chaleur reçue vaut $[\Phi(r)-\Phi(r+\mathrm dr)]\,\mathrm dt$ et la production volumique libère $P_V\,2\pi rNH\,\mathrm dr\,\mathrm dt$.

En régime stationnaire, $\partial_tT=0$. Après division par $\mathrm dt\,\mathrm dr$, on obtient $\Phi'(r)=2\pi rNH P_V$. La loi de Fourier donne $\Phi(r)=-2\pi rNH\lambda_2T'(r)$. Ainsi
$$\boxed{\begin{aligned}
\frac{\mathrm d}{\mathrm dr}\bigl(rT'(r)\bigr)+Ar&=0,\\
A&=\frac{P_V}{\lambda_2}.
\end{aligned}}$$

> [!JURY]
> Le rapport attend un bilan énergétique sur une portion de solide et déconseille de supposer connue la divergence en coordonnées cylindriques. Les deux surfaces et le volume déterminent directement les facteurs de rayon.

### Question 3

> [!INDICATION]
> Une première intégration donne deux termes après division par le rayon.

> [!INDICATION]
> Appliquez successivement la régularité sur l’axe et la valeur du côté combustible en $R_3$.

#### Solution

En intégrant Q2, $rT'(r)=-P_Vr^2/(2\lambda_2)+C$. Si $C\ne0$, la température contient un terme en $\ln r$ et diverge sur l’axe. La régularité en $0$ impose $C=0$. Avec $T(R_3)=T_2$ côté combustible,
$$\boxed{T(r)=T_2+\frac{P_V}{4\lambda_2}(R_3^2-r^2).}$$

### Question 4

> [!INDICATION]
> Repérez le rayon auquel s’applique le coefficient $h_2$.

> [!INDICATION]
> Justifiez que la puissance reçue par la gaine est celle que perd le combustible.

#### Solution

La puissance totale $P_1$ sort intégralement du combustible en régime stationnaire. Elle traverse l’interface sans stockage, du combustible vers la gaine. La loi de Newton donne $P_1=h_2\,2\pi R_3NH(T_2-T_3)$. Comme $2R_3=d-2e$,
$$\boxed{T_3=T_2-\frac{P_1}{h_2\pi(d-2e)HN}.}$$

> [!PIEGE]
> Une discontinuité de température à l’interface est compatible avec une continuité de la puissance transférée si l’interface ne stocke pas d’énergie.

### Question 5

> [!INDICATION]
> Quelle puissance est créée à l’intérieur de la gaine ?

> [!INDICATION]
> Écrivez le flux de Fourier à rayon quelconque, puis imposez la température au bord extérieur.

#### Solution

La gaine ne comporte aucune source. La puissance radiale est donc constante et vaut $P_1$ sur chaque cylindre de rayon $r$. La loi de Fourier donne $-2\pi rNH\lambda_3T'(r)=P_1$. En intégrant à partir du bord extérieur $R_4$, côté gaine, on trouve
$$\boxed{T(r)=T_4+\frac{P_1R_4}{\lambda_3S_{\mathrm{tot}}}\ln\frac{R_4}{r}.}$$

> [!JURY]
> Le rapport distingue la source située dans le combustible de la puissance qui traverse passivement la gaine. La puissance du cœur intervient comme condition au bord.

### Question 6

> [!INDICATION]
> Remontez de l’eau jusqu’à l’axe en additionnant une différence de température à chaque étape.

> [!INDICATION]
> Exprimez la puissance volumique en divisant $P_1$ par le volume total actif.

#### Solution

Avec $S_{\mathrm{tot}}=4{,}527\times10^3\,\mathrm{m^2}$, $R_4=4{,}75\,\mathrm{mm}$ et $R_3=4{,}15\,\mathrm{mm}$, on applique la loi de Newton en $R_4$, puis Q5, Q4 et Q3. On obtient
$$\begin{aligned}
T_4&=T_5+\frac{P_1}{h_4S_{\mathrm{tot}}}\simeq327{,}5\,^\circ\mathrm C,\\
T_3&=T_4+\frac{P_1R_4}{\lambda_3S_{\mathrm{tot}}}\ln\frac{R_4}{R_3}\simeq352{,}1\,^\circ\mathrm C,\\
T_2&=T_3+\frac{P_1}{h_2\pi(d-2e)HN}\simeq422{,}3\,^\circ\mathrm C,\\
T_1&=T_2+\frac{P_1}{4\lambda_2N\pi H}\simeq838{,}3\,^\circ\mathrm C.
\end{aligned}$$
Dans la dernière ligne, on a utilisé $P_1=P_VN\pi R_3^2H$.

### Question 7

> [!INDICATION]
> Reprenez séparément la forme de la solution dans chaque milieu.

> [!INDICATION]
> Aux interfaces, les données de la loi d’échange permettent-elles de prolonger la température par continuité ?

#### Solution

Le profil est une parabole concave, horizontale à l’origine, dans le combustible.

Il saute de $T_2$ à $T_3$ en $R_3$, puis décroît suivant $-\ln r$ dans la gaine.

Il saute de $T_4$ à $T_5$ en $R_4$ et reste constant jusqu’à $R_5$. La position de $R_5$ sur le schéma est indicative.

![Figure 1 — Profil radial du modèle. Les températures ont deux sauts aux interfaces.](figures/q7-profil.svg)

> [!JURY]
> Le rapport relève en particulier les erreurs de concavité et les sauts oubliés. Une parabole qui décroît à partir d’une tangente horizontale à l’axe est concave.

### Question 8

> [!INDICATION]
> Comparez la température du fluide à la température de saturation à la pression indiquée.

> [!INDICATION]
> Dans la relation d’échange, quel facteur géométrique permet de transférer davantage à différence de température fixée ?

#### Solution

À $155\,\mathrm{bar}$, l’eau sature à $345\,^\circ\mathrm C$. Le pressuriseur maintient une pression qui permet au fluide de rester liquide avec une marge sur la température de saturation. Une chute de pression réduit cette marge et peut provoquer une vaporisation préjudiciable au transfert thermique. Dans le modèle, augmenter la surface d’échange permet d’évacuer une puissance plus grande pour un même écart de température, d’après la loi de Newton.

### I.B — Prise en compte de dépendances longitudinales pour la puissance thermique volumique et la température

### Question 9

> [!INDICATION]
> Prenez la couronne d’eau comme volume de contrôle et identifiez la masse qui franchit chaque section pendant $\mathrm dt$.

> [!INDICATION]
> Identifiez la provenance de la chaleur reçue et les raisons pour lesquelles elle est entièrement transférée à l’eau.

#### Solution

Le volume de contrôle est l’espace annulaire entre les cotes $z$ et $z+\mathrm dz$. En régime stationnaire, pendant $\mathrm dt$, la masse entrante et la masse sortante valent toutes deux $D_m\mathrm dt$. Le premier principe en écoulement stationnaire relie leur écart d’enthalpie au transfert thermique reçu, puisque le travail utile et la variation d’énergie mécanique sont nuls. Dans le modèle du liquide incompressible et indilatable, avec variation de pression négligée pour ce bilan, l’écart d’enthalpie massique s’écrit $c_5[T(z+\mathrm dz)-T(z)]$.

La chaleur apportée par la portion de crayon de hauteur $\mathrm dz$ est, au premier ordre, $P_V(z)\pi R_4^2\,\mathrm dz\,\mathrm dt$. Elle est entièrement reçue par l’eau, car il n’y a ni stockage ni flux à travers la paroi extérieure. Après division par $\mathrm dt$,
$$\boxed{D_m c_5[T(z+\mathrm dz)-T(z)]=P_V(z)\pi R_4^2\,\mathrm dz.}$$

> [!JURY]
> Le rapport attend le premier principe pour un écoulement stationnaire et une justification de la provenance de la chaleur reçue par l’eau.

### Question 10

> [!INDICATION]
> Passez à une équation pour $T'(z)$ et intégrez-la en tenant compte du profil de la source.

> [!INDICATION]
> Faites intervenir les valeurs aux extrémités pour éliminer $P_0$ du profil.

#### Solution

En posant $u=\pi z/H$, Q9 donne $T'(z)=\pi R_4^2P_0\sin u/(D_m c_5)$. L’intégration à partir de $0$ donne
$$\begin{aligned}
T_s-T_e&=\frac{2R_4^2HP_0}{D_m c_5},\\
T(z)&=T_e+\frac{T_s-T_e}{2}(1-\cos u).
\end{aligned}$$

### Question 11

> [!INDICATION]
> À une cote fixée, comparez la production par unité de hauteur et le transfert à la paroi.

> [!INDICATION]
> Éliminez ensuite l’amplitude de la source par Q10.

#### Solution

À la cote $z$, la puissance créée par unité de longueur est $\pi R_4^2P_V(z)$. Elle est égale à $2\pi R_4h_{cc}[T_p(z)-T(z)]$ par conservation du flux stationnaire et loi de Newton. On a donc $T_p-T=P_V(z)R_4/(2h_{cc})$. En utilisant la relation de Q10 pour éliminer $P_0$,
$$\boxed{\begin{aligned}
B&=-1,\\
C&=\frac{D_m c_5}{2Hh_{cc}R_4}.
\end{aligned}}$$

### Question 12

> [!INDICATION]
> Expliquez pourquoi on peut reprendre le bilan radial à $z$ fixé.

> [!INDICATION]
> Utilisez la température de paroi comme condition de bord, puis comparez avec la forme réduite donnée.

#### Solution

À $z$ fixé, l’absence de conduction axiale permet de refaire le bilan radial de Q2 avec la source $P_V(z)$. La régularité sur l’axe et la condition $T_c(R_4,z)=T_p(z)$ donnent
$$T_c(r,z)=T_p(z)+\frac{P_0}{4\lambda_2}(R_4^2-r^2)\sin u.$$
Les constantes d’intégration éventuelles dépendent de $z$. En divisant par $T_s-T_e$ et en utilisant Q10–Q11, on retrouve la forme demandée avec
$$\boxed{\begin{aligned}
D&=-1,\\
E&=\frac{D_m c_5}{4Hh_{cc}R_4},\\
F&=\frac{D_m c_5}{8H\lambda_2}.
\end{aligned}}$$

### Question 13

> [!INDICATION]
> Dans l’expression de Q12, fixez le rayon à zéro et remplacez les coefficients.

#### Solution

Sur l’axe, $r=0$. L’expression de Q12 devient
$$\boxed{\begin{aligned}
T_c(0,z)=T_e+(T_s-T_e)\Bigg[&\frac{1-\cos(\pi z/H)}{2}\\
&+\frac{D_mc_5}{4H}\left(\frac1{h_{cc}R_4}+\frac1{2\lambda_2}\right)\sin(\pi z/H)\Bigg].
\end{aligned}}$$

### Question 14

> [!INDICATION]
> Annulez la dérivée par rapport à l’angle $\pi z/H$ et choisissez le bon intervalle pour la racine.

> [!INDICATION]
> Vérifiez que le point donne un maximum, puis comparez sa température à la donnée de fusion.

#### Solution

Posons $a=E+F>0$.

Le terme qui dépend de $u$ est $-\cos u/2+a\sin u$.

Sa dérivée vaut $\sin u/2+a\cos u$.

Elle s’annule une seule fois sur $[0,\pi]$, en $u_*=\pi-\arctan(2a)$, où elle passe de positive à négative.

Le terme atteint alors $\sqrt{a^2+1/4}$.

Ainsi
$$\begin{aligned}
z_*&=\frac{H}{\pi}\bigl[\pi-\arctan(2a)\bigr],\\
T_{\max}&=T_e+(T_s-T_e)\left(\frac12+\sqrt{a^2+\frac14}\right).
\end{aligned}$$
Avec $h_{cc}=33\,\mathrm{kW\,m^{-2}K^{-1}}$, on trouve $a\simeq17{,}58$, puis **$z_*\simeq1{,}86\,\mathrm m$ et $T_{\max}\simeq971\,^\circ\mathrm C$**. Dans le modèle, la température reste inférieure à la température de fusion du combustible, $2800\,^\circ\mathrm C$.

> [!PIEGE]
> La tangente ne détermine un angle qu’à un multiple de π près. Le profil et le domaine fixent ici le quadrant.

### Question 15

> [!INDICATION]
> Séparez l’échauffement cumulé de l’eau et l’écart local entre paroi et eau.

> [!INDICATION]
> Où la production locale commence-t-elle à diminuer ? Où s’annule-t-elle ?

#### Solution

La température de l’eau augmente tout le long du crayon, car le fluide accumule la chaleur reçue. L’écart entre la paroi et l’eau est au contraire proportionnel à la production locale $\sin u$. Il augmente jusqu’à mi-hauteur et décroît ensuite jusqu’à zéro. La température de paroi monte donc d’abord. Son maximum se situe après la mi-hauteur, car l’eau s’y réchauffe encore. Près de la sortie, la baisse de production domine et $T_p$ redescend vers $T_s$.

## II — Étude du circuit secondaire

Les travaux utiles et les transferts de chaleur s’expriment par des différences d’enthalpie massique. On distingue les états calculés avec un tableau de ceux qui doivent être lus sur le diagramme.

### II.A — Préliminaire

### Question 16

> [!INDICATION]
> Construisez un système fermé qui change de position autour du volume de contrôle entre les deux instants.

> [!INDICATION]
> Pour les travaux de pression, comparez le sens des forces à celui du déplacement de chaque tranche.

#### Solution

Sur $\mathrm dt$, prenons le système fermé constitué à l’instant initial du fluide présent dans la machine et de la tranche qui entre. À l’instant final, il est constitué du fluide alors présent dans la machine et de la tranche qui sort.

```text
À t       [tranche entrante] → | volume de contrôle |
À t + dt                       | volume de contrôle | → [tranche sortante]
```

En régime stationnaire, la masse dans le volume de contrôle est constante. Les tranches ont la même masse $\delta m$, et l’énergie stockée dans la machine est inchangée. La variation d’énergie interne du système vaut donc $\delta m(u_s-u_e)$ après négligence des variations d’énergie mécanique.

Les forces pressantes poussent la tranche entrante dans le sens de son déplacement et fournissent $+p_e\delta m v_e$. Elles s’opposent au déplacement de la tranche sortante et fournissent $-p_s\delta m v_s$. Ici $v_e$ et $v_s$ sont les volumes massiques. À ces travaux s’ajoutent $\delta m w_u$ et le transfert thermique $\delta m q$. Le premier principe donne
$$u_s-u_e=p_e v_e-p_s v_s+w_u+q.$$
En regroupant les termes à l’aide de $h=u+pv$, **$h_s-h_e=w_u+q$**.

> [!JURY]
> Le rapport attend deux conséquences distinctes de la stationnarité, à savoir l’égalité des masses franchissant les limites pendant le même temps et l’absence d’accumulation d’énergie dans le volume de contrôle.

### II.B — Cycle de Hirn

### Question 17

> [!INDICATION]
> Utilisez l’expression fournie pour l’entropie d’une phase condensée incompressible.

> [!INDICATION]
> Sur le graphique, quelle direction correspond à une enthalpie presque constante ?

#### Solution

Dans le modèle liquide incompressible, l’entropie varie avec la température selon $\Delta s=c\ln(T_1/T_0)$. La compression isentropique impose donc $T_1\simeq T_0$. Le travail de pompe négligé, avec une compression adiabatique, donne $h_1\simeq h_0$ par Q16. Le trajet isentropique est ainsi presque vertical dans le domaine liquide du diagramme $(p,h)$.

### Question 18

> [!INDICATION]
> Commencez par les deux isobares de l’installation et distinguez les deux branches de saturation.

> [!INDICATION]
> Identifiez les courbes à suivre pour joindre les états entre les niveaux de pression.

#### Solution

La branche gauche de la courbe de saturation est la courbe d’ébullition et la branche droite la courbe de rosée. Le dôme contient les états diphasés. Les isobares sont horizontales, les isenthalpes verticales. Les courbes noires repérées par les températures sont les isothermes. Les courbes rouges repérées par $s$ sont les isentropes. Dans le dôme, une isotherme suit l’isobare de saturation correspondante.

Le fluide est comprimé de $0$ à $1$.

À $85{,}8\,\mathrm{bar}$, on le chauffe jusqu’à $1'$ à l’ébullition, puis on le vaporise jusqu’à $2$ sur la rosée, et enfin on le surchauffe jusqu’à $2'$ à $500\,^\circ\mathrm C$.

On suit ensuite l’isentropique $s=6{,}68\,\mathrm{kJ\,kg^{-1}K^{-1}}$ jusqu’à $0{,}040\,\mathrm{bar}$ pour atteindre $3$.

La condensation isobare ferme le cycle de $3$ à $0$.

![Figure 2 — Cycle de Hirn orienté dans le plan pression–enthalpie, avec les états de saturation repérés.](figures/q18-hirn.svg)

> [!JURY]
> Le rapport demande les noms des familles de courbes, un cycle orienté et les états repérés. La courbe de rosée sépare la région diphasée de la vapeur.

### Question 19

> [!INDICATION]
> Cherchez d’abord l’entropie de sortie à partir de la transformation dans la turbine.

> [!INDICATION]
> Appliquez les lois de mélange à l’entropie puis à l’enthalpie entre les valeurs saturées.

#### Solution

À l’état $3$, la détente isentropique impose $s_3=s_{2'}$. Le titre massique $x_3$ satisfait $s_3=(1-x_3)s_\ell+x_3s_v$ avec les valeurs saturées à $0{,}040\,\mathrm{bar}$. De même, l’enthalpie massique du mélange vaut $h_3=(1-x_3)h_\ell+x_3h_v$. Ainsi
$$\begin{aligned}
x_3&=\frac{6{,}68-0{,}42}{8{,}47-0{,}42}\simeq0{,}778,\\
h_3&=121+x_3(2554-121)\simeq2013\,\mathrm{kJ\,kg^{-1}}.
\end{aligned}$$
Le point $3$ est donc dans le dôme, sur l’isobare $0{,}040\,\mathrm{bar}$, à $h\simeq2{,}01\,\mathrm{MJ\,kg^{-1}}$.

> [!METHODE]
> Le titre en vapeur est une fraction de masse. Il interpole linéairement des grandeurs massiques extensives, notamment l’entropie et l’enthalpie du mélange.

### Question 20

> [!INDICATION]
> Identifiez les étapes qui fournissent du travail et celles qui reçoivent la chaleur payée.

> [!INDICATION]
> Pour chacune, utilisez Q16 en supprimant le terme qui ne s’applique pas.

#### Solution

L’efficacité est le travail utile net livré sur un cycle divisé par la chaleur reçue de la source chaude. La turbine est adiabatique et fournit $h_{2'}-h_3$ par kilogramme, d’après Q16. Le générateur et le surchauffeur reçoivent $h_{2'}-h_1$ en l’absence de travail utile. Le travail de pompe est négligé. Ainsi
$$\boxed{\eta=\frac{h_{2'}-h_3}{h_{2'}-h_1}
\simeq\frac{3391-2013}{3391-121}\simeq0{,}421.}$$

### Question 21

> [!INDICATION]
> Choisissez des signes cohérents pour la chaleur reçue, la chaleur rejetée et le travail.

> [!INDICATION]
> Écrivez les deux bilans sur le cycle réversible, avec les températures absolues.

#### Solution

Notons $Q_C>0$ et $Q_F<0$ les chaleurs algébriquement reçues, et $W<0$ le travail algébriquement reçu par le fluide sur le cycle. La chaleur entre depuis la source chaude. La chaleur rejetée et le travail utile sortent vers la source froide et la charge, respectivement.

```text
Source chaude  -- Q_C --> [moteur] -- -Q_F --> source froide
                              |
                              +------ -W ----> charge
```

Les quantités écrites le long des flèches sont positives dans le sens indiqué. Le premier principe donne $W+Q_C+Q_F=0$. Pour le cycle réversible de Carnot, le second principe donne $Q_C/T_C+Q_F/T_F=0$. On en déduit
$$\boxed{\eta_C=-\frac{W}{Q_C}=1-\frac{T_F}{T_C}
\simeq1-\frac{302{,}15}{773{,}15}\simeq0{,}609.}$$
Le cycle de Hirn reçoit une partie de sa chaleur à des températures inférieures à $500\,^\circ\mathrm C$, notamment durant la vaporisation à $300\,^\circ\mathrm C$. Cela explique l’écart avec la référence de Carnot calculée à partir des deux températures extrêmes.

### II.C — Cycle à double surchauffe

### Question 22

> [!INDICATION]
> Repérez l’intersection de la première isentropique avec l’isotherme de l’état 4, puis chauffez à pression constante.

> [!INDICATION]
> Contrôlez le titre que donne la seconde isentropique et faites apparaître les deux chutes d’enthalpie dans le travail utile.

#### Solution

On conserve jusqu’à $2'$ le tracé de Q18.

À partir de $2'$ on descend le long de l’isentropique jusqu’à l’isotherme $300\,^\circ\mathrm C$, au point $4$.

Le document réponse donne environ $p_4\simeq24\,\mathrm{bar}$ et $h_4\simeq3{,}00\times10^3\,\mathrm{kJ\,kg^{-1}}$.

La seconde surchauffe à cette pression atteint $4'$ sur l’isotherme $500\,^\circ\mathrm C$.

On lit environ $h_{4'}\simeq3{,}46\times10^3\,\mathrm{kJ\,kg^{-1}}$ et $s_{4'}\simeq7{,}35\,\mathrm{kJ\,kg^{-1}K^{-1}}$.

La seconde détente suit cette isentropique jusqu’à $0{,}040\,\mathrm{bar}$. Les données du tableau donnent $x_5\simeq(7{,}35-0{,}42)/(8{,}47-0{,}42)\simeq0{,}86$ et $h_5\simeq2{,}22\times10^3\,\mathrm{kJ\,kg^{-1}}$. Le point se situe à l’intérieur du dôme, plus près de la rosée que l’état $3$ de Q19. Imposer $x_5=1$ exactement demanderait une entropie $s_{4'}=8{,}47$, incompatible avec les deux températures et l’isobare retenues. La construction conserve les deux détentes isentropiques et interprète le titre donné comme une estimation.

![Figure 3 — Cycle à double surchauffe orienté dans le plan pression–enthalpie. Le second chauffage est isobare.](figures/q22-double-surchauffe.svg)

Le fluide est chauffé de $1$ à $2'$ et de $4$ à $4'$, tandis que les turbines fournissent les travaux des deux chutes d’enthalpie. En négligeant toujours le travail de pompe,
$$\boxed{\eta=\frac{(h_{2'}-h_4)+(h_{4'}-h_5)}{(h_{2'}-h_1)+(h_{4'}-h_4)}\simeq0{,}44.}$$
Cette valeur dépend de la précision des lectures graphiques.

> [!JURY]
> Le rapport admet plusieurs interprétations cohérentes du titre final annoncé proche de un. Le calcul présenté privilégie les transformations isentropiques et les deux températures de surchauffe.

### II.D — Cycle réel d’une tranche nucléaire

### Question 23

> [!INDICATION]
> Prenez séparément les échangeurs et chacune des deux turbines comme volumes de contrôle.

> [!INDICATION]
> Pour une turbine avec soutirages, additionnez les débits d’enthalpie sur toutes les sorties.

#### Solution

D’après Q16, la puissance thermique reçue dans les échangeurs vaut $\dot m_{\mathrm{GV}}(h_s-h_e)$. Le débit y vaut $5412{,}1/3{,}6\,\mathrm{kg\,s^{-1}}$, d’où $\dot Q_{\mathrm{GV}}\simeq2776\,\mathrm{MW}$.

Pour chaque turbine adiabatique, la puissance mécanique fournie est le débit d’enthalpie entrant diminué de la somme des débits d’enthalpie sortants. Il faut compter les soutirages en plus de l’échappement. Avec les débits du tableau en $\mathrm{t\,h^{-1}}$, on obtient en mégawatts
$$\begin{aligned}
P_{\mathrm{HP}}={}&\bigl[5001{,}9(2787{,}1)-214{,}3(2682{,}5)-208{,}4(2622{,}6)\\
&\quad-(402{,}1+4177{,}1)(2562{,}8)\bigr]/3600\simeq301,\\
P_{\mathrm{BP}}={}&\bigl[3704(2970{,}4)-281{,}4(2731{,}5)-235{,}4(2538{,}9)\\
&\quad-134{,}2(2377{,}8)-3053(2242{,}2)\bigr]/3600\simeq687.
\end{aligned}$$
On calcule donc **$\eta\simeq35{,}6\,\%$ et $P_{\mathrm{HP}}+P_{\mathrm{BP}}\simeq988\,\mathrm{MW}$** disponibles mécaniquement pour un alternateur idéal. La puissance électrique mesurée peut être inférieure à cause des pertes mécaniques et électriques ainsi que des auxiliaires selon le périmètre de mesure.

> [!METHODE]
> Un soutirage est une sortie du volume de contrôle de la turbine. Son débit d’enthalpie figure au bilan même lorsque la vapeur est réutilisée en aval.

## III — Étude de l’alternateur

La variation du flux extérieur crée une force électromotrice. Le couple moyen et la dissipation se déduisent ensuite de produits de grandeurs périodiques.

### Question 24

> [!INDICATION]
> Calculez le flux lié au champ extérieur avec la normale à la spire.

> [!INDICATION]
> Écrivez la force électromotrice induite et l’équation de la boucle série, puis utilisez le régime sinusoïdal.

#### Solution

Le flux extérieur, avec la normale du sens positif du courant, est $\Phi_{\mathrm{ext}}=BS\cos(\omega t)$. Par la loi de Faraday, la force électromotrice due au champ extérieur est $BS\omega\sin(\omega t)$. La loi des mailles dans la spire, modélisée par une résistance et une inductance en série, donne
$$L\frac{\mathrm di}{\mathrm dt}+Ri=BS\omega\sin(\omega t).$$
En régime forcé, l’amplitude est $I_m=BS\omega/\sqrt{R^2+(L\omega)^2}$. Le courant est en retard de $\varphi=\arctan(L\omega/R)$ sur l’excitation. Ces deux relations s’obtiennent en divisant l’amplitude de la force électromotrice par le module de l’impédance $R+\mathrm iL\omega$, et en retranchant son argument à la phase de l’excitation. Ainsi **$i(t)=I_m\sin(\omega t-\varphi)$**.

### Question 25

> [!INDICATION]
> Orientez le moment magnétique de la spire et projetez son produit vectoriel avec le champ.

> [!INDICATION]
> Pour la moyenne, gardez le terme constant du produit des deux sinus.

#### Solution

Le moment magnétique est $iS\vec n$. Avec $\vec n=\cos(\omega t)\vec u_x+\sin(\omega t)\vec u_y$, le couple magnétique vérifie $\Gamma_z=-iSB\sin(\omega t)$. La moyenne du produit des deux sinus est $\cos\varphi/2$, ce qui donne
$$\boxed{\langle\Gamma_z\rangle=-\frac{(BS)^2\omega R}{2[R^2+(L\omega)^2]}.}$$
Le signe est opposé à celui de la rotation. Ce couple résistant traduit la loi de Lenz.

> [!JURY]
> Le rapport attend un lien explicite entre le couple résistant et la loi de Lenz. La convention choisie avec une rotation positive donne un couple moyen négatif.

### Question 26

> [!INDICATION]
> La vitesse étant constante, quel couple la turbine doit-elle exercer ?

> [!INDICATION]
> Pour l’effet Joule, utilisez la moyenne du carré du courant.

#### Solution

Sans frottement et à vitesse constante, la turbine applique le couple opposé. Sa puissance moyenne vaut $-\omega\langle\Gamma_z\rangle$. Par effet Joule, $\langle P_J\rangle=R\langle i^2\rangle=RI_m^2/2$. Ainsi
$$\boxed{\langle P_{\mathrm{turbine}}\rangle=\langle P_J\rangle
=\frac{R(BS\omega)^2}{2[R^2+(L\omega)^2]}.}$$
L’énergie magnétique de la bobine est périodique et ne reçoit aucune puissance nette en moyenne.

## IV — Contrôle de la concentration en bore dans le circuit primaire

Le mannitol modifie l’acidité apparente. Le titrage conductimétrique repère plutôt le changement d’ion majoritairement ajouté après l’équivalence.

### IV.A — Titrage pH-métrique

### Question 27

> [!INDICATION]
> Additionnez les deux équations pour éliminer le borate.

> [!INDICATION]
> Pour des réactions qui s’ajoutent, comment se combinent les constantes ?

#### Solution

En additionnant les deux réactions, on obtient
$$\mathrm{H_3BO_3(aq)}+2\mathrm{M(aq)}\rightleftharpoons
\mathrm{C^-(aq)}+\mathrm{H_3O^+(aq)}+2\mathrm{H_2O(l)}.$$
Les constantes se multiplient. Ainsi **$K=10^{-9{,}25}\times10^5=10^{-4{,}25}\simeq5{,}6\times10^{-5}$**. La réaction est thermodynamiquement peu favorisée dans l’état standard à $25\,^\circ\mathrm C$. Un excès de mannitol peut néanmoins déplacer l’équilibre.

### Question 28

> [!INDICATION]
> Isolez le quotient des activités qui définit la constante apparente.

> [!INDICATION]
> Analysez le signe du terme logarithmique lorsque le mannitol est ajouté.

#### Solution

Avec l’activité de l’eau prise égale à un, $K=K_{a,\mathrm{app}}/a_{\mathrm M}^2$. En solution diluée, $a_{\mathrm M}\simeq[\mathrm M]/c^\circ$, donc
$$\boxed{\mathrm{p}K_{a,\mathrm{app}}=\mathrm{p}K-2\log\!\left(\frac{[\mathrm M]}{c^\circ}\right).}$$

### Question 29

> [!INDICATION]
> Repérez le volume de demi-équivalence après lecture du volume équivalent.

> [!INDICATION]
> La valeur du pH en ce point fournit une donnée d’équilibre à comparer à la question précédente.

#### Solution

Le titrage sans mannitol suit $\mathrm{H_3BO_3}+\mathrm{OH^-}\to\mathrm{B(OH)_4^-}$. En présence de mannitol en excès, le bilan s’écrit $\mathrm{H_3BO_3}+2\mathrm M+\mathrm{OH^-}\to\mathrm{C^-}+3\mathrm{H_2O}$. Ces bilans consomment une mole d’hydroxyde par mole de bore. Les constantes de neutralisation valent $K_a/K_e$ ou $K_{a,\mathrm{app}}/K_e$, très supérieures à un pour les valeurs de pH de demi-équivalence observées.

On lit $V_{B,\mathrm{eq}}\simeq10\,\mathrm{mL}$ au voisinage du point d’inflexion du saut, surtout net pour (c). Donc **$C_0=C_BV_{B,\mathrm{eq}}/(10\,\mathrm{mL})\simeq0{,}10\,\mathrm{mol\,L^{-1}}$**.

À $V_B\simeq5\,\mathrm{mL}$, on lit environ $9{,}25$, $7{,}3$ et $5{,}6$ pour (a), (b) et (c).

À demi-équivalence, les concentrations analytiques d’acide restant et de base formée sont voisines, donc le pH donne le $\mathrm pK_a$ apparent dans le modèle.

La courbe (a) donne le $\mathrm pK_a$ de l’acide seul, donc **$x_a=0$**.

Dans l’approximation d’excès de mannitol, sa concentration est assimilée à $x/(M_D\,0{,}200\,\mathrm L)$ en négligeant la dilution par les $5\,\mathrm{mL}$ titrants et la fraction complexée. Par Q28,
$$x\simeq M_D(0{,}200\,\mathrm L)c^\circ\,10^{(4{,}25-\mathrm pH_{\mathrm{demi}})/2}.$$
Les lectures donnent **$x_b\simeq1{,}1\,\mathrm g$ et $x_c\simeq7{,}7\,\mathrm g$** dans cette approximation.

Tenir compte du volume à demi-équivalence et d’environ $1\,\mathrm{mmol}$ de mannitol lié ajouterait environ $0{,}2\,\mathrm g$ à $x_b$ et $0{,}4\,\mathrm g$ à $x_c$.

> [!JURY]
> Le rapport demande d’argumenter le caractère quasi total de la transformation de titrage et de justifier le repérage graphique de l’équivalence.

### IV.B — Titrage conductimétrique

### Question 30

> [!INDICATION]
> Écrivez d’abord les quantités d’ions, sans oublier le sodium spectateur.

> [!INDICATION]
> Utilisez le même volume total pour convertir chaque quantité en concentration.

#### Solution

Posons $n_0=C_AV_A$ et $V_e=n_0/C_B$. Le bilan est $\mathrm{H_3BO_3}+\mathrm{OH^-}\to\mathrm{B(OH)_4^-}$. Le modèle de titrage stœchiométrique néglige l’ionisation initiale de l’acide et l’hydrolyse du borate dans les bilans dominants. Le sodium apporté est spectateur. Avant l’équivalence, les quantités de sodium et de borate sont $C_BV_B$. Après, le borate vaut $n_0$ et l’excès d’hydroxyde vaut $C_BV_B-n_0$.

La loi de Kohlrausch donne, avec les volumes en $\mathrm{m^3}$ et les concentrations en $\mathrm{mol\,m^{-3}}$,
$$\boxed{(V_A+V_B)\sigma=
\begin{cases}
C_B(\lambda_{\mathrm{Na^+}}+\lambda_{\mathrm{B(OH)_4^-}})V_B & (V_B\le V_e),\\
C_B(\lambda_{\mathrm{Na^+}}+\lambda_{\mathrm{OH^-}})V_B+
(\lambda_{\mathrm{B(OH)_4^-}}-\lambda_{\mathrm{OH^-}})n_0 & (V_B\ge V_e).
\end{cases}}$$

> [!METHODE]
> Le modèle linéaire par morceaux est un bilan stœchiométrique dominant. L’hydrolyse du borate peut notamment arrondir la cassure au voisinage de l’équivalence.

### Question 31

> [!INDICATION]
> Multipliez par le volume total afin de comparer les pentes, sans facteur de dilution.

> [!INDICATION]
> Comparez notamment les conductivités molaires des ions consommés ou accumulés de part et d’autre de l’équivalence.

#### Solution

Les deux expressions de Q30 coïncident en $V_e$. Les pentes, positives, sont proportionnelles respectivement à $5{,}01+6{,}70=11{,}71$ et $5{,}01+19{,}8=24{,}81$, dans les unités du tableau. La seconde pente est donc plus forte. Leur intersection donne $V_{B,\mathrm{eq}}=C_AV_A/C_B$ et permet d’en déduire la quantité de bore.

![Figure 4 — Conductivité corrigée de la dilution. La cassure en équivalence est suivie d’une pente plus élevée.](figures/q31-conductivite.svg)

## V — Étude de la contamination des circuits par les produits d’activation

Les constantes d’équilibre donnent les concentrations en fonction du pH. Le diagramme de solubilité s’explique en suivant la contribution dominante puis, près du minimum, en gardant leur somme.

### V.A — Préliminaire

### Question 32

> [!INDICATION]
> Écrivez le quotient d’équilibre pour la dissolution du solide.

> [!INDICATION]
> Imposez la concentration de frontière, puis vérifiez de quel côté la concentration de saturation est la plus forte.

#### Solution

Notons $h=[\mathrm{H_3O^+}]/c^\circ=10^{-\mathrm pH}$ et assimilons les activités dissoutes à leurs concentrations divisées par $c^\circ$.

À l’équilibre avec $\mathrm{NiO(s)}$, $[\mathrm{Ni^{2+}}]/c^\circ=K_4h^2$.

À $T=573{,}15\,\mathrm K$, $\mathrm pK_4\simeq-3{,}53$.

Pour $C'_{\mathrm{fr}}/c^\circ=10^{-1}$, la frontière est
$$\boxed{\mathrm pH_{\mathrm{fr}}=\frac{1-\mathrm pK_4}{2}\simeq2{,}26.}$$
Pour un inventaire dissous de référence $C'_{\mathrm{fr}}$, la saturation exige une concentration plus forte en milieu plus acide et le solide peut se dissoudre entièrement. Au-dessus de la frontière, la concentration de saturation devient plus faible et le solide peut subsister.

```text
pH croissant →   Ni²⁺(aq)          │          domaine d’existence de NiO(s)
                                  2,26
```

### Question 33

> [!INDICATION]
> Distinguez la naissance des produits radioactifs et le rayonnement qu’ils émettent au cours de la maintenance.

> [!INDICATION]
> Reliez la quantité qui peut être transportée à sa solubilité dans l’eau.

#### Solution

Des éléments provenant des matériaux du circuit peuvent être transportés ou redéposés. Une exposition au flux de neutrons peut en rendre une fraction radioactive. Le rayonnement émis par ces produits d’activation subsiste lors de la maintenance, même sans flux de neutrons en service. À $300\,^\circ\mathrm C$, la concentration de saturation de $\mathrm{Ni^{2+}}$ selon Q32 décroît d’un facteur $100$ par augmentation d’une unité de pH. Choisir un pH supérieur à $3$ tend donc à limiter la dissolution acide et le transport des produits métalliques dans ce modèle.

> [!PIEGE]
> Un diagramme de solubilité renseigne sur les espèces transportées. La radioactivité dépend de l’activation des noyaux et l’irradiation de l’exposition au rayonnement.

### V.B — Modèle de Palmer

### Question 34

> [!INDICATION]
> Utilisez la réaction entre les deux espèces dissoutes et imposez l’égalité de leurs concentrations.

#### Solution

La réaction de constante $K_5$ donne $[\mathrm{Ni(OH)_2(aq)}]/[\mathrm{Ni^{2+}}]=K_5/h^2$. L’égalité des concentrations impose $\mathrm pH=\mathrm pK_5/2$. À $573{,}15\,\mathrm K$, $\mathrm pK_5\simeq12{,}05$.

```text
pH croissant →   Ni²⁺(aq)          │          Ni(OH)₂(aq)
                                  6,02
```

### Question 35

> [!INDICATION]
> Écrivez les deux concentrations à saturation en fonction de l’activité des ions oxonium.

> [!INDICATION]
> Dans chaque domaine, conservez le terme dominant avant de prendre le logarithme.

#### Solution

À saturation, $[\mathrm{Ni^{2+}}]/c^\circ=K_4h^2$ et $[\mathrm{Ni(OH)_2}]/c^\circ=K_4K_5$. Ainsi $s/c^\circ=K_4(h^2+K_5)$. En ne conservant que l’espèce prédominante, le diagramme de $\log(s/c^\circ)$ s’écrit
$$\boxed{\begin{cases}
-\mathrm pK_4-2\,\mathrm pH\simeq3{,}53-2\,\mathrm pH & (\mathrm pH<6{,}02),\\
-\mathrm pK_4-\mathrm pK_5\simeq-8{,}52 & (\mathrm pH>6{,}02).
\end{cases}}$$
Au raccord exact, les deux contributions sont égales et leur somme ajoute $\log 2$ par rapport aux droites.

### Question 36

> [!INDICATION]
> Reprenez les deux concentrations, puis divisez chacune par leur somme.

> [!INDICATION]
> Pour la verticale, combinez le produit ionique de l’eau et l’égalité des deux concentrations dans l’eau neutre.

#### Solution

Dans l’eau neutre, les concentrations de $\mathrm{H_3O^+}$ et $\mathrm{OH^-}$ sont égales. Ainsi $\mathrm pH_\mathrm{en}=\mathrm pK_e/2=11{,}41/2=5{,}705$ à $300\,^\circ\mathrm C$. Les abondances relatives reprennent les deux termes de Q35.

```python
import numpy as np
import matplotlib.pyplot as plt


def K4(T):
    return 10**(-(6.093 - 5513.46 / T))


def K5(T):
    return 10**(-(-6.09 + 7282.7 / T + 0.009476 * T))


T = 573.15
pHen = 11.41 / 2
N = 1000
pHmin = 3
pHmax = 11
pas = (pHmax - pHmin) / (N - 1)
pH = np.zeros(N)
y1 = np.zeros(N)
y2 = np.zeros(N)

for i in range(N):
    pH[i] = pHmin + i * pas
    h = 10**(-pH[i])
    nickel = K4(T) * h**2
    hydroxyde = K4(T) * K5(T)
    y1[i] = nickel / (nickel + hydroxyde)
    y2[i] = hydroxyde / (nickel + hydroxyde)

plt.figure()
plt.plot(pH, 100 * y1, label="Ni2+")
plt.plot(pH, 100 * y2, linestyle="--", label="Ni(OH)2")
plt.plot([pHen, pHen], [0, 100], linestyle=":", label="Eau neutre")
plt.xlabel("pH")
plt.ylabel("%")
plt.grid()
plt.legend()
plt.show()
```

> [!JURY]
> Le rapport relève les oublis de justification du pH neutre à cette température et les écritures incorrectes d’une puissance de dix en Python.

### V.C — Modèle de Tremaine et Leblanc

### Question 37

> [!INDICATION]
> Exprimez la troisième concentration avec la nouvelle constante.

> [!INDICATION]
> Cherchez les croisements qui limitent le domaine où la concentration constante reste la plus grande.

#### Solution

À saturation, la nouvelle réaction donne $[\mathrm{Ni(OH)_3^-}]/c^\circ=K_{s3}/h$. Les trois concentrations réduites sont donc $K_4h^2$, $K_4K_5$ et $K_{s3}/h$. Le premier croisement de prédominance est celui de Q34. Le second est obtenu par $K_4K_5=K_{s3}/h$, d’où
$$\mathrm pH=\log(K_4K_5/K_{s3})\simeq9{,}25.$$
Comme le premier terme décroît et le troisième augmente avec le pH, et que l’ordre des deux frontières est $6{,}02<9{,}25$, le terme constant domine entre les deux.

```text
pH croissant →   Ni²⁺(aq)      │      Ni(OH)₂(aq)      │      Ni(OH)₃⁻(aq)
                              6,02                    9,25
```

### Question 38

> [!INDICATION]
> Faites de l’activité de l’ion oxonium la variable positive à optimiser.

> [!INDICATION]
> Dérivez la somme complète avant d’introduire les deux températures.

#### Solution

On minimise $s/c^\circ=K_4h^2+K_4K_5+K_{s3}/h$ pour $h>0$. La dérivée en $h$ vaut $2K_4h-K_{s3}/h^2$. Elle change de négative à positive une seule fois, pour $h_*^3=K_{s3}/(2K_4)$. Le pH correspondant est
$$\boxed{\mathrm pH_*=\frac13\log\left(\frac{2K_4}{K_{s3}}\right).}$$
Avec la loi de $\mathrm pK_4(T)$ et $K_{s3}$ supposée constante, on trouve **$\mathrm pH_*\simeq7{,}20$ à $300\,^\circ\mathrm C$ et $\simeq9{,}05$ à $90\,^\circ\mathrm C$**.

> [!METHODE]
> Un terme constant contribue à la solubilité mais disparaît lorsqu’on cherche le minimum par dérivation. Les deux termes variables fixent la position du minimum.

### Question 39

> [!INDICATION]
> Comparez les minimums à chaud et à froid.

> [!INDICATION]
> Qu’arrive-t-il à la solubilité si la température change alors que le pH est maintenu au premier minimum ?

#### Solution

À $300\,^\circ\mathrm C$, choisir un pH proche de $7{,}2$ minimise la solubilité du nickel dans ce modèle et limite la remise en circulation des espèces qui en proviennent. La température d’arrêt déplace le minimum vers un pH proche de $9{,}1$. Si l’eau reste à son pH de fonctionnement en puissance, la solubilité à froid est plus grande et des produits d’activation peuvent se retrouver davantage dans l’eau ou se redéposer ailleurs. Les intervenants peuvent alors subir une irradiation externe et, en cas de transfert de matière radioactive vers les personnes, une contamination.

## Bilan

Pour établir un bilan, commencez par le système, puis distinguez stockage, source et transferts. Le choix du sens positif explique les signes avant tout calcul. Dans un écoulement, l’enthalpie regroupe l’énergie interne et le travail des forces de pression aux sections franchies.

Pour exploiter un diagramme, notez les deux propriétés qui localisent chaque état. Vérifiez ensuite le sens de parcours et les signes des variations d’enthalpie. En chimie, écrivez les quantités de matière avant les lois de conductivité et les relations d’équilibre avant de placer les frontières. Lorsque des espèces sont en proportions comparables, utilisez la somme de leurs contributions.
