"""Ecell_task8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import ProtectedView
from .views import BioView
from .views import EduView
from .views import PlaceView
from .views import ExtraView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('biodata', BioView.as_view(), name='biodata'),
    path('education', EduView.as_view(), name='education'),
    path('places', PlaceView.as_view(), name='places'),
    path('extra', ExtraView.as_view(), name='extra'),
]

urlpatterns += staticfiles_urlpatterns()