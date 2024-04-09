# Script chercheur d'archives d'une playlist

Ce script recense l'existence d'archive de vidéos Youtube dans une playlist grâce à la Wayback Machine. Le but de ce script est de pouvoir retrouver des vidéos qui sont privées/ supprimées en les cherchant dans les recommandations de vidéos similaires.

## Utilisation

```
usage: python main.py [-h] [-a AFTER] [-b BEFORE] [-w WRITE] URL
```
Tapez 
```python main.py -h```
pour plus d'informations.

## A faire

Ajouter un mode "recherche" : Cherche l'existence d'une chaîne de caractères (en l'occurence le titre d'une vidéo par exemple) 
parmi les archives
