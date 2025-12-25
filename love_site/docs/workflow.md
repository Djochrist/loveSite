# Guide de Développement - love_site

## Prérequis Système

- **Python** : Version 3.8 ou supérieure
- **Gestionnaire de dépendances** : uv (recommandé pour sa rapidité et fiabilité)

## Configuration de l'Environnement de Développement

### 1. Récupération du Code Source
```bash
git clone <repository-url>
cd love_site
```

### 2. Installation des Dépendances
```bash
# Installation optimisée avec uv
uv sync

# Vérification de l'environnement (optionnel)
uv run --isolated python --version
```

### 3. Validation de l'Installation
```bash
# Exécution des tests pour vérifier l'intégrité
uv run pytest
```

## Cycle de Développement

### Démarrage du Serveur Local
```bash
# Commande principale
uv run python app/main.py

# Alternative avec Flask CLI
uv run flask run
```

**Point d'accès** : http://localhost:5000

### Processus Itératif
1. **Modification du code** dans le répertoire `app/`
2. **Test automatique** des changements via le navigateur
3. **Exécution des tests** : `uv run pytest`
4. **Validation** de la qualité du code

## Stratégie de Test Automatisé

### Exécution Complète
```bash
uv run pytest
```

### Tests Spécialisés
```bash
# Tests unitaires - logique métier isolée
uv run pytest tests/unit/

# Tests d'intégration - interactions composants
uv run pytest tests/integration/

# Tests applicatifs - comportement global
uv run pytest tests/application/

# Analyse de couverture
uv run pytest --cov=app --cov-report=html
```

### Surveillance Continue (Optionnel)
```bash
# Installation : uv add --dev pytest-watch
uv run pytest-watch
```

## Gestion de Version et Collaboration

### Branches et Commits
```bash
# Création de branche fonctionnelle
git checkout -b feature/enhancement-description

# Développement et validation
git add .
git commit -m "feat: implémentation de la nouvelle fonctionnalité

- Description détaillée des changements
- Impact sur les autres composants
- Tests ajoutés/modifiés"

# Validation avant soumission
uv run pytest
```

### Pull Request
```bash
# Synchronisation
git push origin feature/enhancement-description

# Création de PR avec description complète
# Inclure captures d'écran si applicable
```

## Déploiement et Production

### Environnement de Développement
- Serveur local : `uv run python app/main.py`
- Debug activé pour le développement

### Environnement de Production
- **Serveur WSGI** : Gunicorn ou uWSGI recommandé
- **Variables d'environnement** : Configuration sécurisée
- **Logs** : Monitoring et rotation
- **SSL/TLS** : Chiffrement obligatoire

### Conteneurisation (Optionnel)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install uv && uv sync --no-dev
COPY . .
EXPOSE 5000
CMD ["uv", "run", "python", "app/main.py"]
```

## Standards de Qualité et Bonnes Pratiques

### Qualité du Code
- **PEP 8** : Conformité stricte aux standards Python
- **Tests** : Couverture > 80%, TDD privilégié
- **Documentation** : Docstrings complètes, README à jour
- **Commits** : Messages descriptifs et conventionnels

### Tests et Validation
- **Couverture** : Maintenir > 80% global
- **Cas d'erreur** : Gestion robuste des exceptions
- **Mocks** : Isolation des dépendances externes
- **Performance** : Tests de charge si nécessaire

### Performance et Optimisation
- **Assets statiques** : Minification et cache
- **Requêtes HTTP** : Minimisation et optimisation
- **Base de données** : Indexing et requêtes optimisées
- **Mémorisation** : Cache intelligent si applicable

## Dépannage et Maintenance

### Problèmes Courants

#### Dépendances
```bash
# Régénération complète de l'environnement
uv sync --reinstall

# Nettoyage du cache
uv cache clean
```

#### Tests Défaillants
- Vérification des chemins relatifs
- Validation des fixtures et mocks
- Cohérence des données de test

#### Animations Frontend
- Console développeur du navigateur
- Compatibilité cross-navigateur
- Validation des chemins d'assets
- Transmission des données JavaScript : Utiliser des balises `<script>` pour injecter les données au lieu d'attributs HTML `data-*` afin d'éviter les problèmes d'échappement avec les caractères spéciaux (apostrophes, guillemets)

#### Performance
- Profilage avec `cProfile`
- Optimisation des requêtes SQL
- Cache et compression

### Maintenance Préventive
- **Mises à jour** : Dépendances et sécurité
- **Monitoring** : Logs et métriques
- **Sauvegardes** : Données critiques
- **Documentation** : Mise à jour continue

## Contribution Externe

### Processus Standard
1. **Fork** du repository principal
2. **Branche feature** dédiée
3. **Développement** avec tests
4. **Pull Request** avec description détaillée
5. **Review** et validation automatisée
6. **Merge** après approbation

### Critères de Qualité
- Tests passants et couverture maintenue
- Code review positive
- Documentation mise à jour
- Conformité aux standards du projet

Cette méthodologie assure un développement professionnel, maintenable et scalable pour love_site.
