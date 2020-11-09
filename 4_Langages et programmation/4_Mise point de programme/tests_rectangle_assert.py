"""Tests unitaires du module rectangle avec la librairie unittest"""

# Importation du module à tester
from rectangle_correction import Rectangle


# Instanciation de rectangles pour effectuer les tests
rect5x3 = Rectangle(5, 3)
rect6x6 = Rectangle(6, 6)
rect4x7 = Rectangle(4, 7)
rect7x4 = Rectangle(7, 4)


# Tests unitaires de get_largeur() et get_hauteur()
assert rect5x3.get_largeur() == 5
assert rect5x3.get_hauteur() == 3

# Tests unitaires de set_largeur() et set_hauteur() avec valeurs négatives
# => devrait produire une exception, mais bloquer tout le reste du script
#rect5x3.set_largeur(-3)
#rect5x3.set_hauteur(-3)


# Tests unitaire du constructeur avec des valeurs négatives
# => devrait produire une exception, mais bloquer tout le reste du script
#r = Rectangle(-3, -3)


# Tests unitaires de calculer_perimetre()
assert rect5x3.calculer_perimetre() == 16
assert rect6x6.calculer_perimetre() == 24

# Tests unitaires de calculer_aire()
assert rect5x3.calculer_aire() == 15
assert rect6x6.calculer_aire() == 36

# Tests unitaires de calculer_diagonale()
assert rect5x3.calculer_diagonale() > 5.830
assert rect5x3.calculer_diagonale() < 5.832
assert rect6x6.calculer_diagonale() > 8.484
assert rect6x6.calculer_diagonale() < 8.486

# Tests unitaires de calculer_ratio()
assert rect5x3.calculer_ratio() > 0.599
assert rect5x3.calculer_ratio() < 0.601
assert rect6x6.calculer_ratio() > 0.999
assert rect6x6.calculer_ratio() < 1.001


# Tests unitaires de calculer_ratio()
assert rect5x3.etre_carre() == False
assert rect6x6.etre_carre() == True

# Tests unitaires de etre_horizontal()
assert rect5x3.etre_horizontal() == True
assert rect4x7.etre_horizontal() == False

# Tests unitaires de etre_similaire()
assert rect4x7.etre_similaire(rect7x4) == True
assert rect4x7.etre_similaire(rect5x3) == False

# ests unitaires de etre_plus_grand_que()
assert rect4x7.etre_plus_grand_que(rect5x3) == True
assert rect4x7.etre_plus_grand_que(rect6x6) == False

# Tests unitaires de pouvoir_contenir()
assert rect6x6.pouvoir_contenir(rect5x3) == True
assert rect4x7.pouvoir_contenir(rect6x6) == False

# Tests unitaires de creer_representation()
assert rect5x3.creer_representation(version="simple") == "#####\n#####\n#####\n"
assert rect5x3.creer_representation(version="complexe") == "+---+\n|   |\n+---+\n"

