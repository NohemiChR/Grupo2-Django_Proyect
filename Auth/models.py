

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     # Agrega aquí los campos adicionales que desees

#     def __str__(self):
#         return self.user.username
# ==============================================================
# LO QUE HIZO CHAT GPT 
from django.db import models
from django.contrib.auth.models import User  # Django ya lo tiene implementado


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank=True)
    # relacionamos con el usuario | si en caso el usuario se borra, pues se borran sus tareas
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)





# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
#     biography = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Post by {self.user.username} on {self.created_at}"

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Comment by {self.user.username} on {self.post.id}"

# class Reaction(models.Model):
#     REACTION_TYPES = [
#         ('like', 'Like'),
#         ('love', 'Love'),
#         ('angry', 'Angry'),
#         ('sad', 'Sad'),
#         ('wow', 'Wow'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions', blank=True, null=True)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reactions', blank=True, null=True)
#     reaction_type = models.CharField(max_length=10, choices=REACTION_TYPES)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Reaction by {self.user.username} on {self.post.id if self.post else self.comment.id}"

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     read_at = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return f"Message from {self.sender.username} to {self.receiver.username}"

# class Friendship(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('accepted', 'Accepted'),
#         ('rejected', 'Rejected'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships')
#     friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_set')
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Friendship between {self.user.username} and {self.friend.username}"

# class Notification(models.Model):
#     NOTIFICATION_TYPES = [
#         ('message', 'Message'),
#         ('friend_request', 'Friend Request'),
#         ('comment', 'Comment'),
#         ('reaction', 'Reaction'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
#     type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
#     related_id = models.PositiveIntegerField()  # ID of the related object
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Notification for {self.user.username} of type {self.type}"
