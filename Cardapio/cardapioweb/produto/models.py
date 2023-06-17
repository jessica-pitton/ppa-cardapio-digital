from django.db import models
from django.utils import timezone


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField()
    quantidade = models.IntegerField()
    descricao = models.TextField(null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    
    def __str__(self) -> str:
        return f"codigo={self.codigo}, nome={self.nome}, quantidade={self.quantidade}" 
    

class ImagemProduto(models.Model):
    imagem = models.ImageField(upload_to='produto/static/imagens_produto/')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens', null=True)

    def __str__(self) -> str:
        return str(self.imagem)