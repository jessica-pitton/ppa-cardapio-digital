from django.urls import path

from . import views

app_name = 'pedidos'


urlpatterns = [
    path('adicionar', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('carrinho/<int:item_id>/remover', views.remover_item_carrinho, name='remover_item_carrinho'),
    
]
