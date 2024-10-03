# Exercices Listes Chainées ⛓️

## 🖊️ Exercice : utilisation de l'interface d'une liste chainée

Dans cet exercice, on considère que l'on dispose d'une ***liste chainée*** nommée `chaineGrades` qui représente différents grades militaires dans l'armée française (la _chaine de commandement_), en partant du grade le plus bas (simple _Soldat_) et en allant vers le plus élevé (_Général_) :

> chaineGrades : Soldat → Sergent → Lieutenant → Capitaine → Colonel → Géneral

<img src="" >

1. Indiquer quel est le contenu des variables `g1` et `c1` définies par 
```python
g1 = head(chaineGrades)
c1 = tail(chaineGrades)
```

🙋 Réponse :
2. Même question avec les variables `g2` et `c2`, avec 
```python
g2 = head(tail(chaineGrades))
c2 = tail(tail(chaineGrades))
```
🙋 Réponse :
3. On définit la fonction `mystere` ainsi :

```python 
def mystere(maListeChainée, n) :
    """ Entrée : n est un entier supérieur ou égal à 1 """
    compteur = 1
    listeProvisoire = maListeChainée
    while compteur < n and not est_vide(listeProvisoire) :
        listeProvisoire = tail(listeProvisoire)
        compteur += 1
    if not est_vide(listeProvisoire):
        return head(listeProvisoire)
    else :
        return None
```

Quelle est la valeur retournée par l'appel `mystere(chaineGrades, 3)` ? Et par l'appel `mystere(chaineGrades, 7)` ? 

Quel est le rôle de cette fonction ?
🙋 Réponse :


## 🖊️ Exercice : Visualisation d'une liste chainée

_Remarque_ : pour que la visualisation fonctionne, il faut installer le module `lolviz` de Python.

Sous Linux 
```bash
$ sudo apt-get install graphviz 
```
puis

```bash
$ pip3 install lolviz
```

Dans le cours, nous avons défini une classe `Maillon` et, à titre d'exemple, nous l'avons utilisée pour définir la **liste chainéee** des rois de France. Voici une visualisation graphique de cette structure :


```python
from lolviz import *

class Maillon :
    def __init__(self, data = None, suivant = None)  :
        self.head= data
        self.tail = suivant
        
roi5 = Maillon("Louis XVI") # pas besoin de préciser le 2ème argument, c'est None par défaut
roi4 = Maillon("Louis XV", roi5)
roi3 = Maillon("Louis XIV", roi4)
roi2 = Maillon("Louis XIII", roi3)
roi1 = Maillon("Henri IV", roi2)

objviz(roi1)
```

## 🖊️ Exercice : Renverser une liste chainée


L'objectif de l'exercice est d'écrire le code d'une fonction `renverserListeChainée(maListe)` qui prend en paramètre une ***liste chainée*** et qui renvoie une autre liste chainée correspondant au parcours dans le sens inverse de `maListe`.

Par exemple, en reprenant la liste chainée des grades de l'armée de l'exercice précédent, on veut que l'appel `renverserListeChainée(chaineGrades)` renvoie la liste chainée représentant `Général → Colonel → Capitaine → Lieutenant → Sergent → Soldat`.

