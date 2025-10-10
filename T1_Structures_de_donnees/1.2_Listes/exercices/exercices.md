# Exercices Listes Chainées ⛓️

## Exo 1 : utilisation de l'interface d'une liste chainée 🖊️

Dans cet exercice, on considère que l'on dispose d'une ***liste chainée*** nommée `chaineGrades` qui représente différents grades militaires dans l'armée française (la _chaine de commandement_), en partant du grade le plus bas (simple _Soldat_) et en allant vers le plus élevé (_Général_) :

> chaineGrades : Soldat → Sergent → Lieutenant → Capitaine → Colonel → Géneral

![grade](./data/grade.png){: .center width=100%}


1. Indiquer quel est le contenu des variables `g1` et `c1` définies par 
```python
g1 = head(chaineGrades)
c1 = tail(chaineGrades)
```
??? question "🙋 correction"
    g1 renvoie `soldat`
    c1 renvoie `Sergent → Lieutenant → Capitaine → Colonel → Géneral`

2. Même question avec les variables `g2` et `c2`, avec 

```python
g2 = head(tail(chaineGrades))
c2 = tail(tail(chaineGrades))
```

??? question "🙋 correction"
    g2 renvoie `Sergent`
    c2 renvoie `Lieutenant → Capitaine → Colonel → Géneral`

3. On définit la fonction `mystere` ainsi :

```python 
def mystere(maListeChainée, n) :
    #Entrée : n est un entier supérieur ou égal à 1
    compteur = 1
    listeProvisoire = self
    while compteur < n and not listeProvisoire.est_vide() :
        listeProvisoire = listeProvisoire.tail
        compteur += 1
    if not listeProvisoire.est_vide():
        return listeProvisoire.head
    else :
        return None 
```

Quelle est la valeur retournée par l'appel `mystere(chaineGrades, 3)` ? Et par l'appel `mystere(chaineGrades, 7)` ? 

??? question "🙋 correction"
    `mystere(chaineGrades, 3)` renvoie Lieutenant <br />
    `mystere(chaineGrades, 7)` renvoie `None`

Quel est le rôle de cette fonction ?

??? question "🙋 correction"
    La fonction mystere retourne le n-ième élément d’une liste chaînée (si n est valide), ou None sinon


## Exo 2 : Visualisation d'une liste chainée 🖊️

Dans le cours, nous avons défini une classe `Maillon` et, à titre d'exemple, nous l'avons utilisée pour définir la **liste chainéee** des rois de France. Voici une visualisation graphique de cette structure :

```python
class Maillon :
    def __init__(self, data = None, suivant = None)  :
        self.head= data
        self.tail = suivant
    
    def __str__() :
        return ""
roi5 = Maillon("Louis XVI") # pas besoin de préciser le 2ème argument, c'est None par défaut
roi4 = Maillon("Louis XV", roi5)
roi3 = Maillon("Louis XIV", roi4)
roi2 = Maillon("Louis XIII", roi3)
roi1 = Maillon("Henri IV", roi2)
print(roi1)
```
👉 Complétez la redéfinition de la fonction print pour afficher une liste chainée <br />
exemple : Henri IV → Louis XIII → Louis XIV → Louis XV → Louis XVI

## Exo 3 : Renverser une liste chainée

L'objectif de l'exercice est d'écrire le code d'une fonction `renverserListeChainée(maListe)` qui prend en paramètre une ***liste chainée*** et qui renvoie une autre liste chainée correspondant au parcours dans le sens inverse de `maListe`.

Par exemple, en reprenant la liste chainée des grades de l'armée de l'exercice précédent, on veut que l'appel `renverserListeChainée(chaineGrades)` renvoie la liste chainée représentant `Général → Colonel → Capitaine → Lieutenant → Sergent → Soldat`.

Pour cela on va compléter la définition de la classe Maillon et écrire les _primitives_ de l'interface des listes chainées (`creer_liste_vide`, `inserer_en_tete`, etc).

