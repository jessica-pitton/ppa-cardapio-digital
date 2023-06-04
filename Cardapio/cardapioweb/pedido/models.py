from django.db import models
from django.utils import timezone
from produto.models import Produto
from cliente.models import Cliente


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"pedido={self.id}, data={self.criacao}, total={self.total}, cliente={self.cliente}"


class ItemCarrinho(models.Model):
    produto = models.ManyToManyField(Produto)
    quantidade = models.IntegerField()
    observacao = models.TextField()
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"item={self.id}, produto={self.produto}, quantidade={self.quantidade}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"pedido={self.id}, data={self.criacao}, total={self.total}, cliente={self.cliente}"

class ItemPedido(models.Model):
    produto = models.ManyToManyField(Produto)
    quantidade = models.IntegerField()
    observacao = models.TextField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"item={self.id}, produto={self.produto}, quantidade={self.quantidade}"