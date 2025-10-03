"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# drf-spectacular views for OpenAPI schema + interactive docs
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# SimpleJWT views for token obtain/refresh
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),

    # OpenAPI JSON schema endpoint (machine-readable)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI - interactive API docs for humans (good for demos)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc - another human-friendly API documentation UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Include the portfolio app API under /api/
    path('api/', include('portfolio_api.urls')),

    # Authentication endpoints (SimpleJWT)
    # - POST to token/ with {"username":"...","password":"..."} to obtain access & refresh tokens
    # - POST to token/refresh/ with {"refresh":"..."} to obtain a new access token
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# CURL examples (commented):
# 1) Obtain tokens
# curl -X POST http://127.0.0.1:8000/api/auth/token/ -H "Content-Type: application/json" -d '{"username":"admin","password":"pass"}'
# Response contains access and refresh tokens.
# 2) Call whoami with an access token
# curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/api/auth/whoami/
