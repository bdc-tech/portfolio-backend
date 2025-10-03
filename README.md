# Branden Portfolio API

Backend for my portfolio: Projects/Skills CRUD, JWT auth, Swagger docs, seed data.

Overview
--------
This Django + Django REST Framework project powers a portfolio backend exposing
Projects, Skills, and a Contact endpoint. It includes JWT authentication
(SimpleJWT), CORS settings for local development, and OpenAPI docs generated
by drf-spectacular (Swagger/ReDoc).

ASCII Architecture
------------------

Frontend (React/Vite)  <-- CORS -->  This Django API
																	|
																	+-- /api/projects/   (projects ViewSet)
																	+-- /api/skills/     (skills ViewSet)
																	+-- /api/contact/    (create-only)
																	+-- /api/whoami/     (protected)
																	+-- /api/auth/token/ (JWT obtain)
																	+-- /api/auth/token/refresh/ (JWT refresh)
																	+-- /api/schema/     (OpenAPI JSON)
																	+-- /api/docs/       (Swagger UI)
																	+-- /api/redoc/      (ReDoc UI)

Quickstart (Windows PowerShell)
-------------------------------
1. Create and activate a virtualenv (PowerShell):

```powershell
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
# or, if you don't have requirements.txt installed
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers drf-spectacular pytest pytest-django
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. (Optional) Seed demo data using the Django shell or loaddata if fixtures exist:

```powershell
python manage.py shell
from portfolio_api import models
models.Skill.objects.create(name='Django', level='Advanced')
models.Project.objects.create(name='Demo', description='Demo project')
exit()

# or, if a fixture exists
python manage.py loaddata portfolio_api/fixtures/seed.json
```

5. Run the development server:

```powershell
python manage.py runserver
# Visit http://127.0.0.1:8000/api/docs/ for Swagger UI
```

Swagger / OpenAPI
------------------
- OpenAPI JSON: http://127.0.0.1:8000/api/schema/
- Swagger UI:    http://127.0.0.1:8000/api/docs/
- ReDoc:         http://127.0.0.1:8000/api/redoc/

JWT examples
------------
Obtain tokens (curl):

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
	-H "Content-Type: application/json" \
	-d '{"username":"<username>","password":"<password>"}'
```

Call protected whoami endpoint:

```bash
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/api/whoami/
```

Security notes
--------------
- Don't store long-lived tokens in localStorage in production. Prefer
	secure cookies for refresh tokens and short-lived in-memory access tokens.
- Restrict CORS origins in production.

Testing
-------
Run tests with pytest or Django's test runner:

```powershell
pytest
# or
python manage.py test
```

If anything in this README looks off, let me know which version you'd like
to keep (the short header or the longer docs) and I can adjust accordingly.
