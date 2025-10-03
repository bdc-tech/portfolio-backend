"""WSGI config for this Django project.

Exposes the WSGI `application` used by WSGI servers. Core API code is in
`portfolio_api` and configuration is in `config/settings.py`.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
