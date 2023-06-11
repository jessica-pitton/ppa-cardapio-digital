from django.shortcuts import render, redirect
from produto.models import Produto

def adicionar_carrinho(request):
    
    print('=====================================================================')
    
    if request.method == 'POST':
        
        produto_id = request.POST.get('produto_id')
        quantidade = request.POST.get('quantidade')
        produto = Produto.objects.get(id=produto_id)
        preco = produto.preco
        # form = ItemCarrinhoForm(request.POST)
        # if form.is_valid():
            # form.save()
        return redirect('pagina_sucesso')
    else:
        return redirect('pagina_sucesso')


    return render(request, 'cliente/novo.html', {'form': form})
