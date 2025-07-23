# Videos Manim - Animations éducatives

Ce projet contient des animations vidéo créées avec [Manim](https://www.manim.community/) pour expliquer des concepts techniques de développement logiciel. Les animations sont conçues pour être utilisées dans un contexte éducatif.

## 📋 Description du projet

Le projet utilise la bibliothèque `cs-manim` (une extension de Manim) pour créer des animations explicatives sur divers sujets techniques :

- **SignalR** : Explication des concepts de communication Half-Duplex vs Full-Duplex, avec des démonstrations visuelles de l'architecture client-serveur

D'autres vidéos pourront être ajoutées au fur et à mesure pour couvrir différents concepts techniques.

## 🚀 Installation

### Prérequis

- Python 3.10+
- pip
- uv

### Installation standard

1. **Cloner le projet** :

   ```bash
   git clone <url-du-repo>
   cd Videos
   ```

2. **Créer un environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances** :
   ```bash
   uv pip install -e .
   ```

### Installation pour le développement avec cs-manim

Si vous développez également sur `cs-manim` en parallèle :

1. **Cloner cs-manim** dans le répertoire parent :

   ```bash
   cd ..
   git clone <url-cs-manim> cs-manim
   cd Videos
   ```

2. **Créer un environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Installer en mode développement** :

   ```bash
   uv pip install -e ".[dev]"
   ```

   Cette configuration utilise la version locale de `cs-manim` (via `file://${PROJECT_ROOT}/../cs-manim`) au lieu de la version PyPI, permettant de tester les modifications de `cs-manim` en temps réel. Il faut donc que cs-manim soit installé côte à côte avec ce projet.

## 🎬 Compilation des vidéos

### Méthode 1 : Via VS Code (recommandée)

Si vous utilisez VS Code, une tâche est préconfigurée :

1. Ouvrir le fichier `.py` d'une vidéo (ex: `video/signalr/signalr.py`)
2. Sélectionner la configuration d'exécution "Manim - Fichier actuel".
3. Exécuter

### Méthode 2 : Ligne de commande

```bash
# Depuis la racine du projet
manim -pql video/signalr/signalr.py SignalR
```

**Options Manim courantes :**

- `-pql` : Preview, Quality Low (480p15) - pour les tests rapides
- `-pqm` : Preview, Quality Medium (720p30)
- `-pqh` : Preview, Quality High (1080p60) - pour la production
- `-s` : Sauvegarder la dernière frame comme image
- `--dry_run` : Vérifier la syntaxe sans générer la vidéo

#### Exemple complet :

```bash
# Test rapide en basse qualité
manim -pql video/signalr/signalr.py SignalR

# Production en haute qualité
manim -pqh video/signalr/signalr.py SignalR

# Voir toutes les scènes disponibles dans un fichier
manim video/signalr/signalr.py --dry_run
```

### Méthode 3 : Extension Manim de vscode

1. Installer l'extension [Manim](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview)
2. Ouvrir le fichier `.py` d'une vidéo (ex: `video/signalr/signalr.py`)
3. Cliquer sur le nouveau bouton "Manim : Run as sideview" au haut à droite de l'éditeur
