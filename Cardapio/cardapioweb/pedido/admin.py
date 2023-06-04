from django.contrib import admin
from .models import Carrinho, ItemCarrinho, Pedido, ItemPedido
# Register your models here.

admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
