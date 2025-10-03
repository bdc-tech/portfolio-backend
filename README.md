# portfolio-backend
Backend for my portfolio: Projects/Skills CRUD, JWT auth, Swagger docs, seed data. Django/DRF API with JWT auth and Swagger; serves projects, skills, and contact.

```powershell
Set-Content -Encoding UTF8 -Path "README.md" -Value @'
# Branden Portfolio API

Django/DRF backend powering my portfolio (Projects, Skills, Contact) with JWT auth and Swagger docs.

## Stack
- **Django** + **Django REST Framework**
- **SimpleJWT** (auth), **drf-spectacular** (OpenAPI/Swagger)
- **CORS** for local React dev
- **SQLite** for dev (Postgres in prod later)

## Live Docs (local)
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- OpenAPI JSON: `http://127.0.0.1:8000/api/schema/`

## Quickstart (Windows)
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # or install deps listed below
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata portfolio_api/fixtures/seed.json
python manage.py runserver
