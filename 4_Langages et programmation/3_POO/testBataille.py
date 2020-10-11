# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:33:09 2020

@author: SOPHIE
"""
from bataille import JeuBataille

baston = JeuBataille()
(mat,gagnant,nb_batailles,tours) = baston.jouer()
if mat:
    print("match nul, ce n'est pas fréquent. En récompense, calculer la probabilité de cet évènement.")
else:
    if gagnant == None:
        print("trop de tours de jeu. Il y a eu ",nb_batailles," batailles")
    else:
        print(gagnant," a gagné en ",tours," tours de jeu, et ",nb_batailles," batailles.")