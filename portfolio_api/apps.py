"""App configuration for the `portfolio_api` Django app.

This app contains models, serializers, views, admin, and tests for the
portfolio API (Projects, Skills, Contact). Recent edits added JWT auth,
OpenAPI docs, and example tests.
"""

from django.apps import AppConfig


class PortfolioApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_api'
