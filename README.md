
## Project: Modélisation de la menace de déforestation en utilisant des données relatives au developpement de l'agriculture et de l'urbanisation 

### Installation

Ce projet nécessite le langage **Python** et les bibliothèques Python suivantes installées :

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

Il faut également avoir installé un logiciel permettant de faire fonctionner et d'exécuter un [Jupyter Notebook](http://jupyter.org/install.html).

Si n'est pas installé Python, il est fortement recommandé d'installer la distribution [Anaconda](https://www.anaconda.com/download/) de Python, qui contient déjà les paquets ci-dessus et d'autres encore. 


### Code

Il y'a trois fichiers code, un premier ficher nommé `Exploitation_données_Agriculture_Urbanisation.ipynb` sur lequel on fait une exploitation des données sur l'agriculture et l'urbanisation, un deuxième fichier nommé `Exploitation_des_données_Forestières.ipynb` sur lequel on a realisé une exploitation des données forestières et enfin un troisième fichier `Prédire_Menace_Déforestation.ipynb` sur lequel on a utilisé le jeu de données `Data.csv` pour mettre en place le modèle permettant de prédiré la menace de la déforestation.


### Exécution

Pour ouvrir le fichier contenant le modèle, il suffit d'utiliser un terminal ou une fenêtre de commande et puis naviguez vers le répertoire de projet `Modélisation_Déforestation/` (qui contient ce README) et exécutez une des commandes suivantes :

```bash
ipython notebook Prédire_Menace_Déforestation.ipynb
```  
ou
```bash
jupyter notebook Prédire_Menace_Déforestation.ipynb
```
ou ouvrir avec Jupyter Lab
```bash
jupyter lab
```

Cela ouvrira le logiciel Jupyter Notebook et le fichier du projet dans le navigateur.

### Données 

Sur ce projet on a utilisé deux trois jeu de données `agriculture_data.csv`, `Urbanization_Data.csv` et `Forest_Data.csv`. Les deux derniers sont tirés respectivement des sites [senegal open data for africa](https://senegal.opendataforafrica.org/) et [EARTH MAP](https://earthmap.org/). Le jeu de données qui a servi à mettre en place le modèle est issu des jeux de données cités ci-avant. Il est composé de 279 observations caractérisées par 6 variables. 

**Variables**
1.  region
2.  Date
3.  Taux d'urbanisation
4.  Superficie agricole
5.  Superficie Perdue 

**Variable Cible**

6. Risque déforestation

Pour la modélisation, seules les variables continues ont été utilisées que sont :
1. Taux d'urbanisation 
2. Superficie agricole
3. Superficie Perdue

