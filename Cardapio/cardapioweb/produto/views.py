from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse
from .models import Produto

def produtos(request):

    produtos = Produto.objects.all()
    adicionar_carrinho_url = reverse('pedido:adicionar_carrinho')
    context = {
        'produtos': produtos,
        'adicionar_carrinho_url': adicionar_carrinho_url,
    }

    if request.user.is_authenticated:
        try:
            cliente = request.user.cliente
            context['username'] = cliente.nome
        except:
            logout(request)
    
    return render(request, 'produto/produtos.html', context)
