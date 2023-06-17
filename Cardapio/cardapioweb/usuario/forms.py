from django import forms
from django.contrib.auth.forms import UserCreationForm
from cliente.models import Cliente

class ClienteForm(UserCreationForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu cpf'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(xx) xxxxx-xxxx'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Digite seu MAILL'

    def save(self, commit=True):
        user = super().save(commit=True)

        nome = self.cleaned_data['nome']
        email = user.username
        cpf = self.cleaned_data['cpf']
        celular = self.cleaned_data['celular']

        cliente = Cliente(
            nome=nome,
            email=email,
            cpf=cpf,
            celular=celular,
            user=user
        )
        
        cliente.save()

        return user, cliente 