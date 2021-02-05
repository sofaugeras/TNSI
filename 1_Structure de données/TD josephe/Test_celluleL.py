# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:34:29 2021

@author: SOPHIE
"""
from celluleL import CelluleL

# quelques tests
liste_vide = CelluleL()
print("test liste vide : ", liste_vide, "est vide : ", liste_vide.estVide(), " et de longueur ",
      liste_vide.longueur)


maliste = CelluleL(5,liste_vide)
print(maliste)
for i in range(4 , -1 , -1) :
    maliste = CelluleL(i,maliste)

print("La liste : ",maliste, "a pour longueur ",maliste.longueur)
print("lecture des éléments d'indices 1 et 5 :",maliste.lire(1),maliste.lire(5))
print()

print("ordre inverse")
maliste2 = CelluleL(0,liste_vide)
for i in range(10) :
    maliste2 = CelluleL(i,maliste2)
print(maliste2)

i = 5
print("Suppression puis ajout de l'élément d'indice ",i)
maliste = maliste.supprimer(i)
print("Après suppression : ",maliste, "de longueur ",maliste.longueur)
maliste = maliste.inserer(i,i)
print("Après insertion : ",maliste, "de longueur ",maliste.longueur)