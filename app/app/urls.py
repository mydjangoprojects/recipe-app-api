"""app URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from user.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recipe/', include('recipe.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls'),
         name='rest_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
