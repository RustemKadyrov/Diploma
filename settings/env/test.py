from settings.base import *  # noqa


# ------------------------------------------------
#
DEBUG = True
WSGI_APPLICATION = 'deploy.test.wsgi.application'

# ------------------------------------------------
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_test.sqlite3',
    }
}
ALLOWED_HOSTS = []
INTERNAL_IPS = []

# ------------------------------------------------
#
INSTALLED_APPS += [
    'debug_toolbar'
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
