# Contribuer à love_site

Merci de votre intérêt pour contribuer à love_site ! Ce document fournit des directives et des informations pour les contributeurs.

## Code de conduite

Ce projet suit un code de conduite pour assurer un environnement accueillant pour tous les contributeurs. En participant, vous acceptez de :

- Être respectueux et inclusif
- Se concentrer sur les commentaires constructifs
- Accepter la responsabilité des erreurs
- Montrer de l'empathie envers les autres contributeurs
- Aider à créer une communauté positive

## Comment contribuer

### 1. Fork et clone
```bash
git clone https://github.com/Djochrist/loveSite.git
cd loveSite
```

### 2. Configuration de l'environnement de développement
```bash
uv sync
```

### 3. Créer une branche de fonctionnalité
```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
# ou
git checkout -b fix/mon-correctif-bug
```

### 4. Faire vos modifications
- Suivre le style de code existant
- Ajouter des tests pour les nouvelles fonctionnalités
- Mettre à jour la documentation si nécessaire
- S'assurer que tous les tests passent

### 5. Commiter vos modifications
```bash
git add .
git commit -m "feat: ajouter ma nouvelle fonctionnalité

- Ce qui a été changé
- Pourquoi cela a été changé
- Toute modification avec rupture"
```

Utiliser le format de commit conventionnel :
- `feat:` pour les nouvelles fonctionnalités
- `fix:` pour les corrections de bugs
- `docs:` pour la documentation
- `style:` pour le formatage
- `refactor:` pour la restructuration du code
- `test:` pour les tests
- `chore:` pour la maintenance

### 6. Pousser et créer une pull request
```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

Créer une pull request avec :
- Titre et description clairs
- Référence aux issues liées
- Captures d'écran pour les changements UI
- Résultats des tests

## Directives de développement

### Style de code
- Suivre PEP 8
- Utiliser des indications de type si possible
- Écrire des noms de variables et fonctions descriptifs
- Garder les fonctions petites et ciblées
- Ajouter des docstrings à toutes les fonctions publiques

### Tests
- Écrire des tests unitaires pour les nouvelles fonctionnalités
- Maintenir >80% de couverture de code
- Tester les cas limites et les conditions d'erreur
- Lancer les tests avant de soumettre une PR

### Documentation
- Mettre à jour le README pour les nouvelles fonctionnalités
- Ajouter des docstrings aux nouvelles fonctions
- Mettre à jour la documentation existante
- Tester la construction de la documentation

## Structure du projet

```
love_site/
├── app/                    # Code d'application principal
│   ├── __init__.py         # Fabrique d'application Flask
│   ├── main.py            # Point d'entrée
│   ├── config.py          # Configuration
│   ├── routes/            # Définition des routes
│   ├── services/          # Logique métier
│   ├── data/              # Données statiques
│   ├── templates/         # Templates Jinja2
│   └── static/            # Assets CSS, JS
├── tests/                 # Suite de tests automatisés
├── docs/                  # Documentation
└── pyproject.toml         # Configuration des dépendances
```

## Domaines de contribution

### Haute priorité
- [ ] Ajouter plus de modèles de messages romantiques
- [ ] Améliorer les performances de génération vidéo
- [ ] Ajouter la prise en charge de plus de formats audio
- [ ] Améliorer le design responsive

### Priorité moyenne
- [ ] Ajouter l'internationalisation (i18n)
- [ ] Implémenter l'authentification utilisateur
- [ ] Ajouter des options de personnalisation vidéo
- [ ] Créer une interface d'administration

### Priorité faible
- [ ] Ajouter le partage sur les réseaux sociaux
- [ ] Implémenter des thèmes/modèles vidéo
- [ ] Ajouter le suivi analytique
- [ ] Créer une application mobile

## Signaler des problèmes

Lors du signalement de bugs, veuillez inclure :
- Étapes pour reproduire
- Comportement attendu vs réel
- Détails de l'environnement (OS, version Python, etc.)
- Messages d'erreur et traces de pile
- Captures d'écran si applicable

## Obtenir de l'aide

- Vérifier la [documentation](docs/)
- Rechercher dans les issues existantes
- Demander dans les discussions

## Licence

En contribuant, vous acceptez que vos contributions soient licenciées sous la même licence que le projet (MIT).
