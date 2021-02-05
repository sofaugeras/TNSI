# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:35:34 2021

@author: SOPHIE
"""
from celluleL import CelluleL

def josephe(n, k, s):
    """
    Résoud le problème de Josèphe. Les soldats sont numérotés de 1 à n
    @param n : entier >= 1, nombre initial de soldats
    @param k : entier >= 2, saut entre deux meurtres de soldats
    @param s: entier >=0, nombre de soldats survivants
    @return survivor : liste d'entiers, numéros des sopldats survivants
    """
    survivor = CelluleL()
    #Instanciation de la liste chaînée des soldats
    survivor = CelluleL(n,survivor)
    for i in range(n-1,0,-1) :
        survivor = CelluleL(i,survivor)
        
    #print(survivor)
    #noVictime est la variable temporaire indiquant le n° d'ordre de la victime
    noVictime = 0
    #Tant que la longueur de la liste est supérieur au nb de survivants souhaités, on élimine de la liste
    while survivor.longueur > s :
        #On calcule qui sera la prochaine victime
        noVictime = (noVictime + k -1) % (survivor.longueur)
        #print("La " + str(n-survivor.longueur) + "e victime est le " + str(survivor.lire(noVictime)))
        survivor= survivor.supprimer(noVictime)
        #print(survivor)
    return survivor

#Test pour 1 survivant, tout les 3 soldats avec 41 soldats au départ
# tset = josephe(41, 3, 1)
# print("le Survivant pour 1 survivant, tout les 3 soldats avec 41 soldats au départ est : ",tset.donnee)

# #tests à compléter (ça ne risque pas de fonctionner avec les "?")
# print("un soldat sur deux")
# for i in range(40, 42):
#     print("Survivant pour ", i, "soldats :",josephe(i,2,1).donnee)
# print()

test2 = josephe(10, 2, 1)
#print("2 survivants pour 41 soldats, avec 1 sur 3  :", tset.donnee, tset.suivant.donnee)
print("2 survivants pour 41 soldats, avec 1 sur 3  :", test2.donnee, test2.suivant.donnee)
print(test2)
# test3 = josephe(1234,7, 10)
# print("10 survivants pour 1234 soldats, avec 1 sur 7  :", test3)