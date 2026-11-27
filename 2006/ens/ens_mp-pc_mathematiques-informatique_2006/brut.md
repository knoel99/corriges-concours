# ENS · MP-PC · Mathématiques-informatique 2006 — corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 25 novembre 2026

**Révision** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

Le corps K est de caractéristique différente de deux. On note v la valuation en z. Lors du passage aux fractions continues, une lettre polynomiale dans une identité de séries désigne son image par la substitution x = 1/z.

## Partie 1 · Calcul dans les séries de Laurent

### Question 1.1 · Valuations et convolution

Soient $r=v(a)$, $s=v(b)$ finis. Sous $\min(r,s)$, les deux coefficients sont nuls. Si $r\ne s$, le premier coefficient pouvant intervenir dans la somme vient d’un seul opérande et est non nul. Dans le coefficient $c_i=\sum_j a_jb_{i-j}$ du produit, seuls $r\le j\le i-s$ interviennent, soit au plus $\max(0,i-r-s+1)$ termes. Au rang $r+s$, le seul terme est $a_rb_s\ne0$. Ainsi $v(ab)=r+s$. Un opérande nul donne le produit nul, de valuation infinie. Enfin $a=z^r\sum_{j\ge0}a_{j+r}z^j$ et le second facteur a valuation nulle.

La borne sur le nombre de produits est atteinte, par exemple lorsque $a_j=1$ pour tout $j\ge r$ et $b_j=1$ pour tout $j\ge s$. Il s’agit du nombre de termes non nuls avant leur addition, même si leur somme s’annule dans le corps $K$. Si l’une des séries est nulle, tous ces produits sont nuls et la somme des séries est l’autre série.

### Question 1.2 · Structure d’anneau

La somme, l’opposé et le zéro se calculent terme à terme. L’unité multiplicative est concentrée au rang zéro avec coefficient $1_K$. La commutativité du produit suit du changement $j\leftrightarrow i-j$. Pour trois facteurs, le coefficient du rang $i$ est dans les deux parenthésages la somme finie des $a_jb_kc_l$ pour $j+k+l=i$. La distributivité suit en développant chaque somme finie. Cela établit tous les axiomes.

### Question 1.3 · Inversion

Écrire $a=z^r u$, avec $u_0\ne0$. Pour $uv=1$, les coefficients imposent $v_0=u_0^{-1}$ et, pour $j\ge1$,
$$
v_j=-u_0^{-1}\sum_{i=1}^j u_i v_{j-i}.
$$
La récurrence définit une série entière de terme constant non nul. Alors $a^{-1}=z^{-r}v$ et $v(a^{-1})=-r$, où $v(\cdot)$ désigne ici la valuation.

### Question 1.4 · Inverse tronqué

Pour $k\ge1$ et $A[0]\ne0$, le programme utilise une seule inversion de scalaire.
```text
c ← inverse(A[0])
B[0] ← c
pour j de 1 à k−1
    s ← 0
    pour i de 1 à j
        s ← s + A[i] × B[j−i]
    B[j] ← −c × s
renvoyer B
```
Le coefficient du produit est nul à chaque nouveau rang par 1.3. Coût $O(k^2)$ opérations, $O(k)$ cases.

### Question 1.5 · Newton et doublement

Posons $U=z^{-2k}a$, $B_0=1$, $E_j=B_j^2-U$. Initialement $v(B_0)=0$, $v(E_0)\ge1$. Si $B_j$ a terme constant un et $v(E_j)\ge2^j$, le correctif $E_j/(2B_j)$ existe et a valuation au moins $2^j$. Ainsi $B_{j+1}$ garde son terme un et
$$
E_{j+1}=\frac{E_j^2}{4B_j^2},\qquad v(E_{j+1})\ge 2^{j+1}.
$$
La récurrence simultanée assure la définition et les deux bornes, y compris pour une erreur nulle.

### Question 1.6 · Existence de la racine

Comme $v(B_{j+1}-B_j)\ge2^j$, pour $2^j\ge n$ tous les $B_l$, $l\ge j$, ont les mêmes coefficients d’indices $0,\ldots,n-1$. Définir $B$ par ces valeurs stationnaires. Alors $v(B-B_j)\ge2^j$. Le produit $(B-B_j)(B+B_j)$ tend formellement vers zéro et $B_j^2-U=E_j$ aussi. Chaque coefficient de $B^2-U$ est donc nul. La série $b=z^kB$ vérifie $b^2=a$ et son terme initial a pour coefficient un.

![Figure 1 — Les premières itérations garantissent respectivement un, deux, quatre et huit coefficients exacts pour la racine de terme constant un.](figures/precision-newton.svg)

## Partie 2 · Convergents sur un corps

### Question 2.1 · Récurrences du numérateur et du dénominateur

Soit $M(t)=\left(\begin{smallmatrix}t&1\\1&0\end{smallmatrix}\right)$. Par multiplication à droite,
$$
M(a_0)\cdots M(a_k)=\begin{pmatrix}p_k&p_{k-1}\\q_k&q_{k-1}\end{pmatrix},
$$
avec $(p_{-1},q_{-1})=(1,0)$, $(p_0,q_0)=(a_0,1)$ et $u_i=a_i u_{i-1}+u_{i-2}$ pour $u=p,q$. En particulier $(p_1,q_1)=(a_0a_1+1,a_1)$. L’action homographique est $t\mapsto a+1/t$, d’où le convergent $p_k/q_k$ lorsque défini. Sur un corps général, des $a_i\ne0$ ne suffisent pas à empêcher un dénominateur nul, par exemple $a_1=1$, $a_2=-1$. Les couples matriciels restent définis, ou s’interprètent sur la droite projective.

### Question 2.2 · Une seule inversion

Si $k=0$, renvoyer $a_0$. Sinon initialiser $(P_0,Q_0)=(a_0,1)$, $(P_1,Q_1)=(a_0a_1+1,a_1)$.
```text
pour i de 2 à k
    (P₀,P₁) ← (P₁, aᵢ × P₁ + P₀)
    (Q₀,Q₁) ← (Q₁, aᵢ × Q₁ + Q₀)
si Q₁ = 0 : signaler le dénominateur nul
renvoyer P₁ × inverse(Q₁)
```
Pour $k\ge1$, la construction effectue $2k-1$ additions et $2k-1$ multiplications, puis une multiplication pour le quotient, soit $2k$ multiplications et une inversion.

### Question 2.3 · Différence de deux convergents

Le déterminant du produit matriciel de 2.1 vaut $(-1)^{k+1}$. Donc $p_kq_{k-1}-p_{k-1}q_k=(-1)^{k-1}$ et, pour $k\ge1$ avec dénominateurs non nuls, $C_k-C_{k-1}=(-1)^{k-1}/(q_kq_{k-1})$.

### Question 2.4 · Convergence réelle

Pour $a_i\ge1$, $q_0=1$, $q_1\ge1$, $q_{i+2}\ge q_{i+1}+q_i$. Les dénominateurs sont croissants au sens large et tendent vers l’infini. Par 2.3, $C_k=C_0+\sum_{i=1}^k(-1)^{i-1}/(q_iq_{i-1})$. Le terme positif en valeur absolue décroît vers zéro. Le critère des séries alternées assure la convergence réelle.

## Partie 3 · Fractions continues de polynômes

### Question 3.1 · Substitution et troncature

Pour $U$ de degré $d$, $v(\varphi(U))=-d$, donc $v(\varphi(1/U))=d$. La partie polynomiale $\psi$ conserve les coefficients d’indice $\le0$, puis remplace $z$ par $1/x$. Cette opération est additive. Avec $a=z$, $b=z^{-1}$, on a $\psi(ab)=1$ tandis que $\psi(a)\psi(b)=0$. Enfin $F=\varphi(\psi(F))$ équivaut à l’absence complète de termes de puissances strictement positives de $z$.

### Question 3.2 · Limite formelle des convergents

Notons $d_i=\deg q_i$. Comme $\deg a_i\ge1$ pour $i>0$, la récurrence donne $d_0=0$, $d_i=d_{i-1}+\deg a_i$ sans compensation avec $q_{i-2}$. D’après 2.3, $v(\varphi(C_i-C_{i-1}))=d_i+d_{i-1}\to\infty$. Pour chaque indice, les coefficients des convergents finissent donc par rester constants. Définissons $F$ par ces valeurs. Toutes les différences avec $C_0$ n’ont que des puissances positives, donc $F$ a un support borné inférieurement. La même stabilisation montre $v(F-\varphi(C_i))\to\infty$.

