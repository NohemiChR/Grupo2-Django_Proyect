# Post/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('create/', views.post_create, name='post_create'),
    # Ruta para agregar reacciones a posts
    path('post/<int:post_id>/react/', views.post_react, name='post_react'),
    path('post/<int:post_id>', views.get_post, name='get_post'),
    path('post/<int:post_id>/coment/', views.post_coment, name='post_coment'),
    # Ruta para agregar reacciones a comentarios
    # path('coment/<int:coment_id>/react/', views.add_reaction, name='add_reaction_coment'),
    # # Agrega aquí otras rutas de la aplicación
]
