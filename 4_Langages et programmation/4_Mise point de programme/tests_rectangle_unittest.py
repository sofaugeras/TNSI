"""Tests unitaires du module rectangle avec la librairie unittest"""

# Librairie(s) utilisée(s)
import unittest
from rectangle_correction import Rectangle

class TestRectangle(unittest.TestCase):
    """Classe gérant les tests unitaires du module rectangle"""

    def setUp(self):
        """Initialisation des tests"""
        # Instanciation de rectangles pour effectuer les tests
        self.rect5x3 = Rectangle(5, 3)
        self.rect6x6 = Rectangle(6, 6)
        self.rect4x7 = Rectangle(4, 7)
        self.rect7x4 = Rectangle(7, 4)

    def tearDown(self):
        """Désactivation des tests"""
        pass

    def test_accesseurs(self):
        """Tests unitaires de get_largeur() et get_hauteur()"""
        self.assertEqual(
            self.rect5x3.get_largeur(),
            5,
            "rect5x3 a une largeur de 5")
        self.assertEqual(
            self.rect5x3.get_hauteur(),
            3,
            "rect5x3 a une hauteur de 3")

    def test_mutateurs(self):
        """Tests unitaires de set_largeur() et set_hauteur() avec valeurs négatives"""
        with self.assertRaises(Exception, msg="Pas de largeur négative"):
            self.rect5x3.set_largeur(-3)
        with self.assertRaises(Exception, msg="Pas de hauteur négatives"):
            self.rect5x3.set_hauteur(-3)

    def test_constructeur(self):
        """Tests unitaire du constructeur avec des valeurs négatives"""
        with self.assertRaises(Exception, msg="Pas de valeurs négatives"):
            r = Rectangle(-3, -3)
        with self.assertRaises(Exception, msg="Pas de valeurs nulles"):
            r = Rectangle(0, 0)
        with self.assertRaises(Exception, msg="Que des entiers en paramètres"):
            r = Rectangle(5.0, 6.5)

    def test_perimetre(self):
        """Tests unitaires de calculer_perimetre()"""
        self.assertEqual(
            self.rect5x3.calculer_perimetre(),
            16,
            "rect5x3 a un périmètre de 16")
        self.assertEqual(
            self.rect6x6.calculer_perimetre(),
            24,
            "rect6x6 a un périmètre de 24")

    def test_aire(self):
        """Tests unitaires de calculer_aire()"""
        self.assertEqual(
            self.rect5x3.calculer_aire(),
            15,
            "rect5x3 a une aire de 15")
        self.assertEqual(
            self.rect6x6.calculer_aire(),
            36,
            "rect6x6 a une aire de 36")

    def test_diagonale(self):
        """Tests unitaires de calculer_diagonale()"""
        self.assertAlmostEqual(
            self.rect5x3.calculer_diagonale(),
            5.831,
            3,
            "rect5x3 a une diagonale de 5.831")
        self.assertAlmostEqual(
            self.rect6x6.calculer_diagonale(),
            8.485,
            3,
            "rect6x6 a une aire de 8.485")

    def test_ratio(self):
        """Tests unitaires de calculer_ratio()"""
        self.assertAlmostEqual(
            self.rect5x3.calculer_ratio(),
            0.6,
            3,
            "rect5x3 a un ratio de 0.6")
        self.assertAlmostEqual(
            self.rect6x6.calculer_ratio(),
            1.0,
            3,
            "rect6x6 a un ratio de 1.0")

    def test_carre(self):
        """Tests unitaires de calculer_ratio()"""
        self.assertFalse(
            self.rect5x3.etre_carre(),
            "rect5x3 n'est pas carré")
        self.assertTrue(
            self.rect6x6.etre_carre(),
            "rect6x6 est carré")

    def test_horizontal(self):
        """Tests unitaires de etre_horizontal()"""
        self.assertTrue(
            self.rect5x3.etre_horizontal(),
            "rect5x3 est horizontal")
        self.assertFalse(
            self.rect4x7.etre_horizontal(),
            "rect4x7 est vertical")
        self.assertTrue(
            self.rect6x6.etre_horizontal(),
            "rect6x6 est horizontal")

    def test_similaire(self):
        """Tests unitaires de etre_similaire()"""
        self.assertTrue(
            self.rect4x7.etre_similaire(self.rect7x4),
            "rect4x7 est similaire à rect7x4"
        )
        self.assertFalse(
            self.rect4x7.etre_similaire(self.rect5x3),
            "rect4x7 n'est pas similaire à rect5x3"
        )
        with self.assertRaises(
                Exception,
                msg="On ne peux pas utiliser autre chose qu'un rectangle en paramètre"):
            self.rect4x7.etre_similaire("un rectangle")

    def test_plus_grand(self):
        """Tests unitaires de etre_plus_grand_que()"""
        self.assertTrue(
            self.rect4x7.etre_plus_grand_que(self.rect5x3),
            "rect4x7 est plus grand rect5x3"
        )
        self.assertFalse(
            self.rect4x7.etre_plus_grand_que(self.rect6x6),
            "rect4x7 n'est pas plus grand que rect6x6"
        )
        with self.assertRaises(
                Exception,
                msg="On ne peux pas utiliser autre chose qu'un rectangle en paramètre"):
            self.rect4x7.test_plus_grand("un rectangle")

    def test_contenir(self):
        """Tests unitaires de pouvoir_contenir()"""
        self.assertTrue(
            self.rect6x6.pouvoir_contenir(self.rect5x3),
            "rect6x6 peut contenir rect5x3"
        )
        self.assertFalse(
            self.rect4x7.pouvoir_contenir(self.rect6x6),
            "rect4x7 ne peut pas contenir rect6x6"
        )
        with self.assertRaises(
                Exception,
                msg="On ne peux pas utiliser autre chose qu'un rectangle en paramètre"):
            self.rect4x7.pouvoir_contenir("un rectangle")

    def test_representation(self):
        """Tests unitaires de creer_representation()"""
        self.assertEqual(
            self.rect5x3.creer_representation(version="simple"),
            "#####\n#####\n#####\n",
            "Pas la bonne forme"
        )
        self.assertEqual(
            self.rect5x3.creer_representation(version="complexe"),
            "+---+\n|   |\n+---+\n",
            "Pas la bonne forme"
        )


# Lancement des tests
if __name__ == '__main__':
    unittest.main()
