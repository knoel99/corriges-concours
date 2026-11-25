# ENS Paris-Saclay · Analyse économique générale 2020 — Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

Banque ENS Paris-Saclay et ENSAI, option économique et de gestion, quatre heures. Les numéros suivent le sujet de la session. Aucun rapport distinct de cet écrit n’est identifié sur la page d’annales de la session.

Le revenu et les prix du sujet sont exprimés dans son numéraire fictif. Garder d’abord des variables littérales et distinguer panier continu, panier entier et richesse aléatoire. Les probabilités et les prix de la loterie relèvent de la comparaison des critères économiques.

## 1.1. Préférences de Cobb-Douglas

**Trouver un contre-exemple économique.** Pour vérifier si deux représentations sont équivalentes, comparer leurs taux marginaux de substitution au même panier ou chercher une transformation strictement croissante. En 1.1.10, élever $u$ à la puissance six élimine toutes les racines et produit un tableau de comparaison vérifiable sans calculatrice. Pour chaque $j$, la croissance de $u$ en $x$ justifie qu’un seul panier positif soit retenu.

**1.1.1. Exposants égaux à un demi.** Les deux biens ont le même poids relatif. À l’optimum intérieur, la dépense se partage en deux moitiés. Les quantités peuvent différer si les prix diffèrent.

**1.1.2. Exposants égaux à $3/2$.** La nouvelle fonction est le cube de celle de la première question, transformation strictement croissante. Les préférences sont identiques. Les exposants d’une fonction d’utilité ordinale ne doivent pas nécessairement sommer à un.

**1.1.3. Exposants $1/4$ et $1/3$.** Le rapport des exposants devient $3/4$ au lieu de 1. Ainsi au panier $(1,1)$, la disposition marginale à céder du bien $y$ pour une unité de $x$ vaut $3/4$, contre 1 auparavant. L’ordre est différent.

**1.1.4. Programme.** Maximiser $u=x^\alpha y^\beta$ sous $x,y\ge0$, $p_xx+p_yy\le R$. Les deux biens étant désirables et $R,p_x,p_y>0$, l’optimum est intérieur avec budget saturé. Le lagrangien est $L=x^\alpha y^\beta+\lambda(R-p_xx-p_yy)$.

**1.1.5. Multiplicateur.** À l’optimum, $\lambda=\partial V/\partial R$ mesure le supplément marginal d’utilité associé à une unité de numéraire selon la représentation choisie. Une transformation croissante peut en modifier la valeur numérique.

**1.1.6. Demandes.** Les conditions $\alpha u/x=\lambda p_x$ et $\beta u/y=\lambda p_y$ donnent $p_xx:p_yy=\alpha:\beta$. Posons $A=\alpha/(\alpha+\beta)$, $B=1-A$. Alors $x=AR/p_x$ et $y=BR/p_y$.

**1.1.7. Parts.** Les parts budgétaires sont $A$ et $B$ pour tout $R$. La hausse de revenu accroît proportionnellement les deux quantités. Cette hypothèse homothétique peut convenir à deux biens sur une gamme étroite de revenus, mais rend difficile la description de parts de dépenses essentielles qui diminuent avec le niveau de vie.

**1.1.8. Valeur indirecte.** $V(p_x,p_y,R)=(AR/p_x)^\alpha(BR/p_y)^\beta$.

**1.1.9. Interprétation.** Dans ce problème de choix certain, $V$ représente ordinalement les préférences sur les situations de prix et de revenu. Pour toute fonction strictement croissante $f$, la représentation $f(u)$ conduit à $f(V)$ et au même choix. Les différences ou rapports d’utilité n’acquièrent pas de signification indépendante du choix de l’échelle.

**1.1.10.1. Exposants $1/2$ et $1/3$.** Les parts valent $3/5$ et $2/5$. Avec les prix 80 et 200, $x=3R/400$, $y=R/500$. Au revenu 1 000 le choix continu est $(7{,}5,2)$.

**1.1.10.2. Choix entier.** Pour chaque entier $j$ admissible pour $y$, prendre $x=\lfloor(R-200j)/80\rfloor$. Il suffit ensuite de comparer $u^6=x^3j^2$. Arrondir séparément les deux demandes pourrait violer la contrainte ou éliminer un meilleur panier.

**1.1.10.3 et 1.1.10.4. Comparaison exacte.** Pour $j=0$ ou $j=5$, l’un des biens manque et l’utilité est nulle aux deux revenus. Les quatre candidats restants sont les suivants.

| $j$ | $x$ pour 1 000 | $x^3j^2$ | $x$ pour 1 050 | $x^3j^2$ |
|---|---:|---:|---:|---:|
| 1 | 10 | 1 000 | 10 | 1 000 |
| 2 | 7 | 1 372 | 8 | 2 048 |
| 3 | 5 | 1 125 | 5 | 1 125 |
| 4 | 2 | 128 | 3 | 432 |

Le panier $(7,2)$ coûte 960 et laisse 40 au premier revenu. Le panier $(8,2)$ coûte 1 040 et laisse 10 au second. Ces restes ne permettent aucun achat unitaire supplémentaire.

![Figure 1 — Pour chaque quantité entière de y, on compare le meilleur x finançable.](figures/entiers.svg)

## 1.2. Préférences CES

**Contrôler la dualité.** L’indice $P$ doit être homogène de degré un dans les prix. Multiplier simultanément les deux prix par deux doit doubler la dépense nécessaire à utilité fixée. Dans le cas de la forme imprimée avec exposant supérieur à un, tenter la comparaison du panier intérieur obtenu formellement avec un panier sur un axe montre pourquoi l’hypothèse de convexité des préférences intervient.

**1.2.1. Élasticité de substitution.** À utilité constante, l’élasticité mesure la réaction proportionnelle du rapport $x/y$ à celle du prix relatif $p_y/p_x$ le long des tangences. Pour le cas usuel $\rho<1$, $\rho\ne0$, le TMS est $(x/y)^{\rho-1}$. La condition intérieure donne $x/y=(p_y/p_x)^\sigma$, où $\sigma=1/(1-\rho)>0$. L’élasticité est indépendante du panier.

**1.2.2. Minimisation.** Pour $\bar u>0$, minimiser $p_xx+p_yy$ sur les paniers non négatifs vérifiant $(x^\rho+y^\rho)^{1/\rho}\ge\bar u$. La contrainte est saturée. Pour $\rho<0$, retenir le domaine positif ou prolonger l’utilité par sa limite sur les axes.

**1.2.3. Demandes hicksiennes.** Posons $P=(p_x^{1-\sigma}+p_y^{1-\sigma})^{1/(1-\sigma)}$. La tangence donne $x=t p_x^{-\sigma}$, $y=t p_y^{-\sigma}$. En reportant dans la contrainte d’utilité, on obtient $t=\bar u P^\sigma$. Les demandes compensées sont donc $h_x=\bar u(P/p_x)^\sigma$ et $h_y=\bar u(P/p_y)^\sigma$.

**1.2.4. Dépense.** Puisque $P^{1-\sigma}=p_x^{1-\sigma}+p_y^{1-\sigma}$, la somme des deux dépenses est $E(p,\bar u)=\bar u P$.

**1.2.5. Valeur indirecte.** Inverser $R=\bar u P$ donne $V=R/P$.

**1.2.6. Demandes ordinaires.** Substituer la valeur indirecte aux demandes hicksiennes donne $x=R P^{\sigma-1}p_x^{-\sigma}$ et $y=R P^{\sigma-1}p_y^{-\sigma}$. Leur coût est bien $R$.

Le sujet indique seulement $\rho\ne1$. À $\rho=0$, l’expression imprimée comporte une division par zéro. La limite Cobb-Douglas demande une normalisation préalable, par exemple des poids $1/2$ dans la somme. Pour $\rho>1$, la fonction est convexe et la tangence intérieure ne minimise pas le coût. Comme $(x^\rho+y^\rho)^{1/\rho}\le x+y$, le coût minimum pour atteindre $\bar u$ est $\bar u\min(p_x,p_y)$, atteint en concentrant toute la consommation sur le bien le moins cher. L’utilité indirecte est $R/\min(p_x,p_y)$ et la demande correspond au coin de dépense totale sur ce bien. À prix égaux, les deux coins conviennent.

![Figure 2 — L’homogénéité de degré un permet de passer directement du coût unitaire à la dépense et à l’utilité indirecte.](figures/dualite.svg)

## 2.1 et 2.2. Critères d’espérance et de variance

**Séparer les deux côtés du contrat.** L’acheteur reçoit $L$ et paie $p$, tandis que le vendeur reçoit $p$ et doit $L$. Leurs richesses totales s’additionnent à une constante. En revanche, chacun supporte séparément une variance de 500. Pour interpréter une réponse chiffrée, préciser si elle donne une condition de financement, une indifférence en espérance ou un seuil selon l’utilité spécifiée.

Écrivons $L=60$ avec probabilité $1/6$ et $L=0$ sinon. Le prix certain du contrat est $p$. Dans le modèle de l’énoncé, le vendeur dispose de 60 unités initiales et le premier acheteur de 40.

**2.1.1 et 2.1.2. Espérance et prix vendeur.** $\mathbb E[L]=10$. Le vendeur neutre au risque compare sa richesse certaine initiale à $60+p-10$. Il est indifférent à $p=10$ et accepte un prix supérieur ou égal à 10.

**2.1.3. Portée du critère.** Il convient à une utilité affine de la richesse. Il néglige l’étendue des pertes possibles, les contraintes de financement et l’intérêt d’atteindre un seuil de consommation indivisible.

**2.1.4. Prix acheteur.** Avec maximisation de la richesse espérée, $40-p+10\ge40$ impose $p\le10$. Si l’objectif est exclusivement de pouvoir financer le bien indivisible de prix 80 dans l’état favorable, il faut aussi $40-p+60\ge80$, soit $p\le20$. Ce dernier chiffre est un plafond de faisabilité pour le projet. Une préférence qui valoriserait uniquement la probabilité d’atteindre le seuil pourrait justifier un paiement allant jusqu’à 20. Le seul qualificatif « rationnel » ne fixe pas une utilité du risque.

**2.2.1. Richesse du vendeur.** $W_v=60+p-L$ donne $\mathbb E[W_v]=50+p$.

**2.2.2. Variance.** Le prix étant certain, $\operatorname{Var}(W_v)=\operatorname{Var}(L)=60^2(1/6)(5/6)=500$.

**2.2.3. Préférence pour le risque.** À espérance fixée, $k<0$ pénalise la dispersion, $k>0$ la valorise et $k=0$ la laisse sans effet. Cette lecture concerne le critère espérance-variance spécifié.

**2.2.4. Pour $k=-0{,}05$.** La condition de vente $50+p+500k\ge60$ donne $p_v^{min}=10-500k=35$. Le prix est payable sur les 40 unités de l’acheteur, mais un gain de 60 porterait sa richesse finale seulement à 65. Le but d’atteindre 80 resterait hors d’atteinte.

**2.2.5. Pour $k=-0{,}01$.** $p_v^{min}=15$. Dans l’état favorable, la richesse de l’acheteur serait 85. Le seuil devient accessible. Il reste à déterminer son propre prix de réservation.

**2.2.6. Pour $k=0{,}01$.** $p_v^{min}=5$. Le vendeur qui valorise la dispersion accepte moins que le coût espéré de 10. Au prix de 5, le seuil visé par l’acheteur serait atteint dans l’état favorable.

**2.2.7.1. Prix de réservation de l’acheteur averse au risque.** $W_a=40-p+L$ donne $\mathbb E[W_a]=50-p$ et la même variance de 500. Pour $k=-0{,}01$, son critère vaut $45-p$, à comparer à 40. Il ne consent donc à payer que $p\le5$.

**2.2.7.2. Accord.** Aux probabilités annoncées, le prix maximal de 5 est inférieur au minimum de 15 demandé par le vendeur. Aucun prix ne satisfait les deux participations.

**2.2.7.3. Signification d’une probabilité différente.** Notons $q$ la probabilité réelle du versement de 60. Si les deux parties la connaissent, les seuils valent $60q+36q(1-q)$ pour le vendeur et $60q-36q(1-q)$ pour l’acheteur. Ils sont incompatibles pour tout $0<q<1$. L’hypothèse de tromperie de la question rompt précisément cette information commune. Si l’acheteur reste au plafond de 5 obtenu avec sa croyance initiale, la condition mathématique du vendeur devient $96q-36q^2\le5$. Sur $[0,1]$, elle équivaut à $q\le(8-\sqrt{59})/6$, soit environ 5,31 %. Le prétendu accord provient d’une sous-estimation de la perte par l’acheteur. Le calcul ne décrit aucun bénéfice mutuel sous information exacte.

![Figure 3 — Le paiement contractuel est certain. Le gain du client et la perte associée du vendeur sont aléatoires.](figures/aleas.svg)

## 2.3. Utilité espérée exponentielle

**Vérifier les signes.** Dans l’utilité du vendeur, la perte aléatoire $-L$ entre dans l’exposant avec un signe positif. L’acheteur présente le signe opposé. On peut contrôler la solution en remplaçant la loterie par un versement certain de 10. Les deux prix doivent alors redevenir 10 pour toute valeur de $\delta$.

Les deux agents détiennent initialement 60 et leur utilité de la richesse est $u(w)=-e^{-\delta w}$, $\delta>0$. Les valeurs ci-dessous sont les prix de réservation au sens de cette utilité, avec dé équilibré.

**2.3.1. Prix minimal du vendeur.** À l’indifférence entre vendre et conserver sa richesse initiale,

$$
-e^{-\delta(60+p)}\left(\frac56+\frac16 e^{60\delta}\right)=-e^{-60\delta}.
$$

On en déduit $p_v^{min}=\delta^{-1}\ln[(5+e^{60\delta})/6]$. Une vente au-dessus de ce prix est acceptée. Dans l’état du versement, le vendeur conserve $p$ unités.

**2.3.2. Prix maximal de l’acheteur.** Sa richesse est $60-p+L$. L’indifférence donne $e^{\delta p}[(5+e^{-60\delta})/6]=1$, d’où $p_a^{max}=-\delta^{-1}\ln[(5+e^{-60\delta})/6]$. La stricte convexité de l’exponentielle donne $p_a^{max}<10<p_v^{min}$. Quand $\delta$ tend vers zéro, les deux expressions tendent vers le gain moyen de 10. La richesse initiale disparaît des seuils en raison de l’aversion absolue au risque constante de l’utilité exponentielle.

[Sujet officiel](https://ens-paris-saclay.fr/sites/default/files/CONCOURS/ANNALES_1C/1C_D2_1/2020/2020_Sujet_1A_D2-1_Analyse-Eco.pdf)
