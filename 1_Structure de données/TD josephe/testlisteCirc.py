# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:43:23 2021

@author: SOPHIE
"""

from listeCirc import ListeCirc

# quelques tests
liste_vide = ListeCirc()
print("test liste vide : ", liste_vide, "--> est vide : ", liste_vide.estVide())

maliste = ListeCirc(0)
for i in range(1,5) :
    maliste.ajoutfin(i)

print("La liste : ",maliste)
print("longeur de maliste :", maliste.longueur())
# print("lecture des éléments d'indices 1 et 5 :",maliste.lire(1),maliste.lire(5))
# print()

noeudcourant = maliste.tete
print(noeudcourant)

maliste.supprimerCourant(noeudcourant.suivant, noeudcourant.suivant.suivant)
print("La liste apres suppression element +2 : ",maliste)

# print("ordre inverse")
# maliste2 = CelluleL(10,liste_vide)
# for i in range(9,0,-1) :
#     maliste2 = CelluleL(i,maliste2)
# print(maliste2)

# i = 5
# print("Suppression puis ajout de l'élément d'indice ",i)
# maliste = maliste.supprimer(i)
# print("Après suppression : ",maliste, "de longueur ",maliste.longueur)
# maliste = maliste.inserer(i,i)
# print("Après insertion : ",maliste, "de longueur ",maliste.longueur)