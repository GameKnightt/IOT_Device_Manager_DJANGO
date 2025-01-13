# IoT Device Manager

Ce projet Django a pour but de gérer des capteurs (sensors), leurs unités de mesure et leurs données de mesure au sein d'une plateforme IoT :

## Objectifs

- Centraliser et administrer les capteurs depuis une interface conviviale.
- Visualiser facilement l’emplacement géographique et l’historique des mesures.

## Fonctionnement

- Chaque capteur est associé à une unité de mesure et peut enregistrer plusieurs mesures.
- Une interface web affiche une carte avec la position des capteurs et un graphique en temps réel de leurs mesures.

## Installation

1. Cloner ce dépôt.
2. Créer puis activer un environnement virtuel :
    ```bash
    python -m venv venv
    source robot_venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```
    Installer les packages nécessaires (Django, etc.).
3. Lancer les migrations et démarrer le serveur local :
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
4. Accéder à l’interface via http://127.0.0.1:8000.

## Utilisation

Navigation fluide et intuitive à travers les différentes pages du site.

## Technologies

- Librairies JavaScript : Leaflet pour la carte et Chart.js pour les graphiques.
- Design : Bootstrap pour la mise en page et le style.

## Contribution

Faire un fork du projet et proposer des pull requests pour les nouvelles fonctionnalités ou correctifs.

## Licence MIT

Ce projet est fourni à titre d’exemple et peut être adapté librement en fonction de vos besoins.