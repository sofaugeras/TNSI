# Manipulation des base de données

!!! note "Téléchargement"

Dans ce cours, nous poursuivrons l'étude de l'exemple de la base de données de livres de SF et nous verrons des requêtes de sélection avancées ainsi que la manière de fusionner plusieurs tables (Jointure).

## Clause SELECT

### Sélection simple

:hourglass: Supposons que l'on veuille lister seulement les noms et prénoms des auteurs nés avant 1900, on utilisera une clause **WHERE** *condition* :

```python
%sql SELECT NomAuteur, PrenomAuteur from Auteurs WHERE AnneeNaissance < 1900;
```
<table>
    <tr>
        <th>NomAuteur</th>
        <th>PrenomAuteur</th>
    </tr>
    <tr>
        <td>Huxley</td>
        <td>Aldous</td>
    </tr>
    <tr>
        <td>Verne</td>
        <td>Jules</td>
    </tr>
</table>


:hourglass: Pour obtenir les auteurs prénommés *Jules* :

```python
%sql SELECT NomAuteur, PrenomAuteur from Auteurs WHERE PrenomAuteur = 'Jules';
```
<table>
    <tr>
        <th>NomAuteur</th>
        <th>PrenomAuteur</th>
    </tr>
    <tr>
        <td>Verne</td>
        <td>Jules</td>
    </tr>
</table>

Vous voyez que les textes sont délimités par des quotes **'...'**.

***Attention*** : essayez de remplacer **Jules** par **jules** et vous constaterez que la recherche est sensible aux majuscules.

:hourglass: Supposns maintenant que l'on recherche les auteurs dont le prénom commence par **P** <br />
Nous utiliserons une clause *LIKE* de cette manière.

```python
%sql SELECT NomAuteur, PrenomAuteur from Auteurs WHERE PrenomAuteur LIKE 'P%';
```

### Sélection multiple

Il est possible de croiser plusieurs critères à l'aide d'opérateurs booleens : **AND** et **OR**. 

:hourglass: Voici la liste des auteurs français nés après 1900 :

```python
%sql SELECT NomAuteur, PrenomAuteur from Auteurs WHERE IdLangue = 2 AND AnneeNaissance > 1900;
```

### Compter le nombre de réponses d'une requête SELECT

:hourglass: Combien y a t-il d'auteurs nés entre 1900 et 1915 ? <br />
Vous verrez à l'occation l'utilisation de l'opérateur *BETWEEN* pour tester l'appartenance à un intervalle.

```python
nbr = %sql SELECT COUNT(*) from Auteurs WHERE AnneeNaissance BETWEEN 1900 AND 1915;

print(nbr)
print("récupérer juste le nombre : ", nbr[0][0])
```

### Trier les réponses

:hourglass: Nous allons lister tous les auteurs par ordre croissant d'année de naissance

```python
%sql SELECT * from Auteurs ORDER BY AnneeNaissance;
```

:hourglass: par ordre décroissant, on ajoute **DESC** à la fin de la requête

```python
%sql SELECT * from Auteurs ORDER BY AnneeNaissance DESC;
```

### Éviter les occurrences multiples

interrogeons la table **Livres** sur les années de publication, rangées par ordre croissant :

```python
%sql SELECT AnneePubli from Livres ORDER BY AnneePubli;
```

On constate la présence de quelques doublons. <br />
:hourglass:  Pour éviter les redondances dans les résultats, on peut rajouter le mot-clé *DISTINCT* juste après le *SELECT*.

```python
%sql SELECT DISTINCT AnneePubli from Livres ORDER BY AnneePubli;
```

!!! example "A faire
    === "Question"
        1. Donner la liste de tous les titres des livres écrits entre 1920 et 1950.
        2. Combien y en a t-il ?

        ```python
        # Vérification des réponses

        assert reponse_1[3][0] == 'Les Robots'
        assert reponse_2[0][0] == 6
        ```
    === "Correction"


## Requêtes portant sur plusieurs tables

Jusqu'à présent, nos requêtes ne portaient que sur une seule table. Néanmoins notre liste de livres comporte des données en provenance de plusieurs tables simultanément. Nous allons voir comment effectuer des requêtes pour croiser des données en provenance de plusieurs tables.

```python
%sql SELECT * FROM Langues, Auteurs
```

Comme on peut le constater cette requête est peu pertinente car elle affiche toutes les données de chacune des tables sans effectuer de correspondances. La **clé de jointure** apparaît pourtant ici clairement : il s'agit de **id_langue** qui doit permettre de recouper les informations entre les deux tables : il est en effet inutile d'afficher les données pour lesquelles les langues ne correspondent pas entre les deux tables.

### Jointure

La **jointure** consiste à croiser les données de plusieurs tables pour les présenter sous forme d'un seul tableau. On va utiliser ce mécanisme pour afficher clairement la langue de l'auteur plutôt qu'un numéro qui n'est pas forcément très parlant. Nous utiliserons pour cela l'opérateur **JOIN ... ON** :


```python
%sql SELECT NomAuteur, PrenomAuteur, Langue, AnneeNaissance FROM Auteurs JOIN Langues ON Auteurs.IdLangue = Langues.IdLangue
```

Les champs sur lesquels faire la jointure **ayant les mêmes noms dans les 2 tables**, cette requête peut aussi être écrite plus simplement en utilisant le mot-clé **USING** ainsi : 


```python
%sql SELECT NomAuteur, PrenomAuteur, Langue, AnneeNaissance  FROM Auteurs JOIN Langues USING (IdLangue)
```

!!! example "A vous de jouer"
    === "Questions"
        En croisant la table **Livres** avec la table **Auteurs**

        1. récupérer dans la variable `reponse_1` une liste dont les attributs sont **Titre**, **PrenomAuteur**, **NomAuteur** et **AnneePubli**, triée du plus récent au plus ancien.
        2. récupérer dans la variable `reponse_2` une liste dont les attributs sont **Titre**, **PrenomAuteur**, **NomAuteur** et **AnneePubli** écrits en français.

        ```python
        assert reponse_1[0] == ('Ubik', 'Philip', 'K. Dick', 1969)
        assert reponse_2[0] == ('La nuit des temps', 'René', 'Barjavel', 1968)
        ```
    === "Correction"


### Le cas des relations de n à n

Parfois il arrive que les données à collecter se trouvent dans plus que deux tables : c'est le cas des Thèmes pour les livres qui nécessitent l'analyse de 3 tables : **Livres** et **Thèmes** bien sûr, mais aussi la table de relation **RelationsLivreTheme**.


Observez et étudiez la requête suivante : Le principe est d'enchaîner deux jointures **JOIN ... USING** en utilisant ***la table de Relation au milieu***. En effet, la requête se lit de la gauche vers la droite et on ne peut faire de jointure que si on a une clé externe en commun, ce qui n'est par exemple pas le cas entre **Livres** et **Thèmes**.

```python
%sql SELECT Titre, Intitule FROM Livres JOIN RelationsLivreTheme USING (IdLivre) JOIN Themes USING (IdTheme)
```

!!! example "A vous de jouer"
    === "Question"
        Ecrire une requête permettant d'obtenir une liste dont les attributs sont **Titre**, **NomAuteur** et **Langue** triée par ordre croissant de date de naissance de l'auteur.

        Vous stockerez le résultat dans une variable `result`
        ```python
        assert result[0] == ('De la Terre à la Lune', 'Verne', 'Français')
        ```
    === "Correction"