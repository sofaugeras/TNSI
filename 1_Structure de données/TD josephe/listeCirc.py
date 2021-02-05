# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:43:04 2021

@author: SOPHIE
"""

class Noeud:    
    def __init__(self, donnee, suivant = None):    
        self.donnee = donnee    
        self.suivant = suivant
    
    def __repr__(self):
        if self.donnee == None:
            return ""
        else:
            return str(self.donnee)

class ListeCirc:    
    def __init__(self, donnee_tete = None):    
        self.tete = Noeud(donnee_tete)    
        self.queue = self.tete   
        self.tete.suivant = self.queue    
        self.queue.suivant = self.tete
        
    def estVide(self):
        return self.tete.donnee is None
           
    def longueur(self):
        lg = None  
        if self.tete != None:
            courant = self.tete
            fin = self.queue
            lg = 1
            while courant != fin:
                courant = courant.suivant
                lg += 1
        return lg
    
    
    def supprimerCourant(self, precedent, courant):
        # Suppression du noeud courant connaissant le précédent
        if self.tete == self.queue :    # cas particulier : un seul noeud
            self.tete.donnee = None
        elif courant == self.tete :    # cas particulier : suppression de la tête
            self.tete = self.tete.suivant
            self.queue.suivant = self.tete
        elif courant == self.queue :   # cas particulier : suppression de la queue
            self.queue = precedent
            self.queue.suivant = self.tete
        else:                          # cas général
            precedent.suivant = courant.suivant
                            
    def ajoutfin(self, donnee):           
        if self.tete.donnee is None:     # on remplit d'abord la tête  
            self.tete.donnee = donnee 
        else:                            # sinon on crée un nouveau noeud
            nouveauNoeud = Noeud(donnee)
            self.queue.suivant = nouveauNoeud # On ajoute le noeud à la fin
            self.queue = nouveauNoeud         # il devient la nouvelle queue
            self.queue.suivant = self.tete    # et pointe sur la tête
                    
    def __repr__(self):
        if self.tete.donnee is None :
            return 'nil'
        else:
            chaine = str(self.tete.donnee) + "->"
            courant = self.tete
            while courant.suivant != self.tete and courant.suivant.donnee is not None :    
                courant = courant.suivant    
                chaine = chaine + str(courant.donnee) + "->"
            chaine = chaine + "tête"
            return  chaine

    def lire(self, k):
        courant = self.tete
        for i in range(k-1):
            courant = courant.suivant
        return courant
                
    def supprimer(self, k):
        courant = self.tete
        for i in range(k-1):
            precedent = courant
            courant = courant.suivant
        if self.tete == self.queue :    
            self.tete.donnee = None
        elif courant == self.tete :    
            self.tete = self.tete.suivant
            self.queue.suivant = self.tete
        elif courant == self.queue :   
            self.queue = precedent
            self.queue.suivant = self.tete
        else:                         
            precedent.suivant = courant.suivant