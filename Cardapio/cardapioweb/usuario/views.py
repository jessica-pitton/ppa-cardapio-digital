from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuario/cadastro.html', {'form_usuario': form_usuario})


def index(request):
    return render(request, 'usuario/pagina_sucesso.html', {'username': request.user})

    
def logar_usuario(request):
    
    print()
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            next = request.GET.get('next')
           
            if next is None:
                next = 'index'
            
            return redirect(next)
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuario/login.html', {'form_login': form_login })

def logout_user(request):
    logout(request)
    return redirect('logar_usuario')
    
    