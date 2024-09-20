from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import  Profile
from . forms import  ProfileForm
from .forms import PostForm
from Post.models import Post 

# Create your views here.
def profile(request):
    user = request.user # Obtén el usuario autenticado
    profile = get_object_or_404(Profile, user=request.user) #Obtén el perfil del usuario
     # Filtra los posts para obtener solo los del usuario autenticado
    posts = Post.objects.filter(user=user)  # Solo los posts del usuario actual
    return render(request, "profile.html", {"profile": profile,'posts': posts})

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
        return render(request, "edit_profile.html", {"form": form})
def post_create2(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Crear una instancia del formulario con los datos del POST
        if form.is_valid():  # Verificar si el formulario es válido
            post = form.save(commit=False)  # No guardar en la base de datos todavía
            post.user = request.user  # Asociar el post al usuario autenticado
            post.save()  # Ahora sí guardar el post en la base de datos
            print("Redirigiendo a profile")  # Añadir una impresión para depuración
            return redirect('profile')  # Redirigir a la página de inicio después de guardar
    else:
        form = PostForm()  # Si no es un POST, crear un formulario vacío

    return render(request, 'create_post.html', {'form': form})  # Renderizar la plantilla con el formulario
