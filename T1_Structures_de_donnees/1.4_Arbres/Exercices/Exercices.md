Pour chacun des exercices, on considérera que la hauteur de la racine vaut 1.

!!! example "Exercice 1"
    Dessinez chacun des arbres ci-dessous. Donner pour chaque arbre, sa taille, sa hauteur et son nombre de feuilles. $\Delta$ représente l'arbre vide. 
    On rappelle que la **hauteur** d'un arbre est définie comme la profondeur maximale des noeuds de l'arbre.
    **1.** $(1, \Delta, \Delta)$
    ??? aide "Correction"
         Taille : 1
        Hauteur : 1
        Feuilles : 1
        ```graphviz dot 
            digraph G1 {
            rankdir=LR
            1
        }
        ```
       
    **2.** $(2, (4,\Delta,(1, (5, \Delta, (3, \Delta, (2, \Delta, \Delta))), \Delta)), \Delta)$
    ??? aide "Correction"
       
        Taille : 6
        Hauteur : 6
        Feuilles : 1


```dot
digraph expression
{
    ratio = 0.8
    label = "Arbre peigne gauche de hauteur 4"
    "0" [label=""];

    "1" [label=""];
    "1d" [label="",shape=plaintext];
    "0" -> "1";
    "0" -> "1d" [style=dashed, arrowhead=none];

    "2" [label=""];
    "2d" [label="",shape=plaintext];
    "1" -> "2";
    "1" -> "2d" [style=dashed, arrowhead=none];

    "3" [label=""];
    "3d" [label="",shape=plaintext];
    "2" -> "3";
    "2" -> "3d" [style=dashed, arrowhead=none];

    "4" [label="",shape=plaintext];
    "4d" [label="",shape=plaintext];
    "3" -> "4" [style=dashed, arrowhead=none];
    "3" -> "4d" [style=dashed, arrowhead=none];
}
```





