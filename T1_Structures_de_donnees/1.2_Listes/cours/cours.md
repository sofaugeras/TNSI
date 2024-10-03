# Les listes chainées ⛓️

!!! note "Crédits"
    @crédit de la page [Pierre-Alain Sallard](https://pasallard.gitlab.io/terminale_nsi_voltaire/Structures/1_StructuresLineaires/3_ListesChainees/Structures_ListesChainees/) sous licence CC BY-SA 

!!! warning "Attention au vocabulaire"
    Ne pas confondre la structure de données abstraites **Liste chainée** (ou simplement **liste** dans certains manuels) avec le type `list` de Python.

    Le type `list` de Python s'apparente à une implémentation de la structure de **tableau dynamique** (_hors-programme_).


## ^^1. Notion de liste chainée^^

La structure **liste chainée** fait partie, comme les files (d'attente) et les piles, des **structures de données linéaires** : les données sont "alignées" les unes après les autres. 

Ce qui caractérise une **liste chainée**, ce n'est pas le mode de gestion des entrées et sorties des données (_FIFO_ pour les files, _LIFO_ pour les piles) mais c'est qu'elle offre un moyen de passer d'une donnée à la suivante.

L'idée de base de la notion de structure de **liste chainée** est :

* on forme une "chaine" avec des "maillons" ;
* un ***maillon*** de la chaine contient 
    - la donnée elle-même
    - et un lien ou "pointeur" vers le maillon suivant ;
* et **on "tient" la chaine par son premier maillon**.

!!! done "Exemple : liste chainée des rois de France"

    La dynastie des Bourbons, rois de France qui ont régné de 1589 à 1792, peut être représentée par la liste chainée suivante :

    ![](data/schema-liste-chainee.png){: .center width=60%}


!!! tip "Définition récursive d'une **liste** en informatique :heart:"
    L'idée de base exposée plus haut laisse entrevoir qu'une liste, c'est :

    - soit une liste vide, 
    - soit un élément suivi d'une autre liste (éventuellement vide).

    On est donc devant une définition ***récursive*** d'une liste !

!!! question "Exercice : utiliser la définition récursive d'une liste chainée"

    On donne la construction suivante :

    - L est la liste dont le maillon vaut "Alice" et dont la liste suivante est vide ;
    - M est la liste dont le maillon vaut "Bob" et dont  la liste suivante est L ;
    - N est la liste dont le maillon vaut "Gaston" et dont  la liste suivante est M ;
    - P est la liste dont le maillon vaut "Jeanne" et dont  la liste suivante est N.

    Dessiner la liste chainée P.

??? danger "Solution"
    La liste chainée P est  "Jeanne" → "Gaston" → "Bob" → "Alice" → ⟂.

    _Remarque :_ le symbole "⟂" représente une liste vide, ce qui marque la fin de la liste chainée.

    Ceci illustre bien le principe : **on "tient" la chaine par son premier maillon.**

## ^^2. Interface d'une liste chainée^^

L'**interface** minimale d'une liste chainée comporte les opérations  (_les primitives_) suivantes :

| Fonction | Description |
| :------ | :------- | 
| `créer_liste_vide()` | renvoyer une nouvelle liste chainée vide |
| `inserer_en_tete(lst, donnée)` | ajouter la valeur `donnée` en tête de la liste chainée `lst`|
| `tete(lst)` ou `head(lst)` | renvoyer la valeur du maillon qui est en tête de la liste chainée `lst`  |
| `queue(lst)` ou `tail(lst)` | renvoyer la liste chainée `lst` sans son premier maillon   |
| `est_vide(lst) ` | renvoyer `True` si `lst` est vide et `False` sinon |

!!! done "Exemple d'utilisation avec la liste chainée des rois de France"
    Si on note `Bourbons` la liste chainée de l'exemple précédent, alors :

    - `tête(Bourbons)` renvoie la valeur `"Henri IV"`
    - `queue(Bourbons)` renvoie la liste chainée "Louis XIII" → "Louis XIV" → "Louis XV" → "Louis XVI" → ⟂, c'est-à-dire tout ce qui vient après la "tête" de la liste `Bourbons`.


## ^^3. Longueur d'une liste chainée^^

Supposez que l'on vous demande la longueur d'une liste chainée `maListeChainée` qui a une queue (`tail(maListeChainée)`) de longueur 7 : vous répondrez sans hésitation que la longueur vaut 1+7= 8.

![](data/longueurListe.png){: .center width=60%}

Cette "structure imbriquée", cette disposition en "poupée russe" d'une liste chainée permet de définir une **fonction récursive** de calcul de longueur d'une liste chainée :

    FONCTION LongueurListeChainée(lst)

        SI est_vide(lst) ALORS
            RENVOYER 0 # cas de base
        SINON
            RENVOYER 1 + LongueurListeChainée(tail(lst))

En exercice, vous devrez coder en Python cette fonction pour chacun des deux modes de représentation (_pour chaque implémentation_) d'une liste chainée que l'on va proposer ci-dessous.

## ^^4. Implémentation d'une liste chainée : version impérative, à l'aide de ***tuples***^^

On peut choisir de représenter un maillon par un couple (type `tuple`) de la forme : `maillon = (valeur, maillon_suivant)`.

Quand il n'y a pas de maillon suivant, on indique le couple vide `()` à la place. 

La variable qui désigne la liste chainée est alors simplement celle du premier maillon : souvenez-vous de l'idée de base "**on tient toute la chaine grâce au premier maillon" !**

!!! done "Une implémentation de la liste chainée des rois de France"
    
    Avec cette implémentation d'une liste chainée sous forme de couples, on pourra donc écrire :

    ```python 
    roi5 = ("Louis XVI", ()) # on commence par la fin de la liste chainée
    roi4 = ("Louis XV", roi5)
    roi3 = ("Louis XIV", roi4)
    roi2 = ("Louis XIII", roi3)
    roi1 = ("Henri IV", roi2)
    Bourbons = roi1 # on tient la liste chainée par son premier maillon
    ```

    ou bien de façon plus condensée, mais moins lisible :

    ```python
    Bourbons = ('Henri IV', ('Louis XIII', ('Louis XIV', ('Louis XV', ('Louis XVI', ())))))
    ```

    Voici le contenu visuel du _tuple_ `Bourbons` (le `0` indique le contenu de la case d'indice 0 du tuple et le `1` le contenu de la case d'indice 1).

    ![](data/schema_chaine_bourbons.png)

Avec ce choix d'implémentation d'une liste chainée à l'aide de _tuples_, voici des codes possibles pour les fonctions  `creer_liste_vide()`, `inserer_en_tete(lst, donnée)`,  `head(lst)`,  `tail(lst)` et `est_vide(lst) ` spécifiées par l'interface :

```python
def creer_liste_vide() :
    return () # tuple vide

def inserer_en_tete( lst, donnée ) :
    return (donnée, lst) # c'est le nouveau premier maillon de la chaine

def head( lst ) :
    return lst[0] # c'est ce qu'il y a en position 0 du couple L

def tail( lst ) :
    return lst[1] # c'est ce qu'il y a en position 1 du couple L

def est_vide( lst ) :
    return len( lst ) == 0
```

Une façon d'utiliser cette implémentation est alors :
```python
# exemple d'utilisation
Bourbons = ('Henri IV', ('Louis XIII', ('Louis XIV', ('Louis XV', ('Louis XVI', ())))))
roi = head(Bourbons)
print("La tête de la liste chaine : ", roi)
queLesLouis = tail(Bourbons)
print("Après la tête de la liste chainée, il y a ", queLesLouis)
Bourbons = inserer_en_tete(Bourbons, "Henri III")
print("On a rajouté un roi en tête de la chaine  : ", Bourbons)
```

!!! question "Exercice  : une chaine alimentaire"

    On veut créer en Python la liste chainée qui représente la chaine alimentaire suivante :

    ![](data/chaineAlimentaire.png){: .center width 60%}

    **1.** On pourrait simplement saisir ```chaineAlimentaire = ("corn", ("mouse",("snake",("owl",()))))``` mais, dans un but pédagogique, on vous demande de créer cette liste en utilisant les fonctions `creer_liste_vide()` et `inserer_en_tete(L, donnée)`.

    **2.** Quelle est la valeur renvoyée par l'appel de la fonction `head(tail(chaineAlimentaire))` ?

??? danger "Solution" 

    1. Réponse :
    ```python
    chaineAlimentaire = creer_liste_vide()
    inserer_en_tete(chaineAlimentaire, "owl")
    inserer_en_tete(chaineAlimentaire, "snake")
    inserer_en_tete(chaineAlimentaire, "mouse")
    inserer_en_tete(chaineAlimentaire, "corn")
    ```

    2. Cela renvoie `mouse`.

!!! question "Exercice  : protection des fonctions head et tail"

    Une liste chainée vide n'a "ni queue ni tête" !  Cela signifie que l'exécution des fonctions `head` et `tail` sur une liste chainée vide va provoquer une erreur.
    
    Ajouter une instruction de type `assert` au début de ces fonctions afin de les "protéger". 

??? danger "Solution"
    On ajoute à ces fonctions l'instruction `assert not est_vide(lst), "impossible sur une chaine vide"`.

## ^^5. Implémentation d'une liste chainée : version Programmation Orientée Objet^^

Une autre façon d'implémenter une liste chainée est de créer un objet "Maillon", c'est-à-dire en Python de créer une **classe Maillon** qui a deux **attributs** :

* la donnée à stocker,
* et le maillon suivant, qui est lui-même un objet de la classe `Maillon` (éventuellement vide).

Un maillon vide est représenté par la valeur `None`.

```python
class Maillon :
    def __init__(self, data = None, suivant = None)  :
        self.head= data
        self.tail = suivant
```

> On a mis `None` en valeur par défaut à la fois pour la donnée et pour le maillon suivant, ce qui permet de créer un maillon vide en écrivant `maillonVide = Maillon()`.

On peut noter que cette classe `Maillon` n'a pas de _méthodes_ dédiées. 

!!! done "Exemple avec la liste chainée des rois de France"
    On peut alors créer (_"instancier"_) les objets suivants :
    ```python
    roi5 = Maillon("Louis XVI") # pas besoin de préciser le 2ème argument, c'est None par défaut
    roi4 = Maillon("Louis XV", roi5)
    roi3 = Maillon("Louis XIV", roi4)
    roi2 = Maillon("Louis XIII", roi3)
    roi1 = Maillon("Henri IV", roi2)
    Bourbons = roi1 # on tient la liste par son premier maillon
    ```

    Puis on peut utiliser ainsi la liste chainée :

    ```python
    class Maillon :
    def __init__(self, data = None, suivant = None)  :
        self.head= data
        self.tail = suivant

    roi5 = Maillon("Louis XVI") # pas besoin de préciser le 2ème argument, c'est None par défaut
    roi4 = Maillon("Louis XV", roi5)
    roi3 = Maillon("Louis XIV", roi4)
    roi2 = Maillon("Louis XIII", roi3)
    roi1 = Maillon("Henri IV", roi2)
    Bourbons = roi1 # on tient la liste par son premier maillon
    # exemple d'utilisation
    print("La tête de la liste chainée : ", Bourbons.head )
    queLesLouis = Bourbons.tail
    print("Après la tête de la liste chainée, on trouve ", queLesLouis.head )
    Bourbons = Maillon("Henri III", Bourbons) # insertion en tête de la liste chainée
    print("On rajoute un roi à notre chaine : en tête, on a maintenant ", Bourbons.head )
    ```

!!! info "Remarque : implémentation simpliste"
    Le choix est fait ici de rester avec une version simple de l'implémentation en POO d'une liste chainée. L'interface d'une liste chainée n'est, à ce stade, pas complètement respectée : par exemple, la fonction `est_vide` de l'interface n'a pas été écrite. Et les fonctions `creer_liste_vide` et `inserer_en_tete` n'ont pas été explicitées même si on peut faire la même chose en créant un objet de la classe `Maillon` : par exemple l'instruction `Bourbons = Maillon("Henri III", Bourbons)` a remplacé l'instruction `Bourbons = inserer_en_tete(Bourbons, "Henri III")`.
    
    On verra en exercice comment se conformer rigoureusement à l'interface demandée.


!!! question "Exercice  : la chaine alimentaire en version POO"

    Reprendre les questions de l'exercice "une chaine alimentaire" en utilisant cette fois l'implémentation en version POO.

??? danger "Solution"

    On écrit le code suivant :
    
    ```python
    hibou = Maillon("owl")
    serpent = Maillon("snake", hibou)
    souris = Maillon("mouse", serpent)
    chaineAlimentaire = Maillon("corn",souris)
    ```


!!! question "Exploration d'une liste chainée "
    En appuyant sur le bouton "Lancer", vous allez exécuter un code masqué qui crée (_qui instancie_) un objet `maListeMystere` de la classe `Maillon`. 

    En vous servant des attributs de cet objet, explorer cette liste chainée puis la représenter.

    ```python
    class Maillon :
        def __init__(self, data = None, suivant = None)  :
            self.head= data
            self.tail = suivant

    C = Maillon("Chocolat")
    B = Maillon("Bronze", C)
    A = Maillon("Argent", B)
    maListeMystere = Maillon("Or",A)
    print("Merci d'avoir executé le code : à vous de découvrir la liste chainée maListeMystere")
    ```
    ??? danger "Solution"
        La liste chainée est : Or → Argent → Bronze → Chocolat → ⟂.
        On l'obtient en saisissant `maListeMystere.head`, puis `maListeMystere.tail.head`, etc.


## ^^6. Exercices et TP^^

* Généralités : télécharger le [carnet Jupyter](data/TP_Exos_ListesChainees.ipynb), à ouvrir sous [Basthon](https://notebook.basthon.fr/){target="_blank"}.

* Exercice type Bac :

    - [énoncé](data/Structures_ListesChainees_SujetBac_22NSIJ2AN1.pdf) à faire d'abord sur feuille,
    - puis codage dans un [carnet Jupyter](data/Structures_ListesChainees_SujetBac_22NSIJ2AN1.ipynb).
    - en cas de blocage : éléments de correction [ici](https://pixees.fr/informatiquelycee/term/suj_bac/index.html) (année 2022, sujet 5).


