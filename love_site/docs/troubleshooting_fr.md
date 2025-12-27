# Dépannage — Problèmes courants et solutions (Convivial pour débutants)

Ce fichier liste les erreurs courantes que vous pourriez rencontrer lors de la configuration ou de l'exécution du projet, et montre des corrections claires étape par étape.

## 1) Erreur d'analyse TOML lors de l'exécution de `uv sync`
Symptôme :
```
Erreur d'analyse TOML à la ligne ...
clé non cotée invalide
```
Cause : `pyproject.toml` contient une syntaxe non TOML (par exemple une ligne Python comme `dependencies.append(...)`).
Correction :
1. Ouvrir `pyproject.toml` et s'assurer que le tableau `dependencies = [ ... ]` contient toutes les chaînes requises.
2. Supprimer toute ligne Python comme `dependencies.append(...)`.
3. Exécuter `uv sync` à nouveau.

## 2) Erreur ModuleNotFoundError : Aucun module nommé 'flask_wtf' ou autres paquets manquants
Symptôme : ImportError au démarrage (`flask_wtf`, `moviepy`, etc.).
Correction :
```bash
uv sync  # garantit l'installation des dépendances dans pyproject
```
Si `moviepy` est manquant, assurez-vous également que FFmpeg est installé (voir Démarrage rapide).

## 3) Erreur ModuleNotFoundError : Aucun module nommé 'moviepy.editor' ou erreurs ffmpeg
Cause : `moviepy` non installé ou `ffmpeg` système manquant.
Correction :
```bash
uv sync
# Installer ffmpeg sur Linux
sudo apt update && sudo apt install ffmpeg
# ou sur macOS
brew install ffmpeg
```

## 4) L'application lève SyntaxError : chaîne littérale triple non terminée après modifications
Cause : collage accidentel laissant une chaîne littérale triple ouverte ou un commentaire dans un fichier.
Correction : Réouvrir le fichier mentionné dans la trace et fermer la triple guillemet (""" ou '''), ou annuler la mauvaise modification.

## 5) Fichiers uv.lock dupliqués
Symptôme : Vous trouvez `uv.lock` à la racine du projet et dans `love_site/`.
Recommandation :
- Garder le lockfile à la racine de haut niveau si vous utilisez le dépôt comme un tout ; supprimer le sous-projet lock avec `git rm love_site/uv.lock` s'il n'est pas un projet autonome.
- Si `love_site/` est destiné à être un package autonome, garder son `uv.lock` et supprimer celui de la racine.

## 6) Erreurs CSRF / SECRET_KEY en production
En production, définir `SECRET_KEY` de manière sécurisée :
```bash
export SECRET_KEY="une chaine très longue aléatoire"
# ou définir dans votre unité systemd / environnement conteneur
```
La classe `ProductionConfig` lève une erreur si la `SECRET_KEY` est manquante.

## 7) Échec de génération vidéo à l'exécution (erreurs codec ou write_videofile)
Conseils :
- S'assurer que le système ffmpeg supporte `libx264` et `aac`. Installer un package ffmpeg complet pour votre OS.
- Vérifier les logs d'exécution pour les messages `moviepy`.
- Comme solution de secours, essayer différents codecs configurés dans `love_site/app/config.py`.
- Vérifier que le répertoire temporaire a les permissions d'écriture.

## 8) Problèmes de téléversement de fichiers
- S'assurer que `MAX_CONTENT_LENGTH` (50 Mo par défaut) n'est pas dépassé.
- S'assurer que les extensions de fichiers téléversés correspondent à `ALLOWED_EXTENSIONS` dans `config.py`.
- Si les téléversements échouent, vérifier les permissions de fichiers et les logs d'erreur Flask.

## 9) Conseils de débogage général
- Réexécuter `uv sync` pour s'assurer de la cohérence des dépendances.
- Exécuter les tests : `uv run pytest`.
- Utiliser `uv run python -m pdb <script>` si vous devez parcourir le code défaillant.

Si vous ne parvenez toujours pas à résoudre un problème, ouvrez un issue avec la trace d'erreur exacte et les commandes que vous avez exécutées — cela aide un mainteneur à reproduire et déboguer plus rapidement.
