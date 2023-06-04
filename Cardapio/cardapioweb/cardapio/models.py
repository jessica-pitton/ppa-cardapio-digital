from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    
 
    def __str__(self) -> str:
        return "Nome = " + self.nome + "CPF: " + self.cpf + "ID: " + str(self.id)