??? question "Correction"

    ```python

    class Maillon :
        def __init__(self, data=None, suivant=None):
            self.head = data
            self.tail = suivant

        def __str__(self):
            """Affiche la liste chaînée depuis ce maillon"""
            courant = self
            chaine = ""
            while courant is not None:
                chaine += str(courant.head)
                if courant.tail is not None:
                    chaine += " → "
                courant = courant.tail
            return chaine
        
        def insere(self, data):
            """Insère un nouveau maillon avec la donnée data au début de la liste chaînée"""
            return Maillon(data, self) s

        def head(self):
            """Renvoie la donnée du maillon courant"""
            return self.head
        
        def tail(self):
            """Renvoie le maillon suivant"""
            return self.tail
        
        def est_vide(self):
            """Renvoie True si la liste chaînée est vide, False sinon"""
            return self.head is None and self.tail is None
    ```
👉 Ecrire le code d'une fonction `renverserListeChainée(maListe)` qui prend en paramètre une ***liste chainée*** et qui renvoie une autre liste chainée correspondant au parcours dans le sens inverse de `maListe`.

```python
# Quelques tests 
#Création de la chaine Grade : `Général → Colonel → Capitaine → Lieutenant → Sergent → Soldat`.
soldat = Maillon("Soldat")
sergent = Maillon("Sergent", soldat)
lieutenant = Maillon("Lieutenant", sergent)
capitaine = Maillon("Capitaine", lieutenant)
colonel = Maillon("Colonel", capitaine)
general = Maillon("Général", colonel)
print(general)  # Affiche : Général → Colonel → Capitaine → Lieutenant → Sergent → Soldat
#Insertion d'un nouveau maillon au début de la liste chaînée
Maréchal = general.insere("Maréchal")
print(Maréchal)  # Affiche : Maréchal → Général → Colonel → Capitaine → Lieutenant → Sergent → Soldat

#ou autrement avec la méthode insere
soldat = Maillon("Soldat")
sergent = soldat.insere("Sergent")
lieutenant = sergent.insere("Lieutenant")
capitaine = lieutenant.insere("Capitaine")
colonel = capitaine.insere("Colonel")
general = colonel.insere("Général")
print(general)  # Affiche : Général → Colonel → Capitaine → Lieutenant → Sergent → Soldat

general_renverse = general.renverse()
print(general_renverse)  # Affiche : Soldat → Sergent → Lieutenant → Capitaine → Colonel → Général
```

??? question "Correction"

    ```python
        def renverse(self):
        """Renvoie une nouvelle liste chaînée qui est l'inverse de la liste courante"""
        courant = self
        # On crée une nouvelle liste chaînée vide pour y ajouter les maillons dans l'ordre inverse
        chaineRenversee = None
        #On parcourt la liste chaînée courante et on ajoute chaque maillon au début de la nouvelle liste
        while courant is not None:
            # On sauvegarde le maillon suivant avant de modifier le maillon courant
            next_maillon = courant.tail
            # On insère le maillon courant au début de la nouvelle liste
            courant.tail = chaineRenversee
            # On met à jour la nouvelle liste renversée pour qu'elle commence par le maillon courant
            chaineRenversee = courant
            # On passe au maillon suivant dans la liste courante
            courant = next_maillon
        return chaineRenversee
    ```

## Exo 4 : longueur d'une liste chainée

Il peut être utile de connaître la longueur d'une liste chainée.La définition ***récursive*** ("en poupée russe") d'une liste chainée permet d'envisager un **code récursif** pour la fonction `longueurListeChainée(lst)`.

Compléter le code de la fonction `longueur_rec`.


```python
class Maillon :
    def __init__(self, data = None, suivant = None) :
        self.head = data
        self.tail = suivant

    def longueur_rec(self) :
        if ... is None : # cas de base
            return ...
        else :
            return ... + longueur_recur_POO(...)
```

et quelques test ...

```python
#Test de la méthode longueur_rec
print("Tests de la méthode longueur_rec :")
print(general.longueur_rec())  # Affiche : 6
print(Maréchal.longueur_rec())  # Affiche : 7

#Test sur une chaine vide
print("Tests sur une chaîne vide :")
chaine_vide = Maillon()
print(chaine_vide.est_vide())  # Affiche : True
print(chaine_vide.longueur_rec())  # Affiche : 0
```
??? question "Correction"

    ```python
        def longueur_rec(self) :
        if self.tail is None : # cas de base
            return 1
        else :
            return 1 + self.tail.longueur_rec()
    ```

## Exo 5 : Insérer une donnée dans une liste chainée 

On veut écrire une fonction `inserer(val, chaine, n)` qui va insérer la valeur `val` dans la liste chainée `chaine` après le `n`-ième maillon, où `n` est un entier supérieur ou égal à 1.

