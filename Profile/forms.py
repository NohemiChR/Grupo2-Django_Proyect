from django import forms
from django.forms import ModelForm
from .models import  Profile
from Post.models import Post 


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["biography", "avatar","cover_photo"]
        widgets = {
            "biography": forms.Textarea(attrs={"class": "form-control bg-primary"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
           "cover_photo": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }

# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['description', 'file']
    
#     def clean_file(self):
#         #Este método se llama automáticamente cuando se valida el formulario, específicamente para el campo file.
#         file = self.cleaned_data.get('file')
#         description = self.cleaned_data.get('description')
        
#         if file:
#             # Comprobar si es un video o una imagen
#             if file.name.endswith(('.mp4', '.mov')) and description:
#                 raise forms.ValidationError("No puedes subir una imagen y un video a la vez.")
        
#         return file

#     def clean(self):
#         cleaned_data = super().clean()
#         description = cleaned_data.get('description')
#         file = cleaned_data.get('file')

#         # Validar que al menos uno de los campos esté lleno
#         if not description and not file:
#             raise forms.ValidationError("Debes ingresar texto o subir un archivo (imagen o video).")
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'file']  # Los campos que se editarán
