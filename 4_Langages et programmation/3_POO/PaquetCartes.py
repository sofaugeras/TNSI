# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from carte import Carte
import random

class PaquetCartes:
    """
    Paquet de cartes
    Attributs:
        - nom : nom du paquet, de préférence correspondant au nom du jeu pour
            lequel il va être utilisé
        - paquet : liste des cartes
    """
    _hauteurs = ["deux","trois","quatre","cinq","six","sept","huit","neuf","dix",
              "valet","dame","roi","as"]
    _couleurs = ["coeur","pique","carreau","trèfle"]
    
    def __init__(self,nom,nbCartes):
        """Constructeur du paquet de cartes"""
        self._nom = nom
        self._nbCartes = nbCartes
        self._paquet = []
        for i in range((len(self._hauteurs)-(self._nbCartes // 4)),len(self._hauteurs)):
            for j in range(len(self._couleurs)):
                self._paquet.append(Carte(self._couleurs[j],self._hauteurs[i],i + 2)) 
           
                
    def getPaquet(self):
        return self._paquet
    
    def __repr__(self):
        liste = ""
        for i in range(len(self._paquet)):
            liste += f'{self._paquet[i]}, '
        return liste
    
    """
    la méthode melange(self)qui mélange le paquet comme son nom l'indique. 
    Cette méthode renvoie self, elle modifie l'attribut __paquet. 
    On utilisera la méthode shuffle(tableau_à_mélanger)de la bibliothèque random
    """
    
    def melange(self):
        """
        D@param : pas de parametre dans cette méthode
        @result : procédure qui mélange sur place le paquet de carte
        Returns
        -------
        None.

        """
        random.shuffle(self._paquet)
        
        
        
        """
        la méthode distribution(nbJoueurs,nbADistribuer = 0)qui renvoie une donne, 
        une liste de listes de Cartes. Il y a autant de listes que de joueurs. 
        Si nbADistribuer = 0, on distribue tout le paquet de manière équitable. 
        Sinon, on donne le nombre de cartes indiquées à chaque joueur. 
        Le nombre de cartes à distribuer et le nombre de joueurs doivent être 
        compatibles avec la taille du paquet de cartes. 
        S'il reste des cartes après distribution, une dernière liste sera ajoutée avec celles-ci
        """
    def distribution(self,nbJoueurs,nbADistribuer = 0):     
        """
        D@param : nbJoueurs : entier, détermine le nb de joueurs à servir
                  nbADistribuer : entier, indique le nb de cartes à distribuer.
        @result : renvoie une liste de liste des cartes distribuées en fonction du nombre de joueurs
        """
        # Gestion des paramètres entrants
        if (nbJoueurs*nbADistribuer > len(self._paquet)) or (nbJoueurs>len(self._paquet)):
            raise Exception('nombre de cartes à distribuer et le nombre de joueurs doivent être compatibles avec la taille du paquet de cartes')
            return None
            
        #Initialisation de la liste des cartes à renvoyer
        dist=[]
        #Calcul du nb de paquets à constituer, initialisation
        n = 0
        if nbADistribuer == 0 :
            n = len(self._paquet)//nbJoueurs
        else : n = nbADistribuer  #On aura autant de liste à ajouter à dist que de joueurs.
       
        for i in range(nbJoueurs):
            main=[]
            #tant que l'on a pas atteint le nb de cartes à distribuer
            while len(main) < n:
                #petite astuce de programmation :
                #On tire un élément de la liste jeu au hasard et en l’y supprimme avec 
                #cette instruction à tiroirs :main.append(jeu.pop(randrange(len(jeu))))
                main.append(self._paquet.pop(random.randrange(len(self._paquet))))
            #Une fois la main du joueur constitué, on l'ajoute à la distribution
            dist.append(main)
        #Traitement du cas : il reste des cartes à distribuer 
        if (len(self._paquet) != 0 ):
            dist.append(self._paquet)
        return dist