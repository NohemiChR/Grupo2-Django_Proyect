# Auth/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("profile/",views.profile,name="profile"),
    path("profile/edit", views.edit_profile, name="edit_profile"),
    path('post/create/', views.post_create2, name='post_create2'),
    # Agrega aquí otras rutas de la aplicación
]
