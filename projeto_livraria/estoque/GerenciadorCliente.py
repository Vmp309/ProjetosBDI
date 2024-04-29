from .models import Cliente

class GerenciadorCliente:
    @classmethod
    def listar_Cliente(cls):
        return Cliente.objects.all()

    @classmethod
    def cadastrar(cls, nome, cpf, isflamengo, onePiece,endereco):
        cliente = Cliente(nome=nome, cpf=cpf, isflamengo=isflamengo,onePiece=onePiece,endereco=endereco)
        cliente.save()
        return cliente

    @classmethod
    def obter_Cliente(cls, pk):
        return Cliente.objects.get(pk=pk)

    @classmethod
    def atualizar_Cliente(cls,id, nome, cpf, isflamengo, onePiece,endereco):
        cliente = Cliente.objects.get(pk=id)
        cliente.nome = nome
        cliente.cpf = cpf
        cliente.isflamengo = isflamengo
        cliente.onePiece = onePiece
        cliente.endereco = endereco
        
        cliente.save()
        return cliente

    @classmethod
    def deletar_Cliente(cls, id):
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()