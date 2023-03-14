# OC_Projet_8 Pur_Beurre_App

Le programme est une application web où l'on peut rechercher un produit alimentaire et avoir des propositions de substitut ayant un nutriscore supèrieur à celui recherché. De plus, s'ils nous intéressent, nous pouvons les sauvegarder.  

## Tout d'abord 

Ces consignes vont vous permettre d'obtenir une copie de mon projet et de le tester avec la console de commande de votre machine.

### Pré-requis 

Le programme étant écrit en Python, il doit être installé sur votre ordinateur. Vous pouvez le télécharger à cette adresse : [Télecharger Python](https://www.python.org/downloads/)

### Installation

Tout d'abord, recupérez mon projet avec cette commande : 

```git clone https://github.com/R4mTex/P8_POUTOT_Simon-P8_01_site.git```

puis placez-vous dans ce dossier : 

```cd P8_POUTOT_Simon-P8_01_site/pur_beurre_app```

Pour ne pas interférer avec d'autres projets, il est conseillé d'exécuter celui-ci dans un environnement virtuel. 
Voici les principales commandes pour :

1. Créer un environnement virtuel 

windows/mac/linux : 

```python -m venv env```

2. Activer l'environnement virtuel

windows : 

```env\Scripts\activate.bat```

mac/linux : 

```source env/bin/activate```

Pour en apprendre plus sur les environnements virtuels, vous avez toute la documentation à cette adresse : [Documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html/)

Pour le bon fonctionnement du programme, il est indispensable d'installer les bibliothèques fournies.
Celles-ci sont listées dans le document ```requirements.txt```.

Une fois la console placée dans le dossier racine du programme, leurs installations se fait via la commande suivante :

```pip install -r requirements.txt --use-pep517```

### Initialisation

Exécutez ces commandes à la suite dans cet ordre :

1. ```python manage.py migrate```
2. ```python manage.py createsuperuser``` (suivre les intructions affichées dans la console de commande)
3. ```python manage.py populate_bdd 10 400``` (cette étape prendra quelques minutes)

Maintenant, si les quatres commandes énumérées précédemment sont bien effectives, vous pouvez exécuter la commande :

```python manage.py runserver```

Enfin une URL vous sera donnée : ```Starting development server at http://127.0.0.1:8000/``` suivez le lien et vous serez redirigé vers mon site.
Connectez-vous avec les identifiants de l'utilisateur créé juste avant.

Vous pouvez arrêter le serveur à tout moment en appuyant sur ```ctrl + c```.

Bon essai.

## Écrit avec

[VisualStudioCode](https://code.visualstudio.com/) - Editeur de texte

## Auteur

POUTOT Simon. 

### Remerciements

Merci à **GONNAGE Ranga** pour son soutien.
