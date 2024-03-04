from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.utils import timezone
from .models import Post
from usuarios.forms import ProfileForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'plataforma/index.html')
    else:
        return redirect('/home/')

@login_required(login_url='/user/login/')
def home(request):
    posts = Post.objects.all()
    return render(request, 'plataforma/home.html', {'posts': posts})

@login_required(login_url='/user/login/')
def new_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'plataforma/new_post.html', {'form': form})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')

@login_required(login_url='/user/login/')
def detail_post(request, id):
    post = get_object_or_404(Post,id=id)
    return render(request, "plataforma/detail_post.html", {'post': post})


@login_required(login_url='/user/login/')
def perfil(request, nickname):
    
    current_user = User.objects.get(user_profile__nickname=nickname)
    
    posts = Post.objects.filter(author=current_user)

    if hasattr(current_user, 'user_profile'):
        return render(request, "plataforma/meu_perfil.html",{'posts': posts, 'user':current_user.user_profile})
    else:
        return redirect('edit_perfil')