Par exemple, en reprenant la liste chaine `m1` des grades de l'exercice précédent, on veut que `inserer("Adjudant", m1, 2)` insère le grade d'adjudant après le 2ème maillon, c'est-à-dire entre `Sergent` et `Lieutenant`.

Compléter le code de cette fonction **récursive**.


```python
class Maillon :
    def __init__(self, data = None, suivant = None) :
        self.head = data
        self.tail = suivant
        
    def inserer(val, chaine, n) :
        """ insére la donnée dans la chaine après le n-ième maillon"""
        if n == 0 :
            return 
        else :
            # compléter ici
```

Et quelques Tests ...
```python    
#Test de la méthode inserer
print("Tests de la méthode inserer :")
nouvelle_chaine = general_renverse.inserer("Adjudant", 2)
print(nouvelle_chaine)  # Affiche : Soldat → Sergent → Adjudant → Lieutenant → Capitaine → Colonel → Général
#Test du cas limite ou l'on insere à la fin de la chaine
nouvelle_chaine2 = general_renverse.inserer("Général d'armée", 7)
print(nouvelle_chaine2)  # Affiche : Soldat → Sergent → Adjudant → Lieutenant → Capitaine → Colonel → Général → Général d'armée
```

??? question "Correction"

    ```python
    def inserer(self, val, n) :
        """"
        insére la donnée dans la chaine après le n-ième maillon
        On utiliser une approche récursive.
        @param val : la valeur à insérer
        @param n : la position après laquelle insérer (1 pour insérer en tête)
        @return : None : on modifie la liste en place
        """
        # Cas de base : on insère en tête
        if n == 0 :
            return Maillon(val, self)
            # newMaillon = Maillon(val, self.tail)
            # self.tail = newMaillon
        else :
            #Cas récursif : on délègue l'insertion au maillon suivant
            #Cas particulier : si on est en fin de liste, on ajoute un nouveau maillon
            if self.tail is None :
                self.tail = Maillon(val)
            #cas général : on ajoute à la queue de la liste à la position n-1
            elif self.tail is not None :
                self.tail = self.tail.inserer(val, n-1)
            return self
    ```

## Exo 6 : Chaine de désintégration ⚛️

En Enseignement Scientifique de Première, vous avez étudié la désintégration par radioactivité du noyau des atomes. 

La demi-vie d'un noyau correspond à la durée nécessaire, en nombre d'années, pour que la moitié des noyaux initialement présents dans un échantillon se soit désintégrée.

Par exemple, le Radium 226 (${}^{226}Ra$) se désintègre en Radon 222 (${}^{222}Rn$) avec une demi-vie de 1600 ans.

Le Radon 222 peut lui-même se désintégrer en Polonium 218, et ainsi de suite jusqu'à aboutir au Plomb 206 qui est stable.

On a donc une chaine de désintégration :

![desintégration](./data/desintegration.png){: .center width=50%}

Pour manipuler en Python une chaine de désintégration, on utilise une classe `Chaine` qui implémente la structure de données abstraite de ***liste chainée*** dans une version ***moins simpliste*** que celle utilisée précédemment.

Chaque maillon est un triplet de la forme `(nom_atome, masse_atomique, demi_vie)`, comme par exemple `radium = ('Ra',226, 1600)`.

La classe `Chaine` est munie de méthodes qui modélisent l'interface usuelle des listes chainées : `est_vide()`, `tete()`, `queue()` et `ajout_en_tete(donnée)`.


```python
class Maillon :
    def __init__(self, data = None, suivant = None)  :
        self.head = data
        self.tail = suivant

class Chaine :
    def __init__(self, first = None) :
        self.premier_maillon = first
    
    def est_vide(self) :
        return self.premier_maillon == None
    
    def tete(self) :
        return self.premier_maillon.head
    
    def queue(self) :
        if not (self.est_vide()):
            return Chaine(self.premier_maillon.tail)
    
    def ajout_en_tete(self, data) :
        nouveau_maillon = Maillon(data, self.premier_maillon)
        self.premier_maillon = nouveau_maillon

    def __repr__(self):
        if self.est_vide():
            return "[]"
        courant = self.premier_maillon
        elements = []
        while courant is not None:
            nom, masse, demi_vie = courant.head
            if demi_vie >= 1e99:   # élément stable
                elements.append(f"{nom}{masse} (stable)")
            else:
                elements.append(f"{nom}{masse}")
            courant = courant.tail
        return " → ".join(elements)
```

