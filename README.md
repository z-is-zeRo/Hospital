# Hospital

# PRESENTATION

dans le cadre d'un projet scolaire, nous avons dévellopé une application web  pour la gestion d'un hopital.

# TECHNOLOGIE

pour le developpement nous avons utilisé python/Django.
il s'agit donc ici d'un projet Django.

# CREATION DE L'ENVIRONNELENT DE DEPLOIEMENT 

il faut dans un premier temps créer un environnement virtuel pour le developpement de ce travail

## Mettre en place un environnement de développement Django

comment mettre en place et tester un environnement de développement Django sous Windows, Linux (Ubuntu) et macOS — Peu importe votre système d'exploitation, cet article devrait vous fournir de quoi commencer à développer des applications Django.

-Prérequis : Connaissances de base sur l'utilisation d'un terminal/invite de commande et comment installer des packages sur l'OS de l'ordinateur que vous utiliserez pour développer.
-Objectif : Avoir un environnement de développement pour Django (2.0) fonctionnel sur votre ordinateur.
Aperçu de l'environnement de développement Django

Django simplifie le processus de configuration de votre ordinateur pour que vous puissiez rapidement commencer à développer des applications web. Cette section explique ce que vous aurez dans l'environnement de développement, et vous fournit un aperçu de certaines options de configuration et d'installation. Le reste de l'article explique la méthode recommandée pour installer l'environnement de développement Django sur Ubuntu, macOS et Windows, et comment le tester.

# Qu'est-ce que l'environnement de développement Django ?

L'environnement de développement correspond à une installation de Django sur votre ordinateur local que vous pouvez utiliser pour développer et tester des applications Django avant de les déployer sur un environnement de production.

Le principal outil que fournit Django est un ensemble de scripts Python utilisés pour créer et travailler avec des projets Django, ainsi qu'un simple serveur web de développement que vous pouvez utiliser pour tester en local (i.e. sur votre propre ordinateur, pas sur un serveur web externe) des applications web Django dans votre navigateur web.

## Quelles sont les options d'installation de Django ?

Django est extrêmement flexible sur sa manière d'être installé et configuré. Django peut-être :

    -Installé sur divers systèmes d'exploitation.
    -Installé depuis la source, avec l'Index des Packages Python (PyPI) et bien souvent depuis l'application de gestion de packages de l'ordinateur hôte.
    -Configuré pour communiquer avec diverses bases de données, qui peuvent aussi avoir besoin d'être configurées et installées séparément.
    -Lancé depuis l'environnement principal de Python ou depuis des environnements virtuels Python séparés.

Chacune de ces options requiert une configuration et une installation légèrement différente. Les sous-sections ci-dessous vous expliquent différents choix. Dans le reste de l'article, nous vous montrerons comment installer Django sur un nombre restreint de systèmes d'exploitation, et nous supposerons que cette installation aura été suivie pour tout le reste du module.

## Où peut-on télécharger Django ?

Il y a trois façons de télécharger Django :

    -Le Repository de Packages Python (PyPI), en utilisant l'outil pip. C'est la meilleure façon d'obtenir la dernière version stable de Django.
    -En utilisant la version du gestionnaire de packages de votre ordinateur. Les distributions de Django empaquetées avec les systèmes d'exploitation offrent un mécanisme d'installation plus familier. Veuillez toutefois noter que la version du package peut être datée, et ne pourra alors être installée que dans l'environnement système de Python (ce que vous pourriez ne pas souhaiter).
    -Installation depuis la source : Vous pouvez télécharger et installer la toute dernière version de Django depuis la source. Ce n'est pas recommandé pour les débutants, mais c'est une étape nécessaire si vous souhaitez contribuer à Django lui-même.


Pour utiliser Django, vous devrez installer Python sur votre système d'exploitation. Si vous utilisez Python 3, vous aurez alors aussi besoin de l'outil Python Package Index — pip3 — qui est utilisé pour gérer (installer, mettre à jour, supprimer) les packages/librairies Python qui seront utilisés par Django et vos autres applications Python.

## Ubuntu 18.04

Ubuntu Linux 18.04 LTS inclut par défaut Python 3.6.6. Vous pouvez vous en assurer en exécutant les commandes suivantes depuis le terminal bash :
    -python3 -V
    -Python 3.6.6

Toutefois, l'outil d'Index des Packages Python dont vous aurez besoin pour installer des packages avec Python 3 (y compris Django) n'est pas disponible par défaut. Vous pouvez installer pip3 avec le terminal bash avec :

    sudo apt install python3-pip

## macOS

macOS "El Capitan"et les versions plus récentes n'incluent pas Python 3. Vous pouvez vous en assurer en exécutant les commandes suivantes dans votre terminal bash :

    python3 -V
    bash: python3ommand not found

