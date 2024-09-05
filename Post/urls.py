# Post/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('create/', views.post_create, name='post_create'),
    # Agrega aquí otras rutas de la aplicación
]
