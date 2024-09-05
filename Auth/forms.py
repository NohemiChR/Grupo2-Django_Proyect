from django import forms
from django.forms import ModelForm
from .models import Task, Profile


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "important": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["biography", "avatar"]
        widgets = {
            "biography": forms.Textarea(attrs={"class": "form-control bg-primary"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }
