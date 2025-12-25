class Config:
    """
    Base configuration class for the Flask application.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = "change-me-in-production"  # Change this in production
    WTF_CSRF_ENABLED = False
    # Additional configurations can be added here in the future
