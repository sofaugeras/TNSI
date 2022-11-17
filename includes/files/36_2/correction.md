```python linenums='1'
from math import sqrt

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    assert int(point1[0]) == point1[0], "coordonnée non entière"
    assert int(point1[1]) == point1[1], "coordonnée non entière"
    assert int(point2[0]) == point2[0], "coordonnée non entière"
    assert int(point2[1]) == point2[1], "coordonnée non entière"
    return sqrt((point1[0] - point2[0])**2 + ((point1[1] - point2[1]))**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"


def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"


```