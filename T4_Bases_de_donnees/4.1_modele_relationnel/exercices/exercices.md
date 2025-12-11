# Exercices d'entraînement

## Exercice 1

_D'après un exercice de Frédéric Junier publié sous licence CC BY SA_

???+ question "Le parc informatique"

	On considère la relation suivante qui liste les postes informatiques dans une entreprise.

	![Les postes](./data/relation_postes.png){: .center width=80% }

	Cette relation respecte bien le principe d’unicité car chaque nuplet est identifié de façon unique
	par la valeur de l’attribut `num_serie` ou même par la valeur de l’attribut `nom_poste`.

	En revanche la relation présente de nombreuses redondances. Ces répétitions sont liées au fait
	qu’un nuplet ne contient pas des données sur une seule mais sur trois entités distinctes du monde
	réel :
	* les attributs num_serie et nom_poste caractérisent une entité _poste informatique_ ;
	* les attributs nom_modele, fabricant et annee caractérisent une entité _modèle de poste_ ;
	* les attributs nom_systeme et version caractérisent une entité _système d’exploitation_.

	On peut résumer ceci dans le graphique suivant : 

	![redondances](./data/redondances.png){: .center width=80% }

    **1.** Question 1.   
    Donner quelques exemples d’anomalies que peut entraîner la redondance d’informations pour une relation. 
	On considérera les situations suivantes : on insère un nouveau nuplet, on modifie une valeur d’attribut 
	redondant, on supprime un nuplet.

    ??? success "Solution"

        * On insère un nouveau nuplet : si celui-ci contient des informations redondantes dans la table 
		(par exemple le nom du système exploitation dans la base exemple), alors il faut les saisir à 
		l’identique sinon la cohérence de la table est cassée: aucune sélection selon ces informations 
		ne sera possible.
		
		* On modifie une valeur d’attribut redondant : il faut modifier ces valeurs pour toutes les redondances 
		de cette valeur dans la table sinon la cohérence de la table est cassée.
		
		* On supprime un nuplet : on risque de supprimer des informations utiles de la base par exemple 
		le nom d’un système d’exploitation disponible sur le serveur mais qui n’est plus déployé sur un poste actif.

    **2.** Question 2.   
	Pour éliminer les redondances, ont peut séparer la base de données en trois relations, une par entité, 
	en éliminant les doublons dans les relations `modele` et `systeme`. Proposer un schéma relationnel.

    ??? success "Solution"

        ![3 relations](./data/trois_relations.png){: .center width=50% }

	**3.** Question 3.  
	On donne les extraits de tables suivants : 

	Relation `modele`

	| id_modele | nom | fabricant | annee| 
	|:---------:|:-------:|:------------:|:------------:|
	| 5| hp probook 400 | hp | 2019| 

	
	Relation `systeme`

	| id_systeme | nom | version |  
	|:---------:|:-------:|:------------:|
	| 4          | fedora linux          | 36  | 

	En utilisant le SGBD de la question 2, donner donner l'extrait de la relation `poste` contenant 
	uniquement le premier enregistrement correspondant au numéro de série S2069FST

	??? success "Solution"

		Relation `poste`

		| num_serie | nom | id_modele | id_systeme| 
		|:---------:|:-------:|:------------:|:------------:|
		| S2069FST| Portable-01 | 5 | 4| 



## 2025 Centre Etrangers Groupe 1 Sujet 2

!!! abstract "2025 Centre Etrangers Sujet 2"

    Exercice 1 du sujet [Centre étrangers J2 2025](./data/25_NSIJ2G11.pdf)

    ![schéma relationnel](./data/25_NSIJ2G11_1.png)

    ??? note "Q1"
        Les clés primaires permettent d’identifier de manière unique et non nulle chaque occurrence dans une table.

    ??? note "Q2"
        Sans le champ id_match, il serait difficile de référencer de manière unique chaque match, surtout lorsque plusieurs matchs peuvent impliquer les mêmes équipes avec le même score (une équipe peut jouer plusieurs matchs). Cela entraînerait des problèmes pour distinguer les différents matchs.

    ??? note "Q3"
        Le résultat de la requête est :

        |prenom|
        |:--:|
        |Henri|
        |Laure|
        |Brigitte|
        |Laure|

    ??? note "Q4"
        Pour éviter les doublons, on peut utiliser le mot-clé DISTINCT :

        ```SQL
        SELECT DISTINCT prenom 
        FROM joueur 
        WHERE ann_naiss < 1985
        ```
    ??? note "Q5"

        ```SQL
        SELECT nom, ann_naiss, num_port 
        FROM joueur 
        WHERE commune = 'Bois-Plage'
        ```
    ??? note "Q6"

        ```SQL
        SELECT joueur.nom, joueur.prenom
        FROM joueur INNER JOIN equipe 
            ON joueur.id_joueur = equipe.j_1
        WHERE equipe.nom = 'Les Kangourous'
        ```

    ??? note "Q7"

        ```SQL
        UPDATE equipe SET points = 5 
        WHERE nom = 'Volley Warriors'
        ```
    ??? note "Q8"
        Pour respecter la contrainte de référence, avant de supprimer le joueur avec l’identifiant 35, il faut vérifier qu’il n’est référencé dans aucune équipe. Or c’est le cas pour l’équipe Volley Warriors, la suppression n’est pas autorisée sans d’abord mettre à jour ou supprimer les références, d’où les instructions suivantes :

        ```SQL
        UPDATE equipe SET j_4 = NULL 
        WHERE j_4 = 35;
        DELETE FROM joueur 
        WHERE id_joueur = 35
        ```
    ??? note "Q9"

        ```SQL
        SELECT id_match 
        FROM match 
        WHERE eq_1 = 12 OR eq_2 = 12;
        ```
    ??? note "Q10"

        ```SQL
        SELECT match.id_match
        FROM match INNER JOIN equipe 
            ON match.eq_1 = equipe.id_equipe
                   INNER JOIN joueur 
            ON equipe.j_1 = joueur.id_joueur
        WHERE joueur.commune = 'Bois-Plage';
        ```

    ??? note "Q11"
    
        ```SQL
        SELECT DISTINCT joueur.nom, joueur.prenom
        FROM joueur INNER JOIN equipe 
            ON joueur.id_joueur = equipe.j_1
        INNER JOIN match 
            ON match.eq_1 = equipe.id_equipe
        WHERE match.eq_gagnante = match.eq_1
        ORDER BY joueur.nom, joueur.prenom ;
        ```
