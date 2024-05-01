from .models import Cliente 
from .models import Venda
from .models import Livro
from django.db import connection

class Vendas:
    
    @classmethod
    def addIntem(self,idVenda,idLivro,qtd):
        venda = Venda.objects.get(pk=idVenda)
        livro = Livro.objects.get(pk=idLivro)
        if (livro.pk == idLivro) and (livro.quantidade_em_estoque>0) and (not(idLivro in venda.livros)):
            qtd += venda.livros[idLivro]
            venda.livros[idLivro]= qtd
            venda.valorTotal+=livro.valor
        else:
            print("Livro indisponivel")
        
    @classmethod
    def removerIntem(self,idVenda,idLivro):
        venda = Venda.objects.get(pk=idVenda)
        livro = Livro.objects.get(pk=idLivro)
        if venda.livros != None and livro.pk == idLivro and idLivro in venda.livros: 
            venda.livros.remove(idLivro)
            venda.valorTotal-=livro.valor
        else:
            print("carrinho vazio ")
        
    @classmethod
    def pix(self,idVenda):
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
        cliente = Cliente.objects.get(pk=venda.cliente)
        if(cliente.isflamengo==True):
            desconto+=0.05
        if(cliente.onePiece==True):
            desconto+=0.05
        if (cliente.endereco == "souza"):
            desconto+=0.05
        
        valDesconto = venda.valorTotal-(venda.valorTotal*desconto)
        venda.valorDesconto= valDesconto
        print("total: ",venda.valorTotal)
        if venda.valorDesconto < venda.valorTotal :
            print("total com desconto: " , venda.valorDesconto)
             
    @classmethod
    def pagamento(self,idCliente,idvenda ,formaPagamento):
        venda = Venda.objects.get(pk=idvenda)
        venda.cliente= Cliente.objects.get(pk=idCliente)
        if venda.livros != None:
            if(formaPagamento == 0):
                Vendas.pix(self,idvenda)
            elif(formaPagamento == 1):
                Vendas.cartao(self,idvenda)
            elif(formaPagamento == 2 ):
                Vendas.berries(self,idvenda)
            elif(formaPagamento == 3 ):
                Vendas.boleto(self,idvenda)
    
    @classmethod
    def cadastrarVenda(self,idCliente, idVendedor):
        venda = Venda(cliente=idCliente,vendedor=idVendedor)
        venda.save
        return venda.pk
            
    def obterVenda(self,id):
        return Venda.objects.get(pk=id)       
    
    def gerarRelatorio(self, dataInicio, dataFim):
        with connection.cursor() as cursor:
<<<<<<< Updated upstream
            relatorio = cursor.callproc(gerar_relatório_de_vendas, dataInicio, dataFim)
            return relatorio
=======
            cursor.callproc('storeProcedureVendas.sql')
            # Optionally fetch results using cursor.fetchall() or cursor.fetchone()
>>>>>>> Stashed changes