Le code de la fonction utilisera les _primitives_ de l'interface des listes chainées (`creer_liste_vide`, `inserer_en_tete`, etc) dans la version impérative de l'implémentation vue en cours (à l'aide de _tuples_) et redonnée ici.


```python
def creer_liste_vide() :
    return () # tuple vide

def inserer_en_tete(lst, donnée) :
    return (donnée, lst) # c'est le nouveau premier maillon de la chaine

def head(lst) :
    assert not est_vide(lst), "Pas de tête à une liste chainée vide !"
    return lst[0] # c'est ce qu'il y a en position 0 du couple L

def tail(lst) :
    assert not est_vide(lst), "Pas de queue à une liste chainée vide !"
    return lst[1] # c'est ce qu'il y a en position 1 du couple L

def est_vide(lst) :
    return len(lst) == 0

# un test
chaineGrades = creer_liste_vide()
chaineGrades = inserer_en_tete(chaineGrades, "Général") ; chaineGrades = inserer_en_tete(chaineGrades, "Colonel") ; chaineGrades = inserer_en_tete(chaineGrades, "Capitaine")
chaineGrades = inserer_en_tete(chaineGrades, "Lieutenant") ; chaineGrades = inserer_en_tete(chaineGrades, "Sergent") ; chaineGrades = inserer_en_tete(chaineGrades, "Soldat")
objviz(chaineGrades)
```


```python
def renverserListeChainée(maListe) :
    """ Renvoie la liste chainée parcourue dans l'autre sens
    Entrée : une liste chainée
    Sortie : une liste chainée"""
    # compléter votre code
    newChaine = creer_liste_vide()
    ... # plusieurs lignes à compléter
    return newChaine

```


```python
# un test
gradesInversés = renverserListeChainée(chaineGrades)
objviz(gradesInversés)
```

## 🖊️ Exercice : longueur d'une liste chainée

Il peut être utile de connaître la longueur d'une liste chainée.

**1.** Avec l'implémentation d'une liste chainée à l'aide de _tuples_, l'appel `len(maListeChainée)` ne va pas renvoyer la bonne valeur : essayez pour voir ! 



```python
print(len(chaineGrades))
```

En effet, si la liste chainée n'est pas vide, alors elle est codée par un _couple_ de **deux** éléments : la valeur du premier maillon et le _tuple_ représentant le maillon suivant.

Par contre, la définition ***récursive*** ("en poupée russe") d'une liste chainée permet d'envisager un **code récursif** pour la fonction `longueurListeChainée(lst)`.

Compléter le code de cette fonction, dans le cas où la liste chainée passée en argument est codée par un _tuple_ .


```python
def longueurListeChainée(lst) :
    """ renvoie la longueur d'une liste chainée, avec une implémentation à l'aide de tuples"""
    if est_vide(lst): # cas de base
        return ...
    else :
        return ... + longueurListeChainée(...)
    
# un test
chaineGrades = ("Soldat",("Sergent", ("Lieutenant",("Capitaine", ("Colonel", ("Général",() ))))))
L = longueurListeChainée(chaineGrades)
print("Longueur de cette liste chainée =", L)
assert L == 6 , "problème avec le code"
```

**2.** On choisit maintenant d'utiliser la version Orientée Objet pour manipuler des listes chainées (on donne ci-dessous le code vu en cours).

Compléter le code de la fonction `longueur_recur_POO`.


```python
class Maillon :
    def __init__(self, data = None, suivant = None) :
        self.head = data
        self.tail = suivant

def longueur_recur_POO(lst) :
    if ... is None : # cas de base
        return ...
    else :
        return ... + longueur_recur_POO(...)
        
# un test
m6 = Maillon("Général")  # pas besoin de préciser le 2ème argument, c'est None par défaut
m5 = Maillon("Colonel", m6) 
m4 = Maillon("Capitaine", m5)
m3 = Maillon("Lieutenant", m4)
m2 = Maillon("Sergent", m3)
m1 = Maillon("Soldat", m2)

chaineGradesPOO = m1 # on tient la chaine par son premier maillon
objviz(chaineGradesPOO) # visualisation

L = longueur_recur_POO(chaineGradesPOO)
print("La longueur de cette liste chainée est ", L)
assert  L == 6 , "problème de code"

```

## 🖊️ Exercice : insérer une donnée dans une liste chainée

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
    if n == 1 :
        newMaillon = Maillon(...) # compléter ici
        chaine.tail = newMaillon
    else :
        inserer(..., chaine.tail, ...)  # compléter ici
        
# un test
m6 = Maillon("Général")  # pas besoin de préciser le 2ème argument, c'est None par défaut
m5 = Maillon("Colonel", m6) 
m4 = Maillon("Capitaine", m5)
m3 = Maillon("Lieutenant", m4)
m2 = Maillon("Sergent", m3)
m1 = Maillon("Soldat", m2)

objviz(m1)
```


```python
inserer("Adjudant", m1, 2)
print("Après insertion de l'adjudant")
objviz(m1)
```

## 🖊️ Exercice : Chaine de désintégration ⚛️

En Enseignement Scientifique de Première, vous avez étudié la désintégration par radioactivité du noyau des atomes. 

La demi-vie d'un noyau correspond à la durée nécessaire, en nombre d'années, pour que la moitié des noyaux initialement présents dans un échantillon se soit désintégrée.

Par exemple, le Radium 226 (${}^{226}Ra$) se désintègre en Radon 222 (${}^{222}Rn$) avec une demi-vie de 1600 ans.

Le Radon 222 peut lui-même se désintégrer en Polonium 218, et ainsi de suite jusqu'à aboutir au Plomb 206 qui est stable.

On a donc une chaine de désintégration :

<img src="" >

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

objviz(desintegrationRa)
```

La chaine de désintégration du Césium est plus courte et elle est instanciée par le code suivant :


```python
desintegrationCs = Chaine()
desintegrationCs.ajout_en_tete(('Ba', 137, 1e100))
desintegrationCs.ajout_en_tete(('Cs', 137, 30.2))

objviz(desintegrationCs)
```

**1.** Un élément stable est un élément qui se situe en bout de chaine de desintégration.

Par exemple, le Plomb 206 est un élément stable car il est en bout de la chaine `desintegrationRa`.

Écrire le code de la fonction `estStable(chaine)` qui prend en paramètre une liste chainée `chaine` non vide et qui renvoie `True` si le maillon de tête est un élément stable.


```python
def estStable(chaine) :
    ...

# test 1
estStable(desintegrationRa)
```


```python
# test 2
desintegrationPb = Chaine()
desintegrationPb.ajout_en_tete(('Pb', 206, 1e100))
estStable(desintegrationPb)
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

**3)** Dans la chaine de désintégration du radon, on trouve trois fois l'isotope `Po` (${}^{218}Po$, ${}^{214}Po$ et ${}^{210}Po$) et une seule fois l'isotope `Rn`.

On veut écrire une fonction **récursive** `nbIsotopes(chaine, nom_atome)` qui renvoie le nombre de fois où `nom_atome`apparaît dans la chaine de désintégration `chaine`.

Par exemple, on veut que l'appel `nbIsotopes(desintegrationRa, 'Po')` renvoie le nombre 3 et que l'appel `nbIsotopes(desintegrationRa, 'Rn')`renvoie le nombre 1.

Compléter le code suivant :


```python
def nbIsotopes(chaine, nom_atome) :
    if chaine.est_vide() :
        return ...
    else :
        occurence = int(chaine.tete()[0] == nom_atome) # conversion d'un booléen en entier avec la régle : True -> 1 et False -> 0
        return occurence + nbIsotopes(...)
    
# quelques tests
nbIsotopes(desintegrationRa, 'Po')
```


```python
nbIsotopes(desintegrationRa, 'Rn')
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


```python

```
