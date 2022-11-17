L'opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s'ils sont
différents :  
0 ⊕ 0 = 0 , 0 ⊕ 1 = 1 , 1 ⊕ 0 = 1 , 1 ⊕ 1 = 0  

On représente ici une suite de bits par un tableau contenant des 0 et des 1.


Exemples :

```python
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]
```

Écrire la fonction ```xor``` qui prend en paramètres deux tableaux de même longueur et qui renvoie
un tableau où l’élément situé à position `i` est le résultat, par l’opérateur « ou exclusif », des
éléments à la position `i` des tableaux passés en paramètres.

En considérant les quatre exemples ci-dessus, cette fonction doit passer les tests suivants :

```python
assert(xor(a, b) == [1, 1, 0, 1, 1, 0, 0, 1])
assert(xor(c, d) == [1, 1, 1, 0])
```