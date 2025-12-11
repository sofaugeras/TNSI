# Révision sur la Récursivité

!!! info "Crédits"

    - 2023, Sujet 0.b Ex2 Mise en page et correction par [Franck Chambon](https://e-nsi.gitlab.io/ecrit/)
    - Exercice 1 du [2024 Métropole Septembre Jour 2] correction proposée par rchap sur le forum NSI


## 2023 Sujet 0.b Exercice 2

> D'après 2023, Sujet 0.b, Ex. 2

Cet exercice est consacré à l'analyse et à l'écriture de programmes récursifs.

**1.a)** Expliquer en quelques mots ce qu'est une fonction récursive.

??? success "Réponse"
    Une fonction récursive est une fonction qui possède un appel à elle-même dans son code source.

**1.b)** On considère la fonction Python suivante :

```python
def compte_rebours(n):
    """ n est un entier positif ou nul """
    if n >= 0:
        print(n)
        compte_rebours(n - 1)
```

L'appel `compte_rebours(3)` affiche successivement les nombres `3`, `2`, `1` et `0`.
Expliquer pourquoi le programme s'arrête après l'affichage du nombre `0`.

??? success "Réponse"
    Une fois l'affichage de `0` effectué, il y a un appel récursif `compte_rebours(0 - 1)`.

    Lors de cet appel récursif, `n` vaut `-1`, on ne rentre pas donc dans la structure conditionnelle.

    La pile d'appel récursif se vide sans qu'il ait d'autres instructions effectuées.

    Ainsi le programme s'arrête après avoir affiché `0` et vidé la pile d'appels récursifs.

**2.** En mathématiques, la factorielle d'un entier naturel $n$ est le produit des nombres entiers strictement positifs inférieurs ou égaux à $n$. Par convention, la factorielle de $0$ est $1$. Par exemple :

- la factorielle de $1$ est $1$
- la factorielle de $2$ est $2 × 1 = 2$
- la factorielle de $3$ est $3 × 2 × 1 = 6$
- la factorielle de $4$ est $4 × 3 × 2 × 1 = 24$

Recopier et compléter sur votre copie le programme donné ci-dessous afin que la fonction récursive `fact` renvoie la factorielle de l'entier passé en paramètre de cette fonction. 

Exemple : `#!py fact(4)` renvoie `24`.

```python
def fact(n):
    """ Renvoie le produit des entiers strictement positifs
         et inférieurs ou égaux à n.
    """
    if n == 0:
        return ...  # À compléter
    else:
        return ...  # À compléter
```

??? success "Réponse"

    ```python
    def fact(n):
        """ Renvoie le produit des entiers strictement positifs
            et inférieurs ou égaux à n.
        """
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)
    ```

**3.** La fonction `somme_entiers_rec` ci-dessous permet de calculer la somme des entiers, de `0` à l'entier naturel `n` passé en paramètre.

Par exemple :

- Pour `#!py n = 0`, la fonction renvoie la valeur `0`.
- Pour `#!py n = 1`, la fonction renvoie la valeur `0 + 1 = 1`.
- ...
- Pour `#!py n = 4`, la fonction renvoie la valeur `0 + 1 + 2 + 3 + 4 = 10`.

```python linenums="1"
def somme_entiers_rec(n):
    """ Renvoie, de manière récursive,
     la somme des entiers de 0 à l'entier naturel n.
    """
    if n == 0:
        return 0
    else:
        print(n)  # pour vérification
        return n + somme_entiers(n - 1)
```

L'instruction `#!py print(n)` de la ligne 7 dans le code précédent a été insérée afin de mettre en évidence le mécanisme en œuvre au niveau des appels récursifs.

**3.a)** Écrire ce qui sera affiché dans la console après l'exécution de la ligne suivante : 

```pycon
>>> res = somme_entiers_rec(3)
```

??? success "Réponse"

    ```pycon
    >>> res = somme_entiers_rec(3)
    3
    2
    1
    >>>
    ```

    - L'appel `#!py somme_entiers_rec(3)` affiche `3` puis appelle `#!py somme_entiers_rec(2)`
    - L'appel `#!py somme_entiers_rec(2)` affiche `2` puis appelle `#!py somme_entiers_rec(1)`
    - L'appel `#!py somme_entiers_rec(1)` affiche `3` puis appelle `#!py somme_entiers_rec(0)`
    - L'appel `#!py somme_entiers_rec(0)` n'affiche rien.

