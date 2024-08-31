from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     # Agrega aquí los campos adicionales que desees

#     def __str__(self):
#         return self.user.username