## 2024 Métropole Sujet J2

!!! abstract "2024 Métropole Sujet J2"

    Exercice 1 du sujet [Métropole J2 2024](./data/24_NSIJ2ME.pdf)

    ![schéma relationnel](./data/24_NSIMEJ2_1.png)

    ??? note "Q1"
        La clé primaire n'aurait pas pu être ``Nom_artiste`` dans la relation CD car un artiste peut créer plusieurs CD. Or la clé primaire doit être unique et non nulle pour identifier chaque occurrence de la table. 

    ??? note "Q2"

        |Nom_artiste|
        |:--|
        |Nightwis|
        |The Rasmus| 

    ??? note "Q3"
        |Annee|
        |:--:|
        |2001|
        |1986|
        |1986|

    ??? note "Q4"
        
        ```SQL
        UPDATE CD 
        SET Annee = 2000
        WHERE Titre_album = "Wishmaster" ;
        ```

    ??? note "Q5"

        ```SQL
        SELECT Titre_album
        FROM CD INNER JOIN ARTISTE
            ON CD.Nom_artisite = Artiste.Nom_artiste
        INNER JOIN Rangement
            ON Rangement.id_album = CD.id_album
        WHERE Numero_etagere = 1
        AND style="Metal" ;

        ```

    ??? note "Q6"
      
        Pour respeccter la contrainte de référence, on doit d'abord supprimer l'enregistrement dans rangement, puis le CD et enfin l'artiste. Une clé éétrangère ne peux jamais référencer une clé primaire inexistante.

        ```SQL
        DELETE FROM Rangement
        WHERE id_album = 5 ;
        DELETE FROM CD
        WHERE CD.Titre_album = "Dead Letters";
        DELETE FROM Artiste
        WHERE Nom_artiste =  "The Rasmus" ;
        ```

    ??? note "Q7"
        Dans un chiffrement symétrique on utilise la même clé pour chiffrer et déchiffrer le message. 

    ??? note "Q8"
        Le chiffrement asymétrique est basé sur l'utilisation de deux clés : une clé publique et une clé privée. La clé publique sert à chiffrer et la clé privée à déchiffrer. 
    
    ??? note "Q9"
        On peut chiffrer la clé C avec la clé publique de bob présente sur le serveur. Seul bob pourra dechiffrer avec sa clé privée. La clé C sera alors lisible et utilisable par bob.
    
## 2024 Métropole Septembre Sujet J1

!!! abstract "2024 Métropole Septembre Sujet J1"

    Exercice 1 du sujet [Métropole septembre J1 2024](./data/24-metropole-sept-j1-ex1.pdf)

    ??? note "Q1"
        CP peut e4être de type entier ou texte. 

    ??? note "Q2"
        Le requête renvoie $5$

    ??? note "Q3"
        L'attribut `téléphone` pourrait servir de clé primaire en cas d'unicité du téléphone sur toutes les occurrences de la table. Ce qui est le cas ici dans l'extrait de la table `Agences`

    ??? note "Q4"
        **couple_voitures_agences**(^^#id_agence, #id_voiture^^)

    ??? note "Q5"
        
        ```sql
        INSERT INTO couple_voitures_agences(id_agence, id_voiture)
        VALUES (5,2) ;
        ```

    ??? note "Q6"
        
        ```sql
        UPDATE couple_voitures_agences
        SET id_agence = 2
        WHERE id_voiture = 2 ;
        ```
        *Remarque :* dans la clause WHERE on ne pourra pas indiqué WHERE id_agence=5. En effet, une agence peut avoir plusieurs voitures. 

    ??? note "Q7"

        ```sql
        SELECT Agence, marque, type
        FROM voitures INNER JOIN couple_voitures_agences
            ON voitures.id_voiture = couple_voitures_agences.id_voiture
        INNER JOIN Agences
            ON couple_voitures_agences.id_agence = agence.id_agence ;
        ```

    ??? note "Q8"
        *Note :* On ne peut pas créer une telle fonction car il faut l’id_voiture de la voiture et rien ne nous permet de le récupérer...

        ```python
        def insert_voiture(liste_attribut, id_agence):
            requete1 = "INSERT INTO Voitures
            (marque, modele, kilometrage, nombre_places, type, carburant)
            VALUES ("+liste_attribut[0]+","+liste_attribut[1]+","+liste_attribut[2]+","+liste_attribut[3]+","+liste_attribut[4]+","+liste_attribut[5]+");"
            # On suppose que l'id_voiture est renvoyé sinon c'est impossible
            id_voiture = execute_requete_insert(requete1)
            requete2 = "INSERT INTO couple_voitures_agences
            VALUES ("+id_agence+","+id_voiture+");"
            reponse = execute_requete_insert(requete2)
            return reponse
        ```

    ??? note "Q9"
        ``liste_attribut`` doit voir autant de paramètres que de colonnes de la table ``voiture`` moins une (la clé primaire est auto_incrémenté, elle n'apparait donc pas dans la requete d'INSERT) et id_agence doit exister dans la table ``Agences``


