from django.shortcuts import render
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/produtos.html', {'produtos': produtos})
