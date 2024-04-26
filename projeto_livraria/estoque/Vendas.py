from .models import Cliente 
from .models import Venda
from .models import Livro

class Vendas:
    
    @classmethod
    def addIntem(self,idVenda,idLivro):
        venda = Venda.objects.get(pk=idVenda)
        livro = Livro.objects.get(pk=idLivro)
        venda.livros.append(idLivro)
        venda.valorTotal+=livro.valor
        
    @classmethod
    def removerIntem(self,idVenda,idLivro):
        venda = Venda.objects.get(pk=idVenda)
        livro = Livro.objects.get(pk=idLivro)
        venda.valorTotal-=livro.valor
        venda.livros.remove(idLivro)
        
        
    @classmethod
    def pix(self,idVenda,desconto):
        venda = Venda.objects.get(pk=idVenda)
        venda.formaPagamento="pix"
        Vendas.desconto(idVenda)
        print("pagando com o pix")
        venda.Pagconcluido=True
     
    @classmethod    
    def cartao(self,idVenda):
        venda = Venda.objects.get(pk=idVenda)
        tipo = input("Digite 1 para Credito\n Digite 2 para Debito")
        if(tipo == 1):
            venda.formaPagamento="credito"
            Vendas.desconto(idVenda)
            print("pagando com Credito")
        elif(tipo == 2):
            venda.formaPagamento="debito"
            Vendas.desconto(idVenda)
            print("pagando com Debito")
        venda.Pagconcluido=True
        
    @classmethod
    def berries(self,idVenda):
        venda = Venda.objects.get(pk=idVenda)
        venda.formaPagamento="berries"
        Vendas.desconto(idVenda)
        print("pagando em berries")
        venda.Pagconcluido=True
        
    @classmethod
    def boleto(self,idVenda):
        venda = Venda.objects.get(pk=idVenda)
        
        venda.formaPagamento="boleto"
        Vendas.desconto(idVenda)
        print("pagando com boleto")
        venda.Pagconcluido=True 
        
    @classmethod
    def desconto(self, idVenda):
        venda = Venda.objects.get(pk=idVenda)
        desconto=0.00
        cliente = Cliente.objects.get(pk=venda.Cliente)
        if(cliente.isflamengo==True):
            desconto+=0.05
        if(cliente.onePiece==True):
            desconto+=0.05
        if (cliente.endereco == "mari"):
            desconto+=0.05
        
        valDesconto = venda.valorTotal-(venda.valorTotal*desconto)
        venda.valorDesconto= valDesconto
        print("total: ",venda.valorTotal)
        if venda.valorDesconto < venda.valorTotal :
            print("total com desconto: " , venda.valorDesconto)
        
               
    @classmethod
    def pagamento(self,idCliente,idvenda ,formaPagamento):
        venda = Venda.objects.get(pk=idvenda)
        venda.Cliente= Cliente.objects.get(pk=idCliente)
        
        
        if(formaPagamento == 0):
            Vendas.pix(self,idvenda)
        elif(formaPagamento == 1):
            Vendas.cartao(self,idvenda)
        elif(formaPagamento == 2 ):
            Vendas.berries(self,idvenda)
        elif(formaPagamento == 3 ):
            Vendas.boleto(self,idvenda)
            
    def obterVenda(self,id):
        return Venda.objects.get(pk=id)       
