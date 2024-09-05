from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # Utilizamos el modelo integrado User
from django.contrib.auth import login, authenticate, logout
from .models import Task, Profile
from .forms import TaskForm, ProfileForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")

def create_account(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        print(request.POST)
        try:
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                profile = Profile.objects.create(user=user)
                profile.save()
                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "signup.html",
                    {"error": "Las contraseñas no coinciden"},
                )
        except:
            return render(
                request,
                "signup.html",
                {"error": "El usuario ya existe"},
            )

def session(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "El username o password es incorrecto",
                },
            )
        login(request, user)
        return redirect("home")


def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()  # Obtiene todas las tareas de la BD
        return render(request, "home.html", {"tasks": tasks})
    return redirect("index")
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, "profile.html", {"profile": profile})

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request._files, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
        return render(request, "edit_profile.html", {"form": form})
def create_task(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "create_task.html", {"form": TaskForm})
        else:
            try:
                print(request.POST)
                form = TaskForm(
                    request.POST
                )  # Crear el formulario con los datos enviados
                if form.is_valid():
                    nuevo_task = form.save(
                        commit=False
                    )  # Obtener los datos de ese form
                    nuevo_task.user = request.user
                    nuevo_task.save()
                    return redirect("home")
            except:
                return render(
                    request,
                    "create_task.html",
                    {"form": TaskForm, "error": "No se pudo crear la tarea"},
                )

    redirect("login")
def delete_session(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

    return redirect("index")
