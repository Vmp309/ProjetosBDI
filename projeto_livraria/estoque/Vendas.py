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
        total = venda.valorTotal-(venda.valorTotal*desconto)
        
        desconto(idVenda,desconto)
        print("pagando com o pix")
        venda.Pagconcluido=True
     
    @classmethod    
    def cartao(self,idVenda,desconto):
        venda = Venda.objects.get(pk=idVenda)
        total = venda.valorTotal-(venda.valorTotal*desconto)
        tipo = input("Digite 1 para Credito\n Digite 2 para Debito")
        if(tipo == 1):
            venda.formaPagamento="credito"
            desconto(idVenda,desconto)
            print("pagando com Credito")
        elif(tipo == 2):
            venda.formaPagamento="debito"
            desconto(idVenda,desconto)
            print("pagando com Debito")
        venda.Pagconcluido=True
        
    @classmethod
    def berries(self,idVenda,desconto):
        venda = Venda.objects.get(pk=idVenda)
        total = venda.valorTotal-(venda.valorTotal*desconto)
        venda.formaPagamento="berries"
        
        desconto(idVenda,desconto)
        print("pagando em berries")
        venda.Pagconcluido=True
        
    @classmethod
    def boleto(self,idVenda,desconto):
        venda = Venda.objects.get(pk=idVenda)
        
        venda.formaPagamento="boleto"
        desconto(idVenda,desconto)
        print("pagando com boleto")
        venda.Pagconcluido=True 
        
    @classmethod
    def desconto(self, idVenda,desconto):
        venda = Venda.objects.get(pk=idVenda)
        valDesconto = venda.valorTotal-(venda.valorTotal*desconto)
        venda.valorDesconto= valDesconto
        print("total: ",venda.valorTotal)
        if venda.valorDesconto < venda.valorTotal :
            print("total com desconto: " , venda.valorDesconto)
        
               
    @classmethod
    def pagamento(self,idCliente,idvenda ,formaPagamento):
        desconto=0.00
        cliente = Cliente.objects.get(pk=idCliente)
        if(cliente.isflamengo==True):
            desconto+=0.05
        if(cliente.onePiece==True):
            desconto+=0.05
        if (cliente.endereco == "mari"):
            desconto+=0.05
        
        if(formaPagamento == 0):
            Vendas.pix(self,idvenda,desconto)
        elif(formaPagamento == 1):
            Vendas.cartao(self,idvenda,desconto)
        elif(formaPagamento == 2 ):
            Vendas.berries(self,idvenda,desconto)
        elif(formaPagamento == 3 ):
            Vendas.boleto(self,idvenda,desconto)
            
    def obterVenda(self,id):
        return Venda.objects.get(pk=id)       
