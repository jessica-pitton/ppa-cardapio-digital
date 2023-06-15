from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from produto.models import Produto
from cliente.models import Cliente
from .models import Carrinho, ItemCarrinho

@login_required
def adicionar_carrinho(request):
   
    if request.method == 'POST':
        cliente = Cliente.objects.get(user=request.user)
        carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)        
        
        if created:
            carrinho.cliente = cliente
        
        quantidade = int(request.POST.get('quantidade'))
        produto = Produto.objects.get(id=int(request.POST.get('produto_id')))
        preco = produto.preco

        item = ItemCarrinho(
            carrinho = carrinho, 
            produto = produto,
            quantidade = quantidade,
            valor = preco
        )
        item.save()    
        carrinho.save()        
        
        context = {
            'carrinho': carrinho,
            # 'produtos_url': reverse('produto:produtos'),
            'username': request.user
        }
    
        return render(request, 'carrinho/carrinho.html', context)        
    else:
        return redirect('pagina_sucesso')


    return render(request, 'cliente/novo.html', {'form': form})
