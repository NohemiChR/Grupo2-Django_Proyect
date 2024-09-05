from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Asociar el post al usuario autenticado
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})