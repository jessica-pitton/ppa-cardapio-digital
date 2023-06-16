from django.db import models
from django.utils import timezone
from produto.models import Produto
from cliente.models import Cliente
from decimal import Decimal


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f"id={self.id}, data={self.criacao}, total={self.total}, cliente={self.cliente}, itens={self.itens}"


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="itens", null=True)

    def __str__(self) -> str:
        return f"item={self.id}, quantidade={self.quantidade}, produto={self.produto}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, default="Pendente")
    observacao = models.TextField(null=True)

    def adiciona_ao_total(self, valor):
        self.total += float(valor)
         
    def __str__(self) -> str:
        return f"pedido={self.id}, data={self.criacao}, total={self.total}, cliente={self.cliente}"

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens", null=True)

    def __str__(self) -> str:
        return f"item={self.id}, produto={self.produto}, quantidade={self.quantidade}"