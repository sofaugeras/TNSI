# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:42:17 2020

@author: SOPHIE

"""

from listeChainee import Liste

'''
        def lire(self , i) :
            for k in range(i-1):
                k + = 1
            return  k
        
     
        def supprimer(self , i) :
            return
        
        def inserer(self , i, element) :
            return
'''   
print('***Création de la liste***')
truc = Liste()
bidule = Liste("film1" , truc)
maliste = Liste("film2" , bidule)
print('***Création de la liste vide***')
zaff = Liste()
print(zaff, zaff.estVide())
print(zaff, zaff.longueur()) 
L2 = Liste("item1",zaff)
print(maliste)
print('***Test de longueur***')
print(maliste.longueur())
print('***Test de renverser***')
truc2 = maliste.renverserListe()
print(truc2)
print('***Test de concat***')
truc3 = maliste.concat(L2)
print(truc3)
print('***Test de lire n-ieme***')
print(truc3.lire(2))
print('***Test de supprimer n-ieme***')
truc4=truc3.supprimer(1)
print('***Affichage apres le supprimer n-ieme***')
print(truc4)