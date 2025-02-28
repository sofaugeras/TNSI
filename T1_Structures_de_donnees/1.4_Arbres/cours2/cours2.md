# Arbres

![image](./data/banniere.png){: .center width=70%}

![image](./data/BO1.png){: .center}

![image](./data/BO2.png){: .center}

## Arbres binaires de recherche (ABR)

!!! abstract "Définition d'un ABR :heart:"
    Un **arbre binaire de recherche** est un arbre binaire dont les valeurs des nœuds (valeurs qu'on appelle étiquettes, ou clés) vérifient la propriété suivante :

    - l'étiquette d'un nœud est **supérieure ou égale** à celle de **chaque** nœud de son **sous-arbre gauche**.
    - l'étiquette d'un nœud est **strictement inférieure** à celle du **chaque** nœud de son **sous-arbre droit**.

![](./data/exABR.png){: .center}

À noter que l'arbre 3 (qui est bien un ABR) est appelé **arbre filiforme**. 

L'arbre 5 n'est pas un ABR à cause de la feuille 9, qui fait partie du sous-arbre gauche de 3 sans lui être inférieure.

**Remarque :** on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante.

!!! example "Exercice"
    === "Enoncé"
        ![arbre binaire de recherche](./data/abr1.png){: .center}
        1. Complétez cet ABR en y insérant dans l'ordre les clés 2, 15, 29 puis 28.<br />
        2. Quel est le résultat du parcours de cet arbre suivant l'ordre infixe ?

    === "Correction 1."
        ![arbre binaire de recherche](./data/abr1_corr.png){: .center}

    === "Correction 2."
        On retrouve les clés dans l'ordre croissant : 2,5,10,12,15,17,19,20,22,24,28,29

!!! example "To Do"
    === "consigne"
        Créer un nouveau dossier ABR, et dupliquer votre fichiers de la classe Arbre <br />
        Nous allons en réutiliser la majeure partie, puisque un arbre binaire de recherche est un arbre binaire particulier.<br />
        Créer un nouveau fichier de test avec les deux arbres suivants :

        ![arbre_a](./data/abr_a.png){: .center}
        ![arbre_b](./data/abr_b.png){: .center}

        _question :_ Les 2 arbres sont ils des arbres binaires de recherche ?

    === "Correction"
        ```python
        #arbre a
        a = Arbre(5)
        a.gauche = Arbre(2)
        a.droit = Arbre(7)
        a.gauche.gauche = Arbre(0)
        a.gauche.droit = Arbre(3)
        a.droit.gauche = Arbre(6)
        a.droit.droit = Arbre(8)

        #arbre b
        b = Arbre(3)
        b.gauche = Arbre(2)
        b.droit = Arbre(5)
        b.gauche.gauche = Arbre(1)
        b.gauche.droit = Arbre(9)
        b.droit.gauche = Arbre(4)
        b.droit.droit = Arbre(6)
        ```
        a est bien un arbre binaire de recherche. <br />
        b n'est pas un arbre binaire de recherche à cause du 9 et du 4.

### 1. Déterminer si un arbre est un ABR

Employer une méthode récursive imposerait de garder en mémoire dans l'exploration des sous-arbres la valeur maximale ou minimale. Nous allons plutôt utiliser la remarque précédente, et nous servir du parcours infixe.

Méthode : récupérer le parcours infixe dans une liste, et faire un test sur cette liste.


!!! note "Être ou ne pas être un ABR"

    ```python linenums='1'
    def parcoursInfixe(self):
        """parcours infixe
        @param: l'arbre à parcourir
        @return: la liste des noeuds dans l'ordre infixe
        """
        # Condition d'arrêt
        if self.noeud is None:
            return []
        # Appel récursif et retourne la réponse
        # La valeur est insérée AVANT les appels
        liste_gauche = []
        liste_droite = []
        if not self.gauche is None:
            liste_gauche = self.gauche.parcoursInfixe()
        if not self.droit is None:
            liste_droite = self.droit.parcoursInfixe()
        return [] + liste_gauche + [self.noeud] + liste_droite


    def est_ABR(self):
        '''renvoie un booléen indiquant si arbre est un ABR'''
        parcours = self.parcoursInfixe()
        return parcours == sorted(parcours) # on regarde si le parcours est égal au parcours trié 

    ```

```python
assert a.est_ABR() == True
assert b.est_ABR() == False
```

!!! example "Exercice"
    === "Enoncé"
        ré-équilibrer l'arbre b pour que cela devienne un arbre binaire de recherche et tester avec votre fonction ``est_ABR()``
    === "Correction"
        ```python
        c = Arbre(3)
        c.gauche = Arbre(2)
        c.droit = Arbre(5)
        c.gauche.gauche = Arbre(1)
        c.droit.gauche = Arbre(4)
        c.droit.droit = Arbre(9)
        c.droit.droit.gauche = Arbre(9)

        assert c.est_ABR() == True
        ```
        
### 2. Rechercher une clé dans un ABR

Un arbre binaire de taille $n$ contient $n$ clés (pas forcément différentes). Pour savoir si une valeur particulière fait partie des clés, on peut parcourir tous les nœuds de l'arbre, jusqu'à trouver (ou pas) cette valeur dans l'arbre. Dans le pire des cas, il faut donc faire $n$ comparaisons.

Mais si l'arbre est un ABR, le fait que les valeurs soient «rangées» va considérablement améliorer la vitesse de recherche de cette clé, puisque la moitié de l'arbre restant sera écartée après chaque comparaison.


!!! note "Recherche d'une clé dans un ABR :heart:"
    
    ```python
    def recherche_ABR(self, valeur):
        if self is None :
            return False
        
        if self.noeud == valeur :
            return True
        
        if valeur < self.noeud and not self.gauche is None :
            return self.gauche.recherche_ABR( valeur)
        elif valeur > self.noeud and not self.droit is None :
            return self.droit.recherche_ABR(valeur)
        return False

    ```

**Exemple** 

L'arbre ```a``` contient la valeur 8, mais pas la valeur 4.

```python
#Test de la fonction de recherche dans un arbre binaire de recherche
assert a.recherche_ABR(5) == True #Cas ou la valeur recherchée est la racine
assert a.recherche_ABR(0) == True #Cas ou la valeur recherchée est une feuille
assert a.recherche_ABR(4) == False #Cas ou la valeur recherchée n'est pas dans l'arbre
assert a.recherche_ABR(8) == True #Cas ou la valeur recherchée est une feuille et la plus à droite
```


### 3.  Coût de la recherche dans un ABR équilibré
![](./data/rechercheABR.png){: .center}

Imaginons un arbre équilibré de taille $n$. Combien d'étapes faudra-t-il, dans le pire des cas, pour trouver (ou pas) une clé particulière dans cet arbre ?

Après chaque nœud, le nombre de nœuds restant à explorer est divisé par 2. On retrouve là le principe de recherche dichotomique, vu en classe de Première (voir [ici](https://github.com/glassus/nsi/blob/master/Premiere/Theme05_Algorithmique/05_Dichotomie.ipynb)).

S'il faut parcourir tous les étages de l'arbre avant de trouver (ou pas) la clé recherchée, le nombre de nœuds parcourus est donc égal à la hauteur $h$ de l'arbre.

Pour un arbre complet, cette hauteur vérifie la relation $2^h -1= n$. et donc $2^h = n+1$.

$h$ est donc le «nombre de puissance de 2» que l'on peut mettre dans $n+1$. Cette notion s'appelle le logarithme de base 2 et se note $\log_2$.

Par exemple, $\log_2(64)=6$ car $2^6=64$.

Le nombre maximal de nœuds à parcourir pour rechercher une clé dans un ABR équilibré de taille $n$ est donc de l'ordre de $\log_2(n)$, ce qui est très performant !

Pour arbre contenant 1000 valeurs, 10 étapes suffisent.

Cette **complexité logarithmique** est un atout essentiel de la structure d'arbre binaire de recherche.

### 4.  Insertion dans un ABR
L'insertion d'une clé va se faire au niveau d'une feuille, donc au bas de l'arbre. Dans la version récursive de l'algorithme d'insertion, que nous allons implémenter, il n'est pourtant pas nécessaire de descendre manuellement dans l'arbre jusqu'au bon endroit : il suffit de distinguer dans lequel des deux sous-arbres gauche et droit doit se trouver la future clé, et d'appeler récursivement la fonction d'insertion dans le sous-arbre en question.

**Algorithme :**

- Si l'arbre est vide, on renvoie un nouvel objet Arbre contenant la clé.
- Sinon, on compare la clé à la valeur du nœud sur lequel on est positionné :
    - Si la clé est inférieure à cette valeur, on va modifier le sous-arbre gauche en le faisant pointer vers ce même sous-arbre une fois que la clé y aura été injectée, par un appel récursif.
    - Si la clé est supérieure, on fait la même chose avec l'arbre de droite.
    - on renvoie le nouvel arbre ainsi créé.


!!! note "Insertion dans un ABR :heart:"

    ```python
    def insertion(self, cle):
        if self is None :
            # si l'arbre est vide, on crée un arbre avec la clé
            return Arbre(cle)
        if self.gauche is None and cle <= self.noeud :
            self.gauche = Arbre(cle)
            return self
        if self.droit is None and cle > self.noeud :
            self.droit = Arbre(cle)
            return self
        if cle <= self.noeud  :
            return self.gauche.insertion(cle)
        else : 
            return self.droit.insertion(cle)
    ```


**Exemple :** Nous allons insérer la valeur 4 dans l'arbre ```a``` et vérifier par un parcours infixe (avant et après l'insertion) que la valeur 4 a bien été insérée au bon endroit.

![](./data/insertionABR.png){: .center}


```python
a = Arbre(5)
a.gauche = Arbre(2)
a.droit = Arbre(7)
a.gauche.gauche = Arbre(0)
a.gauche.droit = Arbre(3)
a.droit.gauche = Arbre(6)
a.droit.droit = Arbre(8)
```

```python
>>> a.infixe()
0-2-3-5-6-7-8-
>>> a.insertion(4)
<__main__.Arbre at 0x7f46f0507e80>
>>> a.infixe()
0-2-3-4-5-6-7-8-
```
La valeur 4 a donc bien été insérée au bon endroit.

---
## Bibliographie
-	En majeur partie sur la trame du cours de Gilles Lassus – Enseignant NSI ![](data/ccbysa.png) Lycée François Mauriac --  Bordeaux 
-	Cours de Frédéric Mandon ![](data/ccbysa.png)
-	NSI 24 Leçons avec exercices corrigés – Edition Ellipses
-	Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
- Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
---
