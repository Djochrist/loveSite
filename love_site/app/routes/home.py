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


@home_bp.route("/", methods=["GET", "POST"])
def index():
    """
    Main application route.

    Handles form display (GET) and processing of submitted data
    to generate personalized messages (POST).

    Returns:
        Response: Rendered template with appropriate data.
    """
    messages = []
    lover_name = ""
    sender_name = "Djochrist"  # Default value

    if request.method == "POST":
        # Retrieve form data
        lover_name_raw = request.form.get("lover_name", "").strip()
        sender_name_raw = request.form.get("sender_name", "Djochrist").strip()

        # Validate inputs
        lover_name, lover_errors = validate_name(lover_name_raw, "lover's first name")
        sender_name, sender_errors = validate_name(sender_name_raw, "sender's first name")

        # If validation errors, display messages
        all_errors = lover_errors + sender_errors
        if all_errors:
            for error in all_errors:
                flash(error, "error")
            # Preserve entered values for correction
            lover_name = lover_name_raw[:50]
            sender_name = sender_name_raw[:50] or "Djochrist"
        else:
            # Attempt to load and personalize messages
            try:
                raw_messages = load_messages()
                if not raw_messages:
                    flash("Error: Unable to load messages.", "error")
                else:
                    messages = personalize_messages(raw_messages, lover_name, sender_name)
            except Exception as e:
                flash("Error processing messages.", "error")
                messages = []

    # Render template with contextual data
    return render_template(
        "index.html",
        messages=messages,
        lover_name=lover_name,
        sender_name=sender_name
    )