### Question 3.3 · Développer une série irrationnelle

Posons $\alpha_0=F$, $a_i=\psi(\alpha_i)$ et $\alpha_{i+1}=1/(\alpha_i-\varphi(a_i))$. Si un reste était nul ou un quotient complet rationnel, remonter les étages donnerait $F$ rationnel. Les restes ont donc valuation strictement positive et les $\alpha_i$, $i>0$, valuation strictement négative. Ainsi $\deg a_i=-v(\alpha_i)\ge1$. En appliquant la matrice de 2.1 à la queue $\alpha_{k+1}$, on a, en omettant les symboles $\varphi$,
$$
F=\frac{p_k\alpha_{k+1}+p_{k-1}}{q_k\alpha_{k+1}+q_{k-1}}.
$$
Le dénominateur a valuation $-d_k-\deg a_{k+1}=-d_{k+1}$, strictement inférieure à celle de $q_{k-1}$. Le déterminant donne $v(F-p_k/q_k)=d_k+d_{k+1}\to\infty$.

### Question 3.4 · Meilleure approximation

Posons $E_i=\varphi(p_i)-F\varphi(q_i)$. Le calcul précédent donne $v(E_i)=d_{i+1}>d_i$, aussi pour $i=0$. Les couples $(p_{k-1},q_{k-1})$, $(p_k,q_k)$ forment une base de $K[x]^2$ car leur déterminant vaut $\pm1$. Écrivons $(p,q)=a(p_{k-1},q_{k-1})+b(p_k,q_k)$.

Sous les hypothèses du troisième item, $a=0$ contredirait $\deg q<d_k$ et $b=0$ donnerait $a$ constant par coprimalité, donc $q$ proportionnel à $q_{k-1}$. Puisque $\deg q<d_k$, les termes majeurs de $aq_{k-1}$ et $bq_k$ doivent s’annuler. Ainsi $\deg a+d_{k-1}=\deg b+d_k$, donc $\deg a>\deg b$. Les valuations de $aE_{k-1}$ et $bE_k$ sont respectivement $d_k-\deg a$ et $d_{k+1}-\deg b$, la première strictement moindre. C’est la valuation cherchée.

Enfin, choisir $k$ par $d_{k-1}\le\deg q<d_k$. Si $v(\varphi(p)-F\varphi(q))>\deg q$, le polynôme $p q_{k-1}-p_{k-1}q$ a image de valuation positive. En effet, les deux termes après insertion de $Fqq_{k-1}$ ont valuations strictement positives par l’hypothèse et $v(E_{k-1})=d_k$. Il est donc nul et $p/q=p_{k-1}/q_{k-1}$. Cette preuve couvre aussi les dénominateurs proportionnels.

### Question 3.5 · Partie polynomiale de la racine

Écrivons $\deg D=2m$. Les $m+1$ coefficients de la racine formelle normalisée de $U(z)=z^{2m}D(1/z)$ suffisent, car on la multipliera par $z^{-m}$. Une récurrence triangulaire évite les séries infinies.
```text
t[0] ← 1
pour j de 1 à m
    s ← coefficient de x^(2m−j) dans D
    pour i de 1 à j−1
        s ← s − t[i] × t[j−i]
    t[j] ← s / 2
renvoyer la somme des t[j] × x^(m−j) pour j de 0 à m
```
L’identité $t(z)^2=U(z)\bmod z^{m+1}$ donne à chaque tour la formule affichée. Le degré maximal est $2m$ pour l’entrée, $m$ pour le polynôme construit. Le coût arithmétique est $O(m^2)$.

### Question 3.6 · Quotients complets sans séries infinies

