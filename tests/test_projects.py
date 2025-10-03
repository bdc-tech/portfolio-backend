import pytest


@pytest.mark.django_db
def test_projects_list_returns_seeded_items(client):
    """Verify GET /api/projects/ returns 200 and seeded projects.

    This test seeds a couple of Project objects and ensures the list
    endpoint returns them. It demonstrates a simple integration test
    for DRF endpoints.
    """
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
