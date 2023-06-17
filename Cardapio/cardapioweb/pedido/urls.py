from django.urls import path

from . import views

app_name = 'pedido'


urlpatterns = [
    path('adicionar', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('carrinho/<int:item_id>/remover', views.remover_item_carrinho, name='remover_item_carrinho'),
    path('carrinho/<int:carrinho_id>', views.criar_pedido, name='criar_pedido'),
    path('<int:pedido_id>', views.mostrar_pedido, name='mostrar_pedido'),
    
]
