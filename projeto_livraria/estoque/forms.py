from django import forms
from .models import Livro, Cliente, Vendedor, Login

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'quantidade_em_estoque', 'valor', 'origem', 'categoria']


class ClienteCreationForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'password','nome', 'cpf', 'isflamengo', 'onePiece', 'endereco']


class VendedorCreationForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['username','password','nome', 'cpf']

class LoginForm(forms.ModelForm):
    model = Login
    fields = ['username', 'password']