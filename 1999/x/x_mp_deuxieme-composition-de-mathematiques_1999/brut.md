# École polytechnique — Deuxième composition de mathématiques MP 1999 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée

On note $\mathcal E=\mathbb R\setminus\mathbb Q$, $E(x)=\lfloor x\rfloor$ et $G=\mathrm{GL}_2(\mathbb Z)$. La question finale demande une suite pour tout irrationnel. La restriction $u_0\in\mathbb N$ imprimée en partie III impose une précision pour les irrationnels négatifs.

## I. Quotients d’une récurrence constante

### Question 1

Soient $s=(\alpha+\sqrt{\alpha^2+4})/2$ et $t=(\alpha-\sqrt{\alpha^2+4})/2$. Ce sont les racines distinctes de $X^2-\alpha X-1$. Les conditions $q_0=1$, $q_1=\alpha=s+t$ donnent $q_n=(s^{n+1}-t^{n+1})/(s-t)$. Or $q_1=p_0$, $q_2=\alpha^2+1=p_1$ et les récurrences coïncident. Ainsi $p_n=q_{n+1}=(s^{n+2}-t^{n+2})/(s-t)$.

### Question 2

Comme $s>1$ et $t=-1/s$, $|t/s|<1$. On trouve $p_n/q_n=s(1-(t/s)^{n+2})/(1-(t/s)^{n+1})\to s$. Ainsi $\lambda=(\alpha+\sqrt{\alpha^2+4})/2$.

### Question 3

$X^2-\alpha X-1$ est unitaire à coefficients entiers et à terme constant $-1$, donc ses seules racines rationnelles possibles sont $\pm1$. Ni $1$ ni $-1$ ne conviennent pour $\alpha>0$. Donc $\lambda$ est irrationnel.

## II. Transformations homographiques des irrationnels

### Question 4

Soit $P$ un annulateur unitaire de degré minimal de $x$. Il a degré au moins deux puisque $x$ est irrationnel. Le reste de la division de tout autre annulateur par $P$ annule encore $x$ et a degré plus petit, donc est nul. Une factorisation non triviale de $P$ fournirait un facteur annulateur de plus petit degré. Ainsi $P$ est irréductible. Tout annulateur unitaire irréductible est divisible par $P$, donc lui est égal. Cela définit $P_x$ et $d_x$.

### Question 5.a

Pour $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in G$, le dénominateur $cx+d$ ne s’annule pas en un irrationnel, la ligne $(c,d)$ étant non nulle. Si $(ax+b)/(cx+d)=r\in\mathbb Q$, alors $(a-rc)x=rd-b$. Si $a-rc\ne0$ on a $x\in\mathbb Q$, sinon $a=rc$ et $b=rd$, ce qui annule le déterminant. Les deux possibilités sont exclues.

### Question 5.b

La composition donne $T_g\circ T_h=T_{gh}$ en développant numérateur et dénominateur, et $T_I$ est l’identité. Comme $g^{-1}\in G$, $T_{g^{-1}}$ est la bijection inverse. Dans le noyau, $cx^2+(d-a)x-b=0$ pour tout irrationnel. Ce polynôme est identiquement nul, donc $c=b=0$ et $d=a$. Le déterminant $a^2=\pm1$ force $a=\pm1$. Le noyau est $\{I,-I\}$.

### Question 6

Si $y=T_g(x)$, alors $y\in\mathbb Q(x)$ et $x=T_{g^{-1}}(y)\in\mathbb Q(y)$. Ainsi $\mathbb Q(x)=\mathbb Q(y)$. Ce corps a pour dimension $d_x$ puisque les puissances $1,\ldots,x^{d_x-1}$ forment une base par division modulo $P_x$ et irréductibilité. Tout élément en est algébrique par dépendance des puissances. La même description pour $y$, irrationnel par 5.a, donne $d_y=d_x$.

### Question 7

