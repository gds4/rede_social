from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django
from django.contrib.auth import authenticate

from usuarios.forms import ProfileForm
from plataforma.models import Post

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Já existe usuario com este username")


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login_django(request, user)

        return redirect("/user/perfil/")

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        login_django(request, user)
        return redirect('/home/')
    else:
        return HttpResponse("usuario ou senha incorretos.")


def edit_perfil(request):
    current_user = request.user
    form = ProfileForm()
    if request.method == "GET":
        return render(request, "usuarios/editar_perfil.html", {'form': form})
    else:
        form = ProfileForm(request.POST, request.FILES)
        
        if form.is_valid:
            #CRIA UMA INSTANCIA DO FORMULARIO QUE PODE SER MODIFICADA ANTES DE SER INSERIDA AO BANCO DE DADOS
            profile = form.save(commit=False)
            profile.profile_user = current_user
            #SALVA OS DADOS MODIFICADOS NO BD
            profile.save()
            return redirect('home')
