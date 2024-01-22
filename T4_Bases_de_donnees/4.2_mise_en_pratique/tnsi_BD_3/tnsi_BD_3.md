# Manipuler les données avec SQL

!!! note "Téléchargement"
    Vous pouvez télécharger le notebook du cours [ici](./data/tnsi_BD_3.ipynb)

Dans ce dernier TP, nous allons voir comment insérer, mettre à jour ou supprimer des enregistrements dans des tables.


## Insérer un enregistrement dans une table

Nous avons déjà rencontré cerre requète **INSERT**. Elle s'applique que la table soit vide ou nom. 

:hourglass: On peut très bien ajouter par exemple une troisième langue dans notre table **Langues**

```python
%sql INSERT INTO Langues (Langue) VALUES('Klingon');
```

## Mise a jour, effacement : UPDATE et DELETE

Les requêtes **UPDATE** et **DELETE** fonctionnent sur le même modèle que les requêtes **SELECT**.  Attention, on a vite fait d'effacer toutes ses données si on ne configure pas bien sa requête. Une bonne habitude à prendre est de tester d'abord ses critères à l'aide d'un **SELECT**.

Observez les exemples ci-dessous :

```python
%sql SELECT NomAuteur FROM Auteurs WHERE IdAuteur = 10;
```

Modifions le nom de l'auteur grâce à une requête de mise à jour : 

```SQL
**UPDATE** *table* <br>
**SET**  *attribut1* = *valeur1*, *attribut2* = *valeur2*, ...<br>
**WHERE** *critère*;
```

```sql
%%sql 

UPDATE Auteurs 
SET NomAuteur = "Ze Djloule", PrenomAuteur = "Juju"
WHERE IdAuteur=10;

SELECT * FROM Auteurs ;
```

supprimons vite cette entrée ! Nous utiliserons une requête

```sql
**DELETE FROM** *table* **WHERE** *critere*
```

**Attention** : soyez bien sûr de votre critère sous peine de perdre des données importantes !

```sql
%%sql 

DELETE  FROM Auteurs  WHERE IdAuteur=10;
SELECT * FROM Auteurs;
```

### Attention à la cohérence des données

Dans une base de données relationnelle il faut être vigilant lors de la suppression d'enregistrements : en effet la suppression d'un enregistrement entraîne la suppression de sa clé primaire qui peut être utilisée en tant que clé externe dans une autre table. Cela entraîne la corruption des données. Observez l'exemple ci-dessous dans lequel je me suis attribué un livre célèbre sans toucher à la table **Livres**

Il existe en SQL des moyens pour se prémunir de ce type de problèmes mais cela dépasse le cadre de ce cours.


```sql
%%sql
INSERT INTO Auteurs 
    (NomAuteur, PrenomAuteur, IdLangue, AnneeNaissance) 
VALUES
    ("DUPONT", "Olivier", 2, 1850);
    
SELECT Titre, NomAuteur from Livres JOIN Auteurs USING (IdAuteur);
```

!!! example "A faire"
    === "Question"
        1. Réinsérez l'auteur Jules Verne à sa place !
        2. Supprimez tous les livres écrits au 19e sciecle
    === "Correction"