from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render,redirect
from .models import Post, Coment, Reaction
from .forms import PostForm
from django.contrib.auth.decorators import login_required

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

@login_required
def add_reaction(request, post_id=None, coment_id=None):
    reaction_type = request.POST.get('reaction_type')
    user = request.user
    
    # Si es un post
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        reaction, created = Reaction.objects.get_or_create(user=user, post=post)
        
        # Actualizar o crear reacción
        reaction.reaction_type = reaction_type
        reaction.save()
        
    # Si es un comentario
    elif coment_id:
        coment = get_object_or_404(Coment, id=coment_id)
        reaction, created = Reaction.objects.get_or_create(user=user, coment=coment)
        
        # Actualizar o crear reacción
        reaction.reaction_type = reaction_type
        reaction.save()
    
    return redirect('home')