Soit $y=T_g(\sqrt m)$ avec $y^2=N\in\mathbb Z$. Comme $y$ est réel irrationnel, $N>0$ et $X^2-N$ est son polynôme minimal. En exprimant $\sqrt m=(dy-b)/(a-cy)$ on obtient le polynôme annulateur
$$
H(Y)=(dY-b)^2-m(a-cY)^2.
$$
Son coefficient dominant $d^2-mc^2$ est non nul puisque $m$ n’est pas un carré et $(c,d)\ne(0,0)$. La forme homogène $(dY-bZ)^2-m(aZ-cY)^2$ est primitive. En effet, la substitution entière utilisée a déterminant $ad-bc=\pm1$, donc possède une substitution inverse entière. Tout diviseur commun des nouveaux coefficients diviserait ceux de la forme initiale $Y^2-mZ^2$. Puisque $X^2-N$ divise $H$, on a alors $H=\pm(X^2-N)$ par primitivité. Son discriminant est $4m(ad-bc)^2=4m$ par développement, et également $4N$. Donc $N=m$ et $y=\pm\sqrt m$. Les deux valeurs sont obtenues avec $I$ et $\operatorname{diag}(-1,1)$.

## III. Convergentes à quotients partiels variables

### Question 8

Écrivons $B_n=A(u_0)\cdots A(u_n)$, $v_n=(p_n,q_n)^{\mathsf T}$. Le deuxième vecteur colonne de $B_n$ est le premier de $B_{n-1}$, donc $B_n=(v_n,v_{n-1})$ pour $n\ge1$. Son premier vecteur colonne vaut $u_nv_{n-1}+v_{n-2}$ si $n\ge2$, d’où les deux récurrences. Directement $v_0=(u_0,1)^{\mathsf T}$ et $v_1=(u_0u_1+1,u_1)^{\mathsf T}$.

### Question 9

Pour $n\ge1$, $p_nq_{n-1}-p_{n-1}q_n=\det B_n=(-1)^{n+1}$. Les $q_n$ sont positifs d’après leurs valeurs initiales et la récurrence. Par division, $r_n-r_{n-1}=(-1)^{n+1}/(q_nq_{n-1})$.

### Question 10.a

$q_0=1$, $q_1=u_1\ge1$ et $q_n\ge q_{n-1}+q_{n-2}$ dès $n=2$, donc $q_n\to\infty$. Le quotient $r_n$ est la moyenne de $r_{n-1}$ et $r_{n-2}$ avec les poids strictement positifs $u_nq_{n-1}$ et $q_{n-2}$. Ces deux quotients sont distincts par 9. Par conséquent les intervalles fermés entre $r_n$ et $r_{n+1}$ sont emboîtés et leurs longueurs $1/(q_nq_{n+1})$ tendent vers zéro. Ils définissent une unique limite commune $\lambda(u)$. La stricte intériorité des étapes suivantes assure qu’elle est strictement entre $r_n$ et $r_{n+1}$ pour tout $n$.

![Pour les quotients partiels tous égaux à 1, les intervalles successifs se resserrent autour du nombre d’or.](figures/intervalles-des-convergentes.svg)

### Question 10.b

Si $\lambda(u)=a/b$ avec $b\ge1$, la stricte intériorité de 10.a assure $\lambda(u)\ne r_n$. On aurait $1/(bq_n)\le|\lambda(u)-r_n|<1/(q_nq_{n+1})$, donc $q_{n+1}<b$ pour tout $n$, contrairement à leur divergence. La limite est irrationnelle.

### Question 10.c

$r_0=u_0$ et $r_1=u_0+1/u_1\le u_0+1$. Donc $u_0<\lambda(u)<u_0+1$, même quand $u_1=1$, et $E(\lambda(u))=u_0$.

## IV. Décalage et périodicité

### Question 11

Si $x$ est irrationnel, $x-E(x)$ puis son inverse sont irrationnels, donc l’itération continue indéfiniment. Si $x=p/q$ est rationnel non entier avec $q>0$, écrivons $p=E(x)q+r$, $0<r<q$. Alors $F(x)=q/r$, dont le dénominateur après réduction est strictement inférieur à $q$. Une itération atteint donc un entier, où $F$ cesse d’être définie. Pour un entier initial, elle est déjà indéfinie au premier pas.

