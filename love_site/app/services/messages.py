"""Love messages management service.

This module provides functionality to load and personalize
love messages from a JSON file.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Define relative paths to the project
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "messages.json"


def load_messages():
    """Load messages from the data JSON file.

    Returns:
        list[dict]: List of messages containing 'id' and 'text' with placeholders.
                   Returns an empty list on loading error.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        # Validate and filter valid messages
        messages = [
            msg for msg in data.get("messages", [])
            if isinstance(msg, dict) and "text" in msg
        ]
        return messages
    except FileNotFoundError:
        logger.warning(f"Messages file not found: {DATA_FILE}")
        return []
    except json.JSONDecodeError:
        logger.exception(f"Invalid JSON in messages file: {DATA_FILE}")
        return []
    except Exception:
        logger.exception("Unexpected error loading messages")
        return []


def personalize_messages(messages, lover_name="", sender_name="Djochrist"):
    """Personalize messages by substituting placeholders.

    Args:
        messages (list[dict]): List of raw messages with placeholders.
        lover_name (str): Name of the loved one. Default "".
        sender_name (str): Sender's name. Default "Djochrist".

    Returns:
        list[dict]: List of personalized messages with substitutions applied.
    """
    personalized = []
    for message in messages:
        text = message.get("text", "")
        # Substitute loved one's name
        if lover_name and lover_name.strip():
            text = text.replace("{lover}", lover_name.strip())
        else:
            text = text.replace("{lover}", "my love")

        # Substitute sender's name
        if sender_name and sender_name.strip():
            text = text.replace("{sender}", sender_name.strip())
        else:
            text = text.replace("{sender}", "Djochrist")

        personalized.append({
            "id": message.get("id"),
            "text": text
        })

    return personalized
