# love_site

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.1+-red.svg)](https://flask.palletsprojects.com/)
[![uv](https://img.shields.io/badge/dependency--manager-uv-green.svg)](https://github.com/astral-sh/uv)

Une application web élégante développée en Python/Flask pour créer des cadeaux romantiques personnalisés. L'application offre une expérience émotionnelle immersive avec des animations fluides et un design responsive professionnel.

## 🚀 Installation et lancement

### Prérequis
- Python 3.8+
- uv (gestionnaire de dépendances)

### Installation
```bash
# Cloner le dépôt
git clone <repository-url>
cd love_site

# Installer les dépendances avec uv
uv sync
```

### Lancement
```bash
# Démarrer le serveur
uv run python app/main.py

# Ou si nécessaire avec PYTHONPATH explicite
PYTHONPATH=. uv run python app/main.py

# Alternative avec Flask CLI
uv run flask run
```

Ouvrir `http://localhost:5000` dans votre navigateur.

## 🎁 Utilisation

1. **Page d'accueil** : Remplissez le formulaire avec :
   - Prénom de la personne aimée (optionnel)
   - Prénom de l'expéditeur (défaut : Djochrist)

2. **Créer le cadeau** : Cliquez sur "Créer le cadeau ❤️"

3. **Profitez** : Laissez-vous emporter par les messages d'amour animés

4. **Navigation** : Utilisez les boutons Précédent/Suivant ou les flèches du clavier

## 🛠️ Personnalisation

### Messages d'amour
Modifiez `app/data/messages.json` pour changer les messages :
```json
{
  "messages": [
    { "id": 1, "text": "Mon message personnalisé avec {lover} et {sender}" }
  ]
}
```

### Styles et couleurs
Éditez `app/static/css/style.css` pour personnaliser l'apparence.

### Animations
Ajustez les paramètres dans `app/static/js/hearts.js` et `app/static/js/animation.js`.

## 🧪 Tests

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

# Tests applicatifs
uv run pytest tests/application/

# Avec couverture
uv run pytest --cov=app --cov-report=html
```

## 📁 Structure du projet

```
love_site/
├── app/
│   ├── __init__.py          # Factory Flask
│   ├── main.py              # Point d'entrée
│   ├── config.py            # Configuration
│   ├── routes/home.py       # Route principale
│   ├── services/messages.py # Logique des messages
│   ├── data/messages.json   # Messages d'amour
│   ├── templates/           # HTML Jinja2
│   └── static/              # CSS, JS, assets
├── tests/                   # Tests automatisés
│   ├── unit/                # Tests unitaires
│   ├── integration/         # Tests d'intégration
│   └── application/         # Tests applicatifs
├── docs/                    # Documentation
│   ├── architecture.md      # Architecture technique
│   ├── workflow.md          # Workflow dev
│   └── testing_strategy.md  # Stratégie de tests
├── pyproject.toml           # Dépendances uv
└── README.md
```

## 📚 Documentation

Consultez `docs/` pour :
- [Architecture technique](docs/architecture.md)
- [Workflow de développement](docs/workflow.md)
- [Stratégie de tests](docs/testing_strategy.md)

## 🎨 Technologies

- **Backend** : Python 3.8+, Flask 3.0+
- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Tests** : pytest
- **Gestion deps** : uv
- **Templates** : Jinja2

## 🤝 Contribution

1. Fork le projet
2. Créez une branche `feature/ma-fonctionnalite`
3. Commitez vos changements
4. Poussez et créez une Pull Request
5. Tests passent ? ✅ Merge !

## 📄 Licence

Ce projet est un cadeau d'amour — partagez-le librement avec les personnes que vous aimez.

## 💡 Idées d'amélioration

- Ajout de photos personnalisées
- Sons romantiques (optionnel)
- Thèmes différents (Noël, anniversaire...)
- Export PDF du cadeau
- Partage sur réseaux sociaux

---

**Fait avec ❤️ pour les moments romantiques**
