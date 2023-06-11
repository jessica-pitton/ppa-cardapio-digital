from django.shortcuts import render
from django.urls import reverse
from .models import Produto

def listar_produtos(request):

    produtos = Produto.objects.all()
    adicionar_carrinho_url = reverse('pedidos:adicionar_carrinho')
    context = {
        'produtos': produtos,
        'adicionar_carrinho_url': adicionar_carrinho_url
    }
    
    return render(request, 'produto/produtos.html', context)
