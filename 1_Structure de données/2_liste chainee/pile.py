# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:19:00 2020

@author: SOPHIE
"""

class Pile:
    
    def __init__(self):  
       self.p = []
	
    def est_vide(self):
        return self.p == []

    def depile(self):
        assert not self.est_vide(), "La pile vide ne peut pas être dépilée"
        
        return self.p.pop()
    
    def empile(self, val):
        self.p.append(val)
        
    def sommet(self):
        return self.p[-1]

    def __repr__(self):
        return f"{self.p[-1]}|-"
