from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView


urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
]