# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:39:43 2020

@author: SOPHIE
"""
from pile import Pile
import random

# un test parmi d'autres
a=Pile()
print("j'empile")
for i in range(6): 
    a.empile(random.randint(1, 6))
    print(a)
print("je depile")
for i in range(6):
    print(a)
    a.depile()
    