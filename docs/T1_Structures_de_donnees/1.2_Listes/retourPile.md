# Retour sur la Pile

Où comment coder une interface de Pile à l'aide d'une liste chaînée et de la classe  `Cellule`.

## 1. Rappel : Les listes chaînées

Lorsque l'implémentation de la liste fait apparaître une chaîne de valeurs, chacune pointant vers la suivante, on dit que la liste est une liste **chaînée**.

![](data/listechainee.png){: .center}

**Implémentation choisie :**

- Une liste est caractérisée par un ensemble de cellules.<br />
- Le lien (on dira souvent le «pointeur») vers la variable est un lien vers la première cellule, qui renverra elle-même sur la deuxième, etc.<br />
- Chaque cellule contient donc une valeur et un lien vers la cellule suivante.<br />
- Une liste peut être vide (la liste vide est notée ```x``` ou bien ```None``` sur les schémas)

### 2 Exemple d'implémentation minimale d'une liste chaînée

```python
class Cellule :
    
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante
```

Cette implémentation rudimentaire permet bien la création d'une liste :

```python
lst = Cellule(3, Cellule(5, Cellule(1,None)))
```

La liste créée est donc :  
![](data/ex1.png){: .center}

Mais plus précisément, on a :
![](data/ex2.png){: .center}

!!! abstract "A faire"
    === "Enoncé"
         retrouvez comment accéder aux éléments 3, 5 et 1.

    === "Correction"
        pour 3 : lst.contenu <br />
        pour 5 : lst.suivante.contenu <br />
        pour 1 : lst.suivante.suivante.contenu

## 2. Pile avec Cellule

À l'aide d'une liste chaînée et de la classe  `Cellule` créée ci dessus : 

Nous avons créé la classe  `Cellule` :

```python
class Cellule :
    
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante
```

!!! abstract "Exercice"
    === "Enoncé"
        à l'aide cette classe, re-créer une classe `Pile` disposant exactement de la même interface que dans l'exercice précédent.

        ```python
        class Cellule :
    
            def __init__(self, contenu, suivante):
                self.contenu = contenu
                self.suivante = suivante

        class Pile:
            def __init__(self):
                self.data = None
            
            def est_vide(self):
                return self.data == None
            
            def empile(self, x):
                pass
            
            def depile(self):
                #on récupère la valeur à renvoyer
                # on supprime la 1ère cellule  
                return 
            
            def __str__(self):
                s = "|"
                c = self.data
                while c != None :
                    s += str(c.contenu)+"|"
                    c = c.suivante
                return s

        p = Pile()
        print(p.est_vide()) #True
        p.empile(5) #5
        print(p.est_vide()) #False
        p.empile(3) # 3 5
        p.empile(7) # 7 3 5
        p.empile(2) # 2 7 3 5
        print(p)
        p.depile() # 7 3 5
        print(p)
        ```
    === "Correction"

        ```python
        class Cellule :
    
            def __init__(self, contenu, suivante):
                self.contenu = contenu
                self.suivante = suivante
        class Pile:
            def __init__(self):
                self.data = None
            
            def est_vide(self):
                return self.data == None
            
            def empile(self, x):
                self.data = Cellule(x,self.data)
            
            def depile(self):
                v = self.data.contenu #on récupère la valeur à renvoyer
                self.data = self.data.suivante  # on supprime la 1ère cellule  
                return v
            
            def __str__(self):
                s = "|"
                c = self.data
                while c != None :
                    s += str(c.contenu)+"|"
                    c = c.suivante
                return s
        p = Pile()
        print(p.est_vide()) #True
        p.empile(5) #5
        print(p.est_vide()) #False
        p.empile(3) # 3 5
        p.empile(7) # 7 3 5
        p.empile(2) # 2 7 3 5
        print(p)
        p.depile() # 7 3 5
        print(p)
        ```


!!! warning "À retenir"
    pour l'utilisateur, les 2 interfaces de Pile sont strictement identiques. Il ne peut pas savoir, en les utilisant, l'implémentation qui est derrière. <br />
    ![](data/xkcd.png){: .center}