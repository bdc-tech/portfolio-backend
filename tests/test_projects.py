import pytest


"""Integration tests for project listing.

These tests use the Django test client provided by pytest-django to perform
HTTP-level checks against the running Django test server and database.
"""


@pytest.mark.django_db
def test_projects_list_returns_seeded_items(client):
    """Verify GET /api/projects/ returns 200 and seeded projects."""
    from portfolio_api import models

    # Seed data
    models.Project.objects.create(name='P1', description='First')
    models.Project.objects.create(name='P2', description='Second')

    resp = client.get('/api/projects/')
    assert resp.status_code == 200
    data = resp.json()
    # Expect at least two items
    assert isinstance(data, list)
    assert len(data) >= 2
