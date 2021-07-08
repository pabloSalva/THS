"""api_cheap_heat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings

from allauth.account.views import ConfirmEmailView
import api_login.urls

# from api_artefactos.views import UserCreate
from .views import legal


urlpatterns = [
    path('admin/', admin.site.urls),

    # Legales
    path('politicaprivacidad', legal, name='legales'),
    # End Points
    path('', include('api_artefactos.urls')),
    path('', include('api_entidades.urls')),
    #path('crearUsuario/', UserCreate.as_view(), name='crear_usuario'),

    # Autenticación social
    path('api/auth/oauth/', include('rest_framework_social_oauth2.urls')),

    # path('Login', include('social_django.urls', namespace='social')),
    path('auth/', include('rest_framework_social_oauth2.urls')),

    # validacion por mail
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('aut/', include(api_login.urls)),
    path('autent/', include('authentication.urls')),
    
]
