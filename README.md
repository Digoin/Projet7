# Projet7

Ce code a pour but de mettre en ligne sur le site Heroku une application de recherche de lieu.

Ce code est demandé pour le projet "Créez GrandPy Bot, le papy-robot" du parcours « Développeur d’application – Python » proposé par l’école Open Classrooms.

Pour ouvir l'application localement il vous faudra déclarer la variable d'environnement "GOOGLE_API_KEY" correspondant à la clé d'API fournit lors de la création d'un compte Maps Platform.
Ceci fait, télécharger les dépendances grâce à pipenv install et  exéctuter la commande "flask run -h localhost -p 8003" à la racine du projet.

Pour mettre l'application en ligne sur Heroku il vous faudra initier un repository git à l'aide de la commande "git init", puis ajouter les fichiers en exécutant "git add ." suivi de "git commit -m "first commit". Connectez à Heroku avec "heroku login", ensuite créer l'application en rentrant "heroku create" et enfin il vous faudra push votre projet : "git push heroku master".
