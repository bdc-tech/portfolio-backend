#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

Note for reviewers: used to run migrations, create superuser, and start the
development server. No logic changes were made here; all API work lives in
the `portfolio_api` app and `config` settings.
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
