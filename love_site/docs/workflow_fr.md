# Guide de développement - love_site

## Prérequis système

- **Python** : Version 3.8 ou supérieure
- **Gestionnaire de dépendances** : uv (recommandé pour sa vitesse et fiabilité)

## Configuration de l'environnement de développement

### 1. Récupération du code source
```bash
git clone <url-dépôt>
cd love_site
```

### 2. Installation des dépendances
```bash
# Installation optimisée avec uv
uv sync

# Vérification de l'environnement (optionnel)
uv run --isolated python --version
```

### 3. Validation de l'installation
```bash
# Exécuter les tests pour vérifier l'intégrité
uv run pytest
```

## Cycle de développement

### Démarrage du serveur local
```bash
# Commande principale (depuis le répertoire love_site)
uv run python -m app.main

# Alternative : exécuter le module directement
uv run python app/main.py

# Ou utiliser la CLI Flask
uv run flask run
```

**Point d'accès** : http://localhost:5000

### Processus itératif
1. **Modification du code** dans le répertoire `app/`
2. **Test automatique** des modifications via le navigateur
3. **Exécuter les tests** : `uv run pytest`
4. **Validation** de la qualité du code

## Stratégie de tests automatisés

### Exécution complète
```bash
uv run pytest
```

### Tests spécialisés
```bash
# Tests unitaires - logique métier isolée
uv run pytest tests/unit/

# Tests d'intégration - interactions entre composants
uv run pytest tests/integration/

# Tests d'application - comportement global
uv run pytest tests/application/

# Analyse de couverture
uv run pytest --cov=app --cov-report=html
```

### Surveillance continue (optionnel)
```bash
# Installation : uv add --dev pytest-watch
uv run pytest-watch
```

## Gestion des versions et collaboration

### Branches et commits
```bash
# Créer une branche fonctionnelle
git checkout -b feature/description-fonctionnalite

# Développement et validation
git add .
git commit -m "feat: implémentation de nouvelle fonctionnalité

- Description détaillée des changements
- Impact sur les autres composants
- Tests ajoutés/modifiés"

# Validation avant soumission
uv run pytest
```

### Pull Request
```bash
# Synchronisation
git push origin feature/description-fonctionnalite

# Créer une PR avec description complète
# Inclure des captures d'écran si applicable
```

## Déploiement et production

### Environnement de développement
- Serveur local : `uv run python app/main.py`
- Mode debug activé pour le développement

### Environnement de production
- **Serveur WSGI** : Gunicorn ou uWSGI recommandé
- **Variables d'environnement** : Configuration sécurisée
- **Logs** : Surveillance et rotation
- **SSL/TLS** : Chiffrement obligatoire

### Conteneurisation (optionnel)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
RUN uv sync --no-dev
COPY . .
EXPOSE 5000
CMD ["uv", "run", "python", "app/main.py"]
```

## Standards de qualité et meilleures pratiques

### Qualité du code
- **PEP 8** : Conformité stricte aux standards Python
- **Tests** : Couverture > 80%, TDD préféré
- **Documentation** : Docstrings complètes, README à jour
- **Commits** : Messages descriptifs et conventionnels

### Tests et validation
- **Couverture** : Maintenir > 80% globale
- **Cas d'erreur** : Gestion robuste des exceptions
- **Mocks** : Isolation des dépendances externes
- **Performance** : Tests de charge si nécessaire

### Performance et optimisation
- **Assets statiques** : Minification et mise en cache
- **Requêtes HTTP** : Minimisation et optimisation
- **Base de données** : Indexation et requêtes optimisées
- **Cache** : Cache intelligent si applicable

## Dépannage et maintenance

### Problèmes courants

#### Dépendances
```bash
# Régénération complète de l'environnement
uv sync --reinstall

# Nettoyage du cache
uv cache clean
```

#### Tests défaillants
- Vérification des chemins relatifs
- Validation des fixtures et mocks
- Cohérence des données de test

#### Animations frontend
- Console de développement du navigateur
- Compatibilité cross-navigateur
- Validation des chemins d'assets
- Transmission de données JavaScript : Utiliser des balises `<script>` pour injecter des données au lieu d'attributs HTML `data-*` pour éviter les problèmes d'échappement avec les caractères spéciaux (apostrophes, guillemets)

#### Performance
- Profiling avec `cProfile`
- Optimisation des requêtes SQL
- Cache et compression

### Maintenance préventive
- **Mises à jour** : Dépendances et sécurité
- **Surveillance** : Logs et métriques
- **Sauvegardes** : Données critiques
- **Documentation** : Mise à jour continue

## Contribution externe

### Processus standard
1. **Fork** du dépôt principal
2. **Branche fonctionnelle dédiée**
3. **Développement avec tests**
4. **Pull Request** avec description détaillée
5. **Revue** et validation automatisée
6. **Fusion** après approbation

### Critères de qualité
- Tests réussis et couverture maintenue
- Revue de code positive
- Documentation mise à jour
- Conformité aux standards du projet

Cette méthodologie assure un développement professionnel, maintenable et évolutif pour love_site.