**3.b)** Quelle valeur sera alors affectée à la variable `res` ?

??? success "Réponse"

    ```pycon
    >>> res = somme_entiers_rec(3)
    3
    2
    1
    >>> res
    6
    ```

    La valeur `6` est affectée à la variable `res`, la somme $3+2+1+0$.

**4.** Écrire en Python une fonction `somme_entiers` non récursive : cette fonction devra prendre en argument un entier naturel `n` et renvoyer la somme des entiers de `0` à `n` compris. Elle devra donc renvoyer le même résultat que la fonction `somme_entiers_rec` définie à la question 3.

Exemple : `#!py somme_entiers(4)` renvoie `10`.

??? success "Réponse"

    Il y a plusieurs solutions, par exemple :

    ```python
    def somme_entiers(n):
        # style itératif
        somme = 0
        for x in range(n + 1):
            somme += x
        return somme
    ```

    ```python
    def somme_entiers(n):
        # style fonctionnel
        return sum(range(n + 1))
    ```

## 2024 Métropole Jour 2 Exercice 1

!!! exercice "2024 Métropole Jour 2"

    Exercice 1 du [2024 Métropole Septembre Jour 2](./data/2024/24-NSIJ1AN1.pdf)
    
    [Problème de l'arrêt](https://pratique.forge.apps.education.fr/ecrit/recursif/24-ME3-J2-ex1/){ .md-button .md-button--primary }

    **extrait :** <br />

    Dans cet exercice, si `f` est une fonction Python prenant un argument et si `x` est une valeur, on dira qu'un appel `f(x)` termine lorsque l'évaluation de `f(x)` renvoie toujours une valeur au bout d'un nombre fini d'étapes. À l'opposé, un tel appel ne termine pas s'il est possible qu'il effectue des instructions à l'infini.<br />

    **Partie A : boucle while**<br />

    ??? success "Q1"
        Lors de l'exécution de ``f1(7)``, la variable i prend scessivement les valeurs ``7, 8, 9, 10``, la fontion termine
        et renvoie ``10``.

    ??? success "Q2"
        Lors de l'exécution de ``f1(-2)``, la variable ``i`` prend sucessivement les valeurs ``-2, -1, ..., 7, 8, 9, 10``, la fonction termine et renvoie ``10``.

    ??? success "Q3"  
        Lors de l'exécution de ``f1(12)``, la variable ``i`` prend sucessivement les valeurs ``12, 13, 14, 15, 16`` ... <br />
        la fonction ne termine pas.

    ??? success "Q4"  
        La fonction ``f1`` termine lorsque son paramètre est un entier inférieur ou égal à ``10``.

    **Partie B : fonction récursive**<br />

    ??? success "Q5" 
        L'appel ``f2(4)`` termine et renvoie ``6``.

    ??? success "Q6" 
        L'appel ``f2(5)`` ne termine pas car dans les appels sucessifs la variable ``n`` va rester impaire et ne sera donc  jamais nulle.

    ??? success "Q7" 
        L'appel ``f2(n)`` termine si son paramètre est un entier naturel pair.

    ??? success "Q8" 
        La fonction récursive ci-dessous ne termina pour aucun entier ``n``.

        ```python
        def infini(n):
            return infini(n-1)
        ```
    **Partie C : le problème de l'arrêt**<br/>

    ??? success "Q9" 
        Dans le cas où ``arret(code_paradoxe,code_paradoxe)`` renvoie ``True``, alors l'instruction ``infini(42)`` est     exécutée, et elle ne termine pas, donc ``paradoxe(code_paradoxe)`` ne termine pas.

    ??? success "Q10" 
        Dans le cas où ``arret(code_paradoxe, code_paradoxe)`` renvoie ``False``, alors l'instruction return ``0`` est exécutée, donc ``paradoxe(code_paradoxe)`` termine.

    ??? success "Q11" 
        Par conséquent, l'appel ``paradoxe(code_paradoxe)`` ne termine pas si ``arret(code_paradoxe, code_paradoxe)``    renvoie ``True`` et termine si ``arret(code_paradoxe, code_paradoxe)`` renvoie ``False``, ce qui est contradictoire avec la définition de la fonction ``arrêt``.<br />
        On en déduit, par l'absurde, qu'une fonction ``arret`` possédant la propriété souhaitée ne peut exister.

    [Corrigé complet du sujet 2024 Métropole Septembre Jour 2](./data/2024/24NSIJ2ME3_corr.pdf)