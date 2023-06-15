import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'  # Geheimer Schlüssel für die Session-Verschlüsselung
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///my_blog.db'  # Datenbank-URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deaktiviert die SQLAlchemy-Änderungsverfolgung
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_blog.db'
