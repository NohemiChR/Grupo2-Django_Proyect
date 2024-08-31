from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")

def create_account(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        print(request.POST)
        try:
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
                )
        except:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "El usuario ya existe"},
            )

def session(request):
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
    return render(request, "logout.html")

def home(request):
    return render(request, "home.html")