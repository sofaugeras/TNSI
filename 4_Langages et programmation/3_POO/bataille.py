# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:54:13 2020

@author: SOPHIE
"""
from file import File
from PaquetCartes import PaquetCartes
from carte import Carte

class JeuBataille:
    """
    Jeu de bataille
    Attributs:
        - nom_joueur1 : chaine
        - nom_joueur2 : chaine
        - paquetBataille : liste des cartes
        - cartes_j1 : pile des cartes du joueur 1
        - cartes_j2 : pile des cartes du joueur 2
        - defausse : pile des cartes de la défausse
        - nb_tours : entier, nombre de tours de jeu
        - nb_batailles : entier, nombre de cas d'égalité lors des tirages simultanés
        
        Remarque : certains de ces attributs auraient peut-être plutôt leur place en tant que variable 
        dans la méthode jouer, et vice-versa (?).
        Dans la version proposée ici, le jeu étant automatique, c'est même certain. Mais si on veut
        plus visualiser/intervenir lors du jeu, il vaut mieux avoir les attributs ci-dessus.
        
    Méthodes :
        - __init__
        - jouer : jeu de l'oridnateur contre lui-même. Il est conseillé:
            soit de mettre très peu de cartes (8 au total max)
            soit de préciser un nombre maximal de tours de jeu
            Renvoie :
                match_nul : booléen au nom explicite
                gagnant : chaîne de caractères
                self.nb_batailles
                self.nb_tours
    """
    
    def __init__(self, nom_joueur1 = 'ordi1', nom_joueur2 = 'ordi2'):
        """Constructeur du jeu"""
        self._nomjoueur1 = nom_joueur1
        self._nomjoueur2 = nom_joueur2
        self._paquetBataille = PaquetCartes('bataille',12)
        #On mélange et on distribue entre les 2 joueurs.
        #Pour rappel, distribution(2) distribue toutes les cartes entre les  2 joueurs.
        self._paquetBataille.melange()
        donne = self._paquetBataille.distribution(2)
        #On affecte la première liste au J1
        self._cartesj1 = File(donne[0])
        #Et la seconde au J2
        self._cartesj2 = File(donne[1])
        #Si il reste des cartes, on crée une défausse
        self._defausse = File()
        #Initialisation du nb de tours à 0
        self._nb_tours = 0
        #Crétaion d'un compteur de bataille
        self._nb_batailles = 0
        print("Cartes j1")
        self._cartesj1.printFile()
        print("Cartes j2")
        self._cartesj2.printFile()

    
    def jouer(self) :
        # jouez avec très peu de cartes (4 à 10). Fixez un maximum de nombre de tours de jeu
        poursuivre = True
        print('Partie principale : ')
        print('   - {} : {}'.format(self._nomjoueur1, self._cartesj1.printFile()))
        print('   - {} : {}'.format(self._nomjoueur2, self._cartesj2.printFile()))
        while poursuivre or self._nb_tours < 5  :
            self._nb_tours += 1
            #Cas ou l'un des joueurs n'a plus de carte, on arrête la partie
            if self._cartesj1.estFileVide() or self._cartesj2.estFileVide() :
                poursuivre = False
            else : 
                 #Chaque joueur tire une carte
                 carte1 = self._cartesj1.defiler()
                 carte2 = self._cartesj2.defiler()
            
            #Cas principal
            if carte1.estEgale(carte2) :
                #On lance une bataille uniquement si les 2 joueurs ont un minimum de trois cartes chacun, sinon on arrête le jeu
                if self._cartesj1.getNb_elements() > 3 and self._cartesj2.getNb_elements() > 3 :
                    self._nb_batailles += 1
                    print('   - BATAILLE.')
                    #on crée un liste des cartes cachées
                    setJoueur1 = []
                    setJoueur2 = []
                    setJoueur1.append(carte1)
                    setJoueur2.append(carte2)
                    #Puis on ajoute une carte face cachée
                    setJoueur1.append(self._cartesj1.defiler())
                    setJoueur2.append(self._cartesj2.defiler())
                    #On tire une carte face ouverte pour continuer
                    carte1 = self._cartesj1.defiler()
                    carte2 = self._cartesj2.defiler()
                    #Puis on compare 
                    if carte1.estSuperieure(carte2):
                        #Le joueur1 a gagné, on ajoute les 2 cartes et le set caché dans son paquet
                        self._cartesj1.enfiler(carte1)
                        self._cartesj1.enfiler(carte2)
                        self._cartesj1.enfiler(setJoueur1[0])
                        self._cartesj1.enfiler(setJoueur1[1])
                        self._cartesj1.enfiler(setJoueur2[0])
                        self._cartesj1.enfiler(setJoueur2[1])
                        print('   - {} gagne la bataille.'.format(self._nomjoueur1))
                    else : 
                        #Le joueur2 a gagné, on ajoute les 2 cartes dans son paquet
                        self._cartesj2.enfiler(carte1)
                        self._cartesj2.enfiler(carte2)
                        self._cartesj2.enfiler(setJoueur1[0])
                        self._cartesj2.enfiler(setJoueur1[1])
                        self._cartesj2.enfiler(setJoueur2[0])
                        self._cartesj2.enfiler(setJoueur2[1])
                        print('   - {} gagne la bataille.'.format(self._nomjoueur2))
                else : poursuivre = False
                
            elif carte1.estSuperieure(carte2):
                #Le joueur1 a gagné, on ajoute les 2 cartes dans son paquet
                self._cartesj1.enfiler(carte1)
                self._cartesj1.enfiler(carte2)
                print('   - {} gagne la main.'.format(self._nomjoueur1))
            else : 
                #Le joueur2 a gagné, on ajoute les 2 cartes dans son paquet
                self._cartesj2.enfiler(carte1)
                self._cartesj2.enfiler(carte2)
                print('   - {} gagne la main.'.format(self._nomjoueur2))
                
        #Determine le gagnant
        if self._cartesj1.getNb_elements() == self._cartesj2.getNb_elements():
            match_nul = True
            gagnant = None
        elif self._cartesj1.getNb_elements() > self._cartesj2.getNb_elements():
            match_nul = False
            gagnant = self._nomjoueur1
        else : 
            match_nul = False
            gagnant = self._nomjoueur2
        return (match_nul,gagnant,self._nb_batailles,self._nb_tours)
        
        