Vous pouvez facilement installer Python 3 (ainsi que l'outil pip3) sur python.org:

    Téléchargez l'installeur requis :
        Allez sur https://www.python.org/downloads/
        Sélectionnez le bouton Download Python 3.7.2 (le numéro de version mineure peut varier).
    Localisez le fichier en utilisant le Finder, puis double-cliquez le fichier package. Suivez les consignes d'installation.

Vous pouvez désormais confirmer la bonne installation en vérifiant votre version de Python 3 comme indiqué ci-dessous :

    python3 -V
    Python 3.7.2

Vous pouvez aussi vérifier que pip3 est correctement installé en listant les packages disponibles :

    pip3 list

## Windows 10

Windows n'inclut pas Python par défaut, mais vous pouvez facilement l'installer (ainsi que l'outil pip3) sur python.org:

    Téléchargez l'installeur requis :
        Allez sur https://www.python.org/downloads/
        Sélectionnez le bouton Download Python 3.7.2 (le numéro de version mineure peut varier).
    Installez Python en double-cliquant sur le fichier télécharger puis en suivant les consignes d'installation
    Assurez-vous d'avoir coché la case intitulée "Ajouter Python au PATH".

Vous pouvez ensuite vérifier que Python s'est correctement installé en tapant le texte suivant dans votre invite de commande :

    py -3 -V
    Python 3.7.2


L'installeur Windows inclut pip3 (le gestionnaire de packages Python) par défaut. Vous pouvez lister les packages installés de la manière suivante :

    pip3 list


## Utiliser Django dans un environnement virtuel Python

Les librairies que nous utiliserons pour créer nos environnements virtuels seront virtualenvwrapper (Linux et macOS) et virtualenvwrapper-win (Windows), , qui à leur tour utilisent l'outil virtualenv (en-US). Les outils d'habillage permettent de créer une interface consistante pour gérer les interfaces sur toutes les plateformes.
Installer l'utilitaire d'environnement virtuel
Mise en place de l'environnement virtuel sur Ubuntu

Après avoir installé Python et pip vous pouvez installer virtualenvwrapper (qui inclut virtualenv). Le guide d'installation officiel peut être trouvé ici, ou bien vous pouvez suivre les instructions ci-dessous.

## Installer l'outil en utilisant pip3:

    sudo pip3 install virtualenvwrapper

Ajoutez ensuite les lignes suivantes à la fin de votre fichier de configuration shell (le fichier caché .bashrc dans votre répertoire home). Elles indiquent les endroits où vos environnements virtuels seront installés, l'emplacement de vos projets de développement, et l'emplacement du script installé avec ce package :

    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh



### Note : Les variables VIRTUALENVWRAPPER_PYTHON et VIRTUALENVWRAPPER_VIRTUALENV_ARGS pointent vers l'emplacement d'installation par défaut de Python3, et source /usr/local/bin/virtualenvwrapper.sh pointe vers l'emplacement par défaut du script virtualenvwrapper.sh. Si le virtualenv ne fonctionne pas quand vous le testez, vérifiez que Python et le script sont bien aux emplacements attendus (puis modifiez le fichier de configuration en conséquence).

Vous pourrez trouver les bons emplacements de votre système en utilisant les commandes which virtualenvwrapper.sh et which python3.

Puis relancez le fichier de configuration en exécutant la commande suivante dans votre terminal :

    source ~/.bashrc

Vous pouvez maintenant créer un nouvel environnement virtuel avec la commande mkvirtualenv.
Mise en place de l'environnement virtuel sur macOS

L'installation de virtualenvwrapper on sur macOS est quasiment identique à celle sur Ubuntu (une fois de plus, vous pouvez suivre les instructions du guide officiel d'installation ou suivre les indications ci-dessous).

## Installez virtualenvwrapper (ainsi que virtualenv) en utilisant pip comme indiqué ci-dessous.

    sudo pip3 install virtualenvwrapper

Puis ajoutez les lignes suivantes à la fin de votre fichier de configuration shell.

    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh
    
### Note : La variable VIRTUALENVWRAPPER_PYTHON pointe vers l'emplacement d'installation par défaut de Python3, et source /usr/local/bin/virtualenvwrapper.sh pointe vers l'emplacement par défaut du script virtualenvwrapper.sh. Si le virtualenv ne fonctionne pas quand vous le testez, vérifiez que Python et le script sont bien aux emplacements attendus (puis modifiez le fichier de configuration en conséquence).

Par exemple, une installation test sur macOS a résulté en l'ajout des lignes suivantes dans le fichier startup :

    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
    export PROJECT_HOME=$HOME/Devel
    source /Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh

Vous pourrez trouver les bons emplacements de votre système en utilisant les commandes which virtualenvwrapper.sh et which python3.Puis relancez le fichier de configuration en appelant la ligne suivante depuis le terminal :

    source ~/.bash_profile

Vous devriez alors voir apparaître plusieurs lignes de script (les mêmes scripts que ceux présents dans l'installation Ubuntu). Vous devriez maintenant pouvoir créer un nouvel environnement virtuel avec la commande mkvirtualenv.
Mise en place de l'environnement virtuel sur Windows 10

Installer virtualenvwrapper-win est encore plus simple qu'installer virtualenvwrapper , parce que vous n'avez pas besoin de configurer là où l'outil enregistre les informations de l'environnement virtuel (il y a des valeurs par défaut). Tout ce que vous avez besoin de faire est de lancer la commande suivante depuis l'invite de commande :

    pip3 install virtualenvwrapper-win

Vous pouvez désormais créer un nouvel environnement virtuel avec la commande mkvirtualenv

## Créer un environnement virtuel

Maintenant que vous avez installé virtualenvwrapper ou virtualenvwrapper-win , travailler avec des environnements virtuels sera une tâche très similaire entre chaque plateforme.

Vous pouvez désormais créer un nouvel environnement virtuel avec la commande mkvirtualenv. Lors de son exécution, vous pourrez voir l'environnement être configuré (ce que vous verrez changera légèrement en fonction de votre plateforme). Lorsque l'exécution de la commande sera terminée, votre environnement virtuel sera actif — vous pouvez voir au début de la ligne de commande le nom de votre environnement entre parenthèses (nous vous montrons le résultat pour Ubuntu ci-dessous, mais la dernière ligne est similaire su

    $ mkvirtualenv my_django_environment

    Running virtualenv with interpreter /usr/bin/python3
    ...
    virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/t_env7/bin/get_env_details
    (my_django_environment) ubuntu@ubuntu:~$

Maintenant que vous êtes dans votre environnement virtuel vous pouvez installer Django et commencer à développer.
Utiliser un environnement virtuel

Il y a quelques commandes que vous devriez connaître (il y en a davantage dans la documentation de l'outil, mais celles-ci sont celles que vous utiliserez le plus souvent) :

    deactivate — Permet de sortir de l'environnement virtuel Python actuel
    workon — Lister tous les environnements virtuels disponibles
    workon name_of_environment — Activer l'environnement virtuel spécifié
    rmvirtualenv name_of_environment — Supprimer l'environnement virtuel spécifié

## Installer Django

Une fois que vous avez créé votre environnement virtuel, et que vous avez utilisé workon pour y entrer, vous pouvez utiliser pip3 pour installer Django.

    pip3 install django

Vous pouvez tester l'installation de Django en exécutant la commande suivante (celle-ci ne fait que tester le fait que Python puisse trouver le module Django) :

## Linux/macOS
    python3 -m django --version
    2.1.5

## Windows
    py -3 -m django --version
    2.1.5

   note : Si la commande Windows ci-dessus n'indique aucun module Django présent, essayez :

    py -m django --version

Dans Windows, les scripts Python 3 sont exécutés en préfixant la commande avec py -3, bien que ceci puisse varier suivant votre installation. Essayer en enlevant le modificateur -3 si vous rencontrez un problème avec la commande. Dans Linux/macOS, la commande est python3.

Attention : Le reste de ce module utilise les commandes Linux pour invoquer Python 3 (python3) . . Si vous travaillez sous Windows , remplacez simplement ce préfixe avec :
        py -3

## Tester votre installation

Les tests ci-dessus fonctionnent, mais ne font rien de très divertissant. Un test plus intéressant consiste à créer un projet squelette et de voir si il fonctionne. Pour ce faire, naviguez tout d'abord dans votre invite/terminal de commande à l'endroit où vous désirez stocker vos applications Django. Créez un dossier pour votre site test et placez-vous dedans.

    mkdir django_test
    cd django_test

Vous pouvez ensuite créer un nouveau site squelette intitulé "mytestsite" utilisant l'outil django-admin omme montré. Après avoir créé le site, vous pouvez naviguer dans le dossier où vous trouverez le script principal pour gérer vos projets, intitulé manage.py.

    django-admin startproject mytestsite

    cd mytestsite

Nous pouvons lancer le serveur web de développement depuis ce dossier en utilisant manage.py et la commande runserver command, comme indiqué ci-dessous.

    $ python3 manage.py runserver
Performing system checks...

# DEPLOIEMENT

une fois fois l'environnement virtuel crée, il faudra placer le projet dans le dossier hebergeant l'environnement crée, à partir de ce dossier ouvrir l'invite de commande.
cela étant fait, entrer dans le dossier Hopital en invite de commande, ceci par la commande : 
     cd hopital
 il ne reste plus qu'à installer quelques dépendances et à lancer le serveur:
 
    python manage.py makemigratiions
    pip install django-crispy-forms
    pip install django-allauth
    pip install pillow
    py manage.py runserver



