# Stratégie de Test Automatisé - love_site

## Vue d'ensemble

La stratégie de test de `love_site` adopte une approche pyramidale rigoureuse, structurée en trois niveaux hiérarchiques : tests unitaires, d'intégration et applicatifs. Cette architecture garantit une couverture complète des fonctionnalités critiques tout en maintenant des performances optimales d'exécution. L'implémentation repose sur pytest comme framework principal, avec une intégration native des meilleures pratiques de test en Python.

## Niveaux de tests

### 1. Tests unitaires (`tests/unit/`)

**Objectif** : Valider la logique métier isolée.

**Couverture** :
- Fonctions de service (chargement et personnalisation des messages)
- Gestion d'erreurs (fichiers manquants, JSON invalide)
- Remplacement des placeholders

**Exemples** :
```python
def test_personalize_messages():
    messages = [{"id": 1, "text": "Hello {lover}"}]
    result = personalize_messages(messages, "Alice", "Bob")
    assert result[0]['text'] == "Hello Alice"
```

**Bonnes pratiques** :
- Utiliser des mocks pour les dépendances externes (fichiers, I/O)
- Tester les cas limites et d'erreur
- Maintenir une couverture > 90% pour les services

### 2. Tests d'intégration (`tests/integration/`)

**Objectif** : Valider l'interaction entre composants.

**Couverture** :
- Routes Flask et rendu des templates
- Intégration services/routes
- Gestion des formulaires et personnalisation

**Exemples** :
```python
def test_index_post_with_data(client):
    data = {'lover_name': 'Marie', 'sender_name': 'Pierre'}
    resp = client.post('/', data=data)
    assert b'Marie' in resp.data
```

**Bonnes pratiques** :
- Utiliser le client de test Flask
- Tester les données POST et GET
- Vérifier le contenu HTML rendu

### 3. Tests applicatifs (`tests/application/`)

**Objectif** : Valider le comportement global de l'application.

**Couverture** :
- Création et configuration de l'app Flask
- Enregistrement des blueprints
- Accès aux fichiers statiques
- Rendu des templates complets

**Exemples** :
```python
def test_app_creation():
    app = create_app(Config)
    assert app.config['TESTING'] is False
```

**Bonnes pratiques** :
- Tester la configuration
- Vérifier l'intégration des composants
- Tests de régression pour les changements majeurs

## Métriques de qualité

### Couverture de code
- **Cible** : > 80% global
- **Services** : > 90%
- **Routes** : > 70%
- **Application** : > 60%

### Exécution
- **Temps** : < 30 secondes pour tous les tests
- **Fréquence** : À chaque commit (pré-push)
- **CI/CD** : Intégration continue obligatoire

## Outils et frameworks

### pytest
- Framework principal de test
- Fixtures pour la réutilisabilité
- Paramétrisation pour les tests similaires
- Plugins : coverage, pytest-watch

### Configuration
```toml
[tool.pytest]
addopts = "-q"
```

### Mocking
- `unittest.mock` pour les dépendances externes
- Isolation des tests unitaires
- Simulation des erreurs (fichiers manquants, etc.)

## Types de tests par fonctionnalité

### Messages personnalisables
- ✅ Chargement JSON valide/invalide
- ✅ Remplacement des placeholders
- ✅ Valeurs par défaut

### Routes et formulaires
- ✅ GET/POST sur /
- ✅ Validation des données
- ✅ Rendu conditionnel (formulaire/messages)

### Animations et frontend
- ❌ Tests automatisés difficiles (nécessiterait Selenium/Playwright)
- ✅ Tests manuels documentés
- ✅ Vérification des assets statiques

### Responsive design
- ❌ Tests CSS difficiles à automatiser
- ✅ Tests manuels sur différents appareils
- ✅ Validation HTML/CSS via outils externes

## Workflow de test

### Développement
1. Écrire les tests unitaires en premier (TDD)
2. Implémenter la fonctionnalité
3. Tests d'intégration
4. Tests applicatifs
5. Vérifier la couverture

### CI/CD
```yaml
# Exemple GitHub Actions
- name: Run tests
  run: uv run pytest --cov=app --cov-report=xml
- name: Upload coverage
  uses: codecov/codecov-action@v3
```

### Debug des tests
- Utiliser `--pdb` pour déboguer
- Vérifier les logs Flask en mode test
- Isoler les tests qui échouent

## Maintenance des tests

### Ajout de nouvelles fonctionnalités
- Créer des tests avant l'implémentation
- Mettre à jour les tests existants si nécessaire
- Maintenir la couverture

### Refactoring
- Les tests protègent contre les régressions
- Refactoriser les tests si le code change
- Supprimer les tests obsolètes

### Performance
- Optimiser les fixtures lentes
- Utiliser des mocks pour éviter les I/O
- Paralléliser si nécessaire

Cette stratégie assure la fiabilité et la maintenabilité du site romantique, permettant des évolutions sûres et des déploiements confiants.
