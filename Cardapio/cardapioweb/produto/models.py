from django.db import models
from django.utils import timezone

class ImagemProduto(models.Model):
    imagem = models.ImageField(upload_to='imagens_produto/')

    def __str__(self) -> str:
        return str(self.imagem)

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField()
    quantidade = models.IntegerField()
    imagens = models.ManyToManyField(ImagemProduto, blank=True)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)

    def __str__(self) -> str:
        return f"codigo={self.codigo}, nome={self.nome}, quantidade={self.quantidade}" 
    