Écrivons $S=\sqrt D$, $H=\psi(S)$. Initialement $P_0=0,Q_0=1$ et $Q_0\mid D-P_0^2$. Si $P'=a'Q-P$, alors $P'\equiv-P\pmod Q$. Donc $Q'=(D-P'^2)/Q$ est polynomial et non nul puisque $D$ n’est pas un carré. Il divise $D-P'^2$, d’où l’invariant au tour suivant.

Pour une série $T$, écrire $T=\varphi(\psi(T))+R$ avec $v(R)>0$. Comme $v(1/\varphi(Q))=\deg Q\ge0$, $R/\varphi(Q)$ a partie polynomiale nulle. La division euclidienne de $\psi(T)$ par $Q$ fournit donc exactement $\psi(T/\varphi(Q))$, puisque le reste divisé par $Q$ a valuation positive. On obtient $a'_k=\psi((P_k+S)/Q_k)$.

Enfin $\alpha_0=S$. Si $\alpha_k=(P_k+S)/Q_k$, l’extraction donne $a_k=a'_k$, puis
$$
\alpha_{k+1}=\frac{Q_k}{S-P_{k+1}}=\frac{P_{k+1}+S}{Q_{k+1}}.
$$
Cela achève la récurrence.

![Figure 2 — Pour D égal à x puissance quatre plus un, les quotients complets reviennent au même état dès le premier rang positif.](figures/quotients-complets.svg)

## Partie 4 · Reconnaître une primitive logarithmique

### Question 4.1 · Une norme constante

Sur l’intervalle où $D>0$, poser $S=\sqrt D$, $T=a+bS>0$. L’égalité $T'/T=h/S$ donne, après multiplication par $S$, puis séparation des parties rationnelle et irrationnelle,
$$
a'=hb,\qquad Db'+\tfrac12D'b=ha.
$$
Cette séparation est licite car un polynôme non carré n’a pas de racine rationnelle dans $\mathbb R(x)$. On obtient $(a^2-Db^2)'=0$. La constante $\mu$ est non nulle, car $a^2=Db^2$ imposerait $a=b=0$ ou $D$ carré rationnel, tous deux exclus.

### Question 4.2 · Une solution fournit un convergent

Le polynôme $b$ est non nul car $h\ne0$ et 4.1. La norme constante impose $\deg a=\deg b+m$, $2m=\deg D$, et la coprimalité de $a,b$. Choisir le signe de $a$ pour que son terme dominant soit celui de $bS$ en variable $x$. Alors $v(a+bS)=-(\deg b+m)$ et $(a-bS)(a+bS)=\mu$ donne $v(a-bS)=\deg b+m>\deg b$. Le lemme 3.4 établit que cette fraction $a/b$, après le choix de signe, est un convergent.

### Question 4.3 · Norme des convergents et quasi-périodicité

Dans 3.3 substituer $\alpha_k=(P_k+S)/Q_k$ dans l’expression de $S$ à travers les colonnes $k-1,k-2$. Noter $(p,q)=(p_{k-1},q_{k-1})$, $(r,s)=(p_{k-2},q_{k-2})$. En séparant partie rationnelle et coefficient de $S$, on a $Dq-P_kp=Q_k r$ et $p-P_kq=Q_k s$. Multiplier respectivement par $-q$ et $p$, puis additionner. Il vient
$$
p^2-Dq^2=Q_k(ps-qr)=(-1)^k Q_k .
$$
Le calcul s’applique à $k=1$ avec $(p_{-1},q_{-1})=(1,0)$. En présence de la primitive cherchée, 4.2 fournit un convergent dont le couple est proportionnel à $(\pm a,b)$, les deux couples étant premiers entre eux. Sa norme est constante, donc $Q_k=c\in\mathbb R^*$. La division suivante est exacte, $a_k=(P_k+H)/c$, d’où $P_{k+1}=H=P_1$, $Q_{k+1}=Q_1/c$. Par conséquent $\alpha_{k+1}=c\alpha_1$. Multiplier un quotient complet par $c$ multiplie sa partie polynomiale par $c$ et le quotient complet suivant par $c^{-1}$. Les $a_i$ se reproduisent donc après un décalage de $k$ avec des facteurs scalaires alternés.

### Question 4.4 · Recherche semi-décidable

Calculer $H$, puis énumérer tous les convergents $(p,q)$ à l’aide des mises à jour polynomiales de 3.6 et 2.1. Pour chaque paire, tester $(a,b)=(p,q)$ et $(-p,q)$ à l’aide des identités $a'=hb$ et $2Db'+D'b=2ha$. Vérifier aussi que $a^2-Db^2$ est une constante non nulle. Pour une paire retenue, $a+b\sqrt D$ ne s’annule nulle part sur l’intervalle. Diviser $a,b$ par sa valeur en $x_0$ pour obtenir un argument positif qui vaut un à l’origine de l’intégration. La dérivation et cette valeur initiale prouvent l’égalité voulue. Toute solution apparaît à un facteur scalaire et un signe près par 4.2, donc la recherche finit exactement dans le cas soluble.
