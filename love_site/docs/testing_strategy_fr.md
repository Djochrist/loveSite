# Stratégie de tests automatisés - love_site

## Vue d'ensemble

La stratégie de tests pour `love_site` adopte une approche pyramidale rigoureuse, structurée en trois niveaux hiérarchiques : tests unitaires, tests d'intégration et tests d'application. Cette architecture assure une couverture complète des fonctionnalités critiques tout en maintenant des performances d'exécution optimales. L'implémentation repose sur pytest comme framework principal, avec intégration native des meilleures pratiques de test Python.

## Niveaux de tests

### 1. Tests unitaires (`tests/unit/`)

**Objectif** : Valider la logique métier isolée.

**Couverture** :
- Fonctions de service (chargement et personnalisation des messages)
- Gestion d'erreur (fichiers manquants, JSON invalide)
- Remplacement des espaces réservés

**Exemples** :
```python
def test_personalize_messages():
    messages = [{"id": 1, "text": "Hello {lover}"}]
    result = personalize_messages(messages, "Alice", "Bob")
    assert result[0]['text'] == "Hello Alice"
```

**Meilleures pratiques** :
- Utiliser des mocks pour les dépendances externes (fichiers, I/O)
- Tester les cas limites et erreurs
- Maintenir > 90% de couverture pour les services

### 2. Tests d'intégration (`tests/integration/`)

**Objectif** : Valider l'interaction entre composants.

**Couverture** :
- Routes Flask et rendu des templates
- Intégration service/route
- Gestion des formulaires et personnalisation

**Exemples** :
```python
def test_index_post_with_data(client):
    data = {'lover_name': 'Marie', 'sender_name': 'Pierre'}
    resp = client.post('/', data=data)
    assert b'Marie' in resp.data
```

**Meilleures pratiques** :
- Utiliser le client de test Flask
- Tester les données POST et GET
- Vérifier le contenu HTML rendu

### 3. Tests d'application (`tests/application/`)

**Objectif** : Valider le comportement global de l'application.

**Couverture** :
- Création d'application Flask et configuration
- Enregistrement des blueprints
- Accès aux fichiers statiques
- Rendu complet des templates
- Workflow de génération vidéo (optionnel, nécessite moviepy/ffmpeg)

**Exemples** :
```python
def test_app_creation():
    app = create_app(Config)
    assert app.config['TESTING'] is False
```

**Meilleures pratiques** :
- Tester la configuration
- Vérifier l'intégration des composants
- Tests de régression pour les changements majeurs

## Métriques de qualité

### Couverture du code
- **Cible** : > 80% globale
- **Services** : > 90%
- **Routes** : > 70%
- **Application** : > 60%

### Exécution
- **Temps** : < 30 secondes pour tous les tests
- **Fréquence** : À chaque commit (pre-push)
- **CI/CD** : Obligatoire intégration continue

## Outils et frameworks

### pytest
- Framework de test principal
- Fixtures pour la réutilisabilité
- Paramétrisation pour des tests similaires
- Plugins : coverage, pytest-watch

### Configuration
```toml
[tool.pytest]
addopts = "-q"
```

### Mocking
- `unittest.mock` pour les dépendances externes
- Isolation des tests unitaires
- Simulation d'erreurs (fichiers manquants, etc.)

## Tests par fonctionnalité

### Messages personnalisables
- ✅ Chargement JSON valide/invalide
- ✅ Remplacement des espaces réservés
- ✅ Valeurs par défaut

### Routes et formulaires
- ✅ GET/POST sur /
- ✅ Validation des données
- ✅ Rendu conditionnel (formulaire/messages)

### Animations et frontend
- ❌ Tests automatisés difficiles (nécessiterait Selenium/Playwright)
- ✅ Tests manuels documentés
- ✅ Vérification des assets statiques

### Design responsive
- ❌ Tests CSS difficiles à automatiser
- ✅ Tests manuels sur différents appareils
- ✅ Validation HTML/CSS via outils externes

## Workflow de tests

### Développement
1. Écrire d'abord les tests unitaires (TDD)
2. Implémenter la fonctionnalité
3. Tests d'intégration
4. Tests d'application
5. Vérifier la couverture

### CI/CD
```yaml
# Exemple GitHub Actions
- name: Exécuter les tests
  run: uv run pytest --cov=app --cov-report=xml
- name: Téléverser la couverture
  uses: codecov/codecov-action@v3
```

### Débogage des tests
- Utiliser `--pdb` pour le débogage
- Vérifier les logs Flask en mode test
- Isoler les tests défaillants

## Maintenance des tests

### Ajout de nouvelles fonctionnalités
- Créer des tests avant l'implémentation
- Mettre à jour les tests existants si nécessaire
- Maintenir la couverture

### Refactorisation
- Les tests protègent contre les régressions
- Refactoriser les tests si le code change
- Supprimer les tests obsolètes

### Performance
- Optimiser les fixtures lentes
- Utiliser des mocks pour éviter les I/O
- Paralléliser si nécessaire

Cette stratégie assure la fiabilité et la maintenabilité du site romantique, permettant des évolutions sûres et des déploiements confiants.
