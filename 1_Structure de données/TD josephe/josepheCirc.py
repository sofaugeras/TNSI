# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:44:30 2021

@author: SOPHIE
"""
from listeCirc import ListeCirc

def josephe(n, k, s):
    """
    Résoud le problème de Josèphe. Les soldats sont numérotés de 1 à n
    @param n : entier >= 1, nombre initial de soldats
    @param k : entier >= 2, saut entre deux meurtres de soldats
    @param s: entier >=0, nombre de soldats survivants
    @return survivor : liste d'entiers, numéros des sopldats survivants
    """
    survivor = ListeCirc()
    
    #Instanciation de la liste chaînée des soldats
    for i in range(1,n+1) :
        survivor.ajoutfin(i)
    print(survivor)
    nbTues = 0
    i = 1
    noeudcourant = survivor.tete
    #Tant que la longueur de la liste est supérieur au nb de survivants souhaités, on élimine de la liste
    while n-nbTues > s :
        #on progresse dans la liste chainée par cran de k-1
        if (i==(k-1)):
            survivor.supprimerCourant(noeudcourant, noeudcourant.suivant)
            print(survivor)
            noeudcourant = noeudcourant.suivant
            i =1
            nbTues += 1   
        else : 
            noeudcourant = noeudcourant.suivant
            i +=1
    return survivor


# print("un soldat sur deux")
# for i in range(1,42):
#     print("Survivant pour ", i, "soldats :",josephe(i,2,1).tete.donnee)
# print()

tset = josephe(10,2,1)
print("2 survivants pour 41 soldats, avec 1 sur 3  :", tset.tete.donnee, tset.tete.suivant.donnee)
print(tset)
# tset = josephe(1234,7,10)
# print("10 survivants pour 1234 soldats, avec 1 sur 7  :", tset)
