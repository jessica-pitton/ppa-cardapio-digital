from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=200, null=True)
    criacao = models.DateTimeField("data de criacão", default=timezone.now)
    alteracao = models.DateTimeField("data de alteração", default=timezone.now)
    
 
    def __str__(self) -> str:
        return "id: " + str(self.id) \
            + ", Nome: " + self.nome \
            + ", CPF: " + self.cpf \
            + ", email: " + self.email \
            + ", data criacao: " + str(self.criacao) \
            + ", data alteracao: " + str(self.alteracao)
    
