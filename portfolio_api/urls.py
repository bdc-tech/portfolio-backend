"""API URL routing for the portfolio_api app.

Exposes:
 - /projects/  -> ProjectViewSet (CRUD)
 - /skills/    -> SkillViewSet (CRUD)
 - /contact/   -> create-only contact endpoint (POST)
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'skills', views.SkillViewSet, basename='skill')

urlpatterns = [
    # Router includes list/retrieve/create/update/delete for projects and skills
    path('', include(router.urls)),

    # Create-only contact endpoint: POST to /contact/
    path('contact/', views.contact_create, name='contact-create'),
    # Protected endpoint: returns the current authenticated user's email.
    # This demonstrates token-protected endpoints inside the app's router.
    path('whoami/', views.whoami, name='whoami'),

    # CURL examples (useful for interviews/demos):
    # 1) Obtain tokens (run against the TokenObtainPairView defined in config/urls.py)
    # curl -X POST http://127.0.0.1:8000/api/auth/token/ -H "Content-Type: application/json" -d '{"username":"admin","password":"pass"}'
    # 2) Call whoami with an access token:
    # curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/api/whoami/
]
