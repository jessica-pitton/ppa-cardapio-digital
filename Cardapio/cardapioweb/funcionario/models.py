from django.db import models
from django.utils import timezone

class Cargo(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"nome={self.nome}"

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)

    def __str__(self) -> str:
        return f"id={self.id}, nome={self.nome}, cargo={self.cargo}"
