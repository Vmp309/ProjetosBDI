from Client import Cliente
from Seller import Vendedor
from gerenciadorBD import GerenciadorBD

class MenuVenda():
    
    def __init__(self, gerenciador, cliente):
        self.gerenciador = gerenciador
        self.cliente = cliente
        self.carrinho = []

    def exibir_menu(self):
        vendedores = self.gerenciador.mostrar_vendedores()
        for vendedor in vendedores:
            self.gerenciador.mostrar_vendedor(vendedor)
        input("Escolha o vendedor que deve concluir a venda.\n-> ")