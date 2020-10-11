# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:13:30 2020

@author: SOPHIE
"""

from PaquetCartes import PaquetCartes

p1 = PaquetCartes('p1', 32)
p1.melange()
print(p1.distribution(2,8))