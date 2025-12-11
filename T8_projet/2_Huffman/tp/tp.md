
# TP Compression de données

Le codage de Huffman est un procédé très utilisé en compression de données. Il sert à encoder un texte en binaire, en utilisant pour chaque lettre un nombre de bits dépendant du nombre de fois où la lettre est pré-sente : plus la lettre apparaît, plus le nombre de bits est petit. Ainsi, le nombre total de bits utilisés pour encoder le texte est réduit par rapport à un codage ASCII standard qui utilise huit bits pour chaque lettre.

Cette activité doit nous permettre de mettre en œuvre ce codage afin réaliser la compression d'un texte.

Supposons que notre fichier soit extrêmement simple, et constitué d'un mot unique :

``anticonstitutionnellement``

Il y a 25 caractères dans ce fichier ; chaque caractère étant codé par un octet de 8 bits (codage
ASCII) cela signifie donc 25 octets, ou encore 200 bits.

|Clé|Fréquence|
|:--:|:--:|
|a|1| 
|c|1| 
|s|1| 
|u|1| 
|m|1| 
|o|2| 
|l|1| 
|i|3| 
|e|3| 
|n|5|
|t|5| 

[Télécharger les fichiers de travail 🔽](./data/fichiers_annexes.zip){ .md-button .md-button--primary }

❓ Q1) **Compléter** la fonction ``frequences`` qui permet de déterminer le nombre d'apparition de chaque caractère d'une chaine de caractères. (On pourra utiliser la méthode ``get(cle,defaut)`` de la classe ``dictionnaire``, qui renvoie la valeur associée à la clé, ou la valeur par défaut si la clé n'est pas présente dans le dictionnaire.)  

À partir de ces fréquences, l’algorithme initialise un arbre par caractère, avec comme poids le nombre d’apparitions du caractère : ces arbres constitueront les feuilles de notre arbre de codage.

![etape 0](./data/etape0.png){: .center width=50%}
 
Ce qui nous fait dans notre exemple pour l'instant 11 arbres contenant un seul nœud chacun.


❓ Q2) **Compléter** la fonction ``creer_feuilles`` pour créer un tableau contenant un arbre élémentaire pour chaque caractère du texte.

note : Pour pouvoir créer l’arbre, il est nécessaire que les feuilles soient classées dans l’ordre croissant des fréquences.

Q3) Compléter la procédure ``inserer`` qui permet d’insérer un arbre à la position adaptée pour que les arbres soient correctement triés. (On pourra utiliser la méthode ``insert(position)`` qui permet d’insérer un élément dans objet ``list`` à une position donnée).
Modifier la fonction ``creer_feuilles`` pour créer un tableau trié contenant un arbre élémentaire pour chaque caractère du texte.

On commence l'itération : à chaque fois on supprime les deux arbres de gauche et on les remplace par un "arbre somme". Le nouvel arbre est inséré dans la liste en respectant l'ordre croissant, et on recommence jusqu'à ce qu'il ne reste plus qu'un seul arbre :

![etape1 et 2](./data/etape1et2.png){: .center width=60%}
 
![etape 3 et 4](./data/etape3et4.png){: .center with=30%}

Etc…jusqu’à l’étape finale :

![etape finale](./data/etapeFinale.png){: .center width=60%} 

❓Q4) **Compléter** la fonction ``créer_arbre`` qui permet de créer un arbre de Huffman à partir d'un tableau trié d'arbres élémentaires. (on pourra visualiser l’arbre obtenu grâce à la bibliothèque ``Vizuarbrebet`` l’instruction ``VizuArbreB``(arbre_huffman))

Attention : comme vous pouvez le remarquer, on n’obtient pas 2 fois le même arbre à partir d’un même texte d’origine !

|Clé|Code binaire|
|:--:|:--:|
|n|00| 
|t|01| 
|i|100| 
|e|101| 
|a|11000| 
|c|11001| 
|o|1101| 
|l|1110| 
|m|11110| 
|s|111110|
|u|111111| 

Maintenant, le code binaire associé à chaque Clé n'est autre que le chemin d'accès au nœud terminal cor-respondant, depuis la racine, en notant 0 la branche de gauche et 1 la branche de droite.


❓ Q5) **Expliquer** et **commenter** la procédure code_binaire ci-dessous :

 ![fonction](./data/code_binaire.png){: .center width=50%}

Et voici maintenant, transcrit avec notre nouveau code, le mot de départ :

**110000001100110011101001111100110001111111011001101000010111101110101111101010001**

ce qui nous fait 81 bits, au lieu de 200 au départ ! Cela correspond à un taux de compression de 60 %.

❓ Q6) **Compléter** la fonction ``compresser`` qui permet de créer le codage binaire d'un texte entier à partir d'un dictionnaire de correspondance

Maintenant que l’on a testé les différentes fonctionnalités, il est possible de coder un texte entier. 

❓Q7) A partir des fonctionnalités développées dans ce TP, réaliser la compression du roman « Du côté de chez Swann », issu du site [http://gutenberg.org/](http://gutenberg.org/). 

Rappel : les instructions suivantes permettent de stocker le contenu d’un fichier dans une variable de type chaine de caractères :
```python
with open("swann.txt", "r") as fichier:
    texte= fichier.read()
```
❓Q8) Avec un codage ASCII sur 8 bits, **calculer** le poids du texte. **Calculer** le nombre de bits du texte compressé. En déduire le **taux de compression du texte compressé**.

$Taux de compression = (taille – taille_compresse)/taille * 100$

## Grille d'évaluation

Evaluation basée sur une revue de code : ![Grille d'évaluation](./data/evaluation.png){: .center}

