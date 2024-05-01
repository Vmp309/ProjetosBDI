from .models import Vendedor

class Gerenciadorvendedor:
    @classmethod
    def listar_Vendedor(cls):
        return Vendedor.objects.all()

    @classmethod
    def cadastrar_Vendedor(cls, nome, cpf,endereco):
        vendedor = Vendedor(nome=nome, cpf=cpf,endereco=endereco)
        vendedor.save()
        return vendedor

    @classmethod
    def obter_Vendedor(cls, pk):
        return Vendedor.objects.get(pk=pk)

    @classmethod
    def atualizar_Vendedor(cls,id, nome, cpf,endereco):
        vendedor = Vendedor.objects.get(pk=id)
        vendedor.nome = nome
        vendedor.cpf = cpf
        vendedor.endereco = endereco
        
        vendedor.save()
        return vendedor

    @classmethod
    def deletar_Vendedor(cls, id):
        vendedor = Vendedor.objects.get(pk=id)
        vendedor.delete()