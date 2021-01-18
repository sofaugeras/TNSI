# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:51:56 2021

@author: SOPHIE
"""
from file import File

class ArbreB:
    def __init__(self, valeur, gauche = None, droit = None):
        self.noeud = valeur
        self.gauche = gauche
        self.droit = droit
        
    def __repr__(self):
        return str(self.noeud) +str(self.gauche).replace('None','.')+str(self.droit).replace('None','.')
    
    def est_Vide(self):
        return self.noeud is None
    
    def estFeuille(self):
        return self.gauche is None and self.droit is None and self.noeud is not None
    
    def taille(self):
        """retourne la taille de l'arbre"""
        # condition d'arrêt
        if self.est_Vide():
            return 0
        # Appel récursif
        if self.estFeuille() :
            return 1
        
        taille_gauche = 0
        taille_droite = 0
        
        if not self.gauche is None:
            taille_gauche = self.gauche.taille()
            
        if not self.droit is None :
            taille_droite = self.droit.taille()
        
        return 1 + taille_gauche + taille_droite

    def hauteur(self):
        """retourne la hauteur de l'arbre"""
        hauteur_gauche = 0
        hauteur_droite = 0
        if self.noeud is None:
            return 0
        if not self.gauche is None:
            hauteur_gauche = self.gauche.hauteur()
        if not self.droit is None : 
            hauteur_droite = self.droit.hauteur()
        
        return 1 + max( hauteur_gauche, hauteur_droite)
    
    def parcoursPrefixe(self):
        # Condition d'arrêt
        if self.noeud is None:
            return []
        # Appel récursif et retourne la réponse
        # La valeur est insérée AVANT les appels
        liste_gauche = []
        liste_droite = []
        if not self.gauche is None:
            liste_gauche = self.gauche.parcoursPrefixe()
        if not self.droit is None:
            liste_droite = self.droit.parcoursPrefixe()
        return [self.noeud] + liste_gauche + liste_droite
    
    def parcoursInfixe(self):
        # Condition d'arrêt
        if self.noeud is None:
            return []
        # Appel récursif et retourne la réponse
        # La valeur est insérée AVANT les appels
        liste_gauche = []
        liste_droite = []
        if not self.gauche is None:
            liste_gauche = self.gauche.parcoursInfixe()
        if not self.droit is None:
            liste_droite = self.droit.parcoursInfixe()
        return [] + liste_gauche + [self.noeud] + liste_droite
    
    def parcoursSuffixe(self):
        # Condition d'arrêt
        if self.noeud is None:
            return []
        # Appel récursif et retourne la réponse
        # La valeur est insérée AVANT les appels
        liste_gauche = []
        liste_droite = []
        if not self.gauche is None:
            liste_gauche = self.gauche.parcoursSuffixe()
        if not self.droit is None:
            liste_droite = self.droit.parcoursSuffixe()
        return [] + liste_gauche + liste_droite  + [self.noeud]
    
    def parcoursLargeur(self):
       pass