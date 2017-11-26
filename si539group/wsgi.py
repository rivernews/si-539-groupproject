"""
WSGI config for si539group project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "si539group.settings")

application = get_wsgi_application()

# Whitenoise for heroku. See https://devcenter.heroku.com/articles/django-app-configuration#migrating-an-existing-django-project
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
