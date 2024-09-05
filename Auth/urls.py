# Auth/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.create_account, name="signup"),
    path("login/", views.session, name="login"),
    path("logout/", views.delete_session, name="logout"),
    # path("home/", views.home, name="home"),
    # Agrega aquí otras rutas de la aplicación
]
