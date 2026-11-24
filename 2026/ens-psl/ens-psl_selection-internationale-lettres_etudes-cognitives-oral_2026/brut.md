# ENS-PSL · Sélection internationale Lettres · Études cognitives (oral) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 24 novembre 2026

L’oral demande six réponses en français sur l’article de Herman Cappelen et Josh Dever, *Introspective Machines: Are LLMs Better at Self-Reflection Than Humans?* Le candidat peut compléter en anglais. Les prises de position ci-dessous sont une proposition argumentée. [Sujet bilingue de l’ENS-PSL](https://www.ens.psl.eu/sites/default/files/cogsci_sujet-oral-sil-2026-1.pdf) [Article publié en 2025](https://doi.org/10.1111/phpe.12201) [Texte des auteurs en accès libre](https://philpapers.org/archive/CAPIMA.pdf)

### Question 1 · Quel est l’objectif principal de l’article ?

Cappelen et Dever demandent quelle valeur accorder à la parole d’un grand modèle de langage sur son propre fonctionnement cognitif. Leur exemple initial est celui de Claude, qui annonce une confiance d’environ 60 % après un problème de mathématiques et localise un doute dans son argument. Prendre ce propos au sérieux ouvrirait une source d’information sur le système. Encore faut-il établir pourquoi il a produit cette phrase et dans quelles circonstances elle mérite confiance.

Les auteurs défendent la possibilité réelle d’une introspection de machine, y compris dans des systèmes actuels, et écartent plusieurs objections générales. Leur perspective la plus ambitieuse est comparative. Si l’accès à soi dépend en partie d’une théorie des états mentaux, un système capable de reconnaître de très nombreux régimes d’erreur pourrait, sur certains points, se juger mieux que nous. Cette supériorité reste une hypothèse. L’article offre des arguments et des exemples de conversation, sans présenter une étude comparative de calibration.

### Question 2 · Quelles objections des auteurs vous paraissent les plus convaincantes ?

Le texte examine successivement l’absence de témoignages directs sur les états du modèle dans ses données d’entraînement, l’apparente opposition entre des paramètres figés et des états présents changeants, l’influence des préférences humaines sur les réponses renforcées, les déclarations par lesquelles certains modèles se refusent une vie intérieure et la thèse d’une imitation du langage dépourvue d’une véritable compétence sémantique.

Je retiendrais surtout la troisième objection. Imaginons deux réponses à la même demande, « je suis sûr » et « je dois vérifier ». Si les évaluateurs récompensent systématiquement la seconde parce qu’elle leur semble prudente, elle peut devenir fréquente même lorsque le taux d’erreur du modèle est très faible. La prudence verbale est alors un mauvais indice de la confiance propre à l’essai. La première objection me paraît également sérieuse. Un texte humain enseigne à employer le mot « hésitation » dans les situations appropriées. Le lien entre cet apprentissage et la capacité de reconnaître une hésitation particulière en soi reste à expliquer. Dans les deux cas, une excellente maîtrise des expressions à la première personne laisse ouverte la question de leur source.

### Question 3 · Quelle objection supplémentaire proposeriez-vous ?

J’ajouterais un problème d’identité dans le temps. Après avoir donné une réponse, le système reçoit une nouvelle question qui contient sa réponse précédente. Le calcul produisant « j’hésitais » a lieu à ce nouvel instant. Il peut reconstruire une justification convaincante à partir de la trace écrite, même si l’état précis du calcul initial n’est plus accessible. L’objection subsiste pour un modèle qui comprend le français, varie avec le contexte et n’a reçu aucune récompense spéciale pour se montrer modeste.

Pour la mettre à l’épreuve, je demanderais d’abord un jugement de confiance **avant** de montrer la solution. Je le comparerais à l’estimation d’un observateur qui lit exactement le même énoncé et la même réponse. Les essais seraient appariés en difficulté. Si les deux prédisent aussi bien les erreurs, les indices publics suffisent à rendre compte du résultat. Si le système anticipe des erreurs propres à ses essais que l’observateur ne distingue pas, cela motive la recherche d’un accès supplémentaire. Ce résultat ne suffirait toutefois pas à identifier à lui seul le mécanisme en jeu.

![Comparaison proposée pour la discussion orale. Le système et un observateur voient les mêmes indices publics. On compare ensuite le pouvoir prédictif de leurs jugements.](figures/comparaison-premiere-tierce-personne.svg)

### Question 4 · En quoi consiste la conception non anthropocentrique de l’introspection ?

À la suite de Kammerer et Frankish, les auteurs retiennent trois exigences. Il faut un système cognitif, une représentation d’un de **ses propres états mentaux actuels**, et la possibilité d’utiliser cette information pour régler son comportement pendant qu’il agit. Un exemple serait un système qui repère son incertitude entre deux réponses et change de stratégie pour les départager. Le changement de stratégie rend la représentation de l’incertitude fonctionnellement pertinente. Une seule phrase à la première personne ne permet pas encore de vérifier ces trois conditions.

Cette conception rend comparables des organismes et des machines dont les corps, les sens et les vocabulaires diffèrent. Elle autorise un accès à soi indirect et faillible, et laisse ouverte la possibilité d’états que le vocabulaire humain décrit mal. Sa difficulté réside dans « état mental ». Un thermostat utilise la température mesurée pour régler le chauffage. À quel moment un dispositif représente-t-il sa propre incertitude, en plus de traiter un signal ? Il faut caractériser l’état de premier ordre, montrer que le système le prend lui-même pour objet et préciser son rôle dans la conduite. La définition fonctionnelle laisse aussi ouverte la question d’une éventuelle expérience subjective.

### Question 5 · Quelles réponses des auteurs vous satisfont, et lesquelles vous laissent sur votre réserve ?

La réponse sur les paramètres figés me convainc largement contre une impossibilité de principe. Les mêmes paramètres traitent des contextes différents. Dans l’article, l’annonce que deux noms désignent la même personne fait réviser au modèle le nombre d’individus présents. L’évolution de la conversation produit donc une révision sans réentraînement. Mais recompter les individus porte sur la scène décrite. Il faudrait un pas supplémentaire pour établir que le système représente sa propre révision, puis se sert de cette représentation.

Sur l’entraînement, les auteurs invoquent les régularités implicites des textes, l’analogie avec la psychologie humaine et l’apprentissage dans les interactions. Ces voies rendent concevable l’acquisition d’un vocabulaire utilisable sur soi. Leur réponse à l’objection des récompenses est moins décisive à mes yeux. Les humains aussi apprennent, en société, quelles descriptions d’eux-mêmes seront bien reçues. Cette analogie empêche d’exclure la machine pour cette seule raison. Elle ne donne pas la fréquence des rapports exacts chez l’humain ni chez la machine. Quant aux dénégations de vie intérieure, leur variation avec les modèles, les questions et les habitudes de réponse suffit à rendre leur valeur de verdict douteuse. Une affirmation de sens contraire exige le même contrôle.

Enfin, l’objection de l’imitation sans compréhension engage une théorie générale de la signification. Les auteurs rappellent que plusieurs théories rivales existent et que leurs travaux défendent des approches externalistes. Cela donne une raison de suspendre un rejet dogmatique, tout en laissant une question empirique à résoudre dans chaque cas.

### Question 6 · Partagez-vous l’optimisme des auteurs ?

Je partage leur optimisme sur la comparaison, mais je réserverais mon jugement sur une supériorité actuelle. Leur argument le plus intéressant vient de la conception suivant laquelle nous interprétons nos propres états à l’aide de ressources qui nous servent aussi à comprendre les autres. Ils s’appuient notamment sur Alison Gopnik. Si cette conception est juste, une théorie de soi peut s’améliorer avec l’expérience et demeurer faillible. L’expertise humaine cesse d’être une limite imposée d’avance à tout autre système.

Je comparerais des personnes et plusieurs modèles sur des séries de problèmes nouveaux de difficulté appariée. Avant le corrigé, chacun annoncerait une probabilité de réussite et choisirait de répondre, de vérifier ou de s’abstenir. Sur des problèmes comparables, les réponses annoncées à 70 % devraient effectivement réussir environ sept fois sur dix. J’examinerais aussi si, à difficulté comparable, chacun distingue ses réussites de ses erreurs et si le choix de vérifier améliore le résultat. Annoncer partout le taux moyen de succès peut donner une apparence de calibration sans aucune connaissance de ses erreurs particulières. Un avantage reproductible sur ces trois mesures soutiendrait une supériorité dans cette tâche. La question de l’expérience vécue et celle d’une supériorité générale demanderaient encore d’autres arguments.

![Exemple fictif avec deux groupes de même taille. Le taux total est de 70 % dans les deux cas. Le jugement de droite distingue les groupes dont les taux de réussite diffèrent.](figures/confiance-et-discrimination.svg)
