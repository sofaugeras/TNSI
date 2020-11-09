"""Module pour gérer des rectangles

Caractéristiques du module :
    * Les rectangles peuvent être caractérisés par une largeur et une hauteur
    * L'unité pour la largeur et la hauteur est le caractère texte
    * les rectangles pourront être représentés sous 2 formats. Exemples pour un rectangle de 7x3 :
        Format    Format
        simple    complexe
        #######   +-----+
        #######   |     |
        #######   +-----+
"""

# Librairie(s) utilisée(s)
import math

# Métainformations du script
__author__ = "Johnny BEGOOD"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "johnny.begood@geoforme.fr"
__status__ = "Development"
__date__ = "27/08/2020"


class Rectangle:
    """Classe représentant un rectangle"""

    def __init__(self, largeur, hauteur):
        """Initialise les dimensions du rectangle

        Parameters:
            largeur (int): largeur du rectangle
            hauteur (int): hauteur du rectangle
        """
        # On utilise les méthodes mutateurs pour factoriser le code
        self.set_largeur(largeur)
        self.set_hauteur(hauteur)

    def get_largeur(self):
        """Accesseur retournant la largeur du rectangle

        Returns:
            (int): la largeur du rectangle
        """
        return self.largeur

    def get_hauteur(self):
        """Accesseur retournant la hauteur du rectangle

        Returns:
            (int): la hauteur du rectangle
        """
        return self.hauteur

    def set_largeur(self, nouvelle_largeur):
        """Mutateur fixant la largeur du rectangle

        Parameters:
            nouvelle_largeur (int): la nouvelle largeur du rectangle
        """
        # Tests des cas impossibles...
        if nouvelle_largeur <= 0:
            raise Exception("La largeur ne peut pas être négative ou nulle")
        if type(nouvelle_largeur) != int:
            raise Exception("La largeur doit être de type entier")

        # ... et sinon on affecte la valeur passée en paramètre
        self.largeur = nouvelle_largeur

    def set_hauteur(self, nouvelle_hauteur):
        """Mutateur fixant la hauteur du rectangle

        Parameters:
            nouvelle_hauteur (int): la nouvelle hauteur du rectangle
        """
        # Tests des cas impossibles...
        if nouvelle_hauteur <= 0:
            raise Exception("La hauteur ne peut pas être négative ou nulle")
        if type(nouvelle_hauteur) != int:
            raise Exception("La hauteur doit être de type entier")

        # ... et sinon on affecte la valeur passée en paramètre
        self.hauteur = nouvelle_hauteur

    def calculer_perimetre(self):
        """Calcule et retourne le périmètre du rectangle

        Returns:
            (int): le périmètre du rectangle
        """
        return (self.largeur + self.hauteur) * 2

    def calculer_aire(self):
        """Calcule et retourne l'aire du rectangle

        Returns:
            (int): l'aire du rectangle
        """
        return self.largeur * self.hauteur

    def calculer_diagonale(self):
        """Calcule et retourne la longueur de la diagonale du rectangle

        Returns:
            (float): la longueur de la diagonale du rectangle
        """
        return math.sqrt(self.largeur * self.largeur + self.hauteur * self.hauteur)

    def calculer_ratio(self):
        """Calcule et retourne le ratio hauteur/largeur du rectangle

        Returns:
            (float): le ratio hauteur/largeur du rectangle
        """
        return self.hauteur / self.largeur

    def etre_carre(self):
        """Précise si le rectangle est carré ou pas

        Returns:
            (bool): True si le rectangle est carré, False sinon
        """
        if self.hauteur == self.largeur:
            return True
        else:
            return False

    def etre_horizontal(self):
        """Précise si le rectangle est plutôt horizontal ou vertical

        Rectangle plutôt horizontal VS Rectangle plutôt vertical
               10x3                         4x5
            ##########                     ####
            ##########                     ####
            ##########                     ####
                                           ####
                                           ####
        On considérera un rectangle carré comme plutôt horizontal

        Returns:
            (bool): True si le rectangle est plutôt horizontal, False si vertical
        """
        if self.largeur >= self.hauteur:
            return True
        else:
            return False

    def etre_similaire(self, un_autre_rectangle):
        """Précise si le rectangle est similaire à un autre à une rotation de 90 degrés près

        Exemples de rectangles similaires:
              6x3   ~  3x6
            ######     ###
            ######     ###
            ######     ###
                       ###
                       ###
                       ###
        Parameters:
            un_autre_rectangle (Rectangle): l'autre rectangle peut-être similaire

        Returns:
            (bool): True si les rectangles sont similaires, False sinon
        """
        # Vérification si on a bien à faire un un rectangle...
        if type(un_autre_rectangle) != Rectangle:
            raise Exception("Le paramètre doit être un objet de la classe Rectangle")

        # ... et si oui on évalue la similarité
        if (self.largeur == un_autre_rectangle.get_hauteur()) and\
           (self.hauteur == un_autre_rectangle.get_largeur()):
            return True
        else:
            return False

    def etre_plus_grand_que(self, un_autre_rectangle):
        """Précise si le rectangle est plus grand (ou pas) qu'un autre passé en paramètre

        Details:
            * La comparaison de taille se fera avec l'aire des rectangles.
            * Pour être plus grand l'aire devra être strictement plus grande
            * Le rectangle à la base de la comparaison sera représenté par la variable self
            * Le second rectangle sera celui passé en paramètre

        Parameters:
            un_autre_rectangle (Rectangle) : l'autre rectangle avec lequel on veut se comparer

        Returns:
            (bool): True si le rectangle est plus grand, False sinon
        """
        # Vérification si on a bien à faire un un rectangle...
        if type(un_autre_rectangle) != Rectangle:
            raise Exception("Le paramètre doit être un objet de la classe Rectangle")

        # ... et si oui on évalue la taille
        if self.calculer_aire() > un_autre_rectangle.calculer_aire():
            return True
        else:
            return False

    def pouvoir_contenir(self, un_autre_rectangle):
        """Précise si le rectangle peut en contenir un autre

        Details:
            * Le rectangle de référence sera représenté par la variable self
            * Le second rectangle sera passé en paramètre
            * Le test se fera sur la largeur et la hauteur
            * Si la largeur et/ou la hauteur sont identiques on considérera que le rectangle
            ne peut pas contenir l'autre

        Parameters:
            un_autre_rectangle (Rectangle): rectangle dont on veut savoir si il est
            contenu dans le premier

        Returns:
            (bool): True si le premier contient le second, False sinon
        """
        # Vérification si on a bien à faire un un rectangle...
        if type(un_autre_rectangle) != Rectangle:
            raise Exception("Le paramètre doit être un objet de la classe Rectangle")

        # ... et si oui on évalue si l'un peut contenir l'autre
        if self.largeur > un_autre_rectangle.get_largeur() and\
            self.hauteur > un_autre_rectangle.get_hauteur():
            return True
        else:
            return False

    def creer_representation(self, version="simple"):
        """Créer et retourne une chaîne de caractères représentation le rectangle

        Exemple de représentations selon le format :
            Format    Format
            simple    complexe
            #######   +-----+
            #######   |     |
            #######   +-----+

        Parameters:
            version (string): format d'affichage du rectangle

        Returns:
            (string): chaîne de caractères représentant le rectangle
        """
        representation = ""
        if version == "simple":
            for j in range(0, self.hauteur):
                for i in range(0, self.largeur):
                    representation += "#"
                representation += "\n"
        elif version == "complexe":
            for j in range(0, self.hauteur):
                for i in range(0, self.largeur):
                    if (i == 0) or (i == (self.largeur - 1)):
                        if (j == 0) or (j == (self.hauteur - 1)):
                            representation += "+"
                        else:
                            representation += "|"
                    else:
                        if (j == 0) or (j == (self.hauteur - 1)):
                            representation += "-"
                        else:
                            representation += " "
                representation += "\n"
        return representation


# Pour mettre au point le codage de la classe Rectangle
if __name__ == '__main__':
    un_rectangle = Rectangle(10, 5)
    print(un_rectangle.creer_representation(version="complexe"))
