'''
Epreuve pratique : sujet 1

Calcul de la moyenne d'un tableau à double entrée.
'''


def moyenne_tableau_2d(tableau: list) -> float:
    '''Calcule la moyenne d'un tableau à double entrée'''
    somme = 0
    for ligne in tableau:
        for cellule in ligne:
            somme = somme + cellule

    return somme / (len(tableau) * len(tableau[0]))


def mesurer_ecart_relatif(valeur_souhaitee: float, valeur_comparee: float):
    '''
    Calcule l'écart relatif entre deux flottants.
    Précondition : valeur_souhaitee doit être différent de 0
    '''
    return abs(valeur_souhaitee - valeur_comparee) / valeur_souhaitee


def tests():
    '''Réalise des tests sur la fonction crée. Lève une exception si les
    conditions ne sont pas remplies'''
    # seuil de tolérance accepté dans les erreurs
    seuil = 1e-6

    # premier test
    tableau_1 = [[1]]
    valeur_souhaitee = 1.0
    valeur_comparee = moyenne_tableau_2d(tableau_1)
    assert mesurer_ecart_relatif(valeur_souhaitee, valeur_comparee) < seuil

    # second test
    tableau_2 = [[1, 2, 3],
                 [1, 2, 3],
                 [1, 2, 3]]
    valeur_souhaitee = 2.0
    valeur_comparee = moyenne_tableau_2d(tableau_2)
    assert mesurer_ecart_relatif(valeur_souhaitee, valeur_comparee) < seuil

    # troisième test
    tableau_3 = [[3, 3, 6],
                 [5, 3, 4],
                 [10, 1, 1],
                 [2, 3, 7]]
    valeur_souhaitee = 4.0
    valeur_comparee = moyenne_tableau_2d(tableau_3)
    assert mesurer_ecart_relatif(
        valeur_souhaitee, valeur_comparee) < seuil

    # quatrième test
    tableau_4 = [[1, 1, 10],
                 [1, 2, 2],
                 [3, 3, 4]]
    valeur_souhaitee = 3.0
    valeur_comparee = moyenne_tableau_2d(tableau_4)
    assert mesurer_ecart_relatif(valeur_souhaitee, valeur_comparee) < seuil


if __name__ == "__main__":
    tests()
