from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import  Profile
from . forms import  ProfileForm

# Create your views here.
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