import os
from pathlib import Path

class Config:
    """
    Base configuration class for the Flask application.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    WTF_CSRF_ENABLED = True

    # File upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size
    UPLOAD_FOLDER = Path(__file__).parent.parent / 'uploads'
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'aac', 'ogg', 'webm', 'mp4', 'avi', 'mov'}

    # Video generation settings
    VIDEO_FPS = 24
    VIDEO_CODEC = 'libx264'
    AUDIO_CODEC = 'aac'
    VIDEO_WIDTH = 1920
    VIDEO_HEIGHT = 1080

    # Additional configurations can be added here in the future


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

    @property
    def SECRET_KEY(self):
        key = os.environ.get('SECRET_KEY')
        if not key:
            raise ValueError("SECRET_KEY environment variable must be set in production")
        return key
