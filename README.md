# LITRevu

LITRevu est une application web de critique de livres et d'articles, développée avec Django. Elle permet aux utilisateurs de demander des critiques (via des tickets), de poster des critiques, et de suivre d'autres utilisateurs pour voir leur activité.

## Fonctionnalités

- **Authentification** : Inscription, connexion, déconnexion.
- **Flux d'activité** : Affichage des tickets et critiques des utilisateurs suivis et de l'utilisateur courant.
- **Tickets** : Création, modification et suppression de demandes de critiques (avec upload d'image).
- **Critiques** : Création, modification et suppression de critiques en réponse à des tickets.
- **Abonnements** : Suivi d'autres utilisateurs, désabonnement, recherche d'utilisateurs avec autocomplétion.

## Prérequis

- Python 3.8+
- pip

## Installation

1.  **Cloner le dépôt** :

    ```bash
    git clone <url_du_depot>
    cd OC_LITRevu
    ```

2.  **Créer un environnement virtuel** :

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

4.  **Appliquer les migrations** :

    ```bash
    python manage.py migrate
    ```

5.  **Lancer le serveur de développement** :

    ```bash
    python manage.py runserver
    ```

    L'application sera accessible à l'adresse `http://127.0.0.1:8000/`.

## Utilisation

1.  Créez un compte via la page d'inscription.
2.  Connectez-vous.
3.  Depuis la page d'accueil, vous pouvez :
    -   Voir votre flux d'activité.
    -   Demander une critique (créer un ticket).
    -   Créer une critique (répondre à un ticket existant ou créer un ticket + critique).
    -   Gérer vos abonnements via le bouton "Abonnements".

## Technologies utilisées

-   **Backend** : Django 5.2
-   **Base de données** : SQLite
-   **Frontend** : HTML, CSS (Tailwind CSS, DaisyUI via CDN)

## Note de sécurité

Ce projet est configuré pour un environnement de développement (`DEBUG = True`). La clé secrète (`SECRET_KEY`) est présente dans `settings.py` pour faciliter l'installation locale, mais ne doit jamais être exposée en production.
