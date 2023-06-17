from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import ClienteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = ClienteForm(request.POST)
        if form_usuario.is_valid():
            user, cliente = form_usuario.save()

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect("/usuario/login")
        else:
            print(form_usuario.errors)
    else:
        form_usuario = ClienteForm()
        
    return render(request, 'usuario/cadastro.html', {'form_usuario': form_usuario})


def index(request):
    return render(request, '/usuario/login', {'username': request.user})

    
def realizar_login(request):
       

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            next = request.GET.get('next')
           
            if next is None:
                next = ''
            
            return redirect(next)
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuario/login.html', {'form_login': form_login})

def logout_user(request):
    logout(request)
    return redirect('login')
    
    