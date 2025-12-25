"""
Service de gestion des messages d'amour.

Ce module fournit les fonctionnalités pour charger et personnaliser
les messages d'amour depuis un fichier JSON.
"""

import json
from pathlib import Path

# Définition des chemins relatifs au projet
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "messages.json"


def load_messages():
    """
    Charge les messages depuis le fichier JSON de données.

    Returns:
        list[dict]: Liste des messages contenant 'id' et 'text' avec placeholders.
                   Retourne une liste vide en cas d'erreur de chargement.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        # Validation et filtrage des messages valides
        messages = [
            msg for msg in data.get("messages", [])
            if isinstance(msg, dict) and "text" in msg
        ]
        return messages
    except FileNotFoundError:
        # Fichier de données manquant - comportement dégradé
        return []
    except (json.JSONDecodeError, KeyError, TypeError):
        # Erreur de format JSON ou structure inattendue
        return []


def personalize_messages(messages, lover_name="", sender_name="Djochrist"):
    """
    Personnalise les messages en substituant les placeholders.

    Args:
        messages (list[dict]): Liste des messages bruts avec placeholders.
        lover_name (str): Nom de la personne aimée. Défaut "".
        sender_name (str): Nom de l'expéditeur. Défaut "Djochrist".

    Returns:
        list[dict]: Liste des messages personnalisés avec substitutions appliquées.
    """
    personalized = []
    for message in messages:
        text = message["text"]
        # Substitution du nom de l'être aimé
        if lover_name.strip():
            text = text.replace("{lover}", lover_name.strip())
        else:
            # Valeur par défaut élégante
            text = text.replace("{lover}", "mon amour")

        # Substitution du nom de l'expéditeur
        if sender_name.strip():
            text = text.replace("{sender}", sender_name.strip())
        else:
            text = text.replace("{sender}", "Djochrist")

        personalized.append({
            "id": message["id"],
            "text": text
        })

    return personalized
