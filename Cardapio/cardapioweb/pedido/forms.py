from django import forms
from .models import Produto

class ItemCarrinhoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['id', 'quantidade', 'observacao']
    