from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from produto.models import Produto
from cliente.models import Cliente
from .models import Carrinho, ItemCarrinho, Pedido, ItemPedido

@login_required
def carrinho(request):

    cliente = Cliente.objects.get(user=request.user)
    carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)
    
    context = {
            'carrinho': carrinho,
            # 'produtos_url': reverse('produto:produtos'),
            'username': request.user
        }
    
    return render(request, 'carrinho/carrinho.html', context) 

@login_required
def remover_item_carrinho(request, item_id):
    ItemCarrinho.objects.get(id=item_id).delete()
    return redirect('/pedido/carrinho')

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
        total = float(quantidade * preco)

        item = ItemCarrinho(
            carrinho = carrinho, 
            produto = produto,
            quantidade = quantidade,
            valor = preco,
            total = total
        )
        item.save()    
        carrinho.save()        
                            
    return redirect('/pedido/carrinho')

@login_required
def mostrar_pedido(request, pedido_id):

    pedido = Pedido.objects.get(id=pedido_id)
    context = {
            'pedido': pedido,
            'username': request.user
        }
    
    return render(request, 'pedido/pedido.html', context)

@login_required
def criar_pedido(request, carrinho_id):

    if request.method == 'POST':
        observacao = request.POST.get('observacao')
        carrinho = Carrinho.objects.get(id=carrinho_id)
        
        pedido = _novo_pedido(carrinho)
        carrinho.delete()

        return redirect(f"/pedido/{pedido.id}")
    else:
        return redirect('/pedido/carrinho')

def _novo_pedido(carrinho) -> Pedido:

    pedido = Pedido(cliente=carrinho.cliente)
    pedido.save()
    total: float = 0

    for item_carrinho in carrinho.itens.all():
        item_pedido = ItemPedido(
            produto=item_carrinho.produto,
            quantidade=item_carrinho.quantidade,
            total = float(item_carrinho.quantidade * item_carrinho.produto.preco),
            pedido=pedido,
        )
        item_pedido.save()
        total += item_pedido.total

    pedido = Pedido.objects.get(id=pedido.id)
    pedido.total = total
    pedido.save()
    return pedido


