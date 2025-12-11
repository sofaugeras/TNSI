# Algos récursif 🔂

## Factorielle récursive

??? note "Factorielle récursive"

    ```python linenums='1'
    def factorielle(n):
        if n == 1:
            return 1
        else:
            return n * factorielle(n - 1)
    ```

## PGCD récursif

??? note "PGCD récursif"

    ```python linenums='1'
    def pgcd(a, b):
        if b == 0:
            return a
        else:
            return pgcd(b, a%b)
    ```

## Puissance récursive (simple)

??? note "Puissance récursive "

    ```python linenums='1'
    def puissance(x, n):
        if n == 0:
            return 1
        else:
            return x * puissance(x, n-1)
    ```

## Puissance récursive (optimisée)

??? note "Puissance récursive"

    ```python linenums='1'
    def puissance(x, n):
        if n == 0:
            return 1
        else:
            if n % 2 == 0:
                return puissance(x*x, n//2)
            else :
                return x*puissance(x*x, (n-1)//2)
    ```

## Recherche dichotomique récursive (avec slicing)
*Note : le slicing de liste n'est pas au programme de NSI.*

??? note "Recherche dichotomique récursive"

    ```python linenums='1'
    def recherche(lst, m):
        if len(lst) == 1: 
            if lst[0] == m:
                return True
            else :
                return False
        else:              
            mid = len(lst)//2
            if lst[mid] > m:
                return recherche(lst[:mid], m)
            else :
                return recherche(lst[mid:], m)
    ```