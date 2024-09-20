# Post/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('create/', views.post_create, name='post_create'),
    # Ruta para agregar reacciones a posts
    path('post/<int:post_id>/react/', views.post_react, name='post_react'),
    # Ruta para agregar reacciones a comentarios
    # path('coment/<int:coment_id>/react/', views.add_reaction, name='add_reaction_coment'),
    # # Agrega aquí otras rutas de la aplicación
]
