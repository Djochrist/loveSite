# Architecture Technique - love_site

## Vue d'ensemble

`love_site` constitue une application web spécialisée dans la création de cadeaux romantiques personnalisés. Développée avec Flask, elle intègre une architecture modulaire et maintenable, respectant les principes SOLID et les bonnes pratiques de développement Python. L'application offre une expérience utilisateur émotionnelle immersive grâce à des animations JavaScript sophistiquées et un design responsive professionnel.

## Structure du projet

```
love_site/
├── app/                    # Code applicatif principal
│   ├── __init__.py         # Factory de l'application Flask
│   ├── main.py             # Point d'entrée
│   ├── config.py           # Configuration de base
│   ├── routes/             # Définition des routes
│   │   └── home.py         # Blueprint pour la page d'accueil
│   ├── services/           # Logique métier
│   │   └── messages.py     # Service de gestion des messages
│   ├── data/               # Données statiques
│   │   └── messages.json   # Messages d'amour avec templates
│   ├── templates/          # Templates Jinja2
│   │   ├── base.html       # Template de base
│   │   └── index.html      # Page principale
│   └── static/             # Assets statiques
│       ├── css/
│       │   └── style.css   # Styles romantiques et responsives
│       └── js/
│           ├── hearts.js   # Animation des cœurs flottants
│           └── animation.js # Animation de frappe et carousel
├── tests/                  # Tests automatisés
│   ├── unit/               # Tests unitaires
│   ├── integration/        # Tests d'intégration
│   └── application/        # Tests applicatifs
├── docs/                   # Documentation
└── pyproject.toml          # Configuration des dépendances
```

## Principes architecturaux

### Séparation des responsabilités
- **Routes** : Gestion des requêtes HTTP et rendu des templates
- **Services** : Logique métier (chargement et personnalisation des messages)
- **Templates** : Présentation HTML
- **Static** : Assets (CSS, JS) pour l'interactivité et le style
- **Data** : Données statiques (messages JSON)

### Personnalisation
- Les messages utilisent des placeholders (`{lover}`, `{sender}`) remplacés dynamiquement
- Valeurs par défaut élégantes pour une expérience fluide
- Interface utilisateur simple et intuitive

### Animations
- **Cœurs flottants** : Générés aléatoirement avec couleurs romantiques
- **Texte progressif** : Animation de frappe lettre par lettre avec carousel de navigation
- **Transitions fluides** : CSS moderne pour les interactions
- **Transmission des données** : Injection directe en JavaScript via balises `<script>` pour éviter les conflits d'échappement HTML

### Responsive design
- Adaptation mobile/desktop
- Palette romantique cohérente
- Accessibilité et performance

## Technologies

- **Backend** : Python 3.8+, Flask
- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Tests** : pytest
- **Gestion deps** : uv
- **Templates** : Jinja2

## Sécurité et bonnes pratiques

- Validation des entrées utilisateur
- Gestion d'erreurs robuste
- Code modulaire et testable
- Commentaires et documentation
- Respect des standards PEP 8

Cette architecture permet une évolution facile : ajout de nouvelles routes, personnalisations, ou intégration d'autres fonctionnalités romantiques.
