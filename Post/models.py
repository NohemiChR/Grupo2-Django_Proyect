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

class Coment(models.Model):
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Reaction(models.Model):
    REACTION_TYPES = [
        ('like', 'Me gusta'),
        ('love', 'Me encanta'),
        ('care', 'Me importa'),
        ('haha', 'Me divierte'),
        ('wow', 'Me sorprende'),
        ('sad', 'Me entristece'),
        ('angry', 'Me enoja'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que da la reacción
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)  # Relación opcional con Post
    coment = models.ForeignKey(Coment, null=True, blank=True, on_delete=models.CASCADE)  # Relación opcional con Comentario
    reaction_type = models.CharField(max_length=10, choices=REACTION_TYPES)  # Tipo de reacción
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        
        return self.get_reaction_type_display()

    class Meta:
        unique_together = ('user', 'post', 'coment')  # Evita que un usuario reaccione al mismo post o comentario más de una vez