La chaine de désintégration du Radon est donc instanciée par le code suivant :


```python
desintegrationRa = Chaine()
desintegrationRa.ajout_en_tete(('Pb', 206, 1e100))
desintegrationRa.ajout_en_tete(('Po', 210, 0.4))
desintegrationRa.ajout_en_tete(('Bi', 210, 0.014))
desintegrationRa.ajout_en_tete(('Pb', 210, 22.2))
desintegrationRa.ajout_en_tete(('Po', 214, 5.2e-12))
desintegrationRa.ajout_en_tete(('Bi', 214, 3.8e-2))
desintegrationRa.ajout_en_tete(('Pb', 214, 5.7e-5))
desintegrationRa.ajout_en_tete(('Po', 218, 5.7e-6))
desintegrationRa.ajout_en_tete(('Rn', 222, 0.01))
desintegrationRa.ajout_en_tete(('Ra', 226, 1600))

print(desintegrationRa)
```

La chaine de désintégration du Césium est plus courte et elle est instanciée par le code suivant :

```python
desintegrationCs = Chaine()
desintegrationCs.ajout_en_tete(('Ba', 137, 1e100))
desintegrationCs.ajout_en_tete(('Cs', 137, 30.2))

print(desintegrationCs)
```

**1.** Un élément stable est un élément qui se situe en bout de chaine de desintégration.

Par exemple, le Plomb 206 est un élément stable car il est en bout de la chaine `desintegrationRa`.

Écrire le code de la fonction `estStable(chaine)` qui prend en paramètre une liste chainée `chaine` non vide et qui renvoie `True` si le maillon de tête est un élément stable.


```python
def estStable(chaine) :
    ...

# test 1
estStable(desintegrationRa)
# test 2
desintegrationPb = Chaine()
desintegrationPb.ajout_en_tete(('Pb', 206, 1e100))
estStable(desintegrationPb)
```

??? question "Correction"

    ```python
    def estStable(chaine):
    # stable ↔ il n'y a pas de maillon suivant
    return chaine.queue() is None or chaine.queue().est_vide()
    ```

**2.** L'élément le plus instable d'une chaine de desintégration est celui qui a la demi-vie la plus faible.

La fonction `lePlusInstable(chaine)` qui prend en paramètre une liste chainée non vide `chaine` doit renvoyer le nom et la masse atomique de l'atome le plus instable de `chaine`. 

Par exemple, on veut que l'appel `lePlusInstable(desintegrationRa)` renvoie `(Po, 214)`.

Compléter le code de cette fonction :


```python
def lePlusInstable(chaine) :
    durée_mini = chaine.tete()[2]
    atome_instable = (..., ...)
    chaine = chaine.queue()
    while not chaine.est_vide() :
        ...
    return atome_instable

# test
lePlusInstable(desintegrationRa)
```

??? question "Correction"

    ```python
    def lePlusInstable(chaine):
        duree_mini = chaine.tete()[2]
        atome_instable = (chaine.tete()[0], chaine.tete()[1])
        chaine = chaine.queue()
        while not chaine.est_vide():
            duree = chaine.tete()[2]
            if duree < duree_mini:
                duree_mini = duree
                atome_instable = (chaine.tete()[0], chaine.tete()[1])
            chaine = chaine.queue()
        return atome_instable
    ```

**3)** Dans la chaine de désintégration du radon, on trouve trois fois l'isotope `Po` (${}^{218}Po$, ${}^{214}Po$ et ${}^{210}Po$) et une seule fois l'isotope `Rn`.

On veut écrire une fonction **récursive** `nbIsotopes(chaine, nom_atome)` qui renvoie le nombre de fois où `nom_atome`apparaît dans la chaine de désintégration `chaine`.

Par exemple, on veut que l'appel `nbIsotopes(desintegrationRa, 'Po')` renvoie le nombre 3 et que l'appel `nbIsotopes(desintegrationRa, 'Rn')`renvoie le nombre 1.

Compléter le code suivant :

```python
def nbIsotopes(chaine, nom_atome) :
    if chaine.est_vide() :
        return ...
    else :
        # conversion d'un booléen en entier avec la régle : True -> 1 et False -> 0
        occurence = int(chaine.tete()[0] == nom_atome)
        return occurence + nbIsotopes(...)
    
# quelques tests
nbIsotopes(desintegrationRa, 'Po')
nbIsotopes(desintegrationRa, 'Rn')
```

