# Déploiement — Notes de production pour love_site

Ce document couvre les meilleures pratiques et étapes pour déployer `love_site` dans un environnement de production.

## 1) Environnement et secrets
- **SECRET_KEY** doit être défini dans l'environnement pour ProductionConfig. NE PAS commiter de vraies clés secrètes dans le dépôt.
```bash
export SECRET_KEY="remplacer_par_une_chaine_longue_aleatoire"
```
- Garder la configuration d'environnement gérée de manière centralisée (unité systemd, secrets Docker, ou sections variables d'environnement du fournisseur cloud).

## 2) Serveur WSGI
Utiliser Gunicorn ou uWSGI devant Flask. Commande `gunicorn` exemple (exécuter depuis la racine du projet) :
```bash
uv run gunicorn -w 4 -b 0.0.0.0:8000 "love_site.app:create_app()"
```
Placer un proxy inverse HTTP (Nginx) devant Gunicorn pour la terminaison TLS et la mise en cache des assets statiques.

## 3) Fichiers statiques et assets
- Servir les assets statiques avec votre proxy inverse (Nginx) ou CDN.
- Activer les en-têtes de cache pour les assets CSS/JS.

## 4) FFmpeg et génération vidéo
- S'assurer que `ffmpeg` est installé et disponible pour l'utilisateur de l'application (utilisé par `moviepy`).
- Les vidéos générées sont stockées temporairement dans le répertoire temp du système et sont programmées pour suppression ; envisager une configuration de stockage sécurisé pour une rétention plus longue.

## 5) Sécurité
- Servir l'application sur HTTPS.
- Utiliser une `SECRET_KEY` forte et ne pas utiliser de clés de développement en production.
- Durcir les paramètres `gunicorn` et proxy inverse (limitation du taux, délais d'attente, etc.).

## 6) Logs et surveillance
- Envoyer les logs vers un système centralisé (ELK, Loki, Papertrail, ou logs du fournisseur cloud).
- Surveiller l'utilisation du disque dans `/tmp` si la génération vidéo est fréquente.

## 7) Docker (optionnel)
Un exemple de Dockerfile est inclus dans `docs/workflow.md`. Pour les images de production, utiliser des builds multi-étapes et épingler les versions pour des builds reproductibles.

## 8) Sauvegardes et nettoyage
- Nettoyer périodiquement les anciens fichiers média temporaires.
- Si vous stockez des téléversements utilisateur ou des vidéos générées pour plus longtemps, programmer une sauvegarde sécurisée.

## 9) Mise à l'échelle
- Utiliser une file d'attente de tâches pour la génération vidéo si vous vous attendez à une utilisation lourde (par exemple Redis + RQ/Celery) pour éviter de bloquer le worker web.
- Décharger les tâches lourdes de création vidéo vers des instances worker ou des fonctions serverless si le trafic augmente.
