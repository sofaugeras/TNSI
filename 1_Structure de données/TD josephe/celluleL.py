# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:34:02 2021

@author: SOPHIE
"""

class CelluleL:
    def __init__(self , donnee = None , suivant = None) :
        self.donnee = donnee
        self.suivant = suivant
        if self.donnee is None and self.suivant is None :
            self.longueur = 0
        else :
            self.longueur = self.suivant.longueur + 1
    
    def __repr__(self):
        if self.donnee is None :
            return '()'
        else:
            # la 1ère possibilité met l'aspect récursif en avant
            # la 2ème possibilité met l'aspect chaîné en avant
            #return '(' + str(self.donnee) + repr(self.suivant).replace('None','()') + ')'  
            return  str(self.donnee) + '->' + repr(self.suivant)
    
    def estVide(self):
        return self.longueur == 0
    
    def lire(self, k) :
        if k >= self.longueur :
            raise IndexError('Index trop grand')
        else :
            if k == 0:
                return self.donnee
            else:
                self = self.suivant
                return self.lire(k - 1)
    
    def supprimer(self, k):
        if k >= self.longueur :
            raise IndexError('Index trop grand')
        elif k == 0 :
            return CelluleL(self.suivant.donnee,self.suivant.suivant)
        else :
            return CelluleL(self.donnee, self.suivant.supprimer(k-1))
        
    def inserer(self , element, k) :
        # peut insérer en fin de liste avec k = self.longueur
        if k > self.longueur:
            raise IndexError('Index trop grand')
        elif k == 0 and not self.estVide():
            return CelluleL(element,self)
        elif k == 0 and self.estVide():
            return CelluleL(element, CelluleL())
        else :
            return CelluleL(self.donnee, self.suivant.inserer(element, k-1))
