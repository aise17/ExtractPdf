"""Extract_refactor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from coreapi.auth import BasicAuthentication, AuthBase
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.views import SchemaView
from rest_framework.settings import api_settings

API_TITLE = 'API Extract Pdf'
API_DESCRIPTION = 'documentacion basada en el api Extract Pdf para apoyo a desarrolladores'


urlpatterns = [
    path('admin/', admin.site.urls),

    path('file/', include('ocr_api.urls')),
    path('contenido/', include('anuncios.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION,  authentication_classes = [],
                                    permission_classes = [], public=False))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
