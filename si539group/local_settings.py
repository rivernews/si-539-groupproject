from .settings import BASE_DIR
import os

print('We are at local...')

DEBUG = True
TEMPLATE_DEBUG = True

# use default SQLite DATABASES
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}