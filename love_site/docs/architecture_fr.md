# Architecture technique - love_site

## Vue d'ensemble

`love_site` est une application web spécialisée dans la création de vidéos romantiques personnalisées. Développée avec Flask, elle intègre une architecture modulaire et maintenable, respectant les principes SOLID et les meilleures pratiques de développement Python. L'application génère de belles vidéos animées avec des messages personnalisés, des cœurs flottants, et un support audio optionnel pour créer des cadeaux romantiques uniques.

## Structure du projet

```
love_site/
├── app/                    # Code d'application principal
│   ├── __init__.py         # Fabrique d'application Flask
│   ├── main.py             # Point d'entrée
│   ├── config.py           # Configuration de base
│   ├── routes/             # Définition des routes
│   │   └── home.py         # Blueprint pour la page d'accueil
│   ├── services/           # Logique métier
│   │   └── messages.py     # Service de gestion des messages
│   ├── data/               # Données statiques
│   │   └── messages.json   # Messages romantiques avec templates
│   ├── templates/          # Templates Jinja2
│   │   ├── base.html       # Template de base
│   │   └── index.html      # Page principale
│   └── static/             # Assets statiques
│       ├── css/
│       │   └── style.css   # Styles romantiques et responsives
│       └── js/
│           ├── hearts.js   # Animation des cœurs flottants
│           └── animation.js # Animation de texte et carousel
├── tests/                  # Tests automatisés
│   ├── unit/               # Tests unitaires
│   ├── integration/        # Tests d'intégration
│   └── application/        # Tests d'application
├── docs/                   # Documentation
└── pyproject.toml          # Configuration des dépendances
```

## Principes architecturaux

### Séparation des responsabilités
- **Routes** : Gestion des requêtes HTTP et rendu des templates
- **Services** : Logique métier (chargement et personnalisation des messages)
- **Templates** : Présentation HTML
- **Static** : Assets (CSS, JS) pour l'interactivité et le style
- **Data** : Données statiques (JSON des messages)

### Personnalisation
- Les messages utilisent des espaces réservés (`{lover}`, `{sender}`) remplacés dynamiquement
- Valeurs par défaut élégantes pour une expérience fluide
- Interface utilisateur simple et intuitive

### Animations
- **Cœurs flottants** : Générés aléatoirement avec des couleurs romantiques
- **Texte progressif** : Animation lettre par lettre avec navigation carousel
- **Transitions fluides** : CSS moderne pour les interactions
- **Transmission de données** : Injection directe en JavaScript via des balises `<script>` pour éviter les conflits d'échappement avec les caractères spéciaux (apostrophes, guillemets)

### Design responsive
- Adaptation mobile/desktop
- Palette de couleurs romantiques cohérente
- Accessibilité et performance

## Technologies

- **Backend** : Python 3.8+, Flask
- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Tests** : pytest
- **Gestion des dépendances** : uv
- **Templates** : Jinja2

## Sécurité et meilleures pratiques

- Validation des entrées utilisateur
- Gestion d'erreur robuste
- Code modulaire et testable
- Commentaires et documentation
- Conformité aux standards PEP 8

Cette architecture permet une évolution facile : ajout de nouvelles routes, personnalisations, ou intégration d'autres fonctionnalités romantiques.
