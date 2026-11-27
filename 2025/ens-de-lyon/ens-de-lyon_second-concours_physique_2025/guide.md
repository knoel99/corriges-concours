# ENS de Lyon, second concours universitaire — Physique 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · modèle exact non renseigné (famille GPT-6) · effort non renseigné · vitesse non renseignée

**Révision** · modèle exact non renseigné (famille GPT-6) · effort non renseigné · vitesse non renseignée

**Révision (tour 2)** · GPT-6.2 Astra Ultra · vitesse non renseignée

**Révision (tour 3)** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

[Sujet et figures officiels](https://banques-ecoles.fr/cms/wp-content/uploads/2025/07/25_2cc_sujet_phys.pdf) · [Rapport du jury de l’écrit](https://banques-ecoles.fr/cms/wp-content/uploads/2025/07/25_2cc_rap_ePhy.pdf)

## Présentation du sujet

Cette composition de trois heures autorise la calculatrice. Le rapport du jury attribue 20 % de la note au questionnaire et demande des réponses concises. Le problème suit l’énergie de l’air et du cylindre jusqu’à la surface humide, puis étudie le délai nécessaire pour que le refroidissement atteigne le centre.

## Partie A — Questionnaire de physique

### Question A1

> [!INDICATION]
> Imaginez quel volume de fluide occupait la place de la partie immergée.

##### Solution

Un corps plongé dans un fluide au repos reçoit de ce fluide une poussée opposée au poids du fluide déplacé, appliquée au centre de gravité du fluide déplacé. Dans un fluide homogène en pesanteur uniforme, celui-ci coïncide avec le centre géométrique du volume immergé.

### Question A2

> [!INDICATION]
> Précisez la variable spectrale avant de placer le maximum.

##### Solution

Par unité de longueur d’onde, le spectre solaire hors atmosphère a pour enveloppe celle d’un corps noir proche de $5\,800\,\mathrm K$. Il culmine vers $0{,}50\,\mu\mathrm m$ dans le visible puis décroît vers l’infrarouge. Des raies d’absorption se superposent au spectre continu.

![Figure 1 — Enveloppe de Planck à 5 780 K, par unité de longueur d’onde. Les raies solaires ne sont pas représentées.](figures/spectre-par-longueur-onde.svg)

### Question A3

> [!INDICATION]
> Quel est le devenir d’un projectile lancé exactement à la vitesse limite ?

##### Solution

C’est la vitesse minimale initiale permettant à un corps, lancé depuis un point donné et soumis uniquement à la gravitation terrestre, d’atteindre l’infini avec une vitesse finale nulle. À la surface, $v_{\rm lib}=\sqrt{2GM_T/R_T}\simeq11{,}2\,\mathrm{km\,s^{-1}}$.

### Question A4

> [!INDICATION]
> Situez les rayons par rapport à l’axe du système.

##### Solution

Les rayons restent proches de l’axe optique et font avec lui de petits angles. Les relations de l’optique paraxiale sont alors écrites au premier ordre.

### Question A5

> [!INDICATION]
> Précisez les paramètres de la géométrie et du matériau.

##### Solution

$C=\varepsilon_0\varepsilon_r S/d$ pour deux armatures parallèles d’aire commune $S$, séparées d’une distance $d$ par un diélectrique homogène, en négligeant les effets de bord.

### Question A6

> [!INDICATION]
> Reliez la contrainte tangentielle au gradient transversal de vitesse.

##### Solution

Pour un cisaillement simple $v_x(y)$ d’un fluide newtonien, $\tau_{xy}=\eta\,\partial v_x/\partial y$, où $\eta$ est la viscosité dynamique en $\mathrm{Pa\,s}$.

### Question A7

> [!INDICATION]
> Quels champs doivent être corrélés au niveau des deux ouvertures ?

##### Solution

La cohérence spatiale mesure la corrélation de phase entre les champs reçus en deux points distincts à un même instant. Une phase relative stable permet de former des franges contrastées lorsque ces champs sont recombinés avec des intensités comparables.

### Question A8

> [!INDICATION]
> Distinguez l’entropie échangée et celle créée à l’intérieur.

##### Solution

Pour un système fermé, $\Delta S=S_{\rm éch}+S_{\rm créée}$ avec $S_{\rm créée}\ge0$, nulle pour une transformation réversible. Pour un système isolé, $\Delta S\ge0$.

### Question A9

> [!INDICATION]
> Distinguez le terme cinématique et la force d’inertie.

##### Solution

L’accélération de Coriolis dans la composition des accélérations est $\mathbf a_C=2\boldsymbol\Omega\times\mathbf v_{\rm rel}$. La force d’inertie correspondante dans le repère tournant est $-m\mathbf a_C$.

### Question A10

> [!INDICATION]
> Quelle direction est perpendiculaire au courant et au champ magnétique ?

##### Solution

Dans un conducteur parcouru par un courant et soumis à un champ magnétique transverse, la déviation des porteurs de charge engendre une tension transverse, appelée tension de Hall.

## Partie B — Principe de fonctionnement d’un réfrigérateur du désert

### Considérations préliminaires

#### Question B1

> [!INDICATION]
> Identifiez l’énergie nécessaire au changement d’état d’un kilogramme d’eau.

##### Solution

La vaporisation prélève l’enthalpie massique de vaporisation $L_V=h_{\rm vapeur}-h_{\rm liquide}>0$ par kilogramme d’eau évaporé. C’est ce prélèvement d’énergie au voisinage de la surface humide qui refroidit le cylindre.

#### Question B2

> [!INDICATION]
> Distinguez l’apport thermique de l’air et le transport de vapeur.

##### Solution

L’air échange de la chaleur sensible avec la surface humide par convection naturelle ou forcée. Lorsque la surface est plus froide, cet apport est dirigé de l’air vers le tissu. En même temps, de la vapeur d’eau est transférée du tissu à l’air et emporte l’enthalpie de vaporisation.

#### Question B3

> [!INDICATION]
> Repérez le lieu où l’énergie est prélevée par le changement d’état.

##### Solution

Pendant le refroidissement, la température décroît du centre jusqu’au tissu et croît ensuite du tissu jusqu’à $T_0$ dans l’air. La température admet un minimum au tissu, avec une tangente horizontale sur l’axe par symétrie. Dans le cylindre, le flux diffusif va vers les $r$ croissants. Dans l’air, la chaleur sensible va en sens inverse vers le tissu. Les deux flux alimentent la vaporisation.

![Figure 2 — Profil qualitatif à un instant intermédiaire. Les flèches indiquent les flux de chaleur sensible.](figures/profil-radial-et-flux.svg)

#### Question B4

> [!INDICATION]
> L’axe répond-il immédiatement à un changement du flux en surface ?

##### Solution

Le centre part de $T_0$. Le refroidissement se fait d’abord sentir près de la paroi, de sorte que la température centrale varie très lentement au début. Elle décroît ensuite et tend vers un palier $T_{\rm stat}<T_0$, avec une pente qui tend vers zéro.

![Figure 3 — Réponse normalisée pour hR/λ = 5, avec un tissu sans stockage sensible. Les deux courbes tendent vers le même palier.](figures/retard-thermique-du-centre.svg)

#### Question B5

> [!INDICATION]
> Examinez la concentration en vapeur juste au-dessus du tissu.

##### Solution

Au voisinage d’une surface humide, l’air s’enrichit en vapeur. La ventilation renouvelle cette couche d’air et réduit l’épaisseur de la couche limite. L’air plus sec garde un écart de concentration avec la surface et le flux de vapeur augmente.

### Champ de température dans le cylindre

#### Question B6

> [!INDICATION]
> Le matériau qui transporte la chaleur peut-il se déplacer dans le modèle ?

##### Solution

Au sein du cylindre solide, le transfert thermique se fait par conduction. Le flux est radial par axisymétrie et invariance selon $z$.

#### Question B7

> [!INDICATION]
> Quel sens de transfert est compatible avec la production d’entropie ?

##### Solution

Le flux thermique spontané passe d’une région chaude vers une région froide, en sens opposé à $\nabla T$. La loi $\boldsymbol\varphi=-\lambda\nabla T$ exige donc $\lambda>0$ pour un conducteur thermique. Le taux local de création d’entropie vaut $\boldsymbol\varphi\cdot\nabla(1/T)=\lambda|\nabla T|^2/T^2\ge0$.

#### Question B8

> [!INDICATION]
> Les aires des faces cylindriques intérieure et extérieure sont différentes.

##### Solution

En orientant $\varphi$ vers les $r$ croissants, la puissance qui entre à $r$ est $2\pi r\,dz\,\varphi(r,t)$. Celle qui sort à $r+dr$ est $2\pi(r+dr)\,dz\,\varphi(r+dr,t)$. Sans source volumique ni travail, l’accroissement d’énergie interne de la bague est la différence de ces puissances multipliée par $dt$ :
$$\rho c\,2\pi r\,dr\,dz\,\partial_tT\,dt=-2\pi dz\,\partial_r(r\varphi)\,dr\,dt,$$
soit $\rho c\,\partial_tT=-(1/r)\partial_r(r\varphi)$.

![Figure 4 — Les aires des surfaces qui échangent de l’énergie sont 2πr dz et 2π(r + dr) dz.](figures/bilan-sur-bague.svg)

#### Question B9

> [!INDICATION]
> Remplacez le flux radial par sa loi constitutive.

##### Solution

Comme $\varphi=-\lambda\partial_rT$ et que $\lambda$ est uniforme et constante, le bilan donne
$$\partial_tT=D\,\frac1r\partial_r(r\partial_rT),\qquad D=\frac{\lambda}{\rho c}>0.$$
La diffusivité thermique $D$ s’exprime en $\mathrm{m^2\,s^{-1}}$.

#### Question B10

> [!INDICATION]
> Lisez l’ordre en temps et en espace puis examinez le centre et la surface.

##### Solution

Il faut **une condition initiale** $T(r,0)=T_0$ et **deux conditions spatiales**. La régularité sur l’axe impose $\partial_rT(0,t)=0$. À $r=R$, un bilan entre le flux issu du cylindre, la chaleur reçue de l’air et la chaleur de vaporisation fixe la condition de surface.

#### Question B11

> [!INDICATION]
> La réserve humide est prise sans capacité thermique sensible dans ce modèle.

##### Solution

Suivons durant $dt$ une portion de tissu et la quantité d’eau qui s’en évapore. À pression fixée, le passage d’une masse $dm_V$ du liquide à la vapeur exige l’accroissement d’enthalpie $L_Vdm_V$. On néglige le stockage sensible dans le tissu mince. Les deux puissances algébriques reçues par la portion donnent
$$(\Phi_{0/2}+\Phi_{1/2})dt=L_Vdm_V.$$
Une écriture en système ouvert donne le même résultat, la différence d’enthalpie entre vapeur sortante et eau liquide étant $L_V$.

![Figure 5 — Puissances par unité de surface. Au régime stationnaire, l’apport du cylindre s’annule.](figures/echanges-de-la-surface.svg)

### Régime stationnaire

#### Question B12

> [!INDICATION]
> Annulez la dérivée temporelle dans l’équation de diffusion.

##### Solution

En régime stationnaire, pour $0<r<R$, $\dfrac{d}{dr}\left(r\dfrac{dT}{dr}\right)=0$.

#### Question B13

> [!INDICATION]
> Intégrez d’abord le produit $rT'(r)$.

##### Solution

Une première intégration donne $rT'(r)=A$. Une seconde donne $T(r)=A\ln(r/R)+B$, le rayon $R$ rendant l’argument du logarithme sans dimension.

#### Question B14

> [!INDICATION]
> Testez la solution au centre du cylindre plein.

##### Solution

$\ln(r/R)$ diverge quand $r\to0$. La température au centre devant rester finie, **$A=0$**. Un terme logarithmique correspondrait à un flux permanent vers ou depuis une source linéique sur l’axe.

#### Question B15

> [!INDICATION]
> Utilisez le contact thermique entre le tissu et la surface.

##### Solution

À $r=R$, $T(R)=T_{2,\rm stat}$ en l’absence de résistance de contact. **$B=T_{2,\rm stat}$** et tout le cylindre est isotherme à $T_{\rm stat}=T_{2,\rm stat}$.

#### Question B16

> [!INDICATION]
> Appliquez la convection sur l’aire latérale et la conduction du côté solide.

##### Solution

Pour la portion de hauteur $a$, la surface d’échange est $S_a=2\pi Ra$. Le tissu reçoit de l’air $\Phi_{0/2}=hS_a(T_0-T_{\rm stat})>0$. Il reçoit du cylindre $\Phi_{1/2}=-\lambda S_a\partial_rT(R^-)=0$, car le cylindre est devenu isotherme.

#### Question B17

> [!INDICATION]
> Combien de kilogrammes d’eau quittent une surface $S_a$ pendant $dt$ ?

##### Solution

On a $dm_V=\alpha S_a\,dt$. Le bilan de la question 11 devient $hS_a(T_0-T_{\rm stat})=L_V\alpha S_a$, d’où
$$T_{\rm stat}=T_0-\frac{\alpha L_V}{h}.$$
La différence $\alpha L_V/h$ est en kelvins. L’aire et la hauteur $a$ disparaissent, puisque le débit évaporé et la puissance thermique reçue de l’air sont tous deux proportionnels à la même aire mouillée.

#### Question B18

> [!INDICATION]
> Convertissez d’abord l’enthalpie massique en joules par kilogramme.

##### Solution

$L_V=2{,}4\times10^6\,\mathrm{J\,kg^{-1}}$ donne $\alpha L_V=360\,\mathrm{W\,m^{-2}}$. L’écart stationnaire est **$\Delta T_{\rm stat}=360/30=12\,\mathrm K$**, soit une différence de $12\,{}^\circ\mathrm C$.

#### Question B19

> [!INDICATION]
> La ventilation agit sur deux coefficients de transfert.

##### Solution

La ventilation augmente généralement le taux d’évaporation $\alpha$ et le coefficient de convection thermique $h$. L’écart stationnaire est proportionnel à leur **rapport** $\alpha/h$. Les seules données ne permettent donc pas d’affirmer dans quel sens varie le palier. Si les transferts de chaleur et de masse augmentent dans des proportions comparables, le palier peut peu varier alors que le refroidissement s’accélère.

#### Question B20

> [!INDICATION]
> Comparez des puissances surfaciques évacuées par les deux liquides.

##### Solution

L’écart dépend du produit $\alpha L_V$ rapporté à $h$. L’éther, plus volatil, peut avoir un débit d’évaporation beaucoup plus élevé que celui de l’eau. À $h$ identique, une augmentation de $\alpha$ d’un facteur supérieur à $6{,}7$ suffit à compenser sa plus faible chaleur latente et à donner un écart supérieur.

### Régime transitoire

#### Question B21

> [!INDICATION]
> Le terme stationnaire est constant. Divisez l’équation par la partie séparable.

##### Solution

Avec $T-T_{\rm stat}=T^\star fg$, les dérivées en temps et en espace donnent $T^\star f g'=D T^\star g(r f')'/r$. Comme $f$ et $g$ sont non nulles, on en déduit $g'/g=D(rf')'/(rf)$.

#### Question B22

> [!INDICATION]
> Les deux membres dépendent de variables indépendantes. Interprétez la valeur commune.

##### Solution

Pour tout $r,t$ intérieur, le terme de gauche dépend seulement de $t$ et celui de droite seulement de $r$. Leur valeur commune est une constante $-K$. Ainsi $g'+Kg=0$, $g(0)=1$ donnent $g(t)=e^{-Kt}$. Puisque ce mode doit s’effacer quand $t\to\infty$, $K>0$, de dimension $\mathrm{s^{-1}}$.

#### Question B23

> [!INDICATION]
> Construisez un temps à partir du rayon et de la diffusivité.

##### Solution

L’échelle diffusive donne $K\sim D/R^2=\lambda/(\rho cR^2)$. Un calcul des modes du problème avec la condition en surface affine cette loi en $K=(D/R^2)\,\mu^2$, où $\mu$ est sans dimension et dépend notamment du nombre de Biot $hR/\lambda$. Le taux d’évaporation constant fixe le palier de température. En effet, après soustraction de $T_{\rm stat}$, le bilan de surface devient $-\lambda\partial_r(T-T_{\rm stat})=h(T-T_{\rm stat})$ en $R$.

#### Question B24

> [!INDICATION]
> Vérifiez que le rayon est bien exprimé en mètres avant de le mettre au carré.

##### Solution

$D=0{,}6/(1000\times4200)=1{,}43\times10^{-7}\,\mathrm{m^2\,s^{-1}}$. En négligeant le facteur adimensionné, $1/K\sim R^2/D=7{,}0\times10^4\,\mathrm s\simeq19{,}4\,\mathrm h$. Le cœur d’un assemblage de dix centimètres de rayon se refroidit donc sur une échelle de plusieurs heures. Cette estimation donne une échelle diffusive, et non une durée exacte de mise au palier.

#### Question B25

> [!INDICATION]
> Dans l’équation séparée, remplacez $d/dr$ par $R^{-1}d/dX$.

##### Solution

La dépendance radiale vérifie $(rf')'+(K/D)rf=0$. Avec $X=r/R$ et $Q(X)=f(r)$, on obtient
$$Q''+\frac1XQ'+\frac{KR^2}{D}Q=0\quad(0<X\le1),\qquad Q(0)=1,\quad Q'(0)=0.$$
C’est l’équation de Bessel d’ordre zéro à argument $\sqrt{KR^2/D}\,X$. La condition de surface sélectionne les valeurs admissibles de $K$.

Le temps du mode le plus lent peut être calculé dans le cas du tissu sans stockage thermique. La solution régulière de l’équation de Bessel est $Q(X)=J_0(\mu X)$ avec $\mu^2=KR^2/D$. En $X=1$, la condition d’échange conduit à $\mu J_1(\mu)=\mathrm{Bi}\,J_0(\mu)$ où $\mathrm{Bi}=hR/\lambda$. Les données du sujet donnent $\mathrm{Bi}=5$. La plus petite racine positive est $\mu_1\simeq1{,}990$, d’où $1/K_1\simeq19{,}4/1{,}990^2\simeq4{,}9\ \mathrm h$. Les 19 h demandées à la question 24 représentent l’échelle diffusive brute. Le mode de 4,9 h décrit la pente de fin de refroidissement du modèle, quand les autres modes se sont amortis.

#### Question B26

> [!INDICATION]
> Que devrait valoir la fonction radiale à l’instant initial si un seul mode suffisait ?

##### Solution

À $t=0$, le champ initial est uniforme. L’identité $T_0-T_{\rm stat}=T^\star f(r)g(0)$ et les normalisations donnent $T^\star=T_0-T_{\rm stat}$ puis $f(r)=1$ partout. Or le membre radial de l’équation séparée est alors nul, donc $K=0$, incompatible avec une décroissance. Une **superposition de plusieurs modes** permet de reproduire le champ initial uniforme. En posant $X=r/R$, $\mathrm{Fo}=Dt/R^2$ et $\Theta=(T-T_{\rm stat})/(T_0-T_{\rm stat})$, on peut écrire la série $\Theta=\sum_n b_nJ_0(\mu_n X)e^{-\mu_n^2\mathrm{Fo}}$. Les poids se déduisent de la projection du profil initial $1$ sur chaque mode, avec le poids d’aire $X\,dX$ dans la section du cylindre. Les trois premiers valent environ $1{,}503$, $-0{,}797$ et $0{,}484$. Au temps initial, les modes suivants sont encore nécessaires. À temps long, seul le mode le plus lent contribue sensiblement.

![Figure 6 — Trois premiers modes pour hR/λ = 5. Le profil initial uniforme se reconstruit par la série complète pondérée.](figures/modes-radiaux.svg)

## Bilan

La chaleur latente fixe la puissance prélevée par l’évaporation. Au régime stationnaire, l’air fournit entièrement cette puissance et le cylindre est isotherme. Pendant le refroidissement, l’écart entre le centre et le tissu entraîne une diffusion radiale. L’échelle R²/D fixe un temps caractéristique, tandis que la condition d’échange en surface détermine les taux de décroissance précis.
