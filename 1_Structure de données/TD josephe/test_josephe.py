# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:35:56 2021

@author: SOPHIE
"""
from josephe import *
#Test pour 1 survivant, tout les 3 soldats avec 41 soldats au départ
# tset = josephe(41, 3, 1)
# print("le Survivant pour 1 survivant, tout les 3 soldats avec 41 soldats au départ est : ",tset.donnee)

# #tests à compléter (ça ne risque pas de fonctionner avec les "?")
# print("un soldat sur deux")
# for i in range(40, 42):
#     print("Survivant pour ", i, "soldats :",josephe(i,2,1).donnee)
# print()

test2 = josephe(41, 3, 2)
#print("2 survivants pour 41 soldats, avec 1 sur 3  :", tset.donnee, tset.suivant.donnee)
print("2 survivants pour 41 soldats, avec 1 sur 3  :", test2.donnee, test2.suivant.donnee)
print(test2)
test3 = josephe(1234,7, 10)
print("10 survivants pour 1234 soldats, avec 1 sur 7  :", test3)