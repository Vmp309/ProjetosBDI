from Client import Cliente
from Seller import Vendedor
from gerenciadorBD import GerenciadorBD

class MenuVenda():
    
    def __init__(self, gerenciador, cliente):
        self.gerenciador = gerenciador
        self.cliente = cliente
        self.vendedor = Vendedor(cpf=None, username=None, password=None, nome=None)
        self.opcao = 0
        self.carrinho = []

    def exibir_menu(self):
        vendedores = self.gerenciador.mostrar_vendedores()
        for vendedor in vendedores:
            self.gerenciador.mostrar_vendedor(vendedor)
        user_vendedor = input("Escolha o vendedor que deve concluir a venda\n(Username)-> ")
        if(self.gerenciador.verificar_user_Vendedor(user_vendedor)):
            self.vendedor = self.gerenciador.retornar_vendedor(user_vendedor)
            self.exibir_menu2()
        else:
            print("Acho que você digitou errado...")

    def exibir_menu2(self):
        print("----- Vendedor :" + self.vendedor.username + "-----\n")
        print("1) Adicionar livro no carrinho.")
        print("2) Remover livro do carrinho.")
        print("3) Comprar.")
        print("4) Cancelar compra.")
        self.opcao = input("-> ")
        if self.opcao == "1":
            pass
        elif self.opcao == "2":
            pass
        elif self.opcao == "3":
            pass
        elif self.opcao == "4":
            pass

        return

