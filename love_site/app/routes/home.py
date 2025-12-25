"""
Routes principales de l'application love_site.

Ce module définit les endpoints Flask pour l'interface utilisateur,
gérant l'affichage du formulaire et le rendu des messages personnalisés.
"""

import re
from flask import Blueprint, render_template, request, flash

from ..services.messages import load_messages, personalize_messages

# Blueprint pour les routes de la page d'accueil
home_bp = Blueprint("home", __name__)


def validate_name(name, field_name):
    """
    Valide un nom saisi par l'utilisateur.

    Args:
        name (str): Le nom à valider.
        field_name (str): Nom du champ pour les messages d'erreur.

    Returns:
        tuple: (nom_validé, erreurs)
    """
    errors = []

    # Suppression des espaces et limitation de longueur
    name = name.strip()[:50]  # Max 50 caractères

    if not name:
        return "", errors  # Vide autorisé pour lover_name

    # Validation des caractères : lettres, espaces, apostrophes, tirets
    if not re.match(r"^[a-zA-ZÀ-ÿ\s'-]+$", name):
        errors.append(f"Le {field_name} contient des caractères invalides.")

    # Vérification de la longueur minimale (si non vide)
    if len(name) < 2:
        errors.append(f"Le {field_name} doit contenir au moins 2 caractères.")

    return name, errors


@home_bp.route("/", methods=["GET", "POST"])
def index():
    """
    Route principale de l'application.

    Gère l'affichage du formulaire de personnalisation (GET) et le traitement
    des données soumises pour générer les messages personnalisés (POST).

    Returns:
        Response: Template rendu avec les données appropriées.
    """
    messages = []
    lover_name = ""
    sender_name = "Djochrist"  # Valeur par défaut

    if request.method == "POST":
        # Récupération des données du formulaire
        lover_name_raw = request.form.get("lover_name", "").strip()
        sender_name_raw = request.form.get("sender_name", "Djochrist").strip()

        # Validation des entrées
        lover_name, lover_errors = validate_name(lover_name_raw, "prénom de la personne aimée")
        sender_name, sender_errors = validate_name(sender_name_raw, "prénom de l'expéditeur")

        # Si erreurs de validation, afficher les messages
        all_errors = lover_errors + sender_errors
        if all_errors:
            for error in all_errors:
                flash(error, "error")
            # Conserver les valeurs saisies pour correction
            lover_name = lover_name_raw[:50]
            sender_name = sender_name_raw[:50] or "Djochrist"
        else:
            # Tentative de chargement et personnalisation des messages
            try:
                raw_messages = load_messages()
                if not raw_messages:
                    flash("Erreur : Impossible de charger les messages.", "error")
                else:
                    messages = personalize_messages(raw_messages, lover_name, sender_name)
            except Exception as e:
                flash("Erreur lors du traitement des messages.", "error")
                messages = []

    # Rendu du template avec les données contextuelles
    return render_template(
        "index.html",
        messages=messages,
        lover_name=lover_name,
        sender_name=sender_name
    )
