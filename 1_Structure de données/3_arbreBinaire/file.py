# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:21:55 2021

@author: SOPHIE
"""

class File:
    """
    Gère les files FIFO
    Attributs :
        - file : liste d'éléments à priori du même type
        - nb_elements : taille de la file
        - premier : premier élément de la file
        - dernier : dernier élément de la file
    Méthodes :
        - __init__(liste = []) : constructeur, renvoie une file vide si liste n'est pas renseigné.
            Sinon renvoie une file constituée des éléments de la liste
        - tete : renvoie l'élément en tête de la file, la file étant non vide
        - enfiler(element) : insère element en fin de file 
        - defiler : supprime l'élément en tête de la file. On peut le renvoyer éventuellement.
            Si la file est vide, renvoie None
        - estFileVide : teste si la file est vide
        - getters pour nb_elements, premier et dernier
    """
    def __init__(self,liste = None):
        """Constructeur de la file
        Remarque : écrire self._file = liste copie l'adresse de liste dans self._file. Ceci peut poser
        des problèmes. En effet, si par la suite on modifie liste, alors on modifiera aussi self._file"""
        self._file = []
        if liste == None:
             self._file = []
             self._nb_elements = 0
             self._premier = None
             self._dernier = None
        else:
            self._file.extend(liste)
            self._nb_elements = len(self._file)
            self._premier = self._file[0]
            self._dernier = self._file[len(self._file)-1]
  
  
    def estFileVide(self):
        return not bool(self._file)
        
    def enfile(self,element):
        self._file.append(element)
        self._dernier = self._file[len(self._file)-1]
        self._nb_elements += 1
        
    def defile(self): 
        if self.estFileVide() :
            return None
        else : 
            elt = self._file.pop(0)
            self._nb_elements -= 1
            if self.estFileVide() : 
                self._premier = None
            else : self._premier = self._file[0]
            return elt
        
    # getters
    def premier(self):
        return self._premier
    def dernier(self):
        return self._dernier
    def getNb_elements(self):
        return self._nb_elements
    
    # une petite méthode d'instrumentation ça peut parfois aider :-)
    def printFile(self):
        print("Contenu de la file : ")
        for element in self._file:
            print(element)