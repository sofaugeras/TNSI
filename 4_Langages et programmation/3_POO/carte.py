# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:24:52 2020

@author: SOPHIE
"""

class Carte:
    """Carte d'un paquet de cartes, pour jouer à différents jeux. On reste dans les paquets 32/52/54 cartes ou tarot
    
    Attributs : 
        - couleur : chaine de caractères, en général coeur/carreau/pique/trèfle, mais peut
            aussi être plus exotique batons/coupes/deniers/épées. On peut aussi avoir "atout" ou "joker"
        - hauteur : chaine de caractères, en général de "as" à "roi", 
            variantes "un" à "vingt et un" popur les atouts, "aucune" pour les jokers
        - valeur : entier (en général), dépend du jeu. 
            Dans un langage fortement typé c'est un flottant (valeurs 0.5 au tarot)

    Méthodes :
        init()
        getCouleur()
        getHauteur()
        getValeur()
        setValeur()
        estSuperieure(autre)  : renvoie un booléen vrai si l'objet Carte est de valeur supérieure à celle
            d'un autre objet Carte
        estEgale(autre)
    """
    
    def __init__(self,couleur,hauteur,valeur = 0):
        """
        Constructeur de la classe Carte
        @param:   
            - couleur : chaine de caractères, en général coeur/carreau/pique/trèfle, mais peut
            aussi être plus exotique batons/coupes/deniers/épées. On peut aussi avoir "atout" ou "joker"
            - hauteur : chaine de caractères, en général de "as" à "roi", 
            variantes "un" à "vingt et un" popur les atouts, "aucune" pour les jokers
            - valeur : entier (en général), dépend du jeu. 
            Dans un langage fortement typé c'est un flottant (valeurs 0.5 au tarot)
        Résultat : 
            ne retourne rien, crée une nouvelle Carte
        """
        self._couleur = couleur
        self._hauteur = hauteur
        self._valeur = valeur
        
    # méthodes
    def estSuperieure(self,autre):
        """
        Compare les valeurs de deux objets Carte
        @param : autre, objet de classe Carte
        @result : booléen Vrai si la valeur de la Carte self est supérieure à la valeur de la Carte autre
        """
        return self._valeur > autre.getValeur()
    #Correction
    def estEgale(self,autre):
        """
        Compare les valeurs de deux objets Carte
        @param : autre, objet de classe Carte
        @result : booléen Vrai si la valeur de la Carte self est égale à la valeur de la Carte autre
        """
        return self._valeur == autre.getValeur() 
    
    # méthodes getters/setters
    def getCouleur(self):
        """
        @param : pas de parametre dans cette méthode
        @result : renvoie la couleur de l'objet carte
        """
        return self._couleur
    def getHauteur(self):
        """
        D@param : pas de parametre dans cette méthode
        @result : renvoie la hauteur de l'objet carte
        """
        return self._hauteur
    def getValeur(self):
        """
        @param : pas de parametre dans cette méthode
        @result : revoie la valeur de l'objet carte
        """
        return self._valeur   
    def setValeur(self,nouvValeur):
        """
        @param : entier (en général) ou flottant, nouvelle valeur de la carte
        @result : ne renvoie rien, mais modifie la valeur de l'objet Carte
        """
        self._valeur = nouvValeur
    
    def __repr__(self):
        return f'{self._hauteur} de {self._couleur}, valeur {self._valeur}'
        