from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render,redirect
from .models import Post, Coment, Reaction
from django.http import JsonResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()  # O filtra según lo que necesites
    # reactions = Reaction.objects.all()
    # Recopilamos las reacciones del usuario actual para los posts
    user_reactions = Reaction.objects.filter(user=request.user, post__in=posts)
    reactions = {reaction.post_id: reaction for reaction in user_reactions}
    print('reaction')
    # print(reaction)
    print(user_reactions)
    print(reactions.get(1))
    
    return render(request, 'home.html', {'posts': posts,'reactions_dict': reactions})




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


def post_react(request, post_id):
    print('react')
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        reaction_type = request.POST.get('reaction')
        print(reaction_type)
        # Verificamos si ya existe una reacción de este usuario para este post
        reaction, created = Reaction.objects.get_or_create(
            user=request.user,
            post=post,
        )
        
        # Actualizamos el tipo de reacción
        reaction.reaction_type = reaction_type
        reaction.save()
        print('guardada')

        return JsonResponse({'status': 'ok', 'reaction': reaction_type})

    return JsonResponse({'status': 'error'}, status=400)