from django import forms
from django.forms import ModelForm
from .models import  Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["biography", "avatar"]
        widgets = {
            "biography": forms.Textarea(attrs={"class": "form-control bg-primary"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }