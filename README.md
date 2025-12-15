# LITRevu

LITRevu est une application web développée avec Django permettant aux utilisateurs de partager des critiques de livres et d'articles. Les utilisateurs peuvent demander des critiques via des tickets, répondre à ces demandes, et suivre d'autres utilisateurs pour voir leur flux d'activité.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

*   [Python](https://www.python.org/downloads/) (version 3.8 ou supérieure)
*   [Git](https://git-scm.com/)

## Installation pour le développement

Suivez ces étapes pour configurer l'environnement de développement local.

### 1. Cloner le dépôt

Récupérez le code source du projet :

```bash
git clone <url_du_depot>
cd OC_LITRevu
```

### 2. Créer un environnement virtuel

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.

**Sous Windows :**

```bash
python -m venv venv
venv\Scripts\activate
```

**Sous macOS / Linux :**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

Installez les paquets Python requis listés dans le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

Appliquez les migrations pour créer les tables de la base de données SQLite locale :

```bash
python manage.py migrate
```

### 5. Créer un super-utilisateur (Optionnel)

Pour accéder à l'interface d'administration de Django, créez un compte administrateur :

```bash
python manage.py createsuperuser
```
Suivez les instructions à l'écran pour définir le nom d'utilisateur, l'email et le mot de passe.

### 6. Lancer le serveur de développement

Démarrez le serveur local :

```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Utilisation de l'application

1.  **Inscription/Connexion** : Créez un compte ou connectez-vous.
2.  **Flux** : La page d'accueil affiche les tickets et critiques des personnes que vous suivez, ainsi que vos propres posts.
3.  **Créer un Ticket** : Demandez une critique sur un livre/article.
4.  **Créer une Critique** : Répondez à un ticket existant ou créez une critique libre.
5.  **Abonnements** : Allez dans l'onglet "Abonnements" pour suivre d'autres utilisateurs (recherche par nom d'utilisateur) ou voir qui vous suit.

## Tests

Pour exécuter les tests unitaires de l'application :

```bash
python manage.py test
```

## Structure du projet

*   `authentication/` : Gestion des utilisateurs (inscription, connexion).
*   `reviews/` : Gestion des tickets et des critiques.
*   `follows/` : Gestion des abonnements et blocages entre utilisateurs.
*   `LITRevu/` : Configuration globale du projet Django.
*   `media/` : Dossier de stockage des images uploadées par les utilisateurs.
*   `templates/` : Templates HTML globaux.
*   `db.sqlite3` : Base de données locale.

## Technologies utilisées

*   **Django 5.2** : Framework Web Python.
*   **SQLite** : Base de données relationnelle légère.
*   **HTML5 / CSS3** : Structure et style des pages.