??? question "Correction"

    ```python
    def nbIsotopes(chaine, nom_atome):
        if chaine.est_vide():
            return 0
        else:
            occurence = int(chaine.tete()[0] == nom_atome)
            return occurence + nbIsotopes(chaine.queue(), nom_atome)
    ```

**4.** La masse atomique d'un atome correspond au nombre de protons et de neutrons qui composent le noyau de l'atome. On constate que, au cours d'une suite de désintégration, il y a une baisse de la masse atomique.

On veut écrire une fonction **récursive** `perte_atomique(chaine)` qui prend en paramètre une liste chainée non vide  `chaine` et qui renvoie la baisse totale de la masse atomique.

Par exemple, on veut que l'appel `perte_atomique(desintegrationRa)` renvoie le nombre 20 (car 226 - 206 = 20).

Compléter le code suivant :

```python
def perte_atomique(chaine) :
    if chaine.queue() is None : 
        return ...
    else :
        masse1 = chaine.tete()[1]
        masse2 = chaine.queue().tete()[1]
        return ... + perte_atomique(...)
    
# test
perte_atomique(desintegrationRa)
```

??? question "Correction"

    ```python
    def perte_atomique(chaine):
        if chaine.queue() is None or chaine.queue().est_vide():
            return 0
        else:
            masse1 = chaine.tete()[1]
            masse2 = chaine.queue().tete()[1]
            return (masse1 - masse2) + perte_atomique(chaine.queue())
    ```

**5.** On veut comparer la perte atomique de différentes chaines de désintégration et identifier celle qui a la perte atomique la plus importante.

Écrire le code d'une fonction `maxi_perte_atomique(tab_chaine)` qui prend en argument un tableau `tab_chaine` de listes chainées et qui renvoie la valeur de la perte atomique la plus importante.

Par exemple, l'appel `maxi_perte_atomique([desintegrationRa, desintegrationCs, desintegrationPb])` doit renvoyer la valeur 20.


```python
def maxi_perte_atomique(tab_chaine) :
    tab_perte_atomique = [perte_atomique(chaine) for chaine in ...]
    maxi_perte = ...
    ... # plusieurs lignes à compléter
    return maxi_perte

# un test
maxi_perte_atomique([desintegrationRa, desintegrationCs, desintegrationPb])
```

??? question "Correction"

    ```python
    def maxi_perte_atomique(tab_chaine):
        tab_perte_atomique = [perte_atomique(chaine) for chaine in tab_chaine]
        maxi_perte = tab_perte_atomique[0]
        for v in tab_perte_atomique[1:]:
            if v > maxi_perte:
                maxi_perte = v
        return maxi_perte

    ```

## Exo 7 : Compétition de Kayak 🛶

