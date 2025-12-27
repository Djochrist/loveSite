# Politique de sécurité

## Versions prises en charge

Nous prenons la sécurité au sérieux. Les versions suivantes de love_site sont actuellement prises en charge avec des mises à jour de sécurité :

| Version | Prise en charge          |
| ------- | ------------------------ |
| 0.1.x   | :white_check_mark:       |
| < 0.1   | :x:                      |

## Signaler une vulnérabilité

Si vous découvrez une vulnérabilité de sécurité dans love_site, veuillez nous aider en la signalant de manière responsable.

### Comment signaler

**Veuillez NE PAS signaler les vulnérabilités de sécurité via les issues publiques GitHub.**

Au lieu de cela, veuillez signaler les vulnérabilités de sécurité en créant un avis de sécurité privé sur [GitHub](https://github.com/Djochrist/loveSite/security/advisories/new).

### Que inclure

Lors du signalement d'une vulnérabilité, veuillez inclure :

- Une description claire de la vulnérabilité
- Étapes pour reproduire le problème
- Impact et gravité potentiels
- Corrections ou mesures d'atténuation suggérées
- Vos coordonnées pour le suivi

### Notre processus de réponse

1. **Accusé de réception** : Nous accuserons réception dans les 48 heures
2. **Enquête** : Nous enquêterons et validerons la vulnérabilité
3. **Développement de correctif** : Nous développerons et testerons un correctif
4. **Divulgation** : Nous coordonnerons la divulgation avec vous
5. **Publication** : Nous publierons le correctif et l'avis de sécurité

Nous visons à répondre à tous les rapports dans les 7 jours et à publier des correctifs dans les 30 jours pour les vulnérabilités critiques.

## Considérations de sécurité

### Pour les utilisateurs

- Toujours utiliser HTTPS en production
- Garder votre `SECRET_KEY` sécurisé et unique
- Mettre régulièrement à jour les dépendances
- Surveiller les mises à jour de sécurité
- Utiliser des mots de passe forts et uniques si l'authentification est ajoutée

### Pour les contributeurs

- Suivre les pratiques de codage sécurisé
- Valider toutes les entrées
- Utiliser des requêtes paramétrées si la fonctionnalité de base de données est ajoutée
- Implémenter une gestion d'erreur appropriée
- Éviter de journaliser les informations sensibles

### Mesures de sécurité actuelles

- Protection CSRF sur les formulaires
- Validation et assainissement des entrées
- Gestion sécurisée des téléversements de fichiers
- En-têtes de sécurité de contenu
- Gestion sécurisée des sessions
- Analyse des vulnérabilités des dépendances

## Considérations de sécurité connues

### Sécurité des téléversements de fichiers
- Validation du type de fichier par extension et contenu
- Limites de taille (50 Mo maximum)
- Génération sécurisée de noms de fichiers
- Nettoyage des fichiers temporaires

### Protection des données
- Aucune donnée personnelle stockée (actuellement)
- Gestion sécurisée des fichiers temporaires
- Nettoyage automatique du contenu généré

### Sécurité réseau
- Application forcée de HTTPS en production
- Configuration des en-têtes sécurisés
- Considérations de limitation du taux

## Tests de sécurité

Nous utilisons des outils automatisés pour les tests de sécurité :

- **Bandit** : Linter de sécurité Python
- **Safety** : Analyse des vulnérabilités des dépendances
- **CodeQL** : Analyse statique (GitHub Advanced Security)

## Contact

Pour les questions ou préoccupations liées à la sécurité, contactez les mainteneurs à [security@love-site.dev](mailto:security@love-site.dev).
