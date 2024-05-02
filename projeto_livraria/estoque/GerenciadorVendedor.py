from .models import Vendedor

class GerenciadorVendedor:
    @classmethod
    def listar_Vendedor(cls):
        return Vendedor.objects.all()

    @classmethod
    def cadastrar_Vendedor(cls,username, password, nome, cpf):
        vendedor = Vendedor(username=username, password=password, nome=nome, cpf=cpf)
        vendedor.save()
        return vendedor

    @classmethod
    def obter_vendedor(cls, pk):
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

    def login(cls, username, password):
        
        try:
            user = Vendedor.objects.get(username=username, password=password)
        
        except:
            return "Nome de usuário ou senha inválidos!"
        
        else:
            return True, user 