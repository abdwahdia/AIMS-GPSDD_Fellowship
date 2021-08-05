## Project: Modélisation de la menace de déforestation en utilisant des données relatives à l'urbanisation, l'agriculture et la foresterie. 

### Installation

Ce projet nécessite le langage **Python** et les bibliothèques Python suivantes installées :

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

Il faut également avoir installé un logiciel permettant de faire fonctionner et d'exécuter un [Jupyter Notebook](http://jupyter.org/install.html).

Si n'est pas installé Python, il est fortement recommandé d'installer la distribution [Anaconda](https://www.anaconda.com/download/) de Python, qui contient déjà les paquets ci-dessus et d'autres encore. 


### Code

Il y'a trois principaux fichiers code, un premier ficher nommé `Exploitation_données_Agriculture_Urbanisation.ipynb` sur lequel une exploitation des jeux de données contenus dans les fichiers `Agriculture_Data.csv` et `Urbanization_Data.csv` a été faite, un deuxième fichier nommé `Exploitation_des_données_Forestières.ipynb` sur lequel on a realisé une exploitation des données forestières et enfin un troisième fichier `Prédire_menace_déforestation_avec_données_urbanisation_forestières.ipynb` sur lequel on a utilisé le jeu de données `Data_Urbanization_Forest.csv` pour mettre en place le modèle permettant de prédiré la menace de la déforestation.


### Exécution

Pour ouvrir le fichier contenant le modèle, il suffit d'utiliser un terminal ou une fenêtre de commande et puis naviguez vers le répertoire de projet `Modélisation_Déforestation/` (qui contient ce README) et exécutez une des commandes suivantes :

```bash
ipython notebook Prédire_menace_déforestation_avec_données_urbanisation_forestières.ipynb
```  
ou
```bash
jupyter notebook Prédire_menace_déforestation_avec_données_urbanisation_forestières.ipynb
```
ou ouvrir avec Jupyter Lab
```bash
jupyter lab
```

Cela ouvrira le logiciel Jupyter Notebook et le fichier du projet dans le navigateur.

### Données 

Sur ce projet on a principalement utilisé deux jeux de données `Urbanization_Data.csv` et `Forest_Data.csv` tirés respectivement des sites [senegal open data for africa](https://senegal.opendataforafrica.org/) et [EARTH MAP](https://earthmap.org/). Le jeu de données qui a servi à mettre en place le modèle est issu de la concaténation des deux jeux données cités ci-avant transformés. Le jeu de concaténé est composé de 512 observations caractérisées par 13 variables. 

**Variables**
1.  region
2.  Date
3.  Effectif de la population 
4.  Population rurale
5.  Population urbaine 
6.  Taux d'urbanisation 
7.  Nombre de ménages ruraux
8.  Nombre de ménages urbains 
9.  Taille moyenne des ménages 
10. Taille moyenne des ménages ruraux 
11. Taille moyenne des ménages urbains 
12. Superficie Perdue 

**Variable Cible**

13. risque déforestation

Pour la modélisation, seules les variables les plus correlées avec la variable ont été utilisées. Ces variables sont les suivantes :
1. Population urbaine
2. Taux d'urbanisation
3. Nombre de ménages urbains 
4. Superficie Perdue
