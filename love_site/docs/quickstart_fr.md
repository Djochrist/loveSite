# Quickstart (FR) — love_site

Guide pas‑à‑pas pour débutants — comment cloner, installer, lancer et tester l'application.

## Prérequis
- Python 3.8+ (3.11 recommandé)
- Git
- Le gestionnaire de dépendances `uv` (https://github.com/astral-sh/uv)
- Pour la génération vidéo/audio : FFmpeg installé (moviepy en dépend)
  - Ubuntu/Debian : `sudo apt update && sudo apt install ffmpeg`
  - macOS (Homebrew) : `brew install ffmpeg`

## Cloner le dépôt
```bash
git clone https://github.com/Djochrist/loveSite.git
cd loveSite
```

## Installer les dépendances
`uv` lit `pyproject.toml` et `uv.lock`. Pour installer :
```bash
uv sync
```
Cela crée/actualise un environnement virtuel et installe les paquets.

## Lancer l'application (développement)
Deux façons pratiques :

1) Via la commande Flask (recommandé) :
```bash
uv run flask run
```
Par défaut l'application sera accessible sur `http://localhost:5000`.

2) Lancer le package directement :
```bash
uv run python -m love_site.app.main
```

## Tester l'application
Exécuter la suite de tests :
```bash
uv run pytest
```
Lancer des sous-ensembles :
```bash
uv run pytest tests/unit/
uv run pytest tests/integration/
uv run pytest tests/application/
```

## Tour rapide de l'interface
- Remplissez les noms de l'expéditeur et du destinataire pour personnaliser les messages
- Ajoutez optionnellement des messages personnalisés ou téléversez de la musique de fond (MP3, WAV, etc.)
- Cliquez sur "Générer la vidéo" pour créer et télécharger votre vidéo d'amour personnalisée

## Fichiers à connaître
- Messages : `love_site/app/data/messages.json`
- Configuration : `love_site/app/config.py` (variables : `MAX_CONTENT_LENGTH`, `ALLOWED_EXTENSIONS`, `VIDEO_FPS`, `VIDEO_WIDTH`, `VIDEO_HEIGHT`, `VIDEO_CODEC`, `AUDIO_CODEC`, `SECRET_KEY`) 
- Templates : `love_site/app/templates/` (Jinja2)
- Styles/JS : `love_site/app/static/`

Si vous êtes novice : en cas de problème, consultez `troubleshooting_fr.md` pour les solutions détaillées.
