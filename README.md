# Gestion du Trafic Aérien

Cette SAE 2.03 est une application web de gestion du trafic aérien entre différents aéroports. Il permet de gérer les aéroports, les pistes, les compagnies aériennes, les types d'avions, les avions et les vols. L'application est développée en Django et utilise PostgreSQL comme base de données. Elle est hébergée sur la VM en Nginx et Gunicorn.

## Installation

### Méthode 1 : Développement Local

1. Clonez le dépôt

2. Activez un environnement virtuel :

    ```sh
    source env/bin/activate
    ```

   Sur Windows, utilisez :

    ```sh
    env\Scripts\activate
    ```

3. Installez les dépendances :

    ```sh
    cd src
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Lancez le serveur de développement :

    ```sh
    python manage.py runserver
    ```

6. Accédez à l'application à l'adresse suivante :

    ```
    http://127.0.0.1:8000
    ```

### Méthode 2 : Déploiement sur une VM

#### Étape 1: Configuration de la Base de Données PostgreSQL

1. **Installation de PostgreSQL** :

    ```sh
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```

2. **Création de la base de données et de l'utilisateur** :

    ```sh
    sudo -i -u postgres
    createuser --interactive
    createdb gestion_vol
    psql
    ALTER USER toto WITH PASSWORD 'toto';
    GRANT ALL PRIVILEGES ON DATABASE gestion_vol TO toto;
    \q
    exit
    ```

3. **Importer la base de données existante** :

    ```sh
    sudo -i -u postgres
    psql gestion_vol < /chemin/vers/gestion_aerien.sql
    exit
    ```

#### Étape 2: Clonage du Dépôt et Configuration de l'Environnement Virtuel

1. **Clonez le dépôt** :

2. **Créer et activer un environnement virtuel** :

    ```sh
    cd SAE-203
    virtualenv env
    source env/bin/activate
    ```

3. **Installer les dépendances** :

    ```sh
    cd src
    pip install -r requirements.txt
    ```

4. **Configurer la base de données PostgreSQL dans `settings.py`** :

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'gestion_vol',
            'USER': 'toto',
            'PASSWORD': 'toto',
            'HOST': 'ADRESSE_IP_DE_LA_VM',
            'PORT': '5432',
        }
    }

    ALLOWED_HOSTS = ['*']
    ```

5. **Appliquez les migrations de la base de données et collectez les fichiers statiques** :

    ```sh
    python manage.py migrate
    python manage.py collectstatic
    ```

#### Étape 3: Configuration de Gunicorn

1. **Créez un fichier de service systemd pour Gunicorn** (`/etc/systemd/system/gunicorn.service`) :

    Fichier contenue sur le github

2. **Démarrez et activez Gunicorn** :

    ```sh
    sudo systemctl start gunicorn
    sudo systemctl enable gunicorn
    ```

#### Étape 4: Configuration de Nginx

1. **Créez un fichier de configuration pour Nginx** (`/etc/nginx/sites-available/gestion_aerien`) :

   Fichier contenue sur le github

2. **Activez la configuration du site et redémarrez Nginx** :

    ```sh
    sudo ln -s /etc/nginx/sites-available/gestion_aerien /etc/nginx/sites-enabled
    sudo systemctl restart nginx
    ```

### 8. Pour accéder au site hébergé sur le serveur web

Pour acceder au site hébergé sur le serveur web, entrez http://ADRESSE_IP_DE_LA_VM
