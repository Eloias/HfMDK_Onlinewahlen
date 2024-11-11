# local_settings.py
import logging

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
URL_HOST = "http://192.168.0.169:8000"
SECURE_URL_HOST = "http://192.168.0.169:8000"  # Ihre lokale IP

# Für Entwicklung
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False

HELIOS_VOTERS_UPLOAD = True  # Stellen Sie sicher, dass dies auf True gesetzt ist
HELIOS_VOTERS_EMAIL = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.169', '192.168.0.169']  # Ihre IP eintragen


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.core.mail': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'helios': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Email debug settings (temporär)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_DEBUG = True
