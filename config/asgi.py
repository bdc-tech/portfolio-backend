"""ASGI config for this Django project.

This file exposes the ASGI `application` used by ASGI servers. The API
implementation is in the `portfolio_api` app; settings live in
`config/settings.py`.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
