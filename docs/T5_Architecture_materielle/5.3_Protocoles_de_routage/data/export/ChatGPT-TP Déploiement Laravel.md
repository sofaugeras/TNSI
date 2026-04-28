# TP Déploiement Laravel

**User:** Anonymous (faugeras.info@gmail.com)  
**Created:** 12/9/2025 14:38:38  
**Updated:** 12/9/2025 14:39:03  
**Exported:** 3/13/2026 8:57:44  
**Link:** [https://chatgpt.com/g/g-p-68de49a1a09c81918ece9e31066912c6-bts-sio2-laravel/c/6938265d-9364-832e-bf73-5392647be393](https://chatgpt.com/g/g-p-68de49a1a09c81918ece9e31066912c6-bts-sio2-laravel/c/6938265d-9364-832e-bf73-5392647be393)  

## Prompt:
“On continue avec le TP déploiement Laravel (VM / Docker / GitHub Actions)”.

## Response:
Voici un **texte professionnel et pédagogique**, prêt à être inséré dans ton cours ou ton TP, formulé de manière claire et structurée :

On continue avec le TP : Déploiement d’une application Laravel
--------------------------------------------------------------

### (Machine virtuelle • Docker • GitHub Actions)

Ce TP constitue la **suite logique** de votre travail sur la qualité logicielle et l’intégration continue. Après avoir testé et validé votre application localement, l’objectif est désormais de **maîtriser plusieurs stratégies de déploiement** utilisées en environnement professionnel.

Le TP est organisé en trois volets complémentaires :

1.  **Déploiement sur une machine virtuelle locale**  
    Mise en place d’un serveur Linux minimal (Nginx/Apache, PHP-FPM, MariaDB/MySQL, Composer), configuration des virtual hosts et publication d’une version fonctionnelle de l’application.
2.  **Déploiement via un service Docker**  
    Construction d’images, définition des services (app, nginx, base de données), gestion des volumes et réseaux, puis lancement complet de l’environnement avec `docker compose`.  
    L’objectif : disposer d’un environnement reproductible, versionné et portable.
3.  **Déploiement automatisé via GitHub Actions**  
    Mise en place d’un pipeline CI/CD capable de :
    *   exécuter les tests,
    *   construire l’application,
    *   transférer automatiquement les artefacts vers l’environnement cible (VM ou registry Docker),
    *   déclencher le déploiement final.

Chaque étape vous permettra de comprendre comment une application Laravel passe du **développement local** à une **mise en production maîtrisée**, tout en appliquant les bonnes pratiques de sécurité et d’automatisation.

Si tu veux, je peux maintenant :

*   structurer entièrement le TP en trois parties,
*   créer les consignes élèves + version corrigée,
*   générer les scripts (Nginx, Dockerfile, docker-compose, workflow GitHub Actions),
*   préparer une fiche d’évaluation ou une grille de compétences.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)