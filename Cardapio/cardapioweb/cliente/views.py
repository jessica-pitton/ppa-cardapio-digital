from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cliente
from .forms import ClienteForm


def pagina_sucesso(request):
    return render(request, 'cliente/pagina_sucesso.html')


def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')
    else:
        form = ClienteForm()

    return render(request, 'cliente', {'form': form})
