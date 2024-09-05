from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Post(models.Model):
    # title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # important = models.BooleanField(default=False)
    # datecompleted = models.DateTimeField(null=True, blank=True)
    # relacionamos con el usuario | si en caso el usuario se borra, pues se borran sus tareas
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="file/", blank=True, null=True)

    # def __str__(self): 
    #     return f"{self.title} - {self.user.username}" 