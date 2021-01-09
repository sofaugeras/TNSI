'''
Epreuve pratique : sujet 2

Algorithme glouton : rendu de monnaie
'''

# vos réponses ici


def monnaie(somme: int, pieces: list) -> list:
    '''
    Renvoie la liste des pièces à rendre pour atteindre 'somme' avec
    les pièces de la liste 'piece'

    @param somme: (int) la somme à rendre. >= 0
    @param pieces: (list) les valeurs des pièces, par ordre décroissant.
    @return: (list) les pièces rendues pour atteindre la somme, par ordre
        décroissant.
    '''
    somme_restante = somme
    pieces_a_rendre = []
    position = 0
    while somme_restante > 0 and position < len(pieces):
        if pieces[position] <= somme_restante:
            pieces_a_rendre.append(pieces[position])
            somme_restante -= pieces[position]
        else:
            position += 1
    return pieces_a_rendre


# tests fournis aux candidat. Rien n'est à modifier.


def tests():
    '''réalise des tests sur les fonctions du candidat'''
    pieces = [1]
    somme = 1
    assert monnaie(somme, pieces) == [1]

    pieces = [5, 2, 1]
    somme = 13
    assert monnaie(somme, pieces) == [5, 5, 2, 1]

    pieces = [5, 2, 1]
    somme = 101
    assert monnaie(somme, pieces) == [5] * 20 + [1]

    pieces = [20, 10, 5, 2, 1]
    somme = 138
    assert monnaie(somme, pieces) == [20, 20, 20, 20, 20, 20, 10, 5, 2, 1]


if __name__ == "__main__":
    tests()
