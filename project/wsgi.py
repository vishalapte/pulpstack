"""
WSGI config for pulpstack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

dotenv.load_dotenv(
    os.path.join(settings.BASE_DIR, 'project/.env')
)

application = get_wsgi_application()
