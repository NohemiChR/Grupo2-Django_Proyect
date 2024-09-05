from django.contrib import admin
from .models import Task, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.


# Esto permite que los campos se muestren de una manera apilada
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


# Hereda de la administración base del usuario y te permitirá editar o crear en la misma vista
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Quitamos el registro del usuario que viene por defecto
admin.site.unregister(User)

# Lo registramos de manera personalizada
admin.site.register(User, UserAdmin)

admin.site.register(Task)
# Register your models here.
