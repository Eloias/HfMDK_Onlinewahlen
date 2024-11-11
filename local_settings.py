# local_settings.py

DEBUG = True  # Nur für Entwicklung!

# Datenbank-Einstellungen
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helios',
        'USER': 'eloias',
        'PASSWORD': 'IhrNeuesPasswort',  # Das Passwort, das Sie für PostgreSQL gesetzt haben
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Geheimer Schlüssel (nicht ändern - wurde sicher generiert)
SECRET_KEY = 'TR6v3XQx6kdBgwR-P9Jr437_CyOXH-gRRswb-UxXS9AzjEfT3HePtX5IfebkBxdQ'

# E-Mail-Einstellungen für Entwicklung
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Basis-URL Ihrer Installation
URL_HOST = "http://localhost:8000"

# Für Entwicklung
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False

HELIOS_VOTERS_UPLOAD = True  # Stellen Sie sicher, dass dies auf True gesetzt ist
HELIOS_VOTERS_EMAIL = True
