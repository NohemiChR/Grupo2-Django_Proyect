from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # Utilizamos el modelo integrado User
from django.contrib.auth import login, authenticate, logout
from Profile.models import Profile  # Cambia profile_app por el nombre real de tu app Profile


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

def delete_session(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

    return redirect("index")

    
def delete_session(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

    return redirect("index")
