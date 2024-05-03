from django.db import models


# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    quantidade_em_estoque = models.PositiveIntegerField()
    valor = models.PositiveIntegerField(default=0)
    origem = models.CharField(max_length=100, default='Mari')
    categoria = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    username = models.CharField(max_length=20, default='', primary_key=True)
    password = models.CharField(max_length=20, default='')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    isflamengo = models.BooleanField()
    onePiece = models.BooleanField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.pk


class Vendedor(models.Model):
    username = models.CharField(max_length=20, default='', primary_key=True)
    password = models.CharField(max_length=20, default='')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.pk


class Venda(models.Model):
    valorTotal = models.PositiveIntegerField()
    valorDesconto = models.PositiveIntegerField()
    formaPagamento = models.CharField(max_length=7)
    pagConcluido = models.BooleanField()
    cliente = models.ManyToManyField(Cliente)
    livros = models.ExpressionList({})
    vendedor = models.ManyToManyField(Vendedor)

    def __str__(self):
        return self.pk


class Login(models.Model):
    username = models.CharField(max_length=20, default='', primary_key=True)
    password = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.pk
