"""
Main routes for the love_site application.

This module defines Flask endpoints for the user interface,
handling form display and rendering of personalized messages.
"""

import re
from flask import Blueprint, render_template, request, flash

from ..services.messages import load_messages, personalize_messages

# Blueprint for home page routes
home_bp = Blueprint("home", __name__)


def validate_name(name, field_name):
    """
    Validate a user-entered name.

    Args:
        name (str): The name to validate.
        field_name (str): Field name for error messages.

    Returns:
        tuple: (validated_name, errors)
    """
    errors = []

    # Remove whitespace and limit length
    name = name.strip()[:50]  # Max 50 characters

    if not name:
        return "", errors  # Empty allowed for lover_name

    # Validate characters: letters, spaces, apostrophes, hyphens
    if not re.match(r"^[a-zA-ZÀ-ÿ\s'-]+$", name):
        errors.append(f"The {field_name} contains invalid characters.")

    # Check minimum length (if not empty)
    if len(name) < 2:
        errors.append(f"The {field_name} must contain at least 2 characters.")

    return name, errors


@home_bp.route("/", methods=["GET"])
def index():
    """
    Main application route.

    Displays personalized love messages with hardcoded names.

    Returns:
        Response: Rendered template with messages.
    """
    # Hardcoded personalization
    lover_name = "bae"
    sender_name = "Djochrist"

    messages = []
    try:
        raw_messages = load_messages()
        if raw_messages:
            messages = personalize_messages(raw_messages, lover_name, sender_name)
        else:
            flash("Error: Unable to load messages.", "error")
    except Exception as e:
        flash("Error processing messages.", "error")
        messages = []

    # Render template with messages displayed directly
    return render_template(
        "index.html",
        messages=messages,
        lover_name=lover_name,
        sender_name=sender_name
    )
