"""Module pour gerer des rectangles

Caracteristiques du module :
    * Les rectangles peuvent etre caracterise par une largeur et une hauteur
    * L'unite pour la largeur et la hauteur est le caracterise texte
    * les rectangles pourront etre representes sous 2 formats. Exemples pour un rectangle de 7x3 :
        Format    Format
        simple    complexe
        #######   +-----+
        #######   |     |
        #######   +-----+
"""

# Librairie(s) utilisee(s)
import math

class Rectangle:
    """Classe representant un rectangle"""

    def __init__(self, largeur, hauteur):
        """Initialise les dimensions du rectangle

        Parameters:
            largeur (int): largeur du rectangle
            hauteur (int): hauteur du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def get_largeur(self):
        """Accesseur retournant la largeur du rectangle

        Returns:
            (int): la largeur du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def get_hauteur(self):
        """Accesseur retournant la hauteur du rectangle

        Returns:
            (int): la hauteur du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def set_largeur(self, nouvelle_largeur):
        """Mutateur fixant la largeur du rectangle

        Parameters:
            nouvelle_largeur (int): la nouvelle largeur du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def set_hauteur(self, nouvelle_hauteur):
        """Mutateur fixant la hauteur du rectangle

        Parameters:
            nouvelle_hauteur (int): la nouvelle hauteur du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def calculer_perimetre(self):
        """Calcule et retourne le perimetre du rectangle

        Returns:
            (int): le perimetre du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def calculer_aire(self):
        """Calcule et retourne l'aire du rectangle

        Returns:
            (int): l'aire du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def calculer_diagonale(self):
        """Calcule et retourne la longueur de la diagonale du rectangle

        Returns:
            (float): la longueur de la diagonale du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def calculer_ratio(self):
        """Calcule et retourne le ratio hauteur/largeur du rectangle

        Returns:
            (float): le ratio hauteur/largeur du rectangle
        """
        #  TODO : completer le code de la méthode
        pass

    def etre_carre(self):
        """Precise si le rectangle est carre ou pas

        Returns:
            (bool): True si le rectangle est carre, False sinon
        """
        #  TODO : completer le code de la méthode
        pass

    def etre_horizontal(self):
        """Precise si le rectangle est plutot horizontal ou vertical

        Rectangle plutot horizontal VS Rectangle plutot vertical
               10x3                         4x5
            ##########                     ####
            ##########                     ####
            ##########                     ####
                                           ####
                                           ####
        On considerera un rectangle carre comme plutot horizontal

        Returns:
            (bool): True si le rectangle est plutot horizontal, False si vertical
        """
        #  TODO : completer le code de la méthode
        pass

    def etre_similaire(self, un_autre_rectangle):
        """Precise si le rectangle est similaire a� un autre a� une rotation de 90 degres pres

        Exemples de rectangles similaires:
              6x3   ~  3x6
            ######     ###
            ######     ###
            ######     ###
                       ###
                       ###
                       ###
        Parameters:
            un_autre_rectangle (Rectangle): l'autre rectangle peut-ere similaire

        Returns:
            (bool): True si les rectangles sont similaires, False sinon
        """
        #  TODO : completer le code de la méthode
        pass

    def etre_plus_grand_que(self, un_autre_rectangle):
        """Precise si le rectangle est plus grand (ou pas) qu'un autre passe en parametre

        Details:
            * La comparaison de taille se fera avec l'aire des rectangles.
            * Pour être plus grand l'aire devra etre strictement plus grande
            * Le rectangle à la base de la comparaison sera represente par la variable self
            * Le second rectangle sera celui passe en parametre

        Parameters:
            un_autre_rectangle (Rectangle) : l'autre rectangle avec lequel on veut se comparer

        Returns:
            (bool): True si le rectangle est plus grand, False sinon
        """
        #  TODO : completer le code de la méthode
        pass

    def pouvoir_contenir(self, un_autre_rectangle):
        """Precise si le rectangle peut en contenir un autre

        Details:
            * Le rectangle de refrence sera represente par la variable self
            * Le second rectangle sera passe en parametre
            * Le test se fera sur la largeur et la hauteur
            * Si la largeur et/ou la hauteur sont identiques on considerera que le rectangle
            ne peut pas contenir l'autre

        Parameters:
            un_autre_rectangle (Rectangle): rectangle dont on veut savoir si il est
            contenu dans le premier

        Returns:
            (bool): True si le premier contient le second, False sinon
        """
        #  TODO : completer le code de la méthode
        pass

    def creer_representation(self, version="simple"):
        """Creer et retourne une chaine de caracteres representation le rectangle

        Exemple de representations selon le format :
            Format    Format
            simple    complexe
            #######   +-----+
            #######   |     |
            #######   +-----+

        Parameters:
            version (string): format d'affichage du rectangle

        Returns:
            (string): chaine de caracteres representant le rectangle
        """
        #  TODO : completer le code de la méthode
        pass


# Pour mettre au point le codage de la classe Rectangle
if __name__ == '__main__':
    #  TODO : completer le code pour mettre au point votre classe Rectangle
    pass



