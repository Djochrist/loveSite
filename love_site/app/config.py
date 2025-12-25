class Config:
    """
    Classe de configuration de base pour l'application Flask.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = "change-me-in-production"  # À changer en production
    WTF_CSRF_ENABLED = False
    # Autres configurations futures peuvent être ajoutées ici
