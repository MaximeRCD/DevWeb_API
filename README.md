# Api Garbage Collector Project

## 0 . Objectif du projet
L'objectif de ce projet est de construire une API autonome qui permet de :

- Servir les données d'intérêts au FrontEnd.
- Enregistrer les données d'intérêts du FrontEnd vers la DataBase.

## 1 . Installation du projet (dev)

- Cloner le projet en local
    ```
    git clone https://github.com/MaximeRCD/DevWeb_API.git
    ```

- Ajouter un fichier .env à la base du projet
- Copier / Coller ce contenu
  ```
  DB_USER=root
  DB_PASSWORD=root
  DB_NAME=garbage_app_db
  MODEL_PATH=./img/model_5class_resnet_87%.h5
  LOCAL_API_IP=localhost
  PROD_API_IP=db
  ```
  
- Récupérer le fichier contenant le model pré-entrainé [model_file](https://drive.google.com/file/d/1wamwLZsclQYYsx5dLThTqZG5sJSLR7oS/view?usp=sharing)
- Créer un dossier ./img à la base du projet
- Dézippé et insérer le fichier model dans le dossier ./img
- Vérifier :

    - Le chemin relatif du modèle correspond à la variable MODEL_PATH
    - Aucun service n'utilise le port 3306 car le conteneur mysql y est mappé

## 2 . Utilisation (dev)

- Build l'image Docker à partir du fichier Dockerfile
```
docker build -t api .
```

- Démarrer le Docker Compose fourni

```
docker-compose up --build
```