!!! note "source"
    Correction issue de [pixees : 2022 s5](https://pixees.fr/informatiquelycee/term/suj_bac/index.html)

👉 Ouvrir l'énoncé [Exercice 1 du sujet Amérique du Nord J2 2022 ](./data/Structures_ListesChainees_SujetBac_22NSIJ2AN1.pdf){. target="blank"}

Lors d’une compétition de kayak, chaque concurrent doit descendre le même cours d’eau en passant dans des portes en un minimum de temps. Si le concurrent touche une porte, il se voit octroyé une pénalité en secondes. Son résultat final est le temps qu’il a mis pour descendre le cours d’eau auquel est ajouté l’ensemble des pénalités qu’il a subies.<br />
Un gestionnaire de course de kayak développe un programme Python pour gérer les résultats lors d’une compétition.

Dans ce programme, pour modéliser les concurrents et leurs résultats, une classe Concurrent est définie avec les attributs suivants :

* `nom` de type `str` qui représente le pseudonyme du compétiteur ;
* `temps` de type `float` qui est le temps mis pour réaliser le parcours (_en secondes_) ;
* `penalite` de type `int` qui est le nombre de secondes de pénalité cumulées octroyées au compétiteur ;
* `temps_tot` de type `float` qui correspond au temps total, c'est-à-dire au temps mis pour réaliser le parcours auquel on a ajouté les secondes de pénalité.

On suppose que tous les concurrents ont des temps différents dans cet exercice.

Le code Python incomplet de la classe `Concurrent` est donné ci-dessous.

```python
class Concurrent :
    def __init__(self, pseudo, temps, penalite) :
        self.nom = pseudo
        self.temps = temps
        self.penalite = ...
        self.temps_tot = ...
```

#### Question 1

**1a.** Compléter le code du ***constructeur*** de la classe `Concurrent`.

??? question "Correction"

    ```python
    class Concurrent:
        def __init__(self, pseudo, temps, penalite):
        self.nom = pseudo
        self.temps = temps
        self.penalite = penalite
        self.temps_tot = temps + penalite
    ```

**1b.** On exécute l'instruction suivante `c1 = Concurrent("Mosquito", 87.67, 12)`

* Donner la valeur de l'attribut `temps_tot` de `c1`

??? question "Correction"
    Pour c1, temps_tot est égal à $99,67$ (87,67 + 12)

* Écrire l'instruction qui permet d'accéder à la valeur `temps_tot` de `c1`

??? question "Correction"
    `c1.temps_tot`

#### Question 2

Le code ci-dessous permet de créer la classe `Liste` décrite par l'énoncé : ceci implémente la structure de données abstraite de **liste chainée**, avec l'interface décrite dans l'énoncé.

```python
class Maillon :
    def __init__(self, data = None, suivant = None)  :
        self.head = data
        self.tail = suivant

class Liste :
    def __init__(self, first = None) :
        self.premier_maillon = first
    
    def est_vide(self) :
        return self.premier_maillon == None
    
    def tete(self) :
        return self.premier_maillon.head
    
    def queue(self) :
        if not (self.est_vide()):
            return Liste(self.premier_maillon.tail)
    
    def ajout(self, data) :
        nouveau_maillon = Maillon(data, self.premier_maillon)
        self.premier_maillon = nouveau_maillon
    
```

Pour reprendre l'exemple de l'énoncé :

```python
c1 = Concurrent("Mosquito", 87.67, 12)
c2 = Concurrent("Python Fute", 89.73, 4)
c3 = Concurrent("Piranha Vorace", 90.54, 0)
c4 = Concurrent("Truite Agile", 84.32, 52)
c5 = Concurrent("Tortue Rapide", 92.12, 2)
c6 = Concurrent("Lievre Tranquille", 93.45, 0)

resultats = Liste()
resultats.ajout(c1)
resultats.ajout(c2)
resultats.ajout(c3)
resultats.ajout(c4)
resultats.ajout(c5)
resultats.ajout(c6)
```

Après exécution, ce script génère une liste que l'on peut représenter par : `<c6, c5, c4, c3, c2, c1>`

**2.a** Écrire la (ou les) instruction(s) qui permet(tent) d'accéder à `c4` _uniquement avec les méthodes de la classe `Liste`_ :

??? question "Correction"

    ```python
    L1 = resultats.queue()
    L2 = L1.queue()
    c1 = L2.tete()
    ou bien directement : c1 = resultats.queue().queue().tete()
    ```

**2.b** Écrire la (ou les) instruction(s) qui permet(tent) d'accéder au temps total du concurrent stocké en tête de la liste `resultats` :

```python
# compléter ici
val = ...
assert val == 93.45, "problème de code"
```

??? question "Correction"

    `temps_total = resultats.tete().temps_tot`

#### Question 3

On veut créer une fonction `meilleur_concurrent` 

* qui prend en paramètre une liste `L` de concurrents (de la classe `Liste` ci-dessus)
* et qui renvoie l'objet `Concurrent` correspondant au concurrent le plus rapide.

_On suppose que la liste est non vide_.

Compléter le code de cette fonction :

```python
def meilleur_concurrent(L) :
    conc_mini = L. ... 
    mini = conc_mini.temps_tot
    Q = L.queue()
    while not(Q.est_vide()) :
        elt = Q.tete()
        if elt.temps_tot ... mini :
            conc_mini = elt
            mini = elt.temps_tot
        Q = Q. ...
    return ...

# un test
assert meilleur_concurrent(resultats).nom == 'Piranha Vorace', "problème de code"
```
??? question "Correction"

    ```python
    def meilleur_conccurent(L):
        conc_mini = L.tete()
        mini = conc_mini.temps_tot
        Q = L.queue()
        while not(Q.est_vide()):
        elt = Q.tete()
        if elt.temps_tot < mini :
        conc_mini = elt
        mini = elt.temps_tot
        Q = Q.queue()
        return conc_mini
    ```