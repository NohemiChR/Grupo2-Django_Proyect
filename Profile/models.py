from django.db import models
from django.contrib.auth.models import User  # Django ya lo tiene implementado


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    cover_photo = models.ImageField(upload_to="cover_photos/", blank=True, null=True)



# Create your models here.