### Question 12.a

Pour $n\ge1$, $v_n=A(u_0)(p'_{n-1},q'_{n-1})^{\mathsf T}$. Par conséquent $p_n=u_0p'_{n-1}+q'_{n-1}$ et $q_n=p'_{n-1}$.

### Question 12.b

Comme $u'_0=u_1\ge1$, les quotients de la suite décalée sont positifs et $\lambda(u')>0$. L’identité $r_n=u_0+1/r'_{n-1}$ entraîne $\lambda(u)=u_0+1/\lambda(u')$. Par 10.c on en tire $F(\lambda(u))=\lambda(u')$.

### Question 12.c

Pour une période de longueur $h\ge1$, posons $B=A(u_0)\cdots A(u_{h-1})=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$. L’identité de 12.b itérée et la périodicité montrent que $\lambda=T_B(\lambda)$, donc $c\lambda^2+(d-a)\lambda-b=0$. Le coefficient $c=q_{h-1}>0$, même pour $h=1$. Le nombre étant irrationnel par 10.b, son degré ne peut être un. Son degré algébrique vaut exactement deux.

### Question 12.d

À partir d’un rang $N$, la suite décalée est périodique. Sa limite $\lambda_N$ est quadratique par 12.c. Si $N>0$, $\lambda(u)=T_{A(u_0)\cdots A(u_{N-1})}(\lambda_N)$ par 12.b. Le produit appartient à $G$, et 6 préserve le degré, donc $d_{\lambda(u)}=2$. Pour $N=0$ c’est directement 12.c.

## V. Reconstruction de l’irrationnel

### Question 13.a

Posons $x_k=F^k(x)$, $y_k=F^k(y)$, $s_k=x_k-E(x_k)$ et $t_k=y_k-E(y_k)$. Puisque les parties entières sont égales, $t_k-s_k=y_k-x_k$. Comme $x_{k+1}=1/s_k$, $y_{k+1}=1/t_k$, on a $y_k-x_k=-(y_{k+1}-x_{k+1})s_kt_k$. En répétant cette identité $n$ fois on obtient $y-x=(-1)^n(y_n-x_n)\prod_{k=0}^{n-1}s_kt_k$, exactement la formule demandée.

### Question 13.b

Les parties entières de $x_n,y_n$ étant égales, $|y_n-x_n|<1$. De plus $s_ks_{k+1}=s_{k+1}/(E(x_{k+1})+s_{k+1})<1/2$, car $x_{k+1}>1$ et $0<s_{k+1}<1$. Le même raisonnement vaut pour $t_kt_{k+1}$. Par regroupement dans 13.a, $|y-x|\le(1/4)^{\lfloor n/2\rfloor}$. D’où $x=y$.

### Question 14

Si $x>0$ est irrationnel, tous les itérés existent par 11. Posons $u_k=E(F^k(x))$. Alors $u_0\in\mathbb N$ et $u_k\ge1$ pour $k\ge1$. D’après 12.b et 10.c, les parties entières de tous les itérés de $\lambda(u)$ sont exactement ces $u_k$. La question 13.b donne $\lambda(u)=x$. Ces mêmes identités imposent chaque terme $u_k$, d’où l’unicité.

Pour $x<0$ irrationnel, la consigne finale « un nombre réel irrationnel » ne peut être satisfaite avec la restriction $u_0\in\mathbb N$ de la partie III, car 10.c impose $u_0=E(x)<0$. Si le premier terme est autorisé dans $\mathbb Z$, la même construction vaut pour tout $x$. En effet les dénominateurs, les intervalles emboîtés et l’identité de décalage ne changent pas lorsque $u_0$ est négatif. On peut aussi développer $x-E(x)$ puis ajouter $E(x)$ au premier quotient, ce qui translate toutes les convergentes de $E(x)$. L’unicité reste acquise par l’identification de chaque partie entière.
