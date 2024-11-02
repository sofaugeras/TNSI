2"""
Exercice PizzaDrive sur les exceptions

Le stagiaire qui a développé ce prototype débute dans le langage Python.
Aidez le à rendre ce programme plus robuste à l'aide des exceptions
"""

class PizzaDrive():
    """Classe représentant un drive pour commander des pizzas"""


    def __init__(self):
        """Initialise le PizzaDrive"""
        self.stock = [2, 3, 4]
        self.choix_client = -1

    def prendre_la_commande(self):
        """Affiche le menu pour l'utilisateur et enregistre son choix"""
        # Affiche le menu
        print("===== Pizza drive =====")
        print(f" 0 - pizza 3 fromages   (plus que {self.stock[0]})")
        print(f" 1 - pizza périgourdine (plus que {self.stock[1]})")
        print(f" 2 - pizza savoyarde    (plus que {self.stock[2]})")

        # Prend la commande du client
        while self.choix_client not in (0, 1, 2, 3):
            self.choix_client = int(input("Votre choix ? "))

        # Gère la commande du client
        self.stock[self.choix_client] -= 1

        # Message de confirmation
        print("Vous pouvez venir chercher votre pizza dans 30 minutes")
        self.choix_client = -1


if __name__ == "__main__":
    miam = PizzaDrive()
    while 1:
        miam.prendre_la_commande()
