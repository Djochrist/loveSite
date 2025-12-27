# love_site

[![CI](https://github.com/Djochrist/loveSite/actions/workflows/ci.yml/badge.svg)](https://github.com/Djochrist/loveSite/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.1+-red.svg)](https://flask.palletsprojects.com/)
[![uv](https://img.shields.io/badge/dependency--manager-uv-green.svg)](https://github.com/astral-sh/uv)
[![GitHub](https://img.shields.io/badge/GitHub-Djochrist/loveSite-blue?logo=github)](https://github.com/Djochrist/loveSite)

Une élégante application web développée en Python/Flask pour créer des vidéos romantiques avec messages personnalisés. L'application offre une expérience émotionnelle immersive avec des animations fluides et un design responsive professionnel.

## Installation et Lancement

### Prérequis
- Python 3.8+
- uv (gestionnaire de dépendances)

### Installation
```bash
# Cloner le repository
git clone https://github.com/Djochrist/loveSite.git
cd love_site

# Installer les dépendances avec uv
uv sync
```

### Lancement
```bash
# Depuis le répertoire racine (recommandé)
uv run flask --app love_site.app:create_app() run

# Alternative avec variable d'environnement
FLASK_APP=love_site.app uv run flask run

# Depuis le répertoire love_site
uv run python app/main.py
```

Ouvrez `http://localhost:5000` dans votre navigateur.

## Utilisation

L'application affiche des messages d'amour personnalisés directement sur la page d'accueil.

- **Messages** : Messages d'amour pour "bae" de "Djochrist"
- **Navigation** : Utilisez les boutons Précédent/Suivant ou les flèches du clavier pour naviguer entre les messages
- **Animation** : Profitez de l'effet d'animation de frappe au fur et à mesure que les messages apparaissent

## Personnalisation

### Messages d'Amour
Modifiez `app/data/messages.json` pour changer les messages :
```json
{
  "messages": [
    { "id": 1, "text": "Mon message personnalisé avec {lover} et {sender}" }
  ]
}
```

### Styles et Couleurs
Éditez `app/static/css/style.css` pour personnaliser l'apparence.

### Animations
Ajustez les paramètres dans `app/static/js/hearts.js` et `app/static/js/animation.js`.

## Tests

### Lancer tous les tests
```bash
uv run pytest
```

### Tests spécifiques
```bash
# Tests unitaires
uv run pytest tests/unit/

# Tests d'intégration
uv run pytest tests/integration/

# Tests d'application
uv run pytest tests/application/

# Avec couverture
uv run pytest --cov=app --cov-report=html
```

## Structure du Projet

```
love_site/
├── app/
│   ├── __init__.py          # Fabrique Flask
│   ├── main.py              # Point d'entrée
│   ├── config.py            # Configuration
│   ├── routes/home.py       # Route principale
│   ├── services/messages.py # Logique des messages
│   ├── data/messages.json   # Messages d'amour
│   ├── templates/           # Templates Jinja2
│   └── static/              # CSS, JS, assets
├── tests/                   # Tests automatisés
│   ├── unit/                # Tests unitaires
│   ├── integration/         # Tests d'intégration
│   └── application/         # Tests d'application
├── docs/                    # Documentation
│   ├── architecture_fr.md   # Architecture technique
│   ├── workflow_fr.md       # Workflow développement
│   └── testing_strategy_fr.md # Stratégie de tests
├── pyproject.toml           # Dépendances uv
└── README.md
```

## Documentation

Consultez `docs/` pour :
- [Architecture Technique](docs/architecture_fr.md)
- [Workflow de Développement](docs/workflow_fr.md)
- [Stratégie de Tests](docs/testing_strategy_fr.md)

## Technologies

- **Backend** : Python 3.8+, Flask 3.0+
- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Tests** : pytest
- **Gestionnaire de dépendances** : uv
- **Templates** : Jinja2

## Contribution

1. Forkez le projet
2. Créez une branche `feature/ma-fonctionnalite`
3. Commitez vos changements
4. Pushez et créez une Pull Request
5. Les tests passent ? Fusion !

## Licence

MIT

## Idées d'Amélioration

- Ajouter des photos personnalisées
- Sons romantiques (optionnel)
- Différents thèmes (Noël, anniversaire...)
- Export PDF du cadeau
- Partage sur les réseaux sociaux

---

**Made with love for romantic moments**
