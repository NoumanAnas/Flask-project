# App configuration

import os

class Config:
    # Flask settings
    # SECRET_KEY = 'your_secret_key'  # Change this to a random string for security

    # Database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use a different database URL based on your database choice
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Flask-Mail settings (if using email)
    # MAIL_SERVER = 'smtp.example.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USE_SSL = False
    # MAIL_USERNAME = 'your_email@example.com'
    # MAIL_PASSWORD = 'your_email_password'
    # MAIL_DEFAULT_SENDER = 'your_email@example.com'

    # Flask-Login settings
    LOGIN_DISABLED = False  # Set to True if you want to disable user authentication temporarily

    # Other settings
    DEBUG = True  # Set to False in production
    TESTING = False
    CSRF_ENABLED = True
    # WTF_CSRF_SECRET_KEY = 'your_wtf_csrf_secret_key'  # Change this to a random string for security

    # Flask-Migrate settings
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use the same database URI as above
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    # Add other configuration options as needed