"""Code Python contenant un bogue

Contexte :
  => On souhaite ajouter et malaxer des ingrédients pour faire une pâte

Ce qu'on attend du script :
  => que la somme des 3 ingrédients soit correcte : total = 100 + 100 + 100 = 300 grammes

Ce qui se produit vraiment :
  => on obtient un total de 0g, quel que soit les quantités des ingrédients passées en paramètre

"""


def malaxer(farine, oeufs, chocolat):
    """Malaxe les 3 ingrédients dans certaines quantités exprimées en grammes"""
    # Poids total de la pâte
    total = 0

    # Ajout et malaxage de tous les ingrédients
    if farine > 0:
        total == total + farine
    if oeufs > 0:
        total == total + oeufs
    if chocolat > 0:
        total == total + chocolat

    # On retourne le poids total de la pâte
    return total


# Bannière du programme
print("*******************************")
print("*** Top chef malaxator v0.1 ***")
print("*******************************")

# Saisies utilisateur
quantite_farine = int(input("Quelle quantité de farine (en g) : "))
quantite_oeufs = int(input("Quelle quantité d'oeufs (en g) : "))
quantite_chocolat = int(input("Quelle quantité de chocolat (en g) : "))

# On ajoute et malaxe
poids_pate = malaxer(quantite_farine, quantite_oeufs, quantite_chocolat)
print(f"Poids total pâte => {poids_pate}g")