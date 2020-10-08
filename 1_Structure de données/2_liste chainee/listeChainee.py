# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:21:04 2020

@author: SOPHIE
"""

class Liste(object) :

    def __init__(self, *args):
        #Premier paramètre : element
        #Second paramètre : liste
        if len(args) == 0:
            # Pas de paramètres : on construit une liste vide
            self.__cell = None
        elif len(args) == 2:
            # Deux paramètres : un élément et une liste
            #On vérifie si la liste est de type Liste
            if isinstance(args[1], Liste):
                #l'élément devient la tête suivi d'une liste
                self.__cell = (args[0], args[1])
            else:
                print("le deuxième argument du constructeur doit être une liste")
        else:
            print("le constructeur de liste prend soit 0 soit 2 arguments")

    def estVide(self) :
        return self.__cell == None
    
    def longueur(self) :
        long = 0
        if self.estVide() :
            long = 0
        else : 
            long =  1 + self.getQueue().longueur()
        return long
  
    def getTete(self) :
        if not self.estVide() :
            return self.__cell[0]
        
    def getQueue(self) :
        if not self.estVide() :
            return self.__cell[1]
    
    def __repr__(self) :
        if self.estVide() :
            return '()'
        else:
            return '(' + repr(self.getTete()) + ',' + repr(self.getQueue()) + ')'
        
    def renverserListe(self):
        L2 = Liste()
        c = self
        while not c.estVide() :
            L2 = Liste(c.getTete(), L2)
            c = c.getQueue()
        return L2

    def lire(self , n) :
        if self.estVide():
            raise IndexError("indice invalide sur lecture")
        if n==0 :
            return self.getTete()
        else : 
            return self.getQueue().lire(n-1)
        
    def insererEnTete(self , element) :
        """
        insere un élement en tête de liste
        
        >>> insere(12, (1,(2,(3,vide))))
        (12, (1, (2, (3, vide))))
        """
        return Liste(self,element)

        
    # def supprimer(self , n) :

        # if self.estVide():
        #     raise IndexError("indice invalide sur suppression")
        # if n==0:
        #     return self.getQueue()
        # else : 
        #     #insere(tete(xs), supprime(i-1,queue(xs)))
        #     return self.getQueue().supprimer(n-1).insererEnTete(self.getTete())

    
    def concat(self,lst2):
        """
        concatène deux listes
    
        >>> concat((0,(1,(2,(3,(4,vide))))) ,(10,(11,(12,(13,(14,vide))))) )
        (0, (1, (2, (3, (4, (10, (11, (12, (13, (14, vide))))))))))
        """
        if self.estVide():
            return lst2
        else:
            return Liste(self.getTete(),self.getQueue().concat(lst2))


