import pytest


"""Authentication tests verifying JWT flows and protected endpoints.

These tests ensure the SimpleJWT endpoints and token-protected views
behave as expected.
"""


@pytest.mark.django_db
def test_obtain_token_and_whoami(client, django_user_model):
    username = 'testuser'
    password = 'testpass123'
    email = 'test@example.com'

    # Create a user
    user = django_user_model.objects.create_user(username=username, password=password, email=email)

    # Obtain token
    resp = client.post('/api/auth/token/', {'username': username, 'password': password}, content_type='application/json')
    assert resp.status_code == 200
    tokens = resp.json()
    assert 'access' in tokens and 'refresh' in tokens

    access = tokens['access']

    # Call whoami with Authorization header
    resp2 = client.get('/api/whoami/', HTTP_AUTHORIZATION=f'Bearer {access}')
    assert resp2.status_code == 200
    data = resp2.json()
    assert data.get('email') == email
