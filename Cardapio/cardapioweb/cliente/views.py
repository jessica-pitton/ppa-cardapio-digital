from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cliente

def pagina_sucesso(request):
    return render(request, 'cliente/pagina_sucesso.html')
