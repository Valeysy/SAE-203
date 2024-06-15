# Gestion du Trafic Aérien

Cette SAE 2.03 est une application web de gestion du trafic aérien entre différents aéroports. Il permet de gérer les aéroports, les pistes, les compagnies aériennes, les types d'avions, les avions et les vols. L'application est développée en Django et utilise PostgreSQL comme base de données. Il est hébergé sur la VM en Nginx et Gunicorn.

## Installation

1. Clonez le dépôt :

    ```sh
    git clone https://github.com/votre-utilisateur/gestion-trafic-aerien.git
    cd gestion-trafic-aerien
    ```

1. Activez un environnement virtuel :

    ```sh
    source env/bin/activate  #
    ```

   Sur Windows, utilisez

    ```sh
    env\Scripts\activate`  #
    ````
    

3. Installez les dépendances :

    ```sh
    cd src
    pip install -r requirements.txt
    ```

4. Configurez la base de données PostgreSQL dans `settings.py` :

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
    ```

5. Appliquez les migrations de la base de données :

    ```sh
    python manage.py migrate
    ```

6. Lancez le serveur de développement :

    ```sh
    python manage.py runserver
    ```

7. Accédez à l'application à l'adresse suivante :

    ```
    http://127.0.0.1:8000
    ```
8. Pour acceder au site hébergé sur le serveur web, entrez http://ADRESSE_IP_DE_LA_VM

