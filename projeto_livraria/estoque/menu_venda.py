from menu_busca import MenuBusca
from Vendas import Vendas
from GerenciadorCliente import  GerenciadorCliente
from GerenciadorVendedor import  GerenciadorVendedor

classe MenuVenda:
    cliente =None
    venda = None
    vendedor=None
    
    def iniciar_carrinho(self, cliente, vendedor):
        self.cliente = GerenciadorCliente.obter_Cliente(cliente)
        self.vendedor = GerenciadorVendedor.obter_vendedor(vendedor)
        self.venda = Vendas.cadastrarVenda(self.cliente , self.vendedor)
        return venda
     
    def add_carrinho(self ):
        livro = MenuBusca.exibir_menu("operação_cliente")
        qtd = input("Quantas Unidades\n>")
        self.venda.addIntem(self.venda.pk,livro,qtd)
    
    def remove_carrinho(self,livro):
        self.venda.removerIntem(self.venda.pk,livro)
        print("removendo",livro)
        
    def pagamento(self ):
        print("Valor total da compra: ", self.venda.valorTotal)
        print("Digite 0 para pagar com pix")
        print("Digite 1 para pagar com cartão")
        print("Digite 2 para pagar com beries")
        print("Digite 3 para pagar com boleto")
        formaPagamento = input(">")
        self.venda.pagamento(self.venda.pk,self.cliente.username, formaPagamento)
        print("Pagamento concuido!")
        