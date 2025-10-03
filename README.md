# Branden Portfolio API

Overview
--------
This is a small Django REST Framework backend for a personal portfolio. It
provides endpoints to manage Projects and Skills, receive Contact messages,
and includes JWT authentication (SimpleJWT), CORS configuration, and
OpenAPI schema generation with drf-spectacular.

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

Setup (Windows PowerShell)
---------------------------
Commands assume you're in the project root (where `manage.py` lives).

1. Create and activate a virtualenv (PowerShell):

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

2. Install dependencies (create `requirements.txt` or install manually):

```powershell
# If you have a requirements.txt
pip install -r requirements.txt
# Or install the essentials manually
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers drf-spectacular pytest
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. (Optional) Seed minimal demo data using the Django shell:

```powershell
python manage.py shell
# then in the shell:
from portfolio_api import models
models.Skill.objects.create(name='Django', level='Advanced')
models.Project.objects.create(name='Demo', description='Demo project')
exit()
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

JWT (SimpleJWT) quick examples
------------------------------
1) Obtain tokens (curl):

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"<username>","password":"<password>"}'
```

PowerShell (Invoke-RestMethod):

```powershell
$body = @{ username = '<username>'; password = '<password>' } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/auth/token/ -Method Post -Body $body -ContentType 'application/json'
```

2) Call protected whoami endpoint with access token:

```bash
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/api/whoami/
```

PowerShell:

```powershell
$headers = @{ Authorization = "Bearer $env:ACCESS_TOKEN" }
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/whoami/ -Headers $headers
```

Security notes
--------------
- JWT storage: Keep access tokens in memory (or short-lived storage) and
  refresh tokens in secure HTTP-only cookies when possible. Never store
  long-lived tokens in localStorage for production apps.
- CORS: Current settings allow localhost:3000 and 127.0.0.1:3000 for
  front-end development. In production, restrict `CORS_ALLOWED_ORIGINS` to
  trusted domains only.
- HTTPS: Always use HTTPS in production to protect Authorization headers.

Testing
-------
This repo uses Django's test framework; you can run tests with pytest if
configured.

```powershell
# Run Django tests
python manage.py test
# Or if you have pytest configured
pytest
```

Roadmap
-------
- Add pagination and filtering for `projects/` (e.g., by tag or date).
- Add per-action permissions (e.g., only staff can delete).
- Add tagging model (many-to-many) if tags become first-class.
- Add CI (GitHub Actions) and linting (flake8/ruff).

Interview Talking Points
------------------------
- Why JWT (SimpleJWT): stateless auth, easy to integrate with SPAs and mobile.
- CORS reasoning: allow only dev origins locally; tighten in production.
- Why JSONField for tags: structured data, easier queries, avoids brittle string parsing.
- Admin choices: list_display/search_fields/list_filter improve productivity
  for content editors and support staff.
- DRF permissions: `IsAuthenticatedOrReadOnly` is a sensible default for
  public read + authenticated write patterns—discuss trade-offs vs per-action
  or role-based permissions.
- Schema & docs: drf-spectacular makes schema generation and interactive
  docs (Swagger/Redoc) straightforward for interviews and client integration.

If you want, I can:
- Add a `requirements.txt` based on your virtualenv.
- Add CI and a GitHub Actions workflow to run tests + linting.
- Add more detailed PowerShell examples or a small `seed` management command.
